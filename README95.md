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

## Dados Diários - Página 95

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 75c49a1d-fda8-3f67-8883-b6af2d68315a | -14.21429 | -46.10385 | 2025-10-01 04:51:00 | NPP-375D | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 9b0f2807-9bdd-335e-a303-2b46e9bb59d5 | -13.66866 | -48.07304 | 2025-10-01 04:51:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 9d8e8523-0051-31a3-934e-03e1d9dd49d1 | -12.2445 | -47.80494 | 2025-10-01 04:51:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 0497a8df-55bf-3973-a5a6-648dd9b0078a | -9.51717 | -54.74011 | 2025-10-01 04:51:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 2c8cd0f3-3339-3491-91c4-f1c32d42e076 | -12.96958 | -46.42019 | 2025-10-01 04:51:00 | NPP-375D | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| e5605f03-7c34-3711-97ba-708e96b6f477 | -14.17958 | -46.11633 | 2025-10-01 04:51:00 | NPP-375D | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 53cd3746-1c37-3aec-963c-14ac05ba5819 | -13.09779 | -47.04133 | 2025-10-01 04:51:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| f7ef822b-ff40-34db-adc2-ae3f58bdf99c | -12.46563 | -50.25417 | 2025-10-01 04:51:00 | NPP-375D | SÃO MIGUEL DO ARAGUAIA | GOIÁS | Brasil | 5220207 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| aac11c94-5b01-3133-896b-73fa4ae3b4e5 | -13.03054 | -48.67203 | 2025-10-01 04:51:00 | NPP-375D | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| ab7c98f9-93af-3357-b4fa-c3ffda6205c0 | -12.98252 | -48.41896 | 2025-10-01 04:51:00 | NPP-375D | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | 4.7 |
| bb0730e6-9c0b-38ff-8274-fe4b519efef4 | -13.92888 | -48.11138 | 2025-10-01 04:51:00 | NPP-375D | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| fd65fbc0-4002-3d05-b5e2-09821d793adb | -14.90006 | -48.10651 | 2025-10-01 04:51:00 | NPP-375D | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 7.3 |
| e354aff8-80ae-32a4-aa6a-e9cf9540cb6e | -14.685 | -48.22936 | 2025-10-01 04:51:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 81bdc809-776d-3cc0-8647-ddafd378f550 | -8.26356 | -54.96226 | 2025-10-01 04:51:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 8ab8d392-ca2e-3851-a26c-71b3bf38e5ac | -14.35688 | -45.93423 | 2025-10-01 04:51:00 | NPP-375D | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 20.6 |
| e1590ea1-506e-33d3-8124-72834f93f7e9 | -14.96121 | -46.88227 | 2025-10-01 04:51:00 | NPP-375D | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 23a1cda1-3770-3240-94e5-d9fbb98005bf | -12.15585 | -51.42443 | 2025-10-01 04:51:00 | NPP-375D | SERRA NOVA DOURADA | MATO GROSSO | Brasil | 5107883 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 62d97ecd-1deb-35cb-8e42-ad52c6a3e249 | -15.33965 | -46.28038 | 2025-10-01 04:51:00 | NPP-375D | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 5.0 |
| a5b857a4-1f02-364d-9f88-277f20435dda | -14.03838 | -47.96296 | 2025-10-01 04:51:00 | NPP-375D | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| bea9ddbb-8030-3a62-a0d9-edf7a4d457a9 | -10.18746 | -52.55182 | 2025-10-01 04:51:00 | NPP-375D | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 6d1f4e25-6994-33e9-bb13-f05fa06d4021 | -13.06481 | -47.06446 | 2025-10-01 04:51:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 4791ddb3-1b99-38e7-8597-85ef46243374 | -11.14927 | -54.30485 | 2025-10-01 04:51:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 2ca4a136-a0e1-3148-9017-6a66d7629fa5 | -9.85938 | -44.6012 | 2025-10-01 04:51:00 | NPP-375D | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 4b761ae7-3a88-30f8-b13d-00b591340b9f | -12.77252 | -50.55536 | 2025-10-01 04:51:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 62de0f55-39dc-38d6-80ab-e710235f2a00 | -15.48701 | -45.9054 | 2025-10-01 04:51:00 | NPP-375D | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 1b9f63d4-ea72-3682-90fd-d72c6449ce8f | -13.07986 | -47.07843 | 2025-10-01 04:51:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 616d475f-82be-3cc2-a619-ca88390993bc | -12.85849 | -46.94362 | 2025-10-01 04:51:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 41e6350e-5cc3-3dd0-af2c-be2b7f1ca243 | -11.75299 | -46.84023 | 2025-10-01 04:51:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 5f814bbf-cb7c-31bd-816b-0194d07188da | -16.00201 | -50.87448 | 2025-10-01 04:51:00 | NPP-375D | JUSSARA | GOIÁS | Brasil | 5212204 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 118ade35-52d3-3d2a-b91d-8971ee027026 | -13.93801 | -48.10356 | 2025-10-01 04:51:00 | NPP-375D | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 5.7 |
| f4d6415d-5f11-3da4-b1df-186baa754ddc | -12.66798 | -46.86175 | 2025-10-01 04:51:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 52f3c670-d3b0-35dd-acd9-c33d29c789c8 | -12.4662 | -50.22643 | 2025-10-01 04:51:00 | NPP-375D | SÃO MIGUEL DO ARAGUAIA | GOIÁS | Brasil | 5220207 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 2aec4fad-5a22-3eb4-ac36-ed7404c262db | -12.83203 | -46.98121 | 2025-10-01 04:51:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 33a71ca3-2548-3b59-836a-8ec6d8138a5c | -12.29549 | -55.14085 | 2025-10-01 04:51:00 | NPP-375D | VERA | MATO GROSSO | Brasil | 5108501 | 51 | 33 | nan | nan | nan | Amazônia | 0.4 |
| ebc1289d-7831-384a-9fab-d5951b332e38 | -12.76907 | -50.55483 | 2025-10-01 04:51:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 3b776b47-9001-34ac-bbf4-aaff18573946 | -15.30463 | -46.40064 | 2025-10-01 04:51:00 | NPP-375D | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 4f2bc6df-357f-3953-a000-dc7c6ec977c6 | -13.36083 | -48.10998 | 2025-10-01 04:51:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 86318ffb-94dc-3897-88ec-f494a69ee85f | -9.93952 | -43.6346 | 2025-10-01 04:51:00 | NPP-375D | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 61627dde-707d-39df-a83e-9067b0141efc | -14.59959 | -48.21417 | 2025-10-01 04:51:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| fdab654c-abd2-3b1b-9da7-b07580f7e6b3 | -12.77144 | -46.892 | 2025-10-01 04:51:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 1897b2b5-ba75-3366-98f0-060eef4deb18 | -15.46385 | -45.88444 | 2025-10-01 04:51:00 | NPP-375D | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 1565a9ee-fb7f-3f2c-a013-893ac5378901 | -9.92565 | -43.66246 | 2025-10-01 04:51:00 | NPP-375D | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 4cc73882-94ef-33a2-b724-29fcf12dc466 | -11.12167 | -49.78386 | 2025-10-01 04:51:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 774b6f83-90ff-3169-9430-bfa92f8014f9 | -15.26454 | -49.26148 | 2025-10-01 04:51:00 | NPP-375D | GOIANÉSIA | GOIÁS | Brasil | 5208608 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| e86b598f-c773-3097-9b8f-63ca91420e19 | -13.29377 | -50.65685 | 2025-10-01 04:51:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| f63b4826-3cab-3b4c-bf37-93721c8a6cdb | -16.00571 | -50.87794 | 2025-10-01 04:51:00 | NPP-375D | JUSSARA | GOIÁS | Brasil | 5212204 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| cadd7370-2732-3af2-963d-ad9603e309f7 | -9.92635 | -43.69701 | 2025-10-01 04:51:00 | NPP-375D | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 85e06bcb-357e-3fef-b592-b83031d7cf87 | -12.6716 | -46.86657 | 2025-10-01 04:51:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| bc540213-c607-3967-8894-046f3eefeb96 | -15.65815 | -51.32948 | 2025-10-01 04:51:00 | NPP-375D | SANTA FÉ DE GOIÁS | GOIÁS | Brasil | 5219258 | 52 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 1105bb30-fdf4-3bd6-a515-08652677a717 | -12.8278 | -50.57893 | 2025-10-01 04:51:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 247155d3-3274-3455-a7d6-788e5a6b3eeb | -10.8317 | -45.38163 | 2025-10-01 04:51:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 10.8 |
| 7d544682-112e-3b00-a3f9-de6b02e7e808 | -14.8715 | -49.7159 | 2025-10-01 04:51:00 | NPP-375D | GUARINOS | GOIÁS | Brasil | 5209457 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 0bead91c-f8b5-32af-a645-c664f457c7ae | -10.64491 | -48.52478 | 2025-10-01 04:51:00 | NPP-375D | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 5.6 |
| c3658622-3387-3f9c-9069-1e980652b5da | -16.08129 | -51.04419 | 2025-10-01 04:51:00 | NPP-375D | FAZENDA NOVA | GOIÁS | Brasil | 5207600 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 3e1bbea5-03fb-3366-8f82-d7ea76437b34 | -13.05958 | -47.07156 | 2025-10-01 04:51:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| cb178d99-889b-35eb-a428-3bd085b57925 | -12.79417 | -46.91375 | 2025-10-01 04:51:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 9c313b92-e7aa-35db-930d-ff9f809f0cfd | -15.27273 | -49.2853 | 2025-10-01 04:51:00 | NPP-375D | GOIANÉSIA | GOIÁS | Brasil | 5208608 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 669e1b2a-af3c-377c-8895-d69477b5b7c3 | -12.17655 | -51.42403 | 2025-10-01 04:51:00 | NPP-375D | SERRA NOVA DOURADA | MATO GROSSO | Brasil | 5107883 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| a580cab8-32ce-3ace-9ff3-54c9be667c09 | -15.43835 | -43.64603 | 2025-10-01 04:51:00 | NPP-375D | VERDELÂNDIA | MINAS GERAIS | Brasil | 3171030 | 31 | 33 | nan | nan | nan | Caatinga | 1.3 |
| c37d0ed2-bea7-381e-9ebe-c747d2256c35 | -15.23509 | -48.74796 | 2025-10-01 04:51:00 | NPP-375D | VILA PROPÍCIO | GOIÁS | Brasil | 5222302 | 52 | 33 | nan | nan | nan | Cerrado | 6.0 |
| c1940fe7-2ec0-38b0-bfaa-d3138b6a7c31 | -10.97052 | -46.50766 | 2025-10-01 04:51:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| a70690ef-84f1-303c-86f2-7c174bc5e8a1 | -10.01791 | -50.2452 | 2025-10-01 04:51:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 04b78114-29d2-30f0-a5fd-8736604218e3 | -11.43118 | -43.50258 | 2025-10-01 04:51:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 62942325-3ae0-39e0-a140-383fd9571717 | -14.78879 | -45.78359 | 2025-10-01 04:51:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 6.1 |
| a517667c-36c3-3747-984d-a068c967832c | -13.78124 | -51.23216 | 2025-10-01 04:51:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 5534cccd-2dcf-3fd5-811b-38613eb8a67f | -15.61687 | -46.91203 | 2025-10-01 04:51:00 | NPP-375D | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 75ad4bd0-79c1-397d-93be-0821f3b9c6a6 | -16.19795 | -49.99661 | 2025-10-01 04:51:00 | NPP-375D | ITABERAÍ | GOIÁS | Brasil | 5210406 | 52 | 33 | nan | nan | nan | Cerrado | 11.2 |
| 1a98e50a-ac5b-3dd3-b012-bc338bc19f4d | -11.65346 | -45.32351 | 2025-10-01 04:51:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 45c09a2e-f6b9-3f18-a955-68a4d8d82b26 | -12.37261 | -47.17104 | 2025-10-01 04:51:00 | NPP-375D | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 3ae93d99-6512-3cbf-8553-ef38678292bd | -9.93196 | -43.65651 | 2025-10-01 04:51:00 | NPP-375D | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 36cb7f33-97be-34b6-803c-3ba8b84e81be | -12.24166 | -47.82558 | 2025-10-01 04:51:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 526cef7e-919b-3a3b-9d05-116269954b81 | -15.94221 | -48.11552 | 2025-10-01 04:51:00 | NPP-375D | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 1d224ded-90c2-3aaa-9e91-8381fd5e33b3 | -13.66828 | -48.04694 | 2025-10-01 04:51:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 2f701b6b-b498-335f-a27e-9f83b6ce1f09 | -13.70091 | -48.63317 | 2025-10-01 04:51:00 | NPP-375D | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 697e8c5d-f6b6-3062-9c3b-3cc51c81522b | -12.17711 | -51.42043 | 2025-10-01 04:51:00 | NPP-375D | SERRA NOVA DOURADA | MATO GROSSO | Brasil | 5107883 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 83f6e86f-5b79-3bb0-b1c6-b9d4e3c63750 | -12.67215 | -46.86259 | 2025-10-01 04:51:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| c94f0a3e-8658-3345-9def-b4a6db5f713b | -11.45112 | -43.51172 | 2025-10-01 04:51:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 5df85331-f2a4-3cf3-91a1-00b1cb7d22b7 | -13.76598 | -47.96883 | 2025-10-01 04:51:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 4.4 |
| a1f37161-7188-3884-ae62-6e425ce27d41 | -12.37224 | -54.15968 | 2025-10-01 04:51:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 6042a4ac-cf2b-30df-b4f1-624de4b22a01 | -13.70472 | -48.6338 | 2025-10-01 04:51:00 | NPP-375D | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| df8485a7-bd62-362c-a254-ed9b281cd4e7 | -13.29586 | -46.38713 | 2025-10-01 04:51:00 | NPP-375D | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| c257f57e-fb8b-3594-a085-db364c958ef1 | -13.33405 | -47.86901 | 2025-10-01 04:51:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 5f8e2f7a-d1b2-3f6d-be34-6cf4163fe496 | -13.28286 | -47.22402 | 2025-10-01 04:51:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| a88e626c-7293-38c7-82ca-6b043dd5b1a5 | -9.30496 | -51.56419 | 2025-10-01 04:51:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| c451291f-22ee-3e53-8410-c8e2eac38844 | -12.84869 | -46.95279 | 2025-10-01 04:51:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 51c002f7-220e-33ad-8671-b22d010213fc | -10.60444 | -49.63634 | 2025-10-01 04:51:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 43101810-85e0-3c67-8db0-f91582259c33 | -14.71493 | -48.12828 | 2025-10-01 04:51:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 1172fcbb-5b06-3baa-9fb3-3ec2f465cfd5 | -9.39674 | -54.70353 | 2025-10-01 04:51:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 8ec530c0-ffa9-30c1-a061-b778486e34f5 | -15.29872 | -46.19546 | 2025-10-01 04:51:00 | NPP-375D | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 949974a8-4f47-384c-95cc-cc61fb467d74 | -13.53646 | -47.2622 | 2025-10-01 04:51:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 3f599dec-c9c1-3d67-b5cb-cbc6863d9f08 | -14.37621 | -47.13466 | 2025-10-01 04:51:00 | NPP-375D | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 9e6f7426-0f4b-3df5-90ed-28492db54a63 | -15.23465 | -48.74151 | 2025-10-01 04:51:00 | NPP-375D | VILA PROPÍCIO | GOIÁS | Brasil | 5222302 | 52 | 33 | nan | nan | nan | Cerrado | 7.3 |
| 7c1258d9-c8ee-3e7b-a24e-82d6dcdbb6fb | -13.2955 | -47.24023 | 2025-10-01 04:51:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 4a724e80-5c6b-3107-821b-7919acd4d3bd | -11.46791 | -45.0749 | 2025-10-01 04:51:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 7e8be5fb-f668-30c2-a86b-83bb26af7ba9 | -11.5253 | -43.55452 | 2025-10-01 04:51:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 44a3ce95-6f03-34ba-b636-d264b9e9ec59 | -12.88795 | -45.19715 | 2025-10-01 04:51:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 1e52d0b5-cdb0-32c0-b3e8-d37f8328885a | -13.67187 | -48.07882 | 2025-10-01 04:51:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 306043c5-80c1-38ca-bd1d-52d843c38550 | -13.7379 | -48.69405 | 2025-10-01 04:51:00 | NPP-375D | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| f3faf518-a747-3ec1-9f04-ecc9668b1356 | -11.16238 | -47.23444 | 2025-10-01 04:51:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| dea13ef2-bed4-3008-8f9f-dc8da442a107 | -12.88861 | -45.19212 | 2025-10-01 04:51:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |


[Clique aqui para ver as próximas entradas](README96.md)
