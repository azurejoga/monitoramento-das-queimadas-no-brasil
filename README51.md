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

## Dados Diários - Página 51

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 4d546808-25c3-38d2-840c-e3ef90ce712b | -2.95467 | -49.58234 | 2024-12-02 04:48:00 | NOAA-20 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 7c7e86fc-de80-3b6f-8220-cf5ce7ebd04e | -4.34943 | -45.75678 | 2024-12-02 04:48:00 | NOAA-20 | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| df7b6330-96bf-3eea-8afb-a7e78369f195 | -2.44338 | -53.61578 | 2024-12-02 04:48:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 90f714e3-a049-3dc3-87f6-659b4083c4a9 | -2.30378 | -53.9032 | 2024-12-02 04:48:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 4320fe27-bb2a-3ae6-9e82-da311b509904 | -2.94222 | -51.50576 | 2024-12-02 04:48:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 1094f068-949d-331f-9420-eba0ee15aaef | -2.25472 | -51.2542 | 2024-12-02 04:48:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 08f970e4-5284-3d54-9d2f-bb7dccf8d6a6 | -1.27389 | -54.55546 | 2024-12-02 04:48:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 95f87b37-3699-3d4a-8366-403d6abc4a83 | -1.1498 | -53.66477 | 2024-12-02 04:48:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| d2178a9f-64a0-32d3-96c5-da85bcdc9b81 | -1.26733 | -54.55016 | 2024-12-02 04:48:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 9dcb282a-e4d9-3a03-959c-360ce70737c7 | -3.75577 | -52.27149 | 2024-12-02 04:48:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 3e3f8d7e-ac38-3c74-8e73-e7035f724664 | -2.47187 | -46.56377 | 2024-12-02 04:48:00 | NOAA-20 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 4ce9520c-0800-3bc5-8fef-24678fb4cabc | -1.35033 | -55.17453 | 2024-12-02 04:48:00 | NOAA-20 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 08208c1f-0210-3307-9eb7-93fdb3f8f35c | -3.27073 | -46.45263 | 2024-12-02 04:48:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 30.8 |
| 98ab1b28-8b89-3508-a0c0-2ba20508b120 | -3.55246 | -51.53442 | 2024-12-02 04:48:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 19598a33-a679-3d72-bb58-82de88b571b5 | -2.71968 | -47.55164 | 2024-12-02 04:48:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| ca6e79ac-97b4-3c6c-9f19-bc8ee51db7fb | -4.40075 | -50.69184 | 2024-12-02 04:48:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 02ff8848-7360-356d-b2c3-8740d18899ce | -1.09448 | -53.60973 | 2024-12-02 04:48:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 6a28c7ff-a048-3f18-836b-5f9ef0529849 | -2.96865 | -53.29181 | 2024-12-02 04:48:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| c94ddd45-c49f-357e-ae3c-a112e89f8634 | -3.48985 | -53.82567 | 2024-12-02 04:48:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 4f6d1e24-7eea-3fed-872a-041d88e47373 | -2.55097 | -53.40202 | 2024-12-02 04:48:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 9e4896f5-96ce-3a7b-96c5-7f9eb9f599f9 | -3.26362 | -53.63897 | 2024-12-02 04:48:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d08b345f-8dbe-3595-9fad-4e2e2eb8b9a7 | -2.98285 | -51.46273 | 2024-12-02 04:48:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 4d4200f9-93d9-37c5-af64-9e3300ee1499 | -3.21446 | -53.61672 | 2024-12-02 04:48:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| a1ec991e-3b6a-3efb-a586-8337cb6d251a | -2.81529 | -54.14931 | 2024-12-02 04:48:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| fe5c3509-8f92-3291-93d6-8ea1765bf00f | -2.01272 | -51.19499 | 2024-12-02 04:48:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 8db07dd6-2b82-3305-a206-65b313f35987 | -3.10942 | -54.01315 | 2024-12-02 04:48:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 2673e29d-6f8c-3905-b2f3-e1b3a8b00764 | -5.12831 | -43.20459 | 2024-12-02 04:48:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| a99f8965-fe4d-347f-b870-8d289284a6df | -3.43052 | -53.88909 | 2024-12-02 04:48:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 2b25a9d8-0b7b-3c4d-85b6-894541505183 | -1.40243 | -53.65689 | 2024-12-02 04:48:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 12.7 |
| a32b9376-4288-391d-9266-c8e0552ef63f | -3.09928 | -53.74604 | 2024-12-02 04:48:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 8d42fe35-0529-3e82-9c6c-29d8b65a108c | -2.71061 | -52.00493 | 2024-12-02 04:48:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 1010a4b2-1ce7-30a9-a5fe-5a53a5eae6ba | -4.20369 | -50.67243 | 2024-12-02 04:48:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 88890f7c-9cb2-3622-86a5-ec718e1ee245 | -1.53477 | -51.208 | 2024-12-02 04:48:00 | NOAA-20 | MELGAÇO | PARÁ | Brasil | 1504505 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 10f227d4-8392-3e1b-a8ff-d8eee46ec826 | -3.18033 | -54.33941 | 2024-12-02 04:48:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 3e2f56dc-1492-3fbc-b388-aca4428efda1 | -3.32248 | -50.0323 | 2024-12-02 04:48:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 156193bc-0a62-3a89-9d7c-525784a6e569 | -4.52801 | -45.73421 | 2024-12-02 04:48:00 | NOAA-20 | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 3f29de50-6d15-3578-8f67-2e18fe60f6bd | -0.31116 | -51.77356 | 2024-12-02 04:48:00 | NOAA-20 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 1.8 |
| f746e870-2e29-3296-9e25-cef2e53d432e | -2.54184 | -53.41556 | 2024-12-02 04:48:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 615554af-30ab-3599-b62d-8799d836d008 | -2.8554 | -54.06445 | 2024-12-02 04:48:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| b21c0254-da8e-3e62-a24a-18f238e2f5bd | -2.48235 | -46.57612 | 2024-12-02 04:48:00 | NOAA-20 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 359f2896-61d8-3762-aa08-1bac1320cc1d | -3.24716 | -53.63266 | 2024-12-02 04:48:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 101f5812-2056-33a2-907d-7ccb107e1086 | -4.04062 | -50.73553 | 2024-12-02 04:48:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| c224c565-01b8-33d8-8cc1-b8347dd7bd6f | -3.82674 | -46.60275 | 2024-12-02 04:48:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| aa56c562-8241-33b2-abe0-29c29a939cbf | -3.15638 | -51.11523 | 2024-12-02 04:48:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 2bade8eb-b4fe-3b21-b31b-08c7c49599af | -2.44784 | -50.51935 | 2024-12-02 04:48:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 072e95d8-0d4a-3ae1-80eb-69d9804c2985 | -2.8886 | -53.96809 | 2024-12-02 04:48:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 9bec530e-f689-395b-afdf-decef3de8aa8 | -2.33273 | -50.67039 | 2024-12-02 04:48:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 5f765294-28b3-3c57-9d53-664926748fde | -3.0727 | -53.80397 | 2024-12-02 04:48:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ea4b6dfb-51e2-3540-a2b4-c643eeb5fe80 | -2.09488 | -50.58319 | 2024-12-02 04:48:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| fcc7891d-ebae-3551-88f5-d73acaad38aa | -1.13818 | -53.7853 | 2024-12-02 04:48:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 6188e6b4-0f11-35ac-9660-c96134f265ee | -3.85666 | -50.89518 | 2024-12-02 04:48:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 07dc4070-b7aa-32cf-a995-919a8eb876df | -5.58123 | -45.2102 | 2024-12-02 04:48:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| f203882c-a473-3c0f-bad7-74a8e6f94fcb | -2.44231 | -54.01818 | 2024-12-02 04:48:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 51953a04-6a8c-33fa-9d51-995f7af16765 | -2.68024 | -46.61625 | 2024-12-02 04:48:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 085bd5dd-80a2-3a51-80f5-086dedb2d0ba | -3.95018 | -47.05543 | 2024-12-02 04:48:00 | NOAA-20 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a36faf4b-02a9-3834-9317-64db56224cbf | -4.15 | -48.24239 | 2024-12-02 04:48:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| f33d8179-4db4-389c-833b-d1dad95b4431 | -3.20971 | -54.17702 | 2024-12-02 04:48:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| f4aa579b-291e-3afb-a1f6-3d7ce61b9223 | -3.74512 | -51.30293 | 2024-12-02 04:48:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 4c3b1e9d-9dbb-3c6b-b680-8d6a3c521bd9 | -3.0925 | -53.72288 | 2024-12-02 04:48:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 49cdb578-9f64-306f-8012-654a6f93e229 | -2.98274 | -53.88165 | 2024-12-02 04:48:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| db814294-9660-381b-ba77-9374031a7092 | -3.06809 | -53.81091 | 2024-12-02 04:48:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| fb05cfa0-8efe-318d-a65d-1ce347f208c4 | -2.88405 | -54.10827 | 2024-12-02 04:48:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 7914fe56-14e3-319c-8b58-d82e7f016777 | -3.4775 | -50.25341 | 2024-12-02 04:48:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 8734a5ce-9edf-3d59-b28e-bc381ed6ed99 | -1.49324 | -52.63817 | 2024-12-02 04:48:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 8f399ff4-27b4-3b91-9175-7562f7aa411a | -3.9618 | -54.66296 | 2024-12-02 04:48:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 567a6416-dfae-37c2-bdcc-fd0f8cc027c8 | -3.2534 | -53.63735 | 2024-12-02 04:48:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 4aa6cc8a-ea18-3262-af11-f4d4037fc0b7 | -1.03025 | -53.55373 | 2024-12-02 04:48:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 36fe33a2-b976-3b1a-a0e2-0de3901150b0 | -1.17713 | -53.42189 | 2024-12-02 04:48:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 6f319163-53de-3596-ac6c-f1d3d03e49f2 | -3.1284 | -54.52906 | 2024-12-02 04:48:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 0fa6b042-e784-3d0b-bafb-0d1260635f45 | -2.80908 | -48.61391 | 2024-12-02 04:48:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 73844c0a-733d-3018-b01f-e600768dc1a6 | -3.26435 | -45.37624 | 2024-12-02 04:48:00 | NOAA-20 | PENALVA | MARANHÃO | Brasil | 2108306 | 21 | 33 | nan | nan | nan | Amazônia | 2.5 |
| a2b0c78d-8c35-3e78-8004-dedf8e07aeb0 | -1.72545 | -52.47907 | 2024-12-02 04:48:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 93accefb-4df0-3466-a6f3-1c0e58407c98 | -1.00864 | -51.72369 | 2024-12-02 04:48:00 | NOAA-20 | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 1.7 |
| ba866229-9eb7-3e5e-8927-f301d3a08a80 | -1.67192 | -52.79646 | 2024-12-02 04:48:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 3493ea64-9a98-3cfd-bbbc-63817b6876e9 | -3.3359 | -51.52905 | 2024-12-02 04:48:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 5d51d104-f8a2-3946-a208-260ae688a13b | -3.26586 | -53.64687 | 2024-12-02 04:48:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 99fe37d9-3c20-3ece-8707-01aadbdfa0ec | -2.30792 | -57.08794 | 2024-12-02 04:48:00 | NOAA-20 | NHAMUNDÁ | AMAZONAS | Brasil | 1303007 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 96bb572a-74cd-342a-b60f-5c19e6349716 | -1.12221 | -53.6141 | 2024-12-02 04:48:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 4ce96062-9a55-33f2-9527-62235e6cc00c | -1.72881 | -52.50116 | 2024-12-02 04:48:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 31c0ee11-55c1-323b-8816-7639ca7e6bce | 1.10876 | -56.01484 | 2024-12-02 04:48:00 | NOAA-20 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 9.3 |
| 33f8d888-2e80-38c4-87aa-487e593a58f5 | -4.07374 | -47.08837 | 2024-12-02 04:48:00 | NOAA-20 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 8abfb790-177a-3c1c-96f3-b2d5273c434b | -3.94678 | -48.17906 | 2024-12-02 04:48:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 062dfef3-1fc9-377a-a79f-b408e0eaf27f | -2.59215 | -46.27096 | 2024-12-02 04:48:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 844835bb-993a-31ee-b6fd-e37e4e30d419 | -2.26921 | -53.60796 | 2024-12-02 04:48:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| c7c518d4-3bcf-31b1-b864-47c87bb1e991 | -1.82216 | -53.72872 | 2024-12-02 04:48:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 05d2cec2-3e4f-3059-840a-137613614f1c | -0.8716 | -52.35691 | 2024-12-02 04:48:00 | NOAA-20 | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 4dcef514-16fc-35fa-adf7-ec4928441f0b | -3.47734 | -53.81603 | 2024-12-02 04:48:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 6195f3ad-bc2c-365a-9f87-7853932f98c4 | -1.94856 | -51.2128 | 2024-12-02 04:48:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| e95e0a0e-27a6-38cd-9af3-82f59af8d5fc | -3.29408 | -53.84495 | 2024-12-02 04:48:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 9.3 |
| 983eb41b-bd74-359d-b976-0e9a6c428a6a | -3.84973 | -46.5344 | 2024-12-02 04:48:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 3.1 |
| a67af3a7-9865-3681-bb9c-f269b596292f | -1.23633 | -51.61522 | 2024-12-02 04:48:00 | NOAA-20 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 9a12ed3e-de79-3daa-b2d6-ada5785ff532 | -2.26085 | -53.74859 | 2024-12-02 04:48:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 5ca99c72-95df-3d0b-b917-93e21b88d34e | -2.15324 | -50.60296 | 2024-12-02 04:48:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 2ff6d78e-3a6e-3cda-82e6-c00da5ed4f6b | -3.77273 | -50.04342 | 2024-12-02 04:48:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 03ba3c2a-9bd7-3e0a-a08d-974b2786b4f1 | -1.96008 | -46.45402 | 2024-12-02 04:48:00 | NOAA-20 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| dfbe1d13-aff6-3da3-8a5f-125bfbac393b | -1.45051 | -55.19495 | 2024-12-02 04:48:00 | NOAA-20 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| bdf3b01d-4a86-3c25-b8b9-51d92cadd442 | -3.75908 | -52.27201 | 2024-12-02 04:48:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| cb5c5b7f-65ec-3a83-84dd-16a1760f28ed | -2.32662 | -50.66586 | 2024-12-02 04:48:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 8144015c-c9e4-3278-8030-c0feb87842e3 | -3.13671 | -45.98878 | 2024-12-02 04:48:00 | NOAA-20 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |
| f0a2dcfa-805c-3f69-b563-95ac9186727d | -2.83022 | -54.08796 | 2024-12-02 04:48:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |


[Clique aqui para ver as próximas entradas](README52.md)
