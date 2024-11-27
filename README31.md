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

## Dados Diários - Página 31

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| db4c97d7-fc3a-3494-a142-cb995696a435 | -3.0949 | -53.2588 | 2024-11-27 04:00:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 192.6 |
| 1863d976-9733-3730-8795-0bce206df6ec | -3.1133 | -53.2583 | 2024-11-27 04:00:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 122.9 |
| a78103ab-994b-3a85-9ecb-940a36d33ebb | -2.8346 | -54.1326 | 2024-11-27 04:00:00 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 70.2 |
| ca0b3b75-b920-3962-ba8b-6d5edd8c1242 | -3.0393 | -48.5082 | 2024-11-27 04:00:00 | GOES-16 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 42.7 |
| e44fa4ac-99cc-3fe3-8715-72a313830813 | -23.33878 | -46.77188 | 2024-11-27 04:01:00 | NOAA-21 | CAIEIRAS | SÃO PAULO | Brasil | 3509007 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 75e967d7-029c-37d1-857d-992399d2cd77 | -22.85043 | -45.80823 | 2024-11-27 04:01:00 | NOAA-21 | MONTEIRO LOBATO | SÃO PAULO | Brasil | 3531704 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 042b05bf-7889-3f6d-b1cd-e82401d10b4f | -23.83673 | -47.05541 | 2024-11-27 04:01:00 | NOAA-21 | IBIÚNA | SÃO PAULO | Brasil | 3519709 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| cc06bea9-e1a8-3994-bda7-fa9468f6f867 | -21.33992 | -53.3729 | 2024-11-27 04:01:00 | NOAA-21 | RIBAS DO RIO PARDO | MATO GROSSO DO SUL | Brasil | 5007109 | 50 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 7a279c02-7964-388e-b457-44a9ea0fe836 | -22.14633 | -50.86468 | 2024-11-27 04:01:00 | NOAA-21 | RANCHARIA | SÃO PAULO | Brasil | 3542206 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| fc89e9ae-9065-3273-8c2f-7a8ce53f48a3 | -23.47168 | -46.29854 | 2024-11-27 04:01:00 | NOAA-21 | ITAQUAQUECETUBA | SÃO PAULO | Brasil | 3523107 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 638e7953-497b-3e50-a27b-709e65793863 | -22.9853 | -50.40221 | 2024-11-27 04:01:00 | NOAA-21 | ITAMBARACÁ | PARANÁ | Brasil | 4111001 | 41 | 33 | nan | nan | nan | Mata Atlântica | 15.5 |
| 336418df-afc3-38bb-a903-aa1f8ccbbac1 | -22.98641 | -50.39691 | 2024-11-27 04:01:00 | NOAA-21 | ITAMBARACÁ | PARANÁ | Brasil | 4111001 | 41 | 33 | nan | nan | nan | Mata Atlântica | 15.5 |
| f39f7dc8-6526-30af-a3c9-291a1729b323 | -23.59324 | -47.43819 | 2024-11-27 04:01:00 | NOAA-21 | VOTORANTIM | SÃO PAULO | Brasil | 3557006 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| f6b36d4f-51ff-3842-800c-0f7fb4eb22e9 | -22.11574 | -49.60955 | 2024-11-27 04:01:00 | NOAA-21 | GARÇA | SÃO PAULO | Brasil | 3516705 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| 95686f8f-7f4e-3dbc-981a-226b92b9e261 | -23.70704 | -46.47853 | 2024-11-27 04:01:00 | NOAA-21 | MAUÁ | SÃO PAULO | Brasil | 3529401 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| ef98f99b-1298-3eda-99da-7f603b204df3 | -23.36435 | -47.05511 | 2024-11-27 04:01:00 | NOAA-21 | ARAÇARIGUAMA | SÃO PAULO | Brasil | 3502754 | 35 | 33 | nan | nan | nan | Mata Atlântica | 6.9 |
| 81f13307-c931-3ef8-8472-3a1244dfb019 | -23.33762 | -46.77348 | 2024-11-27 04:01:00 | NOAA-21 | CAIEIRAS | SÃO PAULO | Brasil | 3509007 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| f9513806-5b24-3122-bc8f-c62f7955661f | -22.98174 | -50.39598 | 2024-11-27 04:01:00 | NOAA-21 | ITAMBARACÁ | PARANÁ | Brasil | 4111001 | 41 | 33 | nan | nan | nan | Mata Atlântica | 15.5 |
| ed0c9e78-9978-3f0b-af6d-a3f96716f257 | -22.98062 | -50.40128 | 2024-11-27 04:01:00 | NOAA-21 | ITAMBARACÁ | PARANÁ | Brasil | 4111001 | 41 | 33 | nan | nan | nan | Mata Atlântica | 15.5 |
| 31585978-2e2e-3464-b865-828bd1a76b63 | -22.1148 | -49.61426 | 2024-11-27 04:01:00 | NOAA-21 | GARÇA | SÃO PAULO | Brasil | 3516705 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| a4fefbf3-9269-3d96-90f7-2efee8b3f181 | -22.10576 | -49.61242 | 2024-11-27 04:01:00 | NOAA-21 | PIRAJUÍ | SÃO PAULO | Brasil | 3538907 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.2 |
| e6e3bb80-5e4f-3f6f-9d65-48fc7f5e2ed3 | -22.14149 | -50.86345 | 2024-11-27 04:01:00 | NOAA-21 | RANCHARIA | SÃO PAULO | Brasil | 3542206 | 35 | 33 | nan | nan | nan | Mata Atlântica | 14.7 |
| a4327422-4e2e-3e2a-9806-5b216fbbab27 | -25.06273 | -51.15549 | 2024-11-27 04:01:00 | NOAA-21 | PRUDENTÓPOLIS | PARANÁ | Brasil | 4120606 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| a2d76860-49b6-3a82-9964-a2288245b6fa | -21.34564 | -53.37347 | 2024-11-27 04:01:00 | NOAA-21 | RIBAS DO RIO PARDO | MATO GROSSO DO SUL | Brasil | 5007109 | 50 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 97898eea-0c24-31ba-a048-409b6f79c708 | -22.14276 | -50.85748 | 2024-11-27 04:01:00 | NOAA-21 | RANCHARIA | SÃO PAULO | Brasil | 3542206 | 35 | 33 | nan | nan | nan | Mata Atlântica | 14.7 |
| b83c3039-1e80-3ac5-b7e8-8d738b3f15b6 | -22.90088 | -43.753 | 2024-11-27 04:01:00 | NOAA-21 | RIO DE JANEIRO | RIO DE JANEIRO | Brasil | 3304557 | 33 | 33 | nan | nan | nan | Mata Atlântica | 2.8 |
| 927aefa2-e5ef-31e1-9cc6-d534c8243b89 | -21.33985 | -53.3723 | 2024-11-27 04:01:00 | NOAA-21 | RIBAS DO RIO PARDO | MATO GROSSO DO SUL | Brasil | 5007109 | 50 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 0c991a49-2952-33c8-8ac7-96dfd48d1ba5 | -26.80779 | -48.6582 | 2024-11-27 04:01:00 | NOAA-21 | PENHA | SANTA CATARINA | Brasil | 4212502 | 42 | 33 | nan | nan | nan | Mata Atlântica | 0.4 |
| 86d3bbe8-94aa-3e84-b8b3-e583b06a9e6c | -22.5398 | -48.81145 | 2024-11-27 04:01:00 | NOAA-21 | MACATUBA | SÃO PAULO | Brasil | 3528007 | 35 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 3276fc0b-3b62-3f86-a2b5-20440feeb1e0 | -29.87307 | -51.15613 | 2024-11-27 04:04:00 | NOAA-21 | CANOAS | RIO GRANDE DO SUL | Brasil | 4304606 | 43 | 33 | nan | nan | nan | Pampa | 1.6 |
| 75bd9308-436f-3aff-b163-59bdcc88f457 | -2.8346 | -54.1326 | 2024-11-27 04:10:00 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 69.3 |
| 513440f8-8c3c-3968-9dd7-f42ec728011e | -2.9428 | -54.7904 | 2024-11-27 04:10:00 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 34.0 |
| db26946b-1764-355d-9967-62724242d072 | -3.9674 | -48.0851 | 2024-11-27 04:10:00 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 35.5 |
| 8654d3f9-3351-3e40-ae4e-5659e1b4624e | -3.1692 | -48.4179 | 2024-11-27 04:10:00 | GOES-16 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 50.0 |
| fc4d4059-4bbc-31a9-b966-cb3509be4c89 | -3.1133 | -53.2583 | 2024-11-27 04:10:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 126.5 |
| 899269bf-7199-3e7b-8510-b59f6b49ed1c | -3.0949 | -53.2385 | 2024-11-27 04:10:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 72.2 |
| 9d28c120-1a62-364f-aabc-19fbd98b1311 | -22.9841 | -50.4019 | 2024-11-27 04:10:00 | GOES-16 | ITAMBARACÁ | PARANÁ | Brasil | 4111001 | 41 | 33 | nan | nan | nan | Mata Atlântica | 78.2 |
| 86d926fc-091b-3981-bf74-734d990d9e16 | -2.1928 | -53.7839 | 2024-11-27 04:10:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 62.9 |
| 69cd6b71-aed3-3bae-b589-a9f15cc83100 | -3.1133 | -53.2381 | 2024-11-27 04:10:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 59.0 |
| 3b98f9ca-6e8f-3d0b-b8cb-75a94f227a26 | -2.8347 | -54.1125 | 2024-11-27 04:10:00 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 91.0 |
| c94bd658-287b-3ca1-b136-c684483dd8fc | -3.0393 | -48.5082 | 2024-11-27 04:10:00 | GOES-16 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 57.3 |
| 3a93233a-1f53-3759-b90d-58414b23452a | -3.0949 | -53.2588 | 2024-11-27 04:10:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 161.1 |
| c33ebcb3-ae4b-3dd2-81fb-b60cdab3173c | -3.1691 | -48.4394 | 2024-11-27 04:10:00 | GOES-16 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 106.4 |
| e9d9040a-91fd-3d53-b28e-5a2b5b3e88b1 | -3.1876 | -48.4387 | 2024-11-27 04:10:00 | GOES-16 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 51.7 |
| 235f558e-6198-399f-92a6-c0e236fd3202 | 2.08607 | -50.64048 | 2024-11-27 04:16:00 | NPP-375D | AMAPÁ | AMAPÁ | Brasil | 1600105 | 16 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 9a2110ee-29fc-3110-9745-39aca52796a0 | 2.08028 | -50.63569 | 2024-11-27 04:16:00 | NPP-375D | AMAPÁ | AMAPÁ | Brasil | 1600105 | 16 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 62e6b783-376b-3128-963f-fd15531546ed | 2.07533 | -50.63645 | 2024-11-27 04:16:00 | NPP-375D | AMAPÁ | AMAPÁ | Brasil | 1600105 | 16 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 9c63ab6d-2e88-35c2-9851-84e906028066 | -4.24346 | -48.67709 | 2024-11-27 04:18:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| c0a063e3-a6a9-3ca2-87aa-2d56492b1449 | -5.84941 | -39.12914 | 2024-11-27 04:18:00 | NPP-375D | SOLONÓPOLE | CEARÁ | Brasil | 2313005 | 23 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 297a7f95-4182-336b-b356-d5c33e09a501 | -2.84431 | -53.98715 | 2024-11-27 04:18:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 64cd2abf-812d-3517-918d-14e29f53a6bb | -3.50744 | -50.45909 | 2024-11-27 04:18:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| f01bb685-9e2f-3001-9f58-3ec237da422b | -3.58411 | -45.15422 | 2024-11-27 04:18:00 | NPP-375D | MONÇÃO | MARANHÃO | Brasil | 2106904 | 21 | 33 | nan | nan | nan | Amazônia | 0.4 |
| af151ced-a650-3eb3-9808-8cfbe8f1730e | -3.12242 | -49.21943 | 2024-11-27 04:18:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 3e6da1f5-1bb1-3263-9f21-dc4d1a80dfed | -3.57557 | -41.95823 | 2024-11-27 04:18:00 | NPP-375D | JOAQUIM PIRES | PIAUÍ | Brasil | 2205409 | 22 | 33 | nan | nan | nan | Caatinga | 25.4 |
| baa135ae-6109-32fa-a277-28c18998dd80 | -2.56908 | -46.42339 | 2024-11-27 04:18:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 05ca4989-2772-33da-9198-2b51d1e2b697 | -1.78581 | -52.74424 | 2024-11-27 04:18:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 8a6f3355-443b-3476-8b30-bd6c9382645c | -2.71193 | -46.11259 | 2024-11-27 04:18:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 734fe684-5c23-329d-b3b3-2f97d3cc4cd9 | -3.16187 | -48.4351 | 2024-11-27 04:18:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 18.0 |
| a71765e4-b661-33d6-8485-c58845151a5b | -3.9679 | -48.0653 | 2024-11-27 04:18:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| d39c5b1e-6fa5-314c-b8f0-75a46e08896a | -4.21282 | -48.6672 | 2024-11-27 04:18:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 7.6 |
| 96365396-8198-3fce-a6b3-9d4cadea71d2 | -4.05077 | -46.85182 | 2024-11-27 04:18:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c531f81b-a8af-3859-b9c8-1ba161868f69 | -5.58472 | -43.1531 | 2024-11-27 04:18:00 | NPP-375D | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Caatinga | 3.7 |
| 316e0ead-de5f-3356-b9e6-0cd719bed429 | -3.33106 | -53.71835 | 2024-11-27 04:18:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b7f3ba8e-fd84-3608-9f74-22c8e17cc4b9 | -2.18025 | -53.77034 | 2024-11-27 04:18:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 9ad48f27-cef3-387a-acc3-8c0b983aa40b | -1.36481 | -52.12828 | 2024-11-27 04:18:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 87ec36e6-d290-3a2e-9098-1c1de55d50e4 | -3.67832 | -47.21358 | 2024-11-27 04:18:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| dbe9b419-7c68-3a4e-8f96-b1cc4ca6d901 | -2.25095 | -53.62603 | 2024-11-27 04:18:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| e5e4e5ef-fab7-36ca-a4ca-223670a4ee9c | -3.81387 | -46.60163 | 2024-11-27 04:18:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| c8453246-8f71-3a74-81e6-22696ff74d97 | -0.48028 | -48.63629 | 2024-11-27 04:18:00 | NPP-375D | SOURE | PARÁ | Brasil | 1507904 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 52f10712-94ca-3db1-a150-eb5bc3b54d73 | -6.90681 | -35.0378 | 2024-11-27 04:18:00 | NPP-375D | RIO TINTO | PARAÍBA | Brasil | 2512903 | 25 | 33 | nan | nan | nan | Mata Atlântica | 2.4 |
| 589355c9-f001-35d1-a5ff-007dea69debf | -2.93567 | -54.79809 | 2024-11-27 04:18:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| e6459fb1-d7d5-332f-97cb-8b1c12ae2a6c | -3.43274 | -54.54065 | 2024-11-27 04:18:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 722448e6-9202-3460-9bac-a4d2d68be1d2 | -2.94242 | -51.53616 | 2024-11-27 04:18:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 791b093f-6631-3970-9fca-24b63afdd01b | -1.20139 | -51.75366 | 2024-11-27 04:18:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 426f328d-ae9c-3324-95bd-9b430d83ade3 | -3.97551 | -48.06649 | 2024-11-27 04:18:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 608a91bf-0c75-3e21-9b3c-34e9c3d4268a | -3.94322 | -46.89369 | 2024-11-27 04:18:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 65ae18f7-8037-3ade-bef4-eae3072360f0 | -3.50904 | -50.3111 | 2024-11-27 04:18:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 7a3ad2f0-1bc4-390a-ab2c-51011c7ea8d0 | -2.70195 | -46.19804 | 2024-11-27 04:18:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 6bc88278-b177-3762-bcca-51c092d26ead | -2.09877 | -53.35431 | 2024-11-27 04:18:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 2f714a55-b251-3967-9dd2-6ddefaf7fddc | -3.51956 | -50.22049 | 2024-11-27 04:18:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 59cf11ba-d973-31e7-ba77-af41983a66ef | -5.58928 | -35.43676 | 2024-11-27 04:18:00 | NPP-375D | CEARÁ-MIRIM | RIO GRANDE DO NORTE | Brasil | 2402600 | 24 | 33 | nan | nan | nan | Caatinga | 2.2 |
| aa92efc9-11c6-39e4-9625-b60130a6555b | -2.72064 | -46.28473 | 2024-11-27 04:18:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 519f446d-e06e-3d2a-b6e6-bed3c352b9dc | -4.68658 | -40.6933 | 2024-11-27 04:18:00 | NPP-375D | IPUEIRAS | CEARÁ | Brasil | 2305902 | 23 | 33 | nan | nan | nan | Caatinga | 0.5 |
| f238a920-8e22-3bf8-b05c-ba1b4b3d8052 | -1.66084 | -52.71648 | 2024-11-27 04:18:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 8db67c2b-47b1-3191-9e11-69515cea14a6 | -2.23901 | -53.62792 | 2024-11-27 04:18:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 2344e0bb-fee5-3cbe-a06e-380b9c9fc306 | -2.72309 | -46.26912 | 2024-11-27 04:18:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 1e08a4c6-dfbe-358e-8abd-377eecbbaf53 | -3.77368 | -52.39713 | 2024-11-27 04:18:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| b2dd0f5e-323c-33ea-b7e6-6329ad0c6a7a | -3.10958 | -53.26986 | 2024-11-27 04:18:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 01749d7c-daac-37b1-92cc-eb8ee2d6652f | -3.3183 | -54.09924 | 2024-11-27 04:18:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ae2c72f8-8eaf-33da-9e8e-c296da87275a | -2.88506 | -51.38408 | 2024-11-27 04:18:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 1f9bdc3b-24f4-39e3-9775-1785f822a4a8 | -5.58528 | -43.14952 | 2024-11-27 04:18:00 | NPP-375D | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 67653b74-cc64-3358-a6ee-000012d6ffdb | -2.55918 | -45.13752 | 2024-11-27 04:18:00 | NPP-375D | PINHEIRO | MARANHÃO | Brasil | 2108603 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 3cf553a4-dda1-3dff-b92f-1b26c40d0767 | -2.88961 | -45.25462 | 2024-11-27 04:18:00 | NPP-375D | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 18c7333f-faab-3933-957e-d86a8c021b2a | -3.08249 | -47.81081 | 2024-11-27 04:18:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a747d3d8-7f4b-3d8a-b43a-1d516f55eb69 | -2.82317 | -46.82064 | 2024-11-27 04:18:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 9ed35601-4036-3a7c-91e9-2354d34f7f98 | -3.23263 | -50.19236 | 2024-11-27 04:18:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 1c680f5e-301e-3a45-b955-b3dab7100882 | -4.17937 | -48.62596 | 2024-11-27 04:18:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| ff7307c5-6166-3a60-9821-b29c6a1e5ad8 | -1.35195 | -54.63437 | 2024-11-27 04:18:00 | NPP-375D | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 9ed995b1-e11f-35cb-80c0-87463faa4821 | -2.90143 | -45.38208 | 2024-11-27 04:18:00 | NPP-375D | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 6d8ffaf2-aa59-3cb6-9475-0ae87f839d31 | -3.88551 | -43.15627 | 2024-11-27 04:18:00 | NPP-375D | BURITI | MARANHÃO | Brasil | 2102200 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |


[Clique aqui para ver as próximas entradas](README32.md)
