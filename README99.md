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

## Dados Diários - Página 99

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| b1ed3701-caa9-36c8-ae57-32825cda4a05 | -13.68895 | -47.94905 | 2025-10-07 04:57:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 11cb30f7-64ac-37eb-88e7-7317e8152b97 | -10.39003 | -50.29745 | 2025-10-07 04:57:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 10.4 |
| db900100-92f3-3698-bbd1-0e10250534ce | -9.68179 | -48.39669 | 2025-10-07 04:57:00 | NOAA-20 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 0606a159-c02a-3b2b-8b9f-a135b477bf34 | -13.27947 | -48.4795 | 2025-10-07 04:57:00 | NOAA-20 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 162dc762-925b-335b-a000-92e6d1401388 | -13.22904 | -47.81189 | 2025-10-07 04:57:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 54eeb751-5388-340d-b8b4-b46ad0e1dd95 | -9.68615 | -48.39619 | 2025-10-07 04:57:00 | NOAA-20 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 1ea11120-3569-3b0d-b97c-55d7264e761d | -11.29498 | -48.2728 | 2025-10-07 04:57:00 | NOAA-20 | SANTA ROSA DO TOCANTINS | TOCANTINS | Brasil | 1718907 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 310be668-7fc7-3d7e-85aa-1a428998d92f | -10.40861 | -50.27948 | 2025-10-07 04:57:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| aa236207-99dc-368a-86ed-bcad2a89e298 | -9.44588 | -56.65383 | 2025-10-07 04:57:00 | NOAA-20 | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| a374179c-06b1-30b7-9fa8-72e0e779e028 | -13.3361 | -47.56994 | 2025-10-07 04:57:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.7 |
| f50b0513-50c4-39db-a65c-b72396c837c4 | -15.22018 | -49.31024 | 2025-10-07 04:57:00 | NOAA-20 | GOIANÉSIA | GOIÁS | Brasil | 5208608 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 2469a29d-41c5-3f47-a5eb-033bdf9f5dfb | -10.42758 | -50.28743 | 2025-10-07 04:57:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 6c948076-07a4-3e16-8901-f833b08550a5 | -11.74099 | -51.49763 | 2025-10-07 04:57:00 | NOAA-20 | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 53655c4d-f76c-3c87-a130-31e321981f2a | -8.97085 | -50.80305 | 2025-10-07 04:57:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| e9d42286-b05a-338a-aa89-e172e8ed7d31 | -11.74262 | -54.72116 | 2025-10-07 04:57:00 | NOAA-20 | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| a8627bac-7d31-33d2-9c18-eea77bb4d99b | -13.33741 | -48.03119 | 2025-10-07 04:57:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 7.0 |
| ebfeb8c9-8376-336d-a9bc-c1730bdbcfbd | -9.7524 | -62.26996 | 2025-10-07 04:57:00 | NOAA-20 | VALE DO ANARI | RONDÔNIA | Brasil | 1101757 | 11 | 33 | nan | nan | nan | Amazônia | 3.3 |
| e124800c-6bc2-3973-a1f1-53d456ab5635 | -9.03495 | -49.76576 | 2025-10-07 04:57:00 | NOAA-20 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 356445cb-6983-3ac3-be39-419bcb9589d0 | -12.99672 | -51.09974 | 2025-10-07 04:57:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| e02188d0-a9c1-35bc-aad0-c66b1b7e4e6d | -14.96797 | -49.95174 | 2025-10-07 04:57:00 | NOAA-20 | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 4834c222-b451-3daf-80eb-30ae0686fead | -14.91817 | -46.81997 | 2025-10-07 04:57:00 | NOAA-20 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 6d362890-312e-304b-9fe1-aeacdb688942 | -13.85952 | -43.993 | 2025-10-07 04:57:00 | NOAA-20 | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 40d7f43d-94d4-37f9-8351-17eb2634c425 | -13.08585 | -47.86473 | 2025-10-07 04:57:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| e04bc264-0fa3-3248-b601-9b9d4c065d68 | -9.0015 | -61.54523 | 2025-10-07 04:57:00 | NOAA-20 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 83bdecf2-c230-33e4-82b0-5724a292c7f8 | -12.19991 | -56.95953 | 2025-10-07 04:57:00 | NOAA-20 | ITANHANGÁ | MATO GROSSO | Brasil | 5104542 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 20d5594b-5e4c-305b-a1ab-c4097c6598d1 | -10.81457 | -48.60358 | 2025-10-07 04:57:00 | NOAA-20 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 57e5fb68-9067-3e96-9b88-3482eb07dd77 | -11.9608 | -55.25807 | 2025-10-07 04:57:00 | NOAA-20 | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 5e0ec44b-8d97-32e3-9a1b-bb6b0558019c | -12.37871 | -51.11155 | 2025-10-07 04:57:00 | NOAA-20 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| db9d66fa-9b98-37ca-9e6e-1cad72769e56 | -7.46139 | -63.61798 | 2025-10-07 04:57:00 | NOAA-20 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 94a105cf-9e91-3c1a-a67e-41cc2ee5174d | -12.27594 | -55.11031 | 2025-10-07 04:57:00 | NOAA-20 | VERA | MATO GROSSO | Brasil | 5108501 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 7e238acb-306e-3037-89a8-8b82e01968b9 | -10.45914 | -51.24356 | 2025-10-07 04:57:00 | NOAA-20 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 1b8c6ebb-4c34-3a72-86dd-6d84be0ef965 | -9.18994 | -47.84391 | 2025-10-07 04:57:00 | NOAA-20 | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 65c5469c-ef37-3050-95a3-294ee9efe0de | -12.29635 | -55.11001 | 2025-10-07 04:57:00 | NOAA-20 | VERA | MATO GROSSO | Brasil | 5108501 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 3a6de482-efa6-38e9-96ff-d978b2362827 | -9.90959 | -60.19138 | 2025-10-07 04:57:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 57fdb923-29a3-320e-8e72-e850ce7d6299 | -12.18127 | -47.78235 | 2025-10-07 04:57:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 150b006a-90cb-3fa0-a8e7-0538fa964f0a | -14.98769 | -49.96795 | 2025-10-07 04:57:00 | NOAA-20 | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| a0319d8e-36c2-3a0e-b427-e44c30290e36 | -12.28474 | -51.36477 | 2025-10-07 04:57:00 | NOAA-20 | SERRA NOVA DOURADA | MATO GROSSO | Brasil | 5107883 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 9a49a485-b5c2-364d-899c-47ca5cc4e814 | -10.4135 | -45.39228 | 2025-10-07 04:57:00 | NOAA-20 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 36d75f63-39af-39b5-a01e-fe23c2ed796c | -15.60749 | -47.29863 | 2025-10-07 04:57:00 | NOAA-20 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 4.5 |
| eaf611d9-8f14-3556-978b-5ba5e3b8fc1a | -8.85355 | -62.36539 | 2025-10-07 04:57:00 | NOAA-20 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 2.5 |
| f50aa5cf-ebec-33f0-9c77-f0cd2e676dc6 | -11.02472 | -51.16009 | 2025-10-07 04:57:00 | NOAA-20 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 1bce14c3-0478-3be7-bbe4-9d22116e8949 | -10.42968 | -50.32902 | 2025-10-07 04:57:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 54cab3d5-517c-3f77-9c0c-ac5738178475 | -6.74379 | -63.06349 | 2025-10-07 04:57:00 | NOAA-20 | TAPAUÁ | AMAZONAS | Brasil | 1304104 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 18b1a591-4482-3ddf-9271-a99d2973d7ef | -13.53653 | -42.99656 | 2025-10-07 04:57:00 | NOAA-20 | RIACHO DE SANTANA | BAHIA | Brasil | 2926400 | 29 | 33 | nan | nan | nan | Caatinga | 26.0 |
| b2c71c4a-1b9c-320f-bd60-1545d0aedad4 | -9.60706 | -57.14872 | 2025-10-07 04:57:00 | NOAA-20 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 34521cc3-f95a-3eff-a56d-fba46b4e882f | -12.99793 | -46.79284 | 2025-10-07 04:57:00 | NOAA-20 | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 26340af8-d445-3139-828f-20d7a15f19d5 | -12.31622 | -55.11323 | 2025-10-07 04:57:00 | NOAA-20 | VERA | MATO GROSSO | Brasil | 5108501 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 9dfaf37d-c92d-389d-8728-f7dff1a21a32 | -10.56041 | -56.55395 | 2025-10-07 04:57:00 | NOAA-20 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 4.8 |
| c9787c32-e7f9-34ca-9382-1f64b62bebb5 | -15.20731 | -48.25247 | 2025-10-07 04:57:00 | NOAA-20 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| c03a1dc8-e087-3480-b71f-ee4a4d4fed5c | -11.13116 | -47.21584 | 2025-10-07 04:57:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 4.3 |
| b44046f1-f302-393f-adcc-4bb8ed337536 | -10.32161 | -46.93538 | 2025-10-07 04:57:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 6b29a99c-28bb-3373-84ca-bfe9d1d94fd5 | -13.26087 | -47.79362 | 2025-10-07 04:57:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 259f2b0c-0e84-348d-b64e-609cc4b4a0e4 | -14.69837 | -48.39472 | 2025-10-07 04:57:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 2cfb5a8f-1d0b-3031-b08d-303b7a1caf0c | -15.49967 | -47.93288 | 2025-10-07 04:57:00 | NOAA-20 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 21a1c561-6ce1-37de-b1ee-ba6d7e66c70d | -10.55982 | -56.55762 | 2025-10-07 04:57:00 | NOAA-20 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 7fd383c1-cca7-306c-a46c-fb1ecba6b248 | -12.6154 | -44.75785 | 2025-10-07 04:57:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 7bca4d94-2ab7-3d47-a02a-544b1cc2a6f3 | -14.90369 | -46.85297 | 2025-10-07 04:57:00 | NOAA-20 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 603af94d-acc1-308d-bd82-400060cb12b7 | -9.04012 | -50.59366 | 2025-10-07 04:57:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 4aff95cd-6457-3f92-a61e-39238835951b | -15.86552 | -46.24962 | 2025-10-07 04:57:00 | NOAA-20 | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 167a69aa-922d-35d8-81ca-e14d5a7f7f77 | -12.18529 | -47.7887 | 2025-10-07 04:57:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 1ed66a41-1453-3fb5-ab3b-32a8ec1a6d9f | -10.80244 | -48.59349 | 2025-10-07 04:57:00 | NOAA-20 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 2a1a3829-2b5a-371f-8e7e-6212dffd9a3d | -9.34553 | -54.5256 | 2025-10-07 04:57:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 5afd956e-2194-388d-880f-96097d4fb950 | -6.73743 | -63.06895 | 2025-10-07 04:57:00 | NOAA-20 | TAPAUÁ | AMAZONAS | Brasil | 1304104 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 4711ffbb-63cb-3259-be76-02bb0275a450 | -10.38539 | -50.30193 | 2025-10-07 04:57:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 22.0 |
| 8cf04a0f-4e70-37bf-8375-b23fcdfd4a51 | -11.80093 | -45.0554 | 2025-10-07 04:57:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 13b2b38f-b544-37bf-a365-4f63cf846a08 | -11.9449 | -46.45374 | 2025-10-07 04:57:00 | NOAA-20 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 1199d7a7-db2d-3705-b5ad-e49df7589b17 | -11.51149 | -54.45995 | 2025-10-07 04:57:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 93aa8af8-52bf-3ec2-8699-f4014421d4a5 | -8.61653 | -54.96872 | 2025-10-07 04:57:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 0619e605-5d85-3656-8d5a-16e14aa31edb | -9.60389 | -63.18459 | 2025-10-07 04:57:00 | NOAA-20 | ALTO PARAÍSO | RONDÔNIA | Brasil | 1100403 | 11 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 849c28d1-ad1a-32ef-80d4-d02e986fe7e8 | -12.28809 | -51.36733 | 2025-10-07 04:57:00 | NOAA-20 | SERRA NOVA DOURADA | MATO GROSSO | Brasil | 5107883 | 51 | 33 | nan | nan | nan | Cerrado | 0.5 |
| ccaa7c54-c856-3a6b-b427-a9af35713823 | -13.29102 | -47.7765 | 2025-10-07 04:57:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 8ba9e773-b69a-3528-8fc9-cb850ca324a9 | -10.60201 | -49.63711 | 2025-10-07 04:57:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 3e887f3b-7b1c-3d57-ab0e-fd99ffc9a97b | -13.07889 | -47.84189 | 2025-10-07 04:57:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 6288ed91-477a-3a59-bc2b-0969f0e736b9 | -11.2215 | -47.77656 | 2025-10-07 04:57:00 | NOAA-20 | PINDORAMA DO TOCANTINS | TOCANTINS | Brasil | 1717008 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 5aafeb65-e3fd-31fd-99d0-c05c48b91331 | -10.63665 | -57.09868 | 2025-10-07 04:57:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 7afb3ece-f292-3a0e-ac46-c00d48fa5225 | -9.0937 | -47.95827 | 2025-10-07 04:57:00 | NOAA-20 | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 9bffff92-f17d-3749-86a8-7ac6a148be9e | -12.4098 | -51.14073 | 2025-10-07 04:57:00 | NOAA-20 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 3.2 |
| be2db3c0-c2b8-3385-aff5-ce75407b4d06 | -8.50331 | -49.13192 | 2025-10-07 04:57:00 | NOAA-20 | COUTO MAGALHÃES | TOCANTINS | Brasil | 1706001 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 58b560f2-fd2d-327e-a51f-ef28c6aa5dcd | -9.27488 | -48.32226 | 2025-10-07 04:57:00 | NOAA-20 | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 506d161f-bb7b-3c93-8a31-22528910d53f | -14.40548 | -52.88971 | 2025-10-07 04:57:00 | NOAA-20 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 50e064f0-73ad-36c9-8958-07ba70f6c49e | -9.13945 | -58.93565 | 2025-10-07 04:57:00 | NOAA-20 | COTRIGUAÇU | MATO GROSSO | Brasil | 5103379 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 14531bdf-106f-3f9d-b1ea-a04d223a83f2 | -13.00703 | -51.0252 | 2025-10-07 04:57:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 503daa55-cb67-3ccd-b676-2b5a361eb791 | -7.45832 | -63.61986 | 2025-10-07 04:57:00 | NOAA-20 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 39138e96-e740-3a80-ad30-1c76301b30b5 | -9.8897 | -60.16567 | 2025-10-07 04:57:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 7def656b-2adf-3f30-9029-3b17c78e9122 | -8.10623 | -55.08001 | 2025-10-07 04:57:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 04d4c87e-3782-32a6-8a71-b6a5be952bbe | -10.892 | -53.74711 | 2025-10-07 04:57:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 714d038d-96f6-3c28-b9d5-9b98d16e6fa5 | -15.28543 | -46.33498 | 2025-10-07 04:57:00 | NOAA-20 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 5bd27142-2fe5-3c88-af8f-19b7c9e99eaa | -8.46597 | -49.22466 | 2025-10-07 04:57:00 | NOAA-20 | COUTO MAGALHÃES | TOCANTINS | Brasil | 1706001 | 17 | 33 | nan | nan | nan | Cerrado | 5.6 |
| af8cd476-17f8-3223-8521-8f9717381518 | -14.91908 | -46.82045 | 2025-10-07 04:57:00 | NOAA-20 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| d0e729f1-951c-321e-b8f0-2f04cea51ecd | -9.73826 | -53.96661 | 2025-10-07 04:57:00 | NOAA-20 | MATUPÁ | MATO GROSSO | Brasil | 5105606 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 2ee44f09-e3f2-3493-a998-6ace1585288f | -9.38394 | -59.42134 | 2025-10-07 04:57:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 8a60de75-151d-3ba4-ba1d-ca1d62d0acfb | -13.24685 | -47.17953 | 2025-10-07 04:57:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 79a43dc2-093b-36a2-a482-1bab186d7cd9 | -13.85326 | -43.99231 | 2025-10-07 04:57:00 | NOAA-20 | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| cf2a4e8f-904e-34c4-a6d0-cf5f7a186cc2 | -9.59202 | -51.62487 | 2025-10-07 04:57:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| cfc5640f-4dcd-3c6e-afcc-711ede7d5026 | -6.69552 | -62.8448 | 2025-10-07 04:57:00 | NOAA-20 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c9104364-ff0a-3973-bcad-99a1c94dea13 | -13.07952 | -47.83684 | 2025-10-07 04:57:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 62451854-e569-3910-b094-35310acced38 | -10.39254 | -50.30814 | 2025-10-07 04:57:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 11e6fb53-4695-3a8e-bb19-3a90587e7838 | -8.32166 | -54.96453 | 2025-10-07 04:57:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 2225eba3-8676-345c-8a31-a771c5e1f2cd | -11.67025 | -46.3436 | 2025-10-07 04:57:00 | NOAA-20 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 5b036659-e0ca-3f3e-8108-363f22e6cdb8 | -10.45409 | -50.40939 | 2025-10-07 04:57:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 15.6 |


[Clique aqui para ver as próximas entradas](README100.md)
