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

## Dados Diários - Página 130

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 7d3794a9-6701-3cf7-9261-dc1a25a6b74b | 1.49489 | -55.64208 | 2026-10-05 17:17:00 | NPP-375 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 571acba0-4295-3604-baf5-1dbecedc264d | -1.6512 | -55.18612 | 2026-10-05 17:17:00 | NPP-375 | CURUÁ | PARÁ | Brasil | 1502855 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| dea16ce3-555a-30f6-9291-383101109d82 | -1.42826 | -52.72612 | 2026-10-05 17:17:00 | NPP-375 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| bd47006f-6ed6-3daf-bab7-45e243ea6629 | 2.26021 | -50.82676 | 2026-10-05 17:17:00 | NPP-375 | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 14.2 |
| 0c71b95d-855f-33f9-9f29-e7937c3a8af4 | -3.35036 | -58.28931 | 2026-10-05 17:17:00 | NPP-375 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 11.8 |
| f83bc0f7-2986-3f20-b226-340067ff5c09 | -3.32341 | -59.47847 | 2026-10-05 17:17:00 | NPP-375 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 11.4 |
| 7f7a6699-a4e5-3bf9-8973-53c5e7643563 | -2.98338 | -54.10343 | 2026-10-05 17:17:00 | NPP-375 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 05bad869-7ce1-30a9-b632-6815166e98d7 | -3.68114 | -59.62867 | 2026-10-05 17:17:00 | NPP-375 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 11.1 |
| d974362f-688e-36fe-af32-dc1662ab3c1f | -2.88997 | -54.15383 | 2026-10-05 17:17:00 | NPP-375 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 06c01e61-a08e-30a7-9425-4a93548ff381 | -2.90701 | -54.08772 | 2026-10-05 17:17:00 | NPP-375 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 7.1 |
| 5fa6619b-7484-38bd-8825-bb3fbb054a46 | 1.73745 | -55.71554 | 2026-10-05 17:17:00 | NPP-375 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| ef2b362f-323d-35fc-b381-1555307e385f | -1.27984 | -56.98051 | 2026-10-05 17:17:00 | NPP-375 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| dc072343-b86e-3026-ab21-de56a0f68dbf | -3.24218 | -64.83484 | 2026-10-05 17:17:00 | NPP-375 | ALVARÃES | AMAZONAS | Brasil | 1300029 | 13 | 33 | nan | nan | nan | Amazônia | 13.6 |
| 42f1b3e9-4f69-38c9-ada0-7dea370a4d25 | 3.52118 | -51.49729 | 2026-10-05 17:17:00 | NPP-375 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 4.2 |
| fab8d2f8-b77b-3467-a9fe-e73df892e458 | -3.32855 | -59.48507 | 2026-10-05 17:17:00 | NPP-375 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 18.9 |
| 5a00124a-ecd8-32c7-84e1-ea4d1deb2c63 | -2.94044 | -54.12851 | 2026-10-05 17:17:00 | NPP-375 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 7.3 |
| a1866404-d331-3fd3-9474-9c40fda18d8b | -0.46241 | -52.02449 | 2026-10-05 17:17:00 | NPP-375 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 13.7 |
| fa02d862-6709-3729-a53b-1e7e8ff94166 | -2.9378 | -54.11125 | 2026-10-05 17:17:00 | NPP-375 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 6.6 |
| b1e757c6-8a01-32a7-8619-36511b3eece1 | -2.07658 | -48.43297 | 2026-10-05 17:17:00 | NPP-375 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 8.5 |
| 884f9bd2-15e0-34f4-a210-f7e858d90cf8 | -1.41851 | -55.4136 | 2026-10-05 17:17:00 | NPP-375 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 7fe3c6d8-2a39-3904-9047-53e785db5465 | -3.32289 | -59.47486 | 2026-10-05 17:17:00 | NPP-375 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 9.0 |
| c7276d01-d88f-30d3-a7b0-ab644822fb12 | -3.309 | -57.75638 | 2026-10-05 17:17:00 | NPP-375 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 1667a1cd-7d17-306f-9738-f4e2679f2e9d | -3.75127 | -61.01609 | 2026-10-05 17:17:00 | NPP-375 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 28.4 |
| cf9d6da5-0257-3da3-b1ba-df4d7f055f33 | 1.49158 | -55.64157 | 2026-10-05 17:17:00 | NPP-375 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 7c7e36d1-9bb6-3a43-8c6b-8ec15c33526d | -1.77425 | -53.77909 | 2026-10-05 17:17:00 | NPP-375 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 7.1 |
| 798d9550-5735-3ad0-8839-4c6d243655ec | -3.17607 | -60.05633 | 2026-10-05 17:17:00 | NPP-375 | IRANDUBA | AMAZONAS | Brasil | 1301852 | 13 | 33 | nan | nan | nan | Amazônia | 10.1 |
| 26702585-65a9-3434-8cc6-75979c5469d2 | -1.33247 | -56.41097 | 2026-10-05 17:17:00 | NPP-375 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 6365f410-a0b6-38f7-97fc-0d88a32d2e10 | 1.9134 | -55.7221 | 2026-10-05 17:20:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 70.1 |
| b3a806bc-78f9-3e77-bb6b-10f9b1e0f2b6 | -9.1072 | -67.8326 | 2026-10-05 17:20:00 | GOES-19 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 93.1 |
| 827c7e7a-c787-3454-bd92-4ce857507461 | -7.3272 | -72.6446 | 2026-10-05 17:20:00 | GOES-19 | GUAJARÁ | AMAZONAS | Brasil | 1301654 | 13 | 33 | nan | nan | nan | Amazônia | 170.2 |
| c4fb0c5e-2663-31fe-8b1e-b2369b72e72b | -9.1408 | -64.3836 | 2026-10-05 17:20:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 67.9 |
| a2280519-24fa-3255-a0d4-f6238b79c208 | -9.5594 | -66.0359 | 2026-10-05 17:20:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 55.8 |
| a8f3c294-5835-376a-9fec-c7a58a15a52d | -9.077 | -66.0881 | 2026-10-05 17:20:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 76.8 |
| 05eae21d-a49c-3e5f-85f7-d80332566820 | -9.8618 | -65.0146 | 2026-10-05 17:20:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 49.1 |
| fce77218-0806-3200-977e-90a444615c57 | -9.0585 | -66.0887 | 2026-10-05 17:20:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 51.3 |
| a30328fa-c6be-3d0f-8450-1d47b84f709b | -9.0584 | -66.1073 | 2026-10-05 17:20:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 66.4 |
| dbb53f4c-ab42-32aa-b0e1-91a67fa05bc9 | -9.1147 | -65.9379 | 2026-10-05 17:20:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 60.9 |
| 0b9a2df8-0430-3bee-a0c3-9434fefc5faa | -8.6293 | -66.9926 | 2026-10-05 17:20:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 49.6 |
| 4c7d219c-5d94-31ac-b771-f44221346707 | -8.852 | -66.7827 | 2026-10-05 17:20:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 182.8 |
| 1d312c89-92fa-31a4-9c82-ea44980d48e3 | -9.8061 | -64.9979 | 2026-10-05 17:20:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 47.2 |
| 11b465a4-3e50-34fe-b0d6-0d244653b7a5 | -9.1076 | -67.7215 | 2026-10-05 17:20:00 | GOES-19 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 56.3 |
| 14babb14-50f8-3cba-91f6-a20d3de717cb | -9.9174 | -65.0501 | 2026-10-05 17:20:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 46.1 |
| b1778ef1-d47d-37cc-a433-341f19ee2f47 | -9.0889 | -67.759 | 2026-10-05 17:20:00 | GOES-19 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 58.1 |
| 683a267f-a524-31fe-b1e5-e12715139130 | -9.1222 | -64.3843 | 2026-10-05 17:20:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 67.7 |
| f00239d4-e46b-3856-9770-2d2c9787aa71 | -8.7816 | -72.7807 | 2026-10-05 17:20:00 | GOES-19 | MARECHAL THAUMATURGO | ACRE | Brasil | 1200351 | 12 | 33 | nan | nan | nan | Amazônia | 48.1 |
| e421c6d7-bb2a-37b5-9559-f8078aedc7c2 | -9.1407 | -64.4024 | 2026-10-05 17:20:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 65.1 |
| 7f5d0c48-5a87-3e56-a8b1-12151cf79ea9 | -8.593 | -66.8081 | 2026-10-05 17:20:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 149.7 |
| 4654ee19-b0ce-36f8-97cb-08ae767b5ce5 | -7.3823 | -72.717 | 2026-10-05 17:20:00 | GOES-19 | GUAJARÁ | AMAZONAS | Brasil | 1301654 | 13 | 33 | nan | nan | nan | Amazônia | 41.5 |
| 90c0f1f3-8ef7-3f5d-b1cd-4594564980de | -9.1037 | -64.385 | 2026-10-05 17:20:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 47.1 |
| 93f395f0-5d70-3ae6-a5d8-09ae93a7d3ea | -9.1536 | -65.5447 | 2026-10-05 17:20:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 79.5 |
| 3e2703ff-b6d4-3011-9d20-89038834f015 | -9.1442 | -67.8317 | 2026-10-05 17:20:00 | GOES-19 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 45.8 |
| fd5be0e8-f8c9-317a-952d-4aea5cf85fa9 | -8.8519 | -66.8012 | 2026-10-05 17:20:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 206.5 |
| f6889b2d-a9cf-3428-93bc-c6a73c3238e7 | -9.4751 | -64.3336 | 2026-10-05 17:20:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 60.0 |
| 0c27c730-5192-3ac8-8f6b-79c5e188f099 | 3.56175 | -61.36553 | 2026-10-05 17:20:00 | NPP-375 | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 7.3 |
| 95ff404a-a0ae-3bf0-98d1-9339855975aa | 3.57607 | -61.35616 | 2026-10-05 17:20:00 | NPP-375 | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 8.9 |
| 81456f71-8f36-36e1-b533-70c2262c51b4 | 3.57667 | -61.3524 | 2026-10-05 17:20:00 | NPP-375 | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 7.0 |
| ffa87264-a91d-302b-94a4-2be937e414eb | 3.06406 | -60.60524 | 2026-10-05 17:20:00 | NPP-375 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 8.7 |
| 2b39c3d6-3f62-36a0-9e0b-40fee306c1d6 | 4.05219 | -59.9883 | 2026-10-05 17:20:00 | NPP-375 | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 37.3 |
| 22a037e0-b61e-37b8-a2f4-61734434cdef | 3.56955 | -61.34356 | 2026-10-05 17:20:00 | NPP-375 | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 697dc6a4-b241-362c-867b-7bbab39cde42 | 3.56236 | -61.36174 | 2026-10-05 17:20:00 | NPP-375 | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 7.3 |
| 68f1ae6f-fa39-33df-b3c8-b572cf8954b8 | 3.56418 | -61.35041 | 2026-10-05 17:20:00 | NPP-375 | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 6.0 |
| acb2c1e4-5ab6-342b-9841-8720689afd51 | 4.23493 | -60.36324 | 2026-10-05 17:20:00 | NPP-375 | UIRAMUTÃ | RORAIMA | Brasil | 1400704 | 14 | 33 | nan | nan | nan | Amazônia | 13.4 |
| 80947a6e-7661-3f3b-a625-901e8d9f366b | 3.5749 | -61.33672 | 2026-10-05 17:20:00 | NPP-375 | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 8.1 |
| faaa6c47-ef17-3d1d-a9fc-7036358a2cf2 | 3.56478 | -61.34666 | 2026-10-05 17:20:00 | NPP-375 | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 6.0 |
| d4a1c346-a13c-3838-b3d1-629d038b70a9 | 3.95322 | -59.85688 | 2026-10-05 17:20:00 | NPP-375 | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 13870f5b-3204-3cbd-b90e-0c0694b2a69e | 4.21459 | -60.71457 | 2026-10-05 17:20:00 | NPP-375 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 17.0 |
| e41dd734-d159-3d5f-bf8f-4f950c985f35 | 4.05147 | -59.99038 | 2026-10-05 17:20:00 | NPP-375 | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 15.0 |
| 7a80b339-41e7-3017-b93b-209b89f3c3cf | 3.58738 | -61.33873 | 2026-10-05 17:20:00 | NPP-375 | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 0b16aa07-441f-34f6-aebe-43f830dfb9e1 | 3.5725 | -61.35175 | 2026-10-05 17:20:00 | NPP-375 | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 7.0 |
| 6a755db8-f8a0-34b5-b857-b81c5503adcb | 4.05526 | -59.991 | 2026-10-05 17:20:00 | NPP-375 | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 15.0 |
| 46509066-0a80-3241-ba51-9ebaa6f9bad1 | 4.22794 | -60.4065 | 2026-10-05 17:20:00 | NPP-375 | UIRAMUTÃ | RORAIMA | Brasil | 1400704 | 14 | 33 | nan | nan | nan | Amazônia | 15.7 |
| 7f857537-c4ed-3666-af97-f7096d9da7ab | 4.21854 | -60.7152 | 2026-10-05 17:20:00 | NPP-375 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 17.0 |
| 150306d9-acb5-3ae8-b631-29484b7d0e36 | 3.58322 | -61.33805 | 2026-10-05 17:20:00 | NPP-375 | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 6.2 |
| d38bffc8-faee-3c76-9d46-ff193d79fffe | 3.7562 | -51.6103 | 2026-10-05 17:20:00 | NPP-375 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 3.6 |
| ef55d0b3-87f2-3b1a-b4c0-0bf067e496cc | 4.44232 | -60.08353 | 2026-10-05 17:20:00 | NPP-375 | UIRAMUTÃ | RORAIMA | Brasil | 1400704 | 14 | 33 | nan | nan | nan | Amazônia | 10.1 |
| 6f8412d4-90d8-371f-8e73-168457c17c0d | 4.23257 | -60.40246 | 2026-10-05 17:20:00 | NPP-375 | UIRAMUTÃ | RORAIMA | Brasil | 1400704 | 14 | 33 | nan | nan | nan | Amazônia | 11.0 |
| a836e025-8013-3260-ae47-22db85ee27bd | 3.87133 | -51.79942 | 2026-10-05 17:20:00 | NPP-375 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 9.5 |
| 7375f845-7041-3764-a349-52688b70caad | 3.56114 | -61.36932 | 2026-10-05 17:20:00 | NPP-375 | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 38108ff6-da72-3f68-a542-07301d83f69f | 3.57963 | -61.36058 | 2026-10-05 17:20:00 | NPP-375 | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 7.1 |
| 950033f2-c8e9-3f43-9eb8-921ec1240463 | 4.05221 | -59.98584 | 2026-10-05 17:20:00 | NPP-375 | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 18.4 |
| d52ff85a-373c-316f-aafd-8c620da04e5c | 3.58319 | -61.36508 | 2026-10-05 17:20:00 | NPP-375 | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 9.0 |
| c23d78cd-9147-3680-88dc-959ecbbdad00 | 4.0484 | -59.98763 | 2026-10-05 17:20:00 | NPP-375 | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 9.7 |
| 8327da92-1d5d-3f28-9031-0377cf97fa17 | 3.56297 | -61.35794 | 2026-10-05 17:20:00 | NPP-375 | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 10.7 |
| 3668f7f5-cc4c-323d-a556-e61f622137d1 | 3.57015 | -61.33981 | 2026-10-05 17:20:00 | NPP-375 | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 3.5 |
| ffe7c498-7f2e-3364-9823-fc92bab53af5 | 4.9747 | -59.99051 | 2026-10-05 17:20:00 | NPP-375 | UIRAMUTÃ | RORAIMA | Brasil | 1400704 | 14 | 33 | nan | nan | nan | Amazônia | 11.7 |
| ba3f75bf-65ed-3be3-88d8-3a1c96f6e598 | 2.65493 | -63.7431 | 2026-10-05 17:20:00 | NPP-375 | ALTO ALEGRE | RORAIMA | Brasil | 1400050 | 14 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 397fac22-3be7-3d5a-976c-031deec9a7a4 | -30.00801 | -50.67131 | 2026-10-05 17:28:00 | NOAA-20 | SANTO ANTÔNIO DA PATRULHA | RIO GRANDE DO SUL | Brasil | 4317608 | 43 | 33 | nan | nan | nan | Pampa | 10.8 |
| 6d97aae6-dca7-3d81-b508-f7b23d385db4 | -30.01163 | -50.67051 | 2026-10-05 17:28:00 | NOAA-20 | SANTO ANTÔNIO DA PATRULHA | RIO GRANDE DO SUL | Brasil | 4317608 | 43 | 33 | nan | nan | nan | Pampa | 6.6 |
| d93543c5-7bf6-336a-bef6-e41b4dfbf1ce | 1.7671 | -55.6056 | 2026-10-05 17:30:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 46.2 |
| 9b18eb02-1b16-3bf8-9b40-dbb75eb237be | -9.1221 | -64.4031 | 2026-10-05 17:30:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 48.4 |
| 322d6b92-ddd7-3464-8acf-85383ae8300c | -8.7521 | -68.985 | 2026-10-05 17:30:00 | GOES-19 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 115.0 |
| 9ed19c43-8ac7-303c-8cf4-04e21e5bc93e | -8.9171 | -69.4605 | 2026-10-05 17:30:00 | GOES-19 | MANOEL URBANO | ACRE | Brasil | 1200344 | 12 | 33 | nan | nan | nan | Amazônia | 104.0 |
| 2d967aec-a7b5-3daa-a670-6b2199ed7041 | -9.4819 | -66.7836 | 2026-10-05 17:30:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 64.6 |
| 5fd2efb0-a3ef-3774-94ce-3afb241643e1 | -8.593 | -66.8081 | 2026-10-05 17:30:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 131.7 |
| 84907d69-d86d-3d6e-a444-93b54f40afef | -9.5594 | -66.0359 | 2026-10-05 17:30:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 61.0 |
| e0799380-ad17-3d7b-bd82-28b069d02616 | -9.1147 | -65.9379 | 2026-10-05 17:30:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 60.5 |
| f10406d5-533d-36f0-8d9f-edd771a2b74f | -9.3929 | -65.9105 | 2026-10-05 17:30:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 51.0 |
| 09d197ee-59a0-3031-8d07-758e9d0bd094 | 1.9317 | -55.7219 | 2026-10-05 17:30:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 69.2 |
| d6acbd26-7a2c-3b77-b390-7ed84beff335 | -9.0286 | -69.2559 | 2026-10-05 17:30:00 | GOES-19 | MANOEL URBANO | ACRE | Brasil | 1200344 | 12 | 33 | nan | nan | nan | Amazônia | 55.7 |
| 465a7ae0-5c7a-3c90-ae15-e78ced57e405 | -9.0585 | -66.0887 | 2026-10-05 17:30:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 61.3 |


[Clique aqui para ver as próximas entradas](README131.md)
