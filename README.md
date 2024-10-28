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

## Dados Diários - Página 1

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 1ed13d9e-450e-36e7-a102-2b6de357a34e | -0.9815 | -53.699 | 2024-10-28 00:05:11 | GOES-16 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 50.9 |
| 92df21ba-78d8-3942-9ec3-38e79fbb72d2 | -1.0733 | -53.658 | 2024-10-28 00:05:11 | GOES-16 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 47.5 |
| 8f612e88-63a1-3491-b21d-69149212ca5a | -1.0916 | -53.6578 | 2024-10-28 00:05:11 | GOES-16 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 53.3 |
| 871da71a-cc8a-3818-b42e-5642e15dc0bb | -1.1653 | -53.4957 | 2024-10-28 00:05:12 | GOES-16 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 60.3 |
| 7cfafb7d-54fc-3de0-b4c1-2d08355629e2 | -1.1836 | -53.5158 | 2024-10-28 00:05:12 | GOES-16 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 77.9 |
| 834f2fef-fb41-3d1a-a1b5-dce548ea4640 | -1.1836 | -53.4956 | 2024-10-28 00:05:12 | GOES-16 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 119.6 |
| 2773aed9-bc39-3d64-bb50-7b3727c4d0af | -1.5349 | -52.1079 | 2024-10-28 00:05:14 | GOES-16 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 32.2 |
| 59abeddc-ed87-338b-8f48-55e9d771c5fa | -1.5349 | -52.0874 | 2024-10-28 00:05:14 | GOES-16 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 65.6 |
| 6aa005e5-bd32-3353-b8aa-a224ba7f45ef | -1.5532 | -52.1076 | 2024-10-28 00:05:14 | GOES-16 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 68.1 |
| cb2244af-23af-3aee-b9b6-6a8ba5442467 | -1.5533 | -52.0871 | 2024-10-28 00:05:14 | GOES-16 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 69.3 |
| 51bb9de3-cd29-3387-b7b2-7dc6c8c25515 | -1.7315 | -54.9916 | 2024-10-28 00:05:15 | GOES-16 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 33.4 |
| 751958a2-1abf-3bc5-aecd-fcccfda81f85 | -1.9763 | -52.0804 | 2024-10-28 00:05:16 | GOES-16 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 38.7 |
| 79edbb10-8e7c-39b4-b275-53ef2af2e1fa | -2.0315 | -52.0794 | 2024-10-28 00:05:17 | GOES-16 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 32.0 |
| e6decb07-4a82-3d0c-86c7-3c04903a2e77 | -2.0499 | -52.0996 | 2024-10-28 00:05:17 | GOES-16 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 48.8 |
| e0654977-eb82-343d-be3e-aa41cd14ca0f | -2.0499 | -52.0791 | 2024-10-28 00:05:17 | GOES-16 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 76.5 |
| c9cb1427-f564-3d97-b8ff-5dab82849293 | -2.0681 | -52.1608 | 2024-10-28 00:05:17 | GOES-16 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 31.1 |
| 6702b260-e1e5-3672-b6e2-5292e589ff56 | -2.2662 | -53.8027 | 2024-10-28 00:05:18 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 106.8 |
| 4a72a7bf-626e-369e-85c1-cf4329aede0c | -2.2662 | -53.7825 | 2024-10-28 00:05:18 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 336.3 |
| 2bad250f-570d-34da-9abf-819704a55c4e | -2.2663 | -53.7624 | 2024-10-28 00:05:18 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 102.4 |
| 873b1475-4dae-3625-beed-c3e815f4ee7b | -2.2845 | -53.8023 | 2024-10-28 00:05:18 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 115.4 |
| 000314b1-d71d-328e-8a1c-c403cd6e7269 | -2.2846 | -53.7822 | 2024-10-28 00:05:18 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 370.5 |
| e6657571-1b21-3775-8b54-b74f1c69b1ee | -2.2846 | -53.762 | 2024-10-28 00:05:18 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 112.8 |
| 5dc6533c-d10d-3750-b0b0-b10636b1482f | -2.3919 | -48.5484 | 2024-10-28 00:05:19 | GOES-16 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 71.1 |
| 9e6be1bd-e05c-3038-88b6-5efad745c0e0 | -2.4104 | -48.5479 | 2024-10-28 00:05:19 | GOES-16 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 78.0 |
| 7fefe294-0273-3a1a-9fd0-9036c53da37c | -2.5066 | -47.4425 | 2024-10-28 00:05:19 | GOES-16 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 63.0 |
| 675afc88-6a25-3d74-9cd8-c20a8eed24cc | -2.5127 | -51.1821 | 2024-10-28 00:05:20 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 44.9 |
| b010b136-8c58-3c78-821c-a6ced1ab510c | -2.5251 | -47.442 | 2024-10-28 00:05:20 | GOES-16 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 145.9 |
| 8a5fdd63-83c0-31b1-81fc-cf819939b131 | -2.531 | -51.2024 | 2024-10-28 00:05:20 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 36.2 |
| 1d13abac-6841-3d75-811e-2a69d281318c | -2.5311 | -51.1816 | 2024-10-28 00:05:20 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 68.2 |
| bf13aefc-f964-374d-845d-8c125c717cb5 | -2.6398 | -51.758 | 2024-10-28 00:05:20 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 46.9 |
| a89ad048-429b-31a5-9633-fbd692b55c65 | -2.6399 | -51.7374 | 2024-10-28 00:05:20 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 70.7 |
| b57079d5-d9eb-31ac-8d64-8686990b9fd9 | -2.8054 | -51.8157 | 2024-10-28 00:05:21 | GOES-16 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 66.8 |
| ac3b342c-8da5-383e-a336-e901e8d2a050 | -2.8054 | -51.7951 | 2024-10-28 00:05:21 | GOES-16 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 79.5 |
| 557d2e11-f818-3e62-8773-f1a5ae952637 | -2.8555 | -53.3459 | 2024-10-28 00:05:22 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 63.6 |
| b46822e3-70b1-3b45-b2b1-cb30454e1cd4 | -2.8556 | -53.3256 | 2024-10-28 00:05:22 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 86.0 |
| 02a3449e-d363-3eeb-b30a-e9dadc57c3b1 | -3.0317 | -50.4176 | 2024-10-28 00:05:22 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 93.8 |
| 74bf5e5a-1024-34ea-821b-f31f16bdf6e6 | -3.0317 | -50.3967 | 2024-10-28 00:05:22 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 65.3 |
| 646ce81f-4110-37d2-b1b7-d38521398090 | -3.0501 | -50.4171 | 2024-10-28 00:05:23 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 36.2 |
| 48712ef6-bcdc-3e04-aae9-82cc91ce3ed0 | -3.0538 | -49.4895 | 2024-10-28 00:05:23 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 51.6 |
| 5ab9d13e-c33f-35d3-b635-abf8077b30b5 | -3.0734 | -54.167 | 2024-10-28 00:05:23 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 63.2 |
| 21444ecf-9cbf-3c11-b4a8-25d7ad77cd42 | -3.2719 | -46.2294 | 2024-10-28 00:05:24 | GOES-16 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 67.8 |
| 12c71428-ab1e-34c5-839a-9c1a8a9fe2f6 | -3.272 | -46.2072 | 2024-10-28 00:05:24 | GOES-16 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 109.2 |
| 2d3e7dac-cbeb-38ed-82cc-d31f570c2acf | -3.5588 | -41.3958 | 2024-10-28 00:05:25 | GOES-16 | COCAL DOS ALVES | PIAUÍ | Brasil | 2202729 | 22 | 33 | nan | nan | nan | Caatinga | 81.2 |
| 7d8afdfc-60f6-3d66-9b13-c86a6f80608a | -3.4013 | -46.3353 | 2024-10-28 00:05:25 | GOES-16 | SÃO JOÃO DO CARÚ | MARANHÃO | Brasil | 2111029 | 21 | 33 | nan | nan | nan | Amazônia | 55.7 |
| f713940d-1ed8-3c52-a652-e65f8f84a3f1 | -3.4014 | -46.3131 | 2024-10-28 00:05:25 | GOES-16 | SÃO JOÃO DO CARÚ | MARANHÃO | Brasil | 2111029 | 21 | 33 | nan | nan | nan | Amazônia | 111.0 |
| dac156e8-2de1-3381-b4f8-b9c9dae52534 | -3.42 | -46.3123 | 2024-10-28 00:05:25 | GOES-16 | SÃO JOÃO DO CARÚ | MARANHÃO | Brasil | 2111029 | 21 | 33 | nan | nan | nan | Amazônia | 71.5 |
| 20e0b3c0-8d2c-35d4-a052-2695646cdd1c | -3.6727 | -51.5629 | 2024-10-28 00:05:26 | GOES-16 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 39.9 |
| 66a3d369-5d26-3971-adaf-02bfcbce7e36 | -3.6911 | -51.5622 | 2024-10-28 00:05:26 | GOES-16 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 75.0 |
| 4d0ae54f-a19e-384f-8ecc-bd730f165b45 | -3.6912 | -51.5416 | 2024-10-28 00:05:26 | GOES-16 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 36.9 |
| b5960496-67c9-382c-904b-c448fbb7a1cd | -3.7346 | -59.4577 | 2024-10-28 00:05:27 | GOES-16 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 61.6 |
| 51ee5940-3406-310a-a75b-9283a07539ad | -3.9949 | -46.4867 | 2024-10-28 00:05:28 | GOES-16 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 49.0 |
| 8a3e14d6-7812-3960-b661-aeae7a4bdc57 | -4.1814 | -46.3892 | 2024-10-28 00:05:29 | GOES-16 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 52.6 |
| 81c9f0a0-b98d-30b4-9844-f8a93057dc4b | -4.2797 | -45.5362 | 2024-10-28 00:05:29 | GOES-16 | ALTAMIRA DO MARANHÃO | MARANHÃO | Brasil | 2100402 | 21 | 33 | nan | nan | nan | Amazônia | 81.8 |
| d91975ba-f5ac-3c2d-9236-a8a799bb368c | -4.4093 | -45.6641 | 2024-10-28 00:05:30 | GOES-16 | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | 64.4 |
| 9af6dfba-c4c1-3932-97bc-3821f31ed001 | -4.4094 | -45.6416 | 2024-10-28 00:05:30 | GOES-16 | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | 122.8 |
| bf4d59d8-5a71-33e3-9adc-7926f57b8848 | -4.4279 | -45.6631 | 2024-10-28 00:05:30 | GOES-16 | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | 103.8 |
| dc9e1bc0-854f-3024-a24a-a8aecc1297e8 | -4.428 | -45.6406 | 2024-10-28 00:05:30 | GOES-16 | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | 211.9 |
| d46c41d0-7e47-3e73-9347-7ac0fa5ce21a | -4.5157 | -46.4608 | 2024-10-28 00:05:31 | GOES-16 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 54.0 |
| c6476668-3816-351a-85d9-213b25bd6365 | -4.758 | -46.4033 | 2024-10-28 00:05:32 | GOES-16 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 183.5 |
| 2e19f375-6a54-3985-8437-69987eff761d | -4.7581 | -46.3811 | 2024-10-28 00:05:32 | GOES-16 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 173.5 |
| 1f3b87c1-4ae4-31be-abaa-493fb6045c08 | -4.7766 | -46.4022 | 2024-10-28 00:05:32 | GOES-16 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 320.4 |
| 9186c480-721f-3a3f-9039-242290587620 | -4.7768 | -46.3801 | 2024-10-28 00:05:32 | GOES-16 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 335.4 |
| 6c1a5d1e-e70c-3fed-b3fa-0b6f94484aa1 | -4.9262 | -49.0077 | 2024-10-28 00:05:33 | GOES-16 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 53.2 |
| c3fec30f-bb4c-3bcd-ab95-85a3339ea5c8 | -0.9815 | -53.699 | 2024-10-28 00:15:11 | GOES-16 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 53.6 |
| 04d1ff5b-9ad9-3f0e-8da6-30bb410f0c60 | -1.0733 | -53.658 | 2024-10-28 00:15:11 | GOES-16 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 64.1 |
| c610f747-b947-301f-8738-f03785c6d52a | -1.1653 | -53.4957 | 2024-10-28 00:15:12 | GOES-16 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 69.4 |
| bfb3c38e-c9e7-33d0-a9d9-4963002d1a4e | -1.1836 | -53.5158 | 2024-10-28 00:15:12 | GOES-16 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 68.7 |
| 11d4ccb3-1719-33f0-bad3-b0c7aec8ef4c | -1.1836 | -53.4956 | 2024-10-28 00:15:12 | GOES-16 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 93.2 |
| 42c54d61-0899-34f3-886c-b4b598b0e0cf | -1.2907 | -55.7098 | 2024-10-28 00:15:13 | GOES-16 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 31.6 |
| a7db9b48-b6cc-33ad-ae08-22b2c3e4850d | -1.5349 | -52.1079 | 2024-10-28 00:15:14 | GOES-16 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 39.7 |
| d20cf838-0fe2-3a61-9b00-75dccfb1f553 | -1.5349 | -52.0874 | 2024-10-28 00:15:14 | GOES-16 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 91.4 |
| 764b66af-5a1a-3aab-844c-3cab0a3a7f96 | -1.5532 | -52.1076 | 2024-10-28 00:15:14 | GOES-16 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 87.5 |
| 300c5001-f248-3e25-b568-e6b0cad78f0a | -1.5533 | -52.0871 | 2024-10-28 00:15:14 | GOES-16 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 109.8 |
| e39c0191-0c61-3e0a-a8b8-d37cd24d9f5f | -1.9763 | -52.0804 | 2024-10-28 00:15:16 | GOES-16 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 48.3 |
| 2acb95e8-1617-350a-ba5d-6252787443cb | -2.0497 | -52.1611 | 2024-10-28 00:15:17 | GOES-16 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 41.6 |
| c9afd0b6-5224-365b-a69e-2f6f0b6d29f8 | -2.0499 | -52.0996 | 2024-10-28 00:15:17 | GOES-16 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 48.2 |
| 5ef41e9d-ad5e-3d33-bb48-2154b0786bc8 | -2.0499 | -52.0791 | 2024-10-28 00:15:17 | GOES-16 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 68.9 |
| 9fe0236a-a4a7-3928-808c-b7ad7aaaf806 | -2.1826 | -50.6065 | 2024-10-28 00:15:18 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 30.6 |
| f0012ee2-4a16-3142-8a24-b46095b26d38 | -2.2662 | -53.8027 | 2024-10-28 00:15:18 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 153.5 |
| 6389bc24-a2f7-375b-91d2-86c04b0236d1 | -2.2662 | -53.7825 | 2024-10-28 00:15:18 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 393.7 |
| f508cc5c-433d-33c4-a716-126fc040cb03 | -2.2663 | -53.7624 | 2024-10-28 00:15:18 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 119.5 |
| cb33fc12-857b-3697-b928-8b6632a51782 | -2.2845 | -53.8023 | 2024-10-28 00:15:18 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 96.9 |
| 8759da34-bf14-3c18-a535-df9fb0502eed | -2.2846 | -53.7822 | 2024-10-28 00:15:18 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 224.0 |
| ece1a9ac-7bf5-3ef6-921c-36f7c8f10ef2 | -2.2846 | -53.762 | 2024-10-28 00:15:18 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 91.4 |
| 597962c8-810c-38cb-817b-992bf15271cc | -2.3919 | -48.5484 | 2024-10-28 00:15:19 | GOES-16 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 59.7 |
| 286ef5c5-96b9-3164-8e02-2a492337fa3d | -2.4104 | -48.5479 | 2024-10-28 00:15:19 | GOES-16 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 79.2 |
| 31fb1e91-11af-331f-9806-77209cea8c12 | -2.5127 | -51.1821 | 2024-10-28 00:15:20 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 61.4 |
| 9f35311f-f961-3060-8167-0edd202f2e3c | -2.5251 | -47.442 | 2024-10-28 00:15:20 | GOES-16 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 131.6 |
| 29334f0c-0b7c-31bf-9b7e-888f844bb042 | -2.531 | -51.2024 | 2024-10-28 00:15:20 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 36.8 |
| c9a7c49a-7455-34c5-aadf-588366da839e | -2.5311 | -51.1816 | 2024-10-28 00:15:20 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 81.0 |
| 053cebd4-6fd4-33e2-a9a3-f404d6c26ecb | -2.6399 | -51.7374 | 2024-10-28 00:15:20 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 59.7 |
| 2afffc59-8020-3966-a0cc-b60beb1b6d7c | -2.6583 | -51.737 | 2024-10-28 00:15:20 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 56.2 |
| f6ee19df-7d1b-39a5-a479-f568dcebaebe | -2.7034 | -49.3088 | 2024-10-28 00:15:21 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 39.7 |
| cf3ef994-781c-30b9-96ed-59a339cb92d4 | -2.8054 | -51.7951 | 2024-10-28 00:15:21 | GOES-16 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 61.5 |
| 56182bcd-ce5b-36b3-8933-f0654cc20f3e | -2.8555 | -53.3459 | 2024-10-28 00:15:22 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 56.1 |
| 11d01674-ed4e-3bbe-b742-e871b9c1cb5a | -2.8556 | -53.3256 | 2024-10-28 00:15:22 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 83.7 |
| d9fa43f9-f774-36d0-886c-0173dc2c194f | -2.8739 | -53.3252 | 2024-10-28 00:15:22 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 61.5 |
| 7d489d43-2a33-3f3d-b6d9-dbb00fae0ac9 | -3.0132 | -50.4182 | 2024-10-28 00:15:22 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 31.6 |
| ecc46676-17d9-33b1-b197-d1a39eeb2615 | -3.0317 | -50.4176 | 2024-10-28 00:15:22 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 88.4 |
| 977f1979-2d5e-347b-a3c6-d894317fae0b | -3.0317 | -50.3967 | 2024-10-28 00:15:22 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 49.4 |


[Clique aqui para ver as próximas entradas](README2.md)
