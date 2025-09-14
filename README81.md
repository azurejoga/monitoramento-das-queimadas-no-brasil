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

## Dados Diários - Página 81

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 5f4a897f-eb4b-3128-b4b4-da4d34397a6d | -14.33068 | -46.11263 | 2025-09-14 12:19:00 | TERRA_M-T | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 35.3 |
| b69e4803-d954-33a4-b7c7-f4604a2d6e28 | -15.14392 | -48.58646 | 2025-09-14 12:19:00 | TERRA_M-T | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 6.1 |
| cc66c416-963a-377a-8fd3-6958c933eb70 | -13.94701 | -44.8555 | 2025-09-14 12:19:00 | TERRA_M-T | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 169.4 |
| e3c80980-77d9-3a82-89a3-919e4c028ea9 | -12.92885 | -54.73151 | 2025-09-14 12:19:00 | TERRA_M-T | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 94.6 |
| 6a0fc8af-a46a-3980-be23-05d4e383de3b | -15.43895 | -47.35449 | 2025-09-14 12:19:00 | TERRA_M-T | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 9.9 |
| 52a56bb3-b3e3-39f9-9466-ce24d6aed47d | -18.6361 | -47.19198 | 2025-09-14 12:19:00 | TERRA_M-T | COROMANDEL | MINAS GERAIS | Brasil | 3119302 | 31 | 33 | nan | nan | nan | Cerrado | 8.0 |
| aaa81e9e-d1f0-3b64-af44-1b95399d1efa | -15.75981 | -49.78205 | 2025-09-14 12:19:00 | TERRA_M-T | HEITORAÍ | GOIÁS | Brasil | 5209606 | 52 | 33 | nan | nan | nan | Cerrado | 8.4 |
| 8880d13d-47f5-3e23-ac3a-234d8e201d6e | -16.28863 | -45.67976 | 2025-09-14 12:19:00 | TERRA_M-T | SÃO ROMÃO | MINAS GERAIS | Brasil | 3164209 | 31 | 33 | nan | nan | nan | Cerrado | 11.8 |
| fd532d8c-b28a-30e8-8b23-0af8c0bd404b | -16.39129 | -49.07051 | 2025-09-14 12:19:00 | TERRA_M-T | TEREZÓPOLIS DE GOIÁS | GOIÁS | Brasil | 5221197 | 52 | 33 | nan | nan | nan | Cerrado | 36.2 |
| 85010e67-40bc-349e-9fc0-bfa30ee10f27 | -15.04806 | -47.97327 | 2025-09-14 12:19:00 | TERRA_M-T | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 22.0 |
| 48f5085f-16de-3f4a-8164-be3747235279 | -13.59596 | -51.64919 | 2025-09-14 12:19:00 | TERRA_M-T | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 34.5 |
| c7485bdb-4485-332d-82f6-cf41b37f3ec5 | -14.21714 | -46.20173 | 2025-09-14 12:19:00 | TERRA_M-T | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 8.7 |
| 2f7ec17a-cd61-3d38-bd6b-57febd148df2 | -15.79096 | -53.47141 | 2025-09-14 12:19:00 | TERRA_M-T | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | 35.2 |
| 57ac95c5-0817-3c07-b3e6-d05148ab8ac5 | -15.76806 | -53.46843 | 2025-09-14 12:19:00 | TERRA_M-T | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | 13.9 |
| a753d880-52c7-31ee-ae17-7056774d8398 | -16.43907 | -45.68392 | 2025-09-14 12:19:00 | TERRA_M-T | SÃO ROMÃO | MINAS GERAIS | Brasil | 3164209 | 31 | 33 | nan | nan | nan | Cerrado | 21.8 |
| 4ac9530d-7acd-375b-9735-901696ce1e97 | -20.39279 | -50.51062 | 2025-09-14 12:19:00 | TERRA_M-T | JALES | SÃO PAULO | Brasil | 3524808 | 35 | 33 | nan | nan | nan | Mata Atlântica | 30.3 |
| b59e3d4a-cf76-3a00-9dec-23df2155f64f | -15.18867 | -48.71479 | 2025-09-14 12:19:00 | TERRA_M-T | VILA PROPÍCIO | GOIÁS | Brasil | 5222302 | 52 | 33 | nan | nan | nan | Cerrado | 13.7 |
| 74c92ecf-7a51-3cc4-a05a-3ff1174c578d | -22.78948 | -46.80106 | 2025-09-14 12:19:00 | TERRA_M-T | AMPARO | SÃO PAULO | Brasil | 3501905 | 35 | 33 | nan | nan | nan | Mata Atlântica | 45.8 |
| 8152e9e8-da65-328d-a827-82b59206a0a6 | -15.63201 | -47.29033 | 2025-09-14 12:19:00 | TERRA_M-T | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 8.0 |
| aef1e504-7306-33eb-bc5f-520f982d6f98 | -14.21059 | -46.18082 | 2025-09-14 12:19:00 | TERRA_M-T | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 88.6 |
| d221a48d-54c8-360a-887a-477d0f216cd9 | -15.93247 | -47.24698 | 2025-09-14 12:19:00 | TERRA_M-T | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 6abfdc10-7c02-30e7-80bf-b09d4a837a7e | -15.75072 | -49.78078 | 2025-09-14 12:19:00 | TERRA_M-T | HEITORAÍ | GOIÁS | Brasil | 5209606 | 52 | 33 | nan | nan | nan | Cerrado | 25.6 |
| 9016aa55-76d7-3a9c-a4d0-f5410a5dfc26 | -16.86586 | -49.289 | 2025-09-14 12:19:00 | TERRA_M-T | HIDROLÂNDIA | GOIÁS | Brasil | 5209705 | 52 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 3b1cd6ea-f51a-34c0-9421-f6925ece1c86 | -14.4859 | -47.32446 | 2025-09-14 12:19:00 | TERRA_M-T | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 16.1 |
| 4e3419c2-0f74-3dc6-af00-0124ad0cebfe | -13.12237 | -47.12166 | 2025-09-14 12:19:00 | TERRA_M-T | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 835947bf-bcae-3ba8-82a0-7fc676a81bb8 | -13.18342 | -47.27625 | 2025-09-14 12:19:00 | TERRA_M-T | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 18.9 |
| a6cdc3b0-b7e5-3400-90b2-883f7798f89e | -18.60721 | -47.19776 | 2025-09-14 12:19:00 | TERRA_M-T | COROMANDEL | MINAS GERAIS | Brasil | 3119302 | 31 | 33 | nan | nan | nan | Cerrado | 31.0 |
| af928678-0aa8-3874-8fc8-ff0145fc1547 | -14.17005 | -46.1487 | 2025-09-14 12:19:00 | TERRA_M-T | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 19.4 |
| f5accd59-0b00-3e69-bb19-c233dde6be48 | -12.6636 | -54.6782 | 2025-09-14 12:20:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 97.5 |
| 1b6a24d1-6fbf-369a-8fd7-79b21f190572 | -12.8212 | -47.1445 | 2025-09-14 12:20:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 136.9 |
| 040c2344-7262-35e2-92d4-7dff6bca27ed | -8.9079 | -45.457 | 2025-09-14 12:20:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 137.0 |
| 5ea5d5dd-6ca8-3d21-b1e6-79d9eeb3adcc | -11.502 | -50.7699 | 2025-09-14 12:20:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 157.0 |
| 60a423f0-df43-3367-8c10-5ba1d4279701 | -14.3095 | -46.089 | 2025-09-14 12:20:00 | GOES-19 | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 116.5 |
| 5a6ebc75-54d9-3ad9-b28e-edb7ab4bfc35 | -14.3285 | -46.1088 | 2025-09-14 12:20:00 | GOES-19 | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 139.5 |
| 8af44f92-6870-3e4e-b860-7414b315d0db | -14.31 | -46.066 | 2025-09-14 12:20:00 | GOES-19 | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 78.8 |
| 4bbba580-1ea6-30fa-9e82-e0be44a932e6 | -12.6826 | -54.6763 | 2025-09-14 12:20:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 122.9 |
| f4cb6bbc-ed36-385a-99c3-2c29fbc34774 | -12.9294 | -54.7333 | 2025-09-14 12:20:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 123.2 |
| 3811f364-4d4a-32bc-adca-c07b4f08a9ae | -14.2107 | -46.1749 | 2025-09-14 12:20:00 | GOES-19 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 105.5 |
| 7fe8b14a-f666-3f95-a193-82f7ee47fbbf | -8.9173 | -46.179 | 2025-09-14 12:20:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 94.0 |
| e5c24683-b709-3b48-962f-6f1376857146 | -14.4137 | -52.901 | 2025-09-14 12:20:00 | GOES-19 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 76.1 |
| 0ec4bc13-fcb2-31ae-a6b3-cf837dd9dc08 | -8.979 | -45.7892 | 2025-09-14 12:20:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 73.2 |
| 79af4e60-9a73-385d-bbaf-3f5585da2a81 | -13.9283 | -44.8341 | 2025-09-14 12:20:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 87.6 |
| 23c0ab75-72ea-3c99-aa30-29b7674a78ff | -8.9362 | -46.177 | 2025-09-14 12:20:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 73.7 |
| a69b0493-3825-3d67-a880-10340ccc27fc | -14.1917 | -46.1552 | 2025-09-14 12:20:00 | GOES-19 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 115.6 |
| 31048d36-635e-3de3-bd4c-1afe472df1ad | -15.7786 | -53.482 | 2025-09-14 12:20:00 | GOES-19 | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | 81.8 |
| 32801ef6-0d80-3d16-be3f-b6c0df7141b9 | -8.7683 | -46.0373 | 2025-09-14 12:20:00 | GOES-19 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 105.5 |
| 5a568424-bb9d-33ef-a80f-2dc36e0f334f | -12.7675 | -48.0013 | 2025-09-14 12:20:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 76.8 |
| dd031795-2ed7-3cc3-8e53-3d25ddc744a9 | -12.8208 | -47.1671 | 2025-09-14 12:20:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 186.0 |
| 9de0aeb9-3a04-38bc-82ce-482827204f4e | -11.3831 | -47.3429 | 2025-09-14 12:20:00 | GOES-19 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 77.1 |
| f1e18747-b84c-3f21-9e32-be75e232dd03 | -8.9979 | -45.7871 | 2025-09-14 12:20:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 130.8 |
| 2f256da2-f4dd-3e98-bb8b-1af646d5aefe | -14.1722 | -46.1585 | 2025-09-14 12:20:00 | GOES-19 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 79.2 |
| bd7270fc-a431-3cbb-9697-81a9f9577fd9 | -6.9986 | -44.5512 | 2025-09-14 12:20:00 | GOES-19 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 85.6 |
| 501baf28-b843-3bc1-9b5c-0bc99b77a030 | -8.9976 | -45.8098 | 2025-09-14 12:20:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 102.1 |
| 4be38648-418d-3927-9023-b387ce915ad9 | -12.7871 | -47.9764 | 2025-09-14 12:20:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 73.0 |
| 9cdced62-7dc1-3609-8c43-e8ce3677ed42 | -13.9473 | -44.8541 | 2025-09-14 12:20:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 237.1 |
| 1b732c60-5aa3-34c3-b6f1-fb4155640508 | -8.4334 | -47.2306 | 2025-09-14 12:20:00 | GOES-19 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 72.5 |
| 122512d8-36cb-3e7a-ae0a-f7b1d79de147 | -13.9478 | -44.8306 | 2025-09-14 12:20:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 91.9 |
| f6f90242-0578-3ec2-9ddd-9ea859243ef4 | -14.329 | -46.0857 | 2025-09-14 12:20:00 | GOES-19 | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 179.6 |
| 05be5b7a-2b40-37cb-8407-25b04a2a73d6 | -11.5017 | -50.7912 | 2025-09-14 12:20:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 98.2 |
| bbdd82da-4d86-3820-8f9e-7e8c09fafcdc | -12.8019 | -47.1474 | 2025-09-14 12:20:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 89.6 |
| 9cbc16b7-b3be-3d3c-b349-df60c2642df8 | -12.6824 | -54.6968 | 2025-09-14 12:20:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 85.2 |
| 04576b51-31bd-38d5-9b29-8ad31d5eed95 | -13.9278 | -44.8576 | 2025-09-14 12:20:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 174.4 |
| 5f6dbd91-8744-3c48-a93a-4ca235461571 | -12.6824 | -54.6968 | 2025-09-14 12:30:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 90.0 |
| 93f95ed7-da02-3820-a94c-b427c397e164 | -15.7786 | -53.482 | 2025-09-14 12:30:00 | GOES-19 | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | 128.4 |
| 9fb3234b-b9fc-33f8-bd2a-986a0864e703 | -13.9283 | -44.8341 | 2025-09-14 12:30:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 73.5 |
| f7acf801-b495-3f32-9c18-1594a6eee48f | -8.9976 | -45.8098 | 2025-09-14 12:30:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 222.8 |
| 8cc609db-bb84-37e2-9617-0dca3d57d143 | -8.8987 | -46.1585 | 2025-09-14 12:30:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 87.0 |
| b460f2de-9180-33a8-9b4e-0d855cad13f2 | -8.7683 | -46.0373 | 2025-09-14 12:30:00 | GOES-19 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 198.8 |
| 487ef20c-7461-38a5-894f-66716720762e | -14.1917 | -46.1552 | 2025-09-14 12:30:00 | GOES-19 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 105.2 |
| a8edec68-4347-3547-b456-7a981a8c83bf | -8.6404 | -45.7122 | 2025-09-14 12:30:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 159.8 |
| 5045a353-bc36-3c83-9b21-5fb7a3b97a70 | -14.3095 | -46.089 | 2025-09-14 12:30:00 | GOES-19 | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 118.3 |
| 41b9cd80-bdae-3ee5-8d76-512a11f8342a | -12.6636 | -54.6782 | 2025-09-14 12:30:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 122.1 |
| 9229db79-ba8b-3934-aca7-472f633aa79a | -8.979 | -45.7892 | 2025-09-14 12:30:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 68.7 |
| 3bdf7a63-cec9-304a-9010-b4e74526189d | -8.4334 | -47.2306 | 2025-09-14 12:30:00 | GOES-19 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 135.0 |
| e55c1562-f188-33ef-826e-5ba8914f53db | -11.483 | -50.772 | 2025-09-14 12:30:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 90.6 |
| e7f1b71b-41d2-3925-a658-d87516916834 | -12.6826 | -54.6763 | 2025-09-14 12:30:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 165.0 |
| afa42f1b-7ef9-3aa5-9b57-f03e064ad3ad | -14.1722 | -46.1585 | 2025-09-14 12:30:00 | GOES-19 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 72.7 |
| fcd9cc26-6cf1-3645-a3e8-4a528f272dc5 | -8.9173 | -46.179 | 2025-09-14 12:30:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 87.2 |
| 71289b80-e122-39c6-af9e-4462c3307944 | -14.2107 | -46.1749 | 2025-09-14 12:30:00 | GOES-19 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 92.0 |
| edcb7eca-194f-3820-a049-202d63034a90 | -11.5017 | -50.7912 | 2025-09-14 12:30:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 97.4 |
| ffdf1c56-32d8-32a4-8ea6-81e8ec9e9ab0 | -18.9851 | -48.5844 | 2025-09-14 12:30:00 | GOES-19 | MONTE ALEGRE DE MINAS | MINAS GERAIS | Brasil | 3142809 | 31 | 33 | nan | nan | nan | Cerrado | 115.0 |
| 0d12fcb2-7590-3dfb-aa77-1b9f620ea805 | -12.9294 | -54.7333 | 2025-09-14 12:30:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 97.0 |
| 7149f714-3da2-3b53-843b-4012fdd57f1c | -12.8019 | -47.1474 | 2025-09-14 12:30:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 76.1 |
| c673523a-2aa3-3374-ba30-6dbd360f2e4f | -13.9483 | -44.8072 | 2025-09-14 12:30:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 78.4 |
| 48655bd1-dedd-3dd2-9d36-9434f7af770d | -4.1586 | -38.6978 | 2025-09-14 12:30:00 | GOES-19 | GUAIÚBA | CEARÁ | Brasil | 2304954 | 23 | 33 | nan | nan | nan | Caatinga | 84.5 |
| 3f74f844-d7c2-3644-98ba-42d723b03cb1 | -9.0166 | -45.8077 | 2025-09-14 12:30:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 114.0 |
| b121a96b-1044-3fe7-9542-b1ec66e004b8 | -8.9979 | -45.7871 | 2025-09-14 12:30:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 156.5 |
| 69808564-4a98-3afe-837f-b54caf9f6867 | -12.7675 | -48.0013 | 2025-09-14 12:30:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 65.9 |
| d415e3ba-68d0-377a-9bf5-f5afe8804701 | -12.7671 | -48.0236 | 2025-09-14 12:30:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 74.8 |
| aaf85987-3592-3a26-9414-0600241e6d3a | -8.9176 | -46.1565 | 2025-09-14 12:30:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 77.3 |
| 47280444-0049-3172-81c3-66ed325c27d7 | -14.329 | -46.0857 | 2025-09-14 12:30:00 | GOES-19 | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 298.2 |
| e15f4ea3-4028-31d5-9afc-2e5536e3050c | -8.8109 | -47.1272 | 2025-09-14 12:30:00 | GOES-19 | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 89.8 |
| f3cdea15-9e1d-3ae2-8774-c395c85dcced | -6.9986 | -44.5512 | 2025-09-14 12:30:00 | GOES-19 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 86.0 |
| 4b79bbbc-1a3a-33f3-af1b-06bcd63e88d3 | -14.3285 | -46.1088 | 2025-09-14 12:30:00 | GOES-19 | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 180.8 |
| 63964934-96fd-3f37-b586-ec8d2ac8f249 | -8.9079 | -45.457 | 2025-09-14 12:30:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 118.5 |
| eda8511f-e175-373e-a9d1-470a8448441f | -13.9473 | -44.8541 | 2025-09-14 12:30:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 117.6 |
| d3e31636-65bd-3598-93c1-0af04f68efb3 | -11.502 | -50.7699 | 2025-09-14 12:30:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 169.8 |
| 052b351d-f10e-3fac-b4b5-4a0e5d5c2016 | -12.8208 | -47.1671 | 2025-09-14 12:30:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 109.2 |
| 653a6392-4b70-32f2-8c3d-3607e4a424e9 | -12.8212 | -47.1445 | 2025-09-14 12:30:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 125.9 |
| 486ea14d-636a-3248-9f5e-7cfdd49c6ef6 | -13.9478 | -44.8306 | 2025-09-14 12:30:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 89.7 |


[Clique aqui para ver as próximas entradas](README82.md)
