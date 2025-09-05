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

## Dados Diários - Página 66

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 5946f476-ba61-3c94-9dd7-9f7311ade23c | -15.6988 | -53.598 | 2025-09-05 13:30:00 | GOES-19 | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | 68.2 |
| a6538f53-4014-37ea-a1b6-67b8ecb11864 | -14.0691 | -53.9892 | 2025-09-05 13:30:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 110.3 |
| 0d5ec11d-befd-350a-8609-3edadb0983a6 | -14.0496 | -54.0122 | 2025-09-05 13:30:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 281.4 |
| ff3f42fb-fd84-37c3-a1cd-ebd51ba1e459 | -10.2373 | -50.5417 | 2025-09-05 13:30:00 | GOES-19 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 72.1 |
| ce042296-99d9-3238-ab97-b0951714a0e9 | -8.9034 | -45.7973 | 2025-09-05 13:30:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 106.4 |
| 09744794-9121-38fd-85b0-0c4053ee6b1c | -5.9846 | -44.7261 | 2025-09-05 13:30:00 | GOES-19 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 101.9 |
| 8ff58e99-efa1-3412-b5c4-8e7a14dc57b3 | -12.8816 | -56.9505 | 2025-09-05 13:30:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 63.4 |
| 8c80f79d-70a6-3d4d-a3d4-3c8569d815ae | -6.2421 | -43.2743 | 2025-09-05 13:30:00 | GOES-19 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 67.6 |
| ca62aceb-ff31-368f-8862-8594fda6aecc | -12.7251 | -45.0828 | 2025-09-05 13:30:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 77.8 |
| 22cbd43d-e331-3ddd-a6b8-d899e88e007f | -9.0721 | -50.4181 | 2025-09-05 13:30:00 | GOES-19 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 69.9 |
| ea22331e-b8ba-3de8-8b25-621246453e0d | -10.7691 | -45.2539 | 2025-09-05 13:30:00 | GOES-19 | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 62.6 |
| 5aca581b-34b1-3189-b3df-260709426853 | -9.0719 | -50.4394 | 2025-09-05 13:30:00 | GOES-19 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 105.2 |
| ea6fa5b8-ec31-3b71-b89e-d3e8cad1706e | -6.2609 | -43.2727 | 2025-09-05 13:30:00 | GOES-19 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 81.6 |
| 8da974be-bc72-3a42-9098-297d9cc0617a | -7.6083 | -43.8477 | 2025-09-05 13:30:00 | GOES-19 | BERTOLÍNIA | PIAUÍ | Brasil | 2201705 | 22 | 33 | nan | nan | nan | Cerrado | 76.8 |
| fb9f5405-575f-39e4-b7a2-2bc3f53c6e45 | -16.4624 | -45.2402 | 2025-09-05 13:30:00 | GOES-19 | SÃO ROMÃO | MINAS GERAIS | Brasil | 3164209 | 31 | 33 | nan | nan | nan | Cerrado | 138.4 |
| e2ad394b-99e5-33c2-bb45-0ead54075e44 | -9.7031 | -51.0802 | 2025-09-05 13:30:00 | GOES-19 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 83.6 |
| 9b2914eb-857a-3597-b6c6-ad3717228e5a | -15.235 | -52.3693 | 2025-09-05 13:30:00 | GOES-19 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 75.1 |
| 7458af9f-fab4-3c09-a3f0-e353fb00d091 | -10.7688 | -45.2769 | 2025-09-05 13:30:00 | GOES-19 | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 153.0 |
| f6cb2f9e-425f-3f01-a506-4018a9d8111b | -8.4793 | -45.0475 | 2025-09-05 13:30:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 76.1 |
| be02aff8-bedc-3197-bfcc-42cd2f8eef94 | -15.7179 | -53.6165 | 2025-09-05 13:30:00 | GOES-19 | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | 104.1 |
| 23d15c81-2993-3ad7-8e60-27d7ef670a33 | -15.7182 | -53.5954 | 2025-09-05 13:30:00 | GOES-19 | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | 153.0 |
| 8d5ab94f-00a7-36b7-b6ff-bb7ffce3ae0b | -5.9846 | -44.7261 | 2025-09-05 13:40:00 | GOES-19 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 127.3 |
| 2b4a195b-e4b7-33f9-a2ff-96a8dd0e5d15 | -6.7994 | -45.659 | 2025-09-05 13:40:00 | GOES-19 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 71.0 |
| 8f7fc84b-e73b-37b3-9634-4ad62b810d8d | -9.0719 | -50.4394 | 2025-09-05 13:40:00 | GOES-19 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 105.3 |
| e382fa4e-f315-36f0-9bec-8670991c1d8a | -5.8794 | -46.0433 | 2025-09-05 13:40:00 | GOES-19 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 76.5 |
| e58a4e81-5fbb-3e05-bb56-a1919507c51e | -10.0527 | -46.1183 | 2025-09-05 13:40:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 75.8 |
| 4812a8ac-3917-3e34-ab4e-455fce5bb804 | -7.8964 | -44.9473 | 2025-09-05 13:40:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 70.4 |
| 6193dd0f-278d-3e76-bfe7-7635e96841f3 | -10.7691 | -45.2539 | 2025-09-05 13:40:00 | GOES-19 | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 54.7 |
| 51893b1a-5455-357e-8804-fb67f3b468ae | -15.6137 | -52.9122 | 2025-09-05 13:40:00 | GOES-19 | GENERAL CARNEIRO | MATO GROSSO | Brasil | 5103908 | 51 | 33 | nan | nan | nan | Cerrado | 53.3 |
| 3960e277-84d7-3fdd-a597-41b81f594301 | -5.5884 | -45.1185 | 2025-09-05 13:40:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 71.1 |
| 119859b7-9dff-3396-8d44-3a29cffa9b61 | -6.1679 | -43.1869 | 2025-09-05 13:40:00 | GOES-19 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Caatinga | 66.0 |
| 9b489be0-83bf-3747-ac59-3153b4cdb842 | -16.4624 | -45.2402 | 2025-09-05 13:40:00 | GOES-19 | SÃO ROMÃO | MINAS GERAIS | Brasil | 3164209 | 31 | 33 | nan | nan | nan | Cerrado | 93.2 |
| 1748bf25-904a-39e0-bd5e-40be6370eaf1 | -7.8967 | -44.9244 | 2025-09-05 13:40:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 173.7 |
| 1c4bfc26-ebdc-31cf-8b2c-16f4c56360a1 | -11.6238 | -47.7786 | 2025-09-05 13:40:00 | GOES-19 | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 73.5 |
| ab84f4ab-3cb7-3f33-ac34-b224fe339675 | -10.2373 | -50.5417 | 2025-09-05 13:40:00 | GOES-19 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 71.4 |
| 2044de80-5ca5-37c2-b9f4-47d7fcacc656 | -8.4418 | -45.0286 | 2025-09-05 13:40:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 67.3 |
| 41ecc0e9-c0c8-3a77-9423-988d3520add2 | -9.7031 | -51.0802 | 2025-09-05 13:40:00 | GOES-19 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 82.7 |
| 4e729918-6d98-3200-b2ab-80d9f5a60454 | -5.9844 | -44.7489 | 2025-09-05 13:40:00 | GOES-19 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 125.8 |
| 8e822cce-1cc2-3feb-9cc3-dbd6ca35190e | -6.2609 | -43.2727 | 2025-09-05 13:40:00 | GOES-19 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 89.2 |
| a0983c3a-86a1-3972-a2db-cfc1e496f91f | -7.6083 | -43.8477 | 2025-09-05 13:40:00 | GOES-19 | BERTOLÍNIA | PIAUÍ | Brasil | 2201705 | 22 | 33 | nan | nan | nan | Cerrado | 212.0 |
| 44985a5d-b0c8-3e7c-99e3-db13ec73f8e8 | -8.9034 | -45.7973 | 2025-09-05 13:40:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 101.4 |
| 0b397a18-d088-3d19-ae99-bd9d35e000e6 | -6.2381 | -45.6358 | 2025-09-05 13:40:00 | GOES-19 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 76.8 |
| a53acaa9-eb75-3856-931c-feb5e1bcb78e | -8.8848 | -45.7767 | 2025-09-05 13:40:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 72.4 |
| 7ffd88a5-ab5f-3ba9-b767-e2257554b996 | -13.3192 | -51.6626 | 2025-09-05 13:40:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 90.9 |
| bd0d9fc0-5fca-33a1-ab54-33641bf4c81f | -15.235 | -52.3693 | 2025-09-05 13:40:00 | GOES-19 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 85.7 |
| 7ef1fea5-6e2f-3bb1-a93f-a338b28b6527 | -13.0889 | -57.1126 | 2025-09-05 13:40:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 65.3 |
| 19b07cd2-5490-3d39-8c7e-620b0481e99b | -12.7251 | -45.0828 | 2025-09-05 13:40:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 66.7 |
| 6a5d4139-48c5-3f65-934c-0994a9226ef8 | -9.7105 | -48.9853 | 2025-09-05 13:40:00 | GOES-19 | ABREULÂNDIA | TOCANTINS | Brasil | 1700251 | 17 | 33 | nan | nan | nan | Cerrado | 110.5 |
| 0fd3ea1b-6e11-3f26-8033-f294bcb67281 | -14.7465 | -47.4955 | 2025-09-05 13:40:00 | GOES-19 | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 75.8 |
| 9b401787-de0c-3b93-9241-6004b9119ea3 | -5.9656 | -44.7503 | 2025-09-05 13:40:00 | GOES-19 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 74.4 |
| 1eb6be23-3b7d-3e3a-aeed-04b9d35d0841 | -15.3435 | -53.9382 | 2025-09-05 13:40:00 | GOES-19 | POXORÉU | MATO GROSSO | Brasil | 5107008 | 51 | 33 | nan | nan | nan | Cerrado | 96.9 |
| 1044d0af-03cc-33a7-affd-1bf126d31c38 | -9.0721 | -50.4181 | 2025-09-05 13:40:00 | GOES-19 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 87.9 |
| 3c326560-0e91-3ec5-b8dc-c94a4200543b | -8.4415 | -45.0515 | 2025-09-05 13:40:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 85.2 |
| 4c48afda-1e9d-392d-b904-c928d3377542 | -7.0314 | -43.2742 | 2025-09-05 13:40:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 73.4 |
| 4430b44b-dd01-3b25-b0f1-df41f577b5ff | -10.7688 | -45.2769 | 2025-09-05 13:40:00 | GOES-19 | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 123.0 |
| 5f542cd4-4473-3822-880a-975a19d158ec | -11.5961 | -52.176 | 2025-09-05 13:40:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 63.4 |
| d2be7726-2143-35a8-9c87-62c9de149db5 | -8.9037 | -45.7747 | 2025-09-05 13:40:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 118.0 |
| 2d5d263a-32d9-3d4c-af06-e0217b64aed2 | -5.8799 | -45.9761 | 2025-09-05 13:40:00 | GOES-19 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 69.3 |
| 64e82902-f019-3109-a643-86a2a54627de | -5.7923 | -45.3078 | 2025-09-05 13:40:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 77.8 |
| b3451b77-1c0c-308f-b7de-341f3376452c | -15.6141 | -52.891 | 2025-09-05 13:40:00 | GOES-19 | GENERAL CARNEIRO | MATO GROSSO | Brasil | 5103908 | 51 | 33 | nan | nan | nan | Cerrado | 95.4 |
| 4ecd8ef3-6f15-3c58-8f47-4ed23b74e8b7 | -6.2421 | -43.2743 | 2025-09-05 13:40:00 | GOES-19 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 85.9 |
| bd3bd49e-1587-3def-93d1-020260fed830 | -11.6235 | -47.8008 | 2025-09-05 13:40:00 | GOES-19 | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 96.9 |
| 30d894fd-c658-369b-adbb-4f5a5630207d | -9.0762 | -47.0113 | 2025-09-05 13:40:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 82.0 |
| 4b641935-07ec-37d7-9183-e9cdbb70374b | -9.6916 | -48.9872 | 2025-09-05 13:40:00 | GOES-19 | ABREULÂNDIA | TOCANTINS | Brasil | 1700251 | 17 | 33 | nan | nan | nan | Cerrado | 72.4 |
| ee8030ac-c69b-3af2-aead-046a323e0142 | -14.0307 | -53.9936 | 2025-09-05 13:50:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 84.4 |
| d2b8d300-ff81-3ea0-9a60-4fcf8102fa19 | -15.2346 | -52.3906 | 2025-09-05 13:50:00 | GOES-19 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 77.7 |
| 3360220c-f100-3328-8207-d29e33bfc2e4 | -11.5961 | -52.176 | 2025-09-05 13:50:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 66.8 |
| 4ae5d1a2-4a70-379e-a8fb-4730340d90db | -15.7756 | -53.6509 | 2025-09-05 13:50:00 | GOES-19 | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | 196.5 |
| 0c29bd6b-f02d-357c-9907-9c932d9a18f2 | -15.7179 | -53.6165 | 2025-09-05 13:50:00 | GOES-19 | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | 118.5 |
| c9141c78-658d-34e3-8583-e04280c5e679 | -6.2296 | -42.641 | 2025-09-05 13:50:00 | GOES-19 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 109.3 |
| d9e29770-c160-381b-a73c-1133c55b19ec | -6.2755 | -45.633 | 2025-09-05 13:50:00 | GOES-19 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 87.7 |
| 6367a7a6-7eb2-3c05-8739-c9a3a634a49b | -7.0314 | -43.2742 | 2025-09-05 13:50:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 76.0 |
| 8bb32f28-37b0-3781-8f61-3335c1d9de21 | -9.8479 | -45.8714 | 2025-09-05 13:50:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 84.5 |
| 00b98602-942b-3cf3-bc81-fe38321dd7e4 | -14.7465 | -47.4955 | 2025-09-05 13:50:00 | GOES-19 | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 158.1 |
| e4c97194-69b7-34d7-a63f-ebb0965949e0 | -12.5365 | -48.0557 | 2025-09-05 13:50:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 89.8 |
| 0de7c027-f91d-33e4-a736-04b72019763c | -17.9658 | -48.5847 | 2025-09-05 13:50:00 | GOES-19 | CALDAS NOVAS | GOIÁS | Brasil | 5204508 | 52 | 33 | nan | nan | nan | Cerrado | 95.1 |
| be975f77-095b-3418-82d3-96238437fa44 | -8.9037 | -45.7747 | 2025-09-05 13:50:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 77.6 |
| 4f0218fd-ece2-3ac6-9f6f-31c93992efc4 | -8.9034 | -45.7973 | 2025-09-05 13:50:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 81.2 |
| c4f1da8e-84ed-352b-9962-005d8fa8c759 | -11.864 | -50.7075 | 2025-09-05 13:50:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 104.9 |
| 6bc4be02-bbd7-35a2-a79d-df9975d41cac | -11.0055 | -45.9527 | 2025-09-05 13:50:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 74.1 |
| 560228d4-5074-3964-8463-f2a24fe7a62d | -6.2606 | -43.2961 | 2025-09-05 13:50:00 | GOES-19 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 72.5 |
| 6a496978-a4a6-3ff5-aa6f-a3e095697463 | -15.6988 | -53.598 | 2025-09-05 13:50:00 | GOES-19 | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | 71.4 |
| 6e2e0761-c4d4-3b8c-a2a6-410552e0d14b | -6.1679 | -43.1869 | 2025-09-05 13:50:00 | GOES-19 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Caatinga | 72.0 |
| f72fb3e7-d446-3aa3-a487-6c9d77f4aedf | -11.1714 | -50.0151 | 2025-09-05 13:50:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 83.1 |
| eb3e081e-d9d0-36e6-9900-a57893e69511 | -6.9568 | -44.9434 | 2025-09-05 13:50:00 | GOES-19 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 76.1 |
| 2e952e18-0363-3557-b93a-85b317d24ad6 | -15.7182 | -53.5954 | 2025-09-05 13:50:00 | GOES-19 | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | 277.8 |
| 6782eaad-9cc8-3fcc-a182-56dd02e378ba | -10.7691 | -45.2539 | 2025-09-05 13:50:00 | GOES-19 | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 86.9 |
| c6a7ea40-9cb8-30db-b2ba-d424fec4c255 | -10.2373 | -50.5417 | 2025-09-05 13:50:00 | GOES-19 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 77.9 |
| 0b1f4723-1851-39b7-ac61-b2e141e66f38 | -14.0499 | -53.9914 | 2025-09-05 13:50:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 180.1 |
| c11ba923-fe97-3f9a-a66f-a2a3b0262b59 | -15.235 | -52.3693 | 2025-09-05 13:50:00 | GOES-19 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 98.9 |
| e07ae341-a453-35f8-ad47-dfe0bbcf7cdb | -6.2418 | -43.2976 | 2025-09-05 13:50:00 | GOES-19 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 67.2 |
| 89ec28ed-6982-334d-b186-25a3ad5d9327 | -7.9527 | -44.9646 | 2025-09-05 13:50:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 75.5 |
| 32a4d452-9ea3-32d0-87a0-da0b98d31498 | -8.479 | -45.0704 | 2025-09-05 13:50:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 101.2 |
| 0aaae026-7ab4-3b30-b025-4c5a2d4c9168 | -9.0719 | -50.4394 | 2025-09-05 13:50:00 | GOES-19 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 95.6 |
| 5060529c-0404-3a32-86cd-ecc0a0e6bacb | -6.2421 | -43.2743 | 2025-09-05 13:50:00 | GOES-19 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 77.2 |
| fcd8f96b-953c-3475-83a0-b62cc6fa9253 | -9.7105 | -48.9853 | 2025-09-05 13:50:00 | GOES-19 | ABREULÂNDIA | TOCANTINS | Brasil | 1700251 | 17 | 33 | nan | nan | nan | Cerrado | 90.7 |
| a7649f13-936d-38b5-aef6-e072a3f3ff43 | -8.3458 | -48.2916 | 2025-09-05 13:50:00 | GOES-19 | PRESIDENTE KENNEDY | TOCANTINS | Brasil | 1718402 | 17 | 33 | nan | nan | nan | Cerrado | 69.0 |
| a4a00674-7d72-35ed-b8bd-52fe747a49ae | -9.6916 | -48.9872 | 2025-09-05 13:50:00 | GOES-19 | ABREULÂNDIA | TOCANTINS | Brasil | 1700251 | 17 | 33 | nan | nan | nan | Cerrado | 70.6 |
| e9c65836-dfb0-3d73-a889-fc4bc3c8b4b1 | -5.9844 | -44.7489 | 2025-09-05 13:50:00 | GOES-19 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 116.1 |
| 9455ceae-b6c3-33a1-9617-948b0e9b98d0 | -6.9167 | -45.197 | 2025-09-05 13:50:00 | GOES-19 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 81.4 |


[Clique aqui para ver as próximas entradas](README67.md)
