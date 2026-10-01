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

## Dados Diários - Página 36

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 17e8f04a-e4b8-32be-af27-75a66cea8320 | -6.74075 | -44.13932 | 2026-10-01 04:14:00 | NPP-375D | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 2f50c87a-9d05-366f-a7df-1d29081ec265 | -4.45649 | -47.92415 | 2026-10-01 04:14:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 13.8 |
| 5a7bc07d-a90d-3934-80d0-8bc141f30d82 | -9.78163 | -44.8115 | 2026-10-01 04:14:00 | NPP-375D | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 4f22fa68-2203-3c1f-8653-ed63b4bb6b55 | -10.21536 | -45.31759 | 2026-10-01 04:14:00 | NPP-375D | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 3.7 |
| d8d81052-cd72-3097-9004-d8fc4ca8a9ee | -5.74557 | -45.0582 | 2026-10-01 04:14:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 55b2caae-5912-3b7f-8b71-c1299e70e1e7 | -4.29506 | -50.81784 | 2026-10-01 04:14:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 8.4 |
| 74a83d2f-c919-3c42-840a-8addc6b1d734 | -4.29289 | -50.75822 | 2026-10-01 04:14:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| f0ad4c77-de59-3873-9c18-ed13482d21eb | -4.25618 | -50.76037 | 2026-10-01 04:14:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 45.6 |
| 51999069-e7d8-3969-8f6f-590f31c42973 | -11.40923 | -43.4065 | 2026-10-01 04:14:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 3.8 |
| fb39c63f-f947-3d91-8b97-49d014eb32e8 | -4.26323 | -50.7564 | 2026-10-01 04:14:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 67.2 |
| a3a4a156-d017-3ad2-98b1-5ee079ac251c | -4.28717 | -50.84003 | 2026-10-01 04:14:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| eb655265-53e2-3840-8e4e-a5de85171cfa | -10.84602 | -48.69513 | 2026-10-01 04:14:00 | NPP-375D | BREJINHO DE NAZARÉ | TOCANTINS | Brasil | 1703701 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| dceacdd4-cd85-3716-b848-ba231598cba4 | -5.14433 | -47.60299 | 2026-10-01 04:14:00 | NPP-375D | CIDELÂNDIA | MARANHÃO | Brasil | 2103257 | 21 | 33 | nan | nan | nan | Amazônia | 2.7 |
| e64443f5-e3a6-3e31-a6ed-6af002f4dc95 | -4.25945 | -50.76706 | 2026-10-01 04:14:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 14.3 |
| 858d6b6f-ba7b-3bfd-abb3-aae097b20e1d | -11.41687 | -43.4038 | 2026-10-01 04:14:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 1a2862cc-c59d-3448-b7c5-d3021a08cb7a | -4.27891 | -50.7652 | 2026-10-01 04:14:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 38.5 |
| 3dbb68d5-d7e5-3b4b-8d4b-db1447a08851 | -4.2773 | -50.82292 | 2026-10-01 04:14:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 6f5bc666-24f9-3a94-aa69-33de85f1f843 | -4.27722 | -50.77462 | 2026-10-01 04:14:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 77.4 |
| 980ccdda-a84d-32a6-a36b-eb4057260238 | -9.2266 | -45.83729 | 2026-10-01 04:14:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| e864326a-3e31-3abd-8f18-bc3d25c6d760 | -4.27808 | -50.76984 | 2026-10-01 04:14:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 77.4 |
| a2974e89-f3a1-394a-8c3e-9f0a4ef56802 | -11.42604 | -43.41343 | 2026-10-01 04:14:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 9aed6567-385c-3551-ab84-0534826ad59b | -4.25125 | -50.78885 | 2026-10-01 04:14:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 78f57c3b-e361-3293-be4d-fab5d17f773e | -4.2974 | -50.76869 | 2026-10-01 04:14:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 9005e6ae-d4b6-3400-839c-e23a603cbbe3 | -4.27319 | -50.77251 | 2026-10-01 04:14:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 37.0 |
| c738d543-e713-33fa-919e-b1f8789a0648 | -11.34227 | -50.96971 | 2026-10-01 04:14:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 2f7e4889-511c-3875-9c24-2e74498c6869 | -11.1267 | -44.58998 | 2026-10-01 04:14:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 2f4be2ac-ab16-355c-a834-9309956934ed | -7.03018 | -45.28038 | 2026-10-01 04:14:00 | NPP-375D | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| a340a519-6abb-33c0-a6b4-01b62920253f | -7.32503 | -42.07543 | 2026-10-01 04:14:00 | NPP-375D | COLÔNIA DO PIAUÍ | PIAUÍ | Brasil | 2202778 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 7f1dc567-5564-38b2-82d6-77426bbaaa96 | -4.29995 | -50.75433 | 2026-10-01 04:14:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| b562878a-0c48-334e-9125-1529bd881527 | -11.838 | -44.7529 | 2026-10-01 04:14:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 209197ff-ff55-3bfa-aeea-65ecaae3ccc8 | -9.21611 | -50.68578 | 2026-10-01 04:14:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 4d5384b8-24ef-3c32-8579-017df5f92e14 | -4.63153 | -50.62085 | 2026-10-01 04:14:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 6.3 |
| b90adb75-3969-3655-afbe-c5a0ef765ab7 | -8.20252 | -45.50197 | 2026-10-01 04:14:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| e1a83e69-ffee-34c4-954a-640f705a7d7f | -12.56275 | -43.07303 | 2026-10-01 04:14:00 | NPP-375D | PARATINGA | BAHIA | Brasil | 2923704 | 29 | 33 | nan | nan | nan | Caatinga | 3.5 |
| 84dcb98a-9e27-32dd-b57e-dca19ae0e3c9 | -10.74564 | -50.5406 | 2026-10-01 04:14:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| bc595083-3cf1-3775-8101-f21c474fbd42 | -11.45929 | -43.45145 | 2026-10-01 04:14:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 9ece7363-f5d1-301e-a695-498cd201f830 | -11.17046 | -45.12518 | 2026-10-01 04:14:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 24ad27ff-d3d9-335f-9db2-f17f80f51309 | -5.366 | -46.22141 | 2026-10-01 04:14:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| da4fa674-4ec7-33fe-9719-54a0894f85a9 | -4.28963 | -50.82561 | 2026-10-01 04:14:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 99f87917-a65c-3d66-8948-bd49081eba08 | -10.84035 | -48.6988 | 2026-10-01 04:14:00 | NPP-375D | BREJINHO DE NAZARÉ | TOCANTINS | Brasil | 1703701 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 8d2cc026-c140-36b9-ba91-f483b9775b2e | -4.27399 | -50.76784 | 2026-10-01 04:14:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 19.8 |
| 6f05764f-e5ee-3d3f-a4c9-e5c53036695b | -8.63278 | -47.21799 | 2026-10-01 04:14:00 | NPP-375D | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 2fe3c7be-808f-3202-95c6-7b47e4c032ef | -4.63224 | -50.6184 | 2026-10-01 04:14:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 3914c3f2-36e8-32a2-9279-f6438dd28cdf | -5.7424 | -45.1534 | 2026-10-01 04:14:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 63d70de9-fd20-3366-8237-743b98d44408 | -8.84529 | -49.70792 | 2026-10-01 04:14:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| c8a0f820-4148-3762-81b9-ebdf630c8ec8 | -4.28104 | -50.8248 | 2026-10-01 04:14:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 7.0 |
| 9d810f26-75dd-3d51-b0e5-a6cb0ef4a019 | -8.32967 | -46.76035 | 2026-10-01 04:14:00 | NPP-375D | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 7d5d9f1a-dc73-3419-a995-7a898b713bdf | -6.73228 | -45.53645 | 2026-10-01 04:14:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 5c589ae8-d8cd-3690-b618-ebf03bd9d8d8 | -10.8507 | -48.69693 | 2026-10-01 04:14:00 | NPP-375D | BREJINHO DE NAZARÉ | TOCANTINS | Brasil | 1703701 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| a9efee06-e1b8-3327-9c5a-9b028666406d | -11.17749 | -45.10702 | 2026-10-01 04:14:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| da9fd498-c5ba-3d2a-aa8e-5101b648e3da | -9.20155 | -45.81072 | 2026-10-01 04:14:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| d297b87e-bf7e-30f4-bf0c-2198e0da9d01 | -5.89593 | -43.94431 | 2026-10-01 04:14:00 | NPP-375D | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 7faa38d4-66b1-3864-9a48-737592917c5d | -4.29421 | -50.82265 | 2026-10-01 04:14:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 6.6 |
| a6f404d9-1d41-3174-b3e8-5b35cc31b8dd | -11.45075 | -43.43784 | 2026-10-01 04:14:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 6.0 |
| c4a7cbb6-fbd8-3ffc-a025-5a151f63a898 | -6.01728 | -49.56226 | 2026-10-01 04:14:00 | NPP-375D | CURIONÓPOLIS | PARÁ | Brasil | 1502772 | 15 | 33 | nan | nan | nan | Amazônia | 15.7 |
| a95425c4-4be0-38ec-8b24-fcf7bdee3345 | -4.27966 | -50.73483 | 2026-10-01 04:14:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 51672fcf-c0d3-345b-93de-4ea8357f32bc | -4.26896 | -50.79711 | 2026-10-01 04:14:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 6.6 |
| b2cca909-de9d-38a4-a2bc-aff5546422e3 | -11.19099 | -45.11161 | 2026-10-01 04:14:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 16edb99c-ad03-3d75-8045-00d73529d4c3 | -4.26239 | -50.82177 | 2026-10-01 04:14:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 6416bf92-28cb-34ab-89a6-11d8236d48ea | -11.1813 | -45.10767 | 2026-10-01 04:14:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 8a2ac207-cac2-3ef7-bf0a-19b2b054c254 | -10.25546 | -49.67499 | 2026-10-01 04:14:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 07c6a103-336f-3a9f-8f24-2580e388eea9 | -4.88568 | -48.37459 | 2026-10-01 04:14:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 93846977-566f-310f-8931-b876edfb24b1 | -11.45839 | -43.43514 | 2026-10-01 04:14:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 4.2 |
| f8834c05-86c9-348c-a041-e5d30ee145ba | -4.26365 | -50.79089 | 2026-10-01 04:14:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 6.6 |
| f5f671c2-fcb8-3b0b-941c-b4372890e73e | -4.28953 | -50.75145 | 2026-10-01 04:14:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| e70da255-7278-3fda-920b-08b0e43688a0 | -9.96401 | -45.38772 | 2026-10-01 04:14:00 | NPP-375D | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 5f3f87eb-0b57-3132-b4e2-13dcc189b07d | -11.18893 | -45.10897 | 2026-10-01 04:14:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 1b8b026c-73b1-3f3a-a29e-b1eba6b59599 | -11.26335 | -43.52381 | 2026-10-01 04:14:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 9f989539-12ff-302a-b8c7-b4752ddfdcb5 | -8.985 | -44.17575 | 2026-10-01 04:14:00 | NPP-375D | SANTA LUZ | PIAUÍ | Brasil | 2209302 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 46657ce0-e827-30ae-be05-302ae3e2a602 | -4.28355 | -50.81067 | 2026-10-01 04:14:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 8.7 |
| fd84f9f4-706d-3b86-b822-de2633176155 | -8.85125 | -49.70557 | 2026-10-01 04:14:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| bf1589d2-070a-32fa-89ab-d232222be535 | -6.07534 | -53.30806 | 2026-10-01 04:14:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| d31950a4-ac86-3f8e-93e3-5f3002e8be9f | -4.28252 | -50.75524 | 2026-10-01 04:14:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 15.3 |
| 443d22c6-296e-3eaa-b0d3-0dad40205744 | -6.3321 | -51.12179 | 2026-10-01 04:14:00 | NPP-375D | PARAUAPEBAS | PARÁ | Brasil | 1505536 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 34223045-533e-3098-b45e-7d0311493c35 | -4.29907 | -50.75928 | 2026-10-01 04:14:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 345976f7-b661-3d6d-ad01-8bac10d77a17 | -12.52073 | -43.0929 | 2026-10-01 04:14:00 | NPP-375D | PARATINGA | BAHIA | Brasil | 2923704 | 29 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 2bad0336-411a-3055-b3a2-bd5d6af5c4bd | -11.38826 | -43.40291 | 2026-10-01 04:14:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 5.8 |
| ede2a821-2f27-3745-a70d-b63d6c15215e | -11.43369 | -43.41071 | 2026-10-01 04:14:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 20fde338-f767-3eca-8ea2-5fbeaca8f4f3 | -12.20455 | -43.83297 | 2026-10-01 04:14:00 | NPP-375D | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 2106666d-cde6-3560-b972-b7967144433f | -11.46344 | -43.44813 | 2026-10-01 04:14:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 482b44cb-2f32-3bd0-a030-5d8bb15c9fd2 | -4.28055 | -50.75604 | 2026-10-01 04:14:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 16.4 |
| 8452aa60-f346-3c88-9c88-1ae0f18d828a | -11.42539 | -43.41735 | 2026-10-01 04:14:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 197433a5-0045-3161-9fc3-1cab10a1b261 | -4.26697 | -50.77164 | 2026-10-01 04:14:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 37.0 |
| a577ae85-0f42-3aa6-94d3-2375672a94a7 | -4.28336 | -50.75033 | 2026-10-01 04:14:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 18583c16-24e3-3f52-8dff-9f5c0044a716 | -4.27555 | -50.75875 | 2026-10-01 04:14:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 15.3 |
| 4b176bf9-6c5b-365f-b0bd-dc6913158c42 | -9.21205 | -45.8234 | 2026-10-01 04:14:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 00af4c52-ae2c-394d-9a33-50969e7a7aa8 | -10.70965 | -45.3124 | 2026-10-01 04:14:00 | NPP-375D | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 7cc014a6-967d-326a-8ef2-092108279358 | -10.55203 | -50.04303 | 2026-10-01 04:14:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| abc5c719-479c-3525-a5a6-f3e53be7683a | -11.11776 | -44.5976 | 2026-10-01 04:14:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| a53b50fc-0b96-344d-ac89-ceb9949b39ec | -4.29573 | -50.77809 | 2026-10-01 04:14:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 13.7 |
| 18bfedd8-3229-381f-8a9e-005239218e15 | -10.72071 | -45.32073 | 2026-10-01 04:14:00 | NPP-375D | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| b4fcbbd1-c0c2-3d1c-bd5b-f341bc35cb60 | -4.27545 | -50.78455 | 2026-10-01 04:14:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 81.2 |
| fe5741ff-1044-36c9-9edd-e37013c2a2ce | -7.19238 | -46.54717 | 2026-10-01 04:14:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| bdf2e628-a296-3a9c-9fe8-09f76620df8d | -4.28525 | -50.80115 | 2026-10-01 04:14:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 0e8a9c0e-4380-309b-8de0-49d73f2c7d87 | -8.16719 | -47.14377 | 2026-10-01 04:14:00 | NPP-375D | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 7ee2e8ee-0cfa-315b-b137-5d8564246952 | -7.824 | -45.82354 | 2026-10-01 04:14:00 | NPP-375D | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 45303a26-1537-3f1b-a088-378a371b018d | -7.32442 | -42.07917 | 2026-10-01 04:14:00 | NPP-375D | COLÔNIA DO PIAUÍ | PIAUÍ | Brasil | 2202778 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 3709b47d-ad64-3843-a858-9a2e5f4acb80 | -9.38754 | -49.14926 | 2026-10-01 04:14:00 | NPP-375D | DOIS IRMÃOS DO TOCANTINS | TOCANTINS | Brasil | 1707207 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 1aa39581-d40c-30c5-8ca5-e0f9e38fd00b | -11.39905 | -51.0239 | 2026-10-01 04:14:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 3.8 |
| c66aca16-5d12-3812-973c-c8eb34e9da00 | -4.45699 | -47.92112 | 2026-10-01 04:14:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 13.8 |


[Clique aqui para ver as próximas entradas](README37.md)
