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

## Dados Diários - Página 4

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 0e154e91-1aa3-30a1-b174-23f3153b957c | -9.40168 | -48.41941 | 2025-06-13 00:58:00 | TERRA_M-M | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 13.9 |
| f8314000-6ada-3349-a75e-deb0fe687023 | -13.89367 | -54.63255 | 2025-06-13 00:58:00 | TERRA_M-M | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 92.7 |
| b4d3de54-b1b8-3ee9-9389-b205c15c7e88 | -11.74292 | -54.7224 | 2025-06-13 00:58:00 | TERRA_M-M | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 7.8 |
| 77d81f08-35bd-33b4-9a12-bc3991e67c57 | -11.81533 | -54.50333 | 2025-06-13 00:58:00 | TERRA_M-M | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 48.4 |
| dfa22b54-87b4-3330-a869-146512856f19 | -11.91883 | -57.46479 | 2025-06-13 00:58:00 | TERRA_M-M | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 32.6 |
| c0464560-b118-3dfb-8809-fa9fe2bcd824 | -12.43419 | -54.86673 | 2025-06-13 00:58:00 | TERRA_M-M | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 6.9 |
| 5ec4eef3-2d16-38a6-a1ae-7445b8ed54ca | -12.19763 | -54.26973 | 2025-06-13 00:58:00 | TERRA_M-M | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 7.0 |
| df543e5b-9312-32eb-a597-23b583ed3679 | -10.69826 | -49.48867 | 2025-06-13 00:58:00 | TERRA_M-M | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 28.6 |
| e489591e-0c1a-3f82-9bfe-496fa33fe1a7 | -10.9167 | -56.8336 | 2025-06-13 01:00:00 | GOES-19 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 41.1 |
| 8229d07c-ddb2-33e3-a5e9-a3f99a5a419e | -11.5649 | -54.559 | 2025-06-13 01:00:00 | GOES-19 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 52.8 |
| b9076df5-7e1b-33f0-9ca3-e7e3b56d1cee | -9.4114 | -57.5529 | 2025-06-13 01:00:00 | GOES-19 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 65.7 |
| 154b2582-3841-30f4-b8eb-36d86516510c | -10.6492 | -49.4267 | 2025-06-13 01:00:00 | GOES-19 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 146.7 |
| 839d3aaf-ac99-3eaa-8084-9182ce9c10d0 | -7.2214 | -43.1153 | 2025-06-13 01:00:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 90.0 |
| 10bfc7f4-7d44-32bc-88d5-1416ed938ac3 | -10.7048 | -49.507 | 2025-06-13 01:00:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 51.9 |
| 0a23fe4b-d0aa-3483-8ca5-094ad62d2373 | -11.5836 | -54.5777 | 2025-06-13 01:00:00 | GOES-19 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 50.1 |
| 3a4bfcf2-56a6-37b3-b062-4585216675c1 | -10.7051 | -49.4853 | 2025-06-13 01:00:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 49.4 |
| c8878efa-9c48-32d5-ad2e-1c109c70e0c2 | -11.5647 | -54.5794 | 2025-06-13 01:00:00 | GOES-19 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 70.8 |
| 199a877f-2a97-3c55-a25d-9b8b2eac1387 | -13.9059 | -54.6291 | 2025-06-13 01:00:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 98.1 |
| 81881180-d59e-3ee1-a6ae-35055454705a | -13.887 | -54.6106 | 2025-06-13 01:00:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 44.2 |
| 3172be59-47ac-39cd-a482-858b538dbc21 | -10.6302 | -49.4288 | 2025-06-13 01:00:00 | GOES-19 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 55.3 |
| f778a1bd-1b78-3c63-bb3c-716d5d0f7985 | -7.4575 | -45.5116 | 2025-06-13 01:00:00 | GOES-19 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 54.6 |
| 962c2427-6b52-3352-baec-eda9165ccb2d | -10.9355 | -56.8322 | 2025-06-13 01:00:00 | GOES-19 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 53.2 |
| d1939871-ef76-3b05-b55e-cdc7235d60e3 | -13.9062 | -54.6084 | 2025-06-13 01:00:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 53.8 |
| e7a4b8e7-bcb3-31f4-a5f8-4d0d795d5c5a | -7.2403 | -43.1134 | 2025-06-13 01:00:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 93.0 |
| 924f13b0-8feb-3974-a62f-e7535c424ab0 | -13.8867 | -54.6312 | 2025-06-13 01:00:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 88.9 |
| 884507ce-4e5e-371d-9a08-a1716d7d2e32 | -7.24568 | -43.10301 | 2025-06-13 01:00:00 | TERRA_M-M | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 78.0 |
| 9cac849f-32c0-3742-be35-ba86cc92cad9 | -7.21089 | -43.10892 | 2025-06-13 01:00:00 | TERRA_M-M | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 76.6 |
| 46ad3747-b9af-33b2-ab2e-72a77a162c79 | -9.40028 | -57.55423 | 2025-06-13 01:00:00 | TERRA_M-M | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 67.4 |
| 0940db94-97ad-374f-b043-8dab842c035a | -9.4091 | -57.55887 | 2025-06-13 01:00:00 | TERRA_M-M | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 34.6 |
| 56b21b46-fa56-3a35-b51f-744c427e972c | -9.39636 | -57.54632 | 2025-06-13 01:00:00 | TERRA_M-M | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 10.4 |
| cd357d65-ad69-30c0-b1c5-ef481cc2799f | -9.39818 | -57.56026 | 2025-06-13 01:00:00 | TERRA_M-M | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 10.9 |
| 4ed3d792-7ecc-3554-b959-029fc9895ab8 | -7.2465 | -43.09775 | 2025-06-13 01:00:00 | TERRA_M-M | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 61.4 |
| 783b8ce1-0065-3c33-bc09-ad8907de2ca9 | -9.40726 | -57.54488 | 2025-06-13 01:00:00 | TERRA_M-M | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 47.8 |
| 082ebb02-f0cb-3a6e-a9d7-65ef4fba078a | -7.21001 | -43.11591 | 2025-06-13 01:00:00 | TERRA_M-M | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 81.1 |
| 9f95c8b1-9dc0-3f26-b917-b9a917ecb65d | -9.88218 | -61.40323 | 2025-06-13 01:00:00 | TERRA_M-M | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 22.1 |
| e1e7f1c6-71cf-3b12-91e6-7252ab68488a | -9.41119 | -57.55274 | 2025-06-13 01:00:00 | TERRA_M-M | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 34.9 |
| 7c8fe73d-b7b5-3d6c-8ed6-3349e5644144 | -12.2512 | -58.499599 | 2025-06-13 01:09:00 | METOP-B | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 7184d25f-e1a3-30dd-88cf-1d57cb19ba66 | -10.4156 | -49.4911 | 2025-06-13 01:09:00 | METOP-B | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 638b3676-e124-3356-b687-1a2fe2329733 | -10.7094 | -56.869598 | 2025-06-13 01:09:00 | METOP-B | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 666b2926-e517-3b70-a9ec-2c6fb5046cec | -13.6824 | -54.6534 | 2025-06-13 01:09:00 | METOP-B | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 84def516-0deb-31b5-88e9-f542d3e9fd4b | -9.1773 | -57.5891 | 2025-06-13 01:09:00 | METOP-B | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| ec864468-d581-3b25-9323-f036ee319533 | -12.8635 | -52.327301 | 2025-06-13 01:09:00 | METOP-B | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| f3d79bdd-5140-3e4d-9d73-3f3136ba5ff7 | -13.976 | -57.440201 | 2025-06-13 01:09:00 | METOP-B | DIAMANTINO | MATO GROSSO | Brasil | 5103502 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 1c16532e-1dd2-3b66-b580-13f483ba20d3 | -10.9134 | -53.992199 | 2025-06-13 01:09:00 | METOP-B | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 7a67fce7-df35-327d-8d58-8cdab3e2dc0e | -10.6387 | -54.338799 | 2025-06-13 01:09:00 | METOP-B | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 84ce4b64-5d58-32cc-8fb1-bdcfee66ea41 | -10.0538 | -60.567699 | 2025-06-13 01:09:00 | METOP-B | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| f05f7dbe-cc50-3e4e-961b-dd84b7e406e3 | -8.4636 | -64.9133 | 2025-06-13 01:09:00 | METOP-B | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 2ad89bf6-8170-351e-95bd-4b7fd88d700d | -10.4804 | -49.541599 | 2025-06-13 01:09:00 | METOP-B | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| acdcae64-c28f-344e-ad63-a22af21edc9b | -10.4165 | -49.456299 | 2025-06-13 01:09:00 | METOP-B | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| ec02d7b7-0791-341f-8045-6e9469ff52d9 | -13.6759 | -54.668701 | 2025-06-13 01:09:00 | METOP-B | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 110ae977-0cd1-30fc-b61f-ae1160d98e13 | -11.3481 | -54.618099 | 2025-06-13 01:09:00 | METOP-B | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 548064ab-a14e-33aa-befc-bbfbb0983bb3 | -10.7021 | -56.882301 | 2025-06-13 01:09:00 | METOP-B | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 30715731-12cf-3642-a35f-6d23385a1982 | -10.1449 | -57.273102 | 2025-06-13 01:09:00 | METOP-B | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| f25153e0-cb65-36e7-91ac-5a1e3952d7ce | -14.4532 | -53.401001 | 2025-06-13 01:09:00 | METOP-B | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| cd5f312f-1f52-321a-a3a6-e2e8536bc75a | -13.9877 | -57.446499 | 2025-06-13 01:09:00 | METOP-B | DIAMANTINO | MATO GROSSO | Brasil | 5103502 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 2f17344f-67a1-3b67-9f33-5599c80da4b5 | -9.0045 | -62.502998 | 2025-06-13 01:09:00 | METOP-B | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 8a1b30f7-b81e-3c39-a682-e1a1df206daa | -10.6424 | -54.353699 | 2025-06-13 01:09:00 | METOP-B | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 64dab3d0-ffdb-34c3-b500-3badfea90ceb | -9.0029 | -62.496101 | 2025-06-13 01:09:00 | METOP-B | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| dc506aec-a9e4-38fe-9c2d-93ae503090a3 | -10.6972 | -56.861801 | 2025-06-13 01:09:00 | METOP-B | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 7dc55f94-3a4f-3ec8-88bc-757f84fa96f9 | -13.9836 | -57.429001 | 2025-06-13 01:09:00 | METOP-B | DIAMANTINO | MATO GROSSO | Brasil | 5103502 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 398f15ab-585a-3525-a0e2-1b2363efad4f | -8.4619 | -64.905403 | 2025-06-13 01:09:00 | METOP-B | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 9a08d5ba-f1bc-387c-9bb8-c09ca2753d49 | -13.9857 | -57.437801 | 2025-06-13 01:09:00 | METOP-B | DIAMANTINO | MATO GROSSO | Brasil | 5103502 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| b4db3643-84d4-3d75-9689-d7f1a13f2db9 | -11.335 | -54.606602 | 2025-06-13 01:09:00 | METOP-B | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| f7fe78af-2244-37e2-a32e-cba795883add | -9.6616 | -61.4333 | 2025-06-13 01:09:00 | METOP-B | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| c4d9a8b0-6879-31d5-892d-3ed25b4b23c8 | -9.66 | -61.426399 | 2025-06-13 01:09:00 | METOP-B | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 375a8465-dbdb-3b43-90ae-92ef02a35807 | -11.6959 | -57.4991 | 2025-06-13 01:09:00 | METOP-B | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 6a7e9359-6286-3649-9161-131d1df66987 | -10.1425 | -57.263302 | 2025-06-13 01:09:00 | METOP-B | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| d49606b4-4b7d-32b0-b8c8-a196f233bb75 | -10.4708 | -49.544201 | 2025-06-13 01:09:00 | METOP-B | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| e16c7daf-36b7-3ccf-9e1c-1328ce4d9900 | -12.2531 | -58.507702 | 2025-06-13 01:09:00 | METOP-B | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| e792e8ab-4b48-3653-a894-be7085ed6694 | -13.7538 | -54.483299 | 2025-06-13 01:09:00 | METOP-B | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| ebd4bc72-7497-3fd9-800b-e3d05f9ccec3 | -12.8732 | -52.324699 | 2025-06-13 01:09:00 | METOP-B | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 04379d49-904d-30df-b0dc-e39b00052cf9 | -12.3034 | -57.272301 | 2025-06-13 01:09:00 | METOP-B | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 34148f66-0d3f-393d-a617-3eb60b79e43a | -13.6856 | -54.666199 | 2025-06-13 01:09:00 | METOP-B | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 0ff50328-7271-300c-b463-c8b3282c9b70 | -10.7119 | -56.879902 | 2025-06-13 01:09:00 | METOP-B | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| f0fb060b-32dc-3fc2-8282-9c09fd9e6078 | -10.9037 | -53.994701 | 2025-06-13 01:09:00 | METOP-B | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 07fe8ec2-521f-36f7-bc14-4693fe5d3d9e | -11.3384 | -54.620499 | 2025-06-13 01:09:00 | METOP-B | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 6b4f24db-35bb-3b28-a518-0ee94aa14fc9 | -9.1894 | -57.5965 | 2025-06-13 01:09:00 | METOP-B | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| f83f1608-8ce4-3625-bf59-fce5ad979214 | -12.295 | -58.3773 | 2025-06-13 01:09:00 | METOP-B | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 0ae43059-a7ee-3ac6-af13-c6929597e440 | -14.457 | -53.416 | 2025-06-13 01:09:00 | METOP-B | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| cb6f05e5-a25c-381c-9c95-d2e47300b1ec | -13.6727 | -54.655998 | 2025-06-13 01:09:00 | METOP-B | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 04bbaf2c-d8a9-3709-8733-5a629da12d2f | -13.9955 | -57.435398 | 2025-06-13 01:09:00 | METOP-B | DIAMANTINO | MATO GROSSO | Brasil | 5103502 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| e52a1ccc-7eb7-34c5-b957-f7c3e76a78cc | -9.175 | -57.579399 | 2025-06-13 01:09:00 | METOP-B | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| d336c8c0-e404-30c4-ace1-cbb0ec587d0d | -9.1848 | -57.577099 | 2025-06-13 01:09:00 | METOP-B | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 50bf510a-0251-3e42-af24-9bbbb6d6fc4f | -11.5971 | -54.539299 | 2025-06-13 01:09:00 | METOP-B | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 5fd46229-9231-3f7a-b497-30a40cc43f4c | -8.9619 | -61.896801 | 2025-06-13 01:09:00 | METOP-B | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 1b504bb5-34fd-36ac-8a58-ea769d4ec796 | -11.5874 | -54.541801 | 2025-06-13 01:09:00 | METOP-B | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| ccfd1178-ad7e-3a95-bda1-f928a4183f9c | -11.6981 | -57.508301 | 2025-06-13 01:09:00 | METOP-B | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| a4a18c2a-adb9-390c-ba36-ea48b6a32303 | -10.8998 | -53.979 | 2025-06-13 01:09:00 | METOP-B | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 78efa9ec-c37a-39cc-b86e-2e6a7ac74b5f | -10.4347 | -49.485802 | 2025-06-13 01:09:00 | METOP-B | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 3147192b-7db8-3d9c-890a-16527dc8c99c | -13.6791 | -54.681499 | 2025-06-13 01:09:00 | METOP-B | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 6dd6a08f-99f7-346f-b1a4-a1b8cb56211f | -13.6694 | -54.683998 | 2025-06-13 01:09:00 | METOP-B | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 46029d9a-6112-3a76-95a2-f9f61232c187 | -10.6996 | -56.872002 | 2025-06-13 01:09:00 | METOP-B | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 4a137394-470d-3808-9b1f-cd4433b92f3f | -10.1461 | -57.5392 | 2025-06-13 01:09:00 | METOP-B | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| c3837979-2406-3e7f-89e7-eac4adc89091 | -10.4251 | -49.4884 | 2025-06-13 01:09:00 | METOP-B | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| fdefd3f2-f669-38e4-8ae6-d674f369eac6 | -12.2936 | -57.2747 | 2025-06-13 01:09:00 | METOP-B | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| b43eec0b-5fbf-31e5-9d7c-c7c78be90eec | -10.0555 | -60.574902 | 2025-06-13 01:09:00 | METOP-B | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 3598af6f-acdd-36eb-88fc-bfffdac6e747 | -8.4602 | -64.897499 | 2025-06-13 01:09:00 | METOP-B | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 28542b6b-7e41-3f6d-8c99-d341ba4f12f0 | -9.7446 | -65.0009 | 2025-06-13 01:09:00 | METOP-B | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 4e7105d0-c7fe-3c9f-9f5d-fecf788e6401 | -9.1871 | -57.5868 | 2025-06-13 01:09:00 | METOP-B | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| cc377183-8607-3048-8c6b-29f07ab963bb | -13.6662 | -54.6712 | 2025-06-13 01:09:00 | METOP-B | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | nan |


[Clique aqui para ver as próximas entradas](README5.md)
