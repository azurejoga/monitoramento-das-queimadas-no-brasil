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

## Dados Diários - Página 40

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 296cc822-e2bb-39ff-b3ad-49311757fe79 | -2.95953 | -54.17006 | 2024-11-07 05:10:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a4ecd36f-067f-3970-9b34-8f8ab293937e | -1.13665 | -53.72618 | 2024-11-07 05:10:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 1ee30b81-d7d8-301c-863b-eca1e003a90c | -3.59201 | -50.2664 | 2024-11-07 05:10:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 6d1b5751-e5de-3209-9d06-01da802787a5 | -3.00433 | -54.09604 | 2024-11-07 05:10:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| b5a611d7-82ed-38e9-a37a-5f54a321a763 | -3.44984 | -50.38025 | 2024-11-07 05:10:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 7.9 |
| f61d1ef7-cce0-3f0a-8b71-3074c360a4e2 | -2.99478 | -53.84821 | 2024-11-07 05:10:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 59aaa011-7c82-3bb5-a177-3e2846d5ce23 | -2.66728 | -49.87326 | 2024-11-07 05:10:00 | NOAA-21 | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c123278d-5c5b-3f03-a884-d39b075aa9eb | -2.66275 | -49.87255 | 2024-11-07 05:10:00 | NOAA-21 | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 4a1662e2-e0f9-3832-b86d-bf84601b9c45 | -3.18418 | -50.58677 | 2024-11-07 05:10:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 7db1fba4-94a4-3bcf-8928-5afd254816be | -3.01799 | -53.234 | 2024-11-07 05:10:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 3f6c84f6-02ec-36aa-a208-a3d5e885d083 | -3.53073 | -50.3503 | 2024-11-07 05:10:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 6f2631c3-001b-37e4-a00e-e97151f3f3e0 | -5.04185 | -46.84286 | 2024-11-07 05:10:00 | NOAA-21 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 052f4074-a297-3d27-ab9c-02d99f8c72b9 | -3.56671 | -52.69399 | 2024-11-07 05:10:00 | NOAA-21 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| c47c65bf-8fb8-35c4-90df-9701b6ac1bd6 | -2.16941 | -53.70196 | 2024-11-07 05:10:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 2fcdff49-8ab7-3c4e-b6fd-8213d73ecd6a | -1.15175 | -53.74432 | 2024-11-07 05:10:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| c3035736-9203-33dc-ae4a-4129fc014f91 | -1.51998 | -52.54544 | 2024-11-07 05:10:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 9.2 |
| 824684c4-fa6c-39c6-ad28-b86e09354959 | -4.39726 | -49.76807 | 2024-11-07 05:10:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| f73b3884-f2ac-3d69-b59c-6c44e02e7212 | -2.8457 | -49.81576 | 2024-11-07 05:10:00 | NOAA-21 | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | 23.7 |
| 60ee8ca1-1d88-39f8-8576-aaf227b48705 | -2.96303 | -54.17058 | 2024-11-07 05:10:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b5f9b3e9-9b0c-3570-a465-82d6650ba2e6 | -2.07826 | -52.03913 | 2024-11-07 05:10:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 60c67f89-7701-3240-b9d1-8b63175a2eea | -3.61155 | -51.33517 | 2024-11-07 05:10:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 7aba36ea-dc96-3fb5-96c2-06c709eb828e | -2.73869 | -51.89731 | 2024-11-07 05:10:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 79d12cee-0898-3069-aed3-78b0b28aeebc | -2.17712 | -53.69907 | 2024-11-07 05:10:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 5312e573-23ba-37b7-a621-139ea8605a52 | -4.67525 | -46.33775 | 2024-11-07 05:10:00 | NOAA-21 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d55d1f24-0827-3076-8e38-85d4aa359668 | -2.94529 | -56.97406 | 2024-11-07 05:10:00 | NOAA-21 | PARINTINS | AMAZONAS | Brasil | 1303403 | 13 | 33 | nan | nan | nan | Amazônia | 0.5 |
| ea822aef-b88f-3405-ba66-d2f3b20e04a4 | -3.18354 | -50.59093 | 2024-11-07 05:10:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| b0a331bd-c781-39bb-910b-cf67c9e08fce | -1.34953 | -51.41472 | 2024-11-07 05:10:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 12ec90f5-769e-32fc-a5c4-6a1d7b097715 | -2.76174 | -53.21973 | 2024-11-07 05:10:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 3501de2b-a3f8-3fed-b9dd-2a97e68c786c | -0.1641 | -51.52638 | 2024-11-07 05:10:00 | NOAA-21 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d76bd197-7586-33d8-b8d4-5ab3389f4520 | -1.288 | -54.55952 | 2024-11-07 05:10:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 79dec23e-bbc1-32b0-b30a-35ddb0ff6886 | -2.93931 | -54.11533 | 2024-11-07 05:10:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| bb10dcb2-120e-3601-bd90-ac6a1f9dfc2d | -3.4481 | -56.93721 | 2024-11-07 05:10:00 | NOAA-21 | BARREIRINHA | AMAZONAS | Brasil | 1300508 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 0da3161b-6d27-33be-af54-44dd9ab8201a | -2.87859 | -51.46884 | 2024-11-07 05:10:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| e677039d-206e-3011-a222-b73d5e4aa63e | -2.92989 | -52.54924 | 2024-11-07 05:10:00 | NOAA-21 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| e198e37a-6a18-35fb-87bd-9681fd318394 | -1.94933 | -53.0693 | 2024-11-07 05:10:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| c40a7750-3e00-35ee-82ed-a0a4df26e631 | -3.45556 | -50.37247 | 2024-11-07 05:10:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 7.2 |
| c38d5fc6-e913-3662-b59d-f2768a08a158 | -3.2518 | -50.05017 | 2024-11-07 05:10:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| c2a45457-f830-3828-adbb-59549827bda1 | -2.43216 | -53.66525 | 2024-11-07 05:10:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 90e03626-c87a-31d3-839b-ac4b6022c09f | -3.00843 | -54.09267 | 2024-11-07 05:10:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c08144fb-1550-3cb5-9def-b4ee81a7f614 | -1.33718 | -55.44016 | 2024-11-07 05:10:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| ad5a6a5b-73f1-3de0-9fec-acd858f2ace0 | -1.14084 | -54.22106 | 2024-11-07 05:10:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 8c26173b-aa01-3d60-a197-dd74d4458669 | -1.6742 | -53.81147 | 2024-11-07 05:10:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| de73651c-ae6b-3deb-b162-d083ba8de9f0 | -3.23215 | -50.44965 | 2024-11-07 05:10:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 1d45f243-0dfb-3ff8-986d-0d9b231849f9 | -3.11339 | -51.1076 | 2024-11-07 05:10:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 4e4a0f7d-74bc-31fc-9856-9c9e5e74a14b | -1.18714 | -53.89582 | 2024-11-07 05:10:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 5a1ba311-6acb-350e-a73c-b2a0c5a18382 | -3.12651 | -51.11219 | 2024-11-07 05:10:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| f3b4035e-d8e2-3393-ae21-70beeb5256eb | -1.33245 | -54.63811 | 2024-11-07 05:10:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 3dd73c0a-98d9-321d-a053-ae2c9445026c | -2.82331 | -52.91737 | 2024-11-07 05:10:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 84712705-3422-346a-bcd7-d34fe91ec26e | -2.91446 | -54.25394 | 2024-11-07 05:10:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 607db482-cc0a-3e96-a569-2a9ded6bfef7 | 1.34897 | -50.86442 | 2024-11-07 05:10:00 | NOAA-21 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 0cf6f4e5-9655-359b-8ae4-875b7ea5bb27 | -3.74168 | -50.44524 | 2024-11-07 05:10:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| bae9342a-0c73-3d5f-8c73-01d2a6bead28 | -2.17405 | -46.45135 | 2024-11-07 05:10:00 | NOAA-21 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 6226cad7-fb55-31a1-982a-81369d6f85a6 | -2.8152 | -52.92057 | 2024-11-07 05:10:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 99f38df7-d623-328f-9f45-52fd4fcac6d7 | -3.07094 | -50.99006 | 2024-11-07 05:10:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 6647edc9-6a00-3d39-9001-a1f6e8f294f9 | -3.66575 | -50.23223 | 2024-11-07 05:10:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 6bbcbc1a-dd38-3394-88c8-ed9eb0a1b565 | -3.1811 | -50.57777 | 2024-11-07 05:10:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 31724dd4-7b86-3f37-93e2-4994c47c920d | -2.54565 | -54.01067 | 2024-11-07 05:10:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| acad55d3-cf83-33b2-8d1a-c00ce215ca89 | -3.2941 | -53.11537 | 2024-11-07 05:10:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 3e4302b5-1cc3-3781-805a-73cb0671e8ea | -2.81667 | -54.08958 | 2024-11-07 05:10:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 1ae537c9-12e0-379f-b8db-9a419d6784ce | -2.61445 | -51.73215 | 2024-11-07 05:10:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 5d096c55-4d41-3460-b556-4cb57c1136f5 | -2.93591 | -51.05422 | 2024-11-07 05:10:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 82ff941b-7fd0-3377-b3cb-55dfcf0bad45 | -2.40494 | -53.63281 | 2024-11-07 05:10:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 9e3cd48f-e8fe-382c-b573-e4d854c0fb19 | -3.18481 | -50.58258 | 2024-11-07 05:10:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 4cdcd941-158f-3108-bf9a-0cab87e1a18e | -0.04294 | -50.79445 | 2024-11-07 05:10:00 | NOAA-21 | AFUÁ | PARÁ | Brasil | 1500305 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ebf7899e-cada-392b-a207-e1d0d35d4550 | -1.41437 | -54.49701 | 2024-11-07 05:10:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 385c65bc-5a35-338f-9687-098b711cad68 | -3.1785 | -53.85386 | 2024-11-07 05:10:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 863bc2ab-ab7a-3d50-9ed7-5c22178e656d | -1.14898 | -53.71597 | 2024-11-07 05:10:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 7.7 |
| a56a6934-572d-3bbd-887b-f3ff1cbef919 | -5.62112 | -43.95079 | 2024-11-07 05:10:00 | NOAA-21 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 9.9 |
| c7927893-e510-31cc-ad54-75ca6624751a | -3.47157 | -56.89513 | 2024-11-07 05:10:00 | NOAA-21 | BARREIRINHA | AMAZONAS | Brasil | 1300508 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 77ce3169-41a8-3958-8e8f-b36b52889d0e | -1.29139 | -54.56005 | 2024-11-07 05:10:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 71f20815-93bf-3779-9709-05a51f5a4098 | -2.76109 | -53.22395 | 2024-11-07 05:10:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 606040f5-ab3b-368c-b751-d8b687243037 | -3.11779 | -54.25256 | 2024-11-07 05:10:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 469976dd-0099-34d2-9e8d-0a44ec187ad6 | -2.75937 | -53.21076 | 2024-11-07 05:10:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d227850f-55a4-34cb-b8b9-e6485b6a8792 | -3.27437 | -50.3462 | 2024-11-07 05:10:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 54c1545a-9d0e-3f68-8c6f-f01e614b3ee4 | -3.62338 | -51.50005 | 2024-11-07 05:10:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 109d21df-8023-370e-8f5a-8020eec00fd2 | -3.78263 | -50.14199 | 2024-11-07 05:10:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| cb38cdc1-8780-3272-a0ba-2d9dfcee8cb1 | -2.83513 | -52.91474 | 2024-11-07 05:10:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 40f09c1c-2632-3105-8a1f-62d122411d1b | -3.1638 | -50.21042 | 2024-11-07 05:10:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 475312ff-a451-3cec-a339-cfd0ba7d6ebd | -0.84858 | -52.84621 | 2024-11-07 05:10:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| ba913387-f3fb-34a2-bf74-5bbc0175633e | -1.42745 | -54.50261 | 2024-11-07 05:10:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 20c45211-7a6b-3ae0-8590-c0711f8957cb | -2.72757 | -54.14792 | 2024-11-07 05:10:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 327bf75f-03e7-3dcd-b9b4-b037adaa97f8 | -2.67795 | -51.82352 | 2024-11-07 05:10:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 0cbba878-7902-3279-b68c-a8d9580afeae | -2.92084 | -51.04004 | 2024-11-07 05:10:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 225b5cf2-8405-39ef-85ab-d5e88b1f5a1e | -3.59272 | -50.23012 | 2024-11-07 05:10:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 85.7 |
| 81a92059-c177-37a2-a8bd-b1bdcda662b8 | -2.94198 | -56.97356 | 2024-11-07 05:10:00 | NOAA-21 | PARINTINS | AMAZONAS | Brasil | 1303403 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 548e39ce-8319-34f3-aed4-9e14de159f19 | -2.96363 | -54.16673 | 2024-11-07 05:10:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 3fac12bd-df5e-3b8f-82a6-60924de0dfc1 | -2.85567 | -49.49588 | 2024-11-07 05:10:00 | NOAA-21 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 7d68064c-1d71-30b5-aa33-c7823d904405 | -1.40072 | -54.10589 | 2024-11-07 05:10:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| a73a9071-7731-3287-b03f-0e07acc3761b | -2.62146 | -51.29692 | 2024-11-07 05:10:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 6cc7e2b1-cdc1-379a-8682-a1d338e516a1 | -3.02247 | -54.09484 | 2024-11-07 05:10:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| af7f4702-e222-3b3e-9f3a-eff99ce35a4e | -3.01789 | -53.43209 | 2024-11-07 05:10:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d4e2cec4-be61-3d51-ba93-e152ceea4034 | -2.8366 | -51.80506 | 2024-11-07 05:10:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ba493a89-00cd-3e84-8f2c-c2eb2d3d0d6b | -2.91378 | -51.05209 | 2024-11-07 05:10:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 972feca3-dd36-3c28-b0fc-23ff493fb0e5 | -3.59206 | -50.23462 | 2024-11-07 05:10:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 85.7 |
| 115041a4-9802-33c9-9e47-1ac2f2ef0f6c | -3.58693 | -50.23847 | 2024-11-07 05:10:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 17.9 |
| 80f66177-c8e2-3c90-bb81-8a81e5e41798 | -2.85326 | -48.66573 | 2024-11-07 05:10:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 3d6fd7e0-2bce-3033-97a1-b4ee6cfc60ae | -2.88571 | -48.72963 | 2024-11-07 05:10:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 2d65ae58-9b43-3881-9b26-474df5e8415e | -2.91916 | -51.04502 | 2024-11-07 05:10:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 1a71fdf6-6907-34f1-8dfb-15954e8a118c | -2.65914 | -49.87494 | 2024-11-07 05:10:00 | NOAA-21 | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| fd2c80d9-57b8-3889-9767-f779768d447b | -1.34543 | -54.62149 | 2024-11-07 05:10:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |


[Clique aqui para ver as próximas entradas](README41.md)
