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

## Dados Diários - Página 39

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 0dc10547-a880-37fd-bd14-c607e9b8b0ad | -4.24441 | -48.6948 | 2024-11-23 04:18:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 5ed180a1-3e29-3ea7-9064-66e92329a0b1 | -4.77801 | -48.08171 | 2024-11-23 04:18:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| a6d7670c-3ca7-3235-8fa9-08521cbcb291 | -4.3458 | -46.01451 | 2024-11-23 04:18:00 | NOAA-20 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 8b59f3cf-72ab-3c3b-a205-2bce5213a10f | -5.29279 | -44.86538 | 2024-11-23 04:18:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| c3b5464a-b3e2-3970-85ce-b9582c0aa61e | -2.45243 | -53.70733 | 2024-11-23 04:18:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 73017f1f-be1f-3142-95cb-00458bd15bce | -4.42002 | -49.69178 | 2024-11-23 04:18:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 28c88ee1-b573-3643-889e-05bf2856b980 | -3.95588 | -46.91174 | 2024-11-23 04:18:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 675704c5-08f7-3883-9633-e3bf5df36a01 | -4.58862 | -46.07456 | 2024-11-23 04:18:00 | NOAA-20 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b8baa244-346b-30a1-be6f-ce8b28c40a02 | -5.10502 | -43.15857 | 2024-11-23 04:18:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 8.6 |
| 2f6a90e2-c952-387e-8042-a5f3617c41ca | -3.70991 | -47.61904 | 2024-11-23 04:18:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 9b83792d-b293-310b-826f-7a30e7f91912 | -2.80224 | -52.46735 | 2024-11-23 04:18:00 | NOAA-20 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 323e9553-3082-3135-b717-94d8946f6086 | -5.65679 | -43.3014 | 2024-11-23 04:18:00 | NOAA-20 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| be3e2a55-7ef5-3241-88c1-aeeb8ebfec1e | -4.52575 | -49.81393 | 2024-11-23 04:18:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 0201e383-b18e-33fa-bbaf-468ae2cb883a | -5.46233 | -43.2428 | 2024-11-23 04:18:00 | NOAA-20 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| bdb63749-5447-38af-9bfd-240e23893453 | -4.07334 | -46.83571 | 2024-11-23 04:18:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| ca985a67-bdb9-3fcc-8d35-8381f7372d57 | -4.08103 | -46.8329 | 2024-11-23 04:18:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 820d9d25-37aa-3624-a8f7-5d8849836d79 | -5.12505 | -47.0319 | 2024-11-23 04:18:00 | NOAA-20 | JOÃO LISBOA | MARANHÃO | Brasil | 2105500 | 21 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 40f61100-8cf8-3315-b3bf-3e75d6565360 | -3.93556 | -47.19693 | 2024-11-23 04:18:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 6.8 |
| 2ed46db6-a826-33f1-acc8-c8778e799fbd | -2.7834 | -51.41314 | 2024-11-23 04:18:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| be50a732-7579-3cd4-a54a-304d7ace16c9 | -4.72027 | -45.49579 | 2024-11-23 04:18:00 | NOAA-20 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 3a951b45-bd1f-3dd3-ab19-b46b7d9432d8 | -4.5418 | -45.88737 | 2024-11-23 04:18:00 | NOAA-20 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 57e7d1f0-eb55-389e-9b1c-33615030dc88 | -4.41924 | -44.11297 | 2024-11-23 04:18:00 | NOAA-20 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 7.8 |
| 3ea3228b-4d2e-329a-8c96-86285e087dc6 | -4.70025 | -45.66418 | 2024-11-23 04:18:00 | NOAA-20 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 88a32c76-8d33-3a33-af8f-01ece690d7dd | -6.09825 | -41.8012 | 2024-11-23 04:18:00 | NOAA-20 | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| e4cad77e-db27-32fe-9152-7f94c76a0ddf | -4.09482 | -51.07818 | 2024-11-23 04:18:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| ca132cfc-9e60-32ae-ab00-ed9357ec2181 | -3.24246 | -54.2275 | 2024-11-23 04:18:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 353be50f-afe3-351b-b7b1-7cd72d2f6e44 | -4.78142 | -43.05444 | 2024-11-23 04:18:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 6601ca9a-defd-32ce-b140-909b83d49428 | -4.27311 | -46.29296 | 2024-11-23 04:18:00 | NOAA-20 | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 425c7622-adb5-3a12-bf59-7bc0c4c8240b | -3.18933 | -54.33211 | 2024-11-23 04:18:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 3014e8b5-d658-3a0b-84d9-048d71e6d54d | -5.81987 | -49.32905 | 2024-11-23 04:18:00 | NOAA-20 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 5d526607-1849-3953-a3a9-5a47e5f33e51 | -3.76032 | -49.934 | 2024-11-23 04:18:00 | NOAA-20 | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 4cb7e073-da2a-3ebb-aad9-52921bc7c51e | -3.96073 | -46.90423 | 2024-11-23 04:18:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 24c94562-df38-34fb-a8df-d17fb38e3487 | -3.82701 | -48.98276 | 2024-11-23 04:18:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| bab1a9ac-1528-3eaa-919e-98895a1e2675 | -3.55337 | -51.53819 | 2024-11-23 04:18:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| e08d218d-2346-3186-a93c-81f7e07e6df0 | -3.99884 | -47.91438 | 2024-11-23 04:18:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| bf3afee5-1ff1-30bb-80d3-66a187c3de0d | -3.79643 | -51.76492 | 2024-11-23 04:18:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| da0b4385-d5bf-337d-9887-72f267abc6d2 | -9.72899 | -37.03282 | 2024-11-23 04:18:00 | NOAA-20 | BATALHA | ALAGOAS | Brasil | 2700706 | 27 | 33 | nan | nan | nan | Caatinga | 6.2 |
| 2adf17e9-df31-3727-8e16-ee1eea148f95 | -3.35605 | -46.6548 | 2024-11-23 04:18:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 68de5e9e-f9b3-39e6-a06b-d0781bf3e8b5 | -7.18821 | -46.25234 | 2024-11-23 04:18:00 | NOAA-20 | NOVA COLINAS | MARANHÃO | Brasil | 2107258 | 21 | 33 | nan | nan | nan | Cerrado | 0.4 |
| ee1d1b18-d184-3631-af70-157f0c44cf47 | -3.94689 | -47.9685 | 2024-11-23 04:18:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 6.4 |
| 2eebad7d-19d6-33ce-a4ee-0ee58026c509 | -4.37211 | -48.50291 | 2024-11-23 04:18:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 176379e9-6c50-3ab1-932f-860bc82b4533 | -4.18836 | -49.42144 | 2024-11-23 04:18:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 4f442627-7d38-3851-8630-2d1feac2a4ae | -3.2496 | -50.12098 | 2024-11-23 04:18:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 2d63202f-934e-3f6c-9c3a-e309672c213d | -5.75927 | -46.25433 | 2024-11-23 04:18:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| f4a99c6a-e89e-318a-a6a1-67e739c5d1e5 | -3.20885 | -54.25143 | 2024-11-23 04:18:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 25f60b5b-9d17-3837-8524-8c7b2205fae6 | -4.27027 | -46.28863 | 2024-11-23 04:18:00 | NOAA-20 | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a097bb60-068f-367d-87bf-df028a14ef95 | -7.07435 | -40.00003 | 2024-11-23 04:18:00 | NOAA-20 | POTENGI | CEARÁ | Brasil | 2311207 | 23 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 84017a30-85d2-3223-92ed-76f975cb5cf1 | -5.12848 | -44.29197 | 2024-11-23 04:18:00 | NOAA-20 | GONÇALVES DIAS | MARANHÃO | Brasil | 2104404 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 77a361bf-b716-3496-b26e-8c21836c388b | -2.87824 | -51.58276 | 2024-11-23 04:18:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 6ba5df87-8726-3eba-8559-dafccb26dd61 | -3.41987 | -49.22734 | 2024-11-23 04:18:00 | NOAA-20 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| cd2a31ea-1199-3303-bad1-6ea1aa24fabc | -2.8163 | -54.03211 | 2024-11-23 04:18:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 46f7e7b7-ddf1-3e4d-9f12-f1a1e94c5dd2 | -6.15483 | -46.67362 | 2024-11-23 04:18:00 | NOAA-20 | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 18b8e0fe-0c46-370c-bc4a-684fe594e837 | -4.4187 | -44.11641 | 2024-11-23 04:18:00 | NOAA-20 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 7.8 |
| d844209e-481d-3639-8d60-cfd6791a5b52 | -4.26683 | -46.28808 | 2024-11-23 04:18:00 | NOAA-20 | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 7371a6f1-2822-3518-9729-f24c8b88559d | -5.11518 | -45.83254 | 2024-11-23 04:18:00 | NOAA-20 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 53f4f354-2537-3df2-835e-8e0fc12c7ee4 | -3.17909 | -54.32215 | 2024-11-23 04:18:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 82d96be2-017f-3252-b083-8b6f105bfb71 | -4.72362 | -45.49631 | 2024-11-23 04:18:00 | NOAA-20 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 03cd79e9-9182-3782-9766-8752f6ecc886 | -3.00631 | -51.55067 | 2024-11-23 04:18:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 2a2b94a3-4b8c-300f-a7dd-c3dc324cb2d6 | -4.25532 | -48.70172 | 2024-11-23 04:18:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 39.3 |
| 645099c7-3fc2-3daf-9482-23ddc96e5002 | -3.11456 | -53.11765 | 2024-11-23 04:18:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| e3a9c361-ef2a-3571-a2b1-b196c171d3cb | -3.67645 | -47.12598 | 2024-11-23 04:18:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 5cf1ae43-c099-38bb-a06b-7450e4dad73b | -5.33045 | -45.48653 | 2024-11-23 04:18:00 | NOAA-20 | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 6458a918-26df-3821-a890-1894699147f9 | -4.61151 | -46.50441 | 2024-11-23 04:18:00 | NOAA-20 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 18.7 |
| fc41b3ef-4860-397d-b2cc-dfd148003a73 | -5.32906 | -44.78604 | 2024-11-23 04:18:00 | NOAA-20 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| a101fefe-0c28-36c8-9213-f4fd53c58e7e | -5.0065 | -41.96016 | 2024-11-23 04:18:00 | NOAA-20 | JATOBÁ DO PIAUÍ | PIAUÍ | Brasil | 2205276 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 1dc4d059-1fe3-3b64-9c8b-bdf7fd18aa1e | -3.76126 | -49.93477 | 2024-11-23 04:18:00 | NOAA-20 | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 34e845ad-da75-3b0b-9a9c-3d2c045ec37d | -3.25392 | -53.27471 | 2024-11-23 04:18:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 72104709-845d-30ae-b47d-ac08ea5ec385 | -4.16687 | -46.8173 | 2024-11-23 04:18:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| aa6c0fb9-8a2e-3a78-8d63-04358238a0a9 | -6.06897 | -46.83924 | 2024-11-23 04:18:00 | NOAA-20 | LAJEADO NOVO | MARANHÃO | Brasil | 2105989 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| a78cef80-f07a-37b9-8e9e-b943a280cb64 | -4.60517 | -46.49962 | 2024-11-23 04:18:00 | NOAA-20 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 16.7 |
| f9f65747-48b5-3327-b19c-809b1bca25a3 | -4.60578 | -46.49584 | 2024-11-23 04:18:00 | NOAA-20 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 16.7 |
| a3d51fd0-5a1d-3549-b4f1-8647e65e3f02 | -4.25451 | -48.7067 | 2024-11-23 04:18:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 4a400c23-dad6-3c0a-819f-d84a164ac1a2 | -5.22217 | -43.73679 | 2024-11-23 04:18:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| fb6a5759-2b97-3388-9bc4-4dea64937871 | -3.67821 | -47.12487 | 2024-11-23 04:18:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| e0b5a84d-0b24-3526-b879-81895ec4af79 | -4.44396 | -46.34694 | 2024-11-23 04:18:00 | NOAA-20 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 14bc45de-62ea-3959-9514-a57cc969c9df | -4.44472 | -40.6067 | 2024-11-23 04:18:00 | NOAA-20 | IPU | CEARÁ | Brasil | 2305803 | 23 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 86db3416-0c2f-3a3f-a481-1abf8b873cd4 | -4.90023 | -47.4169 | 2024-11-23 04:18:00 | NOAA-20 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 2.6 |
| a401bea8-b5ef-3955-bcc6-a1c244070f0d | -3.9089 | -46.52983 | 2024-11-23 04:18:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 4a4d2775-5fe4-316f-b05c-0f93bf945e3b | -4.25842 | -48.70731 | 2024-11-23 04:18:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 60b3cf28-0eba-38d1-9f73-73ccacce2c18 | -4.6614 | -45.68012 | 2024-11-23 04:18:00 | NOAA-20 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 079d9af9-d297-33be-8786-a07666a9234c | -4.24981 | -48.711 | 2024-11-23 04:18:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 215af79b-4ef6-3bd9-8814-4fe5fdaf40de | -5.10781 | -43.16264 | 2024-11-23 04:18:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 8.6 |
| 464b5899-c75c-30a7-b0b5-e9c7cbcdf6b7 | -7.0713 | -49.20781 | 2024-11-23 04:18:00 | NOAA-20 | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 80ccb8b5-8db0-3880-b60e-0577b8f53092 | -6.39996 | -39.12576 | 2024-11-23 04:18:00 | NOAA-20 | ORÓS | CEARÁ | Brasil | 2309508 | 23 | 33 | nan | nan | nan | Caatinga | 3.8 |
| 7a25e1a7-ed8a-3ce3-9bbe-3004b73ade0f | -3.23537 | -54.23459 | 2024-11-23 04:18:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 71389a8a-8757-308b-b0c1-9fb84658343b | -3.99942 | -46.93531 | 2024-11-23 04:18:00 | NOAA-20 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 31f2a03c-f1cc-3a22-8119-61e0bb748416 | -4.60864 | -46.50013 | 2024-11-23 04:18:00 | NOAA-20 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 16.7 |
| 8a5682d8-1ae1-3d47-a179-007b500525c8 | -4.69825 | -43.65494 | 2024-11-23 04:18:00 | NOAA-20 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| c6c3b020-68fc-3071-a5fb-47df1825ef22 | -6.90729 | -47.52565 | 2024-11-23 04:18:00 | NOAA-20 | DARCINÓPOLIS | TOCANTINS | Brasil | 1706506 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| db8f3ca2-99d6-3f37-9270-3da8f30c07e6 | -3.96969 | -46.64334 | 2024-11-23 04:18:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 10.4 |
| 87d6c21a-7bb8-3e67-b212-4c90ce6b5253 | -4.0698 | -46.83517 | 2024-11-23 04:18:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| eee6fe74-26f7-3237-a21b-91194a1dbebb | -4.39805 | -49.77405 | 2024-11-23 04:18:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| e3a1b33d-7cc6-3b15-878b-204dfb98c1a7 | -2.95854 | -53.71995 | 2024-11-23 04:18:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 850719ac-5ad1-3b1d-9bce-e41e2e803a6d | -3.24705 | -54.24055 | 2024-11-23 04:18:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 1eed88ea-89b4-3ba1-9d7f-85fc2583dbef | -5.56308 | -46.2984 | 2024-11-23 04:18:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| b455208f-291b-3e85-b26c-8b010dde8531 | -6.24915 | -43.55219 | 2024-11-23 04:18:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| c7e9661d-ef5f-3de1-aa24-41210844c57a | -4.9117 | -47.85624 | 2024-11-23 04:18:00 | NOAA-20 | CIDELÂNDIA | MARANHÃO | Brasil | 2103257 | 21 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 83770517-ca78-3285-88d8-6c62c0236c0a | -3.00627 | -51.30973 | 2024-11-23 04:18:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| e51d7a41-c314-3ca0-8d7a-03b2d604c47f | -4.26082 | -48.69242 | 2024-11-23 04:18:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 6.8 |
| a10bff86-8337-3615-b677-5fefed2db013 | -3.11791 | -53.1147 | 2024-11-23 04:18:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |


[Clique aqui para ver as próximas entradas](README40.md)
