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

## Dados Diários - Página 115

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 0ff9cad5-1a43-3db0-82b3-b6b2cbf6fa59 | -3.05546 | -54.41909 | 2026-09-22 05:42:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 1a62c265-7472-31c7-8077-ab63f7ac2c65 | -6.3105 | -60.0093 | 2026-09-22 05:42:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 38f4dcb3-87d4-3c92-807a-4a0ac8d44f81 | -6.38374 | -55.27621 | 2026-09-22 05:42:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 18ac195a-356d-3de0-96f9-7075cab83bfb | -7.7278 | -61.23835 | 2026-09-22 05:42:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 0.3 |
| 0893b8a1-53d6-32bd-90e0-d0219fc876c4 | -2.9571 | -57.72364 | 2026-09-22 05:42:00 | NOAA-20 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 3.5 |
| c02ba85f-4446-324b-9113-5a4bff0011c1 | -6.09733 | -57.67709 | 2026-09-22 05:42:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 10.7 |
| bc5919d1-675b-34bd-aeb6-ea9c9d7cd6a9 | -3.47795 | -59.60125 | 2026-09-22 05:42:00 | NOAA-20 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 927260cd-bf49-324d-94e2-6ac2002b80ed | -3.45791 | -58.39858 | 2026-09-22 05:42:00 | NOAA-20 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| a358a49e-0d01-361e-ab2d-76a91c92d9e6 | -6.308 | -59.94546 | 2026-09-22 05:42:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 9c03c2a8-173e-340f-ab22-c8ce2096f0c0 | -7.71098 | -61.25255 | 2026-09-22 05:42:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a08b1092-6bbc-3cf0-81d1-38b071d3a960 | -7.70267 | -61.54279 | 2026-09-22 05:42:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 12b8a399-10cb-33a4-ab77-c027a57b0c9a | -2.87206 | -57.7941 | 2026-09-22 05:42:00 | NOAA-20 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 7c64cba3-7a91-319b-a6eb-b422b0044005 | -7.72547 | -61.22963 | 2026-09-22 05:42:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e0398f6c-bd7c-343b-a64e-57e1ebe4f872 | -9.55086 | -66.03213 | 2026-09-22 05:44:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 4aaff48d-1f64-30da-b4cd-c4c4ffa09c94 | -8.52592 | -67.00417 | 2026-09-22 05:44:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| c70c9459-ed36-38f2-85eb-99bd3ae9327b | -9.08229 | -72.19083 | 2026-09-22 05:44:00 | NOAA-20 | MARECHAL THAUMATURGO | ACRE | Brasil | 1200351 | 12 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 00bd4211-54c5-3239-ae8d-735b020d0564 | -9.5573 | -65.99231 | 2026-09-22 05:44:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.5 |
| be89d7a2-eaa0-3df2-908e-9c51568fbfc8 | -12.79543 | -54.03843 | 2026-09-22 05:44:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| fa7e17a8-4934-3869-985b-f189f84a114e | -9.12865 | -58.8902 | 2026-09-22 05:44:00 | NOAA-20 | COTRIGUAÇU | MATO GROSSO | Brasil | 5103379 | 51 | 33 | nan | nan | nan | Amazônia | 3.4 |
| c6793e37-b5ac-38f7-9481-a717598d639f | -9.76762 | -65.06279 | 2026-09-22 05:44:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.9 |
| de81ad3b-9c83-3348-b331-36786f712e43 | -11.96896 | -64.04254 | 2026-09-22 05:44:00 | NOAA-20 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 6da4372e-753c-360f-ac9c-1d18e59f8d4e | -11.99389 | -58.07298 | 2026-09-22 05:44:00 | NOAA-20 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 08a3eddd-a793-3bd6-a979-001375c92620 | -9.09916 | -65.3756 | 2026-09-22 05:44:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 61fb4587-480e-3398-95da-4d83cd35c140 | -13.51514 | -51.51545 | 2026-09-22 05:44:00 | NOAA-20 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 38.6 |
| 2d4efcb4-9f6a-3509-8f0a-0bea76ae0acd | -9.10249 | -65.37613 | 2026-09-22 05:44:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 857d1162-8479-38f2-8d17-03917b0fb007 | -10.90409 | -53.96538 | 2026-09-22 05:44:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| b08a219f-5187-3ff6-83ae-e12e1ab2fc5f | -9.75768 | -65.06118 | 2026-09-22 05:44:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 50b585f2-e0c5-3d1b-bbd9-2971830cdd65 | -9.75823 | -65.05768 | 2026-09-22 05:44:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d6d270e8-861e-3897-bb24-eb07adb701a4 | -9.19049 | -65.85855 | 2026-09-22 05:44:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 4832aa05-7342-3820-9eb2-d0c1bd6b0260 | -8.67456 | -70.03341 | 2026-09-22 05:44:00 | NOAA-20 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d123a448-1929-36bb-b2e2-12949cb2fe32 | -8.68003 | -70.02647 | 2026-09-22 05:44:00 | NOAA-20 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 47234c39-a46e-38e5-a09e-2c314219c922 | -9.55188 | -66.04716 | 2026-09-22 05:44:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ae4636e8-31dd-35a4-a1de-8cc30c2321df | -9.66662 | -54.33855 | 2026-09-22 05:44:00 | NOAA-20 | GUARANTÃ DO NORTE | MATO GROSSO | Brasil | 5104104 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d077b2f7-02da-3632-8281-115863e779b8 | -11.01234 | -54.14808 | 2026-09-22 05:44:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 3a850574-ed9c-36e6-b3fc-4a7fe3c22957 | -12.7949 | -54.0431 | 2026-09-22 05:44:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 31343bcb-3f85-303a-8391-7211a22e8634 | -9.56257 | -66.04523 | 2026-09-22 05:44:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| c03a803f-e822-340c-ba2d-18baa0a0fff7 | -9.55833 | -66.00734 | 2026-09-22 05:44:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 372ca970-65a6-3d5b-a274-fe29592e1bd0 | -9.56653 | -66.04216 | 2026-09-22 05:44:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 2ea52ddd-f74e-3605-819d-d41dcf69e1a3 | -9.18772 | -65.85439 | 2026-09-22 05:44:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 20cca7c0-f725-36b2-b5dc-6b27dd1a1149 | -9.18436 | -65.85384 | 2026-09-22 05:44:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| ffdfa198-4d7f-31f0-9b93-10269a8697b4 | -9.18323 | -65.85021 | 2026-09-22 05:44:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| a890d125-0df7-3bc2-af71-4b8a01572621 | -11.16706 | -51.10346 | 2026-09-22 05:44:00 | NOAA-20 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 92aac2a6-cd35-32b0-84bc-34353e861ba4 | -12.7948 | -54.04114 | 2026-09-22 05:44:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| ef78d38a-edbd-33e3-a38d-5e7187d43694 | -9.56111 | -66.01151 | 2026-09-22 05:44:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 525c8d77-c4ff-3dc2-a31f-37fe702d3a91 | -10.25065 | -68.77308 | 2026-09-22 05:44:00 | NOAA-20 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 2.7 |
| ae70ef3b-daf1-37cf-b6ed-b9d6b9a5d79f | -10.1032 | -69.08955 | 2026-09-22 05:44:00 | NOAA-20 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f2315863-b104-3dd3-9cb4-204dc11d8a3c | -10.90143 | -53.96721 | 2026-09-22 05:44:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| b74250ae-668e-3255-b8bf-63bafe90dbf6 | -12.85043 | -54.04512 | 2026-09-22 05:44:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c3e61ef4-c318-3478-bee3-376d17521004 | -9.02549 | -60.36138 | 2026-09-22 05:44:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| a503b8b8-839f-3e05-92c3-13bfa8ecebe4 | -9.56272 | -66.02291 | 2026-09-22 05:44:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| fbdaf6c2-0eec-34e4-93a0-01727f5e2d51 | -9.56492 | -66.03072 | 2026-09-22 05:44:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| d12b9743-3384-3668-ab5e-761a49373d7d | -8.74401 | -69.45592 | 2026-09-22 05:44:00 | NOAA-20 | MANOEL URBANO | ACRE | Brasil | 1200344 | 12 | 33 | nan | nan | nan | Amazônia | 1.7 |
| c82c6491-6fa5-32be-bbf3-ff1a521a66a8 | -8.67522 | -70.02956 | 2026-09-22 05:44:00 | NOAA-20 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 2f0fc764-237c-39b3-a347-8c6081fe48f5 | -10.44861 | -51.2731 | 2026-09-22 05:44:00 | NOAA-20 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 8aa479cc-6fca-34a3-8486-0b165008c7f2 | -9.66087 | -54.33767 | 2026-09-22 05:44:00 | NOAA-20 | GUARANTÃ DO NORTE | MATO GROSSO | Brasil | 5104104 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 71508a39-a180-353c-93f9-131d66c4fec0 | -10.09653 | -69.12833 | 2026-09-22 05:44:00 | NOAA-20 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 1439a976-cd75-37d8-b7da-4b9c7a4437a7 | -9.80969 | -67.56963 | 2026-09-22 05:44:00 | NOAA-20 | PORTO ACRE | ACRE | Brasil | 1200807 | 12 | 33 | nan | nan | nan | Amazônia | 0.6 |
| ad67f010-0d63-3147-b738-934e121fc6d7 | -9.28095 | -60.62049 | 2026-09-22 05:44:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 95fb7b1f-aa7f-337f-9d52-42d3e9363348 | -9.56155 | -66.03017 | 2026-09-22 05:44:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 79a3362e-f3b3-3f8a-ad12-db4fa08f05ea | -9.6781 | -54.34033 | 2026-09-22 05:44:00 | NOAA-20 | GUARANTÃ DO NORTE | MATO GROSSO | Brasil | 5104104 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 444b6995-0fc8-3417-ae36-a34e414d902d | -9.76099 | -65.06172 | 2026-09-22 05:44:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 9ec0c253-90f3-3d86-967f-43546ac177a1 | -8.79035 | -69.02071 | 2026-09-22 05:44:00 | NOAA-20 | MANOEL URBANO | ACRE | Brasil | 1200344 | 12 | 33 | nan | nan | nan | Amazônia | 1.7 |
| cbb4f4f2-e87d-3a6b-85b6-bf6e23091b0b | -9.07952 | -60.43931 | 2026-09-22 05:44:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 75531e68-6bf5-3ad7-b920-3a9792c43252 | -11.31215 | -54.04798 | 2026-09-22 05:44:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 5ddd22ff-65e6-3acd-803a-e2b4054b3fb5 | -9.55701 | -66.03687 | 2026-09-22 05:44:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.8 |
| bdbb684f-a5f3-344e-be3d-1eb3d66a4387 | -10.16164 | -69.00108 | 2026-09-22 05:44:00 | NOAA-20 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 1.5 |
| c35e5b37-44c1-341a-a64b-7233149b088f | -9.2854 | -60.61644 | 2026-09-22 05:44:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 5b8eb0d5-e7f6-3464-bf23-66b37eb53650 | -8.53581 | -67.0099 | 2026-09-22 05:44:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 4f9130b4-33cc-37a1-bbf7-45f9e15fcdb1 | -11.31601 | -54.04634 | 2026-09-22 05:44:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 182f35af-35a1-3ec3-8309-4a4b25537764 | -9.67763 | -54.34409 | 2026-09-22 05:44:00 | NOAA-20 | GUARANTÃ DO NORTE | MATO GROSSO | Brasil | 5104104 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 30b105b2-c923-3e89-b56c-294fd75d7607 | -11.04745 | -54.15653 | 2026-09-22 05:44:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 93ffe130-7063-3b08-a44d-da5869513b25 | -11.14841 | -51.10721 | 2026-09-22 05:44:00 | NOAA-20 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 1a8939c0-4d3c-3f57-b77a-53023f40fd62 | -10.26176 | -68.79865 | 2026-09-22 05:44:00 | NOAA-20 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 702f44e1-79ac-3163-98e6-34cfab123719 | -10.62063 | -69.35699 | 2026-09-22 05:44:00 | NOAA-20 | BRASILÉIA | ACRE | Brasil | 1200104 | 12 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b84e40ba-391d-3eb3-adea-3e6c007f41dc | -10.24708 | -68.74881 | 2026-09-22 05:44:00 | NOAA-20 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 39d5fa7f-2a39-3e1a-8299-69482178d188 | -10.86504 | -57.17015 | 2026-09-22 05:44:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 2f485463-d27d-3c9a-a039-081ae5303a77 | -10.6011 | -53.99137 | 2026-09-22 05:44:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 3.4 |
| fbca28c0-041a-33b8-8300-19a206bbea8c | -9.56375 | -66.03798 | 2026-09-22 05:44:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| aa9efb36-b44f-348d-834e-d60bc4dbbff2 | -11.03664 | -54.14654 | 2026-09-22 05:44:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| d377bc72-3652-3b4d-916e-0d40c57aba07 | -9.76203 | -65.09778 | 2026-09-22 05:44:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 2af95f87-df59-3163-a963-f3d01b8994cf | -9.18377 | -65.85743 | 2026-09-22 05:44:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| df8c4a30-3836-3401-893e-ecb4e1af3eb2 | -9.07572 | -60.43875 | 2026-09-22 05:44:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 4.5 |
| dfe36cc1-fe7f-3a5c-ac2a-1320ae44021a | -13.29827 | -51.79463 | 2026-09-22 05:44:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 0900a145-7bba-371a-9b78-9c7926ad2ce5 | -11.31813 | -54.0488 | 2026-09-22 05:44:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 5b10d931-8395-3d73-9efa-2b0e2fa175f7 | -11.31761 | -54.05322 | 2026-09-22 05:44:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 9264ec06-2f13-31ea-9015-1939d346d6a7 | -8.91623 | -72.81215 | 2026-09-22 05:44:00 | NOAA-20 | MARECHAL THAUMATURGO | ACRE | Brasil | 1200351 | 12 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 43604d8d-38f6-3c2c-a83b-f40ca221e614 | -7.92949 | -71.34563 | 2026-09-22 05:44:00 | NOAA-20 | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 1.7 |
| e9e9097b-0d16-3d55-9959-786027b873a4 | -9.56096 | -66.0338 | 2026-09-22 05:44:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 01a5b330-2eb6-31cb-87eb-f2d62792d3fc | -13.50652 | -51.52901 | 2026-09-22 05:44:00 | NOAA-20 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 14.3 |
| ee012545-91e6-359b-b5ae-f098cfa22dcc | -10.44784 | -51.27962 | 2026-09-22 05:44:00 | NOAA-20 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| b14a0546-9dc9-370d-935a-c358817f7ad1 | -8.52527 | -67.00813 | 2026-09-22 05:44:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| ef2c51e0-4658-396f-a452-fcc6d200d36e | -9.95266 | -53.98716 | 2026-09-22 05:44:00 | NOAA-20 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 3c6926a5-ea73-34d0-8a31-83163627afa3 | -7.90303 | -72.94618 | 2026-09-22 05:44:00 | NOAA-20 | RODRIGUES ALVES | ACRE | Brasil | 1200427 | 12 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a1da4052-dbe2-3870-92c3-c3afa04d2d89 | -9.81181 | -65.06279 | 2026-09-22 05:44:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 66141fb8-ca7d-30f8-95ce-1a01de977d72 | -10.18477 | -59.44915 | 2026-09-22 05:44:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 460d9339-e2f9-3fec-b8b9-35933800d963 | -9.10859 | -65.38074 | 2026-09-22 05:44:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| ad53bbe4-ecbe-3ea8-994c-5b9e2248840f | -10.59621 | -53.98187 | 2026-09-22 05:44:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 8.7 |
| 2fd563d9-9a3e-3335-b13a-e7c674d0872f | -12.79424 | -54.0458 | 2026-09-22 05:44:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 5cbf6805-d516-3790-8905-dd5721a8800a | -10.27631 | -68.87291 | 2026-09-22 05:44:00 | NOAA-20 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 47748396-fd0b-3bf0-a636-e833f7cc5e76 | -9.10029 | -65.36853 | 2026-09-22 05:44:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |


[Clique aqui para ver as próximas entradas](README116.md)
