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

## Dados Diários - Página 82

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| f96e5dd7-3d36-3995-abda-ce9f117ec040 | -11.2125 | -54.0181 | 2026-08-29 14:50:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 94.8 |
| 917ebd72-2cb3-3dfc-b2e3-bb6669091e33 | -11.2489 | -45.0732 | 2026-08-29 14:50:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 136.0 |
| 015b6384-863c-3555-9db7-d859e4e433aa | -8.116 | -45.4715 | 2026-08-29 14:50:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 78.9 |
| 6191bc66-2df8-335a-8c4b-876d8fa0d64b | -14.3182 | -51.7046 | 2026-08-29 14:50:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 135.9 |
| c6fdb3dd-ad6c-3264-a51d-d635ae55ede3 | -8.9613 | -63.279 | 2026-08-29 14:50:00 | GOES-19 | ITAPUÃ DO OESTE | RONDÔNIA | Brasil | 1101104 | 11 | 33 | nan | nan | nan | Amazônia | 171.4 |
| 3089498b-fc43-32a1-93de-17cecb27bad9 | -3.9363 | -59.3381 | 2026-08-29 14:50:00 | GOES-19 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 69.6 |
| 073cec4b-12df-343e-aac2-affd7c947f0f | -8.9614 | -63.2601 | 2026-08-29 14:50:00 | GOES-19 | ITAPUÃ DO OESTE | RONDÔNIA | Brasil | 1101104 | 11 | 33 | nan | nan | nan | Amazônia | 110.2 |
| bcc7a23a-fac0-3c37-8e16-a33a11339597 | -10.8232 | -50.5239 | 2026-08-29 14:50:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 93.9 |
| 4be40918-1700-3cf3-8900-65913433c522 | -6.6317 | -43.73 | 2026-08-29 14:50:00 | GOES-19 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 161.6 |
| 0168f99a-4a2c-36c2-83ce-73975206c762 | -13.8752 | -54.1153 | 2026-08-29 14:50:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 104.7 |
| 06d16e6d-059f-344b-ab7c-efeb19f109d4 | -11.0247 | -49.6656 | 2026-08-29 14:50:00 | GOES-19 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 61.7 |
| 6354bad9-0cdc-3eca-bb4f-4f0b46578136 | -11.1916 | -51.2708 | 2026-08-29 14:50:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 95.5 |
| e8dcc71a-0662-323a-87d6-4b47c8b4a070 | -14.4142 | -51.7345 | 2026-08-29 14:50:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 135.9 |
| 90451cdf-ac31-3121-b6ce-5bfc61ce5d83 | -13.8563 | -54.0967 | 2026-08-29 14:50:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 291.5 |
| e318bf91-8600-3c40-876f-9ec1ba975f6b | -11.7167 | -54.5244 | 2026-08-29 14:50:00 | GOES-19 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 141.9 |
| ab8467db-e8cf-3efb-a36a-72960f24350f | -11.3622 | -45.1494 | 2026-08-29 14:50:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 76.1 |
| 24c9cb31-e195-3a3d-83a9-30eb251aece7 | -6.5508 | -55.2368 | 2026-08-29 14:50:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 108.5 |
| 84eda9dd-ad95-37a5-accf-2713f869545b | -14.4138 | -51.7559 | 2026-08-29 14:50:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 108.7 |
| c85e0bc8-d244-3020-ba7d-d9d3e568aeca | -5.8894 | -57.7708 | 2026-08-29 14:50:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 73.5 |
| 0464c867-7c14-34c0-8824-0864d5e600da | -11.2693 | -54.0129 | 2026-08-29 14:50:00 | GOES-19 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 70.5 |
| a16ebd50-8981-36a9-9e52-71fc723d8795 | -6.6129 | -43.7317 | 2026-08-29 14:50:00 | GOES-19 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 105.3 |
| b8f4cf20-bd56-3997-beed-1bf5e0d6baa1 | -10.8235 | -50.5026 | 2026-08-29 14:50:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 113.3 |
| 8616b4e1-8da2-3fab-b21c-46c5099af761 | -11.0244 | -49.6872 | 2026-08-29 14:50:00 | GOES-19 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 82.0 |
| 00acdfc0-f0ee-38a6-ab1f-a263794c791b | -8.948 | -62.3894 | 2026-08-29 14:50:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 78.1 |
| cb11baff-305f-3b0c-9808-e36cc4a1b358 | -8.7772 | -49.955 | 2026-08-29 14:50:00 | GOES-19 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 65.4 |
| 4419dabb-b7df-3136-b52f-735ba2257cdd | -10.9402 | -50.2764 | 2026-08-29 14:50:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 94.4 |
| 9c0ab486-164b-34c7-9e8d-cb78cfb5ec0c | -7.5662 | -61.3049 | 2026-08-29 14:50:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 185.6 |
| e1f35078-7419-3b5c-a204-2794814fd097 | -14.3863 | -50.0565 | 2026-08-29 14:50:00 | GOES-19 | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 67.0 |
| 1a941a54-05f0-3b80-ab1c-e10636d0ca25 | -11.2314 | -54.0164 | 2026-08-29 14:50:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 102.1 |
| 50558222-5fb0-332e-af34-a7bf68b8209f | -8.9481 | -62.3704 | 2026-08-29 14:50:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 60.1 |
| 46f17ba5-2391-3b9b-b00b-e299f3fe325e | -11.2298 | -45.0759 | 2026-08-29 14:50:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 80.7 |
| ad51307c-becd-3238-8a6b-5ae8d180c65d | -7.5139 | -55.2851 | 2026-08-29 14:50:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 68.9 |
| 20b26366-1175-374e-bbf4-d87603210b0e | -6.8571 | -59.4179 | 2026-08-29 14:50:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 66.4 |
| 438db640-21e2-39b8-bf8c-1d171c812e2e | -9.971 | -53.9214 | 2026-08-29 14:50:00 | GOES-19 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 91.8 |
| 6b9f9345-1e45-3fa6-9b8d-8087499de43f | -9.9708 | -53.9419 | 2026-08-29 14:50:00 | GOES-19 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 78.2 |
| 28df04c3-8c05-3b8c-a9be-edd4fcf059ce | -11.269 | -54.0334 | 2026-08-29 14:50:00 | GOES-19 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 78.1 |
| 59522d7d-1a50-3864-9809-68862fe7953e | -11.2317 | -53.9958 | 2026-08-29 14:50:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 97.3 |
| b7cce45c-4cef-3b4b-be86-251210281ec9 | -6.9303 | -45.6931 | 2026-08-29 14:50:00 | GOES-19 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 61.5 |
| b80fe41b-1a4c-3630-b15f-482bd57f74d2 | -11.2128 | -53.9976 | 2026-08-29 14:50:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 79.7 |
| 00cb2318-7ebb-373e-b35f-e885b354fffd | -10.9859 | -51.0807 | 2026-08-29 14:50:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 91.6 |
| 45be5f59-b120-3d77-86ed-e3c9c61d9d90 | -4.8001 | -43.1943 | 2026-08-29 14:50:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 74.2 |
| 2ef29e21-8447-3787-8c9c-12e103304d5a | -6.6315 | -43.7533 | 2026-08-29 14:50:00 | GOES-19 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 96.8 |
| 29d56171-2142-309e-ba45-91aa4c54a32d | -8.9428 | -63.2797 | 2026-08-29 14:50:00 | GOES-19 | ITAPUÃ DO OESTE | RONDÔNIA | Brasil | 1101104 | 11 | 33 | nan | nan | nan | Amazônia | 155.3 |
| 79803525-3e4b-3afa-b684-b21c874fc0de | -9.9288 | -60.4277 | 2026-08-29 14:50:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 67.6 |
| aac75820-2d1a-3f90-81f4-5c0b4b320e0f | -11.7165 | -54.5449 | 2026-08-29 14:50:00 | GOES-19 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 110.4 |
| b9603437-98f8-321e-85a1-2bffd07458d9 | -13.3254 | -46.9333 | 2026-08-29 14:50:00 | GOES-19 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 74.1 |
| da39d4cd-4e26-32fe-b5ee-1e4cff34f29f | -13.9919 | -54.0189 | 2026-08-29 14:50:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 95.5 |
| 994b39d4-c710-36cb-aef8-00af109039b6 | -6.1657 | -57.7793 | 2026-08-29 14:50:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 72.4 |
| f40b4afd-b004-3e1d-a086-b8ed3c634425 | -10.9673 | -51.0614 | 2026-08-29 14:50:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 112.3 |
| c6c7c8e0-b4d0-3725-93e8-2b3068c0a407 | -8.7769 | -49.9763 | 2026-08-29 14:50:00 | GOES-19 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 70.4 |
| d40dd8af-347b-36e0-996c-45d108eae193 | -11.0443 | -57.2222 | 2026-08-29 14:50:00 | GOES-19 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 58.1 |
| 9438ff4e-3bdd-378c-886b-03fda402d07b | -12.3811 | -48.1877 | 2026-08-29 14:50:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 103.4 |
| c40ff38d-e138-3469-9edd-03ecea340098 | -10.7791 | -53.9752 | 2026-08-29 14:50:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 89.7 |
| c889ab9e-4f8e-3e0e-b0d2-45968cf9354f | -13.9915 | -54.0397 | 2026-08-29 14:50:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 69.2 |
| 67441403-b15e-3fb8-8ffc-027a5534d439 | -13.8567 | -54.0759 | 2026-08-29 14:50:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 74.3 |
| f88ad592-1edb-3d4f-bbf3-c923255e5b69 | -9.1739 | -56.9754 | 2026-08-29 14:50:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 74.4 |
| 25b60219-5f78-35d3-ad65-5a6bd69a259b | -11.1726 | -51.2728 | 2026-08-29 14:50:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 77.5 |
| 10c87e09-d3cf-3e4a-a5a9-b39b489ae081 | -11.0254 | -57.2237 | 2026-08-29 14:50:00 | GOES-19 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 51.7 |
| 6b2bc8cc-2088-36ff-baa4-111108b5ba41 | -14.4057 | -50.0537 | 2026-08-29 14:50:00 | GOES-19 | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 69.6 |
| 191a39ad-494e-3f9c-9bb2-94e8d24ce38b | -10.8804 | -50.4965 | 2026-08-29 14:50:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 100.2 |
| 60f38781-ea2b-3364-8e93-046e2b79a417 | 2.2375 | -50.7515 | 2026-08-29 14:50:00 | GOES-19 | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 89.3 |
| 3f594d14-93bc-33af-ae54-c9ce01b0d754 | -10.0731 | -48.6868 | 2026-08-29 14:50:00 | GOES-19 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 53.2 |
| bff6f0e5-c0f9-339d-bdc0-2e5859263918 | -10.3391 | -49.9762 | 2026-08-29 14:50:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 58.8 |
| 5bf6aefd-8dde-3236-8533-71dfa4f81b05 | -14.4 | -52.565 | 2026-08-29 14:50:00 | GOES-19 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 94.9 |
| 64d3b75a-b537-30d6-88ca-13fffb56a238 | -6.9193 | -44.9467 | 2026-08-29 14:50:00 | GOES-19 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 58.0 |
| caa69297-3a28-3ea6-8d7f-8093ffeae819 | -12.2284 | -50.5363 | 2026-08-29 14:50:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 195.7 |
| d3f9f22f-358a-3b41-b878-a3de9b913615 | -13.856 | -54.1175 | 2026-08-29 14:50:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 104.3 |
| efb65fb8-11fc-3cc0-b15d-70105294aa0e | -13.8756 | -54.0945 | 2026-08-29 14:50:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 280.3 |
| d348b47d-95ee-3c1b-90b6-c7868f83ffc1 | -10.8161 | -54.0334 | 2026-08-29 14:50:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 69.6 |
| e065d14e-2a70-3175-ae57-80a46924f512 | -8.7767 | -49.9977 | 2026-08-29 14:50:00 | GOES-19 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 73.2 |
| ef3bb594-8a4d-34c2-bada-bd0013cb5b8c | -8.5602 | -54.7175 | 2026-08-29 14:50:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 72.5 |
| 05de7960-a342-30fe-b5b0-9cf72549ffbf | -10.5404 | -50.4683 | 2026-08-29 14:50:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 90.4 |
| 6b2760fa-65c7-35e4-a040-34414743b36e | -12.2475 | -50.534 | 2026-08-29 14:50:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 101.8 |
| 1597aa5d-b4fa-332c-85b6-40ce28dc0021 | -7.0057 | -59.2575 | 2026-08-29 14:50:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 72.9 |
| 735948f8-dc17-31b2-8bf3-66db22003d56 | -9.2094 | -51.5444 | 2026-08-29 14:50:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 63.2 |
| 7666f795-9735-3b38-af1a-632b2bf3628e | -10.8425 | -50.5005 | 2026-08-29 14:50:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 78.7 |
| 814d4cd5-7944-360d-ba94-e6b0c0d43b8a | -15.3654 | -53.7887 | 2026-08-29 14:50:00 | GOES-19 | POXORÉU | MATO GROSSO | Brasil | 5107008 | 51 | 33 | nan | nan | nan | Cerrado | 79.9 |
| 684a01c0-a559-3196-98f7-973fde2f8b07 | -9.6022 | -55.128 | 2026-08-29 14:50:00 | GOES-19 | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 52.5 |
| a60b7a2d-8362-375f-aeb5-c9758e0e56d8 | -11.0054 | -49.6893 | 2026-08-29 14:50:00 | GOES-19 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 75.2 |
| 77f0fcac-b322-3401-bb22-8f77dd5bd89a | -9.9708 | -53.9419 | 2026-08-29 15:00:00 | GOES-19 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 104.9 |
| 7c43138e-043e-366f-bbab-bacbe2ff2225 | -6.6127 | -43.7549 | 2026-08-29 15:00:00 | GOES-19 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 58.1 |
| 2914c86b-ec82-33bc-8ca2-98c15abee29e | -13.8563 | -54.0967 | 2026-08-29 15:00:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 224.0 |
| 9b3a61ac-3e8d-3b0a-aba3-bc4ff5338829 | -11.0057 | -49.6677 | 2026-08-29 15:00:00 | GOES-19 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 64.1 |
| 3faa0b89-1119-3648-be61-1f270e947581 | -11.0247 | -49.6656 | 2026-08-29 15:00:00 | GOES-19 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 57.9 |
| ef0dde7e-dba7-3f6b-918e-0dc31ae3add7 | -13.9915 | -54.0397 | 2026-08-29 15:00:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 64.3 |
| 9937a260-107b-33c3-b04f-7ad421302cfe | -13.8752 | -54.1153 | 2026-08-29 15:00:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 149.7 |
| 31ea6607-409e-3753-8a5b-74b04c36e26f | -11.7165 | -54.5449 | 2026-08-29 15:00:00 | GOES-19 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 112.6 |
| 71d448b1-b79a-3180-9a83-1c2aa27fe653 | -8.116 | -45.4715 | 2026-08-29 15:00:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 88.5 |
| 3a9c4a8e-d233-34b6-995f-49cba7c3a0ea | -11.269 | -54.0334 | 2026-08-29 15:00:00 | GOES-19 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 85.7 |
| b4441288-9da4-36b5-b85d-9c3cc1c9940f | -9.2282 | -51.5428 | 2026-08-29 15:00:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 61.6 |
| 85fbb28f-03bf-365c-b98b-3bfca5e0c813 | -11.0054 | -49.6893 | 2026-08-29 15:00:00 | GOES-19 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 60.9 |
| 7749fba2-715a-3f46-975c-598e1cae4101 | -6.6317 | -43.73 | 2026-08-29 15:00:00 | GOES-19 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 128.0 |
| 50e91758-4afe-359e-a99e-2c0f5b3ef8ee | -11.1639 | -45.5897 | 2026-08-29 15:00:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 95.3 |
| 6fca563c-1e11-3712-9539-9c3a7f92f38a | -11.2298 | -45.0759 | 2026-08-29 15:00:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 106.5 |
| 00af0fec-095f-3f0d-8f9e-d67847655a62 | -9.1552 | -56.9766 | 2026-08-29 15:00:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 56.6 |
| 3681151b-f109-3333-82a0-01f77e9b9d75 | -11.1723 | -51.294 | 2026-08-29 15:00:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 161.7 |
| 491e191b-5c76-3c8b-9e11-8ae2cab40256 | -11.1441 | -50.5961 | 2026-08-29 15:00:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 81.3 |
| 3d651996-6d8c-3c20-a2af-a5876136600c | -20.941 | -57.5694 | 2026-08-29 15:00:00 | GOES-19 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Pantanal | 62.7 |
| 0a572c3c-31e7-3462-89eb-ca38b5bfcde8 | -13.8756 | -54.0945 | 2026-08-29 15:00:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 213.7 |
| 241df05c-ca8a-3c38-9503-3f968e31c009 | -14.2024 | -52.8643 | 2026-08-29 15:00:00 | GOES-19 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 69.2 |


[Clique aqui para ver as próximas entradas](README83.md)
