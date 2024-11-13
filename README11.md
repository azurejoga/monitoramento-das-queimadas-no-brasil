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

## Dados Diários - Página 11

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 946dde12-23d1-3449-8cd8-460e978cfd12 | -2.2479 | -53.7627 | 2024-11-13 02:20:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 56.8 |
| b58bb541-2d5b-398e-8cb1-c4ef93f0dbbf | -3.0689 | -50.3326 | 2024-11-13 02:20:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 52.3 |
| 86225f17-5eae-3d20-91b3-4899844b070b | -2.9924 | -51.045 | 2024-11-13 02:20:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 54.4 |
| bcd503cb-ba12-3f0e-8358-33a7108db28e | -4.658 | -47.4434 | 2024-11-13 02:20:00 | GOES-16 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 45.5 |
| 50ee873c-a87e-36f9-9030-35a8d951c1b7 | -1.6627 | -52.5357 | 2024-11-13 02:20:00 | GOES-16 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 62.2 |
| 99b94968-30f1-31e6-9e55-a922ebbfc667 | 2.689 | -60.9608 | 2024-11-13 02:20:00 | GOES-16 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 45.1 |
| 6ff3f1c1-3da9-31d4-b812-8e43c9891fc5 | -3.9483 | -48.1724 | 2024-11-13 02:20:00 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 44.0 |
| 9cbad250-c034-3cda-b732-0f7d0beeff0f | -2.248 | -53.7426 | 2024-11-13 02:20:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 73.0 |
| fb625e83-f885-355b-908b-b6e120251da0 | -2.7033 | -49.3513 | 2024-11-13 02:20:00 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 61.7 |
| 230a9c6e-f6f5-332f-9368-d37a31ed1ba0 | 1.0663 | -60.5985 | 2024-11-13 02:20:00 | GOES-16 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 77.6 |
| c29f77c1-7962-3869-8e11-4f7262595906 | 1.048 | -60.5986 | 2024-11-13 02:20:00 | GOES-16 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 96.4 |
| e650ca01-3939-3b13-a589-cf59fd7fc897 | -1.6627 | -52.5561 | 2024-11-13 02:20:00 | GOES-16 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 47.7 |
| ca0c2622-564c-3cc1-9fba-5ddedeb1bacf | -10.7425 | -49.5244 | 2024-11-13 02:20:00 | GOES-16 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 69.1 |
| 50dacf2f-a60b-3d2d-bbe0-2c367b4034e5 | 2.689 | -60.9797 | 2024-11-13 02:20:00 | GOES-16 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 45.7 |
| 313e29c1-6edf-3453-9112-bb44598914e8 | -4.6776 | -44.5861 | 2024-11-13 02:20:00 | GOES-16 | BERNARDO DO MEARIM | MARANHÃO | Brasil | 2101939 | 21 | 33 | nan | nan | nan | Cerrado | 59.8 |
| c59866f5-52f9-3603-abaa-62a0131c073f | -2.9925 | -51.0242 | 2024-11-13 02:20:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 56.4 |
| c54b79d7-2a4c-3aea-8020-f199288caf4b | -1.6444 | -52.536 | 2024-11-13 02:20:00 | GOES-16 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 55.6 |
| cfd19340-5d9f-38f7-99b6-1433aae7399f | -3.0504 | -50.3332 | 2024-11-13 02:20:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 78.8 |
| 2deec23a-64a4-318c-8af6-9d022191a82f | 1.048 | -60.5986 | 2024-11-13 02:30:00 | GOES-16 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 72.5 |
| 0a33ebf4-5526-3f3f-ad49-6c8743d8bd8c | -5.9398 | -39.6854 | 2024-11-13 02:30:00 | GOES-16 | MOMBAÇA | CEARÁ | Brasil | 2308500 | 23 | 33 | nan | nan | nan | Caatinga | 74.0 |
| 0dea630e-45eb-3176-b642-59159cb47b70 | 1.0663 | -60.6174 | 2024-11-13 02:30:00 | GOES-16 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 50.8 |
| 59941a4c-1db1-33a5-ae4a-2cd9f406dd8a | -4.658 | -47.4434 | 2024-11-13 02:30:00 | GOES-16 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 55.3 |
| cb8a8bef-1c47-3ce7-a92a-cf75ec3dc12d | 1.0663 | -60.5985 | 2024-11-13 02:30:00 | GOES-16 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 96.8 |
| 6caa585a-a901-3b05-b8f5-d4c14236e9ff | -1.6627 | -52.5561 | 2024-11-13 02:30:00 | GOES-16 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 66.3 |
| f029578d-d441-3e2a-8580-0d4f8a7fd0a7 | -1.6627 | -52.5357 | 2024-11-13 02:30:00 | GOES-16 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 70.3 |
| c1522043-3170-3129-bb16-224f649f61c2 | -3.0689 | -50.3326 | 2024-11-13 02:30:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 117.3 |
| e5e57cde-69da-33f5-88a4-a34453544f24 | -10.7425 | -49.5244 | 2024-11-13 02:30:00 | GOES-16 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 55.4 |
| b2a00439-e4d9-3202-bc67-a5e9bc40d4af | 2.689 | -60.9608 | 2024-11-13 02:30:00 | GOES-16 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 46.7 |
| 9061b64b-0ec9-377b-bb4c-47a95ef2bd22 | -2.2479 | -53.7627 | 2024-11-13 02:30:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 46.4 |
| 80c2d77b-7896-369d-bbf0-0c58ec467b2a | -1.6444 | -52.536 | 2024-11-13 02:30:00 | GOES-16 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 48.8 |
| 4f40fd19-a93d-35c3-883b-3c8ba5a4ece1 | -2.248 | -53.7426 | 2024-11-13 02:30:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 54.6 |
| 6e0b4489-a226-31aa-9e74-50c8556c565a | -4.6581 | -47.4216 | 2024-11-13 02:30:00 | GOES-16 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 77.9 |
| aa82f53d-adcb-3806-a016-10ee72ab6be7 | -3.0504 | -50.3332 | 2024-11-13 02:30:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 94.2 |
| c6c76607-01aa-37b4-be96-138b0bcdc624 | 2.689 | -60.9797 | 2024-11-13 02:30:00 | GOES-16 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 44.9 |
| c3d78f25-b6e3-3ebc-84fb-6e9668d8755e | -2.7033 | -49.3513 | 2024-11-13 02:30:00 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 53.6 |
| fc794e91-6ae4-3c88-8ef3-96a1fd123c43 | 1.0663 | -60.5985 | 2024-11-13 02:40:00 | GOES-16 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 89.1 |
| e9c37745-8951-37a9-89cd-f93957b04b99 | 1.048 | -60.5986 | 2024-11-13 02:40:00 | GOES-16 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 66.0 |
| 64536569-0c47-3d6b-a02a-ae1274032c98 | -3.0504 | -50.3332 | 2024-11-13 02:40:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 95.7 |
| 634314e7-3fc4-3ca3-8078-0513f698c7fa | -3.0688 | -50.3536 | 2024-11-13 02:40:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 55.3 |
| fe1072ee-16d1-3648-9162-edb7f7e466e9 | -3.0689 | -50.3326 | 2024-11-13 02:40:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 129.2 |
| c389aa77-e7dc-31c6-a007-a1fbd0ff6a11 | -4.658 | -47.4434 | 2024-11-13 02:40:00 | GOES-16 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 63.8 |
| e02d8d81-5043-34f6-b40d-d1091381d564 | -3.1096 | -54.3066 | 2024-11-13 02:40:00 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 51.3 |
| 75478822-43f2-3214-9a61-19170cad5240 | -2.9924 | -51.045 | 2024-11-13 02:40:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 55.6 |
| cb1ca58e-6954-3035-8f86-cbfda3dfc1bd | -2.248 | -53.7426 | 2024-11-13 02:40:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 56.6 |
| d0a3801a-a771-3151-b0ff-e2e43d8eb4ca | -2.9925 | -51.0242 | 2024-11-13 02:40:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 50.8 |
| d83a8eba-2065-396b-ad0f-d9472b850c01 | -1.6627 | -52.5357 | 2024-11-13 02:40:00 | GOES-16 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 52.9 |
| a68200a8-dc65-3786-a4ce-df5bc853c903 | -3.3518 | -48.9689 | 2024-11-13 02:40:00 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 32.4 |
| 3edcbc11-c51d-312f-9e38-ee8050b3e1e4 | -3.3519 | -48.9475 | 2024-11-13 02:40:00 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 68.4 |
| 94f2cb15-6427-3317-a78d-ca69975c74f4 | -4.6581 | -47.4216 | 2024-11-13 02:40:00 | GOES-16 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 77.7 |
| 7c914863-410d-3716-b494-9202fe7d36a2 | -3.3333 | -48.9695 | 2024-11-13 02:50:00 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 68.6 |
| fb47b3a0-18a8-3b86-9ef7-98bcbde4827b | -2.9924 | -51.045 | 2024-11-13 02:50:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 60.5 |
| 9dfb2806-7a87-301a-b72f-126a3748e6c7 | -4.6776 | -44.5861 | 2024-11-13 02:50:00 | GOES-16 | BERNARDO DO MEARIM | MARANHÃO | Brasil | 2101939 | 21 | 33 | nan | nan | nan | Cerrado | 61.5 |
| 1524a803-11c3-31cb-aefe-b87d61c7be6d | -2.2479 | -53.7627 | 2024-11-13 02:50:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 50.6 |
| a48c7b18-4ce8-3e83-954e-13b488860b33 | -3.0688 | -50.3536 | 2024-11-13 02:50:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 84.0 |
| 860d66fe-32ba-3a3f-802e-20800974a086 | 1.048 | -60.5986 | 2024-11-13 02:50:00 | GOES-16 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 66.4 |
| ac63f604-00d9-3cea-ae91-3039bdcce42e | -1.6627 | -52.5357 | 2024-11-13 02:50:00 | GOES-16 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 44.6 |
| 8c65aa84-050d-33e6-b1cf-61ebbea15265 | -3.0504 | -50.3332 | 2024-11-13 02:50:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 97.2 |
| 1349579b-4bbb-3bab-8a4e-996231a804cc | -3.0689 | -50.3326 | 2024-11-13 02:50:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 208.1 |
| bcc3bb79-6474-34c6-a811-1a4ce19180ac | -2.9925 | -51.0242 | 2024-11-13 02:50:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 58.1 |
| 8c34f678-e2e3-332e-9d9c-a46b047fadaa | -3.3519 | -48.9475 | 2024-11-13 02:50:00 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 318.9 |
| eaabeae0-7ab5-3878-911a-eb5400587b10 | -4.6581 | -47.4216 | 2024-11-13 02:50:00 | GOES-16 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 67.6 |
| 54b1705f-a772-316c-8c12-6b41c0040ae0 | -3.0874 | -50.3321 | 2024-11-13 02:50:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 61.7 |
| c6dc2faf-8780-3080-b8bd-3fa5ba64f532 | -3.3518 | -48.9689 | 2024-11-13 02:50:00 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 237.2 |
| 69504e7f-01ab-34e2-83ec-1416bbbfe8a9 | -4.658 | -47.4434 | 2024-11-13 02:50:00 | GOES-16 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 49.3 |
| 2e852afa-ed51-3946-b048-56fb894a70b0 | -3.069 | -50.3117 | 2024-11-13 02:50:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 51.3 |
| 1d348219-02a4-31af-846d-29852bed8691 | 1.0663 | -60.5985 | 2024-11-13 02:50:00 | GOES-16 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 73.3 |
| a857e3af-8e0b-34da-95cc-a016a038385a | -2.248 | -53.7426 | 2024-11-13 02:50:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 58.1 |
| de1f9f84-5c91-38cb-ae1e-2c902eccad41 | -3.3334 | -48.9482 | 2024-11-13 02:50:00 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 82.1 |
| 7281d1ba-9054-3b88-9ef2-90693a79f617 | -2.9925 | -51.0242 | 2024-11-13 03:00:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 54.9 |
| 833bfd9b-c17c-3b66-8c75-a8f49c6c25b6 | 1.048 | -60.5986 | 2024-11-13 03:00:00 | GOES-16 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 50.6 |
| b14394e0-7d9e-3988-8567-a0e4d4fa0bb1 | -2.9924 | -51.045 | 2024-11-13 03:00:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 59.8 |
| 86dbc5ce-c9ff-35d4-8a60-3f306a4353c8 | -3.0873 | -50.3531 | 2024-11-13 03:00:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 56.9 |
| 8b5d3cd3-5d82-34bf-bd23-15c8af353588 | -1.6444 | -52.536 | 2024-11-13 03:00:00 | GOES-16 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 39.1 |
| 57629ca9-0886-31e7-bdaa-0858695a79cf | -2.248 | -53.7426 | 2024-11-13 03:00:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 65.9 |
| 9327dfe9-0813-37cd-8846-4871b8476190 | -3.3518 | -48.9689 | 2024-11-13 03:00:00 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 223.8 |
| 29585ee0-b8c4-33d1-b58a-19823485ce6a | -4.6581 | -47.4216 | 2024-11-13 03:00:00 | GOES-16 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 53.6 |
| e6111dd5-294d-3008-95e1-c34286b63bc1 | -10.7425 | -49.5244 | 2024-11-13 03:00:00 | GOES-16 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 61.4 |
| 5b5c9276-4212-3b72-8038-530071c1a456 | -4.6776 | -44.5861 | 2024-11-13 03:00:00 | GOES-16 | BERNARDO DO MEARIM | MARANHÃO | Brasil | 2101939 | 21 | 33 | nan | nan | nan | Cerrado | 77.9 |
| f3b028dd-9d83-3918-b654-6e905331a360 | -3.3704 | -48.9469 | 2024-11-13 03:00:00 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 56.5 |
| 591f060b-2744-3573-b99c-c7c5f929ee33 | -4.6778 | -44.5633 | 2024-11-13 03:00:00 | GOES-16 | PEDREIRAS | MARANHÃO | Brasil | 2108207 | 21 | 33 | nan | nan | nan | Cerrado | 65.1 |
| 5ab77a63-13f5-3aae-8c30-588745174b18 | -2.2479 | -53.7627 | 2024-11-13 03:00:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 66.6 |
| f666d609-832a-3a45-8cbf-ea5134ceb658 | -3.3334 | -48.9482 | 2024-11-13 03:00:00 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 63.2 |
| 8d28a32e-af41-3139-a1cb-6ec63fa2b11d | -3.0504 | -50.3542 | 2024-11-13 03:00:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 52.3 |
| 8f295fbb-a667-3805-a4d2-8a7d555a7179 | -3.0688 | -50.3536 | 2024-11-13 03:00:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 98.2 |
| 5a710668-4d75-3496-b502-4999c804eddd | -3.0874 | -50.3321 | 2024-11-13 03:00:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 145.5 |
| a180beef-990c-34ff-b7e9-4c8af1a6c4fa | -3.3519 | -48.9475 | 2024-11-13 03:00:00 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 229.0 |
| 2cea843f-278d-3982-8285-b57f76b10082 | 1.0663 | -60.5985 | 2024-11-13 03:00:00 | GOES-16 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 58.2 |
| 27382554-0735-3972-b5b0-71afac1cf209 | -3.3703 | -48.9682 | 2024-11-13 03:00:00 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 51.2 |
| 768708e4-cb52-3156-b71a-e3285d1bf157 | -3.3333 | -48.9695 | 2024-11-13 03:00:00 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 61.9 |
| f0760a26-fed9-3968-b4e8-c19ebfe63080 | -3.0689 | -50.3326 | 2024-11-13 03:00:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 222.9 |
| 104cd83f-1aaa-3cd3-95c6-fae9c0a7f31a | -3.0504 | -50.3332 | 2024-11-13 03:00:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 130.3 |
| 14ff7c6b-eaaa-31de-b099-38ea7bf8b9ec | -3.34 | -48.95 | 2024-11-13 03:00:00 | MSG-03 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 15f4d568-d31d-3ce8-805a-69a7121c4bcb | -3.05 | -50.3 | 2024-11-13 03:00:00 | MSG-03 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e4b7aa56-3bb6-3f74-af60-f400f58342df | -4.6581 | -47.4216 | 2024-11-13 03:10:00 | GOES-16 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 46.6 |
| d719a04a-a964-3185-be35-466e1262f923 | -3.0874 | -50.3321 | 2024-11-13 03:10:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 87.7 |
| dbcdcffa-7ef6-33b9-a015-66043cf93459 | -2.9925 | -51.0242 | 2024-11-13 03:10:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 61.4 |
| 40769fc8-5eed-307a-8525-8c0ed1d246f6 | -2.7033 | -49.3513 | 2024-11-13 03:10:00 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 44.5 |
| fb3368e8-5a6e-3ac1-87dc-74796414996d | -3.3518 | -48.9689 | 2024-11-13 03:10:00 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 144.7 |
| 0e344810-a2b2-3fc6-8dd4-88fdfe7d5b17 | -10.7425 | -49.5244 | 2024-11-13 03:10:00 | GOES-16 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 66.2 |
| eadbaf78-814e-3a19-8105-c086232521a3 | -3.0689 | -50.3326 | 2024-11-13 03:10:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 175.7 |


[Clique aqui para ver as próximas entradas](README12.md)
