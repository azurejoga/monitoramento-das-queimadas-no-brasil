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
| 040135ea-88d5-37c7-9708-dc3cc8946468 | -1.9587 | -52.99038 | 2024-11-22 04:36:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 50ee2d34-1f51-3b8c-925d-a1210e22a32e | -2.56064 | -46.55026 | 2024-11-22 04:36:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 692a9aa5-5e80-338d-b6b5-a78c4dc3f9fd | -1.14158 | -51.68838 | 2024-11-22 04:36:00 | NOAA-20 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 7b51d269-7858-33bc-9fdc-f878cb45e32a | 0.16775 | -51.23116 | 2024-11-22 04:36:00 | NOAA-20 | SANTANA | AMAPÁ | Brasil | 1600600 | 16 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 60e8aa12-964a-305a-b6d2-8c959578abf6 | -0.27815 | -51.56211 | 2024-11-22 04:36:00 | NOAA-20 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 7dc598fe-9a8d-3c20-9402-2813584342e7 | -4.4378 | -42.59418 | 2024-11-22 04:36:00 | NOAA-20 | LAGOA ALEGRE | PIAUÍ | Brasil | 2205557 | 22 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 554186c0-3683-3fcb-a3c6-16f6a7cb3437 | -2.84015 | -46.69006 | 2024-11-22 04:36:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| cb57da7e-f7f6-3d52-b6ec-e1d7512babfc | -1.21089 | -51.98892 | 2024-11-22 04:36:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 1984c446-783b-396b-959d-da142f6eed5f | -1.32659 | -47.29546 | 2024-11-22 04:36:00 | NOAA-20 | BONITO | PARÁ | Brasil | 1501600 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 2fca9556-a911-32c2-a83d-c0a7c8ef3403 | -5.50725 | -45.48679 | 2024-11-22 04:36:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 1980f3d8-8d37-3a4a-8b51-d25544538c75 | -3.47033 | -45.91091 | 2024-11-22 04:36:00 | NOAA-20 | GOVERNADOR NEWTON BELLO | MARANHÃO | Brasil | 2104651 | 21 | 33 | nan | nan | nan | Amazônia | 3.9 |
| ff4436d3-2654-337e-b42d-80cec05bd43c | -1.30294 | -52.22068 | 2024-11-22 04:36:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| e0550966-697f-3336-8004-a7ff06979783 | -3.03995 | -54.32106 | 2024-11-22 04:36:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 1fe19b8c-e265-3f41-b6d8-0839292846e4 | -2.63243 | -46.22616 | 2024-11-22 04:36:00 | NOAA-20 | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 5da1d4c7-1c2d-3c9c-b7a2-e2023f7ea588 | -3.28872 | -53.84423 | 2024-11-22 04:36:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 1d73beba-d50d-3f8f-b87d-5c9df1fb5e85 | -2.00954 | -54.5252 | 2024-11-22 04:36:00 | NOAA-20 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 236d175e-312d-35ec-86fd-c570e341080c | -1.23727 | -51.74591 | 2024-11-22 04:36:00 | NOAA-20 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| fb2b190a-a352-375e-8a51-0e68fd4f598c | -1.25995 | -51.60039 | 2024-11-22 04:36:00 | NOAA-20 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 30b613bd-bb6c-3f49-b49d-a9233af96238 | -3.17927 | -54.31556 | 2024-11-22 04:36:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 30899b6e-5cc6-38dd-b1d4-353d622ff1ea | -2.78944 | -48.10546 | 2024-11-22 04:36:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 08c3b7a9-378f-35ac-8255-ddeb12c84742 | -3.23608 | -53.63274 | 2024-11-22 04:36:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b4b7c464-2eee-398a-9828-99ea3d5df7f7 | -2.42591 | -46.51446 | 2024-11-22 04:36:00 | NOAA-20 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 3c2ab929-9dc5-3d6c-b3ed-fb4efc995c6d | -3.22812 | -54.25997 | 2024-11-22 04:36:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 22.9 |
| ce735cbc-68c6-38bf-8d73-e81d26418c8f | -3.23946 | -54.23433 | 2024-11-22 04:36:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 14.3 |
| 1ae8446f-ca18-3f61-a754-9cdad54e64d2 | -2.74701 | -51.88285 | 2024-11-22 04:36:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| a6ac7f61-bd65-3b86-b67b-2b2e1379e0ec | -3.18591 | -49.06226 | 2024-11-22 04:36:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| f0f6c8c8-1192-3ef1-80c8-ec2da5825102 | -4.59718 | -46.3458 | 2024-11-22 04:36:00 | NOAA-20 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 0.5 |
| a136a6a7-d560-3c2f-96e3-c7d9a586d0d4 | -1.21087 | -51.74617 | 2024-11-22 04:36:00 | NOAA-20 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| d3cb1ef1-a6e5-3f26-a6bd-ac11c4601aeb | -1.51963 | -47.06245 | 2024-11-22 04:36:00 | NOAA-20 | OURÉM | PARÁ | Brasil | 1505403 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| dac45314-d138-38b0-8378-cb3ce985b073 | -2.24272 | -46.8172 | 2024-11-22 04:36:00 | NOAA-20 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| f9734581-1476-3fd9-8973-a48742d1850c | -2.54114 | -53.97835 | 2024-11-22 04:36:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| cdb2b951-1c9b-3d10-aaa4-8348bc4d8808 | -2.68986 | -46.25758 | 2024-11-22 04:36:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 57ef36e5-5df5-3ac0-b790-14d239cdae29 | -2.8106 | -54.01995 | 2024-11-22 04:36:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 4157d3e1-2d5b-3df1-bc6b-de5f155c823f | -3.66343 | -51.57314 | 2024-11-22 04:36:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 9f1dcc85-7f73-3612-b0a6-ec72450f918c | -2.45817 | -49.153 | 2024-11-22 04:36:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| cecab6df-8f43-3946-9d85-6cb9ec1ac155 | -1.06225 | -48.76085 | 2024-11-22 04:36:00 | NOAA-20 | CACHOEIRA DO ARARI | PARÁ | Brasil | 1502004 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 06916d11-7e47-3cfe-862c-7a5b96bf5879 | -2.76607 | -54.05888 | 2024-11-22 04:36:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 9450c50f-6a3d-3ff8-8774-4934a9527086 | -3.83992 | -51.14445 | 2024-11-22 04:36:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| e2d75e19-d606-3c3c-a585-f249c4778a9f | -3.5792 | -51.51126 | 2024-11-22 04:36:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 1533903f-261f-3f13-928e-984c8a342567 | -4.2989 | -50.14802 | 2024-11-22 04:36:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 4471ac2e-3ab7-3f0b-96f7-590b48381004 | -2.69847 | -46.08591 | 2024-11-22 04:36:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 6098c268-c95b-3e3f-87fb-af095df4605b | -2.12284 | -50.27201 | 2024-11-22 04:36:00 | NOAA-20 | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 07a22174-0fe7-3c8c-817d-3297b8e4d4d4 | -2.7596 | -54.04629 | 2024-11-22 04:36:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 8200136a-9560-35f8-94d6-159d9e5537bb | -2.55366 | -47.29033 | 2024-11-22 04:36:00 | NOAA-20 | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ff5d4599-621d-3617-ab25-f2f2f2cc9be1 | -3.3432 | -42.78624 | 2024-11-22 04:36:00 | NOAA-20 | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 87f54948-1f63-3e5e-a7b7-e8a09faa8dc9 | -2.39328 | -49.00479 | 2024-11-22 04:36:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 1673d505-cb19-3f62-a436-0a929126b2e2 | -2.80586 | -54.02303 | 2024-11-22 04:36:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 238d44e9-f4b5-3763-9a0e-4b32e5f61d48 | -1.96263 | -52.99097 | 2024-11-22 04:36:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| c0e8f2e3-8387-3f2c-8d1c-e5372c018740 | -4.81125 | -49.72237 | 2024-11-22 04:36:00 | NOAA-20 | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| dcf9cbb7-24d2-3951-9555-14f298a16a5b | -2.45309 | -53.70064 | 2024-11-22 04:36:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| e4af6402-192b-38bb-bb9f-792a718350dc | -1.12155 | -48.79523 | 2024-11-22 04:36:00 | NOAA-20 | CACHOEIRA DO ARARI | PARÁ | Brasil | 1502004 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| b7b72abb-57a0-3f13-8b25-8d4c9d39d9b0 | -3.04988 | -51.33455 | 2024-11-22 04:36:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 7d47e66f-e9fb-3307-93b3-66be78d36221 | -4.40448 | -43.71823 | 2024-11-22 04:36:00 | NOAA-20 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| bcea2cc1-a4fb-31f0-8c34-a8c08921347d | -2.52535 | -46.39592 | 2024-11-22 04:36:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 1418548e-b97b-35d1-9e60-44bff26a5e45 | -3.32155 | -54.77407 | 2024-11-22 04:36:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| f1cca14f-667d-37cf-8feb-e44822e015b8 | -2.27763 | -46.32012 | 2024-11-22 04:36:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c034d608-e720-38a8-b7c2-d578612d90c8 | -1.07718 | -53.36549 | 2024-11-22 04:36:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 445ec424-c556-37c6-9ad7-1c1adc4b5cf8 | -1.09306 | -51.73375 | 2024-11-22 04:36:00 | NOAA-20 | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 1.6 |
| fc72b268-e599-352e-aace-ec13f5cdc8b9 | -2.56977 | -46.55925 | 2024-11-22 04:36:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 7645117f-9256-3709-994c-97d5cc3bfcb9 | -3.27304 | -53.8381 | 2024-11-22 04:36:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b75753ba-2764-3d4b-ab5b-964cc7d1cc6a | -1.43578 | -52.67023 | 2024-11-22 04:36:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| b44cda92-d1be-3de9-81b8-e04fd9d08a77 | -2.67774 | -46.24406 | 2024-11-22 04:36:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 0d968c39-66f6-3691-9c41-a99de3e5a3f3 | -3.24674 | -54.25106 | 2024-11-22 04:36:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 7.6 |
| 58e52372-4cb4-3525-a018-236275539789 | -2.69798 | -46.25102 | 2024-11-22 04:36:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| de75d864-031a-346d-9c22-b30985e219ad | -5.59054 | -45.21246 | 2024-11-22 04:36:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 9bc224d3-28b3-359c-84d3-89f171b146e5 | -2.68409 | -46.24891 | 2024-11-22 04:36:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| ffdd107f-9ffc-3864-9ffd-1b0a68eb176d | -3.73442 | -50.43472 | 2024-11-22 04:36:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| e777656c-15ec-3155-ba90-c25f4f41ae36 | -2.35291 | -50.37107 | 2024-11-22 04:36:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 67648c5d-dd08-31cf-9efa-4aa425211e20 | -3.2585 | -50.82607 | 2024-11-22 04:36:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 6b7febf8-76e3-398c-a1ac-aed4ab87d11b | -3.19843 | -54.3303 | 2024-11-22 04:36:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| e8002bda-cd15-37db-b27b-aeee133c8782 | -3.43129 | -54.60399 | 2024-11-22 04:36:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| ba2453c4-68ae-38ca-b6e0-64fcb1778f65 | -3.80739 | -51.99181 | 2024-11-22 04:36:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| a188d5c9-5cae-3d24-967d-72a9718e7324 | -1.75999 | -52.66752 | 2024-11-22 04:36:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 8041896e-388e-339e-b486-d809b88ff3d0 | -3.82677 | -52.27092 | 2024-11-22 04:36:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| c8f58340-adde-301f-9437-2587893fd663 | -3.46058 | -45.90605 | 2024-11-22 04:36:00 | NOAA-20 | GOVERNADOR NEWTON BELLO | MARANHÃO | Brasil | 2104651 | 21 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 556b0713-9e60-3b86-8f09-54fb0f5c91ca | -1.04244 | -51.74357 | 2024-11-22 04:36:00 | NOAA-20 | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 1.3 |
| dc03e4fe-0958-3657-8a74-bdc7ae7e27f6 | -0.8051 | -51.78323 | 2024-11-22 04:36:00 | NOAA-20 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 4.6 |
| b295da91-260a-31db-89c9-4272b232032d | -2.6185 | -48.17739 | 2024-11-22 04:36:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| e82f26cc-db37-3d6c-8031-88628122f4d0 | -2.05127 | -52.04301 | 2024-11-22 04:36:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| ef7f3307-9077-395d-85ed-a4f37197d826 | -2.69379 | -46.09312 | 2024-11-22 04:36:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 5b8f5aec-abeb-3bc6-8d34-da0491e79aab | -2.50202 | -49.00414 | 2024-11-22 04:36:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 7d8b18cd-1c0c-370f-ab40-1916be8b2850 | -2.6271 | -46.84245 | 2024-11-22 04:36:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 960eb587-3c80-3dcd-94a9-d7945e3092cc | -2.72199 | -49.07427 | 2024-11-22 04:36:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 6f75719d-62c5-376c-a027-18a2504ff1e9 | -3.67161 | -54.27881 | 2024-11-22 04:36:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 5df35f8d-0c01-33c3-b66f-07a71b9844f0 | -3.07093 | -53.29281 | 2024-11-22 04:36:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 24550eda-deec-315f-821d-9dd941dbfe7a | -4.20316 | -53.49767 | 2024-11-22 04:36:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 4b0a6db4-dfe9-3107-a5d8-e3bd7198463b | -3.21072 | -54.25355 | 2024-11-22 04:36:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 212b2ac0-a77c-3b60-8068-3a1eccc95c43 | -0.81006 | -51.79077 | 2024-11-22 04:36:00 | NOAA-20 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 7.2 |
| 92e03d07-be1a-3bbb-9fea-b390a884487e | -4.00416 | -43.24874 | 2024-11-22 04:36:00 | NOAA-20 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 39a5acf6-530c-35c8-b077-740da1d65525 | -3.50384 | -53.80218 | 2024-11-22 04:36:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 11.3 |
| e52f1de4-681e-3e8c-9823-8d8d089d3388 | -2.43679 | -50.28264 | 2024-11-22 04:36:00 | NOAA-20 | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| baa44c3e-c2cb-382a-a5fb-035435831e3b | -2.69864 | -46.22376 | 2024-11-22 04:36:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 96214778-787f-3dbe-8340-9a942a9c5b5f | -2.61148 | -48.22213 | 2024-11-22 04:36:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c4b04ca0-f0ea-3e29-ac24-cd7aa97d3c1a | -3.23549 | -54.24138 | 2024-11-22 04:36:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 11.3 |
| 9227c152-ddfe-3523-b30f-f809f9ddd7f8 | -1.21668 | -51.97617 | 2024-11-22 04:36:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f5a6a269-3ed8-30db-b19d-3dc1d43c6e76 | -4.07183 | -46.83702 | 2024-11-22 04:36:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 439d926f-df6a-3ba6-8c24-ca25bfb0da51 | -2.79054 | -48.57419 | 2024-11-22 04:36:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 1026c5fb-4575-3aaa-b4cf-a6ed0e0ac153 | -2.70152 | -46.22812 | 2024-11-22 04:36:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 7b051f70-20d8-3d41-a5ad-ea1ca8b87acf | -2.91496 | -53.06594 | 2024-11-22 04:36:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 00026012-7df7-3e2b-9c94-1b5b23c6df09 | -2.17825 | -52.13202 | 2024-11-22 04:36:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |


[Clique aqui para ver as próximas entradas](README47.md)
