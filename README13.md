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

## Dados Diários - Página 13

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| fa215af5-9ccc-383c-aa90-8d3071682a97 | -16.71988 | -46.40189 | 2026-08-08 04:27:00 | NPP-375D | DOM BOSCO | MINAS GERAIS | Brasil | 3122470 | 31 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 616e63f5-44ac-3bee-9ada-652216ce6b68 | -19.74421 | -45.96324 | 2026-08-08 04:27:00 | NPP-375D | CÓRREGO DANTA | MINAS GERAIS | Brasil | 3119807 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| eae5409b-7c25-3843-92c9-83fb26eb8123 | -18.36569 | -50.70177 | 2026-08-08 04:27:00 | NPP-375D | QUIRINÓPOLIS | GOIÁS | Brasil | 5218508 | 52 | 33 | nan | nan | nan | Cerrado | 5.7 |
| fd8ecd8f-a7c8-3c06-a8f1-ae379008a464 | -15.16824 | -52.74714 | 2026-08-08 04:27:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 6.6 |
| dd908a8a-f491-3f1e-bbde-86c1a9b30978 | -14.93377 | -48.26771 | 2026-08-08 04:27:00 | NPP-375D | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 3.6 |
| f54311e0-29b7-3c06-80e9-52436b9c9780 | -12.60939 | -52.46212 | 2026-08-08 04:27:00 | NPP-375D | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 59c5a0d4-5d8c-3f6b-91c2-52e190b22f18 | -21.36971 | -45.13328 | 2026-08-08 04:27:00 | NPP-375D | CARMO DA CACHOEIRA | MINAS GERAIS | Brasil | 3113909 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 952a927e-63d0-3a94-998a-c779fc013f9b | -14.32013 | -54.98837 | 2026-08-08 04:27:00 | NPP-375D | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 4.0 |
| c81aa37e-a79f-38b3-8334-6ef49000f06a | -18.34832 | -50.73011 | 2026-08-08 04:27:00 | NPP-375D | QUIRINÓPOLIS | GOIÁS | Brasil | 5218508 | 52 | 33 | nan | nan | nan | Cerrado | 48.3 |
| f43842db-3590-30b3-b55e-cb157d8ce6db | -14.92886 | -48.25342 | 2026-08-08 04:27:00 | NPP-375D | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 4.2 |
| e51b3574-1769-39f1-8ce6-68513fdb77e3 | -14.34341 | -54.98614 | 2026-08-08 04:27:00 | NPP-375D | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 3.4 |
| c5e674d6-6a2e-37f1-9f0a-357c024dfd27 | -15.16111 | -52.74857 | 2026-08-08 04:27:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 18ef43d2-a00d-3832-9022-46361bffb08b | -20.8878 | -43.15702 | 2026-08-08 04:27:00 | NPP-375D | SENADOR FIRMINO | MINAS GERAIS | Brasil | 3165701 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| 01553235-e683-3041-88ec-74319efce21d | -14.93312 | -48.25012 | 2026-08-08 04:27:00 | NPP-375D | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 6.9 |
| f7ffd546-f0ad-3862-a520-99e64f66bdbf | -15.15276 | -52.74146 | 2026-08-08 04:27:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 5a85085c-0d6c-339e-bbdb-dbcb9d34ce80 | -19.63646 | -46.20119 | 2026-08-08 04:27:00 | NPP-375D | CAMPOS ALTOS | MINAS GERAIS | Brasil | 3111507 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 86fd12cb-4406-3264-b351-67418673f1f9 | -14.42181 | -45.66439 | 2026-08-08 04:27:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 3.2 |
| e9c7ee5d-34e7-3e34-8a18-0a664e7f7de3 | -18.37475 | -49.2689 | 2026-08-08 04:27:00 | NPP-375D | ITUMBIARA | GOIÁS | Brasil | 5211503 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 9d5672e7-7833-3664-91be-4467b36da0ce | -13.77836 | -48.5011 | 2026-08-08 04:27:00 | NPP-375D | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 430703f2-51a1-3a12-87ae-1f93132ea991 | -14.93808 | -48.26414 | 2026-08-08 04:27:00 | NPP-375D | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 448a64c6-c4a6-36c0-8a20-4bd37272fed0 | -16.44762 | -43.1477 | 2026-08-08 04:27:00 | NPP-375D | GRÃO MOGOL | MINAS GERAIS | Brasil | 3127800 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 2ff708ea-69fa-3fd1-9bf6-61071d83e67d | -18.34855 | -50.72815 | 2026-08-08 04:27:00 | NPP-375D | QUIRINÓPOLIS | GOIÁS | Brasil | 5218508 | 52 | 33 | nan | nan | nan | Cerrado | 53.4 |
| c17b7496-251f-39c6-96a4-9cd9658b7cb5 | -21.36631 | -45.13271 | 2026-08-08 04:27:00 | NPP-375D | CARMO DA CACHOEIRA | MINAS GERAIS | Brasil | 3113909 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 9792ecb8-cf85-33c0-a824-2110b754dbb5 | -16.21541 | -46.00777 | 2026-08-08 04:27:00 | NPP-375D | RIACHINHO | MINAS GERAIS | Brasil | 3154457 | 31 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 631c1f17-268d-364c-9ffd-c3cc618ff94b | -14.92957 | -48.24933 | 2026-08-08 04:27:00 | NPP-375D | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 6.9 |
| a21a9835-a0b5-30a8-b635-e329e67a811a | -19.78582 | -43.73166 | 2026-08-08 04:27:00 | NPP-375D | SABARÁ | MINAS GERAIS | Brasil | 3156700 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 0c290bcf-14e4-38f0-ae9c-8a337d0af33b | -14.32354 | -54.94348 | 2026-08-08 04:27:00 | NPP-375D | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| e1adb070-182b-34f5-9081-cd52d6f7cbcc | -15.16368 | -52.74568 | 2026-08-08 04:27:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 6.6 |
| d8fffedb-e848-3ad4-bcc3-1dfac2e6d0b7 | -15.38315 | -53.79959 | 2026-08-08 04:27:00 | NPP-375D | GENERAL CARNEIRO | MATO GROSSO | Brasil | 5103908 | 51 | 33 | nan | nan | nan | Cerrado | 7.5 |
| 568154f4-c23c-38ae-b18b-dab359ad4d3f | -15.10041 | -52.73646 | 2026-08-08 04:27:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 6f3eb3a1-ce5f-3fef-aa3f-1d7c00a0f529 | -20.27338 | -41.78459 | 2026-08-08 04:27:00 | NPP-375D | MARTINS SOARES | MINAS GERAIS | Brasil | 3140530 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| 85cb5268-5d62-36fa-a63c-1132a6eb2a70 | -15.92065 | -43.52399 | 2026-08-08 04:27:00 | NPP-375D | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 6.8 |
| f8ebb007-bcda-3aa6-97c0-afa10db21c39 | -15.38477 | -53.79274 | 2026-08-08 04:27:00 | NPP-375D | GENERAL CARNEIRO | MATO GROSSO | Brasil | 5103908 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| ed6d8e73-9924-33a3-95aa-1e8472c19f84 | -14.93451 | -48.26342 | 2026-08-08 04:27:00 | NPP-375D | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 5f6f9281-1fcf-3f34-89aa-e9d440db1669 | -15.70714 | -42.18732 | 2026-08-08 04:27:00 | NPP-375D | INDAIABIRA | MINAS GERAIS | Brasil | 3130655 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 76eadf08-9b9d-33b4-9f70-926dbd9db601 | -18.76655 | -47.06724 | 2026-08-08 04:27:00 | NPP-375D | PATROCÍNIO | MINAS GERAIS | Brasil | 3148103 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 58549cc2-f776-3897-900d-ac74107dcf14 | -18.37049 | -50.6956 | 2026-08-08 04:27:00 | NPP-375D | QUIRINÓPOLIS | GOIÁS | Brasil | 5218508 | 52 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 1a719c49-b233-3edd-9b08-104f8bd0bb2e | -19.03273 | -44.87074 | 2026-08-08 04:27:00 | NPP-375D | POMPÉU | MINAS GERAIS | Brasil | 3152006 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| c4273872-5852-3d16-bf19-2ab614b7f750 | -14.42296 | -45.65724 | 2026-08-08 04:27:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| f65eb46a-ed19-3a0d-88db-1f04cf6492d4 | -15.16006 | -52.73941 | 2026-08-08 04:27:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 73b1d76f-c212-320c-8a5b-0c29380604fe | -15.15905 | -52.74454 | 2026-08-08 04:27:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 0ea13148-6b61-3cd1-aa3f-c856e6e0f877 | -15.37978 | -53.79175 | 2026-08-08 04:27:00 | NPP-375D | GENERAL CARNEIRO | MATO GROSSO | Brasil | 5103908 | 51 | 33 | nan | nan | nan | Cerrado | 5.6 |
| ab8d05e4-a2d1-34c0-b0f9-0cc32a8cb4df | -14.35727 | -54.97393 | 2026-08-08 04:27:00 | NPP-375D | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 24db4ec4-cbbb-344f-b72f-a65f70340a1d | -20.55299 | -43.50964 | 2026-08-08 04:27:00 | NPP-375D | OURO PRETO | MINAS GERAIS | Brasil | 3146107 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 1b6439a7-1ed0-3275-99f3-c896959e9487 | -15.15799 | -52.74994 | 2026-08-08 04:27:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 4a0d6f73-0540-311a-b3ea-443e1c0ffd61 | -14.32206 | -54.95077 | 2026-08-08 04:27:00 | NPP-375D | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| f058902f-f40a-3b61-960c-c0210159fe31 | -18.01617 | -44.37577 | 2026-08-08 04:27:00 | NPP-375D | BUENÓPOLIS | MINAS GERAIS | Brasil | 3109204 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 93cbe869-b19f-3398-a8f7-6c5c6a7d4582 | -19.83954 | -43.88175 | 2026-08-08 04:27:00 | NPP-375D | BELO HORIZONTE | MINAS GERAIS | Brasil | 3106200 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.4 |
| 500bea38-58d6-30d9-b7f8-f90f03dd9da5 | -15.10801 | -52.72213 | 2026-08-08 04:27:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 582d1073-c609-3594-907e-d4152a6d3c58 | -15.9394 | -48.31061 | 2026-08-08 04:27:00 | NPP-375D | SANTO ANTÔNIO DO DESCOBERTO | GOIÁS | Brasil | 5219753 | 52 | 33 | nan | nan | nan | Cerrado | 4.4 |
| ebdbce07-b538-3a51-9678-1586004055ad | -18.36002 | -50.70914 | 2026-08-08 04:27:00 | NPP-375D | QUIRINÓPOLIS | GOIÁS | Brasil | 5218508 | 52 | 33 | nan | nan | nan | Cerrado | 8.7 |
| af9191eb-b861-3e74-8b84-36e6e9a2e174 | -14.36964 | -54.96906 | 2026-08-08 04:27:00 | NPP-375D | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 4.1 |
| dfcb8af0-632e-378f-a60b-f6a1376f853d | -15.39243 | -53.80667 | 2026-08-08 04:27:00 | NPP-375D | GENERAL CARNEIRO | MATO GROSSO | Brasil | 5103908 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 4d3c3ab9-3082-369e-8711-a78bb0a2636f | -16.39572 | -49.37246 | 2026-08-08 04:27:00 | NPP-375D | BRAZABRANTES | GOIÁS | Brasil | 5203609 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 53df231e-3b41-3f7b-97d6-c07a6d91b6a0 | -14.92812 | -48.2577 | 2026-08-08 04:27:00 | NPP-375D | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 43003f32-2196-30c2-82cd-0ea7dc91f289 | -14.41574 | -45.65969 | 2026-08-08 04:27:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| bc4952ac-3132-3e44-8377-e11f437cd64b | -18.36661 | -50.69484 | 2026-08-08 04:27:00 | NPP-375D | QUIRINÓPOLIS | GOIÁS | Brasil | 5218508 | 52 | 33 | nan | nan | nan | Cerrado | 3.8 |
| ef3496f7-b657-3b5d-a20a-a77017822ef3 | -19.78934 | -43.73227 | 2026-08-08 04:27:00 | NPP-375D | SABARÁ | MINAS GERAIS | Brasil | 3156700 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 074dfa68-42a5-38ee-a195-1b609a63cbc9 | -15.70775 | -42.18305 | 2026-08-08 04:27:00 | NPP-375D | INDAIABIRA | MINAS GERAIS | Brasil | 3130655 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| a8af3c5e-c54d-33af-9cb4-154dcf7f2466 | -14.27216 | -45.31018 | 2026-08-08 04:27:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 75ec94a7-c1cc-3a42-99eb-6ec495ac0ac8 | -14.36272 | -54.97516 | 2026-08-08 04:27:00 | NPP-375D | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 15.0 |
| c4146cc2-79a8-36f6-9641-fc4c41822454 | -18.3639 | -50.70995 | 2026-08-08 04:27:00 | NPP-375D | QUIRINÓPOLIS | GOIÁS | Brasil | 5218508 | 52 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 5949a1c2-e130-361a-9569-c33389927291 | -15.38361 | -53.79868 | 2026-08-08 04:27:00 | NPP-375D | GENERAL CARNEIRO | MATO GROSSO | Brasil | 5103908 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 3bc184c9-8d58-3218-a40e-674b3e226ba3 | -18.35415 | -50.72047 | 2026-08-08 04:27:00 | NPP-375D | QUIRINÓPOLIS | GOIÁS | Brasil | 5218508 | 52 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 76534b9e-53a7-3f67-b57f-f052b802e3b7 | -15.15841 | -52.73717 | 2026-08-08 04:27:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| f5342e45-7da6-3740-8921-573b4c57ee97 | -14.27224 | -45.28829 | 2026-08-08 04:27:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 5a8ac8ef-ecc7-3e88-9efd-6b2889c3da93 | -15.3974 | -53.80772 | 2026-08-08 04:27:00 | NPP-375D | GENERAL CARNEIRO | MATO GROSSO | Brasil | 5103908 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| e62dc6e2-7aba-3034-97c1-2b3005cd31c6 | -14.93735 | -48.26841 | 2026-08-08 04:27:00 | NPP-375D | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 3.6 |
| a4c31dd3-0fe5-3a97-82b2-6c4b9c122447 | -19.7469 | -43.90213 | 2026-08-08 04:27:00 | NPP-375D | SANTA LUZIA | MINAS GERAIS | Brasil | 3157807 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 37e26ade-6344-3757-b77b-f87ca0f3319e | -16.25795 | -46.67945 | 2026-08-08 04:27:00 | NPP-375D | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 8db5320f-7984-31e0-bae3-0a973579cb1b | -20.17579 | -43.69053 | 2026-08-08 04:27:00 | NPP-375D | ITABIRITO | MINAS GERAIS | Brasil | 3131901 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| d474a84e-72cc-3631-bd89-be7a1927dfdd | -20.88414 | -43.15641 | 2026-08-08 04:27:00 | NPP-375D | SENADOR FIRMINO | MINAS GERAIS | Brasil | 3165701 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.1 |
| af283989-3a8c-3814-b289-1bc7c14c6db8 | -14.42571 | -45.66138 | 2026-08-08 04:27:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| ca644483-9d57-3573-ba80-e64bd872b060 | -21.36913 | -45.13716 | 2026-08-08 04:27:00 | NPP-375D | CARMO DA CACHOEIRA | MINAS GERAIS | Brasil | 3113909 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.8 |
| d01304fa-2327-3dec-9c03-5a29f1eb9889 | -15.71136 | -42.18367 | 2026-08-08 04:27:00 | NPP-375D | INDAIABIRA | MINAS GERAIS | Brasil | 3130655 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 2d3de777-093f-3455-bc6f-e019a71110fe | -16.87672 | -43.21391 | 2026-08-08 04:27:00 | NPP-375D | ITACAMBIRA | MINAS GERAIS | Brasil | 3132008 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 04cd3be9-0818-38fd-8c87-ffce74b2c679 | -19.86721 | -41.70035 | 2026-08-08 04:27:00 | NPP-375D | CONCEIÇÃO DE IPANEMA | MINAS GERAIS | Brasil | 3117405 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.0 |
| cf08e4f7-2d52-363c-b765-34427ef2f71a | -14.1604 | -54.0046 | 2026-08-08 04:27:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 770b192b-1af9-3bb7-9bea-f6a6d677289c | -14.37509 | -54.97027 | 2026-08-08 04:27:00 | NPP-375D | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 971cb02c-df9d-3c97-8f31-7d03953d60d8 | -14.2728 | -45.28474 | 2026-08-08 04:27:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 37939260-b5d7-3646-bdc7-205e68c090ae | -17.85744 | -44.47915 | 2026-08-08 04:27:00 | NPP-375D | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 7616163b-0385-3938-a4ad-c9e3a445b6b1 | -20.21186 | -45.62395 | 2026-08-08 04:27:00 | NPP-375D | ARCOS | MINAS GERAIS | Brasil | 3104205 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| ee551c32-a3fc-3398-9f01-85e7475fb4db | -18.36088 | -50.70602 | 2026-08-08 04:27:00 | NPP-375D | QUIRINÓPOLIS | GOIÁS | Brasil | 5218508 | 52 | 33 | nan | nan | nan | Cerrado | 7.4 |
| 01d26e4b-71d8-32da-9452-b6ae003d1ce2 | -20.32729 | -43.66132 | 2026-08-08 04:27:00 | NPP-375D | OURO PRETO | MINAS GERAIS | Brasil | 3146107 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 50ee2fa0-7e03-3ffd-aafe-702890b51f63 | -14.36346 | -54.97149 | 2026-08-08 04:27:00 | NPP-375D | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 4.1 |
| cc4a6284-0321-349d-82a9-300025e96ae4 | -14.36891 | -54.9727 | 2026-08-08 04:27:00 | NPP-375D | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 270a3ec2-5a21-35f1-ba56-569b145a0a4f | -15.69992 | -54.85601 | 2026-08-08 04:27:00 | NPP-375D | DOM AQUINO | MATO GROSSO | Brasil | 5103601 | 51 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 107706be-5438-3de4-9db8-e71dc088caea | -17.88739 | -44.44178 | 2026-08-08 04:27:00 | NPP-375D | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 367cd633-640e-34c2-86fd-09dad72cbc4b | -15.1657 | -52.74994 | 2026-08-08 04:27:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 4.8 |
| e3b4e109-1b56-3c34-a270-aab43f3eddfa | -17.98569 | -44.25461 | 2026-08-08 04:27:00 | NPP-375D | BUENÓPOLIS | MINAS GERAIS | Brasil | 3109204 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| fdb5e08c-c162-378b-8129-e1074a14e81d | -14.31391 | -54.99084 | 2026-08-08 04:27:00 | NPP-375D | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 4.0 |
| ff791dc8-f2ba-3b26-88b3-6c9d617b0846 | -18.36662 | -50.69678 | 2026-08-08 04:27:00 | NPP-375D | QUIRINÓPOLIS | GOIÁS | Brasil | 5218508 | 52 | 33 | nan | nan | nan | Cerrado | 5.7 |
| bb7119d0-d786-374b-bf79-421fb242bdc2 | -17.8882 | -44.44118 | 2026-08-08 04:27:00 | NPP-375D | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 067e1d04-125a-31ca-8a63-128476319158 | -17.77208 | -50.45065 | 2026-08-08 04:27:00 | NPP-375D | SANTA HELENA DE GOIÁS | GOIÁS | Brasil | 5219308 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 35d9f06d-9f39-38da-90fd-80234924fc20 | -20.4041 | -43.51888 | 2026-08-08 04:27:00 | NPP-375D | OURO PRETO | MINAS GERAIS | Brasil | 3146107 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 68d92ae5-1cf6-32c1-834f-ce2b95c3091f | -14.35653 | -54.97759 | 2026-08-08 04:27:00 | NPP-375D | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 2e82aed5-22ad-31b7-b981-cc8bb2bc64cb | -17.547 | -49.63726 | 2026-08-08 04:27:00 | NPP-375D | PONTALINA | GOIÁS | Brasil | 5217708 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 693eb765-0f10-3b3e-8d46-7cae115cbf04 | -15.10709 | -52.7269 | 2026-08-08 04:27:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 53b08ac5-01e4-3710-b555-4364d8ba2a68 | -15.37817 | -53.79857 | 2026-08-08 04:27:00 | NPP-375D | GENERAL CARNEIRO | MATO GROSSO | Brasil | 5103908 | 51 | 33 | nan | nan | nan | Cerrado | 7.5 |
| b31a958f-6452-3071-90f8-d4eb50f52e9a | -14.3228 | -54.94713 | 2026-08-08 04:27:00 | NPP-375D | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |


[Clique aqui para ver as próximas entradas](README14.md)
