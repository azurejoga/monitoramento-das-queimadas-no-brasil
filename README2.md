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

## Dados Diários - Página 2

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 5f32d153-41ab-3f23-b750-0779cf65e305 | -12.86221 | -38.36713 | 2025-03-21 03:45:00 | NPP-375D | SALVADOR | BAHIA | Brasil | 2927408 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| b56515f7-ab4b-34be-bac2-ab2d43a59ec3 | -13.35589 | -41.34074 | 2025-03-21 03:45:00 | NPP-375D | IBICOARA | BAHIA | Brasil | 2912202 | 29 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 9fc2ac4f-56c4-3238-b404-ab558b2498bf | -11.89398 | -40.97521 | 2025-03-21 03:45:00 | NPP-375D | MORRO DO CHAPÉU | BAHIA | Brasil | 2921708 | 29 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 08c27ed3-513f-38bd-9760-4e2b703d766f | -12.77733 | -45.40718 | 2025-03-21 03:45:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 9742af49-3849-33ee-9288-310d90d411db | -12.78406 | -45.4047 | 2025-03-21 03:45:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 5bbb8d2c-529a-34b1-b5b2-b0b97d146faf | -15.79873 | -42.03288 | 2025-03-21 03:45:00 | NPP-375D | TAIOBEIRAS | MINAS GERAIS | Brasil | 3168002 | 31 | 33 | nan | nan | nan | Mata Atlântica | 9.7 |
| eefda43f-2ffb-3d04-8c2f-39d6207d9dbe | -12.19945 | -39.0461 | 2025-03-21 03:45:00 | NPP-375D | FEIRA DE SANTANA | BAHIA | Brasil | 2910800 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 1926cc3c-6c19-3280-8309-87aa6fba913c | -15.79969 | -42.02762 | 2025-03-21 03:45:00 | NPP-375D | TAIOBEIRAS | MINAS GERAIS | Brasil | 3168002 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.7 |
| 43d14a9d-2df5-3854-9758-abdb1b957537 | -12.78307 | -45.4051 | 2025-03-21 03:45:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| aa26206f-8353-3969-808c-2dc12f2af884 | -12.77829 | -45.40678 | 2025-03-21 03:45:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 44e4fe9e-63ac-3e30-a112-60ca603f7027 | -12.40423 | -39.24646 | 2025-03-21 03:45:00 | NPP-375D | SANTO ESTÊVÃO | BAHIA | Brasil | 2928802 | 29 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 2843f06d-23ed-3b25-a439-fda9f256bfc6 | -9.37156 | -41.58266 | 2025-03-21 03:45:00 | NPP-375D | CASA NOVA | BAHIA | Brasil | 2907202 | 29 | 33 | nan | nan | nan | Caatinga | 2.1 |
| ff8f0a91-1a55-309f-93a8-42183ab50e21 | -9.89229 | -38.21398 | 2025-03-21 03:45:00 | NPP-375D | JEREMOABO | BAHIA | Brasil | 2918100 | 29 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 94cfa9a4-bce5-3570-92f8-467649c9f2f7 | -9.89293 | -38.21006 | 2025-03-21 03:45:00 | NPP-375D | JEREMOABO | BAHIA | Brasil | 2918100 | 29 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 23271829-df7e-3cae-b062-f70620118d09 | -16.62654 | -43.16275 | 2025-03-21 03:45:00 | NPP-375D | GRÃO MOGOL | MINAS GERAIS | Brasil | 3127800 | 31 | 33 | nan | nan | nan | Cerrado | 3.6 |
| d2fb2b45-12c6-348b-89de-e96c93856f03 | -11.75097 | -39.15553 | 2025-03-21 03:45:00 | NPP-375D | ICHU | BAHIA | Brasil | 2913309 | 29 | 33 | nan | nan | nan | Caatinga | 3.9 |
| e285b383-9b83-3a0c-9c05-e8b0ac35fda5 | -12.79042 | -45.39954 | 2025-03-21 03:45:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 2820a404-5b75-3789-beda-85083f0704ce | -10.69734 | -37.04804 | 2025-03-21 03:45:00 | NPP-375D | ROSÁRIO DO CATETE | SERGIPE | Brasil | 2806107 | 28 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| fd0fce1e-eb93-38f5-9831-cf476ee28ea0 | -15.80265 | -42.03367 | 2025-03-21 03:45:00 | NPP-375D | TAIOBEIRAS | MINAS GERAIS | Brasil | 3168002 | 31 | 33 | nan | nan | nan | Mata Atlântica | 11.3 |
| 22b59dff-de11-37f8-bae3-bcea7a4e1b05 | -11.48653 | -40.04508 | 2025-03-21 03:45:00 | NPP-375D | SÃO JOSÉ DO JACUÍPE | BAHIA | Brasil | 2929370 | 29 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 7ef019dd-3b3d-3cbc-8721-d6bc74d06b77 | -12.77891 | -45.40364 | 2025-03-21 03:45:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| a2c6abc9-375a-3817-a28a-ec54e53d5b3c | -12.13224 | -39.77099 | 2025-03-21 03:45:00 | NPP-375D | IPIRÁ | BAHIA | Brasil | 2914000 | 29 | 33 | nan | nan | nan | Caatinga | 0.5 |
| 7ae8a2ae-7314-3538-b769-ddf9622688ad | -12.77953 | -45.4005 | 2025-03-21 03:45:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| f29f4583-7e5b-3602-a072-72e05e26f655 | -10.2455 | -40.50813 | 2025-03-21 03:45:00 | NPP-375D | CAMPO FORMOSO | BAHIA | Brasil | 2906006 | 29 | 33 | nan | nan | nan | Caatinga | 1.3 |
| ced291f4-3643-3017-90ba-1ae75adad29f | -12.78366 | -45.40197 | 2025-03-21 03:45:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 6f58c54f-3702-3967-b579-2bb4b9ddbdf8 | -11.74741 | -39.15492 | 2025-03-21 03:45:00 | NPP-375D | ICHU | BAHIA | Brasil | 2913309 | 29 | 33 | nan | nan | nan | Caatinga | 1.7 |
| da9b9fc7-de44-3164-9e0b-119473214288 | -27.84858 | -50.18275 | 2025-03-21 03:47:00 | NPP-375D | LAGES | SANTA CATARINA | Brasil | 4209300 | 42 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 8c75854c-31dc-3111-90ee-383d4cc77362 | -17.4893 | -39.45244 | 2025-03-21 03:47:00 | NPP-375D | ALCOBAÇA | BAHIA | Brasil | 2900801 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 44cb283c-b8c0-350f-9d4f-22a8d1070e5b | -19.83237 | -40.11423 | 2025-03-21 03:47:00 | NPP-375D | ARACRUZ | ESPÍRITO SANTO | Brasil | 3200607 | 32 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| 79a96c7d-0514-3377-b878-77d86e82b4a6 | -27.96519 | -51.63562 | 2025-03-21 03:47:00 | NPP-375D | SANTO EXPEDITO DO SUL | RIO GRANDE DO SUL | Brasil | 4317954 | 43 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 73a43cbc-544e-3e79-8545-a6c5547fb92e | -20.22855 | -46.61761 | 2025-03-21 03:47:00 | NPP-375D | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 08ae169b-7fcf-321f-9012-f31af0300f3d | -20.22715 | -46.61277 | 2025-03-21 03:47:00 | NPP-375D | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 9755fdb0-5b76-3eee-87ec-0354e53ac894 | -20.20719 | -46.67289 | 2025-03-21 03:47:00 | NPP-375D | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| d33df5fa-0b6d-3342-a9b8-645a4b05b8d7 | -20.22968 | -46.61203 | 2025-03-21 03:47:00 | NPP-375D | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 7d4fde0d-1b1c-33e7-9a78-702d5cbe435e | -20.11879 | -46.77975 | 2025-03-21 03:47:00 | NPP-375D | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 9a4e65c5-9cb8-32b5-8c67-211e7a326e6d | -20.34724 | -40.36237 | 2025-03-21 03:47:00 | NPP-375D | CARIACICA | ESPÍRITO SANTO | Brasil | 3201308 | 32 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 030a4d11-58ba-33e3-95fc-9cf12792f8f2 | -20.76298 | -46.77101 | 2025-03-21 03:47:00 | NPP-375D | ITAÚ DE MINAS | MINAS GERAIS | Brasil | 3133758 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 893a2e02-3e06-3c20-8540-7645fc30ae9f | -27.84928 | -50.17957 | 2025-03-21 03:47:00 | NPP-375D | LAGES | SANTA CATARINA | Brasil | 4209300 | 42 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 4b7c9777-304e-36b1-8f9d-31b2a6a06a8a | -20.22598 | -46.61834 | 2025-03-21 03:47:00 | NPP-375D | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 8f1ac574-4f71-36b4-bc30-039761b572d0 | -20.21905 | -46.66454 | 2025-03-21 03:47:00 | NPP-375D | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| f30a1c99-9433-3a04-a826-b320a228129e | -20.21362 | -46.6771 | 2025-03-21 03:47:00 | NPP-375D | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| a95e06a7-deef-3e11-a039-ad4d729c4000 | -20.22081 | -46.6671 | 2025-03-21 03:47:00 | NPP-375D | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| c00c3f43-8a09-3b36-8f32-22c69e1bf53f | -20.23316 | -46.60828 | 2025-03-21 03:47:00 | NPP-375D | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 2e5ebb68-080c-3948-89ea-95d8d2835ba0 | -21.26089 | -49.04068 | 2025-03-21 03:47:00 | NPP-375D | ITAJOBI | SÃO PAULO | Brasil | 3521903 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| cb16677b-c716-384a-8c56-6f22d5677999 | -27.39036 | -51.17822 | 2025-03-21 03:47:00 | NPP-375D | CAMPOS NOVOS | SANTA CATARINA | Brasil | 4203600 | 42 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 95a89895-c9c4-374d-822b-75e8e8e73da9 | -27.84776 | -50.18624 | 2025-03-21 03:47:00 | NPP-375D | LAGES | SANTA CATARINA | Brasil | 4209300 | 42 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| b843e207-5fe0-37f1-a7c8-0c9092116b10 | -20.23086 | -46.60621 | 2025-03-21 03:47:00 | NPP-375D | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| df445b1d-0e7f-389d-a22a-72c5b617b338 | -18.12021 | -39.6857 | 2025-03-21 03:47:00 | NPP-375D | MUCURI | BAHIA | Brasil | 2922003 | 29 | 33 | nan | nan | nan | Mata Atlântica | 2.5 |
| 9b980e56-bcaf-373d-ab23-b53d2966db0d | -20.20898 | -46.67497 | 2025-03-21 03:47:00 | NPP-375D | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 77998ddd-9062-3346-9fe5-65353f0e7858 | -27.84848 | -50.18307 | 2025-03-21 03:47:00 | NPP-375D | LAGES | SANTA CATARINA | Brasil | 4209300 | 42 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| ecb08855-c07d-3b14-9eb5-d98df3daac4a | -20.21064 | -46.68096 | 2025-03-21 03:47:00 | NPP-375D | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 3acc6d40-f1a6-3fe5-b782-1dde5f860ab4 | -20.13242 | -46.78817 | 2025-03-21 03:47:00 | NPP-375D | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 41dcb99c-08f2-3548-b49e-93aef7e4c537 | -20.12746 | -46.78735 | 2025-03-21 03:47:00 | NPP-375D | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 406d64f6-e2ca-31a3-9fd3-a4b7027cb77d | -20.21193 | -46.67459 | 2025-03-21 03:47:00 | NPP-375D | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| ab64b9cf-ab23-3f43-abcd-5f64d850987f | -17.46791 | -39.24447 | 2025-03-21 03:47:00 | NPP-375D | ALCOBAÇA | BAHIA | Brasil | 2900801 | 29 | 33 | nan | nan | nan | Mata Atlântica | 2.3 |
| 3432841f-f2b1-326f-9ce2-675dcfe1a371 | -20.11503 | -46.77318 | 2025-03-21 03:47:00 | NPP-375D | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 0871a917-ae1e-36f8-acef-77251121d8eb | -17.46854 | -39.24068 | 2025-03-21 03:47:00 | NPP-375D | ALCOBAÇA | BAHIA | Brasil | 2900801 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.4 |
| 8658698e-5e71-31ac-b09e-a01087f53ee6 | -27.38601 | -51.17921 | 2025-03-21 03:47:00 | NPP-375D | CAMPOS NOVOS | SANTA CATARINA | Brasil | 4203600 | 42 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| 93e9d190-1b81-3af7-8369-67c7a9e55969 | -20.21777 | -46.67087 | 2025-03-21 03:47:00 | NPP-375D | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 170df1d5-715d-3cad-9e71-c061cf8caca2 | -20.12869 | -46.78146 | 2025-03-21 03:47:00 | NPP-375D | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 61f77ecb-848d-3a03-8e55-efd68558de62 | -19.83303 | -40.11034 | 2025-03-21 03:47:00 | NPP-375D | ARACRUZ | ESPÍRITO SANTO | Brasil | 3200607 | 32 | 33 | nan | nan | nan | Mata Atlântica | 4.9 |
| 0edb8eba-46af-3ac3-91e7-fd3ac09108ee | -20.12499 | -46.7746 | 2025-03-21 03:47:00 | NPP-375D | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 8b2123e6-4cd4-3f3a-bc89-ab498fa0fa10 | -27.97066 | -51.6375 | 2025-03-21 03:47:00 | NPP-375D | LAGOA VERMELHA | RIO GRANDE DO SUL | Brasil | 4311304 | 43 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| afe8ad4c-59d3-332a-9e3c-36e8872a0f5d | -27.38697 | -51.17514 | 2025-03-21 03:47:00 | NPP-375D | CAMPOS NOVOS | SANTA CATARINA | Brasil | 4203600 | 42 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| dbd76926-c055-3ef6-aad9-57fd95f4a559 | -20.21029 | -46.66876 | 2025-03-21 03:47:00 | NPP-375D | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 5ce764e5-85aa-3e94-9b72-29ae983ab0f0 | -20.12005 | -46.77368 | 2025-03-21 03:47:00 | NPP-375D | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 4.3 |
| eb9ee2cd-3600-3834-97c9-86fc95e4298b | -20.21496 | -46.67072 | 2025-03-21 03:47:00 | NPP-375D | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| f5896c54-7070-3230-ac3b-21ea2ede39a7 | -20.11626 | -46.7673 | 2025-03-21 03:47:00 | NPP-375D | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 3.7 |
| afb789f3-0927-358a-8be6-f55bb7dd36e5 | -27.38497 | -51.17633 | 2025-03-21 03:47:00 | NPP-375D | CAMPOS NOVOS | SANTA CATARINA | Brasil | 4203600 | 42 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| ac53be1c-d410-32e0-8d3e-25d535d7a0c4 | -20.2123 | -46.68335 | 2025-03-21 03:47:00 | NPP-375D | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| c4da018e-d8d7-39bf-9eee-a9315ef5af13 | -30.71409 | -54.18576 | 2025-03-21 03:49:00 | NPP-375D | SÃO GABRIEL | RIO GRANDE DO SUL | Brasil | 4318309 | 43 | 33 | nan | nan | nan | Pampa | 1.7 |
| 52ddf381-d697-32ca-b346-46c73c5e7dae | -30.70823 | -54.18346 | 2025-03-21 03:49:00 | NPP-375D | SÃO GABRIEL | RIO GRANDE DO SUL | Brasil | 4318309 | 43 | 33 | nan | nan | nan | Pampa | 1.7 |
| 0f01c4b0-97ee-3d53-b74d-45d6b29fd82d | -31.31784 | -54.15946 | 2025-03-21 03:49:00 | NPP-375D | BAGÉ | RIO GRANDE DO SUL | Brasil | 4301602 | 43 | 33 | nan | nan | nan | Pampa | 6.5 |
| 9dc7d671-fee6-3513-9f31-0edfd315462e | -30.70793 | -54.18201 | 2025-03-21 03:49:00 | NPP-375D | SÃO GABRIEL | RIO GRANDE DO SUL | Brasil | 4318309 | 43 | 33 | nan | nan | nan | Pampa | 1.7 |
| f047a633-c0d3-3acc-b46f-e9bead0115e3 | -30.72334 | -54.19962 | 2025-03-21 03:49:00 | NPP-375D | SÃO GABRIEL | RIO GRANDE DO SUL | Brasil | 4318309 | 43 | 33 | nan | nan | nan | Pampa | 1.9 |
| 66b2b9c8-a92a-3ad0-b9f5-22701d1b7173 | -25.1908 | -49.32798 | 2025-03-21 03:49:00 | NPP-375D | RIO BRANCO DO SUL | PARANÁ | Brasil | 4122206 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| a86fe9e9-d028-3b90-8cec-b57590599aed | -23.98396 | -48.91986 | 2025-03-21 03:49:00 | NPP-375D | ITAPEVA | SÃO PAULO | Brasil | 3522406 | 35 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 02e32566-c4e2-3490-b135-a42c956a457b | -30.73066 | -54.19641 | 2025-03-21 03:49:00 | NPP-375D | SÃO GABRIEL | RIO GRANDE DO SUL | Brasil | 4318309 | 43 | 33 | nan | nan | nan | Pampa | 3.9 |
| 3aaca597-91b1-3a56-bf61-52de9fe9db87 | -23.98405 | -48.91773 | 2025-03-21 03:49:00 | NPP-375D | ITAPEVA | SÃO PAULO | Brasil | 3522406 | 35 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 43921df3-e142-3b02-a912-4e130f873d6a | -30.73211 | -54.19101 | 2025-03-21 03:49:00 | NPP-375D | SÃO GABRIEL | RIO GRANDE DO SUL | Brasil | 4318309 | 43 | 33 | nan | nan | nan | Pampa | 2.0 |
| c3139c77-432b-326e-84a1-e18f1ae8d4a2 | -23.98469 | -48.91654 | 2025-03-21 03:49:00 | NPP-375D | ITAPEVA | SÃO PAULO | Brasil | 3522406 | 35 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 8eccb43b-8041-3367-a14e-c8187524fd17 | -6.92688 | -35.13861 | 2025-03-21 04:04:00 | NOAA-20 | CAPIM | PARAÍBA | Brasil | 2504033 | 25 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 6c2b02ad-8dac-3c76-a218-9acb7a7500be | -6.92309 | -35.13368 | 2025-03-21 04:04:00 | NOAA-20 | CAPIM | PARAÍBA | Brasil | 2504033 | 25 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| deaac471-0761-3825-8474-647128bf2808 | -3.30053 | -39.25029 | 2025-03-21 04:04:00 | NOAA-20 | TRAIRI | CEARÁ | Brasil | 2313500 | 23 | 33 | nan | nan | nan | Caatinga | 0.8 |
| b8d9d49f-4b65-37e8-b91b-b718c6de0133 | -3.12488 | -40.99128 | 2025-03-21 04:04:00 | NOAA-20 | GRANJA | CEARÁ | Brasil | 2304707 | 23 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 60f89a2d-1dfe-3de1-94c9-2780338be43e | -2.9273 | -39.98104 | 2025-03-21 04:04:00 | NOAA-20 | ACARAÚ | CEARÁ | Brasil | 2300200 | 23 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 0c0af4ad-1951-30b1-9386-a997421e2751 | -6.05131 | -39.43589 | 2025-03-21 04:04:00 | NOAA-20 | ACOPIARA | CEARÁ | Brasil | 2300309 | 23 | 33 | nan | nan | nan | Caatinga | 0.6 |
| f9d233f7-4bc0-3a2b-a770-5205763bdcb7 | -6.92751 | -35.1343 | 2025-03-21 04:04:00 | NOAA-20 | CAPIM | PARAÍBA | Brasil | 2504033 | 25 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| bd67850f-f37e-30c9-bdcf-63f43c546ecc | -9.88968 | -38.21419 | 2025-03-21 04:06:00 | NOAA-20 | JEREMOABO | BAHIA | Brasil | 2918100 | 29 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 40b28aa6-da29-3bd8-b92e-3474eaa69020 | -11.75033 | -39.15421 | 2025-03-21 04:06:00 | NOAA-20 | ICHU | BAHIA | Brasil | 2913309 | 29 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 208851ad-5fde-32da-b3cc-b4438c29ec67 | -11.20853 | -40.25622 | 2025-03-21 04:06:00 | NOAA-20 | JACOBINA | BAHIA | Brasil | 2917508 | 29 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 7c3de508-76c8-394d-9bd8-425b25a159ec | -8.67468 | -36.24102 | 2025-03-21 04:06:00 | NOAA-20 | LAJEDO | PERNAMBUCO | Brasil | 2608800 | 26 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 4c2d1587-8625-3ce5-b23d-4e6431aece8e | -13.35529 | -41.34109 | 2025-03-21 04:06:00 | NOAA-20 | IBICOARA | BAHIA | Brasil | 2912202 | 29 | 33 | nan | nan | nan | Caatinga | 0.4 |
| 10c9b33b-e604-3451-87f8-2fb4e7cef938 | -10.24295 | -40.51188 | 2025-03-21 04:06:00 | NOAA-20 | CAMPO FORMOSO | BAHIA | Brasil | 2906006 | 29 | 33 | nan | nan | nan | Caatinga | 1.2 |
| ec0c75e5-c8ff-3ca3-b5c6-81616fb477e0 | -11.89132 | -40.97685 | 2025-03-21 04:06:00 | NOAA-20 | MORRO DO CHAPÉU | BAHIA | Brasil | 2921708 | 29 | 33 | nan | nan | nan | Caatinga | 1.8 |
| fe34d94e-2d3a-3092-be66-7e9b36fbbe03 | -9.11701 | -40.61707 | 2025-03-21 04:06:00 | NOAA-20 | PETROLINA | PERNAMBUCO | Brasil | 2611101 | 26 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 825fea6b-1225-3d1d-bec6-fffda4eeca57 | -8.39084 | -35.02509 | 2025-03-21 04:06:00 | NOAA-20 | IPOJUCA | PERNAMBUCO | Brasil | 2607208 | 26 | 33 | nan | nan | nan | Mata Atlântica | 4.4 |
| a390cb7c-bb37-3b91-b198-44a84e12431a | -12.27857 | -43.52479 | 2025-03-21 04:06:00 | NOAA-20 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| a4342974-fba0-364e-8393-f21e877a850c | -11.48559 | -40.04188 | 2025-03-21 04:06:00 | NOAA-20 | SÃO JOSÉ DO JACUÍPE | BAHIA | Brasil | 2929370 | 29 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 391ec2c1-fb0d-3c7b-89ab-1df3281f5c29 | -13.35868 | -41.34162 | 2025-03-21 04:06:00 | NOAA-20 | IBICOARA | BAHIA | Brasil | 2912202 | 29 | 33 | nan | nan | nan | Caatinga | 2.5 |


[Clique aqui para ver as próximas entradas](README3.md)
