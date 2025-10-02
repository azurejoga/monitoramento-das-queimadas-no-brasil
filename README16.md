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

## Dados Diários - Página 16

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 5b7ca984-3ff2-3db5-85d2-fa0097bd3f7b | -19.44056 | -44.16781 | 2025-10-02 03:15:00 | NOAA-20 | SETE LAGOAS | MINAS GERAIS | Brasil | 3167202 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 8c5753e9-2ad3-330b-974f-65553e0212eb | -20.87881 | -43.20648 | 2025-10-02 03:15:00 | NOAA-20 | BRÁS PIRES | MINAS GERAIS | Brasil | 3108701 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| c25219ae-ab02-3024-ae3f-dd2ca0fdbc63 | -21.23569 | -44.07073 | 2025-10-02 03:15:00 | NOAA-20 | SÃO JOÃO DEL REI | MINAS GERAIS | Brasil | 3162500 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.7 |
| a22209dd-32a2-3aa4-8a72-fcfa98f0d0d6 | -18.49532 | -43.4062 | 2025-10-02 03:15:00 | NOAA-20 | SERRO | MINAS GERAIS | Brasil | 3167103 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| e775813e-faca-36be-b733-c21a6a7279f1 | -20.21851 | -43.90134 | 2025-10-02 03:15:00 | NOAA-20 | ITABIRITO | MINAS GERAIS | Brasil | 3131901 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.4 |
| a847199a-4e2f-3444-958b-866431d52ce0 | -19.85868 | -42.58769 | 2025-10-02 03:15:00 | NOAA-20 | DIONÍSIO | MINAS GERAIS | Brasil | 3121803 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| 11c9b6a1-1ae1-3cc3-8042-2967fdaef4cf | -20.22226 | -43.90451 | 2025-10-02 03:15:00 | NOAA-20 | ITABIRITO | MINAS GERAIS | Brasil | 3131901 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| c553a4a5-ad9e-35ad-bbdc-92f2b4a9c479 | -18.33941 | -42.41175 | 2025-10-02 03:15:00 | NOAA-20 | JOSÉ RAYDAN | MINAS GERAIS | Brasil | 3136553 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| 5222aa73-b45a-3c09-b25f-9dcf765f87d9 | -18.463 | -40.56992 | 2025-10-02 03:15:00 | NOAA-20 | ECOPORANGA | ESPÍRITO SANTO | Brasil | 3202108 | 32 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| e20e79ac-2144-3065-80f3-68c871fd1feb | -18.70392 | -43.18622 | 2025-10-02 03:15:00 | NOAA-20 | SABINÓPOLIS | MINAS GERAIS | Brasil | 3156809 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.7 |
| 97403b21-b911-342f-aaff-74ff463dd61f | -22.6212 | -44.50571 | 2025-10-02 03:15:00 | NOAA-20 | RESENDE | RIO DE JANEIRO | Brasil | 3304201 | 33 | 33 | nan | nan | nan | Mata Atlântica | 2.9 |
| c7d89f92-2c20-3fe7-ad9d-4ef74ac869cd | -21.22949 | -44.07308 | 2025-10-02 03:15:00 | NOAA-20 | SÃO JOÃO DEL REI | MINAS GERAIS | Brasil | 3162500 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 5abc315c-3783-3911-85dd-811c46f5e492 | -19.45327 | -44.29647 | 2025-10-02 03:15:00 | NOAA-20 | SETE LAGOAS | MINAS GERAIS | Brasil | 3167202 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 029b2a10-6e44-342c-a7b9-0ecb85ccc4ea | -18.34052 | -42.40687 | 2025-10-02 03:15:00 | NOAA-20 | JOSÉ RAYDAN | MINAS GERAIS | Brasil | 3136553 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| 09d5a620-5ab2-317f-b5df-568de678a005 | -19.28456 | -43.75329 | 2025-10-02 03:15:00 | NOAA-20 | JABOTICATUBAS | MINAS GERAIS | Brasil | 3134608 | 31 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 7af46949-88b1-3fff-acbd-08c9160b124d | -18.99578 | -43.01064 | 2025-10-02 03:15:00 | NOAA-20 | SENHORA DO PORTO | MINAS GERAIS | Brasil | 3166105 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| a8b1651c-06ed-39e6-b2fc-2c0490ae76d1 | -18.33968 | -44.5071 | 2025-10-02 03:15:00 | NOAA-20 | CORINTO | MINAS GERAIS | Brasil | 3119104 | 31 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 88f4c8d8-1083-3b75-97f1-fba3a1a3b199 | -21.2375 | -44.06841 | 2025-10-02 03:15:00 | NOAA-20 | SÃO JOÃO DEL REI | MINAS GERAIS | Brasil | 3162500 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 486cca9e-e912-3018-8fc3-298162ec04eb | -20.22897 | -43.90552 | 2025-10-02 03:15:00 | NOAA-20 | ITABIRITO | MINAS GERAIS | Brasil | 3131901 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.7 |
| 77391db9-0a57-31a8-a7e9-e03c70512735 | -19.36884 | -41.75671 | 2025-10-02 03:15:00 | NOAA-20 | TARUMIRIM | MINAS GERAIS | Brasil | 3168408 | 31 | 33 | nan | nan | nan | Mata Atlântica | 5.9 |
| 0243dd58-28ce-3739-9373-293e8cf711b8 | -19.59062 | -42.47639 | 2025-10-02 03:15:00 | NOAA-20 | BOM JESUS DO GALHO | MINAS GERAIS | Brasil | 3107802 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.4 |
| 65022ca8-a2fa-3769-9dd3-9e6c7a766274 | -19.44205 | -44.16159 | 2025-10-02 03:15:00 | NOAA-20 | SETE LAGOAS | MINAS GERAIS | Brasil | 3167202 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| cf40f464-e819-334d-89e2-5c7b02368b97 | -18.50185 | -44.04593 | 2025-10-02 03:15:00 | NOAA-20 | SANTO HIPÓLITO | MINAS GERAIS | Brasil | 3160603 | 31 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 5f145ae3-b45c-38ef-9897-56a438c8a5b5 | -19.28745 | -43.75451 | 2025-10-02 03:15:00 | NOAA-20 | JABOTICATUBAS | MINAS GERAIS | Brasil | 3134608 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| bbc45833-1897-3776-8719-707461a46b07 | -19.67152 | -43.87599 | 2025-10-02 03:15:00 | NOAA-20 | LAGOA SANTA | MINAS GERAIS | Brasil | 3137601 | 31 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 442fc0ee-9099-3e53-9004-76fba978e474 | -19.95626 | -43.65499 | 2025-10-02 03:15:00 | NOAA-20 | CAETÉ | MINAS GERAIS | Brasil | 3110004 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.9 |
| 81fa229c-57ce-30ad-b356-d416ee384f49 | -18.46215 | -40.57391 | 2025-10-02 03:15:00 | NOAA-20 | ECOPORANGA | ESPÍRITO SANTO | Brasil | 3202108 | 32 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 6858711a-1a31-3537-8c98-4c4e83cdef24 | -20.22731 | -43.91236 | 2025-10-02 03:15:00 | NOAA-20 | ITABIRITO | MINAS GERAIS | Brasil | 3131901 | 31 | 33 | nan | nan | nan | Mata Atlântica | 5.5 |
| 2525256c-9f07-35c1-994f-415f1a19e960 | -22.07861 | -43.09249 | 2025-10-02 03:15:00 | NOAA-20 | CHIADOR | MINAS GERAIS | Brasil | 3116209 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| a709680a-ea97-3ab7-a01c-4e320c339dbb | -19.67505 | -43.8769 | 2025-10-02 03:15:00 | NOAA-20 | LAGOA SANTA | MINAS GERAIS | Brasil | 3137601 | 31 | 33 | nan | nan | nan | Cerrado | 2.9 |
| d724fd6d-9e57-3c2e-b0f4-a534d4cee471 | -22.61966 | -44.51191 | 2025-10-02 03:15:00 | NOAA-20 | RESENDE | RIO DE JANEIRO | Brasil | 3304201 | 33 | 33 | nan | nan | nan | Mata Atlântica | 2.8 |
| 1f1c6b01-aec2-3fd5-b284-a7435000d667 | -20.22367 | -43.90891 | 2025-10-02 03:15:00 | NOAA-20 | ITABIRITO | MINAS GERAIS | Brasil | 3131901 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.4 |
| 469d8ae5-cfdc-3af8-a89f-d733c7dbcaf1 | -19.95811 | -43.65425 | 2025-10-02 03:15:00 | NOAA-20 | CAETÉ | MINAS GERAIS | Brasil | 3110004 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| de42c6ce-2444-3889-9474-c9b5c5acf593 | -20.22078 | -43.91062 | 2025-10-02 03:15:00 | NOAA-20 | ITABIRITO | MINAS GERAIS | Brasil | 3131901 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 35d796f3-8d73-32e3-ad3d-f5d52437d4b6 | -20.21027 | -44.18565 | 2025-10-02 03:15:00 | NOAA-20 | BRUMADINHO | MINAS GERAIS | Brasil | 3109006 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| 7a84b602-2a38-3e4e-a402-8ad5bf83a318 | -21.5771 | -44.96659 | 2025-10-02 03:15:00 | NOAA-20 | LUMINÁRIAS | MINAS GERAIS | Brasil | 3138708 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.5 |
| 4e20b82a-571f-3eba-95b5-5a07ded5599f | -19.88734 | -42.62563 | 2025-10-02 03:15:00 | NOAA-20 | DIONÍSIO | MINAS GERAIS | Brasil | 3121803 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| fcd1509e-8650-3436-9181-530b26041d07 | -19.57784 | -41.90619 | 2025-10-02 03:15:00 | NOAA-20 | IMBÉ DE MINAS | MINAS GERAIS | Brasil | 3130556 | 31 | 33 | nan | nan | nan | Mata Atlântica | 5.0 |
| 9f1be6fc-bcc1-3dc3-af20-3a9e245d467e | -19.00099 | -43.01721 | 2025-10-02 03:15:00 | NOAA-20 | DORES DE GUANHÃES | MINAS GERAIS | Brasil | 3123106 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 609ca5d5-b75f-3b7e-89c2-545f8af22b0f | -22.51868 | -44.78949 | 2025-10-02 03:15:00 | NOAA-20 | QUELUZ | SÃO PAULO | Brasil | 3541901 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 02764fd6-f449-3aa3-ade3-65512b3263e2 | -18.58681 | -43.04671 | 2025-10-02 03:15:00 | NOAA-20 | SABINÓPOLIS | MINAS GERAIS | Brasil | 3156809 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 628fe034-1b4c-3400-85d4-03dab6e64edf | -18.34293 | -44.50657 | 2025-10-02 03:15:00 | NOAA-20 | CORINTO | MINAS GERAIS | Brasil | 3119104 | 31 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 3822c83e-6547-3c19-b63d-4edecb697e80 | -19.45539 | -44.28543 | 2025-10-02 03:15:00 | NOAA-20 | SETE LAGOAS | MINAS GERAIS | Brasil | 3167202 | 31 | 33 | nan | nan | nan | Cerrado | 4.3 |
| b60bc45b-3489-349e-9120-92b1f0c53751 | -19.88618 | -42.6306 | 2025-10-02 03:15:00 | NOAA-20 | DIONÍSIO | MINAS GERAIS | Brasil | 3121803 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.3 |
| 5363ac2b-d0ac-3551-b04c-27b7b6ed71e2 | -21.57864 | -44.96051 | 2025-10-02 03:15:00 | NOAA-20 | LUMINÁRIAS | MINAS GERAIS | Brasil | 3138708 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.6 |
| e847ece4-caed-326b-8919-5aaaa25a7fbf | -21.56365 | -45.27848 | 2025-10-02 03:15:00 | NOAA-20 | VARGINHA | MINAS GERAIS | Brasil | 3170701 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| 32606eaf-217b-35eb-976a-47de4cfcdd2c | -19.85752 | -42.59275 | 2025-10-02 03:15:00 | NOAA-20 | DIONÍSIO | MINAS GERAIS | Brasil | 3121803 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 16087c8f-0a59-3953-ace3-e70df81fbe75 | -19.95454 | -43.66216 | 2025-10-02 03:15:00 | NOAA-20 | CAETÉ | MINAS GERAIS | Brasil | 3110004 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.9 |
| 8a6c2902-93a4-3f36-92b1-ecdbf5495bf3 | -19.4554 | -44.28774 | 2025-10-02 03:15:00 | NOAA-20 | SETE LAGOAS | MINAS GERAIS | Brasil | 3167202 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 1d401617-1b1d-3df4-933c-b74587744570 | -6.6955 | -48.7062 | 2025-10-02 03:20:00 | GOES-19 | ARAGOMINAS | TOCANTINS | Brasil | 1701309 | 17 | 33 | nan | nan | nan | Amazônia | 67.5 |
| 41b2fb4d-cff7-336b-a06b-365b9cb31bcd | -9.9182 | -43.7212 | 2025-10-02 03:20:00 | GOES-19 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 102.9 |
| 6bdbc4c5-8fa8-3e60-8141-cb5eea989247 | -5.3193 | -43.7636 | 2025-10-02 03:20:00 | GOES-19 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 88.1 |
| 81b12633-84b7-33d7-93d6-d727a4e48b5f | -5.338 | -43.7623 | 2025-10-02 03:20:00 | GOES-19 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 171.4 |
| 3c939a7b-cd55-3e72-8f2e-ee9f100fbe1a | -11.5869 | -50.1612 | 2025-10-02 03:20:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 52.6 |
| 38ab20c8-50c4-32e9-b519-bc21df2ebedb | -15.3596 | -47.0724 | 2025-10-02 03:20:00 | GOES-19 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 64.7 |
| 7e31f04a-d001-37e3-89d5-6a330ca53d22 | -9.9559 | -43.7397 | 2025-10-02 03:20:00 | GOES-19 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 74.4 |
| 006dbc36-c24c-35a1-80b3-350473b4711d | -7.7563 | -42.541 | 2025-10-02 03:20:00 | GOES-19 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 108.5 |
| b655b603-01c4-3714-9770-a5a471bc1c2e | -10.9953 | -46.5869 | 2025-10-02 03:20:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 59.4 |
| 9d3a2621-bfd4-3647-8ce8-ec25683f3bd4 | -14.4255 | -46.115 | 2025-10-02 03:20:00 | GOES-19 | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 73.6 |
| 3fe2196c-2f43-3e6b-a300-ec4cd08a64dd | -14.426 | -46.0919 | 2025-10-02 03:20:00 | GOES-19 | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 70.0 |
| 8b80f7dc-47ac-32a3-ab8e-1a0d51621ce5 | -9.9365 | -43.7657 | 2025-10-02 03:20:00 | GOES-19 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 208.4 |
| 69ec2a82-2923-34e5-a236-0b066a15342f | -11.5866 | -50.1827 | 2025-10-02 03:20:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 57.5 |
| 85c5374b-6e95-3340-9ed3-e1aef22d3801 | -13.1743 | -47.8093 | 2025-10-02 03:20:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 84.9 |
| dee31471-fc39-37fa-815a-98485c69b0e7 | -7.7941 | -42.5369 | 2025-10-02 03:20:00 | GOES-19 | SOCORRO DO PIAUÍ | PIAUÍ | Brasil | 2210904 | 22 | 33 | nan | nan | nan | Caatinga | 73.7 |
| 1b94713e-f2b8-38b7-8294-6afae1aaa5f9 | -12.5001 | -50.2453 | 2025-10-02 03:20:00 | GOES-19 | SÃO MIGUEL DO ARAGUAIA | GOIÁS | Brasil | 5220207 | 52 | 33 | nan | nan | nan | Cerrado | 70.5 |
| 3d2b2efb-6384-35b0-bb6c-8aa6c809d9e7 | -7.7752 | -42.539 | 2025-10-02 03:20:00 | GOES-19 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 233.0 |
| 7d110faf-657d-3420-87d2-a0cd2edae2fb | -9.9369 | -43.7422 | 2025-10-02 03:20:00 | GOES-19 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 282.4 |
| c67bf45d-d3f8-34eb-88ce-bde19ae3d724 | -10.823 | -46.6538 | 2025-10-02 03:20:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 48.5 |
| ec5dd7a0-406f-328d-a611-ae566867f504 | -14.3114 | -45.9967 | 2025-10-02 03:20:00 | GOES-19 | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 59.2 |
| 9d81902a-73a6-368b-a710-e24d14265187 | -11.1746 | -47.2805 | 2025-10-02 03:20:00 | GOES-19 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 90.0 |
| 72fa4460-8575-3f58-9de0-e3cf3896d6dd | -9.9178 | -43.7447 | 2025-10-02 03:20:00 | GOES-19 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 127.9 |
| 161623dd-b20c-3516-950e-2e63a6a7d8b7 | -15.3591 | -47.0953 | 2025-10-02 03:20:00 | GOES-19 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 71.6 |
| dd901c79-3a22-3be7-8b7e-41bcea688d34 | -5.3379 | -43.7855 | 2025-10-02 03:20:00 | GOES-19 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 63.8 |
| e1385dbe-13b7-381b-926e-b15f4955ba21 | -9.9372 | -43.7187 | 2025-10-02 03:20:00 | GOES-19 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 182.6 |
| c6ec15ef-7ac8-3317-85e8-8d5528f8b75c | -11.175 | -47.2581 | 2025-10-02 03:20:00 | GOES-19 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 64.7 |
| 533524e8-1a14-3f18-a1a1-3a3809b60cbd | -7.7755 | -42.5152 | 2025-10-02 03:20:00 | GOES-19 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 89.6 |
| 4c5f2801-db70-3e70-9f8e-43b9617bd54e | -11.0144 | -46.5844 | 2025-10-02 03:20:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 58.9 |
| 40773a89-7408-3885-b092-ab277c968af7 | -13.959 | -48.1152 | 2025-10-02 03:20:00 | GOES-19 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 71.9 |
| 9a78148d-49de-3e74-8ff1-4bce9a2d2e1a | -7.7941 | -42.5369 | 2025-10-02 03:30:00 | GOES-19 | SOCORRO DO PIAUÍ | PIAUÍ | Brasil | 2210904 | 22 | 33 | nan | nan | nan | Caatinga | 72.7 |
| 4830b905-2178-32a8-9b89-9dc373740cbb | -16.0025 | -50.902 | 2025-10-02 03:30:00 | GOES-19 | JUSSARA | GOIÁS | Brasil | 5212204 | 52 | 33 | nan | nan | nan | Cerrado | 44.2 |
| 2f944e58-d43c-3139-a7c6-9008608e7166 | -16.023 | -50.8553 | 2025-10-02 03:30:00 | GOES-19 | FAZENDA NOVA | GOIÁS | Brasil | 5207600 | 52 | 33 | nan | nan | nan | Cerrado | 35.4 |
| a0fa36e8-c863-3d66-a8a6-cc98e4534683 | -6.7213 | -44.1387 | 2025-10-02 03:30:00 | GOES-19 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 65.2 |
| 1603c679-baf6-3703-96cb-903f98bdabfa | -11.1746 | -47.2805 | 2025-10-02 03:30:00 | GOES-19 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 87.0 |
| 6b28aebc-1756-3866-a215-0099aec9a288 | -14.3114 | -45.9967 | 2025-10-02 03:30:00 | GOES-19 | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 65.3 |
| 6176ac3b-63ba-3fc0-9a0f-73f2e748f775 | -13.4248 | -47.7945 | 2025-10-02 03:30:00 | GOES-19 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 60.8 |
| f2ff60b6-3597-3e17-b7f3-ff690a95ed16 | -13.1743 | -47.8093 | 2025-10-02 03:30:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 90.8 |
| bad0d4f6-5d4a-39bb-9ba5-4b492f94ca99 | -10.8237 | -46.6088 | 2025-10-02 03:30:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 169.0 |
| 66ec362d-c92d-3af4-be06-d7d1b0149793 | -10.9953 | -46.5869 | 2025-10-02 03:30:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 82.9 |
| 5f6e779f-ab21-3a9a-bd4e-2a7fa41cb1cb | -9.9178 | -43.7447 | 2025-10-02 03:30:00 | GOES-19 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 138.0 |
| bee7500e-aa23-366d-a457-3c8fb4252b4f | -7.7563 | -42.541 | 2025-10-02 03:30:00 | GOES-19 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 91.2 |
| c6cf8c6f-e4ab-34c2-ab3a-b9f609beda8b | -6.6955 | -48.7062 | 2025-10-02 03:30:00 | GOES-19 | ARAGOMINAS | TOCANTINS | Brasil | 1701309 | 17 | 33 | nan | nan | nan | Amazônia | 63.3 |
| 8ca029c4-a9ca-3cc7-a6e0-9cf993b5de2c | -10.2028 | -50.2895 | 2025-10-02 03:30:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 48.1 |
| f08df2e7-f726-3dbf-a65b-8eb2a30a2efc | -16.0426 | -50.8522 | 2025-10-02 03:30:00 | GOES-19 | FAZENDA NOVA | GOIÁS | Brasil | 5207600 | 52 | 33 | nan | nan | nan | Cerrado | 38.6 |
| fc943cb5-0f1a-3e04-bad5-01c38234b463 | -10.8234 | -46.6313 | 2025-10-02 03:30:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 226.2 |
| ed0e6742-a774-3061-97c1-e1691a36e0e2 | -9.9369 | -43.7422 | 2025-10-02 03:30:00 | GOES-19 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 257.6 |
| 6eadfa65-e6b6-34d2-ab6f-63d08ff49e1a | -9.9372 | -43.7187 | 2025-10-02 03:30:00 | GOES-19 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 167.5 |
| 1e393a50-3569-3ed7-9db8-2e3432cf8ca9 | -10.2031 | -50.2681 | 2025-10-02 03:30:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 60.3 |
| 4bd3abcd-bc2f-30f6-a849-1cf2abb28d21 | -10.8043 | -46.6337 | 2025-10-02 03:30:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 66.1 |
| aa2a56d3-5c19-38c9-a1b1-49f03a8bec8e | -15.3591 | -47.0953 | 2025-10-02 03:30:00 | GOES-19 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 64.9 |
| e694c662-ef09-3309-aefc-6f3765484f56 | -7.7749 | -42.5628 | 2025-10-02 03:30:00 | GOES-19 | SOCORRO DO PIAUÍ | PIAUÍ | Brasil | 2210904 | 22 | 33 | nan | nan | nan | Caatinga | 85.2 |


[Clique aqui para ver as próximas entradas](README17.md)
