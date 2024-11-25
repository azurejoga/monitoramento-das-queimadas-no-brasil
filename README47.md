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

## Dados Diários - Página 47

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 3c883582-3a49-3b09-9b18-7e610d2ddb51 | -2.30389 | -51.26634 | 2024-11-25 04:55:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 05aaf212-0ed2-3278-8e34-7957314b449b | -4.21168 | -46.37436 | 2024-11-25 04:55:00 | NPP-375D | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 84819175-a7cb-30fc-8959-ba7dc0d87215 | -1.11169 | -53.59985 | 2024-11-25 04:55:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| b4ca0d60-0a03-3f0e-a571-317de6910a05 | -3.24352 | -53.27578 | 2024-11-25 04:55:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 32b12c92-fec3-3c14-bf0b-b33e0cf97b35 | -1.64456 | -52.1069 | 2024-11-25 04:55:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 306c4cc0-e10b-3ffd-b318-e84d0cdb12d8 | -1.41666 | -52.41042 | 2024-11-25 04:55:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 860e11f3-f1bb-35c2-8ce3-98c3e3b362b7 | -2.96128 | -53.92905 | 2024-11-25 04:55:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 77f7ffda-257d-3281-96b0-c6ba4cc9ae12 | -3.06283 | -53.9948 | 2024-11-25 04:55:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| eb700269-616f-3a15-841f-f783ff4054b5 | -2.81998 | -54.71251 | 2024-11-25 04:55:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 260abde7-dd3e-35bd-bd28-3d845ab9c722 | -0.95213 | -51.64669 | 2024-11-25 04:55:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| f04f3289-c224-31d7-bb92-0e3a6884788a | -3.58607 | -53.72176 | 2024-11-25 04:55:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 8088f7b4-0446-36e0-a012-c07ff9ee7d33 | -2.88314 | -51.57992 | 2024-11-25 04:55:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 3d03391f-8d3f-323c-905d-33cb443bd76a | -1.48258 | -51.96688 | 2024-11-25 04:55:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| d327c188-2e57-3058-90ab-46ce532ebe1d | -2.73468 | -54.39568 | 2024-11-25 04:55:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 5cbaa563-c64d-376a-be4c-9b69d8eeae7e | -3.04177 | -54.02001 | 2024-11-25 04:55:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 47a7429d-a9b8-3188-b90d-abbe5c819934 | -0.09698 | -51.74913 | 2024-11-25 04:55:00 | NPP-375D | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 1.8 |
| fec5e90a-f3b3-3e4c-897c-db372a4227cd | -2.6787 | -53.06044 | 2024-11-25 04:55:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 67a756ce-c930-3e44-a78d-b429650992ed | -2.86429 | -53.9669 | 2024-11-25 04:55:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 83a65b88-990f-33cd-876f-f2b0974ddc1f | -3.78188 | -46.94528 | 2024-11-25 04:55:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| bc9da00a-be99-3556-b798-9e66f105be79 | -2.80383 | -54.02523 | 2024-11-25 04:55:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| cee16e22-2c87-3edd-bff9-61d58393cba8 | -3.50564 | -53.80487 | 2024-11-25 04:55:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| bf9600e8-f80b-3b3c-943e-9115ed75086c | -1.90101 | -52.94921 | 2024-11-25 04:55:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 0a859157-d4be-39a6-9ff2-8f881f5c3348 | -1.25548 | -51.78372 | 2024-11-25 04:55:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e61129fc-e02e-3442-a81f-d5d4bee73268 | -0.92699 | -51.71895 | 2024-11-25 04:55:00 | NPP-375D | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 1af8e3fd-28fb-3aee-8b16-9f2ab592b2ae | -3.49948 | -50.46244 | 2024-11-25 04:55:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 0a215bd8-6c60-3563-8493-a06c5545935d | -2.68693 | -46.27069 | 2024-11-25 04:55:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 2.5 |
| b11da851-4af5-31e9-97e4-df1d0157f1c6 | -0.87832 | -51.72226 | 2024-11-25 04:55:00 | NPP-375D | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 4a5ac30c-eefb-374f-9961-5e0c91734c5d | -2.58637 | -54.05237 | 2024-11-25 04:55:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 7145f4e4-8d05-3f06-8052-a525c8a4bc8b | -3.49589 | -50.46192 | 2024-11-25 04:55:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 559972aa-df5c-3638-bff1-2179205ee2bf | -0.82225 | -51.80712 | 2024-11-25 04:55:00 | NPP-375D | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 7770fd7e-b81d-36ef-afb4-de303764d937 | -2.82504 | -54.10722 | 2024-11-25 04:55:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| a5f29de7-95a0-31a2-b9c5-67cf71ab65cf | -2.81949 | -54.12068 | 2024-11-25 04:55:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 20e98a61-689e-36e1-86fd-8b7c85fe8e57 | -1.3326 | -51.40418 | 2024-11-25 04:55:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 9f9e079e-6ab3-3919-b632-73c83177bd9f | -1.6226 | -52.43504 | 2024-11-25 04:55:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 5a69c854-3b77-34b3-b775-6bd01a390b4b | -1.52126 | -52.04841 | 2024-11-25 04:55:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 293ad58e-e24c-3b18-b4c7-03f12f8cdc12 | -2.61354 | -53.96717 | 2024-11-25 04:55:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 9c2e4a60-ba8f-3ade-8b97-cd79b740b5be | -1.95954 | -53.32867 | 2024-11-25 04:55:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 1dbe9dab-c4df-38b0-801b-1a0ae085f0a4 | -2.85484 | -53.96186 | 2024-11-25 04:55:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| e0de948d-0a85-3300-8418-0bab126a5d64 | -4.29766 | -46.90083 | 2024-11-25 04:55:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 10.6 |
| 9098599e-27fe-3416-af41-a90a8750207e | -2.81671 | -54.11666 | 2024-11-25 04:55:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| a91ac87e-6e0b-3140-bf07-99c34f5ced14 | -2.70722 | -46.29333 | 2024-11-25 04:55:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 1248079c-04a3-3931-b4c7-ab63fa131e30 | -4.01818 | -48.07886 | 2024-11-25 04:55:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a67741cc-842a-3e83-b9c2-8be9b022a266 | -2.07483 | -47.881 | 2024-11-25 04:55:00 | NPP-375D | SÃO DOMINGOS DO CAPIM | PARÁ | Brasil | 1507201 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 69d6a2a5-67cf-398e-8c6c-a19c4f00e04f | -4.03016 | -50.50323 | 2024-11-25 04:55:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 838ee2a6-d58d-3c19-9ff1-2d2dbce036a8 | -3.97338 | -49.94331 | 2024-11-25 04:55:00 | NPP-375D | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 9dfdbc9c-69e5-34da-aa7b-440ea601b601 | -1.61481 | -52.59336 | 2024-11-25 04:55:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| ef543d38-0771-366e-8d93-6f0f94f28594 | -2.57049 | -53.96404 | 2024-11-25 04:55:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 9d823590-c711-349c-9ab7-be8d97e618c4 | -3.72889 | -53.69817 | 2024-11-25 04:55:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f496b071-b350-3149-84f2-dac926f4afdd | -2.29064 | -51.32859 | 2024-11-25 04:55:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 44b81fc1-eb38-3dbe-a55d-ef54c9de1a6c | -2.81779 | -54.08818 | 2024-11-25 04:55:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 6dccb235-a1fb-335e-b995-623857869606 | -2.83549 | -54.01949 | 2024-11-25 04:55:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c2849f0c-5559-30c6-a09c-fdb7ad21cdbe | -2.90861 | -51.70695 | 2024-11-25 04:55:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 05d2d3fe-09cb-38ec-bdc2-50f7c1ec6595 | -2.53717 | -53.98032 | 2024-11-25 04:55:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| f21c97f2-57aa-386b-80c6-3a4eff0fb027 | -1.35222 | -54.62891 | 2024-11-25 04:55:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 7.5 |
| 2bade816-82d7-3c45-9dde-a2f1dc7b43b4 | -0.06354 | -51.34967 | 2024-11-25 04:55:00 | NPP-375D | SANTANA | AMAPÁ | Brasil | 1600600 | 16 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 5289b122-703f-3801-837f-80a412ff1807 | -4.41808 | -49.70681 | 2024-11-25 04:55:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| a3059483-738e-313e-82f3-771b57ea5c12 | -2.85429 | -53.96534 | 2024-11-25 04:55:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 2002d766-bfd2-36f8-a280-e90a696af374 | -2.99801 | -53.7395 | 2024-11-25 04:55:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 51841782-2a6e-3ddc-b4d2-18537557518c | -0.96169 | -51.71709 | 2024-11-25 04:55:00 | NPP-375D | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 3f05b73c-8589-312a-a52b-07ee4a32f512 | -3.75847 | -49.93729 | 2024-11-25 04:55:00 | NPP-375D | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| eeed72cd-f214-3162-932f-9f93d591b5a1 | -2.53497 | -53.99426 | 2024-11-25 04:55:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 190b0dcc-b601-33ff-baf6-0daf68b4a7a4 | -2.79107 | -54.06255 | 2024-11-25 04:55:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| a56e7cab-2a03-346e-a1c4-89e2e3a0b471 | -2.0172 | -51.18228 | 2024-11-25 04:55:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| b57a1605-0639-3183-87eb-0a832c449679 | -0.80407 | -51.59439 | 2024-11-25 04:55:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| d39802c7-f8df-39fc-aff3-fb138013057e | -3.38658 | -50.72987 | 2024-11-25 04:55:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 922065ca-9ebf-3ab6-8f7a-3e0f598e670f | -3.29117 | -53.85603 | 2024-11-25 04:55:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| af35727f-f346-3cb5-a866-d4bff28db551 | -3.64136 | -52.24792 | 2024-11-25 04:55:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 1d1bc958-9ded-3e36-bf1d-f08c30b7dcda | -0.9555 | -51.64721 | 2024-11-25 04:55:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 03e4b91d-7dfd-3b22-85a4-b239796c95f2 | -0.81475 | -51.61423 | 2024-11-25 04:55:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 3c6eb0ba-2fd6-38c8-aaa0-22e108e536c6 | -3.97404 | -47.72036 | 2024-11-25 04:55:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a69b488e-2e21-3d6e-9eec-7b0a50d7c933 | -1.76688 | -52.70602 | 2024-11-25 04:55:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 399deb3f-ff2b-3249-b0d3-ba9e4aad3321 | -1.0846 | -53.64191 | 2024-11-25 04:55:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| bbc6c613-83f7-34d7-b800-8043ed433b08 | -3.52165 | -53.78969 | 2024-11-25 04:55:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 538af150-a67e-3404-b2bb-407459a709b1 | -3.47729 | -51.46529 | 2024-11-25 04:55:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c743377f-f69e-3888-8989-b9217e75fe97 | -3.04734 | -54.02801 | 2024-11-25 04:55:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b88633bf-8b56-3ce3-83a0-6358c02a9584 | -1.09897 | -53.61569 | 2024-11-25 04:55:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| d456b3c5-661c-370c-8077-b4ebabe65923 | -0.57656 | -51.70816 | 2024-11-25 04:55:00 | NPP-375D | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 7139d9d1-7298-39d1-9859-d78fff92ad1a | -3.58908 | -44.92809 | 2024-11-25 04:55:00 | NPP-375D | VITÓRIA DO MEARIM | MARANHÃO | Brasil | 2112902 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c824abae-e35c-348f-9e51-60eca3c3b6a9 | -2.5975 | -46.55368 | 2024-11-25 04:55:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 2fdd0314-99d3-37ea-987a-200a29f85ecc | -2.91201 | -51.70747 | 2024-11-25 04:55:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 2f21da14-be22-3efa-9be9-0067217d53cd | 0.334 | -49.71965 | 2024-11-25 04:55:00 | NPP-375D | CHAVES | PARÁ | Brasil | 1502509 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| e5d62091-09f9-3309-9b7b-27e3f3877de3 | -2.26314 | -53.68093 | 2024-11-25 04:55:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 1dcb797d-37f6-35af-af21-cabd0dd6e592 | -2.97145 | -51.57435 | 2024-11-25 04:55:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 6615ed0a-5ccf-3ddb-82bf-b7e0ac1e515e | -2.84216 | -54.02053 | 2024-11-25 04:55:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 98167be5-bdec-3330-ac96-4f45fa0d94ca | -1.24821 | -51.78621 | 2024-11-25 04:55:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 807a50ba-35dc-3904-a820-be7c3fb409f1 | -3.03646 | -53.23658 | 2024-11-25 04:55:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 2f5a2640-c8a3-3310-826a-97ff45d0bdae | -0.0052 | -51.12057 | 2024-11-25 04:55:00 | NPP-375D | SANTANA | AMAPÁ | Brasil | 1600600 | 16 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a86bc98a-7599-3d63-8337-72e894669ac6 | -0.951 | -51.63197 | 2024-11-25 04:55:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 79314066-1f1a-35f7-b98e-5af19d88cdbe | -1.08793 | -53.64243 | 2024-11-25 04:55:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| fed64e0a-bce9-32da-8277-e362e7d01d0b | -2.77139 | -54.04165 | 2024-11-25 04:55:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 61124644-6233-331d-938b-fec1ba4d9e6f | -0.81138 | -51.61371 | 2024-11-25 04:55:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| e505857d-dea2-3a6f-b367-42e64ddb6e6d | -2.81872 | -51.79305 | 2024-11-25 04:55:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 6a5bdf8d-0b10-3a9d-91b0-354a2ca385f5 | -2.87203 | -54.12569 | 2024-11-25 04:55:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 7184b4f0-c3bf-37e5-ab2e-32f2fc7de553 | -1.47819 | -51.99501 | 2024-11-25 04:55:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 6f3ef2b7-06d1-338d-9643-11a049761ea8 | -2.18628 | -53.80052 | 2024-11-25 04:55:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| d5583e21-59ce-39a4-9e42-969b6d2c01fc | -3.7283 | -52.31998 | 2024-11-25 04:55:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 8589f968-1dd0-3bd5-93eb-df466c6c9d98 | -0.27927 | -51.61868 | 2024-11-25 04:55:00 | NPP-375D | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 0.9 |
| bc76abe6-b057-368a-92d8-5ce3def8ed04 | -0.98804 | -51.71377 | 2024-11-25 04:55:00 | NPP-375D | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 2.4 |
| c0801047-1983-3a69-860e-74965e13ec2d | -2.18515 | -53.78609 | 2024-11-25 04:55:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| eb61fb51-7b73-39a8-b628-f5ab7544adcf | -3.34407 | -51.21456 | 2024-11-25 04:55:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |


[Clique aqui para ver as próximas entradas](README48.md)
