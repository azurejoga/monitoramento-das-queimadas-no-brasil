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

## Dados Diários - Página 9

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 5f2e6307-a0e4-3bea-9dc8-97bdc854676d | -3.85713 | -40.45246 | 2024-12-10 03:12:00 | NOAA-21 | CARIRÉ | CEARÁ | Brasil | 2303105 | 23 | 33 | nan | nan | nan | Caatinga | 4.0 |
| ef76a31a-5d19-36b0-8b98-81721945ff00 | -9.02319 | -35.69736 | 2024-12-10 03:12:00 | NOAA-21 | COLÔNIA LEOPOLDINA | ALAGOAS | Brasil | 2702108 | 27 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| d77e019a-0989-3963-a43c-e0ad63f3d581 | -3.8532 | -40.44408 | 2024-12-10 03:12:00 | NOAA-21 | CARIRÉ | CEARÁ | Brasil | 2303105 | 23 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 37453082-5ca7-3220-a2ee-71cc5e759126 | -3.85134 | -40.44458 | 2024-12-10 03:12:00 | NOAA-21 | CARIRÉ | CEARÁ | Brasil | 2303105 | 23 | 33 | nan | nan | nan | Caatinga | 3.2 |
| 54a4ddc0-ce17-3162-9079-ce6159cdc339 | -9.17034 | -35.70312 | 2024-12-10 03:12:00 | NOAA-21 | SÃO LUÍS DO QUITUNDE | ALAGOAS | Brasil | 2708501 | 27 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| 21c78527-4433-3255-a5ab-c1282bb8e35a | -9.02401 | -35.69422 | 2024-12-10 03:12:00 | NOAA-21 | COLÔNIA LEOPOLDINA | ALAGOAS | Brasil | 2702108 | 27 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| 98466a51-475a-3c0e-ad30-6e76ba8f3191 | -6.16215 | -35.27505 | 2024-12-10 03:12:00 | NOAA-21 | SÃO JOSÉ DE MIPIBU | RIO GRANDE DO NORTE | Brasil | 2412203 | 24 | 33 | nan | nan | nan | Mata Atlântica | 8.7 |
| 15cae02d-efaf-3da3-bae0-09da3a011acc | -7.75143 | -35.1398 | 2024-12-10 03:12:00 | NOAA-21 | TRACUNHAÉM | PERNAMBUCO | Brasil | 2615508 | 26 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| 2de21cc1-906a-3508-a02b-9b711170b8dc | -8.80334 | -35.65881 | 2024-12-10 03:12:00 | NOAA-21 | XEXÉU | PERNAMBUCO | Brasil | 2616506 | 26 | 33 | nan | nan | nan | Mata Atlântica | 5.6 |
| cc1088c4-5dc9-3060-b493-171eabda6683 | -6.39924 | -35.20668 | 2024-12-10 03:12:00 | NOAA-21 | CANGUARETAMA | RIO GRANDE DO NORTE | Brasil | 2402204 | 24 | 33 | nan | nan | nan | Mata Atlântica | 2.3 |
| 17279234-4dbe-3923-9db4-dd19419ee6cc | -3.07107 | -40.04346 | 2024-12-10 03:12:00 | NOAA-21 | ACARAÚ | CEARÁ | Brasil | 2300200 | 23 | 33 | nan | nan | nan | Caatinga | 5.0 |
| cb286f9d-bc15-3593-8d2c-1c24f4a96b4f | -6.40038 | -35.20515 | 2024-12-10 03:12:00 | NOAA-21 | CANGUARETAMA | RIO GRANDE DO NORTE | Brasil | 2402204 | 24 | 33 | nan | nan | nan | Mata Atlântica | 5.2 |
| 14a2af8a-2549-390b-b4cf-e709c88bdc71 | -9.84246 | -36.18633 | 2024-12-10 03:14:00 | NOAA-21 | JEQUIÁ DA PRAIA | ALAGOAS | Brasil | 2703759 | 27 | 33 | nan | nan | nan | Mata Atlântica | 21.7 |
| e895dde9-d10c-3581-bdb6-63ff758dac4e | -10.45357 | -36.7966 | 2024-12-10 03:14:00 | NOAA-21 | JAPOATÃ | SERGIPE | Brasil | 2803401 | 28 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 11095a71-0bab-3740-9060-f6117bc6fd5b | -10.45574 | -36.78504 | 2024-12-10 03:14:00 | NOAA-21 | JAPOATÃ | SERGIPE | Brasil | 2803401 | 28 | 33 | nan | nan | nan | Mata Atlântica | 2.3 |
| 2d71270f-14c9-36ab-a39f-94c6e10827ca | -10.45396 | -36.7955 | 2024-12-10 03:14:00 | NOAA-21 | JAPOATÃ | SERGIPE | Brasil | 2803401 | 28 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| edba7641-3501-3d0f-a3fb-6b8fce0ce040 | -9.82063 | -36.27832 | 2024-12-10 03:14:00 | NOAA-21 | CAMPO ALEGRE | ALAGOAS | Brasil | 2701407 | 27 | 33 | nan | nan | nan | Mata Atlântica | 2.3 |
| d9393914-e505-3c68-9e3a-0e0bdd0edc5c | -10.46014 | -36.78918 | 2024-12-10 03:14:00 | NOAA-21 | JAPOATÃ | SERGIPE | Brasil | 2803401 | 28 | 33 | nan | nan | nan | Mata Atlântica | 3.0 |
| 1d74f94d-4b40-3ef0-964c-ededbb75a4f9 | -10.45961 | -36.79202 | 2024-12-10 03:14:00 | NOAA-21 | JAPOATÃ | SERGIPE | Brasil | 2803401 | 28 | 33 | nan | nan | nan | Mata Atlântica | 3.0 |
| da7733f4-745b-393b-b7a8-92bac52369fa | -10.45411 | -36.79374 | 2024-12-10 03:14:00 | NOAA-21 | JAPOATÃ | SERGIPE | Brasil | 2803401 | 28 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 3f41009b-c574-348b-9418-c34b42cf64c2 | -10.45606 | -36.78385 | 2024-12-10 03:14:00 | NOAA-21 | JAPOATÃ | SERGIPE | Brasil | 2803401 | 28 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 0cb46b6b-35aa-3352-8a8e-d37eb9da1374 | -13.12182 | -39.81054 | 2024-12-10 03:14:00 | NOAA-21 | BREJÕES | BAHIA | Brasil | 2904308 | 29 | 33 | nan | nan | nan | Mata Atlântica | 2.8 |
| e5fadecc-1005-3c40-bbe2-2d7866c62a10 | -13.83237 | -41.79862 | 2024-12-10 03:14:00 | NOAA-21 | DOM BASÍLIO | BAHIA | Brasil | 2910107 | 29 | 33 | nan | nan | nan | Caatinga | 3.5 |
| 397a61c0-4e64-3013-88b2-7bbf6e1a4006 | -15.65546 | -39.19122 | 2024-12-10 03:14:00 | NOAA-21 | CANAVIEIRAS | BAHIA | Brasil | 2906303 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 7a40cc49-de83-34d2-9b27-d511a2f0f565 | -9.83761 | -36.18542 | 2024-12-10 03:14:00 | NOAA-21 | JEQUIÁ DA PRAIA | ALAGOAS | Brasil | 2703759 | 27 | 33 | nan | nan | nan | Mata Atlântica | 21.7 |
| a0efc155-b584-3382-9480-959fbd2a1ec6 | -13.10292 | -43.31536 | 2024-12-10 03:14:00 | NOAA-21 | BOM JESUS DA LAPA | BAHIA | Brasil | 2903904 | 29 | 33 | nan | nan | nan | Caatinga | 6.4 |
| 67404eca-a292-3027-af92-a652aeb8471e | -10.45448 | -36.79259 | 2024-12-10 03:14:00 | NOAA-21 | JAPOATÃ | SERGIPE | Brasil | 2803401 | 28 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| de583087-4b8f-3b4d-9c55-1b55504010b6 | -10.75112 | -37.83306 | 2024-12-10 03:14:00 | NOAA-21 | SIMÃO DIAS | SERGIPE | Brasil | 2807105 | 28 | 33 | nan | nan | nan | Caatinga | 5.6 |
| 0ffcc5f6-8cbe-3b4c-8967-590fb44014de | -10.45996 | -36.7909 | 2024-12-10 03:14:00 | NOAA-21 | JAPOATÃ | SERGIPE | Brasil | 2803401 | 28 | 33 | nan | nan | nan | Mata Atlântica | 2.5 |
| 45050f77-9334-3620-b594-9e897f97e7d6 | -9.83558 | -36.19651 | 2024-12-10 03:14:00 | NOAA-21 | JEQUIÁ DA PRAIA | ALAGOAS | Brasil | 2703759 | 27 | 33 | nan | nan | nan | Mata Atlântica | 41.3 |
| 0b7352bd-0f90-3d46-85d1-33a4bb3e6782 | -10.45945 | -36.79375 | 2024-12-10 03:14:00 | NOAA-21 | JAPOATÃ | SERGIPE | Brasil | 2803401 | 28 | 33 | nan | nan | nan | Mata Atlântica | 2.4 |
| 8845dec5-546c-3cf2-a5a5-052a5ff520d0 | -10.45164 | -36.77967 | 2024-12-10 03:14:00 | NOAA-21 | JAPOATÃ | SERGIPE | Brasil | 2803401 | 28 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| bb944bf5-864e-32af-ae37-8de56b9af13d | -13.12199 | -39.80906 | 2024-12-10 03:14:00 | NOAA-21 | BREJÕES | BAHIA | Brasil | 2904308 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| dee20963-b7ec-3741-9d68-06f776bd1cde | -9.8366 | -36.19094 | 2024-12-10 03:14:00 | NOAA-21 | JEQUIÁ DA PRAIA | ALAGOAS | Brasil | 2703759 | 27 | 33 | nan | nan | nan | Mata Atlântica | 41.3 |
| d9ba8c9e-618f-3e71-826a-8678e666d99e | -15.65617 | -39.18776 | 2024-12-10 03:14:00 | NOAA-21 | CANAVIEIRAS | BAHIA | Brasil | 2906303 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 18466324-8293-3a23-ba43-d3a099ec0336 | -9.84144 | -36.19194 | 2024-12-10 03:14:00 | NOAA-21 | JEQUIÁ DA PRAIA | ALAGOAS | Brasil | 2703759 | 27 | 33 | nan | nan | nan | Mata Atlântica | 41.3 |
| 3890c1fe-9b11-320e-9d1a-9fd4fd3e0b22 | -13.1014 | -43.32237 | 2024-12-10 03:14:00 | NOAA-21 | BOM JESUS DA LAPA | BAHIA | Brasil | 2903904 | 29 | 33 | nan | nan | nan | Caatinga | 10.1 |
| e9f5d35a-3742-3004-8195-027cd2cae26f | -10.45111 | -36.78262 | 2024-12-10 03:14:00 | NOAA-21 | JAPOATÃ | SERGIPE | Brasil | 2803401 | 28 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| c63407ea-6e77-3c10-84be-d63efff3cb4d | -13.12094 | -39.81502 | 2024-12-10 03:14:00 | NOAA-21 | BREJÕES | BAHIA | Brasil | 2904308 | 29 | 33 | nan | nan | nan | Mata Atlântica | 3.3 |
| c15b3e88-4f3b-32a3-934c-56f1f68da05a | -10.46047 | -36.78804 | 2024-12-10 03:14:00 | NOAA-21 | JAPOATÃ | SERGIPE | Brasil | 2803401 | 28 | 33 | nan | nan | nan | Mata Atlântica | 2.5 |
| f23d212d-53a7-36e0-8958-9911eab80889 | -12.78039 | -38.49814 | 2024-12-10 03:14:00 | NOAA-21 | CANDEIAS | BAHIA | Brasil | 2906501 | 29 | 33 | nan | nan | nan | Mata Atlântica | 2.5 |
| b0836745-2385-3d01-bf8a-d47b68e3a043 | -13.12108 | -39.81353 | 2024-12-10 03:14:00 | NOAA-21 | BREJÕES | BAHIA | Brasil | 2904308 | 29 | 33 | nan | nan | nan | Mata Atlântica | 3.5 |
| e2766975-4b5f-3435-9d4b-946b665ea226 | -8.88423 | -41.10974 | 2024-12-10 03:14:00 | NOAA-21 | CASA NOVA | BAHIA | Brasil | 2907202 | 29 | 33 | nan | nan | nan | Caatinga | 3.0 |
| cd7b7ed7-8f35-3126-b04f-cd2ca21cd1a6 | -17.78766 | -40.44375 | 2024-12-10 03:17:00 | NOAA-21 | NANUQUE | MINAS GERAIS | Brasil | 3144300 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| eb415da6-b995-3523-b8b4-098a1a7e484f | -18.73657 | -39.90911 | 2024-12-10 03:17:00 | NOAA-21 | SÃO MATEUS | ESPÍRITO SANTO | Brasil | 3204906 | 32 | 33 | nan | nan | nan | Mata Atlântica | 3.8 |
| f906c4e1-82a8-3715-afac-47593a0b2ca7 | -18.73586 | -39.91251 | 2024-12-10 03:17:00 | NOAA-21 | SÃO MATEUS | ESPÍRITO SANTO | Brasil | 3204906 | 32 | 33 | nan | nan | nan | Mata Atlântica | 5.4 |
| eec217c4-35be-3b1f-841c-6697332201d4 | -4.3959 | -47.7618 | 2024-12-10 03:20:00 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 52.1 |
| 2b0616e3-495e-34bd-a041-988c47f33ac8 | -12.5425 | -58.3561 | 2024-12-10 03:20:00 | GOES-16 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 91.3 |
| 8ecfbaf3-d80b-3f0b-8862-5353e8717f38 | -5.9183 | -48.0667 | 2024-12-10 03:20:00 | GOES-16 | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | 96.9 |
| 1cf5344c-7c1a-34c2-b30e-14c07ef2fc50 | -2.7758 | -44.9931 | 2024-12-10 03:20:00 | GOES-16 | SÃO BENTO | MARANHÃO | Brasil | 2110500 | 21 | 33 | nan | nan | nan | Amazônia | 64.8 |
| d05eea82-9789-35ec-86a5-9929dbb23d8f | -5.9185 | -48.0449 | 2024-12-10 03:20:00 | GOES-16 | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | 99.9 |
| 64afc656-477a-375e-870a-a540155d17da | -3.0043 | -52.8549 | 2024-12-10 03:20:00 | GOES-16 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 70.7 |
| ca1aac5b-13ef-3508-ab84-2212e084dc9d | -2.9859 | -52.8554 | 2024-12-10 03:20:00 | GOES-16 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 67.6 |
| ecedd6cf-2ee7-3453-9015-58744e98fcad | -12.5427 | -58.3362 | 2024-12-10 03:20:00 | GOES-16 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 68.9 |
| 96f96fb5-675b-3dbd-aad7-d30d282adf4d | -12.5615 | -58.3546 | 2024-12-10 03:20:00 | GOES-16 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 98.1 |
| 3b1bd26b-3864-350b-8866-b19192414fc8 | -2.8199 | -52.9816 | 2024-12-10 03:20:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 61.1 |
| 2cff2d68-8732-3bc0-a3f9-18b66722788c | -2.9859 | -52.8554 | 2024-12-10 03:30:00 | GOES-16 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 74.4 |
| 939ba631-b3be-39bc-a665-07e1e9511ba0 | -12.5427 | -58.3362 | 2024-12-10 03:30:00 | GOES-16 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 76.0 |
| 7248ab5a-66ad-3f74-8d27-e5cf28aaf6f0 | -2.7758 | -44.9931 | 2024-12-10 03:30:00 | GOES-16 | SÃO BENTO | MARANHÃO | Brasil | 2110500 | 21 | 33 | nan | nan | nan | Amazônia | 68.8 |
| 2e670357-12a6-394e-9671-400f3b022370 | -12.5425 | -58.3561 | 2024-12-10 03:30:00 | GOES-16 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 99.0 |
| 8de66c85-7f15-3039-a0ad-672119e51917 | -12.5615 | -58.3546 | 2024-12-10 03:30:00 | GOES-16 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 94.9 |
| a7a3a880-4afc-3650-9d20-2c1e4148b4c1 | -3.9747 | -45.62815 | 2024-12-10 03:34:00 | NPP-375D | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 9.8 |
| 25cf9688-d531-3324-943c-720ce8b6f73b | -2.84003 | -40.30467 | 2024-12-10 03:34:00 | NPP-375D | ACARAÚ | CEARÁ | Brasil | 2300200 | 23 | 33 | nan | nan | nan | Caatinga | 3.3 |
| 431fcb9e-0fdf-3171-9c89-a025535b8d78 | -3.34956 | -42.32989 | 2024-12-10 03:34:00 | NPP-375D | SÃO BERNARDO | MARANHÃO | Brasil | 2110609 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 7944072f-302f-3f70-93e2-c8d9577db266 | -3.9778 | -45.62829 | 2024-12-10 03:34:00 | NPP-375D | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 3.1 |
| a95127c1-1f69-3609-9690-8abcb40a2773 | -2.77981 | -45.00111 | 2024-12-10 03:34:00 | NPP-375D | SÃO BENTO | MARANHÃO | Brasil | 2110500 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a7fa3c3e-4a4d-3b3d-a233-f6aebed003b3 | -3.07214 | -40.04705 | 2024-12-10 03:34:00 | NPP-375D | ACARAÚ | CEARÁ | Brasil | 2300200 | 23 | 33 | nan | nan | nan | Caatinga | 7.5 |
| be72a2a5-295b-3da7-a01b-5d49f213fb48 | -2.77424 | -44.99437 | 2024-12-10 03:34:00 | NPP-375D | SÃO BENTO | MARANHÃO | Brasil | 2110500 | 21 | 33 | nan | nan | nan | Amazônia | 7.7 |
| f891a3d9-c494-316a-9bf5-3a38c1b61219 | -3.2365 | -42.43134 | 2024-12-10 03:34:00 | NPP-375D | SÃO BERNARDO | MARANHÃO | Brasil | 2110609 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 80fe3f0a-35db-3cbf-8f5b-8eda2f0db1bb | -3.23539 | -42.43399 | 2024-12-10 03:34:00 | NPP-375D | SÃO BERNARDO | MARANHÃO | Brasil | 2110609 | 21 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 89f1e02c-908f-3d22-9c30-4b836d5c13ff | -3.23724 | -42.42322 | 2024-12-10 03:34:00 | NPP-375D | SÃO BERNARDO | MARANHÃO | Brasil | 2110609 | 21 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 33746efd-6362-3e5b-b5f2-f983f1018794 | -3.97571 | -45.62226 | 2024-12-10 03:34:00 | NPP-375D | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 7.8 |
| 81ec97ae-50ae-319c-8264-cd5d9631ca3d | -2.77936 | -44.99579 | 2024-12-10 03:34:00 | NPP-375D | SÃO BENTO | MARANHÃO | Brasil | 2110500 | 21 | 33 | nan | nan | nan | Amazônia | 3.2 |
| da88718d-2236-346e-83a8-732b8b7afb00 | -3.23602 | -42.43036 | 2024-12-10 03:34:00 | NPP-375D | SÃO BERNARDO | MARANHÃO | Brasil | 2110609 | 21 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 6b46dc11-2c5a-3c09-b9ce-d7b3302ca848 | -2.83989 | -40.3025 | 2024-12-10 03:34:00 | NPP-375D | ACARAÚ | CEARÁ | Brasil | 2300200 | 23 | 33 | nan | nan | nan | Caatinga | 4.6 |
| 88ecf0f5-1423-3ab4-820d-d230f96365bf | -3.85241 | -40.45032 | 2024-12-10 03:34:00 | NPP-375D | CARIRÉ | CEARÁ | Brasil | 2303105 | 23 | 33 | nan | nan | nan | Caatinga | 2.3 |
| de62e16b-1da7-31a8-bc1f-72e7673779c6 | -3.23049 | -42.42956 | 2024-12-10 03:34:00 | NPP-375D | SÃO BERNARDO | MARANHÃO | Brasil | 2110609 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 204a96f9-b961-3634-9086-b5e21fe78980 | -3.35414 | -42.33072 | 2024-12-10 03:34:00 | NPP-375D | SÃO BERNARDO | MARANHÃO | Brasil | 2110609 | 21 | 33 | nan | nan | nan | Caatinga | 1.9 |
| dcfe7a4c-3088-37f2-9fa9-49561132a368 | -2.90105 | -40.44114 | 2024-12-10 03:34:00 | NPP-375D | JIJOCA DE JERICOACOARA | CEARÁ | Brasil | 2307254 | 23 | 33 | nan | nan | nan | Caatinga | 1.2 |
| f59a4980-5cbb-39d4-8114-bc698870e333 | -3.97884 | -45.62243 | 2024-12-10 03:34:00 | NPP-375D | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 03b760a2-ecca-38ce-b2ca-a67e3e061740 | -3.3481 | -42.33331 | 2024-12-10 03:34:00 | NPP-375D | SÃO BERNARDO | MARANHÃO | Brasil | 2110609 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 7410e7ff-0c72-3be6-9c7d-81432bedba66 | -3.37164 | -42.32652 | 2024-12-10 03:34:00 | NPP-375D | SÃO BERNARDO | MARANHÃO | Brasil | 2110609 | 21 | 33 | nan | nan | nan | Caatinga | 1.6 |
| afd5d9ef-adea-3d11-b21b-59f1daae9b4b | -2.77331 | -44.99988 | 2024-12-10 03:34:00 | NPP-375D | SÃO BENTO | MARANHÃO | Brasil | 2110500 | 21 | 33 | nan | nan | nan | Amazônia | 7.7 |
| 6b5925f2-f676-36be-90f1-8534af8cc9e8 | -3.97114 | -45.62721 | 2024-12-10 03:34:00 | NPP-375D | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 3.1 |
| a13860a9-ed4d-39d1-ac23-e4635b32443e | -3.23158 | -42.42691 | 2024-12-10 03:34:00 | NPP-375D | SÃO BERNARDO | MARANHÃO | Brasil | 2110609 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 7182e7dc-7161-3570-94bd-1f92f87225fd | -3.85886 | -40.4409 | 2024-12-10 03:34:00 | NPP-375D | CARIRÉ | CEARÁ | Brasil | 2303105 | 23 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 6f5a1528-b0c4-3774-a340-e02e8a7f4784 | -4.01793 | -38.25185 | 2024-12-10 03:34:00 | NPP-375D | AQUIRAZ | CEARÁ | Brasil | 2301000 | 23 | 33 | nan | nan | nan | Caatinga | 5.0 |
| 2e1da938-7241-3a50-bdf8-9581085a8ee1 | -3.34868 | -42.32983 | 2024-12-10 03:34:00 | NPP-375D | SÃO BERNARDO | MARANHÃO | Brasil | 2110609 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 1f1c8f88-c40e-3735-871e-18345ef982e4 | -3.23768 | -42.42418 | 2024-12-10 03:34:00 | NPP-375D | SÃO BERNARDO | MARANHÃO | Brasil | 2110609 | 21 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 7b079831-f524-3e50-b3d0-eb3cf39c7ee9 | -2.84086 | -40.2995 | 2024-12-10 03:34:00 | NPP-375D | ACARAÚ | CEARÁ | Brasil | 2300200 | 23 | 33 | nan | nan | nan | Caatinga | 2.7 |
| 58e0a96b-1629-302c-b6e4-d109d63bdfed | -3.23709 | -42.42774 | 2024-12-10 03:34:00 | NPP-375D | SÃO BERNARDO | MARANHÃO | Brasil | 2110609 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| e200c78a-bced-32a7-a065-ab760d06a5ba | -3.23663 | -42.42678 | 2024-12-10 03:34:00 | NPP-375D | SÃO BERNARDO | MARANHÃO | Brasil | 2110609 | 21 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 547e3abf-3717-3dba-b8f2-568342803191 | -3.22987 | -42.4332 | 2024-12-10 03:34:00 | NPP-375D | SÃO BERNARDO | MARANHÃO | Brasil | 2110609 | 21 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 80ddecf6-4201-3b49-96b2-caa66b5d0fc7 | -3.34896 | -42.33337 | 2024-12-10 03:34:00 | NPP-375D | SÃO BERNARDO | MARANHÃO | Brasil | 2110609 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 07eed4ce-af73-3ecd-af4a-1ab569a69d2b | -3.85802 | -40.44598 | 2024-12-10 03:34:00 | NPP-375D | CARIRÉ | CEARÁ | Brasil | 2303105 | 23 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 7ecded4c-2133-36fd-8ec1-5c00537ec128 | -3.37221 | -42.32301 | 2024-12-10 03:34:00 | NPP-375D | SÃO BERNARDO | MARANHÃO | Brasil | 2110609 | 21 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 988fd393-6e45-3f8d-b2cb-5e619f48cf1b | -3.07683 | -40.04782 | 2024-12-10 03:34:00 | NPP-375D | ACARAÚ | CEARÁ | Brasil | 2300200 | 23 | 33 | nan | nan | nan | Caatinga | 7.5 |
| d8bcf89c-9625-3190-b6f6-212fefbc2cd0 | -3.23112 | -42.42595 | 2024-12-10 03:34:00 | NPP-375D | SÃO BERNARDO | MARANHÃO | Brasil | 2110609 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| ec419a17-1781-3252-8c20-6cd9e5de6f41 | -4.61967 | -37.69608 | 2024-12-10 03:34:00 | NPP-375D | ARACATI | CEARÁ | Brasil | 2301109 | 23 | 33 | nan | nan | nan | Caatinga | 1.0 |
| d24f7708-339a-382c-8c44-374f282c0827 | -3.23098 | -42.43053 | 2024-12-10 03:34:00 | NPP-375D | SÃO BERNARDO | MARANHÃO | Brasil | 2110609 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |


[Clique aqui para ver as próximas entradas](README10.md)
