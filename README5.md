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

## Dados Diários - Página 5

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 702c141b-d164-3d54-a631-95aa14450550 | -2.6325 | -48.4775 | 2024-11-16 00:30:00 | GOES-16 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 38.0 |
| 8439baff-d25d-3b06-90b4-7b936c358d29 | -2.1562 | -53.7241 | 2024-11-16 00:30:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 144.5 |
| c9193c20-0753-3513-a0f0-07e3e2c66333 | -3.1456 | -54.5459 | 2024-11-16 00:30:00 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 88.9 |
| ec99807e-bbda-3478-be66-785e0cbb652b | -3.6255 | -53.9912 | 2024-11-16 00:30:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 54.0 |
| 9581a52b-e246-3d3e-9b1c-faa15515ed23 | -4.2311 | -50.6684 | 2024-11-16 00:30:00 | GOES-16 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 56.2 |
| 5d489dab-0723-3486-b1c3-cb398b5118d8 | -2.1379 | -53.7043 | 2024-11-16 00:30:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 120.9 |
| 6e369d88-de9e-3264-ab28-74d78e1be356 | -2.1562 | -53.7039 | 2024-11-16 00:30:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 225.5 |
| 3d852ce5-fcaa-3d25-8b98-ee74e3245d6c | -3.1273 | -54.5264 | 2024-11-16 00:30:00 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 115.9 |
| 40ffd126-95d9-32b6-8802-83a4bba7bd56 | -2.651 | -48.477 | 2024-11-16 00:30:00 | GOES-16 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 64.2 |
| f3271e7a-de2a-3cce-bfe3-8e79e1142de6 | -17.5882 | -57.4711 | 2024-11-16 00:30:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 92.1 |
| 617e1490-9906-35f6-adec-c6052a589a1f | -17.5678 | -57.5146 | 2024-11-16 00:30:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 56.6 |
| 4225d13c-b703-36f8-98db-55288165f06c | -3.5851 | -50.5255 | 2024-11-16 00:30:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 91.1 |
| 4fe7c34b-2999-3126-8557-eb549fe656e5 | -2.3741 | -54.6626 | 2024-11-16 00:30:00 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 68.9 |
| df58bc5c-0c19-392a-943f-be634127bec4 | -2.1576 | -46.5527 | 2024-11-16 00:30:00 | GOES-16 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 65.6 |
| edf4d0e1-dbfe-3014-91ea-48fb4efef877 | -3.7394 | -45.6523 | 2024-11-16 00:30:00 | GOES-16 | TUFILÂNDIA | MARANHÃO | Brasil | 2112274 | 21 | 33 | nan | nan | nan | Amazônia | 55.4 |
| 2b986d62-a7b2-3e89-a007-e5d795e5abe2 | -2.1563 | -53.6838 | 2024-11-16 00:40:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 67.9 |
| 4bfce783-d2e5-3fd9-a6ec-b61326433cc0 | -17.5675 | -57.5351 | 2024-11-16 00:40:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 56.0 |
| 382f08c3-b193-3ab7-9fd6-3a60b6cbb678 | -3.4898 | -47.2127 | 2024-11-16 00:40:00 | GOES-16 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 48.0 |
| 20752134-0869-3ed9-b37c-738d7d6cdf70 | -3.1456 | -54.5259 | 2024-11-16 00:40:00 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 117.4 |
| 28c5a675-ff59-33c4-8980-cc99efe6b820 | -2.7801 | -48.5592 | 2024-11-16 00:40:00 | GOES-16 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 104.4 |
| 540f5e94-537f-3402-b6e7-7cf88dc12ee0 | -3.1456 | -54.5459 | 2024-11-16 00:40:00 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 85.0 |
| 1885ad53-7c18-37ac-b338-c4148f70f6a9 | -3.5083 | -47.212 | 2024-11-16 00:40:00 | GOES-16 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 50.4 |
| fe2b858c-ac58-30f6-9634-53a0e934c457 | -3.3688 | -45.4215 | 2024-11-16 00:40:00 | GOES-16 | MONÇÃO | MARANHÃO | Brasil | 2106904 | 21 | 33 | nan | nan | nan | Amazônia | 59.0 |
| e1f1883b-967a-3145-905b-eab7475c0681 | -2.1562 | -53.7241 | 2024-11-16 00:40:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 165.9 |
| dc6bd30d-509b-34b1-91b7-42bca59c0746 | -2.5766 | -54.4388 | 2024-11-16 00:40:00 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 64.3 |
| d2b375fe-3326-3642-8cf4-82a0ad23a205 | -2.6131 | -54.5381 | 2024-11-16 00:40:00 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 62.6 |
| c818a100-dded-3b73-8991-9bd0c78b2cad | -3.0357 | -45.0967 | 2024-11-16 00:40:00 | GOES-16 | MATINHA | MARANHÃO | Brasil | 2106508 | 21 | 33 | nan | nan | nan | Amazônia | 64.7 |
| 42dddd13-fac5-3707-807c-aaa9a7639436 | -2.1378 | -53.7244 | 2024-11-16 00:40:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 81.4 |
| fc373983-7757-3915-be6e-d4c586ef8379 | -2.1562 | -53.7039 | 2024-11-16 00:40:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 249.6 |
| c6ea24b5-9062-3edf-9fdb-e10d239f1b0a | -2.7615 | -48.5812 | 2024-11-16 00:40:00 | GOES-16 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 76.5 |
| 49671917-b4a4-3b4e-9126-494f961846af | -16.9384 | -57.6291 | 2024-11-16 00:40:00 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 52.6 |
| 5363ed08-8b60-367a-aad2-e88856dc2424 | -2.1746 | -53.7036 | 2024-11-16 00:40:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 54.8 |
| 197d9182-079e-37d7-8cba-2036b7e8289d | -3.7685 | -50.7908 | 2024-11-16 00:40:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 59.9 |
| d7bf1e4d-59ed-33d1-afce-31b5923df98b | -3.1273 | -54.5264 | 2024-11-16 00:40:00 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 83.3 |
| 7ce54ca3-5956-3e68-afde-e2cb4de8ba6d | -2.1379 | -53.7043 | 2024-11-16 00:40:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 94.3 |
| e7d2e1c3-41b2-3027-86f2-02035c4e683e | -3.5851 | -50.5255 | 2024-11-16 00:40:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 82.8 |
| 3baa190a-7620-3b54-b21a-f1d1952515ea | -2.7985 | -48.5801 | 2024-11-16 00:40:00 | GOES-16 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 45.4 |
| 15ed005a-9498-32b1-b2b6-c73e1eea0cf9 | -3.2411 | -53.5181 | 2024-11-16 00:40:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 61.9 |
| dd54c27d-28eb-3392-8425-79004d48b9bc | -4.9971 | -44.3149 | 2024-11-16 00:40:00 | GOES-16 | DOM PEDRO | MARANHÃO | Brasil | 2103802 | 21 | 33 | nan | nan | nan | Cerrado | 53.6 |
| 73dc8b17-0caa-30c6-ae85-5e1e97d84170 | -2.7986 | -48.5586 | 2024-11-16 00:40:00 | GOES-16 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 67.0 |
| e48dc0ec-4a64-3634-9479-ea61610a750c | -3.1272 | -54.5464 | 2024-11-16 00:40:00 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 66.3 |
| 175bb23c-dbb6-329e-ae98-dd1b2ce6051d | -2.78 | -48.5806 | 2024-11-16 00:40:00 | GOES-16 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 158.3 |
| b4ca6922-5ca8-389a-b76b-c3c26c2e720e | -2.5767 | -54.4188 | 2024-11-16 00:40:00 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 81.0 |
| b272ac84-af4f-3e41-970c-14c6dc9bea58 | -2.651 | -48.477 | 2024-11-16 00:40:00 | GOES-16 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 37.0 |
| b31389e0-6c45-3da5-a646-fbc93cefcba7 | -2.3741 | -54.6626 | 2024-11-16 00:40:00 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 64.6 |
| 699e8278-6824-336b-ba41-d6fa61b2662f | -10.5381 | -44.68 | 2024-11-16 00:47:00 | METOP-C | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 9155cddb-82be-3398-a279-149e21224f67 | -2.3651 | -54.653 | 2024-11-16 00:47:00 | METOP-C | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0a1a1a30-b777-3b19-8b9d-cb0a3f99e104 | -3.0292 | -45.114799 | 2024-11-16 00:47:00 | METOP-C | MATINHA | MARANHÃO | Brasil | 2106508 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 62f8d4ec-fb69-3e0e-8777-3a21db286398 | -3.6242 | -53.987499 | 2024-11-16 00:47:00 | METOP-C | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 9cf36787-2dbd-35f2-9b30-de48fc825103 | -4.2299 | -50.6688 | 2024-11-16 00:47:00 | METOP-C | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d3aad2d8-af20-3364-b763-75009ba57b57 | -3.0693 | -48.011398 | 2024-11-16 00:47:00 | METOP-C | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 36de8239-d160-300a-8515-81cfa6e70a17 | -3.2542 | -53.6716 | 2024-11-16 00:47:00 | METOP-C | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 2f5d14f0-83f2-3176-91bf-1fdf19a6b106 | -2.3435 | -47.462299 | 2024-11-16 00:47:00 | METOP-C | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| fce889a1-a4a2-3cf9-b047-ed64ad6776d5 | -3.1373 | -54.519199 | 2024-11-16 00:47:00 | METOP-C | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 13e70798-3ae4-3d8f-8a46-2254a362fbcf | -1.8871 | -50.799301 | 2024-11-16 00:47:00 | METOP-C | MELGAÇO | PARÁ | Brasil | 1504505 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 913e0817-9cb8-3ce0-a951-35bcba1122d7 | -1.8887 | -50.806198 | 2024-11-16 00:47:00 | METOP-C | MELGAÇO | PARÁ | Brasil | 1504505 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 61af2940-67ff-3168-ba64-f9bc83cdff88 | -2.6415 | -54.6464 | 2024-11-16 00:47:00 | METOP-C | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 72e7ee65-9b25-37e7-913d-a3035f885756 | -0.3067 | -51.509701 | 2024-11-16 00:47:00 | METOP-C | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | nan |
| 2cb307bf-aeff-3499-89a0-23198b96b8c5 | -3.3728 | -45.436199 | 2024-11-16 00:47:00 | METOP-C | MONÇÃO | MARANHÃO | Brasil | 2106904 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| bfef9fb6-a8aa-321e-b4c1-764d4d6d4d96 | -3.3955 | -45.227299 | 2024-11-16 00:47:00 | METOP-C | CAJARI | MARANHÃO | Brasil | 2102507 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| f2ff7e96-04e1-3585-bb7c-d8e277cfbdb6 | -4.3783 | -45.636799 | 2024-11-16 00:47:00 | METOP-C | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| a44f3f75-42b4-3cca-a185-8a7d9b8be244 | -4.1827 | -45.637901 | 2024-11-16 00:47:00 | METOP-C | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 56b85f5b-14b9-311e-8547-a01bdfa19635 | -3.3225 | -51.6614 | 2024-11-16 00:47:00 | METOP-C | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e6cc4b6e-d4e4-310a-a5e4-5b7fdcbf818e | -4.3758 | -45.626301 | 2024-11-16 00:47:00 | METOP-C | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 2dfec47e-c189-3c24-a9d4-bf694115f570 | -2.1523 | -46.421299 | 2024-11-16 00:47:00 | METOP-C | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 78090928-1c2b-3072-998b-d61ea7c0bf1d | -3.8841 | -52.271 | 2024-11-16 00:47:00 | METOP-C | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| eccff317-faa2-3958-ba05-cd44008fe3ee | -3.5737 | -52.220699 | 2024-11-16 00:47:00 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 48bca8cf-19d4-3f37-9caa-021427ffa8f7 | -2.3753 | -50.4095 | 2024-11-16 00:47:00 | METOP-C | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 25e11694-9b71-38a0-9e66-7aa032c05c3a | -3.0362 | -45.100601 | 2024-11-16 00:47:00 | METOP-C | MATINHA | MARANHÃO | Brasil | 2106508 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 581bd2b4-66b9-33fd-ac8c-dd06039b0c72 | -8.2762 | -45.972801 | 2024-11-16 00:47:00 | METOP-C | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 6fecb4b1-66ad-32ac-afb4-973b2060a693 | -3.1412 | -54.536499 | 2024-11-16 00:47:00 | METOP-C | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 4925f4c1-c999-36a4-a798-84262ba6ba8f | -3.9878 | -45.859299 | 2024-11-16 00:47:00 | METOP-C | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 0219d245-faed-3b81-9848-14453291422c | -4.3749 | -48.0802 | 2024-11-16 00:47:00 | METOP-C | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 2b800704-6c25-3321-aaa9-fb258eb3923a | -6.0272 | -48.040501 | 2024-11-16 00:47:00 | METOP-C | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 576fcfce-6021-38ff-8c98-3b16c134dec3 | -4.5556 | -48.0144 | 2024-11-16 00:47:00 | METOP-C | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f73a0776-45e6-3d15-aa04-9063c181dd80 | -0.6476 | -49.401699 | 2024-11-16 00:47:00 | METOP-C | SANTA CRUZ DO ARARI | PARÁ | Brasil | 1506401 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b1f610c6-1447-354e-9567-0f19dcf6f8d8 | -3.1959 | -45.5592 | 2024-11-16 00:47:00 | METOP-C | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| d18165c3-fdef-3b5a-94b3-04a1bffc6c49 | -3.5787 | -50.528198 | 2024-11-16 00:47:00 | METOP-C | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 6adc589d-f500-3cdd-bfc3-1d67b6ce269b | -2.001 | -46.434601 | 2024-11-16 00:47:00 | METOP-C | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 3f8c9c13-cf69-3277-abd7-7289312c7227 | -3.1392 | -54.527901 | 2024-11-16 00:47:00 | METOP-C | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| eb2f6441-ffa0-3395-85e5-8e4eb71c0b9c | -2.6491 | -46.167999 | 2024-11-16 00:47:00 | METOP-C | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| c8a117f1-77fb-3e95-8646-da0c0676a58e | -4.7252 | -48.122299 | 2024-11-16 00:47:00 | METOP-C | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e8a45f86-07eb-3fce-9d09-24b178cc8db3 | -2.6515 | -46.178299 | 2024-11-16 00:47:00 | METOP-C | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 20f82e0c-7eca-357c-b12f-a14a698875ac | -4.3669 | -48.090302 | 2024-11-16 00:47:00 | METOP-C | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 4c992a33-8e07-32ff-a800-d93d064e8d12 | -1.5784 | -50.443298 | 2024-11-16 00:47:00 | METOP-C | BREVES | PARÁ | Brasil | 1501808 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c1093130-fd01-3c9a-974d-9c5404612447 | -17.5916 | -57.591202 | 2024-11-16 00:47:00 | METOP-C | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| cd64c265-9443-3a54-b5b5-e73066eeaa36 | -2.6441 | -48.490101 | 2024-11-16 00:47:00 | METOP-C | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d0509072-7141-3b52-b1f4-dd30437584b1 | -6.2985 | -39.464199 | 2024-11-16 00:47:00 | METOP-C | ACOPIARA | CEARÁ | Brasil | 2300309 | 23 | 33 | nan | nan | nan | Caatinga | nan |
| 7718ab50-bb83-3f97-8ea7-027cd81f6531 | -17.5508 | -57.529202 | 2024-11-16 00:47:00 | METOP-C | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 3e4d754f-07d3-3c2c-a9f4-d4897d0a749a | -3.1948 | -54.318199 | 2024-11-16 00:47:00 | METOP-C | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c88dad47-cfcc-3011-b01a-5769a70ecaf3 | -1.2309 | -53.697701 | 2024-11-16 00:47:00 | METOP-C | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 3a057d8a-182d-398b-9483-3079866273b2 | -3.6503 | -49.942101 | 2024-11-16 00:47:00 | METOP-C | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 266b63d1-ebf6-39a8-90e8-7a83bf5873da | -4.2807 | -48.2076 | 2024-11-16 00:47:00 | METOP-C | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 9d2993c5-47d9-355b-bd0b-58af35353ba8 | -3.5027 | -47.216301 | 2024-11-16 00:47:00 | METOP-C | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 9ab43eed-beba-3da5-a88c-ac7178800f54 | -3.5051 | -51.017101 | 2024-11-16 00:47:00 | METOP-C | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e8757e86-67e5-3e3c-87b2-6f39a62e5993 | -3.6884 | -50.1077 | 2024-11-16 00:47:00 | METOP-C | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d958cff1-9e2f-3e6b-9e2e-eda126d16f88 | -3.9487 | -50.208 | 2024-11-16 00:47:00 | METOP-C | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0e4326f0-ade0-3077-bcf4-fec03c786c28 | -3.1294 | -54.529999 | 2024-11-16 00:47:00 | METOP-C | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 04a8235f-dab7-33d9-97b0-514974807de1 | -6.0254 | -48.033001 | 2024-11-16 00:47:00 | METOP-C | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 4435681a-c447-37a8-8ce2-0f9f0493f1e3 | -2.4113 | -47.797901 | 2024-11-16 00:47:00 | METOP-C | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | nan |


[Clique aqui para ver as próximas entradas](README6.md)
