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

## Dados Diários - Página 13

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 4a58557e-f80a-39d3-b2ee-d77e2291f55e | -8.15538 | -38.63126 | 2025-10-20 04:12:00 | NOAA-20 | MIRANDIBA | PERNAMBUCO | Brasil | 2609303 | 26 | 33 | nan | nan | nan | Caatinga | 5.3 |
| 487afe60-9627-3d05-aed5-1fd625c78163 | -4.39552 | -43.31603 | 2025-10-20 04:12:00 | NOAA-20 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| ab06f351-5c45-33ac-a18e-45671d547d81 | -5.39711 | -42.80788 | 2025-10-20 04:12:00 | NOAA-20 | NAZÁRIA | PIAUÍ | Brasil | 2206720 | 22 | 33 | nan | nan | nan | Caatinga | 3.0 |
| e6a764e7-18fc-313b-a5da-49022b03e77d | -5.62162 | -43.6432 | 2025-10-20 04:12:00 | NOAA-20 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 20721b04-46a3-3822-ac45-1e97731b5f0f | -2.25016 | -51.91335 | 2025-10-20 04:12:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 9.8 |
| 16b80850-adee-3375-8c8f-fbf832f34882 | -4.83653 | -42.74399 | 2025-10-20 04:12:00 | NOAA-20 | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Cerrado | 33.5 |
| 7820b393-3ffc-3347-9fec-801d6dd7aed5 | -2.62721 | -49.37535 | 2025-10-20 04:12:00 | NOAA-20 | MOCAJUBA | PARÁ | Brasil | 1504604 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| e6299657-4330-311f-bbff-e6cc48289422 | -8.00052 | -39.62613 | 2025-10-20 04:12:00 | NOAA-20 | PARNAMIRIM | PERNAMBUCO | Brasil | 2610400 | 26 | 33 | nan | nan | nan | Caatinga | 3.4 |
| 22b2b0f4-a1ce-364d-ac06-3387e866cf67 | -7.01561 | -35.22004 | 2025-10-20 04:12:00 | NOAA-20 | SAPÉ | PARAÍBA | Brasil | 2515302 | 25 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| 1581e339-bd61-3aeb-bc82-5a0b561ac166 | -7.07528 | -45.21099 | 2025-10-20 04:12:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 7e76d298-4339-3566-b491-0866169bbc33 | -7.13261 | -44.24546 | 2025-10-20 04:12:00 | NOAA-20 | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 9.7 |
| 2cf94538-5053-318c-bea8-f769ffed41c3 | -5.62716 | -43.65128 | 2025-10-20 04:12:00 | NOAA-20 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 2820c2d8-88db-3057-a889-55c2526b5089 | -6.21392 | -40.96674 | 2025-10-20 04:12:00 | NOAA-20 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 61a192f3-6852-33a0-9a30-c623c70e9a30 | -6.13867 | -41.80774 | 2025-10-20 04:12:00 | NOAA-20 | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 8044fca9-bf75-349e-adb1-d7acdbc1f6bd | -5.10118 | -43.19608 | 2025-10-20 04:12:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 0c4323ac-83c0-35af-aff5-6900ad19e0e4 | -5.45374 | -43.73506 | 2025-10-20 04:12:00 | NOAA-20 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| e008738a-926e-36f2-b6c0-b51f77c90e4e | -5.60274 | -43.6546 | 2025-10-20 04:12:00 | NOAA-20 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 08e36601-fe8d-3736-972c-b9aec0a32d66 | -5.62883 | -43.64075 | 2025-10-20 04:12:00 | NOAA-20 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 26175306-68d4-3236-9822-be75f7ef72fb | -6.36612 | -46.15514 | 2025-10-20 04:12:00 | NOAA-20 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 03066c82-79bb-349e-9959-36b7d701241a | -1.97391 | -50.81826 | 2025-10-20 04:12:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| d4a0a309-4017-3d3d-b6bd-f06aed0fced8 | -6.98534 | -39.70044 | 2025-10-20 04:12:00 | NOAA-20 | ALTANEIRA | CEARÁ | Brasil | 2300606 | 23 | 33 | nan | nan | nan | Caatinga | 0.8 |
| b2384061-9c09-3eec-be48-a95ff983f61f | -7.13709 | -44.23891 | 2025-10-20 04:12:00 | NOAA-20 | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 976a4df4-3e18-3bbd-9897-05a2f4167ccd | -5.90334 | -43.90088 | 2025-10-20 04:12:00 | NOAA-20 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| c60048a7-1fa4-340e-9283-c7d92ec9077d | -5.88548 | -43.92691 | 2025-10-20 04:12:00 | NOAA-20 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 1d82c39c-5a0d-3cc8-a26d-abe75c04fd2e | -6.30222 | -40.89228 | 2025-10-20 04:12:00 | NOAA-20 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| de0519e1-fa26-314a-b34d-d46c593bd3ca | -6.20062 | -41.5336 | 2025-10-20 04:12:00 | NOAA-20 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 0e129ba3-d4b2-3aa7-9fdb-039af7ea8d6f | -6.10086 | -44.02609 | 2025-10-20 04:12:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 743ca910-8ae1-3fce-9a3f-ec1554fcaff3 | -4.4574 | -43.75933 | 2025-10-20 04:12:00 | NOAA-20 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 4b8074dc-53ae-3778-946d-ef07ec2ffbe3 | -6.28385 | -44.41555 | 2025-10-20 04:12:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| a4887f38-46cf-3852-a807-08398684803b | -6.31366 | -40.90929 | 2025-10-20 04:12:00 | NOAA-20 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 3d993470-9fb3-33f9-9068-b3111230698d | -5.75495 | -44.58994 | 2025-10-20 04:12:00 | NOAA-20 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| c584704c-7ed4-3c4d-a5a7-1dca63621b9c | -7.14172 | -46.52166 | 2025-10-20 04:12:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 1380e4c8-698b-3a66-b9bf-9e9479e7f3df | -6.21222 | -40.97783 | 2025-10-20 04:12:00 | NOAA-20 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 3f5f4d4e-811b-3fe8-bd00-7093510c3965 | -4.83268 | -42.74692 | 2025-10-20 04:12:00 | NOAA-20 | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Cerrado | 22.2 |
| 0e6b01b8-0cd9-3c28-abbb-29262f1fd730 | -6.24749 | -39.81545 | 2025-10-20 04:12:00 | NOAA-20 | CATARINA | CEARÁ | Brasil | 2303600 | 23 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 2d56a7d5-a6ef-3eef-a62f-60e943958b01 | -3.5874 | -41.65706 | 2025-10-20 04:12:00 | NOAA-20 | COCAL | PIAUÍ | Brasil | 2202703 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| a18da223-f68e-3950-95af-0f6f7648631a | -4.83458 | -45.80103 | 2025-10-20 04:12:00 | NOAA-20 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 462616c8-b77b-31d3-9f92-bf0a58d1ac6b | -8.15931 | -38.63187 | 2025-10-20 04:12:00 | NOAA-20 | MIRANDIBA | PERNAMBUCO | Brasil | 2609303 | 26 | 33 | nan | nan | nan | Caatinga | 25.9 |
| 2cad2c2f-3ec6-3489-9788-7a945dc571d8 | -8.42686 | -44.1204 | 2025-10-20 04:14:00 | NOAA-20 | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 3.5 |
| b3752412-39b8-355f-ab75-0c6015ef49ce | -8.07396 | -48.02726 | 2025-10-20 04:14:00 | NOAA-20 | PALMEIRANTE | TOCANTINS | Brasil | 1715705 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 845e539a-4051-3f41-9bb3-36e12ae40814 | -10.54982 | -43.37035 | 2025-10-20 04:14:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 5ef66681-c972-3ee0-b304-aaac7f9e3a33 | -8.31314 | -46.80399 | 2025-10-20 04:14:00 | NOAA-20 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 5e7e972c-e76a-341f-a226-a13e83ddb2d0 | -10.95226 | -47.57212 | 2025-10-20 04:14:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| f720d07c-7753-3572-8193-b66af5eef414 | -8.43121 | -44.15705 | 2025-10-20 04:14:00 | NOAA-20 | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 38c08d6b-cf6d-3afe-b97f-7c43a2b4bf80 | -8.42629 | -44.1239 | 2025-10-20 04:14:00 | NOAA-20 | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 33b45090-81af-37ea-81b6-78153c3b75fa | -14.19393 | -51.5405 | 2025-10-20 04:14:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 83623964-5dce-3e94-8870-c09408ecd234 | -8.07255 | -48.01138 | 2025-10-20 04:14:00 | NOAA-20 | PALMEIRANTE | TOCANTINS | Brasil | 1715705 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 3eb68327-33f7-39ed-863b-82e4ee85b3e2 | -9.76219 | -41.91892 | 2025-10-20 04:14:00 | NOAA-20 | SENTO SÉ | BAHIA | Brasil | 2930204 | 29 | 33 | nan | nan | nan | Caatinga | 2.9 |
| 05c77d0c-bd41-3c62-8cdd-0b7a0f357996 | -10.59157 | -48.00419 | 2025-10-20 04:14:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 1ef6bf43-3cec-37d7-a21f-a7578ef528f9 | -10.15856 | -42.21235 | 2025-10-20 04:14:00 | NOAA-20 | SENTO SÉ | BAHIA | Brasil | 2930204 | 29 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 6737a40a-7a86-352d-bac0-f29547af21d3 | -10.85184 | -43.91339 | 2025-10-20 04:14:00 | NOAA-20 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 34636390-a168-3740-9d59-1015cf687d89 | -10.15518 | -42.21181 | 2025-10-20 04:14:00 | NOAA-20 | SENTO SÉ | BAHIA | Brasil | 2930204 | 29 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 2525a9f5-7145-3b1b-83d0-245cdaae6e6c | -8.71994 | -49.59716 | 2025-10-20 04:14:00 | NOAA-20 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| d70d67f7-d04e-38b4-8e92-df97602aa19e | -10.95301 | -47.56767 | 2025-10-20 04:14:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 5dec9bcc-dadf-3396-aeef-7d942415c1df | -13.0158 | -43.97427 | 2025-10-20 04:14:00 | NOAA-20 | SANTANA | BAHIA | Brasil | 2928208 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 90370500-2e94-36d0-9ef7-7dee707b5bb3 | -13.36785 | -44.28564 | 2025-10-20 04:14:00 | NOAA-20 | SANTA MARIA DA VITÓRIA | BAHIA | Brasil | 2928109 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| fd78c5fd-3acb-3242-8415-b6492fac5aae | -10.86992 | -47.46031 | 2025-10-20 04:14:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 49dacbad-c71f-338d-adf1-c2458ebc6d5f | -8.43729 | -44.16163 | 2025-10-20 04:14:00 | NOAA-20 | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 84a33675-607e-3c5f-b7a9-5f559d82081b | -8.42793 | -44.13496 | 2025-10-20 04:14:00 | NOAA-20 | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 15.6 |
| bec69bc7-b774-3813-9536-941918588e79 | -11.87837 | -50.14108 | 2025-10-20 04:14:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| b462da99-8fc0-3d38-a7a4-b6b61b6f9473 | -10.52443 | -43.35907 | 2025-10-20 04:14:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 93ed4461-798a-39f4-92a2-a3063656941b | -10.21961 | -44.06532 | 2025-10-20 04:14:00 | NOAA-20 | JÚLIO BORGES | PIAUÍ | Brasil | 2205524 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 2e471176-0ec4-3b59-8f41-8597f71a08fd | -8.43069 | -44.13903 | 2025-10-20 04:14:00 | NOAA-20 | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 966e986a-22c6-303f-990b-2b16081cd87f | -10.86173 | -44.51502 | 2025-10-20 04:14:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 4f460a7e-c923-34bc-bebf-d34308e93cca | -14.18858 | -51.53166 | 2025-10-20 04:14:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 44c8949c-c224-3934-be36-a5e4402f5525 | -8.7149 | -49.60054 | 2025-10-20 04:14:00 | NOAA-20 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| ec5f9282-5af5-399f-a872-6d8ee8be5249 | -8.07466 | -48.01936 | 2025-10-20 04:14:00 | NOAA-20 | PALMEIRANTE | TOCANTINS | Brasil | 1715705 | 17 | 33 | nan | nan | nan | Cerrado | 13.4 |
| 521d2318-b265-3e7f-a23d-76f4685ad4b7 | -7.85061 | -49.65582 | 2025-10-20 04:14:00 | NOAA-20 | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| ce1b0469-e366-3e1a-8a9c-aead31b85f10 | -14.1922 | -51.53714 | 2025-10-20 04:14:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| a71a8ddb-60fa-3229-8de8-f0f237c5b281 | -10.49715 | -47.55558 | 2025-10-20 04:14:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 7ded0e47-2e23-33a7-a52f-a6da53d8db73 | -10.52112 | -43.35853 | 2025-10-20 04:14:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 5be5bdbc-6b95-359b-b2fe-bbf7f20f510c | -7.8413 | -47.11452 | 2025-10-20 04:14:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 45b528ad-d749-3724-b9dd-57bc570e2c94 | -9.27761 | -43.29617 | 2025-10-20 04:14:00 | NOAA-20 | CARACOL | PIAUÍ | Brasil | 2202505 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| e1d00739-8999-3cc8-888b-13619ace4a32 | -10.66533 | -47.62205 | 2025-10-20 04:14:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| df049417-d815-317b-8565-cb65db2c350f | -13.15483 | -43.06934 | 2025-10-20 04:14:00 | NOAA-20 | BOM JESUS DA LAPA | BAHIA | Brasil | 2903904 | 29 | 33 | nan | nan | nan | Caatinga | 1.2 |
| e60f06de-d14a-36d9-aba6-aa790df267c4 | -11.01129 | -47.89003 | 2025-10-20 04:14:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 41309e3a-5e71-3fe0-aeb6-3f83b1d32785 | -10.95377 | -47.56316 | 2025-10-20 04:14:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| d5f9a797-ed36-385b-896b-451c523cffb4 | -10.87065 | -47.45599 | 2025-10-20 04:14:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 470feffa-0665-33e8-9546-480462231d17 | -10.8939 | -47.44903 | 2025-10-20 04:14:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| d14b8b6a-c462-3eb4-8c0b-f902410686c2 | -14.19034 | -51.53505 | 2025-10-20 04:14:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| a2497188-d815-38ea-a0d2-fe02c3fdff80 | -8.71563 | -49.59641 | 2025-10-20 04:14:00 | NOAA-20 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b9f16143-dbfc-3d86-b866-4a462886a645 | -13.01967 | -43.97127 | 2025-10-20 04:14:00 | NOAA-20 | SANTANA | BAHIA | Brasil | 2928208 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| a29af11e-c0a7-396b-b659-e6eef9be9a38 | -9.56918 | -40.33609 | 2025-10-20 04:14:00 | NOAA-20 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 41.8 |
| 5508211d-a1cc-3b58-8f5d-fa3a05d82e1c | -14.19136 | -51.54173 | 2025-10-20 04:14:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| a2fcb22b-bfb1-37d5-9ef5-8c6c17421ba7 | -11.87764 | -50.14511 | 2025-10-20 04:14:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| f0b57dbe-954f-3343-82da-21cf2e6e3be8 | -13.1582 | -43.06988 | 2025-10-20 04:14:00 | NOAA-20 | BOM JESUS DA LAPA | BAHIA | Brasil | 2903904 | 29 | 33 | nan | nan | nan | Caatinga | 1.2 |
| a73afa9d-13a9-3315-9763-2fe1c0ebefd4 | -12.01947 | -41.47221 | 2025-10-20 04:14:00 | NOAA-20 | MULUNGU DO MORRO | BAHIA | Brasil | 2922052 | 29 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 5ecf7ddf-ae13-3276-aca6-d7b424696207 | -8.42354 | -44.11986 | 2025-10-20 04:14:00 | NOAA-20 | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 2.9 |
| e5fd38c0-b26d-3e5c-8e56-1278895df3e4 | -13.01911 | -43.97482 | 2025-10-20 04:14:00 | NOAA-20 | SANTANA | BAHIA | Brasil | 2928208 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 0e91b51b-58fa-3bbc-a5dc-e116872492eb | -8.43397 | -44.16109 | 2025-10-20 04:14:00 | NOAA-20 | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 935e942b-696e-3682-96e7-64c7ed4857b7 | -10.66087 | -47.62582 | 2025-10-20 04:14:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 9f2498b3-6ae0-3ca2-92d5-fd8229cd962e | -9.76558 | -41.91948 | 2025-10-20 04:14:00 | NOAA-20 | SENTO SÉ | BAHIA | Brasil | 2930204 | 29 | 33 | nan | nan | nan | Caatinga | 2.9 |
| 31bb11b8-61ef-3571-a485-2834d7869ee3 | -8.35108 | -47.29228 | 2025-10-20 04:14:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 675a34f0-ce99-36ee-8ad3-0a5b114b1861 | -9.56554 | -40.33555 | 2025-10-20 04:14:00 | NOAA-20 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 41.8 |
| ffc547a5-9ee9-3d19-be1e-2c1c1b01d603 | -9.34419 | -40.66269 | 2025-10-20 04:14:00 | NOAA-20 | PETROLINA | PERNAMBUCO | Brasil | 2611101 | 26 | 33 | nan | nan | nan | Caatinga | 0.4 |
| e685aa83-a850-3969-a588-71fa52914709 | -11.87619 | -50.15319 | 2025-10-20 04:14:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 4dc3908c-b071-3003-adfa-fcac5f0b46d1 | -8.42797 | -44.11341 | 2025-10-20 04:14:00 | NOAA-20 | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| ba276fd2-b9a8-332e-bac5-49919ff0ff12 | -8.0748 | -48.0222 | 2025-10-20 04:14:00 | NOAA-20 | PALMEIRANTE | TOCANTINS | Brasil | 1715705 | 17 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 9547ee9d-409d-3f29-ac91-f5d42f61fb45 | -8.07379 | -48.02441 | 2025-10-20 04:14:00 | NOAA-20 | PALMEIRANTE | TOCANTINS | Brasil | 1715705 | 17 | 33 | nan | nan | nan | Cerrado | 5.9 |
| dbacd33a-b330-3dff-a26e-35ac898b3fff | -14.19304 | -51.53256 | 2025-10-20 04:14:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |


[Clique aqui para ver as próximas entradas](README14.md)
