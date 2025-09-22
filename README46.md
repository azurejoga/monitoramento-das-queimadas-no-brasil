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

## Dados Diários - Página 46

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 2781f2e3-2ea2-33e8-8b59-97edad306054 | -11.1003 | -49.6786 | 2025-09-22 13:30:00 | GOES-19 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 72.5 |
| 89c1caff-d9a9-3c2b-bdd4-09bf31b3a85b | -14.9895 | -44.4022 | 2025-09-22 13:30:00 | GOES-19 | JANUÁRIA | MINAS GERAIS | Brasil | 3135209 | 31 | 33 | nan | nan | nan | Cerrado | 183.5 |
| 115d453a-7ea8-3829-8b0f-949b4bdb5ec7 | -11.215 | -49.6224 | 2025-09-22 13:30:00 | GOES-19 | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 76.4 |
| 04189ca9-9ef0-35ba-9401-3d380ef97d8d | -11.4674 | -43.5248 | 2025-09-22 13:30:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 128.2 |
| 12ceef91-e004-3e6c-863b-a24ede817391 | -10.3568 | -46.0812 | 2025-09-22 13:30:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 64.9 |
| 9ed92a9c-269f-32bc-9efe-e25467569a32 | -11.1 | -49.7003 | 2025-09-22 13:30:00 | GOES-19 | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 73.0 |
| 9868f2f7-5521-3387-8af4-ee40c22255c4 | -5.5773 | -42.1255 | 2025-09-22 13:30:00 | GOES-19 | ALTO LONGÁ | PIAUÍ | Brasil | 2200301 | 22 | 33 | nan | nan | nan | Caatinga | 84.9 |
| 57ab68b1-f0c2-3204-98b6-ac4d3860f9a3 | -12.0767 | -44.8131 | 2025-09-22 13:40:00 | GOES-19 | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 76.5 |
| 03d4ab15-8683-339f-b734-242eaef8ea2b | -12.1156 | -44.7839 | 2025-09-22 13:40:00 | GOES-19 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 83.8 |
| 8a785ad5-d00b-3587-98e0-ae2baac210a6 | -10.3572 | -46.0585 | 2025-09-22 13:40:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 107.4 |
| 4befaffe-ad59-3c21-b493-0f0bb72ab152 | -14.4917 | -44.8496 | 2025-09-22 13:40:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 114.9 |
| 115bc4d8-7387-316d-abce-f3294c3f74ee | -12.4353 | -45.1515 | 2025-09-22 13:40:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 114.9 |
| d4b71239-40f3-3dc9-9863-6cd9913cd4d7 | -12.0963 | -44.7868 | 2025-09-22 13:40:00 | GOES-19 | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 96.7 |
| 86968017-9c9c-369f-bb4e-7a4e9b5ca426 | -12.4545 | -45.1486 | 2025-09-22 13:40:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 122.6 |
| 59a70ed3-a2fa-3442-ae3f-1c99ea072470 | -10.3382 | -46.0609 | 2025-09-22 13:40:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 69.1 |
| 855c1fb2-9e80-33b2-902c-084bc3f37259 | -14.9693 | -44.4297 | 2025-09-22 13:40:00 | GOES-19 | ITACARAMBI | MINAS GERAIS | Brasil | 3132107 | 31 | 33 | nan | nan | nan | Cerrado | 77.7 |
| 06bb3fda-bb33-3f83-8b42-8c5f84c7a007 | -14.9699 | -44.406 | 2025-09-22 13:40:00 | GOES-19 | ITACARAMBI | MINAS GERAIS | Brasil | 3132107 | 31 | 33 | nan | nan | nan | Cerrado | 195.2 |
| 66bc8966-7ab8-382d-9db0-bcceb68d9091 | -14.8484 | -45.4613 | 2025-09-22 13:40:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 112.3 |
| 3d5b1f48-cfa6-30c5-a724-e86b04b821c3 | -10.6928 | -46.4679 | 2025-09-22 13:40:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 67.4 |
| 2ddc87ef-94ee-3dc7-9e36-8db2c06fe8b7 | -12.0771 | -44.7898 | 2025-09-22 13:40:00 | GOES-19 | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 76.1 |
| be069eef-11bd-3d5d-aa4f-8e5407d13f3b | -5.5583 | -42.1507 | 2025-09-22 13:40:00 | GOES-19 | ALTO LONGÁ | PIAUÍ | Brasil | 2200301 | 22 | 33 | nan | nan | nan | Caatinga | 86.6 |
| 5d27e960-4ddb-32bc-8874-9ebfe14e1067 | -11.467 | -43.5485 | 2025-09-22 13:40:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 124.1 |
| 95018ddf-5c16-38b1-b443-d4f20f65efd1 | -11.4482 | -43.5277 | 2025-09-22 13:40:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 84.0 |
| d7d64027-4c13-36e9-bf45-744708367c18 | -12.3592 | -44.0915 | 2025-09-22 13:40:00 | GOES-19 | TABOCAS DO BREJO VELHO | BAHIA | Brasil | 2930907 | 29 | 33 | nan | nan | nan | Cerrado | 76.7 |
| 8eef2292-9e2d-35e0-b74f-62ae04dcbdd2 | -10.3378 | -46.0835 | 2025-09-22 13:40:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 75.8 |
| 7187a621-3435-32e6-8a43-6f551239fe5b | -4.1382 | -41.5557 | 2025-09-22 13:40:00 | GOES-19 | BRASILEIRA | PIAUÍ | Brasil | 2201960 | 22 | 33 | nan | nan | nan | Caatinga | 83.0 |
| a9a5686b-500d-3e3b-a81a-2ed228cee348 | -10.2998 | -46.0882 | 2025-09-22 13:40:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 66.6 |
| e6ee49d6-224a-3b62-be20-cc8714dbc3a0 | -11.2153 | -49.6008 | 2025-09-22 13:40:00 | GOES-19 | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 84.5 |
| 2ddcca6e-8d7a-33ca-92ca-cf2e26e23451 | -12.4379 | -45.0123 | 2025-09-22 13:40:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 72.8 |
| 88c00fae-5cd6-3104-843e-528eacab2b77 | -8.5888 | -45.3322 | 2025-09-22 13:40:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 61.6 |
| ab4e6aa7-d408-353b-8c5e-c80fccf3e789 | -11.215 | -49.6224 | 2025-09-22 13:40:00 | GOES-19 | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 78.9 |
| cb4e57f9-910a-3350-b12a-e2800bf54490 | -11.4862 | -43.5456 | 2025-09-22 13:40:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 82.6 |
| b7da617d-7cf8-326d-8ea9-7e8307241361 | -12.4554 | -45.1022 | 2025-09-22 13:40:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 126.2 |
| 107d2118-abc3-394f-b61b-bbacb0ad588f | -14.8361 | -45.137 | 2025-09-22 13:40:00 | GOES-19 | BONITO DE MINAS | MINAS GERAIS | Brasil | 3108255 | 31 | 33 | nan | nan | nan | Cerrado | 231.5 |
| 7fd7dfeb-80b5-30eb-8ffd-68e34e8a2c6d | -11.6442 | -44.3434 | 2025-09-22 13:40:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 130.4 |
| b33390e8-504d-3013-bd0f-bce7a201ec47 | -5.678 | -41.3987 | 2025-09-22 13:40:00 | GOES-19 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 75.2 |
| 1b11a38d-d949-3ef4-838e-5c1c3cbb8743 | -14.8071 | -51.3809 | 2025-09-22 13:40:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 96.4 |
| 49395f55-a69b-3b75-8aa0-03beec50b9f7 | -11.9296 | -43.4288 | 2025-09-22 13:40:00 | GOES-19 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 105.7 |
| dd914a18-65bd-3579-8732-088c1290e0b2 | -8.2803 | -44.3801 | 2025-09-22 13:40:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 90.7 |
| d9aaff03-2d70-3dc6-842a-459eefe78115 | -14.9895 | -44.4022 | 2025-09-22 13:40:00 | GOES-19 | JANUÁRIA | MINAS GERAIS | Brasil | 3135209 | 31 | 33 | nan | nan | nan | Cerrado | 239.3 |
| 109b7d69-62fd-38fe-a3d9-0773e6b29ed5 | -11.4674 | -43.5248 | 2025-09-22 13:40:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 156.2 |
| e5dae47f-c2ff-3dce-9748-84ec1fd3648d | -10.2621 | -46.0703 | 2025-09-22 13:40:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 118.7 |
| 5451f063-f410-31e6-91d4-68a4e97d0c4b | -9.0078 | -45.0584 | 2025-09-22 13:40:00 | GOES-19 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 75.2 |
| 72e3fa19-a4e9-3886-8c78-74c7f56db63a | -12.455 | -45.1254 | 2025-09-22 13:40:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 106.0 |
| 322a44ec-5e0b-3469-ad22-1f59bba6ad87 | -14.4721 | -44.8532 | 2025-09-22 13:40:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 138.8 |
| 10c49873-81e5-3017-bac9-fd75ccc63c22 | -10.0371 | -47.1952 | 2025-09-22 13:40:00 | GOES-19 | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 60.4 |
| 3c9464ea-2223-36f6-85da-40099824b660 | -5.5773 | -42.1255 | 2025-09-22 13:40:00 | GOES-19 | ALTO LONGÁ | PIAUÍ | Brasil | 2200301 | 22 | 33 | nan | nan | nan | Caatinga | 92.4 |
| eba48d47-eae8-324f-a98b-b1f2b63c55ba | -12.4182 | -45.0385 | 2025-09-22 13:40:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 106.4 |
| 1805195a-94d6-3711-84fa-70505ee51209 | -12.4357 | -45.1284 | 2025-09-22 13:40:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 101.4 |
| 55c8c391-d599-33be-bd34-79b2c4d39c8c | -14.989 | -44.4259 | 2025-09-22 13:40:00 | GOES-19 | JANUÁRIA | MINAS GERAIS | Brasil | 3135209 | 31 | 33 | nan | nan | nan | Cerrado | 104.7 |
| 3228606c-f037-3670-a45d-617d461b92dc | -12.1348 | -44.7809 | 2025-09-22 13:40:00 | GOES-19 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 86.9 |
| 631691e4-8e53-3870-9fec-5d43ed93adaf | -8.5185 | -44.9291 | 2025-09-22 13:40:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 105.2 |
| 3bbb3f0e-5b2c-31eb-a4b5-12ed9c3e9275 | -12.4361 | -45.1052 | 2025-09-22 13:40:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 91.9 |
| 7c4f8683-f133-3b04-8946-de264a0c0ab4 | -10.2617 | -46.0929 | 2025-09-22 13:40:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 79.3 |
| 9e184ca3-5eaf-3946-9a13-4ac9d52de28b | -5.5771 | -42.1493 | 2025-09-22 13:40:00 | GOES-19 | ALTO LONGÁ | PIAUÍ | Brasil | 2200301 | 22 | 33 | nan | nan | nan | Caatinga | 87.0 |
| 3145b37d-0367-3897-95df-4172f47c27b1 | -5.5585 | -42.1269 | 2025-09-22 13:40:00 | GOES-19 | ALTO LONGÁ | PIAUÍ | Brasil | 2200301 | 22 | 33 | nan | nan | nan | Caatinga | 90.1 |
| cc76f03e-850f-34f1-ab74-91221d91e72f | -12.405 | -44.7156 | 2025-09-22 13:40:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 89.5 |
| 4918aab4-a745-39a2-957f-b023fc824dcd | -11.2147 | -49.6441 | 2025-09-22 13:40:00 | GOES-19 | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 74.0 |
| a5e6c7a6-1022-3879-bc58-db076f7f4818 | -12.2983 | -45.2881 | 2025-09-22 13:40:00 | GOES-19 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 67.1 |
| ab858a53-9f10-3946-ae54-d1bb6a6780ed | -14.8265 | -51.3782 | 2025-09-22 13:40:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 111.3 |
| f4b090c2-da1e-303d-9819-1dc4490bf170 | -11.6446 | -44.32 | 2025-09-22 13:40:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 180.1 |
| b38e9fd9-8c27-38ff-9e20-2a6856ce1157 | -18.5983 | -45.0287 | 2025-09-22 13:40:00 | GOES-19 | FELIXLÂNDIA | MINAS GERAIS | Brasil | 3125705 | 31 | 33 | nan | nan | nan | Cerrado | 137.9 |
| 000591d3-67d8-3f87-85e0-c7300b74a297 | -5.5771 | -42.1493 | 2025-09-22 13:50:00 | GOES-19 | ALTO LONGÁ | PIAUÍ | Brasil | 2200301 | 22 | 33 | nan | nan | nan | Caatinga | 88.3 |
| dd8db0c9-2303-37ba-bb0b-4c6f4744daaf | -11.6442 | -44.3434 | 2025-09-22 13:50:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 142.0 |
| b977b51b-f44d-36ef-a3ce-73a5e836538f | -11.7687 | -44.8826 | 2025-09-22 13:50:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 85.2 |
| 9dee9f29-fa65-3023-b60b-69f2c25e0baa | -7.6015 | -44.4262 | 2025-09-22 13:50:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 81.6 |
| 5f21aaa5-7c19-34aa-98b3-5aa9f63cee0e | -5.5959 | -42.1478 | 2025-09-22 13:50:00 | GOES-19 | ALTO LONGÁ | PIAUÍ | Brasil | 2200301 | 22 | 33 | nan | nan | nan | Caatinga | 85.0 |
| 8441f4df-e087-315a-bd6f-34ad7d53ee35 | -5.5585 | -42.1269 | 2025-09-22 13:50:00 | GOES-19 | ALTO LONGÁ | PIAUÍ | Brasil | 2200301 | 22 | 33 | nan | nan | nan | Caatinga | 90.6 |
| 5c4c0952-6331-3fae-948c-41ef37adade7 | -12.2983 | -45.2881 | 2025-09-22 13:50:00 | GOES-19 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 78.9 |
| e62ea3eb-43c6-3f48-8513-f17cd3dcdc17 | -12.4357 | -45.1284 | 2025-09-22 13:50:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 92.7 |
| 5af09dd7-6d5b-3209-ac81-06e0d02641da | -12.4353 | -45.1515 | 2025-09-22 13:50:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 100.5 |
| b2a04dd2-d5f1-39ca-81f5-13283431cb56 | -11.4862 | -43.5456 | 2025-09-22 13:50:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 90.0 |
| 9b01771d-ac81-3cc5-8b1b-13d6570b0d70 | -14.989 | -44.4259 | 2025-09-22 13:50:00 | GOES-19 | JANUÁRIA | MINAS GERAIS | Brasil | 3135209 | 31 | 33 | nan | nan | nan | Cerrado | 110.9 |
| 08cace8c-38b7-35d6-bc1e-7cc80e6b012c | -11.9301 | -43.405 | 2025-09-22 13:50:00 | GOES-19 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 111.4 |
| ba9058a1-422b-35c6-a36a-c8390e7f190b | -12.4554 | -45.1022 | 2025-09-22 13:50:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 78.9 |
| 8296b380-ef9b-33ae-883c-0b447ed2b0e0 | -8.9402 | -44.4688 | 2025-09-22 13:50:00 | GOES-19 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 68.3 |
| 062c2776-a3a5-3b46-95b9-5777c7416e7d | -11.2306 | -46.1722 | 2025-09-22 13:50:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 76.4 |
| 0ed0a896-b4fe-3153-b819-6a1c5917df73 | -14.2613 | -44.7041 | 2025-09-22 13:50:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 250.0 |
| 6e05b1c3-d718-374f-9dbc-c1d9eeb8b624 | -7.6007 | -44.4952 | 2025-09-22 13:50:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 68.2 |
| 18776336-b248-363f-a21a-d61ebdb7f6ba | -11.467 | -43.5485 | 2025-09-22 13:50:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 113.6 |
| 0d2dfba9-9891-3594-8844-2d746abbccbd | -7.6012 | -44.4492 | 2025-09-22 13:50:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 73.4 |
| 6ee5e38d-e189-3d9f-a61f-85634f57cd56 | -12.3592 | -44.0915 | 2025-09-22 13:50:00 | GOES-19 | TABOCAS DO BREJO VELHO | BAHIA | Brasil | 2930907 | 29 | 33 | nan | nan | nan | Cerrado | 164.8 |
| 29f60de2-549b-32ca-9e3d-8bcb7aed5039 | -5.5773 | -42.1255 | 2025-09-22 13:50:00 | GOES-19 | ALTO LONGÁ | PIAUÍ | Brasil | 2200301 | 22 | 33 | nan | nan | nan | Caatinga | 93.2 |
| 54ffccef-ee7b-34ad-8c34-865f2db197a1 | -12.4545 | -45.1486 | 2025-09-22 13:50:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 191.9 |
| f7dea25b-d3ea-3641-9d1c-8d2cb931dc81 | -11.435 | -50.1571 | 2025-09-22 13:50:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 74.8 |
| 8993b610-3a66-301b-9930-1acbca9ec299 | -5.5583 | -42.1507 | 2025-09-22 13:50:00 | GOES-19 | ALTO LONGÁ | PIAUÍ | Brasil | 2200301 | 22 | 33 | nan | nan | nan | Caatinga | 88.9 |
| d2bd8354-d941-3922-8a0b-883c5c4b3e08 | -11.9296 | -43.4288 | 2025-09-22 13:50:00 | GOES-19 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 127.2 |
| 3e4f9e27-1b4e-30af-ac69-90ab60cc67bb | -11.2343 | -49.5986 | 2025-09-22 13:50:00 | GOES-19 | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 159.9 |
| ed4cd008-bc1d-3ebb-bf20-97975822c421 | -12.455 | -45.1254 | 2025-09-22 13:50:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 115.8 |
| ad6886b3-9230-3a1c-be34-0fc69b873ec7 | -14.4726 | -44.8296 | 2025-09-22 13:50:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 117.0 |
| e0ed67a4-1f5d-36db-a5ea-77b30fe1889b | -8.2803 | -44.3801 | 2025-09-22 13:50:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 113.8 |
| 93761004-b009-3c72-801b-d6dc327dcbe2 | -18.5983 | -45.0287 | 2025-09-22 13:50:00 | GOES-19 | FELIXLÂNDIA | MINAS GERAIS | Brasil | 3125705 | 31 | 33 | nan | nan | nan | Cerrado | 174.6 |
| 447a777b-e51d-3b7c-847b-ef5867405ee9 | -12.6474 | -45.1183 | 2025-09-22 13:50:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 72.3 |
| 4c278142-23b8-39c2-a044-fea92985812f | -7.62 | -44.4474 | 2025-09-22 13:50:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 67.5 |
| 7cc7a4cb-0c48-3ef9-a331-a5530749fac8 | -9.3157 | -43.3758 | 2025-09-22 13:50:00 | GOES-19 | CARACOL | PIAUÍ | Brasil | 2202505 | 22 | 33 | nan | nan | nan | Caatinga | 79.8 |
| 02894b8f-024a-3917-a4ee-dda61310c2a1 | -12.0767 | -44.8131 | 2025-09-22 13:50:00 | GOES-19 | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 83.5 |
| db5ce35a-745a-3a12-b6b9-2fd6844de2ec | -12.1156 | -44.7839 | 2025-09-22 13:50:00 | GOES-19 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 93.1 |
| fc9d4ebd-2da0-3e03-82c5-4896765485ab | -14.4917 | -44.8496 | 2025-09-22 13:50:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 114.5 |
| 74d69ff5-4381-32ef-b3b3-eab54bb01b0e | -11.4674 | -43.5248 | 2025-09-22 13:50:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 135.3 |
| bc06fb96-7cae-3ebf-9d3a-d00d22d3c653 | -14.8479 | -45.4846 | 2025-09-22 13:50:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 241.0 |


[Clique aqui para ver as próximas entradas](README47.md)
