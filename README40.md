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
| 61542df9-6696-3f5c-b270-20c19e70f20e | -3.60653 | -49.99274 | 2024-11-30 04:40:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| d1b00224-faf2-3421-85d7-5b20b83c3c7b | -3.33422 | -50.05771 | 2024-11-30 04:40:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 20224ffa-d588-3c91-bbcd-a650fed9ef4f | -2.23219 | -46.39433 | 2024-11-30 04:40:00 | NOAA-21 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| ee374646-6b53-35d2-aa29-44635e3759a9 | -4.69852 | -42.38753 | 2024-11-30 04:40:00 | NOAA-21 | JOSÉ DE FREITAS | PIAUÍ | Brasil | 2205508 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 1c46ce48-54af-3d1d-8670-86776580f8a0 | -2.98477 | -53.2971 | 2024-11-30 04:40:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| c6c5b945-074f-36bf-959d-5772ed99cae3 | -3.25145 | -54.21566 | 2024-11-30 04:40:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 99a57e24-53c3-39f3-807e-ea649f5989b5 | -2.73296 | -48.42126 | 2024-11-30 04:40:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 9b97b4ad-d42e-3a79-8e89-bd5e14098f04 | -2.30856 | -47.08391 | 2024-11-30 04:40:00 | NOAA-21 | GARRAFÃO DO NORTE | PARÁ | Brasil | 1503077 | 15 | 33 | nan | nan | nan | Amazônia | 10.6 |
| a7ca861e-4c7e-30d8-b200-750a9210e228 | -2.30462 | -46.5457 | 2024-11-30 04:40:00 | NOAA-21 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| fc17e6b0-4035-35e1-92ee-83a7baeba604 | -3.00458 | -49.51361 | 2024-11-30 04:40:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 9f389d71-a09d-3c88-9b71-4185feda8be0 | -3.24414 | -48.48021 | 2024-11-30 04:40:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| c78cdb14-0c66-397d-8488-be410e367aa7 | -2.71463 | -46.12622 | 2024-11-30 04:40:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 2c680690-037a-313e-a3ae-89c606751567 | -3.0588 | -49.5369 | 2024-11-30 04:40:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 12e6bb81-6db6-3894-a324-210ea099fab6 | -3.22057 | -54.1736 | 2024-11-30 04:40:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 7.7 |
| 8a5d963c-2ce1-3b1a-9e23-0dba4be0d15c | -2.5063 | -46.23295 | 2024-11-30 04:40:00 | NOAA-21 | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 33bc1490-42d4-3765-9e6a-f39c9a9fedc4 | -1.39545 | -53.63058 | 2024-11-30 04:40:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| a655d960-15b0-302f-a71c-15c66e39ab20 | -4.173 | -48.63158 | 2024-11-30 04:40:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| fce9a996-b527-3a4f-80c9-83916a422c11 | -2.54303 | -47.98034 | 2024-11-30 04:40:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 4f46c49f-af83-3712-8e4b-0059569ebaef | -2.92422 | -52.68831 | 2024-11-30 04:40:00 | NOAA-21 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| bd862385-c20e-365b-8737-fa66964ade8a | -6.70929 | -47.26714 | 2024-11-30 04:40:00 | NOAA-21 | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 43dd97d6-3aa6-3620-a097-bf0de5d21ad5 | -3.25167 | -50.58133 | 2024-11-30 04:40:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 01279853-b055-3439-9981-95e4ed95f158 | -2.23537 | -53.62586 | 2024-11-30 04:40:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 9692dcdc-3b76-3dc1-9016-8c47175f370b | -5.96913 | -43.36996 | 2024-11-30 04:40:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Caatinga | 6.2 |
| 482f8424-aeda-3bf4-9d62-63c0aded8536 | -3.08561 | -49.21189 | 2024-11-30 04:40:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 5dfa17db-8a8e-3c44-ae2f-532b0a0fa907 | -2.94088 | -48.00267 | 2024-11-30 04:40:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 050e3c6b-907f-3762-9009-d152f8fca5b5 | -3.80971 | -46.54217 | 2024-11-30 04:40:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| dc60cd63-b0ae-3f3d-963a-f833c4428573 | -3.73641 | -49.94493 | 2024-11-30 04:40:00 | NOAA-21 | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 8db9ecdc-8aaa-3858-bfb4-93f63b421015 | -2.66943 | -46.54082 | 2024-11-30 04:40:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 4f2f1244-8e37-3f0e-9243-9e4a6c26841c | -3.96839 | -46.90003 | 2024-11-30 04:40:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 2.5 |
| ee984582-cd58-3235-9011-d1a2ad3818ed | -2.32098 | -50.64774 | 2024-11-30 04:40:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 637be3d9-541d-3654-9e5c-e6f118d94a77 | -4.07643 | -54.5627 | 2024-11-30 04:40:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 23584ee3-5c06-3547-8e99-e6c2432e1b3f | -3.84558 | -52.02413 | 2024-11-30 04:40:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 0fbd5560-ba2f-35f5-855e-1e297015d97a | -1.94454 | -51.20917 | 2024-11-30 04:40:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| dd677e8e-0974-3c2c-a27b-24a715eb46bf | -8.31572 | -44.95326 | 2024-11-30 04:40:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 49956b46-45c2-3351-986f-6987e83facbe | -3.17136 | -46.5442 | 2024-11-30 04:40:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 678101f8-0e36-30a5-aed8-fb9a6fe9d7f5 | -3.31705 | -53.75304 | 2024-11-30 04:40:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 92ce7be2-5a46-36d7-9f8a-ce5dcd1bc43c | -3.94006 | -47.98064 | 2024-11-30 04:40:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 079882b9-35bf-324f-ac06-0aa4f607a774 | -1.20735 | -51.74249 | 2024-11-30 04:40:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 735e3b90-b20b-3c7d-8cf5-38484046fafd | -4.07537 | -42.19059 | 2024-11-30 04:40:00 | NOAA-21 | BATALHA | PIAUÍ | Brasil | 2201507 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| b136409f-9a92-3e02-ab4d-3ef74deff1a0 | -2.51041 | -46.22956 | 2024-11-30 04:40:00 | NOAA-21 | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 2f877eb4-f04d-3068-b46c-876b66505886 | -1.56736 | -52.00195 | 2024-11-30 04:40:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 13d37d2a-839e-367d-8f7c-4756727ef67e | -3.26449 | -51.62308 | 2024-11-30 04:40:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 8b980d4a-b1fd-32fe-b2d5-a4d7bab7d0fb | -3.25372 | -53.6468 | 2024-11-30 04:40:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| a91562a1-b1a9-3fcc-963e-66149c8ee5af | -2.69441 | -52.91219 | 2024-11-30 04:40:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 007cec1c-4e9c-3327-a6fd-aea9c033683d | -0.81787 | -51.61855 | 2024-11-30 04:40:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 67bf05bd-9d4b-38a7-ab4d-b81384ddd9b3 | -4.54856 | -50.70606 | 2024-11-30 04:40:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| dc12a068-5326-3cfa-838e-8cf5944dbbb9 | -0.99276 | -51.72421 | 2024-11-30 04:40:00 | NOAA-21 | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 654ff814-3b44-3470-8688-5b1b1c5b4aef | -1.66685 | -52.17805 | 2024-11-30 04:40:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 850f4148-e85c-305d-b3c8-8a8c1a3bc439 | -2.81163 | -55.29984 | 2024-11-30 04:40:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| e6e70066-6913-374c-8861-fc6bf87eb214 | -2.61284 | -48.16589 | 2024-11-30 04:40:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ec3f1e21-aac7-3549-813b-cc6f9fd31bc8 | -2.7237 | -46.23255 | 2024-11-30 04:40:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| b59ac09a-4f44-3d42-93ae-6be73c9645ed | -3.50498 | -53.83419 | 2024-11-30 04:40:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 3309cf77-faaf-3e62-9a4a-7dbd51f6bf33 | -1.62556 | -53.86477 | 2024-11-30 04:40:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 90e37e53-09c6-3a6e-bee3-eca9a6baa386 | -3.31959 | -46.17332 | 2024-11-30 04:40:00 | NOAA-21 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f558fdaf-1240-3f0f-8ba9-06686b0d3512 | -3.25761 | -53.42033 | 2024-11-30 04:40:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 4ade0856-ba67-3219-911a-43ffcc5b62c5 | -2.81076 | -48.62006 | 2024-11-30 04:40:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 7c483c6e-37d7-386e-a069-82fb7c8512a6 | -1.71711 | -52.68806 | 2024-11-30 04:40:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| f7b1256b-0da3-3f61-b091-b74ad06d0950 | -3.94809 | -40.97175 | 2024-11-30 04:40:00 | NOAA-21 | IBIAPINA | CEARÁ | Brasil | 2305308 | 23 | 33 | nan | nan | nan | Caatinga | 2.8 |
| b00fe72f-7220-30fe-a49a-98cfba9c51a8 | -3.86353 | -52.3941 | 2024-11-30 04:40:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| d6487c8b-0935-37fc-ac10-638fc7e467b0 | -3.24974 | -53.86702 | 2024-11-30 04:40:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 1de952d4-46d8-3eb1-b894-3dab752f83c5 | -2.84711 | -54.02938 | 2024-11-30 04:40:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| fce7cd8c-ba6a-3029-9119-88ae4557e32e | -1.70455 | -52.76698 | 2024-11-30 04:40:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 5d626878-16e0-3e51-927b-bd1bca23335f | -2.58756 | -48.19682 | 2024-11-30 04:40:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| f1615dc8-93d1-362b-a222-bd1d075d352e | -1.757 | -50.73227 | 2024-11-30 04:40:00 | NOAA-21 | MELGAÇO | PARÁ | Brasil | 1504505 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 2a0e6f42-d0f0-3336-a120-99e1944b00aa | -3.2446 | -53.92371 | 2024-11-30 04:40:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 8.1 |
| ebf5bc4d-7284-39fa-a719-e441d5a9d93a | -3.38383 | -50.11226 | 2024-11-30 04:40:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 6d8f52a8-d6bb-39ba-8b25-422b99128c13 | -4.00213 | -49.52891 | 2024-11-30 04:40:00 | NOAA-21 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 986e2faf-d12b-306c-81d3-ad8f9ef4a635 | -2.69383 | -51.99301 | 2024-11-30 04:40:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 7de76e0e-2d23-3008-8101-6fe4fb316ca2 | -3.02947 | -49.52808 | 2024-11-30 04:40:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| cd3632b5-065f-34bc-ad1e-01efe8469603 | -3.09583 | -53.28247 | 2024-11-30 04:40:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| fbd2a735-619c-3c74-ba0f-9fd0896f9f8c | -2.94105 | -48.59145 | 2024-11-30 04:40:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 1e2fa6ee-0156-3bc6-be59-b1dae01a5357 | -3.58236 | -50.51107 | 2024-11-30 04:40:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| a4379255-e730-3c75-b533-8e00a8619d11 | -2.66083 | -48.79726 | 2024-11-30 04:40:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| c6e9bc1e-83e3-3331-bd69-829edb7ac161 | -3.09439 | -54.12804 | 2024-11-30 04:40:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| e008c2bb-b0b2-3a7a-b645-1ad738b6d73d | -3.12732 | -51.12141 | 2024-11-30 04:40:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 333ccadf-5a92-3ff8-9a35-de402cb7e78f | -2.55695 | -46.40285 | 2024-11-30 04:40:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 3f6abe77-a835-345a-8310-6dfc6d68ddd2 | -4.8761 | -41.284 | 2024-11-30 04:40:00 | NOAA-21 | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 6.4 |
| 9d77f9f3-f60c-3daa-900e-ba0fd4ff8848 | -2.33958 | -51.06807 | 2024-11-30 04:40:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| eb675151-dfaa-3021-bfbe-217c2b46739e | -4.15092 | -48.99182 | 2024-11-30 04:40:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| c52bcfc9-62cd-3f20-a10f-1d1fa5ef717a | -3.03679 | -51.47684 | 2024-11-30 04:40:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 4b0fbda3-f3d2-3424-81d5-7476dcd9cfee | -3.28579 | -50.16935 | 2024-11-30 04:40:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| bab8ffe1-61e5-382c-a89e-b6821627a2e5 | -2.32366 | -50.67798 | 2024-11-30 04:40:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| e6f33fb9-dc64-3ba3-bd55-e6dc4e06b66a | -4.17461 | -48.62121 | 2024-11-30 04:40:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| e9924fb6-e475-34ee-a901-0be0fb38ed1d | -1.36155 | -54.65512 | 2024-11-30 04:40:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 6bf034e3-01cb-3c00-9fff-332799bf0b7f | -3.71187 | -45.69275 | 2024-11-30 04:40:00 | NOAA-21 | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 021dd71e-9269-32e5-b3ce-efc87bfec4e6 | -1.39834 | -52.05199 | 2024-11-30 04:40:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 0b52275c-50d9-370a-9385-29bf509e49e6 | -2.99388 | -53.36283 | 2024-11-30 04:40:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 895030c5-cf8d-36a7-9290-0dc647fe3372 | -2.62331 | -46.79616 | 2024-11-30 04:40:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 15bb8bf0-9ce9-307a-8223-1135db1027de | -1.51084 | -45.89607 | 2024-11-30 04:40:00 | NOAA-21 | LUÍS DOMINGUES | MARANHÃO | Brasil | 2106201 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| d6733af4-4af3-3ff3-b6f6-147a0b333b8c | -2.10206 | -50.34453 | 2024-11-30 04:40:00 | NOAA-21 | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| d6368524-6295-338c-bdfa-635f289bd12c | -2.60674 | -51.81145 | 2024-11-30 04:40:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| c98a69f2-a870-3b33-ad6f-5c2b53ac6eb9 | -1.29232 | -51.36645 | 2024-11-30 04:40:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 3323489c-bf20-32b2-a80b-63c3df6560aa | -1.7762 | -46.12643 | 2024-11-30 04:40:00 | NOAA-21 | BOA VISTA DO GURUPI | MARANHÃO | Brasil | 2101970 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 92fca3ee-0b30-32d6-85a4-1b8af715aa83 | -3.60429 | -49.98521 | 2024-11-30 04:40:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 124.2 |
| f82eca50-9bf0-3e5f-b7b1-19df41ace033 | -2.862 | -48.09393 | 2024-11-30 04:40:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c0cc3a8a-86e1-3b81-8a77-a6d9761cb3b2 | -3.41533 | -50.16833 | 2024-11-30 04:40:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| ae7310ac-48d9-380f-86b2-8dc6321e1a99 | -1.83542 | -50.65626 | 2024-11-30 04:40:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 1f32d8c0-b0e9-3cdb-bc94-368caf99f400 | -3.74878 | -52.64528 | 2024-11-30 04:40:00 | NOAA-21 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 7f43f7eb-a74b-35df-87e1-c8027dcc9283 | -1.00001 | -51.72531 | 2024-11-30 04:40:00 | NOAA-21 | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 6.5 |
| d5d0cca1-511a-3644-80fd-dcae8e60298d | -6.70172 | -47.26993 | 2024-11-30 04:40:00 | NOAA-21 | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |


[Clique aqui para ver as próximas entradas](README41.md)
