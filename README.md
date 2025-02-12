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
| 622e1d93-a547-3a37-9a66-4eaa3ad701db | 1.121 | -60.5224 | 2025-02-12 00:00:00 | GOES-16 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 71.7 |
| 5f96e43e-5c2b-3db7-8cbb-31886991bbbe | -9.8582 | -36.0297 | 2025-02-12 00:00:00 | GOES-16 | ROTEIRO | ALAGOAS | Brasil | 2707800 | 27 | 33 | nan | nan | nan | Mata Atlântica | 55.8 |
| f58d2ded-9f53-3f19-93ed-889b28efe1b1 | 1.121 | -60.5224 | 2025-02-12 00:10:00 | GOES-16 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 65.0 |
| bca9209f-6031-3e22-87be-296e832d44db | 1.121 | -60.5224 | 2025-02-12 00:20:00 | GOES-16 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 67.7 |
| a17062cc-1e6c-3a45-9ab5-3a8d7fb58de4 | -19.2208 | -40.1595 | 2025-02-12 00:24:00 | METOP-C | LINHARES | ESPÍRITO SANTO | Brasil | 3203205 | 32 | 33 | nan | nan | nan | Mata Atlântica | nan |
| ab23d5de-9442-3cb1-a093-a95eae26b38b | -9.8736 | -41.804001 | 2025-02-12 00:24:00 | METOP-C | SENTO SÉ | BAHIA | Brasil | 2930204 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| 31e47d67-cdc6-3c9c-a34d-ef8a5428407d | -10.533 | -44.672401 | 2025-02-12 00:24:00 | METOP-C | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 8fe1ebf4-dfec-3c12-8e67-6743406e3908 | -19.222601 | -40.167198 | 2025-02-12 00:24:00 | METOP-C | LINHARES | ESPÍRITO SANTO | Brasil | 3203205 | 32 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 086296e4-494c-33fc-8967-c633d52b4e03 | -11.0109 | -45.060299 | 2025-02-12 00:28:00 | METOP-C | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 988aa275-efda-3c8d-b110-21cedfeabfb6 | -17.740299 | -41.627998 | 2025-02-12 00:28:00 | METOP-C | TEÓFILO OTONI | MINAS GERAIS | Brasil | 3168606 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 4a05b3a3-b731-3021-8646-90f2845156a6 | -10.6583 | -44.497398 | 2025-02-12 00:28:00 | METOP-C | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| c2ba4f12-3e5b-33f4-ba71-56b8bbdf308b | -10.1711 | -36.542702 | 2025-02-12 00:28:00 | METOP-C | IGREJA NOVA | ALAGOAS | Brasil | 2703205 | 27 | 33 | nan | nan | nan | Caatinga | nan |
| 3be1a0aa-32a8-3d31-a76d-c9420b3ffd9d | -17.742001 | -41.6353 | 2025-02-12 00:28:00 | METOP-C | TEÓFILO OTONI | MINAS GERAIS | Brasil | 3168606 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| a43cf373-dfd7-3959-8838-5313c0e7ea76 | -10.6567 | -44.490501 | 2025-02-12 00:28:00 | METOP-C | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| a3b3fedd-22f5-3d11-a9a7-683d46806a15 | -13.4851 | -44.015598 | 2025-02-12 00:28:00 | METOP-C | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| cc1cd626-e65d-32be-9ce8-bd214ddd7a05 | -11.0094 | -45.0532 | 2025-02-12 00:28:00 | METOP-C | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 3413457e-b8e1-33d5-bc15-8a3fdcd1f258 | -10.6552 | -44.483501 | 2025-02-12 00:28:00 | METOP-C | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 974cd153-35ca-31f7-9842-5367177ea521 | 1.121 | -60.5224 | 2025-02-12 00:40:00 | GOES-16 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 43.0 |
| 61651ec2-92a1-3512-9895-dc4c93ee7beb | -16.091999 | -60.051399 | 2025-02-12 01:12:00 | METOP-B | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| d4d35ec4-5445-3cd6-8d67-e5ed6c8385a8 | -20.918501 | -56.52 | 2025-02-12 01:12:00 | METOP-B | BONITO | MATO GROSSO DO SUL | Brasil | 5002209 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| 6a984e82-44d7-3d1d-9327-1a94201c0c95 | -21.976801 | -57.5793 | 2025-02-12 01:12:00 | METOP-B | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| 6815bcdc-39d4-316b-aedc-dc1327d4fcaf | -20.9202 | -56.527599 | 2025-02-12 01:12:00 | METOP-B | BONITO | MATO GROSSO DO SUL | Brasil | 5002209 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| 75f11b9c-713c-39c5-956a-1c312c6bf087 | -20.9105 | -56.529999 | 2025-02-12 01:12:00 | METOP-B | BONITO | MATO GROSSO DO SUL | Brasil | 5002209 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| 468a91a1-82c8-37fc-9493-5e30a075ab84 | -21.0835 | -56.381699 | 2025-02-12 01:12:00 | METOP-B | BONITO | MATO GROSSO DO SUL | Brasil | 5002209 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| 5d0e183f-e459-37d5-a471-df2e3b5ed159 | -19.495199 | -55.318699 | 2025-02-12 01:12:00 | METOP-B | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 4c2e16af-757b-3727-b998-29e2e687dc08 | -21.0818 | -56.3741 | 2025-02-12 01:12:00 | METOP-B | BONITO | MATO GROSSO DO SUL | Brasil | 5002209 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| c19980c1-77fd-3f7c-b1ea-ac7cbd752000 | -16.093599 | -60.058601 | 2025-02-12 01:12:00 | METOP-B | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| d4212960-3baa-3fb1-86a9-6e39beaad11a | -21.085199 | -56.389301 | 2025-02-12 01:12:00 | METOP-B | BONITO | MATO GROSSO DO SUL | Brasil | 5002209 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| 0fe03b97-2881-3ce5-8aa8-cd7a767fcbc4 | -20.56863 | -55.09241 | 2025-02-12 01:24:00 | TERRA_M-M | TERENOS | MATO GROSSO DO SUL | Brasil | 5008008 | 50 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 60b99453-d036-3468-a114-e0451e26649d | -20.91108 | -56.53434 | 2025-02-12 01:24:00 | TERRA_M-M | BONITO | MATO GROSSO DO SUL | Brasil | 5002209 | 50 | 33 | nan | nan | nan | Cerrado | 23.9 |
| abf09e70-542e-367e-96ba-5a0e3e1f0f80 | -20.91237 | -56.54414 | 2025-02-12 01:24:00 | TERRA_M-M | BONITO | MATO GROSSO DO SUL | Brasil | 5002209 | 50 | 33 | nan | nan | nan | Cerrado | 7.4 |
| b62dd912-1869-3f4d-8a6a-04ac67b40df1 | -21.96585 | -57.58915 | 2025-02-12 01:24:00 | TERRA_M-M | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 03ee570d-b8bc-3ea1-a8cc-c4b22bfa4419 | -21.07545 | -56.387 | 2025-02-12 01:24:00 | TERRA_M-M | BONITO | MATO GROSSO DO SUL | Brasil | 5002209 | 50 | 33 | nan | nan | nan | Cerrado | 18.3 |
| 0e8244df-5e65-377e-ab59-1a8222810f74 | -21.07675 | -56.39679 | 2025-02-12 01:24:00 | TERRA_M-M | BONITO | MATO GROSSO DO SUL | Brasil | 5002209 | 50 | 33 | nan | nan | nan | Cerrado | 13.4 |
| 6855748c-1b2a-302c-843a-260892d28a76 | -16.08862 | -60.06321 | 2025-02-12 01:24:00 | TERRA_M-M | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 13.5 |
| 9bfbb378-c639-3a7a-835d-fdef1b9c77f6 | 4.82433 | -60.18135 | 2025-02-12 01:32:00 | TERRA_M-M | UIRAMUTÃ | RORAIMA | Brasil | 1400704 | 14 | 33 | nan | nan | nan | Amazônia | 19.4 |
| 4c1a64df-9f9b-39e5-9276-babcf238e4eb | -6.849 | -34.9338 | 2025-02-12 02:20:00 | GOES-16 | RIO TINTO | PARAÍBA | Brasil | 2512903 | 25 | 33 | nan | nan | nan | Mata Atlântica | 112.9 |
| d935cf86-27e8-34b1-a1a0-34e48ca0374b | -10.1226 | -36.3067 | 2025-02-12 02:50:00 | GOES-16 | CORURIPE | ALAGOAS | Brasil | 2702306 | 27 | 33 | nan | nan | nan | Mata Atlântica | 82.2 |
| 976cfc14-d477-3b2e-8471-19855c2d8369 | -10.1419 | -36.3032 | 2025-02-12 02:50:00 | GOES-16 | CORURIPE | ALAGOAS | Brasil | 2702306 | 27 | 33 | nan | nan | nan | Mata Atlântica | 143.1 |
| b462bb79-9b1a-3f63-9d02-f0dba46c8c50 | -10.1424 | -36.2761 | 2025-02-12 02:50:00 | GOES-16 | CORURIPE | ALAGOAS | Brasil | 2702306 | 27 | 33 | nan | nan | nan | Mata Atlântica | 69.9 |
| 7c9530bd-4a27-3c63-8e5f-50b4f1acb0fc | -5.97775 | -39.68439 | 2025-02-12 03:10:00 | NOAA-21 | MOMBAÇA | CEARÁ | Brasil | 2308500 | 23 | 33 | nan | nan | nan | Caatinga | 4.0 |
| 60332a52-85cb-38f3-97e9-4fd548013bcc | -7.23175 | -35.78493 | 2025-02-12 03:10:00 | NOAA-21 | MASSARANDUBA | PARAÍBA | Brasil | 2509206 | 25 | 33 | nan | nan | nan | Caatinga | 1.3 |
| e76a6c39-b3b3-30cd-a609-8632a64c8c00 | -8.22867 | -35.32353 | 2025-02-12 03:10:00 | NOAA-21 | VITÓRIA DE SANTO ANTÃO | PERNAMBUCO | Brasil | 2616407 | 26 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 320f5e62-71d1-3342-bae6-9f724e49e459 | -7.23228 | -35.78192 | 2025-02-12 03:10:00 | NOAA-21 | MASSARANDUBA | PARAÍBA | Brasil | 2509206 | 25 | 33 | nan | nan | nan | Caatinga | 0.9 |
| ac50a493-164a-3be8-83bf-170a350b1dd0 | -9.09729 | -39.96265 | 2025-02-12 03:12:00 | NOAA-21 | CURAÇÁ | BAHIA | Brasil | 2909901 | 29 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 0f656a30-be30-339e-a943-b1d33d9e985d | -9.09628 | -39.96799 | 2025-02-12 03:12:00 | NOAA-21 | CURAÇÁ | BAHIA | Brasil | 2909901 | 29 | 33 | nan | nan | nan | Caatinga | 2.8 |
| b08b8168-2a7f-3693-9136-6f3d547904d0 | -9.85329 | -37.28034 | 2025-02-12 03:12:00 | NOAA-21 | PORTO DA FOLHA | SERGIPE | Brasil | 2805604 | 28 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 3c391129-5bb5-3783-9943-0a7b1c84c666 | -11.80649 | -38.22732 | 2025-02-12 03:12:00 | NOAA-21 | APORÁ | BAHIA | Brasil | 2901908 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| fc5b0583-e16f-32ab-9f93-10b6e6af7c65 | -10.13364 | -36.29706 | 2025-02-12 03:12:00 | NOAA-21 | CORURIPE | ALAGOAS | Brasil | 2702306 | 27 | 33 | nan | nan | nan | Mata Atlântica | 17.5 |
| d059d4de-9580-36d6-8bf9-46d624c2977c | -9.0989 | -39.96457 | 2025-02-12 03:12:00 | NOAA-21 | CURAÇÁ | BAHIA | Brasil | 2909901 | 29 | 33 | nan | nan | nan | Caatinga | 3.8 |
| 874e7125-b852-38c3-af8c-3c0f56792706 | -9.8539 | -37.27707 | 2025-02-12 03:12:00 | NOAA-21 | PORTO DA FOLHA | SERGIPE | Brasil | 2805604 | 28 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 9abd9df1-ccbd-399b-b311-5eeab234df47 | -10.1347 | -36.29134 | 2025-02-12 03:12:00 | NOAA-21 | CORURIPE | ALAGOAS | Brasil | 2702306 | 27 | 33 | nan | nan | nan | Mata Atlântica | 17.0 |
| 766c425f-1cdb-30bd-9439-03a0c5c72ff7 | -20.7136 | -41.88628 | 2025-02-12 03:14:00 | NOAA-21 | CAIANA | MINAS GERAIS | Brasil | 3110103 | 31 | 33 | nan | nan | nan | Mata Atlântica | 5.4 |
| 31b0818a-3c8d-3ea8-9f55-646fca5a9095 | -19.22316 | -40.15969 | 2025-02-12 03:14:00 | NOAA-21 | LINHARES | ESPÍRITO SANTO | Brasil | 3203205 | 32 | 33 | nan | nan | nan | Mata Atlântica | 3.0 |
| 0c89a8c7-e140-3e9b-876f-562caca73126 | -20.70805 | -41.88603 | 2025-02-12 03:14:00 | NOAA-21 | CAIANA | MINAS GERAIS | Brasil | 3110103 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| e6a1240c-ee99-3ceb-85bd-60203c025203 | -20.71373 | -41.88784 | 2025-02-12 03:14:00 | NOAA-21 | CAIANA | MINAS GERAIS | Brasil | 3110103 | 31 | 33 | nan | nan | nan | Mata Atlântica | 5.8 |
| 0792865a-075e-38c9-a5d8-4db028da41cb | -19.22237 | -40.16344 | 2025-02-12 03:14:00 | NOAA-21 | LINHARES | ESPÍRITO SANTO | Brasil | 3203205 | 32 | 33 | nan | nan | nan | Mata Atlântica | 4.1 |
| 2c349adf-fd1d-33bd-a82f-b71a70718bed | -22.67375 | -42.86057 | 2025-02-12 03:17:00 | NOAA-21 | ITABORAÍ | RIO DE JANEIRO | Brasil | 3301900 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| ba989ead-cfed-3eae-8008-357b7a336f02 | -22.67624 | -42.86073 | 2025-02-12 03:17:00 | NOAA-21 | ITABORAÍ | RIO DE JANEIRO | Brasil | 3301900 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| be85c7ec-302c-392d-8cd7-7ff20bd20945 | -22.67732 | -42.85609 | 2025-02-12 03:17:00 | NOAA-21 | ITABORAÍ | RIO DE JANEIRO | Brasil | 3301900 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| c7dbcf5b-b6aa-32b1-b02d-998a86b6f80b | -22.67485 | -42.85596 | 2025-02-12 03:17:00 | NOAA-21 | ITABORAÍ | RIO DE JANEIRO | Brasil | 3301900 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| 780af74b-f9a0-3a55-9cf3-70bf8c8e4b9b | -6.34306 | -41.91769 | 2025-02-12 03:36:00 | NPP-375D | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 9f303619-a1d2-3f5b-918b-aa208af3eb1e | -7.0562 | -37.24393 | 2025-02-12 03:36:00 | NPP-375D | PATOS | PARAÍBA | Brasil | 2510808 | 25 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 01eaa363-3320-3c4a-8618-45e3bca22cc0 | -8.6026 | -36.74457 | 2025-02-12 03:36:00 | NPP-375D | PESQUEIRA | PERNAMBUCO | Brasil | 2610905 | 26 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 346ef36c-58f8-36df-8a62-0ab4bc79e69f | -6.49928 | -39.59406 | 2025-02-12 03:36:00 | NPP-375D | JUCÁS | CEARÁ | Brasil | 2307403 | 23 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 6d3b68c9-fea9-3e23-a3dd-e60a518e3962 | -6.74072 | -37.20945 | 2025-02-12 03:36:00 | NPP-375D | SÃO JOÃO DO SABUGI | RIO GRANDE DO NORTE | Brasil | 2412104 | 24 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 250b9e2a-ca4d-32d0-9a2d-ea1ff739212e | -3.43983 | -39.62379 | 2025-02-12 03:36:00 | NPP-375D | ITAPIPOCA | CEARÁ | Brasil | 2306405 | 23 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 26fed75f-8a2f-3b44-a255-2cdb09e60343 | -5.97582 | -39.68026 | 2025-02-12 03:36:00 | NPP-375D | MOMBAÇA | CEARÁ | Brasil | 2308500 | 23 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 6da6ae7e-deb0-329f-a390-bafb2a33bb47 | -8.22857 | -35.32649 | 2025-02-12 03:36:00 | NPP-375D | VITÓRIA DE SANTO ANTÃO | PERNAMBUCO | Brasil | 2616407 | 26 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 7e4e22c5-1081-3727-9a64-586059c5688c | -7.47521 | -34.84494 | 2025-02-12 03:36:00 | NPP-375D | PITIMBU | PARAÍBA | Brasil | 2511905 | 25 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| 80e82a8d-5488-39aa-ba1a-9aca5f307bc2 | -7.58249 | -37.49438 | 2025-02-12 03:36:00 | NPP-375D | TABIRA | PERNAMBUCO | Brasil | 2614600 | 26 | 33 | nan | nan | nan | Caatinga | 0.5 |
| 1a5986ac-27fb-324e-874f-f1dcaa4472d8 | -5.97513 | -39.68439 | 2025-02-12 03:36:00 | NPP-375D | MOMBAÇA | CEARÁ | Brasil | 2308500 | 23 | 33 | nan | nan | nan | Caatinga | 2.3 |
| de5d1ebc-d52b-379e-b8d1-0dd26ea2250c | -5.22034 | -40.35257 | 2025-02-12 03:36:00 | NPP-375D | INDEPENDÊNCIA | CEARÁ | Brasil | 2305605 | 23 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 5ec921ac-7b30-3291-8a96-47f599ccb67b | -7.23256 | -35.78452 | 2025-02-12 03:36:00 | NPP-375D | MASSARANDUBA | PARAÍBA | Brasil | 2509206 | 25 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 106ee942-0ba8-318e-b155-a92c6ee0938f | -8.43285 | -36.3726 | 2025-02-12 03:36:00 | NPP-375D | SÃO BENTO DO UNA | PERNAMBUCO | Brasil | 2613008 | 26 | 33 | nan | nan | nan | Caatinga | 0.4 |
| c35d7343-6d19-38ad-b97e-d4035de18257 | -6.54102 | -39.14938 | 2025-02-12 03:36:00 | NPP-375D | CEDRO | CEARÁ | Brasil | 2303808 | 23 | 33 | nan | nan | nan | Caatinga | 0.7 |
| fa9934f4-6f7e-31e7-9c98-7893d5f931a2 | -4.31348 | -39.91765 | 2025-02-12 03:36:00 | NPP-375D | SANTA QUITÉRIA | CEARÁ | Brasil | 2312205 | 23 | 33 | nan | nan | nan | Caatinga | 3.1 |
| 3e186d76-8724-38a0-99aa-5f420dab5409 | -7.01704 | -38.82333 | 2025-02-12 03:36:00 | NPP-375D | BARRO | CEARÁ | Brasil | 2302008 | 23 | 33 | nan | nan | nan | Caatinga | 0.9 |
| b836dbe3-06a5-356a-9f0e-10f7e425eb3b | -10.59505 | -44.78602 | 2025-02-12 03:38:00 | NPP-375D | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 0.5 |
| fab1128c-353e-38d1-bd71-87a9dd4a2d5a | -9.18035 | -40.31598 | 2025-02-12 03:38:00 | NPP-375D | PETROLINA | PERNAMBUCO | Brasil | 2611101 | 26 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 4eff9787-7950-3ed0-b639-e2480dead6f7 | -10.53491 | -44.67472 | 2025-02-12 03:38:00 | NPP-375D | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 0940013f-26ec-3f3e-aa29-63e3f105d5c5 | -11.93557 | -39.9967 | 2025-02-12 03:38:00 | NPP-375D | PINTADAS | BAHIA | Brasil | 2924652 | 29 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 16a99bf1-dfb8-3415-b568-3d5ffd9a788e | -10.53417 | -44.67853 | 2025-02-12 03:38:00 | NPP-375D | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 80808e53-a54b-3b85-ba09-266703aab245 | -10.13071 | -36.2912 | 2025-02-12 03:38:00 | NPP-375D | CORURIPE | ALAGOAS | Brasil | 2702306 | 27 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| f9842ca8-1aa4-3a70-9d7d-aa3c4dce05a8 | -11.01722 | -45.0556 | 2025-02-12 03:38:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 3.9 |
| da0c8f8f-0a41-3195-b8f8-3c03ad07c340 | -9.85079 | -37.2768 | 2025-02-12 03:38:00 | NPP-375D | PORTO DA FOLHA | SERGIPE | Brasil | 2805604 | 28 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 154a595f-6137-357b-bcf0-40eb67109f85 | -9.85435 | -37.27732 | 2025-02-12 03:38:00 | NPP-375D | PORTO DA FOLHA | SERGIPE | Brasil | 2805604 | 28 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 59af0795-2ed0-3a8d-9811-191f8cfa3aab | -15.64927 | -39.19001 | 2025-02-12 03:38:00 | NPP-375D | CANAVIEIRAS | BAHIA | Brasil | 2906303 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| e5fe3149-a27b-3179-b697-cc32999e52e3 | -9.57641 | -37.29401 | 2025-02-12 03:38:00 | NPP-375D | MONTEIRÓPOLIS | ALAGOAS | Brasil | 2705408 | 27 | 33 | nan | nan | nan | Caatinga | 1.1 |
| ae5cd474-e652-3b61-b7a0-665df1f0944e | -11.01644 | -45.05958 | 2025-02-12 03:38:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 0dc4f903-7ac0-3a7f-8303-0f3bfbeb7c20 | -11.01081 | -45.05824 | 2025-02-12 03:38:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| ce8ea321-5e8a-3781-a13e-279afb01efba | -11.01158 | -45.05428 | 2025-02-12 03:38:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 476c3cf2-dc49-3348-8777-452a089793b3 | -11.79403 | -40.93178 | 2025-02-12 03:38:00 | NPP-375D | MORRO DO CHAPÉU | BAHIA | Brasil | 2921708 | 29 | 33 | nan | nan | nan | Caatinga | 0.9 |
| b426493a-474a-31df-87cf-2be7b9e3d8d4 | -12.35445 | -38.27986 | 2025-02-12 03:38:00 | NPP-375D | POJUCA | BAHIA | Brasil | 2925204 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.3 |
| 50524bb6-ce3d-315e-8229-617425163084 | -13.03395 | -40.33394 | 2025-02-12 03:38:00 | NPP-375D | IAÇU | BAHIA | Brasil | 2911907 | 29 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 4746f244-fd61-34ee-86f6-43c9cf1e6559 | -10.58945 | -44.78481 | 2025-02-12 03:38:00 | NPP-375D | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 8b45f2f7-dc77-3ad3-9a0b-91bc200ea9ee | -9.09912 | -39.96452 | 2025-02-12 03:38:00 | NPP-375D | CURAÇÁ | BAHIA | Brasil | 2909901 | 29 | 33 | nan | nan | nan | Caatinga | 2.7 |
| 68033dbf-531a-3da4-9cde-ecb1e186228b | -20.20691 | -46.4302 | 2025-02-12 03:40:00 | NPP-375D | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 5c932b18-7a15-3e5e-afef-d6076717deca | -18.92968 | -41.93641 | 2025-02-12 03:40:00 | NPP-375D | ALPERCATA | MINAS GERAIS | Brasil | 3101805 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 0343274d-996e-37ab-9207-9aee96a77d0f | -22.69891 | -43.34943 | 2025-02-12 03:40:00 | NPP-375D | BELFORD ROXO | RIO DE JANEIRO | Brasil | 3300456 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |


[Clique aqui para ver as próximas entradas](README2.md)
