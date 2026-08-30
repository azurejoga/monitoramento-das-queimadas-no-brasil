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

## Dados Diários - Página 51

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| e0b45f4d-f6cf-34bd-9171-af7b0767b87d | -9.89617 | -60.26832 | 2026-08-30 05:18:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 1bbfe5c2-0868-354a-b9a9-a304b53688e9 | -11.21626 | -53.98861 | 2026-08-30 05:18:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 7499f4cc-279e-3d68-a9b6-bdbcf32131fa | -6.11344 | -57.82989 | 2026-08-30 05:18:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| fdb2bbb0-f1fe-3f8b-bb99-4e3a9617c907 | -11.16581 | -51.31755 | 2026-08-30 05:18:00 | NOAA-21 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 9248fdad-e25c-3016-9893-06ec430ab659 | -9.20746 | -60.85836 | 2026-08-30 05:18:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 77b0fd43-61a3-31e4-bd69-d91f3794fa0a | -8.55101 | -54.71611 | 2026-08-30 05:18:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| a71ef018-2bca-368a-9652-3fbcf75d8910 | -5.4888 | -57.1524 | 2026-08-30 05:18:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 721f598d-315d-33ee-9c7e-eb8fe8333d39 | -7.52104 | -55.32526 | 2026-08-30 05:18:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 12.4 |
| a40055ec-39c0-3fd3-b2f4-94f0cb1c62ce | -11.04415 | -57.21435 | 2026-08-30 05:18:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 56742314-27ba-33bc-8264-e4626ba5cc9b | -10.48103 | -59.61374 | 2026-08-30 05:18:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 3e16bd49-bfec-3274-96b4-04f8f1aac1f6 | -7.3122 | -60.60587 | 2026-08-30 05:18:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 6.8 |
| 202d8961-55cb-33d1-a63b-1d486a893ad8 | -9.1903 | -59.36604 | 2026-08-30 05:18:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 3a164727-8fcb-38f0-8419-f0e7269a3238 | -6.18593 | -57.75329 | 2026-08-30 05:18:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 9ca5e945-877f-3642-85fd-90038a85e358 | -8.24858 | -46.50845 | 2026-08-30 05:18:00 | NOAA-21 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| c46bb0da-8a7d-3425-961f-582d336f6496 | -6.15699 | -57.78535 | 2026-08-30 05:18:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| d0c12d44-c0ca-3a67-b10f-938e05597040 | -7.2999 | -60.59658 | 2026-08-30 05:18:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| ca75e487-0cca-3e9e-b878-b5acd6037449 | -9.15991 | -59.51823 | 2026-08-30 05:18:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 8a4dfb4b-9fae-38b8-a635-53b8356c4510 | -9.14644 | -59.62661 | 2026-08-30 05:18:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 07fdbadc-a8b7-34e7-8fbd-6876d53d34fb | -6.37508 | -55.22175 | 2026-08-30 05:18:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f3ed81ce-445f-3513-a1ae-076f4e9f41a9 | -8.60711 | -70.20681 | 2026-08-30 05:18:00 | NOAA-21 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 05e2ef18-da16-3233-8605-8b4863e6f62d | -5.99776 | -57.83052 | 2026-08-30 05:18:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 197aee15-ead3-37a8-b3d2-b72ebc2931b4 | -6.78676 | -55.67373 | 2026-08-30 05:18:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 5bdb652b-0800-3d98-a823-0a39448f12b2 | -8.91373 | -66.95797 | 2026-08-30 05:18:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 3.3 |
| eb42f750-7a38-3b5e-9bee-f0ee60609e35 | -9.38373 | -66.51246 | 2026-08-30 05:18:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 16c4ba8e-44af-3921-acab-e6820c4a0198 | -7.85231 | -72.2784 | 2026-08-30 05:18:00 | NOAA-21 | CRUZEIRO DO SUL | ACRE | Brasil | 1200203 | 12 | 33 | nan | nan | nan | Amazônia | 2.5 |
| ad3565b0-b46e-3e6c-9714-82088c3c7834 | -6.77332 | -60.01174 | 2026-08-30 05:18:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 20a4f984-2261-38f0-8dd5-0040309b35f6 | -9.03768 | -67.61649 | 2026-08-30 05:18:00 | NOAA-21 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 09ff010c-f20d-3c03-845a-bedc6e53afe5 | -11.16284 | -51.30801 | 2026-08-30 05:18:00 | NOAA-21 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 5.5 |
| c44aef9e-4eec-307d-a88f-5bf7332551eb | -9.94038 | -60.52681 | 2026-08-30 05:18:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 3.8 |
| aee23fbe-b1d0-308c-bf3b-413975ef882c | -10.7493 | -54.02591 | 2026-08-30 05:18:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| c13d12d8-e466-3630-8f7c-6b75176c9118 | -11.1591 | -50.58309 | 2026-08-30 05:18:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 9.5 |
| 8194364c-6c03-3597-a0d4-17c6f8131610 | -11.03702 | -57.21325 | 2026-08-30 05:18:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 8f7ea261-80f6-3be8-b7d3-177b971534d8 | -7.31164 | -60.60946 | 2026-08-30 05:18:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 6.8 |
| 1f29cc4d-714c-3f98-925d-5659f858e52f | -6.80269 | -59.45652 | 2026-08-30 05:18:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 7487b2b9-1d0c-3c95-8f20-a1d95e0ca909 | -9.22036 | -59.76304 | 2026-08-30 05:18:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 8e96b108-5b0f-328a-9cab-e446a8a84ee5 | -8.62568 | -54.6955 | 2026-08-30 05:18:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 724c5fe6-32dc-3cc6-96d0-b02d5d4a62a9 | -6.79043 | -55.67427 | 2026-08-30 05:18:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 96199c25-08f6-33b9-82ef-e64d9311d97f | -9.388 | -60.57822 | 2026-08-30 05:18:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 9f2169bf-1e20-386b-be57-45b2c4187f34 | -11.79412 | -51.03907 | 2026-08-30 05:18:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 35.3 |
| af45edd7-2834-3d2e-b0fb-f98f7e0e41f3 | -9.14893 | -61.09555 | 2026-08-30 05:18:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 0e08ab9a-dfa6-3b54-86c0-13d2d0c3bdf4 | -6.81662 | -58.97358 | 2026-08-30 05:18:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 39890ca4-0c20-38e6-b5ef-957630d39a35 | -6.69007 | -60.12832 | 2026-08-30 05:18:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 0ff3198f-79d3-3d8e-8cea-5655def98617 | -9.89154 | -60.27424 | 2026-08-30 05:18:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 13.2 |
| 68535c77-cf6f-3e5e-902d-f7b49fd1602d | -9.13768 | -61.10115 | 2026-08-30 05:18:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 108004d4-fbd3-34a8-881a-122ef40a8d1c | -6.85347 | -58.97925 | 2026-08-30 05:18:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 4fff184d-482b-3d69-8a12-5cca5e21d855 | -11.02096 | -51.40723 | 2026-08-30 05:18:00 | NOAA-21 | PORTO ALEGRE DO NORTE | MATO GROSSO | Brasil | 5106778 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 225453e1-a9e0-3137-aeeb-435b10fbb9c5 | -11.16322 | -51.30482 | 2026-08-30 05:18:00 | NOAA-21 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 5.5 |
| e0e57c8f-7419-3bd4-9664-1d21450bf2f2 | -6.15645 | -57.78892 | 2026-08-30 05:18:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 8ca530fb-9c40-3455-970c-034a104686b3 | -6.81682 | -51.1537 | 2026-08-30 05:18:00 | NOAA-21 | TUCUMÃ | PARÁ | Brasil | 1508084 | 15 | 33 | nan | nan | nan | Amazônia | 11.0 |
| 9096400d-821e-3054-9fc7-cbc21081e816 | -9.79108 | -59.43628 | 2026-08-30 05:18:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 952d6132-ac30-3307-ba21-0c4be82a05f4 | -9.67411 | -55.06779 | 2026-08-30 05:18:00 | NOAA-21 | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 5.9 |
| b7b41dd3-ecda-3df8-b207-013afd46eb7f | -5.97214 | -57.68442 | 2026-08-30 05:18:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| bc281678-f788-3542-bea8-b41d94a01de8 | -9.16087 | -60.29305 | 2026-08-30 05:18:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 2cf4ddff-301c-3c1c-a602-f0ebb60fa6af | -9.91015 | -60.15551 | 2026-08-30 05:18:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| f3c68ec0-8cd1-35e7-899c-0e8a97acbde8 | -8.79969 | -62.48493 | 2026-08-30 05:18:00 | NOAA-21 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 955f9de3-9994-319f-91b1-67ffbb4afc58 | -6.78526 | -55.68035 | 2026-08-30 05:18:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| e88dcb6c-30da-3979-b181-27a1b4100010 | -9.05064 | -65.41635 | 2026-08-30 05:18:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 583efa08-d4b1-3ae0-ab24-f7235413a5c7 | -8.63179 | -66.5527 | 2026-08-30 05:18:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 0ef26dfb-c0cf-3a36-ba62-61bbe557ec73 | -6.1598 | -57.78943 | 2026-08-30 05:18:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 39342fe3-cb10-30d4-88e4-faf00c096658 | -8.93013 | -67.36233 | 2026-08-30 05:18:00 | NOAA-21 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 14.9 |
| eea03f51-a00e-30f9-9aac-018235d3359b | -9.41721 | -51.68355 | 2026-08-30 05:18:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 6959fc44-8b62-3ee3-8b07-3009d59bc1fa | -7.48787 | -55.3138 | 2026-08-30 05:18:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 148b76e4-b007-3f80-987b-ffde43d284ee | -10.74577 | -50.66235 | 2026-08-30 05:18:00 | NOAA-21 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 3.3 |
| df6fb20b-bc5c-3fc2-86e3-3afa3e05075f | -9.19361 | -59.36656 | 2026-08-30 05:18:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| eae30de0-88a8-3e89-b7af-60108b97bbb2 | -6.95277 | -55.71288 | 2026-08-30 05:18:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 84afdb38-7621-3fb6-a47b-0a63bf83c025 | -9.1523 | -61.09609 | 2026-08-30 05:18:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 16afff4d-3734-3855-946f-5463f164a78b | -6.82503 | -59.5736 | 2026-08-30 05:18:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| cc033b7a-b0c7-3464-b39a-18f31b3a645f | -5.88187 | -57.76521 | 2026-08-30 05:18:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 7.3 |
| 8cd1fd27-a1a5-33be-ab71-c1b69651b94e | -11.19776 | -53.99461 | 2026-08-30 05:18:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 1d2cc8f3-982c-3c7b-9d52-2055743589ac | -9.09022 | -65.48753 | 2026-08-30 05:18:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 9f0bee42-d7ae-3dc7-837c-8e2d02f4f948 | -10.75715 | -54.06482 | 2026-08-30 05:18:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| b6644c10-8bab-3b2a-9593-ef2d0e054f1c | -5.4854 | -57.15189 | 2026-08-30 05:18:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 345c405b-2d82-3112-adf9-4e447a3f6d64 | -8.91463 | -66.95294 | 2026-08-30 05:18:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 8ca471ab-9226-31ce-8676-fafd3b765441 | -6.77169 | -55.64903 | 2026-08-30 05:18:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| c9cec413-fd8c-3bd8-8584-0cefb5e21e3e | -9.12605 | -50.58641 | 2026-08-30 05:18:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 7970d858-74e1-3e90-9745-de50c11a77f6 | -8.60635 | -70.20972 | 2026-08-30 05:18:00 | NOAA-21 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 6ae8b114-abdb-3449-a9a7-782cc1a05061 | -9.9354 | -60.51521 | 2026-08-30 05:18:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 56b7b222-bde4-3bc6-b162-5a69fa97bdc3 | -7.05516 | -55.67724 | 2026-08-30 05:18:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| bbb8463f-b314-3b52-b8fb-e87c92f6aa71 | -9.89045 | -60.28123 | 2026-08-30 05:18:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| b550774a-0fee-34be-a1a8-a948e164aba5 | -6.68165 | -58.7499 | 2026-08-30 05:18:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 5fc20590-7c3a-39f6-8a62-05c9d921fbbd | -6.69341 | -60.12885 | 2026-08-30 05:18:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 6dcc7a69-799a-3f65-a569-1c30be4bf596 | -6.37441 | -55.22629 | 2026-08-30 05:18:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 9aeae570-a712-3415-8049-2a04e5908992 | -7.56167 | -61.31178 | 2026-08-30 05:18:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 3.8 |
| bf920e4f-5eeb-3c45-b388-28368e442050 | -9.71192 | -60.72471 | 2026-08-30 05:18:00 | NOAA-21 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 3.7 |
| ec79068f-17d9-35aa-b033-e1b7f4c84463 | -10.48928 | -59.60429 | 2026-08-30 05:18:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 8dd2b25b-cff1-37d0-91aa-d9899bd95cff | -6.02955 | -58.04136 | 2026-08-30 05:18:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 02e99f0e-7f53-3e3e-adfc-69948fdb4b64 | -8.97503 | -50.80205 | 2026-08-30 05:18:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 03dac60d-ba01-3ace-90cc-f88eaf4656a5 | -6.93548 | -58.95302 | 2026-08-30 05:18:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 76c49b2b-6463-3d9a-b1f2-ae7d37d1d7ea | -9.017 | -65.40624 | 2026-08-30 05:18:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 8ab9e046-180c-3700-aeed-0e2255371264 | -6.49738 | -53.25873 | 2026-08-30 05:18:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| fafabe1b-665f-38c4-8544-3320063d42cc | -6.1237 | -57.69648 | 2026-08-30 05:18:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 15d887b3-f65d-38f2-a7fc-6bbda4345775 | -10.4446 | -59.60802 | 2026-08-30 05:18:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 20b2f17e-4447-3fe9-92cd-724785de6e94 | -9.1643 | -59.5118 | 2026-08-30 05:18:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 0285b30d-678b-3b76-b8ff-da4164e18f58 | -11.24312 | -53.99857 | 2026-08-30 05:18:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 60b2ec9d-f4eb-30be-b18d-a5444ec2a576 | -8.25846 | -62.75708 | 2026-08-30 05:18:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 6.3 |
| d18418e9-fecd-34f9-9817-2359e84cb744 | -7.29712 | -60.59245 | 2026-08-30 05:18:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 901d29b1-7fc1-3269-bf2f-9d701e4a5d02 | -10.81504 | -50.50656 | 2026-08-30 05:18:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| ed7da510-eef9-39d0-875d-6a0543560c33 | -9.88271 | -60.26566 | 2026-08-30 05:18:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| ce552107-3824-3d95-b4c6-1621bd932c4f | -10.75136 | -54.04304 | 2026-08-30 05:18:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| bd545af0-17da-3e79-a882-d2db9c48df2b | -6.76611 | -60.01421 | 2026-08-30 05:18:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |


[Clique aqui para ver as próximas entradas](README52.md)
