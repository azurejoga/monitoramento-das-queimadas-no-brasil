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

## Dados Diários - Página 35

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 31268143-cfe9-3fe3-abad-14c036994696 | -11.57294 | -47.02672 | 2025-10-02 04:02:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 88f48654-09af-3b8e-9253-6f407cdb6baf | -12.63917 | -46.95597 | 2025-10-02 04:02:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 14.1 |
| 08f8ad4d-831c-3cc1-a0c6-3490183ded1d | -11.57708 | -50.17095 | 2025-10-02 04:02:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 0eac5ae8-72e4-3199-9432-022998a770c9 | -9.94875 | -43.68315 | 2025-10-02 04:02:00 | NOAA-21 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| dee1ffc1-3b30-3a4d-95e2-ee16591b3964 | -12.85607 | -46.86586 | 2025-10-02 04:02:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 246792da-881b-33ef-b876-3d20c8711fc2 | -11.6206 | -45.05956 | 2025-10-02 04:02:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 3b40473a-a31e-3f19-8fbd-7d407223a177 | -12.14874 | -46.67133 | 2025-10-02 04:02:00 | NOAA-21 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| fda8f2cf-2ec8-3160-9a38-e33ab9b10c7d | -9.93808 | -43.7485 | 2025-10-02 04:02:00 | NOAA-21 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 6.3 |
| b693c8c4-2447-3dd2-b01f-22ab35bc884a | -11.76873 | -46.83036 | 2025-10-02 04:02:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 48ad844b-95d2-3c22-be62-3aa1d728a249 | -9.33352 | -45.71132 | 2025-10-02 04:02:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 3.1 |
| deee7543-1979-3a80-a2bf-0a680db34048 | -11.82055 | -47.68609 | 2025-10-02 04:02:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| ddefea9e-3e40-3f0d-acfe-e354c3b72e4a | -11.82776 | -44.98953 | 2025-10-02 04:02:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 9ce8a98b-4428-3a48-9ead-f0dc6f157636 | -12.80721 | -46.90355 | 2025-10-02 04:02:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 13874407-69a9-3c0c-b798-4aa4e5729698 | -6.69095 | -42.81831 | 2025-10-02 04:02:00 | NOAA-21 | FRANCISCO AYRES | PIAUÍ | Brasil | 2204105 | 22 | 33 | nan | nan | nan | Caatinga | 18.8 |
| 00176969-774f-3781-a228-4227e3c74b45 | -5.88956 | -43.20064 | 2025-10-02 04:02:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Caatinga | 4.2 |
| 56f4789e-a997-37fb-95da-e5252b8e43af | -10.64813 | -48.50849 | 2025-10-02 04:02:00 | NOAA-21 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| a8d03be2-d8f4-33ac-86d5-0f28c7e67236 | -11.59049 | -47.65382 | 2025-10-02 04:02:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 65efed3a-c2f1-3606-9afd-49b5887ff4bb | -6.96438 | -45.34121 | 2025-10-02 04:02:00 | NOAA-21 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 7c95b61a-6f9a-3153-a27d-7219ab135dca | -10.78365 | -45.35221 | 2025-10-02 04:02:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 82885d7d-207f-3a0d-ba02-79958a98c33f | -12.24367 | -47.82926 | 2025-10-02 04:02:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 1297aed4-4600-3412-abbb-1a1912631bc2 | -8.82355 | -44.80015 | 2025-10-02 04:02:00 | NOAA-21 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 746c7724-8c1e-3f0a-86a9-87555ad7856c | -11.81472 | -45.00765 | 2025-10-02 04:02:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 1c3d0f44-1932-3e04-94b4-52e59d44a5f4 | -11.0028 | -46.54546 | 2025-10-02 04:02:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 92ed9d2a-4954-39e6-ae36-ff5b7da1700a | -8.89584 | -46.60748 | 2025-10-02 04:02:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| ca9d8089-a420-31e3-903b-1a46b0cb497f | -6.69757 | -48.69889 | 2025-10-02 04:02:00 | NOAA-21 | ARAGOMINAS | TOCANTINS | Brasil | 1701309 | 17 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 5c01cfa0-4bc1-37bb-b3c3-12c2239e7287 | -12.21409 | -47.79277 | 2025-10-02 04:02:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 45da4249-6230-3fee-a0e2-35498c6434fe | -6.64343 | -42.08668 | 2025-10-02 04:02:00 | NOAA-21 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 0d1fafb1-572c-3cf2-b66a-aff8ce8d2cb6 | -10.83458 | -46.64225 | 2025-10-02 04:02:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 593f6124-2680-39a8-a499-e29a72f00f77 | -9.94919 | -43.72514 | 2025-10-02 04:02:00 | NOAA-21 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 3.6 |
| b8211470-666f-325c-a898-503c191d1c5e | -11.17523 | -47.28334 | 2025-10-02 04:02:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 48.1 |
| b4bae48c-d42d-38e3-92f6-759685121dba | -11.27144 | -47.81482 | 2025-10-02 04:02:00 | NOAA-21 | SANTA ROSA DO TOCANTINS | TOCANTINS | Brasil | 1718907 | 17 | 33 | nan | nan | nan | Cerrado | 6.7 |
| ce3b3be5-ad64-342c-b3ee-c699637cb6a0 | -12.28291 | -45.3724 | 2025-10-02 04:02:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 0ccf8e2d-1ca2-3742-9304-f53dfe3c9333 | -11.44206 | -44.96255 | 2025-10-02 04:02:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 2b3c90a1-c464-3841-92d0-9e76f58b02eb | -6.11234 | -43.12236 | 2025-10-02 04:02:00 | NOAA-21 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 5.4 |
| dbfdd028-54dd-3a04-b266-1f602d2287a8 | -11.82624 | -44.99836 | 2025-10-02 04:02:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 3.5 |
| bc154f8c-494e-3103-b4f4-3b8f6339a8dd | -7.72164 | -46.22623 | 2025-10-02 04:02:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| cb8b8a00-70ff-352a-a155-e4d5392a3b0c | -7.79338 | -42.51652 | 2025-10-02 04:02:00 | NOAA-21 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 13.3 |
| 763701cd-bd75-329c-9599-18ac37a00274 | -9.93077 | -43.72623 | 2025-10-02 04:02:00 | NOAA-21 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 31.3 |
| 5675e1a1-c0e1-33b9-a5b8-f8f4d9684a93 | -7.60277 | -45.40509 | 2025-10-02 04:02:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| f3c559ab-c5bd-3e52-8b34-93293c8d1035 | -9.93963 | -43.76136 | 2025-10-02 04:02:00 | NOAA-21 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 5.7 |
| c5d88dea-2de5-3b55-a0d6-be351ed95e15 | -11.80735 | -47.58517 | 2025-10-02 04:02:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 4cbb9d45-5876-3b19-926a-8dedf3c9dfe4 | -12.12302 | -43.43075 | 2025-10-02 04:02:00 | NOAA-21 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 52779ce1-d825-32b2-b4c5-9a7e5be23f90 | -10.24259 | -50.31715 | 2025-10-02 04:02:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 24.5 |
| a12e41c1-a396-3963-b515-e3ff1a018540 | -11.79632 | -44.98101 | 2025-10-02 04:02:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 94f1fd8c-4a5f-385b-89ca-b6a95dc29dea | -6.77874 | -45.578 | 2025-10-02 04:02:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| ac59da16-b8af-3166-9cd0-db9cc84153b7 | -12.86328 | -47.01675 | 2025-10-02 04:02:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| d53895fa-be20-3c9e-b8ba-77273ee92dda | -10.81843 | -46.58801 | 2025-10-02 04:02:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 706ab4d4-91be-3a77-9f74-06b927b4c6f4 | -10.25201 | -50.32606 | 2025-10-02 04:02:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 772cd260-0bd6-35f6-90a8-bafc9adf04a4 | -11.08904 | -47.83914 | 2025-10-02 04:02:00 | NOAA-21 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 6b5b1c9d-63ec-3267-a9ab-89541f9ddb30 | -11.86708 | -48.07998 | 2025-10-02 04:02:00 | NOAA-21 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 3e3d4a49-0be4-3f77-8114-15d7805040f5 | -11.86689 | -45.00564 | 2025-10-02 04:02:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 265e4560-1930-3d6c-ab37-5fa40bf9659c | -11.2868 | -47.21764 | 2025-10-02 04:02:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 8fa2e1fb-8dc9-3b7e-ab80-fec23b3bfd40 | -9.77045 | -47.7496 | 2025-10-02 04:02:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 6b4cb3f5-56d3-3ed0-bd5a-4e324c2da836 | -12.89568 | -46.90388 | 2025-10-02 04:02:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 55992294-e0fa-3587-be69-5669cc755738 | -6.20409 | -43.92709 | 2025-10-02 04:02:00 | NOAA-21 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 07ba6314-61e4-3216-97e7-5e4d97c14f0d | -10.88622 | -44.2915 | 2025-10-02 04:02:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 4585f974-99d0-3210-84a7-eb034f58cb64 | -11.06814 | -47.81234 | 2025-10-02 04:02:00 | NOAA-21 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 0b790881-4808-3f4b-b6f1-23ea472f8df4 | -12.75904 | -39.73913 | 2025-10-02 04:02:00 | NOAA-21 | ITATIM | BAHIA | Brasil | 2916856 | 29 | 33 | nan | nan | nan | Caatinga | 5.1 |
| c1576204-b2f9-3187-a884-3666aeb70d16 | -6.4471 | -43.44473 | 2025-10-02 04:02:00 | NOAA-21 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 9f9211f9-7d40-34cf-b58a-b39035e8ce20 | -9.89562 | -45.9454 | 2025-10-02 04:02:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 9b4ba758-4c52-3d94-a6bf-754bf8365693 | -11.14554 | -47.20056 | 2025-10-02 04:02:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 371db36d-5229-328b-b5f6-31a6cda9d69f | -10.25136 | -50.32952 | 2025-10-02 04:02:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| d5302dc0-0967-310e-96f2-7c8b3a95c346 | -6.27966 | -44.05973 | 2025-10-02 04:02:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| a9b5cf60-9414-31fd-b7fb-92d0e7580c63 | -11.57273 | -47.02639 | 2025-10-02 04:02:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 35a6b6fe-7372-3818-91f3-750db51a931c | -11.47926 | -44.99135 | 2025-10-02 04:02:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 3f91396d-a2cd-32ce-b56b-2c61104b059f | -7.55131 | -42.64287 | 2025-10-02 04:02:00 | NOAA-21 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| e39b5a3c-f4b4-3871-8b49-f98a6b1aab72 | -6.6653 | -42.79797 | 2025-10-02 04:02:00 | NOAA-21 | FRANCISCO AYRES | PIAUÍ | Brasil | 2204105 | 22 | 33 | nan | nan | nan | Caatinga | 2.9 |
| 63e60805-0201-3659-8dd2-32fdef05bdaf | -12.00658 | -46.64574 | 2025-10-02 04:02:00 | NOAA-21 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| d39c5a4c-abf8-3811-97d4-d16c8ee53da4 | -8.56846 | -48.64758 | 2025-10-02 04:02:00 | NOAA-21 | ITAPORÃ DO TOCANTINS | TOCANTINS | Brasil | 1711100 | 17 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 37708986-7e92-399c-b54d-ff7321f44b93 | -11.00413 | -46.57741 | 2025-10-02 04:02:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| e6ff1e4a-984c-3502-88dd-3f533f03d021 | -11.77626 | -46.83613 | 2025-10-02 04:02:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 374ba029-5619-35d0-8c66-37afa0899540 | -11.37915 | -45.0392 | 2025-10-02 04:02:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| f59c8bb1-f00a-3a12-9a50-30cb4b8e3fb9 | -9.94757 | -43.57932 | 2025-10-02 04:02:00 | NOAA-21 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| b8113e0f-b974-3f2a-9995-89dcce6625da | -8.90375 | -46.66464 | 2025-10-02 04:02:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 8f7701e3-af79-3cc0-bd8c-01fb656c61bf | -6.04479 | -42.43956 | 2025-10-02 04:02:00 | NOAA-21 | HUGO NAPOLEÃO | PIAUÍ | Brasil | 2204600 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 0a268eeb-1308-3819-acba-f619a89c124e | -10.7716 | -45.36282 | 2025-10-02 04:02:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 52d036a6-9ae8-319e-94af-f02dbe8e27d7 | -7.78649 | -42.51542 | 2025-10-02 04:02:00 | NOAA-21 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 3.7 |
| 8fb58835-5a72-372a-b8fa-ad41184e1570 | -7.55883 | -42.40141 | 2025-10-02 04:02:00 | NOAA-21 | SÃO MIGUEL DO FIDALGO | PIAUÍ | Brasil | 2210391 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 258e25e0-da3b-3598-b0f2-0cccaeb30ca9 | -10.99256 | -46.59455 | 2025-10-02 04:02:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 04948196-d91d-3248-9d49-43396963a783 | -11.79684 | -47.56904 | 2025-10-02 04:02:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 47e4c9f5-4ad9-349f-a058-6fcefd9e77d2 | -9.937 | -43.71046 | 2025-10-02 04:02:00 | NOAA-21 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 8ee7342d-8546-36a0-9e40-9cf231a1c9dd | -8.89796 | -46.62087 | 2025-10-02 04:02:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 5.1 |
| e993ea99-1136-3cb0-801c-195d5736cfc5 | -11.27395 | -47.80085 | 2025-10-02 04:02:00 | NOAA-21 | SANTA ROSA DO TOCANTINS | TOCANTINS | Brasil | 1718907 | 17 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 90f0e84b-4cc2-3e41-8717-31c9fdb0d8e9 | -10.99442 | -46.59444 | 2025-10-02 04:02:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 18.4 |
| c30e5a44-31b9-3a93-9d96-8dcdc017dc15 | -11.92531 | -47.88494 | 2025-10-02 04:02:00 | NOAA-21 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 4ab5bf44-6e7d-344e-9d28-ba80acbb3396 | -12.63277 | -44.85671 | 2025-10-02 04:02:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 1185788f-6736-3b3a-ac7f-10079563a604 | -7.77293 | -45.7105 | 2025-10-02 04:02:00 | NOAA-21 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 7c0564b2-682b-3e77-bbd9-294af24a8135 | -6.96843 | -45.31936 | 2025-10-02 04:02:00 | NOAA-21 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 470cb7c0-cc17-3f9d-adf0-a4c2d7d8d112 | -11.35369 | -44.9762 | 2025-10-02 04:02:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 050fdd5e-6960-32ca-b25f-2fb9503ad187 | -12.9367 | -46.43163 | 2025-10-02 04:02:00 | NOAA-21 | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 8e085f95-c8a0-30e6-9e1d-5e6ca12a48a1 | -6.32296 | -43.88794 | 2025-10-02 04:02:00 | NOAA-21 | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 6a159c4f-0482-386c-9515-e7cf7ec1ee9d | -12.1812 | -46.60504 | 2025-10-02 04:02:00 | NOAA-21 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 73809153-bda7-36ba-bac8-350acdd65cda | -6.4621 | -44.57449 | 2025-10-02 04:02:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 11.6 |
| 3e699f7d-6e5d-3f22-9f95-53239be1a93a | -10.21163 | -50.27577 | 2025-10-02 04:02:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 11.5 |
| 5a562779-c3e4-303b-8c00-c4d1be9099f1 | -9.41443 | -47.32794 | 2025-10-02 04:02:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 43fad3d8-ae5a-3417-80ba-a40d0183806d | -9.39873 | -47.33892 | 2025-10-02 04:02:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 0371da61-bd91-347d-8e75-cab2cbcd5953 | -11.71744 | -44.4683 | 2025-10-02 04:02:00 | NOAA-21 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 3c55f661-fa16-3fbe-8dd9-1143e5984c33 | -13.00894 | -45.22905 | 2025-10-02 04:02:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 6.2 |
| e21a56a6-f2d2-3540-a68b-ce639aec71db | -9.1694 | -40.04678 | 2025-10-02 04:02:00 | NOAA-21 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 0.4 |
| a823e445-a66d-3341-8849-4fe78fa9e2aa | -12.27838 | -45.37634 | 2025-10-02 04:02:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 3.8 |


[Clique aqui para ver as próximas entradas](README36.md)
