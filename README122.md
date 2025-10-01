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

## Dados Diários - Página 122

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 77420070-f3d2-3aad-884e-4d3ae65fdc29 | -9.42183 | -54.70955 | 2025-10-01 05:10:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 7aa3d0e9-f3de-3160-b005-d6ae1e5951d4 | -13.30763 | -47.22537 | 2025-10-01 05:10:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 486b5a8c-5794-39df-a3b2-e640f984dc5a | -7.04987 | -46.42321 | 2025-10-01 05:10:00 | NOAA-20 | NOVA COLINAS | MARANHÃO | Brasil | 2107258 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 5b5475a2-3202-30c1-9903-18c582133d37 | -7.01794 | -44.46811 | 2025-10-01 05:10:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 77ab4b93-6e04-3b7d-a9c3-4901b5ed4dc4 | -11.46265 | -45.09072 | 2025-10-01 05:10:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 55ce0626-d34b-3d1a-8242-bc5b0e72a4f2 | -11.85583 | -45.01975 | 2025-10-01 05:10:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 7.3 |
| 2cdd743a-b199-3125-b6e3-657b9d868bfe | -10.73546 | -45.37782 | 2025-10-01 05:10:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 4.2 |
| d07d3787-cb26-3c05-84ee-ab1176985781 | -11.62726 | -47.49736 | 2025-10-01 05:10:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| fef6d0d2-4636-36a3-b56c-6e95d58b9b1c | -8.1573 | -46.26637 | 2025-10-01 05:10:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 07ba8c85-f577-31e4-a93e-b34e84dfb920 | -13.4127 | -48.19997 | 2025-10-01 05:10:00 | NOAA-20 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| d75beeb2-0f18-3258-9cc3-0b5abee8a85b | -10.18545 | -52.55489 | 2025-10-01 05:10:00 | NOAA-20 | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 92884a74-fd66-35d5-b864-554e78f941df | -12.24279 | -47.82294 | 2025-10-01 05:10:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 150024e6-b4d6-3d66-8fe2-e1861e1b2bb5 | -11.39373 | -55.08794 | 2025-10-01 05:10:00 | NOAA-20 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a77b5ba1-b0e2-3f4d-9495-950a88d9b7ba | -9.82531 | -48.27187 | 2025-10-01 05:10:00 | NOAA-20 | LAJEADO | TOCANTINS | Brasil | 1712009 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 968ca477-3b24-3940-a40d-2ac1f905b9d7 | -5.62596 | -51.93849 | 2025-10-01 05:10:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e55235ff-bde2-3a82-b2b2-fd9dd33e729e | -7.62517 | -45.45368 | 2025-10-01 05:10:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| d6bce4ce-7cc9-3018-a181-81829a2ad06e | -13.28951 | -47.23175 | 2025-10-01 05:10:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 2d5ba937-bd06-3a45-9cfd-45cdc58b8ba0 | -9.51704 | -54.74846 | 2025-10-01 05:10:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 9fb3eb66-f291-3a78-942f-7b190568688a | -11.79738 | -47.59536 | 2025-10-01 05:10:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 6d6274c9-68b9-354b-8b43-7af9c395a5e1 | -12.14635 | -50.97247 | 2025-10-01 05:10:00 | NOAA-20 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| ea0af667-d683-3023-a46f-8c52f1709d39 | -11.84394 | -48.05357 | 2025-10-01 05:10:00 | NOAA-20 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 39572963-587f-3c29-a776-811b96240bac | -13.24265 | -47.31299 | 2025-10-01 05:10:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 170315a3-306d-30b4-87a8-ce96d92ac81b | -6.73362 | -49.63771 | 2025-10-01 05:10:00 | NOAA-20 | SAPUCAIA | PARÁ | Brasil | 1507755 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 9808102a-99e3-323a-9b9b-a781b84963ae | -10.06938 | -50.28788 | 2025-10-01 05:10:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 11.6 |
| 297b6540-be7b-3d54-8e45-7f90e154050f | -11.08497 | -47.84012 | 2025-10-01 05:10:00 | NOAA-20 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| e9907737-9068-3ee8-b9d8-f057ae391b1a | -12.43148 | -50.17443 | 2025-10-01 05:10:00 | NOAA-20 | SÃO MIGUEL DO ARAGUAIA | GOIÁS | Brasil | 5220207 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| f1b8ef05-ea4b-3056-8ce0-e91e94f482de | -12.82891 | -47.0258 | 2025-10-01 05:10:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 199607c1-0217-3692-b828-5c7cce5282ec | -11.8427 | -45.01105 | 2025-10-01 05:10:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| b715e41d-c6e3-31c5-835a-cb5820b08aa6 | -12.88413 | -46.914 | 2025-10-01 05:10:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 434b2852-2833-3b3c-8d4a-6fd2b8aed8d9 | -11.16744 | -54.1145 | 2025-10-01 05:10:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 2a032ccc-acce-3e48-962b-039c87db4b40 | -7.47905 | -46.47295 | 2025-10-01 05:10:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 62b651e6-2cd5-3ef7-9f4f-34b414366f6d | -11.14383 | -54.30863 | 2025-10-01 05:10:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 6.9 |
| 3d4321ef-997a-3055-ae17-ba781aea7a8f | -11.78048 | -47.58475 | 2025-10-01 05:10:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| ba4a74c4-db98-36d1-8da3-231ada6feb1b | -7.05419 | -46.4238 | 2025-10-01 05:10:00 | NOAA-20 | NOVA COLINAS | MARANHÃO | Brasil | 2107258 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 4fa0e068-6cec-3e0b-8f8d-e7b791485c11 | -9.51341 | -54.74793 | 2025-10-01 05:10:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 9e5d74f0-6b95-34b9-bd4a-ec557ae3f1c7 | -11.16191 | -47.21584 | 2025-10-01 05:10:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 57b4f448-ad40-3dc6-bcd8-f62f12878abc | -7.86026 | -54.97406 | 2025-10-01 05:10:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 489fa7ce-b6a3-3407-9c64-431774f5f0aa | -7.83623 | -48.19554 | 2025-10-01 05:10:00 | NOAA-20 | PALMEIRANTE | TOCANTINS | Brasil | 1715705 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| a53b0b2c-0d34-3e63-a1e9-69a8346d7492 | -11.39324 | -44.8981 | 2025-10-01 05:10:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 479ec535-d213-3cee-9d57-eeb915528dec | -7.54882 | -46.28318 | 2025-10-01 05:10:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 21f2350e-dd3c-353c-908e-1720d55fe4d8 | -13.3333 | -47.84649 | 2025-10-01 05:10:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| c5dbcf6e-2e3e-3904-9740-185820b899f9 | -8.92371 | -47.59053 | 2025-10-01 05:10:00 | NOAA-20 | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 0b3facfb-9b92-3fa6-a965-04a64969c903 | -11.3925 | -44.90477 | 2025-10-01 05:10:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| fb2589cc-e693-378b-a48a-ff0495b0e579 | -12.84412 | -46.87197 | 2025-10-01 05:10:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 9099aad1-215e-39ca-b476-b6fa9aff3839 | -11.58695 | -45.04335 | 2025-10-01 05:10:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 7.0 |
| 281ff51d-9fee-3ae6-b769-aa103ea3e592 | -13.06889 | -47.09124 | 2025-10-01 05:10:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 8c7d336c-9f66-305c-85bb-7658210cd731 | -7.81773 | -47.06324 | 2025-10-01 05:10:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 15660c09-8eed-3342-8af5-7fe23080df5d | -9.89006 | -45.93992 | 2025-10-01 05:10:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 09cb3f1c-093b-3408-9f4e-a1fd65296c9e | -7.84637 | -47.0649 | 2025-10-01 05:10:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| d7267e9c-71e0-36d6-98ce-93639a5073a5 | -11.83371 | -44.96503 | 2025-10-01 05:10:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 6.8 |
| f660b4b8-d3fb-3246-a5fb-10be22e01c68 | -10.57345 | -57.81416 | 2025-10-01 05:10:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 8fd47598-de1f-3f9f-aac3-5106d6c59f4a | -11.82465 | -44.98289 | 2025-10-01 05:10:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 62c5612e-4e3f-35ce-97dd-de2f8a10da00 | -11.1706 | -54.11982 | 2025-10-01 05:10:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 247acc17-f06d-33bb-b0a8-25d46bd2941c | -11.43582 | -55.05482 | 2025-10-01 05:10:00 | NOAA-20 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 2ee21652-f7c7-3fce-89b3-8737b653805e | -12.43486 | -50.17931 | 2025-10-01 05:10:00 | NOAA-20 | SÃO MIGUEL DO ARAGUAIA | GOIÁS | Brasil | 5220207 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 511613d3-2064-325a-b608-149a0842d2f3 | -7.81704 | -47.06155 | 2025-10-01 05:10:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| daea6668-b9fc-3719-b1e8-6e06959adc90 | -6.72878 | -49.63696 | 2025-10-01 05:10:00 | NOAA-20 | SAPUCAIA | PARÁ | Brasil | 1507755 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 8ddccaa9-30ad-3442-ae6e-ee2d9f4723c5 | -13.03416 | -48.67439 | 2025-10-01 05:10:00 | NOAA-20 | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 15f2463f-1c3e-3385-8b3f-acb2e62ebc48 | -11.6332 | -47.49846 | 2025-10-01 05:10:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 922f739c-994b-3138-86aa-6423b7c1288c | -12.86114 | -46.94813 | 2025-10-01 05:10:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 4dcbd4f5-ed05-3dc7-85bc-7801647f1dc7 | -12.38133 | -50.20425 | 2025-10-01 05:10:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 442d5006-fe01-3ce5-a258-c25af75a6aea | -11.18169 | -47.20494 | 2025-10-01 05:10:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 116ccea5-e6e8-3cfa-bcb6-7a3fa345d27c | -10.6612 | -48.534 | 2025-10-01 05:10:00 | NOAA-20 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 8e2578a1-1071-3ae3-999c-e2fa7b44de26 | -13.33379 | -47.84208 | 2025-10-01 05:10:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 00fd45a0-d1c6-3183-827c-962a9f375f88 | -11.1518 | -54.12465 | 2025-10-01 05:10:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 7b6af49e-596f-3575-a364-9524cdf41dd9 | -12.78469 | -46.85839 | 2025-10-01 05:10:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 7733ffbc-f6f8-351b-b761-d0914536ad24 | -13.33055 | -48.1473 | 2025-10-01 05:10:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 73d47d53-c3bf-3210-bfa1-53448bfe00fb | -12.42942 | -50.18164 | 2025-10-01 05:10:00 | NOAA-20 | SÃO MIGUEL DO ARAGUAIA | GOIÁS | Brasil | 5220207 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| a0b1eac8-c032-31c2-ae2f-dc7a50c1671a | -8.14985 | -46.27493 | 2025-10-01 05:10:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 96df70f0-538e-388f-8201-c8f14943a51e | -8.96062 | -50.32886 | 2025-10-01 05:10:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 2e0b2085-50fe-3ae5-9f98-adc101cef01c | -12.97366 | -48.42621 | 2025-10-01 05:10:00 | NOAA-20 | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 935ea67e-d5a9-3bfa-9f29-8e1eadb5ab25 | -12.75638 | -46.88257 | 2025-10-01 05:10:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 7be1dee2-8c1a-3f91-ab3f-1511b1e31c06 | -13.33066 | -47.84271 | 2025-10-01 05:10:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 1efa3348-8523-3ee2-9d1d-ddc94ebf826c | -12.95185 | -46.43037 | 2025-10-01 05:10:00 | NOAA-20 | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 4096d459-8e3f-3513-b516-da14656c8667 | -9.43142 | -54.71963 | 2025-10-01 05:10:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 0a3ac8c5-32eb-36ce-8421-7fd9bea9e839 | -11.16793 | -47.21687 | 2025-10-01 05:10:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 735a3a2d-4fc1-32b4-a79f-dd8c37d85807 | -12.75586 | -46.88722 | 2025-10-01 05:10:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 2db7f541-e61b-3498-96db-9e5fd219bde6 | -7.01968 | -44.4701 | 2025-10-01 05:10:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 6be01b9f-dfb0-3d58-8663-861b71140dcd | -11.05057 | -47.83193 | 2025-10-01 05:10:00 | NOAA-20 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 6dc9e3d5-0ac9-3fd8-8100-825c1191d940 | -11.84347 | -48.05754 | 2025-10-01 05:10:00 | NOAA-20 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 122809fd-851b-37a2-b45f-f648efc5131d | -10.06827 | -50.28434 | 2025-10-01 05:10:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 7.0 |
| 623b500d-44f8-3050-b47d-d41bf4f274dc | -11.83697 | -48.05747 | 2025-10-01 05:10:00 | NOAA-20 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 6c66b57e-ba3b-3c99-8c1f-24c475c3e744 | -12.8273 | -47.02323 | 2025-10-01 05:10:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 4e4252b1-6249-38c8-8662-650990f3986c | -11.62146 | -52.24617 | 2025-10-01 05:10:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| d737cfc9-f954-36ae-8118-83f2b9a74ba8 | -8.56311 | -44.70995 | 2025-10-01 05:10:00 | NOAA-20 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| b8fecc7b-ce94-37bb-9e8b-6cef238c77ad | -11.91569 | -47.89757 | 2025-10-01 05:10:00 | NOAA-20 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 8e1e415c-76fc-3011-901a-44cbe17fb299 | -11.43409 | -55.04137 | 2025-10-01 05:10:00 | NOAA-20 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c2028eb7-9da4-302a-9149-fa37889be079 | -7.41221 | -45.41343 | 2025-10-01 05:10:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 17398a0b-6ade-309e-a0a9-833bfa1825d0 | -10.64502 | -48.52881 | 2025-10-01 05:10:00 | NOAA-20 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| aba3c7b1-0bd2-3c5a-b035-d91eaff18a5a | -11.76896 | -46.87256 | 2025-10-01 05:10:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 82c1798e-137f-3411-800f-9f929eadc20b | -11.83598 | -48.06545 | 2025-10-01 05:10:00 | NOAA-20 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 168c1063-f0a0-3f8b-acc8-2dfeb5b1df2b | -11.83548 | -48.06947 | 2025-10-01 05:10:00 | NOAA-20 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 2a26026c-64d4-379a-844b-09540f237c1b | -12.70613 | -46.90224 | 2025-10-01 05:10:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| e5c89dc1-a45b-3945-a7a8-4de38ec9a065 | -13.28338 | -47.23035 | 2025-10-01 05:10:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 20c1c8b4-04dd-359b-8951-5fbf3faf40a2 | -7.87709 | -47.27773 | 2025-10-01 05:10:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| c5153891-0eac-3d51-822b-d9931dc331ce | -8.535 | -44.71302 | 2025-10-01 05:10:00 | NOAA-20 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 27278922-72ee-347b-9555-c033aec671ef | -11.80302 | -46.62918 | 2025-10-01 05:10:00 | NOAA-20 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 24.3 |
| eb3d5fee-b2c7-395b-b689-c52d3d5e0d0c | -13.36408 | -48.15881 | 2025-10-01 05:10:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 1182a198-ae0b-3d01-abf8-200d362595ae | -9.4461 | -50.89683 | 2025-10-01 05:10:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 973070b7-44e7-3e5b-9385-5d2144d9fa83 | -12.86747 | -46.94841 | 2025-10-01 05:10:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |


[Clique aqui para ver as próximas entradas](README123.md)
