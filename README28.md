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

## Dados Diários - Página 28

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 920d5e9c-c24e-3da9-87ae-3c6317ad4863 | -6.22067 | -43.33685 | 2025-08-15 04:27:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| a5294e27-4c88-31ca-b1a7-4a738924f5a1 | -6.87309 | -59.8428 | 2025-08-15 04:27:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 5ae70318-62d6-3fed-b790-9191ea405519 | -3.9437 | -41.83087 | 2025-08-15 04:27:00 | NPP-375D | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 40661a00-c078-3382-a523-65f2436eebf0 | -4.7102 | -47.44526 | 2025-08-15 04:27:00 | NPP-375D | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 799bc661-6451-3ce0-9aad-54627b88ff1b | -4.8938 | -45.53339 | 2025-08-15 04:27:00 | NPP-375D | LAGOA GRANDE DO MARANHÃO | MARANHÃO | Brasil | 2105963 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 513cfc21-5480-3185-9294-e4ffcaff8be9 | -6.95032 | -44.55233 | 2025-08-15 04:27:00 | NPP-375D | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 2810d837-5245-3272-88c0-3632c5b44b00 | -2.90809 | -48.25011 | 2025-08-15 04:27:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 472e63ab-fe08-30a5-a182-ed33af0003a8 | -6.66623 | -58.82297 | 2025-08-15 04:27:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 8.2 |
| 99dc95fe-3255-33e8-a7f3-090560945c6b | -4.98196 | -41.71836 | 2025-08-15 04:27:00 | NPP-375D | SIGEFREDO PACHECO | PIAUÍ | Brasil | 2210656 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| f88cc50f-ab81-3f6b-a827-1ed2726e5034 | -7.39603 | -44.8773 | 2025-08-15 04:27:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 6b32962c-8824-33fc-b9c9-a7623f2f51ef | -6.9143 | -59.14826 | 2025-08-15 04:27:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 955b4307-fc4e-3b8f-ae1f-4e537b9ae8cb | -8.30345 | -45.00843 | 2025-08-15 04:27:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| a7530252-558e-32a9-ba70-b3f2dae1df87 | -4.59144 | -43.32095 | 2025-08-15 04:27:00 | NPP-375D | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 73ce9d53-9ada-39ef-bff1-b09d482a6fa9 | -7.42725 | -44.58237 | 2025-08-15 04:27:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| e0796abe-3eb3-35d9-b204-30b17a29499b | -6.66726 | -58.81732 | 2025-08-15 04:27:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 8.6 |
| 759452fd-48a7-3bd9-a373-adf306b74efd | -10.53768 | -42.54789 | 2025-08-15 04:27:00 | NPP-375D | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Caatinga | 2.9 |
| f8640e0b-df10-3982-a8fe-5279136f786b | -7.00901 | -43.86262 | 2025-08-15 04:27:00 | NPP-375D | MARCOS PARENTE | PIAUÍ | Brasil | 2206001 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 17209841-bb2b-30b4-bd2d-86a1f063edee | -6.89187 | -59.15619 | 2025-08-15 04:27:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a29aab65-2676-3723-917c-61be4e74be03 | -4.18879 | -40.75603 | 2025-08-15 04:27:00 | NPP-375D | GUARACIABA DO NORTE | CEARÁ | Brasil | 2305001 | 23 | 33 | nan | nan | nan | Caatinga | 0.8 |
| ad0e8e4f-0ce5-39e5-b374-3d2f1709d1a2 | -6.91216 | -45.211 | 2025-08-15 04:27:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 4.8 |
| c296cdca-c170-346f-bc05-ef5824518dde | -7.33601 | -60.62245 | 2025-08-15 04:27:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| f8d3d66d-48c7-3c4c-96dd-8a82053ffc05 | -6.93709 | -59.63015 | 2025-08-15 04:27:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 6b91719c-3f5c-3fbe-857f-6dfbb612ab54 | -8.37759 | -46.99649 | 2025-08-15 04:27:00 | NPP-375D | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 7eae73df-480e-3470-ae87-a3a71e29d80b | -6.65733 | -58.81529 | 2025-08-15 04:27:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 41c1351e-fdc9-3a5f-a244-669fc64a83ee | -6.07762 | -59.94539 | 2025-08-15 04:27:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 10.3 |
| c9915c75-b298-3313-8a12-353cca84017a | -6.71027 | -58.82552 | 2025-08-15 04:27:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 8.6 |
| b9f62f0b-a4a1-3d64-b347-e2e26d94c3a6 | -7.09053 | -59.22028 | 2025-08-15 04:27:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.8 |
| f2887f4d-d2a9-37c4-9cef-8c5ebccca32d | -7.90974 | -46.85365 | 2025-08-15 04:27:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 92303eb0-c167-3a64-9dbb-04ee21bf6a96 | -7.00961 | -43.85874 | 2025-08-15 04:27:00 | NPP-375D | MARCOS PARENTE | PIAUÍ | Brasil | 2206001 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 481ec05e-4eea-396f-92c4-acb324ba8b96 | -9.21552 | -45.33732 | 2025-08-15 04:27:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 6c6be804-06e5-3106-8c1d-1f0122bb2ef3 | -6.10287 | -59.92853 | 2025-08-15 04:27:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 6638b903-c9a2-3427-ac24-1d6e710b8c8a | -6.77814 | -44.35679 | 2025-08-15 04:27:00 | NPP-375D | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| aca9775c-29f0-3f69-b7ef-e67dfa01d7ef | -5.78423 | -43.60493 | 2025-08-15 04:27:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 882190c1-3995-3c47-a379-0fb70ca848f4 | -4.66711 | -48.86883 | 2025-08-15 04:27:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| a1bab2cb-32e3-3fee-bda8-4fde0f06ea03 | -6.65517 | -58.82673 | 2025-08-15 04:27:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 7.6 |
| 0c29f252-ace4-3a24-9529-61d2ce861b04 | -5.19367 | -46.07669 | 2025-08-15 04:27:00 | NPP-375D | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| d1a2a04d-0e50-3268-aa28-45acabc9e429 | -6.89971 | -59.15166 | 2025-08-15 04:27:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| c3a51df8-adaa-339b-8778-8c027771f88e | -7.07261 | -59.20415 | 2025-08-15 04:27:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 6dbac933-7fcb-3445-948e-54bf0022144b | -4.43186 | -40.9239 | 2025-08-15 04:27:00 | NPP-375D | CROATÁ | CEARÁ | Brasil | 2304236 | 23 | 33 | nan | nan | nan | Caatinga | 0.6 |
| aa4740da-ae96-311a-bc76-8a9a6fc0fc63 | -3.98674 | -47.88934 | 2025-08-15 04:27:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 2003236f-fd3e-3bc6-80a5-e26d63fe3d9b | -9.18222 | -45.32842 | 2025-08-15 04:27:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 10.9 |
| 20ead65d-3f3d-3a41-bfc5-a86a66dc025e | -9.958 | -48.33366 | 2025-08-15 04:27:00 | NPP-375D | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 876fc2fe-7328-3f41-a581-58dbb50b0f9e | -7.61136 | -45.19864 | 2025-08-15 04:27:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 136de31f-cf5b-3b03-911d-2e1eded85c54 | -9.18278 | -45.32478 | 2025-08-15 04:27:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 11.0 |
| d4fded80-6b0a-3252-a06b-0a8ad90362a9 | -4.39039 | -41.90929 | 2025-08-15 04:27:00 | NPP-375D | PIRIPIRI | PIAUÍ | Brasil | 2208403 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 5cb373d1-4396-3864-a1d1-66a75f910969 | -5.82574 | -47.87336 | 2025-08-15 04:27:00 | NPP-375D | ARAGUATINS | TOCANTINS | Brasil | 1702208 | 17 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b7d0124a-12c9-3566-ba59-9778ab8de046 | -2.58807 | -51.92384 | 2025-08-15 04:27:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d1ff6bca-064b-3cc4-9722-2337ccebf434 | -6.7215 | -58.82313 | 2025-08-15 04:27:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 55fb7ec5-97ab-3b7e-a8b6-310b89aa9815 | -6.94952 | -59.99932 | 2025-08-15 04:27:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 0e38337f-1189-35ca-aced-5fae8efa52c4 | -7.33676 | -60.61745 | 2025-08-15 04:27:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 5e9fa585-bcfd-32b4-9115-05fe5bc93e01 | -7.45978 | -60.41075 | 2025-08-15 04:27:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 83a30c92-0641-36b8-b710-c42005f88a14 | -6.55394 | -49.4954 | 2025-08-15 04:27:00 | NPP-375D | XINGUARA | PARÁ | Brasil | 1508407 | 15 | 33 | nan | nan | nan | Amazônia | 7.8 |
| 0dce9b63-de83-3856-bdf5-19e79c21b114 | -9.74373 | -48.57714 | 2025-08-15 04:27:00 | NPP-375D | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 6dc964ba-d413-3b53-88e5-426c65f70f46 | -6.68939 | -58.8272 | 2025-08-15 04:27:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 18f6a09e-a0b0-3402-aefe-113eebabc49c | -6.89876 | -59.14436 | 2025-08-15 04:27:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 9d201407-a8b8-3781-a728-f5388df80336 | -7.39937 | -44.8554 | 2025-08-15 04:27:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 58c78eb1-746f-3bcc-a6fc-460c6c0f7722 | -4.69032 | -43.24365 | 2025-08-15 04:27:00 | NPP-375D | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| c0fbe406-b479-3770-979e-6d66a24c8167 | -7.07108 | -59.2238 | 2025-08-15 04:27:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.0 |
| f9087cf0-b56b-3bbd-a43d-437c49f21d54 | -10.10012 | -46.71706 | 2025-08-15 04:27:00 | NPP-375D | SÃO FÉLIX DO TOCANTINS | TOCANTINS | Brasil | 1720150 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 96b9cf8d-c364-3e1a-84d5-4d24ae0726ec | -8.19428 | -42.26023 | 2025-08-15 04:27:00 | NPP-375D | PEDRO LAURENTINO | PIAUÍ | Brasil | 2207934 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| d36e98e0-b274-3416-b351-e0e61465f399 | -6.7113 | -58.8199 | 2025-08-15 04:27:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 90a8bf93-149d-3f24-b901-d1cd5e911074 | -8.31081 | -45.02831 | 2025-08-15 04:27:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 261b80da-9645-3fc2-b0db-e20a913db4f9 | -2.90386 | -48.2536 | 2025-08-15 04:27:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 35904e7c-4db8-3477-b6a7-2afad1e734dd | -6.60926 | -43.88677 | 2025-08-15 04:27:00 | NPP-375D | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 8d8ba4a1-c843-3ea2-af85-42c09149e038 | -6.88424 | -59.14756 | 2025-08-15 04:27:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 0273d2d8-fc19-3dd4-9d13-d9b59cfb3787 | -4.22632 | -47.21667 | 2025-08-15 04:27:00 | NPP-375D | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 44aa2ea0-b186-3a60-b1db-c3a708e362e7 | -7.09162 | -44.42949 | 2025-08-15 04:27:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 423248a2-fd74-34ef-920e-886141b74b5d | -6.70493 | -58.85437 | 2025-08-15 04:27:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| cd9bcc7f-f604-3705-a812-92a656467146 | -5.22422 | -43.19159 | 2025-08-15 04:27:00 | NPP-375D | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 8c366211-99e7-3f2b-9fb7-d3ddca1cfa71 | -5.6833 | -43.65316 | 2025-08-15 04:27:00 | NPP-375D | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| d7ea0d18-fa43-3c7d-b8aa-bfd24fd57f16 | -6.10747 | -59.9436 | 2025-08-15 04:27:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 615c7ec3-4362-3a57-bef8-2a289fce81a9 | -7.45257 | -60.40957 | 2025-08-15 04:27:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 783e5ca4-0cf7-39ad-8469-766127b4623a | -2.91398 | -48.30518 | 2025-08-15 04:27:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 2f76f86b-fcd2-3066-a2ab-60a7ece95b17 | -3.81827 | -41.56867 | 2025-08-15 04:27:00 | NPP-375D | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 3b0ea05c-8475-3bb8-9c64-dd59706d9b2c | -4.59434 | -43.32536 | 2025-08-15 04:27:00 | NPP-375D | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 55daeb55-4dd1-32dc-9888-03f0352e7f58 | -4.43324 | -40.92564 | 2025-08-15 04:27:00 | NPP-375D | CROATÁ | CEARÁ | Brasil | 2304236 | 23 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 0d4d0c29-7d91-3a2d-bd5b-df82ee1a886a | -8.30855 | -45.02047 | 2025-08-15 04:27:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 3248bd5b-4ae5-3f65-be7f-e0deaa733b9b | -7.44937 | -49.24647 | 2025-08-15 04:27:00 | NPP-375D | PAU D'ARCO | TOCANTINS | Brasil | 1716307 | 17 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 20ed11ea-d0e3-3c01-9afe-7c853c9bcacd | -6.089 | -59.94059 | 2025-08-15 04:27:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 88a7a1ff-ca82-3399-8e30-d31b575a48d1 | -7.37886 | -44.89363 | 2025-08-15 04:27:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 50e03b5a-0967-3389-9070-c8d9f6d68a93 | -3.42514 | -49.04867 | 2025-08-15 04:27:00 | NPP-375D | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 0c0e217a-94ff-37fb-8c25-15c94da7104b | -6.76671 | -44.33982 | 2025-08-15 04:27:00 | NPP-375D | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 3b37e860-064d-3cde-b393-a8a07325ba75 | -9.81393 | -47.75424 | 2025-08-15 04:27:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| ac0ad358-2fc4-3d71-8549-551121644d6d | -7.59933 | -55.19367 | 2025-08-15 04:27:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 41170771-d63a-3247-ae96-02598b2bcbc9 | -6.94115 | -60.00474 | 2025-08-15 04:27:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| b8691a20-f40b-318d-af7b-52daea44dee0 | -6.87843 | -59.15352 | 2025-08-15 04:27:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.7 |
| d8366731-72d9-3426-8dc7-b83589a87c71 | -4.39078 | -41.91174 | 2025-08-15 04:27:00 | NPP-375D | PIRIPIRI | PIAUÍ | Brasil | 2208403 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| edb5f11a-1fae-31af-9bd9-c4b81b3508a1 | -6.90648 | -59.63232 | 2025-08-15 04:27:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| b85d9033-605c-3842-bf4e-f0a704c4c193 | -7.31204 | -60.62845 | 2025-08-15 04:27:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 3fa16cb1-1931-3047-9387-25b1d046c9d2 | -5.60143 | -45.37779 | 2025-08-15 04:27:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| a1fea624-483d-3737-b2f9-2dcf1c12b4d3 | -3.64684 | -48.32324 | 2025-08-15 04:27:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| cb9268bb-6fe6-3196-b23f-13045f3301e9 | -6.72454 | -58.82242 | 2025-08-15 04:27:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c42a13d7-f344-3d94-8b50-09dc1fc24c9b | -7.2418 | -57.67996 | 2025-08-15 04:27:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 75b467f7-de45-3723-873a-e093200e0ede | -6.72595 | -58.83571 | 2025-08-15 04:27:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 7.9 |
| 0ccfafdb-9933-37bf-86f4-392dbf4379af | -6.90437 | -59.15171 | 2025-08-15 04:27:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| e6730c9d-ba7c-3102-999e-5914b0074604 | -8.37427 | -46.99596 | 2025-08-15 04:27:00 | NPP-375D | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| ace02d77-ef88-3f55-96f3-6b8a17951f82 | -5.61756 | -43.46946 | 2025-08-15 04:27:00 | NPP-375D | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 9efe1970-291c-358c-8607-abd498cbab83 | -5.76585 | -46.67282 | 2025-08-15 04:27:00 | NPP-375D | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 8164f335-30a6-375b-b784-06802aceb90a | -7.46655 | -45.93092 | 2025-08-15 04:27:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| e953a387-b269-33fd-803d-03c74c746f25 | -8.51053 | -43.32727 | 2025-08-15 04:27:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |


[Clique aqui para ver as próximas entradas](README29.md)
