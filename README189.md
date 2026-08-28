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

## Dados Diários - Página 189

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 4d1e3b7b-88f6-3e64-a8c6-8ce1ae15c0b8 | -5.3117 | -47.0558 | 2026-08-28 22:00:00 | GOES-19 | SENADOR LA ROCQUE | MARANHÃO | Brasil | 2111763 | 21 | 33 | nan | nan | nan | Amazônia | 64.0 |
| 7a3511a2-8f4a-3d54-b663-b04e1db0561c | -12.4305 | -43.3944 | 2026-08-28 22:00:00 | GOES-19 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 31.6 |
| e16c6c81-f1e9-3ad7-a579-c52c47d32b38 | -4.4613 | -43.4945 | 2026-08-28 22:00:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 59.2 |
| d65bb985-f7f8-3ec3-83c4-a3f55c0ef73f | -4.5695 | -44.0427 | 2026-08-28 22:00:00 | GOES-19 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 68.2 |
| c4607174-49fa-372e-afef-9ddbd9f52846 | -4.4427 | -43.4956 | 2026-08-28 22:00:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 79.0 |
| 86c157e7-84f6-3f4a-adb6-6e6d1bce2955 | -5.3453 | -45.1576 | 2026-08-28 22:00:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 68.8 |
| 38a327df-3129-3e4d-976a-3c98fdc0f1e3 | -11.1916 | -51.2708 | 2026-08-28 22:00:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 66.8 |
| a08fb44e-c990-318b-9b9f-27ea12d51490 | -9.1654 | -43.2768 | 2026-08-28 22:00:00 | GOES-19 | CARACOL | PIAUÍ | Brasil | 2202505 | 22 | 33 | nan | nan | nan | Caatinga | 135.6 |
| 8c9fa90f-a02b-3fcb-8e6f-f9b63f070834 | -8.0113 | -48.0161 | 2026-08-28 22:00:00 | GOES-19 | PALMEIRANTE | TOCANTINS | Brasil | 1715705 | 17 | 33 | nan | nan | nan | Cerrado | 85.9 |
| 8a398feb-b862-3263-89bc-660c3e2d1145 | -13.3526 | -43.6395 | 2026-08-28 22:00:00 | GOES-19 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 57.3 |
| 0a930dd9-ae25-3916-9cd9-096697045623 | -12.43 | -43.4182 | 2026-08-28 22:00:00 | GOES-19 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 31.9 |
| 53180720-43a9-360d-b7af-02c119ec168b | -5.6152 | -44.1808 | 2026-08-28 22:00:00 | GOES-19 | SÃO DOMINGOS DO MARANHÃO | MARANHÃO | Brasil | 2110708 | 21 | 33 | nan | nan | nan | Cerrado | 59.0 |
| 53cafc51-9656-36aa-806f-31bfb75dc5c7 | -5.6273 | -44.9343 | 2026-08-28 22:00:00 | GOES-19 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 54.7 |
| 6c1e9854-7a39-3f52-9dc4-b54d037e81da | -5.5964 | -44.1822 | 2026-08-28 22:00:00 | GOES-19 | SÃO DOMINGOS DO MARANHÃO | MARANHÃO | Brasil | 2110708 | 21 | 33 | nan | nan | nan | Cerrado | 77.3 |
| 2cc08d8a-e5af-30c0-8acd-3ae3340a7499 | -11.2106 | -51.2688 | 2026-08-28 22:00:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 57.7 |
| 9f711d45-4c3f-3804-ab62-5995d113f922 | -10.7596 | -54.0384 | 2026-08-28 22:10:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 57.0 |
| 8ffcd60d-cd02-3a41-ae84-e337334ac9d8 | -17.5997 | -51.6028 | 2026-08-28 22:10:00 | GOES-19 | RIO VERDE | GOIÁS | Brasil | 5218805 | 52 | 33 | nan | nan | nan | Cerrado | 148.0 |
| cce5066d-6898-38b2-ba30-8551735e9038 | -14.6414 | -50.909 | 2026-08-28 22:10:00 | GOES-19 | ARUANÃ | GOIÁS | Brasil | 5202502 | 52 | 33 | nan | nan | nan | Cerrado | 122.6 |
| 4133397f-b86d-3f28-8398-6b265fbc643c | -14.2027 | -52.8432 | 2026-08-28 22:10:00 | GOES-19 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 76.4 |
| ad47a5f7-35ed-34e2-b574-e7dd81d52eca | -17.6191 | -51.6214 | 2026-08-28 22:10:00 | GOES-19 | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | 103.2 |
| b396f1a7-6e28-391e-9b95-5846f5a09942 | -7.2847 | -45.8652 | 2026-08-28 22:10:00 | GOES-19 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 63.1 |
| f11f0b2d-4994-35bb-a1d6-c331779ec369 | -14.9015 | -52.6055 | 2026-08-28 22:10:00 | GOES-19 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 92.3 |
| cccef89a-c51b-3846-ac7a-1a5509367bab | -7.2849 | -45.8427 | 2026-08-28 22:10:00 | GOES-19 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 69.6 |
| 153a2548-d52f-3e8c-8af9-7f9bb0a9befe | -2.5042 | -48.1366 | 2026-08-28 22:10:00 | GOES-19 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 35.8 |
| ee364a69-a3d0-3791-82af-05a8309970d9 | -11.2693 | -54.0129 | 2026-08-28 22:10:00 | GOES-19 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 65.8 |
| b881a550-49ae-3c6d-b778-8e18f25cfd4c | -12.7802 | -44.2341 | 2026-08-28 22:10:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 33.2 |
| a8847b83-2026-3665-806d-1b7fe876497e | -9.1651 | -43.3004 | 2026-08-28 22:10:00 | GOES-19 | CARACOL | PIAUÍ | Brasil | 2202505 | 22 | 33 | nan | nan | nan | Caatinga | 138.2 |
| e4ffd090-444e-348f-bbdd-20d9ebb36a32 | -19.0152 | -47.4288 | 2026-08-28 22:10:00 | GOES-19 | IRAÍ DE MINAS | MINAS GERAIS | Brasil | 3131604 | 31 | 33 | nan | nan | nan | Cerrado | 104.1 |
| 5f68fda5-d503-3855-bd17-bb8964257f7a | -9.1464 | -43.2792 | 2026-08-28 22:10:00 | GOES-19 | CARACOL | PIAUÍ | Brasil | 2202505 | 22 | 33 | nan | nan | nan | Caatinga | 194.1 |
| 1f9bffff-c309-311e-a7b0-bb6a36811391 | -12.43 | -43.4182 | 2026-08-28 22:10:00 | GOES-19 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 143.9 |
| 437decd4-8555-3506-91b9-82816c46cd8b | -9.971 | -53.9214 | 2026-08-28 22:10:00 | GOES-19 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 62.5 |
| 521fc63f-2b9c-3fce-9052-e0f55b8b5631 | -12.4305 | -43.3944 | 2026-08-28 22:10:00 | GOES-19 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 90.1 |
| 67351aab-288d-3d77-8608-73544e616d90 | -14.6224 | -50.8901 | 2026-08-28 22:10:00 | GOES-19 | ARUANÃ | GOIÁS | Brasil | 5202502 | 52 | 33 | nan | nan | nan | Cerrado | 82.8 |
| ac30950c-27f4-341e-b806-49d4ac42e30a | -4.2821 | -48.1791 | 2026-08-28 22:10:00 | GOES-19 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 54.2 |
| 2548f03c-17ef-3881-b722-17ac8d9c95f3 | -14.622 | -50.9117 | 2026-08-28 22:10:00 | GOES-19 | ARUANÃ | GOIÁS | Brasil | 5202502 | 52 | 33 | nan | nan | nan | Cerrado | 88.9 |
| a81bbbf2-9bfb-383d-9cc6-752dc3be869b | -14.6418 | -50.8873 | 2026-08-28 22:10:00 | GOES-19 | ARUANÃ | GOIÁS | Brasil | 5202502 | 52 | 33 | nan | nan | nan | Cerrado | 109.9 |
| fc201309-72a5-3d86-94ce-84de5d9a8a66 | -12.7797 | -44.2576 | 2026-08-28 22:10:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 118.5 |
| c0586860-e873-3349-8fd7-f3a9205e246d | -9.1654 | -43.2768 | 2026-08-28 22:10:00 | GOES-19 | CARACOL | PIAUÍ | Brasil | 2202505 | 22 | 33 | nan | nan | nan | Caatinga | 319.8 |
| f1991876-46a5-395e-a240-e3e46a309458 | -8.0113 | -48.0161 | 2026-08-28 22:10:00 | GOES-19 | PALMEIRANTE | TOCANTINS | Brasil | 1715705 | 17 | 33 | nan | nan | nan | Cerrado | 75.6 |
| 1f3222c9-d52c-3437-a061-9d62d4274614 | -12.7608 | -44.2373 | 2026-08-28 22:10:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 31.4 |
| 57fad5a7-ff6a-38c1-b2bb-99ff7cb9a916 | -5.5964 | -44.1822 | 2026-08-28 22:10:00 | GOES-19 | SÃO DOMINGOS DO MARANHÃO | MARANHÃO | Brasil | 2110708 | 21 | 33 | nan | nan | nan | Cerrado | 107.8 |
| bcfa64e3-fefb-3ae3-ac6f-d1288b01ea31 | -11.2103 | -51.2899 | 2026-08-28 22:10:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 69.6 |
| d8dbf899-42cc-3006-95bf-8f929c2255bf | -15.1173 | -53.5687 | 2026-08-28 22:10:00 | GOES-19 | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | 56.9 |
| 05663d44-3ecd-3ae9-90f5-bffb160ebfd7 | -4.5694 | -44.0657 | 2026-08-28 22:10:00 | GOES-19 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 170.5 |
| 1efbefeb-3cbc-3b51-aed5-7e4b631325db | -17.5798 | -51.6061 | 2026-08-28 22:10:00 | GOES-19 | RIO VERDE | GOIÁS | Brasil | 5218805 | 52 | 33 | nan | nan | nan | Cerrado | 90.0 |
| ccbcff19-8fa2-3ec3-ada9-403567717763 | -5.3117 | -47.0558 | 2026-08-28 22:10:00 | GOES-19 | SENADOR LA ROCQUE | MARANHÃO | Brasil | 2111763 | 21 | 33 | nan | nan | nan | Amazônia | 48.8 |
| f75d6280-7bf2-3001-aed2-ba4f9ce66282 | -17.5794 | -51.628 | 2026-08-28 22:10:00 | GOES-19 | RIO VERDE | GOIÁS | Brasil | 5218805 | 52 | 33 | nan | nan | nan | Cerrado | 128.0 |
| ddfc5aa2-53b4-368d-9b15-4a961d40bd42 | -12.4494 | -43.415 | 2026-08-28 22:10:00 | GOES-19 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 52.3 |
| 5b95b7bd-f63e-3d3c-b998-2fd78841ca05 | -9.9708 | -53.9419 | 2026-08-28 22:10:00 | GOES-19 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 84.0 |
| 8ed7f9e1-d64c-301d-8dd2-ecc0eb441ac7 | -5.5962 | -44.2052 | 2026-08-28 22:10:00 | GOES-19 | SÃO DOMINGOS DO MARANHÃO | MARANHÃO | Brasil | 2110708 | 21 | 33 | nan | nan | nan | Cerrado | 84.9 |
| 99d6287d-c6cc-3bae-9e1f-004942f76858 | -17.6195 | -51.5995 | 2026-08-28 22:10:00 | GOES-19 | RIO VERDE | GOIÁS | Brasil | 5218805 | 52 | 33 | nan | nan | nan | Cerrado | 68.2 |
| b82168e1-b8de-39f4-851b-400d9819344d | -12.7603 | -44.2608 | 2026-08-28 22:10:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 115.3 |
| 980a3f9d-0e62-36c3-bf02-d70bc926e51f | -11.1916 | -51.2708 | 2026-08-28 22:10:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 85.2 |
| 8dc8ffd6-fb20-3eee-953c-610820db5ed8 | -11.269 | -54.0334 | 2026-08-28 22:10:00 | GOES-19 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 89.8 |
| a129ddd8-8950-389a-b525-d38fa3253ead | -17.5992 | -51.6247 | 2026-08-28 22:10:00 | GOES-19 | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | 217.6 |
| be73c1ab-fbfe-3d16-8c40-9b09d8bd4b38 | -5.3453 | -45.1576 | 2026-08-28 22:10:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 63.8 |
| eaa58e21-851e-3573-96a6-9625f8c5348d | -14.9011 | -52.6267 | 2026-08-28 22:10:00 | GOES-19 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 118.4 |
| 4ebedbc5-783e-3def-ac16-c715cb4575d7 | -4.282 | -48.2007 | 2026-08-28 22:10:00 | GOES-19 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 61.4 |
| d3af1133-1855-3f1e-80cd-4ac4b9dcb788 | -2.7304 | -47.0424 | 2026-08-28 22:10:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 59.4 |
| b7438ed0-1dd3-3039-b7d9-c949c5a45ddc | -18.995 | -47.4332 | 2026-08-28 22:10:00 | GOES-19 | IRAÍ DE MINAS | MINAS GERAIS | Brasil | 3131604 | 31 | 33 | nan | nan | nan | Cerrado | 88.5 |
| 32c4e147-76af-3217-8367-ba72fdbd7c66 | -4.5695 | -44.0427 | 2026-08-28 22:10:00 | GOES-19 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 90.4 |
| 6e758485-64a2-3195-86ce-fd8499064bf2 | -9.1461 | -43.3027 | 2026-08-28 22:10:00 | GOES-19 | CARACOL | PIAUÍ | Brasil | 2202505 | 22 | 33 | nan | nan | nan | Caatinga | 85.9 |
| 99583aad-eb1e-3374-b353-262c3223f8fe | -5.88 | -57.75 | 2026-08-28 22:15:00 | MSG-03 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 09f888c9-ffa0-3529-8508-48e7a819a432 | -17.59 | -51.63 | 2026-08-28 22:15:00 | MSG-03 | RIO VERDE | GOIÁS | Brasil | 5218805 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| b3cc89b7-d833-30b2-ab3a-17270b045b89 | -6.77 | -55.68 | 2026-08-28 22:15:00 | MSG-03 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f1dad1a3-6ca8-3039-9415-c335190f8e0a | -6.74 | -55.68 | 2026-08-28 22:15:00 | MSG-03 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0c1e13fd-4dc9-39ce-8f86-f364e257e703 | -17.5992 | -51.6247 | 2026-08-28 22:20:00 | GOES-19 | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | 178.5 |
| b2292cf9-564d-3af1-9eea-6608b039d8b7 | -12.4107 | -43.4214 | 2026-08-28 22:20:00 | GOES-19 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 31.6 |
| c82fbc99-0ac1-30d2-87a9-16a980a076f0 | -17.6191 | -51.6214 | 2026-08-28 22:20:00 | GOES-19 | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | 114.4 |
| 27ce5db0-2083-383b-aa4b-aaaf6f86a426 | -3.7386 | -53.3618 | 2026-08-28 22:20:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 67.7 |
| 40d0b664-4601-3e04-a815-059537bd88c5 | -15.6836 | -42.4766 | 2026-08-28 22:20:00 | GOES-19 | RIO PARDO DE MINAS | MINAS GERAIS | Brasil | 3155603 | 31 | 33 | nan | nan | nan | Cerrado | 110.7 |
| 42b4cc31-c19a-38f6-b09a-dae6f31475c2 | -15.6843 | -42.452 | 2026-08-28 22:20:00 | GOES-19 | RIO PARDO DE MINAS | MINAS GERAIS | Brasil | 3155603 | 31 | 33 | nan | nan | nan | Cerrado | 128.0 |
| 9247f9b7-a6df-3fb2-8733-1b6215113161 | -11.1916 | -51.2708 | 2026-08-28 22:20:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 118.5 |
| 665d0a90-6374-366a-84f9-97598a52e9c5 | -8.5171 | -55.3641 | 2026-08-28 22:20:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 46.5 |
| 9cb9f2d7-e11f-3e81-a1e2-3bd8aab874ea | -4.5507 | -44.0668 | 2026-08-28 22:20:00 | GOES-19 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 82.0 |
| 41bf0335-cbef-37ee-b171-090b442ac001 | -3.7571 | -53.341 | 2026-08-28 22:20:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 67.5 |
| e771832c-568c-3169-8236-d0156b846595 | -6.7341 | -55.487 | 2026-08-28 22:20:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 187.5 |
| d4bfb566-d6fd-3de7-b9b5-39f408930089 | -6.6396 | -53.1934 | 2026-08-28 22:20:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 62.0 |
| 75edfe1a-743a-3c0b-86ad-2d378ce5b67c | -6.6397 | -53.173 | 2026-08-28 22:20:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 60.1 |
| 894df631-e678-3cae-8b1a-4cc3d61a36fa | -4.5694 | -44.0657 | 2026-08-28 22:20:00 | GOES-19 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 123.4 |
| 83e653d7-33f5-3657-9cfd-6c2421c25760 | -14.9011 | -52.6267 | 2026-08-28 22:20:00 | GOES-19 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 88.4 |
| 0b123efe-e0e0-3aaf-b1a3-9512fe04bbd6 | -7.4952 | -55.3062 | 2026-08-28 22:20:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 422.0 |
| 860be704-30fa-3740-8cfc-d2a0e22774ba | -12.4494 | -43.415 | 2026-08-28 22:20:00 | GOES-19 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 64.9 |
| 57a8890d-2b24-3c24-9b81-61dfb09186e0 | -9.1464 | -43.2792 | 2026-08-28 22:20:00 | GOES-19 | CARACOL | PIAUÍ | Brasil | 2202505 | 22 | 33 | nan | nan | nan | Caatinga | 304.8 |
| 7fea75a8-cdf9-3269-b0a4-10a9206e0b23 | -14.2027 | -52.8432 | 2026-08-28 22:20:00 | GOES-19 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 69.1 |
| b8e12121-37c0-3db3-a798-73263f9b997b | -14.6414 | -50.909 | 2026-08-28 22:20:00 | GOES-19 | ARUANÃ | GOIÁS | Brasil | 5202502 | 52 | 33 | nan | nan | nan | Cerrado | 71.0 |
| a11e1152-2f70-3273-a37f-85466110af4b | -7.4953 | -55.2862 | 2026-08-28 22:20:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 433.8 |
| 11416e38-16cb-394c-bf29-2211e496cda4 | -9.1651 | -43.3004 | 2026-08-28 22:20:00 | GOES-19 | CARACOL | PIAUÍ | Brasil | 2202505 | 22 | 33 | nan | nan | nan | Caatinga | 307.9 |
| 5b974937-b199-3a08-8e6d-a76de838570d | -4.282 | -48.2007 | 2026-08-28 22:20:00 | GOES-19 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 60.5 |
| 6ba01e25-dad0-34f5-868f-ae8a653cda62 | -6.1743 | -53.4834 | 2026-08-28 22:20:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 35.6 |
| 63951128-ab06-3fa1-b53d-7ca7028d90b6 | -5.5962 | -44.2052 | 2026-08-28 22:20:00 | GOES-19 | SÃO DOMINGOS DO MARANHÃO | MARANHÃO | Brasil | 2110708 | 21 | 33 | nan | nan | nan | Cerrado | 72.9 |
| d4788b2e-a545-3316-9e6a-bc81e65f492f | -10.7596 | -54.0384 | 2026-08-28 22:20:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 68.7 |
| 7eba747f-6cfb-3889-a6c2-d2623ce6b123 | -9.9708 | -53.9419 | 2026-08-28 22:20:00 | GOES-19 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 79.9 |
| 96585dfb-76bf-375d-870e-1622a913ff79 | -8.5359 | -55.3428 | 2026-08-28 22:20:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 64.2 |
| d86ea6fa-1aea-3cb2-aed6-a3322b080c3e | -11.7167 | -54.5244 | 2026-08-28 22:20:00 | GOES-19 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 73.8 |
| f1857e64-6d89-3f18-a00e-6138bf05da3f | -11.2693 | -54.0129 | 2026-08-28 22:20:00 | GOES-19 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 66.6 |
| 27b112df-96da-3bd0-aba0-12e28f01b3db | -8.5358 | -55.3629 | 2026-08-28 22:20:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 40.4 |
| 2542b6a1-f2b0-3623-9a3f-fd88fe31a456 | -14.9193 | -56.3237 | 2026-08-28 22:20:00 | GOES-19 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 73.9 |
| 0c854706-3e5c-36ea-a821-df82414f3fda | -8.5173 | -55.3441 | 2026-08-28 22:20:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 64.4 |
| 9535aa11-6210-372e-aee5-798201a95bcb | -9.1654 | -43.2768 | 2026-08-28 22:20:00 | GOES-19 | CARACOL | PIAUÍ | Brasil | 2202505 | 22 | 33 | nan | nan | nan | Caatinga | 637.5 |


[Clique aqui para ver as próximas entradas](README190.md)
