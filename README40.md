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

## Dados Diários - Página 40

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 0e17c7cd-69d8-30aa-bb5c-89b10221387e | -14.98528 | -46.92476 | 2025-10-02 04:04:00 | NOAA-21 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 10.2 |
| 8758bea8-6c54-3930-b075-5b64eae2fd2e | -13.21613 | -48.51722 | 2025-10-02 04:04:00 | NOAA-21 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 29e3d979-54e9-3118-aff3-485ccd19e976 | -13.36937 | -47.28357 | 2025-10-02 04:04:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 428305ec-770b-3696-ac84-3d53ec78a306 | -19.89087 | -42.62669 | 2025-10-02 04:04:00 | NOAA-21 | DIONÍSIO | MINAS GERAIS | Brasil | 3121803 | 31 | 33 | nan | nan | nan | Mata Atlântica | 7.3 |
| 416d1617-0f1c-3c01-a4ad-50bc4a08b890 | -18.60517 | -50.6991 | 2025-10-02 04:04:00 | NOAA-21 | QUIRINÓPOLIS | GOIÁS | Brasil | 5218508 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| e5d6f018-f9d9-3437-bafd-0db600c170c1 | -14.42358 | -46.10061 | 2025-10-02 04:04:00 | NOAA-21 | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 7286f2d8-e606-3bd3-8273-bd7bd7c12dd6 | -14.61809 | -48.30012 | 2025-10-02 04:04:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 471ccb2d-fdb1-3e92-a078-327769f6b391 | -15.23283 | -48.72867 | 2025-10-02 04:04:00 | NOAA-21 | VILA PROPÍCIO | GOIÁS | Brasil | 5222302 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| fdc158e7-658a-3d4b-8fb5-7e64b136a6f5 | -13.38999 | -46.95122 | 2025-10-02 04:04:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| e6a6c72a-90c9-34a7-ad66-1a205787a713 | -12.70388 | -48.57439 | 2025-10-02 04:04:00 | NOAA-21 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 8.9 |
| bdace1db-c0d6-3e1f-a426-5ec8643c7c38 | -13.17894 | -47.80621 | 2025-10-02 04:04:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 4.6 |
| a790bdcf-5bf3-3d78-8796-ee41ccb317a2 | -16.03569 | -50.91403 | 2025-10-02 04:04:00 | NOAA-21 | JUSSARA | GOIÁS | Brasil | 5212204 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 8ad52876-0334-3bc3-857d-13db518c3611 | -14.47814 | -48.44021 | 2025-10-02 04:04:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 7.9 |
| 04e2f599-7c70-3b41-ae35-949025970310 | -15.94202 | -43.34425 | 2025-10-02 04:04:00 | NOAA-21 | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| ae265881-5976-34b9-930b-fcffcf7de282 | -14.60036 | -48.32262 | 2025-10-02 04:04:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 431c12b2-7b79-39bf-8959-e6a43f33654d | -13.69955 | -48.61993 | 2025-10-02 04:04:00 | NOAA-21 | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 7.9 |
| 2e89007e-6bca-3565-bc0a-05475aab5250 | -19.59483 | -43.81749 | 2025-10-02 04:04:00 | NOAA-21 | JABOTICATUBAS | MINAS GERAIS | Brasil | 3134608 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 8efcb6e5-d59c-3c36-934b-bc6e5983985a | -14.3222 | -45.87818 | 2025-10-02 04:04:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 9c756a32-c30e-3aa0-9710-d7f02ee9c712 | -13.21046 | -48.49734 | 2025-10-02 04:04:00 | NOAA-21 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 5.9 |
| fa8902c7-e78d-3993-b86a-ba50dd1fc7f1 | -18.89236 | -48.28935 | 2025-10-02 04:04:00 | NOAA-21 | UBERLÂNDIA | MINAS GERAIS | Brasil | 3170206 | 31 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 8b904fda-6c24-3a58-8b82-ea162d831702 | -13.68914 | -48.06739 | 2025-10-02 04:04:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 82b4a416-9047-30c3-94f3-d78c1c551340 | -17.22431 | -39.70351 | 2025-10-02 04:04:00 | NOAA-21 | VEREDA | BAHIA | Brasil | 2933257 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 8e223917-6e74-3f1a-9e37-1ecd0f9080b3 | -14.70127 | -48.2135 | 2025-10-02 04:04:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| f3ce12a9-94f6-313b-b9f1-af2144b9168b | -14.87329 | -48.29374 | 2025-10-02 04:04:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 099b6053-4d46-3f7d-90b3-1ef2d2ec7bf4 | -13.68325 | -48.07492 | 2025-10-02 04:04:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 40ff3664-c935-341d-845c-9ba47f4a1e5e | -18.74164 | -43.14733 | 2025-10-02 04:04:00 | NOAA-21 | SABINÓPOLIS | MINAS GERAIS | Brasil | 3156809 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| d564cf29-4eed-341d-bc9c-8199ba685bdf | -16.03051 | -50.86114 | 2025-10-02 04:04:00 | NOAA-21 | FAZENDA NOVA | GOIÁS | Brasil | 5207600 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 82b68a70-e4aa-31ec-8eba-074db81a2715 | -15.99593 | -50.90396 | 2025-10-02 04:04:00 | NOAA-21 | JUSSARA | GOIÁS | Brasil | 5212204 | 52 | 33 | nan | nan | nan | Cerrado | 36.5 |
| 186429a1-3165-34b2-b3df-4de18f9bb13c | -13.16359 | -47.80575 | 2025-10-02 04:04:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 8.3 |
| 07fd3f5c-00df-395a-b256-f04b7da79142 | -20.02257 | -44.54005 | 2025-10-02 04:04:00 | NOAA-21 | ITAÚNA | MINAS GERAIS | Brasil | 3133808 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 9fc0a379-329f-3a6b-8a3f-2c03b3392ea8 | -15.29481 | -46.39523 | 2025-10-02 04:04:00 | NOAA-21 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 2bc67812-7a8a-3ceb-a68a-43886dd5bbeb | -13.78321 | -48.00323 | 2025-10-02 04:04:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| f89b687c-aea0-3755-bb2e-86f099c9bc4a | -13.30366 | -47.19672 | 2025-10-02 04:04:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 5.3 |
| d98c7a6a-1cfb-3d1f-b4e9-91ffdcb998e1 | -13.86584 | -51.24471 | 2025-10-02 04:04:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| bafa9b9e-ee9b-31a9-b5b3-0715a9512a4e | -19.45566 | -44.28025 | 2025-10-02 04:04:00 | NOAA-21 | SETE LAGOAS | MINAS GERAIS | Brasil | 3167202 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 7f1b897c-5587-3d6f-9682-149093a82cd0 | -14.69413 | -49.61438 | 2025-10-02 04:04:00 | NOAA-21 | PILAR DE GOIÁS | GOIÁS | Brasil | 5216908 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 73068040-f8ae-3ee3-8bb1-d97791c07bf3 | -13.8167 | -47.53989 | 2025-10-02 04:04:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 10.3 |
| 5203c2b3-2476-3604-a755-663abba1439c | -13.67896 | -48.07381 | 2025-10-02 04:04:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| a753b0c1-9557-37be-98a2-d7ef64169ed1 | -19.84841 | -44.0821 | 2025-10-02 04:04:00 | NOAA-21 | CONTAGEM | MINAS GERAIS | Brasil | 3118601 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 67c7cb38-d3f4-3c88-9eff-d664a47da294 | -14.89672 | -48.36089 | 2025-10-02 04:04:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 65425e9d-e33d-3407-b5b4-eac2804aa274 | -14.36848 | -45.96943 | 2025-10-02 04:04:00 | NOAA-21 | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 6bf74486-c75c-3eea-80c8-301660a13268 | -13.47028 | -47.25659 | 2025-10-02 04:04:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 8237bcc6-3dca-3400-9d83-ecc5f27d7eca | -13.08076 | -46.99463 | 2025-10-02 04:04:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 239bd8eb-07c0-36ed-85e2-992673bc1bf0 | -14.4257 | -46.11098 | 2025-10-02 04:04:00 | NOAA-21 | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 12.1 |
| e0171c1a-e6d6-33ce-b350-d378cdf445e7 | -13.15308 | -47.83961 | 2025-10-02 04:04:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 6.3 |
| f6958fab-e1f4-34e7-a75c-cac5c425e205 | -13.75744 | -48.01269 | 2025-10-02 04:04:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 7.0 |
| 7ad6573e-9980-3113-b0d8-3b736b25595a | -13.28525 | -47.25089 | 2025-10-02 04:04:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| cb4c5822-0582-350d-9577-6bff9925997b | -14.47144 | -48.4274 | 2025-10-02 04:04:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 21df31ef-7a91-38ec-b25d-2588b9dcfa78 | -15.84027 | -46.24086 | 2025-10-02 04:04:00 | NOAA-21 | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 2.2 |
| f69646c2-5d40-3362-b9fa-53bca5411b91 | -14.43331 | -46.35193 | 2025-10-02 04:04:00 | NOAA-21 | BURITINÓPOLIS | GOIÁS | Brasil | 5203962 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| f2d85ed3-8bf7-3303-9e82-f3169c9d3cf5 | -19.69711 | -43.98682 | 2025-10-02 04:04:00 | NOAA-21 | SÃO JOSÉ DA LAPA | MINAS GERAIS | Brasil | 3162955 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| ae4c1b54-60a1-32f5-a728-2c2864afe42a | -13.18082 | -47.78392 | 2025-10-02 04:04:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| d671db4f-43b9-3f72-a443-d5b3290a1952 | -20.22424 | -43.90571 | 2025-10-02 04:04:00 | NOAA-21 | ITABIRITO | MINAS GERAIS | Brasil | 3131901 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.2 |
| c4a0e088-db80-3e9d-bc8c-5ef01b3a268d | -13.31607 | -47.82312 | 2025-10-02 04:04:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 0db74023-c859-3489-aa58-8c463b1b4b18 | -13.75951 | -48.69971 | 2025-10-02 04:04:00 | NOAA-21 | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 4.0 |
| bd8eae6d-58f8-3db3-8f10-b3b7b5947a0b | -14.68324 | -49.61409 | 2025-10-02 04:04:00 | NOAA-21 | PILAR DE GOIÁS | GOIÁS | Brasil | 5216908 | 52 | 33 | nan | nan | nan | Cerrado | 12.4 |
| 97b15387-b6bb-333a-aafc-0e703fa63167 | -13.32274 | -47.32856 | 2025-10-02 04:04:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 216b3240-8922-3508-a6ab-0b7dfe6441b6 | -15.50722 | -45.89875 | 2025-10-02 04:04:00 | NOAA-21 | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 5c1ab6af-c32c-3d0a-9c9b-78a1e306fd5f | -13.91482 | -48.07476 | 2025-10-02 04:04:00 | NOAA-21 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| bc746d6c-7f0b-339b-acfb-7ba3d067c25c | -13.76125 | -48.69751 | 2025-10-02 04:04:00 | NOAA-21 | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| dedb10e8-acb9-32e1-be90-48e4aa29bb8b | -14.69739 | -49.617 | 2025-10-02 04:04:00 | NOAA-21 | PILAR DE GOIÁS | GOIÁS | Brasil | 5216908 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 6ee25a4c-9308-382a-b481-de51e7e348cd | -13.53342 | -47.24982 | 2025-10-02 04:04:00 | NOAA-21 | TERESINA DE GOIÁS | GOIÁS | Brasil | 5221080 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 62f7c919-1ae8-37c4-95c5-9f5be14c30b2 | -12.91177 | -47.16514 | 2025-10-02 04:04:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 426289e2-7070-34f1-a0cc-3e27c4dfe92f | -18.61177 | -50.69697 | 2025-10-02 04:04:00 | NOAA-21 | QUIRINÓPOLIS | GOIÁS | Brasil | 5218508 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| b16b4754-9a00-393a-9173-f7df00066d9d | -14.89234 | -48.36031 | 2025-10-02 04:04:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 5db9b7d7-98a6-3de6-98cf-13862483d6d5 | -13.21546 | -48.44501 | 2025-10-02 04:04:00 | NOAA-21 | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 7fe6add4-1a9e-37cb-921e-def2d76fb2c8 | -19.62105 | -43.90915 | 2025-10-02 04:04:00 | NOAA-21 | LAGOA SANTA | MINAS GERAIS | Brasil | 3137601 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 6d663e9e-1d16-3e98-9aa2-8ac5f65018ed | -20.48862 | -43.9341 | 2025-10-02 04:04:00 | NOAA-21 | CONGONHAS | MINAS GERAIS | Brasil | 3118007 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| c2bdb8c5-89c9-34aa-9e41-4c26beeb1038 | -13.338 | -47.8003 | 2025-10-02 04:04:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| b3fc2b9f-7174-3c45-b36c-35954d4ca659 | -12.57076 | -49.89677 | 2025-10-02 04:04:00 | NOAA-21 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 051b059d-7e31-3c09-8a81-2333c2487725 | -13.75769 | -51.21505 | 2025-10-02 04:04:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 5248477b-791f-3338-a100-982719217822 | -16.36037 | -47.03252 | 2025-10-02 04:04:00 | NOAA-21 | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 3.6 |
| e96a4854-a2ad-3781-82e7-5e6c51b6c01f | -14.29928 | -45.89849 | 2025-10-02 04:04:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 105860e3-56a7-3ae2-8d42-5eec8531ee92 | -13.24502 | -47.32252 | 2025-10-02 04:04:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| ef9c912b-6a79-3f61-bb20-a894a7af2e1f | -13.05567 | -47.01696 | 2025-10-02 04:04:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 40b8c6df-7f4f-355d-948b-0c04632f1829 | -14.8928 | -48.33343 | 2025-10-02 04:04:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| bfdb3ed4-c279-3936-b3d2-ee381a234fbc | -16.00158 | -50.9018 | 2025-10-02 04:04:00 | NOAA-21 | JUSSARA | GOIÁS | Brasil | 5212204 | 52 | 33 | nan | nan | nan | Cerrado | 36.5 |
| 92b53ff5-ee46-3958-a81b-1a6b0ffa9df0 | -16.00666 | -50.90253 | 2025-10-02 04:04:00 | NOAA-21 | JUSSARA | GOIÁS | Brasil | 5212204 | 52 | 33 | nan | nan | nan | Cerrado | 7.0 |
| 9842a7b6-e565-3453-a196-6e1661753189 | -17.18055 | -47.03664 | 2025-10-02 04:04:00 | NOAA-21 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 41.7 |
| a341573c-4e7b-3f8f-badd-5ea03bd6dedd | -14.42736 | -46.10141 | 2025-10-02 04:04:00 | NOAA-21 | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 5.0 |
| d20120b3-140f-33e6-8e95-e3e25b0968e8 | -14.90551 | -47.22118 | 2025-10-02 04:04:00 | NOAA-21 | VILA BOA | GOIÁS | Brasil | 5222203 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 2e6def0b-5fc4-35be-8904-f8c0dff87b4b | -13.80344 | -47.54136 | 2025-10-02 04:04:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 13.2 |
| 2cf6b4da-9629-3d8a-8f9b-3d5aa445df56 | -13.40044 | -47.55173 | 2025-10-02 04:04:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 12.3 |
| 385b20e3-d3d4-370e-83db-8002a569ec7f | -18.73255 | -46.88638 | 2025-10-02 04:04:00 | NOAA-21 | PATROCÍNIO | MINAS GERAIS | Brasil | 3148103 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 550eb2a6-8d9e-3211-96be-1407b8e28182 | -15.93928 | -43.34001 | 2025-10-02 04:04:00 | NOAA-21 | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 21582481-2e69-31c6-9540-53a5033e21f1 | -12.70262 | -48.582 | 2025-10-02 04:04:00 | NOAA-21 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 5.8 |
| e9d50fc3-b49b-3673-b065-75b3e813ad0b | -17.96674 | -45.01085 | 2025-10-02 04:04:00 | NOAA-21 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 33eb8430-6955-397e-8682-e41981241e68 | -13.78617 | -48.05927 | 2025-10-02 04:04:00 | NOAA-21 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 08a0aa6c-25d7-30b7-a215-0a1cdd3e8533 | -13.96196 | -48.13564 | 2025-10-02 04:04:00 | NOAA-21 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 13.3 |
| 6f992afa-bc8b-3280-81f5-98684153b794 | -15.25803 | -49.29866 | 2025-10-02 04:04:00 | NOAA-21 | GOIANÉSIA | GOIÁS | Brasil | 5208608 | 52 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 83a1ba2e-a1e7-3b0c-a1de-dc861d1c3a07 | -16.13999 | -46.68504 | 2025-10-02 04:04:00 | NOAA-21 | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 2b32a227-a18a-31bd-a9ef-6202a2d40090 | -14.67721 | -48.22309 | 2025-10-02 04:04:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| e2d171e5-73e5-3a68-af5a-b154f63385ca | -13.17115 | -47.83832 | 2025-10-02 04:04:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 7c189831-aea4-3419-91a1-bbb389b6e787 | -14.6926 | -45.19113 | 2025-10-02 04:04:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 0.4 |
| ce79252d-b70e-39e9-a0df-28b099f6fd4c | -13.57242 | -47.58871 | 2025-10-02 04:04:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 4877951a-4fe1-35e3-ba36-767b9de128c9 | -16.03616 | -50.85889 | 2025-10-02 04:04:00 | NOAA-21 | FAZENDA NOVA | GOIÁS | Brasil | 5207600 | 52 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 5dbdc08a-a562-3a96-a3e9-87bde86b865d | -13.67101 | -48.03669 | 2025-10-02 04:04:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 0dd0abcc-71ae-3dd6-851f-99484f113150 | -17.96359 | -44.3982 | 2025-10-02 04:04:00 | NOAA-21 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 1fe64927-fc2a-3f47-8f21-8e416fefc892 | -13.32874 | -47.87576 | 2025-10-02 04:04:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 6ef8a220-ccb4-35a9-ae54-9ccda75b02b8 | -15.35425 | -46.281 | 2025-10-02 04:04:00 | NOAA-21 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |


[Clique aqui para ver as próximas entradas](README41.md)
