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

## Dados Diários - Página 22

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| e9cee9ce-81de-39b5-bde2-fe28880242a0 | -2.63272 | -54.65691 | 2024-11-08 04:53:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 13a097f6-a2f6-3307-8214-b95293eb5128 | -2.16281 | -53.64812 | 2024-11-08 04:53:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 12.1 |
| 7ce8bfed-8a41-36cd-8ebb-f220a3161d40 | -4.77912 | -48.67655 | 2024-11-08 04:53:00 | NOAA-21 | BOM JESUS DO TOCANTINS | PARÁ | Brasil | 1501576 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| e1cfc99d-2e96-39f3-9518-5f2cb30d0a1d | -3.016 | -53.42306 | 2024-11-08 04:53:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 658b35db-9dbb-3ca8-9e1f-e0430e78257a | -3.94963 | -48.15509 | 2024-11-08 04:53:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 413d8ff6-a4d8-3e27-9ec3-3d8a33afcef2 | -3.08063 | -52.42548 | 2024-11-08 04:53:00 | NOAA-21 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 534853b1-ad3c-3a87-bcb3-c93da6976fdb | -1.57523 | -51.30386 | 2024-11-08 04:53:00 | NOAA-21 | MELGAÇO | PARÁ | Brasil | 1504505 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 77e31790-533e-34e6-bc3c-4320338d3358 | -4.24792 | -48.53532 | 2024-11-08 04:53:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| d1e54dff-3a16-359f-bb3e-eb65afc24796 | -2.28264 | -53.82167 | 2024-11-08 04:53:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 788df2e3-6644-3ad0-bcda-25c438c3fe03 | -4.34933 | -48.62363 | 2024-11-08 04:53:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| c56e9ee6-1b02-3946-af93-9f4c12855683 | -1.38439 | -52.87449 | 2024-11-08 04:53:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| d9eff066-9904-3eb8-a6b2-027b0a2fffe9 | -1.6832 | -51.921 | 2024-11-08 04:53:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 7a9e8f18-d16c-3c37-8187-8bc26ebc2707 | -2.69144 | -51.82595 | 2024-11-08 04:53:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b791575e-36c2-3792-a64e-5e58317d87fc | -2.27921 | -53.82116 | 2024-11-08 04:53:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 1dd899a9-6a6e-3b03-be01-dacb5d859dea | -10.7267 | -49.82657 | 2024-11-08 04:53:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 9a0d350e-d84f-39a6-95bd-8bfd8882fd8d | -0.93111 | -47.13278 | 2024-11-08 04:53:00 | NOAA-21 | PRIMAVERA | PARÁ | Brasil | 1506104 | 15 | 33 | nan | nan | nan | Amazônia | 7.0 |
| adf55f85-e92a-3856-9ee2-025bb1659ec1 | -3.03291 | -51.53105 | 2024-11-08 04:53:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 7.0 |
| 814f087d-2a17-34c3-b831-a9babf684a09 | -4.39627 | -49.76947 | 2024-11-08 04:53:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 8c5b3c6e-3810-3c6b-87bd-1891d43c472f | -1.15302 | -52.00358 | 2024-11-08 04:53:00 | NOAA-21 | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 9.4 |
| c58b6cbd-22c2-3b56-af9c-954b66d33dca | -2.80729 | -51.8024 | 2024-11-08 04:53:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| e7a59cc1-7d2d-385a-95a1-77e0cac76437 | -10.72296 | -49.82601 | 2024-11-08 04:53:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 039952bd-2372-3fb8-a711-a95f47a91cf4 | -0.04261 | -50.78978 | 2024-11-08 04:53:00 | NOAA-21 | AFUÁ | PARÁ | Brasil | 1500305 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| b1505e3a-c2fb-3ab8-80cc-57d752bf3e22 | -1.32388 | -52.23832 | 2024-11-08 04:53:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| d60e35f8-712d-3dae-9a42-cb155b2871a6 | -5.23235 | -45.6647 | 2024-11-08 04:53:00 | NOAA-21 | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 9ebe08a7-8ad5-3746-936a-e0ef2181367e | -1.38774 | -52.875 | 2024-11-08 04:53:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 6.9 |
| c4603106-115a-3e49-b4d0-92a1be719f89 | -3.22748 | -50.38047 | 2024-11-08 04:53:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f24b8f3a-2e26-3bbf-9abe-2d3fde8d7785 | -2.05962 | -53.27483 | 2024-11-08 04:53:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 34b2e04a-1ed5-380f-8187-9edaf5567fcb | -1.38943 | -52.20948 | 2024-11-08 04:53:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 464c3286-b729-3868-9191-a01b7c0931e4 | -5.64183 | -44.24632 | 2024-11-08 04:53:00 | NOAA-21 | SÃO DOMINGOS DO MARANHÃO | MARANHÃO | Brasil | 2110708 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 200a1c9a-726f-3d7f-b07a-84dae3dffaff | -1.15153 | -53.64819 | 2024-11-08 04:53:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| fa58f421-1a62-3204-9306-dcedd47df560 | -3.33525 | -51.62072 | 2024-11-08 04:53:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 2a9425b3-96ce-3337-b78e-8a8bd94a32ec | -4.5594 | -46.34183 | 2024-11-08 04:53:00 | NOAA-21 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ffa442b7-dbcc-3112-8c3a-842c3eebfd40 | -2.81006 | -51.80634 | 2024-11-08 04:53:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 710ae8fa-2ead-3d72-b53c-a5de4f507532 | -1.27942 | -54.13173 | 2024-11-08 04:53:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 0b9502f0-79b4-3d86-85b9-98edf9c6c1fa | -2.15884 | -53.64723 | 2024-11-08 04:53:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 7.1 |
| 8d366965-d0be-355e-8abe-450dd1515ddc | -3.23638 | -53.40633 | 2024-11-08 04:53:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 589a97be-d88f-3f80-aab8-491888f7177d | -4.6936 | -46.37344 | 2024-11-08 04:53:00 | NOAA-21 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 44809cc2-d731-3afa-a4c3-bb96ce294cfa | -3.01105 | -53.23623 | 2024-11-08 04:53:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 27965c76-16ed-3c81-80ac-9d51db057004 | -0.67166 | -51.66428 | 2024-11-08 04:53:00 | NOAA-21 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 5ee2c538-fc6f-31c8-a55b-71ed3502af4e | -5.98469 | -45.3598 | 2024-11-08 04:53:00 | NOAA-21 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 6.7 |
| bc5e0aa3-7847-3b60-8890-65d6feed290a | -2.77161 | -54.03778 | 2024-11-08 04:53:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 2da25fd2-64c5-377c-9ba9-415f6fafa8b0 | -3.2378 | -50.44865 | 2024-11-08 04:53:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 5fb9ee65-8eea-3d32-b211-f1c57d103182 | -1.12889 | -53.7255 | 2024-11-08 04:53:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d2d35da3-e62a-3263-b84e-6eba14e98e6e | -5.98397 | -45.36483 | 2024-11-08 04:53:00 | NOAA-21 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 155b7898-ffcc-3fc5-9dcb-43a31421035d | -3.44635 | -46.08307 | 2024-11-08 04:53:00 | NOAA-21 | GOVERNADOR NEWTON BELLO | MARANHÃO | Brasil | 2104651 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 8ac85b11-784f-32f6-9e2d-d96a29f689b1 | 0.30048 | -51.1333 | 2024-11-08 04:53:00 | NOAA-21 | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 1.5 |
| cec9dc11-1254-3ccc-89ef-a956497fca4f | -2.80186 | -52.94694 | 2024-11-08 04:53:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 13.3 |
| f4c67d4a-0f25-3992-ac87-d90fd671e866 | -2.15448 | -51.23155 | 2024-11-08 04:53:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| c253694c-b448-3e1c-82dd-f30258c37d93 | -1.57179 | -52.13235 | 2024-11-08 04:53:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 7ab9aa4f-d2fa-3bef-80ea-bae9fda8acf6 | -2.8275 | -52.91141 | 2024-11-08 04:53:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 53c47c71-8778-3128-abad-0b4294de9b31 | -2.60285 | -48.19621 | 2024-11-08 04:53:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 40330085-f08f-3779-b867-fefa7f67c713 | -4.61212 | -49.5841 | 2024-11-08 04:53:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 3f1ff4ff-ed92-312b-bcf8-81ea209ffb5a | -0.16931 | -51.41695 | 2024-11-08 04:53:00 | NOAA-21 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 537773f1-85ae-37bf-a6a4-f387912c35a1 | -3.25096 | -53.40121 | 2024-11-08 04:53:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c59d66f9-c055-3959-bbfd-6762623dd18c | -1.56285 | -52.25458 | 2024-11-08 04:53:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 93e3a069-ba1f-3922-afc9-484e0d8bb45d | -1.50655 | -52.06942 | 2024-11-08 04:53:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 84018d58-2a0b-3216-8308-94d5e5660eeb | -4.67784 | -46.44891 | 2024-11-08 04:53:00 | NOAA-21 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 916f25bc-a93e-3bbf-8a8c-b11392be5435 | -3.37749 | -50.22449 | 2024-11-08 04:53:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 10.5 |
| d21cc503-b136-3d65-a491-390bcae2304e | -3.5241 | -51.52329 | 2024-11-08 04:53:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 35868651-3602-3f6c-8575-dcc7af5cf674 | -0.93186 | -47.12794 | 2024-11-08 04:53:00 | NOAA-21 | PRIMAVERA | PARÁ | Brasil | 1506104 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 77539fa5-0638-33cc-9f02-fc32a09d08b8 | -1.16506 | -53.71988 | 2024-11-08 04:53:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| effeea2a-cc00-36c2-b006-e71768bece1f | -3.24345 | -50.45687 | 2024-11-08 04:53:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 53dc88de-ee89-309b-bd64-d9caaa55271c | -3.96965 | -48.12524 | 2024-11-08 04:53:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 60a1d133-8fc1-3153-8240-c7b84a6f6d0b | -3.11439 | -51.29258 | 2024-11-08 04:53:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| bd6c4dc1-279a-3e23-a11b-6ab49ae9631b | -3.04961 | -53.27483 | 2024-11-08 04:53:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 1decbfcb-3057-37c0-9cce-eb2189056fab | -4.4748 | -48.11375 | 2024-11-08 04:53:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b113a460-3c1e-3b93-babc-6a4d45494035 | -5.29917 | -44.85036 | 2024-11-08 04:53:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| cdd2bea9-e2a1-303b-acd7-43207d7f2299 | -1.6299 | -53.43877 | 2024-11-08 04:53:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 8c651950-03ef-356c-beb0-95b092675a82 | -5.54285 | -44.32949 | 2024-11-08 04:53:00 | NOAA-21 | SÃO DOMINGOS DO MARANHÃO | MARANHÃO | Brasil | 2110708 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 86cd047c-a797-35b9-b01d-30b086e45868 | -2.95913 | -53.71789 | 2024-11-08 04:53:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| bd4da9ed-5898-35d0-86b2-d0da3ea36751 | -2.72898 | -51.73689 | 2024-11-08 04:53:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| cd42582a-a98a-370b-91a6-12f16183319d | -3.24314 | -45.68641 | 2024-11-08 04:53:00 | NOAA-21 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 06a7ea96-591d-30fe-8f5e-7b7bdfcfb896 | -2.6321 | -54.66089 | 2024-11-08 04:53:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 823de4ed-ba15-3f15-95a6-ef12bd2067af | -1.14748 | -51.99568 | 2024-11-08 04:53:00 | NOAA-21 | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 02c4c211-2b4b-3b2e-89c6-7906981131b9 | -2.23952 | -53.67121 | 2024-11-08 04:53:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| bffcc0d5-485b-3347-8fbf-4d9543ed47af | -1.76231 | -52.34974 | 2024-11-08 04:53:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| b03c246e-2190-30b1-8f9c-8b39beaf7a43 | -2.72888 | -51.71579 | 2024-11-08 04:53:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 2b8fe612-e753-3e78-b8ec-ba620833a01f | -3.00643 | -53.43997 | 2024-11-08 04:53:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 421edf57-33f5-3e4b-a339-bedc07067da1 | -1.4427 | -52.82539 | 2024-11-08 04:53:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 7b8d9433-43c7-3ef4-b36e-cde09799ae72 | -3.06216 | -52.50032 | 2024-11-08 04:53:00 | NOAA-21 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 89fdf0df-2c4d-355a-b741-1092874a6767 | -6.96713 | -45.47119 | 2024-11-08 04:53:00 | NOAA-21 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| e91d0c40-7c6b-3372-a354-d1e9d4e2687f | -2.14917 | -48.82765 | 2024-11-08 04:53:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 191cdbc5-7d7a-372d-9ebf-25bd97c053d1 | -0.37135 | -51.43117 | 2024-11-08 04:53:00 | NOAA-21 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 2.5 |
| b63076dc-ef8c-35bd-8887-b91a40f70a4e | -1.81881 | -54.43839 | 2024-11-08 04:53:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| abd72719-2c04-346f-b9f4-6429c5ae3cb1 | -10.73045 | -49.82713 | 2024-11-08 04:53:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 7392b549-c586-3506-9c57-a8bdb1891b4e | -0.16853 | -51.48696 | 2024-11-08 04:53:00 | NOAA-21 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 0.7 |
| ff30d868-336b-3b24-906b-f5aa03bf4ab3 | -4.07929 | -43.35891 | 2024-11-08 04:53:00 | NOAA-21 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 5f8e2fcc-7489-3ba5-9e73-ab014e0cfe07 | -1.16648 | -54.20381 | 2024-11-08 04:53:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| f192e48c-6a87-3546-85cd-6592240b80c9 | -1.98469 | -45.61224 | 2024-11-08 04:53:00 | NOAA-21 | TURIAÇU | MARANHÃO | Brasil | 2112407 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 5a8493a8-fc12-35bb-8eeb-5830e3cf9dc5 | -2.46882 | -53.97653 | 2024-11-08 04:53:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| c62ae0ba-0cf1-3444-b6f8-5570ec09e23f | -4.99083 | -46.81939 | 2024-11-08 04:53:00 | NOAA-21 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f364aa72-ad4a-3e15-9d6f-787ee05adf67 | -2.14098 | -56.17982 | 2024-11-08 04:53:00 | NOAA-21 | NHAMUNDÁ | AMAZONAS | Brasil | 1303007 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| dbb88814-6285-3b48-bb27-d84fbffa7397 | -1.37804 | -52.26078 | 2024-11-08 04:53:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| b6cd90a5-e3ea-312e-a896-81f66410c3ba | -3.29435 | -50.07968 | 2024-11-08 04:53:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 0d028e27-591c-3744-aee5-0744fc219fde | -3.97478 | -48.40266 | 2024-11-08 04:53:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 6cdbd47f-3067-3f9d-9531-a92b1c2e86ea | -3.29169 | -53.25093 | 2024-11-08 04:53:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 44655049-8fa7-34b8-a3b8-2381f02091e8 | -3.19606 | -53.40001 | 2024-11-08 04:53:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 91c0db0f-de01-3119-9cdc-612f2edce415 | -0.97192 | -52.44296 | 2024-11-08 04:53:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 39d6779e-596a-3759-830b-6dbe68ba25ef | -2.29686 | -48.55421 | 2024-11-08 04:53:00 | NOAA-21 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 6e7c8f79-6ceb-39f5-9176-f30a8f06bea2 | -4.07347 | -48.31438 | 2024-11-08 04:53:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |


[Clique aqui para ver as próximas entradas](README23.md)
