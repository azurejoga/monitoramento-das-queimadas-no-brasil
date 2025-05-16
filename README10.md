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

## Dados Diários - Página 10

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 5a3c1ce7-6a21-3f4e-b1fc-8a4474724ac3 | -6.65525 | -43.19331 | 2025-05-16 04:55:00 | NOAA-20 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Caatinga | 2.5 |
| a2413141-7ec7-3fd4-82d7-5fa9e75f6d79 | -10.06767 | -48.07858 | 2025-05-16 04:55:00 | NOAA-20 | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 9a76a041-be05-3d27-88b8-c1bd42c3d943 | -9.66694 | -47.5606 | 2025-05-16 04:55:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| a9e4c9ed-19e9-3e01-b984-10d7bceab2b1 | -7.07662 | -44.91766 | 2025-05-16 04:55:00 | NOAA-20 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 5ae30769-1a66-3d32-b8d5-d50c0e6c98cb | -9.29126 | -46.71564 | 2025-05-16 04:55:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 31aa3549-ca40-33db-86e1-e7129ff49a6c | -13.23787 | -56.54473 | 2025-05-16 04:57:00 | NOAA-20 | NOVA MUTUM | MATO GROSSO | Brasil | 5106224 | 51 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 82dc680f-0dbb-3bb4-ac39-63c137ad84b6 | -13.2909 | -47.23171 | 2025-05-16 04:57:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 0.4 |
| b9244b8d-d4f8-3a58-8fdb-be0c892641dd | -10.34432 | -51.69467 | 2025-05-16 04:57:00 | NOAA-20 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| bea61c0b-d8b5-32ea-93db-f33331ab8a9b | -10.66909 | -57.63379 | 2025-05-16 04:57:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 85efb3e3-7549-349a-b607-cde8126902ff | -13.01633 | -53.48014 | 2025-05-16 04:57:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| d905e29e-a445-321f-8749-94a1c8e3f224 | -11.91412 | -54.40461 | 2025-05-16 04:57:00 | NOAA-20 | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| b3c23534-6887-39d6-8316-e352bef14557 | -13.58658 | -47.38188 | 2025-05-16 04:57:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| a9782398-720f-333a-9d21-38a67226e19c | -13.29125 | -47.22898 | 2025-05-16 04:57:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 0.3 |
| 2d54105e-1793-3276-b742-798934ec61a8 | -15.26473 | -51.46647 | 2025-05-16 04:57:00 | NOAA-20 | JUSSARA | GOIÁS | Brasil | 5212204 | 52 | 33 | nan | nan | nan | Cerrado | 5.2 |
| b904e51b-139d-303a-a997-18e0a4f59a0d | -12.62631 | -54.86792 | 2025-05-16 04:57:00 | NOAA-20 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 891b81da-21d5-34e5-883e-1d555a60ef5a | -10.52063 | -59.38506 | 2025-05-16 04:57:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 9f09728d-778c-3fa2-8683-0de85adcdcdc | -11.41689 | -54.33018 | 2025-05-16 04:57:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 5c944716-0273-3590-a817-e4ae44b59318 | -17.25054 | -48.1107 | 2025-05-16 04:57:00 | NOAA-20 | ORIZONA | GOIÁS | Brasil | 5215306 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| dbe52f5f-ca9b-3691-8734-e919cc386cdd | -12.87449 | -55.06109 | 2025-05-16 04:57:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 52ebe33e-d0be-34c7-b73b-4c26eddec0f7 | -11.66304 | -54.95008 | 2025-05-16 04:57:00 | NOAA-20 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| aec6ef94-f890-3647-8b8e-465680fb5bd4 | -13.96238 | -56.79427 | 2025-05-16 04:57:00 | NOAA-20 | DIAMANTINO | MATO GROSSO | Brasil | 5103502 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| ee9d61f9-39f0-3b37-a15e-c169ad7a1045 | -12.44836 | -54.3922 | 2025-05-16 04:57:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f234c16c-39f0-3a97-8f00-de1d839c7441 | -13.04435 | -53.71573 | 2025-05-16 04:57:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| c13fd1aa-fa3f-36fc-9f30-0e87a3916414 | -9.25863 | -60.31461 | 2025-05-16 04:57:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 01da3f94-3fb9-33f0-8c56-ca902ebced99 | -13.04092 | -53.71521 | 2025-05-16 04:57:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 57d66c01-2ad8-3fbe-b348-0423c19d4759 | -14.01664 | -55.13801 | 2025-05-16 04:57:00 | NOAA-20 | SANTA RITA DO TRIVELATO | MATO GROSSO | Brasil | 5107768 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| ce5c75e9-63e1-3680-ae2d-43a5739721a1 | -17.05955 | -45.92215 | 2025-05-16 04:57:00 | NOAA-20 | BRASILÂNDIA DE MINAS | MINAS GERAIS | Brasil | 3108552 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| d3eac87b-70db-3be0-8525-c5b189bd7401 | -14.18304 | -45.47858 | 2025-05-16 04:57:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 72a358aa-a43b-3c98-979e-9fe2a5ed15d9 | -12.45092 | -57.20559 | 2025-05-16 04:57:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 1b9bec9d-f785-33b2-88e8-1bc90cfdb98f | -11.66359 | -54.94656 | 2025-05-16 04:57:00 | NOAA-20 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| f5d0ab1d-269a-341a-ae5c-99fbe9cf27e0 | -15.27189 | -51.47278 | 2025-05-16 04:57:00 | NOAA-20 | JUSSARA | GOIÁS | Brasil | 5212204 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 1ebe28fe-0037-337f-9236-5bff2ede24cd | -15.35513 | -53.08377 | 2025-05-16 04:57:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 7bc09b73-4ff3-3488-94e0-f4bffe00dccf | -13.80164 | -53.29792 | 2025-05-16 04:57:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 649eccb9-3e3c-3804-91fc-7e6db620c1d9 | -13.95788 | -56.80092 | 2025-05-16 04:57:00 | NOAA-20 | DIAMANTINO | MATO GROSSO | Brasil | 5103502 | 51 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 2bcb035a-a7b0-3cb1-a3fc-11ec3cbc7e92 | -15.26543 | -51.46132 | 2025-05-16 04:57:00 | NOAA-20 | JUSSARA | GOIÁS | Brasil | 5212204 | 52 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 3dfcdad5-2004-33a7-9463-5c4bc39962c6 | -13.59352 | -47.37428 | 2025-05-16 04:57:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 03cb802b-57b9-3eb5-b7c1-59cc42a1fad0 | -11.78812 | -47.35826 | 2025-05-16 04:57:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 5a0e2a60-1511-342f-b855-8fa31ecc2fe0 | -14.16668 | -45.46828 | 2025-05-16 04:57:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| c280f101-f1bf-37ae-91c9-852821d72a93 | -11.34918 | -55.0911 | 2025-05-16 04:57:00 | NOAA-20 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| eecc7e40-a511-3798-9d6c-f49804f87121 | -11.96286 | -63.5284 | 2025-05-16 04:57:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 1ba094df-17f6-3d95-b135-49a0e176a8e1 | -13.04412 | -53.71542 | 2025-05-16 04:57:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| d36fb551-4764-3572-9e23-7b847d1aae4d | -12.45431 | -57.20617 | 2025-05-16 04:57:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d5a30d60-07e0-370b-9d7a-b8aee61a62a0 | -11.91357 | -54.40821 | 2025-05-16 04:57:00 | NOAA-20 | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 20296023-6512-3427-98ad-e42269ec1adc | -14.47312 | -56.31853 | 2025-05-16 04:57:00 | NOAA-20 | DIAMANTINO | MATO GROSSO | Brasil | 5103502 | 51 | 33 | nan | nan | nan | Cerrado | 0.1 |
| aa1e3606-23b7-33cb-95bf-571746b7a713 | -15.26866 | -51.46704 | 2025-05-16 04:57:00 | NOAA-20 | JUSSARA | GOIÁS | Brasil | 5212204 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 80881636-e954-34c9-8c0f-f5d7708be878 | -12.16033 | -48.80766 | 2025-05-16 04:57:00 | NOAA-20 | SUCUPIRA | TOCANTINS | Brasil | 1720853 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 7eedc919-5926-3ac0-926c-5b68a2a8b1e6 | -10.68185 | -57.59971 | 2025-05-16 04:57:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 46142d20-ae0f-3736-9d41-c67ec26ece25 | -11.16573 | -48.67541 | 2025-05-16 04:57:00 | NOAA-20 | BREJINHO DE NAZARÉ | TOCANTINS | Brasil | 1703701 | 17 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 7b788391-9607-3dd1-8b97-b515897d0a34 | -13.67282 | -47.96115 | 2025-05-16 04:57:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 7d570eb1-8f4c-321f-b4a3-f32dd47e3b41 | -11.58037 | -47.61698 | 2025-05-16 04:57:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 3d7b96ef-649d-36b9-9c19-bd288caa4061 | -13.96077 | -56.78294 | 2025-05-16 04:57:00 | NOAA-20 | DIAMANTINO | MATO GROSSO | Brasil | 5103502 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| f7b1d291-6fb9-3088-bc2c-ce3341c56374 | -12.26415 | -49.31068 | 2025-05-16 04:57:00 | NOAA-20 | FIGUEIRÓPOLIS | TOCANTINS | Brasil | 1707652 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| c9a30fce-4929-33f3-97d7-0c2dca8ba706 | -11.16515 | -48.67984 | 2025-05-16 04:57:00 | NOAA-20 | BREJINHO DE NAZARÉ | TOCANTINS | Brasil | 1703701 | 17 | 33 | nan | nan | nan | Cerrado | 5.6 |
| bbb26c56-f032-3ed3-9ef6-a2ae50745711 | -11.9405 | -61.99334 | 2025-05-16 04:57:00 | NOAA-20 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 52342078-fab1-39af-92fe-5befeb25a99d | -13.58735 | -47.38252 | 2025-05-16 04:57:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 0da9dcc8-1217-35a8-a978-0c594fcd3613 | -13.38725 | -48.44916 | 2025-05-16 04:57:00 | NOAA-20 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 8eac92df-f4fb-35b8-9541-b349a1ea2e4a | -13.16235 | -53.27458 | 2025-05-16 04:57:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 845f9d8d-1cbc-3ce2-af6c-4bbc8cde65c3 | -11.29425 | -53.97586 | 2025-05-16 04:57:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 3f1b6dcc-c289-324c-9652-fa346ee3185e | -11.57623 | -47.6111 | 2025-05-16 04:57:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 80e62ca9-d213-3c99-a62f-60ebffbf385b | -14.17681 | -45.48199 | 2025-05-16 04:57:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 80ab2100-989a-33d2-aa50-f09e271b4bb6 | -11.55626 | -47.61368 | 2025-05-16 04:57:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| cd13981e-28b9-3d67-afe5-8a5277766c85 | -17.0542 | -45.91729 | 2025-05-16 04:57:00 | NOAA-20 | BRASILÂNDIA DE MINAS | MINAS GERAIS | Brasil | 3108552 | 31 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 3f7e23ef-f185-35d9-b1e2-4475172ac99c | -13.04755 | -53.71595 | 2025-05-16 04:57:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 1526a72a-417f-3546-98db-5270837baaae | -10.24458 | -49.1698 | 2025-05-16 04:57:00 | NOAA-20 | CHAPADA DE AREIA | TOCANTINS | Brasil | 1704600 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 1229fa83-41db-32e3-9c8b-58ac88f4b82e | -12.68326 | -58.12876 | 2025-05-16 04:57:00 | NOAA-20 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 5d73fddd-e3e0-3372-b78b-376ec183cddc | -13.97757 | -56.80022 | 2025-05-16 04:57:00 | NOAA-20 | DIAMANTINO | MATO GROSSO | Brasil | 5103502 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 93f6840a-58f8-3893-9f77-dc79403a8187 | -11.65996 | -54.94967 | 2025-05-16 04:57:00 | NOAA-20 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| da88d427-d558-3b1f-b422-3f3ba08c34d8 | -11.16127 | -48.67477 | 2025-05-16 04:57:00 | NOAA-20 | BREJINHO DE NAZARÉ | TOCANTINS | Brasil | 1703701 | 17 | 33 | nan | nan | nan | Cerrado | 5.6 |
| bcb76432-8a07-3c03-bb8a-82ee55f3df3a | -13.60316 | -47.37177 | 2025-05-16 04:57:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 0.5 |
| e7c2fed1-986c-333a-af63-9195147bc96f | -10.34557 | -51.68612 | 2025-05-16 04:57:00 | NOAA-20 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 9f2b5d84-e3d2-3e94-ab2f-4d6398fdcf7d | -14.8743 | -51.97888 | 2025-05-16 04:57:00 | NOAA-20 | ARAGUAIANA | MATO GROSSO | Brasil | 5101001 | 51 | 33 | nan | nan | nan | Cerrado | 9.5 |
| 3babf298-b2c8-3e38-8824-5d01a960dba6 | -15.00298 | -48.8169 | 2025-05-16 04:57:00 | NOAA-20 | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| e55d4103-86cc-3e49-9020-446b1489e8a4 | -11.96391 | -63.5228 | 2025-05-16 04:57:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 3.8 |
| b2063122-9b69-3fe4-aa19-9cefd25e8a04 | -10.07959 | -54.33029 | 2025-05-16 04:57:00 | NOAA-20 | MATUPÁ | MATO GROSSO | Brasil | 5105606 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 4a37f7e2-d788-3e1a-974e-88c7ac2afead | -14.17774 | -45.47379 | 2025-05-16 04:57:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 2453b5ac-91f6-31d9-9ed7-55e900e957db | -11.78222 | -47.34992 | 2025-05-16 04:57:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 730c5d28-9796-3b38-87a1-25d20443738a | -11.42357 | -54.33125 | 2025-05-16 04:57:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 0ad3be7a-9021-37b2-b5bd-13c43db19bed | -17.2502 | -48.1137 | 2025-05-16 04:57:00 | NOAA-20 | ORIZONA | GOIÁS | Brasil | 5215306 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 1bf9a049-9b6d-3516-bd89-a617724f0d57 | -16.36552 | -57.20803 | 2025-05-16 04:57:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 0.3 |
| 1ba869f5-cae0-3331-9b9c-ef07f4f5b485 | -13.04356 | -53.71923 | 2025-05-16 04:57:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 49524b37-ca22-359a-aa8b-26050bd084ce | -14.01553 | -55.12311 | 2025-05-16 04:57:00 | NOAA-20 | SANTA RITA DO TRIVELATO | MATO GROSSO | Brasil | 5107768 | 51 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 37d2d019-4f92-3532-8cd8-afc5fba3e98d | -12.45709 | -57.21047 | 2025-05-16 04:57:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 555a590e-39d7-36c3-a49c-7e1a6aa3e2a7 | -14.17105 | -45.48127 | 2025-05-16 04:57:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| a6753158-6b63-3070-ae27-c1e9abe1c236 | -11.57206 | -47.6054 | 2025-05-16 04:57:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 5.1 |
| e269cf61-f85e-3266-ab3e-eaa120243a29 | -12.4577 | -57.20675 | 2025-05-16 04:57:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 2b36036c-336a-3c0e-87cd-b138ef48e2e0 | -13.95846 | -56.79732 | 2025-05-16 04:57:00 | NOAA-20 | DIAMANTINO | MATO GROSSO | Brasil | 5103502 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 88882d3b-9747-3520-8fe5-4ad11a52190e | -9.158 | -61.44989 | 2025-05-16 04:57:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| a722c221-f700-3b3d-9fe5-14b7a4e3f468 | -14.16622 | -45.47237 | 2025-05-16 04:57:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 9096a87d-d64b-3585-b866-6a097fc3c8e5 | -13.58765 | -47.38013 | 2025-05-16 04:57:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| d18f716c-a0a7-365e-bd37-ef50e1daeddd | -14.17728 | -45.4779 | 2025-05-16 04:57:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 4d32fd80-3753-3d58-b29e-0a7d55d35a20 | -13.04377 | -53.71953 | 2025-05-16 04:57:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| f5b1b202-2eb1-3823-b87a-741f8f8e63bc | -14.17152 | -45.47718 | 2025-05-16 04:57:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 6d7cf2f6-9867-3531-b86e-bb57ff0a4937 | -15.35452 | -53.08805 | 2025-05-16 04:57:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 99ac6edb-7271-341c-8669-6b91aa34b6f1 | -12.4537 | -57.2099 | 2025-05-16 04:57:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 5d26786b-7557-385a-a624-69858b0fb75f | -12.45492 | -57.20245 | 2025-05-16 04:57:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 3c785f24-0e88-3973-902e-01463a38de4c | -15.7848 | -54.51823 | 2025-05-16 04:57:00 | NOAA-20 | POXORÉU | MATO GROSSO | Brasil | 5107008 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| f02651b9-24bf-3751-8ace-1f0e4cf6e764 | -11.56581 | -47.87458 | 2025-05-16 04:57:00 | NOAA-20 | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 50fcde1f-3e72-333f-a36b-50afd738bfdb | -11.78953 | -47.34708 | 2025-05-16 04:57:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 103dcc51-2cff-3c4e-961b-44d3e31c0425 | -10.24407 | -49.16909 | 2025-05-16 04:57:00 | NOAA-20 | CHAPADA DE AREIA | TOCANTINS | Brasil | 1704600 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 2a4c9dae-712c-39e4-8745-df3069c9cd76 | -9.52826 | -66.43769 | 2025-05-16 04:57:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 3.2 |


[Clique aqui para ver as próximas entradas](README11.md)
