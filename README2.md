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

## Dados Diários - Página 2

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| cb625902-2371-35c7-bb22-c3d9b8633cfb | -3.89664 | -38.63848 | 2025-04-01 03:57:00 | NOAA-20 | MARACANAÚ | CEARÁ | Brasil | 2307650 | 23 | 33 | nan | nan | nan | Caatinga | 0.4 |
| de12861c-2a53-37ea-a8ff-e6c0d30d58dc | -8.07111 | -34.97527 | 2025-04-01 03:57:00 | NOAA-20 | RECIFE | PERNAMBUCO | Brasil | 2611606 | 26 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 4b6763f0-8088-31a5-a4a6-d864c55f8a10 | -8.07517 | -34.97586 | 2025-04-01 03:57:00 | NOAA-20 | RECIFE | PERNAMBUCO | Brasil | 2611606 | 26 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 3f34241f-5733-3e53-b31b-ef723a518c63 | -7.23133 | -44.77771 | 2025-04-01 03:57:00 | NOAA-20 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| e1befd92-0eab-3708-a366-6cd194d685dd | -5.00753 | -37.3113 | 2025-04-01 03:57:00 | NOAA-20 | MOSSORÓ | RIO GRANDE DO NORTE | Brasil | 2408003 | 24 | 33 | nan | nan | nan | Caatinga | 0.7 |
| e143d5f5-6a98-324e-a6ee-3e9b8ddd1315 | -9.32922 | -37.01044 | 2025-04-01 03:57:00 | NOAA-20 | IATI | PERNAMBUCO | Brasil | 2606507 | 26 | 33 | nan | nan | nan | Caatinga | 1.1 |
| bdbbe685-f63e-347f-b482-d8a774385f0f | -4.76056 | -43.38026 | 2025-04-01 03:57:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 637b6c15-595d-3eb6-8a14-3c11450e8170 | -7.23618 | -44.77325 | 2025-04-01 03:57:00 | NOAA-20 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 4.0 |
| a00f3e9c-0bd3-3780-a95d-5f2d900b6ce3 | -5.6882 | -45.19328 | 2025-04-01 03:57:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 35ddf41b-2d7a-370c-a55a-692f3eef8c9d | -5.68757 | -45.19714 | 2025-04-01 03:57:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| b29a9426-10c5-33f3-ac7c-d9b1afd66bef | -7.2322 | -44.77259 | 2025-04-01 03:57:00 | NOAA-20 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| d47eee14-d3d3-38e5-bdaa-3a40a2000b0f | -8.39225 | -35.02475 | 2025-04-01 03:57:00 | NOAA-20 | IPOJUCA | PERNAMBUCO | Brasil | 2607208 | 26 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| 5c933cc7-5af9-3d89-b5e0-f66d3b25a52e | -9.19051 | -45.34516 | 2025-04-01 04:00:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 0.6 |
| be7866a3-8668-306d-8d2c-cd19dfec5d1c | -10.3497 | -38.47984 | 2025-04-01 04:00:00 | NOAA-20 | NOVO TRIUNFO | BAHIA | Brasil | 2923050 | 29 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 64aec5cc-de57-31da-bb32-88d1ae24ab3f | -9.97619 | -37.91314 | 2025-04-01 04:00:00 | NOAA-20 | PEDRO ALEXANDRE | BAHIA | Brasil | 2924207 | 29 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 5d867f4b-e2bd-3a51-9adb-d93d1c8cb98e | -9.18651 | -45.34444 | 2025-04-01 04:00:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 0.6 |
| ad2503c0-8f2d-3676-8621-77536d0df375 | -9.9797 | -37.9137 | 2025-04-01 04:00:00 | NOAA-20 | PEDRO ALEXANDRE | BAHIA | Brasil | 2924207 | 29 | 33 | nan | nan | nan | Caatinga | 0.8 |
| fa11382a-453c-337c-819a-9bdf162d14ae | -10.35028 | -38.47604 | 2025-04-01 04:00:00 | NOAA-20 | NOVO TRIUNFO | BAHIA | Brasil | 2923050 | 29 | 33 | nan | nan | nan | Caatinga | 2.0 |
| bf7d9063-4df3-312f-b2f4-c55ae0c2e06d | -13.02671 | -45.09727 | 2025-04-01 04:00:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 8fea625b-5d7e-39f8-b873-f2227bf5e482 | -12.81909 | -45.46398 | 2025-04-01 04:00:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 237776b9-2965-31a9-85e5-f0f13c3dc7ec | -12.30201 | -42.03024 | 2025-04-01 04:00:00 | NOAA-20 | SEABRA | BAHIA | Brasil | 2929909 | 29 | 33 | nan | nan | nan | Caatinga | 1.0 |
| f383378e-e9a3-3ce9-91c9-3458a3f1de57 | -12.9646 | -41.9459 | 2025-04-01 04:00:00 | NOAA-20 | PIATÃ | BAHIA | Brasil | 2924306 | 29 | 33 | nan | nan | nan | Caatinga | 0.9 |
| cf8288fd-6af3-3a22-b115-0f1b73e07deb | -13.02723 | -45.11618 | 2025-04-01 04:00:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 7b210102-c5c1-380c-821d-7b4f871c006c | -13.02495 | -45.09876 | 2025-04-01 04:00:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 4.1 |
| cf3d6362-e2bd-3919-9e15-25c5e9e2e732 | -13.3135 | -44.19571 | 2025-04-01 04:00:00 | NOAA-20 | SANTA MARIA DA VITÓRIA | BAHIA | Brasil | 2928109 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 5859cf4c-2a7e-37d1-94fb-b34165dca348 | -13.03468 | -45.11753 | 2025-04-01 04:00:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 4.3 |
| e9bcee48-1ce3-3f3c-a942-b6805fed15a3 | -14.11805 | -41.67897 | 2025-04-01 04:00:00 | NOAA-20 | BRUMADO | BAHIA | Brasil | 2904605 | 29 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 3ec95ab5-8d73-30f5-80d7-2ceff05aba52 | -13.03628 | -45.10839 | 2025-04-01 04:00:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 6.3 |
| e48039bc-52e0-3b74-893a-dafea5be3444 | -15.39932 | -40.84098 | 2025-04-01 04:00:00 | NOAA-20 | RIBEIRÃO DO LARGO | BAHIA | Brasil | 2926657 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 525e89bf-bc98-3e11-b272-733b606ef034 | -13.04 | -45.10907 | 2025-04-01 04:00:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 6f0ff7b0-1f2a-3f4c-93b6-16db7bc8d975 | -13.02803 | -45.11161 | 2025-04-01 04:00:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 17da4a2a-f62f-311c-ad37-cd3fdfdd8643 | -13.95558 | -45.34564 | 2025-04-01 04:00:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| a838f95e-5ac5-3f27-ab46-02b2aaf5f1b5 | -13.03096 | -45.11686 | 2025-04-01 04:00:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 0822bd48-cf70-33c5-b1ce-d5ac8efa9598 | -13.02963 | -45.10249 | 2025-04-01 04:00:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| d4c6fa0c-8d79-3995-9ac7-01341c8485f3 | -13.58386 | -45.24395 | 2025-04-01 04:00:00 | NOAA-20 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 1939f90f-a25d-392e-bb9a-2bc642bd3d90 | -15.39598 | -40.84044 | 2025-04-01 04:00:00 | NOAA-20 | RIBEIRÃO DO LARGO | BAHIA | Brasil | 2926657 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 363f0022-b6a5-3b75-8752-fe0afb286267 | -13.02572 | -45.0942 | 2025-04-01 04:00:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 1c7eca4c-2e42-322d-a40d-a3b9c58bdada | -13.0275 | -45.09271 | 2025-04-01 04:00:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 8769f20c-a357-38b8-91ff-af9f68f2fdd3 | -13.40655 | -41.88058 | 2025-04-01 04:00:00 | NOAA-20 | RIO DE CONTAS | BAHIA | Brasil | 2926707 | 29 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 5d0794aa-4585-3588-afa9-8fe9948e0d60 | -12.29106 | -43.54184 | 2025-04-01 04:00:00 | NOAA-20 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 17ca438d-d8d4-30e3-8ad6-3b43722aa623 | -13.0392 | -45.11363 | 2025-04-01 04:00:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 26b65ba9-e0bf-39ed-85c0-49e4b295fa2e | -13.03548 | -45.11296 | 2025-04-01 04:00:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 368c7df2-ca30-373b-8b24-11df60013a8e | -13.58228 | -45.25306 | 2025-04-01 04:00:00 | NOAA-20 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| ab64c04c-9d28-3a58-b224-9418d34dadf8 | -13.58014 | -45.24327 | 2025-04-01 04:00:00 | NOAA-20 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| a0e9ca33-583b-3272-88fe-03e53930a3f8 | -12.29041 | -43.54577 | 2025-04-01 04:00:00 | NOAA-20 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 71b7c470-aaaf-3837-bf7c-06ef082eefe9 | -12.69833 | -44.94315 | 2025-04-01 04:00:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| c809c668-4189-3991-a8ea-817b58b2a736 | -13.03176 | -45.11229 | 2025-04-01 04:00:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 65bef715-d2be-386e-8f28-2b44c4ece748 | -13.03255 | -45.10772 | 2025-04-01 04:00:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| a1ba8030-a5bd-3bde-a4c2-3992435c2d77 | -13.03043 | -45.09793 | 2025-04-01 04:00:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 3.6 |
| e1bb6d66-d314-3ac3-b227-0b195b2d34a0 | -13.58307 | -45.24849 | 2025-04-01 04:00:00 | NOAA-20 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 31e0fafc-ddc7-307c-9f57-e836116e7561 | -12.28758 | -43.54123 | 2025-04-01 04:00:00 | NOAA-20 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 55daec50-b00c-3ce6-9666-6c1fec5e14ff | -20.90117 | -43.81842 | 2025-04-01 04:02:00 | NOAA-20 | CARANAÍBA | MINAS GERAIS | Brasil | 3113107 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| cdbadafa-950a-3498-b025-b170b3e55f09 | -16.6149 | -43.33215 | 2025-04-01 04:02:00 | NOAA-20 | GRÃO MOGOL | MINAS GERAIS | Brasil | 3127800 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 3f382fbf-e21c-31f7-837e-14ab46bcfe1f | -16.6517 | -44.04149 | 2025-04-01 04:02:00 | NOAA-20 | MONTES CLAROS | MINAS GERAIS | Brasil | 3143302 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 42ddfa38-6399-3820-bd53-3494d732654a | -18.73391 | -45.02346 | 2025-04-01 04:02:00 | NOAA-20 | FELIXLÂNDIA | MINAS GERAIS | Brasil | 3125705 | 31 | 33 | nan | nan | nan | Cerrado | 7.2 |
| f92ab3ff-00f3-3ea1-8171-df37e85806d2 | -20.4171 | -43.55328 | 2025-04-01 04:02:00 | NOAA-20 | OURO PRETO | MINAS GERAIS | Brasil | 3146107 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| 0360d72b-e17e-3aec-8c00-756f8800800c | -18.67828 | -48.04147 | 2025-04-01 04:02:00 | NOAA-20 | ARAGUARI | MINAS GERAIS | Brasil | 3103504 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| ed929411-2fd2-3667-983c-ba9055045ae8 | -15.89503 | -43.45673 | 2025-04-01 04:02:00 | NOAA-20 | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| f2c0922c-d2be-3919-858d-ac5ea17eccd0 | -16.09058 | -42.28561 | 2025-04-01 04:02:00 | NOAA-20 | SALINAS | MINAS GERAIS | Brasil | 3157005 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 79ebf0d1-a5c0-378e-b28c-8650a0eabe2a | -16.68159 | -43.88235 | 2025-04-01 04:02:00 | NOAA-20 | MONTES CLAROS | MINAS GERAIS | Brasil | 3143302 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 37e6ce3a-3729-3c76-b306-dd58b9503f58 | -16.09446 | -42.2826 | 2025-04-01 04:02:00 | NOAA-20 | SALINAS | MINAS GERAIS | Brasil | 3157005 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.3 |
| 02d7a3bf-d564-3676-8497-ceb98e5b095b | -17.90666 | -44.41232 | 2025-04-01 04:02:00 | NOAA-20 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 15ca10d8-a3b8-38bd-962e-1f3094c15121 | -15.0782 | -48.94443 | 2025-04-01 04:02:00 | NOAA-20 | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 037a71b2-d49e-3a17-abe2-f2af3a997d75 | -22.90227 | -43.75722 | 2025-04-01 04:02:00 | NOAA-20 | RIO DE JANEIRO | RIO DE JANEIRO | Brasil | 3304557 | 33 | 33 | nan | nan | nan | Mata Atlântica | 0.4 |
| d4c9f15d-a818-3f21-b11c-d7ac4461befa | -21.36036 | -42.65368 | 2025-04-01 04:02:00 | NOAA-20 | CATAGUASES | MINAS GERAIS | Brasil | 3115300 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 3c42f222-4349-3728-aec7-604e95f62cf4 | -15.89165 | -43.45614 | 2025-04-01 04:02:00 | NOAA-20 | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| aaec18e6-3a18-3e21-adec-752755176737 | -18.14409 | -47.80149 | 2025-04-01 04:02:00 | NOAA-20 | OUVIDOR | GOIÁS | Brasil | 5215504 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| afa45fe4-013b-3b08-a18d-8a26c70801f2 | -17.60227 | -39.70927 | 2025-04-01 04:02:00 | NOAA-20 | TEIXEIRA DE FREITAS | BAHIA | Brasil | 2931350 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 671d6c6d-358d-3d24-b42c-cdf872a102da | -19.33396 | -45.0114 | 2025-04-01 04:02:00 | NOAA-20 | POMPÉU | MINAS GERAIS | Brasil | 3152006 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 3e0ed6ba-81d2-3246-a314-b29412ef0019 | -15.88828 | -43.45555 | 2025-04-01 04:02:00 | NOAA-20 | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 3fee8cbd-ceff-38f4-91bf-1608398da3ac | -16.65234 | -44.03763 | 2025-04-01 04:02:00 | NOAA-20 | MONTES CLAROS | MINAS GERAIS | Brasil | 3143302 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| eb0806c9-8020-3188-88b2-7e615050bd18 | -15.77997 | -41.99519 | 2025-04-01 04:02:00 | NOAA-20 | TAIOBEIRAS | MINAS GERAIS | Brasil | 3168002 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 8148aabd-0254-3248-a0dd-a06bcd107022 | -22.90286 | -43.75348 | 2025-04-01 04:02:00 | NOAA-20 | RIO DE JANEIRO | RIO DE JANEIRO | Brasil | 3304557 | 33 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 31b2cc59-9902-338a-86fa-ca15ffab11a4 | -19.45439 | -44.22618 | 2025-04-01 04:02:00 | NOAA-20 | SETE LAGOAS | MINAS GERAIS | Brasil | 3167202 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| a1fac23a-2d40-38cf-9e07-ecc0293fdedd | -15.8984 | -43.45733 | 2025-04-01 04:02:00 | NOAA-20 | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 4d500873-35b8-3e8d-9554-863bc3de0b7b | -15.88766 | -43.45929 | 2025-04-01 04:02:00 | NOAA-20 | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 7beea732-6750-3aeb-8365-4aaa435dae79 | -16.09115 | -42.28203 | 2025-04-01 04:02:00 | NOAA-20 | SALINAS | MINAS GERAIS | Brasil | 3157005 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 88df0120-13da-3196-ab70-41defa6b39d9 | -16.64893 | -44.03703 | 2025-04-01 04:02:00 | NOAA-20 | MONTES CLAROS | MINAS GERAIS | Brasil | 3143302 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 993faef9-d573-38b2-91ee-344bb7896a0e | -17.09522 | -43.80276 | 2025-04-01 04:02:00 | NOAA-20 | BOCAIÚVA | MINAS GERAIS | Brasil | 3107307 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 2cb1d05b-ce7a-3fb5-8a84-d0109b6ba936 | -19.5135 | -44.27571 | 2025-04-01 04:02:00 | NOAA-20 | SETE LAGOAS | MINAS GERAIS | Brasil | 3167202 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 2dd07f0b-1ddc-3f75-9b41-762b9e12d052 | -16.04502 | -43.8045 | 2025-04-01 04:02:00 | NOAA-20 | SÃO JOÃO DA PONTE | MINAS GERAIS | Brasil | 3162401 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 3a84a3d1-9043-3fb6-8a02-b20e11cc2117 | -22.91971 | -45.41445 | 2025-04-01 04:04:00 | NOAA-20 | PINDAMONHANGABA | SÃO PAULO | Brasil | 3538006 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| f94afd9d-9a87-3d05-bc99-a2d451f391ae | -23.33826 | -46.77309 | 2025-04-01 04:04:00 | NOAA-20 | CAIEIRAS | SÃO PAULO | Brasil | 3509007 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| df83b705-053a-3e5a-8ba5-4ff0b45f1553 | -25.19178 | -49.32577 | 2025-04-01 04:04:00 | NOAA-20 | RIO BRANCO DO SUL | PARANÁ | Brasil | 4122206 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| f0dc89bf-671c-30d2-85c5-50cc23d86e73 | -12.29246 | -43.54039 | 2025-04-01 04:51:00 | NOAA-21 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| a7b14f2b-10b5-3174-98c9-2130e23e299e | -13.03386 | -45.11073 | 2025-04-01 04:51:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 4.9 |
| ac78c8c9-3253-3fa4-b811-0cde17289a03 | -12.29305 | -43.54574 | 2025-04-01 04:51:00 | NOAA-21 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 752d8ccb-febd-3e1c-9f00-f5fdbec7c69f | -13.04394 | -45.11539 | 2025-04-01 04:51:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 98371c9d-1151-37cc-b70e-f41caedad9f8 | -13.0298 | -45.10025 | 2025-04-01 04:51:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 49e208ae-7b59-363d-ac59-a3d550fd4e58 | -7.23736 | -44.77706 | 2025-04-01 04:51:00 | NOAA-21 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 47c39d0b-69e2-3c59-a88e-974546debc86 | -13.02743 | -45.11977 | 2025-04-01 04:51:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 429c3f77-bfeb-32eb-8100-c1f093a12e4d | -13.02534 | -45.09301 | 2025-04-01 04:51:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 9b40a41c-86f6-3324-a33e-2f93e6812af9 | -6.20454 | -48.0439 | 2025-04-01 04:51:00 | NOAA-21 | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 7841452f-7ffc-34a2-8619-d10ac9a22d64 | -13.03306 | -45.11723 | 2025-04-01 04:51:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 3.2 |
| dbc98661-c944-3273-8d5f-54035836f5b3 | -13.0387 | -45.11469 | 2025-04-01 04:51:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 509ceec4-08c8-3a66-98b7-fcd824565de3 | -11.35108 | -57.66398 | 2025-04-01 04:51:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 4d32c99f-9274-39de-92d0-edadeb550b16 | -13.03059 | -45.09373 | 2025-04-01 04:51:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| f2cb9f61-ad1b-3232-90de-2b3f53d402de | -7.23568 | -44.77665 | 2025-04-01 04:51:00 | NOAA-21 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| bd3f756b-a55e-3266-9882-36eb839bd12d | -13.02495 | -45.09628 | 2025-04-01 04:51:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 2c1ca633-4f0e-3d5e-92d9-b8a5cb2b7d0a | -13.0383 | -45.11794 | 2025-04-01 04:51:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 3.2 |


[Clique aqui para ver as próximas entradas](README3.md)
