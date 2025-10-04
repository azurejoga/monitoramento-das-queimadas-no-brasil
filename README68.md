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
| 33c16b8f-5f5e-3074-b370-f77dcc23379f | -11.91999 | -46.37458 | 2025-10-04 04:14:00 | NOAA-20 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 19.1 |
| 278fd5e6-8d9c-35d2-976d-ee4e9598f7e6 | -8.95868 | -48.68507 | 2025-10-04 04:14:00 | NOAA-20 | COLMÉIA | TOCANTINS | Brasil | 1716703 | 17 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 0bf83bab-8684-3d70-ab37-104e009a9042 | -14.44353 | -46.11377 | 2025-10-04 04:14:00 | NOAA-20 | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 91f0843c-a03b-3256-8408-fcb763cfbcd3 | -12.90328 | -54.74928 | 2025-10-04 04:14:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d2762282-3c03-356a-99a5-28cdf9f8d91d | -10.04829 | -54.33583 | 2025-10-04 04:14:00 | NOAA-20 | MATUPÁ | MATO GROSSO | Brasil | 5105606 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 560cd4eb-e372-3754-833a-f1acf6ba0285 | -13.21109 | -47.81286 | 2025-10-04 04:14:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 72f0c384-ab9f-3505-b613-a0d859604465 | -11.56436 | -47.67768 | 2025-10-04 04:14:00 | NOAA-20 | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 754aac4c-e094-3116-b4ae-1d2529250c73 | -15.83644 | -42.62225 | 2025-10-04 04:14:00 | NOAA-20 | RIO PARDO DE MINAS | MINAS GERAIS | Brasil | 3155603 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 7e512de1-ce5f-3be2-9be8-0005a798cb12 | -9.91117 | -43.79595 | 2025-10-04 04:14:00 | NOAA-20 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 068b44d8-fd53-36c0-9ca1-7192ea9eda4d | -12.08267 | -45.15932 | 2025-10-04 04:14:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| b737849b-754f-3c9d-8000-eddf3185144d | -11.07454 | -47.80001 | 2025-10-04 04:14:00 | NOAA-20 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 3709d39f-20f6-338e-bf8f-25cda9579cd8 | -14.33089 | -45.86242 | 2025-10-04 04:14:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 754cf2e8-eaef-36af-87e8-0f511c589f17 | -13.2679 | -46.48158 | 2025-10-04 04:14:00 | NOAA-20 | DIVINÓPOLIS DE GOIÁS | GOIÁS | Brasil | 5208301 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 0deee62d-1cc8-3579-826c-2a3a9dfef6d5 | -13.11243 | -47.84077 | 2025-10-04 04:14:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 2f5eae12-7cec-3168-9056-4ec4ff4e9490 | -9.32371 | -54.52512 | 2025-10-04 04:14:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 506d1032-e09a-3229-85a9-6312b5896dd5 | -11.12033 | -47.89991 | 2025-10-04 04:14:00 | NOAA-20 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| a384ffae-7a9c-3182-84ff-0b2c569e8d9e | -11.47928 | -45.01956 | 2025-10-04 04:14:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 5e500b02-2db0-3792-9e6f-9bf258045bce | -13.75082 | -48.0575 | 2025-10-04 04:14:00 | NOAA-20 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 55309b99-ab9e-317d-8c66-b68abeec88d4 | -12.83294 | -43.80695 | 2025-10-04 04:14:00 | NOAA-20 | SERRA DOURADA | BAHIA | Brasil | 2930303 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 1502cdad-efdc-3e19-b1f4-17ccbfd76b99 | -11.09826 | -49.8489 | 2025-10-04 04:14:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 80ca1660-7d8b-35ef-8559-cbc3bbd96cbf | -13.58723 | -48.17813 | 2025-10-04 04:14:00 | NOAA-20 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 4486379d-065c-348d-ab01-a3bc9e84313b | -12.05805 | -50.89735 | 2025-10-04 04:14:00 | NOAA-20 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 7c328042-9b84-3142-9a95-01bf38267d4b | -8.7141 | -44.84479 | 2025-10-04 04:14:00 | NOAA-20 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 8b901c53-3e4b-369b-8173-cfd398f93169 | -12.65268 | -46.978 | 2025-10-04 04:14:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 46e1f790-c3f2-3069-a15a-2e294d1bf4ba | -7.72989 | -49.85439 | 2025-10-04 04:14:00 | NOAA-20 | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| be935b4f-00dd-3f55-b8b0-0c96fbd254cf | -10.5801 | -48.71239 | 2025-10-04 04:14:00 | NOAA-20 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 51e5320e-b961-321c-a331-3b993f98bec3 | -12.0781 | -45.18782 | 2025-10-04 04:14:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 5.9 |
| d03b45da-19e6-3396-9114-2c21529dac58 | -11.12542 | -55.46354 | 2025-10-04 04:14:00 | NOAA-20 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| d959685e-e58c-3d42-8590-708476c9bfe0 | -13.64406 | -48.67682 | 2025-10-04 04:14:00 | NOAA-20 | CAMPINORTE | GOIÁS | Brasil | 5204706 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| f556eb77-3c39-3b17-84e8-e4944ce7b2db | -8.22531 | -46.81484 | 2025-10-04 04:14:00 | NOAA-20 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 06dd4415-881f-3ad7-9395-0c8cc76d0709 | -15.91712 | -43.30355 | 2025-10-04 04:14:00 | NOAA-20 | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| c3944fdd-1945-36fe-bf90-3687b467ff1d | -14.29846 | -45.87186 | 2025-10-04 04:14:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 7c626f92-70c0-3fe6-9adf-6a5dae5358d2 | -13.59828 | -48.17975 | 2025-10-04 04:14:00 | NOAA-20 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 8.6 |
| d519cea9-5387-39b6-9a04-b5a6e113691b | -13.52658 | -47.24085 | 2025-10-04 04:14:00 | NOAA-20 | TERESINA DE GOIÁS | GOIÁS | Brasil | 5221080 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 18b25962-4546-3932-8621-822ebb83f666 | -7.80649 | -49.86221 | 2025-10-04 04:14:00 | NOAA-20 | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 5e113647-e85c-31c4-b88d-f1722ddf144f | -11.91218 | -46.35778 | 2025-10-04 04:14:00 | NOAA-20 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| ab68d06f-67f1-3931-947e-b7513e46d9be | -13.10667 | -47.89613 | 2025-10-04 04:14:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 073325e2-87b9-3a90-b363-750f588ddb42 | -12.87381 | -44.62854 | 2025-10-04 04:14:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 3.3 |
| d835aa62-f32a-30f3-bef9-8d931aef8fc8 | -11.59336 | -47.04361 | 2025-10-04 04:14:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 4a50d759-77ac-3423-9552-55575c523dce | -13.74032 | -47.94466 | 2025-10-04 04:14:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 3961b04e-2ba4-3b7f-bd61-b9f05d16a8af | -8.86364 | -46.69546 | 2025-10-04 04:14:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| cf8a31bb-1b69-3ef7-8a7c-a7bd96ffc011 | -13.25791 | -47.2415 | 2025-10-04 04:14:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 0491c0ab-ff6b-392f-925b-f766912c581d | -9.32671 | -45.75812 | 2025-10-04 04:14:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 539f4b79-7b38-3240-8adf-11cfb1ae9aa7 | -13.30008 | -47.57283 | 2025-10-04 04:14:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 3e070a9e-e347-38e3-b059-ecfd9470b3e1 | -13.25372 | -47.24492 | 2025-10-04 04:14:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 3.3 |
| dee577ef-49cb-390a-b417-73f42e36ed99 | -13.31526 | -47.24576 | 2025-10-04 04:14:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| e70929fa-2ebd-3296-8c95-d29f80b6ee23 | -9.4612 | -45.53649 | 2025-10-04 04:14:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 3b184657-9769-3e2d-9500-01586eeba27a | -13.70556 | -47.33996 | 2025-10-04 04:14:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 129499ee-148b-37fa-ac74-403df663fc3c | -13.73535 | -47.93033 | 2025-10-04 04:14:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 8851eb52-dfe5-3b80-874c-25dd5a21d423 | -13.35244 | -47.23977 | 2025-10-04 04:14:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 60aefbe2-6f4a-34af-8d2f-0d91e92a1337 | -13.4639 | -47.26769 | 2025-10-04 04:14:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 4811236d-e548-318e-ba3a-893f597a178b | -10.82116 | -46.58778 | 2025-10-04 04:14:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 25870d4d-3608-3ca7-a741-a82c058c16f4 | -7.86548 | -48.21062 | 2025-10-04 04:14:00 | NOAA-20 | PALMEIRANTE | TOCANTINS | Brasil | 1715705 | 17 | 33 | nan | nan | nan | Cerrado | 4.9 |
| dd2f1461-9817-3360-950a-cd82f10fa639 | -11.88174 | -45.0135 | 2025-10-04 04:14:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| a1ceb686-0d12-396f-a19d-76840ad9de1f | -13.32602 | -47.62796 | 2025-10-04 04:14:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 7.5 |
| ecd38c47-c8f8-3c43-8820-161cea434eb0 | -10.21185 | -48.18738 | 2025-10-04 04:14:00 | NOAA-20 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| add54389-5fb7-3a3b-96bc-fe8684629f94 | -12.38595 | -47.78703 | 2025-10-04 04:14:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 9298377c-e316-331c-8566-1576a95f7d82 | -9.94381 | -43.73975 | 2025-10-04 04:14:00 | NOAA-20 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 78e9d3e5-86fd-37f9-a277-1c360570ca2b | -11.90683 | -46.36859 | 2025-10-04 04:14:00 | NOAA-20 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| ccb0938c-9356-3bfb-a584-8db6015a0c8e | -11.86532 | -44.96684 | 2025-10-04 04:14:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 703b7a76-722b-3bc8-9b80-02fae111a938 | -11.84162 | -45.05069 | 2025-10-04 04:14:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| d02ab0df-03c1-3866-86b4-fffdec9c7daf | -12.92152 | -46.91392 | 2025-10-04 04:14:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| a4e87b4e-494f-3c7f-b886-8d28070c26eb | -11.2465 | -47.79901 | 2025-10-04 04:14:00 | NOAA-20 | SANTA ROSA DO TOCANTINS | TOCANTINS | Brasil | 1718907 | 17 | 33 | nan | nan | nan | Cerrado | 5.4 |
| bb0470ea-caf0-3482-8e3f-439c68e00e88 | -9.33424 | -45.75537 | 2025-10-04 04:14:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 707951ca-93e0-3d6a-bc4a-70af009b08cb | -9.93553 | -50.24284 | 2025-10-04 04:14:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| bc532e85-5911-3e9b-bd89-95976a7d2fb3 | -14.68011 | -48.26331 | 2025-10-04 04:14:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| f39ff63f-bf0a-3400-ba73-b24d3730a62e | -15.75309 | -43.6754 | 2025-10-04 04:14:00 | NOAA-20 | SÃO JOÃO DA PONTE | MINAS GERAIS | Brasil | 3162401 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| aa964e31-bdf2-3993-a35f-f225d4f48ea5 | -10.88706 | -44.30468 | 2025-10-04 04:14:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 1725f49e-ab9f-3bc9-9db1-5f0abad0f407 | -13.34731 | -47.20576 | 2025-10-04 04:14:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 6844233f-afa2-3c26-bfad-27dd9e8e4047 | -9.93993 | -50.24364 | 2025-10-04 04:14:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| eb5c76a4-9ec6-36c1-9ce5-f5b73db25123 | -13.26133 | -47.22094 | 2025-10-04 04:14:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 1f011715-43ad-3e79-87cd-231e6ed0adba | -13.18339 | -50.93161 | 2025-10-04 04:14:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 35415f3d-5485-3b58-8df1-f54f90f9859e | -12.72587 | -48.57131 | 2025-10-04 04:14:00 | NOAA-20 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 9e450376-ac6c-3c9c-911a-a7b86abf8acb | -8.27706 | -43.84028 | 2025-10-04 04:14:00 | NOAA-20 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 8f4dfb5d-ee51-3838-80e3-d33fd8e303bc | -11.11912 | -43.38884 | 2025-10-04 04:14:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 44fda228-f8b5-37bd-9f47-d04a5ddfc082 | -12.99615 | -47.77489 | 2025-10-04 04:14:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 5b071b5d-4f76-366f-84f5-49f41be03227 | -13.22136 | -47.83981 | 2025-10-04 04:14:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 5b9a4031-9eeb-3a15-9958-76dd518aad79 | -11.7418 | -54.72521 | 2025-10-04 04:14:00 | NOAA-20 | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| a29348d9-0107-3af2-bff7-4db518a3ffd1 | -14.72202 | -50.03933 | 2025-10-04 04:14:00 | NOAA-20 | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| cacd212f-9bb7-318d-ac75-6f4b04037f3a | -8.23039 | -46.80679 | 2025-10-04 04:14:00 | NOAA-20 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 8bf13e69-a67f-3083-b7d3-a87113a58793 | -14.62377 | -48.21914 | 2025-10-04 04:14:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 2943b0ba-f136-3867-9862-041ce2633a6f | -11.92302 | -46.39885 | 2025-10-04 04:14:00 | NOAA-20 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| dc7f7650-dcf0-3324-88ca-4bac0c389f0c | -15.30794 | -46.30936 | 2025-10-04 04:14:00 | NOAA-20 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| f8a38329-5808-3956-a2f8-2321ff85f9a0 | -8.84543 | -46.7827 | 2025-10-04 04:14:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 5b5af6ef-e9c9-30a5-98ff-c99cb01cc29d | -11.54679 | -47.64764 | 2025-10-04 04:14:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 86976a1d-47aa-3b9b-9c9b-f5736d9f2e6c | -9.33709 | -54.51898 | 2025-10-04 04:14:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| e2ab96db-d49a-3ee5-a7fb-8b883b670559 | -14.87265 | -48.13033 | 2025-10-04 04:14:00 | NOAA-20 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 3a1ce2ce-1e9a-3fb6-8cca-df606cd16fa0 | -13.28501 | -47.18711 | 2025-10-04 04:14:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 68b97d30-b815-3f71-b156-aed10527439c | -11.87909 | -44.98735 | 2025-10-04 04:14:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 3b9e0a10-1cba-3ece-929c-e1cacdbb5905 | -8.22744 | -46.80187 | 2025-10-04 04:14:00 | NOAA-20 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| fb8ace44-692f-3410-b7ce-a04e47028a5b | -13.35011 | -47.21056 | 2025-10-04 04:14:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 2c56671d-58c8-36c1-bbe7-777cf89614da | -13.57522 | -47.27376 | 2025-10-04 04:14:00 | NOAA-20 | TERESINA DE GOIÁS | GOIÁS | Brasil | 5221080 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 50e2fcb6-5b00-37ed-805f-a0c4dd3b69c6 | -9.74834 | -48.90453 | 2025-10-04 04:14:00 | NOAA-20 | DIVINÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1707108 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 6f30880a-0d1c-3990-8f34-40fe50b674e4 | -13.96915 | -48.11934 | 2025-10-04 04:14:00 | NOAA-20 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| f69120b4-0b28-3ebb-aea5-d9238f5258f4 | -14.64354 | -48.3013 | 2025-10-04 04:14:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 8.4 |
| 5ed2dfdc-0224-3ee7-97d4-d54d827ef1aa | -12.36335 | -54.17097 | 2025-10-04 04:14:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| e3785db8-c391-34bc-a997-83760bdf61ad | -9.28805 | -45.67427 | 2025-10-04 04:14:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| d4fa1907-18de-3ed4-b8cf-f231ea986436 | -13.12619 | -47.93533 | 2025-10-04 04:14:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 4827ae52-009f-3e76-a399-45421afa1329 | -12.52786 | -45.96966 | 2025-10-04 04:14:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 17.3 |
| d8d85ca7-a20f-31dd-8cb7-bdf50b01da87 | -11.88725 | -45.02172 | 2025-10-04 04:14:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |


[Clique aqui para ver as próximas entradas](README69.md)
