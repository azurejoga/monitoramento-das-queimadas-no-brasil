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

## Dados Diários - Página 56

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 6371fcae-0621-3a8e-9ed9-645614c7456c | -6.54891 | -45.83242 | 2025-10-04 04:12:00 | NOAA-20 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| dc12f901-4d24-32ff-bd92-dd2ca5b4aa58 | -6.66788 | -42.8235 | 2025-10-04 04:12:00 | NOAA-20 | FRANCISCO AYRES | PIAUÍ | Brasil | 2204105 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 741bfa8b-6c9b-3037-b3ad-2f67b5e9b8c2 | -5.83739 | -42.85517 | 2025-10-04 04:12:00 | NOAA-20 | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| b4485702-db7e-3a63-8ae3-c58d3db7d1cd | -6.61718 | -44.29636 | 2025-10-04 04:12:00 | NOAA-20 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 033d5dd9-9e99-3b64-9f4f-adade0d88ff4 | -7.54927 | -42.3982 | 2025-10-04 04:12:00 | NOAA-20 | SÃO MIGUEL DO FIDALGO | PIAUÍ | Brasil | 2210391 | 22 | 33 | nan | nan | nan | Caatinga | 3.5 |
| 1e9f2173-1a75-3996-80b0-775442e9a3db | -4.61326 | -46.46175 | 2025-10-04 04:12:00 | NOAA-20 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 237dd3c1-7a5a-3e2e-92ad-483101747c2f | -4.89326 | -49.96291 | 2025-10-04 04:12:00 | NOAA-20 | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 1cc5ad2e-fed7-360f-ba05-6c3d68c92fb0 | -6.30743 | -46.33094 | 2025-10-04 04:12:00 | NOAA-20 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| b57ac90f-9366-3691-a51f-1a802a43a5fa | -6.13986 | -44.86248 | 2025-10-04 04:12:00 | NOAA-20 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 4f15cf8d-d348-3e62-92c7-8025fd407504 | -5.83194 | -42.88968 | 2025-10-04 04:12:00 | NOAA-20 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 41d6b370-9df8-364b-aae3-b0281eeb01de | -3.98701 | -41.77094 | 2025-10-04 04:12:00 | NOAA-20 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 7085c941-8f9f-304a-8ca4-aec93d42f12f | -5.95709 | -43.4948 | 2025-10-04 04:12:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 16363197-4cb6-36cf-bf17-b80c05b2ebe9 | -7.56035 | -42.39273 | 2025-10-04 04:12:00 | NOAA-20 | SÃO MIGUEL DO FIDALGO | PIAUÍ | Brasil | 2210391 | 22 | 33 | nan | nan | nan | Caatinga | 3.5 |
| 6ed0864c-6878-308b-b5b3-dfdc5b0b6a95 | -1.13082 | -47.80454 | 2025-10-04 04:12:00 | NOAA-20 | SÃO FRANCISCO DO PARÁ | PARÁ | Brasil | 1507409 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| d2124bd1-792f-34df-8dc7-a4f4a92110eb | -7.4806 | -43.03357 | 2025-10-04 04:12:00 | NOAA-20 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 54af3a0c-5c3f-3b3e-959b-af3870defbc7 | -7.00045 | -42.30593 | 2025-10-04 04:12:00 | NOAA-20 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 9e05fa37-e250-3396-86f5-dc6c9ee294ac | -6.99556 | -44.20712 | 2025-10-04 04:12:00 | NOAA-20 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| a1ec6e44-6c5c-3692-8966-905649b1629d | -4.44593 | -43.25498 | 2025-10-04 04:12:00 | NOAA-20 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 957fd001-982d-3d7b-88f3-69ea722f6699 | -6.32209 | -43.25024 | 2025-10-04 04:12:00 | NOAA-20 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 509f9d79-b532-308e-b8ab-1275d1eeb63c | -5.52517 | -44.38923 | 2025-10-04 04:12:00 | NOAA-20 | SÃO DOMINGOS DO MARANHÃO | MARANHÃO | Brasil | 2110708 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| eb568f5d-023c-3364-a686-18e19321b85a | -2.89541 | -50.7339 | 2025-10-04 04:12:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 9b1b6b3e-17a7-30af-8e89-a4188b7121db | -4.95246 | -45.06551 | 2025-10-04 04:12:00 | NOAA-20 | SÃO ROBERTO | MARANHÃO | Brasil | 2111672 | 21 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 5acf6bbb-1ed1-3ef8-ad23-b8d77005b791 | -7.37129 | -39.1983 | 2025-10-04 04:12:00 | NOAA-20 | MISSÃO VELHA | CEARÁ | Brasil | 2308401 | 23 | 33 | nan | nan | nan | Caatinga | 5.3 |
| 15e4adfa-a65d-3f6f-81f0-46cc3f0ac927 | -6.22261 | -44.28077 | 2025-10-04 04:12:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 329911bf-e4f3-3650-a507-93bc1f63868f | -6.55527 | -44.1549 | 2025-10-04 04:12:00 | NOAA-20 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| ec44d860-f2a1-376b-8a96-e709fbd2c05c | -5.26113 | -39.26082 | 2025-10-04 04:12:00 | NOAA-20 | QUIXERAMOBIM | CEARÁ | Brasil | 2311405 | 23 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 5d8b730a-2f0c-3bd6-9ded-8f847196ac49 | -6.43977 | -44.45563 | 2025-10-04 04:12:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| dff1a6f8-7257-3351-9a70-87febebd63bc | -5.13756 | -38.09149 | 2025-10-04 04:12:00 | NOAA-20 | LIMOEIRO DO NORTE | CEARÁ | Brasil | 2307601 | 23 | 33 | nan | nan | nan | Caatinga | 0.5 |
| e3ab8684-06d7-31ef-b43f-73b012e6fd9e | -5.77073 | -45.75962 | 2025-10-04 04:12:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 470d9e92-0f8d-33ac-8a9e-f70eb625fc68 | -4.60949 | -46.46119 | 2025-10-04 04:12:00 | NOAA-20 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |
| a538cd24-edce-3a83-88f2-6327a2ccd7cc | -5.46429 | -43.15325 | 2025-10-04 04:12:00 | NOAA-20 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 627a8f7e-f872-336a-b4f2-f6c3f7a733c7 | -5.81817 | -42.89104 | 2025-10-04 04:12:00 | NOAA-20 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 22e205ea-c2a8-3699-a942-f24b0fbf0ecc | -2.92167 | -48.31134 | 2025-10-04 04:12:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 0c51ebde-6e86-30ea-b6c6-db8666b936d9 | -5.66561 | -42.71848 | 2025-10-04 04:12:00 | NOAA-20 | MONSENHOR GIL | PIAUÍ | Brasil | 2206407 | 22 | 33 | nan | nan | nan | Caatinga | 10.9 |
| 079b1c1e-6585-3583-938c-8f8bc083e7be | -6.72288 | -44.14512 | 2025-10-04 04:12:00 | NOAA-20 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| e65ff42e-7895-3843-8c7d-ecfa44e93c60 | -6.49255 | -42.03656 | 2025-10-04 04:12:00 | NOAA-20 | NOVO ORIENTE DO PIAUÍ | PIAUÍ | Brasil | 2206902 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 966c8e04-a2e1-3099-939f-57a4eab5ff8a | -5.80351 | -42.72607 | 2025-10-04 04:12:00 | NOAA-20 | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 01d56755-436a-3447-a4f2-d6575ac70792 | -6.70824 | -42.15606 | 2025-10-04 04:12:00 | NOAA-20 | TANQUE DO PIAUÍ | PIAUÍ | Brasil | 2210979 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| a0a527d2-defa-3c20-b5c4-2408bfb245d7 | -2.89129 | -50.72696 | 2025-10-04 04:12:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| b8f97646-3815-3dda-8a53-89d5cc1ccaf9 | -7.71506 | -42.60033 | 2025-10-04 04:12:00 | NOAA-20 | RIBEIRA DO PIAUÍ | PIAUÍ | Brasil | 2208874 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 5d16071a-7057-3ad6-ab89-54b4c007b847 | -5.69232 | -42.84996 | 2025-10-04 04:12:00 | NOAA-20 | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 2359561c-192c-3795-a76d-17d1c14d91d3 | -6.97096 | -44.40397 | 2025-10-04 04:12:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| ae9e3fbb-527d-3c69-813c-8a6eb0ff1813 | -5.68788 | -42.83512 | 2025-10-04 04:12:00 | NOAA-20 | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 611b318d-d960-3ff3-8c07-cfe340451b5a | -5.76316 | -42.93897 | 2025-10-04 04:12:00 | NOAA-20 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 24c421c5-2e06-3784-a137-d3f023b751b7 | -6.59202 | -44.62465 | 2025-10-04 04:12:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 4.5 |
| ea75ce17-1faa-3e4b-ae81-87aeda7d915c | -5.83793 | -42.85172 | 2025-10-04 04:12:00 | NOAA-20 | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| dcc0521a-e2f2-3d43-ad87-68c1e39da065 | -6.74689 | -44.59706 | 2025-10-04 04:12:00 | NOAA-20 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 99228088-ca7d-330c-8903-c948dc4c7db1 | -5.23445 | -43.74563 | 2025-10-04 04:12:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 652a5333-6410-3ff1-af5b-8d41a44e6a5a | -5.85077 | -42.20855 | 2025-10-04 04:12:00 | NOAA-20 | SÃO MIGUEL DA BAIXA GRANDE | PIAUÍ | Brasil | 2210383 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 017ea1f3-3195-37ee-95a0-4ae41cc23d63 | -6.05776 | -41.23041 | 2025-10-04 04:12:00 | NOAA-20 | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 4dcb4fb1-bc0c-3872-8d2f-5e6cf6efb2bb | -7.34971 | -44.34721 | 2025-10-04 04:12:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| be96237a-e9c2-3d17-a510-ea0aa51ac7a1 | -5.24302 | -45.55103 | 2025-10-04 04:12:00 | NOAA-20 | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| c7d5a41c-acb2-3342-acb0-9dafe33eaa27 | -6.99758 | -42.80099 | 2025-10-04 04:12:00 | NOAA-20 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 6071ef39-04fc-3174-bdc8-7b0991d25375 | -3.86112 | -51.813 | 2025-10-04 04:12:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 7ceebd8e-1d9a-30c2-b230-eda9108f4ed4 | -5.77946 | -45.77356 | 2025-10-04 04:12:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 705ebe4a-97c0-3dce-9605-7dad4343ac9d | -4.60483 | -43.15223 | 2025-10-04 04:12:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| acce4bfc-745c-391c-b1bf-579514c0c4ea | -5.79226 | -42.88343 | 2025-10-04 04:12:00 | NOAA-20 | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 2.7 |
| dafe0c1a-8949-3fe9-a1b7-22828a43d64c | -6.24186 | -44.22498 | 2025-10-04 04:12:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 723a08e9-d623-3c3c-8f01-942cf976d333 | -7.00412 | -46.99873 | 2025-10-04 04:12:00 | NOAA-20 | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| fa54d99b-2928-3ac9-bd65-959f74101aa9 | -4.25458 | -48.56682 | 2025-10-04 04:12:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 002d6bc7-20f4-3402-af03-a0e54bd824f3 | -6.76637 | -44.80569 | 2025-10-04 04:12:00 | NOAA-20 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 6fd3eeab-8985-3747-b6e3-8c7e2c54c0c3 | -5.3058 | -45.56386 | 2025-10-04 04:12:00 | NOAA-20 | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| b82280ee-c1f6-3805-81cf-a9f71f2b494a | -7.70227 | -42.57328 | 2025-10-04 04:12:00 | NOAA-20 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 1d94c3cc-c013-3853-85dd-9978542ea6ba | -3.66069 | -50.27163 | 2025-10-04 04:12:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 042a7704-e40f-3de1-a556-75a3580cf839 | -5.93495 | -43.31301 | 2025-10-04 04:12:00 | NOAA-20 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 0a8c77e1-ae0d-36ac-a59a-5382ef264bab | -7.78003 | -42.59621 | 2025-10-04 04:12:00 | NOAA-20 | SOCORRO DO PIAUÍ | PIAUÍ | Brasil | 2210904 | 22 | 33 | nan | nan | nan | Caatinga | 5.1 |
| 7e018388-a386-3e9b-bae5-cac16976eda6 | -7.74627 | -42.5945 | 2025-10-04 04:12:00 | NOAA-20 | SOCORRO DO PIAUÍ | PIAUÍ | Brasil | 2210904 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 0b138345-6ecd-3953-b213-97f2f8a3abc8 | -2.89591 | -50.73086 | 2025-10-04 04:12:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 55b965c8-e614-3e8b-a9d9-e0aaf6832fdd | -4.26158 | -48.55095 | 2025-10-04 04:12:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 50b7e25d-7319-375c-b9ce-51b9abb257b9 | -5.89765 | -42.53891 | 2025-10-04 04:12:00 | NOAA-20 | OLHO D'ÁGUA DO PIAUÍ | PIAUÍ | Brasil | 2207108 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 60df30ed-7f68-382e-a2c3-29c4cb44dae3 | -5.97 | -45.89387 | 2025-10-04 04:12:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 7138550d-35b4-3bd2-8340-60c00dff37ca | -4.43541 | -43.25689 | 2025-10-04 04:12:00 | NOAA-20 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| ae4d0a30-23cc-3a20-8e9b-e0e840fd7fcf | -7.78996 | -42.57626 | 2025-10-04 04:12:00 | NOAA-20 | SOCORRO DO PIAUÍ | PIAUÍ | Brasil | 2210904 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 9cd6d911-497a-30fd-85bc-8f3cd06fce01 | -6.12637 | -45.92987 | 2025-10-04 04:12:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| e4ce7596-bc54-3304-a37e-0af8954eb1a4 | -6.70123 | -42.67614 | 2025-10-04 04:12:00 | NOAA-20 | FRANCISCO AYRES | PIAUÍ | Brasil | 2204105 | 22 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 19275dd0-22ac-36d0-8ee6-ad3634d0d12c | -7.0577 | -42.78561 | 2025-10-04 04:12:00 | NOAA-20 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| e1ba6440-550b-3a10-8d5b-b890662fa0b2 | -6.69325 | -42.83459 | 2025-10-04 04:12:00 | NOAA-20 | FRANCISCO AYRES | PIAUÍ | Brasil | 2204105 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 1e3c4870-2a69-3639-961d-44faa7f43d4c | -5.32573 | -43.53379 | 2025-10-04 04:12:00 | NOAA-20 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| b107851d-846b-3b00-956e-152f1e9524c4 | -6.46029 | -44.57387 | 2025-10-04 04:12:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 7.2 |
| 833df093-bd42-39b2-80d1-adc15b5eea2b | -5.94031 | -42.89238 | 2025-10-04 04:12:00 | NOAA-20 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 3.2 |
| a59bf39f-918e-3ff1-8ab3-68caacc8506f | -6.99606 | -42.33395 | 2025-10-04 04:12:00 | NOAA-20 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| d510e9a9-7094-3bf1-99ae-c5de3c1758e8 | -4.45145 | -43.24158 | 2025-10-04 04:12:00 | NOAA-20 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 3cf4429e-0c3f-3ee8-9b4b-1160660bbe07 | -7.77949 | -42.59971 | 2025-10-04 04:12:00 | NOAA-20 | RIBEIRA DO PIAUÍ | PIAUÍ | Brasil | 2208874 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 56c4cf18-3806-3b15-ba4d-5d720d95e601 | -5.7821 | -44.90636 | 2025-10-04 04:12:00 | NOAA-20 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 89e686dd-dea4-370a-a4d4-f89094358000 | -6.17708 | -43.92828 | 2025-10-04 04:12:00 | NOAA-20 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 73dec4c3-609c-3ea1-8a41-c219a963de07 | -7.31704 | -47.28809 | 2025-10-04 04:12:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 7c104a8e-95eb-3f73-a62a-449b48fe2de5 | -7.76789 | -42.60861 | 2025-10-04 04:12:00 | NOAA-20 | RIBEIRA DO PIAUÍ | PIAUÍ | Brasil | 2208874 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 2ecb13a0-5e73-3f2d-b336-13789c1f9e0a | -4.69621 | -48.17078 | 2025-10-04 04:12:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 0307bb29-51fe-36e2-95b8-d41060e3de0c | -6.07521 | -42.51001 | 2025-10-04 04:12:00 | NOAA-20 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 26.9 |
| 3aa9c960-cee7-30ff-8fcc-fe95a4de4910 | -6.71933 | -42.80005 | 2025-10-04 04:12:00 | NOAA-20 | FRANCISCO AYRES | PIAUÍ | Brasil | 2204105 | 22 | 33 | nan | nan | nan | Caatinga | 0.4 |
| 2f7f3de7-c821-354e-8f21-ba308898a959 | -4.49867 | -46.37989 | 2025-10-04 04:12:00 | NOAA-20 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e49d5f2b-832d-3c4c-8dc9-f5ec19cd16e0 | -5.83779 | -42.87625 | 2025-10-04 04:12:00 | NOAA-20 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 97a9f478-293a-3f33-8c2b-28c802f241f3 | -6.35706 | -41.62326 | 2025-10-04 04:12:00 | NOAA-20 | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| af37e716-bb8c-36ec-b06e-4c51da8fd4dc | -5.68956 | -42.84599 | 2025-10-04 04:12:00 | NOAA-20 | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 10.1 |
| 3317cfbe-86d4-3dfc-b037-e33d50c2f30c | -7.75051 | -42.52341 | 2025-10-04 04:12:00 | NOAA-20 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 3.3 |
| 1a41db40-e323-3dca-8da6-ac55bec88409 | -6.10012 | -43.44972 | 2025-10-04 04:12:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 42a5da85-4a43-300d-9da1-3ac2b4f2376c | -5.95543 | -42.94786 | 2025-10-04 04:12:00 | NOAA-20 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 3.9 |
| d994954c-0421-3fdb-8182-a28417c611dd | -6.65076 | -42.80306 | 2025-10-04 04:12:00 | NOAA-20 | FRANCISCO AYRES | PIAUÍ | Brasil | 2204105 | 22 | 33 | nan | nan | nan | Caatinga | 4.1 |
| d83d8353-1710-3153-b2e9-94ae342a8bf0 | -6.71525 | -42.80257 | 2025-10-04 04:12:00 | NOAA-20 | FRANCISCO AYRES | PIAUÍ | Brasil | 2204105 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| c2061e74-89c3-3a10-9dc9-772245e8654f | -7.75389 | -42.54545 | 2025-10-04 04:12:00 | NOAA-20 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |


[Clique aqui para ver as próximas entradas](README57.md)
