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

## Dados Diários - Página 72

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 02c9ac81-ad2c-354f-959d-0519d646b380 | -14.65662 | -48.31238 | 2025-10-04 04:14:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 4b72e5e1-b0d3-3e29-8cc6-9a741a0199ca | -15.31324 | -46.38219 | 2025-10-04 04:14:00 | NOAA-20 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 4b95714d-8d51-3618-9abf-efb3931ef429 | -13.70043 | -47.35014 | 2025-10-04 04:14:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| fef4a7d9-54fa-3ef4-9051-a9b1893651ac | -11.68482 | -47.49673 | 2025-10-04 04:14:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 165166e4-5f55-3514-b924-0760cc641e59 | -11.47756 | -45.03021 | 2025-10-04 04:14:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| d663004d-c25c-3cf8-9163-c43c2a8bd719 | -11.04935 | -47.79082 | 2025-10-04 04:14:00 | NOAA-20 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| d843a71b-2500-3e2b-87f8-496267388dd8 | -7.77415 | -46.25136 | 2025-10-04 04:14:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| e5fdd58f-7af2-375c-a564-11e9677144a7 | -11.65612 | -46.99574 | 2025-10-04 04:14:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 4f0f95a0-fee7-3a9a-9582-fee1aacba464 | -8.85669 | -46.73729 | 2025-10-04 04:14:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 2e96023f-1741-38eb-8334-60db224fa32a | -12.37192 | -46.50871 | 2025-10-04 04:14:00 | NOAA-20 | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| c1967e68-ce77-3bcd-af82-fd4d28592bd8 | -12.7258 | -48.56917 | 2025-10-04 04:14:00 | NOAA-20 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| db3d8866-7645-3d6a-a76b-97500099d52b | -12.06374 | -45.17079 | 2025-10-04 04:14:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| ed01f7fe-7ae0-3753-9ffd-031bcbb72ee8 | -12.70634 | -48.54861 | 2025-10-04 04:14:00 | NOAA-20 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 5.3 |
| a45e0ee1-ee1f-3e95-a36f-6c8365cf2c80 | -11.13778 | -47.86546 | 2025-10-04 04:14:00 | NOAA-20 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| dccc354a-81e8-3c29-af63-83b1e01dd99e | -11.91679 | -46.39377 | 2025-10-04 04:14:00 | NOAA-20 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 37.6 |
| d8ad41f1-a030-39e6-bdac-7e973b0cfe19 | -11.31675 | -47.83454 | 2025-10-04 04:14:00 | NOAA-20 | SANTA ROSA DO TOCANTINS | TOCANTINS | Brasil | 1718907 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 1f5d2cad-15ff-3a1c-a71d-931ce81199a0 | -9.08292 | -48.02746 | 2025-10-04 04:14:00 | NOAA-20 | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 7.5 |
| ad6813f8-2d4e-3267-ac6e-a2de98254f6d | -11.04342 | -47.80309 | 2025-10-04 04:14:00 | NOAA-20 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 329589e8-3c27-30e7-a3b5-a1d7d39915f5 | -14.21794 | -44.78394 | 2025-10-04 04:14:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 1257e5fd-519c-33dd-905a-ba015ad158f3 | -14.23585 | -46.07439 | 2025-10-04 04:14:00 | NOAA-20 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 81e1881c-28f4-36cf-8680-111ecc4b1555 | -11.11659 | -47.89932 | 2025-10-04 04:14:00 | NOAA-20 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| b78843c8-aa35-3296-b764-2c72d25ae8a0 | -9.75596 | -43.61715 | 2025-10-04 04:14:00 | NOAA-20 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Caatinga | 2.7 |
| 79b63257-9426-3a65-ad25-ae3570c6296c | -12.98552 | -53.43183 | 2025-10-04 04:14:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 798be605-8fd6-3ffa-9c9f-46993bd53884 | -13.4804 | -47.23385 | 2025-10-04 04:14:00 | NOAA-20 | TERESINA DE GOIÁS | GOIÁS | Brasil | 5221080 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 218a880c-1406-3daa-8989-cb880b35df29 | -14.63318 | -48.25165 | 2025-10-04 04:14:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 0e206ba4-c38e-30e4-a183-3fb922e5e3e0 | -13.31885 | -47.61424 | 2025-10-04 04:14:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 7510408b-0b24-3fc0-abc6-b2b14b3d4a28 | -7.77191 | -46.24259 | 2025-10-04 04:14:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| f08ba8b3-8022-3c69-a86c-f7aeb799f246 | -14.46586 | -48.3958 | 2025-10-04 04:14:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 5d7a294f-c828-3a32-a49f-ec4b9d87efbe | -15.52843 | -44.34686 | 2025-10-04 04:14:00 | NOAA-20 | PEDRAS DE MARIA DA CRUZ | MINAS GERAIS | Brasil | 3149150 | 31 | 33 | nan | nan | nan | Caatinga | 1.6 |
| bc0c1fcd-51dd-3e3a-a6c5-ec8ccc8bfcfd | -11.81878 | -44.89725 | 2025-10-04 04:14:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| fe2aa8f7-6507-33b0-84f0-ecc573204e60 | -13.10733 | -47.84878 | 2025-10-04 04:14:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 2df05fd8-56dc-3bae-a740-f03dc4a0fded | -9.08375 | -48.02259 | 2025-10-04 04:14:00 | NOAA-20 | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 8d97e09e-eec3-3550-8f41-7ada596f2c3d | -11.70798 | -47.51444 | 2025-10-04 04:14:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| badc06c8-f2bf-32bf-9768-90f37aa7fa96 | -11.12174 | -44.89919 | 2025-10-04 04:14:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 6e4cb002-d886-30a5-849b-a4777ef8f437 | -9.75486 | -43.62411 | 2025-10-04 04:14:00 | NOAA-20 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 19f2aa1b-2add-3b31-9987-bceff1cefbe1 | -12.72146 | -48.55145 | 2025-10-04 04:14:00 | NOAA-20 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| e51ea75c-bacf-3263-b732-ebc4e22b422b | -9.92532 | -50.89503 | 2025-10-04 04:14:00 | NOAA-20 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 0b9ae556-e72c-3abd-bccb-d9cd5c746f62 | -13.88432 | -46.51087 | 2025-10-04 04:14:00 | NOAA-20 | GUARANI DE GOIÁS | GOIÁS | Brasil | 5209408 | 52 | 33 | nan | nan | nan | Cerrado | 6.4 |
| edffe9e8-f83f-35a1-b6f7-ac211b1ca0bb | -12.65402 | -46.96987 | 2025-10-04 04:14:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| dae4e04a-b17c-3727-94ee-dff8acaebb13 | -13.35112 | -48.06937 | 2025-10-04 04:14:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 49912890-9f7c-309a-b0b8-b7590fd1361c | -9.92996 | -50.20011 | 2025-10-04 04:14:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 13f0a74d-5cc0-3b42-9bf8-3eefaa573634 | -13.99506 | -48.18769 | 2025-10-04 04:14:00 | NOAA-20 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 07146fdb-ab02-311f-bdb4-422305af4db2 | -13.57806 | -47.27839 | 2025-10-04 04:14:00 | NOAA-20 | TERESINA DE GOIÁS | GOIÁS | Brasil | 5221080 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 0d0f7c94-545d-3583-98e1-142e6c770451 | -8.6242 | -54.97532 | 2025-10-04 04:14:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| fdd433c3-8392-363a-9c05-ed2a492a9b48 | -10.84123 | -47.20528 | 2025-10-04 04:14:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| afab3979-f65b-3ded-9a22-d493e92be2d5 | -11.47699 | -45.03376 | 2025-10-04 04:14:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| dcd803bd-ac0d-38d1-bccc-91b898b151e3 | -13.26449 | -46.48097 | 2025-10-04 04:14:00 | NOAA-20 | DIVINÓPOLIS DE GOIÁS | GOIÁS | Brasil | 5208301 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 4ae729ee-dfcb-3d67-acbb-2d966261d0ce | -9.63913 | -54.31419 | 2025-10-04 04:14:00 | NOAA-20 | GUARANTÃ DO NORTE | MATO GROSSO | Brasil | 5104104 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 517fe0c1-22ea-3ace-b3d8-805d30132102 | -15.34449 | -46.29679 | 2025-10-04 04:14:00 | NOAA-20 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 230b5ea6-e64d-3060-9595-16bd4630a03d | -12.03191 | -45.19847 | 2025-10-04 04:14:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 8.4 |
| cdf9f970-c11a-382a-a035-126f6b95dbbb | -13.32887 | -47.57621 | 2025-10-04 04:14:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| f5bc354c-a5f7-3e75-a765-4e902112b76e | -13.32738 | -47.62934 | 2025-10-04 04:14:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 7.1 |
| be444cc5-db0a-3176-819d-25311068b11d | -13.81564 | -43.17736 | 2025-10-04 04:14:00 | NOAA-20 | RIACHO DE SANTANA | BAHIA | Brasil | 2926400 | 29 | 33 | nan | nan | nan | Caatinga | 1.7 |
| c4370d5c-e23a-3bf6-9479-10664119c51a | -11.79677 | -47.91917 | 2025-10-04 04:14:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 30b2d9eb-4b5e-3aca-91e9-55ccd1666c26 | -14.94541 | -46.86486 | 2025-10-04 04:14:00 | NOAA-20 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 4.3 |
| d7b111dd-ed28-31ae-aae5-4be85fef3466 | -10.56512 | -48.70504 | 2025-10-04 04:14:00 | NOAA-20 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 3f4f5dda-326b-3935-8101-887db59bc8bb | -11.87633 | -44.98326 | 2025-10-04 04:14:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 5.3 |
| d583c9a7-391a-3d0a-9d7f-551110f61123 | -8.54982 | -44.79298 | 2025-10-04 04:14:00 | NOAA-20 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 46925993-798d-3f2d-9477-da38ead8811d | -13.1276 | -47.81753 | 2025-10-04 04:14:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 511753e2-7df6-3509-b4bd-64f7c31dd2aa | -13.39458 | -47.54947 | 2025-10-04 04:14:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.9 |
| ec2a7d7b-662e-3859-8169-aac1f3e322ba | -9.90397 | -43.73401 | 2025-10-04 04:14:00 | NOAA-20 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| af564755-8c1b-3c38-8ec1-94bcae1af404 | -9.93567 | -50.89428 | 2025-10-04 04:14:00 | NOAA-20 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 00b75c5f-d840-3e0b-9316-3bd597545613 | -8.90037 | -46.05435 | 2025-10-04 04:14:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 67630fc6-b5ea-38f2-94ef-ff2ebd7c6106 | -13.62602 | -48.66902 | 2025-10-04 04:14:00 | NOAA-20 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 39c5d54b-b7b1-3537-920f-80407dc4ae28 | -13.33174 | -50.93967 | 2025-10-04 04:14:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 11.4 |
| e3d1adcf-6948-3e90-854d-bc5cc6f54c07 | -15.91941 | -43.33508 | 2025-10-04 04:14:00 | NOAA-20 | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| b1778181-883d-3139-a5d8-4c6152b6918a | -12.92834 | -46.37041 | 2025-10-04 04:14:00 | NOAA-20 | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| da0ee4bc-7d10-3e21-8f48-3a2e1db0b548 | -13.29806 | -47.82644 | 2025-10-04 04:14:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 516baf23-e142-3e6c-819b-d563ae9c25af | -15.26127 | -44.12233 | 2025-10-04 04:14:00 | NOAA-20 | ITACARAMBI | MINAS GERAIS | Brasil | 3132107 | 31 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 81db39bb-bf20-3ea5-9a5d-083c9e8342a5 | -15.30927 | -46.3853 | 2025-10-04 04:14:00 | NOAA-20 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 86ecf8b7-4d8a-3be7-a4a4-567ae04b56cc | -11.91808 | -46.38603 | 2025-10-04 04:14:00 | NOAA-20 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 26.6 |
| 1fc9324e-bfec-35ec-bf5e-1aa468812ba8 | -8.63368 | -43.99052 | 2025-10-04 04:14:00 | NOAA-20 | CRISTINO CASTRO | PIAUÍ | Brasil | 2203107 | 22 | 33 | nan | nan | nan | Cerrado | 3.1 |
| b9f87696-87fa-346c-9c03-b18b9117fa9a | -13.34746 | -48.06871 | 2025-10-04 04:14:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 068f1f25-4536-3830-8d58-e4caa213f6d8 | -11.63961 | -45.06069 | 2025-10-04 04:14:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 053f0e0c-8ad6-3b5d-8b83-0feb065efdf5 | -12.59131 | -47.00005 | 2025-10-04 04:14:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 426bb4a3-ad33-39d2-a3a6-bf0b54294a8e | -13.97398 | -48.17902 | 2025-10-04 04:14:00 | NOAA-20 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 00fb5111-fb07-3885-a783-35f04bad886a | -11.47956 | -44.97965 | 2025-10-04 04:14:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| bb012374-8f94-30c6-8242-f043b2dbd933 | -12.70936 | -48.55375 | 2025-10-04 04:14:00 | NOAA-20 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 7a3a54f0-a25c-3104-9d1b-3ef0d7d138b9 | -11.05383 | -47.78696 | 2025-10-04 04:14:00 | NOAA-20 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 52581f8c-aea5-3da0-a67c-a342d2641bb0 | -13.97637 | -48.12094 | 2025-10-04 04:14:00 | NOAA-20 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 26537ae0-71bd-3f7f-80da-c6571dbb17f5 | -12.64086 | -46.98408 | 2025-10-04 04:14:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 6.0 |
| d8ba0e15-106d-32e6-adeb-b616d971c566 | -11.72166 | -44.44025 | 2025-10-04 04:14:00 | NOAA-20 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| f761cd33-061f-3162-aa91-5f8e23735726 | -12.37128 | -46.51257 | 2025-10-04 04:14:00 | NOAA-20 | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 6b32d6e9-abe6-3b16-984b-08d1ff16f4f7 | -10.69902 | -47.9987 | 2025-10-04 04:14:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 27f972cb-44f2-34ed-92a5-2386fc40aea6 | -12.39601 | -46.51303 | 2025-10-04 04:14:00 | NOAA-20 | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 5e17a2f2-26c4-39fb-be7b-91b9bb51067e | -8.6259 | -55.00428 | 2025-10-04 04:14:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 9fb94de3-aaf4-32e0-9bd4-2dc295b44f7c | -10.88762 | -44.30118 | 2025-10-04 04:14:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| de430ef8-f8b7-3545-af2c-a8d7bd8d0e24 | -8.61393 | -54.96622 | 2025-10-04 04:14:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 022f46a3-7812-308c-bea3-bd6200de5c66 | -15.32425 | -45.04743 | 2025-10-04 04:14:00 | NOAA-20 | JANUÁRIA | MINAS GERAIS | Brasil | 3135209 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 6ea42e42-2c49-34cc-a6fa-afcbc4c62411 | -11.90782 | -49.94075 | 2025-10-04 04:14:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 0197ddd1-018e-32e2-9e84-3298e9722c7e | -8.9176 | -46.61456 | 2025-10-04 04:14:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| d8e1b94e-d58f-360e-9684-43e997f25eab | -11.48203 | -45.02368 | 2025-10-04 04:14:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 6145641d-cce4-3cdc-8690-d85a20dcbd7d | -12.038 | -45.20314 | 2025-10-04 04:14:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 4.1 |
| eaa471f9-f45f-3053-86dc-db157e1e0c2e | -14.92633 | -46.87405 | 2025-10-04 04:14:00 | NOAA-20 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 55e1aa63-55f9-3774-b481-1b6c7b2126d7 | -12.09437 | -45.15032 | 2025-10-04 04:14:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| ef8308c3-ee75-3b71-a88a-4dfb1fa3f807 | -11.92405 | -46.37146 | 2025-10-04 04:14:00 | NOAA-20 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 19.1 |
| adb458d2-c7c1-3117-81e1-1c749d797747 | -13.52684 | -47.30334 | 2025-10-04 04:14:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| ff209a16-7397-307d-9411-eecf615270b0 | -8.62165 | -54.99289 | 2025-10-04 04:14:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 9c007ef5-0f99-3726-bc51-1169e0f7114b | -13.67501 | -47.3065 | 2025-10-04 04:14:00 | NOAA-20 | TERESINA DE GOIÁS | GOIÁS | Brasil | 5221080 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| bee916ee-2141-31c4-abaf-a42b6369711c | -14.92911 | -46.87844 | 2025-10-04 04:14:00 | NOAA-20 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |


[Clique aqui para ver as próximas entradas](README73.md)
