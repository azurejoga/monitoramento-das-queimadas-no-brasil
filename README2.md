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

## Dados Diários - Página 2

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 8fe07c30-1615-3af6-a3a7-130dd9a661ab | -10.52855 | -42.44468 | 2025-02-25 03:17:00 | NOAA-20 | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Caatinga | 2.2 |
| f7b25ed2-b30e-3c4a-b8a0-c218a4b96f7f | -9.75746 | -36.14263 | 2025-02-25 03:17:00 | NOAA-20 | SÃO MIGUEL DOS CAMPOS | ALAGOAS | Brasil | 2708600 | 27 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| dd661470-80fe-3abf-8879-696069f234a2 | -8.07019 | -34.97532 | 2025-02-25 03:17:00 | NOAA-20 | RECIFE | PERNAMBUCO | Brasil | 2611606 | 26 | 33 | nan | nan | nan | Mata Atlântica | 8.9 |
| 088145fe-1d2c-3813-83d8-7b60cff90d61 | -21.86873 | -43.07518 | 2025-02-25 03:19:00 | NOAA-20 | MAR DE ESPANHA | MINAS GERAIS | Brasil | 3139805 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 1fb167d4-87b3-3de0-8a71-2816b5c9e424 | -22.46185 | -42.66271 | 2025-02-25 03:19:00 | NOAA-20 | CACHOEIRAS DE MACACU | RIO DE JANEIRO | Brasil | 3300803 | 33 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 943c79a1-b33b-34b8-aac3-a6b43d49dfb9 | -22.89267 | -42.71696 | 2025-02-25 03:19:00 | NOAA-20 | MARICÁ | RIO DE JANEIRO | Brasil | 3302700 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 172a0035-9400-33c4-bcda-23b1097b640f | -22.46123 | -42.66548 | 2025-02-25 03:19:00 | NOAA-20 | CACHOEIRAS DE MACACU | RIO DE JANEIRO | Brasil | 3300803 | 33 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| bfb8ad31-a52f-3e75-b605-ec2b8bd41f1d | -21.86961 | -43.07538 | 2025-02-25 03:19:00 | NOAA-20 | MAR DE ESPANHA | MINAS GERAIS | Brasil | 3139805 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 4b282db8-7213-3b63-99d8-40730221873f | 2.7431 | -61.2813 | 2025-02-25 03:20:00 | GOES-16 | ALTO ALEGRE | RORAIMA | Brasil | 1400050 | 14 | 33 | nan | nan | nan | Amazônia | 121.0 |
| 4c101076-a97b-3fb2-9164-9daf9594c0c5 | -15.8955 | -43.4523 | 2025-02-25 03:20:00 | GOES-16 | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 98.0 |
| d2a911eb-92b5-3648-ad3d-48cb3c2d3fcc | 2.7432 | -61.2624 | 2025-02-25 03:20:00 | GOES-16 | ALTO ALEGRE | RORAIMA | Brasil | 1400050 | 14 | 33 | nan | nan | nan | Amazônia | 67.8 |
| 78a3181c-ad6e-3698-9f01-2af953dd818f | 2.7249 | -61.2816 | 2025-02-25 03:20:00 | GOES-16 | ALTO ALEGRE | RORAIMA | Brasil | 1400050 | 14 | 33 | nan | nan | nan | Amazônia | 114.4 |
| 0335bf61-96b8-3a12-bea8-196b30b76a08 | 2.7249 | -61.2627 | 2025-02-25 03:20:00 | GOES-16 | ALTO ALEGRE | RORAIMA | Brasil | 1400050 | 14 | 33 | nan | nan | nan | Amazônia | 62.7 |
| f16b4f0a-1ec7-302c-bf02-4c8ca91bec55 | 2.7249 | -61.2816 | 2025-02-25 03:30:00 | GOES-16 | ALTO ALEGRE | RORAIMA | Brasil | 1400050 | 14 | 33 | nan | nan | nan | Amazônia | 115.3 |
| e4044597-c590-3174-a9a8-d4745c6147ee | 2.7431 | -61.2813 | 2025-02-25 03:30:00 | GOES-16 | ALTO ALEGRE | RORAIMA | Brasil | 1400050 | 14 | 33 | nan | nan | nan | Amazônia | 99.2 |
| 053c2b43-a47f-31bd-88bc-2af4f40a4da0 | 2.7432 | -61.2624 | 2025-02-25 03:30:00 | GOES-16 | ALTO ALEGRE | RORAIMA | Brasil | 1400050 | 14 | 33 | nan | nan | nan | Amazônia | 55.7 |
| 5a9e18bf-2a35-3be2-b851-4eb223647a65 | 2.7249 | -61.2627 | 2025-02-25 03:30:00 | GOES-16 | ALTO ALEGRE | RORAIMA | Brasil | 1400050 | 14 | 33 | nan | nan | nan | Amazônia | 62.6 |
| 7af55910-15b2-3953-a15b-94752dd929d2 | -15.8955 | -43.4523 | 2025-02-25 03:30:00 | GOES-16 | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 107.0 |
| 69b7f41f-6845-38e3-92c1-78dc35cf2b9b | 2.7431 | -61.2813 | 2025-02-25 03:40:00 | GOES-16 | ALTO ALEGRE | RORAIMA | Brasil | 1400050 | 14 | 33 | nan | nan | nan | Amazônia | 69.0 |
| 24cf5c12-cefc-3a4f-b212-1cf4479b7331 | 2.7249 | -61.2816 | 2025-02-25 03:40:00 | GOES-16 | ALTO ALEGRE | RORAIMA | Brasil | 1400050 | 14 | 33 | nan | nan | nan | Amazônia | 102.1 |
| cdccd485-6e4d-3ea0-bd1f-aae17fa1f99a | -15.8955 | -43.4523 | 2025-02-25 03:40:00 | GOES-16 | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 161.9 |
| c640e056-0018-34f7-a0a9-40ba10db0f59 | 2.7432 | -61.2624 | 2025-02-25 03:40:00 | GOES-16 | ALTO ALEGRE | RORAIMA | Brasil | 1400050 | 14 | 33 | nan | nan | nan | Amazônia | 45.9 |
| f5f10cd3-e368-330f-a7bc-d4d67dc9f4e2 | 2.7249 | -61.2627 | 2025-02-25 03:40:00 | GOES-16 | ALTO ALEGRE | RORAIMA | Brasil | 1400050 | 14 | 33 | nan | nan | nan | Amazônia | 74.5 |
| fcb3f14f-23a7-362c-bc3e-d5b955d1f535 | 2.7249 | -61.2627 | 2025-02-25 03:50:00 | GOES-16 | ALTO ALEGRE | RORAIMA | Brasil | 1400050 | 14 | 33 | nan | nan | nan | Amazônia | 43.4 |
| ebf816b6-562f-3f71-a070-62d54133eaec | -15.8955 | -43.4523 | 2025-02-25 03:50:00 | GOES-16 | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 150.5 |
| ab2a4910-3323-340a-b2e9-33c0189c73cf | 2.7431 | -61.2813 | 2025-02-25 03:50:00 | GOES-16 | ALTO ALEGRE | RORAIMA | Brasil | 1400050 | 14 | 33 | nan | nan | nan | Amazônia | 60.9 |
| e145d04f-82e5-3c7d-80b9-2cd7938db6ab | 2.7249 | -61.2816 | 2025-02-25 03:50:00 | GOES-16 | ALTO ALEGRE | RORAIMA | Brasil | 1400050 | 14 | 33 | nan | nan | nan | Amazônia | 86.6 |
| 7488ffd7-0ae3-315d-9479-e413e2c5613f | -15.8949 | -43.4766 | 2025-02-25 04:00:00 | GOES-16 | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 80.6 |
| 4d1875bc-dfb5-37e8-bf0b-a10a5f04a93d | 2.7249 | -61.2627 | 2025-02-25 04:00:00 | GOES-16 | ALTO ALEGRE | RORAIMA | Brasil | 1400050 | 14 | 33 | nan | nan | nan | Amazônia | 63.0 |
| b9d408f2-d6db-3263-a437-0a77a9d88b74 | 2.7432 | -61.2624 | 2025-02-25 04:00:00 | GOES-16 | ALTO ALEGRE | RORAIMA | Brasil | 1400050 | 14 | 33 | nan | nan | nan | Amazônia | 41.6 |
| da2c0448-08ec-34cb-87e1-9709e784fb77 | 2.7249 | -61.2816 | 2025-02-25 04:00:00 | GOES-16 | ALTO ALEGRE | RORAIMA | Brasil | 1400050 | 14 | 33 | nan | nan | nan | Amazônia | 116.6 |
| 1edd528f-fb63-3b63-b7f9-c366c31b4265 | -15.8955 | -43.4523 | 2025-02-25 04:00:00 | GOES-16 | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 150.4 |
| 3a0d26d7-91fa-3e9c-a8a8-435c0a3ac546 | 2.7431 | -61.2813 | 2025-02-25 04:00:00 | GOES-16 | ALTO ALEGRE | RORAIMA | Brasil | 1400050 | 14 | 33 | nan | nan | nan | Amazônia | 84.9 |
| f9e913b7-5be7-35f6-a2c1-e3b0e8029fd7 | -5.1928 | -35.76269 | 2025-02-25 04:06:00 | NOAA-21 | SÃO MIGUEL DO GOSTOSO | RIO GRANDE DO NORTE | Brasil | 2412559 | 24 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 4a10c249-4635-319a-8a8b-9076ff51f127 | -5.19335 | -35.75893 | 2025-02-25 04:06:00 | NOAA-21 | SÃO MIGUEL DO GOSTOSO | RIO GRANDE DO NORTE | Brasil | 2412559 | 24 | 33 | nan | nan | nan | Caatinga | 0.9 |
| edbb96e4-0478-309f-a952-bc22340ebbfa | -5.25162 | -36.31608 | 2025-02-25 04:06:00 | NOAA-21 | GUAMARÉ | RIO GRANDE DO NORTE | Brasil | 2404507 | 24 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 51348392-5a98-3026-bba2-aef8e09edbf4 | -5.24762 | -36.31546 | 2025-02-25 04:06:00 | NOAA-21 | GUAMARÉ | RIO GRANDE DO NORTE | Brasil | 2404507 | 24 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 17ab8f47-13fa-3d25-9bf4-8cb4354f1519 | -8.07153 | -34.97882 | 2025-02-25 04:08:00 | NOAA-21 | RECIFE | PERNAMBUCO | Brasil | 2611606 | 26 | 33 | nan | nan | nan | Mata Atlântica | 6.1 |
| 3dd74282-abeb-39a2-8297-a920e1734f73 | -9.40777 | -40.31277 | 2025-02-25 04:08:00 | NOAA-21 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 13.1 |
| f29f23d3-9978-3f2e-8251-74aa093554ce | -8.37654 | -43.96992 | 2025-02-25 04:08:00 | NOAA-21 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| bb28f664-c132-3402-b215-a42c50685daa | -8.94432 | -44.2387 | 2025-02-25 04:08:00 | NOAA-21 | SANTA LUZ | PIAUÍ | Brasil | 2209302 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| b882f542-1ad8-334e-92d2-dcdb2352f225 | -8.9437 | -44.24249 | 2025-02-25 04:08:00 | NOAA-21 | SANTA LUZ | PIAUÍ | Brasil | 2209302 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| c224b66a-cb0a-35f2-89c3-31fb26bbf1bd | -7.46984 | -35.15119 | 2025-02-25 04:08:00 | NOAA-21 | ITAMBÉ | PERNAMBUCO | Brasil | 2607653 | 26 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 41e15f44-af78-3874-8057-59205ca4c5fb | -7.47216 | -35.15337 | 2025-02-25 04:08:00 | NOAA-21 | ITAMBÉ | PERNAMBUCO | Brasil | 2607653 | 26 | 33 | nan | nan | nan | Mata Atlântica | 3.1 |
| b3e173f0-623d-311f-a031-02429ab5e872 | -10.53278 | -42.43993 | 2025-02-25 04:08:00 | NOAA-21 | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 1c5bf8ec-958b-386a-bc5a-adeded1f2ae1 | -12.86077 | -38.36863 | 2025-02-25 04:08:00 | NOAA-21 | SALVADOR | BAHIA | Brasil | 2927408 | 29 | 33 | nan | nan | nan | Mata Atlântica | 3.9 |
| 158ed17e-6b8b-32ae-ab25-193a656b1965 | -10.52948 | -42.43941 | 2025-02-25 04:08:00 | NOAA-21 | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 86d63f0a-6d2f-3b8c-9db8-a370923e8884 | -9.25766 | -40.96106 | 2025-02-25 04:08:00 | NOAA-21 | CASA NOVA | BAHIA | Brasil | 2907202 | 29 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 3f5bece8-5154-3671-b88a-2f8f3139c6cd | -8.07218 | -34.9741 | 2025-02-25 04:08:00 | NOAA-21 | RECIFE | PERNAMBUCO | Brasil | 2611606 | 26 | 33 | nan | nan | nan | Mata Atlântica | 6.1 |
| bdf6d653-ff0a-314d-9ca3-1c46bafac8ae | -7.47276 | -35.14898 | 2025-02-25 04:08:00 | NOAA-21 | ITAMBÉ | PERNAMBUCO | Brasil | 2607653 | 26 | 33 | nan | nan | nan | Mata Atlântica | 3.0 |
| 16e56ed5-63be-3afc-aa1e-3cecee484ef1 | -8.40341 | -40.61739 | 2025-02-25 04:08:00 | NOAA-21 | DORMENTES | PERNAMBUCO | Brasil | 2605152 | 26 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 9481dec4-7299-37dc-a5f6-ef4c15d6b2d1 | -8.94089 | -44.23814 | 2025-02-25 04:08:00 | NOAA-21 | SANTA LUZ | PIAUÍ | Brasil | 2209302 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| a64a3932-9271-36b1-a9ad-181176ef3cd6 | -7.05785 | -44.35382 | 2025-02-25 04:08:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 36cd5cff-e304-3b5d-8627-456d036293f0 | -8.93745 | -44.23759 | 2025-02-25 04:08:00 | NOAA-21 | SANTA LUZ | PIAUÍ | Brasil | 2209302 | 22 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 834aeb7c-b978-3a10-9a25-6eb36e08f778 | -10.53386 | -42.43296 | 2025-02-25 04:08:00 | NOAA-21 | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 1bc67dcf-c538-3bce-8d1f-556d436b49cd | -7.08841 | -35.10754 | 2025-02-25 04:08:00 | NOAA-21 | CRUZ DO ESPÍRITO SANTO | PARAÍBA | Brasil | 2504900 | 25 | 33 | nan | nan | nan | Mata Atlântica | 2.7 |
| fee1cac2-e5af-3cac-bcad-c608d62fcdce | -8.11527 | -43.13876 | 2025-02-25 04:08:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 6.2 |
| 423eead2-2a97-3fd0-99af-8d987fe5c304 | -12.86064 | -38.36719 | 2025-02-25 04:08:00 | NOAA-21 | SALVADOR | BAHIA | Brasil | 2927408 | 29 | 33 | nan | nan | nan | Mata Atlântica | 3.6 |
| b7d4e503-5cc2-39d8-9834-8d329b79a811 | -8.94714 | -44.24304 | 2025-02-25 04:08:00 | NOAA-21 | SANTA LUZ | PIAUÍ | Brasil | 2209302 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 1d713729-55f8-3fc8-b62b-364ad554945b | -8.06696 | -34.97818 | 2025-02-25 04:08:00 | NOAA-21 | RECIFE | PERNAMBUCO | Brasil | 2611606 | 26 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| 3f9cd822-7261-3152-8344-cc7add1a8116 | -7.08777 | -35.1121 | 2025-02-25 04:08:00 | NOAA-21 | CRUZ DO ESPÍRITO SANTO | PARAÍBA | Brasil | 2504900 | 25 | 33 | nan | nan | nan | Mata Atlântica | 2.7 |
| 568b60c3-ee6a-3660-8d48-c2a6576c002a | -10.53332 | -42.43645 | 2025-02-25 04:08:00 | NOAA-21 | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 85292f62-b29e-3e3d-b27d-586c86ffd902 | -7.85194 | -34.83973 | 2025-02-25 04:08:00 | NOAA-21 | PAULISTA | PERNAMBUCO | Brasil | 2610707 | 26 | 33 | nan | nan | nan | Mata Atlântica | 5.0 |
| 40901826-b3b8-3aac-9fd5-ffbcc49fe750 | -7.09224 | -35.11268 | 2025-02-25 04:08:00 | NOAA-21 | CRUZ DO ESPÍRITO SANTO | PARAÍBA | Brasil | 2504900 | 25 | 33 | nan | nan | nan | Mata Atlântica | 4.7 |
| 280ab439-9cea-3a72-82dd-09c088e89122 | -8.06761 | -34.97342 | 2025-02-25 04:08:00 | NOAA-21 | RECIFE | PERNAMBUCO | Brasil | 2611606 | 26 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| 790cd226-8056-37a3-9a8c-94ceb3f797ad | -8.37312 | -43.96935 | 2025-02-25 04:08:00 | NOAA-21 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 942e51b1-2be5-3e40-8146-49b7642796fd | -7.47432 | -35.15186 | 2025-02-25 04:08:00 | NOAA-21 | ITAMBÉ | PERNAMBUCO | Brasil | 2607653 | 26 | 33 | nan | nan | nan | Mata Atlântica | 4.0 |
| a2c56187-afcd-3483-b66d-7239a386ad6b | -8.72709 | -44.01868 | 2025-02-25 04:08:00 | NOAA-21 | CRISTINO CASTRO | PIAUÍ | Brasil | 2203107 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 61ab6205-6647-395c-8244-9a09333e60ba | -8.1147 | -43.14233 | 2025-02-25 04:08:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 3.7 |
| d43471c3-b32c-30fc-a057-107c06468d2f | -8.68051 | -37.01963 | 2025-02-25 04:08:00 | NOAA-21 | BUÍQUE | PERNAMBUCO | Brasil | 2602803 | 26 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 4f56bb74-3a91-3ab2-9ce4-fb26ba6967fa | -8.14138 | -44.46165 | 2025-02-25 04:08:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 5d87c417-fb7a-36f2-bade-51a96a5755db | -7.45985 | -38.77126 | 2025-02-25 04:08:00 | NOAA-21 | MAURITI | CEARÁ | Brasil | 2308104 | 23 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 054aa538-c9ee-3f16-a7bb-91b91b28ccaa | -7.09289 | -35.10809 | 2025-02-25 04:08:00 | NOAA-21 | CRUZ DO ESPÍRITO SANTO | PARAÍBA | Brasil | 2504900 | 25 | 33 | nan | nan | nan | Mata Atlântica | 4.7 |
| 8d514ed1-2242-3894-85ed-2f3840575880 | 2.7249 | -61.2816 | 2025-02-25 04:10:00 | GOES-16 | ALTO ALEGRE | RORAIMA | Brasil | 1400050 | 14 | 33 | nan | nan | nan | Amazônia | 102.8 |
| 75db8316-0118-3792-aaad-e4ea4477fb04 | 2.7249 | -61.2627 | 2025-02-25 04:10:00 | GOES-16 | ALTO ALEGRE | RORAIMA | Brasil | 1400050 | 14 | 33 | nan | nan | nan | Amazônia | 46.2 |
| 35230bc2-d465-3c7e-8996-ee65adc90607 | 2.7432 | -61.2624 | 2025-02-25 04:10:00 | GOES-16 | ALTO ALEGRE | RORAIMA | Brasil | 1400050 | 14 | 33 | nan | nan | nan | Amazônia | 41.6 |
| 43fde271-caa5-3faa-88b1-0d359b5beb6d | -15.8949 | -43.4766 | 2025-02-25 04:10:00 | GOES-16 | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 67.7 |
| 149c03e2-ef61-3c34-a47a-d3454a1018dd | -15.8955 | -43.4523 | 2025-02-25 04:10:00 | GOES-16 | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 149.3 |
| ae8d69ae-c7ba-3da8-81d9-2ed311386b7d | 2.7431 | -61.2813 | 2025-02-25 04:10:00 | GOES-16 | ALTO ALEGRE | RORAIMA | Brasil | 1400050 | 14 | 33 | nan | nan | nan | Amazônia | 78.8 |
| 4b221d73-b3c8-3fd2-92cd-8bc7a7c524fa | -12.56011 | -44.72298 | 2025-02-25 04:10:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 2a93ca09-1a7c-3aa7-9d15-fad8e51c0606 | -18.11638 | -39.68765 | 2025-02-25 04:10:00 | NOAA-21 | MUCURI | BAHIA | Brasil | 2922003 | 29 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| 299f9746-ca0e-34f9-8a19-f661b3ab7e40 | -17.77998 | -42.806 | 2025-02-25 04:10:00 | NOAA-21 | ITAMARANDIBA | MINAS GERAIS | Brasil | 3132503 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 1b2e9515-b6c5-3ea5-bcf0-ab807afd4848 | -17.67767 | -42.73964 | 2025-02-25 04:10:00 | NOAA-21 | ITAMARANDIBA | MINAS GERAIS | Brasil | 3132503 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| dfba66d4-7baa-3449-b308-c0207de405b2 | -15.89404 | -43.45677 | 2025-02-25 04:10:00 | NOAA-21 | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 14.5 |
| 8c54febb-7fcf-3caf-bf08-185a18ba95ae | -15.5556 | -46.27818 | 2025-02-25 04:10:00 | NOAA-21 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| fd94d629-2873-30cf-9abc-e235bddd40e9 | -15.89349 | -43.46034 | 2025-02-25 04:10:00 | NOAA-21 | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 14.5 |
| bf90fb8e-1c37-397c-8c38-dd84e1297835 | -12.55685 | -44.73804 | 2025-02-25 04:10:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 550bd69a-ad35-3bff-acc0-9b6a2be8f27a | -12.55346 | -44.73748 | 2025-02-25 04:10:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 88d1a1a3-39e3-3e62-915d-c679c60b703b | -12.55765 | -44.73789 | 2025-02-25 04:10:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 8ea1c3d6-fc6c-3d51-a438-0f4157e02745 | -17.633 | -42.11122 | 2025-02-25 04:10:00 | NOAA-21 | SETUBINHA | MINAS GERAIS | Brasil | 3165552 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 5d18045f-84a1-3cc0-82b7-276f543f1c5d | -16.57421 | -41.44481 | 2025-02-25 04:10:00 | NOAA-21 | ITAOBIM | MINAS GERAIS | Brasil | 3133303 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| 6350bafb-95a0-3b3f-8e29-b12b5092b431 | -12.55704 | -44.74162 | 2025-02-25 04:10:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| f4f56190-9e04-3624-b6b3-dd5266dbc920 | -19.62848 | -44.01844 | 2025-02-25 04:10:00 | NOAA-21 | PEDRO LEOPOLDO | MINAS GERAIS | Brasil | 3149309 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 61e86d0c-32f4-3b1c-b21c-61078a85f7f6 | -14.19848 | -44.3054 | 2025-02-25 04:10:00 | NOAA-21 | FEIRA DA MATA | BAHIA | Brasil | 2910776 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| eb9f15f4-59de-3708-8f7d-35ca832d8c97 | -13.29596 | -44.62511 | 2025-02-25 04:10:00 | NOAA-21 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 2d01020a-7f8d-3c52-94a2-ab2db3759209 | -12.55247 | -44.72197 | 2025-02-25 04:10:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 08f55b60-deda-37fe-a1af-9fcd8861e306 | -14.04137 | -41.45621 | 2025-02-25 04:10:00 | NOAA-21 | BRUMADO | BAHIA | Brasil | 2904605 | 29 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 91b2d1f7-50ed-3802-918f-68a96d257954 | -18.63642 | -42.77108 | 2025-02-25 04:10:00 | NOAA-21 | GUANHÃES | MINAS GERAIS | Brasil | 3128006 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.4 |
| dd99d526-92fa-394d-9aac-4f441def5f35 | -18.03372 | -39.73557 | 2025-02-25 04:10:00 | NOAA-21 | MUCURI | BAHIA | Brasil | 2922003 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| f3930dc3-0048-3f6f-a07c-d60fa7b43a86 | -19.41146 | -43.94862 | 2025-02-25 04:10:00 | NOAA-21 | BALDIM | MINAS GERAIS | Brasil | 3105004 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |


[Clique aqui para ver as próximas entradas](README3.md)
