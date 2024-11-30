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

## Dados Diários - Página 14

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 2031b180-108c-3b3c-942e-b99fe1b7fa68 | -3.98226 | -41.50961 | 2024-11-30 03:21:00 | NPP-375D | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 4.1 |
| ceb14bef-72da-3657-a3ca-83ee54b26337 | -4.85776 | -41.30027 | 2024-11-30 03:21:00 | NPP-375D | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 3.3 |
| 9fb6c9d2-daff-310a-94cf-97573cd1b9d4 | -4.3609 | -43.70087 | 2024-11-30 03:21:00 | NPP-375D | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 96422890-e9bd-3890-aa9a-2b3532957f48 | -4.95505 | -37.03665 | 2024-11-30 03:21:00 | NPP-375D | AREIA BRANCA | RIO GRANDE DO NORTE | Brasil | 2401107 | 24 | 33 | nan | nan | nan | Caatinga | 1.0 |
| d0db042f-02e1-3d89-b3c2-092d89ed71c1 | -4.87145 | -41.28762 | 2024-11-30 03:21:00 | NPP-375D | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 10.8 |
| a1221703-6315-3d16-a9ac-31f2d59880ee | -6.78612 | -39.44793 | 2024-11-30 03:21:00 | NPP-375D | CARIÚS | CEARÁ | Brasil | 2303303 | 23 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 69f04d2b-c739-3458-af9b-b16d932f7536 | -6.90589 | -43.54581 | 2024-11-30 03:21:00 | NPP-375D | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 63.2 |
| 7ed92ac8-4779-31f1-a254-e88edbca6b1d | -3.98889 | -41.52175 | 2024-11-30 03:21:00 | NPP-375D | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 5.7 |
| 57d75348-a7b4-3a47-9875-5bd5a4d36e8c | -4.87579 | -41.2987 | 2024-11-30 03:21:00 | NPP-375D | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 5.6 |
| 14941284-c7a8-3d88-a80b-b31882edbc21 | -3.97419 | -41.5188 | 2024-11-30 03:21:00 | NPP-375D | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 7.6 |
| b42cc7f8-763a-3936-8ec7-0e44545f10cc | -3.98857 | -41.51069 | 2024-11-30 03:21:00 | NPP-375D | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 6e923e59-c4e9-3b3c-b93a-911aa38d70c6 | -6.93543 | -42.84115 | 2024-11-30 03:21:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 2.8 |
| a4cf757c-7b67-3ff9-b65c-708d88c13d74 | -4.8787 | -41.28904 | 2024-11-30 03:21:00 | NPP-375D | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 10.1 |
| 23e6749f-33bf-3e62-acc7-396390d86b9e | -4.86374 | -41.3023 | 2024-11-30 03:21:00 | NPP-375D | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 8.4 |
| 63b403a7-0755-3161-ab9e-96d6d6b63aad | -7.21697 | -39.0522 | 2024-11-30 03:21:00 | NPP-375D | MILAGRES | CEARÁ | Brasil | 2308302 | 23 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 01aebc6d-dd69-3ac5-b7ea-c72008451c2a | -4.87564 | -41.30679 | 2024-11-30 03:21:00 | NPP-375D | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 8.2 |
| 93455be6-f3f5-3fd4-a84b-2883a2143381 | -6.91861 | -43.54736 | 2024-11-30 03:21:00 | NPP-375D | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 80.7 |
| 47d797bb-5351-3670-aff1-49f00b13515f | -5.94723 | -39.6636 | 2024-11-30 03:21:00 | NPP-375D | MOMBAÇA | CEARÁ | Brasil | 2308500 | 23 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 4a8611a9-c0a1-37dd-af0c-85ccdeda2549 | -6.84762 | -38.79535 | 2024-11-30 03:21:00 | NPP-375D | IPAUMIRIM | CEARÁ | Brasil | 2305704 | 23 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 441a66aa-e004-3d59-8e62-f5488ab92290 | -7.16563 | -38.71068 | 2024-11-30 03:21:00 | NPP-375D | BARRO | CEARÁ | Brasil | 2302008 | 23 | 33 | nan | nan | nan | Caatinga | 4.4 |
| f4024e17-7b14-3741-9438-eac5fcb09209 | -4.87823 | -41.28509 | 2024-11-30 03:21:00 | NPP-375D | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 10.8 |
| 14c46757-3efa-302a-a3ab-ad66430761c5 | -4.70301 | -42.38365 | 2024-11-30 03:21:00 | NPP-375D | JOSÉ DE FREITAS | PIAUÍ | Brasil | 2205508 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 78125467-67a0-3e1f-b605-94b7f53788c0 | -6.84816 | -38.7923 | 2024-11-30 03:21:00 | NPP-375D | IPAUMIRIM | CEARÁ | Brasil | 2305704 | 23 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 57d8f58c-3dcd-3a80-8c69-95ead4b87cb2 | -7.16502 | -38.71319 | 2024-11-30 03:21:00 | NPP-375D | BARRO | CEARÁ | Brasil | 2302008 | 23 | 33 | nan | nan | nan | Caatinga | 5.3 |
| 0d751adb-916b-3408-af95-d6adc30e5736 | -3.9744 | -41.53007 | 2024-11-30 03:21:00 | NPP-375D | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 9.3 |
| 140f4a02-ee9e-300c-b28b-8fc19db8da52 | -4.87506 | -41.27348 | 2024-11-30 03:21:00 | NPP-375D | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 10.9 |
| 7560bb2b-a5a4-3be8-96a0-11409b478514 | -4.86754 | -41.31694 | 2024-11-30 03:21:00 | NPP-375D | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 6.3 |
| 352bf170-5943-3ab5-ab71-093417689caa | -6.24537 | -39.86019 | 2024-11-30 03:21:00 | NPP-375D | CATARINA | CEARÁ | Brasil | 2303600 | 23 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 83038f91-4775-36e6-87f0-8a2aa505b259 | -6.13502 | -43.94758 | 2024-11-30 03:21:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 5.6 |
| a593ec89-5aba-38fa-a70e-37657832ef93 | -6.99782 | -35.25331 | 2024-11-30 03:21:00 | NPP-375D | SAPÉ | PARAÍBA | Brasil | 2515302 | 25 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| 4dda56a5-a15f-3838-8ed2-34ddbc58dc22 | -7.49998 | -34.88093 | 2024-11-30 03:21:00 | NPP-375D | CAAPORÃ | PARAÍBA | Brasil | 2503001 | 25 | 33 | nan | nan | nan | Mata Atlântica | 2.4 |
| 710d8461-ddc7-3fa0-abd1-176e061c401b | -7.21755 | -39.04899 | 2024-11-30 03:21:00 | NPP-375D | MILAGRES | CEARÁ | Brasil | 2308302 | 23 | 33 | nan | nan | nan | Caatinga | 1.2 |
| a8fc72e0-d65e-3c40-9269-ef5705613af4 | -6.91148 | -43.55339 | 2024-11-30 03:21:00 | NPP-375D | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 61.6 |
| 8f302cab-94ea-3c2d-8784-df178585ed55 | -4.88321 | -41.2996 | 2024-11-30 03:21:00 | NPP-375D | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 8.7 |
| 5e0e4be8-2c0b-3465-a2f6-ac600fe34af5 | -7.88106 | -37.34802 | 2024-11-30 03:21:00 | NPP-375D | IGUARACY | PERNAMBUCO | Brasil | 2606903 | 26 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 338bfb57-5586-3a6a-8bc1-3fe1034099dd | -6.21176 | -44.50483 | 2024-11-30 03:21:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 53e6e249-c7d0-326f-aa78-e4c07dc72e5b | -6.91064 | -43.55243 | 2024-11-30 03:21:00 | NPP-375D | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 80.7 |
| e6428cd5-1db1-3398-aad0-5362787759d2 | -3.99609 | -41.5178 | 2024-11-30 03:21:00 | NPP-375D | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 3.3 |
| e79741c6-8256-3fa8-a3a0-035e7e2a71e9 | -4.87231 | -41.28285 | 2024-11-30 03:21:00 | NPP-375D | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 10.8 |
| b86b5e77-c7e2-3925-9017-1a8ba972afc8 | -6.91829 | -43.55465 | 2024-11-30 03:21:00 | NPP-375D | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 45.4 |
| 33bcfc5e-879f-3064-9421-31578a38c9ee | -6.9163 | -43.55992 | 2024-11-30 03:21:00 | NPP-375D | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 23.0 |
| a7a2b7a6-fe3f-3105-b131-133595165c45 | -4.87272 | -41.28699 | 2024-11-30 03:21:00 | NPP-375D | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 8.8 |
| 1fec31a9-a093-3cf2-b33b-cf6cc8242bbb | -6.67443 | -39.70589 | 2024-11-30 03:21:00 | NPP-375D | TARRAFAS | CEARÁ | Brasil | 2313252 | 23 | 33 | nan | nan | nan | Caatinga | 1.1 |
| b9303790-c688-3690-a2b3-f9adb6a45c55 | -3.96875 | -41.51259 | 2024-11-30 03:21:00 | NPP-375D | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 3.5 |
| 242a3ca9-d5bd-3637-9326-2a614154a8b5 | -6.92424 | -43.55503 | 2024-11-30 03:21:00 | NPP-375D | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 66e54ee3-ee53-3ac5-b93f-655ef089cfda | -6.99385 | -35.25265 | 2024-11-30 03:21:00 | NPP-375D | SAPÉ | PARAÍBA | Brasil | 2515302 | 25 | 33 | nan | nan | nan | Mata Atlântica | 2.7 |
| d2e1049b-9d81-311f-96fc-0ea05ec1b91e | -3.97877 | -41.53011 | 2024-11-30 03:21:00 | NPP-375D | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 4.3 |
| fb2500d4-7a77-3075-8186-b312cb3de00c | -6.99624 | -35.24934 | 2024-11-30 03:21:00 | NPP-375D | SAPÉ | PARAÍBA | Brasil | 2515302 | 25 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| 760e736f-d491-3bb1-bc5e-56a9a7d7e6bd | -3.62399 | -42.73792 | 2024-11-30 03:21:00 | NPP-375D | BREJO | MARANHÃO | Brasil | 2102101 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 8f85fbc8-dd07-3307-aa64-3dee2d52b90b | -4.84902 | -41.31416 | 2024-11-30 03:21:00 | NPP-375D | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 3.3 |
| 77d9e423-a815-33b4-a058-94f6844d7147 | -7.49916 | -34.88571 | 2024-11-30 03:21:00 | NPP-375D | CAAPORÃ | PARAÍBA | Brasil | 2503001 | 25 | 33 | nan | nan | nan | Mata Atlântica | 3.5 |
| 2c312b95-a676-3496-8629-096f918e4e33 | -6.2132 | -39.85165 | 2024-11-30 03:21:00 | NPP-375D | CATARINA | CEARÁ | Brasil | 2303600 | 23 | 33 | nan | nan | nan | Caatinga | 0.4 |
| 13a0bfec-41dd-3b90-a668-6e82228d9764 | -6.91744 | -43.55371 | 2024-11-30 03:21:00 | NPP-375D | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 80.7 |
| e6f08d27-d1f9-31d9-94a1-66ff9f943f3a | -4.87741 | -41.28967 | 2024-11-30 03:21:00 | NPP-375D | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 10.8 |
| 3f44274e-98d1-3297-a29e-7b8a212db80a | -3.98978 | -41.51671 | 2024-11-30 03:21:00 | NPP-375D | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 3.3 |
| cc5ddb86-a12a-3da2-b56d-4be406c573e5 | -6.23994 | -39.85891 | 2024-11-30 03:21:00 | NPP-375D | CATARINA | CEARÁ | Brasil | 2303600 | 23 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 0e626fd2-9996-3acc-9354-f0306daef053 | -3.967 | -41.52287 | 2024-11-30 03:21:00 | NPP-375D | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 4.3 |
| 3a7cef2b-9a55-3abb-bc71-ae4af8da036a | -4.69547 | -42.38803 | 2024-11-30 03:21:00 | NPP-375D | JOSÉ DE FREITAS | PIAUÍ | Brasil | 2205508 | 22 | 33 | nan | nan | nan | Caatinga | 3.3 |
| 52cb987a-9e04-3846-b6a1-919b5a6a49df | -6.94296 | -42.8369 | 2024-11-30 03:21:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| e29739a1-239a-3d9a-b5d6-83f7f430b267 | -4.86966 | -41.30473 | 2024-11-30 03:21:00 | NPP-375D | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 8.4 |
| 8a3b773d-28b5-3b50-9f4f-f0316df36929 | -4.03969 | -41.91219 | 2024-11-30 03:21:00 | NPP-375D | BRASILEIRA | PIAUÍ | Brasil | 2201960 | 22 | 33 | nan | nan | nan | Caatinga | 2.7 |
| 995ee175-d123-3549-aea6-c4fa67356a36 | -4.86978 | -41.26747 | 2024-11-30 03:21:00 | NPP-375D | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 10.9 |
| debb7d1b-c6ad-39ee-8fa8-42d553bc81e1 | -4.82802 | -41.25332 | 2024-11-30 03:21:00 | NPP-375D | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 7de480ab-c94f-394c-9f79-40fb77912add | -4.86792 | -41.2721 | 2024-11-30 03:21:00 | NPP-375D | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 9.0 |
| 932db675-5042-3d9b-b72c-40a74be3c2c2 | -3.99488 | -41.51176 | 2024-11-30 03:21:00 | NPP-375D | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 2648acaf-5560-3eb9-a9ed-496e5b8cfcd6 | -4.8779 | -41.29366 | 2024-11-30 03:21:00 | NPP-375D | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 10.1 |
| e6b95ae1-cdc2-364f-8b3d-b626e7769128 | -4.8729 | -41.32265 | 2024-11-30 03:21:00 | NPP-375D | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 5.5 |
| 3375820a-8bf1-3411-b33e-c5c1c09b509d | -4.8736 | -41.31855 | 2024-11-30 03:21:00 | NPP-375D | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 4.6 |
| b2def3b2-69c6-32b9-a783-2e46c484c2a4 | -3.9699 | -41.51876 | 2024-11-30 03:21:00 | NPP-375D | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 6.6 |
| d01c0d2c-df54-313c-87cc-b4452c4c6a0a | -3.96898 | -41.5239 | 2024-11-30 03:21:00 | NPP-375D | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 6.6 |
| 0e9691aa-d47b-3cb6-97c0-4b3a449a0908 | -6.91389 | -43.54082 | 2024-11-30 03:21:00 | NPP-375D | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 63.2 |
| c6224c4f-bd0a-3aaf-a8da-7b9cada14fff | -4.70055 | -42.38298 | 2024-11-30 03:21:00 | NPP-375D | JOSÉ DE FREITAS | PIAUÍ | Brasil | 2205508 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| c05c255c-0808-33a4-956f-062f35d38460 | -7.22209 | -39.05301 | 2024-11-30 03:21:00 | NPP-375D | MILAGRES | CEARÁ | Brasil | 2308302 | 23 | 33 | nan | nan | nan | Caatinga | 1.2 |
| b396621c-c5d0-3f9d-938e-c4dc93a05493 | -4.85528 | -41.31456 | 2024-11-30 03:21:00 | NPP-375D | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 3.3 |
| f04ec4b1-1d9f-37eb-aa1e-ce55ec8f58db | -4.86906 | -41.27158 | 2024-11-30 03:21:00 | NPP-375D | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 10.9 |
| 148ef652-46ca-30f3-98c0-8d5475e6837b | -6.28754 | -39.59037 | 2024-11-30 03:21:00 | NPP-375D | ACOPIARA | CEARÁ | Brasil | 2300309 | 23 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 1c7edf3d-ea03-3c3c-9e1a-b2ae26f55168 | -6.93646 | -42.83551 | 2024-11-30 03:21:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 3915c710-ca54-3c04-975a-54f6197686e8 | -4.85618 | -41.30936 | 2024-11-30 03:21:00 | NPP-375D | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 3.3 |
| 84c32cb7-efb3-3adc-8f70-28fc499ebcf5 | -4.87426 | -41.31475 | 2024-11-30 03:21:00 | NPP-375D | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 4.6 |
| cb50de4d-2d32-3198-a300-53a4ffe10f11 | -5.9466 | -39.66718 | 2024-11-30 03:21:00 | NPP-375D | MOMBAÇA | CEARÁ | Brasil | 2308500 | 23 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 38b14150-5667-3284-bf56-45ab561b14ef | -4.36209 | -43.69408 | 2024-11-30 03:21:00 | NPP-375D | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 1dc0857a-7b78-3f64-b96d-96059c47463c | -6.9195 | -43.54833 | 2024-11-30 03:21:00 | NPP-375D | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 60.8 |
| b39e635b-df6a-3a7c-8258-4a0d6cf7e13f | -4.87426 | -41.30721 | 2024-11-30 03:21:00 | NPP-375D | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 10.5 |
| 73b6e877-03c3-30b0-b36f-5cc5ead6a8ec | -4.85718 | -41.29648 | 2024-11-30 03:21:00 | NPP-375D | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 3.3 |
| ab993f4e-729b-3910-94e5-375ea131aa92 | -6.90501 | -43.54481 | 2024-11-30 03:21:00 | NPP-375D | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 326bc47e-c926-3e9b-90b3-496b2545fa76 | -4.88183 | -41.30032 | 2024-11-30 03:21:00 | NPP-375D | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 11.8 |
| e5ae7824-0e8e-3363-8c96-c144b7eaaa65 | -6.67894 | -39.26273 | 2024-11-30 03:21:00 | NPP-375D | VÁRZEA ALEGRE | CEARÁ | Brasil | 2314003 | 23 | 33 | nan | nan | nan | Caatinga | 0.4 |
| c2c8024c-edc4-3468-b631-c691e80f5c5f | -4.86707 | -44.00869 | 2024-11-30 03:21:00 | NPP-375D | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 6895c62a-bddc-31c0-8f32-33463e6deb31 | -6.94416 | -42.78588 | 2024-11-30 03:21:00 | NPP-375D | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 4.2 |
| 95cb4728-144a-3bc0-8a2d-6c147cb2a4bf | -3.99403 | -41.51682 | 2024-11-30 03:21:00 | NPP-375D | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 3.4 |
| 1ce7fe3e-78ac-39d9-9e11-45ae884e97ec | -6.40017 | -35.03339 | 2024-11-30 03:21:00 | NPP-375D | BAÍA FORMOSA | RIO GRANDE DO NORTE | Brasil | 2401404 | 24 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| ff1d58eb-4490-37ab-a303-4d24933fb6fe | -5.93387 | -43.78662 | 2024-11-30 03:21:00 | NPP-375D | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 6.2 |
| d99f013e-e0c1-36df-a940-fdbe59b302ac | -6.2138 | -39.84814 | 2024-11-30 03:21:00 | NPP-375D | CATARINA | CEARÁ | Brasil | 2303600 | 23 | 33 | nan | nan | nan | Caatinga | 0.4 |
| f802658b-2289-36f4-bedd-33593797fc5c | -3.97804 | -41.50957 | 2024-11-30 03:21:00 | NPP-375D | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 3.4 |
| 02fe97e9-3e40-3a2b-bcbd-06482e1aab81 | -4.68844 | -42.37487 | 2024-11-30 03:21:00 | NPP-375D | JOSÉ DE FREITAS | PIAUÍ | Brasil | 2205508 | 22 | 33 | nan | nan | nan | Caatinga | 3.6 |
| f5957e13-9a0d-34de-a73d-aec7e95afea3 | -4.86303 | -41.30642 | 2024-11-30 03:21:00 | NPP-375D | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 8.4 |
| 3efc7976-071a-3b40-9582-daf4e1d67ea1 | -4.8683 | -41.30509 | 2024-11-30 03:21:00 | NPP-375D | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 10.5 |
| b62327db-f1a8-327c-a3f7-74bf49678cd1 | -6.79081 | -39.45233 | 2024-11-30 03:21:00 | NPP-375D | VÁRZEA ALEGRE | CEARÁ | Brasil | 2314003 | 23 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 0e88072a-051b-3b63-9466-7fc1fda39e7a | -3.97243 | -41.52911 | 2024-11-30 03:21:00 | NPP-375D | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 4.3 |
| 05175964-76b4-36b2-99a0-46768212c8bc | -3.98435 | -41.51063 | 2024-11-30 03:21:00 | NPP-375D | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 3.4 |


[Clique aqui para ver as próximas entradas](README15.md)
