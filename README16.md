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

## Dados Diários - Página 16

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 0b68b06f-2a98-3a2d-a69e-5726f20aa468 | -16.5084 | -57.345402 | 2024-09-29 01:31:53 | METOP-B | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| db91b91f-0d4c-39f0-b3bf-94a680274a2b | -16.4792 | -57.353001 | 2024-09-29 01:31:54 | METOP-B | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| b00c6376-be17-3a02-b8a3-da0fc67d1301 | -16.4813 | -57.3619 | 2024-09-29 01:31:54 | METOP-B | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 867fc326-c5a2-38bf-a644-90afc9adda59 | -16.4694 | -57.3554 | 2024-09-29 01:31:54 | METOP-B | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 2ff05f62-1040-3fc8-971d-b34a83bcad66 | -16.4715 | -57.3643 | 2024-09-29 01:31:54 | METOP-B | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 2f07c5c3-f130-31f8-b47f-b196fda9505d | -16.451099 | -57.321999 | 2024-09-29 01:31:54 | METOP-B | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 7a4ff268-02d0-30e2-b98d-ea39849aeedc | -16.1138 | -57.5126 | 2024-09-29 01:32:00 | METOP-B | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 029567ae-ffbe-37d3-a786-c9127f4f497e | -15.9416 | -57.181499 | 2024-09-29 01:32:02 | METOP-B | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 3d31765f-f497-340c-bf1d-7f483fe70194 | -15.9438 | -57.190701 | 2024-09-29 01:32:02 | METOP-B | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| cf07a978-07b1-368d-9d9b-35fa2a838d70 | -15.9296 | -57.174702 | 2024-09-29 01:32:02 | METOP-B | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| cddf0159-5d4e-3bbd-b55e-48054c38adaa | -15.9318 | -57.183998 | 2024-09-29 01:32:02 | METOP-B | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 4142589a-0613-39f6-b0a1-45df932e9965 | -15.9176 | -57.1679 | 2024-09-29 01:32:02 | METOP-B | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| dbc85f20-89fa-36b2-845c-5a98af527d39 | -15.9198 | -57.1772 | 2024-09-29 01:32:02 | METOP-B | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 1d797b40-e437-35f3-b7f4-a36abae07463 | -15.9221 | -57.186501 | 2024-09-29 01:32:02 | METOP-B | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 40c22d37-2d6e-3cc0-bd21-ba432bfe3216 | -15.9078 | -57.170399 | 2024-09-29 01:32:02 | METOP-B | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 516c51da-a8bf-32c0-a439-cf4033f6d8f9 | -15.9123 | -57.188999 | 2024-09-29 01:32:02 | METOP-B | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 615d83e4-8fd3-30c0-a3d5-939bce965765 | -15.9004 | -57.182201 | 2024-09-29 01:32:02 | METOP-B | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 6595a2ae-a3d1-3bbf-b10a-8bd934bcc571 | -15.9026 | -57.191502 | 2024-09-29 01:32:02 | METOP-B | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 5e01eb25-41b6-39d0-95be-8286555e6a9b | -15.8305 | -57.365601 | 2024-09-29 01:32:04 | METOP-B | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| b87edc1b-c328-3e84-976f-9914b287ea32 | -15.8327 | -57.374699 | 2024-09-29 01:32:04 | METOP-B | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| d20665f6-7765-3b2b-8e17-f258c9b33662 | -15.8349 | -57.383801 | 2024-09-29 01:32:04 | METOP-B | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 815339e1-9061-3b5d-ab51-19f478c61e4a | -15.812 | -57.331699 | 2024-09-29 01:32:04 | METOP-B | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 4879fecb-a1c0-3781-ba27-5e35c934f33d | -15.8142 | -57.340801 | 2024-09-29 01:32:04 | METOP-B | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 73914b88-d2db-3911-a8d9-119d653e8f96 | -15.8164 | -57.349998 | 2024-09-29 01:32:04 | METOP-B | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 409699cf-1008-371d-a97f-f7180ccd033c | -15.8186 | -57.3591 | 2024-09-29 01:32:04 | METOP-B | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| ba64a56b-8ae7-3b1c-ad91-5531690a807d | -15.8207 | -57.368099 | 2024-09-29 01:32:04 | METOP-B | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 22c1e0dc-d87b-30f5-a4c9-1cebb0709d76 | -15.8229 | -57.377201 | 2024-09-29 01:32:04 | METOP-B | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| b31a47c3-5da6-3f00-86a3-51c8824b6d19 | -15.8251 | -57.386299 | 2024-09-29 01:32:04 | METOP-B | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 4fc7c1ba-60ec-3adb-8ebe-6f7c146533a7 | -15.8273 | -57.395401 | 2024-09-29 01:32:04 | METOP-B | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| d6f67f41-6d32-3844-a9e6-9449ff2b8acb | -15.5649 | -56.906399 | 2024-09-29 01:32:07 | METOP-B | NOSSA SENHORA DO LIVRAMENTO | MATO GROSSO | Brasil | 5106109 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 7fa7637d-b361-37a7-99c5-2d286379fe8b | -15.6225 | -57.447498 | 2024-09-29 01:32:08 | METOP-B | PORTO ESTRELA | MATO GROSSO | Brasil | 5106851 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| e357f12e-3cb3-35dc-845d-e3eb92bb105a | -15.6247 | -57.4566 | 2024-09-29 01:32:08 | METOP-B | PORTO ESTRELA | MATO GROSSO | Brasil | 5106851 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| dc7dbad1-0387-36ba-8e9b-92139a3d73b1 | -15.6268 | -57.465599 | 2024-09-29 01:32:08 | METOP-B | BARRA DO BUGRES | MATO GROSSO | Brasil | 5101704 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| f0ef8224-5264-3d94-831b-2f17a79ead73 | -15.6128 | -57.450001 | 2024-09-29 01:32:08 | METOP-B | PORTO ESTRELA | MATO GROSSO | Brasil | 5106851 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| b04f4c60-0b08-3e57-bdf0-789e134cdc4a | -15.6149 | -57.459099 | 2024-09-29 01:32:08 | METOP-B | BARRA DO BUGRES | MATO GROSSO | Brasil | 5101704 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| ffffe2b7-0293-3594-8074-bd9a17a2debb | -15.6171 | -57.468102 | 2024-09-29 01:32:08 | METOP-B | BARRA DO BUGRES | MATO GROSSO | Brasil | 5101704 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 883e8a15-767b-3b93-857e-bd5b944981c1 | -15.6009 | -57.443401 | 2024-09-29 01:32:08 | METOP-B | BARRA DO BUGRES | MATO GROSSO | Brasil | 5101704 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 451db40f-fa14-34a7-ab2a-bb9cf72d12e5 | -15.603 | -57.452499 | 2024-09-29 01:32:08 | METOP-B | BARRA DO BUGRES | MATO GROSSO | Brasil | 5101704 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 608a27c9-3025-3dcd-b5b5-66c0a992ea58 | -15.6052 | -57.461498 | 2024-09-29 01:32:08 | METOP-B | BARRA DO BUGRES | MATO GROSSO | Brasil | 5101704 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 5b3a4e0a-7e5a-341a-a77c-f6a88e7c24fd | -15.5911 | -57.4459 | 2024-09-29 01:32:08 | METOP-B | BARRA DO BUGRES | MATO GROSSO | Brasil | 5101704 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 493ac23b-0683-3efb-b881-8843f0567cea | -15.5933 | -57.455002 | 2024-09-29 01:32:08 | METOP-B | BARRA DO BUGRES | MATO GROSSO | Brasil | 5101704 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 7c48c389-a17c-35d7-887d-1319e6a9b82d | -15.5835 | -57.457401 | 2024-09-29 01:32:08 | METOP-B | BARRA DO BUGRES | MATO GROSSO | Brasil | 5101704 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 8280d041-b0b6-3390-8a65-7633fcce07e1 | -15.5857 | -57.466499 | 2024-09-29 01:32:08 | METOP-B | BARRA DO BUGRES | MATO GROSSO | Brasil | 5101704 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 6f8660e4-c821-3a1d-abad-f61a2f78040a | -15.59 | -57.484501 | 2024-09-29 01:32:08 | METOP-B | BARRA DO BUGRES | MATO GROSSO | Brasil | 5101704 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| d1e22e13-764e-3a27-b8d5-039e0de88422 | -15.5921 | -57.4935 | 2024-09-29 01:32:08 | METOP-B | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 2a6d7b3d-b522-3176-a28b-0d43af85324b | -15.5738 | -57.4599 | 2024-09-29 01:32:09 | METOP-B | BARRA DO BUGRES | MATO GROSSO | Brasil | 5101704 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| bb17a05d-8844-3561-9105-d75c0f1f32c4 | -15.5759 | -57.468899 | 2024-09-29 01:32:09 | METOP-B | BARRA DO BUGRES | MATO GROSSO | Brasil | 5101704 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 05e7723e-d40b-3eca-ad25-66ef4620468c | -15.9263 | -59.5438 | 2024-09-29 01:32:11 | METOP-B | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 40370fc4-c15a-3a73-946c-b6598201d41b | -15.3107 | -58.137299 | 2024-09-29 01:32:15 | METOP-B | RIO BRANCO | MATO GROSSO | Brasil | 5107206 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 6ffc6968-50d0-3590-86b9-54be13fc0ee2 | -15.3009 | -58.139801 | 2024-09-29 01:32:16 | METOP-B | RIO BRANCO | MATO GROSSO | Brasil | 5107206 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 899a6ad0-bf76-339a-acb2-7797604ac966 | -14.8966 | -57.959702 | 2024-09-29 01:32:21 | METOP-B | BARRA DO BUGRES | MATO GROSSO | Brasil | 5101704 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 8f5ac9fb-bdcf-310c-afa9-5bded8425ebc | -14.8888 | -57.970798 | 2024-09-29 01:32:22 | METOP-B | BARRA DO BUGRES | MATO GROSSO | Brasil | 5101704 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 14aec7f5-fb80-38ab-b529-99a3df4c7e3d | -14.8909 | -57.9795 | 2024-09-29 01:32:22 | METOP-B | BARRA DO BUGRES | MATO GROSSO | Brasil | 5101704 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 71e92a05-f345-3278-9ef2-e1003f6b1a63 | -15.0419 | -60.2369 | 2024-09-29 01:32:28 | METOP-B | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| a5db2d17-9ba3-3819-af8b-4d112691949b | -15.0338 | -60.246399 | 2024-09-29 01:32:28 | METOP-B | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| aba313c0-f6cc-32a1-94e0-7d2446dfa58a | -13.4911 | -57.227402 | 2024-09-29 01:32:41 | METOP-B | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| c49c963f-a44a-3781-8a47-87938dc71f56 | -13.4935 | -57.237202 | 2024-09-29 01:32:41 | METOP-B | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| c26d8345-2a74-3c48-a1f0-2369e850de96 | -13.1049 | -56.403801 | 2024-09-29 01:32:44 | METOP-B | NOVA MUTUM | MATO GROSSO | Brasil | 5106224 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 23220c67-57ce-3120-b3fa-36e7a24b26b9 | -13.7406 | -60.0933 | 2024-09-29 01:32:48 | METOP-B | COMODORO | MATO GROSSO | Brasil | 5103304 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| e9afb769-fb6a-3883-b7ee-0941f134818b | -13.7423 | -60.100601 | 2024-09-29 01:32:48 | METOP-B | COMODORO | MATO GROSSO | Brasil | 5103304 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 44273e23-d1a8-364e-bbd5-04529ecc45c0 | -13.7109 | -60.053699 | 2024-09-29 01:32:48 | METOP-B | COMODORO | MATO GROSSO | Brasil | 5103304 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 3a012730-4be1-301d-bba1-47003af57b79 | -13.7093 | -60.681599 | 2024-09-29 01:32:51 | METOP-B | COMODORO | MATO GROSSO | Brasil | 5103304 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 5fc4e993-24b8-39b6-b797-510de1e2afdf | -13.6995 | -60.683899 | 2024-09-29 01:32:51 | METOP-B | COMODORO | MATO GROSSO | Brasil | 5103304 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 669a24c1-af48-3973-8389-d6f8667c7497 | -13.7027 | -60.698299 | 2024-09-29 01:32:51 | METOP-B | COMODORO | MATO GROSSO | Brasil | 5103304 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 8a287632-1601-374b-a901-6f588583ee9a | -13.6653 | -60.669399 | 2024-09-29 01:32:51 | METOP-B | COMODORO | MATO GROSSO | Brasil | 5103304 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 712ba019-9df7-3dac-901e-1b9479d17b77 | -12.9541 | -60.038399 | 2024-09-29 01:33:01 | METOP-B | COMODORO | MATO GROSSO | Brasil | 5103304 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 782f682c-9492-30f4-845b-69cdb3d3d2c9 | -12.8052 | -60.469299 | 2024-09-29 01:33:05 | METOP-B | CHUPINGUAIA | RONDÔNIA | Brasil | 1100924 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| e69db718-cb33-33a4-a141-c60619e88820 | -12.8068 | -60.476601 | 2024-09-29 01:33:05 | METOP-B | CHUPINGUAIA | RONDÔNIA | Brasil | 1100924 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 55e623e2-1a94-3de6-a315-c06d09d0f0d1 | -12.6863 | -60.899101 | 2024-09-29 01:33:08 | METOP-B | CHUPINGUAIA | RONDÔNIA | Brasil | 1100924 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| c5e696d1-4a15-3d3b-8333-201cc2ddb2a3 | -12.9899 | -62.678699 | 2024-09-29 01:33:10 | METOP-B | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 51156e80-f600-33e0-979f-b4a0f4b3c63a | -12.9914 | -62.685799 | 2024-09-29 01:33:10 | METOP-B | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| cd476857-2d0e-33fc-a5f4-d9b1746ac9c9 | -12.9816 | -62.688 | 2024-09-29 01:33:10 | METOP-B | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 38270351-17ad-3cc1-9399-7e0a02839eda | -12.9832 | -62.695099 | 2024-09-29 01:33:10 | METOP-B | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| abf02fce-11ad-32a1-90f5-8afb1c765066 | -12.8091 | -62.231201 | 2024-09-29 01:33:11 | METOP-B | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| c9e5b536-2e5d-3da0-ae44-835718c44fc1 | -12.8707 | -62.6982 | 2024-09-29 01:33:12 | METOP-B | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 58281332-538e-3768-892c-08bb6437c12c | -12.8723 | -62.705299 | 2024-09-29 01:33:12 | METOP-B | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 463af348-d0c3-3c55-b6d4-3f1f981dfad3 | -12.8589 | -62.738098 | 2024-09-29 01:33:12 | METOP-B | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 9eb331ac-0dfe-3b52-8384-2432ed115c9c | -12.8604 | -62.745201 | 2024-09-29 01:33:12 | METOP-B | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 489da8c3-4de2-348b-a74e-2494a953106d | -12.862 | -62.7523 | 2024-09-29 01:33:12 | METOP-B | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| dfd31c36-4f31-383b-ba4a-c01cb983e9ac | -12.7985 | -62.6031 | 2024-09-29 01:33:12 | METOP-B | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| e87198cc-7bf3-35c7-9d10-8ab16dbf5fe3 | -12.8 | -62.6101 | 2024-09-29 01:33:12 | METOP-B | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| a28fcde2-4d86-3021-a13c-285fa3f54107 | -12.7856 | -62.591099 | 2024-09-29 01:33:13 | METOP-B | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 0184600d-c230-32e9-8bb0-9f4d0fe3b565 | -12.7872 | -62.598202 | 2024-09-29 01:33:13 | METOP-B | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 2165ef20-7b4a-33c0-a04b-39f0ff65e391 | -12.7887 | -62.605301 | 2024-09-29 01:33:13 | METOP-B | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 2dec7287-2d8b-3fb7-a9fd-0660a4da0f00 | -12.7903 | -62.612301 | 2024-09-29 01:33:13 | METOP-B | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 9b9fd424-c2f3-33ea-bad3-e106fc4f45b7 | -12.7758 | -62.5933 | 2024-09-29 01:33:13 | METOP-B | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 6ac01724-63f6-3f58-b76f-9233bef41d5f | -12.7774 | -62.600399 | 2024-09-29 01:33:13 | METOP-B | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 69808023-e3e9-30e1-9dba-dfcd833c6a05 | -12.766 | -62.5956 | 2024-09-29 01:33:13 | METOP-B | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 0c41e3c6-3263-3b81-9bae-4d66bf9f6aac | -12.7676 | -62.602699 | 2024-09-29 01:33:13 | METOP-B | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 9db9416b-f3fb-3c61-98f7-8b634a873438 | -12.7842 | -62.725201 | 2024-09-29 01:33:13 | METOP-B | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 2b6b5ef6-2c57-3907-8600-516f76f2efe7 | -12.779 | -62.748699 | 2024-09-29 01:33:13 | METOP-B | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 2e97e092-7b89-3c57-b2ba-97cc47b1b1ac | -12.7641 | -62.774399 | 2024-09-29 01:33:14 | METOP-B | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 5ead9c08-e267-3e74-9233-19bcf0688b4d | -12.7652 | -62.826401 | 2024-09-29 01:33:14 | METOP-B | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 8d9f6776-cebd-3cd7-80a8-af622dc9f06d | -12.7569 | -62.835701 | 2024-09-29 01:33:14 | METOP-B | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 5fe7758d-6bdb-3a14-8105-c9fb7b0b6d62 | -12.7601 | -62.849998 | 2024-09-29 01:33:14 | METOP-B | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| cc695f46-26e7-308a-98fa-9818cc15aa43 | -12.0118 | -61.198399 | 2024-09-29 01:33:20 | METOP-B | PARECIS | RONDÔNIA | Brasil | 1101450 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 463283c7-c7ab-3f78-9d3d-b5e0779baff4 | -12.0134 | -61.205502 | 2024-09-29 01:33:20 | METOP-B | PARECIS | RONDÔNIA | Brasil | 1101450 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 7c3b807e-35c6-3a35-a94b-193d90a4a447 | -12.0149 | -61.212601 | 2024-09-29 01:33:20 | METOP-B | PARECIS | RONDÔNIA | Brasil | 1101450 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 5293ff1d-7931-3a77-a7c6-e76e2041c2bf | -12.2542 | -62.328201 | 2024-09-29 01:33:20 | METOP-B | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 53cc336a-754d-364b-a547-67279a7dc932 | -12.2558 | -62.335201 | 2024-09-29 01:33:20 | METOP-B | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | nan |


[Clique aqui para ver as próximas entradas](README17.md)
