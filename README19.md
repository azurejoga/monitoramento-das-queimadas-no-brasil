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

## Dados Diários - Página 19

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| bec381cf-81d0-3db4-94bb-ccbae93edb94 | -4.03345 | -48.06615 | 2025-07-17 04:44:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 9a05015b-fb61-380e-af64-4dcf2a3506de | -3.0329 | -47.86034 | 2025-07-17 04:44:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 2a166235-57b3-3433-b7bb-366d2bf24c47 | -4.30019 | -48.10049 | 2025-07-17 04:44:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 12.7 |
| 8ab5d77c-1653-3bcc-88fb-dbc8e8399840 | -3.38449 | -47.47941 | 2025-07-17 04:44:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 15.2 |
| ffb64da3-d491-3d64-baa6-52d7f53b5c5e | -2.63796 | -47.34029 | 2025-07-17 04:44:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 7a5d0231-b460-3535-805f-b3741a536da8 | -2.47976 | -47.20773 | 2025-07-17 04:44:00 | NOAA-21 | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 5bbd5de4-14a4-362b-bdb4-c2055ca6d7e8 | -4.3037 | -48.10102 | 2025-07-17 04:44:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 18.3 |
| 4fb1ed11-7432-3e17-93f8-5f83e633a116 | -5.51669 | -41.32999 | 2025-07-17 04:44:00 | NOAA-21 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 3.2 |
| d3c64c2b-a773-35c7-8a79-7d673f906919 | -3.40577 | -47.50759 | 2025-07-17 04:44:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 7cecb580-89e8-30c3-b907-49b1ce5a2ed9 | -5.01881 | -38.52828 | 2025-07-17 04:44:00 | NOAA-21 | IBICUITINGA | CEARÁ | Brasil | 2305332 | 23 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 33928fa6-a67c-3e29-b419-241dda145a1a | -3.84611 | -47.75092 | 2025-07-17 04:44:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| fc1920cb-89a6-3b33-af46-342e8d913755 | -3.66546 | -48.31573 | 2025-07-17 04:44:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| f4dcb65d-d231-32f1-92cf-5fa5d733cc29 | -3.58693 | -47.52836 | 2025-07-17 04:44:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 612a324f-23d3-300d-86fd-801ab19ae160 | -3.38976 | -47.49271 | 2025-07-17 04:44:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| c48d953a-8b9e-3326-abe0-af08709aa513 | -3.3828 | -47.46657 | 2025-07-17 04:44:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 4771d650-61f3-378b-9749-71973e164b02 | -4.22329 | -49.79012 | 2025-07-17 04:44:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 544d9c1c-ba42-379a-b17f-0ac4b2879c6f | -5.01802 | -38.53392 | 2025-07-17 04:44:00 | NOAA-21 | IBICUITINGA | CEARÁ | Brasil | 2305332 | 23 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 290a30f4-c132-3711-8f1c-1c42c19dcdee | -3.99453 | -43.23386 | 2025-07-17 04:44:00 | NOAA-21 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| fdb2b2fb-7d4d-37f8-9fb6-58db7820d557 | -3.41203 | -47.507 | 2025-07-17 04:44:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 3bd5fcf9-9201-39a5-b332-b379fe48b0c9 | -2.44359 | -47.33336 | 2025-07-17 04:44:00 | NOAA-21 | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 85588782-1078-38de-a78b-cb7c9549ae23 | -4.07434 | -47.32895 | 2025-07-17 04:44:00 | NOAA-21 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 4c8fa456-39cb-34ed-9510-9eb8ffb56b6a | -3.39271 | -47.49733 | 2025-07-17 04:44:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 1d6268b1-2c52-324f-a328-21e4f3b73502 | -4.78213 | -45.33754 | 2025-07-17 04:44:00 | NOAA-21 | LAGO DA PEDRA | MARANHÃO | Brasil | 2105708 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| ec57e5ad-fd04-396a-867b-25bee55f5b3b | -3.04422 | -49.43238 | 2025-07-17 04:44:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 2f3af0b7-401d-3c35-8323-31a288ce19ac | -3.23364 | -51.89626 | 2025-07-17 04:44:00 | NOAA-21 | VITÓRIA DO XINGU | PARÁ | Brasil | 1508357 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 0d7a57b8-c58f-341b-ada3-a6cc3ca0a948 | -2.63859 | -47.33622 | 2025-07-17 04:44:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| f53e6911-fb18-3cd1-83a5-12388bbff6ef | -3.38386 | -47.48349 | 2025-07-17 04:44:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 26.4 |
| ea5799bc-3c5d-3c11-a387-743538694e0e | -3.28361 | -48.87925 | 2025-07-17 04:44:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| a1569dd1-a147-3192-9b6a-e0c1755cb6b7 | -2.91215 | -48.24266 | 2025-07-17 04:44:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 5a0acdfb-f74c-3a7d-8427-25bacd229435 | -3.07605 | -52.428 | 2025-07-17 04:44:00 | NOAA-21 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| d244ec7e-ed20-3a3f-8198-6850b215cc63 | -4.8141 | -43.22004 | 2025-07-17 04:44:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 4.2 |
| f786f485-8612-3357-b066-752a00b1e5d9 | -3.39039 | -47.48865 | 2025-07-17 04:44:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| ac5bae62-b9be-3dac-9a1f-537ee210f1f1 | -5.01776 | -38.52789 | 2025-07-17 04:44:00 | NOAA-21 | IBICUITINGA | CEARÁ | Brasil | 2305332 | 23 | 33 | nan | nan | nan | Caatinga | 2.9 |
| 0d3db2b0-7cad-3b73-9109-5a8d08474be6 | -4.81421 | -45.26531 | 2025-07-17 04:44:00 | NOAA-21 | LAGO DA PEDRA | MARANHÃO | Brasil | 2105708 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| f4ffab96-09af-3142-ac75-fe5343fc38b4 | -4.80429 | -43.22301 | 2025-07-17 04:44:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 10a3f6eb-4c79-3aef-885a-67cc83178d59 | -3.3887 | -47.47586 | 2025-07-17 04:44:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 15.2 |
| dd5b42c9-b4aa-38f5-b54e-227d5ce6083b | -2.91501 | -48.24695 | 2025-07-17 04:44:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 003e5aba-9d71-356f-9ce6-13c35052566f | -3.38744 | -47.48404 | 2025-07-17 04:44:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 26.4 |
| 86df6dce-756d-327a-9349-e755fe4db47f | -3.40998 | -47.50408 | 2025-07-17 04:44:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 2f1db16d-9946-37a6-9420-d462fe81d4af | -3.07664 | -52.42424 | 2025-07-17 04:44:00 | NOAA-21 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 9857a229-b76f-3399-9133-0abe7ba91af4 | -3.02476 | -49.42579 | 2025-07-17 04:44:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 89994269-a4c0-3d56-8886-9d950e5f222b | -2.91904 | -48.24371 | 2025-07-17 04:44:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 17b1b92c-ab6e-3b18-8508-05e0c0490a7d | -3.04476 | -49.42888 | 2025-07-17 04:44:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| e5e3aba5-0ec4-3703-b357-0112093d177a | -5.51723 | -41.32628 | 2025-07-17 04:44:00 | NOAA-21 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 60c4b588-bf77-3b44-9833-601021af490a | -3.39102 | -47.48457 | 2025-07-17 04:44:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| db792eed-795a-3b20-ab7a-9a8e6985d40a | -3.21733 | -48.97236 | 2025-07-17 04:44:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 63190484-9758-3af1-adb8-9710221fe079 | -3.0364 | -47.86089 | 2025-07-17 04:44:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 1b476572-ff47-358c-b64d-5c6c5ce384b3 | -3.40282 | -47.50303 | 2025-07-17 04:44:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 20d9a923-18c8-3b3e-9fee-e4aea7fe0229 | -4.77743 | -45.34064 | 2025-07-17 04:44:00 | NOAA-21 | LAGO DA PEDRA | MARANHÃO | Brasil | 2105708 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 9c1e3de3-d57c-34fc-89fa-99e8dd4e7730 | -4.44634 | -38.44525 | 2025-07-17 04:44:00 | NOAA-21 | OCARA | CEARÁ | Brasil | 2309458 | 23 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 79f8d90b-7449-3239-8bad-3b9c0972ff28 | -3.40936 | -47.50811 | 2025-07-17 04:44:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 7922a920-2949-3fb4-a4d8-9f741b374539 | -2.44065 | -47.32875 | 2025-07-17 04:44:00 | NOAA-21 | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 051b5dba-5825-3334-ad83-9f808e4dbbeb | -3.55091 | -53.01607 | 2025-07-17 04:44:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 8e1e41d3-55cf-39f6-947a-e9a5726ac4d3 | -2.9271 | -48.23726 | 2025-07-17 04:44:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| b6222c17-b03e-3700-b31b-bb121fa2b628 | -3.38807 | -47.47995 | 2025-07-17 04:44:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 15.2 |
| f8b3f372-6eb4-383e-8544-c0c57b868ccd | -2.44715 | -47.33392 | 2025-07-17 04:44:00 | NOAA-21 | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a35d53b7-e5c4-3c29-b166-d050c9a0b0ed | -3.40845 | -47.50648 | 2025-07-17 04:44:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| b7c1c4bb-994a-3b09-8734-9ab928abb0df | -3.38323 | -47.48756 | 2025-07-17 04:44:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 26.4 |
| 92fdaf7e-59fe-3e29-af68-87f9020eb40c | -3.54917 | -53.57408 | 2025-07-17 04:44:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 839e69f3-4f31-39fa-90fc-4e71e8c78f5a | -3.39566 | -47.50195 | 2025-07-17 04:44:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 7.3 |
| 6bde5306-0b65-3154-8c9b-b5b227ba35a9 | -2.47769 | -47.20892 | 2025-07-17 04:44:00 | NOAA-21 | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| cb00a304-7bc7-3f8e-9f2b-ea79a3e741aa | -2.91675 | -48.23565 | 2025-07-17 04:44:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 2bb0aa0d-11de-3d00-b949-20f6870010af | -4.03055 | -48.06169 | 2025-07-17 04:44:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 673b03d6-2bda-3ccd-956b-a80887beaed3 | -4.03405 | -48.06224 | 2025-07-17 04:44:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b6b17188-ee03-3403-8f0e-98b2bb4e289a | -2.91157 | -48.24642 | 2025-07-17 04:44:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| ebb22d30-1a40-31ba-9223-3afc9ee41960 | -5.97104 | -52.20399 | 2025-07-17 04:46:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| f3b78782-5bd8-3b3f-af1c-9f9aa8b02550 | -9.30626 | -44.84628 | 2025-07-17 04:46:00 | NOAA-21 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 63d22c8f-a0ba-3ce7-932a-373817fdeffb | -9.62222 | -49.10145 | 2025-07-17 04:46:00 | NOAA-21 | ABREULÂNDIA | TOCANTINS | Brasil | 1700251 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| a27a8cef-0c92-3e00-ace1-2712f4e2bf16 | -10.65893 | -49.4782 | 2025-07-17 04:46:00 | NOAA-21 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| faefea96-980f-3dd0-90c7-d055625d658c | -8.70998 | -50.04992 | 2025-07-17 04:46:00 | NOAA-21 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 7aa95488-458f-3d13-878e-df6004816d98 | -6.8506 | -44.76502 | 2025-07-17 04:46:00 | NOAA-21 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| f29e8fa7-0b52-3d97-9edd-18c8f9362a29 | -6.381 | -44.75256 | 2025-07-17 04:46:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| a398e106-fe99-3a16-879e-f381cb362a6c | -5.25632 | -47.71035 | 2025-07-17 04:46:00 | NOAA-21 | IMPERATRIZ | MARANHÃO | Brasil | 2105302 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 6b79a47c-7c04-361f-9e41-fc7b111fa126 | -8.88089 | -50.15079 | 2025-07-17 04:46:00 | NOAA-21 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 613b085c-c5e9-3866-a889-4115f147f044 | -4.45554 | -48.99357 | 2025-07-17 04:46:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 424a9a59-b6d2-3443-828c-df16b5d8c57f | -12.09457 | -48.19211 | 2025-07-17 04:46:00 | NOAA-21 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| cf12a267-7a84-3b11-ab20-c989d0a619b2 | -6.62884 | -56.28414 | 2025-07-17 04:46:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 26df4d7e-9d4e-3af2-b79e-030fd4aa4ba0 | -9.71299 | -61.28872 | 2025-07-17 04:46:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 8189fcd1-6a74-32f0-bbe2-57735c078e1d | -8.91674 | -49.83949 | 2025-07-17 04:46:00 | NOAA-21 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 7d9d9b5b-5c91-3009-b1f2-03614dd4a25c | -9.31508 | -44.8489 | 2025-07-17 04:46:00 | NOAA-21 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 2629c262-d75b-31ca-9fd0-e691ce321398 | -11.66985 | -43.76705 | 2025-07-17 04:46:00 | NOAA-21 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 68f16258-0a64-3cad-8322-90759ebe057f | -6.35153 | -44.60885 | 2025-07-17 04:46:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 9c098893-84ac-39ce-9855-c6a9eba6b234 | -8.04281 | -49.88961 | 2025-07-17 04:46:00 | NOAA-21 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 78f0aa35-4257-334e-a24a-7750906cbcb4 | -6.82344 | -43.7834 | 2025-07-17 04:46:00 | NOAA-21 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 6d560de7-a99e-3cc2-9913-7fdafa4e216d | -5.44462 | -42.62838 | 2025-07-17 04:46:00 | NOAA-21 | LAGOA DO PIAUÍ | PIAUÍ | Brasil | 2205581 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 67dea5a5-8a0d-38e2-bf00-53872cbbdcf0 | -5.79853 | -45.10535 | 2025-07-17 04:46:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 935a5466-e524-3790-974a-ed4c2ca045b5 | -10.67858 | -56.54187 | 2025-07-17 04:46:00 | NOAA-21 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 7.4 |
| edc64219-f936-3af4-90ba-24af72579173 | -7.50493 | -55.01214 | 2025-07-17 04:46:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 6bec1434-18a0-36c6-b436-5874b8039424 | -10.65952 | -49.47419 | 2025-07-17 04:46:00 | NOAA-21 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| d65cfb18-6afc-39ad-8e27-9d4d53bd9ed7 | -10.62198 | -48.07793 | 2025-07-17 04:46:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| d630350c-08ff-30c2-914d-5735dd6c92d9 | -11.56927 | -47.09176 | 2025-07-17 04:46:00 | NOAA-21 | PORTO ALEGRE DO TOCANTINS | TOCANTINS | Brasil | 1718006 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| cb3b8761-8152-3d0f-8bc1-2eb342d64a7b | -10.96382 | -49.25203 | 2025-07-17 04:46:00 | NOAA-21 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| e1f1cda4-a5ae-301f-9c20-c1aa29fd6d84 | -9.01461 | -61.22538 | 2025-07-17 04:46:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a73b5d49-2170-3dc3-a0ec-eaed4ebc4475 | -10.67641 | -56.54383 | 2025-07-17 04:46:00 | NOAA-21 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 6.5 |
| 405e6c8b-2835-3233-8f75-2d4d55fe7589 | -6.98043 | -43.74392 | 2025-07-17 04:46:00 | NOAA-21 | MARCOS PARENTE | PIAUÍ | Brasil | 2206001 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 6af7f375-d450-3288-be50-4df0d7693ed0 | -6.84616 | -44.76431 | 2025-07-17 04:46:00 | NOAA-21 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 7231fa37-12cf-3d48-af76-301e9a84af5c | -11.94509 | -48.42628 | 2025-07-17 04:46:00 | NOAA-21 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 2e87fc8a-23d0-3d54-9229-ff54f10ac41b | -9.34272 | -57.43662 | 2025-07-17 04:46:00 | NOAA-21 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 50f1efe1-145b-3a8b-bfbf-53aeb7f10f04 | -6.43361 | -45.31594 | 2025-07-17 04:46:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 48a3f100-5256-30f5-8488-11711b617b53 | -10.67942 | -56.54928 | 2025-07-17 04:46:00 | NOAA-21 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |


[Clique aqui para ver as próximas entradas](README20.md)
