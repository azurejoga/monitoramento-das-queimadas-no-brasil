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

## Dados Diários - Página 13

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 6177f99d-fc99-38d9-b491-3ff54251b9d8 | -0.53923 | -49.18942 | 2026-09-27 04:06:00 | NOAA-20 | CACHOEIRA DO ARARI | PARÁ | Brasil | 1502004 | 15 | 33 | nan | nan | nan | Amazônia | 6.6 |
| f624ada8-b017-391b-9d5c-170f99a2d924 | -2.90505 | -45.42486 | 2026-09-27 04:06:00 | NOAA-20 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 956998f2-fcc3-35b2-83cb-c753ee37d3ad | -2.35088 | -46.09384 | 2026-09-27 04:06:00 | NOAA-20 | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| ab8faa56-e3ac-3208-8526-6ae1853c3faa | -1.85695 | -47.98109 | 2026-09-27 04:06:00 | NOAA-20 | CONCÓRDIA DO PARÁ | PARÁ | Brasil | 1502756 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| c4ecbbcf-c6e6-3222-bb94-167faac9ade8 | -0.51881 | -49.13171 | 2026-09-27 04:06:00 | NOAA-20 | CACHOEIRA DO ARARI | PARÁ | Brasil | 1502004 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 533febb6-46c2-3201-877e-34ceeb336406 | -2.00177 | -47.01195 | 2026-09-27 04:06:00 | NOAA-20 | GARRAFÃO DO NORTE | PARÁ | Brasil | 1503077 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| f682a603-9ecd-3e25-a799-d79a73a2e2c2 | -3.40511 | -39.16933 | 2026-09-27 04:06:00 | NOAA-20 | PARAIPABA | CEARÁ | Brasil | 2310258 | 23 | 33 | nan | nan | nan | Caatinga | 3.1 |
| 05477ae7-18b4-3c00-9867-7f57d8535fee | -0.51369 | -49.12671 | 2026-09-27 04:06:00 | NOAA-20 | CACHOEIRA DO ARARI | PARÁ | Brasil | 1502004 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 16b2bb38-5f99-374e-888b-938c60a3a77d | -3.11521 | -45.43617 | 2026-09-27 04:06:00 | NOAA-20 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 3c59e5ec-0a84-3547-8e60-5f7752c0540e | -2.88457 | -49.48346 | 2026-09-27 04:06:00 | NOAA-20 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 0d0a14dd-48fc-39db-b7b3-2e29161df9c2 | -1.86221 | -47.9819 | 2026-09-27 04:06:00 | NOAA-20 | CONCÓRDIA DO PARÁ | PARÁ | Brasil | 1502756 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 226b7048-aae6-37e3-9743-bd6d8038cae3 | -3.91631 | -43.02042 | 2026-09-27 04:06:00 | NOAA-20 | BURITI | MARANHÃO | Brasil | 2102200 | 21 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 20817b5e-4664-34d2-a6ba-a2673720079c | -0.50592 | -49.13792 | 2026-09-27 04:06:00 | NOAA-20 | CACHOEIRA DO ARARI | PARÁ | Brasil | 1502004 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 85557f7a-76a4-3d4b-8983-b98194ad6ae2 | -2.92832 | -45.50882 | 2026-09-27 04:06:00 | NOAA-20 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 3.8 |
| ee2ad06e-10ed-3087-b23e-bc11912eb428 | -2.88962 | -49.4884 | 2026-09-27 04:06:00 | NOAA-20 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| e296f1de-4900-3117-9a76-e0775e31275a | -0.53857 | -49.19351 | 2026-09-27 04:06:00 | NOAA-20 | CACHOEIRA DO ARARI | PARÁ | Brasil | 1502004 | 15 | 33 | nan | nan | nan | Amazônia | 6.6 |
| 18fb2ea1-08f4-3206-ae27-f6b714775f96 | -0.50596 | -49.13747 | 2026-09-27 04:06:00 | NOAA-20 | CACHOEIRA DO ARARI | PARÁ | Brasil | 1502004 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 8697d38d-11b3-3c6b-83c0-0cc09230e474 | -3.46183 | -39.58404 | 2026-09-27 04:06:00 | NOAA-20 | ITAPIPOCA | CEARÁ | Brasil | 2306405 | 23 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 16a4ba97-6a21-3004-8d90-229376248793 | 0.70515 | -51.43455 | 2026-09-27 04:06:00 | NOAA-20 | PORTO GRANDE | AMAPÁ | Brasil | 1600535 | 16 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 999c0b73-cc1f-38e2-ad40-cb992761966d | -0.50526 | -49.14197 | 2026-09-27 04:06:00 | NOAA-20 | CACHOEIRA DO ARARI | PARÁ | Brasil | 1502004 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| a7e7e765-7568-3ffe-bf51-9fb59a6d3e62 | -0.50017 | -49.1365 | 2026-09-27 04:06:00 | NOAA-20 | CACHOEIRA DO ARARI | PARÁ | Brasil | 1502004 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 4f82a1b3-02b8-362a-8b99-3e33181e36d3 | -3.11953 | -45.4369 | 2026-09-27 04:06:00 | NOAA-20 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 206f6a3e-dafa-3a99-9ec7-9e1892ec9c9c | -2.34631 | -46.09309 | 2026-09-27 04:06:00 | NOAA-20 | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 60c01597-cba3-3bc3-91c6-29d34704c570 | -2.44576 | -49.22507 | 2026-09-27 04:06:00 | NOAA-20 | MOCAJUBA | PARÁ | Brasil | 1504604 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| ba81bb7e-a864-3115-aef5-14813bb494e3 | -2.90871 | -45.42974 | 2026-09-27 04:06:00 | NOAA-20 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 48cff646-c73d-3747-87d0-d6c04d06c02c | -0.5066 | -49.13338 | 2026-09-27 04:06:00 | NOAA-20 | CACHOEIRA DO ARARI | PARÁ | Brasil | 1502004 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 3928d0ae-e13e-3016-bdac-dc30f28082c8 | 0.69835 | -51.43557 | 2026-09-27 04:06:00 | NOAA-20 | PORTO GRANDE | AMAPÁ | Brasil | 1600535 | 16 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 45ee8d16-fb01-3e59-a87a-0fde650121b4 | -0.50469 | -49.14561 | 2026-09-27 04:06:00 | NOAA-20 | CACHOEIRA DO ARARI | PARÁ | Brasil | 1502004 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| a285f82a-aefc-3403-b286-8eae77484b2b | -4.58238 | -37.73497 | 2026-09-27 04:06:00 | NOAA-20 | ARACATI | CEARÁ | Brasil | 2301109 | 23 | 33 | nan | nan | nan | Caatinga | 3.1 |
| f9f25f3f-fef8-3761-8a72-bb963a9517f3 | -0.50659 | -49.13386 | 2026-09-27 04:06:00 | NOAA-20 | CACHOEIRA DO ARARI | PARÁ | Brasil | 1502004 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 027a3c53-ed06-36b4-bac4-ce8881f8e0fe | -0.50014 | -49.13698 | 2026-09-27 04:06:00 | NOAA-20 | CACHOEIRA DO ARARI | PARÁ | Brasil | 1502004 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| f704c407-f6ec-399b-bfbe-2d41598d0c96 | -2.73323 | -49.46659 | 2026-09-27 04:06:00 | NOAA-20 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| e55275cb-d8c0-3064-9a0b-b847579afcf9 | -1.75697 | -48.74471 | 2026-09-27 04:06:00 | NOAA-20 | ABAETETUBA | PARÁ | Brasil | 1500107 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 07822777-4ff1-358e-b6ab-221d83ebf8ad | -0.50533 | -49.14153 | 2026-09-27 04:06:00 | NOAA-20 | CACHOEIRA DO ARARI | PARÁ | Brasil | 1502004 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 77f75a6c-ae2a-3b86-9176-c9c679a8200c | -2.91005 | -45.42142 | 2026-09-27 04:06:00 | NOAA-20 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 72edaf61-b6ca-3ec5-89ba-1315fcc9a4bf | 0.69981 | -51.43535 | 2026-09-27 04:06:00 | NOAA-20 | PORTO GRANDE | AMAPÁ | Brasil | 1600535 | 16 | 33 | nan | nan | nan | Amazônia | 2.8 |
| ddbc0d2b-2a26-3146-bd4b-d87e158a413a | -3.91264 | -43.01982 | 2026-09-27 04:06:00 | NOAA-20 | BURITI | MARANHÃO | Brasil | 2102200 | 21 | 33 | nan | nan | nan | Cerrado | 4.4 |
| d36092e0-9aa4-382a-827c-c0e6fb39dbf4 | -6.15575 | -47.13284 | 2026-09-27 04:08:00 | NOAA-20 | CAMPESTRE DO MARANHÃO | MARANHÃO | Brasil | 2102556 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 6b03be06-384a-31e0-a4b3-0ac7f142e344 | -8.35689 | -44.17592 | 2026-09-27 04:08:00 | NOAA-20 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 119.0 |
| 96cd91a5-c015-3118-82a6-240641b3a272 | -7.3622 | -42.11846 | 2026-09-27 04:08:00 | NOAA-20 | COLÔNIA DO PIAUÍ | PIAUÍ | Brasil | 2202778 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| f2f369a4-73a1-31df-bfd9-b15f4c97a83b | -6.92985 | -41.60845 | 2026-09-27 04:08:00 | NOAA-20 | PICOS | PIAUÍ | Brasil | 2208007 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 7867745e-a3f8-318a-b4f3-0d58a6619d32 | -8.34155 | -44.16133 | 2026-09-27 04:08:00 | NOAA-20 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 419c2252-2cf5-3a49-8a0c-3fa2cc06b546 | -5.10301 | -38.10404 | 2026-09-27 04:08:00 | NOAA-20 | LIMOEIRO DO NORTE | CEARÁ | Brasil | 2307601 | 23 | 33 | nan | nan | nan | Caatinga | 4.4 |
| 67d3b2b1-dd7f-3369-a3b8-8a3a72e563a5 | -5.34776 | -45.84959 | 2026-09-27 04:08:00 | NOAA-20 | ITAIPAVA DO GRAJAÚ | MARANHÃO | Brasil | 2105351 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 8245d16e-b4e2-3550-8ab6-e8df91f2470d | -4.30254 | -46.57437 | 2026-09-27 04:08:00 | NOAA-20 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e9fc7acf-016b-353b-ba55-1aec1e271a2e | -10.02025 | -50.14015 | 2026-09-27 04:08:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 05b6e016-a58c-31ca-9564-84eddeac8ed6 | -8.34234 | -44.17959 | 2026-09-27 04:08:00 | NOAA-20 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 073804e0-1684-371f-829e-79cc8422be7b | -5.51408 | -40.88304 | 2026-09-27 04:08:00 | NOAA-20 | NOVO ORIENTE | CEARÁ | Brasil | 2309409 | 23 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 931bbc14-de17-395f-b5e0-7f1a59421786 | -8.34657 | -44.1697 | 2026-09-27 04:08:00 | NOAA-20 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 5da164a0-924f-3a84-a5aa-ac918bf7051b | -8.34676 | -44.17575 | 2026-09-27 04:08:00 | NOAA-20 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 0738b5ea-4cac-313c-9ebd-fef9a0de5328 | -8.34287 | -44.16912 | 2026-09-27 04:08:00 | NOAA-20 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 4.3 |
| b71ecc89-d956-3391-9f65-44a144ecf416 | -6.0518 | -53.60786 | 2026-09-27 04:08:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b379e31a-9930-39fe-966f-bc2669ffcb14 | -7.36161 | -42.12216 | 2026-09-27 04:08:00 | NOAA-20 | COLÔNIA DO PIAUÍ | PIAUÍ | Brasil | 2202778 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| d9a50d71-14cb-36cf-8a7e-f56f71aa49c1 | -10.0171 | -50.15676 | 2026-09-27 04:08:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 7dab8927-89fe-3baa-9d9c-59dd952c0454 | -7.12331 | -43.66216 | 2026-09-27 04:08:00 | NOAA-20 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 3.6 |
| fb32557c-4102-335b-825c-56d56813d8bb | -7.37556 | -44.76015 | 2026-09-27 04:08:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 5ceaf2eb-1a9a-315b-a103-23315d436484 | -3.41574 | -50.42592 | 2026-09-27 04:08:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 3fea9875-643e-38bd-bc17-2f571123a601 | -6.8451 | -43.50974 | 2026-09-27 04:08:00 | NOAA-20 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 54d071a8-8e60-3e9d-8dc5-60d9de8b75aa | -5.1822 | -46.11613 | 2026-09-27 04:08:00 | NOAA-20 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |
| c939151e-2e1a-3ab0-9c15-53d8bc0f2b91 | -6.77557 | -48.66287 | 2026-09-27 04:08:00 | NOAA-20 | ARAGOMINAS | TOCANTINS | Brasil | 1701309 | 17 | 33 | nan | nan | nan | Amazônia | 3.8 |
| ab3f2c3a-fb11-3066-bc09-dcd98edee4c7 | -8.34363 | -44.16471 | 2026-09-27 04:08:00 | NOAA-20 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 4.3 |
| d09205ea-cd64-3d86-a2de-04b3ecb72868 | -8.34432 | -44.18291 | 2026-09-27 04:08:00 | NOAA-20 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 33.0 |
| a0692aea-9c40-386d-b2ba-8ae46a351798 | -7.33173 | -42.09087 | 2026-09-27 04:08:00 | NOAA-20 | COLÔNIA DO PIAUÍ | PIAUÍ | Brasil | 2202778 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| fbf870ec-cd17-325a-b8a2-a379f8d8bedc | -8.34452 | -44.16634 | 2026-09-27 04:08:00 | NOAA-20 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 86a27191-43a4-34d6-b72f-c241eb203db7 | -6.92992 | -42.86652 | 2026-09-27 04:08:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| b5935b13-a5f3-328b-aedf-54f062114441 | -7.28976 | -43.30648 | 2026-09-27 04:08:00 | NOAA-20 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| ec9b52cd-ff2d-32e1-9324-41e097f16b7a | -3.84641 | -52.014 | 2026-09-27 04:08:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 94e95b6d-e891-3f4f-80ea-0fb35b74dddf | -5.27148 | -48.37863 | 2026-09-27 04:08:00 | NOAA-20 | SÃO SEBASTIÃO DO TOCANTINS | TOCANTINS | Brasil | 1720309 | 17 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 7a48bc53-d311-3288-a94f-46875dfcdff8 | -4.84707 | -42.89125 | 2026-09-27 04:08:00 | NOAA-20 | UNIÃO | PIAUÍ | Brasil | 2211100 | 22 | 33 | nan | nan | nan | Cerrado | 8.5 |
| c829a346-d31d-3f5b-95ff-c32654584ac3 | -3.96489 | -50.71458 | 2026-09-27 04:08:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 1478b366-259e-3374-8349-122f2234dbb7 | -7.37479 | -42.10539 | 2026-09-27 04:08:00 | NOAA-20 | COLÔNIA DO PIAUÍ | PIAUÍ | Brasil | 2202778 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 5e33c8ee-5c19-321a-bd9b-87813756c05b | -3.18633 | -51.03855 | 2026-09-27 04:08:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| d2e4ba23-8c39-33b7-966d-bc13a74893a4 | -7.22467 | -44.62575 | 2026-09-27 04:08:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| a312a930-95e9-3750-86a1-f64af214a144 | -10.92981 | -43.86783 | 2026-09-27 04:08:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 040650bc-564d-3bc9-b642-b8b3dfbdc243 | -7.34373 | -42.08146 | 2026-09-27 04:08:00 | NOAA-20 | COLÔNIA DO PIAUÍ | PIAUÍ | Brasil | 2202778 | 22 | 33 | nan | nan | nan | Caatinga | 3.8 |
| 34f54f53-1211-3ad2-b4fa-e166a8227268 | -8.36871 | -44.15094 | 2026-09-27 04:08:00 | NOAA-20 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| a4054b1f-14ad-340d-aea1-60d26ecdf007 | -7.3702 | -42.1122 | 2026-09-27 04:08:00 | NOAA-20 | COLÔNIA DO PIAUÍ | PIAUÍ | Brasil | 2202778 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| dc2f1465-02a6-305f-be76-dfe6290e2bf5 | -5.13414 | -42.85847 | 2026-09-27 04:08:00 | NOAA-20 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| fc9993ec-f42a-3252-8ee7-09264fc89b53 | -8.1545 | -44.45075 | 2026-09-27 04:08:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| d060f4b7-c03e-3d5b-9a8e-704edeb0f14a | -5.26636 | -48.37784 | 2026-09-27 04:08:00 | NOAA-20 | SÃO SEBASTIÃO DO TOCANTINS | TOCANTINS | Brasil | 1720309 | 17 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 69c5b459-beb2-3f7c-ae33-3dcceca1d17c | -8.35766 | -44.14906 | 2026-09-27 04:08:00 | NOAA-20 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 14.5 |
| f909f14a-c62b-38aa-b8d0-85506770e363 | -7.06023 | -42.82594 | 2026-09-27 04:08:00 | NOAA-20 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 40f57171-5001-352a-bfa1-ada9e894e1d0 | -4.29017 | -48.62623 | 2026-09-27 04:08:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 54a7fa43-68ee-3dce-a9b8-9a0604a288d6 | -3.87237 | -52.29216 | 2026-09-27 04:08:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 114bef1c-8af0-3811-9ed6-b5708be5659c | -10.01962 | -50.14348 | 2026-09-27 04:08:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| c2dd0582-0b27-3171-95d7-2db1682345b3 | -8.35986 | -44.15843 | 2026-09-27 04:08:00 | NOAA-20 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 94.2 |
| d71b6fde-707e-3287-ba24-790caa1dc6fa | -7.32833 | -42.09032 | 2026-09-27 04:08:00 | NOAA-20 | COLÔNIA DO PIAUÍ | PIAUÍ | Brasil | 2202778 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| b037f383-3f46-3f33-94b3-fe77b11ca176 | -8.3401 | -44.17019 | 2026-09-27 04:08:00 | NOAA-20 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 5.0 |
| f792870b-9498-3674-ad30-c8591572a0b7 | -8.34893 | -44.16255 | 2026-09-27 04:08:00 | NOAA-20 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 2a0d9865-197e-3f8d-a385-628e5a962d0c | -8.34668 | -44.15314 | 2026-09-27 04:08:00 | NOAA-20 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 2.7 |
| d4576f64-18fb-3fad-bcfd-03b312f5a45d | -8.35104 | -44.14344 | 2026-09-27 04:08:00 | NOAA-20 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 34aef123-555e-3fd8-8536-84c23fe62e43 | -6.83643 | -43.517 | 2026-09-27 04:08:00 | NOAA-20 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 8eb16b32-3c1f-32a5-96e6-3c2aa4b40e4b | -8.34881 | -44.15654 | 2026-09-27 04:08:00 | NOAA-20 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 4.4 |
| ced69d71-7ce2-3078-be2e-334ec6a401fa | -7.35512 | -42.07578 | 2026-09-27 04:08:00 | NOAA-20 | COLÔNIA DO PIAUÍ | PIAUÍ | Brasil | 2202778 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| e12e001c-aa1a-306f-b7d2-cc4a7462129d | -8.34082 | -44.16576 | 2026-09-27 04:08:00 | NOAA-20 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 675524fb-8f7a-3319-899b-2fd2f1257d79 | -6.04499 | -53.60561 | 2026-09-27 04:08:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 309a6732-adec-35cf-9bcf-341695f70c18 | -7.20196 | -40.12063 | 2026-09-27 04:08:00 | NOAA-20 | ARARIPE | CEARÁ | Brasil | 2301307 | 23 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 68824095-6860-3532-9598-5fe3930344ca | -4.28217 | -44.59164 | 2026-09-27 04:08:00 | NOAA-20 | SÃO LUÍS GONZAGA DO MARANHÃO | MARANHÃO | Brasil | 2111409 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| dd2ab734-4922-38e3-9a06-7607da89c49d | -8.35249 | -44.15717 | 2026-09-27 04:08:00 | NOAA-20 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 956b7cd6-9cdc-35e0-820d-7dcb50d93f36 | -7.9595 | -34.88443 | 2026-09-27 04:08:00 | NOAA-20 | PAULISTA | PERNAMBUCO | Brasil | 2610707 | 26 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |


[Clique aqui para ver as próximas entradas](README14.md)
