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
| c0ea3de1-2eb8-3ca0-a75a-cf3e8a59e33d | -6.0862 | -48.0339 | 2024-11-30 01:20:00 | GOES-16 | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | 138.9 |
| 4b7892c3-ce1d-3eeb-afef-d1de918ae04c | -3.9886 | -41.5165 | 2024-11-30 01:20:00 | GOES-16 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 122.7 |
| af58e0ae-0542-379d-b3dc-f228e3fbd1a9 | -3.4791 | -53.8142 | 2024-11-30 01:20:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 101.5 |
| 206ccd89-4082-3bb7-8f66-14758afc3f8f | -3.2406 | -53.6393 | 2024-11-30 01:20:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 75.2 |
| e71c7b76-bed8-3d09-8cf0-49714658a031 | -3.2591 | -53.6186 | 2024-11-30 01:20:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 65.4 |
| 8eceef05-291b-34a8-afb1-401779c3c1ee | -1.0733 | -53.6378 | 2024-11-30 01:20:00 | GOES-16 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 51.0 |
| 1740adfc-4fb7-3d1e-94db-e286bcfdf38b | -1.6777 | -45.7868 | 2024-11-30 01:20:00 | GOES-16 | CÂNDIDO MENDES | MARANHÃO | Brasil | 2102606 | 21 | 33 | nan | nan | nan | Amazônia | 45.5 |
| 2a9001be-0cd2-3236-a0b7-95ea4e56ea95 | -4.6237 | -47.0069 | 2024-11-30 01:20:00 | GOES-16 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 159.9 |
| 7ed521d4-9a82-3110-bfe6-951cca3035a1 | -3.4792 | -53.7941 | 2024-11-30 01:20:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 53.2 |
| 00b89e5d-dd5c-3996-be36-0255cecf2823 | -6.8967 | -43.5436 | 2024-11-30 01:20:00 | GOES-16 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 80.4 |
| a46abab1-a8e7-33cd-8ef3-58b87dbb0eeb | -1.6753 | -46.7836 | 2024-11-30 01:20:00 | GOES-16 | VISEU | PARÁ | Brasil | 1508308 | 15 | 33 | nan | nan | nan | Amazônia | 46.0 |
| a7820fa1-7ac2-3907-83fc-fe8648568b35 | -17.6457 | -57.5668 | 2024-11-30 01:20:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 68.0 |
| 040216c1-b29b-31e0-8983-3ca3c18179e4 | -2.0164 | -50.756 | 2024-11-30 01:20:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 45.0 |
| 7f0bb683-6f55-3f0b-9071-061f2b62994e | -1.2556 | -54.5589 | 2024-11-30 01:20:00 | GOES-16 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 50.1 |
| 05ca2f32-e21d-32fe-a321-796565893cc6 | -4.8338 | -41.2942 | 2024-11-30 01:20:00 | GOES-16 | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 81.2 |
| 53166908-5119-3054-ae87-b81349a6bfe3 | -2.5216 | -48.4591 | 2024-11-30 01:20:00 | GOES-16 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 45.9 |
| 66e9339e-1cda-35f6-8b5a-cb97f3d35cc9 | -6.0676 | -48.0352 | 2024-11-30 01:20:00 | GOES-16 | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | 60.1 |
| 6bec1899-3900-3d0f-8033-4301e7dd9dd3 | -17.6851 | -57.5621 | 2024-11-30 01:20:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 59.3 |
| 27b78b0e-3e8e-3bec-a191-3b8e3edc75c4 | -17.6654 | -57.5645 | 2024-11-30 01:20:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 105.2 |
| ab3abcfc-6dbd-3a26-a657-6202476501c6 | -4.8715 | -41.2674 | 2024-11-30 01:20:00 | GOES-16 | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 191.3 |
| 381f0ec3-50f8-34f7-b70a-cd88e504b6f0 | -1.2739 | -54.5587 | 2024-11-30 01:20:00 | GOES-16 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 87.7 |
| 52a63888-a9a9-3364-8337-d850f2e40e0a | -4.6052 | -46.9859 | 2024-11-30 01:20:00 | GOES-16 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 111.2 |
| 9fde4443-ba31-3c3d-a401-db2ceec55f93 | -1.6938 | -46.7833 | 2024-11-30 01:20:00 | GOES-16 | VISEU | PARÁ | Brasil | 1508308 | 15 | 33 | nan | nan | nan | Amazônia | 81.9 |
| 8bfdae88-3af0-358b-83c8-bca99b2b163b | -6.9156 | -43.5418 | 2024-11-30 01:20:00 | GOES-16 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 467.6 |
| 139cc5b7-1510-3a05-a908-8891449b13b1 | -1.2739 | -54.5387 | 2024-11-30 01:20:00 | GOES-16 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 48.5 |
| aa7c8f9b-7e8a-3dfe-8dfb-839acecb6360 | -1.2556 | -54.5389 | 2024-11-30 01:20:00 | GOES-16 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 46.4 |
| 92bdd196-54d3-32ba-a65b-fe13746bb2cc | -4.8152 | -41.2713 | 2024-11-30 01:20:00 | GOES-16 | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 88.6 |
| 8913e7e5-485f-3043-bdd7-28e383b04063 | -2.5963 | -53.9771 | 2024-11-30 01:20:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 53.5 |
| 22082547-fee8-3c8f-99cf-a94ecd3c6b4d | -2.0163 | -50.7768 | 2024-11-30 01:20:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 108.0 |
| 72ecb2ce-6b2e-3772-89b3-abfb5199ec0f | -4.8713 | -41.2915 | 2024-11-30 01:20:00 | GOES-16 | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 780.9 |
| dd50f227-3349-3f6b-bbc2-7ec4852e2953 | -4.6238 | -46.9849 | 2024-11-30 01:20:00 | GOES-16 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 94.6 |
| 00ec4a2b-1151-32ab-9f09-64d6ec058905 | -2.0347 | -50.7765 | 2024-11-30 01:20:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 55.6 |
| 2d15c7ba-e1f7-32b7-8372-f021a8efb155 | -6.0674 | -48.0569 | 2024-11-30 01:20:00 | GOES-16 | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | 55.1 |
| e1c85867-d5c4-3da5-ad7a-e3f001701ad5 | -4.8523 | -41.317 | 2024-11-30 01:20:00 | GOES-16 | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 131.4 |
| 337ff085-4004-3408-ace8-a80d8cffd283 | -17.6651 | -57.585 | 2024-11-30 01:20:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 86.8 |
| e8653497-b7e2-3fcb-bf90-04db64d376b7 | -3.6757 | -47.1395 | 2024-11-30 01:20:00 | GOES-16 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 67.0 |
| 90b60df4-3c1f-3e05-9220-30e1549720aa | -4.8899 | -41.3143 | 2024-11-30 01:20:00 | GOES-16 | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 253.8 |
| 5a056519-06fe-3e80-9d36-d52f19252bb4 | -4.8901 | -41.2902 | 2024-11-30 01:20:00 | GOES-16 | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 506.6 |
| 2764d613-b151-3e23-9025-a351fa527fa2 | -3.259 | -53.6388 | 2024-11-30 01:20:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 135.2 |
| 5b5d339b-a9d9-3a55-b127-b05e0b14f14b | -4.8903 | -41.266 | 2024-11-30 01:20:00 | GOES-16 | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 120.9 |
| 994e89f8-e144-3de1-9ccf-ddce02374d40 | -4.8711 | -41.3157 | 2024-11-30 01:20:00 | GOES-16 | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 417.7 |
| a3ad31a1-172c-3132-a610-e486d8c899f5 | -3.9699 | -41.5176 | 2024-11-30 01:20:00 | GOES-16 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 124.1 |
| 91472563-eaa6-3e79-b24c-62f88974d14a | -3.4976 | -53.7935 | 2024-11-30 01:20:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 62.6 |
| 12fd3b6e-8192-3502-9ea5-ca7bf7cff68d | -4.6051 | -47.0079 | 2024-11-30 01:20:00 | GOES-16 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 202.2 |
| 30ded8cf-832b-3cad-a644-4d580970cadc | -4.834 | -41.27 | 2024-11-30 01:20:00 | GOES-16 | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 106.4 |
| 73154af1-a1a7-3fd9-8650-8d8b48af41d3 | -3.4975 | -53.8137 | 2024-11-30 01:20:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 109.1 |
| ebc883b5-73a6-3276-8a46-29f56f9848cf | -2.8304 | -45.2845 | 2024-11-30 01:20:00 | GOES-16 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 47.4 |
| f7417437-5427-39d2-851f-7a362103d7ec | -4.8525 | -41.2928 | 2024-11-30 01:20:00 | GOES-16 | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 138.0 |
| a5be6db4-a665-3922-a5d9-7e789c20a5ab | -3.148 | -53.8434 | 2024-11-30 01:20:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 54.1 |
| 662b3c33-86ea-3cbd-be9d-ce74523fc39f | -4.834 | -41.27 | 2024-11-30 01:30:00 | GOES-16 | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 78.3 |
| 66bff7a2-c16e-3514-b314-8b510f704bc4 | -1.0733 | -53.6378 | 2024-11-30 01:30:00 | GOES-16 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 48.8 |
| 54b3c1da-9fb3-34a2-90f3-e1d3533db7cb | -4.8899 | -41.3143 | 2024-11-30 01:30:00 | GOES-16 | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 236.1 |
| d01e8818-3a99-36f4-9729-de051a7f9438 | -4.6238 | -46.9849 | 2024-11-30 01:30:00 | GOES-16 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 172.7 |
| a5449119-4a00-3fe0-b5ce-8d6eae71c1ed | -4.8711 | -41.3157 | 2024-11-30 01:30:00 | GOES-16 | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 472.5 |
| 55723a56-3669-32a7-b349-9e929da078c7 | -6.9156 | -43.5418 | 2024-11-30 01:30:00 | GOES-16 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 361.9 |
| 52b845b1-d625-350c-8d70-32f81a2548c8 | -2.5216 | -48.4591 | 2024-11-30 01:30:00 | GOES-16 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 46.1 |
| dc464e00-9fb1-3283-ac14-c1bd13798dd7 | -1.2739 | -54.5587 | 2024-11-30 01:30:00 | GOES-16 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 68.7 |
| 48338acd-e6d6-346a-bc6c-d755fc84a85d | -1.6938 | -46.7833 | 2024-11-30 01:30:00 | GOES-16 | VISEU | PARÁ | Brasil | 1508308 | 15 | 33 | nan | nan | nan | Amazônia | 111.9 |
| c073f0e9-96b4-3ba5-8070-c0b88aadb43e | -6.0674 | -48.0569 | 2024-11-30 01:30:00 | GOES-16 | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | 70.9 |
| 8d9751b1-ca82-37d9-8a97-9242a9c77053 | -4.6051 | -47.0079 | 2024-11-30 01:30:00 | GOES-16 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 153.5 |
| 8c1cf9cf-10a7-345f-adb5-8349fc4d7ae6 | -4.6052 | -46.9859 | 2024-11-30 01:30:00 | GOES-16 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 96.4 |
| 9378e1d8-d28e-3c86-806a-ce5527a10571 | -6.0862 | -48.0339 | 2024-11-30 01:30:00 | GOES-16 | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | 133.2 |
| dfa03da0-3428-3e51-96e1-f08f86b0fe85 | -6.0676 | -48.0352 | 2024-11-30 01:30:00 | GOES-16 | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | 89.2 |
| 73354157-4854-3d4c-9be1-af488d136666 | -3.1481 | -53.8233 | 2024-11-30 01:30:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 60.9 |
| 9574a215-630a-37c4-860d-6bb77ee3062b | -4.8525 | -41.2928 | 2024-11-30 01:30:00 | GOES-16 | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 125.5 |
| c81ee4b9-df38-3af4-9e4c-3fcfd7c74c56 | -3.4792 | -53.7941 | 2024-11-30 01:30:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 50.5 |
| 64937cd9-5715-392d-a15d-a29cfc1590b0 | -3.4976 | -53.7935 | 2024-11-30 01:30:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 60.7 |
| 4a44e92f-1667-334f-87b4-670719d90361 | -6.9344 | -43.5401 | 2024-11-30 01:30:00 | GOES-16 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 118.2 |
| 51ec28df-f68a-38c9-b61c-c6a330c55a20 | -6.4474 | -35.0386 | 2024-11-30 01:30:00 | GOES-16 | BAÍA FORMOSA | RIO GRANDE DO NORTE | Brasil | 2401404 | 24 | 33 | nan | nan | nan | Mata Atlântica | 67.0 |
| 02b72646-fd8d-380f-8f12-435be9891be7 | -4.8715 | -41.2674 | 2024-11-30 01:30:00 | GOES-16 | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 148.0 |
| f4ce4512-592e-30bc-8468-1f311a0c5ac1 | -4.8713 | -41.2915 | 2024-11-30 01:30:00 | GOES-16 | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 677.0 |
| 4b3f93aa-1247-374f-8202-c385f089c26d | -1.2556 | -54.5589 | 2024-11-30 01:30:00 | GOES-16 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 59.0 |
| 62871453-2716-3d42-86f1-b1e0f9dccf45 | -4.6237 | -47.0069 | 2024-11-30 01:30:00 | GOES-16 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 264.3 |
| ae25c1be-68d1-3dc7-a05a-c3a0efe9a6b8 | -1.6777 | -45.7868 | 2024-11-30 01:30:00 | GOES-16 | CÂNDIDO MENDES | MARANHÃO | Brasil | 2102606 | 21 | 33 | nan | nan | nan | Amazônia | 44.6 |
| 3b6e8be9-12e0-3673-a975-37a1a6cf3064 | -3.4791 | -53.8142 | 2024-11-30 01:30:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 108.6 |
| 79bb5f4a-8c3d-3eb0-b3bc-a64b762303bf | -4.8901 | -41.2902 | 2024-11-30 01:30:00 | GOES-16 | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 347.7 |
| 0e7ee13f-b89d-39da-ad58-138a6a396cbc | -6.8965 | -43.5669 | 2024-11-30 01:30:00 | GOES-16 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 65.6 |
| f165a2c0-3395-3f00-b968-02b1a86a8d5b | -3.148 | -53.8434 | 2024-11-30 01:30:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 58.4 |
| ef565a26-3f8e-35fc-bc5c-bd6130cc4a80 | -7.4991 | -34.8741 | 2024-11-30 01:30:00 | GOES-16 | CAAPORÃ | PARAÍBA | Brasil | 2503001 | 25 | 33 | nan | nan | nan | Mata Atlântica | 63.6 |
| 1ce20e10-6fb6-35b0-8226-ff4f03fb9395 | -3.2406 | -53.6393 | 2024-11-30 01:30:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 64.2 |
| 6a5ec9a5-49ac-36dc-8d4b-3e09d6f13eb2 | -2.0347 | -50.7765 | 2024-11-30 01:30:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 39.9 |
| 268c2a52-1add-3fc2-af4a-9dc713ebb4a0 | -7.4987 | -34.9017 | 2024-11-30 01:30:00 | GOES-16 | CAAPORÃ | PARAÍBA | Brasil | 2503001 | 25 | 33 | nan | nan | nan | Mata Atlântica | 66.0 |
| f722381e-e051-32dc-9d17-a2312a475b02 | -1.4379 | -55.2533 | 2024-11-30 01:30:00 | GOES-16 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 54.3 |
| b7c600fc-73cc-390e-9bec-d9a5be026770 | -3.9886 | -41.5165 | 2024-11-30 01:30:00 | GOES-16 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 103.1 |
| c3ab3b43-3038-3814-970c-787c682e1a7f | -6.8967 | -43.5436 | 2024-11-30 01:30:00 | GOES-16 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 146.5 |
| 37177612-68da-3e5e-b35d-056ff06c36cc | -3.2591 | -53.6186 | 2024-11-30 01:30:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 64.6 |
| 69a7fee0-ba06-3197-ae88-b0ecb2e3fd1b | -3.259 | -53.6388 | 2024-11-30 01:30:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 154.0 |
| 896366d2-d2e6-3a6d-b649-ba515b2bae96 | -4.8523 | -41.317 | 2024-11-30 01:30:00 | GOES-16 | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 140.5 |
| 827f8430-23f9-34c0-acc0-c3bae751a1c7 | -3.9699 | -41.5176 | 2024-11-30 01:30:00 | GOES-16 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 114.6 |
| 62dcc6df-1d02-3716-8408-a1a894d4657f | -1.6419 | -53.8731 | 2024-11-30 01:30:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 59.2 |
| e10a1371-d165-3933-afb2-737e6c57bbe4 | -3.3998 | -50.6573 | 2024-11-30 01:30:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 48.4 |
| 90529eae-b849-3ef3-90b5-ef1d8fa167c8 | -3.6758 | -47.1176 | 2024-11-30 01:30:00 | GOES-16 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 158.3 |
| f3d433f9-0a9b-328f-b6de-5238ba7cf7b7 | -3.6757 | -47.1395 | 2024-11-30 01:30:00 | GOES-16 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 155.1 |
| 95768c05-c02f-3c16-9d60-85c13a12a64f | -17.6651 | -57.585 | 2024-11-30 01:30:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 79.4 |
| 17469e51-6ab3-3401-9150-1b146d3e16ff | -6.9153 | -43.5652 | 2024-11-30 01:30:00 | GOES-16 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 173.8 |
| 945a719d-8a1a-347b-9a19-3892a8baa8ee | -3.4975 | -53.8137 | 2024-11-30 01:30:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 95.0 |
| de00ed7a-1898-3ad6-8485-37d30ffbf0f0 | -6.086 | -48.0557 | 2024-11-30 01:30:00 | GOES-16 | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | 108.4 |
| cee61f44-ab05-3d1f-b687-2d3d1b6aeeb9 | -6.4477 | -35.0111 | 2024-11-30 01:30:00 | GOES-16 | BAÍA FORMOSA | RIO GRANDE DO NORTE | Brasil | 2401404 | 24 | 33 | nan | nan | nan | Mata Atlântica | 60.5 |
| 6b2f8bdb-de2c-3b6e-89e6-6b21faabd830 | -6.9341 | -43.5634 | 2024-11-30 01:30:00 | GOES-16 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 73.8 |
| 80ea7de5-77a2-3c8d-a45c-a2a9bc23fe46 | -17.6654 | -57.5645 | 2024-11-30 01:30:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 93.3 |


[Clique aqui para ver as próximas entradas](README7.md)
