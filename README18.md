# Monitoramento de Queimadas na Amazônia

Este projeto tem como objetivo monitorar as queimadas na Amazônia e apresentar informações diárias atualizadas sobre os focos de incêndio detectados. Abaixo, você pode visualizar as queimadas mais recentes, com detalhes sobre localização, satélite que realizou a detecção, e outros fatores relevantes.

## Estrutura dos Dados

Cada entrada na tabela representa um foco de incêndio com as seguintes informações:

- **ID:** Identificador único do foco de incêndio.
- **Latitude/Longitude:** Coordenadas geográficas do foco detectado. Para visualizar o local exato, insira estas coordenadas no Google Maps ou outro aplicativo de mapas.
- **Data/Hora GMT:** Data e hora da detecção em formato GMT (Greenwich Mean Time).
- **Satélite:** Satélite responsável pela detecção do foco de incêndio.
- **Município, Estado e País:** Localização administrativa do foco detectado.
- **Dias sem Chuva:** Número de dias consecutivos sem precipitação na região, o que pode indicar um aumento no risco de incêndio.
- **Precipitação:** Quantidade de chuva (em milímetros) registrada no local.
- **Risco de Fogo:** Índice que indica a probabilidade de ocorrência de incêndio, baseado em fatores como condições climáticas e quantidade de combustível disponível.
- **Bioma:** Bioma onde o foco foi identificado, como Amazônia, Cerrado, ou Mata Atlântica.
- **FRP (Fire Radiative Power):** Potência radiativa do fogo, que mede a intensidade do incêndio. Focos com FRP mais alto indicam incêndios mais intensos.

## Visualização Gráfica

Se você deseja visualizar de forma gráfica onde as queimadas estão ocorrendo, copie as coordenadas de latitude e longitude mais recentes e cole no Google Maps. Isso permite uma compreensão espacial mais clara da distribuição dos focos de incêndio. Alternativamente, você também pode usar a descrição de localização (Município, Estado e País) para identificar a região afetada.

## Informação Adicional

As queimadas na Amazônia não apenas afetam a biodiversidade local, mas também têm implicações globais, contribuindo para o aquecimento global e a emissão de gases de efeito estufa. O monitoramento contínuo é essencial para entender e mitigar os impactos desses incêndios, além de auxiliar na gestão de políticas ambientais e ações de preservação.

## Dados Diários - Página 18

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 7b558a8c-2191-3202-88e1-6a0964f012a9 | -15.16928 | -46.40545 | 2025-09-30 03:28:00 | NPP-375D | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 66424098-d11c-3d30-8cb4-2d0cf8c5bb15 | -11.41925 | -44.90354 | 2025-09-30 03:28:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| e0f108c2-0d91-3760-98d7-c38dbc3edbc2 | -10.18627 | -44.90841 | 2025-09-30 03:28:00 | NPP-375D | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 67.4 |
| 95474e1b-d3e3-3a0c-ada8-ffb55c5ee360 | -12.95735 | -46.40358 | 2025-09-30 03:28:00 | NPP-375D | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| a3ad8d79-df60-31be-b3b8-22b7f39f6425 | -14.7166 | -45.674 | 2025-09-30 03:28:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 61d052f6-5802-34ff-9cbd-16129af32dff | -15.04733 | -46.96844 | 2025-09-30 03:28:00 | NPP-375D | VILA BOA | GOIÁS | Brasil | 5222203 | 52 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 20228fd1-0e1d-35f5-9955-a9f114ecd9dd | -11.93951 | -43.91998 | 2025-09-30 03:28:00 | NPP-375D | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| c95873d2-c561-31ce-8f3c-8d4d089da3ee | -14.16798 | -44.3101 | 2025-09-30 03:28:00 | NPP-375D | FEIRA DA MATA | BAHIA | Brasil | 2910776 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 0ab362e8-2c1f-3e62-a1ab-05cf841b35f6 | -11.41823 | -44.90709 | 2025-09-30 03:28:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 4d05f0e8-4af4-39d6-a16f-ac89f7a90aa7 | -14.72422 | -45.22284 | 2025-09-30 03:28:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| f364eeb2-ed39-39b6-85b6-0769020e3266 | -10.18467 | -44.88094 | 2025-09-30 03:28:00 | NPP-375D | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 6.9 |
| efcdbd57-9c46-38a6-99ad-d2ad5116fcb9 | -13.02568 | -42.81195 | 2025-09-30 03:28:00 | NPP-375D | MACAÚBAS | BAHIA | Brasil | 2919801 | 29 | 33 | nan | nan | nan | Caatinga | 16.4 |
| eefaa810-417a-3a2e-9bf9-ed5a7ea5d04b | -10.53003 | -43.63875 | 2025-09-30 03:28:00 | NPP-375D | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 85bd2ac4-fbb8-3f44-8c95-a05a41c14469 | -11.36972 | -45.07389 | 2025-09-30 03:28:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 2eb60a1e-46c4-3db4-8e16-e9cafbb8cedb | -11.45919 | -44.98409 | 2025-09-30 03:28:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.9 |
| b72874a1-0fdf-3fa2-92c2-46fafe629c6a | -10.52896 | -43.64424 | 2025-09-30 03:28:00 | NPP-375D | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| cdb0e22b-396a-3035-96d6-1ae462f8fe8b | -13.63324 | -42.53637 | 2025-09-30 03:28:00 | NPP-375D | TANQUE NOVO | BAHIA | Brasil | 2931053 | 29 | 33 | nan | nan | nan | Caatinga | 0.4 |
| dc726f1d-8d4c-3a84-972c-56d4ec2f2856 | -11.49077 | -43.52034 | 2025-09-30 03:28:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 7d8b1c55-7555-3dc2-b505-161a23dc7b11 | -14.74093 | -45.66655 | 2025-09-30 03:28:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 12.0 |
| 44c971a3-9fa2-3491-b95c-b89120c708ac | -11.69217 | -44.31171 | 2025-09-30 03:28:00 | NPP-375D | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 56aa893f-eacd-3989-8ca1-86e11cbc63b5 | -14.72629 | -45.66921 | 2025-09-30 03:28:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 7.3 |
| 6027b80f-6179-3f83-9856-29946edce314 | -15.29745 | -46.41727 | 2025-09-30 03:28:00 | NPP-375D | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 2.2 |
| b4cdc6cc-d41c-363e-9fca-c5c88c644382 | -14.76238 | -45.76138 | 2025-09-30 03:28:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| c0028a01-5f94-3f50-8c19-639deb014cb4 | -13.65727 | -43.36163 | 2025-09-30 03:28:00 | NPP-375D | BOM JESUS DA LAPA | BAHIA | Brasil | 2903904 | 29 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 1d2bcce8-979c-3623-9329-69d74bc8dbe4 | -13.59885 | -43.46334 | 2025-09-30 03:28:00 | NPP-375D | MALHADA | BAHIA | Brasil | 2920205 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| e28b37e9-40a0-37d8-a0c6-208b01bba698 | -14.64884 | -46.96526 | 2025-09-30 03:28:00 | NPP-375D | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 3.4 |
| c452e7c3-65c0-3e21-9973-bdf329f2d675 | -13.86262 | -44.41631 | 2025-09-30 03:28:00 | NPP-375D | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| a2a24859-4ad9-33df-a871-1226a7e6ce69 | -10.1932 | -44.90986 | 2025-09-30 03:28:00 | NPP-375D | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 10.5 |
| 666d9ba6-aedc-3ac1-a8f6-7a8101e15970 | -10.18108 | -44.9086 | 2025-09-30 03:28:00 | NPP-375D | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 21.9 |
| b478fced-6caa-377a-a101-c9075090bc95 | -11.74955 | -44.75056 | 2025-09-30 03:28:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 4.8 |
| b4abd351-c1ca-3110-9d90-ce443aff61ce | -11.43601 | -44.95915 | 2025-09-30 03:28:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 3475af07-69ef-3cf7-a2c8-2bc4e3372b68 | -15.32641 | -43.80235 | 2025-09-30 03:28:00 | NPP-375D | JAÍBA | MINAS GERAIS | Brasil | 3135050 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| d2b32486-61ed-3a30-bcac-75f9e14a1ea5 | -12.58437 | -41.28991 | 2025-09-30 03:28:00 | NPP-375D | ANDARAÍ | BAHIA | Brasil | 2901304 | 29 | 33 | nan | nan | nan | Caatinga | 5.2 |
| 20708acf-47ef-3d0d-8323-3308393071d4 | -13.65818 | -43.35715 | 2025-09-30 03:28:00 | NPP-375D | BOM JESUS DA LAPA | BAHIA | Brasil | 2903904 | 29 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 6ab7e844-5469-3b81-b7fd-94d2559699b4 | -14.74222 | -45.66071 | 2025-09-30 03:28:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 12.0 |
| 05ac413c-8869-3c80-acf1-9a93ec76ed57 | -10.18895 | -44.89528 | 2025-09-30 03:28:00 | NPP-375D | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 38.1 |
| bfd12f59-6e34-3129-b819-44d009c994ff | -14.04155 | -42.15364 | 2025-09-30 03:28:00 | NPP-375D | LAGOA REAL | BAHIA | Brasil | 2918753 | 29 | 33 | nan | nan | nan | Caatinga | 3.0 |
| 95166fe3-b868-32e7-b21e-ecc534531fb0 | -14.7476 | -45.66816 | 2025-09-30 03:28:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 12.0 |
| 5801f6ea-8b36-3e39-bfcb-a88d9add63e7 | -15.93092 | -43.30931 | 2025-09-30 03:28:00 | NPP-375D | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 7e57eaef-fb1f-3a8d-b6cb-efd20e73109b | -9.57424 | -40.3558 | 2025-09-30 03:28:00 | NPP-375D | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 5.0 |
| 0db54d21-b290-3197-81c8-575516c388bf | -11.45341 | -44.9777 | 2025-09-30 03:28:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 303ea35a-6bdf-3bb7-8213-ecc0263ea061 | -11.43119 | -44.94797 | 2025-09-30 03:28:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| e3dafced-5197-323f-b7bf-5d0d536d4bf2 | -8.54358 | -44.67398 | 2025-09-30 03:28:00 | NPP-375D | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 3.0 |
| a9b2045f-e8de-3c54-b84a-add7c98beb44 | -14.08379 | -44.08878 | 2025-09-30 03:28:00 | NPP-375D | FEIRA DA MATA | BAHIA | Brasil | 2910776 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 78757e7a-8eb2-3f99-947b-67be4dc0c0f9 | -11.43721 | -44.95323 | 2025-09-30 03:28:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 3446ab3a-f5b7-34ed-b0e5-77385a2b6595 | -11.44343 | -44.95739 | 2025-09-30 03:28:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 174a2d74-4d78-3f75-a0ab-5ebdce75ad19 | -15.83169 | -42.02328 | 2025-09-30 03:28:00 | NPP-375D | TAIOBEIRAS | MINAS GERAIS | Brasil | 3168002 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| b63218ab-826b-317c-b54d-d42f6320a6c6 | -14.04224 | -42.15433 | 2025-09-30 03:28:00 | NPP-375D | LAGOA REAL | BAHIA | Brasil | 2918753 | 29 | 33 | nan | nan | nan | Caatinga | 2.6 |
| af381256-0b5f-3d4f-9396-c09c163a55db | -15.17493 | -46.41257 | 2025-09-30 03:28:00 | NPP-375D | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 4.1 |
| c63a43a8-6795-3f4a-80eb-4e4d1090883f | -14.64997 | -46.9636 | 2025-09-30 03:28:00 | NPP-375D | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| f349420b-bdc6-331e-82f7-3aa06f61c8a7 | -11.72222 | -44.44944 | 2025-09-30 03:28:00 | NPP-375D | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 8.3 |
| becfa447-4b01-30ba-bce6-f7dfd7aec9ed | -15.52675 | -39.88207 | 2025-09-30 03:28:00 | NPP-375D | POTIRAGUÁ | BAHIA | Brasil | 2925402 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| 30c4dffb-2644-33f4-a77c-5e4eba491fab | -10.19026 | -44.8889 | 2025-09-30 03:28:00 | NPP-375D | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 38.1 |
| 82c515b2-86eb-3b1b-8f63-09a906f0f113 | -15.8324 | -42.01978 | 2025-09-30 03:28:00 | NPP-375D | TAIOBEIRAS | MINAS GERAIS | Brasil | 3168002 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 8caa5f1a-73ee-3993-ae72-840565a77ea6 | -14.73296 | -45.67082 | 2025-09-30 03:28:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 7.3 |
| 579698fe-3523-3bff-a493-016b4dcc9939 | -14.65598 | -46.96713 | 2025-09-30 03:28:00 | NPP-375D | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 66d2ca12-bbe9-3724-a2fc-8bf24cbd6799 | -13.01336 | -44.1176 | 2025-09-30 03:28:00 | NPP-375D | SANTANA | BAHIA | Brasil | 2928208 | 29 | 33 | nan | nan | nan | Cerrado | 4.6 |
| c95de73d-fb9d-36d3-9d33-bfa7d667fa4f | -15.29904 | -46.41007 | 2025-09-30 03:28:00 | NPP-375D | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 3.0 |
| cef181ca-8a87-3bfe-b4eb-01bd698c5d68 | -15.32549 | -43.80679 | 2025-09-30 03:28:00 | NPP-375D | JAÍBA | MINAS GERAIS | Brasil | 3135050 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 5409ab00-c816-39fd-90f6-4cad2fb194f6 | -15.17001 | -46.41203 | 2025-09-30 03:28:00 | NPP-375D | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 0444846b-c817-33ff-afb8-71a9ea49bd40 | -14.65542 | -46.97293 | 2025-09-30 03:28:00 | NPP-375D | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 130852b7-f5dd-35fa-908c-66ae38000198 | -11.49299 | -43.52186 | 2025-09-30 03:28:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| fd663cc8-52e8-3e56-97ab-4c071de33b7b | -10.53544 | -43.64523 | 2025-09-30 03:28:00 | NPP-375D | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 8484f40f-ae02-3cb6-896a-a9c1764bffca | -10.8061 | -45.36163 | 2025-09-30 03:28:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 398dc1de-45f7-3e50-9254-2533afee4459 | -14.72454 | -45.66976 | 2025-09-30 03:28:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 5.2 |
| c14211d8-3764-3293-9b2e-9ad0e2169456 | -11.67671 | -44.29543 | 2025-09-30 03:28:00 | NPP-375D | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| cbed31ec-daf0-3258-9d2c-9864c06e4444 | -13.01044 | -44.12126 | 2025-09-30 03:28:00 | NPP-375D | SANTANA | BAHIA | Brasil | 2928208 | 29 | 33 | nan | nan | nan | Cerrado | 6.4 |
| efe13bce-b578-335c-9f03-1c8762573240 | -11.36961 | -45.0703 | 2025-09-30 03:28:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 4.5 |
| a43a2a56-2eb7-3e5c-a444-e48ef913678d | -12.58233 | -41.29052 | 2025-09-30 03:28:00 | NPP-375D | ANDARAÍ | BAHIA | Brasil | 2901304 | 29 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 41d98d66-9677-3dd2-9a80-5145c0e6a9db | -14.45021 | -46.36227 | 2025-09-30 03:28:00 | NPP-375D | SÍTIO D'ABADIA | GOIÁS | Brasil | 5220702 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 9c40b394-a52f-3cb2-be87-6f0a5fa30873 | -13.66973 | -44.31114 | 2025-09-30 03:28:00 | NPP-375D | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 7.3 |
| d282d1d3-f055-327c-acc0-28d4b2adabc7 | -11.7134 | -44.44144 | 2025-09-30 03:28:00 | NPP-375D | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 3.7 |
| bb0e422d-95ef-3628-baed-19feeefb463f | -15.17614 | -46.41721 | 2025-09-30 03:28:00 | NPP-375D | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 498a13ef-5e46-363a-9a8b-ca4948578a9f | -13.86154 | -44.42146 | 2025-09-30 03:28:00 | NPP-375D | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 61fbe389-347d-338a-8881-5bd9c7d20f47 | -14.72541 | -45.2174 | 2025-09-30 03:28:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 69c12e43-8fe5-3576-9e41-68cedd2b3738 | -12.58768 | -41.29164 | 2025-09-30 03:28:00 | NPP-375D | ANDARAÍ | BAHIA | Brasil | 2901304 | 29 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 284d32cf-e481-3ef2-9750-3da2b1ba82d1 | -15.33037 | -46.26574 | 2025-09-30 03:28:00 | NPP-375D | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| cc62f33b-b63e-3ea5-9c21-ee4605da1a2d | -13.23717 | -43.37695 | 2025-09-30 03:28:00 | NPP-375D | BOM JESUS DA LAPA | BAHIA | Brasil | 2903904 | 29 | 33 | nan | nan | nan | Caatinga | 5.3 |
| e506cca0-f378-3767-a0b4-44de16f32c6a | -11.48776 | -43.51557 | 2025-09-30 03:28:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 26edd1a1-fcc4-3229-b3f0-414d50e5c671 | -13.23152 | -43.37194 | 2025-09-30 03:28:00 | NPP-375D | BOM JESUS DA LAPA | BAHIA | Brasil | 2903904 | 29 | 33 | nan | nan | nan | Caatinga | 3.2 |
| 217c1427-d37d-3edd-9d36-757b309b4f4c | -12.58833 | -41.28823 | 2025-09-30 03:28:00 | NPP-375D | ANDARAÍ | BAHIA | Brasil | 2901304 | 29 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 1abe77c3-efcd-37cf-9be7-718e9fc5107f | -14.72065 | -45.23916 | 2025-09-30 03:28:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 19350099-5c93-38ba-9b2a-5b0e35b0dd5b | -9.57955 | -40.35682 | 2025-09-30 03:28:00 | NPP-375D | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 2.4 |
| f0713823-ab57-32b1-bd2b-6b9dd929463e | -16.82726 | -39.3352 | 2025-09-30 03:28:00 | NPP-375D | PORTO SEGURO | BAHIA | Brasil | 2925303 | 29 | 33 | nan | nan | nan | Mata Atlântica | 2.9 |
| 410a846f-4e52-3c4b-91ff-6611c3137f12 | -10.7599 | -45.37197 | 2025-09-30 03:28:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 246b9943-e36a-3f70-988a-109fda8744a2 | -11.94029 | -43.92248 | 2025-09-30 03:28:00 | NPP-375D | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 70c2cac0-6cbc-3470-8df5-816351227c84 | -10.18336 | -44.88732 | 2025-09-30 03:28:00 | NPP-375D | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 38.1 |
| 38907cd0-2365-3091-8c6c-271ea7b8516d | -11.49176 | -43.51537 | 2025-09-30 03:28:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 68c1ede9-8595-3a63-aeb5-ef82a57b6914 | -11.49703 | -43.52167 | 2025-09-30 03:28:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 87f2c6ad-30df-3be1-8edc-754c964d27cb | -13.6272 | -42.53276 | 2025-09-30 03:28:00 | NPP-375D | TANQUE NOVO | BAHIA | Brasil | 2931053 | 29 | 33 | nan | nan | nan | Caatinga | 1.6 |
| c34e0944-ca6a-3eff-a2f9-0e559ccba90f | -13.63289 | -42.53389 | 2025-09-30 03:28:00 | NPP-375D | TANQUE NOVO | BAHIA | Brasil | 2931053 | 29 | 33 | nan | nan | nan | Caatinga | 1.1 |
| ad271a01-1087-3398-83a5-6da67a6cc5b0 | -11.94146 | -43.91688 | 2025-09-30 03:28:00 | NPP-375D | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 10915f1f-8259-3e5d-a1f6-abbdd4cc3b0f | -11.75746 | -44.74607 | 2025-09-30 03:28:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 44902e37-c9c5-3157-8222-61267a74481a | -11.23468 | -39.41212 | 2025-09-30 03:28:00 | NPP-375D | SANTALUZ | BAHIA | Brasil | 2928000 | 29 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 9630d489-b2eb-39ea-ab8d-67cb3579a717 | -14.64003 | -46.9709 | 2025-09-30 03:28:00 | NPP-375D | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| ab98a0e0-f626-3b04-9c54-d9736e37fc23 | -11.708 | -44.43425 | 2025-09-30 03:28:00 | NPP-375D | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 0501252a-279b-30cf-b13b-22e89e3569c8 | -8.5449 | -44.6673 | 2025-09-30 03:28:00 | NPP-375D | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 10180143-d2b3-37be-925d-1078c5d6f318 | -10.19154 | -44.88263 | 2025-09-30 03:28:00 | NPP-375D | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 6.9 |
| ae9dee2b-2531-3c35-8da0-74dcc6c0b84b | -11.37092 | -45.06809 | 2025-09-30 03:28:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 25367b5c-d69c-3f58-957a-8b6ef35b868a | -14.73963 | -45.67243 | 2025-09-30 03:28:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 34.4 |


[Clique aqui para ver as próximas entradas](README19.md)
