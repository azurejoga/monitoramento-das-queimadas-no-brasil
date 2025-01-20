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
| f101ce40-5197-34a7-9558-75481a2d5c3d | -7.34914 | -72.59886 | 2025-01-20 06:12:00 | NOAA-20 | GUAJARÁ | AMAZONAS | Brasil | 1301654 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 2b4fedc1-87e8-3328-879f-8b624e1c6856 | -7.35128 | -72.56314 | 2025-01-20 06:12:00 | NOAA-20 | GUAJARÁ | AMAZONAS | Brasil | 1301654 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| ff2af107-1f29-3890-83d7-c4ee25336c62 | -7.34849 | -72.5591 | 2025-01-20 06:12:00 | NOAA-20 | GUAJARÁ | AMAZONAS | Brasil | 1301654 | 13 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 98e3957b-e761-3e92-8313-5e6d84c97e83 | -7.35183 | -72.55962 | 2025-01-20 06:12:00 | NOAA-20 | GUAJARÁ | AMAZONAS | Brasil | 1301654 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 007dab20-f9e3-3d1b-9978-9a8a765fe174 | -7.34794 | -72.56262 | 2025-01-20 06:12:00 | NOAA-20 | GUAJARÁ | AMAZONAS | Brasil | 1301654 | 13 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 430f5cda-3e8f-3525-9dba-61ad4c0d0730 | -7.34968 | -72.59534 | 2025-01-20 06:12:00 | NOAA-20 | GUAJARÁ | AMAZONAS | Brasil | 1301654 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| fde145a0-abf1-3179-b60d-8e478f60bc6f | -17.37 | -44.92 | 2025-01-20 11:00:00 | MSG-03 | PIRAPORA | MINAS GERAIS | Brasil | 3151206 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| a3ac7ef5-9475-3e82-865b-53820baa1b7e | -8.06922 | -34.97369 | 2025-01-20 11:44:00 | TERRA_M-M | RECIFE | PERNAMBUCO | Brasil | 2611606 | 26 | 33 | nan | nan | nan | Mata Atlântica | 21.1 |
| b17ebe18-3093-33a8-8c93-802b04eb304d | -7.77474 | -35.77082 | 2025-01-20 11:44:00 | TERRA_M-M | VERTENTE DO LÉRIO | PERNAMBUCO | Brasil | 2616183 | 26 | 33 | nan | nan | nan | Caatinga | 12.0 |
| 57d53773-ae39-34d6-8888-0938ae7fdeb0 | -15.73 | -45.9 | 2025-01-20 12:00:00 | MSG-03 | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 5b9f0d85-27f9-3397-a129-7d8c15b7352a | -15.83 | -43.46 | 2025-01-20 12:00:00 | MSG-03 | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 2a62a4f9-718a-35a5-9b7d-8d7c1b99829e | -15.73 | -45.95 | 2025-01-20 12:00:00 | MSG-03 | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 41af9a1a-8b5a-3c3f-9a91-bbd7fedcd0cf | -15.39 | -43.78 | 2025-01-20 12:00:00 | MSG-03 | JAÍBA | MINAS GERAIS | Brasil | 3135050 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 01baae5a-fcc8-3e82-bb1c-475e504921fb | 2.8723 | -60.6171 | 2025-01-20 13:20:00 | GOES-16 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 63.5 |
| 4f6d243c-7d84-3fed-a53a-fb00db4c051f | 2.8723 | -60.6171 | 2025-01-20 14:30:00 | GOES-16 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 74.1 |


