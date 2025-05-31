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

## Dados Diários - Página 8

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 75ebe2dd-6b87-385b-a0ed-34f564691ad9 | -8.10802 | -45.90384 | 2025-05-31 04:25:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 4d200320-0cc4-3870-8bef-8bcf5905bdcf | -6.27709 | -44.20314 | 2025-05-31 04:25:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 9790e2f4-654a-327b-a576-37f9a9bf31e5 | -7.24342 | -43.09669 | 2025-05-31 04:25:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| a81fe891-bf85-353b-9ef6-2887cc0f1c32 | -7.24041 | -43.09184 | 2025-05-31 04:25:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 004bb889-36f7-31a1-bcb2-a33cb395e09b | -9.5351 | -43.21216 | 2025-05-31 04:25:00 | NOAA-21 | CAMPO ALEGRE DE LOURDES | BAHIA | Brasil | 2905909 | 29 | 33 | nan | nan | nan | Caatinga | 0.8 |
| d189677c-22c6-3b66-b5b1-be87571639e7 | -6.4449 | -45.72524 | 2025-05-31 04:25:00 | NOAA-21 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| d1d1c892-2d20-37fa-94bb-f12dbe5b3ade | -6.22114 | -43.34727 | 2025-05-31 04:25:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 52903459-e356-3f16-b3a2-88fc28de3b99 | -8.11519 | -45.90138 | 2025-05-31 04:25:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| ef8032cd-b7d8-35aa-b4eb-43cdaa04f6d1 | -5.83175 | -44.08654 | 2025-05-31 04:25:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| ae46bf07-b809-3978-ae0b-f9c74d25a65e | -7.08606 | -46.04639 | 2025-05-31 04:25:00 | NOAA-21 | FORTALEZA DOS NOGUEIRAS | MARANHÃO | Brasil | 2104107 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| be31911a-439f-3131-9f91-8f90d51128a5 | -6.17974 | -48.06516 | 2025-05-31 04:25:00 | NOAA-21 | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 3e5e3103-3376-3eb2-ab50-e92aca9caa78 | -7.87662 | -45.99269 | 2025-05-31 04:25:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| a90e4457-aadc-3f8c-934d-3b2f98131d82 | -8.67875 | -48.28862 | 2025-05-31 04:25:00 | NOAA-21 | GUARAÍ | TOCANTINS | Brasil | 1709302 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 7ff35bab-4a67-3e67-9f28-e6748eded268 | -6.22176 | -43.34318 | 2025-05-31 04:25:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| b8546d03-8b65-3b6f-b849-c9898300db05 | -3.26418 | -42.54296 | 2025-05-31 04:25:00 | NOAA-21 | SANTANA DO MARANHÃO | MARANHÃO | Brasil | 2110237 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| d6411214-5a59-3142-8a36-50900340fb57 | -6.15254 | -42.61013 | 2025-05-31 04:25:00 | NOAA-21 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 8.7 |
| cc698d61-6efc-355e-b426-1155680991bc | -6.44815 | -45.72969 | 2025-05-31 04:25:00 | NOAA-21 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 28e45ecf-1851-3f55-86de-775d95aafa1c | -6.2247 | -43.34782 | 2025-05-31 04:25:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| c1551144-a876-3fa9-994f-921fe7e96f1c | -8.70743 | -50.03951 | 2025-05-31 04:25:00 | NOAA-21 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| c94d4863-9539-3f6e-8f93-7d4a26d9dc0a | -9.0472 | -47.01734 | 2025-05-31 04:25:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 36373e33-4bbb-3b4b-8a5d-f721c1ef5d46 | -3.04493 | -49.44294 | 2025-05-31 04:25:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 6559b1dd-9166-3a96-8604-899373da9a96 | -7.0091 | -44.6245 | 2025-05-31 04:25:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 9.5 |
| fb06e7cb-264f-3009-a2b1-5b2bcbfb76e1 | -7.58301 | -45.86797 | 2025-05-31 04:25:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 5fc4be28-1eb5-3894-a918-34093dd9090b | -5.85424 | -43.64042 | 2025-05-31 04:25:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 1e80264d-38e9-3aa6-ba78-d03e7e3ab210 | -13.1009 | -52.28771 | 2025-05-31 04:27:00 | NOAA-21 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 3.5 |
| ac859a71-5784-3e63-a047-58707ee44005 | -14.83244 | -48.09962 | 2025-05-31 04:27:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| c91e3a3b-72cb-336e-8cb1-b0155fc5d08c | -13.64424 | -47.44864 | 2025-05-31 04:27:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 33924cf2-0663-34a5-b3f1-fad8233c1a17 | -10.46386 | -47.94319 | 2025-05-31 04:27:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| b559c1d1-5419-3012-87cb-401bd8d6cecb | -10.30252 | -57.13674 | 2025-05-31 04:27:00 | NOAA-21 | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 1e50cb2b-da81-3891-a1e0-8f2d8808a2b8 | -14.06623 | -44.10279 | 2025-05-31 04:27:00 | NOAA-21 | FEIRA DA MATA | BAHIA | Brasil | 2910776 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 5df2890a-a94f-3969-80da-0a433f5b24aa | -12.27147 | -44.5868 | 2025-05-31 04:27:00 | NOAA-21 | CATOLÂNDIA | BAHIA | Brasil | 2907400 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| fc902f82-4581-354d-814d-258c6a71d73b | -9.61046 | -49.0233 | 2025-05-31 04:27:00 | NOAA-21 | ABREULÂNDIA | TOCANTINS | Brasil | 1700251 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| fd664071-9e37-3be6-b298-bc1fbc09f778 | -10.47036 | -51.8906 | 2025-05-31 04:27:00 | NOAA-21 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 38b15281-8f87-3f28-a009-d678854ec6d7 | -12.61509 | -48.17959 | 2025-05-31 04:27:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 517f0485-9cc6-3c2f-9f2d-2f0f9c58c900 | -11.90003 | -47.44436 | 2025-05-31 04:27:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 0defc518-2e58-370a-a66b-44ace55ccb52 | -14.0276 | -55.13616 | 2025-05-31 04:27:00 | NOAA-21 | SANTA RITA DO TRIVELATO | MATO GROSSO | Brasil | 5107768 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 8910cea0-2365-382c-9f9d-2819e03dc7cc | -10.45943 | -47.94968 | 2025-05-31 04:27:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 698fa716-a428-3f2a-a57b-9f8cb2a6fb21 | -11.14398 | -53.94632 | 2025-05-31 04:27:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 65f5c26a-6c92-37ce-8171-8227cf6ebaf1 | -12.49725 | -55.73706 | 2025-05-31 04:27:00 | NOAA-21 | SORRISO | MATO GROSSO | Brasil | 5107925 | 51 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 326f81ac-1cd0-31ba-a7cc-3367e7b2ede4 | -12.19727 | -54.26752 | 2025-05-31 04:27:00 | NOAA-21 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| c778ccd7-bf45-3121-a568-b1ee864c753d | -10.64873 | -49.4277 | 2025-05-31 04:27:00 | NOAA-21 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 34e9171c-f16d-3425-9d9b-e3c3dcfe92ce | -14.67061 | -45.40181 | 2025-05-31 04:27:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 3451678a-682b-3b92-92ab-f87756e81d99 | -13.2629 | -47.25274 | 2025-05-31 04:27:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 94ebe3d5-5cd0-3e0c-82e1-164cda452172 | -12.12494 | -54.59284 | 2025-05-31 04:27:00 | NOAA-21 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 6551e4c1-77d1-3e2c-bbda-91c7ca24281f | -10.73496 | -49.28616 | 2025-05-31 04:27:00 | NOAA-21 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 11.3 |
| c0a8d295-f06d-3353-bfad-ac08ba64617d | -10.05303 | -49.65572 | 2025-05-31 04:27:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| bc574f19-d29c-3d43-bcda-d16196cec758 | -12.3008 | -50.08938 | 2025-05-31 04:27:00 | NOAA-21 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| c5dd8d45-b722-31b6-beb0-e9dc12420f57 | -10.83711 | -54.01818 | 2025-05-31 04:27:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 93386920-fe9f-3a7c-8aa9-33904739f630 | -15.88895 | -43.45362 | 2025-05-31 04:27:00 | NOAA-21 | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 06cdc1a2-d793-3973-a1c0-cc0624baca2c | -13.10334 | -45.286 | 2025-05-31 04:27:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 49e5baea-2c38-3595-94cd-3a8bb291e84e | -12.03227 | -49.52229 | 2025-05-31 04:27:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 60ee7230-691d-3489-b67d-4748718d039d | -12.01743 | -49.52748 | 2025-05-31 04:27:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 8.2 |
| d2b89006-ff4e-3f4f-add5-7b208588e90b | -12.01341 | -49.53066 | 2025-05-31 04:27:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 053d70d1-a71b-3846-8aad-f7b1ed692139 | -14.07564 | -47.64893 | 2025-05-31 04:27:00 | NOAA-21 | ALTO PARAÍSO DE GOIÁS | GOIÁS | Brasil | 5200605 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| b22f5634-bccd-32ec-95fd-c62529a58424 | -14.84545 | -48.29799 | 2025-05-31 04:27:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 9fc26280-9091-3af6-9a6e-ebd1e28197a5 | -11.56631 | -51.36066 | 2025-05-31 04:27:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 7e1add19-a5b9-3365-8b6e-c45e2c2da627 | -11.9137 | -54.81721 | 2025-05-31 04:27:00 | NOAA-21 | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| a323f2d7-d040-337a-a98d-e31aef59df0d | -14.07509 | -47.65247 | 2025-05-31 04:27:00 | NOAA-21 | ALTO PARAÍSO DE GOIÁS | GOIÁS | Brasil | 5200605 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 72eb2b6d-7706-3a10-9dd0-cefb01f7189e | -10.45999 | -47.94617 | 2025-05-31 04:27:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 45828b03-c197-3685-8b91-813f77a2674c | -11.69102 | -49.16036 | 2025-05-31 04:27:00 | NOAA-21 | GURUPI | TOCANTINS | Brasil | 1709500 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 68cfddf0-25dc-303e-9de2-9b68697097dd | -11.31138 | -46.47755 | 2025-05-31 04:27:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 15d64a9a-017b-3eaf-94d6-6530eb449418 | -10.46275 | -47.95021 | 2025-05-31 04:27:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 7582a3b4-409b-3e16-957d-4e33bb7c7427 | -10.30182 | -57.14041 | 2025-05-31 04:27:00 | NOAA-21 | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| e69f6934-4d40-3546-b832-7d14be3f8cce | -9.39366 | -48.42275 | 2025-05-31 04:27:00 | NOAA-21 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 279da9c4-3d9c-3258-be0e-0bcd067de4cb | -12.50289 | -55.18497 | 2025-05-31 04:27:00 | NOAA-21 | VERA | MATO GROSSO | Brasil | 5108501 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| c61c58a0-7130-38c0-ba22-258cb92b98dd | -10.46442 | -47.93968 | 2025-05-31 04:27:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 9f90c467-7f7b-3dbe-87b7-81a0d8e46887 | -11.36095 | -55.1279 | 2025-05-31 04:27:00 | NOAA-21 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 13a8ca61-f95c-36ea-b90e-1bafcb58093f | -12.02607 | -49.51739 | 2025-05-31 04:27:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 10.0 |
| ec024c47-fcb9-3a94-9fbd-2cd0ae946606 | -11.90469 | -54.79176 | 2025-05-31 04:27:00 | NOAA-21 | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| a81b2a0c-e9d3-3173-ab4b-da4124dd7a3c | -11.82676 | -51.26794 | 2025-05-31 04:27:00 | NOAA-21 | SERRA NOVA DOURADA | MATO GROSSO | Brasil | 5107883 | 51 | 33 | nan | nan | nan | Cerrado | 13.8 |
| 3055bdaf-a4f3-39fd-bc74-a4f26b0f9095 | -10.45369 | -47.9411 | 2025-05-31 04:27:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 30d7fe88-9fc9-3750-a75d-35f528028021 | -12.50757 | -55.18585 | 2025-05-31 04:27:00 | NOAA-21 | VERA | MATO GROSSO | Brasil | 5108501 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| f4bc72ba-faed-3ac4-b74a-4a6078376ef3 | -9.99008 | -48.15947 | 2025-05-31 04:27:00 | NOAA-21 | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| e4a44d6f-36a9-31b6-a7d0-9c7f230b25c3 | -11.79086 | -44.28391 | 2025-05-31 04:27:00 | NOAA-21 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| d8a7225a-3f55-35d0-a25a-5781861a2831 | -9.53043 | -54.76884 | 2025-05-31 04:27:00 | NOAA-21 | GUARANTÃ DO NORTE | MATO GROSSO | Brasil | 5104104 | 51 | 33 | nan | nan | nan | Amazônia | 3.4 |
| f24906e5-8b2c-3888-8a82-36512ed498f6 | -11.03014 | -54.83578 | 2025-05-31 04:27:00 | NOAA-21 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 89fbec4d-4edc-3c03-869a-c6f935bd66d0 | -13.63616 | -52.1837 | 2025-05-31 04:27:00 | NOAA-21 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 86eb2503-a697-39ad-8e89-2baacdc8385a | -12.26282 | -44.60382 | 2025-05-31 04:27:00 | NOAA-21 | CATOLÂNDIA | BAHIA | Brasil | 2907400 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 28db2fe7-8835-307c-b273-b750cd27f87a | -11.64286 | -55.36837 | 2025-05-31 04:27:00 | NOAA-21 | SINOP | MATO GROSSO | Brasil | 5107909 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 5337e776-633c-3517-a4f2-39128d3a760a | -13.94429 | -54.49191 | 2025-05-31 04:27:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| e00f8f20-0339-384e-827b-406e214c5aed | -12.45831 | -54.91742 | 2025-05-31 04:27:00 | NOAA-21 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| a571ac1a-0086-3a5b-b627-388cdbaab9f7 | -10.61006 | -44.76617 | 2025-05-31 04:27:00 | NOAA-21 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| a27f2396-09d6-3833-bc01-46888576c062 | -12.10589 | -54.67209 | 2025-05-31 04:27:00 | NOAA-21 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 5de0e22f-5346-3522-8ae3-b0b35d644e05 | -10.64407 | -49.43472 | 2025-05-31 04:27:00 | NOAA-21 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 10.4 |
| 0f79420e-2aad-3e61-8177-515b8be64187 | -12.50211 | -55.73793 | 2025-05-31 04:27:00 | NOAA-21 | SORRISO | MATO GROSSO | Brasil | 5107925 | 51 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 4cadfeb4-3c4a-34bf-b7f5-88d6510bcc4e | -9.67455 | -48.60209 | 2025-05-31 04:27:00 | NOAA-21 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| efcbb75c-3b2b-3f93-96ab-1765b9f55238 | -11.78909 | -54.77803 | 2025-05-31 04:27:00 | NOAA-21 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f6eee4cc-d713-3b0f-a591-b60cd8abd0e4 | -13.95377 | -54.48931 | 2025-05-31 04:27:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 7f3a77b9-09da-3ebf-a384-ec830169d5ce | -12.02266 | -49.51682 | 2025-05-31 04:27:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 10.0 |
| 884494c3-b9e9-3ade-bbd4-b052d6e118c2 | -11.83265 | -51.27809 | 2025-05-31 04:27:00 | NOAA-21 | SERRA NOVA DOURADA | MATO GROSSO | Brasil | 5107883 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| feeadc2d-7081-3b1f-8dce-0a9908073647 | -12.49839 | -55.74091 | 2025-05-31 04:27:00 | NOAA-21 | SORRISO | MATO GROSSO | Brasil | 5107925 | 51 | 33 | nan | nan | nan | Cerrado | 8.5 |
| 0b5e4b67-8b9b-3ffb-b4da-676544da5400 | -11.91121 | -54.41742 | 2025-05-31 04:27:00 | NOAA-21 | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| fc74383c-c2c7-3961-949f-4769ab77da23 | -10.64468 | -49.43093 | 2025-05-31 04:27:00 | NOAA-21 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 10.4 |
| e787ca59-3571-33ec-9451-acdb961872d2 | -13.32985 | -49.22223 | 2025-05-31 04:27:00 | NOAA-21 | PORANGATU | GOIÁS | Brasil | 5218003 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| cb55d971-f1d2-3dcc-8da0-5757868e1250 | -9.38637 | -48.42529 | 2025-05-31 04:27:00 | NOAA-21 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 43e89bd9-b72e-3022-912d-eba40dad74ae | -10.45668 | -47.94564 | 2025-05-31 04:27:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| deded6bf-398d-36f4-8cae-bfde05b6e991 | -10.61453 | -44.76977 | 2025-05-31 04:27:00 | NOAA-21 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| f78a056f-d6b4-3b8d-8b5e-d33a640cb113 | -11.89949 | -47.44786 | 2025-05-31 04:27:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 211c9fcd-0142-37b8-8226-409e1225c144 | -12.02205 | -49.52057 | 2025-05-31 04:27:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 10.0 |
| 6087d36c-333f-33a4-aa87-3be5f5a57e14 | -12.08506 | -54.58082 | 2025-05-31 04:27:00 | NOAA-21 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |


[Clique aqui para ver as próximas entradas](README9.md)
