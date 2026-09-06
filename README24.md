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

## Dados Diários - Página 24

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 1b8256ad-b2c8-30f2-a267-4284b141eeac | -5.15264 | -55.95923 | 2026-09-06 05:23:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| c16f31d5-91a0-37a8-a521-cd6221f69639 | -4.45302 | -46.13303 | 2026-09-06 05:23:00 | NPP-375D | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 881094cd-fba0-3c08-ba17-acb0f8a121a0 | -5.84594 | -52.03778 | 2026-09-06 05:23:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 9cbb81aa-b642-3a6e-9a2c-116e6bcf073e | -2.04204 | -56.42229 | 2026-09-06 05:23:00 | NPP-375D | TERRA SANTA | PARÁ | Brasil | 1507979 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 50ed4cb9-1807-3eb3-bb92-6cf88b5b6136 | -6.95479 | -59.74272 | 2026-09-06 05:23:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 1f61a7a1-e95d-31c7-9c5b-9e4f2d8e3be3 | -5.59909 | -60.24047 | 2026-09-06 05:23:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 539ac6ea-1fb1-325f-9bcd-5c18a4808fd5 | -3.42017 | -58.31267 | 2026-09-06 05:23:00 | NPP-375D | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 5.3 |
| a0707725-4d87-39e6-94cb-ec75f89992a7 | -3.66416 | -57.08118 | 2026-09-06 05:23:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| efbeee4a-9a75-3de8-b796-f90bcedc109c | -3.33762 | -54.17663 | 2026-09-06 05:23:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 4fd1afce-ca8b-3266-97fc-14e63c6a073a | -4.66804 | -55.63914 | 2026-09-06 05:23:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| c3d56600-3af2-3357-a03a-198a762237dd | -3.93284 | -59.34062 | 2026-09-06 05:23:00 | NPP-375D | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 19c44a0c-fd4e-3039-ae7a-29b39ffe704d | -4.11955 | -49.08372 | 2026-09-06 05:23:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 6137caaa-779a-31d3-b2cb-1740c97a6207 | -13.80388 | -51.64951 | 2026-09-06 05:23:00 | NPP-375D | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 04f5f176-97b7-3842-80d1-edc3ae093742 | -5.36234 | -56.02387 | 2026-09-06 05:23:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 9.6 |
| 1368a745-b039-3b6d-bea1-f01e289d1125 | -3.85959 | -51.03431 | 2026-09-06 05:23:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 3302f6d6-b803-3d33-ada5-a041ae444a11 | -5.28417 | -60.13348 | 2026-09-06 05:23:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 9c36955f-2007-357b-9f53-3d65ea86bb25 | -3.78319 | -59.71638 | 2026-09-06 05:23:00 | NPP-375D | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| f01e06f4-1841-33ee-8c46-5acc1bd660ef | -5.36515 | -56.02796 | 2026-09-06 05:23:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 9.6 |
| eb1181c0-83ca-3c33-8529-66ccea3c237b | -2.02603 | -52.10582 | 2026-09-06 05:23:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 4afdf629-11fd-3a5f-89c7-b75a1677fabb | -13.35527 | -61.13618 | 2026-09-06 05:23:00 | NPP-375D | CEREJEIRAS | RONDÔNIA | Brasil | 1100056 | 11 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 1ce5570d-769e-3f17-84dd-cc66d6e2a4c3 | -4.55884 | -55.03798 | 2026-09-06 05:23:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 02e4e621-78f9-3097-b4dd-b8c2ec11c8f5 | -5.34281 | -56.02845 | 2026-09-06 05:23:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| f317e10f-06b4-3fd1-9a0e-95bee739d73c | -7.097 | -56.51113 | 2026-09-06 05:23:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 393c37d7-9f9d-3897-83e1-b61a31d8172d | -5.3023 | -55.86855 | 2026-09-06 05:23:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 5741fef8-e402-38be-a372-3460a8c11cb5 | -4.87517 | -55.876 | 2026-09-06 05:23:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 6f3e1a4f-4bd7-3ce7-b8a4-33b55462d70c | -6.13213 | -57.68925 | 2026-09-06 05:23:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| d3cc877b-2dcc-327b-9d01-e6c59d30da11 | -5.6507 | -60.24054 | 2026-09-06 05:23:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 8c4bc741-0002-300c-8718-19e25b759d71 | -3.42415 | -58.30959 | 2026-09-06 05:23:00 | NPP-375D | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 4ef0b01b-0f60-3e5a-85f5-916d8571673c | -13.82563 | -51.66896 | 2026-09-06 05:23:00 | NPP-375D | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 248f29d1-6d54-3af0-8b57-c8ff2348ad91 | -3.83425 | -59.39281 | 2026-09-06 05:23:00 | NPP-375D | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 662b7152-8b8b-3c7c-b790-42d4d3f8f54b | -6.67896 | -58.75412 | 2026-09-06 05:23:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 6324dc83-4c7a-312a-b2b2-a86ba0b9241e | -5.30286 | -55.86496 | 2026-09-06 05:23:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 70c78229-5cba-30cc-af4b-70d77d706008 | -6.94786 | -59.74156 | 2026-09-06 05:23:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 617120ac-ce50-3f92-87d4-b63b099690a6 | -3.55537 | -48.18331 | 2026-09-06 05:23:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 323122d2-5d35-3af3-8ac4-f52d693f8d5d | -3.15686 | -59.14602 | 2026-09-06 05:23:00 | NPP-375D | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 27b4cc6b-e2f7-3893-bdb8-772a7de8dafb | -5.3691 | -56.0468 | 2026-09-06 05:23:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| ca1c7618-3973-321b-bdd7-df1e3a681511 | -5.17131 | -56.06022 | 2026-09-06 05:23:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 5e9fe334-1478-3f71-a57f-c30996de7723 | -5.36067 | -56.03456 | 2026-09-06 05:23:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 8eecd59b-4d0e-3de7-910f-77bf718d47f0 | -10.75618 | -60.71085 | 2026-09-06 05:23:00 | NPP-375D | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 9bb9ee40-8849-32c1-84c6-3b47f53c654f | -6.89086 | -62.96095 | 2026-09-06 05:23:00 | NPP-375D | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 67f26d63-f65f-3b78-97a8-e647275998d0 | -6.06675 | -57.80001 | 2026-09-06 05:23:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| ea5c6a2c-fdce-39c2-919f-73cceb86aa23 | -5.36293 | -56.0422 | 2026-09-06 05:23:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 0669354e-3281-3839-a847-af75c2ecd245 | -4.46768 | -55.08949 | 2026-09-06 05:23:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| a568aaef-6524-31b5-81cb-60c07e9eb87a | -5.28484 | -60.12939 | 2026-09-06 05:23:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| adef50fd-d3e0-34f7-ab6d-1fbb1af4e9a2 | -4.69115 | -56.09797 | 2026-09-06 05:23:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 632778c3-efc3-343d-8feb-03283c7dee76 | -3.17658 | -61.14212 | 2026-09-06 05:23:00 | NPP-375D | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| c82d197a-d86a-3094-b944-853c8f0494ba | -4.67198 | -55.63606 | 2026-09-06 05:23:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 5e1d1e59-b7b2-3fa3-80ae-d0672b46bf7e | -3.79018 | -55.87444 | 2026-09-06 05:23:00 | NPP-375D | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 7e36ec86-74b5-3be9-ab27-a09398677bff | -6.06342 | -57.79948 | 2026-09-06 05:23:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| dde1e0c6-5cdd-338c-a85a-03e0ee78be7e | -5.34561 | -56.03252 | 2026-09-06 05:23:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| e118caaa-dd07-3662-b7c6-d13ac11b045d | -5.15153 | -55.96635 | 2026-09-06 05:23:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 80d0d545-538e-3bcc-a949-2a3bb2d7b065 | -3.83179 | -60.76554 | 2026-09-06 05:23:00 | NPP-375D | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| a8eb4462-cecc-3f39-9578-4201508a56b3 | -5.84788 | -52.03874 | 2026-09-06 05:23:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 011ad654-9772-3013-872b-5f2970493ac3 | -7.3739 | -47.75751 | 2026-09-06 05:23:00 | NPP-375D | FILADÉLFIA | TOCANTINS | Brasil | 1707702 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 273b06bf-f4b0-3192-b4c9-3719236d30dc | -1.38991 | -55.17393 | 2026-09-06 05:23:00 | NPP-375D | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 9567e9a3-27c4-39ec-a5f3-dcd438299d37 | -5.36851 | -56.02848 | 2026-09-06 05:23:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 20.4 |
| 7d86f01e-61fc-399c-ad0b-043b8bf53a5c | -6.9507 | -59.74594 | 2026-09-06 05:23:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 780fd3fb-275a-3abb-86ce-7facf791950e | -4.6731 | -55.62892 | 2026-09-06 05:23:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 8ae5a445-cdb7-3998-9bc1-094c85f9dc83 | -15.48897 | -50.36608 | 2026-09-06 05:23:00 | NPP-375D | FAINA | GOIÁS | Brasil | 5207535 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| e9ca13fa-e205-31f2-9f7d-6b69fc6fa111 | -4.28134 | -59.96926 | 2026-09-06 05:23:00 | NPP-375D | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| ae48b853-f1f5-3193-932d-a8e65c60f672 | -13.82021 | -51.67255 | 2026-09-06 05:23:00 | NPP-375D | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 6f39d412-bf56-3f6b-8bd6-3ea68e47e2aa | -4.35326 | -56.28911 | 2026-09-06 05:23:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 28bb8bb4-2b89-3618-9ec4-de4ed9fe92b5 | -3.79578 | -55.88251 | 2026-09-06 05:23:00 | NPP-375D | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| bcb02963-b904-3d18-9b49-c004632c5650 | -3.81086 | -55.89568 | 2026-09-06 05:23:00 | NPP-375D | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 7de059cb-8e95-3d51-8e90-c1f9ea0405f2 | -5.15656 | -55.95619 | 2026-09-06 05:23:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 091f6439-d8fd-35de-b54a-328234c737aa | -3.78313 | -58.85661 | 2026-09-06 05:23:00 | NPP-375D | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 886b90be-dd3d-3bca-a953-d72c033a4b24 | -3.62857 | -54.60543 | 2026-09-06 05:23:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 56cb0bb9-2925-32d3-9290-cc7b1eead4e6 | -6.02916 | -60.16867 | 2026-09-06 05:23:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 051bf831-16ac-3488-9fed-41f70ca911e0 | -5.3545 | -56.02995 | 2026-09-06 05:23:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 2abcf869-0f46-3c5e-ac3c-d2c495fa725c | -3.78963 | -55.87795 | 2026-09-06 05:23:00 | NPP-375D | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 23ab6a4f-8b27-3c05-8f44-39bfae9636bb | -5.14646 | -55.95461 | 2026-09-06 05:23:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 299f1013-a63b-3b96-8308-eabac8db5144 | -5.30636 | -56.01912 | 2026-09-06 05:23:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 7bc3631e-13d0-3ae4-aa6e-b39c01e06b36 | -4.29484 | -59.95459 | 2026-09-06 05:23:00 | NPP-375D | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 00aaa3cd-d91f-3923-87e4-0e3a2d7b2207 | -3.55019 | -48.1825 | 2026-09-06 05:23:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 58955c07-f645-3c2f-9ca6-ee11c8e9994b | -5.13754 | -56.27552 | 2026-09-06 05:23:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 11.9 |
| f8c6f86f-5f46-336d-b87b-42d3cb03580a | -4.36205 | -47.77467 | 2026-09-06 05:23:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 2694d651-8838-3ab4-bd05-fbdc4485c383 | -7.09365 | -56.5106 | 2026-09-06 05:23:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 2cab6a3e-3b19-3f4a-8be2-7ffd2df75a35 | -3.388 | -59.41415 | 2026-09-06 05:23:00 | NPP-375D | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 8effcc29-60c8-312b-bd77-858f24e8b5fe | -14.14475 | -52.88489 | 2026-09-06 05:23:00 | NPP-375D | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 57b8894c-425b-32f8-aad5-62631f41605e | -5.37132 | -56.03256 | 2026-09-06 05:23:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 8.6 |
| bdcec240-cd97-3110-a2bb-636282c1f750 | -1.49121 | -54.81669 | 2026-09-06 05:23:00 | NPP-375D | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 9b800dff-3332-3bc9-b6e3-7fa462deb919 | -3.86018 | -51.03033 | 2026-09-06 05:23:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| ff590f21-7a85-3487-b893-66be727fe0cf | -3.22663 | -50.29586 | 2026-09-06 05:23:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 14207a1e-acec-3f7b-9a1b-80a882024300 | -7.89642 | -47.69541 | 2026-09-06 05:23:00 | NPP-375D | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 777ae249-30fd-3d5d-84e5-fb6ca631c3bf | -6.18578 | -57.75541 | 2026-09-06 05:23:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 687ea4cd-4426-34c0-9c3e-6b7e7c37e36e | -4.1097 | -49.08238 | 2026-09-06 05:23:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| a6701e7d-3537-3b1e-b3f5-e2ebbf259523 | -4.66632 | -55.62791 | 2026-09-06 05:23:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 009e02a3-4502-356d-bd80-daa4f68dfde1 | -2.86124 | -50.46159 | 2026-09-06 05:23:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| cccd396c-e02c-3e13-9c7a-b0a5af754729 | -5.36796 | -56.03204 | 2026-09-06 05:23:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 8.6 |
| 39ebf643-716c-3223-8e3b-038cd851b976 | -5.84291 | -60.25323 | 2026-09-06 05:23:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| f4d30dbf-96c0-3654-8d97-9902824bbd88 | -3.16042 | -50.82504 | 2026-09-06 05:23:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 4d10a561-c955-3444-9721-3a29ebd1ee6b | -3.11987 | -57.69495 | 2026-09-06 05:23:00 | NPP-375D | BOA VISTA DO RAMOS | AMAZONAS | Brasil | 1300680 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 47160b83-8188-3164-946a-f749ade7da29 | -1.70649 | -54.97822 | 2026-09-06 05:23:00 | NPP-375D | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| e62b16cd-6163-3dda-a1fa-74c3184c6077 | -6.90039 | -62.95492 | 2026-09-06 05:23:00 | NPP-375D | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 9.0 |
| 717d6ba0-99f8-3c5c-9590-0f4d4ca8f246 | -13.81005 | -51.67643 | 2026-09-06 05:23:00 | NPP-375D | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 2.8 |
| f60839a5-7b26-381f-9604-2fc7683f9a8d | -5.83573 | -60.25208 | 2026-09-06 05:23:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| c4c5c195-6afa-3f15-ac98-3f318211c986 | -4.41597 | -59.96507 | 2026-09-06 05:23:00 | NPP-375D | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c008931e-7c64-3094-9501-24bc7973295c | -5.14535 | -55.96173 | 2026-09-06 05:23:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| a3f0321b-a650-3692-aa2b-35f7a86beeea | -5.85036 | -52.05009 | 2026-09-06 05:23:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c345f9a9-4907-387f-bad8-4cc9868d46e8 | -5.35335 | -56.01518 | 2026-09-06 05:23:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |


[Clique aqui para ver as próximas entradas](README25.md)
