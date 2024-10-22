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

## Dados Diários - Página 17

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 2a32dc44-daeb-3088-b2c4-775c4204d434 | -6.72646 | -40.47843 | 2024-10-22 03:53:00 | NPP-375D | AIUABA | CEARÁ | Brasil | 2300408 | 23 | 33 | nan | nan | nan | Caatinga | 2.4 |
| c7863c95-a765-3541-81ca-cb04d98aeb6c | -6.72585 | -40.48224 | 2024-10-22 03:53:00 | NPP-375D | AIUABA | CEARÁ | Brasil | 2300408 | 23 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 9f982cf3-5e41-3b2e-914d-d6cfc362acc1 | -6.72543 | -40.46268 | 2024-10-22 03:53:00 | NPP-375D | AIUABA | CEARÁ | Brasil | 2300408 | 23 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 73586a3a-5042-3342-b3a7-7d4325fcb0b7 | -6.72482 | -40.46648 | 2024-10-22 03:53:00 | NPP-375D | AIUABA | CEARÁ | Brasil | 2300408 | 23 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 7dc3c39b-9e83-375c-8b54-df9b3144af41 | -6.7236 | -40.47408 | 2024-10-22 03:53:00 | NPP-375D | AIUABA | CEARÁ | Brasil | 2300408 | 23 | 33 | nan | nan | nan | Caatinga | 2.4 |
| a6d78baf-0a61-3271-9b2f-c162562f6ea1 | -6.72239 | -40.48169 | 2024-10-22 03:53:00 | NPP-375D | AIUABA | CEARÁ | Brasil | 2300408 | 23 | 33 | nan | nan | nan | Caatinga | 1.3 |
| a64d996f-2afd-37f8-ba11-ecd979026ad3 | -6.57941 | -39.716 | 2024-10-22 03:53:00 | NPP-375D | JUCÁS | CEARÁ | Brasil | 2307403 | 23 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 564d9210-2c5d-3fe9-891a-279a567af3a3 | -5.12558 | -41.06309 | 2024-10-22 03:53:00 | NPP-375D | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| e8a019e1-91f9-3c61-ad4b-e1af641d2852 | -9.03842 | -41.99626 | 2024-10-22 03:53:00 | NPP-375D | DOM INOCÊNCIO | PIAUÍ | Brasil | 2203453 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 50a46d15-c4b8-3ba0-b33c-73007321cce2 | -12.67062 | -42.70943 | 2024-10-22 03:55:00 | NPP-375D | BOQUIRA | BAHIA | Brasil | 2904100 | 29 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 911a1c74-16f1-3979-9457-3671f7115164 | -11.91762 | -44.61281 | 2024-10-22 03:55:00 | NPP-375D | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| d0b389cb-6252-3f43-addb-5b3595591fcd | -10.75819 | -45.01922 | 2024-10-22 03:55:00 | NPP-375D | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 2dbb785c-6648-374f-a47c-a17aba3d17f6 | -10.51809 | -44.85825 | 2024-10-22 03:55:00 | NPP-375D | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| ffff0f91-a034-30bd-9935-f1be408442ac | -10.44688 | -44.89345 | 2024-10-22 03:55:00 | NPP-375D | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 3446f36d-a318-3aa0-ac05-9a698d2f1ecc | -10.44618 | -44.89737 | 2024-10-22 03:55:00 | NPP-375D | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 6d0e3ff2-be4e-34d4-bfab-7e397cffbe88 | -10.44196 | -44.89668 | 2024-10-22 03:55:00 | NPP-375D | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 5f98c7ea-53a9-3b28-8994-3b9240c71196 | -12.21941 | -47.27446 | 2024-10-22 03:55:00 | NPP-375D | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| fc9c2f34-38c0-39cd-9f49-d62f0a7e3722 | -12.21462 | -47.27358 | 2024-10-22 03:55:00 | NPP-375D | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| cd16584a-aab9-369a-a970-125ce030fd69 | -12.10808 | -48.3041 | 2024-10-22 03:55:00 | NPP-375D | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 585b20d9-68f7-3522-8e57-11ff1a2791c1 | -12.10747 | -48.30724 | 2024-10-22 03:55:00 | NPP-375D | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| d9bd65a5-564b-31fd-9326-58f0c2b49564 | -12.07524 | -47.98891 | 2024-10-22 03:55:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 240ad782-4e33-3c9f-8682-b082c04ae71d | -12.07021 | -47.98796 | 2024-10-22 03:55:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 1a92028d-5006-397e-9fe0-9c855a5f5ba7 | -16.75116 | -50.76459 | 2024-10-22 03:55:00 | NPP-375D | CACHOEIRA DE GOIÁS | GOIÁS | Brasil | 5204201 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 00b07286-41a4-3c84-9567-0d05d92426b1 | -11.73263 | -37.61366 | 2024-10-22 03:55:00 | NPP-375D | CONDE | BAHIA | Brasil | 2908606 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| 2eb3476f-1cbd-3980-9cff-c4180e751b42 | -11.73207 | -37.6174 | 2024-10-22 03:55:00 | NPP-375D | CONDE | BAHIA | Brasil | 2908606 | 29 | 33 | nan | nan | nan | Mata Atlântica | 2.4 |
| 477a2b6b-20c2-3b0a-b1a0-f714b49bd1be | -11.72958 | -37.61392 | 2024-10-22 03:55:00 | NPP-375D | CONDE | BAHIA | Brasil | 2908606 | 29 | 33 | nan | nan | nan | Mata Atlântica | 3.8 |
| 6d901bec-a8f6-3345-9e55-5d2914560d0f | -11.7292 | -37.61315 | 2024-10-22 03:55:00 | NPP-375D | CONDE | BAHIA | Brasil | 2908606 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| ca7c7ca7-5fd1-379c-b219-97bc56b52f19 | -11.72864 | -37.61689 | 2024-10-22 03:55:00 | NPP-375D | CONDE | BAHIA | Brasil | 2908606 | 29 | 33 | nan | nan | nan | Mata Atlântica | 2.4 |
| c0c63b76-7304-3150-adcc-970c35d83fd2 | -12.77928 | -38.49962 | 2024-10-22 03:55:00 | NPP-375D | CANDEIAS | BAHIA | Brasil | 2906501 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| eaff810f-7258-331b-943e-48c739d5eaec | -12.13546 | -39.39921 | 2024-10-22 03:55:00 | NPP-375D | SERRA PRETA | BAHIA | Brasil | 2930402 | 29 | 33 | nan | nan | nan | Caatinga | 0.9 |
| d60925fc-b6d6-3943-acbf-664133c619b5 | -13.06328 | -39.93007 | 2024-10-22 03:55:00 | NPP-375D | BREJÕES | BAHIA | Brasil | 2904308 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 36c6dab9-4c3e-3a70-98cb-b87459b4ac95 | -13.06272 | -39.93361 | 2024-10-22 03:55:00 | NPP-375D | BREJÕES | BAHIA | Brasil | 2904308 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 96c009b2-48a3-325d-a050-1d62b9bd1039 | -12.54643 | -38.99674 | 2024-10-22 03:55:00 | NPP-375D | CONCEIÇÃO DA FEIRA | BAHIA | Brasil | 2908200 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| d88a914c-ef54-308f-a3ca-8d664619ce0b | -13.3901 | -40.47171 | 2024-10-22 03:55:00 | NPP-375D | MARACÁS | BAHIA | Brasil | 2920502 | 29 | 33 | nan | nan | nan | Mata Atlântica | 4.2 |
| d55e6b48-29ac-32d4-adb7-f06a17dc8d6f | -13.37941 | -40.60255 | 2024-10-22 03:55:00 | NPP-375D | MARACÁS | BAHIA | Brasil | 2920502 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 56d84f68-5b89-32e1-9b90-63720f912006 | -15.49879 | -41.28738 | 2024-10-22 03:55:00 | NPP-375D | CÂNDIDO SALES | BAHIA | Brasil | 2906709 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 49735e2d-6bc5-3f74-bbe9-ead2cad4abe5 | -1.165 | -53.6571 | 2024-10-22 03:55:13 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 59.2 |
| 735c4fef-ce87-3db6-a4b1-8ca391f16171 | -1.1834 | -53.6569 | 2024-10-22 03:55:13 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 49.8 |
| 23fdddda-d32b-3fcd-8cb9-ade37748110b | -2.4824 | -49.1233 | 2024-10-22 03:55:20 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 56.4 |
| 1996c4b2-2b17-3fbb-9736-e24629b7e7e8 | -2.4824 | -49.102 | 2024-10-22 03:55:20 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 50.8 |
| f86ec86e-22dd-3003-aa8c-56ae49dc80da | -2.7588 | -49.3285 | 2024-10-22 03:55:22 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 98.3 |
| bbee5c61-06ca-3e3e-a117-c5ddfa7eb024 | -2.7589 | -49.3072 | 2024-10-22 03:55:22 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 99.5 |
| b972db95-2c51-31a4-b062-e0ef44e97421 | -2.7773 | -49.3279 | 2024-10-22 03:55:22 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 69.9 |
| d4e662bc-d272-3a3a-9c86-1a482e92bebf | -2.7773 | -49.3067 | 2024-10-22 03:55:22 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 63.4 |
| 8785dc1f-7c7b-35e1-bfa2-28c1e69b10f2 | -3.0917 | -54.1867 | 2024-10-22 03:55:24 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 54.8 |
| 6ecbe64c-a282-38fc-8c7b-4fb36b34c128 | -3.0917 | -54.1666 | 2024-10-22 03:55:24 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 100.8 |
| 44af9411-57d0-324c-b1ca-8d4532ea365a | -3.0918 | -54.1465 | 2024-10-22 03:55:24 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 55.4 |
| de4290a3-e2fa-30ff-861d-7bf821a1225e | -3.1101 | -54.1661 | 2024-10-22 03:55:24 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 75.8 |
| 694c1bf3-67da-31c2-a7fa-0f26cfec063e | -23.40644 | -46.55622 | 2024-10-22 03:57:00 | NPP-375D | GUARULHOS | SÃO PAULO | Brasil | 3518800 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 346aeb9c-9484-3cc4-b326-edd247f8e970 | -23.33848 | -46.7712 | 2024-10-22 03:57:00 | NPP-375D | CAIEIRAS | SÃO PAULO | Brasil | 3509007 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| aca22809-fa8f-345e-a373-1502549281b6 | -16.96495 | -52.02152 | 2024-10-22 03:57:00 | NPP-375D | CAIAPÔNIA | GOIÁS | Brasil | 5204409 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 4fe208b2-0155-38fd-8ee3-df7123c4428a | -16.96396 | -52.02605 | 2024-10-22 03:57:00 | NPP-375D | CAIAPÔNIA | GOIÁS | Brasil | 5204409 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 4c8d3535-61db-3017-9fd9-cdf2806a1e64 | -17.98271 | -52.79878 | 2024-10-22 03:57:00 | NPP-375D | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 4e4f52f7-de3e-3cf7-a82b-d8c7bb24e3d8 | -17.97668 | -52.79714 | 2024-10-22 03:57:00 | NPP-375D | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| ec361864-135e-37e0-a48f-b871678df3ad | -22.30451 | -41.88234 | 2024-10-22 03:57:00 | NPP-375D | MACAÉ | RIO DE JANEIRO | Brasil | 3302403 | 33 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| 67484421-e739-3cd2-a2fd-10c06adc42e7 | -21.91338 | -42.26144 | 2024-10-22 03:57:00 | NPP-375D | CANTAGALO | RIO DE JANEIRO | Brasil | 3301108 | 33 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 3740a8fd-7f89-3994-9ed6-5c968d0be104 | -22.9007 | -43.75189 | 2024-10-22 03:57:00 | NPP-375D | RIO DE JANEIRO | RIO DE JANEIRO | Brasil | 3304557 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| 40dc0261-598b-3242-96f7-4555ebdffb6e | -29.81685 | -51.17616 | 2024-10-22 04:00:00 | NPP-375D | SAPUCAIA DO SUL | RIO GRANDE DO SUL | Brasil | 4320008 | 43 | 33 | nan | nan | nan | Pampa | 0.8 |
| 66347303-347d-3ff7-884a-bb8ba35e6b2b | -29.81253 | -51.17491 | 2024-10-22 04:00:00 | NPP-375D | SAPUCAIA DO SUL | RIO GRANDE DO SUL | Brasil | 4320008 | 43 | 33 | nan | nan | nan | Pampa | 0.8 |
| 92c82f54-62e2-3f8a-be00-b8d2f79dbd89 | -1.1834 | -53.6569 | 2024-10-22 04:05:13 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 49.2 |
| fdf06675-0e4b-3a09-a520-6d26beac1101 | -2.7589 | -49.3072 | 2024-10-22 04:05:22 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 71.8 |
| 921390c6-0ecd-38bc-8dd3-a4d5cae045f7 | -2.7588 | -49.3285 | 2024-10-22 04:05:22 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 85.3 |
| 263b42c5-ddb5-3aa7-b649-8f6e44fe4422 | -3.1101 | -54.1661 | 2024-10-22 04:05:24 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 54.6 |
| 1e36f593-406f-3e49-9f1d-c1f3749c991a | -3.0917 | -54.1666 | 2024-10-22 04:05:24 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 56.2 |
| c41d72d6-80d9-38d3-8202-2982619c9c68 | -5.5905 | -44.8687 | 2024-10-22 04:05:38 | GOES-16 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 42.7 |
| 428f1a35-c087-3e89-b800-00c7e790b578 | -9.9914 | -36.1142 | 2024-10-22 04:06:01 | GOES-16 | CORURIPE | ALAGOAS | Brasil | 2702306 | 27 | 33 | nan | nan | nan | Mata Atlântica | 68.2 |
| d7eb96c4-0720-3012-af1e-4631b77ad5a9 | -17.0184 | -57.5178 | 2024-10-22 04:06:42 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 88.4 |
| 81532555-42bc-3049-9bd1-0ad0f98ae024 | -1.1834 | -53.6569 | 2024-10-22 04:15:13 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 49.7 |
| 9b30fd73-e571-3ab6-804c-9ab47c660d3d | -2.7773 | -49.3067 | 2024-10-22 04:15:22 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 53.3 |
| a839b8e3-d1a8-357f-8f9c-736d390c447b | -2.7588 | -49.3285 | 2024-10-22 04:15:22 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 85.6 |
| f6101aa9-4492-3986-b9cd-7cb28854aa91 | -2.7589 | -49.3072 | 2024-10-22 04:15:22 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 89.8 |
| c0c1082b-2a96-3bd5-a1c2-54e9df3f9512 | -5.5718 | -44.87 | 2024-10-22 04:15:38 | GOES-16 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 58.5 |
| fd5a82b6-b073-335c-adad-d19ece700b36 | -5.5903 | -44.8914 | 2024-10-22 04:15:38 | GOES-16 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 42.9 |
| 861595ed-6b59-38ab-8b88-72a2a38c2f0e | -5.5905 | -44.8687 | 2024-10-22 04:15:38 | GOES-16 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 78.5 |
| 5b4fccd5-4f02-31bc-bbe6-50621beae60f | -5.23509 | -41.94283 | 2024-10-22 04:17:00 | NOAA-20 | NOVO SANTO ANTÔNIO | PIAUÍ | Brasil | 2206951 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 916fcb9f-d8cb-3d7b-9a48-0eb9e2971e94 | -5.23208 | -43.18612 | 2024-10-22 04:17:00 | NOAA-20 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 1fe0a23d-056d-397e-87cb-37bafd2f6a6e | -5.23153 | -43.18966 | 2024-10-22 04:17:00 | NOAA-20 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 07c7277f-d548-3edf-aa85-1020da9a7719 | -5.22984 | -43.17849 | 2024-10-22 04:17:00 | NOAA-20 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 09e04314-75a5-3fda-894d-43558306393c | -5.22928 | -43.18205 | 2024-10-22 04:17:00 | NOAA-20 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 6.5 |
| e8e61b99-9731-301f-b4d0-59fc3f60bfc7 | -5.22873 | -43.1856 | 2024-10-22 04:17:00 | NOAA-20 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 6.5 |
| c07712b9-97ea-3e0e-bc9d-287bb04348e5 | -5.22817 | -43.18915 | 2024-10-22 04:17:00 | NOAA-20 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 7c91fae5-563d-3543-b4cc-245f33eff88e | -5.22649 | -43.17797 | 2024-10-22 04:17:00 | NOAA-20 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 35a18f9e-2b89-34d1-b08b-a68d74545588 | -5.22593 | -43.18153 | 2024-10-22 04:17:00 | NOAA-20 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 026314bb-212e-3ded-b02c-234b5ebac00b | -5.22538 | -43.18509 | 2024-10-22 04:17:00 | NOAA-20 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 6.5 |
| acdb63b6-05cf-3af4-80a2-fff1f62ad9d3 | -5.1884 | -42.59196 | 2024-10-22 04:17:00 | NOAA-20 | PAU D'ARCO DO PIAUÍ | PIAUÍ | Brasil | 2207793 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| cc1dfb2a-8417-3113-b87e-93bdb413efa3 | -5.17077 | -42.88374 | 2024-10-22 04:17:00 | NOAA-20 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 96b36385-61c6-3b6e-9809-a66d99ebab86 | -5.16739 | -42.88322 | 2024-10-22 04:17:00 | NOAA-20 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| c3c3c145-1183-3950-94e6-7c5582f370b5 | -5.09411 | -43.11047 | 2024-10-22 04:17:00 | NOAA-20 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 59294a4f-fd87-3a00-808b-c9477ee532bc | -5.09355 | -43.11403 | 2024-10-22 04:17:00 | NOAA-20 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 80671115-a39d-3823-b046-153cec5dbd1d | 1.84549 | -50.50002 | 2024-10-22 04:17:00 | NOAA-20 | AMAPÁ | AMAPÁ | Brasil | 1600105 | 16 | 33 | nan | nan | nan | Amazônia | 1.7 |
| fdca37b0-4434-3cc6-a158-26c4137dd798 | 1.84066 | -50.50081 | 2024-10-22 04:17:00 | NOAA-20 | AMAPÁ | AMAPÁ | Brasil | 1600105 | 16 | 33 | nan | nan | nan | Amazônia | 1.8 |
| e9fb4386-943a-3464-ba38-c4dc937f6776 | 1.83985 | -50.4955 | 2024-10-22 04:17:00 | NOAA-20 | AMAPÁ | AMAPÁ | Brasil | 1600105 | 16 | 33 | nan | nan | nan | Amazônia | 3.2 |
| ad64fef6-98bd-3ef4-8000-d9353e786448 | 1.81331 | -50.48348 | 2024-10-22 04:17:00 | NOAA-20 | AMAPÁ | AMAPÁ | Brasil | 1600105 | 16 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 9d4e5691-d866-3675-b55f-44f47b6556ee | 0.99088 | -51.17462 | 2024-10-22 04:17:00 | NOAA-20 | FERREIRA GOMES | AMAPÁ | Brasil | 1600238 | 16 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 8d39a626-ed93-32fa-85d6-d423b9bccaf4 | 0.99043 | -51.1718 | 2024-10-22 04:17:00 | NOAA-20 | FERREIRA GOMES | AMAPÁ | Brasil | 1600238 | 16 | 33 | nan | nan | nan | Amazônia | 0.5 |
| a73e70be-b63f-3fe0-bfa5-1b572386f64a | 0.98588 | -51.17538 | 2024-10-22 04:17:00 | NOAA-20 | FERREIRA GOMES | AMAPÁ | Brasil | 1600238 | 16 | 33 | nan | nan | nan | Amazônia | 1.2 |
| da244acf-de9d-331d-b74a-ea8c77d1aeae | 0.88792 | -50.67632 | 2024-10-22 04:17:00 | NOAA-20 | CUTIAS | AMAPÁ | Brasil | 1600212 | 16 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 9444d1a2-f4f1-3a16-a26b-6dcf5c0c3c69 | -7.04871 | -46.44293 | 2024-10-22 04:17:00 | NOAA-20 | FEIRA NOVA DO MARANHÃO | MARANHÃO | Brasil | 2104073 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 0cdd5da9-854d-361d-bac2-b5166e58bcce | -7.00664 | -46.70387 | 2024-10-22 04:17:00 | NOAA-20 | FEIRA NOVA DO MARANHÃO | MARANHÃO | Brasil | 2104073 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| a1230c4f-e2f5-3bcb-85f8-5b619b004a68 | -7.00604 | -46.70758 | 2024-10-22 04:17:00 | NOAA-20 | FEIRA NOVA DO MARANHÃO | MARANHÃO | Brasil | 2104073 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |


[Clique aqui para ver as próximas entradas](README18.md)
