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

## Dados Diários - Página 13

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 3f09f3f4-bbd9-3f1b-ad5b-abf2e5969bb7 | -3.6593 | -50.439 | 2024-11-18 02:20:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 49.5 |
| 68ed8654-5094-32cb-be14-aa1fb02fceca | -3.1461 | -45.3404 | 2024-11-18 02:20:00 | GOES-16 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 90.4 |
| 685ccf96-e659-3352-a487-42e8e7f08629 | -3.146 | -45.3629 | 2024-11-18 02:20:00 | GOES-16 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 70.6 |
| f056b672-5c7f-376c-961d-21bf02a4b82a | -2.5073 | -47.2461 | 2024-11-18 02:20:00 | GOES-16 | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 95.5 |
| 56e02602-fe33-3104-833a-fc160c57b82f | -2.8608 | -51.7731 | 2024-11-18 02:20:00 | GOES-16 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 61.0 |
| da93e9c6-5115-3ce9-8581-005d1c47b492 | -1.2964 | -51.7616 | 2024-11-18 02:20:00 | GOES-16 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 66.5 |
| 69effde0-7622-3358-b843-b86dd2f16579 | -2.8607 | -51.7937 | 2024-11-18 02:20:00 | GOES-16 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 84.9 |
| 1d9083e6-fb69-352c-b6a4-c0da45e51119 | -1.6962 | -45.8311 | 2024-11-18 02:20:00 | GOES-16 | CÂNDIDO MENDES | MARANHÃO | Brasil | 2102606 | 21 | 33 | nan | nan | nan | Amazônia | 170.9 |
| 89b2030b-f2cf-332f-a3b7-c3f1d6171669 | -1.3148 | -51.7408 | 2024-11-18 02:20:00 | GOES-16 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 188.4 |
| c49f9f40-98a6-33ec-bbce-baa5f03a4401 | -3.0542 | -54.4081 | 2024-11-18 02:20:00 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 55.2 |
| 9fae6204-4b5e-3488-837f-40954d2f4f1e | -2.5847 | -51.7181 | 2024-11-18 02:20:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 83.2 |
| 5d214756-6101-3a39-bc15-4c82782298dd | -2.5074 | -47.2242 | 2024-11-18 02:20:00 | GOES-16 | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 65.1 |
| a081c1d3-958c-3247-9b6f-06bf33e88f12 | -1.2964 | -51.741 | 2024-11-18 02:20:00 | GOES-16 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 194.6 |
| 01ee4a10-2727-3f20-8fc7-72aec86716bf | -2.5073 | -47.2461 | 2024-11-18 02:30:00 | GOES-16 | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 84.4 |
| 9c8de68f-889e-32d8-abab-1344cbbd4cfc | -3.3267 | -50.4923 | 2024-11-18 02:30:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 37.2 |
| dde73e22-d43c-39c2-8b5c-8b3d79aae61e | -1.7147 | -45.8307 | 2024-11-18 02:30:00 | GOES-16 | CÂNDIDO MENDES | MARANHÃO | Brasil | 2102606 | 21 | 33 | nan | nan | nan | Amazônia | 133.2 |
| 26347db3-cc60-3399-b38a-82e127b421f5 | -3.6593 | -50.439 | 2024-11-18 02:30:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 51.0 |
| 41aade28-d06a-3feb-a34b-e66c96ea3c73 | -2.5847 | -51.7181 | 2024-11-18 02:30:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 70.3 |
| 5df7e97d-2c02-3bf1-ad29-74e876835af4 | -1.3148 | -51.7614 | 2024-11-18 02:30:00 | GOES-16 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 56.5 |
| 9484a197-7700-3b9f-b7bf-180bde9551cb | -1.2964 | -51.7616 | 2024-11-18 02:30:00 | GOES-16 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 62.9 |
| d236f628-7758-3429-8910-9e9d147ebd00 | -1.2964 | -51.7204 | 2024-11-18 02:30:00 | GOES-16 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 62.7 |
| cbb8132e-bbb7-3100-9648-2fc3f6e62700 | -2.8607 | -51.7937 | 2024-11-18 02:30:00 | GOES-16 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 46.1 |
| 200aff9f-c181-3f0a-a884-a1fdb2d77caa | -2.8791 | -51.7932 | 2024-11-18 02:30:00 | GOES-16 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 41.6 |
| b700d533-c478-32a2-93df-b351a2d083f2 | -1.3148 | -51.7408 | 2024-11-18 02:30:00 | GOES-16 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 136.2 |
| 83ca7796-8663-3a57-8651-042ded56a974 | -4.5869 | -44.2255 | 2024-11-18 02:30:00 | GOES-16 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 112.9 |
| f8db9516-623d-36bf-8192-68fff2861349 | -1.6962 | -45.8311 | 2024-11-18 02:30:00 | GOES-16 | CÂNDIDO MENDES | MARANHÃO | Brasil | 2102606 | 21 | 33 | nan | nan | nan | Amazônia | 141.8 |
| a2981b23-d300-3452-ae3f-585a2028d0a5 | -1.2964 | -51.741 | 2024-11-18 02:30:00 | GOES-16 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 189.7 |
| 00e0ae7a-a6b3-3c41-9f5d-6cf960cb3005 | -3.4015 | -50.2801 | 2024-11-18 02:30:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 41.9 |
| c91492b1-97b4-3f9d-8bca-24b2091251e8 | -3.0542 | -54.4081 | 2024-11-18 02:30:00 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 55.1 |
| 16de70d3-f55a-3bbe-ac10-4c5e0911f242 | -2.5847 | -51.7181 | 2024-11-18 02:40:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 63.7 |
| 4804ec78-6286-3eda-b5c6-805a4bcf17c6 | -3.4015 | -50.2801 | 2024-11-18 02:40:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 36.6 |
| e0aef06a-73ff-3516-b4c6-07d513339722 | -2.8607 | -51.7937 | 2024-11-18 02:40:00 | GOES-16 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 34.9 |
| 4a061b21-7b89-345f-98b7-04c9d465941a | -3.0542 | -54.4081 | 2024-11-18 02:40:00 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 54.9 |
| 2b5f44fd-43d5-3fc1-b647-9cb3b8715c01 | -1.2964 | -51.7616 | 2024-11-18 02:40:00 | GOES-16 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 69.3 |
| 8c935d51-ad43-37e8-8a14-05d806cc72c1 | -1.6962 | -45.8311 | 2024-11-18 02:40:00 | GOES-16 | CÂNDIDO MENDES | MARANHÃO | Brasil | 2102606 | 21 | 33 | nan | nan | nan | Amazônia | 95.2 |
| a65a7e90-08a1-39c0-88f7-1e1ee724ae7c | -1.2964 | -51.741 | 2024-11-18 02:40:00 | GOES-16 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 197.5 |
| edc8977c-377e-30aa-a06d-61c6433b9d31 | -1.2964 | -51.7204 | 2024-11-18 02:40:00 | GOES-16 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 65.8 |
| 83b2db6e-2fc3-387a-a1fe-2debf38c1c98 | -1.7147 | -45.8307 | 2024-11-18 02:40:00 | GOES-16 | CÂNDIDO MENDES | MARANHÃO | Brasil | 2102606 | 21 | 33 | nan | nan | nan | Amazônia | 157.6 |
| 105ef736-ca73-3a94-b6f5-b99919bab8e5 | -1.3148 | -51.7408 | 2024-11-18 02:40:00 | GOES-16 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 96.8 |
| 6a11adec-852e-3d5a-80b5-2dbf0218f339 | -2.8791 | -51.7932 | 2024-11-18 02:40:00 | GOES-16 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 36.5 |
| 05467f47-41d7-360f-bd7b-f40ea08eee82 | -4.5869 | -44.2255 | 2024-11-18 02:40:00 | GOES-16 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 108.1 |
| 25bb0643-8733-3140-8b32-192a64355ce1 | -5.1462 | -44.351 | 2024-11-18 02:50:00 | GOES-16 | PRESIDENTE DUTRA | MARANHÃO | Brasil | 2109106 | 21 | 33 | nan | nan | nan | Cerrado | 78.1 |
| 85f263b3-f5b6-3148-8f94-1cfaa8ec857c | -1.3148 | -51.7408 | 2024-11-18 02:50:00 | GOES-16 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 104.3 |
| 081a8535-64e3-372f-ba8b-eabc0c2db65c | -1.2964 | -51.741 | 2024-11-18 02:50:00 | GOES-16 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 173.5 |
| 36691d4e-9dac-3fad-b122-a06e601c82a2 | -2.5847 | -51.7181 | 2024-11-18 02:50:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 36.2 |
| f71191fd-e944-3887-89d4-cfaf1b9ee543 | -4.5869 | -44.2255 | 2024-11-18 02:50:00 | GOES-16 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 75.9 |
| 6642d8fb-8cb9-3487-9a83-65f0b56902f6 | -1.6962 | -45.8311 | 2024-11-18 02:50:00 | GOES-16 | CÂNDIDO MENDES | MARANHÃO | Brasil | 2102606 | 21 | 33 | nan | nan | nan | Amazônia | 108.6 |
| 4670e382-fbfb-3c16-9990-e56c5aa85a24 | -1.7147 | -45.8307 | 2024-11-18 02:50:00 | GOES-16 | CÂNDIDO MENDES | MARANHÃO | Brasil | 2102606 | 21 | 33 | nan | nan | nan | Amazônia | 106.9 |
| d631ddd2-752c-3215-bcaf-101f01892d38 | -2.8607 | -51.7937 | 2024-11-18 02:50:00 | GOES-16 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 36.1 |
| 45032bca-74ba-32bf-82fc-a329be80b9ea | -2.8791 | -51.7932 | 2024-11-18 02:50:00 | GOES-16 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 45.0 |
| 6969c76d-214d-3401-9a89-efd49e2a105e | -3.0542 | -54.4081 | 2024-11-18 02:50:00 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 55.1 |
| 019b9b71-b235-3bd8-8326-cbfdf6fac400 | -1.2964 | -51.7616 | 2024-11-18 02:50:00 | GOES-16 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 63.0 |
| 5334e291-ca00-3530-b982-2ed66651d48e | -3.0542 | -54.4081 | 2024-11-18 03:00:00 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 53.0 |
| 5bdefe96-99bc-3eee-a986-28744cf7cfaf | -2.8791 | -51.7932 | 2024-11-18 03:00:00 | GOES-16 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 42.7 |
| e6ca84c8-f835-3623-a36a-d5d140fbddf6 | -1.2964 | -51.7616 | 2024-11-18 03:00:00 | GOES-16 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 57.8 |
| 7124d3b0-7b0c-391a-8a38-febcb7638dd3 | -1.6962 | -45.8311 | 2024-11-18 03:00:00 | GOES-16 | CÂNDIDO MENDES | MARANHÃO | Brasil | 2102606 | 21 | 33 | nan | nan | nan | Amazônia | 84.4 |
| 01f718d8-b4f2-356c-900e-f613e38f9859 | -1.7147 | -45.8307 | 2024-11-18 03:00:00 | GOES-16 | CÂNDIDO MENDES | MARANHÃO | Brasil | 2102606 | 21 | 33 | nan | nan | nan | Amazônia | 100.4 |
| 66ef31bd-7715-3fd8-9646-c68caae3763b | -1.2964 | -51.741 | 2024-11-18 03:00:00 | GOES-16 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 176.4 |
| 32d77175-fcee-3d6b-8097-ea29148b7e53 | -1.3148 | -51.7408 | 2024-11-18 03:00:00 | GOES-16 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 90.4 |
| 1e385edb-de12-38d7-a34e-7e834c9f9c98 | -2.8607 | -51.7937 | 2024-11-18 03:00:00 | GOES-16 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 37.4 |
| 8f83beef-e311-3ae2-8bc3-f7e48e6d34ca | -1.2964 | -51.7204 | 2024-11-18 03:00:00 | GOES-16 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 52.1 |
| a4bad4e3-c960-3e7a-a803-a8bb2bb12321 | -17.626 | -57.5692 | 2024-11-18 03:10:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 91.2 |
| 35a238cd-2f7b-3968-a237-e92a0646ed7c | -1.3148 | -51.7614 | 2024-11-18 03:10:00 | GOES-16 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 44.5 |
| 6b1a97b0-0581-3f62-950f-b50bb0d3c039 | -1.2964 | -51.741 | 2024-11-18 03:10:00 | GOES-16 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 161.4 |
| ecb0711a-559b-37fe-a572-3e7ba31f278e | -1.7147 | -45.8307 | 2024-11-18 03:10:00 | GOES-16 | CÂNDIDO MENDES | MARANHÃO | Brasil | 2102606 | 21 | 33 | nan | nan | nan | Amazônia | 102.3 |
| 06a5f088-de3d-3edd-ae0b-d9992eeb4fc9 | -1.2964 | -51.7204 | 2024-11-18 03:10:00 | GOES-16 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 53.9 |
| 0bd0fc37-df85-3a40-994b-b285c378f6f6 | -1.3148 | -51.7408 | 2024-11-18 03:10:00 | GOES-16 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 88.3 |
| 046e425c-2e2f-3d75-9913-60988c7209d9 | -3.0542 | -54.4081 | 2024-11-18 03:10:00 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 51.0 |
| b9b0f330-49a7-38aa-a9a0-627b5a4da66d | -17.6059 | -57.5921 | 2024-11-18 03:10:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 61.2 |
| 7643a213-7a62-38aa-9a2d-4698fd6eb969 | -1.2964 | -51.7616 | 2024-11-18 03:10:00 | GOES-16 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 68.2 |
| d3fce848-a7b2-38c4-8fa7-a7b37b848014 | -17.6256 | -57.5897 | 2024-11-18 03:10:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 60.4 |
| f049a85a-5aa1-3f31-8790-faa0eb8a6df5 | -17.6063 | -57.5715 | 2024-11-18 03:10:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 88.9 |
| 1a9ed7f1-90c5-3c05-983a-890dd669229b | -2.8607 | -51.7937 | 2024-11-18 03:10:00 | GOES-16 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 45.7 |
| f4aa55e6-f9f7-3f64-a05e-9e3ca606f3ea | -2.5847 | -51.7181 | 2024-11-18 03:10:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 32.8 |
| 603f74a0-b2e7-3c67-83a4-3b97032b2cc7 | -2.8791 | -51.7932 | 2024-11-18 03:10:00 | GOES-16 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 38.8 |
| 3bd70b78-f3e3-36de-9378-b9caaacfb23f | -1.2964 | -51.741 | 2024-11-18 03:20:00 | GOES-16 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 171.3 |
| e678855c-3dc1-3fbe-adce-f4d3bd437f8f | -17.6059 | -57.5921 | 2024-11-18 03:20:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 62.6 |
| 7dcc8316-7283-3803-a2f6-563f400c8a2b | -2.8791 | -51.7932 | 2024-11-18 03:20:00 | GOES-16 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 32.3 |
| bd92e015-5cb0-3b3f-8f83-824ce2198fda | -3.0542 | -54.4081 | 2024-11-18 03:20:00 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 49.6 |
| 6d128a8d-8888-37e5-a650-e42fa838d174 | -1.6962 | -45.8311 | 2024-11-18 03:20:00 | GOES-16 | CÂNDIDO MENDES | MARANHÃO | Brasil | 2102606 | 21 | 33 | nan | nan | nan | Amazônia | 68.4 |
| e495fa80-a933-3224-b8d4-67e3eef03538 | -3.3267 | -50.4923 | 2024-11-18 03:20:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 35.5 |
| d0bbd913-01bf-381d-9396-30ac9ecf6d53 | -1.2964 | -51.7204 | 2024-11-18 03:20:00 | GOES-16 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 44.8 |
| fc6e9138-6c0a-325c-8925-ab2b4f706795 | -2.8607 | -51.7937 | 2024-11-18 03:20:00 | GOES-16 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 32.1 |
| 310c9411-8ead-3e82-9dc6-21af314442a8 | -2.5847 | -51.7181 | 2024-11-18 03:20:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 32.9 |
| 9a942268-0ed9-36fa-ad29-bc4235bd4384 | -1.2964 | -51.7616 | 2024-11-18 03:20:00 | GOES-16 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 59.4 |
| 8aaaa061-2987-3b7b-96d2-fcfa75d15c45 | -17.6063 | -57.5715 | 2024-11-18 03:20:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 100.1 |
| 51995a97-6abf-3469-b389-c8326f043962 | -1.3148 | -51.7408 | 2024-11-18 03:20:00 | GOES-16 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 121.7 |
| abcfbc6c-528e-3062-8ac9-e26c1f43e445 | -17.626 | -57.5692 | 2024-11-18 03:20:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 92.8 |
| 4eec5163-143f-3fe0-94b8-4a08935ed555 | -17.6256 | -57.5897 | 2024-11-18 03:20:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 60.6 |
| f572c18e-7c4f-3942-9473-e21be27c1285 | -1.3148 | -51.7614 | 2024-11-18 03:20:00 | GOES-16 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 44.1 |
| 819a38f5-07c8-3028-b15d-62781a640f32 | -4.78586 | -40.40596 | 2024-11-18 03:23:00 | NOAA-21 | TAMBORIL | CEARÁ | Brasil | 2313203 | 23 | 33 | nan | nan | nan | Caatinga | 4.2 |
| 0d8b582a-0e83-3ef9-9ad4-540cc2bca259 | -6.42941 | -35.25179 | 2024-11-18 03:23:00 | NOAA-21 | PEDRO VELHO | RIO GRANDE DO NORTE | Brasil | 2409803 | 24 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 60aa89be-9fcc-38af-a472-f420a24a3b10 | -4.79822 | -37.38834 | 2024-11-18 03:23:00 | NOAA-21 | ARACATI | CEARÁ | Brasil | 2301109 | 23 | 33 | nan | nan | nan | Caatinga | 2.3 |
| f3c8f680-0ab6-3c39-b539-9ad7847b47e0 | -4.90933 | -44.02765 | 2024-11-18 03:23:00 | NOAA-21 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 17.7 |
| 01c0539e-a7d2-302d-980a-d9f51fbc50f7 | -6.7426 | -35.42903 | 2024-11-18 03:23:00 | NOAA-21 | SERTÃOZINHO | PARAÍBA | Brasil | 2515930 | 25 | 33 | nan | nan | nan | Caatinga | 3.8 |
| 11bb67ee-8f8b-37b7-a5f9-e3ba29ff529a | -4.91206 | -44.0279 | 2024-11-18 03:23:00 | NOAA-21 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 5.8 |
| e396537d-23d5-39a4-966b-15c5224c11ee | -6.66775 | -34.97638 | 2024-11-18 03:23:00 | NOAA-21 | BAÍA DA TRAIÇÃO | PARAÍBA | Brasil | 2501401 | 25 | 33 | nan | nan | nan | Mata Atlântica | 5.7 |
| d0688904-399b-31be-92e2-23385d5b0581 | -6.05138 | -39.43759 | 2024-11-18 03:23:00 | NOAA-21 | ACOPIARA | CEARÁ | Brasil | 2300309 | 23 | 33 | nan | nan | nan | Caatinga | 0.9 |
| bc42acd8-414b-33a3-9ee3-798e899e961f | -6.73787 | -35.4304 | 2024-11-18 03:23:00 | NOAA-21 | SERTÃOZINHO | PARAÍBA | Brasil | 2515930 | 25 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 7aaa8887-dcec-336d-9e0b-c0ddf036f881 | -4.78653 | -40.40202 | 2024-11-18 03:23:00 | NOAA-21 | TAMBORIL | CEARÁ | Brasil | 2313203 | 23 | 33 | nan | nan | nan | Caatinga | 4.0 |


[Clique aqui para ver as próximas entradas](README14.md)
