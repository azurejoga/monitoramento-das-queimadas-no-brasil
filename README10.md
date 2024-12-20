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

## Dados Diários - Página 10

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 8ec1541f-187b-32ee-9a02-905dc695197f | -2.77037 | -47.38811 | 2024-12-20 05:03:00 | NOAA-21 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| b9dd1141-c323-3881-b479-f8d2aef69a58 | -4.0764 | -50.00854 | 2024-12-20 05:03:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| cfd52758-e5d6-3e61-8455-a851da2dd402 | -2.63241 | -48.05145 | 2024-12-20 05:03:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 01e0c2b2-ca05-3687-80c9-292aede5f6fb | 0.48936 | -51.08173 | 2024-12-20 05:03:00 | NOAA-21 | FERREIRA GOMES | AMAPÁ | Brasil | 1600238 | 16 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 6618ac9d-e86d-37b4-9b66-16c0ea710024 | -1.72557 | -52.55322 | 2024-12-20 05:03:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| b88629a6-54be-3a10-b962-b1f940b3f826 | -2.76761 | -47.3856 | 2024-12-20 05:03:00 | NOAA-21 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| b854ea3f-54d8-3c41-a244-c2536280546b | -0.35793 | -50.09 | 2024-12-20 05:03:00 | NOAA-21 | CHAVES | PARÁ | Brasil | 1502509 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| a7608e40-0cd0-3273-9692-74590064916c | -1.25437 | -53.48433 | 2024-12-20 05:03:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 001119a7-3545-317a-a619-4ddfd8da162f | -3.00731 | -46.71064 | 2024-12-20 05:03:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 4ff32276-e240-3ae7-8c8d-0c4493d16d79 | -0.85907 | -51.73705 | 2024-12-20 05:03:00 | NOAA-21 | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 1.6 |
| ed47d18d-4547-3b74-8f11-a746186a69c3 | -4.15109 | -48.99266 | 2024-12-20 05:03:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| ebaecc48-9eb6-3abf-8920-87ebce2921fe | -3.23683 | -46.79007 | 2024-12-20 05:03:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ac6191eb-4f62-306c-992b-0f3ff2d8cab9 | -1.61567 | -45.8376 | 2024-12-20 05:03:00 | NOAA-21 | AMAPÁ DO MARANHÃO | MARANHÃO | Brasil | 2100550 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 8cd26c5c-7fa9-3932-8ee1-6ea9857cec2b | -1.00963 | -53.13841 | 2024-12-20 05:03:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 5169cafa-4856-395e-9fd8-22c167fc736c | -1.23671 | -53.9032 | 2024-12-20 05:03:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 82dbed2b-7c15-36cd-8a78-4c7f24802c8a | -1.25859 | -54.13441 | 2024-12-20 05:03:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 08e8777f-78e4-32ac-9ab4-6eddab93ed51 | -1.25492 | -53.48077 | 2024-12-20 05:03:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 11496746-a128-333d-ae96-8ace8d690858 | -1.50507 | -52.64119 | 2024-12-20 05:03:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 8f3ada1b-fe8a-3287-bc49-e6fe7139f6b6 | -1.68361 | -53.27766 | 2024-12-20 05:03:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 2883012e-321b-3ba3-8d6a-30fcc921ec35 | -1.3122 | -53.52562 | 2024-12-20 05:03:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 1aa6a74c-5db6-32fc-8117-c240bab6f7e3 | -2.58817 | -51.91866 | 2024-12-20 05:03:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| db3cfa08-75cc-3291-9ebc-db34ec1fcee0 | -3.22994 | -46.80146 | 2024-12-20 05:03:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b5bcf3ea-be74-3b5f-9a56-4a7d5b6ac74f | -1.02511 | -52.95066 | 2024-12-20 05:03:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 068b3d64-867b-33e3-bfef-3c52afc3edf8 | -1.25163 | -53.52393 | 2024-12-20 05:03:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ed1f75a4-4c7a-3183-8153-6c439a4e0ba8 | -2.96422 | -54.16632 | 2024-12-20 05:03:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 7f6875f5-a3b1-3422-a602-99421dd6eb36 | -2.76597 | -47.39634 | 2024-12-20 05:03:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 3538c3f1-eabb-3b2a-b4eb-5d8bfab0db75 | -6.0424 | -44.04241 | 2024-12-20 05:03:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 9.5 |
| 233c0566-67fb-3548-a953-580cd10816ea | -0.25467 | -51.5001 | 2024-12-20 05:03:00 | NOAA-21 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 0.7 |
| d0911436-0d6c-32d7-9723-e6e29c489ffe | -3.21062 | -45.50782 | 2024-12-20 05:03:00 | NOAA-21 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| ea046e21-39fe-3bf7-95df-9b90bb36833e | -1.26306 | -54.1493 | 2024-12-20 05:03:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 1d8a9e95-e9cb-332c-8633-96bba0acdefd | -2.92152 | -54.57336 | 2024-12-20 05:03:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 33b5bffb-8a7d-3e8d-bb47-b8ab4152f13f | -1.28328 | -53.18732 | 2024-12-20 05:03:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 29f5cfc8-7065-3c42-a970-b6df1b92a4d1 | -2.09852 | -53.58738 | 2024-12-20 05:03:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 8875b9de-4ae6-35f2-b3eb-9a10a269a7d9 | -2.38933 | -47.08291 | 2024-12-20 05:03:00 | NOAA-21 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 2b9c2606-6730-31bd-a253-9bc37fc1adca | -9.22532 | -60.33071 | 2024-12-20 05:05:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 4.6 |
| d73e11ae-ef4d-3248-8431-15ecf930a474 | -9.22459 | -60.33516 | 2024-12-20 05:05:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 4.6 |
| dc94d5ee-7c1d-3c11-a53e-e4a3374d2858 | -9.45271 | -62.05244 | 2024-12-20 05:05:00 | NOAA-21 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 2.9 |
| dfd68dc2-1b72-3cf0-a6cc-bb7ee3eaefea | -9.21943 | -60.34343 | 2024-12-20 05:05:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 7.7 |
| 780698a6-2a6a-3484-8891-15ea285d293c | -9.23349 | -61.93925 | 2024-12-20 05:05:00 | NOAA-21 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 0.7 |
| d1155dd7-42cd-335c-b6c8-849cee0de434 | -6.9644 | -44.84281 | 2024-12-20 05:05:00 | NOAA-21 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 36aa27d7-c3f9-3473-b8ac-344d67e8c97a | -9.44799 | -62.05543 | 2024-12-20 05:05:00 | NOAA-21 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 4.2 |
| ef763002-7c05-3dc9-afde-678045e65842 | -9.21869 | -60.34789 | 2024-12-20 05:05:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 5f183e93-1d49-39b0-a9b0-c0355796f5fe | -9.2261 | -60.34916 | 2024-12-20 05:05:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f3822f3d-ac31-3507-a902-719ea1e8cd4e | -9.22386 | -60.33961 | 2024-12-20 05:05:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 7.7 |
| cb07a979-76bc-3c60-853b-b141e9f6d7f1 | -7.2501 | -44.71268 | 2024-12-20 05:05:00 | NOAA-21 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 0ac7e1a6-d2c1-3d03-9d61-5e3e58285af4 | -9.22903 | -60.33132 | 2024-12-20 05:05:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.9 |
| d5870e6b-12e5-33fb-b6cd-5752373ddbb9 | -9.5196 | -47.78223 | 2024-12-20 05:05:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| faf4deac-902a-3047-9f79-e83763c1dbb1 | -9.22829 | -60.33579 | 2024-12-20 05:05:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 7c3d502c-abef-323d-9aea-05db9824ccce | -9.21348 | -60.33334 | 2024-12-20 05:05:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 60ddae05-ae11-3d2e-bc23-6e21aa1b223b | -9.51439 | -47.78128 | 2024-12-20 05:05:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 245bf2db-066a-3b74-913c-55558d10a443 | -9.2224 | -60.34851 | 2024-12-20 05:05:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 71827d04-04a3-31db-a80b-017366de58ea | -9.21645 | -60.33836 | 2024-12-20 05:05:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e52eab9e-ddac-3303-9915-94bfc7018166 | -9.21718 | -60.33393 | 2024-12-20 05:05:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 1bf51953-4d7a-3819-923b-04223461fa5d | -9.22016 | -60.33898 | 2024-12-20 05:05:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 7.7 |
| a61d5693-0983-3ca0-a97a-b074fb801fc3 | -9.22089 | -60.33454 | 2024-12-20 05:05:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 4c484f73-a909-35aa-a346-86235e723e8d | -9.44862 | -62.05173 | 2024-12-20 05:05:00 | NOAA-21 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 6c7717bf-e185-31a4-854d-095ce9763bbe | -9.22756 | -60.34025 | 2024-12-20 05:05:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 88ddc4a6-5de7-352d-a8c9-a1ad9ef9d8b1 | -9.22162 | -60.3301 | 2024-12-20 05:05:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 1688f475-eaba-3b48-a0a5-b75d0721e793 | -9.22683 | -60.34469 | 2024-12-20 05:05:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 2da4d238-8a53-3894-bce5-321eafdb1014 | -9.21572 | -60.34282 | 2024-12-20 05:05:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 75d4ed10-544c-3791-83a7-d53098e920b6 | -9.44734 | -62.05916 | 2024-12-20 05:05:00 | NOAA-21 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 4eb7bc6e-c839-3e1a-b116-4003c677c000 | -9.22313 | -60.34405 | 2024-12-20 05:05:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 7.7 |
| 443e6a5b-aa2c-371a-8048-6776f1d02090 | -9.16249 | -49.49659 | 2024-12-20 05:05:00 | NOAA-21 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| ae24e251-677e-3fa9-bdcf-a0959999bac7 | -9.232 | -60.3364 | 2024-12-20 05:05:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 4fb2073f-866d-3917-ad8b-22ed94d848a6 | -9.23273 | -60.33193 | 2024-12-20 05:05:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.9 |
| c10059df-e40d-3f1a-a4f5-4ccecb22d9ff | -18.73917 | -56.56258 | 2024-12-20 05:08:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.6 |
| d637ae4c-7168-3362-aafd-f84733257e2a | -11.93818 | -63.17308 | 2024-12-20 05:08:00 | NOAA-21 | SERINGUEIRAS | RONDÔNIA | Brasil | 1101500 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| f83e89a8-12a6-3b43-9d85-cb882adc9888 | -12.23038 | -54.31103 | 2024-12-20 05:08:00 | NOAA-21 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 9bb24494-1eaf-3c45-bfc7-e464d175a076 | -12.18667 | -64.06039 | 2024-12-20 05:08:00 | NOAA-21 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a85a3120-b756-3ecf-aa23-656f9e6e822e | -12.1822 | -64.0596 | 2024-12-20 05:08:00 | NOAA-21 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 8c424b19-9ec7-3c4f-bfdb-a3bcacbcc079 | -12.33482 | -64.2402 | 2024-12-20 05:08:00 | NOAA-21 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 1.9 |
| b35eb07e-f745-31c2-a75f-390f037ded09 | -12.22621 | -54.31464 | 2024-12-20 05:08:00 | NOAA-21 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 891de7d6-6f9d-35f5-b986-4c8695f2eab8 | -11.99378 | -57.20199 | 2024-12-20 05:08:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| deae1054-4cbb-3ff3-b2cc-a677dcaba854 | -12.23396 | -54.31155 | 2024-12-20 05:08:00 | NOAA-21 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| e780bf25-bd7a-3b35-96a9-ab228f26ffb7 | -11.94242 | -63.1738 | 2024-12-20 05:08:00 | NOAA-21 | SERINGUEIRAS | RONDÔNIA | Brasil | 1101500 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f1f2b828-53c4-3e3a-ada4-26f59c321857 | -11.43779 | -55.89062 | 2024-12-20 05:08:00 | NOAA-21 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 1c9f882f-d0c5-3898-b0c8-574288d5856e | -14.52621 | -59.96951 | 2024-12-20 05:08:00 | NOAA-21 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 554544bd-a638-324e-ab5f-bc8b67eb65d4 | -12.18441 | -64.06267 | 2024-12-20 05:08:00 | NOAA-21 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 893c7a67-dbba-383b-8896-e52c1b3ea1f1 | -15.07841 | -59.64501 | 2024-12-20 05:08:00 | NOAA-21 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 4b93954a-d10d-32b4-9ccd-f6dd2d6660ad | -19.12546 | -53.45551 | 2024-12-20 05:08:00 | NOAA-21 | CAMAPUÃ | MATO GROSSO DO SUL | Brasil | 5002605 | 50 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 0c1e69f7-1504-36f4-98ec-c3c4300e1660 | -10.19423 | -64.24848 | 2024-12-20 05:08:00 | NOAA-21 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 41b6168c-cfed-3717-b928-b7e5b9e0532e | -18.73859 | -56.56656 | 2024-12-20 05:08:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 0.6 |
| 9a7f4c39-078a-3819-9865-38501e23fbd5 | -12.18586 | -64.06497 | 2024-12-20 05:08:00 | NOAA-21 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| ccf44813-ac04-39d5-89b4-8150cb68050a | -12.19642 | -54.31865 | 2024-12-20 05:08:00 | NOAA-21 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 608819ed-4917-37d9-bb9a-c1b5071d405b | -3.232 | -46.8056 | 2024-12-20 05:10:00 | GOES-16 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 66.9 |
| d14afaf9-7b6c-304a-a8f4-cf2871ef58d8 | -3.2321 | -46.7836 | 2024-12-20 05:10:00 | GOES-16 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 57.5 |
| ff23a317-3755-3287-b578-a1764b1dcf18 | -20.97302 | -49.75887 | 2024-12-20 05:10:00 | NOAA-21 | JOSÉ BONIFÁCIO | SÃO PAULO | Brasil | 3525706 | 35 | 33 | nan | nan | nan | Mata Atlântica | 4.3 |
| ee23c48c-d594-3c04-9050-94b32739381c | -20.97449 | -49.76091 | 2024-12-20 05:10:00 | NOAA-21 | JOSÉ BONIFÁCIO | SÃO PAULO | Brasil | 3525706 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.2 |
| 4403af7f-5886-3147-9e3a-c31fdbf4d9d9 | -20.97269 | -49.7624 | 2024-12-20 05:10:00 | NOAA-21 | JOSÉ BONIFÁCIO | SÃO PAULO | Brasil | 3525706 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.2 |
| e0ec1d30-c5b4-37b5-a983-7fb811d3027c | -20.99163 | -49.01907 | 2024-12-20 05:10:00 | NOAA-21 | TABAPUÃ | SÃO PAULO | Brasil | 3552601 | 35 | 33 | nan | nan | nan | Mata Atlântica | 11.6 |
| 64edc7bc-ae15-39c3-959e-3539d38b90e6 | -20.99126 | -49.02305 | 2024-12-20 05:10:00 | NOAA-21 | TABAPUÃ | SÃO PAULO | Brasil | 3552601 | 35 | 33 | nan | nan | nan | Mata Atlântica | 11.6 |
| 20f09077-526b-3177-930c-34ca7f5dd4c7 | -20.96916 | -49.76027 | 2024-12-20 05:10:00 | NOAA-21 | JOSÉ BONIFÁCIO | SÃO PAULO | Brasil | 3525706 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| 90c1dbdd-daac-3f1c-a482-d8eb746a97a6 | -3.232 | -46.8056 | 2024-12-20 05:20:00 | GOES-16 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 59.8 |
| 1068a33c-0809-3c8b-9fc1-f1359472488b | -3.2321 | -46.7836 | 2024-12-20 05:20:00 | GOES-16 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 57.3 |
| bbd011d0-0bdd-3fcd-8a8a-0784f5c89061 | -1.28246 | -53.18761 | 2024-12-20 05:29:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 90938128-dfcd-3d71-849b-f9343ed9d11d | -2.50894 | -48.05838 | 2024-12-20 05:29:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 2e2155b4-83a1-3df5-a565-ff6628368f30 | -1.68245 | -53.27659 | 2024-12-20 05:29:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 69187982-ed7e-35fe-bfbc-2937c91eac88 | -2.90492 | -54.49668 | 2024-12-20 05:29:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 02d1d940-d5d0-3d5a-b192-4f13339fd7dc | -1.28099 | -53.1864 | 2024-12-20 05:29:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| a994477e-132a-3377-a2d4-8e1b1f90ffe3 | -1.31014 | -53.52666 | 2024-12-20 05:29:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |


[Clique aqui para ver as próximas entradas](README11.md)
