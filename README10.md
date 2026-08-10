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

## Dados Diários - Página 10

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| b4f773bb-4648-3f55-8724-233adaa2441c | -2.97801 | -51.69001 | 2026-08-10 04:51:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 6.4 |
| 78ce19c6-4731-3f10-8f28-b2bd948360db | -6.46836 | -47.8476 | 2026-08-10 04:51:00 | NOAA-21 | ANGICO | TOCANTINS | Brasil | 1701051 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 5e111d6d-4c40-3e82-b847-2f130cc4d442 | -6.87587 | -56.64297 | 2026-08-10 04:51:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 9dc2fa51-015e-3e27-822b-55452b26f571 | -3.83596 | -54.322 | 2026-08-10 04:51:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| c6b332da-da03-33ef-a164-3d8d44614dbe | -3.39299 | -49.22158 | 2026-08-10 04:51:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c24d5b4c-fd04-3f69-910e-e056a43eb808 | -7.23989 | -49.8719 | 2026-08-10 04:51:00 | NOAA-21 | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| b1da5518-3735-3a7d-9de4-e6dd4f2d2206 | -6.81252 | -56.43306 | 2026-08-10 04:51:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 6aea070b-6e9b-36af-846f-f5fd117e5370 | -5.02698 | -56.12524 | 2026-08-10 04:51:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| fe6d80ca-e432-3cc6-bd09-aae57b90ebe7 | -10.25317 | -45.82107 | 2026-08-10 04:51:00 | NOAA-21 | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 22e936a7-75de-36eb-b4ac-ba7ab7ba0cbf | -7.66204 | -62.54553 | 2026-08-10 04:51:00 | NOAA-21 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b2d429ec-20ce-3a0a-9083-dceabd20037a | -3.48848 | -50.05221 | 2026-08-10 04:51:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 8.0 |
| f998a9be-91c8-3592-9510-31b231fa3e0f | -2.90898 | -54.14884 | 2026-08-10 04:51:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 822aae47-284b-3ff8-b31b-2fc170b2e1c6 | -6.82661 | -56.43991 | 2026-08-10 04:51:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 6ff5f98f-fe93-37cf-b3b7-65f5f9554326 | -6.82417 | -56.44679 | 2026-08-10 04:51:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a67bbd0c-cdf9-3d2d-9f1e-e5ace82aee1b | -6.85735 | -56.40705 | 2026-08-10 04:51:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 63972f4e-2caf-3362-be43-2fb0fb3b8c68 | -7.38932 | -59.97197 | 2026-08-10 04:51:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 420180ac-46c9-3360-b807-6202ea82ac9c | -2.96252 | -49.19595 | 2026-08-10 04:51:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a5db09cc-2214-3bb4-b661-1e6a8a2ecc6f | -6.83446 | -56.40789 | 2026-08-10 04:51:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| e445f801-4b91-30b8-b934-8929e58c0409 | -9.41328 | -47.43573 | 2026-08-10 04:51:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| f247b76f-a853-3cb1-b8c6-789435e171da | -7.6901 | -55.16167 | 2026-08-10 04:51:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| e9186b54-50cb-39db-a06d-c81e52048935 | -8.1722 | -61.51659 | 2026-08-10 04:51:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 7a4a939d-63f5-3d69-9e4f-0472a772cc42 | -2.50597 | -51.81669 | 2026-08-10 04:51:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| f7619489-3473-3eab-a4ab-755a732f6e33 | -6.80882 | -56.43246 | 2026-08-10 04:51:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 9edcdee1-53f5-3ba1-8256-40430e71db79 | -6.8308 | -56.42983 | 2026-08-10 04:51:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 49e22810-7f03-3470-8cee-6df69a74c166 | -6.25031 | -49.88485 | 2026-08-10 04:51:00 | NOAA-21 | CANAÃ DOS CARAJÁS | PARÁ | Brasil | 1502152 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| da21010a-92fa-3340-834c-b604f5c9b66c | -6.83373 | -56.41227 | 2026-08-10 04:51:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 2573bde2-60e1-36f8-85d8-a1c570e950d9 | -6.81181 | -56.43748 | 2026-08-10 04:51:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| d8b413c3-19f5-3580-b496-c55a1bd67fc0 | -10.25694 | -45.82293 | 2026-08-10 04:51:00 | NOAA-21 | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 4.8 |
| e5c6e111-1ffd-315f-a793-f1252b103917 | -6.83598 | -56.42154 | 2026-08-10 04:51:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 1f617ee8-edf5-3ee5-8fc2-129902d1d5a3 | -3.93283 | -59.12278 | 2026-08-10 04:51:00 | NOAA-21 | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | 6.4 |
| 0206d91f-b17f-3e6e-887b-262455ffde6d | -7.61405 | -42.76959 | 2026-08-10 04:51:00 | NOAA-21 | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | 3.4 |
| 89e35ae5-e94e-3692-af65-845fcff386ea | -6.84701 | -56.40082 | 2026-08-10 04:51:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 6e9b5150-06a7-3e19-b096-35dc55360507 | -3.26969 | -49.53241 | 2026-08-10 04:51:00 | NOAA-21 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 37f7aa63-b443-3183-b791-8ff8adcc7516 | -2.9626 | -49.19302 | 2026-08-10 04:51:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| e51bb835-89f0-3014-b462-8581c1e91f38 | -7.5386 | -55.5749 | 2026-08-10 04:51:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 668b59ab-950c-3344-bae2-feb458129efb | -7.68948 | -55.16547 | 2026-08-10 04:51:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 6221e461-e1cd-33ad-8cc8-25921b0e4ed1 | -7.69231 | -55.16983 | 2026-08-10 04:51:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 4eed8e55-dcae-3ff0-9a3b-75ae0e58848d | -6.2505 | -55.61926 | 2026-08-10 04:51:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 659164c1-7487-3d81-a02d-86f7ad238396 | -6.72078 | -58.93026 | 2026-08-10 04:51:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d5cbf091-c4ea-3a54-a449-3594b81a5336 | -4.86726 | -55.8194 | 2026-08-10 04:51:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 0ad28344-99ea-3a51-be2e-f17c41c99637 | -6.83015 | -56.4179 | 2026-08-10 04:51:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 250866cf-90be-359c-abcf-e56d4e1c4ddc | -3.18949 | -52.88297 | 2026-08-10 04:51:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 8707d4d1-12b4-303e-9976-6d0331d4ae90 | -8.46954 | -47.72792 | 2026-08-10 04:51:00 | NOAA-21 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 4849d2a0-2c93-3234-a745-a6a798840c78 | -6.13149 | -57.77118 | 2026-08-10 04:51:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 1424f049-f207-37d4-a725-ada5b915b629 | -6.81693 | -56.4293 | 2026-08-10 04:51:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 0c306265-d806-34fd-8870-80b3870fff25 | -3.32136 | -48.81725 | 2026-08-10 04:51:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 2b500ff0-d7f5-3e3d-a81a-3acf5e58e62a | -6.24692 | -55.61874 | 2026-08-10 04:51:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 4a924747-bd66-381a-9ba7-1f280df63033 | -6.83671 | -56.41718 | 2026-08-10 04:51:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 42aa9301-e8c9-39e6-81c2-57e29303be67 | -4.40056 | -54.78545 | 2026-08-10 04:51:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 7539d9a3-a769-3bee-b789-c1aa8b2348d0 | -6.16206 | -57.91352 | 2026-08-10 04:51:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 8cc23a42-e0f8-3858-a06c-5f18d9471949 | -8.63841 | -45.86987 | 2026-08-10 04:51:00 | NOAA-21 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 8c7f7d8d-3a1c-3842-961c-1ced88192ce7 | -6.8441 | -56.41838 | 2026-08-10 04:51:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| fdf1e888-30e5-37c8-8e77-77e557ca283c | -10.25791 | -45.82238 | 2026-08-10 04:51:00 | NOAA-21 | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 4.1 |
| d1523f7a-67ab-3a98-beac-cd7c174381a8 | -2.5065 | -51.81326 | 2026-08-10 04:51:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| d72988d3-3e23-3a09-b585-6046e10c64ef | -6.70862 | -58.94966 | 2026-08-10 04:51:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| ae1b7f6d-b0d0-3498-b6e4-1861e430ea38 | -9.41754 | -47.43639 | 2026-08-10 04:51:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 7e292cde-e1a7-3a95-b2a0-adbe52d84963 | -6.84998 | -56.40581 | 2026-08-10 04:51:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 53f3b50c-3ca9-3cc8-807f-5942023acdb1 | -3.96231 | -48.12562 | 2026-08-10 04:51:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| d514ccc2-fc43-3613-9eab-53ff47a6e098 | -6.84482 | -56.41403 | 2026-08-10 04:51:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 370c0d71-01ac-3436-8f08-fbb8e0448b4b | -2.65269 | -54.62428 | 2026-08-10 04:51:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 1fae85bb-99df-3be1-8ae9-a6eecf48bdc0 | -6.72441 | -58.93521 | 2026-08-10 04:51:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| dab452b3-d5fe-3a8d-b001-89d23dff16da | -6.833 | -56.41663 | 2026-08-10 04:51:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 573b8c90-4e0c-3037-bb85-5e430de7cb53 | -6.83472 | -56.43669 | 2026-08-10 04:51:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 49b3d608-dc15-31e6-a9ad-94d267b49a37 | -7.62181 | -42.75492 | 2026-08-10 04:51:00 | NOAA-21 | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| f49d1c56-4c67-3549-8fed-0b5ab64ffc85 | -7.54212 | -55.57545 | 2026-08-10 04:51:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 3e776d1b-4df1-3e37-bbaa-3daf911d8643 | -6.83007 | -56.43421 | 2026-08-10 04:51:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 0b38e2aa-94ae-3ea1-bb4b-4185e9e99a59 | -7.57215 | -55.5682 | 2026-08-10 04:51:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 60f05785-ba64-31ed-867c-59716bcb5e3f | -4.45921 | -47.91756 | 2026-08-10 04:51:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 16.5 |
| 754a113d-937c-3520-96ad-2e541651cdea | -4.28495 | -49.97828 | 2026-08-10 04:51:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 2d44b16f-6b6c-3908-981d-3e39f53d9ae8 | -5.03512 | -56.12216 | 2026-08-10 04:51:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 3f9ad9cc-fe21-32c5-84d8-5308022ebbbb | -7.6614 | -62.54908 | 2026-08-10 04:51:00 | NOAA-21 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 23f90bbe-5f4e-3ec3-b542-0eb4920deb5b | -6.82857 | -56.42043 | 2026-08-10 04:51:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a475f3c0-dbe3-3371-9873-9e074c69c008 | -7.61456 | -42.76574 | 2026-08-10 04:51:00 | NOAA-21 | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | 3.4 |
| 56e372c7-9ea8-3573-8103-30ed72418d8b | -8.6405 | -45.87104 | 2026-08-10 04:51:00 | NOAA-21 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 396ea41f-29d2-3bb6-99b0-959676da9cdf | -7.61558 | -42.75798 | 2026-08-10 04:51:00 | NOAA-21 | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | 2.9 |
| b090cc9a-ef0b-3445-9b77-4633f2afe8f7 | -7.55396 | -55.56922 | 2026-08-10 04:51:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 8.1 |
| b41d1235-6412-3cd8-a3af-09f8a013fe25 | -4.4515 | -47.9164 | 2026-08-10 04:51:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 25.5 |
| 969eb108-ef3e-3a8e-b40c-701c8556ae6b | -6.14145 | -57.71082 | 2026-08-10 04:51:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 6.3 |
| c911ea34-f6d7-338a-a080-638b807347d1 | -7.54757 | -55.56418 | 2026-08-10 04:51:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| dfe0a106-6623-3e14-8fad-ffde7e287c1d | -10.25646 | -45.83308 | 2026-08-10 04:51:00 | NOAA-21 | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 0a1f4f24-0a73-36e3-8a94-c7376bc7a7a7 | -6.82361 | -56.43495 | 2026-08-10 04:51:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 3cb5a775-2e75-3579-b617-497a141ed8ba | -6.84851 | -56.41463 | 2026-08-10 04:51:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| cccbcf48-4f1d-3156-93e4-2602f37e4f11 | -5.73292 | -49.13501 | 2026-08-10 04:51:00 | NOAA-21 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| db77c0b8-cc46-30a7-90a4-d005252bd711 | -10.25627 | -45.82819 | 2026-08-10 04:51:00 | NOAA-21 | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 10.2 |
| 34f97709-e83d-3654-bc50-67dba1b98d59 | -5.87844 | -51.71328 | 2026-08-10 04:51:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a92428fe-3ec5-35f8-a54f-f9861ed40a84 | -3.75902 | -51.61074 | 2026-08-10 04:51:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 944251da-93ba-3491-b83b-38aaffeb944d | -6.84112 | -56.41343 | 2026-08-10 04:51:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 3e2a2bc0-faf7-3efe-899b-3769b544ee93 | -6.84628 | -56.40521 | 2026-08-10 04:51:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e3e565e3-ed06-3000-b1c4-1e142bc3d350 | -6.83965 | -56.40593 | 2026-08-10 04:51:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| c6c3d625-9ec2-345b-a381-c52cb381d4a3 | -6.85439 | -56.40206 | 2026-08-10 04:51:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 1570237d-6af9-3386-98f5-f63e3d3171b1 | -6.83543 | -56.4323 | 2026-08-10 04:51:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 2ea45fee-65bb-320f-9728-0d7b63388755 | -6.83967 | -56.42214 | 2026-08-10 04:51:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 6fbbbef7-b37a-3b72-b276-d060cee41397 | -4.86429 | -55.81454 | 2026-08-10 04:51:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| bde80a16-6249-3f43-a153-da4065047950 | -6.98643 | -39.50034 | 2026-08-10 04:51:00 | NOAA-21 | FARIAS BRITO | CEARÁ | Brasil | 2304301 | 23 | 33 | nan | nan | nan | Caatinga | 5.1 |
| dd03017c-1161-3076-8665-4e171811632c | -8.30482 | -46.41513 | 2026-08-10 04:51:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 9.4 |
| 6d504b7a-51f4-3b5b-9c68-92b4d75ecb72 | -5.02883 | -56.12651 | 2026-08-10 04:51:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| ba05ee23-0914-3e9d-ac16-5b654e25ca06 | -7.55044 | -55.56866 | 2026-08-10 04:51:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 8.1 |
| 2bd5b408-5498-3c75-9bb2-2fb173b0b566 | -6.98559 | -39.50684 | 2026-08-10 04:51:00 | NOAA-21 | FARIAS BRITO | CEARÁ | Brasil | 2304301 | 23 | 33 | nan | nan | nan | Caatinga | 5.1 |
| 2d7a4e40-a150-3e88-8bb5-57afaf6e757f | -6.85367 | -56.40642 | 2026-08-10 04:51:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 52e007d0-b14a-3fcc-b5a2-4b513f6a30a3 | -5.79719 | -51.88651 | 2026-08-10 04:51:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |


[Clique aqui para ver as próximas entradas](README11.md)
