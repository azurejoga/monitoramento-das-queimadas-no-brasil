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

## Dados Diários - Página 28

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 0fd76162-a2cf-3f81-9d38-6e58164261b9 | -3.57445 | -44.0893 | 2025-11-16 04:06:00 | NOAA-20 | CANTANHEDE | MARANHÃO | Brasil | 2102705 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 06396451-f899-38eb-85e3-a81c123634da | -5.33254 | -43.04118 | 2025-11-16 04:06:00 | NOAA-20 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 8d3a7f5c-c22e-3830-b898-a4e382933b98 | -3.85295 | -40.77037 | 2025-11-16 04:06:00 | NOAA-20 | COREAÚ | CEARÁ | Brasil | 2304004 | 23 | 33 | nan | nan | nan | Caatinga | 2.8 |
| 427b7a0a-659a-3e07-9031-61996acf5ec5 | -5.51307 | -40.97214 | 2025-11-16 04:06:00 | NOAA-20 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 5566e320-3f77-3eff-b2dd-8ed8c3f8dc65 | -5.32634 | -43.03643 | 2025-11-16 04:06:00 | NOAA-20 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| d879aa88-bddf-3e96-8f18-9d660a10f317 | -5.52421 | -41.78292 | 2025-11-16 04:06:00 | NOAA-20 | SÃO JOÃO DA SERRA | PIAUÍ | Brasil | 2209906 | 22 | 33 | nan | nan | nan | Caatinga | 0.5 |
| baa0e3e8-6e6c-32b5-951d-e54c39c0b32b | -5.43178 | -42.57617 | 2025-11-16 04:06:00 | NOAA-20 | LAGOA DO PIAUÍ | PIAUÍ | Brasil | 2205581 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 11055d31-cf0a-39e2-bc99-88037700d6e3 | -3.99316 | -44.28005 | 2025-11-16 04:06:00 | NOAA-20 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 8d514e58-f965-321c-99ab-45d7497c9de2 | -3.57378 | -44.09346 | 2025-11-16 04:06:00 | NOAA-20 | CANTANHEDE | MARANHÃO | Brasil | 2102705 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 31cc09e0-2ecc-3f81-82df-24e795f0fa3d | -5.51973 | -40.99438 | 2025-11-16 04:06:00 | NOAA-20 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 4.4 |
| 09bc75ac-13ad-358f-9dcb-294388e7ed2d | -4.19636 | -43.10278 | 2025-11-16 04:06:00 | NOAA-20 | COELHO NETO | MARANHÃO | Brasil | 2103406 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 1147046a-cca0-3a81-87e9-a25515fba852 | -3.46824 | -48.97617 | 2025-11-16 04:06:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| ca6a04c6-c944-37cc-8578-61d5ee70cb0e | -4.10034 | -43.34752 | 2025-11-16 04:06:00 | NOAA-20 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| e17e46c8-e0bc-3296-95b5-072ba537ee21 | -1.99197 | -46.54885 | 2025-11-16 04:06:00 | NOAA-20 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f1e92903-ec25-32a9-87d5-8c764f9d60db | -3.45498 | -51.02442 | 2025-11-16 04:06:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 95f4c656-8595-3379-b933-a5943a535d61 | -4.15974 | -42.13855 | 2025-11-16 04:06:00 | NOAA-20 | BATALHA | PIAUÍ | Brasil | 2201507 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 5a501f49-3cdf-31ed-99fb-8a25d0ddee6c | -4.2031 | -48.56591 | 2025-11-16 04:06:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| dca3ea9a-e174-398c-b418-7cbae064f82f | -3.67999 | -44.17826 | 2025-11-16 04:06:00 | NOAA-20 | CANTANHEDE | MARANHÃO | Brasil | 2102705 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 9e82c0cb-476e-38ed-9f3c-c4d776057da2 | -5.58953 | -41.06897 | 2025-11-16 04:06:00 | NOAA-20 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| c6325860-1278-32d9-b031-a9fb445c9206 | -4.42258 | -43.41672 | 2025-11-16 04:06:00 | NOAA-20 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| ceec2e9e-f594-3456-bce3-f796cc25ccff | -4.23124 | -46.10754 | 2025-11-16 04:06:00 | NOAA-20 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e343240f-d5e9-37e1-88d7-abe1d6597826 | -3.10344 | -45.78236 | 2025-11-16 04:06:00 | NOAA-20 | ARAGUANÃ | MARANHÃO | Brasil | 2100873 | 21 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 4ea25ea4-6e37-333b-861a-6d204a0004f7 | -2.81705 | -48.46075 | 2025-11-16 04:06:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 4456395e-1839-332f-a9c4-a3757eaafa27 | -4.81162 | -45.505 | 2025-11-16 04:06:00 | NOAA-20 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 4d031e40-0b8f-3874-848b-0634b92deb21 | -2.88939 | -53.28542 | 2025-11-16 04:06:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 10.6 |
| 3e3af3d5-20e7-3917-a195-89d1144cb350 | -4.01924 | -48.81519 | 2025-11-16 04:06:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 1452af28-e5fa-3d23-8a05-2612b337b0a6 | -3.41831 | -46.15265 | 2025-11-16 04:06:00 | NOAA-20 | GOVERNADOR NEWTON BELLO | MARANHÃO | Brasil | 2104651 | 21 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 0f72d400-8e88-3b15-b734-22fa8e1f1c46 | -4.81161 | -41.60597 | 2025-11-16 04:06:00 | NOAA-20 | JUAZEIRO DO PIAUÍ | PIAUÍ | Brasil | 2205516 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| b14ae7c8-9031-3d27-b5f8-474144d3a9ed | -4.00701 | -42.88265 | 2025-11-16 04:06:00 | NOAA-20 | BURITI | MARANHÃO | Brasil | 2102200 | 21 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 11e2e84c-1b10-36ee-9131-7ffb0e526164 | -5.60768 | -41.06121 | 2025-11-16 04:06:00 | NOAA-20 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| bf9f7285-4c60-382e-91a9-c3a7f6b61878 | -3.98638 | -41.88128 | 2025-11-16 04:06:00 | NOAA-20 | BATALHA | PIAUÍ | Brasil | 2201507 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| b9afcdb5-c7b6-395e-8c72-6a5e1f195fbb | -3.99611 | -44.28489 | 2025-11-16 04:06:00 | NOAA-20 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| b0115b48-e3d2-3528-938e-2c946c6bea5b | -4.42667 | -43.41343 | 2025-11-16 04:06:00 | NOAA-20 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 10.0 |
| e4f9dd6a-97b3-336a-b349-1d9a6072291f | -3.84088 | -40.78257 | 2025-11-16 04:06:00 | NOAA-20 | COREAÚ | CEARÁ | Brasil | 2304004 | 23 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 88e2a0c0-fd57-3536-8809-915c6d348690 | -3.95674 | -44.84547 | 2025-11-16 04:06:00 | NOAA-20 | LAGO VERDE | MARANHÃO | Brasil | 2105906 | 21 | 33 | nan | nan | nan | Amazônia | 4.7 |
| e10a1539-5628-3dc7-9c6c-41b89f29a161 | -4.00925 | -42.89057 | 2025-11-16 04:06:00 | NOAA-20 | BURITI | MARANHÃO | Brasil | 2102200 | 21 | 33 | nan | nan | nan | Caatinga | 2.1 |
| e29b16e7-c54f-3aea-961d-0a188625ee18 | -5.41649 | -43.25829 | 2025-11-16 04:06:00 | NOAA-20 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 6.5 |
| c5d45590-901b-33d3-8396-dbea3baabc0d | -5.32601 | -35.93436 | 2025-11-16 04:06:00 | NOAA-20 | JOÃO CÂMARA | RIO GRANDE DO NORTE | Brasil | 2405801 | 24 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 6ecaf5ef-194a-3d04-ba5f-565301608abf | -2.68657 | -49.07946 | 2025-11-16 04:06:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 3845631a-0bb4-332a-9dfa-0cd358ed0d5b | -4.41681 | -45.56336 | 2025-11-16 04:06:00 | NOAA-20 | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b9fc5095-a486-3cfe-92a9-6ce668eaf3bc | -4.02696 | -42.07487 | 2025-11-16 04:06:00 | NOAA-20 | BATALHA | PIAUÍ | Brasil | 2201507 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| e63299e8-075f-315d-944b-3921560bb42f | -2.4829 | -44.19139 | 2025-11-16 04:06:00 | NOAA-20 | SÃO JOSÉ DE RIBAMAR | MARANHÃO | Brasil | 2111201 | 21 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 64400862-7c2b-3bfc-a02e-951b68e8b128 | -4.01438 | -48.81429 | 2025-11-16 04:06:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 1ef3ad35-6cf7-3faa-a080-0feade499b2e | -4.46555 | -46.30745 | 2025-11-16 04:06:00 | NOAA-20 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 35592ded-a6df-34b4-af24-4a6e7ca15082 | -2.46465 | -48.8653 | 2025-11-16 04:06:00 | NOAA-20 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 8ad1a1e1-b85b-3fcd-a738-052ad497f064 | -4.00984 | -42.88688 | 2025-11-16 04:06:00 | NOAA-20 | BURITI | MARANHÃO | Brasil | 2102200 | 21 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 06c69317-cfc8-3cdd-b67e-c0256b1dae3a | -4.2301 | -44.64391 | 2025-11-16 04:06:00 | NOAA-20 | BACABAL | MARANHÃO | Brasil | 2101202 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 576e7755-25fd-3887-9560-29b71ee7e95f | -3.09941 | -45.78173 | 2025-11-16 04:06:00 | NOAA-20 | ARAGUANÃ | MARANHÃO | Brasil | 2100873 | 21 | 33 | nan | nan | nan | Amazônia | 0.6 |
| b4e1aefb-2d14-36ca-a78a-1ad750b34ecc | -5.48447 | -40.98182 | 2025-11-16 04:06:00 | NOAA-20 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| a8819e5d-118d-3907-bd8e-001a8008cae1 | -2.9655 | -53.22273 | 2025-11-16 04:06:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 0a3162be-2974-3660-a111-46e4b985101e | -4.96186 | -44.04532 | 2025-11-16 04:06:00 | NOAA-20 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 4766f6a4-c3c7-3c4a-8710-b182b3c98150 | -4.40932 | -43.41065 | 2025-11-16 04:06:00 | NOAA-20 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 8189b36e-ed8c-3058-aad9-59ded359dd1d | -4.53026 | -43.23151 | 2025-11-16 04:06:00 | NOAA-20 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 1b6c34f0-f94c-3fc5-be89-bfb880061a47 | -5.51692 | -40.96921 | 2025-11-16 04:06:00 | NOAA-20 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 3976440c-b621-3b49-a47d-293669da950c | -4.05549 | -50.73148 | 2025-11-16 04:06:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ee8f2325-4344-3c05-a5b3-6b6d5810abeb | -2.82936 | -48.43678 | 2025-11-16 04:06:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e7bb6ab6-d9e8-3412-9cf8-0c78c4c5d76a | -3.45427 | -51.02846 | 2025-11-16 04:06:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 8746e411-9826-3310-a762-3c5d2a0b2fc9 | -4.1672 | -46.84159 | 2025-11-16 04:06:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e81777d0-8723-3af6-a942-d3208cae9bb7 | -2.51084 | -47.81208 | 2025-11-16 04:06:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 2f1a586f-815a-37ad-9372-a11233e9ec22 | -4.04109 | -46.34746 | 2025-11-16 04:06:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 9a7081b0-4ef4-3390-a795-eb4efacf3120 | -3.53834 | -40.65431 | 2025-11-16 04:06:00 | NOAA-20 | COREAÚ | CEARÁ | Brasil | 2304004 | 23 | 33 | nan | nan | nan | Caatinga | 1.6 |
| a216bc4d-175e-3d27-9557-008920c94cda | -5.05732 | -45.04079 | 2025-11-16 04:06:00 | NOAA-20 | SÃO RAIMUNDO DO DOCA BEZERRA | MARANHÃO | Brasil | 2111631 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| bbfba420-8ab5-3acf-a4b7-d8e553689c96 | -3.66227 | -44.81737 | 2025-11-16 04:06:00 | NOAA-20 | VITÓRIA DO MEARIM | MARANHÃO | Brasil | 2112902 | 21 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 0a2d9310-2db0-3d23-93de-532402ffbe5e | -5.47601 | -41.40051 | 2025-11-16 04:06:00 | NOAA-20 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 3.1 |
| c11f51d6-02b7-32ea-b61d-1c67ff7723e8 | -2.37324 | -44.85165 | 2025-11-16 04:06:00 | NOAA-20 | BEQUIMÃO | MARANHÃO | Brasil | 2101905 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 40c6bf54-ce49-3196-8c05-2f0a4de3adae | -4.46612 | -46.30392 | 2025-11-16 04:06:00 | NOAA-20 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| b0a75630-c495-3724-b2e8-0e66ace5504f | -3.59019 | -43.14043 | 2025-11-16 04:06:00 | NOAA-20 | MATA ROMA | MARANHÃO | Brasil | 2106409 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 0e9957d0-5ea7-3f13-beac-9b23cf854d16 | -5.23016 | -44.3526 | 2025-11-16 04:06:00 | NOAA-20 | GONÇALVES DIAS | MARANHÃO | Brasil | 2104404 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| a6b066bb-58ec-3c56-991a-2045813b02fd | -4.65529 | -46.74628 | 2025-11-16 04:06:00 | NOAA-20 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 7f7dbf08-a87b-3a59-9f08-068a411c0c82 | -3.49186 | -54.05264 | 2025-11-16 04:06:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 7c52294c-7392-3164-a347-5d6c051aa65c | -2.91493 | -45.23384 | 2025-11-16 04:06:00 | NOAA-20 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 6a9b4ed8-0815-3179-966a-f26590da6eb0 | -4.43138 | -43.40633 | 2025-11-16 04:06:00 | NOAA-20 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 6535f5bd-a3db-3b0a-acda-0eebbdc474ca | -5.23801 | -44.34967 | 2025-11-16 04:06:00 | NOAA-20 | GONÇALVES DIAS | MARANHÃO | Brasil | 2104404 | 21 | 33 | nan | nan | nan | Cerrado | 7.3 |
| 76e4f7f8-42ee-3658-b624-cf5d1548242a | -4.09339 | -40.51538 | 2025-11-16 04:06:00 | NOAA-20 | RERIUTABA | CEARÁ | Brasil | 2311702 | 23 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 18ae0f61-c304-3606-9c8e-3f7e1dba584e | -4.74512 | -46.38206 | 2025-11-16 04:06:00 | NOAA-20 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b3dd6496-4001-3042-8233-3083a3f58a66 | -4.7352 | -46.39148 | 2025-11-16 04:06:00 | NOAA-20 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 284ca19f-d49a-378b-abd4-be2e4c1aad21 | -2.75297 | -49.52945 | 2025-11-16 04:06:00 | NOAA-20 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d52eff68-fe4f-37da-836c-0d7f16f7d56c | -4.46536 | -46.30616 | 2025-11-16 04:06:00 | NOAA-20 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 6c8742b5-48df-3204-a337-73e0833d0e4f | -3.95974 | -44.85059 | 2025-11-16 04:06:00 | NOAA-20 | LAGO VERDE | MARANHÃO | Brasil | 2105906 | 21 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 382497aa-f9db-3d6f-ac5e-438c6433193b | -5.52833 | -40.89669 | 2025-11-16 04:06:00 | NOAA-20 | NOVO ORIENTE | CEARÁ | Brasil | 2309409 | 23 | 33 | nan | nan | nan | Caatinga | 1.1 |
| a3c4da02-aa73-32c3-af00-107b0483745e | -5.32188 | -35.93382 | 2025-11-16 04:06:00 | NOAA-20 | PARAZINHO | RIO GRANDE DO NORTE | Brasil | 2408805 | 24 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 112f144c-1f43-3950-a22b-371cdaa8ed88 | -4.46147 | -46.30685 | 2025-11-16 04:06:00 | NOAA-20 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 491f188a-5c2f-3656-bbc3-1b5d481f5ffb | -4.74046 | -46.38493 | 2025-11-16 04:06:00 | NOAA-20 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 5.1 |
| afc552c1-479a-3408-a21c-bd70a5cd37b1 | -4.80779 | -45.43086 | 2025-11-16 04:06:00 | NOAA-20 | LAGOA GRANDE DO MARANHÃO | MARANHÃO | Brasil | 2105963 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 5ecc366e-e448-367f-9300-7c13b3b42f11 | -4.59951 | -41.78554 | 2025-11-16 04:06:00 | NOAA-20 | CAPITÃO DE CAMPOS | PIAUÍ | Brasil | 2202406 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 755fce71-e1ea-344d-9338-621f4626b5d8 | -4.15335 | -50.23154 | 2025-11-16 04:06:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 214875aa-29c9-3a85-ba4a-525f65e94655 | -2.42675 | -45.71285 | 2025-11-16 04:06:00 | NOAA-20 | SANTA LUZIA DO PARUÁ | MARANHÃO | Brasil | 2110039 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| f8fd2639-a90f-330c-8563-fa5862073213 | -4.6141 | -43.29845 | 2025-11-16 04:06:00 | NOAA-20 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 5.0 |
| bfd38f0a-aa74-32ff-bc79-204c6f731936 | -3.53808 | -44.84229 | 2025-11-16 04:06:00 | NOAA-20 | VITÓRIA DO MEARIM | MARANHÃO | Brasil | 2112902 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 86420fcf-6feb-3cde-a40a-3657b793af24 | -3.13262 | -41.88326 | 2025-11-16 04:06:00 | NOAA-20 | BURITI DOS LOPES | PIAUÍ | Brasil | 2202000 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 1e4e4a86-4719-3b9b-95c9-d17d1767df40 | -2.14391 | -45.35146 | 2025-11-16 04:06:00 | NOAA-20 | TURILÂNDIA | MARANHÃO | Brasil | 2112456 | 21 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 06ff307c-ae9a-39b3-9c85-99aac9d8485c | -2.95157 | -48.59189 | 2025-11-16 04:06:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 44b9fed6-226b-377c-aba4-0d4338750c56 | -4.61065 | -43.2979 | 2025-11-16 04:06:00 | NOAA-20 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 70c4835e-78c4-3905-981b-78301a063a9b | -4.42505 | -43.51172 | 2025-11-16 04:06:00 | NOAA-20 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 03f24003-9367-3af2-a80d-67a00554db5e | -3.6882 | -45.14005 | 2025-11-16 04:06:00 | NOAA-20 | IGARAPÉ DO MEIO | MARANHÃO | Brasil | 2105153 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 93555232-87b6-3cc9-9ece-c826db73192c | -5.42333 | -43.25941 | 2025-11-16 04:06:00 | NOAA-20 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 3604d80c-259e-3213-9196-99150062a4f9 | -3.08285 | -52.92351 | 2025-11-16 04:06:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 47a6ba26-d8f2-34de-977a-f89970393122 | -3.49292 | -54.04663 | 2025-11-16 04:06:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 5634aade-5389-3fda-aa3d-1b14766f52f3 | -2.90806 | -49.79292 | 2025-11-16 04:06:00 | NOAA-20 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| aedab56b-7a48-3db6-a33d-88bb01980118 | -2.88844 | -53.2912 | 2025-11-16 04:06:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 16.2 |


[Clique aqui para ver as próximas entradas](README29.md)
