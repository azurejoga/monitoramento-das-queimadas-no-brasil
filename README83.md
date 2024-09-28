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

## Dados Diários - Página 83

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| f63996c2-6b86-3f03-91be-d0a807a00614 | -8.51569 | -55.1936 | 2024-09-28 05:10:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 19169702-1861-32c8-a38b-63c8ac43605b | -8.51338 | -55.18524 | 2024-09-28 05:10:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| cf3976d7-c62f-3e12-a4ee-5378438be20e | -8.39995 | -55.02807 | 2024-09-28 05:10:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 97febd56-4219-3678-8cb9-8e6a9526abaa | -8.39703 | -55.02357 | 2024-09-28 05:10:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 1bed6ca1-3c7c-3e7c-89a2-499ba016e878 | -8.39643 | -55.02754 | 2024-09-28 05:10:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 55492300-324b-31fa-b7a4-bc594b6b6d6f | -8.3935 | -55.02303 | 2024-09-28 05:10:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 0e24b848-84f0-3f39-aa8b-760972dc8f6b | -8.33244 | -55.09453 | 2024-09-28 05:10:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 1e00ab29-9d73-3291-acab-d2b4a8d618a3 | -8.3121 | -55.01169 | 2024-09-28 05:10:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 166a0c5c-dd9b-3fd9-ad19-6af87fff9935 | -8.30918 | -55.0072 | 2024-09-28 05:10:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 74d84407-79cc-3fc9-8d40-18d4902c9fc7 | -8.30858 | -55.01114 | 2024-09-28 05:10:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f4cb506e-c9bf-3f35-ab01-79a91cd53a29 | -8.29587 | -55.38724 | 2024-09-28 05:10:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 7bdf52d7-d190-3888-83ae-01ab82469c52 | -8.29529 | -55.39106 | 2024-09-28 05:10:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 6e9e21b7-9725-31d5-80e7-b0c559908c8b | -8.2924 | -55.3867 | 2024-09-28 05:10:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 377711d1-024d-317a-b602-63ddee61bef5 | -8.29183 | -55.39053 | 2024-09-28 05:10:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 29b39cb1-ed9c-3dba-a67f-cb55b6935cfe | -9.69981 | -55.54344 | 2024-09-28 05:10:00 | NOAA-20 | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 17ed6d74-3429-3a40-85c8-3e30a9c75934 | -9.65857 | -55.58112 | 2024-09-28 05:10:00 | NOAA-20 | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 6f242504-e72e-320c-8d1d-f469ea520e1a | -9.65566 | -55.57668 | 2024-09-28 05:10:00 | NOAA-20 | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 85290e66-2115-3cd0-a22d-1ea0a6bcad3b | -9.65399 | -55.57689 | 2024-09-28 05:10:00 | NOAA-20 | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 47fb022e-4234-3368-8465-79850eec8300 | -9.54476 | -55.97036 | 2024-09-28 05:10:00 | NOAA-20 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 5a472f4a-99c0-3d34-9cdb-540560f01ba8 | -9.54133 | -55.96983 | 2024-09-28 05:10:00 | NOAA-20 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e72a773b-af50-3bb3-8fff-0af7d987cbbe | -13.76745 | -56.47039 | 2024-09-28 05:10:00 | NOAA-20 | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 0a6ef8ef-7d34-36ea-9f93-f5183b9f54c3 | -13.50405 | -57.25637 | 2024-09-28 05:10:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 3dab5cec-ad09-344b-b6b8-5c72be133ec4 | -13.49501 | -57.24734 | 2024-09-28 05:10:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| e4bb33d4-1515-3c85-b32a-ec66857636b2 | -13.49445 | -57.25106 | 2024-09-28 05:10:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 5ee7d022-121b-3bb2-a942-c5bc89023aa0 | -13.49389 | -57.25478 | 2024-09-28 05:10:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 671ff203-91f8-3846-bb3a-81f767d96de9 | -13.49332 | -57.25848 | 2024-09-28 05:10:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 74000b32-fa8e-32bf-955a-19600c3b875b | -13.49106 | -57.25052 | 2024-09-28 05:10:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 1c9fb444-6af0-38e2-abf0-3c5994f566b4 | -13.4905 | -57.25424 | 2024-09-28 05:10:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 5c63b257-7b0d-3fc1-800b-03947669c349 | -13.48994 | -57.25794 | 2024-09-28 05:10:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 3.8 |
| a5936c2e-04de-30c0-90fc-ba4aedfae8e2 | -13.48768 | -57.24998 | 2024-09-28 05:10:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 6b643a52-8752-3f3d-b761-39c78ea1aab5 | -13.48711 | -57.2537 | 2024-09-28 05:10:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| f9044b0d-85d2-3440-b331-ea8a49ff4ac6 | -13.28784 | -56.73816 | 2024-09-28 05:10:00 | NOAA-20 | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 5ffe8d88-03a6-3a91-bad5-6b4ea81ea10e | -13.02936 | -57.31929 | 2024-09-28 05:10:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 0001a2a0-3ee8-3786-af1f-89ad9de11d4f | -13.01361 | -57.3093 | 2024-09-28 05:10:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 4fe4cf0a-1932-38db-9c72-ff9e156d1875 | -13.00577 | -55.97381 | 2024-09-28 05:10:00 | NOAA-20 | LUCAS DO RIO VERDE | MATO GROSSO | Brasil | 5105259 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 7384fd25-e949-330f-82b6-32a05a4e78df | -13.9596 | -56.16633 | 2024-09-28 05:10:00 | NOAA-20 | NOVA MUTUM | MATO GROSSO | Brasil | 5106224 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 72dd99bd-f408-3f21-b0f6-36bcbe3d1845 | -13.95132 | -56.14853 | 2024-09-28 05:10:00 | NOAA-20 | NOVA MUTUM | MATO GROSSO | Brasil | 5106224 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 67813c46-d8a3-37b2-a93a-1636f448608c | -13.94837 | -56.14394 | 2024-09-28 05:10:00 | NOAA-20 | NOVA MUTUM | MATO GROSSO | Brasil | 5106224 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 5cc5b92e-a64c-3e30-a813-c9f0ef419811 | -13.94778 | -56.14801 | 2024-09-28 05:10:00 | NOAA-20 | NOVA MUTUM | MATO GROSSO | Brasil | 5106224 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 989049b8-fdae-3bb9-84c2-20832321be01 | -13.94482 | -56.1434 | 2024-09-28 05:10:00 | NOAA-20 | NOVA MUTUM | MATO GROSSO | Brasil | 5106224 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| e9d15010-0662-3eab-b537-80c05b023777 | -13.78314 | -56.50943 | 2024-09-28 05:10:00 | NOAA-20 | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| beca2a6f-0134-36cc-95ef-a04328bba22e | -13.77385 | -56.4999 | 2024-09-28 05:10:00 | NOAA-20 | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| c96941e4-7618-399d-b5b0-e144d0064133 | -13.77036 | -56.49939 | 2024-09-28 05:10:00 | NOAA-20 | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 9c208fcf-5185-368b-98f5-68c98509519a | -13.76978 | -56.50336 | 2024-09-28 05:10:00 | NOAA-20 | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 5b5f7bad-41f4-39e2-9917-bbe3a4e990f4 | -13.7663 | -56.50283 | 2024-09-28 05:10:00 | NOAA-20 | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| f356c033-caf7-383f-80f4-918c4e055885 | -15.61852 | -57.48112 | 2024-09-28 05:10:00 | NOAA-20 | BARRA DO BUGRES | MATO GROSSO | Brasil | 5101704 | 51 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 6df8b0b9-10fe-35dc-922a-175e33434e98 | -15.61796 | -57.48493 | 2024-09-28 05:10:00 | NOAA-20 | BARRA DO BUGRES | MATO GROSSO | Brasil | 5101704 | 51 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 66f2c261-517f-346d-9fa5-c08dc2f193ac | -15.61511 | -57.48058 | 2024-09-28 05:10:00 | NOAA-20 | BARRA DO BUGRES | MATO GROSSO | Brasil | 5101704 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| bbf07e1e-0dea-35aa-b152-260d41aedd13 | -15.61226 | -57.47623 | 2024-09-28 05:10:00 | NOAA-20 | BARRA DO BUGRES | MATO GROSSO | Brasil | 5101704 | 51 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 2ee971f6-6a91-3939-82fc-888c2a985ff9 | -15.61169 | -57.48005 | 2024-09-28 05:10:00 | NOAA-20 | BARRA DO BUGRES | MATO GROSSO | Brasil | 5101704 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| e12485ae-8d6a-31ac-93c5-60100f468897 | -15.61128 | -56.96584 | 2024-09-28 05:10:00 | NOAA-20 | NOSSA SENHORA DO LIVRAMENTO | MATO GROSSO | Brasil | 5106109 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 282a28ab-d284-3e4c-b9c2-f36dcd0b5ffb | -15.60884 | -57.47569 | 2024-09-28 05:10:00 | NOAA-20 | BARRA DO BUGRES | MATO GROSSO | Brasil | 5101704 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| dd8a8a7a-7f0b-3e6a-931b-bd2abbdd6466 | -15.60779 | -56.96535 | 2024-09-28 05:10:00 | NOAA-20 | NOSSA SENHORA DO LIVRAMENTO | MATO GROSSO | Brasil | 5106109 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 218ce2f3-781d-314f-a152-3ce423c9b266 | -15.60601 | -57.49476 | 2024-09-28 05:10:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 684e4210-6b34-34c1-9519-8fea0938cef3 | -15.60599 | -57.47134 | 2024-09-28 05:10:00 | NOAA-20 | BARRA DO BUGRES | MATO GROSSO | Brasil | 5101704 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 3eb5b842-1e20-3838-aecf-a6e2cae4cbeb | -15.60544 | -57.4986 | 2024-09-28 05:10:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| ecc9e08f-42b6-362e-a12c-73459e0efd76 | -15.60543 | -57.47514 | 2024-09-28 05:10:00 | NOAA-20 | BARRA DO BUGRES | MATO GROSSO | Brasil | 5101704 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 5248fe56-6a18-35dc-aa99-1050edf4667f | -15.60373 | -56.96877 | 2024-09-28 05:10:00 | NOAA-20 | NOSSA SENHORA DO LIVRAMENTO | MATO GROSSO | Brasil | 5106109 | 51 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 2ab7e664-bc44-3ece-8f21-fe80b74dd658 | -15.60316 | -57.49041 | 2024-09-28 05:10:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| f73cf045-e3ad-32ba-8ce5-2a0cc3adef88 | -15.60258 | -57.47079 | 2024-09-28 05:10:00 | NOAA-20 | BARRA DO BUGRES | MATO GROSSO | Brasil | 5101704 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 908ec717-25ee-3ec1-ad17-5bd4dd9aa3c1 | -15.60202 | -57.49806 | 2024-09-28 05:10:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 8fecc332-66d6-3a1e-a9a8-d8d5e2f5aac6 | -15.60201 | -57.47461 | 2024-09-28 05:10:00 | NOAA-20 | BARRA DO BUGRES | MATO GROSSO | Brasil | 5101704 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 22a077b7-11c1-3ea6-83aa-99c20b735394 | -15.60083 | -56.96435 | 2024-09-28 05:10:00 | NOAA-20 | NOSSA SENHORA DO LIVRAMENTO | MATO GROSSO | Brasil | 5106109 | 51 | 33 | nan | nan | nan | Cerrado | 3.3 |
| f01b0677-9263-3392-acf7-00ce648f78c6 | -15.60024 | -56.9683 | 2024-09-28 05:10:00 | NOAA-20 | NOSSA SENHORA DO LIVRAMENTO | MATO GROSSO | Brasil | 5106109 | 51 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 96e95ad2-4928-31b7-ad59-c17080f81cbb | -15.59861 | -57.49752 | 2024-09-28 05:10:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| d85ee52e-ea80-3f5e-a71b-3ac65123c9d5 | -15.59804 | -57.50136 | 2024-09-28 05:10:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 8ab2e0d3-d309-3e53-b804-de31f141a0b1 | -15.59676 | -56.96782 | 2024-09-28 05:10:00 | NOAA-20 | NOSSA SENHORA DO LIVRAMENTO | MATO GROSSO | Brasil | 5106109 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| cd791415-e74d-337a-9c83-816312565b54 | -15.59577 | -57.49316 | 2024-09-28 05:10:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 3e258376-240b-37db-b4a0-25a603d0162c | -15.59519 | -57.49699 | 2024-09-28 05:10:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| edae4d3d-d926-338e-a73d-198d20580afa | -15.59292 | -57.48879 | 2024-09-28 05:10:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 4e18134d-623a-3153-99ad-725b3948f976 | -15.59235 | -57.49263 | 2024-09-28 05:10:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 82be5706-bf98-3a91-851d-ee41f18f7574 | -15.59178 | -57.49646 | 2024-09-28 05:10:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 2efc70b5-13a5-379a-82a2-af62dca5aebe | -15.58893 | -57.49208 | 2024-09-28 05:10:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 2a56005f-d7e3-3905-9e94-d24c31252226 | -15.58837 | -57.49593 | 2024-09-28 05:10:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | 4.2 |
| db7af85c-d3ab-3a3c-ad42-e9052fd31c78 | -15.58609 | -57.48771 | 2024-09-28 05:10:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 392b8a47-3e33-3246-b0a0-26e2e2d6bce2 | -15.58552 | -57.49155 | 2024-09-28 05:10:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 9728ce9b-e8fa-3c1b-93f6-d6ef1895ee69 | -15.58267 | -57.48717 | 2024-09-28 05:10:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| d829904e-9ab8-37b9-83b7-88fdf32e3d9e | -15.5821 | -57.49101 | 2024-09-28 05:10:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 5fdeec41-058f-3b11-8eee-5c65fbb8d1df | -15.56714 | -56.92702 | 2024-09-28 05:10:00 | NOAA-20 | NOSSA SENHORA DO LIVRAMENTO | MATO GROSSO | Brasil | 5106109 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| b91b3bae-890a-3359-a8ea-f595eb83fdc5 | -15.56364 | -56.92658 | 2024-09-28 05:10:00 | NOAA-20 | NOSSA SENHORA DO LIVRAMENTO | MATO GROSSO | Brasil | 5106109 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 7f1dba0f-bcfc-387c-80d2-8c401f5e43ae | -15.56131 | -56.91811 | 2024-09-28 05:10:00 | NOAA-20 | NOSSA SENHORA DO LIVRAMENTO | MATO GROSSO | Brasil | 5106109 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| d37c7433-17d5-3735-9301-c80e92dbb718 | -15.55782 | -56.91766 | 2024-09-28 05:10:00 | NOAA-20 | NOSSA SENHORA DO LIVRAMENTO | MATO GROSSO | Brasil | 5106109 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| f4c16fba-635b-3f58-b6f4-7341dd75124b | -15.55724 | -56.92165 | 2024-09-28 05:10:00 | NOAA-20 | NOSSA SENHORA DO LIVRAMENTO | MATO GROSSO | Brasil | 5106109 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| d7a2a624-4232-39c5-9bda-eb069152f226 | -15.55432 | -56.91724 | 2024-09-28 05:10:00 | NOAA-20 | NOSSA SENHORA DO LIVRAMENTO | MATO GROSSO | Brasil | 5106109 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 91e5fcea-5570-3d81-be90-b774180b0b1f | -9.40883 | -56.88217 | 2024-09-28 05:10:00 | NOAA-20 | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 4b7058e8-32e1-39cf-83d6-3fb660985f07 | -9.40828 | -56.88574 | 2024-09-28 05:10:00 | NOAA-20 | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 19d089ee-61d8-3278-b091-e82199ef941c | -9.40265 | -56.85567 | 2024-09-28 05:10:00 | NOAA-20 | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 13d3aadb-55b5-36f0-9def-65f81cd927da | -9.4016 | -56.88471 | 2024-09-28 05:10:00 | NOAA-20 | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 0b95866b-afd7-35fb-87e1-be2619ee813c | -9.39826 | -56.88417 | 2024-09-28 05:10:00 | NOAA-20 | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 1912faf7-0767-3f04-ada7-e9d51e3a7eae | -9.39707 | -56.8475 | 2024-09-28 05:10:00 | NOAA-20 | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| a0569556-dfe1-32e4-951a-837392b0534b | -9.39652 | -56.85107 | 2024-09-28 05:10:00 | NOAA-20 | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 5a8cda81-d1cb-3496-8122-66f14ee8e110 | -9.39317 | -56.85054 | 2024-09-28 05:10:00 | NOAA-20 | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 802068b1-2294-3bc6-b3f7-91bb7fa2fc6d | -9.39263 | -56.85411 | 2024-09-28 05:10:00 | NOAA-20 | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 0d618aa9-b713-339e-9f86-34bafc0c286d | -9.38425 | -56.8418 | 2024-09-28 05:10:00 | NOAA-20 | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| b7569061-5f66-3508-b380-ad32a8aa2365 | -9.3837 | -56.84535 | 2024-09-28 05:10:00 | NOAA-20 | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 6fae077c-9ad9-3efe-8d54-880d0f49ecac | -9.38036 | -56.84483 | 2024-09-28 05:10:00 | NOAA-20 | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| bfec340e-7949-30f5-87ab-aba86a6ebbe4 | -9.37936 | -57.09499 | 2024-09-28 05:10:00 | NOAA-20 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| a12f0897-0a39-3747-90eb-a30f819a1e1d | -9.37702 | -56.8443 | 2024-09-28 05:10:00 | NOAA-20 | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 741f2c1f-ace0-3cbd-b013-1ebafc671b69 | -9.32689 | -57.16982 | 2024-09-28 05:10:00 | NOAA-20 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 508d3952-2703-3e8f-83cd-fb6059c73b2b | -9.32635 | -57.17333 | 2024-09-28 05:10:00 | NOAA-20 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |


[Clique aqui para ver as próximas entradas](README84.md)
