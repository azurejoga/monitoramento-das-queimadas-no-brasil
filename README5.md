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
| f4d25a89-1963-3ec9-b924-89e20340e7e2 | 0.9645 | -60.53026 | 2025-03-01 05:20:00 | NOAA-20 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 448f3f61-7c4a-3932-81f1-f00f3f2c1500 | -2.71586 | -54.61536 | 2025-03-01 05:20:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 59bba3fc-3c00-3040-aeed-b3fa544b52c9 | 0.9707 | -60.5256 | 2025-03-01 05:20:00 | NOAA-20 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 2.7 |
| a68045e9-8a3f-3db9-8170-6a7ed28d1f3d | 0.95773 | -60.53131 | 2025-03-01 05:20:00 | NOAA-20 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 9036f244-ec6a-321e-aba5-c4ec23e7d6c1 | 2.82537 | -60.82054 | 2025-03-01 05:20:00 | NOAA-20 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 8e347d80-072c-34d3-ac07-1dbd15902d5c | 2.15054 | -61.83876 | 2025-03-01 05:20:00 | NOAA-20 | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b55d2f17-25f3-3042-85d0-af8df7654941 | 1.31336 | -60.06998 | 2025-03-01 05:20:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 9f86d7de-8fc3-3213-88f3-ce90aed2fdc9 | 2.82766 | -60.81235 | 2025-03-01 05:20:00 | NOAA-20 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 59916880-faec-3241-b851-0add4a840496 | 1.94148 | -60.38831 | 2025-03-01 05:20:00 | NOAA-20 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 41303b64-0474-30d1-b158-242215c2db2f | 0.74264 | -60.54602 | 2025-03-01 05:20:00 | NOAA-20 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 0.8 |
| c9c37617-0a37-3783-a6bd-a9a893b82ada | 2.22504 | -61.34179 | 2025-03-01 05:20:00 | NOAA-20 | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 2750faab-4a49-376f-a6ff-64f3ece1b911 | -2.71181 | -54.61476 | 2025-03-01 05:20:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| d3f2ff73-39ce-3a1e-865b-e89357abd7a7 | 2.18505 | -61.84626 | 2025-03-01 05:20:00 | NOAA-20 | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 6ea0178a-62c4-3983-aac4-f56b7a6e74cc | 0.70754 | -59.4362 | 2025-03-01 05:20:00 | NOAA-20 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b6b4f4aa-2f72-396a-b6fb-fe09779d413f | 2.22534 | -61.34239 | 2025-03-01 05:20:00 | NOAA-20 | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 9a5850fd-857d-3189-881c-c49158e52cf5 | -23.78124 | -55.15431 | 2025-03-01 05:25:00 | NOAA-20 | SETE QUEDAS | MATO GROSSO DO SUL | Brasil | 5007703 | 50 | 33 | nan | nan | nan | Mata Atlântica | 2.7 |
| 0d1b4533-bc61-36c5-b819-64c951aca111 | -23.78125 | -55.15398 | 2025-03-01 05:25:00 | NOAA-20 | SETE QUEDAS | MATO GROSSO DO SUL | Brasil | 5007703 | 50 | 33 | nan | nan | nan | Mata Atlântica | 2.8 |
| 90cfacdc-998c-36e7-8718-d655250c38c9 | -20.87706 | -54.78261 | 2025-03-01 05:25:00 | NOAA-20 | SIDROLÂNDIA | MATO GROSSO DO SUL | Brasil | 5007901 | 50 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 5030f25d-04bc-3c88-902f-1b89d16b6ba2 | -23.78094 | -55.15744 | 2025-03-01 05:25:00 | NOAA-20 | SETE QUEDAS | MATO GROSSO DO SUL | Brasil | 5007703 | 50 | 33 | nan | nan | nan | Mata Atlântica | 2.8 |
| 546a78f1-02b5-3e1e-a09b-c76c6d4c6a68 | -23.7809 | -55.15776 | 2025-03-01 05:25:00 | NOAA-20 | SETE QUEDAS | MATO GROSSO DO SUL | Brasil | 5007703 | 50 | 33 | nan | nan | nan | Mata Atlântica | 2.7 |
| 94d48c7e-864b-378e-94d3-2c4ffa0a235a | -20.88191 | -54.78643 | 2025-03-01 05:25:00 | NOAA-20 | SIDROLÂNDIA | MATO GROSSO DO SUL | Brasil | 5007901 | 50 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 3efdd5ed-ff09-377a-a278-74e4ac4d3f4a | -20.87458 | -54.77784 | 2025-03-01 05:46:00 | AQUA_M-M | SIDROLÂNDIA | MATO GROSSO DO SUL | Brasil | 5007901 | 50 | 33 | nan | nan | nan | Cerrado | 5.9 |
| c98b8a8f-e9b8-396e-9d98-14ff68978259 | -22.71297 | -47.11524 | 2025-03-01 05:46:00 | AQUA_M-M | PAULÍNIA | SÃO PAULO | Brasil | 3536505 | 35 | 33 | nan | nan | nan | Cerrado | 11.1 |
| e8cef013-f39f-3b91-9c05-6071a10b31f4 | 4.33884 | -60.35641 | 2025-03-01 06:09:00 | NOAA-21 | UIRAMUTÃ | RORAIMA | Brasil | 1400704 | 14 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a7b060d6-bfbc-3af5-82e1-3cb02f25f48c | 2.82677 | -60.81424 | 2025-03-01 06:09:00 | NOAA-21 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 29e8baf0-65b8-35fb-b1c7-251ffa66dbe9 | 4.33941 | -60.35974 | 2025-03-01 06:09:00 | NOAA-21 | UIRAMUTÃ | RORAIMA | Brasil | 1400704 | 14 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 478f0a5d-b6fa-3cda-b40e-ce1d2baef51f | 2.10849 | -61.82454 | 2025-03-01 06:12:00 | NOAA-21 | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 54442a7f-171e-3b3e-b0fe-516507ddf6d0 | 2.10733 | -61.81745 | 2025-03-01 06:12:00 | NOAA-21 | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 3.4 |
| ba54eadd-7abd-3289-8dfa-39653c72ff7f | 2.1828 | -61.85909 | 2025-03-01 06:12:00 | NOAA-21 | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 3.3 |
| d85966b0-a334-3285-91b3-ea9d826684b1 | 0.97021 | -60.52909 | 2025-03-01 06:12:00 | NOAA-21 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 6.4 |
| 9163ca87-36cc-369a-9198-8d37e2c709b7 | 0.9695 | -60.52456 | 2025-03-01 06:12:00 | NOAA-21 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 6.4 |
| 55070f89-7ca8-3718-8f67-30e214e029e8 | 0.96418 | -60.53019 | 2025-03-01 06:12:00 | NOAA-21 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 6.4 |
| 7f554a18-0dfe-3dad-b5dd-42a1fcdef2f8 | 2.11397 | -61.82377 | 2025-03-01 06:12:00 | NOAA-21 | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 4.1 |
| dc61b3b0-28ed-306f-b685-63d5d2b3735e | 0.97107 | -60.52557 | 2025-03-01 06:12:00 | NOAA-21 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 4f75e675-e757-344f-a8f1-f966ddde3f29 | 2.11222 | -61.81297 | 2025-03-01 06:12:00 | NOAA-21 | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 9285c84b-5e11-30c0-96be-de248aa195a7 | 2.10791 | -61.82095 | 2025-03-01 06:12:00 | NOAA-21 | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 6cb5c67a-d94e-37d0-87ac-b2ea1c3368ca | 0.95743 | -60.52669 | 2025-03-01 06:12:00 | NOAA-21 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 752f192d-b42a-386a-b464-659d1c7d19cd | 2.18104 | -61.84843 | 2025-03-01 06:12:00 | NOAA-21 | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 2.2 |
| eaf9f848-8a43-360f-b2f7-7a21146a4af4 | 2.11338 | -61.82015 | 2025-03-01 06:12:00 | NOAA-21 | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 28dda659-0d86-3a94-9bef-0f3b8e03d8a7 | 0.96489 | -60.53468 | 2025-03-01 06:12:00 | NOAA-21 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 6.8 |
| 0d081e6a-5133-38dd-a421-886d9cec424b | 2.19306 | -61.85352 | 2025-03-01 06:12:00 | NOAA-21 | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 0ab8eb3b-77ee-3fd3-82a4-67c269f5e260 | 2.18221 | -61.85553 | 2025-03-01 06:12:00 | NOAA-21 | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 6666b6ae-3fb8-3e30-8bf6-7b579364f920 | 1.07209 | -59.23434 | 2025-03-01 06:12:00 | NOAA-21 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 1.9 |
| cc89b909-4039-3484-a2db-8cbe4536831a | 2.18163 | -61.85198 | 2025-03-01 06:12:00 | NOAA-21 | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 2.2 |
| b2e5eae0-fc73-3e5b-9633-e0fa5e4fc52f | 2.18822 | -61.85806 | 2025-03-01 06:12:00 | NOAA-21 | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 3.3 |
| b6a568ee-2382-3326-98a2-645dabcdf69c | 2.02329 | -61.40751 | 2025-03-01 06:12:00 | NOAA-21 | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 7b40ebfe-096b-34e4-b696-d9b0ac585576 | 2.02893 | -61.40672 | 2025-03-01 06:12:00 | NOAA-21 | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 5.9 |
| be3dd02d-482a-393a-8d3b-a7b742240a3c | 0.96347 | -60.52567 | 2025-03-01 06:12:00 | NOAA-21 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 6.4 |
| 8f9ab4df-1309-3bb1-b67a-50dd1dcb706a | 2.18704 | -61.85094 | 2025-03-01 06:12:00 | NOAA-21 | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 2.2 |
| a321f2ac-c95b-3ab8-83fa-3f9619a92396 | 0.95815 | -60.53123 | 2025-03-01 06:12:00 | NOAA-21 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 676e5b57-089e-3256-bce4-fa01eb21f15f | 2.10677 | -61.81399 | 2025-03-01 06:12:00 | NOAA-21 | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 6.3 |
| c051cf7e-8242-3b99-a95c-1b08b270e72a | 2.11456 | -61.82743 | 2025-03-01 06:12:00 | NOAA-21 | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 4.1 |
| cc7881c2-94a2-3aed-ad73-09b34dc3366d | 2.18763 | -61.8545 | 2025-03-01 06:12:00 | NOAA-21 | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 7b58c3a5-c89e-302b-b4b1-059643775d63 | 2.18646 | -61.8474 | 2025-03-01 06:12:00 | NOAA-21 | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 93f1b4c5-da1a-3d4d-884f-3056b84bcbfd | 0.97182 | -60.53009 | 2025-03-01 06:12:00 | NOAA-21 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 3.5 |
| aba88f84-0548-3f27-95e7-e140fa162f92 | -9.33372 | -38.37913 | 2025-03-01 11:59:00 | TERRA_M-M | GLÓRIA | BAHIA | Brasil | 2911402 | 29 | 33 | nan | nan | nan | Caatinga | 15.5 |
| f256bfdf-6f8e-326b-8ccc-245ba2af79b7 | -8.24714 | -37.59299 | 2025-03-01 11:59:00 | TERRA_M-M | CUSTÓDIA | PERNAMBUCO | Brasil | 2605103 | 26 | 33 | nan | nan | nan | Caatinga | 11.9 |
| b54c1698-1ae2-3e00-a122-54a4aa52b417 | -9.57136 | -36.89492 | 2025-03-01 11:59:00 | TERRA_M-M | MAJOR ISIDORO | ALAGOAS | Brasil | 2704401 | 27 | 33 | nan | nan | nan | Caatinga | 40.6 |
| 3a7774ca-3c10-3808-8e25-3ff2b1b2bf5c | -7.93738 | -38.46994 | 2025-03-01 11:59:00 | TERRA_M-M | SERRA TALHADA | PERNAMBUCO | Brasil | 2613909 | 26 | 33 | nan | nan | nan | Caatinga | 6.5 |
| 0b88b69f-cde2-3ee7-a732-bf25ef23537e | -13.79829 | -41.71704 | 2025-03-01 12:01:00 | TERRA_M-T | DOM BASÍLIO | BAHIA | Brasil | 2910107 | 29 | 33 | nan | nan | nan | Caatinga | 9.4 |
| c6dd0a5c-8cc2-3398-b29b-eb65e60f2397 | -11.79396 | -42.60569 | 2025-03-01 12:01:00 | TERRA_M-T | IPUPIARA | BAHIA | Brasil | 2914109 | 29 | 33 | nan | nan | nan | Caatinga | 30.0 |
| 1974ccb7-0723-3065-a5eb-28ebe1402c77 | -13.79979 | -41.70718 | 2025-03-01 12:01:00 | TERRA_M-T | DOM BASÍLIO | BAHIA | Brasil | 2910107 | 29 | 33 | nan | nan | nan | Caatinga | 9.4 |
| 68f8f3ed-dfc6-3790-9ca0-3565a2e53db3 | -22.76333 | -43.65707 | 2025-03-01 12:04:00 | TERRA_M-T | SEROPÉDICA | RIO DE JANEIRO | Brasil | 3305554 | 33 | 33 | nan | nan | nan | Mata Atlântica | 6.9 |
| c8327f59-b4d2-3dc2-9c51-bd8ab53a7b5c | -22.97369 | -43.61245 | 2025-03-01 12:04:00 | TERRA_M-T | RIO DE JANEIRO | RIO DE JANEIRO | Brasil | 3304557 | 33 | 33 | nan | nan | nan | Mata Atlântica | 7.9 |
| f3b17005-9cf4-3e16-a102-a9d996ecb7b1 | -20.8766 | -54.7742 | 2025-03-01 13:20:00 | GOES-16 | SIDROLÂNDIA | MATO GROSSO DO SUL | Brasil | 5007901 | 50 | 33 | nan | nan | nan | Cerrado | 69.6 |
| 3289a0c2-9833-3e94-b3b4-4e66c3666df2 | -20.8766 | -54.7742 | 2025-03-01 13:30:00 | GOES-16 | SIDROLÂNDIA | MATO GROSSO DO SUL | Brasil | 5007901 | 50 | 33 | nan | nan | nan | Cerrado | 78.4 |
| 83ecb193-ae59-30dc-ac2c-1c7bc2e63e02 | 3.7882 | -59.858 | 2025-03-01 13:30:00 | GOES-16 | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 65.6 |
| a49276a1-7974-3a5b-ae42-ae993d305561 | 3.8065 | -59.8576 | 2025-03-01 13:30:00 | GOES-16 | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 66.8 |
| 345aed31-7cb4-331d-a196-3cf064339f1b | -20.8766 | -54.7742 | 2025-03-01 13:40:00 | GOES-16 | SIDROLÂNDIA | MATO GROSSO DO SUL | Brasil | 5007901 | 50 | 33 | nan | nan | nan | Cerrado | 75.2 |
| 43c5d8ce-a35f-3234-86dd-4814b3720a12 | -20.8766 | -54.7742 | 2025-03-01 13:50:00 | GOES-16 | SIDROLÂNDIA | MATO GROSSO DO SUL | Brasil | 5007901 | 50 | 33 | nan | nan | nan | Cerrado | 89.1 |
| 87384da9-dbc3-388f-9068-123d6229f35b | -20.8766 | -54.7742 | 2025-03-01 14:00:00 | GOES-16 | SIDROLÂNDIA | MATO GROSSO DO SUL | Brasil | 5007901 | 50 | 33 | nan | nan | nan | Cerrado | 74.9 |


