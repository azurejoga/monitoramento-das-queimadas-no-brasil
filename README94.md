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

## Dados Diários - Página 94

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| cf63190d-398e-3dd6-ad28-ba297b8a4033 | -11.5694 | -47.6081 | 2025-09-02 12:40:00 | GOES-19 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 111.0 |
| ffaa593a-0df4-324c-968c-12e608c40e57 | -11.9224 | -50.6153 | 2025-09-02 12:40:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 71.3 |
| 4869d3ec-54d2-3797-b400-10c49dab7e6e | -7.9351 | -46.4559 | 2025-09-02 12:40:00 | GOES-19 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 108.9 |
| 2722bbda-f5e1-3665-ba3e-4155c7268aa0 | -6.2038 | -43.3475 | 2025-09-02 12:40:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 97.5 |
| 0459b4e7-127f-3f9e-9d91-c6727f4f3aa1 | -8.8659 | -45.7788 | 2025-09-02 12:40:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 147.7 |
| f0dd81e4-c3a5-3b56-8ea6-59ea44de619d | -9.7483 | -48.9814 | 2025-09-02 12:40:00 | GOES-19 | DIVINÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1707108 | 17 | 33 | nan | nan | nan | Cerrado | 406.1 |
| b74a8aa5-26bb-3466-9d56-007894c771e0 | -9.7294 | -48.9834 | 2025-09-02 12:40:00 | GOES-19 | DIVINÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1707108 | 17 | 33 | nan | nan | nan | Cerrado | 167.4 |
| 6e29d86c-bc18-35f6-b0df-cbe7d31245a9 | -4.9122 | -43.2103 | 2025-09-02 12:40:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 73.1 |
| 7a478079-6fbd-356b-8df3-a086cb6c9a7d | -9.7294 | -48.9834 | 2025-09-02 12:50:00 | GOES-19 | DIVINÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1707108 | 17 | 33 | nan | nan | nan | Cerrado | 110.1 |
| c791bd72-c8a4-30ae-9db7-6758b00b505f | -5.8882 | -42.9988 | 2025-09-02 12:50:00 | GOES-19 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 71.5 |
| 0fca725e-deb0-3d0a-b56a-9b101dae6e94 | -5.3974 | -43.3867 | 2025-09-02 12:50:00 | GOES-19 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 74.5 |
| 5f08258c-52ff-303f-8c0b-9e777f57615a | -11.1037 | -44.6315 | 2025-09-02 12:50:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 112.9 |
| 8fd89455-e9d2-3175-9f91-8f02a545e848 | -8.8467 | -45.8034 | 2025-09-02 12:50:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 162.2 |
| c56ef69f-710d-3246-a6d0-63563216dd25 | -9.4984 | -46.4973 | 2025-09-02 12:50:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 70.6 |
| ecb6aad1-b267-332f-9f81-5c8f2ac11c48 | -10.0623 | -48.0978 | 2025-09-02 12:50:00 | GOES-19 | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 78.8 |
| 559a0b39-2edf-3047-b50d-5b7a1024bd74 | -11.6527 | -52.191 | 2025-09-02 12:50:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 111.4 |
| dd798c9d-ac2b-301c-8f32-a5e93ba58c7f | -7.9348 | -46.4783 | 2025-09-02 12:50:00 | GOES-19 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 67.3 |
| 757d8009-8e82-3027-902d-8ba8cc8c6267 | -9.7483 | -48.9814 | 2025-09-02 12:50:00 | GOES-19 | DIVINÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1707108 | 17 | 33 | nan | nan | nan | Cerrado | 322.1 |
| d03baaac-3b02-39db-8f90-88ccd2c55ce0 | -7.9165 | -46.4354 | 2025-09-02 12:50:00 | GOES-19 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 72.4 |
| e0b58dc2-9370-3b3e-8619-5221268d58bd | -8.8656 | -45.8014 | 2025-09-02 12:50:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 255.4 |
| b2ff4a95-ca84-38c3-99f7-e752524a62b5 | -5.9698 | -44.2923 | 2025-09-02 12:50:00 | GOES-19 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 147.5 |
| 2f6ad4c7-4b31-3aa7-856b-ba3e8a7c02e2 | -11.853 | -51.453 | 2025-09-02 12:50:00 | GOES-19 | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Cerrado | 74.1 |
| bbd81de9-83a5-3299-9b73-7fd649cb9611 | -6.9632 | -44.3477 | 2025-09-02 12:50:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 85.1 |
| 3a725d46-ccc7-3328-b046-984eaee1d9c8 | -11.653 | -52.17 | 2025-09-02 12:50:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 94.3 |
| bd280e51-ca9d-3065-86ee-b916267c2ef8 | -5.9511 | -44.2937 | 2025-09-02 12:50:00 | GOES-19 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 181.3 |
| c238e9c2-8418-3f58-9785-e41a602941f0 | -11.6717 | -52.189 | 2025-09-02 12:50:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 128.5 |
| ffedeb7d-3c80-3dbd-ac97-ba23bac969aa | -6.9754 | -43.2326 | 2025-09-02 12:50:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 198.1 |
| 30d64354-410d-3be0-89cb-916ca12b05fb | -9.4981 | -46.5197 | 2025-09-02 12:50:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 79.5 |
| f135b9d3-650f-3745-9a88-1141699002bf | -9.4794 | -46.4994 | 2025-09-02 12:50:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 80.2 |
| 6fd1681c-154c-3433-aec6-19f59acd9c62 | -11.5694 | -47.6081 | 2025-09-02 12:50:00 | GOES-19 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 105.8 |
| e524e887-9138-3145-a422-c14b3c8eab9c | -6.8724 | -45.8554 | 2025-09-02 12:50:00 | GOES-19 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 185.4 |
| 9978497b-e7fb-3cd6-9e02-b450b187ef29 | -8.847 | -45.7808 | 2025-09-02 12:50:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 76.8 |
| 05c433f9-e488-3b8b-b471-d04106760613 | -8.8638 | -50.5847 | 2025-09-02 12:50:00 | GOES-19 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 70.7 |
| 58c03719-cf45-3944-ad06-ab7ac9d26c57 | -13.325 | -46.956 | 2025-09-02 12:50:00 | GOES-19 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 71.1 |
| ea58cbd1-e7ed-3b6c-9f25-d294a3eb2fce | -11.9415 | -50.6131 | 2025-09-02 12:50:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 77.9 |
| 6563e13b-e57f-305a-9ff1-59a0ad5b079c | -11.8527 | -51.4742 | 2025-09-02 12:50:00 | GOES-19 | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Cerrado | 78.8 |
| 9cca5ca2-aab0-334d-ab13-80ab5a9f4cfc | -4.9122 | -43.2103 | 2025-09-02 12:50:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 71.7 |
| 092e4a1c-e068-3f6a-ae9c-8029221c4061 | -10.062 | -48.1197 | 2025-09-02 12:50:00 | GOES-19 | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 68.1 |
| e69106fe-e564-3ab2-ab25-e52600750683 | -4.9124 | -43.187 | 2025-09-02 12:50:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 98.7 |
| 6e48bc27-08df-38ed-932c-9baba7722d59 | -7.9163 | -46.4577 | 2025-09-02 12:50:00 | GOES-19 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 263.8 |
| ed28561c-54e1-34f3-b2e9-f00f1a390897 | -8.8659 | -45.7788 | 2025-09-02 12:50:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 120.6 |
| f12a9abb-c7a9-33ad-8cdd-0fd6f93cab41 | -9.4791 | -46.5218 | 2025-09-02 12:50:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 87.1 |
| 6f6c3758-89a7-399c-8177-f376c5a0f76b | -6.8911 | -45.8538 | 2025-09-02 12:50:00 | GOES-19 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 259.4 |
| a0992135-d830-3826-a593-e0bee654de40 | -5.9513 | -44.2707 | 2025-09-02 12:50:00 | GOES-19 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 80.1 |
| b637cdec-b5b8-3e56-87d8-05f9f6ba0a5d | -9.7485 | -48.9598 | 2025-09-02 12:50:00 | GOES-19 | DIVINÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1707108 | 17 | 33 | nan | nan | nan | Cerrado | 97.5 |
| a4d0910b-5c1f-305c-b7e6-57ba4da412f5 | -6.9942 | -43.2308 | 2025-09-02 12:50:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 137.5 |
| 857ae0f7-49af-3e9e-8ed8-d1d83e9d270d | -11.6715 | -52.21 | 2025-09-02 12:50:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 119.2 |
| 0ec85b83-0769-3ee7-9776-20903704adad | -7.9351 | -46.4559 | 2025-09-02 12:50:00 | GOES-19 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 147.2 |
| ab23f12f-1e1c-3a28-b42c-1bc3623d8905 | -11.8138 | -51.542 | 2025-09-02 12:50:00 | GOES-19 | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Cerrado | 64.3 |
| 08eafb97-a514-3dec-9370-a84b9af84b32 | -13.5364 | -46.991 | 2025-09-02 12:50:00 | GOES-19 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 70.6 |
| c5f0bba5-aea5-37a1-8a7e-6fd521d335ed | -11.672 | -52.168 | 2025-09-02 12:50:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 75.4 |
| 41557319-3398-3021-a466-16344d83ef54 | -11.1033 | -44.6548 | 2025-09-02 12:50:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 191.1 |
| 7c3e4bc5-e4fa-35a2-a4dc-c8a25a1898f3 | -11.8328 | -51.5399 | 2025-09-02 12:50:00 | GOES-19 | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Cerrado | 65.9 |
| 79c8a3fd-de9d-3abd-89c7-a7527e81915d | -11.8518 | -51.5378 | 2025-09-02 12:50:00 | GOES-19 | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Cerrado | 89.5 |
| 38c87fd0-7370-3478-a3df-e88a85c5a39c | -11.8527 | -51.4742 | 2025-09-02 13:00:00 | GOES-19 | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Cerrado | 96.7 |
| 8c6fddcc-d75f-3b9d-8dc7-4c6146441006 | -11.6715 | -52.21 | 2025-09-02 13:00:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 110.7 |
| 3d6e585f-ea1f-3919-aefc-4913fdd496df | -11.6717 | -52.189 | 2025-09-02 13:00:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 120.0 |
| 9929f445-3cb8-329b-96df-1932d97c06b5 | -5.8694 | -43.0003 | 2025-09-02 13:00:00 | GOES-19 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 69.0 |
| 5471e64a-8c2e-324f-9849-202d3164f735 | -11.4297 | -46.8223 | 2025-09-02 13:00:00 | GOES-19 | RIO DA CONCEIÇÃO | TOCANTINS | Brasil | 1718659 | 17 | 33 | nan | nan | nan | Cerrado | 69.1 |
| f34a380f-77a9-3f45-a6ac-f9e42a35a732 | -11.1037 | -44.6315 | 2025-09-02 13:00:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 124.1 |
| c0d53547-1bd9-3a05-a5d5-1265435ff22a | -5.9698 | -44.2923 | 2025-09-02 13:00:00 | GOES-19 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 104.5 |
| 7e634720-6805-3eb1-8871-c406997613ca | -7.9163 | -46.4577 | 2025-09-02 13:00:00 | GOES-19 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 306.8 |
| d9fced52-8e3c-3f30-97d4-623276701682 | -11.9415 | -50.6131 | 2025-09-02 13:00:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 84.2 |
| d96c572c-b3b2-3975-a06b-ffd290289ead | -4.9122 | -43.2103 | 2025-09-02 13:00:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 98.0 |
| f934fe79-f4d2-3f71-90fb-d9dcaa602809 | -11.1033 | -44.6548 | 2025-09-02 13:00:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 178.9 |
| 5c7555df-cf25-37b3-ba67-e03c84efe7b7 | -11.8328 | -51.5399 | 2025-09-02 13:00:00 | GOES-19 | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Cerrado | 74.2 |
| d9342091-d4d2-384b-930b-b3a2414efa27 | -11.8138 | -51.542 | 2025-09-02 13:00:00 | GOES-19 | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Cerrado | 69.3 |
| dce5a154-62eb-376a-a921-bd9a63b98cbc | -11.672 | -52.168 | 2025-09-02 13:00:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 70.3 |
| f7f71bc2-2681-3d3d-b8aa-914597204757 | -11.653 | -52.17 | 2025-09-02 13:00:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 89.6 |
| 145c79c7-5ff9-3b82-b81f-ccfe73e694b0 | -7.1089 | -44.7703 | 2025-09-02 13:00:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 69.3 |
| 9531c54e-1f52-3838-b916-7041ad63c7b4 | -5.9513 | -44.2707 | 2025-09-02 13:00:00 | GOES-19 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 76.5 |
| cd580a96-be9c-3c1d-897b-d9c499e07526 | -4.9124 | -43.187 | 2025-09-02 13:00:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 115.2 |
| 20df574e-1a2a-3de2-bd1e-8c95de5982bb | -14.0508 | -44.5543 | 2025-09-02 13:00:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 110.5 |
| fe43fdd9-cb9e-3c7a-b99f-d4b875beb295 | -4.8936 | -43.1882 | 2025-09-02 13:00:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 75.5 |
| bd263a91-3fb6-3005-bee6-d6fa848b90a0 | -6.9942 | -43.2308 | 2025-09-02 13:00:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 128.8 |
| 4ece7f6e-a3f4-3453-a289-c35b3f7f98f7 | -5.8882 | -42.9988 | 2025-09-02 13:00:00 | GOES-19 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 83.9 |
| 33758f21-df8b-33e1-811b-90bc959555f6 | -11.6527 | -52.191 | 2025-09-02 13:00:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 111.0 |
| fc971944-9a73-331d-a1ca-db4bc4b26b13 | -12.5769 | -44.7814 | 2025-09-02 13:00:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 87.9 |
| 9dae65cb-8d12-3bff-a335-fba9971e530c | -7.9165 | -46.4354 | 2025-09-02 13:00:00 | GOES-19 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 75.6 |
| 43a406b1-bf15-3f21-9ea7-81dbdf8317c5 | -16.2953 | -52.9443 | 2025-09-02 13:00:00 | GOES-19 | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 62.4 |
| c45328ba-15e3-3427-86ab-37b95255070e | -8.8451 | -50.5864 | 2025-09-02 13:00:00 | GOES-19 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 73.1 |
| dc351a3f-f083-3d9e-9143-df7ac04fd2f7 | -11.8518 | -51.5378 | 2025-09-02 13:00:00 | GOES-19 | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Cerrado | 147.6 |
| d0dc4392-40a3-3cb9-a674-d3f2af7e5a31 | -5.9511 | -44.2937 | 2025-09-02 13:00:00 | GOES-19 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 122.8 |
| 67ff965e-c0a2-33ce-8358-a326470f498f | -11.5694 | -47.6081 | 2025-09-02 13:00:00 | GOES-19 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 85.7 |
| 05ce99d6-ea58-3957-b4cb-d71db4185e51 | -11.6647 | -57.3533 | 2025-09-02 13:00:00 | GOES-19 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 91.9 |
| 5ae93997-2a0a-3d38-b9c6-d0fb10b53a5d | -10.0623 | -48.0978 | 2025-09-02 13:00:00 | GOES-19 | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 67.2 |
| 08286d5a-ceb6-3375-860c-9b8ec6f07b71 | -9.7485 | -48.9598 | 2025-09-02 13:00:00 | GOES-19 | DIVINÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1707108 | 17 | 33 | nan | nan | nan | Cerrado | 91.3 |
| b9edaf8a-ffa3-3a3e-8f10-c91afc28e135 | -9.7483 | -48.9814 | 2025-09-02 13:00:00 | GOES-19 | DIVINÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1707108 | 17 | 33 | nan | nan | nan | Cerrado | 292.5 |
| 9baba704-2287-38ec-b046-a4c9ee2e5079 | -7.9351 | -46.4559 | 2025-09-02 13:00:00 | GOES-19 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 168.0 |
| d90f99b8-b813-3973-9f60-a53e1b3c5858 | -9.7294 | -48.9834 | 2025-09-02 13:00:00 | GOES-19 | DIVINÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1707108 | 17 | 33 | nan | nan | nan | Cerrado | 144.4 |
| 3ac33dbd-f1bc-34e0-b07f-4a78dc46750d | -11.853 | -51.453 | 2025-09-02 13:00:00 | GOES-19 | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Cerrado | 75.4 |
| 55c24619-2182-36a6-9ceb-468547395884 | -7.9348 | -46.4783 | 2025-09-02 13:00:00 | GOES-19 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 105.0 |
| b7b5df41-bb17-3e24-8ece-279cfc77fe51 | -9.2633 | -47.1249 | 2025-09-02 13:00:00 | GOES-19 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 81.5 |
| 4ce16a28-c82a-34b2-ae8c-71d92a76f4d2 | -6.9754 | -43.2326 | 2025-09-02 13:00:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 221.0 |
| 5de47474-2905-30cd-b3c7-c16f86256732 | -8.8638 | -50.5847 | 2025-09-02 13:00:00 | GOES-19 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 89.1 |
| aa6aa314-041c-341e-8acc-df96a4993929 | -17.901 | -47.1801 | 2025-09-02 13:00:00 | GOES-19 | GUARDA-MOR | MINAS GERAIS | Brasil | 3128600 | 31 | 33 | nan | nan | nan | Cerrado | 106.1 |
| baee1f4f-15a7-3355-858f-0ea6b973e552 | -6.9942 | -43.2308 | 2025-09-02 13:10:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 167.4 |
| 28615d99-95e7-3bff-bd0e-9ab36a808751 | -8.8656 | -45.8014 | 2025-09-02 13:10:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 143.4 |
| e9105d7d-c84e-352c-8c62-45f91261c41c | -8.8467 | -45.8034 | 2025-09-02 13:10:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 121.3 |
| 36cf1507-a800-30da-ac8c-b88520db2878 | -8.201 | -49.5131 | 2025-09-02 13:10:00 | GOES-19 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 84.0 |


[Clique aqui para ver as próximas entradas](README95.md)
