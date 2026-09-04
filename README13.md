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

## Dados Diários - Página 13

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| d1943288-49e9-3f8b-a8d8-25db45cdf322 | -10.9104 | -49.61255 | 2026-09-04 04:19:00 | NPP-375D | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 9190738a-6529-3021-9320-38873e038100 | -5.3197 | -44.84676 | 2026-09-04 04:19:00 | NPP-375D | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 2ea06285-9858-3979-ae03-45d3c6bbf90b | -6.35466 | -46.1131 | 2026-09-04 04:19:00 | NPP-375D | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 0cc9be66-f370-3eaa-82c5-e593a5b6190a | -6.90677 | -47.44822 | 2026-09-04 04:19:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 8.0 |
| 9854743e-468d-3483-9aef-e655dcacfecf | -10.64687 | -50.39563 | 2026-09-04 04:19:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 10.6 |
| 3e1eb68e-dd0d-347c-b058-c0c16b2a4091 | -9.57663 | -40.34566 | 2026-09-04 04:19:00 | NPP-375D | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 20.3 |
| c892cefa-9238-3662-aae9-de2861a0e032 | -10.50186 | -51.33007 | 2026-09-04 04:19:00 | NPP-375D | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 5b3ce902-ab8d-31a0-94f3-53795657182c | -5.38503 | -54.4542 | 2026-09-04 04:19:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| b5db404c-03a1-3b77-8657-c75b67786806 | -7.24459 | -42.76611 | 2026-09-04 04:19:00 | NPP-375D | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| ec86a307-42df-32df-bc63-2fe17f78a60c | -10.83566 | -51.78569 | 2026-09-04 04:19:00 | NPP-375D | PORTO ALEGRE DO NORTE | MATO GROSSO | Brasil | 5106778 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| ec81efb3-f609-32f3-9123-e446f02f86c5 | -10.9141 | -49.61814 | 2026-09-04 04:19:00 | NPP-375D | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 6bec97ca-7877-34bd-b612-ed7918d44a07 | -8.1123 | -54.7883 | 2026-09-04 04:19:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| bd36a67d-4959-3a42-93a3-5f6e4915984f | -7.59379 | -44.74841 | 2026-09-04 04:19:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 22.2 |
| 96d5a938-3473-357b-ad0b-2d01b0731353 | -5.38616 | -54.44791 | 2026-09-04 04:19:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| ed940e25-6f5f-3bec-a750-72c1be265a7f | -10.63351 | -50.39705 | 2026-09-04 04:19:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| a065cab8-30c5-398b-96d1-dcc46163886c | -8.11898 | -54.78955 | 2026-09-04 04:19:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 132978ae-7158-3804-9e4d-c40caeb746e9 | -10.39449 | -49.95685 | 2026-09-04 04:19:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 38e62b01-3628-3c2d-9090-ed0ccb457be7 | -10.49669 | -51.32908 | 2026-09-04 04:19:00 | NPP-375D | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 18985f2d-1ec0-3c89-9905-f8404fcaa4d1 | -10.90895 | -45.35098 | 2026-09-04 04:19:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 11.9 |
| 244b7966-93d0-330f-97cf-f5ba1316fb32 | -10.65093 | -50.41159 | 2026-09-04 04:19:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 7.4 |
| 38e78af2-0007-36fe-8e7b-89a54fa8d299 | -10.91249 | -45.35157 | 2026-09-04 04:19:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 11.9 |
| 5f1f2a33-e120-3e44-b419-c2e658e02830 | -6.32714 | -43.81836 | 2026-09-04 04:19:00 | NPP-375D | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 15be8588-0992-390b-8798-8c03e3857ef6 | -10.31025 | -50.34072 | 2026-09-04 04:19:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 42d0d353-b02f-3650-9464-425f16577b78 | -12.11229 | -45.15865 | 2026-09-04 04:19:00 | NPP-375D | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 8c379457-8c2c-32c2-a7ad-60365fdca9c7 | -10.91317 | -45.34752 | 2026-09-04 04:19:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.9 |
| ee4db6cc-f73f-3bff-852d-218c3fc20adf | -10.39354 | -49.96193 | 2026-09-04 04:19:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| c8de332a-6629-3dfc-860a-5f1095a74639 | -10.26699 | -50.03515 | 2026-09-04 04:19:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 38.2 |
| ee2198f5-c0ae-3234-bc9b-0118a0472324 | -11.51846 | -46.89954 | 2026-09-04 04:19:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 607fa0dd-2683-3fdc-9818-779445437b59 | -8.49993 | -54.65334 | 2026-09-04 04:19:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| efade22d-a8b6-306a-bc6d-377e11305df2 | -10.64969 | -50.40732 | 2026-09-04 04:19:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 0ac4841f-6d5c-3246-a355-b69b5d7c7c6f | -5.80157 | -43.63081 | 2026-09-04 04:19:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 592f6d17-03eb-3b9d-a749-d62352be5a6b | -10.5764 | -50.03537 | 2026-09-04 04:19:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| d561d656-fc5c-31a5-abb5-7db1319779c6 | -4.47968 | -55.08337 | 2026-09-04 04:19:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 9ad41028-7474-3bce-a6d9-32b3278e3e6a | -6.11608 | -44.67858 | 2026-09-04 04:19:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 200a542e-07f2-3317-9128-4c04a32eefbe | -10.64383 | -50.41179 | 2026-09-04 04:19:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 178cf23b-7053-35a3-9ebb-a65622189afb | -6.11246 | -44.678 | 2026-09-04 04:19:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 9864d042-b561-3cca-acd5-358a8c4dfd6b | -5.96884 | -46.67931 | 2026-09-04 04:19:00 | NPP-375D | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 268e576b-04d2-307c-a897-60798f998a94 | -9.70542 | -50.84392 | 2026-09-04 04:19:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 527fabec-4d10-32d3-b719-111e6d2f25e4 | -10.6519 | -50.40619 | 2026-09-04 04:19:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 3eeb2a72-bc30-3a86-ae84-54fa3eee5b3d | -10.63235 | -50.39286 | 2026-09-04 04:19:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 06e03922-b5ff-35d5-8db1-10fef3d396f1 | -8.50104 | -54.64756 | 2026-09-04 04:19:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 41fc4bd9-d268-3098-a8d1-566dfebbfcde | -9.57778 | -40.33812 | 2026-09-04 04:19:00 | NPP-375D | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 5.3 |
| d14f532e-be77-31cb-aef9-46078e199058 | -13.4002 | -41.88371 | 2026-09-04 04:19:00 | NPP-375D | RIO DE CONTAS | BAHIA | Brasil | 2926707 | 29 | 33 | nan | nan | nan | Caatinga | 1.2 |
| a4b3a97c-919e-38de-888c-e7f452b32f1c | -10.63932 | -50.3926 | 2026-09-04 04:19:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 93087a5d-53ab-31b4-b755-c3699f98a825 | -10.49881 | -48.65208 | 2026-09-04 04:19:00 | NPP-375D | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 5142fd8a-4b39-3074-9068-4f9083ed2c79 | -5.80257 | -43.64656 | 2026-09-04 04:19:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 00de1966-6b27-3b5c-b555-47a5baca04e3 | -9.70035 | -50.84289 | 2026-09-04 04:19:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| fd790039-d122-364d-813a-c81a733544c3 | -6.31021 | -46.0904 | 2026-09-04 04:19:00 | NPP-375D | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 744d1ec9-32c4-3cb3-b915-72f379c287fa | -10.52516 | -47.95722 | 2026-09-04 04:19:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 1ef86407-8a2f-3b08-855b-fb4f4627bb6a | -9.20298 | -43.23438 | 2026-09-04 04:19:00 | NPP-375D | CARACOL | PIAUÍ | Brasil | 2202505 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 763468b1-bac3-3e1b-8f10-99e194692462 | -10.64406 | -50.38394 | 2026-09-04 04:19:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 11.8 |
| c9ffbbcc-aa25-3de0-9ee2-105a7ba2e093 | -10.90826 | -45.35503 | 2026-09-04 04:19:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 11.9 |
| 2bb304d3-29b8-3e0c-919b-f6a3e7e41505 | -6.31129 | -46.08891 | 2026-09-04 04:19:00 | NPP-375D | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 175411c6-cfdc-3fa3-bad3-33cfdfd8b4b7 | -4.48691 | -55.08438 | 2026-09-04 04:19:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 618666d6-933a-327b-be08-a77d012cc205 | -10.65937 | -50.40918 | 2026-09-04 04:19:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 87d04384-f913-321e-b03f-0e8ad79ccb5d | -7.5476 | -61.3437 | 2026-09-04 04:20:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 34.7 |
| 80ab15b3-44ae-34a1-a387-5ce741cf8110 | -5.565 | -60.1739 | 2026-09-04 04:20:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 50.4 |
| 3a4e58df-15fa-362d-8adc-f5ee1442fae6 | -7.566 | -61.343 | 2026-09-04 04:20:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 42.2 |
| a6f43724-09ba-3b39-b434-5037b66f3c17 | -8.6101 | -67.1783 | 2026-09-04 04:20:00 | GOES-19 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 45.8 |
| 8bc95c5b-ef6f-3a26-94e3-f17603f3a03c | -14.7986 | -47.13652 | 2026-09-04 04:21:00 | NPP-375D | VILA BOA | GOIÁS | Brasil | 5222203 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| cb6f835c-567e-3205-aed4-004ba6fcd538 | -13.52034 | -46.10578 | 2026-09-04 04:21:00 | NPP-375D | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 5e8bead1-6aa1-3698-aa9b-1c591dbded28 | -17.09656 | -56.8493 | 2026-09-04 04:21:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.2 |
| 17df071e-3ca2-3168-a29c-f78a50c56cf4 | -15.7308 | -47.78682 | 2026-09-04 04:21:00 | NPP-375D | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 55c0ba1f-130f-3d93-b284-9cd546b3e57a | -15.90449 | -50.16116 | 2026-09-04 04:21:00 | NPP-375D | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| bae896d6-5ccb-310d-ab6d-3309c4177f75 | -19.06971 | -46.99795 | 2026-09-04 04:21:00 | NPP-375D | PATROCÍNIO | MINAS GERAIS | Brasil | 3148103 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| f7064bb6-970e-34d8-b413-589eb09543f8 | -15.76795 | -43.31643 | 2026-09-04 04:21:00 | NPP-375D | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 1221029a-cae1-3f70-a0ff-1f737745eb0b | -15.72703 | -47.78615 | 2026-09-04 04:21:00 | NPP-375D | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 9702e99b-7f68-336b-931a-563f18be79a9 | -17.09402 | -56.86039 | 2026-09-04 04:21:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.3 |
| 9a68e95e-60bb-33b1-85ca-7233d48e319f | -16.66097 | -43.63776 | 2026-09-04 04:21:00 | NPP-375D | FRANCISCO SÁ | MINAS GERAIS | Brasil | 3126703 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| a1bc1701-60eb-386c-b9a9-94a2633c2aa7 | -17.09554 | -56.85392 | 2026-09-04 04:21:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.2 |
| aa7d3ff0-e35b-34c8-ac59-8edb727ea21f | -17.24876 | -44.86695 | 2026-09-04 04:21:00 | NPP-375D | PIRAPORA | MINAS GERAIS | Brasil | 3151206 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| eb889b15-2344-3912-89b1-beeddb86b83f | -17.10318 | -56.84998 | 2026-09-04 04:21:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.7 |
| ac261610-e755-3de0-9b6c-e26e1a307252 | -15.90977 | -50.1571 | 2026-09-04 04:21:00 | NPP-375D | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| b83b9c3f-6b5b-3b48-900f-935dfbbf302b | -18.13822 | -51.80042 | 2026-09-04 04:21:00 | NPP-375D | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 783069b5-b001-3263-9442-e9884b9c4c02 | -17.09431 | -56.85947 | 2026-09-04 04:21:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.2 |
| 4a4bf408-e6e7-38d0-bbf4-65418886ce7a | -19.48785 | -44.12975 | 2026-09-04 04:21:00 | NPP-375D | PRUDENTE DE MORAIS | MINAS GERAIS | Brasil | 3153608 | 31 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 0e5f3e84-1d5f-3829-85c5-54410f61fb55 | -13.41124 | -43.87871 | 2026-09-04 04:21:00 | NPP-375D | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| a0361d75-0e0f-3d70-99d0-3901a0577e6e | -17.09788 | -56.87309 | 2026-09-04 04:21:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 4.3 |
| 95634c33-c397-301e-8b7b-66b831732241 | -17.1017 | -56.85645 | 2026-09-04 04:21:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.1 |
| ac16ef7d-bf21-3dc8-9cb6-feba5260dd9f | -16.57085 | -51.62648 | 2026-09-04 04:21:00 | NPP-375D | PIRANHAS | GOIÁS | Brasil | 5217203 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 9cc3217a-b46a-3323-a376-9c3c9afbfc31 | -13.5832 | -47.87462 | 2026-09-04 04:21:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 2e2224b3-59a0-3e31-86fc-ef28810c0bc8 | -17.10194 | -56.85555 | 2026-09-04 04:21:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.5 |
| 8557a49b-fc8b-3d94-89d3-4bf72f08da1d | -16.17923 | -46.66738 | 2026-09-04 04:21:00 | NPP-375D | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 777f25cf-1da9-31ea-be18-1605a0462945 | -15.91406 | -50.1582 | 2026-09-04 04:21:00 | NPP-375D | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| c5904a03-c6bd-3855-84fb-e692bbd82e20 | -17.09529 | -56.85484 | 2026-09-04 04:21:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.2 |
| 4cef0424-7f42-3cd8-b943-59333fe800b9 | -13.40848 | -43.87458 | 2026-09-04 04:21:00 | NPP-375D | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 98fa8ec2-746f-3e2b-ad52-c57ece4c99cb | -15.90793 | -50.16677 | 2026-09-04 04:21:00 | NPP-375D | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| d5efe8bf-2104-399e-ab16-481e19b1b20a | -17.10042 | -56.862 | 2026-09-04 04:21:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.5 |
| 42c0f4b3-4e7f-3758-b6db-f4303fa1234c | -13.5832 | -47.87093 | 2026-09-04 04:21:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 9d9a05b4-e6e9-3274-a2c7-efbda61c2d96 | -13.5823 | -47.87594 | 2026-09-04 04:21:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 7.8 |
| 20d74d45-eb4f-3eee-ad19-27ebf9d7e5df | -16.6643 | -43.63832 | 2026-09-04 04:21:00 | NPP-375D | FRANCISCO SÁ | MINAS GERAIS | Brasil | 3126703 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 0fb751a3-7704-3234-b091-2e650119b74e | -14.79491 | -47.13585 | 2026-09-04 04:21:00 | NPP-375D | VILA BOA | GOIÁS | Brasil | 5222203 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 7bd61f45-4adb-3a25-b729-67c667d76df2 | -16.66154 | -43.63415 | 2026-09-04 04:21:00 | NPP-375D | FRANCISCO SÁ | MINAS GERAIS | Brasil | 3126703 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 7a1800d6-0bd9-36bb-bff3-43c3f60261d6 | -15.32257 | -47.04583 | 2026-09-04 04:21:00 | NPP-375D | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 4.7 |
| aaa8d4bb-b14f-3f34-89b9-a80ea4ad0589 | -17.09678 | -56.84838 | 2026-09-04 04:21:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.4 |
| 1482602c-f828-371f-b240-79d536f7d260 | -16.65821 | -43.63359 | 2026-09-04 04:21:00 | NPP-375D | FRANCISCO SÁ | MINAS GERAIS | Brasil | 3126703 | 31 | 33 | nan | nan | nan | Cerrado | 12.4 |
| db9782bc-be16-3d1d-8a80-6500a751cac3 | -14.91061 | -44.67278 | 2026-09-04 04:21:00 | NPP-375D | CÔNEGO MARINHO | MINAS GERAIS | Brasil | 3117836 | 31 | 33 | nan | nan | nan | Cerrado | 8.5 |
| 619f180a-790b-3735-a81d-e67786a08d7b | -15.67925 | -51.84425 | 2026-09-04 04:21:00 | NPP-375D | ARAGUAIANA | MATO GROSSO | Brasil | 5101001 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 65c6a56b-b876-34c7-aed2-64e58d238028 | -19.62461 | -46.9688 | 2026-09-04 04:21:00 | NPP-375D | ARAXÁ | MINAS GERAIS | Brasil | 3104007 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| e5c85fd6-6642-3638-a39b-9e2b445ed736 | -13.41515 | -43.8757 | 2026-09-04 04:21:00 | NPP-375D | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |


[Clique aqui para ver as próximas entradas](README14.md)
