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

## Dados Diários - Página 25

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 16824e42-9288-3f88-887b-8c11bf6655f9 | -16.84813 | -49.03218 | 2026-09-05 05:08:00 | NOAA-21 | BELA VISTA DE GOIÁS | GOIÁS | Brasil | 5203302 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 77333f4e-8dbd-30a0-a660-1a51496738ce | -19.75738 | -46.67992 | 2026-09-05 05:08:00 | NOAA-21 | IBIÁ | MINAS GERAIS | Brasil | 3129509 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| c3cd4c83-010a-3487-a6ad-1522e92b87f2 | -21.39292 | -45.50701 | 2026-09-05 05:08:00 | NOAA-21 | TRÊS PONTAS | MINAS GERAIS | Brasil | 3169406 | 31 | 33 | nan | nan | nan | Mata Atlântica | 7.1 |
| 45f3f6b9-f808-363f-9f1b-81e7a1cd2e7d | -20.77294 | -57.93698 | 2026-09-05 05:08:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 0.5 |
| a691d75e-b7be-3988-9503-1552a8a87584 | -18.06372 | -49.05225 | 2026-09-05 05:08:00 | NOAA-21 | BURITI ALEGRE | GOIÁS | Brasil | 5203906 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 96fa7155-8b29-38fe-9331-095be6142d8d | -19.23623 | -46.73054 | 2026-09-05 05:08:00 | NOAA-21 | SERRA DO SALITRE | MINAS GERAIS | Brasil | 3166808 | 31 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 5ad0cff9-07eb-3ab3-b562-2fc581fd8bc3 | -17.10902 | -56.83325 | 2026-09-05 05:08:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 4.4 |
| 8ffea90c-03d7-38f1-bbaa-85d6798218c0 | -20.79547 | -57.87828 | 2026-09-05 05:08:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.9 |
| 3d9e2856-5f16-3e7d-ba3b-f5f4fec0c317 | -19.75887 | -46.6181 | 2026-09-05 05:08:00 | NOAA-21 | IBIÁ | MINAS GERAIS | Brasil | 3129509 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 2fcfc7f0-00d9-30b6-9d35-9408579c95aa | -20.82603 | -46.31077 | 2026-09-05 05:08:00 | NOAA-21 | ALPINÓPOLIS | MINAS GERAIS | Brasil | 3101904 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 1475da4a-c8e3-31b3-b6da-b1ed2e056d8f | -20.82558 | -46.31663 | 2026-09-05 05:08:00 | NOAA-21 | ALPINÓPOLIS | MINAS GERAIS | Brasil | 3101904 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| d0a08aea-0c2e-31e3-926a-37c946d6640c | -14.45244 | -60.10863 | 2026-09-05 05:08:00 | NOAA-21 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| f49b0b7b-9c3c-3042-968a-573087916a10 | -17.10675 | -56.82517 | 2026-09-05 05:08:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 5.6 |
| 9678bb7f-14c3-366d-8426-64cd8b92a089 | -17.15514 | -55.9187 | 2026-09-05 05:08:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.3 |
| 71e90a63-04ee-3774-9ae1-ad990f40ef9f | -16.84851 | -49.02882 | 2026-09-05 05:08:00 | NOAA-21 | BELA VISTA DE GOIÁS | GOIÁS | Brasil | 5203302 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 0c57eda7-0000-365a-83c8-b206aa13e036 | -17.16212 | -55.91979 | 2026-09-05 05:08:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.3 |
| 51d7c75c-aa5f-3278-a8da-9a5f02bd8d26 | -16.39888 | -50.15081 | 2026-09-05 05:08:00 | NOAA-21 | ANICUNS | GOIÁS | Brasil | 5201306 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 712246c7-323f-32e7-97d9-ef26850f207c | -20.79884 | -57.87884 | 2026-09-05 05:08:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.9 |
| 7cfc3e0e-bc35-3856-b5a7-6a76345cc450 | -18.06412 | -49.04837 | 2026-09-05 05:08:00 | NOAA-21 | BURITI ALEGRE | GOIÁS | Brasil | 5203906 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 6a514493-d651-3c28-a24f-959f32c21fbb | -20.78883 | -57.75954 | 2026-09-05 05:08:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.2 |
| 8aeabeb2-2271-32db-aa14-1fcc81121bf6 | -19.76526 | -46.61867 | 2026-09-05 05:08:00 | NOAA-21 | IBIÁ | MINAS GERAIS | Brasil | 3129509 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 6e6c4366-7d2a-3d2e-b071-43d39c69b097 | -19.16418 | -57.33663 | 2026-09-05 05:08:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.1 |
| 62b2919c-34b8-3c67-9943-4aba19e29005 | -20.7539 | -57.87915 | 2026-09-05 05:08:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 0.9 |
| eb87e294-746f-3255-8e49-6c2f1496a182 | -18.8984 | -47.05145 | 2026-09-05 05:08:00 | NOAA-21 | PATROCÍNIO | MINAS GERAIS | Brasil | 3148103 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| f2e87fd8-0ccb-3006-984d-17d935566f0f | -15.01687 | -48.63253 | 2026-09-05 05:08:00 | NOAA-21 | VILA PROPÍCIO | GOIÁS | Brasil | 5222302 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| b404145e-0867-3164-921e-c38812c47c5c | -19.16701 | -57.34099 | 2026-09-05 05:08:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.1 |
| e300fcbe-9142-3c4f-9d34-55446c6fa3b9 | -17.11579 | -56.83434 | 2026-09-05 05:08:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 9.9 |
| 89d4ff80-bcc8-31e7-b6b9-bceefdf750fc | -16.23452 | -57.43376 | 2026-09-05 05:08:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.4 |
| 4d7c67ae-0e77-362d-bc4a-69cc865e1f77 | -17.10958 | -56.82948 | 2026-09-05 05:08:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 4.4 |
| 0f3a280c-ad15-3d43-85c5-dd4665d9491a | -18.89885 | -47.04647 | 2026-09-05 05:08:00 | NOAA-21 | PATROCÍNIO | MINAS GERAIS | Brasil | 3148103 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 395b8f9d-8ffb-3068-a57c-1dc39c5f6f7a | -16.23507 | -57.43011 | 2026-09-05 05:08:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.4 |
| 2269cb1b-ef83-3133-986d-dee40e87ca51 | -20.80178 | -57.76563 | 2026-09-05 05:08:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.2 |
| e2d1c9e7-1e34-3704-a71a-5f813506a74e | -21.5212 | -50.02688 | 2026-09-05 05:08:00 | NOAA-21 | PENÁPOLIS | SÃO PAULO | Brasil | 3537305 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 24b4a613-c8d7-37e9-b394-61711ebe671d | -20.76508 | -57.94345 | 2026-09-05 05:08:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.0 |
| e03b645f-870a-315e-b2c5-c8a620f57051 | -17.17259 | -55.92142 | 2026-09-05 05:08:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.6 |
| 0ff0946a-79f2-3d1b-8e9b-0304be8d935d | -17.1124 | -56.83379 | 2026-09-05 05:08:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 4.4 |
| aeb0647c-516e-3d83-a5c6-4e0253e4f7b4 | -17.10007 | -56.87034 | 2026-09-05 05:08:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.1 |
| 6d6b15d3-0320-3572-be2e-53bd0e29b785 | -21.46362 | -48.67259 | 2026-09-05 05:08:00 | NOAA-21 | TAQUARITINGA | SÃO PAULO | Brasil | 3553708 | 35 | 33 | nan | nan | nan | Cerrado | 3.0 |
| fa21a02b-cdca-3952-8312-280424c81102 | -20.60515 | -46.37394 | 2026-09-05 05:08:00 | NOAA-21 | SÃO JOÃO BATISTA DO GLÓRIA | MINAS GERAIS | Brasil | 3162203 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| e6933a5d-937b-3f85-ba42-fb664cb5e0e2 | -21.52086 | -50.03026 | 2026-09-05 05:08:00 | NOAA-21 | PENÁPOLIS | SÃO PAULO | Brasil | 3537305 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| dd96c0bf-2f71-349a-9233-74541c8b0105 | -16.23175 | -57.42957 | 2026-09-05 05:08:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.4 |
| a4656ab6-407e-3520-81cc-645dc93442be | -19.1614 | -57.35567 | 2026-09-05 05:08:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.9 |
| fa208bed-42db-35c9-a537-75aadf499885 | -20.79277 | -57.75626 | 2026-09-05 05:08:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.3 |
| b35e77c7-2343-3f14-bc52-8cb8462aae02 | -20.76845 | -57.94402 | 2026-09-05 05:08:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.0 |
| 92d7751a-771f-3531-b85e-9b2e590eeb68 | -17.23288 | -53.86254 | 2026-09-05 05:08:00 | NOAA-21 | ITIQUIRA | MATO GROSSO | Brasil | 5104609 | 51 | 33 | nan | nan | nan | Cerrado | 4.5 |
| b85efcb0-1758-3ee6-ab07-9a9f1053aade | -17.1691 | -55.92088 | 2026-09-05 05:08:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.6 |
| 96bdf55b-ddef-3e5f-8da3-a7dfd27da5ba | -16.40916 | -51.10793 | 2026-09-05 05:08:00 | NOAA-21 | IPORÁ | GOIÁS | Brasil | 5210208 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 4e01a73c-f6ce-32df-98ea-88499eb33b1f | -17.11296 | -56.83002 | 2026-09-05 05:08:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 4.4 |
| 8449021c-48f2-39f8-80d4-dee72a9f5d65 | -20.60553 | -46.36936 | 2026-09-05 05:08:00 | NOAA-21 | SÃO JOÃO BATISTA DO GLÓRIA | MINAS GERAIS | Brasil | 3162203 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 8cbaf517-1784-307c-a42f-8dd40fb289fa | -19.15857 | -57.3513 | 2026-09-05 05:08:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.9 |
| 6f941ef1-439f-3fcf-99e5-80969f22cc26 | -19.75388 | -46.67827 | 2026-09-05 05:08:00 | NOAA-21 | IBIÁ | MINAS GERAIS | Brasil | 3129509 | 31 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 93b5ac8a-db4b-3e5e-82ba-adb30a5afe8a | -11.90454 | -64.99423 | 2026-09-05 05:08:00 | NOAA-21 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 23f5654a-fcb1-3a87-b462-ebc2dce06d49 | -17.60513 | -48.25364 | 2026-09-05 05:08:00 | NOAA-21 | IPAMERI | GOIÁS | Brasil | 5210109 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| bf4d175c-7adf-302c-b43f-d4c8cb716a4b | -17.15863 | -55.91924 | 2026-09-05 05:08:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.3 |
| 59d9c74b-cc70-381f-b910-4570732be54a | -15.01725 | -48.62912 | 2026-09-05 05:08:00 | NOAA-21 | VILA PROPÍCIO | GOIÁS | Brasil | 5222302 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| d4d5990d-909f-3d63-85f4-24bbfc8ed2fc | -20.78939 | -57.7557 | 2026-09-05 05:08:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 5.2 |
| 10b7643d-37a8-3cfb-95db-ebd46b5dbf7e | -15.47603 | -60.05833 | 2026-09-05 05:08:00 | NOAA-21 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c4e30702-da11-3644-8623-d9a83e45f9cd | -17.15165 | -55.91816 | 2026-09-05 05:08:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 4.1 |
| 982004d1-86d6-3daf-9448-e405842774d3 | -15.94968 | -49.47062 | 2026-09-05 05:08:00 | NOAA-21 | JARAGUÁ | GOIÁS | Brasil | 5211800 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| f2c0a0f2-1927-3ec4-81fe-efad8ce9e82e | -20.75446 | -57.89877 | 2026-09-05 05:08:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.9 |
| 23c144c4-679f-3645-9be8-c713b608f19c | -21.46325 | -48.67691 | 2026-09-05 05:08:00 | NOAA-21 | TAQUARITINGA | SÃO PAULO | Brasil | 3553708 | 35 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 1defb005-a61b-3f5e-a144-882b07caa360 | -14.74201 | -47.14738 | 2026-09-05 05:08:00 | NOAA-21 | VILA BOA | GOIÁS | Brasil | 5222203 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 578ae2f4-0e52-302b-8361-4ca6991e21e5 | -19.75787 | -46.67453 | 2026-09-05 05:08:00 | NOAA-21 | IBIÁ | MINAS GERAIS | Brasil | 3129509 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 225a99cf-c56d-3aeb-b922-aafd40c08250 | -21.4616 | -48.67624 | 2026-09-05 05:08:00 | NOAA-21 | TAQUARITINGA | SÃO PAULO | Brasil | 3553708 | 35 | 33 | nan | nan | nan | Cerrado | 4.6 |
| aafd94ab-3e57-31b8-a5d1-10c2a9057a04 | -17.10615 | -56.80576 | 2026-09-05 05:08:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 5.9 |
| 0f6da620-cf8a-387e-a85d-5174ac0f4c6b | -17.11635 | -56.83057 | 2026-09-05 05:08:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 9.9 |
| 2c5e45ac-a9c4-32f7-aae9-81cb0cc8834d | -20.75502 | -57.89497 | 2026-09-05 05:08:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.9 |
| 85148219-18d9-38ae-b28d-0cc6eaf760cc | -17.10619 | -56.82894 | 2026-09-05 05:08:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 5.2 |
| 41aad895-d62e-36aa-b64f-e62e0b9065fd | -17.1078 | -56.8304 | 2026-09-05 05:10:00 | GOES-19 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 72.3 |
| c281a367-b0ba-30b7-b4b0-29604c82c208 | -5.346 | -56.0454 | 2026-09-05 05:10:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 79.9 |
| bbda4894-14dd-3f04-b0d4-1f5c4f265f2c | -5.3277 | -56.0263 | 2026-09-05 05:10:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 64.4 |
| cb091170-82ed-3485-aca2-b353f1fc66dc | -6.6514 | -59.945 | 2026-09-05 05:10:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 239.1 |
| 30fa7098-435b-3391-8f9a-ac27c476982b | -5.3462 | -56.0256 | 2026-09-05 05:10:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 117.1 |
| fa3dfe51-5792-3d93-91b9-1756ee7a3d29 | -3.7827 | -61.7733 | 2026-09-05 05:10:00 | GOES-19 | ANORI | AMAZONAS | Brasil | 1300102 | 13 | 33 | nan | nan | nan | Amazônia | 40.4 |
| 7692efd9-1d8d-3b85-8013-9e7f267a72ef | -6.6513 | -59.9642 | 2026-09-05 05:10:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 143.7 |
| ffaa71ce-3ced-302d-a47f-03f3fa741a3f | -6.6698 | -59.9443 | 2026-09-05 05:10:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 168.5 |
| 5f7e1b99-0f36-3266-9b37-05b174faaad8 | -6.6697 | -59.9635 | 2026-09-05 05:10:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 100.9 |
| 0b0b7b35-684c-3091-a2a8-01570c9e1371 | -3.7645 | -61.7548 | 2026-09-05 05:20:00 | GOES-19 | ANORI | AMAZONAS | Brasil | 1300102 | 13 | 33 | nan | nan | nan | Amazônia | 43.2 |
| dfb43415-2680-3afa-b1b1-38cd762cd4eb | -6.6515 | -59.9258 | 2026-09-05 05:20:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 91.6 |
| eec6b90a-2b4a-3838-b50c-700bf655a56a | -6.6514 | -59.945 | 2026-09-05 05:20:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 242.1 |
| 0ab1f49e-9751-3ca8-a183-1dc0a4b3bee8 | -5.3277 | -56.0263 | 2026-09-05 05:20:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 64.5 |
| 2b0c0604-e4a0-34ef-9abf-a9935bb9c37f | -6.6513 | -59.9642 | 2026-09-05 05:20:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 57.5 |
| 3f3c015b-f4af-3af8-a9c0-333d0c453418 | -6.6698 | -59.9443 | 2026-09-05 05:20:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 178.9 |
| 178e9e20-385b-3d8c-a2ca-73588395fe89 | -6.6697 | -59.9635 | 2026-09-05 05:20:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 50.3 |
| 21d43ec0-de6c-3df2-bcf1-46c809c35967 | -5.3463 | -56.0059 | 2026-09-05 05:20:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 58.7 |
| daa59615-297b-3e8e-acd7-201a81360387 | -6.6699 | -59.9251 | 2026-09-05 05:20:00 | GOES-19 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 77.8 |
| 057590d6-c091-37ce-9bdf-72f5977ec574 | -5.3462 | -56.0256 | 2026-09-05 05:20:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 111.7 |
| eb7d0373-4f76-3dc4-ae64-e04c09f389a4 | -5.346 | -56.0454 | 2026-09-05 05:30:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 64.8 |
| 8b7f2559-e745-320b-870f-0a07dd7f8e04 | -3.7645 | -61.7737 | 2026-09-05 05:30:00 | GOES-19 | ANORI | AMAZONAS | Brasil | 1300102 | 13 | 33 | nan | nan | nan | Amazônia | 38.9 |
| 6d9f7fe4-8752-3e7e-bd7e-1bab265a9ccb | -5.3462 | -56.0256 | 2026-09-05 05:30:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 105.4 |
| cf1c4a8d-18d5-3255-91e3-4c1352fa109b | -5.3277 | -56.0263 | 2026-09-05 05:30:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 60.7 |
| 90af017e-890a-34bd-8622-65737bd449b2 | -3.7645 | -61.7548 | 2026-09-05 05:30:00 | GOES-19 | ANORI | AMAZONAS | Brasil | 1300102 | 13 | 33 | nan | nan | nan | Amazônia | 44.0 |
| 78c61494-51a8-3104-9ef9-5ed34878a871 | 4.35917 | -59.73852 | 2026-09-05 05:38:00 | NPP-375D | UIRAMUTÃ | RORAIMA | Brasil | 1400704 | 14 | 33 | nan | nan | nan | Amazônia | 0.9 |
| be5d4f11-091f-34ef-99d2-e5e679c9ec21 | 4.39618 | -59.73623 | 2026-09-05 05:38:00 | NPP-375D | UIRAMUTÃ | RORAIMA | Brasil | 1400704 | 14 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 05d84f37-1587-338b-b1a0-80a19dec2d0e | 4.39286 | -59.73675 | 2026-09-05 05:38:00 | NPP-375D | UIRAMUTÃ | RORAIMA | Brasil | 1400704 | 14 | 33 | nan | nan | nan | Amazônia | 1.1 |
| af4a0210-a0be-3ab5-a23e-0bc9564d8563 | 2.69686 | -60.12077 | 2026-09-05 05:38:00 | NPP-375D | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 9f049969-b47b-3e2a-b188-6e3fa6e60a27 | 4.21192 | -60.60288 | 2026-09-05 05:38:00 | NPP-375D | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 7b5e23ad-72f6-3524-9b46-5f8996ad54c0 | 2.37878 | -50.75804 | 2026-09-05 05:38:00 | NPP-375D | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 9fc5d88c-8428-3503-b05e-dd08199ab90a | 4.88493 | -60.108 | 2026-09-05 05:38:00 | NPP-375D | UIRAMUTÃ | RORAIMA | Brasil | 1400704 | 14 | 33 | nan | nan | nan | Amazônia | 0.6 |
| f7f6f1a8-d132-3f74-bca9-c97baf951406 | 4.94976 | -60.17575 | 2026-09-05 05:38:00 | NPP-375D | UIRAMUTÃ | RORAIMA | Brasil | 1400704 | 14 | 33 | nan | nan | nan | Amazônia | 0.4 |


[Clique aqui para ver as próximas entradas](README26.md)
