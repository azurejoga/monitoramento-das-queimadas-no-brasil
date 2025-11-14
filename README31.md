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

## Dados Diários - Página 31

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 02bedb96-7779-3640-84d5-2a41af7de8fd | -6.57255 | -47.9012 | 2025-11-14 04:25:00 | NPP-375D | DARCINÓPOLIS | TOCANTINS | Brasil | 1706506 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 860f9338-edf3-390c-856e-88a1845398a6 | -7.0997 | -41.82661 | 2025-11-14 04:25:00 | NPP-375D | SANTA CRUZ DO PIAUÍ | PIAUÍ | Brasil | 2209104 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| fb4bab38-b057-32a0-8d9b-7c494b2233f1 | -12.01244 | -46.76692 | 2025-11-14 04:25:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 250f77a3-19b3-3001-b0aa-fab6a95a161d | -5.78896 | -43.73549 | 2025-11-14 04:25:00 | NPP-375D | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| a5ce8b98-4d5b-3ce8-af96-5a5a894b7374 | -12.45134 | -44.63625 | 2025-11-14 04:25:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| fdf34fcb-fd54-3a39-805c-02d716b16fcc | -4.75168 | -46.39285 | 2025-11-14 04:25:00 | NPP-375D | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| bb4ebf80-efc9-3300-b50d-7e43400f57f2 | -7.2643 | -40.17394 | 2025-11-14 04:25:00 | NPP-375D | ARARIPE | CEARÁ | Brasil | 2301307 | 23 | 33 | nan | nan | nan | Caatinga | 0.9 |
| d8e2500c-f4ad-39c0-a873-e223d663b535 | -5.34902 | -46.76238 | 2025-11-14 04:25:00 | NPP-375D | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| c87da8c8-c24b-31d3-879d-92df351b7d5a | -6.7396 | -46.06617 | 2025-11-14 04:25:00 | NPP-375D | FORTALEZA DOS NOGUEIRAS | MARANHÃO | Brasil | 2104107 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 783b0dbd-f5f3-3c10-a90b-e583b22d5498 | -4.59914 | -46.53653 | 2025-11-14 04:25:00 | NPP-375D | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 0500b0f8-b63a-3fc1-9353-c0da3cd85f47 | -4.95966 | -47.71956 | 2025-11-14 04:25:00 | NPP-375D | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 244c74bf-bdc3-3f67-8be3-2052c730b48b | -5.41628 | -43.26173 | 2025-11-14 04:25:00 | NPP-375D | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| d99e1792-ce98-39b3-ac59-ffc075664b01 | -6.61179 | -47.63737 | 2025-11-14 04:25:00 | NPP-375D | PALMEIRAS DO TOCANTINS | TOCANTINS | Brasil | 1713809 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 7cf14b4d-6c18-32eb-9616-353b2ce1ebe4 | -6.14808 | -48.04984 | 2025-11-14 04:25:00 | NPP-375D | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 65af66fc-1258-3baa-a8e8-4f8e0940dd59 | -6.07592 | -41.6329 | 2025-11-14 04:25:00 | NPP-375D | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 215d097b-81bd-375a-a6e3-8c80253928c5 | -12.45327 | -43.75818 | 2025-11-14 04:25:00 | NPP-375D | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 23e759e4-bb3d-3751-88fc-164b8538131b | -5.85851 | -47.58492 | 2025-11-14 04:25:00 | NPP-375D | ITAGUATINS | TOCANTINS | Brasil | 1710706 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 77505d72-3f3c-3769-accb-7c730876ec62 | -4.76727 | -44.78669 | 2025-11-14 04:25:00 | NPP-375D | POÇÃO DE PEDRAS | MARANHÃO | Brasil | 2108900 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| cebdacd3-e705-309d-a344-80d162d72f76 | -6.44842 | -45.66297 | 2025-11-14 04:25:00 | NPP-375D | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| e64e7a12-e760-3c71-aa62-a8120434b496 | -18.70896 | -43.00552 | 2025-11-14 04:25:00 | NPP-375D | SABINÓPOLIS | MINAS GERAIS | Brasil | 3156809 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 2e7b3a98-4128-3001-a429-cb09ee06116b | -4.96403 | -47.71581 | 2025-11-14 04:25:00 | NPP-375D | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 2.4 |
| d1ca0bc3-f361-33e7-bb99-f7f051c3f87c | -5.652 | -46.59084 | 2025-11-14 04:25:00 | NPP-375D | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 83389c66-4efc-32c8-a7ee-c3b6f1dd9d36 | -6.09881 | -41.6029 | 2025-11-14 04:25:00 | NPP-375D | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| d65ba661-0c64-30cc-8ff9-1762a87a49b0 | -12.59693 | -48.33547 | 2025-11-14 04:25:00 | NPP-375D | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| f40fe1dc-1015-3064-aa8d-7a27107772ad | -12.00185 | -46.76881 | 2025-11-14 04:25:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| df5b3249-cc75-38c8-bd99-4f005ae693f6 | -3.43852 | -52.88932 | 2025-11-14 04:25:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 506a7ea2-f010-3d93-a83c-c0093baf4961 | -4.64025 | -48.74663 | 2025-11-14 04:25:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| fdaf2ea9-543f-3395-bbde-448870d397c3 | -5.7519 | -49.26117 | 2025-11-14 04:25:00 | NPP-375D | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| b98282ae-5aa5-3bc6-943d-41695e8e72a8 | -11.73543 | -48.53437 | 2025-11-14 04:25:00 | NPP-375D | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| d2ba4792-3431-3a9b-b8a2-1dae37ccedc0 | -6.10667 | -42.68124 | 2025-11-14 04:25:00 | NPP-375D | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 0.5 |
| 56759718-d04a-3f5d-a828-5ff0c83f83a9 | -12.49328 | -47.29331 | 2025-11-14 04:25:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| db776624-a6c5-3792-9214-3a22940f2715 | -12.598 | -48.3715 | 2025-11-14 04:25:00 | NPP-375D | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 9c753a92-75b2-3ac1-b38a-244f90056398 | -7.173 | -38.45606 | 2025-11-14 04:25:00 | NPP-375D | SÃO JOSÉ DE PIRANHAS | PARAÍBA | Brasil | 2514503 | 25 | 33 | nan | nan | nan | Caatinga | 2.1 |
| ad1f4464-0edc-3732-bf2a-6887c0447156 | -13.68854 | -43.00566 | 2025-11-14 04:25:00 | NPP-375D | RIACHO DE SANTANA | BAHIA | Brasil | 2926400 | 29 | 33 | nan | nan | nan | Caatinga | 2.0 |
| e5976cbd-cf91-3a8f-b12d-33d9758de7e8 | -6.06871 | -41.55272 | 2025-11-14 04:25:00 | NPP-375D | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 6368b071-9995-3471-8885-350aabe34364 | -12.21146 | -44.94846 | 2025-11-14 04:25:00 | NPP-375D | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| b7823e52-5723-3123-a69d-c5dcba7ac13f | -5.53122 | -43.68093 | 2025-11-14 04:25:00 | NPP-375D | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 7.7 |
| f1289687-57c3-3583-be0a-aeeebea86694 | -11.85589 | -49.21547 | 2025-11-14 04:25:00 | NPP-375D | CARIRI DO TOCANTINS | TOCANTINS | Brasil | 1703867 | 17 | 33 | nan | nan | nan | Cerrado | 31.8 |
| d958eb6c-16c2-3ba3-b9cb-9ecf1788f0af | -4.71433 | -46.44876 | 2025-11-14 04:25:00 | NPP-375D | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 7b687545-a991-34b2-9658-86c8bac08a82 | -6.8082 | -41.5142 | 2025-11-14 04:25:00 | NPP-375D | SÃO JOSÉ DO PIAUÍ | PIAUÍ | Brasil | 2210201 | 22 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 216d00c4-2acf-30a0-a8f5-a643c1874acf | -5.36514 | -46.28971 | 2025-11-14 04:25:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Amazônia | 12.0 |
| 35bf1c62-58de-3058-b488-83cc0c1e3af6 | -12.13978 | -48.01933 | 2025-11-14 04:25:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 83c8960d-f48f-39b1-bc03-c30b2ae57d4e | -7.06192 | -43.58404 | 2025-11-14 04:25:00 | NPP-375D | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 70d4b74d-cf0f-30f2-ae88-defa133cef5d | -5.18113 | -44.09653 | 2025-11-14 04:25:00 | NPP-375D | GONÇALVES DIAS | MARANHÃO | Brasil | 2104404 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 16b805e5-6756-38a9-8462-d36f34919d74 | -5.45668 | -47.10131 | 2025-11-14 04:25:00 | NPP-375D | BURITIRANA | MARANHÃO | Brasil | 2102358 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 9063c031-3cc2-380c-a5da-dbe99762c3ba | -4.68409 | -45.00891 | 2025-11-14 04:25:00 | NPP-375D | POÇÃO DE PEDRAS | MARANHÃO | Brasil | 2108900 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 6d03b7d0-39d6-3144-91ea-532162bdde28 | -4.6475 | -47.95045 | 2025-11-14 04:25:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 8e19f67d-8a48-3785-ba81-6d43e6873496 | -6.14071 | -48.04878 | 2025-11-14 04:25:00 | NPP-375D | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| ce84c7c0-4a0f-31cf-a9e9-334c92f0272b | -15.85741 | -43.61146 | 2025-11-14 04:25:00 | NPP-375D | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 2cf816a4-e85c-30bb-9f3a-302b0d1c5741 | -4.53081 | -46.39746 | 2025-11-14 04:25:00 | NPP-375D | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |
| b7ae3c05-7c1e-3440-9e89-f78e4ab65689 | -6.16349 | -48.0478 | 2025-11-14 04:25:00 | NPP-375D | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 10.2 |
| c9b85e18-f543-3dec-9bff-764b07628478 | -4.21928 | -49.12303 | 2025-11-14 04:25:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |
| ce6fd955-00ea-300a-b6bb-7c5bdda59881 | -14.6976 | -46.61545 | 2025-11-14 04:25:00 | NPP-375D | ALVORADA DO NORTE | GOIÁS | Brasil | 5200803 | 52 | 33 | nan | nan | nan | Cerrado | 12.2 |
| 36e36529-6caf-37e2-b349-fa7c495d1cf6 | -5.19442 | -48.03865 | 2025-11-14 04:25:00 | NPP-375D | VILA NOVA DOS MARTÍRIOS | MARANHÃO | Brasil | 2112852 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 751167b9-3ba2-3a2c-84b0-a18d4de84cbd | -15.13746 | -42.93407 | 2025-11-14 04:25:00 | NPP-375D | MONTE AZUL | MINAS GERAIS | Brasil | 3142908 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 074d179c-79f7-33fb-9ddc-09af9baa1a14 | -4.8736 | -46.69251 | 2025-11-14 04:25:00 | NPP-375D | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| b98ca939-4de6-3df4-a9e5-23f6ed805dd4 | -5.42897 | -46.0894 | 2025-11-14 04:25:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| ced5c2b7-888e-3cfa-8b1b-94778cdbaafd | -4.84306 | -45.62676 | 2025-11-14 04:25:00 | NPP-375D | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 73864cb3-3e5b-3c0e-ac41-ddb317c1485a | -13.76838 | -43.69118 | 2025-11-14 04:25:00 | NPP-375D | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 24791342-e85b-324b-a631-6e557df7b09d | -5.41964 | -43.26224 | 2025-11-14 04:25:00 | NPP-375D | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 247ba74c-6c2b-30a4-9fea-50aa47ee31af | -3.5296 | -52.7962 | 2025-11-14 04:25:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 68127bfc-2397-34ab-b044-9830f41d37c8 | -4.93243 | -48.55159 | 2025-11-14 04:25:00 | NPP-375D | BOM JESUS DO TOCANTINS | PARÁ | Brasil | 1501576 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 3a43109b-1cd4-3d7f-a6d0-46ce4241d62b | -5.72885 | -42.35175 | 2025-11-14 04:25:00 | NPP-375D | PASSAGEM FRANCA DO PIAUÍ | PIAUÍ | Brasil | 2207751 | 22 | 33 | nan | nan | nan | Caatinga | 7.3 |
| 85acba7b-4fbd-315c-81b4-38222f30d63f | -6.09336 | -41.61471 | 2025-11-14 04:25:00 | NPP-375D | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| fdf3309d-806b-3057-a4eb-206e0ee70525 | -6.18766 | -40.87764 | 2025-11-14 04:25:00 | NPP-375D | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 0.5 |
| a4479595-e8c1-336c-b1bb-f31c4061b00b | -4.42639 | -47.26257 | 2025-11-14 04:25:00 | NPP-375D | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 14ea8524-551a-3953-bbc8-59a3a017325d | -4.99318 | -47.51311 | 2025-11-14 04:25:00 | NPP-375D | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 3d9a1c17-749e-3927-a563-657ff92458e6 | -13.49 | -46.71891 | 2025-11-14 04:25:00 | NPP-375D | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 45b59b5f-154c-32f9-9110-8dbe2a9c2c75 | -5.36454 | -46.29342 | 2025-11-14 04:25:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Amazônia | 10.8 |
| 92025f9e-cbe5-366a-8dea-15761640cf99 | -12.02092 | -43.73116 | 2025-11-14 04:25:00 | NPP-375D | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| b7b08c14-68ef-3181-95d1-2c2817ba7585 | -7.15241 | -41.25601 | 2025-11-14 04:25:00 | NPP-375D | GEMINIANO | PIAUÍ | Brasil | 2204352 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 137d234b-c129-3ca8-b74e-494a9a28c131 | -15.24914 | -47.94714 | 2025-11-14 04:25:00 | NPP-375D | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| e2c03cd5-afbe-3c5f-b54d-18a846216817 | -12.62698 | -44.13919 | 2025-11-14 04:25:00 | NPP-375D | TABOCAS DO BREJO VELHO | BAHIA | Brasil | 2930907 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| dd5ddc9d-75ea-38d6-95a1-e77130dae530 | -5.74635 | -42.72987 | 2025-11-14 04:25:00 | NPP-375D | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| a2892c4c-5006-3940-b57a-1a200d122ba2 | -5.74293 | -42.72935 | 2025-11-14 04:25:00 | NPP-375D | AGRICOLÂNDIA | PIAUÍ | Brasil | 2200103 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| cd7b4ac7-4a9d-339b-8352-f2ec5a55a0d6 | -6.09819 | -41.60701 | 2025-11-14 04:25:00 | NPP-375D | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 2.7 |
| 78cbf2ec-2173-3936-8dc0-7a3830247ca2 | -12.59614 | -48.33242 | 2025-11-14 04:25:00 | NPP-375D | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 727f09f2-1685-31b3-b96e-21eb79338d7e | -10.63377 | -51.76384 | 2025-11-14 04:25:00 | NPP-375D | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| bdf969fd-96f4-333d-ac87-8ecad27542b6 | -17.99076 | -42.9903 | 2025-11-14 04:25:00 | NPP-375D | ITAMARANDIBA | MINAS GERAIS | Brasil | 3132503 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| b5db6e5b-dc1f-3a9b-992c-2037551ea037 | -14.66781 | -46.56657 | 2025-11-14 04:25:00 | NPP-375D | ALVORADA DO NORTE | GOIÁS | Brasil | 5200803 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 2c139237-7633-3cfe-b841-0446184f1c31 | -6.90477 | -42.08375 | 2025-11-14 04:25:00 | NPP-375D | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 75fba81d-2e0c-350b-98e3-455385c6a8b3 | -6.13999 | -48.05307 | 2025-11-14 04:25:00 | NPP-375D | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 85b7a15b-8b72-3b1f-9892-2dfafa5742f0 | -13.46798 | -46.493 | 2025-11-14 04:25:00 | NPP-375D | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 6132c044-22c7-3ca0-aab3-83d23ae2431f | -5.51973 | -41.74862 | 2025-11-14 04:25:00 | NPP-375D | SÃO JOÃO DA SERRA | PIAUÍ | Brasil | 2209906 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 211d34d9-4505-35c7-b571-11caefa4ed47 | -5.53456 | -43.68144 | 2025-11-14 04:25:00 | NPP-375D | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 7.7 |
| 5f507319-fa67-3ee0-8705-fcc4151fda1d | -5.54764 | -46.47828 | 2025-11-14 04:25:00 | NPP-375D | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 0.4 |
| ad0c4235-80c3-313d-92e9-cc4df5550510 | -12.99584 | -43.86151 | 2025-11-14 04:25:00 | NPP-375D | SANTANA | BAHIA | Brasil | 2928208 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| bb00b2b8-48ca-32a1-a403-4d8a04bc15f6 | -6.48243 | -43.76053 | 2025-11-14 04:25:00 | NPP-375D | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| d70505e9-9d8c-309d-9044-30d12a1d1faa | -6.47361 | -48.36731 | 2025-11-14 04:25:00 | NPP-375D | XAMBIOÁ | TOCANTINS | Brasil | 1722107 | 17 | 33 | nan | nan | nan | Amazônia | 1.8 |
| c4e57a68-7815-34d2-9037-3f7d5ca412ca | -5.45733 | -47.09733 | 2025-11-14 04:25:00 | NPP-375D | BURITIRANA | MARANHÃO | Brasil | 2102358 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| a1ab4b43-39cb-31e7-a7d6-d1675fe2abe3 | -12.69093 | -45.43255 | 2025-11-14 04:25:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 3cddd3d7-345d-38c6-bb88-ec531400b0c1 | -12.59736 | -48.37533 | 2025-11-14 04:25:00 | NPP-375D | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 548a7740-b442-302e-8492-761cefa7bfaa | -14.70092 | -46.61601 | 2025-11-14 04:25:00 | NPP-375D | ALVORADA DO NORTE | GOIÁS | Brasil | 5200803 | 52 | 33 | nan | nan | nan | Cerrado | 12.2 |
| 60464acb-40ad-35ad-80ee-eeb3bbb5ebae | -16.96703 | -52.38389 | 2025-11-14 04:25:00 | NPP-375D | CAIAPÔNIA | GOIÁS | Brasil | 5204409 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| a1ba5afe-6484-3873-9c67-5549ba600b39 | -5.65467 | -46.42253 | 2025-11-14 04:25:00 | NPP-375D | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 43907aa9-9bfe-3afd-b468-14e277121521 | -5.21013 | -42.76896 | 2025-11-14 04:25:00 | NPP-375D | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| dffa1a26-3107-339d-90e3-93f041999ad3 | -3.8509 | -50.20747 | 2025-11-14 04:25:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 90c6341a-12c8-3e60-9743-ecd49227ab36 | -12.04554 | -49.44168 | 2025-11-14 04:25:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 55a46b7f-b4cb-3228-ad58-977988d3919c | -4.53876 | -46.4143 | 2025-11-14 04:25:00 | NPP-375D | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 2176b22d-c1ce-32bc-a7b5-aa43845f3cc5 | -7.2783 | -38.81019 | 2025-11-14 04:25:00 | NPP-375D | MILAGRES | CEARÁ | Brasil | 2308302 | 23 | 33 | nan | nan | nan | Caatinga | 0.8 |


[Clique aqui para ver as próximas entradas](README32.md)
