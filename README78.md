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

## Dados Diários - Página 78

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| f69cb283-d233-3319-b45d-027214506688 | -16.47807 | -55.10414 | 2025-09-16 04:53:00 | NOAA-20 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 20.2 |
| 6a38a3e3-64f3-3ed5-b05b-34fbfb375fbc | -16.06718 | -59.41689 | 2025-09-16 04:53:00 | NOAA-20 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| d2506077-5fe6-35eb-adcb-b631d9329e5d | -17.07961 | -45.83674 | 2025-09-16 04:53:00 | NOAA-20 | BRASILÂNDIA DE MINAS | MINAS GERAIS | Brasil | 3108552 | 31 | 33 | nan | nan | nan | Cerrado | 17.6 |
| 84264f39-2f99-3281-aeeb-57bbfacfd7ed | -15.99716 | -59.42224 | 2025-09-16 04:53:00 | NOAA-20 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 66692fcb-ce63-3128-9f15-620f8a10c2f3 | -15.80664 | -53.46023 | 2025-09-16 04:53:00 | NOAA-20 | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 311c1a10-78d7-3777-817d-0fb1e129656d | -15.79317 | -53.45812 | 2025-09-16 04:53:00 | NOAA-20 | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| a7478de1-70e6-3daf-b67e-1a9180fd9c8a | -16.01607 | -59.2513 | 2025-09-16 04:53:00 | NOAA-20 | PORTO ESPERIDIÃO | MATO GROSSO | Brasil | 5106828 | 51 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 9eb463af-6d45-35b6-9d40-1533e77866e6 | -15.77245 | -53.45843 | 2025-09-16 04:53:00 | NOAA-20 | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 754f4c62-f805-3eab-9a4e-012e1da6b062 | -16.01594 | -59.45157 | 2025-09-16 04:53:00 | NOAA-20 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 38fbfdec-cf7c-3ce4-83ec-0ef5f624d9f9 | -16.06397 | -59.42925 | 2025-09-16 04:53:00 | NOAA-20 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 4b553918-21e3-3504-a162-b9b1ff5b97c9 | -16.06099 | -59.42345 | 2025-09-16 04:53:00 | NOAA-20 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e2244aa1-bc7b-32ea-9cc6-3bfdf5202359 | -15.83686 | -59.41471 | 2025-09-16 04:53:00 | NOAA-20 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 930fcff5-d152-3756-8e5d-229a6688350d | -16.28331 | -45.6811 | 2025-09-16 04:53:00 | NOAA-20 | SÃO ROMÃO | MINAS GERAIS | Brasil | 3164209 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| efb6cf59-be24-38e5-8c43-80bb08137ca9 | -16.02923 | -59.24426 | 2025-09-16 04:53:00 | NOAA-20 | PORTO ESPERIDIÃO | MATO GROSSO | Brasil | 5106828 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| dcb6d77e-d77d-3743-87a3-cddab33b3b9b | -18.15937 | -49.20597 | 2025-09-16 04:53:00 | NOAA-20 | BURITI ALEGRE | GOIÁS | Brasil | 5203906 | 52 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 74ff4ddc-afe1-3a31-973d-5b6ae1a03a64 | -16.70066 | -54.96507 | 2025-09-16 04:53:00 | NOAA-20 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| ee7e2960-7d1b-3dc4-96dd-617d84a0e525 | -18.16364 | -49.20663 | 2025-09-16 04:53:00 | NOAA-20 | BURITI ALEGRE | GOIÁS | Brasil | 5203906 | 52 | 33 | nan | nan | nan | Mata Atlântica | 4.3 |
| 64b7b854-4a3d-344e-9e78-07365c80ba7b | -15.81841 | -53.47346 | 2025-09-16 04:53:00 | NOAA-20 | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 4af5868f-94c7-381a-8552-388b4ad6561c | -17.07503 | -45.82963 | 2025-09-16 04:53:00 | NOAA-20 | BRASILÂNDIA DE MINAS | MINAS GERAIS | Brasil | 3108552 | 31 | 33 | nan | nan | nan | Cerrado | 10.2 |
| 7f032171-e5ea-314f-be3d-e794d6f579d0 | -17.07046 | -45.82927 | 2025-09-16 04:53:00 | NOAA-20 | BRASILÂNDIA DE MINAS | MINAS GERAIS | Brasil | 3108552 | 31 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 857d60a0-cf40-3b6f-9424-d2e55b91d0e7 | -16.71392 | -54.96732 | 2025-09-16 04:53:00 | NOAA-20 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 68c07943-cafe-3df0-87c6-22d6f0711f2b | -15.65174 | -52.76624 | 2025-09-16 04:53:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| cc2dbafc-16df-3cee-9667-28407fcb952c | -15.85898 | -59.38499 | 2025-09-16 04:53:00 | NOAA-20 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| f882e903-7ac9-3690-9652-75516c97fcd4 | -15.99827 | -59.25232 | 2025-09-16 04:53:00 | NOAA-20 | PORTO ESPERIDIÃO | MATO GROSSO | Brasil | 5106828 | 51 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 66acde8c-0efd-3d2b-a2a4-c6354128ce7a | -16.68758 | -49.76686 | 2025-09-16 04:53:00 | NOAA-20 | PALMEIRAS DE GOIÁS | GOIÁS | Brasil | 5215702 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| bc2006ef-9658-3540-9263-ec2c3a5245e7 | -16.70406 | -54.94351 | 2025-09-16 04:53:00 | NOAA-20 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| d9bfc779-768f-3216-b6f2-fcee9d8dd403 | -15.26344 | -56.03823 | 2025-09-16 04:53:00 | NOAA-20 | CUIABÁ | MATO GROSSO | Brasil | 5103403 | 51 | 33 | nan | nan | nan | Cerrado | 4.9 |
| f46f587f-9557-3247-b953-0bf6776e0106 | -15.86372 | -59.38098 | 2025-09-16 04:53:00 | NOAA-20 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 69fb6b22-c888-37d4-b693-2e435b609be2 | -17.08028 | -45.83691 | 2025-09-16 04:53:00 | NOAA-20 | BRASILÂNDIA DE MINAS | MINAS GERAIS | Brasil | 3108552 | 31 | 33 | nan | nan | nan | Cerrado | 19.6 |
| 9a47ad30-6c43-3112-a4e6-aec5993cab73 | -16.02544 | -59.2433 | 2025-09-16 04:53:00 | NOAA-20 | PORTO ESPERIDIÃO | MATO GROSSO | Brasil | 5106828 | 51 | 33 | nan | nan | nan | Amazônia | 3.7 |
| ed667822-5809-3fdd-885c-a8fb9ba88013 | -15.99743 | -59.2571 | 2025-09-16 04:53:00 | NOAA-20 | PORTO ESPERIDIÃO | MATO GROSSO | Brasil | 5106828 | 51 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 73759655-7570-319e-abfd-2f52ead7bf69 | -15.99335 | -59.2672 | 2025-09-16 04:53:00 | NOAA-20 | PORTO ESPERIDIÃO | MATO GROSSO | Brasil | 5106828 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 7dc0da8e-edff-3c47-90eb-6e350bca2ca0 | -15.83801 | -59.4309 | 2025-09-16 04:53:00 | NOAA-20 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| bac44fdc-4a49-3c34-9730-5468a3b97e64 | -16.28294 | -45.6844 | 2025-09-16 04:53:00 | NOAA-20 | SÃO ROMÃO | MINAS GERAIS | Brasil | 3164209 | 31 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 0ffe8477-135d-3a3c-ae29-ff131b77e776 | -15.77804 | -53.44422 | 2025-09-16 04:53:00 | NOAA-20 | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 2d974f97-4589-3c1c-a817-20ff8f054561 | -15.79459 | -52.17815 | 2025-09-16 04:53:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 997eb856-f918-326a-8526-8b5341d5a264 | -16.72045 | -54.94538 | 2025-09-16 04:53:00 | NOAA-20 | RONDONÓPOLIS | MATO GROSSO | Brasil | 5107602 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| d43e78b3-b9c4-3413-8d10-37fb18eca8c1 | -15.79286 | -52.19001 | 2025-09-16 04:53:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 3.1 |
| d556f6a8-a174-3b54-9508-26dbe1b4dce4 | -15.77301 | -53.45475 | 2025-09-16 04:53:00 | NOAA-20 | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | 7.1 |
| bd8465d9-9d39-3cb2-b7c7-984bd84e3f05 | -15.77636 | -53.45536 | 2025-09-16 04:53:00 | NOAA-20 | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| fb9d01f4-97bd-3056-9ca2-904e7bfa491d | -17.73226 | -46.77452 | 2025-09-16 04:53:00 | NOAA-20 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 3906e24c-eb79-3be3-9df1-fc575dd22c6b | -16.01484 | -59.23618 | 2025-09-16 04:53:00 | NOAA-20 | PORTO ESPERIDIÃO | MATO GROSSO | Brasil | 5106828 | 51 | 33 | nan | nan | nan | Amazônia | 6.4 |
| 7fbcb390-f7a1-330e-a5ee-1cc7537be15b | -15.85986 | -59.38019 | 2025-09-16 04:53:00 | NOAA-20 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 3a4b1370-43b2-3533-b5d2-16c93c769050 | -15.87445 | -59.38807 | 2025-09-16 04:53:00 | NOAA-20 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 03c3cf7b-e81a-32ef-82aa-c58e202d4652 | -16.7001 | -54.96866 | 2025-09-16 04:53:00 | NOAA-20 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Cerrado | 3.5 |
| e8390c9a-61da-31e9-9ca2-ca26c4a1d425 | -15.7999 | -53.45917 | 2025-09-16 04:53:00 | NOAA-20 | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 67117742-db92-33e2-afc3-7915c3da1ca1 | -15.81 | -53.46076 | 2025-09-16 04:53:00 | NOAA-20 | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 651e36fc-5d07-34bc-9218-c402f111710b | -16.01222 | -59.25065 | 2025-09-16 04:53:00 | NOAA-20 | PORTO ESPERIDIÃO | MATO GROSSO | Brasil | 5106828 | 51 | 33 | nan | nan | nan | Amazônia | 3.7 |
| d314f4e7-dca7-3b2c-925b-ffb3991bbfbb | -15.86724 | -59.42775 | 2025-09-16 04:53:00 | NOAA-20 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| ca42a0b0-88e4-3551-9d6c-ac743ddab2b1 | -16.70737 | -54.94407 | 2025-09-16 04:53:00 | NOAA-20 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 3d782f53-485e-3afb-ad49-5bc1ea244ab5 | -15.7747 | -53.46637 | 2025-09-16 04:53:00 | NOAA-20 | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 5fa282f0-2624-39d8-825c-02cb3d28c7af | -15.78994 | -52.18539 | 2025-09-16 04:53:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 0e1918a4-1467-35dc-bf99-66e4f75b01f4 | -16.00016 | -59.42785 | 2025-09-16 04:53:00 | NOAA-20 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 3e975396-bdef-3f13-9c2a-f33783a6c033 | -16.714 | -54.94519 | 2025-09-16 04:53:00 | NOAA-20 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 3e9a201b-2544-3d99-9006-c429129e6f03 | -16.43275 | -45.68081 | 2025-09-16 04:53:00 | NOAA-20 | SÃO ROMÃO | MINAS GERAIS | Brasil | 3164209 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| b9d6d251-4e5e-31fb-80de-d7bb0d2d337b | -16.01867 | -59.23689 | 2025-09-16 04:53:00 | NOAA-20 | PORTO ESPERIDIÃO | MATO GROSSO | Brasil | 5106828 | 51 | 33 | nan | nan | nan | Amazônia | 6.4 |
| ea05f7ae-1d81-304c-89b2-ab00ad188f33 | -17.86535 | -44.44188 | 2025-09-16 04:53:00 | NOAA-20 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 2.3 |
| ac44dd26-0422-357e-a363-51363c0e6816 | -15.79654 | -53.45864 | 2025-09-16 04:53:00 | NOAA-20 | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 3b98aba2-7335-3e6a-8329-83fc77497bbd | -15.8229 | -53.46658 | 2025-09-16 04:53:00 | NOAA-20 | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | 2.6 |
| eeb2db30-1a62-328e-9992-750b6aabe7c5 | -15.82234 | -53.47029 | 2025-09-16 04:53:00 | NOAA-20 | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 6ade9aed-c01d-3399-aac6-e908c24d5d31 | -16.0571 | -59.42288 | 2025-09-16 04:53:00 | NOAA-20 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 72f04a79-7f49-3830-b870-4c5fa97fa052 | -16.42787 | -45.6767 | 2025-09-16 04:53:00 | NOAA-20 | SÃO ROMÃO | MINAS GERAIS | Brasil | 3164209 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| e38c8178-292f-3405-ae6e-c3cf29f1df30 | -15.86328 | -59.37855 | 2025-09-16 04:53:00 | NOAA-20 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 578d5eeb-c0c7-3f90-9c3b-b9e13e004c18 | -15.01277 | -55.34776 | 2025-09-16 04:53:00 | NOAA-20 | CHAPADA DOS GUIMARÃES | MATO GROSSO | Brasil | 5103007 | 51 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 4655c321-87ef-385d-8a64-b6717466ed22 | -16.51159 | -43.55455 | 2025-09-16 04:53:00 | NOAA-20 | FRANCISCO SÁ | MINAS GERAIS | Brasil | 3126703 | 31 | 33 | nan | nan | nan | Cerrado | 4.2 |
| eea71d71-a3ec-33c0-9fa3-5fdbdc73e8d7 | -15.85771 | -59.38741 | 2025-09-16 04:53:00 | NOAA-20 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| b99acfc1-1efd-3be8-8564-0d91b51d432d | -15.83386 | -59.40899 | 2025-09-16 04:53:00 | NOAA-20 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 6d2cc24b-429a-36ef-b5fa-8566adcd8749 | -16.43313 | -45.67759 | 2025-09-16 04:53:00 | NOAA-20 | SÃO ROMÃO | MINAS GERAIS | Brasil | 3164209 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 50c159ef-672c-384e-9f4e-48ffc9852aac | -15.80327 | -53.4597 | 2025-09-16 04:53:00 | NOAA-20 | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 4ec1cf99-5fab-3f8f-91b4-1a1b526a3d41 | -15.77748 | -53.44794 | 2025-09-16 04:53:00 | NOAA-20 | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 27ab84bb-908e-3495-be22-125f56a9d938 | -15.87059 | -59.38727 | 2025-09-16 04:53:00 | NOAA-20 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| b770f9c6-db86-3408-8ed1-bcd671e6b07c | -16.02849 | -59.44866 | 2025-09-16 04:53:00 | NOAA-20 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 5ff4def3-bd64-3ef3-97d3-b840bee674e8 | -15.84253 | -53.47349 | 2025-09-16 04:53:00 | NOAA-20 | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| d57dd000-db94-33d6-be17-3c97882a8e0c | -17.07539 | -45.82629 | 2025-09-16 04:53:00 | NOAA-20 | BRASILÂNDIA DE MINAS | MINAS GERAIS | Brasil | 3108552 | 31 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 18df7a54-afbb-3f7a-bcad-d4cf5e83a581 | -15.81954 | -53.46604 | 2025-09-16 04:53:00 | NOAA-20 | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| f1c6d81a-9422-391d-a41f-06849b5f9e30 | -17.7324 | -46.77602 | 2025-09-16 04:53:00 | NOAA-20 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| aacf35a0-b8c7-337d-9de5-61eea0a480cb | -15.80329 | -53.5277 | 2025-09-16 04:53:00 | NOAA-20 | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 111e9ef9-f98b-3298-a565-1d170ef76dad | -17.30533 | -40.67951 | 2025-09-16 04:53:00 | NOAA-20 | UMBURATIBA | MINAS GERAIS | Brasil | 3170305 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| 05ef7d3e-7776-3526-9b47-599d10724898 | -15.82514 | -53.47454 | 2025-09-16 04:53:00 | NOAA-20 | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 5dc45d2c-5e64-324f-82b9-418f4d979253 | -17.08142 | -45.82705 | 2025-09-16 04:53:00 | NOAA-20 | BRASILÂNDIA DE MINAS | MINAS GERAIS | Brasil | 3108552 | 31 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 72a0bc8a-1349-34b0-92a9-7b2bfff41cfb | -17.08068 | -45.82686 | 2025-09-16 04:53:00 | NOAA-20 | BRASILÂNDIA DE MINAS | MINAS GERAIS | Brasil | 3108552 | 31 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 23f97706-b1f0-3966-a5fd-c8bdb41bb092 | -15.85856 | -59.38258 | 2025-09-16 04:53:00 | NOAA-20 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 6cf7e5d5-f987-368a-874a-3a7af54e086e | -16.01013 | -59.24029 | 2025-09-16 04:53:00 | NOAA-20 | PORTO ESPERIDIÃO | MATO GROSSO | Brasil | 5106828 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 5f464efc-e2ab-371e-9340-317babdd3986 | -18.01402 | -43.93584 | 2025-09-16 04:53:00 | NOAA-20 | BUENÓPOLIS | MINAS GERAIS | Brasil | 3109204 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| d3c93540-2214-318d-aa76-29512eb73d8c | -16.47864 | -55.10055 | 2025-09-16 04:53:00 | NOAA-20 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 20.2 |
| 994878bd-60eb-3133-97d1-f5a48859a0ee | -15.8285 | -53.47508 | 2025-09-16 04:53:00 | NOAA-20 | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | 5.4 |
| f0f2a145-9067-3d77-ac73-24e5a81cd9d3 | -16.70616 | -54.97338 | 2025-09-16 04:53:00 | NOAA-20 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 1eb229a2-dc58-3454-9bc2-b501eae3cfc7 | -16.00451 | -59.2494 | 2025-09-16 04:53:00 | NOAA-20 | PORTO ESPERIDIÃO | MATO GROSSO | Brasil | 5106828 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 9852fb8e-dc73-38bb-bd73-63526ad2def0 | -17.72739 | -46.77555 | 2025-09-16 04:53:00 | NOAA-20 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| fb69651f-e5cf-366b-b81d-5451d0a1fa21 | -15.78925 | -53.43846 | 2025-09-16 04:53:00 | NOAA-20 | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 3e5aec02-b044-3823-9056-353041bcc226 | -15.99444 | -59.2516 | 2025-09-16 04:53:00 | NOAA-20 | PORTO ESPERIDIÃO | MATO GROSSO | Brasil | 5106828 | 51 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 8b96a53d-b5b7-3e51-b19e-ae52c43f0419 | -17.86563 | -44.4439 | 2025-09-16 04:53:00 | NOAA-20 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 3.4 |
| ca094448-2a0a-3fe7-a5d1-6bfdca6f8ae3 | -16.0532 | -59.42229 | 2025-09-16 04:53:00 | NOAA-20 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 9bbea2a5-bc26-3df9-93b5-6080939ae258 | -16.0054 | -59.2445 | 2025-09-16 04:53:00 | NOAA-20 | PORTO ESPERIDIÃO | MATO GROSSO | Brasil | 5106828 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| e18e2aa5-68d5-3540-bcae-09f85be3122f | -17.72441 | -47.94335 | 2025-09-16 04:53:00 | NOAA-20 | IPAMERI | GOIÁS | Brasil | 5210109 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 61a19d0f-706a-3c8e-928b-58f972aaeff1 | -18.01451 | -43.93074 | 2025-09-16 04:53:00 | NOAA-20 | BUENÓPOLIS | MINAS GERAIS | Brasil | 3109204 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 67998da7-e294-3e03-8e7d-7b3fec4931c1 | -15.99123 | -59.257 | 2025-09-16 04:53:00 | NOAA-20 | PORTO ESPERIDIÃO | MATO GROSSO | Brasil | 5106828 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 8a40bd02-7205-31ce-8bbd-fb930a05141e | -15.78869 | -53.4422 | 2025-09-16 04:53:00 | NOAA-20 | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 058b0fa9-e9e8-3482-8195-f6e4364d487d | -16.5889 | -42.9118 | 2025-09-16 04:53:00 | NOAA-20 | GRÃO MOGOL | MINAS GERAIS | Brasil | 3127800 | 31 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 0bd6da90-5966-3623-b414-f1448d8a41b4 | -17.73308 | -46.76994 | 2025-09-16 04:53:00 | NOAA-20 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 2.5 |


[Clique aqui para ver as próximas entradas](README79.md)
