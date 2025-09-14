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

## Dados Diários - Página 55

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| bce67301-e612-3120-a298-28eba2a29187 | -12.68602 | -54.67973 | 2025-09-14 05:08:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 011cbc63-af6b-34dc-ac4f-a3d72b048e81 | -11.47387 | -50.77615 | 2025-09-14 05:08:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 55fa6355-c0d2-3e28-afa0-902b7adec647 | -12.76987 | -48.02226 | 2025-09-14 05:08:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 4f8ddcec-7532-35f1-87cd-c8cd05957a24 | -11.27517 | -51.10898 | 2025-09-14 05:08:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 62135294-2651-34f7-87a3-236cdc57ea59 | -11.82199 | -50.48631 | 2025-09-14 05:08:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| a52da90e-a2ae-3770-ac9c-4be56446cac0 | -14.30968 | -46.08472 | 2025-09-14 05:08:00 | NPP-375D | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 45c19380-969a-307b-9e1b-101e7c4ebc1a | -11.24893 | -44.78038 | 2025-09-14 05:08:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 68.5 |
| 4b0d3a39-d7c9-387a-98f1-d611666ad389 | -12.68244 | -54.70376 | 2025-09-14 05:08:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 9.7 |
| f4a5b1b3-5652-3ff3-bebe-fd16d91f7200 | -12.69366 | -54.6768 | 2025-09-14 05:08:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 26.5 |
| 9bf390f8-5871-3c88-9c49-dadab0772390 | -12.68894 | -54.68427 | 2025-09-14 05:08:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 56.7 |
| c39ecfe0-1cff-37e9-92ac-acaecdea2c26 | -11.86421 | -50.46383 | 2025-09-14 05:08:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 6a448215-da74-3a81-8e70-e30d3583a701 | -14.20017 | -46.17584 | 2025-09-14 05:08:00 | NPP-375D | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 4.0 |
| db829db9-42d8-379e-b508-1d25e1bab825 | -11.28993 | -50.81342 | 2025-09-14 05:08:00 | NPP-375D | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 8.3 |
| d8779df5-e86e-3246-b97d-278378fa5a03 | -8.98788 | -45.77217 | 2025-09-14 05:08:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| c6e4cf87-de5e-308f-bf91-481a9443cef7 | -9.95553 | -55.08817 | 2025-09-14 05:08:00 | NPP-375D | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 70f9af5a-e188-39e1-a238-acac109a94b3 | -14.1539 | -46.25893 | 2025-09-14 05:08:00 | NPP-375D | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 4.4 |
| cc24feb6-25dd-30df-9138-be1fabe44b19 | -13.27968 | -51.69412 | 2025-09-14 05:08:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 9df4946d-222e-3fd1-890c-49ae42d8103b | -12.78097 | -48.02044 | 2025-09-14 05:08:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| fb12648d-495b-3941-bbcf-0debb32e44aa | -12.25895 | -46.78896 | 2025-09-14 05:08:00 | NPP-375D | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 3be24ba5-3b0c-3028-8e64-489e5203b2d9 | -13.8887 | -48.24757 | 2025-09-14 05:08:00 | NPP-375D | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 91866607-52ed-3be9-a91f-0b94980cddea | -14.19508 | -46.16569 | 2025-09-14 05:08:00 | NPP-375D | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 783b5de1-922c-3069-a444-c8463e1307a1 | -11.77978 | -46.62202 | 2025-09-14 05:08:00 | NPP-375D | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 376524d6-3bbf-3325-aaf7-ead589a90381 | -11.43949 | -50.47148 | 2025-09-14 05:08:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 8.4 |
| 68d89086-f063-3595-a615-4d1bce37aed6 | -12.69127 | -54.69281 | 2025-09-14 05:08:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 10.9 |
| 13920817-1e6b-32d0-b1bb-29d6830ed020 | -10.75613 | -44.77804 | 2025-09-14 05:08:00 | NPP-375D | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 93aed5c4-5054-3c16-a3de-ec83d9bd805f | -12.74811 | -48.02255 | 2025-09-14 05:08:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| cd7c7e02-0f60-3d11-91ac-0cd2c9fe1945 | -11.27886 | -51.11354 | 2025-09-14 05:08:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 99666bb5-7d33-3027-8bcd-5633df05ec66 | -11.13596 | -47.65561 | 2025-09-14 05:08:00 | NPP-375D | PINDORAMA DO TOCANTINS | TOCANTINS | Brasil | 1717008 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 7e774d78-338e-30e4-afc6-a8f637e1f57b | -10.89979 | -47.21525 | 2025-09-14 05:08:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 4.2 |
| b06d0819-863a-384d-be39-9bab9c60de24 | -10.88231 | -48.18744 | 2025-09-14 05:08:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 081cba16-efc5-303a-a4bf-a669307f8c31 | -12.67541 | -54.70268 | 2025-09-14 05:08:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 041c58c7-8bfe-3e58-bd6b-c1aeb5455fe6 | -10.32363 | -48.81804 | 2025-09-14 05:08:00 | NPP-375D | PARAÍSO DO TOCANTINS | TOCANTINS | Brasil | 1716109 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 5acfa253-1e4d-36c7-811c-60b26b34f47c | -13.54102 | -43.01165 | 2025-09-14 05:08:00 | NPP-375D | RIACHO DE SANTANA | BAHIA | Brasil | 2926400 | 29 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 6a6a02d0-a0f6-3dfa-850d-add49ee4475e | -12.9817 | -48.00719 | 2025-09-14 05:08:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 578bd29d-dc39-3215-b6db-6c31f43f5383 | -14.28655 | -46.12504 | 2025-09-14 05:08:00 | NPP-375D | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 24e448d9-674c-304a-a8d6-3d59922a7afb | -11.25095 | -44.77006 | 2025-09-14 05:08:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 26.0 |
| 5955d3ec-2656-33f8-91b1-9801ffe26498 | -14.16096 | -46.25082 | 2025-09-14 05:08:00 | NPP-375D | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 9def1cca-eac7-3f3e-bf1c-5d5aa8a795a1 | -10.76266 | -46.47806 | 2025-09-14 05:08:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| ff008b78-021a-35f0-b87c-0550200a41aa | -12.68483 | -54.68773 | 2025-09-14 05:08:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 27.1 |
| 1bdd3a88-04dc-34e4-bc73-b9392321c386 | -12.68954 | -54.68027 | 2025-09-14 05:08:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 26.5 |
| 0b2c3672-dd4b-342a-b7a9-34809918a836 | -12.87247 | -52.96353 | 2025-09-14 05:08:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 4fb28f43-4bb2-3544-a89c-a2813e4cf621 | -13.1816 | -55.62399 | 2025-09-14 05:08:00 | NPP-375D | SORRISO | MATO GROSSO | Brasil | 5107925 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| c48de1c5-5592-3861-a2a7-1cf850002808 | -8.10541 | -50.16647 | 2025-09-14 05:08:00 | NPP-375D | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| bca4e56b-cbb3-3e86-b3f1-467c45829771 | -12.70649 | -54.71139 | 2025-09-14 05:08:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 7.3 |
| 01e3c930-d177-3389-98c1-20a44b0337b0 | -10.76964 | -44.77973 | 2025-09-14 05:08:00 | NPP-375D | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 9a2d089c-e685-3e84-9b1f-386f6f1aee89 | -12.66312 | -54.68853 | 2025-09-14 05:08:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 26.0 |
| b0c80540-e4fa-35ae-b243-fbf65ed7697b | -10.97466 | -49.59365 | 2025-09-14 05:08:00 | NPP-375D | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| ff1deab5-a4e4-3f32-a52d-b606f8a38363 | -13.94435 | -44.84641 | 2025-09-14 05:08:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 25.9 |
| afc031be-9e18-3876-95f4-4f75cceb6399 | -11.77918 | -46.62945 | 2025-09-14 05:08:00 | NPP-375D | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 0aa309ed-e6ea-31ae-a4bf-b4e5acaf5a81 | -12.93985 | -54.73965 | 2025-09-14 05:08:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 18.4 |
| d6966c84-8d87-3ceb-9677-765b4812d318 | -12.12936 | -44.83979 | 2025-09-14 05:08:00 | NPP-375D | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 848d8803-e921-3ac5-893a-451f5c1b6497 | -11.13298 | -45.31679 | 2025-09-14 05:08:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 35f50e70-e1d8-3666-9d90-5a0becf065c5 | -12.97175 | -48.04529 | 2025-09-14 05:08:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 44dbcfe5-2034-376b-afdc-31d0f940d655 | -13.01027 | -46.75046 | 2025-09-14 05:08:00 | NPP-375D | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| b2f37adf-3661-3308-9cc5-5b33bc4a86d8 | -14.62126 | -52.02123 | 2025-09-14 05:08:00 | NPP-375D | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| a7c07b45-6582-359d-affe-e821ca1dbefc | -12.7703 | -48.01891 | 2025-09-14 05:08:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 45ba370d-c0e3-34ed-bfed-488f9b8a4437 | -10.89383 | -47.21819 | 2025-09-14 05:08:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 91edb804-7d91-30dc-ba80-eaa9c89904df | -10.13747 | -47.19451 | 2025-09-14 05:08:00 | NPP-375D | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| e8d2854c-2ac3-3659-ba07-0e1d7084f3d8 | -10.96201 | -49.56932 | 2025-09-14 05:08:00 | NPP-375D | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| fd102130-738f-3b09-b6b7-3f1c8cd0eea6 | -11.67028 | -46.50937 | 2025-09-14 05:08:00 | NPP-375D | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 8dd2e402-9272-3e70-8635-bc24acf80e52 | -8.76524 | -46.03761 | 2025-09-14 05:08:00 | NPP-375D | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 2ac4c72c-2e32-3637-8b1b-b8efd6cdf4d4 | -12.13634 | -47.60016 | 2025-09-14 05:08:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 803201e7-9d53-3c84-8093-a80f14f875fc | -11.35103 | -43.50269 | 2025-09-14 05:08:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 1cac8929-847f-3231-a762-ca8ac26e86fc | -12.77072 | -48.01555 | 2025-09-14 05:08:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 57e4ab1a-e8d4-3c95-8cb4-909d675a40b2 | -14.16095 | -46.25204 | 2025-09-14 05:08:00 | NPP-375D | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 237d7523-94e1-3454-b08d-6a18cd99ccc6 | -12.69479 | -54.69334 | 2025-09-14 05:08:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 8.9 |
| 39cee7a6-1458-3716-9596-fbbd8b11db7d | -11.36057 | -47.33104 | 2025-09-14 05:08:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 66fb5229-ab2f-35e3-908d-26e373017569 | -12.98118 | -47.9879 | 2025-09-14 05:08:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| bd263373-a48a-33e5-93eb-d81fe3c4895e | -13.02646 | -47.99771 | 2025-09-14 05:08:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 537c608c-75a1-31ac-b4b6-2a105aef6d06 | -14.62493 | -52.02578 | 2025-09-14 05:08:00 | NPP-375D | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 3b2b50e5-4ee6-3e45-bc33-cf4cbb9272e0 | -12.14351 | -47.58705 | 2025-09-14 05:08:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 2cd7c4bd-3ead-3266-ac0e-ddf86830d98c | -14.27979 | -46.13231 | 2025-09-14 05:08:00 | NPP-375D | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| a99d5b33-4994-3510-a334-81379cfa13f9 | -8.90721 | -46.16432 | 2025-09-14 05:08:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 0.3 |
| 2043ceaf-e2ea-3504-8770-cc737dde9807 | -12.76623 | -48.00804 | 2025-09-14 05:08:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 17b98556-c78c-3c11-9fc6-823e7145b894 | -12.676 | -54.69867 | 2025-09-14 05:08:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| fb3a99d9-3db5-305e-9e42-de1c57996b7c | -12.78263 | -48.00737 | 2025-09-14 05:08:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 835f517b-f975-37d6-946b-f6cea39b1e42 | -11.8688 | -46.76637 | 2025-09-14 05:08:00 | NPP-375D | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| d6c1cc61-bc64-33dd-8f33-e0eab6a2980a | -13.26012 | -51.68112 | 2025-09-14 05:08:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| df2b11a2-4a27-37c8-bf02-ed7f95f2c0ee | -11.46521 | -48.70219 | 2025-09-14 05:08:00 | NPP-375D | GURUPI | TOCANTINS | Brasil | 1709500 | 17 | 33 | nan | nan | nan | Cerrado | 25.8 |
| c9ed7651-5e0f-3f60-acad-3342b0d29df0 | -11.85914 | -50.46766 | 2025-09-14 05:08:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 22d302b9-1345-32a0-a2b8-9445adb3aa53 | -11.1443 | -45.32793 | 2025-09-14 05:08:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| de8cbef6-2919-3db9-a692-1168cf996145 | -12.78808 | -47.13907 | 2025-09-14 05:08:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| f72eb784-6af1-3bed-841d-22c75d24104b | -12.69008 | -54.70082 | 2025-09-14 05:08:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 12.4 |
| e5deda3b-ae96-39a9-864b-ad234dbba1cb | -9.85598 | -46.47779 | 2025-09-14 05:08:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 41e3bb12-1611-365f-aa76-ac4a6f2b1f88 | -12.67075 | -54.68559 | 2025-09-14 05:08:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 5890d661-35a6-3fa1-81ba-bd367d4ea270 | -12.68012 | -54.69519 | 2025-09-14 05:08:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 4.3 |
| a7e0e69a-cf68-3cb5-a528-7c4d4e2f659b | -11.78497 | -46.63016 | 2025-09-14 05:08:00 | NPP-375D | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| d27b06d7-c9e7-34cb-9828-cc79b8521764 | -12.94337 | -54.74017 | 2025-09-14 05:08:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 18.4 |
| 45079929-6a50-3216-87b6-16e11a4fe28e | -11.87015 | -50.48737 | 2025-09-14 05:08:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 21.6 |
| bbda9c6b-8e18-329c-8a44-0276012f74d3 | -12.70124 | -54.69838 | 2025-09-14 05:08:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 5.4 |
| d5cb21e8-3c1c-3c7e-b1e8-3a4eb7572eca | -12.76131 | -48.00393 | 2025-09-14 05:08:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 89d4937c-77cc-36d8-ae8b-e8cf6fa920d1 | -12.73083 | -48.03049 | 2025-09-14 05:08:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| e63c85d8-7305-3ad3-9337-6258c35b42c1 | -13.0167 | -46.74617 | 2025-09-14 05:08:00 | NPP-375D | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 655983a1-7e9a-356c-9ca6-aff4b1455b79 | -12.6643 | -54.68053 | 2025-09-14 05:08:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 16.6 |
| 66df2fbb-10ec-38e7-8cdb-70c140cd6147 | -11.25678 | -44.77637 | 2025-09-14 05:08:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 53.5 |
| 81a77839-2978-3539-875c-025a682eb1b4 | -12.69652 | -54.70586 | 2025-09-14 05:08:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 8.0 |
| 6faa27f3-56b6-3200-a015-8d43fef1cb58 | -14.17214 | -46.15533 | 2025-09-14 05:08:00 | NPP-375D | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| d6cb0636-c2ad-3183-9bff-2c7ff6a90aac | -12.97543 | -47.99027 | 2025-09-14 05:08:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| e6ae7f28-95ae-32cb-9810-424e724e98bd | -12.6561 | -54.66287 | 2025-09-14 05:08:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 63c3fac6-bd81-3361-82a0-1c2f4cef6ac1 | -12.669 | -54.67305 | 2025-09-14 05:08:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |


[Clique aqui para ver as próximas entradas](README56.md)
