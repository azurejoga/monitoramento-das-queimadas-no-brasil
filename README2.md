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

## Dados Diários - Página 2

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 14bd3c97-9ab3-34ca-bd2f-88f5ceed6b60 | -11.80881 | -46.79149 | 2025-08-28 00:09:00 | TERRA_M-M | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 12.3 |
| a53a496d-cda4-350e-965d-e08dacbcce78 | -17.54752 | -46.60744 | 2025-08-28 00:09:00 | TERRA_M-M | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 24.0 |
| 4edc8877-31e9-383d-ad91-84d7a074fc69 | -8.44686 | -43.66532 | 2025-08-28 00:09:00 | TERRA_M-M | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 8798d088-8306-30ce-80a2-0a6511300fab | -10.12569 | -47.42609 | 2025-08-28 00:09:00 | TERRA_M-M | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 12.4 |
| 45d0a2df-3ffd-3947-8946-f9d15ed81cc3 | -14.13518 | -45.40554 | 2025-08-28 00:09:00 | TERRA_M-M | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 18.1 |
| a74b3db3-09f3-3669-adce-be0bbac69db4 | -13.23024 | -40.94903 | 2025-08-28 00:09:00 | TERRA_M-M | ITAETÉ | BAHIA | Brasil | 2915007 | 29 | 33 | nan | nan | nan | Caatinga | 6.8 |
| 1caaa2f5-6809-3936-bacd-a04f779eda20 | -17.76154 | -44.48861 | 2025-08-28 00:09:00 | TERRA_M-M | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 7.6 |
| c8bca093-6d33-3904-9e63-8991e8544ee3 | -18.06271 | -45.17136 | 2025-08-28 00:09:00 | TERRA_M-M | TRÊS MARIAS | MINAS GERAIS | Brasil | 3169356 | 31 | 33 | nan | nan | nan | Cerrado | 8.0 |
| 6252739b-4a77-3617-a56d-48cb308d5d53 | -9.47739 | -51.93122 | 2025-08-28 00:09:00 | TERRA_M-M | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 104.8 |
| 7840c0df-f0fc-3429-8ff8-81c375e6b722 | -12.8861 | -48.12033 | 2025-08-28 00:09:00 | TERRA_M-M | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 33.7 |
| 0a7bec76-6051-38b5-b92d-47ed9bb461b0 | -13.61621 | -48.23812 | 2025-08-28 00:09:00 | TERRA_M-M | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 57.7 |
| 3399beda-3379-38ce-b5ae-b0a2630fe597 | -11.34018 | -43.55462 | 2025-08-28 00:09:00 | TERRA_M-M | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 14.1 |
| 6bc2572f-e667-3e33-b2e4-bc7e402fd832 | -10.53665 | -46.68453 | 2025-08-28 00:09:00 | TERRA_M-M | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 20.7 |
| 72f1690a-4abe-3ebd-873a-f6f37272a9b3 | -12.81108 | -48.15035 | 2025-08-28 00:09:00 | TERRA_M-M | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 26.4 |
| de81588e-19c2-365e-bdf9-3c8f5bcf173a | -12.96279 | -44.57568 | 2025-08-28 00:09:00 | TERRA_M-M | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 28.8 |
| ec9525a4-679e-31bf-b5f8-3116d4f4c0c3 | -9.49546 | -40.86873 | 2025-08-28 00:09:00 | TERRA_M-M | SOBRADINHO | BAHIA | Brasil | 2930774 | 29 | 33 | nan | nan | nan | Caatinga | 10.8 |
| 959590a4-a4fc-3349-9eb9-e70f19255e8d | -17.76884 | -44.4955 | 2025-08-28 00:09:00 | TERRA_M-M | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 16d0d8ea-9e89-3aec-9404-8c038de10394 | -14.14579 | -45.40423 | 2025-08-28 00:09:00 | TERRA_M-M | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 10.9 |
| 9a8e1749-02d5-3f22-85dd-ed363231dd5d | -14.24196 | -44.11895 | 2025-08-28 00:09:00 | TERRA_M-M | FEIRA DA MATA | BAHIA | Brasil | 2910776 | 29 | 33 | nan | nan | nan | Cerrado | 15.8 |
| 7b03c2da-ea76-3785-bf15-d57860d7422d | -7.947 | -42.6446 | 2025-08-28 00:09:00 | TERRA_M-M | RIBEIRA DO PIAUÍ | PIAUÍ | Brasil | 2208874 | 22 | 33 | nan | nan | nan | Caatinga | 14.1 |
| 0b936093-1797-3105-aa5d-fe83315fb6be | -9.48137 | -51.96786 | 2025-08-28 00:09:00 | TERRA_M-M | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 74.3 |
| 64c7d142-b9d0-393d-b682-a213adb506a3 | -11.31935 | -43.53795 | 2025-08-28 00:09:00 | TERRA_M-M | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 37.1 |
| d2d28a8b-10b2-3886-a81d-b9e05bd95471 | -13.99551 | -46.34449 | 2025-08-28 00:09:00 | TERRA_M-M | GUARANI DE GOIÁS | GOIÁS | Brasil | 5209408 | 52 | 33 | nan | nan | nan | Cerrado | 9.1 |
| 325b8886-76ef-345d-9def-fe089ad4ae68 | -13.74588 | -51.8985 | 2025-08-28 00:09:00 | TERRA_M-M | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 70.4 |
| 49f4b7b4-e64f-35f2-ade8-e5ce6c172e9d | -13.1859 | -45.27966 | 2025-08-28 00:09:00 | TERRA_M-M | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 16.0 |
| 64b98ef0-0d17-3296-a1be-fa0a38f99598 | -9.13943 | -45.22293 | 2025-08-28 00:09:00 | TERRA_M-M | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 8.7 |
| ee57d848-25b8-3e13-8c30-1bbc0f194969 | -11.57536 | -44.6511 | 2025-08-28 00:09:00 | TERRA_M-M | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 37.8 |
| e5d9dcb2-3e4f-3a15-81f8-6bbc004d5f33 | -13.17716 | -45.29367 | 2025-08-28 00:09:00 | TERRA_M-M | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 118.0 |
| 0b0fdc59-94a3-3929-b862-00e8d0e1de27 | -9.10365 | -46.05514 | 2025-08-28 00:09:00 | TERRA_M-M | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 13.1 |
| e208ce75-9faf-3623-8e6a-0b686cbd0096 | -8.47359 | -43.65532 | 2025-08-28 00:09:00 | TERRA_M-M | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Cerrado | 7.1 |
| a004a7a5-4a1e-3267-96ed-c23d9285fc4e | -12.7994 | -48.15769 | 2025-08-28 00:09:00 | TERRA_M-M | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 66.1 |
| 9b71ae62-d890-3b25-b824-6401e8c0d26e | -7.94455 | -42.62689 | 2025-08-28 00:09:00 | TERRA_M-M | RIBEIRA DO PIAUÍ | PIAUÍ | Brasil | 2208874 | 22 | 33 | nan | nan | nan | Caatinga | 4.7 |
| 7ec178ac-072a-327f-be17-f758a790b9d4 | -8.45458 | -43.65485 | 2025-08-28 00:09:00 | TERRA_M-M | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Cerrado | 5.4 |
| fdd08a7e-ca31-3ddb-bf23-9ea4874e810f | -11.81048 | -44.26303 | 2025-08-28 00:09:00 | TERRA_M-M | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 8.6 |
| 8e4a523c-3d04-3fbc-992c-18ca6363c070 | -9.14083 | -45.23379 | 2025-08-28 00:09:00 | TERRA_M-M | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 70564237-b766-33da-9def-5efb5a2d5206 | -13.62615 | -48.22786 | 2025-08-28 00:09:00 | TERRA_M-M | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 37.0 |
| 6097132f-d7ee-373c-8140-4ac5bf4d9b60 | -11.21494 | -43.37373 | 2025-08-28 00:09:00 | TERRA_M-M | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Caatinga | 18.1 |
| a693c793-2d37-3312-ab68-abac7a693e22 | -11.28777 | -43.29952 | 2025-08-28 00:09:00 | TERRA_M-M | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 6.8 |
| c6b113a5-a975-31f7-a0ef-e31dbebc3eb0 | -11.32062 | -43.54757 | 2025-08-28 00:09:00 | TERRA_M-M | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 13.0 |
| 77cc3ddd-b57c-3d22-b266-c46a650a61e1 | -10.54771 | -46.68304 | 2025-08-28 00:09:00 | TERRA_M-M | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 19.4 |
| 5412da50-ee14-32c2-9f64-b16f40bf727a | -13.18369 | -45.28701 | 2025-08-28 00:09:00 | TERRA_M-M | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 160.1 |
| 5e400099-79c6-3d9a-acd0-e7e072489fed | -13.32841 | -40.34006 | 2025-08-28 00:09:00 | TERRA_M-M | MARACÁS | BAHIA | Brasil | 2920502 | 29 | 33 | nan | nan | nan | Mata Atlântica | 6.5 |
| 6738490d-7978-3231-ac85-8d79c6bc35c9 | -11.32722 | -43.52707 | 2025-08-28 00:09:00 | TERRA_M-M | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 37.3 |
| 3cddb0b2-b220-3115-8036-4b1654919514 | -11.33253 | -43.49699 | 2025-08-28 00:09:00 | TERRA_M-M | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 7.0 |
| da77fc00-0c68-3b7b-a1b5-61443541a082 | -13.07985 | -46.33674 | 2025-08-28 00:09:00 | TERRA_M-M | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 17.1 |
| 629d4327-d9a3-3454-aed7-abe4884d51b7 | -16.54173 | -42.347 | 2025-08-28 00:09:00 | TERRA_M-M | VIRGEM DA LAPA | MINAS GERAIS | Brasil | 3171600 | 31 | 33 | nan | nan | nan | Cerrado | 14.3 |
| 80bb728e-ce14-3a40-afc3-3cea07386afa | -13.61373 | -48.21682 | 2025-08-28 00:09:00 | TERRA_M-M | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 17.6 |
| 071c9680-1c58-3f1d-b0e4-6d0cfd617765 | -11.79739 | -46.79261 | 2025-08-28 00:09:00 | TERRA_M-M | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 18.2 |
| 1c688642-f3ed-391c-9055-a5c0d3a229ab | -12.8006 | -48.17361 | 2025-08-28 00:09:00 | TERRA_M-M | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 31.8 |
| 28e821a8-fc4d-3ae8-9525-7e316d77bea0 | -9.86433 | -44.69418 | 2025-08-28 00:09:00 | TERRA_M-M | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 9.4 |
| d829ef3b-2c44-32ca-9232-1d170806d769 | -17.54434 | -46.6133 | 2025-08-28 00:09:00 | TERRA_M-M | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 35.6 |
| 37c11687-4716-343d-8243-4fdd3cc23924 | -11.33508 | -43.51617 | 2025-08-28 00:09:00 | TERRA_M-M | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 9.1 |
| b3b1096f-e5c5-3b9d-96d3-d1d631084d0e | -15.7095 | -41.76034 | 2025-08-28 00:09:00 | TERRA_M-M | BERIZAL | MINAS GERAIS | Brasil | 3106655 | 31 | 33 | nan | nan | nan | Mata Atlântica | 9.8 |
| 47c74d0a-c8dd-3b5b-a22b-8734abc5121e | -14.13679 | -45.41889 | 2025-08-28 00:09:00 | TERRA_M-M | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 9.3 |
| 333f3829-daca-3d25-bd51-ed2169dec398 | -13.7572 | -42.50053 | 2025-08-28 00:09:00 | TERRA_M-M | CAETITÉ | BAHIA | Brasil | 2905206 | 29 | 33 | nan | nan | nan | Caatinga | 4.5 |
| e5e01ff3-61b3-3513-b96d-ddafe196d030 | -9.03406 | -42.70573 | 2025-08-28 00:09:00 | TERRA_M-M | SÃO RAIMUNDO NONATO | PIAUÍ | Brasil | 2210607 | 22 | 33 | nan | nan | nan | Caatinga | 12.5 |
| b23e14ee-6287-3a96-92e2-8abfc19990a8 | -8.44545 | -41.45596 | 2025-08-28 00:09:00 | TERRA_M-M | QUEIMADA NOVA | PIAUÍ | Brasil | 2208650 | 22 | 33 | nan | nan | nan | Caatinga | 7.8 |
| 0607e026-fdfd-3efa-980b-f5b5e78dd5c5 | -12.78651 | -48.15947 | 2025-08-28 00:09:00 | TERRA_M-M | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 27.9 |
| 7713873e-9cb5-31ac-a9da-43efb34a4a71 | -11.34335 | -43.30116 | 2025-08-28 00:09:00 | TERRA_M-M | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 5122d801-919a-371d-bcf6-5966fa338527 | -11.31808 | -43.52834 | 2025-08-28 00:09:00 | TERRA_M-M | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 13.3 |
| 44f875c3-aa33-300b-bdb8-9369f300c833 | -12.96425 | -44.58708 | 2025-08-28 00:09:00 | TERRA_M-M | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 18.2 |
| 117eb966-fe4d-3f85-886a-8866dca8de4f | -17.54279 | -44.37085 | 2025-08-28 00:09:00 | TERRA_M-M | FRANCISCO DUMONT | MINAS GERAIS | Brasil | 3126604 | 31 | 33 | nan | nan | nan | Cerrado | 15.2 |
| f7d45def-adf8-30e8-b06a-9619ad5ba2f0 | -7.93818 | -42.64586 | 2025-08-28 00:09:00 | TERRA_M-M | RIBEIRA DO PIAUÍ | PIAUÍ | Brasil | 2208874 | 22 | 33 | nan | nan | nan | Caatinga | 8.3 |
| 89692675-733f-3c90-840c-b584c5230084 | -13.98425 | -46.34685 | 2025-08-28 00:09:00 | TERRA_M-M | GUARANI DE GOIÁS | GOIÁS | Brasil | 5209408 | 52 | 33 | nan | nan | nan | Cerrado | 12.2 |
| cdfe2f6a-e1bd-3803-a5bb-66d5843f9bc1 | -12.44462 | -40.7993 | 2025-08-28 00:09:00 | TERRA_M-M | LAJEDINHO | BAHIA | Brasil | 2919009 | 29 | 33 | nan | nan | nan | Caatinga | 17.9 |
| af3c58de-069e-353e-9548-f2a303d02fe8 | -13.18752 | -45.29229 | 2025-08-28 00:09:00 | TERRA_M-M | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 37.5 |
| 6c208233-a712-3de7-a162-2015c77d3631 | -13.66982 | -46.88467 | 2025-08-28 00:09:00 | TERRA_M-M | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 18.4 |
| 1572f103-0592-39d6-b6fa-bf7292027a21 | -11.32976 | -43.54629 | 2025-08-28 00:09:00 | TERRA_M-M | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 36.8 |
| 044db3a2-782e-3a90-a378-6b3f09ab9f40 | -9.13949 | -40.5665 | 2025-08-28 00:09:00 | TERRA_M-M | PETROLINA | PERNAMBUCO | Brasil | 2611101 | 26 | 33 | nan | nan | nan | Caatinga | 13.1 |
| b2486d8c-8409-35ec-811d-30e16e041985 | -8.89943 | -47.3278 | 2025-08-28 00:09:00 | TERRA_M-M | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | 20.7 |
| 1b86e922-f5cd-3030-8a2a-8a078f750302 | -12.79821 | -48.15225 | 2025-08-28 00:09:00 | TERRA_M-M | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 56.0 |
| 52bc4bc1-0eb0-31e1-925d-13a3e64e8e1e | -8.6147 | -45.90392 | 2025-08-28 00:09:00 | TERRA_M-M | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 8.6 |
| f837aabb-e12a-3750-bed2-582c53b79617 | -13.75121 | -51.93501 | 2025-08-28 00:09:00 | TERRA_M-M | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 54.9 |
| dc8c1791-8329-3783-8155-f333fc84e784 | -9.50088 | -40.3318 | 2025-08-28 00:09:00 | TERRA_M-M | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 10.8 |
| 35d667b5-c798-3b68-8e98-dfeec4cdb877 | -13.18523 | -45.29968 | 2025-08-28 00:09:00 | TERRA_M-M | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 40.1 |
| 4a5aeb18-6364-3d66-a2fe-92a8b4331daf | -12.9544 | -44.58836 | 2025-08-28 00:09:00 | TERRA_M-M | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 15.6 |
| ca337b45-0cbb-34e8-8e16-b16e0b833f90 | -12.44234 | -45.97366 | 2025-08-28 00:09:00 | TERRA_M-M | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 15.8 |
| 30b75990-57b4-3148-8c55-83c208b489c4 | -8.82901 | -40.59132 | 2025-08-28 00:09:00 | TERRA_M-M | PETROLINA | PERNAMBUCO | Brasil | 2611101 | 26 | 33 | nan | nan | nan | Caatinga | 5.5 |
| d1ef776a-4817-32b5-bb15-4c2b3c78fa3e | -8.43526 | -41.45401 | 2025-08-28 00:09:00 | TERRA_M-M | QUEIMADA NOVA | PIAUÍ | Brasil | 2208650 | 22 | 33 | nan | nan | nan | Caatinga | 30.4 |
| 24f0d60a-1547-381e-ae47-6d27242a6b4a | -16.1502 | -40.34851 | 2025-08-28 00:09:00 | TERRA_M-M | JACINTO | MINAS GERAIS | Brasil | 3134707 | 31 | 33 | nan | nan | nan | Mata Atlântica | 5.2 |
| 2168d7e4-a755-3be3-b134-4a0c4e3084cb | -7.93941 | -42.65472 | 2025-08-28 00:09:00 | TERRA_M-M | RIBEIRA DO PIAUÍ | PIAUÍ | Brasil | 2208874 | 22 | 33 | nan | nan | nan | Caatinga | 9.8 |
| 58cd5c42-4358-36bc-b270-3c7fb4ae368a | -10.70044 | -47.08479 | 2025-08-28 00:09:00 | TERRA_M-M | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 8.8 |
| e6ac6b3f-a2b6-332e-8fa4-e6a1a27f6e17 | -8.44415 | -41.44682 | 2025-08-28 00:09:00 | TERRA_M-M | QUEIMADA NOVA | PIAUÍ | Brasil | 2208650 | 22 | 33 | nan | nan | nan | Caatinga | 5.9 |
| fcc10a6d-2550-3e58-9bfa-427598d0b0b2 | -13.75018 | -51.94031 | 2025-08-28 00:09:00 | TERRA_M-M | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 34.6 |
| 53202da3-7c68-3b10-98d1-aff7da1fe9be | -9.49201 | -51.9727 | 2025-08-28 00:09:00 | TERRA_M-M | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 38.4 |
| b6290bba-18bf-3b73-ba14-9d204034a4b7 | -13.17555 | -45.28103 | 2025-08-28 00:09:00 | TERRA_M-M | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 130.2 |
| 40141c7b-f635-3766-82ce-6ee2a707b71f | -13.32975 | -40.34942 | 2025-08-28 00:09:00 | TERRA_M-M | MARACÁS | BAHIA | Brasil | 2920502 | 29 | 33 | nan | nan | nan | Mata Atlântica | 5.6 |
| b3dd14ac-19cf-3671-a5c0-fde0c1c94d6a | -11.35757 | -47.87469 | 2025-08-28 00:09:00 | TERRA_M-M | SANTA ROSA DO TOCANTINS | TOCANTINS | Brasil | 1718907 | 17 | 33 | nan | nan | nan | Cerrado | 79.4 |
| 3b8084f4-c0d2-3a16-90e7-d8bb97b5574c | -17.90587 | -44.25772 | 2025-08-28 00:09:00 | TERRA_M-M | BUENÓPOLIS | MINAS GERAIS | Brasil | 3109204 | 31 | 33 | nan | nan | nan | Cerrado | 17.3 |
| c2d83940-c1e1-3d42-be46-1eb780a951fc | -16.40393 | -49.95053 | 2025-08-28 00:09:00 | TERRA_M-M | ANICUNS | GOIÁS | Brasil | 5201306 | 52 | 33 | nan | nan | nan | Cerrado | 85.5 |
| f872accb-e27a-3533-a8f7-fee73fcf8a50 | -12.06349 | -46.63216 | 2025-08-28 00:09:00 | TERRA_M-M | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 15.2 |
| 8b86c718-605c-378f-a027-93abdde9952d | -8.6132 | -45.89235 | 2025-08-28 00:09:00 | TERRA_M-M | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 19.3 |
| d431094d-ba40-3e8f-ae10-ec71441029f8 | -12.43749 | -45.96677 | 2025-08-28 00:09:00 | TERRA_M-M | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 63.7 |
| 1303efe3-5410-336b-bdcd-59ef7a0fad3a | -11.56415 | -46.39524 | 2025-08-28 00:09:00 | TERRA_M-M | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 17.6 |
| b3f9c696-6b65-3bd0-9b3d-1d7989482dcd | -13.60069 | -48.21922 | 2025-08-28 00:09:00 | TERRA_M-M | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 18.1 |
| 0b368965-eb4e-37cf-9554-304dcded989c | -11.63191 | -44.85784 | 2025-08-28 00:09:00 | TERRA_M-M | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 53107abc-fd59-37db-93c5-69438ede3945 | -9.10209 | -46.04303 | 2025-08-28 00:09:00 | TERRA_M-M | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 11.8 |
| 0c720274-4977-3c8f-a8f4-a22e2950855a | -9.49945 | -40.32196 | 2025-08-28 00:09:00 | TERRA_M-M | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 29.6 |
| 9f5de91c-4520-32de-8ebe-1b2188e01b46 | -9.03529 | -42.71465 | 2025-08-28 00:09:00 | TERRA_M-M | SÃO RAIMUNDO NONATO | PIAUÍ | Brasil | 2210607 | 22 | 33 | nan | nan | nan | Caatinga | 4.9 |
| e9554120-9490-3b6f-b135-af9e339693b9 | -13.18216 | -45.27436 | 2025-08-28 00:09:00 | TERRA_M-M | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 22.8 |


[Clique aqui para ver as próximas entradas](README3.md)
