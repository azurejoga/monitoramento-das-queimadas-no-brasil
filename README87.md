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

## Dados Diários - Página 87

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 3d8ba31c-89a6-3e63-a382-288b2be92530 | -3.56026 | -54.59592 | 2024-11-03 05:33:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 81e8f11c-8b30-3f6c-81e5-3734e5fa159f | -3.55823 | -54.6447 | 2024-11-03 05:33:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| fdc4ba86-2992-3935-a456-762d5e29a448 | -3.55562 | -54.59195 | 2024-11-03 05:33:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 0d7c7447-058c-313c-98ff-cc99df5e6f96 | -3.55518 | -54.59492 | 2024-11-03 05:33:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| b98c9ef7-3166-3373-8b4e-78a21258c212 | -3.55474 | -54.59787 | 2024-11-03 05:33:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 3497f005-d148-300d-be5c-73c0ac3d8ec0 | -3.55009 | -54.59399 | 2024-11-03 05:33:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 84d6a5ff-f264-3437-8132-6405062b4622 | -3.54964 | -54.59699 | 2024-11-03 05:33:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| c67609b0-2ba3-3a6b-80bc-9eb51ee36a1a | -3.54619 | -50.87671 | 2024-11-03 05:33:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 1364b44c-3562-3740-b4d0-b74202ea8813 | -3.54045 | -50.87037 | 2024-11-03 05:33:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 639b722a-aa57-347a-970f-9ee2d02ce16f | -3.52051 | -54.68877 | 2024-11-03 05:33:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 0.3 |
| 7c48f3d3-951d-3bad-bf16-ce06356753d9 | -3.51544 | -54.68793 | 2024-11-03 05:33:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 0.3 |
| 49261ae2-6c9b-3265-816d-c2b6b3deb2ab | -3.40997 | -53.80924 | 2024-11-03 05:33:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 170baeff-5b51-378a-ad91-db47a9127969 | -3.40794 | -53.80447 | 2024-11-03 05:33:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| aefb5eae-de0c-3ca9-aeac-d88f5e23bea5 | -3.40744 | -53.80792 | 2024-11-03 05:33:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 739a794d-45ac-3e97-bc5e-ae33bdb85202 | -3.40511 | -53.80502 | 2024-11-03 05:33:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e87a6257-4b3d-3d4d-ba2a-b145165f2e02 | -3.4046 | -53.80839 | 2024-11-03 05:33:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f4c42cd8-4345-3eeb-aa90-53da5fb01d26 | -3.33798 | -54.17595 | 2024-11-03 05:33:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| f4734f19-b5f6-3e52-886e-5529af80bc18 | -3.33572 | -53.79033 | 2024-11-03 05:33:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 601d4b3e-f05a-3b9a-ac48-3cd66db1ee9b | -3.33519 | -53.79395 | 2024-11-03 05:33:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 67decc84-ae1e-31a5-9947-77b8348128db | -3.33272 | -54.17526 | 2024-11-03 05:33:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 5c159606-f797-3090-8e54-fb009b536504 | -3.33085 | -53.78602 | 2024-11-03 05:33:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| bf9854ab-d46e-35d3-a877-6bcdbf5fc077 | -3.33032 | -53.7896 | 2024-11-03 05:33:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 9184d4c3-c818-344a-bc7a-0563dc0d91b9 | -3.32979 | -53.79325 | 2024-11-03 05:33:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 79c3d909-a095-3bc9-ad36-34bc01c701bf | -3.32926 | -53.79684 | 2024-11-03 05:33:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| f5256ad9-6fd0-3b80-9102-90544943b85d | -3.31095 | -52.85891 | 2024-11-03 05:33:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 481225fc-db4f-341e-9d46-2e9292b77cb3 | -3.30644 | -54.13562 | 2024-11-03 05:33:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e6c6dc85-2633-342f-9d65-ac7a3fd67816 | -3.2845 | -54.52863 | 2024-11-03 05:33:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ccea6d68-be4a-3958-a7cf-da53560cd917 | -3.28403 | -54.53168 | 2024-11-03 05:33:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| cafa4e28-c446-3a80-8ee9-d4b7901c6813 | -3.27799 | -54.53706 | 2024-11-03 05:33:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 397f234d-441f-3793-8295-2907ba592b11 | -3.27754 | -54.54 | 2024-11-03 05:33:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 20310711-aac1-33d8-8189-3d6c1dbba582 | -3.27659 | -54.78167 | 2024-11-03 05:33:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 7acc9764-94f6-3995-ab3f-a9402e5bbae4 | -3.27291 | -54.53605 | 2024-11-03 05:33:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 13d0d8d5-1d93-3d84-a04d-35cce8a1f956 | -3.27246 | -54.53903 | 2024-11-03 05:33:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b2b7b9d8-84d6-32f2-aee9-e7291a263725 | -3.27058 | -52.73453 | 2024-11-03 05:33:00 | NOAA-20 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 83181ef8-6f8a-378e-b707-09ed1439bd36 | -3.27002 | -52.73836 | 2024-11-03 05:33:00 | NOAA-20 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 34bb59cc-7036-3c88-b612-d151153993b2 | -3.25003 | -53.07257 | 2024-11-03 05:33:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 18c9a55d-749c-309f-9a98-228bb8d22306 | -3.24947 | -53.07633 | 2024-11-03 05:33:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 2a5d43ac-315f-34a0-bbfa-2e5ccecc9e32 | -3.2444 | -53.07166 | 2024-11-03 05:33:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 1e8d1ff0-4085-3d21-89dd-af9becf2e063 | -3.24383 | -53.07548 | 2024-11-03 05:33:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 6a2f76f1-8233-3216-9c4f-ead8b544f687 | -3.23129 | -59.87286 | 2024-11-03 05:33:00 | NOAA-20 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 329e07c8-fff1-3940-9434-612d05b51229 | -3.22833 | -59.86816 | 2024-11-03 05:33:00 | NOAA-20 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 6840125a-9bf5-323d-8298-e16d323dbd05 | -3.22769 | -59.8723 | 2024-11-03 05:33:00 | NOAA-20 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 360d0630-2e6f-308f-9d39-7fd65ded96b5 | -3.21128 | -54.94335 | 2024-11-03 05:33:00 | NOAA-20 | BELTERRA | PARÁ | Brasil | 1501451 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 5c7e374c-8361-3ed4-8685-3e2f757cb1de | -3.21044 | -54.9489 | 2024-11-03 05:33:00 | NOAA-20 | BELTERRA | PARÁ | Brasil | 1501451 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 5266d3f6-67f2-30eb-b33e-ca838d119052 | -3.20274 | -54.58683 | 2024-11-03 05:33:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 20d5e877-ac5e-36b9-abc5-d0a6b225c35e | -3.15455 | -54.4704 | 2024-11-03 05:33:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c1bc3c1d-fc2f-3d85-86e4-bd87ac6f1355 | -3.15408 | -54.47354 | 2024-11-03 05:33:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 6998ddd1-ba81-349a-b23c-f382652e3b40 | -3.12865 | -54.25241 | 2024-11-03 05:33:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 064561cb-d0eb-3bf7-bc1e-e3c7be4c7190 | -3.12818 | -54.25562 | 2024-11-03 05:33:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 93c00dff-79c5-3a2b-88ff-8abbcd56658c | -3.12772 | -54.25881 | 2024-11-03 05:33:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| b1e233a2-adb2-3e03-aa59-de07d321a8bd | -3.12728 | -54.25416 | 2024-11-03 05:33:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| bc88bf6e-0fc0-3e4a-8fff-9a6c9ae15655 | -3.12679 | -54.25735 | 2024-11-03 05:33:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 6d47469a-088e-3c48-a228-097201d801ec | -3.1263 | -54.26054 | 2024-11-03 05:33:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| c16a97e0-935d-3603-b6eb-b0228b70fa0f | -3.12342 | -54.25177 | 2024-11-03 05:33:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| fd830df4-3e5d-3e7e-9f8d-739b9eb0f0f5 | -3.12296 | -54.255 | 2024-11-03 05:33:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 5b78a280-ad02-3dc1-bbdc-ce4fea44f61a | -3.12254 | -54.25032 | 2024-11-03 05:33:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| d2062c6f-4a08-39c0-8271-2fef8fda73d5 | -3.12249 | -54.25821 | 2024-11-03 05:33:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 99d6d96f-a9aa-34f2-9d35-48e8c5daa2cb | -3.12205 | -54.25354 | 2024-11-03 05:33:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| d66ba230-4294-32b2-99c7-717b283b3dcf | -3.12202 | -54.26142 | 2024-11-03 05:33:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 50f8ad81-25f5-31d8-8be1-d606b0e2dd88 | -3.12191 | -54.47839 | 2024-11-03 05:33:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| e2548f3b-3894-30d4-b061-2c6db58d7649 | -3.12156 | -54.25674 | 2024-11-03 05:33:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 79297bca-305c-35e3-a824-c27548e87732 | -3.12107 | -54.25996 | 2024-11-03 05:33:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| b93020f2-27a8-3d1a-a3af-0447a5f3fef5 | -3.12058 | -54.26315 | 2024-11-03 05:33:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 23816dda-c17d-31aa-88e5-9cc41ce1f385 | -3.12009 | -54.26635 | 2024-11-03 05:33:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 6f36693d-2648-30af-a8dd-1a53a0e9c803 | -3.11774 | -54.25429 | 2024-11-03 05:33:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 6a211973-a17b-35ee-955a-e9df7b292a76 | -3.11728 | -54.25749 | 2024-11-03 05:33:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 77b714a1-324c-35cb-9897-db0ed961c74a | -3.11726 | -54.47446 | 2024-11-03 05:33:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 32d76e1f-6b16-35c7-bc75-bac5f6bbee96 | -3.11681 | -54.2607 | 2024-11-03 05:33:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 0bca291f-64a4-3360-b80f-c32670690a50 | -3.11635 | -54.26391 | 2024-11-03 05:33:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| ae77e1f1-66dd-3f67-ae83-5ecc8ab5023c | -3.11635 | -54.25602 | 2024-11-03 05:33:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 0304f44a-f550-3514-b740-bd11b698ebf9 | -3.11586 | -54.25923 | 2024-11-03 05:33:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 56fd5f87-e3e5-3e04-860f-2c1300a90af2 | -3.11538 | -54.26242 | 2024-11-03 05:33:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 4479c7e0-1804-3124-9472-8ee0b11fc15b | -3.11489 | -54.26561 | 2024-11-03 05:33:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d9afff71-92bd-3c20-ab4a-9f3571fe38d1 | -3.1118 | -54.29536 | 2024-11-03 05:33:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| f80b2470-77e0-3fea-90af-2247275aabd3 | -3.11135 | -54.29845 | 2024-11-03 05:33:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| e802d9aa-0852-3955-b549-e21cf55db940 | -3.11058 | -54.29383 | 2024-11-03 05:33:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| f18d0236-2210-3316-9840-b9a2d155809d | -3.11011 | -54.29694 | 2024-11-03 05:33:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 189e8ae6-ac1e-39f3-a8f6-e50ce85f70b3 | -3.10661 | -54.47564 | 2024-11-03 05:33:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 90224845-8b28-3a90-adb9-62917a1fb819 | -3.10617 | -54.47861 | 2024-11-03 05:33:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 4c3fc3ee-2748-3b35-aad7-605b46d9f53a | -3.1054 | -54.29305 | 2024-11-03 05:33:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 8a6e9562-d7d8-3fc3-9f52-ca0eb94505e5 | -3.10021 | -54.29227 | 2024-11-03 05:33:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 67f639f5-e272-349e-8423-ae180e71a704 | -3.09958 | -53.71382 | 2024-11-03 05:33:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 22baf0bf-e5a5-32c6-bbe2-5d8eab1dc359 | -3.09908 | -53.71724 | 2024-11-03 05:33:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 8107665d-78b3-37d9-aad1-bed73a502c60 | -3.09736 | -53.71353 | 2024-11-03 05:33:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 25f85f97-a9d7-34dc-8f40-e50fd7467346 | -3.09684 | -53.71695 | 2024-11-03 05:33:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 184bf97e-3bf5-3991-ba1c-b90acca62ce6 | -3.09632 | -53.72035 | 2024-11-03 05:33:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 0082c097-6018-39f2-8614-b1734353260f | -3.09369 | -53.71643 | 2024-11-03 05:33:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 0f427b08-9036-3745-b362-e70dbc719a75 | -3.08328 | -54.15693 | 2024-11-03 05:33:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 3099a8af-e746-3419-88fc-7dc881a37178 | -3.0828 | -54.16013 | 2024-11-03 05:33:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 770aeadf-c408-3b0f-9d3f-cb30d9fd8b77 | -3.0785 | -54.15312 | 2024-11-03 05:33:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 64d5b3f5-5333-3fec-8068-c898ec25bc05 | -3.07803 | -54.15628 | 2024-11-03 05:33:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| dbe81b5c-ca12-31c6-8fd4-acffc4f21507 | -3.07756 | -54.15944 | 2024-11-03 05:33:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 81c83159-65d8-3640-834d-96d58fa47130 | -3.07708 | -54.16264 | 2024-11-03 05:33:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 4db1ee57-575e-39ae-96a7-1fe039eae1a0 | -3.07659 | -54.1659 | 2024-11-03 05:33:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 4a365d8a-307c-327e-9c39-34dbd8e9b317 | -3.07372 | -54.14925 | 2024-11-03 05:33:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 2acfc2d2-0a9a-3dfd-8b6b-73bb15e5ecc4 | -3.07325 | -54.15242 | 2024-11-03 05:33:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 9cbaffa5-80e7-34fc-8399-1a990ac9a14e | -3.07278 | -54.15561 | 2024-11-03 05:33:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| d86405f9-3722-348e-ace3-82b40d438988 | -3.0723 | -54.15878 | 2024-11-03 05:33:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| f3d9cf49-199b-3069-b697-876571eb9a47 | -3.07183 | -54.16196 | 2024-11-03 05:33:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| c827beea-4a03-3be4-9051-6e610de8a941 | -3.07135 | -54.16521 | 2024-11-03 05:33:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |


[Clique aqui para ver as próximas entradas](README88.md)
