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

## Dados Diários - Página 38

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| e9e8a3ef-cbd3-3ca3-a368-d67ee86310d8 | -10.77595 | -59.20612 | 2025-09-22 05:31:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| f98f6cad-58f0-34ec-8bff-59db8bc032a1 | -15.94839 | -59.3949 | 2025-09-22 05:31:00 | NOAA-21 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 8.5 |
| ccb79f1e-fdcf-3b1a-996e-325f58cda111 | -12.86941 | -62.09369 | 2025-09-22 05:31:00 | NOAA-21 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 8241364d-ecba-370e-a302-6c8d79f6e4f9 | -15.94794 | -59.39833 | 2025-09-22 05:31:00 | NOAA-21 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 8.5 |
| 91332e63-7597-3a74-9f11-6546272a6b94 | -14.42639 | -60.3001 | 2025-09-22 05:31:00 | NOAA-21 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 3c91178f-52d6-34fe-9d13-b6e7fd05978e | -10.0565 | -68.45454 | 2025-09-22 05:31:00 | NOAA-21 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 42e2f66e-dce1-3800-9fde-86c37bef2d55 | -20.67072 | -54.49218 | 2025-09-22 05:33:00 | NOAA-21 | CAMPO GRANDE | MATO GROSSO DO SUL | Brasil | 5002704 | 50 | 33 | nan | nan | nan | Cerrado | 1.5 |
| dfb16cc7-4cf1-3a8d-9cae-8a8be770151e | -20.54664 | -56.1521 | 2025-09-22 05:33:00 | NOAA-21 | MIRANDA | MATO GROSSO DO SUL | Brasil | 5005608 | 50 | 33 | nan | nan | nan | Cerrado | 4.5 |
| a1a675c6-d31a-3ed9-852e-06a37e2bd71d | -19.64241 | -57.74004 | 2025-09-22 05:33:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 4.4 |
| 578dde1a-a268-3b1c-bec1-4d205749f2ef | -20.50413 | -56.88406 | 2025-09-22 05:33:00 | NOAA-21 | BODOQUENA | MATO GROSSO DO SUL | Brasil | 5002159 | 50 | 33 | nan | nan | nan | Cerrado | 3.0 |
| ba8dbf03-714a-32b2-b5f6-12b088d9559f | -20.55687 | -56.15505 | 2025-09-22 05:33:00 | NOAA-21 | MIRANDA | MATO GROSSO DO SUL | Brasil | 5005608 | 50 | 33 | nan | nan | nan | Cerrado | 0.8 |
| a3b41ea8-8ed6-3f51-a300-4ba738a428eb | -20.26116 | -55.5064 | 2025-09-22 05:33:00 | NOAA-21 | DOIS IRMÃOS DO BURITI | MATO GROSSO DO SUL | Brasil | 5003488 | 50 | 33 | nan | nan | nan | Cerrado | 7.1 |
| c4dab8d4-953d-3f26-9558-070a32964a90 | -19.85436 | -57.29362 | 2025-09-22 05:33:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 4.2 |
| b87d2ed9-b743-367a-bd39-d8c52ade4331 | -20.6127 | -56.71442 | 2025-09-22 05:33:00 | NOAA-21 | BODOQUENA | MATO GROSSO DO SUL | Brasil | 5002159 | 50 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 3d738681-fdd8-304b-b403-656c047dc687 | -20.66486 | -54.49169 | 2025-09-22 05:33:00 | NOAA-21 | CAMPO GRANDE | MATO GROSSO DO SUL | Brasil | 5002704 | 50 | 33 | nan | nan | nan | Cerrado | 10.7 |
| 9b62b4e7-3313-32e5-aace-b098e40ae1c5 | -19.64932 | -57.74204 | 2025-09-22 05:33:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 11.9 |
| 3cba275f-24b4-33d3-94b2-b4be690bb1d6 | -20.50964 | -56.87996 | 2025-09-22 05:33:00 | NOAA-21 | BODOQUENA | MATO GROSSO DO SUL | Brasil | 5002159 | 50 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 6f158bd7-56d8-3bb3-9b3a-60b65e99259d | -20.26191 | -55.49895 | 2025-09-22 05:33:00 | NOAA-21 | DOIS IRMÃOS DO BURITI | MATO GROSSO DO SUL | Brasil | 5003488 | 50 | 33 | nan | nan | nan | Cerrado | 15.9 |
| 0c0c4002-b738-3b25-a3ea-a79a38244f6b | -19.85015 | -57.28739 | 2025-09-22 05:33:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.0 |
| 5873f6b4-1da5-3311-84ce-4dace7f433c9 | -19.86341 | -57.30046 | 2025-09-22 05:33:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.3 |
| 2817fd9f-91ad-3ec4-813c-df1c0fc78b57 | -19.64464 | -57.74142 | 2025-09-22 05:33:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 5.9 |
| 2e17e1c8-9bae-31f7-9a96-308b294973a5 | -20.50908 | -56.88525 | 2025-09-22 05:33:00 | NOAA-21 | BODOQUENA | MATO GROSSO DO SUL | Brasil | 5002159 | 50 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 6b1f8a5a-9e15-3415-9f96-976b255593ef | -20.38267 | -58.05616 | 2025-09-22 05:33:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 10.4 |
| 9c49124b-2b54-3f53-a8de-4ac411a4be95 | -20.47785 | -56.65361 | 2025-09-22 05:33:00 | NOAA-21 | BODOQUENA | MATO GROSSO DO SUL | Brasil | 5002159 | 50 | 33 | nan | nan | nan | Cerrado | 1.7 |
| d1f909ed-2deb-3022-a2de-19418f1a8f58 | -20.51431 | -56.88378 | 2025-09-22 05:33:00 | NOAA-21 | BODOQUENA | MATO GROSSO DO SUL | Brasil | 5002159 | 50 | 33 | nan | nan | nan | Cerrado | 1.7 |
| bf439e8d-117e-336c-a447-1f5cfd5864e0 | -20.54636 | -56.15382 | 2025-09-22 05:33:00 | NOAA-21 | MIRANDA | MATO GROSSO DO SUL | Brasil | 5005608 | 50 | 33 | nan | nan | nan | Cerrado | 2.7 |
| d571eb16-e8d2-3f81-95f6-12537e8b6805 | -20.37285 | -58.06003 | 2025-09-22 05:33:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 4.3 |
| 770a66b1-363f-34de-8b02-fe93957622b7 | -19.85795 | -57.30543 | 2025-09-22 05:33:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.4 |
| a1303edf-6691-35c3-a783-d668b23e4877 | -20.267 | -55.50331 | 2025-09-22 05:33:00 | NOAA-21 | DOIS IRMÃOS DO BURITI | MATO GROSSO DO SUL | Brasil | 5003488 | 50 | 33 | nan | nan | nan | Cerrado | 10.3 |
| be128fb0-ce04-3ed3-bf7e-ec01fd0deaa8 | -19.84953 | -57.293 | 2025-09-22 05:33:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.2 |
| 640c3565-55b2-3146-b7b2-b8958b7df10f | -20.55197 | -56.15103 | 2025-09-22 05:33:00 | NOAA-21 | MIRANDA | MATO GROSSO DO SUL | Brasil | 5005608 | 50 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 25f4059a-ff02-3fa2-bf69-6901a2b5652f | -21.13511 | -54.47937 | 2025-09-22 05:33:00 | NOAA-21 | NOVA ALVORADA DO SUL | MATO GROSSO DO SUL | Brasil | 5006002 | 50 | 33 | nan | nan | nan | Cerrado | 1.8 |
| c9d7be30-497e-3a71-8f9e-ee1e7b888596 | -20.57298 | -54.53399 | 2025-09-22 05:33:00 | NOAA-21 | CAMPO GRANDE | MATO GROSSO DO SUL | Brasil | 5002704 | 50 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 2391fade-8857-3aad-838a-21d4d4e33e0a | -19.63528 | -57.74016 | 2025-09-22 05:33:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 9.3 |
| 15debc3e-fcb2-3bca-956a-9b763b8a5c8a | -19.84469 | -57.29237 | 2025-09-22 05:33:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.2 |
| 0c1fa3d9-3e24-3611-a03b-6eea41f17c6a | -20.60731 | -56.71698 | 2025-09-22 05:33:00 | NOAA-21 | BODOQUENA | MATO GROSSO DO SUL | Brasil | 5002159 | 50 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 74f9a93c-c0ea-35b2-b84d-3d026bdfbec6 | -20.505 | -56.87568 | 2025-09-22 05:33:00 | NOAA-21 | BODOQUENA | MATO GROSSO DO SUL | Brasil | 5002159 | 50 | 33 | nan | nan | nan | Cerrado | 1.2 |
| d063ef99-1042-34a2-977d-03bcdd8caf13 | -19.63996 | -57.74079 | 2025-09-22 05:33:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 5.9 |
| 19d209f5-7f5e-378a-a2b6-2c4808a087e2 | -20.50443 | -56.88113 | 2025-09-22 05:33:00 | NOAA-21 | BODOQUENA | MATO GROSSO DO SUL | Brasil | 5002159 | 50 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 1b584208-4725-3483-831b-6e8c9d3ccee9 | -20.25569 | -55.50586 | 2025-09-22 05:33:00 | NOAA-21 | DOIS IRMÃOS DO BURITI | MATO GROSSO DO SUL | Brasil | 5003488 | 50 | 33 | nan | nan | nan | Cerrado | 7.1 |
| f3455715-f505-382f-8bf0-51285dfe37fe | -19.63305 | -57.73881 | 2025-09-22 05:33:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.5 |
| 1d2ee1bd-d67d-32d5-836c-9e19449ad6db | -20.25606 | -55.50212 | 2025-09-22 05:33:00 | NOAA-21 | DOIS IRMÃOS DO BURITI | MATO GROSSO DO SUL | Brasil | 5003488 | 50 | 33 | nan | nan | nan | Cerrado | 15.9 |
| b2d98ea2-4bf8-3c50-af1a-6f148bb49031 | -19.85498 | -57.28801 | 2025-09-22 05:33:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 5.4 |
| 297f5c02-3f84-3a44-bcfa-d9b445fa142c | -19.84531 | -57.28677 | 2025-09-22 05:33:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.0 |
| e22fe08e-16c6-3d15-925b-5643a921e25a | -19.85858 | -57.29984 | 2025-09-22 05:33:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 4.2 |
| 95f36567-1e7e-340b-9965-c1006f6a9409 | -20.55161 | -56.15451 | 2025-09-22 05:33:00 | NOAA-21 | MIRANDA | MATO GROSSO DO SUL | Brasil | 5005608 | 50 | 33 | nan | nan | nan | Cerrado | 0.8 |
| d476900a-549e-39a8-a18d-e002746c5256 | -19.59092 | -57.73325 | 2025-09-22 05:33:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.5 |
| 6ebe9c3f-30c1-38a0-82e6-26a731dce9d3 | -20.51403 | -56.88646 | 2025-09-22 05:33:00 | NOAA-21 | BODOQUENA | MATO GROSSO DO SUL | Brasil | 5002159 | 50 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 9e0bfa57-5ade-3533-97dc-20dca436811d | -20.26153 | -55.50272 | 2025-09-22 05:33:00 | NOAA-21 | DOIS IRMÃOS DO BURITI | MATO GROSSO DO SUL | Brasil | 5003488 | 50 | 33 | nan | nan | nan | Cerrado | 15.9 |
| 8ec85d69-149f-3d7b-8818-3a43b19e9a2d | -20.37228 | -58.0651 | 2025-09-22 05:33:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 4.3 |
| 0e121289-0447-3f99-8b02-27d96fcd0844 | -20.27284 | -55.50014 | 2025-09-22 05:33:00 | NOAA-21 | DOIS IRMÃOS DO BURITI | MATO GROSSO DO SUL | Brasil | 5003488 | 50 | 33 | nan | nan | nan | Cerrado | 10.3 |
| 8a2ab434-9eb3-3a4c-895f-17644fdc71b4 | -19.85312 | -57.3048 | 2025-09-22 05:33:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.4 |
| 03c9851d-03b7-3661-a5c5-8eded586498e | -20.26737 | -55.49956 | 2025-09-22 05:33:00 | NOAA-21 | DOIS IRMÃOS DO BURITI | MATO GROSSO DO SUL | Brasil | 5003488 | 50 | 33 | nan | nan | nan | Cerrado | 10.3 |
| 338da993-eb9a-3cf5-987a-7c41fcdd431d | -20.50936 | -56.88259 | 2025-09-22 05:33:00 | NOAA-21 | BODOQUENA | MATO GROSSO DO SUL | Brasil | 5002159 | 50 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 89afa84a-1283-34b3-82f9-1741ab832a8e | -20.37748 | -58.06063 | 2025-09-22 05:33:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 4.3 |
| 18de4575-fdec-3008-9915-e68937b64e72 | -20.26776 | -55.49577 | 2025-09-22 05:33:00 | NOAA-21 | DOIS IRMÃOS DO BURITI | MATO GROSSO DO SUL | Brasil | 5003488 | 50 | 33 | nan | nan | nan | Cerrado | 14.6 |
| 4b237d47-b6c8-35a5-ab31-083b75b14795 | -20.55189 | -56.15281 | 2025-09-22 05:33:00 | NOAA-21 | MIRANDA | MATO GROSSO DO SUL | Brasil | 5005608 | 50 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 6b63367c-18f0-37ad-8a5b-79fe51e2fac9 | -20.3873 | -58.05677 | 2025-09-22 05:33:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 10.4 |
| a6cb92dc-4d0a-3abd-ba57-578e16c84eb8 | -20.54672 | -56.15033 | 2025-09-22 05:33:00 | NOAA-21 | MIRANDA | MATO GROSSO DO SUL | Brasil | 5005608 | 50 | 33 | nan | nan | nan | Cerrado | 2.7 |
| a51bda7c-7c13-34ac-843e-e1f5f49150ae | -20.57258 | -54.5382 | 2025-09-22 05:33:00 | NOAA-21 | CAMPO GRANDE | MATO GROSSO DO SUL | Brasil | 5002704 | 50 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 11bd7c0d-2c03-3c04-a84d-9797f842d12f | -20.50994 | -56.87709 | 2025-09-22 05:33:00 | NOAA-21 | BODOQUENA | MATO GROSSO DO SUL | Brasil | 5002159 | 50 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 493d6941-74c7-3ed3-a9ea-45f7f4203de8 | -19.63773 | -57.73942 | 2025-09-22 05:33:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 4.4 |
| 8ecceea7-6800-3024-b673-0a889dd2ec10 | -19.6499 | -57.73686 | 2025-09-22 05:33:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.1 |
| 82b6194d-ceb3-39aa-9dd6-5e5c56fd0a6b | -20.2537 | -55.4959 | 2025-09-22 05:50:00 | GOES-19 | DOIS IRMÃOS DO BURITI | MATO GROSSO DO SUL | Brasil | 5003488 | 50 | 33 | nan | nan | nan | Cerrado | 80.4 |
| 76139668-9e19-32dc-8cd4-a98b9fa146ba | 4.32978 | -60.76965 | 2025-09-22 05:53:00 | NPP-375D | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 374032db-aab8-3e1f-874f-013bf5efad7c | 4.33441 | -60.72034 | 2025-09-22 05:53:00 | NPP-375D | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 3.0 |
| b7d937b0-0a7d-342e-a1fd-3639deb65b15 | 4.33035 | -60.77314 | 2025-09-22 05:53:00 | NPP-375D | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 1.6 |
| dfd9186f-d2a4-38ce-9e92-b3f367a35ac2 | -3.86092 | -63.90498 | 2025-09-22 05:55:00 | NPP-375D | COARI | AMAZONAS | Brasil | 1301209 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f457e4e4-5f1c-35c3-9097-5f42124dc8bd | -3.59721 | -58.58865 | 2025-09-22 05:55:00 | NPP-375D | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 26bc0e50-7f3e-3928-a608-f8e47592b00a | -2.36461 | -67.21325 | 2025-09-22 05:55:00 | NPP-375D | TONANTINS | AMAZONAS | Brasil | 1304237 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 6c215678-2056-37e1-9ae8-845a6c502ed6 | -3.18909 | -58.98598 | 2025-09-22 05:55:00 | NPP-375D | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 41d36516-fa94-3940-a7fd-9895e44b2b15 | -3.18957 | -58.98284 | 2025-09-22 05:55:00 | NPP-375D | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| e0c0ec83-caca-314b-87de-68a8214c809b | -8.33607 | -70.91821 | 2025-09-22 05:57:00 | NPP-375D | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 0.7 |
| a09691b0-3701-38b5-bbc0-93a408f66a8c | -7.24925 | -72.51118 | 2025-09-22 05:57:00 | NPP-375D | GUAJARÁ | AMAZONAS | Brasil | 1301654 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 3054d2ba-797d-3b57-9eea-265f03deda01 | -9.91851 | -65.04333 | 2025-09-22 05:57:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 325490b0-adfb-3264-82c8-cb21755a4145 | -6.63334 | -62.93567 | 2025-09-22 05:57:00 | NPP-375D | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 81829f91-4207-3dca-a79f-f42715cb6765 | -9.28899 | -68.11629 | 2025-09-22 05:57:00 | NPP-375D | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 6e7fa90d-3594-3610-a3ed-dd558bb3de22 | -9.46807 | -67.10178 | 2025-09-22 05:57:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| f5149ced-8907-3985-8b0e-37277a015ba9 | -9.02694 | -68.52129 | 2025-09-22 05:57:00 | NPP-375D | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 35e3d310-dfc1-3517-88ec-820c29fcd2b8 | -10.16455 | -68.6896 | 2025-09-22 05:57:00 | NPP-375D | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 0.8 |
| e2fbeadf-c849-3d78-bf01-0a7070102663 | -9.82021 | -68.89545 | 2025-09-22 05:57:00 | NPP-375D | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 03bc45e5-a423-3a98-b14c-04eef934f81f | -9.91466 | -65.04275 | 2025-09-22 05:57:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f502f7bf-b638-3a11-85ab-e964e2f36745 | -10.16344 | -68.69668 | 2025-09-22 05:57:00 | NPP-375D | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 2.4 |
| be40b44b-973b-3eda-97a0-7a7cb258a9ca | -9.71725 | -69.08067 | 2025-09-22 05:57:00 | NPP-375D | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 4fb2c05e-3e11-3c55-b72d-c1e47782ad5a | -7.56657 | -69.90838 | 2025-09-22 05:57:00 | NPP-375D | ENVIRA | AMAZONAS | Brasil | 1301506 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 5ec483eb-e828-3e07-a816-d88fea79e2f2 | -9.5934 | -68.57814 | 2025-09-22 05:57:00 | NPP-375D | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d250796e-db84-3bd3-bb51-5106b72c5c31 | -9.91503 | -63.5103 | 2025-09-22 05:57:00 | NPP-375D | ARIQUEMES | RONDÔNIA | Brasil | 1100023 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d84bac42-aaf5-30c3-82c8-dd6f992a54a2 | -8.96582 | -63.62584 | 2025-09-22 05:57:00 | NPP-375D | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| b852c2de-ded3-3b01-b4c5-0abf52881d66 | -9.47153 | -67.10231 | 2025-09-22 05:57:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| ab7ba6c1-a5b0-3686-bb20-4093fbff9edc | -9.02639 | -68.5248 | 2025-09-22 05:57:00 | NPP-375D | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 662a15fa-650f-35dd-bb76-b118875ddb47 | -8.82526 | -68.60147 | 2025-09-22 05:57:00 | NPP-375D | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 4756f7cb-d63a-3a26-8476-fcc9ae402d7e | -10.10807 | -64.89161 | 2025-09-22 05:57:00 | NPP-375D | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 333e18ae-7b04-36e2-8b7d-f154dfe4dad9 | -9.49895 | -68.72918 | 2025-09-22 05:57:00 | NPP-375D | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 0.7 |
| a2b01da6-903a-34f2-8133-dd3502991824 | -10.43132 | -61.34107 | 2025-09-22 05:57:00 | NPP-375D | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| afb10bcb-86cd-3044-98d5-4d7a5b1a6fbb | -9.13222 | -65.4659 | 2025-09-22 05:57:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| e2e3f4ff-95c8-37fb-983a-7c4153c00d6d | -7.71488 | -55.45357 | 2025-09-22 05:57:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| d91f80b0-c6b3-3a74-9b56-a1dfcb4b50ab | -9.10413 | -64.00966 | 2025-09-22 05:57:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 7401b03a-27f6-3a04-aa36-2efbcbc41341 | -8.46481 | -70.70528 | 2025-09-22 05:57:00 | NPP-375D | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 33c8bc7f-d6e3-3d8e-9abc-7b1a5f122500 | -8.44482 | -70.76301 | 2025-09-22 05:57:00 | NPP-375D | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 0.7 |
| fa5b3ce2-c76a-3a8c-9127-bfce83ede570 | -10.10417 | -64.89102 | 2025-09-22 05:57:00 | NPP-375D | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |


[Clique aqui para ver as próximas entradas](README39.md)
