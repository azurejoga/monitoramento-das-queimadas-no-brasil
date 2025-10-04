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

## Dados Diários - Página 121

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 0f58140f-ea9c-3e75-b566-1fd9c467a78d | -14.04287 | -53.92221 | 2025-10-04 05:06:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 5.8 |
| ee076e72-d5de-3f44-8b6d-97e0bea2b216 | -11.87277 | -44.97008 | 2025-10-04 05:06:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 7d18c3b6-9446-33de-bab2-555962be1b1c | -13.33206 | -48.07785 | 2025-10-04 05:06:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 15.4 |
| 08152005-7fe1-391f-9b7b-ff293e21be49 | -11.48883 | -44.98791 | 2025-10-04 05:06:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 1f1f41c4-7a46-37d7-b6fc-8c82685240ae | -9.53012 | -59.38452 | 2025-10-04 05:06:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 90110077-b013-3c1f-b3e6-c05c3b8a9008 | -10.12812 | -52.34851 | 2025-10-04 05:06:00 | NOAA-21 | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 5.0 |
| dedf0582-dcd0-36b1-8273-8931035440ba | -10.29802 | -50.28928 | 2025-10-04 05:06:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 9edd7b9e-4400-3ac7-b17a-ef3cc920b09a | -11.86629 | -44.96997 | 2025-10-04 05:06:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| fb4f83fd-c214-3836-9126-cb6c10153639 | -11.91238 | -46.36501 | 2025-10-04 05:06:00 | NOAA-21 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 56d89a9c-1656-3590-8c9c-d9f0d4918ce3 | -12.04179 | -45.19878 | 2025-10-04 05:06:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 4.0 |
| d78e837d-a583-37a6-9888-b2a821baff11 | -14.88764 | -48.29903 | 2025-10-04 05:06:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 9.7 |
| 64417bb9-d191-3075-b105-f0fcae1ae5d5 | -10.57942 | -48.71104 | 2025-10-04 05:06:00 | NOAA-21 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 1aab1713-7606-3458-9813-a818278aeffc | -11.13465 | -47.8649 | 2025-10-04 05:06:00 | NOAA-21 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 57329b82-20cc-3449-8802-88d91afa335c | -15.23175 | -56.81853 | 2025-10-04 05:06:00 | NOAA-21 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| c26aaa64-b5ae-33cd-8bbb-059bfc60d1c1 | -10.41095 | -56.15401 | 2025-10-04 05:06:00 | NOAA-21 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ef2cc138-7e5a-34dc-b716-c9e06d6b7bfd | -11.9268 | -46.35256 | 2025-10-04 05:06:00 | NOAA-21 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 5.2 |
| c2ea1a33-a7ad-327b-aa85-dbb8d8a565c9 | -12.78953 | -56.95915 | 2025-10-04 05:06:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a6efa1e7-6992-32e7-8245-16fc5d90db5b | -10.05203 | -54.33142 | 2025-10-04 05:06:00 | NOAA-21 | MATUPÁ | MATO GROSSO | Brasil | 5105606 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| b4f97073-d767-3f09-b985-ebeafc287d2d | -11.91342 | -46.36449 | 2025-10-04 05:06:00 | NOAA-21 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 19d1ba64-a602-3bdd-a013-46ac82e8c410 | -13.23877 | -47.83253 | 2025-10-04 05:06:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| cc76556a-ffa0-3a65-b8f4-228eac4493be | -15.66785 | -54.63453 | 2025-10-04 05:06:00 | NOAA-21 | DOM AQUINO | MATO GROSSO | Brasil | 5103601 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 1f80976a-4e6e-330c-b5fd-dcae408dbf3f | -11.08152 | -54.78383 | 2025-10-04 05:06:00 | NOAA-21 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 7d414e80-4454-30c3-932a-fbdc709a2b65 | -13.32655 | -48.10722 | 2025-10-04 05:06:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 6.9 |
| a9a0f802-011a-3b02-b933-ec4bb1846207 | -13.19041 | -50.88149 | 2025-10-04 05:06:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| e76620d3-0a81-30a5-bee4-4472546ada38 | -11.87348 | -49.91445 | 2025-10-04 05:06:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 65b115b8-d47e-358e-888e-7774cc7e8e49 | -13.31394 | -48.13697 | 2025-10-04 05:06:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 983910cc-c3b7-3b58-9e64-44e808751077 | -13.32319 | -47.25521 | 2025-10-04 05:06:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 431053ff-0962-3791-920b-2115014d6d79 | -12.3856 | -54.46038 | 2025-10-04 05:06:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 1ed9e030-1123-3ace-9217-715cf019ef2f | -15.70934 | -46.27696 | 2025-10-04 05:06:00 | NOAA-21 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 1b479956-4490-3cc4-817c-999a71b0bb2a | -13.27816 | -47.21883 | 2025-10-04 05:06:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 7efb7699-28bc-319d-ab1c-ebc7f9606258 | -11.91288 | -46.36896 | 2025-10-04 05:06:00 | NOAA-21 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 8b104277-88b7-3393-850c-1abc4652a685 | -12.07453 | -45.16634 | 2025-10-04 05:06:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| e23c4268-97e3-3e05-836e-9c1fafe9bea9 | -11.92401 | -46.3756 | 2025-10-04 05:06:00 | NOAA-21 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 8.9 |
| 7f71c6f2-f363-3a91-b51b-1c15ff5096f0 | -13.31594 | -47.8038 | 2025-10-04 05:06:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| f7419478-e02f-374d-bcbe-ea096582d1a4 | -13.70717 | -47.33806 | 2025-10-04 05:06:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.5 |
| a974ad01-24c4-3116-bcd2-1e95a8caabe0 | -16.00887 | -50.85782 | 2025-10-04 05:06:00 | NOAA-21 | JUSSARA | GOIÁS | Brasil | 5212204 | 52 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 28b3bcce-9e5b-32fe-bf3e-20890adfb00d | -15.3079 | -46.30988 | 2025-10-04 05:06:00 | NOAA-21 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 2.3 |
| ac2a1211-61da-3fd6-ba22-542769ca179a | -13.13125 | -47.80878 | 2025-10-04 05:06:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 20.8 |
| 90426050-7824-38cd-ad11-9707a2c99803 | -13.3544 | -47.233 | 2025-10-04 05:06:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 72712a7a-3549-3f78-afef-c0dc3c073d26 | -11.80182 | -45.02338 | 2025-10-04 05:06:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 2dbb15a8-0c83-3b9c-ab30-1f2fcebf9b2f | -11.81319 | -56.3441 | 2025-10-04 05:06:00 | NOAA-21 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 9585efbf-c78a-3ade-8351-b0a3b08b22f3 | -11.55781 | -47.67715 | 2025-10-04 05:06:00 | NOAA-21 | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 8.6 |
| 69cec30b-0a8a-362d-ba96-5a5f4f53a2db | -11.49421 | -46.75673 | 2025-10-04 05:06:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 5cdb2ffc-d85d-3825-a975-39b384e5e332 | -13.11096 | -47.91607 | 2025-10-04 05:06:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 7dbac0da-e61b-3e01-9cbf-5e1800886819 | -10.28921 | -50.28802 | 2025-10-04 05:06:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| c57540fe-608c-3625-b989-33daaca906fa | -11.47655 | -45.03901 | 2025-10-04 05:06:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 186eab76-ba47-3068-bdd9-457be612cef4 | -15.53356 | -46.83233 | 2025-10-04 05:06:00 | NOAA-21 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 16dd1f45-1313-3330-b7ba-f058e152138f | -10.44179 | -57.58401 | 2025-10-04 05:06:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 1963b146-d8b0-3680-bfb4-99a89fff1736 | -14.24174 | -46.09337 | 2025-10-04 05:06:00 | NOAA-21 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 5a8965cf-7447-3502-853c-886a27c35ad8 | -10.05323 | -59.36115 | 2025-10-04 05:06:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| d6e7c16e-80e6-36d6-99f3-76c9ffeb0227 | -13.11455 | -47.84108 | 2025-10-04 05:06:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 9c3a5672-5776-3370-956c-f445efcda019 | -13.29796 | -47.81564 | 2025-10-04 05:06:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 2ec1af5a-edfa-3691-b78b-a4d8ebc6a43d | -13.78009 | -47.81411 | 2025-10-04 05:06:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 83b29218-f3ba-3f0a-9756-0530e2aa342b | -14.94554 | -46.87067 | 2025-10-04 05:06:00 | NOAA-21 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 0198b3ae-afba-3dbe-a4fd-6eb2f32e601b | -11.13549 | -47.85812 | 2025-10-04 05:06:00 | NOAA-21 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 9a44aef6-51ba-33c7-84ad-9087b6311575 | -13.12906 | -47.81221 | 2025-10-04 05:06:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 26.1 |
| 91b09758-5190-386a-bdda-1d308a9c8b87 | -15.22287 | -56.80952 | 2025-10-04 05:06:00 | NOAA-21 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 5.9 |
| c36fa222-aa8d-3574-8034-8af385aaebbb | -14.17014 | -49.20571 | 2025-10-04 05:06:00 | NOAA-21 | NOVA IGUAÇU DE GOIÁS | GOIÁS | Brasil | 5214879 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| ae6656a3-a065-3e2c-97f9-9d4483d28136 | -11.24352 | -47.80452 | 2025-10-04 05:06:00 | NOAA-21 | SANTA ROSA DO TOCANTINS | TOCANTINS | Brasil | 1718907 | 17 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 6297c2aa-0674-3835-a4ea-423e575d545b | -11.49821 | -45.01864 | 2025-10-04 05:06:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 512b3c30-6037-3de1-a5b0-03a8dd839f23 | -14.67425 | -48.2738 | 2025-10-04 05:06:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| b1915364-2a12-3166-a72c-00b362876191 | -13.56508 | -47.30021 | 2025-10-04 05:06:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 4485b817-5907-3943-bdc7-8e9d449e6984 | -11.62391 | -45.06878 | 2025-10-04 05:06:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 0a6b611d-524f-3e16-8f14-0b14cdf7a1cb | -15.60386 | -52.48529 | 2025-10-04 05:06:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 706cf25a-2ce9-3a3a-8c5b-91f22b816549 | -13.33192 | -47.62157 | 2025-10-04 05:06:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 6c6a21f3-088b-396d-91a6-12e6163cfaff | -15.23123 | -56.8444 | 2025-10-04 05:06:00 | NOAA-21 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 562d1d8d-c338-3aaf-8fee-a9c64e5941f7 | -9.99953 | -60.0111 | 2025-10-04 05:06:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 12277f38-816e-3a87-9d5f-a5ee4962ac6a | -14.65652 | -48.28556 | 2025-10-04 05:06:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| d20aab84-12cb-3d18-944a-d6612dc691de | -9.20282 | -59.40759 | 2025-10-04 05:06:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 87b5f88f-11e7-32a5-a29f-d663d70301c5 | -12.22776 | -43.77183 | 2025-10-04 05:06:00 | NOAA-21 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 2c938698-3507-3639-a89d-2ec3f9ab1f18 | -13.62858 | -48.67046 | 2025-10-04 05:06:00 | NOAA-21 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 383fc2c1-a8b9-3ca9-81e1-f87af204da84 | -10.36288 | -57.82207 | 2025-10-04 05:06:00 | NOAA-21 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b14230fe-f1e6-379f-bfb6-7a7f87a32ab3 | -11.91621 | -46.73981 | 2025-10-04 05:06:00 | NOAA-21 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| bbbe5251-5243-31e6-a5b7-d9eb2b745eb7 | -11.0058 | -46.67788 | 2025-10-04 05:06:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| da2a81e7-7b86-3196-a8aa-6fb44fe1df82 | -11.50132 | -46.74571 | 2025-10-04 05:06:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| bb731886-ae45-32d6-81bf-f64cd29a56cc | -13.92891 | -48.16959 | 2025-10-04 05:06:00 | NOAA-21 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| fe4419e7-1d6a-36cc-864e-f42421ace8e1 | -13.51277 | -47.27808 | 2025-10-04 05:06:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 9e7dd150-ab34-39ab-902b-afaf93454983 | -10.59976 | -54.34772 | 2025-10-04 05:06:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 5d1ce1c2-07c9-3841-aac5-f9e3d64ad6d7 | -15.35604 | -47.95739 | 2025-10-04 05:06:00 | NOAA-21 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 08cbb763-211f-3f3f-9e47-870b3f27d924 | -13.74074 | -47.95814 | 2025-10-04 05:06:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| efac0d2c-5458-341c-ad8f-5f9523957bac | -13.30414 | -47.57126 | 2025-10-04 05:06:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| d3f34801-806c-300f-9a5f-988861bb039c | -15.98991 | -50.86221 | 2025-10-04 05:06:00 | NOAA-21 | JUSSARA | GOIÁS | Brasil | 5212204 | 52 | 33 | nan | nan | nan | Cerrado | 5.0 |
| ec4d4a66-b55c-3282-91fc-d905773d57f1 | -12.68767 | -47.56595 | 2025-10-04 05:06:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| d259c39d-fd59-3b12-8701-52d9bb4680bd | -13.12234 | -47.8222 | 2025-10-04 05:06:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 963d4d2e-d56e-3b43-adb2-db5405747f7d | -12.03105 | -45.20876 | 2025-10-04 05:06:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 12.6 |
| 12911ea5-b688-31d4-8ba3-ef4fefb6d63f | -11.796 | -45.01762 | 2025-10-04 05:06:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| cec5e14c-f560-354c-924a-aa1600aa26bc | -11.51221 | -45.00917 | 2025-10-04 05:06:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 3.1 |
| edbc913c-639b-3d08-aa80-c8eec1512f91 | -13.12964 | -47.91896 | 2025-10-04 05:06:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| c350019f-165d-3b2e-87ff-9d46b89c445c | -11.26657 | -47.7925 | 2025-10-04 05:06:00 | NOAA-21 | SANTA ROSA DO TOCANTINS | TOCANTINS | Brasil | 1718907 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| c091fa56-de0f-38c4-98d3-df74665a52f0 | -11.8923 | -44.98753 | 2025-10-04 05:06:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 4fa6a16f-4207-3ae9-aedb-4300fc7f07f7 | -10.58368 | -48.71703 | 2025-10-04 05:06:00 | NOAA-21 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 6.6 |
| e4f9d9ae-6aac-3a66-a822-895e4cc5a6f0 | -13.24023 | -47.83755 | 2025-10-04 05:06:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 587bb7c3-7fb2-3448-9685-9aa92ca750d9 | -11.39539 | -55.16577 | 2025-10-04 05:06:00 | NOAA-21 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| cf910e42-1385-3772-a325-10be3c1067c3 | -11.10058 | -49.85334 | 2025-10-04 05:06:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 7bc38218-7882-36c3-8511-65de0fddfec6 | -11.53902 | -47.66964 | 2025-10-04 05:06:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 38e4303b-50d4-3034-879d-213352b2b05d | -14.44506 | -46.11354 | 2025-10-04 05:06:00 | NOAA-21 | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 1115630c-9afc-3230-9caf-12e978a6ac5b | -16.04133 | -51.04846 | 2025-10-04 05:06:00 | NOAA-21 | FAZENDA NOVA | GOIÁS | Brasil | 5207600 | 52 | 33 | nan | nan | nan | Cerrado | 4.8 |
| b7795193-18c0-3248-ab94-c09d48e438d0 | -12.30635 | -55.14809 | 2025-10-04 05:06:00 | NOAA-21 | VERA | MATO GROSSO | Brasil | 5108501 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 23df2588-bae0-3bd2-9324-f421994bde49 | -13.7492 | -48.07038 | 2025-10-04 05:06:00 | NOAA-21 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 0738c4c9-fd40-3fea-9989-ae64d184f759 | -11.96659 | -51.47708 | 2025-10-04 05:06:00 | NOAA-21 | SERRA NOVA DOURADA | MATO GROSSO | Brasil | 5107883 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |


[Clique aqui para ver as próximas entradas](README122.md)
