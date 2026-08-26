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

## Dados Diários - Página 89

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| c3390087-4ca3-38d3-8e6d-7d779127eba2 | -15.5948 | -56.392 | 2026-08-26 15:20:00 | GOES-19 | NOSSA SENHORA DO LIVRAMENTO | MATO GROSSO | Brasil | 5106109 | 51 | 33 | nan | nan | nan | Cerrado | 93.8 |
| c814fad3-757a-32d8-ac2f-45d4983572ad | -8.7772 | -49.955 | 2026-08-26 15:20:00 | GOES-19 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 121.7 |
| cfc3b7d4-9d8a-33cf-8a6d-6c43f32109ab | -6.7648 | -59.4408 | 2026-08-26 15:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 128.0 |
| bfdc3826-60f5-31cd-9a84-3fd96a4538bf | -14.2985 | -51.7286 | 2026-08-26 15:20:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 80.0 |
| 38cdc2bf-7084-3871-8ad3-68299d7c0c03 | -7.5256 | -44.4795 | 2026-08-26 15:20:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 104.7 |
| ef7529ca-6b31-31f2-9ffc-41c1fa6d22b1 | -9.9708 | -53.9419 | 2026-08-26 15:20:00 | GOES-19 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 76.8 |
| 95f65c3d-b04e-3374-94fe-a0a003ea6130 | -10.95 | -49.5877 | 2026-08-26 15:20:00 | GOES-19 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 107.3 |
| 16d280b2-a5f9-3e56-a342-8defe1439c99 | -6.1107 | -57.723 | 2026-08-26 15:20:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 55.3 |
| 31908915-3807-3d8f-bb69-f4361dcc8b84 | -14.3175 | -51.7474 | 2026-08-26 15:20:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 96.9 |
| 1cedcddb-6a6f-381b-90b5-8ed75578b9d3 | -6.7833 | -59.4208 | 2026-08-26 15:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 92.4 |
| a068eaeb-0094-383e-a848-f056d2d5b2d2 | -3.1083 | -61.238 | 2026-08-26 15:20:00 | GOES-19 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 82.9 |
| cc2a1cc2-de3e-3a63-9b96-1138a2a37cf2 | -6.0353 | -58.0376 | 2026-08-26 15:20:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 67.1 |
| 68c9b878-efd2-383e-9e47-d9068ed7b1d1 | -9.4519 | -51.67 | 2026-08-26 15:20:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 101.4 |
| 5f28eaf2-6b98-3085-83bc-2150727e7b7a | -11.7357 | -54.5227 | 2026-08-26 15:20:00 | GOES-19 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 121.3 |
| 9bf47919-7cb2-318f-a948-4137a424f92c | -6.4232 | -54.9632 | 2026-08-26 15:20:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 73.3 |
| 97a29ccb-7554-3211-9a4e-dedf39f02772 | -6.7999 | -59.7473 | 2026-08-26 15:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 60.0 |
| 310be7a2-71ab-3c59-afed-325501538d5f | -8.1113 | -47.4592 | 2026-08-26 15:20:00 | GOES-19 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 86.7 |
| d68469af-cc6d-348b-8808-a03c857652b8 | -9.7249 | -49.3296 | 2026-08-26 15:20:00 | GOES-19 | DIVINÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1707108 | 17 | 33 | nan | nan | nan | Cerrado | 104.9 |
| cb787c92-afea-32d0-814d-2ac81a1a0f2e | -8.616 | -54.7339 | 2026-08-26 15:20:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 72.3 |
| 821e02ea-5894-38c8-8465-7a1c784eef46 | -12.6836 | -48.4116 | 2026-08-26 15:20:00 | GOES-19 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 89.8 |
| 033a10b4-e2a5-3188-86c7-95adc95f48c6 | -6.6766 | -58.7299 | 2026-08-26 15:20:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 53.3 |
| 81d903c9-6e33-3a0b-be90-880f8848dfb5 | -10.9664 | -51.1251 | 2026-08-26 15:20:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 126.2 |
| 6b8d38d1-a19a-31b7-9066-125d08cfff6d | -9.1317 | -57.5506 | 2026-08-26 15:20:00 | GOES-19 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 43.6 |
| e80ec34d-c5ae-3c6e-8d65-870ccd201739 | -7.0234 | -45.7528 | 2026-08-26 15:20:00 | GOES-19 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 105.6 |
| 7b9feb21-c643-38a3-af03-8eb018e6749d | -8.7582 | -49.978 | 2026-08-26 15:20:00 | GOES-19 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 303.2 |
| 8b097256-f010-36cb-b5b5-c2949d55f309 | -11.1165 | -49.8707 | 2026-08-26 15:20:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 78.7 |
| fffd8174-897f-37d5-a628-460ecfcb3b88 | -14.3179 | -51.726 | 2026-08-26 15:20:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 125.6 |
| 30914120-2131-3828-b0c9-706da1b27911 | -11.3705 | -50.6779 | 2026-08-26 15:20:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 99.4 |
| b83109d7-1ee8-387c-8658-323568d463c2 | -13.2849 | -51.4114 | 2026-08-26 15:20:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 128.4 |
| 94eb11ac-f04c-3b5a-aea8-8165337d1a46 | -8.1301 | -47.4575 | 2026-08-26 15:20:00 | GOES-19 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 88.7 |
| 023ce484-7c24-378a-b929-d598ec2ca0db | -12.6452 | -48.4168 | 2026-08-26 15:20:00 | GOES-19 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 99.3 |
| 30252351-6f59-3d84-8f44-eed72281c686 | -8.5962 | -54.8563 | 2026-08-26 15:20:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 91.2 |
| 1dff7d93-128f-32a1-8845-c9456e409108 | -14.2402 | -51.7576 | 2026-08-26 15:20:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 138.6 |
| d9b6ad94-f557-39da-bf7f-160a8d196713 | -9.1711 | -49.9835 | 2026-08-26 15:20:00 | GOES-19 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 174.6 |
| 4fe8d630-f7ab-3114-8719-19493165052e | -10.779 | -50.9962 | 2026-08-26 15:20:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 107.7 |
| ebba44ed-b7b0-34f2-8a6c-be12c2819be1 | -15.7878 | -56.452 | 2026-08-26 15:20:00 | GOES-19 | NOSSA SENHORA DO LIVRAMENTO | MATO GROSSO | Brasil | 5106109 | 51 | 33 | nan | nan | nan | Cerrado | 62.8 |
| e4bcf607-faf2-3c9f-bdeb-31f585c7fc08 | -3.2179 | -61.2174 | 2026-08-26 15:20:00 | GOES-19 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 69.0 |
| d2da0635-e888-3c05-a5f4-6752e561cb9b | -11.115 | -49.9784 | 2026-08-26 15:20:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 109.9 |
| 9b51b71f-81ef-3f6e-8b62-82339d9354af | -9.6022 | -55.128 | 2026-08-26 15:20:00 | GOES-19 | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 88.9 |
| 2e56a443-6aa4-38cb-8f74-9c5012e1f193 | -10.7793 | -50.975 | 2026-08-26 15:20:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 97.0 |
| 6dc63304-c517-3a60-bc4e-e6ed1a381fde | -6.3323 | -54.7272 | 2026-08-26 15:20:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 83.9 |
| 1885df8b-50c1-3db7-8058-1debaff42741 | -6.7647 | -59.4601 | 2026-08-26 15:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 58.4 |
| fef03214-aeb8-3070-a30c-590f68349b45 | -7.6649 | -47.1242 | 2026-08-26 15:20:00 | GOES-19 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 177.7 |
| ae2b96fd-f378-377e-9a8c-de42e13b7356 | -6.8247 | -58.6461 | 2026-08-26 15:20:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 142.4 |
| 0d18769e-6338-3bf9-beac-50a7222d0fd6 | -11.7736 | -54.5191 | 2026-08-26 15:20:00 | GOES-19 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 388.4 |
| 6e9b630c-bb35-3974-9e71-5da9ab63e960 | -6.8019 | -59.4008 | 2026-08-26 15:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 57.6 |
| 7d695c6d-2d89-35e8-961a-307adf04de47 | -6.7692 | -58.6679 | 2026-08-26 15:20:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 70.3 |
| bbb47406-f2c1-302a-aa04-b8fcef52b66e | -8.9418 | -45.748 | 2026-08-26 15:20:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 85.5 |
| 65dd0392-1c8e-3f4c-b52b-5686983d3fa1 | -7.1121 | -42.7963 | 2026-08-26 15:20:00 | GOES-19 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 967.5 |
| a0ca5c29-509a-3d78-a1a2-83c42d76b25e | -11.7733 | -54.5396 | 2026-08-26 15:20:00 | GOES-19 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 240.8 |
| 934c16c5-b9a6-30c8-98e4-81f3fd15108b | -11.3702 | -50.6993 | 2026-08-26 15:20:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 266.1 |
| 0f1f5982-cee3-3cc9-b091-f4548f567ebd | -3.1083 | -61.2191 | 2026-08-26 15:20:00 | GOES-19 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 96.9 |
| c01e487e-3ea6-3fb9-838a-72f56aa925cc | -6.7296 | -59.1337 | 2026-08-26 15:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 80.4 |
| 82cd62dd-9406-35c6-a966-b4ce1707830f | -9.6776 | -55.082 | 2026-08-26 15:20:00 | GOES-19 | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 188.4 |
| a4ab1b15-a912-3740-8bd9-1d643d66b559 | -9.659 | -55.0632 | 2026-08-26 15:20:00 | GOES-19 | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 73.1 |
| d4ee30cf-f6b3-31ed-84c7-a928711b472b | -8.1482 | -47.5218 | 2026-08-26 15:20:00 | GOES-19 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 136.1 |
| ada656fb-7b4e-3404-b4bd-102419777cfa | -6.695 | -58.7291 | 2026-08-26 15:20:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 65.0 |
| 52ea8fc3-87e9-3c46-bdc8-0c963f45288e | -12.757 | -46.4538 | 2026-08-26 15:20:00 | GOES-19 | AURORA DO TOCANTINS | TOCANTINS | Brasil | 1702703 | 17 | 33 | nan | nan | nan | Cerrado | 93.3 |
| 2c32b155-1bb7-3c98-9b74-4a884c5973fb | -14.3368 | -51.7448 | 2026-08-26 15:20:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 139.4 |
| abbdfc4e-fc50-3a7b-9d65-6bc5d508d6f4 | -7.385 | -55.1523 | 2026-08-26 15:20:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 158.7 |
| 4e27e8d1-fb17-3ed1-985e-fbb5f2e353fd | -7.6461 | -47.1258 | 2026-08-26 15:20:00 | GOES-19 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 597.3 |
| e80bd51e-7772-303d-a401-3b2369a44bf8 | -4.8002 | -43.1709 | 2026-08-26 15:20:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 140.1 |
| 6a94fb23-6e1a-3e01-a1bb-4e4b0df68687 | -7.5015 | -44.9397 | 2026-08-26 15:20:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 168.2 |
| 4515c354-8f1a-327f-92d3-4b52d269d333 | -8.5975 | -54.715 | 2026-08-26 15:20:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 90.0 |
| 426174d4-e49d-3f21-ada2-9d4a40c9227e | -9.106 | -60.9127 | 2026-08-26 15:20:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 57.8 |
| 56c03b71-c747-3984-b896-2631cba700cf | -9.1315 | -57.5703 | 2026-08-26 15:20:00 | GOES-19 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 57.3 |
| cfc5cd42-9dae-36f4-862d-bbbd26dc2cb3 | -8.1484 | -47.4998 | 2026-08-26 15:20:00 | GOES-19 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 106.0 |
| 2d298666-4856-3293-8c8e-1850bade9b58 | -9.7246 | -49.3512 | 2026-08-26 15:20:00 | GOES-19 | DIVINÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1707108 | 17 | 33 | nan | nan | nan | Cerrado | 98.4 |
| c891475a-ea25-3333-814a-58c590e71324 | -6.5138 | -55.2387 | 2026-08-26 15:20:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 57.8 |
| 96562dd2-b1c6-3c3b-9634-daa6b4cb0469 | -7.0242 | -59.2374 | 2026-08-26 15:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 90.2 |
| d02628fc-2b4c-3925-8ef2-188fb354e653 | -3.2178 | -61.2362 | 2026-08-26 15:20:00 | GOES-19 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 127.0 |
| aab48ea4-635f-32f8-a89c-21d0d4c8a2b8 | -6.8246 | -58.6655 | 2026-08-26 15:20:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 137.3 |
| 85849f19-eec8-37a6-bce1-bea802c7dd14 | -6.5829 | -58.9851 | 2026-08-26 15:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 68.1 |
| fc21c921-9739-3117-9f8e-3f8b52ea5871 | -6.6227 | -58.4801 | 2026-08-26 15:20:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 53.2 |
| ca2df9d4-18ef-3fca-b2ee-dde45271b0e3 | -6.4045 | -54.9842 | 2026-08-26 15:20:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 46.3 |
| f3f8b3bb-2a04-374c-ad18-d711d51d2673 | -9.6588 | -55.0834 | 2026-08-26 15:20:00 | GOES-19 | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 116.5 |
| cacc3153-1236-3c7d-ab55-114a45f09d0e | -10.5596 | -50.4449 | 2026-08-26 15:20:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 116.3 |
| c2df3dfc-737f-3741-86f3-695838d20aae | -11.7544 | -54.5414 | 2026-08-26 15:20:00 | GOES-19 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 222.1 |
| 7423908a-88fd-3bcf-9cb0-f685bda70ba5 | -8.6415 | -50.3495 | 2026-08-26 15:20:00 | GOES-19 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 94.4 |
| 59451f5e-a817-320e-99b3-afeacaf728d5 | -9.1713 | -49.9622 | 2026-08-26 15:20:00 | GOES-19 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 80.4 |
| af0203c3-7922-3827-9c32-57c7df7be98c | -6.7815 | -59.748 | 2026-08-26 15:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 51.6 |
| b179b0ba-5753-3af0-9277-e1cb56f1249d | -7.0058 | -59.2382 | 2026-08-26 15:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 64.7 |
| 6912af0a-88c7-3078-b060-40cfbb946769 | -6.8008 | -59.5934 | 2026-08-26 15:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 54.4 |
| 1b2d5263-de29-393d-8ce8-b0504a79be98 | -3.7717 | -59.2844 | 2026-08-26 15:20:00 | GOES-19 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 65.7 |
| 68c6a427-50d8-3c3e-b03a-d1073549e2ea | -6.7834 | -59.4016 | 2026-08-26 15:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 46.4 |
| e5842ab2-aec5-3d74-b2aa-bac7b9118a47 | -8.8189 | -49.5879 | 2026-08-26 15:20:00 | GOES-19 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 53.7 |
| b062e6c1-ffe6-320d-a350-d42a16cc520f | -13.7555 | -51.9691 | 2026-08-26 15:20:00 | GOES-19 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 76.3 |
| bd26a900-28cc-3695-a581-e685bfc3ef1a | -11.175 | -54.001 | 2026-08-26 15:20:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 89.1 |
| 0f2af1d8-08c8-3c73-aec8-40b2c84f9763 | -6.8062 | -58.6469 | 2026-08-26 15:20:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 70.5 |
| da144c67-0fc8-3429-881e-d220693e1ef5 | -11.1561 | -54.0028 | 2026-08-26 15:20:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 73.3 |
| 1c69d931-ea4b-3398-b1ce-3a55365a5b68 | -8.2224 | -55.0015 | 2026-08-26 15:20:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 67.3 |
| 6f8d864c-2886-3a19-bc1b-6c851a0f3da0 | -11.7354 | -54.5431 | 2026-08-26 15:20:00 | GOES-19 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 78.5 |
| babe1c4a-44f2-3e1d-81d9-4585512465ac | -9.1899 | -49.9818 | 2026-08-26 15:20:00 | GOES-19 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 113.4 |
| e7368cca-629a-3ce3-a663-2600ec3ec9e6 | -5.4142 | -45.8734 | 2026-08-26 15:20:00 | GOES-19 | ITAIPAVA DO GRAJAÚ | MARANHÃO | Brasil | 2105351 | 21 | 33 | nan | nan | nan | Cerrado | 58.4 |
| a6c93c43-ae8c-39f9-b435-bbe75bb665ea | -8.5177 | -55.3039 | 2026-08-26 15:20:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 166.7 |
| a0116fd2-1c9c-3dbb-8a39-e639d129cab9 | -6.4047 | -54.9642 | 2026-08-26 15:20:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 95.5 |
| 26f75984-e13f-3bc8-9746-556819082193 | -11.7546 | -54.5209 | 2026-08-26 15:20:00 | GOES-19 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 361.1 |
| b6ab4c84-757f-3875-856f-7b8644d3fa87 | -6.7691 | -58.6873 | 2026-08-26 15:20:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 61.0 |
| 2efcb329-a69c-35cf-ab87-fd7039d73b71 | -8.8187 | -49.6093 | 2026-08-26 15:20:00 | GOES-19 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 301.0 |
| 60250ced-3bd1-3fa4-8f91-2ea5f7919cf4 | -8.5173 | -55.3441 | 2026-08-26 15:20:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 64.2 |


[Clique aqui para ver as próximas entradas](README90.md)
