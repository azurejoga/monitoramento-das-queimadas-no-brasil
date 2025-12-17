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

## Dados Diários - Página 6

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 673a81dd-67eb-3f10-888b-d804bf285f7a | -4.75337 | -38.72194 | 2025-12-17 04:06:00 | NPP-375D | IBARETAMA | CEARÁ | Brasil | 2305266 | 23 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 340286d0-9760-349e-a475-e88528a5ffea | -4.4301 | -46.28658 | 2025-12-17 04:06:00 | NPP-375D | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 504095b9-8223-3066-9590-48b14708b48d | -10.0732 | -39.43744 | 2025-12-17 04:06:00 | NPP-375D | UAUÁ | BAHIA | Brasil | 2932002 | 29 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 538be457-2b00-3f76-af01-03a0fbdec9f2 | -5.44846 | -43.52319 | 2025-12-17 04:06:00 | NPP-375D | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 455f3ef2-56c5-3c63-b542-7fe2145997f9 | -9.00962 | -45.92157 | 2025-12-17 04:06:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 4c591f21-6002-35ae-94e5-a27e51e7fd27 | -5.36768 | -36.8416 | 2025-12-17 04:06:00 | NPP-375D | CARNAUBAIS | RIO GRANDE DO NORTE | Brasil | 2402501 | 24 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 06f5aa95-56b2-3be8-ae51-5368efc76015 | -3.65961 | -47.54722 | 2025-12-17 04:06:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 03f6771d-96ad-3e39-9857-0f7ddd980c2c | -8.3713 | -35.57884 | 2025-12-17 04:06:00 | NPP-375D | BARRA DE GUABIRABA | PERNAMBUCO | Brasil | 2601300 | 26 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 1f3fd12e-d6ce-3ffb-835e-54cbd14bff67 | -4.43322 | -46.28975 | 2025-12-17 04:06:00 | NPP-375D | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 78fe45aa-a332-3ee7-b828-eba92946951c | -5.44473 | -43.52255 | 2025-12-17 04:06:00 | NPP-375D | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 4.2 |
| dc9fc181-9e7c-31cf-bb15-62bcc2a2aadf | -9.36499 | -40.52893 | 2025-12-17 04:06:00 | NPP-375D | PETROLINA | PERNAMBUCO | Brasil | 2611101 | 26 | 33 | nan | nan | nan | Caatinga | 1.0 |
| b64e713a-17d2-3513-9c55-b128d0ab3607 | -5.32355 | -40.5526 | 2025-12-17 04:06:00 | NPP-375D | CRATEÚS | CEARÁ | Brasil | 2304103 | 23 | 33 | nan | nan | nan | Caatinga | 2.9 |
| a70acdca-18ff-3e5b-842f-bdafc8bab400 | -2.79194 | -51.40409 | 2025-12-17 04:06:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 76dc865f-f0a7-317c-b7a7-39a5d0211804 | -9.00899 | -45.92529 | 2025-12-17 04:06:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 7662a463-5a67-3481-967d-20b1ac3253b1 | -4.42834 | -43.69205 | 2025-12-17 04:06:00 | NPP-375D | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 28b5ea0e-7eeb-39cb-9e5f-f621570c688e | -9.39182 | -35.90586 | 2025-12-17 04:06:00 | NPP-375D | MURICI | ALAGOAS | Brasil | 2705507 | 27 | 33 | nan | nan | nan | Mata Atlântica | 2.7 |
| fc80ce98-e433-3c0e-a311-fc3bbddb0563 | -9.82083 | -43.93605 | 2025-12-17 04:06:00 | NPP-375D | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| cb6f5628-4884-397a-ab9d-180d2e75d54a | -8.58999 | -39.4478 | 2025-12-17 04:06:00 | NPP-375D | CURAÇÁ | BAHIA | Brasil | 2909901 | 29 | 33 | nan | nan | nan | Caatinga | 4.0 |
| 931ab78f-409c-3011-9283-a0be4ce35467 | -4.39749 | -45.76426 | 2025-12-17 04:06:00 | NPP-375D | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| bb6c3b32-c8d2-3e5c-a5a1-b7c02ea25ada | -5.9839 | -44.59289 | 2025-12-17 04:06:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 2fdb3c87-3172-32a2-8746-b14174e287bf | -9.26809 | -44.31462 | 2025-12-17 04:06:00 | NPP-375D | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| c27ab208-e938-3b05-af13-56ef1a398f4a | -5.98784 | -44.59358 | 2025-12-17 04:06:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 0590258d-d8eb-3b2f-a33b-20325c507017 | -8.56545 | -39.47314 | 2025-12-17 04:06:00 | NPP-375D | CABROBÓ | PERNAMBUCO | Brasil | 2603009 | 26 | 33 | nan | nan | nan | Caatinga | 1.3 |
| b8d16997-0205-3937-b876-eae3c987a3b3 | -4.39697 | -45.76678 | 2025-12-17 04:06:00 | NPP-375D | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 99a52444-6817-34a9-959c-a81cc4484528 | -9.16281 | -35.69037 | 2025-12-17 04:06:00 | NPP-375D | SÃO LUÍS DO QUITUNDE | ALAGOAS | Brasil | 2708501 | 27 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| a2b5b796-3d9a-3ddd-9cc9-fc40d94abe2a | -6.79155 | -39.95962 | 2025-12-17 04:06:00 | NPP-375D | ANTONINA DO NORTE | CEARÁ | Brasil | 2300804 | 23 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 7a63c099-3473-30df-a1d4-b0abdb3fb9c1 | -5.57593 | -43.59347 | 2025-12-17 04:06:00 | NPP-375D | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| f7ec4cc1-d91f-3317-bc74-1d2da10e013a | -2.69884 | -51.64178 | 2025-12-17 04:06:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 137f7f2f-9253-34ab-9d76-ce01d0789799 | -2.79101 | -51.40942 | 2025-12-17 04:06:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 0ed82ab4-05c4-3c36-b976-fb5494a891e0 | -4.72124 | -40.40347 | 2025-12-17 04:06:00 | NPP-375D | TAMBORIL | CEARÁ | Brasil | 2313203 | 23 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 4c48ef62-6954-3ff7-8bd3-824e6f05b80b | -9.3958 | -35.90647 | 2025-12-17 04:06:00 | NPP-375D | RIO LARGO | ALAGOAS | Brasil | 2707701 | 27 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| ade7f3ce-a40a-3a61-b33a-cac508257f3f | -3.64966 | -46.89674 | 2025-12-17 04:06:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 2.6 |
| b185db0f-f88f-34d4-bc33-1abf18a8e65e | -9.26512 | -44.3096 | 2025-12-17 04:06:00 | NPP-375D | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 97ced51e-0e86-3421-9441-82e4c8e3231a | -5.47442 | -45.40668 | 2025-12-17 04:06:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| b8fa1ea2-dda6-3095-b042-758d72ac2a21 | -3.65948 | -47.55231 | 2025-12-17 04:06:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 97204ff7-c2e7-366b-b088-b4e422eac3d6 | -8.3718 | -35.57546 | 2025-12-17 04:06:00 | NPP-375D | BARRA DE GUABIRABA | PERNAMBUCO | Brasil | 2601300 | 26 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| e9f73a04-a041-3d66-a00f-b6a22af45e86 | -9.00835 | -45.929 | 2025-12-17 04:06:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 46719c3f-e2e6-3ddd-be07-97c4a9542858 | -9.28913 | -40.49175 | 2025-12-17 04:06:00 | NPP-375D | PETROLINA | PERNAMBUCO | Brasil | 2611101 | 26 | 33 | nan | nan | nan | Caatinga | 0.5 |
| efab5b95-9988-3210-8280-dee99d750e78 | -2.79282 | -51.4064 | 2025-12-17 04:06:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 1e2cb579-69c2-38a2-8bd6-f4f467a25445 | -9.82455 | -40.57063 | 2025-12-17 04:06:00 | NPP-375D | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 1.6 |
| e66fd238-d167-3fbf-ae5b-6eb924659630 | -5.57859 | -44.88567 | 2025-12-17 04:06:00 | NPP-375D | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 10452b3b-3ee2-3d3b-8450-1cbd22366ae5 | -5.08392 | -40.37506 | 2025-12-17 04:06:00 | NPP-375D | TAMBORIL | CEARÁ | Brasil | 2313203 | 23 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 358cb831-53b7-34db-8e7c-22b09b9d4178 | -8.5649 | -39.47669 | 2025-12-17 04:06:00 | NPP-375D | CABROBÓ | PERNAMBUCO | Brasil | 2603009 | 26 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 9eaa7083-5930-3275-96cb-d94daf8fb9ab | -3.66038 | -47.54684 | 2025-12-17 04:06:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 6bec05a1-0f82-33eb-8029-6d22759bf687 | -4.13793 | -46.29211 | 2025-12-17 04:06:00 | NPP-375D | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| acbdb1ea-1a1a-3b48-90e7-b8af8871dbd3 | -5.47378 | -45.41046 | 2025-12-17 04:06:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 2670624c-a964-325e-a6f9-1b6442e2abf2 | -5.4492 | -43.51872 | 2025-12-17 04:06:00 | NPP-375D | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 5f5d466d-a8cc-3152-89c9-571f0654c9d9 | -5.57799 | -44.88928 | 2025-12-17 04:06:00 | NPP-375D | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 675525d9-8b28-34a2-ac1d-59d4eaa5cfe5 | -2.79192 | -51.41174 | 2025-12-17 04:06:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 7e7853b8-cf27-3bf9-978c-abc46c4106df | -9.16684 | -35.69097 | 2025-12-17 04:06:00 | NPP-375D | SÃO LUÍS DO QUITUNDE | ALAGOAS | Brasil | 2708501 | 27 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| ee3204b8-cc9e-3609-b76f-f1f6facf49a2 | -5.97194 | -43.77072 | 2025-12-17 04:06:00 | NPP-375D | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 141dffb9-ec64-3246-a067-a7173b885ee9 | -10.36185 | -39.12608 | 2025-12-17 04:06:00 | NPP-375D | EUCLIDES DA CUNHA | BAHIA | Brasil | 2910701 | 29 | 33 | nan | nan | nan | Caatinga | 1.4 |
| d3b04b5c-6b86-3107-93b3-8952fc71577b | -9.16332 | -35.68681 | 2025-12-17 04:06:00 | NPP-375D | SÃO LUÍS DO QUITUNDE | ALAGOAS | Brasil | 2708501 | 27 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 54d5da46-73d2-33e1-a08e-a90208a9fbf9 | -4.32584 | -44.82452 | 2025-12-17 04:06:00 | NPP-375D | BACABAL | MARANHÃO | Brasil | 2101202 | 21 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 1bc64dc2-3fa7-318c-a366-265524389c95 | -3.21771 | -49.36273 | 2025-12-17 04:06:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 6fe57cd0-b8c3-3f5b-a9ae-d236bd9d069b | -5.58263 | -44.8864 | 2025-12-17 04:06:00 | NPP-375D | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 76ba6e9d-f400-3f7e-8018-3b1381e0e585 | -3.65052 | -46.89151 | 2025-12-17 04:06:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 2c31e45e-dc19-3700-b4c1-8f290f022c5e | -9.01308 | -45.92606 | 2025-12-17 04:06:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| b8d7877d-b11e-30e0-9b10-e9d9c3d7c112 | -4.32895 | -45.87909 | 2025-12-17 04:06:00 | NPP-375D | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 504e79d2-e67a-325e-8ce5-0be72593a390 | -4.24539 | -45.97844 | 2025-12-17 04:06:00 | NPP-375D | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| e57411ce-a981-371c-945c-69dfae1f3fab | -4.42869 | -46.28895 | 2025-12-17 04:06:00 | NPP-375D | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 0d0ccd2e-7bb7-3601-bb2e-3fe50e35d376 | -3.65867 | -47.55267 | 2025-12-17 04:06:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 23b65ee2-3464-35d8-970e-97f3574417fc | -8.84116 | -35.68002 | 2025-12-17 04:06:00 | NPP-375D | XEXÉU | PERNAMBUCO | Brasil | 2616506 | 26 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 70e7309a-cf40-3b46-b32a-739944708b9d | -9.15852 | -40.97564 | 2025-12-17 04:06:00 | NPP-375D | CASA NOVA | BAHIA | Brasil | 2907202 | 29 | 33 | nan | nan | nan | Caatinga | 2.2 |
| be3983fb-e86d-38e3-a5e0-046862da44b2 | -9.1552 | -40.97511 | 2025-12-17 04:06:00 | NPP-375D | CASA NOVA | BAHIA | Brasil | 2907202 | 29 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 0b7251a2-edc3-3044-b053-192b895c9803 | -2.69787 | -51.64746 | 2025-12-17 04:06:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| b823728a-5558-385b-ba23-8c72a6f81dcd | -4.42947 | -46.28419 | 2025-12-17 04:06:00 | NPP-375D | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| daa45c21-7aa6-3d3f-9d45-61f5ea1618cb | -10.07376 | -39.4338 | 2025-12-17 04:06:00 | NPP-375D | UAUÁ | BAHIA | Brasil | 2932002 | 29 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 06fc0e88-f577-3b58-b01d-41ebbe2b9510 | -9.87935 | -40.56864 | 2025-12-17 04:06:00 | NPP-375D | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 1.2 |
| e5b344cb-3c74-3242-9260-9897cc6b47a4 | -4.32644 | -44.82082 | 2025-12-17 04:06:00 | NPP-375D | BACABAL | MARANHÃO | Brasil | 2101202 | 21 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 18dbd79f-f122-37d1-a1ba-3b2ffe978ea2 | -6.20442 | -39.73546 | 2025-12-17 04:06:00 | NPP-375D | ACOPIARA | CEARÁ | Brasil | 2300309 | 23 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 66ab9af2-2546-3ad1-b5e7-0f2385edc658 | -11.80304 | -41.77259 | 2025-12-17 04:08:00 | NPP-375D | CANARANA | BAHIA | Brasil | 2906204 | 29 | 33 | nan | nan | nan | Caatinga | 0.4 |
| cf44ade4-998f-3af2-ac72-92fc09aa5bfc | -11.01563 | -45.25729 | 2025-12-17 04:08:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 8c992b45-b16f-31eb-a2d6-74026eb874b1 | -13.7234 | -43.7774 | 2025-12-17 04:08:00 | NPP-375D | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 6eada6b2-4412-3a28-ac63-7313cef02152 | -11.97258 | -44.49451 | 2025-12-17 04:08:00 | NPP-375D | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 86b06136-3bbb-3af3-895d-96705b867bee | -11.82131 | -43.79424 | 2025-12-17 04:08:00 | NPP-375D | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| fa001c4e-0250-3e2e-8111-10747274464b | -12.39579 | -43.66281 | 2025-12-17 04:08:00 | NPP-375D | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 1a420127-b337-326c-8128-0dd6ea1eab7e | -12.66882 | -46.77742 | 2025-12-17 04:08:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| a8bfc3fc-2270-32ce-8b2f-13b6779b17b8 | -14.05031 | -43.8872 | 2025-12-17 04:08:00 | NPP-375D | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| ffceaead-8b34-3362-9152-1497debb7ab5 | -12.42095 | -44.45382 | 2025-12-17 04:08:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 0.5 |
| a8fa829b-2bfd-382a-9187-76247cf795b1 | -11.37719 | -39.25909 | 2025-12-17 04:08:00 | NPP-375D | CONCEIÇÃO DO COITÉ | BAHIA | Brasil | 2908408 | 29 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 3493a922-ab4d-3ee4-9328-c13d389eb029 | -11.96837 | -44.49565 | 2025-12-17 04:08:00 | NPP-375D | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 855dd903-423b-32f1-bc45-ab4c4a99a520 | -11.02026 | -45.25325 | 2025-12-17 04:08:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 7583defc-d58a-3c9b-8d71-4e2b5f6b2637 | -13.72517 | -43.78081 | 2025-12-17 04:08:00 | NPP-375D | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 540e5d3f-737c-361d-968a-7a762e282825 | -14.43712 | -44.86542 | 2025-12-17 04:08:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 5493dfcb-5458-35b3-a470-c4d9eb801891 | -14.22657 | -44.31971 | 2025-12-17 04:08:00 | NPP-375D | FEIRA DA MATA | BAHIA | Brasil | 2910776 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 4bcfc56c-d959-3d3b-b0ff-ae3c62dc0a33 | -12.30142 | -43.73051 | 2025-12-17 04:08:00 | NPP-375D | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 0.3 |
| 5152dd4d-68d6-3426-8abe-c55d69809dd2 | -11.7661 | -44.62909 | 2025-12-17 04:08:00 | NPP-375D | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 1f32b66d-5028-3a39-8302-74385aea66ca | -11.96908 | -44.49142 | 2025-12-17 04:08:00 | NPP-375D | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 0b95340b-0a1e-3c1b-8381-4f53f5d645db | -13.72582 | -43.77698 | 2025-12-17 04:08:00 | NPP-375D | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 6a1a07e6-542b-3a79-af56-e9b43e51b670 | -11.80247 | -41.77612 | 2025-12-17 04:08:00 | NPP-375D | CANARANA | BAHIA | Brasil | 2906204 | 29 | 33 | nan | nan | nan | Caatinga | 0.4 |
| 0ca4a55a-7279-3f3d-8c38-ff023869bd6f | -11.84939 | -43.73389 | 2025-12-17 04:08:00 | NPP-375D | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 9852b760-7333-38d9-a8cf-8cff1fb7afd4 | -14.23006 | -44.32035 | 2025-12-17 04:08:00 | NPP-375D | FEIRA DA MATA | BAHIA | Brasil | 2910776 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 002dff45-d085-37bf-91aa-2e767c719ee8 | -11.84873 | -43.73785 | 2025-12-17 04:08:00 | NPP-375D | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| d03baf4b-0143-3f4b-ba82-4839c7561b23 | -11.82198 | -43.79026 | 2025-12-17 04:08:00 | NPP-375D | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 445d8959-17c0-391c-ae08-bcbb92b7b3bd | -13.38427 | -41.87267 | 2025-12-17 04:08:00 | NPP-375D | RIO DE CONTAS | BAHIA | Brasil | 2926707 | 29 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 28e5697a-639a-3efb-8a68-87e1c56021a4 | -12.67357 | -46.77445 | 2025-12-17 04:08:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 5.8 |
| ec9e5e1b-8358-3614-85b9-a6b98dea266b | -13.18238 | -42.96135 | 2025-12-17 04:08:00 | NPP-375D | BOM JESUS DA LAPA | BAHIA | Brasil | 2903904 | 29 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 02916d01-1b44-3015-98e9-4e7e88b99b95 | -11.73159 | -44.59384 | 2025-12-17 04:08:00 | NPP-375D | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 5df1cbd5-ed87-3037-b979-95b0e9a49714 | -14.04686 | -43.8866 | 2025-12-17 04:08:00 | NPP-375D | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 0.4 |


[Clique aqui para ver as próximas entradas](README7.md)
