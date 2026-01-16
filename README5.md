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
| dc5ab1fe-6bc9-39b7-bb93-16d4f0cd2a87 | -14.465 | -44.23293 | 2026-01-16 04:16:00 | NOAA-21 | JUVENÍLIA | MINAS GERAIS | Brasil | 3136959 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 5009f485-d157-3862-8ba4-11e276a2aa5d | -8.72525 | -48.31845 | 2026-01-16 04:16:00 | NOAA-21 | GUARAÍ | TOCANTINS | Brasil | 1709302 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| bd7733da-871e-3f41-ab12-b97ec3514540 | -14.77131 | -45.92588 | 2026-01-16 04:16:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| ac60897e-8c96-3c3a-b1c0-5d56d45fb470 | -14.77015 | -45.93305 | 2026-01-16 04:16:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| aca49116-756b-3c18-b99b-459b2d343bfc | -11.1596 | -43.57866 | 2026-01-16 04:16:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| b8282b74-899e-3088-ad63-c1eda9a903a4 | -12.29327 | -43.50207 | 2026-01-16 04:16:00 | NOAA-21 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| b345d320-5c3b-3b73-a0fa-adaad4657061 | -12.16388 | -44.33802 | 2026-01-16 04:16:00 | NOAA-21 | CRISTÓPOLIS | BAHIA | Brasil | 2909703 | 29 | 33 | nan | nan | nan | Cerrado | 0.3 |
| 0ed941ac-2f02-3636-bfd2-29a393ab381c | -12.22884 | -40.40932 | 2026-01-16 04:16:00 | NOAA-21 | RUY BARBOSA | BAHIA | Brasil | 2927200 | 29 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 58842124-c019-3b94-afb2-be4cc45add5a | -10.7382 | -48.69525 | 2026-01-16 04:16:00 | NOAA-21 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| e4fb35df-7f1b-3b4d-8e12-b03d7fb93ae1 | -11.18496 | -43.30259 | 2026-01-16 04:16:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 16d632ac-c7de-3457-8b58-e3fc235b7b88 | -9.43119 | -35.54675 | 2026-01-16 04:16:00 | NOAA-21 | PARIPUEIRA | ALAGOAS | Brasil | 2706448 | 27 | 33 | nan | nan | nan | Mata Atlântica | 2.4 |
| e6f81903-9e16-3295-bbfb-b9d42b188973 | -14.77895 | -45.94189 | 2026-01-16 04:16:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 988b3290-c58e-3ee0-bbea-febcced3b31a | -12.22942 | -40.40769 | 2026-01-16 04:16:00 | NOAA-21 | RUY BARBOSA | BAHIA | Brasil | 2927200 | 29 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 3edf224e-6a18-3b7c-9636-34e09e37145e | -9.42655 | -35.54304 | 2026-01-16 04:16:00 | NOAA-21 | PARIPUEIRA | ALAGOAS | Brasil | 2706448 | 27 | 33 | nan | nan | nan | Mata Atlântica | 2.4 |
| 683e0b58-097b-32ce-a038-e4c390d12dd2 | -13.32327 | -40.45614 | 2026-01-16 04:16:00 | NOAA-21 | MARACÁS | BAHIA | Brasil | 2920502 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| 95bf83d0-b0f1-3441-b58a-52cb46a036ee | -9.37691 | -47.08617 | 2026-01-16 04:16:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| d9d13da2-8341-3002-ada6-3a27005b43ee | -12.66496 | -46.76641 | 2026-01-16 04:16:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| f99597fd-de81-3d08-b7fc-c8a1fa9e5aec | -12.29 | -57.3914 | 2026-01-16 04:16:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 59ea479e-79c2-393e-9582-ea81def890b6 | -12.4982 | -46.34394 | 2026-01-16 04:16:00 | NOAA-21 | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 1ed6c6b7-d878-3a07-b24e-5053175d0953 | -12.08554 | -45.28825 | 2026-01-16 04:16:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 283818c6-e3bb-35c2-b838-cd82b8ec53da | -12.08611 | -45.2847 | 2026-01-16 04:16:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 8db2ca59-aa39-33fb-92fe-d7ebab6d997e | -12.16333 | -44.34153 | 2026-01-16 04:16:00 | NOAA-21 | CRISTÓPOLIS | BAHIA | Brasil | 2909703 | 29 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 253102ba-1edb-3153-bbb1-c3855c217027 | -11.16292 | -43.57919 | 2026-01-16 04:16:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| e1e0733e-c4bb-3294-8c99-f3ecdd99374a | -14.47998 | -44.33428 | 2026-01-16 04:16:00 | NOAA-21 | MONTALVÂNIA | MINAS GERAIS | Brasil | 3142700 | 31 | 33 | nan | nan | nan | Cerrado | 3.5 |
| b32e90f6-ab24-3f03-9192-02403c561c34 | -13.46919 | -44.03329 | 2026-01-16 04:16:00 | NOAA-21 | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 3d9bed3c-fe35-389d-bce9-a97b12d6b56d | -12.29652 | -57.39281 | 2026-01-16 04:16:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 5.3 |
| be2e0f1a-015c-317b-9d52-edc8fc8960b8 | -9.86261 | -39.97397 | 2026-01-16 04:16:00 | NOAA-21 | JAGUARARI | BAHIA | Brasil | 2917706 | 29 | 33 | nan | nan | nan | Caatinga | 3.5 |
| 094b015d-4cde-3955-8c74-3cb819e08378 | -9.4305 | -35.54642 | 2026-01-16 04:16:00 | NOAA-21 | PARIPUEIRA | ALAGOAS | Brasil | 2706448 | 27 | 33 | nan | nan | nan | Mata Atlântica | 3.3 |
| 1b5f0209-6cac-3867-b789-2080874aee6f | -13.43146 | -43.85856 | 2026-01-16 04:16:00 | NOAA-21 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 4.3 |
| ff9fc983-7581-35cd-9775-d40ef3b8223c | -12.92108 | -49.48586 | 2026-01-16 04:16:00 | NOAA-21 | ARAGUAÇU | TOCANTINS | Brasil | 1702000 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| d9688391-cc0a-3c3c-9509-2085938c352d | -8.00108 | -43.24625 | 2026-01-16 04:16:00 | NOAA-21 | PAVUSSU | PIAUÍ | Brasil | 2207850 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| afa3063b-d5cc-3928-a0b2-61dd4e3504b8 | -12.29272 | -43.50566 | 2026-01-16 04:16:00 | NOAA-21 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| e6df8b6f-6a5e-39be-853a-3998fd9723d5 | -12.08498 | -45.29179 | 2026-01-16 04:16:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 2dfc3712-6d77-3396-913b-fef64dbf7c35 | -12.925 | -49.48656 | 2026-01-16 04:16:00 | NOAA-21 | ARAGUAÇU | TOCANTINS | Brasil | 1702000 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 754e0023-01a2-3548-ac72-9fe4ac459a89 | -9.43088 | -35.54343 | 2026-01-16 04:16:00 | NOAA-21 | PARIPUEIRA | ALAGOAS | Brasil | 2706448 | 27 | 33 | nan | nan | nan | Mata Atlântica | 3.3 |
| 2b4f1e2e-2e39-319d-8588-704c791143ed | -14.12656 | -43.41779 | 2026-01-16 04:16:00 | NOAA-21 | PALMAS DE MONTE ALTO | BAHIA | Brasil | 2923407 | 29 | 33 | nan | nan | nan | Cerrado | 0.4 |
| f5a98ef4-55a5-3493-9bde-d70b8ab9eb74 | -11.73378 | -37.52515 | 2026-01-16 04:16:00 | NOAA-21 | JANDAÍRA | BAHIA | Brasil | 2917904 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| c151b687-4612-30a6-9bea-274a557c6f85 | -12.66472 | -46.76588 | 2026-01-16 04:16:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 6e041078-95ca-3159-95d7-9b82f46b1772 | -8.37084 | -41.78905 | 2026-01-16 04:16:00 | NOAA-21 | CAMPO ALEGRE DO FIDALGO | PIAUÍ | Brasil | 2202117 | 22 | 33 | nan | nan | nan | Caatinga | 5.5 |
| c9f342eb-1ca7-33f1-8a58-a7cb1e9b5f30 | -8.72609 | -48.31353 | 2026-01-16 04:16:00 | NOAA-21 | GUARAÍ | TOCANTINS | Brasil | 1709302 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 3c1fc761-ef51-3f16-b57f-a20e24ac8014 | -9.43159 | -35.54376 | 2026-01-16 04:16:00 | NOAA-21 | PARIPUEIRA | ALAGOAS | Brasil | 2706448 | 27 | 33 | nan | nan | nan | Mata Atlântica | 2.4 |
| 99dd3ad7-6b4d-3854-bee0-b2066297acaf | -14.12318 | -43.41726 | 2026-01-16 04:16:00 | NOAA-21 | PALMAS DE MONTE ALTO | BAHIA | Brasil | 2923407 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 0f722086-2b29-3aab-9b79-8222f7d886d3 | -10.69849 | -42.67629 | 2026-01-16 04:16:00 | NOAA-21 | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Caatinga | 1.4 |
| a2afbfa8-9358-3abb-a5bf-898f52f69fe1 | -12.67727 | -46.64756 | 2026-01-16 04:16:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 399ad263-6c2c-3d20-a6d6-6e1b80e0d19a | -9.86328 | -39.96931 | 2026-01-16 04:16:00 | NOAA-21 | JAGUARARI | BAHIA | Brasil | 2917706 | 29 | 33 | nan | nan | nan | Caatinga | 3.5 |
| d793fcd3-bf3f-3951-91c5-43de7447d18b | -9.91957 | -36.58561 | 2026-01-16 04:16:00 | NOAA-21 | SÃO SEBASTIÃO | ALAGOAS | Brasil | 2708808 | 27 | 33 | nan | nan | nan | Mata Atlântica | 5.0 |
| 8d1bb668-7a47-36bd-8a8c-6b92d12ba26d | -9.43126 | -35.54044 | 2026-01-16 04:16:00 | NOAA-21 | PARIPUEIRA | ALAGOAS | Brasil | 2706448 | 27 | 33 | nan | nan | nan | Mata Atlântica | 3.0 |
| 13015a18-c99e-36a7-845c-b720d87aa616 | -14.49502 | -44.41377 | 2026-01-16 04:16:00 | NOAA-21 | MONTALVÂNIA | MINAS GERAIS | Brasil | 3142700 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 484c1feb-84f8-3dcd-bf04-0fa837030f56 | -10.47829 | -40.54322 | 2026-01-16 04:16:00 | NOAA-21 | CAMPO FORMOSO | BAHIA | Brasil | 2906006 | 29 | 33 | nan | nan | nan | Caatinga | 1.7 |
| b7b315ec-2d46-32c6-9097-ecbb97e328ac | -9.30157 | -40.84146 | 2026-01-16 04:16:00 | NOAA-21 | CASA NOVA | BAHIA | Brasil | 2907202 | 29 | 33 | nan | nan | nan | Caatinga | 2.2 |
| a308af44-0e5d-3fc5-bc6f-254856678935 | -12.65187 | -46.76029 | 2026-01-16 04:16:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 7.7 |
| 7ae9850c-318f-3d49-ac81-c7b3d01ad1de | -12.27332 | -43.54301 | 2026-01-16 04:16:00 | NOAA-21 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 8ab6cf5a-ae8c-3d39-838f-001c6df59e45 | -10.61977 | -44.63993 | 2026-01-16 04:16:00 | NOAA-21 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| b1af2cd4-bb63-3be8-bf0e-5ee41750644a | -14.77073 | -45.92946 | 2026-01-16 04:16:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 28948fa5-9291-3e16-9e99-96d71151a8f3 | -7.9973 | -43.24563 | 2026-01-16 04:16:00 | NOAA-21 | PAVUSSU | PIAUÍ | Brasil | 2207850 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| b959dee3-7902-3fc5-80ee-113147a7bcff | -11.95583 | -44.21113 | 2026-01-16 04:16:00 | NOAA-21 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| a54059c7-9cf8-372d-a206-c1ab7211c1a4 | -12.64906 | -46.7559 | 2026-01-16 04:16:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 7.7 |
| 5ed780cf-a441-37eb-802e-73e8b422d3d0 | -12.29382 | -43.49848 | 2026-01-16 04:16:00 | NOAA-21 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 27d406fa-8ab6-3292-8fd3-5eec4491b4e6 | -12.29217 | -43.50925 | 2026-01-16 04:16:00 | NOAA-21 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 28a8c3f9-9dd0-3558-bf43-90a5d66c231d | -12.28274 | -43.52613 | 2026-01-16 04:16:00 | NOAA-21 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 85c0c5d3-f1c1-3e54-8906-3557adff33bd | -14.3324 | -42.97823 | 2026-01-16 04:16:00 | NOAA-21 | GUANAMBI | BAHIA | Brasil | 2911709 | 29 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 46c51a86-ea4c-3e86-bd33-e155cd7d4035 | -9.92128 | -44.38699 | 2026-01-16 04:16:00 | NOAA-21 | CURIMATÁ | PIAUÍ | Brasil | 2203206 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 162938db-d746-34d6-aa04-2be0e2a14bb2 | -14.77621 | -45.93774 | 2026-01-16 04:16:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 9ab738b2-c88a-3f20-9ce5-6b4b01165d87 | -10.78336 | -44.42263 | 2026-01-16 04:16:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| b402c421-97a6-3805-af3f-6c062b0e6ea2 | -9.42614 | -35.54603 | 2026-01-16 04:16:00 | NOAA-21 | PARIPUEIRA | ALAGOAS | Brasil | 2706448 | 27 | 33 | nan | nan | nan | Mata Atlântica | 2.4 |
| e7efddd7-2d6d-3c08-9d5c-3289f7b55122 | -12.65311 | -46.75269 | 2026-01-16 04:16:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 11.0 |
| f47b3c9e-e061-33f8-af48-f13e3ed5db7b | -13.21692 | -47.78152 | 2026-01-16 04:16:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 91fd128b-97aa-32ba-bf9e-2089c1f31f29 | -11.95253 | -44.2106 | 2026-01-16 04:16:00 | NOAA-21 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| a88098df-595b-3a4f-a025-e8362901c5a4 | -12.08932 | -43.76625 | 2026-01-16 04:16:00 | NOAA-21 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 8.5 |
| 9f007ae7-b10a-3b7d-ac4e-04802d2593ff | -13.3195 | -50.17429 | 2026-01-16 04:16:00 | NOAA-21 | SÃO MIGUEL DO ARAGUAIA | GOIÁS | Brasil | 5220207 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| e8e3fec3-2962-3f65-b2fb-b3cc298c92d3 | -14.47721 | -44.33016 | 2026-01-16 04:16:00 | NOAA-21 | MONTALVÂNIA | MINAS GERAIS | Brasil | 3142700 | 31 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 8642f944-f660-3565-a2d2-7278c51ad953 | -9.51974 | -42.99125 | 2026-01-16 04:16:00 | NOAA-21 | CAMPO ALEGRE DE LOURDES | BAHIA | Brasil | 2905909 | 29 | 33 | nan | nan | nan | Caatinga | 0.7 |
| a486e182-1aa6-3b00-8eca-a5f427f98bd4 | -12.65592 | -46.75707 | 2026-01-16 04:16:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 05649e3a-8a52-398d-8027-f283841cbe99 | -10.62088 | -44.63294 | 2026-01-16 04:16:00 | NOAA-21 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 4.7 |
| f58cddaa-38d8-31c9-aa51-655e758a71fb | -12.29161 | -43.51284 | 2026-01-16 04:16:00 | NOAA-21 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 8b02b352-799d-3f5e-b2d4-0093758a29f5 | -14.48053 | -44.33069 | 2026-01-16 04:16:00 | NOAA-21 | MONTALVÂNIA | MINAS GERAIS | Brasil | 3142700 | 31 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 4568c84c-3109-3ba0-8b42-6575e5f168f5 | -10.4125 | -44.89398 | 2026-01-16 04:16:00 | NOAA-21 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 12ac02e1-eeb7-3852-a380-984e0ce6d2d9 | -10.74287 | -48.69124 | 2026-01-16 04:16:00 | NOAA-21 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 50c22915-1b53-3d6c-bc27-e0172b3499a6 | -10.61702 | -44.63592 | 2026-01-16 04:16:00 | NOAA-21 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| da3c468d-95bf-396a-83cf-cac4a97a696e | -16.6588 | -43.3501 | 2026-01-16 04:18:00 | NOAA-21 | GRÃO MOGOL | MINAS GERAIS | Brasil | 3127800 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 9a5d9399-f495-3c8c-bf4b-fc71018c4d5f | -18.81645 | -51.60148 | 2026-01-16 04:18:00 | NOAA-21 | ITAJÁ | GOIÁS | Brasil | 5210802 | 52 | 33 | nan | nan | nan | Cerrado | 25.6 |
| e026195c-ce21-358b-b073-0928f3e8409b | -16.13774 | -40.40268 | 2026-01-16 04:18:00 | NOAA-21 | JACINTO | MINAS GERAIS | Brasil | 3134707 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| e2f63249-dcf0-3684-a37b-29e9627bf648 | -18.82577 | -51.61883 | 2026-01-16 04:18:00 | NOAA-21 | ITAJÁ | GOIÁS | Brasil | 5210802 | 52 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 6fe98bf9-dcea-3c95-9638-f2bc2a99339a | -13.69747 | -55.67328 | 2026-01-16 04:18:00 | NOAA-21 | NOVA MUTUM | MATO GROSSO | Brasil | 5106224 | 51 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 62e2e57e-1e1a-31af-93fb-9c25864d3a77 | -16.1005 | -56.75595 | 2026-01-16 04:18:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 245452b0-7741-3daa-b782-75feb7ab0020 | -15.8801 | -45.19685 | 2026-01-16 04:18:00 | NOAA-21 | PINTÓPOLIS | MINAS GERAIS | Brasil | 3150570 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| a7cd30fb-3b35-34fb-afa1-e432e3777df7 | -16.21937 | -45.65649 | 2026-01-16 04:18:00 | NOAA-21 | SÃO ROMÃO | MINAS GERAIS | Brasil | 3164209 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 8751c5af-f373-3eb1-beae-dbc283e7aad6 | -15.43621 | -56.33137 | 2026-01-16 04:18:00 | NOAA-21 | VÁRZEA GRANDE | MATO GROSSO | Brasil | 5108402 | 51 | 33 | nan | nan | nan | Cerrado | 5.8 |
| ad406815-ad0a-3f9d-9f6f-82229f4df16f | -18.82051 | -51.60224 | 2026-01-16 04:18:00 | NOAA-21 | ITAJÁ | GOIÁS | Brasil | 5210802 | 52 | 33 | nan | nan | nan | Cerrado | 25.6 |
| 00d06aa8-298c-3a34-a0ae-766859081db4 | -20.48073 | -42.24265 | 2026-01-16 04:18:00 | NOAA-21 | SANTA MARGARIDA | MINAS GERAIS | Brasil | 3157906 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 7463bb01-4580-39f0-9ca0-1251b335d09f | -15.5938 | -57.34153 | 2026-01-16 04:18:00 | NOAA-21 | PORTO ESTRELA | MATO GROSSO | Brasil | 5106851 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 6795bdc8-2e0e-3b82-9d1f-63e6f8ce18ea | -18.8198 | -51.60597 | 2026-01-16 04:18:00 | NOAA-21 | ITAJÁ | GOIÁS | Brasil | 5210802 | 52 | 33 | nan | nan | nan | Cerrado | 25.6 |
| 5765722b-d977-3f35-bcac-910d93e24c41 | -18.82172 | -51.61801 | 2026-01-16 04:18:00 | NOAA-21 | ITAJÁ | GOIÁS | Brasil | 5210802 | 52 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 1248f259-774d-3cef-919e-0ccd7db66d02 | -18.81837 | -51.61351 | 2026-01-16 04:18:00 | NOAA-21 | ITAJÁ | GOIÁS | Brasil | 5210802 | 52 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 9fcb049b-7230-3f3f-88f2-83473c8df7b7 | -13.6917 | -55.67216 | 2026-01-16 04:18:00 | NOAA-21 | NOVA MUTUM | MATO GROSSO | Brasil | 5106224 | 51 | 33 | nan | nan | nan | Cerrado | 4.8 |
| e26ea68f-85a6-383d-ab1a-3492dd3bd69f | -15.01536 | -48.65971 | 2026-01-16 04:18:00 | NOAA-21 | VILA PROPÍCIO | GOIÁS | Brasil | 5222302 | 52 | 33 | nan | nan | nan | Cerrado | 0.4 |
| fb546449-1ec9-3393-a800-f23f95954199 | -16.65477 | -43.35349 | 2026-01-16 04:18:00 | NOAA-21 | GRÃO MOGOL | MINAS GERAIS | Brasil | 3127800 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 9eb31ba1-f813-3fe6-9028-b3035a734919 | -17.61167 | -46.66027 | 2026-01-16 04:18:00 | NOAA-21 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 767a15a6-0a7b-3205-b0ae-607006bf88e9 | -20.09501 | -44.07175 | 2026-01-16 04:18:00 | NOAA-21 | BRUMADINHO | MINAS GERAIS | Brasil | 3109006 | 31 | 33 | nan | nan | nan | Mata Atlântica | 5.7 |
| 804a9678-1a6d-3dc5-b3c3-e2f389daed11 | -16.11412 | -56.74973 | 2026-01-16 04:18:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Cerrado | 7.1 |


[Clique aqui para ver as próximas entradas](README6.md)
