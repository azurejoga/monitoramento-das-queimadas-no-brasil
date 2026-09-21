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

## Dados Diários - Página 116

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 52763553-5713-34c5-99d3-11e37bcf8d18 | -7.32626 | -54.9221 | 2026-09-21 12:44:00 | TERRA_M-T | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 60.4 |
| 9f23136f-2e63-3e77-8b2b-91109ed17239 | -6.13311 | -59.94508 | 2026-09-21 12:44:00 | TERRA_M-T | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 12.1 |
| d982aa8b-e068-30e0-a8e5-1860b87c9361 | -3.43578 | -59.26025 | 2026-09-21 12:44:00 | TERRA_M-T | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 68c912c8-6d7f-32c9-8030-d90bec2fbf59 | -10.59944 | -53.99173 | 2026-09-21 12:44:00 | TERRA_M-T | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 73.6 |
| 8efcd315-ee03-36d4-bee6-b9c9942b9cef | -6.80179 | -58.79083 | 2026-09-21 12:44:00 | TERRA_M-T | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 8.8 |
| 5940ef4e-2b2f-3633-a33c-24b5ca66f4a5 | -6.5571 | -45.5434 | 2026-09-21 12:50:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 60.3 |
| fa44cbc1-792a-3307-ab7b-b03a098d7d57 | -10.4486 | -50.2644 | 2026-09-21 12:50:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 145.3 |
| 834134d0-beb4-393e-81c2-b3abd0075f3f | -10.3924 | -50.2275 | 2026-09-21 12:50:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 83.1 |
| d689d84c-0d3e-34be-8c0e-4baceafedd23 | -11.9967 | -58.0821 | 2026-09-21 12:50:00 | GOES-19 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 115.6 |
| f0a8321c-8747-3be5-a768-70c0189011db | -8.7911 | -48.7502 | 2026-09-21 12:50:00 | GOES-19 | COLMÉIA | TOCANTINS | Brasil | 1716703 | 17 | 33 | nan | nan | nan | Amazônia | 78.0 |
| 92a882ed-3c5c-3a34-a82b-5b58bfa04bb8 | -5.9335 | -59.9515 | 2026-09-21 12:50:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 91.1 |
| 49f0dfcb-6932-3dd3-8b0f-e4171ad6f98e | -10.09 | -50.2581 | 2026-09-21 12:50:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 81.6 |
| 014a09ef-b9d7-3052-9ab8-2d5e9aadbda1 | -10.7061 | -50.7915 | 2026-09-21 12:50:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 67.2 |
| 0272f225-e339-36c9-8891-30e587f39861 | -10.7437 | -50.8089 | 2026-09-21 12:50:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 69.5 |
| 65547651-1457-3573-be45-d47878128cee | -12.2914 | -50.1633 | 2026-09-21 12:50:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 95.1 |
| 7769f391-891f-367b-8183-6ed4c58ffa7c | -12.8437 | -54.0422 | 2026-09-21 12:50:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 276.4 |
| 31d21117-71d5-37ab-b056-2f63efe5bb31 | -12.9091 | -50.9672 | 2026-09-21 12:50:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 211.3 |
| ba29c963-4871-370c-82df-0530cdccdfbd | -8.7914 | -48.7285 | 2026-09-21 12:50:00 | GOES-19 | COLMÉIA | TOCANTINS | Brasil | 1716703 | 17 | 33 | nan | nan | nan | Amazônia | 64.9 |
| 73bad957-63bc-36e1-8c87-5eca41bdba81 | -8.7726 | -44.28 | 2026-09-21 12:50:00 | GOES-19 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 119.5 |
| f85b7b80-6560-36a0-9d55-986f6657e9d0 | -11.8682 | -46.8529 | 2026-09-21 12:50:00 | GOES-19 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 78.9 |
| 32ad5394-9c8b-384f-a128-395226960761 | -12.8246 | -54.0442 | 2026-09-21 12:50:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 254.8 |
| 459a4c6e-5e39-3def-af0b-c6538f27264b | -11.9507 | -46.5033 | 2026-09-21 12:50:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 66.4 |
| fce8b460-5413-36d8-b92a-acecf6ea17ad | -11.041 | -54.1567 | 2026-09-21 12:50:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 74.4 |
| 11673dda-a50d-39ba-a619-073b9fa757c9 | -13.2794 | -51.7524 | 2026-09-21 12:50:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 103.4 |
| 4867ff82-6368-3bf4-8f8b-d094f6fea092 | -12.4012 | -47.0255 | 2026-09-21 12:50:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 80.1 |
| 5646da41-0a50-377e-8f53-2d0649e15ead | -10.7064 | -50.7703 | 2026-09-21 12:50:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 115.7 |
| 83205aaa-0641-3262-887d-0f675330e890 | -7.3289 | -55.2155 | 2026-09-21 12:50:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 91.8 |
| 35ad7cc4-9907-3d68-b541-382378528de1 | -12.5415 | -50.046 | 2026-09-21 12:50:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 61.1 |
| c0fb4963-4528-3e79-bf61-8871096c32d6 | -7.3291 | -55.1955 | 2026-09-21 12:50:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 153.6 |
| 7679bac1-486e-3ba4-97d9-b0d0ae8b2cb4 | -12.9283 | -50.9648 | 2026-09-21 12:50:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 98.8 |
| 865828d3-cea4-319b-8973-540b1a66056a | -10.8011 | -50.7604 | 2026-09-21 12:50:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 98.9 |
| 874c6104-a240-3ddd-8c18-859f627d562e | -8.7537 | -44.2821 | 2026-09-21 12:50:00 | GOES-19 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 124.8 |
| b3d992db-117b-3d62-a5c5-6a23874e818c | -11.9969 | -58.0622 | 2026-09-21 12:50:00 | GOES-19 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 80.0 |
| 14c477e8-1a5a-3339-85d9-237d5d73116d | -6.8448 | -55.5411 | 2026-09-21 12:50:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 61.7 |
| 57fc151d-33e8-3f3c-ada3-f4b482b6d2a7 | -12.8899 | -50.9695 | 2026-09-21 12:50:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 85.2 |
| 2ffec692-6ccd-3eec-8f82-fb5f173343c7 | -9.4567 | -45.4178 | 2026-09-21 12:50:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 66.2 |
| 8e8cf3f1-0ae7-345d-bfc2-91b861b58dd1 | -12.2723 | -50.1657 | 2026-09-21 12:50:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 79.8 |
| 0151e57a-37ad-3445-9c4e-3e0e3f55c0bc | -11.8014 | -49.8129 | 2026-09-21 12:50:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 100.3 |
| 0b7eeeed-e4bf-329b-a3e7-7d397bfbc405 | -6.2026 | -57.7778 | 2026-09-21 12:50:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 97.8 |
| 520a5e12-bc17-3e21-abe6-421e76a34411 | -13.2602 | -51.7548 | 2026-09-21 12:50:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 68.4 |
| 655d63d7-41dd-3a7d-85c4-3ae2c1668893 | -12.5419 | -50.0243 | 2026-09-21 12:50:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 61.2 |
| d07f5176-3889-3bf6-b1b6-ea55d6d992ca | -14.0607 | -52.1213 | 2026-09-21 12:50:00 | GOES-19 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 71.5 |
| b4c70d8f-cacf-37b2-95d4-6e9941965dd2 | -10.3917 | -48.8915 | 2026-09-21 12:50:00 | GOES-19 | PUGMIL | TOCANTINS | Brasil | 1718451 | 17 | 33 | nan | nan | nan | Cerrado | 97.3 |
| 5a6114cf-dfed-3903-912c-8e674bce8bc1 | -7.428 | -44.7867 | 2026-09-21 12:50:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 93.5 |
| 22f18055-a903-3dfd-a665-7fe1467b342f | -7.4092 | -44.7885 | 2026-09-21 12:50:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 145.2 |
| ea4b41fe-8a4b-3c6a-8cd8-40e00fc0d51c | -10.7262 | -50.7044 | 2026-09-21 12:50:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 113.7 |
| e2db2f0c-58bb-3639-a498-43d262b59394 | -7.5661 | -42.656 | 2026-09-21 12:50:00 | GOES-19 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 169.1 |
| 1cf5171f-509c-3ae3-9d28-9dd274806295 | -13.3443 | -51.2973 | 2026-09-21 12:50:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 76.0 |
| b6d15813-620f-3306-b961-4f81bb82c7ff | -10.0898 | -50.2795 | 2026-09-21 12:50:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 80.5 |
| d301a02e-ae9c-307b-94f2-162458ad7a75 | -10.7259 | -50.7257 | 2026-09-21 12:50:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 103.0 |
| 57f77792-b182-3dcf-876b-8d3a93d6cac0 | -9.0227 | -49.8262 | 2026-09-21 12:50:00 | GOES-19 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 61.4 |
| d9b1f6fb-38bb-3865-abdc-44920cfdb292 | -14.061 | -52.1 | 2026-09-21 12:50:00 | GOES-19 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 79.4 |
| 8612c1a5-75e2-329d-b74a-91bc8fee5060 | -10.744 | -50.7876 | 2026-09-21 12:50:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 96.1 |
| ac47c23f-6421-3c38-9df7-2ee59500aa33 | -10.8662 | -50.156 | 2026-09-21 12:50:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 87.7 |
| 9c40cd42-155c-3d2a-b1c1-8da7603dc67a | -14.1819 | -51.7866 | 2026-09-21 12:50:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 72.1 |
| 0e5fbccf-7479-39e0-9e23-86289486490c | -10.3728 | -48.8936 | 2026-09-21 12:50:00 | GOES-19 | PUGMIL | TOCANTINS | Brasil | 1718451 | 17 | 33 | nan | nan | nan | Cerrado | 77.6 |
| 3d27b1fb-0780-3e09-87e8-dd35f855dcf0 | -6.5759 | -45.5419 | 2026-09-21 12:50:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 75.9 |
| 2315bf04-5818-3372-92ca-54e1b29c223a | -10.4672 | -50.2838 | 2026-09-21 12:50:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 81.3 |
| ca04c512-6c42-3c3e-8c99-7da0c5d6eb8e | -10.0526 | -50.2406 | 2026-09-21 12:50:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 67.0 |
| 8dc2e389-305b-3f79-9cf3-4b6c90d4c69c | -10.4675 | -50.2624 | 2026-09-21 12:50:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 137.5 |
| a711bb13-5457-356b-ac85-8add24129538 | -12.42 | -47.0453 | 2026-09-21 12:50:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 108.4 |
| eacb51da-aeb3-3f59-ae73-a814bf5633d0 | -12.4204 | -47.0228 | 2026-09-21 12:50:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 133.7 |
| 20009e8e-debb-3948-bbc4-e9a45b7aff09 | -11.9507 | -46.5033 | 2026-09-21 13:00:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 70.9 |
| b2c4b371-624f-381b-a84e-facd257b165c | -10.3917 | -48.8915 | 2026-09-21 13:00:00 | GOES-19 | PUGMIL | TOCANTINS | Brasil | 1718451 | 17 | 33 | nan | nan | nan | Cerrado | 123.3 |
| 94f2e306-0b70-3288-bbdc-694108f3a4de | -9.0227 | -49.8262 | 2026-09-21 13:00:00 | GOES-19 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 126.0 |
| 1e01390c-c10f-3393-bb94-6115ae0ccca5 | -10.4486 | -50.2644 | 2026-09-21 13:00:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 108.8 |
| 4b49402d-22fa-3f8e-9e31-be0132ca1dff | -10.7626 | -50.8069 | 2026-09-21 13:00:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 84.8 |
| fd864e8a-f153-31f2-9b11-96eb5b1a5b59 | -7.4124 | -49.853 | 2026-09-21 13:00:00 | GOES-19 | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 93.3 |
| 1c9ef86d-8844-39e6-8378-411d388551aa | -5.9335 | -59.9515 | 2026-09-21 13:00:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 82.6 |
| caaa8dd5-5642-3a79-8a62-3d8326b1c066 | -9.8121 | -48.4312 | 2026-09-21 13:00:00 | GOES-19 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 75.8 |
| 3dfa89d2-7005-3c86-80fa-97b57f2e0108 | -12.2723 | -50.1657 | 2026-09-21 13:00:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 99.5 |
| 78e97c7f-7b4b-3822-8034-9678ed2d8ac1 | -14.1819 | -51.7866 | 2026-09-21 13:00:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 75.8 |
| ad8c1d9f-7b2b-3d4c-a1ee-cb26c429977a | -6.5571 | -45.5434 | 2026-09-21 13:00:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 105.8 |
| 119e67f2-5b01-3c31-aac4-f455110f60aa | -8.7537 | -44.2821 | 2026-09-21 13:00:00 | GOES-19 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 192.6 |
| d8430187-a0ae-3ab8-aedf-f046fc8d922b | -10.8282 | -50.1601 | 2026-09-21 13:00:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 73.6 |
| de0fb9d9-22fb-3cb4-a0ce-5e3ae3cbd489 | -10.7064 | -50.7703 | 2026-09-21 13:00:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 166.6 |
| 96326895-0e99-31f6-a975-1a8bcd2b26c7 | -13.3443 | -51.2973 | 2026-09-21 13:00:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 107.9 |
| b0e7b945-b7b5-33bb-84be-8704a3ed22c2 | -12.42 | -47.0453 | 2026-09-21 13:00:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 122.1 |
| ee6b7aea-48af-336d-8a72-b3dc7ed83226 | -6.2026 | -57.7778 | 2026-09-21 13:00:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 79.6 |
| cd23b8a3-7046-3ef0-b958-48ce22f84049 | -12.8437 | -54.0422 | 2026-09-21 13:00:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 155.0 |
| 6fc3a08c-444d-397b-adbf-1aa2f9837d8d | -10.09 | -50.2581 | 2026-09-21 13:00:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 122.6 |
| 886b01ce-c769-3326-bc1e-6a16f9daf79e | -10.8011 | -50.7604 | 2026-09-21 13:00:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 106.8 |
| d13229dc-c312-39d7-b1fd-4a71dba53246 | -7.3291 | -55.1955 | 2026-09-21 13:00:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 80.9 |
| 2e3ee00c-605f-3c3b-9cbf-1ddefd4ff914 | -13.2596 | -51.7973 | 2026-09-21 13:00:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 76.7 |
| 65856064-633c-32e9-bcdf-fc86180dfb03 | -11.9969 | -58.0622 | 2026-09-21 13:00:00 | GOES-19 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 76.4 |
| 7527afd2-95a6-32ff-bf18-58e432b9228b | -10.7061 | -50.7915 | 2026-09-21 13:00:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 116.9 |
| 72b5395d-156f-39cf-b786-efa15b5e77da | -12.8246 | -54.0442 | 2026-09-21 13:00:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 100.3 |
| 9827dfff-571d-3aef-ab85-c7c0a0032ff2 | -6.8034 | -59.1307 | 2026-09-21 13:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 58.1 |
| 693f1f31-11c8-304c-b5ca-510bd736fa42 | -9.0415 | -49.8245 | 2026-09-21 13:00:00 | GOES-19 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 73.4 |
| 2c9f251f-5a3f-3b91-950f-80541bc6e817 | -11.041 | -54.1567 | 2026-09-21 13:00:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 108.3 |
| e1a88482-1664-38ce-a68a-c6c6e7fbf638 | -10.336 | -50.2119 | 2026-09-21 13:00:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 88.5 |
| 853771dd-30df-3e93-a597-515a31c89bf4 | -9.4567 | -45.4178 | 2026-09-21 13:00:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 66.9 |
| be73022d-918a-395b-b9cf-0ceb91ef9115 | -10.0526 | -50.2406 | 2026-09-21 13:00:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 75.7 |
| 72921e3a-27fa-3526-a10e-c1e3a314268c | -10.7253 | -50.7683 | 2026-09-21 13:00:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 156.3 |
| b56e5ec8-537a-36aa-9f1a-90f1d14ea8ae | -7.3289 | -55.2155 | 2026-09-21 13:00:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 64.4 |
| 522dba62-88d8-3ad9-be33-c196b3f5e5a1 | -6.7464 | -59.4223 | 2026-09-21 13:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 98.4 |
| 0de102e2-1277-3da3-b17f-cd752fe074bc | -10.0898 | -50.2795 | 2026-09-21 13:00:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 130.3 |
| 2c0215c1-969a-34d3-b9d0-0bb6446f7803 | -10.0714 | -50.2387 | 2026-09-21 13:00:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 73.0 |
| 565f8607-2e51-3d9d-9fe3-d7be1ada412b | -6.5759 | -45.5419 | 2026-09-21 13:00:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 155.7 |
| 9e2b67ce-dedd-3583-ae29-456e36920088 | -6.0033 | -44.7247 | 2026-09-21 13:00:00 | GOES-19 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 58.9 |


[Clique aqui para ver as próximas entradas](README117.md)
