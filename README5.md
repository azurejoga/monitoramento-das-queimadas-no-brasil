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

## Dados Diários - Página 5

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 80065d9e-a4db-3a99-a029-4a7d4b8ba584 | -4.8876 | -37.52979 | 2025-06-17 03:13:00 | NOAA-20 | ARACATI | CEARÁ | Brasil | 2301109 | 23 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 643fdcc2-dff2-3e54-9289-567548c42ab3 | -4.88873 | -37.52316 | 2025-06-17 03:13:00 | NOAA-20 | ARACATI | CEARÁ | Brasil | 2301109 | 23 | 33 | nan | nan | nan | Caatinga | 1.7 |
| aa96f5a3-64fa-3178-9a10-a68d39fe8a18 | -8.06535 | -43.11603 | 2025-06-17 03:15:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 11.1 |
| 250536c4-4b04-3a58-b842-bea4083bcb7e | -7.22957 | -43.08089 | 2025-06-17 03:15:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 3.8 |
| e972816c-2532-3e52-bfef-3a6074b84c0e | -7.23533 | -43.08947 | 2025-06-17 03:15:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 11.5 |
| 5196c25a-2b5f-306c-b824-494a6dc56cf7 | -8.06898 | -43.11604 | 2025-06-17 03:15:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 7.6 |
| 3ae03719-abf4-3b0d-b0a3-28268cef38e8 | -8.07742 | -43.11062 | 2025-06-17 03:15:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 7.6 |
| 379ac92c-81e4-3a67-89ef-e41bd4c4001c | -8.07605 | -43.11751 | 2025-06-17 03:15:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 7.6 |
| 1b71b0fc-aa6f-3e43-9954-c9ed4b09385e | -8.0667 | -43.10905 | 2025-06-17 03:15:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 10.2 |
| c9e75508-7805-3537-8b21-ae14d4d38110 | -7.24249 | -43.09083 | 2025-06-17 03:15:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 11.5 |
| f94d50af-f91f-3668-9842-5d6841ce688d | -8.07037 | -43.1091 | 2025-06-17 03:15:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 7.6 |
| 1261a89e-749c-328d-9c3c-e97f9f8f16dc | -8.07241 | -43.1175 | 2025-06-17 03:15:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 11.1 |
| 533a944b-6680-333d-8281-a0bab2926349 | -7.23427 | -43.0825 | 2025-06-17 03:15:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 15.8 |
| 8fe5b58b-ec5d-37d4-9f6f-3ab1e9de9c9c | -8.07375 | -43.11059 | 2025-06-17 03:15:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 10.2 |
| 356801ee-add2-381b-8b37-20e424375eae | -7.24006 | -43.09118 | 2025-06-17 03:15:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 9.6 |
| 8cbd59fb-6589-3739-a410-017c97ab69f8 | -7.23291 | -43.08969 | 2025-06-17 03:15:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 9.6 |
| a6cced51-a4e1-37c1-b4bb-9fc36b70dae7 | -7.24967 | -43.09212 | 2025-06-17 03:15:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 6.5 |
| a7cde18d-3c3e-3d9b-b944-7ed6b6678fd1 | -7.24723 | -43.09252 | 2025-06-17 03:15:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 19.1 |
| a7edfa34-91fc-395c-94f7-8e009dd2ef19 | -7.23674 | -43.08221 | 2025-06-17 03:15:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 11.5 |
| 899bbba0-86eb-3472-b460-c15b5eb1eb5b | -12.22585 | -44.21422 | 2025-06-17 03:17:00 | NOAA-20 | CRISTÓPOLIS | BAHIA | Brasil | 2909703 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| bd3b6f3f-cf45-3171-b6ec-882a48f1f50d | -14.85935 | -45.12703 | 2025-06-17 03:17:00 | NOAA-20 | BONITO DE MINAS | MINAS GERAIS | Brasil | 3108255 | 31 | 33 | nan | nan | nan | Cerrado | 2.2 |
| e73ac4a3-c617-309f-b93f-f09fcbf374e3 | -12.22972 | -44.21684 | 2025-06-17 03:17:00 | NOAA-20 | CRISTÓPOLIS | BAHIA | Brasil | 2909703 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 387bfb67-ae69-3b7c-bcff-e47ae5b208e4 | -12.22436 | -44.2213 | 2025-06-17 03:17:00 | NOAA-20 | CRISTÓPOLIS | BAHIA | Brasil | 2909703 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 0b3db9f2-4b60-33f7-9c18-007ba335f756 | -12.22817 | -44.22396 | 2025-06-17 03:17:00 | NOAA-20 | CRISTÓPOLIS | BAHIA | Brasil | 2909703 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| b762fbaa-1836-3ad1-8cc9-2857dc528047 | -19.71668 | -40.35264 | 2025-06-17 03:19:00 | NOAA-20 | JOÃO NEIVA | ESPÍRITO SANTO | Brasil | 3203130 | 32 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 1b882ee3-dcb6-339e-b482-84530d8bd341 | -21.17957 | -43.98001 | 2025-06-17 03:19:00 | NOAA-20 | BARROSO | MINAS GERAIS | Brasil | 3105905 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 0a494a9c-af7c-321c-a8d2-5303b7cbdf8c | -21.97524 | -42.80434 | 2025-06-17 03:19:00 | NOAA-20 | SAPUCAIA | RIO DE JANEIRO | Brasil | 3305406 | 33 | 33 | nan | nan | nan | Mata Atlântica | 3.1 |
| c9996089-f3e9-3587-b646-8e36e96faa21 | -20.00764 | -44.18176 | 2025-06-17 03:19:00 | NOAA-20 | BETIM | MINAS GERAIS | Brasil | 3106705 | 31 | 33 | nan | nan | nan | Mata Atlântica | 9.7 |
| 8a0fc16a-6d8d-331c-b7b7-ac7bd9521961 | -20.00877 | -44.17679 | 2025-06-17 03:19:00 | NOAA-20 | BETIM | MINAS GERAIS | Brasil | 3106705 | 31 | 33 | nan | nan | nan | Mata Atlântica | 9.7 |
| d968245d-dc8d-3988-9a07-9b0fa2df93e3 | -8.0703 | -43.0981 | 2025-06-17 03:20:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 63.7 |
| dc785fb4-c7eb-3f9d-8ed6-d6c5be7e7fc4 | -10.9355 | -56.8322 | 2025-06-17 03:20:00 | GOES-19 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 48.0 |
| de339fda-7b9e-38d4-a56b-4af8a1ab1e2d | -8.07 | -43.1216 | 2025-06-17 03:30:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 65.1 |
| b27b3af1-a346-321b-921d-626c03e336c7 | -10.6043 | -48.5845 | 2025-06-17 04:00:00 | GOES-19 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 35.9 |
| dc45019e-1872-33f6-a90b-0a4f647b3283 | -8.07 | -43.1216 | 2025-06-17 04:00:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 68.7 |
| 22aa3266-103c-31a4-8e8a-90a1669aa9c9 | -8.0703 | -43.0981 | 2025-06-17 04:00:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 70.7 |
| 05445f97-d982-38d1-9199-8bde2ebd7298 | -2.87503 | -40.38137 | 2025-06-17 04:06:00 | NOAA-21 | CRUZ | CEARÁ | Brasil | 2304251 | 23 | 33 | nan | nan | nan | Caatinga | 0.5 |
| d1c9dac2-34c7-3f98-9382-7f781e63bddb | -3.77306 | -41.60234 | 2025-06-17 04:06:00 | NOAA-21 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 145be7a5-d1f7-3c60-9649-00803a138b60 | -2.44833 | -47.49886 | 2025-06-17 04:06:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 4d182f05-7063-30ec-ae13-0fb80ed1cdd0 | -3.77636 | -41.60286 | 2025-06-17 04:06:00 | NOAA-21 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 0.6 |
| f7e991f7-e838-3d5c-8c22-46fd8afd2b52 | -3.9999 | -43.24283 | 2025-06-17 04:06:00 | NOAA-21 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| b1e74bc2-daac-30fe-80da-b64a6475af68 | -4.13658 | -43.06887 | 2025-06-17 04:06:00 | NOAA-21 | COELHO NETO | MARANHÃO | Brasil | 2103406 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| bc0aa208-2d93-3d16-bbbe-7ed4abb848ec | -3.77967 | -41.60337 | 2025-06-17 04:06:00 | NOAA-21 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 37f60e66-f871-37a7-bb99-8ee0e1b4bc97 | -4.13317 | -43.06834 | 2025-06-17 04:06:00 | NOAA-21 | COELHO NETO | MARANHÃO | Brasil | 2103406 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 3cf42ea9-f104-35ca-b504-5b0a59d152fc | -3.76975 | -41.60184 | 2025-06-17 04:06:00 | NOAA-21 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 1a38b021-c889-302f-a6e1-910bcb7a6463 | -2.45285 | -47.49961 | 2025-06-17 04:06:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 38cd8905-5859-3c16-9805-aa4cde5e7236 | -3.77251 | -41.6058 | 2025-06-17 04:06:00 | NOAA-21 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 0.6 |
| bd136537-12e8-35ed-9aa9-12a33ee515fe | -4.00051 | -43.23907 | 2025-06-17 04:06:00 | NOAA-21 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 5cc472a1-5dea-3b1e-b6f0-2fce8097e39d | -4.59879 | -38.53839 | 2025-06-17 04:06:00 | NOAA-21 | OCARA | CEARÁ | Brasil | 2309458 | 23 | 33 | nan | nan | nan | Caatinga | 1.2 |
| fb64123e-c164-3918-a238-b3a42a0304e9 | -3.76921 | -41.60529 | 2025-06-17 04:06:00 | NOAA-21 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 12d1c648-e4d6-3ee0-ab71-3d9ff8b38aaa | -3.77582 | -41.60632 | 2025-06-17 04:06:00 | NOAA-21 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 50b772d6-8924-3423-9f3f-543b000b88d8 | -4.89145 | -37.5305 | 2025-06-17 04:06:00 | NOAA-21 | ARACATI | CEARÁ | Brasil | 2301109 | 23 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 6e17addd-e666-3ef4-88d3-6bacb67a11cc | -4.89211 | -37.52605 | 2025-06-17 04:06:00 | NOAA-21 | ARACATI | CEARÁ | Brasil | 2301109 | 23 | 33 | nan | nan | nan | Caatinga | 5.1 |
| ff856449-c6f9-3d41-ae84-3e1aac04c3dd | -3.10966 | -47.48775 | 2025-06-17 04:06:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| b4cf2825-c7c8-3266-8d62-4651ea2cd4aa | -4.13718 | -43.06516 | 2025-06-17 04:06:00 | NOAA-21 | COELHO NETO | MARANHÃO | Brasil | 2103406 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 82a3a6b1-b2ee-3c11-916e-b1744bfe67dd | -2.4521 | -47.50417 | 2025-06-17 04:06:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 0f9a627d-a20b-3f48-ad73-0d35d1c4caf2 | -4.22971 | -43.01504 | 2025-06-17 04:06:00 | NOAA-21 | COELHO NETO | MARANHÃO | Brasil | 2103406 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 5176edc8-668a-3671-b23f-a1f346a5d729 | -6.12266 | -42.52664 | 2025-06-17 04:08:00 | NOAA-21 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 3c6860eb-6a45-3d90-be7e-7a107ff53fa7 | -9.2024 | -45.34418 | 2025-06-17 04:08:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| a47fd4b0-5f7d-3913-9de0-fead4fc46cb1 | -7.25977 | -44.61665 | 2025-06-17 04:08:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| be46092c-9c3a-347c-b742-f259eea1a85e | -7.97615 | -45.94722 | 2025-06-17 04:08:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 088f7d87-1b00-3d89-8d10-da11cffaee1b | -9.41187 | -48.415 | 2025-06-17 04:08:00 | NOAA-21 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 84a74732-8f50-3d5b-a15e-6876a048ab76 | -6.1221 | -42.53016 | 2025-06-17 04:08:00 | NOAA-21 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 7224a934-5293-3177-8438-a99d17077ba5 | -9.20209 | -49.69624 | 2025-06-17 04:08:00 | NOAA-21 | ABREULÂNDIA | TOCANTINS | Brasil | 1700251 | 17 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 5453d372-b9f5-345a-a8f7-6eddf8aa2be6 | -7.24522 | -43.09037 | 2025-06-17 04:08:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 7.5 |
| cd0a1667-d900-392f-887e-a9600f7ceace | -6.22295 | -43.33486 | 2025-06-17 04:08:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| a038a58d-f73b-3150-b574-b2b42a80d587 | -7.98084 | -55.29445 | 2025-06-17 04:08:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 2b1024e5-5225-3d97-a35c-a5600159775b | -7.21609 | -35.78027 | 2025-06-17 04:08:00 | NOAA-21 | MASSARANDUBA | PARAÍBA | Brasil | 2509206 | 25 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 9c4bc500-0c91-30b8-8b1c-9e77869d59f5 | -10.60701 | -48.59121 | 2025-06-17 04:08:00 | NOAA-21 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| cb28829c-48c6-3b3f-9ecb-92adda5f543f | -7.23574 | -43.08521 | 2025-06-17 04:08:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 4.9 |
| a163214b-30a9-377d-80d0-73a7bcb1a061 | -10.59847 | -48.58983 | 2025-06-17 04:08:00 | NOAA-21 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 870814ce-f9e5-3db3-899e-57d68cfaea08 | -5.57126 | -45.20467 | 2025-06-17 04:08:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 9.3 |
| 3342f95a-6651-3269-b065-cf37493bf662 | -10.60278 | -48.59032 | 2025-06-17 04:08:00 | NOAA-21 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| b5414e11-d3b9-39db-af5d-609377c1b514 | -9.3337 | -47.83633 | 2025-06-17 04:08:00 | NOAA-21 | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 5cd8b24f-11df-334b-a248-4167b4e2cfcd | -6.22353 | -43.33122 | 2025-06-17 04:08:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| c36ca9e4-d417-3e18-815e-835421e7d6e0 | -7.14376 | -43.29498 | 2025-06-17 04:08:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 6440ac32-5a25-31b2-b376-4a5ab1e87a8a | -7.96562 | -45.94089 | 2025-06-17 04:08:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| bc907fac-bec4-3a14-ae95-0b34bfb0a072 | -9.39185 | -48.42847 | 2025-06-17 04:08:00 | NOAA-21 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 05e47abf-2e6d-3351-8a50-e2893bdc18a7 | -10.77722 | -44.69009 | 2025-06-17 04:08:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 0024e83a-083d-3285-acb1-3f37f591039b | -5.57199 | -45.2002 | 2025-06-17 04:08:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 08cf2853-762a-3b76-968e-772435db5d43 | -7.04588 | -43.42072 | 2025-06-17 04:08:00 | NOAA-21 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 7bd89581-e547-38e8-9279-20dbb87e1e9e | -6.84492 | -47.83874 | 2025-06-17 04:08:00 | NOAA-21 | DARCINÓPOLIS | TOCANTINS | Brasil | 1706506 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 6b62c432-35ed-3c17-8480-9ca577dac514 | -6.84125 | -42.80392 | 2025-06-17 04:08:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 2.8 |
| 9815f39b-d18f-3b3f-8f06-7a94c7307b53 | -6.29341 | -47.00255 | 2025-06-17 04:08:00 | NOAA-21 | SÃO JOÃO DO PARAÍSO | MARANHÃO | Brasil | 2111052 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| adc4d403-7ee5-39ef-9a40-704a973de010 | -9.67168 | -48.77407 | 2025-06-17 04:08:00 | NOAA-21 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| f25f2fcc-bc58-3428-af0a-cdb194ef4083 | -11.03313 | -44.65067 | 2025-06-17 04:08:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 2d645340-c650-3a6d-8cbc-26b235a64f6e | -10.98545 | -45.11079 | 2025-06-17 04:08:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| bb48a641-f7fc-34f6-bf48-41224ec9ec3b | -6.66843 | -43.1857 | 2025-06-17 04:08:00 | NOAA-21 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 9c525023-9b32-3db0-a6dd-ddab3811b281 | -7.20257 | -45.35203 | 2025-06-17 04:08:00 | NOAA-21 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| bb2138cd-2471-3bd6-9e19-65c7bd40df20 | -6.68304 | -43.18064 | 2025-06-17 04:08:00 | NOAA-21 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 2e4deced-a1ac-316d-b943-466e92ec9f58 | -6.6718 | -43.18623 | 2025-06-17 04:08:00 | NOAA-21 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 25aa16af-2ca4-33fe-8f67-3774f0f7a4e3 | -9.40688 | -48.4183 | 2025-06-17 04:08:00 | NOAA-21 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 3186b856-c45d-32c7-bd37-5bf2f4cd4a56 | -7.7239 | -55.14248 | 2025-06-17 04:08:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 4b548a93-4151-3ef7-944a-510aceb6184b | -7.27936 | -50.0066 | 2025-06-17 04:08:00 | NOAA-21 | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| b26059a8-82a9-3374-8bd9-a975ce583c36 | -9.41617 | -48.41577 | 2025-06-17 04:08:00 | NOAA-21 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| b396a566-6817-39f8-b6d7-21aedd611bd5 | -4.24942 | -47.58866 | 2025-06-17 04:08:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 0d2786d6-e710-33f5-bba6-1af74ba8ad1f | -7.18558 | -43.60414 | 2025-06-17 04:08:00 | NOAA-21 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 2.9 |
| d2a6d62d-7d9f-3a0d-b823-7873b23bb924 | -6.22967 | -44.65864 | 2025-06-17 04:08:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 360d88fd-2123-325d-a40b-8a155fb07720 | -8.54636 | -48.26304 | 2025-06-17 04:08:00 | NOAA-21 | TUPIRATINS | TOCANTINS | Brasil | 1721307 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| b149efc7-b2d1-30ea-93f5-d79f5ec2d0bd | -8.96132 | -47.97456 | 2025-06-17 04:08:00 | NOAA-21 | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| e2db6068-92a3-3b39-aa1c-1d3d59109217 | -7.23631 | -43.08164 | 2025-06-17 04:08:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 3.8 |


[Clique aqui para ver as próximas entradas](README6.md)
