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

## Dados Diários - Página 141

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 1b88566d-b4ab-38a8-bf91-cff37f987a73 | -2.8961 | -58.3018 | 2026-09-20 15:50:00 | GOES-19 | SILVES | AMAZONAS | Brasil | 1304005 | 13 | 33 | nan | nan | nan | Amazônia | 59.4 |
| 247bc957-bd40-3e08-9883-78bcb11a92a2 | -3.1357 | -57.697 | 2026-09-20 15:50:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 44.1 |
| beafdf0c-e1df-3441-8fe5-5e4f065e6a1e | -9.2676 | -48.2472 | 2026-09-20 15:50:00 | GOES-19 | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | 86.3 |
| 32814c49-0890-392a-a691-930836bd1c53 | -6.7464 | -59.4223 | 2026-09-20 15:50:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 45.2 |
| 3e8d1977-7f5c-3282-95aa-1492cdd7a277 | -2.9326 | -58.3397 | 2026-09-20 15:50:00 | GOES-19 | SILVES | AMAZONAS | Brasil | 1304005 | 13 | 33 | nan | nan | nan | Amazônia | 82.4 |
| 3d248c0d-d5ab-39e5-b584-bbdf65cc555d | -10.279 | -50.2391 | 2026-09-20 15:50:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 100.6 |
| ea7a792a-bc0a-347e-bc6c-806937764667 | -2.9997 | -60.8047 | 2026-09-20 15:50:00 | GOES-19 | IRANDUBA | AMAZONAS | Brasil | 1301852 | 13 | 33 | nan | nan | nan | Amazônia | 158.0 |
| 519acf59-76fc-3c2f-9bb3-d6e4b831c04c | -3.6076 | -59.0769 | 2026-09-20 15:50:00 | GOES-19 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 82.2 |
| 08ebd5f4-90b9-3be4-b061-5162db47e29b | -3.3494 | -59.8097 | 2026-09-20 15:50:00 | GOES-19 | CAREIRO | AMAZONAS | Brasil | 1301100 | 13 | 33 | nan | nan | nan | Amazônia | 73.3 |
| 0ffd678b-0709-3021-9d1d-b19136a00318 | -3.3359 | -58.1191 | 2026-09-20 15:50:00 | GOES-19 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 56.5 |
| 3b358314-f33f-3ef1-a9ce-b0c0aca8fa21 | -3.5894 | -59.0581 | 2026-09-20 15:50:00 | GOES-19 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 81.0 |
| f732db7b-73d3-3823-b8ea-4219a0673843 | -3.7347 | -59.4002 | 2026-09-20 15:50:00 | GOES-19 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 87.7 |
| 36306ab0-4056-3be6-981f-34a752fb78d7 | -3.6077 | -59.0577 | 2026-09-20 15:50:00 | GOES-19 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 74.8 |
| a0f4e2c7-1fb0-3869-97eb-0393b6ad048f | -11.1225 | -49.4601 | 2026-09-20 15:50:00 | GOES-19 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 102.7 |
| 399b1500-dd80-35f4-b958-4dfd22c8bd50 | -9.4137 | -50.1317 | 2026-09-20 15:50:00 | GOES-19 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 84.6 |
| a5df1216-c90d-34c7-854e-a041c2e0b787 | -3.3138 | -59.4472 | 2026-09-20 15:50:00 | GOES-19 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 107.1 |
| d2fcff14-fc28-3d64-96d0-b54f3dd18ee9 | -1.7316 | -54.9518 | 2026-09-20 15:50:00 | GOES-19 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 67.9 |
| e8f4800c-6aa0-3b33-b0a6-5383231930ba | -2.8974 | -57.7987 | 2026-09-20 15:50:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 114.3 |
| 812e810d-8779-36fc-9f2e-1b8e42994612 | -3.6398 | -60.5656 | 2026-09-20 15:50:00 | GOES-19 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 57.9 |
| 9963cf50-3c5f-3b71-a800-0e27ab7183b7 | -8.4296 | -54.7262 | 2026-09-20 15:50:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 65.7 |
| f684a37b-c279-345c-aed4-7eada6bb291d | -8.1688 | -54.7432 | 2026-09-20 15:50:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 132.4 |
| 53788625-b8ab-31fa-b8fe-46539930ab62 | -10.8282 | -50.1601 | 2026-09-20 16:00:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 219.7 |
| f2fa0f19-a0d1-39b7-a23b-fde185602ef4 | -3.6763 | -60.6029 | 2026-09-20 16:00:00 | GOES-19 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 64.7 |
| 8850a44d-985e-3c6b-9600-b87ff6f43fe9 | -10.8656 | -50.1989 | 2026-09-20 16:00:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 117.9 |
| 79d961de-8ed6-37d6-af0c-98f6f8588a5c | -2.9326 | -58.3397 | 2026-09-20 16:00:00 | GOES-19 | SILVES | AMAZONAS | Brasil | 1304005 | 13 | 33 | nan | nan | nan | Amazônia | 94.9 |
| dc3a9172-b490-36c4-9205-cfc09dec2b68 | -6.0928 | -57.6262 | 2026-09-20 16:00:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 54.5 |
| da8f36d6-6d41-355e-b759-6eb9154b8e8f | -9.8397 | -46.4361 | 2026-09-20 16:00:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 108.1 |
| 5129dee1-0be2-3b33-9f8b-907d82ff7983 | -3.1079 | -61.408 | 2026-09-20 16:00:00 | GOES-19 | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 60.7 |
| 4c5549cd-e8ee-3205-b2cb-93a2104a327a | -9.6668 | -54.3129 | 2026-09-20 16:00:00 | GOES-19 | GUARANTÃ DO NORTE | MATO GROSSO | Brasil | 5104104 | 51 | 33 | nan | nan | nan | Amazônia | 128.1 |
| 797ffeb3-d3ea-3d6d-ad79-a92aed028ae0 | -3.6449 | -58.8647 | 2026-09-20 16:00:00 | GOES-19 | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | 60.7 |
| 0194bfe5-baa5-3b3f-8f81-80183b8ebb08 | -3.2955 | -59.4476 | 2026-09-20 16:00:00 | GOES-19 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 95.9 |
| b94c421c-f3e2-3d58-bb41-a4a8c64fd168 | -10.8279 | -50.1815 | 2026-09-20 16:00:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 158.8 |
| e7224694-efb5-301b-847c-0d2eba0db87f | -2.9143 | -58.3401 | 2026-09-20 16:00:00 | GOES-19 | SILVES | AMAZONAS | Brasil | 1304005 | 13 | 33 | nan | nan | nan | Amazônia | 162.9 |
| 7adefefd-1209-3995-bcdb-c3409830a9f9 | -1.1345 | -49.2123 | 2026-09-20 16:00:00 | GOES-19 | MUANÁ | PARÁ | Brasil | 1504901 | 15 | 33 | nan | nan | nan | Amazônia | 61.1 |
| 0d7d6443-e286-352b-8185-17a1d2d1f035 | -10.279 | -50.2391 | 2026-09-20 16:00:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 95.8 |
| 2326ba23-c31f-3561-a3f2-68642c78aab9 | -10.7466 | -50.5959 | 2026-09-20 16:00:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 82.5 |
| e06c6880-46b8-3b98-839c-b8e65dabf2bb | -3.6762 | -60.6219 | 2026-09-20 16:00:00 | GOES-19 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 119.1 |
| a4911bbd-3578-3771-b503-0b98fd54e8db | -10.1145 | -48.4205 | 2026-09-20 16:00:00 | GOES-19 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 61.2 |
| 690c9199-a346-3b03-8799-330c2530afd0 | -6.0927 | -57.6457 | 2026-09-20 16:00:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 41.1 |
| 1760d018-976d-3269-bd0e-1d1a91cde03c | -3.5894 | -59.0581 | 2026-09-20 16:00:00 | GOES-19 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 98.5 |
| a25d1f1f-c284-3d44-bbc9-1a341fa0955a | -3.4963 | -59.5967 | 2026-09-20 16:00:00 | GOES-19 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 40.8 |
| 43ffa366-5e29-3b20-99cf-9a3bdfeb6d1f | -10.2787 | -50.2605 | 2026-09-20 16:00:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 108.8 |
| e7d623b1-867a-3c33-b7d9-dcaff9f82c71 | -2.8975 | -57.7793 | 2026-09-20 16:00:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 50.9 |
| 049770ce-92c9-31f7-bd68-20bed1dbea05 | -10.1791 | -69.0659 | 2026-09-20 16:00:00 | GOES-19 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 60.6 |
| 3e2aa1bc-7615-38b1-bde0-5cf200033d0c | -3.4003 | -61.2898 | 2026-09-20 16:00:00 | GOES-19 | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 49.5 |
| e7b1fa0d-d9aa-3d85-beb8-acc49cf21c9f | -3.3136 | -59.5238 | 2026-09-20 16:00:00 | GOES-19 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 51.1 |
| 2d461555-40da-30f1-b2b5-34b50fafffdd | -3.9902 | -41.2759 | 2026-09-20 16:00:00 | GOES-19 | SÃO JOÃO DA FRONTEIRA | PIAUÍ | Brasil | 2209872 | 22 | 33 | nan | nan | nan | Caatinga | 143.5 |
| a3a807ce-10a2-35e6-9445-d00a3228817f | -10.1598 | -69.3068 | 2026-09-20 16:00:00 | GOES-19 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 37.8 |
| 1e03391e-b723-395f-a263-b9ae958429f8 | -10.2598 | -50.2624 | 2026-09-20 16:00:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 87.5 |
| 9214c3e5-e1f6-347e-bc83-d210c91fc5d2 | -9.8136 | -48.3218 | 2026-09-20 16:00:00 | GOES-19 | LAJEADO | TOCANTINS | Brasil | 1712009 | 17 | 33 | nan | nan | nan | Cerrado | 72.6 |
| cc654a72-8c86-3886-8344-078fd664baa4 | -6.4402 | -58.138 | 2026-09-20 16:00:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 51.4 |
| eee09a9a-e1a3-3d00-95bf-34134a5a6c65 | -11.0614 | -49.7477 | 2026-09-20 16:00:00 | GOES-19 | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 149.1 |
| 44c78f87-4ff2-3fb6-81c4-2d1125259595 | -8.1688 | -54.7432 | 2026-09-20 16:00:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 131.6 |
| bbb5c69a-42f9-3dce-8368-38c583e6f7de | -6.7483 | -59.0943 | 2026-09-20 16:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 41.9 |
| b7c8427b-fb93-31f0-a65d-f09bd507f2ea | -10.809 | -50.1836 | 2026-09-20 16:00:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 126.6 |
| dd3609b9-5a96-3fe6-88a3-a37972ec5ebd | -6.3014 | -59.9579 | 2026-09-20 16:00:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 94.5 |
| 07e91b4a-a6c3-3696-902e-fc5845da701f | -11.0259 | -48.2944 | 2026-09-20 16:00:00 | GOES-19 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 86.3 |
| e6bb3fab-618e-311c-a94c-5f557e414a04 | -11.1222 | -49.4818 | 2026-09-20 16:00:00 | GOES-19 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 98.9 |
| d4a8c30c-f57e-35a7-a6aa-f02883f005e6 | -3.7347 | -59.4194 | 2026-09-20 16:00:00 | GOES-19 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 54.8 |
| 2d79ad05-6983-3a7c-ae6a-8b1530756563 | -3.1467 | -60.4228 | 2026-09-20 16:00:00 | GOES-19 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 48.5 |
| a4b034a4-89b5-3ca2-b6e7-d075217a6579 | -10.6705 | -50.6251 | 2026-09-20 16:00:00 | GOES-19 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 96.2 |
| 60c667a5-ea14-36a6-9b36-896d4c7d0433 | -2.9997 | -60.8047 | 2026-09-20 16:00:00 | GOES-19 | IRANDUBA | AMAZONAS | Brasil | 1301852 | 13 | 33 | nan | nan | nan | Amazônia | 76.1 |
| e502633f-4517-3685-93d8-e04ef5049f83 | -8.4296 | -54.7262 | 2026-09-20 16:00:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 67.0 |
| 45d8ec00-f5bc-384a-a1e6-68c9961e6291 | -3.3321 | -59.4469 | 2026-09-20 16:00:00 | GOES-19 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 102.9 |
| 1bffdfc4-179e-3363-a7bb-514b664110b3 | -3.5893 | -59.0773 | 2026-09-20 16:00:00 | GOES-19 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 74.9 |
| 1615fc0f-63c5-374c-b57a-03c283387fb5 | -3.2189 | -60.8011 | 2026-09-20 16:00:00 | GOES-19 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 56.1 |
| d9d31bb5-b8ca-384e-964c-7d4703f5d972 | -6.2832 | -59.9202 | 2026-09-20 16:00:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 57.1 |
| 6a9a25fc-f0af-38f0-85ae-8ed9d89c289e | -1.1161 | -49.2125 | 2026-09-20 16:00:00 | GOES-19 | PONTA DE PEDRAS | PARÁ | Brasil | 1505700 | 15 | 33 | nan | nan | nan | Amazônia | 58.4 |
| fe70a098-c34d-39ce-9ccd-503b3a8ca20c | -6.7464 | -59.4223 | 2026-09-20 16:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 56.6 |
| 980bcce3-5edd-38f0-8685-e6e326bb23f9 | 2.2187 | -50.8977 | 2026-09-20 16:00:00 | GOES-19 | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 80.7 |
| 60312582-c291-3a73-a4df-cf2b7f4a410a | -3.6076 | -59.0769 | 2026-09-20 16:00:00 | GOES-19 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 64.9 |
| 7c6d40d3-2a95-38b1-9d63-5427bf626da2 | 2.1267 | -50.858 | 2026-09-20 16:00:00 | GOES-19 | AMAPÁ | AMAPÁ | Brasil | 1600105 | 16 | 33 | nan | nan | nan | Amazônia | 64.5 |
| 51d307da-0329-32a4-89e0-eb3a480a4c07 | -3.5319 | -59.9397 | 2026-09-20 16:00:00 | GOES-19 | CAREIRO | AMAZONAS | Brasil | 1301100 | 13 | 33 | nan | nan | nan | Amazônia | 49.6 |
| 10e36568-b289-33f2-9750-f5fb515c2474 | -10.6516 | -50.6271 | 2026-09-20 16:00:00 | GOES-19 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 287.1 |
| 7609ef54-24e8-36dd-b9e5-8fc4d6a2f7fb | -2.8961 | -58.3018 | 2026-09-20 16:00:00 | GOES-19 | SILVES | AMAZONAS | Brasil | 1304005 | 13 | 33 | nan | nan | nan | Amazônia | 48.2 |
| c4336dab-1cf7-3fe9-a337-f8bce9f02acf | -3.2955 | -59.4284 | 2026-09-20 16:00:00 | GOES-19 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 62.3 |
| 8afd4761-46a2-3dc4-a4bb-fe0a5a69d609 | -10.8469 | -50.1795 | 2026-09-20 16:00:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 264.4 |
| 853699c1-36ef-3daf-9cff-6dd9bfe813f9 | -6.0925 | -57.6847 | 2026-09-20 16:00:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 69.1 |
| 3c0e3ea4-2e9f-31a9-837a-992a0624d97b | -11.0048 | -49.7325 | 2026-09-20 16:00:00 | GOES-19 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 104.5 |
| 99b38be4-6ab0-39af-bb83-d602f1d07dd0 | -5.7431 | -57.5814 | 2026-09-20 16:00:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 70.5 |
| 28c33fd5-cba3-3b62-a2ad-aa64d0ee6745 | -8.1686 | -54.7634 | 2026-09-20 16:00:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 339.3 |
| 494450a1-5c84-3429-8788-532ac48529c3 | -11.4537 | -45.3892 | 2026-09-20 16:00:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 188.4 |
| f5eb6fef-7d4e-3cc0-987d-3aed14d26d35 | 1.1503 | -50.998 | 2026-09-20 16:00:00 | GOES-19 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 84.0 |
| 9a829433-91ec-3b21-8298-a1720a84c601 | -10.8093 | -50.1621 | 2026-09-20 16:00:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 172.8 |
| abd04608-79bb-3e92-ac6f-9ee10c12c588 | -9.0353 | -48.7704 | 2026-09-20 16:00:00 | GOES-19 | GOIANORTE | TOCANTINS | Brasil | 1708304 | 17 | 33 | nan | nan | nan | Amazônia | 70.0 |
| 6a9432ea-daaa-30cd-8575-d35898612d26 | -10.809 | -50.1836 | 2026-09-20 16:10:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 123.0 |
| 165a9c62-84df-3c53-94a6-c10b7a2ada4a | -3.0352 | -61.277 | 2026-09-20 16:10:00 | GOES-19 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 73.7 |
| 54a4e6eb-1bc5-3e12-aaef-8fa402e26b11 | -10.1145 | -48.4205 | 2026-09-20 16:10:00 | GOES-19 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 66.8 |
| 9f8f8225-a65a-3c40-9479-ac24a2e90ef4 | -6.7863 | -58.8995 | 2026-09-20 16:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 60.0 |
| 0585756e-6334-3d0b-a23d-94e756e51e8e | -2.9997 | -60.8047 | 2026-09-20 16:10:00 | GOES-19 | IRANDUBA | AMAZONAS | Brasil | 1301852 | 13 | 33 | nan | nan | nan | Amazônia | 89.2 |
| bf870882-c4f1-3288-ae0a-8c0c735c34e5 | -10.2598 | -50.2624 | 2026-09-20 16:10:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 87.1 |
| 6fb8b69d-0302-323f-aacb-703a678d9b9e | -2.9143 | -58.3401 | 2026-09-20 16:10:00 | GOES-19 | SILVES | AMAZONAS | Brasil | 1304005 | 13 | 33 | nan | nan | nan | Amazônia | 154.0 |
| 3e383f7b-98d7-32b5-919b-581288499091 | -11.4545 | -45.3432 | 2026-09-20 16:10:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 288.4 |
| 85987180-c94b-3729-af18-bcffb50a36af | -6.7463 | -59.4416 | 2026-09-20 16:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 45.2 |
| 7997d8ba-d73f-3fc9-8c51-b6f0ac49b1e5 | -6.1291 | -57.7418 | 2026-09-20 16:10:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 55.7 |
| 3ed09dfa-fd32-3660-937a-7aa544a3f348 | -10.8279 | -50.1815 | 2026-09-20 16:10:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 138.0 |
| f09164c1-8342-37fc-a073-43a15a18fd92 | -3.6763 | -60.6029 | 2026-09-20 16:10:00 | GOES-19 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 153.8 |
| c7e01bec-a7d1-3efb-a7a5-5712216824a3 | -10.8093 | -50.1621 | 2026-09-20 16:10:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 172.8 |
| ab3acd9f-d536-3810-88f3-05ed9cc59687 | -6.1112 | -57.645 | 2026-09-20 16:10:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 36.6 |
| e1e86096-360e-36b0-8c24-ba1fb7210f19 | 2.2003 | -50.8773 | 2026-09-20 16:10:00 | GOES-19 | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 84.6 |


[Clique aqui para ver as próximas entradas](README142.md)
