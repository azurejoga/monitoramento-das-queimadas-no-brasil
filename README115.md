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

## Dados Diários - Página 115

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 19519c36-e873-3ee0-a9c7-d6d7758b6702 | -10.66296 | -65.19803 | 2025-09-13 05:50:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 992b698f-860e-304c-ac02-3a7960c38ae5 | -12.86594 | -62.12361 | 2025-09-13 05:50:00 | NOAA-20 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 2e0c6488-3fdf-3140-bfef-214528f8d4a2 | -10.63473 | -64.9752 | 2025-09-13 05:50:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 2b1cc532-2516-339e-8245-8486dd847c22 | -14.71775 | -59.72265 | 2025-09-13 05:50:00 | NOAA-20 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| cf0733bc-d37d-3686-8a00-6e5bfeb43277 | -11.36972 | -59.14359 | 2025-09-13 05:50:00 | NOAA-20 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 0c592d7f-b774-3d3a-a253-8b7761d8c4e5 | -11.38488 | -63.35644 | 2025-09-13 05:50:00 | NOAA-20 | SÃO MIGUEL DO GUAPORÉ | RONDÔNIA | Brasil | 1100320 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| c1e3fa55-ff47-36f6-873e-057ae3713c3c | -11.77809 | -64.93922 | 2025-09-13 05:50:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 066f7d81-db3b-3ba8-bcde-feeee4461a50 | -10.66356 | -65.19405 | 2025-09-13 05:50:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 8e38b9de-e243-3243-9048-572c4764d3ed | -12.86314 | -62.14479 | 2025-09-13 05:50:00 | NOAA-20 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 396b0117-1cc4-37d8-af22-bc4f964e0d0f | -12.88013 | -62.11693 | 2025-09-13 05:50:00 | NOAA-20 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| ae6ab174-1bb8-332c-a0b8-dd75e41424ee | -15.59602 | -54.77334 | 2025-09-13 05:50:00 | NOAA-20 | DOM AQUINO | MATO GROSSO | Brasil | 5103601 | 51 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 17c6472f-deab-34e0-823c-6137836f343d | -15.20977 | -56.68607 | 2025-09-13 05:50:00 | NOAA-20 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 3.1 |
| f864256d-3092-32e3-a1f2-68e4db7fca48 | -10.90099 | -68.30251 | 2025-09-13 05:50:00 | NOAA-20 | XAPURI | ACRE | Brasil | 1200708 | 12 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 2f34498d-7aa8-3f5d-92cd-db3d80858f1b | -14.723 | -59.7233 | 2025-09-13 05:50:00 | NOAA-20 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 1a115a5b-d8c2-3c7b-a723-0e787e71c547 | -11.36932 | -59.1467 | 2025-09-13 05:50:00 | NOAA-20 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 78a806e2-fe6c-3b89-8f94-9b66633db03d | -11.77211 | -64.92973 | 2025-09-13 05:50:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 47dbbccd-6b2d-3688-ab7d-313f0784ed12 | -12.86159 | -62.12302 | 2025-09-13 05:50:00 | NOAA-20 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 6e53fb3e-5ebf-38e3-8f4f-137a1d28cd37 | -10.89779 | -68.21563 | 2025-09-13 05:50:00 | NOAA-20 | XAPURI | ACRE | Brasil | 1200708 | 12 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 46a8ef0b-94a9-3e08-98f8-a65c45f78a68 | -12.86103 | -62.12726 | 2025-09-13 05:50:00 | NOAA-20 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 4086ef66-d51d-38e5-9fb0-e59b6118585e | -15.59139 | -54.77199 | 2025-09-13 05:50:00 | NOAA-20 | DOM AQUINO | MATO GROSSO | Brasil | 5103601 | 51 | 33 | nan | nan | nan | Cerrado | 8.8 |
| 1b022b01-1c36-3633-9d5e-a51ef773afdd | -12.87617 | -62.14661 | 2025-09-13 05:50:00 | NOAA-20 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 3.0 |
| d602fdda-8a7f-32d6-a50b-4e4659fae097 | -12.89282 | -62.0883 | 2025-09-13 05:50:00 | NOAA-20 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 9cc00b56-9f1c-38da-bc4a-9857be5f8b19 | -10.84241 | -68.30737 | 2025-09-13 05:50:00 | NOAA-20 | XAPURI | ACRE | Brasil | 1200708 | 12 | 33 | nan | nan | nan | Amazônia | 0.6 |
| f7d067d0-90ce-3363-9761-5f8b5ce86d12 | -10.66648 | -65.19857 | 2025-09-13 05:50:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 5f9bdfbd-a002-3638-9cec-f143ef64f0c0 | -11.37012 | -59.14048 | 2025-09-13 05:50:00 | NOAA-20 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 23688039-258c-3f34-9f9f-85a142da736c | -12.38746 | -62.20538 | 2025-09-13 05:50:00 | NOAA-20 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 6031c7e0-abf7-3a7c-8cfe-011967666086 | -14.72338 | -59.72016 | 2025-09-13 05:50:00 | NOAA-20 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b456713d-b233-3014-a359-1b913e00e107 | -12.86047 | -62.13149 | 2025-09-13 05:50:00 | NOAA-20 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 62166310-a6d4-3fe9-985b-5c7cb49da53c | -10.66334 | -65.19635 | 2025-09-13 05:50:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 2.8 |
| e8c4821f-bee4-32c0-a038-795e5cddf2c3 | -12.88069 | -62.11271 | 2025-09-13 05:50:00 | NOAA-20 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 2990bfe1-03b7-35af-b536-9c6bc58f77b1 | -20.84906 | -56.87428 | 2025-09-13 05:53:00 | NOAA-20 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 5ea08402-4f96-3904-83fc-3909c6edcf18 | -22.26679 | -56.80956 | 2025-09-13 05:53:00 | NOAA-20 | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 2c654fb0-ec40-3bf4-a327-1ae06f26bb71 | -22.26591 | -56.80973 | 2025-09-13 05:53:00 | NOAA-20 | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 2.6 |
| e64adc6d-5ae5-3ccb-a72b-dd404a7fb380 | -22.27275 | -56.81025 | 2025-09-13 05:53:00 | NOAA-20 | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 76f3438c-2ced-3926-960e-d6b51788e84a | -20.84597 | -56.8781 | 2025-09-13 05:53:00 | NOAA-20 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 0.7 |
| f3da746a-d33c-39c9-be2a-2e4bc76e89b8 | -20.84637 | -56.87325 | 2025-09-13 05:53:00 | NOAA-20 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 0.7 |
| b26afb5a-8a4e-3d54-abf2-6c4c6acec8c9 | -20.84864 | -56.8796 | 2025-09-13 05:53:00 | NOAA-20 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 231c07fa-bfbe-3818-b1e2-c9faf7545772 | -9.2843 | -59.418 | 2025-09-13 06:00:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 39.6 |
| b5ee3060-e70e-34be-b306-6ae78699bf89 | -20.1208 | -46.9208 | 2025-09-13 06:00:00 | GOES-19 | SACRAMENTO | MINAS GERAIS | Brasil | 3156908 | 31 | 33 | nan | nan | nan | Cerrado | 62.5 |
| e8fc0512-1823-3432-89c4-308d23932528 | -10.1611 | -64.7401 | 2025-09-13 06:00:00 | GOES-19 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 53.6 |
| c26bc8bd-97c5-39f0-a4a5-c75bfc588c47 | -9.5324 | -54.6277 | 2025-09-13 06:00:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 87.0 |
| 172c84c3-ecd1-3df6-910f-c22d56612599 | -9.2656 | -59.4191 | 2025-09-13 06:00:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 112.9 |
| 36228e38-3fab-32ea-a469-2bd8b6009776 | -9.5137 | -54.6292 | 2025-09-13 06:00:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 86.3 |
| 350f5464-9270-3478-94ed-20a50cd9afce | -9.2658 | -59.3997 | 2025-09-13 06:00:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 102.6 |
| 479fd57f-cd6b-3dbc-9338-a420d52bba2a | -15.4517 | -47.3291 | 2025-09-13 06:10:00 | GOES-19 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 59.8 |
| 3b6474f8-fc16-3cc2-a60a-d43c8a9f4d2f | -11.0948 | -51.4289 | 2025-09-13 06:10:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 91.6 |
| 4e12137a-42de-35a4-8875-4cc0ee6ef44b | -11.8656 | -50.6005 | 2025-09-13 06:10:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 137.4 |
| 4a476774-ae54-39ea-8cbc-008c3ddf1f64 | -9.2472 | -59.4007 | 2025-09-13 06:10:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 40.2 |
| 069ca665-89f0-3872-892d-12eed8a3cb9e | -9.2844 | -59.3986 | 2025-09-13 06:10:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 40.3 |
| 401bcda9-b2ee-3096-82ce-a3c16adc2c4b | -11.8846 | -50.5983 | 2025-09-13 06:10:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 148.9 |
| c8d0179d-349c-3f4d-8a24-e2f2f99f8224 | -11.885 | -50.5768 | 2025-09-13 06:10:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 363.7 |
| 8f0c19ac-048a-33bd-8727-af11e3f9b376 | -10.1611 | -64.7401 | 2025-09-13 06:10:00 | GOES-19 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 45.4 |
| 2990fa65-4f4b-3545-8e8c-a36eaef70eea | -16.3422 | -51.5217 | 2025-09-13 06:10:00 | GOES-19 | ARENÓPOLIS | GOIÁS | Brasil | 5202353 | 52 | 33 | nan | nan | nan | Cerrado | 70.4 |
| a439f17f-aa13-31dd-ad7f-68b4f89d6d7d | -21.5912 | -48.419 | 2025-09-13 06:10:00 | GOES-19 | MATÃO | SÃO PAULO | Brasil | 3529302 | 35 | 33 | nan | nan | nan | Cerrado | 61.0 |
| e0374721-708f-3bea-a56c-ee7e5588f60d | -11.8853 | -50.5554 | 2025-09-13 06:10:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 132.2 |
| 67a6844b-1411-3fc5-99c6-5fdfd26437fd | -11.8662 | -50.5576 | 2025-09-13 06:10:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 148.5 |
| bad0f371-75a7-376e-87d5-dc1a28c144bd | -9.5324 | -54.6277 | 2025-09-13 06:10:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 92.6 |
| 14c858fd-91e9-311a-8ade-e41349cd64a6 | -9.2658 | -59.3997 | 2025-09-13 06:10:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 102.0 |
| 602f508d-4a63-3dc8-833a-6589cb36584f | -9.2843 | -59.418 | 2025-09-13 06:10:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 50.0 |
| 2760d3a7-eee0-3901-8dfc-e4373d2c3d40 | -9.2656 | -59.4191 | 2025-09-13 06:10:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 104.5 |
| 9efc6ce1-8c02-3225-a5b7-b4a5010f9e5b | -11.8659 | -50.5791 | 2025-09-13 06:10:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 348.8 |
| 6d4ad033-8e98-3a9b-8420-c25563a8e06d | -9.5137 | -54.6292 | 2025-09-13 06:10:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 111.9 |
| 67d97800-73cc-36f3-96ae-0033bb335ab5 | -14.1698 | -46.2735 | 2025-09-13 06:20:00 | GOES-19 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 165.4 |
| e2ac6ed4-cafe-30e0-b1b7-70ceac76488c | -9.2472 | -59.4007 | 2025-09-13 06:20:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 40.0 |
| fe7b4cb6-aa75-32e2-869b-31293a5da3a2 | -12.8263 | -47.9263 | 2025-09-13 06:20:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 59.0 |
| 115e3a46-433f-3273-8715-73ef4577daf8 | -15.4517 | -47.3291 | 2025-09-13 06:20:00 | GOES-19 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 62.8 |
| 7b60d354-de75-321f-9796-27466cfc63ec | -9.2658 | -59.3997 | 2025-09-13 06:20:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 164.5 |
| ba722bad-ee6e-3d84-b6ac-bc34866fa2df | -9.2656 | -59.4191 | 2025-09-13 06:20:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 135.0 |
| 3ffe8027-e7af-37ab-81af-3b4454cac924 | -9.2844 | -59.3986 | 2025-09-13 06:20:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 49.4 |
| 1f188dce-0e6c-3cc2-8a75-5e71dedb0f5e | -11.8846 | -50.5983 | 2025-09-13 06:20:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 72.1 |
| e6fab3e6-93fc-386c-9fb8-0ff2575489b0 | -14.1898 | -46.2472 | 2025-09-13 06:20:00 | GOES-19 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 112.9 |
| 42de3bc5-c901-36ef-83b6-c725838235e2 | -21.0633 | -48.9356 | 2025-09-13 06:20:00 | GOES-19 | CATANDUVA | SÃO PAULO | Brasil | 3511102 | 35 | 33 | nan | nan | nan | Mata Atlântica | 66.2 |
| cd443747-b918-3b8c-a3fe-6c10c8316154 | -11.1426 | -50.7028 | 2025-09-13 06:20:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 170.9 |
| 3f9cb0be-370f-309f-9786-4accad640953 | -11.8659 | -50.5791 | 2025-09-13 06:20:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 123.8 |
| 32b67970-fc12-3416-b7cd-e99b36d4112a | -14.1708 | -46.2275 | 2025-09-13 06:20:00 | GOES-19 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 68.3 |
| a7128ce0-4bf2-3c4a-b968-adc80f3cf28c | -11.8662 | -50.5576 | 2025-09-13 06:20:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 74.4 |
| 599e06a7-de73-388a-b3a7-5471a641b2ea | -14.1703 | -46.2505 | 2025-09-13 06:20:00 | GOES-19 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 218.3 |
| 7bee09dd-a74a-307c-a414-bdb15854d21c | -18.0298 | -50.9606 | 2025-09-13 06:20:00 | GOES-19 | RIO VERDE | GOIÁS | Brasil | 5218805 | 52 | 33 | nan | nan | nan | Cerrado | 57.2 |
| 4e48cc27-6593-3c06-8728-aa7a48f86253 | -11.1429 | -50.6815 | 2025-09-13 06:20:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 81.9 |
| 3a5ec75d-c9dc-30ce-bdd0-7e3166b06996 | -11.885 | -50.5768 | 2025-09-13 06:20:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 156.1 |
| 932f32cd-c7e1-3ecd-9892-fa05d7ba0c04 | -14.2088 | -46.2669 | 2025-09-13 06:20:00 | GOES-19 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 67.1 |
| 57fe8121-38e6-36c1-a2b7-4d3230f8df69 | -9.2843 | -59.418 | 2025-09-13 06:20:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 49.1 |
| b7c5d386-550b-394b-82dc-fca8d2ce8ae8 | -12.006 | -47.7505 | 2025-09-13 06:20:00 | GOES-19 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 65.6 |
| ef62310d-7eac-3028-9391-73443f2788d5 | -11.1616 | -50.7008 | 2025-09-13 06:20:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 238.5 |
| 93226ce1-ebd2-37c4-91d5-ce6a0d9cdb4b | -11.0948 | -51.4289 | 2025-09-13 06:20:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 78.3 |
| aa31c209-cdbb-34ca-838b-4cf38f31e26d | -9.5137 | -54.6292 | 2025-09-13 06:20:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 85.6 |
| 4e1fcb22-4fd6-3a83-823e-b1d121cc512c | -11.1619 | -50.6794 | 2025-09-13 06:20:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 115.2 |
| 3e47d8ca-fe1b-3dd5-85ba-a49df20e9b9f | -14.1893 | -46.2702 | 2025-09-13 06:20:00 | GOES-19 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 183.2 |
| 91939d27-0c06-3a0a-911f-a96d680d9607 | -9.5324 | -54.6277 | 2025-09-13 06:20:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 105.9 |
| 417945cb-72e8-3473-9182-42243ffcbe5d | -9.5324 | -54.6277 | 2025-09-13 06:30:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 89.2 |
| 5ab7e5bc-bd86-32a4-b390-b550cc34ca37 | -15.6906 | -49.9018 | 2025-09-13 06:30:00 | GOES-19 | ITAPURANGA | GOIÁS | Brasil | 5211206 | 52 | 33 | nan | nan | nan | Cerrado | 82.5 |
| 1b491ce1-2f2f-31f5-a5d4-0b05d276057a | -21.0845 | -48.9077 | 2025-09-13 06:30:00 | GOES-19 | CATANDUVA | SÃO PAULO | Brasil | 3511102 | 35 | 33 | nan | nan | nan | Mata Atlântica | 80.2 |
| 73a8b56f-c69f-31d7-934e-09257cf96950 | -21.0633 | -48.9356 | 2025-09-13 06:30:00 | GOES-19 | CATANDUVA | SÃO PAULO | Brasil | 3511102 | 35 | 33 | nan | nan | nan | Mata Atlântica | 337.0 |
| 6bcb95be-86f9-34a9-9f6d-9fda01a5f9d5 | -18.0303 | -50.9385 | 2025-09-13 06:30:00 | GOES-19 | RIO VERDE | GOIÁS | Brasil | 5218805 | 52 | 33 | nan | nan | nan | Cerrado | 67.4 |
| f972e16c-c62b-3fb4-a555-a4cb6a144d50 | -12.006 | -47.7505 | 2025-09-13 06:30:00 | GOES-19 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 74.5 |
| 261bc555-1db3-39e4-b6e3-aa4e203c2ea7 | -14.1698 | -46.2735 | 2025-09-13 06:30:00 | GOES-19 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 185.2 |
| 60c55f1b-2088-3f9d-8b03-737b44baff16 | -9.2658 | -59.3997 | 2025-09-13 06:30:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 165.9 |
| f3dbf626-15c8-3779-ad28-84c31348964d | -21.0639 | -48.9124 | 2025-09-13 06:30:00 | GOES-19 | CATANDUVA | SÃO PAULO | Brasil | 3511102 | 35 | 33 | nan | nan | nan | Mata Atlântica | 139.9 |
| b9a3eb1b-1f40-326d-bbb5-5e61ae0419ed | -15.4517 | -47.3291 | 2025-09-13 06:30:00 | GOES-19 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 67.7 |
| da56ef4b-52b9-3d95-8d3d-64e10fce965f | -14.4584 | -47.34 | 2025-09-13 06:30:00 | GOES-19 | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 81.3 |


[Clique aqui para ver as próximas entradas](README116.md)
