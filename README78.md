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
| fbf019c9-72c5-3daa-8c97-911a5b531918 | -8.866 | -40.4212 | 2024-11-20 13:00:00 | GOES-16 | PETROLINA | PERNAMBUCO | Brasil | 2611101 | 26 | 33 | nan | nan | nan | Caatinga | 120.5 |
| aa50b723-9771-370a-8102-3214f2de60cd | -8.8469 | -40.4237 | 2024-11-20 13:00:00 | GOES-16 | PETROLINA | PERNAMBUCO | Brasil | 2611101 | 26 | 33 | nan | nan | nan | Caatinga | 124.0 |
| 1f684bea-6ee3-3d2a-b774-e74e3930046e | -3.5921 | -42.0869 | 2024-11-20 13:00:00 | GOES-16 | JOAQUIM PIRES | PIAUÍ | Brasil | 2205409 | 22 | 33 | nan | nan | nan | Caatinga | 135.2 |
| 0e038d40-3a69-3159-8c46-bb8143b72c1b | -7.3137 | -37.2384 | 2024-11-20 13:00:00 | GOES-16 | ITAPETIM | PERNAMBUCO | Brasil | 2607703 | 26 | 33 | nan | nan | nan | Caatinga | 90.8 |
| 19a6419a-98a7-3a39-b5c7-68c92b89ab9c | -3.51 | -42.06 | 2024-11-20 13:00:00 | MSG-03 | JOAQUIM PIRES | PIAUÍ | Brasil | 2205409 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 84426dbd-f2b0-3e29-8190-34bd11bfb729 | -3.6 | -42.11 | 2024-11-20 13:00:00 | MSG-03 | JOAQUIM PIRES | PIAUÍ | Brasil | 2205409 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 2835c04f-f07b-3e51-b37e-f900d4cbb323 | -3.48 | -42.06 | 2024-11-20 13:00:00 | MSG-03 | JOAQUIM PIRES | PIAUÍ | Brasil | 2205409 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| c4ff6496-76e5-35cd-8523-7eda5ec6d9c2 | -3.5921 | -42.0869 | 2024-11-20 13:10:00 | GOES-16 | JOAQUIM PIRES | PIAUÍ | Brasil | 2205409 | 22 | 33 | nan | nan | nan | Caatinga | 85.4 |
| d69b96d8-3894-393b-805e-86d1a1b3896d | -7.1941 | -39.1301 | 2024-11-20 13:10:00 | GOES-16 | MISSÃO VELHA | CEARÁ | Brasil | 2308401 | 23 | 33 | nan | nan | nan | Caatinga | 85.6 |
| d3c67121-b7b7-3e23-b3d7-5b9d2eaaeecc | -2.9166 | -42.6607 | 2024-11-20 13:20:00 | GOES-16 | PAULINO NEVES | MARANHÃO | Brasil | 2108058 | 21 | 33 | nan | nan | nan | Cerrado | 89.0 |
| 890adff0-190b-38ae-99cf-e011bb975be0 | -7.1944 | -39.1048 | 2024-11-20 13:20:00 | GOES-16 | MISSÃO VELHA | CEARÁ | Brasil | 2308401 | 23 | 33 | nan | nan | nan | Caatinga | 169.9 |
| 4411febb-d708-369d-bd38-ce253ed3dec6 | -3.5174 | -42.0669 | 2024-11-20 13:20:00 | GOES-16 | JOAQUIM PIRES | PIAUÍ | Brasil | 2205409 | 22 | 33 | nan | nan | nan | Caatinga | 93.1 |
| e67cb6ca-0324-3e3b-9be2-2590f15cfa69 | -3.8181 | -41.8371 | 2024-11-20 13:20:00 | GOES-16 | SÃO JOSÉ DO DIVINO | PIAUÍ | Brasil | 2210052 | 22 | 33 | nan | nan | nan | Caatinga | 81.4 |
| c953adce-bc25-3e90-8005-1a0eb30ea10c | -3.7858 | -44.0622 | 2024-11-20 13:20:00 | GOES-16 | PIRAPEMAS | MARANHÃO | Brasil | 2108801 | 21 | 33 | nan | nan | nan | Cerrado | 73.5 |
| fc7ad7d2-f8d0-37dd-a49c-64d81a6b6882 | -8.8469 | -40.4237 | 2024-11-20 13:30:00 | GOES-16 | PETROLINA | PERNAMBUCO | Brasil | 2611101 | 26 | 33 | nan | nan | nan | Caatinga | 113.3 |
| 585b4ead-0dd4-3882-ac96-abd208855e1d | -7.1754 | -39.107 | 2024-11-20 13:30:00 | GOES-16 | MISSÃO VELHA | CEARÁ | Brasil | 2308401 | 23 | 33 | nan | nan | nan | Caatinga | 77.5 |
| 5a873b63-6926-39a9-a7a9-72ddcdaea128 | -7.1941 | -39.1301 | 2024-11-20 13:30:00 | GOES-16 | MISSÃO VELHA | CEARÁ | Brasil | 2308401 | 23 | 33 | nan | nan | nan | Caatinga | 115.5 |
| 479969d8-e809-3f81-bcf9-e8cc97f88a49 | -3.8181 | -41.8371 | 2024-11-20 13:30:00 | GOES-16 | SÃO JOSÉ DO DIVINO | PIAUÍ | Brasil | 2210052 | 22 | 33 | nan | nan | nan | Caatinga | 83.5 |
| 84538a0e-c03a-3937-bf07-9c77635dfb7f | -3.5174 | -42.0669 | 2024-11-20 13:30:00 | GOES-16 | JOAQUIM PIRES | PIAUÍ | Brasil | 2205409 | 22 | 33 | nan | nan | nan | Caatinga | 93.1 |
| 3a9c43fe-cdf3-38b7-be14-856aea52b469 | -3.3525 | -41.4781 | 2024-11-20 13:30:00 | GOES-16 | COCAL | PIAUÍ | Brasil | 2202703 | 22 | 33 | nan | nan | nan | Caatinga | 87.8 |
| 440f3fef-61d5-36b9-9fac-08e92f00172c | -3.7858 | -44.0622 | 2024-11-20 13:30:00 | GOES-16 | PIRAPEMAS | MARANHÃO | Brasil | 2108801 | 21 | 33 | nan | nan | nan | Cerrado | 73.0 |
| 600078fa-ffe7-38ce-9a51-aac7c1b08ade | -3.5545 | -42.1126 | 2024-11-20 13:30:00 | GOES-16 | JOAQUIM PIRES | PIAUÍ | Brasil | 2205409 | 22 | 33 | nan | nan | nan | Caatinga | 89.5 |
| 4e139f76-1f86-3cf4-baa6-b8a8c876468f | -1.1715 | -49.1268 | 2024-11-20 13:30:00 | GOES-16 | PONTA DE PEDRAS | PARÁ | Brasil | 1505700 | 15 | 33 | nan | nan | nan | Amazônia | 65.6 |
| 7a5fd5db-35c5-3dd6-83c4-242f52231df9 | -3.3525 | -41.4781 | 2024-11-20 13:40:00 | GOES-16 | COCAL | PIAUÍ | Brasil | 2202703 | 22 | 33 | nan | nan | nan | Caatinga | 81.4 |
| bbd30f60-1c3f-3e02-b542-66fe71add854 | -10.4196 | -44.4937 | 2024-11-20 13:40:00 | GOES-16 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 98.8 |
| 21528e9a-4027-38cd-9c7a-d7ec318b5abd | -10.4009 | -44.4731 | 2024-11-20 13:40:00 | GOES-16 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 94.9 |
| 0e8f7d00-c2b4-31ec-87d6-f7033fef0bce | -10.42 | -44.4705 | 2024-11-20 13:40:00 | GOES-16 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 78.4 |
| 7316936a-52fc-3990-8c6d-b52b00cc9326 | -3.3925 | -44.4239 | 2024-11-20 13:40:00 | GOES-16 | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Cerrado | 110.3 |
| e85df2c2-6219-31cb-a5e0-fab43c4a5e3d | -3.5174 | -42.0669 | 2024-11-20 13:40:00 | GOES-16 | JOAQUIM PIRES | PIAUÍ | Brasil | 2205409 | 22 | 33 | nan | nan | nan | Caatinga | 82.4 |
| 0fd72c10-b80a-38a8-8be4-8d287ccd01c8 | -3.5545 | -42.1126 | 2024-11-20 13:50:00 | GOES-16 | JOAQUIM PIRES | PIAUÍ | Brasil | 2205409 | 22 | 33 | nan | nan | nan | Caatinga | 78.3 |
| 8332fa70-f894-32c4-abf7-fcf9a5d5c5da | -4.0148 | -43.2408 | 2024-11-20 13:50:00 | GOES-16 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 81.7 |
| e018814f-b12a-38b1-a5e6-e5f30144b502 | -3.3925 | -44.4239 | 2024-11-20 13:50:00 | GOES-16 | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Cerrado | 79.8 |
| 7c7b9729-877b-3139-b664-20191f695429 | -10.4196 | -44.4937 | 2024-11-20 13:50:00 | GOES-16 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 123.0 |
| b9fe67ad-5d62-3178-aa71-7c595a6b4663 | -3.3525 | -41.4781 | 2024-11-20 13:50:00 | GOES-16 | COCAL | PIAUÍ | Brasil | 2202703 | 22 | 33 | nan | nan | nan | Caatinga | 83.0 |
| f9062182-7110-32c8-97a9-3559d764f8fd | -10.4009 | -44.4731 | 2024-11-20 13:50:00 | GOES-16 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 89.1 |
| b6153cf7-3a78-310f-97ce-cf4c67c441e8 | -3.7858 | -44.0622 | 2024-11-20 13:50:00 | GOES-16 | PIRAPEMAS | MARANHÃO | Brasil | 2108801 | 21 | 33 | nan | nan | nan | Cerrado | 76.1 |
| c4885408-3ff0-3521-bbc7-d4542e76b44f | -1.1715 | -49.1268 | 2024-11-20 13:50:00 | GOES-16 | PONTA DE PEDRAS | PARÁ | Brasil | 1505700 | 15 | 33 | nan | nan | nan | Amazônia | 72.1 |
| 9a0dc376-edb5-37d0-b29e-c250457cafec | -10.4009 | -44.4731 | 2024-11-20 14:00:00 | GOES-16 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 86.7 |
| 29875cf6-756a-324c-8d1b-3e74d695b1b9 | -4.0148 | -43.2408 | 2024-11-20 14:00:00 | GOES-16 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 81.5 |
| 26e6543b-dbd4-370f-af68-99cc9d855ca1 | -7.1941 | -39.1301 | 2024-11-20 14:00:00 | GOES-16 | MISSÃO VELHA | CEARÁ | Brasil | 2308401 | 23 | 33 | nan | nan | nan | Caatinga | 74.0 |
| 33db66b0-8eeb-3b03-af24-13e3a02b5b65 | -22.1631 | -54.8758 | 2024-11-20 14:00:00 | GOES-16 | ITAPORÃ | MATO GROSSO DO SUL | Brasil | 5004502 | 50 | 33 | nan | nan | nan | Mata Atlântica | 97.9 |
| f95bbef2-6f5e-3e98-9527-e770c0112079 | -1.2017 | -53.6769 | 2024-11-20 14:00:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 80.7 |
| 61a02c46-c683-34c9-b3ac-bf04fdfa92ed | -3.7858 | -44.0622 | 2024-11-20 14:00:00 | GOES-16 | PIRAPEMAS | MARANHÃO | Brasil | 2108801 | 21 | 33 | nan | nan | nan | Cerrado | 75.1 |
| 61d9f34d-a48d-3ef5-b9eb-dc27510b53ec | -3.5174 | -42.0669 | 2024-11-20 14:00:00 | GOES-16 | JOAQUIM PIRES | PIAUÍ | Brasil | 2205409 | 22 | 33 | nan | nan | nan | Caatinga | 75.5 |
| 24914ddf-7ae1-3978-839d-e774b8cfb9eb | -10.4196 | -44.4937 | 2024-11-20 14:00:00 | GOES-16 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 109.4 |
| 2daf26ff-1e69-33af-a489-7e5dcb70e36c | -10.4196 | -44.4937 | 2024-11-20 14:10:00 | GOES-16 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 94.5 |
| 407d7118-8e69-3d59-a2ae-9f4a106247ea | -1.2017 | -53.6769 | 2024-11-20 14:10:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 80.3 |
| e88d5b61-7cce-362f-b330-28af7df2f154 | -10.4009 | -44.4731 | 2024-11-20 14:10:00 | GOES-16 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 106.2 |
| adf9863a-1529-32d7-b669-a13f72f6fe9d | -4.0148 | -43.2408 | 2024-11-20 14:10:00 | GOES-16 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 88.3 |
| 8385a60c-6c4c-3365-bc50-966831ab6aeb | -10.7235 | -49.5265 | 2024-11-20 14:10:00 | GOES-16 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 218.3 |
| ea94a8ce-6459-32cc-84a2-65f0e7e650bc | -3.3986 | -43.2714 | 2024-11-20 14:10:00 | GOES-16 | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 82.6 |
| 352c5430-1e30-33b7-a5a1-ef45cac9b523 | -1.2017 | -53.6769 | 2024-11-20 14:20:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 73.1 |
| 09d9cb30-d8e6-3236-825a-143a459edf5b | -10.7235 | -49.5265 | 2024-11-20 14:20:00 | GOES-16 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 187.3 |
| 45a9946f-235c-3fe9-ae73-4a50bdcd9d61 | -10.4196 | -44.4937 | 2024-11-20 14:20:00 | GOES-16 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 101.0 |
| bb2a674c-7806-3d80-a4be-a476144f49b8 | -3.8111 | -42.948 | 2024-11-20 14:20:00 | GOES-16 | BURITI | MARANHÃO | Brasil | 2102200 | 21 | 33 | nan | nan | nan | Cerrado | 78.4 |
| f267d75d-fade-3dcb-9255-eedeabda479d | -6.9236 | -42.8144 | 2024-11-20 14:20:00 | GOES-16 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 52.1 |
| fe851f49-a758-3550-9b1a-16aa430fcbd8 | -10.4009 | -44.4731 | 2024-11-20 14:20:00 | GOES-16 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 87.2 |
| 92ce2c1b-28cc-3c55-8c32-5c2bad51be96 | -1.1715 | -49.1481 | 2024-11-20 14:30:00 | GOES-16 | PONTA DE PEDRAS | PARÁ | Brasil | 1505700 | 15 | 33 | nan | nan | nan | Amazônia | 76.7 |
| 3d0c5174-7280-3e5c-81e4-a1af8c164e9d | -1.1715 | -49.1268 | 2024-11-20 14:30:00 | GOES-16 | PONTA DE PEDRAS | PARÁ | Brasil | 1505700 | 15 | 33 | nan | nan | nan | Amazônia | 67.1 |
| 046e5d2e-33d1-3f5c-997d-094457b4bc15 | -10.4009 | -44.4731 | 2024-11-20 14:30:00 | GOES-16 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 81.8 |
| 17858a08-e055-32d5-8485-06c3afbb09c9 | -10.4196 | -44.4937 | 2024-11-20 14:30:00 | GOES-16 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 94.0 |
| c03954cf-6a6c-3888-ba5b-e9e14a734283 | -10.7235 | -49.5265 | 2024-11-20 14:30:00 | GOES-16 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 229.8 |
| 48ef4b47-1dd7-3bb2-ba67-c0d5a05fa859 | -1.2017 | -53.6769 | 2024-11-20 14:30:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 80.7 |
| 69fc816d-44d3-3c6a-80af-baf37894702f | -1.2017 | -53.6769 | 2024-11-20 14:40:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 90.2 |
| 40274633-ece5-3248-8473-3f999aaeae48 | -10.4009 | -44.4731 | 2024-11-20 14:40:00 | GOES-16 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 73.6 |
| 2dbe3b78-8606-36cc-98c6-03eba35704b1 | -12.2653 | -44.9927 | 2024-11-20 14:40:00 | GOES-16 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 82.3 |
| acaccb9b-a30f-3207-b184-aae7d9d00295 | -10.4196 | -44.4937 | 2024-11-20 14:40:00 | GOES-16 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 113.6 |


