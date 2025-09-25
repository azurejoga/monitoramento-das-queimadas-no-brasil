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

## Dados Diários - Página 7

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 6e409329-11c6-3738-b878-f08f442e8084 | -7.38765 | -39.64351 | 2025-09-25 03:19:00 | NPP-375D | EXU | PERNAMBUCO | Brasil | 2605301 | 26 | 33 | nan | nan | nan | Caatinga | 1.0 |
| d71ce01b-e850-3217-a402-dba36f3617ea | -6.41827 | -43.08875 | 2025-09-25 03:19:00 | NPP-375D | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 30.3 |
| ac3c2182-0674-3cc8-8ea3-dfa92684fb2d | -6.41609 | -43.09982 | 2025-09-25 03:19:00 | NPP-375D | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 20.4 |
| e471e083-a9db-369c-a1f1-412ecfa863f3 | -6.41029 | -43.0906 | 2025-09-25 03:19:00 | NPP-375D | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 62433d02-e4c2-3d62-94e5-2254f57ff949 | -6.56015 | -42.06474 | 2025-09-25 03:19:00 | NPP-375D | BARRA D'ALCÂNTARA | PIAUÍ | Brasil | 2201176 | 22 | 33 | nan | nan | nan | Caatinga | 8.2 |
| ce0d12af-da33-3703-9466-c2cf088ea2a8 | -9.48829 | -40.35617 | 2025-09-25 03:19:00 | NPP-375D | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 1.5 |
| db58e336-8b57-3baf-bbfa-bc8c0d033fa8 | -5.08861 | -37.60635 | 2025-09-25 03:19:00 | NPP-375D | BARAÚNA | RIO GRANDE DO NORTE | Brasil | 2401453 | 24 | 33 | nan | nan | nan | Caatinga | 1.8 |
| e5c0633e-7573-371e-8bd0-1a088a3dfe59 | -6.55886 | -42.07233 | 2025-09-25 03:19:00 | NPP-375D | BARRA D'ALCÂNTARA | PIAUÍ | Brasil | 2201176 | 22 | 33 | nan | nan | nan | Caatinga | 3.6 |
| 641b9b5c-a0c7-374b-80d6-3bd9fecdb03d | -6.42403 | -43.09785 | 2025-09-25 03:19:00 | NPP-375D | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 30.3 |
| 2985e74a-d89d-3cb4-8292-7b4c4b435e65 | -3.8085 | -41.55669 | 2025-09-25 03:19:00 | NPP-375D | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 3.6 |
| e2536dd2-bfc0-3e28-910c-c45b5760cc38 | -9.6584 | -40.5887 | 2025-09-25 03:19:00 | NPP-375D | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 14.0 |
| 741700df-1005-3d5d-aef5-7c06eb65ccef | -5.09156 | -37.60691 | 2025-09-25 03:19:00 | NPP-375D | BARAÚNA | RIO GRANDE DO NORTE | Brasil | 2401453 | 24 | 33 | nan | nan | nan | Caatinga | 1.8 |
| ff10a235-2026-3637-ae24-e3c694072995 | -6.42768 | -43.07824 | 2025-09-25 03:19:00 | NPP-375D | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 13.2 |
| 0b610c53-2900-323d-81c5-bbaaf2860827 | -6.42555 | -43.09003 | 2025-09-25 03:19:00 | NPP-375D | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 30.3 |
| 0e2339c4-f1ae-35fc-9d93-b24ecec79ec1 | -9.48911 | -40.35188 | 2025-09-25 03:19:00 | NPP-375D | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 962ea6fc-e466-34dc-b4fd-25911d5fba64 | -8.84471 | -42.47646 | 2025-09-25 03:19:00 | NPP-375D | CORONEL JOSÉ DIAS | PIAUÍ | Brasil | 2202851 | 22 | 33 | nan | nan | nan | Caatinga | 5.1 |
| 5016d3c9-d35c-373e-8af4-c5dffebee1d9 | -6.56692 | -42.06721 | 2025-09-25 03:19:00 | NPP-375D | BARRA D'ALCÂNTARA | PIAUÍ | Brasil | 2201176 | 22 | 33 | nan | nan | nan | Caatinga | 15.0 |
| 3cc935c8-c13f-3c39-8217-9db9a8a83fc5 | -5.95311 | -42.91099 | 2025-09-25 03:19:00 | NPP-375D | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 9.0 |
| b5e3a8ac-9e9c-39f3-be9e-6a938ceada44 | -6.56823 | -41.36174 | 2025-09-25 03:19:00 | NPP-375D | LAGOA DO SÍTIO | PIAUÍ | Brasil | 2205599 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 1a4d0fdb-435e-3d83-896b-dd23f9c7b2aa | -3.80508 | -41.57608 | 2025-09-25 03:19:00 | NPP-375D | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 884f6812-c7a2-3cb9-a361-70c0e53b9474 | -9.05975 | -40.52528 | 2025-09-25 03:19:00 | NPP-375D | PETROLINA | PERNAMBUCO | Brasil | 2611101 | 26 | 33 | nan | nan | nan | Caatinga | 1.2 |
| c350b75a-63cc-3bc9-bad5-db555a31f403 | -3.78988 | -41.74379 | 2025-09-25 03:19:00 | NPP-375D | SÃO JOSÉ DO DIVINO | PIAUÍ | Brasil | 2210052 | 22 | 33 | nan | nan | nan | Caatinga | 4.4 |
| 4e1df96b-67cd-3861-8d0f-a4ca50259a17 | -6.41967 | -43.08154 | 2025-09-25 03:19:00 | NPP-375D | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 33.4 |
| e7461715-46e5-3579-8f2e-82e90150088a | -8.85023 | -42.48415 | 2025-09-25 03:19:00 | NPP-375D | CORONEL JOSÉ DIAS | PIAUÍ | Brasil | 2202851 | 22 | 33 | nan | nan | nan | Caatinga | 9.7 |
| e395f96f-8f17-36f0-8a06-33cb14857304 | -6.42036 | -43.07716 | 2025-09-25 03:19:00 | NPP-375D | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 13.2 |
| 40c2610f-5670-3d06-9c8a-1560de33c513 | -2.91262 | -40.39089 | 2025-09-25 03:19:00 | NPP-375D | CRUZ | CEARÁ | Brasil | 2304251 | 23 | 33 | nan | nan | nan | Caatinga | 3.8 |
| 76922c0a-852b-3e17-aae1-a1832c9b8270 | -6.419 | -43.08434 | 2025-09-25 03:19:00 | NPP-375D | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 32.1 |
| 21b68cd0-6460-3bfd-8b98-3c10ca8d8fd5 | -6.41673 | -43.09663 | 2025-09-25 03:19:00 | NPP-375D | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 30.3 |
| a5a0a91a-08e5-356f-b842-ff1fb5260bc1 | -3.61591 | -38.76512 | 2025-09-25 03:19:00 | NPP-375D | CAUCAIA | CEARÁ | Brasil | 2303709 | 23 | 33 | nan | nan | nan | Caatinga | 0.6 |
| bb4b099b-ab85-39df-b334-5b67adcc4e58 | -6.41169 | -43.08321 | 2025-09-25 03:19:00 | NPP-375D | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| b4343fd1-1f89-325f-a0bc-321e2b614a7c | -5.2942 | -35.56907 | 2025-09-25 03:19:00 | NPP-375D | TOUROS | RIO GRANDE DO NORTE | Brasil | 2414407 | 24 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 771dfef1-c1ac-32f8-91d6-d2ad5ac35b97 | -6.42338 | -43.10115 | 2025-09-25 03:19:00 | NPP-375D | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 20.4 |
| 888a723d-984e-3ab0-9e68-b03954560864 | -6.4263 | -43.08556 | 2025-09-25 03:19:00 | NPP-375D | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 32.1 |
| 2e624ec1-38ae-3a53-849f-0712d953910b | -2.91169 | -40.3965 | 2025-09-25 03:19:00 | NPP-375D | CRUZ | CEARÁ | Brasil | 2304251 | 23 | 33 | nan | nan | nan | Caatinga | 6.9 |
| 29d434e8-9967-304e-a02c-42be3e6163a9 | -6.55897 | -42.07121 | 2025-09-25 03:19:00 | NPP-375D | BARRA D'ALCÂNTARA | PIAUÍ | Brasil | 2201176 | 22 | 33 | nan | nan | nan | Caatinga | 7.4 |
| 1c492e4e-dae1-349d-a596-82c14b243468 | -3.74266 | -38.95499 | 2025-09-25 03:19:00 | NPP-375D | CAUCAIA | CEARÁ | Brasil | 2303709 | 23 | 33 | nan | nan | nan | Caatinga | 2.5 |
| aa005842-36c3-38bc-b203-e77c32bd283b | -6.56815 | -42.06068 | 2025-09-25 03:19:00 | NPP-375D | BARRA D'ALCÂNTARA | PIAUÍ | Brasil | 2201176 | 22 | 33 | nan | nan | nan | Caatinga | 6.5 |
| 3316b8fa-b701-3b56-bb1e-472b03c74620 | -5.09393 | -37.60726 | 2025-09-25 03:19:00 | NPP-375D | BARAÚNA | RIO GRANDE DO NORTE | Brasil | 2401453 | 24 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 21be4978-3037-3001-b8bc-755f9c5d613b | -6.56581 | -42.07258 | 2025-09-25 03:19:00 | NPP-375D | BARRA D'ALCÂNTARA | PIAUÍ | Brasil | 2201176 | 22 | 33 | nan | nan | nan | Caatinga | 7.4 |
| 3dd80818-4dca-3bc5-8cd7-89ffd2d6764a | -6.41759 | -43.09187 | 2025-09-25 03:19:00 | NPP-375D | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 32.1 |
| 0ea135cd-7b6d-3b3d-b1d0-d0fb35fb31fa | -2.91606 | -40.39738 | 2025-09-25 03:19:00 | NPP-375D | CRUZ | CEARÁ | Brasil | 2304251 | 23 | 33 | nan | nan | nan | Caatinga | 3.7 |
| d9ba0868-2483-304e-b978-08455cad57ec | -3.78408 | -41.73565 | 2025-09-25 03:19:00 | NPP-375D | SÃO JOSÉ DO DIVINO | PIAUÍ | Brasil | 2210052 | 22 | 33 | nan | nan | nan | Caatinga | 3.3 |
| 87578f7b-9815-34ff-8e0e-2fd76356362f | -6.56008 | -42.06586 | 2025-09-25 03:19:00 | NPP-375D | BARRA D'ALCÂNTARA | PIAUÍ | Brasil | 2201176 | 22 | 33 | nan | nan | nan | Caatinga | 3.6 |
| dd12b07b-ec8a-3d53-8cc6-baf85bb4aa97 | -17.9312 | -55.8548 | 2025-09-25 03:20:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 132.0 |
| 1d33babe-323d-3b47-bfed-c055872e686a | -20.972 | -50.0305 | 2025-09-25 03:20:00 | GOES-19 | MACAUBAL | SÃO PAULO | Brasil | 3528106 | 35 | 33 | nan | nan | nan | Mata Atlântica | 58.6 |
| 5ba855af-378f-3096-86bb-b3b5048eeba2 | -21.9721 | -49.5102 | 2025-09-25 03:20:00 | GOES-19 | PIRAJUÍ | SÃO PAULO | Brasil | 3538907 | 35 | 33 | nan | nan | nan | Mata Atlântica | 72.1 |
| aa4dde40-cb2f-30eb-ab4a-f2525639c94b | -20.9931 | -50.0032 | 2025-09-25 03:20:00 | GOES-19 | PLANALTO | SÃO PAULO | Brasil | 3539608 | 35 | 33 | nan | nan | nan | Mata Atlântica | 114.0 |
| abe0d8cd-1152-39ce-97d3-1aeae5d15115 | -6.4129 | -43.0958 | 2025-09-25 03:20:00 | GOES-19 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 106.4 |
| 8b2ffe7b-4931-3a77-8851-32207fa61505 | -23.0297 | -49.56 | 2025-09-25 03:20:00 | GOES-19 | IPAUSSU | SÃO PAULO | Brasil | 3520905 | 35 | 33 | nan | nan | nan | Mata Atlântica | 60.5 |
| 73a0eb61-341a-34bd-b73b-194b2b523e5c | -6.4131 | -43.0724 | 2025-09-25 03:20:00 | GOES-19 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 89.1 |
| 2b76fca7-6f60-3f97-9814-2b77b6773fee | -17.951 | -55.8522 | 2025-09-25 03:20:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 105.1 |
| a96f9833-1fb9-3c97-8a1a-1b736a794e01 | -6.1308 | -47.1784 | 2025-09-25 03:20:00 | GOES-19 | CAMPESTRE DO MARANHÃO | MARANHÃO | Brasil | 2102556 | 21 | 33 | nan | nan | nan | Cerrado | 52.7 |
| 4f6fda67-1fd4-314f-823b-77044ad99bb6 | -6.4319 | -43.0707 | 2025-09-25 03:20:00 | GOES-19 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 97.1 |
| 8c03059b-5e1a-344d-9ee1-e03443a04a9f | -17.9308 | -55.8758 | 2025-09-25 03:20:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 106.6 |
| a47f07bf-02d6-3eac-8fa1-9ab8229685b8 | -23.0304 | -49.5367 | 2025-09-25 03:20:00 | GOES-19 | BERNARDINO DE CAMPOS | SÃO PAULO | Brasil | 3506300 | 35 | 33 | nan | nan | nan | Mata Atlântica | 93.5 |
| de35b40a-c674-30e5-8926-6994c675b792 | -17.9506 | -55.8731 | 2025-09-25 03:20:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 86.2 |
| 3ea24291-9f26-31db-a4e8-1c21cd879d57 | -20.9925 | -50.0261 | 2025-09-25 03:20:00 | GOES-19 | PLANALTO | SÃO PAULO | Brasil | 3539608 | 35 | 33 | nan | nan | nan | Mata Atlântica | 130.8 |
| eea2a7ca-9b69-3028-a37d-b83b4a4fe555 | -6.4317 | -43.0942 | 2025-09-25 03:20:00 | GOES-19 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 112.2 |
| a8a578f5-4852-3d7a-9b62-5339c5673e6e | -11.69017 | -44.38461 | 2025-09-25 03:21:00 | NPP-375D | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| d90fcb31-c92b-3759-a596-eba4b4360a40 | -11.69024 | -44.39008 | 2025-09-25 03:21:00 | NPP-375D | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| cff52a26-9f08-3332-a706-693674bc1c69 | -11.69426 | -44.40084 | 2025-09-25 03:21:00 | NPP-375D | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 377af6e5-eed1-369a-af79-6beb80b19799 | -11.67123 | -44.4032 | 2025-09-25 03:21:00 | NPP-375D | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 3d5e6cfb-3294-3316-8f5e-299d73b889b1 | -11.66813 | -44.4178 | 2025-09-25 03:21:00 | NPP-375D | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 1ba7f4df-94eb-38eb-9e60-b1d4abeae635 | -12.8599 | -44.68856 | 2025-09-25 03:21:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 4.1 |
| a2b3b15c-29ff-3c32-b72c-1b302c5df0d3 | -10.43604 | -44.23347 | 2025-09-25 03:21:00 | NPP-375D | JÚLIO BORGES | PIAUÍ | Brasil | 2205524 | 22 | 33 | nan | nan | nan | Cerrado | 2.7 |
| eea97ecb-a6d7-3a38-b6ef-1ca4bdec263f | -12.41154 | -44.74688 | 2025-09-25 03:21:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 9e65b1f1-2579-3faa-ac89-a9be3f2725cf | -12.85269 | -44.67653 | 2025-09-25 03:21:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 3.0 |
| e268a026-dd4b-39bd-ad54-578df3bee15a | -11.76628 | -37.57616 | 2025-09-25 03:21:00 | NPP-375D | CONDE | BAHIA | Brasil | 2908606 | 29 | 33 | nan | nan | nan | Mata Atlântica | 3.8 |
| 7fd7560f-54be-3423-ad50-70b3c321ecd0 | -12.85671 | -44.69287 | 2025-09-25 03:21:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 3.1 |
| e209ede2-5a0a-3537-a32e-965df6d8a3c9 | -12.41175 | -44.75055 | 2025-09-25 03:21:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 1421a250-cbea-3040-94d7-7dd64a51bd43 | -12.41902 | -44.75195 | 2025-09-25 03:21:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 84235035-1407-3a0e-991d-61e45b018408 | -10.58853 | -44.08188 | 2025-09-25 03:21:00 | NPP-375D | JÚLIO BORGES | PIAUÍ | Brasil | 2205524 | 22 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 359e80a3-964d-3f1c-8153-266881da1eb7 | -10.59097 | -44.07878 | 2025-09-25 03:21:00 | NPP-375D | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 211588d4-2be8-3813-96d6-f53986ed94f7 | -12.41878 | -44.74842 | 2025-09-25 03:21:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 300b6c1f-0bc3-3f49-ac1f-5850e13c7ca6 | -11.69582 | -44.39896 | 2025-09-25 03:21:00 | NPP-375D | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| d1ba5b30-60f7-32f1-9b39-27de91e8f50d | -11.68865 | -44.39736 | 2025-09-25 03:21:00 | NPP-375D | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 8f9edf2b-ac71-39e9-b07f-07ae4fe1cd0e | -11.67685 | -44.41212 | 2025-09-25 03:21:00 | NPP-375D | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 04f98e74-6eb9-3a4d-8177-fdba45170660 | -11.76623 | -37.57753 | 2025-09-25 03:21:00 | NPP-375D | CONDE | BAHIA | Brasil | 2908606 | 29 | 33 | nan | nan | nan | Mata Atlântica | 3.4 |
| a416bcff-97be-30b0-9661-3200e161cae5 | -10.58943 | -44.08604 | 2025-09-25 03:21:00 | NPP-375D | JÚLIO BORGES | PIAUÍ | Brasil | 2205524 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 7011a560-7bff-3d6d-8cf5-dc8965536cf8 | -11.64192 | -44.43491 | 2025-09-25 03:21:00 | NPP-375D | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| db2d9cca-b3e5-3f74-b420-afa24c43e6fe | -11.64349 | -44.42754 | 2025-09-25 03:21:00 | NPP-375D | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 3.2 |
| ae9bdc51-b16c-39f1-88e7-ba8b3dcfe9c5 | -11.66968 | -44.4105 | 2025-09-25 03:21:00 | NPP-375D | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 0b09209e-ed91-3e6a-aa8a-f1d73b52b45f | -11.68863 | -44.39192 | 2025-09-25 03:21:00 | NPP-375D | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 4a3854ad-4efb-370a-ba73-95b6064a2a52 | -6.4131 | -43.0724 | 2025-09-25 03:30:00 | GOES-19 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 82.9 |
| 3593eef6-f8f3-326b-bfbd-3bc1b778f662 | -16.8538 | -50.5026 | 2025-09-25 03:30:00 | GOES-19 | PARAÚNA | GOIÁS | Brasil | 5216403 | 52 | 33 | nan | nan | nan | Cerrado | 58.0 |
| 18afbc79-f18e-3620-8e4e-250d9a03ade2 | -6.4317 | -43.0942 | 2025-09-25 03:30:00 | GOES-19 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 110.9 |
| 355ed0fb-b95b-3fc4-b18d-2bdd7d0de9b7 | -17.9308 | -55.8758 | 2025-09-25 03:30:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 97.8 |
| 1d24af17-f139-3fe2-96b8-873caac9f5b3 | -6.4319 | -43.0707 | 2025-09-25 03:30:00 | GOES-19 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 81.6 |
| 7a22af57-badd-3194-b507-2b0a68d07e48 | -20.972 | -50.0305 | 2025-09-25 03:30:00 | GOES-19 | MACAUBAL | SÃO PAULO | Brasil | 3528106 | 35 | 33 | nan | nan | nan | Mata Atlântica | 79.2 |
| 8f762f7d-0f1e-36a4-8bdc-e598dee658e2 | -21.9929 | -49.5054 | 2025-09-25 03:30:00 | GOES-19 | PIRAJUÍ | SÃO PAULO | Brasil | 3538907 | 35 | 33 | nan | nan | nan | Mata Atlântica | 62.5 |
| 2293bc1c-cde6-33e3-8e02-5fed518bce82 | -20.9931 | -50.0032 | 2025-09-25 03:30:00 | GOES-19 | PLANALTO | SÃO PAULO | Brasil | 3539608 | 35 | 33 | nan | nan | nan | Mata Atlântica | 107.7 |
| 11582a98-9ed3-3cb9-9f5a-05acefe01753 | -17.9506 | -55.8731 | 2025-09-25 03:30:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 85.8 |
| 546a3d26-d831-3dea-96fb-493c7da86e62 | -6.4129 | -43.0958 | 2025-09-25 03:30:00 | GOES-19 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 119.2 |
| 5f93e89b-aebe-3b50-87a6-2e04483572ad | -21.9721 | -49.5102 | 2025-09-25 03:30:00 | GOES-19 | PIRAJUÍ | SÃO PAULO | Brasil | 3538907 | 35 | 33 | nan | nan | nan | Mata Atlântica | 83.2 |
| 2aac6942-58f6-3017-920f-35898b312947 | -17.951 | -55.8522 | 2025-09-25 03:30:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 97.5 |
| 41236838-cbc7-37f4-b8e6-c0cb1ff42d17 | -17.9312 | -55.8548 | 2025-09-25 03:30:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 112.2 |
| bb1791e2-aa21-3ba9-bad0-0b97bff2d8e7 | -20.9925 | -50.0261 | 2025-09-25 03:30:00 | GOES-19 | PLANALTO | SÃO PAULO | Brasil | 3539608 | 35 | 33 | nan | nan | nan | Mata Atlântica | 176.9 |
| 56270780-bf9f-3e20-9a9b-c4f290d6ebff | -20.972 | -50.0305 | 2025-09-25 03:40:00 | GOES-19 | MACAUBAL | SÃO PAULO | Brasil | 3528106 | 35 | 33 | nan | nan | nan | Mata Atlântica | 53.6 |
| 81e62aa0-765f-3054-a529-10977b8189be | -17.9308 | -55.8758 | 2025-09-25 03:40:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 104.7 |
| 8242bf2d-9847-3872-a9c9-a0ea3490e288 | -2.9291 | -48.3181 | 2025-09-25 03:40:00 | GOES-19 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 54.0 |


[Clique aqui para ver as próximas entradas](README8.md)
