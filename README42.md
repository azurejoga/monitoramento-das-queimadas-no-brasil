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

## Dados Diários - Página 42

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| c84dfc67-8773-3825-a4cd-19b8551ab40b | -4.93789 | -50.64914 | 2024-11-20 04:50:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 1d02915b-9426-3d7d-9d3b-4d68e0b9aa24 | -1.14776 | -51.94559 | 2024-11-20 04:50:00 | NPP-375D | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 0717cb41-afe0-3b1a-97af-6afd2bd68183 | -2.4194 | -49.10558 | 2024-11-20 04:50:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 9e0c2420-9cb8-3565-a348-fa3872db9ecc | -3.4666 | -48.25323 | 2024-11-20 04:50:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 451a7c4f-3799-368a-90df-1b25fffc89a6 | -2.91893 | -53.06976 | 2024-11-20 04:50:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 7f36a14f-ec9a-3139-a555-4d95f61aa74b | -6.63453 | -47.35168 | 2024-11-20 04:50:00 | NPP-375D | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 2f8e1278-fff8-39ff-bcde-b72661c89632 | -2.92906 | -53.07141 | 2024-11-20 04:50:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 09408700-2859-3671-aeff-c7d3b831e543 | -3.10139 | -53.74589 | 2024-11-20 04:50:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 9d53d07e-3334-3dbc-a02b-046637e49d31 | -2.82843 | -51.82591 | 2024-11-20 04:50:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 5587b570-0d4f-33c2-94f1-5b4da759ff2a | -2.5871 | -51.72482 | 2024-11-20 04:50:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 7904de40-6663-3b5c-a38f-cd69903e7992 | -2.92681 | -53.06371 | 2024-11-20 04:50:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 39b604a8-4663-3b89-ab58-7981a861f0fb | -1.64035 | -52.67717 | 2024-11-20 04:50:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 698f85f1-fb73-35ae-9790-543b1b62cdc1 | -2.06183 | -53.43081 | 2024-11-20 04:50:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 334f7180-104c-32ca-abb7-270ca0409ebc | -1.60554 | -54.64105 | 2024-11-20 04:50:00 | NPP-375D | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 6d4f2391-a8e2-3c42-9a68-3aa3ce179d5a | -1.51595 | -55.48146 | 2024-11-20 04:50:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| cd12fc35-d0d8-3a00-ae3f-a4e83a03a6cf | -4.37343 | -50.73188 | 2024-11-20 04:50:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 3dba5438-00d9-3a3b-a46f-f22410271fe3 | -1.85391 | -54.27689 | 2024-11-20 04:50:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 26faa015-a9dd-3d42-8302-4281d0d1ab58 | -3.77944 | -44.06523 | 2024-11-20 04:50:00 | NPP-375D | PIRAPEMAS | MARANHÃO | Brasil | 2108801 | 21 | 33 | nan | nan | nan | Cerrado | 6.0 |
| c52c6da2-bb4c-31fc-8494-68fb7bd0ded9 | -1.26043 | -51.7679 | 2024-11-20 04:50:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 4cd23bca-6a61-3a2a-bb76-7fdafdec5cba | -2.89755 | -53.05174 | 2024-11-20 04:50:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 75215586-b8d0-3892-ae15-45252c0bd089 | -2.60774 | -51.78807 | 2024-11-20 04:50:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 3dc795e5-5cbe-3928-aef2-9f8e8893b5f7 | -3.00503 | -46.96408 | 2024-11-20 04:50:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 24b1d3a4-95db-3886-9816-1284bba3d542 | -2.19701 | -49.86989 | 2024-11-20 04:50:00 | NPP-375D | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 624f3ef7-cb62-3946-86d0-65b9cadac926 | -0.97365 | -51.71929 | 2024-11-20 04:50:00 | NPP-375D | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 2.1 |
| bc81b28b-7f32-33ad-ad5e-838ac6738127 | -3.31188 | -54.07324 | 2024-11-20 04:50:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| cd3463c8-214e-35e9-b211-4691b955c22b | -9.17343 | -44.73278 | 2024-11-20 04:50:00 | NPP-375D | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| d5c9ea82-d6a3-3329-b4dd-b168c0da4778 | -2.64201 | -46.21202 | 2024-11-20 04:50:00 | NPP-375D | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 6872aac7-87ae-354a-b477-d9ac8deee891 | -2.82104 | -54.02272 | 2024-11-20 04:50:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 03b9d33c-25d3-35d2-a6bd-ac8cf91aace2 | -2.59862 | -54.01641 | 2024-11-20 04:50:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| a99319d7-932b-3731-893f-6f64aa0c9389 | -3.53679 | -54.08752 | 2024-11-20 04:50:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 08597313-0b27-3d70-aa3c-f82e3d70f1c3 | -1.19835 | -51.77594 | 2024-11-20 04:50:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| a9629879-3e9e-3068-97a7-6e6c9aa47707 | -6.9463 | -45.08072 | 2024-11-20 04:50:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| ada862cb-b677-3dcf-b975-9141923f461b | -3.05238 | -48.50105 | 2024-11-20 04:50:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| be8e63c4-46ea-3561-92f8-c3a874d231ab | -2.61666 | -45.89568 | 2024-11-20 04:50:00 | NPP-375D | SANTA LUZIA DO PARUÁ | MARANHÃO | Brasil | 2110039 | 21 | 33 | nan | nan | nan | Amazônia | 8.7 |
| b6898604-6c94-304d-8d61-748b71d3f5af | -2.58046 | -51.72379 | 2024-11-20 04:50:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 55f58b46-9415-3679-9a03-26cec4e78ecb | -3.45157 | -51.2192 | 2024-11-20 04:50:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 6c1453a7-d321-3e8b-a077-a473a4834280 | -1.48526 | -52.1049 | 2024-11-20 04:50:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b99484eb-4df6-3bc3-8001-19d5d4ac2172 | -1.20385 | -51.76262 | 2024-11-20 04:50:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 3bbff735-5c51-31d8-b336-31d4a16baf86 | -6.82313 | -43.28653 | 2024-11-20 04:50:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 488c9677-21bc-3929-8fae-abd70fa862c8 | -3.79874 | -52.2186 | 2024-11-20 04:50:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| bb742e81-2dfb-3bb7-b625-e53a1b319ab9 | -5.25196 | -43.83178 | 2024-11-20 04:50:00 | NPP-375D | SENADOR ALEXANDRE COSTA | MARANHÃO | Brasil | 2111748 | 21 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 3a052293-92b0-31c1-8066-3d30a6942354 | -3.79187 | -51.07981 | 2024-11-20 04:50:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| ecd51e63-b9a8-3be3-908b-0a27727aeb88 | -4.78933 | -50.48175 | 2024-11-20 04:50:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 782ea752-8307-3f62-8b2f-af51792bbdc3 | -1.33908 | -52.236 | 2024-11-20 04:50:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 62d92b48-dfee-3953-acda-3f87184766cd | -0.94597 | -51.72207 | 2024-11-20 04:50:00 | NPP-375D | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 258f44e5-6122-30c4-b25e-b2d873d2dbab | -2.62161 | -51.80789 | 2024-11-20 04:50:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 9523b0e6-82dc-31e8-b5fb-7a9a880b8acb | -1.56208 | -51.99971 | 2024-11-20 04:50:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 9a5c0081-36df-357c-bc7b-b98e063b4001 | -3.13144 | -48.58996 | 2024-11-20 04:50:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 5809af94-caa7-3531-bef0-0cde5d69d46d | -1.97992 | -51.11045 | 2024-11-20 04:50:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| c3d8179c-7180-32a6-9aa6-01d2bba0e47f | -2.26518 | -50.82157 | 2024-11-20 04:50:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 8c80ca31-a0e5-38a4-ac93-4982c26db80a | -5.6971 | -45.85092 | 2024-11-20 04:50:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| cd6dbd22-4e53-3d32-9d3f-9dceb663f999 | -2.2808 | -53.63688 | 2024-11-20 04:50:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 3248354e-3c7f-3ad2-a8a4-2f324b11db23 | -2.2802 | -53.64065 | 2024-11-20 04:50:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| e3892c9e-7583-3009-a226-5aa896f9bb11 | -3.76952 | -52.66254 | 2024-11-20 04:50:00 | NPP-375D | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 5e423183-abbe-3508-bd68-96a93887b8ab | -2.01817 | -52.41044 | 2024-11-20 04:50:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| edfd6fe7-f3f2-3a4c-9cf7-2a151a33aa30 | -1.92753 | -46.44732 | 2024-11-20 04:50:00 | NPP-375D | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| add7a239-02cb-3c4d-b835-b0edf366fdeb | -2.67431 | -46.16696 | 2024-11-20 04:50:00 | NPP-375D | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| b268e210-c54e-3e12-80d2-e454e394848c | -1.2444 | -51.78311 | 2024-11-20 04:50:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 6da8e942-0346-3807-beec-6ed2860ccde5 | -1.46349 | -48.19691 | 2024-11-20 04:50:00 | NPP-375D | SANTA IZABEL DO PARÁ | PARÁ | Brasil | 1506500 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 602fc214-194f-34cf-8965-f3a15f204f39 | -2.51905 | -44.99759 | 2024-11-20 04:50:00 | NPP-375D | PERI MIRIM | MARANHÃO | Brasil | 2108405 | 21 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 006d903c-9534-3075-b79a-235ac37cadc5 | -2.28288 | -48.49011 | 2024-11-20 04:50:00 | NPP-375D | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 3cc9c908-8c79-3e07-bc68-f07fd94b5c80 | -2.28503 | -50.5849 | 2024-11-20 04:50:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| e3ca8a3d-42bb-325f-942b-89e58b419406 | -5.6997 | -45.84886 | 2024-11-20 04:50:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| ff0e99c8-6d34-3815-b9bd-21d98f94ee20 | -3.72565 | -47.37402 | 2024-11-20 04:50:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| ab7c31f1-d908-3209-9852-7c484d108edf | -3.80203 | -51.14574 | 2024-11-20 04:50:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 17328a39-47a6-3a88-b465-2a1ec706a18e | -1.21612 | -51.79287 | 2024-11-20 04:50:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 850df538-cfe2-31a6-9a22-77180e5c467f | -3.81312 | -47.80231 | 2024-11-20 04:50:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 36cddea1-b722-3848-b993-cc2e08a0044d | -2.62077 | -48.3263 | 2024-11-20 04:50:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| dfe306cd-5864-3fbb-a61e-3d023e040bab | -2.92517 | -45.27703 | 2024-11-20 04:50:00 | NPP-375D | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 9b22866d-a50a-3b59-8235-93fb547db40d | -1.30455 | -52.25935 | 2024-11-20 04:50:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 2e2c083a-79c0-33c7-bfcc-612debda76a9 | -6.82807 | -43.29079 | 2024-11-20 04:50:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| bc5b1e20-5ef1-3d16-bf49-37cb837de2bd | -2.70344 | -47.9796 | 2024-11-20 04:50:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 42a8d280-1479-333f-9f67-4bd652e7342d | -1.2399 | -51.747 | 2024-11-20 04:50:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d79e5b93-47b1-35d3-b023-76362ae29737 | -1.68802 | -55.0301 | 2024-11-20 04:50:00 | NPP-375D | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| fb73877a-776e-305e-927e-359dd10bb5cb | -1.75394 | -52.37256 | 2024-11-20 04:50:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| a6642544-1805-34ae-a594-cb5c1f6e249d | -1.37772 | -52.07742 | 2024-11-20 04:50:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 1a1eaf64-71c1-3d6b-8e5a-6b231d3db8b2 | -2.70784 | -47.97577 | 2024-11-20 04:50:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 9371d789-4ffa-31e8-b2d1-30cf2dee6c58 | -1.13886 | -51.67818 | 2024-11-20 04:50:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 0d8da2fd-bfea-34e1-b990-99f5150ae43a | -1.4382 | -53.3777 | 2024-11-20 04:50:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 5b29b939-d610-3985-b2ce-274582c55cff | -1.14164 | -51.68214 | 2024-11-20 04:50:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 158e2a1e-6b81-30b0-9dd9-2cea93eababd | -4.19302 | -46.8118 | 2024-11-20 04:50:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 60610054-6f46-3aa0-9854-254b4c8c66e6 | -2.94152 | -48.32707 | 2024-11-20 04:50:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 26814ed9-7c68-3a82-b018-31275d5674e5 | -2.03482 | -48.09164 | 2024-11-20 04:50:00 | NPP-375D | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 04c26c74-fc18-3004-99ff-38e26f51d0ee | -2.0207 | -51.17342 | 2024-11-20 04:50:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 081b0c77-cae0-3dbf-8efc-e839c0847707 | -2.37001 | -49.83314 | 2024-11-20 04:50:00 | NPP-375D | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 4003047f-ff89-3135-bcf6-c56cbd593f56 | -1.38933 | -52.4309 | 2024-11-20 04:50:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 7c42d957-9df2-3615-9862-27be8615f35f | -1.05127 | -51.74257 | 2024-11-20 04:50:00 | NPP-375D | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 3.3 |
| c914ebdb-3bb7-3e23-b1a3-fd86594c3d33 | -2.72417 | -49.35086 | 2024-11-20 04:50:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| ee1194f5-777d-3d77-8f67-561c9d8a2368 | -1.41111 | -51.11363 | 2024-11-20 04:50:00 | NPP-375D | MELGAÇO | PARÁ | Brasil | 1504505 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 82596e25-4195-35ce-ab0d-f272d5fa330b | -3.05612 | -54.41018 | 2024-11-20 04:50:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e853f069-b31a-3f86-a7e4-c4598eb98ee8 | -2.6409 | -46.21947 | 2024-11-20 04:50:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 2.6 |
| a05ca258-1823-3d6b-b5b9-70b16c531fec | -3.45838 | -53.30486 | 2024-11-20 04:50:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 38362388-0c15-31df-8f42-27daebebc04b | -3.31989 | -54.09028 | 2024-11-20 04:50:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 5eb01e33-acc5-317b-9367-36546cb9b70b | -1.41376 | -51.07521 | 2024-11-20 04:50:00 | NPP-375D | MELGAÇO | PARÁ | Brasil | 1504505 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 47c05aad-70b0-39da-864e-4faa3f8c502c | -2.62671 | -54.27321 | 2024-11-20 04:50:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b6f8c67f-0da4-362d-b73e-6273c978d580 | -1.51056 | -52.06643 | 2024-11-20 04:50:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 82ae935a-33dc-342f-a21d-7da205fcad7b | -2.75305 | -45.70331 | 2024-11-20 04:50:00 | NPP-375D | NOVA OLINDA DO MARANHÃO | MARANHÃO | Brasil | 2107357 | 21 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 9f8a02f5-f88c-326b-8188-a8f372978398 | -3.84915 | -50.69197 | 2024-11-20 04:50:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 280dcc20-0da9-3b2c-9710-ff8c61a352e7 | -2.60741 | -48.21989 | 2024-11-20 04:50:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| be5bb712-0456-3d43-a202-2fe834222e02 | -3.80686 | -51.07144 | 2024-11-20 04:50:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |


[Clique aqui para ver as próximas entradas](README43.md)
