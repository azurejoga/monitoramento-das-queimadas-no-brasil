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

## Dados Diários - Página 10

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 80b06427-60a6-3377-902b-d7fd545256ac | -3.7017 | -51.812302 | 2024-12-03 00:37:00 | METOP-B | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| af97b96e-bd99-3bbd-9d23-978c182387c5 | -3.1192 | -53.988201 | 2024-12-03 00:37:00 | METOP-B | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0ceb3674-39ab-367d-9348-ad5d5b2dc231 | -1.6733 | -52.505402 | 2024-12-03 00:37:00 | METOP-B | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e33b1c0d-3067-39f2-a4f3-d59422bc63bf | -2.8443 | -54.094398 | 2024-12-03 00:37:00 | METOP-B | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 3f3266c6-bd03-3b6e-835e-f2287da0f1f2 | -3.7021 | -51.220901 | 2024-12-03 00:37:00 | METOP-B | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0ffad3b9-3673-3969-8ed5-d47044a16c6a | -8.1232 | -44.450298 | 2024-12-03 00:37:00 | METOP-B | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 954d3b15-5c8a-3994-beb8-886ef3362e16 | -2.2425 | -46.021099 | 2024-12-03 00:37:00 | METOP-B | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 7c1bdc8f-0ca5-33e2-9c50-b7b0677500da | -4.0425 | -46.999199 | 2024-12-03 00:37:00 | METOP-B | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| a42307c2-cc96-3115-a690-9187a0fcfa69 | -3.0201 | -51.532299 | 2024-12-03 00:37:00 | METOP-B | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a3ff21d9-fafb-3563-919c-b043d72fb488 | -2.8117 | -54.0406 | 2024-12-03 00:37:00 | METOP-B | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 797bf2f0-c46e-3897-aca5-abf89f06d936 | -3.2652 | -46.930801 | 2024-12-03 00:37:00 | METOP-B | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| eda386da-39f7-3beb-9201-0da5e8d37f35 | -3.5547 | -50.163399 | 2024-12-03 00:37:00 | METOP-B | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 55996ac7-94a5-310d-92d4-af5e3b2fc6dc | -3.4643 | -50.944698 | 2024-12-03 00:37:00 | METOP-B | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 4baaa1e3-6905-35df-bce5-9607ca062576 | -1.6831 | -52.503201 | 2024-12-03 00:37:00 | METOP-B | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 1c0d876b-9b3c-3535-9b19-e41009dfe6ab | -1.7288 | -52.614498 | 2024-12-03 00:37:00 | METOP-B | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 31c3df91-7d47-3ce7-91af-8fd395c36008 | -2.457 | -53.698399 | 2024-12-03 00:37:00 | METOP-B | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 3491bbe1-48ff-375a-be7a-8d1f04442c16 | -3.021 | -54.0098 | 2024-12-03 00:37:00 | METOP-B | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 7c0b33c3-5937-3b55-b61f-1134cd1799ce | -4.5443 | -42.912701 | 2024-12-03 00:37:00 | METOP-B | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 8db50bd7-81ff-3e31-8492-3962667f8af3 | -2.6728 | -46.593102 | 2024-12-03 00:37:00 | METOP-B | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 50de1dfe-96b8-3416-ba36-b7f5f6048dbf | -3.2608 | -53.6553 | 2024-12-03 00:37:00 | METOP-B | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 85999813-a356-3508-ad88-30e09e85d8ed | -3.398 | -50.2449 | 2024-12-03 00:37:00 | METOP-B | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 02b45b6b-85ee-3384-a6b9-1bf4a91489e2 | -3.0721 | -50.988098 | 2024-12-03 00:37:00 | METOP-B | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 6d8af81d-5ae6-31d6-baf7-37d44446ca1b | -4.4795 | -46.358101 | 2024-12-03 00:37:00 | METOP-B | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| dbd101cf-55c1-3c8f-8808-16b4180a17e4 | -8.1265 | -44.463699 | 2024-12-03 00:37:00 | METOP-B | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 45803aef-3713-3c74-8658-8dac504e7fd3 | -3.3155 | -49.9277 | 2024-12-03 00:37:00 | METOP-B | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 5a93c930-1a8c-31e1-967a-9ae379e42068 | -2.8158 | -53.048698 | 2024-12-03 00:37:00 | METOP-B | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c3842bed-750d-3da9-8c2c-9c1a9b9477e5 | -1.7316 | -52.764 | 2024-12-03 00:37:00 | METOP-B | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 736db0fc-98ba-3487-b048-0274ef6c20ff | -1.735 | -52.641701 | 2024-12-03 00:37:00 | METOP-B | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0a7a5e50-7512-3e0a-9522-2d2391b517b9 | -1.2532 | -54.528801 | 2024-12-03 00:37:00 | METOP-B | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f0621550-cf0b-3e54-a641-70899e85861e | -0.3542 | -51.592602 | 2024-12-03 00:37:00 | METOP-B | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | nan |
| 527b6f86-91ca-35ea-a12f-242343f8b3ef | -3.3988 | -50.974098 | 2024-12-03 00:37:00 | METOP-B | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 97ee5fd5-2d81-39f2-9a73-57d70d354dd2 | -3.359 | -45.831799 | 2024-12-03 00:37:00 | METOP-B | GOVERNADOR NEWTON BELLO | MARANHÃO | Brasil | 2104651 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 61922f29-66d0-30f7-9c71-f32a73b797e9 | -3.0833 | -53.3685 | 2024-12-03 00:37:00 | METOP-B | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e603e564-b0ab-3feb-9795-c9745a57239e | -1.7086 | -52.4333 | 2024-12-03 00:37:00 | METOP-B | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 63445d60-ce9b-3ac2-a7c6-edefb6a7d5da | -2.3678 | -53.852001 | 2024-12-03 00:37:00 | METOP-B | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 11761969-b1be-370c-87af-43d945b607aa | -3.2529 | -46.922199 | 2024-12-03 00:37:00 | METOP-B | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| be0c3c66-48df-3355-8935-4d3a563ba035 | -3.039 | -54.043999 | 2024-12-03 00:37:00 | METOP-B | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 059413f2-ad9a-329d-b0f0-e665d9bd01b9 | -3.8646 | -50.892101 | 2024-12-03 00:37:00 | METOP-B | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 8832ac7b-b3de-36f5-8942-569085c06092 | -3.3914 | -50.2155 | 2024-12-03 00:37:00 | METOP-B | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 719fdebc-f3df-3a93-bc36-17cc88ffd9ab | -2.8003 | -54.0354 | 2024-12-03 00:37:00 | METOP-B | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 8a6d8a22-03be-3c28-b6ae-216d682980fe | -2.376 | -53.842701 | 2024-12-03 00:37:00 | METOP-B | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a1c2b146-8360-3d8d-ac1a-d8ead37a9e69 | -1.8351 | -45.990799 | 2024-12-03 00:37:00 | METOP-B | MARACAÇUMÉ | MARANHÃO | Brasil | 2106326 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 70b8a613-32b6-3484-8ced-04d7d9d4d313 | -3.0702 | -53.907902 | 2024-12-03 00:37:00 | METOP-B | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 703e5a9c-eedb-3017-a577-da3e22eaa7c4 | -3.0945 | -54.108398 | 2024-12-03 00:37:00 | METOP-B | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 242ffb3e-e21e-33a7-b82b-5e23569a9a1c | -2.374 | -53.650101 | 2024-12-03 00:37:00 | METOP-B | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f927f66c-745d-3328-a0a6-7310ba9f8c64 | -1.7319 | -52.628101 | 2024-12-03 00:37:00 | METOP-B | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 9c185918-6e1d-382d-b2a8-a7f8e64496fb | -3.0279 | -53.856701 | 2024-12-03 00:37:00 | METOP-B | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 92e91f53-7036-3cec-a98a-a73f81528dff | -3.6496 | -52.633598 | 2024-12-03 00:37:00 | METOP-B | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a2b172f9-b83f-37e5-bb15-550ff1af541a | -3.3445 | -52.6507 | 2024-12-03 00:37:00 | METOP-B | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 32291eb8-4df5-372a-8c1e-3b6dfb7fba37 | -3.274 | -53.622601 | 2024-12-03 00:37:00 | METOP-B | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 746202ed-f3c1-3b31-a226-139d916274cd | -3.0144 | -54.026402 | 2024-12-03 00:37:00 | METOP-B | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 55dc359d-1428-30c8-b70f-aea84a92750d | -3.07 | -54.0448 | 2024-12-03 00:37:00 | METOP-B | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| acc6a885-a4ec-31f7-aa08-85b42e884732 | -1.2588 | -53.3638 | 2024-12-03 00:37:00 | METOP-B | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a4ff8471-596c-37fa-bde9-159fa5f664f2 | -3.0323 | -53.416599 | 2024-12-03 00:37:00 | METOP-B | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f4247438-f515-3ef6-b890-d11186d717d5 | -3.1076 | -54.0289 | 2024-12-03 00:37:00 | METOP-B | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ce4bd7e7-c0c8-36a2-bb4c-73d267411b39 | -3.4558 | -42.001499 | 2024-12-03 00:37:00 | METOP-B | MURICI DOS PORTELAS | PIAUÍ | Brasil | 2206696 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 0a62f9cd-d6ac-3433-b4ef-a0dfce442f85 | -1.0831 | -53.453201 | 2024-12-03 00:37:00 | METOP-B | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e55cb504-c46b-3eec-82e2-db911b711fb4 | -3.2822 | -50.324699 | 2024-12-03 00:37:00 | METOP-B | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f7b7fabc-5402-3ad8-9dd2-544482c5807b | -3.2674 | -53.638901 | 2024-12-03 00:37:00 | METOP-B | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e0abbfbf-0faa-3f0c-9be6-c0172f124beb | -3.7048 | -51.825901 | 2024-12-03 00:37:00 | METOP-B | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a97eade3-a26b-312d-85f6-c0909de694e6 | -2.8236 | -52.579498 | 2024-12-03 00:37:00 | METOP-B | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b63c72cb-d471-34d1-900d-2fba015d76ad | -3.8111 | -52.3895 | 2024-12-03 00:37:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ae39a088-51d9-3422-bcc1-0d191a80d780 | -2.7748 | -55.349201 | 2024-12-03 00:37:00 | METOP-B | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 595bc546-3c63-3ed3-b245-793a7d149575 | -2.8427 | -54.087101 | 2024-12-03 00:37:00 | METOP-B | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 41c2420e-4357-301d-b46f-dfe800d011ae | -1.5825 | -52.2397 | 2024-12-03 00:37:00 | METOP-B | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 51635c40-7c16-3823-8f6e-9b749b34a772 | -3.2431 | -53.622002 | 2024-12-03 00:37:00 | METOP-B | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ee4e53c0-224f-3c31-a2a0-a21569e41e8c | -2.8013 | -53.0303 | 2024-12-03 00:37:00 | METOP-B | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| adf44e17-2594-3ae8-838c-77e40d1fcd46 | -1.9065 | -52.854099 | 2024-12-03 00:37:00 | METOP-B | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 35ed30a4-107f-33c8-8540-24eac411a872 | -3.0128 | -54.019199 | 2024-12-03 00:37:00 | METOP-B | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 90398421-7b2c-3198-9f0c-bfc3db556803 | -3.2576 | -53.641102 | 2024-12-03 00:37:00 | METOP-B | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 59e76089-ce9f-3f26-b649-cdeea8185fc7 | -3.2547 | -50.612 | 2024-12-03 00:37:00 | METOP-B | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 4cd23da8-9ee8-3cb8-aac1-0aa129cbf849 | -4.1613 | -48.580898 | 2024-12-03 00:37:00 | METOP-B | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 3dc36528-b7c0-3b8c-af4f-c36a4b181529 | -2.8931 | -51.7911 | 2024-12-03 00:37:00 | METOP-B | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 494c8b68-5413-3b58-8086-f04d77242503 | -3.2595 | -53.603298 | 2024-12-03 00:37:00 | METOP-B | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 938dae91-7e5e-337f-a238-4a359dfef98a | -2.0491 | -54.680401 | 2024-12-03 00:37:00 | METOP-B | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 3032a9de-6320-3496-86bd-43a1428d4148 | -2.806 | -53.0509 | 2024-12-03 00:37:00 | METOP-B | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 961abe0e-7653-311f-8df0-5eddcc18a09e | -3.0548 | -54.483299 | 2024-12-03 00:37:00 | METOP-B | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 67a57f16-71a0-3be4-84e4-46541c6dee68 | -2.285 | -45.762001 | 2024-12-03 00:37:00 | METOP-B | PRESIDENTE MÉDICI | MARANHÃO | Brasil | 2109239 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 6634e6ce-1d67-3136-9879-837a8cc53de8 | -4.3153 | -48.0872 | 2024-12-03 00:37:00 | METOP-B | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d00a188c-839d-3bc9-ac1d-d153858f6c37 | -3.3429 | -52.643902 | 2024-12-03 00:37:00 | METOP-B | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0a61fc69-30d2-3088-a59a-2dfeb7782103 | -2.8345 | -54.0965 | 2024-12-03 00:37:00 | METOP-B | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e7e3164c-54a1-3bbd-a71a-3d3133a338d6 | -3.2531 | -50.604801 | 2024-12-03 00:37:00 | METOP-B | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 97742b8e-a608-3c3f-b4f3-3e96e7cb6237 | -3.2333 | -53.6241 | 2024-12-03 00:37:00 | METOP-B | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f15a8972-779a-3c93-b00e-16a9bc30bb42 | -2.8313 | -54.082001 | 2024-12-03 00:37:00 | METOP-B | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 6b812159-71b7-3e69-b681-e27bb3762d44 | -3.0193 | -54.002499 | 2024-12-03 00:37:00 | METOP-B | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 105733f6-8b5c-3e17-b107-b2696068699d | -3.3845 | -51.138699 | 2024-12-03 00:37:00 | METOP-B | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 955a1f6f-6dfa-38db-ba7d-2ffcd501a5d9 | -2.8641 | -53.9986 | 2024-12-03 00:37:00 | METOP-B | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 7a7c0093-9b9a-38d5-8f44-b360ac236318 | -2.8854 | -54.001598 | 2024-12-03 00:37:00 | METOP-B | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 418fb6ab-0f3d-3a5a-8ee5-ca7967174951 | -3.2415 | -53.614799 | 2024-12-03 00:37:00 | METOP-B | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a677a621-4540-305e-9533-c6995c1b5b2d | -1.746 | -52.7822 | 2024-12-03 00:37:00 | METOP-B | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 6a076333-2531-3c4a-8720-3c49fb5966a7 | -2.5747 | -53.672501 | 2024-12-03 00:37:00 | METOP-B | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 8971f62d-3137-3a03-b90f-659ad2ca6a96 | -2.815 | -54.055099 | 2024-12-03 00:37:00 | METOP-B | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 72f837f0-408f-3e92-a6fb-bcbe019d9fb2 | 2.7378 | -60.351601 | 2024-12-03 00:37:00 | METOP-B | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| 3c6b6e60-e51f-3ac7-90c9-f9acb47509de | -2.8329 | -54.089199 | 2024-12-03 00:37:00 | METOP-B | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 408dfebd-fcec-3295-8b4a-2cf1ef3cfa3f | -3.2446 | -53.629101 | 2024-12-03 00:37:00 | METOP-B | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 51ed5d6f-8f75-3ad1-abe8-1cf006bc1622 | -2.3708 | -53.911098 | 2024-12-03 00:37:00 | METOP-B | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 3dafd414-c7de-3e49-a908-bee12b0d85b9 | -1.2309 | -51.5961 | 2024-12-03 00:37:00 | METOP-B | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 4b41f953-d835-31fd-b800-51b028f01d50 | -1.8215 | -55.271801 | 2024-12-03 00:37:00 | METOP-B | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 9a338f08-90d1-3900-ad95-7694c3630013 | -3.0259 | -54.031601 | 2024-12-03 00:37:00 | METOP-B | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d89856ed-697d-3355-bbac-1d1b11ccdcb7 | -4.7435 | -45.642899 | 2024-12-03 00:37:00 | METOP-B | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | nan |


[Clique aqui para ver as próximas entradas](README11.md)
