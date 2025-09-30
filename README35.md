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
| 9d8974d8-de3c-36db-8d25-1ddb21dcf3b2 | -13.76533 | -48.31691 | 2025-09-30 03:49:00 | NOAA-20 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 55971fcb-af8d-32cf-a3b2-4b39ff7331fa | -14.71863 | -45.67232 | 2025-09-30 03:49:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 0f2d859a-4fb4-3967-a7b1-468ec65f3901 | -15.26755 | -49.49632 | 2025-09-30 03:49:00 | NOAA-20 | SANTA ISABEL | GOIÁS | Brasil | 5219357 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| abacdc87-7133-365e-b921-964aea264f53 | -17.50439 | -43.47805 | 2025-09-30 03:49:00 | NOAA-20 | OLHOS-D'ÁGUA | MINAS GERAIS | Brasil | 3145455 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 82b9fbf4-03f4-316d-ae90-82ff4a1f5ffc | -17.10217 | -48.57316 | 2025-09-30 03:49:00 | NOAA-20 | VIANÓPOLIS | GOIÁS | Brasil | 5222005 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| c96772c0-a4eb-3a89-a9b6-6eac5605475f | -7.23353 | -46.76187 | 2025-09-30 03:49:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 77ae6db5-39c9-3618-9502-ebc869239814 | -6.38606 | -42.91386 | 2025-09-30 03:49:00 | NOAA-20 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 037866f0-040c-311a-970a-f6797a4964ee | -13.2065 | -50.95936 | 2025-09-30 03:49:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 39.3 |
| 132f72c7-86b7-35f3-9e21-06221e539cd6 | -13.65998 | -44.31437 | 2025-09-30 03:49:00 | NOAA-20 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 7957ac80-70d7-3802-96f7-d189a311875f | -19.84891 | -40.45329 | 2025-09-30 03:49:00 | NOAA-20 | IBIRAÇU | ESPÍRITO SANTO | Brasil | 3202504 | 32 | 33 | nan | nan | nan | Mata Atlântica | 0.3 |
| 49356229-385b-3750-ac8c-667fafe10a6d | -13.37055 | -47.31021 | 2025-09-30 03:49:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| d30b9d8d-3f6c-3b7d-bd78-bc2a8eccddbe | -12.83253 | -47.00399 | 2025-09-30 03:49:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 77103297-0ddb-3665-bf39-cae17ee323dd | -7.50671 | -44.28671 | 2025-09-30 03:49:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 491aff93-a881-3788-8a1c-bc64a9c3e891 | -6.49639 | -44.26728 | 2025-09-30 03:49:00 | NOAA-20 | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 33.8 |
| c666fedc-8ce9-3166-b939-7eab386ee3a6 | -14.51328 | -48.42883 | 2025-09-30 03:49:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 9c9f1d16-bb15-3302-b706-0d014e6f5a5b | -14.59764 | -48.29134 | 2025-09-30 03:49:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| b9d32f15-05ee-3ca7-8fb5-e7fe4a83bbd2 | -14.53454 | -48.26099 | 2025-09-30 03:49:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 6db6cc67-e4ea-35ac-bb3b-2fee73f650a3 | -12.95638 | -48.40487 | 2025-09-30 03:49:00 | NOAA-20 | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 7c3c6cb3-9d38-3114-9584-2b37bbad758e | -14.53583 | -48.23583 | 2025-09-30 03:49:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| b9d7225a-59dc-3927-b6bd-c28f4fbc36df | -14.37931 | -47.14484 | 2025-09-30 03:49:00 | NOAA-20 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| a9e4a308-ecc4-39f0-b74f-86e92bd612e9 | -15.53373 | -47.8695 | 2025-09-30 03:49:00 | NOAA-20 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 94e51b1d-3310-32c3-98fe-968d28ce4f69 | -12.78851 | -46.90045 | 2025-09-30 03:49:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| fa594609-2dec-3c1e-9604-aa7e4b0e43f2 | -15.49258 | -48.55389 | 2025-09-30 03:49:00 | NOAA-20 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 7aa2653a-c996-3869-84eb-391ad9f6e613 | -13.20889 | -50.94302 | 2025-09-30 03:49:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 11.3 |
| 1daad2a7-1834-39c3-a161-6900aeae8289 | -11.80729 | -44.91468 | 2025-09-30 03:49:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 318156b8-c712-31f3-902d-f86e11bedd2b | -6.1032 | -42.66275 | 2025-09-30 03:49:00 | NOAA-20 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 8.0 |
| 0b34ce38-4699-35f8-808b-58ed8e52ab99 | -18.47721 | -43.80205 | 2025-09-30 03:49:00 | NOAA-20 | GOUVEIA | MINAS GERAIS | Brasil | 3127602 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 210250b3-069f-3f94-acf5-958cb032c81d | -6.20604 | -44.21188 | 2025-09-30 03:49:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 3934c2d8-ea8a-3796-8592-b1581c418c3f | -12.83362 | -46.99824 | 2025-09-30 03:49:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 42087b1d-4060-3525-9ccd-0092c10e1aa6 | -13.78113 | -47.9524 | 2025-09-30 03:49:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 5.4 |
| ccba90d0-6097-3254-9144-0b93e1c39715 | -16.38238 | -47.03321 | 2025-09-30 03:49:00 | NOAA-20 | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 0426bed0-4f61-3214-95d4-c4881c537dc9 | -17.73889 | -46.67442 | 2025-09-30 03:49:00 | NOAA-20 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 2.6 |
| db5399d3-c21e-3360-8e35-2bbc3c164e76 | -16.08809 | -48.11173 | 2025-09-30 03:49:00 | NOAA-20 | NOVO GAMA | GOIÁS | Brasil | 5215231 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 157a8a40-eedb-396d-b8fd-c36974f4256a | -12.83648 | -46.98307 | 2025-09-30 03:49:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 4.3 |
| f96e712f-8b71-3e35-ad2b-4154ee96ebe8 | -16.03444 | -48.00023 | 2025-09-30 03:49:00 | NOAA-20 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 7033c458-7030-3750-a47c-d1d87956ea33 | -14.57288 | -48.21912 | 2025-09-30 03:49:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 3060d28b-24a4-35a3-be83-38ac2db44356 | -14.60705 | -48.30056 | 2025-09-30 03:49:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| a94259ab-02cc-369f-b722-71fb6feea378 | -11.80794 | -44.91223 | 2025-09-30 03:49:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 8b76afec-18cf-3acb-b33a-ea74452c6e06 | -6.74296 | -43.36658 | 2025-09-30 03:49:00 | NOAA-20 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 77464386-49bc-36b7-bb41-a5cf9cb2d899 | -12.86997 | -46.95837 | 2025-09-30 03:49:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 765f4e5c-96ea-30d2-a81f-e9654e3ad3b6 | -12.75502 | -46.8689 | 2025-09-30 03:49:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 21ab564c-375e-391a-94c6-7f5075559c78 | -17.75536 | -51.34677 | 2025-09-30 03:49:00 | NOAA-20 | RIO VERDE | GOIÁS | Brasil | 5218805 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 690060ad-c353-3a1c-b5ea-c7328bb9091d | -14.53922 | -48.26573 | 2025-09-30 03:49:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 7b2fc2c2-24e9-3d17-8b3c-59b0ab5cca32 | -14.64111 | -46.96872 | 2025-09-30 03:49:00 | NOAA-20 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 159d05ea-8305-33f0-b0fb-f6258955fc20 | -18.33443 | -41.80206 | 2025-09-30 03:49:00 | NOAA-20 | CAMPANÁRIO | MINAS GERAIS | Brasil | 3110806 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 66320d5d-9618-37ac-9e1e-cd97e970276e | -16.29004 | -44.9277 | 2025-09-30 03:49:00 | NOAA-20 | ICARAÍ DE MINAS | MINAS GERAIS | Brasil | 3130051 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 382334a5-01b4-35ce-87b5-a90f474bfcce | -18.02141 | -44.3703 | 2025-09-30 03:49:00 | NOAA-20 | BUENÓPOLIS | MINAS GERAIS | Brasil | 3109204 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 59175e00-aa67-3ebe-bbc6-dc50cfdd4f9e | -12.83492 | -46.87903 | 2025-09-30 03:49:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| b72fd972-666d-3afe-9471-ada206cfc1fc | -14.51956 | -48.45377 | 2025-09-30 03:49:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 3aad5303-3010-3941-8527-afff57f90e14 | -13.21294 | -50.95575 | 2025-09-30 03:49:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 18.0 |
| 5dfe8203-d259-3c3e-9a86-4155bbfb9884 | -14.79385 | -44.37507 | 2025-09-30 03:49:00 | NOAA-20 | MIRAVÂNIA | MINAS GERAIS | Brasil | 3142254 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| caed369c-6701-3f86-a149-e1a1ca2d8ab7 | -7.0127 | -45.21148 | 2025-09-30 03:49:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 68f60537-0eab-3b25-a41d-83c92f503bd8 | -11.19743 | -47.2317 | 2025-09-30 03:49:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 7f4237a8-9078-3cce-987f-78de7596f71a | -18.5319 | -46.05006 | 2025-09-30 03:49:00 | NOAA-20 | VARJÃO DE MINAS | MINAS GERAIS | Brasil | 3170750 | 31 | 33 | nan | nan | nan | Cerrado | 11.8 |
| 000a51f1-0ae9-3580-9a36-96034171a89f | -6.14946 | -42.79283 | 2025-09-30 03:49:00 | NOAA-20 | ANGICAL DO PIAUÍ | PIAUÍ | Brasil | 2200608 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 85caad4c-7b57-377b-8258-e513f6dfc66a | -11.18464 | -47.2403 | 2025-09-30 03:49:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 01830f92-1143-31b5-ac15-57eb2ce941c6 | -14.17106 | -44.30552 | 2025-09-30 03:49:00 | NOAA-20 | FEIRA DA MATA | BAHIA | Brasil | 2910776 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| c36999d6-631c-32cc-a11a-b9d45f607958 | -12.85766 | -46.88556 | 2025-09-30 03:49:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 8fe10ff4-e811-3dc8-91ba-8af67caeef67 | -13.21003 | -50.94242 | 2025-09-30 03:49:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 23.8 |
| eb67e904-a0cd-363b-8af6-3dd2d8673e9f | -18.46625 | -40.5705 | 2025-09-30 03:49:00 | NOAA-20 | ECOPORANGA | ESPÍRITO SANTO | Brasil | 3202108 | 32 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| cfbce554-2626-340b-8f12-3da691f9a1ea | -15.3939 | -44.97595 | 2025-09-30 03:49:00 | NOAA-20 | JANUÁRIA | MINAS GERAIS | Brasil | 3135209 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 0abee0b2-e3e2-3b03-b461-ba6d648d8a91 | -6.8368 | -44.83496 | 2025-09-30 03:49:00 | NOAA-20 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 7.1 |
| e2a412ae-3f72-34b7-9761-2c82ed5fcc31 | -13.40681 | -47.54061 | 2025-09-30 03:49:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 5.7 |
| cf4c2268-1426-3d0b-a352-e4abe7f46071 | -15.27906 | -48.02901 | 2025-09-30 03:49:00 | NOAA-20 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| b3ada136-61d4-3f8e-92db-cd4e92b816dd | -14.53294 | -48.24991 | 2025-09-30 03:49:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 3cae120d-e395-382f-bca4-5f66857c4163 | -5.70013 | -42.64149 | 2025-09-30 03:49:00 | NOAA-20 | MIGUEL LEÃO | PIAUÍ | Brasil | 2206308 | 22 | 33 | nan | nan | nan | Caatinga | 2.9 |
| e5d24746-9cfb-352b-8a2c-e4315edff6e8 | -18.46686 | -40.56678 | 2025-09-30 03:49:00 | NOAA-20 | ECOPORANGA | ESPÍRITO SANTO | Brasil | 3202108 | 32 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 7de426bd-88d5-3a83-bd68-a8798d4ad618 | -12.92492 | -43.20362 | 2025-09-30 03:49:00 | NOAA-20 | BOM JESUS DA LAPA | BAHIA | Brasil | 2903904 | 29 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 4cbb7a9e-efa6-3948-9a08-ef9a48354d94 | -7.18715 | -41.69762 | 2025-09-30 03:49:00 | NOAA-20 | PAQUETÁ | PIAUÍ | Brasil | 2207553 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| c489a007-87b5-3d33-a602-b12389027822 | -13.23226 | -48.44561 | 2025-09-30 03:49:00 | NOAA-20 | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 115f1bf5-865d-362f-a759-b57cd7145ef2 | -6.53449 | -42.83499 | 2025-09-30 03:49:00 | NOAA-20 | AMARANTE | PIAUÍ | Brasil | 2200509 | 22 | 33 | nan | nan | nan | Caatinga | 4.3 |
| 718079a6-6573-3f88-851d-52683bad4f2f | -14.5942 | -48.16893 | 2025-09-30 03:49:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 49c09705-2b45-3e22-b1c4-ae3b456df39c | -14.53654 | -48.23236 | 2025-09-30 03:49:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 735f528b-e3f0-3b82-9807-4b644c85b1ac | -11.24833 | -47.22718 | 2025-09-30 03:49:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 3bf2f974-9ca8-3c13-b51d-d7a9851a82a3 | -12.95958 | -46.41439 | 2025-09-30 03:49:00 | NOAA-20 | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 4d83b716-a005-3244-bb68-d3f2dc9592f8 | -13.56939 | -48.09841 | 2025-09-30 03:49:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 2af1f66d-5a66-3992-acd0-86d847584bb6 | -14.51493 | -48.44859 | 2025-09-30 03:49:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 8dcaf796-60c1-3563-afc5-aae5c586a9af | -11.72399 | -44.44013 | 2025-09-30 03:49:00 | NOAA-20 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 404ab5f3-2a87-3043-9370-a41e3218b32d | -15.37568 | -47.07423 | 2025-09-30 03:49:00 | NOAA-20 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 57aa072d-ee7a-36ac-9803-039ff2129874 | -6.30461 | -43.81161 | 2025-09-30 03:49:00 | NOAA-20 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 8a3e1247-c8fd-36f3-b317-0bdc228bb10f | -12.75772 | -46.86812 | 2025-09-30 03:49:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 7fc87051-8a67-3e39-9518-fe4472a20dd4 | -13.86043 | -44.41398 | 2025-09-30 03:49:00 | NOAA-20 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 3.4 |
| cb328cfd-7fbc-3840-aaa8-832a50b4da7b | -15.25747 | -49.71648 | 2025-09-30 03:49:00 | NOAA-20 | CERES | GOIÁS | Brasil | 5205406 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| e9ce2231-9bfb-3ef2-bb0c-e04648533d26 | -11.64358 | -47.49156 | 2025-09-30 03:49:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 148635bb-67a8-3a34-9922-7f6ff487fa16 | -5.91177 | -43.91718 | 2025-09-30 03:49:00 | NOAA-20 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 7d586cd1-5282-3846-bc81-3ef6556eee60 | -15.85595 | -46.23021 | 2025-09-30 03:49:00 | NOAA-20 | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 1009ef4e-94b7-3b25-8b35-c8626a9674ab | -12.05279 | -42.95836 | 2025-09-30 03:49:00 | NOAA-20 | OLIVEIRA DOS BREJINHOS | BAHIA | Brasil | 2923209 | 29 | 33 | nan | nan | nan | Caatinga | 1.1 |
| b2a0c127-5cc6-3d3b-b780-1ec329312bea | -13.60389 | -48.03717 | 2025-09-30 03:49:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| aad525a8-636d-3c57-9d42-e788533ffd10 | -14.52145 | -48.38467 | 2025-09-30 03:49:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 9be88579-95b3-35e1-ac53-f4d7ff6fee42 | -14.52595 | -48.47836 | 2025-09-30 03:49:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 11.8 |
| b0dde83d-c610-3bbb-804a-d41dbcd0742e | -14.73403 | -45.66575 | 2025-09-30 03:49:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 23.9 |
| b70df74f-0c09-365b-aa07-0e5aab395f03 | -13.64705 | -48.05307 | 2025-09-30 03:49:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| f94aa5b0-22ef-3d1f-b3c2-a5892591a0bc | -13.70789 | -43.50787 | 2025-09-30 03:49:00 | NOAA-20 | MALHADA | BAHIA | Brasil | 2920205 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| fcd48244-7370-3f88-b0fb-25d7fed1bd3f | -14.5134 | -48.45608 | 2025-09-30 03:49:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 9e50e5fe-bead-367a-a188-810ea919557c | -11.06485 | -47.82858 | 2025-09-30 03:49:00 | NOAA-20 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 6.0 |
| fa553c57-aef2-3aef-b822-fc7fcbd5e984 | -14.56548 | -48.22795 | 2025-09-30 03:49:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| c644f9fa-c716-3381-992d-2229fd2b8504 | -16.99712 | -43.5043 | 2025-09-30 03:49:00 | NOAA-20 | ITACAMBIRA | MINAS GERAIS | Brasil | 3132008 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 0a1418cb-e0b7-3450-861e-c5159bc512a3 | -14.51026 | -48.44358 | 2025-09-30 03:49:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 9eb6cb35-9af8-3816-8a1a-0d75650c72ed | -13.24401 | -48.44508 | 2025-09-30 03:49:00 | NOAA-20 | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| f1ff4c49-ef4b-3b53-b3c9-2991eda9bc1c | -5.76426 | -43.83469 | 2025-09-30 03:49:00 | NOAA-20 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |


[Clique aqui para ver as próximas entradas](README36.md)
