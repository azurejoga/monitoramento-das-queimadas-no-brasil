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

## Dados Diários - Página 91

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| f51fcab6-67b7-3ede-912b-abc68b2ac180 | -17.95567 | -57.36921 | 2024-10-13 05:06:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 11.2 |
| b572d337-fc36-372c-a752-3435126fa434 | -17.95511 | -57.3729 | 2024-10-13 05:06:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 11.2 |
| 51f0f9c5-d31e-3075-813c-ed6dbb726d24 | -17.95455 | -57.37659 | 2024-10-13 05:06:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 7.8 |
| e079fbc2-9d5b-3322-84e2-29e0251be552 | -17.9114 | -57.35492 | 2024-10-13 05:06:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.9 |
| 9c968dac-733c-3f25-9b8e-8675855c682d | -17.91084 | -57.35861 | 2024-10-13 05:06:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.9 |
| 91279e77-a609-3348-90c6-72553b2378ac | -17.91027 | -57.3623 | 2024-10-13 05:06:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.1 |
| bef8ddba-7855-3e7c-b7b6-f59e58567e7c | -17.90861 | -57.35067 | 2024-10-13 05:06:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 4.9 |
| 45b94a02-4b01-348c-a379-d7cabc455759 | -17.90807 | -57.33164 | 2024-10-13 05:06:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.3 |
| b77d1056-41e7-3e23-84cb-7a3d0a808cba | -17.90804 | -57.35436 | 2024-10-13 05:06:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 5.4 |
| cac9b811-5a97-3ab7-813d-338ffee63471 | -17.90748 | -57.35805 | 2024-10-13 05:06:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 5.4 |
| 4e4cd016-875c-378f-aa8e-21b72c4d73ce | -17.90694 | -57.33903 | 2024-10-13 05:06:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.0 |
| 442ebe3e-d560-3e3e-8316-2ae21c4aaf94 | -17.90581 | -57.34641 | 2024-10-13 05:06:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 4.9 |
| d2ba021e-b78b-38e8-ae66-dd29432a9ee9 | -17.90527 | -57.32738 | 2024-10-13 05:06:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.1 |
| 662c4a59-d3e3-3d76-834a-8fa1968c2e55 | -17.90525 | -57.35011 | 2024-10-13 05:06:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 4.9 |
| 4c23d65b-21ab-360b-9849-95d3b23816b9 | -17.90471 | -57.33108 | 2024-10-13 05:06:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.4 |
| a9745a7e-3bd3-39f0-8559-58cb47069d6c | -17.90469 | -57.3538 | 2024-10-13 05:06:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 5.4 |
| 04fa8768-2644-3a97-a91a-6411dcb9793c | -17.90415 | -57.33478 | 2024-10-13 05:06:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.4 |
| 70cb0a59-6a55-3309-9bf7-aa52b77b4492 | -17.90413 | -57.3575 | 2024-10-13 05:06:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 5.4 |
| 57ef5091-12f0-3f7a-841a-b77dd34aec51 | -17.90358 | -57.33847 | 2024-10-13 05:06:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.6 |
| a0e4a39d-8c6b-32b1-9fe3-b6cdb254853d | -17.90356 | -57.36119 | 2024-10-13 05:06:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 7.0 |
| 0d52d520-1278-3283-b453-9bb62cb831ce | -17.903 | -57.36489 | 2024-10-13 05:06:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 7.0 |
| 4fcb36e0-0e2f-37e9-9b1c-ecc85648daa6 | -17.90246 | -57.34586 | 2024-10-13 05:06:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.4 |
| 6b6df10e-d90f-33a8-bc42-dc6cddb4d362 | -17.9019 | -57.34955 | 2024-10-13 05:06:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.4 |
| 9dfbd8fb-90b5-3416-9c3c-c958ae996534 | -17.90133 | -57.35324 | 2024-10-13 05:06:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 4.1 |
| 73c7f19f-5e2a-3067-816a-5acb01eb60d1 | -17.90077 | -57.35694 | 2024-10-13 05:06:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 4.1 |
| 8ea529b0-23eb-3abc-9c25-c194df5c68ba | -17.90023 | -57.33791 | 2024-10-13 05:06:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.6 |
| 3328e0e1-d4bb-3a95-a41d-9be0431ed799 | -17.90021 | -57.36063 | 2024-10-13 05:06:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 16.3 |
| 4ed3e991-7b17-3c41-a59a-09eefad34b14 | -17.89967 | -57.3416 | 2024-10-13 05:06:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.6 |
| e2a78632-9352-342c-8b4c-6779984b44cc | -17.8991 | -57.3453 | 2024-10-13 05:06:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.4 |
| 803d6948-7269-37b4-80b4-68e5be4699f0 | -17.89854 | -57.349 | 2024-10-13 05:06:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.4 |
| 71c74c95-074a-30b1-bb67-73ea206a9ab6 | -17.89798 | -57.35269 | 2024-10-13 05:06:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 4.1 |
| 1f489495-0ea2-3fed-b103-9619ae6fe81c | -17.89742 | -57.35638 | 2024-10-13 05:06:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 4.1 |
| edf00e6b-c83c-3dab-a0a8-58c2473d14d8 | -17.89685 | -57.36007 | 2024-10-13 05:06:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 16.3 |
| 1c9f1ff9-9b94-3d28-a5ca-801cf9c58193 | -17.89462 | -57.35213 | 2024-10-13 05:06:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.5 |
| a49af0d0-3f7c-3777-9647-aadb6c495943 | -17.89186 | -57.30241 | 2024-10-13 05:06:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.5 |
| d28e6728-7159-3b6b-9c7f-fb1ebdc1c652 | -17.88906 | -57.29815 | 2024-10-13 05:06:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.2 |
| 282471bc-b99c-36ee-8d25-40602b75991b | -17.8885 | -57.30185 | 2024-10-13 05:06:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.2 |
| 158b51f8-6ac7-390f-9aaf-533720c34d1f | -17.88514 | -57.30129 | 2024-10-13 05:06:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.2 |
| 62e61690-c635-312b-a7c8-369eea19706f | -17.88458 | -57.30499 | 2024-10-13 05:06:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 0.8 |
| debda5ac-26bc-3364-83cb-c3438cb49ea2 | -17.88123 | -57.30443 | 2024-10-13 05:06:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.1 |
| dac8aff9-a567-33e6-964f-c2343521a996 | -17.87451 | -57.30331 | 2024-10-13 05:06:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.4 |
| 29fbe240-44c7-3bf5-b75d-3fc21dee5b55 | -17.85547 | -57.38345 | 2024-10-13 05:06:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.8 |
| b57b6bf8-e570-3770-a2a3-5248419da966 | -17.85267 | -57.3792 | 2024-10-13 05:06:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 5.5 |
| eac9e2c1-77ea-3871-b0b9-3d30e40b7176 | -17.84785 | -57.31447 | 2024-10-13 05:06:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.1 |
| 01cb03eb-ff3a-3a62-8801-f932353def30 | -17.8445 | -57.31392 | 2024-10-13 05:06:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.1 |
| fcfa6a47-9c31-39cf-ac9b-551db81ea9b8 | -17.84393 | -57.31761 | 2024-10-13 05:06:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.1 |
| 7ecd8ebb-1f3d-3d02-9bd2-b105693eac22 | -17.84114 | -57.31335 | 2024-10-13 05:06:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.6 |
| 05fd0ca0-7dfa-3185-b901-d61df5a4019e | -17.84057 | -57.31705 | 2024-10-13 05:06:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.6 |
| 7f74e910-0193-35e7-84e0-77b00549e381 | -17.83993 | -57.36615 | 2024-10-13 05:06:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 7.2 |
| b3f4c962-de99-315d-893a-d3784258a2d6 | -17.83937 | -57.36983 | 2024-10-13 05:06:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 7.2 |
| 3fd2480d-ac43-339a-b36b-2bbefe81f24a | -17.83778 | -57.3128 | 2024-10-13 05:06:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.6 |
| c819bdaa-4c49-35cc-a7d2-44cc047fda48 | -17.83658 | -57.36559 | 2024-10-13 05:06:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 7.2 |
| e2236d3a-e3d0-3027-a384-f9a98b278d23 | -17.83601 | -57.36928 | 2024-10-13 05:06:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 7.2 |
| 6a7b6a80-be13-3524-89f7-13f8d4cc75b4 | -17.83322 | -57.36503 | 2024-10-13 05:06:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 4.9 |
| 7a233fcb-7d6f-3ad5-9ef8-8a32bfc56e42 | -17.83266 | -57.36872 | 2024-10-13 05:06:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 4.9 |
| 3da3eee1-244f-367a-b59a-b171d9c3d988 | -17.83209 | -57.37241 | 2024-10-13 05:06:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.8 |
| 7fed2df9-620f-3ac1-ab8d-7d3e739b8682 | -17.83153 | -57.37609 | 2024-10-13 05:06:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.8 |
| f1e12e76-0bec-39f9-952d-2dff9536a2c4 | -17.83096 | -57.37978 | 2024-10-13 05:06:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.7 |
| 38eed75c-cc1f-37e0-bdba-34d08a479111 | -17.82817 | -57.37553 | 2024-10-13 05:06:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.8 |
| 530aa04d-3d62-35f3-9fb9-1660688f1ce1 | -17.21836 | -57.30991 | 2024-10-13 05:06:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 0.5 |
| b35eb4f2-4436-3db4-8c29-b4e33e007cc8 | -17.2178 | -57.31357 | 2024-10-13 05:06:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 0.5 |
| 59129787-2a43-3e78-9bf0-4ac5868190c2 | -17.21724 | -57.31723 | 2024-10-13 05:06:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 0.6 |
| bd7eef92-dc6d-3594-b3dd-a26c42be2432 | -17.19431 | -57.46709 | 2024-10-13 05:06:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.9 |
| 5d93be38-b55f-3d20-b36d-ce77dedd2e0e | -17.19096 | -57.46653 | 2024-10-13 05:06:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.9 |
| cb7a81fd-784a-371a-a097-7b4724335929 | -17.1904 | -57.47018 | 2024-10-13 05:06:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 0.6 |
| b89b9a8b-270c-3e14-8469-261d377c4e49 | -17.18984 | -57.47382 | 2024-10-13 05:06:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 0.6 |
| 40cc6b45-f05b-3bac-becb-95695561c820 | -17.18874 | -57.45868 | 2024-10-13 05:06:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 0.3 |
| a650769c-24e4-3e99-9b7f-cb97e8251da0 | -17.18596 | -57.45447 | 2024-10-13 05:06:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 0.3 |
| 6e95aba2-cefa-3bfc-8cc4-0c57d6ae6259 | -17.1854 | -57.45813 | 2024-10-13 05:06:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 0.3 |
| dfd03a45-f145-3538-b993-cf4b46fe0fb1 | -17.18206 | -57.45757 | 2024-10-13 05:06:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.9 |
| d1d44a65-f2e3-3593-b622-80dbdca1b6b3 | -17.17926 | -57.4758 | 2024-10-13 05:06:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 5.0 |
| 6336151c-5726-3ee0-bbed-bc5b6366ca90 | -17.17706 | -57.45718 | 2024-10-13 05:06:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.9 |
| 83852bb7-a7bd-39b1-92dc-4494074760a5 | -17.17424 | -57.4754 | 2024-10-13 05:06:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 0.7 |
| 693af8db-1872-3a61-adf6-32b8cb3b4b74 | -17.17368 | -57.47905 | 2024-10-13 05:06:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 0.7 |
| 74a8090b-1a25-3ff9-9e74-90ddeb690765 | -17.17282 | -57.30658 | 2024-10-13 05:06:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 0.5 |
| 70dac460-ae89-3190-887d-1a9fe2c6338e | -17.1709 | -57.47485 | 2024-10-13 05:06:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 0.7 |
| a30423c8-0bd9-36d8-b7eb-78b6ee056677 | -17.17033 | -57.47849 | 2024-10-13 05:06:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 0.7 |
| d6485243-3a05-3954-9517-34e35f6c5acb | -16.9983 | -57.46885 | 2024-10-13 05:06:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.9 |
| ee7385b1-61e3-3825-bb27-10975ee30f51 | -16.99774 | -57.47249 | 2024-10-13 05:06:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.9 |
| 135cdb84-6825-342f-b93d-8e2da8e9234d | -16.90732 | -57.80004 | 2024-10-13 05:06:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 0.8 |
| 28074680-43a6-30b0-af1f-fb287e153c14 | -16.90676 | -57.80365 | 2024-10-13 05:06:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.5 |
| 2422a69c-a066-393e-ac4c-5602ac6e0ded | -16.90399 | -57.79948 | 2024-10-13 05:06:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 0.8 |
| bd03b49d-b0e3-3ac7-960f-31454510562c | -16.90343 | -57.80309 | 2024-10-13 05:06:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.5 |
| 9d33ab0c-78b1-3cf9-8e81-0edc5ddc448c | -18.67483 | -57.33628 | 2024-10-13 05:06:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 0.8 |
| de61cc0e-3b27-3cdd-a4d2-07ba4d846477 | -18.67426 | -57.34002 | 2024-10-13 05:06:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.4 |
| b55c4704-0e13-38fa-af53-629940d1498a | -18.67146 | -57.33572 | 2024-10-13 05:06:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 0.8 |
| b9800b02-dfae-39bb-b38a-380e5b38fb9d | -18.67089 | -57.33946 | 2024-10-13 05:06:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.4 |
| 83e63e77-6c6b-3f0b-afdb-d8b80757fb65 | -14.76643 | -57.79471 | 2024-10-13 05:06:00 | NPP-375D | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| de5194a7-c140-3e53-a557-f77a9d29f719 | -14.76587 | -57.79827 | 2024-10-13 05:06:00 | NPP-375D | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| a983ac04-f9dd-357c-8bf6-c3c532941903 | -14.76254 | -57.79772 | 2024-10-13 05:06:00 | NPP-375D | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 4231b3cc-eb81-3557-a3e9-c825c051be31 | -14.63448 | -57.94534 | 2024-10-13 05:06:00 | NPP-375D | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 704068cd-b79e-3c79-9148-81b872caf858 | -14.63391 | -57.94893 | 2024-10-13 05:06:00 | NPP-375D | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| d51b5dad-6bf9-32f4-b275-94eff2d0d09d | -14.62782 | -57.94423 | 2024-10-13 05:06:00 | NPP-375D | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 94ae2dd3-3022-3de0-a681-53af4c73a27a | -14.62506 | -57.94011 | 2024-10-13 05:06:00 | NPP-375D | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 776f34b0-469d-3a5d-9478-bb3a0fe8902a | -15.96729 | -59.12375 | 2024-10-13 05:06:00 | NPP-375D | PORTO ESPERIDIÃO | MATO GROSSO | Brasil | 5106828 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 5cdf88f7-50f9-33de-ab63-ba2e92d7c7b6 | -15.96391 | -59.12318 | 2024-10-13 05:06:00 | NPP-375D | PORTO ESPERIDIÃO | MATO GROSSO | Brasil | 5106828 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| b6e7e0d4-7d90-30e7-8c71-5b6ea7606df0 | -15.96331 | -59.12684 | 2024-10-13 05:06:00 | NPP-375D | PORTO ESPERIDIÃO | MATO GROSSO | Brasil | 5106828 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 617a4006-ab31-3747-8109-f8bff3826b93 | -15.96054 | -59.12261 | 2024-10-13 05:06:00 | NPP-375D | PORTO ESPERIDIÃO | MATO GROSSO | Brasil | 5106828 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 6e236ccf-f53a-3403-a069-56e6da9d43da | -15.95994 | -59.12626 | 2024-10-13 05:06:00 | NPP-375D | PORTO ESPERIDIÃO | MATO GROSSO | Brasil | 5106828 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 077603d5-6ae9-3de0-a8e5-41f8d74d0315 | -15.95742 | -59.09935 | 2024-10-13 05:06:00 | NPP-375D | PORTO ESPERIDIÃO | MATO GROSSO | Brasil | 5106828 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |


[Clique aqui para ver as próximas entradas](README92.md)
