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

## Dados Diários - Página 25

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 541d4014-465d-388b-918e-a0732b3149a2 | -15.42991 | -53.92185 | 2025-08-11 05:21:00 | NOAA-21 | POXORÉU | MATO GROSSO | Brasil | 5107008 | 51 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 7d174b37-d23c-3e1c-bf3f-61606f3bd95c | -15.42909 | -53.91877 | 2025-08-11 05:21:00 | NOAA-21 | POXORÉU | MATO GROSSO | Brasil | 5107008 | 51 | 33 | nan | nan | nan | Cerrado | 5.7 |
| b06c338f-0c7b-3b24-a902-bc5614a0fdd7 | -15.44182 | -53.93074 | 2025-08-11 05:21:00 | NOAA-21 | POXORÉU | MATO GROSSO | Brasil | 5107008 | 51 | 33 | nan | nan | nan | Cerrado | 27.8 |
| f789f8d6-f973-395a-8864-5ad540f456ff | -16.33538 | -54.32991 | 2025-08-11 05:21:00 | NOAA-21 | SÃO JOSÉ DO POVO | MATO GROSSO | Brasil | 5107297 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 26700a43-22bd-3f7c-983a-442cd33d540e | -15.42929 | -53.92683 | 2025-08-11 05:21:00 | NOAA-21 | POXORÉU | MATO GROSSO | Brasil | 5107008 | 51 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 248481b8-5c4f-3a94-8d34-dedfe30cbe11 | -15.44586 | -53.93641 | 2025-08-11 05:21:00 | NOAA-21 | POXORÉU | MATO GROSSO | Brasil | 5107008 | 51 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 657a423e-72b7-3324-9166-0b94fca69e57 | -15.41663 | -53.91489 | 2025-08-11 05:21:00 | NOAA-21 | POXORÉU | MATO GROSSO | Brasil | 5107008 | 51 | 33 | nan | nan | nan | Cerrado | 3.4 |
| e2b80cf2-2c12-3e89-b7a7-7795912c952b | -14.83543 | -51.22555 | 2025-08-11 05:21:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 141e344b-6883-39a0-9122-7e463dc71d62 | -13.66616 | -59.83802 | 2025-08-11 05:21:00 | NOAA-21 | COMODORO | MATO GROSSO | Brasil | 5103304 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 402da3ce-264e-3976-a026-95b0328a882e | -16.303 | -52.92037 | 2025-08-11 05:21:00 | NOAA-21 | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 8dfd43bf-3502-3ce3-a732-eebbb4de9e1a | -15.45049 | -53.93708 | 2025-08-11 05:21:00 | NOAA-21 | POXORÉU | MATO GROSSO | Brasil | 5107008 | 51 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 0db809ae-4ff9-3221-a478-0cabbaf44d83 | -10.16706 | -69.00951 | 2025-08-11 05:21:00 | NOAA-21 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 0d595691-cec4-366f-96dc-62c3c9cd0100 | -13.66283 | -59.83748 | 2025-08-11 05:21:00 | NOAA-21 | COMODORO | MATO GROSSO | Brasil | 5103304 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 9673054b-5df6-3bfd-86ee-1332c21af320 | -10.16765 | -69.00634 | 2025-08-11 05:21:00 | NOAA-21 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 0.5 |
| ee6fc398-bf6d-3c8c-816e-035f86f07929 | -16.30332 | -52.91769 | 2025-08-11 05:21:00 | NOAA-21 | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 5.9 |
| ec788b02-2e1b-3c22-b552-d119cd02d099 | -24.73746 | -50.91939 | 2025-08-11 05:23:00 | NOAA-21 | RESERVA | PARANÁ | Brasil | 4121703 | 41 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| 5b6e83c1-fe3d-384f-ba49-6e144aa273ad | -20.60344 | -48.87665 | 2025-08-11 05:23:00 | NOAA-21 | OLÍMPIA | SÃO PAULO | Brasil | 3533908 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 10389809-cf9d-3780-a98b-7f117545baeb | -9.3806 | -61.5315 | 2025-08-11 05:30:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 42.1 |
| cd221083-fa73-3c5f-bf6c-ad4dd9ebde3b | -7.0614 | -59.1972 | 2025-08-11 05:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 57.3 |
| 00ce39b7-2790-3cdf-9914-d0c88ca9db04 | -6.5856 | -44.564 | 2025-08-11 05:30:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 114.3 |
| 333d3ebb-41f4-3ae9-bc80-ddb9aff58c8e | -7.0613 | -59.2165 | 2025-08-11 05:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 52.4 |
| c03ca208-1766-350c-8d17-933ddcc3f9e4 | -15.4407 | -53.9258 | 2025-08-11 05:30:00 | GOES-19 | POXORÉU | MATO GROSSO | Brasil | 5107008 | 51 | 33 | nan | nan | nan | Cerrado | 74.8 |
| dc23e39b-8f28-3646-bffe-86ff17bd9a6b | -7.0799 | -59.1964 | 2025-08-11 05:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 63.3 |
| 22a7a3f4-7130-3b78-9b2f-eaf1050d2515 | -15.4403 | -53.9468 | 2025-08-11 05:40:00 | GOES-19 | POXORÉU | MATO GROSSO | Brasil | 5107008 | 51 | 33 | nan | nan | nan | Cerrado | 48.7 |
| ccd10046-f102-38f8-bfe1-e18620a4b3ee | -19.2766 | -49.7711 | 2025-08-11 05:40:00 | GOES-19 | GURINHATÃ | MINAS GERAIS | Brasil | 3129103 | 31 | 33 | nan | nan | nan | Cerrado | 60.2 |
| 1efbde88-44f0-36b8-b937-4b509e251fff | -15.4407 | -53.9258 | 2025-08-11 05:40:00 | GOES-19 | POXORÉU | MATO GROSSO | Brasil | 5107008 | 51 | 33 | nan | nan | nan | Cerrado | 81.8 |
| c3e148d4-5ae3-3d64-a0c9-363824001eb8 | -7.0799 | -59.1964 | 2025-08-11 05:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 64.7 |
| 1a01809f-09db-3962-aa5c-191a07bcf1cb | -6.5856 | -44.564 | 2025-08-11 05:40:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 100.3 |
| 53f3aac9-b23c-3cc7-ada4-13863451a9c9 | -7.0614 | -59.1972 | 2025-08-11 05:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 56.9 |
| 66b59d3e-25a9-3b4b-a82b-306c85154d79 | -7.4752 | -43.9536 | 2025-08-11 05:40:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 62.1 |
| 8e7481da-3f86-3543-92a0-98aa9129bb3d | -7.0589 | -59.20034 | 2025-08-11 05:44:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 09b62b92-c9da-399e-83bd-ebe551f36e47 | -7.08132 | -59.19913 | 2025-08-11 05:44:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 9c750560-5ab7-326e-af94-bab665593ab2 | -8.56563 | -54.67585 | 2025-08-11 05:44:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| cf112244-1293-34f9-bdbc-23ac684373a4 | -9.38091 | -61.53138 | 2025-08-11 05:44:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 8.6 |
| 784362ee-eeb7-3699-86c6-431edf441807 | -7.07219 | -59.16965 | 2025-08-11 05:44:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| c4bd0a23-1f6d-3b43-a488-6e5fddd094de | -8.55843 | -54.67832 | 2025-08-11 05:44:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 45c39c45-090e-3972-8cd4-6ad8dceb69ac | -7.08568 | -59.19976 | 2025-08-11 05:44:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 8fa4bb16-c7db-37a4-a67e-3ecd53a78471 | -7.07754 | -59.19438 | 2025-08-11 05:44:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 1c3713c1-f221-3584-be43-e23ab2b8d46b | -5.34665 | -55.90576 | 2025-08-11 05:44:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| c8ebbb16-f24c-3357-a640-aedab922b89d | -7.07082 | -59.21043 | 2025-08-11 05:44:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 8.2 |
| 4278b687-6cc1-3520-a078-18e7ea3cd3be | -8.55957 | -54.67509 | 2025-08-11 05:44:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| fda78ed0-7081-31de-8772-b32580236834 | -9.36931 | -61.52964 | 2025-08-11 05:44:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 1d88e8ab-2573-33e4-98db-c2fd63324c74 | -7.06657 | -59.17746 | 2025-08-11 05:44:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| a1587b71-e71d-30b8-8f8d-6e3f9648335f | -7.07376 | -59.18961 | 2025-08-11 05:44:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c8d70fc0-4993-31a5-86ac-6b1d47eec7e5 | -7.06646 | -59.20984 | 2025-08-11 05:44:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 8.2 |
| 482f1c7e-7442-3130-a287-4622f9690c14 | -8.57109 | -54.68129 | 2025-08-11 05:44:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 830bb4a6-fdfb-3b18-ab32-ef0d25bf010a | -7.07058 | -59.18052 | 2025-08-11 05:44:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| a21514b0-25b2-3082-bfd9-c137a5e84e2c | -8.93842 | -60.73509 | 2025-08-11 05:44:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 7341cfef-0771-3f41-aa91-8465301e3dcb | -7.07342 | -59.19142 | 2025-08-11 05:44:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 55651d75-6903-3cbf-a399-0a2b18564591 | -7.05948 | -59.19619 | 2025-08-11 05:44:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f15dad9f-b28a-3ef7-a643-74ad8135a3de | -7.05847 | -59.2021 | 2025-08-11 05:44:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 01a6c914-8878-34e9-95e8-8af1d868b48a | -7.0956 | -59.19267 | 2025-08-11 05:44:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| ef9ce43a-50f7-3232-9531-7c58896e6d11 | -7.06939 | -59.18899 | 2025-08-11 05:44:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 58f904fa-4f60-3236-99d8-6620b171d39c | -7.07258 | -59.198 | 2025-08-11 05:44:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 889c2cac-48b2-38ae-9fcd-28e130a16cea | -7.07435 | -59.18539 | 2025-08-11 05:44:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 0e72497e-19d5-34ce-bd6a-a636e1c8a8fe | -7.06742 | -59.1713 | 2025-08-11 05:44:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 73a13fbd-0b90-3e45-b82d-c116f18a4f83 | -8.56327 | -54.69425 | 2025-08-11 05:44:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 845806ad-6a52-3d10-bfe0-f2d1b97bd660 | -9.74145 | -63.19545 | 2025-08-11 05:44:00 | NPP-375D | ALTO PARAÍSO | RONDÔNIA | Brasil | 1100403 | 11 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 4319a92e-c372-3522-9252-a6b90d1f4c36 | -7.07519 | -59.21104 | 2025-08-11 05:44:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| bcbfee7d-6a2d-3fcc-acfe-e9cec26994bb | -7.07118 | -59.17626 | 2025-08-11 05:44:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| a5deb150-b38f-30b3-a22e-c5e919a80a99 | -7.07033 | -59.21217 | 2025-08-11 05:44:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 6.5 |
| fb1c5a58-ef34-3370-beba-b610fb68e5cf | -7.07156 | -59.1739 | 2025-08-11 05:44:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b8b1da6f-ab4a-33f5-8451-9ca590b83276 | -6.10501 | -59.92579 | 2025-08-11 05:44:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| ccc87155-3996-3130-96dc-e68b676080dd | -9.56549 | -62.7248 | 2025-08-11 05:44:00 | NPP-375D | RIO CRESPO | RONDÔNIA | Brasil | 1100262 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 22c90ab5-25e2-30f3-b8be-9a275d06fa32 | -6.08936 | -59.92789 | 2025-08-11 05:44:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| eb128828-9753-3c31-930d-1ae73f82db11 | -6.10162 | -59.92979 | 2025-08-11 05:44:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c254c5d6-a586-36c6-8681-0c604e0dce9c | -7.06209 | -59.20925 | 2025-08-11 05:44:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 4bf9865e-9c0a-3c09-8bf8-71c73a90219d | -9.7379 | -63.19493 | 2025-08-11 05:44:00 | NPP-375D | ALTO PARAÍSO | RONDÔNIA | Brasil | 1100403 | 11 | 33 | nan | nan | nan | Amazônia | 0.7 |
| faaed208-4282-3151-9bd9-22ec5d5e726f | -8.99196 | -68.4599 | 2025-08-11 05:44:00 | NPP-375D | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 7bc0acbc-e986-3d94-9696-d686575dfea1 | -8.93032 | -60.73393 | 2025-08-11 05:44:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 537afc3f-bd1f-37f7-957d-80a903b15a6d | -7.07141 | -59.20629 | 2025-08-11 05:44:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 8.2 |
| 060cac09-0dc8-3878-9eca-11472474bee3 | -8.57168 | -54.67666 | 2025-08-11 05:44:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 240e23c5-ede9-3d19-8ba7-725da6f51c45 | -8.93083 | -60.73038 | 2025-08-11 05:44:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 99733926-05d9-329d-bcfe-2d378496daf4 | -7.07577 | -59.20688 | 2025-08-11 05:44:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| cab62880-4504-337c-b9eb-27d69c355bb3 | -8.57478 | -54.70037 | 2025-08-11 05:44:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 8aa8287d-9d33-37bd-9b10-0d751317f60c | -6.10041 | -59.92873 | 2025-08-11 05:44:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 9546c037-4dd7-39d5-a239-3cd308a27b09 | -8.57419 | -54.70494 | 2025-08-11 05:44:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| ce907739-048a-318e-bc57-8199b65f2f2d | -9.37388 | -61.52539 | 2025-08-11 05:44:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| dfa355e7-51b5-3eeb-ac89-dbf0cb40d7ba | -7.06125 | -59.1835 | 2025-08-11 05:44:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 08ec0d0f-a7cc-3b75-9cfa-94aee0472dde | -7.06094 | -59.18541 | 2025-08-11 05:44:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 196ab1c9-2d91-3f41-954e-b136be9f33b4 | -8.56872 | -54.69968 | 2025-08-11 05:44:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| a2c32d15-377e-3d0f-bcbb-46b59c4995e5 | -7.05832 | -59.20446 | 2025-08-11 05:44:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 4d82230d-b502-3107-9a99-a7f74cccf052 | -8.55904 | -54.67373 | 2025-08-11 05:44:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 9db40c0e-1dc9-3135-a412-874bcc2b7778 | -7.0778 | -59.16193 | 2025-08-11 05:44:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 71c600b0-2f2a-3860-a1b5-8d5d00ecdcb3 | -7.06704 | -59.2057 | 2025-08-11 05:44:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 8.2 |
| fe6c8b0d-6459-3eb9-b86c-d917f5f880b0 | -7.04788 | -59.18332 | 2025-08-11 05:44:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 41e50c43-cf78-3bcd-b9ff-c2e6ca504717 | -6.10093 | -59.92512 | 2025-08-11 05:44:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 1b469814-f213-3d3d-a0a9-1bda93eef14f | -7.06846 | -59.16475 | 2025-08-11 05:44:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 045cec5f-1fd4-3b28-82c3-f59df4d0b640 | -9.3802 | -61.53622 | 2025-08-11 05:44:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 8.6 |
| 387935df-ead8-325f-bc24-fa31813da5a1 | -7.05223 | -59.18406 | 2025-08-11 05:44:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 180b7bc5-e0dd-3dde-80fb-167426d0ffce | -7.07199 | -59.20214 | 2025-08-11 05:44:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 08995652-7085-3067-9fce-1df5ccfc6264 | -7.06325 | -59.20099 | 2025-08-11 05:44:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 4f72834a-49f6-3a47-ad13-fb5cff94cb00 | -7.07931 | -59.18182 | 2025-08-11 05:44:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 2dcc639e-935c-36e3-975f-8d975998bfdc | -7.05908 | -59.19798 | 2025-08-11 05:44:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| ed9f3bdf-521b-3d38-aa10-1a471fa8603e | -7.07655 | -59.17038 | 2025-08-11 05:44:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| f665ff50-dcb0-38c0-9999-0b365b2b5361 | -7.06531 | -59.18602 | 2025-08-11 05:44:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 95f63fd6-4897-3812-881d-fd09b56b2d83 | -7.05473 | -59.19732 | 2025-08-11 05:44:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 0a6deaee-51bc-3dd2-a289-24fc77f73dcc | -7.06719 | -59.20333 | 2025-08-11 05:44:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 7.9 |
| 807f814f-6b4c-36ed-bf49-b236c940701c | -7.0811 | -59.16919 | 2025-08-11 05:44:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b0566c79-0e0b-3b33-ae06-40308f9bb5a7 | -8.56211 | -54.70335 | 2025-08-11 05:44:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |


[Clique aqui para ver as próximas entradas](README26.md)
