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

## Dados Diários - Página 50

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 326c39c1-2df9-3ed6-b0ee-0bc1fd026c00 | -9.72319 | -46.26122 | 2024-10-30 04:21:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 42c2a9cc-29cf-32d3-a896-1f29b578fde9 | -9.72099 | -46.25364 | 2024-10-30 04:21:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 597c56bb-0604-3345-a0dd-7f7e420c7e00 | -9.72043 | -46.25716 | 2024-10-30 04:21:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 33cd5d9c-2393-3e81-9f2b-38e5e3c179de | -11.69265 | -47.11593 | 2024-10-30 04:21:00 | NOAA-21 | PORTO ALEGRE DO TOCANTINS | TOCANTINS | Brasil | 1718006 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 96a8276e-7353-3975-88d7-dbe7caeb9404 | -12.32259 | -46.75717 | 2024-10-30 04:21:00 | NOAA-21 | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 62eb6787-a230-388b-8ada-9a738449e1f6 | -12.31287 | -46.49778 | 2024-10-30 04:21:00 | NOAA-21 | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| a1f53740-5ed8-393b-93de-d1e2b3e3b871 | -12.17053 | -47.65271 | 2024-10-30 04:21:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| af7a6676-c4fd-3cf8-aab6-db7bd3c4945c | -12.14659 | -46.45253 | 2024-10-30 04:21:00 | NOAA-21 | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 47ba89b5-4374-3a4f-a1b5-91b622765fd2 | -12.09532 | -47.24228 | 2024-10-30 04:21:00 | NOAA-21 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 5ea1b1c7-f888-3033-aa18-44237ace8b61 | -12.09474 | -47.2459 | 2024-10-30 04:21:00 | NOAA-21 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 229363de-3dce-361d-8010-5560c2b249f3 | -12.09197 | -47.24173 | 2024-10-30 04:21:00 | NOAA-21 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 04185d00-b23d-3c7e-8f83-6a915eb25e00 | -12.09138 | -47.24535 | 2024-10-30 04:21:00 | NOAA-21 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 04e4a6db-bc0d-307e-9357-68e3bfafee11 | -12.00564 | -46.50488 | 2024-10-30 04:21:00 | NOAA-21 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| fe3fc610-67d5-37ee-a15a-06b817954499 | -12.00477 | -47.65285 | 2024-10-30 04:21:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 9e3194f2-c411-3a6c-ad47-4b750219672d | -12.00417 | -47.65655 | 2024-10-30 04:21:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 00b5d8ae-f14e-32de-bc59-6ebc31841181 | -12.00078 | -47.65599 | 2024-10-30 04:21:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 8f9cd7ad-330f-31d0-af36-39f6ca8b81ed | -11.99533 | -47.16575 | 2024-10-30 04:21:00 | NOAA-21 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 26bafc74-bf7d-3325-b8a5-662d8c993707 | -11.93172 | -46.58347 | 2024-10-30 04:21:00 | NOAA-21 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 483b3859-fda4-39ae-8a80-9deb2d6ab2ea | -11.88542 | -46.53231 | 2024-10-30 04:21:00 | NOAA-21 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 5b242af7-5945-3932-bab5-af8ade5095ee | -11.88486 | -46.53584 | 2024-10-30 04:21:00 | NOAA-21 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 4a9be605-21e0-3917-8c37-4f719f050f97 | -11.88155 | -46.5353 | 2024-10-30 04:21:00 | NOAA-21 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| d60b9aa1-65d6-3acb-9668-2905ba91a7e2 | -11.78566 | -47.072 | 2024-10-30 04:21:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 17e331da-8ecf-3b50-87ed-255bbe3dfd11 | -11.78508 | -47.07561 | 2024-10-30 04:21:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 088f4bc2-966d-3d3f-b43a-4f218c052faa | -11.78231 | -47.07145 | 2024-10-30 04:21:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| c4ebe3aa-b6a2-3503-a322-d6ea1de2ab7a | -11.78173 | -47.07505 | 2024-10-30 04:21:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 8aed3870-5963-3c10-ab0f-25e1c876dceb | -11.77897 | -47.0709 | 2024-10-30 04:21:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 6fecac2d-2107-311c-b632-098a05465121 | -11.77839 | -47.0745 | 2024-10-30 04:21:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| ee1cf27b-76fa-39d3-b682-6680133b78bf | -11.77723 | -47.0817 | 2024-10-30 04:21:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| dcced7ca-cb86-3354-924d-ce54e9c150c1 | -11.77447 | -47.07754 | 2024-10-30 04:21:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| a6efe189-5f11-3abe-a82e-fdf01a043bb4 | -11.77331 | -47.08474 | 2024-10-30 04:21:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| b032a246-2490-354b-b94d-a82eadc25d84 | -11.77112 | -47.07698 | 2024-10-30 04:21:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 239575f8-80cd-3949-8779-e6c2ef5bc3fb | -12.43151 | -46.63006 | 2024-10-30 04:21:00 | NOAA-21 | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 34d243b3-f804-3c50-a872-e26350e66b81 | -12.43095 | -46.63359 | 2024-10-30 04:21:00 | NOAA-21 | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 40be48c2-a703-356f-8ba3-5987d9487b34 | -12.26274 | -47.69168 | 2024-10-30 04:21:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 4c14cd11-ecb2-3486-99eb-c0a3027ea9c5 | -12.25935 | -47.69112 | 2024-10-30 04:21:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 7d1fad61-ad9c-301a-92b4-63bd6957eeab | -14.09999 | -47.00945 | 2024-10-30 04:21:00 | NOAA-21 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 1c8899e9-5739-3508-9abb-22762f9bf122 | -7.54162 | -48.30492 | 2024-10-30 04:21:00 | NOAA-21 | NOVA OLINDA | TOCANTINS | Brasil | 1714880 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 825bb705-657f-3874-bce8-21929d640369 | -7.41393 | -47.8649 | 2024-10-30 04:21:00 | NOAA-21 | FILADÉLFIA | TOCANTINS | Brasil | 1707702 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 47ea96f7-965e-3b71-831d-9c363f255553 | -7.66852 | -47.32628 | 2024-10-30 04:21:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 9.1 |
| 6292d7eb-4f7e-3b28-98af-f10120ad835c | -7.66851 | -47.28262 | 2024-10-30 04:21:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| ab5b438c-714d-30c6-ac03-25167046b3d5 | -7.6644 | -47.28593 | 2024-10-30 04:21:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 98eddb02-bb19-3b07-b95c-8741a7d7721d | -7.64295 | -47.24309 | 2024-10-30 04:21:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 9dc48e68-3bcf-3c92-b6a5-b984697b95b8 | -7.59022 | -47.11668 | 2024-10-30 04:21:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| d92472ba-20c3-37cb-95f1-364bce6aa9ad | -7.58677 | -47.11613 | 2024-10-30 04:21:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 9c384ebb-55a6-338e-b3e9-cb2e2c645df6 | -7.58368 | -47.13513 | 2024-10-30 04:21:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 535d7d3a-fa49-3f31-8d81-e39362842341 | -7.58332 | -47.11557 | 2024-10-30 04:21:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 8782af19-be8b-3e9d-ae4c-49d0008c9d43 | -7.48564 | -47.15507 | 2024-10-30 04:21:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 295428c5-5111-31a8-b3bf-2639f6f8a312 | -7.48502 | -47.15889 | 2024-10-30 04:21:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 5db571ef-d035-31c2-afc9-6ce3d2b06413 | -7.46682 | -47.18346 | 2024-10-30 04:21:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 95d2bd54-3745-3201-8f2c-27bba1d33341 | -7.46619 | -47.18731 | 2024-10-30 04:21:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 56b9a527-596e-3d85-b542-679c91713e30 | -7.45337 | -47.37572 | 2024-10-30 04:21:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 9f9b20ce-3c59-3983-9350-2f98f392c23b | -9.28062 | -48.71225 | 2024-10-30 04:21:00 | NOAA-21 | MIRANORTE | TOCANTINS | Brasil | 1713304 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 9bd61672-7dc2-32ab-82a1-5431d57e6381 | -9.05 | -48.72106 | 2024-10-30 04:21:00 | NOAA-21 | COLMÉIA | TOCANTINS | Brasil | 1716703 | 17 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 830877f5-fb32-3936-8cac-1b75962cb437 | -9.04059 | -47.81593 | 2024-10-30 04:21:00 | NOAA-21 | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| d6f84bb1-c8c6-36a7-a938-14bdb4e0096e | -9.03709 | -47.81533 | 2024-10-30 04:21:00 | NOAA-21 | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 34e7c5c7-6164-33af-92c3-054c9fcb0ed8 | -8.99654 | -48.17543 | 2024-10-30 04:21:00 | NOAA-21 | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 065125b2-da71-3a78-b70b-3916bed731f1 | -8.9629 | -47.62355 | 2024-10-30 04:21:00 | NOAA-21 | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| c15ba7c3-3993-370d-85e9-ba88b5d71580 | -8.95942 | -47.62299 | 2024-10-30 04:21:00 | NOAA-21 | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| ce30b42e-aeff-33b7-872d-d4bd1428ff8a | -8.95879 | -47.62687 | 2024-10-30 04:21:00 | NOAA-21 | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 396656ef-9b21-3f89-80eb-e46137a23916 | -8.95405 | -47.63408 | 2024-10-30 04:21:00 | NOAA-21 | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 13208955-8b8c-3730-863c-ff66e96ab9b6 | -8.95342 | -47.63796 | 2024-10-30 04:21:00 | NOAA-21 | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 770cb00e-160a-3314-b80b-7d2448ebe03e | -8.87338 | -47.97315 | 2024-10-30 04:21:00 | NOAA-21 | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 1520a00d-5f71-3a7f-8839-ce873072f12e | -8.87052 | -47.96854 | 2024-10-30 04:21:00 | NOAA-21 | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 6ae63e84-651b-3702-af20-15f05a7233f2 | -8.68034 | -47.95481 | 2024-10-30 04:21:00 | NOAA-21 | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| c46c9cb9-f0b0-3b54-8565-a558b0a61a55 | -8.67968 | -47.95885 | 2024-10-30 04:21:00 | NOAA-21 | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 3e809364-c80d-3c19-b9e7-0684c93d29af | -8.55013 | -47.99627 | 2024-10-30 04:21:00 | NOAA-21 | ITAPIRATINS | TOCANTINS | Brasil | 1710904 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 1002e7ca-15a6-3adc-abf0-5911075c6c66 | -8.23331 | -47.67145 | 2024-10-30 04:21:00 | NOAA-21 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| a05d709a-88c8-3385-9ae9-d077dd2a86a8 | -8.23265 | -47.67542 | 2024-10-30 04:21:00 | NOAA-21 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 84e0b652-4713-3b02-9cf9-f27c8cc69a96 | -8.15478 | -47.16782 | 2024-10-30 04:21:00 | NOAA-21 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| e5da4d40-6dc0-389b-8cb4-59fe7f568285 | -8.06306 | -47.08359 | 2024-10-30 04:21:00 | NOAA-21 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 6d37a63b-beae-3164-9e05-5b4b4f047248 | -8.05559 | -47.08625 | 2024-10-30 04:21:00 | NOAA-21 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 870c6a61-b368-373f-8bf4-88f5dbd2c16b | -9.90212 | -48.20962 | 2024-10-30 04:21:00 | NOAA-21 | LAJEADO | TOCANTINS | Brasil | 1712009 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 7992bfca-0c92-31aa-87e7-f210e01af83f | -9.8947 | -48.65279 | 2024-10-30 04:21:00 | NOAA-21 | BARROLÂNDIA | TOCANTINS | Brasil | 1703107 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 13f16f17-dcc7-3fdb-bd27-41b0b7751f3a | -9.78211 | -48.23241 | 2024-10-30 04:21:00 | NOAA-21 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 8baee677-64df-3d7c-8359-efe6a9cabb10 | -9.47004 | -47.83201 | 2024-10-30 04:21:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 784273f9-1fcb-3071-9329-6c49a857f218 | -10.61773 | -47.70919 | 2024-10-30 04:21:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 4dbaeb24-3cf4-303b-814c-bf7f96b51a8c | -10.61711 | -47.71297 | 2024-10-30 04:21:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 6fae39ad-dc62-33c5-a688-ec65a462b376 | -10.60472 | -48.9697 | 2024-10-30 04:21:00 | NOAA-21 | NOVA ROSALÂNDIA | TOCANTINS | Brasil | 1715002 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 878b380d-c1d1-35f2-9324-5248446e0298 | -10.51019 | -49.01999 | 2024-10-30 04:21:00 | NOAA-21 | NOVA ROSALÂNDIA | TOCANTINS | Brasil | 1715002 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| b0d7c310-8e95-32a4-94aa-9a86d408aacb | -10.50803 | -49.0107 | 2024-10-30 04:21:00 | NOAA-21 | NOVA ROSALÂNDIA | TOCANTINS | Brasil | 1715002 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 34d084fe-35b4-3e6a-8578-4f95d9da8603 | -10.50365 | -49.01439 | 2024-10-30 04:21:00 | NOAA-21 | NOVA ROSALÂNDIA | TOCANTINS | Brasil | 1715002 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| a5b261b7-29ef-376a-ae17-811c9308d674 | -10.50309 | -49.01587 | 2024-10-30 04:21:00 | NOAA-21 | NOVA ROSALÂNDIA | TOCANTINS | Brasil | 1715002 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 2ef6773f-7db9-3700-bb3f-f9a9f4c68ae8 | -10.44188 | -49.04541 | 2024-10-30 04:21:00 | NOAA-21 | NOVA ROSALÂNDIA | TOCANTINS | Brasil | 1715002 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| d747e2b4-d339-3c25-975a-1152050cd3d8 | -10.29413 | -48.89429 | 2024-10-30 04:21:00 | NOAA-21 | PARAÍSO DO TOCANTINS | TOCANTINS | Brasil | 1716109 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 4cea059c-56e4-39df-8b11-c16df9edd035 | -10.2905 | -48.89363 | 2024-10-30 04:21:00 | NOAA-21 | PARAÍSO DO TOCANTINS | TOCANTINS | Brasil | 1716109 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 6d8f8354-6571-3dbb-8fc2-e88f3ad059eb | -10.26041 | -48.78352 | 2024-10-30 04:21:00 | NOAA-21 | PARAÍSO DO TOCANTINS | TOCANTINS | Brasil | 1716109 | 17 | 33 | nan | nan | nan | Cerrado | 0.3 |
| 22168b52-a7f6-3cda-8724-d48538853894 | -10.02706 | -48.69876 | 2024-10-30 04:21:00 | NOAA-21 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 1938f4ea-e32c-31e7-b3ab-00b603241935 | -10.62116 | -47.70978 | 2024-10-30 04:21:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 698f653e-14f2-3b0b-b700-58b331c2c131 | -12.0773 | -47.9846 | 2024-10-30 04:21:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 9937a34c-3422-3e3a-882d-ac570d8f5795 | -12.07387 | -47.98403 | 2024-10-30 04:21:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| b2da0cd7-c55c-3c98-a8e1-6013da6f5480 | -11.81893 | -48.76197 | 2024-10-30 04:21:00 | NOAA-21 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| cd821a96-b1fd-3f94-bd37-8a4e327660fa | -11.81825 | -48.76606 | 2024-10-30 04:21:00 | NOAA-21 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 13cfb26d-3b6a-3a2b-ab51-74e5dd5d1383 | -11.65658 | -48.79766 | 2024-10-30 04:21:00 | NOAA-21 | GURUPI | TOCANTINS | Brasil | 1709500 | 17 | 33 | nan | nan | nan | Cerrado | 8.1 |
| 9511f796-f469-3d29-9433-86fb097fbe09 | -11.65589 | -48.80173 | 2024-10-30 04:21:00 | NOAA-21 | GURUPI | TOCANTINS | Brasil | 1709500 | 17 | 33 | nan | nan | nan | Cerrado | 8.1 |
| 92988b57-ac92-35c4-b475-275bded8d47a | -11.65302 | -48.79706 | 2024-10-30 04:21:00 | NOAA-21 | GURUPI | TOCANTINS | Brasil | 1709500 | 17 | 33 | nan | nan | nan | Cerrado | 8.1 |
| c5c66e44-13dd-39f4-8dde-a8495892acf6 | -11.65233 | -48.80114 | 2024-10-30 04:21:00 | NOAA-21 | GURUPI | TOCANTINS | Brasil | 1709500 | 17 | 33 | nan | nan | nan | Cerrado | 8.1 |
| d4387b37-a114-3274-b306-cc400afd2515 | -11.64946 | -48.79647 | 2024-10-30 04:21:00 | NOAA-21 | GURUPI | TOCANTINS | Brasil | 1709500 | 17 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 6c526575-65a6-3f10-be0e-abe86bcf52a1 | -11.64877 | -48.80057 | 2024-10-30 04:21:00 | NOAA-21 | GURUPI | TOCANTINS | Brasil | 1709500 | 17 | 33 | nan | nan | nan | Cerrado | 5.3 |
| d5658e47-8cc5-3dd9-be5b-e3207d39ebaa | -7.63174 | -48.53552 | 2024-10-30 04:21:00 | NOAA-21 | PAU D'ARCO | TOCANTINS | Brasil | 1716307 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 6cc94032-85e0-3d1f-9d71-5a2a2f15b29c | -7.33893 | -48.48545 | 2024-10-30 04:21:00 | NOAA-21 | ARAGUAÍNA | TOCANTINS | Brasil | 1702109 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |


[Clique aqui para ver as próximas entradas](README51.md)
