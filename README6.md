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

## Dados Diários - Página 6

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 911913be-647b-3520-ad28-09f94efa7ce0 | -6.95222 | -42.73864 | 2025-07-13 04:19:00 | NOAA-21 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 20.3 |
| 1cb14b49-8873-3b7f-ba09-c77c1d7a1619 | -6.78415 | -43.96461 | 2025-07-13 04:19:00 | NOAA-21 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 372773fd-61b9-3da6-99db-561e58c746a8 | -6.78082 | -43.96409 | 2025-07-13 04:19:00 | NOAA-21 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 5db290ad-fada-3d71-9552-bccf3333efeb | -6.49036 | -45.26118 | 2025-07-13 04:19:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 43652d0e-723a-3c7e-9510-92b458cb6baa | -7.30978 | -45.32757 | 2025-07-13 04:19:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| fb5d8cdf-c4fa-3e84-a807-9e620af42c42 | -4.29012 | -48.06258 | 2025-07-13 04:19:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| bfcccc5d-0723-3c06-b900-3d4b820de914 | -5.54713 | -40.17884 | 2025-07-13 04:19:00 | NOAA-21 | INDEPENDÊNCIA | CEARÁ | Brasil | 2305605 | 23 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 8cfd2e95-b913-3033-b4ce-cf0e5db3c2c8 | -5.74713 | -44.98686 | 2025-07-13 04:19:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 5.3 |
| d4f36d25-a781-3c16-b133-6b8a7f985cde | -6.23234 | -43.34808 | 2025-07-13 04:19:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 4e9cdf5c-448b-335f-8525-df0e2a0fbac3 | -7.15107 | -43.78562 | 2025-07-13 04:19:00 | NOAA-21 | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 187f81e7-1be9-3819-b28b-d537a71d6eb0 | -6.62547 | -43.01939 | 2025-07-13 04:19:00 | NOAA-21 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 72341dd6-f6c1-3707-bfa3-81af6873f49d | -6.26699 | -45.2751 | 2025-07-13 04:19:00 | NOAA-21 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 02905e0c-8398-3e2a-aaf7-f6fa3b5ae6ad | -6.43636 | -43.04006 | 2025-07-13 04:19:00 | NOAA-21 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 483e6691-a7d3-3b8d-bc67-12a147549c36 | -6.63773 | -43.1907 | 2025-07-13 04:19:00 | NOAA-21 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 84d0845f-64e1-3534-94ab-bee14d11113d | -5.74382 | -44.98634 | 2025-07-13 04:19:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 13.3 |
| bab88731-d4db-36fd-b931-9394b8a254ec | -8.50627 | -43.28537 | 2025-07-13 04:19:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 7.1 |
| 418d1997-30d8-3c38-a321-952ae54b5c21 | -7.10856 | -40.39148 | 2025-07-13 04:19:00 | NOAA-21 | SALITRE | CEARÁ | Brasil | 2311959 | 23 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 5ea4d0d4-947e-383d-8a76-90aa3c0c99ef | -7.02172 | -43.29692 | 2025-07-13 04:19:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 9324db04-26af-3fc4-b272-3f2daeffc90e | -6.45614 | -45.3687 | 2025-07-13 04:19:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 2708fc04-c97e-30a8-a3f5-59cf3de7279b | -7.98585 | -43.38982 | 2025-07-13 04:19:00 | NOAA-21 | PAVUSSU | PIAUÍ | Brasil | 2207850 | 22 | 33 | nan | nan | nan | Cerrado | 9.9 |
| 4526e7ab-ed59-3348-83ae-206677443e68 | -7.28773 | -45.31702 | 2025-07-13 04:19:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 8290e5af-8969-3e78-a347-494fb830dce5 | -7.29489 | -44.02561 | 2025-07-13 04:19:00 | NOAA-21 | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 0d760ff6-1167-3ea5-91fb-1f840e9c06b5 | -3.39543 | -46.90818 | 2025-07-13 04:19:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 85010780-3fcb-3385-a4d9-4c049ff6d6be | -7.28882 | -45.31009 | 2025-07-13 04:19:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 7948efea-ec32-3c0a-a7f4-73460e96f3d6 | -7.11247 | -40.39211 | 2025-07-13 04:19:00 | NOAA-21 | SALITRE | CEARÁ | Brasil | 2311959 | 23 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 0e9c030f-4ec2-392e-9b13-3d416f7342c4 | -6.28247 | -43.42567 | 2025-07-13 04:19:00 | NOAA-21 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 4259417d-7480-35a5-b1dd-1528634a87e9 | -7.18687 | -42.96981 | 2025-07-13 04:19:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 6a4992ba-a412-3871-8af7-057924114174 | -5.88608 | -42.90142 | 2025-07-13 04:19:00 | NOAA-21 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 0.7 |
| f736f194-d510-3078-8b4f-db36ed8166bd | -6.24853 | -43.69037 | 2025-07-13 04:19:00 | NOAA-21 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 8ca14b04-3566-3db5-b783-712cf815d67c | -7.09479 | -44.06686 | 2025-07-13 04:19:00 | NOAA-21 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 52a2c2b9-0a31-3c6e-b3c0-55680f085f3f | -7.18067 | -43.01091 | 2025-07-13 04:19:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 57cb01a2-f64b-3639-84b2-1c66c44543f2 | -4.29522 | -48.05434 | 2025-07-13 04:19:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 555d3975-67c5-3245-a77a-959d0f16be6d | -7.15083 | -42.29033 | 2025-07-13 04:19:00 | NOAA-21 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| e95e7b90-a182-37df-855f-d63c2754dc62 | -6.82812 | -42.88586 | 2025-07-13 04:19:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 48b5cbfe-c15a-3a99-8ac7-a77923fb7ec5 | -5.23898 | -40.87372 | 2025-07-13 04:19:00 | NOAA-21 | CRATEÚS | CEARÁ | Brasil | 2304103 | 23 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 3a47f805-1e19-38c0-a1a6-01e3a0659958 | -7.49194 | -43.9367 | 2025-07-13 04:19:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 3.4 |
| fa1f68b6-9777-3007-9341-6211a67357df | -4.53513 | -48.02499 | 2025-07-13 04:19:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c9c4d718-4c87-30ed-914a-7cc5ff470b85 | -5.79185 | -42.96565 | 2025-07-13 04:19:00 | NOAA-21 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 9bb6b67b-2900-382f-9e05-26472c45b64a | -7.26447 | -43.49426 | 2025-07-13 04:19:00 | NOAA-21 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| e5f306b0-14f8-3181-bc09-cf2fe9f43751 | -6.25145 | -43.35836 | 2025-07-13 04:19:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| e3880d6f-4021-346a-9652-a2b5ce19c1d8 | -6.94876 | -42.73812 | 2025-07-13 04:19:00 | NOAA-21 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 5.9 |
| 78671024-f539-3b4a-a0ff-7e68f53a53a6 | -7.17438 | -43.00613 | 2025-07-13 04:19:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 83e1af13-8464-3659-b8ce-0c68c9a91baa | -4.93611 | -46.72659 | 2025-07-13 04:19:00 | NOAA-21 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| df5db90e-82fd-35b4-8ad5-c33bbd181b78 | -6.94705 | -43.92102 | 2025-07-13 04:19:00 | NOAA-21 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 7c6c57ec-c00f-304e-ac4d-8a063d02fcca | -8.35001 | -45.63568 | 2025-07-13 04:19:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 8b2bdbc2-8e54-32a7-9136-68122976de6d | -4.28955 | -48.05625 | 2025-07-13 04:19:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| ffa4147a-1d52-3668-a69a-048971465ad7 | -8.5057 | -43.28913 | 2025-07-13 04:19:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 7.9 |
| 5cb00159-59fe-3bf4-9869-aed350ed17ee | -5.7449 | -44.97943 | 2025-07-13 04:19:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| a0f975d7-c56c-3e02-b771-4ef3007e3d71 | -7.30421 | -45.29832 | 2025-07-13 04:19:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 7faeb0a4-b378-36e0-bdaf-0efa01f4b7cd | -6.28022 | -43.41797 | 2025-07-13 04:19:00 | NOAA-21 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 9fcb5e34-cb1c-3c14-bf6d-fc628c6ecf58 | -6.5211 | -43.35561 | 2025-07-13 04:19:00 | NOAA-21 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 1d72284e-464f-303f-8868-b156702628db | -8.3511 | -45.62875 | 2025-07-13 04:19:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| cdd51e58-2357-3728-b8a9-d8cea42d0526 | -6.71382 | -44.32964 | 2025-07-13 04:19:00 | NOAA-21 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 1d9ebe6a-105f-38a8-95d8-0ea5a423fb74 | -5.59603 | -50.0783 | 2025-07-13 04:19:00 | NOAA-21 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 5db34735-549c-3f5f-b3a0-f2f4414781bf | -7.29877 | -44.02262 | 2025-07-13 04:19:00 | NOAA-21 | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 9ac2b5a1-b7ce-3361-8213-0ef41319336a | -6.65346 | -43.11049 | 2025-07-13 04:19:00 | NOAA-21 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 909dfc5e-73df-3a0d-a85a-8ce2f5a1469d | -6.83384 | -42.87146 | 2025-07-13 04:19:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 4d76cf31-7d50-3afe-b2fd-2c540ca4bfc8 | -7.09092 | -44.06985 | 2025-07-13 04:19:00 | NOAA-21 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| cd15c83b-a8e4-3550-8a03-d967f8c51889 | -6.63434 | -43.19019 | 2025-07-13 04:19:00 | NOAA-21 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 4b427fd0-2a73-3e91-8afd-6b3c8d05692a | -3.97782 | -48.41693 | 2025-07-13 04:19:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e78c0c91-544f-3056-90ca-03ee189fce5e | -7.28828 | -45.31355 | 2025-07-13 04:19:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| c2551246-ef37-3c7f-a05f-6373530d53fc | -7.28112 | -45.31598 | 2025-07-13 04:19:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| dcc1e04b-b224-33a0-bc64-d5f2a3ae50f8 | -5.27321 | -44.95107 | 2025-07-13 04:19:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 55c5a262-b803-3807-ac06-93d143857a29 | -6.2509 | -43.36198 | 2025-07-13 04:19:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 7b26876b-4d39-3f19-98a0-087042535608 | -5.74767 | -44.9834 | 2025-07-13 04:19:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 65d0235b-cd67-328e-bf5c-58276a2ec5e5 | -3.6967 | -43.39201 | 2025-07-13 04:19:00 | NOAA-21 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 52bc8670-9cd2-3942-8918-1699afd89213 | -2.90817 | -48.88878 | 2025-07-13 04:19:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 652d9b91-a95e-393a-b009-44f2de14b898 | -6.28077 | -43.41437 | 2025-07-13 04:19:00 | NOAA-21 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 27d0b8c3-6bc7-3ccc-9d2d-d0a9094119fe | -7.98982 | -43.38665 | 2025-07-13 04:19:00 | NOAA-21 | PAVUSSU | PIAUÍ | Brasil | 2207850 | 22 | 33 | nan | nan | nan | Cerrado | 9.9 |
| c4c620c3-a258-37c1-b4e4-ec9eba23537f | -8.34889 | -45.62128 | 2025-07-13 04:19:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| d4ec68d5-1ca3-378c-b340-30906922b68c | -6.4245 | -48.54219 | 2025-07-13 04:19:00 | NOAA-21 | XAMBIOÁ | TOCANTINS | Brasil | 1722107 | 17 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 0efe7488-799d-3b9a-a830-bb1a0792461a | -5.62533 | -44.26473 | 2025-07-13 04:19:00 | NOAA-21 | SÃO DOMINGOS DO MARANHÃO | MARANHÃO | Brasil | 2110708 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| ac96682e-048d-3c03-ac0f-7c9d0bc28ced | -3.75576 | -47.10563 | 2025-07-13 04:19:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 047a8269-ae44-3518-bbf9-7839304858a6 | -7.1903 | -42.97033 | 2025-07-13 04:19:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| a665914e-0553-3e0e-a7e6-9216fc04964c | -6.83041 | -42.87093 | 2025-07-13 04:19:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| b690dcb5-fc0c-321b-88ca-2c94a5935f30 | -7.18123 | -43.0072 | 2025-07-13 04:19:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 518e8c1c-9877-3a4f-b5f5-25191cd5215b | -6.6215 | -43.02259 | 2025-07-13 04:19:00 | NOAA-21 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 686f0cbe-4d45-3ce4-b031-2fab597b697d | -4.29325 | -48.05688 | 2025-07-13 04:19:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 355161c1-2b3b-35e5-a429-38af18b0526b | -7.09297 | -44.38526 | 2025-07-13 04:19:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 5199a4bb-dc2c-3558-800f-442d5e7c64e5 | -6.7481 | -44.70009 | 2025-07-13 04:19:00 | NOAA-21 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 12127945-7a60-358b-aeeb-d55446de566c | -6.78306 | -43.97165 | 2025-07-13 04:19:00 | NOAA-21 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 53574a7a-4785-38f8-b767-ec0cfccb96cc | -6.71713 | -44.33016 | 2025-07-13 04:19:00 | NOAA-21 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 2c92322f-062d-3a81-ae3f-c7b664544e35 | -7.61033 | -49.93873 | 2025-07-13 04:19:00 | NOAA-21 | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 50913e4a-3766-3beb-90a4-848c53eff4c3 | -4.30222 | -48.07182 | 2025-07-13 04:19:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 4567ffe5-4f31-333e-ae45-8a0669aa9864 | -4.85833 | -43.22245 | 2025-07-13 04:19:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 27719c84-4e63-307d-b255-07f9281070f4 | -3.61469 | -47.54769 | 2025-07-13 04:19:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 7.3 |
| 3667f21f-a3c5-372a-a06b-4f9e4929a72a | -5.27375 | -44.94762 | 2025-07-13 04:19:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| d2d511ce-1596-33dc-ac4f-97c3da431b2e | -6.82984 | -42.87466 | 2025-07-13 04:19:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 1e76131a-a487-3b42-9e72-c95c3b0ba781 | -8.01356 | -50.10311 | 2025-07-13 04:19:00 | NOAA-21 | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 81f5b9aa-994b-3649-a4ed-cd393be72a1a | -3.61832 | -47.5483 | 2025-07-13 04:19:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 7.3 |
| 7adfcec1-91c0-39df-87ca-2d424f8b4002 | -6.7836 | -43.96813 | 2025-07-13 04:19:00 | NOAA-21 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 74f13585-0135-3127-b098-ff3695a2ef1e | -5.74436 | -44.98288 | 2025-07-13 04:19:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 13.3 |
| ff9bbd22-8bab-36f2-970a-4d54403bc069 | -4.45191 | -48.29243 | 2025-07-13 04:19:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| d3e0016b-06fb-3793-a0ff-98a83f90c190 | -5.53051 | -43.89126 | 2025-07-13 04:19:00 | NOAA-21 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 8938086f-b23f-3c79-9d79-afad0e6862fe | -5.41226 | -49.08123 | 2025-07-13 04:19:00 | NOAA-21 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| d6b69c4a-4ad1-3e05-9de3-be3bc63fb9c8 | -7.69502 | -44.34019 | 2025-07-13 04:19:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| b64e5771-dbd0-3ba7-8fef-1d01191dfaf3 | -7.31032 | -45.32411 | 2025-07-13 04:19:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| b8d1b704-feda-380a-8e78-514c633fb777 | -7.02511 | -43.29745 | 2025-07-13 04:19:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 1d41858f-f57b-3304-a6e5-9ac024918be7 | -4.66649 | -44.63276 | 2025-07-13 04:19:00 | NOAA-21 | BERNARDO DO MEARIM | MARANHÃO | Brasil | 2101939 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 2343ffaa-c3f0-3531-8c45-cce50c7e7d32 | -7.17944 | -42.97249 | 2025-07-13 04:19:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |


[Clique aqui para ver as próximas entradas](README7.md)
