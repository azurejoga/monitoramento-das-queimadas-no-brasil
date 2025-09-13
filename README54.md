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

## Dados Diários - Página 54

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 8051f0c0-7a22-336b-b91e-efe21b81d399 | -13.00075 | -46.73689 | 2025-09-13 04:08:00 | NOAA-20 | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 3.7 |
| cc697c57-5b86-3f91-9fb0-4875de4087b4 | -11.70712 | -46.55833 | 2025-09-13 04:08:00 | NOAA-20 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| b8c55ea7-5bf7-394e-a805-f2c65bc80879 | -14.20395 | -46.28135 | 2025-09-13 04:08:00 | NOAA-20 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 79d47373-1e61-31ba-806d-02ecfd250fd7 | -10.42847 | -50.63352 | 2025-09-13 04:08:00 | NOAA-20 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 3f7bff81-6bed-3bd2-a051-d6b1feb83cf6 | -11.8704 | -50.58563 | 2025-09-13 04:08:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 48.9 |
| 79dae7e5-535a-3b25-a027-7926003c1ac6 | -14.28961 | -46.07693 | 2025-09-13 04:08:00 | NOAA-20 | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 7.2 |
| b2b98b67-b93f-3099-8526-c0c23a22d606 | -11.79756 | -50.54919 | 2025-09-13 04:08:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 11.6 |
| 6c06dc2a-784e-3f7e-937d-6fd8d5662be5 | -12.91462 | -54.76989 | 2025-09-13 04:08:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 50c174e9-5f39-3d72-a5fc-4ca796d33cbd | -9.23615 | -51.24376 | 2025-09-13 04:08:00 | NOAA-20 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 46a82bc7-6710-3e77-b134-46e7d5723c42 | -12.12154 | -47.5969 | 2025-09-13 04:08:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 9682b1f2-97d7-3fc0-953a-aacc8ca631de | -13.45482 | -51.77782 | 2025-09-13 04:08:00 | NOAA-20 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 4879dd57-749d-3b85-bec3-de7f12ca3893 | -9.23495 | -51.25034 | 2025-09-13 04:08:00 | NOAA-20 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 4308e889-4826-32e1-8749-af0a045825a8 | -11.83679 | -50.57901 | 2025-09-13 04:08:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| afeba16b-71e0-3d2d-a7e2-446ebb053851 | -9.02245 | -47.07576 | 2025-09-13 04:08:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 265aa623-cef6-3441-a059-07c3ff39d04c | -12.99129 | -46.73822 | 2025-09-13 04:08:00 | NOAA-20 | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 2ac51931-b2bb-3378-8f38-87409f97245a | -11.73357 | -46.61315 | 2025-09-13 04:08:00 | NOAA-20 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 69f70bab-69ba-35a5-9440-49c939a19973 | -9.75155 | -45.3895 | 2025-09-13 04:08:00 | NOAA-20 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| e609c569-a092-38ea-bb81-327f17f913a6 | -14.1805 | -46.2471 | 2025-09-13 04:08:00 | NOAA-20 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 3fddd064-eebc-3df5-8cad-ba1f4190a6da | -13.89542 | -48.25618 | 2025-09-13 04:08:00 | NOAA-20 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 44ca3f83-fcc8-3ee8-b3e6-31c658c1e5f4 | -11.36576 | -43.50224 | 2025-09-13 04:08:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 5c186c3c-f67e-3a08-a5ca-5cf7dca2bc8d | -10.78269 | -50.54009 | 2025-09-13 04:08:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 25.8 |
| ea752900-7cb3-38e7-ac40-64ea334ea0ea | -10.78155 | -50.53354 | 2025-09-13 04:08:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| f904b009-f235-3850-8bb7-59c2db73991d | -14.29301 | -46.05659 | 2025-09-13 04:08:00 | NOAA-20 | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 61bcd7fa-9b61-3ef6-b9df-0340b4bc4057 | -8.09747 | -50.18844 | 2025-09-13 04:08:00 | NOAA-20 | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 7.4 |
| 02b26e55-e40d-3d2a-9d43-bf0042bb716b | -12.69681 | -43.46598 | 2025-09-13 04:08:00 | NOAA-20 | SÍTIO DO MATO | BAHIA | Brasil | 2930758 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 7b2c03a5-bc2b-3a01-a623-71a214237659 | -11.42355 | -45.60915 | 2025-09-13 04:08:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 2ba54934-1ead-3c4f-8f57-bc2b11d7e948 | -14.17335 | -46.26732 | 2025-09-13 04:08:00 | NOAA-20 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| e498c772-16ff-34c1-8ab4-96589410b8ba | -11.81654 | -46.73941 | 2025-09-13 04:08:00 | NOAA-20 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 8d6fe8d2-9131-3344-b78f-7d12140de24c | -12.06354 | -50.94624 | 2025-09-13 04:08:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 47203022-94c4-3ae7-a2f8-75f760e06200 | -10.23768 | -48.63997 | 2025-09-13 04:08:00 | NOAA-20 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 386a7603-34bb-3282-ad14-cb05ae9605ae | -14.19547 | -46.26665 | 2025-09-13 04:08:00 | NOAA-20 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 14276502-3978-3de7-903e-9d2319987276 | -9.17084 | -40.57017 | 2025-09-13 04:08:00 | NOAA-20 | PETROLINA | PERNAMBUCO | Brasil | 2611101 | 26 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 95ba9856-f0e8-3dd4-9a48-465d90d39a84 | -11.19989 | -48.4288 | 2025-09-13 04:08:00 | NOAA-20 | IPUEIRAS | TOCANTINS | Brasil | 1709807 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 34193ccb-f422-3e90-9382-dc5e1d298f13 | -13.89661 | -48.24946 | 2025-09-13 04:08:00 | NOAA-20 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 3a2db743-03f4-37a7-95ad-f6334d5bd9a9 | -13.2881 | -43.78267 | 2025-09-13 04:08:00 | NOAA-20 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 7a1a2f97-714b-37ff-af5e-4f52ec45ba94 | -9.25115 | -51.24645 | 2025-09-13 04:08:00 | NOAA-20 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 683f5377-7fad-3510-85a8-93138dbbd004 | -14.2231 | -46.27664 | 2025-09-13 04:08:00 | NOAA-20 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 31c222bb-a681-3301-823c-c064730b6eb1 | -13.91501 | -48.28529 | 2025-09-13 04:08:00 | NOAA-20 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| b41562a8-814f-36a7-8cda-6d6e106c8894 | -11.10754 | -51.41796 | 2025-09-13 04:08:00 | NOAA-20 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 9297c2a1-7023-3871-b933-f285caf3f8eb | -14.21878 | -46.25888 | 2025-09-13 04:08:00 | NOAA-20 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 5a114264-5d6c-3dca-a485-614c3c2f5b97 | -14.18548 | -46.23944 | 2025-09-13 04:08:00 | NOAA-20 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 9a0c262c-8538-3486-8cc0-e32a0df89edb | -12.09835 | -44.88002 | 2025-09-13 04:08:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| b3e8c53d-c7b5-322a-a2fa-af2d0eda54a7 | -14.25958 | -45.05017 | 2025-09-13 04:08:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 8ac3fa87-1772-3a9f-ad60-0aff8d80fa79 | -11.57098 | -50.57354 | 2025-09-13 04:08:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 7.7 |
| f2d6c6b7-2471-35a0-a886-3adc04953ad5 | -14.61795 | -46.36393 | 2025-09-13 04:08:00 | NOAA-20 | SÍTIO D'ABADIA | GOIÁS | Brasil | 5220702 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 586af061-cfbc-307f-9fa2-93047a73a9a5 | -10.65335 | -46.29168 | 2025-09-13 04:08:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| f9fa8348-3bb9-3288-a5d5-d8dec07b8484 | -13.2842 | -43.78568 | 2025-09-13 04:08:00 | NOAA-20 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 5aabb6d3-c0fa-389a-b9e9-b1707ff3ec0a | -14.19688 | -46.2584 | 2025-09-13 04:08:00 | NOAA-20 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 5.5 |
| b0f74f60-d5c9-3d48-a270-8224af7fbdbb | -15.09712 | -41.57123 | 2025-09-13 04:08:00 | NOAA-20 | TREMEDAL | BAHIA | Brasil | 2931806 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.4 |
| 73831dad-7fbf-38fd-a665-b250608bf452 | -10.77821 | -44.77734 | 2025-09-13 04:08:00 | NOAA-20 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| ed3d5df1-1973-3217-9dfc-aa8a5383d73c | -10.32865 | -48.81752 | 2025-09-13 04:08:00 | NOAA-20 | PARAÍSO DO TOCANTINS | TOCANTINS | Brasil | 1716109 | 17 | 33 | nan | nan | nan | Cerrado | 9.3 |
| 51cbc092-9781-38ae-b49a-1e42ffebb5cb | -9.91238 | -51.61962 | 2025-09-13 04:08:00 | NOAA-20 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| d925d4e0-72a5-3a96-a85c-1b590f770c6b | -8.05672 | -44.53125 | 2025-09-13 04:08:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 8b9f138a-8a6a-3af4-91c1-49518dc61144 | -11.21726 | -54.98956 | 2025-09-13 04:08:00 | NOAA-20 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 72d6e5bf-f197-3abb-91b7-9d09ee4fc68a | -12.85065 | -47.94327 | 2025-09-13 04:08:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 9ff3efb0-2920-3f30-b8ca-abc590e1aa01 | -11.11318 | -50.70098 | 2025-09-13 04:08:00 | NOAA-20 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 8231fb37-bfa4-37f1-bd55-a46db97377c0 | -15.53808 | -42.57285 | 2025-09-13 04:08:00 | NOAA-20 | RIO PARDO DE MINAS | MINAS GERAIS | Brasil | 3155603 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 36ffb4d8-f2d2-3536-a94a-a34eaf320960 | -14.27911 | -45.10335 | 2025-09-13 04:08:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| cc16baa2-edb2-3f98-aa17-656a6f4eb7db | -8.42413 | -47.24862 | 2025-09-13 04:08:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| e7224cde-0d5c-3932-913d-cf58bd7b62e2 | -9.23569 | -51.21637 | 2025-09-13 04:08:00 | NOAA-20 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 91f98bf3-0828-3363-9569-406b5662a807 | -11.42507 | -43.53756 | 2025-09-13 04:08:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 2473956d-75e8-3fe3-ab37-a229a02c9676 | -12.80466 | -47.99393 | 2025-09-13 04:08:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 5.3 |
| ce98a798-18f1-39b3-9557-2ae6cae2b195 | -14.21814 | -46.28423 | 2025-09-13 04:08:00 | NOAA-20 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 23d1e8e7-3383-3581-ac59-6de11d7a637a | -10.69647 | -54.44502 | 2025-09-13 04:08:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| eaf44489-8d67-394c-b850-88a35e5c71cf | -10.50256 | -51.52778 | 2025-09-13 04:08:00 | NOAA-20 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 28ab6702-2b80-3b3f-914b-66a4fc0c716d | -11.74149 | -44.20803 | 2025-09-13 04:08:00 | NOAA-20 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 0fe28ab7-53f0-3540-b03f-6f194414a57e | -9.06192 | -47.03787 | 2025-09-13 04:08:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 9.9 |
| f4bb7cb9-23af-3ccd-8394-60f13b300056 | -14.28892 | -46.08103 | 2025-09-13 04:08:00 | NOAA-20 | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 7.2 |
| 3a449e7f-ce35-3bbb-a60a-ef69db7e0e77 | -14.43699 | -48.44061 | 2025-09-13 04:08:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| c9dd3fea-fad3-3d0b-9426-7d7814ab26bc | -8.47588 | -47.26096 | 2025-09-13 04:08:00 | NOAA-20 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 8.3 |
| 1d6af852-fb44-3617-a4bf-2f581ee1fcd6 | -14.70345 | -45.14808 | 2025-09-13 04:08:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 6.9 |
| b98443ae-de00-369d-98ef-956110b4b38c | -14.20247 | -46.24712 | 2025-09-13 04:08:00 | NOAA-20 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 3.8 |
| eaa5cba2-bf2b-34a0-a3d5-a46c5dfc0412 | -12.08208 | -44.89309 | 2025-09-13 04:08:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 8ad5b533-da8e-344b-81e0-c47d186668cd | -11.45327 | -43.57511 | 2025-09-13 04:08:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| dfb55477-a491-332b-8593-466d7e692df4 | -7.94722 | -46.90702 | 2025-09-13 04:08:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 2851bd6c-b612-36de-9c77-1e5bc9599d74 | -11.93431 | -44.29586 | 2025-09-13 04:08:00 | NOAA-20 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 1cc91e22-7850-30e1-9705-fe178d2d3384 | -12.76568 | -47.16047 | 2025-09-13 04:08:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 99889b0e-37bd-38d8-ac39-5cd6e05f6516 | -9.8664 | -46.47136 | 2025-09-13 04:08:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 4fda8289-ab2d-3442-80d1-b4e551e43015 | -11.43554 | -43.55755 | 2025-09-13 04:08:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| adc973b5-cbf3-3ca1-8346-587134215750 | -14.19323 | -46.2369 | 2025-09-13 04:08:00 | NOAA-20 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 6b001939-4da0-3c9a-8e55-24a26f83e361 | -9.5236 | -54.62792 | 2025-09-13 04:08:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 70.8 |
| ab1d421b-bb3b-3b2d-bfc6-a89e8408e401 | -11.33435 | -50.78659 | 2025-09-13 04:08:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 3.7 |
| a971e817-7d08-3368-9064-57ceb5fd5bb7 | -12.10972 | -47.59483 | 2025-09-13 04:08:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 8ef76605-2d76-3a0f-89db-e5ca545007ab | -11.7206 | -46.57715 | 2025-09-13 04:08:00 | NOAA-20 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| cf413983-e73f-365f-bb7b-1612375a14ea | -11.82634 | -50.55482 | 2025-09-13 04:08:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 21.9 |
| 5e299318-49be-3e1e-9372-cff93698f43c | -10.77128 | -44.77619 | 2025-09-13 04:08:00 | NOAA-20 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| a6444fc1-59a3-3120-a425-4a45cdb3f7b0 | -15.2341 | -44.06357 | 2025-09-13 04:08:00 | NOAA-20 | ITACARAMBI | MINAS GERAIS | Brasil | 3132107 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| c04e8fd6-abb1-3bdc-b068-30edcf8283ff | -14.00115 | -44.7688 | 2025-09-13 04:08:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 10188136-67ab-3238-8c5a-15fadc045587 | -11.71544 | -46.56266 | 2025-09-13 04:08:00 | NOAA-20 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 6eec6c2c-f4b5-384d-add5-1930e731293b | -8.09312 | -50.18387 | 2025-09-13 04:08:00 | NOAA-20 | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 7.4 |
| bc1cea10-b8f2-3581-8041-e1e17b2de582 | -12.10184 | -47.59348 | 2025-09-13 04:08:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| c0f866b1-0181-3f23-83bf-d15950a944b5 | -9.05056 | -47.03239 | 2025-09-13 04:08:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 84ffa32a-eb02-322c-8f83-a171d37de89a | -8.06793 | -44.52901 | 2025-09-13 04:08:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 52dac96b-a905-3fea-8734-5113a1cf12f5 | -11.8608 | -50.58372 | 2025-09-13 04:08:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 10.3 |
| e9c45036-f9e4-3514-8424-faa654a7f0f1 | -14.12931 | -45.37107 | 2025-09-13 04:08:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 061df1f4-572b-3eb7-865d-c90db32ebe5b | -9.02491 | -47.06167 | 2025-09-13 04:08:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| fce3542f-c8b1-3baa-89b2-a5a17390a700 | -10.75144 | -50.50486 | 2025-09-13 04:08:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 34.9 |
| 0e62a07b-4865-3f3e-ad01-6a5e5f76126a | -14.14264 | -45.39714 | 2025-09-13 04:08:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 2ca2a17f-4457-3a2d-9cd3-3fa57e9c71a9 | -11.4222 | -45.61721 | 2025-09-13 04:08:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 13.1 |
| 0c42d487-7a10-38f3-a4cf-e85fed227457 | -9.52889 | -54.63519 | 2025-09-13 04:08:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 70.8 |


[Clique aqui para ver as próximas entradas](README55.md)
