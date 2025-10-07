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

## Dados Diários - Página 93

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 2c67a8f7-3e4b-355d-aac1-1e960400790d | -15.55593 | -46.82611 | 2025-10-07 04:57:00 | NOAA-20 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 378ebf72-f8cd-31bf-b847-ebd4accfb8fb | -15.3596 | -47.32469 | 2025-10-07 04:57:00 | NOAA-20 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| d95510cc-453b-398b-bc83-62417487ce91 | -12.21065 | -44.25759 | 2025-10-07 04:57:00 | NOAA-20 | CRISTÓPOLIS | BAHIA | Brasil | 2909703 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 75afabf6-cf3f-3161-befa-5bd6cc58d60e | -8.15774 | -62.83424 | 2025-10-07 04:57:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 127e5a93-0b4a-39a4-93ed-da74dcc4b72d | -13.39744 | -47.59926 | 2025-10-07 04:57:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 1af2a9c2-eaa5-35ed-ae84-bdfd15e852ef | -10.3743 | -50.29515 | 2025-10-07 04:57:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 7.6 |
| 00e939bd-23c8-3429-9344-aa18fe331a18 | -14.73416 | -46.02298 | 2025-10-07 04:57:00 | NOAA-20 | SÍTIO D'ABADIA | GOIÁS | Brasil | 5220702 | 52 | 33 | nan | nan | nan | Cerrado | 12.2 |
| 356e069c-b0b5-31e8-90dd-be260892639c | -14.75933 | -46.04901 | 2025-10-07 04:57:00 | NOAA-20 | SÍTIO D'ABADIA | GOIÁS | Brasil | 5220702 | 52 | 33 | nan | nan | nan | Cerrado | 3.7 |
| b8281845-f494-338d-ba8a-cf6d0a6ff059 | -11.86995 | -56.89023 | 2025-10-07 04:57:00 | NOAA-20 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 5ef02bd2-4ca2-36e8-aa1e-8e542fc018bf | -10.89738 | -51.05104 | 2025-10-07 04:57:00 | NOAA-20 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 458b6ff9-b0b4-3d73-aaee-018809245d5b | -9.33284 | -54.52002 | 2025-10-07 04:57:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 2f39d739-e60b-3e27-bc8e-f8bfe582254d | -10.40321 | -45.38049 | 2025-10-07 04:57:00 | NOAA-20 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 6a59831d-8285-36b8-be94-8b9c7d5c82bf | -11.944 | -51.48282 | 2025-10-07 04:57:00 | NOAA-20 | SERRA NOVA DOURADA | MATO GROSSO | Brasil | 5107883 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 1ef62a38-404e-31c1-99de-ee094d3f79ab | -13.0265 | -51.02804 | 2025-10-07 04:57:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 16b6a216-54b8-379b-917e-713a7cf66b76 | -10.1797 | -45.53924 | 2025-10-07 04:57:00 | NOAA-20 | SÃO GONÇALO DO GURGUÉIA | PIAUÍ | Brasil | 2209757 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 80f1e734-593f-39f5-a60a-e143249d3b9f | -9.39728 | -61.44297 | 2025-10-07 04:57:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 27901f01-a8f1-30dd-8277-6fafefef379e | -9.18152 | -47.83775 | 2025-10-07 04:57:00 | NOAA-20 | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 6047f37d-1b31-3d72-977b-56ffe60a3e1b | -8.61927 | -54.99418 | 2025-10-07 04:57:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 933f3602-e46c-3015-a847-32f25f318675 | -11.7447 | -51.49827 | 2025-10-07 04:57:00 | NOAA-20 | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 3b08b4bb-e1be-3ff6-b5f1-b037b979b5c8 | -13.72543 | -48.19726 | 2025-10-07 04:57:00 | NOAA-20 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 71cfb187-cec0-3bab-bc23-6079a2197592 | -12.6159 | -44.75356 | 2025-10-07 04:57:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| da80e34d-5173-3fc1-b751-ecd325b6611b | -15.76289 | -47.77533 | 2025-10-07 04:57:00 | NOAA-20 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 956ccd2d-6f04-3dc3-9bfc-9f2aae5a8941 | -8.52459 | -48.23306 | 2025-10-07 04:57:00 | NOAA-20 | TUPIRATINS | TOCANTINS | Brasil | 1721307 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 3d950fc7-e7ff-324b-b6a0-7247e106105d | -10.73333 | -56.5936 | 2025-10-07 04:57:00 | NOAA-20 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| e70799bb-abfa-3aed-832d-6a351dabf43f | -9.91188 | -58.56464 | 2025-10-07 04:57:00 | NOAA-20 | COTRIGUAÇU | MATO GROSSO | Brasil | 5103379 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b24e64de-14c6-37da-87d4-c1baed6c1963 | -15.60506 | -47.28992 | 2025-10-07 04:57:00 | NOAA-20 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 8.6 |
| 528cca70-8411-3808-98d9-85862bc27cb0 | -9.12647 | -61.85286 | 2025-10-07 04:57:00 | NOAA-20 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c2946d83-0033-3218-a9c0-f74f50abc940 | -11.15382 | -54.88294 | 2025-10-07 04:57:00 | NOAA-20 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| f166caa4-2ddb-3998-9941-b8942580c522 | -13.50148 | -43.6784 | 2025-10-07 04:57:00 | NOAA-20 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 18.7 |
| 0bd6b209-3316-3e10-a653-8842dd02c564 | -12.02006 | -47.7832 | 2025-10-07 04:57:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| afffcffc-fabf-3fcb-8043-292d80b7f340 | -10.91817 | -47.07264 | 2025-10-07 04:57:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 6.8 |
| fb9b29bd-bb9d-3e54-8171-135358b14e4c | -10.61071 | -48.68334 | 2025-10-07 04:57:00 | NOAA-20 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 292375ac-38e6-31a3-a012-fe2d6813f8ac | -10.81201 | -56.23801 | 2025-10-07 04:57:00 | NOAA-20 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 7db75eb5-f8ed-3d10-9ddf-8a5bad689605 | -9.09303 | -47.96293 | 2025-10-07 04:57:00 | NOAA-20 | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 2587ec90-4739-324e-944b-a324e2db0010 | -7.80746 | -61.50575 | 2025-10-07 04:57:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 19f0183d-9a56-3517-a153-9a64aa633260 | -12.91563 | -54.73005 | 2025-10-07 04:57:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 567343f0-30cf-38a4-a9d8-09623acebf1c | -10.81015 | -48.60292 | 2025-10-07 04:57:00 | NOAA-20 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 229dce87-c266-3b7e-8af1-50c8f4d76066 | -11.29089 | -49.99232 | 2025-10-07 04:57:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| f4c0eefb-e44a-364c-af5b-996b78c02c46 | -8.62039 | -54.96577 | 2025-10-07 04:57:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| e038fa4c-3f81-3e60-bc3e-e65d62c7eebe | -13.57656 | -51.80726 | 2025-10-07 04:57:00 | NOAA-20 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| d6e2cfbd-b547-332e-bd04-4a5abfb8af1e | -10.0369 | -48.28733 | 2025-10-07 04:57:00 | NOAA-20 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| a12da495-270d-3212-aeb6-111c0d329f01 | -14.96372 | -49.95085 | 2025-10-07 04:57:00 | NOAA-20 | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 3.6 |
| cd2a51a2-254d-3299-a012-dbb9bad8b3f3 | -11.80872 | -45.13195 | 2025-10-07 04:57:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 8afdd227-5b6b-37ed-93b3-931d5cafd24b | -11.80916 | -45.12847 | 2025-10-07 04:57:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| f5b10634-30dc-3459-9cde-c2e1c461840a | -13.67488 | -47.33628 | 2025-10-07 04:57:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 7d8c7469-9889-3a39-bd47-5181109ad90e | -9.38395 | -59.42468 | 2025-10-07 04:57:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 2c4b2f66-b691-347f-8ab4-7d8d76c2ec6f | -14.77466 | -46.06239 | 2025-10-07 04:57:00 | NOAA-20 | SÍTIO D'ABADIA | GOIÁS | Brasil | 5220702 | 52 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 199b0fdf-9763-3fc7-bf4f-46b365469ac3 | -14.27448 | -45.84296 | 2025-10-07 04:57:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| a917dae9-ace3-36b4-95ee-c5b313986147 | -13.72473 | -48.20278 | 2025-10-07 04:57:00 | NOAA-20 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| bd5724de-f078-39ba-8d8f-2d85de9c7655 | -14.75803 | -46.06023 | 2025-10-07 04:57:00 | NOAA-20 | SÍTIO D'ABADIA | GOIÁS | Brasil | 5220702 | 52 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 845c2710-27db-348e-9614-a37c3279b73e | -12.9559 | -46.8218 | 2025-10-07 04:57:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| b080c4db-778d-343b-89c9-dd59699fe2a4 | -9.83103 | -56.37889 | 2025-10-07 04:57:00 | NOAA-20 | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 658a1362-ac44-3886-9953-729fc8097b32 | -8.91058 | -50.60845 | 2025-10-07 04:57:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| c98c9926-7db0-3007-9470-84761190f9ba | -11.15146 | -47.75008 | 2025-10-07 04:57:00 | NOAA-20 | PINDORAMA DO TOCANTINS | TOCANTINS | Brasil | 1717008 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| c63cad43-b046-31f5-9761-ab86d0e91cc9 | -10.39845 | -45.37903 | 2025-10-07 04:57:00 | NOAA-20 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 18114443-9215-338d-a837-5c05aa9bab81 | -11.29018 | -49.99829 | 2025-10-07 04:57:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 334a7bc0-7692-3f62-9448-3a83d81f3dd4 | -14.91199 | -51.43956 | 2025-10-07 04:57:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 44203b9c-3ea1-322b-a469-5fe51e292e17 | -11.05357 | -50.90804 | 2025-10-07 04:57:00 | NOAA-20 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 4.6 |
| d64e65de-ede4-306d-906c-a31cb6c7eb19 | -9.00346 | -61.64266 | 2025-10-07 04:57:00 | NOAA-20 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 5e28db26-bf24-3fcc-9a11-fb5e2af9100d | -9.55946 | -63.50995 | 2025-10-07 04:57:00 | NOAA-20 | ALTO PARAÍSO | RONDÔNIA | Brasil | 1100403 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| acb5f269-06d0-3361-be5a-78fa1e72750a | -14.28428 | -45.84427 | 2025-10-07 04:57:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 1dbdf31d-6dd6-35ef-a82b-f2cfdef10792 | -10.43073 | -51.63516 | 2025-10-07 04:57:00 | NOAA-20 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 6cf08f7f-0b74-3ef4-ad12-9b9a5e61d879 | -14.92727 | -46.79726 | 2025-10-07 04:57:00 | NOAA-20 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 6.7 |
| e8049516-89e9-3a87-9e14-4eadbc780ae3 | -13.27104 | -48.05809 | 2025-10-07 04:57:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| e1a25721-329a-31b0-b9fd-42b59d1766c4 | -12.40596 | -51.14018 | 2025-10-07 04:57:00 | NOAA-20 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 34e3d793-0693-3734-a78d-8ce6d8bfff03 | -9.91304 | -60.19575 | 2025-10-07 04:57:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b7823892-c847-3b58-9e19-0b7326f2ed93 | -10.35988 | -44.98453 | 2025-10-07 04:57:00 | NOAA-20 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| f2b36c07-1fac-3b4f-9b0c-d1477c159630 | -15.36477 | -47.3251 | 2025-10-07 04:57:00 | NOAA-20 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 472b7888-9530-386d-b5c2-6f73c8d00267 | -12.16306 | -51.43424 | 2025-10-07 04:57:00 | NOAA-20 | BOM JESUS DO ARAGUAIA | MATO GROSSO | Brasil | 5101852 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| bed8a212-fb85-32d6-bc66-fa9748391ca6 | -9.02486 | -50.70028 | 2025-10-07 04:57:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| e8427567-5152-34bb-90a9-809018072b6e | -14.82821 | -52.93502 | 2025-10-07 04:57:00 | NOAA-20 | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 6054dc20-285c-3b9a-a3f2-2fc3eab490ee | -12.89623 | -54.74523 | 2025-10-07 04:57:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 38.0 |
| 2d75b824-2e8d-3390-a035-50d5384c2fc0 | -10.64008 | -57.09465 | 2025-10-07 04:57:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| d820724d-738a-3740-849d-734190df0325 | -12.61639 | -44.74928 | 2025-10-07 04:57:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 2e805073-6796-3113-b248-aa37a80e145d | -15.60787 | -47.29554 | 2025-10-07 04:57:00 | NOAA-20 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 6ba0f9b1-9974-30cb-bdc4-3d1b9e21287d | -11.73876 | -54.72416 | 2025-10-07 04:57:00 | NOAA-20 | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 450912eb-4b2f-30b3-9e92-20706fc8b98f | -13.22447 | -48.46843 | 2025-10-07 04:57:00 | NOAA-20 | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| e0f4fde3-3deb-3c64-bc4d-71437ac7b767 | -14.9044 | -46.85309 | 2025-10-07 04:57:00 | NOAA-20 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 543bfac0-3edc-3805-9dfc-e3123b7074ff | -12.95004 | -54.72821 | 2025-10-07 04:57:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 8dbd65c6-bfdc-3526-94d2-6e4c4b0b4dde | -13.27387 | -47.57354 | 2025-10-07 04:57:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 354ed1e2-f9a5-3068-8f18-2ce71ff33aae | -12.99633 | -46.79224 | 2025-10-07 04:57:00 | NOAA-20 | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 0d9ee423-75e8-3f76-bb7d-090a08de3d1d | -7.4608 | -63.62135 | 2025-10-07 04:57:00 | NOAA-20 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e04983f2-37a2-379a-81b9-e1f330dbe259 | -12.66015 | -45.02987 | 2025-10-07 04:57:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 4d48b63d-678f-341d-9743-53ddcb186686 | -14.75043 | -46.02859 | 2025-10-07 04:57:00 | NOAA-20 | SÍTIO D'ABADIA | GOIÁS | Brasil | 5220702 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| fedf8b25-82c5-3de6-b24a-ec3976469dde | -10.42709 | -51.63465 | 2025-10-07 04:57:00 | NOAA-20 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 96ce9eab-c865-3dab-aeda-5d99797e2ae4 | -9.06567 | -54.51288 | 2025-10-07 04:57:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| c8e38698-6f34-38f8-be1f-243b47ba982a | -11.95452 | -45.48695 | 2025-10-07 04:57:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 7b6f6d74-72b0-3dc1-9a69-76c0b56a53a9 | -13.09968 | -47.98732 | 2025-10-07 04:57:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 61351fc1-3d0c-34fb-bcde-7f794cc52f3e | -10.40969 | -50.30032 | 2025-10-07 04:57:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 52.4 |
| dcf80aa0-5357-34fc-879a-e83ae19bc097 | -14.64235 | -52.54222 | 2025-10-07 04:57:00 | NOAA-20 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 1c298796-c7c0-3ef9-8924-d1110b657ca9 | -9.90895 | -60.19502 | 2025-10-07 04:57:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 2156d839-24d1-386d-842d-f820e93d90f7 | -11.94788 | -46.43042 | 2025-10-07 04:57:00 | NOAA-20 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 1ff6f02e-342f-3920-a95c-6793d4bb9e10 | -11.67591 | -46.34092 | 2025-10-07 04:57:00 | NOAA-20 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 9348026d-dd63-3f3b-98ea-4d9a936c24d3 | -11.93822 | -46.42299 | 2025-10-07 04:57:00 | NOAA-20 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| d7432f24-31bc-39c4-ad9d-f7d38fa57003 | -14.93567 | -46.80782 | 2025-10-07 04:57:00 | NOAA-20 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 8820527f-47be-3bf8-a57e-bdb63be5871d | -15.07223 | -46.64066 | 2025-10-07 04:57:00 | NOAA-20 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 2e5f2e61-01c4-31fd-a862-61225030b094 | -9.67457 | -45.6735 | 2025-10-07 04:57:00 | NOAA-20 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| c2ea8533-5c0b-304e-ac36-e3386cfcbfaa | -10.33733 | -46.94532 | 2025-10-07 04:57:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 9.4 |
| ea53ea2c-53a3-3e51-8f87-066c425d5ded | -9.89962 | -58.43493 | 2025-10-07 04:57:00 | NOAA-20 | COTRIGUAÇU | MATO GROSSO | Brasil | 5103379 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 94dffaa7-7b8d-3a36-98bf-ff2e28fbb990 | -10.32282 | -51.45314 | 2025-10-07 04:57:00 | NOAA-20 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |


[Clique aqui para ver as próximas entradas](README94.md)
