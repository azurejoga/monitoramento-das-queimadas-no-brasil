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

## Dados Diários - Página 96

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 13ed08b1-4d22-329d-b2cf-2a27e21c6e5f | -9.4618 | -60.5682 | 2025-08-29 13:50:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 272.9 |
| bdd90490-e4e1-38bb-a2fe-28705d02b1c0 | -13.5967 | -46.8684 | 2025-08-29 13:50:00 | GOES-19 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 91.8 |
| d739e3ff-92f6-3bae-a8b5-730998655d29 | -9.4432 | -60.5692 | 2025-08-29 13:50:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 146.8 |
| 853ba43b-cd19-3402-99a8-fd33a15f2489 | -11.8756 | -46.4234 | 2025-08-29 13:50:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 72.8 |
| f0e3b386-244f-3c9a-a728-e216be0d1694 | -6.7074 | -49.4561 | 2025-08-29 13:50:00 | GOES-19 | XINGUARA | PARÁ | Brasil | 1508407 | 15 | 33 | nan | nan | nan | Amazônia | 65.6 |
| fa6cf0c1-7062-3f30-b2fc-2e6a7c17cc49 | -14.3299 | -53.3108 | 2025-08-29 13:50:00 | GOES-19 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 230.3 |
| 5dd17ae6-5632-3d4d-b381-26acc1e04b51 | -10.6413 | -48.6458 | 2025-08-29 13:50:00 | GOES-19 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 81.5 |
| 0c61e11e-47d0-34bc-a045-863e9fb84d04 | -1.7507 | -54.513 | 2025-08-29 13:50:00 | GOES-19 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 77.2 |
| b1191125-fc7e-3bbd-97f6-e1a4932e74ec | -9.1339 | -65.788 | 2025-08-29 13:50:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 63.2 |
| c5d4f5f9-2b6d-33dd-b309-d1a54628a748 | -9.1338 | -65.8067 | 2025-08-29 13:50:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 117.0 |
| 9d196b05-4553-3a7f-ab84-2a9b9cfe2022 | -9.7916 | -64.2461 | 2025-08-29 13:50:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 82.3 |
| d4fd2fa2-82ca-3f75-9822-0e65069ea2de | -12.9382 | -56.9856 | 2025-08-29 13:50:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 63.3 |
| a8d6df48-46ac-3621-896d-0b7de18b2a32 | -10.4736 | -57.9563 | 2025-08-29 13:50:00 | GOES-19 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 61.0 |
| 46e6de65-1499-3484-837b-12b0ac2486ff | -6.2741 | -43.8299 | 2025-08-29 13:50:00 | GOES-19 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 90.1 |
| f1e5e1d4-d22c-3c1c-8607-f5b6e30b5f4c | -9.773 | -64.2469 | 2025-08-29 13:50:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 79.2 |
| cc798b0c-99e3-37c5-8f06-749e65170eb3 | -12.9385 | -56.9655 | 2025-08-29 13:50:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 91.5 |
| acea558e-6eca-3faa-b46e-3309df481064 | -14.0328 | -44.487 | 2025-08-29 13:50:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 175.8 |
| 0d19ba39-31e5-3acd-9c4e-2a18ad1f9182 | -10.8607 | -60.8191 | 2025-08-29 13:50:00 | GOES-19 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 73.7 |
| c8552f45-9e75-3722-ba39-60dba67741d2 | -11.3513 | -43.5897 | 2025-08-29 13:50:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 66.9 |
| 41f80193-446c-3b16-81d6-0267d0f5f506 | -7.415 | -44.283 | 2025-08-29 13:50:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 73.8 |
| 4f0fac15-c7ad-3390-abdf-0d51d2cf04b5 | -9.7728 | -64.2657 | 2025-08-29 13:50:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 68.0 |
| d290c3a3-96b2-32c1-b33c-426efd7a92ce | -6.2743 | -43.8067 | 2025-08-29 13:50:00 | GOES-19 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 87.0 |
| efc8d5f3-8978-3af3-8c18-6f8b137aaa38 | -11.876 | -46.4007 | 2025-08-29 13:50:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 112.4 |
| e76edc69-4175-36a9-a61a-62e4c40d5b3e | -14.3502 | -53.2453 | 2025-08-29 13:50:00 | GOES-19 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 76.6 |
| 0666d294-6bef-3842-b4fc-269efc22b10a | -12.8994 | -48.1381 | 2025-08-29 13:50:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 106.8 |
| 9e24b071-bc64-366f-b91d-2c1dbaecf91c | -15.1225 | -48.1302 | 2025-08-29 13:50:00 | GOES-19 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 103.9 |
| e79436ae-6ed4-3791-9136-26246f612d72 | -13.5774 | -46.8714 | 2025-08-29 13:50:00 | GOES-19 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 216.4 |
| e455b089-4ab8-34b4-bc9b-0d8806ab6a45 | -14.3106 | -53.3131 | 2025-08-29 13:50:00 | GOES-19 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 84.5 |
| b2f6d918-30c1-389d-86db-4dd0805471ae | -7.6222 | -42.6975 | 2025-08-29 13:50:00 | GOES-19 | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | 121.9 |
| 19c72120-537c-3f8e-b982-1b1c1a6dd609 | -14.3489 | -53.3294 | 2025-08-29 14:00:00 | GOES-19 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 68.7 |
| 0ffb120c-0def-3358-afbc-098457cca884 | -11.876 | -46.4007 | 2025-08-29 14:00:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 95.1 |
| 1f77f41f-db3f-3205-82d6-44bf0d739e1c | -11.3667 | -63.2853 | 2025-08-29 14:00:00 | GOES-19 | SÃO MIGUEL DO GUAPORÉ | RONDÔNIA | Brasil | 1100320 | 11 | 33 | nan | nan | nan | Amazônia | 56.0 |
| 98fc8d19-340d-3027-8b24-0e469c4de33a | -8.1964 | -45.0541 | 2025-08-29 14:00:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 110.4 |
| dd81394d-2f97-3121-8fe7-8fe9f982e582 | -14.3299 | -53.3108 | 2025-08-29 14:00:00 | GOES-19 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 210.7 |
| d12fcabe-a10a-3d1f-8a48-c3e6207b4cfa | -7.1106 | -44.6099 | 2025-08-29 14:00:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 121.9 |
| d896ef82-480a-3e8b-a41f-24f82711c7d7 | -12.0553 | -50.6425 | 2025-08-29 14:00:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 79.1 |
| 1adba2e9-15bb-3de0-99ab-a3c8338fb59e | -15.0835 | -48.1367 | 2025-08-29 14:00:00 | GOES-19 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 93.3 |
| 5b025fa6-a4d4-37da-a611-b9025615b738 | -7.9735 | -46.3854 | 2025-08-29 14:00:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 70.1 |
| 5299b4c3-2655-3b4e-ad5e-ea190498539f | -9.1154 | -65.7886 | 2025-08-29 14:00:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 73.0 |
| 24a26d14-0df2-3bd1-ad09-61daa0032946 | -7.6222 | -42.6975 | 2025-08-29 14:00:00 | GOES-19 | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | 132.3 |
| 65a92ecc-69c0-3573-a886-fd5428c8ad36 | -9.1339 | -65.788 | 2025-08-29 14:00:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 71.3 |
| 3c098173-f4c6-3d71-b7ea-7dd02d3784c0 | -11.3521 | -43.5423 | 2025-08-29 14:00:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 152.3 |
| b720f680-de10-3d1e-933d-7429e12d0be4 | -10.3812 | -57.8245 | 2025-08-29 14:00:00 | GOES-19 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 110.1 |
| ab6aa4ab-151c-3281-b715-4c3d0fa55768 | -6.3881 | -45.6018 | 2025-08-29 14:00:00 | GOES-19 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 181.9 |
| 60ce08ea-68d7-32d6-8e99-d0fbef02f542 | -12.9385 | -56.9655 | 2025-08-29 14:00:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 104.4 |
| 74a01dce-f9f8-3929-99c5-fec36260eef1 | -13.5584 | -46.8517 | 2025-08-29 14:00:00 | GOES-19 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 84.8 |
| e2b8c633-dfa9-3185-a163-00165c202d95 | -11.0826 | -44.7503 | 2025-08-29 14:00:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 114.2 |
| 92c6bc45-59ba-37eb-8adc-b0a03cf29499 | -9.7728 | -64.2657 | 2025-08-29 14:00:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 68.3 |
| 60f1e0de-90f5-393f-af91-cb1599a74ead | -13.5774 | -46.8714 | 2025-08-29 14:00:00 | GOES-19 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 248.2 |
| 4550d2c1-ad66-3770-b90a-c3c190c448f1 | -9.4432 | -60.5692 | 2025-08-29 14:00:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 116.2 |
| 968bda04-9ef4-35d9-807d-22234e1229fd | -10.66 | -48.6655 | 2025-08-29 14:00:00 | GOES-19 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 69.2 |
| f5c3ab2a-7882-30ba-bc54-6ee7bc10eb5c | -7.6219 | -42.7212 | 2025-08-29 14:00:00 | GOES-19 | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | 98.4 |
| 619105ab-cdb8-3563-910e-87a507aeb87a | -11.5714 | -46.3298 | 2025-08-29 14:00:00 | GOES-19 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 153.6 |
| 00684d2e-1d98-38a7-887f-18400a13f230 | -13.558 | -46.8745 | 2025-08-29 14:00:00 | GOES-19 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 263.1 |
| c293cbac-4707-3acc-9386-bbda867936d1 | -14.3506 | -53.2243 | 2025-08-29 14:00:00 | GOES-19 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 72.1 |
| 48581442-63b1-3dbd-8475-93510c015617 | -10.7568 | -59.798 | 2025-08-29 14:00:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 71.5 |
| fde1c93b-929d-3047-bceb-f9ee578c5f5e | -6.2743 | -43.8067 | 2025-08-29 14:00:00 | GOES-19 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 110.5 |
| f81ffc09-698a-3156-8dad-903c500ebe10 | -9.773 | -64.2469 | 2025-08-29 14:00:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 96.7 |
| a1d35049-386e-3ce5-8e82-90cc26b02c91 | -13.3559 | -51.7642 | 2025-08-29 14:00:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 51.5 |
| 15e27002-204f-39c0-88e1-b8c45ec7fd89 | -11.3325 | -43.5689 | 2025-08-29 14:00:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 119.0 |
| 50f06385-a200-321c-8df6-5bafc86fc0d2 | -10.8483 | -47.4768 | 2025-08-29 14:00:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 102.0 |
| 15d380bb-f111-3e2b-8450-d368daf25916 | -12.9382 | -56.9856 | 2025-08-29 14:00:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 74.3 |
| 8facb21f-a346-325c-bb00-bd7cde9241d0 | -12.9186 | -48.1354 | 2025-08-29 14:00:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 127.9 |
| e64dfa33-f71a-31ad-ba0e-0a14dd4733e5 | -10.3709 | -45.1686 | 2025-08-29 14:00:00 | GOES-19 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 97.0 |
| 28630f9b-f652-31c3-939b-6c37ed264f1f | -12.8801 | -48.1408 | 2025-08-29 14:00:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 81.8 |
| b09c686f-9bb1-3d47-9cbd-71974c038af7 | -13.3555 | -51.7855 | 2025-08-29 14:00:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 50.1 |
| 23ac6eb5-b723-355c-8684-fbd2239b4032 | -9.1153 | -65.8073 | 2025-08-29 14:00:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 68.2 |
| 41c9197f-2f50-3dba-bb22-b8d610cc95be | -14.0328 | -44.487 | 2025-08-29 14:00:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 435.1 |
| 937c8484-bd42-34ea-90a1-9b6faa989a42 | -13.354 | -54.4006 | 2025-08-29 14:00:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 87.3 |
| 87cc735e-7b4f-3bf6-8103-0b7a2479370d | -13.5967 | -46.8684 | 2025-08-29 14:00:00 | GOES-19 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 124.2 |
| bce0ebb8-4a6b-395b-89fb-fd6654a4109b | -6.2741 | -43.8299 | 2025-08-29 14:00:00 | GOES-19 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 115.5 |
| 35632f77-1489-3dc6-b9e0-835111d743dc | -10.8607 | -60.8191 | 2025-08-29 14:00:00 | GOES-19 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 86.1 |
| f015d35c-b917-3a34-859c-de38171b0a71 | -11.3517 | -43.566 | 2025-08-29 14:00:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 247.0 |
| 8203da0d-7270-34b8-a472-3559fe77e09e | -10.6413 | -48.6458 | 2025-08-29 14:00:00 | GOES-19 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 107.4 |
| e223262e-5815-35bf-ae5d-a241ec7c3ce7 | -12.9182 | -48.1576 | 2025-08-29 14:00:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 111.8 |
| 6444bc8b-f1bf-32ca-a951-3158f775dbeb | -14.3106 | -53.3131 | 2025-08-29 14:00:00 | GOES-19 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 109.4 |
| 07d6b86e-efb6-3555-8b6c-46101b6fc23c | -12.8994 | -48.1381 | 2025-08-29 14:00:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 96.3 |
| 5ae6d30d-8a55-320d-906c-778bb1175021 | -10.4551 | -57.9378 | 2025-08-29 14:00:00 | GOES-19 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 62.1 |
| 8e375505-272b-35d5-82cd-34a6a68531fc | -11.8756 | -46.4234 | 2025-08-29 14:00:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 82.6 |
| 8882eb9f-293b-3b62-8d1c-4d6dff3f49a7 | -14.3296 | -53.3318 | 2025-08-29 14:00:00 | GOES-19 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 233.8 |
| 530ad732-b5bf-3132-b757-2fea6cf7ecad | -12.9194 | -56.9672 | 2025-08-29 14:00:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 72.3 |
| 01b5abf8-b89e-35b8-9eae-c925b138a8a7 | -12.9318 | -46.359 | 2025-08-29 14:00:00 | GOES-19 | LAVANDEIRA | TOCANTINS | Brasil | 1712157 | 17 | 33 | nan | nan | nan | Cerrado | 89.6 |
| d8b945d3-2534-3b1d-95ea-ec824332c838 | -9.4618 | -60.5682 | 2025-08-29 14:00:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 198.0 |
| 2f8a545b-8e45-344f-b683-3e2236759e08 | -10.848 | -47.4991 | 2025-08-29 14:00:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 88.3 |
| d6025aed-bca6-3030-ab0b-6891a1eb3b7d | -10.8419 | -60.8202 | 2025-08-29 14:00:00 | GOES-19 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 62.6 |
| e60ad3c9-f256-31a6-adbc-7e93053b5b48 | -6.19 | -44.7788 | 2025-08-29 14:00:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 77.5 |
| 229d07bd-d177-3271-a7a8-06d33e1f8ab8 | -13.5576 | -46.8972 | 2025-08-29 14:00:00 | GOES-19 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 117.8 |
| bc07064c-01f3-37e4-9d7d-9f449a971c67 | -8.1775 | -45.056 | 2025-08-29 14:00:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 109.3 |
| 975b3729-2540-3a11-9f4e-59494de0f1e8 | -9.1338 | -65.8067 | 2025-08-29 14:00:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 132.7 |
| af3ef2bd-b00f-36f8-a9b3-f34259bed28e | -14.3502 | -53.2453 | 2025-08-29 14:00:00 | GOES-19 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 71.0 |
| de4b4aa1-bebe-3a22-96ee-660001b568fc | -13.3543 | -54.38 | 2025-08-29 14:00:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 83.2 |
| e74a1866-2224-3e2f-8191-ca734dadff74 | -9.1155 | -65.7699 | 2025-08-29 14:00:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 108.5 |
| 0106825d-024f-3eca-98f5-37368b080ac5 | -10.641 | -48.6677 | 2025-08-29 14:00:00 | GOES-19 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 148.3 |
| 5e27b144-a1e8-35e5-b670-bcc863b333c8 | -12.822 | -48.1712 | 2025-08-29 14:00:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 87.0 |
| 128f191d-44d2-36ca-b773-931d5f357983 | -6.8131 | -44.338 | 2025-08-29 14:00:00 | GOES-19 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 85.2 |
| cf66a595-0e73-3dcc-9076-5185509923c8 | -11.3713 | -43.5394 | 2025-08-29 14:00:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 80.2 |
| 2ee6d7b6-f954-34f7-b681-acefd53d823b | -9.7916 | -64.2461 | 2025-08-29 14:00:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 82.0 |
| 3f2fa199-9659-37fe-bd70-61d7a8476b4c | -11.3856 | -63.2653 | 2025-08-29 14:00:00 | GOES-19 | SÃO MIGUEL DO GUAPORÉ | RONDÔNIA | Brasil | 1100320 | 11 | 33 | nan | nan | nan | Amazônia | 58.8 |
| 03762f0e-3afd-3f6a-bc30-cf6392bc685d | -12.8413 | -48.1685 | 2025-08-29 14:00:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 81.4 |
| aba1bf83-5bbe-36f9-83df-b215d18c3250 | -6.4103 | -45.2387 | 2025-08-29 14:00:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 74.9 |


[Clique aqui para ver as próximas entradas](README97.md)
