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
| 1af3030a-eeda-3845-92c2-d1bc73fc40cd | -8.9418 | -44.24239 | 2025-02-25 04:33:00 | NPP-375D | SANTA LUZ | PIAUÍ | Brasil | 2209302 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 37c8c11d-6ff9-3bb7-810c-a0c670265963 | -8.94565 | -44.24298 | 2025-02-25 04:33:00 | NPP-375D | SANTA LUZ | PIAUÍ | Brasil | 2209302 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| d91527ed-80ad-3dc4-ae9f-6631284b6d8d | -8.93863 | -44.23703 | 2025-02-25 04:33:00 | NPP-375D | SANTA LUZ | PIAUÍ | Brasil | 2209302 | 22 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 563eb0b8-bd0a-3800-aee4-25432ccc409a | -11.00773 | -44.65157 | 2025-02-25 04:33:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 96fa730f-809f-3a1e-83c3-7ff3e60433d6 | -12.66632 | -44.50754 | 2025-02-25 04:33:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 5eadae55-9862-393b-93f5-df449a0d0a2f | -8.93719 | -44.23987 | 2025-02-25 04:33:00 | NPP-375D | SANTA LUZ | PIAUÍ | Brasil | 2209302 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 4800b343-7a50-348d-9840-1f4858547de8 | -12.55534 | -44.7222 | 2025-02-25 04:33:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 4.1 |
| d486416c-ccf7-33b4-a97f-a39bb8993df6 | -20.54844 | -45.93964 | 2025-02-25 04:36:00 | NPP-375D | PIMENTA | MINAS GERAIS | Brasil | 3150505 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 1e4f33c6-caaa-3434-b27d-8698028d1a69 | -20.54887 | -45.93613 | 2025-02-25 04:36:00 | NPP-375D | PIMENTA | MINAS GERAIS | Brasil | 3150505 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| bbeb9e27-6b09-34a7-b7f3-e6bf3ad01501 | -20.54526 | -45.93202 | 2025-02-25 04:36:00 | NPP-375D | PIUMHI | MINAS GERAIS | Brasil | 3151503 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| a7a30d50-fea0-3958-b96c-294fbbdcdea1 | -19.67997 | -44.05144 | 2025-02-25 04:36:00 | NPP-375D | PEDRO LEOPOLDO | MINAS GERAIS | Brasil | 3149309 | 31 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 5f48edef-d010-3eae-83ff-1cc6437b47dd | -19.67966 | -44.04999 | 2025-02-25 04:36:00 | NPP-375D | PEDRO LEOPOLDO | MINAS GERAIS | Brasil | 3149309 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 39d40cb6-4fcc-3029-bb11-9cd38b5af97d | -20.54932 | -45.93255 | 2025-02-25 04:36:00 | NPP-375D | PIMENTA | MINAS GERAIS | Brasil | 3150505 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 5e317879-160f-383e-891e-19cd16382637 | -20.54482 | -45.93554 | 2025-02-25 04:36:00 | NPP-375D | PIUMHI | MINAS GERAIS | Brasil | 3151503 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 40e93717-9fad-35fe-98ac-6d141a9a47d5 | -16.34653 | -43.70041 | 2025-02-25 04:36:00 | NPP-375D | CAPITÃO ENÉAS | MINAS GERAIS | Brasil | 3112703 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 39338436-1c7c-3cc5-b69f-0f57ae1a3b81 | -15.88576 | -43.45612 | 2025-02-25 04:36:00 | NPP-375D | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 64.3 |
| 4201ecd1-d609-3d39-b949-fab949a79a1a | -16.67892 | -43.89111 | 2025-02-25 04:36:00 | NPP-375D | MONTES CLAROS | MINAS GERAIS | Brasil | 3143302 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 9578d721-48f4-347a-8181-23af8772631c | -15.89469 | -43.45739 | 2025-02-25 04:36:00 | NPP-375D | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 0afc5216-afbe-32cd-b1f6-e2978fe645d5 | -16.56844 | -41.44929 | 2025-02-25 04:36:00 | NPP-375D | ITAOBIM | MINAS GERAIS | Brasil | 3133303 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 067a7d5e-d23f-39bc-8379-89b2564933e4 | -15.89081 | -43.45224 | 2025-02-25 04:36:00 | NPP-375D | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 64.3 |
| bd2a74f8-9795-379d-9b76-ac76c15348cd | -16.56807 | -41.45264 | 2025-02-25 04:36:00 | NPP-375D | ITAOBIM | MINAS GERAIS | Brasil | 3133303 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 5914f5f8-ff30-3076-bc3a-126d50d09c3b | -15.88964 | -43.46127 | 2025-02-25 04:36:00 | NPP-375D | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 88.3 |
| c4a57628-e289-3953-884c-f693e5d0033a | -22.89207 | -42.71786 | 2025-02-25 04:38:00 | NPP-375D | MARICÁ | RIO DE JANEIRO | Brasil | 3302700 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 9027930c-81e9-3aa8-bd3a-94cb49a0987c | -22.20677 | -56.96727 | 2025-02-25 04:38:00 | NPP-375D | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 100b60a6-853f-32bb-9eb7-80b88ca4f58d | -22.89726 | -42.71812 | 2025-02-25 04:38:00 | NPP-375D | MARICÁ | RIO DE JANEIRO | Brasil | 3302700 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 8d068bf6-05f7-325b-9cfd-c994a4c7c751 | -22.7872 | -43.75691 | 2025-02-25 04:38:00 | NPP-375D | SEROPÉDICA | RIO DE JANEIRO | Brasil | 3305554 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| e0b2dd15-d03f-3c82-9b12-c79032d8f8c1 | -21.1954 | -44.93896 | 2025-02-25 04:38:00 | NPP-375D | IJACI | MINAS GERAIS | Brasil | 3130408 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 6cf1a5d1-0df8-32b9-afcf-c0ff3a188af2 | -21.31459 | -44.22003 | 2025-02-25 04:38:00 | NPP-375D | SÃO JOÃO DEL REI | MINAS GERAIS | Brasil | 3162500 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| c2966aac-f1d1-3e4a-b975-fe5b9a2774b0 | -23.594 | -47.43721 | 2025-02-25 04:38:00 | NPP-375D | VOTORANTIM | SÃO PAULO | Brasil | 3557006 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 7c6aa52e-20ce-3ff2-8ce0-535c976a74d5 | -23.02543 | -48.43778 | 2025-02-25 04:38:00 | NPP-375D | BOTUCATU | SÃO PAULO | Brasil | 3507506 | 35 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 5c4ae16a-cad8-3bb1-beaa-c8b93fae53eb | -21.16113 | -48.56289 | 2025-02-25 04:38:00 | NPP-375D | TAIAÇU | SÃO PAULO | Brasil | 3553104 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 6431858c-d5d2-3d5a-8f42-2a06d65728c0 | -24.24324 | -50.74064 | 2025-02-25 04:38:00 | NPP-375D | ORTIGUEIRA | PARANÁ | Brasil | 4117305 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 8849a1cd-6fd2-322d-91cb-0b038deb56ca | -23.33995 | -46.7725 | 2025-02-25 04:38:00 | NPP-375D | CAIEIRAS | SÃO PAULO | Brasil | 3509007 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 8aefda42-fadd-3776-ba9b-2371ba2affde | -15.8955 | -43.4523 | 2025-02-25 04:40:00 | GOES-16 | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 109.1 |
| 46f725d8-aae6-33b2-acf1-3e6a93334ea7 | 2.7432 | -61.2624 | 2025-02-25 04:40:00 | GOES-16 | ALTO ALEGRE | RORAIMA | Brasil | 1400050 | 14 | 33 | nan | nan | nan | Amazônia | 65.1 |
| 6739a785-28b7-3b84-8526-2ea232dd76db | 2.7249 | -61.2627 | 2025-02-25 04:40:00 | GOES-16 | ALTO ALEGRE | RORAIMA | Brasil | 1400050 | 14 | 33 | nan | nan | nan | Amazônia | 38.0 |
| 04be359c-b84b-3881-b307-3f5b66dd5242 | 2.7431 | -61.2813 | 2025-02-25 04:40:00 | GOES-16 | ALTO ALEGRE | RORAIMA | Brasil | 1400050 | 14 | 33 | nan | nan | nan | Amazônia | 80.1 |
| b491007b-bb56-3413-ad43-6ef8048c7534 | 2.7249 | -61.2816 | 2025-02-25 04:40:00 | GOES-16 | ALTO ALEGRE | RORAIMA | Brasil | 1400050 | 14 | 33 | nan | nan | nan | Amazônia | 48.6 |
| a2fd44c8-37f7-3b78-a4fc-d62ec17c096e | -15.8757 | -43.4566 | 2025-02-25 04:40:00 | GOES-16 | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 69.0 |
| 09630248-1658-3ec1-ba57-aaa8d3f431fc | -30.14912 | -51.8763 | 2025-02-25 04:40:00 | NPP-375D | BUTIÁ | RIO GRANDE DO SUL | Brasil | 4302709 | 43 | 33 | nan | nan | nan | Pampa | 0.8 |
| 8964bb88-cd2c-36ab-8928-69f59b57d33c | -30.14851 | -51.88054 | 2025-02-25 04:40:00 | NPP-375D | BUTIÁ | RIO GRANDE DO SUL | Brasil | 4302709 | 43 | 33 | nan | nan | nan | Pampa | 1.3 |
| 99051050-1121-3bf2-aad9-f15e1c719e29 | -28.89894 | -50.89268 | 2025-02-25 04:40:00 | NPP-375D | CAXIAS DO SUL | RIO GRANDE DO SUL | Brasil | 4305108 | 43 | 33 | nan | nan | nan | Mata Atlântica | 3.2 |
| dc10c42e-2127-3e46-bebf-6f5551082a4c | -28.58696 | -49.44136 | 2025-02-25 04:40:00 | NPP-375D | SIDERÓPOLIS | SANTA CATARINA | Brasil | 4217600 | 42 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 09535343-f361-3769-8ff1-b01cd67d3a8d | -30.1479 | -51.87939 | 2025-02-25 04:40:00 | NPP-375D | BUTIÁ | RIO GRANDE DO SUL | Brasil | 4302709 | 43 | 33 | nan | nan | nan | Pampa | 1.9 |
| d94b95f8-9dc5-3dcf-8855-fd4b6eae65df | -8.06814 | -34.97834 | 2025-02-25 04:44:00 | AQUA_M-M | RECIFE | PERNAMBUCO | Brasil | 2611606 | 26 | 33 | nan | nan | nan | Mata Atlântica | 9.7 |
| de4f17e3-e789-3d8b-8f5b-61892290e6b4 | -8.06952 | -34.96934 | 2025-02-25 04:44:00 | AQUA_M-M | RECIFE | PERNAMBUCO | Brasil | 2611606 | 26 | 33 | nan | nan | nan | Mata Atlântica | 9.8 |
| a8faa679-65c3-3007-9e4d-25b2efe8b512 | -15.89067 | -43.45645 | 2025-02-25 04:46:00 | AQUA_M-M | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 202.4 |
| 373d863b-2aee-38b9-8e2b-4fc2d30ad786 | -15.88154 | -43.47186 | 2025-02-25 04:46:00 | AQUA_M-M | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 35.4 |
| 1b7772c2-774b-3d97-a652-2bff280bbaec | -15.88588 | -43.44784 | 2025-02-25 04:46:00 | AQUA_M-M | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 201.5 |
| 3d6339f0-389e-3b6e-91f3-ccaf325a0c98 | -15.89517 | -43.43248 | 2025-02-25 04:46:00 | AQUA_M-M | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 33.3 |
| ec10a1d2-1529-3561-bc03-1fe42a85a880 | 2.7432 | -61.2624 | 2025-02-25 04:50:00 | GOES-16 | ALTO ALEGRE | RORAIMA | Brasil | 1400050 | 14 | 33 | nan | nan | nan | Amazônia | 65.8 |
| 082aa314-8e4a-3887-a427-09f60bb2aaed | 2.7431 | -61.2813 | 2025-02-25 04:50:00 | GOES-16 | ALTO ALEGRE | RORAIMA | Brasil | 1400050 | 14 | 33 | nan | nan | nan | Amazônia | 85.6 |
| 9e8ff26d-d6be-3707-a78e-e25030ac70fe | 2.7249 | -61.2816 | 2025-02-25 04:50:00 | GOES-16 | ALTO ALEGRE | RORAIMA | Brasil | 1400050 | 14 | 33 | nan | nan | nan | Amazônia | 46.8 |
| d96cf147-db09-313c-b889-c560259d4179 | -15.8757 | -43.4566 | 2025-02-25 04:50:00 | GOES-16 | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 66.8 |
| 641305ba-43a2-3b78-873d-49a7151231f3 | -15.8955 | -43.4523 | 2025-02-25 04:50:00 | GOES-16 | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 101.7 |
| dd72ef34-1180-3551-8226-400e8cd043df | 2.7249 | -61.2627 | 2025-02-25 04:50:00 | GOES-16 | ALTO ALEGRE | RORAIMA | Brasil | 1400050 | 14 | 33 | nan | nan | nan | Amazônia | 42.9 |
| cb19a8a9-d654-3803-bca8-1a087dcf0d09 | 2.73262 | -61.27631 | 2025-02-25 04:53:00 | NOAA-20 | ALTO ALEGRE | RORAIMA | Brasil | 1400050 | 14 | 33 | nan | nan | nan | Amazônia | 12.0 |
| 3e1dcb90-7ea3-3032-908d-a509f99e206c | 2.73847 | -61.27888 | 2025-02-25 04:53:00 | NOAA-20 | ALTO ALEGRE | RORAIMA | Brasil | 1400050 | 14 | 33 | nan | nan | nan | Amazônia | 10.9 |
| cd8486c6-fe27-3ca6-a180-29f5ad4d1ea0 | 2.73313 | -61.27966 | 2025-02-25 04:53:00 | NOAA-20 | ALTO ALEGRE | RORAIMA | Brasil | 1400050 | 14 | 33 | nan | nan | nan | Amazônia | 10.9 |
| 4b3e475f-7800-3746-8502-a7c9c0ba3dd3 | 2.73797 | -61.27554 | 2025-02-25 04:53:00 | NOAA-20 | ALTO ALEGRE | RORAIMA | Brasil | 1400050 | 14 | 33 | nan | nan | nan | Amazônia | 12.0 |
| bdc0b6c6-bb10-3a03-8e80-99a3930415c4 | 1.33342 | -60.72694 | 2025-02-25 04:53:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 8d25ab48-4141-338d-ab90-7a3f7d2b923d | -8.93729 | -44.24084 | 2025-02-25 04:55:00 | NOAA-20 | SANTA LUZ | PIAUÍ | Brasil | 2209302 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| e46b348b-66ab-30ba-83b9-6d3c911bcda9 | -8.94313 | -44.24169 | 2025-02-25 04:55:00 | NOAA-20 | SANTA LUZ | PIAUÍ | Brasil | 2209302 | 22 | 33 | nan | nan | nan | Cerrado | 0.6 |
| bee69aff-850c-3f43-bbaf-5ac7bc71761b | -8.11158 | -43.14243 | 2025-02-25 04:55:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 85c177c6-f9d9-3687-81d6-17cdac7f3f11 | 4.52465 | -60.99395 | 2025-02-25 04:55:00 | NOAA-20 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 12eab9c6-5a01-30d3-ae80-0d68be0927d9 | -8.11221 | -43.13758 | 2025-02-25 04:55:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| e9d331f1-1661-37e0-b930-d6cc1aa62eee | 4.52421 | -60.99095 | 2025-02-25 04:55:00 | NOAA-20 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 8f09e056-048b-3b35-80e7-fe1f960c6a65 | -8.37449 | -43.97035 | 2025-02-25 04:55:00 | NOAA-20 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 9289b5ff-a418-362a-85ee-32e9aca61414 | -12.55867 | -44.72161 | 2025-02-25 04:57:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 7c81ba0b-2d52-38d8-b4ad-0e0ada7cb6a8 | -12.55273 | -44.72086 | 2025-02-25 04:57:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| fee7669b-f547-39e9-974f-349fceeb221a | -12.5507 | -44.73849 | 2025-02-25 04:57:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| cfc9ea75-177d-3a50-9000-b0717bf714b1 | -12.55663 | -44.73932 | 2025-02-25 04:57:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| d07d47ac-a8f5-3521-9805-82b1e51edfdd | -12.55222 | -44.72528 | 2025-02-25 04:57:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| c55f33a2-c0d5-38f9-a0ff-44901badd111 | -15.88373 | -43.46113 | 2025-02-25 04:57:00 | NOAA-20 | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 5a0f7bc8-5a82-3af7-aba2-9240db9c595a | -15.89097 | -43.45603 | 2025-02-25 04:57:00 | NOAA-20 | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 39.5 |
| 7e975011-7bc4-3de6-9799-49874cca6ca3 | -12.55816 | -44.72604 | 2025-02-25 04:57:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 6e451123-7834-3664-a6c3-2513ba078077 | -11.15081 | -54.3078 | 2025-02-25 04:57:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ce505d1a-5be0-3652-bacd-add7111ceea1 | -12.54913 | -44.72246 | 2025-02-25 04:57:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 68077f94-9891-3207-b708-5e265f3acd87 | -15.88981 | -43.4678 | 2025-02-25 04:57:00 | NOAA-20 | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 17.3 |
| 6eb4c969-5af1-3c56-b2b9-65ad060ae37c | -10.68114 | -54.33972 | 2025-02-25 04:57:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 5e157b28-5ac1-3a59-b261-5107b0ff7d3c | -15.89039 | -43.46191 | 2025-02-25 04:57:00 | NOAA-20 | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 39.5 |
| 68a6948b-2fea-3ad8-aa86-228c6ec68860 | -15.64075 | -59.71494 | 2025-02-25 04:57:00 | NOAA-20 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 520d28aa-7521-30c1-a609-ec5f4a23f5e1 | -20.5444 | -45.93144 | 2025-02-25 04:59:00 | NOAA-20 | PIUMHI | MINAS GERAIS | Brasil | 3151503 | 31 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 9b20272b-ecfe-367c-b21d-60990e977cb3 | -21.82966 | -57.55311 | 2025-02-25 04:59:00 | NOAA-20 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 0.5 |
| dee367eb-7922-3af6-a85f-272ff86d02ab | -20.54588 | -45.93419 | 2025-02-25 04:59:00 | NOAA-20 | PIUMHI | MINAS GERAIS | Brasil | 3151503 | 31 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 077eba0f-be88-31b3-8f6f-621f4b5090d7 | -20.54402 | -45.93543 | 2025-02-25 04:59:00 | NOAA-20 | PIUMHI | MINAS GERAIS | Brasil | 3151503 | 31 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 54cb948a-740f-3f1c-b9e1-3c44191a7462 | -21.83024 | -57.5494 | 2025-02-25 04:59:00 | NOAA-20 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 8ad4c84e-71e9-33ce-80b3-5192ce51954d | -21.83298 | -57.5537 | 2025-02-25 04:59:00 | NOAA-20 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 0.5 |
| fbe6a703-1674-3662-ba96-7f1b96a9a3d0 | 2.7249 | -61.2627 | 2025-02-25 05:00:00 | GOES-16 | ALTO ALEGRE | RORAIMA | Brasil | 1400050 | 14 | 33 | nan | nan | nan | Amazônia | 37.2 |
| 424706d8-3fff-3462-9e0f-f1c7096f672a | 2.7432 | -61.2624 | 2025-02-25 05:00:00 | GOES-16 | ALTO ALEGRE | RORAIMA | Brasil | 1400050 | 14 | 33 | nan | nan | nan | Amazônia | 55.0 |
| 3dc29baf-ca39-3cb9-80c3-653f247986a9 | 2.7249 | -61.2816 | 2025-02-25 05:00:00 | GOES-16 | ALTO ALEGRE | RORAIMA | Brasil | 1400050 | 14 | 33 | nan | nan | nan | Amazônia | 41.1 |
| 12a8bea5-33e7-3dab-ac11-3d647dc4b3f6 | 2.7431 | -61.2813 | 2025-02-25 05:00:00 | GOES-16 | ALTO ALEGRE | RORAIMA | Brasil | 1400050 | 14 | 33 | nan | nan | nan | Amazônia | 69.7 |
| 7acb24be-9e57-3938-b323-2e00193d8de9 | -15.8955 | -43.4523 | 2025-02-25 05:00:00 | GOES-16 | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 95.8 |
| 4491cf57-fcfb-3d3e-be59-623b94fabc25 | -28.90098 | -50.89275 | 2025-02-25 05:01:00 | NOAA-20 | CAXIAS DO SUL | RIO GRANDE DO SUL | Brasil | 4305108 | 43 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| b04f2357-3ebd-3776-b355-38e41f1960ab | -30.14765 | -51.87997 | 2025-02-25 05:01:00 | NOAA-20 | BUTIÁ | RIO GRANDE DO SUL | Brasil | 4302709 | 43 | 33 | nan | nan | nan | Pampa | 1.5 |
| 4471486d-dd0c-3ff9-8b5f-092f31aeac4f | 2.7431 | -61.2813 | 2025-02-25 05:10:00 | GOES-16 | ALTO ALEGRE | RORAIMA | Brasil | 1400050 | 14 | 33 | nan | nan | nan | Amazônia | 60.8 |
| 3d96214b-826e-3f0b-b411-3ccb63b34366 | 2.7249 | -61.2816 | 2025-02-25 05:10:00 | GOES-16 | ALTO ALEGRE | RORAIMA | Brasil | 1400050 | 14 | 33 | nan | nan | nan | Amazônia | 39.4 |
| b8b2ecfd-4e89-3ba9-a4f2-f7d044c66629 | 2.7249 | -61.2627 | 2025-02-25 05:10:00 | GOES-16 | ALTO ALEGRE | RORAIMA | Brasil | 1400050 | 14 | 33 | nan | nan | nan | Amazônia | 36.3 |
| ebd9f71b-25d1-309c-aa39-e4547298edc9 | 2.7432 | -61.2624 | 2025-02-25 05:10:00 | GOES-16 | ALTO ALEGRE | RORAIMA | Brasil | 1400050 | 14 | 33 | nan | nan | nan | Amazônia | 48.7 |
| b81a373b-7d67-3992-baab-62f47aa64869 | 2.7431 | -61.2813 | 2025-02-25 05:20:00 | GOES-16 | ALTO ALEGRE | RORAIMA | Brasil | 1400050 | 14 | 33 | nan | nan | nan | Amazônia | 47.3 |


[Clique aqui para ver as próximas entradas](README5.md)
