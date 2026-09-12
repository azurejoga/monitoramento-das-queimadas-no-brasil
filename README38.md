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

## Dados Diários - Página 38

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| d10b9b09-9aea-3639-b21a-452a7ac64713 | -4.86507 | -55.99956 | 2026-09-12 05:10:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| ad75eaf1-01d5-3947-b812-962339730076 | -6.10343 | -55.63353 | 2026-09-12 05:10:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 0cf75a2e-cc5e-30c7-a021-df1ad9037a1d | -9.55327 | -51.36294 | 2026-09-12 05:10:00 | NPP-375D | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 2c10c8a0-00d4-3a3f-aa43-aa1d3848d644 | -4.2817 | -46.53309 | 2026-09-12 05:10:00 | NPP-375D | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 2.5 |
| f90ef754-b42e-3cdb-ba36-1ea39f53e707 | -8.81424 | -46.91157 | 2026-09-12 05:10:00 | NPP-375D | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 783f4f8e-ddc8-3e62-9f7b-c9bc1dd240f6 | -10.56055 | -51.34761 | 2026-09-12 05:10:00 | NPP-375D | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d3a0f842-a95f-316d-916e-7234cc2f4602 | -9.7031 | -43.45906 | 2026-09-12 05:10:00 | NPP-375D | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 5d70d67f-587f-3d01-bd36-d548effe66dd | -4.45993 | -58.64019 | 2026-09-12 05:10:00 | NPP-375D | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | 3.1 |
| dce54c58-473a-3993-94ca-67c1d75cad83 | -5.80821 | -53.81031 | 2026-09-12 05:10:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 29d70bd3-e9bc-3780-9693-2527fe075f2f | -6.18278 | -57.71043 | 2026-09-12 05:10:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| c4b7eecd-d0ca-3f13-9bdb-6f99af13e028 | -5.82315 | -53.802 | 2026-09-12 05:10:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| d93dced6-f40c-3d42-a129-0f707e022a5e | -6.11244 | -55.64237 | 2026-09-12 05:10:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 0d4341b0-b25a-390b-958e-15d3f6b76e53 | -4.81731 | -55.76906 | 2026-09-12 05:10:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 03c655b6-2cb5-3390-9f88-d8a6c2a21dbe | -4.53177 | -54.96186 | 2026-09-12 05:10:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 56af0539-9adc-3541-959c-cae7a7703752 | -10.69242 | -54.16394 | 2026-09-12 05:10:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 29.3 |
| fca3fc20-1204-3395-a254-0838ebdd85bf | -10.74864 | -46.20108 | 2026-09-12 05:10:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 113786d8-fb5f-3bac-94fd-4be813cac0b5 | -6.6094 | -58.84069 | 2026-09-12 05:10:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 2439e7d2-a344-3e7a-9bf5-5bd89b39f396 | -10.63599 | -46.11988 | 2026-09-12 05:10:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| fd7cb041-6255-34b6-bd88-4671aeebbf1a | -6.10567 | -55.64126 | 2026-09-12 05:10:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 7bd9d9b1-8f73-3901-b63d-dfbeff5cec28 | -6.84787 | -55.24727 | 2026-09-12 05:10:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 43b1e496-1c6c-33ff-a8a2-4246b6cd9504 | -10.47912 | -48.64058 | 2026-09-12 05:10:00 | NPP-375D | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 417d1e8f-2dab-395b-b371-11d7b627a57d | -10.23262 | -56.26202 | 2026-09-12 05:10:00 | NPP-375D | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 6df5191d-652d-3d2a-8682-180021cb5b26 | -11.81782 | -46.36419 | 2026-09-12 05:10:00 | NPP-375D | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 1c065cf3-4362-3545-9e5e-f843fa573d06 | -6.28936 | -56.01965 | 2026-09-12 05:10:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 29b1412e-2180-3b9b-844a-4e283897de3d | -8.53385 | -54.71736 | 2026-09-12 05:10:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| cb67b235-02d2-3787-8e87-f79c9fd73065 | -5.83145 | -53.79264 | 2026-09-12 05:10:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 69b8c9e3-3ff3-3424-91d1-5b69850909d9 | -6.84474 | -55.80405 | 2026-09-12 05:10:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 7c13dffe-07c7-3be1-90f9-0e9bbd07a706 | -5.79714 | -53.81569 | 2026-09-12 05:10:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 0cfbc3d4-5fd1-3cfb-a3dc-eaf97d552c26 | -10.68515 | -54.16646 | 2026-09-12 05:10:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 5d2684c6-7f73-3cb3-930a-6dc71b7d20b3 | -6.00855 | -57.67465 | 2026-09-12 05:10:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| e8a4f556-5bae-3307-bb37-3ec4abd57cdd | -6.39277 | -55.19985 | 2026-09-12 05:10:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ce9d3ea5-ecf0-3a16-8afb-816f13964f61 | -5.09832 | -56.12459 | 2026-09-12 05:10:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 7eb667bf-5e09-319a-9848-344479eb62a2 | -8.32495 | -54.76983 | 2026-09-12 05:10:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 05260de5-28d9-3ef7-a287-3698f419562d | -10.55314 | -51.37175 | 2026-09-12 05:10:00 | NPP-375D | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 2a4a4dba-4f72-3cc3-9492-5f60dbcf6d97 | -11.3532 | -45.78813 | 2026-09-12 05:10:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 82a99047-20e0-3abe-b034-ada0ebfede81 | -6.60857 | -58.84565 | 2026-09-12 05:10:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 0dcd1835-309c-35ec-a7c3-654a61f267d3 | -9.3188 | -45.64204 | 2026-09-12 05:10:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| dc3fb8a3-0741-3432-b17d-78259fe4a820 | -2.71441 | -57.61667 | 2026-09-12 05:10:00 | NPP-375D | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 96d9a795-bde8-3327-aafe-99b5bc3bb1d7 | -9.71084 | -54.34779 | 2026-09-12 05:10:00 | NPP-375D | GUARANTÃ DO NORTE | MATO GROSSO | Brasil | 5104104 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| a4ddd2d2-34e6-3bbc-9e47-57c4f5f403ce | -6.72507 | -45.43642 | 2026-09-12 05:10:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 7.3 |
| d2aa8409-ac96-331b-acb9-7087ad41b353 | -5.97834 | -57.76388 | 2026-09-12 05:10:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| bf5cb0dd-6ed8-34a6-934f-2f0ace8b03a1 | -6.76799 | -59.43042 | 2026-09-12 05:10:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d0a08c8a-f34a-35a8-aa91-5de2da6309a5 | -10.56633 | -51.36006 | 2026-09-12 05:10:00 | NPP-375D | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 7929a92b-d736-3409-805d-8f9d96dc0f24 | -6.88841 | -55.64405 | 2026-09-12 05:10:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 0ba10a0d-2292-3026-95d9-d1e10b24f7aa | -6.84452 | -55.80719 | 2026-09-12 05:10:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| e702ccc2-8928-3cf6-8197-6203299c1e5c | -6.88388 | -55.65068 | 2026-09-12 05:10:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c952b721-2f14-3499-af13-32ce3ee1ad50 | -6.10072 | -56.46511 | 2026-09-12 05:10:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 99f65140-c64b-3a7a-9b08-e26646224766 | -6.1747 | -57.71344 | 2026-09-12 05:10:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 3bb3f99f-a18f-3950-918f-fb2cf6ab13b6 | -8.81975 | -46.90783 | 2026-09-12 05:10:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 0439f344-46df-31ee-a302-2af84cb2d897 | -6.24182 | -51.6982 | 2026-09-12 05:10:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 59968afb-1616-3d42-bdbd-f7edd256b624 | -4.45484 | -55.44028 | 2026-09-12 05:10:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f38b59be-94d1-331d-b954-e91d1d3b6147 | -10.89613 | -47.83254 | 2026-09-12 05:10:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| e25c48fe-1b32-31e1-9748-7b5550a37c2e | -9.90844 | -46.24224 | 2026-09-12 05:10:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 81c0e936-059d-38a1-a8b5-ed34c7f8cf12 | -8.82373 | -46.02657 | 2026-09-12 05:10:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 0632f898-cfd9-3c28-8249-63085c247379 | -8.11226 | -54.7891 | 2026-09-12 05:10:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ff6ba526-9e9d-3e1d-bcba-80575ed1cd9b | -9.3212 | -45.64185 | 2026-09-12 05:10:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 100f8d63-3fcd-3d69-b9d7-351039d7c564 | -4.35278 | -54.7702 | 2026-09-12 05:10:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b982ec14-34a0-37ee-a99e-21c77f947c93 | -3.81062 | -59.32132 | 2026-09-12 05:10:00 | NPP-375D | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 3123984a-e894-39ff-a642-4f984035b26c | -6.8783 | -55.64238 | 2026-09-12 05:10:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| ae345c16-578d-3a6a-b549-3e32c055dd53 | -5.76558 | -45.09155 | 2026-09-12 05:10:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 40.8 |
| 3432cd6a-5174-37b5-9534-b9218ae5eeb2 | -6.20779 | -55.27154 | 2026-09-12 05:10:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| c6743d55-9d78-3dc6-8b09-065a8f796ed4 | -9.46765 | -50.31912 | 2026-09-12 05:10:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 57cbb08f-3d55-39ec-8f73-2fe95718b990 | -6.61835 | -44.20113 | 2026-09-12 05:10:00 | NPP-375D | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 6ecb1cff-0ab6-32ef-b1fd-784bc9f47165 | -6.88004 | -55.63164 | 2026-09-12 05:10:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 1e95a5ea-947e-39c0-95c1-fb9409b95e56 | -4.72879 | -55.73254 | 2026-09-12 05:10:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 5f0d7e05-d265-3cf7-8365-36c4c5d0ab6f | -6.10682 | -55.63405 | 2026-09-12 05:10:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a5721261-269f-3041-945d-77b1ccf0ac98 | -6.84452 | -55.24673 | 2026-09-12 05:10:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 761074ee-321d-349f-840a-649ed0a91926 | -4.45269 | -50.15802 | 2026-09-12 05:10:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| eed875f8-d686-304f-bf4f-664e62e7e6b9 | -9.54346 | -45.47261 | 2026-09-12 05:10:00 | NPP-375D | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| bae3d9fb-3209-3a7a-adfb-7871a20df0c4 | -5.6133 | -44.85136 | 2026-09-12 05:10:00 | NPP-375D | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 14.5 |
| b2087577-8ca4-332f-8d2f-dd6cea32b9d5 | -6.79332 | -58.79515 | 2026-09-12 05:10:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 6.8 |
| 4345b613-5e2b-39b9-b31d-c765761a57b6 | -6.15922 | -57.71526 | 2026-09-12 05:10:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 01c5c7e0-6f91-33aa-94cf-a5b58a78f28e | -10.55254 | -45.22273 | 2026-09-12 05:10:00 | NPP-375D | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 052e873b-b9b7-3934-b633-ddfda41c7db8 | -6.84532 | -55.80043 | 2026-09-12 05:10:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 8d7ad4db-dba4-3a95-8869-34130eb2e114 | -4.52899 | -54.95775 | 2026-09-12 05:10:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| e03fc909-21d6-35b3-a791-1194e08df2fe | -6.88446 | -55.64709 | 2026-09-12 05:10:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 505949a6-ede3-3193-9b05-9d38f9eab7b4 | -6.85634 | -47.43354 | 2026-09-12 05:10:00 | NPP-375D | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 065df52b-a081-30a5-949c-59b7024353b4 | -10.55341 | -51.36974 | 2026-09-12 05:10:00 | NPP-375D | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 84a4ff7c-b8f9-3437-a455-9537f60ec2a9 | -5.97128 | -57.77359 | 2026-09-12 05:10:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 9190c1e5-d6b6-3d2c-bed1-1af8bba36414 | -5.1229 | -55.97321 | 2026-09-12 05:10:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 654e90d5-982c-3746-93b4-357f3229b57e | -4.5262 | -54.95364 | 2026-09-12 05:10:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 1fcf8451-76bd-3da9-98ea-deb5ecdf68d7 | -10.46953 | -48.64405 | 2026-09-12 05:10:00 | NPP-375D | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 481be214-d025-3ceb-aa46-882b128aab56 | -6.72554 | -45.43306 | 2026-09-12 05:10:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 7.3 |
| 3f9dff22-8971-33ce-bfdd-0cdc5288e3ea | -5.8237 | -53.79853 | 2026-09-12 05:10:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 178472d3-af6f-35a8-93e9-9289ad38215a | -8.49615 | -54.65411 | 2026-09-12 05:10:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| d3e16324-44c3-36e7-ae4c-e7fae11cc70d | -10.23761 | -56.25878 | 2026-09-12 05:10:00 | NPP-375D | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 1fc00833-f085-3db0-a346-efda64775650 | -6.11938 | -55.64685 | 2026-09-12 05:10:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 2175b114-99e9-34bd-8116-d10608c93640 | -9.70472 | -54.34321 | 2026-09-12 05:10:00 | NPP-375D | GUARANTÃ DO NORTE | MATO GROSSO | Brasil | 5104104 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| a1206596-08ee-37fe-8db5-f783837fb602 | -5.85499 | -53.87427 | 2026-09-12 05:10:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| f5a714ec-4557-3681-a919-61f34afec745 | -8.18224 | -49.03255 | 2026-09-12 05:10:00 | NPP-375D | JUARINA | TOCANTINS | Brasil | 1711803 | 17 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 108ce3c0-40da-353f-ba6f-c9357b504e0e | -6.23419 | -51.70107 | 2026-09-12 05:10:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 145b60cc-4986-3233-83e7-95db4dcf9113 | -10.90976 | -47.83922 | 2026-09-12 05:10:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 6a6a6b1f-00b1-38ac-b791-195945c4e68b | -10.55691 | -45.2153 | 2026-09-12 05:10:00 | NPP-375D | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| e1478561-d79d-3db6-85d1-864d28bc113f | -8.7084 | -49.61811 | 2026-09-12 05:10:00 | NPP-375D | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| afc2119d-3c1f-3090-9c9b-4f3b0810090b | -6.39669 | -55.19685 | 2026-09-12 05:10:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 41950540-af00-3263-9095-692d2052b673 | -6.84395 | -55.25026 | 2026-09-12 05:10:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| b57051fd-f041-3acf-8b19-c10355086bd0 | -6.06432 | -53.49411 | 2026-09-12 05:10:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 923ccb81-d1bb-3468-910a-3ce8a1048c4f | -10.54565 | -45.21357 | 2026-09-12 05:10:00 | NPP-375D | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 9f98d455-6b54-334b-b3ea-1a1f28fd8e90 | -6.22895 | -51.68824 | 2026-09-12 05:10:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 5043f70c-b6c5-312a-9051-47714d1ce7b8 | -6.61557 | -58.85198 | 2026-09-12 05:10:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 3.9 |


[Clique aqui para ver as próximas entradas](README39.md)
