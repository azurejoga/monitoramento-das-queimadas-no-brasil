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

## Dados Diários - Página 102

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| f1c3671b-3b4e-3a13-b090-b8280c548ffb | -8.9138 | -45.0232 | 2026-08-31 15:40:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 96.9 |
| c0c79070-f87e-3dd7-83a6-d3a4dcb1eedb | -10.8046 | -50.5046 | 2026-08-31 15:40:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 105.8 |
| 2329ea06-8b0d-3cbd-b2e2-d11abce2d1e9 | -10.7593 | -54.0589 | 2026-08-31 15:40:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 71.5 |
| 8fad8f15-8850-3cf3-8f88-0634b29ef203 | -9.694 | -65.0958 | 2026-08-31 15:40:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 159.8 |
| a4165fa3-14a6-3325-9b83-a474ffaf83f9 | -8.6673 | -62.8369 | 2026-08-31 15:40:00 | GOES-19 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 58.1 |
| 6acff034-dedb-37eb-bf56-71fec05a6fa6 | -5.2362 | -55.9112 | 2026-08-31 15:40:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 93.3 |
| e63097aa-8c42-3571-8a3c-e170ff28d33b | -5.2363 | -55.8914 | 2026-08-31 15:40:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 43.3 |
| f54bbdd8-a4f2-3462-8f34-4b1c90adcb21 | -10.7856 | -50.5066 | 2026-08-31 15:40:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 92.7 |
| 4ade8c1c-1ca0-34ee-862e-eeb2425e7700 | -10.1087 | -50.2776 | 2026-08-31 15:40:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 117.6 |
| 066587b4-3179-3335-b5c9-4cb3ce8b7a07 | -6.7123 | -58.9412 | 2026-08-31 15:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 66.1 |
| eff98649-6b9f-38d7-a5f6-07e0552c847e | -13.4707 | -57.0574 | 2026-08-31 15:40:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Cerrado | 72.9 |
| 4db7cf84-fd89-3f32-bec9-17e88ec0b08d | -11.3615 | -45.1955 | 2026-08-31 15:40:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 131.6 |
| e58209ef-c3e8-3606-bc3a-310ba8bfc86b | -11.2298 | -51.2456 | 2026-08-31 15:40:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 68.2 |
| 1f5f27f7-14e0-3336-a55c-ecc1e8c4061a | -5.8537 | -57.5576 | 2026-08-31 15:40:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 76.3 |
| 1037d5a0-c538-378b-9b79-fa1997f25c31 | -8.87 | -66.8935 | 2026-08-31 15:40:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 79.2 |
| a8663edb-8159-3c56-bd1a-951e4cb0b690 | -10.7407 | -54.0401 | 2026-08-31 15:40:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 252.8 |
| 89d7b9e7-8437-31a3-a9dc-e7ccf2e835d1 | -8.7442 | -46.4437 | 2026-08-31 15:40:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 122.5 |
| e0872b48-d878-3526-8d49-91c670043a76 | -3.1083 | -61.2191 | 2026-08-31 15:40:00 | GOES-19 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 51.9 |
| a193edd6-08d7-399b-9070-d3cd284a1f43 | -10.7428 | -50.8727 | 2026-08-31 15:40:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 84.7 |
| 4f6f3202-6f02-3471-ae63-3875772e669e | -8.5969 | -54.7755 | 2026-08-31 15:40:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 67.8 |
| b163ee3a-7354-3df8-8033-12f0dbb47b6d | -9.5964 | -47.6204 | 2026-08-31 15:40:00 | GOES-19 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 145.9 |
| 37187e9a-ecf7-3d1e-9a3c-6568ad5702a3 | -6.77 | -55.6445 | 2026-08-31 15:40:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 63.7 |
| 68e0e744-0def-3830-b5f8-a9a8217cb123 | -7.9907 | -46.5177 | 2026-08-31 15:40:00 | GOES-19 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 112.3 |
| aab8fa34-abaa-3ba0-a032-25cbd703f127 | -9.7873 | -59.4479 | 2026-08-31 15:40:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 47.4 |
| e62e02ea-d59b-30b9-8fc5-ccea32d069ad | -13.9667 | -54.4157 | 2026-08-31 15:40:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 162.0 |
| 2cabf0e3-9f37-331f-9006-527402fd84ee | -10.8614 | -50.4985 | 2026-08-31 15:40:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 86.3 |
| aff5d0cf-123e-35f9-8b01-dd0754b2552f | -11.1821 | -50.592 | 2026-08-31 15:40:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 145.7 |
| 810f81e2-317d-3d9f-bfe4-2e07c50eb354 | -6.7699 | -55.6644 | 2026-08-31 15:40:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 78.5 |
| 2ff606c2-d3b3-3911-9d2c-1d432b836b78 | -7.3663 | -55.1734 | 2026-08-31 15:40:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 70.8 |
| e74e2c1a-431c-3e0b-bf52-fc945b66823a | -6.2471 | -53.6623 | 2026-08-31 15:40:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 58.3 |
| e89486d9-629a-32f5-b326-35c3e1dfcceb | -8.7968 | -62.8695 | 2026-08-31 15:40:00 | GOES-19 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 50.7 |
| 93e37f3a-7c88-3e32-98cc-0b20db6ebac4 | -12.3615 | -50.5632 | 2026-08-31 15:40:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 97.9 |
| ffa11fb9-779f-3658-9ee0-7f70b72e2e90 | -8.7039 | -62.9111 | 2026-08-31 15:40:00 | GOES-19 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 54.9 |
| 6ae8e566-f80d-365a-b7e8-67e603f3d0de | -11.1824 | -50.5706 | 2026-08-31 15:40:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 164.1 |
| 88db4e12-8128-3f02-8f8f-e4b761e13685 | -11.6975 | -54.5467 | 2026-08-31 15:40:00 | GOES-19 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 97.0 |
| 6214bb23-5ef3-3367-a4f8-9de9815c5e1c | -13.471 | -57.0373 | 2026-08-31 15:40:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Cerrado | 268.0 |
| 09c67260-e2b4-30f2-9dd9-27da73c3870c | -8.7631 | -46.4418 | 2026-08-31 15:40:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 145.7 |
| 27123deb-5933-3029-b16b-3b4b292d06fa | -11.8021 | -51.0343 | 2026-08-31 15:40:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 70.8 |
| fb6a588d-cab9-3e1e-ac1a-fe2700c75405 | -2.6741 | -59.3628 | 2026-08-31 15:40:00 | GOES-19 | RIO PRETO DA EVA | AMAZONAS | Brasil | 1303569 | 13 | 33 | nan | nan | nan | Amazônia | 74.3 |
| c41b48db-018a-333e-ac8c-f98c9fa8616d | -7.2934 | -60.5713 | 2026-08-31 15:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 114.2 |
| 66944f28-e93b-3f9d-a3e4-b6b8a1fa8d12 | -5.2548 | -55.8907 | 2026-08-31 15:40:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 114.7 |
| adbc5684-ae1b-3cc3-a706-9f6e3f28567c | -3.6215 | -60.566 | 2026-08-31 15:40:00 | GOES-19 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 220.3 |
| c809cafe-da94-30bb-894c-5b0405a3f42e | -9.4342 | -45.6704 | 2026-08-31 15:40:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 122.8 |
| 98238894-3cd3-3aab-b940-e1ae7582f0ce | -7.3478 | -55.1744 | 2026-08-31 15:40:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 72.7 |
| 5fcb0fa6-a5c7-38b5-b761-b254811de6be | -10.5793 | -50.3789 | 2026-08-31 15:40:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 91.5 |
| 24a94f0a-2f8a-332d-a60f-237eda454e6b | -15.2275 | -56.3716 | 2026-08-31 15:40:00 | GOES-19 | ACORIZAL | MATO GROSSO | Brasil | 5100102 | 51 | 33 | nan | nan | nan | Cerrado | 222.4 |
| f7613a52-cc88-3517-818c-3aa4fa99e4de | -14.4201 | -52.5201 | 2026-08-31 15:40:00 | GOES-19 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 140.1 |
| b03f71e1-d9a4-325d-a415-f9924134a54a | -13.9474 | -54.4179 | 2026-08-31 15:40:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 187.1 |
| f1798018-1520-3039-ad77-00adf5147022 | -9.1662 | -60.2752 | 2026-08-31 15:40:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 38.1 |
| ee19caeb-e12b-317b-8b58-565fe395c588 | -6.9177 | -55.6967 | 2026-08-31 15:40:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 58.8 |
| 8dfef67c-36fa-36fc-9fa5-b63fa3d0c005 | -3.9707 | -60.0258 | 2026-08-31 15:40:00 | GOES-19 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 65.0 |
| 1ef986e0-7903-3b12-b972-4f453e07face | -3.1998 | -61.161 | 2026-08-31 15:40:00 | GOES-19 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 81.1 |
| 7b81bc6c-6118-34ef-957e-d763516697b2 | -3.9363 | -59.3381 | 2026-08-31 15:40:00 | GOES-19 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 54.1 |
| 5a5c0520-dcf1-37c6-ad3d-bfdf424895c7 | -14.5255 | -51.9968 | 2026-08-31 15:40:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 41.8 |
| 3d93dcaa-6dc9-3161-bce2-72a1364e4603 | -9.806 | -59.4468 | 2026-08-31 15:40:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 62.0 |
| 33e928fd-4446-3731-a490-4eb02a91c140 | -7.9336 | -44.9893 | 2026-08-31 15:40:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 104.9 |
| a03546ee-0561-3ee2-be64-a6f4c8d8785c | -7.9425 | -44.2538 | 2026-08-31 15:40:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 194.1 |
| 9bde400b-6df8-3c3d-96ba-4e8a25134308 | -5.4876 | -57.1416 | 2026-08-31 15:40:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 59.8 |
| d268e196-71a2-3a5d-bacd-f1a13855178f | -3.4185 | -61.3273 | 2026-08-31 15:40:00 | GOES-19 | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 52.5 |
| 2dfaf548-fd3d-33a8-aa58-50c37c34be9b | -9.8927 | -60.2752 | 2026-08-31 15:40:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 44.9 |
| 6389ae7d-cdee-3cc1-ac4c-0bc75302c39d | -10.8425 | -50.5005 | 2026-08-31 15:40:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 90.0 |
| 33e4b465-1061-34a6-9484-17b909242e2b | -11.3806 | -45.1928 | 2026-08-31 15:40:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 164.7 |
| fcc27dea-667e-30f4-86bc-7543237ff0fc | -6.8751 | -56.5116 | 2026-08-31 15:40:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 81.8 |
| 55ece903-d133-3a8b-8335-e05725bc77e4 | -10.1528 | -45.7665 | 2026-08-31 15:40:00 | GOES-19 | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 136.0 |
| c97ec519-c3f4-3b14-af9d-24eea4f88133 | -10.8617 | -50.4772 | 2026-08-31 15:40:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 92.5 |
| 40557051-80fd-3308-a1c5-1defaed75155 | -3.6076 | -59.0769 | 2026-08-31 15:40:00 | GOES-19 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 89.1 |
| 93205caa-3444-352d-8f68-e7315956ba41 | -12.1109 | -45.0395 | 2026-08-31 15:40:00 | GOES-19 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 82.4 |
| 9c849cd4-a495-34f4-9367-c10a66d2c5d6 | -8.7439 | -46.4661 | 2026-08-31 15:40:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 299.2 |
| 7e1261e5-afef-3331-b555-0c99a90cc308 | -11.1634 | -50.5727 | 2026-08-31 15:40:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 113.2 |
| 914a780b-ab0c-37e3-9258-e930bd68df37 | -11.1818 | -50.6133 | 2026-08-31 15:40:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 78.8 |
| b96d5b7c-8b01-361e-ac70-6b1add8e1da7 | -10.7598 | -54.0179 | 2026-08-31 15:40:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 97.3 |
| e423ff1e-362c-3fd0-83ce-6fc289990eab | -5.9636 | -57.6704 | 2026-08-31 15:40:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 64.7 |
| 05350026-6270-36e5-a437-7eb7bfc23eb8 | -15.6139 | -56.4103 | 2026-08-31 15:40:00 | GOES-19 | NOSSA SENHORA DO LIVRAMENTO | MATO GROSSO | Brasil | 5106109 | 51 | 33 | nan | nan | nan | Cerrado | 77.7 |
| 8db639ce-1ad4-3cb0-be88-ea4464de1d5d | -11.3431 | -45.1521 | 2026-08-31 15:40:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 126.9 |
| 6638569e-f73d-368b-961c-2f3760c9228b | -10.5598 | -50.4236 | 2026-08-31 15:40:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 94.6 |
| 23a7c3c8-7d4f-3f87-90db-9bbde09bbb93 | -9.6676 | -47.9429 | 2026-08-31 15:40:00 | GOES-19 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 257.1 |
| aaa33dc1-b49e-328b-9c16-e020c0904a52 | -8.9428 | -63.2797 | 2026-08-31 15:40:00 | GOES-19 | ITAPUÃ DO OESTE | RONDÔNIA | Brasil | 1101104 | 11 | 33 | nan | nan | nan | Amazônia | 54.6 |
| d833f80f-79cb-3513-9e79-0bc56029b134 | -10.7409 | -54.0196 | 2026-08-31 15:40:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 88.2 |
| 29c6082e-cf53-3429-98af-6e2b7fb60756 | -8.7989 | -62.5095 | 2026-08-31 15:40:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 173.3 |
| 3f2652cb-fc63-3fd1-b1ff-d8bc4bd94152 | -14.483 | -49.0333 | 2026-08-31 15:40:00 | GOES-19 | URUAÇU | GOIÁS | Brasil | 5221601 | 52 | 33 | nan | nan | nan | Cerrado | 57.7 |
| a7f136f3-1a32-3d5d-bd94-7edcaf80d03d | -6.1295 | -57.6637 | 2026-08-31 15:40:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 74.2 |
| 2b840850-5971-3ca7-976a-153a2524fe32 | -11.6786 | -54.5484 | 2026-08-31 15:40:00 | GOES-19 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 112.1 |
| 71114836-1dcd-37b7-aed3-28b5ad6e62e3 | -15.6336 | -56.3876 | 2026-08-31 15:40:00 | GOES-19 | NOSSA SENHORA DO LIVRAMENTO | MATO GROSSO | Brasil | 5106109 | 51 | 33 | nan | nan | nan | Cerrado | 250.6 |
| e7520999-23b5-3c0f-aa98-154b3e572859 | -12.0925 | -47.1587 | 2026-08-31 15:40:00 | GOES-19 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 145.4 |
| f180f2f7-63bb-3a1e-a4a3-0ebd191c1de4 | -7.3476 | -55.1945 | 2026-08-31 15:40:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 68.2 |
| a5ac34aa-9307-3ee0-9caa-d7c4a214ac10 | -10.8043 | -50.5259 | 2026-08-31 15:40:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 84.2 |
| f1e1658d-7cd8-3b83-92d2-1badd1589d92 | -9.2092 | -51.5654 | 2026-08-31 15:40:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 114.0 |
| b83f5e36-fd28-31c6-b523-b2bc96a068ce | -13.4901 | -57.0355 | 2026-08-31 15:50:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Cerrado | 89.2 |
| 967cd26c-7e8b-3d7b-93d2-781af497cc39 | -6.7123 | -58.9412 | 2026-08-31 15:50:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 70.5 |
| a1321f5c-8283-3d5c-8d86-2de1351baeee | -10.1087 | -50.2776 | 2026-08-31 15:50:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 77.6 |
| 51257fa6-4f46-3a74-b42b-23b1bee9146e | -6.9491 | -56.508 | 2026-08-31 15:50:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 55.9 |
| a2ba9b2f-14e2-3324-b0c0-cf9f2ef8fad1 | -12.9054 | -59.8857 | 2026-08-31 15:50:00 | GOES-19 | COMODORO | MATO GROSSO | Brasil | 5103304 | 51 | 33 | nan | nan | nan | Cerrado | 60.6 |
| 01249bf2-73b9-3ded-a2c8-de1a283cfad5 | -12.2468 | -50.577 | 2026-08-31 15:50:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 59.6 |
| 809824f9-1780-30ac-87ad-01899e1ecec0 | -8.7039 | -62.9111 | 2026-08-31 15:50:00 | GOES-19 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 80.5 |
| d7d1be16-6625-3838-aa4f-dd956812693f | -10.8428 | -50.4792 | 2026-08-31 15:50:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 69.7 |
| 7037c1b2-00cc-3a7a-a6d8-c3349579bda2 | -6.3032 | -53.5782 | 2026-08-31 15:50:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 80.8 |
| 24ac10a3-8ba1-323f-a6ca-34d18112ac5c | -2.6559 | -59.3631 | 2026-08-31 15:50:00 | GOES-19 | RIO PRETO DA EVA | AMAZONAS | Brasil | 1303569 | 13 | 33 | nan | nan | nan | Amazônia | 54.8 |
| 3355a534-e900-372e-bd11-fa0aa11ac14d | -11.2317 | -53.9958 | 2026-08-31 15:50:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 90.4 |
| fab08188-b158-3171-8f56-4a3452be8665 | -14.8316 | -55.7399 | 2026-08-31 15:50:00 | GOES-19 | CHAPADA DOS GUIMARÃES | MATO GROSSO | Brasil | 5103007 | 51 | 33 | nan | nan | nan | Cerrado | 53.8 |
| 95d5cc61-93e6-35a3-b1be-d88279f2badc | -11.2125 | -54.0181 | 2026-08-31 15:50:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 104.2 |


[Clique aqui para ver as próximas entradas](README103.md)
