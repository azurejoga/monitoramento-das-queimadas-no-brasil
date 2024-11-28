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
| 73213497-6c78-38c6-b5fa-c9390260e0bd | -6.1041 | -43.9593 | 2024-11-28 00:00:00 | GOES-16 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 148.7 |
| 341bbb0e-c9d5-3fb3-aed9-f7a7aa7d7987 | -1.3145 | -51.9465 | 2024-11-28 00:00:00 | GOES-16 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 50.4 |
| adda3e9a-4a8b-35de-99fe-a109bfe2f6cd | -3.9213 | -53.6796 | 2024-11-28 00:00:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 49.4 |
| 6c1873bf-164c-37de-b73d-b019bcc508ed | -3.4022 | -50.1119 | 2024-11-28 00:00:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 60.4 |
| 40e0b24a-d5dc-357c-adb9-062d6411020c | -1.5897 | -52.271 | 2024-11-28 00:00:00 | GOES-16 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 67.4 |
| 56a68821-c041-3fc4-a25d-6da244456029 | -6.1735 | -42.6221 | 2024-11-28 00:00:00 | GOES-16 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 88.5 |
| 07ac6fe3-a620-381f-88a6-c4603879ac14 | -3.093 | -53.8045 | 2024-11-28 00:00:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 74.1 |
| 4a567398-4915-3016-8a48-ef06633e180d | -1.3145 | -51.9259 | 2024-11-28 00:00:00 | GOES-16 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 55.2 |
| 348108f6-f962-3375-a540-c0da0beb44cb | -2.8424 | -46.8413 | 2024-11-28 00:00:00 | GOES-16 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 72.8 |
| 2326181f-b0ea-3630-bde4-de1acf0c1c49 | -4.6565 | -42.3811 | 2024-11-28 00:00:00 | GOES-16 | JOSÉ DE FREITAS | PIAUÍ | Brasil | 2205508 | 22 | 33 | nan | nan | nan | Caatinga | 34.2 |
| 0a3ff867-d91c-3161-bc88-831369814ad0 | -9.0108 | -36.1458 | 2024-11-28 00:00:00 | GOES-16 | CANHOTINHO | PERNAMBUCO | Brasil | 2603702 | 26 | 33 | nan | nan | nan | Mata Atlântica | 60.6 |
| 2d843690-889f-34c3-b19f-7f3e5c1d3bfc | -4.1458 | -46.1244 | 2024-11-28 00:00:00 | GOES-16 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 70.7 |
| b027a32a-e2aa-38d1-824a-82f95e68a924 | -1.5713 | -52.2713 | 2024-11-28 00:00:00 | GOES-16 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 71.3 |
| 9b161114-3744-32c0-ab0b-8bd9da109d8e | -3.6829 | -45.7891 | 2024-11-28 00:00:00 | GOES-16 | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 198.5 |
| 6382371b-9527-36ec-824c-ddac89d85f61 | -3.0929 | -53.8247 | 2024-11-28 00:00:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 81.8 |
| f39ac60e-c8c0-39ee-ba60-64a477f72e48 | -18.764 | -55.8444 | 2024-11-28 00:00:00 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 64.4 |
| 7e91f634-11af-3080-82f8-fe137e4be773 | -2.8423 | -46.8632 | 2024-11-28 00:00:00 | GOES-16 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 69.3 |
| 05be4864-ed33-34cf-aee9-4250b9973a6d | -6.0864 | -48.0122 | 2024-11-28 00:00:00 | GOES-16 | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | 69.7 |
| 49312183-5d82-30b6-9045-ab1bec47e1af | -4.146 | -46.1021 | 2024-11-28 00:00:00 | GOES-16 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 67.2 |
| c4e01437-dc0d-3ec1-a7c4-1bedb628889c | -2.8794 | -46.862 | 2024-11-28 00:00:00 | GOES-16 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 212.5 |
| f324e531-eed4-322c-b657-82e6cd319a59 | -6.1048 | -48.0327 | 2024-11-28 00:00:00 | GOES-16 | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | 87.8 |
| cde43ada-9545-3dfd-944d-38593a5cdd62 | -2.8795 | -46.84 | 2024-11-28 00:00:00 | GOES-16 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 172.8 |
| 5a5dd08c-d4ea-3d03-a018-1704a559d123 | -18.784 | -55.8416 | 2024-11-28 00:00:00 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 78.8 |
| 476bf229-1e84-3e2c-9039-d59cee45b45a | -17.6457 | -57.5668 | 2024-11-28 00:00:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 36.3 |
| ad2f1585-cfec-3ef1-9f8c-13be4666ac33 | -17.6453 | -57.5874 | 2024-11-28 00:00:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 39.8 |
| 6e73a50f-45f2-3f23-9061-05f687e9a27d | -2.1511 | -48.7042 | 2024-11-28 00:00:00 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 47.8 |
| 615c28bf-665f-3cea-bf22-be62d8fd7ab4 | -1.3329 | -51.9463 | 2024-11-28 00:00:00 | GOES-16 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 91.0 |
| 1ee5cdb7-0fa1-3300-b0c0-17386e9afda5 | -5.9788 | -45.3621 | 2024-11-28 00:00:00 | GOES-16 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 184.8 |
| 0637ccd9-021e-336e-9e67-bf85b061421d | -2.5963 | -53.9771 | 2024-11-28 00:00:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 87.1 |
| c3b43bed-59a3-3222-9036-07a57164a013 | -4.1272 | -46.1253 | 2024-11-28 00:00:00 | GOES-16 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 59.2 |
| 9d8a0529-de38-3464-a045-3eb431dd3adf | -9.8364 | -36.1687 | 2024-11-28 00:00:00 | GOES-16 | SÃO MIGUEL DOS CAMPOS | ALAGOAS | Brasil | 2708600 | 27 | 33 | nan | nan | nan | Mata Atlântica | 112.3 |
| 458cc540-8c64-315f-a71d-567396df305c | -1.3329 | -51.9257 | 2024-11-28 00:00:00 | GOES-16 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 82.5 |
| e881d872-cb9f-3314-9a5b-7809f5dddb42 | -2.861 | -46.8406 | 2024-11-28 00:00:00 | GOES-16 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 159.0 |
| 75710bc5-f218-3524-802d-bf8247b0365d | -2.8609 | -46.8626 | 2024-11-28 00:00:00 | GOES-16 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 166.6 |
| 799340b4-e9f5-37e7-8c0d-fa8474a0da75 | 0.9857 | -50.1224 | 2024-11-28 00:00:00 | GOES-16 | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 27.2 |
| 9f4fb8b9-185a-3735-a8b4-6e76794d297a | -6.1737 | -42.5985 | 2024-11-28 00:00:00 | GOES-16 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 57.9 |
| 2ae0b827-3223-39a3-8b7d-4e6401724a03 | -6.1039 | -43.9824 | 2024-11-28 00:00:00 | GOES-16 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 71.8 |
| cf7f8a28-b969-33c5-8b6e-339a1d92bcd9 | -3.1114 | -53.8041 | 2024-11-28 00:00:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 70.9 |
| f393a71b-ea47-3196-b082-dbe1c10a0d1f | -3.1113 | -53.8242 | 2024-11-28 00:00:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 85.0 |
| c65e4e82-ee56-3069-a655-02dcc4263b31 | -3.3837 | -50.1125 | 2024-11-28 00:00:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 126.0 |
| 366e5d16-7a0d-322f-8304-f36176838f9c | -2.6147 | -53.9768 | 2024-11-28 00:00:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 62.1 |
| 02023193-ce08-3cbc-b7e0-02fe4af50dd0 | -6.086 | -48.0557 | 2024-11-28 00:00:00 | GOES-16 | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | 106.5 |
| 5e015e80-9b34-3b66-9cd7-2a64a1b0bd46 | -6.0862 | -48.0339 | 2024-11-28 00:00:00 | GOES-16 | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | 238.1 |
| 70b5d657-329e-3c64-bc24-73833599ef64 | -3.9674 | -48.0851 | 2024-11-28 00:00:00 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 35.0 |
| 57085bdd-d26f-3bb6-8078-96ea80f4a188 | -3.6643 | -45.7899 | 2024-11-28 00:00:00 | GOES-16 | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 115.7 |
| cbf91da1-db1b-348c-abc7-5258d56acb77 | -3.683 | -45.7667 | 2024-11-28 00:00:00 | GOES-16 | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 74.1 |
| 6919cd91-b963-3c68-9f56-c928b8146e56 | -5.979 | -45.3395 | 2024-11-28 00:00:00 | GOES-16 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 112.8 |
| eef32f86-ecc5-3d2f-a083-68ad8530a346 | -4.1273 | -46.103 | 2024-11-28 00:00:00 | GOES-16 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 56.1 |
| 95e5e8ca-1327-3b88-9b6e-b8c70684b883 | -9.8359 | -36.1958 | 2024-11-28 00:00:00 | GOES-16 | JEQUIÁ DA PRAIA | ALAGOAS | Brasil | 2703759 | 27 | 33 | nan | nan | nan | Mata Atlântica | 109.5 |
| 1b74eed4-dc6c-378d-9dd6-a8843529a8f9 | -5.9975 | -45.3607 | 2024-11-28 00:00:00 | GOES-16 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 78.1 |
| 16a466a5-50e8-3904-8b75-7808b117e5e2 | -2.86 | -46.85 | 2024-11-28 00:00:00 | MSG-03 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c2a262c7-e9e5-3983-a9e9-6c201a250657 | -5.97 | -45.35 | 2024-11-28 00:00:00 | MSG-03 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| d0f1611a-579a-3217-bdfd-d7940e6d1fed | -4.77 | -44.43 | 2024-11-28 00:00:00 | MSG-03 | SANTO ANTÔNIO DOS LOPES | MARANHÃO | Brasil | 2110302 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 9cbba327-8234-3ce8-b13e-79fdee6751d2 | -2.83 | -46.85 | 2024-11-28 00:00:00 | MSG-03 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f4fc575b-8b5c-376b-8c79-5cdd7b1726d8 | -4.74 | -44.42 | 2024-11-28 00:00:00 | MSG-03 | SANTO ANTÔNIO DOS LOPES | MARANHÃO | Brasil | 2110302 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 486606ed-2fc1-3ee6-a0fc-979343c9562b | -5.2573 | -43.082298 | 2024-11-28 00:03:00 | METOP-C | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| f0a10647-3dd3-34f1-b976-6567a0b0aab8 | -9.9751 | -36.449299 | 2024-11-28 00:03:00 | METOP-C | TEOTÔNIO VILELA | ALAGOAS | Brasil | 2709152 | 27 | 33 | nan | nan | nan | Mata Atlântica | nan |
| c11d0ac6-731d-3b25-8bf6-f73706dd9611 | -5.1613 | -41.268902 | 2024-11-28 00:03:00 | METOP-C | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 1364b95e-32b2-3b71-b25d-05158c3a00ce | -3.626 | -45.790798 | 2024-11-28 00:03:00 | METOP-C | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 86ff9b48-086f-374b-9f0a-871f74f4b501 | -3.2807 | -45.480301 | 2024-11-28 00:03:00 | METOP-C | PENALVA | MARANHÃO | Brasil | 2108306 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 358c14c4-0288-33ef-91c6-d8be4e2fdf29 | -3.3184 | -50.088902 | 2024-11-28 00:03:00 | METOP-C | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0e289f5c-9311-3364-b5ac-8bd5cef2a5b2 | -6.0523 | -43.948799 | 2024-11-28 00:03:00 | METOP-C | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| c82b434d-90a3-3a43-8ccd-7531035f5b19 | -4.6054 | -42.367699 | 2024-11-28 00:03:00 | METOP-C | JOSÉ DE FREITAS | PIAUÍ | Brasil | 2205508 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 80cdf895-1ebc-3a55-bbd5-ff49cc8ec784 | -4.7391 | -44.445599 | 2024-11-28 00:03:00 | METOP-C | SANTO ANTÔNIO DOS LOPES | MARANHÃO | Brasil | 2110302 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 3eae875b-6da1-3dae-96a8-e9d0db262700 | -4.7293 | -44.447701 | 2024-11-28 00:03:00 | METOP-C | SANTO ANTÔNIO DOS LOPES | MARANHÃO | Brasil | 2110302 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| c9de1a50-1a5d-3846-865a-13e3099fb36b | -8.3996 | -35.089298 | 2024-11-28 00:03:00 | METOP-C | IPOJUCA | PERNAMBUCO | Brasil | 2607208 | 26 | 33 | nan | nan | nan | Mata Atlântica | nan |
| f5326182-efc3-3c1d-9ac5-ddb3b9db0019 | -5.7774 | -44.095501 | 2024-11-28 00:03:00 | METOP-C | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 733303e5-1f28-3ea1-9383-2fe6640e687e | -2.7974 | -46.836899 | 2024-11-28 00:03:00 | METOP-C | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 1bd8d616-ec57-3d6a-aa20-1642cb1aa6b6 | -2.8266 | -46.830601 | 2024-11-28 00:03:00 | METOP-C | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0336611b-cce7-3dca-bae5-c4c4398b2df5 | -2.486 | -46.904598 | 2024-11-28 00:03:00 | METOP-C | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e89f0f2f-3e0a-3939-868e-a6f5518aa28e | -4.6115 | -42.395 | 2024-11-28 00:03:00 | METOP-C | JOSÉ DE FREITAS | PIAUÍ | Brasil | 2205508 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| b8755bbd-30db-3cf2-a8aa-0a924f6904a8 | -3.8128 | -40.4491 | 2024-11-28 00:03:00 | METOP-C | SOBRAL | CEARÁ | Brasil | 2312908 | 23 | 33 | nan | nan | nan | Caatinga | nan |
| 33c57fb2-b930-344e-a737-4231cda2501f | -6.1198 | -42.623001 | 2024-11-28 00:03:00 | METOP-C | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| e38c09c8-4f2d-3254-9749-a842f0ee196e | -5.267 | -43.080101 | 2024-11-28 00:03:00 | METOP-C | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 26b3cc08-8fe4-35d7-8127-cbe769287ac3 | -2.6688 | -48.854 | 2024-11-28 00:03:00 | METOP-C | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 9a7eefa9-a225-3672-8dc2-7c3b28922366 | -2.2742 | -46.145802 | 2024-11-28 00:03:00 | METOP-C | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 2d25776a-fb6b-3559-b7d8-40f47eb674f8 | -2.8169 | -46.832699 | 2024-11-28 00:03:00 | METOP-C | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 9b5b1b76-d672-3dcb-989c-4ea6996199ca | -8.4539 | -35.101002 | 2024-11-28 00:03:00 | METOP-C | IPOJUCA | PERNAMBUCO | Brasil | 2607208 | 26 | 33 | nan | nan | nan | Mata Atlântica | nan |
| bd43d9f7-732c-3f68-84f4-4a6ffecc8f5d | -10.0516 | -36.512402 | 2024-11-28 00:03:00 | METOP-C | IGREJA NOVA | ALAGOAS | Brasil | 2703205 | 27 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 31b2a923-abfc-3d6a-9b76-9c2c4210c31c | -6.8752 | -38.140202 | 2024-11-28 00:03:00 | METOP-C | SOUSA | PARAÍBA | Brasil | 2516201 | 25 | 33 | nan | nan | nan | Caatinga | nan |
| 1ce32765-0403-3d34-b589-c36faff071f3 | -2.8012 | -46.853699 | 2024-11-28 00:03:00 | METOP-C | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 9a91e848-fb0f-3fa7-b69e-47f7de50d049 | -5.0269 | -44.822899 | 2024-11-28 00:03:00 | METOP-C | JOSELÂNDIA | MARANHÃO | Brasil | 2105609 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 19b0d2f7-5e29-3cdf-bdb5-425d018807f9 | -5.6415 | -39.516102 | 2024-11-28 00:03:00 | METOP-C | MOMBAÇA | CEARÁ | Brasil | 2308500 | 23 | 33 | nan | nan | nan | Caatinga | nan |
| 34be27ad-1ddb-3d29-b19c-1fa093f907fe | -1.9603 | -46.386299 | 2024-11-28 00:03:00 | METOP-C | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0182aea5-9bc5-3b4f-9a13-d0b0186d2e15 | -4.0735 | -46.1049 | 2024-11-28 00:03:00 | METOP-C | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| f45a4434-135e-3362-b8bb-074acc968f69 | -2.674 | -48.877102 | 2024-11-28 00:03:00 | METOP-C | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0e9861b5-65e6-3104-b344-73bec27f4c82 | -5.1449 | -44.2435 | 2024-11-28 00:03:00 | METOP-C | GONÇALVES DIAS | MARANHÃO | Brasil | 2104404 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| e5f267ad-568a-365d-8f71-8d25e569eece | -2.3374 | -47.151199 | 2024-11-28 00:03:00 | METOP-C | GARRAFÃO DO NORTE | PARÁ | Brasil | 1503077 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c92c4809-f4bf-3ffa-8b33-6cec0bad1767 | -2.4674 | -45.186901 | 2024-11-28 00:03:00 | METOP-C | PINHEIRO | MARANHÃO | Brasil | 2108603 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 5fad2b59-8fed-3d72-8a57-05995c9458f2 | -3.2593 | -46.345798 | 2024-11-28 00:03:00 | METOP-C | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 8d007c4b-3f95-3a72-ba56-5f4430ec0fe3 | -3.9051 | -41.4939 | 2024-11-28 00:03:00 | METOP-C | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 6097ce4f-035b-3410-9e05-08c4d99717b5 | -3.9129 | -48.0541 | 2024-11-28 00:03:00 | METOP-C | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d737826f-6094-3a7e-857c-3ab04f6b1ad9 | -6.1017 | -39.272999 | 2024-11-28 00:03:00 | METOP-C | ACOPIARA | CEARÁ | Brasil | 2300309 | 23 | 33 | nan | nan | nan | Caatinga | nan |
| f5902ae3-62ba-35f0-8760-f2557311c402 | -4.9596 | -38.017601 | 2024-11-28 00:03:00 | METOP-C | RUSSAS | CEARÁ | Brasil | 2311801 | 23 | 33 | nan | nan | nan | Caatinga | nan |
| 25721ac5-7f17-3ed3-acf0-958ed8a55dc5 | -3.9835 | -46.528702 | 2024-11-28 00:03:00 | METOP-C | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 3838fd14-4960-3a4a-834f-ba7ed3ed5444 | -8.8481 | -35.949501 | 2024-11-28 00:03:00 | METOP-C | SÃO BENEDITO DO SUL | PERNAMBUCO | Brasil | 2612901 | 26 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 92a91593-fce5-3463-9ff6-bad80ef16c37 | -4.108 | -43.817799 | 2024-11-28 00:03:00 | METOP-C | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 341160c5-fea3-3952-9ce5-09cc9efe4cb2 | -9.1256 | -44.724701 | 2024-11-28 00:03:00 | METOP-C | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| ed8a15ac-2246-366e-b137-91e2e15c38a9 | -4.4573 | -42.073799 | 2024-11-28 00:03:00 | METOP-C | BOQUEIRÃO DO PIAUÍ | PIAUÍ | Brasil | 2201945 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 96048e46-826b-3876-889e-3ce72cc08d7a | -8.4507 | -43.266998 | 2024-11-28 00:03:00 | METOP-C | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | nan |


[Clique aqui para ver as próximas entradas](README2.md)
