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

## Dados Diários - Página 73

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 3847b94e-5488-36be-9edb-5af05f9cff7b | -15.38556 | -48.0036 | 2025-10-08 04:40:00 | NOAA-20 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 11d86f67-18a0-3f2b-8368-8e18d8267c0d | -13.58541 | -48.68108 | 2025-10-08 04:40:00 | NOAA-20 | TROMBAS | GOIÁS | Brasil | 5221452 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 985f0d7c-0e0e-3725-b79b-f48ecd72d616 | -11.12147 | -54.05129 | 2025-10-08 04:40:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 0ad35d82-c035-3659-aa99-094aff019419 | -15.61046 | -52.57917 | 2025-10-08 04:40:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 090f6cb7-0dee-34ad-ab41-f86d7ca39092 | -11.44888 | -50.21534 | 2025-10-08 04:40:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| c4673746-3579-357d-8f4e-76a5e2c69f09 | -18.02772 | -51.14888 | 2025-10-08 04:40:00 | NOAA-20 | RIO VERDE | GOIÁS | Brasil | 5218805 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 7b8c94e4-989d-3207-b146-c1ebe0aa596f | -11.50446 | -51.48727 | 2025-10-08 04:40:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 1bababe7-c23f-3aab-af25-39a79cf87ef2 | -11.70091 | -50.96252 | 2025-10-08 04:40:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 0e08a186-16f5-3f5b-8471-be9401214f07 | -12.29015 | -55.10273 | 2025-10-08 04:40:00 | NOAA-20 | VERA | MATO GROSSO | Brasil | 5108501 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| a9043979-34ca-356d-8ae3-014b59dd7c5b | -15.35859 | -47.32991 | 2025-10-08 04:40:00 | NOAA-20 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 61eef262-77c5-3ac0-9426-ae03e05623e9 | -16.13321 | -47.91022 | 2025-10-08 04:40:00 | NOAA-20 | CIDADE OCIDENTAL | GOIÁS | Brasil | 5205497 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 14d58c60-5980-322f-9a2f-6d61917721e3 | -10.97487 | -59.02809 | 2025-10-08 04:40:00 | NOAA-20 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| c97a5eed-ac96-3c44-a124-92a67e0e984e | -14.52512 | -46.63648 | 2025-10-08 04:40:00 | NOAA-20 | ALVORADA DO NORTE | GOIÁS | Brasil | 5200803 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 0bb05d58-d891-342c-a3f8-283b2b19d0e9 | -15.38526 | -46.2796 | 2025-10-08 04:40:00 | NOAA-20 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 2.2 |
| d833b0c8-d0da-33db-836e-188dec99e428 | -15.25566 | -50.20371 | 2025-10-08 04:40:00 | NOAA-20 | FAINA | GOIÁS | Brasil | 5207535 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| b240b132-e506-3023-bc62-bf916b1892da | -15.4007 | -48.00147 | 2025-10-08 04:40:00 | NOAA-20 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| ddfdd745-5a5d-3800-9160-275ddb80cac2 | -15.60376 | -52.57807 | 2025-10-08 04:40:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 1416d47a-1c49-3e65-a582-e89b9a2840e6 | -11.71311 | -50.95006 | 2025-10-08 04:40:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 17.4 |
| 44d026fa-5622-3880-a9df-84f1f8bba3d0 | -14.70944 | -48.40066 | 2025-10-08 04:40:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| d6263d91-4ab9-3c9f-b9ae-3df1fd90b5fe | -17.37409 | -45.0584 | 2025-10-08 04:40:00 | NOAA-20 | BURITIZEIRO | MINAS GERAIS | Brasil | 3109402 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 8cd85b5d-1026-36f8-9f7a-24bf13197f60 | -12.94089 | -46.85214 | 2025-10-08 04:40:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| d0b7a159-81cb-33fb-bec9-b65cb01fa465 | -12.51183 | -54.71379 | 2025-10-08 04:40:00 | NOAA-20 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 767cf496-d552-3fb7-93ca-445fef31cf12 | -12.99373 | -46.78082 | 2025-10-08 04:40:00 | NOAA-20 | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 14.1 |
| ea160483-7810-31ea-95cf-62abc868676a | -17.38303 | -45.05959 | 2025-10-08 04:40:00 | NOAA-20 | BURITIZEIRO | MINAS GERAIS | Brasil | 3109402 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 8932bef5-c78c-3f65-a753-f222ba1c7f7e | -15.56343 | -43.84764 | 2025-10-08 04:40:00 | NOAA-20 | VARZELÂNDIA | MINAS GERAIS | Brasil | 3170909 | 31 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 8fd815ac-eb89-3410-b0b8-b64daa3200db | -15.53995 | -47.52093 | 2025-10-08 04:40:00 | NOAA-20 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 977db89c-de7a-3440-97c8-41a0c4c24c05 | -19.47013 | -45.96134 | 2025-10-08 04:40:00 | NOAA-20 | SANTA ROSA DA SERRA | MINAS GERAIS | Brasil | 3159704 | 31 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 6c4d1126-1986-3710-a0b9-0e577bff3f6d | -11.94273 | -51.46743 | 2025-10-08 04:40:00 | NOAA-20 | SERRA NOVA DOURADA | MATO GROSSO | Brasil | 5107883 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| ea312fcf-39cf-3a12-b5db-c5d73e4efdd4 | -19.26699 | -44.12191 | 2025-10-08 04:40:00 | NOAA-20 | JEQUITIBÁ | MINAS GERAIS | Brasil | 3135704 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 04dfd4d7-530d-3e18-a8a2-1df6123696e3 | -18.02106 | -51.14777 | 2025-10-08 04:40:00 | NOAA-20 | RIO VERDE | GOIÁS | Brasil | 5218805 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| d1e0484f-b9ad-37ef-bb4e-8ab4298058aa | -14.45295 | -48.79659 | 2025-10-08 04:40:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| a5dfe2ac-30c8-35d2-b04c-d3eb04b84dc8 | -12.94376 | -46.86359 | 2025-10-08 04:40:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| ea9b2768-dee9-3600-a696-1d016be88707 | -13.754 | -45.74941 | 2025-10-08 04:40:00 | NOAA-20 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| ac58a177-ab01-304b-83df-adc65d11c6cf | -12.02518 | -45.20572 | 2025-10-08 04:40:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 9.2 |
| c6772425-981b-342b-8cb4-1b032d16ec41 | -15.39769 | -47.99642 | 2025-10-08 04:40:00 | NOAA-20 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 6ed98bf3-748a-38b8-9cdc-44e3d6c97f34 | -17.28409 | -42.65876 | 2025-10-08 04:40:00 | NOAA-20 | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 18f8b8cd-c495-3442-bd32-d60b1987d1f9 | -11.94793 | -46.42557 | 2025-10-08 04:40:00 | NOAA-20 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 0ff195c2-1a90-3faf-a025-e221b16527da | -16.18234 | -51.74904 | 2025-10-08 04:40:00 | NOAA-20 | ARENÓPOLIS | GOIÁS | Brasil | 5202353 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| acce850c-2a4e-3d20-ac7b-cb4da7d8e329 | -15.55908 | -46.84837 | 2025-10-08 04:40:00 | NOAA-20 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 6d105a67-6d22-3d6b-ab9b-6c2cd64894a0 | -16.59673 | -46.55138 | 2025-10-08 04:40:00 | NOAA-20 | NATALÂNDIA | MINAS GERAIS | Brasil | 3144375 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| cecaf868-73ee-3774-a44a-24bafad607b7 | -11.69097 | -50.96088 | 2025-10-08 04:40:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 03797586-e6b7-300a-9615-3e68f9b125fe | -13.26079 | -47.7875 | 2025-10-08 04:40:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 1a150267-64eb-34a4-a60f-0104cd14f6ce | -17.85098 | -44.31697 | 2025-10-08 04:40:00 | NOAA-20 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 20e21a8a-9f5b-3533-af12-a3f26e12cac0 | -12.35132 | -50.28564 | 2025-10-08 04:40:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| c66b85f4-52ac-3a6d-b59d-6e606854d61b | -12.36672 | -46.49236 | 2025-10-08 04:40:00 | NOAA-20 | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 12.1 |
| 84f709b3-c59f-3cfb-9615-24195b168168 | -11.7463 | -50.93382 | 2025-10-08 04:40:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 9.6 |
| f5322b79-c4c5-32d7-b1a6-ff909706a618 | -15.6365 | -52.54599 | 2025-10-08 04:40:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| fc9a9543-4b74-30cd-b60a-77404ca09ab5 | -11.17126 | -54.86906 | 2025-10-08 04:40:00 | NOAA-20 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 95265a1b-b272-30f3-adb7-7b7a8ff2f14c | -16.6045 | -58.15734 | 2025-10-08 04:40:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.0 |
| e019b8b8-564f-3b65-bd9a-9571182605e4 | -12.31029 | -55.10831 | 2025-10-08 04:40:00 | NOAA-20 | VERA | MATO GROSSO | Brasil | 5108501 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 9c5dd3f1-4949-37f3-8d51-d894a94e2a5e | -17.27524 | -58.11236 | 2025-10-08 04:40:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.2 |
| d442b6a3-19f3-3cc7-adb5-8ad25090d482 | -13.72394 | -45.66652 | 2025-10-08 04:40:00 | NOAA-20 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 4616dc84-fd68-300e-be76-963f512e06a0 | -11.12587 | -54.89504 | 2025-10-08 04:40:00 | NOAA-20 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 21b12503-974d-359e-beea-fb147e89ffdb | -15.3015 | -47.96532 | 2025-10-08 04:40:00 | NOAA-20 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 7340df70-bca5-3917-a1d6-e054e445dc78 | -11.74798 | -50.92326 | 2025-10-08 04:40:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 36.9 |
| bd154707-4244-3def-9a56-d04040a035fe | -17.15535 | -43.44091 | 2025-10-08 04:40:00 | NOAA-20 | ITACAMBIRA | MINAS GERAIS | Brasil | 3132008 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| ffd5e202-8efb-3a27-8ca2-71fc27524613 | -12.01388 | -45.1965 | 2025-10-08 04:40:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 5dd63c80-5b90-3ca7-bca1-6301604627e9 | -17.14279 | -45.7908 | 2025-10-08 04:40:00 | NOAA-20 | BRASILÂNDIA DE MINAS | MINAS GERAIS | Brasil | 3108552 | 31 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 2ec4f574-8c1b-3c3a-94eb-73fcfbfba796 | -15.64021 | -52.56548 | 2025-10-08 04:40:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 87c0bbd3-1a9e-3a4f-897a-243fe4d19f3d | -13.31382 | -48.02393 | 2025-10-08 04:40:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.6 |
| cd8eb16d-9337-3098-8725-2e8d189c2521 | -11.13447 | -54.89148 | 2025-10-08 04:40:00 | NOAA-20 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 50b0841f-fb0f-3eee-8742-4b4d31881519 | -14.71202 | -46.08281 | 2025-10-08 04:40:00 | NOAA-20 | SÍTIO D'ABADIA | GOIÁS | Brasil | 5220702 | 52 | 33 | nan | nan | nan | Cerrado | 4.5 |
| f2e2cc11-ee54-3897-b1a5-cc37e346f079 | -12.04371 | -47.77333 | 2025-10-08 04:40:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 290a5f14-8ae5-3595-9e8b-cb1643216c8b | -14.94688 | -46.79457 | 2025-10-08 04:40:00 | NOAA-20 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| bc969097-7ea3-3962-a5ca-b51ad21cf94a | -12.38735 | -51.13259 | 2025-10-08 04:40:00 | NOAA-20 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| a464dcdc-56e8-34bb-be5c-dd221a6ad9c1 | -14.82668 | -48.41413 | 2025-10-08 04:40:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| aa40d0b7-da16-3614-8da4-c2e55a670d19 | -17.36011 | -45.06124 | 2025-10-08 04:40:00 | NOAA-20 | BURITIZEIRO | MINAS GERAIS | Brasil | 3109402 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| d6dc003d-60ed-3a31-bb1d-4fdc01602446 | -11.93882 | -51.47042 | 2025-10-08 04:40:00 | NOAA-20 | SERRA NOVA DOURADA | MATO GROSSO | Brasil | 5107883 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 3124fca8-6eae-3d99-86ce-85b3d1819f91 | -10.88613 | -56.06657 | 2025-10-08 04:40:00 | NOAA-20 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| ec5908fb-ae28-3654-a8c8-973f294d5ccf | -15.28316 | -45.34342 | 2025-10-08 04:40:00 | NOAA-20 | JANUÁRIA | MINAS GERAIS | Brasil | 3135209 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| a6853bdc-671d-3176-a20f-b20c2ff0ee6e | -12.93513 | -46.86547 | 2025-10-08 04:40:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 5.2 |
| c34abd83-4ee2-3a60-b4b3-93134622a1f7 | -15.31867 | -46.16395 | 2025-10-08 04:40:00 | NOAA-20 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 5.2 |
| c1786aa8-caf0-3c74-85d7-8b9de79b2277 | -18.44758 | -42.91224 | 2025-10-08 04:40:00 | NOAA-20 | PAULISTAS | MINAS GERAIS | Brasil | 3148400 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 03b317cd-5049-37ee-87ac-30b537c7bc03 | -11.14241 | -54.87428 | 2025-10-08 04:40:00 | NOAA-20 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| dc95067b-de4f-3ced-b064-dd073e3dd944 | -14.62092 | -48.13735 | 2025-10-08 04:40:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| d2e5cb60-e486-325e-8ad9-34f742a063cf | -15.32179 | -46.1715 | 2025-10-08 04:40:00 | NOAA-20 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 14.3 |
| 956ed6f0-445f-3a21-b349-b4fc45727d6b | -11.73748 | -50.92515 | 2025-10-08 04:40:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 5c027432-ea67-3343-a357-d2fe0bf2c6aa | -13.05493 | -47.89129 | 2025-10-08 04:40:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 4e129b32-6d68-32a0-adac-feb500a00a25 | -14.24767 | -45.86686 | 2025-10-08 04:40:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 8d514c84-3a86-30f0-91db-2d31c1eeca5c | -14.6493 | -52.53333 | 2025-10-08 04:40:00 | NOAA-20 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| acc3377c-5973-33b1-8d53-98b1817b4a1d | -12.12226 | -45.12861 | 2025-10-08 04:40:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 165ff18b-59e0-3a4a-aa86-140725079e33 | -11.13595 | -54.88828 | 2025-10-08 04:40:00 | NOAA-20 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| cd4858ed-931e-39de-92ac-7c2df1c16a8d | -18.29982 | -45.4426 | 2025-10-08 04:40:00 | NOAA-20 | SÃO GONÇALO DO ABAETÉ | MINAS GERAIS | Brasil | 3161700 | 31 | 33 | nan | nan | nan | Cerrado | 3.0 |
| a15bc3e2-b54a-33ec-850e-51482c4dd6e8 | -13.78671 | -45.81342 | 2025-10-08 04:40:00 | NOAA-20 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 64bb4a03-f202-3db2-918c-567c0c8d579c | -12.23193 | -47.86729 | 2025-10-08 04:40:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| ac4e259b-24c0-3869-84e4-5bbbde668f5a | -12.17966 | -57.23745 | 2025-10-08 04:40:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 86df2f8d-0aeb-3e74-b72e-c9936acc15ca | -11.75129 | -50.92381 | 2025-10-08 04:40:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 36.9 |
| 13ea5bdd-eb68-3cd7-9290-56a23fd75b23 | -15.25877 | -46.35553 | 2025-10-08 04:40:00 | NOAA-20 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 3.3 |
| b3d2f4ad-bcd6-3e5c-a827-143d3f8daed2 | -15.63315 | -52.54544 | 2025-10-08 04:40:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 0438c5b7-608f-38e1-a9dc-b4badd902763 | -13.22597 | -47.17488 | 2025-10-08 04:40:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 7acc69e8-316b-34a4-baa4-aa7d011c7a43 | -14.28926 | -44.76217 | 2025-10-08 04:40:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 1a337345-7fe8-3ae8-8a7e-780139bbbc7c | -13.26437 | -48.48592 | 2025-10-08 04:40:00 | NOAA-20 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| ee835707-17ff-3db8-a01c-fda014223b86 | -11.71367 | -50.94654 | 2025-10-08 04:40:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 53.8 |
| 88149f2e-7a82-304c-905d-5009cca6284c | -12.5035 | -54.71704 | 2025-10-08 04:40:00 | NOAA-20 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 0bd45967-89cf-3159-b193-2fd420f78450 | -11.16695 | -54.89383 | 2025-10-08 04:40:00 | NOAA-20 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 7.7 |
| 622faed1-75eb-31f4-ac1a-a884b38fcdef | -12.02108 | -45.20511 | 2025-10-08 04:40:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 325eb57c-d409-3f2f-90e8-8a1d2a90ca43 | -10.86932 | -53.74531 | 2025-10-08 04:40:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 455b3d64-d266-3ee2-93d1-42a6f241c7fd | -11.37834 | -54.34558 | 2025-10-08 04:40:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 21a51bfe-1017-32ee-a819-3a647049d2cd | -18.54886 | -41.57439 | 2025-10-08 04:40:00 | NOAA-20 | NOVA MÓDICA | MINAS GERAIS | Brasil | 3144904 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.9 |
| 365d3755-19f1-3e11-a14a-70efbd19461d | -11.16955 | -54.87888 | 2025-10-08 04:40:00 | NOAA-20 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 9.4 |


[Clique aqui para ver as próximas entradas](README74.md)
