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

## Dados Diários - Página 72

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 467606fd-a19b-3e9d-abaa-e16a288bc484 | -1.9489 | -49.52573 | 2024-11-24 05:14:00 | NPP-375D | LIMOEIRO DO AJURU | PARÁ | Brasil | 1504000 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 2c4068ed-6e75-31a0-9c91-cbcd27d54de1 | -1.42821 | -46.06211 | 2024-11-24 05:14:00 | NPP-375D | CARUTAPERA | MARANHÃO | Brasil | 2102903 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |
| b06efc7c-3e49-3471-a7bd-144cf31c40a1 | -2.6182 | -51.79963 | 2024-11-24 05:14:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 419d9f4c-7c4b-3852-b87a-4d03cf432948 | -3.0994 | -53.87949 | 2024-11-24 05:14:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| b57a5ac1-7680-3a30-a79b-6a44c08b3789 | -3.67434 | -50.25399 | 2024-11-24 05:14:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 413c7f7b-5daa-3fed-bd1f-7fedb2ecdddf | -2.95183 | -53.71576 | 2024-11-24 05:14:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 1a841971-7389-32cf-a95a-5bff69999549 | -2.85985 | -53.97115 | 2024-11-24 05:14:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| dc3cb52a-50d4-3e4a-8093-da954b30ff52 | -2.80489 | -54.02435 | 2024-11-24 05:14:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| c8cdb8cc-e374-3b53-ba61-fe7ed4821767 | -2.50451 | -54.25058 | 2024-11-24 05:14:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| bfd41578-ebd4-323f-a068-721ce5c9de0d | -1.60567 | -52.59107 | 2024-11-24 05:14:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 17f16f4b-d8d8-3f52-bdc5-ced9da61036b | -1.24093 | -54.00656 | 2024-11-24 05:14:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 69005b1f-1b43-3ed4-85cf-21b19a795274 | -2.83362 | -54.01452 | 2024-11-24 05:14:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| d356dfa9-d8ee-3bbd-84a6-245a6463b6e2 | -2.81937 | -54.03125 | 2024-11-24 05:14:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 239d2b49-cc54-3414-bf55-c725f6d74b11 | -3.22673 | -53.93487 | 2024-11-24 05:14:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 08f689a3-4614-311e-9d5d-06d6c289e321 | -1.73144 | -52.71988 | 2024-11-24 05:14:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 49b87b89-2b91-369b-b983-9a670d9aa6b2 | -1.1362 | -53.40345 | 2024-11-24 05:14:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 4e5b5300-bd8f-3118-abf6-a3059ffa2316 | -2.7011 | -51.99259 | 2024-11-24 05:14:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| a95f2990-56e7-3a8a-802c-1a5dd51e06b4 | -2.06935 | -50.30883 | 2024-11-24 05:14:00 | NPP-375D | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 2592ba1d-c282-3eb7-9c67-9dd2555d073b | -2.74175 | -54.10842 | 2024-11-24 05:14:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 754640e4-39e8-3897-9055-893d7bf1ef16 | -2.5856 | -54.04633 | 2024-11-24 05:14:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 379c033c-7db5-314f-81bc-920b618742bf | -3.29213 | -49.90524 | 2024-11-24 05:14:00 | NPP-375D | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 7c724566-c515-3cc4-a5be-c121a99a51dd | -2.28073 | -53.63235 | 2024-11-24 05:14:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 5da1238d-640a-3c4a-bdec-b7baf54fda12 | -3.95561 | -45.99169 | 2024-11-24 05:14:00 | NPP-375D | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 8ff37225-96e7-3b5a-8161-d7445b73624d | -1.46636 | -46.04387 | 2024-11-24 05:14:00 | NPP-375D | CARUTAPERA | MARANHÃO | Brasil | 2102903 | 21 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 3c7b811e-896c-3445-a04f-3617f3778077 | -3.09988 | -53.74048 | 2024-11-24 05:14:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 770af1af-2d4d-39d8-b1bb-0e01bca5951d | 0.87481 | -54.63178 | 2024-11-24 05:14:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 0c6c5c01-c75d-3155-86f5-2aea549b58eb | -3.10016 | -54.00515 | 2024-11-24 05:14:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 6.5 |
| 8f4a86ae-6c6d-3757-9971-629944568e41 | -3.03123 | -49.45499 | 2024-11-24 05:14:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| cac08bdb-405a-37bf-8ae6-c46d4ffc0f44 | -2.28903 | -49.2042 | 2024-11-24 05:14:00 | NPP-375D | IGARAPÉ-MIRI | PARÁ | Brasil | 1503309 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 3c37b63b-41e6-3cf0-8e5f-2289f3db4936 | -1.61268 | -54.41404 | 2024-11-24 05:14:00 | NPP-375D | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ba77d810-273c-3dd5-9d4d-61742915fbb9 | -3.31644 | -53.28406 | 2024-11-24 05:14:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 24ec9d6a-6791-3d9c-acf8-a46e0c503012 | -1.25654 | -51.75685 | 2024-11-24 05:14:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| a0539923-e78c-3bd9-ae74-afe1888ead85 | -3.03899 | -49.44691 | 2024-11-24 05:14:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 7.3 |
| 3a0ec43b-ae06-3e7d-9886-8db91f1d3480 | -2.10125 | -46.26545 | 2024-11-24 05:14:00 | NPP-375D | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 81e2500b-2c3d-3c1e-b28e-2bb01b2ea38d | -3.25034 | -50.62365 | 2024-11-24 05:14:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 262c7b6a-9c93-3926-9719-e48d350e0a59 | -0.96525 | -51.71926 | 2024-11-24 05:14:00 | NPP-375D | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 72903137-847c-3887-8628-15eb4bf1ae56 | -2.75367 | -48.67106 | 2024-11-24 05:14:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 9240dabb-86a8-321a-878e-6356a5efb34e | -2.84503 | -54.16316 | 2024-11-24 05:14:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f70d4c1b-3faa-3735-a460-22e252d53baf | -2.58773 | -54.23183 | 2024-11-24 05:14:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| f14f6eba-e5c9-379e-b91d-b22abec5430a | -1.76163 | -52.16347 | 2024-11-24 05:14:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| edbf848f-3f4f-3ae4-8c34-657a1f6dfc81 | -1.15863 | -53.67368 | 2024-11-24 05:14:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 5846da37-951f-3061-896b-2e8d556079cb | -3.68497 | -50.11109 | 2024-11-24 05:14:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 89739aea-d7c3-33a8-ae93-5d48e06fb534 | -2.45796 | -53.7033 | 2024-11-24 05:14:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 1741169f-9be4-33a3-beba-98f39c5185f4 | -0.33283 | -51.54635 | 2024-11-24 05:14:00 | NPP-375D | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 02e1111e-67d1-3db7-9d3a-0580a3a19492 | 0.40804 | -50.84878 | 2024-11-24 05:14:00 | NPP-375D | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 6c070e72-3419-3de2-a9ad-76030ee27d0d | -0.36144 | -50.02464 | 2024-11-24 05:14:00 | NPP-375D | CHAVES | PARÁ | Brasil | 1502509 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 8e312719-10f1-32aa-9c14-4b92a813607c | -1.23262 | -51.7408 | 2024-11-24 05:14:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 20bc530d-1bb8-3a0a-a5af-58c74cdfdddb | -3.37143 | -53.32643 | 2024-11-24 05:14:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 54b77d61-6333-38a6-829d-6d69f5d3e070 | -0.37461 | -51.54731 | 2024-11-24 05:14:00 | NPP-375D | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 2c23eb83-c696-33df-aac3-bd860f6d0b7f | -1.94844 | -49.52863 | 2024-11-24 05:14:00 | NPP-375D | LIMOEIRO DO AJURU | PARÁ | Brasil | 1504000 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 387117ba-5d2c-3128-bae8-283da0d8647a | -3.03334 | -49.44923 | 2024-11-24 05:14:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 8d0d64c0-6822-3b74-be8a-8f6d445255be | -2.93902 | -54.07987 | 2024-11-24 05:14:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 18bc78cd-7135-33bf-9a42-fe5aa5fa4c54 | -3.00128 | -52.50904 | 2024-11-24 05:14:00 | NPP-375D | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 81ad5f42-a516-39c0-9ea4-3024f19b3a3a | -1.15937 | -53.66896 | 2024-11-24 05:14:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 1718100a-0db7-3fce-836e-8633aca985e0 | -3.24516 | -50.12167 | 2024-11-24 05:14:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c6888dc0-7410-3e67-b623-462a64838386 | -1.96397 | -48.39198 | 2024-11-24 05:14:00 | NPP-375D | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 310e0269-4d39-33af-938f-2679743f0d00 | -3.75107 | -50.01088 | 2024-11-24 05:14:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 11312ac6-a328-3371-b9e9-238a8ea11c0b | -3.1832 | -54.32409 | 2024-11-24 05:14:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 9b5e1fd7-b30e-337c-b067-2f834b507d51 | -3.17244 | -45.29624 | 2024-11-24 05:14:00 | NPP-375D | PENALVA | MARANHÃO | Brasil | 2108306 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 639847ef-9886-38ee-a793-b161c404824f | -1.72736 | -53.25745 | 2024-11-24 05:14:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 0fe0d216-8330-3e9a-8696-c3e90feb239a | -2.75269 | -54.11241 | 2024-11-24 05:14:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 95edebb1-587e-34ec-ab2a-c7dc1663d0ad | -1.19816 | -51.7644 | 2024-11-24 05:14:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 7f1cd086-4f33-3927-a3e8-a2e25f1d062d | -3.24684 | -53.27367 | 2024-11-24 05:14:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 19173b56-4f24-3252-80aa-32b089b5469d | -3.39388 | -50.3206 | 2024-11-24 05:14:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| ad630bbd-fd86-3f1c-9b6c-198ae8d8f111 | -1.41251 | -54.90465 | 2024-11-24 05:14:00 | NPP-375D | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 4ab54815-17d5-3397-82c3-ad29c1b90c5c | -3.15973 | -50.58111 | 2024-11-24 05:14:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 9284df8c-1604-3447-8731-a77ceb215ad9 | -3.2217 | -53.83725 | 2024-11-24 05:14:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| f383ffc9-f4dc-3e62-8e43-fb6880631704 | -3.68413 | -50.11686 | 2024-11-24 05:14:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| d7f6a0bb-d760-312f-9711-9f0cdc6f37c6 | -1.96182 | -49.53292 | 2024-11-24 05:14:00 | NPP-375D | LIMOEIRO DO AJURU | PARÁ | Brasil | 1504000 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 65b32abc-87d8-3fe6-8dab-86ad592a4cdc | -2.16921 | -53.79382 | 2024-11-24 05:14:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 5831bf9e-f404-349d-b154-2816d8ae453e | -3.5917 | -49.35402 | 2024-11-24 05:14:00 | NPP-375D | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 763674fe-9b5e-3e1f-bda0-e88f295781dc | -3.23225 | -54.23025 | 2024-11-24 05:14:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| fa7f2991-16cd-394c-b718-e6a80df42f03 | -2.74524 | -49.11493 | 2024-11-24 05:14:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| abf1713f-3665-3de8-b341-b54d20534ddf | -0.74546 | -52.41346 | 2024-11-24 05:14:00 | NPP-375D | LARANJAL DO JARI | AMAPÁ | Brasil | 1600279 | 16 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 6d8f55b8-efb6-36ad-a426-397e77a441b6 | -1.20432 | -51.75295 | 2024-11-24 05:14:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 99119b57-3f83-3f9e-af5a-02bfc04ed532 | -3.34612 | -50.50584 | 2024-11-24 05:14:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 684afb7a-ae0d-3cdf-b1a0-304122d4667b | -1.42899 | -46.05716 | 2024-11-24 05:14:00 | NPP-375D | CARUTAPERA | MARANHÃO | Brasil | 2102903 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 07af86f3-0b56-3f6e-84c6-0e746f7f89ca | -1.48063 | -52.5202 | 2024-11-24 05:14:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 6c70a67e-7564-3358-9854-690e70b3e745 | -1.76322 | -52.70288 | 2024-11-24 05:14:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| a420f87e-2461-39e4-83fc-6ced993d67be | -1.14593 | -53.40237 | 2024-11-24 05:14:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| dc5c4367-89e7-350e-ab85-08e4c387d352 | 0.41767 | -50.85179 | 2024-11-24 05:14:00 | NPP-375D | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 2.2 |
| cd018a99-b686-3652-b433-530a7bd8fed8 | -0.09731 | -51.7508 | 2024-11-24 05:14:00 | NPP-375D | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 7699dbf7-7340-3281-a0e2-4f2f885ea30a | -2.95109 | -53.72058 | 2024-11-24 05:14:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 45f48469-44b2-3b31-81e0-78b46d4e38a2 | -0.97344 | -51.71092 | 2024-11-24 05:14:00 | NPP-375D | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 6909ef4a-6ea8-355c-ac2b-47db4a891c11 | -2.80276 | -53.00563 | 2024-11-24 05:14:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| c1b192bb-ca72-3de0-9f08-d20ff0bf709f | -1.84208 | -46.64399 | 2024-11-24 05:14:00 | NPP-375D | VISEU | PARÁ | Brasil | 1508308 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 622fbcbe-3e41-3d77-88b8-bd85128482a3 | -2.46911 | -47.08826 | 2024-11-24 05:14:00 | NPP-375D | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 5820af09-cfc7-3cd2-a1e4-560ae0a9f46f | -2.64804 | -46.85625 | 2024-11-24 05:14:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| dacb5c80-d67f-39e6-8b69-17d7a899aac0 | -2.83054 | -54.00933 | 2024-11-24 05:14:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 1747f131-7f73-3fe9-af34-07a03b839bed | -0.93334 | -52.41198 | 2024-11-24 05:14:00 | NPP-375D | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f0456875-384e-365d-9a35-0ec54402b22c | -2.59245 | -54.37247 | 2024-11-24 05:14:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 999d06a3-e9e4-3cd8-bf39-ba695a89614e | -1.6827 | -52.65757 | 2024-11-24 05:14:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 4c9c76c3-efea-3e44-ba22-6ce13fd18934 | -2.99612 | -53.73731 | 2024-11-24 05:14:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| b8c60be9-dfe5-3f5d-9e84-4e2432e22b09 | -2.57747 | -51.89156 | 2024-11-24 05:14:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| c7f7c587-4ef0-36be-8f8e-ec6c48fbbbfe | -0.77111 | -52.49069 | 2024-11-24 05:14:00 | NPP-375D | LARANJAL DO JARI | AMAPÁ | Brasil | 1600279 | 16 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e6d656fa-c074-3f45-aa0f-61e01403beaf | -2.77412 | -54.04788 | 2024-11-24 05:14:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| a1282570-a2ec-3218-9f3b-b7bea49bd32d | -2.46368 | -49.03651 | 2024-11-24 05:14:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| cc98aa38-a815-3818-9f7e-635cb5713a7b | -2.83291 | -54.01913 | 2024-11-24 05:14:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 50a65482-74af-30c1-9e13-43a7cc8ee2b1 | -1.95168 | -49.5313 | 2024-11-24 05:14:00 | NPP-375D | LIMOEIRO DO AJURU | PARÁ | Brasil | 1504000 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 15d45030-1f0a-3662-940c-84d4476df36a | -1.59124 | -55.87326 | 2024-11-24 05:14:00 | NPP-375D | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |


[Clique aqui para ver as próximas entradas](README73.md)
