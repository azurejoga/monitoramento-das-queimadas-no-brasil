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

## Dados Diários - Página 17

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 20630001-6bb2-30de-a72b-efbd67a45b4e | -4.30199 | -48.60172 | 2025-11-26 04:21:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| be8c5078-78a4-3ef9-a185-038774b68459 | -9.12083 | -44.44025 | 2025-11-26 04:21:00 | NOAA-20 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| df11fbb4-2546-3991-a975-53878ad43e33 | -8.06728 | -43.11023 | 2025-11-26 04:21:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 2ee583d3-f6f0-3f5e-8a3b-b01ce0aa9d70 | -4.65625 | -43.97607 | 2025-11-26 04:21:00 | NOAA-20 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 11b8a573-3640-37b4-941e-fd90306e6e65 | -6.57219 | -47.89581 | 2025-11-26 04:21:00 | NOAA-20 | DARCINÓPOLIS | TOCANTINS | Brasil | 1706506 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| fd2be14f-5c05-39bd-aa04-eb1e50f823f7 | -3.42838 | -39.16776 | 2025-11-26 04:21:00 | NOAA-20 | PARAIPABA | CEARÁ | Brasil | 2310258 | 23 | 33 | nan | nan | nan | Caatinga | 1.1 |
| d30fedc9-3553-3b1a-b977-fa2ced731430 | -6.56726 | -47.90349 | 2025-11-26 04:21:00 | NOAA-20 | DARCINÓPOLIS | TOCANTINS | Brasil | 1706506 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 0f4874f2-14c7-34d0-9cec-7e856192f3b8 | -6.59624 | -44.3201 | 2025-11-26 04:21:00 | NOAA-20 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| a88bb8ab-1bba-361e-8422-dd67a2ec2c45 | -4.95721 | -42.7445 | 2025-11-26 04:21:00 | NOAA-20 | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 4f2aeea4-bd17-3c75-8e1a-ba9bd956617b | -7.1806 | -45.50239 | 2025-11-26 04:21:00 | NOAA-20 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 59a5cf99-bf3b-34fe-a95f-397a76b28f30 | -6.2523 | -46.79008 | 2025-11-26 04:21:00 | NOAA-20 | SÃO JOÃO DO PARAÍSO | MARANHÃO | Brasil | 2111052 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 73ca89b1-df51-3e26-8424-5c089d9afdac | -4.93987 | -41.15007 | 2025-11-26 04:21:00 | NOAA-20 | PORANGA | CEARÁ | Brasil | 2311009 | 23 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 7ff8b930-3249-3a0a-a242-f7a7cbcea2ea | -6.48543 | -38.83083 | 2025-11-26 04:21:00 | NOAA-20 | ICÓ | CEARÁ | Brasil | 2305407 | 23 | 33 | nan | nan | nan | Caatinga | 1.8 |
| f9358770-09dc-333a-869b-3aee12bed8bf | -5.57305 | -46.28434 | 2025-11-26 04:21:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| a4bce105-6983-3fae-a5b8-93e84fa55fec | -5.76272 | -46.43496 | 2025-11-26 04:21:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 1c1519b0-3cde-3d42-9596-6029cdd31c6e | -5.03336 | -43.26278 | 2025-11-26 04:21:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| f3c34b18-c5c2-3273-8fa0-2b339076f98d | -6.5072 | -44.30233 | 2025-11-26 04:21:00 | NOAA-20 | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 6b6f0aee-4e87-3392-9b6c-8815e0bd21f7 | -8.0427 | -43.11029 | 2025-11-26 04:21:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 2e9f6492-acd5-348f-979b-bfaddafcce5f | -5.37155 | -43.72589 | 2025-11-26 04:21:00 | NOAA-20 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 77240550-e03a-3563-824b-d6abbdf22c8a | -2.49704 | -47.8189 | 2025-11-26 04:21:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 81083dc2-645b-32d9-95b7-37855781558a | -8.04384 | -43.12581 | 2025-11-26 04:21:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 5.7 |
| ab1a04ae-1027-39c9-a401-5af9a8365ca2 | -4.70918 | -43.98434 | 2025-11-26 04:21:00 | NOAA-20 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 5.7 |
| aee4e3bd-e69d-340a-b5c0-0aacb7b6db5b | -8.05755 | -43.12793 | 2025-11-26 04:21:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 10.3 |
| 79ef5dff-3f37-302c-83d4-47516645c0b5 | -3.2205 | -50.56797 | 2025-11-26 04:21:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b534829e-8756-3d21-9889-a6ad2ef214bd | -3.21723 | -50.17136 | 2025-11-26 04:21:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| adbca57b-6084-328e-954a-e6ebb12cd3e7 | -6.30566 | -43.78889 | 2025-11-26 04:21:00 | NOAA-20 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 10.3 |
| c8113d96-d231-32c8-b76f-ccf35d0ad53e | -2.49932 | -47.82863 | 2025-11-26 04:21:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 37cde6d6-f0da-37ec-948d-0bec870f8353 | -2.73482 | -49.46235 | 2025-11-26 04:21:00 | NOAA-20 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 2cdfa39f-a677-3add-b1e4-3f7514279484 | -7.52267 | -43.8687 | 2025-11-26 04:21:00 | NOAA-20 | BERTOLÍNIA | PIAUÍ | Brasil | 2201705 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 6e4ea31e-2815-35e4-9ca1-30f3c0019f0c | -3.71833 | -43.22161 | 2025-11-26 04:21:00 | NOAA-20 | MATA ROMA | MARANHÃO | Brasil | 2106409 | 21 | 33 | nan | nan | nan | Cerrado | 0.3 |
| 98d63e32-37a8-3868-86b5-4cd704a795a7 | -3.29944 | -53.04811 | 2025-11-26 04:21:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| efe566dd-1bd8-3187-af49-fa57574523a4 | -5.06198 | -46.81868 | 2025-11-26 04:21:00 | NOAA-20 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| e445397e-91b8-3e24-bb61-41836babe189 | -2.75028 | -51.90138 | 2025-11-26 04:21:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| fbba4784-ec1f-3467-b3a7-52d866027314 | -4.41153 | -42.91627 | 2025-11-26 04:21:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| ad630570-5272-3345-b531-c064a33290ed | -4.17328 | -43.71955 | 2025-11-26 04:21:00 | NOAA-20 | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 18.4 |
| 1e150847-cb98-3027-a6ee-5f686ce9153e | -3.32179 | -49.71981 | 2025-11-26 04:21:00 | NOAA-20 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 87448865-c5b8-35f3-869d-4e21df628271 | -2.86681 | -51.7865 | 2025-11-26 04:21:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 72075230-4da9-3b8f-a02b-9e0e98d2d341 | -4.27388 | -45.12568 | 2025-11-26 04:21:00 | NOAA-20 | OLHO D'ÁGUA DAS CUNHÃS | MARANHÃO | Brasil | 2107407 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 9fbb0cf2-70c5-342a-b9af-0877910b8cf9 | -4.55477 | -49.69421 | 2025-11-26 04:21:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| bf04c7eb-8067-3e31-8157-673a95d5a855 | -7.19941 | -45.91798 | 2025-11-26 04:21:00 | NOAA-20 | FORTALEZA DOS NOGUEIRAS | MARANHÃO | Brasil | 2104107 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| ea92c02d-2dfd-333e-9ba5-0e074771893d | -6.11286 | -42.95248 | 2025-11-26 04:21:00 | NOAA-20 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| a36d2096-4fbe-3784-aef7-9ae4bc428de8 | -2.93555 | -48.22834 | 2025-11-26 04:21:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 8.2 |
| e886c754-9ca5-3602-8feb-6ed8ef70c1fd | -6.30457 | -43.79588 | 2025-11-26 04:21:00 | NOAA-20 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 220b2cc1-4bc2-37d3-8339-a3384fe860b6 | -8.0587 | -43.12043 | 2025-11-26 04:21:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 19.2 |
| cea0a8ff-78b6-3419-aaea-1c7b4bf1ba10 | -6.25997 | -47.04869 | 2025-11-26 04:21:00 | NOAA-20 | PORTO FRANCO | MARANHÃO | Brasil | 2109007 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 6a153b89-486f-338a-ace1-f7cd94e3daa9 | -3.25371 | -50.68922 | 2025-11-26 04:21:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| abbebbae-4fed-3aa5-95c9-647cdeebf671 | -6.95526 | -39.13558 | 2025-11-26 04:21:00 | NOAA-20 | CARIRIAÇU | CEARÁ | Brasil | 2303204 | 23 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 4fc54a6b-02bd-3d38-9186-03ec60355a34 | -10.20812 | -36.37046 | 2025-11-26 04:21:00 | NOAA-20 | PENEDO | ALAGOAS | Brasil | 2706703 | 27 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| 6ccbcdb7-0fe3-354f-b0a1-d3dd43ebd8d9 | -4.55497 | -43.30091 | 2025-11-26 04:21:00 | NOAA-20 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 40292305-fc21-35c7-aaf3-5c0db0ee7af5 | -5.10947 | -44.26994 | 2025-11-26 04:21:00 | NOAA-20 | GONÇALVES DIAS | MARANHÃO | Brasil | 2104404 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 2689fb3e-9ff0-3134-bb29-590b58e49b82 | -3.44686 | -50.55379 | 2025-11-26 04:21:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 77e56c0e-01af-344e-a8b7-e21e03eac60b | -6.7428 | -39.05356 | 2025-11-26 04:21:00 | NOAA-20 | LAVRAS DA MANGABEIRA | CEARÁ | Brasil | 2307502 | 23 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 876868e9-6f9d-38bc-8ae1-a0a300d37b10 | -4.92855 | -49.15125 | 2025-11-26 04:21:00 | NOAA-20 | NOVA IPIXUNA | PARÁ | Brasil | 1504976 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 6a9722cf-eba9-3c25-9060-b338af50b159 | -4.896 | -43.7474 | 2025-11-26 04:21:00 | NOAA-20 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| ca9f0eca-9a90-3510-97b7-b201bab86efb | -2.82557 | -49.12738 | 2025-11-26 04:21:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 70b019e3-f198-3fe8-b8ba-ec8daed8ed90 | -9.09522 | -44.43249 | 2025-11-26 04:21:00 | NOAA-20 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| bed83892-bfc3-36ad-b48e-4ad47b10416c | -4.17165 | -49.87693 | 2025-11-26 04:21:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 8.0 |
| b1665e66-7853-3a0d-9dfe-1514ed5ade49 | -3.47168 | -43.42884 | 2025-11-26 04:21:00 | NOAA-20 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 4acacdf2-771c-3fbc-9312-0519a3357fc6 | -7.75067 | -44.19037 | 2025-11-26 04:21:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 8f453cf5-fccb-3f37-8cb2-22e087359a4e | -5.38919 | -50.48717 | 2025-11-26 04:21:00 | NOAA-20 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 00546c11-e9bb-38aa-ac90-ad2e7a5d40ce | -4.64959 | -47.94378 | 2025-11-26 04:21:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 5c0c04c3-6b70-3e39-a16d-71fa206b61ba | -4.41478 | -45.11572 | 2025-11-26 04:21:00 | NOAA-20 | BOM LUGAR | MARANHÃO | Brasil | 2102077 | 21 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 1f542cad-647d-37eb-9886-1572d0c58d15 | -4.7714 | -46.42392 | 2025-11-26 04:21:00 | NOAA-20 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 485a0d46-313f-39f9-a335-d1749d1e06ac | -2.54928 | -45.38743 | 2025-11-26 04:21:00 | NOAA-20 | PRESIDENTE SARNEY | MARANHÃO | Brasil | 2109270 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 56e8042d-7120-30b7-b2b2-72d0e66156e7 | -5.60431 | -46.26321 | 2025-11-26 04:21:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| a13757e1-cbb7-3bb2-ab63-4d19233867b2 | -2.93939 | -48.22897 | 2025-11-26 04:21:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| fe9433db-7e98-3728-8727-ea73db901f7d | -4.65798 | -48.47945 | 2025-11-26 04:21:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 991d60f8-a7a7-3d9c-83cd-61254881224d | -5.75397 | -45.11438 | 2025-11-26 04:21:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| da05cd87-69d3-3e62-bdef-b5104b6d1ece | -3.16485 | -51.43507 | 2025-11-26 04:21:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 34c43d85-6dfe-3aba-a7ad-2b57e6d1395c | -2.47314 | -48.23348 | 2025-11-26 04:21:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 7fbcc4d2-f28b-3cf5-adde-6c8b6c8137d1 | -5.38423 | -50.49052 | 2025-11-26 04:21:00 | NOAA-20 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 4bad8fea-6990-38c0-8727-9852fb74e891 | -6.75969 | -46.51678 | 2025-11-26 04:21:00 | NOAA-20 | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 4eb49d4d-b1d9-3d10-96c6-b170c58e6ea6 | -4.46031 | -45.40711 | 2025-11-26 04:21:00 | NOAA-20 | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Amazônia | 0.5 |
| adfa35b4-4ad4-33d5-bc2c-25aa75cab3df | -2.85387 | -45.23037 | 2025-11-26 04:21:00 | NOAA-20 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| af57d53a-874c-3d4a-b3cf-51e8e69d3631 | -4.66102 | -48.48471 | 2025-11-26 04:21:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 5ebccba2-95e9-3f85-89b0-d3fb5984b9c4 | -5.41903 | -45.29633 | 2025-11-26 04:21:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| dde3d7aa-3cba-3a71-9887-d1478033e54d | -5.6077 | -46.26379 | 2025-11-26 04:21:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 3e8d0457-09c1-3ab0-b1f4-698249f5318e | -2.49389 | -48.15321 | 2025-11-26 04:21:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| f03209da-a04d-31ab-8788-8a78a7eccd68 | -6.58232 | -47.90163 | 2025-11-26 04:21:00 | NOAA-20 | DARCINÓPOLIS | TOCANTINS | Brasil | 1706506 | 17 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 27fd94af-035d-39f5-8fe9-b6cb412fd9e3 | -4.90827 | -43.7991 | 2025-11-26 04:21:00 | NOAA-20 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 6a0aaa00-13e3-309f-b6be-139737edbae5 | -5.1166 | -42.79822 | 2025-11-26 04:21:00 | NOAA-20 | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Cerrado | 3.5 |
| bee875ea-d3ee-394a-9efa-05f65ae1e921 | -6.30178 | -43.79186 | 2025-11-26 04:21:00 | NOAA-20 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 8fce24c7-a19a-3561-8d68-f2ac04763b8f | -4.1722 | -43.72647 | 2025-11-26 04:21:00 | NOAA-20 | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 9bcb559f-f5ce-3123-8e8c-f46696e2e343 | -7.61378 | -42.98409 | 2025-11-26 04:21:00 | NOAA-20 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 18b3a5e5-e201-347e-b2e1-c4b6c4a9f173 | -5.03391 | -43.25924 | 2025-11-26 04:21:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 42b912b2-b0b3-303b-989c-5df40ce370c6 | -5.06599 | -49.87972 | 2025-11-26 04:21:00 | NOAA-20 | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 1dd2c646-0460-3120-8e8f-05f2056ffd79 | -3.45722 | -50.54637 | 2025-11-26 04:21:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 714f8cc9-8945-36b0-9a95-9f51e9b79baa | -2.87302 | -51.80978 | 2025-11-26 04:21:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| f6869465-3a89-39b1-98cf-76b27bd36df8 | -3.92001 | -49.22063 | 2025-11-26 04:21:00 | NOAA-20 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 19.7 |
| 57937dea-6972-327a-8725-37985981e42f | -3.69921 | -45.89382 | 2025-11-26 04:21:00 | NOAA-20 | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 75933786-540f-31f0-881e-07c80d233f4e | -3.28967 | -51.27324 | 2025-11-26 04:21:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 92c1f4ce-a400-3245-99bb-2c972487333f | -5.29298 | -43.64183 | 2025-11-26 04:21:00 | NOAA-20 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 5f80b17e-f9b9-3d11-a76a-58cd79daea33 | -2.6077 | -51.214 | 2025-11-26 04:21:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| ec700156-94fe-3ee0-b6f0-8bad2204adb1 | -4.72685 | -46.46354 | 2025-11-26 04:21:00 | NOAA-20 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 0.3 |
| cf174bf0-bcb4-33c5-b7ee-da17258c6e29 | -3.50288 | -50.27338 | 2025-11-26 04:21:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| de2bc57c-f3e5-3042-9894-7ffa90a3e686 | -6.81325 | -38.57553 | 2025-11-26 04:21:00 | NOAA-20 | CAJAZEIRAS | PARAÍBA | Brasil | 2503704 | 25 | 33 | nan | nan | nan | Caatinga | 2.1 |
| d9748804-5a21-3e81-8699-45fd53cc21d6 | -7.13645 | -43.85986 | 2025-11-26 04:21:00 | NOAA-20 | MARCOS PARENTE | PIAUÍ | Brasil | 2206001 | 22 | 33 | nan | nan | nan | Cerrado | 4.1 |
| be7007bd-2cbe-39b8-854f-634bdf06ffae | -4.17496 | -43.73044 | 2025-11-26 04:21:00 | NOAA-20 | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 11.0 |
| 175d80cf-2fec-3d4e-8dbf-67862eae0c3f | -3.82528 | -50.19734 | 2025-11-26 04:21:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 001ccae9-f197-30b6-b417-2d64baa7774e | -4.03228 | -49.09863 | 2025-11-26 04:21:00 | NOAA-20 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |


[Clique aqui para ver as próximas entradas](README18.md)
