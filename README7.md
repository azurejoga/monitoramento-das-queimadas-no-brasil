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
| e83b3a2d-22e0-31ca-a2ce-25ff6e07b65c | -10.32216 | -48.03628 | 2025-09-30 00:33:00 | TERRA_M-M | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 0ba3d43c-c66c-3f82-a9b7-b0f5ba12811b | -11.21116 | -47.21302 | 2025-09-30 00:33:00 | TERRA_M-M | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 118.0 |
| 8cf381ca-3baa-3e5b-9411-3b720ff1d110 | -13.00436 | -44.11377 | 2025-09-30 00:33:00 | TERRA_M-M | SANTANA | BAHIA | Brasil | 2928208 | 29 | 33 | nan | nan | nan | Cerrado | 20.7 |
| dc709a95-c7e2-3532-8b0d-b9aebabb79d0 | -8.83259 | -46.18513 | 2025-09-30 00:33:00 | TERRA_M-M | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 7.9 |
| 9cac2cdf-deaf-3c67-89dc-81884d98fd4b | -12.82983 | -46.99664 | 2025-09-30 00:33:00 | TERRA_M-M | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 26.0 |
| fd1a5805-d75c-3073-b9f6-e0316f13e06a | -13.72237 | -48.6489 | 2025-09-30 00:33:00 | TERRA_M-M | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 11.4 |
| a0af6693-ae32-3b4c-80be-ae191d61cb88 | -15.38636 | -47.08027 | 2025-09-30 00:33:00 | TERRA_M-M | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 6c325eed-4ed6-32e8-b381-87b546643e31 | -11.46504 | -44.98029 | 2025-09-30 00:33:00 | TERRA_M-M | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 7.1 |
| ed0df8d2-5b1b-376b-89f1-08b5dd45800e | -11.45694 | -44.99338 | 2025-09-30 00:33:00 | TERRA_M-M | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 10.3 |
| c056e336-da7c-3232-8827-cbd1b56f77fb | -15.2731 | -49.25282 | 2025-09-30 00:33:00 | TERRA_M-M | GOIANÉSIA | GOIÁS | Brasil | 5208608 | 52 | 33 | nan | nan | nan | Cerrado | 11.4 |
| 6e103c1f-bc46-391b-9c49-9677f6bf4d37 | -11.88843 | -48.03191 | 2025-09-30 00:33:00 | TERRA_M-M | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 84.5 |
| b5d225ec-157c-321b-bbbb-c64a02e91235 | -10.11055 | -47.77804 | 2025-09-30 00:33:00 | TERRA_M-M | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 24.3 |
| 4b10036d-d5f3-3af6-b516-7af5ae726abc | -10.39997 | -48.14321 | 2025-09-30 00:33:00 | TERRA_M-M | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 12.5 |
| 45f1ae8b-36dc-398f-88bd-6e1f1baef534 | -12.2214 | -43.75375 | 2025-09-30 00:33:00 | TERRA_M-M | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 10.6 |
| 3212e0f6-d717-382d-bf10-1fa1a1fa3a74 | -7.83185 | -46.99165 | 2025-09-30 00:33:00 | TERRA_M-M | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 24.3 |
| 4bf6e2fb-7328-37b3-9567-efb2c1bedf6e | -13.07176 | -47.07249 | 2025-09-30 00:33:00 | TERRA_M-M | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 13.2 |
| f7313513-d28f-3478-896c-c54804fee465 | -13.38503 | -48.06396 | 2025-09-30 00:33:00 | TERRA_M-M | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 12.6 |
| be285b82-0605-3b1e-bfd1-4efe969c4609 | -10.20179 | -44.89453 | 2025-09-30 00:33:00 | TERRA_M-M | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 47.0 |
| df5fdee1-1198-3be2-93f3-9f29eb1b517a | -11.28523 | -47.81601 | 2025-09-30 00:33:00 | TERRA_M-M | SANTA ROSA DO TOCANTINS | TOCANTINS | Brasil | 1718907 | 17 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 69ec2423-fb45-393f-83dc-915c99284a0f | -14.54504 | -48.26789 | 2025-09-30 00:33:00 | TERRA_M-M | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 7.1 |
| c7386c29-32be-3694-8469-30b8374fdcc3 | -10.40456 | -49.0417 | 2025-09-30 00:33:00 | TERRA_M-M | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 5db5cb37-fbf0-31ce-87db-88106459beed | -10.20701 | -48.2106 | 2025-09-30 00:33:00 | TERRA_M-M | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 1fe13caf-c34b-3758-839d-f9a200c803fb | -11.88337 | -49.90866 | 2025-09-30 00:33:00 | TERRA_M-M | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 6.0 |
| b7b411b1-93e2-3069-a330-4b773813c793 | -13.2247 | -47.31169 | 2025-09-30 00:33:00 | TERRA_M-M | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 14.9 |
| 69a5e033-6445-32f4-824b-8be7d08062d0 | -9.13102 | -47.63879 | 2025-09-30 00:33:00 | TERRA_M-M | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 6.6 |
| ca564fc1-440c-3a1a-8559-bb696f548956 | -9.7652 | -47.81635 | 2025-09-30 00:33:00 | TERRA_M-M | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 4.3 |
| b9d5e038-3493-3ca3-8f12-64eccccfcc9d | -10.62059 | -48.53515 | 2025-09-30 00:33:00 | TERRA_M-M | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 39368aa2-b9fd-3b70-a593-3c8c1c38a455 | -7.90623 | -44.62399 | 2025-09-30 00:33:00 | TERRA_M-M | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 24.5 |
| 7fe3f127-7275-3c69-ba47-0765c9a34587 | -13.03072 | -42.80898 | 2025-09-30 00:33:00 | TERRA_M-M | MACAÚBAS | BAHIA | Brasil | 2919801 | 29 | 33 | nan | nan | nan | Caatinga | 86.8 |
| 500ce7c5-cf9f-3a68-9d1d-a735b7acacc7 | -9.51696 | -47.69648 | 2025-09-30 00:33:00 | TERRA_M-M | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 5.9 |
| cd02a953-6220-3aae-84da-d795e62dc4a4 | -9.44873 | -50.90625 | 2025-09-30 00:33:00 | TERRA_M-M | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 11.2 |
| 511d7364-0892-3c48-a918-14f6b4ac5b90 | -11.05096 | -47.65219 | 2025-09-30 00:33:00 | TERRA_M-M | PINDORAMA DO TOCANTINS | TOCANTINS | Brasil | 1717008 | 17 | 33 | nan | nan | nan | Cerrado | 12.5 |
| 8d93cfe1-f9e9-3c1e-9bfb-272eff6cd308 | -11.03355 | -49.81456 | 2025-09-30 00:33:00 | TERRA_M-M | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 9.3 |
| d6ce70f6-450c-31ef-9dbc-c17dbdbb2c07 | -10.88627 | -49.39953 | 2025-09-30 00:33:00 | TERRA_M-M | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 5.3 |
| ad093340-ced2-34fb-85bf-82f2e0af8f76 | -10.63185 | -48.55168 | 2025-09-30 00:33:00 | TERRA_M-M | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 7.9 |
| 79dd346c-0343-31f0-ab78-f8d62678177c | -9.84888 | -51.38128 | 2025-09-30 00:33:00 | TERRA_M-M | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 8.8 |
| 7556cd81-a054-3e43-96b8-2edc2ed41f71 | -9.96683 | -48.79915 | 2025-09-30 00:33:00 | TERRA_M-M | BARROLÂNDIA | TOCANTINS | Brasil | 1703107 | 17 | 33 | nan | nan | nan | Cerrado | 10.6 |
| dadeef5f-3230-3585-b119-043443998901 | -7.83323 | -47.00136 | 2025-09-30 00:33:00 | TERRA_M-M | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 28.8 |
| 7bbd4e20-82bf-37fe-89ac-806d93a3cf92 | -14.00071 | -49.63696 | 2025-09-30 00:33:00 | TERRA_M-M | MARA ROSA | GOIÁS | Brasil | 5212808 | 52 | 33 | nan | nan | nan | Cerrado | 28.1 |
| 1fb4a8c0-9f82-32dd-86ef-27445fe602af | -15.48258 | -45.87488 | 2025-09-30 00:33:00 | TERRA_M-M | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 4.8 |
| dcf87594-17c0-3c84-9125-de4febd847fd | -8.15756 | -46.38279 | 2025-09-30 00:33:00 | TERRA_M-M | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 18.5 |
| f6b1e9ba-8f13-32d7-bd6f-ab09134565a4 | -9.3085 | -54.51631 | 2025-09-30 00:33:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 12.8 |
| a1d6b775-ea59-3aaa-b55f-1a212beb5635 | -13.22156 | -50.9474 | 2025-09-30 00:33:00 | TERRA_M-M | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 15.2 |
| ea73c171-4c8e-3057-8b40-c0d0ad8214b1 | -15.32737 | -46.26763 | 2025-09-30 00:33:00 | TERRA_M-M | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 5.3 |
| a0047705-5fd2-3df5-98df-0025668c2377 | -7.54617 | -45.29658 | 2025-09-30 00:33:00 | TERRA_M-M | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 7.4 |
| 81455cfa-8cc5-366a-8fcd-44da05c06712 | -11.152 | -54.12846 | 2025-09-30 00:33:00 | TERRA_M-M | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 185.1 |
| c59ad396-c15c-3ae0-be49-0adc8f86b840 | -11.49467 | -43.51862 | 2025-09-30 00:33:00 | TERRA_M-M | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 32.4 |
| e1ac5663-81dc-3dc7-9d81-db83f20b3a20 | -8.9579 | -51.67515 | 2025-09-30 00:33:00 | TERRA_M-M | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| ad8a6f30-03aa-32ab-828c-d01aa824af57 | -15.17224 | -46.4086 | 2025-09-30 00:33:00 | TERRA_M-M | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 8.7 |
| 40db3d78-de65-3857-922d-e529cdd345f8 | -13.57019 | -48.07079 | 2025-09-30 00:33:00 | TERRA_M-M | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 0e8b759d-350d-36d4-aff6-da1be3549157 | -8.71766 | -47.97837 | 2025-09-30 00:33:00 | TERRA_M-M | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 13.4 |
| 23f776c7-d842-3d15-bd23-b157e1ba1c61 | -8.32754 | -46.21708 | 2025-09-30 00:33:00 | TERRA_M-M | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 13.9 |
| 0f71af79-ae9f-3c3e-819f-2e9d8681d056 | -13.60175 | -48.03825 | 2025-09-30 00:33:00 | TERRA_M-M | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 5.5 |
| b9438192-c863-3b8a-9324-19074bb36108 | -8.64537 | -50.195 | 2025-09-30 00:33:00 | TERRA_M-M | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 8.0 |
| 41ef1b77-96e0-37fe-9c8e-e1bee7e52e51 | -11.13028 | -48.352 | 2025-09-30 00:33:00 | TERRA_M-M | IPUEIRAS | TOCANTINS | Brasil | 1709807 | 17 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 6c32eacd-a7e3-3809-b46a-902791793607 | -8.94859 | -51.69408 | 2025-09-30 00:33:00 | TERRA_M-M | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 44.2 |
| 4fda7210-6627-3d18-951e-366c5efe9dde | -11.44004 | -44.94858 | 2025-09-30 00:33:00 | TERRA_M-M | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 1cb52576-1546-3122-b2a2-d627d7c5d3d6 | -15.60002 | -47.83305 | 2025-09-30 00:33:00 | TERRA_M-M | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 17.5 |
| a82a2605-cfa6-37b7-986d-88272689c5ef | -13.216 | -50.9837 | 2025-09-30 00:33:00 | TERRA_M-M | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 10.8 |
| fd8ade88-fcef-35c5-b9e4-e0fa0b2e6c78 | -8.7088 | -47.97966 | 2025-09-30 00:33:00 | TERRA_M-M | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 13.4 |
| 1d34ec07-f5af-3274-8080-741e921b56dc | -10.65318 | -48.57592 | 2025-09-30 00:33:00 | TERRA_M-M | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 9.8 |
| 4c32a65b-2aec-3644-b2e9-32bbf2f6af1e | -15.03985 | -46.98075 | 2025-09-30 00:33:00 | TERRA_M-M | VILA BOA | GOIÁS | Brasil | 5222203 | 52 | 33 | nan | nan | nan | Cerrado | 8.7 |
| aa3f36e8-0cc0-322c-b710-f0364bf0bdad | -14.5636 | -48.47301 | 2025-09-30 00:33:00 | TERRA_M-M | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 9.3 |
| 27f41c1b-a08c-3255-9b8a-7af82626dfa6 | -9.93518 | -47.45598 | 2025-09-30 00:33:00 | TERRA_M-M | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 25.0 |
| dac58e9f-8463-3316-aed9-20214cd8e49e | -14.58514 | -48.21828 | 2025-09-30 00:33:00 | TERRA_M-M | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 9dc56260-8222-3c75-b3a1-a245ad023141 | -11.0748 | -47.82267 | 2025-09-30 00:33:00 | TERRA_M-M | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 51.8 |
| 2d735383-1e84-3929-8c40-caf745247885 | -9.58741 | -54.58148 | 2025-09-30 00:33:00 | TERRA_M-M | GUARANTÃ DO NORTE | MATO GROSSO | Brasil | 5104104 | 51 | 33 | nan | nan | nan | Amazônia | 10.8 |
| 437925a5-dc2c-3b93-902c-9147ac123a0b | -14.51396 | -48.44223 | 2025-09-30 00:33:00 | TERRA_M-M | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 8993a6c4-104f-3b79-905c-5be659a7da69 | -11.5101 | -43.54539 | 2025-09-30 00:33:00 | TERRA_M-M | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 16.4 |
| ed5d4188-2649-3a07-8f91-6adc96512657 | -14.71629 | -48.23972 | 2025-09-30 00:33:00 | TERRA_M-M | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 6.8 |
| c15ebc9f-3135-3514-9c10-8711d24f9eec | -11.42155 | -44.89924 | 2025-09-30 00:33:00 | TERRA_M-M | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 14.5 |
| 855fea98-03a3-3880-bbb4-4c5e64926c92 | -13.80366 | -47.8887 | 2025-09-30 00:33:00 | TERRA_M-M | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 7.6 |
| 4c56170e-ac61-3bb0-8882-d4aef2f343a1 | -14.69853 | -48.24246 | 2025-09-30 00:33:00 | TERRA_M-M | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 18.3 |
| ad1745f5-8846-3b98-9a2a-a977ce885742 | -9.41041 | -54.73038 | 2025-09-30 00:33:00 | TERRA_M-M | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 15.8 |
| 5f864efc-e5d7-3de0-9869-b2c8ae119587 | -11.88333 | -48.06006 | 2025-09-30 00:33:00 | TERRA_M-M | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 33259249-a684-3770-906a-cf73a3f7950f | -14.56671 | -48.22718 | 2025-09-30 00:33:00 | TERRA_M-M | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 9.1 |
| 0c4a7c27-a69e-3e53-abe1-98f1b7db5d51 | -12.84063 | -46.99859 | 2025-09-30 00:33:00 | TERRA_M-M | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 32.9 |
| 663e1a9d-b12f-3cb4-bafd-4016cd2723a6 | -9.42192 | -54.7038 | 2025-09-30 00:33:00 | TERRA_M-M | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 16.4 |
| 5d27c132-fac8-3785-b3b7-bca1f584bc6d | -10.06603 | -50.2224 | 2025-09-30 00:33:00 | TERRA_M-M | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 17.9 |
| e4cd55ec-699a-3d85-95c4-39b26b207aa2 | -11.24176 | -47.23647 | 2025-09-30 00:33:00 | TERRA_M-M | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 18.6 |
| 64f4e1e3-596d-31a0-865c-8aa710c9fc37 | -11.14979 | -54.11024 | 2025-09-30 00:33:00 | TERRA_M-M | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 36.4 |
| ab4aef75-b4d3-349a-8094-bfd08ac3d6bb | -11.65886 | -45.32807 | 2025-09-30 00:33:00 | TERRA_M-M | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 7.0 |
| ce653b39-6a6f-3510-95ab-5812a1da4f3f | -11.49299 | -43.52542 | 2025-09-30 00:33:00 | TERRA_M-M | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 30.5 |
| a3a476af-8df4-3669-8a94-2d8798a3e49b | -13.66976 | -44.30609 | 2025-09-30 00:33:00 | TERRA_M-M | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 26.8 |
| 47455435-0911-3fe8-a22c-b8654f89a4bf | -16.1587 | -51.92724 | 2025-09-30 00:33:00 | TERRA_M-M | BOM JARDIM DE GOIÁS | GOIÁS | Brasil | 5203401 | 52 | 33 | nan | nan | nan | Cerrado | 9.0 |
| d42aebfb-9688-3d68-b346-9c7784134f88 | -12.76063 | -50.52073 | 2025-09-30 00:33:00 | TERRA_M-M | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 6.4 |
| e5c4d64d-486d-33fc-bda6-b67571d1d77a | -13.65151 | -43.0117 | 2025-09-30 00:33:00 | TERRA_M-M | RIACHO DE SANTANA | BAHIA | Brasil | 2926400 | 29 | 33 | nan | nan | nan | Caatinga | 11.4 |
| 9d795aad-a086-3dc5-8336-4f7e2e4ae7a8 | -13.65055 | -47.31925 | 2025-09-30 00:33:00 | TERRA_M-M | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 4.4 |
| c0b4abed-426b-3f8e-a8a7-322dac46ea75 | -9.3728 | -47.58465 | 2025-09-30 00:33:00 | TERRA_M-M | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 12.8 |
| df90abec-b922-32bf-aa41-422d053a258c | -13.7363 | -48.68496 | 2025-09-30 00:33:00 | TERRA_M-M | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 39.4 |
| 4407da63-d432-318c-ac50-4380c547a6be | -12.69169 | -45.28901 | 2025-09-30 00:33:00 | TERRA_M-M | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 9.2 |
| 9a33d8dd-1c72-3ef1-8983-02afd6ab0c49 | -14.51272 | -48.43291 | 2025-09-30 00:33:00 | TERRA_M-M | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 6.9 |
| f1645922-3140-3301-9f38-665db0dea289 | -11.45518 | -44.98179 | 2025-09-30 00:33:00 | TERRA_M-M | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 21.3 |
| 361c3fcc-fc95-3c65-9164-337a8bbb25c5 | -13.7785 | -47.85257 | 2025-09-30 00:33:00 | TERRA_M-M | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 4.5 |
| cb8b63a8-19ff-3b90-a070-229bf4257989 | -10.39116 | -48.14445 | 2025-09-30 00:33:00 | TERRA_M-M | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 7.2 |
| 15a6ab11-ee42-3d51-93fc-a767a534393a | -13.86142 | -44.41771 | 2025-09-30 00:33:00 | TERRA_M-M | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 33.0 |
| e87e20e2-0806-346e-8d2d-f33069ccb7e3 | -10.8351 | -47.95848 | 2025-09-30 00:33:00 | TERRA_M-M | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 15.5 |
| 48a98571-8592-326d-b0a9-e54fee1af6b6 | -13.56894 | -48.06171 | 2025-09-30 00:33:00 | TERRA_M-M | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 8.2 |
| 1dce974a-ae3e-3fbe-8dcd-3619471d4d2a | -12.77301 | -50.54111 | 2025-09-30 00:33:00 | TERRA_M-M | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 8.5 |
| 40427993-be7e-38b4-b258-13cf9af10e2f | -15.0323 | -46.99111 | 2025-09-30 00:33:00 | TERRA_M-M | VILA BOA | GOIÁS | Brasil | 5222203 | 52 | 33 | nan | nan | nan | Cerrado | 10.0 |


[Clique aqui para ver as próximas entradas](README8.md)
