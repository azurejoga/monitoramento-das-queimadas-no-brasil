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

## Dados Diários - Página 38

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| cf4cbaf5-6261-3ac1-af5d-0303a8115145 | -4.87364 | -41.30122 | 2024-11-30 04:40:00 | NOAA-21 | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 3.6 |
| 1619f0e3-0e27-3321-b1ed-e1e8828046c5 | -2.71661 | -48.59138 | 2024-11-30 04:40:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| b3e8dec9-f8d8-352f-b2d4-83b3fef1ec0b | -1.66769 | -52.05534 | 2024-11-30 04:40:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 9393c522-e8f3-3bc7-89b2-d22ef048629d | -3.05184 | -54.05412 | 2024-11-30 04:40:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 91edb536-d5fa-38e8-99e1-545c1211a88f | -2.98304 | -53.35616 | 2024-11-30 04:40:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| ff1a2c3b-3b0e-33b4-b714-99786cd36750 | -1.84125 | -47.17913 | 2024-11-30 04:40:00 | NOAA-21 | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 2d457a40-7a70-3208-a46c-d334152d9d73 | -0.95716 | -51.65995 | 2024-11-30 04:40:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 8f718b57-9736-335a-ac4f-1fca45a0ae9a | -2.2143 | -53.75812 | 2024-11-30 04:40:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| c3032818-7796-3bf7-a612-a9477bf92cf0 | -1.96634 | -47.70876 | 2024-11-30 04:40:00 | NOAA-21 | SÃO DOMINGOS DO CAPIM | PARÁ | Brasil | 1507201 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 8a31947e-8174-38f0-860b-ec302a549947 | -2.71403 | -46.13019 | 2024-11-30 04:40:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 308da644-a751-3863-b1a9-827902ea4695 | -2.54775 | -55.23107 | 2024-11-30 04:40:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 0ff66ffd-31e3-357b-aa9b-d21440a490d0 | -2.61453 | -51.80849 | 2024-11-30 04:40:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 35eb151f-0163-33f3-9d9e-68a44f92fb1e | -3.93907 | -48.14267 | 2024-11-30 04:40:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| df985240-0ad7-328c-aaf9-87f33c9be5d4 | -2.82218 | -54.02911 | 2024-11-30 04:40:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 43dd152f-9d74-3c6b-b674-c18d2a32fd26 | -2.97645 | -53.28875 | 2024-11-30 04:40:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 87af3de9-1d9c-3c2f-82a8-348629678f1a | -3.2503 | -53.86357 | 2024-11-30 04:40:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 8f5e8da4-284c-37b2-ab0f-0c7a6516759d | -3.23366 | -53.37155 | 2024-11-30 04:40:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| c7211ee0-117c-35cf-b879-50fc1a06cb9e | -2.73887 | -47.98962 | 2024-11-30 04:40:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 4385fd2b-20f1-3007-82c3-b85c1f0d9078 | -3.2889 | -48.76209 | 2024-11-30 04:40:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| c8469c41-a6ef-32f8-80ab-9282e0e7a841 | -2.85364 | -46.68845 | 2024-11-30 04:40:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 8df9c097-6136-31b5-a508-c2faf8ce783d | -3.33324 | -50.21656 | 2024-11-30 04:40:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| ce480cfa-1448-377a-a244-04fc7803b38d | -3.33257 | -46.70087 | 2024-11-30 04:40:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 8d03002e-bc83-37e9-8bf7-646190dda3f1 | -2.70884 | -46.30629 | 2024-11-30 04:40:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 1a19fde3-e2cf-3bc6-87b4-7a0784aad7a4 | -2.58051 | -49.2246 | 2024-11-30 04:40:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 08b2a878-762f-3a72-8161-843ac88cf99d | -1.28168 | -51.7411 | 2024-11-30 04:40:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 7.5 |
| 7253ae57-c780-3a4a-9863-641929ce9c9e | -3.54007 | -50.17668 | 2024-11-30 04:40:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| df5568cf-ce0a-331a-84fd-f7ae36dffb0a | -3.50845 | -53.78747 | 2024-11-30 04:40:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 018cc42f-2e41-3a05-bbd4-b028183b044a | -3.33535 | -53.36547 | 2024-11-30 04:40:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e554c428-4aa5-3aa9-accb-039f04790860 | -2.87133 | -51.6535 | 2024-11-30 04:40:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| f12ed567-3159-34d9-b146-7ee98c96f816 | -3.41867 | -50.16886 | 2024-11-30 04:40:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 9b205c18-c1b5-3247-82a3-adbfed6f552b | -2.65323 | -46.57721 | 2024-11-30 04:40:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 3.0 |
| c3c9ae8e-8267-365e-b043-b74efdb66ebc | -2.87968 | -53.323 | 2024-11-30 04:40:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| a4ddbc72-74be-3deb-b80c-6cba291d7ece | -3.72727 | -54.52637 | 2024-11-30 04:40:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 635722fe-fbb9-3535-bdac-07a9758aa590 | -2.57764 | -50.00106 | 2024-11-30 04:40:00 | NOAA-21 | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| b7c91da5-cfdc-39c4-a3aa-cb99fa4953e3 | -2.02357 | -50.77666 | 2024-11-30 04:40:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |
| b5abb989-b23c-3f59-ba83-827ebf685ced | -3.24663 | -53.64057 | 2024-11-30 04:40:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 6cfdd9c1-c047-3ac9-9395-a9c5c73c9ad0 | -2.97217 | -53.92557 | 2024-11-30 04:40:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 9f680be5-d21b-351b-8438-e668ae65f6b2 | -2.47006 | -46.56182 | 2024-11-30 04:40:00 | NOAA-21 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| c67a378c-82e9-352e-9778-9b2283dbdba6 | -3.31254 | -50.08678 | 2024-11-30 04:40:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 918c737b-c08e-34a0-9400-73d81a41d1c2 | -3.67972 | -50.22004 | 2024-11-30 04:40:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 30ae70dc-004a-346a-98c5-08f938135e10 | -2.1892 | -48.3962 | 2024-11-30 04:40:00 | NOAA-21 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 811b4730-6641-39a3-9b9c-56a5a8019263 | -3.08567 | -49.47379 | 2024-11-30 04:40:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 5687ccbd-a788-3750-82de-0a24b7f0463a | -2.25389 | -53.45882 | 2024-11-30 04:40:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 5d798a9d-9f32-3016-bcc7-71bfb716460f | -2.69322 | -48.65461 | 2024-11-30 04:40:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| f5f9528a-9db4-3803-b588-b3f99c7186e4 | -2.58382 | -49.22512 | 2024-11-30 04:40:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 4189bb21-882e-385c-86fd-b71bf757ce21 | -4.49539 | -49.63867 | 2024-11-30 04:40:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 2fe43939-ddbc-32e6-977e-941673927df5 | -4.52238 | -45.72778 | 2024-11-30 04:40:00 | NOAA-21 | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 11441980-f451-3621-85b3-07d8c718bd4f | -3.99025 | -49.93143 | 2024-11-30 04:40:00 | NOAA-21 | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 3e5cd016-0cd2-3e3b-bd79-0cabab58b50a | -2.7121 | -46.19052 | 2024-11-30 04:40:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 937ca4aa-8c64-32e9-9e25-d3345c10397a | -1.6227 | -53.88259 | 2024-11-30 04:40:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| f1ae6c15-80a0-3b98-836c-635b19034eb7 | -3.6474 | -50.22951 | 2024-11-30 04:40:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| ce234594-14fa-326f-983f-c6931720a731 | -2.3319 | -49.09382 | 2024-11-30 04:40:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 11bc6633-bdf0-32d1-925f-2c52904aea6a | -1.69239 | -46.78144 | 2024-11-30 04:40:00 | NOAA-21 | VISEU | PARÁ | Brasil | 1508308 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 566127f3-2a89-350b-8ed3-99e11b714ef0 | -4.64858 | -43.74297 | 2024-11-30 04:40:00 | NOAA-21 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| b6a1bf1c-061e-3053-a766-1fd35d9c4cfc | -1.58385 | -52.27815 | 2024-11-30 04:40:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 21de81ca-12d4-3de5-a276-eaed580e62ef | -2.93755 | -48.00216 | 2024-11-30 04:40:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ec2f3a6c-d726-3f99-a838-fb22f203eab0 | -2.53859 | -47.32575 | 2024-11-30 04:40:00 | NOAA-21 | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 101a25a0-68b3-36dd-a5a9-46217f77ecdc | -1.71906 | -52.774 | 2024-11-30 04:40:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 563d2422-3282-36ac-aec2-d50f88727e6e | -3.20278 | -46.56049 | 2024-11-30 04:40:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e8e5346f-942b-389d-9e04-e1b381f215b1 | -2.80138 | -53.04595 | 2024-11-30 04:40:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 82449baa-ca4b-3fbd-a9ce-e3dc6137ce41 | -1.09849 | -53.39638 | 2024-11-30 04:40:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 9d345f98-5e02-34dd-a26b-87c528ca4697 | -3.34386 | -50.23634 | 2024-11-30 04:40:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| f64b2e47-72ea-33d4-a66d-44366f3f7783 | -2.98107 | -53.28454 | 2024-11-30 04:40:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 2281f645-e149-361e-b197-32c9915d1176 | -7.90214 | -46.67089 | 2024-11-30 04:40:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 09571b9b-6f2f-3504-be6d-75e037e30739 | -4.14567 | -48.23582 | 2024-11-30 04:40:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| bfb415ab-7708-3feb-83d8-3c77725fe201 | -1.95075 | -53.34279 | 2024-11-30 04:40:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 3b8d37c0-c829-35a7-852a-c1b78624c38e | -3.79137 | -58.97672 | 2024-11-30 04:40:00 | NOAA-21 | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 73afe59f-d5ed-389d-85ba-d9d5242ca97a | -1.60736 | -48.70264 | 2024-11-30 04:40:00 | NOAA-21 | BARCARENA | PARÁ | Brasil | 1501303 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 986c902c-5903-3db3-809e-201fa20b3857 | -3.98035 | -46.72989 | 2024-11-30 04:40:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| a0fe109a-0747-3355-b6c0-5b8b8314b6f8 | -3.7745 | -49.98355 | 2024-11-30 04:40:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 1a4c784f-5881-324a-9b95-394f8d160ac9 | -3.07527 | -49.10472 | 2024-11-30 04:40:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d8215bd9-4a0e-3d2b-9c98-47fc65430e40 | -1.15695 | -51.70179 | 2024-11-30 04:40:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 92dac303-b210-3726-ad41-14d7c7e58e6d | -2.1836 | -47.14295 | 2024-11-30 04:40:00 | NOAA-21 | GARRAFÃO DO NORTE | PARÁ | Brasil | 1503077 | 15 | 33 | nan | nan | nan | Amazônia | 7.4 |
| 9b363bfb-0cac-31a5-bba0-5d6a3b22d8b4 | -2.63711 | -49.90562 | 2024-11-30 04:40:00 | NOAA-21 | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| a67f9d52-0d98-3709-a1df-2a710c8441a2 | -3.01074 | -49.53936 | 2024-11-30 04:40:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 3f82832b-0085-3014-af9f-38ee00bd8c69 | -3.05759 | -54.04412 | 2024-11-30 04:40:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 8448f633-2338-3bfe-a594-97c9470e3f75 | -4.37357 | -50.88239 | 2024-11-30 04:40:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 72ebc1d6-d0e7-33e1-9276-01c80b0f269b | -3.59986 | -49.9917 | 2024-11-30 04:40:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 2f9d9461-4ba6-3309-8548-2ae606dff961 | -1.30691 | -51.7309 | 2024-11-30 04:40:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 36a5caa3-63ba-3683-828d-1726c14fd7cb | -2.00415 | -47.83661 | 2024-11-30 04:40:00 | NOAA-21 | SÃO DOMINGOS DO CAPIM | PARÁ | Brasil | 1507201 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| d45734cd-32e1-353f-b16a-53239d31a170 | -3.1909 | -54.33059 | 2024-11-30 04:40:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 30eedfb1-eda5-3a58-8635-3a8d164f02b6 | -2.82461 | -54.09211 | 2024-11-30 04:40:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| dc383078-cac8-3305-a6a8-f01f9f52e493 | -2.34345 | -50.57561 | 2024-11-30 04:40:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| bf10aea7-707e-31bb-a583-b03fdb9a65ba | -3.09444 | -54.02091 | 2024-11-30 04:40:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 09ab53f2-ef57-3270-82ce-477c1e9d6540 | -1.84484 | -47.65802 | 2024-11-30 04:40:00 | NOAA-21 | SÃO DOMINGOS DO CAPIM | PARÁ | Brasil | 1507201 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 951088ce-4288-3927-aa6d-71c5407c155a | -3.05646 | -54.0512 | 2024-11-30 04:40:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| f9040820-8b1c-34a9-8b80-4c3852b989ba | -2.84268 | -52.54116 | 2024-11-30 04:40:00 | NOAA-21 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 42eb8a72-06f3-3380-8db4-15a49b9d750f | -2.58548 | -51.92141 | 2024-11-30 04:40:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| c3fabbb4-ea22-3892-b135-70c384b907d2 | -2.83657 | -48.47609 | 2024-11-30 04:40:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 91edc706-5a0f-3789-b987-8bb51e0e123e | -2.97181 | -53.29301 | 2024-11-30 04:40:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 9b0e4dad-76f5-3c3a-b47e-22915487c7bc | -3.93335 | -51.17655 | 2024-11-30 04:40:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 48f33ea5-f205-3832-903e-7bb49dc13fc6 | -1.31831 | -51.91771 | 2024-11-30 04:40:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 29c0e161-e025-3ac2-851b-b384c0724592 | -3.96723 | -46.90753 | 2024-11-30 04:40:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 9e5b2300-8950-36c8-8499-438fed6d4af9 | -2.80885 | -54.03434 | 2024-11-30 04:40:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| cbefa56e-7718-34c5-abe0-738994893acd | -1.6806 | -52.52514 | 2024-11-30 04:40:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 443bdf31-89b4-3a67-a3a1-15bea487ac97 | -3.15824 | -53.23838 | 2024-11-30 04:40:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 6.7 |
| 4bb94d9f-7d21-308e-81f6-af3a2f1cb941 | -3.7858 | -50.1288 | 2024-11-30 04:40:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| b360b680-feb2-33b5-b2f2-faf8c2366875 | -3.7661 | -50.79152 | 2024-11-30 04:40:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 05813346-a4d5-38c8-9584-bc57b88ee6be | -2.95419 | -53.8834 | 2024-11-30 04:40:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 8dd77c2f-4a64-3888-99d2-9805021004b4 | -3.52965 | -49.26809 | 2024-11-30 04:40:00 | NOAA-21 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |


[Clique aqui para ver as próximas entradas](README39.md)
