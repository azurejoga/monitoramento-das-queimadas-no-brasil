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

## Dados Diários - Página 12

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| a0df7422-5cf9-3190-8b14-ce814b922583 | -5.81688 | -44.12399 | 2024-10-08 00:35:00 | TERRA_M-M | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 119.1 |
| 746d7e32-87be-3f4f-a871-5e3679229e45 | -11.32489 | -51.03286 | 2024-10-08 00:35:00 | TERRA_M-M | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 226.3 |
| e6adb912-bb55-3c16-a6c9-8bbdf5f8daa4 | -5.75153 | -49.25142 | 2024-10-08 00:35:00 | TERRA_M-M | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 14.5 |
| e44b3f71-5945-3455-8889-d42a4a3facba | -5.75131 | -49.25796 | 2024-10-08 00:35:00 | TERRA_M-M | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 13.7 |
| e58c6a57-3959-3b7e-a275-0f4570b07e46 | -5.71036 | -46.46231 | 2024-10-08 00:35:00 | TERRA_M-M | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 11.4 |
| cb55db55-cc6a-355d-87ac-dcfe25d198c9 | -5.57926 | -44.88057 | 2024-10-08 00:35:00 | TERRA_M-M | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 45.4 |
| 9d960016-62cb-3463-9a90-25c7fd4b2395 | -5.57794 | -44.87086 | 2024-10-08 00:35:00 | TERRA_M-M | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 23.2 |
| 5695bb97-31a3-3a66-9edd-65db930a9871 | -5.57135 | -44.8916 | 2024-10-08 00:35:00 | TERRA_M-M | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 8.9 |
| 391b177a-e157-3a38-948a-088917e96cbb | -5.57003 | -44.88187 | 2024-10-08 00:35:00 | TERRA_M-M | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 159.0 |
| 71f2f8c3-9811-394f-af83-4c272fc16bc5 | -5.56873 | -44.87222 | 2024-10-08 00:35:00 | TERRA_M-M | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 46.6 |
| 93c4df87-ffb6-3541-a3d7-67aaa365baee | -5.56556 | -46.29641 | 2024-10-08 00:35:00 | TERRA_M-M | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 7.5 |
| 4670f65d-5719-310b-ac07-935ab1b92b31 | -5.56403 | -46.28482 | 2024-10-08 00:35:00 | TERRA_M-M | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 370db870-f998-3480-b40d-dfb637f9b3b9 | -5.51679 | -45.49207 | 2024-10-08 00:35:00 | TERRA_M-M | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 7.8 |
| 2372d99b-318a-3b1b-af8f-e86c769ef93c | -5.50552 | -46.38223 | 2024-10-08 00:35:00 | TERRA_M-M | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 7.5 |
| 66f7e8c5-f38d-399f-8bd9-f77974a5d8a1 | -2.78 | -48.5806 | 2024-10-08 00:35:22 | GOES-16 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 44.9 |
| 8d5dcbe6-1701-34f9-a7f5-d06f38148877 | -2.7985 | -48.5801 | 2024-10-08 00:35:22 | GOES-16 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 42.7 |
| 7fe240a3-94bf-3b87-85f1-a874d6445d84 | -2.9797 | -49.5342 | 2024-10-08 00:35:23 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 59.5 |
| aece1b10-7dec-30e7-a038-fe3293f90093 | -3.2862 | -47.133 | 2024-10-08 00:35:25 | GOES-16 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 50.8 |
| 09ea3077-9027-3b9f-aa5f-e797185443e5 | -3.2863 | -47.1111 | 2024-10-08 00:35:25 | GOES-16 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 34.5 |
| 8f9693d3-bbe5-31c0-b1cd-7c0dc90dbbab | -4.4468 | -42.9123 | 2024-10-08 00:35:31 | GOES-16 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 80.1 |
| 5868d976-5120-33ad-ad01-bccb0662fbcc | -4.447 | -42.8889 | 2024-10-08 00:35:31 | GOES-16 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 74.6 |
| 5bb26f2b-dfa1-3a91-96a0-386c5c005da4 | -5.015 | -49.5999 | 2024-10-08 00:35:35 | GOES-16 | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 51.3 |
| 68102790-eabd-3f61-9666-24b9c940525e | -5.5716 | -44.8927 | 2024-10-08 00:35:38 | GOES-16 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 72.2 |
| 5bf8a2e8-a229-3092-ab13-96813bf143e4 | -5.5718 | -44.87 | 2024-10-08 00:35:38 | GOES-16 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 117.0 |
| f0f76f93-5b17-3e90-ac12-cd30cfcc43d4 | -5.8216 | -44.1196 | 2024-10-08 00:35:39 | GOES-16 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 70.9 |
| c8e195e2-7e2c-3b3e-92e3-8a199befa676 | -9.4087 | -66.5438 | 2024-10-08 00:36:00 | GOES-16 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 48.9 |
| f2eed6bc-765b-39ac-a247-7164c5c09362 | -9.445 | -66.7289 | 2024-10-08 00:36:00 | GOES-16 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 68.5 |
| 44ce530c-e9bb-345b-b30b-d325e37177eb | -9.4635 | -66.7283 | 2024-10-08 00:36:01 | GOES-16 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 50.1 |
| b44fa462-862a-3e8b-8af8-70dacac4384e | -9.572 | -67.4315 | 2024-10-08 00:36:01 | GOES-16 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 63.7 |
| c03c8794-ebbc-3438-a8dd-03bb21275b13 | -10.0653 | -45.2761 | 2024-10-08 00:36:03 | GOES-16 | SÃO GONÇALO DO GURGUÉIA | PIAUÍ | Brasil | 2209757 | 22 | 33 | nan | nan | nan | Cerrado | 61.2 |
| 30d04dc0-bc3b-3202-9c24-ac1cd47eb490 | -10.1261 | -55.2093 | 2024-10-08 00:36:04 | GOES-16 | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 82.2 |
| 7788197e-3eff-3f43-9b8c-9e7225f9fbd7 | -10.1263 | -55.1891 | 2024-10-08 00:36:04 | GOES-16 | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 103.0 |
| 073ed0c9-80e7-3cab-be58-2b91ea5237cc | -10.1451 | -55.1876 | 2024-10-08 00:36:04 | GOES-16 | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 91.2 |
| ea9f1f0f-09ef-3623-b916-d4817c678868 | -10.8755 | -63.8979 | 2024-10-08 00:36:08 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 60.2 |
| 4ee3dfcc-94f6-3aa7-8575-21141fe5f994 | -10.8756 | -63.8789 | 2024-10-08 00:36:08 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 50.6 |
| 82ca89a0-7450-3a78-930b-2b4734609b79 | -11.5232 | -65.1559 | 2024-10-08 00:36:12 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 53.6 |
| b862413d-1370-369c-a450-053e416e76c8 | -11.5233 | -65.137 | 2024-10-08 00:36:12 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 75.8 |
| 49fcf9ae-e609-3dff-bea2-b386e9982dee | -11.5421 | -65.1362 | 2024-10-08 00:36:12 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 49.5 |
| c7c7235b-1c47-3aaf-9f6e-da694f65473d | -11.6806 | -64.0312 | 2024-10-08 00:36:13 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 42.8 |
| 38022655-6308-3ca2-92b5-131bff21c7ae | -12.3616 | -47.0986 | 2024-10-08 00:36:16 | GOES-16 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 43.2 |
| b6fe845a-a240-33ef-bf16-1a84f152305e | -12.1913 | -63.6628 | 2024-10-08 00:36:16 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 60.0 |
| 773a7913-75da-3795-8a77-ebd6d4315210 | -12.4414 | -63.018 | 2024-10-08 00:36:17 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 64.2 |
| 86faa0fc-8292-3704-b347-45b7db0bd95e | -12.4603 | -63.0169 | 2024-10-08 00:36:17 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 61.5 |
| 721fa4a5-d8ec-39e9-8c94-bf9a1d2345fc | -12.8242 | -62.4573 | 2024-10-08 00:36:19 | GOES-16 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 61.9 |
| 925ff0a7-36e4-316d-9b9f-efb1b23bcf17 | -16.0951 | -50.1883 | 2024-10-08 00:36:36 | GOES-16 | MOSSÂMEDES | GOIÁS | Brasil | 5213905 | 52 | 33 | nan | nan | nan | Cerrado | 87.0 |
| 5b16fabd-e7c1-39ad-8159-18272bba86c2 | -16.5704 | -46.4785 | 2024-10-08 00:36:38 | GOES-16 | NATALÂNDIA | MINAS GERAIS | Brasil | 3144375 | 31 | 33 | nan | nan | nan | Cerrado | 63.0 |
| 5725fe88-a8d7-34f9-975e-447a8daa2811 | -16.5897 | -46.4979 | 2024-10-08 00:36:38 | GOES-16 | NATALÂNDIA | MINAS GERAIS | Brasil | 3144375 | 31 | 33 | nan | nan | nan | Cerrado | 151.9 |
| ffe9180a-ab99-3d5d-a0ae-31aa4c5d55e8 | -16.5902 | -46.4746 | 2024-10-08 00:36:38 | GOES-16 | NATALÂNDIA | MINAS GERAIS | Brasil | 3144375 | 31 | 33 | nan | nan | nan | Cerrado | 181.9 |
| 54b0d462-7b4a-33d7-877c-360af87c392c | -16.6095 | -46.494 | 2024-10-08 00:36:39 | GOES-16 | NATALÂNDIA | MINAS GERAIS | Brasil | 3144375 | 31 | 33 | nan | nan | nan | Cerrado | 96.2 |
| 56d0dacf-dd6d-32bc-bb69-c99aec884c19 | -16.6101 | -46.4707 | 2024-10-08 00:36:39 | GOES-16 | NATALÂNDIA | MINAS GERAIS | Brasil | 3144375 | 31 | 33 | nan | nan | nan | Cerrado | 107.3 |
| 06b8e8f7-46fc-32e0-8d56-984c48fd50b9 | -16.4353 | -57.3393 | 2024-10-08 00:36:39 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 40.2 |
| a1e70abb-d73d-324d-9929-970914acdf21 | -16.5462 | -57.7344 | 2024-10-08 00:36:39 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 37.7 |
| d26b4c84-d8cf-351e-a046-c214d948421b | -16.992 | -56.721 | 2024-10-08 00:36:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 37.2 |
| 560af163-1d66-31dc-8726-258db0ee6122 | -16.9924 | -56.7003 | 2024-10-08 00:36:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 59.9 |
| 9725b5ef-b399-3f60-b9ea-0967f4743e4b | -16.9927 | -56.6797 | 2024-10-08 00:36:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 59.8 |
| 5734ef27-e9bd-3f57-9b11-4acb6dd9cddd | -17.012 | -56.698 | 2024-10-08 00:36:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 30.9 |
| fbacf275-03ac-3bae-807b-749101cf132c | -17.0123 | -56.6773 | 2024-10-08 00:36:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 76.5 |
| 05d8b880-cfd2-38de-bda1-acebfb553b9c | -17.1584 | -56.1429 | 2024-10-08 00:36:43 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 31.3 |
| 55c8e837-0901-3032-9b95-04fdbae22d2b | -17.3353 | -55.0156 | 2024-10-08 00:36:43 | GOES-16 | ITIQUIRA | MATO GROSSO | Brasil | 5104609 | 51 | 33 | nan | nan | nan | Pantanal | 47.7 |
| 47662556-1bb3-3ea2-9841-99e97b8f6b50 | -17.1588 | -56.1222 | 2024-10-08 00:36:43 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 35.2 |
| 93f2a506-fb92-3f05-b3c3-19e3714582e5 | -19.0045 | -50.2277 | 2024-10-08 00:36:52 | GOES-16 | SANTA VITÓRIA | MINAS GERAIS | Brasil | 3159803 | 31 | 33 | nan | nan | nan | Cerrado | 129.2 |
| 5f91e11a-aab5-32b4-a801-56c4d44a9199 | -19.2723 | -46.1305 | 2024-10-08 00:36:53 | GOES-16 | SÃO GOTARDO | MINAS GERAIS | Brasil | 3162104 | 31 | 33 | nan | nan | nan | Cerrado | 93.0 |
| 8b9e58fa-0ca7-35c5-ab55-fb427bb10d5b | -19.2729 | -46.1067 | 2024-10-08 00:36:53 | GOES-16 | SÃO GOTARDO | MINAS GERAIS | Brasil | 3162104 | 31 | 33 | nan | nan | nan | Cerrado | 87.2 |
| ce8a9422-6089-3eed-9c81-b63a229b92bf | -20.3732 | -43.9468 | 2024-10-08 00:36:58 | GOES-16 | MOEDA | MINAS GERAIS | Brasil | 3142304 | 31 | 33 | nan | nan | nan | Mata Atlântica | 247.8 |
| ac8631f9-3a76-3b0e-bd3c-d922f6e00a79 | -20.374 | -43.922 | 2024-10-08 00:36:58 | GOES-16 | ITABIRITO | MINAS GERAIS | Brasil | 3131901 | 31 | 33 | nan | nan | nan | Mata Atlântica | 86.2 |
| 4de41641-4a67-349f-b8e7-7bec0e545384 | -20.3938 | -43.9412 | 2024-10-08 00:36:58 | GOES-16 | MOEDA | MINAS GERAIS | Brasil | 3142304 | 31 | 33 | nan | nan | nan | Mata Atlântica | 276.7 |
| d35918d9-5ee7-3135-b4e9-dfea648ae9f8 | -20.3946 | -43.9163 | 2024-10-08 00:36:58 | GOES-16 | OURO PRETO | MINAS GERAIS | Brasil | 3146107 | 31 | 33 | nan | nan | nan | Mata Atlântica | 136.7 |
| cd616b01-8d1f-34ba-b07d-96d4ec384686 | -20.4144 | -43.9356 | 2024-10-08 00:36:58 | GOES-16 | BELO VALE | MINAS GERAIS | Brasil | 3106408 | 31 | 33 | nan | nan | nan | Mata Atlântica | 78.9 |
| 5fa3db15-da2f-3d10-94a4-307f354e8fa2 | -20.4251 | -47.6688 | 2024-10-08 00:36:59 | GOES-16 | ITUVERAVA | SÃO PAULO | Brasil | 3524105 | 35 | 33 | nan | nan | nan | Cerrado | 108.6 |
| 741698af-915a-300a-83ca-4a05588280b1 | -20.4258 | -47.6453 | 2024-10-08 00:36:59 | GOES-16 | RIBEIRÃO CORRENTE | SÃO PAULO | Brasil | 3543105 | 35 | 33 | nan | nan | nan | Cerrado | 153.8 |
| 0f48a344-637c-3ed9-ba9d-9f2c5cd6a266 | -3.41189 | -50.33158 | 2024-10-08 00:37:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 14.9 |
| ed48ab96-43c6-38b7-aed4-dadef0598c1c | -3.21909 | -48.92413 | 2024-10-08 00:37:00 | TERRA_M-M | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 38.8 |
| 80d4e021-f7bb-3726-82a1-86c5c9f99840 | -2.99055 | -49.53945 | 2024-10-08 00:37:00 | TERRA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 8.3 |
| 289ab968-3ea2-3f85-92af-b71ff44ff100 | -2.97817 | -49.54128 | 2024-10-08 00:37:00 | TERRA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 10.1 |
| 05faaae0-5cef-3083-ba89-6cda87740100 | -2.97285 | -51.02922 | 2024-10-08 00:37:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 16.0 |
| 36c74757-949e-322d-ad00-473656b4e634 | -2.87742 | -52.91623 | 2024-10-08 00:37:00 | TERRA_M-M | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 22.7 |
| ce88544b-5565-303d-ba1a-c76fc778d02a | -2.7937 | -48.58631 | 2024-10-08 00:37:00 | TERRA_M-M | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 22.7 |
| e2e7952c-7383-3295-a5e8-642d7f307308 | -2.7916 | -48.57102 | 2024-10-08 00:37:00 | TERRA_M-M | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 29.8 |
| 43c3253a-601f-32da-ae19-1e5870a82149 | -2.75271 | -49.53402 | 2024-10-08 00:37:00 | TERRA_M-M | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 16.0 |
| 8af41b38-582e-32b1-bc46-4aeb715e3b78 | -2.4053 | -48.60177 | 2024-10-08 00:37:00 | TERRA_M-M | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 10.0 |
| b495079f-5956-3daa-8aef-bd17b9a4cdb0 | -1.17622 | -46.72492 | 2024-10-08 00:37:00 | TERRA_M-M | BRAGANÇA | PARÁ | Brasil | 1501709 | 15 | 33 | nan | nan | nan | Amazônia | 10.7 |
| 4b988e36-8361-3023-8ee0-d24b54702eb4 | -1.17773 | -46.73563 | 2024-10-08 00:37:00 | TERRA_M-M | BRAGANÇA | PARÁ | Brasil | 1501709 | 15 | 33 | nan | nan | nan | Amazônia | 10.6 |
| ac05d058-dcff-386b-897f-28c497248d59 | -1.24859 | -46.13301 | 2024-10-08 00:37:00 | TERRA_M-M | CARUTAPERA | MARANHÃO | Brasil | 2102903 | 21 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 14887050-89d2-3429-912b-0c5e4bd80679 | -1.26288 | -46.82789 | 2024-10-08 00:37:00 | TERRA_M-M | BRAGANÇA | PARÁ | Brasil | 1501709 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 7d606096-fe63-38ea-ab28-43043a258067 | -21.0712 | -47.2331 | 2024-10-08 00:37:02 | GOES-16 | SANTO ANTÔNIO DA ALEGRIA | SÃO PAULO | Brasil | 3547908 | 35 | 33 | nan | nan | nan | Cerrado | 73.3 |
| a75f6df7-d109-3a63-86bb-ddcddcff4f11 | -3.2862 | -47.133 | 2024-10-08 00:45:25 | GOES-16 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 43.1 |
| 33422fd1-7a5d-3a8a-a4a6-ede476836f3c | -4.4468 | -42.9123 | 2024-10-08 00:45:31 | GOES-16 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 59.8 |
| bc75b6bb-e485-3aea-af54-e2d39617b83f | -4.447 | -42.8889 | 2024-10-08 00:45:31 | GOES-16 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 60.6 |
| 11bd682e-7cc3-33dd-816f-b30c867a81c9 | -5.5716 | -44.8927 | 2024-10-08 00:45:38 | GOES-16 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 71.1 |
| d961cf80-871a-3f49-aefd-3c693d45bda3 | -5.5718 | -44.87 | 2024-10-08 00:45:38 | GOES-16 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 121.6 |
| 440b8bf4-389c-30d0-960c-a169f53a8908 | -5.8216 | -44.1196 | 2024-10-08 00:45:39 | GOES-16 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 70.0 |
| bc365bce-72d1-3036-bd5b-93dd0947ce60 | -6.4213 | -38.8347 | 2024-10-08 00:45:42 | GOES-16 | ICÓ | CEARÁ | Brasil | 2305407 | 23 | 33 | nan | nan | nan | Caatinga | 75.3 |
| 5f53a4a1-2961-3de9-8c9a-6e4a20de368f | -6.4402 | -38.8327 | 2024-10-08 00:45:42 | GOES-16 | ICÓ | CEARÁ | Brasil | 2305407 | 23 | 33 | nan | nan | nan | Caatinga | 73.7 |
| 60c54d63-c46e-34d9-862e-be64d378ebc7 | -9.3901 | -66.5444 | 2024-10-08 00:46:00 | GOES-16 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 54.4 |
| 6a4c08a1-7cb9-3d00-acbb-b9ff44f74a65 | -9.4087 | -66.5438 | 2024-10-08 00:46:00 | GOES-16 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 66.5 |
| c11ce4fd-b645-3b80-820d-a277c823023e | -9.445 | -66.7289 | 2024-10-08 00:46:00 | GOES-16 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 69.8 |
| 7c006ed9-53a6-3cd8-87df-f7b108451d9f | -9.4635 | -66.7283 | 2024-10-08 00:46:01 | GOES-16 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 51.7 |
| 335f1dae-e514-3470-a190-a14e29669fdc | -10.1261 | -55.2093 | 2024-10-08 00:46:04 | GOES-16 | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 73.1 |
| 3df2dab3-05fc-3e79-9009-895501eadfff | -10.1263 | -55.1891 | 2024-10-08 00:46:04 | GOES-16 | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 88.8 |
| 29f9ae4c-eab7-316c-ad12-3671b6bde99b | -10.1451 | -55.1876 | 2024-10-08 00:46:04 | GOES-16 | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 84.9 |


[Clique aqui para ver as próximas entradas](README13.md)
