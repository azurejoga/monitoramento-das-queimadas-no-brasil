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

## Dados Diários - Página 106

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| a0a1be11-9e75-3ad9-873b-e0da2aad75bd | -3.65527 | -50.26984 | 2025-10-17 05:08:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 6.3 |
| a22ffdd7-e128-38c6-a65a-427b8870363b | -3.21097 | -54.96732 | 2025-10-17 05:08:00 | NOAA-20 | BELTERRA | PARÁ | Brasil | 1501451 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 3367752d-1e4d-37e5-92c6-e7e4913ca16a | -2.74363 | -49.38494 | 2025-10-17 05:08:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 86ad32df-7066-31d0-be49-b8986f36fc83 | 1.78412 | -55.73093 | 2025-10-17 05:08:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| a228b83a-1239-3481-acf9-bff77c8a5c41 | -5.28336 | -47.92857 | 2025-10-17 05:08:00 | NOAA-20 | SAMPAIO | TOCANTINS | Brasil | 1718808 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 5a87153a-0348-3b15-9340-a763273792ed | -4.39713 | -43.41798 | 2025-10-17 05:08:00 | NOAA-20 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 4.3 |
| beaaaeb6-34c9-30e0-b998-ff095f787e46 | -6.74299 | -44.37344 | 2025-10-17 05:08:00 | NOAA-20 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 06226969-c0bc-398c-983b-218a33e27cd2 | -7.35291 | -43.85575 | 2025-10-17 05:08:00 | NOAA-20 | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 759affc1-20df-36b7-afe2-d12ced0da433 | -7.11587 | -44.74587 | 2025-10-17 05:08:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 4cbadd59-41ab-3fb5-949f-a6c588ee1896 | 2.08175 | -55.80821 | 2025-10-17 05:08:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| cef2480a-2c7a-3aef-8eee-8323a6811db2 | -1.48949 | -55.44216 | 2025-10-17 05:08:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| e450ae3f-e82e-3a12-bcd5-a4f993dd4eff | -4.40797 | -43.39253 | 2025-10-17 05:08:00 | NOAA-20 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 10.3 |
| 0e826c36-e96a-339d-80a3-90c8fba870a4 | -6.29155 | -44.01839 | 2025-10-17 05:08:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 9993b0cd-03de-36f3-959f-dc32dfec309f | -7.08923 | -44.26404 | 2025-10-17 05:08:00 | NOAA-20 | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| b049f9d2-6924-3cfb-afc5-bea3c34b81e0 | -4.41379 | -43.39386 | 2025-10-17 05:08:00 | NOAA-20 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 15.1 |
| 3f7cc651-4686-3508-b756-9f5f40718795 | -5.69607 | -53.63953 | 2025-10-17 05:08:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 715c1a9d-770b-3f09-acb2-bc0b16ebfca6 | -5.23626 | -49.23127 | 2025-10-17 05:08:00 | NOAA-20 | NOVA IPIXUNA | PARÁ | Brasil | 1504976 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 3723b1c7-6ba3-31a1-9c9f-5456864f102e | 1.78136 | -55.73489 | 2025-10-17 05:08:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 0cce6c0a-43f3-363f-8600-327c85e3d615 | -3.50134 | -52.48871 | 2025-10-17 05:08:00 | NOAA-20 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 65e2fd6c-24bb-3027-9c81-580d9a8dd17a | 2.08506 | -55.80769 | 2025-10-17 05:08:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 1b0cabc9-1e2c-3845-a055-1984b90a3f0b | -5.24785 | -50.96303 | 2025-10-17 05:08:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 847a127c-cf4d-3f38-b943-bc5ada0ad2d1 | -4.49527 | -49.64326 | 2025-10-17 05:08:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 69ab60a8-925c-30fb-a02f-1df7904266c0 | -3.40432 | -46.902 | 2025-10-17 05:08:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 89335085-d706-33c4-9e05-6cfa1651d5d9 | -2.86978 | -50.74176 | 2025-10-17 05:08:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| e030eb7d-ac71-356a-929c-ea026b7e1a2a | 1.84786 | -55.68222 | 2025-10-17 05:08:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| bcc52179-1a3a-3371-9c12-0ffe3f6fbf5a | 1.73551 | -55.78785 | 2025-10-17 05:08:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 9.0 |
| e8e39bf5-61f2-315f-a3e2-1707adb60dc5 | 1.73166 | -55.78493 | 2025-10-17 05:08:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 9.0 |
| 8c6cc0e3-980d-3bd5-8ceb-498316102e53 | -2.30882 | -57.16005 | 2025-10-17 05:08:00 | NOAA-20 | NHAMUNDÁ | AMAZONAS | Brasil | 1303007 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 000cf14f-2ffe-3413-a44a-8c7e946a55a3 | 1.79645 | -55.87365 | 2025-10-17 05:08:00 | NOAA-20 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 42d834a0-1c36-3d94-a388-2dc417bcb0e1 | -4.405 | -43.4059 | 2025-10-17 05:08:00 | NOAA-20 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 8.0 |
| 0eb91534-501f-3133-a94e-f299ba7b6e30 | -1.70611 | -55.68483 | 2025-10-17 05:08:00 | NOAA-20 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 4374d391-3e8b-3ab2-8ae7-e05217ad9ef3 | -2.87412 | -50.74556 | 2025-10-17 05:08:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 37cf3e2e-37c8-3f93-a77b-de4b83cb55f9 | -2.94444 | -47.31452 | 2025-10-17 05:08:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 31badf23-bc09-3fee-a90f-68f9aa2c88b5 | -3.53275 | -54.17532 | 2025-10-17 05:08:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c56c1700-8f88-33b0-b304-2baea8d45d80 | -2.43315 | -57.69011 | 2025-10-17 05:08:00 | NOAA-20 | URUCARÁ | AMAZONAS | Brasil | 1304302 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 207c0023-5047-3b8f-b1fe-6a9d54679778 | -1.7369 | -54.43551 | 2025-10-17 05:08:00 | NOAA-20 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| ec2e8c3b-f9a6-3859-8a96-0f657e69f269 | 1.77806 | -55.7354 | 2025-10-17 05:08:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 5828cea0-9f7a-3eba-a961-0d0b9dea240e | -5.91039 | -44.7558 | 2025-10-17 05:08:00 | NOAA-20 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| b1e02635-3558-3a5b-9b9d-4dbcf03f9b9e | 1.85339 | -55.67432 | 2025-10-17 05:08:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 3b4994f0-91f6-3c36-9215-213b614edf26 | -6.20978 | -47.88325 | 2025-10-17 05:08:00 | NOAA-20 | LUZINÓPOLIS | TOCANTINS | Brasil | 1712454 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 3ab1c809-f947-3e63-a747-b97147e1126d | -4.40701 | -43.39906 | 2025-10-17 05:08:00 | NOAA-20 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 7.3 |
| 089fab86-371a-329f-8c90-02d9fbdf85cd | -4.04283 | -47.50447 | 2025-10-17 05:08:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 930ce4ad-b7fb-3315-8b81-67e04d2868f7 | -5.50965 | -43.86764 | 2025-10-17 05:08:00 | NOAA-20 | GOVERNADOR EUGÊNIO BARROS | MARANHÃO | Brasil | 2104602 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 7f67222b-3fde-3136-96ce-50a625794d03 | 1.89587 | -55.85817 | 2025-10-17 05:08:00 | NOAA-20 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 44119410-e95e-39fd-af8a-f9bd13c3696c | -6.22395 | -47.04352 | 2025-10-17 05:08:00 | NOAA-20 | PORTO FRANCO | MARANHÃO | Brasil | 2109007 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| ac58e013-6f08-3bc9-beca-99afc09cb474 | -1.48563 | -55.4451 | 2025-10-17 05:08:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| a0636115-c02c-3861-9379-f72b0e25378e | 1.90408 | -55.65232 | 2025-10-17 05:08:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| b3d7eaae-4ccd-3ee6-956b-f5f71883d3bd | -4.10555 | -48.02523 | 2025-10-17 05:08:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 4ba38e64-bea9-36f8-8515-b70af56abf9f | -2.86992 | -50.74492 | 2025-10-17 05:08:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 30c0e2bf-dcaa-33df-8ffa-8e778137f905 | -3.78173 | -49.43375 | 2025-10-17 05:08:00 | NOAA-20 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 836a96de-c5c8-33ae-8fc8-50ddf8b240fe | -2.67085 | -55.75106 | 2025-10-17 05:08:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| ba2597fc-1084-3172-8623-e9776db49722 | -1.49608 | -47.81443 | 2025-10-17 05:08:00 | NOAA-20 | SÃO MIGUEL DO GUAMÁ | PARÁ | Brasil | 1507607 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| b4fd67cb-30c8-3131-85c6-09cedd712d61 | -5.86251 | -47.58427 | 2025-10-17 05:08:00 | NOAA-20 | ITAGUATINS | TOCANTINS | Brasil | 1710706 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 65ce49b7-33e2-382b-8e7d-3639bdb826ec | -2.88063 | -50.73074 | 2025-10-17 05:08:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| c07111c5-7cfa-352f-af66-72ca19b72126 | -4.71788 | -49.62677 | 2025-10-17 05:08:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ba7b8c28-e3f8-30ef-9d30-a1aec70e137e | -5.29197 | -43.55918 | 2025-10-17 05:08:00 | NOAA-20 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 7.4 |
| fa3e7e5f-4b2c-3780-b33f-7fe66cb4f5bb | -6.29724 | -45.53142 | 2025-10-17 05:08:00 | NOAA-20 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| c9b94019-67f5-39a9-8c2e-a97d6ea45d9b | 1.77307 | -55.74675 | 2025-10-17 05:08:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a2832cca-cef3-3f15-91d0-015c2820c791 | -5.85354 | -43.87202 | 2025-10-17 05:08:00 | NOAA-20 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 3dd8acf9-3d6f-307a-a153-a986f6e56e33 | -5.58093 | -47.46391 | 2025-10-17 05:08:00 | NOAA-20 | IMPERATRIZ | MARANHÃO | Brasil | 2105302 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| d08521e2-c0f2-31d9-b589-13ecf14b3b39 | 1.8219 | -55.71091 | 2025-10-17 05:08:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| c23e1ca3-4b6e-374e-9209-d394c3762f7b | 1.77253 | -55.74331 | 2025-10-17 05:08:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 81819211-bbe2-3bc1-9fe1-eb1d9054233b | -6.2201 | -44.43266 | 2025-10-17 05:08:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 324e6cef-8154-3b8b-b2f6-4a7d25e6ade8 | -2.86687 | -50.73658 | 2025-10-17 05:08:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 7a7f4c62-75d8-3fbb-adf5-51078a7840d2 | -4.01749 | -48.96933 | 2025-10-17 05:08:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| cbc63c34-567e-3d10-b5cd-620428446b81 | -6.29071 | -44.02485 | 2025-10-17 05:08:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 440d4238-3674-34b2-9419-cb7d4d9bd202 | 1.80395 | -55.96442 | 2025-10-17 05:08:00 | NOAA-20 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 1fce96c2-631e-3769-ae68-8e6a1daeaaf6 | -1.7028 | -55.68432 | 2025-10-17 05:08:00 | NOAA-20 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 50cb1f53-3917-31d2-8e45-d195662af107 | 1.78641 | -55.91764 | 2025-10-17 05:08:00 | NOAA-20 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| bf1716de-3e27-33ca-b91c-202a6d0578ea | -1.49149 | -47.81075 | 2025-10-17 05:08:00 | NOAA-20 | SÃO MIGUEL DO GUAMÁ | PARÁ | Brasil | 1507607 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 03743568-a275-3785-8b4e-ecb9aaeef6db | -3.5028 | -52.4938 | 2025-10-17 05:10:00 | GOES-19 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 44.9 |
| 90af232d-de01-3246-8a68-e19a32403ae0 | -3.5028 | -52.4734 | 2025-10-17 05:10:00 | GOES-19 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 42.5 |
| 844fcec9-ba2c-32a7-8f53-578ed192ecfd | -9.14316 | -46.63913 | 2025-10-17 05:10:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 9.1 |
| 4dbd124c-fd84-3b78-b3c3-ec9b848d3494 | -9.14936 | -46.73676 | 2025-10-17 05:10:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| d42cfd59-a854-33af-8e27-47c3ddbcd2ec | -8.31472 | -47.8646 | 2025-10-17 05:10:00 | NOAA-20 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| c4551891-0b48-380c-839e-5edc236f7ac3 | -11.36287 | -54.32459 | 2025-10-17 05:10:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 960de6e5-632e-3b4e-8114-4abdce52ce61 | -10.64681 | -45.30495 | 2025-10-17 05:10:00 | NOAA-20 | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 754b2677-ede6-3fb1-b03f-a53b8662072a | -7.20815 | -45.49461 | 2025-10-17 05:10:00 | NOAA-20 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 5e366e41-3d13-38e4-b8d3-e971b1ac1e69 | -11.82008 | -57.94234 | 2025-10-17 05:10:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 84c66e66-08d3-3b55-97bc-956044b43fab | -8.4564 | -46.25237 | 2025-10-17 05:10:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 388e1039-a443-331e-9ccf-ff04530a4c4f | -13.44365 | -47.96885 | 2025-10-17 05:10:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 4f5da60e-225e-3a78-ab3a-d2403a39b2a5 | -8.36822 | -46.25508 | 2025-10-17 05:10:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| c73e7225-aca6-35c4-aad7-59d168681f14 | -7.90235 | -44.98969 | 2025-10-17 05:10:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 97a37b24-ebf3-3989-8380-94bccafed130 | -13.39111 | -47.21719 | 2025-10-17 05:10:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 913d1886-4093-3624-8dc9-b4c8e6ce7571 | -11.18502 | -57.26863 | 2025-10-17 05:10:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| c20ef45d-513b-37ca-8241-0083970eaf30 | -13.93735 | -48.69528 | 2025-10-17 05:10:00 | NOAA-20 | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 9f349446-b232-3fcf-9bb9-c2bdcf42e8e4 | -8.37369 | -46.30962 | 2025-10-17 05:10:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| df2cb85b-79e5-33b7-876b-2f6cb63d7c3f | -10.53012 | -49.55669 | 2025-10-17 05:10:00 | NOAA-20 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 12.6 |
| 383ceea3-e2f4-3fc6-97fd-cc851cc95f58 | -8.16236 | -46.06941 | 2025-10-17 05:10:00 | NOAA-20 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 8a782a01-6515-315e-b6b5-70ac0579fb3e | -9.25341 | -44.35452 | 2025-10-17 05:10:00 | NOAA-20 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 73b09745-de4a-3763-8ad5-af700368d3d9 | -10.13719 | -44.58525 | 2025-10-17 05:10:00 | NOAA-20 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 117bcb0b-395d-3552-9588-2370b0aecd57 | -13.43365 | -47.96452 | 2025-10-17 05:10:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 04fe0635-9699-3c57-9783-db401194bae9 | -7.95603 | -44.12344 | 2025-10-17 05:10:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 3.9 |
| af893933-4ccb-3172-87da-f9901f91210d | -13.417 | -47.93962 | 2025-10-17 05:10:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| f92854b0-f2b9-34b5-a72b-9867d49b0602 | -10.15608 | -44.53523 | 2025-10-17 05:10:00 | NOAA-20 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 97fc248e-e65d-32fa-b181-f740ee815287 | -12.44476 | -54.50784 | 2025-10-17 05:10:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 0782137f-6dc0-3566-a4bb-721e9447255a | -12.04561 | -51.37566 | 2025-10-17 05:10:00 | NOAA-20 | SERRA NOVA DOURADA | MATO GROSSO | Brasil | 5107883 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| bca24a6c-c952-3452-b66a-8861c3994c0a | -9.71222 | -44.55593 | 2025-10-17 05:10:00 | NOAA-20 | REDENÇÃO DO GURGUÉIA | PIAUÍ | Brasil | 2208700 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| e305b611-727c-3a37-93ad-37666c3616c0 | -11.0731 | -57.87725 | 2025-10-17 05:10:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 24c7fc28-a014-3cfb-a2f4-b8d398afd504 | -8.73177 | -43.88001 | 2025-10-17 05:10:00 | NOAA-20 | CRISTINO CASTRO | PIAUÍ | Brasil | 2203107 | 22 | 33 | nan | nan | nan | Cerrado | 4.0 |


[Clique aqui para ver as próximas entradas](README107.md)
