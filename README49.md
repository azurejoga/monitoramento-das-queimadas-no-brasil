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

## Dados Diários - Página 49

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| f63eaca2-fa4f-3820-9e58-274064154eaa | -11.04274 | -51.55809 | 2025-09-27 04:46:00 | NOAA-20 | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 04c00a42-44b8-3fcd-b3e0-80f78f099c6e | -12.84509 | -46.89829 | 2025-09-27 04:46:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| ab2dc00c-32b8-3284-8438-1fd64edd580b | -15.56216 | -47.91628 | 2025-09-27 04:46:00 | NOAA-20 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 92e0dbe9-063b-3532-934b-c72abf22e23f | -11.29322 | -47.80895 | 2025-09-27 04:46:00 | NOAA-20 | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 509be262-2013-356c-9d67-a98fb408bc34 | -12.98743 | -49.43729 | 2025-09-27 04:46:00 | NOAA-20 | ARAGUAÇU | TOCANTINS | Brasil | 1702000 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| d0469ae7-8f25-3b5e-ac81-4a7e6f735dbb | -14.63232 | -48.28695 | 2025-09-27 04:46:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| cfdcc142-6fac-36ba-b7ba-37c7f1c7439e | -11.35725 | -45.01479 | 2025-09-27 04:46:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 75375d0d-9cd8-396e-a889-5c57f1066bb5 | -10.12823 | -45.31152 | 2025-09-27 04:46:00 | NOAA-20 | SÃO GONÇALO DO GURGUÉIA | PIAUÍ | Brasil | 2209757 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 6a622117-1602-3c52-8d36-85d6d92db83b | -11.71251 | -44.41808 | 2025-09-27 04:46:00 | NOAA-20 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 4.3 |
| d055a914-a4a7-31f8-a71e-e3f6001a5533 | -15.92988 | -57.48795 | 2025-09-27 04:46:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 76655332-035e-3af0-af3e-723f3e0752ae | -16.81381 | -48.81026 | 2025-09-27 04:46:00 | NOAA-20 | BELA VISTA DE GOIÁS | GOIÁS | Brasil | 5203302 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| bcd1c339-4a3c-3e1f-9cf6-fb5bc1df0ba1 | -15.26211 | -51.47845 | 2025-09-27 04:46:00 | NOAA-20 | JUSSARA | GOIÁS | Brasil | 5212204 | 52 | 33 | nan | nan | nan | Cerrado | 8.4 |
| 54dcfabc-dffa-3f73-bb8a-778e453039d6 | -12.28532 | -44.05296 | 2025-09-27 04:46:00 | NOAA-20 | TABOCAS DO BREJO VELHO | BAHIA | Brasil | 2930907 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 86ef5827-4bd0-3b4b-84f0-62736b68ecd4 | -11.9446 | -47.86784 | 2025-09-27 04:46:00 | NOAA-20 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 7d024769-612a-3c99-b7af-be94b79d18ae | -14.51788 | -48.01314 | 2025-09-27 04:46:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 6d15b13a-bedf-3662-97c6-f945d69d1d89 | -13.32408 | -47.3076 | 2025-09-27 04:46:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| f92f5f0f-85ad-382b-9d4e-ec742ae3127f | -11.43244 | -44.97975 | 2025-09-27 04:46:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 4.7 |
| c353d093-daba-3d37-8587-6279c152ecc2 | -15.93562 | -57.49219 | 2025-09-27 04:46:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | 9.4 |
| a8a2e37e-a46a-33f5-a4fe-0ce5a543dc64 | -12.06712 | -46.62715 | 2025-09-27 04:46:00 | NOAA-20 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| ff63bf72-d464-3138-9afd-23c9f20670a9 | -11.38016 | -44.98342 | 2025-09-27 04:46:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| b0463ded-24bc-3561-8e8b-849c0c988788 | -11.70697 | -44.42277 | 2025-09-27 04:46:00 | NOAA-20 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 2b214a4e-cf8b-3031-9346-d09e04ccdac6 | -12.48858 | -54.31709 | 2025-09-27 04:46:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 87f360e1-ac48-361f-91c6-006fd92e21c6 | -15.4225 | -48.20678 | 2025-09-27 04:46:00 | NOAA-20 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 3cc03da6-2037-3e51-89b5-91b4aeb41ae7 | -10.88573 | -53.75637 | 2025-09-27 04:46:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 722af9f1-e233-3b99-8cca-9b7e1360e6a2 | -12.64532 | -51.66527 | 2025-09-27 04:46:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| af2699a9-1f4b-336f-9e58-75ee2f86642d | -15.28038 | -46.43033 | 2025-09-27 04:46:00 | NOAA-20 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 60526f20-e689-392b-95e0-9e6852b7e9f2 | -14.5944 | -48.24491 | 2025-09-27 04:46:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 5fd5d216-1d9a-3aa7-8eb4-c98ba7d48e7d | -13.76626 | -47.87298 | 2025-09-27 04:46:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.3 |
| c5fc7c8c-6fee-3509-8e7a-a785c0e35fb0 | -12.64824 | -48.15818 | 2025-09-27 04:46:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 52cf3dc6-6664-33be-bbf9-638e056a7ab6 | -15.27057 | -51.46837 | 2025-09-27 04:46:00 | NOAA-20 | JUSSARA | GOIÁS | Brasil | 5212204 | 52 | 33 | nan | nan | nan | Cerrado | 5.7 |
| b691815a-c7d8-37a4-aaa0-3ace287dd607 | -14.82594 | -45.63116 | 2025-09-27 04:46:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 2cc5e611-dce4-3ba2-b826-793197979fa5 | -10.03543 | -52.08868 | 2025-09-27 04:46:00 | NOAA-20 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 1168b693-8524-3352-b73d-ed3142287529 | -10.12743 | -45.30958 | 2025-09-27 04:46:00 | NOAA-20 | SÃO GONÇALO DO GURGUÉIA | PIAUÍ | Brasil | 2209757 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 3e7cf848-6f42-319a-803a-2b6005e9e862 | -10.23695 | -50.25357 | 2025-09-27 04:46:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 48ef625f-e981-32ae-8e42-fa39a8438fb0 | -15.96754 | -50.87433 | 2025-09-27 04:46:00 | NOAA-20 | JUSSARA | GOIÁS | Brasil | 5212204 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 3af94817-829f-38bb-8cb6-d53ea2db338f | -15.27425 | -46.44319 | 2025-09-27 04:46:00 | NOAA-20 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 7a1345a1-0456-3848-b777-a334f6759752 | -15.41965 | -48.22738 | 2025-09-27 04:46:00 | NOAA-20 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 1c7ab641-b101-3753-b435-c7d92a096d5f | -15.0227 | -46.96515 | 2025-09-27 04:46:00 | NOAA-20 | VILA BOA | GOIÁS | Brasil | 5222203 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 1c830a0c-1c5f-3700-ac7e-08d109ecdd9b | -12.55561 | -45.842 | 2025-09-27 04:46:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 36e01ab6-6f6d-38b0-b083-fd8c8c831d9a | -12.05518 | -48.77105 | 2025-09-27 04:46:00 | NOAA-20 | SUCUPIRA | TOCANTINS | Brasil | 1720853 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 8428e6d5-2e0d-3950-8794-edd54a089ab3 | -9.763 | -48.58937 | 2025-09-27 04:46:00 | NOAA-20 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 271b5c25-fc64-389d-a823-4070cdad7d04 | -10.59751 | -46.28502 | 2025-09-27 04:46:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 5d964093-a68e-38ca-b37d-399bf50bd6ac | -11.43315 | -44.9745 | 2025-09-27 04:46:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 9b832aff-10be-3c06-9ba0-c9f8f7586212 | -9.91333 | -58.56721 | 2025-09-27 04:46:00 | NOAA-20 | COTRIGUAÇU | MATO GROSSO | Brasil | 5103379 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 2dd20fcd-dad1-316c-ad19-255c301da920 | -11.50563 | -47.74988 | 2025-09-27 04:46:00 | NOAA-20 | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 606806c6-1af7-322e-9ea4-500217afa1c3 | -9.8853 | -52.13617 | 2025-09-27 04:46:00 | NOAA-20 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 539609cc-fb9b-3a39-ac93-ccd7eaa1d048 | -14.77731 | -60.18238 | 2025-09-27 04:46:00 | NOAA-20 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 5.6 |
| eb2c12c9-23ae-30d5-9e2b-5b30e2576989 | -13.63504 | -48.07357 | 2025-09-27 04:46:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 4.3 |
| e93f87bc-3a96-3c86-93e9-401909e98ecd | -12.03032 | -47.06756 | 2025-09-27 04:46:00 | NOAA-20 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 4.4 |
| c7b41744-6bdb-34bc-b85d-1aa656758d23 | -15.02221 | -46.96888 | 2025-09-27 04:46:00 | NOAA-20 | VILA BOA | GOIÁS | Brasil | 5222203 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| e4703b31-fee9-3f4f-97cd-ff0004176966 | -11.69802 | -44.41612 | 2025-09-27 04:46:00 | NOAA-20 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| ef74e6b7-4746-3e67-a593-40c75d553020 | -15.00941 | -49.23078 | 2025-09-27 04:46:00 | NOAA-20 | GOIANÉSIA | GOIÁS | Brasil | 5208608 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| c5389424-ca40-356d-8720-bc605c9d4f04 | -15.93186 | -57.49123 | 2025-09-27 04:46:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| c1bbc818-7b70-38ad-815f-f9b9d560f97d | -10.18061 | -49.51468 | 2025-09-27 04:46:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 9fdf4099-3b14-33a0-9cdf-4353d654301e | -12.96425 | -48.91061 | 2025-09-27 04:46:00 | NOAA-20 | PORANGATU | GOIÁS | Brasil | 5218003 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 1ed55301-0e44-37cc-b694-a9f69d2d6a51 | -10.12404 | -45.34103 | 2025-09-27 04:46:00 | NOAA-20 | SÃO GONÇALO DO GURGUÉIA | PIAUÍ | Brasil | 2209757 | 22 | 33 | nan | nan | nan | Cerrado | 8.7 |
| b08f704a-e302-3885-9777-d49ed75b1b0e | -15.57364 | -51.70588 | 2025-09-27 04:46:00 | NOAA-20 | MONTES CLAROS DE GOIÁS | GOIÁS | Brasil | 5213707 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 4ac11225-1766-32b4-bf25-f69754f52897 | -11.99512 | -46.62474 | 2025-09-27 04:46:00 | NOAA-20 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 8f4df913-d484-3433-a8e8-a3f4811130b8 | -12.17272 | -64.10783 | 2025-09-27 04:46:00 | NOAA-20 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 9848ef32-bee3-37a8-993f-c855be3bc584 | -9.85899 | -48.80854 | 2025-09-27 04:46:00 | NOAA-20 | BARROLÂNDIA | TOCANTINS | Brasil | 1703107 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| ea22b310-2bdb-3d2a-ad82-f61edbd8bf63 | -11.96838 | -47.86656 | 2025-09-27 04:46:00 | NOAA-20 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 465f13a9-7639-30b1-988c-b4029baf8074 | -13.37349 | -47.82564 | 2025-09-27 04:46:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 715f7ec5-253a-3507-b361-ddced4bddcca | -10.05527 | -59.36565 | 2025-09-27 04:46:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d89e76fc-9aa6-3573-908e-aba1efedc980 | -10.28905 | -45.21284 | 2025-09-27 04:46:00 | NOAA-20 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 0c8496d0-bf47-3d73-a28b-8fed546472b4 | -11.68831 | -44.45282 | 2025-09-27 04:46:00 | NOAA-20 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| a169d341-aed1-34b0-94f1-3a46b243c589 | -15.19566 | -50.10117 | 2025-09-27 04:46:00 | NOAA-20 | ARAGUAPAZ | GOIÁS | Brasil | 5202155 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| b6b1f824-fede-3367-87ca-89402b420d5c | -10.56671 | -46.26109 | 2025-09-27 04:46:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 5.1 |
| ad5b3131-42bf-346d-bdc3-bc6fce960603 | -15.99981 | -48.76825 | 2025-09-27 04:46:00 | NOAA-20 | CORUMBÁ DE GOIÁS | GOIÁS | Brasil | 5205802 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 26fec46c-933a-3819-9557-b526647ce24c | -10.97434 | -49.56725 | 2025-09-27 04:46:00 | NOAA-20 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| ccd05500-a6e9-30c5-83e2-411ae128dc3e | -15.36813 | -59.17028 | 2025-09-27 04:46:00 | NOAA-20 | VALE DE SÃO DOMINGOS | MATO GROSSO | Brasil | 5108352 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 1548314c-6739-3752-8964-125179503896 | -15.9983 | -48.76536 | 2025-09-27 04:46:00 | NOAA-20 | CORUMBÁ DE GOIÁS | GOIÁS | Brasil | 5205802 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 04bcee21-890a-33db-b643-9bb6c0a6a201 | -11.99154 | -46.60915 | 2025-09-27 04:46:00 | NOAA-20 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| b5565a0a-f042-3910-bb25-d42aee888e89 | -14.63165 | -48.29174 | 2025-09-27 04:46:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 39666d7d-5299-3769-8eff-ab9e032e2ae3 | -17.11593 | -46.8706 | 2025-09-27 04:46:00 | NOAA-20 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| ed1068be-7664-339d-a9bd-8c3b97dc23ba | -9.41355 | -54.6892 | 2025-09-27 04:46:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| e06a107e-0464-3dea-92b7-40513d45d6a0 | -13.75851 | -47.87076 | 2025-09-27 04:46:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 10e5f6fc-4943-34bd-b449-b035791be422 | -10.1202 | -45.32979 | 2025-09-27 04:46:00 | NOAA-20 | SÃO GONÇALO DO GURGUÉIA | PIAUÍ | Brasil | 2209757 | 22 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 42e5f1a0-d7f9-3f4e-978e-d0aeb3bb5685 | -11.3762 | -44.94183 | 2025-09-27 04:46:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 73aa4633-aa08-3e23-9237-26c454f69e05 | -13.51341 | -47.40956 | 2025-09-27 04:46:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 415d8a81-73ae-3f69-a04e-15441f569795 | -11.36312 | -45.0058 | 2025-09-27 04:46:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| da4bfc71-f2cb-3ae8-bedd-d18d97ffbb92 | -12.06294 | -46.62658 | 2025-09-27 04:46:00 | NOAA-20 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 7ee7693a-4f9b-387a-bd84-8fef0207525f | -13.60544 | -47.31199 | 2025-09-27 04:46:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 33d76cd4-a2e5-3c9b-97c4-670e1825b0e3 | -12.02958 | -47.07441 | 2025-09-27 04:46:00 | NOAA-20 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 14.5 |
| 5593e805-67fb-3d75-b523-3f33f9113faa | -12.65475 | -51.67041 | 2025-09-27 04:46:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 3.6 |
| af3d6995-163f-3b9b-b790-6c8eb3827784 | -11.62308 | -44.4309 | 2025-09-27 04:46:00 | NOAA-20 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 79a2272b-fa67-3169-8794-1eca2c52516b | -15.41392 | -48.21058 | 2025-09-27 04:46:00 | NOAA-20 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 4814f194-be76-31e6-8abf-2c219fda12a0 | -15.27594 | -46.42988 | 2025-09-27 04:46:00 | NOAA-20 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 9aa5476d-ca7f-3671-be24-ff44acb03f31 | -15.26922 | -46.44736 | 2025-09-27 04:46:00 | NOAA-20 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| ea93fb3b-83d1-3bbd-b5f2-ece4e2f0bc6a | -12.8688 | -60.20313 | 2025-09-27 04:46:00 | NOAA-20 | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 59a18907-9bdd-3e5c-aedb-18a3acd0b98e | -9.89535 | -49.12579 | 2025-09-27 04:46:00 | NOAA-20 | DIVINÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1707108 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| dae3c498-6a22-3072-be17-d02b0a55dd06 | -10.18145 | -46.93318 | 2025-09-27 04:46:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 0c048088-fcc2-3afe-ac77-d25029d037aa | -13.59886 | -47.29949 | 2025-09-27 04:46:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| bbd754fb-0d26-3c81-b31e-0fcffe4a48bd | -14.05315 | -47.03692 | 2025-09-27 04:46:00 | NOAA-20 | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 59744292-f439-380c-bd07-b4fe387e6f19 | -14.83837 | -45.60718 | 2025-09-27 04:46:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 0.4 |
| fe674bff-1fb9-33c2-946d-972b083286e5 | -10.40174 | -46.14415 | 2025-09-27 04:46:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| e01eb369-1f02-305c-bce8-a6ff33861b4a | -12.65309 | -51.68109 | 2025-09-27 04:46:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 1101f02c-3a39-366b-bbf2-d8ffca114efd | -10.41577 | -46.16629 | 2025-09-27 04:46:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 9cfadc5d-9b51-349f-9f2c-8bd8b213d429 | -15.8984 | -57.48767 | 2025-09-27 04:46:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 3d5b1804-1d06-379f-92f5-d8eddeb6634f | -11.97376 | -47.91169 | 2025-09-27 04:46:00 | NOAA-20 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 8681ba23-351b-3f18-ae22-1ae47760ffe3 | -10.62192 | -53.88972 | 2025-09-27 04:46:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |


[Clique aqui para ver as próximas entradas](README50.md)
