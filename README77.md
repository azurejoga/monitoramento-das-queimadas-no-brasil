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

## Dados Diários - Página 77

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| e1e537b4-121a-3069-8add-c64173777b0b | -11.83884 | -45.01744 | 2025-10-02 04:29:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| a8f82483-48b7-3872-a71e-681ed025f737 | -11.79455 | -44.99998 | 2025-10-02 04:29:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| cd8d4655-450c-3d54-911c-d77fadc0c6b2 | -7.15641 | -44.99402 | 2025-10-02 04:29:00 | NPP-375D | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 220bfaaf-8de1-3f7c-84ce-bd970a75de9f | -10.22094 | -48.2263 | 2025-10-02 04:29:00 | NPP-375D | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| dad67522-a7a7-35d4-85c5-81b450dd5b97 | -7.55765 | -42.40308 | 2025-10-02 04:29:00 | NPP-375D | SÃO MIGUEL DO FIDALGO | PIAUÍ | Brasil | 2210391 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 743e12da-34a0-3a1d-8c39-d6d1a741f1eb | -11.8165 | -45.02251 | 2025-10-02 04:29:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| b2c0f74d-58da-3930-96ad-270a6e5d6c67 | -6.74382 | -46.33205 | 2025-10-02 04:29:00 | NPP-375D | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 9adf7075-f37f-30a6-81a0-3d4ee5a648c1 | -6.53689 | -46.52353 | 2025-10-02 04:29:00 | NPP-375D | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 8711beb5-5781-3b9b-9a79-a9bac5c2853a | -9.94802 | -43.69417 | 2025-10-02 04:29:00 | NPP-375D | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 7157ce5f-8d19-3d39-aceb-0401a52c437a | -11.80223 | -44.97283 | 2025-10-02 04:29:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| d793359f-da4b-3951-bea7-79d80bafa608 | -6.30307 | -45.92769 | 2025-10-02 04:29:00 | NPP-375D | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| efe8ecf5-210a-336a-a802-bfe4aa0f7bba | -8.38366 | -47.99211 | 2025-10-02 04:29:00 | NPP-375D | ITAPIRATINS | TOCANTINS | Brasil | 1710904 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 966d98f5-d07f-380f-9754-6ce6adc76c8a | -6.72178 | -44.62436 | 2025-10-02 04:29:00 | NPP-375D | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| c3d3bff4-818d-3e87-a25e-dd451a46c6a4 | -9.92554 | -50.49609 | 2025-10-02 04:29:00 | NPP-375D | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 5.3 |
| e09ece44-1676-3b09-8b5c-5cdb569b5efe | -7.76943 | -42.54656 | 2025-10-02 04:29:00 | NPP-375D | SOCORRO DO PIAUÍ | PIAUÍ | Brasil | 2210904 | 22 | 33 | nan | nan | nan | Caatinga | 22.9 |
| 62fb3839-5da9-304a-92d8-b49f60b508e0 | -5.96569 | -45.7112 | 2025-10-02 04:29:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 0d0f6dcb-9601-3d49-b35c-c50865a43058 | -9.92993 | -43.73986 | 2025-10-02 04:29:00 | NPP-375D | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 64.5 |
| 3bd4a1f1-9e25-36dd-b83a-45dac41cfcef | -8.68601 | -47.69335 | 2025-10-02 04:29:00 | NPP-375D | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| d36d514d-9c53-3bf7-920c-c415f722f28e | -11.1735 | -47.27464 | 2025-10-02 04:29:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 7.7 |
| 2d2eaf16-f153-3b73-9f29-1ccacc423a86 | -6.7845 | -45.59479 | 2025-10-02 04:29:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| f873ed21-1eb6-3bb3-86f4-f1b14ab2031b | -11.25945 | -47.80491 | 2025-10-02 04:29:00 | NPP-375D | SANTA ROSA DO TOCANTINS | TOCANTINS | Brasil | 1718907 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| c1344e62-8dd5-3fb6-adae-ea42587dd041 | -11.00822 | -46.58549 | 2025-10-02 04:29:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| d71c087b-2a78-3eda-a173-e971850bc68d | -10.84664 | -45.39136 | 2025-10-02 04:29:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 7.7 |
| 4da2b0ae-f33d-39c3-ada4-7237ac194afa | -6.12892 | -45.89711 | 2025-10-02 04:29:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 751c8503-57a8-31f3-a5db-1575bf4b0244 | -7.04207 | -43.34569 | 2025-10-02 04:29:00 | NPP-375D | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Caatinga | 2.7 |
| 97928758-043a-3808-af3f-d30491feabda | -8.94449 | -48.7167 | 2025-10-02 04:29:00 | NPP-375D | COLMÉIA | TOCANTINS | Brasil | 1716703 | 17 | 33 | nan | nan | nan | Amazônia | 0.8 |
| b914c7d1-98c1-3256-b6f5-c383855dedfc | -11.70322 | -45.34656 | 2025-10-02 04:29:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 08237e73-e380-3cb6-a3dc-8f028b6d477d | -11.15298 | -47.19587 | 2025-10-02 04:29:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 0b6fef91-9a9d-3d8a-b475-c59dbbd1730b | -9.93506 | -43.70549 | 2025-10-02 04:29:00 | NPP-375D | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 0cec530f-8fc2-35e0-9531-e16589d4f82a | -11.45784 | -44.96727 | 2025-10-02 04:29:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| c5b25ccf-abe0-30d4-b457-c2a469ab531c | -6.27141 | -44.05877 | 2025-10-02 04:29:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 5bb67308-2c08-3672-83ce-1e02e82b2890 | -12.11787 | -43.43347 | 2025-10-02 04:29:00 | NPP-375D | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| cbdd452c-2411-3988-8f38-a8ff0160781a | -8.8995 | -45.03859 | 2025-10-02 04:29:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 608b1bd5-7372-3a4a-88eb-84a5b94f1013 | -8.87155 | -46.58725 | 2025-10-02 04:29:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| f24641fa-e504-3e2b-b12a-5cd9963f7c0b | -11.13566 | -43.3894 | 2025-10-02 04:29:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 053b63fe-14be-3712-aad4-d0c62d83c4d0 | -11.81564 | -45.0274 | 2025-10-02 04:29:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 8decdf49-c9dd-35ac-95a6-82d802339dda | -9.40537 | -47.54814 | 2025-10-02 04:29:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| c7737e4d-3e31-318e-b082-3240bee02456 | -10.84733 | -46.59296 | 2025-10-02 04:29:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| a43f506d-1019-34f1-8e52-9e480f3ec81f | -12.22123 | -43.75573 | 2025-10-02 04:29:00 | NPP-375D | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 2e9a38a3-7385-3af0-a313-c68a1cd7e970 | -10.10949 | -45.70071 | 2025-10-02 04:29:00 | NPP-375D | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 13676048-4b7e-350c-81de-07164c666913 | -11.43934 | -43.89056 | 2025-10-02 04:29:00 | NPP-375D | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 2d28f031-7b08-3df7-a33d-ece2f6faf94a | -11.4712 | -44.998 | 2025-10-02 04:29:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 8c68aef6-4280-3f6d-8d8e-86d7f60f6dae | -9.92865 | -43.74844 | 2025-10-02 04:29:00 | NPP-375D | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 6.9 |
| f2705b17-6e9a-3e71-bd70-91368cd5903c | -11.45493 | -44.96269 | 2025-10-02 04:29:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 2af3a75c-2692-3c2f-80ed-3ab5bc8f8482 | -11.26577 | -47.65752 | 2025-10-02 04:29:00 | NPP-375D | PINDORAMA DO TOCANTINS | TOCANTINS | Brasil | 1717008 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| f47f4526-175d-3b8d-b973-a433f2d2362a | -8.85219 | -46.62357 | 2025-10-02 04:29:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 0dfaaef6-6013-3eb6-bca4-f386bc98b9ba | -7.55473 | -42.64781 | 2025-10-02 04:29:00 | NPP-375D | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 577551da-b0d2-3a18-bb51-bdd7db5970ff | -10.24637 | -50.31917 | 2025-10-02 04:29:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 13f738c4-503a-3203-993d-b63caa2edb14 | -10.28843 | -44.3246 | 2025-10-02 04:29:00 | NPP-375D | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| c958486b-2fb8-3606-8e2c-9aaefaa04f8f | -8.40815 | -47.75396 | 2025-10-02 04:29:00 | NPP-375D | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 9d13804d-27f6-342e-8bb1-f4a3ea0394bf | -11.26334 | -47.80191 | 2025-10-02 04:29:00 | NPP-375D | SANTA ROSA DO TOCANTINS | TOCANTINS | Brasil | 1718907 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| b4f10ecc-0b6e-3b9c-88b0-615fd806c3cf | -9.94609 | -43.7071 | 2025-10-02 04:29:00 | NPP-375D | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 745ff5a9-4e78-3610-a7b1-0e35327814a8 | -11.09695 | -47.82204 | 2025-10-02 04:29:00 | NPP-375D | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 55cd0b00-f8d0-371d-9d30-08a45dc6aa66 | -11.46195 | -44.96387 | 2025-10-02 04:29:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 22a8ac05-c284-3550-918d-4f683b69de1f | -9.56434 | -50.94263 | 2025-10-02 04:29:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 2d413e7a-ee5e-3989-aa8a-84ff2549eacd | -11.43999 | -43.88613 | 2025-10-02 04:29:00 | NPP-375D | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| ba9dfaf6-6f95-3bfc-8412-2fc4d0d935af | -10.85122 | -46.58994 | 2025-10-02 04:29:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 32d38a1c-660c-3e4d-af1a-3b93292d1189 | -9.39974 | -47.58336 | 2025-10-02 04:29:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 7.3 |
| c88a6aa0-6c9d-3c2d-ad03-4779e2ab8787 | -9.94136 | -43.76363 | 2025-10-02 04:29:00 | NPP-375D | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 5.6 |
| f28f9116-d240-37fa-9c96-e5b82438dd39 | -11.49623 | -43.50558 | 2025-10-02 04:29:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| bc555900-cc64-3348-8597-63d98385d185 | -10.82637 | -47.96687 | 2025-10-02 04:29:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| cb120501-80ed-36b9-8360-422dcfe63e5e | -8.90142 | -46.06963 | 2025-10-02 04:29:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| f5de5ef1-4489-39dc-95a4-31cf24666e8d | -11.1796 | -47.25759 | 2025-10-02 04:29:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 8e6e66f9-98c4-316c-aeca-4ef7693d414f | -12.2208 | -43.75792 | 2025-10-02 04:29:00 | NPP-375D | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 39f78153-8486-3f51-9dd7-7da5e0ab3779 | -10.342 | -43.74197 | 2025-10-02 04:29:00 | NPP-375D | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 8ef5cf0f-c9b1-3acb-83bd-9b0a37759e04 | -11.05994 | -47.80541 | 2025-10-02 04:29:00 | NPP-375D | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| ec22eeec-abd9-3541-bce0-9d5c6cd80190 | -8.81793 | -44.80343 | 2025-10-02 04:29:00 | NPP-375D | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| a752038d-9651-3146-9bbb-277d53133ac5 | -10.70916 | -48.57963 | 2025-10-02 04:29:00 | NPP-375D | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| cd9d9da6-5c8f-3bdd-9ccc-a2c022ee4ed8 | -11.27442 | -47.81821 | 2025-10-02 04:29:00 | NPP-375D | SANTA ROSA DO TOCANTINS | TOCANTINS | Brasil | 1718907 | 17 | 33 | nan | nan | nan | Cerrado | 4.5 |
| f92906a8-a440-3247-9fd1-12eee467c841 | -10.11005 | -45.69705 | 2025-10-02 04:29:00 | NPP-375D | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 62b0f11f-5216-34d5-ac73-78bb6348286d | -11.35999 | -44.96983 | 2025-10-02 04:29:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 667e4bed-7b33-3f19-98e3-297d802c6eb3 | -11.00989 | -46.57481 | 2025-10-02 04:29:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| b80edfd0-063e-3424-9afe-7f99e32904d2 | -7.78776 | -42.50119 | 2025-10-02 04:29:00 | NPP-375D | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| b26efe3d-3622-3465-a677-eb884f573f9d | -7.79159 | -42.50177 | 2025-10-02 04:29:00 | NPP-375D | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 3.6 |
| 81c17f71-2cf8-3243-a92c-9cc758a36000 | -11.86876 | -45.01011 | 2025-10-02 04:29:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 3.6 |
| b62ac93d-9842-3730-a2fe-c9131754c15b | -9.92578 | -43.71734 | 2025-10-02 04:29:00 | NPP-375D | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 3950aa2b-516a-309b-8a74-d440418d5255 | -9.91108 | -47.70635 | 2025-10-02 04:29:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 68873e71-eb36-3c8f-8c73-a61322e676c6 | -9.93726 | -43.74099 | 2025-10-02 04:29:00 | NPP-375D | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 10.7 |
| c35077fe-d7a5-3483-a789-06543a2fcf12 | -10.19787 | -50.27374 | 2025-10-02 04:29:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| a2f4a626-bed5-3213-9430-49c273ce4b5d | -11.07532 | -47.80763 | 2025-10-02 04:29:00 | NPP-375D | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| b3359419-2f3a-3dd2-b174-b333bd2b2507 | -11.7045 | -44.30654 | 2025-10-02 04:29:00 | NPP-375D | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 33bbf5be-3e0a-3981-bcc8-5b79b6d9f681 | -11.09086 | -47.81742 | 2025-10-02 04:29:00 | NPP-375D | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| c54a4c47-9a3b-39c8-acb4-f4cd6aa0764f | -9.07248 | -46.72313 | 2025-10-02 04:29:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 8f58a050-2430-3aba-bdc5-85d940c82c7a | -6.95908 | -45.3213 | 2025-10-02 04:29:00 | NPP-375D | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| c4bd7648-811c-3d36-9777-7a6de39215bb | -11.46354 | -45.02504 | 2025-10-02 04:29:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 680cb5a7-4cb8-31d1-9e97-aade36eb60ce | -12.76057 | -39.73586 | 2025-10-02 04:29:00 | NPP-375D | ITATIM | BAHIA | Brasil | 2916856 | 29 | 33 | nan | nan | nan | Caatinga | 3.5 |
| 08100d36-1480-3f8f-81ec-f53409a976bf | -6.73146 | -44.60698 | 2025-10-02 04:29:00 | NPP-375D | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| d5932cd5-0032-3322-8dcc-8b9e2002896d | -11.81299 | -45.02187 | 2025-10-02 04:29:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 865002c9-f049-3c3d-8e70-59a4951d7151 | -8.87656 | -46.59139 | 2025-10-02 04:29:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 204dbe36-8d14-3d1f-8bc5-05ec8ff9d458 | -11.1042 | -51.07679 | 2025-10-02 04:29:00 | NPP-375D | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 22a0221a-15f1-3ce8-bc1c-3cc799982a96 | -11.46294 | -45.02901 | 2025-10-02 04:29:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 3.9 |
| c0aae93b-5db6-3ae5-979d-9ab3ea9951dc | -10.85008 | -45.39189 | 2025-10-02 04:29:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 1364a902-2e9a-3ae2-8638-faca97670649 | -11.47236 | -45.01418 | 2025-10-02 04:29:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| ad7381ce-0249-31d8-a581-d413ffcb0a05 | -9.32521 | -45.67431 | 2025-10-02 04:29:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 3.3 |
| dca60b7f-52c4-3eb1-ad37-2614beaee40a | -6.27896 | -44.05597 | 2025-10-02 04:29:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| a5b4754f-f444-352e-8771-64335b77f39d | -7.30329 | -42.89101 | 2025-10-02 04:29:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 8de0f67b-7569-33aa-b9fb-7d943cc52e8e | -11.28195 | -47.82703 | 2025-10-02 04:29:00 | NPP-375D | SANTA ROSA DO TOCANTINS | TOCANTINS | Brasil | 1718907 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 3df935f3-b875-3e3e-bc22-36027b271ceb | -8.74547 | -47.34127 | 2025-10-02 04:29:00 | NPP-375D | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 7b815407-1385-36c5-99bd-67adb43fe298 | -9.33308 | -45.92183 | 2025-10-02 04:29:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 93c1492a-95ab-326f-b106-89dce9c7b3d8 | -11.66794 | -45.321 | 2025-10-02 04:29:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |


[Clique aqui para ver as próximas entradas](README78.md)
