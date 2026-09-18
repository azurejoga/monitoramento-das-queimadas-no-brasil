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

## Dados Diários - Página 76

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 7798db95-1c7f-3532-a2f2-1714ad266e61 | -1.21758 | -55.64043 | 2026-09-18 05:16:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| bd2a191f-d3fb-3237-89ea-70628f82e47b | -2.81422 | -50.47133 | 2026-09-18 05:16:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 27.3 |
| a6ec92a6-423c-36a4-a8e6-dcbb24ddceb0 | -5.73424 | -52.24433 | 2026-09-18 05:16:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 53cd3aed-07b6-3200-bc9e-f1bf595a2797 | -3.37227 | -50.4432 | 2026-09-18 05:16:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| c0a6aeec-d4be-3921-9ea8-e191eed1bd92 | -2.97328 | -54.15242 | 2026-09-18 05:16:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| eba2b80a-7183-3fa6-bc3c-02d25f328733 | -5.75695 | -45.09834 | 2026-09-18 05:16:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 3f1868bc-9cbb-34c8-b34e-ed44ca0da71c | -3.7312 | -52.27459 | 2026-09-18 05:16:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| a781698c-9b6a-3951-877d-d84a6c47e17f | -3.06745 | -49.51902 | 2026-09-18 05:16:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 552030ee-bba8-38c0-ba1d-916c9326c934 | -2.6792 | -57.61047 | 2026-09-18 05:16:00 | NOAA-20 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 406079ed-5c54-326d-87f7-5cbf935a22fb | -2.91778 | -50.41268 | 2026-09-18 05:16:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 19a524fb-ffb4-3b18-85c5-6de3aa810713 | -1.37787 | -49.36555 | 2026-09-18 05:16:00 | NOAA-20 | MUANÁ | PARÁ | Brasil | 1504901 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 65d635eb-d7b2-3187-b0e6-d303a2eca0a3 | -2.09929 | -52.03598 | 2026-09-18 05:16:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| e6e19ade-275f-34ee-b545-5656d71a1657 | -3.37453 | -52.79499 | 2026-09-18 05:16:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| e53b197b-1ea2-3eba-a210-a4d2ee85622c | -7.5515 | -45.67936 | 2026-09-18 05:16:00 | NOAA-20 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| f43b9fc3-2056-3abc-a517-f5dadd5cd61e | -3.3569 | -50.45443 | 2026-09-18 05:16:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| e026fe96-82fa-3de6-9562-c356f5419917 | -4.4308 | -55.52106 | 2026-09-18 05:16:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 44c2fbd9-5b6c-36fd-b3e5-1cbe2ddb162b | -6.48551 | -57.88031 | 2026-09-18 05:16:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| c170ce22-1a08-3376-bb9a-8137c650d938 | -4.51153 | -54.97347 | 2026-09-18 05:16:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 5dc090db-fee8-35e5-9371-e3ff5d73c6f8 | -3.96764 | -52.1887 | 2026-09-18 05:16:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 636bdb2b-cd70-305f-9696-1c8bfebdd8ca | -5.75254 | -45.0909 | 2026-09-18 05:16:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 5.7 |
| b7b11a87-2ff2-3dcb-91b5-7c0e2428c9f3 | -4.37441 | -55.02671 | 2026-09-18 05:16:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| da6f93ff-f8de-3ed3-b7c3-3ac1a9b53fa1 | -2.81862 | -50.47202 | 2026-09-18 05:16:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 27.3 |
| 5eb29eb7-ec6c-39e4-9b48-ab349aef74a1 | -3.36514 | -50.45431 | 2026-09-18 05:16:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 642fc86e-80ad-3ec1-9776-fa16f9d50028 | -4.01565 | -49.9502 | 2026-09-18 05:16:00 | NOAA-20 | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| f92f636d-79ea-360a-b597-6be297028bca | -2.81026 | -57.61706 | 2026-09-18 05:16:00 | NOAA-20 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| ef20315d-fc72-39e2-a5e9-3bad5eb8644e | -4.37667 | -55.03477 | 2026-09-18 05:16:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 62dfe8d2-51b8-34df-8433-e17ec10e83ab | -3.92028 | -55.75523 | 2026-09-18 05:16:00 | NOAA-20 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 2eadac88-46ed-317c-8beb-a9528d035fd2 | -1.78378 | -47.837 | 2026-09-18 05:16:00 | NOAA-20 | SÃO DOMINGOS DO CAPIM | PARÁ | Brasil | 1507201 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| e8e59cb4-ca4b-3820-ad68-a9b57826cb82 | -3.10854 | -57.68557 | 2026-09-18 05:16:00 | NOAA-20 | BOA VISTA DO RAMOS | AMAZONAS | Brasil | 1300680 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 6e365b4d-499a-30d7-8d98-97935c10c5d9 | -3.36449 | -50.45865 | 2026-09-18 05:16:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| a8f7cd99-d3c8-300d-8314-826d98054fcf | -3.47027 | -54.70989 | 2026-09-18 05:16:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 525dd3e9-67d0-36af-af44-519ff4d38707 | -1.14884 | -54.17134 | 2026-09-18 05:16:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 3e266b5a-1dce-3d5f-8dc3-16fef4f0ce4a | -4.54614 | -54.93246 | 2026-09-18 05:16:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| f4200287-db93-3d51-9102-e01f7ca0afab | -4.33777 | -55.44354 | 2026-09-18 05:16:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 81bea2aa-336d-391e-9487-8e1e4592c824 | -3.44114 | -58.20355 | 2026-09-18 05:16:00 | NOAA-20 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| cc1b1050-c14e-3fa4-8edf-03c901b80102 | -7.68059 | -46.10486 | 2026-09-18 05:16:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 44991b47-cecd-39b0-a402-cefe26097b5a | -6.09825 | -57.68746 | 2026-09-18 05:16:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 7e360dde-dd82-340e-8e1c-b1df5fe2c6a8 | -2.52084 | -57.23692 | 2026-09-18 05:16:00 | NOAA-20 | PARINTINS | AMAZONAS | Brasil | 1303403 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| d1152ec4-e5aa-3b1c-b35c-1092fdd955bb | -1.03356 | -53.737 | 2026-09-18 05:16:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 99a2df77-8a8f-3a36-a241-ddc456d2e4e2 | -3.06671 | -49.52408 | 2026-09-18 05:16:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 24d7e642-6ee9-38e6-aa23-19c7e1c0f9e3 | -7.11313 | -55.125 | 2026-09-18 05:16:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| b469496a-a344-3613-b759-f3491a767a87 | -4.79259 | -56.12187 | 2026-09-18 05:16:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 12.6 |
| 49cd9855-1683-3614-85b5-b55155245bf9 | -3.44551 | -58.42474 | 2026-09-18 05:16:00 | NOAA-20 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| b89fd796-0159-3a64-b5c8-1aa5bfcc1418 | -2.81776 | -50.47786 | 2026-09-18 05:16:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 6d4f178d-3f8b-3fd2-9c4a-cbe8ea45fc94 | -3.43551 | -58.21727 | 2026-09-18 05:16:00 | NOAA-20 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b08b79a1-144f-3905-b301-ba605ae3cd73 | -6.36958 | -58.28944 | 2026-09-18 05:16:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 1b9c2ec7-500c-3eab-816b-5e3d9367ca4b | -4.77227 | -55.71077 | 2026-09-18 05:16:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 5d2c2a09-5963-38a6-9318-e4b931c9a815 | -2.86978 | -49.62587 | 2026-09-18 05:16:00 | NOAA-20 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 2a697f87-9039-3237-b326-56896637007c | -6.43369 | -59.98037 | 2026-09-18 05:16:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 7.3 |
| b4ddb25c-ae7d-33b3-a4b7-6d74117cfafe | -4.51395 | -56.08277 | 2026-09-18 05:16:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 998652d2-9c12-3992-aa65-1acae7abd289 | -3.32046 | -57.84836 | 2026-09-18 05:16:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| b438e669-5787-390f-832d-6eb75b7a8365 | -4.38069 | -55.0316 | 2026-09-18 05:16:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 523878ba-05be-32b6-bbd5-769c45778e39 | -3.88471 | -58.9431 | 2026-09-18 05:16:00 | NOAA-20 | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| ef2ec114-20bb-37a6-961d-17ec38af4c43 | -3.27023 | -54.26801 | 2026-09-18 05:16:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d4e52b8c-0b81-3855-a3ea-35cabdc863e6 | -0.77986 | -47.55395 | 2026-09-18 05:16:00 | NOAA-20 | MARACANÃ | PARÁ | Brasil | 1504307 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| c22dc4b0-a5db-34a1-8bfc-c7ab2b70e3b0 | -4.43236 | -55.08106 | 2026-09-18 05:16:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 6f335f8f-1798-3d4c-acc2-b73a19706578 | -2.05467 | -52.16939 | 2026-09-18 05:16:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| da2ada8a-5a82-38dd-9dc3-78c8eea7bb2a | -3.34486 | -59.44874 | 2026-09-18 05:16:00 | NOAA-20 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 9317379f-d94b-3d3b-a9f3-8a591f065ec0 | -1.72264 | -55.75512 | 2026-09-18 05:16:00 | NOAA-20 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 1f046435-5070-372e-9294-981ff744c6de | -3.35625 | -50.45303 | 2026-09-18 05:16:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| f4bdf083-f3ff-3841-a19c-1931e77fb8a0 | -4.48433 | -54.97385 | 2026-09-18 05:16:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 984f5e97-2d53-3bf0-a5da-a91f0d288b27 | -1.70504 | -54.89001 | 2026-09-18 05:16:00 | NOAA-20 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 6d1b0ed5-d632-3898-840a-79357e73fe65 | -2.82786 | -50.47079 | 2026-09-18 05:16:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 45.2 |
| 0cebe094-faea-3fa5-a24f-3cfd4e7d1f43 | -2.36976 | -55.24956 | 2026-09-18 05:16:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 0d7462f5-efde-334e-9da2-4a77ec64149f | -5.72937 | -51.75075 | 2026-09-18 05:16:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 50f7d547-9dde-39b0-b497-c25dd99880a5 | -6.45878 | -46.0105 | 2026-09-18 05:16:00 | NOAA-20 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| ac11deb4-2afd-344c-a98c-d0dbc9d79d94 | -3.72351 | -60.61936 | 2026-09-18 05:16:00 | NOAA-20 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 56acde4c-b10f-3a5b-beb6-07817d3a0527 | -4.56294 | -54.91541 | 2026-09-18 05:16:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| d9808ce6-4a54-3eb6-8582-a44ef4290f7c | -4.37226 | -55.42292 | 2026-09-18 05:16:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| cc8c2084-1be7-381d-8c23-990248b5b252 | -3.13169 | -59.02222 | 2026-09-18 05:16:00 | NOAA-20 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| ebe1922a-16da-3686-a976-0af8e821dd23 | -2.89972 | -54.1854 | 2026-09-18 05:16:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 4e1a2cb9-6dfe-358d-8e51-cbfcef352926 | -3.03768 | -51.37526 | 2026-09-18 05:16:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 11.8 |
| 1eae1232-922a-37a8-b55d-3f13da29f532 | -5.88868 | -49.78331 | 2026-09-18 05:16:00 | NOAA-20 | CURIONÓPOLIS | PARÁ | Brasil | 1502772 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| cdf81402-8fd4-335a-8c89-ee30f45ebfb7 | -2.81974 | -50.46521 | 2026-09-18 05:16:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| ecbad058-44f2-3e3c-886c-390e5030c6c3 | -4.87621 | -56.06966 | 2026-09-18 05:16:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 2013b745-952c-3609-a3eb-6116b4917d26 | -3.69354 | -54.54434 | 2026-09-18 05:16:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 5c070bde-7575-3cc3-939f-8420095a0abc | -3.43611 | -58.1918 | 2026-09-18 05:16:00 | NOAA-20 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 771513d1-e088-358b-b426-7d4db5bb2645 | -5.82945 | -49.95666 | 2026-09-18 05:16:00 | NOAA-20 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 9a47b5cf-caea-3fd5-aa51-7df06e349d15 | -7.79619 | -44.90342 | 2026-09-18 05:16:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| d27c0b51-7c2a-3db8-8c38-a16080811e25 | -5.51312 | -43.66861 | 2026-09-18 05:16:00 | NOAA-20 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| c4cb3653-81fa-3b13-b26a-11c4a5be49a4 | -4.27443 | -55.55316 | 2026-09-18 05:16:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 67d5384a-f228-3208-8618-74d96910245b | -5.88639 | -52.08835 | 2026-09-18 05:16:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 38c17104-af35-302a-b56b-6d2d43cb884b | -4.36488 | -55.64785 | 2026-09-18 05:16:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 9813b29e-91f0-31d1-be7a-eff21fb19afa | -5.49845 | -45.5208 | 2026-09-18 05:16:00 | NOAA-20 | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 2f809f2f-3027-3f8a-bd76-f4397ab9bc4e | -2.35517 | -55.23262 | 2026-09-18 05:16:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| fdbf4e2a-85af-3e26-88f7-ac5e99db8d29 | -4.88068 | -56.0631 | 2026-09-18 05:16:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 3be9e98c-0ecf-3303-86ae-0fcd7cb3f291 | -1.62316 | -55.11683 | 2026-09-18 05:16:00 | NOAA-20 | CURUÁ | PARÁ | Brasil | 1502855 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 57efbe0d-b31a-3114-9478-8710b94869da | -4.48315 | -54.98135 | 2026-09-18 05:16:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 3c1e4230-2412-369b-bc25-472345bdedd3 | -5.17442 | -56.18149 | 2026-09-18 05:16:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| fa719195-94bd-3626-9459-9894caffa513 | -6.10647 | -57.63562 | 2026-09-18 05:16:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 670aa6c8-6204-35c7-87c7-9f53917580d4 | -2.84522 | -57.63329 | 2026-09-18 05:16:00 | NOAA-20 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| a8997bc5-4872-34fb-81e6-51f68d241001 | -4.43418 | -55.52164 | 2026-09-18 05:16:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| e4a86295-622b-37c0-be4a-92990d4eb10c | -3.16668 | -53.93044 | 2026-09-18 05:16:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 548aa2b9-a5a9-372e-b615-bf3c2f39adc6 | -1.03707 | -53.73757 | 2026-09-18 05:16:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 0a379fbd-705d-32a2-973c-9c79752aeb7c | -3.44506 | -58.20053 | 2026-09-18 05:16:00 | NOAA-20 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| f7286ee4-9460-3b4a-8759-f18c4c8cf3e4 | -3.14849 | -53.9371 | 2026-09-18 05:16:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 9b5dfce5-3609-304d-a89c-13ff2670e6f8 | -2.90212 | -54.16973 | 2026-09-18 05:16:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 71979cff-4576-3909-8e29-7f0602ee0fe3 | -2.9032 | -50.41928 | 2026-09-18 05:16:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 1bf32fbd-21f3-3c00-986b-3e695fce4d10 | -3.27145 | -54.26019 | 2026-09-18 05:16:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 966df50c-3556-3c7c-804c-ba41373ae92e | -2.8991 | -54.18622 | 2026-09-18 05:16:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |


[Clique aqui para ver as próximas entradas](README77.md)
