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
| fc99824c-4778-302f-989a-07d493f5c3aa | -14.1866 | -51.5085 | 2025-10-20 13:50:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 89.2 |
| f5936424-3ae0-305f-ab0f-84b78d723982 | -14.2052 | -51.5488 | 2025-10-20 13:50:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 145.3 |
| fcfa0084-9082-3840-8262-3ef4c367f620 | -14.1811 | -51.8293 | 2025-10-20 13:50:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 101.9 |
| c677a8d5-3332-3fb2-979b-d1e0e4e12dc9 | 1.8219 | -55.6642 | 2025-10-20 13:50:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 81.3 |
| 3b97b36c-f6e4-3fad-a69c-54072de944b3 | -14.4523 | -52.8961 | 2025-10-20 13:50:00 | GOES-19 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 104.2 |
| f4fd87ea-22cf-31f7-84b6-d973ef7b7616 | 1.7852 | -55.7042 | 2025-10-20 13:50:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 71.1 |
| b14fb6ce-fe2c-32ee-98a3-6dc26588eb96 | -14.2264 | -51.439 | 2025-10-20 13:50:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 123.6 |
| 3796e63e-b0f0-3962-84e4-581b3e7e2261 | -4.7708 | -42.1365 | 2025-10-20 13:50:00 | GOES-19 | CAMPO MAIOR | PIAUÍ | Brasil | 2202208 | 22 | 33 | nan | nan | nan | Caatinga | 96.3 |
| aeffe439-8c14-33eb-b6e4-96bf9575fae5 | -11.3776 | -44.2663 | 2025-10-20 13:50:00 | GOES-19 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 130.9 |
| d56e92d3-1237-3a21-8085-fcb48513e5c9 | -14.206 | -51.5059 | 2025-10-20 13:50:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 91.7 |
| 6937dca6-cf63-344d-aab4-9b3602eb7ec6 | -14.2071 | -51.4416 | 2025-10-20 13:50:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 104.0 |
| 5b6308e6-908e-3830-bc76-dcf302e69444 | -14.2056 | -51.5273 | 2025-10-20 13:50:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 102.4 |
| 6322398e-0bde-347b-815e-16dcc8963816 | -6.3041 | -40.9076 | 2025-10-20 13:50:00 | GOES-19 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 99.9 |
| 45da40c7-ed2c-307e-909a-84464e4323a0 | -14.2071 | -51.4416 | 2025-10-20 14:00:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 87.1 |
| 0247ae5f-4bc1-3fdf-b31d-fb03341499c0 | -14.2457 | -51.4364 | 2025-10-20 14:00:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 187.6 |
| cec957e4-28a6-3911-82fc-c76c1dd9af3a | -14.2264 | -51.439 | 2025-10-20 14:00:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 118.9 |
| e475118d-2197-3504-a0e8-a983b0096ebc | -6.209 | -40.9894 | 2025-10-20 14:00:00 | GOES-19 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 110.7 |
| 62463155-bfb9-3ecb-baeb-c45e82d2acc5 | -14.4523 | -52.8961 | 2025-10-20 14:00:00 | GOES-19 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 104.6 |
| 5faec7ec-880e-3b3e-8cfb-6a86690f9487 | -6.1512 | -41.1161 | 2025-10-20 14:00:00 | GOES-19 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 121.3 |
| 155264c6-4276-333c-b036-1a84f2c031c3 | -14.4764 | -51.4909 | 2025-10-20 14:00:00 | GOES-19 | ARAGUAIANA | MATO GROSSO | Brasil | 5101001 | 51 | 33 | nan | nan | nan | Cerrado | 86.9 |
| 5f1cd737-8dd0-37bc-9ecd-bec559b4b83b | -6.1514 | -41.0918 | 2025-10-20 14:00:00 | GOES-19 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 88.1 |
| 5b44ec98-3aa1-3657-b341-6deeda8014fe | -6.2092 | -40.965 | 2025-10-20 14:00:00 | GOES-19 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 136.6 |
| 140c75f4-b778-3ea8-9735-0b29ca19d6b3 | -2.7236 | -48.8393 | 2025-10-20 14:00:00 | GOES-19 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 124.0 |
| a08324b4-2122-3929-8bfc-742fa4958d89 | -4.7708 | -42.1365 | 2025-10-20 14:00:00 | GOES-19 | CAMPO MAIOR | PIAUÍ | Brasil | 2202208 | 22 | 33 | nan | nan | nan | Caatinga | 100.3 |
| c303f61c-ea1a-3ff7-8f97-577dfd1cb299 | -14.1811 | -51.8293 | 2025-10-20 14:00:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 106.1 |
| f99cc7d3-91dd-386f-92e0-52e516481705 | -14.1815 | -51.808 | 2025-10-20 14:00:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 89.0 |
| 16c5e24a-5cd6-3717-bc16-1179e7da6f3f | -4.096 | -42.2496 | 2025-10-20 14:10:00 | GOES-19 | BATALHA | PIAUÍ | Brasil | 2201507 | 22 | 33 | nan | nan | nan | Caatinga | 91.6 |
| b7c95972-c886-3feb-9507-aa15b06e9485 | -4.7708 | -42.1365 | 2025-10-20 14:10:00 | GOES-19 | CAMPO MAIOR | PIAUÍ | Brasil | 2202208 | 22 | 33 | nan | nan | nan | Caatinga | 96.8 |
| bfc490c2-d67b-3171-8b46-c73809887eb9 | 1.7852 | -55.7042 | 2025-10-20 14:10:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 67.4 |
| 505c6152-b541-39d6-99c6-dc3493ef4cf8 | -6.209 | -40.9894 | 2025-10-20 14:10:00 | GOES-19 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 113.0 |
| ee961b0a-489e-3667-b331-e297a1cc206a | -6.2092 | -40.965 | 2025-10-20 14:10:00 | GOES-19 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 126.8 |
| b187c3b3-8b5c-31c4-b20e-4a7f24481ff8 | -14.4523 | -52.8961 | 2025-10-20 14:10:00 | GOES-19 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 90.1 |
| f6351e74-a86a-3876-b02e-b2e92b0c0838 | -14.4566 | -51.515 | 2025-10-20 14:10:00 | GOES-19 | ARAGUAIANA | MATO GROSSO | Brasil | 5101001 | 51 | 33 | nan | nan | nan | Cerrado | 92.0 |
| ed242f4d-e954-3c71-bcd1-08ef412cb6dd | -14.4764 | -51.4909 | 2025-10-20 14:10:00 | GOES-19 | ARAGUAIANA | MATO GROSSO | Brasil | 5101001 | 51 | 33 | nan | nan | nan | Cerrado | 87.7 |
| c0b9afd2-34db-3526-ada9-c7f379f548fc | -6.1512 | -41.1161 | 2025-10-20 14:10:00 | GOES-19 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 129.0 |
| c12c6afc-c0d7-36d1-8311-84fab891b2d9 | -14.4377 | -51.4961 | 2025-10-20 14:10:00 | GOES-19 | ARAGUAIANA | MATO GROSSO | Brasil | 5101001 | 51 | 33 | nan | nan | nan | Cerrado | 85.0 |
| 37bd54c2-f2f4-3ab0-bc78-5197b99f3c8c | -6.3542 | -41.5087 | 2025-10-20 14:10:00 | GOES-19 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 97.3 |
| 3ffe8277-50b6-3a8d-a5a2-cef483f9c4f9 | -2.7236 | -48.8393 | 2025-10-20 14:10:00 | GOES-19 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 129.4 |
| da1bd1f2-004e-31ae-8516-39772a7968c2 | -14.2071 | -51.4416 | 2025-10-20 14:10:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 96.9 |
| c81d9a4b-782e-33fe-bd53-1a8962fb3082 | -6.1514 | -41.0918 | 2025-10-20 14:10:00 | GOES-19 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 96.1 |
| 0cb37b1d-a9cd-32ea-a357-a7b3184f68f8 | -14.4764 | -51.4909 | 2025-10-20 14:20:00 | GOES-19 | ARAGUAIANA | MATO GROSSO | Brasil | 5101001 | 51 | 33 | nan | nan | nan | Cerrado | 93.6 |
| bde2095e-aa83-30ee-8dbe-dd157595e003 | -6.1514 | -41.0918 | 2025-10-20 14:20:00 | GOES-19 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 93.9 |
| 6ab5e5c6-64ad-3aca-bafd-380983129c48 | -14.1815 | -51.808 | 2025-10-20 14:20:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 91.0 |
| 3219fc70-2b07-355f-bebf-a66022ff4482 | -4.1712 | -42.1978 | 2025-10-20 14:20:00 | GOES-19 | BATALHA | PIAUÍ | Brasil | 2201507 | 22 | 33 | nan | nan | nan | Caatinga | 95.4 |
| dc31db50-9a7e-3eda-a9ea-e1187d41dd0a | -14.4523 | -52.8961 | 2025-10-20 14:20:00 | GOES-19 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 91.3 |
| 4484565c-dd95-3dcd-b042-135bd124b30f | 1.7852 | -55.7042 | 2025-10-20 14:20:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 76.9 |
| a7da20be-fabc-3aa4-aa5b-a3b96acfc4b3 | -14.4566 | -51.515 | 2025-10-20 14:20:00 | GOES-19 | ARAGUAIANA | MATO GROSSO | Brasil | 5101001 | 51 | 33 | nan | nan | nan | Cerrado | 93.2 |
| 1dc6dd2d-bd97-345b-acf9-a0886fc7a8a8 | -14.277 | -51.8593 | 2025-10-20 14:20:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 112.7 |
| 4b8a024e-b4ef-34e5-8f9b-d1d25e9285d6 | -14.2766 | -51.8807 | 2025-10-20 14:20:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 95.5 |
| badf2e34-dda3-33dc-8343-013fc10866da | -6.209 | -40.9894 | 2025-10-20 14:20:00 | GOES-19 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 115.3 |
| b21e8e20-58b6-3e1d-957c-710c0b1fe86c | -6.3542 | -41.5087 | 2025-10-20 14:20:00 | GOES-19 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 100.2 |
| 7c971cc9-82de-36c9-a8ee-8791526e5b1b | 1.8036 | -55.6842 | 2025-10-20 14:20:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 68.9 |
| 2c716e27-ea36-34b8-a03e-b5189edeb21b | 1.8035 | -55.7039 | 2025-10-20 14:20:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 67.0 |
| 63288aa2-dec7-3048-a5f3-64a8fe67a486 | -4.1525 | -42.1989 | 2025-10-20 14:30:00 | GOES-19 | BATALHA | PIAUÍ | Brasil | 2201507 | 22 | 33 | nan | nan | nan | Caatinga | 98.1 |
| d86fe130-bfa8-3f1f-a867-890bbb386e7b | 1.8219 | -55.6642 | 2025-10-20 14:30:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 69.8 |
| d6431b2a-63ba-30d3-8a8e-8d0333bae9a7 | -4.1845 | -42.9979 | 2025-10-20 14:30:00 | GOES-19 | COELHO NETO | MARANHÃO | Brasil | 2103406 | 21 | 33 | nan | nan | nan | Cerrado | 81.8 |
| 7a82fea8-a889-3fad-b533-24e86c1bf2f4 | -4.1526 | -42.1752 | 2025-10-20 14:30:00 | GOES-19 | BATALHA | PIAUÍ | Brasil | 2201507 | 22 | 33 | nan | nan | nan | Caatinga | 102.6 |
| 1dc7c67d-5858-3c79-ba15-da9c824ca41c | -14.4377 | -51.4961 | 2025-10-20 14:30:00 | GOES-19 | ARAGUAIANA | MATO GROSSO | Brasil | 5101001 | 51 | 33 | nan | nan | nan | Cerrado | 94.3 |
| 5e5f8674-ffd0-3087-9c20-e010ee0668ae | -14.1811 | -51.8293 | 2025-10-20 14:30:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 104.9 |
| 991c8af0-4926-3e16-92fd-f3d2605bdb82 | -14.4523 | -52.8961 | 2025-10-20 14:30:00 | GOES-19 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 87.5 |
| 788f5db9-12c8-3235-a6cc-80d619d4de0c | -14.1866 | -51.5085 | 2025-10-20 14:30:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 83.0 |
| 3520844b-6dce-3c04-bb7e-24097c4e9cba | -2.7236 | -48.8393 | 2025-10-20 14:30:00 | GOES-19 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 107.8 |
| 94d38be2-a5f5-3735-89b9-a95cbe4e1df6 | 1.8036 | -55.6842 | 2025-10-20 14:30:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 72.7 |
| 4a07a9cd-d41e-32ce-bc83-de4f2299e606 | -14.1815 | -51.808 | 2025-10-20 14:30:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 91.3 |
| 7e58cc10-a770-33b0-83c2-75358c463057 | -14.4764 | -51.4909 | 2025-10-20 14:30:00 | GOES-19 | ARAGUAIANA | MATO GROSSO | Brasil | 5101001 | 51 | 33 | nan | nan | nan | Cerrado | 95.8 |
| b47bc9ab-566c-3463-a2df-4b18d79b04c8 | 1.7852 | -55.7042 | 2025-10-20 14:40:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 73.1 |
| 5cf25c00-b5ca-39cb-908a-8c757e8a138f | -14.9045 | -52.4354 | 2025-10-20 14:40:00 | GOES-19 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 76.2 |
| b1db3fec-b337-3434-b77c-54f31d922444 | -4.171 | -42.2215 | 2025-10-20 14:40:00 | GOES-19 | BATALHA | PIAUÍ | Brasil | 2201507 | 22 | 33 | nan | nan | nan | Caatinga | 101.3 |
| af08a4bc-abfa-32a2-8bb2-fd98155d9d02 | -14.4523 | -52.8961 | 2025-10-20 14:40:00 | GOES-19 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 85.3 |
| b407f5cf-04a9-3344-a758-ea365d58336a | -2.7236 | -48.8393 | 2025-10-20 14:40:00 | GOES-19 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 96.1 |
| 27f7edf7-f61d-355d-aba8-0285d2c7b622 | -4.1525 | -42.1989 | 2025-10-20 14:40:00 | GOES-19 | BATALHA | PIAUÍ | Brasil | 2201507 | 22 | 33 | nan | nan | nan | Caatinga | 99.0 |
| 980d144c-0542-33d0-8e0b-dac19602f733 | -3.7626 | -41.7207 | 2025-10-20 14:40:00 | GOES-19 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 103.1 |
| 043d73c9-dde5-35fe-ae50-e61792989354 | -14.3223 | -51.4689 | 2025-10-20 14:40:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 80.2 |
| 6c9c59ac-ead5-3859-a4d4-dfb0622135cc | 1.6935 | -55.7843 | 2025-10-20 14:40:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 83.5 |
| be308b53-35b3-3c0a-bc4b-8d3806090681 | -4.1526 | -42.1752 | 2025-10-20 14:40:00 | GOES-19 | BATALHA | PIAUÍ | Brasil | 2201507 | 22 | 33 | nan | nan | nan | Caatinga | 102.8 |


