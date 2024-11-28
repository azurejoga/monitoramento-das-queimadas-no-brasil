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
| 0d23c6e2-8775-3dbb-9824-d0fce471eceb | -4.7706 | -44.4025 | 2024-11-28 00:38:00 | METOP-B | SANTO ANTÔNIO DOS LOPES | MARANHÃO | Brasil | 2110302 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| fdd0d483-c3ed-3c6d-a75b-c0b1596975f4 | -2.9327 | -51.4417 | 2024-11-28 00:38:00 | METOP-B | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 54369e9c-aceb-3998-a757-394560f7e431 | -2.358 | -54.372799 | 2024-11-28 00:38:00 | METOP-B | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ca70cf3a-6404-3c87-a9e1-c0da9f882ec9 | -3.255 | -48.887402 | 2024-11-28 00:38:00 | METOP-B | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ecb37568-4097-30a1-8dea-03a434b58012 | -3.3205 | -50.024399 | 2024-11-28 00:38:00 | METOP-B | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a5ca28a1-406d-3d00-9de4-b0eef0c7c520 | -2.0215 | -51.196098 | 2024-11-28 00:38:00 | METOP-B | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b4bedfc8-1642-3ef4-a270-dd508e19252d | -2.1908 | -53.766899 | 2024-11-28 00:38:00 | METOP-B | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 59a3f8b1-fa62-3a03-be23-6017dcccdad7 | -3.6027 | -50.356998 | 2024-11-28 00:38:00 | METOP-B | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 446cd4c1-25d3-3053-bf9e-47b4d2ae1305 | -4.6656 | -49.509499 | 2024-11-28 00:38:00 | METOP-B | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 3c90a74f-3ed5-3669-a683-07123771d8b0 | -3.1084 | -53.815498 | 2024-11-28 00:38:00 | METOP-B | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 41ea1485-7482-3ad2-9a76-d9bd21ea237b | -2.6373 | -54.056801 | 2024-11-28 00:38:00 | METOP-B | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e10e8b4b-ac03-32a6-a833-7dfc6735fa90 | -3.5386 | -50.7528 | 2024-11-28 00:38:00 | METOP-B | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 3c3bbfbf-26c8-342a-8a9d-9ddd2e6a9259 | -2.0049 | -51.168301 | 2024-11-28 00:38:00 | METOP-B | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a70d23fa-9ca5-3f78-917a-26bd40ebba5d | -2.0566 | -47.126598 | 2024-11-28 00:38:00 | METOP-B | GARRAFÃO DO NORTE | PARÁ | Brasil | 1503077 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 48e2abdb-ba0b-307a-acf9-5c5c27bb4fe4 | -3.174 | -48.5812 | 2024-11-28 00:38:00 | METOP-B | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a12817fd-b8fa-3aa2-9bde-e5487ebaf698 | -2.0536 | -47.113899 | 2024-11-28 00:38:00 | METOP-B | GARRAFÃO DO NORTE | PARÁ | Brasil | 1503077 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 7d237464-34c8-31a8-870a-46baa780c918 | -2.8826 | -54.002602 | 2024-11-28 00:38:00 | METOP-B | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 2660ef88-3a15-398a-a510-25ac856cf80e | -18.7997 | -55.821899 | 2024-11-28 00:38:00 | METOP-B | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| d77135ba-6f40-39fc-bdf8-f50a25abc798 | -2.1677 | -53.435902 | 2024-11-28 00:38:00 | METOP-B | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b7b2e6cc-9f95-3b2c-9f14-3a7ab6d26772 | -2.83 | -54.043201 | 2024-11-28 00:38:00 | METOP-B | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 63dea455-a98f-3460-aa96-5c0f5d5be68a | -21.1 | -49.805401 | 2024-11-28 00:38:00 | METOP-B | JOSÉ BONIFÁCIO | SÃO PAULO | Brasil | 3525706 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 47bb60cf-55ee-3b07-8c49-1f8260962c2e | -3.3967 | -50.312199 | 2024-11-28 00:38:00 | METOP-B | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| bd4cd012-6037-3ca7-ab67-454122463d56 | -3.1107 | -50.368401 | 2024-11-28 00:38:00 | METOP-B | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0ded62ea-d2f0-3043-957f-7f5a1b9fd5bb | -4.1484 | -43.817799 | 2024-11-28 00:38:00 | METOP-B | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| e282227c-cba0-3adb-9fe9-1a89ff0f5d35 | -5.4313 | -47.9249 | 2024-11-28 00:38:00 | METOP-B | AUGUSTINÓPOLIS | TOCANTINS | Brasil | 1702554 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 43bd91b2-d915-313c-8310-95ec47abdd16 | -3.9764 | -48.089901 | 2024-11-28 00:38:00 | METOP-B | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 332f2682-e17e-3428-91e2-cc302148628e | -3.6537 | -51.394001 | 2024-11-28 00:38:00 | METOP-B | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e3de9747-9e3f-3278-9a0d-ce6670a4413f | -2.7494 | -54.097301 | 2024-11-28 00:38:00 | METOP-B | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| eb535133-6969-375f-9c93-65c84b7f1ef8 | -2.2613 | -53.622398 | 2024-11-28 00:38:00 | METOP-B | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 745526f7-7a40-3524-b73d-6ad0cba40107 | -2.8176 | -54.125702 | 2024-11-28 00:38:00 | METOP-B | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 902dae3b-e1ea-3fd3-b02b-e6b9ef882fba | -3.076 | -54.405201 | 2024-11-28 00:38:00 | METOP-B | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| bcd41fa9-9dfd-3bed-9029-d0eec8bfac51 | -2.2678 | -53.742699 | 2024-11-28 00:38:00 | METOP-B | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 92622b6c-c20d-3d4d-8f50-e41e845cc847 | -21.180599 | -48.696701 | 2024-11-28 00:38:00 | METOP-B | VISTA ALEGRE DO ALTO | SÃO PAULO | Brasil | 3556909 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 53884d4e-c75a-37fb-9f02-2e8d60350c94 | -2.0164 | -51.173599 | 2024-11-28 00:38:00 | METOP-B | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 40a7c2f2-06f5-3309-bf38-59a879f7b685 | -2.4641 | -53.699299 | 2024-11-28 00:38:00 | METOP-B | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 7dfc27ef-a7d2-3463-ad45-e7618a2852b9 | -3.0928 | -53.288101 | 2024-11-28 00:38:00 | METOP-B | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d6e5218c-ae60-3296-b0c4-69dfd67d6271 | -3.0619 | -54.020901 | 2024-11-28 00:38:00 | METOP-B | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 8c7ab954-596c-30b5-b972-ddb7ef1639eb | -3.2507 | -54.219799 | 2024-11-28 00:38:00 | METOP-B | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 8ce83c88-9a98-3434-b887-5118d240fcc6 | -3.2997 | -51.152 | 2024-11-28 00:38:00 | METOP-B | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f354bb33-e8b7-3e9f-83a2-f4a221225f94 | -2.8936 | -51.587002 | 2024-11-28 00:38:00 | METOP-B | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 50ca3776-f444-38f1-9fbb-2174d9eda976 | -2.4452 | -53.890099 | 2024-11-28 00:38:00 | METOP-B | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ca2e07aa-89fb-39ba-bd14-b515704eeed8 | -3.1719 | -53.227699 | 2024-11-28 00:38:00 | METOP-B | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 17ffb3a9-7c32-31f7-a149-98a857f75551 | -2.4518 | -50.4161 | 2024-11-28 00:38:00 | METOP-B | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 91640fda-935b-30df-8229-e21a597c462b | -2.8718 | -53.954399 | 2024-11-28 00:38:00 | METOP-B | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 35b70c2b-a65b-3632-81f8-8f31ba3c16cf | -2.8093 | -53.0364 | 2024-11-28 00:38:00 | METOP-B | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 4dc54a90-9ab6-36d8-9aee-59ef88a37333 | -2.8099 | -46.8326 | 2024-11-28 00:38:00 | METOP-B | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 467404db-6f16-3dd1-91bc-fe89af6a280f | -3.4786 | -51.621399 | 2024-11-28 00:38:00 | METOP-B | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e6085c78-435e-3a80-b342-b1bba227f819 | -3.3821 | -50.1133 | 2024-11-28 00:38:00 | METOP-B | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 590db002-5821-3647-aec7-97b530ac70bc | -2.9524 | -51.573799 | 2024-11-28 00:38:00 | METOP-B | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 72e98b39-2acc-35fc-873f-3db5645be55a | -2.6316 | -53.985802 | 2024-11-28 00:38:00 | METOP-B | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e77175d4-bcc9-38f7-b3e8-5076e0d3da8f | -3.2764 | -54.1045 | 2024-11-28 00:38:00 | METOP-B | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 6fc6f316-762d-3f7b-97a2-663bac2d5d51 | -2.0181 | -51.181099 | 2024-11-28 00:38:00 | METOP-B | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e023262b-194e-3ecc-a8f1-d507f5da433f | -3.0912 | -53.2813 | 2024-11-28 00:38:00 | METOP-B | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 1f6032cc-224c-3737-8f22-1d7aa725563a | -3.5334 | -50.189201 | 2024-11-28 00:38:00 | METOP-B | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0cc57927-b02d-397a-9cc9-14310b7f1154 | -3.695 | -50.219799 | 2024-11-28 00:38:00 | METOP-B | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 3e94b634-4f94-3ccd-9c24-bbc36e149d06 | -4.6694 | -49.526299 | 2024-11-28 00:38:00 | METOP-B | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e574ef9f-8767-384d-acd7-9708a250c06e | -2.5541 | -54.053501 | 2024-11-28 00:38:00 | METOP-B | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e288ccbe-b5f5-34d1-989f-8a4aab51b206 | -2.7077 | -51.994301 | 2024-11-28 00:38:00 | METOP-B | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0a954b4e-f8a6-34de-9aed-58933f231917 | -3.5353 | -51.1455 | 2024-11-28 00:38:00 | METOP-B | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 7a6d3fe4-a565-342b-b8bb-ab5d9272d158 | -3.5101 | -50.493 | 2024-11-28 00:38:00 | METOP-B | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f9b6ecec-ff2a-36bf-9311-4758cdc4d3ec | -1.8845 | -50.5938 | 2024-11-28 00:38:00 | METOP-B | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 27195dec-985b-3f7b-8626-875848283455 | -2.6351 | -51.764999 | 2024-11-28 00:38:00 | METOP-B | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c2c60a94-ffd5-3107-acb3-e78040883efd | -2.9803 | -53.8871 | 2024-11-28 00:38:00 | METOP-B | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b04f1272-ed1b-384d-8eeb-7322c16ee34f | -2.9028 | -53.9548 | 2024-11-28 00:38:00 | METOP-B | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c70fc15b-0d7c-3b39-bf00-2039ce3d5379 | -2.8682 | -53.9841 | 2024-11-28 00:38:00 | METOP-B | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 92b71c32-7960-3354-a7f7-5dd4fb772129 | -2.3256 | -51.945999 | 2024-11-28 00:38:00 | METOP-B | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ae2fdcfa-a099-3516-883c-5123a6372e04 | -3.5149 | -53.7906 | 2024-11-28 00:38:00 | METOP-B | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 619d4345-78f2-358c-8b90-3433107bd81c | -3.9308 | -53.6698 | 2024-11-28 00:38:00 | METOP-B | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| af915fae-5dea-36ed-9b88-88cc101c329d | -2.8284 | -54.036301 | 2024-11-28 00:38:00 | METOP-B | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a4fe55e9-fb11-3b3a-a6eb-42808d445ed2 | -3.2579 | -50.6068 | 2024-11-28 00:38:00 | METOP-B | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c3412d8c-aca8-3b31-84c4-ee73797d811f | -3.7048 | -50.217602 | 2024-11-28 00:38:00 | METOP-B | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 01bc3c0b-cd8e-33c5-82da-097e28d03ffd | -2.7905 | -52.8615 | 2024-11-28 00:38:00 | METOP-B | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 9be6eee4-012e-3685-866d-b30342c4f4da | -3.3802 | -50.105202 | 2024-11-28 00:38:00 | METOP-B | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f962ffdd-73bd-3b23-8e03-f4cca6e1dc63 | -2.2582 | -53.608799 | 2024-11-28 00:38:00 | METOP-B | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 12371fe3-b9f9-3903-bae1-0e90158c60ff | -4.6711 | -44.628799 | 2024-11-28 00:38:00 | METOP-B | BERNARDO DO MEARIM | MARANHÃO | Brasil | 2101939 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 1e2366b0-38ce-39a1-9cfe-5534ca545933 | -3.5875 | -50.335602 | 2024-11-28 00:38:00 | METOP-B | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 5b668f78-a7ba-379a-803a-f1a442ccf26f | -3.0552 | -54.036999 | 2024-11-28 00:38:00 | METOP-B | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 7f1f007b-3200-3fd4-a8e4-a6bbe7a8f08c | -3.1161 | -53.987202 | 2024-11-28 00:38:00 | METOP-B | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 9d53b09a-704f-3617-9e91-c76561bd08fe | -2.8811 | -53.995701 | 2024-11-28 00:38:00 | METOP-B | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f2237a04-6f98-3eaa-a1c3-5c9a94e14117 | -2.8149 | -54.068199 | 2024-11-28 00:38:00 | METOP-B | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 2b62c796-bdf9-3ccf-a539-dbf139ff3e00 | -3.3788 | -50.820599 | 2024-11-28 00:38:00 | METOP-B | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a6e3994d-091a-353f-90e7-ef678f01d792 | -2.6063 | -54.0564 | 2024-11-28 00:38:00 | METOP-B | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f13da7cc-43d3-3669-a57e-b7065cf74ac9 | -4.0588 | -50.864601 | 2024-11-28 00:38:00 | METOP-B | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a63764c6-0de5-34ab-8a77-79faacde7371 | -3.2554 | -50.7766 | 2024-11-28 00:38:00 | METOP-B | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| deed8e84-ff1e-379b-b5bf-44f23ef99ddd | -3.3839 | -50.121399 | 2024-11-28 00:38:00 | METOP-B | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 9cde3211-f457-3766-ac8c-a4113c99e7a7 | -3.0558 | -53.719101 | 2024-11-28 00:38:00 | METOP-B | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0828bb57-fc32-3f32-95ae-f1236f8cad23 | -2.9047 | -51.3638 | 2024-11-28 00:38:00 | METOP-B | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| dacdde87-0495-364d-8e79-1238cfa6dc16 | -3.4226 | -50.155102 | 2024-11-28 00:38:00 | METOP-B | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 72c7852b-855d-35bf-83ae-d867064a1649 | -3.4464 | -50.124298 | 2024-11-28 00:38:00 | METOP-B | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| aadab0bc-65a5-32da-9c93-87cfe7de91de | -3.2492 | -54.212799 | 2024-11-28 00:38:00 | METOP-B | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 29d5e665-03e2-3e36-af5a-1a10deca3030 | -2.9948 | -51.443001 | 2024-11-28 00:38:00 | METOP-B | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d2423bf0-4b71-3eb0-8386-10d60864686d | -2.8925 | -54.000401 | 2024-11-28 00:38:00 | METOP-B | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 3ff1aa94-194f-3534-a784-79f94f60c894 | -2.7644 | -54.072102 | 2024-11-28 00:38:00 | METOP-B | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c0db53db-bfc6-3133-8af3-6816458b878e | -3.6905 | -50.8769 | 2024-11-28 00:38:00 | METOP-B | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 1889fbf6-a1b1-39a1-a556-1464042498ea | -2.8489 | -51.8442 | 2024-11-28 00:38:00 | METOP-B | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 1ef064ea-8e3c-39ad-8016-cfdbef79d05a | -2.6553 | -49.503899 | 2024-11-28 00:38:00 | METOP-B | MOCAJUBA | PARÁ | Brasil | 1504604 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d62a54b0-6d90-350f-9f14-13ae7d8ded0a | -3.0973 | -50.354698 | 2024-11-28 00:38:00 | METOP-B | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 7cd5f591-d394-3a00-bb61-05edaf829be2 | -2.8378 | -54.077801 | 2024-11-28 00:38:00 | METOP-B | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 60afb1b6-fbad-33e8-85e5-6f5d7166ea02 | -3.3937 | -50.119202 | 2024-11-28 00:38:00 | METOP-B | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ae343381-9c9f-3176-a721-70cbea4e2fc8 | -4.038 | -46.548 | 2024-11-28 00:38:00 | METOP-B | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | nan |


[Clique aqui para ver as próximas entradas](README10.md)
