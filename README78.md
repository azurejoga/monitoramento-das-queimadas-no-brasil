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

## Dados Diários - Página 78

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| ac14b4d4-94ec-39e8-ab8b-8eccd8acaff2 | -2.77367 | -49.19097 | 2025-08-16 12:51:00 | TERRA_M-T | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 11.5 |
| aea4ff8f-7a2d-3dfe-933f-c56e2c8ecbd6 | -6.45746 | -44.81116 | 2025-08-16 12:51:00 | TERRA_M-T | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 56.4 |
| b333abeb-c43d-3f84-b40a-e225f36df197 | -5.25368 | -55.64538 | 2025-08-16 12:51:00 | TERRA_M-T | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 10.7 |
| 359c0be7-4196-3140-8354-fa0e6379e076 | -6.46204 | -44.77273 | 2025-08-16 12:51:00 | TERRA_M-T | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 56.5 |
| 81861e91-e164-3e38-af2d-12fbed37cc2d | -6.45508 | -44.80423 | 2025-08-16 12:51:00 | TERRA_M-T | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 75.4 |
| c5d893c8-4188-3ea8-b18f-d9194ca54b0b | -5.57212 | -52.05201 | 2025-08-16 12:51:00 | TERRA_M-T | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 6.6 |
| ce5103a5-49e6-30f3-8b39-384cca6a502e | -6.45991 | -44.76589 | 2025-08-16 12:51:00 | TERRA_M-T | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 44.0 |
| d3a8b358-c538-34f0-95b9-2ddf398ff397 | -5.86656 | -59.90953 | 2025-08-16 12:53:00 | TERRA_M-T | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 20.3 |
| 3f13a970-4416-3af5-ac24-f85b5ac12dd6 | -7.26008 | -57.62909 | 2025-08-16 12:53:00 | TERRA_M-T | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 20.6 |
| 3d8ae7ab-940b-3cba-8299-d88f082faf47 | -7.88086 | -61.80994 | 2025-08-16 12:53:00 | TERRA_M-T | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 24.1 |
| 38047959-9ac2-30e0-8290-ac11ab485914 | -9.16054 | -59.626 | 2025-08-16 12:53:00 | TERRA_M-T | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 18.1 |
| 1226740e-b591-3ad6-975d-c6c6e3672e63 | -11.55599 | -47.25898 | 2025-08-16 12:53:00 | TERRA_M-T | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 28.8 |
| 81c89852-426e-3a15-9781-6fa0fcd543b4 | -10.62424 | -54.60435 | 2025-08-16 12:53:00 | TERRA_M-T | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 7.1 |
| 32b0eff9-40e3-3a35-b10a-157bda36fd65 | -10.93156 | -56.83629 | 2025-08-16 12:53:00 | TERRA_M-T | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 19.7 |
| 770bccfc-4e28-3c3d-b5dc-04bfa1e70abe | -12.80805 | -45.99798 | 2025-08-16 12:53:00 | TERRA_M-T | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 37.5 |
| fee75dd6-aac1-3dc6-9506-5e40f0d984ce | -11.69467 | -51.63119 | 2025-08-16 12:53:00 | TERRA_M-T | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 12.1 |
| 1c5adeb8-9b55-3b6d-9d4f-9cbf3c3352bb | -6.6345 | -60.01265 | 2025-08-16 12:53:00 | TERRA_M-T | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 15.0 |
| 9e1d0c94-f2e8-3501-938c-9411933a7ee1 | -11.02087 | -54.20589 | 2025-08-16 12:53:00 | TERRA_M-T | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 18.7 |
| c61f551d-5764-3fc1-a71b-8297ebb46f94 | -9.82533 | -45.70681 | 2025-08-16 12:53:00 | TERRA_M-T | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 46.9 |
| 471895f0-66fb-3f16-b1aa-94ceebc2b46d | -10.04908 | -59.11854 | 2025-08-16 12:53:00 | TERRA_M-T | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 9.3 |
| c1b9e0f3-8b67-3559-a613-8c4387580596 | -7.07837 | -59.22975 | 2025-08-16 12:53:00 | TERRA_M-T | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 26.7 |
| 807f3fda-d713-3bf2-aed0-53c8f62f287b | -9.92619 | -52.43514 | 2025-08-16 12:53:00 | TERRA_M-T | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 15.2 |
| 3f754dd2-9d4f-350b-b3a8-52702c6f3ba7 | -11.05141 | -55.37165 | 2025-08-16 12:53:00 | TERRA_M-T | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 6.9 |
| aa80ab3b-47b5-389e-908a-d8c9144ba096 | -12.13137 | -47.90409 | 2025-08-16 12:53:00 | TERRA_M-T | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 34.9 |
| 372d4dba-4008-3ea6-9b8f-2828bcc011e7 | -12.81445 | -45.96479 | 2025-08-16 12:53:00 | TERRA_M-T | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 49.8 |
| 89800c17-52c4-31e3-8050-70dea9abb5ac | -9.21559 | -59.65467 | 2025-08-16 12:53:00 | TERRA_M-T | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 7.4 |
| 8999276b-37d9-3660-9b89-8f78c074a623 | -11.65996 | -46.66543 | 2025-08-16 12:53:00 | TERRA_M-T | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 63.5 |
| 44071009-b0f9-32e4-9711-73f9453a731e | -9.17114 | -59.62769 | 2025-08-16 12:53:00 | TERRA_M-T | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 14.4 |
| 74ca42e7-e5d2-35a8-b12e-d462be112dfe | -11.46865 | -47.06125 | 2025-08-16 12:53:00 | TERRA_M-T | PORTO ALEGRE DO TOCANTINS | TOCANTINS | Brasil | 1718006 | 17 | 33 | nan | nan | nan | Cerrado | 24.7 |
| 3a034c93-9d69-3865-b1c8-3a066d9920a3 | -11.36039 | -55.3978 | 2025-08-16 12:53:00 | TERRA_M-T | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 14.9 |
| d8c87b74-43f7-37c2-bcf9-89053376935b | -12.20545 | -53.63105 | 2025-08-16 12:53:00 | TERRA_M-T | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 9.8 |
| 585a9a85-c5d6-3e0f-b91c-829c7ff1dd83 | -9.70366 | -46.26907 | 2025-08-16 12:53:00 | TERRA_M-T | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 67.9 |
| 42e53c6c-b83e-324c-9566-0d510691d895 | -7.98302 | -49.94369 | 2025-08-16 12:53:00 | TERRA_M-T | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 13.0 |
| a3c77f72-8843-32b7-a9dc-9be0120b6ae3 | -9.82101 | -45.69946 | 2025-08-16 12:53:00 | TERRA_M-T | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 56.5 |
| 6a11080f-b806-3a5a-b98e-bc9732a13c4e | -12.54144 | -46.94957 | 2025-08-16 12:53:00 | TERRA_M-T | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 50.2 |
| 2dc0c618-a7b3-3162-b2a9-396d2c7fa1b6 | -12.55731 | -46.95231 | 2025-08-16 12:53:00 | TERRA_M-T | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 104.6 |
| a66ab7c9-c0fa-3839-b238-4d8c6a0b5ecb | -11.66384 | -51.61268 | 2025-08-16 12:53:00 | TERRA_M-T | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 11.2 |
| 9460f49a-e69d-363e-a8f4-d9c224064507 | -7.45316 | -59.93156 | 2025-08-16 12:53:00 | TERRA_M-T | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 11.3 |
| 38fb9d49-0447-32e1-bd4a-a112f30e6c42 | -7.95385 | -63.23387 | 2025-08-16 12:53:00 | TERRA_M-T | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 94.7 |
| 28ee3ff1-9649-3c9f-98ae-f0650dc246ac | -10.9302 | -56.84544 | 2025-08-16 12:53:00 | TERRA_M-T | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 22.1 |
| 09388031-0a02-3d66-a93c-e63b0bd9f45a | -12.61741 | -46.93259 | 2025-08-16 12:53:00 | TERRA_M-T | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 86.3 |
| 11411eed-30c6-3004-aa9a-15f3aa4b635c | -12.62115 | -46.89825 | 2025-08-16 12:53:00 | TERRA_M-T | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 64.9 |
| 06b93eee-f791-3911-a71b-9f95d6246a91 | -6.94957 | -59.53816 | 2025-08-16 12:53:00 | TERRA_M-T | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 21.3 |
| 073f855a-45a5-3666-9b68-4fcb103f3acc | -6.93863 | -59.53651 | 2025-08-16 12:53:00 | TERRA_M-T | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 30.5 |
| 5eab9762-2885-33bf-a9de-19a2ac34473a | -11.55267 | -47.264 | 2025-08-16 12:53:00 | TERRA_M-T | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 27.1 |
| 64cd447a-08e8-34e4-a055-62c439c46263 | -11.35911 | -55.40683 | 2025-08-16 12:53:00 | TERRA_M-T | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 32.6 |
| a78ccc4b-a3e0-3f71-9db6-aef22b729a76 | -9.16911 | -59.64081 | 2025-08-16 12:53:00 | TERRA_M-T | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 18.4 |
| 58ba4d45-00b7-3d2a-8273-b2923679b1ab | -7.25383 | -57.67099 | 2025-08-16 12:53:00 | TERRA_M-T | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 7.2 |
| 6f31c37b-6047-3266-8922-256cb2898d91 | -12.60143 | -46.93044 | 2025-08-16 12:53:00 | TERRA_M-T | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 89.2 |
| 57fd7a01-f04e-3da2-9c64-dcf2a91adca5 | -7.95811 | -63.20771 | 2025-08-16 12:53:00 | TERRA_M-T | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 106.0 |
| 4e95a558-535f-3afd-ac77-728117c16848 | -12.81232 | -45.9574 | 2025-08-16 12:53:00 | TERRA_M-T | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 52.7 |
| f21265be-159b-3acb-9153-77ed4c5eb79c | -12.48602 | -57.18262 | 2025-08-16 12:53:00 | TERRA_M-T | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 23.7 |
| 89d58be5-5c1b-3a41-9fa6-9974af1312fe | -10.17776 | -48.27778 | 2025-08-16 12:53:00 | TERRA_M-T | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 77.0 |
| 71bf393e-8c01-3b2d-9305-ec1c97451a67 | -12.48466 | -57.19182 | 2025-08-16 12:53:00 | TERRA_M-T | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 18.4 |
| 54f3cc4f-55de-368e-b371-2764ff317f5b | -11.27428 | -52.74166 | 2025-08-16 12:53:00 | TERRA_M-T | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 12.9 |
| 2a07dcff-9136-3df4-b3bf-abf14fec6c8f | -11.66825 | -46.65941 | 2025-08-16 12:53:00 | TERRA_M-T | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 81.7 |
| a4b3f2e3-43f0-33e4-b948-615543becde3 | -7.98087 | -49.95997 | 2025-08-16 12:53:00 | TERRA_M-T | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 13.7 |
| 03abcdf2-0de8-393c-b6e4-b98f889c62ad | -12.55 | -46.95751 | 2025-08-16 12:53:00 | TERRA_M-T | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 121.5 |
| a2366916-28d7-30be-b881-8c6791e5c320 | -14.94829 | -54.76198 | 2025-08-16 12:55:00 | TERRA_M-T | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 7.6 |
| 891910fd-4933-358a-95f4-d863c0b6c4af | -15.19003 | -51.14392 | 2025-08-16 12:55:00 | TERRA_M-T | ARUANÃ | GOIÁS | Brasil | 5202502 | 52 | 33 | nan | nan | nan | Cerrado | 34.8 |
| 730ceb79-815b-3de0-8368-16fa132f1930 | -14.96158 | -54.73349 | 2025-08-16 12:55:00 | TERRA_M-T | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 48.1 |
| bf4aadb9-8793-3cec-9b52-28a761e46bf5 | -14.93911 | -54.6893 | 2025-08-16 12:55:00 | TERRA_M-T | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 44.7 |
| e8c9b6a7-0d9c-35cf-bb7d-a65a1721a1ea | -14.60738 | -47.93759 | 2025-08-16 12:55:00 | TERRA_M-T | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 35.1 |
| 23ff7731-b9ab-30d3-b53b-6525baa98016 | -15.18102 | -53.84866 | 2025-08-16 12:55:00 | TERRA_M-T | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | 73.2 |
| cfaf2a18-060d-31e0-a656-e357122bcd86 | -14.94042 | -54.67945 | 2025-08-16 12:55:00 | TERRA_M-T | PRIMAVERA DO LESTE | MATO GROSSO | Brasil | 5107040 | 51 | 33 | nan | nan | nan | Cerrado | 8.5 |
| 04df4749-bed9-3147-91fb-8158dc2d5631 | -16.12998 | -49.66753 | 2025-08-16 12:55:00 | TERRA_M-T | ITABERAÍ | GOIÁS | Brasil | 5210406 | 52 | 33 | nan | nan | nan | Cerrado | 54.9 |
| 9dc6ae33-e09f-3bec-80af-9f629312f97b | -14.87411 | -60.08407 | 2025-08-16 12:55:00 | TERRA_M-T | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 23.2 |
| 0b3b17c6-20ff-368e-8505-41679a835970 | -16.06294 | -57.63978 | 2025-08-16 12:55:00 | TERRA_M-T | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 5.2 |
| f5e9f2e5-44dd-3d5f-80a7-7ce9df9880e8 | -14.60464 | -47.94362 | 2025-08-16 12:55:00 | TERRA_M-T | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 39.9 |
| 056272e3-2c20-393d-be15-c5cb83c05a7f | -13.12363 | -57.11583 | 2025-08-16 12:55:00 | TERRA_M-T | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 11.2 |
| fbfaa99e-643b-3cc5-a04f-c732ef8da5eb | -16.42274 | -49.34896 | 2025-08-16 12:55:00 | TERRA_M-T | BRAZABRANTES | GOIÁS | Brasil | 5203609 | 52 | 33 | nan | nan | nan | Cerrado | 120.8 |
| f5320f65-e08f-3179-a8cd-7a612efa1e0c | -13.61991 | -55.45535 | 2025-08-16 12:55:00 | TERRA_M-T | SANTA RITA DO TRIVELATO | MATO GROSSO | Brasil | 5107768 | 51 | 33 | nan | nan | nan | Cerrado | 14.2 |
| b1df865b-900b-3e9f-bc2e-f8ed3997e719 | -16.44584 | -49.72538 | 2025-08-16 12:55:00 | TERRA_M-T | ARAÇU | GOIÁS | Brasil | 5201603 | 52 | 33 | nan | nan | nan | Cerrado | 17.7 |
| 0187f80e-a928-3bb3-afea-9e5b644be0c3 | -14.96025 | -54.74339 | 2025-08-16 12:55:00 | TERRA_M-T | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 35.7 |
| b7f4b6d4-9ff8-32db-90b8-939124aa9860 | -14.97357 | -54.71486 | 2025-08-16 12:55:00 | TERRA_M-T | CAMPO VERDE | MATO GROSSO | Brasil | 5102678 | 51 | 33 | nan | nan | nan | Cerrado | 22.8 |
| 452c2d42-692d-334a-882f-4135b30b784d | -16.42536 | -49.32417 | 2025-08-16 12:55:00 | TERRA_M-T | BRAZABRANTES | GOIÁS | Brasil | 5203609 | 52 | 33 | nan | nan | nan | Cerrado | 96.7 |
| e88a5415-3a16-3351-ae00-e466b2071949 | -14.59206 | -47.93647 | 2025-08-16 12:55:00 | TERRA_M-T | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 88.9 |
| 7c7e1e43-882e-3f63-bf3f-afdac192c1ff | -14.43844 | -57.58675 | 2025-08-16 12:55:00 | TERRA_M-T | SANTO AFONSO | MATO GROSSO | Brasil | 5107263 | 51 | 33 | nan | nan | nan | Amazônia | 9.7 |
| 3cce0a8a-e352-3567-8d9e-728d60685b50 | -13.12094 | -57.13411 | 2025-08-16 12:55:00 | TERRA_M-T | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 12.1 |
| 4595510a-27e6-3e90-aa6c-ee1b9ceead89 | -14.97493 | -54.70475 | 2025-08-16 12:55:00 | TERRA_M-T | CAMPO VERDE | MATO GROSSO | Brasil | 5102678 | 51 | 33 | nan | nan | nan | Cerrado | 7.8 |
| 7b75b486-5b1a-3a35-a42c-76fb36ae624f | -15.18791 | -51.16122 | 2025-08-16 12:55:00 | TERRA_M-T | BRITÂNIA | GOIÁS | Brasil | 5203807 | 52 | 33 | nan | nan | nan | Cerrado | 43.0 |
| 846fc27b-a9f1-385f-8d00-e1f71f8a96b9 | -14.97218 | -54.72507 | 2025-08-16 12:55:00 | TERRA_M-T | CAMPO VERDE | MATO GROSSO | Brasil | 5102678 | 51 | 33 | nan | nan | nan | Cerrado | 48.6 |
| 2deca7a5-ee38-357a-857d-f9360a338acb | -16.51142 | -48.94731 | 2025-08-16 12:55:00 | TERRA_M-T | LEOPOLDO DE BULHÕES | GOIÁS | Brasil | 5212303 | 52 | 33 | nan | nan | nan | Cerrado | 22.1 |
| 39193190-a15f-3be3-8cd6-29b1adc09a4b | -14.87228 | -60.09548 | 2025-08-16 12:55:00 | TERRA_M-T | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 11.6 |
| 7f3b48f1-dd80-34ca-8b26-4271ab1ebf1f | -13.12229 | -57.12497 | 2025-08-16 12:55:00 | TERRA_M-T | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 73.8 |
| f457a65c-acc1-3481-85de-08e3c5376ea4 | -16.1436 | -49.66923 | 2025-08-16 12:55:00 | TERRA_M-T | ITAUÇU | GOIÁS | Brasil | 5211404 | 52 | 33 | nan | nan | nan | Cerrado | 114.4 |
| 0add682a-45c7-3d7b-a443-ab129d693f92 | -13.00209 | -56.87148 | 2025-08-16 12:55:00 | TERRA_M-T | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 9.4 |
| 2991d8f9-1ea4-309c-9367-128391b33c24 | -15.18366 | -51.14956 | 2025-08-16 12:55:00 | TERRA_M-T | ARUANÃ | GOIÁS | Brasil | 5202502 | 52 | 33 | nan | nan | nan | Cerrado | 51.8 |
| bc9bbc94-7fa1-3e5b-b561-587678ee36bc | -14.53663 | -48.58632 | 2025-08-16 12:55:00 | TERRA_M-T | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 27.6 |
| 28890a2a-b6f4-34da-a06b-e88366cc407f | -14.93779 | -54.69913 | 2025-08-16 12:55:00 | TERRA_M-T | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 11.4 |
| bf0a19c0-4dee-318b-a4da-f7773058ed67 | -14.53849 | -48.59343 | 2025-08-16 12:55:00 | TERRA_M-T | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 33.3 |
| 70efb58d-f1ad-3fed-aa54-570b1dd641e6 | -15.18168 | -51.1669 | 2025-08-16 12:55:00 | TERRA_M-T | BRITÂNIA | GOIÁS | Brasil | 5203807 | 52 | 33 | nan | nan | nan | Cerrado | 10.3 |
| ca1d1bc1-93f4-327f-becc-15cf2da3b6fd | -15.17953 | -53.85998 | 2025-08-16 12:55:00 | TERRA_M-T | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | 36.1 |
| 18ad5fe8-43b8-3db4-a59a-527cf18809f5 | -14.33688 | -53.04079 | 2025-08-16 12:55:00 | TERRA_M-T | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 24.0 |
| c07fc9ae-080c-3b96-b9bb-28de3c4b5eec | -14.97082 | -54.73515 | 2025-08-16 12:55:00 | TERRA_M-T | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 65.2 |
| a9da465f-a953-3ead-a14d-625894adaba4 | -20.39489 | -54.7827 | 2025-08-16 12:57:00 | TERRA_M-T | TERENOS | MATO GROSSO DO SUL | Brasil | 5008008 | 50 | 33 | nan | nan | nan | Cerrado | 29.8 |
| ef4c821e-2215-35c4-b534-a8659b7d6049 | -22.98179 | -48.79931 | 2025-08-16 12:57:00 | TERRA_M-T | AVARÉ | SÃO PAULO | Brasil | 3504503 | 35 | 33 | nan | nan | nan | Cerrado | 38.8 |
| 9e2b91b6-e760-3c1b-80bf-3f635a54481a | -18.32969 | -51.67349 | 2025-08-16 12:57:00 | TERRA_M-T | SERRANÓPOLIS | GOIÁS | Brasil | 5220504 | 52 | 33 | nan | nan | nan | Cerrado | 23.3 |
| d6dc580a-094d-3b50-8cff-94adaec7ea4c | -19.50536 | -55.34753 | 2025-08-16 12:57:00 | TERRA_M-T | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 16.9 |
| af3d31b1-9944-3e79-a925-00de2e8c7a11 | -22.97268 | -48.79276 | 2025-08-16 12:57:00 | TERRA_M-T | AVARÉ | SÃO PAULO | Brasil | 3504503 | 35 | 33 | nan | nan | nan | Cerrado | 31.1 |


[Clique aqui para ver as próximas entradas](README79.md)
