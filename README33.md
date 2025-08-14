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

## Dados Diários - Página 33

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 0adcd9b0-d26f-3111-96a4-f445541882d6 | -15.58132 | -47.32574 | 2025-08-14 05:12:00 | NOAA-20 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 4b365cb1-0bf5-336d-93bf-a0e4e4d611be | -16.31334 | -52.9143 | 2025-08-14 05:12:00 | NOAA-20 | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 10f91222-797a-3c15-9a60-36591d5fd327 | -17.04964 | -51.7941 | 2025-08-14 05:12:00 | NOAA-20 | CAIAPÔNIA | GOIÁS | Brasil | 5204409 | 52 | 33 | nan | nan | nan | Cerrado | 8.9 |
| 98d8fe47-735a-35d4-af90-9e072df99ca9 | -16.2858 | -52.91494 | 2025-08-14 05:12:00 | NOAA-20 | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 3f83b605-3726-3b64-8a49-809c8e615621 | -10.02761 | -67.6445 | 2025-08-14 05:12:00 | NOAA-20 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 0.8 |
| cda8f0cb-2636-392f-82b4-e48ec49c4740 | -12.29971 | -50.01726 | 2025-08-14 05:12:00 | NOAA-20 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| c5a265f2-d4e1-328b-99f5-d3a6b8cf8129 | -10.06087 | -67.74722 | 2025-08-14 05:12:00 | NOAA-20 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 28f309be-4249-3636-8595-bed01b44517f | -15.68101 | -56.39359 | 2025-08-14 05:12:00 | NOAA-20 | NOSSA SENHORA DO LIVRAMENTO | MATO GROSSO | Brasil | 5106109 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 3509b915-f09b-3b09-96b8-557d12df36de | -11.03723 | -55.37605 | 2025-08-14 05:12:00 | NOAA-20 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 65d64c0a-1703-32a4-83dc-408be5a4bf4f | -11.04865 | -55.37352 | 2025-08-14 05:12:00 | NOAA-20 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| d6a3865c-6d89-36ab-b559-4064534a3f8f | -13.05258 | -57.10018 | 2025-08-14 05:12:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 1a6710db-35c5-36da-9cc3-e41d7b23b5dd | -13.07101 | -57.14141 | 2025-08-14 05:12:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 91639b3b-f534-3eed-bc79-f79a90248dc9 | -12.34859 | -49.92024 | 2025-08-14 05:12:00 | NOAA-20 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| bb9a98a0-1fcc-3bf0-8804-06410a6e85cd | -13.1154 | -57.14829 | 2025-08-14 05:12:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| e7dde6c4-d6e1-390c-8f90-148b230dbd51 | -10.02824 | -67.64107 | 2025-08-14 05:12:00 | NOAA-20 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 0.8 |
| a0055e95-6cb3-3487-a0a1-53954ee93594 | -14.32501 | -48.63954 | 2025-08-14 05:12:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 89c6489a-ad9d-35c5-b519-893017a070bd | -13.12962 | -57.14667 | 2025-08-14 05:12:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 6c5e9b32-6bda-31bf-b364-8afe73b2d74e | -9.61986 | -67.30537 | 2025-08-14 05:12:00 | NOAA-20 | SENADOR GUIOMARD | ACRE | Brasil | 1200450 | 12 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 0411568c-3e85-3de0-ac9a-018e0df23af1 | -13.0784 | -57.13872 | 2025-08-14 05:12:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 58863881-fc6e-3300-9fa0-54ec2c6ff771 | -11.6898 | -51.61829 | 2025-08-14 05:12:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| f3e22c65-9f3c-3afe-98cf-f6987744af84 | -14.36563 | -53.37422 | 2025-08-14 05:12:00 | NOAA-20 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| c8c3e329-5962-343d-964a-7ead1fe81b0f | -16.6674 | -49.34819 | 2025-08-14 05:12:00 | NOAA-20 | GOIÂNIA | GOIÁS | Brasil | 5208707 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 8ac4b647-8c6b-320a-902e-2e9a31f424d0 | -17.04474 | -51.79348 | 2025-08-14 05:12:00 | NOAA-20 | CAIAPÔNIA | GOIÁS | Brasil | 5204409 | 52 | 33 | nan | nan | nan | Cerrado | 8.9 |
| 42fbef43-c627-38a9-91dd-98ac8e044082 | -12.30086 | -50.00777 | 2025-08-14 05:12:00 | NOAA-20 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| d40f09a3-2d74-35ab-bf62-1decd40ab462 | -16.30381 | -52.91719 | 2025-08-14 05:12:00 | NOAA-20 | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 8edea9f8-f0b4-36ed-895d-6d9f6d0f704b | -16.3083 | -52.91789 | 2025-08-14 05:12:00 | NOAA-20 | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| e34dcd13-a996-3e03-a89f-cc5b4561bade | -17.05032 | -51.78836 | 2025-08-14 05:12:00 | NOAA-20 | CAIAPÔNIA | GOIÁS | Brasil | 5204409 | 52 | 33 | nan | nan | nan | Cerrado | 7.5 |
| 5be3f063-b17f-3a3b-bce0-e9a850f9d238 | -16.32122 | -52.9242 | 2025-08-14 05:12:00 | NOAA-20 | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 4.1 |
| dda6fa80-8560-3663-8d92-ee31dc21d5ed | -15.56936 | -58.71374 | 2025-08-14 05:12:00 | NOAA-20 | FIGUEIRÓPOLIS D'OESTE | MATO GROSSO | Brasil | 5103809 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 6fa9998a-be97-30fa-9d3f-7588f5f341c4 | -16.31885 | -52.92155 | 2025-08-14 05:12:00 | NOAA-20 | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 114a72b5-5294-306f-8fc2-fc5ef338b264 | -9.6146 | -67.30443 | 2025-08-14 05:12:00 | NOAA-20 | SENADOR GUIOMARD | ACRE | Brasil | 1200450 | 12 | 33 | nan | nan | nan | Amazônia | 0.6 |
| a5183808-1179-3201-ba3e-4c16084f47c8 | -13.05278 | -56.84267 | 2025-08-14 05:12:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 6244ae6e-5cb3-39f8-a6d2-91660974e217 | -16.30776 | -52.92216 | 2025-08-14 05:12:00 | NOAA-20 | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| c501bbae-e9f2-3234-91ba-bb18a33b23fb | -13.07896 | -57.13494 | 2025-08-14 05:12:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 734917b8-37a6-30ba-9f70-62b6167f8e11 | -12.30009 | -50.0141 | 2025-08-14 05:12:00 | NOAA-20 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| c9b7e0c0-58df-384a-a2b3-d076c500db03 | -16.3117 | -52.92713 | 2025-08-14 05:12:00 | NOAA-20 | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 802ba810-affc-33ad-b7a1-845f1720c01f | -16.32335 | -52.92217 | 2025-08-14 05:12:00 | NOAA-20 | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 6.3 |
| b2257116-50f7-327a-b09a-9fc1b4cc4cb8 | -16.26018 | -49.96653 | 2025-08-14 05:12:00 | NOAA-20 | AMERICANO DO BRASIL | GOIÁS | Brasil | 5200852 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 0dd79386-ecab-34e2-9e7e-ca050c7f15bc | -11.31892 | -55.20693 | 2025-08-14 05:12:00 | NOAA-20 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 526dd7c7-89a9-36e8-ac92-f1b56674aa24 | -16.31834 | -52.92572 | 2025-08-14 05:12:00 | NOAA-20 | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 2a9208ab-ece9-31ba-8c5e-50b151b47081 | -13.28551 | -57.25051 | 2025-08-14 05:12:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 5f00ec79-a558-3550-a9be-80d04cf089ce | -16.30885 | -52.91359 | 2025-08-14 05:12:00 | NOAA-20 | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| c19fbfb1-eb44-3bac-85cc-38227f23b00b | -15.69661 | -56.41352 | 2025-08-14 05:12:00 | NOAA-20 | NOSSA SENHORA DO LIVRAMENTO | MATO GROSSO | Brasil | 5106109 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 5078ac4d-64e7-3ed4-aeee-47fc9b61baa2 | -16.32176 | -52.91998 | 2025-08-14 05:12:00 | NOAA-20 | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 9.8 |
| 1be75d90-8c03-34a4-8893-3a8a284dd44c | -17.05456 | -51.79459 | 2025-08-14 05:12:00 | NOAA-20 | CAIAPÔNIA | GOIÁS | Brasil | 5204409 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| aa0fa119-8b87-3e57-97e1-37da65393ed0 | -12.30048 | -50.01093 | 2025-08-14 05:12:00 | NOAA-20 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 2d74086a-4271-31f9-8e19-ba36b768c71c | -13.27869 | -57.24941 | 2025-08-14 05:12:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 15659304-9739-3037-9e05-ec8cc57401c8 | -15.583 | -47.32555 | 2025-08-14 05:12:00 | NOAA-20 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 3217cb53-e4f0-3de7-9229-700de4b0e465 | -16.2903 | -52.91549 | 2025-08-14 05:12:00 | NOAA-20 | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| c8d49d54-97e8-3861-91ed-784d0cd0a90c | -14.31923 | -48.63848 | 2025-08-14 05:12:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 52af4f04-1010-3e31-b099-1a985c32eef4 | -16.30721 | -52.92645 | 2025-08-14 05:12:00 | NOAA-20 | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 8ebb79c5-5dfc-3d88-931e-7f8393817ce5 | -10.47383 | -61.32074 | 2025-08-14 05:12:00 | NOAA-20 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 671c788b-fc5e-3052-9a36-009702f1ded1 | -16.31278 | -52.91861 | 2025-08-14 05:12:00 | NOAA-20 | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 9e5b8dce-170a-30f6-8de2-1a58a557d38d | -16.30664 | -52.93097 | 2025-08-14 05:12:00 | NOAA-20 | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 9e958c19-f848-3467-995e-f771cda515c2 | -10.476 | -61.32973 | 2025-08-14 05:12:00 | NOAA-20 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 3a1081f0-287a-3c26-aed4-399b28879214 | -16.31673 | -52.92355 | 2025-08-14 05:12:00 | NOAA-20 | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| e7b9c179-3d55-3032-97af-72c649d6b8be | -16.31113 | -52.93161 | 2025-08-14 05:12:00 | NOAA-20 | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 7a38aae8-f6fb-3d66-bdf1-1839239fb371 | -16.31224 | -52.92287 | 2025-08-14 05:12:00 | NOAA-20 | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| d9a2ea12-828a-3185-b82e-2eecf4842e40 | -12.50663 | -57.78448 | 2025-08-14 05:12:00 | NOAA-20 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 68e5d8ab-9760-30c4-b7a7-86dc999d242d | -10.0586 | -67.74712 | 2025-08-14 05:12:00 | NOAA-20 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 17a43a56-c92a-3e8b-98e0-eef3c59bbe99 | -16.32068 | -52.92842 | 2025-08-14 05:12:00 | NOAA-20 | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 4.1 |
| fbabbdec-f039-3788-94b4-0fc31ccdfd5b | -13.12279 | -57.14561 | 2025-08-14 05:12:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 4d6926e8-0d51-3e70-bd08-33bbabc6be9a | -13.07605 | -49.33207 | 2025-08-14 05:12:00 | NOAA-20 | PORANGATU | GOIÁS | Brasil | 5218003 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| a097b42a-2da8-31ad-a0db-6b10591a71ae | -11.04144 | -55.37241 | 2025-08-14 05:12:00 | NOAA-20 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 7911b1b6-1d00-3ab9-92cc-4f7e7d502f12 | -12.34899 | -49.917 | 2025-08-14 05:12:00 | NOAA-20 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 17358425-f85c-38a7-89a8-6eb4e94bf9e1 | -15.30167 | -59.23719 | 2025-08-14 05:12:00 | NOAA-20 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 189d3e0a-87e8-3436-98d2-b62be359a52c | -16.31782 | -52.93006 | 2025-08-14 05:12:00 | NOAA-20 | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| b4029d28-c16e-3dea-a96a-f64bc2696db2 | -13.05271 | -57.09993 | 2025-08-14 05:12:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 3f95c1d7-dc9b-39e5-a0f7-e309329c37cf | -11.68458 | -51.6224 | 2025-08-14 05:12:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 83a2a295-7d84-3159-8d79-20d28b55fdba | -13.27529 | -57.24886 | 2025-08-14 05:12:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 4c246183-d3a2-34a7-96a3-3cb2a0f5f925 | -13.11881 | -57.14882 | 2025-08-14 05:12:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 2d109d3a-97b2-3a22-8d69-22c7fff37a69 | -16.31937 | -52.91724 | 2025-08-14 05:12:00 | NOAA-20 | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 6.4 |
| d4ce574a-79d4-3b6d-9d11-8aa1eb07a8e5 | -16.31619 | -52.92776 | 2025-08-14 05:12:00 | NOAA-20 | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| c6785ef2-9bd6-3143-8064-78d7f9816314 | -16.29481 | -52.91604 | 2025-08-14 05:12:00 | NOAA-20 | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 3e03b841-e763-3d57-9b48-d8873edebe2c | -15.57487 | -47.32535 | 2025-08-14 05:12:00 | NOAA-20 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 56fc71b7-8511-36f5-a1cf-d962524b260e | -15.57655 | -47.3252 | 2025-08-14 05:12:00 | NOAA-20 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 4.4 |
| e450859e-76f2-3050-a07f-11328d4fdbeb | -16.29985 | -52.91233 | 2025-08-14 05:12:00 | NOAA-20 | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 62fd9688-ff40-393d-bb9a-2b1294395538 | -13.11938 | -57.14507 | 2025-08-14 05:12:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 3.8 |
| c8296344-9057-3390-9cfd-541cf9a1bc50 | -16.30327 | -52.92146 | 2025-08-14 05:12:00 | NOAA-20 | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 1c27d60f-d9ff-3c1b-9cf1-04d7302bd248 | -16.31727 | -52.91932 | 2025-08-14 05:12:00 | NOAA-20 | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 2.9 |
| f866fb83-f9dc-37fc-800e-4e25021cbca5 | -12.34939 | -49.91376 | 2025-08-14 05:12:00 | NOAA-20 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 920cb876-b196-3761-92fc-e09020b75d59 | -22.85701 | -49.22496 | 2025-08-14 05:14:00 | NOAA-20 | ÁGUAS DE SANTA BÁRBARA | SÃO PAULO | Brasil | 3500550 | 35 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 15098333-5257-38ff-a9ae-ba563ac4b1ad | -22.55222 | -49.77541 | 2025-08-14 05:14:00 | NOAA-20 | SÃO PEDRO DO TURVO | SÃO PAULO | Brasil | 3550506 | 35 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 6728320d-8ca5-34b2-9394-065cfeadfdd6 | -21.7741 | -48.80003 | 2025-08-14 05:14:00 | NOAA-20 | IBITINGA | SÃO PAULO | Brasil | 3519600 | 35 | 33 | nan | nan | nan | Cerrado | 1.7 |
| f74b968b-1e46-3061-841e-8759273cfff4 | -22.66948 | -47.4596 | 2025-08-14 05:14:00 | NOAA-20 | LIMEIRA | SÃO PAULO | Brasil | 3526902 | 35 | 33 | nan | nan | nan | Cerrado | 8.7 |
| 1521a1b3-d8be-38b2-bd19-bbaa5ad3dcbb | -22.67635 | -47.45969 | 2025-08-14 05:14:00 | NOAA-20 | LIMEIRA | SÃO PAULO | Brasil | 3526902 | 35 | 33 | nan | nan | nan | Cerrado | 8.7 |
| ef8ff4de-cc26-36a7-8ddc-73b56ffe2759 | -18.54144 | -46.05592 | 2025-08-14 05:14:00 | NOAA-20 | VARJÃO DE MINAS | MINAS GERAIS | Brasil | 3170750 | 31 | 33 | nan | nan | nan | Cerrado | 3.2 |
| f81c7ce4-8e27-3dbd-b70d-27ae180f988e | -22.67071 | -47.46101 | 2025-08-14 05:14:00 | NOAA-20 | LIMEIRA | SÃO PAULO | Brasil | 3526902 | 35 | 33 | nan | nan | nan | Cerrado | 9.0 |
| 45961364-b1f6-3c26-8c28-85dbb9b981e4 | -21.01719 | -48.91925 | 2025-08-14 05:14:00 | NOAA-20 | NOVAIS | SÃO PAULO | Brasil | 3533254 | 35 | 33 | nan | nan | nan | Mata Atlântica | 10.2 |
| 697d8c53-80c5-363d-95bf-6f80b61beb1c | -17.86684 | -52.19709 | 2025-08-14 05:14:00 | NOAA-20 | SERRANÓPOLIS | GOIÁS | Brasil | 5220504 | 52 | 33 | nan | nan | nan | Cerrado | 7.5 |
| f7ad1360-930f-3a93-b6ec-31083338fb04 | -21.01648 | -48.91542 | 2025-08-14 05:14:00 | NOAA-20 | NOVAIS | SÃO PAULO | Brasil | 3533254 | 35 | 33 | nan | nan | nan | Mata Atlântica | 8.7 |
| d9411250-78bb-34f6-8b26-a41551a9f3bc | -18.24676 | -47.26581 | 2025-08-14 05:14:00 | NOAA-20 | COROMANDEL | MINAS GERAIS | Brasil | 3119302 | 31 | 33 | nan | nan | nan | Cerrado | 2.5 |
| db452915-ba7b-356a-b6e6-34452a735604 | -21.01604 | -48.92068 | 2025-08-14 05:14:00 | NOAA-20 | NOVAIS | SÃO PAULO | Brasil | 3533254 | 35 | 33 | nan | nan | nan | Mata Atlântica | 9.5 |
| 80da3d73-6235-3520-aa05-e3be5fb5be31 | -21.00986 | -48.91997 | 2025-08-14 05:14:00 | NOAA-20 | NOVAIS | SÃO PAULO | Brasil | 3533254 | 35 | 33 | nan | nan | nan | Mata Atlântica | 9.5 |
| 9d977f5b-33fe-39a4-9887-6f76259fd748 | -21.01055 | -48.92367 | 2025-08-14 05:14:00 | NOAA-20 | NOVAIS | SÃO PAULO | Brasil | 3533254 | 35 | 33 | nan | nan | nan | Mata Atlântica | 7.7 |
| 64127495-9d1e-3fb2-8a89-c4c3ab2ce5b3 | -22.77901 | -50.20263 | 2025-08-14 05:14:00 | NOAA-20 | PALMITAL | SÃO PAULO | Brasil | 3535309 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 9ac3fc71-35c8-3f63-b3f2-6c43345d41de | -18.5408 | -46.06323 | 2025-08-14 05:14:00 | NOAA-20 | PATOS DE MINAS | MINAS GERAIS | Brasil | 3148004 | 31 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 9ad4f9a7-c170-3a37-8ddf-383689d85014 | -21.01101 | -48.91866 | 2025-08-14 05:14:00 | NOAA-20 | NOVAIS | SÃO PAULO | Brasil | 3533254 | 35 | 33 | nan | nan | nan | Mata Atlântica | 15.5 |
| 77fd329e-c982-35ce-81fc-a2376dde60a6 | -21.01029 | -48.91487 | 2025-08-14 05:14:00 | NOAA-20 | NOVAIS | SÃO PAULO | Brasil | 3533254 | 35 | 33 | nan | nan | nan | Mata Atlântica | 8.7 |
| 62822c20-3c3f-3208-a327-daff2b2495ab | -19.08302 | -48.15639 | 2025-08-14 05:14:00 | NOAA-20 | UBERLÂNDIA | MINAS GERAIS | Brasil | 3170206 | 31 | 33 | nan | nan | nan | Cerrado | 2.6 |


[Clique aqui para ver as próximas entradas](README34.md)
