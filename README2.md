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
| 12168baf-839c-39d5-b5d8-1fa7cdf6c2a9 | -5.91963 | -43.49658 | 2026-05-17 03:57:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 4acd51e1-4144-3618-bf80-fb0ae03f6ff2 | -7.56381 | -40.23022 | 2026-05-17 03:57:00 | NOAA-20 | IPUBI | PERNAMBUCO | Brasil | 2607307 | 26 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 3826123c-15e0-3cb0-9970-ea6f27e81055 | -11.88288 | -43.80715 | 2026-05-17 03:57:00 | NOAA-20 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 31.1 |
| 4586b7a5-3e1c-3929-b307-0c85033f2dd2 | -9.23072 | -46.65078 | 2026-05-17 03:57:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 834bb869-4593-3f55-9269-902ea7878afd | -6.29834 | -43.63404 | 2026-05-17 03:57:00 | NOAA-20 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 3f0e62e0-0b3a-346f-84f8-01eb23895d7c | -9.45797 | -46.11065 | 2026-05-17 03:57:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 4a623387-04b9-3b2a-825f-ace075fe54a5 | -9.44875 | -46.10885 | 2026-05-17 03:57:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 4b703de0-f97e-3e58-80cd-0aeb270a1fcd | -8.09405 | -43.15034 | 2026-05-17 03:57:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 0a9f1e16-ff81-337f-99a5-7285bedb044b | -12.26868 | -43.50539 | 2026-05-17 03:57:00 | NOAA-20 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 8.2 |
| a18165bc-e9d2-3026-8050-c3117a9125b5 | -6.29421 | -43.63337 | 2026-05-17 03:57:00 | NOAA-20 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| a936f413-4fca-3c36-a316-a74cdc4af589 | -12.00873 | -38.83576 | 2026-05-17 03:57:00 | NOAA-20 | SANTANÓPOLIS | BAHIA | Brasil | 2928307 | 29 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 4634ef38-abf4-3242-9add-5a06f5ae8ebd | -9.45416 | -46.11215 | 2026-05-17 03:57:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 4.0 |
| b13ea4b3-ecfb-389d-afe7-82533acb8ad8 | -9.44408 | -46.11523 | 2026-05-17 03:57:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 919a8726-dcde-3b87-a364-231f831dfbe2 | -11.08455 | -48.25079 | 2026-05-17 03:57:00 | NOAA-20 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 1adb62ff-6ce3-3a5c-ae4a-3d8c249a07d1 | -10.46622 | -40.35482 | 2026-05-17 03:57:00 | NOAA-20 | CAMPO FORMOSO | BAHIA | Brasil | 2906006 | 29 | 33 | nan | nan | nan | Caatinga | 1.1 |
| ca914175-92f0-3b1a-8bbe-1400241d90fc | -6.29662 | -43.63314 | 2026-05-17 03:57:00 | NOAA-20 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 507e44bf-e099-3e98-857b-013ac51f40ee | -12.26573 | -43.50011 | 2026-05-17 03:57:00 | NOAA-20 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 4dc435a2-1dd3-32a9-b33b-b0f26c018fd2 | -9.45502 | -46.10721 | 2026-05-17 03:57:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 7a81a9ba-4521-333e-af7b-f223bb90511b | -9.91552 | -37.09846 | 2026-05-17 03:57:00 | NOAA-20 | TRAIPU | ALAGOAS | Brasil | 2709202 | 27 | 33 | nan | nan | nan | Mata Atlântica | 3.0 |
| 4f5426ae-d674-34c4-8f24-9c9a844cb64e | -8.72144 | -48.32573 | 2026-05-17 03:57:00 | NOAA-20 | GUARAÍ | TOCANTINS | Brasil | 1709302 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| b64e5ed5-81dd-39b5-8867-f0047e7a02a8 | -9.78597 | -48.07915 | 2026-05-17 03:57:00 | NOAA-20 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 71763756-0fa6-3ceb-b4a8-648beecc9ca7 | -9.44787 | -46.11367 | 2026-05-17 03:57:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 1096727f-08d8-3784-8b45-fd59ab0b0c90 | -5.91552 | -43.4959 | 2026-05-17 03:57:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| b826fea9-cf55-3b12-8d2f-cf9822dea324 | -11.04529 | -49.59927 | 2026-05-17 03:57:00 | NOAA-20 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 66df9c35-dc53-3904-950d-1a66d5456f0c | -11.07935 | -48.24992 | 2026-05-17 03:57:00 | NOAA-20 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 0.3 |
| a9052d8b-2248-3bbd-8799-7663f7da93f9 | -8.85638 | -50.21202 | 2026-05-17 03:57:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| b075ef23-2ec4-396d-b0f8-88159f192f25 | -9.44148 | -46.12251 | 2026-05-17 03:57:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 90b842ba-5c4f-3371-a91a-b3a8cbf9fa0a | -11.6129 | -47.1002 | 2026-05-17 03:57:00 | NOAA-20 | PORTO ALEGRE DO TOCANTINS | TOCANTINS | Brasil | 1718006 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 85ec2053-31d6-357f-9ac6-7f955f58a32b | -11.87822 | -43.81129 | 2026-05-17 03:57:00 | NOAA-20 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| ea88b012-ad83-3e86-ae6c-661dbc2be088 | -12.2679 | -43.50997 | 2026-05-17 03:57:00 | NOAA-20 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 8.2 |
| 43394fb7-4990-3a35-be89-a4a1cbaaddc4 | -9.22628 | -46.65395 | 2026-05-17 03:57:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 51d92fb8-98cb-3d22-8d67-52735dc47934 | -12.13393 | -39.76713 | 2026-05-17 03:57:00 | NOAA-20 | IPIRÁ | BAHIA | Brasil | 2914000 | 29 | 33 | nan | nan | nan | Caatinga | 3.8 |
| 66a12e20-aa4b-3825-84ce-7c5095f76f4e | -8.84036 | -37.03312 | 2026-05-17 03:57:00 | NOAA-20 | BUÍQUE | PERNAMBUCO | Brasil | 2602803 | 26 | 33 | nan | nan | nan | Caatinga | 0.8 |
| a02d0832-c9ae-3895-88f7-cbaa72d11c22 | -8.10101 | -43.15662 | 2026-05-17 03:57:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 1e35da2d-cd0b-3d64-91ab-6606a68cbf56 | -11.54529 | -48.27352 | 2026-05-17 03:57:00 | NOAA-20 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| ab986225-9280-3179-977b-50290840f7f9 | -9.44324 | -46.1129 | 2026-05-17 03:57:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 3af72489-0658-3e73-b579-aeb40e47791a | -8.45498 | -46.42231 | 2026-05-17 03:57:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 016f0ab7-4578-32ee-b402-faf95f4930ea | -9.44492 | -46.1104 | 2026-05-17 03:57:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| fa283068-4908-30db-a73f-d5fefa8ee4b5 | -9.45427 | -46.10477 | 2026-05-17 03:57:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 33857d61-b30b-3ed7-be4d-da38ba0d9b63 | -11.54015 | -48.27252 | 2026-05-17 03:57:00 | NOAA-20 | SANTA ROSA DO TOCANTINS | TOCANTINS | Brasil | 1718907 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| d08b6929-6aff-3580-916f-3eabe25fea53 | -11.8262 | -38.26432 | 2026-05-17 03:57:00 | NOAA-20 | APORÁ | BAHIA | Brasil | 2901908 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 03d069d0-d721-3bd5-bbaa-3453a8ad60ca | -9.46719 | -46.11245 | 2026-05-17 03:57:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| be661ee7-9677-3547-acb6-65a90d18056d | -11.03057 | -48.93248 | 2026-05-17 03:57:00 | NOAA-20 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 6548c530-0329-3fda-aecb-6f7f2eb87f0a | -9.46631 | -46.11728 | 2026-05-17 03:57:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 77b0ecf1-1a16-31ba-84eb-867567dda8f5 | -9.45337 | -46.1097 | 2026-05-17 03:57:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 3e2d54f7-81f6-3117-b3ee-4b79f722270d | -9.22721 | -46.64866 | 2026-05-17 03:57:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 391a9cc7-7d3c-3ae4-a82a-9d2bccaafe4b | -10.97565 | -44.86986 | 2026-05-17 03:57:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 4e49a580-8fd2-3c8b-8dae-ba03dedf85b3 | -10.97746 | -44.86995 | 2026-05-17 03:57:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| e6774b8f-a191-32ee-a569-ec64d4e1e5e8 | -9.7912 | -48.08023 | 2026-05-17 03:57:00 | NOAA-20 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 35defe25-554a-36f2-a48b-31e15b3d1dc8 | -8.72267 | -48.3256 | 2026-05-17 03:57:00 | NOAA-20 | GUARAÍ | TOCANTINS | Brasil | 1709302 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 7e0a3a03-0f9d-318e-80bd-d14444229cf1 | -10.98045 | -45.09411 | 2026-05-17 03:57:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 639ca69f-15f8-3eca-b28f-fedd1572735b | -5.9114 | -43.49522 | 2026-05-17 03:57:00 | NOAA-20 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| acc51444-29d8-3278-9e69-01050f4866ff | -9.44239 | -46.12487 | 2026-05-17 03:57:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 11baf118-f883-3473-9f16-ab4096a6350f | -12.26416 | -43.50928 | 2026-05-17 03:57:00 | NOAA-20 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 15.3 |
| 92496757-9022-35f4-b6bd-a72df1bd00c4 | -9.44954 | -46.11124 | 2026-05-17 03:57:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| e528a3d7-4ff6-3251-81d1-43469f636b04 | -10.40395 | -44.938 | 2026-05-17 03:57:00 | NOAA-20 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 185bb898-a495-36e4-a8b6-785177df2b7a | -11.42809 | -39.07547 | 2026-05-17 03:57:00 | NOAA-20 | BARROCAS | BAHIA | Brasil | 2903276 | 29 | 33 | nan | nan | nan | Caatinga | 0.7 |
| a751facc-d086-35a1-ba10-99d8bae9df29 | -9.4718 | -46.11332 | 2026-05-17 03:57:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 49992e6a-8ad4-3f50-94b7-d6f385c01f75 | -12.92996 | -43.61946 | 2026-05-17 03:57:00 | NOAA-20 | SÍTIO DO MATO | BAHIA | Brasil | 2930758 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 58c6a642-a43f-37b4-b225-dd685c83f9a0 | -12.04194 | -45.28527 | 2026-05-17 03:57:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 07d1a72b-4d58-3e35-a17b-5a5fee2586ae | -9.4504 | -46.10636 | 2026-05-17 03:57:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 4a65b431-625d-34cf-a511-70920b1e4e6e | -12.26494 | -43.5047 | 2026-05-17 03:57:00 | NOAA-20 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 15.3 |
| c411c98e-e1cc-337e-95fb-4c83729394b1 | -9.44236 | -46.11771 | 2026-05-17 03:57:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 9675bb82-6277-338b-94c8-8607fcf97d18 | -6.30075 | -43.63382 | 2026-05-17 03:57:00 | NOAA-20 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| c42bb991-9512-3d0a-b15c-284c7ece4192 | -14.15303 | -52.89017 | 2026-05-17 04:00:00 | NOAA-20 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| a520bd97-b405-341e-bfd2-e7831b1f839a | -17.5681 | -44.95052 | 2026-05-17 04:00:00 | NOAA-20 | VÁRZEA DA PALMA | MINAS GERAIS | Brasil | 3170800 | 31 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 414d5d1e-8e90-367f-80a5-d983bd4b01a9 | -17.56519 | -44.94505 | 2026-05-17 04:00:00 | NOAA-20 | VÁRZEA DA PALMA | MINAS GERAIS | Brasil | 3170800 | 31 | 33 | nan | nan | nan | Cerrado | 4.5 |
| d00d2531-b3ae-3292-b00e-06f43f3fc5fd | -17.35197 | -47.81367 | 2026-05-17 04:00:00 | NOAA-20 | CAMPO ALEGRE DE GOIÁS | GOIÁS | Brasil | 5204805 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| ccdf5435-cb87-37b0-9bfa-0f5aeeaa8b33 | -13.3993 | -46.60872 | 2026-05-17 04:00:00 | NOAA-20 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 0a182d90-8299-35bf-952c-ba0addfeeade | -18.84613 | -40.09779 | 2026-05-17 04:00:00 | NOAA-20 | JAGUARÉ | ESPÍRITO SANTO | Brasil | 3203056 | 32 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 110ef367-7a85-326e-8ce7-fe0c35cba0db | -14.30574 | -49.24825 | 2026-05-17 04:00:00 | NOAA-20 | NOVA IGUAÇU DE GOIÁS | GOIÁS | Brasil | 5214879 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 377ab575-7eac-3060-be76-dedf3c1be740 | -14.16193 | -52.88076 | 2026-05-17 04:00:00 | NOAA-20 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| e6c2e714-ff8c-3097-a052-ce963fc69d67 | -17.56895 | -44.94578 | 2026-05-17 04:00:00 | NOAA-20 | VÁRZEA DA PALMA | MINAS GERAIS | Brasil | 3170800 | 31 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 9249f2a7-bbf1-3b65-a634-477246aa9be8 | -16.04727 | -47.23507 | 2026-05-17 04:00:00 | NOAA-20 | CABECEIRA GRANDE | MINAS GERAIS | Brasil | 3109451 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 8c35d954-0554-3d61-95b0-d510309bf84c | -16.05258 | -47.23131 | 2026-05-17 04:00:00 | NOAA-20 | CABECEIRA GRANDE | MINAS GERAIS | Brasil | 3109451 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 995ab14a-3148-3db6-a606-ed8e7d24a79d | -17.56979 | -44.94106 | 2026-05-17 04:00:00 | NOAA-20 | VÁRZEA DA PALMA | MINAS GERAIS | Brasil | 3170800 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| d3ef9ec7-244d-3d2b-b5a4-c840a48c8963 | -16.04903 | -47.22576 | 2026-05-17 04:00:00 | NOAA-20 | CABECEIRA GRANDE | MINAS GERAIS | Brasil | 3109451 | 31 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 9b48ca6e-f11d-3dd0-a28e-6f3b36c7e6e6 | -18.86298 | -41.97982 | 2026-05-17 04:00:00 | NOAA-20 | GOVERNADOR VALADARES | MINAS GERAIS | Brasil | 3127701 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 51d4ebf6-3b83-34f5-9064-8cab85285ba5 | -14.15591 | -52.88249 | 2026-05-17 04:00:00 | NOAA-20 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 79cdcda9-065e-38f4-8dd8-905ab90da663 | -14.16126 | -52.88942 | 2026-05-17 04:00:00 | NOAA-20 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 54159004-5f95-3aa2-b582-fa1bdcb579f4 | -13.40101 | -46.59959 | 2026-05-17 04:00:00 | NOAA-20 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 3ae708ff-09ee-3472-b693-133619ba71c4 | -16.04815 | -47.23043 | 2026-05-17 04:00:00 | NOAA-20 | CABECEIRA GRANDE | MINAS GERAIS | Brasil | 3109451 | 31 | 33 | nan | nan | nan | Cerrado | 2.8 |
| eb251320-e5f6-3b05-bf31-6ff500e3be09 | -13.40015 | -46.60416 | 2026-05-17 04:00:00 | NOAA-20 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| ca0cbeef-a2e4-3e93-abe6-93504a234d6f | -16.05346 | -47.22666 | 2026-05-17 04:00:00 | NOAA-20 | CABECEIRA GRANDE | MINAS GERAIS | Brasil | 3109451 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 5eda6167-4803-337d-ae98-645cee92a0c1 | -14.15425 | -52.88462 | 2026-05-17 04:00:00 | NOAA-20 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 0f0bf7cc-773e-39b6-80c7-cb7e8d17d9b6 | -14.16076 | -52.88606 | 2026-05-17 04:00:00 | NOAA-20 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| fae63d3e-526e-37bb-8c57-ec8a86528bf8 | -16.04373 | -47.22954 | 2026-05-17 04:00:00 | NOAA-20 | CABECEIRA GRANDE | MINAS GERAIS | Brasil | 3109451 | 31 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 78134661-53c4-34eb-b9ac-748667c9ee50 | -14.16242 | -52.88399 | 2026-05-17 04:00:00 | NOAA-20 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| bef45825-65ca-3f25-9155-4912af4e46af | -17.58021 | -44.94798 | 2026-05-17 04:00:00 | NOAA-20 | VÁRZEA DA PALMA | MINAS GERAIS | Brasil | 3170800 | 31 | 33 | nan | nan | nan | Cerrado | 3.1 |
| d030d985-d69f-3b98-89b7-ee994aaeeb32 | -14.48784 | -47.07497 | 2026-05-17 04:00:00 | NOAA-20 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 4f08a772-2d8e-313a-8272-4f1a55306d25 | -17.56435 | -44.94979 | 2026-05-17 04:00:00 | NOAA-20 | VÁRZEA DA PALMA | MINAS GERAIS | Brasil | 3170800 | 31 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 77a7256a-0f76-385b-94a9-017a69fd48b4 | -17.56603 | -44.94034 | 2026-05-17 04:00:00 | NOAA-20 | VÁRZEA DA PALMA | MINAS GERAIS | Brasil | 3170800 | 31 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 5eb5b8d2-e095-3c5d-8e49-6a04a2e135c5 | -20.08572 | -40.20096 | 2026-05-17 04:00:00 | NOAA-20 | SERRA | ESPÍRITO SANTO | Brasil | 3205002 | 32 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| afde9e1c-ebfc-328e-829b-fd1c36313626 | -16.04461 | -47.22488 | 2026-05-17 04:00:00 | NOAA-20 | CABECEIRA GRANDE | MINAS GERAIS | Brasil | 3109451 | 31 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 13a58f02-6c98-3fe4-adc4-41dd3b3205cf | -16.04284 | -47.23419 | 2026-05-17 04:00:00 | NOAA-20 | CABECEIRA GRANDE | MINAS GERAIS | Brasil | 3109451 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 1918eb0a-f23c-3143-a139-03036d5ced58 | -14.15476 | -52.88787 | 2026-05-17 04:00:00 | NOAA-20 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| befe2f6c-30cb-3d2f-9911-ea49f5784f50 | -14.27153 | -43.42044 | 2026-05-17 04:00:00 | NOAA-20 | IUIU | BAHIA | Brasil | 2917334 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 5abefcdf-12a8-3fa6-952f-e238392d2e45 | -16.58766 | -39.59138 | 2026-05-17 04:00:00 | NOAA-20 | ITABELA | BAHIA | Brasil | 2914653 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| f3f3177c-176d-3d37-939b-dce627bda92f | -17.56144 | -44.94432 | 2026-05-17 04:00:00 | NOAA-20 | VÁRZEA DA PALMA | MINAS GERAIS | Brasil | 3170800 | 31 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 6aefafe6-534e-33b8-8623-ec29f0214ccb | -14.27163 | -43.42282 | 2026-05-17 04:00:00 | NOAA-20 | IUIU | BAHIA | Brasil | 2917334 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |


[Clique aqui para ver as próximas entradas](README3.md)
