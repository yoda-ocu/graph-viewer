# -*- coding: utf-8 -*-
"""サンプルデータの表示"""
import os
import argparse
import traceback
import pandas as pd

supported_format = ['zip', 'pickle', 'pkl']

def cui_mode(args):
    """指定された引数でCUI描画する

        args            : コマンドライン引数の一覧
        ===========================================
        .mode (str)         : 描画モード debug時はサンプルデータを用いる
        .max_rows (int)     : 表示行数
        .max_cols (int)     : 表示列数
        .describe (bool)    : 統計情報の表示/非表示
        .input (list)       : 表示するファイルリスト
        
        
    Note:
        args.input = None or [] の場合、ファイル名は手打ち入力画面になる
        args.inputで複数のファイルを指定した場合は最初の読み込み可能ファイルのみを表示する
    """
    
    print("CUI MODE")

    if args.mode == 'debug':
        args.input = ['./data/SampleData1.zip']
    
    pd.set_option('display.max_rows', args.max_rows)
    pd.set_option('display.max_columns', args.max_cols)

    while args.input is None or len(args.input) == []:
        file_path = input("開くファイルを入力 >> ")
        if os.path.isfile(file_path):
            args.input = [file_path]        
    
    print()

    for file in args.input:                        
        if not os.path.isfile(file): continue

        if not os.path.splitext(file)[1] not in supported_format:                
            print("読み込みに対応していないファイルです : {}".format(file))
            print("対応フォーマット : {}".format(supported_format))
            print()
            continue

        try:
            print("ファイル : {}".format(file))
            df = pd.read_pickle(file)
            print(df)
            if args.describe: print(); pd.set_option('display.max_rows', None); print(df.describe())
            return
        except:
            print("ファイルの読み込みに失敗しました : {}".format(file))
            print()
            continue

def gui_mode(args):
    print("GUI MODE")
    print(args)

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='サンプルデータの表示')        
    parser.add_argument('-m', '--mode', help='表示のCUI/GUIの切り替え', choices=['CUI', 'GUI', 'debug'], default='debug')
    parser.add_argument('-mr','--max_rows', help='CUIモードにおける表示する行数', default='7', type=int)
    parser.add_argument('-mc','--max_cols', help='CUIモードにおける表示する列数', default='7', type=int)
    parser.add_argument('-d','--describe', help="CUIモードに置いて統計量の表示", action='store_false')
    parser.add_argument('-i', '--input', help='表示するファイル', nargs='*')
    
    args = parser.parse_args()

    if args.mode == 'debug':
        gui_mode(args)            
    elif args.mode == 'CUI':
        try:
            cui_mode(args)
        except:            
            traceback.print_exc()
        input("press key to quit >>")
    elif args.mode == 'GUI':
        gui_mode(args)
    

