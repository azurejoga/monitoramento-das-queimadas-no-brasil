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

## Dados Diários - Página 74

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| dc826967-53b7-3acb-8907-ae65235a7729 | -2.70696 | -49.17733 | 2024-11-10 04:38:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e3240e36-d2a0-30dc-8085-c9bf6eceed3e | -2.94482 | -49.49775 | 2024-11-10 04:38:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 74c630f8-6f01-3fea-81f2-6a7ae973b3b8 | -2.38191 | -50.60357 | 2024-11-10 04:38:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| cdd2fafa-37c2-394a-ac9f-6a7513b288d5 | -2.88067 | -49.38358 | 2024-11-10 04:38:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 88f9b558-72b9-30f4-a07f-bc821fa23ae7 | -2.71687 | -52.0021 | 2024-11-10 04:38:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 6.5 |
| 4dd90fa1-bb43-307f-a2d3-f4339461c4b0 | -2.19993 | -50.23595 | 2024-11-10 04:38:00 | NPP-375D | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ac091e8f-c014-35ab-b056-adcb2cc6218c | -5.44929 | -44.8218 | 2024-11-10 04:38:00 | NPP-375D | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 3a7c9ad2-4549-3b74-9e67-b7f08d679e63 | -3.2854 | -49.46498 | 2024-11-10 04:38:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| d1fffc14-d8e8-348c-90b0-2eb09f1c92a2 | -3.04173 | -50.32318 | 2024-11-10 04:38:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 0bb810dd-1162-3f64-8e48-62ddd9b188eb | -2.76836 | -49.3513 | 2024-11-10 04:38:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 20.9 |
| 50af3833-359d-3cda-bf58-1594405e61f0 | -2.88849 | -49.50692 | 2024-11-10 04:38:00 | NPP-375D | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| f71e6e50-0776-3905-a9e6-74aed10a2b15 | -3.81301 | -46.90542 | 2024-11-10 04:38:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d0494fb7-afb3-3263-906d-cd01667e2dfc | -4.61036 | -45.97361 | 2024-11-10 04:38:00 | NPP-375D | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| cd104250-3593-352c-aea4-2b08d3edecbe | -3.11721 | -53.12044 | 2024-11-10 04:38:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 9d6f82ec-1d0e-325c-a12b-4c33888bffa7 | -3.23907 | -50.26777 | 2024-11-10 04:38:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| ebd6fa69-93cb-3edf-b5d7-c369efe6825e | -2.90561 | -49.24806 | 2024-11-10 04:38:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 6a06a473-830c-3bb5-9e50-f86b769b4b95 | -2.58237 | -48.16761 | 2024-11-10 04:38:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 832cb9e8-c8a9-3970-97a3-c246d9b86cd9 | -5.08894 | -50.67125 | 2024-11-10 04:38:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 88dd8469-a1dc-33f4-95ab-3422e7a129d8 | -5.14177 | -48.2419 | 2024-11-10 04:38:00 | NPP-375D | SÃO PEDRO DA ÁGUA BRANCA | MARANHÃO | Brasil | 2111532 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 36748ab7-15b2-3ed5-93e0-3fa2a36d6375 | -5.01247 | -45.04052 | 2024-11-10 04:38:00 | NPP-375D | SÃO ROBERTO | MARANHÃO | Brasil | 2111672 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 8ce4f4ce-0c04-3c4e-acf5-ca2067c475d2 | -2.07675 | -52.04131 | 2024-11-10 04:38:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 1b664901-c1f9-3ad7-91e1-50606f032047 | -2.47684 | -49.32736 | 2024-11-10 04:38:00 | NPP-375D | MOCAJUBA | PARÁ | Brasil | 1504604 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| c69a0027-283e-35b6-8ec8-1d23c84ba87a | -2.88573 | -48.30286 | 2024-11-10 04:38:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| ddf7e48c-b3a5-3002-90ea-59e094eae371 | -8.41317 | -44.11832 | 2024-11-10 04:38:00 | NPP-375D | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| e7fe66cc-6db0-3542-8367-5e17b111de67 | -4.19467 | -48.39409 | 2024-11-10 04:38:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| c8d72c6f-4e95-3c97-9b63-378952c08739 | -2.87615 | -51.48001 | 2024-11-10 04:38:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 29.0 |
| fe175fad-bd25-3992-80d7-4ebb0e0a35c9 | -2.8092 | -52.99408 | 2024-11-10 04:38:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| a19a6c84-a750-3938-9f19-126240906b31 | -3.48766 | -44.55059 | 2024-11-10 04:38:00 | NPP-375D | MIRANDA DO NORTE | MARANHÃO | Brasil | 2106755 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 4d77bba1-f9a3-3f3c-a3a1-a29186a27bb1 | -3.69576 | -54.62091 | 2024-11-10 04:38:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 9d0a678b-b7c2-36b4-9c03-cdc02156e4e9 | -2.68141 | -49.19496 | 2024-11-10 04:38:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 8610714a-b0d6-3405-970e-f852e48a12ea | -1.86326 | -53.73431 | 2024-11-10 04:38:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 1c86cc76-ebda-3678-a9ec-a6d6dbd35dee | -8.4101 | -44.10984 | 2024-11-10 04:38:00 | NPP-375D | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| fdeb72c9-b5c8-3457-b763-1afa56baab71 | -3.14525 | -52.96981 | 2024-11-10 04:38:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| e7f1d451-c7f6-304c-8666-31c8c2151ea6 | -3.89352 | -50.08469 | 2024-11-10 04:38:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 323f00b4-31e7-3889-b02e-40247c12cc49 | -3.47234 | -50.38223 | 2024-11-10 04:38:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 10ed97ac-585f-302a-b149-43c3bc3b8e98 | -4.88448 | -48.6122 | 2024-11-10 04:38:00 | NPP-375D | BOM JESUS DO TOCANTINS | PARÁ | Brasil | 1501576 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 42ed0281-2961-3e15-ba20-b6511c0e088b | -2.67838 | -48.5036 | 2024-11-10 04:38:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e22d03aa-c48e-3990-8213-781827975782 | -4.31511 | -48.61543 | 2024-11-10 04:38:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| c4e64843-2cbc-3772-85e3-69ee69172e94 | -2.85686 | -48.44318 | 2024-11-10 04:38:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 41e9aebf-e3fc-3c81-a9ef-614fb675af11 | -3.02278 | -48.03436 | 2024-11-10 04:38:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c55f68d9-d48e-389d-beac-f0464a507522 | -2.56177 | -50.67768 | 2024-11-10 04:38:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 2ed5b429-21aa-3313-a85a-838786a2c994 | -3.22597 | -50.28437 | 2024-11-10 04:38:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 48.4 |
| 15669552-7893-3bc8-99c4-b68d920bc14b | -5.20097 | -48.3442 | 2024-11-10 04:38:00 | NPP-375D | SÃO SEBASTIÃO DO TOCANTINS | TOCANTINS | Brasil | 1720309 | 17 | 33 | nan | nan | nan | Amazônia | 1.7 |
| b3067e4e-5035-3fdf-a4a4-8ab7d1b19a98 | -4.36601 | -47.25512 | 2024-11-10 04:38:00 | NPP-375D | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 4041919a-b1b1-3418-b550-1a99d0a333a7 | -3.53155 | -49.98425 | 2024-11-10 04:38:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 5f805415-aaaa-3795-9671-f7b07305fc95 | -2.38229 | -49.07364 | 2024-11-10 04:38:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 457eb841-537d-3ddb-a3f2-ad0db6b45094 | -2.26586 | -51.8902 | 2024-11-10 04:38:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 7bd973ee-dc2a-3704-bdac-e0f85d39ee5d | -3.18422 | -50.59151 | 2024-11-10 04:38:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 1336ed1b-c374-3aa1-9c17-b0e173a6d879 | -2.40798 | -50.30873 | 2024-11-10 04:38:00 | NPP-375D | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 8a41bb41-3ec3-3744-aa19-e8aac148236a | -6.2293 | -42.91912 | 2024-11-10 04:38:00 | NPP-375D | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| b96da263-4d42-3830-a624-10a62c941883 | -2.87678 | -49.45115 | 2024-11-10 04:38:00 | NPP-375D | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 3279b611-ab31-3179-a306-672b4c02a7b7 | -2.41399 | -50.55828 | 2024-11-10 04:38:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| c77ef2f2-1fd9-33e3-9434-f74479136bf8 | -3.95582 | -48.12233 | 2024-11-10 04:38:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 15.4 |
| bd1a8121-a876-3056-968b-4271d0fea65e | -8.39997 | -44.1203 | 2024-11-10 04:38:00 | NPP-375D | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 64a53fec-61a3-37b3-a9d6-6b7c4b7eb754 | -2.76726 | -49.3583 | 2024-11-10 04:38:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 6.8 |
| f33ba933-95e6-3c2a-9e7e-84d6a8370920 | -3.78675 | -47.73023 | 2024-11-10 04:38:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 7ad3bb68-a8ca-36cf-9db5-6126d132550c | -2.09419 | -50.91175 | 2024-11-10 04:38:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| b8c8c904-a48a-317d-9fde-4aa19561e460 | -2.65615 | -48.64485 | 2024-11-10 04:38:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| cfc430bf-d0c3-3b00-9426-316fef64030e | -2.92851 | -49.36242 | 2024-11-10 04:38:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 013e139e-4a35-334c-b0c3-a9d97ff16de2 | -7.97 | -50.03422 | 2024-11-10 04:38:00 | NPP-375D | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 2da28446-02a2-3679-9464-7798c1505618 | -4.6251 | -49.08096 | 2024-11-10 04:38:00 | NPP-375D | JACUNDÁ | PARÁ | Brasil | 1503804 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| ae6d88c5-684a-3f49-a012-9f2c72ca7f7d | -2.8635 | -48.44421 | 2024-11-10 04:38:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 2560c752-c38b-3ed2-9d8c-a942070f088f | -4.27924 | -48.19758 | 2024-11-10 04:38:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| b1fef6ec-eb50-32ec-b396-14b2b37ead6a | -5.67042 | -41.75355 | 2024-11-10 04:38:00 | NPP-375D | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 40044a5e-8265-3582-b0ad-9cec46e28ac5 | -2.30287 | -50.46418 | 2024-11-10 04:38:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 88c0182d-84f1-3689-8a14-de13b353cf95 | -4.41812 | -49.72499 | 2024-11-10 04:38:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| b084f500-cf4e-3f2e-99e1-ab9af0ef1111 | -2.82279 | -49.79012 | 2024-11-10 04:38:00 | NPP-375D | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 070eff6b-dae4-36aa-8b15-ee22f75e571a | -4.10712 | -49.12363 | 2024-11-10 04:38:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 6.8 |
| 11b8f884-af7f-30eb-89ce-6a947d68e8c7 | -3.72969 | -50.17323 | 2024-11-10 04:38:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 4ca7c326-d14c-3d8c-82d7-6e1c9ad8a268 | -4.90185 | -47.4698 | 2024-11-10 04:38:00 | NPP-375D | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ed31a70d-3858-39e7-b38b-2e8da34725ca | -4.49697 | -48.49499 | 2024-11-10 04:38:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 3dce461f-6425-3128-b917-8b451bd12135 | -3.2259 | -50.30682 | 2024-11-10 04:38:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 7b001f87-fed9-3b4f-95fc-20b5fd12995a | -4.71805 | -50.58717 | 2024-11-10 04:38:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 27fc7266-f53a-35e6-b89d-49242b7ba53a | -5.36874 | -47.91908 | 2024-11-10 04:38:00 | NPP-375D | SAMPAIO | TOCANTINS | Brasil | 1718808 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 55dcd354-3d6d-3f69-b0db-17321367d44d | -3.40528 | -50.01229 | 2024-11-10 04:38:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 3dab4894-dc99-3545-a439-3b4b8b5cf375 | -2.40591 | -49.37412 | 2024-11-10 04:38:00 | NPP-375D | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 4fddcd4d-7c07-378f-8446-c480ebf26c6d | -2.97023 | -49.35821 | 2024-11-10 04:38:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 64601119-936e-30ec-87eb-08d77e6f1a6a | -4.12287 | -43.59758 | 2024-11-10 04:38:00 | NPP-375D | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 1ccecd13-10e4-3a9c-acb3-e46eb0b9a58a | -2.89453 | -49.26075 | 2024-11-10 04:38:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| ee8b4419-b65e-38f0-9fb2-d6d00152116e | -2.46592 | -50.40904 | 2024-11-10 04:38:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 55d72867-465e-3833-9c2c-3fcbc539ec07 | -3.42426 | -50.31098 | 2024-11-10 04:38:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c74aaaf4-9087-3615-a8aa-b5680dac3e38 | -5.5663 | -43.97149 | 2024-11-10 04:38:00 | NPP-375D | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 7.6 |
| b503b309-75c7-336b-b115-ffeaf6254356 | -2.97216 | -51.45358 | 2024-11-10 04:38:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 17c94593-597e-36c6-a8c7-f2bb2be9cff0 | -2.83587 | -49.04871 | 2024-11-10 04:38:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 2f0ec065-7c03-3273-8595-817702f061d0 | -4.27366 | -48.18958 | 2024-11-10 04:38:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 1ef27280-22ed-3317-8bee-565bc46e093c | -2.29818 | -53.82095 | 2024-11-10 04:38:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 8ade868d-69bb-37b6-a8e4-f22776d027df | -5.24753 | -46.66254 | 2024-11-10 04:38:00 | NPP-375D | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 7ffc0524-ad98-3bc2-9388-418e2475b6c5 | -3.22523 | -50.68179 | 2024-11-10 04:38:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 12.3 |
| 2c60a67a-97d2-364d-8a7a-06063ff43940 | -3.2283 | -50.44642 | 2024-11-10 04:38:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 2b6cc383-4777-37b4-8907-d95ccc61647c | -2.23208 | -50.51951 | 2024-11-10 04:38:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 2b2fc790-40db-3442-ada6-c73d64819184 | -5.32671 | -44.84033 | 2024-11-10 04:38:00 | NPP-375D | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 007f2310-3182-3c53-a6b7-d8e2c54a62e2 | -2.67143 | -49.90184 | 2024-11-10 04:38:00 | NPP-375D | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 560fff53-68f2-3589-a6e6-4f4a6fa500d2 | -4.06379 | -48.23529 | 2024-11-10 04:38:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 6b61bcf2-44be-3372-8ac9-7972f947130c | -6.10127 | -44.75752 | 2024-11-10 04:38:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| b4365439-e036-3c00-ab7e-4e2b8902e619 | -4.37725 | -45.56768 | 2024-11-10 04:38:00 | NPP-375D | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| c53ae342-994c-3be4-ad0c-a50120cb054c | -4.37395 | -48.15195 | 2024-11-10 04:38:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 6e25db90-0f47-3359-8208-2627b6e16172 | -2.23614 | -50.51628 | 2024-11-10 04:38:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 22799746-9b4a-33b5-bd69-fd4c61d3061d | -3.92658 | -45.00895 | 2024-11-10 04:38:00 | NPP-375D | PIO XII | MARANHÃO | Brasil | 2108702 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| e4b90ba2-6233-37ad-8cf8-1ca2948462ae | -3.60332 | -50.23905 | 2024-11-10 04:38:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 0baed453-d34f-3caf-b709-5833affa51d5 | -4.59699 | -48.48184 | 2024-11-10 04:38:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |


[Clique aqui para ver as próximas entradas](README75.md)
