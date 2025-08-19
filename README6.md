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

## Dados Diários - Página 6

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 79126d23-a9fe-327f-9737-0846d9e8499a | -12.6536 | -45.8082 | 2025-08-19 00:40:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 65.0 |
| 92caad61-8c10-3526-8a7b-9741e076aacf | -6.9524 | -43.6083 | 2025-08-19 00:40:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 136.0 |
| 4a564b47-8c22-371a-a3fc-9f93752b32c7 | -21.8869 | -48.1841 | 2025-08-19 00:40:00 | GOES-19 | ARARAQUARA | SÃO PAULO | Brasil | 3503208 | 35 | 33 | nan | nan | nan | Cerrado | 72.9 |
| 0bcd7d63-d98e-34b5-a743-aa01d82b6fd9 | -5.5785 | -44.0914 | 2025-08-19 00:40:00 | GOES-19 | GOVERNADOR LUIZ ROCHA | MARANHÃO | Brasil | 2104628 | 21 | 33 | nan | nan | nan | Cerrado | 84.8 |
| 8e5118af-b276-3a7f-a47d-f93cb4952144 | -16.4665 | -45.0743 | 2025-08-19 00:40:00 | GOES-19 | SÃO ROMÃO | MINAS GERAIS | Brasil | 3164209 | 31 | 33 | nan | nan | nan | Cerrado | 69.0 |
| 2d5050d0-a41e-3bb6-b654-f9788ffb7a9f | -16.4659 | -45.098 | 2025-08-19 00:40:00 | GOES-19 | SÃO ROMÃO | MINAS GERAIS | Brasil | 3164209 | 31 | 33 | nan | nan | nan | Cerrado | 94.7 |
| 50610048-b94d-34ab-992f-463bfccf0ca0 | -9.1895 | -59.6364 | 2025-08-19 00:40:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 77.8 |
| 1b8d4a1a-9091-3f29-9e8c-49ed72f575a8 | -11.8512 | -51.5801 | 2025-08-19 00:40:00 | GOES-19 | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Cerrado | 70.2 |
| 6ab49aca-0037-3599-99b4-4e6e700e0e01 | -9.1894 | -59.6558 | 2025-08-19 00:40:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 62.0 |
| 0d64f49a-2dc0-30bf-a3f7-a421a93753bc | -5.8807 | -48.1125 | 2025-08-19 00:40:00 | GOES-19 | ARAGUATINS | TOCANTINS | Brasil | 1702208 | 17 | 33 | nan | nan | nan | Cerrado | 64.1 |
| aac26644-4497-3273-9ad3-b3a0d4008137 | -3.982 | -42.516 | 2025-08-19 00:40:00 | GOES-19 | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 296.9 |
| 06e93c85-aa94-3c08-8c78-47afb537ccf9 | -6.9336 | -43.6101 | 2025-08-19 00:40:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 99.0 |
| 95f4b764-1436-3020-8afa-5fe4c80f3951 | -14.9812 | -54.7951 | 2025-08-19 00:40:00 | GOES-19 | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 79.5 |
| 637ba7a9-e004-34eb-8e2f-d91247a2f904 | -13.2563 | -50.8162 | 2025-08-19 00:40:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 59.9 |
| 9032b245-36a3-3027-8d8d-bb1847fcd698 | -11.8702 | -51.578 | 2025-08-19 00:40:00 | GOES-19 | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Cerrado | 135.5 |
| 2651885a-7883-32e5-b52a-82e0258f9cb4 | -9.5351 | -63.5771 | 2025-08-19 00:40:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 39.4 |
| bd53e58f-639b-32df-83e2-497bc33b20ec | -3.9819 | -42.5396 | 2025-08-19 00:40:00 | GOES-19 | NOSSA SENHORA DOS REMÉDIOS | PIAUÍ | Brasil | 2206803 | 22 | 33 | nan | nan | nan | Caatinga | 144.8 |
| 74047b8a-826b-3501-a9e4-ff67555eb9e0 | -5.5787 | -44.0684 | 2025-08-19 00:40:00 | GOES-19 | GOVERNADOR LUIZ ROCHA | MARANHÃO | Brasil | 2104628 | 21 | 33 | nan | nan | nan | Cerrado | 56.4 |
| bfcdebd0-0e66-39bc-ab03-01153796b133 | -5.7887 | -43.6134 | 2025-08-19 00:40:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 79.0 |
| 2d65af87-a1ba-3549-9141-473ed940478d | -6.9715 | -43.5833 | 2025-08-19 00:40:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 135.0 |
| 1408f43e-c5ca-3393-9379-8921b166b9e0 | -15.4243 | -49.5702 | 2025-08-19 00:40:00 | GOES-19 | RIALMA | GOIÁS | Brasil | 5218607 | 52 | 33 | nan | nan | nan | Cerrado | 116.2 |
| 9137256b-faf6-3971-af3e-c84472f62de8 | -24.91772 | -50.10885 | 2025-08-19 00:43:00 | TERRA_M-M | CARAMBEÍ | PARANÁ | Brasil | 4104659 | 41 | 33 | nan | nan | nan | Mata Atlântica | 8.9 |
| fd99c160-4569-3382-9130-ab7556e7b5ac | -20.2394 | -44.18757 | 2025-08-19 00:45:00 | TERRA_M-M | BONFIM | MINAS GERAIS | Brasil | 3108107 | 31 | 33 | nan | nan | nan | Mata Atlântica | 31.5 |
| 76bc6f91-9190-3b83-aa1f-f9c5a328273c | -23.77453 | -51.7169 | 2025-08-19 00:45:00 | TERRA_M-M | MARUMBI | PARANÁ | Brasil | 4115507 | 41 | 33 | nan | nan | nan | Mata Atlântica | 56.0 |
| 65e987d3-e742-3ab3-801f-3476e219e97c | -23.45694 | -47.12565 | 2025-08-19 00:45:00 | TERRA_M-M | ARAÇARIGUAMA | SÃO PAULO | Brasil | 3502754 | 35 | 33 | nan | nan | nan | Mata Atlântica | 21.7 |
| 091bfc6b-7f09-330e-86cc-0a1df775e357 | -21.39141 | -48.57778 | 2025-08-19 00:45:00 | TERRA_M-M | TAQUARITINGA | SÃO PAULO | Brasil | 3553708 | 35 | 33 | nan | nan | nan | Mata Atlântica | 6.6 |
| ac8b66ef-523e-3480-848c-39c1d9bed741 | -21.24295 | -49.08968 | 2025-08-19 00:45:00 | TERRA_M-M | MARAPOAMA | SÃO PAULO | Brasil | 3528858 | 35 | 33 | nan | nan | nan | Mata Atlântica | 6.7 |
| cd0e285d-d07e-35b8-b51c-63bf7f5bf898 | -23.08923 | -46.2733 | 2025-08-19 00:45:00 | TERRA_M-M | PIRACAIA | SÃO PAULO | Brasil | 3538600 | 35 | 33 | nan | nan | nan | Mata Atlântica | 11.8 |
| 8a0e5545-4eb2-3a9a-870c-697e3d5a1a21 | -22.88332 | -47.48637 | 2025-08-19 00:45:00 | TERRA_M-M | CAPIVARI | SÃO PAULO | Brasil | 3510401 | 35 | 33 | nan | nan | nan | Mata Atlântica | 17.5 |
| 44d0b3fd-1f1b-3112-84f5-57de78fb2e17 | -23.31146 | -46.89619 | 2025-08-19 00:45:00 | TERRA_M-M | CAJAMAR | SÃO PAULO | Brasil | 3509205 | 35 | 33 | nan | nan | nan | Mata Atlântica | 6.6 |
| 8152de4a-fcbf-3dca-adba-c0b46028df93 | -22.88477 | -47.4963 | 2025-08-19 00:45:00 | TERRA_M-M | CAPIVARI | SÃO PAULO | Brasil | 3510401 | 35 | 33 | nan | nan | nan | Mata Atlântica | 19.9 |
| 15f4f23f-b977-35e3-b2a2-338675f6e47b | -21.88773 | -48.18277 | 2025-08-19 00:45:00 | TERRA_M-M | ARARAQUARA | SÃO PAULO | Brasil | 3503208 | 35 | 33 | nan | nan | nan | Cerrado | 6.3 |
| efb2d51b-c671-344c-b73d-a23fb07178c0 | -21.40193 | -45.00556 | 2025-08-19 00:45:00 | TERRA_M-M | INGAÍ | MINAS GERAIS | Brasil | 3130804 | 31 | 33 | nan | nan | nan | Mata Atlântica | 31.9 |
| 217faae3-e4d1-3bf6-b697-929f9f73a359 | -23.77314 | -51.70507 | 2025-08-19 00:45:00 | TERRA_M-M | MARUMBI | PARANÁ | Brasil | 4115507 | 41 | 33 | nan | nan | nan | Mata Atlântica | 17.3 |
| 7a1da2ac-b8ae-3c18-bff4-7df56959489f | -23.77594 | -51.72887 | 2025-08-19 00:45:00 | TERRA_M-M | MARUMBI | PARANÁ | Brasil | 4115507 | 41 | 33 | nan | nan | nan | Mata Atlântica | 5.6 |
| a5b4fe88-049e-3624-9216-689ff4118199 | -21.23277 | -49.08165 | 2025-08-19 00:45:00 | TERRA_M-M | MARAPOAMA | SÃO PAULO | Brasil | 3528858 | 35 | 33 | nan | nan | nan | Mata Atlântica | 8.5 |
| 1446a1a0-86a4-3dc2-a29d-9873cf36f8a0 | -21.87405 | -48.21478 | 2025-08-19 00:45:00 | TERRA_M-M | ARARAQUARA | SÃO PAULO | Brasil | 3503208 | 35 | 33 | nan | nan | nan | Cerrado | 7.7 |
| edbe7563-1b64-355e-9f4c-8ac17d5ecb67 | -21.98309 | -50.35158 | 2025-08-19 00:45:00 | TERRA_M-M | HERCULÂNDIA | SÃO PAULO | Brasil | 3519006 | 35 | 33 | nan | nan | nan | Mata Atlântica | 12.2 |
| 48204af9-3da5-38f6-b734-bfa46b0f721f | -21.87266 | -48.20508 | 2025-08-19 00:45:00 | TERRA_M-M | ARARAQUARA | SÃO PAULO | Brasil | 3503208 | 35 | 33 | nan | nan | nan | Cerrado | 17.0 |
| c98a2f57-ddce-3a48-a9d1-2f8434fad907 | -21.88913 | -48.19253 | 2025-08-19 00:45:00 | TERRA_M-M | ARARAQUARA | SÃO PAULO | Brasil | 3503208 | 35 | 33 | nan | nan | nan | Cerrado | 83.6 |
| dfe8466e-f339-3cc3-8db6-4a63492a03dc | -21.66166 | -49.73277 | 2025-08-19 00:45:00 | TERRA_M-M | LINS | SÃO PAULO | Brasil | 3527108 | 35 | 33 | nan | nan | nan | Mata Atlântica | 16.1 |
| f4aa6a48-bce1-3c57-9e6b-8ffb6a5f3494 | -21.24163 | -49.08022 | 2025-08-19 00:45:00 | TERRA_M-M | MARAPOAMA | SÃO PAULO | Brasil | 3528858 | 35 | 33 | nan | nan | nan | Mata Atlântica | 8.4 |
| 41179750-8d16-327d-877f-4e8d6dbfc5ce | -22.8497 | -48.47144 | 2025-08-19 00:45:00 | TERRA_M-M | BOTUCATU | SÃO PAULO | Brasil | 3507506 | 35 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 6a024eb2-069c-3493-a76a-5a48680d79eb | -15.04588 | -54.82597 | 2025-08-19 00:48:00 | TERRA_M-M | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 22.4 |
| 0d1cffbf-c324-32d8-9d8f-5879e0afb8cb | -14.97308 | -54.80114 | 2025-08-19 00:48:00 | TERRA_M-M | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 43.2 |
| a2c99ac1-3e53-3c62-9ce0-f735d0a9cd92 | -12.04464 | -44.00366 | 2025-08-19 00:48:00 | TERRA_M-M | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 14.2 |
| 8559331f-50c8-34a9-9970-09aa0aa10ec1 | -15.49388 | -50.31348 | 2025-08-19 00:48:00 | TERRA_M-M | FAINA | GOIÁS | Brasil | 5207535 | 52 | 33 | nan | nan | nan | Cerrado | 6.8 |
| de016f5e-a6f0-3470-a3dd-476f33f37a81 | -15.41653 | -49.57359 | 2025-08-19 00:48:00 | TERRA_M-M | RIALMA | GOIÁS | Brasil | 5218607 | 52 | 33 | nan | nan | nan | Cerrado | 59.2 |
| e92cebf6-5e24-3759-b6a1-b151adb4736c | -20.87449 | -54.98556 | 2025-08-19 00:48:00 | TERRA_M-M | SIDROLÂNDIA | MATO GROSSO DO SUL | Brasil | 5007901 | 50 | 33 | nan | nan | nan | Cerrado | 17.9 |
| d1014494-b153-3f72-87b0-25dd7cc8036d | -20.92663 | -57.64622 | 2025-08-19 00:48:00 | TERRA_M-M | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Pantanal | 29.9 |
| 90ed69ef-b9db-3e9d-bfa1-7bac5869bb6d | -15.40627 | -49.56569 | 2025-08-19 00:48:00 | TERRA_M-M | RIALMA | GOIÁS | Brasil | 5218607 | 52 | 33 | nan | nan | nan | Cerrado | 61.1 |
| e9268540-9cb3-3716-a890-881241b46be6 | -16.50195 | -45.09829 | 2025-08-19 00:48:00 | TERRA_M-M | PONTO CHIQUE | MINAS GERAIS | Brasil | 3152131 | 31 | 33 | nan | nan | nan | Cerrado | 9.1 |
| fca8cdc8-c54e-3866-94d7-294e6de9c42d | -15.39926 | -49.13343 | 2025-08-19 00:48:00 | TERRA_M-M | GOIANÉSIA | GOIÁS | Brasil | 5208608 | 52 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 3ce2e351-922e-3e3f-bf37-cb0e73026e6e | -17.88614 | -48.61274 | 2025-08-19 00:48:00 | TERRA_M-M | CALDAS NOVAS | GOIÁS | Brasil | 5204508 | 52 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 8c1e2389-496c-3cfb-b496-c7c11cab83ba | -17.33554 | -47.17249 | 2025-08-19 00:48:00 | TERRA_M-M | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 13.6 |
| 22a5f814-ee9a-3f1c-9616-51b264f44ea7 | -12.04834 | -44.0265 | 2025-08-19 00:48:00 | TERRA_M-M | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 23.7 |
| f2fb3f09-df6c-3d67-8dc2-2944ea4916a1 | -20.92529 | -57.65162 | 2025-08-19 00:48:00 | TERRA_M-M | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Pantanal | 27.5 |
| e6d2de9a-38d5-3a08-a7d2-cf9accfc21af | -19.98457 | -47.89692 | 2025-08-19 00:48:00 | TERRA_M-M | UBERABA | MINAS GERAIS | Brasil | 3170107 | 31 | 33 | nan | nan | nan | Cerrado | 15.1 |
| 3e62b26a-36b4-3928-b248-fd7e19d02723 | -13.26206 | -50.81931 | 2025-08-19 00:48:00 | TERRA_M-M | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 28.8 |
| 651e8144-cc09-3507-8598-a5fa23457702 | -15.83739 | -48.17073 | 2025-08-19 00:48:00 | TERRA_M-M | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 11.2 |
| 60c49f16-45c6-3b5f-8898-73f0feb877ba | -19.19953 | -46.84181 | 2025-08-19 00:48:00 | TERRA_M-M | SERRA DO SALITRE | MINAS GERAIS | Brasil | 3166808 | 31 | 33 | nan | nan | nan | Cerrado | 9.2 |
| 33af7dc0-0062-3909-a720-e4b3cf43bf3d | -13.26332 | -50.82835 | 2025-08-19 00:48:00 | TERRA_M-M | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 13.0 |
| 293c6548-57ef-3a17-b139-1faedb8deeb7 | -13.24846 | -50.79995 | 2025-08-19 00:48:00 | TERRA_M-M | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 7.0 |
| ac2fd156-1ef8-3cad-983c-bd091ff30526 | -15.02286 | -54.8159 | 2025-08-19 00:48:00 | TERRA_M-M | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 47.2 |
| 4d14d413-2d51-38da-8e7d-9bb673c305b7 | -13.29744 | -50.81406 | 2025-08-19 00:48:00 | TERRA_M-M | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 61c221fd-4d25-3a69-86c5-bc2dfef35c7c | -16.48804 | -45.08468 | 2025-08-19 00:48:00 | TERRA_M-M | PONTO CHIQUE | MINAS GERAIS | Brasil | 3152131 | 31 | 33 | nan | nan | nan | Cerrado | 14.0 |
| 5d63d819-ef3a-356b-bcc1-a6d623d0cb79 | -12.98869 | -45.19297 | 2025-08-19 00:48:00 | TERRA_M-M | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 25.1 |
| 3e5f3e33-3965-3fac-b170-5766f636eb9c | -17.81887 | -44.49421 | 2025-08-19 00:48:00 | TERRA_M-M | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 14.0 |
| 0a528e42-e88c-3f56-9281-e0fd66848e15 | -15.04418 | -54.81222 | 2025-08-19 00:48:00 | TERRA_M-M | CAMPO VERDE | MATO GROSSO | Brasil | 5102678 | 51 | 33 | nan | nan | nan | Cerrado | 14.6 |
| aa40ee06-6bf8-3a94-8823-e06b27ba030e | -16.62922 | -51.35764 | 2025-08-19 00:48:00 | TERRA_M-M | PALESTINA DE GOIÁS | GOIÁS | Brasil | 5215652 | 52 | 33 | nan | nan | nan | Cerrado | 8.0 |
| 9bb61b69-be31-3344-85ab-a8d6e234079f | -15.75076 | -46.61139 | 2025-08-19 00:48:00 | TERRA_M-M | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 20.2 |
| 82fc56df-b21a-3f99-8eee-f16f8a1f7668 | -16.71685 | -47.63054 | 2025-08-19 00:48:00 | TERRA_M-M | CRISTALINA | GOIÁS | Brasil | 5206206 | 52 | 33 | nan | nan | nan | Cerrado | 12.4 |
| 83ae9776-34d6-36c7-8e99-794ce3891545 | -17.34523 | -47.1709 | 2025-08-19 00:48:00 | TERRA_M-M | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 11.9 |
| d60da658-0744-374f-b0f1-0475cc99b46d | -13.588 | -47.00576 | 2025-08-19 00:48:00 | TERRA_M-M | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 12.1 |
| 0b0bfde9-203c-33a6-af14-94268b805ac3 | -15.68663 | -47.65799 | 2025-08-19 00:48:00 | TERRA_M-M | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 7.2 |
| 9b2a290c-b597-3ca0-94ce-dbf008b32e2c | -14.84586 | -48.06809 | 2025-08-19 00:48:00 | TERRA_M-M | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 12.2 |
| 6b159d80-e301-3c39-a940-0ee024f3a542 | -14.87281 | -48.05288 | 2025-08-19 00:48:00 | TERRA_M-M | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 19.9 |
| ed3d54de-4ce4-3d18-aed9-d1808fbc326b | -12.95593 | -46.12748 | 2025-08-19 00:48:00 | TERRA_M-M | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 12.1 |
| 06cb5252-f62e-38b9-92e6-422904ec1261 | -12.6528 | -45.81566 | 2025-08-19 00:48:00 | TERRA_M-M | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 68.1 |
| e3a927e7-b010-3ae6-bb22-08c5e44c5257 | -14.17506 | -45.31386 | 2025-08-19 00:48:00 | TERRA_M-M | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 18.2 |
| a355616f-b412-3d0a-984f-2a02fdb8991c | -13.00357 | -45.2084 | 2025-08-19 00:48:00 | TERRA_M-M | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 16.0 |
| fdec068d-dfdc-3d51-8e63-fa5fe0afe140 | -13.58617 | -46.99387 | 2025-08-19 00:48:00 | TERRA_M-M | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 10.4 |
| d55853f7-1f15-32a8-b48e-f4b1a9160155 | -15.49261 | -50.30434 | 2025-08-19 00:48:00 | TERRA_M-M | FAINA | GOIÁS | Brasil | 5207535 | 52 | 33 | nan | nan | nan | Cerrado | 5.4 |
| ea618fc7-18fb-30e7-82b6-0b21f726f756 | -12.65537 | -45.83174 | 2025-08-19 00:48:00 | TERRA_M-M | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 19.3 |
| 4972cf15-01af-360d-a015-146c785dce65 | -13.31388 | -50.80239 | 2025-08-19 00:48:00 | TERRA_M-M | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 8.6 |
| 2357f8e2-175d-3440-9fce-a83af797456e | -12.49598 | -45.56175 | 2025-08-19 00:48:00 | TERRA_M-M | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 21.8 |
| ff859aee-6c78-3d12-9ede-9f03c191ab09 | -15.40893 | -49.58426 | 2025-08-19 00:48:00 | TERRA_M-M | RIALMA | GOIÁS | Brasil | 5218607 | 52 | 33 | nan | nan | nan | Cerrado | 9.5 |
| 059e12c2-a567-379a-8dd3-0ecdcb68b101 | -14.98916 | -54.80716 | 2025-08-19 00:48:00 | TERRA_M-M | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 33.9 |
| af44a183-3783-302d-b31b-2f068058153b | -17.56235 | -44.47641 | 2025-08-19 00:48:00 | TERRA_M-M | VÁRZEA DA PALMA | MINAS GERAIS | Brasil | 3170800 | 31 | 33 | nan | nan | nan | Cerrado | 26.4 |
| e45b0941-d3f4-3a6d-a5c2-40fa972592d6 | -20.33176 | -51.71468 | 2025-08-19 00:48:00 | TERRA_M-M | SELVÍRIA | MATO GROSSO DO SUL | Brasil | 5007802 | 50 | 33 | nan | nan | nan | Cerrado | 21.0 |
| 93fc4259-ff42-3ba3-bbcb-d020efdfe6ba | -14.64561 | -54.90403 | 2025-08-19 00:48:00 | TERRA_M-M | PLANALTO DA SERRA | MATO GROSSO | Brasil | 5106455 | 51 | 33 | nan | nan | nan | Cerrado | 8.7 |
| be398ca8-aff2-3590-8b09-85a25810c106 | -15.84671 | -48.16909 | 2025-08-19 00:48:00 | TERRA_M-M | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 17.0 |
| 2f5ef5b8-e997-3806-9abe-050f8ad88be4 | -16.61897 | -51.34964 | 2025-08-19 00:48:00 | TERRA_M-M | PALESTINA DE GOIÁS | GOIÁS | Brasil | 5215652 | 52 | 33 | nan | nan | nan | Cerrado | 10.3 |
| 7a3a605a-11fd-3c91-8d7a-0faf4efab0de | -20.29942 | -50.96513 | 2025-08-19 00:48:00 | TERRA_M-M | SANTA FÉ DO SUL | SÃO PAULO | Brasil | 3546603 | 35 | 33 | nan | nan | nan | Mata Atlântica | 7.9 |
| 4a046597-34d6-3eb6-91e2-55d5e6e5a8fe | -16.47931 | -45.10242 | 2025-08-19 00:48:00 | TERRA_M-M | PONTO CHIQUE | MINAS GERAIS | Brasil | 3152131 | 31 | 33 | nan | nan | nan | Cerrado | 108.5 |
| 3dfb24c6-1093-3343-8b33-d9e1ef4a81ad | -16.30791 | -49.17192 | 2025-08-19 00:48:00 | TERRA_M-M | OURO VERDE DE GOIÁS | GOIÁS | Brasil | 5215405 | 52 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 6a01742d-0e4c-350b-b6d6-b15ba3b558fa | -16.81495 | -49.36803 | 2025-08-19 00:48:00 | TERRA_M-M | GOIÂNIA | GOIÁS | Brasil | 5208707 | 52 | 33 | nan | nan | nan | Cerrado | 5.3 |
| c48a96ed-c59a-3a54-bbab-7af3ffcce9e1 | -19.9463 | -48.20127 | 2025-08-19 00:48:00 | TERRA_M-M | CONCEIÇÃO DAS ALAGOAS | MINAS GERAIS | Brasil | 3117306 | 31 | 33 | nan | nan | nan | Cerrado | 15.5 |
| 6f4f61cd-920f-3b39-9425-b663dc718f03 | -17.89376 | -48.6016 | 2025-08-19 00:48:00 | TERRA_M-M | CALDAS NOVAS | GOIÁS | Brasil | 5204508 | 52 | 33 | nan | nan | nan | Cerrado | 6.7 |
| e92bfe94-8fc4-3827-8540-dbd4c6db724d | -14.50525 | -45.94039 | 2025-08-19 00:48:00 | TERRA_M-M | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 28.1 |


[Clique aqui para ver as próximas entradas](README7.md)
