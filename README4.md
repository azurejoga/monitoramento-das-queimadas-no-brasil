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

## Dados Diários - Página 4

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 369a3ccd-32d1-3aff-b4e9-8ab55d1ce83c | -2.9739 | -51.0455 | 2026-09-30 01:00:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 129.1 |
| 4d06e10d-dd40-3e37-92ac-3674e45f1b73 | -11.8297 | -50.4548 | 2026-09-30 01:00:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 56.4 |
| 3f4cdf32-48df-369a-a022-5b5a48cff078 | -11.1775 | -44.7832 | 2026-09-30 01:00:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 150.7 |
| 11f7b231-f4cf-3f62-95b0-e1cdd8baee77 | -2.974 | -51.0247 | 2026-09-30 01:00:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 95.1 |
| 376a551f-6a38-3770-a38e-88a0ceac6ef6 | -11.7182 | -43.4386 | 2026-09-30 01:00:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 85.9 |
| 26955b66-7543-365b-888a-c1e07dc7ddca | -2.9924 | -51.045 | 2026-09-30 01:00:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 87.5 |
| b37418f6-df3c-3e10-a5d0-618393fbf4f6 | -3.2314 | -46.9376 | 2026-09-30 01:00:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 245.4 |
| 83aba1e2-1bea-3cb6-9508-593613bf2496 | -2.9925 | -51.0242 | 2026-09-30 01:00:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 57.2 |
| a551d472-0844-3981-9d22-939b64c19284 | -4.8582 | -42.9332 | 2026-09-30 01:00:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 69.8 |
| 1a07212e-0c70-32be-880a-1157ba12d779 | -7.8107 | -45.8399 | 2026-09-30 01:00:00 | GOES-19 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 62.6 |
| 908ad3c8-57d4-3988-b4ca-477ce963cd07 | -7.8109 | -45.8173 | 2026-09-30 01:00:00 | GOES-19 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 122.1 |
| 02baea13-8095-396b-bb80-97880e8832be | -7.8297 | -45.8156 | 2026-09-30 01:00:00 | GOES-19 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 239.0 |
| d148c577-72d7-3730-829b-2bc4c0f5c95c | -11.8491 | -50.4311 | 2026-09-30 01:00:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 119.4 |
| f718ce97-79da-3bb2-b24a-32ee158acdaa | -7.8483 | -45.8363 | 2026-09-30 01:00:00 | GOES-19 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 115.6 |
| 6c87166a-f4b8-3728-8c16-be667bb14a12 | -3.2129 | -46.9383 | 2026-09-30 01:00:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 79.3 |
| 2455408f-787b-3f34-b650-7a41a84401d6 | -7.8295 | -45.8381 | 2026-09-30 01:00:00 | GOES-19 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 113.2 |
| 7487feff-4d9a-3463-acc5-ca71edbf67df | -7.8486 | -45.8138 | 2026-09-30 01:00:00 | GOES-19 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 187.5 |
| 2504c331-8f26-3118-b862-4fd99f7d3293 | -6.895 | -43.7066 | 2026-09-30 01:00:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 119.4 |
| 195cde87-d8a9-3619-ace4-36e21094809b | -5.7561 | -45.1747 | 2026-09-30 01:00:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 90.9 |
| b31f1072-a6c7-3328-a298-0bccd69067dd | -12.3085 | -47.9539 | 2026-09-30 01:00:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 168.5 |
| e9fe3757-6e07-3824-a1fa-45be46241b76 | -19.9067 | -49.5752 | 2026-09-30 01:00:00 | GOES-19 | ITAPAGIPE | MINAS GERAIS | Brasil | 3133402 | 31 | 33 | nan | nan | nan | Mata Atlântica | 92.6 |
| c02649a6-14e1-3490-bd39-a61bcee2944d | -11.1779 | -44.76 | 2026-09-30 01:00:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 78.3 |
| dfa405dc-5005-3b5f-982d-470378a0d16c | -11.8678 | -50.4504 | 2026-09-30 01:00:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 48.5 |
| 46314134-3ff0-36ec-95e4-a4aa87810b4e | -2.9082 | -54.0907 | 2026-09-30 01:00:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 94.4 |
| 20cdc031-0d2e-397b-826f-f0eda7cb55ce | -3.2313 | -46.9596 | 2026-09-30 01:00:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 64.1 |
| d988ade6-a1fc-3c96-a6dd-8769a72a5e93 | -4.4507 | -47.9112 | 2026-09-30 01:00:00 | GOES-19 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 63.6 |
| ab5e4fbf-f462-3522-9bdc-068eeb6d9f9b | -12.3089 | -47.9317 | 2026-09-30 01:00:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 74.9 |
| c2a3cad9-30de-3eff-97a7-7ea067cd8293 | -3.3801 | -50.95 | 2026-09-30 01:00:00 | GOES-19 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 76.5 |
| 8daa28a5-b49d-3df9-b079-878ab1a948e9 | -4.4506 | -47.9329 | 2026-09-30 01:00:00 | GOES-19 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 60.1 |
| 54f412c6-308c-3143-90cd-1f5f6a54ce55 | -13.3262 | -43.976 | 2026-09-30 01:10:00 | GOES-19 | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | 324.9 |
| 68c5acde-02a4-3f34-b8e3-828873807cc7 | -10.0779 | -63.0804 | 2026-09-30 01:10:00 | GOES-19 | ARIQUEMES | RONDÔNIA | Brasil | 1100023 | 11 | 33 | nan | nan | nan | Amazônia | 64.2 |
| a148ed84-e57c-37a6-bcbb-dd2ad15b5fe0 | -18.2632 | -53.0312 | 2026-09-30 01:10:00 | GOES-19 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 61.4 |
| f4d9171b-68d9-3d56-951f-d60429d8ba8f | -11.83 | -50.4333 | 2026-09-30 01:10:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 48.5 |
| 27801afa-fc65-3096-9d4d-bec08f68b783 | -18.2827 | -53.0496 | 2026-09-30 01:10:00 | GOES-19 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 126.3 |
| 1ec44cb9-26a3-36a0-a9d8-f6f8ff109540 | -18.3026 | -53.0464 | 2026-09-30 01:10:00 | GOES-19 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 58.1 |
| 22168f32-86f9-309a-bf09-f7eaf473c63e | -5.7561 | -45.1747 | 2026-09-30 01:10:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 85.9 |
| c8f40a33-38fb-35fb-8776-d4d3fb3b47a8 | -15.6256 | -43.2199 | 2026-09-30 01:10:00 | GOES-19 | PORTEIRINHA | MINAS GERAIS | Brasil | 3152204 | 31 | 33 | nan | nan | nan | Caatinga | 69.4 |
| 3d0c37a1-85ce-34e0-8de1-b561fb9d4ce7 | -13.3457 | -43.9726 | 2026-09-30 01:10:00 | GOES-19 | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | 249.6 |
| c9b145ce-90b9-3eb2-b72c-179ddace1a48 | -7.8297 | -45.8156 | 2026-09-30 01:10:00 | GOES-19 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 222.1 |
| 5fc1e573-8bd7-32f2-9c09-7840a1591969 | -2.9739 | -51.0455 | 2026-09-30 01:10:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 112.9 |
| c072bb2d-4f38-3ee2-b540-5d34f5d2288e | -7.4408 | -64.3272 | 2026-09-30 01:10:00 | GOES-19 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 63.0 |
| 5cb8df9a-9c64-3825-8ea1-21a25022d783 | -7.8486 | -45.8138 | 2026-09-30 01:10:00 | GOES-19 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 176.8 |
| 605237c1-437b-3e91-b7d2-d7a61ad099f3 | -13.3462 | -43.9489 | 2026-09-30 01:10:00 | GOES-19 | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | 231.4 |
| 6ec49e55-2553-35ee-87b6-b100685c18b6 | -11.8491 | -50.4311 | 2026-09-30 01:10:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 61.2 |
| f5b607e7-14dd-3b2b-89ff-48ab8e775dae | -11.9545 | -51.017 | 2026-09-30 01:10:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 57.7 |
| f44d6779-a25d-3b45-b142-b14d236dd051 | -7.4224 | -64.3277 | 2026-09-30 01:10:00 | GOES-19 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 57.3 |
| 6fa4c44f-8092-3634-9ffd-b7ec11c1e801 | -4.4507 | -47.9112 | 2026-09-30 01:10:00 | GOES-19 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 53.4 |
| 8e375520-a7db-3d7f-abcf-a350b9df7043 | -9.1626 | -60.7948 | 2026-09-30 01:10:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 39.3 |
| 5d537ff6-8461-3118-9e29-d307a56af265 | -13.3267 | -43.9523 | 2026-09-30 01:10:00 | GOES-19 | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | 277.8 |
| 0a2e4cb6-b09f-398b-8d47-6296fb4381d1 | -11.64 | -43.5218 | 2026-09-30 01:10:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 131.2 |
| 3704afe3-934a-3f9a-b59a-728600c5622d | -11.699 | -43.4416 | 2026-09-30 01:10:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 90.0 |
| 47596dc1-7e27-32f6-acfc-a8c48da202da | -6.895 | -43.7066 | 2026-09-30 01:10:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 103.1 |
| d49ce31c-e200-3ce7-a9c0-fbcbc61a5432 | -11.1775 | -44.7832 | 2026-09-30 01:10:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 81.2 |
| 940a13a6-b67f-3ca3-845e-9978a9780b93 | -2.9924 | -51.045 | 2026-09-30 01:10:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 78.0 |
| 5054fc41-f092-3cad-aa12-35272f61fe0b | -5.1806 | -55.9925 | 2026-09-30 01:10:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 53.2 |
| fc3dedfb-4026-3d06-8777-57949a25e42a | -7.8109 | -45.8173 | 2026-09-30 01:10:00 | GOES-19 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 111.4 |
| 1824de64-8373-3bbb-b051-ede0c9512612 | -12.3085 | -47.9539 | 2026-09-30 01:10:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 163.9 |
| 0f3075f0-d690-3fe2-9fc2-e7e963a8ccd2 | -11.9548 | -50.9957 | 2026-09-30 01:10:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 75.2 |
| 2b3478a8-0924-38e5-81f2-27c8a396bfac | -11.8297 | -50.4548 | 2026-09-30 01:10:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 84.5 |
| ca00c6b1-f1fe-3c96-872e-150cf9b56701 | -11.7182 | -43.4386 | 2026-09-30 01:10:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 80.8 |
| 8fc6342a-af22-3fbf-abcb-8e52cde9a530 | -3.2314 | -46.9376 | 2026-09-30 01:10:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 208.0 |
| c06ff837-2687-3c4f-95fa-98d83c58ac8d | -2.9925 | -51.0242 | 2026-09-30 01:10:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 53.9 |
| d6ecfdeb-e9fa-36b6-9ee8-29f271d544ed | -19.8864 | -49.5795 | 2026-09-30 01:10:00 | GOES-19 | ITAPAGIPE | MINAS GERAIS | Brasil | 3133402 | 31 | 33 | nan | nan | nan | Mata Atlântica | 187.8 |
| 166f3ac8-61c4-3241-8973-2b0fbbb0b21e | -7.4407 | -64.3459 | 2026-09-30 01:10:00 | GOES-19 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 75.7 |
| 7410dcdd-299e-3d90-94f5-c591cd376409 | -5.1621 | -55.9931 | 2026-09-30 01:10:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 59.1 |
| 0ad5730a-211a-31a5-9c5b-4606fb9d5593 | -7.4223 | -64.3464 | 2026-09-30 01:10:00 | GOES-19 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 65.3 |
| 586e4c05-0af2-367f-8109-f17f12c64289 | -12.3089 | -47.9317 | 2026-09-30 01:10:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 73.7 |
| b35e16b6-a153-36cf-ad30-d28900591a53 | -2.974 | -51.0247 | 2026-09-30 01:10:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 81.9 |
| 67cca775-05ed-3bb7-b6c0-dc3b0029eff9 | -3.2313 | -46.9596 | 2026-09-30 01:10:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 68.1 |
| 3c7bdabb-b9d4-333a-b2c5-659717f035a7 | -19.9067 | -49.5752 | 2026-09-30 01:10:00 | GOES-19 | ITAPAGIPE | MINAS GERAIS | Brasil | 3133402 | 31 | 33 | nan | nan | nan | Mata Atlântica | 166.5 |
| d3da39ec-81da-384e-873d-df8a67f61ce6 | -7.8483 | -45.8363 | 2026-09-30 01:10:00 | GOES-19 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 114.1 |
| fb6c323f-d3d5-336c-bdd9-ac0611141d42 | -11.3918 | -43.4654 | 2026-09-30 01:10:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 65.1 |
| 03d8d4e9-6cfe-3110-8cec-b49c3f101ba4 | -7.8295 | -45.8381 | 2026-09-30 01:10:00 | GOES-19 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 113.1 |
| ab6371e3-9245-34df-8c78-3afe8903d49a | -6.9138 | -43.7049 | 2026-09-30 01:10:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 71.1 |
| b1aad1f3-4a0b-3d75-a5a5-92c1c922bfdb | -18.2831 | -53.028 | 2026-09-30 01:10:00 | GOES-19 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 94.9 |
| 04232ba4-d4a0-351c-a141-5a89356e8fcd | -3.2129 | -46.9383 | 2026-09-30 01:10:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 71.9 |
| 36756e19-4189-39c7-b765-2a0c732b2e88 | -4.4506 | -47.9329 | 2026-09-30 01:10:00 | GOES-19 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 54.2 |
| 0c04da72-579e-30d3-a304-e73e16fbe605 | -7.8107 | -45.8399 | 2026-09-30 01:10:00 | GOES-19 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 61.2 |
| 928fd833-65e7-33d6-8cc1-0a1a9d1c976c | -3.2315 | -46.9156 | 2026-09-30 01:10:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 66.3 |
| b210b919-3ae8-3977-b7f7-9808aee142a9 | -2.9082 | -54.0907 | 2026-09-30 01:10:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 106.4 |
| 506be7f1-de12-30f5-b4e2-13e368650a28 | -11.8488 | -50.4526 | 2026-09-30 01:10:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 89.1 |
| caea4fee-38f8-31db-8653-60f7f3f9ec1d | -7.84 | -45.84 | 2026-09-30 01:15:00 | MSG-03 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 4727ffe3-003b-316a-ba97-34166b6ac10a | -3.23 | -46.93 | 2026-09-30 01:15:00 | MSG-03 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 9cd6a92c-6332-36f1-a591-31c1eb207e75 | -9.12502 | -67.84337 | 2026-09-30 01:17:00 | TERRA_M-M | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 22.3 |
| ae32c38e-2ec5-3274-8169-d700e8599275 | -7.43338 | -64.35036 | 2026-09-30 01:17:00 | TERRA_M-M | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 53.0 |
| a6bbd5fb-04b7-3c4b-b179-7e0f09b738bf | -9.11617 | -67.84464 | 2026-09-30 01:17:00 | TERRA_M-M | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 7.7 |
| 0b9c815b-aadf-3b0f-b3ec-06a5582cba61 | -9.11492 | -67.83568 | 2026-09-30 01:17:00 | TERRA_M-M | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 14.3 |
| 21480f23-c37f-3d7c-be67-37879445b70b | -8.03409 | -71.25968 | 2026-09-30 01:17:00 | TERRA_M-M | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 22.3 |
| 212cc1c1-ab21-3a29-9a48-7a6d64b6f531 | -9.12378 | -67.8344 | 2026-09-30 01:17:00 | TERRA_M-M | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 22.6 |
| 43be2466-497f-3149-be30-edd3ac61a182 | -12.12368 | -61.16316 | 2026-09-30 01:17:00 | TERRA_M-M | PARECIS | RONDÔNIA | Brasil | 1101450 | 11 | 33 | nan | nan | nan | Amazônia | 18.8 |
| 842ce7de-3ff0-3cfa-b65b-77d40eac067b | -10.07238 | -63.08377 | 2026-09-30 01:17:00 | TERRA_M-M | ARIQUEMES | RONDÔNIA | Brasil | 1100023 | 11 | 33 | nan | nan | nan | Amazônia | 68.4 |
| b706cc4d-be64-3316-943a-df1d9a0ca8e3 | -12.13823 | -63.17699 | 2026-09-30 01:17:00 | TERRA_M-M | SERINGUEIRAS | RONDÔNIA | Brasil | 1101500 | 11 | 33 | nan | nan | nan | Amazônia | 11.3 |
| d6fd11ca-a94b-3a3b-8700-491799f0aee2 | -12.1349 | -63.16916 | 2026-09-30 01:17:00 | TERRA_M-M | SERINGUEIRAS | RONDÔNIA | Brasil | 1101500 | 11 | 33 | nan | nan | nan | Amazônia | 8.2 |
| d9e47461-994e-331c-87e6-7481ed2743f7 | -9.16765 | -61.40635 | 2026-09-30 01:17:00 | TERRA_M-M | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 58.4 |
| 26366302-e9a1-3559-9020-363c4acb228e | -9.12267 | -67.76125 | 2026-09-30 01:17:00 | TERRA_M-M | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 0e48de79-981d-319b-953f-4bb3985a2c8f | -12.12027 | -61.14256 | 2026-09-30 01:17:00 | TERRA_M-M | PIMENTA BUENO | RONDÔNIA | Brasil | 1100189 | 11 | 33 | nan | nan | nan | Amazônia | 17.3 |
| ca3761b4-6dfc-33c2-bd80-aa277f655be3 | -9.10755 | -67.71751 | 2026-09-30 01:17:00 | TERRA_M-M | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 15.2 |
| aa606d87-dc65-31bb-b0f8-1344c07cd656 | -9.10482 | -67.82798 | 2026-09-30 01:17:00 | TERRA_M-M | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 9.4 |
| f65ea3a6-60f7-3574-9024-11a741d370b4 | -9.78225 | -59.01287 | 2026-09-30 01:17:00 | TERRA_M-M | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 36.9 |
| 8336653f-7a9f-3bca-9d6b-1ae9c6eaa51f | -9.10386 | -68.21042 | 2026-09-30 01:17:00 | TERRA_M-M | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 3.6 |


[Clique aqui para ver as próximas entradas](README5.md)
