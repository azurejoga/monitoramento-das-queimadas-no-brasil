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

## Dados Diários - Página 8

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 0c31eeaf-0653-34f4-b00e-e8e939e1d980 | -15.5529 | -42.633999 | 2024-09-27 00:32:46 | METOP-B | RIO PARDO DE MINAS | MINAS GERAIS | Brasil | 3155603 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| fd763a30-2f88-39c5-b1d7-be8f4e6be2f0 | -15.555 | -42.643101 | 2024-09-27 00:32:46 | METOP-B | RIO PARDO DE MINAS | MINAS GERAIS | Brasil | 3155603 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 7c6ec18c-ef3b-3e9f-b8c7-2b6ebe18e563 | -16.4958 | -46.958302 | 2024-09-27 00:32:47 | METOP-B | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| fb8d92e2-8e92-3c26-b534-ee26849a377e | -16.679701 | -47.817799 | 2024-09-27 00:32:47 | METOP-B | CRISTALINA | GOIÁS | Brasil | 5206206 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| ead9fc57-7c73-33c5-bad9-3cbf21d02185 | -16.681299 | -47.825298 | 2024-09-27 00:32:47 | METOP-B | CRISTALINA | GOIÁS | Brasil | 5206206 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 1db98aec-04ae-31ef-98e0-3b6d324eca09 | -16.3673 | -49.917801 | 2024-09-27 00:32:59 | METOP-B | ANICUNS | GOIÁS | Brasil | 5201306 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| d1551ce8-9f26-3be3-a1f6-67b11a76beda | -16.369101 | -49.9268 | 2024-09-27 00:32:59 | METOP-B | ANICUNS | GOIÁS | Brasil | 5201306 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| f5898f4f-64b4-3f9b-a9e5-02d46ac54a05 | -14.7865 | -44.163898 | 2024-09-27 00:33:05 | METOP-B | SÃO JOÃO DAS MISSÕES | MINAS GERAIS | Brasil | 3162450 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| c3920069-f0da-32d1-bfdb-d03295971313 | -17.048201 | -56.095001 | 2024-09-27 00:33:07 | METOP-B | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 7c3cfbf6-863f-30c8-a4fa-e80d60d9d007 | -17.052099 | -56.118 | 2024-09-27 00:33:07 | METOP-B | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 6af99c40-a252-3677-8bd1-d966b7e17cc7 | -17.0385 | -56.096802 | 2024-09-27 00:33:07 | METOP-B | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 3704176a-bdd7-31a9-b7a1-6272755a9148 | -17.0424 | -56.119801 | 2024-09-27 00:33:07 | METOP-B | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| b9811557-cf60-3c7b-b54b-4e6cc6e9d20c | -17.0249 | -56.075699 | 2024-09-27 00:33:07 | METOP-B | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 897a5781-020c-3d0e-af54-aae05f5d0460 | -17.0289 | -56.098598 | 2024-09-27 00:33:07 | METOP-B | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 0cc3d06a-c6bb-3ec6-b947-d04b2687e272 | -17.032801 | -56.121601 | 2024-09-27 00:33:07 | METOP-B | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| ed841f5b-3a73-32cb-a6cf-7866c5734cf8 | -17.011299 | -56.0546 | 2024-09-27 00:33:08 | METOP-B | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 4e6b242d-c9f0-3db6-987c-1f29334663de | -17.0152 | -56.0774 | 2024-09-27 00:33:08 | METOP-B | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 8305d2a0-b81a-3d20-a9bc-2d0b13677067 | -17.019199 | -56.1003 | 2024-09-27 00:33:08 | METOP-B | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 3c08b887-d509-3f38-a2b1-c1ce03f80f67 | -17.0231 | -56.123299 | 2024-09-27 00:33:08 | METOP-B | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 12d08d3d-2050-34ad-a9d8-a44f98ca2151 | -17.0016 | -56.0564 | 2024-09-27 00:33:08 | METOP-B | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| c9f371b7-1249-3c4e-a9a6-b54ef9cf42ef | -17.005501 | -56.079201 | 2024-09-27 00:33:08 | METOP-B | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 7943d835-6b3f-35fd-a382-f5ebcd0bb641 | -16.607201 | -54.061199 | 2024-09-27 00:33:08 | METOP-B | PEDRA PRETA | MATO GROSSO | Brasil | 5106372 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 91c2a853-ca4e-30ee-a362-e2ab967f11f5 | -16.610201 | -54.077599 | 2024-09-27 00:33:08 | METOP-B | PEDRA PRETA | MATO GROSSO | Brasil | 5106372 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| f3e6ad53-a02b-3901-a3d4-557865228c46 | -16.1306 | -51.962002 | 2024-09-27 00:33:10 | METOP-B | BOM JARDIM DE GOIÁS | GOIÁS | Brasil | 5203401 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 8be45b8e-523e-39f2-8801-c1865a526e9b | -16.118601 | -51.952301 | 2024-09-27 00:33:10 | METOP-B | BOM JARDIM DE GOIÁS | GOIÁS | Brasil | 5203401 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| d4931730-a033-3eec-bca7-71ebc1903edc | -16.120899 | -51.964001 | 2024-09-27 00:33:10 | METOP-B | BOM JARDIM DE GOIÁS | GOIÁS | Brasil | 5203401 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| a8210a04-e5a9-31ad-81d9-5927433393b1 | -16.127701 | -51.999401 | 2024-09-27 00:33:10 | METOP-B | BOM JARDIM DE GOIÁS | GOIÁS | Brasil | 5203401 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 769894d3-1966-3475-9052-cbf562fab7b9 | -16.101999 | -51.919102 | 2024-09-27 00:33:10 | METOP-B | BOM JARDIM DE GOIÁS | GOIÁS | Brasil | 5203401 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 76cd02ea-019c-39e1-950d-8191ad2d5832 | -16.1043 | -51.930801 | 2024-09-27 00:33:10 | METOP-B | BOM JARDIM DE GOIÁS | GOIÁS | Brasil | 5203401 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 21be7087-f442-3092-94c9-0271a5964bb1 | -16.1066 | -51.942501 | 2024-09-27 00:33:10 | METOP-B | BOM JARDIM DE GOIÁS | GOIÁS | Brasil | 5203401 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 7839c431-2896-3c9c-8837-be89909e233b | -16.1089 | -51.954201 | 2024-09-27 00:33:10 | METOP-B | BOM JARDIM DE GOIÁS | GOIÁS | Brasil | 5203401 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| cc41e5a2-e696-3a29-9b4c-a5714ae5b0b7 | -16.0968 | -51.9445 | 2024-09-27 00:33:10 | METOP-B | BOM JARDIM DE GOIÁS | GOIÁS | Brasil | 5203401 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 20eea57d-20ec-35dc-ab06-54ad44ed6d8c | -16.0991 | -51.9562 | 2024-09-27 00:33:10 | METOP-B | BOM JARDIM DE GOIÁS | GOIÁS | Brasil | 5203401 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 8598c204-8f62-37fb-a0d5-3019c13da6fb | -16.101299 | -51.967999 | 2024-09-27 00:33:10 | METOP-B | BOM JARDIM DE GOIÁS | GOIÁS | Brasil | 5203401 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| e21ccdfa-850f-3800-b940-d66ec73be485 | -16.0893 | -51.958199 | 2024-09-27 00:33:10 | METOP-B | BOM JARDIM DE GOIÁS | GOIÁS | Brasil | 5203401 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 9f1135eb-a603-329d-832f-2b90a3f57a4a | -16.0916 | -51.970001 | 2024-09-27 00:33:10 | METOP-B | BOM JARDIM DE GOIÁS | GOIÁS | Brasil | 5203401 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 8fb1a146-af4d-3bb7-b1d7-84b232f62693 | -14.7112 | -45.501499 | 2024-09-27 00:33:11 | METOP-B | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 5dac2758-02fe-3f99-9d3d-4e649d8bc553 | -14.7128 | -45.508701 | 2024-09-27 00:33:11 | METOP-B | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 248cf4dc-5f70-38c1-a71f-9685dbcf02d1 | -14.7079 | -45.487 | 2024-09-27 00:33:11 | METOP-B | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 79a64428-f9e6-3503-8fd0-90883c11b224 | -14.7096 | -45.494202 | 2024-09-27 00:33:11 | METOP-B | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| fbabd6af-aa99-338d-916d-1215c225ad80 | -15.8675 | -51.396099 | 2024-09-27 00:33:12 | METOP-B | JUSSARA | GOIÁS | Brasil | 5212204 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| f2699abe-b81a-38fb-846c-9558b9e7a572 | -14.8379 | -46.6684 | 2024-09-27 00:33:13 | METOP-B | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| ab2b4c1d-8e01-3be3-9369-5d6caa565aa8 | -15.136 | -48.763599 | 2024-09-27 00:33:15 | METOP-B | VILA PROPÍCIO | GOIÁS | Brasil | 5222302 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 959cd84e-48fc-3d75-bf95-694e9f2752a7 | -15.3482 | -49.831902 | 2024-09-27 00:33:16 | METOP-B | SÃO PATRÍCIO | GOIÁS | Brasil | 5220280 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 1d81a7d6-3ceb-37bc-a494-efa5f39824f3 | -15.35 | -49.840599 | 2024-09-27 00:33:16 | METOP-B | SÃO PATRÍCIO | GOIÁS | Brasil | 5220280 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| eff01a44-b9c4-3365-a266-d6c648436de5 | -13.9729 | -43.8638 | 2024-09-27 00:33:17 | METOP-B | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| f712900a-d857-31db-a535-bfbcbce3369d | -13.2472 | -41.4837 | 2024-09-27 00:33:19 | METOP-B | MUCUGÊ | BAHIA | Brasil | 2921906 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| f553473f-5b35-3aff-846a-8f662b432718 | -13.5276 | -42.5541 | 2024-09-27 00:33:19 | METOP-B | TANQUE NOVO | BAHIA | Brasil | 2931053 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| 7676eff7-8e29-38dd-9a7c-fe1e21e5e2fd | -14.8651 | -48.888901 | 2024-09-27 00:33:20 | METOP-B | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 09e3087c-8de9-362a-be89-8084123ff729 | -14.8537 | -48.883202 | 2024-09-27 00:33:20 | METOP-B | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 142d90f0-563c-3194-ace2-23afbadcd177 | -14.8488 | -48.908901 | 2024-09-27 00:33:21 | METOP-B | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| d2952223-3c43-338d-88ad-c09d31c78849 | -14.1675 | -46.431099 | 2024-09-27 00:33:23 | METOP-B | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 70d67b69-be94-3b01-a751-f539fceaf79b | -14.1691 | -46.438099 | 2024-09-27 00:33:23 | METOP-B | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 22c7a0f4-03bf-3f02-8fde-54a264915044 | -15.0338 | -51.199402 | 2024-09-27 00:33:25 | METOP-B | BRITÂNIA | GOIÁS | Brasil | 5203807 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 985332fa-f70b-315d-a1d5-fabbd34749e0 | -15.0358 | -51.209499 | 2024-09-27 00:33:25 | METOP-B | BRITÂNIA | GOIÁS | Brasil | 5203807 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| dc3896f1-ff6a-3147-a1f5-cf848b65bf86 | -13.4438 | -43.766201 | 2024-09-27 00:33:25 | METOP-B | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 419e25a1-b0a3-3d70-ae09-3d564ebee72d | -13.4457 | -43.774502 | 2024-09-27 00:33:25 | METOP-B | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 14f34646-7ee3-32b9-add1-82606d260f5b | -13.0086 | -42.2019 | 2024-09-27 00:33:26 | METOP-B | RIO DO PIRES | BAHIA | Brasil | 2926905 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| 32f57474-5521-370d-8614-65026562d400 | -14.5833 | -49.1572 | 2024-09-27 00:33:26 | METOP-B | URUAÇU | GOIÁS | Brasil | 5221601 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 96b55517-a323-3073-a471-fcd7ebe390bb | -14.585 | -49.165199 | 2024-09-27 00:33:26 | METOP-B | URUAÇU | GOIÁS | Brasil | 5221601 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 8c269365-0158-3755-a666-e3275d2f8234 | -13.4276 | -44.005699 | 2024-09-27 00:33:26 | METOP-B | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 74c73301-eb86-33ff-81ea-c646cccf7880 | -13.4296 | -44.013901 | 2024-09-27 00:33:26 | METOP-B | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 0bb8c577-d4c7-3a5e-88dc-12898627e83e | -13.4315 | -44.021999 | 2024-09-27 00:33:26 | METOP-B | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| c4817b47-2b47-3d49-ada4-71655e4963e7 | -14.886 | -51.072899 | 2024-09-27 00:33:27 | METOP-B | ARUANÃ | GOIÁS | Brasil | 5202502 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| a4f0601b-fbe6-3af0-b0c9-40a787d0c5a1 | -14.8762 | -51.074902 | 2024-09-27 00:33:27 | METOP-B | ARUANÃ | GOIÁS | Brasil | 5202502 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 21095c98-2cb5-3edb-98f8-59eebc842944 | -14.9305 | -51.447102 | 2024-09-27 00:33:28 | METOP-B | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| d7ec20ae-9d4a-3ee3-9092-9b38f7680856 | -14.9326 | -51.4576 | 2024-09-27 00:33:28 | METOP-B | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| ba95fea9-99a6-31b5-a44a-83fa6366407b | -14.9186 | -51.438702 | 2024-09-27 00:33:28 | METOP-B | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 898889ed-7c63-3d3e-b081-ca584a4862fc | -14.9207 | -51.4492 | 2024-09-27 00:33:28 | METOP-B | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 8902d107-2b34-3cd9-a64c-8cbe017fcf10 | -14.9088 | -51.440701 | 2024-09-27 00:33:28 | METOP-B | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| b0bb6f3a-b865-3405-b711-9909eb70a70c | -14.9109 | -51.451199 | 2024-09-27 00:33:28 | METOP-B | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| ad17166a-9cda-3632-91e9-b0fe0a232d28 | -14.9019 | -51.5079 | 2024-09-27 00:33:28 | METOP-B | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| f6628c47-26ed-3f0b-81ed-84b3f0e523ae | -14.904 | -51.518501 | 2024-09-27 00:33:28 | METOP-B | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 7f8c8816-fb33-369e-b529-0acc8d5a33f7 | -14.8697 | -51.448799 | 2024-09-27 00:33:29 | METOP-B | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| c8fbb2f7-ca12-340c-81d6-ce179f235b30 | -14.8718 | -51.459301 | 2024-09-27 00:33:29 | METOP-B | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 042e012b-2d7e-3916-b70a-f43bac88b8ca | -14.8599 | -51.450901 | 2024-09-27 00:33:29 | METOP-B | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 8f2ec2c5-e2cb-3f84-b92c-ffa7096ee472 | -14.862 | -51.461399 | 2024-09-27 00:33:29 | METOP-B | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 656d0e64-3bf5-3b2d-94a0-aeade795fe00 | -14.8501 | -51.4529 | 2024-09-27 00:33:29 | METOP-B | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 42d9e75a-ccb3-39ca-b5d2-a8139b3390ea | -14.8522 | -51.463402 | 2024-09-27 00:33:29 | METOP-B | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| e3566633-1cb5-36ae-bdc8-b9bb16920142 | -14.8404 | -51.455002 | 2024-09-27 00:33:29 | METOP-B | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 1e318767-c09b-3b30-a768-271074087924 | -12.1478 | -40.839802 | 2024-09-27 00:33:34 | METOP-B | RUY BARBOSA | BAHIA | Brasil | 2927200 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| 7a54a076-a20d-3a36-8a5f-e6cf28ad1c0d | -12.1509 | -40.8526 | 2024-09-27 00:33:34 | METOP-B | RUY BARBOSA | BAHIA | Brasil | 2927200 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| a2d95409-e359-3236-9436-3ac5aaceb3a9 | -12.1412 | -40.855 | 2024-09-27 00:33:34 | METOP-B | RUY BARBOSA | BAHIA | Brasil | 2927200 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| c4383205-9bf7-390e-94e7-6cc8ac76d00c | -13.7308 | -47.576401 | 2024-09-27 00:33:34 | METOP-B | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| cfd0f729-6742-3a06-97f3-dc9d16334cf2 | -13.2251 | -45.632702 | 2024-09-27 00:33:35 | METOP-B | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 49d921b1-6f48-301f-81ca-18af3eaeeb35 | -13.2267 | -45.6399 | 2024-09-27 00:33:35 | METOP-B | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 2e23d637-c085-3176-bb6c-505c9a287143 | -13.2169 | -45.6422 | 2024-09-27 00:33:35 | METOP-B | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 9a909d2f-8d92-3199-81fa-8d96f9464a9e | -13.8071 | -48.116501 | 2024-09-27 00:33:35 | METOP-B | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| be3974bf-f43e-364b-b5c9-bf0e09d6d5f5 | -13.8087 | -48.123798 | 2024-09-27 00:33:35 | METOP-B | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| d183e66b-a7cb-36e9-805c-8816875815ed | -13.287 | -46.3172 | 2024-09-27 00:33:37 | METOP-B | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| d5d49811-1638-3ba9-b4e8-d9502bdb55bf | -13.2626 | -46.300499 | 2024-09-27 00:33:37 | METOP-B | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 07135018-47c8-3218-bcaf-4f5c5ef80f3f | -13.2854 | -46.310101 | 2024-09-27 00:33:37 | METOP-B | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 8ea1053c-032d-399e-800a-ef7759a566eb | -13.2724 | -46.298199 | 2024-09-27 00:33:37 | METOP-B | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 3475c8fd-7d83-3020-a54a-a0b0e1e20a91 | -12.9496 | -45.374802 | 2024-09-27 00:33:39 | METOP-B | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 1a31c9ae-701d-3719-a848-70ba2982e9d8 | -12.9513 | -45.382198 | 2024-09-27 00:33:39 | METOP-B | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 5fe8d3b3-6d46-35a2-a9cc-8fafce065914 | -11.9 | -41.2593 | 2024-09-27 00:33:40 | METOP-B | BONITO | BAHIA | Brasil | 2904050 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| d2bbc739-3d9a-367c-8736-a3428f16799a | -13.4566 | -48.348099 | 2024-09-27 00:33:41 | METOP-B | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| f3f1620d-9f05-3823-8e9a-bf8a6b536f7b | -13.4582 | -48.3554 | 2024-09-27 00:33:41 | METOP-B | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 0df3aace-7330-3303-8fa5-14c1dc42df37 | -14.4137 | -53.262299 | 2024-09-27 00:33:42 | METOP-B | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 8fdcd66e-c42e-36bb-bdab-ee5135b7834f | -14.4163 | -53.2757 | 2024-09-27 00:33:42 | METOP-B | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | nan |


[Clique aqui para ver as próximas entradas](README9.md)
