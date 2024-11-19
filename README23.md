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

## Dados Diários - Página 23

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| d605bc27-dbd2-3b08-8580-c900003e4598 | -3.36389 | -50.82484 | 2024-11-19 04:46:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 812ebe81-ba96-3772-b769-2ca4ccbe829c | -2.03566 | -48.56739 | 2024-11-19 04:46:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 194dbc83-ae62-3b55-9e7b-6d8d06991ff5 | -2.76292 | -54.05225 | 2024-11-19 04:46:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 1a90bf00-a1f1-3489-9ed0-39c60bd2fee6 | -1.95795 | -46.49046 | 2024-11-19 04:46:00 | NOAA-21 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 5cb5ee1b-4507-3e14-877e-ee4b73c0751f | -0.82614 | -52.86447 | 2024-11-19 04:46:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 34c84676-98c9-301d-b120-7e9ebe57c092 | -4.11139 | -51.0478 | 2024-11-19 04:46:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 9b6e4152-af8c-304b-9675-7ea7ffcc62e8 | -2.10852 | -48.10135 | 2024-11-19 04:46:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 3fdb633e-14b5-3687-8dc6-3db5600f3875 | -6.2591 | -46.09214 | 2024-11-19 04:46:00 | NOAA-21 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 8c1540ed-200f-3d1a-8bda-32b13a4b3e75 | -2.28772 | -51.17997 | 2024-11-19 04:46:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| f3582dff-5956-31ba-b439-1b408273600c | -1.2067 | -51.76772 | 2024-11-19 04:46:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| ef72401a-4916-3032-b2ea-73a0c30b99d3 | -7.9009 | -44.22399 | 2024-11-19 04:46:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 79b47ab8-4185-3659-9e2b-9c7760c7f1a4 | -2.8536 | -53.97585 | 2024-11-19 04:46:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| ed95fb72-d458-35a9-a9b9-e044a41e99b2 | -3.11449 | -53.70607 | 2024-11-19 04:46:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 573e5139-f6c5-3ca3-8bc9-5f1b52dc68be | -2.85327 | -51.58763 | 2024-11-19 04:46:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ef5292a7-1ebe-3680-ac41-d2695fe2869a | -3.77324 | -50.16334 | 2024-11-19 04:46:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| e809b03e-84cf-3520-bd53-517515bc8822 | -2.87154 | -51.79338 | 2024-11-19 04:46:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 6a9e2ffb-b73a-3eb7-afc4-8e9fbb87b41a | -3.94038 | -49.98355 | 2024-11-19 04:46:00 | NOAA-21 | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e0e184c5-d81f-3ba9-a326-5f009bd8b2a2 | -3.37047 | -45.32932 | 2024-11-19 04:46:00 | NOAA-21 | MONÇÃO | MARANHÃO | Brasil | 2106904 | 21 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 591f033c-43cd-3e5c-9bdc-d33e3392932a | -2.11547 | -48.55305 | 2024-11-19 04:46:00 | NOAA-21 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 9c06bf1a-470c-3016-8f64-308014ab0f59 | -7.48515 | -47.15169 | 2024-11-19 04:46:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| a3255b76-b14d-373d-9fd7-3f84c05d5301 | -1.51503 | -52.08838 | 2024-11-19 04:46:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 9d48a38e-af0d-3c2a-bbc7-32acfda46950 | -1.85501 | -47.82974 | 2024-11-19 04:46:00 | NOAA-21 | SÃO DOMINGOS DO CAPIM | PARÁ | Brasil | 1507201 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| b3462442-0f20-35e2-8ea2-6f676a46e37c | -1.3084 | -51.7461 | 2024-11-19 04:46:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 051971ef-44fb-3012-86bb-c2419613a7d8 | -1.20218 | -51.77445 | 2024-11-19 04:46:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 61a465d0-9dc9-3dd2-9a0c-a5f1c1c51d2f | 0.27806 | -51.14153 | 2024-11-19 04:46:00 | NOAA-21 | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 0.4 |
| c7a7074b-f762-3f90-b92b-67f09ab9cf57 | -5.97188 | -45.35689 | 2024-11-19 04:46:00 | NOAA-21 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 8f5e3ca8-79b1-3c6b-aeb8-d1300b617838 | -1.2463 | -52.05509 | 2024-11-19 04:46:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 6faf31e0-8db3-39a1-93ea-6a54b5af2fc4 | -3.03807 | -49.46496 | 2024-11-19 04:46:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 09e6c816-c598-325e-a029-a7a9ce98568c | -5.74454 | -47.91481 | 2024-11-19 04:46:00 | NOAA-21 | ARAGUATINS | TOCANTINS | Brasil | 1702208 | 17 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 6bbf2d52-76f1-3d18-b03f-1e768aeed264 | -4.73976 | -46.66615 | 2024-11-19 04:46:00 | NOAA-21 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| d1174432-df7d-3480-bc77-f284e2d131a3 | -0.15014 | -51.58737 | 2024-11-19 04:46:00 | NOAA-21 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 42570d27-b9f6-3eb2-8fc2-cc06914de93b | -3.85139 | -50.99336 | 2024-11-19 04:46:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 1c9702c2-0850-32e6-875c-94ba746fb9d9 | -3.94873 | -46.70009 | 2024-11-19 04:46:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 3b610cce-63ca-3520-8614-7aafb5a8670a | -7.88674 | -44.22197 | 2024-11-19 04:46:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 53be424d-532b-3486-b456-b5ea38aa552b | -4.06045 | -49.99896 | 2024-11-19 04:46:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| e1e291f4-baf7-3bc9-875c-585ddf2497d4 | -2.68387 | -46.22732 | 2024-11-19 04:46:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 10842d46-292e-33fe-b0eb-7e82cb874875 | -3.52826 | -50.25205 | 2024-11-19 04:46:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 6c19fc65-475d-3a9c-9998-22f926604a57 | -1.6223 | -53.29429 | 2024-11-19 04:46:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 3f522326-02d0-38f5-aae4-f00d9cda8b9d | -2.77828 | -48.57808 | 2024-11-19 04:46:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| eeccf3af-568a-3fc3-be63-7c260b20563c | -3.86792 | -51.16888 | 2024-11-19 04:46:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 3b6be693-bd3c-3373-bb69-b685d078c729 | -2.56256 | -48.06264 | 2024-11-19 04:46:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 8b475141-717b-3b29-8671-b84b129f210e | -0.12524 | -51.61341 | 2024-11-19 04:46:00 | NOAA-21 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 90df2943-977f-387a-9c9c-054d9a900657 | -3.29379 | -53.85156 | 2024-11-19 04:46:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| b51ab795-8008-3fca-b762-15ba9b4c7023 | -2.58344 | -51.72303 | 2024-11-19 04:46:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 0d46ca24-dabb-38d1-80e5-f4e4428efedb | -3.29606 | -53.86055 | 2024-11-19 04:46:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| fbe1267a-eb91-3d61-81fe-922683791be3 | -5.15493 | -48.18226 | 2024-11-19 04:46:00 | NOAA-21 | VILA NOVA DOS MARTÍRIOS | MARANHÃO | Brasil | 2112852 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| bc39f922-ddf8-3dde-8805-37b9091c21a1 | -0.91332 | -51.74104 | 2024-11-19 04:46:00 | NOAA-21 | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 1.4 |
| e01434a3-6295-3a5b-b9f9-32c8d3516bbb | -3.69355 | -51.56432 | 2024-11-19 04:46:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 26f5f33e-12f8-370e-84b8-b0acc8d99f31 | -3.55351 | -51.52466 | 2024-11-19 04:46:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| fb3bdf75-921b-3037-87ce-510cb71121f4 | -1.64019 | -52.67214 | 2024-11-19 04:46:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 9.0 |
| 2a3b1f6a-5021-3cca-8c62-a863fa6a3ce8 | -2.40185 | -46.99399 | 2024-11-19 04:46:00 | NOAA-21 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 671bce89-b4ba-3372-9c61-1ed9a6022a0e | -1.42627 | -51.09882 | 2024-11-19 04:46:00 | NOAA-21 | MELGAÇO | PARÁ | Brasil | 1504505 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 3625bc0b-7bc7-3081-80ed-49b3009f4744 | -2.44017 | -50.402 | 2024-11-19 04:46:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 8ab109e3-5a47-311c-9e75-e141189442a4 | -1.60628 | -52.51344 | 2024-11-19 04:46:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| b8e357a2-8b06-35ac-90c7-d97320291325 | -3.47016 | -48.25541 | 2024-11-19 04:46:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 98e24e13-360e-3287-b686-e40b50b493a8 | -0.95463 | -51.72132 | 2024-11-19 04:46:00 | NOAA-21 | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 886a1e59-5303-3345-93e2-0916f51947ed | -2.82394 | -51.79709 | 2024-11-19 04:46:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d1922138-8724-31d1-b82c-4c36f0eb3859 | -6.99626 | -48.12198 | 2024-11-19 04:46:00 | NOAA-21 | WANDERLÂNDIA | TOCANTINS | Brasil | 1722081 | 17 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 953f3375-b4d7-334f-a9aa-c326f193cb39 | -3.33031 | -52.9939 | 2024-11-19 04:46:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 99be863e-c117-32b9-a57b-501be50c0f33 | -2.44347 | -50.4025 | 2024-11-19 04:46:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 82468b6e-c876-3c0d-9fd8-b1604988460f | -1.64858 | -52.64177 | 2024-11-19 04:46:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| b2e14a10-2da1-3f84-a78d-9656743ed237 | -1.22192 | -51.78852 | 2024-11-19 04:46:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 9758e6c0-093f-3638-b2c4-adda864fbfec | -3.6654 | -50.43943 | 2024-11-19 04:46:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 9255f157-de68-37e7-b97f-70a1d8e2ab63 | -1.42024 | -52.82304 | 2024-11-19 04:46:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 6f003366-3ba1-3a15-8990-6dd085083a78 | -3.50424 | -54.03486 | 2024-11-19 04:46:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 5c028132-61ad-3bbd-b589-18a9b8dc75af | -4.11031 | -51.05469 | 2024-11-19 04:46:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 8.1 |
| 91dd237b-eb35-35a8-a3e9-014bce1f954e | -2.7339 | -54.11523 | 2024-11-19 04:46:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| bdb59a9d-6fdc-308e-b7c7-ca4100aeb462 | -2.61562 | -54.53979 | 2024-11-19 04:46:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 3c03881c-3f6b-3140-b96c-80117d9503f4 | -2.96531 | -49.16479 | 2024-11-19 04:46:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b2487323-1a3c-36f9-85e2-f457f45865ee | -3.58363 | -53.72431 | 2024-11-19 04:46:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 7c4e2a2a-a143-3404-9208-2aabb0590942 | -5.66843 | -46.34993 | 2024-11-19 04:46:00 | NOAA-21 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 798296ec-5344-380c-ae0e-b5528163bf97 | -3.31123 | -51.24775 | 2024-11-19 04:46:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| b80ed905-2331-3f8b-9491-c88aebcfd76b | -4.56087 | -48.01715 | 2024-11-19 04:46:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 33737f5a-b80b-3a54-8543-39f451b37490 | -2.96922 | -49.16175 | 2024-11-19 04:46:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 03a67855-d760-39cb-89e6-efd9f14c06ec | -2.26326 | -48.41398 | 2024-11-19 04:46:00 | NOAA-21 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| a98a65b2-f7f2-321c-a0fc-9760277632e5 | -7.56993 | -46.46014 | 2024-11-19 04:46:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 182beaef-cbe4-3f23-9d1d-329436772f21 | -3.08574 | -54.6563 | 2024-11-19 04:46:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 8dfb30fd-24b2-371d-8256-2eef88db5ab7 | -3.59855 | -51.30355 | 2024-11-19 04:46:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 5fbf2d45-4a01-3d8f-84de-702b5741e2be | -3.77502 | -52.40622 | 2024-11-19 04:46:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 95cf458c-7b87-3f1a-82c1-71a98eb149e6 | -3.84973 | -50.69675 | 2024-11-19 04:46:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 90c6569f-1ca8-363d-8c12-4f8d00e5c233 | -0.84679 | -48.74875 | 2024-11-19 04:46:00 | NOAA-21 | CACHOEIRA DO ARARI | PARÁ | Brasil | 1502004 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 9428dced-59f0-352c-a8da-6d69bbf1a2b2 | -3.80789 | -52.39636 | 2024-11-19 04:46:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| bb991974-eaaf-3748-82b9-f3d906791b33 | -3.10601 | -53.10263 | 2024-11-19 04:46:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| dca39cbc-17a6-3b21-8b0b-52e19eb2083c | -2.25939 | -48.32621 | 2024-11-19 04:46:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| a1262153-b9ea-3776-8dc4-579f898d9c1c | -5.15848 | -48.1828 | 2024-11-19 04:46:00 | NOAA-21 | VILA NOVA DOS MARTÍRIOS | MARANHÃO | Brasil | 2112852 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 90a1e9dc-1930-34c7-875a-00f436c559a2 | -4.15766 | -50.77325 | 2024-11-19 04:46:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d773ac19-b5c6-3ac8-a383-6ff5751dde5b | -4.11428 | -43.58933 | 2024-11-19 04:46:00 | NOAA-21 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 18.4 |
| 5421dae0-6848-30f2-82e3-48b3fe06ff3c | -3.06031 | -51.32918 | 2024-11-19 04:46:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 0fd5d572-baf8-3c22-82d2-9d88418a6f8f | -3.94283 | -46.71339 | 2024-11-19 04:46:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 2.2 |
| cbe2fb93-e737-32f6-966f-4136b5be2a91 | -2.1989 | -53.65973 | 2024-11-19 04:46:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 4b58bacf-1200-36ea-8365-fee11861d71d | -4.55317 | -48.02006 | 2024-11-19 04:46:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 9.3 |
| b1fae1cd-b2f1-37dc-b485-539cdcb46971 | -4.22541 | -47.18602 | 2024-11-19 04:46:00 | NOAA-21 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| bbb30177-9103-319b-b6ac-a68b7cf38225 | -4.58214 | -48.02042 | 2024-11-19 04:46:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 10.0 |
| c0661260-3564-3861-84af-37a8606c09b4 | -2.59971 | -51.79486 | 2024-11-19 04:46:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| c8f4e0bf-3c3f-3024-9f45-8ba1d26892ce | -2.57299 | -48.04078 | 2024-11-19 04:46:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 09ea527c-f0f8-3852-b9fc-bd22891b7de3 | -1.38162 | -51.55463 | 2024-11-19 04:46:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 006f1486-f4fc-3d99-bbac-4b7c8e592797 | -2.0193 | -53.5135 | 2024-11-19 04:46:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b174af85-3169-3798-b235-ee5bbfff9bea | -2.68769 | -46.22791 | 2024-11-19 04:46:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a7eb7015-f40b-369b-a1c1-15a1cfe1793f | -1.63177 | -52.50955 | 2024-11-19 04:46:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 934f2562-2247-3ebe-9057-74c464c780e0 | -3.17303 | -54.69157 | 2024-11-19 04:46:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |


[Clique aqui para ver as próximas entradas](README24.md)
