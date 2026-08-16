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
| eeb9629f-1e7b-35a1-bdc0-2e852acd598d | -8.60091 | -54.6825 | 2026-08-16 05:16:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 97ac6689-710c-3428-9a57-d7ac1e6289d9 | -6.97189 | -59.01118 | 2026-08-16 05:16:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.9 |
| cf29be11-a786-3c8d-a09f-b0d10a0afef0 | -6.58776 | -58.98889 | 2026-08-16 05:16:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 07ee2105-c976-3797-9dee-34dbe2d344c2 | -8.89684 | -60.5889 | 2026-08-16 05:16:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.9 |
| fc7b0e22-7abd-341f-82f2-e3dddbb52dc0 | -9.39868 | -60.36283 | 2026-08-16 05:16:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 2140eed7-f2e1-3485-97ee-7cdc643af4f8 | -6.61137 | -58.98001 | 2026-08-16 05:16:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 27d36fcf-7acf-382d-947e-228d5e934e7c | -3.11788 | -59.92895 | 2026-08-16 05:16:00 | NPP-375D | MANAUS | AMAZONAS | Brasil | 1302603 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| ff4112a9-9396-39f8-9f8a-091c97e7aa1f | -8.97372 | -60.51846 | 2026-08-16 05:16:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 6.6 |
| 1704cbf0-4078-3abe-aac9-6957eb4fc077 | -9.29826 | -56.81634 | 2026-08-16 05:16:00 | NPP-375D | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| e7a11713-135b-3fa4-8b8c-8dbb21965271 | -9.19439 | -60.28973 | 2026-08-16 05:16:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 473a63a1-b733-39f5-9f07-8334259482b3 | -9.20895 | -59.67238 | 2026-08-16 05:16:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 27b48c06-ed0e-3c45-b431-769d127cb592 | -6.71165 | -58.94069 | 2026-08-16 05:16:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 5.6 |
| e5728079-fb34-3fd2-8d22-f61e042672ee | -6.97839 | -59.01647 | 2026-08-16 05:16:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.3 |
| f6d2a452-fe90-37b4-bead-ee1ff7be292f | -7.42573 | -60.01801 | 2026-08-16 05:16:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 4838843d-3961-3e2d-b695-b85c996dd8e8 | -8.42972 | -62.67581 | 2026-08-16 05:16:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 09b56fbd-2ebc-336a-bee4-95542666c3ba | -8.96759 | -60.53175 | 2026-08-16 05:16:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 8.7 |
| 43d89fec-2952-3752-a2b3-2c8ee8399811 | -11.50868 | -54.63388 | 2026-08-16 05:16:00 | NPP-375D | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 53b932fe-8451-362f-ae0b-1ae02519046b | -12.03702 | -46.44082 | 2026-08-16 05:16:00 | NPP-375D | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 0a9b4870-69cc-325a-bfc1-643330602d13 | -8.61 | -54.71417 | 2026-08-16 05:16:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 8265d7f9-6dad-3c6c-989c-3ce072cd244b | -7.4077 | -60.01036 | 2026-08-16 05:16:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| e365a297-84d0-3ef9-8d79-e89ed0ee4aeb | -11.45352 | -46.613 | 2026-08-16 05:16:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| e106224e-3d8f-30d0-ab2a-fc97b830eafb | -8.95007 | -60.54315 | 2026-08-16 05:16:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 4.0 |
| b94d9c56-e732-3898-8493-d3afbf4ead5b | -6.69958 | -58.94691 | 2026-08-16 05:16:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 98e6a771-0501-3deb-b1dc-3c741a88bcab | -11.21772 | -54.81474 | 2026-08-16 05:16:00 | NPP-375D | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 79fd2242-3633-38e3-af4f-6eb3b9d49212 | -7.41673 | -60.00254 | 2026-08-16 05:16:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| aaf18449-51b9-3a17-8035-e081fa1302a7 | -8.89757 | -60.55334 | 2026-08-16 05:16:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 7.1 |
| af6fde76-329f-31ad-9997-74c7657c755b | -8.96837 | -60.5271 | 2026-08-16 05:16:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 16f5cd1e-33a8-3189-9ab5-c79878b5a150 | -8.60546 | -54.69832 | 2026-08-16 05:16:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 342e8aa0-7a23-32fd-8d87-992bb4b00784 | -7.3749 | -46.81277 | 2026-08-16 05:16:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 6a37530b-86ef-3a43-842b-b8fa1fc9e47a | -9.37089 | -57.36057 | 2026-08-16 05:16:00 | NPP-375D | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| cc93f599-a84b-343f-be0a-7e7141e8fccc | -6.71097 | -58.94477 | 2026-08-16 05:16:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 1d942265-c2a0-3c4d-9cf9-8c38f7823e56 | -8.97673 | -60.52374 | 2026-08-16 05:16:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 6.4 |
| c026d825-a2cb-3deb-8cb4-55698e8fe19d | -6.71232 | -58.93661 | 2026-08-16 05:16:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 8c6476e8-c4c4-3d4e-a150-c0acd72a8c1c | -10.15373 | -48.09056 | 2026-08-16 05:16:00 | NPP-375D | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| d0205c1b-a5cf-32b1-bab1-28ca739248bc | -9.42784 | -60.32644 | 2026-08-16 05:16:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 626c9193-b929-3195-9b7f-d5e5d4f20c50 | -6.63083 | -56.3953 | 2026-08-16 05:16:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| b793f70c-a6d0-36da-9c0e-d8ba2ae22d8a | -6.83036 | -56.45965 | 2026-08-16 05:16:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 5f2d5ddf-cafa-3820-adfc-9f80be90f790 | -7.11139 | -55.12959 | 2026-08-16 05:16:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 913ce3d4-e63c-325c-b0f5-1f836774588a | -6.28603 | -47.73025 | 2026-08-16 05:16:00 | NPP-375D | NAZARÉ | TOCANTINS | Brasil | 1714302 | 17 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 01be6d77-4d5f-3146-87f9-3dc000373dd9 | -6.71881 | -58.94188 | 2026-08-16 05:16:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| eb67c86a-76b9-39c3-8b55-ff74111cf0a8 | -7.4581 | -45.0946 | 2026-08-16 05:16:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 35dfb472-21b5-3369-8e6e-50ed79519422 | -10.07613 | -60.49551 | 2026-08-16 05:16:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 21639a05-258a-3d8c-af1e-efa9b46d7e71 | -6.599 | -59.12282 | 2026-08-16 05:16:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 34c55240-7816-3d6b-978a-40c58af718f8 | -6.60078 | -58.99946 | 2026-08-16 05:16:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a355c6ab-f160-3688-995c-3a362bffa1cf | -7.68977 | -55.15408 | 2026-08-16 05:16:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 4119fc84-6fa0-30a1-b405-1df48b838348 | -6.11267 | -57.71427 | 2026-08-16 05:16:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 090351d5-8283-3f6b-ad42-9eab1a8113f1 | -8.67219 | -54.76489 | 2026-08-16 05:16:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| e96cccdd-0eaf-3fc1-bdfe-94bb4abc5c2b | -8.41438 | -62.65998 | 2026-08-16 05:16:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.5 |
| d4eb1a1e-5014-3f7b-b3df-8c0e3dfca7ce | -8.65453 | -54.72065 | 2026-08-16 05:16:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 6843c02f-360e-3d97-9077-43f6b5f1304c | -8.95307 | -60.54845 | 2026-08-16 05:16:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 176e9913-f357-3fe3-ae0f-60718958723e | -7.34998 | -59.59349 | 2026-08-16 05:16:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 4.0 |
| fb9bc2e9-c013-373f-b360-652ff8f93872 | -8.89311 | -60.56424 | 2026-08-16 05:16:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 150a28ae-e8ef-3dd4-9adb-25d121761760 | -8.94993 | -60.56702 | 2026-08-16 05:16:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 9ca64c1e-1a8b-3a12-bbfe-a27d349145c3 | -9.19884 | -59.66632 | 2026-08-16 05:16:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e82b7f8c-cfb2-3347-b980-b4c086ff7c00 | -6.84033 | -56.43984 | 2026-08-16 05:16:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 80297774-ecb6-385a-b4d6-a2ab639d4bc0 | -8.43726 | -62.68429 | 2026-08-16 05:16:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 36.0 |
| ee03ce30-7266-3989-9e50-86afe47013a9 | -6.679 | -43.99057 | 2026-08-16 05:16:00 | NPP-375D | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 8.2 |
| 3ec7eb10-a760-3073-bb7b-f5ec69075aac | -8.60262 | -54.6941 | 2026-08-16 05:16:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| daf68788-7bc2-38ea-9d1e-de2253864881 | -6.55858 | -55.15881 | 2026-08-16 05:16:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| e8b91be8-f49a-37a8-9108-951895d9077b | -9.30213 | -56.81338 | 2026-08-16 05:16:00 | NPP-375D | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 07b762f2-4b19-3efa-a865-22c81b67d206 | -9.48937 | -51.64707 | 2026-08-16 05:16:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 17326c99-abae-3f70-8fb7-68750607bd36 | -8.5992 | -54.67089 | 2026-08-16 05:16:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ee7adc93-9d1d-374c-89bc-30cf9f88c1d3 | -11.48475 | -46.59737 | 2026-08-16 05:16:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 4d230173-4063-3472-937e-b376bb279f46 | -6.62794 | -59.05927 | 2026-08-16 05:16:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 3953755f-0521-3740-a51b-9ec7ae178ea1 | -8.26528 | -57.34894 | 2026-08-16 05:16:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 123ba4f2-9409-3a78-85d5-84ed7ddaf851 | -11.06997 | -47.27045 | 2026-08-16 05:16:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 3db36d83-abc1-3cf1-a729-1b610b6c2dcd | -10.27617 | -48.29183 | 2026-08-16 05:16:00 | NPP-375D | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 71988bac-ca49-37ed-8c7b-101565e0718b | -9.13153 | -66.97185 | 2026-08-16 05:16:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| f90f8609-0a91-36a3-9c31-ffdc2a440cdd | -6.54932 | -56.54297 | 2026-08-16 05:16:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| c41c388b-5d06-34e2-b6a9-fb47b8dfc597 | -5.25512 | -47.70628 | 2026-08-16 05:16:00 | NPP-375D | IMPERATRIZ | MARANHÃO | Brasil | 2105302 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| fbe323d4-9788-3cc5-9014-69df3676c4bb | -8.61514 | -54.68093 | 2026-08-16 05:16:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| b1acafa3-77ed-3069-9390-20296eabf67f | -6.62387 | -59.08423 | 2026-08-16 05:16:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.2 |
| df660572-854a-31e8-9847-fe0b22951785 | -6.97613 | -59.0077 | 2026-08-16 05:16:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 670548b7-f010-3805-8317-1904c052b2d8 | -8.94944 | -60.52387 | 2026-08-16 05:16:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 8.4 |
| 67252f15-3fe3-3e4f-8776-d6489ae40e4f | -6.96235 | -59.29789 | 2026-08-16 05:16:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 3f649e0f-2e13-38a6-910b-6a6b4c7cd4a7 | -6.54583 | -55.17476 | 2026-08-16 05:16:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 20ef29d4-b1e1-3312-b85f-371edadb9dab | -9.39874 | -65.96066 | 2026-08-16 05:16:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ce2091e1-f80a-3264-ad63-5c2359c121e7 | -8.65284 | -54.7317 | 2026-08-16 05:16:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b935bf43-c942-336d-975f-84267c761ed2 | -12.01129 | -46.42985 | 2026-08-16 05:16:00 | NPP-375D | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| a85a0b72-1955-3d00-a611-8850e040b69b | -9.13758 | -68.202 | 2026-08-16 05:16:00 | NPP-375D | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 7ebb122d-b65f-3e8e-a938-08a844040121 | -6.61496 | -58.9806 | 2026-08-16 05:16:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.9 |
| ccfd9028-0c9f-3ec9-8b61-98af3d1c3d91 | -9.30601 | -56.81042 | 2026-08-16 05:16:00 | NPP-375D | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 1f721e94-738a-3250-bd8d-62faf27ba0d1 | -6.86468 | -56.41523 | 2026-08-16 05:16:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 992ca867-d7d7-3761-b29d-a0695129fd3e | -8.95292 | -60.5724 | 2026-08-16 05:16:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 01bc5708-1b98-30e4-8475-389862596b3f | -6.63521 | -56.26073 | 2026-08-16 05:16:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 3ccebc87-46fe-3dee-8890-3a056caba91b | -6.83146 | -56.40993 | 2026-08-16 05:16:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| c00ec769-e718-3189-98b5-f54fb900e87b | -11.08431 | -47.24677 | 2026-08-16 05:16:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| def90f07-34fb-3e51-bafc-ef163a9fc08c | -8.97895 | -60.53368 | 2026-08-16 05:16:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 3c9e7375-429b-3584-9f0d-d23ce12082f0 | -6.62074 | -59.05806 | 2026-08-16 05:16:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 097c7600-fa6a-3af3-b5b2-c9383a191cf0 | -6.59855 | -58.99063 | 2026-08-16 05:16:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 041ec605-7245-36a2-b053-040fe59ee456 | -6.62726 | -59.06344 | 2026-08-16 05:16:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 4c5ff04a-18be-3507-a874-9f8359a50491 | -12.0286 | -46.43592 | 2026-08-16 05:16:00 | NPP-375D | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 56e7559d-3bba-3e19-9eab-731849d79402 | -6.81707 | -56.45754 | 2026-08-16 05:16:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| ec2c12b3-795b-338f-a136-ae57afe7981d | -11.08009 | -47.27935 | 2026-08-16 05:16:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| d00952b6-243a-3338-b4a5-54944ee1ddcb | -12.44881 | -46.65416 | 2026-08-16 05:16:00 | NPP-375D | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 4a2dc722-2541-308b-942b-e948f4ea0fef | -8.61456 | -54.68464 | 2026-08-16 05:16:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| e56a6203-9141-334d-a6a6-4b1429643d77 | -6.60094 | -56.36912 | 2026-08-16 05:16:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 1d14e41d-c308-3224-9947-a8654fd93a49 | -6.84859 | -59.10207 | 2026-08-16 05:16:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 50624994-75ff-3abe-8072-7298a1adedee | -6.83645 | -56.44279 | 2026-08-16 05:16:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 7f7aa48c-ad6a-3662-8c14-75637cc3b6c9 | -7.24165 | -49.87761 | 2026-08-16 05:16:00 | NPP-375D | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 7.7 |


[Clique aqui para ver as próximas entradas](README41.md)
