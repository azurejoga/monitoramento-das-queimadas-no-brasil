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

## Dados Diários - Página 55

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 07624c26-2d0e-399e-95da-a3d6381240e5 | -6.91642 | -59.14989 | 2025-08-15 05:42:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| f109c0a0-9d53-3e6d-a333-50041195c470 | -7.24269 | -60.0023 | 2025-08-15 05:42:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| ab398b2b-c111-3308-8940-790f16e12cd9 | -6.89808 | -59.15164 | 2025-08-15 05:42:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 13e54e3c-fe66-3621-acb7-cc868c2e3187 | -6.94625 | -59.99572 | 2025-08-15 05:42:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| c9dc8850-fda0-3d18-bbf1-b6d79956f2ec | -7.13026 | -59.64105 | 2025-08-15 05:42:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 45cb3d2f-aead-33d9-b468-e7bd60c039c6 | -6.88036 | -59.14908 | 2025-08-15 05:42:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| f485b946-0fe9-3ecd-ac92-71d17b4c8b16 | -6.94882 | -60.00777 | 2025-08-15 05:42:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 5.5 |
| fe7a265f-0227-361f-bac1-0d16b5bc1824 | -6.66912 | -58.82381 | 2025-08-15 05:42:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 5947f33a-c40e-3ae1-9ce0-9df22e1c2fdc | -6.48596 | -62.94226 | 2025-08-15 05:42:00 | NOAA-21 | TAPAUÁ | AMAZONAS | Brasil | 1304104 | 13 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 0b0a72b3-05a6-3752-82d0-f6ff2c4b4014 | -6.78995 | -58.78583 | 2025-08-15 05:42:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 4e3f3302-e3a2-34b0-8629-8847ad19fac0 | -7.29332 | -60.6276 | 2025-08-15 05:42:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| c160c5a8-02f2-3786-8028-57d2dd86b446 | -5.45797 | -60.14204 | 2025-08-15 05:42:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 165f225c-9806-3110-acd2-3d97130b62c7 | -5.75169 | -59.87464 | 2025-08-15 05:42:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.8 |
| ab5b62b2-cc13-3d65-a98f-73b2a65213ec | -6.90881 | -59.13981 | 2025-08-15 05:42:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 4af96f7b-375d-313f-abfe-5d88eb63b669 | -6.8816 | -59.14029 | 2025-08-15 05:42:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 59e74e15-1f8f-33f2-a711-49ffa0370381 | -5.44686 | -60.13304 | 2025-08-15 05:42:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 4.7 |
| bbf18131-b4df-3789-b4b7-d7caee302b3b | -6.69493 | -58.83698 | 2025-08-15 05:42:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 964d916b-0732-3e03-9ea6-2f6e7f4277cb | -5.92239 | -59.92583 | 2025-08-15 05:42:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 42ab9ab3-34d4-3de4-bc52-6281a9e4591d | -7.12395 | -59.62355 | 2025-08-15 05:42:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 4300bea4-2167-3538-af77-8ef57b851503 | -7.14922 | -59.63118 | 2025-08-15 05:42:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| d52db3ec-40f9-3276-bacc-ccd87c1cd21e | -6.93032 | -59.14758 | 2025-08-15 05:42:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 43c63668-8c15-3e1d-9e17-abe19a1b572c | -6.90119 | -59.12981 | 2025-08-15 05:42:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| dadc3115-db70-3e99-ae03-31fc8d0bff06 | -5.92956 | -59.93464 | 2025-08-15 05:42:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 1a8e1dae-f374-3d7b-91d0-68938909f5ec | -6.7104 | -58.82519 | 2025-08-15 05:42:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 31787709-a62c-359e-b5e8-a9483e487b2b | -6.9448 | -59.82219 | 2025-08-15 05:42:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 1663be94-ee18-3448-8fe2-a6c3bcd56bda | -6.65885 | -58.81935 | 2025-08-15 05:42:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 10.2 |
| b897a9af-066b-3afd-8b98-93f1a61be0ff | -6.67364 | -58.82449 | 2025-08-15 05:42:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| f2b7331f-fd8e-340f-b016-a8c39ce50d6e | -7.14574 | -59.6556 | 2025-08-15 05:42:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c4e15dc1-7b17-3f99-a99e-d148faebc972 | -6.71621 | -58.81667 | 2025-08-15 05:42:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 4.2 |
| f34a21f0-cd0f-384f-9e50-b5c52fb36a42 | -7.31624 | -59.61753 | 2025-08-15 05:42:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.2 |
| 178a3aa0-dc04-33f2-acde-be1ed1501c43 | -6.90819 | -59.14417 | 2025-08-15 05:42:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 97f5810f-f11f-3526-aa88-c9e5aa0a32a4 | -7.09044 | -59.22122 | 2025-08-15 05:42:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 4.4 |
| e20a6ad6-b243-3329-beb7-8e6a233654ed | -6.90944 | -59.13545 | 2025-08-15 05:42:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| b1c970f0-a11e-3991-9c28-6588946fdf32 | -6.72329 | -58.83181 | 2025-08-15 05:42:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 9847188b-bbdd-3b03-9c80-216bf8e5ea0c | -6.90197 | -59.6358 | 2025-08-15 05:42:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| b2e43ae1-5552-3f55-a326-d545413e4416 | -6.91829 | -59.13684 | 2025-08-15 05:42:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| d0a1b51f-5fff-3229-8656-0edcd01a55bf | -7.15294 | -59.63585 | 2025-08-15 05:42:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 29646cbb-1b5e-3506-88b1-982b4a6dcda3 | -5.44581 | -60.14019 | 2025-08-15 05:42:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 4.7 |
| e95f97f3-31fc-3fff-bf31-8f3d58c93f35 | -7.31499 | -60.62011 | 2025-08-15 05:42:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d6b23cdd-86fe-3298-b08c-7b4877d1795f | -6.6962 | -58.82787 | 2025-08-15 05:42:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 7.3 |
| 6ddc82f6-98e6-30a7-bc1b-377cdc5482bf | -7.24936 | -57.66794 | 2025-08-15 05:42:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| d2aa7a6a-4cea-3382-a073-7bbe81c22533 | -6.90625 | -59.63646 | 2025-08-15 05:42:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 3403ced1-19fa-3752-8469-36462da23f62 | -7.11965 | -59.62293 | 2025-08-15 05:42:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| c4b4adbc-34a1-3a24-9d42-5c832603b149 | -6.70071 | -58.82854 | 2025-08-15 05:42:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 7.4 |
| 72d2f87a-1959-3a7a-9f08-90545e0452db | -7.07459 | -59.20555 | 2025-08-15 05:42:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 1302ed5c-310f-36fa-9da7-e40f2a2b34ad | -7.31449 | -60.6236 | 2025-08-15 05:42:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d7d9abdb-beb8-3c3e-a90c-44b8e7feca35 | -7.27294 | -57.65492 | 2025-08-15 05:42:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 28b6628e-ec23-35a6-bea5-e0328f3c4370 | -7.44255 | -60.02577 | 2025-08-15 05:42:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 1d049dd8-3c9f-36ce-801d-8254f4775ebc | -6.08458 | -62.5103 | 2025-08-15 05:42:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 9e1b1f3d-5d56-38c1-a241-d24680d3e923 | -7.42883 | -60.03156 | 2025-08-15 05:42:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 3d112363-95b6-3703-afa2-808b48ccf619 | -7.43413 | -60.02455 | 2025-08-15 05:42:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 4338938f-f8d3-3d87-8c8b-bdc06c6fe044 | -5.73705 | -59.88768 | 2025-08-15 05:42:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 13449403-5a72-3e03-b146-d17270ce91e7 | -6.72716 | -58.837 | 2025-08-15 05:42:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 11.1 |
| ac387b50-358f-3c7a-90cd-1c3ec1d5f1c0 | -6.66336 | -58.82005 | 2025-08-15 05:42:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 10.2 |
| 095cf395-30f3-3e6f-b83f-ab1036ce82f8 | -5.93784 | -59.93583 | 2025-08-15 05:42:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| fbea955e-8f35-3bec-81d3-3128210ff15c | -6.89303 | -59.1554 | 2025-08-15 05:42:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| e2fc5efb-951d-3f19-8f50-d6c5519e673f | -6.90057 | -59.13412 | 2025-08-15 05:42:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 2d26a3b9-d44e-3b11-b148-7d60e23a53f2 | -5.75226 | -59.87083 | 2025-08-15 05:42:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b783ab61-1cc4-3a5c-a6b7-a77b1bd992b0 | -7.25529 | -60.00412 | 2025-08-15 05:42:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 72055175-edc2-3f0b-85d8-d9d7eaab2058 | -7.25098 | -57.66855 | 2025-08-15 05:42:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| e376b162-b06c-347d-b877-3e0b5a0bd5c9 | -7.28852 | -57.65141 | 2025-08-15 05:42:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| c6d84a4e-a544-3126-80eb-c7fa393af91f | -6.94517 | -60.00339 | 2025-08-15 05:42:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| e6669a5e-ffb0-355b-91ab-d68c837919a7 | -7.27563 | -60.62913 | 2025-08-15 05:42:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| de738bff-9809-3540-808e-93f6070c9ec0 | -7.39377 | -60.00639 | 2025-08-15 05:42:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 3e1e8ada-e3ba-32b9-8f4c-f4ed482a39f0 | -5.81297 | -59.22291 | 2025-08-15 05:42:00 | NOAA-21 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 45a60ffe-49b2-3d11-879c-32396b391ff0 | -6.8886 | -59.15475 | 2025-08-15 05:42:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 8b3b68ae-7e60-34cb-8102-e1a0517a0e39 | -5.92487 | -59.93774 | 2025-08-15 05:42:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 92d277eb-1617-3118-8dcc-90ce8a601202 | -5.93425 | -59.93148 | 2025-08-15 05:42:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 41792929-3147-3be0-af31-103cee88ff7f | -6.87744 | -59.84028 | 2025-08-15 05:42:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 8fe21e37-6989-37e8-ab56-ec88fca8a18e | -5.93315 | -59.93897 | 2025-08-15 05:42:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 64ad2361-97db-3f82-836a-11b401e6d781 | -7.12653 | -59.63641 | 2025-08-15 05:42:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f3fc3ce8-e5a2-38c2-8950-d37f0a670e7f | -7.32357 | -60.61777 | 2025-08-15 05:42:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| efaf3816-4a27-3606-b53e-125d3523f38a | -6.66854 | -58.8161 | 2025-08-15 05:42:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 5.8 |
| fd7c9da3-067e-3b53-a055-99356a5abc2d | -6.95045 | -59.99627 | 2025-08-15 05:42:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.5 |
| bfe75be1-284e-3d23-b36c-8e66399f981f | -7.26425 | -60.00157 | 2025-08-15 05:42:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 2a5eeb7f-3786-313d-945d-5be423287c4d | -6.87779 | -59.13525 | 2025-08-15 05:42:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| f2a4ef51-82aa-304c-aff2-4fc1077fc2e4 | -7.07519 | -59.20123 | 2025-08-15 05:42:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 231c7b24-e549-3af3-868e-0f44c4d94a15 | -6.91199 | -59.14919 | 2025-08-15 05:42:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| e57ccf13-3519-373a-bee0-1cc244416ffe | -5.45744 | -60.14561 | 2025-08-15 05:42:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 0f5b2e9f-33dd-3b21-a2f2-85eb957144f3 | -6.91084 | -59.54147 | 2025-08-15 05:42:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 1d178abd-bf56-38df-a09e-359d00620731 | -6.94333 | -59.52982 | 2025-08-15 05:42:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 1457a9ec-a639-3f4e-b670-fd6b4381f54b | -6.69105 | -58.83179 | 2025-08-15 05:42:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| afb477ca-aca3-3c8e-979e-111897c916bf | -7.30238 | -60.62181 | 2025-08-15 05:42:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 6774ed93-4216-3ca3-a245-23d955d05dc3 | -7.43104 | -60.01619 | 2025-08-15 05:42:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| db1ffc2e-dccc-30d4-8631-52cdb734e807 | -6.92061 | -59.53463 | 2025-08-15 05:42:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 31e7a707-2880-30be-ae02-69a878feec9a | -6.70142 | -58.85631 | 2025-08-15 05:42:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 3.4 |
| c516a685-d19b-328a-9180-ab288bb624df | -7.15665 | -59.6406 | 2025-08-15 05:42:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| da4fad1c-c8a8-319d-85e9-e1c905e2f15d | -6.69169 | -58.82718 | 2025-08-15 05:42:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 7.3 |
| 892ab40d-07a3-3e55-a147-fbb212d98ea4 | -6.70332 | -58.84278 | 2025-08-15 05:42:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 8855d904-7075-3797-ade4-d15686612a62 | -7.13107 | -60.12656 | 2025-08-15 05:42:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 48b6deed-4b3e-3a35-9a74-99bb855a8657 | -6.87089 | -59.15218 | 2025-08-15 05:42:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 3a924b86-ce74-3832-a52d-5554d173d018 | -7.43525 | -60.0168 | 2025-08-15 05:42:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 2a87e449-3e24-3e2d-8260-97e21a4b0323 | -6.9111 | -59.63308 | 2025-08-15 05:42:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 80cebf88-82b2-3747-8400-6a0b50b57e54 | -6.87717 | -59.13966 | 2025-08-15 05:42:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 81cbe99c-857d-3e50-a3bd-2f9a26cb705b | -6.88479 | -59.1497 | 2025-08-15 05:42:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 1ccccb8c-f60b-3b75-90de-8f6c66fce3bc | -7.41477 | -60.00982 | 2025-08-15 05:42:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 47dd7bca-b978-3ab2-bfee-1092499160e9 | -6.92551 | -59.53116 | 2025-08-15 05:42:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 6970d1ce-efc4-3cf4-ac3a-6d941266ffbd | -6.91573 | -59.53806 | 2025-08-15 05:42:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 1ad0b97d-41cd-340d-8f3f-d2ae76cb34c7 | -6.94679 | -59.9919 | 2025-08-15 05:42:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| cbd4d723-f508-3f9d-88ae-5a800aeaa6cf | -6.70136 | -58.82391 | 2025-08-15 05:42:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 7.4 |


[Clique aqui para ver as próximas entradas](README56.md)
