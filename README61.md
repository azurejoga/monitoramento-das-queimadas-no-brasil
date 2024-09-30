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

## Dados Diários - Página 61

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| fbdd0f91-07de-32ca-8881-6414246ce087 | -3.0133 | -51.05093 | 2024-09-30 05:23:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 5074f40c-a33e-3d98-8254-3854fea7c404 | -3.01284 | -51.05406 | 2024-09-30 05:23:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 691b50f3-34fc-394e-8ac1-96c9d3c26b5a | -3.00859 | -51.047 | 2024-09-30 05:23:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 9c540507-abf9-35f7-9526-cf84c1c9862d | -3.00813 | -51.05011 | 2024-09-30 05:23:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| a2154c5f-d737-31c7-8eb3-ab79ff3c9f75 | -3.00767 | -51.05323 | 2024-09-30 05:23:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| b5b99c7d-5482-38ff-b267-7b01ed31778c | -2.88162 | -51.66228 | 2024-09-30 05:23:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| d9f2d358-1a9c-352a-b414-88c9f67526fc | -2.88079 | -51.66796 | 2024-09-30 05:23:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 53deea47-c56e-30ea-94d1-69a120e2b136 | -2.88028 | -51.6617 | 2024-09-30 05:23:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 63eeb5ac-1eed-3f49-87a0-9a0170b858a3 | -2.8794 | -51.66739 | 2024-09-30 05:23:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 7.4 |
| c869378e-c9d0-36f5-b58a-f1c031a211a7 | -2.87667 | -51.66151 | 2024-09-30 05:23:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 0afefe04-9100-3993-ad22-bac40f4205ef | -2.87584 | -51.66719 | 2024-09-30 05:23:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 016dd42c-dbbf-351b-b951-c1e7605a75f6 | -2.87272 | -51.67788 | 2024-09-30 05:23:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 22b22e03-37c3-3cb6-b66b-b31d948c2384 | -2.8121 | -51.94218 | 2024-09-30 05:23:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 63fc4ee5-2e51-3a21-b0be-0df85ef4c0a3 | -2.81148 | -51.93719 | 2024-09-30 05:23:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| b4c0d600-d3b9-3580-b970-d7131b4320c6 | -2.8107 | -51.94255 | 2024-09-30 05:23:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| cf3b3a96-641c-3772-ac80-e3f8c37a765c | -2.80725 | -51.94143 | 2024-09-30 05:23:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 744e9243-8de7-3ff8-97fd-20859fdb173f | -2.70738 | -51.34733 | 2024-09-30 05:23:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 4cbfee61-007d-3ef9-b908-3bf70c44f714 | -2.70694 | -51.35035 | 2024-09-30 05:23:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 4503ffa4-e968-3df4-b260-8edbdc9ccbaf | -2.70344 | -51.34383 | 2024-09-30 05:23:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| cbce9a40-86e9-3cd3-9657-354f0a27c942 | -2.70299 | -51.34679 | 2024-09-30 05:23:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 6ecac784-9b50-37d9-be0b-5951727df12c | -2.70277 | -51.34352 | 2024-09-30 05:23:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 0c0f3500-0318-351f-a8fb-cc83bb9ee88c | -2.70252 | -51.34979 | 2024-09-30 05:23:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 15a4b8b3-aecb-3049-8bdc-7a2b3c400d58 | -2.70234 | -51.34648 | 2024-09-30 05:23:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| a19d03c6-9c21-3b11-b2b4-07aa12574454 | -2.70206 | -51.35279 | 2024-09-30 05:23:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| ca4cbdac-1e36-38de-96e5-b361990c498c | -2.7019 | -51.34948 | 2024-09-30 05:23:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 18642365-3dc7-39e5-97c8-aad02fe1cd54 | -2.70146 | -51.35248 | 2024-09-30 05:23:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 163def8e-290f-3160-80a2-f97c71185f15 | -2.61393 | -51.21451 | 2024-09-30 05:23:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 7707970a-1d37-37a5-aa8c-0b93ace20677 | -3.82508 | -51.34287 | 2024-09-30 05:23:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 637335f7-1955-3d01-946e-a3023869186b | -9.90431 | -52.21162 | 2024-09-30 05:23:00 | NOAA-21 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 493f5049-88c0-3d09-860d-5bc2006f7162 | -9.90389 | -52.21492 | 2024-09-30 05:23:00 | NOAA-21 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| e1c6ebb8-09f1-31e9-a6dc-30d72330d9a6 | -10.23685 | -52.73438 | 2024-09-30 05:23:00 | NOAA-21 | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| b2e1fa5a-b9b0-3d49-bedc-a1a120197b3a | -10.23523 | -52.72719 | 2024-09-30 05:23:00 | NOAA-21 | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 5a32dc94-a933-3659-85c5-6a27e20fc29b | -10.23484 | -52.73033 | 2024-09-30 05:23:00 | NOAA-21 | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b6e9cc96-711b-3831-a840-156f207dcd04 | -10.23445 | -52.73343 | 2024-09-30 05:23:00 | NOAA-21 | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 7e6cf7b2-ee13-3669-b0f2-a93d3a14928b | -10.23367 | -52.73959 | 2024-09-30 05:23:00 | NOAA-21 | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 113dbb96-16e0-3b1e-b066-c9138399ddcf | -10.23296 | -52.72434 | 2024-09-30 05:23:00 | NOAA-21 | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 183ba64f-0c7b-31da-bff8-b293678feee6 | -10.23254 | -52.7275 | 2024-09-30 05:23:00 | NOAA-21 | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 2ee1ee07-dfec-3a1a-9162-87bdde8d4882 | -10.23213 | -52.73063 | 2024-09-30 05:23:00 | NOAA-21 | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| e00cb8a9-85e5-3234-86b5-8fcc73201338 | -10.23009 | -52.72649 | 2024-09-30 05:23:00 | NOAA-21 | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| ed8f19b6-c336-3dd4-8c85-7719d9889229 | -10.2297 | -52.72964 | 2024-09-30 05:23:00 | NOAA-21 | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 1ee12ab1-4bf1-3139-8a0f-33a8f7078082 | -10.22931 | -52.73273 | 2024-09-30 05:23:00 | NOAA-21 | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e23e2f93-48d5-3c6f-b643-c0addcbaad0b | -10.22741 | -52.72678 | 2024-09-30 05:23:00 | NOAA-21 | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| d25e0149-b9b5-34be-8e87-6c4dc1fb2fda | -10.22699 | -52.7299 | 2024-09-30 05:23:00 | NOAA-21 | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| d843ef44-4726-3d6a-b013-543833d32427 | -10.22352 | -52.7166 | 2024-09-30 05:23:00 | NOAA-21 | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| f25de1f9-2f48-3594-944e-0b47533221f1 | -10.22311 | -52.71973 | 2024-09-30 05:23:00 | NOAA-21 | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 9fb5b27a-e5c3-3ff8-9bf5-0d7becb7968a | -10.2227 | -52.72284 | 2024-09-30 05:23:00 | NOAA-21 | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 6cc2d7c6-e4fc-3549-88f5-1fa49cf5d11b | -10.22229 | -52.72596 | 2024-09-30 05:23:00 | NOAA-21 | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 98c6502f-3902-3d57-8497-c9ea09fcf3d8 | -10.22187 | -52.72907 | 2024-09-30 05:23:00 | NOAA-21 | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| eb0dd667-fce5-30b6-aa24-486051d59ef8 | -11.45587 | -53.83402 | 2024-09-30 05:23:00 | NOAA-21 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 56819944-ae32-3455-bed1-c088ebbdf93f | -11.45102 | -53.83334 | 2024-09-30 05:23:00 | NOAA-21 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 6.2 |
| f7e521e0-378c-3cec-91bb-a22fe9647dac | -11.0878 | -52.49456 | 2024-09-30 05:23:00 | NOAA-21 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 3f48d0ce-85c7-3c0e-ab32-7c61996fe5ff | -11.08737 | -52.49786 | 2024-09-30 05:23:00 | NOAA-21 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 20983fba-6389-31b1-b6d7-29963c51acb6 | -11.07995 | -52.42897 | 2024-09-30 05:23:00 | NOAA-21 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 0.4 |
| f4fc3748-7cbb-3171-93da-a7a5ed834879 | -11.07952 | -52.4324 | 2024-09-30 05:23:00 | NOAA-21 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 0.4 |
| d0e538f0-a4de-307f-b425-a07c17baf51c | -11.07909 | -52.43581 | 2024-09-30 05:23:00 | NOAA-21 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 799ecd91-8747-3c6f-9a70-5cab65f7dc0f | -11.07867 | -52.43919 | 2024-09-30 05:23:00 | NOAA-21 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 6c6ac4ce-a12c-392d-8561-a4e6b26f507e | -11.07824 | -52.44254 | 2024-09-30 05:23:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 76c2a5fb-8e37-3369-99a0-ebfa296b247c | -11.07782 | -52.4459 | 2024-09-30 05:23:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 4cca66db-2147-3f5f-bb70-0658b920a576 | -11.0774 | -52.44923 | 2024-09-30 05:23:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| f7d5a79f-2657-3a23-adb5-1e4dade93f98 | -11.07698 | -52.45258 | 2024-09-30 05:23:00 | NOAA-21 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 8dc77f2d-b42b-3393-a5c9-c2e0f487c31c | -11.07656 | -52.45592 | 2024-09-30 05:23:00 | NOAA-21 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| f1fd0a2e-090a-34ab-a430-a9e96ba6dd6e | -11.07613 | -52.45929 | 2024-09-30 05:23:00 | NOAA-21 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| d5796b14-b6e2-31ba-8cfd-4ccfd477250c | -11.07571 | -52.46264 | 2024-09-30 05:23:00 | NOAA-21 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b7b71e6e-af01-3a21-8fb5-810e426c72d6 | -11.07529 | -52.46598 | 2024-09-30 05:23:00 | NOAA-21 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 5fa197c2-8bc9-32cb-b654-7377e7479415 | -11.07508 | -52.42477 | 2024-09-30 05:23:00 | NOAA-21 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 0b963e40-24c4-3f13-b475-68c92de2ffda | -11.07487 | -52.46931 | 2024-09-30 05:23:00 | NOAA-21 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 513cdb13-5352-3052-803d-a8ecf00d7b8c | -11.07466 | -52.42819 | 2024-09-30 05:23:00 | NOAA-21 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| ab200a17-283c-31e1-a1dc-67955a7f281f | -11.07444 | -52.47267 | 2024-09-30 05:23:00 | NOAA-21 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ea934f16-bcae-3e33-8d20-d815d61b30c3 | -11.07423 | -52.4316 | 2024-09-30 05:23:00 | NOAA-21 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 04c0991f-81ab-37ad-ac54-0348c674e2d7 | -11.07402 | -52.47605 | 2024-09-30 05:23:00 | NOAA-21 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| cacc6508-240e-34cb-ac5b-fde3030f23cb | -11.0738 | -52.43502 | 2024-09-30 05:23:00 | NOAA-21 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| dbbe3748-35bb-39ac-8c49-661fced51e85 | -11.07337 | -52.4384 | 2024-09-30 05:23:00 | NOAA-21 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| ef1c5942-c9fd-3f60-980c-e635377256f5 | -11.07295 | -52.44178 | 2024-09-30 05:23:00 | NOAA-21 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 2ddd8869-3e0f-3698-b023-ffef5d58ca08 | -11.07253 | -52.44514 | 2024-09-30 05:23:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 1662059f-eae0-3ebc-bc53-ca060dc9696f | -11.0721 | -52.44852 | 2024-09-30 05:23:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 30.6 |
| c5ccbbc6-8cce-3260-9b2e-4e39a80a9c3c | -11.07167 | -52.45192 | 2024-09-30 05:23:00 | NOAA-21 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 30.6 |
| febb891e-7022-3970-8069-c38be148140f | -11.07125 | -52.4553 | 2024-09-30 05:23:00 | NOAA-21 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 29.0 |
| 0a4df702-a513-3a7a-9a30-cab6a1db3d6f | -11.07082 | -52.45868 | 2024-09-30 05:23:00 | NOAA-21 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 29.0 |
| 5fb9b38d-664f-3ce8-a003-dc877ed99be5 | -11.0704 | -52.46205 | 2024-09-30 05:23:00 | NOAA-21 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 6.6 |
| 89cde16d-17b7-3c4f-b8a9-6cfc229b8b86 | -11.07021 | -52.42064 | 2024-09-30 05:23:00 | NOAA-21 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 0.4 |
| ea72bdfa-cebd-3748-a12b-698285069afe | -11.06998 | -52.46539 | 2024-09-30 05:23:00 | NOAA-21 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 6.6 |
| ffc73cee-8591-3c5e-88ba-73ff928d950f | -11.06978 | -52.42404 | 2024-09-30 05:23:00 | NOAA-21 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 4f02476c-f4ad-346c-87dd-5b0f121c7cb1 | -11.06956 | -52.46873 | 2024-09-30 05:23:00 | NOAA-21 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 10b53b29-c4aa-3003-88bc-6960186f3fbc | -11.06943 | -52.51232 | 2024-09-30 05:23:00 | NOAA-21 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 6bfe8f73-8670-387d-9cfb-a0029e5da6a1 | -11.06936 | -52.42744 | 2024-09-30 05:23:00 | NOAA-21 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 2df88c6f-4f10-3786-8b18-3c215d982743 | -11.06914 | -52.47206 | 2024-09-30 05:23:00 | NOAA-21 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| fa9dbf39-f90b-39aa-8001-e13fc64b517d | -11.06893 | -52.43085 | 2024-09-30 05:23:00 | NOAA-21 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 571532a6-3230-30cf-9de5-68e160564a13 | -11.06872 | -52.47543 | 2024-09-30 05:23:00 | NOAA-21 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 5846f3ef-50d8-37ba-8373-4b409abaa63b | -11.0685 | -52.43427 | 2024-09-30 05:23:00 | NOAA-21 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 3a6a66a2-757f-3f80-a426-124ba60baa04 | -11.0683 | -52.47877 | 2024-09-30 05:23:00 | NOAA-21 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c74f327b-90ba-37db-aa19-24bd7d5f1f7f | -11.06807 | -52.43769 | 2024-09-30 05:23:00 | NOAA-21 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 7416b0e6-ad39-3e34-a6a0-e5f3c11a1e00 | -11.06788 | -52.48207 | 2024-09-30 05:23:00 | NOAA-21 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 151d3c6a-2c87-374b-a526-922939bcbbbc | -11.06765 | -52.44109 | 2024-09-30 05:23:00 | NOAA-21 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 67b6c538-8586-3c0f-8245-2a4651b26936 | -11.06722 | -52.44447 | 2024-09-30 05:23:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 48d1a82a-fb06-3e9f-9f08-437c46cea79a | -11.06679 | -52.44788 | 2024-09-30 05:23:00 | NOAA-21 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 30.6 |
| 233263de-9cc8-331a-bca1-a6a5ef881200 | -11.05452 | -52.45988 | 2024-09-30 05:23:00 | NOAA-21 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 11.3 |
| dca59c86-6c49-3088-8d93-a29244c1d096 | -11.0541 | -52.46329 | 2024-09-30 05:23:00 | NOAA-21 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 11.3 |
| 5b426d1a-205d-317d-b1eb-4f429021ddad | -11.05368 | -52.46663 | 2024-09-30 05:23:00 | NOAA-21 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| be7e8adc-085d-3655-839e-7ccb70e1144b | -11.05327 | -52.46993 | 2024-09-30 05:23:00 | NOAA-21 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| b76f212d-635e-3b5b-8d24-ea7cbafb8f32 | -11.05286 | -52.47324 | 2024-09-30 05:23:00 | NOAA-21 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |


[Clique aqui para ver as próximas entradas](README62.md)
