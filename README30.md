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

## Dados Diários - Página 30

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| d6a52642-764b-39f1-b76e-290e0f78eabe | -2.3178 | -48.5717 | 2025-10-26 04:10:00 | GOES-19 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 30.2 |
| c1c6579d-8cec-35c0-9910-7d1081ff2dde | -13.5405 | -43.0077 | 2025-10-26 04:20:00 | GOES-19 | RIACHO DE SANTANA | BAHIA | Brasil | 2926400 | 29 | 33 | nan | nan | nan | Caatinga | 83.4 |
| 1437cc43-4209-33ac-9682-b3197da8e383 | -6.3864 | -45.7819 | 2025-10-26 04:20:00 | GOES-19 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 29.2 |
| d1f20035-734a-37a3-8715-320ed4acfcaf | -10.4065 | -45.3244 | 2025-10-26 04:20:00 | GOES-19 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 68.7 |
| 49bbcb2f-a6d6-3473-8591-383e693a0f55 | -5.0994 | -43.1977 | 2025-10-26 04:30:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 33.4 |
| aa33666b-a33d-32c6-b84f-fc3609d40b69 | -17.3165 | -43.643 | 2025-10-26 04:30:00 | GOES-19 | OLHOS-D'ÁGUA | MINAS GERAIS | Brasil | 3145455 | 31 | 33 | nan | nan | nan | Cerrado | 106.6 |
| 5bdce97e-65c5-3cc9-be0a-812ff4544639 | -21.7717 | -50.0374 | 2025-10-26 04:30:00 | GOES-19 | GETULINA | SÃO PAULO | Brasil | 3517000 | 35 | 33 | nan | nan | nan | Mata Atlântica | 113.8 |
| 6371bcb4-1546-315c-83b5-33bb8d2419a1 | -17.3365 | -43.6383 | 2025-10-26 04:30:00 | GOES-19 | OLHOS-D'ÁGUA | MINAS GERAIS | Brasil | 3145455 | 31 | 33 | nan | nan | nan | Cerrado | 74.4 |
| 486dbfd2-11af-3b2f-b571-925aa2df43d6 | -5.1181 | -43.1964 | 2025-10-26 04:30:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 31.4 |
| d6d2320e-011e-3e70-8a37-b6c408bc7f0b | -21.7509 | -50.042 | 2025-10-26 04:30:00 | GOES-19 | GETULINA | SÃO PAULO | Brasil | 3517000 | 35 | 33 | nan | nan | nan | Mata Atlântica | 80.3 |
| 653920d6-c765-3ebe-a92f-7471ffd51e21 | -13.5405 | -43.0077 | 2025-10-26 04:30:00 | GOES-19 | RIACHO DE SANTANA | BAHIA | Brasil | 2926400 | 29 | 33 | nan | nan | nan | Caatinga | 78.3 |
| d9cd3cbd-a906-3a4b-a241-d35f93725f8e | -6.3864 | -45.7819 | 2025-10-26 04:30:00 | GOES-19 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 31.3 |
| 76f8ff2d-0152-313e-83cf-8ba47ec2d874 | -5.1181 | -43.1964 | 2025-10-26 04:40:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 77.0 |
| e5258b6b-4787-3451-a341-881546f06930 | -5.0994 | -43.1977 | 2025-10-26 04:40:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 44.3 |
| 6589687e-80e1-3dff-b286-1b337f916546 | -2.3178 | -48.5717 | 2025-10-26 04:40:00 | GOES-19 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 33.7 |
| bbad1e09-f289-306e-bcb5-6a1950ca7603 | -17.3165 | -43.643 | 2025-10-26 04:40:00 | GOES-19 | OLHOS-D'ÁGUA | MINAS GERAIS | Brasil | 3145455 | 31 | 33 | nan | nan | nan | Cerrado | 102.8 |
| d011d3c9-e727-3598-a165-65e4ce792693 | -17.3365 | -43.6383 | 2025-10-26 04:40:00 | GOES-19 | OLHOS-D'ÁGUA | MINAS GERAIS | Brasil | 3145455 | 31 | 33 | nan | nan | nan | Cerrado | 80.9 |
| 648a9dac-35b4-3bf6-908a-79f42077d4a6 | -13.5405 | -43.0077 | 2025-10-26 04:40:00 | GOES-19 | RIACHO DE SANTANA | BAHIA | Brasil | 2926400 | 29 | 33 | nan | nan | nan | Caatinga | 74.9 |
| d4149271-e5bf-3336-94d0-fbf6c69f8c21 | 3.63649 | -51.82637 | 2025-10-26 04:46:00 | NOAA-21 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 0.6 |
| af5f201f-a713-3f89-b36a-77b62415af86 | 3.31927 | -60.08065 | 2025-10-26 04:46:00 | NOAA-21 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 8478b992-de05-3507-baa2-cd99c560d73d | 3.31455 | -60.08271 | 2025-10-26 04:46:00 | NOAA-21 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 2.4 |
| e08e73c5-a949-32f4-9c27-cfed5e1e6f80 | 3.31981 | -60.0844 | 2025-10-26 04:46:00 | NOAA-21 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 1.8 |
| adcb8f0a-115e-36b1-93c2-fb09a118801d | 3.3207 | -60.0858 | 2025-10-26 04:46:00 | NOAA-21 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 1.6 |
| f8c0ad2d-12fb-32fe-9e8d-15efc0cc0271 | 3.63312 | -51.82689 | 2025-10-26 04:46:00 | NOAA-21 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 47fdf19d-3156-3585-ba41-eed0aa9bc189 | 3.34265 | -60.08512 | 2025-10-26 04:46:00 | NOAA-21 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 44db27bc-d068-34ea-a98b-a74238a623c4 | -2.63454 | -47.30115 | 2025-10-26 04:49:00 | NOAA-21 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 91a8bd1d-1fd8-30d9-94d7-4b914cf37469 | -2.31742 | -48.58025 | 2025-10-26 04:49:00 | NOAA-21 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 40c65329-b958-329b-a617-3947ca3ed903 | -5.50507 | -49.58072 | 2025-10-26 04:49:00 | NOAA-21 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| ab738e80-268d-3e22-b46d-dc88fddd403d | -4.19742 | -54.94237 | 2025-10-26 04:49:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 6c0fbf39-eb2e-3ef9-a139-3184e6a37cde | -4.26659 | -50.50585 | 2025-10-26 04:49:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| f9d3fd7d-47c1-3792-ba36-9d6d67f8664e | -4.15557 | -46.78991 | 2025-10-26 04:49:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 2.3 |
| e540c693-c3ec-385b-82a1-7e6d2faa72c8 | 0.37292 | -50.91434 | 2025-10-26 04:49:00 | NOAA-21 | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 9c2ca33d-2da8-3a4c-b567-9844f52f1bf5 | -2.4789 | -49.25613 | 2025-10-26 04:49:00 | NOAA-21 | MOCAJUBA | PARÁ | Brasil | 1504604 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| a86e102c-2fc9-395f-ae1b-a616558636a8 | -2.48001 | -49.2573 | 2025-10-26 04:49:00 | NOAA-21 | MOCAJUBA | PARÁ | Brasil | 1504604 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| e1ede161-c541-3fb3-96ed-311756fd3dbc | -6.72684 | -39.27411 | 2025-10-26 04:49:00 | NOAA-21 | VÁRZEA ALEGRE | CEARÁ | Brasil | 2314003 | 23 | 33 | nan | nan | nan | Caatinga | 12.1 |
| 9c5893fe-5c44-3899-96fd-96c6dd6a70a9 | 1.60828 | -55.75575 | 2025-10-26 04:49:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| a93250f3-2aa8-3c04-acd9-2af0e263e86e | -4.72524 | -47.4222 | 2025-10-26 04:49:00 | NOAA-21 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 7.8 |
| 02754495-c959-3ab6-82ea-bc8ff0535f1c | -6.90686 | -46.15002 | 2025-10-26 04:49:00 | NOAA-21 | FORTALEZA DOS NOGUEIRAS | MARANHÃO | Brasil | 2104107 | 21 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 8a99616d-2db2-3fcc-a9b3-66514e7ec788 | -6.08779 | -49.89765 | 2025-10-26 04:49:00 | NOAA-21 | PARAUAPEBAS | PARÁ | Brasil | 1505536 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| f82af623-4822-3cf1-be2e-a552a82a8373 | -3.14679 | -50.16182 | 2025-10-26 04:49:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| fe7e2c5e-eb92-36ff-9de3-bdb9e65256a0 | -3.52697 | -52.43837 | 2025-10-26 04:49:00 | NOAA-21 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 63b2fc64-2608-3041-900b-6372f636418a | -6.63035 | -44.63372 | 2025-10-26 04:49:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| b8dad77c-5370-331b-96d3-5acf63905519 | -4.22154 | -48.35718 | 2025-10-26 04:49:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 8880fc96-3dae-3f57-9af9-27b3425f7032 | -3.10118 | -49.4536 | 2025-10-26 04:49:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| ea579e4b-dbdc-3662-8e28-d0568e7440e5 | -5.75458 | -53.39743 | 2025-10-26 04:49:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| ece3f667-4278-391f-94cb-8ad8f962cd10 | -7.36001 | -42.43896 | 2025-10-26 04:49:00 | NOAA-21 | SÃO FRANCISCO DO PIAUÍ | PIAUÍ | Brasil | 2209708 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 70c606ab-847c-320b-8fa1-3858a20a3bb0 | -3.49107 | -53.28697 | 2025-10-26 04:49:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| c8f89afd-18c5-3c0b-8306-40b617c35188 | -3.14042 | -50.44687 | 2025-10-26 04:49:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 1b45b6c2-ad99-34d3-967a-2a9d957de289 | -4.48433 | -48.67102 | 2025-10-26 04:49:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 0cddd6cc-198f-333f-a55f-2fdafc87c026 | -3.79769 | -52.01593 | 2025-10-26 04:49:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 7b4f123e-d07d-38c1-95d8-32e942701f75 | -3.27671 | -50.04811 | 2025-10-26 04:49:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e0643cba-3bec-3b37-904e-aff608c32bfb | -7.34797 | -42.4413 | 2025-10-26 04:49:00 | NOAA-21 | SÃO FRANCISCO DO PIAUÍ | PIAUÍ | Brasil | 2209708 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| e1c6652c-7dfd-3c7f-999c-48289cb02ab9 | -4.52894 | -55.80823 | 2025-10-26 04:49:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| a78720f9-25b1-31b7-ad3d-9cf3c38ab0b9 | -5.71077 | -49.27546 | 2025-10-26 04:49:00 | NOAA-21 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 694eb663-0204-3d4f-ac88-e91b45729534 | -3.90259 | -47.72345 | 2025-10-26 04:49:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| da20f2b4-9205-3903-a851-eb672cf51078 | -4.2694 | -50.50998 | 2025-10-26 04:49:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| c8ca81c4-b04f-3fa1-a2ea-beb184b4a360 | -5.11146 | -43.18596 | 2025-10-26 04:49:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| ceda7cda-8865-37f6-8743-bf577623c2a8 | -4.89803 | -43.25465 | 2025-10-26 04:49:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 3314d324-7ff4-34ae-bdd5-280695873805 | -3.78539 | -52.04554 | 2025-10-26 04:49:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| e5e5f4dc-c219-3f10-8e42-3968cc9716b1 | -4.89332 | -43.25141 | 2025-10-26 04:49:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 6.0 |
| c13ca921-1bbd-30e1-8ef3-87b8faf9fd2a | -2.95532 | -49.67487 | 2025-10-26 04:49:00 | NOAA-21 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 869c13c9-56fc-33e4-aef3-ae87a3309d3d | -3.7944 | -52.01542 | 2025-10-26 04:49:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 2c26470d-c764-36be-814e-69704f9691c5 | -4.88807 | -43.25061 | 2025-10-26 04:49:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 6f66596a-8880-3276-9efe-0584ce1f55ce | 1.6455 | -55.7034 | 2025-10-26 04:49:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| db9e4231-8f5d-3382-a551-c5ddf3bba983 | -6.79641 | -45.4099 | 2025-10-26 04:49:00 | NOAA-21 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 56b55b2c-5d4f-3128-9ba1-d15169d69dc5 | -4.83775 | -50.92595 | 2025-10-26 04:49:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| deec0fed-ded8-368d-a4ed-5f1aa7f96607 | -2.79084 | -48.89497 | 2025-10-26 04:49:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 249da766-7592-3e36-b946-5133c3b1c212 | -3.10234 | -49.44596 | 2025-10-26 04:49:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 2fb78749-f326-3874-8ed9-5afbfc624646 | -2.91762 | -52.71926 | 2025-10-26 04:49:00 | NOAA-21 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 33ac96fe-e6e4-3818-97f0-724c9d5788d0 | -3.99896 | -48.31758 | 2025-10-26 04:49:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 07e9c99d-621d-3f95-a5a4-8c30bee97c84 | -6.22416 | -42.54802 | 2025-10-26 04:49:00 | NOAA-21 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 3.2 |
| 8ec02fab-bca1-3a8a-b90a-a270947b312e | -4.71216 | -46.43802 | 2025-10-26 04:49:00 | NOAA-21 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 5.4 |
| b6df83a7-a7b2-3d90-b74f-62f4bc1fe552 | -3.53347 | -52.99921 | 2025-10-26 04:49:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 0483ad89-dc44-3046-91a9-d2c3e5d8173c | -6.548 | -41.60361 | 2025-10-26 04:49:00 | NOAA-21 | LAGOA DO SÍTIO | PIAUÍ | Brasil | 2205599 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 92549b57-48d4-3e66-a89f-64a1b9aff6d9 | -1.01635 | -53.72138 | 2025-10-26 04:49:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 47cf42b8-74f6-388c-926e-918fb746d500 | -6.66844 | -47.74174 | 2025-10-26 04:49:00 | NOAA-21 | PALMEIRAS DO TOCANTINS | TOCANTINS | Brasil | 1713809 | 17 | 33 | nan | nan | nan | Cerrado | 4.3 |
| c255fe1a-f5d7-3c08-bd1e-99de589c4ef8 | -3.87186 | -52.18904 | 2025-10-26 04:49:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| cb82dd2c-ac5f-3b00-b8f0-3946c755fb88 | -4.73733 | -50.87088 | 2025-10-26 04:49:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| d1bc0cd2-f4d4-3993-ad40-0c5717be71c5 | -3.13491 | -53.00198 | 2025-10-26 04:49:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| de39fec7-c190-363e-99ea-5a3933e7404f | -2.57355 | -48.96468 | 2025-10-26 04:49:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ddc66ad4-d388-3c70-9f80-c59e28493c6c | -3.83213 | -50.19898 | 2025-10-26 04:49:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 3a6ebfbe-2de4-310b-8daa-6714f2de0a75 | -7.14357 | -44.84753 | 2025-10-26 04:49:00 | NOAA-21 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 4a144b71-c3b6-3832-95fd-d38289dcefb4 | -7.35474 | -42.4457 | 2025-10-26 04:49:00 | NOAA-21 | SÃO FRANCISCO DO PIAUÍ | PIAUÍ | Brasil | 2209708 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 0bf081df-97a8-3cea-971a-61e245e420af | -7.14552 | -44.84692 | 2025-10-26 04:49:00 | NOAA-21 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 024cabeb-57ff-3021-a216-52f80cdf4c6b | -2.06657 | -56.88396 | 2025-10-26 04:49:00 | NOAA-21 | NHAMUNDÁ | AMAZONAS | Brasil | 1303007 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 156b521e-bd29-3b07-a475-802de0019b7d | -2.974 | -49.11901 | 2025-10-26 04:49:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 0470cb35-e0f2-3fce-83d3-af74ef5d7ab2 | -4.89287 | -43.25467 | 2025-10-26 04:49:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 2f6cd729-1150-396c-8302-fc90f51c18d1 | -3.81286 | -49.29704 | 2025-10-26 04:49:00 | NOAA-21 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 4662de69-4770-35b8-802b-77f1333a4a38 | -2.60777 | -51.91574 | 2025-10-26 04:49:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 2d512470-32eb-311a-b9a6-8149db045e65 | -6.4451 | -45.73501 | 2025-10-26 04:49:00 | NOAA-21 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 22651b3d-6fff-3ce7-a704-a6a1a83032c6 | -5.1159 | -43.19754 | 2025-10-26 04:49:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 96fff4a0-13da-3ffa-a92c-f7bb6ec7ebaa | -4.48004 | -48.6747 | 2025-10-26 04:49:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 7.8 |
| 7a5a061b-45ee-3f66-9e58-c7ef0e969962 | -4.2053 | -49.78389 | 2025-10-26 04:49:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 66d196b0-3fe9-3fde-8560-2dba50299f8b | -2.81349 | -49.14441 | 2025-10-26 04:49:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 28bf4077-328c-3139-858a-5f94982656bd | -2.32037 | -48.58485 | 2025-10-26 04:49:00 | NOAA-21 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 037aa7a7-82b3-3990-bf16-2ae1b169094e | -4.3915 | -49.78038 | 2025-10-26 04:49:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 06bc7eee-5799-3b40-b1c3-b267ee6ed92a | -4.02473 | -45.99755 | 2025-10-26 04:49:00 | NOAA-21 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 14acd80a-5f20-381b-9d7d-aa24a82ec25c | -5.1861 | -49.8856 | 2025-10-26 04:49:00 | NOAA-21 | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| bdb07311-ec8c-32cd-a481-93dab790052b | 1.6519 | -55.69171 | 2025-10-26 04:49:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 8b3c8f2d-b5a2-3e9c-967c-bf5617c54e27 | -1.19482 | -53.386 | 2025-10-26 04:49:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |


[Clique aqui para ver as próximas entradas](README31.md)
