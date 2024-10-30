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

## Dados Diários - Página 62

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 298c043c-9892-3778-b994-a71d989c638b | -5.94457 | -50.85909 | 2024-10-30 04:44:00 | NPP-375D | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 972f492d-798c-361c-ac32-86b58d10e09e | -5.94125 | -50.85857 | 2024-10-30 04:44:00 | NPP-375D | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 7b9844da-90ae-3f73-b7c6-0dc8eff3ea04 | -5.73281 | -49.98536 | 2024-10-30 04:44:00 | NPP-375D | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 9b0afa07-ea41-3c9a-b98c-807ffb9982bd | -5.69908 | -49.87218 | 2024-10-30 04:44:00 | NPP-375D | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 7e020d9e-3e4a-3c80-b4ca-4cd4c0fd9c78 | -5.52095 | -49.80171 | 2024-10-30 04:44:00 | NPP-375D | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| defd7320-e4a6-351a-9bf1-ab5e572f024b | -5.47425 | -50.53335 | 2024-10-30 04:44:00 | NPP-375D | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ad6d92fb-ee10-3ab0-9d88-f1f939f8b957 | -5.47093 | -50.53283 | 2024-10-30 04:44:00 | NPP-375D | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b42cc220-470f-3bd1-ad39-8b4402ffa025 | -5.47038 | -50.53629 | 2024-10-30 04:44:00 | NPP-375D | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 023e1bb7-dc8e-3e4b-9118-6ea5507d43bf | -5.4674 | -50.53584 | 2024-10-30 04:44:00 | NPP-375D | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 2652f463-40d8-3a63-88da-f652dbc6fc2d | -5.46627 | -50.64907 | 2024-10-30 04:44:00 | NPP-375D | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 0486fd34-8ffa-3e0f-8463-bece6368e35a | -5.46572 | -50.65253 | 2024-10-30 04:44:00 | NPP-375D | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| e0e7e387-e7ce-309a-a512-fa8cfbdc2425 | -5.29624 | -50.56943 | 2024-10-30 04:44:00 | NPP-375D | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 2e2b5138-3b98-3601-96ac-a845192759fb | -5.29292 | -50.56891 | 2024-10-30 04:44:00 | NPP-375D | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| b1a72d76-61d7-3e50-9f7f-d927c7fc1d4b | -5.21426 | -49.99453 | 2024-10-30 04:44:00 | NPP-375D | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 0.2 |
| 331b3c6d-3088-39e3-ab63-b9b288ab78d9 | -8.51497 | -50.77436 | 2024-10-30 04:44:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 26abe000-6124-33cc-a630-d55231bcc4da | -2.08465 | -51.42048 | 2024-10-30 04:44:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| f74479cb-9d46-385f-bacc-f17ccf684a2a | -1.42282 | -51.60553 | 2024-10-30 04:44:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 3419f53a-59ba-3f58-be47-f27370453bf2 | -1.41999 | -51.60131 | 2024-10-30 04:44:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 4618a380-ef05-3568-ae22-8a6e84662195 | -1.4194 | -51.60498 | 2024-10-30 04:44:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 8be4c949-cb05-3215-9644-7e77abb1c264 | -1.36462 | -51.4209 | 2024-10-30 04:44:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 0b004ce3-6e32-39e8-be9b-939731570ffd | -2.23261 | -50.70537 | 2024-10-30 04:44:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| af5f30bb-1a57-32e4-b477-106dacb0dc13 | -2.22928 | -50.70485 | 2024-10-30 04:44:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 1aad22f2-5daa-36b3-b74a-b88023b4bfda | -2.20087 | -50.58645 | 2024-10-30 04:44:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 48648b9b-1b86-3618-9389-8d41b96d2f71 | -2.20032 | -50.58992 | 2024-10-30 04:44:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 7b439681-d7d3-37af-b0a8-8b5ebba7bcb9 | -2.19809 | -50.58247 | 2024-10-30 04:44:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| e7e0e72e-7c46-31f0-a1c3-5e9fa0580e87 | -2.19754 | -50.58593 | 2024-10-30 04:44:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f899963b-b005-330e-8d8e-b2dcbe10d26c | -2.19699 | -50.58941 | 2024-10-30 04:44:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 23ec9616-1940-3e9e-8c89-723a601019dd | -2.19476 | -50.58195 | 2024-10-30 04:44:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 66af72fa-deae-3d96-b2e7-686aa9f9706c | -2.19438 | -50.8173 | 2024-10-30 04:44:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 1e9a232b-fcd8-3752-bd55-a328bd62cc84 | -2.19421 | -50.58541 | 2024-10-30 04:44:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| ff2588d3-079f-3783-b020-8a89547bd121 | -2.19366 | -50.58889 | 2024-10-30 04:44:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 91f528b2-075c-357b-babe-e5f6252ab4d6 | -2.16324 | -50.63039 | 2024-10-30 04:44:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| bd31f933-a3fd-3c6e-b5d1-5823fd63d45b | -2.16291 | -50.74088 | 2024-10-30 04:44:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 17f30c24-6636-377c-b44b-be5c419f27a1 | -2.15767 | -50.90482 | 2024-10-30 04:44:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| d8f458d2-775a-39c2-af17-48ace89ffe36 | -2.15692 | -50.80072 | 2024-10-30 04:44:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 8d13d9b8-ff72-391b-b606-fa88a48c5dfd | -2.15358 | -50.80019 | 2024-10-30 04:44:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 1aaaee77-522f-3ed3-8ea5-c09ea0897dd0 | -2.11745 | -50.83395 | 2024-10-30 04:44:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 45184845-0d9d-3b07-8879-6380d3726e57 | -2.09908 | -50.84184 | 2024-10-30 04:44:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 4260f736-edd1-3a67-bbd9-0dc11fca26c4 | -1.96602 | -50.72465 | 2024-10-30 04:44:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 60fb88fc-8381-3faa-aac5-31b232cd1ea7 | -1.95989 | -50.72012 | 2024-10-30 04:44:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.3 |
| b2edea85-d146-3803-955c-6946d07da838 | -1.87667 | -51.03075 | 2024-10-30 04:44:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 8a7da0cf-b170-3863-b06f-848fb5c40aad | -1.87331 | -51.03022 | 2024-10-30 04:44:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| f37e5ef5-0278-3cb6-bcd8-9aaf22710305 | -1.86718 | -51.1127 | 2024-10-30 04:44:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 2a51bfbe-f8d8-3896-9e1a-c64c22c849d5 | -1.86211 | -50.9923 | 2024-10-30 04:44:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 1e4f2dd1-a301-3fc8-99df-0dac1d568d41 | -3.60354 | -51.44861 | 2024-10-30 04:44:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| e1f41bcf-44e6-3e45-8900-36f335584397 | -3.58893 | -51.47538 | 2024-10-30 04:44:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 25c8b21d-dc85-3f76-92b3-f982b4749d2d | -3.58735 | -51.43103 | 2024-10-30 04:44:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 4750e83c-953a-321d-9be9-ba28666a18b5 | -3.53573 | -50.85608 | 2024-10-30 04:44:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 4e44e857-11ab-3725-91a3-1a84569fae12 | -3.0373 | -51.44365 | 2024-10-30 04:44:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c4d323a7-0e0f-331e-8708-388cb21d6f93 | -3.03674 | -51.44722 | 2024-10-30 04:44:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ab31214a-5ec7-3949-ad14-1c368e18453f | -3.03393 | -51.44315 | 2024-10-30 04:44:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 943cec79-b7d5-35b4-aa7f-b15676433c18 | -3.03337 | -51.44672 | 2024-10-30 04:44:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c36bd023-9934-32b9-9b5a-2f8fdfc1e11a | -3.03173 | -51.78905 | 2024-10-30 04:44:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 87bc1f03-5246-3e71-8914-c39f55309a8f | -3.03115 | -51.7927 | 2024-10-30 04:44:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c482c848-94ac-3340-8e3c-0f698cc2c0de | -3.02891 | -51.78488 | 2024-10-30 04:44:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 34bac46c-80cc-3b87-b7fe-f94eee48afdb | -3.02833 | -51.78851 | 2024-10-30 04:44:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 7e4bb855-7f76-39e2-bd57-5e2cd101137b | -3.02551 | -51.78435 | 2024-10-30 04:44:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| db7b7958-4847-3b20-9b65-35b416661242 | -3.02493 | -51.78799 | 2024-10-30 04:44:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 854a9ea0-0a92-351d-a0cf-0b91e02a8b03 | -2.93187 | -51.58481 | 2024-10-30 04:44:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d9865455-2740-3ebd-92ee-5783400d8d5b | -2.92849 | -51.58428 | 2024-10-30 04:44:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| cc438e50-ed50-305d-9816-ee6d8dae9359 | -2.92569 | -51.75419 | 2024-10-30 04:44:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a8bb4498-e1b0-3279-bd8d-c52b0d987d8a | -2.74335 | -51.64828 | 2024-10-30 04:44:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 30dce903-3ba1-36c8-8d76-ac076a8def55 | -2.74147 | -51.72598 | 2024-10-30 04:44:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 0f7abbb7-84c2-3cdf-927a-191e23d8802a | -2.74089 | -51.72961 | 2024-10-30 04:44:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| daaee53c-148d-3943-8b8a-305b15fdd55b | -2.7388 | -51.65498 | 2024-10-30 04:44:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 19e6de5c-6672-39e2-adbb-0872a5e6c50b | -2.73807 | -51.72543 | 2024-10-30 04:44:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 141c8cbc-ba04-39f4-901e-beabc351f15a | -2.73749 | -51.72906 | 2024-10-30 04:44:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| f4829ebb-6c31-3efd-91a5-fb2db0e1f8f3 | -2.73467 | -51.7249 | 2024-10-30 04:44:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| b5814fdf-2e34-341d-a3ae-da78eb0cd479 | -2.73409 | -51.72853 | 2024-10-30 04:44:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| fad8cdbc-eeca-31af-9974-feb729ed63b9 | -2.70994 | -51.96909 | 2024-10-30 04:44:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e31c69de-6dfb-310c-91b0-6c3a77be3007 | -2.70133 | -51.97911 | 2024-10-30 04:44:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| bb87ca62-8ce7-396e-bc28-b8270f77bacf | -2.65022 | -51.74932 | 2024-10-30 04:44:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 6836b865-7b9b-3b82-a0e9-cfd492fefabe | -2.64964 | -51.75296 | 2024-10-30 04:44:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| f930fcf7-6f66-3964-8bec-e6f820d6c2ae | -2.64907 | -51.75661 | 2024-10-30 04:44:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| ba4d092f-6749-3e1b-92ad-9177947a4a2e | -2.64681 | -51.74879 | 2024-10-30 04:44:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 64dc9290-c806-32dd-94c5-c658deff67d8 | -2.64624 | -51.75243 | 2024-10-30 04:44:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 9628ef0d-00f3-3b35-b6a0-5647cfd215d4 | -2.64566 | -51.75608 | 2024-10-30 04:44:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| a6ee017e-2e2a-32f2-83ee-f879cb73f6c8 | -2.64513 | -51.73732 | 2024-10-30 04:44:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 30a45cd4-a328-339b-b04c-06e3a4b28e42 | -2.64398 | -51.74461 | 2024-10-30 04:44:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 54cdce54-9693-3485-973c-18334529208e | -2.64341 | -51.74825 | 2024-10-30 04:44:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 7502906b-54d7-3788-9485-5d3a4d2917b8 | -2.64283 | -51.75189 | 2024-10-30 04:44:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 7327f48d-965c-38ae-87be-b7bec804bf7a | -2.6423 | -51.73315 | 2024-10-30 04:44:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| e14eea81-49da-3e57-a77f-1564c74e8802 | -2.64058 | -51.74407 | 2024-10-30 04:44:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| cf8a476c-fc4d-3b14-b6dd-4a7d346a4e36 | -2.64 | -51.74771 | 2024-10-30 04:44:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 614dd586-ed10-307f-86fe-c27d627553bc | -2.63948 | -51.72897 | 2024-10-30 04:44:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 55c4fdde-2311-30b5-9806-53b5c4f21c4e | -2.6389 | -51.73261 | 2024-10-30 04:44:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| d767e9c7-682f-3a19-a53d-9246e4702a14 | -2.63717 | -51.74353 | 2024-10-30 04:44:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 17e58688-1144-39c4-8a86-85d441602065 | -2.63607 | -51.72844 | 2024-10-30 04:44:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 76eb404a-bc00-31a8-8533-50f584cf003d | -2.58416 | -51.92317 | 2024-10-30 04:44:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 855695b8-f52a-3fd5-b1c7-6f9183a9b9ba | -2.58073 | -51.92264 | 2024-10-30 04:44:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 41b8eb05-2c9e-35bc-b4c4-4aa6a32ef5c9 | -2.55851 | -51.23079 | 2024-10-30 04:44:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 10999366-78a8-3a6b-bb2c-c6f4385db103 | -2.55515 | -51.23026 | 2024-10-30 04:44:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 74cb69de-1acf-35c1-9136-4f378a855237 | -2.50661 | -50.4714 | 2024-10-30 04:44:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 69129945-b3be-34b5-8369-143827a46eb9 | -2.48062 | -50.48506 | 2024-10-30 04:44:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 45003098-b673-38a5-8d4a-fc5690a82d99 | -2.48003 | -50.46725 | 2024-10-30 04:44:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 4750291c-6f2a-3683-9b31-9f89c5902fc7 | -2.4767 | -50.46674 | 2024-10-30 04:44:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| f5d3c90f-707e-37b9-8d65-ace4b28cfb42 | -2.56594 | -50.65076 | 2024-10-30 04:44:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 0384295c-5f85-3658-8717-fa7d07191c05 | -2.22248 | -51.87178 | 2024-10-30 04:44:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 4c4f0ef6-a6e5-3940-a01f-987a8626572f | -2.21295 | -51.55537 | 2024-10-30 04:44:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 2f70036c-bda3-365c-8787-05c928f1db29 | -2.1969 | -51.41616 | 2024-10-30 04:44:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |


[Clique aqui para ver as próximas entradas](README63.md)
