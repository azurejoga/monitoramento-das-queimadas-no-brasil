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

## Dados Diários - Página 82

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| aaa8aa61-f5cf-370b-b6e3-a30b832a71c9 | -6.2676 | -53.3768 | 2026-08-26 13:50:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 73.7 |
| ac73e928-7a4f-3ec1-a730-8e4fe4fe849d | -9.7249 | -49.3296 | 2026-08-26 13:50:00 | GOES-19 | DIVINÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1707108 | 17 | 33 | nan | nan | nan | Cerrado | 126.7 |
| 04b37c0b-c737-3d6e-acbd-85b8e05198e0 | -10.7598 | -54.0179 | 2026-08-26 13:50:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 109.4 |
| 2b4759f6-f864-38f4-a5ef-005b3acf7e97 | -14.3558 | -51.7636 | 2026-08-26 13:50:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 118.9 |
| e314339c-6d04-3374-b052-d1487aeab765 | -8.1482 | -47.5218 | 2026-08-26 13:50:00 | GOES-19 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 160.2 |
| 0921cf93-5a49-3db6-997f-ef9e5245672f | -7.1264 | -43.1948 | 2026-08-26 13:50:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 138.8 |
| c8dd1ec8-71f4-321f-a2eb-4f654e7e7223 | -6.1741 | -53.5037 | 2026-08-26 13:50:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 66.2 |
| 928b16a6-1c63-30c9-96e7-b419c2e9dab8 | -7.1452 | -43.193 | 2026-08-26 13:50:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 91.3 |
| c022f72b-b27b-34d6-99e9-ed8c6f7cb796 | -8.8187 | -49.6093 | 2026-08-26 13:50:00 | GOES-19 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 159.1 |
| 42f53ccf-9bde-3aee-bc8e-472c01246d76 | -13.3402 | -48.2079 | 2026-08-26 13:50:00 | GOES-19 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 77.9 |
| 3039cdf8-a377-382f-bfae-984d7e53638d | -8.5177 | -55.3039 | 2026-08-26 13:50:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 63.2 |
| 18e98493-9f1b-30ec-a789-a1d6951fda1e | -8.5777 | -54.8373 | 2026-08-26 13:50:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 66.6 |
| eff53949-4c69-39a3-b516-d0d4baa43e3e | -7.1121 | -42.7963 | 2026-08-26 13:50:00 | GOES-19 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 195.1 |
| 89c46ee9-ff51-3e3f-9881-8f3071b06384 | -6.7663 | -45.2324 | 2026-08-26 13:50:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 78.5 |
| 1e1d9315-8f9a-3751-965b-8adae26d9e68 | -8.7769 | -49.9763 | 2026-08-26 13:50:00 | GOES-19 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 81.8 |
| d00e4523-a868-3846-8822-0c851c86f144 | -12.6836 | -48.4116 | 2026-08-26 13:50:00 | GOES-19 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 99.5 |
| cb7e3f7a-fea8-3acc-85c6-dcf452b57436 | -15.5543 | -47.106 | 2026-08-26 13:50:00 | GOES-19 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 100.7 |
| 52cc12e1-b90e-3a2d-bd93-bb1158e6319e | -6.0031 | -44.7475 | 2026-08-26 13:50:00 | GOES-19 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 70.6 |
| 617033ca-b284-3e62-88b3-0c643a2c243b | -4.8004 | -43.1476 | 2026-08-26 13:50:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 114.2 |
| 998b17be-1845-3c5d-ba5b-c28b4f274fb8 | -7.6461 | -47.1258 | 2026-08-26 13:50:00 | GOES-19 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 553.1 |
| 7affe4a7-2743-3e1f-8b7b-c1839dda328e | -4.8002 | -43.1709 | 2026-08-26 13:50:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 177.1 |
| 38ab412d-87a9-32e8-8062-c2a0612eff37 | -6.7661 | -45.2551 | 2026-08-26 13:50:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 86.4 |
| c2ce2d3a-8011-36ed-8389-597b1277f936 | -12.1229 | -43.3738 | 2026-08-26 13:50:00 | GOES-19 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 130.4 |
| 6a009afa-6b1f-3cf2-bbf4-248fdff2365f | -3.79 | -59.284 | 2026-08-26 13:50:00 | GOES-19 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 80.7 |
| bd7a0251-a7c4-3c1a-9349-58c884d350a4 | -7.1266 | -43.1714 | 2026-08-26 13:50:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 91.4 |
| 39f16258-b05f-396f-bd4d-b1a66b70900b | -9.5936 | -49.278 | 2026-08-26 13:50:00 | GOES-19 | ABREULÂNDIA | TOCANTINS | Brasil | 1700251 | 17 | 33 | nan | nan | nan | Cerrado | 108.5 |
| ed07ac46-34ef-3198-9464-f6e13078ed5a | -7.1312 | -42.7708 | 2026-08-26 13:50:00 | GOES-19 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 138.3 |
| beb1369e-80c6-3b90-8626-a68a264cd9f9 | -9.7246 | -49.3512 | 2026-08-26 13:50:00 | GOES-19 | DIVINÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1707108 | 17 | 33 | nan | nan | nan | Cerrado | 90.7 |
| 88983b3f-3f50-3c09-ab8f-9efc8f7c10e2 | -9.1896 | -50.0032 | 2026-08-26 13:50:00 | GOES-19 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 68.0 |
| 0a57d55b-06cb-3ce8-a20c-614c56a6a086 | -7.385 | -55.1523 | 2026-08-26 13:50:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 106.7 |
| 0eaef261-ad4f-335e-92db-b8f9d7d9557b | -14.3751 | -51.7611 | 2026-08-26 13:50:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 210.3 |
| 4c30a5b9-3ff0-33e9-9d78-13e22cdb9dbb | -12.1422 | -43.3707 | 2026-08-26 13:50:00 | GOES-19 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 147.8 |
| 8fb0ec77-613b-3275-bc72-98e969a27410 | -6.3322 | -54.7473 | 2026-08-26 13:50:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 64.9 |
| a4eb996a-e9bc-359a-b58f-72fc389f9e6a | -13.2643 | -51.4992 | 2026-08-26 13:50:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 86.8 |
| 30b02108-f3a4-3801-8de8-541acf694672 | -8.7584 | -49.9566 | 2026-08-26 13:50:00 | GOES-19 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 89.3 |
| 36de5dc9-004a-3235-bb45-411e593976e9 | -14.3562 | -51.7422 | 2026-08-26 13:50:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 161.5 |
| fd34575c-8b66-3176-9151-2a490abfe6eb | -15.3446 | -53.8752 | 2026-08-26 13:50:00 | GOES-19 | POXORÉU | MATO GROSSO | Brasil | 5107008 | 51 | 33 | nan | nan | nan | Cerrado | 192.5 |
| fbf8c13e-e7b3-3de9-afd9-1c42f983c8f3 | -11.8161 | -47.6869 | 2026-08-26 13:50:00 | GOES-19 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 78.5 |
| 8844eccb-fcd1-30cb-b493-ec58cf4004ab | -10.7596 | -54.0384 | 2026-08-26 13:50:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 156.3 |
| a2860206-a5d7-30d6-b06e-7cb5e3ae5195 | -8.9418 | -45.748 | 2026-08-26 13:50:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 209.9 |
| 583fc470-b021-37d1-bc3f-356e9af65811 | -7.3849 | -55.1723 | 2026-08-26 13:50:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 64.3 |
| a88fd533-4fd3-3fc7-b729-bb28f5156c63 | -7.1309 | -42.7945 | 2026-08-26 13:50:00 | GOES-19 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 198.2 |
| 02622e50-946a-3b53-882a-302f4091a864 | -9.6776 | -55.082 | 2026-08-26 13:50:00 | GOES-19 | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 76.7 |
| 9b4c3b91-e241-3c96-bfb6-1aaaef72759f | -12.1704 | -50.5861 | 2026-08-26 13:50:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 105.1 |
| 61db9e75-6d3b-3325-aa04-51b008a30f14 | -7.0236 | -45.7303 | 2026-08-26 13:50:00 | GOES-19 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 220.0 |
| 8991bffb-5e12-3046-a377-1cdc700860f0 | -11.0037 | -51.1635 | 2026-08-26 13:50:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 152.5 |
| 266cdd71-1022-3521-89cb-12ab6a3adc3d | -8.5363 | -55.3027 | 2026-08-26 13:50:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 90.0 |
| 09f143d7-db4b-3625-ae88-599a61410e50 | -6.2676 | -53.3768 | 2026-08-26 14:00:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 76.7 |
| 9f2a89f5-7161-307c-9401-6157a4799a02 | -6.6409 | -58.5181 | 2026-08-26 14:00:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 61.2 |
| 6b212953-e2af-3516-b4b1-56743f2fc7ce | -13.6617 | -51.8323 | 2026-08-26 14:00:00 | GOES-19 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 107.9 |
| 0af10ad4-8e3b-353a-b266-ec88b6ef76b3 | -13.286 | -51.3473 | 2026-08-26 14:00:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 68.8 |
| c1ad305f-6861-338c-8be8-fc47f874c8f0 | -14.3945 | -51.7585 | 2026-08-26 14:00:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 198.6 |
| 998e0abb-c0c1-3ae0-b0be-0689584a4b65 | -7.1121 | -42.7963 | 2026-08-26 14:00:00 | GOES-19 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 649.2 |
| 6d7d4bb1-0b98-378f-bcb3-99a420a6cbf5 | -9.6022 | -55.128 | 2026-08-26 14:00:00 | GOES-19 | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 62.4 |
| c34d9662-6286-3a05-9be6-5393461a15cf | -8.9421 | -45.7253 | 2026-08-26 14:00:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 171.5 |
| d8bf4736-4d2d-3c29-bf3c-12b4ecc1a38d | -8.1484 | -47.4998 | 2026-08-26 14:00:00 | GOES-19 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 91.0 |
| eb215451-f398-3f10-bad3-5d527faac14c | -3.79 | -59.284 | 2026-08-26 14:00:00 | GOES-19 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 64.4 |
| 9d045c46-d81b-344d-b30e-47861b1c1e0b | -10.7784 | -54.0368 | 2026-08-26 14:00:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 107.5 |
| a737d9ca-a51a-3cb6-aa58-0da7cf0a56dd | -12.1417 | -43.3945 | 2026-08-26 14:00:00 | GOES-19 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 108.8 |
| 98cd4e25-fe9d-37fe-b88c-26cd0b8d7bd3 | -9.6776 | -55.082 | 2026-08-26 14:00:00 | GOES-19 | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 135.0 |
| 7bc9c608-4be9-33cd-87d7-c5795d1ffb88 | -9.6588 | -55.0834 | 2026-08-26 14:00:00 | GOES-19 | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 70.8 |
| 67630504-1ab5-3008-9484-9e4e6ab6646a | -8.5363 | -55.3027 | 2026-08-26 14:00:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 179.4 |
| d6bea6d8-5d9f-3397-9d6a-21b3f966bc40 | -7.385 | -55.1523 | 2026-08-26 14:00:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 79.1 |
| a71a4bd2-5d72-37a3-babc-48403540f122 | -9.7249 | -49.3296 | 2026-08-26 14:00:00 | GOES-19 | DIVINÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1707108 | 17 | 33 | nan | nan | nan | Cerrado | 133.0 |
| 65531c55-6c8a-31fd-98c4-18187a9df5d3 | -11.8161 | -47.6869 | 2026-08-26 14:00:00 | GOES-19 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 85.7 |
| 3092d275-61bc-3522-99c2-69caa9642d7d | -7.1312 | -42.7708 | 2026-08-26 14:00:00 | GOES-19 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 135.7 |
| ae17da3f-867c-3d94-a429-461493bd07d6 | -8.9418 | -45.748 | 2026-08-26 14:00:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 639.1 |
| 4cb8f213-b4aa-3f67-a7de-65a51c9f97db | -13.3038 | -51.4304 | 2026-08-26 14:00:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 83.9 |
| ed181459-512f-3e67-a71c-c0b557f31ca3 | -13.6817 | -51.7872 | 2026-08-26 14:00:00 | GOES-19 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 134.3 |
| dc0f85f5-7648-3117-9625-09a0bbe61654 | -10.7596 | -54.0384 | 2026-08-26 14:00:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 156.5 |
| f3c81789-96b0-32e1-bdcd-46c4b3d83fd9 | -14.3751 | -51.7611 | 2026-08-26 14:00:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 99.2 |
| f57f6f6c-5095-30dc-9ef1-7b17f4849d11 | -12.0354 | -47.1442 | 2026-08-26 14:00:00 | GOES-19 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 95.1 |
| caf6f089-820a-3020-b5a4-b558b53cb046 | -9.5936 | -49.278 | 2026-08-26 14:00:00 | GOES-19 | ABREULÂNDIA | TOCANTINS | Brasil | 1700251 | 17 | 33 | nan | nan | nan | Cerrado | 80.6 |
| 2dd3fa1a-15af-3787-947b-01c5fc3d114f | -12.6452 | -48.4168 | 2026-08-26 14:00:00 | GOES-19 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 75.1 |
| 450473e2-5620-3279-afd8-b9f082c59d52 | -12.1704 | -50.5861 | 2026-08-26 14:00:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 111.4 |
| 0bc8662d-d033-3f4f-9a54-07a0d7dabc5a | -8.7584 | -49.9566 | 2026-08-26 14:00:00 | GOES-19 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 89.6 |
| f0d2cd4e-c462-39e3-8a9c-1e198ec269b0 | -8.5962 | -54.8563 | 2026-08-26 14:00:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 84.4 |
| 5afecf02-55b2-3684-a51e-4dc4421521db | -7.6461 | -47.1258 | 2026-08-26 14:00:00 | GOES-19 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 331.1 |
| e191ff67-eecf-3787-b6a9-3807c09e71f5 | -3.7717 | -59.2844 | 2026-08-26 14:00:00 | GOES-19 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 63.5 |
| ab883353-30ca-332d-a16c-d3393b62a8d9 | -4.8002 | -43.1709 | 2026-08-26 14:00:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 189.3 |
| 0bb78209-0b02-30a3-a1af-a5a2f4f49746 | -8.8187 | -49.6093 | 2026-08-26 14:00:00 | GOES-19 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 137.3 |
| e9edf81d-2ab9-3e2f-ad81-29ffb2922d9c | -12.1422 | -43.3707 | 2026-08-26 14:00:00 | GOES-19 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 157.0 |
| 3ae00def-5b2f-3b49-b6b1-dca2b648ab21 | -3.2178 | -61.2362 | 2026-08-26 14:00:00 | GOES-19 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 70.0 |
| 9fae007a-8d35-3bd0-a63a-89b21af6f0f8 | -9.1896 | -50.0032 | 2026-08-26 14:00:00 | GOES-19 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 72.3 |
| 1a4b9bd5-6e06-3b02-ad5e-3b28f0ff151c | -9.7246 | -49.3512 | 2026-08-26 14:00:00 | GOES-19 | DIVINÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1707108 | 17 | 33 | nan | nan | nan | Cerrado | 119.8 |
| d519910c-ecbe-3194-aaa4-c1c51a0c8756 | -8.1857 | -54.9435 | 2026-08-26 14:00:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 55.1 |
| 2a78986c-9df9-33bd-a501-c7f0531a9b4b | -12.6836 | -48.4116 | 2026-08-26 14:00:00 | GOES-19 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 98.1 |
| 5ded02b1-963b-3eb3-936e-88d51edcacd8 | -10.7598 | -54.0179 | 2026-08-26 14:00:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 119.5 |
| 86b35885-3d7f-3344-8569-3343ea9e5088 | -8.5361 | -55.3228 | 2026-08-26 14:00:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 83.5 |
| ee969884-01ab-32af-8755-0924996d6254 | -13.6614 | -51.8535 | 2026-08-26 14:00:00 | GOES-19 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 100.4 |
| 9bb98601-cf81-358c-b879-4ee64c4ba242 | -6.4114 | -60.0498 | 2026-08-26 14:00:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 68.2 |
| e1220258-c363-3aaf-9b16-d210d935ba1f | -6.6226 | -58.4995 | 2026-08-26 14:00:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 54.6 |
| 1f9d2820-c7f6-3955-a075-1ae2cc333e94 | -9.6024 | -55.1078 | 2026-08-26 14:00:00 | GOES-19 | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 158.3 |
| e8590881-e640-3610-82c0-d4f7e9f2a40f | -8.5177 | -55.3039 | 2026-08-26 14:00:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 56.8 |
| ef970226-9862-3aa9-8960-32589b71d308 | -7.1309 | -42.7945 | 2026-08-26 14:00:00 | GOES-19 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 386.5 |
| cc17bf27-ba91-3f2c-9e32-66aac38c390c | -13.2664 | -51.3711 | 2026-08-26 14:00:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 101.7 |
| 0f936924-e493-33bf-889c-1e06101ac488 | -6.8358 | -59.9379 | 2026-08-26 14:00:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 116.4 |
| 0e5567a4-46ec-3824-a988-c5b941f2faf1 | -11.411 | -44.541 | 2026-08-26 14:00:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 73.7 |
| b528196c-66e0-37c8-874f-570d35562e0b | -6.3322 | -54.7473 | 2026-08-26 14:00:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 59.7 |
| 46bef6eb-57a7-34a4-89bb-d57351f9a6e8 | -8.6344 | -54.7528 | 2026-08-26 14:00:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 73.9 |


[Clique aqui para ver as próximas entradas](README83.md)
