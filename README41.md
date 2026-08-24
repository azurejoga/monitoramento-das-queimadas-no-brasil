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

## Dados Diários - Página 41

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 39d65074-a25f-3f5d-881d-aab8ed5c5e7d | -6.79991 | -59.42758 | 2026-08-24 05:29:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| e3e0731f-63c1-3358-a225-4a8fd5f0d59b | -6.68626 | -58.7244 | 2026-08-24 05:29:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 3a87fc2d-7bab-33dd-8e7c-5ea8a304f0d0 | -4.96663 | -56.2715 | 2026-08-24 05:29:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 5ab32b68-633f-308a-b447-c1a3f81217ec | -7.77823 | -61.10401 | 2026-08-24 05:29:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| a113aa0e-1f32-39ee-98c3-231639ed61e8 | -6.12523 | -57.74815 | 2026-08-24 05:29:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 775ea77d-145d-376b-aae0-857b36586f1b | -6.67633 | -58.74081 | 2026-08-24 05:29:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 20dc0382-c0c3-3e38-948a-cc87d394732f | -7.71714 | -61.10905 | 2026-08-24 05:29:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 3bdd3534-d311-3eb4-a575-1ce785956f50 | -6.80703 | -58.66484 | 2026-08-24 05:29:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 7d2319f6-7b25-39ca-9809-a648f0ebb81f | -7.67443 | -63.32871 | 2026-08-24 05:29:00 | NOAA-21 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| ef096f54-bdf0-36d9-93ba-36f5ff26a22a | -6.96775 | -59.07388 | 2026-08-24 05:29:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| aa88aa31-1606-31c5-80b3-7ff21be6a154 | -6.83841 | -52.49829 | 2026-08-24 05:29:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| fda7353b-5376-377d-adc5-49825485bc54 | -6.80207 | -59.58411 | 2026-08-24 05:29:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| dd68da32-bae8-3f57-9f1e-13cc9f6b311d | -6.17415 | -55.44495 | 2026-08-24 05:29:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| eceb31f3-e9a7-3319-a423-7e470e5a0140 | -7.77094 | -61.10658 | 2026-08-24 05:29:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| efcc3dbd-ef8a-3970-a2fe-c3bb9299a0a0 | -5.88375 | -52.10809 | 2026-08-24 05:29:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 0ca445b8-9e5d-3b1d-b944-f3da0fd3555e | -6.94866 | -59.07276 | 2026-08-24 05:29:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e591dcda-772d-3435-b8a1-c20ed3129eaf | -6.21691 | -55.92314 | 2026-08-24 05:29:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| c6e8ad7e-a32f-3c53-a2d3-a2699b6b89d9 | -6.96961 | -59.06121 | 2026-08-24 05:29:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 475faafa-f6c3-36e9-b7bf-9712ca445242 | -6.79574 | -59.4311 | 2026-08-24 05:29:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 8a52ac5f-5d6c-3dd2-93bd-d4482604a13d | -6.14171 | -57.7706 | 2026-08-24 05:29:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 6d227188-cc05-3035-b88f-081889c86189 | -6.77653 | -59.4421 | 2026-08-24 05:29:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 6c52c515-aaf3-35ad-9258-833ab7a0a64e | -8.05369 | -61.5926 | 2026-08-24 05:29:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| d9731c24-8bb3-3230-bb6c-6ebd02324d5f | -6.80397 | -58.65982 | 2026-08-24 05:29:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b4ce73c4-f184-3b1e-8d51-073ac5781aa3 | -8.5432 | -55.28601 | 2026-08-24 05:29:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 919f4650-f2de-3c94-b9ea-3c80ea6e9dc2 | -6.67072 | -58.73329 | 2026-08-24 05:29:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 1867e369-d98f-3b88-8b63-903272a2b547 | -6.81639 | -58.65266 | 2026-08-24 05:29:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| bca33b20-0ffb-339d-a433-58800d6f256a | -7.25643 | -60.61437 | 2026-08-24 05:29:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| ca5967f7-95f6-35b1-b893-f63693612eb2 | -6.15024 | -57.94067 | 2026-08-24 05:29:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 1ba2e68c-5e5d-3b31-ab9d-b03b9cd8afb8 | -7.24931 | -49.87791 | 2026-08-24 05:29:00 | NOAA-21 | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |
| c07a34f5-bb03-3086-8d60-e0457c245b62 | -9.05233 | -50.7746 | 2026-08-24 05:29:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 34fe3b69-7ab2-303a-b439-3a169797b8f2 | -4.46829 | -55.66322 | 2026-08-24 05:29:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| a08057b6-32a3-3ab6-adc8-5d057ff8dc62 | -6.8056 | -59.58465 | 2026-08-24 05:29:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 5ee596cb-eb22-349f-8da6-cfdc13ca988c | -8.57917 | -55.27783 | 2026-08-24 05:29:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 00863004-948c-324d-b264-61868830b6d2 | -7.67886 | -63.32221 | 2026-08-24 05:29:00 | NOAA-21 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 110c6b2d-7d5c-3e9e-9230-d60f0e9b18f7 | -6.6118 | -58.38041 | 2026-08-24 05:29:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 837d9af3-e3cc-3810-9e4e-15f415596a72 | -7.76474 | -61.10193 | 2026-08-24 05:29:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| ffb1ae8e-4d62-3a45-903d-39b7d5a4ecf9 | -5.79201 | -57.56146 | 2026-08-24 05:29:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| c8212c72-98aa-3ef1-8099-d28f5f6a8d2d | -6.19476 | -53.52692 | 2026-08-24 05:29:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 93e4264e-5eda-3284-9494-31c4b719452b | -6.94773 | -59.08379 | 2026-08-24 05:29:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 8e5f3580-72d8-344b-b0e9-863ddfbed2ec | -5.87168 | -57.5631 | 2026-08-24 05:29:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 29e30334-6f93-3863-aedd-c243d9d02d48 | -5.86786 | -57.56417 | 2026-08-24 05:29:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| d21bf1f7-59fa-39aa-833d-4eb57ade5ac4 | -5.85827 | -57.5459 | 2026-08-24 05:29:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 432b5047-9573-317d-b643-2f7f99faa252 | -7.77486 | -61.10349 | 2026-08-24 05:29:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 6f4d6a58-33e9-3217-a7af-908a1d3b93af | -6.35117 | -55.86206 | 2026-08-24 05:29:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 87d18a8c-e291-3cb2-b58c-f5750cb94a43 | -8.54865 | -55.28159 | 2026-08-24 05:29:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| b62315af-0a6d-34bc-86c8-8edac3007fc3 | -6.22898 | -55.61966 | 2026-08-24 05:29:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 13.7 |
| 0c6d97dc-4ea7-311d-9123-1184987bffb2 | -6.97139 | -59.07444 | 2026-08-24 05:29:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 2c91ba42-2f79-3f0b-abf8-de51737807b2 | -6.81073 | -58.66544 | 2026-08-24 05:29:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 86b8cdc6-74a3-3f12-bd67-36201e9a14f7 | -5.57571 | -55.81719 | 2026-08-24 05:29:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 60db5d82-9560-3c67-ad3a-3955b56ebf57 | -6.80087 | -59.59211 | 2026-08-24 05:29:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 44a6ef01-af57-31ea-a180-7f2d8e6f8863 | -7.49227 | -55.34227 | 2026-08-24 05:29:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 3f6375b0-ea1b-36f7-bb93-3abd8e44873a | -8.57784 | -55.28041 | 2026-08-24 05:29:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| e8e4b5f2-8b87-39d9-8a35-e40b2bb19253 | -7.25031 | -49.87032 | 2026-08-24 05:29:00 | NOAA-21 | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 0e7e1f70-5809-3151-adae-0dc4a36d98ad | -6.80026 | -58.65925 | 2026-08-24 05:29:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b4cfdb45-4d60-33f9-9070-2715ce0b851c | -6.74011 | -59.65752 | 2026-08-24 05:29:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 75f77c04-2793-346d-b5f6-8cb65cc862ca | -7.2513 | -49.86282 | 2026-08-24 05:29:00 | NOAA-21 | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 211a6dc4-07bb-3a4b-a241-5131fd2a26ac | -4.99502 | -56.13992 | 2026-08-24 05:29:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 8eb6989b-5d54-39f0-928b-20cd9d6d12bf | -5.32611 | -55.8577 | 2026-08-24 05:29:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| bf27da5d-f93d-3c0e-8e57-cc1f4c5b991f | -7.79243 | -56.28727 | 2026-08-24 05:29:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 9e2d7d6f-6da0-34c3-a2a9-fe30fca117e3 | -6.82432 | -59.41045 | 2026-08-24 05:29:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| dac65a87-aada-3bff-98d5-f3dfde5f0603 | -6.79278 | -59.42647 | 2026-08-24 05:29:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 04d83983-2af3-3af9-b030-2bb89688da77 | -7.6772 | -63.33274 | 2026-08-24 05:29:00 | NOAA-21 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| c8a8f082-077d-368e-a66a-d72033f76b17 | -6.94533 | -59.07481 | 2026-08-24 05:29:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 899647d3-0e9f-3c24-9778-f6a3b0d8f3f8 | -6.25826 | -55.41706 | 2026-08-24 05:29:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| d1744415-5a23-3dc6-80b1-0fd7803ad35a | -6.34776 | -54.75972 | 2026-08-24 05:29:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| c626992a-9e39-3c8b-9f5c-b58c92f889e4 | -7.44266 | -59.77693 | 2026-08-24 05:29:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 82fd8ee0-323b-3bb2-85a6-85a766ce3a1f | -7.49127 | -55.33853 | 2026-08-24 05:29:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 1a86ce96-db8f-333b-9244-ca68735a3af1 | -6.79985 | -59.81432 | 2026-08-24 05:29:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 1d734566-d580-3b81-a260-19765a7ec1e7 | -5.78419 | -57.56033 | 2026-08-24 05:29:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 69411782-ac08-3f80-99c7-7575b1f8f7f8 | -6.12461 | -57.83222 | 2026-08-24 05:29:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 260cc8e9-b761-3fb5-9ac4-4418c4627bee | -7.68108 | -63.32976 | 2026-08-24 05:29:00 | NOAA-21 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 5.7 |
| e6e6db5d-ff57-386e-8cce-953e22501f91 | -6.18916 | -53.52927 | 2026-08-24 05:29:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 765f54a4-2f4d-39be-bd44-ec174705d9d7 | -9.05385 | -50.77425 | 2026-08-24 05:29:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 9e993b36-d61d-3f25-9e98-0f24c4c24265 | -6.78133 | -59.43449 | 2026-08-24 05:29:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 2879b9b0-7d38-3484-90e5-c4a3024912eb | -6.86896 | -59.40477 | 2026-08-24 05:29:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f1f0856b-f54e-353a-bae9-4877faa59620 | -6.9417 | -59.07424 | 2026-08-24 05:29:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| c181e307-6917-3229-b33f-28d5d4276034 | -6.61222 | -58.38258 | 2026-08-24 05:29:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| fb0485de-1f40-330f-bb02-47f4132a8121 | -7.77596 | -61.09626 | 2026-08-24 05:29:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 1411f971-6b82-39ab-9395-27bcd66803e8 | -5.78738 | -57.56585 | 2026-08-24 05:29:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 0b3f37ea-2f43-3614-be53-0ec548da5899 | -6.34053 | -55.87374 | 2026-08-24 05:29:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| cb3f952b-7b07-3a34-b311-02d2b8690420 | -6.18399 | -53.5285 | 2026-08-24 05:29:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| cd3421fb-5e2f-3f28-a234-54c70573a13d | -7.43913 | -59.77639 | 2026-08-24 05:29:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 4c248a4f-ba33-3b14-b4f8-dbc0dc610124 | -6.71837 | -59.44154 | 2026-08-24 05:29:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 221d66a3-1126-3d5b-90a1-d0c9528c8725 | -6.86835 | -59.40886 | 2026-08-24 05:29:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 67480760-6e08-3b61-b330-6597e265757f | -6.61532 | -58.38771 | 2026-08-24 05:29:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 89fb0071-e5ad-33e5-b533-2f85a71dad18 | -4.61374 | -55.74048 | 2026-08-24 05:29:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ef1d6e2d-d3d1-3911-a704-92f89cd5719b | -6.33825 | -54.75827 | 2026-08-24 05:29:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| d2392669-3794-3e40-ba72-16ecc625959d | -6.70102 | -58.72668 | 2026-08-24 05:29:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 4b7561b1-22d3-3ee9-9833-2936d23594c2 | -6.76897 | -59.73334 | 2026-08-24 05:29:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 74fef19c-8495-305c-a32e-a6c2cc352a63 | -7.49298 | -55.33731 | 2026-08-24 05:29:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 1aafab9a-892c-3420-a1e1-c76a726ec8cd | -6.83228 | -52.50154 | 2026-08-24 05:29:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 350bc862-a34e-34b3-b6e3-2b1e9b64e514 | -5.0125 | -56.13681 | 2026-08-24 05:29:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 4e50efbd-8601-33a7-b8e7-ac8249b8b0f4 | -7.30391 | -60.71894 | 2026-08-24 05:29:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 523c32ce-dcbf-3498-8767-f36581b93563 | -6.1434 | -57.94277 | 2026-08-24 05:29:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| a74f10c6-0ab7-3cc0-8f26-75ea294a6ab9 | -6.77235 | -59.44566 | 2026-08-24 05:29:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 9caf0513-ec1f-341c-a528-51d4e9636d7b | -5.79129 | -57.56639 | 2026-08-24 05:29:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f299ab6b-f8e6-388f-871a-8ae10e616777 | -7.25519 | -49.86832 | 2026-08-24 05:29:00 | NOAA-21 | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 7.5 |
| a5f09675-6dc7-3e53-868b-464edaf7f107 | -6.85702 | -59.41133 | 2026-08-24 05:29:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 51574510-287f-3cad-a990-14a3a641caac | -6.82075 | -58.64877 | 2026-08-24 05:29:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 9028dd67-9f78-3199-bd0e-7bf2f37bc579 | -7.68773 | -63.33081 | 2026-08-24 05:29:00 | NOAA-21 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 11.2 |


[Clique aqui para ver as próximas entradas](README42.md)
