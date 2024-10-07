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

## Dados Diários - Página 86

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 411b8a30-2e38-3bea-95fc-bfb52f7d4c69 | -19.78048 | -42.65398 | 2024-10-07 04:55:00 | AQUA_M-M | MARLIÉRIA | MINAS GERAIS | Brasil | 3140308 | 31 | 33 | nan | nan | nan | Mata Atlântica | 13.6 |
| 2a1ca1b8-4633-3e4e-81fa-3e2628c4e513 | -20.3478 | -44.68272 | 2024-10-07 04:55:00 | AQUA_M-M | CLÁUDIO | MINAS GERAIS | Brasil | 3116605 | 31 | 33 | nan | nan | nan | Cerrado | 11.4 |
| 67a817ad-b057-3eb6-904a-03de941033d4 | -19.952 | -44.08856 | 2024-10-07 04:55:00 | AQUA_M-M | BETIM | MINAS GERAIS | Brasil | 3106705 | 31 | 33 | nan | nan | nan | Mata Atlântica | 8.2 |
| f7302f83-11dd-3492-bbd0-010fb490c121 | -19.92477 | -44.4964 | 2024-10-07 04:55:00 | AQUA_M-M | FLORESTAL | MINAS GERAIS | Brasil | 3126000 | 31 | 33 | nan | nan | nan | Mata Atlântica | 10.2 |
| 6d4a2aba-6df5-306a-8747-9984f24a9db5 | -19.86975 | -44.08859 | 2024-10-07 04:55:00 | AQUA_M-M | CONTAGEM | MINAS GERAIS | Brasil | 3118601 | 31 | 33 | nan | nan | nan | Cerrado | 4.8 |
| a1892da1-98cf-332c-baef-d745893fb322 | -19.86808 | -44.09901 | 2024-10-07 04:55:00 | AQUA_M-M | CONTAGEM | MINAS GERAIS | Brasil | 3118601 | 31 | 33 | nan | nan | nan | Cerrado | 9.3 |
| de5ca270-63e6-3690-bfbb-9149692f85c1 | -19.83344 | -43.79238 | 2024-10-07 04:55:00 | AQUA_M-M | SANTA LUZIA | MINAS GERAIS | Brasil | 3157807 | 31 | 33 | nan | nan | nan | Mata Atlântica | 9.9 |
| 76340dd5-81bf-353c-9769-1f5419482870 | -19.82429 | -43.79057 | 2024-10-07 04:55:00 | AQUA_M-M | SANTA LUZIA | MINAS GERAIS | Brasil | 3157807 | 31 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 1fb31555-429a-3da8-947b-8d0347c932c2 | -21.96236 | -45.36668 | 2024-10-07 04:55:00 | AQUA_M-M | LAMBARI | MINAS GERAIS | Brasil | 3137809 | 31 | 33 | nan | nan | nan | Mata Atlântica | 17.6 |
| 77a28d0c-2b67-3809-b6c8-d6d3baf236eb | -21.96058 | -45.37732 | 2024-10-07 04:55:00 | AQUA_M-M | LAMBARI | MINAS GERAIS | Brasil | 3137809 | 31 | 33 | nan | nan | nan | Mata Atlântica | 30.0 |
| d61db548-8c30-32af-a0df-3e803abce3e2 | -21.67593 | -44.00274 | 2024-10-07 04:55:00 | AQUA_M-M | LIMA DUARTE | MINAS GERAIS | Brasil | 3138609 | 31 | 33 | nan | nan | nan | Mata Atlântica | 30.1 |
| 825615b7-d98f-3a4c-b839-f0934c87075a | -21.67432 | -44.01276 | 2024-10-07 04:55:00 | AQUA_M-M | LIMA DUARTE | MINAS GERAIS | Brasil | 3138609 | 31 | 33 | nan | nan | nan | Mata Atlântica | 19.2 |
| 5e44ed32-57bf-3910-b834-ea3014551a95 | -21.54205 | -43.97652 | 2024-10-07 04:55:00 | AQUA_M-M | IBERTIOGA | MINAS GERAIS | Brasil | 3129400 | 31 | 33 | nan | nan | nan | Mata Atlântica | 7.1 |
| 3468a75f-a2e2-3918-a262-2aefa9cc7b6c | -21.0067 | -46.09514 | 2024-10-07 04:55:00 | AQUA_M-M | CARMO DO RIO CLARO | MINAS GERAIS | Brasil | 3114402 | 31 | 33 | nan | nan | nan | Mata Atlântica | 24.7 |
| 94672ecf-8929-380e-a9f1-aca0f520a9da | -20.99664 | -46.09227 | 2024-10-07 04:55:00 | AQUA_M-M | CARMO DO RIO CLARO | MINAS GERAIS | Brasil | 3114402 | 31 | 33 | nan | nan | nan | Mata Atlântica | 17.1 |
| 8345b9ad-65ac-3689-b93a-c4f5751b5256 | -20.98852 | -46.07826 | 2024-10-07 04:55:00 | AQUA_M-M | CARMO DO RIO CLARO | MINAS GERAIS | Brasil | 3114402 | 31 | 33 | nan | nan | nan | Mata Atlântica | 23.3 |
| eaa21da6-b3fa-37b2-8e32-2674b28a0256 | -20.98639 | -46.09051 | 2024-10-07 04:55:00 | AQUA_M-M | CARMO DO RIO CLARO | MINAS GERAIS | Brasil | 3114402 | 31 | 33 | nan | nan | nan | Mata Atlântica | 26.2 |
| 06aac830-c27c-3912-b3e7-92fe80461d9b | -20.52772 | -48.12315 | 2024-10-07 04:55:00 | AQUA_M-M | MORRO AGUDO | SÃO PAULO | Brasil | 3531902 | 35 | 33 | nan | nan | nan | Cerrado | 14.9 |
| 89b6bf5a-d561-3cbe-a96c-c5708b498b8a | -20.51577 | -48.12095 | 2024-10-07 04:55:00 | AQUA_M-M | MORRO AGUDO | SÃO PAULO | Brasil | 3531902 | 35 | 33 | nan | nan | nan | Cerrado | 348.3 |
| 98ffdb38-4189-3ef8-a2ce-574a4f4a901c | -20.51247 | -48.1386 | 2024-10-07 04:55:00 | AQUA_M-M | MORRO AGUDO | SÃO PAULO | Brasil | 3531902 | 35 | 33 | nan | nan | nan | Cerrado | 116.0 |
| 485fcb06-0005-365a-b45b-5f1e661f9343 | -20.51211 | -48.11258 | 2024-10-07 04:55:00 | AQUA_M-M | SÃO JOAQUIM DA BARRA | SÃO PAULO | Brasil | 3549409 | 35 | 33 | nan | nan | nan | Cerrado | 146.7 |
| 2d1223ab-0345-36a7-b853-79f2a17368cf | -20.50885 | -48.13073 | 2024-10-07 04:55:00 | AQUA_M-M | MORRO AGUDO | SÃO PAULO | Brasil | 3531902 | 35 | 33 | nan | nan | nan | Cerrado | 283.6 |
| 46fad81e-5715-3a1e-ba98-e8b3d616e227 | -20.47713 | -47.65158 | 2024-10-07 04:55:00 | AQUA_M-M | GUARÁ | SÃO PAULO | Brasil | 3517703 | 35 | 33 | nan | nan | nan | Cerrado | 14.0 |
| aed29e35-44d1-3ec0-8e54-aa6e609dbdef | -20.47408 | -47.66864 | 2024-10-07 04:55:00 | AQUA_M-M | GUARÁ | SÃO PAULO | Brasil | 3517703 | 35 | 33 | nan | nan | nan | Cerrado | 83.5 |
| b612a353-3b4c-3472-9671-a39dd5e326ae | -20.47104 | -47.68558 | 2024-10-07 04:55:00 | AQUA_M-M | GUARÁ | SÃO PAULO | Brasil | 3517703 | 35 | 33 | nan | nan | nan | Cerrado | 70.8 |
| bec27f7b-d0eb-3c10-9c46-fa28aace8be8 | -20.45955 | -47.68298 | 2024-10-07 04:55:00 | AQUA_M-M | GUARÁ | SÃO PAULO | Brasil | 3517703 | 35 | 33 | nan | nan | nan | Cerrado | 24.6 |
| f77a7aef-9c24-33ca-af71-9519761cce87 | -20.45652 | -47.69973 | 2024-10-07 04:55:00 | AQUA_M-M | GUARÁ | SÃO PAULO | Brasil | 3517703 | 35 | 33 | nan | nan | nan | Cerrado | 29.0 |
| 647af11e-a7f3-3b10-8b61-92a5fc00b558 | -20.45347 | -47.71662 | 2024-10-07 04:55:00 | AQUA_M-M | GUARÁ | SÃO PAULO | Brasil | 3517703 | 35 | 33 | nan | nan | nan | Cerrado | 20.1 |
| 98d4295a-0522-3a0b-adc5-b72b5473bbc7 | -20.44799 | -47.68073 | 2024-10-07 04:55:00 | AQUA_M-M | ITUVERAVA | SÃO PAULO | Brasil | 3524105 | 35 | 33 | nan | nan | nan | Cerrado | 70.4 |
| 396223c6-3d79-3f37-8887-7452f6aa8b1e | -20.44495 | -47.6975 | 2024-10-07 04:55:00 | AQUA_M-M | ITUVERAVA | SÃO PAULO | Brasil | 3524105 | 35 | 33 | nan | nan | nan | Cerrado | 68.1 |
| 1bfa92e6-4d27-3094-a630-a3ae0dc8abd5 | -21.66821 | -47.72689 | 2024-10-07 04:55:00 | AQUA_M-M | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 13.4 |
| bbd4895c-efab-361a-9659-5573a393ba7c | -21.65697 | -47.72424 | 2024-10-07 04:55:00 | AQUA_M-M | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 15.9 |
| 5598488b-5f38-3173-b834-da499bdbc3f8 | -21.64573 | -47.7216 | 2024-10-07 04:55:00 | AQUA_M-M | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 13.0 |
| ee2b5584-c3e9-3a8c-af7a-45523ed1e08e | -21.61181 | -47.71486 | 2024-10-07 04:55:00 | AQUA_M-M | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 11.8 |
| f4c955ea-6552-3ffb-9553-bef7201cc08b | -21.60387 | -47.95155 | 2024-10-07 04:55:00 | AQUA_M-M | RINCÃO | SÃO PAULO | Brasil | 3543709 | 35 | 33 | nan | nan | nan | Cerrado | 40.3 |
| e0e5c8a9-785d-376a-b11c-f14e9d519326 | -21.60056 | -47.71227 | 2024-10-07 04:55:00 | AQUA_M-M | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 27.9 |
| e760d041-479f-34bc-ac56-f79e9c79361d | -21.59888 | -47.7229 | 2024-10-07 04:55:00 | AQUA_M-M | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 111.4 |
| 3ebfbf26-4bc0-3d3d-b7e7-6c81438f4cc4 | -21.5976 | -47.72825 | 2024-10-07 04:55:00 | AQUA_M-M | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 148.7 |
| 1f057e00-08a9-36e1-abf1-938d7aec8c43 | -21.59598 | -47.73927 | 2024-10-07 04:55:00 | AQUA_M-M | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 68.8 |
| 23ad7f8e-d427-3902-9744-9f4009b783c0 | -21.59455 | -47.74473 | 2024-10-07 04:55:00 | AQUA_M-M | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 21.0 |
| 9e589573-dcad-33a9-b7e8-5ddfdee35e6e | -21.59236 | -47.94923 | 2024-10-07 04:55:00 | AQUA_M-M | GUATAPARÁ | SÃO PAULO | Brasil | 3518859 | 35 | 33 | nan | nan | nan | Cerrado | 16.9 |
| 0f866b81-ea17-3ccd-920f-055175c16e50 | -21.58773 | -47.71967 | 2024-10-07 04:55:00 | AQUA_M-M | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 30.1 |
| 5bb7b71f-6b21-3758-a98b-c44ad5d76e24 | -21.5864 | -47.72533 | 2024-10-07 04:55:00 | AQUA_M-M | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 39.4 |
| 61b11b1b-3c99-36c2-b6b1-61a1a6796bb3 | -21.58471 | -47.73662 | 2024-10-07 04:55:00 | AQUA_M-M | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 65.6 |
| d5a8adeb-c8e8-3325-ad20-2ea756f28f81 | -21.58328 | -47.74212 | 2024-10-07 04:55:00 | AQUA_M-M | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 47.3 |
| b1e66424-565e-3f5c-81c1-633b46cb2ad4 | -21.58173 | -47.7533 | 2024-10-07 04:55:00 | AQUA_M-M | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 40.6 |
| d37c1366-d1cc-3e3c-a939-8e387620f605 | -21.58018 | -47.75875 | 2024-10-07 04:55:00 | AQUA_M-M | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 29.9 |
| a7cd2cb1-7dd5-32c4-8308-2510419450c7 | -21.57343 | -47.73403 | 2024-10-07 04:55:00 | AQUA_M-M | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 35.1 |
| 7d87cd81-56f3-30a3-8a32-991809bab7fe | -21.57039 | -47.75096 | 2024-10-07 04:55:00 | AQUA_M-M | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 16.8 |
| ee1917b3-fcf9-3e26-ab6b-bf6199858682 | -21.56209 | -47.73179 | 2024-10-07 04:55:00 | AQUA_M-M | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 21.1 |
| c6126a94-40bf-3ef5-8d3b-d69ef2d94a4e | -21.33246 | -47.59859 | 2024-10-07 04:55:00 | AQUA_M-M | SERRA AZUL | SÃO PAULO | Brasil | 3551405 | 35 | 33 | nan | nan | nan | Cerrado | 17.2 |
| 9b597d01-6074-37a5-925d-ba6eb070a7f9 | -21.32957 | -47.60501 | 2024-10-07 04:55:00 | AQUA_M-M | SERRA AZUL | SÃO PAULO | Brasil | 3551405 | 35 | 33 | nan | nan | nan | Cerrado | 27.3 |
| bc98816a-5580-3d54-9f4c-2bd59d334eca | -21.32952 | -47.6151 | 2024-10-07 04:55:00 | AQUA_M-M | SERRA AZUL | SÃO PAULO | Brasil | 3551405 | 35 | 33 | nan | nan | nan | Cerrado | 8.7 |
| e3072b05-7acb-3885-8046-015090579dee | -21.32125 | -47.59594 | 2024-10-07 04:55:00 | AQUA_M-M | SERRA AZUL | SÃO PAULO | Brasil | 3551405 | 35 | 33 | nan | nan | nan | Cerrado | 13.2 |
| 93df1f26-97eb-3585-bf9a-f8fa7fb3a7c6 | -21.28813 | -47.39436 | 2024-10-07 04:55:00 | AQUA_M-M | CAJURU | SÃO PAULO | Brasil | 3509403 | 35 | 33 | nan | nan | nan | Cerrado | 19.8 |
| 67bec7e4-8182-3642-96cb-cda78ee6f7d4 | -21.28777 | -47.38833 | 2024-10-07 04:55:00 | AQUA_M-M | CAJURU | SÃO PAULO | Brasil | 3509403 | 35 | 33 | nan | nan | nan | Cerrado | 16.7 |
| cb035c75-64d3-3b90-af1a-717befc85e62 | -20.76426 | -49.46479 | 2024-10-07 04:55:00 | AQUA_M-M | MIRASSOL | SÃO PAULO | Brasil | 3530300 | 35 | 33 | nan | nan | nan | Cerrado | 34.4 |
| 787aea71-cf42-313f-925e-a4cdff67930a | -20.75993 | -49.48734 | 2024-10-07 04:55:00 | AQUA_M-M | MIRASSOL | SÃO PAULO | Brasil | 3530300 | 35 | 33 | nan | nan | nan | Cerrado | 26.6 |
| 3b81106c-9132-31fc-b04e-539fd5751bd3 | -20.71624 | -49.64231 | 2024-10-07 04:55:00 | AQUA_M-M | MONTE APRAZÍVEL | SÃO PAULO | Brasil | 3531407 | 35 | 33 | nan | nan | nan | Cerrado | 41.6 |
| 2016ad31-d652-31ce-9cbd-c1b7b3220031 | -20.58792 | -48.50573 | 2024-10-07 04:55:00 | AQUA_M-M | BARRETOS | SÃO PAULO | Brasil | 3505500 | 35 | 33 | nan | nan | nan | Cerrado | 55.3 |
| 7d8a95d8-e472-3ff2-b523-d8a572135fc0 | -20.57568 | -48.50318 | 2024-10-07 04:55:00 | AQUA_M-M | BARRETOS | SÃO PAULO | Brasil | 3505500 | 35 | 33 | nan | nan | nan | Cerrado | 81.1 |
| baf4c959-6f13-3089-aaa4-e38cba3c2c7f | -20.57213 | -48.52229 | 2024-10-07 04:55:00 | AQUA_M-M | BARRETOS | SÃO PAULO | Brasil | 3505500 | 35 | 33 | nan | nan | nan | Cerrado | 22.7 |
| b50a6ce5-d3e3-32ee-8d5a-a39aa604295c | -20.35021 | -48.78809 | 2024-10-07 04:55:00 | AQUA_M-M | COLÔMBIA | SÃO PAULO | Brasil | 3512100 | 35 | 33 | nan | nan | nan | Cerrado | 36.5 |
| 57556d8d-9ba8-395a-b4de-a1ce1b802e89 | -20.34642 | -48.80836 | 2024-10-07 04:55:00 | AQUA_M-M | COLÔMBIA | SÃO PAULO | Brasil | 3512100 | 35 | 33 | nan | nan | nan | Cerrado | 103.3 |
| bdf65d4f-4bea-3758-91c7-735b173af04c | -21.70596 | -42.29328 | 2024-10-07 04:55:00 | NOAA-21 | PIRAPETINGA | MINAS GERAIS | Brasil | 3151107 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.9 |
| 85e4d51f-db88-39a1-ad12-4ecd240bb3cc | -21.6991 | -42.29232 | 2024-10-07 04:55:00 | NOAA-21 | PIRAPETINGA | MINAS GERAIS | Brasil | 3151107 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| bcd457b3-3c23-37d7-804c-dd31aa38d919 | -17.8377 | -42.22369 | 2024-10-07 04:55:00 | NOAA-21 | MALACACHETA | MINAS GERAIS | Brasil | 3139201 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.3 |
| 987079ec-f67c-3705-af36-4876c46b209c | -17.83719 | -42.22938 | 2024-10-07 04:55:00 | NOAA-21 | MALACACHETA | MINAS GERAIS | Brasil | 3139201 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.9 |
| b423b553-1ae1-380a-a3d9-f57e494bbe91 | -19.28319 | -42.57389 | 2024-10-07 04:55:00 | NOAA-21 | MESQUITA | MINAS GERAIS | Brasil | 3141702 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| b120b7c8-204d-3ea9-99ff-730b57df58e5 | -19.13954 | -42.72464 | 2024-10-07 04:55:00 | NOAA-21 | BRAÚNAS | MINAS GERAIS | Brasil | 3108800 | 31 | 33 | nan | nan | nan | Mata Atlântica | 5.3 |
| 35d6ae05-816c-3d98-bc98-bd2c8402195b | -19.13898 | -42.73081 | 2024-10-07 04:55:00 | NOAA-21 | BRAÚNAS | MINAS GERAIS | Brasil | 3108800 | 31 | 33 | nan | nan | nan | Mata Atlântica | 5.3 |
| a6f0d0dd-5c00-3466-9114-d2ccbedc9c73 | -19.13862 | -42.72899 | 2024-10-07 04:55:00 | NOAA-21 | BRAÚNAS | MINAS GERAIS | Brasil | 3108800 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.7 |
| a6ab4ca3-1e43-3a13-9192-4d838662182d | -19.13854 | -42.73556 | 2024-10-07 04:55:00 | NOAA-21 | BRAÚNAS | MINAS GERAIS | Brasil | 3108800 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.8 |
| 312db9b7-8516-31cb-a366-698f26552565 | -19.1382 | -42.73397 | 2024-10-07 04:55:00 | NOAA-21 | BRAÚNAS | MINAS GERAIS | Brasil | 3108800 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.7 |
| c1e17515-9c32-3aaf-916c-a11ef27b3d15 | -19.13248 | -42.72962 | 2024-10-07 04:55:00 | NOAA-21 | BRAÚNAS | MINAS GERAIS | Brasil | 3108800 | 31 | 33 | nan | nan | nan | Mata Atlântica | 5.3 |
| b841c141-38c6-3520-9fb1-9b832428c5e7 | -19.13214 | -42.72747 | 2024-10-07 04:55:00 | NOAA-21 | BRAÚNAS | MINAS GERAIS | Brasil | 3108800 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.7 |
| d0bcf70e-63ab-32c3-b7f1-94b39f7a2fb9 | -19.13199 | -42.73493 | 2024-10-07 04:55:00 | NOAA-21 | BRAÚNAS | MINAS GERAIS | Brasil | 3108800 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.8 |
| fc56e36a-763f-3875-87ee-0b759cb67a56 | -19.13167 | -42.73304 | 2024-10-07 04:55:00 | NOAA-21 | BRAÚNAS | MINAS GERAIS | Brasil | 3108800 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.7 |
| 948c7f51-ad3e-34ae-bcc7-8667f72883c6 | -19.13149 | -42.74047 | 2024-10-07 04:55:00 | NOAA-21 | BRAÚNAS | MINAS GERAIS | Brasil | 3108800 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.8 |
| ea304b00-003a-3cff-a693-9c0c2de0cead | -19.13121 | -42.73854 | 2024-10-07 04:55:00 | NOAA-21 | BRAÚNAS | MINAS GERAIS | Brasil | 3108800 | 31 | 33 | nan | nan | nan | Mata Atlântica | 6.1 |
| 692e1f91-fdd8-325f-8c1d-422689ea5f78 | -18.4691 | -42.43279 | 2024-10-07 04:55:00 | NOAA-21 | PEÇANHA | MINAS GERAIS | Brasil | 3148608 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.4 |
| 14c5e633-117e-391b-b728-eb449e16203a | -18.46857 | -42.43873 | 2024-10-07 04:55:00 | NOAA-21 | PEÇANHA | MINAS GERAIS | Brasil | 3148608 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| d6c4c7b7-3be0-3e1e-81af-bb0a76ab2b56 | -20.87176 | -43.27507 | 2024-10-07 04:55:00 | NOAA-21 | BRÁS PIRES | MINAS GERAIS | Brasil | 3108701 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| cab2b691-d3e6-36bc-a52c-d235a601cde2 | -20.86575 | -43.26881 | 2024-10-07 04:55:00 | NOAA-21 | BRÁS PIRES | MINAS GERAIS | Brasil | 3108701 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.6 |
| b479acff-a977-31df-b938-294973daa9cb | -20.63885 | -42.91288 | 2024-10-07 04:55:00 | NOAA-21 | TEIXEIRAS | MINAS GERAIS | Brasil | 3168507 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.6 |
| 40829d49-a926-3266-be30-9cfd05fbfbf6 | -20.21399 | -42.89608 | 2024-10-07 04:55:00 | NOAA-21 | RIO DOCE | MINAS GERAIS | Brasil | 3155009 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.6 |
| 3922c074-70cb-3012-a301-412ef4a4fc4a | -19.98244 | -42.46142 | 2024-10-07 04:55:00 | NOAA-21 | RAUL SOARES | MINAS GERAIS | Brasil | 3154002 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.3 |
| eca0d3a4-4bab-3773-b7e6-1a8e5946ef1b | -19.97986 | -42.45356 | 2024-10-07 04:55:00 | NOAA-21 | RAUL SOARES | MINAS GERAIS | Brasil | 3154002 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.2 |
| aedf598c-278f-3c21-ad58-4043136a2d08 | -19.97941 | -42.45926 | 2024-10-07 04:55:00 | NOAA-21 | RAUL SOARES | MINAS GERAIS | Brasil | 3154002 | 31 | 33 | nan | nan | nan | Mata Atlântica | 9.4 |
| e1eae94f-3327-36b7-bd47-489fa9117482 | -19.97895 | -42.4651 | 2024-10-07 04:55:00 | NOAA-21 | RAUL SOARES | MINAS GERAIS | Brasil | 3154002 | 31 | 33 | nan | nan | nan | Mata Atlântica | 9.4 |
| 6db07e37-c109-3e7d-bf84-f0b5fa94e4b7 | -19.97621 | -42.45516 | 2024-10-07 04:55:00 | NOAA-21 | RAUL SOARES | MINAS GERAIS | Brasil | 3154002 | 31 | 33 | nan | nan | nan | Mata Atlântica | 6.9 |
| 460c059d-dff2-3022-981f-8d82709b4b16 | -19.97574 | -42.46077 | 2024-10-07 04:55:00 | NOAA-21 | RAUL SOARES | MINAS GERAIS | Brasil | 3154002 | 31 | 33 | nan | nan | nan | Mata Atlântica | 6.9 |
| b843eebf-a9d6-3f5d-a495-01d2000cdf8f | -19.97317 | -42.45266 | 2024-10-07 04:55:00 | NOAA-21 | RAUL SOARES | MINAS GERAIS | Brasil | 3154002 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.1 |
| 358d8833-900e-35e6-862e-8a8bfe083658 | -19.97271 | -42.45853 | 2024-10-07 04:55:00 | NOAA-21 | RAUL SOARES | MINAS GERAIS | Brasil | 3154002 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.8 |
| 36dbb8f0-c5ae-3308-8621-ccb4dd00015d | -19.96952 | -42.45428 | 2024-10-07 04:55:00 | NOAA-21 | RAUL SOARES | MINAS GERAIS | Brasil | 3154002 | 31 | 33 | nan | nan | nan | Mata Atlântica | 6.9 |
| 4f679132-ca00-300a-b94b-d8a80df68a26 | -19.96555 | -42.46373 | 2024-10-07 04:55:00 | NOAA-21 | RAUL SOARES | MINAS GERAIS | Brasil | 3154002 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.8 |
| c7330bf1-7ad9-3048-8dd7-4bd5cbff9823 | -19.96183 | -42.46541 | 2024-10-07 04:55:00 | NOAA-21 | RAUL SOARES | MINAS GERAIS | Brasil | 3154002 | 31 | 33 | nan | nan | nan | Mata Atlântica | 7.6 |
| d035ffaf-4bca-3ac5-b713-d6bce9e25d35 | -19.95883 | -42.46323 | 2024-10-07 04:55:00 | NOAA-21 | RAUL SOARES | MINAS GERAIS | Brasil | 3154002 | 31 | 33 | nan | nan | nan | Mata Atlântica | 5.2 |
| b11b7be7-4e05-3daf-8815-7a5fc3248d28 | -19.95837 | -42.46916 | 2024-10-07 04:55:00 | NOAA-21 | RAUL SOARES | MINAS GERAIS | Brasil | 3154002 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.9 |
| d737d2bb-3ec8-34b5-9759-6ee47d3fac6a | -19.89381 | -42.63776 | 2024-10-07 04:55:00 | NOAA-21 | DIONÍSIO | MINAS GERAIS | Brasil | 3121803 | 31 | 33 | nan | nan | nan | Mata Atlântica | 9.3 |


[Clique aqui para ver as próximas entradas](README87.md)
