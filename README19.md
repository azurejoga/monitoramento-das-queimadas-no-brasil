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
| ee676d02-2930-34e1-9e27-218ccd6a988f | -5.65815 | -39.07282 | 2024-12-23 12:46:00 | TERRA_M-T | SOLONÓPOLE | CEARÁ | Brasil | 2313005 | 23 | 33 | nan | nan | nan | Caatinga | 37.3 |
| d3833f1f-df9a-30d2-913b-a0ac71b24d54 | -0.78111 | -48.79167 | 2024-12-23 12:46:00 | TERRA_M-T | CACHOEIRA DO ARARI | PARÁ | Brasil | 1502004 | 15 | 33 | nan | nan | nan | Amazônia | 18.2 |
| 0fc536c2-f391-3973-ba9c-3bb95941a0bb | -0.97784 | -47.55547 | 2024-12-23 12:46:00 | TERRA_M-T | MARACANÃ | PARÁ | Brasil | 1504307 | 15 | 33 | nan | nan | nan | Amazônia | 32.7 |
| 0559ee1d-c9f6-3c62-a0ad-53f156d51969 | -2.34125 | -45.57875 | 2024-12-23 12:46:00 | TERRA_M-T | TURILÂNDIA | MARANHÃO | Brasil | 2112456 | 21 | 33 | nan | nan | nan | Amazônia | 12.1 |
| 2bb8171a-3cd8-3b22-8538-4263667065e2 | -2.10091 | -45.32527 | 2024-12-23 12:46:00 | TERRA_M-T | TURILÂNDIA | MARANHÃO | Brasil | 2112456 | 21 | 33 | nan | nan | nan | Amazônia | 28.2 |
| 8c0aba19-8adb-31ef-9626-5a2d19551b1d | -3.87222 | -42.0281 | 2024-12-23 12:46:00 | TERRA_M-T | ESPERANTINA | PIAUÍ | Brasil | 2203701 | 22 | 33 | nan | nan | nan | Caatinga | 25.1 |
| f2f137e7-2c97-3fdd-aa7e-8d15dbedb3db | -4.15379 | -43.6361 | 2024-12-23 12:46:00 | TERRA_M-T | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 23.1 |
| 207c3257-2508-3e93-9402-05afcec63b62 | -5.34913 | -42.12383 | 2024-12-23 12:46:00 | TERRA_M-T | ALTO LONGÁ | PIAUÍ | Brasil | 2200301 | 22 | 33 | nan | nan | nan | Caatinga | 31.6 |
| bbec17fe-7d60-336a-b79f-7daf5cd5121b | -4.39061 | -43.11286 | 2024-12-23 12:46:00 | TERRA_M-T | COELHO NETO | MARANHÃO | Brasil | 2103406 | 21 | 33 | nan | nan | nan | Cerrado | 19.4 |
| 2b26bdd7-008c-33de-b67a-63aa2409f188 | -1.36082 | -53.70971 | 2024-12-23 12:46:00 | TERRA_M-T | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 59.5 |
| 75ecaa39-7048-3b7e-9c06-051a217ca1bb | -0.22303 | -51.60619 | 2024-12-23 12:46:00 | TERRA_M-T | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 12.8 |
| 531e0b72-2e32-3ed9-8262-95fe172e4a5b | -2.79901 | -46.76134 | 2024-12-23 12:46:00 | TERRA_M-T | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 4303fdbd-5e58-32ca-b79a-215cb08bd1b7 | -2.46395 | -45.80458 | 2024-12-23 12:46:00 | TERRA_M-T | SANTA LUZIA DO PARUÁ | MARANHÃO | Brasil | 2110039 | 21 | 33 | nan | nan | nan | Amazônia | 7.3 |
| c77e9f56-d141-3a8d-83d1-af6da971044c | -11.45038 | -43.82367 | 2024-12-23 12:48:00 | TERRA_M-T | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 25.8 |
| 3e75d03c-e446-301a-bf30-4cd54d6876fc | -9.27611 | -43.47399 | 2024-12-23 12:48:00 | TERRA_M-T | CAMPO ALEGRE DE LOURDES | BAHIA | Brasil | 2905909 | 29 | 33 | nan | nan | nan | Caatinga | 29.8 |
| 8c9cc546-d99f-3904-ba6c-e204b8ceebe0 | -8.66648 | -44.16542 | 2024-12-23 12:48:00 | TERRA_M-T | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 21.7 |
| d31f76b2-e956-35e7-b1e5-9bffe6b804bd | -9.21221 | -48.13966 | 2024-12-23 12:48:00 | TERRA_M-T | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | 7.2 |
| 1795241a-a6d3-374a-80d8-788a175a09e9 | -8.8038 | -49.79231 | 2024-12-23 12:48:00 | TERRA_M-T | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 14.5 |
| 4234bf24-2434-34dc-92f6-c4569cd68f58 | -8.80252 | -49.80118 | 2024-12-23 12:48:00 | TERRA_M-T | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 12.2 |
| 0d859556-8f78-3448-bf1e-c8121243b4d7 | -9.21488 | -48.12028 | 2024-12-23 12:48:00 | TERRA_M-T | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | 7.8 |
| 6cf9a755-914d-3b5e-968a-b447b3080328 | -8.02601 | -43.44725 | 2024-12-23 12:48:00 | TERRA_M-T | PAVUSSU | PIAUÍ | Brasil | 2207850 | 22 | 33 | nan | nan | nan | Cerrado | 21.5 |
| 4f5de24d-4101-3eb1-9717-9f3e0e3740e5 | -6.32577 | -45.98211 | 2024-12-23 12:48:00 | TERRA_M-T | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 13.5 |
| abc1a7d7-899a-3cc7-b634-fa89dd27b586 | -11.46329 | -43.82523 | 2024-12-23 12:48:00 | TERRA_M-T | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 24.8 |
| bee8cd97-dffb-3255-a2c2-3d658393d981 | -12.69526 | -46.76285 | 2024-12-23 12:50:00 | TERRA_M-T | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 12.1 |
| efd9f03d-92c7-39e9-8135-ed9bae73b62d | -21.71939 | -54.28863 | 2024-12-23 12:53:00 | TERRA_M-T | RIO BRILHANTE | MATO GROSSO DO SUL | Brasil | 5007208 | 50 | 33 | nan | nan | nan | Mata Atlântica | 8.9 |
| 9dfee6db-5689-3a87-b06e-740774ee7a85 | -19.93462 | -50.55843 | 2024-12-23 12:53:00 | TERRA_M-T | POPULINA | SÃO PAULO | Brasil | 3540408 | 35 | 33 | nan | nan | nan | Mata Atlântica | 7.4 |
| c2404771-75ac-302f-a412-2cea033d186e | -19.26637 | -50.80873 | 2024-12-23 12:53:00 | TERRA_M-T | ITARUMÃ | GOIÁS | Brasil | 5211305 | 52 | 33 | nan | nan | nan | Mata Atlântica | 9.7 |
| 84b3f049-dfc9-3f84-a069-324622672407 | -17.61568 | -50.1609 | 2024-12-23 12:53:00 | TERRA_M-T | TURVELÂNDIA | GOIÁS | Brasil | 5221551 | 52 | 33 | nan | nan | nan | Cerrado | 9.1 |
| 15e4cdad-a45e-3b2d-aba1-f5bd091a8366 | -20.07186 | -51.43753 | 2024-12-23 12:53:00 | TERRA_M-T | APARECIDA DO TABOADO | MATO GROSSO DO SUL | Brasil | 5001003 | 50 | 33 | nan | nan | nan | Cerrado | 9.8 |
| 34482178-bbf5-344a-97ee-b34abb1bc9bb | -23.1102 | -50.37109 | 2024-12-23 12:53:00 | TERRA_M-T | BANDEIRANTES | PARANÁ | Brasil | 4102406 | 41 | 33 | nan | nan | nan | Mata Atlântica | 7.5 |
| cd836bad-5204-3bf6-8b30-098bb12e859c | -21.90062 | -50.08794 | 2024-12-23 12:53:00 | TERRA_M-T | POMPÉIA | SÃO PAULO | Brasil | 3540002 | 35 | 33 | nan | nan | nan | Mata Atlântica | 6.2 |
| 76276f92-a90d-39c2-9764-93e3dddcb39c | -20.74335 | -54.99049 | 2024-12-23 12:53:00 | TERRA_M-T | TERENOS | MATO GROSSO DO SUL | Brasil | 5008008 | 50 | 33 | nan | nan | nan | Cerrado | 11.2 |
| 6fe5cff3-a019-342b-b566-e74b7f8d8122 | -20.1091 | -50.36255 | 2024-12-23 12:53:00 | TERRA_M-T | FERNANDÓPOLIS | SÃO PAULO | Brasil | 3515509 | 35 | 33 | nan | nan | nan | Mata Atlântica | 9.4 |
| db68f04f-04de-35b9-a8c4-03e3afe7a259 | -21.67262 | -54.35751 | 2024-12-23 12:53:00 | TERRA_M-T | RIO BRILHANTE | MATO GROSSO DO SUL | Brasil | 5007208 | 50 | 33 | nan | nan | nan | Mata Atlântica | 8.1 |
| 69c8f603-6f29-3323-b1d9-feeeaabc1971 | -21.6642 | -54.04706 | 2024-12-23 12:53:00 | TERRA_M-T | NOVA ALVORADA DO SUL | MATO GROSSO DO SUL | Brasil | 5006002 | 50 | 33 | nan | nan | nan | Cerrado | 9.4 |
| 1fe71d46-6461-3766-aecf-e26df8603667 | -20.46708 | -45.42943 | 2024-12-23 12:53:00 | TERRA_M-T | FORMIGA | MINAS GERAIS | Brasil | 3126109 | 31 | 33 | nan | nan | nan | Mata Atlântica | 16.6 |
| 0c513628-0cc1-3cd4-a258-8efbfa6d7a29 | -19.39557 | -51.53225 | 2024-12-23 12:53:00 | TERRA_M-T | PARANAÍBA | MATO GROSSO DO SUL | Brasil | 5006309 | 50 | 33 | nan | nan | nan | Cerrado | 8.1 |
| 5b4aeeb9-5b61-30ea-ba47-7a38b861f75c | -21.08028 | -50.85942 | 2024-12-23 12:53:00 | TERRA_M-T | VALPARAÍSO | SÃO PAULO | Brasil | 3556305 | 35 | 33 | nan | nan | nan | Mata Atlântica | 8.7 |
| cd0877b5-d2e6-3ffe-9ed6-5fe5dddfec99 | -18.9106 | -51.96681 | 2024-12-23 12:53:00 | TERRA_M-T | APORÉ | GOIÁS | Brasil | 5201504 | 52 | 33 | nan | nan | nan | Cerrado | 7.4 |
| 79ed3166-4f2b-36a4-b6b8-8165039edc6c | -29.50979 | -51.3991 | 2024-12-23 12:55:00 | TERRA_M-T | TUPANDI | RIO GRANDE DO SUL | Brasil | 4322251 | 43 | 33 | nan | nan | nan | Mata Atlântica | 6.0 |
| 77f46b4c-b505-3c95-a89a-34a391ae6f68 | -29.23083 | -51.703 | 2024-12-23 12:55:00 | TERRA_M-T | CORONEL PILAR | RIO GRANDE DO SUL | Brasil | 4305934 | 43 | 33 | nan | nan | nan | Mata Atlântica | 13.1 |
| 8a36e0c2-cfec-3c70-9833-e72f10c87a2c | -29.57114 | -50.79515 | 2024-12-23 12:55:00 | TERRA_M-T | IGREJINHA | RIO GRANDE DO SUL | Brasil | 4310108 | 43 | 33 | nan | nan | nan | Mata Atlântica | 8.8 |
| 9189662e-c916-3643-a9cf-dca5bba3625c | -29.23576 | -52.47742 | 2024-12-23 12:55:00 | TERRA_M-T | BARROS CASSAL | RIO GRANDE DO SUL | Brasil | 4302006 | 43 | 33 | nan | nan | nan | Mata Atlântica | 8.9 |
| 34620167-cdb2-3789-a3f5-0843835c65ac | -29.23435 | -52.48848 | 2024-12-23 12:55:00 | TERRA_M-T | BARROS CASSAL | RIO GRANDE DO SUL | Brasil | 4302006 | 43 | 33 | nan | nan | nan | Mata Atlântica | 8.5 |


