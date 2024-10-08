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

## Dados Diários - Página 100

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 6aaa6000-398f-3bc9-8c1b-baede3842bf8 | -16.43565 | -57.25093 | 2024-10-08 04:59:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.6 |
| 55c13277-dd98-390d-be89-8383e2351681 | -16.4354 | -57.33735 | 2024-10-08 04:59:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.4 |
| 4252c23c-2f8b-36fb-8e9d-ea86391f009c | -16.43506 | -57.25457 | 2024-10-08 04:59:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.2 |
| c2afef35-ecb9-3890-afef-25ec28946432 | -16.43502 | -57.31847 | 2024-10-08 04:59:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.2 |
| f1993f54-fa48-31e3-b7c0-e9f144b94c5d | -16.43447 | -57.25822 | 2024-10-08 04:59:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.2 |
| 6caf85ba-51a4-3c1e-a5cb-4d2a42f61c09 | -16.43442 | -57.32212 | 2024-10-08 04:59:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.2 |
| c9cc6f9b-efc2-3204-91ad-bc77bf2db403 | -16.43205 | -57.33677 | 2024-10-08 04:59:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.4 |
| 04d7becc-8160-377f-8469-d549706fee98 | -16.43171 | -57.25399 | 2024-10-08 04:59:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.2 |
| f90dcb7d-b5f5-3eca-a47a-b062ef71fccd | -16.43145 | -57.34043 | 2024-10-08 04:59:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.4 |
| 710e6aa9-f329-3105-b64c-97bf6ffb5a39 | -16.43112 | -57.25765 | 2024-10-08 04:59:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.2 |
| bf64b5fe-bcd2-3762-a87f-960228ed639c | -16.4287 | -57.33617 | 2024-10-08 04:59:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.2 |
| 6eb80c4b-da9d-387d-b972-1fc2991f786e | -16.4281 | -57.33985 | 2024-10-08 04:59:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.2 |
| f6220b8e-afca-34bd-a787-1066b7f252ce | -16.42534 | -57.3356 | 2024-10-08 04:59:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.2 |
| 067ed19c-c3a7-3e8b-ad98-2abd8a05d54d | -16.42318 | -57.32769 | 2024-10-08 04:59:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.9 |
| c3a75e1d-eea4-31b7-a0bd-7dc0d040c214 | -16.41983 | -57.32711 | 2024-10-08 04:59:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.9 |
| a5f7d9f4-5c6b-3d26-9391-ee66f805a4c2 | -16.41804 | -57.33809 | 2024-10-08 04:59:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.5 |
| ae71531e-39ea-3003-bc96-a367449ddd5c | -16.41707 | -57.32287 | 2024-10-08 04:59:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.6 |
| 2cb6d05c-c49c-3fe2-974c-d6230a493b8e | -16.41648 | -57.32652 | 2024-10-08 04:59:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.2 |
| ba050152-7265-33c8-b86b-cb0acfd4fe50 | -16.41529 | -57.33384 | 2024-10-08 04:59:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 0.8 |
| 7e0281ea-1a95-37ee-8952-7e9c33a4d64e | -16.41469 | -57.33751 | 2024-10-08 04:59:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 0.8 |
| f5ea128d-6a7d-3dbe-aaab-ebb6ec7d496e | -16.41372 | -57.32228 | 2024-10-08 04:59:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.6 |
| 8ce63431-daae-3bf3-b0b6-8158361ed5a4 | -16.41313 | -57.32594 | 2024-10-08 04:59:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.2 |
| 79067818-007f-3563-88a2-8a078361e83e | -16.41203 | -57.32245 | 2024-10-08 04:59:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.3 |
| c696df2c-0504-35c9-8829-f8cbd1033e87 | -16.41194 | -57.33326 | 2024-10-08 04:59:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 0.8 |
| cbdcfccc-b320-31c5-8fbb-b47ed9664f53 | -16.41134 | -57.33693 | 2024-10-08 04:59:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 0.8 |
| 3b520ae0-e318-3adc-9386-b0f9e56186ab | -16.40967 | -57.3371 | 2024-10-08 04:59:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 0.7 |
| 00ca1bf0-eb33-3914-8bd7-29ff0b5c0653 | -16.40632 | -57.33651 | 2024-10-08 04:59:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 0.7 |
| 91b5488a-407e-3dca-af74-ae321dfd0a0c | -16.39074 | -57.39034 | 2024-10-08 04:59:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 0.6 |
| 1ab6e33a-1ddf-34d8-8eb6-9524ad756840 | -16.38739 | -57.38976 | 2024-10-08 04:59:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 0.7 |
| 8e494d42-2b52-3122-ad2d-1992a63f6820 | -16.14592 | -57.41569 | 2024-10-08 04:59:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 1becb1cf-f8d4-34b9-bf30-15ef389ddb32 | -16.14257 | -57.41508 | 2024-10-08 04:59:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 2bc19207-b5e5-3df3-9862-ebd538abddc1 | -16.13921 | -57.41446 | 2024-10-08 04:59:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 60f484f8-db10-3455-beed-36b20d0d4ad6 | -16.13862 | -57.41814 | 2024-10-08 04:59:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| aaa498fb-ba83-3b41-944e-7fb1a9d3af9b | -15.97065 | -57.22449 | 2024-10-08 04:59:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | 3.6 |
| a50bf77a-ee73-32ab-89ad-8edef79731c0 | -15.96789 | -57.22029 | 2024-10-08 04:59:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 181c89ec-3c17-307d-89f5-3972672f4cba | -15.9673 | -57.2239 | 2024-10-08 04:59:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| ccaef90a-3172-3b73-8184-3adc5662832a | -15.96672 | -57.22753 | 2024-10-08 04:59:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 06b43e91-e50f-3d31-b738-ba3b4bb52fb1 | -15.96395 | -57.22331 | 2024-10-08 04:59:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| b00f6738-e02e-35c2-a517-7d65a8d17540 | -15.96119 | -57.21909 | 2024-10-08 04:59:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 0ef5cd7f-a98e-3a8b-92cf-ffc2b7e8bc9d | -15.95843 | -57.21487 | 2024-10-08 04:59:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 88e12233-0de0-32bd-a35d-56e67f5322e8 | -15.95784 | -57.21849 | 2024-10-08 04:59:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 007595d0-fb54-34ba-946b-cfbd3645956d | -15.95508 | -57.21425 | 2024-10-08 04:59:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 3797c81e-724f-3272-9c4d-2f210159c142 | -15.9545 | -57.21788 | 2024-10-08 04:59:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | 4.0 |
| e230b868-b785-3af2-b80b-d8a493abd77d | -15.7741 | -57.16417 | 2024-10-08 04:59:00 | NPP-375D | NOSSA SENHORA DO LIVRAMENTO | MATO GROSSO | Brasil | 5106109 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 258ad654-74b9-33f1-bbd5-2185fa6076e8 | -15.68904 | -57.39101 | 2024-10-08 04:59:00 | NPP-375D | PORTO ESTRELA | MATO GROSSO | Brasil | 5106851 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 9800b88f-8fd6-323f-a8a4-7e1f88798e29 | -15.68845 | -57.39467 | 2024-10-08 04:59:00 | NPP-375D | PORTO ESTRELA | MATO GROSSO | Brasil | 5106851 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| c38b0805-28cf-3e46-b594-02a08ba065ec | -15.68509 | -57.39406 | 2024-10-08 04:59:00 | NPP-375D | PORTO ESTRELA | MATO GROSSO | Brasil | 5106851 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 6096c4ee-0567-3930-8ff3-60cca141b2ce | -15.6845 | -57.39765 | 2024-10-08 04:59:00 | NPP-375D | PORTO ESTRELA | MATO GROSSO | Brasil | 5106851 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| d95d772c-e8c0-34ef-9165-bfba2f2e2b70 | -15.68392 | -57.4012 | 2024-10-08 04:59:00 | NPP-375D | PORTO ESTRELA | MATO GROSSO | Brasil | 5106851 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 32c850a9-3e52-35c4-8cff-6bb4dabc8685 | -15.68114 | -57.39705 | 2024-10-08 04:59:00 | NPP-375D | PORTO ESTRELA | MATO GROSSO | Brasil | 5106851 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 38adfeae-7ef3-3a0d-8485-006b801c7e5f | -15.68056 | -57.4006 | 2024-10-08 04:59:00 | NPP-375D | PORTO ESTRELA | MATO GROSSO | Brasil | 5106851 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 5adb091f-bd52-3814-9388-f3dbba44030f | -15.67559 | -57.38863 | 2024-10-08 04:59:00 | NPP-375D | PORTO ESTRELA | MATO GROSSO | Brasil | 5106851 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| e7f28e22-9c41-31c3-9ab9-e990adf9460d | -15.675 | -57.39223 | 2024-10-08 04:59:00 | NPP-375D | PORTO ESTRELA | MATO GROSSO | Brasil | 5106851 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 1c259027-023d-33db-abba-a5fbe3f63808 | -15.66828 | -57.39101 | 2024-10-08 04:59:00 | NPP-375D | PORTO ESTRELA | MATO GROSSO | Brasil | 5106851 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 12191fc7-b629-3b50-9ff5-290b7853d3b6 | -15.66492 | -57.39037 | 2024-10-08 04:59:00 | NPP-375D | PORTO ESTRELA | MATO GROSSO | Brasil | 5106851 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 4d81c773-d0f7-3f6d-ace1-0106e12aeeff | -15.64162 | -57.37933 | 2024-10-08 04:59:00 | NPP-375D | PORTO ESTRELA | MATO GROSSO | Brasil | 5106851 | 51 | 33 | nan | nan | nan | Cerrado | 4.7 |
| aaa2cc7a-ae7f-37c4-b6cf-99c4943f3247 | -15.63826 | -57.37872 | 2024-10-08 04:59:00 | NPP-375D | PORTO ESTRELA | MATO GROSSO | Brasil | 5106851 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| a9d67e0c-8a09-3c66-b53f-140074ab2da7 | -15.63547 | -57.37455 | 2024-10-08 04:59:00 | NPP-375D | PORTO ESTRELA | MATO GROSSO | Brasil | 5106851 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| e155baac-901a-3305-b797-0caa588c40f7 | -15.62262 | -57.36849 | 2024-10-08 04:59:00 | NPP-375D | PORTO ESTRELA | MATO GROSSO | Brasil | 5106851 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 7f0ed5df-4564-324c-8636-0313951e741a | -15.61925 | -57.36789 | 2024-10-08 04:59:00 | NPP-375D | PORTO ESTRELA | MATO GROSSO | Brasil | 5106851 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| cc019eee-069a-34ab-9648-c0fe37fffdb1 | -15.61589 | -57.36731 | 2024-10-08 04:59:00 | NPP-375D | PORTO ESTRELA | MATO GROSSO | Brasil | 5106851 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 5bcdb9c9-13ce-3275-9024-e7b53f392d7e | -15.61132 | -57.37415 | 2024-10-08 04:59:00 | NPP-375D | PORTO ESTRELA | MATO GROSSO | Brasil | 5106851 | 51 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 456f2ca7-f724-330e-94a8-4946e52445e7 | -15.60856 | -57.36985 | 2024-10-08 04:59:00 | NPP-375D | PORTO ESTRELA | MATO GROSSO | Brasil | 5106851 | 51 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 35d2ea73-78a1-338d-9e1f-54d3becb3c93 | -15.60795 | -57.3736 | 2024-10-08 04:59:00 | NPP-375D | PORTO ESTRELA | MATO GROSSO | Brasil | 5106851 | 51 | 33 | nan | nan | nan | Cerrado | 2.6 |
| a37b318e-966f-3ad6-9430-f719de4c17f4 | -15.60458 | -57.37307 | 2024-10-08 04:59:00 | NPP-375D | PORTO ESTRELA | MATO GROSSO | Brasil | 5106851 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 4ef560cc-279d-3c2f-8a5e-848bc5e5f634 | -15.55125 | -56.64743 | 2024-10-08 04:59:00 | NPP-375D | NOSSA SENHORA DO LIVRAMENTO | MATO GROSSO | Brasil | 5106109 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| ad3f57da-eef9-38c5-addf-7d8d945148c0 | -15.54139 | -56.6537 | 2024-10-08 04:59:00 | NPP-375D | NOSSA SENHORA DO LIVRAMENTO | MATO GROSSO | Brasil | 5106109 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 52457596-3fa8-3e51-91ee-4ee3eda285ee | -15.53136 | -56.89938 | 2024-10-08 04:59:00 | NPP-375D | NOSSA SENHORA DO LIVRAMENTO | MATO GROSSO | Brasil | 5106109 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 40f9d9de-9d05-3acd-9f5e-f8838ea5742b | -15.52861 | -56.8952 | 2024-10-08 04:59:00 | NPP-375D | NOSSA SENHORA DO LIVRAMENTO | MATO GROSSO | Brasil | 5106109 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 89df4da7-733c-32cd-a39d-9f7acdf11a7b | -15.52468 | -56.89824 | 2024-10-08 04:59:00 | NPP-375D | NOSSA SENHORA DO LIVRAMENTO | MATO GROSSO | Brasil | 5106109 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 173afce3-3ee2-3801-b0fd-d1e3d915b5dd | -16.56236 | -57.47585 | 2024-10-08 04:59:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 0.4 |
| 9b68fd09-896b-3fdd-afcd-eea3753ba0a5 | -16.559 | -57.47526 | 2024-10-08 04:59:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 0.4 |
| 8307bfa6-8ffa-3f23-baee-59a266451e27 | -16.55759 | -57.71821 | 2024-10-08 04:59:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 0.3 |
| 372e6889-260e-3e86-a4c9-b5e3bb8a8cb2 | -16.55699 | -57.72195 | 2024-10-08 04:59:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.1 |
| a028608c-7632-3080-9bbc-cb33bbf55586 | -16.55638 | -57.72568 | 2024-10-08 04:59:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.1 |
| 898abe0d-07f3-37a4-a41a-32bc6ed7b340 | -16.55578 | -57.72941 | 2024-10-08 04:59:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 0.8 |
| 2146ae04-8467-3ffa-95ab-07025e8e850b | -16.55301 | -57.72507 | 2024-10-08 04:59:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.1 |
| f51e3452-2a2b-387f-a04e-c796136d86cf | -16.55024 | -57.72075 | 2024-10-08 04:59:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.7 |
| 85e0602e-2a0e-34e3-87e5-03fdb816f549 | -16.54963 | -57.72447 | 2024-10-08 04:59:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.7 |
| 1cedca5c-fa4f-39e9-acb8-f7b2d2f15b85 | -16.54782 | -57.73565 | 2024-10-08 04:59:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 0.4 |
| f9d7d466-712e-300b-a2dc-dab7e2cdf99e | -16.54721 | -57.73938 | 2024-10-08 04:59:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 0.4 |
| 9b647f58-34e4-32c3-a0e4-99a070abba46 | -16.54626 | -57.72388 | 2024-10-08 04:59:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.7 |
| c036be00-9f58-3898-b535-34d72d9514f1 | -16.54565 | -57.72759 | 2024-10-08 04:59:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 0.4 |
| 01b67af2-0d40-396f-905b-5060a23028d7 | -16.54167 | -57.73073 | 2024-10-08 04:59:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 0.8 |
| 5e49665d-2c1e-3744-ad39-f52b06e6ee9a | -16.53586 | -57.74511 | 2024-10-08 04:59:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 0.6 |
| bce5b047-90e2-3785-b544-a02515ae1572 | -16.52971 | -57.74021 | 2024-10-08 04:59:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 0.4 |
| 21e5e1f9-d853-3e97-8330-47106e8cc0c4 | -16.5291 | -57.74393 | 2024-10-08 04:59:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 0.4 |
| cef75d69-4a28-33d0-9d13-ce9d743e6798 | -16.52446 | -57.70853 | 2024-10-08 04:59:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 0.4 |
| 5a42248c-6556-3935-b04a-4c77b8524d5c | -16.52047 | -57.7117 | 2024-10-08 04:59:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 0.4 |
| e2e45599-edfa-39b9-b71b-4426e875fbe1 | -16.51312 | -57.71421 | 2024-10-08 04:59:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 0.9 |
| 493c0ce3-7d18-307e-90af-a2589d2abdb0 | -16.50974 | -57.71362 | 2024-10-08 04:59:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.1 |
| 558c5194-1227-3708-85fc-2a057e03fd86 | -16.50637 | -57.71303 | 2024-10-08 04:59:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.1 |
| 3cb45288-d23b-3f59-9a91-02fbf62aebb4 | -16.50206 | -57.69696 | 2024-10-08 04:59:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 0.4 |
| 5e901edf-2d7c-382e-97a7-35ed3e7bf143 | -16.49869 | -57.69637 | 2024-10-08 04:59:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 0.7 |
| b9d8aab6-7811-3643-9860-9ae157fe2637 | -16.49472 | -57.7417 | 2024-10-08 04:59:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 0.5 |
| 91154c07-cab7-3a77-b26c-e84bfe9101f4 | -16.4947 | -57.69951 | 2024-10-08 04:59:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 0.7 |
| 35f394a7-091d-3d0d-affb-0d64824a16af | -16.49409 | -57.70324 | 2024-10-08 04:59:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.5 |
| 61800367-e6d3-3ce8-8e0e-732edc71f8ea | -16.49348 | -57.70696 | 2024-10-08 04:59:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.5 |
| 02456ef5-d472-389b-9a10-c29032254ada | -16.49318 | -57.72996 | 2024-10-08 04:59:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 0.9 |
| 0ff8d6c1-ddff-30bc-b2a2-0ab7e6bf24ea | -16.49256 | -57.73368 | 2024-10-08 04:59:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 0.9 |


[Clique aqui para ver as próximas entradas](README101.md)
