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

## Dados Diários - Página 21

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 740db4aa-534f-38f5-b0a5-bdb6b61ade73 | -13.7065 | -45.2454 | 2025-05-27 12:10:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 94.5 |
| 557b70b6-7d19-3d5c-b2e1-fe20b68f94fc | -7.9827 | -50.7201 | 2025-05-27 12:20:00 | GOES-19 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 103.2 |
| 3c924c6b-08f1-3b10-aab4-024551351576 | -13.7065 | -45.2454 | 2025-05-27 12:20:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 99.1 |
| 4855e3c4-c752-360a-bb8a-60a7970befbf | -12.3324 | -49.9857 | 2025-05-27 12:20:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 166.3 |
| f19b6b74-799b-3b8a-a23e-65c773e63335 | -12.3706 | -49.981 | 2025-05-27 12:20:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 196.2 |
| a20eb9ba-bb9b-33e0-b075-defe26629b35 | -12.3898 | -49.9786 | 2025-05-27 12:20:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 95.7 |
| abad3c0a-a90e-3190-bd22-bedb690c9c04 | -12.3703 | -50.0026 | 2025-05-27 12:20:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 115.8 |
| 00125f81-0ab1-3ea9-aa9c-1057a484a32f | -12.3703 | -50.0026 | 2025-05-27 12:30:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 136.3 |
| 5b43e435-19cb-3af6-947e-e3698e74119f | -7.9827 | -50.7201 | 2025-05-27 12:30:00 | GOES-19 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 95.0 |
| 07d13089-e50d-3829-a706-d41b15a27df3 | -12.3898 | -49.9786 | 2025-05-27 12:30:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 102.5 |
| b3015b74-c8a1-3742-a2dc-c271b2358a91 | -12.3324 | -49.9857 | 2025-05-27 12:30:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 235.0 |
| a18df6dc-b257-38fc-b20d-20d504bee168 | -13.7065 | -45.2454 | 2025-05-27 12:30:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 101.5 |
| eae34e5f-ba94-3480-ae1a-e474da406e02 | -12.3706 | -49.981 | 2025-05-27 12:30:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 283.7 |
| bd473f5e-8d8c-3723-8c04-f0d23a307555 | -12.3324 | -49.9857 | 2025-05-27 12:40:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 223.9 |
| 86d81e7d-2ef2-310a-8604-e764db866525 | -7.9827 | -50.7201 | 2025-05-27 12:40:00 | GOES-19 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 108.9 |
| 62e8aa29-6502-36da-bd1e-e4278eb2afde | -13.7065 | -45.2454 | 2025-05-27 12:40:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 129.8 |
| 4efdd9f5-11af-3be1-b312-03386c489413 | -12.3898 | -49.9786 | 2025-05-27 12:40:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 139.1 |
| 3f3958b9-9caf-3504-ac73-85f8862c1528 | -12.3703 | -50.0026 | 2025-05-27 12:40:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 132.2 |
| 419f06d0-a28a-395a-8d93-2cc5affdd00d | -12.3706 | -49.981 | 2025-05-27 12:40:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 279.0 |
| 3fb03f0b-276f-3945-9e9d-6113f5239311 | -13.7065 | -45.2454 | 2025-05-27 12:50:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 133.8 |
| 177391e3-d2f7-353e-8480-e178830a6f48 | -7.9827 | -50.7201 | 2025-05-27 12:50:00 | GOES-19 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 88.5 |
| b6feccd7-4462-377f-bc42-76c0a8ea5769 | -7.6236 | -45.7672 | 2025-05-27 12:50:00 | GOES-19 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 72.3 |
| c0c3a7eb-c6c0-3acf-bd6e-ce7501992a41 | -7.9827 | -50.7201 | 2025-05-27 13:00:00 | GOES-19 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 71.8 |
| 87d1ffbd-9abe-3b64-94cb-f21c81cd1c16 | -7.6236 | -45.7672 | 2025-05-27 13:00:00 | GOES-19 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 82.0 |
| 1d5b5d4d-18e8-3d27-b591-d047b0db2b52 | -13.7065 | -45.2454 | 2025-05-27 13:00:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 102.0 |
| 4556bc81-6eec-35d6-a725-0601a54f6905 | -7.9827 | -50.7201 | 2025-05-27 13:10:00 | GOES-19 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 97.6 |
| cdb546cf-4648-3c1e-994c-dce09cee23f4 | -13.7065 | -45.2454 | 2025-05-27 13:10:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 107.6 |
| ab5a960f-1317-3fd1-8f9b-e76071217c6f | -7.6236 | -45.7672 | 2025-05-27 13:10:00 | GOES-19 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 80.6 |
| 3a72ae31-12eb-3de2-a245-2e0370088c07 | -7.9827 | -50.7201 | 2025-05-27 13:20:00 | GOES-19 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 128.9 |
| aba0f37d-eb4f-3e04-bc9d-a61a5fbdced6 | -13.7065 | -45.2454 | 2025-05-27 13:20:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 92.3 |
| 6dbc755c-b9ed-3f5a-b8f8-eececa3d08ae | -7.6236 | -45.7672 | 2025-05-27 13:20:00 | GOES-19 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 115.1 |
| 692b7533-2fac-3dd4-a627-b168177a6521 | -13.7065 | -45.2454 | 2025-05-27 13:30:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 113.1 |
| 8feadf7a-07c7-36c2-9c1e-95ab930e7176 | -7.9827 | -50.7201 | 2025-05-27 13:30:00 | GOES-19 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 133.6 |
| 22b5c613-a0cf-3322-a7ba-9268546445af | -7.6236 | -45.7672 | 2025-05-27 13:30:00 | GOES-19 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 102.5 |
| b8efa44d-0681-3a5c-bb45-b20289116e45 | -6.6371 | -43.2167 | 2025-05-27 13:30:00 | GOES-19 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Caatinga | 74.8 |
| aba9706e-7df9-3adb-8d24-b912c429d9e2 | -7.6236 | -45.7672 | 2025-05-27 13:40:00 | GOES-19 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 113.8 |
| f9f6ee33-7f8a-3eb4-9e7d-a8fd1eb690e2 | -6.6371 | -43.2167 | 2025-05-27 13:40:00 | GOES-19 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Caatinga | 72.5 |
| 90aaeb74-0575-31b8-bbc0-a6c1252e495f | -13.7065 | -45.2454 | 2025-05-27 13:40:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 121.5 |
| b8ad7166-b514-33fb-ba4d-59a98341ac0e | -11.7802 | -46.4141 | 2025-05-27 13:50:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 85.8 |
| a93b31bf-c241-3f47-a48a-07abc957a930 | -11.761 | -46.4167 | 2025-05-27 13:50:00 | GOES-19 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 102.8 |
| 36876b81-5c37-320f-abef-e5b60e969ec4 | -6.6371 | -43.2167 | 2025-05-27 13:50:00 | GOES-19 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Caatinga | 80.8 |
| a039c774-10d2-3e4b-9bf6-6fcf7691e170 | -7.6236 | -45.7672 | 2025-05-27 13:50:00 | GOES-19 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 130.2 |
| 3288b3b5-7594-3e34-b15f-9a21b21fba58 | -13.7065 | -45.2454 | 2025-05-27 13:50:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 110.4 |
| f187308f-4178-3ba2-966c-3ec041bcd136 | -13.7065 | -45.2454 | 2025-05-27 14:00:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 115.1 |
| 9e4e41c8-720e-343f-a866-9043209ee13d | -7.6236 | -45.7672 | 2025-05-27 14:00:00 | GOES-19 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 139.3 |
| ebdaf91e-c27a-3f9b-8ddc-093ba41886b3 | -7.6239 | -45.7447 | 2025-05-27 14:00:00 | GOES-19 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 90.5 |
| 9ed45f4c-3bb9-3f2d-8f26-3ba021620388 | -6.3351 | -43.3598 | 2025-05-27 14:00:00 | GOES-19 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 135.8 |
| 0dba7344-a92c-311c-9d60-aed264c51703 | -6.3348 | -43.3832 | 2025-05-27 14:00:00 | GOES-19 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 105.2 |
| 22043269-b23a-3d90-ba5e-4de43914cde1 | -6.6371 | -43.2167 | 2025-05-27 14:00:00 | GOES-19 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Caatinga | 86.8 |
| 5ebf9c63-f2c3-3979-a2c5-5fb2aee4cfec | -11.761 | -46.4167 | 2025-05-27 14:00:00 | GOES-19 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 70.8 |
| 2c2340e9-2165-3a8b-a2cc-b8889e523cb2 | -13.0681 | -45.2823 | 2025-05-27 14:00:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 88.2 |
| 3a91d934-3e4d-35e4-8157-46f93e69b515 | -9.5525 | -48.0867 | 2025-05-27 14:10:00 | GOES-19 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 185.6 |
| 49aaecca-6ebd-3353-b471-31b4c49091ab | -6.6371 | -43.2167 | 2025-05-27 14:10:00 | GOES-19 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Caatinga | 77.3 |
| 66c0b18e-ea17-3623-802e-5dfdff999f6a | -7.6239 | -45.7447 | 2025-05-27 14:10:00 | GOES-19 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 80.9 |
| 20c6a21c-6f47-399e-9c14-4d58be4e519e | -6.3348 | -43.3832 | 2025-05-27 14:10:00 | GOES-19 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 99.4 |
| b513ec06-4211-35dd-b2b8-4c0dbf7dfaaf | -7.6236 | -45.7672 | 2025-05-27 14:10:00 | GOES-19 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 109.3 |
| 41740cba-ecbc-3847-86fa-550d410e2e5f | -13.7065 | -45.2454 | 2025-05-27 14:10:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 145.3 |
| fcc3cb87-5414-320e-b345-0e63e9211b04 | -6.3351 | -43.3598 | 2025-05-27 14:10:00 | GOES-19 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 112.6 |
| c553d479-c2db-3baf-978b-bbad755d1e7a | -6.3351 | -43.3598 | 2025-05-27 14:20:00 | GOES-19 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 95.8 |
| b0c3f9b7-c3cb-3e4d-879d-7ab2f640812f | -9.5525 | -48.0867 | 2025-05-27 14:20:00 | GOES-19 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 194.4 |
| a45092b6-6a93-3cae-b547-efd8246328c6 | -7.6236 | -45.7672 | 2025-05-27 14:20:00 | GOES-19 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 116.9 |
| b9a3b04f-5f2e-31ce-8a53-8170cb07ade1 | -6.6371 | -43.2167 | 2025-05-27 14:20:00 | GOES-19 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Caatinga | 75.3 |
| c6889cb6-7071-34b5-9633-58563b94c863 | -6.3348 | -43.3832 | 2025-05-27 14:20:00 | GOES-19 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 104.6 |
| e748c3a4-9ad6-397b-a9f7-300e3061eb8b | -7.6239 | -45.7447 | 2025-05-27 14:20:00 | GOES-19 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 73.2 |
| 30caf5c9-7d89-3280-b656-5da1bf014f20 | -11.1037 | -44.6315 | 2025-05-27 14:30:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 82.2 |
| 47a3ed83-5d37-3000-a77a-fcea556559b7 | -6.3351 | -43.3598 | 2025-05-27 14:30:00 | GOES-19 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 112.4 |
| b7e2a5d1-d88f-3e49-91a4-a22a78cbe093 | -7.6239 | -45.7447 | 2025-05-27 14:30:00 | GOES-19 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 71.0 |
| 7cd722cb-0a3b-3011-a0c2-f931ea09496c | -7.6236 | -45.7672 | 2025-05-27 14:30:00 | GOES-19 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 115.4 |
| 7f27d685-2428-358b-b164-77cc374cdd98 | -12.3706 | -49.981 | 2025-05-27 14:30:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 221.1 |
| 36d90d88-cf5e-3911-8ad8-76d1272f538d | -12.3324 | -49.9857 | 2025-05-27 14:30:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 222.0 |
| 7ae62b9c-6f3c-3896-8a29-4e586da07a69 | -6.3348 | -43.3832 | 2025-05-27 14:30:00 | GOES-19 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 97.3 |
| 680359ba-d902-3a7a-a396-8bca4d55892c | -9.5525 | -48.0867 | 2025-05-27 14:30:00 | GOES-19 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 80.3 |
| 74cdce4f-d66d-3b93-b7c8-482011a8b568 | -6.6371 | -43.2167 | 2025-05-27 14:30:00 | GOES-19 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Caatinga | 79.1 |
| 201b51a3-ed5c-335b-a8fa-f5976fee84c8 | -6.3163 | -43.3614 | 2025-05-27 14:30:00 | GOES-19 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 61.4 |
| 4e5cb247-e772-3a22-a9e3-4cdce31c0755 | -7.2548 | -43.4866 | 2025-05-27 14:30:00 | GOES-19 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Caatinga | 118.9 |
| f6011167-f114-3b81-8291-d1f8c1762997 | -12.3898 | -49.9786 | 2025-05-27 14:30:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 113.6 |
| bb8a2894-bd62-32e1-969c-20486d7ed05e | -12.3703 | -50.0026 | 2025-05-27 14:30:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 122.3 |
| 90a7114a-f967-392a-b860-958c29b9cb6e | -12.3703 | -50.0026 | 2025-05-27 14:40:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 114.1 |
| 0a8c10d2-e91b-3d31-894e-bda72c9a4f84 | -7.2548 | -43.4866 | 2025-05-27 14:40:00 | GOES-19 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Caatinga | 133.5 |
| 9fe804b3-6f60-317c-bb82-dd3e44c8d6a7 | -11.1037 | -44.6315 | 2025-05-27 14:40:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 72.9 |
| 590ab5a4-0fe8-3516-9c09-05c0b83a75e0 | -7.6236 | -45.7672 | 2025-05-27 14:40:00 | GOES-19 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 112.1 |
| de71df50-ff5b-38ce-85f3-443044fdfd9f | -12.3706 | -49.981 | 2025-05-27 14:40:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 208.9 |
| 57701660-05e1-3ccd-b0d7-7000d225c581 | -6.3351 | -43.3598 | 2025-05-27 14:40:00 | GOES-19 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 120.7 |
| 7dc16fbf-438c-31d6-898c-eaa3b3997f85 | -6.3163 | -43.3614 | 2025-05-27 14:40:00 | GOES-19 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 64.8 |
| 6dd2d2fc-e2a0-3b73-b1c3-d561637c14a1 | -12.3324 | -49.9857 | 2025-05-27 14:40:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 197.8 |
| bda888dc-dced-32dc-ac24-b1be4c91b015 | -9.5525 | -48.0867 | 2025-05-27 14:40:00 | GOES-19 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 66.9 |
| 67038847-848c-374a-8e77-6f202d613f8b | -17.9741 | -44.4077 | 2025-05-27 14:40:00 | GOES-19 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 109.4 |
| be29f7b5-7ffe-38bc-aa73-62bfbb7f4d5e | -6.6371 | -43.2167 | 2025-05-27 14:40:00 | GOES-19 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Caatinga | 78.2 |
| 4e68af68-2ed3-303e-aaee-b4f2f0d64d3c | -6.3348 | -43.3832 | 2025-05-27 14:40:00 | GOES-19 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 108.5 |


