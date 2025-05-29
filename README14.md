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

## Dados Diários - Página 14

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 646ea120-5373-3e96-9f14-ea86e8ce5e2b | -8.09151 | -46.28827 | 2025-05-29 05:04:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 3ceec53f-38a9-306b-a727-a5115daffbf2 | -3.04863 | -49.44006 | 2025-05-29 05:04:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 86760cd1-691d-3887-85a6-83c58db392f6 | -7.07567 | -44.91759 | 2025-05-29 05:04:00 | NOAA-21 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 3459792d-e805-373b-9bb5-8994e70f9ada | -8.40683 | -47.09502 | 2025-05-29 05:04:00 | NOAA-21 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| d232cf16-4beb-3846-94a8-db8ee8165109 | -7.23314 | -43.09443 | 2025-05-29 05:04:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 5.5 |
| b584b164-7df0-391b-bd0c-38b2fcda1d9d | -9.2027 | -49.4743 | 2025-05-29 05:04:00 | NOAA-21 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 17.3 |
| ebeb2400-972f-3adc-a4ee-c34cbd55d65f | -9.21255 | -49.47224 | 2025-05-29 05:04:00 | NOAA-21 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| c1d85755-2346-3aba-97b1-3464364f9601 | -6.909 | -47.85655 | 2025-05-29 05:04:00 | NOAA-21 | WANDERLÂNDIA | TOCANTINS | Brasil | 1722081 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| f125d4e9-579b-3563-b8ff-d34d8ee98fdd | -10.53069 | -47.58397 | 2025-05-29 05:04:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| ac1403a8-cb2d-31c6-b1cc-de5eedca3d43 | -10.65469 | -44.49355 | 2025-05-29 05:04:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 9f53fc92-7952-3608-b805-5f10ba75789f | -9.96732 | -49.80949 | 2025-05-29 05:04:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 61f9318d-1098-3b08-865a-c5f7a73a2e9a | -9.35765 | -57.54457 | 2025-05-29 05:04:00 | NOAA-21 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 79d4faf7-7c3b-3458-ba3a-9adebaf8cddf | -7.62407 | -45.74381 | 2025-05-29 05:04:00 | NOAA-21 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| dd387704-f0db-3ef3-9b81-0a02b1a36aa0 | -8.00912 | -46.14813 | 2025-05-29 05:04:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 6b340c7c-2222-342e-afd7-674e17e2ca61 | -6.8288 | -44.65172 | 2025-05-29 05:04:00 | NOAA-21 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 10.2 |
| a64c477f-00e0-3b78-aa8f-f4a4d8efc6d4 | -10.53109 | -47.58073 | 2025-05-29 05:04:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| f1a5ec7d-9757-3dd8-8ac2-fe7850fcad58 | -9.35318 | -57.55112 | 2025-05-29 05:04:00 | NOAA-21 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| bcb07951-4ac1-3026-a905-b80fb17bfb4e | -5.21847 | -43.30715 | 2025-05-29 05:04:00 | NOAA-21 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 5.8 |
| d42174bf-ecae-3d3c-8cad-5a6dcb0159d5 | -7.23911 | -43.10157 | 2025-05-29 05:04:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 6.8 |
| a25c2798-68de-3d7b-986e-caf53274f18e | -9.80495 | -47.74184 | 2025-05-29 05:04:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| cd7ee659-be3e-3e50-85f9-2c7ed5fb142c | -7.63447 | -45.92838 | 2025-05-29 05:04:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| a293de80-cb2f-3d6a-904c-d496f6fd4b8f | -7.6727 | -46.09457 | 2025-05-29 05:04:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 2f9f949c-a371-367c-a939-db6dc290a28d | -3.04805 | -49.44385 | 2025-05-29 05:04:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 8d66d716-3d62-3f77-bdc2-77b328a54ef1 | -6.80325 | -45.36549 | 2025-05-29 05:04:00 | NOAA-21 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 6.6 |
| baeb17a1-2faf-339a-b37b-7258cd978766 | -7.64017 | -45.9292 | 2025-05-29 05:04:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 3c48984b-31e3-3457-b44a-f0b18cbafd6e | -8.1976 | -49.81304 | 2025-05-29 05:04:00 | NOAA-21 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| fce380c9-297f-3b3a-ae02-fc9acf6d3c63 | -8.74849 | -49.76744 | 2025-05-29 05:04:00 | NOAA-21 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| a62a0ec5-d52b-3e0b-8c31-12ed0af62c85 | -7.67783 | -46.09926 | 2025-05-29 05:04:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 5.4 |
| ec4b5a40-e29e-37a0-b884-52878530a3f6 | -6.82813 | -44.65667 | 2025-05-29 05:04:00 | NOAA-21 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 10.2 |
| f16f9135-bf69-3458-93ba-f6202b02c4e5 | -6.63415 | -55.01151 | 2025-05-29 05:04:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 0dc3d504-cf78-3431-b0ed-d022ef79bfd6 | -6.83488 | -44.6529 | 2025-05-29 05:04:00 | NOAA-21 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 7b529137-0671-317b-aa68-d337e87e2521 | -5.88658 | -49.82985 | 2025-05-29 05:04:00 | NOAA-21 | PARAUAPEBAS | PARÁ | Brasil | 1505536 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| cf93c487-1069-31fd-8925-b33dd30b1359 | -4.81873 | -47.32199 | 2025-05-29 05:04:00 | NOAA-21 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 864bf6a8-a883-31e4-a766-22d59ab1ca33 | -7.58419 | -45.8687 | 2025-05-29 05:04:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| ebc43ccc-acad-30c3-82fe-32d7cc32594c | -9.25039 | -56.32471 | 2025-05-29 05:04:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 2471ca48-a9fb-3e6d-b0a5-154212816875 | -10.64806 | -48.80153 | 2025-05-29 05:04:00 | NOAA-21 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 36aef567-9837-3502-8048-c562705aaa5f | -6.8295 | -44.64651 | 2025-05-29 05:04:00 | NOAA-21 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 8.2 |
| bf296a9c-9c33-3900-a5f1-5e8534a33396 | -10.46793 | -47.95164 | 2025-05-29 05:04:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 537d5256-c6e2-38e4-9bf3-e7157b062992 | -8.74307 | -49.76355 | 2025-05-29 05:04:00 | NOAA-21 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 56d13b0b-289e-3cf3-95b8-a2849c3b86d3 | -5.10885 | -44.44994 | 2025-05-29 05:04:00 | NOAA-21 | PRESIDENTE DUTRA | MARANHÃO | Brasil | 2109106 | 21 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 46d2321f-505e-3453-8d33-8a8d27ad8b9e | -7.63393 | -45.93232 | 2025-05-29 05:04:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 5a6ada78-78f8-3f53-9592-fdf030293bfd | -4.82106 | -44.35453 | 2025-05-29 05:04:00 | NOAA-21 | SANTO ANTÔNIO DOS LOPES | MARANHÃO | Brasil | 2110302 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 270287b1-c27e-3469-b991-f17d7326e86b | -3.58414 | -48.95045 | 2025-05-29 05:04:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 904242d4-4292-354e-9f4c-ab829783badc | -10.53236 | -47.58067 | 2025-05-29 05:04:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 9a78a259-e26e-3453-9139-bac954d17a73 | -6.6347 | -55.00801 | 2025-05-29 05:04:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 6705b225-36a5-3692-89e3-a627efc45887 | -7.65753 | -47.61462 | 2025-05-29 05:04:00 | NOAA-21 | BARRA DO OURO | TOCANTINS | Brasil | 1703073 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 1fee1cc2-093d-3d5b-9b32-a85fe5aa8aaf | -7.6334 | -45.93625 | 2025-05-29 05:04:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 3a5b5001-429f-343f-8473-bae89683ccb0 | -8.00345 | -46.14748 | 2025-05-29 05:04:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 125e4cf3-c01f-3b82-b575-aa0c566fd28b | -9.11072 | -46.93033 | 2025-05-29 05:04:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 8472f88d-179f-3989-9820-bda570f846e2 | -7.68386 | -49.62859 | 2025-05-29 05:04:00 | NOAA-21 | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| c6f57111-83c7-3fdd-9f71-1c53151b9423 | -4.11783 | -54.91626 | 2025-05-29 05:04:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 0.3 |
| c37f17bb-5d62-3244-a45e-d0fadd115429 | -8.78866 | -47.94276 | 2025-05-29 05:04:00 | NOAA-21 | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 0113e03e-f810-3d6e-afca-45b3fb27908e | -9.29676 | -50.43367 | 2025-05-29 05:04:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| e73e6dd3-f4ee-3e9b-89a2-dc32a873ad34 | -8.09712 | -46.28904 | 2025-05-29 05:04:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 87ed5d3c-e004-3f9e-bf8e-baade888627b | -7.9468 | -44.85748 | 2025-05-29 05:04:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 3.6 |
| c79a4207-9725-310a-a7b1-4a88ef1a680d | -5.21774 | -43.31264 | 2025-05-29 05:04:00 | NOAA-21 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 08bf4251-f1b1-39eb-8be9-c9a7dcdf62f1 | -8.02205 | -49.68526 | 2025-05-29 05:04:00 | NOAA-21 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| baa8bdba-0477-30a9-8d8a-c197595c142e | -7.08111 | -44.923 | 2025-05-29 05:04:00 | NOAA-21 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 7eaf14fe-ec9f-368a-b2f1-3df75b7757e7 | -6.21715 | -57.77466 | 2025-05-29 05:04:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 7.0 |
| 83f82214-d60e-337e-975a-b104bc2f5e3c | -7.46934 | -47.05889 | 2025-05-29 05:04:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 4ed91227-d2d9-33ef-ae0a-033c62a2bb29 | -5.21199 | -43.30589 | 2025-05-29 05:04:00 | NOAA-21 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 5.8 |
| ce128c92-2753-34b2-8499-2078a5690f65 | -5.21701 | -43.31815 | 2025-05-29 05:04:00 | NOAA-21 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 0ce221ec-ece2-3f48-96e6-b5531e879521 | -10.64877 | -48.7961 | 2025-05-29 05:04:00 | NOAA-21 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| b244df51-686d-34fd-b115-82047cdb1341 | -6.24311 | -43.37968 | 2025-05-29 05:04:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 88472931-18bc-31a9-88a5-0f15842b11b9 | -7.26414 | -49.51237 | 2025-05-29 05:04:00 | NOAA-21 | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| ab785670-57f6-3148-87e2-392fc82d28fa | -9.4 | -48.42145 | 2025-05-29 05:04:00 | NOAA-21 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| aba04348-de1a-3a64-a38a-f980156d1a77 | -10.67773 | -44.41035 | 2025-05-29 05:04:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 8.7 |
| 3eeac711-65a3-3aba-b3f1-f0bf07d98cb9 | -10.63824 | -48.80024 | 2025-05-29 05:04:00 | NOAA-21 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 4.5 |
| f9ee931f-5e77-3164-b28f-1b16dd2003f5 | -9.35652 | -57.55166 | 2025-05-29 05:04:00 | NOAA-21 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 80a07e01-2d19-3aeb-a205-300b4f697c53 | -8.45554 | -48.33164 | 2025-05-29 05:04:00 | NOAA-21 | PRESIDENTE KENNEDY | TOCANTINS | Brasil | 1718402 | 17 | 33 | nan | nan | nan | Cerrado | 4.9 |
| bafc9530-855a-3412-b2ed-1181f1f92cf6 | -9.35375 | -57.54758 | 2025-05-29 05:04:00 | NOAA-21 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| fc3f454f-e54a-320b-a9a4-e5620273b688 | -8.01784 | -46.21208 | 2025-05-29 05:04:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| c4b79164-882d-32b0-bdf3-549817dade1b | -7.58985 | -45.95808 | 2025-05-29 05:04:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| cd7a558d-36c3-3a5f-bf67-dd68f44a987f | -7.0799 | -44.93214 | 2025-05-29 05:04:00 | NOAA-21 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 931cde48-972b-3b0a-8d65-44cf22f55b53 | -9.21192 | -49.47699 | 2025-05-29 05:04:00 | NOAA-21 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| b48a962e-7f87-3ad3-9a02-e37ea2f3bcdb | -9.20734 | -49.47628 | 2025-05-29 05:04:00 | NOAA-21 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 18.4 |
| 98f26dbb-b768-3782-8cef-53682cc3074f | -7.19455 | -43.1083 | 2025-05-29 05:04:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 5.9 |
| 668f40a9-2c30-331b-be8e-7a9ccd3a5aa8 | -7.27881 | -44.22356 | 2025-05-29 05:04:00 | NOAA-21 | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 29d259da-c220-3344-bc3c-96c3a23085c9 | -8.74403 | -49.76676 | 2025-05-29 05:04:00 | NOAA-21 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| d578d0df-a472-35d3-a8e7-591c8c4099ba | -10.6571 | -49.44052 | 2025-05-29 05:06:00 | NOAA-21 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| a9168ce1-a179-3036-8fdd-917126d50dea | -11.28335 | -46.43507 | 2025-05-29 05:06:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 35689cc1-982e-34e2-be1a-30f477bbb5da | -10.82946 | -56.95264 | 2025-05-29 05:06:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 5760f4c8-cd71-3924-a237-cc64c38f09a3 | -10.83058 | -54.0342 | 2025-05-29 05:06:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| bb43c7eb-576f-356c-b7ab-d79ade67a25f | -11.97192 | -52.45916 | 2025-05-29 05:06:00 | NOAA-21 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 6.5 |
| 048ae356-f10d-3364-aee2-1bfaad464fc8 | -10.93612 | -55.31327 | 2025-05-29 05:06:00 | NOAA-21 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b5f755eb-8eb7-3519-b27d-f55aae494f50 | -11.1399 | -53.92306 | 2025-05-29 05:06:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 78bf4a97-757d-339f-b327-34cc980e2388 | -12.42296 | -53.32413 | 2025-05-29 05:06:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 78250940-04ed-3b24-b240-34b38e38f302 | -14.67171 | -45.08729 | 2025-05-29 05:06:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 3.4 |
| eeedc6de-a390-3c32-a420-e8d59a010224 | -10.73108 | -49.2903 | 2025-05-29 05:06:00 | NOAA-21 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 6.8 |
| c68977d9-72f4-3d16-a299-b0dbb7cbf1fd | -11.81051 | -55.07215 | 2025-05-29 05:06:00 | NOAA-21 | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 22fbc80f-ca09-3d38-8ad2-b7340b751bbc | -10.32607 | -57.49177 | 2025-05-29 05:06:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 9d1835d0-fdba-3477-a15d-23f4f8292f7a | -15.07958 | -48.94582 | 2025-05-29 05:06:00 | NOAA-21 | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| bf21cbea-2e2b-35d0-b8be-04401309a13a | -10.95189 | -48.1474 | 2025-05-29 05:06:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| b6ad9d61-954b-3cf3-b38c-a1ca37114d8a | -10.95149 | -48.15055 | 2025-05-29 05:06:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 19efee32-8421-343a-a5fc-d4458d575196 | -10.95069 | -48.15681 | 2025-05-29 05:06:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 21e0130b-88ea-345e-a1d1-a2c3e7b8d4a3 | -11.80367 | -55.07108 | 2025-05-29 05:06:00 | NOAA-21 | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 506e241a-6f14-3da6-98e4-6a3eb8b26ee8 | -10.19444 | -52.64925 | 2025-05-29 05:06:00 | NOAA-21 | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| e9522606-f298-3361-8a12-3dc6599f6d17 | -10.6524 | -49.43986 | 2025-05-29 05:06:00 | NOAA-21 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 922473c5-52b8-31ae-a0ea-7a7b6d6dcbe4 | -10.81997 | -54.03261 | 2025-05-29 05:06:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| fcaaadb0-d79a-33ea-b422-e7d4ed1243f8 | -11.08097 | -55.0515 | 2025-05-29 05:06:00 | NOAA-21 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |


[Clique aqui para ver as próximas entradas](README15.md)
