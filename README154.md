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

## Dados Diários - Página 154

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| da8a939e-17ea-35b3-a797-3a1fde6926b1 | -17.05336 | -56.71032 | 2024-10-01 05:48:00 | AQUA_M-M | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 21.0 |
| 6cfbcf60-0766-38fd-ad24-20775722d23d | -19.15986 | -57.47015 | 2024-10-01 05:48:00 | AQUA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 7.1 |
| 187dfee5-bc69-3d28-8fd3-cb9607fed6c7 | -19.12285 | -57.46369 | 2024-10-01 05:48:00 | AQUA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 59.6 |
| 6b639d9b-2111-3b0e-8c6f-b30218ea79d7 | -19.12121 | -57.47379 | 2024-10-01 05:48:00 | AQUA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 12.0 |
| b67679f7-22f2-3b85-9f12-87c6682e7276 | -19.11794 | -57.45601 | 2024-10-01 05:48:00 | AQUA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 9.5 |
| 0a92359c-e0fe-3a7b-8734-c79db79bc6f3 | -18.71321 | -57.31852 | 2024-10-01 05:48:00 | AQUA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 11.8 |
| 9ea056e2-c1a7-3588-a0e7-d9d925d7ff80 | -18.70561 | -57.30676 | 2024-10-01 05:48:00 | AQUA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 15.4 |
| fcf1eab8-f884-3792-bb88-6899fe356f93 | -18.70398 | -57.31691 | 2024-10-01 05:48:00 | AQUA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 93.4 |
| b3553f85-0b78-3e55-a376-9282c85854e0 | -18.70234 | -57.32706 | 2024-10-01 05:48:00 | AQUA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 86.2 |
| 5816bf2f-629f-37b8-aed9-c80ffc5c9151 | -18.69474 | -57.3153 | 2024-10-01 05:48:00 | AQUA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 21.9 |
| baf1c522-6157-305d-b647-1f2b97e016ad | -18.69311 | -57.32545 | 2024-10-01 05:48:00 | AQUA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 65.6 |
| ab5126e9-db5d-36aa-aa1f-bf5ca3df4626 | -18.68387 | -57.32384 | 2024-10-01 05:48:00 | AQUA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 16.2 |
| 3d04a1d0-8f3f-397a-95bc-5fb5306b36f8 | -17.15943 | -56.15224 | 2024-10-01 05:48:00 | AQUA_M-M | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 83.7 |
| e46146c9-32e3-39b6-adb6-68da0b1e939e | -11.57421 | -63.80462 | 2024-10-01 05:53:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 1137bcd7-8ba3-3e73-80dc-e4e142fb56be | -11.57 | -63.80404 | 2024-10-01 05:53:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 3c29fb06-6867-38e5-a552-6ba406719aab | -11.56948 | -63.80794 | 2024-10-01 05:53:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 2.4 |
| b57160d3-f2a1-3e28-8e92-62f41b16a92e | -11.56895 | -63.81184 | 2024-10-01 05:53:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 316e2f80-60b2-3bf8-a2b8-f64c06386412 | -11.56843 | -63.81575 | 2024-10-01 05:53:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 3f75ff14-158f-3a1a-ad89-4c87c799b4e3 | -11.56422 | -63.81518 | 2024-10-01 05:53:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 7e4a617b-2289-3715-a0c6-94929ac2fbfb | -11.5637 | -63.81909 | 2024-10-01 05:53:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 250660a2-5a62-39ee-b024-d67958b90d1b | -11.56318 | -63.82299 | 2024-10-01 05:53:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 021e6ccc-c996-3e72-9625-c45aa98dcdb0 | -11.56265 | -63.82688 | 2024-10-01 05:53:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 577cd06c-d8a2-3a93-af39-d69e3a06330e | -11.56213 | -63.83078 | 2024-10-01 05:53:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 6ce30896-06e5-3064-b694-71d15981a2e6 | -11.55897 | -63.82242 | 2024-10-01 05:53:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 8dfa9608-956e-3071-8e2c-6f1b6737435b | -11.55845 | -63.82631 | 2024-10-01 05:53:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 4836e89f-eab4-37f1-b162-602ed6a7704c | -11.55793 | -63.83022 | 2024-10-01 05:53:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| a92fed63-3726-3993-929c-63e12b7168c6 | -11.55163 | -63.84529 | 2024-10-01 05:53:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 5a7c05a2-2629-3e32-a7de-1edc343d7b7e | -11.55157 | -63.71832 | 2024-10-01 05:53:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 62bf22ba-bad6-3078-b2e8-51e3e2bc3e8a | -11.55088 | -63.84607 | 2024-10-01 05:53:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| be8661bb-a93f-38c3-b1e0-b989601f3eea | -11.55033 | -63.84996 | 2024-10-01 05:53:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| d1763ff2-fcac-3229-bbe0-041389fccca5 | -11.54692 | -63.84856 | 2024-10-01 05:53:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 7fb2eb7a-de07-3b9f-aa43-04dafceabe6a | -11.54614 | -63.84934 | 2024-10-01 05:53:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 87491a81-a9fa-333a-a561-f5444d514bfa | -11.53947 | -63.71224 | 2024-10-01 05:53:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| bde0e4a7-bed2-38fd-a611-3f39cab0ba4e | -11.53634 | -63.70365 | 2024-10-01 05:53:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 2.7 |
| fa1c13a2-04a8-35c2-98f3-ecb4d05aad50 | -11.66706 | -64.99557 | 2024-10-01 05:53:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 0042ade9-d174-3767-91ef-0a7efc8f1f0d | -11.66635 | -65.0006 | 2024-10-01 05:53:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 54282672-5e19-37bd-924b-58c9ebadc1a7 | -11.66613 | -65.19669 | 2024-10-01 05:53:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 3.0 |
| af32bde7-5a09-3060-98b8-4ac2889352d4 | -11.66386 | -64.99001 | 2024-10-01 05:53:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 2.7 |
| fe5d4c4c-b88d-3468-914f-b1515c03adce | -11.66315 | -64.99502 | 2024-10-01 05:53:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 68c3be5a-2793-3281-92a4-dd503c379628 | -11.66244 | -65.00005 | 2024-10-01 05:53:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 7487e8d9-c3aa-3977-978c-e0dbd356f907 | -11.66214 | -65.03038 | 2024-10-01 05:53:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 48392b3f-3779-38ad-85ff-91e6d6c9595e | -11.65995 | -64.98945 | 2024-10-01 05:53:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 17c4e94c-7abf-3c63-a44b-2b5eb19f8033 | -11.65924 | -64.99448 | 2024-10-01 05:53:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 58971989-0af6-3bb1-82cb-a68dc63a7c48 | -11.65854 | -64.9995 | 2024-10-01 05:53:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 3.4 |
| fca69c80-4143-3dd0-8d4d-d7af15355d1b | -11.65783 | -65.00451 | 2024-10-01 05:53:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 020444ac-c4ea-348f-9da5-af4cabc71b4a | -11.65675 | -64.98388 | 2024-10-01 05:53:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 2.6 |
| fab0b120-5152-3845-9b2a-72ef831136d7 | -11.65605 | -64.98889 | 2024-10-01 05:53:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 457fc8ea-440b-3c2f-9228-1d1fd153451c | -11.65534 | -64.99393 | 2024-10-01 05:53:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 4.2 |
| c14b116a-0944-3c2d-89e6-c18e4199a2b5 | -11.65463 | -64.99895 | 2024-10-01 05:53:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 683cf0e0-923c-3361-a4bf-b498637e1894 | -11.65393 | -65.00395 | 2024-10-01 05:53:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 0c8d12f3-54b8-3e03-82e2-e61ea5bc46ba | -11.65323 | -65.00893 | 2024-10-01 05:53:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 15e5a6da-7997-3011-b5fa-9028cebb43c4 | -11.65214 | -64.98834 | 2024-10-01 05:53:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 7ec98abe-ad59-331b-ba54-e2fded02e919 | -11.65143 | -64.99338 | 2024-10-01 05:53:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 3217e691-7fce-38ea-a75a-ec1cc544792b | -11.65073 | -64.99839 | 2024-10-01 05:53:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 3.1 |
| ba1c78d9-a879-3c67-b28d-9c3bc04dabc0 | -11.64753 | -64.99281 | 2024-10-01 05:53:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 6dfa0166-d567-3e0b-901b-8f6061840ebe | -11.63581 | -64.99115 | 2024-10-01 05:53:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 8818c8dd-2970-38e4-9cbd-7b7b165c32d9 | -11.63191 | -64.9906 | 2024-10-01 05:53:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 8db94239-42e6-3d87-8cc4-bc0d97cbc262 | -11.62731 | -64.99506 | 2024-10-01 05:53:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 2.3 |
| e0ddd749-eff4-3789-b6ba-db192647fa93 | -11.62272 | -64.99945 | 2024-10-01 05:53:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 731a7a33-adcb-3873-a853-c59ff0269971 | -11.61744 | -65.00886 | 2024-10-01 05:53:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 9a658f44-6f60-3d2c-86b3-4f32f7203cb9 | -11.61354 | -65.00831 | 2024-10-01 05:53:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 6bf60b7d-7430-3bfe-ac91-3793c43f39e1 | -8.95182 | -69.11712 | 2024-10-01 05:53:00 | NOAA-20 | MANOEL URBANO | ACRE | Brasil | 1200344 | 12 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 2204b751-7b9a-303b-9e02-d9f75daf8ca0 | -10.73315 | -69.47388 | 2024-10-01 05:53:00 | NOAA-20 | ASSIS BRASIL | ACRE | Brasil | 1200054 | 12 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 79732e04-6c9f-3167-a72f-2cf5b16b6698 | -10.72984 | -69.47334 | 2024-10-01 05:53:00 | NOAA-20 | ASSIS BRASIL | ACRE | Brasil | 1200054 | 12 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 7e6c56cc-d89e-3f03-86fb-2399ff0e91d3 | -10.71379 | -69.42415 | 2024-10-01 05:53:00 | NOAA-20 | ASSIS BRASIL | ACRE | Brasil | 1200054 | 12 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b15f084a-99b5-3828-9f94-0dbc4ffd4819 | -10.71213 | -69.41313 | 2024-10-01 05:53:00 | NOAA-20 | BRASILÉIA | ACRE | Brasil | 1200104 | 12 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 4dd50965-89cf-3136-9c7b-bce63645531d | -10.71049 | -69.42361 | 2024-10-01 05:53:00 | NOAA-20 | ASSIS BRASIL | ACRE | Brasil | 1200054 | 12 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 81ed20e6-8892-3d0b-8379-6cf04b560d3f | -10.70938 | -69.4091 | 2024-10-01 05:53:00 | NOAA-20 | BRASILÉIA | ACRE | Brasil | 1200104 | 12 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 1860b767-86a3-3f8d-82f6-6bdaf2e04abc | -10.70883 | -69.4126 | 2024-10-01 05:53:00 | NOAA-20 | BRASILÉIA | ACRE | Brasil | 1200104 | 12 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 3c899c87-0934-32ab-8d81-f25ced5e17ae | -10.70828 | -69.41609 | 2024-10-01 05:53:00 | NOAA-20 | BRASILÉIA | ACRE | Brasil | 1200104 | 12 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 1168bb81-282f-31e8-88fe-9e6d31254602 | -10.70773 | -69.41959 | 2024-10-01 05:53:00 | NOAA-20 | BRASILÉIA | ACRE | Brasil | 1200104 | 12 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 2ae334f2-3021-3f07-87fd-16cc88eb2185 | -10.70718 | -69.42308 | 2024-10-01 05:53:00 | NOAA-20 | ASSIS BRASIL | ACRE | Brasil | 1200054 | 12 | 33 | nan | nan | nan | Amazônia | 2.6 |
| a94218f1-f50a-3f7e-afc4-eedab495efb9 | -10.70499 | -69.48009 | 2024-10-01 05:53:00 | NOAA-20 | ASSIS BRASIL | ACRE | Brasil | 1200054 | 12 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 95c4dfed-9d7b-3656-aa20-7f5d0fabf721 | -10.70497 | -69.41556 | 2024-10-01 05:53:00 | NOAA-20 | BRASILÉIA | ACRE | Brasil | 1200104 | 12 | 33 | nan | nan | nan | Amazônia | 1.8 |
| a49beb48-7e37-323f-9d1c-d24df8f4b8ce | -10.70442 | -69.41906 | 2024-10-01 05:53:00 | NOAA-20 | BRASILÉIA | ACRE | Brasil | 1200104 | 12 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 03e36c95-f93d-385d-8aea-d755fceb5c98 | -10.6829 | -69.38334 | 2024-10-01 05:53:00 | NOAA-20 | BRASILÉIA | ACRE | Brasil | 1200104 | 12 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 512800a3-f0f1-3485-8e35-eeda72a47f18 | -10.54531 | -69.3078 | 2024-10-01 05:53:00 | NOAA-20 | BRASILÉIA | ACRE | Brasil | 1200104 | 12 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ca94def9-f245-39c8-8e7a-0865cca30df8 | -10.542 | -69.30727 | 2024-10-01 05:53:00 | NOAA-20 | BRASILÉIA | ACRE | Brasil | 1200104 | 12 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 010c75b7-f815-3cc4-9ddd-db256a76bc0c | -10.53924 | -69.30325 | 2024-10-01 05:53:00 | NOAA-20 | BRASILÉIA | ACRE | Brasil | 1200104 | 12 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 35345f51-09a0-3f0d-9707-a71d985072c8 | -10.53869 | -69.30674 | 2024-10-01 05:53:00 | NOAA-20 | BRASILÉIA | ACRE | Brasil | 1200104 | 12 | 33 | nan | nan | nan | Amazônia | 1.6 |
| a119879c-166b-396a-a6cc-0a670d972c88 | -10.53593 | -69.30272 | 2024-10-01 05:53:00 | NOAA-20 | BRASILÉIA | ACRE | Brasil | 1200104 | 12 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 9d583c80-1edd-3c1d-8a32-dacc3de55dd4 | -10.43088 | -69.23547 | 2024-10-01 05:53:00 | NOAA-20 | BRASILÉIA | ACRE | Brasil | 1200104 | 12 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 6d3fb430-8418-307a-ab67-6f14b7473c39 | -10.42757 | -69.23495 | 2024-10-01 05:53:00 | NOAA-20 | BRASILÉIA | ACRE | Brasil | 1200104 | 12 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 4b629857-8ac2-3e7c-8732-508cabdced5e | -10.07866 | -69.16524 | 2024-10-01 05:53:00 | NOAA-20 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 31b91c58-072c-349b-aa4e-2c5772f73807 | -8.9763 | -71.56747 | 2024-10-01 05:53:00 | NOAA-20 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 924bb303-3c7e-398c-8668-9cb6d560f63a | -9.74585 | -66.59299 | 2024-10-01 05:53:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| d08ae7cf-b69a-3396-93e5-240906f6a1ed | -9.70282 | -66.85281 | 2024-10-01 05:53:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| e86a0978-ba50-30a4-9c23-e01ebc1d331d | -9.69936 | -66.85227 | 2024-10-01 05:53:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 3.1 |
| deecd888-b631-3da4-a734-7781a3d21969 | -9.69877 | -66.85612 | 2024-10-01 05:53:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 5d3173e5-82cf-3fd5-bf01-bbc72c218c62 | -9.61317 | -67.16504 | 2024-10-01 05:53:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d03377b6-6ad7-35c6-9071-29e3213e2e77 | -9.6126 | -67.16879 | 2024-10-01 05:53:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 286e4d16-952c-3645-9ef2-a6a68134ccf8 | -9.60975 | -67.16451 | 2024-10-01 05:53:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 478d47b9-5806-3281-9ed6-eec37497d166 | -9.59106 | -66.18253 | 2024-10-01 05:53:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.4 |
| eb486640-0d44-3ae5-98b8-c9c7f18d1efb | -9.57554 | -66.64824 | 2024-10-01 05:53:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| dc63f69b-27c1-31e0-ac76-8c1d51a27607 | -9.36496 | -68.32094 | 2024-10-01 05:53:00 | NOAA-20 | BUJARI | ACRE | Brasil | 1200138 | 12 | 33 | nan | nan | nan | Amazônia | 1.0 |
| aa82a3c1-a0f3-36e6-a1b4-b1f1ab8c5530 | -9.36332 | -68.33149 | 2024-10-01 05:53:00 | NOAA-20 | BUJARI | ACRE | Brasil | 1200138 | 12 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 39e51682-3596-32dd-a83c-6739703ff3a7 | -9.30115 | -68.7516 | 2024-10-01 05:53:00 | NOAA-20 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 2.0 |
| e536f27f-fe2e-39a0-961a-0b793a7f6b6a | -9.27374 | -67.6063 | 2024-10-01 05:53:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| f0dddbdb-c7f9-3591-b88a-ebe9d5093144 | -9.27319 | -67.60992 | 2024-10-01 05:53:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| cb35ca83-1c04-3999-8244-500a725e9d76 | -9.27208 | -67.60696 | 2024-10-01 05:53:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |


[Clique aqui para ver as próximas entradas](README155.md)
