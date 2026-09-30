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

## Dados Diários - Página 40

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 1a3f710c-d15f-3c51-a998-23f97d7685ad | -3.24115 | -46.94219 | 2026-09-30 04:51:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b0199cb3-4e1c-3613-8f0c-d44c37213b59 | 3.28221 | -60.61822 | 2026-09-30 04:51:00 | NOAA-20 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 6.4 |
| 534ff431-53a9-3459-871a-89f6608c7a39 | 1.80649 | -55.64284 | 2026-09-30 04:51:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 38049b97-f669-3479-85ad-c7a5049c0e01 | -2.98253 | -51.0382 | 2026-09-30 04:51:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 53d142ad-a271-39b4-93ba-2bbde4a965fb | -2.97756 | -51.04806 | 2026-09-30 04:51:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 14.0 |
| c5f1f64e-4b6c-34f8-9431-b01b5b1a55f5 | -2.97587 | -51.01588 | 2026-09-30 04:51:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| b380d868-796f-3947-9908-ebdfb2d0d079 | -0.41565 | -52.01376 | 2026-09-30 04:51:00 | NOAA-20 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 0e30e084-d59c-3640-a729-98af3ab905df | -3.02663 | -51.3373 | 2026-09-30 04:51:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| b2bb687b-8dfb-3ff2-8422-bc2f9692d555 | -1.47455 | -48.91122 | 2026-09-30 04:51:00 | NOAA-20 | PONTA DE PEDRAS | PARÁ | Brasil | 1505700 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| b6a2414e-c4cd-300c-a076-de0498265f05 | -2.44793 | -49.21756 | 2026-09-30 04:51:00 | NOAA-20 | MOCAJUBA | PARÁ | Brasil | 1504604 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 0ea68b23-e46c-3a70-adf4-72a6b7cb8c0c | -2.92972 | -48.75425 | 2026-09-30 04:51:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 325a14a1-a912-39a1-8826-c7923a3d62a8 | -2.98363 | -51.03127 | 2026-09-30 04:51:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| ce5c72d7-fce5-3a6d-bc8c-3282f4be0956 | 1.81392 | -55.63292 | 2026-09-30 04:51:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 54f5ac2a-ad74-3cb4-9ec4-a4c441393d3e | -3.24738 | -50.11641 | 2026-09-30 04:51:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| a30b273d-4222-3d6f-94b9-00dfca49e3ec | 1.85895 | -55.6328 | 2026-09-30 04:51:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| ba40e2b3-b7fb-3af8-bff9-c536ea8c8963 | 2.5476 | -61.30962 | 2026-09-30 04:51:00 | NOAA-20 | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 66aba40c-7668-38ae-ac4c-193209686332 | -2.96871 | -51.03957 | 2026-09-30 04:51:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 3e02fbe7-96bf-3018-b09f-2b9705780290 | -3.22927 | -50.16655 | 2026-09-30 04:51:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| c7763b7e-1bf5-3f90-8481-c3588e05664a | -1.78835 | -47.94374 | 2026-09-30 04:51:00 | NOAA-20 | CONCÓRDIA DO PARÁ | PARÁ | Brasil | 1502756 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 0b119fd2-34c1-3cca-8d4a-e4c1b3139f34 | -2.5768 | -50.79 | 2026-09-30 04:51:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 1eab5896-d963-3ee8-861c-f18caba5d674 | -3.22715 | -46.9426 | 2026-09-30 04:51:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 2eaa1f98-cbe5-3fbe-bdca-eaba391a31a1 | -2.64282 | -49.27328 | 2026-09-30 04:51:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 2ed38a5b-b5b5-3614-8595-4995678bfb5b | -2.98472 | -51.02436 | 2026-09-30 04:51:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| c4a4c624-9c44-377b-9186-e9b77ae75f3e | -2.84244 | -51.57471 | 2026-09-30 04:51:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| e751bcdb-8dce-382c-9ed2-2106c2f5a92d | -3.24181 | -46.93783 | 2026-09-30 04:51:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 11e7370f-6323-3455-8191-65c1db536672 | -2.84187 | -51.57825 | 2026-09-30 04:51:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 511304f9-912c-3f83-a1a8-4e8155d03525 | -3.27957 | -50.08589 | 2026-09-30 04:51:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 6cbd4e77-0fe2-3daa-81f5-e8e5a92cac0a | -2.45128 | -49.21808 | 2026-09-30 04:51:00 | NOAA-20 | MOCAJUBA | PARÁ | Brasil | 1504604 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 098a0647-4c03-3563-a489-05d950770f86 | -2.97921 | -51.03767 | 2026-09-30 04:51:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| a5bc7841-13cc-3bc4-9620-18595a089a9b | 1.68444 | -55.9047 | 2026-09-30 04:51:00 | NOAA-20 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 046625f7-f122-3779-9b63-14506a90e7eb | -2.96649 | -51.03212 | 2026-09-30 04:51:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 6baf4d18-2ee2-34b8-81f3-54f0b4670321 | -2.97644 | -51.03369 | 2026-09-30 04:51:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| ef9fbe7b-4f5f-3fd0-8ef5-cc8d31251eda | -2.9737 | -51.051 | 2026-09-30 04:51:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 14.0 |
| bac0aa8f-93bb-3dbf-b784-176b44a32ade | -3.24048 | -46.94656 | 2026-09-30 04:51:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| c2daa41d-a6fd-3764-8820-fd9e4039cbef | -2.82463 | -46.70618 | 2026-09-30 04:51:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 3b440da8-71b9-33e4-9ae2-4d6d9a993df2 | -2.73251 | -49.41702 | 2026-09-30 04:51:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.3 |
| 94dde5d0-056c-374e-b210-91eb058c8da8 | -2.97091 | -51.02573 | 2026-09-30 04:51:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 60bbc95e-7f00-3b7d-abc0-8e24db1a07c0 | -0.48194 | -49.12953 | 2026-09-30 04:51:00 | NOAA-20 | CHAVES | PARÁ | Brasil | 1502509 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 0ebd9d98-3b97-373a-b333-6c8d9df946d1 | 1.80277 | -55.64781 | 2026-09-30 04:51:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 86e6f8fc-5ca2-3b19-a6e2-ba0e475fee4f | -3.25015 | -50.12037 | 2026-09-30 04:51:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 6dbb3615-573b-3fb8-9826-607c0ef5a6e0 | -1.59587 | -45.8126 | 2026-09-30 04:51:00 | NOAA-20 | CÂNDIDO MENDES | MARANHÃO | Brasil | 2102606 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| e0183bd1-15ca-32a6-be55-b76cd610bd03 | 1.6831 | -55.89589 | 2026-09-30 04:51:00 | NOAA-20 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 83e3c699-2948-34a3-ab5c-250e969a0e56 | -3.23812 | -46.93727 | 2026-09-30 04:51:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 30.3 |
| 012c6431-f080-38e0-9a47-7b36738a71f4 | -3.10589 | -50.28117 | 2026-09-30 04:51:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 7.8 |
| 8e6921ce-6f95-33e0-97e7-8b3da4900a93 | -3.00434 | -50.47313 | 2026-09-30 04:51:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 8f0aae1f-6bd0-3ee9-b39b-c150793ac931 | -3.10456 | -51.27424 | 2026-09-30 04:51:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| ffee4d98-6509-3a4a-a96b-5422760e4cee | -0.50375 | -49.11874 | 2026-09-30 04:51:00 | NOAA-20 | CACHOEIRA DO ARARI | PARÁ | Brasil | 1502004 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 47a956c5-2a58-3544-8031-18a3ff52b10e | -2.96816 | -51.04303 | 2026-09-30 04:51:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 5d97e644-a1f4-34c4-83b3-ea79521d610a | -3.23746 | -46.94163 | 2026-09-30 04:51:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 30.3 |
| e77adc4a-8bbc-3d01-a213-b21337e65e56 | -3.22044 | -46.93722 | 2026-09-30 04:51:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 4b38a98a-dde7-3c00-88bb-2354e8a357b0 | 0.31769 | -51.06651 | 2026-09-30 04:51:00 | NOAA-20 | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 3b87b0c4-1acd-370d-8120-c8e5eaca5912 | -2.94308 | -50.30112 | 2026-09-30 04:51:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 3930dec5-5b8e-3e77-9164-cf77b5d5c67e | -2.37626 | -47.60728 | 2026-09-30 04:51:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a1306624-6388-34bd-9f8d-bdbcc9510134 | -1.47064 | -48.91423 | 2026-09-30 04:51:00 | NOAA-20 | PONTA DE PEDRAS | PARÁ | Brasil | 1505700 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 4e64ccca-145f-3dee-8dcc-e27f05073134 | 0.70189 | -51.43288 | 2026-09-30 04:51:00 | NOAA-20 | PORTO GRANDE | AMAPÁ | Brasil | 1600535 | 16 | 33 | nan | nan | nan | Amazônia | 3.8 |
| fc8179e3-8510-38cf-9373-5cc6ce91db2a | 1.70637 | -55.9285 | 2026-09-30 04:51:00 | NOAA-20 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 762b0a7c-3745-3f12-ba30-dc089a6912ac | -1.12169 | -48.90737 | 2026-09-30 04:51:00 | NOAA-20 | CACHOEIRA DO ARARI | PARÁ | Brasil | 1502004 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| cf1e0c5b-83ea-3cf7-8008-e4a41f6f3efb | -3.02815 | -48.41774 | 2026-09-30 04:51:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 10.7 |
| da911c49-e96f-391b-8a0c-b8d6a8187635 | -3.27087 | -50.14109 | 2026-09-30 04:51:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ab5f5161-ffc6-3c0e-8bf1-b3e0f1ccb39b | -3.22414 | -46.93773 | 2026-09-30 04:51:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 719fc195-e58d-37ae-9ec6-80f0a8b3f9ab | -1.05738 | -53.58758 | 2026-09-30 04:51:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 214cd229-2fd9-3c71-b9ba-953b4e0fd2f1 | -3.05553 | -51.70956 | 2026-09-30 04:51:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 629f2a43-20e8-3bb3-8474-67fd96994cae | -2.97148 | -51.04355 | 2026-09-30 04:51:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 7ba912bf-69af-369e-8a61-6794c1c4d630 | -2.37572 | -50.40892 | 2026-09-30 04:51:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 5cfad817-f2b4-3311-a843-88d0776cceea | -0.50762 | -49.11579 | 2026-09-30 04:51:00 | NOAA-20 | CACHOEIRA DO ARARI | PARÁ | Brasil | 1502004 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 11fb2987-baa5-3495-b559-2e83fbba2458 | -0.67369 | -49.24864 | 2026-09-30 04:51:00 | NOAA-20 | SANTA CRUZ DO ARARI | PARÁ | Brasil | 1506401 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| cba02a33-6333-3a83-9d6d-2c079f7ba602 | -2.97976 | -51.03421 | 2026-09-30 04:51:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 2962d384-55b4-3893-be2c-6168e6cee87d | -3.23509 | -46.93235 | 2026-09-30 04:51:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 55808d9a-f954-3103-bc44-b55108cd0787 | -3.18696 | -48.02587 | 2026-09-30 04:51:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| a54e2c1a-c927-35da-864e-cb4d38a4f4f0 | -3.15269 | -51.03646 | 2026-09-30 04:51:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 5ed006e8-7de8-3d9f-9f17-9e29a3add3c9 | -3.28556 | -50.30572 | 2026-09-30 04:51:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| e0f250bf-2787-315a-a4c8-b86e45eb1b3f | -3.22483 | -46.93336 | 2026-09-30 04:51:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 5c40a228-dff6-3d77-b0f7-e9bf1c97ff66 | -3.22771 | -46.93123 | 2026-09-30 04:51:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 7a94c7b5-795b-3f07-bbe0-77ec6277be71 | -2.73584 | -49.41753 | 2026-09-30 04:51:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 7.2 |
| c11efbdb-944e-35d6-a701-dd9042f22c86 | -3.27626 | -50.08538 | 2026-09-30 04:51:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| cf31e993-bfeb-3e95-b6f4-230c010c4f26 | -3.22207 | -46.9508 | 2026-09-30 04:51:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| b67c9abc-7393-3f87-a614-3fa7c1b70af6 | 3.28294 | -60.62319 | 2026-09-30 04:51:00 | NOAA-20 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 8.0 |
| d335f6b4-0838-30a0-8601-34d2adec2acb | -2.96814 | -51.02175 | 2026-09-30 04:51:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 2b988926-eec4-3ba9-adc2-79db46f0a7a7 | -2.97754 | -51.02677 | 2026-09-30 04:51:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 59aff563-524b-3b1e-98ed-bf7a2bb5e2ac | -2.98907 | -50.43864 | 2026-09-30 04:51:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 23eecaac-04ac-3714-b4e9-c0f0ffcc4945 | -3.14882 | -51.03939 | 2026-09-30 04:51:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 177a00f2-8b81-3acb-b5ee-ab6c9f189781 | -3.22784 | -46.93824 | 2026-09-30 04:51:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 5157522f-d99a-3d7d-8b91-1de94d575b88 | -3.26701 | -50.14402 | 2026-09-30 04:51:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 7d3677e1-fa76-3118-b8ca-85aff3878c30 | -2.97477 | -51.02279 | 2026-09-30 04:51:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| fed07f2c-624b-381f-8fa3-4ad36a75dc1d | -2.97919 | -51.0164 | 2026-09-30 04:51:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 625fc85e-abac-3613-90b4-a294884dbad8 | -2.98861 | -51.04271 | 2026-09-30 04:51:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| da1f542a-4e96-35f2-838a-803c5e7969fc | -2.38393 | -47.60442 | 2026-09-30 04:51:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 2ed48028-62ac-3941-b635-087dfed49f25 | -2.97864 | -51.01986 | 2026-09-30 04:51:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| f8a080e5-fb4d-3a3e-80b0-ad03656b6d01 | -0.50707 | -49.11926 | 2026-09-30 04:51:00 | NOAA-20 | CACHOEIRA DO ARARI | PARÁ | Brasil | 1502004 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 9dc93c0a-2612-3809-9c36-fdb7d9bfae8e | -3.09982 | -50.2767 | 2026-09-30 04:51:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| e106f4e4-2ac3-3601-bf72-128ccebe347b | -2.97036 | -51.02919 | 2026-09-30 04:51:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| f0021f02-8f73-372f-8e33-9f8f294585eb | -3.23008 | -46.94051 | 2026-09-30 04:51:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 6.7 |
| 5453a610-6fe0-39e4-807f-73e2203cca6e | 1.8627 | -55.62792 | 2026-09-30 04:51:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 73bf390e-46cf-3d8b-8c9d-4404edd93ef3 | -3.22853 | -46.93388 | 2026-09-30 04:51:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 6c03e4c9-05b2-311e-ae04-adac9bbb1227 | -3.553 | -48.17926 | 2026-09-30 04:51:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| be9fb496-321a-3e11-a3bf-c90c781ea2cf | -1.47846 | -48.90821 | 2026-09-30 04:51:00 | NOAA-20 | PONTA DE PEDRAS | PARÁ | Brasil | 1505700 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 320691fa-acd9-37e1-acdd-bfae30fa49bd | -3.23377 | -46.94107 | 2026-09-30 04:51:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 30.3 |
| 000e475a-b77e-32b2-86a3-cee10055cc8b | -2.36513 | -50.34743 | 2026-09-30 04:51:00 | NOAA-20 | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a5280df9-3ec2-3ecc-a5a3-9d57390d9a05 | -3.42 | -48.33492 | 2026-09-30 04:51:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 1ae99517-8332-38a8-ae0e-9d106de0b8eb | -2.96981 | -51.03265 | 2026-09-30 04:51:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 9.3 |


[Clique aqui para ver as próximas entradas](README41.md)
