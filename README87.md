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

## Dados Diários - Página 87

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 12cef9b7-82f8-397c-8c84-ae1f56c1122f | -7.21401 | -45.44295 | 2025-08-31 12:53:00 | TERRA_M-T | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 81.5 |
| 32a032db-7fd5-3540-a540-d91b0160f855 | -6.34254 | -53.42999 | 2025-08-31 12:53:00 | TERRA_M-T | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 21.9 |
| 1b046a9e-c010-3fcb-870e-b04cc4db92e1 | -8.47899 | -47.45494 | 2025-08-31 12:53:00 | TERRA_M-T | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 54.9 |
| 1693ca3f-6082-32ab-bb55-8c0eeb986703 | -7.87028 | -46.96667 | 2025-08-31 12:53:00 | TERRA_M-T | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 677.1 |
| d10b59d9-9cd5-3df7-a959-349fcf58156a | -7.21977 | -45.40901 | 2025-08-31 12:53:00 | TERRA_M-T | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 46.4 |
| 06266248-67f6-3490-8a11-5b1774a1af1c | -7.86392 | -46.92857 | 2025-08-31 12:53:00 | TERRA_M-T | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 75.1 |
| 0bb1d855-e5dd-3759-9868-f5ba810ab814 | -6.33316 | -53.42874 | 2025-08-31 12:53:00 | TERRA_M-T | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 10.1 |
| ecc51359-7115-3f3c-b4f1-e0bd9fd55721 | -7.41845 | -47.46086 | 2025-08-31 12:53:00 | TERRA_M-T | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 27.9 |
| a992ba2e-9d61-3846-9bbc-49325cbf3d4b | -7.85454 | -46.96485 | 2025-08-31 12:53:00 | TERRA_M-T | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 190.1 |
| 7b35dde3-86c2-3240-9376-56cc161f1892 | -7.85997 | -46.96042 | 2025-08-31 12:53:00 | TERRA_M-T | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 736.8 |
| 232c4f55-b19e-3010-87fb-35ef271ceb8c | -7.21507 | -45.44985 | 2025-08-31 12:53:00 | TERRA_M-T | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 45.4 |
| f2eec3de-28be-3fd7-933a-c25e66c80869 | -8.48207 | -47.44888 | 2025-08-31 12:53:00 | TERRA_M-T | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 95.9 |
| 0fd31719-d3d9-3410-bb15-6607df3e2570 | -6.27104 | -53.67212 | 2025-08-31 12:53:00 | TERRA_M-T | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 8.6 |
| 2a33cf01-5f3b-3a8d-94ab-3a77862dbdea | -6.62266 | -53.33246 | 2025-08-31 12:53:00 | TERRA_M-T | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 9.9 |
| 816b84fc-1584-3ec5-9117-b42378e56198 | -8.29117 | -46.31824 | 2025-08-31 12:53:00 | TERRA_M-T | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 66.7 |
| be906adc-18e8-3b19-b1eb-253e456e7b6c | -5.34593 | -47.29008 | 2025-08-31 12:53:00 | TERRA_M-T | JOÃO LISBOA | MARANHÃO | Brasil | 2105500 | 21 | 33 | nan | nan | nan | Amazônia | 264.5 |
| c42cf7bd-bb97-3110-96f1-600a270f7ed4 | -6.34494 | -58.31755 | 2025-08-31 12:53:00 | TERRA_M-T | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 8.6 |
| 686c5eea-1d01-332e-865a-cd8224e3f891 | -8.30194 | -46.3147 | 2025-08-31 12:53:00 | TERRA_M-T | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 86.2 |
| f290a799-40ea-38bd-a037-a40a502ac93d | -6.81987 | -58.96955 | 2025-08-31 12:53:00 | TERRA_M-T | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 9.3 |
| cbea8ac6-d846-3a8b-bf9d-460ad94a5605 | -9.886 | -45.77024 | 2025-08-31 12:55:00 | TERRA_M-T | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 46.3 |
| d8ccb3da-b6cb-354e-af44-38b2713b8e52 | -12.39408 | -46.42185 | 2025-08-31 12:55:00 | TERRA_M-T | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 227.8 |
| 6aee800b-a7a8-32fa-8c39-ee8c09563bab | -10.03758 | -48.10284 | 2025-08-31 12:55:00 | TERRA_M-T | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 30.8 |
| caca119c-7e16-32f6-a2b0-7427eb4fbbbc | -11.8065 | -51.44427 | 2025-08-31 12:55:00 | TERRA_M-T | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Cerrado | 19.7 |
| 244c7757-c044-3f66-99fd-35032d9e2e20 | -9.68244 | -47.02995 | 2025-08-31 12:55:00 | TERRA_M-T | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 40.4 |
| 4d070529-8040-3b00-9c7d-e29c751d6952 | -10.94362 | -50.84592 | 2025-08-31 12:55:00 | TERRA_M-T | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 31.0 |
| 0b1b330d-6ffe-3106-b5c5-25280585a458 | -10.88004 | -55.76481 | 2025-08-31 12:55:00 | TERRA_M-T | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 8.6 |
| 78bfb901-fd0e-3bd6-9abf-41c73bb340db | -9.26757 | -47.05949 | 2025-08-31 12:55:00 | TERRA_M-T | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 88.0 |
| c970b12a-a792-3435-8033-2fdee597f99e | -9.69095 | -47.03653 | 2025-08-31 12:55:00 | TERRA_M-T | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 56.0 |
| 4bcf8bf4-96a1-353a-b372-45e3c3b4fed8 | -10.67043 | -50.53938 | 2025-08-31 12:55:00 | TERRA_M-T | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 19.1 |
| 9c6fc077-faad-3781-90ae-de0ce02ede57 | -9.00346 | -50.08421 | 2025-08-31 12:55:00 | TERRA_M-T | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 22.0 |
| 0a178154-a310-3b9c-ba71-a5a93c384e1c | -11.91063 | -46.37627 | 2025-08-31 12:55:00 | TERRA_M-T | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 102.2 |
| f3eb8421-4503-3de6-9d06-20c50228c870 | -10.92795 | -56.8466 | 2025-08-31 12:55:00 | TERRA_M-T | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 7.1 |
| a6709784-6b5e-3e8b-b634-9cac17181706 | -9.32333 | -56.91111 | 2025-08-31 12:55:00 | TERRA_M-T | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 6.6 |
| 7cf8f577-9124-3414-9a29-5bb40f788cc8 | -10.03828 | -48.09602 | 2025-08-31 12:55:00 | TERRA_M-T | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 43.3 |
| a7068e26-fb38-3061-93f7-abcc4494e0b6 | -12.39277 | -46.41475 | 2025-08-31 12:55:00 | TERRA_M-T | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 212.2 |
| 2085d5f0-fa05-31b2-b1b5-9702ac0cf1dc | -9.94095 | -51.60588 | 2025-08-31 12:55:00 | TERRA_M-T | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 15.1 |
| 852641a0-1e02-3bec-a601-f14f4af285c7 | -11.85205 | -46.40808 | 2025-08-31 12:55:00 | TERRA_M-T | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 93.7 |
| f70657a2-853e-3e81-a88a-6df0dea92f99 | -9.70811 | -48.31598 | 2025-08-31 12:55:00 | TERRA_M-T | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 25.5 |
| 57efb463-c71a-3d12-abc8-c51a72747ee6 | -8.11927 | -61.22078 | 2025-08-31 12:55:00 | TERRA_M-T | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 14.3 |
| 5d5195f2-2027-3eb0-a410-c6e0c59ec5dd | -8.17578 | -61.36881 | 2025-08-31 12:55:00 | TERRA_M-T | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 22.4 |
| dfed52a1-2991-3204-9d60-41ff6f8b460c | -9.24784 | -47.09033 | 2025-08-31 12:55:00 | TERRA_M-T | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 62.8 |
| d2b8390a-4d1c-3540-b736-2bfe9c7a9be9 | -8.96801 | -46.73375 | 2025-08-31 12:55:00 | TERRA_M-T | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 59.1 |
| 77d05b58-46c2-3f70-9598-d3870b756d6b | -8.97668 | -46.72945 | 2025-08-31 12:55:00 | TERRA_M-T | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 53.9 |
| 7371a3aa-b634-3429-8b2e-ad60e6c79f42 | -10.68278 | -50.54091 | 2025-08-31 12:55:00 | TERRA_M-T | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 90.1 |
| f3d39b2a-f42b-31d5-9489-aa3a6eba0104 | -10.12892 | -58.01661 | 2025-08-31 12:55:00 | TERRA_M-T | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 17.1 |
| 0ff68c68-8472-3740-aa33-a4b462133836 | -8.64943 | -61.93616 | 2025-08-31 12:55:00 | TERRA_M-T | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 29.4 |
| b7a874ce-2dbb-34fd-bcb8-f1728e7bddfd | -12.08146 | -50.63929 | 2025-08-31 12:55:00 | TERRA_M-T | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 34.2 |
| ed5c62ba-a2ac-3f18-a748-3db8b27f39f5 | -8.12496 | -55.56625 | 2025-08-31 12:55:00 | TERRA_M-T | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 8.9 |
| 659f66af-bb0a-3971-ac3d-fbf31f8a8f75 | -9.26375 | -47.09211 | 2025-08-31 12:55:00 | TERRA_M-T | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 91.7 |
| 2d67b668-0d47-339e-b91e-3569b32aa537 | -8.64338 | -61.94665 | 2025-08-31 12:55:00 | TERRA_M-T | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 33.5 |
| a11d876f-cb6c-3962-931d-010beac1f427 | -9.25476 | -47.08387 | 2025-08-31 12:55:00 | TERRA_M-T | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 116.8 |
| 8cd8644e-b848-3867-a3aa-80e9bde6db75 | -9.67842 | -47.06345 | 2025-08-31 12:55:00 | TERRA_M-T | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 44.2 |
| ae8d8163-e437-3d76-a1ef-0c0457cae0f8 | -9.25163 | -47.05768 | 2025-08-31 12:55:00 | TERRA_M-T | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 57.7 |
| 2ab779a1-9a59-3604-98bb-1daa2ea17422 | -12.3882 | -46.45631 | 2025-08-31 12:55:00 | TERRA_M-T | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 59.7 |
| 9bcb5f9d-01ed-32de-9ea2-e293b5e3d67c | -8.16909 | -61.36097 | 2025-08-31 12:55:00 | TERRA_M-T | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 23.5 |
| 993c884d-87cd-33f1-b8ea-bed8c9cf9aae | -9.94076 | -51.61253 | 2025-08-31 12:55:00 | TERRA_M-T | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 16.9 |
| 440a48e4-9bf3-3e19-a3d7-3eac1f14d2f9 | -11.80436 | -51.43367 | 2025-08-31 12:55:00 | TERRA_M-T | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Cerrado | 28.8 |
| 21e25617-dd28-36ec-88cd-799b47253a0a | -10.92925 | -56.83764 | 2025-08-31 12:55:00 | TERRA_M-T | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 7.8 |
| b2dc473f-3ba3-31a0-afbb-88a73a9e13e1 | -9.33485 | -56.13269 | 2025-08-31 12:55:00 | TERRA_M-T | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 8621897a-7249-3945-a7b5-5262cd703913 | -11.91239 | -46.38151 | 2025-08-31 12:55:00 | TERRA_M-T | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 100.2 |
| b060be56-3dfb-3d30-9fad-92bade60b035 | -12.08005 | -50.63243 | 2025-08-31 12:55:00 | TERRA_M-T | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 32.0 |
| dd5051fa-642f-32aa-99fd-084de174e39d | -8.64654 | -61.95401 | 2025-08-31 12:55:00 | TERRA_M-T | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 37.5 |
| a6983209-28d0-3b3e-8145-a07b90e47e4c | -11.20868 | -55.91956 | 2025-08-31 12:55:00 | TERRA_M-T | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 7.0 |
| e6d4bb01-181d-3989-baaf-ac004f09bc38 | -10.94585 | -50.82837 | 2025-08-31 12:55:00 | TERRA_M-T | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 25.6 |
| 021e6b22-1a21-3bfd-97df-ddc4d70ca63e | -12.62803 | -48.18668 | 2025-08-31 12:57:00 | TERRA_M-T | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 218.3 |
| 0e3d7065-987e-3c0d-ba37-4eb2cbf3ed14 | -12.64343 | -48.18805 | 2025-08-31 12:57:00 | TERRA_M-T | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 54.6 |
| 91daf889-2f42-3c1e-8baa-af704d738d18 | -11.7812 | -54.24584 | 2025-08-31 12:57:00 | TERRA_M-T | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 10.2 |
| ada1e2e7-daac-3b90-9c64-7f01c7961b35 | -14.79238 | -46.74216 | 2025-08-31 12:57:00 | TERRA_M-T | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 44.1 |
| f19560b4-db7a-3242-9ecc-7c94c97f5ee7 | -14.98907 | -48.15008 | 2025-08-31 12:57:00 | TERRA_M-T | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 44.3 |
| c7e62118-d089-389c-9240-e1108925b63c | -12.62491 | -48.21608 | 2025-08-31 12:57:00 | TERRA_M-T | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 361.9 |
| c0123411-7c3d-3d46-9407-aebb78da19f4 | -14.33497 | -51.86816 | 2025-08-31 12:57:00 | TERRA_M-T | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 35.5 |
| c57cd796-0349-39a8-bbea-5c53401fe2ab | -16.22423 | -52.69538 | 2025-08-31 12:57:00 | TERRA_M-T | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 51.0 |
| b037bd90-e2d8-3e5c-8f5b-ab119e402866 | -13.80343 | -60.08999 | 2025-08-31 12:57:00 | TERRA_M-T | COMODORO | MATO GROSSO | Brasil | 5103304 | 51 | 33 | nan | nan | nan | Amazônia | 9.3 |
| 1ef75675-7315-34e9-84b1-6701f6fa8731 | -12.64025 | -48.21762 | 2025-08-31 12:57:00 | TERRA_M-T | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 169.1 |
| 278d8e73-d379-3d5e-9e5d-3b21f1d71a6b | -14.68019 | -56.18687 | 2025-08-31 12:57:00 | TERRA_M-T | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 298fe6a3-7f87-39f6-91a2-e3510969b21f | -11.78264 | -54.23524 | 2025-08-31 12:57:00 | TERRA_M-T | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 9.7 |
| f8ec52f0-73c3-3e0e-b2d7-6fac94d70a01 | -13.34854 | -46.9487 | 2025-08-31 12:57:00 | TERRA_M-T | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 70.1 |
| 8a701d32-7beb-3df1-991b-7a02fcd0547d | -12.62777 | -48.21105 | 2025-08-31 12:57:00 | TERRA_M-T | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 396.8 |
| a57653a6-f5a6-3e51-9502-1b228a69f207 | -14.56006 | -51.98114 | 2025-08-31 12:57:00 | TERRA_M-T | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 10.4 |
| fb03e574-082e-3175-92d7-502d6c5c3986 | -12.63704 | -48.2475 | 2025-08-31 12:57:00 | TERRA_M-T | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 44.4 |
| c6e0554a-f1ad-3939-9422-f0d4d0873fee | -14.31735 | -60.34848 | 2025-08-31 12:57:00 | TERRA_M-T | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 7.5 |
| a3b5a4f7-cfc8-3a6e-a8bf-4a6d40be2994 | -14.35445 | -51.90454 | 2025-08-31 12:57:00 | TERRA_M-T | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 23.6 |
| ab011334-7cfb-35c6-aa4c-c6c9f5174f59 | -16.22569 | -52.68912 | 2025-08-31 12:57:00 | TERRA_M-T | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 65.4 |
| 41b2b868-a19a-3540-af5b-88d3e6348130 | -12.95397 | -48.11677 | 2025-08-31 12:57:00 | TERRA_M-T | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 29.0 |
| b8f0f1f2-8664-381c-9d0d-740fd3eecadf | -13.34488 | -46.94306 | 2025-08-31 12:57:00 | TERRA_M-T | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 54.2 |
| 5a13d020-bc09-38c3-876b-e50c22d04535 | -13.47433 | -46.97707 | 2025-08-31 12:57:00 | TERRA_M-T | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 58.6 |
| 3b613c0b-d040-3b65-b7ee-f919c9ef68fa | -15.70658 | -48.92012 | 2025-08-31 12:57:00 | TERRA_M-T | PIRENÓPOLIS | GOIÁS | Brasil | 5217302 | 52 | 33 | nan | nan | nan | Cerrado | 61.4 |
| 497eef41-6923-3f7b-a405-e036ee6573f8 | -14.80917 | -46.73839 | 2025-08-31 12:57:00 | TERRA_M-T | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 154.7 |
| c44bc793-ba16-39f3-a960-0c1882ba43d4 | -14.98264 | -48.15419 | 2025-08-31 12:57:00 | TERRA_M-T | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 57.0 |
| 1ec56946-5913-3111-b6c9-b294d6f91cbc | -14.49601 | -52.98621 | 2025-08-31 12:57:00 | TERRA_M-T | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 10.5 |
| f00b60cb-2fbe-39d0-a99d-17d343d35062 | -13.2581 | -51.99015 | 2025-08-31 12:57:00 | TERRA_M-T | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Amazônia | 19.6 |
| 492117b3-cd87-3b91-9eea-55b5b8ced7df | -14.36621 | -51.90569 | 2025-08-31 12:57:00 | TERRA_M-T | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 45.8 |
| 87f59a13-6de1-3ff2-a5e9-be5e77057537 | -12.64312 | -48.21249 | 2025-08-31 12:57:00 | TERRA_M-T | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 131.8 |
| 54f81997-7743-340f-9bea-489c00add432 | -13.26007 | -51.97438 | 2025-08-31 12:57:00 | TERRA_M-T | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Amazônia | 18.0 |
| 5696445a-a679-307f-b8a0-f8b803a17c4d | -14.0174 | -54.01938 | 2025-08-31 12:57:00 | TERRA_M-T | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 11.7 |
| 996b132a-0ddb-3d12-96fe-72064ebad86d | -15.70355 | -48.94894 | 2025-08-31 12:57:00 | TERRA_M-T | PIRENÓPOLIS | GOIÁS | Brasil | 5217302 | 52 | 33 | nan | nan | nan | Cerrado | 76.8 |
| bbc4ef71-04e8-3078-a7b4-c4a12c018a3b | -14.53884 | -51.98945 | 2025-08-31 12:57:00 | TERRA_M-T | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 15.9 |
| 985c1f14-68af-3a34-a20c-e4bc9f32d235 | -12.63112 | -48.18153 | 2025-08-31 12:57:00 | TERRA_M-T | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 89.4 |
| 8e93b3e6-447e-31c3-a6c3-b7da1f42eacd | -14.02275 | -54.05545 | 2025-08-31 12:57:00 | TERRA_M-T | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 9.6 |
| 90c36fff-d86d-3cd2-b9e9-f1a87c148689 | -15.71394 | -48.9848 | 2025-08-31 12:57:00 | TERRA_M-T | PIRENÓPOLIS | GOIÁS | Brasil | 5217302 | 52 | 33 | nan | nan | nan | Cerrado | 142.1 |


[Clique aqui para ver as próximas entradas](README88.md)
