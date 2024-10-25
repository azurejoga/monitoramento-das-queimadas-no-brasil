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

## Dados Diários - Página 30

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| ec89ccac-23fc-3b91-b078-15ec27ce5689 | -7.18762 | -46.96059 | 2024-10-25 04:14:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 5dc74d30-6685-3395-9a4c-8aec32e60966 | -7.18689 | -46.96497 | 2024-10-25 04:14:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 1fc57501-688e-3ab1-afc9-29d8b42bcb87 | -7.13548 | -47.06707 | 2024-10-25 04:14:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 2ac7346f-a0fb-3ee7-9bd6-51b3441da5dc | -7.1209 | -47.19962 | 2024-10-25 04:14:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| dfcd4278-8d30-377e-ac29-843d274d2b0d | -6.99266 | -47.38491 | 2024-10-25 04:14:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 91eca05a-c7ae-37c6-9528-670550acb73e | -6.85195 | -48.26823 | 2024-10-25 04:14:00 | NOAA-21 | PIRAQUÊ | TOCANTINS | Brasil | 1717206 | 17 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 114a8c08-d24f-303a-9665-27cb7638a410 | -6.84793 | -48.26752 | 2024-10-25 04:14:00 | NOAA-21 | PIRAQUÊ | TOCANTINS | Brasil | 1717206 | 17 | 33 | nan | nan | nan | Amazônia | 1.4 |
| dba41e9e-24b3-3e19-8284-06112e1e81c0 | -6.66866 | -47.11121 | 2024-10-25 04:14:00 | NOAA-21 | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 14e70ea5-5c47-38f7-988c-c8ef4037532a | -6.54074 | -48.05655 | 2024-10-25 04:14:00 | NOAA-21 | RIACHINHO | TOCANTINS | Brasil | 1718550 | 17 | 33 | nan | nan | nan | Amazônia | 2.6 |
| eed6044f-87f1-3b2a-93b4-c32ef0c60218 | -7.25451 | -46.85342 | 2024-10-25 04:14:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| f75f9dcb-a43d-33d5-a9c7-a4e86edcce10 | -7.116 | -46.85039 | 2024-10-25 04:14:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| d50f1186-02fd-3cad-bb99-2b798662e2ed | -2.47816 | -48.49736 | 2024-10-25 04:14:00 | NOAA-21 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| c5a0e32e-c007-3c5a-816a-7da37fa23b32 | -2.01405 | -48.51697 | 2024-10-25 04:14:00 | NOAA-21 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 6dc0e308-c38a-3bf9-b71d-1e4e0df1dad9 | -2.00748 | -48.52931 | 2024-10-25 04:14:00 | NOAA-21 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 7.0 |
| 7c9034d6-5c13-3616-b627-3b3a5e2f433b | -2.00676 | -48.53365 | 2024-10-25 04:14:00 | NOAA-21 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| f413e578-d318-3cf5-968c-9a1a3dcc40bf | -1.60626 | -48.69865 | 2024-10-25 04:14:00 | NOAA-21 | BARCARENA | PARÁ | Brasil | 1501303 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| b1652d70-122e-35d3-b117-04048fecd3ac | -1.64178 | -47.74052 | 2024-10-25 04:14:00 | NOAA-21 | SÃO MIGUEL DO GUAMÁ | PARÁ | Brasil | 1507607 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 50ed1bef-fdb4-307d-bdd6-4e330a72361d | -1.5354 | -47.20403 | 2024-10-25 04:14:00 | NOAA-21 | OURÉM | PARÁ | Brasil | 1505403 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 59f3e864-b7ac-3354-a0d3-7edb5e451575 | -1.53191 | -47.19967 | 2024-10-25 04:14:00 | NOAA-21 | OURÉM | PARÁ | Brasil | 1505403 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 405474e6-e046-3c8d-a3e4-7a144c42de52 | -1.20072 | -47.59701 | 2024-10-25 04:14:00 | NOAA-21 | IGARAPÉ-AÇU | PARÁ | Brasil | 1503200 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| db977447-47c4-3983-ac02-da502156be07 | -1.20009 | -47.60092 | 2024-10-25 04:14:00 | NOAA-21 | IGARAPÉ-AÇU | PARÁ | Brasil | 1503200 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| faf6ae61-d4b2-370c-a475-bb49931079fd | -1.19946 | -47.60482 | 2024-10-25 04:14:00 | NOAA-21 | IGARAPÉ-AÇU | PARÁ | Brasil | 1503200 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e7c110fd-89eb-30d5-9f46-08d2b0d5c01c | -1.04549 | -47.61743 | 2024-10-25 04:14:00 | NOAA-21 | MARAPANIM | PARÁ | Brasil | 1504406 | 15 | 33 | nan | nan | nan | Amazônia | 8.2 |
| f5289917-5a9a-327d-b53f-834706df9b74 | -1.04488 | -47.62135 | 2024-10-25 04:14:00 | NOAA-21 | MARAPANIM | PARÁ | Brasil | 1504406 | 15 | 33 | nan | nan | nan | Amazônia | 14.8 |
| 5277fcad-e58b-358f-988d-1ac85d4a75f4 | -1.04126 | -47.61678 | 2024-10-25 04:14:00 | NOAA-21 | MARAPANIM | PARÁ | Brasil | 1504406 | 15 | 33 | nan | nan | nan | Amazônia | 8.2 |
| fa284b15-e3fc-3859-80c2-9031e214ec8f | -3.27334 | -48.46671 | 2024-10-25 04:14:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 8258c099-7df4-352d-b698-73a3f6842c9b | -3.26902 | -48.46597 | 2024-10-25 04:14:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| e3714d52-0c7b-398b-9adb-f13379f0f45e | -3.10148 | -48.66427 | 2024-10-25 04:14:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 9b3733e5-cb7f-3095-92d4-f22aac3862cb | -2.95133 | -48.61591 | 2024-10-25 04:14:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| c2fc67dc-5a93-315e-9a24-9204d3a1c112 | -2.95106 | -48.61599 | 2024-10-25 04:14:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| db91e685-3697-32ce-9c87-a1eef6e3e637 | -2.92176 | -48.95741 | 2024-10-25 04:14:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 17950df2-de6d-3568-851b-837f0334f62e | -2.87938 | -48.61336 | 2024-10-25 04:14:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 4e3b9df3-89da-339a-ab5c-d528b152eef3 | -2.6509 | -48.49242 | 2024-10-25 04:14:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 27b18e5c-a05a-3e62-95e5-fcd4ab33f392 | -2.65005 | -48.49268 | 2024-10-25 04:14:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 806affad-529f-3fa6-bb83-17052d6a3a4e | -2.43852 | -48.46488 | 2024-10-25 04:14:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 18.2 |
| 46b88985-141b-3c90-86c1-afe457e44bdc | -2.43782 | -48.46914 | 2024-10-25 04:14:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 18.2 |
| 1d5609dd-95f6-3e23-a661-cce48c60f32d | -2.43767 | -48.46622 | 2024-10-25 04:14:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 18.5 |
| 325cb1c7-54af-3f70-a22a-838e4bb1e1a9 | -2.437 | -48.47046 | 2024-10-25 04:14:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 18.5 |
| 3e8c9b9c-d81f-3e87-9380-29fc73e3a9a4 | -2.21011 | -48.84035 | 2024-10-25 04:14:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 56712564-20e3-373a-9639-0f5549cbbb93 | -2.19333 | -48.74545 | 2024-10-25 04:14:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 5e199f02-7ca9-3ebe-b5ae-05d809902b82 | -2.18884 | -48.74473 | 2024-10-25 04:14:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 8881252c-1dbb-3ace-8d1a-a7a2acf16455 | -3.46039 | -47.67044 | 2024-10-25 04:14:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 7.0 |
| 904472a2-7153-33e9-b77e-c30b38887a16 | -3.45978 | -47.67414 | 2024-10-25 04:14:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 6.7 |
| e3a690c4-ea19-3ee6-ae40-6fde894b18d7 | -3.07429 | -48.11432 | 2024-10-25 04:14:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c47567b9-96c5-3b90-ba86-aa736f122615 | -3.01289 | -48.09203 | 2024-10-25 04:14:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 8733c544-db5d-3047-85eb-cfedfa688ac3 | -3.00866 | -48.09137 | 2024-10-25 04:14:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 41e790e7-8337-39c1-9aeb-89a5bf3243bd | -3.00569 | -48.08285 | 2024-10-25 04:14:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| f86af0f5-8187-362b-9120-dd5b3b793799 | -2.96652 | -48.00452 | 2024-10-25 04:14:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 176e34ca-54d1-3e57-9f91-42c9cc415f87 | -2.96231 | -48.00386 | 2024-10-25 04:14:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 77f8e753-9b79-365f-a462-32fffbe71462 | -2.89496 | -48.28753 | 2024-10-25 04:14:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| dfced389-fe8e-3568-890b-5564a06368ef | -2.8926 | -48.27466 | 2024-10-25 04:14:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 8.8 |
| bb8f8d61-a913-3408-beab-3bcef775933d | -2.89196 | -48.27872 | 2024-10-25 04:14:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 7.3 |
| 56079d3a-c61a-39b3-bd3e-e16feb1b57f3 | -2.89066 | -48.28685 | 2024-10-25 04:14:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 8.4 |
| de509c24-41d1-36bd-bc1a-91767c435c3b | -2.89002 | -48.29088 | 2024-10-25 04:14:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 8.4 |
| 17804ac8-8ba8-3c55-834b-5402a7d711c6 | -2.88814 | -47.84673 | 2024-10-25 04:14:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 964f759b-3894-319b-b6e9-7fcc14956389 | -2.57957 | -48.14386 | 2024-10-25 04:14:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 97b91e36-7e47-3643-967b-65bf4b3e8895 | -2.55566 | -47.37714 | 2024-10-25 04:14:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 66cf151c-a913-31d4-a255-be78b757b62d | -2.5516 | -47.37646 | 2024-10-25 04:14:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 74573c36-aea7-3f88-bdf4-5afc279fc9ce | -4.58213 | -48.0123 | 2024-10-25 04:14:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 23.1 |
| b5f22db7-12c6-3e9c-8d17-2b15a75b1798 | -4.56897 | -48.02163 | 2024-10-25 04:14:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 7.1 |
| 64c3ab89-59f9-39cf-b696-5412214b543d | -4.56836 | -48.0254 | 2024-10-25 04:14:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 7.6 |
| f478bce5-d012-3b26-b8ca-e343e054b99f | -4.56314 | -48.00547 | 2024-10-25 04:14:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 90a29fe9-96ee-3912-9543-86a6a87a4019 | -4.56255 | -48.00916 | 2024-10-25 04:14:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 6.4 |
| 127d25f8-28e5-3ac9-a170-9cf7c892c0b4 | -4.55904 | -48.00481 | 2024-10-25 04:14:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 32516b9a-73c6-36e1-995d-8f74884a30b7 | -4.55844 | -48.0085 | 2024-10-25 04:14:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 6.4 |
| 6f13d3df-0df4-3b03-bbf3-12fffbfa5972 | -4.19144 | -47.77368 | 2024-10-25 04:14:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| ad9eef2f-2c7e-38ba-818d-734b3198f6ed | -4.19085 | -47.77724 | 2024-10-25 04:14:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 5da3556b-749b-37bb-a120-140cd81c1ead | -4.18675 | -47.77674 | 2024-10-25 04:14:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 73aa16c1-4445-3a18-808d-63fae0d161fe | -4.03957 | -47.95658 | 2024-10-25 04:14:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 2055f1ce-facb-3a55-88bf-3c5d9ffa6551 | -4.58624 | -48.01295 | 2024-10-25 04:14:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 23.1 |
| 2c7b54a7-ade0-3544-88f2-2193f537d208 | -4.58562 | -48.01665 | 2024-10-25 04:14:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 23.1 |
| 70a1241d-b106-3727-944b-c878a41c71b7 | -4.585 | -48.02036 | 2024-10-25 04:14:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 7.1 |
| f6134a0d-1f43-3ec8-b236-746977be28e4 | -4.58151 | -48.01598 | 2024-10-25 04:14:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 23.1 |
| 42226301-b12d-3cc5-8c89-ffa772737207 | -4.58089 | -48.01968 | 2024-10-25 04:14:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 7.1 |
| 854b60da-ee25-350a-bccf-a7c7fa295fad | -4.36604 | -48.60623 | 2024-10-25 04:14:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 89c02bbf-b686-32f4-bc13-dd2c677348a2 | -4.36404 | -48.60919 | 2024-10-25 04:14:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 1a7ec075-799c-370d-80e2-2a84cf4c1c2e | -4.34692 | -48.61553 | 2024-10-25 04:14:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 1f399ea6-2354-34ee-a571-c3853e582149 | -4.34262 | -48.61483 | 2024-10-25 04:14:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 9c2013e2-1a4b-3575-baa7-e208941003aa | -4.33865 | -48.63918 | 2024-10-25 04:14:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| b813b398-e2c1-3199-8bc4-c3d702860b54 | -4.33501 | -48.63441 | 2024-10-25 04:14:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 22.1 |
| 6294dc9a-0f22-39a9-811c-ae6f8c9ff70e | -4.33434 | -48.63853 | 2024-10-25 04:14:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 22.1 |
| 468aaa74-4235-30c9-877d-b153c4cfcad3 | -4.29335 | -48.61949 | 2024-10-25 04:14:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 5ca2cf90-1802-3201-a678-c6772b3031de | -4.26765 | -48.59881 | 2024-10-25 04:14:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 466dbb13-adf4-31a0-a82a-642d76fc5d40 | -4.26597 | -48.59865 | 2024-10-25 04:14:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 1f3b253b-4bce-3f55-b1c1-f12cccdf6aac | -4.25346 | -48.55047 | 2024-10-25 04:14:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| eee80004-537f-3e98-b6e6-807bcc411e15 | -4.2528 | -48.55457 | 2024-10-25 04:14:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| fa9e8be1-91bb-3a5b-8dbe-e20471bb358a | -4.2527 | -48.34167 | 2024-10-25 04:14:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 2620985c-d0f6-3b6f-a89c-3e8eca32a081 | -4.24918 | -48.54979 | 2024-10-25 04:14:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 11.0 |
| 0cd94158-28ef-309a-9314-6c363593bf81 | -4.24848 | -48.34101 | 2024-10-25 04:14:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 7.3 |
| 9e3d6b81-6d57-3a1c-a35e-b9b870c6538a | -4.24424 | -48.55313 | 2024-10-25 04:14:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 8.1 |
| 14de5182-7cb6-39e9-838c-e5971d081786 | -4.23996 | -48.55247 | 2024-10-25 04:14:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 19.8 |
| b2d3fc67-6db2-386b-b42e-fa552be8bbbf | -4.2393 | -48.55648 | 2024-10-25 04:14:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 19.8 |
| 3b573161-211f-3e33-9316-b76608e96bb6 | -4.22084 | -48.5618 | 2024-10-25 04:14:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 7ccaa8e9-b1cb-329b-8cc3-7c6bf9cac1f9 | -4.22016 | -48.56593 | 2024-10-25 04:14:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| b7ef96e6-a6be-3fb2-ad84-a7c3d9e69f97 | -4.19494 | -47.77773 | 2024-10-25 04:14:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| a21f5844-f644-3327-ae2f-c2e1d90c2ee8 | -4.18734 | -47.77322 | 2024-10-25 04:14:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| bab8be44-9f40-3e2d-be8f-0ca20c3e9414 | -4.14002 | -48.96983 | 2024-10-25 04:14:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| b2ebdc21-0e02-38bb-ab43-df8bd11cc654 | -4.13678 | -48.41298 | 2024-10-25 04:14:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 9.1 |
| 6f945096-b459-3bf7-af67-4c31f0833603 | -4.13253 | -48.41232 | 2024-10-25 04:14:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 9.1 |
| c9b2ee4b-83bf-3938-82b1-adca8233ad98 | -4.10004 | -48.23865 | 2024-10-25 04:14:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |


[Clique aqui para ver as próximas entradas](README31.md)
