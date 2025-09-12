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

## Dados Diários - Página 130

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 203bd049-1311-3d37-a3e0-ccf5fb92d358 | -10.679 | -48.6633 | 2025-09-12 13:20:00 | GOES-19 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 175.7 |
| dc538b3d-5fb8-3c5a-acbc-6d72a61dcf60 | -7.5641 | -44.4068 | 2025-09-12 13:20:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 124.4 |
| 9e592461-056c-31bd-95bd-00250f005db7 | -7.2374 | -55.0604 | 2025-09-12 13:20:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 61.7 |
| de1c7edc-c758-39cb-a747-3b953f538c67 | -10.6793 | -48.6415 | 2025-09-12 13:20:00 | GOES-19 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 102.1 |
| d1b65074-90d0-35e3-80c1-32521a6255f0 | -10.6983 | -48.6393 | 2025-09-12 13:20:00 | GOES-19 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 179.4 |
| c77cf05b-b838-36a0-bb6c-17c93bee3e1d | -14.4394 | -47.3206 | 2025-09-12 13:20:00 | GOES-19 | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 99.3 |
| cba2134e-36fc-3cc7-b917-1450cf147ad5 | -6.1703 | -41.0901 | 2025-09-12 13:20:00 | GOES-19 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 523.0 |
| 613130e1-e20c-3bb0-9f91-2d6ae9ef317c | -7.5455 | -44.3856 | 2025-09-12 13:20:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 96.8 |
| c4e32b7b-24a5-3ac2-b7ec-61375a808d71 | -10.7172 | -48.6371 | 2025-09-12 13:20:00 | GOES-19 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 80.2 |
| 25138c17-ed5a-33cf-8b46-517dd46dd154 | -9.7197 | -46.8972 | 2025-09-12 13:20:00 | GOES-19 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 73.6 |
| 63c6b936-a3a7-394e-8631-ce6ccf68ba56 | -9.673 | -47.5459 | 2025-09-12 13:20:00 | GOES-19 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 572.6 |
| 70b2bc40-2967-3622-bc4b-7798c64eed79 | -11.4402 | -48.5513 | 2025-09-12 13:20:00 | GOES-19 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 87.0 |
| a61ddb6e-06d4-3413-acf1-a6d2ab800f0b | -8.4893 | -47.2694 | 2025-09-12 13:20:00 | GOES-19 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 63.3 |
| f46496c6-ec03-3967-b15f-2f84d0beeea7 | -9.5324 | -54.6277 | 2025-09-12 13:20:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 67.8 |
| f412455e-1eba-396e-b61c-0fdb14691b62 | -9.6916 | -47.566 | 2025-09-12 13:20:00 | GOES-19 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 80.8 |
| 3f76765f-691c-347e-85b5-2ff1be20e4d0 | -14.4588 | -47.3174 | 2025-09-12 13:20:00 | GOES-19 | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 137.9 |
| ab9de330-dc32-350f-8b54-ffe880a1a991 | -9.0379 | -47.0597 | 2025-09-12 13:20:00 | GOES-19 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 72.2 |
| 2da3dfab-0cfc-3246-9aab-0558d6a9a824 | -8.1837 | -46.0965 | 2025-09-12 13:20:00 | GOES-19 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 90.8 |
| 24571716-1e9a-33a1-ae73-dee38aa5212e | -10.0943 | -47.1664 | 2025-09-12 13:20:00 | GOES-19 | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 145.0 |
| de18b24a-134a-3fb0-9776-2551e887e0a6 | -9.0373 | -47.1041 | 2025-09-12 13:20:00 | GOES-19 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 189.9 |
| 6a3bfb77-d1c6-3bbb-96ed-9d4013de1238 | -10.8972 | -45.58 | 2025-09-12 13:20:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 89.5 |
| 275d429c-d214-33d5-8bb6-856835a89d10 | -9.6727 | -47.568 | 2025-09-12 13:20:00 | GOES-19 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 196.9 |
| ba9d8f8c-c6ab-3973-ab1f-07b60f54e574 | -14.3937 | -52.9456 | 2025-09-12 13:20:00 | GOES-19 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 102.1 |
| f9add435-9f17-36ed-ae5c-576aea8d775c | -6.8369 | -45.6559 | 2025-09-12 13:20:00 | GOES-19 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 90.2 |
| 12659555-ce72-3e9c-b905-c36200edc822 | -9.0759 | -47.0335 | 2025-09-12 13:20:00 | GOES-19 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 75.3 |
| d7b3c174-d3da-3369-b721-9b3dc6ccfcc6 | -12.0852 | -47.5842 | 2025-09-12 13:20:00 | GOES-19 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 157.7 |
| eaa9d57f-2f48-30a8-aa2e-ce86deda5b5d | -8.956 | -46.1074 | 2025-09-12 13:20:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 175.4 |
| 3f84beef-a0e6-33b0-9545-bcbcf4c64300 | -8.9563 | -46.0849 | 2025-09-12 13:30:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 137.5 |
| 4aeaf96e-718f-3c52-8548-2574e9bd4655 | -11.5422 | -50.6161 | 2025-09-12 13:30:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 128.5 |
| 84f8f626-01e2-308a-ba1a-9f94f3b90f3d | -9.6727 | -47.568 | 2025-09-12 13:30:00 | GOES-19 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 119.8 |
| 62b122c4-0c36-3826-8974-884a285541b7 | -9.6733 | -47.5238 | 2025-09-12 13:30:00 | GOES-19 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 118.3 |
| fcbb165f-3bf9-3de0-8e39-1915270c216a | -16.5102 | -55.125 | 2025-09-12 13:30:00 | GOES-19 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 78.1 |
| 546a2ae5-0dd2-3fee-aa98-83e43e5a52bb | -6.8184 | -45.6349 | 2025-09-12 13:30:00 | GOES-19 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 110.9 |
| faaef1ec-006e-3dbe-8211-2dbad87c6c15 | -11.4398 | -48.5733 | 2025-09-12 13:30:00 | GOES-19 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 460.8 |
| 216c5ba7-0b0e-399c-8586-84f9ff217ef0 | -7.3212 | -49.6255 | 2025-09-12 13:30:00 | GOES-19 | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 76.4 |
| d4725811-5866-3cfd-8b59-18cfbfde8b1f | -9.6919 | -47.5438 | 2025-09-12 13:30:00 | GOES-19 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 277.6 |
| 8f58a26b-6355-3a9c-af76-bc19f5f64ed2 | -12.9101 | -54.7558 | 2025-09-12 13:30:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 110.7 |
| 3280870c-08b0-32f1-bf80-0c8361a2f989 | -11.1949 | -48.4277 | 2025-09-12 13:30:00 | GOES-19 | IPUEIRAS | TOCANTINS | Brasil | 1709807 | 17 | 33 | nan | nan | nan | Cerrado | 76.2 |
| 45335924-ceba-31c8-8399-14cb35d1d080 | -11.8761 | -47.5232 | 2025-09-12 13:30:00 | GOES-19 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 49.9 |
| 92244aa8-2b45-3893-8653-0748a6fd6e76 | -6.3092 | -42.2072 | 2025-09-12 13:30:00 | GOES-19 | ELESBÃO VELOSO | PIAUÍ | Brasil | 2203503 | 22 | 33 | nan | nan | nan | Caatinga | 73.9 |
| b0b70578-516f-3664-b054-19aaecd04c25 | -12.9292 | -54.7538 | 2025-09-12 13:30:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 159.1 |
| ef134717-2d74-3b11-bd18-b52aef0270ab | -12.9294 | -54.7333 | 2025-09-12 13:30:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 55.2 |
| 806622d5-385e-3386-a227-3889205b8ccc | -7.5455 | -44.3856 | 2025-09-12 13:30:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 105.9 |
| 5afa9d01-649d-391e-aa4a-84fc2198f944 | -7.321 | -49.6468 | 2025-09-12 13:30:00 | GOES-19 | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 60.6 |
| 301ed7ad-70b3-33cc-b2e2-5c88caee9ed4 | -16.08 | -49.9709 | 2025-09-12 13:30:00 | GOES-19 | ITABERAÍ | GOIÁS | Brasil | 5210406 | 52 | 33 | nan | nan | nan | Cerrado | 94.1 |
| 26039cbe-0dc0-324d-82fb-97f8980d05a7 | -13.1838 | -51.7429 | 2025-09-12 13:30:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 108.1 |
| b5cb93b7-3b92-3e3b-9520-b0ff6537b231 | -10.6983 | -48.6393 | 2025-09-12 13:30:00 | GOES-19 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 74.9 |
| 1f7a00f5-7ba3-384f-9d9c-0088a4359ad6 | -7.5643 | -44.3838 | 2025-09-12 13:30:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 124.9 |
| 019497a1-cfcd-30b0-8a89-cee10a6fa8f4 | -6.3226 | -53.4553 | 2025-09-12 13:30:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 62.9 |
| 34290768-9f28-3d52-bbdc-eeda054ac315 | -16.2939 | -50.0459 | 2025-09-12 13:30:00 | GOES-19 | ANICUNS | GOIÁS | Brasil | 5201306 | 52 | 33 | nan | nan | nan | Cerrado | 121.8 |
| cafcf7e3-44ff-3e74-bc8f-1a8c2fbb5112 | -6.3278 | -42.2294 | 2025-09-12 13:30:00 | GOES-19 | ELESBÃO VELOSO | PIAUÍ | Brasil | 2203503 | 22 | 33 | nan | nan | nan | Caatinga | 73.2 |
| 75c3b495-851f-3765-8b59-9f3f6ffec9a5 | -6.309 | -42.2311 | 2025-09-12 13:30:00 | GOES-19 | ELESBÃO VELOSO | PIAUÍ | Brasil | 2203503 | 22 | 33 | nan | nan | nan | Caatinga | 86.4 |
| 4859a82e-75d7-360c-bd31-eb6b3335cc28 | -7.2374 | -55.0604 | 2025-09-12 13:30:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 59.0 |
| a70b9572-b825-3a00-aa93-89f750935dac | -9.057 | -47.0355 | 2025-09-12 13:30:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 103.7 |
| 9810ebb1-fe26-367f-859a-c3e401982a67 | -13.2027 | -51.7618 | 2025-09-12 13:30:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 118.6 |
| c75729f0-5587-3b40-8922-7a5b3240dcf3 | -8.8901 | -49.9236 | 2025-09-12 13:30:00 | GOES-19 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 72.1 |
| 8e909537-4cca-3da4-843a-29708fd24bb3 | -13.2219 | -51.7595 | 2025-09-12 13:30:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 71.3 |
| cc97eeeb-1eaf-3070-b072-31a5750f7fd8 | -11.6622 | -46.611 | 2025-09-12 13:30:00 | GOES-19 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 60.3 |
| f562a7d1-b0a2-31a6-96e1-bc023e78b10b | -10.4252 | -50.6078 | 2025-09-12 13:30:00 | GOES-19 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 65.7 |
| 7cb11105-6cb8-3d79-9d57-277d0ad3b3ac | -14.394 | -52.9245 | 2025-09-12 13:30:00 | GOES-19 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 81.2 |
| 70cb5b9e-f475-362c-9b6f-5ddf62b34632 | -8.9371 | -46.1094 | 2025-09-12 13:30:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 84.3 |
| 3255086d-0d6c-3050-a6b1-a5740bea5874 | -6.1735 | -42.6221 | 2025-09-12 13:30:00 | GOES-19 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 83.6 |
| 5265a8cb-cb78-398f-8620-8a921dbd3238 | -9.0373 | -47.1041 | 2025-09-12 13:30:00 | GOES-19 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 223.4 |
| 953928a7-7152-3183-b9d2-4e3889807c23 | -10.7172 | -48.6371 | 2025-09-12 13:30:00 | GOES-19 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 70.4 |
| dce0c587-4fb5-359f-a1d0-19ae8f0100e7 | -9.7197 | -46.8972 | 2025-09-12 13:30:00 | GOES-19 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 167.9 |
| 1f0ac514-025f-3d93-9b17-9033ba91c6b1 | -10.679 | -48.6633 | 2025-09-12 13:30:00 | GOES-19 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 195.4 |
| 2ef7f5b3-2bc6-3866-a408-00f2f23e4acf | -7.5641 | -44.4068 | 2025-09-12 13:30:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 153.0 |
| 3cc4910f-db52-3c21-a408-d22155d408d6 | -9.77 | -46.0163 | 2025-09-12 13:30:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 143.5 |
| 297a0486-01dc-3a91-bdab-4391d7783fa9 | -11.4402 | -48.5513 | 2025-09-12 13:30:00 | GOES-19 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 148.6 |
| 40163d96-e6dd-345c-b256-5d13d4f985ad | -10.8968 | -45.6029 | 2025-09-12 13:30:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 94.0 |
| a7adcb11-935f-3cdf-a847-270e0670edb5 | -8.1837 | -46.0965 | 2025-09-12 13:30:00 | GOES-19 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 91.9 |
| f6155740-f2b9-3e60-8634-1f612d45d8a5 | -10.1405 | -47.9133 | 2025-09-12 13:30:00 | GOES-19 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 73.6 |
| ffdadf53-7892-319c-9839-4aabf6e32b86 | -8.956 | -46.1074 | 2025-09-12 13:30:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 132.1 |
| bd7c429b-bd86-39f8-a20a-b8620d4e683a | -8.8768 | -51.111 | 2025-09-12 13:30:00 | GOES-19 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 71.5 |
| 6932228a-2ae4-3f8b-a8b9-c21c7dd4258c | -16.5099 | -55.1459 | 2025-09-12 13:30:00 | GOES-19 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 86.0 |
| 1a5ca0c1-4bcc-35f0-8913-60c13cc8b12f | -7.2188 | -55.0615 | 2025-09-12 13:30:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 86.8 |
| 6a4320b9-d49e-3023-bd46-e2840622f67f | -6.8369 | -45.6559 | 2025-09-12 13:30:00 | GOES-19 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 70.3 |
| aa2bfca9-f66e-333a-86f9-e6a4d2c53e51 | -8.9374 | -46.0869 | 2025-09-12 13:30:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 85.0 |
| e33f312c-8b42-3d90-a8a5-ae390491c64d | -21.6455 | -50.1339 | 2025-09-12 13:30:00 | GOES-19 | ALTO ALEGRE | SÃO PAULO | Brasil | 3501103 | 35 | 33 | nan | nan | nan | Mata Atlântica | 104.4 |
| adfc6c35-1344-3b32-ab85-96de7858c48e | -21.6194 | -46.7875 | 2025-09-12 13:30:00 | GOES-19 | SÃO JOSÉ DO RIO PARDO | SÃO PAULO | Brasil | 3549706 | 35 | 33 | nan | nan | nan | Mata Atlântica | 100.1 |
| 989c6f18-f322-3427-b6d0-fc58ca1d7d0a | -11.9402 | -50.6987 | 2025-09-12 13:30:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 61.2 |
| 838122b1-51ca-3408-863e-9fc33a6d1334 | -6.7997 | -45.6364 | 2025-09-12 13:30:00 | GOES-19 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 64.0 |
| ab5e87c3-22b7-38e1-a15c-c6f9bb840578 | -10.1133 | -47.1642 | 2025-09-12 13:30:00 | GOES-19 | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 134.4 |
| afc8d27a-e2f4-3ebc-b155-1490f39aa09a | -12.6821 | -45.3209 | 2025-09-12 13:30:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 51.2 |
| 0f325142-cb6d-3346-abcf-2fbff2a77e3d | -9.0376 | -47.0819 | 2025-09-12 13:30:00 | GOES-19 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 121.4 |
| 8ae2298d-6601-3a28-b449-d050c13a6eb7 | -8.4331 | -47.2527 | 2025-09-12 13:30:00 | GOES-19 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 72.9 |
| 786d5fd4-324e-3cd8-ba98-e9b8a39ed6a9 | -11.4285 | -43.5544 | 2025-09-12 13:30:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 135.6 |
| e3e2ce46-21d0-3ebc-92aa-fbd703214fcf | -14.5132 | -53.8949 | 2025-09-12 13:30:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 96.2 |
| 37892771-e30a-384c-907c-b3c607fa25e6 | -9.673 | -47.5459 | 2025-09-12 13:30:00 | GOES-19 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 493.6 |
| a712ef5b-ee17-3f01-89d4-5dc8b83334b3 | -10.1216 | -47.9154 | 2025-09-12 13:30:00 | GOES-19 | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 72.4 |
| 1e6b4ba8-9c00-30be-a581-1dea8cd142ba | -10.8781 | -45.5826 | 2025-09-12 13:30:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 132.9 |
| 5897ae3a-2455-3082-a680-d23878baa504 | -14.3937 | -52.9456 | 2025-09-12 13:30:00 | GOES-19 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 129.0 |
| 42582752-992f-332a-a507-64ced3a91de1 | -7.5452 | -44.4086 | 2025-09-12 13:30:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 142.3 |
| a2967729-a442-36e5-9317-b3f3f2649253 | -8.2085 | -45.5981 | 2025-09-12 13:30:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 66.0 |
| ed4a87d6-7ce1-3aaf-b3a5-6bcc5c626f2c | -9.5137 | -54.6292 | 2025-09-12 13:30:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 77.9 |
| 632642cf-160e-32ca-8e75-a222df36d8c1 | -14.2162 | -58.5917 | 2025-09-12 13:30:00 | GOES-19 | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | 133.1 |
| d0603611-b748-3d14-a978-25d189bb4fd8 | -15.5236 | -48.5332 | 2025-09-12 13:30:00 | GOES-19 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 100.1 |
| 4aad9b93-831c-3740-b568-5fb839f5c525 | -8.4705 | -47.2712 | 2025-09-12 13:30:00 | GOES-19 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 71.7 |
| 07fd40f3-b191-3f0b-8135-917be1345f34 | -10.8972 | -45.58 | 2025-09-12 13:30:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 180.5 |
| 20a04873-1685-3c73-8901-adcc530004e8 | -8.8899 | -49.945 | 2025-09-12 13:30:00 | GOES-19 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 80.1 |


[Clique aqui para ver as próximas entradas](README131.md)
