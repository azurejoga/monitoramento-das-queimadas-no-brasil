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
| 24d1adb9-f9e8-3e4b-94ba-334ac58bcabb | -12.52065 | -48.29408 | 2026-06-29 04:40:00 | NOAA-21 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 8.5 |
| 7031fa4f-fa36-3085-a895-06e565b1b185 | -9.1474 | -50.91137 | 2026-06-29 04:40:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 9eaeffe6-db4d-38bd-9fd8-a24b3b204524 | -12.51686 | -48.30607 | 2026-06-29 04:40:00 | NOAA-21 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 03badff6-bf55-3688-8b0a-bf418c8aa234 | -10.32909 | -50.17073 | 2026-06-29 04:40:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 7015fe4f-47c6-3d64-967f-535122a81a65 | -9.9603 | -52.20047 | 2026-06-29 04:40:00 | NOAA-21 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 44f87bc3-bad7-3db8-b573-d7ae621d58d2 | -11.22062 | -54.30871 | 2026-06-29 04:40:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 56f083aa-6443-3af4-8409-cd9b9a7d7d46 | -10.46647 | -46.58178 | 2026-06-29 04:40:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 8162c56e-5d4e-39bc-b0cb-6c7861d87e06 | -10.84346 | -49.12759 | 2026-06-29 04:40:00 | NOAA-21 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 0aa76a1e-5cf5-38af-b8a7-a067bd96a8f4 | -7.28174 | -49.68054 | 2026-06-29 04:40:00 | NOAA-21 | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| c0f075bd-c48a-3e9d-914a-3f9a57f00326 | -9.69173 | -47.69379 | 2026-06-29 04:40:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 52bb8869-b33c-325c-896e-2af1b7ddc7f3 | -11.52782 | -54.79219 | 2026-06-29 04:40:00 | NOAA-21 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 15502cc6-468a-3899-ab5a-37c705a306a6 | -11.64575 | -48.53098 | 2026-06-29 04:40:00 | NOAA-21 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 059877cd-a445-3bff-936d-6665ac952fc5 | -11.15398 | -49.18654 | 2026-06-29 04:40:00 | NOAA-21 | CRIXÁS DO TOCANTINS | TOCANTINS | Brasil | 1706258 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 13944770-822e-3425-9189-33de035a88b1 | -9.22359 | -46.64184 | 2026-06-29 04:40:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 8be844b8-3faa-3d25-a89e-116aabc4fa3c | -6.86982 | -47.48502 | 2026-06-29 04:40:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 20c56e80-4b4e-3275-b39c-0bc8272bf389 | -10.72598 | -50.24504 | 2026-06-29 04:40:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| cdd1ce1b-d71b-3f9c-823a-7b12601e7527 | -11.22167 | -53.83088 | 2026-06-29 04:40:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| d33e0434-5800-3c68-ad53-93f5f72269b1 | -11.52319 | -54.79628 | 2026-06-29 04:40:00 | NOAA-21 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| dd7e868e-c24c-3df4-884a-4d8201f17b01 | -11.48639 | -47.41634 | 2026-06-29 04:40:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| be58823b-061d-31fa-8ea8-7fab353e0328 | -11.88636 | -57.11099 | 2026-06-29 04:40:00 | NOAA-21 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| fedf2521-fb68-3e13-8690-76001232cc8f | -11.49293 | -47.42175 | 2026-06-29 04:40:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 3b39dc62-baaf-3bae-beae-186061005ec4 | -13.56032 | -47.84555 | 2026-06-29 04:40:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 57f09e62-718d-3117-b826-454cefae7b59 | -11.89926 | -57.14039 | 2026-06-29 04:40:00 | NOAA-21 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| ab0aa982-69c6-34ea-83e4-0b221c013d83 | -13.86057 | -44.75379 | 2026-06-29 04:40:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 4.9 |
| aed866f8-b62c-39e5-bddd-0ce2875aa187 | -9.59216 | -56.92614 | 2026-06-29 04:40:00 | NOAA-21 | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| c9b2123f-f09b-3335-a1e6-711b4eb5134f | -7.91892 | -48.24443 | 2026-06-29 04:40:00 | NOAA-21 | PALMEIRANTE | TOCANTINS | Brasil | 1715705 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 259dd5e6-9d77-30ce-ade8-ac1f88c36243 | -11.21804 | -53.83024 | 2026-06-29 04:40:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 6.6 |
| 4f620623-7bbd-3ec4-acdb-0885c1c9914b | -13.5681 | -47.84227 | 2026-06-29 04:40:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 6790b9d3-12f9-3ce1-82fc-5199acc80698 | -11.52019 | -54.79083 | 2026-06-29 04:40:00 | NOAA-21 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 60a08b36-d2b5-3026-b505-b515711bbadf | -10.33623 | -50.16829 | 2026-06-29 04:40:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 27378c1a-fa1b-3d05-a6a3-9d69ce6ed091 | -7.30368 | -46.29016 | 2026-06-29 04:40:00 | NOAA-21 | NOVA COLINAS | MARANHÃO | Brasil | 2107258 | 21 | 33 | nan | nan | nan | Cerrado | 5.0 |
| b4c0a86f-30da-3793-970a-a25f443d9db6 | -7.74845 | -44.18312 | 2026-06-29 04:40:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 7f3663ea-244b-32ef-b41e-a9f364802f64 | -9.32137 | -58.02026 | 2026-06-29 04:40:00 | NOAA-21 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 0a101386-a2de-3b43-bfaf-e352f840061e | -10.30307 | -57.12947 | 2026-06-29 04:40:00 | NOAA-21 | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 8.1 |
| 9ba340a6-c988-3cd2-a56e-114373368849 | -7.55652 | -43.7699 | 2026-06-29 04:40:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 99c6b229-ee82-3633-b366-f435bef4a3ca | -13.5639 | -47.84609 | 2026-06-29 04:40:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| eaf951a4-c6d7-32d1-b814-0685d943f044 | -13.42643 | -47.85397 | 2026-06-29 04:40:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 019b694c-7c34-3ba2-94d2-773e2f746534 | -11.21295 | -53.81619 | 2026-06-29 04:40:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 2ccf402b-8ba6-3a7e-8a21-19501d60a986 | -7.7443 | -44.18267 | 2026-06-29 04:40:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 29ef792a-f075-3b70-a06f-3fb30fd54051 | -11.21367 | -53.83393 | 2026-06-29 04:40:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 6.5 |
| 39cd0422-9cd0-346c-8425-014a0721ea48 | -12.52122 | -48.29014 | 2026-06-29 04:40:00 | NOAA-21 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 7.9 |
| 875746fc-7717-3c5c-b9e8-44e96074e84b | -9.95688 | -52.19991 | 2026-06-29 04:40:00 | NOAA-21 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 6d73699e-3ca5-3152-9a9d-4a47eccaeec8 | -10.53082 | -48.15701 | 2026-06-29 04:40:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 83aa9904-0abd-3699-8e88-a9c75e15c496 | -11.2195 | -53.82166 | 2026-06-29 04:40:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 3.8 |
| c427960f-e1ca-3a72-a097-d5f118fb703d | -9.32626 | -58.02115 | 2026-06-29 04:40:00 | NOAA-21 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 5dd79520-90b2-3097-9bed-276a2c314b8b | -11.88478 | -57.11972 | 2026-06-29 04:40:00 | NOAA-21 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 46ba1948-9d8f-3857-a363-e6b050d14420 | -9.14516 | -50.92551 | 2026-06-29 04:40:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| d66c8613-a397-3557-a3e6-b5ab3b7d9b27 | -9.14685 | -50.91488 | 2026-06-29 04:40:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 81ac7b7c-e6cd-366b-a556-4dc2725d7147 | -12.2303 | -56.55307 | 2026-06-29 04:40:00 | NOAA-21 | ITANHANGÁ | MATO GROSSO | Brasil | 5104542 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 20563dd3-66b5-322b-9fe5-507813dfe223 | -11.48878 | -47.42514 | 2026-06-29 04:40:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| e2a0770c-ae36-3118-a695-b85332025f86 | -11.15623 | -49.19425 | 2026-06-29 04:40:00 | NOAA-21 | CRIXÁS DO TOCANTINS | TOCANTINS | Brasil | 1706258 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 07300f82-adcc-3080-82f2-fce2a3cf28d9 | -10.98122 | -49.56024 | 2026-06-29 04:40:00 | NOAA-21 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 95ecf070-fc9b-3e4c-8df0-03aade73501e | -12.23382 | -56.55776 | 2026-06-29 04:40:00 | NOAA-21 | ITANHANGÁ | MATO GROSSO | Brasil | 5104542 | 51 | 33 | nan | nan | nan | Amazônia | 4.9 |
| c60497c2-88e0-333a-a563-dd74d7709b5b | -11.89846 | -57.14485 | 2026-06-29 04:40:00 | NOAA-21 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 440a24ba-19b5-357b-bc0c-df8eccb55ea1 | -12.51838 | -48.30976 | 2026-06-29 04:40:00 | NOAA-21 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 770e03d7-e488-3a2d-ac96-80b065199784 | -10.32032 | -50.18361 | 2026-06-29 04:40:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 12.5 |
| 6ee66384-94e5-3b22-bba2-4137a551ef37 | -10.82955 | -49.12906 | 2026-06-29 04:40:00 | NOAA-21 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| d6c01a4c-7320-3caf-a90a-7626529ec63f | -10.33953 | -50.16882 | 2026-06-29 04:40:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 43a1d36c-4a44-3b90-bc5f-6a7afbbb7b59 | -9.16004 | -46.82563 | 2026-06-29 04:40:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 3e4d1cf0-ef79-3c8b-b0d0-d5e10deba33e | -10.328 | -50.17769 | 2026-06-29 04:40:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 10.1 |
| c4e191f4-ba6a-34c3-a501-63aa5b53aef1 | -11.91043 | -57.12883 | 2026-06-29 04:40:00 | NOAA-21 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 1d6fe930-408f-33e1-ae04-5f264fed8751 | -9.32915 | -58.03311 | 2026-06-29 04:40:00 | NOAA-21 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| b804cbe6-7bec-3fa1-b6f0-600a05c8c3bf | -12.5192 | -48.29038 | 2026-06-29 04:40:00 | NOAA-21 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| cd542ee2-64f0-3e32-80a5-a527d77b635f | -11.88195 | -57.11022 | 2026-06-29 04:40:00 | NOAA-21 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 63f38729-4eba-3793-b0f3-70c81f4defae | -11.3182 | -51.38806 | 2026-06-29 04:40:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 95be5cec-6fb1-3a55-bbfb-4ff9466a2ac0 | -11.2113 | -53.82183 | 2026-06-29 04:40:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 743a5017-2b36-3103-8d56-485ac7f53817 | -12.51628 | -48.30997 | 2026-06-29 04:40:00 | NOAA-21 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| d475eac1-3823-3cb4-8e72-269995010c5e | -6.88126 | -43.65418 | 2026-06-29 04:40:00 | NOAA-21 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 81598609-bcc5-3751-a954-1a3e13393bc9 | -11.88243 | -57.13278 | 2026-06-29 04:40:00 | NOAA-21 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 8663356a-f15f-370d-bc95-5d3ed07fb6ca | -10.39387 | -56.76231 | 2026-06-29 04:40:00 | NOAA-21 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 10.0 |
| 87a27a05-7b9c-311a-89a3-b6228b8f9aa7 | -10.30388 | -57.12486 | 2026-06-29 04:40:00 | NOAA-21 | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 8.1 |
| d356afe7-a0c9-308f-9cfd-b282d32f03cd | -10.83289 | -49.12959 | 2026-06-29 04:40:00 | NOAA-21 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 4aee025f-403d-3dff-9189-309b2f75a885 | -10.5156 | -51.93864 | 2026-06-29 04:40:00 | NOAA-21 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 7db8845b-b9a5-3ccd-8c3e-606eff54be3b | -11.88684 | -57.13357 | 2026-06-29 04:40:00 | NOAA-21 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 32f0a5f7-6afd-300a-a191-5781b0a266b3 | -13.56215 | -47.84312 | 2026-06-29 04:40:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 8cc22916-15da-3ed6-90c5-30c4677b02e5 | -11.90367 | -57.14122 | 2026-06-29 04:40:00 | NOAA-21 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 24dd055b-7a54-3cd7-9b00-2b9819aa99c0 | -9.31936 | -58.03136 | 2026-06-29 04:40:00 | NOAA-21 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 279ec921-94cc-3add-be99-caba3e6639ca | -10.98176 | -49.55671 | 2026-06-29 04:40:00 | NOAA-21 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 4.9 |
| e6557f9e-6bbc-3621-b594-dd8a40561a2d | -10.33569 | -50.17177 | 2026-06-29 04:40:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 7.3 |
| 1bc90490-82bf-343c-acb8-739d0562f654 | -10.29855 | -57.12864 | 2026-06-29 04:40:00 | NOAA-21 | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 8.1 |
| 78cf3498-c6d0-3526-962a-28a24ee4cb51 | -11.04758 | -55.75006 | 2026-06-29 04:40:00 | NOAA-21 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| eb25cd35-b5ba-3c0d-a4b6-783c11faf4d1 | -10.32471 | -50.17717 | 2026-06-29 04:40:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 10.1 |
| 7fac4ba7-e3f4-3641-82aa-0be4845a18a3 | -11.212 | -53.81755 | 2026-06-29 04:40:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 992dbc67-2118-3039-af83-5bed3b42e825 | -12.23452 | -56.55379 | 2026-06-29 04:40:00 | NOAA-21 | ITANHANGÁ | MATO GROSSO | Brasil | 5104542 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 99d36c95-0d6b-3c19-a1ed-979b5fb04333 | -10.32416 | -50.18065 | 2026-06-29 04:40:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 10.1 |
| 74ccb5cd-6fe6-3bac-b09a-29d7e6c5cc4c | -12.20273 | -52.87072 | 2026-06-29 04:40:00 | NOAA-21 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a6d9409a-6867-37a1-a06f-c5656f8ebf3e | -11.48047 | -47.43204 | 2026-06-29 04:40:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 4d1cda5d-58f3-396a-ae11-d388628a370b | -7.78618 | -48.17625 | 2026-06-29 04:40:00 | NOAA-21 | NOVA OLINDA | TOCANTINS | Brasil | 1714880 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 74cb9ca3-9a44-35ea-85f5-ffd2a4c1aa5f | -12.52413 | -48.2946 | 2026-06-29 04:40:00 | NOAA-21 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 5ea4cda4-fa5a-342c-9ac6-d41c3d3c2e72 | -13.85624 | -44.75314 | 2026-06-29 04:40:00 | NOAA-21 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 4.9 |
| a58c69f9-73aa-3563-89d9-86c38f697a0e | -9.95345 | -52.19933 | 2026-06-29 04:40:00 | NOAA-21 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 3e1b3198-2ba8-386f-bcc7-df74c4de4c0a | -10.47079 | -46.57802 | 2026-06-29 04:40:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| ae43e74f-7611-36b5-8f87-cd33bbb0dda8 | -13.71077 | -47.85916 | 2026-06-29 04:40:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 38fba59b-f02b-37ac-bfd7-ca31d3e4847d | -10.84292 | -49.13117 | 2026-06-29 04:40:00 | NOAA-21 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 4d161aef-6c43-36ae-a5a6-510b0c94e72d | -11.31853 | -54.46603 | 2026-06-29 04:40:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ce12bc3e-a14c-3ebf-865e-eeec24d36813 | -13.12618 | -48.60889 | 2026-06-29 04:40:00 | NOAA-21 | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | 0.4 |
| d7e2f76d-23a4-35f3-9942-64d7c3675fe1 | -11.32261 | -54.46923 | 2026-06-29 04:40:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| ca234c7b-d3b1-3838-b490-f8dd28709981 | -7.74899 | -44.17929 | 2026-06-29 04:40:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 2.9 |
| b451e1a0-7c4d-3177-90d0-0c69ed0b7522 | -11.31211 | -51.38343 | 2026-06-29 04:40:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 625458e3-0057-3e86-9bea-894926128af8 | -12.231 | -56.54912 | 2026-06-29 04:40:00 | NOAA-21 | ITANHANGÁ | MATO GROSSO | Brasil | 5104542 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |


[Clique aqui para ver as próximas entradas](README5.md)
