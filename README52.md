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

## Dados Diários - Página 52

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 9ba08610-7b5f-37b4-b65f-404efaa9d598 | -12.94946 | -53.51175 | 2024-10-12 04:08:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 3.7 |
| b25acd5f-d3dc-306f-a74a-35d2a619c067 | -12.94918 | -53.51992 | 2024-10-12 04:08:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 11.1 |
| b2941d04-85cb-352c-9dbe-fe6215d7fd11 | -12.94866 | -53.54609 | 2024-10-12 04:08:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 5.0 |
| b0e40c4d-38d2-36af-a6f0-d2c87987bbd0 | -12.94866 | -53.51584 | 2024-10-12 04:08:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 6bfe6806-c6ce-38ba-a9be-b581f6942e18 | -12.94834 | -53.52405 | 2024-10-12 04:08:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 11.1 |
| ebc2b30e-c671-31c8-ab2e-8f51d8011c85 | -12.94785 | -53.51994 | 2024-10-12 04:08:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 11.2 |
| 03bb6f13-3e52-370d-b7c2-edbc084ea75f | -12.94749 | -53.52821 | 2024-10-12 04:08:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 19.8 |
| efd7038a-81ce-30c3-b728-3a33106fadcf | -12.94704 | -53.52409 | 2024-10-12 04:08:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 11.2 |
| 2919c7dc-d7e7-344f-8025-a4cf00823e9f | -12.94665 | -53.53234 | 2024-10-12 04:08:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 19.8 |
| bb65a501-f774-3e4b-ae07-19e387c299c3 | -12.94622 | -53.52826 | 2024-10-12 04:08:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 17.9 |
| 6f41858e-b7ef-3a9d-b394-5e0f7a9c9464 | -12.94581 | -53.53647 | 2024-10-12 04:08:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 10.8 |
| 19d99a60-cdd8-344f-9e85-fa68b95840da | -12.9454 | -53.5324 | 2024-10-12 04:08:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 17.9 |
| 4fbc1caa-060c-319e-a147-155fefa2951d | -12.94496 | -53.54062 | 2024-10-12 04:08:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 10.8 |
| d2164647-f9b5-39d4-b5cf-fa580faa1b62 | -12.94459 | -53.53652 | 2024-10-12 04:08:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 11.7 |
| 12a8dbae-ea28-3950-9203-c2a28c2f32aa | -12.94456 | -53.50651 | 2024-10-12 04:08:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 8d6dc304-d129-3d39-a949-376d612b947e | -12.94376 | -53.51054 | 2024-10-12 04:08:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 8594f680-5387-308c-801b-85a2f93c9d64 | -12.84761 | -53.51573 | 2024-10-12 04:08:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 3d539df9-c60d-3749-92b7-7527a35617da | -12.84677 | -53.51988 | 2024-10-12 04:08:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 0330b189-9c0a-35f8-a6b2-3f7d2ea22ae0 | -12.8464 | -53.51713 | 2024-10-12 04:08:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 0aa5b011-705e-3859-af02-c3a16a2a769c | -12.84592 | -53.52405 | 2024-10-12 04:08:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 872f592a-8b57-37a4-98fb-84e8b221ee94 | -12.84558 | -53.5213 | 2024-10-12 04:08:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| eee94549-fb4e-34ce-8532-3670ce4a2745 | -12.84506 | -53.52825 | 2024-10-12 04:08:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| ba82bc55-4f97-3add-9b56-b73a8580366c | -12.84476 | -53.52549 | 2024-10-12 04:08:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| f7991bd9-d79d-3b92-b793-1684fa603da4 | -12.84393 | -53.52971 | 2024-10-12 04:08:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 638135fe-17e5-32c3-95a1-5c511e91cca6 | -12.8419 | -53.51453 | 2024-10-12 04:08:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 7584f7b6-235c-31bb-9906-27f115d851bc | -12.8415 | -53.51177 | 2024-10-12 04:08:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 9c879e96-06ec-310d-893a-8e07c4f026ce | -12.84105 | -53.51868 | 2024-10-12 04:08:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 200207d7-8325-30c4-ac02-2d0036de9be6 | -12.84069 | -53.51592 | 2024-10-12 04:08:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| ae63e80a-5928-3f0e-9fab-c2a93c78ceb6 | -12.8402 | -53.52287 | 2024-10-12 04:08:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 6137a6da-faf4-38ea-9f22-d4bc123d7a90 | -12.83987 | -53.52009 | 2024-10-12 04:08:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 4fcb2eca-8018-3f54-8250-52beacd7e6bf | -12.83934 | -53.52708 | 2024-10-12 04:08:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| f4485ea8-94c9-3761-896b-e62f5a267fd0 | -12.83904 | -53.5243 | 2024-10-12 04:08:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 4be7aefd-28f3-3b81-980a-0e9de1abed16 | -12.83849 | -53.53126 | 2024-10-12 04:08:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 987e7154-76ea-31b4-95e0-06831d806369 | -12.83821 | -53.52852 | 2024-10-12 04:08:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 11bea9e6-46ff-3d05-be8b-bfd02810b978 | -12.83739 | -53.53267 | 2024-10-12 04:08:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 56ee002e-28e3-354f-b0de-5268ee7b67e8 | -12.83579 | -53.51058 | 2024-10-12 04:08:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| ae889f4d-2f71-3a15-b27d-b70cab29454d | -12.83497 | -53.51471 | 2024-10-12 04:08:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| d9d4972f-a334-33cf-9bf9-0ba40783de30 | -12.83415 | -53.51889 | 2024-10-12 04:08:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| abd43acb-ee76-375f-8b8a-61106bf00f3f | -12.83333 | -53.52309 | 2024-10-12 04:08:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 2dbffbae-05bc-3b21-8b95-d7e3750c99f1 | -12.83249 | -53.52732 | 2024-10-12 04:08:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 4779509b-236e-3a9b-9b0c-b2ab042dfd6d | -12.83168 | -53.53146 | 2024-10-12 04:08:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| ef75a00a-a1ae-3f1f-8295-c05c4becc2fc | -12.83089 | -53.50526 | 2024-10-12 04:08:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 6bd70a1d-7f94-3b25-ad2c-e19ebaedd93a | -12.83008 | -53.50938 | 2024-10-12 04:08:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a6d66734-27a7-32e2-a177-9569b8c1aca7 | -12.82926 | -53.51353 | 2024-10-12 04:08:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 16551577-ddb8-3cb0-b68a-ea1a37402558 | -12.82844 | -53.5177 | 2024-10-12 04:08:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 8e6accd0-36d9-3f62-9a68-9fe78a9512dd | -12.82761 | -53.52188 | 2024-10-12 04:08:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| d092dcb0-fb96-3882-ae9a-fec1763100ef | -12.82679 | -53.49591 | 2024-10-12 04:08:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| ff1de7c3-7f97-3715-841c-bfc20278dde0 | -12.82678 | -53.52611 | 2024-10-12 04:08:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 373d5473-3150-3abf-853d-4beabf80e732 | -12.82598 | -53.49999 | 2024-10-12 04:08:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 20d98496-2307-381f-8218-51fd53e45af4 | -12.82596 | -53.53026 | 2024-10-12 04:08:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| d2e0020e-b1f9-3c99-830f-686f1a6404d0 | -12.82517 | -53.50409 | 2024-10-12 04:08:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 341b3c8b-5a77-3152-8b7f-2db3f9b9975a | -12.82436 | -53.50822 | 2024-10-12 04:08:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| b29ee8b3-7796-3586-bd94-6860441f9c38 | -12.82354 | -53.51236 | 2024-10-12 04:08:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 5e6c144f-6879-3439-9099-687e3fd28d33 | -12.82271 | -53.51653 | 2024-10-12 04:08:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 8395ba4d-abb9-3c18-9c7b-810d993ffe64 | -12.82189 | -53.52072 | 2024-10-12 04:08:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| c971034c-e705-3f78-8b85-b58e535a46b5 | -12.82188 | -53.4907 | 2024-10-12 04:08:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 4ba47202-bb36-3aac-ae67-fa8d61621415 | -12.82107 | -53.49477 | 2024-10-12 04:08:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| ca669130-1514-3ff1-b38f-8351e154d50d | -12.82106 | -53.52492 | 2024-10-12 04:08:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 676e32e9-3311-382f-9ccf-d99a6d8dc66d | -12.82027 | -53.49884 | 2024-10-12 04:08:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 40ae8bfc-3c9b-3fc1-b40f-85f669684098 | -12.81946 | -53.50293 | 2024-10-12 04:08:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 874b93c3-ce55-316b-8d75-11646de02c96 | -12.81864 | -53.50706 | 2024-10-12 04:08:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| f548253f-8b8a-3b29-b141-b8d86095b48d | -12.81782 | -53.5112 | 2024-10-12 04:08:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| afeaa3c3-88d9-3ec2-9eca-b7b7b8c07e42 | -12.81699 | -53.51539 | 2024-10-12 04:08:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 445840dc-5e8a-3797-b855-4fad3b8957c5 | -12.81616 | -53.51959 | 2024-10-12 04:08:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| c56beca9-2fd9-36f4-87c2-344f404ee77a | -12.81616 | -53.4896 | 2024-10-12 04:08:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| bdef7cde-674a-376f-b65d-dc7610ac81c2 | -12.81535 | -53.49364 | 2024-10-12 04:08:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 27ee8dd2-b49c-3ec2-a382-0eb96108ab7c | -12.81534 | -53.52375 | 2024-10-12 04:08:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| e44e1d47-f1f9-352e-a963-9d8cdba87709 | -12.81454 | -53.49772 | 2024-10-12 04:08:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 25ab6cd8-fb9a-3f38-97ca-8173cbc23ea3 | -12.81373 | -53.50181 | 2024-10-12 04:08:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 7.9 |
| 5241f70c-1a93-3dc0-bd94-912ca77913ec | -12.81292 | -53.50592 | 2024-10-12 04:08:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 7.9 |
| ac05f35e-0b84-386e-88fb-9c8a353ec8da | -12.81209 | -53.51007 | 2024-10-12 04:08:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 12.2 |
| 34fe76a9-8dd0-317e-977c-0bad3d1066cb | -12.81126 | -53.51424 | 2024-10-12 04:08:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 12.2 |
| f2cae2f4-2c76-37c4-b744-eef147bf9c82 | -12.81043 | -53.51844 | 2024-10-12 04:08:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 6.8 |
| e087d35b-19cf-3627-87b4-03689b091a5b | -12.80962 | -53.52256 | 2024-10-12 04:08:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 6.8 |
| bf79bb1f-c686-3a5e-8603-697db58d24f5 | -12.80962 | -53.49256 | 2024-10-12 04:08:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 873f9e25-1e43-3da7-9d82-cbfdee7eb3ee | -12.80882 | -53.49662 | 2024-10-12 04:08:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 145139f6-7480-367c-80f0-b2d360c5cf9f | -12.808 | -53.50071 | 2024-10-12 04:08:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 7.9 |
| 3f59c6b6-e252-3873-8264-0d9fa1b13582 | -12.80719 | -53.50481 | 2024-10-12 04:08:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 7.9 |
| 92f7ce81-55ea-3670-a12d-cef077c0da28 | -12.80636 | -53.50896 | 2024-10-12 04:08:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 12.2 |
| 147fc71f-3fb8-32a1-be45-161c2207c4c2 | -12.80553 | -53.51313 | 2024-10-12 04:08:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 12.2 |
| 35b7ce7d-bed1-3c10-b178-5d72ad9acc3e | -12.80471 | -53.51727 | 2024-10-12 04:08:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 6.8 |
| e854dedb-9bd8-3153-9845-3c26e9b82136 | -12.80146 | -53.50369 | 2024-10-12 04:08:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 263fbc9c-27f6-3cee-acdf-6b136f7db827 | -12.80064 | -53.50784 | 2024-10-12 04:08:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 0db76ce6-75f1-3de6-8df5-bbf2ece12317 | -12.63989 | -53.11015 | 2024-10-12 04:08:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 80a20133-1358-3054-bca1-75c43218b1c9 | -12.63353 | -53.11285 | 2024-10-12 04:08:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 20473962-9c8c-35b9-b05c-c4e57d48aa8b | -12.58517 | -53.07435 | 2024-10-12 04:08:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| f5103b93-78b5-3e00-a202-3f3678cebe0c | -12.58443 | -53.07814 | 2024-10-12 04:08:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 0a483cfd-4c43-3689-a6e8-3442ceaa4046 | -12.57959 | -53.07318 | 2024-10-12 04:08:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 75c6ff08-532c-3893-b67b-74af58bf8f5b | -12.57475 | -53.06822 | 2024-10-12 04:08:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 5954cc4f-c612-3d92-b47d-92c8664c47a1 | -12.57401 | -53.07199 | 2024-10-12 04:08:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c8937c33-0638-3366-af5d-8718b950978a | -12.57104 | -53.08713 | 2024-10-12 04:08:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 19639da6-f529-3d93-906e-4f3023980616 | -12.56917 | -53.06709 | 2024-10-12 04:08:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| be4ad154-0809-37ff-b609-9d49c327ded1 | -12.56546 | -53.08596 | 2024-10-12 04:08:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| aeb3a8f1-154f-37a0-96da-fd796143bd7d | -12.56211 | -53.07343 | 2024-10-12 04:08:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ec1356f8-0e50-32c6-938a-fde192bbb333 | -12.56137 | -53.07719 | 2024-10-12 04:08:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d466a9f2-19f7-39c8-9bd5-c74eb74b8b09 | -12.56062 | -53.08099 | 2024-10-12 04:08:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d040fb83-88b2-312d-b5bb-a7e418fe468d | -12.55987 | -53.0848 | 2024-10-12 04:08:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ca1f89b6-5eea-3fea-ac10-ba0c242bf0d5 | -12.52159 | -53.21939 | 2024-10-12 04:08:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 62919cbd-e9e5-3b89-b02f-297a7c28131e | -12.52081 | -53.22333 | 2024-10-12 04:08:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| c79352e7-3413-3cc3-96ee-17a20de163e8 | -12.51439 | -53.22609 | 2024-10-12 04:08:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |


[Clique aqui para ver as próximas entradas](README53.md)
