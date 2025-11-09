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

## Dados Diários - Página 30

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 32f8b5af-3da6-3798-8c60-18fbf048f567 | -3.40317 | -50.27709 | 2025-11-09 04:38:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 30cda025-05a5-321a-a764-f31357969f4d | -4.63642 | -46.39724 | 2025-11-09 04:38:00 | NOAA-20 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 42aed182-d7f0-302a-9b6f-2e1b4735fce4 | -4.72172 | -48.30659 | 2025-11-09 04:38:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 843024f3-88c6-3532-aa94-ee05d02b6551 | -4.73639 | -50.68586 | 2025-11-09 04:38:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 3622c8dc-da8e-3237-9d8a-f64eaba0bdf9 | -4.11279 | -47.28815 | 2025-11-09 04:38:00 | NOAA-20 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| a88e4a91-3f4c-3ae9-9c50-7f6b79e51521 | -4.3951 | -49.77321 | 2025-11-09 04:38:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| bc502358-0173-3465-8a19-11423ee8118f | -4.06971 | -48.95367 | 2025-11-09 04:38:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 25e6f9c9-6848-394b-a307-069f702b033f | -2.50693 | -49.46505 | 2025-11-09 04:38:00 | NOAA-20 | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 682ad2a1-367a-3644-a23d-acf1ddeb2d14 | -3.45739 | -50.2193 | 2025-11-09 04:38:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 0c2c6785-9e99-30c6-9e73-b26776e3b31a | -5.21317 | -45.14489 | 2025-11-09 04:38:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 64936359-625b-3e96-9ab3-52ef29709db8 | -6.76443 | -46.67389 | 2025-11-09 04:38:00 | NOAA-20 | SÃO PEDRO DOS CRENTES | MARANHÃO | Brasil | 2111573 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| b3e81694-d203-3a43-8ae2-9e7097caf1a6 | -3.09628 | -49.26222 | 2025-11-09 04:38:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 6abdfb9f-45e6-38d2-b7b7-46c0f41fd6c1 | -4.39546 | -45.97022 | 2025-11-09 04:38:00 | NOAA-20 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 320f75d8-2483-3670-b3ee-53924d21dcf1 | -4.28756 | -50.66413 | 2025-11-09 04:38:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 7.3 |
| 0b60b3f7-ade4-34eb-9624-9c6f2c1ec0e4 | -3.42409 | -50.25455 | 2025-11-09 04:38:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 8625c507-87f1-3e9d-bc9a-1e24274a8bef | -4.11955 | -47.28924 | 2025-11-09 04:38:00 | NOAA-20 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 62f06cbc-2164-3190-a2b4-7bd7b2d5e545 | -4.8732 | -49.00656 | 2025-11-09 04:38:00 | NOAA-20 | NOVA IPIXUNA | PARÁ | Brasil | 1504976 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| bdea5cfc-65d3-3ba1-81c4-fd91fe77812b | -3.14326 | -50.27312 | 2025-11-09 04:38:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 90e1081e-3147-33b9-bf46-a232f67455f9 | -2.92148 | -52.51308 | 2025-11-09 04:38:00 | NOAA-20 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 36ae2edd-8696-326b-a3c0-354ef051e5d3 | -2.94177 | -49.35863 | 2025-11-09 04:38:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 14.5 |
| 58a4a44e-03bb-357b-be9f-8663572229e9 | -4.00633 | -44.78607 | 2025-11-09 04:38:00 | NOAA-20 | BACABAL | MARANHÃO | Brasil | 2101202 | 21 | 33 | nan | nan | nan | Amazônia | 2.8 |
| d9439a2c-f6fd-3cc8-af27-994c81e42f0a | -5.91803 | -42.71198 | 2025-11-09 04:38:00 | NOAA-20 | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| f3675aa8-42c4-3417-816e-12af2cf91564 | -5.44422 | -45.86935 | 2025-11-09 04:38:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 6a683b8f-1fd9-3d22-a361-334a790782c2 | -4.90314 | -48.62286 | 2025-11-09 04:38:00 | NOAA-20 | BOM JESUS DO TOCANTINS | PARÁ | Brasil | 1501576 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c215a885-163b-3a78-99f2-5cf49aa4063e | -3.86557 | -49.38348 | 2025-11-09 04:38:00 | NOAA-20 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 4685b054-c723-3f23-9e8d-8d7a1c6111d1 | -6.74468 | -44.29737 | 2025-11-09 04:38:00 | NOAA-20 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 50b598ea-c2a4-38ba-b91b-b681124331b3 | -3.97929 | -51.03439 | 2025-11-09 04:38:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| be95d5ff-7e68-3ee7-9d37-30430d555760 | -3.5618 | -51.12553 | 2025-11-09 04:38:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 3b631c05-109d-34b7-9ba4-a17047af6c22 | -4.81779 | -46.80255 | 2025-11-09 04:38:00 | NOAA-20 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 95a47965-d97c-339c-b07f-ec6bbf341bd5 | -4.3929 | -49.65876 | 2025-11-09 04:38:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 56afd547-21ef-31be-80e0-f6184b9f7593 | -3.08721 | -50.3199 | 2025-11-09 04:38:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c6f3148e-3211-3120-923c-f28165abd202 | -4.01505 | -49.72755 | 2025-11-09 04:38:00 | NOAA-20 | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| c2f529dc-148f-3855-b9bf-bb8a6247ccf2 | -6.0487 | -58.05282 | 2025-11-09 04:38:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 85abbe25-04bf-302a-b649-b8f4fc7e3006 | -6.87248 | -47.24487 | 2025-11-09 04:38:00 | NOAA-20 | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| aa2bd9bd-8c4d-3239-b9a0-2f1604c4340d | -3.03821 | -50.27232 | 2025-11-09 04:38:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 5737d852-b59c-32c4-b607-240e35bafb24 | -3.24285 | -50.02802 | 2025-11-09 04:38:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 1b5e1d12-a237-3a73-86c7-5b0e11c765b4 | -4.13384 | -49.25642 | 2025-11-09 04:38:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 58a64893-b657-3670-8c87-f181c080a5b4 | -5.57318 | -47.13096 | 2025-11-09 04:38:00 | NOAA-20 | BURITIRANA | MARANHÃO | Brasil | 2102358 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 669e34f0-0fbe-3c44-a145-d18e505c1403 | -3.32 | -50.10598 | 2025-11-09 04:38:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 8.0 |
| 7476d81e-9b93-3fff-9945-2d1b1516754b | -3.35943 | -51.28482 | 2025-11-09 04:38:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 4505b0cd-9003-389f-918c-ffec747afbb1 | -3.95 | -49.02256 | 2025-11-09 04:38:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 4ca9413c-67c7-33ae-9d31-cee24609dbd7 | -3.50035 | -50.05779 | 2025-11-09 04:38:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f0582146-e3ce-3105-b8b9-21b763457fba | -2.92204 | -40.00677 | 2025-11-09 04:38:00 | NOAA-20 | ACARAÚ | CEARÁ | Brasil | 2300200 | 23 | 33 | nan | nan | nan | Caatinga | 4.0 |
| 32facea2-02ce-3245-a69e-beec5c170d30 | -5.49417 | -45.8595 | 2025-11-09 04:38:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| e6b90893-7d9c-3ea7-8e91-b229c7fab24e | -3.64173 | -49.87339 | 2025-11-09 04:38:00 | NOAA-20 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 769137d1-3508-3b56-9d1e-a24c6c82896b | -2.62377 | -50.07787 | 2025-11-09 04:38:00 | NOAA-20 | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 9d54910b-d172-3f52-b335-4851d40f1c31 | -4.4326 | -43.57919 | 2025-11-09 04:38:00 | NOAA-20 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 9.1 |
| 6e2a88d9-95bc-3ec9-bab2-520f4befbfbe | -3.73558 | -52.66063 | 2025-11-09 04:38:00 | NOAA-20 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 826ece1d-752b-3e11-877f-b129f49862db | -4.62941 | -46.39608 | 2025-11-09 04:38:00 | NOAA-20 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| aaccc59d-7018-32d6-8104-e8172e877742 | -3.33382 | -50.03125 | 2025-11-09 04:38:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 0aa8eec1-4afb-3fe2-bc00-28db5e4fc930 | -4.63921 | -49.54175 | 2025-11-09 04:38:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| de1f23cc-2cae-3a7c-946e-a6f2e4134b51 | -4.29228 | -49.73526 | 2025-11-09 04:38:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 9f6bed8f-5c41-3447-8bf3-a54fb4dd1fc7 | -3.32181 | -50.10604 | 2025-11-09 04:38:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 507290d6-4264-3c37-85b0-73c27eb77fff | -3.74191 | -52.17889 | 2025-11-09 04:38:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 933e61cb-90fb-3374-8733-4e63af1665d9 | -3.41052 | -52.19144 | 2025-11-09 04:38:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 7adf0aad-0b47-36f6-bc0c-498827f6d5ca | -3.81247 | -45.99359 | 2025-11-09 04:38:00 | NOAA-20 | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 2.5 |
| bd9be12f-a2f3-385f-86eb-c4dc21b32d27 | -4.96083 | -44.9479 | 2025-11-09 04:38:00 | NOAA-20 | ESPERANTINÓPOLIS | MARANHÃO | Brasil | 2104008 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| b0ee4048-fc10-3000-92f8-9c5df52f4a9c | -2.60671 | -49.22067 | 2025-11-09 04:38:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| e70836f2-b259-3422-b421-b5f1fb76226f | -4.12718 | -49.79173 | 2025-11-09 04:38:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| e2d746d2-491d-3ebc-a573-ef11a680dcd9 | -4.40393 | -45.96288 | 2025-11-09 04:38:00 | NOAA-20 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| fc8f6a90-9daf-3665-b7b2-c19008212a2b | -3.79504 | -51.30308 | 2025-11-09 04:38:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c24ea337-dd67-3743-a4e7-677a2c2d59e0 | -4.28698 | -50.66779 | 2025-11-09 04:38:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 3c56999b-5306-3b84-b141-3011a7bbd734 | -4.51982 | -45.72527 | 2025-11-09 04:38:00 | NOAA-20 | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| cc82aeaa-1208-3726-b9a8-efb614611b4b | -7.1728 | -41.74119 | 2025-11-09 04:38:00 | NOAA-20 | SANTA CRUZ DO PIAUÍ | PIAUÍ | Brasil | 2209104 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 826a8311-6b92-3d80-a3f4-8b19606f7a02 | -5.28459 | -44.95539 | 2025-11-09 04:38:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 9.1 |
| 0f09a064-e450-33ad-9b65-926f9e9de4c1 | -3.59097 | -49.33691 | 2025-11-09 04:38:00 | NOAA-20 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 728f3074-8bf7-3cdd-8b6e-2127003202a4 | -3.9204 | -51.00962 | 2025-11-09 04:38:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 8853aa23-7b9d-32a9-877a-95230f8be582 | -7.54682 | -45.85646 | 2025-11-09 04:38:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| e3c18749-45bf-347b-8c37-8c7040cd5b38 | -4.40008 | -49.65634 | 2025-11-09 04:38:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 11.0 |
| 8b920a9a-cabd-38ca-8b42-fde1fa8fed9e | -1.25233 | -53.34077 | 2025-11-09 04:38:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 00ed5e51-7237-3138-b347-a742ada8ce1f | -2.62345 | -46.85392 | 2025-11-09 04:38:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 6d460698-79ac-35b1-80d7-fcdb845cc31d | -6.62913 | -56.28843 | 2025-11-09 04:38:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 9ac28d38-8579-3317-bfa6-576790a93750 | -4.51683 | -45.72057 | 2025-11-09 04:38:00 | NOAA-20 | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 0872a825-c977-32a6-8993-e8b0a04f7ed7 | -4.21862 | -48.35245 | 2025-11-09 04:38:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 81a84eba-95d3-3afb-bdee-cb98c1954580 | -2.96552 | -49.82843 | 2025-11-09 04:38:00 | NOAA-20 | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d482994c-6f4e-3de5-bc04-74e8ab24f389 | -3.65049 | -50.26387 | 2025-11-09 04:38:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| e331ba10-978f-3b90-b957-3a85dc3bb04c | -3.58249 | -51.25058 | 2025-11-09 04:38:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| c933c870-66c1-3d7a-9e5e-9f90807b0259 | -4.39784 | -45.15955 | 2025-11-09 04:38:00 | NOAA-20 | VITORINO FREIRE | MARANHÃO | Brasil | 2113009 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d3a46779-f6ab-3dc2-891b-9736adffcff0 | -4.67878 | -46.40713 | 2025-11-09 04:38:00 | NOAA-20 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e8c7fc57-0948-3ba3-9572-330759927fa6 | -3.08565 | -52.92031 | 2025-11-09 04:38:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| bfcdf8e1-7531-337e-8f0a-56022ea7ac7a | -3.25207 | -50.1429 | 2025-11-09 04:38:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b3b2c8d9-abda-36dc-ac31-ba3d3ea10ea6 | -4.12164 | -49.80519 | 2025-11-09 04:38:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| bd5e6d4b-c41b-3b47-94ff-17229266be54 | -4.2749 | -48.33998 | 2025-11-09 04:38:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 17811531-b668-3d0a-b567-0d1511589f68 | -4.39905 | -45.9707 | 2025-11-09 04:38:00 | NOAA-20 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 83da8278-729c-3103-bd27-26f1e5c411aa | -3.65041 | -50.28598 | 2025-11-09 04:38:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| d9fa9444-f9c3-39fc-91e4-d2fcdb539ff0 | -3.12991 | -49.24269 | 2025-11-09 04:38:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 4a847b93-aada-3bdf-9075-72bf817b4f66 | -3.09621 | -50.32878 | 2025-11-09 04:38:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 75d80e6e-b00f-31d8-ba41-c00ae3f11922 | -3.31664 | -50.10545 | 2025-11-09 04:38:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 8.0 |
| c0e2c683-95d7-3c01-902b-0bcaf01ab92d | -3.32125 | -53.35905 | 2025-11-09 04:38:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| e9479227-6020-39d6-a003-3add3307c00e | -5.7378 | -46.45699 | 2025-11-09 04:38:00 | NOAA-20 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 8b881dff-a06d-37e8-beb8-9c4355b5752a | -7.43051 | -46.71774 | 2025-11-09 04:38:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| f6cfda3f-e90b-32fc-8a2b-4eed60635053 | -6.08299 | -42.69672 | 2025-11-09 04:38:00 | NOAA-20 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 4.6 |
| 2a9c4c73-5cd2-3983-91ef-eace1d7cf3c2 | -2.54634 | -45.15787 | 2025-11-09 04:38:00 | NOAA-20 | PINHEIRO | MARANHÃO | Brasil | 2108603 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 08f74212-24b7-32f7-880a-73d46323a4b2 | -7.03885 | -46.98448 | 2025-11-09 04:38:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 110fe444-5bca-363d-b37f-e279eea93e58 | -3.62828 | -43.15461 | 2025-11-09 04:38:00 | NOAA-20 | MATA ROMA | MARANHÃO | Brasil | 2106409 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 54db2803-c294-30e9-b6b6-7b8fc6b40d97 | -4.40285 | -49.66034 | 2025-11-09 04:38:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 6.7 |
| ca61947b-4b15-38c2-a21f-f9af8fa5756f | -5.43549 | -47.5672 | 2025-11-09 04:38:00 | NOAA-20 | IMPERATRIZ | MARANHÃO | Brasil | 2105302 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 21d7bf88-e7ae-3779-a4a7-49b21b923fb5 | -4.72067 | -42.93538 | 2025-11-09 04:38:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 903c9f73-5d62-31a1-b44b-5f326287295b | -2.25774 | -47.87902 | 2025-11-09 04:38:00 | NOAA-20 | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 8fbf99d9-4c99-38d9-afb4-2529690c3d0c | -4.32939 | -49.75897 | 2025-11-09 04:38:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |


[Clique aqui para ver as próximas entradas](README31.md)
