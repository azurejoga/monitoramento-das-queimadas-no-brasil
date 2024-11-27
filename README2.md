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

## Dados Diários - Página 2

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 7ac91b48-2282-3074-9f48-9cc82eae3f1e | -2.1928 | -53.7839 | 2024-11-27 00:10:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 56.0 |
| a6643231-49b7-3db7-b52f-6a8262c3d8cb | -3.1876 | -48.4387 | 2024-11-27 00:10:00 | GOES-16 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 278.4 |
| d36826ab-43c6-3fa4-9001-7c79514af803 | -4.2299 | -50.8983 | 2024-11-27 00:10:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 71.1 |
| 9cbb2c8f-a6ff-34b2-846f-9430146a880a | -2.8347 | -54.1125 | 2024-11-27 00:10:00 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 131.1 |
| c421f3ce-c44c-3f49-86b7-a979f8fe1403 | -1.9376 | -45.7141 | 2024-11-27 00:10:00 | GOES-16 | CÂNDIDO MENDES | MARANHÃO | Brasil | 2102606 | 21 | 33 | nan | nan | nan | Amazônia | 56.9 |
| 9937c8c9-4e2c-3b42-90ec-3299444c8754 | -1.675 | -46.9155 | 2024-11-27 00:10:00 | GOES-16 | SANTA LUZIA DO PARÁ | PARÁ | Brasil | 1506559 | 15 | 33 | nan | nan | nan | Amazônia | 69.7 |
| a9a55acc-575a-3fe7-b8ce-a7a965efcc59 | -2.5963 | -53.9771 | 2024-11-27 00:10:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 61.7 |
| 46737457-be94-36ec-b3bc-d4470b8225f9 | -3.1877 | -48.4172 | 2024-11-27 00:10:00 | GOES-16 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 117.4 |
| b4eeb449-2940-32ed-9014-70fd384dae0a | -1.6629 | -52.4336 | 2024-11-27 00:10:00 | GOES-16 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 52.6 |
| 05c8abb8-d814-30d7-81fa-439d655b67dd | -3.1691 | -48.4394 | 2024-11-27 00:10:00 | GOES-16 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 790.4 |
| 7dde9a09-b111-33b3-8ab9-8d050cf38aad | -4.7197 | -46.5605 | 2024-11-27 00:10:00 | GOES-16 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 111.7 |
| d1a466e0-43ea-3540-923c-9262b1b717b8 | -2.8424 | -46.8413 | 2024-11-27 00:10:00 | GOES-16 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 79.7 |
| 8f2f0b9d-d3a4-3e0f-aef3-f05071217c5c | -3.9674 | -48.0851 | 2024-11-27 00:10:00 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 112.4 |
| 9bb60d7c-e2f4-3b47-98f0-a9e4e2ce29bf | -4.7381 | -46.5816 | 2024-11-27 00:10:00 | GOES-16 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 42.9 |
| c7ac5e2a-c35b-32e5-b5d7-b74eed3278b3 | -2.8611 | -46.8186 | 2024-11-27 00:10:00 | GOES-16 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 82.4 |
| 1200aa60-13f6-3b44-a8f9-0a04e29923d8 | -4.6646 | -43.8065 | 2024-11-27 00:10:00 | GOES-16 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 70.9 |
| 7c71df5b-b425-390d-ae02-a20853bbadf6 | -3.5226 | -52.1653 | 2024-11-27 00:10:00 | GOES-16 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 112.3 |
| 964cfed5-54be-3e2d-9490-a115af3c680e | -2.9968 | -45.4584 | 2024-11-27 00:10:00 | GOES-16 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 476.0 |
| 47d1b704-63a0-3f18-8582-785b53810501 | -4.1419 | -43.7905 | 2024-11-27 00:10:00 | GOES-16 | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 71.1 |
| 3d95dacb-8871-31b8-8133-afadde1fb5a2 | -1.9376 | -45.7365 | 2024-11-27 00:10:00 | GOES-16 | GOVERNADOR NUNES FREIRE | MARANHÃO | Brasil | 2104677 | 21 | 33 | nan | nan | nan | Amazônia | 54.1 |
| 1c126520-37dd-33b3-8e6a-16f5fb4088a6 | -4.7195 | -46.5827 | 2024-11-27 00:10:00 | GOES-16 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 110.3 |
| 73fa0e0a-f6ca-3b39-bfb5-091b8307704b | -2.8239 | -46.8419 | 2024-11-27 00:10:00 | GOES-16 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 79.1 |
| 1a8d017f-a85d-3a36-9bbf-50232cf75509 | -1.9247 | -50.5908 | 2024-11-27 00:10:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 53.1 |
| 96a04c0e-b108-3dd0-bc38-7154ca380b6b | -1.6813 | -52.4537 | 2024-11-27 00:10:00 | GOES-16 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 55.7 |
| 2de8b689-bee5-3439-85cb-9a97a55e7cb3 | -2.6988 | -45.6481 | 2024-11-27 00:10:00 | GOES-16 | NOVA OLINDA DO MARANHÃO | MARANHÃO | Brasil | 2107357 | 21 | 33 | nan | nan | nan | Amazônia | 130.8 |
| dd718470-1317-313f-ba95-14f2f0fb9f5e | -3.0153 | -45.4802 | 2024-11-27 00:10:00 | GOES-16 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 139.7 |
| ca4b7a31-6681-31ef-abd9-1546147519d6 | -4.1829 | -50.866402 | 2024-11-27 00:17:00 | METOP-C | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a9b89504-b845-3d5e-ab5c-47a760f30cad | -3.1509 | -48.447899 | 2024-11-27 00:17:00 | METOP-C | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 9243b990-623b-319d-bf5b-23df30bb1477 | -4.6905 | -46.5625 | 2024-11-27 00:17:00 | METOP-C | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| eeb90c1c-2e3b-3644-ac1a-2e4d2e4b2d13 | -3.3621 | -44.1609 | 2024-11-27 00:17:00 | METOP-C | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| a5e1a994-ea15-3f81-a77b-4c338d835e6f | -4.2725 | -48.182701 | 2024-11-27 00:17:00 | METOP-C | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 2b8e5475-5df4-3ce2-8647-daa5653dd6f5 | -2.7933 | -46.821301 | 2024-11-27 00:17:00 | METOP-C | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 752daa9a-534e-330e-bbe1-874dcc76b238 | -4.0158 | -48.3204 | 2024-11-27 00:17:00 | METOP-C | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d6f01f9c-c742-36a9-adc2-aef98aaf2e9d | -3.8647 | -43.159 | 2024-11-27 00:17:00 | METOP-C | BURITI | MARANHÃO | Brasil | 2102200 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 9dd8b583-83af-3d0f-9360-0ca84be2adc5 | -3.6282 | -44.467499 | 2024-11-27 00:17:00 | METOP-C | MATÕES DO NORTE | MARANHÃO | Brasil | 2106631 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 957c690c-d0ea-3a8a-8bce-59e8ffed2e8f | -4.1861 | -50.880901 | 2024-11-27 00:17:00 | METOP-C | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 3516ea43-1b95-3d52-9b6f-a68147c0eb30 | -2.8165 | -46.832699 | 2024-11-27 00:17:00 | METOP-C | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b3b8896c-f583-3abe-8cf2-493463cab89c | -17.2603 | -46.277302 | 2024-11-27 00:17:00 | METOP-C | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 872c2bea-4f2d-3d91-ab99-c4dacc814cc8 | -2.7835 | -46.823399 | 2024-11-27 00:17:00 | METOP-C | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 33bb50de-2ec9-3aab-a15c-9ff52e95548e | -4.1163 | -43.806099 | 2024-11-27 00:17:00 | METOP-C | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 80105711-5eb5-388a-9dc4-4efe41587d66 | -19.793501 | -43.126999 | 2024-11-27 00:17:00 | METOP-C | BELA VISTA DE MINAS | MINAS GERAIS | Brasil | 3106002 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 8b9530b4-e77d-395b-ad04-992c3e6a1559 | -20.361401 | -47.4771 | 2024-11-27 00:17:00 | METOP-C | CRISTAIS PAULISTA | SÃO PAULO | Brasil | 3513207 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| 168b6e9f-3ed8-316f-9941-642b7cd20681 | -3.1563 | -48.426399 | 2024-11-27 00:17:00 | METOP-C | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| efa159df-62ce-3d42-88aa-3c8aadf073b3 | -3.822 | -45.272499 | 2024-11-27 00:17:00 | METOP-C | SATUBINHA | MARANHÃO | Brasil | 2111722 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| f1c9657d-5dca-3d9c-ab5b-3998a3a54321 | -2.8098 | -45.4897 | 2024-11-27 00:17:00 | METOP-C | SANTA HELENA | MARANHÃO | Brasil | 2109809 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| cc6b80fa-16ae-364d-9bb6-e2804ceb5199 | -5.179 | -40.637699 | 2024-11-27 00:17:00 | METOP-C | CRATEÚS | CEARÁ | Brasil | 2304103 | 23 | 33 | nan | nan | nan | Caatinga | nan |
| 834a3353-b0ba-3e41-bf11-ccaf1e0d3fe1 | -3.1411 | -48.4501 | 2024-11-27 00:17:00 | METOP-C | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 213cb1a0-e1cf-3d3e-a44d-4bb566c026e5 | -3.9458 | -48.053501 | 2024-11-27 00:17:00 | METOP-C | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d079e5eb-782a-3038-8fd2-0839635f383a | -4.6768 | -47.923901 | 2024-11-27 00:17:00 | METOP-C | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 5937e40c-0f99-317a-9497-217a8c6ae971 | -3.2154 | -50.6078 | 2024-11-27 00:17:00 | METOP-C | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f3ac0292-1e5f-36e9-8b44-75c5264f6617 | -3.8236 | -45.279598 | 2024-11-27 00:17:00 | METOP-C | SATUBINHA | MARANHÃO | Brasil | 2111722 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| b64cb103-f8af-35bd-8ad0-4ae00c5747e9 | -4.1764 | -50.882999 | 2024-11-27 00:17:00 | METOP-C | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 7f20373f-2f34-33ad-a726-c5bd07c53bc1 | -2.8183 | -46.840599 | 2024-11-27 00:17:00 | METOP-C | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| bc40fe4e-ee8e-31f4-b4da-d4aee514ba56 | -4.6923 | -46.570499 | 2024-11-27 00:17:00 | METOP-C | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 06193a89-52d8-3d69-a9e7-0c9aad7e6b87 | -4.3188 | -45.872799 | 2024-11-27 00:17:00 | METOP-C | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| bf6c8052-06e3-3dc5-bd09-6cdec7b7b130 | -4.7039 | -46.576401 | 2024-11-27 00:17:00 | METOP-C | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| ee8f5252-b25b-3929-8571-b48ad51649ee | -2.7546 | -49.195599 | 2024-11-27 00:17:00 | METOP-C | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a4b64dfa-00a6-33a4-9b6e-d9932a54f68c | -3.1487 | -48.438202 | 2024-11-27 00:17:00 | METOP-C | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b4633c0e-f1de-36a4-9cc3-380369c51579 | -2.7897 | -46.8055 | 2024-11-27 00:17:00 | METOP-C | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e018017e-b319-3328-8c71-663e28082d19 | -2.6857 | -46.257198 | 2024-11-27 00:17:00 | METOP-C | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| dd6295d6-cb46-3a42-a1c2-69ca5ab07532 | -3.9479 | -48.062901 | 2024-11-27 00:17:00 | METOP-C | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 2baa3a20-cf2b-3bf0-8c8b-1dfe05601a92 | -3.6958 | -42.2924 | 2024-11-27 00:17:00 | METOP-C | MORRO DO CHAPÉU DO PIAUÍ | PIAUÍ | Brasil | 2206670 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 3c97ba79-2f58-3c57-b8a1-a394301c507a | -3.9093 | -47.9827 | 2024-11-27 00:17:00 | METOP-C | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 1c9d50aa-9aa7-3b55-bf23-d56b2f5cf661 | -2.3222 | -47.648102 | 2024-11-27 00:17:00 | METOP-C | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 101e8bee-09a8-34a0-9c9f-561c92d89be4 | -20.358601 | -47.4617 | 2024-11-27 00:17:00 | METOP-C | CRISTAIS PAULISTA | SÃO PAULO | Brasil | 3513207 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| fa611f41-ef52-336b-9f07-00eb27c4514c | -3.684 | -47.118198 | 2024-11-27 00:17:00 | METOP-C | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 19cf0fc3-9862-36db-9afc-9a72981a4e23 | -3.0848 | -48.017899 | 2024-11-27 00:17:00 | METOP-C | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 3725eacb-0dd7-320b-89d0-bf9ee569fcba | -3.2184 | -50.621201 | 2024-11-27 00:17:00 | METOP-C | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f3860ff6-adb8-39c4-b741-bcf26238437a | -2.9602 | -45.471199 | 2024-11-27 00:17:00 | METOP-C | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 0cd3cb91-34e9-367f-8713-5ab41e4dc90a | -16.6446 | -47.238201 | 2024-11-27 00:17:00 | METOP-C | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 0f884adc-b384-3e27-a885-94682bb7629b | -3.6297 | -44.4744 | 2024-11-27 00:17:00 | METOP-C | MATÕES DO NORTE | MARANHÃO | Brasil | 2106631 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 951816be-9f9d-332f-a5a2-7c1bec0520f4 | -3.7841 | -47.4715 | 2024-11-27 00:17:00 | METOP-C | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| cecddca2-09a8-3dbb-9061-140910d43de3 | -3.4574 | -44.577702 | 2024-11-27 00:17:00 | METOP-C | MIRANDA DO NORTE | MARANHÃO | Brasil | 2106755 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| cb3a4c6d-9a81-339f-88e4-1878cc1c5110 | -3.97 | -43.257999 | 2024-11-27 00:17:00 | METOP-C | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 84dfc3bc-6199-3e33-9845-0c9b5ccdfb51 | -3.9325 | -48.085999 | 2024-11-27 00:17:00 | METOP-C | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e78dbe1c-bc7a-35f8-b89e-4026f2c04739 | -2.8405 | -46.802601 | 2024-11-27 00:17:00 | METOP-C | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 5b1df3e4-3bdc-3d8c-a6e9-8ba639d5154e | -3.9072 | -47.973301 | 2024-11-27 00:17:00 | METOP-C | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 66b6e5a3-2678-3cae-a583-58650e35f9c8 | -2.9668 | -45.454899 | 2024-11-27 00:17:00 | METOP-C | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| db916581-21d3-37d1-b581-5a13680a6de0 | -2.8147 | -46.824799 | 2024-11-27 00:17:00 | METOP-C | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 7ee17fdd-9a42-3bad-a1a6-10893776a42f | -2.3619 | -45.5149 | 2024-11-27 00:17:00 | METOP-C | TURILÂNDIA | MARANHÃO | Brasil | 2112456 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 5f469b2e-f34f-3023-9344-059255ca9f01 | -2.97 | -45.469002 | 2024-11-27 00:17:00 | METOP-C | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| c19bd161-dd46-3017-bd0e-7509d1a383e7 | -2.7853 | -46.831299 | 2024-11-27 00:17:00 | METOP-C | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a606cb77-b23d-3b90-9805-8d8b2ee68faf | -3.6859 | -47.126598 | 2024-11-27 00:17:00 | METOP-C | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ca419fd4-e903-344f-b59a-96e0d527904a | -2.6874 | -46.264702 | 2024-11-27 00:17:00 | METOP-C | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| be2a8c78-66b5-3bc9-bf06-543fd8549cc4 | -2.0743 | -46.558498 | 2024-11-27 00:17:00 | METOP-C | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| df1958ec-6faa-3ef2-91a1-0339ced0f428 | -2.7969 | -46.837101 | 2024-11-27 00:17:00 | METOP-C | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ee7474ee-736b-303a-bad2-4be402dfb67c | -1.9135 | -45.718498 | 2024-11-27 00:17:00 | METOP-C | CÂNDIDO MENDES | MARANHÃO | Brasil | 2102606 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 2ad1daa1-0dcd-33f7-b323-be0c0c803751 | -3.1443 | -48.4188 | 2024-11-27 00:17:00 | METOP-C | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 03b5bbfd-6691-30ee-849d-aca80d7e867c | -3.8631 | -43.152199 | 2024-11-27 00:17:00 | METOP-C | BURITI | MARANHÃO | Brasil | 2102200 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 9b235630-c01d-3c5b-afa8-cacf485ed7c5 | -4.1179 | -43.812901 | 2024-11-27 00:17:00 | METOP-C | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 91c9803e-d51c-3880-afea-461dd5f139b2 | -2.7915 | -46.8134 | 2024-11-27 00:17:00 | METOP-C | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ef468ea9-66c3-3beb-a67c-bf78fd6d1322 | -5.1772 | -40.6297 | 2024-11-27 00:17:00 | METOP-C | CRATEÚS | CEARÁ | Brasil | 2304103 | 23 | 33 | nan | nan | nan | Caatinga | nan |
| bbfd1b91-c4a3-3bc3-906b-555ccafb7ae2 | -3.1585 | -48.4361 | 2024-11-27 00:17:00 | METOP-C | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| faa343fc-bca7-38d5-b047-fa73a87009d0 | -22.0828 | -49.594799 | 2024-11-27 00:17:00 | METOP-C | PIRAJUÍ | SÃO PAULO | Brasil | 3538907 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 73bcfb9c-51b2-395d-b99f-abe0159fda24 | -2.8423 | -46.810501 | 2024-11-27 00:17:00 | METOP-C | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0137bf96-4cd2-398a-b66a-d53a5207e73a | -2.5192 | -45.391201 | 2024-11-27 00:17:00 | METOP-C | PRESIDENTE SARNEY | MARANHÃO | Brasil | 2109270 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 517ab312-60f5-3d9f-bdc5-0552a778a40e | -4.1732 | -50.8685 | 2024-11-27 00:17:00 | METOP-C | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 8fdfc41b-2c8a-3ebb-981f-ff5eca9edd71 | -2.6831 | -46.109699 | 2024-11-27 00:17:00 | METOP-C | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| fb0f8d44-cf72-3634-97de-42aa81423270 | -3.1541 | -48.416698 | 2024-11-27 00:17:00 | METOP-C | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 534f5587-4bcc-325c-9db9-5dfa59d55672 | -4.7021 | -46.568401 | 2024-11-27 00:17:00 | METOP-C | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | nan |


[Clique aqui para ver as próximas entradas](README3.md)
