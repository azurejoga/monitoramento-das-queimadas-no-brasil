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

## Dados Diários - Página 16

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 0c8b8511-9c6d-376b-b96d-81c9eb8c6e64 | -1.23829 | -54.14096 | 2024-12-13 04:18:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 83255bcb-3689-3406-9d50-10eb46b1213c | -1.24626 | -52.16262 | 2024-12-13 04:18:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| a95b62c5-73b2-3497-be92-7a17eff8734c | -1.74077 | -52.02921 | 2024-12-13 04:18:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 27730174-f2ea-3a2c-ba25-ae6bf1f1f7cb | -1.52898 | -46.29412 | 2024-12-13 04:18:00 | NPP-375D | VISEU | PARÁ | Brasil | 1508308 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 485fe72f-d637-305e-a7f3-bb4390c9816b | -1.5319 | -46.29863 | 2024-12-13 04:18:00 | NPP-375D | VISEU | PARÁ | Brasil | 1508308 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 5e1e9f5b-5971-39e2-9793-658da3a087f4 | -2.50034 | -47.69407 | 2024-12-13 04:18:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 8c0c5aab-3131-39b9-8c35-60d0def37167 | -3.36124 | -42.30848 | 2024-12-13 04:18:00 | NPP-375D | SÃO BERNARDO | MARANHÃO | Brasil | 2110609 | 21 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 43a3d922-22c2-3b7a-9f44-0e95cc61d6a7 | -1.73393 | -52.02308 | 2024-12-13 04:18:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| cb1985dd-fac9-3c55-974d-0de2b0d6351e | -3.00334 | -44.43283 | 2024-12-13 04:18:00 | NPP-375D | BACABEIRA | MARANHÃO | Brasil | 2101251 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| afa263c7-c142-3a25-89a6-9c9242df6121 | -1.74537 | -52.03297 | 2024-12-13 04:18:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f6ff5ad6-63a9-3d39-9568-5fa59b40ab59 | -11.2148 | -53.833 | 2024-12-13 04:20:00 | GOES-16 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 53.4 |
| ae9da0ca-d145-3d70-b0d4-01c0114d1934 | -5.2298 | -43.282 | 2024-12-13 04:20:00 | GOES-16 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 47.2 |
| 7fa6d3c2-f0a0-330f-b0ec-c4c8b709848a | -5.2108 | -43.3067 | 2024-12-13 04:20:00 | GOES-16 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 83.2 |
| dd7f7a9e-3bb9-3e83-9d9a-7bdc1789a911 | -5.211 | -43.2833 | 2024-12-13 04:20:00 | GOES-16 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 93.5 |
| 5573fc25-7b39-3073-b9ac-f6f38c86707c | -10.0265 | -36.2969 | 2024-12-13 04:20:00 | GOES-16 | CORURIPE | ALAGOAS | Brasil | 2702306 | 27 | 33 | nan | nan | nan | Caatinga | 62.0 |
| a47a0498-aeba-3e60-8273-4641e81006ba | -11.1962 | -53.8142 | 2024-12-13 04:20:00 | GOES-16 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 64.4 |
| 8fbedc34-0c4c-3ded-af20-98b59e17a93b | -11.1959 | -53.8348 | 2024-12-13 04:20:00 | GOES-16 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 75.4 |
| b172d849-8ee2-307f-a9d5-53bc8b4ce49c | -13.0644 | -52.0326 | 2024-12-13 04:20:00 | GOES-16 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Amazônia | 74.8 |
| 8715208e-6dc3-3ce3-af73-acbd94bd9b80 | -11.2151 | -53.8125 | 2024-12-13 04:20:00 | GOES-16 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 45.0 |
| 91433be2-ae42-3c7e-a398-089b71d15f4c | -6.9161 | -43.4952 | 2024-12-13 04:20:00 | GOES-16 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 71.2 |
| 6c76a056-61fd-3094-8c93-86d49918c70e | -2.5108 | -51.8023 | 2024-12-13 04:20:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 56.5 |
| fcd82d23-5e62-3e24-8f14-816cde28ca3f | -2.4923 | -51.8027 | 2024-12-13 04:20:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 84.0 |
| 9f87d982-97ce-3bff-9aba-ca1e3062fa1d | -12.5497 | -57.7196 | 2024-12-13 04:20:00 | GOES-16 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 58.6 |
| 83ebc053-c26c-3e1d-950c-ebb44e7aaa0c | -6.9158 | -43.5185 | 2024-12-13 04:20:00 | GOES-16 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 54.4 |
| 5ccf5022-df6e-3034-b2fe-a40502c12da1 | -6.94612 | -42.85847 | 2024-12-13 04:21:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| d04fa24e-2ada-3163-ad31-a0bb7030d022 | -2.48862 | -51.80445 | 2024-12-13 04:21:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| ddfb5df6-a84b-3d8a-a360-d311873dbf4e | -3.95757 | -41.48906 | 2024-12-13 04:21:00 | NPP-375D | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 1298a278-4565-3d24-a6df-ffe071f4c506 | -9.90342 | -42.11299 | 2024-12-13 04:21:00 | NPP-375D | SENTO SÉ | BAHIA | Brasil | 2930204 | 29 | 33 | nan | nan | nan | Caatinga | 2.8 |
| ba9a3fc3-c546-3672-949b-28c94b8a2e74 | -4.51717 | -42.07101 | 2024-12-13 04:21:00 | NPP-375D | BOQUEIRÃO DO PIAUÍ | PIAUÍ | Brasil | 2201945 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| e590bcfc-80bb-3c7c-92ff-5af67d1a9e52 | -3.83481 | -41.5605 | 2024-12-13 04:21:00 | NPP-375D | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 1a9de875-5860-3b1a-91e5-b8f0bb9b41cd | -2.52188 | -51.79411 | 2024-12-13 04:21:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| c56cdb31-a66c-3516-aec4-dec9b06ab120 | -7.58051 | -47.11728 | 2024-12-13 04:21:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 2db25192-7090-3aa8-adb0-3541ac7d0d0f | -5.986 | -42.3131 | 2024-12-13 04:21:00 | NPP-375D | ELESBÃO VELOSO | PIAUÍ | Brasil | 2203503 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 248e9b4b-b2a9-3bfc-91e7-fe2defc6cf96 | -9.9661 | -49.82291 | 2024-12-13 04:21:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| a08cd19d-9626-3b53-8ed1-81294c58aa22 | -5.32402 | -43.74853 | 2024-12-13 04:21:00 | NPP-375D | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 0d46f6c1-cdc0-3cb0-92a0-f99be999e82b | -4.08462 | -44.26935 | 2024-12-13 04:21:00 | NPP-375D | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 4662bcc6-b9ca-3d35-8f75-b95f17b79562 | -6.59194 | -44.15763 | 2024-12-13 04:21:00 | NPP-375D | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 9977c1e2-659f-3fec-b17f-cff9a2836763 | -5.36025 | -37.91422 | 2024-12-13 04:21:00 | NPP-375D | TABULEIRO DO NORTE | CEARÁ | Brasil | 2313104 | 23 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 90c4b7e9-7c0d-3818-ba10-ee5d7dfad472 | -8.43294 | -49.86649 | 2024-12-13 04:21:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 75515e8c-18c8-35bc-87b7-2f04c025ee09 | -6.98392 | -47.08559 | 2024-12-13 04:21:00 | NPP-375D | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| c486abb3-63b5-318d-8af9-a2e1156bd0bb | -5.05843 | -44.23082 | 2024-12-13 04:21:00 | NPP-375D | GOVERNADOR ARCHER | MARANHÃO | Brasil | 2104503 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 9d7afa7d-db65-3469-9bec-8531b21368a7 | -2.58189 | -51.92487 | 2024-12-13 04:21:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 9ea0e543-5b3a-3326-b29c-0bec04c0c182 | -6.09126 | -44.76246 | 2024-12-13 04:21:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| cf437842-d542-3041-b831-b1796289d1d3 | -6.9467 | -42.85472 | 2024-12-13 04:21:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| a6cdad77-492c-3d83-b2cb-17463336ee1c | -4.87925 | -44.40443 | 2024-12-13 04:21:00 | NPP-375D | SANTO ANTÔNIO DOS LOPES | MARANHÃO | Brasil | 2110302 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 59a4c7be-2778-3d1d-902b-9e4fb4d9f30c | -3.99501 | -46.95516 | 2024-12-13 04:21:00 | NPP-375D | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 2.5 |
| ec86b115-1fe7-3e74-8cef-04b045c9a4a7 | -4.64482 | -47.71202 | 2024-12-13 04:21:00 | NPP-375D | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 0.6 |
| c9bc171b-5dd7-394f-905d-d0c94a25207b | -6.98126 | -42.81388 | 2024-12-13 04:21:00 | NPP-375D | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| b2533f75-0b63-32a2-8bf8-e5b440bca4a1 | -2.49357 | -51.80525 | 2024-12-13 04:21:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 22.7 |
| 53bd5061-6530-3346-86c1-db7f7950edbd | -2.49267 | -51.81083 | 2024-12-13 04:21:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 22.7 |
| 6a316935-db9e-3e3b-a3b8-53f4f555299d | -5.15868 | -44.36695 | 2024-12-13 04:21:00 | NPP-375D | PRESIDENTE DUTRA | MARANHÃO | Brasil | 2109106 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 4ab445e8-c234-354b-851f-1209c3833731 | -6.05457 | -44.04517 | 2024-12-13 04:21:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 7ff4d95b-ef06-3d97-a1e0-9a1cc60f31c5 | -4.97375 | -44.49054 | 2024-12-13 04:21:00 | NPP-375D | SANTO ANTÔNIO DOS LOPES | MARANHÃO | Brasil | 2110302 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 2b4902bb-6583-3aed-bddb-584d3487ecf3 | -3.83128 | -41.55994 | 2024-12-13 04:21:00 | NPP-375D | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| f6a3a5d3-118c-3f10-b0bc-22a5548b3903 | -7.97067 | -48.16879 | 2024-12-13 04:21:00 | NPP-375D | PALMEIRANTE | TOCANTINS | Brasil | 1715705 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 3269eb9c-9553-3919-ba2b-87329acaea48 | -10.03114 | -36.28126 | 2024-12-13 04:21:00 | NPP-375D | CORURIPE | ALAGOAS | Brasil | 2702306 | 27 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| 92a9c539-724e-31b7-83ed-6ac814cdce65 | -3.01042 | -48.03253 | 2024-12-13 04:21:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 2ddb3d88-6fef-3541-b564-05770a2233cf | -7.99528 | -39.43072 | 2024-12-13 04:21:00 | NPP-375D | SERRITA | PERNAMBUCO | Brasil | 2614006 | 26 | 33 | nan | nan | nan | Caatinga | 2.3 |
| f44f503e-0dc4-3066-992d-597d3e3661f4 | -3.0066 | -48.03193 | 2024-12-13 04:21:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| cb9917df-8b73-3ee9-9dd7-30b161498721 | -4.13517 | -47.73119 | 2024-12-13 04:21:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 74fa0d58-8398-3aa7-b487-ef77641b9879 | -3.26347 | -46.92895 | 2024-12-13 04:21:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| b324064a-c481-35e3-8f0e-3e2f9b0330ef | -5.21482 | -43.29495 | 2024-12-13 04:21:00 | NPP-375D | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 19.7 |
| 37ef2909-a086-3def-8a23-7b2f24f929a0 | -2.91581 | -48.01257 | 2024-12-13 04:21:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 1c0cc49c-270d-3fb6-9709-4014e0aeeaf8 | -4.42949 | -44.14312 | 2024-12-13 04:21:00 | NPP-375D | PERITORÓ | MARANHÃO | Brasil | 2108454 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 9599c84b-ae11-31f4-b233-edc71e16bd1d | -10.02572 | -36.2807 | 2024-12-13 04:21:00 | NPP-375D | CORURIPE | ALAGOAS | Brasil | 2702306 | 27 | 33 | nan | nan | nan | Mata Atlântica | 6.4 |
| 6eb277cc-9aae-38ac-b64f-11a9129f852a | -2.48772 | -51.81001 | 2024-12-13 04:21:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| f4c83b08-a00f-368e-b0e3-8cfc96254f03 | -3.80204 | -51.08975 | 2024-12-13 04:21:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 4d577b5e-fdde-3e24-be9d-79181432c86e | -9.47426 | -37.06655 | 2024-12-13 04:21:00 | NPP-375D | MAJOR ISIDORO | ALAGOAS | Brasil | 2704401 | 27 | 33 | nan | nan | nan | Caatinga | 2.0 |
| fcb41ec4-593c-3178-b8d0-fc33eec6f695 | -5.06175 | -44.23134 | 2024-12-13 04:21:00 | NPP-375D | GOVERNADOR ARCHER | MARANHÃO | Brasil | 2104503 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 4738c75e-d528-393d-a85b-480ab340ab24 | -5.05789 | -44.23428 | 2024-12-13 04:21:00 | NPP-375D | GOVERNADOR ARCHER | MARANHÃO | Brasil | 2104503 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 331158d7-f7ea-3409-a164-373372a634ba | -4.7818 | -48.50529 | 2024-12-13 04:21:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| d64d0b81-854c-3010-ab61-33c7b94ed13e | -6.09459 | -44.76299 | 2024-12-13 04:21:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 77963f20-4545-323a-a539-dc8694893775 | -2.516 | -51.79886 | 2024-12-13 04:21:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 25c356b4-aeae-3f92-a8cf-2ee0abe809df | -8.60455 | -40.57281 | 2024-12-13 04:21:00 | NPP-375D | DORMENTES | PERNAMBUCO | Brasil | 2605152 | 26 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 133e073a-7795-3e51-a5a7-7212dd54e171 | -5.6261 | -45.38828 | 2024-12-13 04:21:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 0.4 |
| e6928c97-643d-3750-b3fa-1754e3a2c014 | -2.45395 | -53.71278 | 2024-12-13 04:21:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 45081ede-55f2-3a94-ba37-e1372ba23083 | -7.25285 | -39.7532 | 2024-12-13 04:21:00 | NPP-375D | SANTANA DO CARIRI | CEARÁ | Brasil | 2312106 | 23 | 33 | nan | nan | nan | Caatinga | 3.6 |
| ad4abaf9-49b2-35e8-98d2-1a206696c9d1 | -6.5386 | -44.52026 | 2024-12-13 04:21:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 6c6e5947-646c-3303-994a-d3c304fb82bf | -9.08296 | -36.12914 | 2024-12-13 04:21:00 | NPP-375D | SANTANA DO MUNDAÚ | ALAGOAS | Brasil | 2708105 | 27 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 3832d645-fac9-3dc1-ba32-d70f27c36ace | -4.77997 | -48.50259 | 2024-12-13 04:21:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| dd6ab896-d2a0-3aaf-af92-ab733b08839b | -2.91359 | -48.00985 | 2024-12-13 04:21:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 569f46d5-f787-352f-a330-d9b541d2f0b3 | -3.31891 | -45.70467 | 2024-12-13 04:21:00 | NPP-375D | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| fb0f64f5-35a3-3b48-b560-bc1ceb1c000f | -5.48374 | -40.51857 | 2024-12-13 04:21:00 | NPP-375D | INDEPENDÊNCIA | CEARÁ | Brasil | 2305605 | 23 | 33 | nan | nan | nan | Caatinga | 2.8 |
| 0768bf67-6ad6-3222-9111-9ff75f64a8b3 | -3.26835 | -46.92142 | 2024-12-13 04:21:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| dc6b1c0f-ca0b-38f0-8034-4f07c0397c99 | -7.43251 | -44.73233 | 2024-12-13 04:21:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 2e04dbad-f76c-36dc-ae01-7ccbcc64e669 | -9.59722 | -47.7047 | 2024-12-13 04:21:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| a555404c-69d2-33bc-be89-8b5e88dbc9b3 | -3.38893 | -49.72127 | 2024-12-13 04:21:00 | NPP-375D | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 01fabbf4-a346-3984-8740-3939b2b2bf6a | -5.98251 | -42.31254 | 2024-12-13 04:21:00 | NPP-375D | ELESBÃO VELOSO | PIAUÍ | Brasil | 2203503 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 7843d7fb-22ca-3ad7-941c-76ef4d39da09 | -2.91199 | -48.01197 | 2024-12-13 04:21:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e4f408b4-6e0b-3f11-a2c9-68485dbffa27 | -4.51477 | -47.94275 | 2024-12-13 04:21:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| d2aa0224-4983-3997-82f8-dfda16aa40a9 | -4.55266 | -43.57549 | 2024-12-13 04:21:00 | NPP-375D | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| ef7c9dec-635c-3494-b210-32596b385d7f | -4.51196 | -42.0585 | 2024-12-13 04:21:00 | NPP-375D | BOQUEIRÃO DO PIAUÍ | PIAUÍ | Brasil | 2201945 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 787c65b2-a10e-34e0-b55c-e365eed5c0ed | -7.98607 | -50.70422 | 2024-12-13 04:21:00 | NPP-375D | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 7fe41177-d26f-35c5-a139-3b0f29db8a67 | -9.71052 | -37.35439 | 2024-12-13 04:21:00 | NPP-375D | PÃO DE AÇÚCAR | ALAGOAS | Brasil | 2706406 | 27 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 0026ff0f-ef74-305d-bc4d-00fdd5eaa4f7 | -4.13999 | -50.41703 | 2024-12-13 04:21:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b6506c38-f8f1-3c72-a893-42018050d295 | -2.49762 | -51.81165 | 2024-12-13 04:21:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 22.7 |
| b5ccca23-05e7-39f3-8ccb-81bf4bed8ac8 | -6.53528 | -44.51974 | 2024-12-13 04:21:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| b80d1808-2285-3024-bea9-23f749cfb1aa | -7.13322 | -44.95541 | 2024-12-13 04:21:00 | NPP-375D | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| b9f177d7-5335-3ce3-a77a-9896c9e2504b | -3.83361 | -41.56834 | 2024-12-13 04:21:00 | NPP-375D | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 3.4 |
| b6e8e0e5-72e0-3c2e-9dfe-676082d746e8 | -4.4808 | -47.98728 | 2024-12-13 04:21:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |


[Clique aqui para ver as próximas entradas](README17.md)
