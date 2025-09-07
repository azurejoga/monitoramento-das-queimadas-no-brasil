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

## Dados Diários - Página 66

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 90cda81c-da28-3071-99bd-067064de856b | -5.9 | -51.9388 | 2025-09-07 05:10:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| a0a2db08-378d-3cb5-bca3-8e483a102250 | -6.73149 | -50.45717 | 2025-09-07 05:10:00 | NOAA-21 | ÁGUA AZUL DO NORTE | PARÁ | Brasil | 1500347 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| b4557ebc-7c08-312f-87e7-495bbd69236a | -6.19792 | -53.2656 | 2025-09-07 05:10:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 7644f34d-cf7b-3728-be03-41a07d0a5a9f | -6.18447 | -45.43252 | 2025-09-07 05:10:00 | NOAA-21 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 23.3 |
| 5ba6d1af-d366-33c6-8964-c0cce201eff4 | -6.85236 | -52.80519 | 2025-09-07 05:10:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 05cbb884-99ca-34d1-ab82-f82de689c770 | -5.03842 | -45.32003 | 2025-09-07 05:10:00 | NOAA-21 | LAGOA GRANDE DO MARANHÃO | MARANHÃO | Brasil | 2105963 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 4885d4e7-6fef-30ce-b82f-afe8145351d2 | -7.7565 | -48.8146 | 2025-09-07 05:10:00 | NOAA-21 | ARAPOEMA | TOCANTINS | Brasil | 1702307 | 17 | 33 | nan | nan | nan | Amazônia | 2.2 |
| aa2fa3ba-d98c-3b51-9d77-e0ff0649af30 | -5.58362 | -51.91271 | 2025-09-07 05:10:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 1ac4bb20-6dbe-32e5-8cd7-b82589f58e9b | -3.33025 | -54.91203 | 2025-09-07 05:10:00 | NOAA-21 | BELTERRA | PARÁ | Brasil | 1501451 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 31c75957-cb50-3b92-a4bd-cb22f17faedb | -3.53821 | -53.0233 | 2025-09-07 05:10:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 79e70e78-21c1-3ec1-b085-584b3ba17017 | -4.48149 | -48.11923 | 2025-09-07 05:10:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| a46dd872-093c-3803-aa9e-18777056fd27 | -6.27084 | -52.80745 | 2025-09-07 05:10:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 0843dcce-4aff-3730-b0b2-0ab57397949b | -3.44337 | -54.63425 | 2025-09-07 05:10:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 6628a415-030f-3837-adbb-6c69f4835350 | -8.14598 | -44.89069 | 2025-09-07 05:10:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 9.8 |
| 3c3e35c6-4567-3950-b714-972cfb5d2b10 | -5.96835 | -53.58639 | 2025-09-07 05:10:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 2751f807-d619-3211-96bc-ba97f81476e1 | -5.88101 | -45.08008 | 2025-09-07 05:10:00 | NOAA-21 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 044e5d6e-76f5-3f10-b960-89231b85459f | -2.43178 | -49.30521 | 2025-09-07 05:10:00 | NOAA-21 | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 7c316192-8261-334b-ac4a-66f08965f791 | -1.29034 | -48.4344 | 2025-09-07 05:10:00 | NOAA-21 | BELÉM | PARÁ | Brasil | 1501402 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 9e65ea1b-dd6c-356f-8089-93978db2cc55 | -6.82782 | -52.80669 | 2025-09-07 05:10:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 96771f2d-21be-3739-b8d4-2de757b24063 | -5.97143 | -53.59148 | 2025-09-07 05:10:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| f5053d8d-44e4-3b6d-a2d3-9fde58295e7f | -6.84719 | -52.84089 | 2025-09-07 05:10:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| f495521f-5972-39ee-adf8-d869243dcb76 | -7.73251 | -50.31377 | 2025-09-07 05:10:00 | NOAA-21 | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 5e16d32f-3879-3f66-838f-38965c795e3f | -6.18592 | -45.42173 | 2025-09-07 05:10:00 | NOAA-21 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 12.4 |
| 9a7cc73c-0e74-372f-9e1a-fc969a226411 | -7.67577 | -50.26197 | 2025-09-07 05:10:00 | NOAA-21 | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 7.4 |
| f825dd18-d4b8-330e-9a56-8111a6518be1 | -4.26806 | -48.18332 | 2025-09-07 05:10:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| c972cb36-80e0-3cbe-9ab2-e287fd1d6935 | -6.73077 | -50.46209 | 2025-09-07 05:10:00 | NOAA-21 | ÁGUA AZUL DO NORTE | PARÁ | Brasil | 1500347 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 31d29a1a-c288-3b82-b708-49e104d1a3f2 | -3.53674 | -53.02465 | 2025-09-07 05:10:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| b9f6673f-01fd-344a-845a-a09efcb7bf8b | -6.30102 | -55.18729 | 2025-09-07 05:10:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 4cd588a6-6120-3fb7-91d8-4e0998fbab8f | -7.67525 | -50.3006 | 2025-09-07 05:10:00 | NOAA-21 | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| fd5d92dc-c174-3c71-9672-8b3e773dde8e | -3.37884 | -50.84643 | 2025-09-07 05:10:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 964cd879-a90e-368f-af3c-d62c47595468 | -5.03201 | -45.31934 | 2025-09-07 05:10:00 | NOAA-21 | LAGOA GRANDE DO MARANHÃO | MARANHÃO | Brasil | 2105963 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| df34e273-3a7c-38cc-94f8-c8f2218b30db | -8.11995 | -45.31604 | 2025-09-07 05:10:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 5.1 |
| f45373b1-bbe3-34fd-9a21-983e2b0e9976 | -6.13666 | -44.2569 | 2025-09-07 05:10:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 434f34ca-441a-3299-9130-6da047963d6a | -5.10783 | -56.14389 | 2025-09-07 05:10:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 89887b43-098c-3d68-9823-f9aad8901fe2 | -5.95226 | -46.17984 | 2025-09-07 05:10:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| bad9b7fa-ca3c-389b-b7ab-79a598f03efb | -3.90969 | -54.68356 | 2025-09-07 05:10:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| ad8b3e5c-a4b5-3a07-9ee4-f8dead66b11e | -6.20101 | -53.271 | 2025-09-07 05:10:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| fde6489a-a5ef-382f-9716-dc7dca630bfd | -2.81573 | -49.20017 | 2025-09-07 05:10:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 9f576b9e-3a3b-3e3c-9c95-ce12f2d5d775 | -5.9957 | -44.15276 | 2025-09-07 05:10:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 12.1 |
| 471e64ca-b179-3965-b7cb-192ea6be56ac | -6.84249 | -52.84544 | 2025-09-07 05:10:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 4d3cfb18-16ac-313c-ae03-543b31f379d3 | -6.27011 | -52.8123 | 2025-09-07 05:10:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| d6bd6d3b-e6db-3eb2-b926-17f1e052c4de | -3.24628 | -50.80317 | 2025-09-07 05:10:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| f334e03a-2ff8-3481-a6b2-78616004dd6f | -6.80346 | -47.0712 | 2025-09-07 05:10:00 | NOAA-21 | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 4cd65595-7b98-34e0-8c94-b00a4cdc3823 | -6.20009 | -53.25122 | 2025-09-07 05:10:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| effb8cfe-4ff5-3723-95c6-07c6bc30d27c | -6.27921 | -53.44633 | 2025-09-07 05:10:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 62b7e968-6e9a-36fc-8fde-8c585abbcfb8 | -5.97451 | -53.59646 | 2025-09-07 05:10:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 6cf26b98-8054-3346-87be-ef6510d05a1e | -6.80249 | -50.84693 | 2025-09-07 05:10:00 | NOAA-21 | OURILÂNDIA DO NORTE | PARÁ | Brasil | 1505437 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 78386e0d-281e-3674-b078-583c2f2eb652 | -5.98846 | -44.15437 | 2025-09-07 05:10:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 11.9 |
| 4028d13f-5f03-39e6-9228-9156e9b445c5 | -3.59552 | -47.51859 | 2025-09-07 05:10:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 9.6 |
| e664eaeb-bcf4-3d03-b6a7-9b6cdd911132 | -3.62984 | -49.1951 | 2025-09-07 05:10:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 6e935714-f013-3f73-86f8-53228bbafb2d | -6.20246 | -53.26143 | 2025-09-07 05:10:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| b7990083-b4d0-3366-969d-b1429a82fd89 | -7.81324 | -45.43274 | 2025-09-07 05:10:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 76c03078-4e4c-370e-a473-8b216b86f789 | -6.20484 | -53.27153 | 2025-09-07 05:10:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 78365fcd-5861-37d7-b4b3-544355342483 | -6.95561 | -52.78376 | 2025-09-07 05:10:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 5b5c801c-9e98-3b8e-b63d-acef9e8b492d | -5.88064 | -45.07895 | 2025-09-07 05:10:00 | NOAA-21 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 7.0 |
| 51a15776-6c77-357b-a64f-910d7228dec9 | -6.86363 | -52.78335 | 2025-09-07 05:10:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 4a5cc531-ddb8-3f93-9ab8-343c53069c3a | -5.95241 | -53.79688 | 2025-09-07 05:10:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 0f44d481-b3e0-35ec-8abf-e75574bdf9fe | -7.67529 | -47.33098 | 2025-09-07 05:10:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 3dc11ee8-589c-330f-b89b-0c341459cb1f | -5.06758 | -56.07268 | 2025-09-07 05:10:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 09ff447d-7913-317e-a7df-1c88655742ed | -8.15014 | -44.85706 | 2025-09-07 05:10:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 2a108708-617b-39fd-972e-672e7140e254 | -4.42761 | -54.85023 | 2025-09-07 05:10:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| dd0b18b5-e42b-3efa-8e16-76ff59facb73 | -4.25783 | -48.54846 | 2025-09-07 05:10:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 7e2970bf-033d-39f4-b23f-a99ceec92892 | -5.22026 | -43.70077 | 2025-09-07 05:10:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 7.5 |
| ee20ea12-644a-32e5-9ddd-2aeebb85b7a1 | -5.71911 | -53.70298 | 2025-09-07 05:10:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 482122f7-8b6f-3cf8-9414-07a44d62e06c | -6.13831 | -44.24453 | 2025-09-07 05:10:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 0e1831b3-d299-3fde-96fe-f748dfc8207c | -6.283 | -53.44687 | 2025-09-07 05:10:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| dfc8e940-b3ff-3f98-a681-8e82082293e2 | -2.82604 | -49.1965 | 2025-09-07 05:10:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 1c7fa743-b33f-34b5-b647-b3e03cd2952e | -6.29698 | -55.19058 | 2025-09-07 05:10:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c7047031-02e4-340a-b5f7-b0d6d32a5241 | -6.34897 | -55.56398 | 2025-09-07 05:10:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 274ee518-2ab2-310e-b9ee-55b1ce7669ef | -5.07147 | -56.06967 | 2025-09-07 05:10:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 6064b68d-5d2b-39b1-bd7e-087a85426d34 | -8.33552 | -46.94403 | 2025-09-07 05:10:00 | NOAA-21 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| f606dfa7-8bbc-3cfb-877c-2a2251ebf832 | -1.94237 | -56.59106 | 2025-09-07 05:10:00 | NOAA-21 | TERRA SANTA | PARÁ | Brasil | 1507979 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 4c4a6481-e004-3f8c-95c0-614f18a04738 | -7.97871 | -44.94453 | 2025-09-07 05:10:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 3bf75fd1-3727-3cd7-8a1a-f0ad86140ec2 | -3.59109 | -47.51077 | 2025-09-07 05:10:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 12.4 |
| fc3a69d5-d5d7-3db1-8f00-397b5ccdd69f | -6.84323 | -52.84029 | 2025-09-07 05:10:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 7bc42338-a880-311c-8949-6aa34cc89f51 | -5.97825 | -53.59698 | 2025-09-07 05:10:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f968f7d3-4bad-3062-814d-133266e18857 | -6.19937 | -53.256 | 2025-09-07 05:10:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 3a8802ed-8013-328e-a040-d2a4f746b8c0 | -5.97077 | -53.59594 | 2025-09-07 05:10:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 14020476-ad30-3c3c-ae45-837dc1a6500b | -3.59369 | -47.5165 | 2025-09-07 05:10:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 9.7 |
| 868b766f-009c-34fc-b538-6a57f9c28f93 | -6.82451 | -52.81001 | 2025-09-07 05:10:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 8790fd21-955a-3570-8f29-4b5d95fa7fc7 | -4.26852 | -48.18011 | 2025-09-07 05:10:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 019cd084-387f-3dee-b441-ccc9d8606e93 | -4.48104 | -48.11848 | 2025-09-07 05:10:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 68234c26-c8de-33a1-8c91-637c9a225f0c | -6.19865 | -53.26078 | 2025-09-07 05:10:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| b80210f7-8884-34a4-a41e-7c349d176a8d | -5.99626 | -44.14891 | 2025-09-07 05:10:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 16.6 |
| 68afdcb9-fe61-3e03-a7cd-3d51155ea9ec | -2.55405 | -48.39489 | 2025-09-07 05:10:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 0777972d-46aa-39bb-8949-d0f0c2624d6c | -7.75605 | -48.81789 | 2025-09-07 05:10:00 | NOAA-21 | ARAPOEMA | TOCANTINS | Brasil | 1702307 | 17 | 33 | nan | nan | nan | Amazônia | 2.2 |
| a475b768-629d-3046-8661-23cfd3e7f741 | -5.63338 | -51.35857 | 2025-09-07 05:10:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 5a6d5a91-93b5-3689-afc5-b5cd3f9f58d0 | -5.95175 | -53.80128 | 2025-09-07 05:10:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 71131f76-d378-34b4-a2fe-8e21c9de2288 | -5.79723 | -45.6561 | 2025-09-07 05:10:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 5d6bfdc5-2c3a-303f-9651-46a13217f82a | -8.48476 | -45.17849 | 2025-09-07 05:10:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 23cf01dc-ea12-36cc-8149-e0eb134d5320 | -6.28201 | -53.42776 | 2025-09-07 05:10:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| c784bd80-9e6e-3f5d-99e1-3bf802a82ac5 | -3.34854 | -47.60917 | 2025-09-07 05:10:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| aae91bc5-b83e-3295-ae52-e1fd0e681fa2 | -5.10728 | -56.14741 | 2025-09-07 05:10:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 529f85b3-8b0d-3211-90e5-74d74466d2cc | -5.09897 | -56.15696 | 2025-09-07 05:10:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 7ffc813f-f545-3c68-8617-27ed0fb606d6 | -6.15943 | -53.68383 | 2025-09-07 05:10:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| bea1ce7f-72ff-39c4-b9e1-5f239a167481 | -7.71752 | -44.71831 | 2025-09-07 05:10:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 33be1d81-a2e4-3d4c-a964-942be4fff4e1 | -6.60775 | -48.05935 | 2025-09-07 05:10:00 | NOAA-21 | DARCINÓPOLIS | TOCANTINS | Brasil | 1706506 | 17 | 33 | nan | nan | nan | Amazônia | 5.5 |
| d9717f0d-7a6a-3529-b150-131ad22d50bb | -3.5906 | -47.51427 | 2025-09-07 05:10:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 15.1 |
| 49525eaa-2533-3a7c-85f7-1f966a101677 | -6.18266 | -53.26317 | 2025-09-07 05:10:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| f1800feb-8036-3f9f-bbc4-3faa1c40b73a | -6.61087 | -44.07938 | 2025-09-07 05:10:00 | NOAA-21 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 14.3 |


[Clique aqui para ver as próximas entradas](README67.md)
