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

## Dados Diários - Página 123

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| df1378f5-9efb-32ee-ae9e-628721c7e8da | -7.78466 | -37.85831 | 2024-10-25 15:33:00 | NPP-375 | QUIXABA | PERNAMBUCO | Brasil | 2611533 | 26 | 33 | nan | nan | nan | Caatinga | 13.5 |
| 2dd92d7e-eebf-3255-a023-c13172d35de7 | -7.52447 | -37.89431 | 2024-10-25 15:33:00 | NPP-375 | JURU | PARAÍBA | Brasil | 2508000 | 25 | 33 | nan | nan | nan | Caatinga | 10.5 |
| a2650dba-4581-3f4f-adfe-0220566ce810 | -7.52385 | -37.88971 | 2024-10-25 15:33:00 | NPP-375 | JURU | PARAÍBA | Brasil | 2508000 | 25 | 33 | nan | nan | nan | Caatinga | 14.9 |
| 8c0340ff-ff69-3ebe-84be-524a0c5d5028 | -7.12784 | -38.3536 | 2024-10-25 15:33:00 | NPP-375 | SÃO JOSÉ DE PIRANHAS | PARAÍBA | Brasil | 2514503 | 25 | 33 | nan | nan | nan | Caatinga | 3.6 |
| 56573ac0-f91b-3a97-94c2-0e2ad8fe83f9 | -7.02196 | -38.10276 | 2024-10-25 15:33:00 | NPP-375 | AGUIAR | PARAÍBA | Brasil | 2500205 | 25 | 33 | nan | nan | nan | Caatinga | 20.4 |
| ef8de647-6534-3260-b723-c7032a034f06 | -6.77294 | -38.38279 | 2024-10-25 15:33:00 | NPP-375 | SÃO JOÃO DO RIO DO PEIXE | PARAÍBA | Brasil | 2500700 | 25 | 33 | nan | nan | nan | Caatinga | 5.6 |
| 1514c225-5246-3767-bbaa-b3c513452095 | -6.71576 | -37.50528 | 2024-10-25 15:33:00 | NPP-375 | SÃO JOSÉ DE ESPINHARAS | PARAÍBA | Brasil | 2514404 | 25 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 631e316b-104d-38b5-b164-ce7bb4359ebb | -7.78625 | -38.03796 | 2024-10-25 15:33:00 | NPP-375 | TRIUNFO | PERNAMBUCO | Brasil | 2615706 | 26 | 33 | nan | nan | nan | Caatinga | 9.6 |
| 5e26355f-1d20-3cea-9f1c-3f594a173aa3 | -7.71197 | -38.07305 | 2024-10-25 15:33:00 | NPP-375 | SÃO JOSÉ DE PRINCESA | PARAÍBA | Brasil | 2514552 | 25 | 33 | nan | nan | nan | Caatinga | 4.6 |
| 16ba5e63-ccb4-3c56-9ba4-03073e8bc612 | -7.25087 | -38.59978 | 2024-10-25 15:33:00 | NPP-375 | MAURITI | CEARÁ | Brasil | 2308104 | 23 | 33 | nan | nan | nan | Caatinga | 3.8 |
| f4161786-b7e2-3b81-ade5-303438f74fe3 | -7.1543 | -38.53959 | 2024-10-25 15:33:00 | NPP-375 | SÃO JOSÉ DE PIRANHAS | PARAÍBA | Brasil | 2514503 | 25 | 33 | nan | nan | nan | Caatinga | 5.4 |
| 7333f9f9-30b9-3d9d-9fc8-37b36ed1af19 | -7.13526 | -38.17953 | 2024-10-25 15:33:00 | NPP-375 | IGARACY | PARAÍBA | Brasil | 2502607 | 25 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 4f6fccf9-2724-3db5-9b0a-ab965fd386d1 | -6.58597 | -38.01494 | 2024-10-25 15:33:00 | NPP-375 | SANTA CRUZ | PARAÍBA | Brasil | 2513208 | 25 | 33 | nan | nan | nan | Caatinga | 9.3 |
| b56c17f9-e0ad-3dc1-8c90-685032a8867c | -6.54638 | -38.09819 | 2024-10-25 15:33:00 | NPP-375 | SANTA CRUZ | PARAÍBA | Brasil | 2513208 | 25 | 33 | nan | nan | nan | Caatinga | 8.5 |
| afcb86cf-aac0-315c-a848-c78f6a43dd93 | -7.72743 | -37.84706 | 2024-10-25 15:33:00 | NPP-375 | QUIXABA | PERNAMBUCO | Brasil | 2611533 | 26 | 33 | nan | nan | nan | Caatinga | 3.1 |
| 9761296c-fad0-3c84-b9c5-9b6e1adddeb8 | -7.67918 | -37.9389 | 2024-10-25 15:33:00 | NPP-375 | PRINCESA ISABEL | PARAÍBA | Brasil | 2512309 | 25 | 33 | nan | nan | nan | Caatinga | 3.7 |
| 3863da9c-4c7e-39f4-9984-a0d47c734354 | -7.52903 | -37.89373 | 2024-10-25 15:33:00 | NPP-375 | JURU | PARAÍBA | Brasil | 2508000 | 25 | 33 | nan | nan | nan | Caatinga | 47.6 |
| 266d4523-b8bd-3779-8e79-f9fb6075b1c0 | -7.02259 | -38.10731 | 2024-10-25 15:33:00 | NPP-375 | AGUIAR | PARAÍBA | Brasil | 2500205 | 25 | 33 | nan | nan | nan | Caatinga | 9.3 |
| 079cbd5c-64a5-3b77-8569-237aff71a3f7 | -6.63542 | -37.66413 | 2024-10-25 15:33:00 | NPP-375 | PAULISTA | PARAÍBA | Brasil | 2510907 | 25 | 33 | nan | nan | nan | Caatinga | 9.7 |
| 7595c397-741b-3051-ad25-376689c694b6 | -6.58533 | -38.01041 | 2024-10-25 15:33:00 | NPP-375 | SANTA CRUZ | PARAÍBA | Brasil | 2513208 | 25 | 33 | nan | nan | nan | Caatinga | 9.3 |
| c3227f7b-d04b-308b-8a74-3656f759d74d | -6.58084 | -38.01122 | 2024-10-25 15:33:00 | NPP-375 | SANTA CRUZ | PARAÍBA | Brasil | 2513208 | 25 | 33 | nan | nan | nan | Caatinga | 9.3 |
| c4a0765c-d4fb-37c1-ab5c-161bdb0da19e | -6.54613 | -38.09507 | 2024-10-25 15:33:00 | NPP-375 | SANTA CRUZ | PARAÍBA | Brasil | 2513208 | 25 | 33 | nan | nan | nan | Caatinga | 14.3 |
| f0725c8d-5c91-3f8c-b847-204132bd512b | -7.91909 | -37.98909 | 2024-10-25 15:33:00 | NPP-375 | FLORES | PERNAMBUCO | Brasil | 2605608 | 26 | 33 | nan | nan | nan | Caatinga | 12.7 |
| 38a54508-3e2c-3e98-86d8-8cc6e24478a5 | -7.53675 | -37.91617 | 2024-10-25 15:33:00 | NPP-375 | TAVARES | PARAÍBA | Brasil | 2516607 | 25 | 33 | nan | nan | nan | Caatinga | 6.1 |
| ed957543-48aa-3a32-9b61-4dbba66f63d7 | -7.53304 | -37.62482 | 2024-10-25 15:33:00 | NPP-375 | SOLIDÃO | PERNAMBUCO | Brasil | 2614402 | 26 | 33 | nan | nan | nan | Caatinga | 12.2 |
| 7111a62b-aa39-3c4f-8648-2126937ef3a6 | -7.52839 | -37.88904 | 2024-10-25 15:33:00 | NPP-375 | JURU | PARAÍBA | Brasil | 2508000 | 25 | 33 | nan | nan | nan | Caatinga | 60.0 |
| 41dda7ef-796a-39e0-97bf-eaccd17e20a6 | -6.68427 | -37.59608 | 2024-10-25 15:33:00 | NPP-375 | PAULISTA | PARAÍBA | Brasil | 2510907 | 25 | 33 | nan | nan | nan | Caatinga | 7.9 |
| 62483228-e0e1-33d0-809d-8aa094b39e6c | -7.37152 | -39.05893 | 2024-10-25 15:33:00 | NPP-375 | ABAIARA | CEARÁ | Brasil | 2300101 | 23 | 33 | nan | nan | nan | Caatinga | 2.5 |
| f1ff5254-e7b6-3541-9b9f-f138c3b708b1 | -7.36659 | -39.0595 | 2024-10-25 15:33:00 | NPP-375 | ABAIARA | CEARÁ | Brasil | 2300101 | 23 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 5fd7ef39-f83c-342e-970f-1a5483eedc6a | -7.35654 | -39.0966 | 2024-10-25 15:33:00 | NPP-375 | ABAIARA | CEARÁ | Brasil | 2300101 | 23 | 33 | nan | nan | nan | Caatinga | 4.3 |
| 6ed0728e-7825-345e-80d4-0644b53da3ff | -7.26032 | -38.73699 | 2024-10-25 15:33:00 | NPP-375 | MAURITI | CEARÁ | Brasil | 2308104 | 23 | 33 | nan | nan | nan | Caatinga | 5.1 |
| 6016b3fe-c6b3-376c-aece-1c8a5d72c89f | -7.15587 | -38.54176 | 2024-10-25 15:33:00 | NPP-375 | SÃO JOSÉ DE PIRANHAS | PARAÍBA | Brasil | 2514503 | 25 | 33 | nan | nan | nan | Caatinga | 3.5 |
| 82b9429b-7497-391d-844a-1d7624fb85da | -7.08045 | -39.01691 | 2024-10-25 15:33:00 | NPP-375 | AURORA | CEARÁ | Brasil | 2301703 | 23 | 33 | nan | nan | nan | Caatinga | 5.4 |
| 02ca872e-9219-3ded-a443-e09dcced1d56 | -7.59916 | -39.05099 | 2024-10-25 15:33:00 | NPP-375 | PORTEIRAS | CEARÁ | Brasil | 2311108 | 23 | 33 | nan | nan | nan | Caatinga | 9.3 |
| 927a3b3e-2eaf-3c04-874e-c4b39101110b | -7.46492 | -38.77626 | 2024-10-25 15:33:00 | NPP-375 | MAURITI | CEARÁ | Brasil | 2308104 | 23 | 33 | nan | nan | nan | Caatinga | 2.8 |
| 4bf99ccf-c99a-393a-bf19-96e6b528ca55 | -7.15518 | -38.53661 | 2024-10-25 15:33:00 | NPP-375 | SÃO JOSÉ DE PIRANHAS | PARAÍBA | Brasil | 2514503 | 25 | 33 | nan | nan | nan | Caatinga | 4.8 |
| ebebb6eb-666d-3964-beb9-0d41c8ac611b | -9.24424 | -38.58247 | 2024-10-25 15:33:00 | NPP-375 | GLÓRIA | BAHIA | Brasil | 2911402 | 29 | 33 | nan | nan | nan | Caatinga | 6.9 |
| 3a26b612-639a-3d5f-a0f7-ee17101404c3 | -8.17478 | -38.18451 | 2024-10-25 15:33:00 | NPP-375 | SERRA TALHADA | PERNAMBUCO | Brasil | 2613909 | 26 | 33 | nan | nan | nan | Caatinga | 13.4 |
| 84a25606-ddf0-3fb7-b706-dfc51d483808 | -8.17548 | -38.18947 | 2024-10-25 15:33:00 | NPP-375 | SERRA TALHADA | PERNAMBUCO | Brasil | 2613909 | 26 | 33 | nan | nan | nan | Caatinga | 13.4 |
| b053de47-fced-3ed1-b7ff-c7070d98704a | -8.17275 | -38.18828 | 2024-10-25 15:33:00 | NPP-375 | SERRA TALHADA | PERNAMBUCO | Brasil | 2613909 | 26 | 33 | nan | nan | nan | Caatinga | 16.9 |
| 78b6b959-f1f4-3874-af6f-72173f855da9 | -9.97867 | -38.56224 | 2024-10-25 15:33:00 | NPP-375 | JEREMOABO | BAHIA | Brasil | 2918100 | 29 | 33 | nan | nan | nan | Caatinga | 6.8 |
| b152fbe5-8d31-39d8-bcbc-69faa37f6150 | -10.30517 | -39.32374 | 2024-10-25 15:33:00 | NPP-375 | MONTE SANTO | BAHIA | Brasil | 2921500 | 29 | 33 | nan | nan | nan | Caatinga | 9.4 |
| 2d63cb7a-66cb-3a0a-ab68-8401e3e25e98 | -10.30475 | -39.32048 | 2024-10-25 15:33:00 | NPP-375 | MONTE SANTO | BAHIA | Brasil | 2921500 | 29 | 33 | nan | nan | nan | Caatinga | 9.4 |
| d012762e-0932-305e-a1a9-043a8ce11fd2 | -10.08882 | -39.42039 | 2024-10-25 15:33:00 | NPP-375 | UAUÁ | BAHIA | Brasil | 2932002 | 29 | 33 | nan | nan | nan | Caatinga | 8.6 |
| 69b23157-8f06-3ec4-a44c-5e909c06087e | -10.0779 | -38.50791 | 2024-10-25 15:33:00 | NPP-375 | JEREMOABO | BAHIA | Brasil | 2918100 | 29 | 33 | nan | nan | nan | Caatinga | 6.7 |
| 23a75d96-f2c2-364c-b7c9-041b84785e57 | -4.98914 | -39.8539 | 2024-10-25 15:33:00 | NPP-375 | BOA VIAGEM | CEARÁ | Brasil | 2302404 | 23 | 33 | nan | nan | nan | Caatinga | 21.7 |
| 4a466974-9536-3a0b-a81f-be1d05535d63 | -4.98863 | -39.85184 | 2024-10-25 15:33:00 | NPP-375 | BOA VIAGEM | CEARÁ | Brasil | 2302404 | 23 | 33 | nan | nan | nan | Caatinga | 25.3 |
| 5ce671ff-fb45-3120-a7af-4ecd05c9e044 | -4.98828 | -39.84805 | 2024-10-25 15:33:00 | NPP-375 | BOA VIAGEM | CEARÁ | Brasil | 2302404 | 23 | 33 | nan | nan | nan | Caatinga | 21.7 |
| 06910a3e-f9c0-39ff-bc55-f86ea883cabc | -4.98782 | -39.84599 | 2024-10-25 15:33:00 | NPP-375 | BOA VIAGEM | CEARÁ | Brasil | 2302404 | 23 | 33 | nan | nan | nan | Caatinga | 18.3 |
| feeef3bc-078a-3eb5-98ff-91c86deca13e | -4.91941 | -39.90351 | 2024-10-25 15:33:00 | NPP-375 | BOA VIAGEM | CEARÁ | Brasil | 2302404 | 23 | 33 | nan | nan | nan | Caatinga | 11.4 |
| fb5d52ed-f339-3e6a-8849-d0ecf6f6b817 | -4.91859 | -39.89763 | 2024-10-25 15:33:00 | NPP-375 | BOA VIAGEM | CEARÁ | Brasil | 2302404 | 23 | 33 | nan | nan | nan | Caatinga | 13.8 |
| 134f9f69-8ffb-3bbf-b0be-50802cd285be | -4.82134 | -39.92699 | 2024-10-25 15:33:00 | NPP-375 | BOA VIAGEM | CEARÁ | Brasil | 2302404 | 23 | 33 | nan | nan | nan | Caatinga | 43.5 |
| 9fc68180-ed3f-3e13-8f58-c34cce4abd8c | -4.76328 | -40.01928 | 2024-10-25 15:33:00 | NPP-375 | MONSENHOR TABOSA | CEARÁ | Brasil | 2308609 | 23 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 444dfc95-9f82-330c-ae20-fc77c58c9e7c | -4.73916 | -40.06734 | 2024-10-25 15:33:00 | NPP-375 | MONSENHOR TABOSA | CEARÁ | Brasil | 2308609 | 23 | 33 | nan | nan | nan | Caatinga | 2.4 |
| aad242dd-5f81-31c5-a110-f8c1d63cd5ab | -4.7341 | -40.06813 | 2024-10-25 15:33:00 | NPP-375 | MONSENHOR TABOSA | CEARÁ | Brasil | 2308609 | 23 | 33 | nan | nan | nan | Caatinga | 26.1 |
| fc225e12-8f02-30bc-bb5b-940fffdefa5d | -4.71693 | -39.29486 | 2024-10-25 15:33:00 | NPP-375 | CHORÓ | CEARÁ | Brasil | 2303931 | 23 | 33 | nan | nan | nan | Caatinga | 4.0 |
| e5fa8302-20d9-31ed-b1e6-12b5ec4f9fbc | -4.70901 | -39.96338 | 2024-10-25 15:33:00 | NPP-375 | SANTA QUITÉRIA | CEARÁ | Brasil | 2312205 | 23 | 33 | nan | nan | nan | Caatinga | 29.2 |
| e2f8bbf3-072d-364b-bcb0-e4b5ebc2c33f | -4.62876 | -39.39569 | 2024-10-25 15:33:00 | NPP-375 | CANINDÉ | CEARÁ | Brasil | 2302800 | 23 | 33 | nan | nan | nan | Caatinga | 13.0 |
| 7f262f67-fa2c-3eb9-acb4-2fc75635c568 | -4.62393 | -39.39639 | 2024-10-25 15:33:00 | NPP-375 | CANINDÉ | CEARÁ | Brasil | 2302800 | 23 | 33 | nan | nan | nan | Caatinga | 13.0 |
| b42fd0bb-a942-39da-b627-1dd61b24efc5 | -4.20418 | -39.73737 | 2024-10-25 15:33:00 | NPP-375 | CANINDÉ | CEARÁ | Brasil | 2302800 | 23 | 33 | nan | nan | nan | Caatinga | 41.4 |
| 424a5947-c2df-3c91-beb9-c5b99004d84a | -4.20328 | -39.73975 | 2024-10-25 15:33:00 | NPP-375 | CANINDÉ | CEARÁ | Brasil | 2302800 | 23 | 33 | nan | nan | nan | Caatinga | 34.9 |
| 95080b29-1e8d-3b03-aad1-b71332390bea | -5.50667 | -39.13339 | 2024-10-25 15:33:00 | NPP-375 | QUIXERAMOBIM | CEARÁ | Brasil | 2311405 | 23 | 33 | nan | nan | nan | Caatinga | 8.0 |
| ae992777-aa5c-309e-a154-59a5e65a22a0 | -5.39371 | -40.01677 | 2024-10-25 15:33:00 | NPP-375 | PEDRA BRANCA | CEARÁ | Brasil | 2310506 | 23 | 33 | nan | nan | nan | Caatinga | 3.8 |
| 9a63a6d6-b8c1-3f4c-b3d3-20cc18162db1 | -5.36667 | -40.23649 | 2024-10-25 15:33:00 | NPP-375 | INDEPENDÊNCIA | CEARÁ | Brasil | 2305605 | 23 | 33 | nan | nan | nan | Caatinga | 13.1 |
| 37c1aedc-a68b-31f6-ba41-9577157b9274 | -5.36625 | -40.2334 | 2024-10-25 15:33:00 | NPP-375 | INDEPENDÊNCIA | CEARÁ | Brasil | 2305605 | 23 | 33 | nan | nan | nan | Caatinga | 14.2 |
| c756eebb-24cd-3a4f-b6e7-32294684c890 | -5.3658 | -40.23537 | 2024-10-25 15:33:00 | NPP-375 | INDEPENDÊNCIA | CEARÁ | Brasil | 2305605 | 23 | 33 | nan | nan | nan | Caatinga | 19.4 |
| c161d5a8-4999-374a-9cdf-6f2f3314e941 | -5.33085 | -39.71731 | 2024-10-25 15:33:00 | NPP-375 | BOA VIAGEM | CEARÁ | Brasil | 2302404 | 23 | 33 | nan | nan | nan | Caatinga | 11.5 |
| c4bc5fd5-6f11-340a-8bd2-92e42a88b7e5 | -5.08377 | -40.08836 | 2024-10-25 15:33:00 | NPP-375 | MONSENHOR TABOSA | CEARÁ | Brasil | 2308609 | 23 | 33 | nan | nan | nan | Caatinga | 4.9 |
| 48f56672-3573-3edf-aa2c-9f5aa690f9a9 | -5.04412 | -39.59233 | 2024-10-25 15:33:00 | NPP-375 | MADALENA | CEARÁ | Brasil | 2307635 | 23 | 33 | nan | nan | nan | Caatinga | 5.6 |
| 7337bb1c-fb8f-361f-ad64-d44b96f10ab9 | -5.04327 | -39.59338 | 2024-10-25 15:33:00 | NPP-375 | MADALENA | CEARÁ | Brasil | 2307635 | 23 | 33 | nan | nan | nan | Caatinga | 4.9 |
| cd2ba653-93d9-323d-a33a-ebb2bac53e43 | -6.35379 | -40.12506 | 2024-10-25 15:33:00 | NPP-375 | AIUABA | CEARÁ | Brasil | 2300408 | 23 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 5ae45386-de42-3549-b8f3-b4b4ef6a3f1c | -6.0649 | -38.95638 | 2024-10-25 15:33:00 | NPP-375 | JAGUARIBE | CEARÁ | Brasil | 2306900 | 23 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 9e3371dc-dbb8-39a5-b121-9cc306ffd5cf | -5.76911 | -40.05969 | 2024-10-25 15:33:00 | NPP-375 | TAUÁ | CEARÁ | Brasil | 2313302 | 23 | 33 | nan | nan | nan | Caatinga | 3.3 |
| 603220c7-453f-3d3c-82c3-685fec193ecf | -5.76761 | -40.05885 | 2024-10-25 15:33:00 | NPP-375 | TAUÁ | CEARÁ | Brasil | 2313302 | 23 | 33 | nan | nan | nan | Caatinga | 4.3 |
| 2519c83e-6eda-3c46-85bd-74b01ea0ce8c | -7.98884 | -39.76276 | 2024-10-25 15:33:00 | NPP-375 | PARNAMIRIM | PERNAMBUCO | Brasil | 2610400 | 26 | 33 | nan | nan | nan | Caatinga | 8.7 |
| 11572d6b-9d9b-3f1f-89c4-4bedaacaa5bb | -7.98842 | -39.75961 | 2024-10-25 15:33:00 | NPP-375 | PARNAMIRIM | PERNAMBUCO | Brasil | 2610400 | 26 | 33 | nan | nan | nan | Caatinga | 13.2 |
| 5c6a936e-2c4c-3bcd-8da3-ceebfca5a5c8 | -7.85535 | -39.64062 | 2024-10-25 15:33:00 | NPP-375 | GRANITO | PERNAMBUCO | Brasil | 2606309 | 26 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 392c2d07-aae4-371c-9bad-b2bd79ef342c | -7.3686 | -39.14902 | 2024-10-25 15:33:00 | NPP-375 | MISSÃO VELHA | CEARÁ | Brasil | 2308401 | 23 | 33 | nan | nan | nan | Caatinga | 4.0 |
| 4cc40bc5-dd71-371e-8ab2-a0bf0b9718e6 | -6.6798 | -39.9033 | 2024-10-25 15:33:00 | NPP-375 | SABOEIRO | CEARÁ | Brasil | 2311900 | 23 | 33 | nan | nan | nan | Caatinga | 5.3 |
| aedf6e6c-8f0a-30fa-a238-30034143f8c5 | -6.5677 | -39.86248 | 2024-10-25 15:33:00 | NPP-375 | SABOEIRO | CEARÁ | Brasil | 2311900 | 23 | 33 | nan | nan | nan | Caatinga | 5.4 |
| fcaab76f-16c8-3fb0-81a6-1bb959d93871 | -6.60339 | -39.20068 | 2024-10-25 15:33:00 | NPP-375 | CEDRO | CEARÁ | Brasil | 2303808 | 23 | 33 | nan | nan | nan | Caatinga | 1.8 |
| c566e506-52da-33da-9c60-462dca382010 | -6.56727 | -39.85942 | 2024-10-25 15:33:00 | NPP-375 | SABOEIRO | CEARÁ | Brasil | 2311900 | 23 | 33 | nan | nan | nan | Caatinga | 5.4 |
| f5875dd8-39c7-3d69-8832-f31d00c6ee5d | -7.39716 | -40.3076 | 2024-10-25 15:33:00 | NPP-375 | IPUBI | PERNAMBUCO | Brasil | 2607307 | 26 | 33 | nan | nan | nan | Caatinga | 10.2 |
| 1c794e26-abee-32c0-b310-09c174b3c65d | -7.32301 | -40.40693 | 2024-10-25 15:33:00 | NPP-375 | SALITRE | CEARÁ | Brasil | 2311959 | 23 | 33 | nan | nan | nan | Caatinga | 12.6 |
| 8da395ac-87b4-3d64-a939-f84b3e7a70cc | -7.31722 | -40.40461 | 2024-10-25 15:33:00 | NPP-375 | SALITRE | CEARÁ | Brasil | 2311959 | 23 | 33 | nan | nan | nan | Caatinga | 8.2 |
| 8129716b-b826-38d8-b3c2-d0109dde22e7 | -7.07341 | -40.31453 | 2024-10-25 15:33:00 | NPP-375 | CAMPOS SALES | CEARÁ | Brasil | 2302701 | 23 | 33 | nan | nan | nan | Caatinga | 1.6 |
| afefd230-2bdf-3311-8256-496038402cd1 | -7.07086 | -40.31506 | 2024-10-25 15:33:00 | NPP-375 | CAMPOS SALES | CEARÁ | Brasil | 2302701 | 23 | 33 | nan | nan | nan | Caatinga | 1.5 |
| a7246524-f50b-3cc5-8885-1b981337b529 | -7.39522 | -40.31035 | 2024-10-25 15:33:00 | NPP-375 | IPUBI | PERNAMBUCO | Brasil | 2607307 | 26 | 33 | nan | nan | nan | Caatinga | 7.3 |
| b6cb44b5-dd43-3573-9bb2-24940b35d7ef | -7.70577 | -40.34502 | 2024-10-25 15:33:00 | NPP-375 | TRINDADE | PERNAMBUCO | Brasil | 2615607 | 26 | 33 | nan | nan | nan | Caatinga | 9.1 |
| 2c05f920-ccad-3a68-a431-eae8d821e679 | -7.69573 | -40.17001 | 2024-10-25 15:33:00 | NPP-375 | IPUBI | PERNAMBUCO | Brasil | 2607307 | 26 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 3826babf-69a7-3564-b12a-e69fbc4e9b21 | -7.68607 | -40.61176 | 2024-10-25 15:33:00 | NPP-375 | ARARIPINA | PERNAMBUCO | Brasil | 2601102 | 26 | 33 | nan | nan | nan | Caatinga | 6.1 |
| d26b2827-45b9-3871-b579-84e12872f3c5 | -7.39764 | -40.31106 | 2024-10-25 15:33:00 | NPP-375 | IPUBI | PERNAMBUCO | Brasil | 2607307 | 26 | 33 | nan | nan | nan | Caatinga | 7.0 |
| 10d3a89d-94c2-319b-a014-a29c7ddf7694 | -7.87127 | -39.40855 | 2024-10-25 15:33:00 | NPP-375 | SERRITA | PERNAMBUCO | Brasil | 2614006 | 26 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 340ba200-5047-3c35-9a0c-115e22fb38bc | -7.8685 | -39.66064 | 2024-10-25 15:33:00 | NPP-375 | GRANITO | PERNAMBUCO | Brasil | 2606309 | 26 | 33 | nan | nan | nan | Caatinga | 1.3 |
| adf4ca2a-e234-333d-b905-d9554a32cd3f | -7.48647 | -39.48885 | 2024-10-25 15:33:00 | NPP-375 | MOREILÂNDIA | PERNAMBUCO | Brasil | 2614303 | 26 | 33 | nan | nan | nan | Caatinga | 3.1 |
| 01a73278-1af2-37e7-8793-789b27648bc4 | -8.03205 | -39.46023 | 2024-10-25 15:33:00 | NPP-375 | SERRITA | PERNAMBUCO | Brasil | 2614006 | 26 | 33 | nan | nan | nan | Caatinga | 2.8 |
| b2839318-ee53-3192-a873-c1b865876636 | -7.88719 | -40.00667 | 2024-10-25 15:33:00 | NPP-375 | OURICURI | PERNAMBUCO | Brasil | 2609907 | 26 | 33 | nan | nan | nan | Caatinga | 5.7 |
| 5b3c4f35-4810-310d-ab7f-92bc3f04553f | -7.88677 | -40.00343 | 2024-10-25 15:33:00 | NPP-375 | OURICURI | PERNAMBUCO | Brasil | 2609907 | 26 | 33 | nan | nan | nan | Caatinga | 5.7 |
| 5caa2742-9d24-3f21-aeb4-a97998d4d5c4 | -7.88374 | -40.0085 | 2024-10-25 15:33:00 | NPP-375 | OURICURI | PERNAMBUCO | Brasil | 2609907 | 26 | 33 | nan | nan | nan | Caatinga | 6.6 |
| f0bc8875-5989-39a9-8fa2-b33c686afdaa | -7.8833 | -40.00526 | 2024-10-25 15:33:00 | NPP-375 | OURICURI | PERNAMBUCO | Brasil | 2609907 | 26 | 33 | nan | nan | nan | Caatinga | 6.6 |


[Clique aqui para ver as próximas entradas](README124.md)
