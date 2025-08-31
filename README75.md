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

## Dados Diários - Página 75

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 6e2957ea-a963-3c4d-bb6a-8a0ce1ca36eb | -9.45948 | -62.35103 | 2025-08-31 05:44:00 | NOAA-21 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 8.6 |
| 50d2be31-9e8e-30b3-b089-18b60cdc6f2a | -9.68699 | -62.25024 | 2025-08-31 05:44:00 | NOAA-21 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 96068d78-1a8f-33be-9093-4b2598db4ae8 | -12.92798 | -56.98877 | 2025-08-31 05:44:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 719e1a58-7b1b-34ef-9f80-1419408d9e1a | -8.96438 | -65.96864 | 2025-08-31 05:44:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e07ef436-12ff-3c7e-881c-fbac874b0b02 | -8.88534 | -62.3898 | 2025-08-31 05:44:00 | NOAA-21 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 92a6bfe9-b71d-342d-94ee-b79b5f0378ea | -10.72509 | -65.04542 | 2025-08-31 05:44:00 | NOAA-21 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| ce47dd44-79c8-3dc2-8584-32f0723f39e3 | -8.74209 | -62.39668 | 2025-08-31 05:44:00 | NOAA-21 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 2.7 |
| c896549f-4362-34f6-a87b-534f80543c13 | -8.81593 | -63.90619 | 2025-08-31 05:44:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 0f81ef4d-ca35-3902-af8d-8936854b0ec5 | -8.6792 | -66.93569 | 2025-08-31 05:44:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 2d014d93-b6ec-3d71-9986-0732da8ca13e | -14.79934 | -59.72393 | 2025-08-31 05:44:00 | NOAA-21 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 5.6 |
| dbf85b7d-8ced-3993-a5a6-4a1db5a1207d | -11.32212 | -63.2706 | 2025-08-31 05:44:00 | NOAA-21 | SÃO MIGUEL DO GUAPORÉ | RONDÔNIA | Brasil | 1100320 | 11 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 8f9c425c-6adf-3b31-89b2-fcffe9adb936 | -8.86103 | -63.02368 | 2025-08-31 05:44:00 | NOAA-21 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 0edadbe0-dc0f-3c6c-9526-9da5f9ab8bba | -8.92144 | -62.42678 | 2025-08-31 05:44:00 | NOAA-21 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 7da34609-f961-39a1-a31b-f620eb7936d5 | -8.74154 | -62.38087 | 2025-08-31 05:44:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.1 |
| f5e6f11d-bdc9-33d7-8523-8cc9d0873ebf | -12.94001 | -56.98281 | 2025-08-31 05:44:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 27005a5f-f997-3789-9f2c-5cd5578af162 | -8.5587 | -63.01536 | 2025-08-31 05:44:00 | NOAA-21 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 77ab70d0-ac65-327c-9f91-ff383c4ae083 | -9.45371 | -60.54965 | 2025-08-31 05:44:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d1c2c148-6110-3c6a-b00b-c37c5e12ef9b | -8.84206 | -66.72352 | 2025-08-31 05:44:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 929184d4-3dcc-31b6-90d2-32c5e3415758 | -9.32492 | -61.91954 | 2025-08-31 05:44:00 | NOAA-21 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 88172091-626a-3ab9-9954-974a3f967060 | -8.74768 | -62.38401 | 2025-08-31 05:44:00 | NOAA-21 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 2.3 |
| afbdcbe7-309d-39ac-9673-f197d0d68d82 | -8.74022 | -62.3897 | 2025-08-31 05:44:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 0181b618-4d10-3329-944b-35e9e31027b7 | -12.4358 | -63.92352 | 2025-08-31 05:44:00 | NOAA-21 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 5f02bfea-4d2f-321c-bdc6-700817f802ef | -8.2345 | -72.80968 | 2025-08-31 05:44:00 | NOAA-21 | PORTO WALTER | ACRE | Brasil | 1200393 | 12 | 33 | nan | nan | nan | Amazônia | 1.5 |
| f17083ae-4785-31b1-b515-3ec3d78ae481 | -9.71877 | -62.39936 | 2025-08-31 05:44:00 | NOAA-21 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 13062c7f-6635-3149-bd65-5e28300d5219 | -11.32575 | -63.27116 | 2025-08-31 05:44:00 | NOAA-21 | SÃO MIGUEL DO GUAPORÉ | RONDÔNIA | Brasil | 1100320 | 11 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 228ffc9b-162a-3964-b01e-459b72c87493 | -13.03193 | -56.91064 | 2025-08-31 05:44:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 46dac332-2199-3054-9af3-cc69f0387ca0 | -8.73956 | -62.39411 | 2025-08-31 05:44:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 0b17434b-d249-3bba-b737-07c19a527e15 | -9.45509 | -62.35499 | 2025-08-31 05:44:00 | NOAA-21 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 4.5 |
| b3b88b87-3b95-3d77-ae29-e1db87499908 | -9.44325 | -62.35776 | 2025-08-31 05:44:00 | NOAA-21 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 6201a15f-2d3a-3478-a6c3-867c4fcb1890 | -9.06352 | -65.41682 | 2025-08-31 05:44:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 82293499-bb75-32ae-bba3-c3bf6f68d54f | -15.23196 | -56.06885 | 2025-08-31 05:44:00 | NOAA-21 | CUIABÁ | MATO GROSSO | Brasil | 5103403 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 36eeddf5-4f9f-323a-8588-afea1cace06d | -8.64828 | -62.83068 | 2025-08-31 05:44:00 | NOAA-21 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 4ce2ab0e-cfdc-38c6-a357-dac530fab841 | -10.31819 | -59.20237 | 2025-08-31 05:44:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 3103191a-4a84-3fe5-95ae-398692c8777a | -11.83015 | -62.92646 | 2025-08-31 05:44:00 | NOAA-21 | SERINGUEIRAS | RONDÔNIA | Brasil | 1101500 | 11 | 33 | nan | nan | nan | Amazônia | 2.4 |
| e3b5a36b-38dd-3e28-b1de-2c232027ca47 | -9.71504 | -62.39877 | 2025-08-31 05:44:00 | NOAA-21 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 209059f3-18d1-31ab-a209-6e88e4a1bab4 | -9.45463 | -62.33186 | 2025-08-31 05:44:00 | NOAA-21 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 01d894f7-b3c0-3f15-beeb-755a7d14c657 | -7.87658 | -63.27359 | 2025-08-31 05:44:00 | NOAA-21 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| d2ca4882-1e2d-38d7-9a4b-aa61b9c21108 | -15.23144 | -56.07395 | 2025-08-31 05:44:00 | NOAA-21 | CUIABÁ | MATO GROSSO | Brasil | 5103403 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| d5ccf53c-b64d-3593-85a9-9c7297be62c4 | -8.66628 | -62.83341 | 2025-08-31 05:44:00 | NOAA-21 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 7.4 |
| 4d9adfe2-b9e4-38fd-b0e2-01aa167ab6ee | -8.73653 | -62.38914 | 2025-08-31 05:44:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 2c9452c5-e10c-3253-8c0f-1f1b70951e4f | -9.44586 | -62.33979 | 2025-08-31 05:44:00 | NOAA-21 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 08c2090e-ec3e-3b60-af90-9d54315eed80 | -9.6755 | -63.17112 | 2025-08-31 05:44:00 | NOAA-21 | ALTO PARAÍSO | RONDÔNIA | Brasil | 1100403 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 50f8dc95-99db-3526-8c55-dfc5aa6ca4b1 | -8.72442 | -64.16413 | 2025-08-31 05:44:00 | NOAA-21 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 362507c7-370a-360f-b492-3b0960e3b51b | -8.64952 | -62.82235 | 2025-08-31 05:44:00 | NOAA-21 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| e4c39089-37e5-3974-bac4-0f2b52d20e53 | -8.56402 | -63.02869 | 2025-08-31 05:44:00 | NOAA-21 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 2.3 |
| f402b80c-696f-3c04-be58-58d6bede4c36 | -8.63904 | -67.25396 | 2025-08-31 05:44:00 | NOAA-21 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 3976e949-dafa-3b7e-be0e-879bb11402e6 | -11.32514 | -63.27544 | 2025-08-31 05:44:00 | NOAA-21 | SÃO MIGUEL DO GUAPORÉ | RONDÔNIA | Brasil | 1100320 | 11 | 33 | nan | nan | nan | Amazônia | 6.9 |
| 81a43503-2a13-3b77-a028-a6ba8cc1cebc | -7.68123 | -61.08986 | 2025-08-31 05:44:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 64b57682-4bf2-39a4-865c-0b726b72ed6d | -7.91602 | -63.00778 | 2025-08-31 05:44:00 | NOAA-21 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 43748104-22a2-36d4-93d4-0c4c0ee36206 | -9.44431 | -60.55614 | 2025-08-31 05:44:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| c5e99d29-3e58-3c3c-8869-bebe7e4af7ae | -9.44 | -60.54515 | 2025-08-31 05:44:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 63d2345e-0b23-3f67-ac70-927e7e5a3e7e | -9.46145 | -62.33747 | 2025-08-31 05:44:00 | NOAA-21 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 105c4e08-7822-3783-b920-658d02b4a509 | -8.67976 | -66.93215 | 2025-08-31 05:44:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 16f2b9bf-adb1-377d-8e1c-d9f016932634 | -9.44067 | -60.55162 | 2025-08-31 05:44:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 4604c6a4-c6e5-394b-b716-3ce7ec5d3ed5 | -9.4417 | -60.57521 | 2025-08-31 05:44:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 6.1 |
| a4ceba16-9c49-3fdd-a40c-861fa7bb2243 | -8.6489 | -62.82652 | 2025-08-31 05:44:00 | NOAA-21 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 1e31c1ef-ded1-3b06-b098-dcc47ac0a7bf | -13.0285 | -56.9084 | 2025-08-31 05:44:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 9a38b053-c00e-3add-aa47-c6c114546583 | -13.02629 | -56.91 | 2025-08-31 05:44:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| b24a63bf-3507-3308-8984-6a02236e8365 | -9.70079 | -61.28331 | 2025-08-31 05:44:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 9.6 |
| 79588350-4c35-3855-9c73-695d61d78112 | -10.30475 | -68.26199 | 2025-08-31 05:44:00 | NOAA-21 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 35bd51c4-f132-36aa-a271-2743c35fdeae | -12.62884 | -57.00725 | 2025-08-31 05:44:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 19f9c9ef-5c0d-3805-b922-b4ac1e241095 | -9.57528 | -66.69097 | 2025-08-31 05:44:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| c0732946-d462-312b-9786-151165ea88c5 | -10.30816 | -68.26256 | 2025-08-31 05:44:00 | NOAA-21 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 1f23e8f3-65e6-35ac-97a9-590648871394 | -8.88164 | -62.38923 | 2025-08-31 05:44:00 | NOAA-21 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 55c8dc36-c3cb-3e85-a62a-5ea257be9b93 | -9.46893 | -60.3117 | 2025-08-31 05:44:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| f993f39a-17df-3869-8ddc-18ca3b7a0b9c | -7.91307 | -63.00321 | 2025-08-31 05:44:00 | NOAA-21 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 02842c59-54eb-3961-8ec1-46cc47c9ba64 | -10.72117 | -65.04848 | 2025-08-31 05:44:00 | NOAA-21 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 6a4bbdbd-5ec6-3b98-a030-7952ef491f52 | -9.43805 | -60.57082 | 2025-08-31 05:44:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 6.1 |
| bb90e336-0383-31f6-a827-9284772f7783 | -9.06355 | -71.2584 | 2025-08-31 05:44:00 | NOAA-21 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 84054896-2c7e-362a-b872-ec866a0762f0 | -13.01445 | -56.88288 | 2025-08-31 05:44:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 2b4026e8-2495-3b3a-8c43-a81e490ead1e | -8.55157 | -63.01427 | 2025-08-31 05:44:00 | NOAA-21 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 531bada7-5476-3f3e-a0e2-7b9c022a2d52 | -13.01503 | -56.90873 | 2025-08-31 05:44:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a9c3a47a-bb68-3508-b45d-fe1d8171bc17 | -9.56535 | -66.68938 | 2025-08-31 05:44:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 56cc947e-8468-3269-8367-c187d7ccda66 | -9.07015 | -65.41786 | 2025-08-31 05:44:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 770b3002-f778-3438-9663-ecbcf793738e | -12.61085 | -57.01639 | 2025-08-31 05:44:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| bc080dbf-c5a2-3030-9e11-515d6f9d5ac5 | -7.94078 | -63.50048 | 2025-08-31 05:44:00 | NOAA-21 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 7d04bead-263f-38ee-b4d0-06653fb207b4 | -8.85144 | -70.6263 | 2025-08-31 05:44:00 | NOAA-21 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 1.8 |
| e17d2870-bc11-3bf5-ad07-2a1969aa781a | -11.32537 | -63.26859 | 2025-08-31 05:44:00 | NOAA-21 | SÃO MIGUEL DO GUAPORÉ | RONDÔNIA | Brasil | 1100320 | 11 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 6085d547-f4b3-39ae-b6a7-f4c823c7ffa2 | -8.38833 | -70.83249 | 2025-08-31 05:44:00 | NOAA-21 | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a5b7ffd8-f370-3e6b-9a29-0c89e7f49798 | -8.66393 | -62.82452 | 2025-08-31 05:44:00 | NOAA-21 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 12400935-794a-36f6-840b-87884f333d56 | -8.56523 | -63.02053 | 2025-08-31 05:44:00 | NOAA-21 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f0151e81-095f-3c5e-99b5-48b55ec68cfe | -9.44195 | -62.36676 | 2025-08-31 05:44:00 | NOAA-21 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| b16ff514-dbb1-3ac9-9b82-4604da518093 | -8.2374 | -73.33527 | 2025-08-31 05:44:00 | NOAA-21 | CRUZEIRO DO SUL | ACRE | Brasil | 1200203 | 12 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 310d556d-b73d-3d95-9d67-fa96095ad43b | -13.01815 | -56.88114 | 2025-08-31 05:44:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 5b20b9f3-eb06-3063-8b60-95941150244d | -8.23906 | -72.81043 | 2025-08-31 05:44:00 | NOAA-21 | PORTO WALTER | ACRE | Brasil | 1200393 | 12 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 66bdd04e-748c-305f-a1ee-55296953e3ce | -13.02764 | -56.89818 | 2025-08-31 05:44:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| c5174520-b92a-3d15-a958-1c80b9111468 | -8.83877 | -66.72295 | 2025-08-31 05:44:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 0feb0eb1-7fff-3eb8-a1d6-b5e4b597335b | -8.73785 | -62.3803 | 2025-08-31 05:44:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 2c548bdf-aaf3-3c57-8912-bdfb4f970b5c | -8.73661 | -62.38231 | 2025-08-31 05:44:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 79fe705f-9d5f-3af6-9754-514272d884f3 | -9.43093 | -62.3375 | 2025-08-31 05:44:00 | NOAA-21 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 1d090cdf-d195-3e52-8d87-f94b24ef2a2d | -15.23662 | -56.07558 | 2025-08-31 05:44:00 | NOAA-21 | CUIABÁ | MATO GROSSO | Brasil | 5103403 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| e62501a6-5a63-34c6-b746-518686f54c48 | -9.43402 | -62.34254 | 2025-08-31 05:44:00 | NOAA-21 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 4489dcfa-6465-3e4f-a153-20f3d19b47ab | -8.66066 | -70.03784 | 2025-08-31 05:44:00 | NOAA-21 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 1.3 |
| efe8d9e4-433c-3101-b22f-3ca9e39a7028 | -7.91956 | -63.00831 | 2025-08-31 05:44:00 | NOAA-21 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ac836da0-f634-3d9a-93bf-e49f3bff8b52 | -9.57197 | -66.69044 | 2025-08-31 05:44:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 2282ebb3-b966-357b-a29d-3ff082b7373a | -8.67643 | -66.93163 | 2025-08-31 05:44:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 14c99bc4-d539-3444-a33a-fb5bc1d1a546 | -8.74578 | -62.39725 | 2025-08-31 05:44:00 | NOAA-21 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 4a283db3-efb6-398f-90af-c1350b4ffa95 | -10.7549 | -59.82266 | 2025-08-31 05:44:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 2ee93144-a8ee-301e-a5a1-d77704d3a452 | -8.56346 | -63.00773 | 2025-08-31 05:44:00 | NOAA-21 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a8398f91-587d-3fa3-a62a-8a0d60a26493 | -9.45024 | -62.33585 | 2025-08-31 05:44:00 | NOAA-21 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |


[Clique aqui para ver as próximas entradas](README76.md)
