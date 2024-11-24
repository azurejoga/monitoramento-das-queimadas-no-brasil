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

## Dados Diários - Página 79

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| c94b384b-2ff1-38f0-a879-2db64a99ff53 | -4.637 | -48.83969 | 2024-11-24 05:16:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 1d5ddb56-193e-3e68-8853-1a9a8fe5b19a | -3.24734 | -54.2326 | 2024-11-24 05:16:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| d60c5fb5-23b6-3447-893c-c09421f5fabd | -3.24593 | -54.24165 | 2024-11-24 05:16:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 3443e879-ea01-3595-a9a5-ad4264d15923 | -3.91465 | -50.57179 | 2024-11-24 05:16:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 9575ec03-77dd-3702-be17-c6b2ec47528e | -4.24103 | -48.70876 | 2024-11-24 05:16:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 615fb74c-203b-34d3-b47e-98a35dc3200e | -3.82492 | -52.41359 | 2024-11-24 05:16:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 7.4 |
| d69ea48a-4bc4-34e6-89fa-f2e511b9f569 | -4.16161 | -54.57891 | 2024-11-24 05:16:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 0f494fec-71b3-3d70-bfbb-2c24d78baf78 | -3.53104 | -52.98635 | 2024-11-24 05:16:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 6e5ac2a1-025c-357f-b0f1-0a208d68ae50 | -4.63478 | -46.87234 | 2024-11-24 05:16:00 | NPP-375D | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 79a68318-eded-3b32-9fdb-3b7846921fa6 | -3.62993 | -52.25101 | 2024-11-24 05:16:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 385c2a3d-69a6-3e76-b360-7f0678d2315f | -4.37284 | -49.75071 | 2024-11-24 05:16:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 8243c140-96be-39ae-bee8-b8ab16ed4a45 | -3.70815 | -51.79276 | 2024-11-24 05:16:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 49c9b4de-62da-3235-bf73-209edb509cdf | -4.38347 | -55.07398 | 2024-11-24 05:16:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 9548e65c-701e-363b-99ea-6d462f0b1193 | -3.89072 | -50.07072 | 2024-11-24 05:16:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 5584188c-fb3b-39b5-8145-45469c27c2e9 | -3.50237 | -53.80068 | 2024-11-24 05:16:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 2fdf2dd9-3aed-316b-ae9e-6ae7cdd4a36a | -3.80648 | -51.2663 | 2024-11-24 05:16:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 0bb55926-2f32-30b3-9138-b2f62438db9e | -6.63714 | -47.34505 | 2024-11-24 05:16:00 | NPP-375D | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 78132522-52f3-3348-8cfb-e2342a52d7d1 | -3.52409 | -53.78881 | 2024-11-24 05:16:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 378cfeea-7315-3368-8f24-636e117d4a11 | -3.24216 | -54.24107 | 2024-11-24 05:16:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 3349ba39-f35f-3cc4-929e-b89d33a002a2 | -4.2183 | -50.40362 | 2024-11-24 05:16:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| abe7420f-1475-3f17-825c-ee2877c03a55 | -3.18599 | -54.77127 | 2024-11-24 05:16:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 49a722f3-7fed-3f03-a3d6-ab1e65fcd925 | -4.23654 | -48.70055 | 2024-11-24 05:16:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 9446b7de-7e6b-3891-939d-06957b653483 | -3.51576 | -53.81705 | 2024-11-24 05:16:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 13.1 |
| 503aa28c-28aa-3b88-b59c-332fb0bccf89 | -3.32651 | -53.85548 | 2024-11-24 05:16:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 0cd46b39-219f-37d4-b379-4ec3e18dfe40 | -4.40798 | -49.65371 | 2024-11-24 05:16:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| b127946b-cd9a-3360-ba26-7b93c17fa85c | -5.19261 | -49.15517 | 2024-11-24 05:16:00 | NPP-375D | NOVA IPIXUNA | PARÁ | Brasil | 1504976 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 5724da72-425e-36f2-bf89-08a3d58aee6b | -3.89428 | -50.07173 | 2024-11-24 05:16:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| dc06e783-d8f0-3a48-bc26-c2778c45de2a | -4.85162 | -50.80577 | 2024-11-24 05:16:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 484bd749-18e6-31ad-8b20-5c201d4a8397 | -3.83168 | -55.6866 | 2024-11-24 05:16:00 | NPP-375D | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| dc286534-f6ad-3e84-a1b7-d43cfba18926 | -4.2411 | -48.6293 | 2024-11-24 05:16:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| c66e694e-d864-3705-b8a9-548345b3d1be | -3.25253 | -54.22407 | 2024-11-24 05:16:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 3ab47a0a-c00e-3fe1-b2da-c8fdf807781b | -3.24286 | -54.23658 | 2024-11-24 05:16:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 8de2d2aa-6f33-3065-aca1-8871e42de123 | -4.24712 | -48.70591 | 2024-11-24 05:16:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 103c0800-dad1-3606-8ceb-27606c858022 | -4.23707 | -48.69686 | 2024-11-24 05:16:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 2caac9c8-79cc-3f40-8a33-5c7d2182b379 | -4.52669 | -46.42466 | 2024-11-24 05:16:00 | NPP-375D | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 0e9c9bdb-31d7-3916-b707-91d434bcf212 | -3.71945 | -51.31167 | 2024-11-24 05:16:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| a3f058fa-2a8a-3aff-aead-df5b9fcda166 | -3.2504 | -54.23777 | 2024-11-24 05:16:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| a0788307-dc61-3681-a58f-af30edc8d151 | -3.24428 | -54.22746 | 2024-11-24 05:16:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 46e57a39-0f5f-38d4-9ebb-acfbf50340ab | -5.1975 | -49.15307 | 2024-11-24 05:16:00 | NPP-375D | NOVA IPIXUNA | PARÁ | Brasil | 1504976 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c9e37bf5-a1d2-3dbc-8481-cab16e471551 | -4.02644 | -54.63286 | 2024-11-24 05:16:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| face5521-9a48-3038-a5b8-c50e1dc8a576 | -3.45542 | -60.39683 | 2024-11-24 05:16:00 | NPP-375D | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 89ba35a9-6cc4-3b22-a958-b34937533655 | -5.58511 | -45.20815 | 2024-11-24 05:16:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| d9f9e700-5d9c-3722-be86-94872dcf0ba4 | -4.10017 | -51.07348 | 2024-11-24 05:16:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 25f19356-70c0-3d65-803c-ec22c2c7a9fc | -4.51807 | -45.72537 | 2024-11-24 05:16:00 | NPP-375D | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| be16a501-6a5f-3e36-8e3f-a951dcfa6564 | -3.52662 | -53.50928 | 2024-11-24 05:16:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 35c3a5f3-8424-33a5-9877-14d0f0b2a142 | -3.5126 | -53.81171 | 2024-11-24 05:16:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| c5a49d30-6ea0-39ed-89d1-580f9436df5a | -4.37829 | -50.46308 | 2024-11-24 05:16:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 327e4180-a8b1-3a85-be58-9af9d3247c51 | -6.87165 | -51.98847 | 2024-11-24 05:16:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 0fc93a3a-4e29-3457-a2b6-93223a02ac19 | -3.5753 | -54.68343 | 2024-11-24 05:16:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 12b879b0-3fc7-3411-b651-fb19449fca40 | -4.23601 | -48.70425 | 2024-11-24 05:16:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 3c96644e-f50a-30a4-9bab-1ee93daa8244 | -3.25631 | -54.22465 | 2024-11-24 05:16:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 66a98d6c-065c-3c3d-b395-99123adffb8b | -3.1848 | -54.7735 | 2024-11-24 05:16:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| e0f04f2a-47b8-380d-bfe2-152129806c3a | -3.24805 | -54.22803 | 2024-11-24 05:16:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| b9ccda01-698b-3528-9e4f-4b76c9def053 | -2.55672 | -59.85554 | 2024-11-24 05:16:00 | NPP-375D | RIO PRETO DA EVA | AMAZONAS | Brasil | 1303569 | 13 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 0276ffd2-6bf6-3b8e-9814-27b79ca80f95 | -3.67136 | -51.73353 | 2024-11-24 05:16:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| f22939ae-67bc-3d76-9531-c3b3a4bab8f1 | -3.81597 | -52.00104 | 2024-11-24 05:16:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 2cf03913-1d61-337c-bb1e-f98664013e14 | -4.9367 | -50.61426 | 2024-11-24 05:16:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 89776051-36f1-35fa-a611-9dcc541f2de7 | -3.49568 | -54.02375 | 2024-11-24 05:16:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| eacab31a-dc37-346e-8d37-b1e8c803b460 | -3.57161 | -54.68288 | 2024-11-24 05:16:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 0cdca358-427b-31b9-a09a-f00cf2f5bad7 | -3.42362 | -53.2858 | 2024-11-24 05:16:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| a0510794-f122-398a-bac1-f5ac3da0690a | -5.19698 | -49.15659 | 2024-11-24 05:16:00 | NPP-375D | NOVA IPIXUNA | PARÁ | Brasil | 1504976 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ed8e54d6-e7db-3e00-9d18-726a19352d7d | -3.77423 | -52.09832 | 2024-11-24 05:16:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f794597c-7266-36bd-9774-4b51d37b376c | -4.3723 | -49.75056 | 2024-11-24 05:16:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| a0a9cfb7-c6c1-3b4d-a835-ce3b6adecd63 | -4.11479 | -49.50526 | 2024-11-24 05:16:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 72b828cf-33e1-3485-8c69-57aae05177cb | -3.53206 | -54.07988 | 2024-11-24 05:16:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 06d9792e-5d1b-3fc1-8fe9-e517e8a308b7 | -3.80921 | -51.33701 | 2024-11-24 05:16:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 7bd970d7-4d48-3e6f-898b-5225f089474d | -4.64201 | -48.84427 | 2024-11-24 05:16:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 90d65395-634b-3e7e-9a27-6cc438eee91d | -3.13532 | -55.11718 | 2024-11-24 05:16:00 | NPP-375D | BELTERRA | PARÁ | Brasil | 1501451 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| eebfc298-2bdb-35e1-a412-9f6fa49b64a4 | -3.8462 | -52.38882 | 2024-11-24 05:16:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 9a07af17-71f5-3299-9314-37ab0fc3d687 | -3.70967 | -53.75085 | 2024-11-24 05:16:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 69937a98-0e3e-3734-9f98-a9f362c4685f | -3.57803 | -54.7149 | 2024-11-24 05:16:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 281974f3-4e0a-33e0-8302-c033a31a4759 | -3.7753 | -52.17912 | 2024-11-24 05:16:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 220672a8-9683-322e-92f7-99e22cf5fec5 | -3.88294 | -54.21088 | 2024-11-24 05:16:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 1676ebb0-77f6-3c8c-94d4-1840604e4d0d | -3.25394 | -54.215 | 2024-11-24 05:16:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 54b4974c-aa7e-37c6-aa40-4405074c2ade | -3.52019 | -53.78824 | 2024-11-24 05:16:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 2c82a609-c8e1-3d0f-bab7-35e860aa79ad | -3.50723 | -53.82086 | 2024-11-24 05:16:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 13.5 |
| 5a8149f7-a00b-3f4c-98bc-b46be2dc4f77 | -3.52354 | -53.81815 | 2024-11-24 05:16:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| a78f2361-48bf-3ef8-9024-a6bd9ab5cfc3 | -3.66375 | -51.72309 | 2024-11-24 05:16:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 0ca8ca01-af8c-3c6c-a149-cac2bae3e842 | -4.24155 | -48.70514 | 2024-11-24 05:16:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 2c76dfca-48d8-38e0-88ae-2548dcb21d69 | -4.24208 | -48.70148 | 2024-11-24 05:16:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 8fbbec7a-1251-3f64-9384-eb9d6fe168a7 | -4.26035 | -48.69299 | 2024-11-24 05:16:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 50983aab-0083-39c4-b3b4-7251b4f9ee29 | -3.82552 | -52.40959 | 2024-11-24 05:16:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 6.8 |
| 98a9fd9d-07b8-3c89-9a4b-f874c523192d | -7.56685 | -49.40279 | 2024-11-24 05:16:00 | NPP-375D | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 644cc366-410a-3d11-8f4e-2f8e02d78bd4 | -3.81156 | -52.00047 | 2024-11-24 05:16:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| af5abc4e-f491-32d9-8bb0-124d459a7b89 | -3.98243 | -49.92885 | 2024-11-24 05:16:00 | NPP-375D | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 3824eace-4877-35ad-9074-7f373ec8449f | -5.57307 | -50.94997 | 2024-11-24 05:16:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 98cd2e4e-934a-3c1b-a4ca-c41545427738 | -3.81221 | -51.99619 | 2024-11-24 05:16:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| e7a40811-3018-3578-ac37-a0d218422dc6 | -3.63424 | -52.25171 | 2024-11-24 05:16:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 28952654-2f12-3e5b-8f98-f7fdb33999f9 | -3.721 | -51.31017 | 2024-11-24 05:16:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| c6b8ae3b-0fb9-3d87-94d1-e8f692855923 | -3.75359 | -54.78201 | 2024-11-24 05:16:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 6388a1f9-6645-30f5-85a2-1dbbb2fb89d0 | -3.628 | -55.46253 | 2024-11-24 05:16:00 | NPP-375D | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 5c42b69d-c9fe-31bb-b985-3fe01d9c3950 | -4.03528 | -54.62501 | 2024-11-24 05:16:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 71bee29b-3da9-399e-9e11-b02ed7183ebe | -5.5842 | -45.21481 | 2024-11-24 05:16:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 193bca8d-014d-3dfc-b4e5-5666115719cf | -3.90868 | -50.59138 | 2024-11-24 05:16:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 0d8f9a62-05ed-372a-b8f8-bb38ac9d9656 | -3.32595 | -53.85358 | 2024-11-24 05:16:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 30fcabda-cc38-3f66-bf88-42f73d8796e3 | -4.15856 | -54.57385 | 2024-11-24 05:16:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 78a81f67-848b-3787-857c-ac1f79fd35c9 | -3.25842 | -54.21107 | 2024-11-24 05:16:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 596092d9-513a-32a6-8491-8ad0401397bb | -3.50479 | -53.81086 | 2024-11-24 05:16:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 5dfd3fe6-2842-37df-a248-a2d98cca8d7e | -3.85208 | -50.43419 | 2024-11-24 05:16:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 6a22f3c7-67e2-3626-8a30-8e186a80cd1a | -3.88227 | -51.94354 | 2024-11-24 05:16:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |


[Clique aqui para ver as próximas entradas](README80.md)
