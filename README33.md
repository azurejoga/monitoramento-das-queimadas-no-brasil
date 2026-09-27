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

## Dados Diários - Página 33

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 476e5e37-dc5c-3ab8-a52b-7fbbd0552867 | -11.0542 | -54.19789 | 2026-09-27 04:53:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| fc762d64-6b3c-3499-b42e-3e7081928531 | -10.59269 | -48.71759 | 2026-09-27 04:53:00 | NOAA-21 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 47a2cf39-6794-3d08-ace5-aa2b1296e49a | -11.99261 | -57.60279 | 2026-09-27 04:53:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 07baa839-1c8e-316a-b581-0aceff22d457 | -9.93299 | -60.71991 | 2026-09-27 04:53:00 | NOAA-21 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 55843c61-26ca-3806-a91b-c35163592bb5 | -11.9441 | -50.505 | 2026-09-27 04:53:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| fd36b939-9061-3e9f-8eac-7e74059b2efc | -10.31199 | -54.26432 | 2026-09-27 04:53:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 13391687-e1bb-3230-bef4-5fd5313e3649 | -14.96038 | -47.5359 | 2026-09-27 04:53:00 | NOAA-21 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 2b1ea3a3-65e8-3454-88c5-d39e4f1c547a | -12.68083 | -47.31919 | 2026-09-27 04:53:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 6da96b5d-4d27-3ab6-b3cc-f98008bc98d4 | -13.53549 | -52.91445 | 2026-09-27 04:53:00 | NOAA-21 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 2e8f4315-cf56-35cc-a016-b768ced41c0f | -10.72136 | -53.99706 | 2026-09-27 04:53:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 270704f5-e375-3d0c-b370-c9a280daf063 | -12.18539 | -47.3824 | 2026-09-27 04:53:00 | NOAA-21 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| c554cafc-737e-3640-b01e-3f2ba54e4294 | -10.4223 | -53.77735 | 2026-09-27 04:53:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 99e62c20-a116-3b17-bec5-59a34892c20e | -12.28759 | -50.29346 | 2026-09-27 04:53:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 11.1 |
| 41f9a866-6044-3487-8acb-d79d76a3b628 | -10.80757 | -60.7185 | 2026-09-27 04:53:00 | NOAA-21 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b69d01d2-7fa2-3c13-9986-3d30348e55b5 | -10.42673 | -53.79235 | 2026-09-27 04:53:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 9f7cd5e3-7e9a-32d0-bbe8-df23ed0368e0 | -12.7127 | -47.3233 | 2026-09-27 04:53:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| f9a46d1a-47e5-3196-bd22-7fb20c968090 | -14.81854 | -49.27695 | 2026-09-27 04:53:00 | NOAA-21 | SÃO LUIZ DO NORTE | GOIÁS | Brasil | 5220157 | 52 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 5f1f33e1-dc0f-3d1f-a306-18a176241793 | -12.29634 | -50.28545 | 2026-09-27 04:53:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 0563d3a9-586d-30e2-a4d3-08274dce1486 | -11.96477 | -50.54401 | 2026-09-27 04:53:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 006f9d61-bd31-3682-8b72-b326e0cd70de | -11.9654 | -50.53963 | 2026-09-27 04:53:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 5.8 |
| d7800aed-a5c0-3a37-93e5-355513d82f8b | -12.21288 | -50.37755 | 2026-09-27 04:53:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| b2fdbe99-143f-30cb-8c30-3a926d93e927 | -14.59098 | -45.59616 | 2026-09-27 04:53:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 89f61b27-a51e-332e-b957-f7d04588c93f | -9.93314 | -60.71732 | 2026-09-27 04:53:00 | NOAA-21 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 77335831-e5d8-3ef0-8a7c-b8e35ef70e3b | -11.93847 | -50.54455 | 2026-09-27 04:53:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 7.3 |
| cd93c501-705d-321d-add1-139efff534bf | -12.13186 | -57.17471 | 2026-09-27 04:53:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 3a8f112a-f21a-3126-bcd1-ec1245fa83e4 | -11.89754 | -50.51598 | 2026-09-27 04:53:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 66f63171-b031-3183-93a0-aed3b1566622 | -11.96907 | -50.54017 | 2026-09-27 04:53:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 6e8ace09-d379-39e7-85d9-a52bcdb632a9 | -13.53886 | -52.91499 | 2026-09-27 04:53:00 | NOAA-21 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 74c93fb8-bd8d-3582-ae8e-98b8e2cb77e2 | -12.02752 | -50.62785 | 2026-09-27 04:53:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 6b0dbbc9-250e-3e45-a6ef-bef08cf42acf | -12.13712 | -50.33638 | 2026-09-27 04:53:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 18988c87-164a-3134-b7d7-bfd5c2bb3fd9 | -14.8048 | -45.96285 | 2026-09-27 04:53:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 9da78d36-ac49-3439-ba6a-8908bf7b2907 | -8.33977 | -62.85632 | 2026-09-27 04:53:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 14d84556-bd7f-375f-8618-ea119323bd2b | -11.77143 | -51.00443 | 2026-09-27 04:53:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 9f921a0d-6bdf-3737-a01f-7ee099b533fd | -10.82565 | -57.21291 | 2026-09-27 04:53:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 8739f87d-e65f-3a7a-8d83-3ae4d20f7e22 | -10.40916 | -53.81812 | 2026-09-27 04:53:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 23544e66-4978-3236-a6f1-123414451255 | -9.53688 | -62.26963 | 2026-09-27 04:53:00 | NOAA-21 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 1f51da37-000a-3282-a373-96f44dae5c79 | -11.87502 | -50.5192 | 2026-09-27 04:53:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 805a12ba-e926-300d-ad14-9a2e52436077 | -12.29892 | -50.26714 | 2026-09-27 04:53:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 7caac818-7322-323d-8ed4-04e838bf0658 | -11.89325 | -50.51982 | 2026-09-27 04:53:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| a6f5b7e8-41f7-3c3b-89b0-122a343f99c5 | -11.88794 | -50.50768 | 2026-09-27 04:53:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 3b97fab0-3076-3055-ad9e-60a2721e13ee | -12.65993 | -47.30144 | 2026-09-27 04:53:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 7.1 |
| ee8eb22c-bb3e-377b-8608-03fd91fb48a5 | -11.7726 | -51.02156 | 2026-09-27 04:53:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 2.7 |
| d2a2fd22-2be6-3b66-8495-88fd6787e9f0 | -11.27636 | -54.42818 | 2026-09-27 04:53:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 2d2dae0a-b2fa-3442-823a-6f108819f919 | -10.01849 | -50.14829 | 2026-09-27 04:53:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 1ee86726-6267-3fbd-a914-33ac8e210e15 | -10.31143 | -54.26785 | 2026-09-27 04:53:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 0ba5e9f9-eebd-39ee-b99e-1edea6c8df2f | -10.40971 | -53.81464 | 2026-09-27 04:53:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 6.1 |
| a67c6e3f-5010-3400-8d78-dafdc8fbdbdd | -11.57825 | -50.50298 | 2026-09-27 04:53:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 3819b8d9-d804-3c21-92b2-c35d7aa73888 | -11.98835 | -57.60553 | 2026-09-27 04:53:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| af1b2770-94e3-3b4f-9732-e5f2de23d97f | -13.33973 | -51.33094 | 2026-09-27 04:53:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| cf98c56f-e8ab-3256-b872-be8b0eeb88e9 | -14.68606 | -59.60877 | 2026-09-27 04:53:00 | NOAA-21 | NOVA LACERDA | MATO GROSSO | Brasil | 5106182 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 9cf3929f-f639-3817-b527-511b043e0ce9 | -14.40079 | -43.78174 | 2026-09-27 04:53:00 | NOAA-21 | MALHADA | BAHIA | Brasil | 2920205 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 8a1e0501-7642-36d8-8c85-d16bc9061b06 | -12.29325 | -50.28032 | 2026-09-27 04:53:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 8.4 |
| a804a33c-435d-32b8-91d4-eb6aea5236f0 | -11.77557 | -51.02624 | 2026-09-27 04:53:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| eb7b381b-0987-3ba8-85e3-8c51daea25f0 | -11.94571 | -50.57246 | 2026-09-27 04:53:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 59cd8ea3-7735-386a-b970-3fb40e97f77b | -10.81863 | -60.73475 | 2026-09-27 04:53:00 | NOAA-21 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 10.9 |
| b7a82d93-8d73-3af7-bff0-e44afd19f1f6 | -12.67671 | -45.04047 | 2026-09-27 04:53:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| a2c4ac71-b852-3fae-b5f2-47e442ec8347 | -10.31474 | -54.26837 | 2026-09-27 04:53:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 35a733f6-cb25-3b22-bedf-11f0b417497a | -10.02339 | -50.14016 | 2026-09-27 04:53:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 4.5 |
| de8a035c-cff9-329a-b948-eec28fe4150f | -11.94633 | -50.5681 | 2026-09-27 04:53:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 12.0 |
| 8f1e7da6-9ff1-383a-a3e6-94681ab13b1d | -11.28187 | -54.43627 | 2026-09-27 04:53:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 57150b65-ae0c-3075-bb5c-73d0676f27ef | -12.47278 | -47.47887 | 2026-09-27 04:53:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 0460d28b-96fc-3ea2-9298-9021b4a2bf1c | -11.99682 | -50.29415 | 2026-09-27 04:53:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 53d115eb-2472-32a9-8fc1-6cc736634822 | -11.975 | -50.57687 | 2026-09-27 04:53:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 3834db53-905f-3a0b-9d00-aa2d28bf05ea | -13.87996 | -49.03479 | 2026-09-27 04:53:00 | NOAA-21 | ESTRELA DO NORTE | GOIÁS | Brasil | 5207501 | 52 | 33 | nan | nan | nan | Cerrado | 9.5 |
| 582be91b-d4ab-34bd-8148-46ea93e8cc38 | -11.04123 | -51.32642 | 2026-09-27 04:53:00 | NOAA-21 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 288e9aba-990e-3963-99c7-8cbec05118ef | -13.37199 | -51.31017 | 2026-09-27 04:53:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 8349c4ca-7bba-315f-b569-790de016665d | -12.67234 | -47.31316 | 2026-09-27 04:53:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 727a0eb9-7fbc-3811-8aa7-ff5cb8cc0fd5 | -11.16193 | -62.86835 | 2026-09-27 04:53:00 | NOAA-21 | MIRANTE DA SERRA | RONDÔNIA | Brasil | 1101302 | 11 | 33 | nan | nan | nan | Amazônia | 0.5 |
| cd7314ee-d5f0-371f-ac59-708120071a92 | -12.66052 | -47.29669 | 2026-09-27 04:53:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 6148593e-4d62-3b28-a6a3-474ecd630417 | -12.05445 | -50.59625 | 2026-09-27 04:53:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 5.7 |
| d646bb3a-16f4-3f39-9b27-c095be3b6839 | -12.75733 | -52.82479 | 2026-09-27 04:53:00 | NOAA-21 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| fc9d8807-304f-3596-96c9-4fad16c22650 | -12.26454 | -50.69478 | 2026-09-27 04:53:00 | NOAA-21 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 6.2 |
| a51037ba-9f8d-3c12-a5b6-ccbaad0b8ec4 | -11.02329 | -54.04604 | 2026-09-27 04:53:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 22c2458d-52ae-3bc0-98fd-d15f0a97f93a | -12.66447 | -47.30212 | 2026-09-27 04:53:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 7.1 |
| cdb0312e-cc8e-3ab8-87c5-79022a7ca876 | -10.68101 | -57.63415 | 2026-09-27 04:53:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| e506e670-0af0-37cc-91a9-1fb0b1fdc640 | -10.11254 | -50.19644 | 2026-09-27 04:53:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 2b1cc073-7e1a-35a9-be6b-79a509a4c704 | -10.41025 | -53.81115 | 2026-09-27 04:53:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 4.6 |
| e196ed01-f058-33d6-8f6d-f7f16d61182b | -11.16254 | -62.86516 | 2026-09-27 04:53:00 | NOAA-21 | MIRANTE DA SERRA | RONDÔNIA | Brasil | 1101302 | 11 | 33 | nan | nan | nan | Amazônia | 0.5 |
| fbc81402-d9f9-32f9-a61d-c3c00dd8b56b | -12.28386 | -50.29291 | 2026-09-27 04:53:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 3b243bd1-13f3-3406-a425-e5fa28bcfd49 | -11.85542 | -50.52521 | 2026-09-27 04:53:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 1d260c68-3b06-3ac8-97ec-29e9c38df014 | -13.08986 | -47.41025 | 2026-09-27 04:53:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 5233fb55-129b-3ce8-8e37-4c962c682790 | -10.60902 | -53.99706 | 2026-09-27 04:53:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| eca0fd6f-e6a5-3db2-b3e9-913073da326f | -11.98395 | -57.60923 | 2026-09-27 04:53:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 85f90f91-2c14-3b3e-8d16-32faac41f398 | -10.79088 | -48.7285 | 2026-09-27 04:53:00 | NOAA-21 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 4.5 |
| dda821ed-9fd7-37b4-8191-3494682e52a3 | -14.7905 | -45.95137 | 2026-09-27 04:53:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 07711cb5-2eaf-3a1e-84ff-57c435fc125a | -11.27746 | -54.44276 | 2026-09-27 04:53:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 243cd049-c5ad-3406-990b-a7802a3ef760 | -10.45129 | -61.31049 | 2026-09-27 04:53:00 | NOAA-21 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 7ac7b165-1c9f-3d8f-8ba8-7aa412130434 | -10.88124 | -50.14962 | 2026-09-27 04:53:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 669e9e28-ff8c-38c0-b21a-0406359daf5f | -14.79527 | -45.95517 | 2026-09-27 04:53:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| b4ab6cef-49e4-3f00-8e09-81cba9dc2312 | -13.34048 | -46.79974 | 2026-09-27 04:53:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 0936eea5-a351-3231-83ca-8df9dd0df622 | -11.9847 | -57.60487 | 2026-09-27 04:53:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c2f6dad3-fef8-3f9d-a873-6753db3eff06 | -12.02268 | -50.60932 | 2026-09-27 04:53:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 7.8 |
| 7f8ba43e-ca47-3566-9899-d182f05c774b | -11.85112 | -50.52904 | 2026-09-27 04:53:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 6.2 |
| b79e96db-9e80-3aad-aa87-08cd6e0c30c0 | -11.02768 | -54.03958 | 2026-09-27 04:53:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 72336c4b-3109-3bb4-bbf8-6acd8916abd1 | -9.77726 | -54.28904 | 2026-09-27 04:53:00 | NOAA-21 | GUARANTÃ DO NORTE | MATO GROSSO | Brasil | 5104104 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d61bc9f6-9d8c-3480-8491-988773e63ac7 | -11.88427 | -50.50713 | 2026-09-27 04:53:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 6da1f262-2992-389d-ae97-b87918bcc50c | -12.76852 | -52.81904 | 2026-09-27 04:53:00 | NOAA-21 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e3acb7dd-a642-3948-be14-c1d94e796f2a | -13.37497 | -51.31489 | 2026-09-27 04:53:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 4.9 |
| c56d1bbf-43e8-3215-bd6e-00ab04ac9bb6 | -11.89401 | -50.51755 | 2026-09-27 04:53:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| e7221e7c-9c77-36f5-8cf7-26b2cec94eab | -13.37855 | -51.31544 | 2026-09-27 04:53:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |


[Clique aqui para ver as próximas entradas](README34.md)
