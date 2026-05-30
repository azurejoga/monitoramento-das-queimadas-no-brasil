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

## Dados Diários - Página 3

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 5e5b3c32-fb14-3ca4-99df-514442b31b10 | -10.76177 | -46.96758 | 2026-05-30 04:02:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 0d70e0ec-fb64-3229-92a6-21ac2b1c5459 | -9.40034 | -48.45047 | 2026-05-30 04:02:00 | NOAA-21 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| d5393a4e-0e15-36b7-b843-a071c63b1d2e | -10.82127 | -46.95689 | 2026-05-30 04:02:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 784cdc28-63e1-3781-a6a8-e0b5c1537734 | -10.84353 | -46.93067 | 2026-05-30 04:02:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 0a19ae6d-f09e-31f3-baad-02f7cc858fa2 | -10.76737 | -46.98589 | 2026-05-30 04:02:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 13.6 |
| de887a6f-2bb2-30db-b1fd-45cd89fad2c5 | -9.92614 | -48.00515 | 2026-05-30 04:02:00 | NOAA-21 | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 7f342dbe-c647-3548-b899-d277f2a5de79 | -10.84423 | -46.92661 | 2026-05-30 04:02:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| d09c4366-74e6-3255-b015-7fe2edbed7a5 | -9.79856 | -48.92549 | 2026-05-30 04:02:00 | NOAA-21 | BARROLÂNDIA | TOCANTINS | Brasil | 1703107 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 38047f40-17e6-3aac-9e77-cc3bd523a9d5 | -8.72671 | -47.83281 | 2026-05-30 04:02:00 | NOAA-21 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 3a9bf221-72c3-39ee-9311-ac4077ce82e0 | -8.40818 | -49.60627 | 2026-05-30 04:02:00 | NOAA-21 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 247a6e7e-3b7c-3306-abaa-8d55beca7429 | -10.76609 | -46.96826 | 2026-05-30 04:02:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 5.0 |
| ba8dc9df-36d0-3006-b05c-f5e23c8493fc | -7.33984 | -49.85836 | 2026-05-30 04:02:00 | NOAA-21 | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 771b9f55-ed56-3730-972a-c712bb95061b | -6.75797 | -45.00996 | 2026-05-30 04:02:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| c24253bb-f6b7-3455-87ca-ceba6bf25c50 | -6.39452 | -44.16943 | 2026-05-30 04:02:00 | NOAA-21 | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 0092d0b6-6e6c-3c8e-a6ab-416924f8fab5 | -10.84139 | -46.91759 | 2026-05-30 04:02:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| e45840b4-ed3e-3e5f-905c-4de00dac27dc | -8.40878 | -49.60291 | 2026-05-30 04:02:00 | NOAA-21 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| d0b35ae4-3c76-329c-a612-1a56d77e7849 | -10.75877 | -46.9843 | 2026-05-30 04:02:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| a148a41b-c203-3ba5-8c01-d90f756a9fb9 | -11.70531 | -38.55463 | 2026-05-30 04:02:00 | NOAA-21 | SÁTIRO DIAS | BAHIA | Brasil | 2929701 | 29 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 18b060d9-d99f-36f2-bfa6-6e4612430e06 | -9.9302 | -48.68734 | 2026-05-30 04:02:00 | NOAA-21 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| eca002d3-85ba-30b5-8bd8-e4f319f6fcd8 | -10.78489 | -46.93738 | 2026-05-30 04:02:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 2dfc4315-5c7e-3e90-9b7a-5e2f70bff298 | -10.84495 | -46.92252 | 2026-05-30 04:02:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 61e6c87e-a052-3185-a7dc-365694aaea39 | -5.28562 | -43.96044 | 2026-05-30 04:02:00 | NOAA-21 | SENADOR ALEXANDRE COSTA | MARANHÃO | Brasil | 2111748 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| c5671985-f816-3980-8872-a24910e0ebf3 | -10.7648 | -46.95069 | 2026-05-30 04:02:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 8ff5faa4-ac81-38f7-9ba1-b07e2383d747 | -10.80491 | -46.94922 | 2026-05-30 04:02:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| e6b69aad-c5ff-3916-96c1-49a964738f78 | -10.81437 | -46.89563 | 2026-05-30 04:02:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 6acbb8b8-1801-3564-91ca-d92f6978831e | -10.83222 | -46.89435 | 2026-05-30 04:02:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 2a7b537a-ccbb-3035-bb78-91d250869c98 | -10.84139 | -46.94294 | 2026-05-30 04:02:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| cc036f77-216f-3179-a93a-7c05897545f5 | -7.84484 | -46.25957 | 2026-05-30 04:02:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 1734fc1d-238e-3d38-a8c0-a8c28913d22c | -10.76778 | -46.93409 | 2026-05-30 04:02:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| ff83b549-8beb-3e43-a6ff-9f4580f554ef | -9.50478 | -40.3064 | 2026-05-30 04:02:00 | NOAA-21 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 483de178-9fe9-3474-b1ee-b97d5c2630a9 | -10.76306 | -46.98515 | 2026-05-30 04:02:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 879d1a22-75a6-3a7d-b5a4-b840d78fe988 | -10.77394 | -46.97393 | 2026-05-30 04:02:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| f764468a-f8a4-32ba-9a9e-20371cabc56e | -10.06384 | -49.11311 | 2026-05-30 04:02:00 | NOAA-21 | MONTE SANTO DO TOCANTINS | TOCANTINS | Brasil | 1713700 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 238c9be3-a3f0-326d-8c79-d53876254a8a | -10.76276 | -46.93742 | 2026-05-30 04:02:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 2f747f94-feec-3cac-96fc-dd036d9c8a8b | -10.06329 | -49.1161 | 2026-05-30 04:02:00 | NOAA-21 | MONTE SANTO DO TOCANTINS | TOCANTINS | Brasil | 1713700 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 077c53fb-98b0-36a3-8336-9f504aace425 | -10.82207 | -46.92708 | 2026-05-30 04:02:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 1a0ad402-3685-30c1-8bb0-3e13d3a8d7f7 | -10.76329 | -46.95913 | 2026-05-30 04:02:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 7.6 |
| cd82ba36-735a-3d5d-8121-de7b9ccedf4e | -10.82054 | -46.96106 | 2026-05-30 04:02:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| c523858c-7795-3294-b88c-7acea9310a1a | -10.77618 | -46.96139 | 2026-05-30 04:02:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| a1718196-571f-310c-8e5c-b606186a6c32 | -10.79835 | -46.96132 | 2026-05-30 04:02:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| dbc4cabb-c996-3c6c-a81f-0ca836bf901f | -10.7676 | -46.95984 | 2026-05-30 04:02:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 7.6 |
| 72010eb4-fc77-3bc1-8068-001fecc612dc | -7.71559 | -44.5652 | 2026-05-30 04:02:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 9a856e37-08e9-3f7a-800b-df10ecc464f4 | -6.99226 | -42.88142 | 2026-05-30 04:02:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 7bc429f0-b0e2-366f-abcb-0bc1a734621d | -17.83944 | -42.61342 | 2026-05-30 04:04:00 | NOAA-21 | ARICANDUVA | MINAS GERAIS | Brasil | 3104452 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 3dae62e5-d273-3d88-9d49-7f4e0ba94d55 | -11.59086 | -47.44994 | 2026-05-30 04:04:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| e87ca401-b261-3212-89c5-78cd0167069c | -10.80056 | -48.29768 | 2026-05-30 04:04:00 | NOAA-21 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 10.1 |
| 376d7607-72ed-3ff4-b5e6-06ccfdd585e1 | -11.76249 | -47.07323 | 2026-05-30 04:04:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 0e332ead-2bb3-3180-97db-e55cc4c7f7df | -11.16784 | -46.79232 | 2026-05-30 04:04:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 1908cdf8-4575-3340-b03d-8b997fa861fb | -10.80158 | -48.292 | 2026-05-30 04:04:00 | NOAA-21 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 10.1 |
| 6f2e38ac-ec16-39aa-9995-42d97dcac557 | -10.73131 | -49.0259 | 2026-05-30 04:04:00 | NOAA-21 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| a7d69f93-5986-3fdd-bc9c-36f84cd3459c | -10.99129 | -49.04247 | 2026-05-30 04:04:00 | NOAA-21 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 5d381150-b445-3bb4-b831-9e02e6d7cdb3 | -12.00828 | -45.35706 | 2026-05-30 04:04:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 16fb9ae3-017e-3a85-84b9-7e9771b2e2dd | -12.34697 | -40.4204 | 2026-05-30 04:04:00 | NOAA-21 | ITABERABA | BAHIA | Brasil | 2914703 | 29 | 33 | nan | nan | nan | Caatinga | 1.1 |
| e264f183-9c5b-32c7-afce-b3c27a879e57 | -12.318 | -47.89786 | 2026-05-30 04:04:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| c2984b7f-edfc-334f-8453-1f93600b41b3 | -11.16855 | -46.78828 | 2026-05-30 04:04:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 07d4dc14-879b-345e-8e33-bdba133e8883 | -11.92632 | -43.9263 | 2026-05-30 04:04:00 | NOAA-21 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 2364c7b4-6059-339f-8414-3178bda9dcde | -12.00322 | -45.35952 | 2026-05-30 04:04:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 85496d47-8849-3a18-afe4-beb281a81057 | -10.80531 | -48.29825 | 2026-05-30 04:04:00 | NOAA-21 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| ede1e2e2-aac2-374e-9198-2872e528cee0 | -15.59858 | -46.81499 | 2026-05-30 04:04:00 | NOAA-21 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| d1d6bec9-5ee2-3a5b-b934-edf748332ffa | -11.92645 | -43.92649 | 2026-05-30 04:04:00 | NOAA-21 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 165a7add-286f-3c1d-be6b-e8a42691bee3 | -11.58801 | -47.44059 | 2026-05-30 04:04:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 68f256d5-4860-3565-930a-4c893500d1e6 | -11.96609 | -44.1914 | 2026-05-30 04:04:00 | NOAA-21 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 2ff545fb-e564-33dd-b684-2fc86c456165 | -11.97421 | -47.89238 | 2026-05-30 04:04:00 | NOAA-21 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| d1fa3e1c-6984-37f6-8bcd-90217fa3c2c5 | -17.83887 | -42.61702 | 2026-05-30 04:04:00 | NOAA-21 | ARICANDUVA | MINAS GERAIS | Brasil | 3104452 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 665310fb-10e7-3bf5-b230-06171c33f3e1 | -12.70398 | -44.79078 | 2026-05-30 04:04:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| d9554efd-9069-34b9-acd2-2645f8d1495d | -12.00048 | -47.77105 | 2026-05-30 04:04:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| b4b1d43d-b9e3-3441-8848-2ae82b8877fa | -15.3069 | -47.38199 | 2026-05-30 04:04:00 | NOAA-21 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| be0919f9-da1c-37ec-8284-5e94c05a45d3 | -11.99683 | -47.76581 | 2026-05-30 04:04:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 19dfb5f6-530d-33f8-bd35-dc44f74dfa75 | -11.58941 | -47.45801 | 2026-05-30 04:04:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 19701844-3981-3279-b78e-b52c9b8e3d81 | -11.70096 | -44.16518 | 2026-05-30 04:04:00 | NOAA-21 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 2e3f01e7-6485-347a-b737-fba38698efbe | -12.32097 | -47.89755 | 2026-05-30 04:04:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 85f668a9-5d74-308c-aefe-2c21c02ace02 | -16.21691 | -43.76551 | 2026-05-30 04:04:00 | NOAA-21 | CAPITÃO ENÉAS | MINAS GERAIS | Brasil | 3112703 | 31 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 9386c834-9238-3e37-a49d-cbdcf295668e | -10.7812 | -48.54242 | 2026-05-30 04:04:00 | NOAA-21 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 8dccd7b3-e3ca-3604-9161-b02ade561078 | -14.71432 | -43.21058 | 2026-05-30 04:04:00 | NOAA-21 | ESPINOSA | MINAS GERAIS | Brasil | 3124302 | 31 | 33 | nan | nan | nan | Caatinga | 0.4 |
| b8b8013c-6ca2-3a7a-8901-b3d66ce77770 | -17.93549 | -42.67393 | 2026-05-30 04:04:00 | NOAA-21 | ITAMARANDIBA | MINAS GERAIS | Brasil | 3132503 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.4 |
| c6d3f9e2-ba72-3a97-ae88-d7d07d9feb10 | -11.59676 | -47.44218 | 2026-05-30 04:04:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 7387084e-aad4-3c0f-a7da-6e42f6fc71bb | -14.90111 | -44.80156 | 2026-05-30 04:04:00 | NOAA-21 | BONITO DE MINAS | MINAS GERAIS | Brasil | 3108255 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 12d94ab6-997b-3a15-a70d-25f25fa4895c | -11.16433 | -46.78756 | 2026-05-30 04:04:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 61f016b0-edfd-384a-86d5-794e1e49f060 | -18.11835 | -42.43835 | 2026-05-30 04:04:00 | NOAA-21 | SANTA MARIA DO SUAÇUÍ | MINAS GERAIS | Brasil | 3158201 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 2e66e11c-b015-3f97-809a-6cb593b193eb | -14.71096 | -43.21 | 2026-05-30 04:04:00 | NOAA-21 | ESPINOSA | MINAS GERAIS | Brasil | 3124302 | 31 | 33 | nan | nan | nan | Caatinga | 1.1 |
| f9453b2a-1209-389a-8b35-fdbb1e89bec2 | -12.13324 | -47.2137 | 2026-05-30 04:04:00 | NOAA-21 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 920e7c8e-42d3-3b72-98c1-282950bd2fe0 | -12.1325 | -47.21781 | 2026-05-30 04:04:00 | NOAA-21 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 5764dbf3-5e90-355c-8f02-250a88afe3bf | -11.76464 | -47.06112 | 2026-05-30 04:04:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 9fc2b465-79dd-3524-84e8-ef736959d34a | -11.90931 | -43.83211 | 2026-05-30 04:04:00 | NOAA-21 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 7c918853-74b9-3973-93d4-0dea362e43d2 | -11.54131 | -46.42786 | 2026-05-30 04:04:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| f105924d-a814-36e8-ac6d-38abd1dadc40 | -10.79066 | -48.54465 | 2026-05-30 04:04:00 | NOAA-21 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 5cf439b8-c123-38c7-b4a4-bfacb072c6c5 | -13.47766 | -47.51338 | 2026-05-30 04:04:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| b58358b3-d801-3968-a83b-514722e2bfb7 | -11.5901 | -47.45415 | 2026-05-30 04:04:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 80d49002-b706-3d0c-a55a-dc9988dfb4e7 | -10.78013 | -48.54815 | 2026-05-30 04:04:00 | NOAA-21 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 7fd2bcd6-5392-3778-b387-04b2b5c1ccda | -11.99603 | -47.77026 | 2026-05-30 04:04:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| d9e8c8b7-1599-33d1-9239-c08452995fdc | -10.84782 | -48.34174 | 2026-05-30 04:04:00 | NOAA-21 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 4e04cd56-bba6-3bee-98df-a42e7a6b81b2 | -11.90864 | -43.83614 | 2026-05-30 04:04:00 | NOAA-21 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 2434e19f-2272-3ab7-ad78-19e851809bd5 | -15.58673 | -46.81318 | 2026-05-30 04:04:00 | NOAA-21 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| f3b39316-bd68-3859-aa12-19f565b383d1 | -11.58648 | -47.44913 | 2026-05-30 04:04:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 15.5 |
| ace3ca39-db8f-34bf-aef3-54671e6b0fe2 | -11.16996 | -46.80508 | 2026-05-30 04:04:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 4782bd9c-bf4c-3530-9d5b-ce75fb696079 | -18.69606 | -47.30613 | 2026-05-30 04:04:00 | NOAA-21 | COROMANDEL | MINAS GERAIS | Brasil | 3119302 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| cc867427-7cd7-3295-9505-d4826fbc550f | -15.58765 | -46.80804 | 2026-05-30 04:04:00 | NOAA-21 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 55b5a500-0339-3646-90be-414f34e10877 | -11.59163 | -47.44563 | 2026-05-30 04:04:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| b471e28d-88dc-3f53-b065-3128a53c1161 | -12.44772 | -44.74981 | 2026-05-30 04:04:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 06c3b81a-a6f4-35f6-a1a3-9b2cb9a77254 | -13.47411 | -47.5141 | 2026-05-30 04:04:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 4.5 |


[Clique aqui para ver as próximas entradas](README4.md)
