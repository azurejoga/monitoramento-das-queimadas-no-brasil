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

## Dados Diários - Página 5

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 8a85cee7-cbfc-3e73-9b57-92c70e654beb | -8.02639 | -45.03749 | 2026-06-12 04:12:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| d4daf33e-d905-35e1-a52e-94be1726bcd6 | -10.84063 | -53.74152 | 2026-06-12 04:12:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| b9dc5a4c-74d6-3bd9-abb5-d544088b87f6 | -10.83468 | -53.74014 | 2026-06-12 04:12:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 1f0e9fdc-8b7c-31b9-a7c5-6fab0735be27 | -7.32733 | -47.04743 | 2026-06-12 04:12:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| a88a4fe7-e405-3004-ad4d-15a1cd206e66 | -10.82537 | -53.72428 | 2026-06-12 04:12:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 36b3e013-2e9a-31a1-9f0f-0c466e2abff8 | -9.29461 | -47.62435 | 2026-06-12 04:12:00 | NOAA-20 | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 962b686f-8fc3-3336-a430-2a1c2d07f20a | -12.4772 | -45.44356 | 2026-06-12 04:12:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| e56b4bca-2d41-3b3c-89c6-ce35c9054c03 | -10.99961 | -46.74697 | 2026-06-12 04:12:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| ca69956e-0189-38cc-8cff-fc5a23f8fb1c | -7.64578 | -45.29578 | 2026-06-12 04:12:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| c302917e-864a-3f06-910b-0e7bfb66cd36 | -11.5775 | -47.45488 | 2026-06-12 04:12:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 5650a465-866a-35ca-ad10-18177d1d1080 | -10.71619 | -49.48269 | 2026-06-12 04:12:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 684f8409-0fbb-34ed-961b-835846199e02 | -10.61138 | -44.32566 | 2026-06-12 04:12:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 244617c4-1b37-3fe8-bcbb-fbde01d42006 | -10.61185 | -44.32552 | 2026-06-12 04:12:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| cd9d8837-feaa-3cb1-8088-ff5d4e688d6f | -9.07222 | -44.74501 | 2026-06-12 04:12:00 | NOAA-20 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| dc6617bd-14e4-3490-b411-5b9b2f649b44 | -11.25643 | -53.95569 | 2026-06-12 04:12:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 5.5 |
| de90fe3c-8a41-3f79-b460-12e0ec5e1217 | -10.8482 | -46.76701 | 2026-06-12 04:12:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 05ee32a1-8b44-3980-bac1-329a62444c32 | -12.8614 | -44.36541 | 2026-06-12 04:12:00 | NOAA-20 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 25.9 |
| b6d3c1b5-a114-326e-a6f6-0954a0f4dc6b | -10.29424 | -46.62625 | 2026-06-12 04:12:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| a3e8e908-97fb-3876-a796-8f6174027f37 | -9.2961 | -47.62527 | 2026-06-12 04:12:00 | NOAA-20 | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| b8846300-a3a1-3883-8ee2-168d7fb6e6aa | -10.84875 | -46.76928 | 2026-06-12 04:12:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 2fce8b2c-3989-368e-a1bb-6d1bc7c3b966 | -11.54452 | -48.26907 | 2026-06-12 04:12:00 | NOAA-20 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| a5357e47-2405-325c-8acc-e68ee04e42e6 | -10.84737 | -46.77172 | 2026-06-12 04:12:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| fbb9dbbd-083f-34a4-ae1d-04977956e327 | -10.82961 | -53.73433 | 2026-06-12 04:12:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 27fa9a89-1903-3742-847b-05c4e442893d | -7.74362 | -47.56927 | 2026-06-12 04:12:00 | NOAA-20 | BARRA DO OURO | TOCANTINS | Brasil | 1703073 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| c37479e6-9206-36e0-86ab-26ce6775a591 | -9.31186 | -48.97329 | 2026-06-12 04:12:00 | NOAA-20 | DOIS IRMÃOS DO TOCANTINS | TOCANTINS | Brasil | 1707207 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 776207b8-7ff1-3f53-bdab-c0bf901ae150 | -12.8608 | -44.36906 | 2026-06-12 04:12:00 | NOAA-20 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 25.9 |
| d76ec8ab-d02d-3713-94b4-ac377f4ce40d | -10.94616 | -44.18789 | 2026-06-12 04:12:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 0.5 |
| b8799b4a-92cd-3b4f-a98c-a218903207f0 | -9.74168 | -47.86902 | 2026-06-12 04:12:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 61d15661-e432-3844-83c0-1de905daecdf | -12.85132 | -44.36369 | 2026-06-12 04:12:00 | NOAA-20 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 5eabdb38-c089-3f5a-ae48-df794f7ee048 | -10.90065 | -49.34808 | 2026-06-12 04:12:00 | NOAA-20 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| aed0871a-5087-3f93-bb11-f86e1c48a142 | -12.3493 | -47.90101 | 2026-06-12 04:12:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 68319906-dcca-34ce-bf9f-dbfc4011e467 | -12.14664 | -48.45589 | 2026-06-12 04:12:00 | NOAA-20 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| adfe3b9e-a703-3147-8c52-84706e981fa3 | -9.21024 | -48.57866 | 2026-06-12 04:12:00 | NOAA-20 | MIRANORTE | TOCANTINS | Brasil | 1713304 | 17 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 30742e2a-9021-35aa-990e-ec23b559b18a | -12.85685 | -44.37213 | 2026-06-12 04:12:00 | NOAA-20 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 73db6217-d001-316a-bdc7-db88953d632b | -11.90547 | -43.7365 | 2026-06-12 04:12:00 | NOAA-20 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 7df4a82b-dc59-3124-be0d-0154d6c0ca05 | -9.00714 | -47.99445 | 2026-06-12 04:12:00 | NOAA-20 | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 798fc17e-9f2b-3c4b-872b-0a36e4526916 | -11.74385 | -48.91007 | 2026-06-12 04:12:00 | NOAA-20 | GURUPI | TOCANTINS | Brasil | 1709500 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| e38126d9-44bd-3da9-ac4c-84a4851eeb58 | -7.3268 | -47.04646 | 2026-06-12 04:12:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| b662ac48-21d5-3d92-8565-eec10b100778 | -11.79641 | -40.07759 | 2026-06-12 04:12:00 | NOAA-20 | MAIRI | BAHIA | Brasil | 2920106 | 29 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 76d13633-c9ea-3951-b7d0-5bcd7a3d212f | -10.93358 | -44.67215 | 2026-06-12 04:12:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 9956ace6-b02e-3b3f-861e-7080ae82b03b | -7.33431 | -47.05167 | 2026-06-12 04:12:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 04867a9e-d7bf-388a-9b50-b5f6d3450cda | -12.47371 | -45.44297 | 2026-06-12 04:12:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 6d74b092-3e38-36d2-bd31-768a0b56e93a | -13.84488 | -41.40947 | 2026-06-12 04:12:00 | NOAA-20 | ITUAÇU | BAHIA | Brasil | 2917201 | 29 | 33 | nan | nan | nan | Caatinga | 2.4 |
| c62ede3e-9efc-3102-85f9-3cd49c3cdef2 | -11.71605 | -37.66782 | 2026-06-12 04:12:00 | NOAA-20 | CONDE | BAHIA | Brasil | 2908606 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 3aff5d82-004b-387b-836c-d8e1e8ae3b3a | -7.30719 | -46.29628 | 2026-06-12 04:12:00 | NOAA-20 | NOVA COLINAS | MARANHÃO | Brasil | 2107258 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 8395293d-63a5-3f1c-aae3-30d5528f1ea2 | -12.31653 | -46.07385 | 2026-06-12 04:12:00 | NOAA-20 | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 878e466b-8104-37fc-83df-e38fa28e8bfe | -7.74716 | -47.5739 | 2026-06-12 04:12:00 | NOAA-20 | BARRA DO OURO | TOCANTINS | Brasil | 1703073 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| c47ab85b-a628-366a-bc47-b4003c08d649 | -9.21463 | -48.57945 | 2026-06-12 04:12:00 | NOAA-20 | MIRANORTE | TOCANTINS | Brasil | 1713304 | 17 | 33 | nan | nan | nan | Cerrado | 4.9 |
| a03d09fa-bc7d-3299-9b37-9eaa1a39f4f4 | -9.30821 | -48.96776 | 2026-06-12 04:12:00 | NOAA-20 | DOIS IRMÃOS DO TOCANTINS | TOCANTINS | Brasil | 1707207 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| f607743e-64e2-3791-8e5a-15301800c453 | -12.85804 | -44.36484 | 2026-06-12 04:12:00 | NOAA-20 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 25.9 |
| 355a6aaf-bdbb-3215-99d2-a4de245b2305 | -11.54039 | -48.26832 | 2026-06-12 04:12:00 | NOAA-20 | SANTA ROSA DO TOCANTINS | TOCANTINS | Brasil | 1718907 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 98c5caee-e814-3415-84fb-6810bbc36453 | -9.00754 | -47.99565 | 2026-06-12 04:12:00 | NOAA-20 | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| b690ca66-c0e8-366f-8983-341aceeafb37 | -11.25464 | -53.95652 | 2026-06-12 04:12:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| a1999161-c1fe-30f9-9cd4-144961709b2a | -9.00644 | -47.9984 | 2026-06-12 04:12:00 | NOAA-20 | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 2520cb75-e1be-33f1-b510-368a5430671a | -8.94054 | -47.26038 | 2026-06-12 04:12:00 | NOAA-20 | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| d7c0b6d0-7368-3aa5-b368-1193c20d3d77 | -7.72126 | -44.16669 | 2026-06-12 04:12:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 04077152-c054-384d-b5f1-c14216f980fc | -9.21193 | -47.91738 | 2026-06-12 04:12:00 | NOAA-20 | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 61d25b0f-04b9-3ba4-80a3-f8d89719b1e8 | -7.33087 | -47.04725 | 2026-06-12 04:12:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| f4809b76-bc78-3400-b75a-04c02ff74cc6 | -10.8338 | -53.74464 | 2026-06-12 04:12:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| b3515193-214f-371d-893a-7efd4b78c58b | -11.80375 | -44.95238 | 2026-06-12 04:12:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| f3ced856-b25d-3405-8eca-90bbebc7f583 | -7.33368 | -47.05531 | 2026-06-12 04:12:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 2800479e-a93c-3117-bef7-1837d78cfe90 | -9.84531 | -38.95948 | 2026-06-12 04:12:00 | NOAA-20 | CANUDOS | BAHIA | Brasil | 2906824 | 29 | 33 | nan | nan | nan | Caatinga | 1.1 |
| b321e805-e2c5-3ade-8756-8488ee542bfa | -7.34936 | -47.0132 | 2026-06-12 04:12:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 13.4 |
| b45927d4-31c1-3c8f-97a0-8986a52c255a | -7.63699 | -45.30324 | 2026-06-12 04:12:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| bc9ab107-6a41-3088-ae51-add569a43315 | -12.14732 | -48.45205 | 2026-06-12 04:12:00 | NOAA-20 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 388b5708-5091-31b9-8535-dc3d2c79f060 | -7.33712 | -47.05975 | 2026-06-12 04:12:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 151a4a62-b73f-3587-9cb1-7b76ae5b947f | -7.64139 | -45.29951 | 2026-06-12 04:12:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 35471fb5-61cd-3bb1-8fcc-36ec41db3000 | -12.86021 | -44.37271 | 2026-06-12 04:12:00 | NOAA-20 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 3fdd3f50-652c-3880-86de-83a1240abdd1 | -9.3127 | -48.96863 | 2026-06-12 04:12:00 | NOAA-20 | DOIS IRMÃOS DO TOCANTINS | TOCANTINS | Brasil | 1707207 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 381a2d50-af70-38e1-91e8-3b1097affaa6 | -9.10898 | -47.96003 | 2026-06-12 04:12:00 | NOAA-20 | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 6e94462d-9414-3e25-a044-4970a6972591 | -7.36611 | -49.87583 | 2026-06-12 04:12:00 | NOAA-20 | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 6bdc2922-7d31-3cd6-bad5-179532f395c7 | -10.90001 | -49.48167 | 2026-06-12 04:12:00 | NOAA-20 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 5aa253cd-4395-3d12-862c-d09ad4e26fab | -7.36512 | -49.8759 | 2026-06-12 04:12:00 | NOAA-20 | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 963d1211-2eb8-3d34-a2d8-1b2ce3a4729c | -14.08707 | -42.11688 | 2026-06-12 04:12:00 | NOAA-20 | LAGOA REAL | BAHIA | Brasil | 2918753 | 29 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 4cf9b623-b2ed-37aa-89ab-1280489052da | -11.57836 | -47.44988 | 2026-06-12 04:12:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| b0677512-0fcd-309e-9cd5-259d81d4d7fa | -9.21387 | -48.58383 | 2026-06-12 04:12:00 | NOAA-20 | MIRANORTE | TOCANTINS | Brasil | 1713304 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 4b5afbb6-5bde-3dd4-a6f8-d7e8a48d56af | -11.81445 | -47.24979 | 2026-06-12 04:12:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 1edc99c5-0ae8-31ec-baa5-5b60176caed3 | -11.26069 | -53.95756 | 2026-06-12 04:12:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| a86ba91e-18a1-39d0-903c-d3989193298b | -14.07464 | -39.50198 | 2026-06-12 04:12:00 | NOAA-20 | UBATÃ | BAHIA | Brasil | 2932309 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 3c04b684-0c64-363a-b4af-e613e4447cc6 | -9.20774 | -47.91661 | 2026-06-12 04:12:00 | NOAA-20 | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| df6e1283-a7e8-37eb-8cee-551dac098dbe | -9.06521 | -44.7438 | 2026-06-12 04:12:00 | NOAA-20 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 6864943a-7d73-3782-9d1c-0bc9c57966bb | -7.72189 | -44.16286 | 2026-06-12 04:12:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 5.3 |
| b363c7e2-c106-3494-ba9c-1019a772cf03 | -7.63011 | -50.03849 | 2026-06-12 04:12:00 | NOAA-20 | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 1b85d392-9e46-35af-bf1d-bf300e272ff5 | -9.74101 | -47.87285 | 2026-06-12 04:12:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| c68e70fe-9319-30aa-ae6f-16e3bea50286 | -9.69733 | -47.69461 | 2026-06-12 04:12:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| bd634387-2f70-3637-ab56-28603d121a70 | -9.20841 | -47.9127 | 2026-06-12 04:12:00 | NOAA-20 | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| c414f1f3-b191-3ca6-9c7b-0be54e8e6d7a | -12.92764 | -43.61757 | 2026-06-12 04:12:00 | NOAA-20 | SÍTIO DO MATO | BAHIA | Brasil | 2930758 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| a9aff0cd-af6d-35d1-9443-f718376f80d6 | -13.8957 | -43.78931 | 2026-06-12 04:12:00 | NOAA-20 | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| fda06255-1056-3186-94c1-06c7ec94ce62 | -8.02998 | -45.03809 | 2026-06-12 04:12:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 64940230-98e8-3880-8c6a-8dc650ba3a6f | -12.03222 | -47.80241 | 2026-06-12 04:12:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 0dba9c4f-710a-3938-a271-5aa0208c0640 | -14.07358 | -39.49935 | 2026-06-12 04:12:00 | NOAA-20 | UBATÃ | BAHIA | Brasil | 2932309 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| b31f555b-a68c-31b3-8f22-fedf826899d6 | -12.74706 | -43.93459 | 2026-06-12 04:12:00 | NOAA-20 | SERRA DOURADA | BAHIA | Brasil | 2930303 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 9bf11416-e06d-3faf-b388-b3ed0fcba664 | -11.7958 | -40.08162 | 2026-06-12 04:12:00 | NOAA-20 | MAIRI | BAHIA | Brasil | 2920106 | 29 | 33 | nan | nan | nan | Caatinga | 1.3 |
| d618507d-796f-3304-80b8-c4f3202b1e98 | -7.36611 | -49.87021 | 2026-06-12 04:12:00 | NOAA-20 | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 522191c8-64ea-3bad-a9f7-1e0e592b3bb2 | -12.85409 | -44.36791 | 2026-06-12 04:12:00 | NOAA-20 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 27c81102-cc7f-35b8-9cf9-e0b55e00fdeb | -9.6247 | -49.01921 | 2026-06-12 04:12:00 | NOAA-20 | ABREULÂNDIA | TOCANTINS | Brasil | 1700251 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 87c12ebe-8c99-315d-998b-69ea084c734f | -7.36714 | -49.87015 | 2026-06-12 04:12:00 | NOAA-20 | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 1da76380-1d84-30ab-a6c1-96c096ee42c2 | -7.74847 | -47.56616 | 2026-06-12 04:12:00 | NOAA-20 | BARRA DO OURO | TOCANTINS | Brasil | 1703073 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 83ad7987-0ddf-38ed-87ab-f76a4657da48 | -8.03358 | -45.03869 | 2026-06-12 04:12:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| b38bf10a-dff3-3764-834e-f33ec3ad54ed | -10.9941 | -44.13459 | 2026-06-12 04:12:00 | NOAA-20 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |


[Clique aqui para ver as próximas entradas](README6.md)
