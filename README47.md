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

## Dados Diários - Página 47

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 05d0c534-6f7f-3cd1-a4c6-9595d115a346 | -3.48141 | -48.44321 | 2025-08-19 05:16:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| d8a603b3-5f66-3ba3-bf16-7a5d8ca06ca9 | -8.8799 | -62.39383 | 2025-08-19 05:16:00 | NOAA-20 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 2.2 |
| bfbceeda-e243-30d2-b97e-c9f0219d7f36 | -9.16926 | -59.62145 | 2025-08-19 05:16:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 1a1d4451-119e-3cbc-aa42-2f207a785881 | -9.05316 | -50.18073 | 2025-08-19 05:16:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 78b12cb8-f779-3625-b8f9-7e2ba5d58532 | -9.1146 | -60.33136 | 2025-08-19 05:16:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.9 |
| c0bb9489-74bc-3314-b044-c434e87d395e | -3.98501 | -47.88613 | 2025-08-19 05:16:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f4a8b8bc-6015-31e4-95d8-82dd1bdc280e | -7.25497 | -50.17287 | 2025-08-19 05:16:00 | NOAA-20 | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| be19c43c-577c-3c44-b71f-b09ab44b3757 | -9.34323 | -48.51863 | 2025-08-19 05:16:00 | NOAA-20 | RIO DOS BOIS | TOCANTINS | Brasil | 1718709 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| dcf632fb-c143-3c8b-8933-2ee15022be44 | -8.96806 | -60.50294 | 2025-08-19 05:16:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.6 |
| ae683bda-5a98-3575-ba0d-cc6c7d09df31 | -9.19546 | -59.62893 | 2025-08-19 05:16:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 766d6516-be60-3951-8218-3aec9c794b19 | -7.78964 | -66.95824 | 2025-08-19 05:16:00 | NOAA-20 | PAUINI | AMAZONAS | Brasil | 1303502 | 13 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 0c21d4d1-4e49-3c6b-ade1-654e70296ec0 | -7.02435 | -59.67433 | 2025-08-19 05:16:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 547bb761-c8df-3837-889b-d60ffcc6157a | -7.59603 | -63.44725 | 2025-08-19 05:16:00 | NOAA-20 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 11a7ee84-334d-3b94-b992-9dac5e1821d2 | -5.75953 | -46.6728 | 2025-08-19 05:16:00 | NOAA-20 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| cfaa2002-e6cf-32d7-8579-f4c8a408f14e | -8.82692 | -52.04901 | 2025-08-19 05:16:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 2e798f54-5917-3881-aa56-cf34d88e75fd | -3.48199 | -48.43931 | 2025-08-19 05:16:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| d0250f42-1682-34bd-8fcb-cf2ae280b3ee | -7.25726 | -50.156 | 2025-08-19 05:16:00 | NOAA-20 | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 0f9a3951-265c-3538-9afe-d30a3361199d | -9.18252 | -59.64496 | 2025-08-19 05:16:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 4.7 |
| c7551cd7-2d92-334b-af01-d5c3863631b6 | -7.44781 | -63.0299 | 2025-08-19 05:16:00 | NOAA-20 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 7b319970-2b33-353e-b45e-e55f90cbebe7 | -9.07671 | -60.41895 | 2025-08-19 05:16:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 8ccba361-0686-3c89-a76c-d6157c7bc066 | -5.87545 | -48.12584 | 2025-08-19 05:16:00 | NOAA-20 | ARAGUATINS | TOCANTINS | Brasil | 1702208 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| b7308d0c-089d-3494-be88-8dc4860e0d4e | -9.04053 | -50.18045 | 2025-08-19 05:16:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 56c72a10-fdb3-3b14-8884-edd7f3b7ccb5 | -9.17036 | -59.61449 | 2025-08-19 05:16:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| d4e82355-e09f-3ce9-a74e-3115b66f7400 | -5.87013 | -48.12043 | 2025-08-19 05:16:00 | NOAA-20 | ARAGUATINS | TOCANTINS | Brasil | 1702208 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 13cdc273-fcad-3846-8ccd-8322da7e3ad0 | -7.25635 | -50.16273 | 2025-08-19 05:16:00 | NOAA-20 | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| b6d91eb8-2811-3de7-8de4-c823bb7f5f91 | -3.27989 | -48.81451 | 2025-08-19 05:16:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 291b05d2-76f5-3cd6-a6a8-418ce049971d | -3.98443 | -47.89013 | 2025-08-19 05:16:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| be841987-a10e-3823-a922-0d7ee5d02dec | -6.11655 | -53.8727 | 2025-08-19 05:16:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 88a976ef-b75e-3499-94ad-b72913abeb27 | -9.15112 | -60.82364 | 2025-08-19 05:16:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| b9eb3f2d-a6ba-3e23-9210-1e21b6d0f469 | -9.17643 | -59.61903 | 2025-08-19 05:16:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 32706f13-71ae-3b9b-8cc8-22b62b26f6b6 | -8.70409 | -50.68808 | 2025-08-19 05:16:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 443ab132-132b-3672-ba32-bb6d4f45ec4f | -9.18578 | -59.60268 | 2025-08-19 05:16:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| da6a651e-4ca0-38c5-8054-e2cba7254b18 | -6.63038 | -55.27593 | 2025-08-19 05:16:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 86563e21-4456-3e77-8a0b-a20f2120bf3e | -9.16981 | -59.61797 | 2025-08-19 05:16:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 9ed84808-15f8-30db-bbfc-7598c69348c8 | -5.75225 | -46.67746 | 2025-08-19 05:16:00 | NOAA-20 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| b96a9320-64b0-37a3-8c22-acacbe9dfdd3 | -9.23793 | -59.63926 | 2025-08-19 05:16:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ecc1a833-cf53-3784-8aca-1f3d79e19a68 | -7.59335 | -63.44535 | 2025-08-19 05:16:00 | NOAA-20 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| df3d11d7-7051-32cb-8a61-b4028bfb8190 | -7.44409 | -63.02927 | 2025-08-19 05:16:00 | NOAA-20 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 681f3e61-f7d8-3989-aec6-bdd8fd0506ae | -7.18334 | -59.54955 | 2025-08-19 05:16:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.3 |
| 709a028a-a2c4-3090-a59e-d4d2c1c3a84a | -10.58068 | -49.13715 | 2025-08-19 05:16:00 | NOAA-20 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 5784f951-da69-377d-8edb-b7d032f1c3c2 | -9.31178 | -56.07514 | 2025-08-19 05:16:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 7210bff3-dc50-3573-9e2f-b33719c377fa | -9.11792 | -60.33189 | 2025-08-19 05:16:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 50c8d74f-2c98-3f2b-a1c3-a627df26dea3 | -9.18197 | -59.64845 | 2025-08-19 05:16:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 68e5ee95-595d-37a2-9d36-1844feb0aa74 | -8.96919 | -60.49587 | 2025-08-19 05:16:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 679db227-6cbe-3faf-a813-718469f877e4 | -8.40011 | -49.50216 | 2025-08-19 05:16:00 | NOAA-20 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| fb9d135b-b5c8-390f-9cb2-b381b5d10613 | -7.92893 | -63.29051 | 2025-08-19 05:16:00 | NOAA-20 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| a42da6a4-fabf-3c94-a2cc-0096d4863186 | -9.19822 | -59.63293 | 2025-08-19 05:16:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| ca71b2d0-cb2e-3b5b-93bd-eab1a0e2bcf8 | -9.15054 | -60.8272 | 2025-08-19 05:16:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| b33ca6ca-98a1-33b5-8a33-425346883254 | -6.5452 | -49.51809 | 2025-08-19 05:16:00 | NOAA-20 | XINGUARA | PARÁ | Brasil | 1508407 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| b496583d-a483-3bcb-b2ba-0a619ea2f977 | -9.14777 | -60.82309 | 2025-08-19 05:16:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| cd7b542b-28d3-3028-811a-a1774f0c17a9 | -8.81873 | -52.0376 | 2025-08-19 05:16:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 0373209a-8e41-3108-817b-253010654076 | -9.07282 | -60.42193 | 2025-08-19 05:16:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| f812380e-46ae-363d-8f67-86dd11843f77 | -3.45522 | -48.96512 | 2025-08-19 05:16:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 5e1b3a4a-cd90-38d7-af51-d2ad8f14e2b2 | -6.13303 | -57.93136 | 2025-08-19 05:16:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 13d3fa5a-415e-3d83-8b9a-13841df7a726 | -5.97954 | -61.36226 | 2025-08-19 05:16:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| dd701e2f-4139-3cd8-ab8f-643cf410845e | -7.97141 | -55.30297 | 2025-08-19 05:16:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 7f365c41-981c-30c1-bedb-34def9c4e7f3 | -6.13248 | -57.93489 | 2025-08-19 05:16:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| cbd89441-f82d-3b5a-81f5-e90e1badab6e | -7.91843 | -63.28405 | 2025-08-19 05:16:00 | NOAA-20 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 0.4 |
| ff4d843f-e69e-36d1-8490-fa37b985e859 | -7.24964 | -50.17229 | 2025-08-19 05:16:00 | NOAA-20 | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 2ac7299c-384f-382a-a4a8-20c4192109ac | -4.01765 | -48.0683 | 2025-08-19 05:16:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| bfd2c09e-36b2-3d3a-9b7e-aa922a066818 | -9.7247 | -51.97464 | 2025-08-19 05:16:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 8b2b4771-2caf-3b0f-9670-3d104e0134d9 | -6.63411 | -55.27651 | 2025-08-19 05:16:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 9beeda3c-b873-3fcd-b414-0c2d7d443a92 | -9.18637 | -59.64201 | 2025-08-19 05:16:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 79dcf072-3c86-3493-9723-3f56a75f6ad0 | -5.88199 | -48.12261 | 2025-08-19 05:16:00 | NOAA-20 | ARAGUATINS | TOCANTINS | Brasil | 1702208 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 13e534d3-f4f7-31a8-aa19-cab337b5df78 | -5.75149 | -46.68296 | 2025-08-19 05:16:00 | NOAA-20 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 5a826286-6cb4-3cb0-adc8-a13ae9918ffe | -4.43 | -47.7593 | 2025-08-19 05:16:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 402a7d64-f6e9-3ac2-aca1-8a94515a6779 | -9.17921 | -59.64444 | 2025-08-19 05:16:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 4.7 |
| d0b3f7c2-0a07-32d9-bba2-45b3b07048a9 | -9.18142 | -59.65192 | 2025-08-19 05:16:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 8a1ad595-6fa8-3d32-b12c-66dc3cec3fb4 | -4.01806 | -48.06686 | 2025-08-19 05:16:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 5e059eb4-c079-3120-8f53-795db540c6b3 | -9.23021 | -59.64517 | 2025-08-19 05:16:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 24f70b70-1454-31b3-a588-030cec30a1d1 | -5.55127 | -49.07 | 2025-08-19 05:16:00 | NOAA-20 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a9005c28-9895-33a5-a9fe-cc8d3744c2af | -9.11128 | -60.33082 | 2025-08-19 05:16:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 8d4cd3f9-6e4c-37e9-9bcc-b26963ef8416 | -7.25453 | -50.17614 | 2025-08-19 05:16:00 | NOAA-20 | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 2d45dbd3-ef7c-3528-b720-f0b1c6940ad1 | -8.70365 | -50.69132 | 2025-08-19 05:16:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 19b0a2bf-d6b0-3d92-9446-80cd66d47398 | -6.16108 | -47.27646 | 2025-08-19 05:16:00 | NOAA-20 | CAMPESTRE DO MARANHÃO | MARANHÃO | Brasil | 2102556 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 395e0721-45e2-3ffa-b258-994e989cd3cc | -9.71984 | -51.97393 | 2025-08-19 05:16:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| ecb0acb8-b764-31e5-8afb-78ca366bbe9e | -5.55074 | -49.07365 | 2025-08-19 05:16:00 | NOAA-20 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f382aa22-3633-3edc-b38e-3a5b8daac6eb | -9.17866 | -59.64791 | 2025-08-19 05:16:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 32e417b2-1e25-3028-9c35-c5daef000821 | -7.59223 | -63.44659 | 2025-08-19 05:16:00 | NOAA-20 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| bf6b8d6b-73e2-3042-99d7-e1c938607724 | -7.78394 | -66.96263 | 2025-08-19 05:16:00 | NOAA-20 | PAUINI | AMAZONAS | Brasil | 1303502 | 13 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 1d5a8ee9-652d-3db8-aa3d-b96841bf08bc | -8.96863 | -60.4994 | 2025-08-19 05:16:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 1645118c-1eb9-32cf-b712-9a299c5aad8a | -9.1759 | -59.64391 | 2025-08-19 05:16:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 7ebeb8dd-2cbb-35c6-a897-70495b041caa | -7.30498 | -46.29424 | 2025-08-19 05:16:00 | NOAA-20 | NOVA COLINAS | MARANHÃO | Brasil | 2107258 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 2d4d65a9-5002-3d07-98fe-dd34b35dacfe | -9.17367 | -59.61502 | 2025-08-19 05:16:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| bd681c4e-8161-3613-9fdc-c6f84949924a | -5.88991 | -57.7524 | 2025-08-19 05:16:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 02b9dfb6-4b11-3df0-b0c1-c7dac69df76e | -4.43063 | -47.75497 | 2025-08-19 05:16:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 2f8bdea3-8879-36df-a1d1-86c406187d38 | -7.59291 | -67.37048 | 2025-08-19 05:16:00 | NOAA-20 | PAUINI | AMAZONAS | Brasil | 1303502 | 13 | 33 | nan | nan | nan | Amazônia | 4.1 |
| b082868b-823c-3c84-83b1-8d2b7db86189 | -7.25542 | -50.16954 | 2025-08-19 05:16:00 | NOAA-20 | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 1397510d-b05c-3bee-b962-e615a07276b2 | -4.14633 | -46.45495 | 2025-08-19 05:16:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |
| c5cdc602-b0dd-3a5e-8225-bf187b8c60a2 | -7.78871 | -66.96345 | 2025-08-19 05:16:00 | NOAA-20 | PAUINI | AMAZONAS | Brasil | 1303502 | 13 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 7fc7535b-92f6-37d9-b73b-81088403f47e | -9.05192 | -50.17822 | 2025-08-19 05:16:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e84e6fbf-ef8d-3590-8865-52ac87d5ba43 | -7.30717 | -46.28916 | 2025-08-19 05:16:00 | NOAA-20 | NOVA COLINAS | MARANHÃO | Brasil | 2107258 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| cfa29704-abb8-329c-89f8-45464794c32e | -9.22581 | -59.6516 | 2025-08-19 05:16:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 99e26aa0-72a0-3182-8f86-d8181124262a | -7.25589 | -50.16614 | 2025-08-19 05:16:00 | NOAA-20 | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 9ee6cc5e-c182-3aee-8a15-9b2a27c56cd1 | -8.61996 | -62.6257 | 2025-08-19 05:16:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.6 |
| b8d93354-6c2e-308e-8408-c16e5bd4fab6 | -5.98161 | -61.36343 | 2025-08-19 05:16:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| a3822ae1-53d1-35b9-8172-abff350184de | -9.19491 | -59.6324 | 2025-08-19 05:16:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 0054c37a-1cd0-35e5-95ac-51304e1d0207 | -9.19133 | -59.6321 | 2025-08-19 05:16:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 08d8c4c1-787d-3bc7-90b2-724b89220460 | -4.40453 | -48.94315 | 2025-08-19 05:16:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 947988d3-c07f-38ed-8994-58d1aee5221b | -7.21368 | -59.91495 | 2025-08-19 05:16:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |


[Clique aqui para ver as próximas entradas](README48.md)
