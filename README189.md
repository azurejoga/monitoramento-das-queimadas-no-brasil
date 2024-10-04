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

## Dados Diários - Página 189

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 4771d923-7051-346d-b0d1-d30f7302b324 | -9.9822 | -42.0976 | 2024-10-04 12:36:02 | GOES-16 | SENTO SÉ | BAHIA | Brasil | 2930204 | 29 | 33 | nan | nan | nan | Caatinga | 87.3 |
| d1d3fd40-e4c1-3e72-8391-6a7bb07da929 | -10.2571 | -47.7017 | 2024-10-04 12:36:04 | GOES-16 | SANTA TEREZA DO TOCANTINS | TOCANTINS | Brasil | 1719004 | 17 | 33 | nan | nan | nan | Cerrado | 125.8 |
| f77ef150-f012-3481-9cad-1ed738fa00d9 | -10.2761 | -47.6995 | 2024-10-04 12:36:04 | GOES-16 | SANTA TEREZA DO TOCANTINS | TOCANTINS | Brasil | 1719004 | 17 | 33 | nan | nan | nan | Cerrado | 96.3 |
| ea467b64-c0dd-3def-b057-2c692471cacf | -10.2381 | -47.7038 | 2024-10-04 12:36:04 | GOES-16 | SANTA TEREZA DO TOCANTINS | TOCANTINS | Brasil | 1719004 | 17 | 33 | nan | nan | nan | Cerrado | 76.3 |
| cfa8f1c5-e544-3a6b-b104-61e4e966026c | -10.2378 | -47.726 | 2024-10-04 12:36:04 | GOES-16 | SANTA TEREZA DO TOCANTINS | TOCANTINS | Brasil | 1719004 | 17 | 33 | nan | nan | nan | Cerrado | 98.8 |
| 00b0130b-eaa4-3ebd-8a4a-96d2f7de0b58 | -10.8021 | -45.5698 | 2024-10-04 12:36:07 | GOES-16 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 134.2 |
| 2e4bdd46-b2dd-3e93-954a-512bcdb7b503 | -10.7309 | -47.7126 | 2024-10-04 12:36:07 | GOES-16 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 120.4 |
| c3b1bdcd-db35-383e-9fd9-5279751799ca | -10.7359 | -46.1465 | 2024-10-04 12:36:07 | GOES-16 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 161.8 |
| d47577e3-34ba-3fe1-8d6f-2c7e75b90b7f | -10.7115 | -47.737 | 2024-10-04 12:36:07 | GOES-16 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 75.4 |
| 8148f230-f4c8-304d-9f9f-44749a1f13a5 | -10.7355 | -46.1692 | 2024-10-04 12:36:07 | GOES-16 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 251.8 |
| 33221b51-ab06-331a-bcae-288676cf9917 | -10.8661 | -46.3331 | 2024-10-04 12:36:07 | GOES-16 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 100.2 |
| 8a574f6d-e678-3be2-a067-a58fb7bf4849 | -10.8018 | -45.5927 | 2024-10-04 12:36:07 | GOES-16 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 145.0 |
| 2494dd57-6f7b-3747-9771-d5e16075ca66 | -10.7118 | -47.7149 | 2024-10-04 12:36:07 | GOES-16 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 70.9 |
| 698907f8-00ca-356e-a52d-20ec37935a45 | -10.7352 | -46.1918 | 2024-10-04 12:36:07 | GOES-16 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 94.2 |
| bca7a149-fc1f-36ce-b77d-cb325186b0e2 | -11.0349 | -46.4917 | 2024-10-04 12:36:08 | GOES-16 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 128.6 |
| 1f386766-f948-3d7b-824e-17d60555cb42 | -11.0345 | -46.5143 | 2024-10-04 12:36:08 | GOES-16 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 120.3 |
| 63b88904-d488-3423-9bb0-7be455302f9c | -10.8992 | -46.6442 | 2024-10-04 12:36:08 | GOES-16 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 164.5 |
| 922bd016-894a-34be-b61a-44c9487462d1 | -11.0536 | -46.5118 | 2024-10-04 12:36:08 | GOES-16 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 115.8 |
| 67aa5b67-a9f5-3434-9725-932c3f05c644 | -11.2779 | -43.4118 | 2024-10-04 12:36:09 | GOES-16 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 126.6 |
| 87e530cb-2744-3672-9424-0f266d8c3c1c | -11.2783 | -43.388 | 2024-10-04 12:36:09 | GOES-16 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 163.1 |
| 56c8d118-eb88-3e1e-9aa8-72da05e57d9a | -11.2971 | -43.4088 | 2024-10-04 12:36:09 | GOES-16 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 204.9 |
| 4da01372-44f3-34e7-a9f4-31f64b60044a | -12.7815 | -50.5758 | 2024-10-04 12:36:18 | GOES-16 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 132.0 |
| 60bf6be2-88b7-3666-b162-88509f753055 | -13.0786 | -51.1385 | 2024-10-04 12:36:20 | GOES-16 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 156.0 |
| 59963bb9-c175-3ec2-905e-7c6e07e4ff96 | -13.1791 | -48.6073 | 2024-10-04 12:36:20 | GOES-16 | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | 109.5 |
| da4abe25-934d-3724-9c5b-eb2e551577be | -13.0594 | -51.1409 | 2024-10-04 12:36:20 | GOES-16 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 114.0 |
| 096794dd-66d5-3851-8d15-74eed75cf3e9 | -13.1591 | -48.6543 | 2024-10-04 12:36:20 | GOES-16 | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | 114.1 |
| 245e70a8-e58d-3e29-903a-2943dcaf2604 | -13.1595 | -48.6322 | 2024-10-04 12:36:20 | GOES-16 | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | 100.6 |
| 0cf1b665-7413-33a9-87e0-bc27060c49d1 | -13.1787 | -48.6295 | 2024-10-04 12:36:20 | GOES-16 | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | 140.0 |
| a407feaf-7489-34cc-8d7a-ff83b44eba03 | -13.1443 | -46.3261 | 2024-10-04 12:36:20 | GOES-16 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 157.3 |
| 9a6ef5e0-d298-3e4c-84bf-9637cad32494 | -13.1447 | -46.3033 | 2024-10-04 12:36:20 | GOES-16 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 94.1 |
| 858d68d0-8c95-30cb-8be2-1bcd7bc57375 | -13.1783 | -48.6516 | 2024-10-04 12:36:20 | GOES-16 | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | 131.4 |
| 74f354ec-15c8-3640-8acb-82b311d3d245 | -13.0598 | -51.1195 | 2024-10-04 12:36:20 | GOES-16 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 147.2 |
| 97e2947f-cec9-30f4-a9f5-80db0a3bc61d | -13.1587 | -48.6764 | 2024-10-04 12:36:20 | GOES-16 | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | 100.1 |
| 42490e17-3560-3d73-a78e-ab974ac37c9a | -13.1163 | -51.1765 | 2024-10-04 12:36:20 | GOES-16 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 109.6 |
| b3deed9f-015d-3a71-9ef0-1c799d279f53 | -13.1779 | -48.6737 | 2024-10-04 12:36:20 | GOES-16 | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | 164.2 |
| 0bc8c0b1-a011-357d-b520-cd664b972cdd | -14.5163 | -49.3148 | 2024-10-04 12:36:28 | GOES-16 | URUAÇU | GOIÁS | Brasil | 5221601 | 52 | 33 | nan | nan | nan | Cerrado | 54.0 |
| 730aa99f-26b6-3d31-82c4-fb5187e17155 | -16.6133 | -57.176 | 2024-10-04 12:36:40 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 147.0 |
| feffd08d-c6ef-3d7d-9eba-a1990e447cd2 | -16.613 | -57.1965 | 2024-10-04 12:36:40 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 200.3 |
| 1f4e3cdb-711b-3974-9a0e-e47b62514cba | -19.1134 | -48.2833 | 2024-10-04 12:36:52 | GOES-16 | UBERLÂNDIA | MINAS GERAIS | Brasil | 3170206 | 31 | 33 | nan | nan | nan | Cerrado | 148.7 |
| 983fcc20-db13-3c4c-8a30-22d91ac7a2ea | -19.133 | -48.3021 | 2024-10-04 12:36:52 | GOES-16 | UBERLÂNDIA | MINAS GERAIS | Brasil | 3170206 | 31 | 33 | nan | nan | nan | Cerrado | 85.5 |
| d30e0ee5-10d9-3514-a951-37058ba161b6 | -7.6675 | -45.2201 | 2024-10-04 12:45:49 | GOES-16 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 115.3 |
| a77fd243-6be0-32fa-94ea-d371aa456f3e | -7.8353 | -50.5204 | 2024-10-04 12:45:51 | GOES-16 | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 74.1 |
| cc8e4e1c-d719-34c4-be64-cdd66879d6e8 | -8.1759 | -43.6957 | 2024-10-04 12:45:52 | GOES-16 | COLÔNIA DO GURGUÉIA | PIAUÍ | Brasil | 2202752 | 22 | 33 | nan | nan | nan | Cerrado | 116.5 |
| 049f2d09-e4e0-3308-8526-48229e584ad3 | -8.1948 | -43.6936 | 2024-10-04 12:45:52 | GOES-16 | COLÔNIA DO GURGUÉIA | PIAUÍ | Brasil | 2202752 | 22 | 33 | nan | nan | nan | Cerrado | 400.2 |
| 7de801fe-afaf-3808-bb76-62555534c5b5 | -8.1055 | -44.7891 | 2024-10-04 12:45:52 | GOES-16 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 74.0 |
| a732a5db-99e7-3a1e-b180-bf8a0fb80b6b | -8.1762 | -43.6723 | 2024-10-04 12:45:52 | GOES-16 | COLÔNIA DO GURGUÉIA | PIAUÍ | Brasil | 2202752 | 22 | 33 | nan | nan | nan | Cerrado | 86.8 |
| 954f5d33-d854-3a65-b941-0a15d71adfaf | -8.1945 | -43.717 | 2024-10-04 12:45:52 | GOES-16 | COLÔNIA DO GURGUÉIA | PIAUÍ | Brasil | 2202752 | 22 | 33 | nan | nan | nan | Caatinga | 75.7 |
| 8744e720-c63e-342e-9ab3-a2a11cc518a9 | -8.1951 | -43.6703 | 2024-10-04 12:45:52 | GOES-16 | COLÔNIA DO GURGUÉIA | PIAUÍ | Brasil | 2202752 | 22 | 33 | nan | nan | nan | Cerrado | 280.5 |
| c95aed38-5692-3689-b1f3-d67a01e83514 | -8.3194 | -42.8343 | 2024-10-04 12:45:53 | GOES-16 | BREJO DO PIAUÍ | PIAUÍ | Brasil | 2201988 | 22 | 33 | nan | nan | nan | Caatinga | 63.8 |
| e5d111dc-50bd-3260-92ac-a5e436d2480d | -9.1041 | -50.902 | 2024-10-04 12:45:58 | GOES-16 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 220.1 |
| eaa29177-5292-3c24-b2b0-e7d9b6de46ba | -9.1039 | -50.9231 | 2024-10-04 12:45:58 | GOES-16 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 95.1 |
| 304c7e92-12ce-3f38-826c-034375fd3c99 | -9.9822 | -42.0976 | 2024-10-04 12:46:02 | GOES-16 | SENTO SÉ | BAHIA | Brasil | 2930204 | 29 | 33 | nan | nan | nan | Caatinga | 106.4 |
| 109fe1f7-94df-3061-9edd-8ea6e147365f | -10.2761 | -47.6995 | 2024-10-04 12:46:04 | GOES-16 | SANTA TEREZA DO TOCANTINS | TOCANTINS | Brasil | 1719004 | 17 | 33 | nan | nan | nan | Cerrado | 81.9 |
| f45b574d-1a53-3d34-a303-09c6c5d245a6 | -10.2571 | -47.7017 | 2024-10-04 12:46:04 | GOES-16 | SANTA TEREZA DO TOCANTINS | TOCANTINS | Brasil | 1719004 | 17 | 33 | nan | nan | nan | Cerrado | 136.9 |
| 0f3f0f8c-d838-3b8c-96d1-c929e5da59bd | -10.2381 | -47.7038 | 2024-10-04 12:46:04 | GOES-16 | SANTA TEREZA DO TOCANTINS | TOCANTINS | Brasil | 1719004 | 17 | 33 | nan | nan | nan | Cerrado | 68.2 |
| 76606b7a-4487-352a-ad79-741ad4c67b7f | -10.2378 | -47.726 | 2024-10-04 12:46:04 | GOES-16 | SANTA TEREZA DO TOCANTINS | TOCANTINS | Brasil | 1719004 | 17 | 33 | nan | nan | nan | Cerrado | 82.2 |
| ee9f7151-e775-3cc2-a24c-5b626ed90e2f | -10.7352 | -46.1918 | 2024-10-04 12:46:07 | GOES-16 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 104.8 |
| 3959e9a9-d0a6-3da4-9402-b8f0e2cf671a | -10.8661 | -46.3331 | 2024-10-04 12:46:07 | GOES-16 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 267.0 |
| b93ca4dd-46e3-3505-8185-d0d61851e7ee | -10.8018 | -45.5927 | 2024-10-04 12:46:07 | GOES-16 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 130.7 |
| 56ce2c9b-e598-302e-877a-86049a9e56e3 | -10.8852 | -46.3307 | 2024-10-04 12:46:07 | GOES-16 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 99.9 |
| d549e3e0-6408-30e0-a1dc-e07b0e5f9b4f | -10.8657 | -46.3557 | 2024-10-04 12:46:07 | GOES-16 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 120.3 |
| 6c22ba20-ab86-33cd-84b4-cf10a1c0723e | -10.7359 | -46.1465 | 2024-10-04 12:46:07 | GOES-16 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 217.2 |
| 72ee96fb-3220-3171-9128-fd98402976cd | -10.7115 | -47.737 | 2024-10-04 12:46:07 | GOES-16 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 69.3 |
| 393d33ee-73e2-3461-b083-3bdb5b59295e | -10.7355 | -46.1692 | 2024-10-04 12:46:07 | GOES-16 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 328.8 |
| 8e66b124-d612-3e6a-826d-dff06f6d5ac1 | -10.847 | -46.3356 | 2024-10-04 12:46:07 | GOES-16 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 120.9 |
| 1931d374-1688-315c-950b-0b9f008e6736 | -10.8021 | -45.5698 | 2024-10-04 12:46:07 | GOES-16 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 155.0 |
| edf513d5-e75b-3a7a-8078-730c13315c6a | -10.7309 | -47.7126 | 2024-10-04 12:46:07 | GOES-16 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 91.8 |
| ce18cde2-abe1-39ea-a712-6f7bb6b7add7 | -10.7118 | -47.7149 | 2024-10-04 12:46:07 | GOES-16 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 73.7 |
| 3d40725e-6941-3e5e-bcf0-e9fc5df085d6 | -10.8992 | -46.6442 | 2024-10-04 12:46:08 | GOES-16 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 127.7 |
| 1cd3cc2e-ce9e-3fc9-9899-a6664c423309 | -11.0536 | -46.5118 | 2024-10-04 12:46:08 | GOES-16 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 230.9 |
| c447b515-2cb9-36cd-ad53-5e990c846ea2 | -10.8996 | -46.6216 | 2024-10-04 12:46:08 | GOES-16 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 105.2 |
| 3dde1cfa-0950-3796-a2a8-e563b536fc24 | -11.0349 | -46.4917 | 2024-10-04 12:46:08 | GOES-16 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 204.1 |
| aae32c90-92e6-320a-a2f2-e813150d9815 | -11.0345 | -46.5143 | 2024-10-04 12:46:08 | GOES-16 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 177.9 |
| 2120522d-3895-33fc-965b-61d038dcd6fd | -11.2971 | -43.4088 | 2024-10-04 12:46:09 | GOES-16 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 254.4 |
| c5aea16f-b832-3c70-ad2e-2156c5cca39c | -11.1796 | -46.9671 | 2024-10-04 12:46:09 | GOES-16 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 108.8 |
| b7f7f23d-67c1-317e-8c7e-9c816ffb5337 | -11.1792 | -46.9895 | 2024-10-04 12:46:09 | GOES-16 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 92.3 |
| edc76e86-ba02-3685-8022-9649c0d24266 | -11.2185 | -46.9173 | 2024-10-04 12:46:09 | GOES-16 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 143.6 |
| 8ac5a054-98b4-369d-b1d8-97081376baf2 | -11.2779 | -43.4118 | 2024-10-04 12:46:09 | GOES-16 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 126.7 |
| 2e650e8e-2b55-3433-859a-25d947bc6f57 | -11.2783 | -43.388 | 2024-10-04 12:46:09 | GOES-16 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 134.6 |
| 5f20dfe3-8cb8-3819-ae57-3f497316e305 | -11.3853 | -47.2088 | 2024-10-04 12:46:10 | GOES-16 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 84.8 |
| dd7a514f-1282-3d8d-b3c2-136b669b42c6 | -11.3536 | -50.5304 | 2024-10-04 12:46:10 | GOES-16 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 73.4 |
| effd75ec-3f11-3a6f-bd47-f13a3eef3f1a | -11.9296 | -50.1425 | 2024-10-04 12:46:14 | GOES-16 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 66.6 |
| ad3f5bf1-d305-3bfb-bf60-8c2e1fe38a83 | -12.7815 | -50.5758 | 2024-10-04 12:46:18 | GOES-16 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 149.6 |
| 0f4ab030-2825-34a1-b4a3-53054b8b82c4 | -13.1595 | -48.6322 | 2024-10-04 12:46:20 | GOES-16 | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | 104.9 |
| cd6582ae-c142-3d3c-b77d-d856a178d820 | -13.0786 | -51.1385 | 2024-10-04 12:46:20 | GOES-16 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 103.4 |
| 33e88e61-3707-3a82-9cb9-bb977d21db52 | -13.1443 | -46.3261 | 2024-10-04 12:46:20 | GOES-16 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 130.8 |
| 0bb87ad4-224a-3a17-8856-30f3002973b7 | -13.1447 | -46.3033 | 2024-10-04 12:46:20 | GOES-16 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 86.7 |
| de4f3f88-51ff-3cae-a1b5-7f5b7f29b927 | -13.1783 | -48.6516 | 2024-10-04 12:46:20 | GOES-16 | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | 163.8 |
| f7e72465-774c-3b31-86e5-876d296b7e8a | -13.1587 | -48.6764 | 2024-10-04 12:46:20 | GOES-16 | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | 154.6 |
| 0a22cbb7-64a4-37f9-a4c9-f05a1376d59a | -13.1787 | -48.6295 | 2024-10-04 12:46:20 | GOES-16 | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | 156.5 |
| 86175bb8-5735-3405-89af-f6f4ccf84981 | -13.1791 | -48.6073 | 2024-10-04 12:46:20 | GOES-16 | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | 115.2 |
| a2de5689-96f5-3565-92be-05e325f608c2 | -13.0594 | -51.1409 | 2024-10-04 12:46:20 | GOES-16 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 91.1 |
| 2bce1172-5ee1-3494-bb53-7a1f0d8c0d7f | -13.1591 | -48.6543 | 2024-10-04 12:46:20 | GOES-16 | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | 170.4 |
| 810b4fb2-9562-3de4-a36f-0a4ae796ec3a | -13.1163 | -51.1765 | 2024-10-04 12:46:20 | GOES-16 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 118.7 |
| 996e3fe7-00d2-368a-977a-13e4f9352148 | -13.1779 | -48.6737 | 2024-10-04 12:46:20 | GOES-16 | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | 162.5 |
| ab9a31d1-6fbf-30ef-bff2-d3bc1378d051 | -16.6133 | -57.176 | 2024-10-04 12:46:40 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 150.5 |
| 447b0a0b-7681-3860-b7b2-924da3df17b7 | -16.613 | -57.1965 | 2024-10-04 12:46:40 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 186.8 |
| 12ee5843-cc27-3bb9-9644-dbec18cf30d3 | -19.1134 | -48.2833 | 2024-10-04 12:46:52 | GOES-16 | UBERLÂNDIA | MINAS GERAIS | Brasil | 3170206 | 31 | 33 | nan | nan | nan | Cerrado | 97.5 |
| 67cc0d23-831f-31e6-8584-8968c698aa86 | -7.6675 | -45.2201 | 2024-10-04 12:55:49 | GOES-16 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 120.3 |
| efe3e018-0814-390f-9728-715ca7a3478a | -7.8539 | -45.3611 | 2024-10-04 12:55:50 | GOES-16 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 52.3 |


[Clique aqui para ver as próximas entradas](README190.md)
