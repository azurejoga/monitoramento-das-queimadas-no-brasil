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

## Dados Diários - Página 6

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| a20c6c58-7cde-3d57-ae4d-2adfce342658 | -5.1621 | -55.9931 | 2026-09-30 01:30:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 73.0 |
| 49fe142e-20c5-3b39-bac1-2e5a5a2dd571 | -7.8297 | -45.8156 | 2026-09-30 01:30:00 | GOES-19 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 230.6 |
| 64b56aa7-0e22-3615-be91-dba0b7b2c61c | -11.8491 | -50.4311 | 2026-09-30 01:30:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 158.9 |
| 0fe9c440-059e-3b72-ad26-77cdcec0f727 | -2.974 | -51.0247 | 2026-09-30 01:30:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 68.5 |
| 58c8f922-13c8-3782-acd9-064ddeb2ccd5 | -5.7561 | -45.1747 | 2026-09-30 01:30:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 75.5 |
| 0453636b-927b-3bd2-8108-e42a5c55a019 | -19.8864 | -49.5795 | 2026-09-30 01:30:00 | GOES-19 | ITAPAGIPE | MINAS GERAIS | Brasil | 3133402 | 31 | 33 | nan | nan | nan | Mata Atlântica | 234.5 |
| ddb39bd1-bd66-38ef-95a1-b545fcb013f9 | -19.9061 | -49.598 | 2026-09-30 01:30:00 | GOES-19 | ITAPAGIPE | MINAS GERAIS | Brasil | 3133402 | 31 | 33 | nan | nan | nan | Mata Atlântica | 72.9 |
| 0f6438f0-cb29-3b43-a401-196dda2b1939 | -11.64 | -43.5218 | 2026-09-30 01:30:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 149.3 |
| a0e6e48a-a0f7-3485-906a-e9227347651c | -11.3918 | -43.4654 | 2026-09-30 01:30:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 75.9 |
| 9c263887-b42c-3a77-bf35-2d50f7448463 | -11.8297 | -50.4548 | 2026-09-30 01:30:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 123.5 |
| a96f3b24-b163-3060-80cf-04dc73a983b4 | -11.6986 | -43.4654 | 2026-09-30 01:30:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 72.0 |
| bc8741ae-c592-3597-943e-3f64b94453ba | -11.7178 | -43.4623 | 2026-09-30 01:30:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 70.1 |
| 8dd327b1-552a-32f8-9bf2-870e1ad7fe0f | -11.6395 | -43.5455 | 2026-09-30 01:30:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 118.9 |
| d2342029-fb1e-3961-9b8e-5d2f89afff81 | -11.8297 | -50.4548 | 2026-09-30 01:40:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 117.7 |
| d79d89bf-ed9c-33c8-abe2-8a15b43379f5 | -12.2515 | -50.2758 | 2026-09-30 01:40:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 46.3 |
| 83b22e85-eae0-39b9-a811-f92ed9cfc193 | -7.8486 | -45.8138 | 2026-09-30 01:40:00 | GOES-19 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 152.2 |
| 73a87da6-2175-3daf-a9e6-7ccfb629d11f | -3.2313 | -46.9596 | 2026-09-30 01:40:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 51.4 |
| 5b3e9782-72fe-310d-8109-00fbb67d98fc | -19.8858 | -49.6022 | 2026-09-30 01:40:00 | GOES-19 | ITAPAGIPE | MINAS GERAIS | Brasil | 3133402 | 31 | 33 | nan | nan | nan | Mata Atlântica | 88.0 |
| e24acb8b-c9a9-3aaa-86a0-e2d853b0a6bf | -12.3085 | -47.9539 | 2026-09-30 01:40:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 144.8 |
| f692660a-d834-340e-bd99-ee6cc10ba3c5 | -15.625 | -43.2442 | 2026-09-30 01:40:00 | GOES-19 | PORTEIRINHA | MINAS GERAIS | Brasil | 3152204 | 31 | 33 | nan | nan | nan | Caatinga | 71.5 |
| 09ac49de-0a87-3176-8955-c2451ce4c682 | -5.1621 | -55.9931 | 2026-09-30 01:40:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 58.0 |
| c19ae81b-255c-3c22-9544-b58e6553a663 | -19.8864 | -49.5795 | 2026-09-30 01:40:00 | GOES-19 | ITAPAGIPE | MINAS GERAIS | Brasil | 3133402 | 31 | 33 | nan | nan | nan | Mata Atlântica | 226.0 |
| 2b1d9bc0-3410-3d7d-972d-be2c45531991 | -12.2327 | -50.2566 | 2026-09-30 01:40:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 53.2 |
| d5924294-4722-3315-9a37-2363f2d6608b | -2.9082 | -54.0907 | 2026-09-30 01:40:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 109.7 |
| 9cf1322d-46eb-3e58-8028-156d40cc9bfd | -3.2315 | -46.9156 | 2026-09-30 01:40:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 43.7 |
| c1122730-8705-325b-87d1-9d08829a8402 | -2.9925 | -51.0242 | 2026-09-30 01:40:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 61.3 |
| 84471ae1-906c-3da5-aa20-73018cf19c8e | -21.3977 | -45.3069 | 2026-09-30 01:40:00 | GOES-19 | CARMO DA CACHOEIRA | MINAS GERAIS | Brasil | 3113909 | 31 | 33 | nan | nan | nan | Mata Atlântica | 72.7 |
| db24f996-1fcd-3480-8bcb-248f00ba0da0 | -11.6395 | -43.5455 | 2026-09-30 01:40:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 146.0 |
| b474e841-6d58-3472-9be5-365be5d069ba | -11.8488 | -50.4526 | 2026-09-30 01:40:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 64.6 |
| 5e29e45b-42d5-3594-8749-ab7ec546af64 | -11.699 | -43.4416 | 2026-09-30 01:40:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 97.2 |
| b5324939-9665-3882-861c-af6b876fc843 | -19.8869 | -49.5567 | 2026-09-30 01:40:00 | GOES-19 | ITAPAGIPE | MINAS GERAIS | Brasil | 3133402 | 31 | 33 | nan | nan | nan | Mata Atlântica | 68.7 |
| b4aaa479-c184-3ccf-b63a-8493d9c208b6 | -10.0779 | -63.0804 | 2026-09-30 01:40:00 | GOES-19 | ARIQUEMES | RONDÔNIA | Brasil | 1100023 | 11 | 33 | nan | nan | nan | Amazônia | 59.1 |
| 96cedc2d-c0e7-3646-8f15-d5f1a78da888 | -5.7561 | -45.1747 | 2026-09-30 01:40:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 70.8 |
| 23983688-474b-39b2-a130-e810f35ec8a6 | -7.8295 | -45.8381 | 2026-09-30 01:40:00 | GOES-19 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 112.5 |
| fa0ed9b2-c982-3daa-a371-ee438f2baa26 | -6.895 | -43.7066 | 2026-09-30 01:40:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 78.3 |
| 5b408add-2fad-3f6f-a836-621701c4fef9 | -2.9739 | -51.0455 | 2026-09-30 01:40:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 124.0 |
| d74402e7-46ee-31f6-a29d-a9c36afcda88 | -11.3918 | -43.4654 | 2026-09-30 01:40:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 80.6 |
| 22c0569e-14ae-39c5-8652-11f50f93be0f | -11.8491 | -50.4311 | 2026-09-30 01:40:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 87.9 |
| 221f844f-e1f6-36ab-b7c3-50768c5190ca | -7.8297 | -45.8156 | 2026-09-30 01:40:00 | GOES-19 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 201.5 |
| 4aabb7d2-02b3-39f4-b5c2-1598f0b870a6 | -2.974 | -51.0247 | 2026-09-30 01:40:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 94.8 |
| b2d44076-e9e8-385c-986d-29a76bc30404 | -19.9067 | -49.5752 | 2026-09-30 01:40:00 | GOES-19 | ITAPAGIPE | MINAS GERAIS | Brasil | 3133402 | 31 | 33 | nan | nan | nan | Mata Atlântica | 112.7 |
| 207fa716-eb23-348e-be68-9c61e59ea2be | -11.64 | -43.5218 | 2026-09-30 01:40:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 214.8 |
| 476247b3-56ee-3a69-8433-b874c22612e7 | -2.9924 | -51.045 | 2026-09-30 01:40:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 87.9 |
| 4f40be89-07a9-3c7d-85a3-331f39635d01 | -3.2314 | -46.9376 | 2026-09-30 01:40:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 142.6 |
| a29a8e32-9c6f-3d9f-a6bf-8d0e76fd882d | -11.7182 | -43.4386 | 2026-09-30 01:40:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 83.9 |
| 062ece19-b38d-34dc-856c-77a5ad3b617c | -18.2827 | -53.0496 | 2026-09-30 01:40:00 | GOES-19 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 74.4 |
| 30d172ab-174a-33db-aba6-10f3acfd7cef | -5.1806 | -55.9925 | 2026-09-30 01:40:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 54.4 |
| dad09958-49b9-3b12-8d07-d4cfa8a02812 | -11.9548 | -50.9957 | 2026-09-30 01:40:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 70.2 |
| 77c3cc76-e015-3171-bf99-4794d216aedf | -3.2129 | -46.9383 | 2026-09-30 01:40:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 65.9 |
| 28932f5f-35a5-3917-beb2-cd6bafa22980 | -7.8483 | -45.8363 | 2026-09-30 01:40:00 | GOES-19 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 108.9 |
| 234abf6e-0a19-3c0e-bb2c-e09e477b7cf8 | -12.2518 | -50.2543 | 2026-09-30 01:40:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 84.8 |
| a7dc053d-9007-30d4-a698-a07197766bc9 | -10.1445 | -36.1678 | 2026-09-30 01:40:00 | GOES-19 | CORURIPE | ALAGOAS | Brasil | 2702306 | 27 | 33 | nan | nan | nan | Mata Atlântica | 84.9 |
| be8bd428-fd14-3e70-9972-13dca7d1183e | -3.3801 | -50.95 | 2026-09-30 01:40:00 | GOES-19 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 42.9 |
| 808d1584-f22b-3044-96c5-51c253ac04ed | -7.8109 | -45.8173 | 2026-09-30 01:40:00 | GOES-19 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 100.7 |
| ac0b0e4b-dcb3-314c-970d-7d5904833a6f | -11.9545 | -51.017 | 2026-09-30 01:40:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 55.1 |
| 1b6736f5-2756-3fd5-a776-622b0c657b8f | -11.83 | -50.4333 | 2026-09-30 01:40:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 102.9 |
| 9d3bff98-4609-3933-ba06-422488c51e71 | -2.9925 | -51.0242 | 2026-09-30 01:50:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 54.3 |
| 6d4784d1-00f9-3a97-b0a4-1a78705ec024 | -5.1621 | -55.9931 | 2026-09-30 01:50:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 60.1 |
| da3787eb-9acf-36bb-823b-d19244e9fb06 | -7.8295 | -45.8381 | 2026-09-30 01:50:00 | GOES-19 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 106.8 |
| 558b1c65-0d57-3d11-b6fa-79bb2a1c3502 | -2.9739 | -51.0663 | 2026-09-30 01:50:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 45.1 |
| dae6f650-a6e5-3e74-a48c-63dc1ae15c03 | -6.895 | -43.7066 | 2026-09-30 01:50:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 90.0 |
| 2a787907-676b-3eaa-8212-e42da2dcd256 | -2.9082 | -54.0907 | 2026-09-30 01:50:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 99.2 |
| c0f58641-093c-395c-9ee6-747dd5acf0b0 | -2.974 | -51.0247 | 2026-09-30 01:50:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 97.0 |
| 6d8a7f45-ff37-3526-ad6c-22df5ff48a1f | -5.7561 | -45.1747 | 2026-09-30 01:50:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 73.9 |
| 3fc35d92-6cfb-3e7c-8e3a-5984a61272c5 | -7.8486 | -45.8138 | 2026-09-30 01:50:00 | GOES-19 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 150.4 |
| 69c930f8-716f-35dd-bb5c-1214e5cc1baf | -12.3085 | -47.9539 | 2026-09-30 01:50:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 133.2 |
| 350bf137-cf25-32f8-a241-dce8563ff5ca | -5.0215 | -43.5754 | 2026-09-30 01:50:00 | GOES-19 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 69.5 |
| 29ba3d9d-272d-3080-81d0-ca384e2c0c7f | -11.8491 | -50.4311 | 2026-09-30 01:50:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 87.0 |
| 72fdbf92-6a33-3ccc-b015-c656ceff475a | -7.8483 | -45.8363 | 2026-09-30 01:50:00 | GOES-19 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 109.5 |
| f1cd9113-f8e8-3027-80a5-d80c3f12220e | -2.9739 | -51.0455 | 2026-09-30 01:50:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 143.3 |
| 3cbe6f33-e4ac-3d97-9ae4-29a30f5aeb78 | -7.8297 | -45.8156 | 2026-09-30 01:50:00 | GOES-19 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 218.9 |
| baf6fe37-db4d-3c7c-bdc4-e84a9015813c | -12.2518 | -50.2543 | 2026-09-30 01:50:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 108.5 |
| 5b112d10-52a4-33ce-b3d3-2a6800340239 | -3.2314 | -46.9376 | 2026-09-30 01:50:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 184.4 |
| 1f17216d-2e12-3d49-b1d1-67723fba74a4 | -3.2129 | -46.9383 | 2026-09-30 01:50:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 58.0 |
| 49016592-0b23-3ebe-901c-c870146a65e2 | -11.6395 | -43.5455 | 2026-09-30 01:50:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 84.2 |
| 9f164552-1571-3e43-8746-1dd48b610f1f | -3.2313 | -46.9596 | 2026-09-30 01:50:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 58.5 |
| 6557d82d-a001-341a-b33b-05699b381b45 | -21.3977 | -45.3069 | 2026-09-30 01:50:00 | GOES-19 | CARMO DA CACHOEIRA | MINAS GERAIS | Brasil | 3113909 | 31 | 33 | nan | nan | nan | Mata Atlântica | 77.4 |
| 67a19e77-3a74-3c1f-8ceb-afb00e077848 | -11.8488 | -50.4526 | 2026-09-30 01:50:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 49.8 |
| 29458f2f-b044-306b-bd54-af257f812e4d | -11.83 | -50.4333 | 2026-09-30 01:50:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 100.9 |
| 01ba2b30-376f-351c-9901-258e156cf571 | -2.9924 | -51.045 | 2026-09-30 01:50:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 78.3 |
| 1655880e-4186-3cff-942a-38b5141eacea | -22.0892 | -46.9756 | 2026-09-30 01:50:00 | GOES-19 | AGUAÍ | SÃO PAULO | Brasil | 3500303 | 35 | 33 | nan | nan | nan | Cerrado | 95.5 |
| ee3113b8-93d3-3746-998c-c883d9b757c9 | -7.8109 | -45.8173 | 2026-09-30 01:50:00 | GOES-19 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 111.6 |
| 80c52e48-4e7b-3596-80c6-814a8d280ea1 | -12.3277 | -47.9513 | 2026-09-30 01:50:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 81.5 |
| 4af953ec-cd65-3d00-9987-7b77592c0476 | -4.4507 | -47.9112 | 2026-09-30 01:50:00 | GOES-19 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 54.2 |
| b3ab38b7-a0d5-3eac-8092-2cb3a6a63fec | -3.3801 | -50.95 | 2026-09-30 01:50:00 | GOES-19 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 33.8 |
| c9f8f511-8c31-3b82-ba3a-cef5924d6de2 | -11.3918 | -43.4654 | 2026-09-30 01:50:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 74.0 |
| b6c02bd6-a387-34c7-8624-acef697bab8a | -11.8297 | -50.4548 | 2026-09-30 01:50:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 78.8 |
| 4c300918-1775-3e51-8d69-88837a3a28ac | -11.64 | -43.5218 | 2026-09-30 01:50:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 95.4 |
| a67b87c1-22cf-3723-a796-bf51f8538fe3 | -11.699 | -43.4416 | 2026-09-30 02:00:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 61.0 |
| 15482c4a-1cac-327a-9b6b-95ddb28caccc | -2.9924 | -51.045 | 2026-09-30 02:00:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 87.2 |
| 00383e60-feb5-3e7c-92d7-f25c95621b85 | -5.7561 | -45.1747 | 2026-09-30 02:00:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 56.6 |
| be7a2102-9f12-34c0-9172-d3fbe23d0b18 | -2.8899 | -54.0912 | 2026-09-30 02:00:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 72.4 |
| a0ffda19-86e0-3539-bd98-a8b65b474f02 | -2.9925 | -51.0242 | 2026-09-30 02:00:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 56.4 |
| d03a14e7-7471-3512-8e3a-a3e00db26dde | -3.2314 | -46.9376 | 2026-09-30 02:00:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 137.6 |
| 86a84c23-0959-3efb-9c80-556d0803a9f4 | -7.8109 | -45.8173 | 2026-09-30 02:00:00 | GOES-19 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 90.4 |
| adda2380-9c01-3724-9cf0-8e409bf25ddf | -12.2518 | -50.2543 | 2026-09-30 02:00:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 103.9 |
| 7ba4cd05-f41b-34c3-a53e-09ca0f30d8bb | -11.64 | -43.5218 | 2026-09-30 02:00:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 78.0 |
| 0ab2f89e-3ca9-397e-b462-fb5ea6ac0381 | -7.8295 | -45.8381 | 2026-09-30 02:00:00 | GOES-19 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 106.5 |
| dc819174-dded-36d7-83b6-0396209daef9 | -11.7182 | -43.4386 | 2026-09-30 02:00:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 91.8 |
| d387db37-bb91-36f7-9663-714a5db14874 | -6.9138 | -43.7049 | 2026-09-30 02:00:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 68.7 |


[Clique aqui para ver as próximas entradas](README7.md)
