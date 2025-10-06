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

## Dados Diários - Página 64

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 6bdffb2d-4b92-3f8e-ada7-b9d484c08ec7 | -8.61884 | -54.97204 | 2025-10-06 05:16:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 7b7980d2-11ba-35c3-9d79-96b33ac388c4 | -10.67181 | -48.47326 | 2025-10-06 05:16:00 | NOAA-20 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| d930c2ec-f00b-3396-bd6f-c9e3347a380b | -8.11845 | -55.08343 | 2025-10-06 05:16:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 9dabedfd-3faf-3c37-ae18-da75db871e24 | -11.32293 | -54.34354 | 2025-10-06 05:16:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| f91d6941-0ec0-35be-9485-dbc954eb7470 | -8.55225 | -46.25484 | 2025-10-06 05:16:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| d1375c3c-1b0f-3a0b-b452-f0b8e7980591 | -9.23099 | -51.82069 | 2025-10-06 05:16:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| de441899-8aba-32d3-8ae4-4cdaa3c63d6e | -10.67778 | -48.47558 | 2025-10-06 05:16:00 | NOAA-20 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| dc49b011-9c2d-322f-88d7-8513b86f0b65 | -5.64606 | -50.30985 | 2025-10-06 05:16:00 | NOAA-20 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 02896e21-b0d4-38f1-ad4b-1997d48fd804 | -8.11915 | -55.07874 | 2025-10-06 05:16:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| b71c777d-055a-367f-93b1-7db279aede9a | -6.54831 | -47.86385 | 2025-10-06 05:16:00 | NOAA-20 | DARCINÓPOLIS | TOCANTINS | Brasil | 1706506 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 0f33a800-2a2c-3f6b-a654-07988fd78f29 | -11.41587 | -55.06842 | 2025-10-06 05:16:00 | NOAA-20 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| b394265c-a1bb-3e13-9109-801afc12440f | -11.50431 | -54.46895 | 2025-10-06 05:16:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| bab93ce4-1d4d-3df6-9082-89a42d14d51f | -5.66039 | -48.92529 | 2025-10-06 05:16:00 | NOAA-20 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 30f441df-d834-38d5-bb23-92ba8780fda9 | -8.62028 | -54.96243 | 2025-10-06 05:16:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 77a91823-40bd-343b-ad9e-43de8edfefd5 | -7.21212 | -45.90872 | 2025-10-06 05:16:00 | NOAA-20 | FORTALEZA DOS NOGUEIRAS | MARANHÃO | Brasil | 2104107 | 21 | 33 | nan | nan | nan | Cerrado | 10.0 |
| 3679cf5d-bd73-376d-974d-c99ca529fca8 | -7.24801 | -59.53573 | 2025-10-06 05:16:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| e8f1a95e-1954-3c32-beec-05e3edd7e3cc | -11.50794 | -54.47336 | 2025-10-06 05:16:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b17ebdf0-cfc2-35bf-baee-e46c09450411 | -12.25375 | -49.20442 | 2025-10-06 05:16:00 | NOAA-20 | FIGUEIRÓPOLIS | TOCANTINS | Brasil | 1707652 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 965387d0-0743-30b8-ab04-a792b4e96a12 | -11.49966 | -54.4721 | 2025-10-06 05:16:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d58ae850-71af-33af-93f1-e17f58c0219a | -10.34366 | -51.2482 | 2025-10-06 05:16:00 | NOAA-20 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 3e4e3b8e-04cf-3824-be70-5ef8f3bc3a04 | -9.31814 | -59.67865 | 2025-10-06 05:16:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 212e85fc-daed-3a7e-a5a1-43b84ef92916 | -9.27243 | -51.80077 | 2025-10-06 05:16:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 91c45f83-ae6b-3dbc-bbba-b0c0d2bcafa9 | -6.36723 | -58.20647 | 2025-10-06 05:16:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 587a5b2a-0e38-3dce-ba19-3670142337e7 | -10.42552 | -50.35228 | 2025-10-06 05:16:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 2862da20-7fb0-3501-a02e-879ab1410518 | -11.45991 | -51.52511 | 2025-10-06 05:16:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| b192ae78-cd76-343d-b016-90682d956ba6 | -9.48199 | -54.6019 | 2025-10-06 05:16:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 118be0b9-324f-3dad-a425-58c660bd4300 | -8.61595 | -54.99128 | 2025-10-06 05:16:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 731c35f2-b852-302e-ad15-2b5c9b587a72 | -12.41582 | -51.12265 | 2025-10-06 05:16:00 | NOAA-20 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 11ea6ed9-fe00-3a9b-a466-efdc8e020a4c | -9.27176 | -51.80578 | 2025-10-06 05:16:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 06dc6677-8342-3085-8971-cd66661f3e44 | -11.1767 | -54.12091 | 2025-10-06 05:16:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 75ab7455-5010-3e11-b187-a6dd1fe1716b | -10.46308 | -57.89082 | 2025-10-06 05:16:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d5d48d7f-fa73-3b4e-bcf9-6f8751f7d180 | -7.36002 | -64.65766 | 2025-10-06 05:16:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| db83c8f8-e1a4-3f95-b3eb-fdeb6d673e18 | -9.49057 | -56.07718 | 2025-10-06 05:16:00 | NOAA-20 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 105d7b08-d96d-3ef6-b827-f2aac5fb4cca | -10.32672 | -50.27506 | 2025-10-06 05:16:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 666ea7b6-1008-3c98-8afb-82019fb9e6d1 | -10.47417 | -55.59249 | 2025-10-06 05:16:00 | NOAA-20 | COLÍDER | MATO GROSSO | Brasil | 5103205 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 9f92a40d-ab09-3284-967c-b5cf1940c300 | -9.25237 | -51.8078 | 2025-10-06 05:16:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 6d5625c0-edde-3e62-b803-990be52a23b6 | -8.61642 | -54.96187 | 2025-10-06 05:16:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| d6aaf340-aecc-306e-a394-9d1a96c5eee8 | -10.32222 | -50.26734 | 2025-10-06 05:16:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 71695a1e-046e-378c-818e-bdb27fc50b19 | -9.27166 | -51.81023 | 2025-10-06 05:16:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 76c35691-aba7-3f94-aea6-ed57bf5405a2 | -9.24262 | -60.28028 | 2025-10-06 05:16:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 82290809-8d04-3093-8898-de0d22d601b1 | -10.43093 | -50.353 | 2025-10-06 05:16:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 3d2f7516-0ca5-3767-a577-7e61873ba41d | -10.31088 | -51.461 | 2025-10-06 05:16:00 | NOAA-20 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 0.4 |
| e53aabb8-09c1-36d8-893d-75ecba099535 | -11.21373 | -54.98691 | 2025-10-06 05:16:00 | NOAA-20 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| c17422d1-9bd5-3f50-aa98-d6d86e9957ac | -11.07338 | -47.92198 | 2025-10-06 05:16:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 94e1c74d-9778-3a2b-a78b-cccc2b6d5574 | -5.64524 | -50.31565 | 2025-10-06 05:16:00 | NOAA-20 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| d7c21d5c-0cd9-3afa-a87f-a874448ff6b4 | -9.32877 | -54.51866 | 2025-10-06 05:16:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f5b35f17-88f9-3b63-9367-b990be7d6246 | -9.27721 | -51.80562 | 2025-10-06 05:16:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| de35fbfe-377c-370f-a487-3bde3c374b85 | -6.91567 | -59.72285 | 2025-10-06 05:16:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| b426e548-ee75-3c48-870b-4ee1321d13ba | -9.27238 | -51.80507 | 2025-10-06 05:16:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 6250a45a-acca-318b-9fa6-0605b466be80 | -10.6252 | -50.56561 | 2025-10-06 05:16:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 544ed326-20b2-31de-bdb1-d3fc266b4bab | -8.60869 | -54.97314 | 2025-10-06 05:16:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 78e59e9c-8684-3820-8f0f-e0ee2b272cbb | -8.51913 | -46.33757 | 2025-10-06 05:16:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| f7d96f06-aa84-3305-a590-26f7d3ffd391 | -11.42122 | -55.0759 | 2025-10-06 05:16:00 | NOAA-20 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| d2757a03-6c2d-3ee2-924e-73d40ba6beb2 | -8.62235 | -54.96033 | 2025-10-06 05:16:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 5fa39444-b81c-3d9e-9b05-05d408b811c9 | -6.91179 | -59.7258 | 2025-10-06 05:16:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 0ee75fe0-5f76-3257-9b38-31cd60a068dc | -6.55005 | -47.85107 | 2025-10-06 05:16:00 | NOAA-20 | PALMEIRAS DO TOCANTINS | TOCANTINS | Brasil | 1713809 | 17 | 33 | nan | nan | nan | Cerrado | 9.0 |
| 06ae96c1-2ed1-3cea-a813-2afd8d985780 | -9.12295 | -60.39148 | 2025-10-06 05:16:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 60c6a1eb-1473-3cc3-ac5f-a82603f07542 | -10.67126 | -48.47767 | 2025-10-06 05:16:00 | NOAA-20 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| c39b8e0e-258e-379f-bd70-ded101b33dc9 | -11.01065 | -50.67664 | 2025-10-06 05:16:00 | NOAA-20 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 589b3d6d-426c-35a0-b4a6-2ee261154ef8 | -8.42969 | -70.12023 | 2025-10-06 05:16:00 | NOAA-20 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 044a2210-d203-3d36-9d3a-f3b3a3eb762d | -12.41095 | -51.11872 | 2025-10-06 05:16:00 | NOAA-20 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 50f060e6-c4a5-31b5-9a02-32d4be7883a4 | -8.61262 | -46.27129 | 2025-10-06 05:16:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 7effff2b-cbe3-3ae6-b4e4-0e3b1f454d55 | -9.22883 | -51.83643 | 2025-10-06 05:16:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 66ecebeb-1d0f-3d15-8ee7-7586cfaa87d5 | -8.47644 | -54.69315 | 2025-10-06 05:16:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 5dee30bb-7288-3bb2-98c1-5b4bf8355f68 | -6.54889 | -47.85962 | 2025-10-06 05:16:00 | NOAA-20 | PALMEIRAS DO TOCANTINS | TOCANTINS | Brasil | 1713809 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 3d93ace0-f645-3c4c-b92a-310b8b31b8c8 | -10.4305 | -50.35648 | 2025-10-06 05:16:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 22c4eec0-6cd2-39a8-ba65-c3c8bf6824b3 | -8.50213 | -54.59902 | 2025-10-06 05:16:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 4113cee9-0c25-3e90-afb0-72e5f07d1496 | -8.47325 | -54.68753 | 2025-10-06 05:16:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 6a29e04d-0ee0-3072-aa1d-9985ac130705 | -10.05865 | -59.35435 | 2025-10-06 05:16:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| c641c9fb-816a-36be-a188-f379b1c0883f | -8.61186 | -54.97857 | 2025-10-06 05:16:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 183ce32d-0519-3570-8dde-943569f63eac | -10.30548 | -50.26871 | 2025-10-06 05:16:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 6aaa49e9-b403-3639-bc20-04373d387dc1 | -8.61407 | -46.31377 | 2025-10-06 05:16:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 584af5b5-851b-3956-aaf8-009efb819795 | -11.00445 | -50.68267 | 2025-10-06 05:16:00 | NOAA-20 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 0.6 |
| afdfb43a-2319-3eca-9451-4e376c32e271 | -11.02239 | -46.53412 | 2025-10-06 05:16:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 10.4 |
| b932da72-aaef-3091-952c-69e7c8da21c8 | -8.74524 | -50.66767 | 2025-10-06 05:16:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 8407f1f0-72b5-3da4-ade8-b49f1bc0978a | -8.61117 | -46.28253 | 2025-10-06 05:16:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 5.4 |
| f08ed0b1-2c31-3902-8305-48bd726deca6 | -5.13819 | -60.38889 | 2025-10-06 05:16:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 53b830b0-186a-3196-aaec-c91dcff30b3f | -8.6183 | -46.2905 | 2025-10-06 05:16:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 7.2 |
| 13566aa2-2b92-3a47-a8a6-5edfe1c5431a | -8.6182 | -54.98931 | 2025-10-06 05:16:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 0fa932c2-7147-30fe-8af5-3e374351bc25 | -7.91174 | -49.27101 | 2025-10-06 05:16:00 | NOAA-20 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 4e8431bc-7e0a-33f5-8eba-2e26fe630823 | -8.62101 | -54.95758 | 2025-10-06 05:16:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 8535ebfe-124a-3192-898f-f239279e4501 | -10.3624 | -51.18375 | 2025-10-06 05:16:00 | NOAA-20 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 3d7cce04-b39a-36e4-a085-c3a658a6a7a7 | -8.62317 | -46.29692 | 2025-10-06 05:16:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 85e71fe0-7ef8-3d24-9fc7-9529c25e0354 | -11.94921 | -51.47805 | 2025-10-06 05:16:00 | NOAA-20 | SERRA NOVA DOURADA | MATO GROSSO | Brasil | 5107883 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| f5e60dee-cd75-3774-9bcd-d1fe221e78b0 | -9.32828 | -54.52221 | 2025-10-06 05:16:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 03fb6a72-3733-3e5c-887a-4290b69d2aef | -10.42392 | -50.34871 | 2025-10-06 05:16:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 2a07b4ad-19d0-336e-a493-7714f73f16b3 | -9.31483 | -59.67812 | 2025-10-06 05:16:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c415cafe-3f6e-3962-a7b3-a8efe5289cd0 | -7.25132 | -59.53627 | 2025-10-06 05:16:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 93893db2-105c-30a3-91a0-937e4e698d5f | -7.35165 | -55.51641 | 2025-10-06 05:16:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 1b7ebb0c-c93c-3d35-9b46-653ea93dbd37 | -8.62027 | -54.97483 | 2025-10-06 05:16:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| d94d6fdf-45d2-32df-abfb-dc2ed9b0485c | -8.88004 | -62.32541 | 2025-10-06 05:16:00 | NOAA-20 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 0.5 |
| acf7dfaa-dc73-3e14-b2a6-e5064760047b | -8.51 | -54.60025 | 2025-10-06 05:16:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 161b5ccd-8464-301f-9dcb-19fc025bd26e | -11.06703 | -47.92102 | 2025-10-06 05:16:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 106e0b6d-bf8c-396a-8686-cb8c909ff2e7 | -8.60938 | -54.96833 | 2025-10-06 05:16:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 9e73d9db-5789-385b-962e-c7e6fbd44812 | -6.33239 | -55.18913 | 2025-10-06 05:16:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 3437a9a5-dea5-38dd-99a1-080307d446fc | -9.31152 | -59.67758 | 2025-10-06 05:16:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 1a7a5b5e-ed2b-315d-a381-54bb1f53a4b2 | -10.3286 | -50.27582 | 2025-10-06 05:16:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| b075e13d-d112-3eba-b935-a37f22aefb43 | -9.16212 | -58.3109 | 2025-10-06 05:16:00 | NOAA-20 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 14eb6665-64d2-32f4-be7e-c272ab68b321 | -5.64195 | -45.96404 | 2025-10-06 05:16:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 6.0 |
| fce6e2b5-02e3-3fa3-8eab-a5aa4e87e332 | -8.61183 | -54.96615 | 2025-10-06 05:16:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |


[Clique aqui para ver as próximas entradas](README65.md)
