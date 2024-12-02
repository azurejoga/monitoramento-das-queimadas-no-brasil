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

## Dados Diários - Página 23

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 2aec05bb-bf80-349a-99df-1bdd7e3293a7 | -3.32655 | -50.1863 | 2024-12-02 04:01:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 98735d9d-537b-3b0c-b3a7-2652ca491ef6 | -3.65564 | -51.11992 | 2024-12-02 04:01:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| bf16a896-2fac-3e35-92ab-25398e48a65d | -4.96413 | -41.31726 | 2024-12-02 04:01:00 | NOAA-21 | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 3.2 |
| bac98f2f-6ae3-3b08-b509-a424047fd80b | -1.72793 | -52.64057 | 2024-12-02 04:01:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 48bbe781-217f-3101-8e9e-86e95d848f28 | -1.99077 | -46.45042 | 2024-12-02 04:01:00 | NOAA-21 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 5b9dd3b1-9fcb-3f36-8606-f8af52167bbe | -2.74011 | -51.75091 | 2024-12-02 04:01:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| a07bb139-44d4-37c6-96ed-624f51b728a7 | -5.57928 | -45.14895 | 2024-12-02 04:01:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 13.3 |
| 1d5df0f2-007e-3493-a3de-7e8aa51ca8c8 | -5.19908 | -43.86504 | 2024-12-02 04:01:00 | NOAA-21 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 6e3b48b6-5f5e-3789-8209-2f8517ad435a | -4.91185 | -41.34191 | 2024-12-02 04:01:00 | NOAA-21 | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 8.6 |
| 073779d9-d2f2-32ae-8e8f-399a586f5f40 | -3.45184 | -44.92522 | 2024-12-02 04:01:00 | NOAA-21 | CAJARI | MARANHÃO | Brasil | 2102507 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| b6ffa378-f34a-3c18-8960-1fbf5417620d | -4.07998 | -49.06009 | 2024-12-02 04:01:00 | NOAA-21 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 93e1948a-8dd3-35cf-8019-21eede9cda22 | -3.59908 | -42.80883 | 2024-12-02 04:01:00 | NOAA-21 | BREJO | MARANHÃO | Brasil | 2102101 | 21 | 33 | nan | nan | nan | Cerrado | 10.8 |
| 42f7f7ee-1d71-38f7-afde-e7d89df612c5 | -4.3628 | -46.27224 | 2024-12-02 04:01:00 | NOAA-21 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a44ee5b5-cf26-3569-9356-624f9df2e0ca | -4.40627 | -49.76892 | 2024-12-02 04:01:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 943d9187-07cc-35bc-a1cc-015fea439e9e | -6.08059 | -48.0547 | 2024-12-02 04:01:00 | NOAA-21 | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | 15.8 |
| f04b7159-2a13-3e6e-81b2-27f45996cd9e | -5.61471 | -43.47588 | 2024-12-02 04:01:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 5bd1155e-e9ff-3e98-a6ee-5b496e321965 | -4.43989 | -45.35328 | 2024-12-02 04:01:00 | NOAA-21 | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 0df0dca2-e93f-3e2b-80fe-cf16c18ba1df | -3.88763 | -49.93283 | 2024-12-02 04:01:00 | NOAA-21 | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| c93f5fc5-94f0-3184-bdda-9186ff76ec80 | -7.88098 | -35.13534 | 2024-12-02 04:01:00 | NOAA-21 | PAUDALHO | PERNAMBUCO | Brasil | 2610608 | 26 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| c3736967-a82a-3302-8637-ba69510f4340 | -3.05578 | -51.05904 | 2024-12-02 04:01:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 936ade9d-6251-3666-8160-684cac8cd1a3 | -3.95788 | -46.01623 | 2024-12-02 04:01:00 | NOAA-21 | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 04bb20b2-652f-3eb3-ae73-97b460212405 | -3.67878 | -50.24768 | 2024-12-02 04:01:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 2d39bd1a-54e7-3621-93a4-934d1a6285d1 | -4.11442 | -39.99102 | 2024-12-02 04:01:00 | NOAA-21 | SANTA QUITÉRIA | CEARÁ | Brasil | 2312205 | 23 | 33 | nan | nan | nan | Caatinga | 1.1 |
| b6cde9c6-a978-33ae-bb4e-f2ac6639d616 | -5.17181 | -44.80292 | 2024-12-02 04:01:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 7.0 |
| e79b40d6-84b9-33e4-8178-0a390eae9599 | -3.35698 | -49.50953 | 2024-12-02 04:01:00 | NOAA-21 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 22db066f-b1de-3761-bf90-74a3731112c5 | -3.96187 | -46.50608 | 2024-12-02 04:01:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 2.2 |
| c3bd4d73-04b6-363e-b088-f617a3529f7d | -2.49984 | -49.01839 | 2024-12-02 04:01:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| e7ce8c60-6c57-3ebb-a5f3-2ee22cc78690 | -4.74914 | -41.10405 | 2024-12-02 04:01:00 | NOAA-21 | PORANGA | CEARÁ | Brasil | 2311009 | 23 | 33 | nan | nan | nan | Caatinga | 1.8 |
| e2718899-9d04-347e-ae94-6b7f087bede6 | -3.09387 | -53.23042 | 2024-12-02 04:01:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 5ed449e2-8a8e-3762-98b9-239f30067c4d | -3.85817 | -46.53411 | 2024-12-02 04:01:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 9cc2667d-bd08-3db6-b5b0-f3afe9cbac6c | -2.69193 | -51.87733 | 2024-12-02 04:01:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| a7cb14ae-c5c2-3299-88fd-13eea5595fd8 | 0.88888 | -50.96241 | 2024-12-02 04:01:00 | NOAA-21 | FERREIRA GOMES | AMAPÁ | Brasil | 1600238 | 16 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 983cedaf-3e81-3d3c-aa81-e60ccda48bbd | -3.28994 | -50.44497 | 2024-12-02 04:01:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 31077b3e-9cc7-3aee-a567-df97d3ec4c42 | -5.128 | -43.21194 | 2024-12-02 04:01:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 39.2 |
| 23555607-9ffd-30f0-891a-5b7f13bf1d4a | -3.48935 | -46.08935 | 2024-12-02 04:01:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 74032c3f-13e9-3101-a10a-5521ede74c61 | -4.77048 | -46.42854 | 2024-12-02 04:01:00 | NOAA-21 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 6ae50686-4fe7-3d8c-a42f-295a0e1f7a9d | -5.20674 | -42.87022 | 2024-12-02 04:01:00 | NOAA-21 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 5c97797a-fb29-3252-b08f-f408f4f0f02a | -3.26903 | -46.4523 | 2024-12-02 04:01:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 8.6 |
| cd80f014-8618-361c-b3bc-11a6da0733a7 | -4.63981 | -46.89926 | 2024-12-02 04:01:00 | NOAA-21 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 0ac2ed69-dd70-3a5a-b862-239c538322f7 | -1.73073 | -45.60862 | 2024-12-02 04:01:00 | NOAA-21 | TURIAÇU | MARANHÃO | Brasil | 2112407 | 21 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 6fd47f1d-1ecd-3ca5-b6a0-87b1e0406303 | -2.99077 | -51.33053 | 2024-12-02 04:01:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 94337495-8c03-3124-a2ac-463ee92d6c3c | -2.48626 | -46.58158 | 2024-12-02 04:01:00 | NOAA-21 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 23fa5d98-d5d1-3403-add1-d67ed61dd93c | -2.90164 | -51.58279 | 2024-12-02 04:01:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 2a0cd6a3-fa0d-3695-a4c4-ecb020d11434 | -4.58351 | -43.35499 | 2024-12-02 04:01:00 | NOAA-21 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 62e67682-ede5-32a3-ab38-71959b5e1dcc | -2.74667 | -51.75198 | 2024-12-02 04:01:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 701a7fb3-c54d-38d1-8091-20747d306eeb | -4.55775 | -45.72127 | 2024-12-02 04:01:00 | NOAA-21 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 7d58a31b-77cf-3ffc-ab23-3716216ea6cc | -3.19539 | -46.58325 | 2024-12-02 04:01:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 3.0 |
| d4409a0b-dee9-388f-871f-77ca24a5d104 | -2.83065 | -51.83848 | 2024-12-02 04:01:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 7b2553ae-4c78-3dd4-98ce-d9fc63901083 | -5.60738 | -43.47465 | 2024-12-02 04:01:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| eabf30e1-b68d-3826-ba6e-212a605be529 | -3.23637 | -50.65564 | 2024-12-02 04:01:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 35643f96-e233-3543-a63c-31a69000a4f4 | -6.81792 | -46.7726 | 2024-12-02 04:01:00 | NOAA-21 | SÃO PEDRO DOS CRENTES | MARANHÃO | Brasil | 2111573 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 853ff834-b070-3c25-bea4-e5f8cbfae532 | -2.95596 | -39.96154 | 2024-12-02 04:01:00 | NOAA-21 | ITAREMA | CEARÁ | Brasil | 2306553 | 23 | 33 | nan | nan | nan | Caatinga | 3.2 |
| d220ff14-c5de-3bb1-b87e-ec7d061e7e7e | -2.69127 | -48.85656 | 2024-12-02 04:01:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 4ab34e12-4e63-35bc-8085-7478383b2d96 | -4.66793 | -46.87378 | 2024-12-02 04:01:00 | NOAA-21 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 3.9 |
| ac36ba2c-1b90-36e4-bd63-83d1523c5c07 | -4.08061 | -49.05643 | 2024-12-02 04:01:00 | NOAA-21 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 6e0c5ff2-6a94-36c1-a1e7-e5e775bf990a | -4.91239 | -41.33846 | 2024-12-02 04:01:00 | NOAA-21 | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 3.7 |
| fa269755-cca9-3df9-8c24-538fbe1e1c7d | -4.90512 | -41.31899 | 2024-12-02 04:01:00 | NOAA-21 | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 4.3 |
| e9086d52-6a6b-3fc5-90c9-393593060429 | -4.54768 | -43.30175 | 2024-12-02 04:01:00 | NOAA-21 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| a3bdaba8-8704-3a1d-92a4-4a3c35bab85c | -4.43865 | -45.36102 | 2024-12-02 04:01:00 | NOAA-21 | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 72e3580f-114e-32bf-bf7d-09f557d43801 | -5.21031 | -42.8708 | 2024-12-02 04:01:00 | NOAA-21 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 4084c80e-5b07-3fe3-8c1d-8cdaa5b2fcc0 | -3.27361 | -46.45313 | 2024-12-02 04:01:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 8.6 |
| dd40b78f-2ea7-3f24-a3c5-ce5e0e443859 | -2.73865 | -51.75238 | 2024-12-02 04:01:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 1b8f3d4a-9ce6-32be-88e5-4896b364e000 | -3.28665 | -50.44213 | 2024-12-02 04:01:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 9958b744-9798-30b4-b14d-1af9f37c76a7 | -4.90398 | -41.32617 | 2024-12-02 04:01:00 | NOAA-21 | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 3.1 |
| 9cb92c1c-7df3-3cb6-b346-b8baaa608afc | -2.67749 | -46.61745 | 2024-12-02 04:01:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 9.0 |
| 3ac8f97f-c2b6-3a95-8021-c99f7144687b | -2.37028 | -46.07291 | 2024-12-02 04:01:00 | NOAA-21 | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| bb929c9d-8528-3a68-ad58-44184927d1a1 | -5.17125 | -44.80635 | 2024-12-02 04:01:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 7.0 |
| 765ff5c9-5afd-3ff8-82f7-8fa77e45de7d | -2.59526 | -45.65012 | 2024-12-02 04:01:00 | NOAA-21 | SANTA LUZIA DO PARUÁ | MARANHÃO | Brasil | 2110039 | 21 | 33 | nan | nan | nan | Amazônia | 9.5 |
| 1c5c5e15-6020-32e8-8d0f-a1674bfa9054 | -4.40561 | -49.77274 | 2024-12-02 04:01:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 3658f903-e91f-3664-938e-a1f2d973df3a | -4.19104 | -50.67958 | 2024-12-02 04:01:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 728844db-de93-35b7-9c93-9cafaa55dec0 | -4.33045 | -45.9198 | 2024-12-02 04:01:00 | NOAA-21 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 77230e5c-d359-3b43-9d35-9942e12a3f38 | -3.04538 | -49.37552 | 2024-12-02 04:01:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| bc6fdc89-6712-31f4-bd9c-1e4c3adb9f7f | -3.04153 | -49.37745 | 2024-12-02 04:01:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 2302d36b-5280-376b-b686-a94d19ebe592 | -3.87695 | -38.43661 | 2024-12-02 04:01:00 | NOAA-21 | EUSÉBIO | CEARÁ | Brasil | 2304285 | 23 | 33 | nan | nan | nan | Caatinga | 2.7 |
| b5a1cb7e-7a06-3228-b275-f9d4dfcf4208 | -3.9586 | -46.01187 | 2024-12-02 04:01:00 | NOAA-21 | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 830e8a08-b6df-3a12-96a5-e26cc749f5c6 | -6.45938 | -47.54091 | 2024-12-02 04:01:00 | NOAA-21 | AGUIARNÓPOLIS | TOCANTINS | Brasil | 1700301 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 970866cd-5458-3258-8c89-7488cc33f0d3 | -4.90116 | -41.34387 | 2024-12-02 04:01:00 | NOAA-21 | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| d88d00fd-421b-37c6-bf48-b5369dc78d1a | -3.70611 | -51.83711 | 2024-12-02 04:01:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 6.0 |
| a4be0b92-38c6-3554-83a9-8af30b3dbc52 | -3.14037 | -45.99391 | 2024-12-02 04:01:00 | NOAA-21 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 7.6 |
| dedf95f5-0c20-3125-bc05-16c5f5576fe6 | -3.12768 | -45.98736 | 2024-12-02 04:01:00 | NOAA-21 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| b84132dd-cf82-3861-910e-0cea2eff84db | -6.07764 | -48.05804 | 2024-12-02 04:01:00 | NOAA-21 | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | 5.4 |
| eba9069e-98f0-3472-846d-cdee244c5d8e | -4.26851 | -50.85389 | 2024-12-02 04:01:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 7.0 |
| 354f28a4-27e5-3812-b9e4-82550926e929 | -5.12435 | -43.21139 | 2024-12-02 04:01:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 39.2 |
| 5cc17585-7ae5-36bd-a2d0-0dabc1468695 | -2.6783 | -46.61247 | 2024-12-02 04:01:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 4.1 |
| e218374a-f008-3a8a-9302-bbe75cad3e90 | -4.07277 | -49.06964 | 2024-12-02 04:01:00 | NOAA-21 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 45849c20-8c10-3a34-aa07-74ef5ab48881 | -3.0974 | -53.23139 | 2024-12-02 04:01:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| df961b6f-6e4d-39c5-9364-66d325906982 | -3.45597 | -44.92587 | 2024-12-02 04:01:00 | NOAA-21 | VITÓRIA DO MEARIM | MARANHÃO | Brasil | 2112902 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 6b35dad8-b145-324a-b312-87337472ce9b | -4.91521 | -41.34248 | 2024-12-02 04:01:00 | NOAA-21 | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 16.6 |
| 537858e8-f635-3b24-949c-f06e35464317 | -3.26629 | -45.37111 | 2024-12-02 04:01:00 | NOAA-21 | PENALVA | MARANHÃO | Brasil | 2108306 | 21 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 24f5002e-f068-3bb2-86cc-4625e0f320e7 | -3.10349 | -40.08352 | 2024-12-02 04:01:00 | NOAA-21 | BELA CRUZ | CEARÁ | Brasil | 2302305 | 23 | 33 | nan | nan | nan | Caatinga | 0.9 |
| d6d234bb-1718-3726-9295-722758e3b6e2 | -5.00978 | -44.16798 | 2024-12-02 04:01:00 | NOAA-21 | GOVERNADOR ARCHER | MARANHÃO | Brasil | 2104503 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| c3b2f199-5b0c-3d64-8dde-a06d7e799c7e | -2.72409 | -45.07206 | 2024-12-02 04:01:00 | NOAA-21 | PALMEIRÂNDIA | MARANHÃO | Brasil | 2107605 | 21 | 33 | nan | nan | nan | Amazônia | 9.5 |
| 73f53ea1-9a7f-3765-95e0-6f073edfe5b4 | -2.86059 | -48.55681 | 2024-12-02 04:01:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 458588f5-db0a-3ba7-9285-4a50adf657ff | -4.13562 | -44.83258 | 2024-12-02 04:01:00 | NOAA-21 | BACABAL | MARANHÃO | Brasil | 2101202 | 21 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 51817c8b-f737-3880-909f-8ff869a40ded | -0.92848 | -47.61796 | 2024-12-02 04:01:00 | NOAA-21 | MARAPANIM | PARÁ | Brasil | 1504406 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 030c9177-1e5f-3867-831b-5f178cde7a3c | -3.77747 | -52.03923 | 2024-12-02 04:01:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 8.0 |
| 705363a2-d84f-377e-aa48-ffbb73b3b62c | -4.86975 | -41.35765 | 2024-12-02 04:01:00 | NOAA-21 | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 3.4 |
| d5e82873-1339-3c4b-a612-82c5f7a0fa51 | -3.26751 | -51.1109 | 2024-12-02 04:01:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 6d955a97-dfd1-3ee3-b30f-c16c6dfe0c21 | -3.2676 | -50.21194 | 2024-12-02 04:01:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| f9bee68f-d61d-3607-85e5-9cd9a044bb0a | -4.63489 | -45.46249 | 2024-12-02 04:01:00 | NOAA-21 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Cerrado | 16.9 |


[Clique aqui para ver as próximas entradas](README24.md)
