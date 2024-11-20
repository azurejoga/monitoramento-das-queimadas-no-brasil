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
| 3af8ce0c-9b6e-3f20-afee-4b1594316f09 | -2.6212 | -51.7997 | 2024-11-20 00:40:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 91.2 |
| 7ece12bb-8a5b-34e8-8c4d-451eccc4bb06 | -3.8021 | -47.7887 | 2024-11-20 00:40:00 | GOES-16 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 94.0 |
| 361f04fe-67ac-315a-b5f0-ce216769ab05 | -3.2014 | -54.3243 | 2024-11-20 00:40:00 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 100.5 |
| 12d014cf-c49c-3dff-b46a-207d02271906 | -2.8309 | -45.1493 | 2024-11-20 00:40:00 | GOES-16 | PALMEIRÂNDIA | MARANHÃO | Brasil | 2107605 | 21 | 33 | nan | nan | nan | Amazônia | 86.9 |
| 2fff7874-0108-3fda-8a31-5a7dc6d892a5 | -4.4404 | -46.5975 | 2024-11-20 00:40:00 | GOES-16 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 60.9 |
| 8330b462-e880-3e74-871b-4aa4c6b24d52 | -11.1106 | -54.6408 | 2024-11-20 00:40:00 | GOES-16 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 54.5 |
| ac6d21ed-3ef3-3f09-bd42-4d09996e3df5 | -2.6397 | -51.7992 | 2024-11-20 00:40:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 55.4 |
| 3689fc72-8c9d-33ab-8e1b-d012d6db9f6e | -11.1109 | -54.6204 | 2024-11-20 00:40:00 | GOES-16 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 66.7 |
| 4f4564d8-e87c-3fca-8b15-0ca9a598b72a | -0.947 | -51.724 | 2024-11-20 00:40:00 | GOES-16 | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 57.6 |
| d2850941-d96e-3678-9f9e-0e9d65eea2cc | -4.459 | -46.5966 | 2024-11-20 00:40:00 | GOES-16 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 68.8 |
| cb934e9a-3ae6-3a37-89bc-ee54a5ddfc40 | -4.1682 | -45.5195 | 2024-11-20 00:50:00 | GOES-16 | ALTAMIRA DO MARANHÃO | MARANHÃO | Brasil | 2100402 | 21 | 33 | nan | nan | nan | Amazônia | 82.8 |
| b42f46b5-64ef-3264-a842-8d5ba5d853a6 | -3.1477 | -49.1251 | 2024-11-20 00:50:00 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 48.8 |
| 4b368ecc-2c56-3d35-97fc-22c23e6651f7 | -2.9116 | -53.0606 | 2024-11-20 00:50:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 98.2 |
| 50aa8282-12ff-3592-b0fa-51dc7f022305 | -2.9969 | -45.436 | 2024-11-20 00:50:00 | GOES-16 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 193.9 |
| 04233de5-13f0-3253-93e9-6088a1a259d5 | -4.4405 | -46.5754 | 2024-11-20 00:50:00 | GOES-16 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 63.6 |
| 485bde1d-0b14-3852-8f60-354d2d49202d | -2.6212 | -51.7997 | 2024-11-20 00:50:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 80.2 |
| 6bd8319e-823a-3815-a549-fe7da3634013 | -2.7501 | -51.8171 | 2024-11-20 00:50:00 | GOES-16 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 42.6 |
| 66e401a1-821d-31dd-a457-df5ffd4c5804 | -14.3216 | -51.5118 | 2024-11-20 00:50:00 | GOES-16 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 79.9 |
| 758ee41d-9775-32e9-b68e-0499b645fac8 | -3.802 | -47.8104 | 2024-11-20 00:50:00 | GOES-16 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 78.0 |
| b1fcc33d-8f34-3c64-a98f-0542748c81f4 | -14.3219 | -51.4904 | 2024-11-20 00:50:00 | GOES-16 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 73.1 |
| f07f6795-b915-3e9a-bf46-67abd78ad973 | -2.6028 | -51.8001 | 2024-11-20 00:50:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 44.2 |
| 58a8fc63-f6d4-3356-bbc7-a0b36ca53a9f | -1.2017 | -53.6769 | 2024-11-20 00:50:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 85.1 |
| a10c0eee-cdbf-3609-b8b0-afafe6a4b91b | -2.8124 | -45.1274 | 2024-11-20 00:50:00 | GOES-16 | PALMEIRÂNDIA | MARANHÃO | Brasil | 2107605 | 21 | 33 | nan | nan | nan | Amazônia | 146.3 |
| 09da36ac-cbcf-35e9-9a38-254fe03750d7 | -3.1292 | -49.1257 | 2024-11-20 00:50:00 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 55.6 |
| 29954336-9740-388c-bf85-257aec37a26b | 1.5284 | -55.9045 | 2024-11-20 00:50:00 | GOES-16 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 57.4 |
| 0bc06381-c5a0-34e6-905c-4b6c3b8ae429 | -3.2586 | -45.1332 | 2024-11-20 00:50:00 | GOES-16 | PENALVA | MARANHÃO | Brasil | 2108306 | 21 | 33 | nan | nan | nan | Amazônia | 124.2 |
| 3fb30a85-ffdb-30ab-9a37-8b3f3646a1e7 | -7.395 | -42.7682 | 2024-11-20 00:50:00 | GOES-16 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 51.3 |
| 73aa1eba-86a0-32a2-a088-4b1d47559b84 | -3.4752 | -50.3196 | 2024-11-20 00:50:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 44.4 |
| be010744-b16a-38b0-925c-7074e79a8023 | -3.2014 | -54.3243 | 2024-11-20 00:50:00 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 100.9 |
| 4a6b0278-ef4e-390e-b515-62c4375cd366 | -11.1109 | -54.6204 | 2024-11-20 00:50:00 | GOES-16 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 71.2 |
| ee5922ee-534c-3592-9a7f-4181de786b72 | -3.2585 | -45.1558 | 2024-11-20 00:50:00 | GOES-16 | PENALVA | MARANHÃO | Brasil | 2108306 | 21 | 33 | nan | nan | nan | Amazônia | 81.0 |
| a60d7804-c743-3f15-bedc-b6837ee625a0 | -4.3774 | -47.7627 | 2024-11-20 00:50:00 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 73.4 |
| 11281c56-14d0-3ee9-9389-2b105c0a6be3 | -17.1362 | -57.5041 | 2024-11-20 00:50:00 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 51.9 |
| bc7df010-b42b-3e10-a79c-122fd283152b | -2.831 | -45.1267 | 2024-11-20 00:50:00 | GOES-16 | SÃO BENTO | MARANHÃO | Brasil | 2110500 | 21 | 33 | nan | nan | nan | Amazônia | 218.9 |
| 74839d86-959c-3cf7-ac1a-bdf57282f0aa | -2.6212 | -51.8203 | 2024-11-20 00:50:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 44.6 |
| 28371ca9-2c1a-3190-b79f-e0794016276e | -3.0155 | -45.4353 | 2024-11-20 00:50:00 | GOES-16 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 100.7 |
| c8cc6443-0587-36f0-8ffc-c28f80ead311 | -3.4936 | -50.319 | 2024-11-20 00:50:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 45.3 |
| 2191eec5-8bfa-343d-a9e1-9af99356bedb | -2.8309 | -45.1493 | 2024-11-20 00:50:00 | GOES-16 | PALMEIRÂNDIA | MARANHÃO | Brasil | 2107605 | 21 | 33 | nan | nan | nan | Amazônia | 113.5 |
| 593e7236-1a2a-33a8-9402-3375b469cc17 | -3.011 | -51.0028 | 2024-11-20 00:50:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 83.2 |
| 458d00bc-f06b-3ca8-a65b-00c781b3a9bc | -4.5429 | -48.0151 | 2024-11-20 00:50:00 | GOES-16 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 48.9 |
| 62fee866-f009-31c2-a247-308c4332a879 | -4.4592 | -46.5745 | 2024-11-20 00:50:00 | GOES-16 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 80.6 |
| 7f9755f3-a7af-3074-a638-484f4a56e1e6 | -4.1594 | -43.9739 | 2024-11-20 00:50:00 | GOES-16 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 56.5 |
| ab1d3ff8-ed6c-3383-af88-cc8362bdeca6 | -3.8021 | -47.7887 | 2024-11-20 00:50:00 | GOES-16 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 56.5 |
| 8afc3036-8321-385f-b609-9b54d69df0da | -2.9968 | -45.4584 | 2024-11-20 00:50:00 | GOES-16 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 87.7 |
| 4bd7fc8f-23fb-3538-9c6c-a95924388ab5 | -4.3772 | -47.7844 | 2024-11-20 00:50:00 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 53.2 |
| 2fb79131-878a-32c5-8f4c-de87271c81aa | -4.459 | -46.5966 | 2024-11-20 00:50:00 | GOES-16 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 54.6 |
| 0c1c7133-d28d-35e8-85a1-d42f808d9409 | -3.8205 | -47.8096 | 2024-11-20 00:50:00 | GOES-16 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 52.1 |
| b255d714-296c-3e10-948d-f82219ff4c30 | -4.2528 | -53.6684 | 2024-11-20 00:50:00 | GOES-16 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 50.0 |
| 23cdebd7-fa1c-3a5b-ad0e-fbf857457aa7 | -2.8124 | -45.1499 | 2024-11-20 00:50:00 | GOES-16 | PALMEIRÂNDIA | MARANHÃO | Brasil | 2107605 | 21 | 33 | nan | nan | nan | Amazônia | 74.9 |
| c4f8996a-ea41-397c-a2c1-1b1d4a25ccdc | -4.4404 | -46.5975 | 2024-11-20 00:50:00 | GOES-16 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 47.5 |
| 32d473e1-57f8-3964-8ada-a8aa86eef1c4 | -4.3959 | -47.7618 | 2024-11-20 00:50:00 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 67.7 |
| 1163f436-acd7-30e9-aa96-ae227a790160 | -3.0109 | -51.0236 | 2024-11-20 00:50:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 72.5 |
| 7de19a5b-acd1-3497-82bd-aaaea628e7e8 | -4.5614 | -48.0141 | 2024-11-20 00:50:00 | GOES-16 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 70.0 |
| 55a85117-5969-32ce-80df-6c63b0db8258 | -2.75 | -51.8377 | 2024-11-20 00:50:00 | GOES-16 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 47.1 |
| 15ecd5e1-4fb4-3e14-9ef6-0d912568076e | -11.1106 | -54.6408 | 2024-11-20 00:50:00 | GOES-16 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 62.1 |
| b23369af-91aa-3500-af02-df419da11fe3 | -4.1683 | -45.4971 | 2024-11-20 00:50:00 | GOES-16 | ALTAMIRA DO MARANHÃO | MARANHÃO | Brasil | 2100402 | 21 | 33 | nan | nan | nan | Amazônia | 70.9 |
| bc29b12b-4583-34ba-af96-33ea31323c64 | -2.831 | -45.1267 | 2024-11-20 01:00:00 | GOES-16 | SÃO BENTO | MARANHÃO | Brasil | 2110500 | 21 | 33 | nan | nan | nan | Amazônia | 240.4 |
| 4dff3db0-4341-3685-92ee-468e5aa64eba | -4.4404 | -46.5975 | 2024-11-20 01:00:00 | GOES-16 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 57.1 |
| a95f42d4-c794-3689-96fb-07db350f61f0 | -2.75 | -51.8377 | 2024-11-20 01:00:00 | GOES-16 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 45.9 |
| 2182b376-c314-31e6-afb8-1480f78d14c6 | -2.9116 | -53.0606 | 2024-11-20 01:00:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 97.4 |
| 22f4ad70-eee8-3547-bf47-2611d07f2a61 | -3.1292 | -49.1257 | 2024-11-20 01:00:00 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 41.6 |
| 8cb9d9f7-563e-3a5c-babf-2f416e22c026 | -4.5614 | -48.0141 | 2024-11-20 01:00:00 | GOES-16 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 74.2 |
| 9c65e648-32e0-3935-94e1-2d152620f1aa | -2.6397 | -51.7992 | 2024-11-20 01:00:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 50.2 |
| 45bcf56f-af8d-34ed-9741-964805273582 | 1.5284 | -55.9045 | 2024-11-20 01:00:00 | GOES-16 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 54.4 |
| ad82af9b-f87a-3d48-bcf6-5f65b9f1720b | -11.1106 | -54.6408 | 2024-11-20 01:00:00 | GOES-16 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 74.7 |
| 761164bc-d703-336a-aaff-b9598877569d | -2.6212 | -51.7997 | 2024-11-20 01:00:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 87.3 |
| f2392262-1a4e-3ac2-8527-676739b08ae6 | -3.2585 | -45.1558 | 2024-11-20 01:00:00 | GOES-16 | PENALVA | MARANHÃO | Brasil | 2108306 | 21 | 33 | nan | nan | nan | Amazônia | 70.8 |
| a5d49871-d966-3ef2-81dc-a57cf9d6f816 | -3.2586 | -45.1332 | 2024-11-20 01:00:00 | GOES-16 | PENALVA | MARANHÃO | Brasil | 2108306 | 21 | 33 | nan | nan | nan | Amazônia | 125.1 |
| 822432fd-4804-3de7-84b5-e08065d2d2e1 | -3.0155 | -45.4353 | 2024-11-20 01:00:00 | GOES-16 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 132.4 |
| 53d3b5b1-3069-3b3c-9807-b13ededb25ec | -3.4936 | -50.319 | 2024-11-20 01:00:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 43.7 |
| e4829c68-834c-3fc4-a55f-734bd9d6be99 | -14.3216 | -51.5118 | 2024-11-20 01:00:00 | GOES-16 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 90.1 |
| 2c8416f9-eff4-3be2-8c19-b158cc5a16f8 | -4.5429 | -48.0151 | 2024-11-20 01:00:00 | GOES-16 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 45.6 |
| 154b0b3d-6b9f-3a1e-baae-37cf896543ec | -3.2014 | -54.3243 | 2024-11-20 01:00:00 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 95.4 |
| 1222cf02-6f75-31a6-8a03-2dc4717103ca | -2.7217 | -49.3508 | 2024-11-20 01:00:00 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 74.9 |
| 6c8180b3-6f93-3e35-a2f1-76132cde5cde | -11.1109 | -54.6204 | 2024-11-20 01:00:00 | GOES-16 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 104.1 |
| dfdcf18a-fefc-3260-ad9e-c515d2b1e064 | -2.2996 | -48.4863 | 2024-11-20 01:00:00 | GOES-16 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 66.6 |
| cfbffecb-5afa-3f73-acf6-7a6243f1614b | -1.3138 | -52.3973 | 2024-11-20 01:00:00 | GOES-16 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 65.6 |
| 6c44b801-358a-362b-9ff1-13262a11a28b | -4.3774 | -47.7627 | 2024-11-20 01:00:00 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 69.9 |
| 305b5d16-116f-3948-87d8-02c88ec628ab | -3.2772 | -45.1324 | 2024-11-20 01:00:00 | GOES-16 | PENALVA | MARANHÃO | Brasil | 2108306 | 21 | 33 | nan | nan | nan | Amazônia | 73.0 |
| 649b916e-2087-31c6-8d12-758262b827ec | -4.3959 | -47.7618 | 2024-11-20 01:00:00 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 83.9 |
| 92205083-3210-33a4-aa4d-54a2dfb2dd44 | -14.3219 | -51.4904 | 2024-11-20 01:00:00 | GOES-16 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 89.5 |
| 9411dcab-b7e4-375c-8a18-699029c36044 | -4.4592 | -46.5745 | 2024-11-20 01:00:00 | GOES-16 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 82.7 |
| cdcf387e-d577-3326-83a7-29869cef23e4 | -2.9969 | -45.436 | 2024-11-20 01:00:00 | GOES-16 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 165.6 |
| 4ac09187-bd08-369b-9e35-31f93f2d7c39 | -0.9654 | -51.7238 | 2024-11-20 01:00:00 | GOES-16 | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 57.5 |
| 5b9fd286-8c26-3894-9b60-6840f94b4787 | -2.8309 | -45.1493 | 2024-11-20 01:00:00 | GOES-16 | PALMEIRÂNDIA | MARANHÃO | Brasil | 2107605 | 21 | 33 | nan | nan | nan | Amazônia | 118.1 |
| 10a7899d-5dc5-37ee-9692-a29d5bd58227 | -3.8206 | -47.7879 | 2024-11-20 01:00:00 | GOES-16 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 59.3 |
| 0d6edf4e-8ab9-328c-a45c-ebe6a4584029 | -3.802 | -47.8104 | 2024-11-20 01:00:00 | GOES-16 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 97.7 |
| f97ec996-e908-31ee-8fdc-2573b6d98e92 | -3.8021 | -47.7887 | 2024-11-20 01:00:00 | GOES-16 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 81.1 |
| a8b59860-7795-3195-ba44-20b5beeaab8b | -9.6598 | -36.361 | 2024-11-20 01:00:00 | GOES-16 | ANADIA | ALAGOAS | Brasil | 2700201 | 27 | 33 | nan | nan | nan | Mata Atlântica | 62.8 |
| 4baed2a5-455e-3543-a343-990cca610328 | -4.459 | -46.5966 | 2024-11-20 01:00:00 | GOES-16 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 68.8 |
| ca0daf3a-cdcf-3b6d-ac60-b2a6a208dd21 | -3.8205 | -47.8096 | 2024-11-20 01:00:00 | GOES-16 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 75.5 |
| 26d9292a-071c-32d9-a5b7-4dfa276974c7 | -11.092 | -54.6221 | 2024-11-20 01:00:00 | GOES-16 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 62.2 |
| 0d11d0e2-ac48-35cb-b018-fa379e6e1b3f | -3.1477 | -49.1251 | 2024-11-20 01:00:00 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 48.5 |
| 7fd170a8-6db3-3f90-8b1b-2108a42999d3 | -2.6212 | -51.8203 | 2024-11-20 01:00:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 40.5 |
| f2f2a04e-aeff-3b01-ba60-fe377f7b3ba7 | -2.9968 | -45.4584 | 2024-11-20 01:00:00 | GOES-16 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 86.4 |
| e91ce3fb-1b4e-351c-9261-94489b031f2c | -1.2017 | -53.6769 | 2024-11-20 01:00:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 105.2 |
| 61eae024-0ad3-3eaa-bad1-ef2af1eca602 | -4.1594 | -43.9739 | 2024-11-20 01:00:00 | GOES-16 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 47.8 |
| 98dee8d9-db72-3f07-bb12-7314f079548d | -1.3321 | -52.3971 | 2024-11-20 01:00:00 | GOES-16 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 65.6 |
| a41857ac-ab70-38b6-a44a-5c3720c2db4f | -3.0109 | -51.0236 | 2024-11-20 01:00:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 78.7 |
| 8c799b55-0830-36b0-ac49-0e9845fff34b | -3.011 | -51.0028 | 2024-11-20 01:00:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 72.5 |


[Clique aqui para ver as próximas entradas](README10.md)
