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
| 10d8763b-7022-3b9f-abb6-cbd23a7b585e | -8.9322 | -45.74866 | 2026-08-25 04:25:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 83cb6f8a-2bc0-3d6c-8d5c-0fc8dd253cd0 | -7.14854 | -42.74583 | 2026-08-25 04:25:00 | NOAA-20 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 3.2 |
| 636291ad-1138-3b51-86ab-267467836a49 | -7.86801 | -46.11513 | 2026-08-25 04:25:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| f511a446-5aa1-37f6-b777-cf38abb77f7c | -4.71422 | -42.77262 | 2026-08-25 04:25:00 | NOAA-20 | UNIÃO | PIAUÍ | Brasil | 2211100 | 22 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 619037ec-40fe-3f32-8469-9ad19973eae9 | -6.34786 | -54.75704 | 2026-08-25 04:25:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f98654f9-ee8f-3345-ac68-b7d1b3eac5e1 | -7.30185 | -43.00622 | 2026-08-25 04:25:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 0dc04615-a17c-3688-841a-e510d1bdf4a2 | -6.2169 | -55.47958 | 2026-08-25 04:25:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b1fa2013-e617-3246-945b-c6f947044bf3 | -6.17615 | -53.48145 | 2026-08-25 04:25:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 1b3e8f3e-546a-3934-bd93-e21f7d4b2d1b | -6.62743 | -58.48898 | 2026-08-25 04:25:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 11.5 |
| 270ca6b5-fe79-3fbc-beaf-d88ba2898cfd | -6.32774 | -54.7505 | 2026-08-25 04:25:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 0e91c280-f53b-39ad-b68d-fc8ea865bec5 | -7.42687 | -43.12406 | 2026-08-25 04:25:00 | NOAA-20 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 2.7 |
| 80f77e03-f401-3a25-b869-168fb8c47f92 | -7.27419 | -45.36471 | 2026-08-25 04:25:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 5b2c1420-e07a-3768-98f0-545319a30b47 | -3.06743 | -48.36101 | 2026-08-25 04:25:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 1f267c9f-ff05-3eab-a296-b27e995b9314 | -8.57717 | -54.85328 | 2026-08-25 04:25:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 8.0 |
| 3ef8206a-8c0d-37b9-8c78-7ef143edc56e | -6.74574 | -50.96167 | 2026-08-25 04:25:00 | NOAA-20 | OURILÂNDIA DO NORTE | PARÁ | Brasil | 1505437 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| eddcec08-e403-3e18-bc45-d1fa8826e66b | -13.87444 | -54.03384 | 2026-08-25 04:27:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 5.8 |
| ffd39277-288a-3d2a-8c0f-881a4af44515 | -15.24047 | -52.80241 | 2026-08-25 04:27:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| b848d3d5-3b66-3e09-81c4-eb969da1d19e | -13.86795 | -54.01714 | 2026-08-25 04:27:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 6d3ed3e4-6ee6-36f2-9e9d-da893ea893e4 | -13.4434 | -43.84766 | 2026-08-25 04:27:00 | NOAA-20 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 3342a055-5306-3d67-816a-fd26a08f9f2a | -11.5769 | -46.96969 | 2026-08-25 04:27:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 08338e56-fb35-3f52-bae9-073c4caa6753 | -13.64379 | -49.02698 | 2026-08-25 04:27:00 | NOAA-20 | SANTA TEREZA DE GOIÁS | GOIÁS | Brasil | 5219605 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 82fd2263-d2e3-345c-a646-6e6f74cb2268 | -10.92238 | -51.09423 | 2026-08-25 04:27:00 | NOAA-20 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 5055ecd0-1298-3ea6-aecc-57629ffbc998 | -12.88949 | -48.50366 | 2026-08-25 04:27:00 | NOAA-20 | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 2f423ecd-9e78-32d3-9d42-88e457cc8893 | -12.60399 | -44.63767 | 2026-08-25 04:27:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 42c35ab1-d15f-3818-b4b0-e13206530372 | -13.34666 | -48.20327 | 2026-08-25 04:27:00 | NOAA-20 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| d1a2e09f-fc2d-3017-9a7b-64c0c146e681 | -13.35566 | -48.21214 | 2026-08-25 04:27:00 | NOAA-20 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 646486f4-08d7-3803-83ac-8cfa23287259 | -15.24151 | -52.79454 | 2026-08-25 04:27:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| ae4bd720-1d3d-3ceb-a0e3-6dc8b4354395 | -15.24646 | -52.79118 | 2026-08-25 04:27:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| b245e6da-10e2-3c3f-ae0e-33e5d5c5166c | -10.85481 | -50.55949 | 2026-08-25 04:27:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 411e8833-e605-343c-b9c7-8fab9b1c207c | -12.88653 | -48.47896 | 2026-08-25 04:27:00 | NOAA-20 | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| ca0459da-abd2-3bf2-8c0e-9df80f5a82bc | -10.77476 | -50.93192 | 2026-08-25 04:27:00 | NOAA-20 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 19.6 |
| 14daf7fd-caac-382a-8d72-5aa345cdd2cc | -11.98582 | -45.91957 | 2026-08-25 04:27:00 | NOAA-20 | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| efbb9fb4-22a8-3a27-b3b4-0a850496355f | -14.2785 | -53.20752 | 2026-08-25 04:27:00 | NOAA-20 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 16a682c3-3886-3666-afe9-37e6e890aab9 | -11.16127 | -54.00555 | 2026-08-25 04:27:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| e14fcdea-da50-3aa9-84c5-18d3a0d19430 | -14.35726 | -51.75888 | 2026-08-25 04:27:00 | NOAA-20 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| d2bf06a2-3afc-32c9-afeb-c5cb9a72dc80 | -14.97424 | -52.68682 | 2026-08-25 04:27:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| acd746c0-921f-3389-95b9-aaf548e456aa | -15.24701 | -52.79073 | 2026-08-25 04:27:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 4be424e5-d374-38a8-a70a-052c0eab763e | -12.86328 | -48.49106 | 2026-08-25 04:27:00 | NOAA-20 | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| f5b889eb-9602-395e-bcca-05094d195b9b | -12.21334 | -43.18061 | 2026-08-25 04:27:00 | NOAA-20 | IBOTIRAMA | BAHIA | Brasil | 2913200 | 29 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 739e23d7-c8a3-3ce4-8c6c-ac57e66c8d67 | -12.84472 | -48.49614 | 2026-08-25 04:27:00 | NOAA-20 | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 587afd13-24ea-3972-96ce-b9b266683a05 | -14.72808 | -47.15406 | 2026-08-25 04:27:00 | NOAA-20 | VILA BOA | GOIÁS | Brasil | 5222203 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 1eb852c2-96e9-3903-89a2-745558fa1227 | -14.3579 | -51.75533 | 2026-08-25 04:27:00 | NOAA-20 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| ea921ca1-d302-3f69-99f9-e0b3cb46bb2d | -16.44003 | -43.46629 | 2026-08-25 04:27:00 | NOAA-20 | FRANCISCO SÁ | MINAS GERAIS | Brasil | 3126703 | 31 | 33 | nan | nan | nan | Cerrado | 4.9 |
| fc7489d4-dfc4-30c3-8791-495f30d7c5f7 | -10.3183 | -50.40193 | 2026-08-25 04:27:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| f1e9c15b-0037-36d5-a715-430a1815197f | -15.26724 | -52.7986 | 2026-08-25 04:27:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 3201914b-7a99-3e6d-9e67-299f5f2bca83 | -10.85145 | -50.55529 | 2026-08-25 04:27:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| e1928e18-f4df-311a-a5db-2f3d03a8730f | -11.43468 | -44.52573 | 2026-08-25 04:27:00 | NOAA-20 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 1d006317-1214-3f6d-a899-08a7390d324c | -11.97204 | -45.8993 | 2026-08-25 04:27:00 | NOAA-20 | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 8e08874d-7bfa-3b36-8e85-cd0f772d0b5b | -14.37759 | -51.96732 | 2026-08-25 04:27:00 | NOAA-20 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| c50dc433-d270-3cf3-a596-71ead3297671 | -14.39311 | -51.76571 | 2026-08-25 04:27:00 | NOAA-20 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 2e69005f-2d71-3375-b9a1-8d2ae7796d5d | -18.44621 | -48.41601 | 2026-08-25 04:27:00 | NOAA-20 | ARAGUARI | MINAS GERAIS | Brasil | 3103504 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 5aeed3df-35db-39eb-a68f-4c88f088679a | -16.06218 | -50.46282 | 2026-08-25 04:27:00 | NOAA-20 | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 22ebc0da-c074-3d82-b287-9308983f925d | -12.77236 | -48.3634 | 2026-08-25 04:27:00 | NOAA-20 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 24f1f853-24bc-3029-ac51-310d6c43eb70 | -10.77938 | -50.92912 | 2026-08-25 04:27:00 | NOAA-20 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 19.6 |
| 5b3e88b9-cd17-342e-a0ef-e1080ec26eb0 | -10.78678 | -50.93411 | 2026-08-25 04:27:00 | NOAA-20 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 27.0 |
| f4f9d834-28df-31c6-9424-717101e1e531 | -11.08938 | -46.15474 | 2026-08-25 04:27:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 9d841bc6-d3e4-3aaf-a3f0-38717289f08e | -15.31928 | -52.82241 | 2026-08-25 04:27:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 33b8d8cb-b291-3f25-aae1-d9c1af7fe329 | -13.35966 | -48.20907 | 2026-08-25 04:27:00 | NOAA-20 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 8965caea-31c4-38b6-aff3-9717313c4e3b | -13.35404 | -48.20089 | 2026-08-25 04:27:00 | NOAA-20 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 9dd30fb8-95d4-3cb9-91c6-99a9b25a4032 | -9.19586 | -59.58111 | 2026-08-25 04:27:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 072a2f6f-0cbd-33f8-a396-58b122d8173d | -12.77851 | -44.26764 | 2026-08-25 04:27:00 | NOAA-20 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 8.2 |
| 525b5757-37b5-3bca-9f13-eeff1340556e | -15.27143 | -52.79943 | 2026-08-25 04:27:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 13dbb479-f683-30da-8cf5-1de2004f8b58 | -10.79743 | -50.92814 | 2026-08-25 04:27:00 | NOAA-20 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 24.8 |
| c7849220-b416-3d0e-9db0-320b82107b34 | -14.35168 | -52.92896 | 2026-08-25 04:27:00 | NOAA-20 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 19d46832-4a8c-3705-832e-ba039d67a720 | -13.0943 | -43.35469 | 2026-08-25 04:27:00 | NOAA-20 | BOM JESUS DA LAPA | BAHIA | Brasil | 2903904 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| d7c3a69b-213e-314a-9e67-138c66f45275 | -9.16587 | -58.33384 | 2026-08-25 04:27:00 | NOAA-20 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| a45aed0b-f225-3910-80df-e264b4db39f5 | -14.39247 | -51.76925 | 2026-08-25 04:27:00 | NOAA-20 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 0f5c0e8f-983a-335a-aac7-458de419c877 | -10.92744 | -51.06544 | 2026-08-25 04:27:00 | NOAA-20 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 7.6 |
| 37715fe1-1d04-34d3-8f34-0bbbeaf20c16 | -12.69883 | -48.4053 | 2026-08-25 04:27:00 | NOAA-20 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| d3ed250b-5afe-3a26-a350-8362410b5355 | -11.56849 | -46.97932 | 2026-08-25 04:27:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| bce49a07-7bd8-3720-87df-b1afccc1f046 | -11.56598 | -46.97907 | 2026-08-25 04:27:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 5.5 |
| e90ea65c-f8be-3244-8bc2-fc8f6c6066b5 | -14.40883 | -52.89622 | 2026-08-25 04:27:00 | NOAA-20 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| c984d58b-8b56-3bfd-9f21-63bbdf32de51 | -11.43245 | -44.54039 | 2026-08-25 04:27:00 | NOAA-20 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 9021847b-abc4-3257-9f0c-f97feb11cf00 | -13.62706 | -49.01983 | 2026-08-25 04:27:00 | NOAA-20 | SANTA TEREZA DE GOIÁS | GOIÁS | Brasil | 5219605 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| dec13c36-2e9f-3dfa-9b88-a65b8af43cb0 | -13.35005 | -48.20387 | 2026-08-25 04:27:00 | NOAA-20 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 0e211eef-fef5-3487-bcec-b8a9b39cfcae | -15.40698 | -52.84251 | 2026-08-25 04:27:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 6e800b0a-9a33-3b6f-a6e9-dffec49db203 | -14.72533 | -47.14994 | 2026-08-25 04:27:00 | NOAA-20 | VILA BOA | GOIÁS | Brasil | 5222203 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 6cc3bcc3-dd1a-3803-98b7-2607e2f71feb | -14.30534 | -53.33039 | 2026-08-25 04:27:00 | NOAA-20 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 18d87eb5-9eb0-327e-83e2-e6d86778627a | -16.40521 | -49.92349 | 2026-08-25 04:27:00 | NOAA-20 | ANICUNS | GOIÁS | Brasil | 5201306 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 6221e42a-ceb0-324c-bfee-4ca8eb514145 | -16.06293 | -50.45847 | 2026-08-25 04:27:00 | NOAA-20 | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 43db28fb-8802-39e4-b30d-5a057b5aaaa5 | -16.01881 | -42.98138 | 2026-08-25 04:27:00 | NOAA-20 | RIACHO DOS MACHADOS | MINAS GERAIS | Brasil | 3154507 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 01f5780a-2d03-3d1d-ae84-847cc44344d8 | -12.74135 | -46.46833 | 2026-08-25 04:27:00 | NOAA-20 | AURORA DO TOCANTINS | TOCANTINS | Brasil | 1702703 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| cd265c85-0e17-36e6-a519-37dcd2d0ebf3 | -12.12852 | -43.3866 | 2026-08-25 04:27:00 | NOAA-20 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 3fba51de-a743-302e-8f8c-768f9539425a | -12.74466 | -46.46888 | 2026-08-25 04:27:00 | NOAA-20 | AURORA DO TOCANTINS | TOCANTINS | Brasil | 1702703 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| eb3ba890-044d-3805-8f87-5608b8425a24 | -12.73692 | -46.47484 | 2026-08-25 04:27:00 | NOAA-20 | AURORA DO TOCANTINS | TOCANTINS | Brasil | 1702703 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| e9418a12-c35a-3f52-8b06-e0613ec1f586 | -11.07782 | -46.14208 | 2026-08-25 04:27:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.5 |
| d119c7d3-5348-3e24-b85b-39066a138880 | -10.77075 | -50.9312 | 2026-08-25 04:27:00 | NOAA-20 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 90f429dd-f39d-387e-ba4d-2cfe86b4c8ed | -14.38097 | -51.97176 | 2026-08-25 04:27:00 | NOAA-20 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 56c4cad3-0746-33e0-a01a-8088cb2376fb | -16.50424 | -54.67527 | 2026-08-25 04:27:00 | NOAA-20 | RONDONÓPOLIS | MATO GROSSO | Brasil | 5107602 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| b7b9654a-2ef2-31a1-838b-d78df67303aa | -11.98637 | -45.91605 | 2026-08-25 04:27:00 | NOAA-20 | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| ed54314d-908f-3578-97f5-cf29be2b40d0 | -16.41225 | -49.9247 | 2026-08-25 04:27:00 | NOAA-20 | ANICUNS | GOIÁS | Brasil | 5201306 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 2a9d8a76-8bcc-371d-a7bf-cb8775c707b4 | -11.86024 | -51.69699 | 2026-08-25 04:27:00 | NOAA-20 | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 6e6925c6-dea7-3e00-9b5b-c200f7272f19 | -13.35463 | -48.1973 | 2026-08-25 04:27:00 | NOAA-20 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| a8d604e3-00b1-3676-88fb-cdcb568217d6 | -13.4475 | -43.84429 | 2026-08-25 04:27:00 | NOAA-20 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| a4a4a02d-15d0-37e6-a5f3-5d14a40b40b0 | -12.87014 | -48.49237 | 2026-08-25 04:27:00 | NOAA-20 | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| e3fccb87-e3a5-353c-8e5a-f41731ccf463 | -12.11448 | -45.72757 | 2026-08-25 04:27:00 | NOAA-20 | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 635e74a2-f964-3f9c-95e6-3c526f7cb0d9 | -14.46475 | -51.81147 | 2026-08-25 04:27:00 | NOAA-20 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 0828d0f6-249e-3c0a-b8ae-ca150d013a8d | -10.91344 | -51.07402 | 2026-08-25 04:27:00 | NOAA-20 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 19.0 |
| f0064003-360d-32ca-ae0f-e901b5ed7f2c | -12.74304 | -46.45776 | 2026-08-25 04:27:00 | NOAA-20 | AURORA DO TOCANTINS | TOCANTINS | Brasil | 1702703 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 85905859-0845-36a0-988c-c9d547305dc2 | -12.70438 | -48.41448 | 2026-08-25 04:27:00 | NOAA-20 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 4.2 |


[Clique aqui para ver as próximas entradas](README38.md)
