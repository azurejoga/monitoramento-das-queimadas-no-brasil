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

## Dados Diários - Página 37

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 9499377b-5064-35c3-8d99-525252eab418 | -15.8354 | -46.24212 | 2025-10-03 03:45:00 | NOAA-21 | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| d57b61cc-1733-361a-a8b0-a66167f67bad | -12.64219 | -46.9968 | 2025-10-03 03:45:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 23e34e41-1895-3e1d-b9e4-9fca67b51f1d | -11.76757 | -46.82866 | 2025-10-03 03:45:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| f107b353-4ab4-3bb9-9ebd-34384dd13c7e | -13.77794 | -47.52839 | 2025-10-03 03:45:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.6 |
| d2dd143a-6c2f-3379-a9da-1a6c9243c473 | -15.60343 | -47.04653 | 2025-10-03 03:45:00 | NOAA-21 | CABECEIRAS | GOIÁS | Brasil | 5204003 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 4b2c732f-81cb-339c-861e-ca1fe429de38 | -12.90956 | -46.36221 | 2025-10-03 03:45:00 | NOAA-21 | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 3.4 |
| a9c653e8-f734-3bfe-b4ae-a380ce5b3f98 | -11.13691 | -43.40951 | 2025-10-03 03:45:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Caatinga | 6.6 |
| 04c4954e-704b-34e2-853e-271d01b1653d | -14.60339 | -46.72433 | 2025-10-03 03:45:00 | NOAA-21 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 4.7 |
| c219c072-ae3a-32c8-a59f-9b980a916d7a | -11.81256 | -45.0353 | 2025-10-03 03:45:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 138a7c92-5c6e-35e1-b263-687e3ccf6dd5 | -15.7125 | -46.26044 | 2025-10-03 03:45:00 | NOAA-21 | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 0e3aed96-088f-3e3b-8f02-d96d351ea722 | -15.30172 | -46.29948 | 2025-10-03 03:45:00 | NOAA-21 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 2.2 |
| bc608ff5-0615-3057-871d-69a9e865bb0d | -11.10351 | -47.84269 | 2025-10-03 03:45:00 | NOAA-21 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 7e5c3ed4-b092-3c31-bb2a-073d3beb9fa7 | -14.73532 | -48.11727 | 2025-10-03 03:45:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 13a6d2c2-7315-3b9f-8fea-ed7611e8a124 | -12.75253 | -50.55999 | 2025-10-03 03:45:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| ba119272-86d5-3086-81f1-8feb6af00ab4 | -12.66008 | -46.95275 | 2025-10-03 03:45:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 9a2c6991-c39c-38b4-91e4-d33f6692af50 | -14.01762 | -44.96732 | 2025-10-03 03:45:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 2964645d-f7b9-3327-a61d-7607e1583ee4 | -14.46331 | -48.40956 | 2025-10-03 03:45:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 649d90bb-ef44-3a0f-a532-59513d6fc190 | -16.34129 | -42.37429 | 2025-10-03 03:45:00 | NOAA-21 | RUBELITA | MINAS GERAIS | Brasil | 3156502 | 31 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 402bf70a-4a23-3f31-977e-da7a38c37cf2 | -14.73636 | -48.11229 | 2025-10-03 03:45:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| fa817e3a-1aef-304c-98ed-e09702f8d589 | -13.37079 | -47.28018 | 2025-10-03 03:45:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 875c7fe9-ff6c-3829-a81c-8f19e9346676 | -12.89847 | -46.93334 | 2025-10-03 03:45:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 3b35e6bb-f0a9-3d2e-a276-a1da17221354 | -15.2019 | -47.99178 | 2025-10-03 03:45:00 | NOAA-21 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 6355da8f-34ef-3a00-8878-878990451d1a | -12.62165 | -39.52557 | 2025-10-03 03:45:00 | NOAA-21 | SANTA TEREZINHA | BAHIA | Brasil | 2928505 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 1da85a66-5612-35c3-b80f-4278aa11864f | -10.99019 | -46.52159 | 2025-10-03 03:45:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| bfea55f3-65e6-3265-a90f-0e93d1b5c808 | -13.39824 | -42.646 | 2025-10-03 03:45:00 | NOAA-21 | MACAÚBAS | BAHIA | Brasil | 2919801 | 29 | 33 | nan | nan | nan | Caatinga | 1.8 |
| c2f4ea06-67c8-3ad4-9292-999546a92037 | -15.30591 | -46.28819 | 2025-10-03 03:45:00 | NOAA-21 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 05cf16f7-c79b-32b2-9d93-5fe693714bd9 | -13.73824 | -48.01193 | 2025-10-03 03:45:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 30d18b94-a1fd-36a0-ab92-37c5f5f1dbb6 | -11.0775 | -48.36297 | 2025-10-03 03:45:00 | NOAA-21 | IPUEIRAS | TOCANTINS | Brasil | 1709807 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 194b621e-9c83-32c4-9c85-059c50ceccc8 | -15.3287 | -45.05256 | 2025-10-03 03:45:00 | NOAA-21 | JANUÁRIA | MINAS GERAIS | Brasil | 3135209 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| c1c4e67d-d6a2-32a0-8e2b-a4ca18f4fdd9 | -11.62543 | -45.03564 | 2025-10-03 03:45:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 562db4a3-e47b-3e0c-945c-fa3c7d27cf45 | -14.6831 | -48.08 | 2025-10-03 03:45:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 9ac94e00-adaa-3b66-b44d-23f91dc5c448 | -11.85131 | -44.96656 | 2025-10-03 03:45:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 40806aa8-df97-3e46-b191-32bbe178b114 | -12.90886 | -46.91048 | 2025-10-03 03:45:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 17cbf6e5-a8da-3fbf-bdab-81873ab07ba9 | -9.90545 | -43.72528 | 2025-10-03 03:45:00 | NOAA-21 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 7.4 |
| 57762cf6-65ec-3b05-8749-477918552628 | -13.68568 | -48.03843 | 2025-10-03 03:45:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| d6a1b95e-5f08-311f-88b1-69306e88a8c6 | -14.29104 | -45.91987 | 2025-10-03 03:45:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 527b32f6-f9fb-33fd-afbd-973e1da320ea | -12.63061 | -46.96634 | 2025-10-03 03:45:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 7268fcd6-2d2b-3261-8d5e-781e2a3e77ee | -14.98479 | -49.95916 | 2025-10-03 03:45:00 | NOAA-21 | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 4b10b6f0-4277-3f75-8b60-d1e8b1574bce | -13.19295 | -47.82925 | 2025-10-03 03:45:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 28c094bb-11d5-32f2-ae38-145b5a13598d | -14.09912 | -44.30629 | 2025-10-03 03:45:00 | NOAA-21 | FEIRA DA MATA | BAHIA | Brasil | 2910776 | 29 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 2952062b-fc88-363f-95e8-03f70cbe29ff | -15.27978 | -47.91209 | 2025-10-03 03:45:00 | NOAA-21 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 1a587a49-2281-3cb5-9336-e003e8fc8660 | -12.86759 | -46.99977 | 2025-10-03 03:45:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 91336091-6ec3-33d4-8f0b-b7dc6bb9d917 | -15.21688 | -47.65012 | 2025-10-03 03:45:00 | NOAA-21 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 072c8008-fa56-3efa-8b12-8142e091de29 | -11.10923 | -47.84656 | 2025-10-03 03:45:00 | NOAA-21 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 4.4 |
| e3ca2fbe-14e4-30cb-8982-0bac2b24c5f3 | -11.49255 | -45.00451 | 2025-10-03 03:45:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 19e48109-a55f-3724-8d15-cae886975deb | -13.29181 | -47.19329 | 2025-10-03 03:45:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| ec039441-d794-3d91-8b24-3b9f951da8c7 | -15.17591 | -43.62445 | 2025-10-03 03:45:00 | NOAA-21 | JAÍBA | MINAS GERAIS | Brasil | 3135050 | 31 | 33 | nan | nan | nan | Caatinga | 5.2 |
| a32cece3-7244-33b0-91f9-72c2d549ed57 | -15.66633 | -43.26711 | 2025-10-03 03:45:00 | NOAA-21 | NOVA PORTEIRINHA | MINAS GERAIS | Brasil | 3145059 | 31 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 09222961-4fa3-3405-b39b-349f8c794e5f | -14.19641 | -46.11958 | 2025-10-03 03:45:00 | NOAA-21 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 3ab9c866-6fdf-34c0-9d51-7659c1e8ac98 | -14.28537 | -45.92171 | 2025-10-03 03:45:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 3.9 |
| ade345ae-387e-3824-9cd2-f87a575dd4b1 | -14.45216 | -46.33841 | 2025-10-03 03:45:00 | NOAA-21 | SÍTIO D'ABADIA | GOIÁS | Brasil | 5220702 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 7e3706bf-07eb-3134-ac59-cbab019b1402 | -16.33736 | -42.3736 | 2025-10-03 03:45:00 | NOAA-21 | RUBELITA | MINAS GERAIS | Brasil | 3156502 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.0 |
| e56fa7bd-6d71-373f-9a14-6d70368cd610 | -13.48137 | -47.24178 | 2025-10-03 03:45:00 | NOAA-21 | TERESINA DE GOIÁS | GOIÁS | Brasil | 5221080 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 36ec28bd-b010-315c-9f13-bc745c92164e | -14.65934 | -48.25502 | 2025-10-03 03:45:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 69b7a481-ddb9-356a-b551-7f0d84cc852a | -10.8374 | -41.27689 | 2025-10-03 03:45:00 | NOAA-21 | OUROLÂNDIA | BAHIA | Brasil | 2923357 | 29 | 33 | nan | nan | nan | Caatinga | 3.8 |
| 26069f03-bbeb-31ba-85b0-53d1bc388180 | -13.27782 | -47.26239 | 2025-10-03 03:45:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 4.2 |
| cc79789d-61a4-39e4-a02e-dfe9de977216 | -9.77027 | -46.22018 | 2025-10-03 03:45:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| f642592c-5ee6-3f9e-9b3c-f256dd9a8b44 | -14.37964 | -45.94209 | 2025-10-03 03:45:00 | NOAA-21 | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 8ed57446-ea76-3208-8a35-7dc6177fd73b | -11.25851 | -47.79815 | 2025-10-03 03:45:00 | NOAA-21 | SANTA ROSA DO TOCANTINS | TOCANTINS | Brasil | 1718907 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| eb339462-d46f-363c-8e48-77350248c988 | -9.90669 | -43.71789 | 2025-10-03 03:45:00 | NOAA-21 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 10.6 |
| 295d971c-00e4-39db-9be7-d5e554afab4a | -14.74869 | -48.1113 | 2025-10-03 03:45:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 46078ef2-f822-3b75-81eb-b46dee852c0a | -12.92507 | -45.08613 | 2025-10-03 03:45:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 3.7 |
| b49d2d5b-baf3-36bb-a994-61c081db2e53 | -13.35256 | -47.33134 | 2025-10-03 03:45:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 4c0685af-c1d7-3c5b-be8f-c187060de68b | -15.83586 | -46.23977 | 2025-10-03 03:45:00 | NOAA-21 | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| cdfe9a15-d43b-311e-8c5d-7fb8d6044fcd | -15.25281 | -49.31671 | 2025-10-03 03:45:00 | NOAA-21 | GOIANÉSIA | GOIÁS | Brasil | 5208608 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 379cf8e5-75ae-3bb7-87f4-32a339559665 | -9.75847 | -47.81174 | 2025-10-03 03:45:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 0e093a20-13d1-3ec6-894c-2bf809ee42c4 | -12.62635 | -46.9583 | 2025-10-03 03:45:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 73ea9863-33b9-3052-878a-e2f4dedf7047 | -12.39592 | -45.01362 | 2025-10-03 03:45:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| d8097c7a-1a56-3213-8321-c208de95b8a9 | -10.86495 | -46.68244 | 2025-10-03 03:45:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 2f632f6b-7d24-3fdf-a2a1-03f1a2f1277e | -12.87452 | -47.03648 | 2025-10-03 03:45:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 4b8f3edd-4776-3d81-9ef7-3a5cc09fa611 | -12.39374 | -46.51445 | 2025-10-03 03:45:00 | NOAA-21 | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 6b2d9984-67eb-3e4b-b163-f173163f7a5d | -13.48078 | -47.24468 | 2025-10-03 03:45:00 | NOAA-21 | TERESINA DE GOIÁS | GOIÁS | Brasil | 5221080 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| e54e511b-1785-342e-8ec5-1830122cc80c | -11.62238 | -45.03152 | 2025-10-03 03:45:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 4e9892a6-0c19-3c84-a82f-41a65bade9e7 | -11.91634 | -46.26728 | 2025-10-03 03:45:00 | NOAA-21 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 5b5f31ef-5de5-3dda-895e-5d8af04751db | -12.68166 | -46.85376 | 2025-10-03 03:45:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| acdef6c6-703e-3b9c-83c9-2f0be1b37b10 | -12.54069 | -43.188 | 2025-10-03 03:45:00 | NOAA-21 | PARATINGA | BAHIA | Brasil | 2923704 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 174a0613-1807-35b9-8b59-9968f094e289 | -11.14775 | -43.40171 | 2025-10-03 03:45:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Caatinga | 6.7 |
| 389cef08-3ed8-3a65-a3ee-d006e022f99c | -12.68089 | -46.84956 | 2025-10-03 03:45:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 37026363-ba48-338b-85a0-da9f6550acc2 | -11.91698 | -46.26393 | 2025-10-03 03:45:00 | NOAA-21 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| bdfbb50d-6f2d-34a3-a265-f7a5509bb8e8 | -14.94147 | -46.88754 | 2025-10-03 03:45:00 | NOAA-21 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 994a32dc-e917-3db7-83b2-7ee4286d3e12 | -10.89278 | -44.27263 | 2025-10-03 03:45:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 3885361e-40ee-30c9-9fab-b9da0fa9ffdb | -11.47323 | -45.02383 | 2025-10-03 03:45:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 9e81fa9a-e68e-3a47-a0f2-090dfb01dd40 | -15.35912 | -47.06723 | 2025-10-03 03:45:00 | NOAA-21 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| f5eff07b-9578-3849-9b6f-f7e4520a518c | -12.90575 | -47.1604 | 2025-10-03 03:45:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 6a649841-c0cd-3d4c-87e1-7899097f51fc | -11.05357 | -47.80673 | 2025-10-03 03:45:00 | NOAA-21 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| d33c7cee-0ec5-34eb-a7de-ecbcfd4d2e66 | -15.20841 | -47.98915 | 2025-10-03 03:45:00 | NOAA-21 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| cc9f7baa-7fbe-389a-b0d2-3974d3bc6a6e | -13.57346 | -47.27977 | 2025-10-03 03:45:00 | NOAA-21 | TERESINA DE GOIÁS | GOIÁS | Brasil | 5221080 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 496b2acd-279a-3bff-bdbc-2c9efdca1fac | -13.75979 | -48.06688 | 2025-10-03 03:45:00 | NOAA-21 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 8.7 |
| fd1f50db-536c-30d6-8f25-a23ec0d75839 | -14.42445 | -46.09245 | 2025-10-03 03:45:00 | NOAA-21 | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| e6fa2004-803b-3478-a4fc-c1fb6469321f | -10.76887 | -45.33942 | 2025-10-03 03:45:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 991ae62b-5caf-3ad8-bcc9-6b7919db4c30 | -10.86481 | -46.67465 | 2025-10-03 03:45:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 7.0 |
| cb408ec1-c9e0-3692-8b6f-dee0f7d32c5a | -12.67651 | -48.57843 | 2025-10-03 03:45:00 | NOAA-21 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 04ec692b-dd79-32d0-b20d-f25700689525 | -10.34924 | -43.73017 | 2025-10-03 03:45:00 | NOAA-21 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 02183dad-f769-3aca-acef-3ba0929b3f4c | -14.93574 | -46.88828 | 2025-10-03 03:45:00 | NOAA-21 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 5b01efa3-e556-3119-b71e-40bb13283006 | -14.98513 | -49.95735 | 2025-10-03 03:45:00 | NOAA-21 | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 4.6 |
| f70e4a67-d4b9-3314-b98d-a984332f3aba | -14.18908 | -46.67883 | 2025-10-03 03:45:00 | NOAA-21 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 3f0074f4-109b-337e-8dff-aea8161631dc | -15.28523 | -47.9049 | 2025-10-03 03:45:00 | NOAA-21 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 2d53147b-56f3-3d19-aea7-f161ce9d38db | -13.20288 | -47.81039 | 2025-10-03 03:45:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 06282a53-831e-347f-9abc-4e385fb6b045 | -12.8697 | -47.00125 | 2025-10-03 03:45:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 356f17dc-7a01-3fa1-9875-403221904995 | -14.64672 | -48.25681 | 2025-10-03 03:45:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 5.1 |


[Clique aqui para ver as próximas entradas](README38.md)
