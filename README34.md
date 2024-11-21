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

## Dados Diários - Página 34

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| f58815dc-50f8-3dcd-8690-a7cd37cd7370 | -2.27021 | -53.75009 | 2024-11-21 04:29:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| ab61ea94-d351-3823-812f-79b2a09dbdf9 | -2.69924 | -47.982 | 2024-11-21 04:29:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| a62b12f0-fad7-3915-a4cc-a4839e2d657b | -1.24635 | -51.74919 | 2024-11-21 04:29:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 026b085d-eb1d-397b-bba4-11ad69e2b2b6 | -0.96213 | -51.78304 | 2024-11-21 04:29:00 | NPP-375D | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 3d2d59f2-f485-3ba9-a690-3addf926a7c4 | -2.51243 | -47.23364 | 2024-11-21 04:29:00 | NPP-375D | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| cdd3ad86-e6a6-3f8d-a394-414a41c186ca | -2.68276 | -46.23455 | 2024-11-21 04:29:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 5bd1f239-8878-3aac-97cd-2f3d5838d104 | -1.72571 | -52.70492 | 2024-11-21 04:29:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| c58adc90-7d88-3b6c-b8e1-e1374bba96ad | -1.63877 | -52.59976 | 2024-11-21 04:29:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e8e8a49d-5e2e-3bf4-88ce-e547b1fd5ec7 | -1.96842 | -48.38636 | 2024-11-21 04:29:00 | NPP-375D | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 7331965c-c5de-3231-a39f-1a51deb4f227 | -1.50415 | -54.39951 | 2024-11-21 04:29:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 8748d3e7-9bac-31b3-9021-454eeb095bea | -2.93068 | -49.12461 | 2024-11-21 04:29:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| bd91f572-8af0-305f-8117-6745b0dd65d2 | -3.53877 | -50.5264 | 2024-11-21 04:29:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 24878165-e068-3239-bb7c-9f3c0a6eb9ec | -2.63671 | -46.20609 | 2024-11-21 04:29:00 | NPP-375D | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| df258b43-bbff-371b-abbd-6cf94d9832eb | -3.71919 | -49.43161 | 2024-11-21 04:29:00 | NPP-375D | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 89650f36-26a7-3a03-ba89-464fea4a297c | -1.64577 | -52.66801 | 2024-11-21 04:29:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 5c964098-0b41-329e-a609-36c32a972948 | -3.1294 | -45.44938 | 2024-11-21 04:29:00 | NPP-375D | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 0f721716-da6e-39a6-92ec-7b99e4226dcc | -2.68649 | -46.18885 | 2024-11-21 04:29:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 66d7587b-d620-3d11-98b3-0dab4e694ea4 | -2.80321 | -51.79934 | 2024-11-21 04:29:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| dbe2944a-9bef-344b-b25b-8b9f0d017527 | -2.24851 | -48.15974 | 2024-11-21 04:29:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 0dec1b7e-026c-3715-a207-c8543547b697 | -2.3687 | -53.83706 | 2024-11-21 04:29:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 7.2 |
| 51b2917b-d627-3449-8987-5a67e921a6e3 | -0.05059 | -51.25026 | 2024-11-21 04:29:00 | NPP-375D | SANTANA | AMAPÁ | Brasil | 1600600 | 16 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 845a904f-5685-3bd3-9971-a1ed202d573f | -1.55314 | -53.43905 | 2024-11-21 04:29:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 1f0cdaea-4fdd-3de2-b1cb-96aba50f087c | -1.64547 | -52.61338 | 2024-11-21 04:29:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 4e9f6b7e-f820-363c-9478-3262b6488e5b | -3.99863 | -46.38892 | 2024-11-21 04:29:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| a437df61-248f-346c-8d00-aadaec59a6a1 | -2.0828 | -46.28678 | 2024-11-21 04:29:00 | NPP-375D | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 4b1b8e95-b0d1-348a-afb8-e1fea423464c | 0.14 | -51.09241 | 2024-11-21 04:29:00 | NPP-375D | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 0.6 |
| c68430ce-8533-39b4-b751-ade380c7e8e4 | -2.69058 | -46.24998 | 2024-11-21 04:29:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 8779d6a3-31ac-375d-91d6-706cc1515831 | 0.05039 | -51.71574 | 2024-11-21 04:29:00 | NPP-375D | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 6a96d9e5-ce14-38d4-b670-70caaddae8b4 | -2.59913 | -54.00843 | 2024-11-21 04:29:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 9afdccb4-cf0b-3dcf-9073-0215ed34e5cd | -4.02918 | -43.24027 | 2024-11-21 04:29:00 | NPP-375D | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 72ee951f-df36-35d4-9094-e75e47b2a4dc | -1.42312 | -51.1012 | 2024-11-21 04:29:00 | NPP-375D | MELGAÇO | PARÁ | Brasil | 1504505 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 52a643ba-64da-3937-8183-8fdd2714d33f | -1.71144 | -52.49046 | 2024-11-21 04:29:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| fac27904-3632-3556-b48b-c7c82cb73da8 | -1.98245 | -48.71372 | 2024-11-21 04:29:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 6bdba6a0-e661-3d40-802a-20666f02a932 | -2.92194 | -48.95704 | 2024-11-21 04:29:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e45b2789-b2bb-3507-b0e1-101c7f58e8cb | -0.86426 | -51.85159 | 2024-11-21 04:29:00 | NPP-375D | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 1.8 |
| b69c250e-429b-3492-9cd7-3fcbf1c38240 | -2.2582 | -49.17906 | 2024-11-21 04:29:00 | NPP-375D | IGARAPÉ-MIRI | PARÁ | Brasil | 1503309 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 02f256a4-fe66-39d2-872f-86f24f5096fa | -2.76475 | -52.11423 | 2024-11-21 04:29:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 069b7cc6-541d-3742-b42a-62afe01eba6c | -2.41485 | -47.83249 | 2024-11-21 04:29:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 041d9119-a252-36cf-98b2-045f47510f8a | -2.53357 | -45.43995 | 2024-11-21 04:29:00 | NPP-375D | PRESIDENTE SARNEY | MARANHÃO | Brasil | 2109270 | 21 | 33 | nan | nan | nan | Amazônia | 11.7 |
| 6405f9de-c45f-392c-9319-2ee79b1e7e4f | -2.25579 | -48.42328 | 2024-11-21 04:29:00 | NPP-375D | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 21aee570-479b-30f1-833d-2233b7c2c57a | -2.69323 | -46.21125 | 2024-11-21 04:29:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| fdd29974-b767-3262-8049-51737ce95027 | -0.93395 | -51.72223 | 2024-11-21 04:29:00 | NPP-375D | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 1.0 |
| f4a17497-6f06-3953-9a3f-9487e7110bdd | -3.09006 | -53.13148 | 2024-11-21 04:29:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 5b061455-0166-30dc-bcd5-3791e21e67fb | -2.72005 | -46.08342 | 2024-11-21 04:29:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f76179d0-4ceb-31a2-974b-2de10845f90f | -1.82953 | -46.28249 | 2024-11-21 04:29:00 | NPP-375D | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 3f9cb617-1ada-3731-83b0-a72f3dcc44d7 | -3.28182 | -48.80264 | 2024-11-21 04:29:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b54dd200-9585-3ae3-a82e-9f85defa9191 | -3.2798 | -50.21091 | 2024-11-21 04:29:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 1622d535-dbde-3034-a83d-95539a6af6d1 | -2.43721 | -48.40302 | 2024-11-21 04:29:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 12e42949-2dca-3088-89e5-714c15ffc807 | -1.95194 | -46.25589 | 2024-11-21 04:29:00 | NPP-375D | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| ac9d1676-c380-3c09-971f-bed71edc754d | -1.04432 | -51.74345 | 2024-11-21 04:29:00 | NPP-375D | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 3.1 |
| f373283b-c45a-323e-a818-2d12bfb58083 | -2.69275 | -46.2361 | 2024-11-21 04:29:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 13deb6a9-276c-30ad-86cb-eb43e1f46907 | -3.96347 | -46.72188 | 2024-11-21 04:29:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 14859838-71d0-3671-aa73-64d6effa68e9 | -2.08171 | -46.2937 | 2024-11-21 04:29:00 | NPP-375D | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| d37e96f8-a2b6-3d7b-94d3-067953e936e4 | -2.55629 | -46.54457 | 2024-11-21 04:29:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| da67f5d0-3694-3d5f-982e-be825f0b8c84 | -2.9267 | -48.33434 | 2024-11-21 04:29:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| d5886630-9b20-39c1-8425-82f9bc506ab0 | -3.15282 | -46.62346 | 2024-11-21 04:29:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 6e9bb497-1f38-3cab-a4a7-8f63a81c3567 | -2.66619 | -46.23555 | 2024-11-21 04:29:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 2e696112-d205-33da-8f8d-718b1eb0a7bc | -1.66026 | -45.7476 | 2024-11-21 04:29:00 | NPP-375D | CÂNDIDO MENDES | MARANHÃO | Brasil | 2102606 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d53b10a1-e523-3ab4-8b0e-47f67214ed03 | -1.57882 | -50.43761 | 2024-11-21 04:29:00 | NPP-375D | BREVES | PARÁ | Brasil | 1501808 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 93bf652d-6fd5-3202-b6e2-8609428e19f4 | -1.0583 | -51.74956 | 2024-11-21 04:29:00 | NPP-375D | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 47d8fe55-d84d-3932-875b-3d9a00f96442 | -2.144 | -53.77761 | 2024-11-21 04:29:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| bdc66f84-2cc5-3907-82e8-d7b8ad8aabc8 | -1.11107 | -52.11861 | 2024-11-21 04:29:00 | NPP-375D | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 1.5 |
| d048e9ac-4e3d-3e26-811e-d8bcdc8d98e0 | -1.4977 | -51.99199 | 2024-11-21 04:29:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| a9875e4c-3885-32aa-a28c-bd292fbdeb0a | -4.00066 | -43.24997 | 2024-11-21 04:29:00 | NPP-375D | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| fcde2307-6c4b-37ff-a57b-55d500f68aea | -1.43266 | -46.00849 | 2024-11-21 04:29:00 | NPP-375D | CARUTAPERA | MARANHÃO | Brasil | 2102903 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| fb695723-5eeb-393c-808a-a78ae9082013 | -2.22468 | -48.37789 | 2024-11-21 04:29:00 | NPP-375D | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f48af2e9-daaa-3806-9e15-fa8cc31fe3ae | -2.56238 | -46.54905 | 2024-11-21 04:29:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 0f6d658f-dd9a-379e-a143-e788ed071b5f | -2.72339 | -46.08394 | 2024-11-21 04:29:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| aa16f6b5-4298-35ba-8f23-29458fcf3480 | -1.04657 | -51.74396 | 2024-11-21 04:29:00 | NPP-375D | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 37120a77-3739-3fd4-96c1-ae871216c821 | -3.77918 | -46.66862 | 2024-11-21 04:29:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 8626655b-dc73-37c2-9655-29f40f7667f3 | -2.6368 | -46.57127 | 2024-11-21 04:29:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 75268579-ec8c-3e4e-ae44-5536a82d105e | -3.46252 | -50.83011 | 2024-11-21 04:29:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 1c9d501a-8616-3fba-b555-cfdb8fe1676d | -2.62034 | -51.79876 | 2024-11-21 04:29:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 589521e6-886d-32bc-97f5-b826397b25a8 | -2.83014 | -46.67607 | 2024-11-21 04:29:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 6f7b5357-d23a-3d02-a55b-9d6ac3d55d6a | -2.78256 | -51.71725 | 2024-11-21 04:29:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 035d4d9c-d9fa-3ea7-89d1-9d049561c2b0 | -4.14874 | -43.87638 | 2024-11-21 04:29:00 | NPP-375D | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| e98bd8d8-01e4-316f-846f-0f931f4f719b | -1.46599 | -52.67468 | 2024-11-21 04:29:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| ad355930-2017-3548-839e-bca07c8994fe | -0.42042 | -51.56831 | 2024-11-21 04:29:00 | NPP-375D | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 3.3 |
| d54de255-bd2c-305b-a1fd-fa353bc42b4a | -2.68779 | -46.24599 | 2024-11-21 04:29:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 65c51a35-d996-334a-a05b-249c29d1e80b | -2.56548 | -49.19784 | 2024-11-21 04:29:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 35b50e96-a3b5-3b79-bbf9-e6a92d5f3925 | -2.9087 | -48.31681 | 2024-11-21 04:29:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 9ea1c93a-b72f-32b8-a1d4-75e42f4bd914 | -1.19808 | -51.97644 | 2024-11-21 04:29:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 5a6f6dbe-7314-3a55-93e6-3b4c1217bed1 | -1.64775 | -46.9637 | 2024-11-21 04:29:00 | NPP-375D | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 10057f20-d280-34a5-9aee-62b82274749e | -2.19865 | -50.27786 | 2024-11-21 04:29:00 | NPP-375D | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d82fe9a3-19d8-3cc6-a4a3-7455a4ed6a6e | -2.65824 | -46.15598 | 2024-11-21 04:29:00 | NPP-375D | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |
| e3881eae-7d8b-30da-ab5e-c89999b676f6 | -3.95296 | -46.72377 | 2024-11-21 04:29:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 4978e93b-416a-30dd-a502-d33592f1859b | -2.84342 | -46.67814 | 2024-11-21 04:29:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 750d0653-b7f3-33f4-a18d-fb1814c5ebdf | -3.39788 | -50.10448 | 2024-11-21 04:29:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| bed48cea-4cc8-3725-abe2-dd6f55e68eac | -1.44303 | -49.58694 | 2024-11-21 04:29:00 | NPP-375D | SÃO SEBASTIÃO DA BOA VISTA | PARÁ | Brasil | 1507706 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d062d221-68a9-3e4e-9450-1f1c3cdd558b | -1.73656 | -52.38894 | 2024-11-21 04:29:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 7.3 |
| 8fb3cfcf-bb18-3a60-b4e8-f9049835d5c1 | -2.51189 | -47.2371 | 2024-11-21 04:29:00 | NPP-375D | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| e5b72a85-4b6e-3852-b504-8f020d1937e1 | -2.01133 | -54.52454 | 2024-11-21 04:29:00 | NPP-375D | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 8.5 |
| d91380d1-42a3-3275-9d15-a3d37d82df1b | -2.80373 | -51.77078 | 2024-11-21 04:29:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| e89595df-ef31-3523-be42-eaa94f55ce26 | -0.17381 | -51.63198 | 2024-11-21 04:29:00 | NPP-375D | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 0.9 |
| a7a48ee7-1fd8-336f-bcf6-09d3512c36c5 | -3.28465 | -45.97663 | 2024-11-21 04:29:00 | NPP-375D | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| b9c7eec4-4189-36a5-a11c-7c70b398dc6a | -3.67161 | -45.23991 | 2024-11-21 04:29:00 | NPP-375D | MONÇÃO | MARANHÃO | Brasil | 2106904 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| f94b69e7-21df-3193-9b99-bbcce72fd497 | -2.67715 | -46.16605 | 2024-11-21 04:29:00 | NPP-375D | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 2.5 |
| b88ea227-a87b-334a-b44e-57cd75682f16 | -2.94195 | -45.19422 | 2024-11-21 04:29:00 | NPP-375D | SÃO VICENTE FERRER | MARANHÃO | Brasil | 2111706 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 28c4d7b4-a6a8-31ef-a379-6339756bdaf9 | -2.74161 | -47.53981 | 2024-11-21 04:29:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 566e4b46-49e5-30d8-bc88-db049351407c | -3.25716 | -50.39843 | 2024-11-21 04:29:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |


[Clique aqui para ver as próximas entradas](README35.md)
