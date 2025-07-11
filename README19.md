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

## Dados Diários - Página 19

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| ad21bd23-950b-369d-b4f8-54bb049b704b | -14.32188 | -57.59819 | 2025-07-11 04:59:00 | NOAA-21 | NOVA MARILÂNDIA | MATO GROSSO | Brasil | 5108857 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 7876919a-ab83-3fc2-9050-6d4cf0c206e5 | -10.57033 | -49.14529 | 2025-07-11 04:59:00 | NOAA-21 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 5eec261e-bc19-3f58-a7de-0f1a7a2fb910 | -10.6856 | -49.49531 | 2025-07-11 04:59:00 | NOAA-21 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 3f437e22-1303-3bcb-9347-5ab884a00062 | -12.57937 | -56.97742 | 2025-07-11 04:59:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 7e904754-db49-3c6b-9798-8c134a559e49 | -10.74143 | -49.84638 | 2025-07-11 04:59:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| ff6ded80-137f-3455-b2b7-3c9adf794d93 | -13.13775 | -47.29359 | 2025-07-11 04:59:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 30a4ac3b-0cf1-3058-a3cf-ef45d1016924 | -12.41819 | -43.49408 | 2025-07-11 04:59:00 | NOAA-21 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 037aba34-a26e-3736-be31-37650ffe5eb9 | -13.00021 | -46.28357 | 2025-07-11 04:59:00 | NOAA-21 | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 8da27022-2425-3dd1-90dc-5e968e6c85a5 | -10.8486 | -49.11974 | 2025-07-11 04:59:00 | NOAA-21 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 3db85388-f96e-3446-97cf-e322a290fa77 | -11.32113 | -55.21238 | 2025-07-11 04:59:00 | NOAA-21 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 1d8d5a5e-0e3f-3cea-bbcd-6f57b865a49f | -13.15439 | -47.28458 | 2025-07-11 04:59:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| a9e10a70-84e5-36ba-9c3e-82f2fdb97eb6 | -13.00539 | -47.82209 | 2025-07-11 04:59:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 50ea205e-5bd1-3a79-a13f-f7656a58115e | -11.32793 | -45.21775 | 2025-07-11 04:59:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 2b333b55-f30f-38d2-86a2-681faf3e8b80 | -13.17452 | -47.28935 | 2025-07-11 04:59:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 4f73c2c5-92c5-3dcc-b53c-9cb8201634c8 | -10.62522 | -48.68149 | 2025-07-11 04:59:00 | NOAA-21 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| e76a3f15-f9aa-3913-8c4f-02f2f9c6bd62 | -9.94793 | -64.95405 | 2025-07-11 04:59:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 3.0 |
| e1a65fcc-cc5c-3e69-a159-4d4e92a33536 | -12.9904 | -46.28585 | 2025-07-11 04:59:00 | NOAA-21 | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 9b19e89c-0c96-3d1c-a9d0-5c651c19e41d | -10.68614 | -49.49133 | 2025-07-11 04:59:00 | NOAA-21 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 2fa9d4cf-2c7e-3125-b938-4391a35e37c9 | -12.40415 | -45.35957 | 2025-07-11 04:59:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 94dc4ffe-55b0-3973-ad2f-92bd83d23586 | -9.96169 | -64.97174 | 2025-07-11 04:59:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 0cc262c9-9e7e-3704-b2f8-31d2652d94a0 | -11.57179 | -47.42672 | 2025-07-11 04:59:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| b67af751-2d88-322f-aa95-6e1601333e56 | -11.44572 | -45.12084 | 2025-07-11 04:59:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| d991b7c9-e4b8-33be-a013-d353e9d605f2 | -10.57092 | -49.14102 | 2025-07-11 04:59:00 | NOAA-21 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 6.9 |
| ec875193-80cc-3c97-b222-35329600aad4 | -14.43318 | -58.72172 | 2025-07-11 04:59:00 | NOAA-21 | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | 3.5 |
| b88ef6b4-dd3e-3849-9ef8-6b9d7607da0a | -11.57602 | -47.43312 | 2025-07-11 04:59:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| d9c26603-2373-3367-b7f7-2205c94487a5 | -9.70495 | -56.18563 | 2025-07-11 04:59:00 | NOAA-21 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 6.4 |
| acea1947-4783-34ec-9340-d9ee43994be5 | -11.8416 | -47.50459 | 2025-07-11 04:59:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 56d89044-1242-3064-94c2-e833e3ec2970 | -14.05899 | -46.25091 | 2025-07-11 04:59:00 | NOAA-21 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| dd4a2a25-6a10-3fd1-b6ca-a872944339aa | -10.87271 | -54.05928 | 2025-07-11 04:59:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 24ee53b1-1929-340e-bba0-88b5a0612254 | -10.97453 | -58.66619 | 2025-07-11 04:59:00 | NOAA-21 | CASTANHEIRA | MATO GROSSO | Brasil | 5102850 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 33ec69e3-e727-3e5f-a2db-7615a0f6cd3d | -12.57995 | -56.97382 | 2025-07-11 04:59:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 6c5f6f87-e587-3ee7-902c-87152e679c45 | -10.6819 | -49.49075 | 2025-07-11 04:59:00 | NOAA-21 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 19.3 |
| 378b9f66-1e8b-39a9-80af-b749a459d486 | -10.57464 | -49.146 | 2025-07-11 04:59:00 | NOAA-21 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 2e9031e7-9808-3645-a28b-b74692ec49e4 | -9.86839 | -63.30231 | 2025-07-11 04:59:00 | NOAA-21 | ARIQUEMES | RONDÔNIA | Brasil | 1100023 | 11 | 33 | nan | nan | nan | Amazônia | 1.9 |
| b289a07a-13e6-3df4-9078-9c62772dc4db | -12.02347 | -49.52425 | 2025-07-11 04:59:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| d3a21120-3ef8-3434-b89d-38c206644f2d | -12.09638 | -64.24976 | 2025-07-11 04:59:00 | NOAA-21 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 87d82f4f-6723-3223-8e01-73f8341463bb | -9.9404 | -64.96394 | 2025-07-11 04:59:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 3172e1cf-0bf0-3aad-a5c4-cf8aa4fbbce7 | -14.05946 | -46.24895 | 2025-07-11 04:59:00 | NOAA-21 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| d64287af-04e8-30c9-89d7-791f32b8acbb | -12.05645 | -48.5437 | 2025-07-11 04:59:00 | NOAA-21 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| b345e01c-c44f-399a-8384-05195c83338d | -12.98999 | -46.28937 | 2025-07-11 04:59:00 | NOAA-21 | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| df7a1558-18ef-3ef5-ad6c-42260212e6c5 | -11.32168 | -55.20888 | 2025-07-11 04:59:00 | NOAA-21 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 86cb1c53-7663-32fc-8c2c-39e866726a79 | -10.58338 | -49.12815 | 2025-07-11 04:59:00 | NOAA-21 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| cd0ba4b4-d063-30a6-b0e1-36dd2fddfbea | -11.32746 | -45.22172 | 2025-07-11 04:59:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| ef75f95d-9ef1-3aa2-ad0b-4754a606b860 | -11.85067 | -46.7571 | 2025-07-11 04:59:00 | NOAA-21 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 5b846622-9e35-3386-9252-dd565a01fc7f | -13.16897 | -47.29224 | 2025-07-11 04:59:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 8566ff8d-c3a6-31e6-99c6-293e4afb394f | -12.99564 | -46.27576 | 2025-07-11 04:59:00 | NOAA-21 | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 7.0 |
| 5ae425de-8e09-3120-b220-bcef3b23df19 | -10.85352 | -49.11618 | 2025-07-11 04:59:00 | NOAA-21 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 7.7 |
| ceaa7a7c-faac-3249-8de8-69fd277423c5 | -10.6782 | -49.48618 | 2025-07-11 04:59:00 | NOAA-21 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 19.3 |
| 2ab88d4f-014f-3854-9822-bb0c03d417af | -11.84232 | -47.49895 | 2025-07-11 04:59:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| ece3e773-c90d-3e26-a49a-8c0a58644b36 | -10.84425 | -49.11908 | 2025-07-11 04:59:00 | NOAA-21 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 6.4 |
| e04053df-71f2-3655-b74b-35c4f9e68c96 | -11.43427 | -50.45556 | 2025-07-11 04:59:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 047bd72f-c3d3-3288-8b17-878d2774662f | -9.86561 | -60.29478 | 2025-07-11 04:59:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 6d102c45-4ca2-33bd-a20c-ebb6551f7387 | -11.78294 | -64.9828 | 2025-07-11 04:59:00 | NOAA-21 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d090034a-d22b-34f2-bb90-a4b76a5ed8d0 | -10.87217 | -54.06291 | 2025-07-11 04:59:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| ed10c9f7-270d-386d-b2e0-8ebb1f2d9681 | -13.16866 | -47.29478 | 2025-07-11 04:59:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 0fe4c14b-7141-32d5-8719-7db8f5116ad2 | -9.96305 | -64.96442 | 2025-07-11 04:59:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 3.8 |
| f83686f1-5883-352f-afa3-1645a05a8529 | -10.90371 | -49.2153 | 2025-07-11 04:59:00 | NOAA-21 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 2349edfe-0a6f-3c8c-a5a2-e9db2c620321 | -10.13253 | -57.78026 | 2025-07-11 04:59:00 | NOAA-21 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 75b27265-4913-369a-90e5-a36a3eb9057f | -11.37097 | -48.70751 | 2025-07-11 04:59:00 | NOAA-21 | ALIANÇA DO TOCANTINS | TOCANTINS | Brasil | 1700350 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| f7d7b62d-5b8d-31d4-949b-23a68fe9e84c | -12.99706 | -46.27602 | 2025-07-11 04:59:00 | NOAA-21 | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 66c3fe12-1958-3a0e-a92d-8702bc3d2570 | -10.67712 | -49.49419 | 2025-07-11 04:59:00 | NOAA-21 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 16.9 |
| fb6640ca-7391-3dc9-ab48-cd3b727bc4b7 | -9.6111 | -64.52621 | 2025-07-11 04:59:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 8d420b64-8bad-3b61-8f3d-fab5e5c21066 | -9.24568 | -58.76174 | 2025-07-11 04:59:00 | NOAA-21 | COTRIGUAÇU | MATO GROSSO | Brasil | 5103379 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| c503777f-af56-3412-beba-6fb26aa23b50 | -13.36619 | -47.88511 | 2025-07-11 04:59:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 2cacdc5d-09b9-3a18-adfb-f9cbb91b73ab | -12.99288 | -44.85857 | 2025-07-11 04:59:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| c783dbb2-e1b3-3833-93a0-ec0be70a249c | -12.57878 | -56.98104 | 2025-07-11 04:59:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 7916cfec-c056-3114-8794-ba3cd7e52c9e | -9.97017 | -64.95831 | 2025-07-11 04:59:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 117f0a2e-27b8-39d2-ae81-510aaacd24b0 | -13.00432 | -44.86438 | 2025-07-11 04:59:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| b7b18255-55f5-314f-a013-58aea1f2118b | -12.4099 | -45.36025 | 2025-07-11 04:59:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| bbb6d0b1-0ab4-3e84-bf50-9dd49ac86a56 | -11.93699 | -49.30272 | 2025-07-11 04:59:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 6fc69a46-fc57-3e83-b50f-af50316be018 | -10.57524 | -49.14172 | 2025-07-11 04:59:00 | NOAA-21 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 300a4aac-11b9-3f49-ba05-1ca35c1e8d83 | -11.88011 | -58.71556 | 2025-07-11 04:59:00 | NOAA-21 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 7accef34-0300-3d85-b79b-4e77829f7125 | -12.99667 | -46.27942 | 2025-07-11 04:59:00 | NOAA-21 | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 4.4 |
| f4e4c33e-8130-3800-9643-257c848f2674 | -12.09695 | -64.24676 | 2025-07-11 04:59:00 | NOAA-21 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 8ace0579-09a9-3de0-b916-07d91d6c98e5 | -11.4462 | -45.11678 | 2025-07-11 04:59:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| b657f113-0bcb-3675-a2c5-9949a265c863 | -12.99019 | -46.27509 | 2025-07-11 04:59:00 | NOAA-21 | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 56f0677c-cd5e-3b9f-889a-cb8b23fcfabc | -13.13226 | -47.29618 | 2025-07-11 04:59:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 9e4110d1-7af2-3e36-a0c4-063a37302eaf | -12.41879 | -43.4887 | 2025-07-11 04:59:00 | NOAA-21 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 3.7 |
| b7374e98-1b89-3ecf-809c-e64a7c089850 | -12.98846 | -46.28924 | 2025-07-11 04:59:00 | NOAA-21 | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| bc47c72b-59f2-355a-8511-57866d636999 | -11.8599 | -62.73645 | 2025-07-11 04:59:00 | NOAA-21 | SÃO MIGUEL DO GUAPORÉ | RONDÔNIA | Brasil | 1100320 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 01660656-57a1-3b2a-8b13-5fb66a3822d8 | -11.84726 | -47.4996 | 2025-07-11 04:59:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 253ff45d-4b36-3f48-a1dc-d55d363d5fda | -12.98889 | -46.28573 | 2025-07-11 04:59:00 | NOAA-21 | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| c658f4f4-747b-3398-9e6a-4bb0cebdf60e | -12.10257 | -64.24467 | 2025-07-11 04:59:00 | NOAA-21 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| fc4d5b19-a297-3216-abea-dc0b5b0851f8 | -10.5813 | -49.12988 | 2025-07-11 04:59:00 | NOAA-21 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 21.2 |
| 0bf798a2-388b-358e-8018-232fc1d091f3 | -11.33407 | -51.44354 | 2025-07-11 04:59:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 8273dd49-eb0d-3540-9771-d90faf774173 | -10.906 | -49.2175 | 2025-07-11 04:59:00 | NOAA-21 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| dea128a0-9186-3f73-a168-ca9bcb48b3d5 | -12.01916 | -49.52364 | 2025-07-11 04:59:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| e0f8758b-95fc-3b4b-b67e-663f75aa8dda | -13.36055 | -47.89049 | 2025-07-11 04:59:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 9.1 |
| 6ecb5fad-8ad6-3d29-89b7-04643498a5f2 | -12.02778 | -49.52486 | 2025-07-11 04:59:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| b4163bd4-ef1a-3f69-9a92-9f2c4362147f | -12.98588 | -44.86697 | 2025-07-11 04:59:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| db1cb3a6-64e3-3c0e-996e-5c5b37e08cfc | -10.57641 | -49.1333 | 2025-07-11 04:59:00 | NOAA-21 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 07f5b546-3a2f-3756-83f9-0f2479eab629 | -11.8794 | -58.71974 | 2025-07-11 04:59:00 | NOAA-21 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 4.3 |
| e3296d14-bcff-364f-8676-85653d9a9a59 | -14.05988 | -46.24543 | 2025-07-11 04:59:00 | NOAA-21 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 8a310e83-c156-3a3d-bdd0-21ad148d26cc | -13.35975 | -47.89708 | 2025-07-11 04:59:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 18e3248b-625b-339d-98b9-210c2c736cf8 | -10.90426 | -49.21111 | 2025-07-11 04:59:00 | NOAA-21 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 9846f71d-eaeb-3f9e-89e2-a54f510db8e0 | -13.00953 | -47.82874 | 2025-07-11 04:59:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 38557ad1-1a41-3dd8-86da-c055a566b807 | -12.99236 | -44.86319 | 2025-07-11 04:59:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 7d49596c-d45a-3565-879b-10a6f1d7421b | -12.99079 | -44.87706 | 2025-07-11 04:59:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 0c1d93d4-2aad-394e-a36a-d22fe4e76b0c | -13.13264 | -47.29306 | 2025-07-11 04:59:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 147bf215-2b59-37ec-9d0a-6f5753e93b91 | -13.13416 | -47.28056 | 2025-07-11 04:59:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |


[Clique aqui para ver as próximas entradas](README20.md)
