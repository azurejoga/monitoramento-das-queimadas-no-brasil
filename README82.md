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

## Dados Diários - Página 82

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 1e3482e0-9e28-3273-b1cf-554d9bc33f77 | -8.3904 | -62.6774 | 2026-08-22 07:20:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 128.0 |
| 96a36d4d-4865-3c89-a7ba-b3030bae0b0a | -6.7833 | -59.4208 | 2026-08-22 07:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 82.3 |
| 19cb65f1-9815-3c70-8fc6-c0fb1a47dfd0 | -6.8019 | -59.4008 | 2026-08-22 07:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 56.9 |
| 3caa7e55-9e2c-30f8-bcc3-0f60ae715132 | -14.3744 | -51.8038 | 2026-08-22 07:20:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 57.3 |
| fe855a44-c4d5-34fa-8210-dc2a05ca8c81 | -6.7507 | -58.6687 | 2026-08-22 07:20:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 48.6 |
| 41f2b0f3-1e80-379b-813c-cd9f1c377afe | -6.7833 | -59.4208 | 2026-08-22 07:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 88.5 |
| 3814f2ee-3bb2-3260-8978-f0a84fd6233b | -6.8018 | -59.4201 | 2026-08-22 07:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 113.9 |
| 8fef1708-ebfa-3ed9-aeda-8c561bffd62e | -8.3903 | -62.6963 | 2026-08-22 07:30:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 57.7 |
| 229edd57-15c3-3bdc-8cca-7af537cf9a60 | -6.8019 | -59.4008 | 2026-08-22 07:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 49.5 |
| 331efce6-56e8-342a-a0db-64e6a74263f9 | -8.3904 | -62.6774 | 2026-08-22 07:30:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 103.6 |
| 16203979-e00b-3e00-9256-4164067a5d19 | -6.7692 | -58.6679 | 2026-08-22 07:30:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 66.8 |
| 1c32fadc-b905-3a20-affd-a2ad62336d19 | -9.1722 | -59.4629 | 2026-08-22 07:30:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 64.0 |
| 772ec5dc-bb2f-3c59-8cd2-aa6e3a396da0 | -8.5406 | -54.8197 | 2026-08-22 07:30:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 47.5 |
| b2ee65a8-918f-3529-8049-35492b72dd6e | -6.7507 | -58.6687 | 2026-08-22 07:30:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 47.3 |
| 3110f3d7-aa34-3700-9ae7-e2c03c99e41f | -8.3718 | -62.697 | 2026-08-22 07:30:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 43.8 |
| 6dc885a5-89a1-3105-8c52-64852878b03f | -8.3719 | -62.6781 | 2026-08-22 07:30:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 80.1 |
| 642b70de-698f-333b-ad1f-68ac0dd30262 | -5.79586 | -57.54905 | 2026-08-22 07:39:00 | AQUA_M-M | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 9.5 |
| 19f7e658-a3b0-3af2-9a06-88bc67b49645 | -6.22799 | -55.62095 | 2026-08-22 07:39:00 | AQUA_M-M | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 22.8 |
| 8af8a033-99eb-3b1c-9b86-f68af757c735 | -8.3719 | -62.6781 | 2026-08-22 07:40:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 56.9 |
| 7493a886-f6d5-39e7-8f75-2dc22c200e58 | -6.7692 | -58.6679 | 2026-08-22 07:40:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 63.2 |
| 62a52f7c-019b-3551-ba98-1413a4090bd1 | -9.1722 | -59.4629 | 2026-08-22 07:40:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 61.9 |
| e2b1f925-249e-3486-96c8-1d124d91ec13 | -10.8172 | -50.9711 | 2026-08-22 07:40:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 39.9 |
| 3a64e011-537f-343b-943a-5443cd27b736 | -8.3904 | -62.6774 | 2026-08-22 07:40:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 105.1 |
| 2fa791d9-22dd-39c4-8cca-8a5d8c3e4ba1 | -6.8019 | -59.4008 | 2026-08-22 07:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 48.8 |
| 82c7444b-3c58-30c5-89e1-d6383dbe7e7f | -6.7507 | -58.6687 | 2026-08-22 07:40:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 50.1 |
| 21df76a8-3932-361a-8d18-ebe7d107295f | -6.7833 | -59.4208 | 2026-08-22 07:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 83.1 |
| bad39de5-ae08-344c-8fa7-58d7ea53940d | -6.8018 | -59.4201 | 2026-08-22 07:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 125.3 |
| 3e1028e0-5a50-3b9f-afb5-a48def992e4c | -6.7878 | -58.6477 | 2026-08-22 07:40:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 51.2 |
| 2f041bd5-26cf-391d-b163-bb7c3678cd91 | -13.99408 | -53.6521 | 2026-08-22 07:41:00 | AQUA_M-M | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 42.5 |
| e71347e0-839b-344b-8501-6dd559f39307 | -6.76928 | -58.67566 | 2026-08-22 07:41:00 | AQUA_M-M | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 14.6 |
| 97e4596c-df7c-3fb5-953f-97d4836e12a3 | -6.78768 | -59.40807 | 2026-08-22 07:41:00 | AQUA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 39.3 |
| d715ce0c-e638-3ba0-af90-d5a2d48e629d | -9.18843 | -59.45327 | 2026-08-22 07:41:00 | AQUA_M-M | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 10.0 |
| 4a5121b7-0937-3f76-89eb-bb802a3e53d5 | -13.98159 | -53.65878 | 2026-08-22 07:41:00 | AQUA_M-M | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 48.0 |
| 4ff5d7bb-e3bf-388b-aef9-6839939992f4 | -6.93356 | -59.30541 | 2026-08-22 07:41:00 | AQUA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 6.4 |
| 1adfe680-af07-30dd-b340-714057caea94 | -9.15728 | -59.46036 | 2026-08-22 07:41:00 | AQUA_M-M | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 18.2 |
| 208a3a92-1122-3cdf-b25a-dc500af1d059 | -8.89469 | -60.54253 | 2026-08-22 07:41:00 | AQUA_M-M | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 56.8 |
| b7eeb915-34fd-3e02-a19c-498ae33f62fb | -6.79875 | -59.66375 | 2026-08-22 07:41:00 | AQUA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 13.9 |
| 5526849b-147d-3b87-bf20-6b975ac86ffe | -6.80987 | -59.3897 | 2026-08-22 07:41:00 | AQUA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 13.0 |
| 48ed3585-31e7-3abe-9481-0d87eb44aa30 | -8.38933 | -62.68165 | 2026-08-22 07:41:00 | AQUA_M-M | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 47.9 |
| 2e951cc2-1be9-3979-9a1d-641fdd7a1e0b | -6.75234 | -58.65469 | 2026-08-22 07:41:00 | AQUA_M-M | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 30.2 |
| 8f32208c-c036-3c69-9124-309503a9b417 | -6.77766 | -58.68882 | 2026-08-22 07:41:00 | AQUA_M-M | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 10.3 |
| e040e56f-e207-329a-8a2d-55d7db5db802 | -6.26706 | -62.52676 | 2026-08-22 07:41:00 | AQUA_M-M | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 0a392ee8-eb5b-30f7-9a4e-6c653da0c45b | -12.64382 | -58.03462 | 2026-08-22 07:41:00 | AQUA_M-M | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 18.6 |
| 2819a108-8581-36cd-88e6-f30c07dd2650 | -6.80679 | -59.41087 | 2026-08-22 07:41:00 | AQUA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 13.6 |
| 7c65dccc-8057-3461-908f-72d899e78a23 | -12.64671 | -58.02958 | 2026-08-22 07:41:00 | AQUA_M-M | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 11.5 |
| c96d232f-1a24-3651-a14e-3c87fc8b6e94 | -6.8138 | -59.6622 | 2026-08-22 07:41:00 | AQUA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 13.7 |
| 8cdace9a-bc98-3f55-8143-b3a4308084db | -9.21556 | -59.76865 | 2026-08-22 07:41:00 | AQUA_M-M | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 8.6 |
| 514250a6-b8b9-3202-b0fa-199f5d7aa1fa | -6.79045 | -59.58915 | 2026-08-22 07:41:00 | AQUA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 6.8 |
| 5c65a2a8-a4d9-3363-aa5b-0856caf8a5e6 | -6.82175 | -59.67379 | 2026-08-22 07:41:00 | AQUA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 21.7 |
| 06697723-58f3-3b7f-b6ff-11c1fd33cd24 | -6.79724 | -59.40944 | 2026-08-22 07:41:00 | AQUA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 42.6 |
| c00af017-898f-3376-a8d6-d5c629f9a3ab | -12.64451 | -58.046 | 2026-08-22 07:41:00 | AQUA_M-M | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 15.6 |
| 21980b1e-d6bb-3824-a0be-245d8bc2a847 | -8.90208 | -60.54028 | 2026-08-22 07:41:00 | AQUA_M-M | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 24.0 |
| ba24ed66-4df4-3d4e-a100-cae449dc240f | -6.82323 | -59.66352 | 2026-08-22 07:41:00 | AQUA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 12.1 |
| 90c04d0c-959d-3305-864f-ceb5960d3828 | -7.59722 | -60.94114 | 2026-08-22 07:41:00 | AQUA_M-M | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 7.7 |
| 1f3c28c1-795a-39ce-a01c-74907e99a65c | -6.75063 | -58.66642 | 2026-08-22 07:41:00 | AQUA_M-M | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 30.4 |
| 6b709346-4047-3c60-976e-affd6bc61798 | -6.86345 | -59.02046 | 2026-08-22 07:41:00 | AQUA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 6.5 |
| f146456b-8c33-3245-9a6e-75470a311cfe | -9.17858 | -59.45184 | 2026-08-22 07:41:00 | AQUA_M-M | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 29.6 |
| 2f179fda-08c5-35a7-8ca9-08490347c2a5 | -8.52005 | -54.80007 | 2026-08-22 07:41:00 | AQUA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 25.2 |
| a5c0200e-9098-37d7-a99c-0441cc2599ca | -6.78615 | -59.41864 | 2026-08-22 07:41:00 | AQUA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 80.5 |
| a802ec83-24fd-31d1-b706-b18e11227746 | -8.39928 | -62.68985 | 2026-08-22 07:41:00 | AQUA_M-M | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 10.4 |
| f196ad28-41cc-3404-a0bb-db97e179e29e | -8.38057 | -62.68033 | 2026-08-22 07:41:00 | AQUA_M-M | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 122.2 |
| d7970109-d6f4-3c3b-a282-e49bc924f1de | -6.53484 | -58.52765 | 2026-08-22 07:41:00 | AQUA_M-M | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 35.3 |
| 3618d5c4-d93c-373c-b713-8ceafe5bf7d9 | -9.03695 | -60.44462 | 2026-08-22 07:41:00 | AQUA_M-M | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 7e1bb24d-4d92-3851-8658-94080e3342b6 | -6.97037 | -59.05374 | 2026-08-22 07:41:00 | AQUA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 13.3 |
| 5144c769-1a17-36f7-a738-36020df8dd5b | -6.81635 | -59.41223 | 2026-08-22 07:41:00 | AQUA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 16.4 |
| aaca74dd-e1e2-3694-8e45-5ccc867d7418 | -6.78426 | -58.64201 | 2026-08-22 07:41:00 | AQUA_M-M | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 17.9 |
| 79df420c-f448-3146-a1fa-5883baf1708f | -8.51683 | -54.82502 | 2026-08-22 07:41:00 | AQUA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 23.5 |
| 1dc5697b-f335-3f35-bbac-be7aaa4e8600 | -6.77071 | -58.66921 | 2026-08-22 07:41:00 | AQUA_M-M | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 14.7 |
| 9ce23267-e47f-3f85-ac27-85c5ffa603d4 | -6.80526 | -59.42139 | 2026-08-22 07:41:00 | AQUA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 28.3 |
| 375fea70-bfba-3da0-97b5-631683de090f | -6.76898 | -58.68095 | 2026-08-22 07:41:00 | AQUA_M-M | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 15.1 |
| 29c42831-03ab-3e6b-91ff-a8377bdac24c | -6.7957 | -59.42004 | 2026-08-22 07:41:00 | AQUA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 82.7 |
| 54ba00c4-8f59-36fd-bab6-1e770c81da27 | -9.1184 | -61.59282 | 2026-08-22 07:41:00 | AQUA_M-M | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 12.2 |
| 5fe1d24e-fc30-318f-be3d-b875174bcb0b | -8.39067 | -62.67285 | 2026-08-22 07:41:00 | AQUA_M-M | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 27.8 |
| 006e66a6-4491-3344-b13e-4bad26d0f8ae | -6.36802 | -62.89998 | 2026-08-22 07:41:00 | AQUA_M-M | TAPAUÁ | AMAZONAS | Brasil | 1304104 | 13 | 33 | nan | nan | nan | Amazônia | 7.4 |
| 532481fc-a6ff-3790-a696-00d4a049300d | -6.90765 | -58.99248 | 2026-08-22 07:41:00 | AQUA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 7.3 |
| 2bbd5bac-35ae-3a10-adf7-dfdf155fea3e | -9.09743 | -60.91573 | 2026-08-22 07:41:00 | AQUA_M-M | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 12.9 |
| 0b63a975-b480-39c1-b6a9-1e489b9ef321 | -6.76239 | -58.65608 | 2026-08-22 07:41:00 | AQUA_M-M | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 32.1 |
| 118dcaa3-cb6b-3922-a902-bc74b79bf1e1 | -8.89614 | -60.53272 | 2026-08-22 07:41:00 | AQUA_M-M | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 19.8 |
| 667fb5b0-2fb4-353b-b883-9dcf53f42ede | -9.15886 | -59.44903 | 2026-08-22 07:41:00 | AQUA_M-M | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 11.8 |
| a4b4c23f-e15b-3464-909b-da964147c961 | -6.8978 | -58.99118 | 2026-08-22 07:41:00 | AQUA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 5b91adcb-ff10-37d5-94d6-8034f299e26f | -6.13294 | -59.90797 | 2026-08-22 07:41:00 | AQUA_M-M | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 7.5 |
| 1941f9a2-f73b-3a44-a8f6-a01b7be96357 | -6.86184 | -59.0316 | 2026-08-22 07:41:00 | AQUA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 12.7 |
| 2ae64d2e-4395-3f00-8667-d7adf043d282 | -9.41094 | -60.4109 | 2026-08-22 07:41:00 | AQUA_M-M | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 7.3 |
| b34ebc1e-cf5f-30e8-811d-46a262e00221 | -8.53089 | -54.82693 | 2026-08-22 07:41:00 | AQUA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 67.3 |
| c278be76-b020-33c6-a1ff-5f2894fd49d5 | -9.16872 | -59.45045 | 2026-08-22 07:41:00 | AQUA_M-M | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 31.7 |
| 202a2016-a414-33ae-b139-850091420294 | -6.79432 | -58.64343 | 2026-08-22 07:41:00 | AQUA_M-M | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 44.4 |
| 06a7e373-f07e-300a-acc8-68f20d075c2f | -6.96056 | -59.05236 | 2026-08-22 07:41:00 | AQUA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 27.6 |
| 7cad7d0e-99bf-3397-9cc6-2f95355e9c1e | -8.388 | -62.69045 | 2026-08-22 07:41:00 | AQUA_M-M | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 7.2 |
| 8bd0c2ab-225c-3c1d-82c6-4991d2c8f1d7 | -6.79598 | -58.63171 | 2026-08-22 07:41:00 | AQUA_M-M | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 21.3 |
| 0c67730b-b6ab-322e-9841-6d46cab37c7f | -6.25961 | -62.51662 | 2026-08-22 07:41:00 | AQUA_M-M | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 1aabe7c7-5189-3e1c-bf9b-5116a7b16980 | -9.16713 | -59.46175 | 2026-08-22 07:41:00 | AQUA_M-M | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 32.2 |
| 0ad59faf-3ed0-39da-9800-8a8c396bec26 | -6.78592 | -58.63025 | 2026-08-22 07:41:00 | AQUA_M-M | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 8.9 |
| 82585ddc-22b4-3951-8b40-94ebdf3a13ef | -8.37923 | -62.68914 | 2026-08-22 07:41:00 | AQUA_M-M | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 7.0 |
| 4461cd2d-ddd2-3689-b3e3-7f2e7d40e721 | -6.79765 | -58.61989 | 2026-08-22 07:41:00 | AQUA_M-M | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 7.9 |
| 7e4e26fb-7482-3cec-ad26-8c21fc124662 | -9.17698 | -59.46316 | 2026-08-22 07:41:00 | AQUA_M-M | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 22.6 |
| 709bf4ce-0efb-3aea-9912-47139db30faf | -6.79417 | -59.4306 | 2026-08-22 07:41:00 | AQUA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 23.5 |
| b37799db-aeb9-3506-a2e2-0b8dca7f44f9 | -11.46531 | -54.30151 | 2026-08-22 07:41:00 | AQUA_M-M | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 31.0 |
| fe6262d2-6926-3b19-a36a-fbc6e56cfbd4 | -6.78463 | -59.42914 | 2026-08-22 07:41:00 | AQUA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 20.1 |
| 69a6b47f-2ea3-3963-943e-e66a95cdbf97 | -9.10651 | -60.91705 | 2026-08-22 07:41:00 | AQUA_M-M | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 10.8 |
| 2a3ed7bc-9f94-3d7a-b325-1d168805dabb | -6.53652 | -58.51579 | 2026-08-22 07:41:00 | AQUA_M-M | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 11.8 |


[Clique aqui para ver as próximas entradas](README83.md)
