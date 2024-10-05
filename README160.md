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

## Dados Diários - Página 160

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 123d721e-aeef-3355-8951-fb7cd93c3261 | -6.99955 | -45.72879 | 2024-10-05 12:36:00 | TERRA_M-T | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 20.1 |
| f4209c93-f672-3a14-ba25-a7e2f7291132 | -6.99825 | -45.73773 | 2024-10-05 12:36:00 | TERRA_M-T | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 16.3 |
| 96972601-514b-3616-b411-87bc7be592fc | -6.76083 | -46.29095 | 2024-10-05 12:36:00 | TERRA_M-T | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 15.8 |
| 60e449cc-42da-3dae-81c0-599fa91107ed | -6.75179 | -46.28965 | 2024-10-05 12:36:00 | TERRA_M-T | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 11.7 |
| f7d6cd8b-3d0b-3063-9ea3-0913135b6826 | -6.67014 | -45.96616 | 2024-10-05 12:36:00 | TERRA_M-T | FORTALEZA DOS NOGUEIRAS | MARANHÃO | Brasil | 2104107 | 21 | 33 | nan | nan | nan | Cerrado | 8.3 |
| 6fe8f9f3-e82c-3ccb-bf21-6398cdd6a89a | -6.64667 | -45.30764 | 2024-10-05 12:36:00 | TERRA_M-T | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 13.5 |
| 73f86b1e-85f3-311a-95a0-72df919145f3 | -8.59379 | -46.49358 | 2024-10-05 12:36:00 | TERRA_M-T | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 17.2 |
| 535d3568-bcb1-3cc6-b729-5d90e3d3fe9a | -8.40085 | -46.29778 | 2024-10-05 12:36:00 | TERRA_M-T | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 21.6 |
| 6cf102bb-131e-3bc9-9c43-b7004e435861 | -9.9719 | -46.34235 | 2024-10-05 12:36:00 | TERRA_M-T | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 8.3 |
| dbd41f2a-d496-3cda-bd13-4caf5bce4aab | -9.97056 | -46.35142 | 2024-10-05 12:36:00 | TERRA_M-T | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 10.3 |
| b73b2efb-6005-3c77-8957-dcd8c3c8c5cb | -9.936 | -46.08274 | 2024-10-05 12:36:00 | TERRA_M-T | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 11.4 |
| 7980e160-a66c-37c7-ae00-5ae1b31d0787 | -9.93468 | -46.09173 | 2024-10-05 12:36:00 | TERRA_M-T | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 1a8d84c1-6285-3f1a-8f69-c583c2cb59da | -9.90164 | -47.18938 | 2024-10-05 12:36:00 | TERRA_M-T | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 12.2 |
| 62a8876e-e005-3180-aa5f-016b9d28d932 | -9.90023 | -47.19889 | 2024-10-05 12:36:00 | TERRA_M-T | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 29.2 |
| 9a2c1116-095f-3b6d-a9f0-fc209c9a2024 | -9.89253 | -47.18801 | 2024-10-05 12:36:00 | TERRA_M-T | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 21.4 |
| 1acae5e8-fa70-3d56-8a8b-c353f4c92365 | -9.89112 | -47.19749 | 2024-10-05 12:36:00 | TERRA_M-T | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 16.1 |
| b1b53862-b689-3a61-b9e1-d199ce040021 | -9.87289 | -47.19478 | 2024-10-05 12:36:00 | TERRA_M-T | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 8.3 |
| ee8710f2-97a6-3490-a47b-93007067ee6b | -9.86202 | -46.71038 | 2024-10-05 12:36:00 | TERRA_M-T | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 14.4 |
| 279afd3e-fa2e-3fe9-88fe-8d62e7333167 | -9.85304 | -46.70904 | 2024-10-05 12:36:00 | TERRA_M-T | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 37.3 |
| 57858073-9a65-3b5f-85d2-33f4ffccc6f7 | -9.85168 | -46.71821 | 2024-10-05 12:36:00 | TERRA_M-T | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 51.7 |
| e08615da-0879-38ed-b340-a4332729cea1 | -9.85033 | -46.72738 | 2024-10-05 12:36:00 | TERRA_M-T | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 16.9 |
| e51113ad-2677-37cb-8c46-0dc4dfc129ca | -9.84406 | -46.70772 | 2024-10-05 12:36:00 | TERRA_M-T | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 9.2 |
| e902b83f-29e1-3ed3-b313-d468116bb893 | -9.84271 | -46.71686 | 2024-10-05 12:36:00 | TERRA_M-T | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 44.0 |
| e2c5a9c5-acb0-3026-9b4e-fb46b4874fa1 | -9.78254 | -46.0571 | 2024-10-05 12:36:00 | TERRA_M-T | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 11.8 |
| 3ed0371e-6ef9-3724-b608-9bc486d3c964 | -9.55249 | -46.12135 | 2024-10-05 12:36:00 | TERRA_M-T | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 11.3 |
| c2c534a7-b1f9-3c60-bda6-e5decfe14190 | -10.77877 | -46.17884 | 2024-10-05 12:36:00 | TERRA_M-T | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 26.8 |
| c8c67488-a49c-387f-9cde-4c6627284215 | -10.7699 | -46.17756 | 2024-10-05 12:36:00 | TERRA_M-T | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 45.8 |
| 8cfdd81f-3a28-34ab-a898-a74f1b1cd2ee | -10.09585 | -46.56094 | 2024-10-05 12:36:00 | TERRA_M-T | SÃO FÉLIX DO TOCANTINS | TOCANTINS | Brasil | 1720150 | 17 | 33 | nan | nan | nan | Cerrado | 17.6 |
| c78aa710-7de9-3154-a5e3-120abe4112f3 | -12.04932 | -47.38181 | 2024-10-05 12:36:00 | TERRA_M-T | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 22.3 |
| 1f289afb-ceb2-3601-9b3b-15ddf2435351 | -12.04588 | -47.34309 | 2024-10-05 12:36:00 | TERRA_M-T | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 9.4 |
| 45c6f3d3-c757-340d-9783-703e3c088366 | -12.04028 | -47.38045 | 2024-10-05 12:36:00 | TERRA_M-T | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 18.3 |
| 680826c2-95d3-3667-83bc-58e4b1fca41f | -11.73201 | -46.91225 | 2024-10-05 12:36:00 | TERRA_M-T | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 34.8 |
| 4702ef62-eb0d-386b-b88e-339ae54c1942 | -11.73065 | -46.92141 | 2024-10-05 12:36:00 | TERRA_M-T | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 10.2 |
| c189d069-de13-3632-949b-3e7085af5e12 | -11.42231 | -47.1959 | 2024-10-05 12:36:00 | TERRA_M-T | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 12.3 |
| 7ff9d823-0e90-3551-a65c-4106e626d4ce | -11.38426 | -47.20331 | 2024-10-05 12:36:00 | TERRA_M-T | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 13.0 |
| ce927ba0-ae3f-3d65-9402-c6c3d25e108a | -11.38012 | -47.23126 | 2024-10-05 12:36:00 | TERRA_M-T | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 17.6 |
| 099c9468-368e-3367-b26f-9edca1063c0f | -11.37662 | -47.19262 | 2024-10-05 12:36:00 | TERRA_M-T | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 6.3 |
| eab1cd99-46cb-3f4d-8c40-21d268e81461 | -11.37524 | -47.20195 | 2024-10-05 12:36:00 | TERRA_M-T | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 36.8 |
| 9fb23a6d-3d37-33f8-8c9e-823630679e2a | -11.36622 | -47.20058 | 2024-10-05 12:36:00 | TERRA_M-T | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 43.7 |
| 3fc0ab12-9bbe-3d70-91db-329078e42d8e | -11.36483 | -47.20991 | 2024-10-05 12:36:00 | TERRA_M-T | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 30.0 |
| 567638e9-0ca3-30f1-b686-1740f3f26dda | -11.28683 | -46.80529 | 2024-10-05 12:36:00 | TERRA_M-T | RIO DA CONCEIÇÃO | TOCANTINS | Brasil | 1718659 | 17 | 33 | nan | nan | nan | Cerrado | 9.6 |
| d7abcc93-91ec-3574-a5d7-45471acc8347 | -11.26857 | -46.98998 | 2024-10-05 12:36:00 | TERRA_M-T | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 32.6 |
| 8325404f-624c-3356-807e-54cd5e9d852c | -11.2672 | -46.99916 | 2024-10-05 12:36:00 | TERRA_M-T | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 49.9 |
| 220fddf4-9860-322f-a365-69c8b8ca7b8a | -11.25863 | -46.61818 | 2024-10-05 12:36:00 | TERRA_M-T | RIO DA CONCEIÇÃO | TOCANTINS | Brasil | 1718659 | 17 | 33 | nan | nan | nan | Cerrado | 20.0 |
| 53d9013f-fdd3-3904-9483-6b2b2d1a10bf | -11.24971 | -46.61693 | 2024-10-05 12:36:00 | TERRA_M-T | RIO DA CONCEIÇÃO | TOCANTINS | Brasil | 1718659 | 17 | 33 | nan | nan | nan | Cerrado | 15.2 |
| 402cb8ba-f8a5-33f7-809b-5c58fbd57f6c | -11.2408 | -46.61565 | 2024-10-05 12:36:00 | TERRA_M-T | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 35.9 |
| d1d8f359-fdfe-3898-a8b6-8e752d12e190 | -11.23946 | -46.62475 | 2024-10-05 12:36:00 | TERRA_M-T | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 26.4 |
| 0f2dab26-42c5-3092-b983-55fd50b9eb4b | -11.22566 | -46.59488 | 2024-10-05 12:36:00 | TERRA_M-T | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 11.6 |
| 40ae5c25-f2a7-3686-9b9b-0fc4d02a6b37 | -11.1457 | -46.51197 | 2024-10-05 12:36:00 | TERRA_M-T | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 15.0 |
| 8f287493-cdd7-3409-b30f-9d4a89e4a39e | -9.8545 | -46.7257 | 2024-10-05 12:36:02 | GOES-16 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 96.3 |
| 3a22a18c-05bf-3307-b4bf-341ebdd2aaff | -10.2942 | -50.5147 | 2024-10-05 12:36:05 | GOES-16 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 77.6 |
| b7939e5a-e9f3-3e00-b51d-50e5009eef8d | -10.3131 | -50.5128 | 2024-10-05 12:36:05 | GOES-16 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 80.8 |
| afe01bc4-685c-3fd3-afce-6a8a8ee5a123 | -11.3368 | -45.5202 | 2024-10-05 12:36:10 | GOES-16 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 76.2 |
| bbe78b73-535d-3814-bdd4-e578bb53c153 | -11.3853 | -47.2088 | 2024-10-05 12:36:10 | GOES-16 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 58.0 |
| 4bcf0b07-f0a8-30f0-98ee-1fcd9ecb1d98 | -11.3665 | -47.1889 | 2024-10-05 12:36:10 | GOES-16 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 56.4 |
| 8fe266b5-9eec-3d04-b257-1aee403444cb | -11.3662 | -47.2113 | 2024-10-05 12:36:10 | GOES-16 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 67.2 |
| 72998d20-70eb-3113-8de2-431b9ca4fd25 | -11.7187 | -47.8107 | 2024-10-05 12:36:12 | GOES-16 | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 94.4 |
| afdc429e-5f1f-3f88-b43c-1c842efb8db7 | -11.6995 | -47.8131 | 2024-10-05 12:36:12 | GOES-16 | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 66.9 |
| 6c05c5f1-cb83-3a9e-8340-910fd99ea928 | -12.7815 | -50.5758 | 2024-10-05 12:36:18 | GOES-16 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 58.3 |
| a41d0f6b-ebcc-3630-b448-c6e35627b099 | -12.7623 | -50.5782 | 2024-10-05 12:36:18 | GOES-16 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 69.5 |
| 80949cce-0e55-3ac8-9916-6f93e447d0d7 | -13.1056 | -46.3321 | 2024-10-05 12:36:20 | GOES-16 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 83.1 |
| 42f5e9e7-540d-3369-a07b-a1d8c883d34d | -15.1826 | -48.0528 | 2024-10-05 12:36:31 | GOES-16 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 78.8 |
| 0b0c7c6d-ad20-34a4-9eca-fd5204ef9e37 | -15.1821 | -48.0754 | 2024-10-05 12:36:31 | GOES-16 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 54.5 |
| 19b873ba-76e6-3afd-b429-67e64aa0d7d5 | -16.9714 | -56.7852 | 2024-10-05 12:36:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 149.1 |
| eee55cf2-32d7-35a4-a97f-dddc227146d8 | -16.9717 | -56.7646 | 2024-10-05 12:36:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 153.3 |
| 07cc098c-ed7b-325a-aa47-d4414c20112a | -16.9913 | -56.7622 | 2024-10-05 12:36:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 126.7 |
| 446c71e8-deb9-3a83-949e-43c33c6b0880 | -17.0113 | -56.7392 | 2024-10-05 12:36:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 79.2 |
| ea737f66-cffe-3aa5-85df-bbe2798ebbb2 | -17.1085 | -56.7892 | 2024-10-05 12:36:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 111.8 |
| 6d6fb274-29fd-37ea-bd10-700c8eae69f0 | -17.0888 | -56.7915 | 2024-10-05 12:36:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 97.1 |
| f7866d4c-6c68-30e7-aec5-66e7fbc4240d | -17.1378 | -57.4016 | 2024-10-05 12:36:43 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 238.1 |
| a800f86c-1724-3db9-8c7a-d09e712ea697 | -17.1185 | -57.3834 | 2024-10-05 12:36:43 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 80.2 |
| 729f1f7a-9e6f-3ded-9c7c-5ea7071a1829 | -18.6586 | -57.2759 | 2024-10-05 12:36:51 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 131.2 |
| fe82af45-bdad-3a5b-af4c-08af8c193e6d | -18.6981 | -57.2915 | 2024-10-05 12:36:51 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 71.3 |
| fac05e97-66e6-31f5-b6a0-c84037299ca0 | -18.6984 | -57.2708 | 2024-10-05 12:36:51 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 95.3 |
| e440f514-27f3-3e6d-a534-552d46c00dc3 | -18.6785 | -57.2734 | 2024-10-05 12:36:51 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 163.4 |
| 8302a270-97a3-31d9-a327-73fb602b1494 | -17.11652 | -51.73305 | 2024-10-05 12:38:00 | TERRA_M-T | CAIAPÔNIA | GOIÁS | Brasil | 5204409 | 52 | 33 | nan | nan | nan | Cerrado | 12.1 |
| b9319506-b42d-33b0-9469-de2759a73faa | -12.6665 | -54.03916 | 2024-10-05 12:38:00 | TERRA_M-T | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 50.7 |
| c4e2ca46-598d-30d5-bd9b-72ce79bdc376 | -12.62885 | -53.1071 | 2024-10-05 12:38:00 | TERRA_M-T | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 159.5 |
| 12f53157-df3b-3451-9318-c5de054d4e77 | -12.61218 | -53.12587 | 2024-10-05 12:38:00 | TERRA_M-T | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 58.5 |
| 58a1cb52-213d-3c09-9ded-5323a9632e19 | -12.60242 | -53.1172 | 2024-10-05 12:38:00 | TERRA_M-T | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 34.0 |
| 24e9fb88-5408-3891-9309-8b273ce3f514 | -12.59909 | -53.12364 | 2024-10-05 12:38:00 | TERRA_M-T | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 34.4 |
| 2080a111-a209-3d6e-9e95-c7db669f2df2 | -17.65364 | -54.6491 | 2024-10-05 12:38:00 | TERRA_M-T | SONORA | MATO GROSSO DO SUL | Brasil | 5007935 | 50 | 33 | nan | nan | nan | Cerrado | 16.9 |
| b11f5b70-db17-3a6f-9edd-2ef615e32d46 | -16.87993 | -54.81208 | 2024-10-05 12:38:00 | TERRA_M-T | RONDONÓPOLIS | MATO GROSSO | Brasil | 5107602 | 51 | 33 | nan | nan | nan | Cerrado | 38.7 |
| 3726b2e5-ef1e-32ef-a4d9-9532c672b459 | -16.87544 | -54.83606 | 2024-10-05 12:38:00 | TERRA_M-T | RONDONÓPOLIS | MATO GROSSO | Brasil | 5107602 | 51 | 33 | nan | nan | nan | Cerrado | 171.7 |
| 0eea1d0c-e931-35b0-bd91-d73cddbc0541 | -16.8697 | -54.8281 | 2024-10-05 12:38:00 | TERRA_M-T | RONDONÓPOLIS | MATO GROSSO | Brasil | 5107602 | 51 | 33 | nan | nan | nan | Cerrado | 207.0 |
| d6db3e33-9a8d-3386-9cd1-8a9bccecd04c | -16.86549 | -54.85139 | 2024-10-05 12:38:00 | TERRA_M-T | RONDONÓPOLIS | MATO GROSSO | Brasil | 5107602 | 51 | 33 | nan | nan | nan | Cerrado | 27.3 |
| 3a891cc3-b6e9-3ca5-b4f8-96fbfcd784cf | -17.08114 | -56.67122 | 2024-10-05 12:38:00 | TERRA_M-T | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 39.6 |
| c596243f-4efa-3a72-a005-a499f96585b3 | -16.93158 | -55.83358 | 2024-10-05 12:38:00 | TERRA_M-T | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 38.6 |
| 156b8fc6-a063-32de-98fc-848ed8ce7d0f | -16.91777 | -55.82383 | 2024-10-05 12:38:00 | TERRA_M-T | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 32.9 |
| 73671e15-95d0-35e9-9f9f-41ca20c389d5 | -16.91684 | -55.83062 | 2024-10-05 12:38:00 | TERRA_M-T | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 37.7 |
| 56813f47-12c6-33e8-aa67-35a2680bbd03 | -16.6761 | -55.56027 | 2024-10-05 12:38:00 | TERRA_M-T | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 50.0 |
| 5b0f5b73-9644-3f22-bbef-ac996c88e609 | -16.67539 | -55.55407 | 2024-10-05 12:38:00 | TERRA_M-T | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 63.8 |
| caecb977-eff6-3724-a01d-0d312f14c8a5 | -16.55757 | -57.21641 | 2024-10-05 12:38:00 | TERRA_M-T | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 49.4 |
| 46d91803-d8ca-3578-a677-7ed485d33585 | -16.55199 | -57.20964 | 2024-10-05 12:38:00 | TERRA_M-T | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 35.4 |
| e352feff-6d0a-3a47-a8b9-a9e4c57470ac | -17.17875 | -57.38667 | 2024-10-05 12:38:00 | TERRA_M-T | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 65.2 |
| ef4ba103-00fa-3684-b04a-b0d156f23313 | -17.13893 | -57.4164 | 2024-10-05 12:38:00 | TERRA_M-T | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 231.7 |
| ed9bec22-e1d3-3bc8-b8ca-9a9010adb4d7 | -17.12724 | -57.42145 | 2024-10-05 12:38:00 | TERRA_M-T | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 217.5 |
| bab5039b-7a33-34ae-8b9e-81fafc432eac | -17.12251 | -57.41292 | 2024-10-05 12:38:00 | TERRA_M-T | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 234.1 |
| c6280c8d-cc23-3a5d-bae7-0eada6dafb09 | -17.11794 | -56.78854 | 2024-10-05 12:38:00 | TERRA_M-T | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 156.6 |
| 683415ed-bd06-3cdd-8fdf-134547856dc9 | -17.10954 | -56.77945 | 2024-10-05 12:38:00 | TERRA_M-T | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 78.9 |


[Clique aqui para ver as próximas entradas](README161.md)
