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

## Dados Diários - Página 161

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| c5977eb8-9df9-39d9-8834-fac421b1c790 | -11.258 | -45.6682 | 2024-10-01 11:16:09 | GOES-16 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 98.8 |
| ef47548a-b3e3-3d6b-8c31-ee2014d424ec | -11.2584 | -45.6453 | 2024-10-01 11:16:09 | GOES-16 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 127.7 |
| 60ada7d4-653a-3c70-ae40-0cfcb8720d09 | -12.9433 | -51.2192 | 2024-10-01 11:16:19 | GOES-16 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 83.3 |
| ca84a36a-8036-39a5-867f-dfc1e4d414dd | -12.9629 | -51.1955 | 2024-10-01 11:16:19 | GOES-16 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 75.3 |
| 548d4dd7-4688-3a47-9dc5-57767fa13588 | -12.9625 | -51.2169 | 2024-10-01 11:16:19 | GOES-16 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 115.1 |
| eca4f698-c976-3cc0-b99d-c171feccd03a | -17.1574 | -56.2052 | 2024-10-01 11:16:43 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 101.3 |
| 03778245-f4fe-3abe-9add-a83b216d94df | -17.1771 | -56.2027 | 2024-10-01 11:16:43 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 119.7 |
| 525505fc-f50a-3f4d-a1c5-797d9032fd94 | -17.1767 | -56.2234 | 2024-10-01 11:16:43 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 112.1 |
| 1c5c5204-6c70-3a34-9c4d-6ee3812f8b8f | -17.1577 | -56.1844 | 2024-10-01 11:16:43 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 81.6 |
| 0544812f-e71c-35c9-95aa-5aa7ea4e2d23 | -21.5864 | -47.8827 | 2024-10-01 11:17:05 | GOES-16 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 194.4 |
| 35c55912-689e-3a7f-a300-7cd1a2a90845 | -21.5871 | -47.8591 | 2024-10-01 11:17:05 | GOES-16 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 232.0 |
| 3919245b-72ca-361b-a877-cdea816fb0fa | -21.6078 | -47.854 | 2024-10-01 11:17:05 | GOES-16 | SÃO CARLOS | SÃO PAULO | Brasil | 3548906 | 35 | 33 | nan | nan | nan | Cerrado | 126.3 |
| 4a8069b2-9e6f-3c62-bba2-ecd49d4d8cd3 | -22.3707 | -49.3244 | 2024-10-01 11:17:09 | GOES-16 | DUARTINA | SÃO PAULO | Brasil | 3514502 | 35 | 33 | nan | nan | nan | Mata Atlântica | 123.6 |
| 4ec2d183-7267-36ce-bf3a-a87639e6458b | -12.9433 | -51.2192 | 2024-10-01 11:26:19 | GOES-16 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 95.1 |
| 6759ac15-11d6-35d9-b102-2f342ad64703 | -12.9629 | -51.1955 | 2024-10-01 11:26:19 | GOES-16 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 71.2 |
| 6a5a8ac5-2023-32d4-8d93-61c81d725d83 | -12.9793 | -51.364 | 2024-10-01 11:26:19 | GOES-16 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 76.8 |
| f298fe59-0a32-3624-9d0b-0dcf2d14c7c0 | -12.9985 | -51.3617 | 2024-10-01 11:26:19 | GOES-16 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 98.9 |
| 253e7a15-ee25-3840-956f-bbbb1e189a37 | -12.9625 | -51.2169 | 2024-10-01 11:26:19 | GOES-16 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 148.2 |
| 341d2768-27d5-30e4-b91a-d0625cf4f397 | -16.6316 | -57.2557 | 2024-10-01 11:26:40 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 77.1 |
| 1e3047a8-6e65-3c35-9147-d8a10f96336b | -16.7471 | -57.3651 | 2024-10-01 11:26:40 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 104.9 |
| 7d8481d7-18d1-36d7-be22-7b3f3728525d | -16.6319 | -57.2352 | 2024-10-01 11:26:40 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 77.3 |
| 0d45520e-fe2a-3704-95af-44f5aa065551 | -16.8292 | -55.9152 | 2024-10-01 11:26:41 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 78.7 |
| 8650635c-b89a-3ae8-b111-c1b55ef548c4 | -16.8488 | -55.9128 | 2024-10-01 11:26:41 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 93.3 |
| efacb40a-36b6-3337-85c7-ac1523e4ddb3 | -17.1577 | -56.1844 | 2024-10-01 11:26:43 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 84.2 |
| 37457bc0-29ac-3a83-b874-02cd9e6fe89b | -17.1574 | -56.2052 | 2024-10-01 11:26:43 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 106.7 |
| 7931e9e0-3606-389a-b447-8a6768354554 | -17.1771 | -56.2027 | 2024-10-01 11:26:43 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 115.8 |
| f2f7612c-eb03-33b4-97fb-211daa6df570 | -17.1767 | -56.2234 | 2024-10-01 11:26:43 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 103.4 |
| 6a2b9da4-2482-3752-b4cd-51d4b8e944ff | -17.1964 | -56.2209 | 2024-10-01 11:26:43 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 75.6 |
| 8f3694fb-88f0-3541-8a61-0854aa89ffc7 | -21.6078 | -47.854 | 2024-10-01 11:27:05 | GOES-16 | SÃO CARLOS | SÃO PAULO | Brasil | 3548906 | 35 | 33 | nan | nan | nan | Cerrado | 556.5 |
| af490842-5e83-3f6c-86d0-66c2c96a2059 | -21.5864 | -47.8827 | 2024-10-01 11:27:05 | GOES-16 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 465.6 |
| 96bc8966-8d90-379f-9f73-7bd5c2bec282 | -21.6085 | -47.8304 | 2024-10-01 11:27:05 | GOES-16 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 96.9 |
| 09e175ad-9125-332b-b9fa-3d2a7af553c6 | -21.5871 | -47.8591 | 2024-10-01 11:27:05 | GOES-16 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 575.0 |
| 5b95c2db-e812-374c-93a6-dafc77469d72 | -21.5878 | -47.8355 | 2024-10-01 11:27:05 | GOES-16 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 106.4 |
| 1eda0ca5-69ad-3f3d-bfef-11fb6a71aa06 | -22.3713 | -49.3011 | 2024-10-01 11:27:09 | GOES-16 | PIRATININGA | SÃO PAULO | Brasil | 3539400 | 35 | 33 | nan | nan | nan | Mata Atlântica | 100.5 |
| d215f8e7-71c3-395b-a8cb-c7a6357deab4 | -22.3707 | -49.3244 | 2024-10-01 11:27:09 | GOES-16 | DUARTINA | SÃO PAULO | Brasil | 3514502 | 35 | 33 | nan | nan | nan | Mata Atlântica | 147.8 |
| b9f9c617-41c5-32ef-b349-6bce89ac8560 | -10.5743 | -48.0399 | 2024-10-01 11:36:06 | GOES-16 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 77.8 |
| ad57e3be-6891-3275-9337-4261781beead | -12.9985 | -51.3617 | 2024-10-01 11:36:19 | GOES-16 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 197.9 |
| 1865eb7c-43e1-3883-ad97-3d7e1d83a6a2 | -12.9793 | -51.364 | 2024-10-01 11:36:19 | GOES-16 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 95.4 |
| a470c5c5-69b6-3679-bd8c-81d948c03139 | -12.9988 | -51.3403 | 2024-10-01 11:36:19 | GOES-16 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 70.5 |
| a79fee15-3e19-3079-9d02-e084fdce1fec | -12.9625 | -51.2169 | 2024-10-01 11:36:19 | GOES-16 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 80.0 |
| 376c43dc-93c8-37a1-8f1f-5a2a9165eac4 | -16.6316 | -57.2557 | 2024-10-01 11:36:40 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 82.5 |
| fcb61f17-3664-337f-887c-689474df5dc7 | -16.6319 | -57.2352 | 2024-10-01 11:36:40 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 77.8 |
| ebb98fbc-6990-35e7-a3d4-352f5eae0700 | -16.8292 | -55.9152 | 2024-10-01 11:36:41 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 94.5 |
| 75fd190e-c03c-3ab2-ac7b-d99e482502fb | -16.8488 | -55.9128 | 2024-10-01 11:36:41 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 87.1 |
| 2fba31bf-a617-3fb5-9113-becb39271879 | -17.1967 | -56.2002 | 2024-10-01 11:36:43 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 90.6 |
| fb5b3792-122e-3129-8979-51e7819ea937 | -17.1574 | -56.2052 | 2024-10-01 11:36:43 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 119.0 |
| 7dffa155-0a40-30b5-bd77-dbf5235591ba | -17.1577 | -56.1844 | 2024-10-01 11:36:43 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 96.6 |
| 21bf6c00-0f9f-33e7-9e09-dfff75d85311 | -17.1767 | -56.2234 | 2024-10-01 11:36:43 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 98.5 |
| 2eb2ec04-94ee-3cf9-883c-98c098fed908 | -18.8895 | -49.1942 | 2024-10-01 11:36:51 | GOES-16 | MONTE ALEGRE DE MINAS | MINAS GERAIS | Brasil | 3142809 | 31 | 33 | nan | nan | nan | Mata Atlântica | 130.1 |
| fb9f52a2-4360-3264-a75f-3f0bfc800271 | -18.8889 | -49.2169 | 2024-10-01 11:36:51 | GOES-16 | MONTE ALEGRE DE MINAS | MINAS GERAIS | Brasil | 3142809 | 31 | 33 | nan | nan | nan | Mata Atlântica | 80.6 |
| b37668d1-7aef-36d4-be77-51fa357f12da | -18.9091 | -49.2129 | 2024-10-01 11:36:51 | GOES-16 | MONTE ALEGRE DE MINAS | MINAS GERAIS | Brasil | 3142809 | 31 | 33 | nan | nan | nan | Mata Atlântica | 136.7 |
| 9d97daa4-e47b-367b-891f-2d37e223944b | -18.9096 | -49.1902 | 2024-10-01 11:36:51 | GOES-16 | MONTE ALEGRE DE MINAS | MINAS GERAIS | Brasil | 3142809 | 31 | 33 | nan | nan | nan | Mata Atlântica | 227.3 |
| 421c84e2-460e-3390-9f92-54daf28669a5 | -21.5864 | -47.8827 | 2024-10-01 11:37:05 | GOES-16 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 319.8 |
| 2983ae36-be77-39e0-afa5-6d55c468fc35 | -22.3707 | -49.3244 | 2024-10-01 11:37:09 | GOES-16 | DUARTINA | SÃO PAULO | Brasil | 3514502 | 35 | 33 | nan | nan | nan | Mata Atlântica | 148.7 |
| 293315c9-d2a6-3eaa-8d80-5fe3f5685672 | -22.3713 | -49.3011 | 2024-10-01 11:37:09 | GOES-16 | PIRATININGA | SÃO PAULO | Brasil | 3539400 | 35 | 33 | nan | nan | nan | Mata Atlântica | 120.2 |
| 45b556ed-a5ca-385a-be93-44b6beff4b2b | -12.3934 | -50.9658 | 2024-10-01 11:46:16 | GOES-16 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 90.7 |
| be4a12e4-6c82-3ce9-8469-74376b81c12c | -12.9985 | -51.3617 | 2024-10-01 11:46:19 | GOES-16 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 444.7 |
| af572dcc-eb3c-3ffc-8446-b80cd2c745eb | -12.9793 | -51.364 | 2024-10-01 11:46:19 | GOES-16 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 123.6 |
| ad3212d4-ad54-31f8-8847-14bf55bd387f | -12.9988 | -51.3403 | 2024-10-01 11:46:19 | GOES-16 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 116.5 |
| 87df5dba-f85a-399d-9076-c1048fa14726 | -16.6316 | -57.2557 | 2024-10-01 11:46:40 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 100.9 |
| f2942748-5d85-3b0a-84e9-45ad8fd63361 | -16.7471 | -57.3651 | 2024-10-01 11:46:40 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 185.0 |
| 5e03425e-742a-3aac-9a18-8b408ca2d67a | -16.6319 | -57.2352 | 2024-10-01 11:46:40 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 89.5 |
| 9a3abf99-fb27-322f-b2e0-77e48e6e5b48 | -16.8292 | -55.9152 | 2024-10-01 11:46:41 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 125.3 |
| 7b8050e8-8004-3943-a340-948677bc7562 | -16.8488 | -55.9128 | 2024-10-01 11:46:41 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 86.0 |
| a11a638c-6564-3ea3-9709-4fb8807ff839 | -16.8787 | -57.6971 | 2024-10-01 11:46:41 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 70.9 |
| 8d15e75f-3687-36d8-b870-62a77c6cdc69 | -16.7663 | -57.3833 | 2024-10-01 11:46:41 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 89.4 |
| 6ef2de5f-a837-32e4-ad6a-da2f8e88272b | -17.1574 | -56.2052 | 2024-10-01 11:46:43 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 110.0 |
| ab2f9ac9-1049-3bce-b862-32a2b7c04878 | -17.1577 | -56.1844 | 2024-10-01 11:46:43 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 96.1 |
| cc73ecb2-97be-35a4-bcee-ebe01276895b | -17.1767 | -56.2234 | 2024-10-01 11:46:43 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 152.0 |
| ccef2a92-6799-3576-8d76-d68aeb7025cf | -18.1121 | -49.121 | 2024-10-01 11:46:47 | GOES-16 | ITUMBIARA | GOIÁS | Brasil | 5211503 | 52 | 33 | nan | nan | nan | Cerrado | 76.0 |
| 9ca6244b-2346-3dc8-aa07-2235d67916ab | -18.1127 | -49.0983 | 2024-10-01 11:46:47 | GOES-16 | BURITI ALEGRE | GOIÁS | Brasil | 5203906 | 52 | 33 | nan | nan | nan | Cerrado | 95.9 |
| 58b3cfd5-d625-3f7e-af88-1efb4faa8772 | -18.9091 | -49.2129 | 2024-10-01 11:46:51 | GOES-16 | MONTE ALEGRE DE MINAS | MINAS GERAIS | Brasil | 3142809 | 31 | 33 | nan | nan | nan | Mata Atlântica | 72.9 |
| 6f1bc0aa-60ea-3f56-9cbb-234adeede211 | -18.9096 | -49.1902 | 2024-10-01 11:46:51 | GOES-16 | MONTE ALEGRE DE MINAS | MINAS GERAIS | Brasil | 3142809 | 31 | 33 | nan | nan | nan | Mata Atlântica | 146.5 |
| 1bc1640c-cc33-3214-ab1b-6b26bcc2599a | -18.6977 | -57.3123 | 2024-10-01 11:46:51 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 71.7 |
| 0ebfd8f3-0026-3fd9-895d-2a0a8008c34c | -21.3841 | -48.4681 | 2024-10-01 11:47:04 | GOES-16 | TAQUARITINGA | SÃO PAULO | Brasil | 3553708 | 35 | 33 | nan | nan | nan | Cerrado | 164.9 |
| 3bdeafc6-a335-3047-a538-eaf92c2743fb | -21.3834 | -48.4915 | 2024-10-01 11:47:04 | GOES-16 | TAQUARITINGA | SÃO PAULO | Brasil | 3553708 | 35 | 33 | nan | nan | nan | Cerrado | 142.4 |
| 796836ec-60f7-3e40-ad28-d25e18e4e5c5 | -21.6099 | -47.7831 | 2024-10-01 11:47:05 | GOES-16 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 238.3 |
| 744f433f-2211-318a-aaa5-9f57e9802080 | -21.5892 | -47.7882 | 2024-10-01 11:47:05 | GOES-16 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 512.4 |
| 3bf0b677-c39a-32a9-a168-d9eac3647c81 | -22.3707 | -49.3244 | 2024-10-01 11:47:09 | GOES-16 | DUARTINA | SÃO PAULO | Brasil | 3514502 | 35 | 33 | nan | nan | nan | Mata Atlântica | 126.5 |
| 1e288717-5ffd-3b73-ac53-82c4ed1c6439 | -22.3713 | -49.3011 | 2024-10-01 11:47:09 | GOES-16 | PIRATININGA | SÃO PAULO | Brasil | 3539400 | 35 | 33 | nan | nan | nan | Mata Atlântica | 113.1 |
| 8a8a31a5-e9e8-3a9b-a6f7-570007e01091 | -10.996 | -46.5418 | 2024-10-01 11:56:08 | GOES-16 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 82.0 |
| 5ff79682-c1b8-36af-8c7e-c41f33f6aab0 | -10.9964 | -46.5192 | 2024-10-01 11:56:08 | GOES-16 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 87.2 |
| 7e2eb91e-9b2e-3ef1-bd1c-a1b8d47cfef1 | -12.9205 | -51.4563 | 2024-10-01 11:56:19 | GOES-16 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 79.7 |
| cad4a405-b39b-30b4-9d6f-eafa17404567 | -12.9985 | -51.3617 | 2024-10-01 11:56:19 | GOES-16 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 306.5 |
| 1e034299-c085-3bdd-aea8-a73ee8cfc24b | -13.018 | -51.338 | 2024-10-01 11:56:20 | GOES-16 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 81.5 |
| c0a97b35-59cc-3b04-9b8f-30f3eff79483 | -13.218 | -48.5797 | 2024-10-01 11:56:20 | GOES-16 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 66.9 |
| 509a14a8-1f48-3704-87fc-96597d8bb98e | -16.6117 | -57.2784 | 2024-10-01 11:56:40 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 72.5 |
| 65635f30-9755-3a65-866f-2497fcbeaf11 | -16.6316 | -57.2557 | 2024-10-01 11:56:40 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 107.9 |
| 1aef7ca4-0f4c-3649-8c30-cde8bba5046a | -16.6515 | -57.233 | 2024-10-01 11:56:40 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 111.7 |
| 824e83a5-2662-358c-a94a-cee3e01fcb4a | -16.6319 | -57.2352 | 2024-10-01 11:56:40 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 105.9 |
| 5bfd846a-becd-3a83-8fd5-58e3288b6e9c | -16.612 | -57.2579 | 2024-10-01 11:56:40 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 80.3 |
| 8695b1b6-313d-3967-8396-dffb0210ba4a | -16.6512 | -57.2535 | 2024-10-01 11:56:40 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 77.9 |
| 3038dda0-68d9-3a22-ab81-bb5c61e57a14 | -16.7471 | -57.3651 | 2024-10-01 11:56:40 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 250.6 |
| e25716dd-7b82-316e-82de-85d67371ea48 | -16.8484 | -55.9335 | 2024-10-01 11:56:41 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 81.9 |
| fab6f1e9-2623-3d64-8770-8e9049110532 | -16.8488 | -55.9128 | 2024-10-01 11:56:41 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 117.1 |
| 8b6abdc5-1480-3a6b-b995-6c5621948dab | -16.8787 | -57.6971 | 2024-10-01 11:56:41 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 85.2 |
| 5354accc-a13f-36a6-bbaa-afec97010ce5 | -16.8292 | -55.9152 | 2024-10-01 11:56:41 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 106.6 |
| 86c11348-4856-306b-9788-8b63900914a0 | -17.1574 | -56.2052 | 2024-10-01 11:56:43 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 116.6 |
| 02cdd6d8-3dd0-3919-8e88-f36461f4d285 | -17.1767 | -56.2234 | 2024-10-01 11:56:43 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 159.3 |
| 3f1c0f30-fc4b-363b-8163-33b3334d36c2 | -17.1577 | -56.1844 | 2024-10-01 11:56:43 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 98.6 |


[Clique aqui para ver as próximas entradas](README162.md)
