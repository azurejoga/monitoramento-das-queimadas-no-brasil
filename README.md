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

## Dados Diários - Página 1

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| b7f99520-3c01-3f1b-9b63-45e4293aa5a4 | -2.6987 | -45.6705 | 2024-11-23 00:00:00 | GOES-16 | NOVA OLINDA DO MARANHÃO | MARANHÃO | Brasil | 2107357 | 21 | 33 | nan | nan | nan | Amazônia | 63.5 |
| bcebed3d-cfa1-3268-8cda-776ee979c327 | -3.4663 | -48.2349 | 2024-11-23 00:00:00 | GOES-16 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 73.0 |
| 017a7368-4247-34e0-82d6-18673da76042 | -4.5898 | -46.5012 | 2024-11-23 00:00:00 | GOES-16 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 111.7 |
| 935bc1db-8ac1-315e-bd70-109c8a5995ef | -1.7359 | -52.7385 | 2024-11-23 00:00:00 | GOES-16 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 73.6 |
| bfbb2878-7cfa-34ab-953f-9db026ba0f4b | -1.7359 | -52.7181 | 2024-11-23 00:00:00 | GOES-16 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 130.8 |
| 3ffa708b-23f5-34f0-8fc4-26cbaf53d8a3 | -3.1138 | -53.096 | 2024-11-23 00:00:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 90.4 |
| 368d81a9-d4b3-3339-a6b9-6ae8a53ca733 | -1.7175 | -52.7184 | 2024-11-23 00:00:00 | GOES-16 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 74.9 |
| 8a80152f-b524-3744-8792-45e60567a07b | -4.4196 | -44.1204 | 2024-11-23 00:00:00 | GOES-16 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 69.4 |
| 03464e3e-5c6f-3a08-ae6b-4cd792dd8fa6 | -4.5402 | -42.93 | 2024-11-23 00:00:00 | GOES-16 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 95.0 |
| 94eabab6-b100-3b5d-a5c3-d49535fd8c04 | -4.5403 | -42.9066 | 2024-11-23 00:00:00 | GOES-16 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 137.4 |
| 82969474-3c47-35ad-8c87-e4a8e9f31639 | -3.5159 | -53.8132 | 2024-11-23 00:00:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 80.8 |
| e23bab99-1198-373e-8fcc-90a4109f5126 | -3.2386 | -54.223 | 2024-11-23 00:00:00 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 135.4 |
| 2b0628de-f5e3-3180-85ce-5d786719a920 | -3.1831 | -54.3247 | 2024-11-23 00:00:00 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 89.7 |
| 8923038a-da54-37bb-b8e3-9e636e374da3 | -2.8124 | -45.1499 | 2024-11-23 00:00:00 | GOES-16 | PALMEIRÂNDIA | MARANHÃO | Brasil | 2107605 | 21 | 33 | nan | nan | nan | Amazônia | 81.8 |
| bd7cc6dd-53f4-3bfb-92a9-629140b3379f | -3.1138 | -53.1163 | 2024-11-23 00:00:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 145.3 |
| 82a47f9d-c97c-34d6-8e8d-99a8ab8989d2 | -2.8308 | -45.1719 | 2024-11-23 00:00:00 | GOES-16 | SÃO BENTO | MARANHÃO | Brasil | 2110500 | 21 | 33 | nan | nan | nan | Amazônia | 122.6 |
| 55aa249f-da40-3fb1-9d37-08a784eba553 | -3.6276 | -45.7021 | 2024-11-23 00:00:00 | GOES-16 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 94.8 |
| 62e4e893-485b-3095-a076-937db7b9e57b | -2.8309 | -45.1493 | 2024-11-23 00:00:00 | GOES-16 | PALMEIRÂNDIA | MARANHÃO | Brasil | 2107605 | 21 | 33 | nan | nan | nan | Amazônia | 111.6 |
| bb177509-397c-32a1-9fc3-8d9af366c01f | -4.6086 | -46.478 | 2024-11-23 00:00:00 | GOES-16 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 87.8 |
| 31bfc793-a701-3fdd-8617-b051278e29e1 | -4.1133 | -42.4614 | 2024-11-23 00:00:00 | GOES-16 | BARRAS | PIAUÍ | Brasil | 2201200 | 22 | 33 | nan | nan | nan | Caatinga | 70.0 |
| eb486117-fc2c-3b3b-82e6-bed9154525bf | -9.9294 | -36.3411 | 2024-11-23 00:00:00 | GOES-16 | TEOTÔNIO VILELA | ALAGOAS | Brasil | 2709152 | 27 | 33 | nan | nan | nan | Mata Atlântica | 174.1 |
| 0d3d9658-f284-3985-b8c5-432ddd774b69 | -2.6802 | -45.6711 | 2024-11-23 00:00:00 | GOES-16 | NOVA OLINDA DO MARANHÃO | MARANHÃO | Brasil | 2107357 | 21 | 33 | nan | nan | nan | Amazônia | 59.4 |
| 9aca98c6-50d2-3125-9756-3c8813f7de4b | -2.7149 | -46.2713 | 2024-11-23 00:00:00 | GOES-16 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 77.5 |
| 6985e29f-ee98-38dd-b8c3-74fdf609bfe5 | -3.2768 | -53.8199 | 2024-11-23 00:00:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 91.8 |
| 67e76fb7-be4e-31c7-8d9b-d23b2a821109 | -3.2569 | -54.2226 | 2024-11-23 00:00:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 159.5 |
| b3aae9a1-ba5a-341f-8760-1d26646d3a77 | -4.5216 | -42.9078 | 2024-11-23 00:00:00 | GOES-16 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 107.0 |
| 6113af41-cc5c-3ee0-8235-3851ef976b80 | -4.5614 | -48.0141 | 2024-11-23 00:00:00 | GOES-16 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 83.8 |
| 3fea50e5-1c0a-36de-b844-ad3e47452b8d | -2.961 | -45.1672 | 2024-11-23 00:00:00 | GOES-16 | VIANA | MARANHÃO | Brasil | 2112803 | 21 | 33 | nan | nan | nan | Amazônia | 89.2 |
| e3fc856c-28a3-3806-af87-c46bbf4f7206 | -3.4662 | -48.2565 | 2024-11-23 00:00:00 | GOES-16 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 90.8 |
| 4ab19a6b-818e-3819-b5b4-6fc57f085037 | -3.2544 | -50.1168 | 2024-11-23 00:00:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 73.0 |
| 098c48f9-deb2-3091-a419-076af6a76c74 | -4.706 | -45.8493 | 2024-11-23 00:00:00 | GOES-16 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 84.8 |
| 9c89d839-c4dc-36da-baad-7e2fa65e621b | -4.67 | -45.6722 | 2024-11-23 00:00:00 | GOES-16 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 101.8 |
| df99b51f-9f6d-3276-8957-6404f436620a | -1.8106 | -52.1652 | 2024-11-23 00:00:00 | GOES-16 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 64.2 |
| ed591cd5-8887-371f-a583-0285c9a5c135 | -1.1287 | -53.3951 | 2024-11-23 00:00:00 | GOES-16 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 80.7 |
| 59715c33-a78e-3769-b64c-6f70c1b42fec | -9.9289 | -36.368 | 2024-11-23 00:00:00 | GOES-16 | TEOTÔNIO VILELA | ALAGOAS | Brasil | 2709152 | 27 | 33 | nan | nan | nan | Mata Atlântica | 52.5 |
| 80cda7f6-dd5f-3822-ab10-d2855891f540 | -6.5054 | -47.0414 | 2024-11-23 00:00:00 | GOES-16 | SÃO JOÃO DO PARAÍSO | MARANHÃO | Brasil | 2111052 | 21 | 33 | nan | nan | nan | Cerrado | 103.6 |
| a2b57433-306a-3ea2-b546-b744772ece93 | -3.7354 | -49.9948 | 2024-11-23 00:00:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 62.9 |
| b0f88c24-e5ef-3273-a75d-054f804fab8c | -9.9487 | -36.3377 | 2024-11-23 00:00:00 | GOES-16 | TEOTÔNIO VILELA | ALAGOAS | Brasil | 2709152 | 27 | 33 | nan | nan | nan | Mata Atlântica | 80.3 |
| 37e3e83c-3d5a-31cc-98db-fdf9210beb80 | -2.9609 | -45.1898 | 2024-11-23 00:00:00 | GOES-16 | VIANA | MARANHÃO | Brasil | 2112803 | 21 | 33 | nan | nan | nan | Amazônia | 55.8 |
| 763ae748-5f9a-3f4d-b59f-7d051f396bf0 | -3.7538 | -50.0152 | 2024-11-23 00:00:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 189.2 |
| cc1afefe-58e4-3cc6-9823-fe90bf3fa7ab | -6.4867 | -47.0428 | 2024-11-23 00:00:00 | GOES-16 | SÃO JOÃO DO PARAÍSO | MARANHÃO | Brasil | 2111052 | 21 | 33 | nan | nan | nan | Cerrado | 75.7 |
| e38f62c2-3d25-3da3-8594-f2832331d778 | -3.7539 | -49.9941 | 2024-11-23 00:00:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 140.4 |
| 124a91cb-af8f-3aa6-aec6-58a16c3cb08d | -3.058 | -53.28 | 2024-11-23 00:00:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 80.9 |
| a21fc024-5c0b-32af-8e22-1c4640c0d03d | -4.5215 | -42.9312 | 2024-11-23 00:00:00 | GOES-16 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 75.4 |
| db0ab144-0520-32a7-88f7-265ffdbae10b | -3.2385 | -54.2431 | 2024-11-23 00:00:00 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 147.9 |
| b24eb294-d905-3eb9-a56d-af369500338a | -3.7353 | -50.0158 | 2024-11-23 00:00:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 75.7 |
| 09d62cad-012c-3c12-b078-a7583bd48d05 | -3.7086 | -51.7888 | 2024-11-23 00:00:00 | GOES-16 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 78.6 |
| 19e40a30-aeca-3fb7-b9b8-b9bce5ad4ffc | -4.1131 | -42.4851 | 2024-11-23 00:00:00 | GOES-16 | BARRAS | PIAUÍ | Brasil | 2201200 | 22 | 33 | nan | nan | nan | Caatinga | 62.3 |
| 019f5c5e-b8d4-3c07-bb11-a1ca863db27c | -3.2569 | -54.2426 | 2024-11-23 00:00:00 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 162.5 |
| 3830aee1-d864-369e-b68e-1fa17f17e901 | -2.8123 | -45.1725 | 2024-11-23 00:00:00 | GOES-16 | SÃO BENTO | MARANHÃO | Brasil | 2110500 | 21 | 33 | nan | nan | nan | Amazônia | 92.5 |
| 1659ceed-dad9-38c2-ae75-55b0f4f97f2b | -2.6963 | -46.2719 | 2024-11-23 00:00:00 | GOES-16 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 98.7 |
| 47fbefe2-6a26-35a9-893e-50af3ede96dd | -4.6085 | -46.5002 | 2024-11-23 00:00:00 | GOES-16 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 196.1 |
| 02439303-70de-39a3-a30e-07ea434234c9 | -3.4954 | -49.9191 | 2024-11-23 00:00:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 56.0 |
| ec53f7b7-74c5-3300-82be-af4ff4f95bb6 | -2.82 | -45.14 | 2024-11-23 00:00:00 | MSG-03 | PALMEIRÂNDIA | MARANHÃO | Brasil | 2107605 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 7c9f2f26-f70b-3cf9-9a04-82c701bc50c4 | -2.8228 | -45.1595 | 2024-11-23 00:00:00 | METOP-C | PALMEIRÂNDIA | MARANHÃO | Brasil | 2107605 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 13ea3445-7da3-3e63-bdab-53745003a6b3 | -4.6956 | -44.407501 | 2024-11-23 00:00:00 | METOP-C | CAPINZAL DO NORTE | MARANHÃO | Brasil | 2102754 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| e8eaa200-5ae7-3b8c-9a29-009fe5f08bbd | -10.477 | -37.152302 | 2024-11-23 00:00:00 | METOP-C | NOSSA SENHORA DAS DORES | SERGIPE | Brasil | 2804607 | 28 | 33 | nan | nan | nan | Mata Atlântica | nan |
| e8f12684-a839-30fd-b262-3436ed1d79be | -10.4722 | -37.131199 | 2024-11-23 00:00:00 | METOP-C | CAPELA | SERGIPE | Brasil | 2801306 | 28 | 33 | nan | nan | nan | Mata Atlântica | nan |
| e2632aa7-e410-32f7-be19-9379cdf5b035 | -4.0973 | -42.468498 | 2024-11-23 00:00:00 | METOP-C | BARRAS | PIAUÍ | Brasil | 2201200 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 129ab013-d2de-30c2-80ed-f79e674adf7a | -9.7977 | -36.1362 | 2024-11-23 00:00:00 | METOP-C | SÃO MIGUEL DOS CAMPOS | ALAGOAS | Brasil | 2708600 | 27 | 33 | nan | nan | nan | Mata Atlântica | nan |
| cddce505-2b13-32e7-9775-fb1734a4cf81 | -4.1108 | -42.4827 | 2024-11-23 00:00:00 | METOP-C | BARRAS | PIAUÍ | Brasil | 2201200 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 3174c477-8fa6-302a-82df-d2b8a853961f | -4.3834 | -38.967098 | 2024-11-23 00:00:00 | METOP-C | CAPISTRANO | CEARÁ | Brasil | 2302909 | 23 | 33 | nan | nan | nan | Caatinga | nan |
| bc88e602-11b1-38be-9cf4-86e17d7546dc | -3.6649 | -47.139702 | 2024-11-23 00:00:00 | METOP-C | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 80fa8328-7f81-36fc-b132-c1432ad59aff | -4.9713 | -44.958401 | 2024-11-23 00:00:00 | METOP-C | ESPERANTINÓPOLIS | MARANHÃO | Brasil | 2104008 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| f99fc583-60e2-31d5-8099-cc20a1e9cf4c | -4.09 | -47.031898 | 2024-11-23 00:00:00 | METOP-C | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 5680a954-d186-36af-a6b3-2c265ba4dd88 | -5.1037 | -43.151798 | 2024-11-23 00:00:00 | METOP-C | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 99bede20-3692-3927-a561-67729f23f89c | -4.7082 | -45.852901 | 2024-11-23 00:00:00 | METOP-C | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 906b1a69-f5cb-3ef2-91b1-c8ea0796cb5f | -2.6915 | -46.261101 | 2024-11-23 00:00:00 | METOP-C | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 11e0b74f-57e2-3e01-aec9-3d275d3f5cf8 | -7.0105 | -39.2257 | 2024-11-23 00:00:00 | METOP-C | CARIRIAÇU | CEARÁ | Brasil | 2303204 | 23 | 33 | nan | nan | nan | Caatinga | nan |
| 96401966-a94d-3bfa-8fab-c4bc2493462d | -10.5034 | -36.684601 | 2024-11-23 00:00:00 | METOP-C | PACATUBA | SERGIPE | Brasil | 2804904 | 28 | 33 | nan | nan | nan | Mata Atlântica | nan |
| d0c38177-4b47-319f-9468-30f92d9631b0 | -4.282 | -44.8069 | 2024-11-23 00:00:00 | METOP-C | BACABAL | MARANHÃO | Brasil | 2101202 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| be4a61a0-264f-3fa0-8bd8-0d623a07894f | -2.7614 | -45.933998 | 2024-11-23 00:00:00 | METOP-C | NOVA OLINDA DO MARANHÃO | MARANHÃO | Brasil | 2107357 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 0745f618-5f2d-3143-8d94-2f9e811a88e7 | -2.9601 | -45.1768 | 2024-11-23 00:00:00 | METOP-C | VIANA | MARANHÃO | Brasil | 2112803 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 8c6a10cf-6ee4-3699-b4f7-e75562af4897 | -2.4114 | -46.063599 | 2024-11-23 00:00:00 | METOP-C | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 1d591019-d5b6-3c65-ab9c-e3957a93511a | -4.0377 | -46.195801 | 2024-11-23 00:00:00 | METOP-C | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 1d60370f-bf1f-3d9b-b149-ba539a317d66 | -2.7073 | -46.2855 | 2024-11-23 00:00:00 | METOP-C | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| f8511b6c-b3a5-3088-93fc-45a2f56f3b8e | -4.2845 | -44.8181 | 2024-11-23 00:00:00 | METOP-C | BACABAL | MARANHÃO | Brasil | 2101202 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 0afa7d9f-8a99-399b-90c0-ce2d8eac6ed7 | -4.5043 | -44.700298 | 2024-11-23 00:00:00 | METOP-C | TRIZIDELA DO VALE | MARANHÃO | Brasil | 2112233 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 34073d53-7138-3878-bbc3-785a7c5cfa84 | -7.4848 | -41.753399 | 2024-11-23 00:00:00 | METOP-C | FLORESTA DO PIAUÍ | PIAUÍ | Brasil | 2203859 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 62c75bcc-e885-3942-b664-ea151bf2b2e3 | -4.3655 | -47.819901 | 2024-11-23 00:00:00 | METOP-C | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 18122550-58f6-33aa-bb76-58eb331a2625 | -10.4738 | -37.138199 | 2024-11-23 00:00:00 | METOP-C | SIRIRI | SERGIPE | Brasil | 2807204 | 28 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 74f39613-3de2-3669-bf78-c5eafd12e04a | -4.4037 | -44.1101 | 2024-11-23 00:00:00 | METOP-C | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 8da1fbfe-863f-38c9-9ffa-24a229e1bc66 | -4.2573 | -44.695801 | 2024-11-23 00:00:00 | METOP-C | BACABAL | MARANHÃO | Brasil | 2101202 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 5bee105a-0143-3e83-9b75-3a19e402328b | -2.8939 | -45.383999 | 2024-11-23 00:00:00 | METOP-C | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 4c09b71f-f19e-3c6b-845e-545a60eecd66 | -2.6788 | -46.25 | 2024-11-23 00:00:00 | METOP-C | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| e082de2d-b6a1-3217-864a-22907a31c4dd | -4.5422 | -45.8885 | 2024-11-23 00:00:00 | METOP-C | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 85be50f8-4ef1-3bdf-b0fb-f01dca7bda39 | -2.8254 | -45.1707 | 2024-11-23 00:00:00 | METOP-C | SÃO BENTO | MARANHÃO | Brasil | 2110500 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| a206c6c8-bdbe-3c55-bf60-501ebdc138a5 | -4.5382 | -42.920101 | 2024-11-23 00:00:00 | METOP-C | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| deca8cb9-7bfe-3a6a-bc70-bb0e30884907 | -4.5939 | -46.493599 | 2024-11-23 00:00:00 | METOP-C | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 0204ab29-c375-3c1f-af8e-798c7f6bb4ee | -10.5084 | -36.706001 | 2024-11-23 00:00:00 | METOP-C | PACATUBA | SERGIPE | Brasil | 2804904 | 28 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 66c88875-9ad3-366b-8832-09162a065770 | -4.0127 | -44.3349 | 2024-11-23 00:00:00 | METOP-C | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 24f93d2c-fdb7-3ba0-91bd-c38aa44e174c | -4.028 | -46.197899 | 2024-11-23 00:00:00 | METOP-C | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 384d609a-ea8f-3235-8c0b-a91e40a09f66 | -3.1458 | -44.405499 | 2024-11-23 00:00:00 | METOP-C | SANTA RITA | MARANHÃO | Brasil | 2110203 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 677a8eff-af3e-3dd8-872b-2ba04030bc98 | -4.1154 | -43.234798 | 2024-11-23 00:00:00 | METOP-C | COELHO NETO | MARANHÃO | Brasil | 2103406 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| f2c92d0d-6a3b-311b-96ba-61277c20358d | -2.8913 | -45.372299 | 2024-11-23 00:00:00 | METOP-C | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 10df00d0-839c-3560-8573-c26ecd1391d7 | -3.3443 | -43.827702 | 2024-11-23 00:00:00 | METOP-C | NINA RODRIGUES | MARANHÃO | Brasil | 2107209 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 6c71a5a3-3076-3abd-96e3-36601931afa3 | -4.5972 | -46.508301 | 2024-11-23 00:00:00 | METOP-C | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 094b0873-adc9-3c71-b6a2-043a0b353c5a | -5.7477 | -46.2635 | 2024-11-23 00:00:00 | METOP-C | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 03919a90-d6a3-35bf-babf-7a94442b5fe3 | -10.0777 | -36.496101 | 2024-11-23 00:00:00 | METOP-C | IGREJA NOVA | ALAGOAS | Brasil | 2703205 | 27 | 33 | nan | nan | nan | Mata Atlântica | nan |
| c9abdf33-7ea1-301c-a03a-2e53e0c45cd2 | -3.7291 | -46.049801 | 2024-11-23 00:00:00 | METOP-C | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | nan |


[Clique aqui para ver as próximas entradas](README2.md)
