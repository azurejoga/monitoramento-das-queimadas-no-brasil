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

## Dados Diários - Página 48

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 3bfe6828-b0c2-37e5-bc85-72eb203140a7 | -19.5546 | -40.22416 | 2024-10-02 03:08:00 | NOAA-21 | LINHARES | ESPÍRITO SANTO | Brasil | 3203205 | 32 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 70c71079-c8b5-361c-90fe-e78898e6a86c | -19.73453 | -41.65093 | 2024-10-02 03:08:00 | NOAA-21 | TAPARUBA | MINAS GERAIS | Brasil | 3168051 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.3 |
| d4b1d4e3-6a23-3129-8fcd-73f73567cd20 | -19.73554 | -41.65331 | 2024-10-02 03:08:00 | NOAA-21 | TAPARUBA | MINAS GERAIS | Brasil | 3168051 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| b0675feb-df4d-393e-ad68-5d9a38d0dfb9 | -19.73699 | -41.64724 | 2024-10-02 03:08:00 | NOAA-21 | TAPARUBA | MINAS GERAIS | Brasil | 3168051 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.3 |
| 859dacda-6a01-3688-a870-416a26110d49 | -19.76034 | -42.00521 | 2024-10-02 03:08:00 | NOAA-21 | CARATINGA | MINAS GERAIS | Brasil | 3113404 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| 225b54cd-c6cd-323f-906b-35cbcd1dc4e2 | -19.76047 | -42.00674 | 2024-10-02 03:08:00 | NOAA-21 | PIEDADE DE CARATINGA | MINAS GERAIS | Brasil | 3150158 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| 57f4088c-2e50-3538-b353-4953c8f3f282 | -19.86975 | -42.34848 | 2024-10-02 03:08:00 | NOAA-21 | BOM JESUS DO GALHO | MINAS GERAIS | Brasil | 3107802 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.4 |
| 7f4411e8-a295-3fd6-b832-2aabd5b958d3 | -19.87821 | -43.15639 | 2024-10-02 03:08:00 | NOAA-21 | JOÃO MONLEVADE | MINAS GERAIS | Brasil | 3136207 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.4 |
| 64d76186-f257-3943-a9b7-fa19afeb2835 | -19.88486 | -43.15894 | 2024-10-02 03:08:00 | NOAA-21 | JOÃO MONLEVADE | MINAS GERAIS | Brasil | 3136207 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.3 |
| fd2e176a-dffc-3cae-a710-40f45268d91c | -19.99216 | -43.54708 | 2024-10-02 03:08:00 | NOAA-21 | BARÃO DE COCAIS | MINAS GERAIS | Brasil | 3105400 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| c8a8fe1f-bf06-3be6-9cd1-7fe298e95441 | -19.91157 | -43.16872 | 2024-10-02 03:08:00 | NOAA-21 | RIO PIRACICABA | MINAS GERAIS | Brasil | 3155702 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.6 |
| a66da49d-1111-3377-aaae-76a5bce06bb2 | -19.9112 | -43.1688 | 2024-10-02 03:08:00 | NOAA-21 | RIO PIRACICABA | MINAS GERAIS | Brasil | 3155702 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.5 |
| a475868a-57e6-36b5-89a2-6a2c4769f0da | -19.89274 | -43.15524 | 2024-10-02 03:08:00 | NOAA-21 | RIO PIRACICABA | MINAS GERAIS | Brasil | 3155702 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.1 |
| d070a66f-260a-36ab-b849-609a88da7e24 | -17.70667 | -42.37808 | 2024-10-02 03:08:00 | NOAA-21 | CAPELINHA | MINAS GERAIS | Brasil | 3112307 | 31 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 1f7e5689-c076-3f5c-a612-345a1556eb10 | -17.70667 | -42.37797 | 2024-10-02 03:08:00 | NOAA-21 | CAPELINHA | MINAS GERAIS | Brasil | 3112307 | 31 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 8ca7d2c8-3b97-39c5-abcd-2b2e8c2e93dd | -16.37534 | -40.54296 | 2024-10-02 03:08:00 | NOAA-21 | RUBIM | MINAS GERAIS | Brasil | 3156601 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.1 |
| 35b92250-4f41-366d-ad4f-5c95540c98df | -19.74211 | -41.64711 | 2024-10-02 03:08:00 | NOAA-21 | TAPARUBA | MINAS GERAIS | Brasil | 3168051 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| 10a3e630-ca86-359f-97ac-b3a8c46a47f4 | -20.8604 | -41.67731 | 2024-10-02 03:08:00 | NOAA-21 | GUAÇUÍ | ESPÍRITO SANTO | Brasil | 3202306 | 32 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| 0c45c525-d8f3-35f9-ba04-d630b6f70c20 | -20.85428 | -41.6754 | 2024-10-02 03:08:00 | NOAA-21 | GUAÇUÍ | ESPÍRITO SANTO | Brasil | 3202306 | 32 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| 47649b3f-0e65-3da8-a917-bd24ca75bca9 | -20.35747 | -41.6661 | 2024-10-02 03:08:00 | NOAA-21 | IRUPI | ESPÍRITO SANTO | Brasil | 3202652 | 32 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| 15763511-96e4-3251-a40f-efdd2699febd | -20.35689 | -42.76265 | 2024-10-02 03:08:00 | NOAA-21 | URUCÂNIA | MINAS GERAIS | Brasil | 3170503 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.3 |
| 9a101ea0-89d4-332e-a611-f821fd8804bc | -20.35256 | -42.76286 | 2024-10-02 03:08:00 | NOAA-21 | URUCÂNIA | MINAS GERAIS | Brasil | 3170503 | 31 | 33 | nan | nan | nan | Mata Atlântica | 8.8 |
| 8cc4ee64-60e9-3de2-9029-5d7d07406c1d | -20.35023 | -42.761 | 2024-10-02 03:08:00 | NOAA-21 | URUCÂNIA | MINAS GERAIS | Brasil | 3170503 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.3 |
| 20ddf8e9-3f87-3355-9afc-f6b4eb0bee92 | -20.33861 | -42.15022 | 2024-10-02 03:08:00 | NOAA-21 | SÃO JOÃO DO MANHUAÇU | MINAS GERAIS | Brasil | 3162559 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| 5e646a08-2109-33e1-84a7-daeea1b2fcad | -20.33229 | -42.1481 | 2024-10-02 03:08:00 | NOAA-21 | SÃO JOÃO DO MANHUAÇU | MINAS GERAIS | Brasil | 3162559 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| 01a68fe4-8c81-37a9-9a5b-bd31f177a117 | -19.99349 | -43.54172 | 2024-10-02 03:08:00 | NOAA-21 | BARÃO DE COCAIS | MINAS GERAIS | Brasil | 3105400 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 6abf47cb-94c6-32f3-a350-f2876ea864ce | -18.06095 | -42.62158 | 2024-10-02 03:08:00 | NOAA-21 | SÃO SEBASTIÃO DO MARANHÃO | MINAS GERAIS | Brasil | 3164506 | 31 | 33 | nan | nan | nan | Mata Atlântica | 8.1 |
| 8cbef354-1646-3fa1-ba78-695a0f44d7cf | -18.06234 | -42.61571 | 2024-10-02 03:08:00 | NOAA-21 | SÃO SEBASTIÃO DO MARANHÃO | MINAS GERAIS | Brasil | 3164506 | 31 | 33 | nan | nan | nan | Mata Atlântica | 8.1 |
| c25f8c7e-a959-3f1b-891b-2c4895bc9679 | -18.06374 | -42.60977 | 2024-10-02 03:08:00 | NOAA-21 | SÃO SEBASTIÃO DO MARANHÃO | MINAS GERAIS | Brasil | 3164506 | 31 | 33 | nan | nan | nan | Mata Atlântica | 13.4 |
| 6530a7cb-cf69-35be-a1ba-c038344c4a9b | -18.06855 | -42.61719 | 2024-10-02 03:08:00 | NOAA-21 | SÃO SEBASTIÃO DO MARANHÃO | MINAS GERAIS | Brasil | 3164506 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| 6b7eabb8-7434-3ba7-9606-223559f42189 | -22.76682 | -44.65852 | 2024-10-02 03:10:00 | NOAA-21 | SÃO JOSÉ DO BARREIRO | SÃO PAULO | Brasil | 3549607 | 35 | 33 | nan | nan | nan | Mata Atlântica | 6.8 |
| 29ea4350-ab76-378f-b436-b245543c7e1f | -22.76844 | -44.65231 | 2024-10-02 03:10:00 | NOAA-21 | SÃO JOSÉ DO BARREIRO | SÃO PAULO | Brasil | 3549607 | 35 | 33 | nan | nan | nan | Mata Atlântica | 6.8 |
| 22b9bbea-8395-3fe6-92d4-8fca75ef3281 | -22.76981 | -44.64702 | 2024-10-02 03:10:00 | NOAA-21 | SÃO JOSÉ DO BARREIRO | SÃO PAULO | Brasil | 3549607 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.6 |
| b977fa47-9727-3fe5-b01a-e0dc87c8e946 | -22.93418 | -43.73032 | 2024-10-02 03:10:00 | NOAA-21 | RIO DE JANEIRO | RIO DE JANEIRO | Brasil | 3304557 | 33 | 33 | nan | nan | nan | Mata Atlântica | 11.0 |
| b726495b-84d0-3d18-a4a0-9dcb71dd6107 | -22.93253 | -43.73672 | 2024-10-02 03:10:00 | NOAA-21 | RIO DE JANEIRO | RIO DE JANEIRO | Brasil | 3304557 | 33 | 33 | nan | nan | nan | Mata Atlântica | 11.0 |
| 165953c1-ab13-3346-90c8-c21f7dbf3727 | -22.93125 | -43.73167 | 2024-10-02 03:10:00 | NOAA-21 | RIO DE JANEIRO | RIO DE JANEIRO | Brasil | 3304557 | 33 | 33 | nan | nan | nan | Mata Atlântica | 14.2 |
| 8d73a9a1-af5b-3e5d-89e1-2ace4191a537 | -22.61119 | -43.9631 | 2024-10-02 03:10:00 | NOAA-21 | PIRAÍ | RIO DE JANEIRO | Brasil | 3304003 | 33 | 33 | nan | nan | nan | Mata Atlântica | 4.8 |
| 2261bd0a-4094-3c50-a987-036ab54e578c | -22.92964 | -43.73808 | 2024-10-02 03:10:00 | NOAA-21 | RIO DE JANEIRO | RIO DE JANEIRO | Brasil | 3304557 | 33 | 33 | nan | nan | nan | Mata Atlântica | 14.2 |
| d010dbcd-c655-3190-bd42-1626bb8c5a2a | -22.92755 | -43.72842 | 2024-10-02 03:10:00 | NOAA-21 | RIO DE JANEIRO | RIO DE JANEIRO | Brasil | 3304557 | 33 | 33 | nan | nan | nan | Mata Atlântica | 11.0 |
| 0ae66c05-d4ea-3ed7-9972-108fc622e3d6 | -22.92625 | -43.72331 | 2024-10-02 03:10:00 | NOAA-21 | RIO DE JANEIRO | RIO DE JANEIRO | Brasil | 3304557 | 33 | 33 | nan | nan | nan | Mata Atlântica | 7.3 |
| e2387d84-751a-3918-9b7e-5f95679314e8 | -22.77489 | -43.80496 | 2024-10-02 03:10:00 | NOAA-21 | ITAGUAÍ | RIO DE JANEIRO | Brasil | 3302007 | 33 | 33 | nan | nan | nan | Mata Atlântica | 4.4 |
| 97b9cc6a-fadb-3888-b2ed-6991b1c12569 | -22.77431 | -44.2362 | 2024-10-02 03:10:00 | NOAA-21 | RIO CLARO | RIO DE JANEIRO | Brasil | 3304409 | 33 | 33 | nan | nan | nan | Mata Atlântica | 13.7 |
| 750ae799-9c44-3b90-bbb7-4c7300257b8d | -22.77309 | -44.24092 | 2024-10-02 03:10:00 | NOAA-21 | RIO CLARO | RIO DE JANEIRO | Brasil | 3304409 | 33 | 33 | nan | nan | nan | Mata Atlântica | 13.7 |
| 6baa646a-5e95-3ea7-a577-c5c906962168 | -22.76987 | -43.79657 | 2024-10-02 03:10:00 | NOAA-21 | ITAGUAÍ | RIO DE JANEIRO | Brasil | 3302007 | 33 | 33 | nan | nan | nan | Mata Atlântica | 15.7 |
| af5912f7-da08-398f-af5c-4f058822b97f | -22.76859 | -43.8016 | 2024-10-02 03:10:00 | NOAA-21 | ITAGUAÍ | RIO DE JANEIRO | Brasil | 3302007 | 33 | 33 | nan | nan | nan | Mata Atlântica | 15.7 |
| 3299cccc-8e94-35b9-bdc8-536f24b71f75 | -22.76737 | -43.8064 | 2024-10-02 03:10:00 | NOAA-21 | ITAGUAÍ | RIO DE JANEIRO | Brasil | 3302007 | 33 | 33 | nan | nan | nan | Mata Atlântica | 14.0 |
| 4459fd55-fc96-3725-8412-16a2a6757ab4 | -22.76437 | -43.7619 | 2024-10-02 03:10:00 | NOAA-21 | SEROPÉDICA | RIO DE JANEIRO | Brasil | 3305554 | 33 | 33 | nan | nan | nan | Mata Atlântica | 3.7 |
| 90213daa-e1e1-3da3-86db-35211138e183 | -22.76308 | -43.76698 | 2024-10-02 03:10:00 | NOAA-21 | SEROPÉDICA | RIO DE JANEIRO | Brasil | 3305554 | 33 | 33 | nan | nan | nan | Mata Atlântica | 4.5 |
| 3eb1fd9a-a030-3ff1-9cf8-60a097a31b69 | -22.66945 | -43.7058 | 2024-10-02 03:10:00 | NOAA-21 | SEROPÉDICA | RIO DE JANEIRO | Brasil | 3305554 | 33 | 33 | nan | nan | nan | Mata Atlântica | 2.9 |
| 08cb2e8a-23c1-3dc2-b304-1a65e9975bf4 | -22.66725 | -43.71449 | 2024-10-02 03:10:00 | NOAA-21 | SEROPÉDICA | RIO DE JANEIRO | Brasil | 3305554 | 33 | 33 | nan | nan | nan | Mata Atlântica | 2.9 |
| 38a6e761-c901-33e9-a8d3-d5a047bdd663 | -22.6045 | -43.96093 | 2024-10-02 03:10:00 | NOAA-21 | PIRAÍ | RIO DE JANEIRO | Brasil | 3304003 | 33 | 33 | nan | nan | nan | Mata Atlântica | 3.6 |
| 1020a4d8-d967-32c5-9cdc-3a803dce6d9c | -22.52613 | -43.54884 | 2024-10-02 03:10:00 | NOAA-21 | MIGUEL PEREIRA | RIO DE JANEIRO | Brasil | 3302908 | 33 | 33 | nan | nan | nan | Mata Atlântica | 8.1 |
| 2facd02a-5315-3320-a016-32599519501c | -22.52184 | -43.54872 | 2024-10-02 03:10:00 | NOAA-21 | MIGUEL PEREIRA | RIO DE JANEIRO | Brasil | 3302908 | 33 | 33 | nan | nan | nan | Mata Atlântica | 9.1 |
| b6f6c35e-b990-35dc-ae7e-1f5132b764ed | -22.51191 | -43.83874 | 2024-10-02 03:10:00 | NOAA-21 | PIRAÍ | RIO DE JANEIRO | Brasil | 3304003 | 33 | 33 | nan | nan | nan | Mata Atlântica | 5.2 |
| 0a96f5ef-0d8f-3058-92a6-7ca1f2f5501c | -22.49785 | -43.54853 | 2024-10-02 03:10:00 | NOAA-21 | MIGUEL PEREIRA | RIO DE JANEIRO | Brasil | 3302908 | 33 | 33 | nan | nan | nan | Mata Atlântica | 15.3 |
| 49c4f888-2c1c-3a0d-acd1-aa4afef3ced7 | -22.49655 | -43.5537 | 2024-10-02 03:10:00 | NOAA-21 | VASSOURAS | RIO DE JANEIRO | Brasil | 3306206 | 33 | 33 | nan | nan | nan | Mata Atlântica | 15.3 |
| ae2c81fe-e67f-37cf-8ef7-7013d963fb4b | -22.49053 | -44.14842 | 2024-10-02 03:10:00 | NOAA-21 | VOLTA REDONDA | RIO DE JANEIRO | Brasil | 3306305 | 33 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| b7036571-9ba6-38b7-9f44-5024d9fafab2 | -22.49029 | -44.15174 | 2024-10-02 03:10:00 | NOAA-21 | VOLTA REDONDA | RIO DE JANEIRO | Brasil | 3306305 | 33 | 33 | nan | nan | nan | Mata Atlântica | 4.3 |
| 37619749-3cab-30a2-b9aa-33556b0a63ab | -22.48885 | -44.15486 | 2024-10-02 03:10:00 | NOAA-21 | BARRA MANSA | RIO DE JANEIRO | Brasil | 3300407 | 33 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| 61c9eae7-4b77-3aa9-a754-df0da74a6e4a | -22.45108 | -44.13314 | 2024-10-02 03:10:00 | NOAA-21 | VOLTA REDONDA | RIO DE JANEIRO | Brasil | 3306305 | 33 | 33 | nan | nan | nan | Mata Atlântica | 2.8 |
| cf591c20-9c6e-349c-a9ee-a0cd503565e0 | -22.38752 | -43.52423 | 2024-10-02 03:10:00 | NOAA-21 | VASSOURAS | RIO DE JANEIRO | Brasil | 3306206 | 33 | 33 | nan | nan | nan | Mata Atlântica | 6.7 |
| 6a08614a-0336-31db-ab39-f2d548317964 | -22.38021 | -43.52509 | 2024-10-02 03:10:00 | NOAA-21 | VASSOURAS | RIO DE JANEIRO | Brasil | 3306206 | 33 | 33 | nan | nan | nan | Mata Atlântica | 6.7 |
| 1903bc6d-8773-334b-8a55-5acefe6606d3 | -22.35581 | -44.02248 | 2024-10-02 03:10:00 | NOAA-21 | BARRA DO PIRAÍ | RIO DE JANEIRO | Brasil | 3300308 | 33 | 33 | nan | nan | nan | Mata Atlântica | 4.4 |
| 7c2bf560-2b57-3396-9c26-e057f2f46d82 | -22.35201 | -44.23159 | 2024-10-02 03:10:00 | NOAA-21 | QUATIS | RIO DE JANEIRO | Brasil | 3304128 | 33 | 33 | nan | nan | nan | Mata Atlântica | 3.9 |
| 7012f47b-7ed6-330c-a5bf-f6aa3c4644e1 | -21.67317 | -43.95868 | 2024-10-02 03:10:00 | NOAA-21 | LIMA DUARTE | MINAS GERAIS | Brasil | 3138609 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.6 |
| d2ca57ce-0cb0-343f-98a2-eecd23063063 | -21.61635 | -42.80737 | 2024-10-02 03:10:00 | NOAA-21 | ARGIRITA | MINAS GERAIS | Brasil | 3104403 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| 0aab58e9-03d6-3d76-9dc4-aea19e93387a | -21.61629 | -42.81415 | 2024-10-02 03:10:00 | NOAA-21 | ARGIRITA | MINAS GERAIS | Brasil | 3104403 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.7 |
| 29d0f8f1-7df9-35c2-a18a-583ac4696a4a | -21.61435 | -42.81536 | 2024-10-02 03:10:00 | NOAA-21 | ARGIRITA | MINAS GERAIS | Brasil | 3104403 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.3 |
| ddcc281e-3b7b-3926-8a6f-b3135444c2fb | -21.61328 | -42.8265 | 2024-10-02 03:10:00 | NOAA-21 | ARGIRITA | MINAS GERAIS | Brasil | 3104403 | 31 | 33 | nan | nan | nan | Mata Atlântica | 7.6 |
| 0b92c68a-6866-337e-b24c-527d27384344 | -21.61284 | -42.82138 | 2024-10-02 03:10:00 | NOAA-21 | ARGIRITA | MINAS GERAIS | Brasil | 3104403 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.3 |
| 8284424e-f13c-33a7-b67d-d21bf71717d6 | -21.61134 | -42.82739 | 2024-10-02 03:10:00 | NOAA-21 | ARGIRITA | MINAS GERAIS | Brasil | 3104403 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.5 |
| b1b2d5cd-2ab2-386a-9725-89ba658b1a2b | -21.56676 | -41.30075 | 2024-10-02 03:10:00 | NOAA-21 | CAMPOS DOS GOYTACAZES | RIO DE JANEIRO | Brasil | 3301009 | 33 | 33 | nan | nan | nan | Mata Atlântica | 8.2 |
| bdd9defc-da7c-3d64-b777-4eb269a874b1 | -21.56563 | -41.30031 | 2024-10-02 03:10:00 | NOAA-21 | CAMPOS DOS GOYTACAZES | RIO DE JANEIRO | Brasil | 3301009 | 33 | 33 | nan | nan | nan | Mata Atlântica | 9.1 |
| 49d65622-7f8d-300d-997d-e53db141f90c | -21.56562 | -41.30554 | 2024-10-02 03:10:00 | NOAA-21 | CAMPOS DOS GOYTACAZES | RIO DE JANEIRO | Brasil | 3301009 | 33 | 33 | nan | nan | nan | Mata Atlântica | 8.2 |
| a438751f-e1a1-37d2-ad6c-032ee29f5593 | -21.56453 | -41.30508 | 2024-10-02 03:10:00 | NOAA-21 | CAMPOS DOS GOYTACAZES | RIO DE JANEIRO | Brasil | 3301009 | 33 | 33 | nan | nan | nan | Mata Atlântica | 9.1 |
| d5de5eae-f472-3d27-a313-2059edc3ff4c | -21.55759 | -43.96128 | 2024-10-02 03:10:00 | NOAA-21 | SANTA RITA DE IBITIPOCA | MINAS GERAIS | Brasil | 3159407 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.5 |
| df1e6d74-d275-35a2-a140-d89648afb0c9 | -21.32751 | -41.41375 | 2024-10-02 03:10:00 | NOAA-21 | CAMPOS DOS GOYTACAZES | RIO DE JANEIRO | Brasil | 3301009 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 43aedcac-c171-3e18-b459-471bfa16b1c7 | -21.32161 | -41.41156 | 2024-10-02 03:10:00 | NOAA-21 | CAMPOS DOS GOYTACAZES | RIO DE JANEIRO | Brasil | 3301009 | 33 | 33 | nan | nan | nan | Mata Atlântica | 12.6 |
| 9b85e16b-38f0-3917-922d-d6465ec9a2b8 | -21.32103 | -41.41412 | 2024-10-02 03:10:00 | NOAA-21 | CAMPOS DOS GOYTACAZES | RIO DE JANEIRO | Brasil | 3301009 | 33 | 33 | nan | nan | nan | Mata Atlântica | 12.3 |
| 39367307-09ba-3832-94e7-4d0b7b95b9d1 | -21.32025 | -41.41726 | 2024-10-02 03:10:00 | NOAA-21 | CAMPOS DOS GOYTACAZES | RIO DE JANEIRO | Brasil | 3301009 | 33 | 33 | nan | nan | nan | Mata Atlântica | 12.6 |
| 219b09d7-8c50-311d-a649-0b0c8be6bae3 | -21.31962 | -41.42022 | 2024-10-02 03:10:00 | NOAA-21 | CAMPOS DOS GOYTACAZES | RIO DE JANEIRO | Brasil | 3301009 | 33 | 33 | nan | nan | nan | Mata Atlântica | 12.3 |
| b1cb274f-867e-3d9e-8f3a-40de66777aad | -20.9742 | -43.29946 | 2024-10-02 03:10:00 | NOAA-21 | ALTO RIO DOCE | MINAS GERAIS | Brasil | 3102100 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.4 |
| 6d409ac2-589a-39ec-b48d-fd49a463ac11 | -20.97281 | -43.30512 | 2024-10-02 03:10:00 | NOAA-21 | ALTO RIO DOCE | MINAS GERAIS | Brasil | 3102100 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.4 |
| 09bb1ab4-f699-368f-a664-fecdee51d130 | -20.82008 | -42.30144 | 2024-10-02 03:10:00 | NOAA-21 | SÃO FRANCISCO DO GLÓRIA | MINAS GERAIS | Brasil | 3161403 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.3 |
| e7c4036e-40be-3834-b85c-7fe8e5ebbb13 | -20.81387 | -42.29892 | 2024-10-02 03:10:00 | NOAA-21 | SÃO FRANCISCO DO GLÓRIA | MINAS GERAIS | Brasil | 3161403 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.3 |
| c57e9f87-a813-30ea-af69-15795c166537 | -3.2136 | -46.7843 | 2024-10-02 03:15:24 | GOES-16 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 65.2 |
| d5b1c525-00bd-3046-811b-f4c7002a4f15 | -8.4643 | -62.7124 | 2024-10-02 03:15:54 | GOES-16 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 42.6 |
| af4ae591-6c24-3699-9b55-56ad8b85782e | -10.0799 | -46.8561 | 2024-10-02 03:16:03 | GOES-16 | SÃO FÉLIX DO TOCANTINS | TOCANTINS | Brasil | 1720150 | 17 | 33 | nan | nan | nan | Cerrado | 61.7 |
| 78d64028-5f93-3457-a6f4-1949500ea45e | -9.9367 | -64.9179 | 2024-10-02 03:16:03 | GOES-16 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 87.9 |
| 93a266e1-40ab-3918-b402-60ed2c6f2f5d | -9.9368 | -64.8991 | 2024-10-02 03:16:03 | GOES-16 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 65.1 |
| 7bc5abfa-e1cc-3a4b-86bc-2844bbe1fc6c | -9.9553 | -64.9172 | 2024-10-02 03:16:03 | GOES-16 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 74.8 |
| 8bbf92e2-542c-36bb-85e7-25e207f818fe | -9.9554 | -64.8984 | 2024-10-02 03:16:03 | GOES-16 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 68.3 |
| 6556ed25-6b9c-33da-8215-6b6d993ca89e | -11.6743 | -64.9983 | 2024-10-02 03:16:13 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 64.7 |
| abdcebeb-3e00-3599-a8d4-36ed6f7298a9 | -12.6484 | -63.1214 | 2024-10-02 03:16:18 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 85.7 |
| edb97471-39f2-37dd-80d6-1c54b887d35a | -12.7054 | -63.0798 | 2024-10-02 03:16:18 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 61.5 |
| 5da935eb-f64a-3f79-a200-024d91e009ab | -12.8423 | -62.5526 | 2024-10-02 03:16:19 | GOES-16 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 70.7 |
| e3e5af67-79b8-3689-bb15-d4b77674d82b | -12.8424 | -62.5333 | 2024-10-02 03:16:19 | GOES-16 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 106.9 |
| c0c8db22-9d33-3315-9929-94b47fbf56de | -12.8612 | -62.5514 | 2024-10-02 03:16:19 | GOES-16 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 78.0 |
| 4ee188f0-7d57-35f5-aa77-dd07b711f309 | -12.8614 | -62.5321 | 2024-10-02 03:16:19 | GOES-16 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 143.3 |
| b276c7b1-eb7a-36a3-a03f-5d54f7f4a539 | -12.8615 | -62.5129 | 2024-10-02 03:16:19 | GOES-16 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 44.1 |


[Clique aqui para ver as próximas entradas](README49.md)
