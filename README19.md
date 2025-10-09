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
| fb6e6c31-251c-3661-ac47-c5d4d1dfacb0 | -7.80479 | -44.20512 | 2025-10-09 03:57:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 66b34ec6-df45-3acf-98b2-4391f473a905 | -5.31589 | -45.38047 | 2025-10-09 03:57:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| cdd13e50-6167-33b6-a33b-04cf4cda1b47 | -8.53154 | -46.21677 | 2025-10-09 03:57:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 36.7 |
| 5ac6b420-362d-33c9-b33f-2192b5b535c2 | -6.36386 | -46.30329 | 2025-10-09 03:57:00 | NPP-375D | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| ff3c4a55-c3c0-32dd-bcc1-91825f3255b0 | -4.68478 | -45.84398 | 2025-10-09 03:57:00 | NPP-375D | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 0.5 |
| ed6af2d0-e272-3d53-bbc1-9160bcc333b5 | -4.81508 | -47.34305 | 2025-10-09 03:57:00 | NPP-375D | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 79650da4-cfe8-3c09-b771-b470b36eeee7 | -9.61479 | -40.32841 | 2025-10-09 03:57:00 | NPP-375D | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 3.7 |
| 5de702f6-23a8-3460-845c-c505a3e77944 | -8.53989 | -46.20475 | 2025-10-09 03:57:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 33.5 |
| 55f15688-4c88-3b5f-bc57-70affb567d9b | -9.76667 | -47.70171 | 2025-10-09 03:57:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| e658975f-807f-36b9-a8c4-af54e74e58f0 | -7.78583 | -44.19064 | 2025-10-09 03:57:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 261b5320-a5b3-3281-8514-1689b648f9a9 | -4.3746 | -46.75824 | 2025-10-09 03:57:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 738e66b6-87cb-3caa-9218-5d6ed270b032 | -5.00921 | -37.80309 | 2025-10-09 03:57:00 | NPP-375D | QUIXERÉ | CEARÁ | Brasil | 2311504 | 23 | 33 | nan | nan | nan | Caatinga | 0.8 |
| a1831041-b2dd-3994-aafc-b52d2353d88b | -7.63912 | -39.90601 | 2025-10-09 03:57:00 | NPP-375D | BODOCÓ | PERNAMBUCO | Brasil | 2602001 | 26 | 33 | nan | nan | nan | Caatinga | 0.5 |
| 4301bcce-e7a1-388d-8e0a-301e68d1cd2e | -8.17577 | -43.32439 | 2025-10-09 03:57:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 18dee6b9-7ff9-369e-a64a-c34ee3606783 | -3.11101 | -47.79605 | 2025-10-09 03:57:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| e7304864-b562-3d3f-a753-a4b5034777f1 | -4.51571 | -37.92761 | 2025-10-09 03:57:00 | NPP-375D | FORTIM | CEARÁ | Brasil | 2304459 | 23 | 33 | nan | nan | nan | Caatinga | 3.7 |
| 57b168ff-a472-3540-a9a0-3965d0392391 | -7.52496 | -42.73022 | 2025-10-09 03:57:00 | NPP-375D | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 8ed1a1b7-f413-318c-a233-c14937f0fcb0 | -7.48735 | -43.10523 | 2025-10-09 03:57:00 | NPP-375D | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| e8734d04-a0ad-3a55-b8b9-21391af5a287 | -5.13564 | -37.55618 | 2025-10-09 03:57:00 | NPP-375D | BARAÚNA | RIO GRANDE DO NORTE | Brasil | 2401453 | 24 | 33 | nan | nan | nan | Caatinga | 3.4 |
| ba0f7dd8-38e1-3166-8eab-995b004ed99e | -3.64568 | -39.37333 | 2025-10-09 03:57:00 | NPP-375D | TURURU | CEARÁ | Brasil | 2313559 | 23 | 33 | nan | nan | nan | Caatinga | 0.9 |
| cc66c113-8fef-3c30-b710-76f93d19e00e | -5.39845 | -40.98654 | 2025-10-09 03:57:00 | NPP-375D | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 4.9 |
| 04727f49-3113-39c1-8d33-833d75e24a3e | -7.66758 | -42.58873 | 2025-10-09 03:57:00 | NPP-375D | RIBEIRA DO PIAUÍ | PIAUÍ | Brasil | 2208874 | 22 | 33 | nan | nan | nan | Caatinga | 3.4 |
| 40ac4b35-e516-306e-b3c1-431bf8b74308 | -6.79439 | -50.49005 | 2025-10-09 03:57:00 | NPP-375D | ÁGUA AZUL DO NORTE | PARÁ | Brasil | 1500347 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 626ba94f-0273-39ed-b0f7-7b1ff3fafc92 | -4.50857 | -38.82468 | 2025-10-09 03:57:00 | NPP-375D | ARACOIABA | CEARÁ | Brasil | 2301208 | 23 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 1ca7cb6c-ca3f-34ee-89ad-921c517108e2 | -8.31004 | -46.22788 | 2025-10-09 03:57:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 83e53d5c-4983-37a9-9ac2-f3ecbd060ed4 | -7.68346 | -42.39753 | 2025-10-09 03:57:00 | NPP-375D | SÃO MIGUEL DO FIDALGO | PIAUÍ | Brasil | 2210391 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 84aee4f7-c3bf-38e7-941d-dc95d478136e | -4.26114 | -48.56844 | 2025-10-09 03:57:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| d59dbe58-cd62-32a4-9da1-00d1dc3e8171 | -6.74386 | -42.83212 | 2025-10-09 03:57:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 4.0 |
| 0183bb93-849a-3ea8-a2b0-6ca9e75a3a20 | -7.63784 | -47.69088 | 2025-10-09 03:57:00 | NPP-375D | FILADÉLFIA | TOCANTINS | Brasil | 1707702 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| ecb0cc2f-361d-320d-b592-a3bbb34be8f4 | -5.11967 | -41.1894 | 2025-10-09 03:57:00 | NPP-375D | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| b973bc0f-c872-32fb-b2d1-871c558beca3 | -8.10433 | -39.46786 | 2025-10-09 03:57:00 | NPP-375D | PARNAMIRIM | PERNAMBUCO | Brasil | 2610400 | 26 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 4e4be4a9-1093-3d49-a45b-363fc17351ad | -8.63122 | -45.14426 | 2025-10-09 03:57:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 71566358-bb83-30a4-b6f1-98f39a9c7a57 | -7.63188 | -43.05737 | 2025-10-09 03:57:00 | NPP-375D | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| c686551d-db30-3005-aadb-7fcd0238207c | -7.17788 | -39.31987 | 2025-10-09 03:57:00 | NPP-375D | JUAZEIRO DO NORTE | CEARÁ | Brasil | 2307304 | 23 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 77a517f3-4061-3532-b731-963ff796390f | -10.09799 | -40.776 | 2025-10-09 03:57:00 | NPP-375D | CAMPO FORMOSO | BAHIA | Brasil | 2906006 | 29 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 9315b16f-0d56-31d2-a60d-2ccb698c78ef | -7.71088 | -42.37782 | 2025-10-09 03:57:00 | NPP-375D | SÃO MIGUEL DO FIDALGO | PIAUÍ | Brasil | 2210391 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 40df2d06-5784-3dbd-a644-2b6e91bd0ea7 | -7.55169 | -44.29785 | 2025-10-09 03:57:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 1cd6e363-6526-3c38-aa62-a781bd884b41 | -7.48178 | -43.11441 | 2025-10-09 03:57:00 | NPP-375D | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 7.8 |
| 58d87ac5-1200-3672-9c5c-25ecb2cddc33 | -3.74352 | -39.96669 | 2025-10-09 03:57:00 | NPP-375D | IRAUÇUBA | CEARÁ | Brasil | 2306108 | 23 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 5f2a96e2-452d-39ac-a90d-3488411eb840 | -8.53138 | -46.22485 | 2025-10-09 03:57:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 6.8 |
| eaaa243d-b2d9-3c1a-8ae2-70751f58ed44 | -7.79245 | -42.42125 | 2025-10-09 03:57:00 | NPP-375D | SOCORRO DO PIAUÍ | PIAUÍ | Brasil | 2210904 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 18d9fc5b-b8fd-3430-bee8-9fc52bbdee13 | -3.36536 | -43.37791 | 2025-10-09 03:57:00 | NPP-375D | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| a1185ad5-0b4a-3740-bc63-231f0cee62b5 | -7.76755 | -42.40568 | 2025-10-09 03:57:00 | NPP-375D | SOCORRO DO PIAUÍ | PIAUÍ | Brasil | 2210904 | 22 | 33 | nan | nan | nan | Caatinga | 3.1 |
| d8752669-9bca-39da-b7b0-5bfcb01d05e0 | -8.12992 | -47.25224 | 2025-10-09 03:57:00 | NPP-375D | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| b2f97d56-e9da-30c0-8d14-d22b317be2a1 | -8.19892 | -43.35379 | 2025-10-09 03:57:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 5.9 |
| cbacf3d3-4dd3-3737-ad07-a82a27991fee | -8.19056 | -43.33202 | 2025-10-09 03:57:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 18.1 |
| fd86156d-9708-3c53-b77d-5df8f8090fee | -7.2731 | -41.98466 | 2025-10-09 03:57:00 | NPP-375D | WALL FERRAZ | PIAUÍ | Brasil | 2211704 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 4e440538-5e1c-3023-8499-5d18dce61a2e | -6.69246 | -46.30426 | 2025-10-09 03:57:00 | NPP-375D | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 35.0 |
| 5a7eada9-3493-3f37-b728-1c6b4861e4c9 | -6.45754 | -44.57885 | 2025-10-09 03:57:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 4.0 |
| c801e1ba-b9fd-38ff-9bd1-642ff613460e | -3.10518 | -47.80215 | 2025-10-09 03:57:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| f6c0b643-5119-3091-b6e5-101c56bd627d | -8.53137 | -46.19822 | 2025-10-09 03:57:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 6.5 |
| d1bb77c3-b6c5-35f0-b109-1b1640a336f5 | -7.79221 | -42.41892 | 2025-10-09 03:57:00 | NPP-375D | SOCORRO DO PIAUÍ | PIAUÍ | Brasil | 2210904 | 22 | 33 | nan | nan | nan | Caatinga | 4.2 |
| ab4b5adf-492f-37ed-8ca0-5c7c3c7282aa | -8.5285 | -46.21396 | 2025-10-09 03:57:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 43.4 |
| 3573ca2c-f66d-35e6-8efb-531b777b0817 | -7.81616 | -46.71003 | 2025-10-09 03:57:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| aa2c92b2-7423-3ad8-bbb7-36d1329db633 | -5.64413 | -45.04133 | 2025-10-09 03:57:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| ab42ddd9-7037-3aac-8aa2-ca4161ad922f | -5.63383 | -35.457 | 2025-10-09 03:57:00 | NPP-375D | CEARÁ-MIRIM | RIO GRANDE DO NORTE | Brasil | 2402600 | 24 | 33 | nan | nan | nan | Caatinga | 5.8 |
| 8c24fff8-e4db-3717-87ee-bdec34ff24d1 | -3.13611 | -49.03938 | 2025-10-09 03:57:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| d03a0aef-f9d0-324d-a164-9a692242f0d4 | -5.44591 | -44.82589 | 2025-10-09 03:57:00 | NPP-375D | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 10.9 |
| e49d2999-d407-3fe3-a145-2f70d6b43dd4 | -4.36994 | -46.754 | 2025-10-09 03:57:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 18ef241c-c207-35fd-a66a-b5ce462e1343 | -8.41031 | -41.45375 | 2025-10-09 03:57:00 | NPP-375D | QUEIMADA NOVA | PIAUÍ | Brasil | 2208650 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| e86e9f47-14f2-372c-8e7f-c68138b78614 | -4.45679 | -43.22624 | 2025-10-09 03:57:00 | NPP-375D | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 10.2 |
| 70511db9-e54a-341b-8c75-f6c6c8dcb4b8 | -9.75992 | -47.7099 | 2025-10-09 03:57:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 661c30b0-e53f-3960-83cc-0b79ac451139 | -3.90649 | -44.34297 | 2025-10-09 03:57:00 | NPP-375D | SÃO MATEUS DO MARANHÃO | MARANHÃO | Brasil | 2111508 | 21 | 33 | nan | nan | nan | Cerrado | 4.2 |
| bcc88d6d-2f51-3767-b543-70fd5920f0ff | -7.81426 | -46.71415 | 2025-10-09 03:57:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 61b0674f-69e5-3e3f-ae5e-1aa6bc9f88e9 | -9.77012 | -47.71177 | 2025-10-09 03:57:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 40a4aa90-4709-39b5-bd0d-d8961d681f5f | -7.50359 | -42.74109 | 2025-10-09 03:57:00 | NPP-375D | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 8eea459b-e949-3519-953c-60864879ee68 | -6.00471 | -39.8209 | 2025-10-09 03:57:00 | NPP-375D | MOMBAÇA | CEARÁ | Brasil | 2308500 | 23 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 98af5c9b-df62-3f11-acb4-c4cc330fd747 | -7.8295 | -44.14427 | 2025-10-09 03:57:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 8e0a693a-cfaf-3d0b-83f6-125e6aa19ef9 | -7.42987 | -44.56363 | 2025-10-09 03:57:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 9adf5ca2-4a60-35e6-a791-88409717ec1d | -7.79866 | -42.61311 | 2025-10-09 03:57:00 | NPP-375D | RIBEIRA DO PIAUÍ | PIAUÍ | Brasil | 2208874 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| f5f7ad41-7b2d-3e16-b355-c7f9e75c87e0 | -9.88545 | -40.47144 | 2025-10-09 03:57:00 | NPP-375D | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 0.5 |
| 5a0a6bc9-6143-3f70-b1e4-4a2a17cb30bc | -6.50638 | -44.1455 | 2025-10-09 03:57:00 | NPP-375D | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| f204971e-4466-38c0-b1c5-3a3fe37a04ae | -6.68339 | -42.18776 | 2025-10-09 03:57:00 | NPP-375D | TANQUE DO PIAUÍ | PIAUÍ | Brasil | 2210979 | 22 | 33 | nan | nan | nan | Caatinga | 3.9 |
| cbb498f3-c1f2-3e07-ba0c-654f28589e2c | -3.26094 | -50.12076 | 2025-10-09 03:57:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 27141bd0-10a2-324c-88bd-08c10df74905 | -8.5354 | -46.22252 | 2025-10-09 03:57:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 28.1 |
| f81764e3-8932-3dcb-b464-cf61591a6965 | -4.75439 | -45.77374 | 2025-10-09 03:57:00 | NPP-375D | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 2f2c06e1-36a7-31c6-afd8-97fae6a4b606 | -7.25767 | -42.97048 | 2025-10-09 03:57:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 651b9a84-4792-313b-a435-5c336ad6cdd7 | -7.80933 | -46.71328 | 2025-10-09 03:57:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| ecd0bd83-8f04-32af-83d7-06440808146c | -8.53518 | -46.19581 | 2025-10-09 03:57:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| f4b7a58b-ae42-3e10-b243-e720860be3d7 | -5.39976 | -40.97839 | 2025-10-09 03:57:00 | NPP-375D | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 5.0 |
| 45dec496-8118-3520-bbe2-5fc3f4764b73 | -4.36312 | -45.5729 | 2025-10-09 03:57:00 | NPP-375D | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f85c9e59-0f84-31c0-b508-7caf53f94cc8 | -4.45267 | -43.22556 | 2025-10-09 03:57:00 | NPP-375D | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| b043b90a-af69-36f4-9a61-80b90c74ccbf | -4.97914 | -45.31704 | 2025-10-09 03:57:00 | NPP-375D | LAGOA GRANDE DO MARANHÃO | MARANHÃO | Brasil | 2105963 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 61064642-1c95-37ed-8200-ab3f3ee7ba84 | -7.02824 | -42.78834 | 2025-10-09 03:57:00 | NPP-375D | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 00ee8474-91ce-32f0-8060-78b2916827de | -8.53628 | -46.2174 | 2025-10-09 03:57:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 28.1 |
| 591493f2-6c30-3537-9fcb-76695180fee3 | -9.03658 | -40.64226 | 2025-10-09 03:57:00 | NPP-375D | PETROLINA | PERNAMBUCO | Brasil | 2611101 | 26 | 33 | nan | nan | nan | Caatinga | 1.6 |
| c00b401b-a035-3b75-a240-ca7880593492 | -8.55248 | -47.72282 | 2025-10-09 03:57:00 | NPP-375D | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 85d4a176-6c93-35f9-944a-8e85366a95a4 | -8.54579 | -46.21854 | 2025-10-09 03:57:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 4.6 |
| c63e440e-b5bf-3d32-8222-5a965488b8fb | -9.09593 | -47.95706 | 2025-10-09 03:57:00 | NPP-375D | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 47d5bc0f-2358-3aa9-bc03-7fc0d50be870 | -5.44243 | -44.82401 | 2025-10-09 03:57:00 | NPP-375D | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| e81131a1-96d6-396d-8e90-4d1b31b00825 | -6.45826 | -44.57465 | 2025-10-09 03:57:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 5.0 |
| af72c491-96f6-326e-be80-85872d36e0f6 | -4.6116 | -43.14715 | 2025-10-09 03:57:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| aaf34d59-ad03-3f35-8928-5a0de67a1c36 | -7.30158 | -41.97179 | 2025-10-09 03:57:00 | NPP-375D | COLÔNIA DO PIAUÍ | PIAUÍ | Brasil | 2202778 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| a0d66a43-5a8c-3ab8-96ab-c9dcc63a4e4e | -7.99462 | -44.46309 | 2025-10-09 03:57:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 902d13dd-d690-351e-9e79-1594123bb406 | -7.02744 | -42.79315 | 2025-10-09 03:57:00 | NPP-375D | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 2eac9aa6-1280-382f-a83b-be33d64457df | -5.4884 | -42.89521 | 2025-10-09 03:57:00 | NPP-375D | NAZÁRIA | PIAUÍ | Brasil | 2206720 | 22 | 33 | nan | nan | nan | Caatinga | 3.6 |
| 7b45c7fe-a282-38c4-a1b1-95ab81f050a3 | -4.88884 | -42.252 | 2025-10-09 03:57:00 | NPP-375D | CAMPO MAIOR | PIAUÍ | Brasil | 2202208 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| fbd5bd3f-fa61-3bed-bb94-ceb3e412bfb0 | -7.01236 | -42.74144 | 2025-10-09 03:57:00 | NPP-375D | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 3.5 |
| 8e2c2df3-1327-3978-b121-bc0795c18ab0 | -7.50668 | -42.72229 | 2025-10-09 03:57:00 | NPP-375D | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | 9.2 |
| e7821887-0219-34d3-a6c1-bb46b552db4b | -5.67932 | -42.78388 | 2025-10-09 03:57:00 | NPP-375D | MIGUEL LEÃO | PIAUÍ | Brasil | 2206308 | 22 | 33 | nan | nan | nan | Caatinga | 5.0 |


[Clique aqui para ver as próximas entradas](README20.md)
