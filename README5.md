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

## Dados Diários - Página 5

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 7fd23383-f923-3b8a-87ec-e907c8321c5e | -15.29057 | -53.20384 | 2025-05-03 04:53:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| cd3a2922-e840-355b-ade5-6dd2fc4004b2 | -19.95219 | -49.82252 | 2025-05-03 04:53:00 | NOAA-21 | RIOLÂNDIA | SÃO PAULO | Brasil | 3544202 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 8bfc5e81-70bd-36b9-871a-73745f26aa0a | -17.86894 | -44.56747 | 2025-05-03 04:53:00 | NOAA-21 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 27d33f82-4803-3c33-b481-310c6590d131 | -16.09108 | -57.44064 | 2025-05-03 04:53:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 3800b703-7264-31a5-a487-7524b7510b0b | -15.56984 | -47.85627 | 2025-05-03 04:53:00 | NOAA-21 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 940051df-5cc4-3613-bf55-1c0d2606d9c0 | -20.74154 | -56.0374 | 2025-05-03 04:55:00 | NOAA-21 | ANASTÁCIO | MATO GROSSO DO SUL | Brasil | 5000708 | 50 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 0dca2ff4-456d-3352-97de-2cd17d423bb5 | -23.79327 | -54.85336 | 2025-05-03 04:55:00 | NOAA-21 | TACURU | MATO GROSSO DO SUL | Brasil | 5007950 | 50 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| e52b9dac-6398-3ca6-b2f4-d45509ce2706 | -21.19723 | -44.93586 | 2025-05-03 04:55:00 | NOAA-21 | IJACI | MINAS GERAIS | Brasil | 3130408 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| baaa2818-a49d-3a0c-8a11-d23d98056a22 | -22.24653 | -52.97948 | 2025-05-03 04:55:00 | NOAA-21 | ANAURILÂNDIA | MATO GROSSO DO SUL | Brasil | 5000807 | 50 | 33 | nan | nan | nan | Mata Atlântica | 3.2 |
| 1448ccdc-12cc-3de4-a547-be89e5164e6c | -21.1508 | -48.60835 | 2025-05-03 04:55:00 | NOAA-21 | VISTA ALEGRE DO ALTO | SÃO PAULO | Brasil | 3556909 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 907a7c7e-bd07-3c53-805c-bc424e15b954 | -22.16619 | -52.29483 | 2025-05-03 04:55:00 | NOAA-21 | PRESIDENTE EPITÁCIO | SÃO PAULO | Brasil | 3541307 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.4 |
| eec80daf-76a4-37de-a0e5-96bb1bf4f0da | -20.27303 | -54.63981 | 2025-05-03 04:55:00 | NOAA-21 | CAMPO GRANDE | MATO GROSSO DO SUL | Brasil | 5002704 | 50 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 5bf9ab9c-32c8-3966-b110-26d6ab965ef3 | -20.72107 | -54.40989 | 2025-05-03 04:55:00 | NOAA-21 | CAMPO GRANDE | MATO GROSSO DO SUL | Brasil | 5002704 | 50 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 0dcef879-36fe-364b-8280-cf713e11c0f3 | -20.52955 | -55.71786 | 2025-05-03 04:55:00 | NOAA-21 | ANASTÁCIO | MATO GROSSO DO SUL | Brasil | 5000708 | 50 | 33 | nan | nan | nan | Cerrado | 0.6 |
| a990d750-a85c-37ca-87fb-f6ae5aee3827 | -22.02514 | -55.82943 | 2025-05-03 04:55:00 | NOAA-21 | PONTA PORÃ | MATO GROSSO DO SUL | Brasil | 5006606 | 50 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 2296d6d2-c059-3314-9784-e73faa5924b7 | -22.02571 | -55.82572 | 2025-05-03 04:55:00 | NOAA-21 | PONTA PORÃ | MATO GROSSO DO SUL | Brasil | 5006606 | 50 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 6137da40-4366-3629-bc4c-116bf369e9af | -25.08774 | -50.53024 | 2025-05-03 04:55:00 | NOAA-21 | IPIRANGA | PARANÁ | Brasil | 4110508 | 41 | 33 | nan | nan | nan | Mata Atlântica | 2.5 |
| 22080543-eaa7-3a6a-8516-b76626e0437a | -23.79044 | -54.8488 | 2025-05-03 04:55:00 | NOAA-21 | TACURU | MATO GROSSO DO SUL | Brasil | 5007950 | 50 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| ff973141-8580-3254-8616-3b56f395654b | -21.02975 | -55.64943 | 2025-05-03 04:55:00 | NOAA-21 | NIOAQUE | MATO GROSSO DO SUL | Brasil | 5005806 | 50 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 4688d43e-f152-321e-bbb2-13ac0f6c645d | -20.82046 | -55.52992 | 2025-05-03 04:55:00 | NOAA-21 | ANASTÁCIO | MATO GROSSO DO SUL | Brasil | 5000708 | 50 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 3375703f-2f14-35ed-9ae4-eb143e4ad87c | -21.98469 | -46.82032 | 2025-05-03 04:55:00 | NOAA-21 | SÃO JOÃO DA BOA VISTA | SÃO PAULO | Brasil | 3549102 | 35 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 9893f535-145a-35ec-b838-99d498d81bf5 | -24.24413 | -50.74127 | 2025-05-03 04:55:00 | NOAA-21 | ORTIGUEIRA | PARANÁ | Brasil | 4117305 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| 6ab8c838-f2b4-33e6-b779-e3ae39839c2c | -21.98436 | -46.82368 | 2025-05-03 04:55:00 | NOAA-21 | SÃO JOÃO DA BOA VISTA | SÃO PAULO | Brasil | 3549102 | 35 | 33 | nan | nan | nan | Cerrado | 1.2 |
| fb6ae042-049e-3f55-8891-513e09f771f3 | -20.74459 | -50.53779 | 2025-05-03 04:55:00 | NOAA-21 | AURIFLAMA | SÃO PAULO | Brasil | 3504206 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.4 |
| 4a89137d-6b92-34d8-be00-1d72b4159a26 | -21.14046 | -48.61737 | 2025-05-03 04:55:00 | NOAA-21 | PIRANGI | SÃO PAULO | Brasil | 3539004 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| 4c7e0f18-6849-3bb3-a8e6-6808df23d723 | -21.70191 | -55.4986 | 2025-05-03 04:55:00 | NOAA-21 | MARACAJU | MATO GROSSO DO SUL | Brasil | 5005400 | 50 | 33 | nan | nan | nan | Cerrado | 0.7 |
| d3c5faa1-8898-32ac-ab34-4d892823d2c2 | -20.62379 | -55.03761 | 2025-05-03 04:55:00 | NOAA-21 | TERENOS | MATO GROSSO DO SUL | Brasil | 5008008 | 50 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 270717dc-45fa-3d3d-8bc8-ebbb648e616b | -21.89259 | -56.26707 | 2025-05-03 04:55:00 | NOAA-21 | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 76796e1f-c2fa-3ed1-90d9-10695cd9f418 | -19.84917 | -54.72668 | 2025-05-03 04:55:00 | NOAA-21 | ROCHEDO | MATO GROSSO DO SUL | Brasil | 5007505 | 50 | 33 | nan | nan | nan | Cerrado | 0.8 |
| cdd1713c-46b2-38d3-be69-e6ef8da8712a | -21.03032 | -55.64574 | 2025-05-03 04:55:00 | NOAA-21 | NIOAQUE | MATO GROSSO DO SUL | Brasil | 5005806 | 50 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 36959e00-2970-3f02-9ef1-028defbd2d5d | -21.15022 | -48.61355 | 2025-05-03 04:55:00 | NOAA-21 | VISTA ALEGRE DO ALTO | SÃO PAULO | Brasil | 3556909 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 54db3aa8-1f19-3271-b280-2819923b43eb | -24.35088 | -51.5799 | 2025-05-03 04:55:00 | NOAA-21 | ARIRANHA DO IVAÍ | PARANÁ | Brasil | 4101853 | 41 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 8c372452-d77a-378f-8cde-a26eea2bb513 | -23.33798 | -46.77134 | 2025-05-03 04:55:00 | NOAA-21 | CAIEIRAS | SÃO PAULO | Brasil | 3509007 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 065dbef7-b292-375b-81d8-4bd9712d197d | -20.81702 | -55.52995 | 2025-05-03 04:55:00 | NOAA-21 | ANASTÁCIO | MATO GROSSO DO SUL | Brasil | 5000708 | 50 | 33 | nan | nan | nan | Cerrado | 2.1 |
| e90b126d-3980-3965-b5d4-3b6754b67803 | -23.78705 | -54.84822 | 2025-05-03 04:55:00 | NOAA-21 | TACURU | MATO GROSSO DO SUL | Brasil | 5007950 | 50 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| d19b9364-0534-3140-80d5-0f9a988618d9 | -21.05045 | -55.9974 | 2025-05-03 04:55:00 | NOAA-21 | NIOAQUE | MATO GROSSO DO SUL | Brasil | 5005806 | 50 | 33 | nan | nan | nan | Cerrado | 0.9 |
| eaf2e198-5fff-3d65-abb4-179d83523fe6 | -30.80078 | -52.88941 | 2025-05-03 04:57:00 | NOAA-21 | ENCRUZILHADA DO SUL | RIO GRANDE DO SUL | Brasil | 4306908 | 43 | 33 | nan | nan | nan | Pampa | 1.8 |
| d43ee646-1b44-3f7e-8d97-c303fe41e4a4 | -30.79972 | -52.88786 | 2025-05-03 04:57:00 | NOAA-21 | ENCRUZILHADA DO SUL | RIO GRANDE DO SUL | Brasil | 4306908 | 43 | 33 | nan | nan | nan | Pampa | 1.3 |
| 72f36adb-f06a-37eb-92a3-60b9f9eac139 | -6.7053 | -42.1234 | 2025-05-03 05:10:00 | GOES-19 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 58.8 |
| 3aafd99a-c95c-3fff-aff4-74551e2eee42 | -5.1684 | -45.10883 | 2025-05-03 05:16:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 2fd7ea43-4155-3480-b584-a7862ecc8f73 | -5.16933 | -45.10217 | 2025-05-03 05:16:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| e6768a19-df0c-3e32-b636-c21acdf20e39 | -5.16514 | -45.10833 | 2025-05-03 05:16:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| b938c07b-55cc-3559-913b-07136130fea7 | -6.7053 | -42.1234 | 2025-05-03 05:20:00 | GOES-19 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 61.8 |
| 6a6a9a89-e5af-390e-95b1-cfd19f68220b | -17.62396 | -50.91465 | 2025-05-03 05:21:00 | NPP-375D | RIO VERDE | GOIÁS | Brasil | 5218805 | 52 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 321fe604-f035-3873-b3e3-6158e2e68dc5 | -13.04276 | -53.72738 | 2025-05-03 05:21:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 3b436eee-18eb-385b-babb-a3d23b8b09f2 | -12.68384 | -58.09315 | 2025-05-03 05:21:00 | NPP-375D | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 49d34c61-250a-36f2-a9b3-f5d677596455 | -12.35255 | -54.51569 | 2025-05-03 05:21:00 | NPP-375D | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a2c147ee-280d-3abe-bc80-a2c190263fb4 | -16.31182 | -53.82349 | 2025-05-03 05:21:00 | NPP-375D | GUIRATINGA | MATO GROSSO | Brasil | 5104203 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 5a66df38-8ec7-3ccd-ad7b-738344199df6 | -18.25606 | -53.01433 | 2025-05-03 05:21:00 | NPP-375D | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 1a4e85c5-f488-366b-943d-ccd2d5fad25c | -11.3937 | -52.94357 | 2025-05-03 05:21:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 1ffdbce3-f0d5-33d8-8e25-0fd806c6aa1e | -12.66332 | -58.10723 | 2025-05-03 05:21:00 | NPP-375D | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 3.9 |
| c3e35aa7-4a7e-34ec-a7ec-efcf836be94e | -17.62353 | -50.91882 | 2025-05-03 05:21:00 | NPP-375D | RIO VERDE | GOIÁS | Brasil | 5218805 | 52 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 561432ff-06f6-31c5-bbfb-8392c7759f94 | -12.68035 | -58.09264 | 2025-05-03 05:21:00 | NPP-375D | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 0.6 |
| b8f21482-0bbf-33ff-88cf-3c448feb4e2d | -12.6645 | -58.09942 | 2025-05-03 05:21:00 | NPP-375D | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 7a30ac68-4f05-3107-8295-7425faff1a79 | -12.55696 | -57.70864 | 2025-05-03 05:21:00 | NPP-375D | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 95abe4fb-924a-3866-9254-624424af885e | -14.63257 | -57.46289 | 2025-05-03 05:21:00 | NPP-375D | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| fb4dd78a-b228-3d60-ac9a-8c6a19a1bebc | -12.66391 | -58.10332 | 2025-05-03 05:21:00 | NPP-375D | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 644af4e6-8f92-3156-be78-2a5a87f3cbee | -11.39837 | -52.94421 | 2025-05-03 05:21:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| c553c437-d1fe-39d5-a476-464887b13cd6 | -13.04916 | -53.714 | 2025-05-03 05:21:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 9b3f96bb-0876-33c9-b865-b4b8c4edd5b2 | -13.04978 | -53.7093 | 2025-05-03 05:21:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 31a63fa8-b676-3918-b139-06271ce70695 | -18.25641 | -53.01125 | 2025-05-03 05:21:00 | NPP-375D | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 83951b93-299b-37c5-9ee2-d43302b2e0e3 | -11.39305 | -52.94851 | 2025-05-03 05:21:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 3.5 |
| e6140a96-17f2-30c6-8b59-62d56e8283f6 | -22.16502 | -52.2916 | 2025-05-03 05:23:00 | NPP-375D | PRESIDENTE EPITÁCIO | SÃO PAULO | Brasil | 3541307 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 1d8babdc-397c-3602-8538-d6052d4972a2 | -20.82085 | -55.53294 | 2025-05-03 05:23:00 | NPP-375D | ANASTÁCIO | MATO GROSSO DO SUL | Brasil | 5000708 | 50 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 34806aeb-14bb-3b08-9f8a-2c4904bb99e8 | -22.0254 | -55.82215 | 2025-05-03 05:23:00 | NPP-375D | PONTA PORÃ | MATO GROSSO DO SUL | Brasil | 5006606 | 50 | 33 | nan | nan | nan | Cerrado | 0.4 |
| f03fb819-8d18-3976-8c84-fc04a03f84e6 | -25.08611 | -50.52916 | 2025-05-03 05:23:00 | NPP-375D | IPIRANGA | PARANÁ | Brasil | 4110508 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| ae34471e-eef7-3c4b-a07e-31ae051282d3 | -20.74614 | -50.53693 | 2025-05-03 05:23:00 | NPP-375D | AURIFLAMA | SÃO PAULO | Brasil | 3504206 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| a9732c33-d816-3ac2-990b-28a75bae35ed | -20.81638 | -55.53226 | 2025-05-03 05:23:00 | NPP-375D | ANASTÁCIO | MATO GROSSO DO SUL | Brasil | 5000708 | 50 | 33 | nan | nan | nan | Cerrado | 2.7 |
| a752ba35-0026-32ca-8fe8-46d17e7e17df | -22.02487 | -55.82687 | 2025-05-03 05:23:00 | NPP-375D | PONTA PORÃ | MATO GROSSO DO SUL | Brasil | 5006606 | 50 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 20a61328-11de-3b94-993a-43acf9da9e39 | -20.73835 | -56.03653 | 2025-05-03 05:23:00 | NPP-375D | ANASTÁCIO | MATO GROSSO DO SUL | Brasil | 5000708 | 50 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 4615afab-e04a-37e6-96c2-1c00397f0d1b | -22.2448 | -52.98008 | 2025-05-03 05:23:00 | NPP-375D | ANAURILÂNDIA | MATO GROSSO DO SUL | Brasil | 5000807 | 50 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 6682057a-752c-383c-937d-e00142079f89 | -21.02981 | -55.64575 | 2025-05-03 05:23:00 | NPP-375D | NIOAQUE | MATO GROSSO DO SUL | Brasil | 5005806 | 50 | 33 | nan | nan | nan | Cerrado | 2.0 |
| dc05b022-19a9-33be-ba32-87ab76895ef0 | -20.62366 | -55.03846 | 2025-05-03 05:23:00 | NPP-375D | TERENOS | MATO GROSSO DO SUL | Brasil | 5008008 | 50 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 4005e7d4-7fe5-31ef-9a41-cbd05dae28d4 | -21.02926 | -55.65032 | 2025-05-03 05:23:00 | NPP-375D | NIOAQUE | MATO GROSSO DO SUL | Brasil | 5005806 | 50 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 3de21034-94e7-3473-9990-4cf024ccc0fd | -20.73999 | -50.53626 | 2025-05-03 05:23:00 | NPP-375D | AURIFLAMA | SÃO PAULO | Brasil | 3504206 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 65112007-d0b0-3655-b493-f18123bbd77d | -20.72286 | -54.41178 | 2025-05-03 05:23:00 | NPP-375D | CAMPO GRANDE | MATO GROSSO DO SUL | Brasil | 5002704 | 50 | 33 | nan | nan | nan | Cerrado | 0.8 |
| c858a1d2-c2b8-3d8c-b612-99ff91a3a319 | -22.16464 | -52.29575 | 2025-05-03 05:23:00 | NPP-375D | PRESIDENTE EPITÁCIO | SÃO PAULO | Brasil | 3541307 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| a9ee45f9-66f0-35c6-9da8-8e9e7f102e8b | -20.71803 | -54.41127 | 2025-05-03 05:23:00 | NPP-375D | CAMPO GRANDE | MATO GROSSO DO SUL | Brasil | 5002704 | 50 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 24fc6114-038a-35e7-b461-4f54a9ff9635 | -12.6661 | -58.10221 | 2025-05-03 05:42:00 | NOAA-20 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 57830bac-6327-3c46-ab4f-0413fbb556f6 | -13.04938 | -53.71133 | 2025-05-03 05:42:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 0f69ff56-025b-3d3d-9273-1474d0e82ec7 | -12.66571 | -58.10522 | 2025-05-03 05:42:00 | NOAA-20 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| fa28f410-bc0d-3533-9ebd-7ecb4473a44b | -12.66533 | -58.10824 | 2025-05-03 05:42:00 | NOAA-20 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 80d50856-a3fd-37d1-a3e8-a09f653504c9 | -13.0487 | -53.71757 | 2025-05-03 05:42:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 697d524e-48e0-3016-8167-4661431fe91d | -21.03104 | -55.65173 | 2025-05-03 05:44:00 | NOAA-20 | NIOAQUE | MATO GROSSO DO SUL | Brasil | 5005806 | 50 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 35afc7bc-b1f7-3160-9400-778c4dabc754 | -21.03151 | -55.64603 | 2025-05-03 05:44:00 | NOAA-20 | NIOAQUE | MATO GROSSO DO SUL | Brasil | 5005806 | 50 | 33 | nan | nan | nan | Cerrado | 1.7 |
| d64e6007-8b02-35c8-b055-fcb70016ca0d | -7.67291 | -42.98711 | 2025-05-03 05:50:00 | AQUA_M-M | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 31.3 |
| 5fe43d8c-97e3-32c6-a48c-ba1d841436f1 | -6.70347 | -42.13117 | 2025-05-03 05:50:00 | AQUA_M-M | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 18.2 |
| f6e1163b-35bf-3b0c-b8d1-053152e48618 | -7.68798 | -42.97012 | 2025-05-03 05:50:00 | AQUA_M-M | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | 11.5 |
| feaa76b6-b85e-3000-987b-26ec39c1874c | -6.69025 | -42.12944 | 2025-05-03 05:50:00 | AQUA_M-M | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 53.4 |
| 1416f8e4-27e2-3b61-864d-9da371ae37c5 | -7.68542 | -42.98892 | 2025-05-03 05:50:00 | AQUA_M-M | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 24.3 |
| 0556c1a7-f2cb-3359-92da-0c8171841d5f | -6.69336 | -42.10656 | 2025-05-03 05:50:00 | AQUA_M-M | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 18.4 |
| 9f06f79b-a85c-3a53-a9ae-5b3822f3123f | -20.81675 | -55.52572 | 2025-05-03 05:55:00 | AQUA_M-M | ANASTÁCIO | MATO GROSSO DO SUL | Brasil | 5000708 | 50 | 33 | nan | nan | nan | Cerrado | 7.0 |
| dcabfd05-9462-33cf-a4fa-0b4c1dc495e0 | -19.95127 | -49.81964 | 2025-05-03 05:55:00 | AQUA_M-M | RIOLÂNDIA | SÃO PAULO | Brasil | 3544202 | 35 | 33 | nan | nan | nan | Mata Atlântica | 8.2 |
| 2fdc88db-8f3b-379a-af8b-28633f8326cf | -20.15657 | -50.72764 | 2025-05-03 05:55:00 | AQUA_M-M | ASPÁSIA | SÃO PAULO | Brasil | 3503950 | 35 | 33 | nan | nan | nan | Mata Atlântica | 7.6 |
| 8ef9da53-e0ac-357f-9c1a-f083a9a72424 | -6.7053 | -42.1234 | 2025-05-03 06:10:00 | GOES-19 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 59.6 |
| db8a8e2d-c62e-3776-bfb1-e0ad68222461 | -2.65623 | -48.79573 | 2025-05-03 12:34:00 | TERRA_M-T | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 19.9 |
| 006397f5-9eb1-3235-a409-79772b6f9c29 | -5.78299 | -44.96556 | 2025-05-03 12:36:00 | TERRA_M-T | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 8.5 |
| 768c21c9-5147-30c1-82a1-12409505f781 | -7.67853 | -42.97983 | 2025-05-03 12:36:00 | TERRA_M-T | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 11.1 |
| 98d6cb4d-084c-3afb-b51f-d2595a29d3f0 | -10.01499 | -46.59741 | 2025-05-03 12:36:00 | TERRA_M-T | SÃO FÉLIX DO TOCANTINS | TOCANTINS | Brasil | 1720150 | 17 | 33 | nan | nan | nan | Cerrado | 8.5 |
| 10088e99-9b0a-34ce-a196-73f67bfa478b | -8.94587 | -44.23211 | 2025-05-03 12:36:00 | TERRA_M-T | SANTA LUZ | PIAUÍ | Brasil | 2209302 | 22 | 33 | nan | nan | nan | Cerrado | 14.1 |


[Clique aqui para ver as próximas entradas](README6.md)
