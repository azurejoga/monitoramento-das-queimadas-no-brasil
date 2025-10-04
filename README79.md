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

## Dados Diários - Página 79

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| c03f325f-df83-3cc9-ac49-8487965e08be | -12.64153 | -46.98003 | 2025-10-04 04:14:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 7447d55e-62cc-3d54-a194-a811ceab8fa9 | -13.77664 | -47.81956 | 2025-10-04 04:14:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 1f916a6c-f0e4-3374-9037-739551d4609b | -9.90804 | -45.96102 | 2025-10-04 04:14:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 47a4cc26-1258-3eb1-b7af-d140216c2a19 | -11.14426 | -47.89478 | 2025-10-04 04:14:00 | NOAA-20 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 2efdf2ee-0d2a-3a19-aecf-b3f942f016f4 | -13.12915 | -47.91795 | 2025-10-04 04:14:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 8.7 |
| 8906e0ca-a55e-3492-8ec2-b2ea5c4e2e20 | -12.27848 | -55.13467 | 2025-10-04 04:14:00 | NOAA-20 | VERA | MATO GROSSO | Brasil | 5108501 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 7c1337e8-0a6e-3fcd-b6ec-ff25236b1bcc | -11.4262 | -43.48859 | 2025-10-04 04:14:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 668b2f0f-b20c-3819-a540-0bf4942b638a | -13.96955 | -48.18298 | 2025-10-04 04:14:00 | NOAA-20 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 406a1402-0c7b-3ef0-aa14-0de68f5e346b | -8.56057 | -44.64009 | 2025-10-04 04:14:00 | NOAA-20 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| c8d943b3-ca6e-398d-ace5-9c0bb0108d69 | -8.63478 | -43.98356 | 2025-10-04 04:14:00 | NOAA-20 | CRISTINO CASTRO | PIAUÍ | Brasil | 2203107 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 91c5f291-b76d-3f6b-8434-77faf0542e68 | -10.81476 | -46.73475 | 2025-10-04 04:14:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| abe225d4-c7b1-358c-831a-8cd45ccc5874 | -11.49401 | -43.55364 | 2025-10-04 04:14:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 61d86039-de14-37f2-9598-1e62ca4b81c9 | -9.99432 | -48.27974 | 2025-10-04 04:14:00 | NOAA-20 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 53545b1d-9793-3475-a705-bc0492b0883d | -11.49663 | -44.99678 | 2025-10-04 04:14:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 3.2 |
| da38c011-9588-39a3-959b-2975f7c84010 | -10.02672 | -44.01084 | 2025-10-04 04:14:00 | NOAA-20 | AVELINO LOPES | PIAUÍ | Brasil | 2201101 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 150e5ce7-d07c-3806-9d05-03c79862c63f | -9.94591 | -50.23883 | 2025-10-04 04:14:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 5f6fd058-8413-3063-a3d9-56810abe9ea9 | -12.57753 | -54.74266 | 2025-10-04 04:14:00 | NOAA-20 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 143a9a7b-11e1-39ff-96ac-f239f0c184b5 | -11.15292 | -43.39039 | 2025-10-04 04:14:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Caatinga | 1.1 |
| e50eb891-1cf9-3a1b-9615-27436a38dbf7 | -12.10911 | -43.44085 | 2025-10-04 04:14:00 | NOAA-20 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| fb559327-8a48-3c58-b1b3-1fd6da889ec5 | -11.90851 | -49.93686 | 2025-10-04 04:14:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| bd982e0f-34aa-32b6-aa8a-37428010eb39 | -7.77705 | -46.25606 | 2025-10-04 04:14:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| de4d3d46-542b-3007-b4c8-57d4e11d5e46 | -8.8553 | -46.74569 | 2025-10-04 04:14:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 5.1 |
| b3bce432-86bd-325a-a435-45440787a872 | -11.13115 | -47.85945 | 2025-10-04 04:14:00 | NOAA-20 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 48309142-527e-395f-ba81-db1dad24448c | -12.10584 | -45.15946 | 2025-10-04 04:14:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 873f580b-95bd-3895-b072-39f455618faa | -8.89592 | -45.02252 | 2025-10-04 04:14:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 3be18aa5-402d-3679-8ff7-ebbde29af186 | -13.10521 | -47.90464 | 2025-10-04 04:14:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| c1b4dd58-4b88-39a7-82ae-df1be48d591e | -11.11738 | -47.89474 | 2025-10-04 04:14:00 | NOAA-20 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 7.8 |
| 464a12e3-171f-3225-a128-d4cf8d3a70fa | -13.74411 | -48.09673 | 2025-10-04 04:14:00 | NOAA-20 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 10.5 |
| 058e573c-1765-3cb7-9544-2889bac98f98 | -7.85808 | -48.20586 | 2025-10-04 04:14:00 | NOAA-20 | PALMEIRANTE | TOCANTINS | Brasil | 1715705 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| dcc8a97e-0108-36ba-af0c-5bdef148db22 | -13.20822 | -47.80793 | 2025-10-04 04:14:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 899a1fa8-d8d6-3b5b-a429-53a68df43e95 | -12.07029 | -45.19385 | 2025-10-04 04:14:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 4b47fe8b-96cc-362f-ad3f-5d6fd9171e50 | -13.12841 | -47.92226 | 2025-10-04 04:14:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 8.7 |
| 43ba4873-02db-3323-acda-c5afe82b6457 | -8.84695 | -46.79593 | 2025-10-04 04:14:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| c6167efb-efe0-3f24-a6d3-2f1c840d11ca | -12.29378 | -45.36326 | 2025-10-04 04:14:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| d3507ec0-2034-3899-8c96-156d4dfcf80e | -11.90643 | -46.37709 | 2025-10-04 04:14:00 | NOAA-20 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 3edd7228-74a4-3204-bac1-db5ac90a94ac | -14.90867 | -48.28735 | 2025-10-04 04:14:00 | NOAA-20 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 702a4367-d046-3d94-abe1-cfce5e348582 | -13.9333 | -48.15343 | 2025-10-04 04:14:00 | NOAA-20 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| e999a26f-6139-3b48-906f-7751bcc846dd | -14.66549 | -48.30445 | 2025-10-04 04:14:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 7.4 |
| 093457c0-91cf-3028-b393-cacf6aff4fbe | -13.52062 | -47.27596 | 2025-10-04 04:14:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 4.2 |
| cb557476-d4c5-3974-9919-f89ab5b424af | -8.62237 | -54.9847 | 2025-10-04 04:14:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d4016b03-b605-3fb4-94db-c768307af3c2 | -10.12529 | -52.34805 | 2025-10-04 04:14:00 | NOAA-20 | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 6c17f4d2-0e84-3bd6-adf1-f2fcba2babd2 | -12.09095 | -45.17168 | 2025-10-04 04:14:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 122383f8-3fee-355b-996f-900dde34f3f2 | -8.75962 | -49.91273 | 2025-10-04 04:14:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 29a7eb06-334b-3383-a345-fa27b3ef4b07 | -11.11139 | -47.87673 | 2025-10-04 04:14:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| be14f510-4549-3fcb-ae68-679ac69d24e0 | -8.90175 | -46.59889 | 2025-10-04 04:14:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| e721365e-68b0-36fa-909f-03786aff383c | -13.73761 | -48.09083 | 2025-10-04 04:14:00 | NOAA-20 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| fa81e577-e06b-3050-ae58-ce226a58c080 | -13.32471 | -48.09174 | 2025-10-04 04:14:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 51cd8905-237d-3895-a0b2-92b6e8941df4 | -14.44629 | -46.118 | 2025-10-04 04:14:00 | NOAA-20 | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| a6661311-b3f6-3353-a168-8ea12b58fafe | -14.89311 | -48.35595 | 2025-10-04 04:14:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.8 |
| a262be13-c49d-39fd-aa6d-bccff909fdee | -9.11336 | -44.39149 | 2025-10-04 04:14:00 | NOAA-20 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| d7707074-ce85-3a95-9cd5-0966394651dd | -13.85272 | -47.92379 | 2025-10-04 04:14:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 2803decb-5e65-354e-b3a6-6d88ae24614a | -13.74392 | -47.94539 | 2025-10-04 04:14:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 3c918c75-507b-3fa6-984f-317449372e43 | -11.00065 | -46.68618 | 2025-10-04 04:14:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 98b5f857-4fba-34e5-9fc4-ce41822b0e2d | -14.3018 | -45.87242 | 2025-10-04 04:14:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 0d304b44-9be9-37f7-91a0-3b57c1f57114 | -14.4364 | -46.15775 | 2025-10-04 04:14:00 | NOAA-20 | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 29955634-3d8b-33eb-9511-1a58d2096e64 | -13.32754 | -47.19453 | 2025-10-04 04:14:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 8867d2e5-6d57-3eac-87c3-a5c3c696834d | -9.94933 | -43.74778 | 2025-10-04 04:14:00 | NOAA-20 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 029de462-cd84-36eb-9d8a-b3d29673f2b6 | -12.70541 | -48.5767 | 2025-10-04 04:14:00 | NOAA-20 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 38724adb-9769-31cc-9988-bddcefc23e09 | -12.23415 | -47.77509 | 2025-10-04 04:14:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| e3f34374-5d7b-3360-9b84-cc55a83d396b | -15.16136 | -48.01937 | 2025-10-04 04:14:00 | NOAA-20 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| c84ee0d5-8e89-3b5c-8945-0b8579de3381 | -12.63952 | -46.99213 | 2025-10-04 04:14:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 041b4b4a-41ad-3f0e-8cb7-46d95b9da57f | -10.99848 | -46.67759 | 2025-10-04 04:14:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 8ab2ecdc-2764-3840-96e9-7fe69a235e4f | -10.19205 | -45.48429 | 2025-10-04 04:14:00 | NOAA-20 | SÃO GONÇALO DO GURGUÉIA | PIAUÍ | Brasil | 2209757 | 22 | 33 | nan | nan | nan | Cerrado | 0.6 |
| e6d84455-e3a8-398d-a492-f72a8ba311ae | -9.94457 | -50.89373 | 2025-10-04 04:14:00 | NOAA-20 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 9e8742db-e21c-312e-98d6-3d1c4fbc19cf | -13.33318 | -47.62922 | 2025-10-04 04:14:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 062155f5-f2bb-3370-a40d-d9e24d152bec | -8.46756 | -47.41725 | 2025-10-04 04:14:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 8baa96d1-280f-36e3-9bd6-26d440e66836 | -13.28566 | -47.18322 | 2025-10-04 04:14:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 9a033f0d-0d2d-3608-b59a-7ddbde4b550b | -9.63123 | -55.13701 | 2025-10-04 04:14:00 | NOAA-20 | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| e88b7585-c16b-3b01-a3ef-fcc55414b314 | -8.6155 | -54.99179 | 2025-10-04 04:14:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 7febba72-0eca-3229-8583-80a4820c3491 | -11.48447 | -44.98748 | 2025-10-04 04:14:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 96012211-1e2c-31af-9f87-0ae1a12c4eba | -7.79936 | -47.62538 | 2025-10-04 04:14:00 | NOAA-20 | BARRA DO OURO | TOCANTINS | Brasil | 1703073 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 4d70a981-2391-3eea-a2cc-8155c37798f8 | -11.49938 | -45.00092 | 2025-10-04 04:14:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| f4a37ca3-8c34-3b28-b0c8-54890f453ea6 | -13.98184 | -48.19921 | 2025-10-04 04:14:00 | NOAA-20 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 6.3 |
| ec9bc637-6892-3a4f-b6e3-4a377e16dd54 | -15.36094 | -46.28049 | 2025-10-04 04:14:00 | NOAA-20 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| ef55e697-922b-36ac-a08d-775856d64d46 | -13.54413 | -47.24384 | 2025-10-04 04:14:00 | NOAA-20 | TERESINA DE GOIÁS | GOIÁS | Brasil | 5221080 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 5d6a50d2-faa4-3d2d-9c32-cdd2191c797b | -13.6842 | -48.02898 | 2025-10-04 04:14:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 89b8cedb-77f0-3d23-83de-fe6746c2eafc | -14.88996 | -48.28759 | 2025-10-04 04:14:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| cd23e99e-0f4e-3787-a855-20ae3c85ff58 | -11.86475 | -44.97039 | 2025-10-04 04:14:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 9c34db2c-d4fb-3c5e-9a0c-39373ae880b5 | -14.30573 | -45.86936 | 2025-10-04 04:14:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 94ab68e9-1e33-30cb-a0ef-1cc6ae1f40a7 | -14.2072 | -46.08088 | 2025-10-04 04:14:00 | NOAA-20 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 92c9ddb4-1c8b-3bb3-83dd-d40fe3a53941 | -14.37923 | -48.47998 | 2025-10-04 04:14:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 3492e417-392a-3b37-883d-55d395a74ec1 | -12.27462 | -55.12906 | 2025-10-04 04:14:00 | NOAA-20 | VERA | MATO GROSSO | Brasil | 5108501 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 93d92779-36aa-3523-8b64-18310740e648 | -14.23563 | -46.0971 | 2025-10-04 04:14:00 | NOAA-20 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 575387ff-96ca-39ef-9faa-56754bfb93d3 | -7.72543 | -49.85363 | 2025-10-04 04:14:00 | NOAA-20 | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 3381aeff-cdc0-3e24-9da6-4fd2de1c6a23 | -13.55223 | -48.21116 | 2025-10-04 04:14:00 | NOAA-20 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 3f76d244-34b5-3694-9027-5fd7d1860635 | -13.26485 | -47.22151 | 2025-10-04 04:14:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 32403d42-ea7e-3933-bf14-cd97374e55cd | -13.47164 | -47.26463 | 2025-10-04 04:14:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 70da7a26-601c-3c5d-a41b-ea17e912b953 | -15.35111 | -46.25624 | 2025-10-04 04:14:00 | NOAA-20 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| e9cfc418-ddbd-373d-8102-41ab08adb24c | -13.32536 | -47.18604 | 2025-10-04 04:14:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| ef10a7b0-8e14-3384-a57e-dd75a94ee227 | -12.28343 | -55.14019 | 2025-10-04 04:14:00 | NOAA-20 | VERA | MATO GROSSO | Brasil | 5108501 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 24f51cc5-6d93-35c4-8443-8382a079a1fe | -14.92503 | -46.88186 | 2025-10-04 04:14:00 | NOAA-20 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 42865a94-2833-308f-bc0c-5e22165d2bc0 | -11.79299 | -46.82745 | 2025-10-04 04:14:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 7.0 |
| f1721ce0-47c5-35df-bfbd-50453530448f | -9.94873 | -50.24525 | 2025-10-04 04:14:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 3e81875c-0095-345e-ac2b-91db052725cd | -13.50662 | -47.27327 | 2025-10-04 04:14:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| b941d451-86d0-3a2c-a141-fd427cc482fb | -9.51555 | -54.7139 | 2025-10-04 04:14:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 60cc703b-f0da-32cc-8010-b545226cd7db | -12.91846 | -46.79443 | 2025-10-04 04:14:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 1dbeaee3-ebdd-389a-b752-c009fa69b549 | -13.33432 | -47.57999 | 2025-10-04 04:14:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 94a93312-dd85-35f1-a953-a22925d56dc3 | -13.59092 | -48.17865 | 2025-10-04 04:14:00 | NOAA-20 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 46308952-6442-379b-8182-3fbac57ee6c3 | -14.29079 | -47.42022 | 2025-10-04 04:14:00 | NOAA-20 | ALTO PARAÍSO DE GOIÁS | GOIÁS | Brasil | 5200605 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| e764152a-f68b-3694-8495-5731439a1580 | -10.5946 | -48.69899 | 2025-10-04 04:14:00 | NOAA-20 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |


[Clique aqui para ver as próximas entradas](README80.md)
