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

## Dados Diários - Página 38

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 19578037-4553-3dc2-905e-f7d66620d12d | -4.31797 | -48.21499 | 2024-12-02 04:25:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 385c101a-6322-3bc1-9255-bb3392c5fbd2 | -3.74282 | -52.26771 | 2024-12-02 04:25:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 6f30101a-8ecd-39e0-af36-f2c4a07efda5 | -4.27374 | -50.68791 | 2024-12-02 04:25:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 5db36d33-d7ce-3f34-bd95-88fab7eece71 | -3.96817 | -46.34358 | 2024-12-02 04:25:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| af0ca1c0-2bdc-367f-9bda-c017e72f17cd | -3.85641 | -46.53661 | 2024-12-02 04:25:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 0fbf9975-db1a-3b0c-9d84-411ae2509da1 | -4.31509 | -48.21056 | 2024-12-02 04:25:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 62cc1dbd-3cb1-3838-a9b4-aae31eca5451 | -2.98347 | -53.88364 | 2024-12-02 04:25:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 869f2878-f3c1-3e35-ac92-951ce6bd7197 | -3.31129 | -50.50262 | 2024-12-02 04:25:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 5d7dbd62-da12-3462-b95e-3d45f42e8c7d | -2.62933 | -53.3647 | 2024-12-02 04:25:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| e9719e43-107e-3e7e-91e7-c00774e648a0 | -3.21026 | -50.27349 | 2024-12-02 04:25:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| a65790fb-7282-3e21-97d7-0f24dd6351fb | -4.03916 | -46.85832 | 2024-12-02 04:25:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 06fdd4c4-ca58-3c6d-b8b8-e87924c551d5 | -5.58435 | -45.14499 | 2024-12-02 04:25:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 6.2 |
| b85bfa39-a150-3471-9376-0e38d4da3032 | -4.09116 | -46.12065 | 2024-12-02 04:25:00 | NPP-375D | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 9b04cb17-1c27-366a-8b91-f07c72d010d5 | -3.82797 | -46.56461 | 2024-12-02 04:25:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 5c9dc518-caeb-314b-a797-f596296b3c36 | -3.93485 | -46.7044 | 2024-12-02 04:25:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 6bd2d875-c796-38a0-abaf-52ac42061935 | -3.95155 | -46.9252 | 2024-12-02 04:25:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a0fc1321-63c4-397b-90db-45fc39d6da96 | -4.25935 | -50.85233 | 2024-12-02 04:25:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| c89117c9-f9fd-3ace-a39c-57e1db32b624 | -3.1547 | -51.11441 | 2024-12-02 04:25:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.3 |
| 6cf2f97f-6d81-366d-a6be-d57e0190a65e | -3.9441 | -49.98522 | 2024-12-02 04:25:00 | NPP-375D | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 7932fe8f-8c8d-3dc2-b596-7e420cd525a3 | -5.20204 | -45.53667 | 2024-12-02 04:25:00 | NPP-375D | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 83b1b0c5-cfb5-3def-8cec-3299a1fe3e57 | -4.5905 | -50.60939 | 2024-12-02 04:25:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| f4090af3-b496-328a-99a6-b6b2c264a7e6 | -2.83292 | -51.83345 | 2024-12-02 04:25:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 79bbea87-592e-328e-b058-b0d461b51c4d | -4.76708 | -46.42949 | 2024-12-02 04:25:00 | NPP-375D | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 6bbb3d1a-ee3a-39c6-999a-7ca5ff8f02dd | -4.0515 | -46.82394 | 2024-12-02 04:25:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 3088b5af-e298-3c69-9e06-be30a648f35c | -5.61148 | -45.05898 | 2024-12-02 04:25:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 42d11bde-f8c3-3f56-94fd-6578618d2ad9 | 1.65604 | -50.7728 | 2024-12-02 04:25:00 | NPP-375D | PRACUÚBA | AMAPÁ | Brasil | 1600550 | 16 | 33 | nan | nan | nan | Amazônia | 0.7 |
| f6f04378-137e-37d3-9ce7-88c26777d6dc | -3.10944 | -50.31511 | 2024-12-02 04:25:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 11a81ec2-35a1-39c5-bafb-a282fff519bd | -4.07721 | -46.68323 | 2024-12-02 04:25:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| daa322c8-350e-3ee5-857d-b057fddbfc92 | -5.58507 | -45.2063 | 2024-12-02 04:25:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 4.1 |
| f5aa2272-7ef2-3bbc-a4d2-17968370f97b | -4.07489 | -49.06535 | 2024-12-02 04:25:00 | NPP-375D | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| a12ce373-ec5c-303c-89ca-5d1a9734e894 | -3.27558 | -50.2076 | 2024-12-02 04:25:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 6a9ca1fb-c34c-3009-9991-7621503f8e41 | -3.74735 | -52.26828 | 2024-12-02 04:25:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| d5a92e43-5212-3cb1-b90c-986f9c82f5b1 | -3.33039 | -53.5493 | 2024-12-02 04:25:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 593aeea3-58c5-3dca-a6f2-f3005e19dab4 | -4.62624 | -48.02222 | 2024-12-02 04:25:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| ab07a24b-fbd8-3e6d-bcb2-0810aebf5062 | -4.1353 | -44.831 | 2024-12-02 04:25:00 | NPP-375D | BACABAL | MARANHÃO | Brasil | 2101202 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 532ab4a2-7b59-3320-9239-50a9f3be0a0d | -3.11852 | -53.80957 | 2024-12-02 04:25:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 0cd7ed83-92de-3e71-be40-d47a4759fd02 | -3.05526 | -51.06344 | 2024-12-02 04:25:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 3b5e47ff-6e73-3fc6-9a91-34697f55a314 | -4.30746 | -48.21329 | 2024-12-02 04:25:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 85f1561c-d005-324d-844a-1908e85c21e2 | -3.88961 | -46.68647 | 2024-12-02 04:25:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 3624717c-54b0-3357-bee6-ccf33583bee6 | -3.25727 | -53.62085 | 2024-12-02 04:25:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 1ffb8afc-c6f4-36f5-b0eb-1c399cb9ea43 | -3.98788 | -46.65144 | 2024-12-02 04:25:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 2.7 |
| b4b616ff-9875-3a64-a694-74c66dd07ab6 | -3.93191 | -46.91837 | 2024-12-02 04:25:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 2853c7ab-6b45-3f06-a1ea-390b9eb70d29 | -3.96689 | -48.19841 | 2024-12-02 04:25:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 5e23d496-093b-321b-83d1-7c948232484a | -11.13029 | -37.21505 | 2024-12-02 04:25:00 | NPP-375D | ITAPORANGA D'AJUDA | SERGIPE | Brasil | 2803203 | 28 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| a775098a-6302-3407-8f5d-76efc6a22e8d | -4.42966 | -46.29441 | 2024-12-02 04:25:00 | NPP-375D | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 28235502-ccb6-334b-b332-2da6c46d308d | -2.89968 | -54.16245 | 2024-12-02 04:25:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 83be7f4f-255a-343f-a33b-06bf9e4bb53e | -3.65521 | -51.11777 | 2024-12-02 04:25:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| baaf9941-b4a9-360f-9550-b34d07a61026 | -4.13941 | -46.93221 | 2024-12-02 04:25:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| bf6bada7-44ab-3db5-879b-717659e5d2b1 | -4.09414 | -44.85335 | 2024-12-02 04:25:00 | NPP-375D | LAGO VERDE | MARANHÃO | Brasil | 2105906 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 0ef65d1e-1c8e-37ae-a1ff-dd44b1b27b89 | -4.111 | -46.76445 | 2024-12-02 04:25:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 0.5 |
| f156a552-23dd-3a47-ad74-f3888de7d735 | -3.85696 | -46.5331 | 2024-12-02 04:25:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 3.5 |
| e8f02a60-47b2-393d-9c18-61ac6ab7464a | -4.04366 | -46.82996 | 2024-12-02 04:25:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |
| d6e5e002-49c7-3983-a0b7-e070eb01ad39 | -3.74014 | -51.83159 | 2024-12-02 04:25:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 1be1f8ff-ccbb-3eb6-b9f0-40362173cefe | -2.89393 | -54.16479 | 2024-12-02 04:25:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| e34bbc84-5aa5-33d3-aad8-35991f29ff9f | -4.76763 | -46.42602 | 2024-12-02 04:25:00 | NPP-375D | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 6bc070fd-6662-3523-a969-cd2d3983e846 | -3.25541 | -53.63208 | 2024-12-02 04:25:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| fc7e2aa7-5ba7-3f1d-9337-23416577fc6e | 1.88188 | -55.70747 | 2024-12-02 04:25:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 8020f5d0-f7e8-34a4-a8e5-20aecab12ca8 | -3.95369 | -46.30568 | 2024-12-02 04:25:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 8700fdfd-17b8-3cdd-a43f-ac0ec2bda37f | -3.46773 | -53.49454 | 2024-12-02 04:25:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 8ce4fb52-cee0-39f6-85cc-c3c129d548ff | -4.91781 | -41.33499 | 2024-12-02 04:25:00 | NPP-375D | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 2.8 |
| 69c30b36-f9fb-3594-a181-5795a7f222f1 | -3.32027 | -50.03038 | 2024-12-02 04:25:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 9c85f9ed-4a68-3e85-9fe6-da6dd2dc630a | -3.71817 | -51.79942 | 2024-12-02 04:25:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 5425677d-02b2-38f9-9909-b9f16e016e76 | -3.45838 | -51.41792 | 2024-12-02 04:25:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ecf2fd9e-e79b-31e1-93e0-4a674215cfae | -3.78545 | -46.70216 | 2024-12-02 04:25:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f7bf0acc-cedc-30b1-9a7e-06b11a3c68a1 | -4.0487 | -46.81986 | 2024-12-02 04:25:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 2.6 |
| e94ee217-a1d3-3659-8db8-c87086d5586e | -3.76713 | -50.66248 | 2024-12-02 04:25:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 92de20ec-f35d-343a-b425-f0179bcb2ba8 | -4.31992 | -48.09244 | 2024-12-02 04:25:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| efb9dffc-7291-3ab4-bf74-357a14bb184f | -2.98297 | -53.88664 | 2024-12-02 04:25:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f8f7a993-5f70-3e75-8cf1-c16deed247ef | -3.3607 | -49.10394 | 2024-12-02 04:25:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b9db78dc-0597-30a2-92c6-8e26cde1ec3f | -4.63484 | -45.46213 | 2024-12-02 04:25:00 | NPP-375D | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Cerrado | 10.5 |
| 4655cc89-2637-39cd-bf29-a4668aba383d | -3.25077 | -50.61924 | 2024-12-02 04:25:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 6b488e66-8d23-3c56-ae20-590d1b271f73 | -3.49617 | -53.84089 | 2024-12-02 04:25:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| be0695c4-805f-3b54-a1a6-f66667a6d3ff | -5.12254 | -43.20916 | 2024-12-02 04:25:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 34.4 |
| d959ed4b-207e-3932-864a-943aa40e3e18 | -2.65915 | -54.08904 | 2024-12-02 04:25:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 9c9c7d21-fdf4-3f0d-b26c-68a2e4bdc42b | -3.391 | -51.14787 | 2024-12-02 04:25:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| eb25b27e-8691-37f8-8b3a-0d948ee591bd | -4.56122 | -45.71955 | 2024-12-02 04:25:00 | NPP-375D | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 560281c8-1a85-3ae7-8266-7b94e9f871be | -4.03974 | -46.83297 | 2024-12-02 04:25:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 24731e42-0e56-33c9-a0d2-3854ed3470e8 | -4.9036 | -41.32268 | 2024-12-02 04:25:00 | NPP-375D | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| c6dc7720-122c-3930-8c19-9d8ac2470ba7 | -3.48487 | -52.09796 | 2024-12-02 04:25:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| cd69214f-febe-3cde-9981-5620e3e2cc38 | -3.7429 | -52.26111 | 2024-12-02 04:25:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 16f5b3e8-bd4a-318b-9047-691540f4d48d | -2.63024 | -53.35916 | 2024-12-02 04:25:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 117e317e-499b-326d-8c1d-50ee4952c9c3 | -3.02483 | -51.53511 | 2024-12-02 04:25:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| c0aac29b-5c00-3d2c-9da5-9ba1073d709f | -3.97002 | -46.65583 | 2024-12-02 04:25:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 0f93e168-6dbb-36f1-90e3-0afb93e7065c | -4.01318 | -47.00038 | 2024-12-02 04:25:00 | NPP-375D | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 306f74ec-9590-3bbc-8f60-c92a17cb03ee | -4.58082 | -43.35701 | 2024-12-02 04:25:00 | NPP-375D | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 8.8 |
| b93df54b-9fc8-37d6-9440-d6cb85a81aa8 | -10.49965 | -44.91294 | 2024-12-02 04:25:00 | NPP-375D | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 5effe6e2-d0fa-31c1-9101-1eb058f0676b | -4.11293 | -50.50022 | 2024-12-02 04:25:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 087082a1-550d-3297-ab1e-7f7ae074316b | -4.90912 | -41.33923 | 2024-12-02 04:25:00 | NPP-375D | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 3.3 |
| 799120b7-48af-349b-be2e-84f014237218 | -2.74706 | -51.75481 | 2024-12-02 04:25:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 35f812b7-5800-3e8f-a313-9335409fa560 | -4.27834 | -50.68506 | 2024-12-02 04:25:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| cf28e878-4917-30b7-a63d-d918cf63789f | -2.37575 | -53.66189 | 2024-12-02 04:25:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| a6c37593-f534-3234-90af-98d530e3ff13 | -3.94412 | -48.1829 | 2024-12-02 04:25:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| d52750f2-2a7d-3c1d-af04-a0e2dababd41 | -4.08461 | -46.20493 | 2024-12-02 04:25:00 | NPP-375D | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 0.3 |
| d03c3f25-5c44-3d6b-aaa2-7562aea65729 | -4.32689 | -48.09359 | 2024-12-02 04:25:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 27e7c7cc-3871-3528-910d-b76eb38b6f0f | -4.59533 | -50.60489 | 2024-12-02 04:25:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| f8cf1ea3-c60b-395a-a01d-87e35f99219a | -3.79721 | -46.6931 | 2024-12-02 04:25:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| bc482b5e-0e88-3c00-8e1f-df7539254c3a | -4.31518 | -48.09246 | 2024-12-02 04:25:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 4b52b184-935b-311a-a8de-6951712dfcb7 | -3.50171 | -53.83885 | 2024-12-02 04:25:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| c7aeed3c-1e7f-38ed-898c-fe45856777a5 | -3.93429 | -46.70793 | 2024-12-02 04:25:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| f0a6aebf-ecb7-3595-aca0-502660b0e855 | -4.07275 | -47.0904 | 2024-12-02 04:25:00 | NPP-375D | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |


[Clique aqui para ver as próximas entradas](README39.md)
