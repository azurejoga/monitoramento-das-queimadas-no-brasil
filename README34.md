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

## Dados Diários - Página 34

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 8f69ac95-bef2-31b4-9807-cd0158c2319c | -10.9369 | -54.254299 | 2024-09-27 01:28:26 | METOP-C | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 25058439-e5db-3bca-8581-9e2659c3ab69 | -10.9391 | -54.2631 | 2024-09-27 01:28:26 | METOP-C | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 401861d6-49c1-3767-82e9-cff4dd196371 | -10.9412 | -54.2719 | 2024-09-27 01:28:26 | METOP-C | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 38829b64-e99f-31e1-999e-164b898d6902 | -10.923 | -54.238899 | 2024-09-27 01:28:27 | METOP-C | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| c22060dc-b4ed-324a-bc8e-34922a8d74c8 | -10.9251 | -54.247799 | 2024-09-27 01:28:27 | METOP-C | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 34244afb-e669-3d9d-9e13-86ca6e1ae655 | -10.9272 | -54.256699 | 2024-09-27 01:28:27 | METOP-C | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 56ae6c16-c072-3d4f-a599-5bcced8b2093 | -10.9294 | -54.265499 | 2024-09-27 01:28:27 | METOP-C | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 9e083f35-fae7-3f4d-b295-191245e39858 | -10.9315 | -54.2743 | 2024-09-27 01:28:27 | METOP-C | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 2d47e3a9-d840-3569-ab66-aaae1f4eb020 | -9.6083 | -50.136398 | 2024-09-27 01:28:31 | METOP-C | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| affa0362-e641-306f-b817-a4db1fe7e303 | -9.5943 | -50.122101 | 2024-09-27 01:28:32 | METOP-C | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 469c8c28-b40e-3ed7-bdbd-14edf70dd88c | -9.5986 | -50.138901 | 2024-09-27 01:28:32 | METOP-C | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| dd9bdbb8-b612-34ff-a24f-1b02df2fb22f | -9.6028 | -50.155602 | 2024-09-27 01:28:32 | METOP-C | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 6129c552-0697-31f3-b2c2-438276428b25 | -9.5846 | -50.1245 | 2024-09-27 01:28:32 | METOP-C | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f5053c99-678d-3504-bc1c-857a3416033d | -9.5889 | -50.1413 | 2024-09-27 01:28:32 | METOP-C | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f7e4b14d-78ce-3315-89fd-2a450eb05364 | -10.6284 | -54.6054 | 2024-09-27 01:28:33 | METOP-C | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| d43e4649-e378-3e57-96d7-eca1e7bbf325 | -10.6187 | -54.6077 | 2024-09-27 01:28:33 | METOP-C | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 05695b89-2213-3da6-84a1-28297f074913 | -10.3757 | -53.769001 | 2024-09-27 01:28:34 | METOP-C | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 940244fe-7759-3933-93fb-733027128a13 | -10.378 | -53.7785 | 2024-09-27 01:28:34 | METOP-C | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 3d654ea7-dba5-33b9-aaa6-2c548e2f52f4 | -10.366 | -53.771301 | 2024-09-27 01:28:34 | METOP-C | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| df54f320-069d-3d1c-85dc-774b8edd390c | -10.3683 | -53.780899 | 2024-09-27 01:28:34 | METOP-C | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| b4e710ef-2c88-3563-91ff-547ae94f0af7 | -10.3706 | -53.790401 | 2024-09-27 01:28:34 | METOP-C | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 0e5cf7f0-85cb-3397-91b7-a23861914787 | -10.3729 | -53.7999 | 2024-09-27 01:28:34 | METOP-C | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| c5e80bd9-c20e-333c-8c9a-c718be54ffc1 | -10.3562 | -53.773701 | 2024-09-27 01:28:34 | METOP-C | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 8240960e-387e-36a2-88a8-1c8a2876fa80 | -10.3585 | -53.783298 | 2024-09-27 01:28:34 | METOP-C | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 3e475047-ce9c-3810-b50f-47d017d22e3d | -10.3608 | -53.792801 | 2024-09-27 01:28:34 | METOP-C | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 7b01e629-5336-3d48-a2b1-1da486fc5496 | -10.0149 | -53.431301 | 2024-09-27 01:28:38 | METOP-C | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 46c09a9a-bf98-365a-838c-5068f961d25e | -10.049 | -53.444199 | 2024-09-27 01:28:38 | METOP-C | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| afc5a8a8-e161-34b1-957b-5a50b0b49e4b | -10.0514 | -53.4543 | 2024-09-27 01:28:38 | METOP-C | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 014ff2a6-6bc9-31e8-b06c-b59849bae7f2 | -10.0368 | -53.4366 | 2024-09-27 01:28:38 | METOP-C | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 5e3506c8-4c19-3941-8a99-cd71d4f16d57 | -10.0393 | -53.446602 | 2024-09-27 01:28:38 | METOP-C | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| e22d65a0-f934-32ee-b6f6-5c8986c745dd | -10.0417 | -53.456699 | 2024-09-27 01:28:38 | METOP-C | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 3dac360c-7912-3ffc-a08a-62dc2b2addc9 | -10.0442 | -53.466702 | 2024-09-27 01:28:38 | METOP-C | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 9fc4741c-8b8f-3305-83ae-b2209e08de07 | -10.027 | -53.438999 | 2024-09-27 01:28:38 | METOP-C | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| b794a8df-3f14-34dd-bf9f-de982568818c | -10.0295 | -53.449001 | 2024-09-27 01:28:38 | METOP-C | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| d7c88e33-3e7f-371d-bc4c-9f50a1bfe29d | -10.0319 | -53.459099 | 2024-09-27 01:28:38 | METOP-C | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| c8b61cc3-3716-3099-bb0a-4ee0c36e1687 | -10.0173 | -53.441399 | 2024-09-27 01:28:38 | METOP-C | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 8e6e1a64-21f5-3ca4-8e4b-f92b5ebab619 | -10.0198 | -53.451401 | 2024-09-27 01:28:38 | METOP-C | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 66d26ab7-aa0e-31c7-a06b-4c24f1e32c74 | -11.6109 | -60.350601 | 2024-09-27 01:28:38 | METOP-C | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 96548c42-4fbc-3d77-a01e-438592d1f188 | -9.4542 | -51.4487 | 2024-09-27 01:28:39 | METOP-C | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 1c6360ec-2adc-37b4-be1e-582f367b2ff4 | -9.4576 | -51.462399 | 2024-09-27 01:28:39 | METOP-C | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e809959b-9aef-397a-8c34-2816ed057ee3 | -9.4478 | -51.464802 | 2024-09-27 01:28:39 | METOP-C | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 36282546-64d0-3428-bbf2-332b8714c32f | -9.4216 | -51.4422 | 2024-09-27 01:28:40 | METOP-C | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| aefb35fe-684e-3778-bc0f-9eb892ed03c4 | -9.425 | -51.456001 | 2024-09-27 01:28:40 | METOP-C | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 7f45fbc8-cb0d-36db-97b9-305ab23a2a5c | -9.4084 | -51.430901 | 2024-09-27 01:28:40 | METOP-C | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| dd43a15f-3812-365e-811b-e227b3e92d4b | -9.4119 | -51.444698 | 2024-09-27 01:28:40 | METOP-C | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 711589c9-2b67-302e-8268-d3216cbcc7ed | -9.6639 | -53.5172 | 2024-09-27 01:28:44 | METOP-C | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| acbe0e02-b36e-33e4-bbc2-ccc9acd5a076 | -9.6664 | -53.527199 | 2024-09-27 01:28:44 | METOP-C | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| cdf1a27d-7405-3ca3-be38-daa7bff394f1 | -8.5621 | -49.588699 | 2024-09-27 01:28:46 | METOP-C | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| aa822f32-3ee6-3c92-9803-a965af2e9a1c | -8.567 | -49.607601 | 2024-09-27 01:28:46 | METOP-C | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 042b8d5e-6eca-3334-a6a3-ea84da954515 | -8.5718 | -49.626499 | 2024-09-27 01:28:46 | METOP-C | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f7def7b6-bfe3-38db-a056-7485be284e95 | -8.5525 | -49.591099 | 2024-09-27 01:28:46 | METOP-C | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| bef69f59-319a-3d19-9401-401a55e908f2 | -8.5573 | -49.610001 | 2024-09-27 01:28:46 | METOP-C | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 48544d64-3478-398a-9bf8-ced8b1a34374 | -8.8932 | -53.023499 | 2024-09-27 01:28:55 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a6a9ea8a-731d-32dd-8ad3-a8acedbfb6cc | -9.175 | -54.661098 | 2024-09-27 01:28:56 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ca4eb8ea-8fbe-35ec-9df5-142d47e92070 | -9.1771 | -54.669899 | 2024-09-27 01:28:56 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 00f4c5a7-f039-3fc5-8d73-621ad3733c67 | -7.1001 | -46.4352 | 2024-09-27 01:28:57 | METOP-C | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| f79493c2-63f0-3b57-988e-b6c1a7bf54c2 | -7.0905 | -46.437698 | 2024-09-27 01:28:57 | METOP-C | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 1eb1666b-ee9a-3a2c-aad1-024af115d73f | -8.6613 | -53.173302 | 2024-09-27 01:28:59 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 18776283-df1b-3af8-b2e7-e70c19b82a7d | -8.6738 | -53.1819 | 2024-09-27 01:28:59 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| cd460c61-c15f-39a9-896d-3fd44da7cf68 | -8.664 | -53.1842 | 2024-09-27 01:28:59 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ef2f3542-d1b8-3ec6-bfff-fda4d748ef7d | -8.6543 | -53.1866 | 2024-09-27 01:28:59 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e87fbd56-da7a-3dc4-ad2e-e961837c64f3 | -8.9253 | -54.739399 | 2024-09-27 01:29:01 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 81260ff4-1f1b-3eb6-953e-32329c74a7d0 | -8.5759 | -53.3316 | 2024-09-27 01:29:01 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 3a66647a-0ed5-351d-ac56-6d3b644f9781 | -8.5785 | -53.3423 | 2024-09-27 01:29:01 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 96099858-181e-3e6d-b14f-750a292b82dc | -8.5811 | -53.352901 | 2024-09-27 01:29:01 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 53be4e64-c5b4-304f-9e19-f2e12c82183e | -8.7103 | -54.790699 | 2024-09-27 01:29:04 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| bddba8d5-d59f-31b3-9a55-fd2ac0a18124 | -8.7124 | -54.7995 | 2024-09-27 01:29:04 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 43913bd1-754e-39ac-b076-fcd1d45f1ab3 | -8.7145 | -54.8083 | 2024-09-27 01:29:04 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 586a1312-b2e9-3ab1-84f8-ebdb326aa8bd | -8.7559 | -54.981899 | 2024-09-27 01:29:04 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 5306e741-447d-368b-a472-97a57aaca78e | -8.6985 | -54.784199 | 2024-09-27 01:29:05 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 21c4923e-7106-3f23-9430-8c68ce18c477 | -8.7006 | -54.792999 | 2024-09-27 01:29:05 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 57b7a69e-433b-30f1-a6ab-ea0a220b0b2b | -8.7027 | -54.8018 | 2024-09-27 01:29:05 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 7e8e7463-4636-317a-b2f0-31570fdc7781 | -8.5334 | -54.5686 | 2024-09-27 01:29:06 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 970e9ecd-4878-3f32-a9a5-23419314fdfe | -8.5356 | -54.577702 | 2024-09-27 01:29:06 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| dbce6d3b-c7bc-37c3-99b2-9b1b7de03bca | -8.5377 | -54.5868 | 2024-09-27 01:29:06 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| db0d34ee-2ff8-3bce-ac8d-44cb5a5f2ed7 | -8.5302 | -54.598099 | 2024-09-27 01:29:07 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 6e243056-8703-3527-9859-48bda0aaaa8a | -8.4356 | -54.677898 | 2024-09-27 01:29:08 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f3b8653c-c098-3a6d-a894-60079f1f75a4 | -8.4258 | -54.680199 | 2024-09-27 01:29:09 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 1ea0a96c-7eb2-36c7-b0bc-3fc9450e4151 | -8.428 | -54.689201 | 2024-09-27 01:29:09 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 86bd2ea7-8d35-3a6c-afbc-3ef1924e8b08 | -8.4183 | -54.691502 | 2024-09-27 01:29:09 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 2cf1ae03-f15d-3422-bbdd-84110c45d36b | -8.4204 | -54.700401 | 2024-09-27 01:29:09 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a533730f-d56a-30b8-866e-c2bbe8d3e7e3 | -8.4225 | -54.7094 | 2024-09-27 01:29:09 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b421b63e-0242-31bb-bd90-abaab574b75a | -8.5244 | -55.180698 | 2024-09-27 01:29:09 | METOP-C | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| bced5c9e-f004-365d-91d3-1d66d35294d3 | -8.5264 | -55.189098 | 2024-09-27 01:29:09 | METOP-C | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 7fbfaccb-0afb-3c52-ba49-827d1769cad4 | -8.5146 | -55.182999 | 2024-09-27 01:29:09 | METOP-C | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b737dbc0-a89f-3893-be67-56867bd1a715 | -8.5166 | -55.191399 | 2024-09-27 01:29:09 | METOP-C | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e3777c3d-4f59-3232-a0d1-9d5638fc9a55 | -8.4057 | -55.028702 | 2024-09-27 01:29:10 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 65c9458d-b3cf-3ebb-96a0-1aed43232e56 | -8.3532 | -55.068401 | 2024-09-27 01:29:11 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 30287412-a7eb-3193-a4b5-2b11bfd737e4 | -8.3553 | -55.077 | 2024-09-27 01:29:11 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e13868e2-4126-377b-9884-ffc2bae905ac | -8.3434 | -55.070801 | 2024-09-27 01:29:11 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ceb54c64-96c5-3211-83cc-dcbaa369a119 | -8.3151 | -54.995399 | 2024-09-27 01:29:12 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 19824359-bf83-3980-941f-cbc7b36cd8c6 | -8.3172 | -55.004101 | 2024-09-27 01:29:12 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 2bbeb9be-cc7e-3683-8c33-a027567c7064 | -8.3193 | -55.012699 | 2024-09-27 01:29:12 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| aeaf6c1d-7d9a-39f6-a819-c695d2bbb72c | -8.3213 | -55.0214 | 2024-09-27 01:29:12 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e68be668-bb40-373e-92e5-1d56c0835bca | -8.3074 | -55.006401 | 2024-09-27 01:29:12 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d5c4ca38-0ef4-3244-b0a5-a1dd397f9cf3 | -8.1218 | -54.790401 | 2024-09-27 01:29:14 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c7f1e911-adbd-38c4-b5d5-3ab41547c340 | -8.1141 | -55.061401 | 2024-09-27 01:29:15 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 2f9ca643-1e97-3b36-a7e9-d6a73dd98b72 | -8.1161 | -55.07 | 2024-09-27 01:29:15 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 75d3d249-6570-3452-8b9e-85556f6a4e7a | -8.1182 | -55.078701 | 2024-09-27 01:29:15 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 244eb931-c3f5-3666-aa8b-2b0775a0ed43 | -8.0985 | -55.3876 | 2024-09-27 01:29:17 | METOP-C | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | nan |


[Clique aqui para ver as próximas entradas](README35.md)
