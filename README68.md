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

## Dados Diários - Página 68

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 5f377e4f-c94b-3be2-afbb-f966e582910e | -11.11938 | -54.0263 | 2026-09-20 04:40:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 22.6 |
| 99282072-a021-336c-9690-d19b0cd17962 | -13.62802 | -46.96266 | 2026-09-20 04:40:00 | NOAA-20 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 918635ca-8ed9-3316-b512-72a93800dcbf | -10.28826 | -50.20709 | 2026-09-20 04:40:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| ad8431ac-7f2c-387f-823e-cebed8b8f82c | -8.35839 | -47.25294 | 2026-09-20 04:40:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| e001d726-98a2-3069-be62-3bf8517d20b6 | -8.16574 | -54.74144 | 2026-09-20 04:40:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 8a233373-bf04-367a-809e-b36043d06020 | -8.05966 | -46.83347 | 2026-09-20 04:40:00 | NOAA-20 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 9e4c7b77-d14a-3169-a013-a22c78ccda8b | -7.88359 | -44.86429 | 2026-09-20 04:40:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 2c71aa29-a248-3486-b191-d4b50882e90d | -9.72446 | -47.21062 | 2026-09-20 04:40:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| c33c6fd6-f829-38ea-8577-07110141b489 | -6.3594 | -58.31332 | 2026-09-20 04:40:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 33d7d244-4012-3e97-9545-7e41c19bcd0a | -10.68252 | -60.73807 | 2026-09-20 04:40:00 | NOAA-20 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| c998b03e-e548-3149-b580-1134c3ded644 | -10.26549 | -50.26263 | 2026-09-20 04:40:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| e9f66fa3-6c5c-3259-a761-b52544773e30 | -7.18097 | -47.89652 | 2026-09-20 04:40:00 | NOAA-20 | BABAÇULÂNDIA | TOCANTINS | Brasil | 1703008 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 6471efb3-14ba-3777-aa2b-33cb3742b4e9 | -5.84872 | -53.55423 | 2026-09-20 04:40:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 11973625-5137-3412-9cdb-5f0efe22da7e | -13.67029 | -48.5761 | 2026-09-20 04:40:00 | NOAA-20 | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 8f83079d-514c-3776-b6d9-e72b1914e950 | -7.05769 | -47.53508 | 2026-09-20 04:40:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 31bc7bc6-5c9c-3946-8eb9-cf78f701f841 | -12.13115 | -47.02624 | 2026-09-20 04:40:00 | NOAA-20 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 5.9 |
| f05aa4fd-be3b-3dd2-9fe3-ea288f0b2119 | -8.22053 | -45.61256 | 2026-09-20 04:40:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 94de9a3d-a173-3692-b5a9-bd7bfc63018b | -8.38527 | -47.19098 | 2026-09-20 04:40:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 25022016-7f9f-3088-a58f-a74b7e05b930 | -9.90092 | -46.52931 | 2026-09-20 04:40:00 | NOAA-20 | SÃO FÉLIX DO TOCANTINS | TOCANTINS | Brasil | 1720150 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 7bf6677c-53d9-3809-94c3-d0371c989b36 | -13.67474 | -48.56945 | 2026-09-20 04:40:00 | NOAA-20 | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| c68cb4ea-de65-306a-874c-58cd75b4e004 | -9.69714 | -54.82445 | 2026-09-20 04:40:00 | NOAA-20 | GUARANTÃ DO NORTE | MATO GROSSO | Brasil | 5104104 | 51 | 33 | nan | nan | nan | Amazônia | 4.0 |
| a864571c-6cae-31f2-9e62-2fb98d1c1117 | -11.84209 | -46.83256 | 2026-09-20 04:40:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 871ffd09-587a-3f20-9146-bd71678d64bb | -13.23683 | -46.94775 | 2026-09-20 04:40:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 16051670-659e-3450-8b29-4b057ce28d6d | -10.40898 | -48.941 | 2026-09-20 04:40:00 | NOAA-20 | PUGMIL | TOCANTINS | Brasil | 1718451 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 7a08b36a-f0e9-3519-9ec7-1f43e208e8c3 | -10.88404 | -54.05798 | 2026-09-20 04:40:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| f7e842a1-5d97-36d0-b325-a9bfb8617ca0 | -9.02794 | -48.78213 | 2026-09-20 04:40:00 | NOAA-20 | GOIANORTE | TOCANTINS | Brasil | 1708304 | 17 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 78809c04-1f4b-30d5-9b50-55bbd1e279ef | -9.68818 | -49.28653 | 2026-09-20 04:40:00 | NOAA-20 | DIVINÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1707108 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 065e8e7a-a816-3543-b833-bea1eb7c79e7 | -11.88264 | -47.65334 | 2026-09-20 04:40:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| d8986366-54b0-3e06-a3e6-87c7d4ab9fed | -10.27382 | -50.27517 | 2026-09-20 04:40:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 4.6 |
| ff41508b-1df2-3460-9cd4-c5a6dee8dbde | -6.65253 | -50.93074 | 2026-09-20 04:40:00 | NOAA-20 | ÁGUA AZUL DO NORTE | PARÁ | Brasil | 1500347 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 238c5286-70cf-3d81-8b41-497f6c968dad | -8.45011 | -45.86354 | 2026-09-20 04:40:00 | NOAA-20 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 2567d1d3-3fe0-32b2-8776-73e5837e8ca9 | -9.23563 | -46.23807 | 2026-09-20 04:40:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 54215e82-a517-3e46-bce7-51a9f5ab6f60 | -11.31403 | -51.72145 | 2026-09-20 04:40:00 | NOAA-20 | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| d231d9e5-15d3-3109-aa56-2ce9515e59de | -13.74727 | -48.78139 | 2026-09-20 04:40:00 | NOAA-20 | CAMPINORTE | GOIÁS | Brasil | 5204706 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 1cfe14e5-aa2f-3795-bcca-8b2c26e858cf | -7.43247 | -44.68918 | 2026-09-20 04:40:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 26e5659a-550f-3e7c-925c-6c8a98df06ea | -5.89317 | -53.64888 | 2026-09-20 04:40:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 4e53117d-6a24-38c8-a01b-556982acd791 | -6.6541 | -47.46749 | 2026-09-20 04:40:00 | NOAA-20 | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 1207e607-5118-35b2-8e53-fb2cc4bb1948 | -9.72431 | -48.15646 | 2026-09-20 04:40:00 | NOAA-20 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| ce6ae582-09a4-3ccf-a329-76ba00d2e666 | -12.75575 | -46.12517 | 2026-09-20 04:40:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| e42c32a3-8dae-35d2-93cc-18db53516a5e | -7.27932 | -45.55298 | 2026-09-20 04:40:00 | NOAA-20 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| e8d20ed2-de6b-3adf-98c3-39e3b24e4549 | -11.04104 | -54.15908 | 2026-09-20 04:40:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 286e1405-e458-39eb-aa62-5cc4d53283cf | -7.53299 | -45.88236 | 2026-09-20 04:40:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| c2df89d5-1ed6-392f-b287-e92c9b0e45c8 | -9.92788 | -60.73412 | 2026-09-20 04:40:00 | NOAA-20 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 42dddbed-8390-32c3-9302-142a5c3074d1 | -10.89646 | -53.98726 | 2026-09-20 04:40:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 9a6a36f8-1b66-395b-9577-b0fe31c8941e | -11.85776 | -47.67963 | 2026-09-20 04:40:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 7bca3aa7-7ea2-3f8c-85b5-957523147f37 | -7.43296 | -44.76059 | 2026-09-20 04:40:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 4.6 |
| a0432940-3809-3e67-bc73-fce013ded6bc | -7.62915 | -46.76416 | 2026-09-20 04:40:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 82bda072-b7ff-3256-a6ac-59e423d87e37 | -9.23686 | -45.91717 | 2026-09-20 04:40:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| be9711e5-f67d-3c7b-8d1e-c573517ac56d | -7.78645 | -42.92563 | 2026-09-20 04:40:00 | NOAA-20 | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| b616c032-fcd4-30b2-b9c3-0a08779c1902 | -8.14872 | -54.813 | 2026-09-20 04:40:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 7d640e09-7e43-385a-af0b-9efacd32c7ce | -9.96514 | -46.55128 | 2026-09-20 04:40:00 | NOAA-20 | SÃO FÉLIX DO TOCANTINS | TOCANTINS | Brasil | 1720150 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 96b25f6b-2ae5-3dae-b527-a43eacbfa5fc | -13.55224 | -47.6723 | 2026-09-20 04:40:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 7409dcb7-c31a-3047-8b78-ef73e6586656 | -10.27791 | -50.24984 | 2026-09-20 04:40:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 7.4 |
| c6851b4d-dfdb-33dc-87fd-a10e6d0738ff | -7.53649 | -45.88288 | 2026-09-20 04:40:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 4c01708b-b8ea-3c8e-8ccf-d34fd062485c | -11.74435 | -54.56104 | 2026-09-20 04:40:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 05d790a0-1fe3-38f3-8b42-c2506dd60b95 | -5.85326 | -53.52761 | 2026-09-20 04:40:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 3aeb368a-7888-35e3-bd4d-e987f28a369c | -7.5794 | -44.90284 | 2026-09-20 04:40:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 5151a065-7ccb-35d7-8b6d-1597187f297e | -7.88488 | -44.85557 | 2026-09-20 04:40:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| deeef424-3ae3-36f0-a0df-ec66550aba1a | -8.76348 | -48.67228 | 2026-09-20 04:40:00 | NOAA-20 | GUARAÍ | TOCANTINS | Brasil | 1709302 | 17 | 33 | nan | nan | nan | Amazônia | 8.9 |
| 7fbb3d97-8cbc-3687-b81f-57d6ba33b56c | -9.71318 | -45.99424 | 2026-09-20 04:40:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 2d7d4ec7-34f3-3c05-8f75-a3a3505d392c | -5.86855 | -52.04262 | 2026-09-20 04:40:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| a0994412-f9f4-3882-954f-e06a9bce57de | -11.87416 | -47.6633 | 2026-09-20 04:40:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 769c7690-814b-3ee9-92e3-99f4f2611c64 | -10.4134 | -48.91304 | 2026-09-20 04:40:00 | NOAA-20 | PUGMIL | TOCANTINS | Brasil | 1718451 | 17 | 33 | nan | nan | nan | Cerrado | 5.8 |
| c527608b-88bd-37d3-8c28-90f5fc011fc0 | -10.20288 | -46.57809 | 2026-09-20 04:40:00 | NOAA-20 | SÃO FÉLIX DO TOCANTINS | TOCANTINS | Brasil | 1720150 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| c303cdbd-6db2-3c6e-8861-cab4014aee9f | -13.8894 | -48.58521 | 2026-09-20 04:40:00 | NOAA-20 | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 8.3 |
| ad74a285-23ad-3c56-9856-2d4fb890d986 | -9.83991 | -46.40239 | 2026-09-20 04:40:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 2ef11539-eaa0-3c59-8811-b8a81cf88323 | -8.77396 | -48.73451 | 2026-09-20 04:40:00 | NOAA-20 | COLMÉIA | TOCANTINS | Brasil | 1716703 | 17 | 33 | nan | nan | nan | Amazônia | 3.0 |
| e560a0a4-3aec-3ddd-8b8d-9706c809c593 | -10.98307 | -46.53856 | 2026-09-20 04:40:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| d076b764-87af-341a-8830-10c5f1a7be03 | -8.42422 | -45.86781 | 2026-09-20 04:40:00 | NOAA-20 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| f5067643-34f5-3677-a75f-ad22e30b2917 | -7.87494 | -44.872 | 2026-09-20 04:40:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| a0eb0898-fdd4-3374-ba12-2a2d197cfeb7 | -9.76722 | -46.06738 | 2026-09-20 04:40:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 43bd8a6d-65ec-349c-a646-9fcac803ce15 | -10.60082 | -46.48383 | 2026-09-20 04:40:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 4a580010-df88-36d1-881a-77133ee3307f | -5.78092 | -57.58258 | 2026-09-20 04:40:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 7e4b3625-7445-3c9d-8b17-11c0f2a69bd1 | -8.04688 | -46.2567 | 2026-09-20 04:40:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| f964abe0-6d83-3528-b4a5-92416c9883bc | -6.66319 | -50.93238 | 2026-09-20 04:40:00 | NOAA-20 | ÁGUA AZUL DO NORTE | PARÁ | Brasil | 1500347 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 9946d8dd-4502-3164-aa16-d8d8a995c956 | -11.7819 | -47.46653 | 2026-09-20 04:40:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 4c0606b5-81ff-3e0c-b50d-2035e75eea08 | -8.25946 | -50.85852 | 2026-09-20 04:40:00 | NOAA-20 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 5d912c9d-34f8-3459-aa9c-268a5392848e | -8.16352 | -54.75417 | 2026-09-20 04:40:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 4befa761-6702-3626-a162-027461c44e2a | -9.73112 | -46.09134 | 2026-09-20 04:40:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 98d128b8-96f8-39d3-a69c-e5bf0a71e9d6 | -11.09373 | -54.0325 | 2026-09-20 04:40:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 27.5 |
| ec1db733-da80-3070-bd6e-ff114b97b993 | -7.88183 | -44.85071 | 2026-09-20 04:40:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 7.3 |
| 2d6de263-dbfe-3637-8e26-843ebd8bd268 | -10.82675 | -50.93214 | 2026-09-20 04:40:00 | NOAA-20 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 0a0cd778-7cc9-35f5-bbd8-4aa2f40e15a5 | -11.44206 | -45.33649 | 2026-09-20 04:40:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 6399b351-e987-38ce-b972-7bed8ed789fb | -8.76127 | -48.66479 | 2026-09-20 04:40:00 | NOAA-20 | GUARAÍ | TOCANTINS | Brasil | 1709302 | 17 | 33 | nan | nan | nan | Amazônia | 7.2 |
| 17a1d529-15a6-3be9-86dc-c291cda19d4c | -7.7647 | -44.88912 | 2026-09-20 04:40:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 6f6e5bb2-8d80-32e1-935f-1ba5a4a0311d | -8.05034 | -46.25723 | 2026-09-20 04:40:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 62d961e5-cd68-3300-84df-9b9fdc3e4b89 | -11.02504 | -54.15604 | 2026-09-20 04:40:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ed437ca9-d229-39fd-8e9d-c11dea71babc | -8.3623 | -47.24989 | 2026-09-20 04:40:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 6e11adb1-06e3-344f-aadd-133de08415ec | -5.83655 | -53.5452 | 2026-09-20 04:40:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 7825a63f-db70-3f3a-9c57-4b0f7c2a2416 | -6.10249 | -57.68785 | 2026-09-20 04:40:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 49835ab0-75de-337c-bde1-e84945407f0a | -11.98185 | -52.47883 | 2026-09-20 04:40:00 | NOAA-20 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 8fee55e9-a14d-3bab-82a3-63aa9807ef72 | -9.21644 | -46.22301 | 2026-09-20 04:40:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 1edaa587-6daa-3f1e-880b-50925deae819 | -13.30908 | -51.77095 | 2026-09-20 04:40:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 2baa523d-2a52-3009-ad20-587610abc948 | -11.85077 | -46.87018 | 2026-09-20 04:40:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 46b7f242-2bbf-30c6-9f49-2408f4001715 | -8.75852 | -48.66079 | 2026-09-20 04:40:00 | NOAA-20 | GUARAÍ | TOCANTINS | Brasil | 1709302 | 17 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 404ecf54-3242-3490-9fcc-4be66e40caeb | -11.87327 | -49.00095 | 2026-09-20 04:40:00 | NOAA-20 | GURUPI | TOCANTINS | Brasil | 1709500 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| ee38d2c0-7b56-3e25-98e2-d1f7ec2b1774 | -11.28384 | -54.05806 | 2026-09-20 04:40:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 8f36af94-a746-372a-83a1-cd28fccf8a12 | -6.75642 | -47.91815 | 2026-09-20 04:40:00 | NOAA-20 | DARCINÓPOLIS | TOCANTINS | Brasil | 1706506 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 9fb003bb-04c4-329b-9da2-f98cb9415ae9 | -5.84205 | -53.51786 | 2026-09-20 04:40:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| ce783e85-497a-348a-9ab1-d294891d9651 | -12.75072 | -45.95461 | 2026-09-20 04:40:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |


[Clique aqui para ver as próximas entradas](README69.md)
