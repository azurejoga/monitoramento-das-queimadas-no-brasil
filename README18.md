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

## Dados Diários - Página 18

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 3feffb1c-cff5-3da6-9feb-bc1334b4516a | -6.71504 | -40.81001 | 2025-11-18 03:29:00 | NOAA-20 | PIO IX | PIAUÍ | Brasil | 2208205 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 01979e6c-a106-348d-b013-2510fb36feff | -6.7156 | -40.80684 | 2025-11-18 03:29:00 | NOAA-20 | PIO IX | PIAUÍ | Brasil | 2208205 | 22 | 33 | nan | nan | nan | Caatinga | 3.0 |
| 1ba07a3a-7146-359e-8d53-dbee446c7f75 | -7.42985 | -45.20679 | 2025-11-18 03:29:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 6de6a846-3b64-33f2-9e4e-e6a4aacfadae | -7.61549 | -42.58941 | 2025-11-18 03:29:00 | NOAA-20 | RIBEIRA DO PIAUÍ | PIAUÍ | Brasil | 2208874 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| ce82f922-49be-31a2-9fc0-fee65429d0f1 | -5.42908 | -43.04985 | 2025-11-18 03:29:00 | NOAA-20 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 11.9 |
| ab8248eb-73df-3304-a0c8-b736b40671d9 | -7.62196 | -42.58636 | 2025-11-18 03:29:00 | NOAA-20 | RIBEIRA DO PIAUÍ | PIAUÍ | Brasil | 2208874 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 4f657efc-d45e-3970-8a69-a6336feac059 | -6.7276 | -35.21971 | 2025-11-18 03:29:00 | NOAA-20 | CURRAL DE CIMA | PARAÍBA | Brasil | 2505279 | 25 | 33 | nan | nan | nan | Caatinga | 8.0 |
| b5f8071e-339f-3be1-8f57-35b2901590cd | -10.23602 | -36.29607 | 2025-11-18 03:29:00 | NOAA-20 | CORURIPE | ALAGOAS | Brasil | 2702306 | 27 | 33 | nan | nan | nan | Mata Atlântica | 25.5 |
| baddb105-9117-3eb7-98ec-b0749252f0fe | -8.29616 | -44.01437 | 2025-11-18 03:29:00 | NOAA-20 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 2947030d-dfb2-320e-9424-082a7eafbfa0 | -7.54303 | -41.19789 | 2025-11-18 03:29:00 | NOAA-20 | MASSAPÊ DO PIAUÍ | PIAUÍ | Brasil | 2206050 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 52cbd9e1-f933-394a-847b-92f873bf3312 | -5.4554 | -40.978 | 2025-11-18 03:29:00 | NOAA-20 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| c636b32e-2dba-32a5-a21f-73c14d348f66 | -6.72335 | -35.22318 | 2025-11-18 03:29:00 | NOAA-20 | CURRAL DE CIMA | PARAÍBA | Brasil | 2505279 | 25 | 33 | nan | nan | nan | Caatinga | 3.0 |
| 776e7664-915d-3f0f-82ce-efb1c0566f56 | -6.72225 | -35.2177 | 2025-11-18 03:29:00 | NOAA-20 | CURRAL DE CIMA | PARAÍBA | Brasil | 2505279 | 25 | 33 | nan | nan | nan | Caatinga | 4.8 |
| cb5f118f-b182-326d-bef3-33f4def80260 | -6.67063 | -43.76404 | 2025-11-18 03:29:00 | NOAA-20 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 8709bac9-76ba-39de-977e-ce14fe421a82 | -7.61951 | -42.59035 | 2025-11-18 03:29:00 | NOAA-20 | RIBEIRA DO PIAUÍ | PIAUÍ | Brasil | 2208874 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| bc17a04e-dc6e-3d90-b053-9dc5fbe83969 | -10.51657 | -43.96098 | 2025-11-18 03:29:00 | NOAA-20 | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 8.2 |
| f704dd1f-d91b-32d8-a622-3d6815b13b4f | -6.44025 | -43.81868 | 2025-11-18 03:29:00 | NOAA-20 | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 8.4 |
| 097ddb84-3d3b-318b-b4b7-b590d0fda4ab | -5.63249 | -43.93375 | 2025-11-18 03:29:00 | NOAA-20 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 4.8 |
| e2d6888c-f3a6-380c-a3e6-121c111f425f | -8.54261 | -46.05313 | 2025-11-18 03:29:00 | NOAA-20 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 73c0aec9-0b8c-351a-92f6-e3b87401f5fd | -6.72074 | -40.80782 | 2025-11-18 03:29:00 | NOAA-20 | PIO IX | PIAUÍ | Brasil | 2208205 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 477cdd1f-c3e1-3ab5-9d21-c2e4dfb1e9cd | -10.90715 | -40.53457 | 2025-11-18 03:29:00 | NOAA-20 | MIRANGABA | BAHIA | Brasil | 2921401 | 29 | 33 | nan | nan | nan | Caatinga | 1.5 |
| fed2afcf-928b-3f2a-b6af-23c7500caf99 | -7.33248 | -46.16924 | 2025-11-18 03:29:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 10.8 |
| f5c0aee9-6ea1-3b46-8251-5706354677dc | -4.63979 | -45.53121 | 2025-11-18 03:29:00 | NOAA-20 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 57cf9a18-9073-343a-92f1-a0b822b214e4 | -7.36416 | -35.1119 | 2025-11-18 03:29:00 | NOAA-20 | PEDRAS DE FOGO | PARAÍBA | Brasil | 2511202 | 25 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| ad7a5942-9f61-3eb1-b6bd-a41a7ca9a45a | -5.63172 | -43.93044 | 2025-11-18 03:29:00 | NOAA-20 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 72dec49e-b78c-33af-86c0-204b6b6d221a | -6.66761 | -42.04102 | 2025-11-18 03:29:00 | NOAA-20 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 14.5 |
| dfa23958-c67c-33d3-9bd1-a7b54ef2f9f7 | -5.46194 | -40.97198 | 2025-11-18 03:29:00 | NOAA-20 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 2.8 |
| 5a151136-5da2-305b-94ca-dee9c09e36f5 | -6.43297 | -45.73954 | 2025-11-18 03:29:00 | NOAA-20 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 6008f5b2-e17a-3ada-a316-ca5163846175 | -6.43929 | -43.82407 | 2025-11-18 03:29:00 | NOAA-20 | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 9.7 |
| 906d29c8-691a-3a68-b119-8b0fdd2c9ea0 | -8.58111 | -44.11049 | 2025-11-18 03:29:00 | NOAA-20 | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 3626c211-8c04-3dab-94e8-6c7e72d0809b | -7.92297 | -42.76917 | 2025-11-18 03:29:00 | NOAA-20 | PAJEÚ DO PIAUÍ | PIAUÍ | Brasil | 2207355 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 649d365d-13f1-3c4a-8521-74a658591bee | -9.96652 | -38.34334 | 2025-11-18 03:29:00 | NOAA-20 | JEREMOABO | BAHIA | Brasil | 2918100 | 29 | 33 | nan | nan | nan | Caatinga | 1.5 |
| a707c308-fe0b-31e8-b4ab-e9e9453f2de6 | -7.42614 | -45.20341 | 2025-11-18 03:29:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| a0f165aa-301b-384a-87d5-5fe3c9eb1978 | -7.37809 | -39.12742 | 2025-11-18 03:29:00 | NOAA-20 | MISSÃO VELHA | CEARÁ | Brasil | 2308401 | 23 | 33 | nan | nan | nan | Caatinga | 1.7 |
| ae5708b1-6cbc-3136-9cff-fd8042cc9dfa | -7.56533 | -46.2974 | 2025-11-18 03:29:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 1a97c3f2-6b7c-3a73-a90b-f633fe59eba6 | -7.24334 | -39.38831 | 2025-11-18 03:29:00 | NOAA-20 | CRATO | CEARÁ | Brasil | 2304202 | 23 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 460f0c10-8626-37bd-8103-ef996c9a9be8 | -6.71157 | -40.79952 | 2025-11-18 03:29:00 | NOAA-20 | PIO IX | PIAUÍ | Brasil | 2208205 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 9265224d-3376-3880-8ea7-c68fe736d496 | -6.1189 | -42.9669 | 2025-11-18 03:29:00 | NOAA-20 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 3.3 |
| 670544b3-b8a2-33ed-a4a4-44c28905be8c | -7.54362 | -41.19468 | 2025-11-18 03:29:00 | NOAA-20 | MASSAPÊ DO PIAUÍ | PIAUÍ | Brasil | 2206050 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 0292a593-26e3-348a-bd38-cf53ae3d8e9a | -8.63923 | -45.48783 | 2025-11-18 03:29:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 5b3c9851-65da-3973-a51f-ceb3d0295d44 | -6.03834 | -39.49547 | 2025-11-18 03:29:00 | NOAA-20 | ACOPIARA | CEARÁ | Brasil | 2300309 | 23 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 4467743e-98bb-3085-9074-edb8053137d6 | -7.45042 | -42.7677 | 2025-11-18 03:29:00 | NOAA-20 | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 26a196e4-ebab-3bc7-846b-2c166b15d85d | -7.41572 | -42.76124 | 2025-11-18 03:29:00 | NOAA-20 | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| d7ec6597-6f89-362e-9cec-a333423d3f4c | -7.9659 | -38.2826 | 2025-11-18 03:29:00 | NOAA-20 | SERRA TALHADA | PERNAMBUCO | Brasil | 2613909 | 26 | 33 | nan | nan | nan | Caatinga | 6.3 |
| 623f0199-9299-396b-81c9-ee463caa5ea4 | -6.74831 | -35.00038 | 2025-11-18 03:29:00 | NOAA-20 | MARCAÇÃO | PARAÍBA | Brasil | 2509057 | 25 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 197b1f34-c1ff-3b95-8e18-609aa504fa17 | -7.62119 | -42.59048 | 2025-11-18 03:29:00 | NOAA-20 | RIBEIRA DO PIAUÍ | PIAUÍ | Brasil | 2208874 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| f8f014b7-4ba8-37ea-a0cd-3625508f1769 | -10.39248 | -44.92038 | 2025-11-18 03:29:00 | NOAA-20 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| bf13a6b3-392a-34d3-9a98-6b45d672b363 | -7.79879 | -42.62668 | 2025-11-18 03:29:00 | NOAA-20 | RIBEIRA DO PIAUÍ | PIAUÍ | Brasil | 2208874 | 22 | 33 | nan | nan | nan | Caatinga | 2.8 |
| d71bd968-bf3b-3a15-9ea7-7aaa0614f9c6 | -5.47314 | -44.69926 | 2025-11-18 03:29:00 | NOAA-20 | SANTA FILOMENA DO MARANHÃO | MARANHÃO | Brasil | 2109759 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 2e77838d-54d3-3db4-a972-ec4ac8bf298c | -9.05789 | -45.43248 | 2025-11-18 03:29:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 6ec26059-a9b2-3576-86d1-ad5bb578ccdb | -9.05908 | -45.4264 | 2025-11-18 03:29:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 3.1 |
| cdf9bf4a-15d4-3bd8-93a4-c2d43619d452 | -10.74464 | -45.14989 | 2025-11-18 03:29:00 | NOAA-20 | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 5f77a845-6d22-320d-a980-c1c5cc54e2ab | -6.44211 | -43.82606 | 2025-11-18 03:29:00 | NOAA-20 | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 579dd942-890c-3982-9058-3bb46129d60b | -7.248 | -39.38898 | 2025-11-18 03:29:00 | NOAA-20 | CRATO | CEARÁ | Brasil | 2304202 | 23 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 3b61818f-3686-385c-9637-681587d26907 | -6.93526 | -41.5375 | 2025-11-18 03:29:00 | NOAA-20 | SANTANA DO PIAUÍ | PIAUÍ | Brasil | 2209351 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| a4d62901-1cf8-3902-bd67-c9f81e512a58 | -10.7343 | -41.36943 | 2025-11-18 03:29:00 | NOAA-20 | UMBURANAS | BAHIA | Brasil | 2932457 | 29 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 99ead75b-1cb1-3360-895a-4af504b0f92b | -6.67791 | -40.90003 | 2025-11-18 03:29:00 | NOAA-20 | PIO IX | PIAUÍ | Brasil | 2208205 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| cd993bbb-64a3-36e6-81c5-d2168cb86896 | -7.45693 | -42.76473 | 2025-11-18 03:29:00 | NOAA-20 | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 45e1b615-3211-344b-b3d7-030baaa2197f | -6.93585 | -41.53426 | 2025-11-18 03:29:00 | NOAA-20 | SANTANA DO PIAUÍ | PIAUÍ | Brasil | 2209351 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| cf0b97a9-7306-309e-99d9-d344ee2b5c63 | -6.67626 | -40.90939 | 2025-11-18 03:29:00 | NOAA-20 | PIO IX | PIAUÍ | Brasil | 2208205 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 0dbc80c6-2ff8-3dba-b3a4-35d05bc69e1f | -7.62276 | -42.58208 | 2025-11-18 03:29:00 | NOAA-20 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 8858c32d-cbd0-3ccf-91f8-b6761a69ae6c | -6.72514 | -35.22251 | 2025-11-18 03:29:00 | NOAA-20 | CURRAL DE CIMA | PARAÍBA | Brasil | 2505279 | 25 | 33 | nan | nan | nan | Caatinga | 5.4 |
| 2178a8b7-4f4c-3c79-97ce-fa402138b558 | -5.42222 | -43.05307 | 2025-11-18 03:29:00 | NOAA-20 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 6.0 |
| ca8e4c24-c619-3c69-b7df-877669ec03c9 | -5.42825 | -43.05447 | 2025-11-18 03:29:00 | NOAA-20 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 11.9 |
| c57a04c7-297d-319a-812e-8f19095cc9ea | -6.66976 | -43.76888 | 2025-11-18 03:29:00 | NOAA-20 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| b5a351c8-d42d-3e5e-b51e-b7ff651ae24e | -8.7916 | -44.39268 | 2025-11-18 03:29:00 | NOAA-20 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 9ffbff56-cc36-3cbd-8228-04b5568e4443 | -8.38723 | -44.06696 | 2025-11-18 03:29:00 | NOAA-20 | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 5d031a9e-fb41-336b-8c3c-e5fe620ef412 | -8.33461 | -45.36541 | 2025-11-18 03:29:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 730b64dd-5ac6-39d9-a75f-c4dfccb6556f | -10.50477 | -43.9585 | 2025-11-18 03:29:00 | NOAA-20 | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 00a1b247-5954-3a07-a567-7a55d03af2b2 | -5.46791 | -40.96914 | 2025-11-18 03:29:00 | NOAA-20 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 955c0123-3209-3f8b-b4d8-aa2555c73b3d | -6.67329 | -42.04154 | 2025-11-18 03:29:00 | NOAA-20 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 9.8 |
| e28d0181-8109-3949-a343-2202aab9b04e | -5.41698 | -43.04724 | 2025-11-18 03:29:00 | NOAA-20 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 1a0271e0-a866-3a5f-896d-f96b130d0f62 | -7.14033 | -44.92892 | 2025-11-18 03:29:00 | NOAA-20 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 06693759-20e2-3382-9de7-3eec421bf36e | -6.71212 | -40.79636 | 2025-11-18 03:29:00 | NOAA-20 | PIO IX | PIAUÍ | Brasil | 2208205 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 584c2aae-0989-347c-812c-cbb4a92e3bad | -6.81689 | -39.13511 | 2025-11-18 03:29:00 | NOAA-20 | LAVRAS DA MANGABEIRA | CEARÁ | Brasil | 2307502 | 23 | 33 | nan | nan | nan | Caatinga | 2.7 |
| fd99fc67-0d2e-3116-aa3e-d653052af79f | -6.44569 | -45.74926 | 2025-11-18 03:29:00 | NOAA-20 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 11a7d31e-0410-31e6-b8f5-0eebd43be406 | -6.67258 | -42.04546 | 2025-11-18 03:29:00 | NOAA-20 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 9.8 |
| 7fefb932-eba3-3236-a242-d77e9eddcf16 | -8.17172 | -34.98195 | 2025-11-18 03:29:00 | NOAA-20 | JABOATÃO DOS GUARARAPES | PERNAMBUCO | Brasil | 2607901 | 26 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| c4f506b2-5af2-3be9-b119-7573d3021d3e | -6.13169 | -42.96449 | 2025-11-18 03:29:00 | NOAA-20 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| d226fc95-c15a-3faf-b4cd-05af9fd60c76 | -7.33116 | -46.17617 | 2025-11-18 03:29:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 10.8 |
| 7edc5b76-72ef-3242-be8d-6eed3264d491 | -5.47098 | -41.40304 | 2025-11-18 03:29:00 | NOAA-20 | CASTELO DO PIAUÍ | PIAUÍ | Brasil | 2202604 | 22 | 33 | nan | nan | nan | Caatinga | 2.7 |
| 664deb86-c2be-3d05-9299-11c7f0fa18f3 | -7.54284 | -41.19749 | 2025-11-18 03:29:00 | NOAA-20 | MASSAPÊ DO PIAUÍ | PIAUÍ | Brasil | 2206050 | 22 | 33 | nan | nan | nan | Caatinga | 3.3 |
| 4f58be12-5fa1-3642-bc0c-7de3b7014eff | -8.38632 | -44.07181 | 2025-11-18 03:29:00 | NOAA-20 | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 3d555c38-3826-3843-aec4-a3b61f92f438 | -11.01335 | -41.91542 | 2025-11-18 03:29:00 | NOAA-20 | JUSSARA | BAHIA | Brasil | 2918506 | 29 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 5d0ae7ab-f4c7-3a29-9ab2-63170f491930 | -7.62671 | -42.583 | 2025-11-18 03:29:00 | NOAA-20 | RIBEIRA DO PIAUÍ | PIAUÍ | Brasil | 2208874 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| ac270463-6b16-303e-b773-9b5ed1ad27a6 | -7.62766 | -42.58743 | 2025-11-18 03:29:00 | NOAA-20 | RIBEIRA DO PIAUÍ | PIAUÍ | Brasil | 2208874 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 2523e548-9644-35e9-a1ae-31eb25d059f2 | -6.67682 | -40.90625 | 2025-11-18 03:29:00 | NOAA-20 | PIO IX | PIAUÍ | Brasil | 2208205 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| d28b5b0b-134c-370b-8a60-9dfbc1e0c610 | -6.05287 | -39.43987 | 2025-11-18 03:29:00 | NOAA-20 | ACOPIARA | CEARÁ | Brasil | 2300309 | 23 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 8c15b378-c253-3335-8f99-02d3e967081d | -7.24712 | -39.39403 | 2025-11-18 03:29:00 | NOAA-20 | CRATO | CEARÁ | Brasil | 2304202 | 23 | 33 | nan | nan | nan | Caatinga | 2.0 |
| f6c62ef1-9fdb-3f1f-b27b-923abff58779 | -7.9666 | -38.27859 | 2025-11-18 03:29:00 | NOAA-20 | SERRA TALHADA | PERNAMBUCO | Brasil | 2613909 | 26 | 33 | nan | nan | nan | Caatinga | 6.3 |
| 162efced-d92a-3bd8-89db-61e51a7024ca | -6.71615 | -40.80368 | 2025-11-18 03:29:00 | NOAA-20 | PIO IX | PIAUÍ | Brasil | 2208205 | 22 | 33 | nan | nan | nan | Caatinga | 3.0 |
| 06eea95a-3760-39c3-bd6e-11c7d05105cf | -10.85578 | -44.10194 | 2025-11-18 03:29:00 | NOAA-20 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 574ef4a6-dfc3-3aa3-ad93-b697ec9a6545 | -6.72942 | -35.21903 | 2025-11-18 03:29:00 | NOAA-20 | CURRAL DE CIMA | PARAÍBA | Brasil | 2505279 | 25 | 33 | nan | nan | nan | Caatinga | 3.8 |
| a567d87c-63eb-34dd-b119-cd9c2ad87682 | -7.14696 | -44.93013 | 2025-11-18 03:29:00 | NOAA-20 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| f05c7222-fca7-33a9-afc2-dc9b0aeee8b4 | -8.18863 | -39.34485 | 2025-11-18 03:29:00 | NOAA-20 | TERRA NOVA | PERNAMBUCO | Brasil | 2615201 | 26 | 33 | nan | nan | nan | Caatinga | 0.7 |
| f20122bb-208a-3597-a96d-c54d375de81d | -10.23674 | -36.29176 | 2025-11-18 03:29:00 | NOAA-20 | CORURIPE | ALAGOAS | Brasil | 2702306 | 27 | 33 | nan | nan | nan | Mata Atlântica | 16.5 |
| 8350af66-3e5e-3059-aff2-8bbff6029ed8 | -8.53524 | -46.05893 | 2025-11-18 03:29:00 | NOAA-20 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| b278e4b7-38b0-36f5-93da-734c9907592d | -4.77124 | -44.92669 | 2025-11-18 03:29:00 | NOAA-20 | POÇÃO DE PEDRAS | MARANHÃO | Brasil | 2108900 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 02f1c0a5-6742-35ae-9199-1b425d131628 | -6.43682 | -43.81961 | 2025-11-18 03:29:00 | NOAA-20 | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 6c3e6191-1efb-3c02-a962-3543bc60c1df | -10.50562 | -43.95417 | 2025-11-18 03:29:00 | NOAA-20 | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |


[Clique aqui para ver as próximas entradas](README19.md)
