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
| fbc9bf94-5671-35aa-bfc0-2150c64f47ec | -9.34655 | -46.58865 | 2025-11-16 03:46:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 72da4fa2-70a0-330f-81c7-e28056e911c6 | -9.34995 | -46.6026 | 2025-11-16 03:46:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 8.1 |
| 1602d5c0-f44f-3837-b82d-f2865231d086 | -6.71236 | -42.13447 | 2025-11-16 03:46:00 | NPP-375D | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 9.9 |
| e728e8d6-9c4d-3002-8ff8-0c283391a526 | -9.84924 | -44.71291 | 2025-11-16 03:46:00 | NPP-375D | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 6ac1da9f-e559-3e3d-b0c0-d0ae014ee69d | -5.23902 | -44.34922 | 2025-11-16 03:46:00 | NPP-375D | GONÇALVES DIAS | MARANHÃO | Brasil | 2104404 | 21 | 33 | nan | nan | nan | Cerrado | 4.3 |
| ffcedd6f-9c43-3515-b540-bea6cb3cc187 | -6.30961 | -43.79535 | 2025-11-16 03:46:00 | NPP-375D | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 20.2 |
| 040b6d43-0345-30d6-9ec7-b5c0a0ed406e | -7.10803 | -42.7271 | 2025-11-16 03:46:00 | NPP-375D | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 4034c852-5941-33ec-a16e-b7df51e49b44 | -9.35079 | -46.59822 | 2025-11-16 03:46:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 1c5e3f21-3876-3cd8-b063-a849ce4a501b | -4.57359 | -45.81344 | 2025-11-16 03:46:00 | NPP-375D | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 2.3 |
| a12f37df-bda8-319e-ad93-59cbd4aad999 | -5.6067 | -41.06082 | 2025-11-16 03:46:00 | NPP-375D | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 78f93ba1-a5ba-3278-8a10-75a66eb721c5 | -4.57451 | -45.81035 | 2025-11-16 03:46:00 | NPP-375D | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| f39f4ba0-10b3-3821-9a27-e57f0d3f0c00 | -6.36742 | -39.62313 | 2025-11-16 03:46:00 | NPP-375D | JUCÁS | CEARÁ | Brasil | 2307403 | 23 | 33 | nan | nan | nan | Caatinga | 2.5 |
| c7d85d53-8441-3c5a-89ac-dfe3217278f8 | -7.22557 | -47.98663 | 2025-11-16 03:46:00 | NPP-375D | BABAÇULÂNDIA | TOCANTINS | Brasil | 1703008 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 5e6d64a0-b64d-3594-ae25-10f0e74ad7a4 | -6.084 | -41.61521 | 2025-11-16 03:46:00 | NPP-375D | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 8b7615ce-6b6a-32ab-8a67-0ccfc17921dc | -3.92775 | -47.05174 | 2025-11-16 03:46:00 | NPP-375D | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 3d98c653-5a58-3946-8c4f-5c15ce82fa6a | -8.57687 | -46.05889 | 2025-11-16 03:46:00 | NPP-375D | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 97b4d9f6-7827-32c6-8312-87bd00bb12bd | -4.02579 | -42.07854 | 2025-11-16 03:46:00 | NPP-375D | BATALHA | PIAUÍ | Brasil | 2201507 | 22 | 33 | nan | nan | nan | Caatinga | 2.8 |
| 99ba820a-3923-3776-81bb-641347cdde69 | -6.689 | -39.09731 | 2025-11-16 03:46:00 | NPP-375D | CEDRO | CEARÁ | Brasil | 2303808 | 23 | 33 | nan | nan | nan | Caatinga | 6.0 |
| d9249f44-2cda-3d78-9baa-6541d5cc881b | -7.19275 | -39.20525 | 2025-11-16 03:46:00 | NPP-375D | MISSÃO VELHA | CEARÁ | Brasil | 2308401 | 23 | 33 | nan | nan | nan | Caatinga | 2.6 |
| d1eeca12-c9b4-3882-8094-cbd7c4cd230f | -3.82152 | -46.02483 | 2025-11-16 03:46:00 | NPP-375D | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| cbdcc46e-c93a-3fcc-aa64-c1b21cfa3c81 | -5.51947 | -40.99181 | 2025-11-16 03:46:00 | NPP-375D | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 16156695-8584-3de1-b3f0-9b0bd4e33456 | -10.18011 | -44.50176 | 2025-11-16 03:46:00 | NPP-375D | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 2.7 |
| ac878015-9942-35fa-9201-f2d227f06234 | -6.30049 | -43.79469 | 2025-11-16 03:46:00 | NPP-375D | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| e591fb20-0a0a-38f3-9012-5f3c40064384 | -5.52682 | -40.8966 | 2025-11-16 03:46:00 | NPP-375D | NOVO ORIENTE | CEARÁ | Brasil | 2309409 | 23 | 33 | nan | nan | nan | Caatinga | 1.1 |
| c4e048ee-3d3a-316a-83a1-f32f61ab833e | -6.30682 | -43.78905 | 2025-11-16 03:46:00 | NPP-375D | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 12.4 |
| 8caf2080-43d0-336d-b8de-2293b723d154 | -5.51869 | -40.97031 | 2025-11-16 03:46:00 | NPP-375D | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 855efccf-3353-354d-91d3-d4b9a9d402a3 | -9.11235 | -40.46143 | 2025-11-16 03:46:00 | NPP-375D | PETROLINA | PERNAMBUCO | Brasil | 2611101 | 26 | 33 | nan | nan | nan | Caatinga | 6.6 |
| 50e34370-c3dc-3500-8553-1449c700cf67 | -7.3571 | -43.33886 | 2025-11-16 03:46:00 | NPP-375D | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 55b4c6db-e2aa-33b5-ab40-0bd699e9b879 | -6.44976 | -47.28141 | 2025-11-16 03:46:00 | NPP-375D | PORTO FRANCO | MARANHÃO | Brasil | 2109007 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 413c2b97-68f5-3e88-9763-3f56a144859e | -3.59645 | -41.65941 | 2025-11-16 03:46:00 | NPP-375D | COCAL | PIAUÍ | Brasil | 2202703 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 4a6edb16-b81e-30da-be1c-25158f45b236 | -5.34174 | -43.04213 | 2025-11-16 03:46:00 | NPP-375D | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 11.5 |
| 293a76e2-47c8-386e-83ea-fa5ece8e45db | -6.3108 | -43.7965 | 2025-11-16 03:46:00 | NPP-375D | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 21.7 |
| 3071bd7a-8122-361f-b932-09228ab28c6b | -6.53689 | -39.40306 | 2025-11-16 03:46:00 | NPP-375D | CARIÚS | CEARÁ | Brasil | 2303303 | 23 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 0721dfaf-f5da-3ff2-9e84-ab3734d56ce5 | -6.86058 | -38.61064 | 2025-11-16 03:46:00 | NPP-375D | CAJAZEIRAS | PARAÍBA | Brasil | 2503704 | 25 | 33 | nan | nan | nan | Caatinga | 1.0 |
| d3bae0c0-d52a-34c0-b481-0b36c94303e8 | -6.41627 | -42.3344 | 2025-11-16 03:46:00 | NPP-375D | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 8ec4b343-05fb-314b-ac3c-001622d9afbb | -8.20434 | -43.56625 | 2025-11-16 03:46:00 | NPP-375D | COLÔNIA DO GURGUÉIA | PIAUÍ | Brasil | 2202752 | 22 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 8aed1846-29e9-38e4-87f7-fe09848a5d20 | -4.7691 | -38.71414 | 2025-11-16 03:46:00 | NPP-375D | IBARETAMA | CEARÁ | Brasil | 2305266 | 23 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 51546604-106c-3d34-9aec-7b5bd2b7003e | -4.04547 | -40.87674 | 2025-11-16 03:46:00 | NPP-375D | SÃO BENEDITO | CEARÁ | Brasil | 2312304 | 23 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 6563843e-a7db-3439-88b0-7ff95e3b4163 | -5.99156 | -41.90955 | 2025-11-16 03:46:00 | NPP-375D | SANTA CRUZ DOS MILAGRES | PIAUÍ | Brasil | 2209153 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 72fc19ae-8ebf-3802-af89-333d3c3643c8 | -8.09284 | -43.01176 | 2025-11-16 03:46:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 10621d25-0dfd-34cc-86ef-86b7f3130ed7 | -10.00906 | -44.78279 | 2025-11-16 03:46:00 | NPP-375D | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 034bea16-d4a9-3477-bc3b-b25badb3d235 | -5.92638 | -42.25602 | 2025-11-16 03:46:00 | NPP-375D | SÃO MIGUEL DA BAIXA GRANDE | PIAUÍ | Brasil | 2210383 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 83fb6237-81fa-3f53-9e51-11b0e6e26550 | -5.28681 | -44.30072 | 2025-11-16 03:46:00 | NPP-375D | GONÇALVES DIAS | MARANHÃO | Brasil | 2104404 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 71b615a6-4bfd-3c41-bfb2-6569260a6aef | -9.94943 | -44.92726 | 2025-11-16 03:46:00 | NPP-375D | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 21e5d64b-ed72-32cc-acb3-70d6e57f29e5 | -6.67658 | -42.04487 | 2025-11-16 03:46:00 | NPP-375D | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 8.6 |
| ffde82ba-d943-3a77-b58b-d170b89f3f36 | -4.26592 | -38.08432 | 2025-11-16 03:46:00 | NPP-375D | BEBERIBE | CEARÁ | Brasil | 2302206 | 23 | 33 | nan | nan | nan | Caatinga | 3.3 |
| f886bc70-70e3-340e-9f54-33303f1b7025 | -5.63053 | -43.93161 | 2025-11-16 03:46:00 | NPP-375D | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 6d2d2898-952d-324a-b727-3d3ec79fcdc3 | -9.33064 | -46.57649 | 2025-11-16 03:46:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 6b2be078-fab8-3348-8ac2-0c33a1b5c19a | -3.66675 | -44.81977 | 2025-11-16 03:46:00 | NPP-375D | VITÓRIA DO MEARIM | MARANHÃO | Brasil | 2112902 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 22894a2b-bf37-3882-842a-74030b5a01d9 | -7.09688 | -42.73517 | 2025-11-16 03:46:00 | NPP-375D | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 09114fc1-299f-3961-b06f-4c5c43388e4c | -8.30569 | -43.80341 | 2025-11-16 03:46:00 | NPP-375D | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 5dae2b5a-30d0-30c3-819d-5730f21358bd | -7.01898 | -45.16542 | 2025-11-16 03:46:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| f7e398d8-dd50-3b77-8a00-a38623f48bd1 | -5.71494 | -41.40667 | 2025-11-16 03:46:00 | NPP-375D | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 2d504bb4-aab0-3280-ac07-3a433e85234c | -5.00518 | -41.96768 | 2025-11-16 03:46:00 | NPP-375D | JATOBÁ DO PIAUÍ | PIAUÍ | Brasil | 2205276 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 2f1ddeef-602c-319a-b627-be15b2a62206 | -10.16486 | -44.512 | 2025-11-16 03:46:00 | NPP-375D | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 8c262818-4581-3749-a4c3-35e1d864e44f | -5.42586 | -44.63389 | 2025-11-16 03:46:00 | NPP-375D | SANTA FILOMENA DO MARANHÃO | MARANHÃO | Brasil | 2109759 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| ac5d7a42-49ca-3493-b0de-2ba65319abea | -7.18388 | -39.44106 | 2025-11-16 03:46:00 | NPP-375D | CRATO | CEARÁ | Brasil | 2304202 | 23 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 195efc81-bb50-307d-b8d4-5e92ba9e8c4a | -4.42627 | -43.40616 | 2025-11-16 03:46:00 | NPP-375D | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| be873505-dfd8-32c5-bb50-f8ef0878d137 | -7.2123 | -47.98428 | 2025-11-16 03:46:00 | NPP-375D | BABAÇULÂNDIA | TOCANTINS | Brasil | 1703008 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| dba37ca8-8e5c-3e13-8b2e-29afe5f284e4 | -10.0047 | -44.77158 | 2025-11-16 03:46:00 | NPP-375D | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 3.3 |
| f2b5815d-6dba-302d-80e2-ce39a02cb8a8 | -4.65493 | -46.74212 | 2025-11-16 03:46:00 | NPP-375D | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 3.8 |
| da39a5eb-b5fb-34dd-9b5a-ce5cde452551 | -7.10246 | -42.7311 | 2025-11-16 03:46:00 | NPP-375D | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| a777fb32-2ead-3011-97d3-1871472f5975 | -9.74748 | -43.95413 | 2025-11-16 03:46:00 | NPP-375D | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| faf53de3-03bc-375e-b941-17410b23e425 | -6.20945 | -44.64448 | 2025-11-16 03:46:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 6cb7799c-5512-3f78-b74e-f2c686412f0c | -6.43371 | -42.06627 | 2025-11-16 03:46:00 | NPP-375D | NOVO ORIENTE DO PIAUÍ | PIAUÍ | Brasil | 2206902 | 22 | 33 | nan | nan | nan | Caatinga | 3.6 |
| 6ad9e848-f848-3276-904d-edd76e57a8cf | -10.14456 | -42.13335 | 2025-11-16 03:46:00 | NPP-375D | SENTO SÉ | BAHIA | Brasil | 2930204 | 29 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 137df827-e115-355a-839f-f175b4f77f0f | -6.82119 | -39.81051 | 2025-11-16 03:46:00 | NPP-375D | ASSARÉ | CEARÁ | Brasil | 2301604 | 23 | 33 | nan | nan | nan | Caatinga | 0.9 |
| e29c8b4a-f63c-3df1-9851-e258c834aa77 | -7.71694 | -47.29211 | 2025-11-16 03:46:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 3a112f0d-fcfa-3b87-a51b-0e4ece29b32d | -5.23839 | -44.35279 | 2025-11-16 03:46:00 | NPP-375D | GONÇALVES DIAS | MARANHÃO | Brasil | 2104404 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 15ba5b4a-2524-3fb0-820f-8ece605568c1 | -9.73455 | -43.96156 | 2025-11-16 03:46:00 | NPP-375D | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 4.5 |
| a4890457-aae9-3f4e-9eae-1e483e831d27 | -5.52744 | -40.89298 | 2025-11-16 03:46:00 | NPP-375D | NOVO ORIENTE | CEARÁ | Brasil | 2309409 | 23 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 7fd40a72-452b-3e83-a199-4871180e6085 | -5.48551 | -44.83866 | 2025-11-16 03:46:00 | NPP-375D | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 5948337a-beaa-3a1b-a0be-269f3bce1535 | -9.83943 | -44.1789 | 2025-11-16 03:46:00 | NPP-375D | CURIMATÁ | PIAUÍ | Brasil | 2203206 | 22 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 51ae6803-6d91-3f4d-8cec-a163c0b62d8d | -3.78935 | -44.17751 | 2025-11-16 03:46:00 | NPP-375D | PIRAPEMAS | MARANHÃO | Brasil | 2108801 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| b3e58a5f-b914-3712-9064-edd6da9a66a7 | -10.16335 | -44.5074 | 2025-11-16 03:46:00 | NPP-375D | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| d72f174e-3657-3842-9047-6d3a3c0654bc | -9.34388 | -46.58385 | 2025-11-16 03:46:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 059263df-4333-314f-9151-1984336ceac4 | -9.7424 | -43.98172 | 2025-11-16 03:46:00 | NPP-375D | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 6143e7db-d9b0-3dc1-b9ec-a6214d9c9b9c | -2.51619 | -47.8161 | 2025-11-16 03:46:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 15.1 |
| e36ea3e2-a90b-3b62-a95b-34769991b337 | -8.06707 | -43.10112 | 2025-11-16 03:46:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 4a2c70f9-5f9f-367a-a570-8ca965fddd0f | -9.33298 | -46.57708 | 2025-11-16 03:46:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| a449e7e3-cc46-3a06-ae55-4eb44f27991e | -6.95073 | -38.7206 | 2025-11-16 03:46:00 | NPP-375D | CACHOEIRA DOS ÍNDIOS | PARAÍBA | Brasil | 2503308 | 25 | 33 | nan | nan | nan | Caatinga | 2.0 |
| def3be3d-8286-330f-ba3d-500690e8734c | -6.56032 | -39.76632 | 2025-11-16 03:46:00 | NPP-375D | SABOEIRO | CEARÁ | Brasil | 2311900 | 23 | 33 | nan | nan | nan | Caatinga | 2.4 |
| b3ca7aaa-096e-3466-af76-83bd2816341d | -4.68243 | -46.73588 | 2025-11-16 03:46:00 | NPP-375D | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 86d3a283-3e80-3682-8820-ef8554f9a063 | -5.69419 | -45.98951 | 2025-11-16 03:46:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| aca26713-bbbc-380a-97e5-48b9ed8ad228 | -7.71497 | -47.30246 | 2025-11-16 03:46:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 4.2 |
| d06bc92b-da07-3323-bdb1-463525d91353 | -6.07299 | -41.5457 | 2025-11-16 03:46:00 | NPP-375D | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| bfd2b8e9-6660-3dbb-a3ef-4123a1f60705 | -6.85694 | -42.84675 | 2025-11-16 03:46:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 13.1 |
| c30d4c1c-9782-3b99-9e6d-d7b459d2fcc5 | -4.07302 | -46.34186 | 2025-11-16 03:46:00 | NPP-375D | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 8db43585-7e22-3a7a-a3d4-9d4cbdd6c109 | -3.85706 | -39.82705 | 2025-11-16 03:46:00 | NPP-375D | IRAUÇUBA | CEARÁ | Brasil | 2306108 | 23 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 733007e4-1465-3f55-857d-342c2e6c5e8c | -6.08622 | -41.60213 | 2025-11-16 03:46:00 | NPP-375D | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 3.4 |
| 94c2324b-b051-3820-a68f-b6d61dffc14c | -8.0623 | -43.10025 | 2025-11-16 03:46:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 26.2 |
| f09e5c1c-e3ce-31d3-9045-51ca132f9cc7 | -3.5918 | -41.6586 | 2025-11-16 03:46:00 | NPP-375D | COCAL | PIAUÍ | Brasil | 2202703 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 3edc6d61-0b82-3aaf-98ac-d3b42b209bd2 | -3.85234 | -40.76746 | 2025-11-16 03:46:00 | NPP-375D | COREAÚ | CEARÁ | Brasil | 2304004 | 23 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 7b8e617f-7c74-36c6-90a1-5c186a5292ae | -6.06853 | -41.54505 | 2025-11-16 03:46:00 | NPP-375D | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| d40685a4-7b1f-3c2f-aa4f-ea342b29cb87 | -5.66013 | -41.08735 | 2025-11-16 03:46:00 | NPP-375D | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 88f3bf83-7800-3119-a9ea-1423d4736421 | -7.38797 | -45.5162 | 2025-11-16 03:46:00 | NPP-375D | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 2d4c9377-acfc-38bf-a71a-49888aa4d858 | -7.26658 | -48.02443 | 2025-11-16 03:46:00 | NPP-375D | BABAÇULÂNDIA | TOCANTINS | Brasil | 1703008 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| f0edd91f-ece8-3f15-b493-d972c9fb5a4f | -7.35973 | -46.58506 | 2025-11-16 03:46:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 8cc9f716-3103-3df9-8f53-791968d2eb67 | -9.67613 | -37.09575 | 2025-11-16 03:46:00 | NPP-375D | BATALHA | ALAGOAS | Brasil | 2700706 | 27 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 4bc8ec00-40f4-320b-9b9e-c9a9dad5614e | -9.34469 | -46.57949 | 2025-11-16 03:46:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |


[Clique aqui para ver as próximas entradas](README18.md)
