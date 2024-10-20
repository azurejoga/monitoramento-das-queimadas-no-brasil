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
| 2631a432-cdb8-30d0-a619-24c973c61879 | -2.2199 | -50.4594 | 2024-10-20 00:05:19 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 69.0 |
| 1d5045c3-cd62-349b-8e79-ac9a39e0b01d | -2.2993 | -48.5936 | 2024-10-20 00:05:19 | GOES-16 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 309.2 |
| aa286e18-ee0e-3db4-9ecb-80aef3e70b64 | -2.2994 | -48.5722 | 2024-10-20 00:05:19 | GOES-16 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 130.4 |
| a65ef00c-c002-372e-9e3a-b821e020cda5 | -2.3178 | -48.5932 | 2024-10-20 00:05:19 | GOES-16 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 63.0 |
| 929cc8a6-5bd0-3934-b535-0470938892f6 | -2.7773 | -49.3067 | 2024-10-20 00:05:22 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 142.5 |
| 15dfae3c-d6a7-3ca3-b072-84baef24df5e | -2.7774 | -49.2854 | 2024-10-20 00:05:22 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 74.2 |
| 2f3ab632-cd7f-3838-b741-fce36ed44132 | -2.7958 | -49.3062 | 2024-10-20 00:05:22 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 142.7 |
| 7b08eebf-7a7d-30fd-98c9-95a7b0dc4d3b | -2.7959 | -49.2849 | 2024-10-20 00:05:22 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 74.3 |
| 87d38651-7beb-3b49-b8dc-47af914ace8e | -2.7981 | -48.6873 | 2024-10-20 00:05:22 | GOES-16 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 73.0 |
| 8e1e763f-7474-3f8a-8eb0-684688e74d70 | -3.0478 | -51.0226 | 2024-10-20 00:05:23 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 66.8 |
| fb5e387a-5790-31e3-8c13-d1f40ba9d3a4 | -3.1278 | -54.3662 | 2024-10-20 00:05:24 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 69.4 |
| 783cb42f-8096-3d55-893d-911e6510a694 | -3.1279 | -54.3462 | 2024-10-20 00:05:24 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 62.7 |
| 250e7fec-3745-367a-947d-05bca2964ae7 | -3.1462 | -54.3658 | 2024-10-20 00:05:24 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 116.9 |
| b6d74c58-94ff-3576-90f6-927ff7a32a4d | -3.1462 | -54.3457 | 2024-10-20 00:05:24 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 89.1 |
| ff83f8a4-e8d7-3a4b-aeb9-96bbe5627e58 | -3.3813 | -50.6788 | 2024-10-20 00:05:25 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 131.9 |
| f4e175aa-a0f0-3107-8a8e-0541cb70486c | -3.3814 | -50.6579 | 2024-10-20 00:05:25 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 128.1 |
| 40f14e6d-d243-3bad-af22-8b592585ce9b | -3.3997 | -50.6782 | 2024-10-20 00:05:25 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 98.7 |
| 93385e44-4aea-3e32-aefb-c9ae080f9843 | -3.3998 | -50.6573 | 2024-10-20 00:05:25 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 96.8 |
| 282206a5-353d-3777-a806-8866e6fbd3f9 | -3.5713 | -53.7511 | 2024-10-20 00:05:26 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 59.7 |
| 55eb1942-1fa1-338c-a1d5-622e27cef749 | -3.586 | -54.6941 | 2024-10-20 00:05:26 | GOES-16 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 69.7 |
| 2c2eae62-bca1-3d19-8fba-a99aa53268f8 | -3.5861 | -54.6741 | 2024-10-20 00:05:26 | GOES-16 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 133.0 |
| a0d16b65-3829-3bc0-9ed9-0bf9251b9f88 | -3.815 | -48.866 | 2024-10-20 00:05:28 | GOES-16 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 80.0 |
| c6b487b6-89e1-3947-92c5-f884836368f9 | -3.833 | -48.9722 | 2024-10-20 00:05:28 | GOES-16 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 106.6 |
| 36610490-1645-36e7-b429-fbbcbf833423 | -3.8331 | -48.9508 | 2024-10-20 00:05:28 | GOES-16 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 95.2 |
| b268957e-9e50-3fa0-8b80-e04fe82c190b | -3.8334 | -48.8866 | 2024-10-20 00:05:28 | GOES-16 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 85.2 |
| 709fe621-ef22-3fcb-931c-d3e1d6b806d3 | -3.8335 | -48.8652 | 2024-10-20 00:05:28 | GOES-16 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 70.8 |
| 5f02f1ff-0614-33e4-ab49-bf8dc0c090eb | -3.8686 | -45.8254 | 2024-10-20 00:05:28 | GOES-16 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 116.6 |
| dafaa666-534b-3f5d-9fc1-2f3ad91add8b | -3.9018 | -49.9884 | 2024-10-20 00:05:28 | GOES-16 | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 89.0 |
| 669b46c7-4b71-390b-b9e3-04566cb857d7 | -4.1985 | -46.6318 | 2024-10-20 00:05:30 | GOES-16 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 99.6 |
| 6c0ed588-584e-3cbb-ba81-34b0a144beaf | -4.2478 | -51.0018 | 2024-10-20 00:05:30 | GOES-16 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 72.9 |
| 02ae10d7-46a7-3fb1-bc0c-1249efa8b53d | -4.4468 | -42.9123 | 2024-10-20 00:05:31 | GOES-16 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 71.7 |
| d4ab556d-a870-3231-9652-0ebe44eba8bd | -4.354 | -48.5638 | 2024-10-20 00:05:31 | GOES-16 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 81.5 |
| 48f27c8e-3fc7-3a22-b81c-15d830ab47d8 | -4.4899 | -44.7564 | 2024-10-20 00:05:31 | GOES-16 | IGARAPÉ GRANDE | MARANHÃO | Brasil | 2105203 | 21 | 33 | nan | nan | nan | Cerrado | 149.7 |
| 1a56fbc5-afa5-364f-8c16-12c87a30a64b | -4.4727 | -50.4487 | 2024-10-20 00:05:31 | GOES-16 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 79.0 |
| 046ca7b4-39a4-3c51-9bae-cfea839dbfb8 | -4.5085 | -44.7554 | 2024-10-20 00:05:31 | GOES-16 | IGARAPÉ GRANDE | MARANHÃO | Brasil | 2105203 | 21 | 33 | nan | nan | nan | Cerrado | 78.9 |
| 0fb643fb-9b60-38f6-9563-76316ef09abc | -4.8924 | -45.8386 | 2024-10-20 00:05:34 | GOES-16 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 76.0 |
| 6465dd17-3c88-3807-b3a5-1e621a12e263 | -4.8925 | -45.8162 | 2024-10-20 00:05:34 | GOES-16 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 80.1 |
| c4061848-28a0-3b2d-8521-f728a5609edd | -4.911 | -45.8374 | 2024-10-20 00:05:34 | GOES-16 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 101.2 |
| 00c76464-f104-30ba-8ac4-877bdbbf1908 | -4.9112 | -45.8151 | 2024-10-20 00:05:34 | GOES-16 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 89.9 |
| b7f87c97-d6df-3155-82c3-c05f7cca8c3e | -5.2072 | -46.11 | 2024-10-20 00:05:35 | GOES-16 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 92.2 |
| 395174a1-d0ac-3873-b345-8cc81776c009 | -5.2073 | -46.0876 | 2024-10-20 00:05:35 | GOES-16 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 96.6 |
| 90c7aa0c-cf8f-3753-a100-14b75c30d7c7 | -5.2258 | -46.1088 | 2024-10-20 00:05:36 | GOES-16 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 80.1 |
| b2629775-1bf3-32c3-8246-fb9ced8f2283 | -5.226 | -46.0865 | 2024-10-20 00:05:36 | GOES-16 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 84.9 |
| 27249058-da7e-39ed-8f81-7dcd6559eb7c | -5.3873 | -46.9191 | 2024-10-20 00:05:36 | GOES-16 | BURITIRANA | MARANHÃO | Brasil | 2102358 | 21 | 33 | nan | nan | nan | Cerrado | 100.2 |
| 0b060031-8a2b-3c27-8798-45a4dabf2a9a | -5.3875 | -46.897 | 2024-10-20 00:05:36 | GOES-16 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 123.7 |
| 52dc9213-94d6-3688-99cd-1b5ee5acd77e | -5.4059 | -46.9179 | 2024-10-20 00:05:37 | GOES-16 | BURITIRANA | MARANHÃO | Brasil | 2102358 | 21 | 33 | nan | nan | nan | Cerrado | 180.2 |
| 33cfc0f0-e563-3d14-8ec5-7a833ac7ad39 | -5.4061 | -46.8959 | 2024-10-20 00:05:37 | GOES-16 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 226.1 |
| 99359a79-2e1e-36de-91df-4ec43f5fdfe4 | -5.4247 | -46.8947 | 2024-10-20 00:05:37 | GOES-16 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 55.1 |
| 8b390db2-f5e1-3600-90e6-f7e8af65afc0 | -5.721 | -68.6862 | 2024-10-20 00:05:39 | GOES-16 | JUTAÍ | AMAZONAS | Brasil | 1302306 | 13 | 33 | nan | nan | nan | Amazônia | 48.6 |
| 5a2131bd-b1bd-37dd-bfeb-230a9140814a | -7.3638 | -72.8628 | 2024-10-20 00:05:49 | GOES-16 | GUAJARÁ | AMAZONAS | Brasil | 1301654 | 13 | 33 | nan | nan | nan | Amazônia | 96.4 |
| d44ed18f-f650-3a3c-b9d0-0c09aaa0d915 | -7.5841 | -73.0436 | 2024-10-20 00:05:50 | GOES-16 | MÂNCIO LIMA | ACRE | Brasil | 1200336 | 12 | 33 | nan | nan | nan | Amazônia | 66.2 |
| 28b0945f-49ee-31bc-bbca-1a280c956042 | -10.4759 | -48.2928 | 2024-10-20 00:06:05 | GOES-16 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 62.5 |
| 1fe801c7-e8f8-3831-a79b-49efd44870d1 | -10.4762 | -48.2708 | 2024-10-20 00:06:05 | GOES-16 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 60.8 |
| 35420862-f5d2-3a56-8a45-8b109c3bf459 | -12.4967 | -63.1874 | 2024-10-20 00:06:17 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 79.3 |
| aa8c5240-8818-365d-b1af-9f31a1f81231 | -17.851299 | -39.792702 | 2024-10-20 00:10:13 | METOP-C | NOVA VIÇOSA | BAHIA | Brasil | 2923001 | 29 | 33 | nan | nan | nan | Mata Atlântica | nan |
| d5dd01c6-73fc-3410-8e2d-a14ba56fd4ba | -17.853001 | -39.8008 | 2024-10-20 00:10:13 | METOP-C | NOVA VIÇOSA | BAHIA | Brasil | 2923001 | 29 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 1de42faa-ffa1-369d-b531-b29deb8cbf24 | -17.841499 | -39.794899 | 2024-10-20 00:10:14 | METOP-C | NOVA VIÇOSA | BAHIA | Brasil | 2923001 | 29 | 33 | nan | nan | nan | Mata Atlântica | nan |
| f611cd27-9306-3161-8ba6-93fd1ff3d807 | -17.843201 | -39.803001 | 2024-10-20 00:10:14 | METOP-C | NOVA VIÇOSA | BAHIA | Brasil | 2923001 | 29 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 432aeb8a-c179-3494-8d1c-c3fff78d2b82 | -17.581301 | -40.217098 | 2024-10-20 00:10:19 | METOP-C | LAJEDÃO | BAHIA | Brasil | 2918902 | 29 | 33 | nan | nan | nan | Mata Atlântica | nan |
| ff4141ed-b09c-3d05-a205-34a2187e3567 | -17.583 | -40.225601 | 2024-10-20 00:10:19 | METOP-C | LAJEDÃO | BAHIA | Brasil | 2918902 | 29 | 33 | nan | nan | nan | Mata Atlântica | nan |
| cf8cc303-b061-3d31-be12-e882b078f141 | -17.571501 | -40.2192 | 2024-10-20 00:10:19 | METOP-C | LAJEDÃO | BAHIA | Brasil | 2918902 | 29 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 136ca235-ccf0-3633-83f5-f1783bbb2902 | -17.5732 | -40.227699 | 2024-10-20 00:10:19 | METOP-C | LAJEDÃO | BAHIA | Brasil | 2918902 | 29 | 33 | nan | nan | nan | Mata Atlântica | nan |
| dc4eeb19-1c18-3498-bf0e-49a68d72b282 | -17.501101 | -42.188801 | 2024-10-20 00:10:27 | METOP-C | SETUBINHA | MINAS GERAIS | Brasil | 3165552 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| def94ecb-0e13-35ec-aeec-962309bc187b | -16.8585 | -40.580799 | 2024-10-20 00:10:32 | METOP-C | SANTA HELENA DE MINAS | MINAS GERAIS | Brasil | 3157658 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 6fc7c575-232e-338a-899f-26237aee60b6 | -16.8603 | -40.589401 | 2024-10-20 00:10:32 | METOP-C | SANTA HELENA DE MINAS | MINAS GERAIS | Brasil | 3157658 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| d5a676a5-3027-3d24-9d3d-db610a4261f4 | -15.5883 | -39.615601 | 2024-10-20 00:10:50 | METOP-C | PAU BRASIL | BAHIA | Brasil | 2923902 | 29 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 1eba338d-846b-30b3-baf9-3430b0d42df5 | -15.59 | -39.623199 | 2024-10-20 00:10:50 | METOP-C | PAU BRASIL | BAHIA | Brasil | 2923902 | 29 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 21e37a13-8494-35ce-93d3-d1593f10d766 | -10.0641 | -36.342201 | 2024-10-20 00:12:01 | METOP-C | CORURIPE | ALAGOAS | Brasil | 2702306 | 27 | 33 | nan | nan | nan | Caatinga | nan |
| b72ac054-664c-35a1-9aa9-384979df095a | -10.0659 | -36.350101 | 2024-10-20 00:12:01 | METOP-C | CORURIPE | ALAGOAS | Brasil | 2702306 | 27 | 33 | nan | nan | nan | Caatinga | nan |
| f35b20ae-d033-378d-90c1-c1575ed0f0c0 | -7.822 | -37.5252 | 2024-10-20 00:12:41 | METOP-C | IGUARACY | PERNAMBUCO | Brasil | 2606903 | 26 | 33 | nan | nan | nan | Caatinga | nan |
| 7117aec1-270e-3bbf-a30f-eda3bc8b0d78 | -7.6505 | -47.310001 | 2024-10-20 00:13:19 | METOP-C | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 8bcc0a68-2579-3958-aa22-e56431ac30bb | -5.8522 | -40.168598 | 2024-10-20 00:13:23 | METOP-C | TAUÁ | CEARÁ | Brasil | 2313302 | 23 | 33 | nan | nan | nan | Caatinga | nan |
| d71ca7fb-8c8b-36c4-94f0-9a323d815103 | -6.5206 | -43.0443 | 2024-10-20 00:13:23 | METOP-C | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| a82d29ea-9ef6-32e4-b5bf-e9483d87050f | -5.9292 | -43.387501 | 2024-10-20 00:13:34 | METOP-C | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Caatinga | nan |
| f4262f3e-fad0-3863-88b1-3e508a601db2 | -6.6098 | -47.342899 | 2024-10-20 00:13:37 | METOP-C | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| c4fe2e6a-1cd6-3819-afe6-b9223e104273 | -5.5705 | -42.9314 | 2024-10-20 00:13:38 | METOP-C | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 5e218cb1-41dc-3fe2-9bd6-d8c707b2f6c9 | -5.5723 | -42.939499 | 2024-10-20 00:13:38 | METOP-C | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 618fa5a9-3647-364f-918c-d43e7c28a000 | -5.8079 | -44.043201 | 2024-10-20 00:13:38 | METOP-C | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| d06d8708-d50e-34e0-be79-dc7c26938a52 | -5.81 | -44.052502 | 2024-10-20 00:13:38 | METOP-C | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| e356a3b4-1dc5-3a47-936e-0efafddb6fba | -5.6959 | -43.770199 | 2024-10-20 00:13:39 | METOP-C | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 8f8a4f04-5f74-34e2-a62d-b27f4ec26f93 | -5.6979 | -43.779202 | 2024-10-20 00:13:39 | METOP-C | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 2e07921f-014a-3fd2-a310-04f0a5983906 | -5.4658 | -43.336399 | 2024-10-20 00:13:41 | METOP-C | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| fda72009-53b1-3e94-9115-d14844850d2a | -5.4677 | -43.344898 | 2024-10-20 00:13:41 | METOP-C | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 620c5404-c900-3ab9-a5ca-248d5d8db143 | -5.456 | -43.338501 | 2024-10-20 00:13:41 | METOP-C | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 79996d5b-e045-328e-a5bd-4da6614bd0c0 | -5.4579 | -43.347 | 2024-10-20 00:13:41 | METOP-C | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 9f5a315f-3254-3e9b-84a4-d067b76aa629 | -5.5182 | -43.894001 | 2024-10-20 00:13:42 | METOP-C | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| dac82a10-34f6-38aa-88c4-72eb59c5cfac | -5.5202 | -43.903 | 2024-10-20 00:13:42 | METOP-C | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| b33cf347-97d2-3596-8c91-e386c25417cc | -5.5222 | -43.912102 | 2024-10-20 00:13:42 | METOP-C | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 5701a971-dc81-346e-83b1-802533ea36ea | -5.3432 | -43.569698 | 2024-10-20 00:13:44 | METOP-C | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| ed26ba31-35b7-35c9-ad10-cd612aa78f1e | -5.3451 | -43.5783 | 2024-10-20 00:13:44 | METOP-C | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 311590f5-c5c3-345a-b8f3-531baf0ee535 | -5.3334 | -43.5718 | 2024-10-20 00:13:44 | METOP-C | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 342e97b4-f248-3847-8e49-772803a1845e | -5.4462 | -44.170601 | 2024-10-20 00:13:44 | METOP-C | GOVERNADOR EUGÊNIO BARROS | MARANHÃO | Brasil | 2104602 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| c5c08afb-9f49-33cc-ba5f-ea4b1716d62a | -5.4483 | -44.18 | 2024-10-20 00:13:44 | METOP-C | GOVERNADOR LUIZ ROCHA | MARANHÃO | Brasil | 2104628 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 1113e54d-c757-3973-8131-514a0740c8ca | -5.2287 | -44.208 | 2024-10-20 00:13:48 | METOP-C | GONÇALVES DIAS | MARANHÃO | Brasil | 2104404 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| f18b6ac4-62c1-3f4d-b218-28a2ee1eccb0 | -4.8408 | -43.254101 | 2024-10-20 00:13:51 | METOP-C | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| ae35d987-cb66-3e4a-acda-e60c8ed981dc | -5.4145 | -46.347301 | 2024-10-20 00:13:53 | METOP-C | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 752eff7c-2035-30d0-9157-57ce2464f606 | -5.4173 | -46.360199 | 2024-10-20 00:13:53 | METOP-C | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 91659cb2-6a9b-3476-be8c-d08b8dcaca7e | -5.1513 | -45.569599 | 2024-10-20 00:13:54 | METOP-C | ITAIPAVA DO GRAJAÚ | MARANHÃO | Brasil | 2105351 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| d349e3da-87db-320a-9b02-37bff357c24d | -5.3829 | -46.902802 | 2024-10-20 00:13:55 | METOP-C | BURITIRANA | MARANHÃO | Brasil | 2102358 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 8849a869-2f30-3a32-b977-7309d2ee23ef | -4.6051 | -43.349098 | 2024-10-20 00:13:55 | METOP-C | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | nan |


[Clique aqui para ver as próximas entradas](README2.md)
