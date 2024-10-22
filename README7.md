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

## Dados Diários - Página 7

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 837979b0-e139-379f-aef8-ad8b7c3b7170 | -3.9977 | -46.0202 | 2024-10-22 00:55:29 | GOES-16 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 108.8 |
| 1185bf46-8726-322d-a881-a400550720c7 | -4.0163 | -46.0193 | 2024-10-22 00:55:29 | GOES-16 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 90.6 |
| 7b98ed4f-c55e-33f7-afc6-ac7c73bf5e6e | -5.2305 | -43.1886 | 2024-10-22 00:55:36 | GOES-16 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 67.8 |
| ef9edd90-4dd3-330d-997f-cb96825610f5 | -5.5716 | -44.8927 | 2024-10-22 00:55:38 | GOES-16 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 57.0 |
| 802748fd-85d3-3aa6-a063-3b30a7a9c2b4 | -5.5718 | -44.87 | 2024-10-22 00:55:38 | GOES-16 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 88.5 |
| 639f7245-628c-30b2-858d-10de0f57516d | -5.5903 | -44.8914 | 2024-10-22 00:55:38 | GOES-16 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 68.3 |
| 0df8b54f-1b38-3dce-a747-766b77928d04 | -5.5905 | -44.8687 | 2024-10-22 00:55:38 | GOES-16 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 99.9 |
| 509c361d-8eb9-3c14-aa2f-71beb6c65ad7 | -5.9487 | -35.369 | 2024-10-22 00:55:39 | GOES-16 | MACAÍBA | RIO GRANDE DO NORTE | Brasil | 2407104 | 24 | 33 | nan | nan | nan | Caatinga | 63.0 |
| 0c14cc26-e342-3689-a507-c39fb9e60d40 | -5.949 | -35.3418 | 2024-10-22 00:55:39 | GOES-16 | MACAÍBA | RIO GRANDE DO NORTE | Brasil | 2407104 | 24 | 33 | nan | nan | nan | Caatinga | 126.4 |
| a69ecd44-9645-3b00-b7f7-11e0edd53c6d | -6.2334 | -44.1565 | 2024-10-22 00:55:41 | GOES-16 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 67.3 |
| 8b1cf6eb-b317-3cbc-b525-666ffa0d586a | -6.2336 | -44.1335 | 2024-10-22 00:55:41 | GOES-16 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 89.5 |
| c0ade7d6-6b93-3350-8f5f-3d579d850252 | -6.2522 | -44.155 | 2024-10-22 00:55:41 | GOES-16 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 62.7 |
| d15ea1b3-2a12-36c0-bb17-261dee48af73 | -6.2524 | -44.132 | 2024-10-22 00:55:41 | GOES-16 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 84.8 |
| a3a6be9a-1819-3706-8886-3311fac378a0 | -7.8245 | -61.3709 | 2024-10-22 00:55:51 | GOES-16 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 69.4 |
| d7803d25-56aa-3bf2-b849-0ae61ebb7045 | -12.4778 | -63.1885 | 2024-10-22 00:56:17 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 54.1 |
| 474783af-675c-3062-a240-e00c183b8741 | -12.5336 | -63.3003 | 2024-10-22 00:56:18 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 49.4 |
| 48232be8-5f58-3d9a-8d70-186afcd930ef | -14.3218 | -59.3581 | 2024-10-22 00:56:27 | GOES-16 | CAMPOS DE JÚLIO | MATO GROSSO | Brasil | 5102686 | 51 | 33 | nan | nan | nan | Cerrado | 66.2 |
| 7b51ba88-bb34-36ea-9081-1c7cd9ba459d | -14.322 | -59.3382 | 2024-10-22 00:56:27 | GOES-16 | CAMPOS DE JÚLIO | MATO GROSSO | Brasil | 5102686 | 51 | 33 | nan | nan | nan | Cerrado | 80.9 |
| 24760f76-9167-35b7-9698-40e7244fc691 | -17.0213 | -57.3333 | 2024-10-22 00:56:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 90.4 |
| 365994de-d935-366b-8745-6a9ae4f11a4d | -1.1834 | -53.6569 | 2024-10-22 01:05:13 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 65.9 |
| 39dc84c3-29c7-352f-b307-63f5e607b41a | -2.0839 | -53.2405 | 2024-10-22 01:05:18 | GOES-16 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 60.8 |
| 597b667e-9a52-3c5b-a45e-60e3ffb3041f | -2.7404 | -49.3077 | 2024-10-22 01:05:22 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 55.6 |
| b962396c-6638-3a53-acf2-4871a20c4b66 | -2.7588 | -49.3285 | 2024-10-22 01:05:22 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 69.0 |
| 4a54588f-55e3-36a7-871b-2faecb74d765 | -2.7589 | -49.3072 | 2024-10-22 01:05:22 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 91.7 |
| 2de4406f-b11e-36f9-81a0-dfda52792a79 | -2.7773 | -49.3067 | 2024-10-22 01:05:22 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 62.6 |
| 69ee5a1e-b622-3333-9aae-6b0bf0c4a3c6 | -2.8482 | -45.4637 | 2024-10-22 01:05:22 | GOES-16 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 113.2 |
| c46be359-0b5b-3d10-aacf-4360b02f8c8c | -2.8668 | -45.4631 | 2024-10-22 01:05:22 | GOES-16 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 91.0 |
| 20dab154-860d-3825-b814-be22934e9733 | -2.9574 | -50.5245 | 2024-10-22 01:05:23 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 91.5 |
| 75093664-cc40-3870-b166-3fd57e272cba | -3.0581 | -53.2395 | 2024-10-22 01:05:24 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 61.1 |
| 1d95c5bc-a3c1-3c5c-8be6-ea8eca8566a9 | -3.0654 | -51.2506 | 2024-10-22 01:05:24 | GOES-16 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 55.6 |
| ac7057bc-075d-3f95-a1f1-26babeb6cb65 | -3.0765 | -53.2593 | 2024-10-22 01:05:24 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 55.8 |
| cc3b49b6-4ac3-3221-aea9-edf467793412 | -3.0765 | -53.239 | 2024-10-22 01:05:24 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 62.6 |
| eb090f36-4545-32ac-893d-957f1df84b81 | -3.0837 | -51.2708 | 2024-10-22 01:05:24 | GOES-16 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 66.6 |
| 2e3fb4bf-6e52-37de-bb1e-d5a8b56aad2e | -3.0838 | -51.25 | 2024-10-22 01:05:24 | GOES-16 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 75.1 |
| 1aff085a-dea7-3375-896a-f64eb27e9d6f | -3.0917 | -54.1867 | 2024-10-22 01:05:24 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 59.8 |
| 380c099d-1a59-3759-9934-7014cb9d2603 | -3.0917 | -54.1666 | 2024-10-22 01:05:24 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 131.1 |
| 16c7b3ce-4ead-38a3-aefe-2c6315b2cf7a | -3.0918 | -54.1465 | 2024-10-22 01:05:24 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 85.8 |
| 2168b807-66bb-3e0b-9b1b-122ca3ac223f | -3.11 | -54.1862 | 2024-10-22 01:05:24 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 53.4 |
| 346efdf6-b6ba-3ac9-b2f5-3f30af1cdc50 | -3.1101 | -54.1661 | 2024-10-22 01:05:24 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 99.7 |
| c307fddc-6854-32d5-afac-e5497cc4beec | -3.1102 | -54.146 | 2024-10-22 01:05:24 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 59.3 |
| ab9aea89-b9a6-3c68-8ccb-9d725f096a7c | -3.9977 | -46.0202 | 2024-10-22 01:05:29 | GOES-16 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 107.2 |
| 8bfffb51-eee7-3824-856b-60fc94b7510a | -4.0161 | -46.0416 | 2024-10-22 01:05:29 | GOES-16 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 78.2 |
| f36906dc-7614-3c95-ad4a-df93b1fc7095 | -4.0163 | -46.0193 | 2024-10-22 01:05:29 | GOES-16 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 181.4 |
| dde1563f-b645-39d8-a492-d3ba3e4abd30 | -4.5572 | -45.8128 | 2024-10-22 01:05:32 | GOES-16 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 57.9 |
| 2196ec4d-5ab2-3bfd-957f-2db12f6d949d | -4.5574 | -45.7905 | 2024-10-22 01:05:32 | GOES-16 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 49.0 |
| 790d6892-3e94-373a-b0a9-7e3bd61f0453 | -5.2305 | -43.1886 | 2024-10-22 01:05:36 | GOES-16 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 53.5 |
| 24e9a0fc-0c8e-3fe2-add0-e8aa24ce50fb | -5.5718 | -44.87 | 2024-10-22 01:05:38 | GOES-16 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 99.1 |
| d6cad775-c86c-3bcd-8488-597b0f150c0e | -5.5903 | -44.8914 | 2024-10-22 01:05:38 | GOES-16 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 81.5 |
| f960e342-0284-3e17-9541-955b9170e101 | -5.5905 | -44.8687 | 2024-10-22 01:05:38 | GOES-16 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 138.3 |
| e1ab895b-0420-37ca-9d35-a4bff3760b0b | -6.2334 | -44.1565 | 2024-10-22 01:05:41 | GOES-16 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 60.1 |
| 5822ff1d-9cab-3f45-9314-9c00f4f6d5f0 | -6.2336 | -44.1335 | 2024-10-22 01:05:41 | GOES-16 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 78.9 |
| 5e1479a0-80fb-37d7-af85-481b0357f031 | -6.2522 | -44.155 | 2024-10-22 01:05:41 | GOES-16 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 48.3 |
| f9963c41-8528-3d04-973d-ad5e9aeab2f5 | -6.2524 | -44.132 | 2024-10-22 01:05:41 | GOES-16 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 66.2 |
| f62993d6-6fc3-32cf-aa7f-440e3d9df1b5 | -7.8245 | -61.3709 | 2024-10-22 01:05:51 | GOES-16 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 66.7 |
| 41bf0164-d6d3-3ec2-ad66-b6b40a36e043 | -12.5167 | -63.0521 | 2024-10-22 01:06:18 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 66.7 |
| dafe9af7-54bb-3e38-89ee-0f8eeafe0dd8 | -12.5356 | -63.051 | 2024-10-22 01:06:18 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 56.9 |
| 3f01f543-a3ce-3f43-9b94-015c55b17fd4 | -17.0213 | -57.3333 | 2024-10-22 01:06:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 91.5 |
| 855aed37-5eb8-30c3-b443-35ce109047f3 | -16.9189 | -52.017601 | 2024-10-22 01:09:37 | METOP-C | CAIAPÔNIA | GOIÁS | Brasil | 5204409 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| f5df6192-cddf-3e30-8ea1-06634fc5488b | -16.9205 | -52.0247 | 2024-10-22 01:09:37 | METOP-C | CAIAPÔNIA | GOIÁS | Brasil | 5204409 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 7ea073b5-79dc-328b-8904-7ef090981363 | -16.980801 | -55.992802 | 2024-10-22 01:09:50 | METOP-C | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 1f60122c-1ecc-3669-bfc3-c8446be36ee4 | -16.9827 | -56.001999 | 2024-10-22 01:09:50 | METOP-C | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 72ea7f62-6da6-3662-a4bf-a0a01f1450c6 | -16.971001 | -55.994999 | 2024-10-22 01:09:50 | METOP-C | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 5404d10f-3ce0-3001-a384-b84c6d48d94e | -16.9729 | -56.004101 | 2024-10-22 01:09:50 | METOP-C | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 167f012b-25ff-34b0-bb06-5494a42f8b40 | -17.2101 | -57.2845 | 2024-10-22 01:09:50 | METOP-C | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 3842a290-95a2-34ca-acc0-9535ffe301c9 | -17.2122 | -57.295399 | 2024-10-22 01:09:50 | METOP-C | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 590d4a53-5c4e-3adf-8aab-02d0a516f7dd | -17.214399 | -57.306301 | 2024-10-22 01:09:50 | METOP-C | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 95da4e85-7e9f-3393-b2b0-bb2de5438a34 | -17.1614 | -57.5019 | 2024-10-22 01:09:52 | METOP-C | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| d0693663-52c3-3031-9f71-32ab31e67aee | -17.1516 | -57.504002 | 2024-10-22 01:09:52 | METOP-C | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 97831c52-1c12-30f4-9d23-051a420a2845 | -17.0114 | -57.463402 | 2024-10-22 01:09:54 | METOP-C | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 6d34dfff-9678-3230-9935-158029b4b414 | -17.013599 | -57.474499 | 2024-10-22 01:09:54 | METOP-C | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| d4677cda-55c2-3ef4-8549-02902a7ad1a7 | -16.973301 | -57.322498 | 2024-10-22 01:09:54 | METOP-C | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| c17aa756-3c4e-3a28-8e8b-832e99e952fb | -16.9755 | -57.333401 | 2024-10-22 01:09:54 | METOP-C | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| d420f0ca-ec5e-3960-b3c9-ea73bf7299df | -16.963499 | -57.3246 | 2024-10-22 01:09:54 | METOP-C | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 6f574972-a85f-3a36-9781-06fb71636669 | -16.9657 | -57.335499 | 2024-10-22 01:09:54 | METOP-C | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| aab041e6-c25a-3bc3-97af-c3940a8d09b7 | -16.9701 | -57.4603 | 2024-10-22 01:09:55 | METOP-C | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| ce23c986-8e0d-37cb-8296-85a3053435b2 | -16.966801 | -57.4958 | 2024-10-22 01:09:55 | METOP-C | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 85f2886f-e96b-370c-ba36-dadb03130b9d | -16.9571 | -57.497799 | 2024-10-22 01:09:55 | METOP-C | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| a3b559a0-fc5c-3244-8b4e-9e0513b45465 | -16.959299 | -57.5089 | 2024-10-22 01:09:55 | METOP-C | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| d62474e7-df7d-39c2-93d2-01f3967e64e3 | -16.9615 | -57.5201 | 2024-10-22 01:09:55 | METOP-C | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| b878c040-f923-3ac0-9a88-ea0a3fe78ea0 | -16.949499 | -57.511002 | 2024-10-22 01:09:55 | METOP-C | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 0dad0c13-f362-3578-a517-51d0ff4e4d5b | -16.9104 | -57.519001 | 2024-10-22 01:09:56 | METOP-C | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 7dd16d59-b4a1-3b16-bd6b-c297f2075e84 | -16.898399 | -57.509998 | 2024-10-22 01:09:56 | METOP-C | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 025cedb9-cc5f-3d6f-a98e-ac02b6b40154 | -16.9006 | -57.521099 | 2024-10-22 01:09:56 | METOP-C | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 8c103acc-0df2-358e-a05c-096c0a2aa180 | -16.902901 | -57.532299 | 2024-10-22 01:09:56 | METOP-C | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 3393e865-d45f-3ddf-b650-cc4ccd658d6c | -16.1709 | -56.577702 | 2024-10-22 01:10:05 | METOP-C | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 3a2d9ba9-f33f-3e9a-bf82-bae0c3a10e08 | -16.1611 | -56.5798 | 2024-10-22 01:10:05 | METOP-C | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 7847192b-c4ba-322f-91be-a98f6a0d2626 | -16.163 | -56.589401 | 2024-10-22 01:10:05 | METOP-C | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| d25f527c-bd43-3af2-bb7b-8881eeff3155 | -15.8988 | -56.645901 | 2024-10-22 01:10:09 | METOP-C | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| d53692e2-6a26-3968-a55c-855b69ca7f15 | -16.2528 | -59.146599 | 2024-10-22 01:10:12 | METOP-C | PORTO ESPERIDIÃO | MATO GROSSO | Brasil | 5106828 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| a318c7f3-0ff9-3f9c-ba43-54d57209a750 | -16.039101 | -60.0956 | 2024-10-22 01:10:18 | METOP-C | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 993c40cb-a5d2-3eae-a483-69b0f1f5a15b | -16.042101 | -60.1115 | 2024-10-22 01:10:18 | METOP-C | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 01f46cd9-f3d1-3117-9952-bcb8e5d087d6 | -16.029301 | -60.0975 | 2024-10-22 01:10:18 | METOP-C | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 002b7797-23b0-35c8-8a6b-856314f7889a | -16.032301 | -60.113499 | 2024-10-22 01:10:18 | METOP-C | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| a5b1b320-a9b9-36ec-8c61-ee3b8fe9eabc | -11.5872 | -58.607601 | 2024-10-22 01:11:26 | METOP-C | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 2afdb545-706a-3c27-ac8a-aa37e5b26891 | -6.1887 | -44.125401 | 2024-10-22 01:11:59 | METOP-C | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| c8ecce3d-90ae-3270-b13c-fa49a3fdff72 | -5.1784 | -43.164799 | 2024-10-22 01:12:11 | METOP-C | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 39ac1962-ec4d-364d-b0a8-5e6bf81acb44 | -5.5356 | -44.867298 | 2024-10-22 01:12:13 | METOP-C | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 948a2f0a-6275-39ee-add3-f2e6ac409582 | -5.5412 | -44.8899 | 2024-10-22 01:12:13 | METOP-C | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 0ad5441d-2ace-3d6b-baa9-ce3c0c0023a2 | -5.526 | -44.869701 | 2024-10-22 01:12:13 | METOP-C | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| b2ca5136-0ace-3c30-aa08-24a18508594b | -5.5316 | -44.8923 | 2024-10-22 01:12:13 | METOP-C | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | nan |


[Clique aqui para ver as próximas entradas](README8.md)
