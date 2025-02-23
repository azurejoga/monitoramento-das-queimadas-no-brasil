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

## Dados Diários - Página 4

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 66f5c28e-3075-392a-a834-6b277691a5aa | -20.58196 | -46.37756 | 2025-02-23 04:50:00 | NOAA-21 | SÃO JOÃO BATISTA DO GLÓRIA | MINAS GERAIS | Brasil | 3162203 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| faab1d52-f996-3eee-a768-2c50cfa88f06 | -20.31715 | -46.48886 | 2025-02-23 04:50:00 | NOAA-21 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 3.3 |
| a8330899-b2ae-3c4b-b862-b6de055fb788 | -22.67767 | -42.85268 | 2025-02-23 04:50:00 | NOAA-21 | ITABORAÍ | RIO DE JANEIRO | Brasil | 3301900 | 33 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| 5cc7a8bb-8101-3e34-9663-48578352a914 | -20.30385 | -46.47878 | 2025-02-23 04:50:00 | NOAA-21 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 8a2422cf-5b43-38f7-83b6-4203a20519d7 | -21.88686 | -53.72132 | 2025-02-23 04:50:00 | NOAA-21 | NOVA ANDRADINA | MATO GROSSO DO SUL | Brasil | 5006200 | 50 | 33 | nan | nan | nan | Cerrado | 0.6 |
| e6437cd9-664e-3f58-9e12-2e970003ff85 | -20.5863 | -46.38214 | 2025-02-23 04:50:00 | NOAA-21 | SÃO JOÃO BATISTA DO GLÓRIA | MINAS GERAIS | Brasil | 3162203 | 31 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 61ab2e0d-7350-30e0-b5a2-538901ef7273 | -23.59303 | -47.43948 | 2025-02-23 04:50:00 | NOAA-21 | VOTORANTIM | SÃO PAULO | Brasil | 3557006 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| e9bd6714-40ab-3c13-880e-6fca7bd2990a | -20.58683 | -46.37743 | 2025-02-23 04:50:00 | NOAA-21 | SÃO JOÃO BATISTA DO GLÓRIA | MINAS GERAIS | Brasil | 3162203 | 31 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 04f692cb-96ee-3ed5-9861-8f705ed489da | -20.30328 | -46.48404 | 2025-02-23 04:50:00 | NOAA-21 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 742bb48c-10d0-3a5a-b058-16c490f23a18 | -19.50234 | -55.44758 | 2025-02-23 04:50:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 0.6 |
| b63d1b06-b75c-38d5-9dbe-5ac3b9fbc8f5 | -24.32927 | -50.65388 | 2025-02-23 04:50:00 | NOAA-21 | TELÊMACO BORBA | PARANÁ | Brasil | 4127106 | 41 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| ef0f8320-a785-3cff-b872-16281e8db496 | -29.8108 | -51.34324 | 2025-02-23 04:53:00 | NOAA-21 | NOVA SANTA RITA | RIO GRANDE DO SUL | Brasil | 4313375 | 43 | 33 | nan | nan | nan | Pampa | 0.9 |
| 6a281767-a9f7-3000-93ad-d5f830b4a0e8 | -29.80899 | -51.34454 | 2025-02-23 04:53:00 | NOAA-21 | NOVA SANTA RITA | RIO GRANDE DO SUL | Brasil | 4313375 | 43 | 33 | nan | nan | nan | Pampa | 0.8 |
| 57f6b32f-4733-30c4-a8c6-e3935fb4840b | -19.81753 | -40.09892 | 2025-02-23 05:08:00 | AQUA_M-M | ARACRUZ | ESPÍRITO SANTO | Brasil | 3200607 | 32 | 33 | nan | nan | nan | Mata Atlântica | 7.8 |
| 506c18cb-30db-3d8c-882e-a55d0f297e87 | -19.81895 | -40.08889 | 2025-02-23 05:08:00 | AQUA_M-M | ARACRUZ | ESPÍRITO SANTO | Brasil | 3200607 | 32 | 33 | nan | nan | nan | Mata Atlântica | 6.0 |
| e180817c-e4a2-3a0a-adee-d7578994dc67 | 4.3311 | -60.8462 | 2025-02-23 05:08:00 | NPP-375D | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 2.3 |
| b45b18d7-1051-3493-8cba-5e0c920961f8 | 4.3317 | -60.85016 | 2025-02-23 05:08:00 | NPP-375D | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 9389d33d-ad1a-34ca-9fa8-7c6e99c839d1 | 4.10286 | -59.94395 | 2025-02-23 05:08:00 | NPP-375D | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 2.0 |
| e3e0aa74-f733-38e6-8b8f-42fc3ed83180 | -3.01866 | -54.59047 | 2025-02-23 05:10:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 15743c20-1c5d-3d4c-9503-f1262f417a0e | -3.01062 | -54.57377 | 2025-02-23 05:10:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 57d687a8-1720-3d6c-bb2e-d562b8c81785 | -3.71276 | -53.73609 | 2025-02-23 05:10:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| a1874f9a-b6ef-33df-bfad-827c06944cd9 | -3.01004 | -54.57754 | 2025-02-23 05:10:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 1dd4e840-3c9b-3c0a-a284-6ad372448288 | -3.02213 | -54.59099 | 2025-02-23 05:10:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 10a39c99-cbb7-3859-b8db-54169c6704df | -1.59872 | -54.59069 | 2025-02-23 05:10:00 | NPP-375D | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| cb6b20af-c5f2-3800-bf4e-93d4415dffd5 | -1.59929 | -54.58702 | 2025-02-23 05:10:00 | NPP-375D | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| c4c1e426-192e-3378-bbd0-40b0c19866ff | -3.00716 | -54.57323 | 2025-02-23 05:10:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 62884840-bf4a-3266-a113-aeb1eb1f205c | -12.10329 | -51.22917 | 2025-02-23 05:12:00 | NPP-375D | SERRA NOVA DOURADA | MATO GROSSO | Brasil | 5107883 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 59aefe7f-6b67-36f2-b293-39b62883bc11 | -12.09841 | -51.23255 | 2025-02-23 05:12:00 | NPP-375D | SERRA NOVA DOURADA | MATO GROSSO | Brasil | 5107883 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| e5db1cd4-6e24-30fb-afcc-0e332085bd26 | -12.10396 | -51.22392 | 2025-02-23 05:12:00 | NPP-375D | SERRA NOVA DOURADA | MATO GROSSO | Brasil | 5107883 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| a050582f-253d-32b8-a221-85b863cf2c31 | -12.0985 | -51.2286 | 2025-02-23 05:12:00 | NPP-375D | SERRA NOVA DOURADA | MATO GROSSO | Brasil | 5107883 | 51 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 08a4ca32-3719-35da-9883-b492f4b83b1f | -12.09912 | -51.22736 | 2025-02-23 05:12:00 | NPP-375D | SERRA NOVA DOURADA | MATO GROSSO | Brasil | 5107883 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| ea1efcc0-e6f6-3749-aa1f-89eebe94424d | -20.89885 | -46.15942 | 2025-02-23 05:14:00 | NPP-375D | CARMO DO RIO CLARO | MINAS GERAIS | Brasil | 3114402 | 31 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 19526d45-f89d-3b25-9891-9e04393358c1 | -20.89684 | -46.16207 | 2025-02-23 05:14:00 | NPP-375D | CARMO DO RIO CLARO | MINAS GERAIS | Brasil | 3114402 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| bab1ff20-7b95-30bc-bbce-033d622965ab | -16.6471 | -49.36601 | 2025-02-23 05:14:00 | NPP-375D | GOIÂNIA | GOIÁS | Brasil | 5208707 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| d0284e17-5297-3594-939c-01586b30611c | -15.28911 | -53.20348 | 2025-02-23 05:14:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 3f766fc5-6875-3c4f-8393-7765511601bc | -16.03122 | -60.08172 | 2025-02-23 05:14:00 | NPP-375D | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 0938c41f-ec1e-3cb1-962a-bb04121cd49d | -20.58482 | -46.37921 | 2025-02-23 05:14:00 | NPP-375D | SÃO JOÃO BATISTA DO GLÓRIA | MINAS GERAIS | Brasil | 3162203 | 31 | 33 | nan | nan | nan | Cerrado | 2.2 |
| fcdcfc54-b83d-3135-a64e-ab0dfe4ff6ca | -20.58442 | -46.38448 | 2025-02-23 05:14:00 | NPP-375D | SÃO JOÃO BATISTA DO GLÓRIA | MINAS GERAIS | Brasil | 3162203 | 31 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 3cc8646b-fdc2-3ac1-a148-a45e6e96726d | -16.64805 | -49.36783 | 2025-02-23 05:14:00 | NPP-375D | GOIÂNIA | GOIÁS | Brasil | 5208707 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| a98ab2be-e0cb-3b5f-9b93-d02fe85f8da1 | -20.58692 | -46.38241 | 2025-02-23 05:14:00 | NPP-375D | SÃO JOÃO BATISTA DO GLÓRIA | MINAS GERAIS | Brasil | 3162203 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 709a8a56-6ee2-3785-a869-e57b7bbcbbf3 | -15.28857 | -53.20771 | 2025-02-23 05:14:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 2e839079-afcb-32f3-a26e-74de4356f963 | -15.04246 | -45.62263 | 2025-02-23 05:14:00 | NPP-375D | CHAPADA GAÚCHA | MINAS GERAIS | Brasil | 3116159 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 42621a7b-56ae-3a2f-a627-f84980a37af8 | -15.53001 | -60.10571 | 2025-02-23 05:14:00 | NPP-375D | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b54d51e3-66fc-38f7-8708-5c68affcaa33 | -15.04639 | -45.61817 | 2025-02-23 05:14:00 | NPP-375D | CHAPADA GAÚCHA | MINAS GERAIS | Brasil | 3116159 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 1c52e227-10b4-39c4-a724-72c4431d461a | -20.89845 | -46.16534 | 2025-02-23 05:14:00 | NPP-375D | CARMO DO RIO CLARO | MINAS GERAIS | Brasil | 3114402 | 31 | 33 | nan | nan | nan | Cerrado | 4.0 |
| ada7eade-40ce-3f91-8afb-f0af1040ec94 | -20.5873 | -46.37706 | 2025-02-23 05:14:00 | NPP-375D | SÃO JOÃO BATISTA DO GLÓRIA | MINAS GERAIS | Brasil | 3162203 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 137552e4-2cfc-3275-9cc0-de3c280e4724 | -15.04312 | -45.61554 | 2025-02-23 05:14:00 | NPP-375D | CHAPADA GAÚCHA | MINAS GERAIS | Brasil | 3116159 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 100b98d7-82ad-355c-9aaa-cd00a825e7de | -20.89646 | -46.16718 | 2025-02-23 05:14:00 | NPP-375D | CARMO DO RIO CLARO | MINAS GERAIS | Brasil | 3114402 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 10df8298-9141-3f48-8b1f-becfec5609b5 | -15.03935 | -45.61703 | 2025-02-23 05:14:00 | NPP-375D | CHAPADA GAÚCHA | MINAS GERAIS | Brasil | 3116159 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 65f25da3-404a-3d58-a4aa-08a9db092678 | -22.1613 | -54.09929 | 2025-02-23 05:16:00 | NPP-375D | DEODÁPOLIS | MATO GROSSO DO SUL | Brasil | 5003454 | 50 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 4a5aef46-b983-350b-9a78-7a9613732348 | 4.3269 | -60.84663 | 2025-02-23 05:31:00 | NOAA-20 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 7fa1b673-0b76-35d0-9078-2e1dfb3f637b | 4.33352 | -60.84563 | 2025-02-23 05:31:00 | NOAA-20 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 01d3d9e8-a03c-31f0-a8d9-ebf8f046b211 | -3.00928 | -54.57778 | 2025-02-23 05:31:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| be3caf8c-8dc7-3cc5-a7d8-338818ee67da | -3.00973 | -54.57482 | 2025-02-23 05:31:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| c30d28ed-7e56-3081-9e97-ffefe41053a8 | 4.33076 | -60.84958 | 2025-02-23 05:31:00 | NOAA-20 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 2.0 |
| a88bd553-0bbb-327f-996d-efc6d2ab0ac7 | -10.05458 | -62.17976 | 2025-02-23 05:35:00 | NOAA-20 | THEOBROMA | RONDÔNIA | Brasil | 1101609 | 11 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 95e2c7fa-3f66-3f6a-a4b8-9e6eb1621335 | -12.09751 | -51.23296 | 2025-02-23 05:35:00 | NOAA-20 | SERRA NOVA DOURADA | MATO GROSSO | Brasil | 5107883 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| d40e240f-bd62-34fa-9fe5-5f2093c5a936 | -16.0286 | -60.08192 | 2025-02-23 05:35:00 | NOAA-20 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| afef5047-8247-3a09-bfda-f3717221d705 | -15.53103 | -60.10641 | 2025-02-23 05:35:00 | NOAA-20 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 8bb2d589-e113-37d9-8b60-8bf41f910adb | -12.09829 | -51.22598 | 2025-02-23 05:35:00 | NOAA-20 | SERRA NOVA DOURADA | MATO GROSSO | Brasil | 5107883 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 7af63e50-99c7-3c5a-a28d-07ef4443812b | -18.42133 | -55.59071 | 2025-02-23 05:37:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.6 |
| 50aee271-5054-38da-bb6f-08835cd319ee | -18.41547 | -55.59006 | 2025-02-23 05:37:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 8.4 |
| 0212fded-4822-357e-98f3-2f3fd25dd0de | -18.4159 | -55.58572 | 2025-02-23 05:37:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 5.1 |
| a0a19f06-a57b-3e71-9482-7df31a0a3980 | -18.42176 | -55.58636 | 2025-02-23 05:37:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.7 |


