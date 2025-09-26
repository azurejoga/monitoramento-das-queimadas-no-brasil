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

## Dados Diários - Página 18

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 3f9bbffd-5ea5-3788-9204-c7580b0acc4e | -5.72849 | -44.97618 | 2025-09-26 04:14:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 35c79f07-25de-3ca8-bdd5-ce31b1370ff1 | -4.7924 | -42.82063 | 2025-09-26 04:14:00 | NOAA-21 | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Cerrado | 38.5 |
| e7baf3ec-71f0-30d6-ad3d-ad872d2f3b32 | -3.33771 | -50.20395 | 2025-09-26 04:14:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| b14b7568-df43-32a0-b200-2c04c186a909 | -8.72735 | -45.42605 | 2025-09-26 04:14:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| a1e7f735-5203-3d58-9ae9-1c43d9432f88 | -7.45943 | -41.91518 | 2025-09-26 04:14:00 | NOAA-21 | SANTO INÁCIO DO PIAUÍ | PIAUÍ | Brasil | 2209500 | 22 | 33 | nan | nan | nan | Caatinga | 3.7 |
| 086ae2f3-fd4c-3347-b642-f9ce657772a4 | -5.74096 | -44.98579 | 2025-09-26 04:14:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 9f5243f3-0789-35bd-ac54-bdb1599a2b99 | -6.25603 | -42.48963 | 2025-09-26 04:14:00 | NOAA-21 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 3.9 |
| a061735b-ade0-37ce-9277-2333b45717be | -5.63011 | -43.91991 | 2025-09-26 04:14:00 | NOAA-21 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 4.4 |
| eb4b82ef-b10e-3842-9a40-592df877c97a | -9.93672 | -47.44852 | 2025-09-26 04:14:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 2baeb190-7744-32ce-a5d1-2027993c109b | -5.74449 | -44.96349 | 2025-09-26 04:14:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 19.7 |
| 6bc6830f-f0b3-3595-af4d-0275f7cf2381 | -4.40171 | -44.08744 | 2025-09-26 04:14:00 | NOAA-21 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| d7d4184a-12d9-3fc0-b97d-e2f7dbcb67c1 | -10.39749 | -46.14205 | 2025-09-26 04:14:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 5.4 |
| f7d107e2-a3ca-3622-8156-37ffac05eaf0 | -7.13003 | -44.8274 | 2025-09-26 04:14:00 | NOAA-21 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 5b7b15b4-d4cd-3fda-927d-39f457f05d46 | -3.81715 | -50.79558 | 2025-09-26 04:14:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| aba5f474-1c34-31ec-935a-722d3e28de49 | -5.80549 | -42.80436 | 2025-09-26 04:14:00 | NOAA-21 | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 4.6 |
| 13991f18-6c48-3762-bcf9-bc8ba09d14ba | -10.40344 | -46.17018 | 2025-09-26 04:14:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| b5413c74-384f-31fb-b586-5e2d51c16da3 | -7.17667 | -42.23028 | 2025-09-26 04:14:00 | NOAA-21 | COLÔNIA DO PIAUÍ | PIAUÍ | Brasil | 2202778 | 22 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 845a16e0-a353-322e-b36d-8874726f5379 | -5.73354 | -44.98843 | 2025-09-26 04:14:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 6fdd4df6-43c1-32fd-a6dc-aa8be601ad7b | -7.31278 | -45.76646 | 2025-09-26 04:14:00 | NOAA-21 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| c9c4bd7d-a04a-39bb-8315-8a9c70ce58c8 | -10.93358 | -44.28222 | 2025-09-26 04:14:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 03e79abc-4af9-30fb-aaec-4d87c2534b25 | -6.59546 | -41.91922 | 2025-09-26 04:14:00 | NOAA-21 | NOVO ORIENTE DO PIAUÍ | PIAUÍ | Brasil | 2206902 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 7d725e61-230c-32b9-8e90-92b237fb507b | -7.31118 | -45.75436 | 2025-09-26 04:14:00 | NOAA-21 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 0ffdef2c-0c5b-3770-8899-8da32609487a | -5.63564 | -43.92795 | 2025-09-26 04:14:00 | NOAA-21 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 9.3 |
| 8b0936a7-9913-347f-a085-c406826c7a64 | -9.98215 | -49.24905 | 2025-09-26 04:14:00 | NOAA-21 | MONTE SANTO DO TOCANTINS | TOCANTINS | Brasil | 1713700 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 21023cdc-b126-3867-907b-83c4c53c9052 | -8.67154 | -43.99591 | 2025-09-26 04:14:00 | NOAA-21 | CRISTINO CASTRO | PIAUÍ | Brasil | 2203107 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 3c393161-fb8f-35f2-b036-d5ecff25ca22 | -7.05659 | -46.4229 | 2025-09-26 04:14:00 | NOAA-21 | NOVA COLINAS | MARANHÃO | Brasil | 2107258 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| cee2975d-c5c5-35db-91fa-72c6998475c2 | -9.76154 | -48.34558 | 2025-09-26 04:14:00 | NOAA-21 | LAJEADO | TOCANTINS | Brasil | 1712009 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 906c7482-d14a-3a9c-9f06-0080b60719d0 | -5.46403 | -43.07101 | 2025-09-26 04:14:00 | NOAA-21 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 27.7 |
| 7568c651-4293-3f39-8d9c-6ca0c7550cf8 | -5.9653 | -43.67371 | 2025-09-26 04:14:00 | NOAA-21 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 911b6261-0539-3f8c-a2e7-4f34d6630fe0 | -8.4982 | -49.54609 | 2025-09-26 04:14:00 | NOAA-21 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 3e815197-25ec-3f1e-900c-84ba012f5381 | -5.73072 | -44.98415 | 2025-09-26 04:14:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 804c7808-d109-3fa9-8178-03243c8c3656 | -7.27543 | -42.97989 | 2025-09-26 04:14:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| a944a0f8-8f38-3b5c-bcc1-ab89a8edf087 | -5.42597 | -41.32489 | 2025-09-26 04:14:00 | NOAA-21 | CASTELO DO PIAUÍ | PIAUÍ | Brasil | 2202604 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| fcfac443-453a-3e9f-91b6-d0f869a4abc4 | -3.80703 | -47.58558 | 2025-09-26 04:14:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| fcb887a3-0a02-31b2-8db0-609c00d85b43 | -9.80003 | -45.7317 | 2025-09-26 04:14:00 | NOAA-21 | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 24ed4f9b-d4c0-37aa-85ec-f457da4cd18d | -3.81677 | -50.79403 | 2025-09-26 04:14:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| d3492655-e553-3886-9912-f97a78cc936e | -5.72284 | -44.9677 | 2025-09-26 04:14:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 4d377344-dbee-3809-b728-4336272f3ea3 | -5.72671 | -44.98735 | 2025-09-26 04:14:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| fa6198e3-95a3-3cee-abff-c9ab0b6ea43a | -5.73767 | -44.96241 | 2025-09-26 04:14:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 60.1 |
| d7b872a2-9f7b-3956-b06e-45ed6ef8c983 | -6.59827 | -41.92325 | 2025-09-26 04:14:00 | NOAA-21 | NOVO ORIENTE DO PIAUÍ | PIAUÍ | Brasil | 2206902 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 3729e0e8-aae2-38a4-9f03-a59ce7e8a341 | -8.14032 | -42.37548 | 2025-09-26 04:14:00 | NOAA-21 | PEDRO LAURENTINO | PIAUÍ | Brasil | 2207934 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| d320ab71-065a-3ebe-87bb-ef1af747781a | -7.10055 | -44.09366 | 2025-09-26 04:14:00 | NOAA-21 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| e0f7520c-9df5-3780-9a0f-782e4f28bb55 | -7.1153 | -43.73954 | 2025-09-26 04:14:00 | NOAA-21 | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 12906192-ed46-36cd-b291-768d22b77431 | -5.37472 | -42.29124 | 2025-09-26 04:14:00 | NOAA-21 | ALTO LONGÁ | PIAUÍ | Brasil | 2200301 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| c1bf2874-b920-37f6-8247-01c556b98fcb | -10.57247 | -46.27529 | 2025-09-26 04:14:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 82f64d7a-727e-345b-8bd6-2d1fdf4b1376 | -3.63314 | -43.87182 | 2025-09-26 04:14:00 | NOAA-21 | VARGEM GRANDE | MARANHÃO | Brasil | 2112704 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| be3ddffa-bf57-3c0d-aeae-0fe167ea54db | -5.78922 | -42.86526 | 2025-09-26 04:14:00 | NOAA-21 | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 2c49e779-bf7c-3fbd-9073-b2a0f5b0a678 | -10.93854 | -44.29374 | 2025-09-26 04:14:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 271438dd-30cc-3086-a1d6-47c53b982c34 | -6.62062 | -46.13936 | 2025-09-26 04:14:00 | NOAA-21 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 8cab9d44-985b-32c3-81e2-63bceb563689 | -5.79398 | -42.81316 | 2025-09-26 04:14:00 | NOAA-21 | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 5a3fe931-475d-32ad-a0c5-2c106779cfce | -3.68507 | -52.38659 | 2025-09-26 04:14:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| b44dc36c-0d56-3554-be4a-db9739437b00 | -6.82594 | -44.17159 | 2025-09-26 04:14:00 | NOAA-21 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| f73795ed-590e-3529-8acb-2125ee276bbb | -6.59881 | -41.91969 | 2025-09-26 04:14:00 | NOAA-21 | NOVO ORIENTE DO PIAUÍ | PIAUÍ | Brasil | 2206902 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| c3c808f4-46ca-3f7d-b565-b58f0242b695 | -5.53535 | -43.87288 | 2025-09-26 04:14:00 | NOAA-21 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 50574cbb-60a9-3e20-9af1-a2bc9dd283f1 | -10.17563 | -44.83707 | 2025-09-26 04:14:00 | NOAA-21 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 5d4f1661-d713-36d7-8184-aa8c6531b85f | -6.13913 | -44.87088 | 2025-09-26 04:14:00 | NOAA-21 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 410e6beb-7395-3511-820e-a92e53820708 | -5.56329 | -44.38362 | 2025-09-26 04:14:00 | NOAA-21 | SÃO DOMINGOS DO MARANHÃO | MARANHÃO | Brasil | 2110708 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 6b085ac9-26e2-38ca-b252-1e48333c2fe6 | -6.07175 | -44.07643 | 2025-09-26 04:14:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 6.2 |
| ab2d5e2b-fe0c-3b50-9c50-55b235350437 | -5.08257 | -41.18719 | 2025-09-26 04:14:00 | NOAA-21 | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 6b002ed9-20f7-3f39-923d-2a97acb5c104 | -9.03366 | -45.53195 | 2025-09-26 04:14:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 3e6bf141-0d17-3f48-8872-8b685d3a01f9 | -5.30157 | -42.76042 | 2025-09-26 04:14:00 | NOAA-21 | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 5484f9bc-7eca-34f1-99ec-a6a06d5dc760 | -5.20387 | -43.73098 | 2025-09-26 04:14:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| dab93196-4bc4-30e4-9832-606ce3e52560 | -10.19497 | -44.84378 | 2025-09-26 04:14:00 | NOAA-21 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 529844a8-4b09-30ac-8fdf-1600be26ee54 | -5.77288 | -42.90498 | 2025-09-26 04:14:00 | NOAA-21 | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 9a942200-d360-3357-b13b-435776cc3f82 | -2.92226 | -48.31026 | 2025-09-26 04:14:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| c9b05046-ab68-38e8-9f9e-26ed0a2c6243 | -14.75715 | -48.35048 | 2025-09-26 04:17:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 39101216-069a-3e46-a32a-738ebdcace00 | -11.25097 | -45.54191 | 2025-09-26 04:17:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 14.7 |
| dcc2c9f5-92ab-3c81-b03c-0d8b1e1b5649 | -11.24472 | -45.55936 | 2025-09-26 04:17:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 67878eec-7ad4-3c10-a9fc-5d9bf80ccdb4 | -12.38677 | -44.14711 | 2025-09-26 04:17:00 | NOAA-21 | TABOCAS DO BREJO VELHO | BAHIA | Brasil | 2930907 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 0c4b6487-34ce-358a-9134-f688bf3a9b83 | -22.20038 | -54.8401 | 2025-09-26 04:17:00 | NOAA-21 | DOURADOS | MATO GROSSO DO SUL | Brasil | 5003702 | 50 | 33 | nan | nan | nan | Mata Atlântica | 2.8 |
| 80f5f4d8-3f96-35e6-b498-58122046ed60 | -12.06717 | -47.98558 | 2025-09-26 04:17:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 4c21a900-e79a-3977-9e8b-bdbbdebc947e | -12.87611 | -44.69484 | 2025-09-26 04:17:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| a658bb3c-dccd-3fe5-a99b-45cace3561e2 | -17.87249 | -48.78151 | 2025-09-26 04:17:00 | NOAA-21 | RIO QUENTE | GOIÁS | Brasil | 5218789 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 6499297b-b8ff-3e84-bda8-0ba2ca07f61e | -12.73632 | -46.82404 | 2025-09-26 04:17:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| ebf05556-4201-339d-b608-6fe337cbd002 | -11.23411 | -45.56131 | 2025-09-26 04:17:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 83d44986-981e-317f-9b8a-25ef4a6ef639 | -15.88027 | -59.33848 | 2025-09-26 04:17:00 | NOAA-21 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| d36344c8-1df4-36aa-b388-79fc0be2a931 | -12.148 | -47.95351 | 2025-09-26 04:17:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 286a3831-6da7-385d-9a85-ca2797bf5f53 | -12.73584 | -47.07867 | 2025-09-26 04:17:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 37be3773-33ba-3584-9b16-d2b8d72f2e5d | -15.01502 | -49.54041 | 2025-09-26 04:17:00 | NOAA-21 | NOVA GLÓRIA | GOIÁS | Brasil | 5214861 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 7d56bca9-b5d1-34ff-b794-389ea3f1f73a | -20.60685 | -56.73388 | 2025-09-26 04:17:00 | NOAA-21 | BODOQUENA | MATO GROSSO DO SUL | Brasil | 5002159 | 50 | 33 | nan | nan | nan | Cerrado | 7.2 |
| eafb2071-741d-3cf5-8cac-3fbc23283690 | -12.55426 | -45.82392 | 2025-09-26 04:17:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| ba2df103-9c91-3dbc-808c-ef6ea2415361 | -13.69067 | -44.29182 | 2025-09-26 04:17:00 | NOAA-21 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| ef814ee2-972c-36d3-b966-31a8d1a267ec | -15.57569 | -51.68924 | 2025-09-26 04:17:00 | NOAA-21 | MONTES CLAROS DE GOIÁS | GOIÁS | Brasil | 5213707 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| f4f7e088-6297-37f9-924e-53f0316dd2df | -11.68074 | -44.44294 | 2025-09-26 04:17:00 | NOAA-21 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 63bd7dbb-c252-3020-9b0b-20e89d9a207f | -11.23527 | -45.55411 | 2025-09-26 04:17:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 7b4e080d-1847-3c07-b7fb-6c2204c8987c | -23.11992 | -54.44998 | 2025-09-26 04:17:00 | NOAA-21 | IGUATEMI | MATO GROSSO DO SUL | Brasil | 5004304 | 50 | 33 | nan | nan | nan | Mata Atlântica | 2.9 |
| ea184099-83f8-3412-8e6e-cdc9acf7dc4d | -20.9935 | -50.00365 | 2025-09-26 04:17:00 | NOAA-21 | PLANALTO | SÃO PAULO | Brasil | 3539608 | 35 | 33 | nan | nan | nan | Mata Atlântica | 4.6 |
| 5646a43a-3922-3ee2-96d5-67c5ca2ee0ea | -15.01666 | -49.53821 | 2025-09-26 04:17:00 | NOAA-21 | NOVA GLÓRIA | GOIÁS | Brasil | 5214861 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 395fa59a-6c34-327a-87bc-e554e0c11be7 | -11.2453 | -45.55575 | 2025-09-26 04:17:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 33.4 |
| 97caa323-ee9a-34af-8bac-de6a728db265 | -15.24209 | -48.08341 | 2025-09-26 04:17:00 | NOAA-21 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 7f9efe84-e8f0-336a-bfcb-8ff9b905620c | -10.18415 | -49.50919 | 2025-09-26 04:17:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 150910f3-e05b-3f9d-86f2-e08c733de355 | -15.59525 | -46.45507 | 2025-09-26 04:17:00 | NOAA-21 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| c313dfe0-0618-3dc8-9eaa-3a09272b2c71 | -21.66249 | -46.06348 | 2025-09-26 04:17:00 | NOAA-21 | MACHADO | MINAS GERAIS | Brasil | 3139003 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.7 |
| 5dd5d0ed-7553-3cb5-ac31-5fbfce1cf6ef | -20.98964 | -50.46664 | 2025-09-26 04:17:00 | NOAA-21 | SANTO ANTÔNIO DO ARACANGUÁ | SÃO PAULO | Brasil | 3548054 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| b59b5bba-323e-382d-b566-ef2d59f3c209 | -11.41322 | -44.97395 | 2025-09-26 04:17:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 50c4241d-fb74-3ab0-9a0a-633b6757e319 | -11.62354 | -44.44091 | 2025-09-26 04:17:00 | NOAA-21 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 8771bc0f-abbb-3b70-b793-ec4f4acc6fc5 | -15.51581 | -50.42501 | 2025-09-26 04:17:00 | NOAA-21 | FAINA | GOIÁS | Brasil | 5207535 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| d2152e84-e0ec-3b00-a175-de1e8ffc82df | -14.82298 | -45.40689 | 2025-09-26 04:17:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| eea57892-5dfd-3c89-bdbd-483866974631 | -13.28014 | -50.69914 | 2025-09-26 04:17:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| b7e6b48c-8ce6-3fcb-840d-9ed17ab4482b | -21.03778 | -51.12356 | 2025-09-26 04:17:00 | NOAA-21 | MIRANDÓPOLIS | SÃO PAULO | Brasil | 3530102 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |


[Clique aqui para ver as próximas entradas](README19.md)
