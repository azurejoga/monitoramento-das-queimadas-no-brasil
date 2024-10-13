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

## Dados Diários - Página 36

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| eb4164d6-728a-36ae-a6b5-c29f80a539b4 | -17.6478 | -56.2668 | 2024-10-13 03:26:45 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 204.8 |
| bd693024-4b38-33dd-bee9-983919ca1a60 | -17.6672 | -56.2851 | 2024-10-13 03:26:46 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 88.7 |
| d22431e5-61aa-372a-af2d-210c5f17244d | -17.6675 | -56.2643 | 2024-10-13 03:26:46 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 85.8 |
| 3225cf51-63bc-387c-b6a8-9a9a1d23c408 | -17.964 | -57.3843 | 2024-10-13 03:26:47 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 151.9 |
| df22b720-2492-3667-b008-e6c6fb0fff03 | -17.9643 | -57.3637 | 2024-10-13 03:26:47 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 132.2 |
| 8d8ba1ed-bc69-31ed-8750-c80243631f8f | -17.9837 | -57.3819 | 2024-10-13 03:26:47 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 80.0 |
| 01eae839-59e1-3516-9b11-62ef11fd8458 | -17.9841 | -57.3612 | 2024-10-13 03:26:47 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 112.8 |
| 62fe97cb-b1ab-306a-9fc7-008db8c4a78b | -18.2151 | -56.5665 | 2024-10-13 03:26:49 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 104.2 |
| 3607a3d7-e243-3f8e-a124-f7bd31b7f5fa | -18.2155 | -56.5457 | 2024-10-13 03:26:49 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 112.7 |
| 568036c5-051d-347d-8cd0-ce6db6d31b36 | -18.2162 | -56.504 | 2024-10-13 03:26:49 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 96.3 |
| 1b045b66-1e64-325d-85c1-ef2e65466033 | -18.2166 | -56.4832 | 2024-10-13 03:26:49 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 117.7 |
| 4e1c443a-206d-38cd-abf5-4066728543eb | -18.236 | -56.5014 | 2024-10-13 03:26:49 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 163.8 |
| 6bbb16a1-8356-33d5-aaaa-660e0f74d964 | -18.2364 | -56.4806 | 2024-10-13 03:26:49 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 187.9 |
| b84f3063-fc9b-349e-a587-3b1a4db2d25a | -25.61669 | -49.35301 | 2024-10-13 03:28:00 | NPP-375D | CURITIBA | PARANÁ | Brasil | 4106902 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| 252fb0a2-af76-3fc9-abdc-cc8dc16f1613 | -3.0731 | -54.2473 | 2024-10-13 03:35:24 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 54.8 |
| 5a212a2e-37ac-3838-90c7-1ccf46d0e9f5 | -3.0956 | -53.0559 | 2024-10-13 03:35:24 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 119.7 |
| 2900986b-1c9b-3f4f-a5f2-08f9b35390a4 | -3.0957 | -53.0355 | 2024-10-13 03:35:24 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 147.5 |
| a79aee51-897b-3243-858f-46ca7d9a13f9 | -3.114 | -53.0554 | 2024-10-13 03:35:24 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 63.6 |
| ce9d0cf9-d50d-3801-a591-a89e7788c37a | -3.1141 | -53.0351 | 2024-10-13 03:35:24 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 75.0 |
| 94873545-2364-3467-98f5-6be921b5e707 | -3.1791 | -50.476 | 2024-10-13 03:35:24 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 85.7 |
| b08a9403-f94e-31d4-8207-4d6661b1dc1a | -3.1792 | -50.4551 | 2024-10-13 03:35:24 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 119.7 |
| e617bd98-1009-356f-a2e2-6d68a70cf695 | -3.1976 | -50.4545 | 2024-10-13 03:35:24 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 70.8 |
| 996d0889-4b03-37ce-b47c-d7c3ff70a178 | -4.1148 | -48.2515 | 2024-10-13 03:35:30 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 76.4 |
| 26ea290a-3cdd-35c2-8c7f-439d7bd1016a | -4.1149 | -48.2299 | 2024-10-13 03:35:30 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 63.8 |
| 333dd097-3c85-3994-ae27-857795ed5c0a | -4.3985 | -44.4881 | 2024-10-13 03:35:31 | GOES-16 | SÃO LUÍS GONZAGA DO MARANHÃO | MARANHÃO | Brasil | 2111409 | 21 | 33 | nan | nan | nan | Cerrado | 80.5 |
| bb8bd076-9939-3007-a7ca-7f47331fa224 | -4.3986 | -44.4652 | 2024-10-13 03:35:31 | GOES-16 | SÃO LUÍS GONZAGA DO MARANHÃO | MARANHÃO | Brasil | 2111409 | 21 | 33 | nan | nan | nan | Cerrado | 54.5 |
| 367d5913-d8b0-3019-8053-3a9db371ddcc | -7.6815 | -47.3213 | 2024-10-13 03:35:50 | GOES-16 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 87.0 |
| b0a782a1-dc06-385e-98e5-8c813729b689 | -10.5097 | -42.5023 | 2024-10-13 03:36:05 | GOES-16 | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Caatinga | 88.4 |
| d5725125-3f4b-36b5-8d8f-9b94984d780d | -10.5283 | -49.9564 | 2024-10-13 03:36:06 | GOES-16 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 85.1 |
| 4a92aa69-9e17-3dd6-af07-9969bae9bc85 | -10.9502 | -44.6762 | 2024-10-13 03:36:08 | GOES-16 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 43.9 |
| 079837fb-b391-3cd0-8dec-3ce3ebbacc88 | -10.9506 | -44.653 | 2024-10-13 03:36:08 | GOES-16 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 56.7 |
| 8a1f2a6b-a82f-3c3f-8cc0-ce316db530f4 | -11.633 | -48.3956 | 2024-10-13 03:36:12 | GOES-16 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 81.7 |
| 274b4229-fc55-3787-a79f-2c7dbf2c9c49 | -11.6334 | -48.3736 | 2024-10-13 03:36:12 | GOES-16 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 117.6 |
| a3185751-fc2e-3c7b-8ac0-64d13863c0e9 | -11.7308 | -64.9769 | 2024-10-13 03:36:14 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 64.8 |
| 48291353-7fcd-353c-a92e-867beec1860e | -13.7346 | -60.6079 | 2024-10-13 03:36:24 | GOES-16 | COMODORO | MATO GROSSO | Brasil | 5103304 | 51 | 33 | nan | nan | nan | Amazônia | 69.1 |
| 0be155a1-b08d-3df9-9584-4154ebe1de0a | -13.7348 | -60.5883 | 2024-10-13 03:36:24 | GOES-16 | COMODORO | MATO GROSSO | Brasil | 5103304 | 51 | 33 | nan | nan | nan | Amazônia | 48.2 |
| 1853e9a9-1cdc-3121-9504-01c3c4120b1b | -13.7541 | -60.5672 | 2024-10-13 03:36:25 | GOES-16 | COMODORO | MATO GROSSO | Brasil | 5103304 | 51 | 33 | nan | nan | nan | Amazônia | 57.1 |
| a3b25750-fe73-3c97-b55e-08cc61abe342 | -17.1758 | -57.479 | 2024-10-13 03:36:43 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 91.4 |
| da4a8e6e-9e2d-3c73-a5c1-8db9b6e4459b | -17.1761 | -57.4585 | 2024-10-13 03:36:43 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 118.8 |
| 66c2518b-5cd5-381a-862b-e7a8916acc35 | -17.1764 | -57.438 | 2024-10-13 03:36:43 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 55.2 |
| 9c1f7ecd-4b28-3204-93e1-007f10fbf910 | -17.1954 | -57.4767 | 2024-10-13 03:36:43 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 96.0 |
| cfaa1e1d-88a0-3811-9fbe-89e5f2180b99 | -17.1957 | -57.4562 | 2024-10-13 03:36:43 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 122.8 |
| 12f86808-479f-36bc-8bed-07bf83b57643 | -17.196 | -57.4357 | 2024-10-13 03:36:43 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 60.6 |
| 2594e148-95c8-3bae-b408-ac6b6b9b37e9 | -17.6277 | -56.2902 | 2024-10-13 03:36:45 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 68.3 |
| 5c3f8f05-41e1-364c-9b2c-0febd3fb3749 | -17.628 | -56.2694 | 2024-10-13 03:36:45 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 71.2 |
| 2f8ffd45-3021-38f5-8b21-9d70be91ea93 | -17.6474 | -56.2876 | 2024-10-13 03:36:45 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 201.6 |
| e0779727-9507-3daa-b7f3-813db9c3b0c1 | -17.6478 | -56.2668 | 2024-10-13 03:36:45 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 220.9 |
| cb4ec3af-49bf-33f0-ae4d-41ee027ab506 | -17.6672 | -56.2851 | 2024-10-13 03:36:46 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 70.3 |
| fee4cdcb-a1ca-396a-bc24-c521e78e8d52 | -17.6675 | -56.2643 | 2024-10-13 03:36:46 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 76.2 |
| 53833055-da93-3f42-a46d-12f053cf66c5 | -17.964 | -57.3843 | 2024-10-13 03:36:47 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 132.8 |
| e7643d83-21c4-3124-befc-f177600363d2 | -17.9643 | -57.3637 | 2024-10-13 03:36:47 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 120.6 |
| d959b814-67f5-3d20-b069-d0cf6847a9ff | -17.9837 | -57.3819 | 2024-10-13 03:36:47 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 80.6 |
| ab59023c-352e-3e54-be2c-b4f68f254377 | -17.9841 | -57.3612 | 2024-10-13 03:36:47 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 110.8 |
| 6e85b6c7-2228-3fbf-951d-4a9610a266ea | -18.2151 | -56.5665 | 2024-10-13 03:36:49 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 114.2 |
| 06de7bf5-4fe2-34af-9a13-43bb0ac603b3 | -18.2155 | -56.5457 | 2024-10-13 03:36:49 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 105.5 |
| 0a0ab9b3-f19d-3a86-9bfb-08dc8bfc4f3c | -18.2166 | -56.4832 | 2024-10-13 03:36:49 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 96.2 |
| 4d812ba3-1d55-3bd7-867c-5d8a768c3d93 | -18.236 | -56.5014 | 2024-10-13 03:36:49 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 111.6 |
| b662bc7a-4358-3390-8712-c5819c5934a0 | -18.2364 | -56.4806 | 2024-10-13 03:36:49 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 126.6 |
| 153da229-26fa-3a90-9b56-6fdffaa9341b | -3.1792 | -50.4551 | 2024-10-13 03:45:24 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 124.4 |
| 8a9451de-8af8-3e60-9cbf-da5bcd7b3844 | -3.1791 | -50.476 | 2024-10-13 03:45:24 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 96.2 |
| 621811af-f643-37b7-bde2-6ad89439cbf6 | -3.1141 | -53.0351 | 2024-10-13 03:45:24 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 82.2 |
| 064e214e-2be9-3cfc-9e31-bdb31eda3264 | -3.114 | -53.0554 | 2024-10-13 03:45:24 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 66.4 |
| e8d4f2ec-1725-3a30-bc3f-0e2e7d72a8c3 | -3.0957 | -53.0355 | 2024-10-13 03:45:24 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 127.0 |
| 893abf77-ccde-398c-b11c-1abce6b2e951 | -3.0956 | -53.0559 | 2024-10-13 03:45:24 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 89.4 |
| ba0565fc-13cc-3ce2-aca7-5eb5e9b76903 | -3.0773 | -53.036 | 2024-10-13 03:45:24 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 51.0 |
| f4ad5acf-f285-3298-9e4e-146556b4640e | -3.3594 | -47.3271 | 2024-10-13 03:45:25 | GOES-16 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 59.1 |
| f8838671-9cd1-327a-8e1d-03b52601b07e | -3.3409 | -47.3278 | 2024-10-13 03:45:25 | GOES-16 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 57.0 |
| 6258417b-9807-36f9-9709-a5783ee7aec1 | -4.1149 | -48.2299 | 2024-10-13 03:45:30 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 62.9 |
| 6e0ba049-4d26-33a9-884a-7308205091c2 | -4.1148 | -48.2515 | 2024-10-13 03:45:30 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 92.0 |
| 9bb2ce2d-aec8-3f1e-a8bb-5aa87ef71c39 | -4.3985 | -44.4881 | 2024-10-13 03:45:31 | GOES-16 | SÃO LUÍS GONZAGA DO MARANHÃO | MARANHÃO | Brasil | 2111409 | 21 | 33 | nan | nan | nan | Cerrado | 118.1 |
| 8ee0288b-a6ee-3ac6-be5a-8e5771b8d5d8 | -4.3986 | -44.4652 | 2024-10-13 03:45:31 | GOES-16 | SÃO LUÍS GONZAGA DO MARANHÃO | MARANHÃO | Brasil | 2111409 | 21 | 33 | nan | nan | nan | Cerrado | 75.7 |
| c5caa0bb-cc3e-3f0d-a5d6-0c882c20dddd | -7.6627 | -47.3229 | 2024-10-13 03:45:50 | GOES-16 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 77.0 |
| 2b84667e-7b11-33b6-a87d-487336d43906 | -10.9506 | -44.653 | 2024-10-13 03:46:08 | GOES-16 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 99.9 |
| e9bdd331-5f65-30af-9c3a-1135e0e0bc21 | -10.9502 | -44.6762 | 2024-10-13 03:46:08 | GOES-16 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 96.2 |
| 54f5009d-5e04-3be5-bc05-b921c517f3f1 | -10.9315 | -44.6557 | 2024-10-13 03:46:08 | GOES-16 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 83.9 |
| 11e1b355-399d-33b1-8643-85ad9b00f89a | -10.9311 | -44.6789 | 2024-10-13 03:46:08 | GOES-16 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 95.1 |
| 2ad8bf8e-b287-366a-a352-3b7c954cb7c7 | -11.6334 | -48.3736 | 2024-10-13 03:46:12 | GOES-16 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 91.9 |
| 90fec461-734c-3479-9f3e-60aaa25fc19c | -11.7308 | -64.9769 | 2024-10-13 03:46:14 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 60.8 |
| acad4037-5c99-348e-9247-35e8806e3930 | -12.4792 | -63.0159 | 2024-10-13 03:46:18 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 76.4 |
| f9a73737-95be-3f58-b954-56debd9905d2 | -15.6419 | -59.9767 | 2024-10-13 03:46:35 | GOES-16 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 77.9 |
| 9d8eb45d-6159-37db-9289-1329c9dc658a | -16.9995 | -57.4791 | 2024-10-13 03:46:42 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 56.2 |
| b088bd49-7d8c-3f3b-94f5-3aaf9b6f0074 | -17.6478 | -56.2668 | 2024-10-13 03:46:45 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 207.0 |
| beb24304-105a-3409-bd0d-c94d5b162588 | -17.6474 | -56.2876 | 2024-10-13 03:46:45 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 229.3 |
| fd6e2a2d-a038-3cc5-82b1-e5c48e85ab3a | -17.6675 | -56.2643 | 2024-10-13 03:46:46 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 106.4 |
| 778f1ada-936f-33a2-9933-73e01d559085 | -17.6672 | -56.2851 | 2024-10-13 03:46:46 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 111.3 |
| f6be30b0-739a-3ed2-bc91-6d997b1cf62f | -17.9841 | -57.3612 | 2024-10-13 03:46:47 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 102.1 |
| 00d89d4b-b0db-375c-9485-f28b2cd8f29b | -17.9837 | -57.3819 | 2024-10-13 03:46:47 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 79.3 |
| a10ccc03-394e-3509-a787-d8da3e603471 | -17.9643 | -57.3637 | 2024-10-13 03:46:47 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 117.6 |
| fe638abb-ccf6-3d87-b103-3c9adafc4819 | -17.964 | -57.3843 | 2024-10-13 03:46:47 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 112.3 |
| f8a96ebc-af2f-3821-895c-a899834c60f4 | -18.2364 | -56.4806 | 2024-10-13 03:46:49 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 90.5 |
| 44aa83ff-2621-34c0-9f24-e3d34747e0b6 | -18.236 | -56.5014 | 2024-10-13 03:46:49 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 76.8 |
| 75661633-277a-3069-abd0-f5efe624e81a | -18.2166 | -56.4832 | 2024-10-13 03:46:49 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 97.7 |
| 8e81057e-a46e-3b3e-bd4a-bbcf1f2e3273 | -18.2162 | -56.504 | 2024-10-13 03:46:49 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 76.0 |
| c159e31d-a588-3bde-b0c5-cc8b37bbd693 | -18.2155 | -56.5457 | 2024-10-13 03:46:49 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 76.6 |
| 124fd5c9-ab3e-3b88-99af-e7af59358343 | -18.2151 | -56.5665 | 2024-10-13 03:46:49 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 82.4 |
| 01a1edd0-8ec6-32d9-a61e-d2d7583f0d3e | -8.45478 | -34.99603 | 2024-10-13 03:47:00 | NOAA-20 | IPOJUCA | PERNAMBUCO | Brasil | 2607208 | 26 | 33 | nan | nan | nan | Mata Atlântica | 0.4 |
| 7f1c4c6f-83a9-3cf5-9eba-53dea85e81be | -8.69101 | -36.99402 | 2024-10-13 03:47:00 | NOAA-20 | BUÍQUE | PERNAMBUCO | Brasil | 2602803 | 26 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 5e3d3fc0-0c8e-398c-b6fb-8405f11160c5 | -11.86041 | -38.20375 | 2024-10-13 03:47:00 | NOAA-20 | APORÁ | BAHIA | Brasil | 2901908 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.4 |
| 7a6a0855-b572-397a-ab79-e0b443d61d9f | -11.7929 | -38.26451 | 2024-10-13 03:47:00 | NOAA-20 | APORÁ | BAHIA | Brasil | 2901908 | 29 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| f4b823e6-4b39-3a74-9979-eeae060e87fc | -12.77862 | -38.49774 | 2024-10-13 03:47:00 | NOAA-20 | CANDEIAS | BAHIA | Brasil | 2906501 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |


[Clique aqui para ver as próximas entradas](README37.md)
