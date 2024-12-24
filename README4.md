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

## Dados Diários - Página 4

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 7b38f8c7-5e35-3d1c-b834-e96d9a98303a | -2.85195 | -46.74236 | 2024-12-24 03:46:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 3027d088-1b3c-3e2a-b698-df6849c0fa56 | -2.7649 | -45.1044 | 2024-12-24 03:46:00 | NOAA-21 | PALMEIRÂNDIA | MARANHÃO | Brasil | 2107605 | 21 | 33 | nan | nan | nan | Amazônia | 8.0 |
| f7f7426c-b3b0-3ac9-9a5a-f37841f60f1e | -2.85783 | -46.74325 | 2024-12-24 03:46:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 22766ca7-dd2d-3d3e-9fc0-0bf2c4cbc18a | -2.11157 | -45.49214 | 2024-12-24 03:46:00 | NOAA-21 | TURILÂNDIA | MARANHÃO | Brasil | 2112456 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 011ee51c-4ce6-3777-892e-a7aeaadc7947 | -6.97027 | -43.54675 | 2024-12-24 03:49:00 | NOAA-21 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 5.4 |
| c535b588-be3c-3a37-8d81-2dccb82d87d2 | -10.6506 | -37.1163 | 2024-12-24 03:49:00 | NOAA-21 | DIVINA PASTORA | SERGIPE | Brasil | 2802007 | 28 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| e934be2d-7a34-37c0-9128-12afa93950fa | -6.95699 | -43.54458 | 2024-12-24 03:49:00 | NOAA-21 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| a2e335a4-441c-313e-9a96-d340bc561945 | -4.52422 | -45.82544 | 2024-12-24 03:49:00 | NOAA-21 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 3.1 |
| e3ae3d9c-d35b-3552-ada2-aad47dbad564 | -10.65006 | -37.11984 | 2024-12-24 03:49:00 | NOAA-21 | DIVINA PASTORA | SERGIPE | Brasil | 2802007 | 28 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 79034a9e-af85-356a-8557-f1cd5a9cd1d2 | -4.74957 | -45.3037 | 2024-12-24 03:49:00 | NOAA-21 | LAGO DA PEDRA | MARANHÃO | Brasil | 2105708 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| b8721881-5487-3d7a-8a42-c3cf12bf9b9a | -7.91258 | -35.21343 | 2024-12-24 03:49:00 | NOAA-21 | PAUDALHO | PERNAMBUCO | Brasil | 2610608 | 26 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 24a18a52-5028-3c95-a5b5-c50d35a85b29 | -6.20084 | -42.63513 | 2024-12-24 03:49:00 | NOAA-21 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 55f26975-de21-33d2-aedb-99c4c9ba35c0 | -6.66169 | -39.78868 | 2024-12-24 03:49:00 | NOAA-21 | SABOEIRO | CEARÁ | Brasil | 2311900 | 23 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 02af1558-9c0f-3825-8ec3-17762909315e | -6.20798 | -42.64425 | 2024-12-24 03:49:00 | NOAA-21 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 3.7 |
| f7755a5f-114b-3b39-9360-ab54e3470b21 | -10.62557 | -37.05833 | 2024-12-24 03:49:00 | NOAA-21 | ROSÁRIO DO CATETE | SERGIPE | Brasil | 2806107 | 28 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| d6312d75-2a23-3c8b-bed5-e66c26eab4cb | -6.20928 | -42.63641 | 2024-12-24 03:49:00 | NOAA-21 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 4.2 |
| 84119488-e14e-3a83-ba4d-622a36a92586 | -8.05944 | -35.12286 | 2024-12-24 03:49:00 | NOAA-21 | SÃO LOURENÇO DA MATA | PERNAMBUCO | Brasil | 2613701 | 26 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 8cc63806-9a0d-3ea6-8f8c-901c716ef58e | -9.16401 | -35.4904 | 2024-12-24 03:49:00 | NOAA-21 | MATRIZ DE CAMARAGIBE | ALAGOAS | Brasil | 2705101 | 27 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| d198718e-27dc-3d1d-8cd0-262a0b2b033b | -10.14653 | -36.41249 | 2024-12-24 03:49:00 | NOAA-21 | PENEDO | ALAGOAS | Brasil | 2706703 | 27 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| b480e2e2-1ecc-36b7-80fb-e7f6fb900c6a | -7.24456 | -37.4367 | 2024-12-24 03:49:00 | NOAA-21 | MÃE D'ÁGUA | PARAÍBA | Brasil | 2508703 | 25 | 33 | nan | nan | nan | Caatinga | 1.9 |
| d4bb52b3-dbca-3577-8c5b-6301fb38b5c2 | -9.15758 | -40.96275 | 2024-12-24 03:49:00 | NOAA-21 | CASA NOVA | BAHIA | Brasil | 2907202 | 29 | 33 | nan | nan | nan | Caatinga | 4.1 |
| 449c4d6e-ffe3-34ee-b0c7-f2376e478f50 | -6.96847 | -43.55376 | 2024-12-24 03:49:00 | NOAA-21 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 7.4 |
| f9ec7bd6-5aa7-3e50-b220-78a3a7655b5c | -9.01108 | -35.43691 | 2024-12-24 03:49:00 | NOAA-21 | PORTO CALVO | ALAGOAS | Brasil | 2707305 | 27 | 33 | nan | nan | nan | Mata Atlântica | 2.5 |
| 34e6015b-ac3f-36ec-8b22-98bf7608a3ca | -4.7501 | -45.30066 | 2024-12-24 03:49:00 | NOAA-21 | LAGO DA PEDRA | MARANHÃO | Brasil | 2105708 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 3c3d639e-ce15-38f0-9261-e50186599191 | -6.97469 | -43.54749 | 2024-12-24 03:49:00 | NOAA-21 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 5.4 |
| cd315d32-a298-3e7a-936b-6e341c24290f | -5.42508 | -40.74797 | 2024-12-24 03:49:00 | NOAA-21 | CRATEÚS | CEARÁ | Brasil | 2304103 | 23 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 64abb5fc-092d-33e4-8c56-b3c8643567bc | -6.99394 | -43.26966 | 2024-12-24 03:49:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 28550d16-7842-3871-bf4f-987d20aa1b06 | -6.94961 | -43.53435 | 2024-12-24 03:49:00 | NOAA-21 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 21e7d723-5b2c-3293-917b-49c5fd60142d | -6.69276 | -39.11861 | 2024-12-24 03:49:00 | NOAA-21 | CEDRO | CEARÁ | Brasil | 2303808 | 23 | 33 | nan | nan | nan | Caatinga | 3.2 |
| aa3e03b5-50f0-3280-a699-3c3baaa686fe | -7.2418 | -37.43272 | 2024-12-24 03:49:00 | NOAA-21 | MÃE D'ÁGUA | PARAÍBA | Brasil | 2508703 | 25 | 33 | nan | nan | nan | Caatinga | 1.9 |
| ade2cce2-3bb2-3b05-b0d0-4d382c8d806e | -10.59521 | -36.76549 | 2024-12-24 03:49:00 | NOAA-21 | PIRAMBU | SERGIPE | Brasil | 2805307 | 28 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 11d65844-b987-36ef-bbbd-e34eeb6da8a5 | -10.79393 | -37.15674 | 2024-12-24 03:49:00 | NOAA-21 | LARANJEIRAS | SERGIPE | Brasil | 2803609 | 28 | 33 | nan | nan | nan | Mata Atlântica | 12.0 |
| fd67d2bd-b83e-3cfe-bb99-6159fd70fc92 | -5.68585 | -39.0666 | 2024-12-24 03:49:00 | NOAA-21 | SOLONÓPOLE | CEARÁ | Brasil | 2313005 | 23 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 17bfca09-85b1-36fe-9392-fe46cfbf94b9 | -6.10721 | -44.75502 | 2024-12-24 03:49:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| abf19252-9e65-3f6d-ad8e-dad3c3a96d67 | -5.47692 | -39.66565 | 2024-12-24 03:49:00 | NOAA-21 | PEDRA BRANCA | CEARÁ | Brasil | 2310506 | 23 | 33 | nan | nan | nan | Caatinga | 2.1 |
| fa9a4afe-39c1-39b4-b66e-0388e69a194a | -5.53493 | -42.85517 | 2024-12-24 03:49:00 | NOAA-21 | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| addd626e-e596-3043-a315-5bfcc42d6677 | -6.95338 | -40.16224 | 2024-12-24 03:49:00 | NOAA-21 | CAMPOS SALES | CEARÁ | Brasil | 2302701 | 23 | 33 | nan | nan | nan | Caatinga | 2.1 |
| fb4cfc7c-ae1e-3be6-a54f-46b4da25bfbe | -4.529 | -45.82979 | 2024-12-24 03:49:00 | NOAA-21 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 3aafce68-e675-336a-9257-9d1007a88785 | -6.91793 | -43.53345 | 2024-12-24 03:49:00 | NOAA-21 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 9052fde1-9fa4-34e7-8cfa-c90bcf0c050c | -6.94444 | -43.53806 | 2024-12-24 03:49:00 | NOAA-21 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| f5a2a3ef-e19e-38c9-9e4f-bee98294f30e | -6.35303 | -38.083 | 2024-12-24 03:49:00 | NOAA-21 | ALEXANDRIA | RIO GRANDE DO NORTE | Brasil | 2400505 | 24 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 5d1a97ae-3f47-3b0b-af81-5a3200685cf6 | -6.91719 | -43.53781 | 2024-12-24 03:49:00 | NOAA-21 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 26878253-c33d-350d-b5d7-9030ce430e01 | -6.97367 | -43.55006 | 2024-12-24 03:49:00 | NOAA-21 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 7.4 |
| 6cab3961-2e9e-36c5-a82c-0b17a84df558 | -5.92129 | -38.1235 | 2024-12-24 03:49:00 | NOAA-21 | RODOLFO FERNANDES | RIO GRANDE DO NORTE | Brasil | 2411007 | 24 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 3670c34d-477b-3394-94c5-f141c2430ff1 | -7.87581 | -38.00795 | 2024-12-24 03:49:00 | NOAA-21 | TRIUNFO | PERNAMBUCO | Brasil | 2615706 | 26 | 33 | nan | nan | nan | Caatinga | 1.5 |
| c88c8d5b-6fe8-3cd2-bc40-bfba63dacac0 | -6.97323 | -43.55629 | 2024-12-24 03:49:00 | NOAA-21 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 4a377439-07d9-3900-9cd3-a2c1e51c8659 | -5.39319 | -42.94902 | 2024-12-24 03:49:00 | NOAA-21 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Caatinga | 2.4 |
| a441e336-c9f5-305e-a6ce-a7ed4366ad89 | -6.99465 | -43.26547 | 2024-12-24 03:49:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| ec174ef7-bfc1-3a4c-9420-28fea99ac5e9 | -9.16 | -35.49366 | 2024-12-24 03:49:00 | NOAA-21 | MATRIZ DE CAMARAGIBE | ALAGOAS | Brasil | 2705101 | 27 | 33 | nan | nan | nan | Mata Atlântica | 2.5 |
| f5cd70e1-e661-3779-90a7-5c40f8141851 | -4.33061 | -40.18958 | 2024-12-24 03:49:00 | NOAA-21 | SANTA QUITÉRIA | CEARÁ | Brasil | 2312205 | 23 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 35c90920-adab-3d8e-b82e-7ab0c28c8227 | -6.80545 | -35.55257 | 2024-12-24 03:49:00 | NOAA-21 | PIRPIRITUBA | PARAÍBA | Brasil | 2511806 | 25 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 9b9cb401-408d-346a-9bc5-e06d72bf7d88 | -6.25704 | -43.16174 | 2024-12-24 03:49:00 | NOAA-21 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Caatinga | 2.2 |
| ff4a8728-dd50-33ff-8d82-46a9515c724d | -4.33432 | -40.19017 | 2024-12-24 03:49:00 | NOAA-21 | SANTA QUITÉRIA | CEARÁ | Brasil | 2312205 | 23 | 33 | nan | nan | nan | Caatinga | 1.3 |
| d3d40365-10ed-3952-8cb0-12790247e85d | -6.98961 | -43.26893 | 2024-12-24 03:49:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| c7258589-2aff-3249-862e-fd998beb4450 | -6.9729 | -43.55446 | 2024-12-24 03:49:00 | NOAA-21 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 7.4 |
| 5b50d9b1-bdf2-3731-8a17-c8ce020a0b15 | -6.69216 | -39.12238 | 2024-12-24 03:49:00 | NOAA-21 | CEDRO | CEARÁ | Brasil | 2303808 | 23 | 33 | nan | nan | nan | Caatinga | 3.2 |
| 67799e4f-4fae-38c2-be60-27e052b83964 | -5.8975 | -35.8643 | 2024-12-24 03:49:00 | NOAA-21 | RUY BARBOSA | RIO GRANDE DO NORTE | Brasil | 2411106 | 24 | 33 | nan | nan | nan | Caatinga | 0.7 |
| d6f3a0bc-cea4-3f3f-b8ca-9c060156a7c4 | -10.79447 | -37.1532 | 2024-12-24 03:49:00 | NOAA-21 | LARANJEIRAS | SERGIPE | Brasil | 2803609 | 28 | 33 | nan | nan | nan | Mata Atlântica | 12.0 |
| 520fa20d-14d0-390c-81da-bffd084e6400 | -6.91352 | -43.5327 | 2024-12-24 03:49:00 | NOAA-21 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| f6ddf11e-3062-3644-90d7-dbdecaec8da2 | -5.99105 | -45.39467 | 2024-12-24 03:49:00 | NOAA-21 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 732805a2-9c2c-3f0c-abd6-35fdef1ddbec | -4.30245 | -40.69929 | 2024-12-24 03:49:00 | NOAA-21 | IPU | CEARÁ | Brasil | 2305803 | 23 | 33 | nan | nan | nan | Caatinga | 25.8 |
| 91eee933-69ef-3964-88b5-61d2b32d2f77 | -6.19599 | -42.63829 | 2024-12-24 03:49:00 | NOAA-21 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 7.6 |
| f6374119-e908-3eb5-9aad-85eae4644ad1 | -6.92309 | -43.52985 | 2024-12-24 03:49:00 | NOAA-21 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| fc4e9b4c-c6d7-3309-a222-6190ee8c7e3f | -7.38284 | -37.46537 | 2024-12-24 03:49:00 | NOAA-21 | SANTA TEREZINHA | PERNAMBUCO | Brasil | 2612802 | 26 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 160661f5-a015-3b0e-8e3d-5447239fddea | -6.68872 | -39.1218 | 2024-12-24 03:49:00 | NOAA-21 | CEDRO | CEARÁ | Brasil | 2303808 | 23 | 33 | nan | nan | nan | Caatinga | 3.2 |
| bfbb378c-e2e8-3963-8d54-2ccc6c5d0f2c | -6.96953 | -43.55117 | 2024-12-24 03:49:00 | NOAA-21 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 6.1 |
| fbdb3a40-c49d-3582-8d30-4f65b12f3738 | -6.95772 | -43.54016 | 2024-12-24 03:49:00 | NOAA-21 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 454e12c0-c9e4-3d87-aff0-98dbf78effae | -6.98456 | -43.27242 | 2024-12-24 03:49:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| caff78be-5e4d-31b6-835a-afd4b504947f | -5.04132 | -37.77365 | 2024-12-24 03:49:00 | NOAA-21 | QUIXERÉ | CEARÁ | Brasil | 2311504 | 23 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 5e3cc6ca-5c82-3d78-a6da-e7335a4246ee | -6.97396 | -43.55189 | 2024-12-24 03:49:00 | NOAA-21 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 6.1 |
| d8085ac7-8df6-37d0-aeb5-a61ba6c1193c | -7.2385 | -37.43219 | 2024-12-24 03:49:00 | NOAA-21 | MÃE D'ÁGUA | PARAÍBA | Brasil | 2508703 | 25 | 33 | nan | nan | nan | Caatinga | 5.1 |
| 3c425609-8421-3e60-aa9e-d0342bc60c98 | -5.39787 | -37.77927 | 2024-12-24 03:49:00 | NOAA-21 | APODI | RIO GRANDE DO NORTE | Brasil | 2401008 | 24 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 4cc66ce5-0ae8-33bf-b6dc-571f489c2337 | -7.82052 | -35.19633 | 2024-12-24 03:49:00 | NOAA-21 | TRACUNHAÉM | PERNAMBUCO | Brasil | 2615508 | 26 | 33 | nan | nan | nan | Mata Atlântica | 5.4 |
| 8960586d-9df7-348b-a809-69c5f78dc256 | -7.97872 | -38.67098 | 2024-12-24 03:49:00 | NOAA-21 | SÃO JOSÉ DO BELMONTE | PERNAMBUCO | Brasil | 2613503 | 26 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 97b97383-bd83-3bd3-bbbf-3dd330bca1b9 | -4.52361 | -45.82896 | 2024-12-24 03:49:00 | NOAA-21 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 90cc8f98-74f7-34ee-b0ab-9288b8b93ecc | -4.52648 | -45.8289 | 2024-12-24 03:49:00 | NOAA-21 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 5ab2f6be-fecd-32ac-979a-be6a2b646955 | -5.87842 | -43.87978 | 2024-12-24 03:49:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 10a71e4b-e382-3ef6-bc09-887bbe43c35b | -4.57329 | -45.86199 | 2024-12-24 03:49:00 | NOAA-21 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| fcbe4849-aa5f-3394-9b59-4ec44db16b01 | -8.50155 | -36.92279 | 2024-12-24 03:49:00 | NOAA-21 | PEDRA | PERNAMBUCO | Brasil | 2610806 | 26 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 22115b77-16f8-3b37-8f8d-eac303f02554 | -6.94887 | -43.53876 | 2024-12-24 03:49:00 | NOAA-21 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 8e151a6d-2770-3f48-b787-41a9b5e32b15 | -6.19665 | -42.63432 | 2024-12-24 03:49:00 | NOAA-21 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 4.8 |
| e2956a64-e412-3b67-bf58-e4ed3c9b46f6 | -6.9696 | -42.99599 | 2024-12-24 03:49:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 3.3 |
| ca408aee-1c1f-3052-ba76-4f88ddefa011 | -6.96924 | -43.54934 | 2024-12-24 03:49:00 | NOAA-21 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 7.4 |
| b7297191-893d-371c-80c5-3cad6c9764a1 | -9.02655 | -39.93393 | 2024-12-24 03:49:00 | NOAA-21 | CURAÇÁ | BAHIA | Brasil | 2909901 | 29 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 80b7a3bc-ee09-3c5e-b241-7997352015da | -7.87892 | -35.25053 | 2024-12-24 03:49:00 | NOAA-21 | CARPINA | PERNAMBUCO | Brasil | 2604007 | 26 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 5e6fb726-bb94-3393-bad1-e7048ec18e31 | -5.60642 | -35.63546 | 2024-12-24 03:49:00 | NOAA-21 | TAIPU | RIO GRANDE DO NORTE | Brasil | 2413904 | 24 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 0041e33f-e340-3bd6-af2d-17cfac2b2b1a | -10.79115 | -37.15268 | 2024-12-24 03:49:00 | NOAA-21 | LARANJEIRAS | SERGIPE | Brasil | 2803609 | 28 | 33 | nan | nan | nan | Mata Atlântica | 12.4 |
| 80cbee4b-4652-3e3b-93ae-204558f3c589 | -6.21286 | -42.6409 | 2024-12-24 03:49:00 | NOAA-21 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 3.7 |
| aa0dedb0-5723-3449-93f4-db779789093a | -9.43042 | -35.51455 | 2024-12-24 03:49:00 | NOAA-21 | BARRA DE SANTO ANTÔNIO | ALAGOAS | Brasil | 2700508 | 27 | 33 | nan | nan | nan | Mata Atlântica | 3.1 |
| 7bc747be-cd10-3d3e-b83f-16d6afc3ec3b | -7.82453 | -35.19307 | 2024-12-24 03:49:00 | NOAA-21 | PAUDALHO | PERNAMBUCO | Brasil | 2610608 | 26 | 33 | nan | nan | nan | Mata Atlântica | 13.2 |
| f44fc663-abde-32a6-8967-0e27338dda50 | -5.39454 | -37.77874 | 2024-12-24 03:49:00 | NOAA-21 | APODI | RIO GRANDE DO NORTE | Brasil | 2401008 | 24 | 33 | nan | nan | nan | Caatinga | 1.0 |
| a34824f4-509c-3a63-8e88-666dbb92d095 | -7.88243 | -38.54837 | 2024-12-24 03:49:00 | NOAA-21 | SERRA TALHADA | PERNAMBUCO | Brasil | 2613909 | 26 | 33 | nan | nan | nan | Caatinga | 19.7 |
| bccad6e7-175e-34bf-934c-40f0f043d54f | -6.9688 | -43.55558 | 2024-12-24 03:49:00 | NOAA-21 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 4d3a0687-c600-3374-9866-78386d272af1 | -6.08939 | -43.69448 | 2024-12-24 03:49:00 | NOAA-21 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| f517a9a8-1b2e-3b31-960d-5fb6e42d72d8 | -6.9533 | -43.53945 | 2024-12-24 03:49:00 | NOAA-21 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| fb708abc-015f-3b5b-ab21-6388eb21d841 | -8.05887 | -35.12666 | 2024-12-24 03:49:00 | NOAA-21 | SÃO LOURENÇO DA MATA | PERNAMBUCO | Brasil | 2613701 | 26 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 9acf8dbe-d16d-34fb-ab30-bb9db35d8b9e | -6.64283 | -39.54342 | 2024-12-24 03:49:00 | NOAA-21 | CARIÚS | CEARÁ | Brasil | 2303303 | 23 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 0322f04c-ee35-3ccb-a37b-7a331f07d7fe | -6.2015 | -42.6312 | 2024-12-24 03:49:00 | NOAA-21 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 973cd229-878c-3462-96dc-de7a523d4134 | -5.73576 | -44.10987 | 2024-12-24 03:49:00 | NOAA-21 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 59dcebf4-8727-3bf7-9efd-756c02b2fc95 | -7.89947 | -37.57651 | 2024-12-24 03:49:00 | NOAA-21 | CUSTÓDIA | PERNAMBUCO | Brasil | 2605103 | 26 | 33 | nan | nan | nan | Caatinga | 3.9 |


[Clique aqui para ver as próximas entradas](README5.md)
