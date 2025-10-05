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
| fc2483f8-07f2-30d0-bb6b-4ef6571835ab | -10.23771 | -47.1472 | 2025-10-05 12:57:00 | TERRA_M-T | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 138.5 |
| f12f73ee-6061-30df-aeb9-06d7665011c2 | -10.04547 | -52.06595 | 2025-10-05 12:57:00 | TERRA_M-T | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 31.3 |
| b8145be0-b73b-3466-9b07-280137102c3a | -7.80276 | -48.03622 | 2025-10-05 12:57:00 | TERRA_M-T | PALMEIRANTE | TOCANTINS | Brasil | 1715705 | 17 | 33 | nan | nan | nan | Cerrado | 36.0 |
| 7486ea0d-aefc-3033-97e4-3dbe8e14e397 | -10.23798 | -47.13987 | 2025-10-05 12:57:00 | TERRA_M-T | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 161.8 |
| 6c1f23c9-9da3-34f2-8430-ee1aacc05b5b | -11.09785 | -49.86062 | 2025-10-05 12:57:00 | TERRA_M-T | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 29.4 |
| 02ea7297-43ce-306e-a96a-7c58a2a07098 | -11.08896 | -47.74913 | 2025-10-05 12:57:00 | TERRA_M-T | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 133.1 |
| 1bc0ddb0-b3ac-36ae-91e8-67c3cd93395b | -8.54747 | -47.67302 | 2025-10-05 12:57:00 | TERRA_M-T | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 60.4 |
| 8b250c6c-e840-39da-a892-2452f5de9102 | -8.61527 | -54.95844 | 2025-10-05 12:57:00 | TERRA_M-T | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 18.8 |
| 0623b509-83af-33df-8542-03097c653bea | -9.34104 | -54.52459 | 2025-10-05 12:57:00 | TERRA_M-T | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 27.0 |
| 8b9d52b6-8232-3aa2-813a-6b107be1e336 | -7.80632 | -48.06349 | 2025-10-05 12:57:00 | TERRA_M-T | PALMEIRANTE | TOCANTINS | Brasil | 1715705 | 17 | 33 | nan | nan | nan | Cerrado | 27.4 |
| 60b28e9c-a4bc-3fda-b2dd-c04652fc40ad | -10.06439 | -50.41276 | 2025-10-05 12:57:00 | TERRA_M-T | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 311.8 |
| 5f846d94-b3b0-3bab-8483-9612f63a3c9f | -9.28347 | -57.15126 | 2025-10-05 12:57:00 | TERRA_M-T | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 12.2 |
| b99f0145-a5d9-3937-aeee-ee4ac7381c57 | -9.1489 | -59.52959 | 2025-10-05 12:57:00 | TERRA_M-T | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 21.1 |
| 347ae6e2-84ca-31cf-b679-43950e3706db | -9.92702 | -50.90863 | 2025-10-05 12:57:00 | TERRA_M-T | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 26.0 |
| 3d74bf62-0769-30ff-bbd8-134c9f182323 | -10.03041 | -50.40202 | 2025-10-05 12:57:00 | TERRA_M-T | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 34.3 |
| af4a142f-b24d-3119-9a3a-fec7805f8669 | -9.14744 | -59.53949 | 2025-10-05 12:57:00 | TERRA_M-T | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 8.1 |
| 97bc9c90-a466-3a20-8fb7-45119466efd7 | -8.55266 | -47.68092 | 2025-10-05 12:57:00 | TERRA_M-T | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 66.7 |
| 82871824-405c-305a-92ae-1a2e4c16a575 | -10.055 | -50.42844 | 2025-10-05 12:57:00 | TERRA_M-T | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 123.7 |
| 2517f945-dce9-3b15-b95d-e745ad423e25 | -8.54304 | -47.70937 | 2025-10-05 12:57:00 | TERRA_M-T | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 27.4 |
| 14df724a-6bfd-35b5-8436-88c0f9d734c2 | -9.61866 | -51.82242 | 2025-10-05 12:57:00 | TERRA_M-T | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 19.3 |
| e6d53762-f29e-340a-a51e-b82037664901 | -8.62597 | -54.98695 | 2025-10-05 12:57:00 | TERRA_M-T | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 17.4 |
| de12af0a-b44f-3b05-9e92-0221847492b5 | -9.33118 | -54.52325 | 2025-10-05 12:57:00 | TERRA_M-T | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 27.9 |
| d2584b22-cb6a-394d-8aa1-9d3664503e49 | -10.06161 | -50.43605 | 2025-10-05 12:57:00 | TERRA_M-T | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 125.7 |
| a9aa7644-adea-31a5-850d-4883e91cc60a | -9.33055 | -54.51659 | 2025-10-05 12:57:00 | TERRA_M-T | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 27.4 |
| 51aaec99-1458-3fbc-8386-63e041ff559f | -9.56169 | -54.62353 | 2025-10-05 12:57:00 | TERRA_M-T | GUARANTÃ DO NORTE | MATO GROSSO | Brasil | 5104104 | 51 | 33 | nan | nan | nan | Amazônia | 11.4 |
| 740a2ac2-e7e2-3096-a211-4d79628727b0 | -10.05794 | -50.40517 | 2025-10-05 12:57:00 | TERRA_M-T | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 144.0 |
| 0c3b94bf-bebd-3051-8fb6-806fca3a72cc | -6.99902 | -47.46143 | 2025-10-05 12:57:00 | TERRA_M-T | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 47.2 |
| 864e7db2-2f12-3bc7-b6fd-2dace7548d9c | -15.64672 | -53.84171 | 2025-10-05 12:59:00 | TERRA_M-T | GENERAL CARNEIRO | MATO GROSSO | Brasil | 5103908 | 51 | 33 | nan | nan | nan | Cerrado | 28.9 |
| 187ce1d3-e3e2-3a40-9174-9d7da4de03f1 | -12.58677 | -54.75634 | 2025-10-05 12:59:00 | TERRA_M-T | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 58.6 |
| fbff1fd3-1327-3e91-9740-702e7f653f71 | -20.82694 | -54.76335 | 2025-10-05 12:59:00 | TERRA_M-T | SIDROLÂNDIA | MATO GROSSO DO SUL | Brasil | 5007901 | 50 | 33 | nan | nan | nan | Cerrado | 18.4 |
| 9fd3935b-e07a-3518-ba72-8c40a53c9a22 | -17.95911 | -57.53609 | 2025-10-05 12:59:00 | TERRA_M-T | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 69.5 |
| 9861300e-5716-3092-9b32-558b4d377a20 | -12.925 | -57.79059 | 2025-10-05 12:59:00 | TERRA_M-T | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 3086adb6-720a-38ab-b40b-237731b3b4fe | -17.95246 | -57.58612 | 2025-10-05 12:59:00 | TERRA_M-T | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 27.6 |
| 009d1226-8678-3d5f-9549-cb94de1ba5f8 | -17.97763 | -51.13061 | 2025-10-05 12:59:00 | TERRA_M-T | RIO VERDE | GOIÁS | Brasil | 5218805 | 52 | 33 | nan | nan | nan | Cerrado | 51.3 |
| 11c36e7c-862c-30b3-9e76-61f6ba312238 | -11.77823 | -58.33699 | 2025-10-05 12:59:00 | TERRA_M-T | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 7.5 |
| 670d9c83-2026-374d-8330-08ad274cd1bd | -18.18789 | -53.35792 | 2025-10-05 12:59:00 | TERRA_M-T | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 68.3 |
| bea26da5-27f1-3341-bace-2aa8e258973f | -17.94852 | -57.54498 | 2025-10-05 12:59:00 | TERRA_M-T | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 22.6 |
| efcc84ae-97c5-3950-8907-3b6d34ca41af | -14.74748 | -54.66196 | 2025-10-05 12:59:00 | TERRA_M-T | PLANALTO DA SERRA | MATO GROSSO | Brasil | 5106455 | 51 | 33 | nan | nan | nan | Cerrado | 18.4 |
| 40972e6e-3dab-3ffd-9a66-1362665fc24f | -21.46783 | -51.51711 | 2025-10-05 12:59:00 | TERRA_M-T | DRACENA | SÃO PAULO | Brasil | 3514403 | 35 | 33 | nan | nan | nan | Mata Atlântica | 60.5 |
| 82c655b2-d1ca-324f-bd5e-34a025fe5163 | -16.94626 | -52.68826 | 2025-10-05 12:59:00 | TERRA_M-T | DOVERLÂNDIA | GOIÁS | Brasil | 5207253 | 52 | 33 | nan | nan | nan | Cerrado | 20.6 |
| 92e0c860-babe-3a75-ad98-2923e20fd830 | -17.96694 | -57.54803 | 2025-10-05 12:59:00 | TERRA_M-T | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 6.1 |
| a72fa449-9492-3663-9526-5489cdc50047 | -14.98179 | -54.81738 | 2025-10-05 12:59:00 | TERRA_M-T | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 36.1 |
| fecfbdc3-32e5-32d2-af3e-03e6e20a75a1 | -19.7496 | -49.63606 | 2025-10-05 12:59:00 | TERRA_M-T | ITAPAGIPE | MINAS GERAIS | Brasil | 3133402 | 31 | 33 | nan | nan | nan | Mata Atlântica | 40.9 |
| 4456c10f-2443-3d97-ac75-196ff7b41b2b | -12.59693 | -54.75763 | 2025-10-05 12:59:00 | TERRA_M-T | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 22.5 |
| a5cbb786-b14a-3baf-9ba5-8553689b6297 | -12.16843 | -50.92034 | 2025-10-05 12:59:00 | TERRA_M-T | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 53.0 |
| 28f76e06-2b60-3861-ae15-68a5e9176380 | -16.0172 | -50.94984 | 2025-10-05 12:59:00 | TERRA_M-T | JUSSARA | GOIÁS | Brasil | 5212204 | 52 | 33 | nan | nan | nan | Cerrado | 36.2 |
| 73df5f38-ff45-315d-b628-0210a3285cac | -19.00885 | -50.58194 | 2025-10-05 12:59:00 | TERRA_M-T | SÃO SIMÃO | GOIÁS | Brasil | 5220405 | 52 | 33 | nan | nan | nan | Mata Atlântica | 56.7 |
| e5ef8581-71ad-303b-be72-f522175d3de5 | -15.5801 | -52.457 | 2025-10-05 12:59:00 | TERRA_M-T | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 33.2 |
| 28c10946-6f5f-3cc9-ad21-65df6a0723b7 | -15.97701 | -50.91504 | 2025-10-05 12:59:00 | TERRA_M-T | JUSSARA | GOIÁS | Brasil | 5212204 | 52 | 33 | nan | nan | nan | Cerrado | 39.3 |
| 270c9aa9-4a69-3907-b80b-72c30a76ccaf | -13.74232 | -51.31363 | 2025-10-05 12:59:00 | TERRA_M-T | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 392.5 |
| 59034977-717b-3702-8c89-e5fe5ab500be | -15.90703 | -48.83443 | 2025-10-05 12:59:00 | TERRA_M-T | CORUMBÁ DE GOIÁS | GOIÁS | Brasil | 5205802 | 52 | 33 | nan | nan | nan | Cerrado | 61.1 |
| a7676d12-ba6a-3512-a79c-948ca014b2a4 | -14.75798 | -54.66375 | 2025-10-05 12:59:00 | TERRA_M-T | PLANALTO DA SERRA | MATO GROSSO | Brasil | 5106455 | 51 | 33 | nan | nan | nan | Cerrado | 15.3 |
| 21e42609-604f-3db4-9722-aa84a26414f6 | -14.6236 | -52.51777 | 2025-10-05 12:59:00 | TERRA_M-T | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 30.5 |
| 1e7b51ec-4764-34a4-b3d0-716391382d19 | -19.02479 | -50.60906 | 2025-10-05 12:59:00 | TERRA_M-T | SÃO SIMÃO | GOIÁS | Brasil | 5220405 | 52 | 33 | nan | nan | nan | Mata Atlântica | 233.0 |
| ecf9b1e7-b3e0-3860-9c29-27285fb9693c | -15.83141 | -56.39505 | 2025-10-05 12:59:00 | TERRA_M-T | NOSSA SENHORA DO LIVRAMENTO | MATO GROSSO | Brasil | 5106109 | 51 | 33 | nan | nan | nan | Cerrado | 6.9 |
| b9d008ab-3b3d-3b31-aee8-c32bad1ebb82 | -13.73726 | -51.28315 | 2025-10-05 12:59:00 | TERRA_M-T | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 42.2 |
| d352621c-9de7-3f59-863e-2f05e83e8ce6 | -12.26295 | -49.21298 | 2025-10-05 12:59:00 | TERRA_M-T | FIGUEIRÓPOLIS | TOCANTINS | Brasil | 1707652 | 17 | 33 | nan | nan | nan | Cerrado | 52.2 |
| a063152f-19cc-3c27-af80-87a4e5fb4638 | -20.60503 | -51.39968 | 2025-10-05 12:59:00 | TERRA_M-T | ITAPURA | SÃO PAULO | Brasil | 3523008 | 35 | 33 | nan | nan | nan | Mata Atlântica | 35.1 |
| 4b56f4f9-ceb2-3db0-ab7c-e956c7720f65 | -13.3278 | -57.02342 | 2025-10-05 12:59:00 | TERRA_M-T | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 10.5 |
| d40eb95d-5db0-31bb-97aa-639a4c56e601 | -19.02792 | -50.57763 | 2025-10-05 12:59:00 | TERRA_M-T | SÃO SIMÃO | GOIÁS | Brasil | 5220405 | 52 | 33 | nan | nan | nan | Mata Atlântica | 51.1 |
| fb19dc2e-82d0-3e2f-b224-9fdc5a841cb2 | -12.53755 | -54.73755 | 2025-10-05 12:59:00 | TERRA_M-T | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 107.6 |
| 74621e15-f0e1-3712-8c61-7ac514c28d4f | -17.88132 | -57.64107 | 2025-10-05 12:59:00 | TERRA_M-T | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 14.6 |
| 581499ad-20ac-30f9-9ce4-479b64419252 | -12.2942 | -49.21626 | 2025-10-05 12:59:00 | TERRA_M-T | ALVORADA | TOCANTINS | Brasil | 1700707 | 17 | 33 | nan | nan | nan | Cerrado | 117.9 |
| d98a0a63-2fa9-378f-b776-31d183bb7fc8 | -13.70169 | -51.23244 | 2025-10-05 12:59:00 | TERRA_M-T | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 50.6 |
| b3e89e81-ce25-3422-884b-ab4d87b1f7e5 | -12.04529 | -56.91 | 2025-10-05 12:59:00 | TERRA_M-T | ITANHANGÁ | MATO GROSSO | Brasil | 5104542 | 51 | 33 | nan | nan | nan | Amazônia | 9.6 |
| 78b5211c-a483-3d68-ad84-66a81c4e4860 | -16.12253 | -53.9758 | 2025-10-05 12:59:00 | TERRA_M-T | POXORÉU | MATO GROSSO | Brasil | 5107008 | 51 | 33 | nan | nan | nan | Cerrado | 14.3 |
| 0e7f1bdd-855f-32b5-a2f4-360d2b0bfe01 | -18.20025 | -53.35896 | 2025-10-05 12:59:00 | TERRA_M-T | COSTA RICA | MATO GROSSO DO SUL | Brasil | 5003256 | 50 | 33 | nan | nan | nan | Cerrado | 25.5 |
| 129b0110-9689-39c3-89df-a146d1c7291e | -15.19349 | -56.83214 | 2025-10-05 12:59:00 | TERRA_M-T | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 8.7 |
| abf08517-249c-3ff2-a507-03824b5e9b08 | -15.22795 | -56.85701 | 2025-10-05 12:59:00 | TERRA_M-T | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 10.3 |
| 2f5a0b0b-7550-3338-8434-f49b57c60249 | -19.79391 | -51.9513 | 2025-10-05 12:59:00 | TERRA_M-T | INOCÊNCIA | MATO GROSSO DO SUL | Brasil | 5004403 | 50 | 33 | nan | nan | nan | Cerrado | 116.2 |
| 4b52b1b9-d618-32d7-bf70-9faf565d2e53 | -17.94059 | -57.60478 | 2025-10-05 12:59:00 | TERRA_M-T | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 17.3 |
| 0c60398e-54c1-3d83-a909-6ea3486cfef5 | -12.29299 | -49.18951 | 2025-10-05 12:59:00 | TERRA_M-T | ALVORADA | TOCANTINS | Brasil | 1700707 | 17 | 33 | nan | nan | nan | Cerrado | 42.0 |
| 7242df86-c0c6-333e-be11-1d7038ca5969 | -11.76858 | -58.21649 | 2025-10-05 12:59:00 | TERRA_M-T | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 7.9 |
| e2a54ef3-3a89-3175-80f1-df92f742514a | -17.9749 | -51.15831 | 2025-10-05 12:59:00 | TERRA_M-T | RIO VERDE | GOIÁS | Brasil | 5218805 | 52 | 33 | nan | nan | nan | Cerrado | 130.3 |
| a87614ad-f633-375d-b849-2a5954d1c901 | -17.9577 | -57.54675 | 2025-10-05 12:59:00 | TERRA_M-T | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 90.3 |
| 4eda9699-1d15-3827-a84c-c7d037660e33 | -19.02143 | -50.61458 | 2025-10-05 12:59:00 | TERRA_M-T | SÃO SIMÃO | GOIÁS | Brasil | 5220405 | 52 | 33 | nan | nan | nan | Mata Atlântica | 207.4 |
| 265c8922-8bd7-3655-afcb-bacb8c5810a9 | -17.9617 | -57.58725 | 2025-10-05 12:59:00 | TERRA_M-T | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 19.2 |
| 04207276-7b46-3eff-90b0-b8e909e8af4c | -14.97618 | -54.81012 | 2025-10-05 12:59:00 | TERRA_M-T | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 12.6 |
| de9b901e-4125-3d4d-a32d-816ce30d10ad | -18.17544 | -53.35783 | 2025-10-05 12:59:00 | TERRA_M-T | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 20.5 |
| 0b3c6843-a718-3777-8990-079fcdcaecdd | -17.95115 | -57.59599 | 2025-10-05 12:59:00 | TERRA_M-T | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 61.2 |
| d826e9d6-9ac9-3186-8bac-d6325eb9f338 | -15.21478 | -56.81435 | 2025-10-05 12:59:00 | TERRA_M-T | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 32.2 |
| 23012e96-0daa-3304-be54-366cb69c6146 | -11.843 | -57.7603 | 2025-10-05 12:59:00 | TERRA_M-T | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 7.1 |
| 12a0f4f7-47c8-3aa3-b7b1-1416d82e8d63 | -12.26168 | -49.18602 | 2025-10-05 12:59:00 | TERRA_M-T | ALVORADA | TOCANTINS | Brasil | 1700707 | 17 | 33 | nan | nan | nan | Cerrado | 114.8 |
| a1e38f6a-4ec4-31b8-a9c5-10b7e708e4a3 | -14.97452 | -54.82301 | 2025-10-05 12:59:00 | TERRA_M-T | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 60.1 |
| e24012fb-5467-35b3-a7e2-9937d221df97 | -12.26654 | -49.18139 | 2025-10-05 12:59:00 | TERRA_M-T | ALVORADA | TOCANTINS | Brasil | 1700707 | 17 | 33 | nan | nan | nan | Cerrado | 126.2 |
| ebc6c79c-32be-36d6-9f8b-dbd7095110dc | -13.61302 | -57.02413 | 2025-10-05 12:59:00 | TERRA_M-T | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Cerrado | 9.6 |
| 396dd349-d9b9-3ea3-8ad4-ab1c2c59993b | -12.28957 | -49.22101 | 2025-10-05 12:59:00 | TERRA_M-T | ALVORADA | TOCANTINS | Brasil | 1700707 | 17 | 33 | nan | nan | nan | Cerrado | 72.5 |
| c79f5684-eff1-35bc-b646-19d4b8484318 | -14.85409 | -60.06669 | 2025-10-05 12:59:00 | TERRA_M-T | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 10.9 |
| 1be370f1-7655-3a81-a540-dfe879abdb8f | -17.86829 | -57.59845 | 2025-10-05 12:59:00 | TERRA_M-T | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 13.0 |
| eb155ff5-9760-3f76-9e5e-7b3aafc9aa96 | -16.35285 | -51.4738 | 2025-10-05 12:59:00 | TERRA_M-T | ARENÓPOLIS | GOIÁS | Brasil | 5202353 | 52 | 33 | nan | nan | nan | Cerrado | 56.0 |
| e542bf09-9779-3da8-91df-8e16e3215281 | -15.98913 | -50.91027 | 2025-10-05 12:59:00 | TERRA_M-T | JUSSARA | GOIÁS | Brasil | 5212204 | 52 | 33 | nan | nan | nan | Cerrado | 23.1 |
| 1aeb20ac-fdaa-328c-a13c-dbfe8b07c120 | -15.18936 | -52.7929 | 2025-10-05 12:59:00 | TERRA_M-T | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 26.5 |
| 1f8ced3a-217d-37bd-8910-6e93d78f5547 | -15.31983 | -56.92714 | 2025-10-05 12:59:00 | TERRA_M-T | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 12.7 |
| 3c9b8478-28e4-312a-af2d-d8e50a1c1535 | -17.93136 | -57.6036 | 2025-10-05 12:59:00 | TERRA_M-T | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 17.3 |
| d6c2de39-78cb-3206-943f-e0cc57cc48d7 | -18.25139 | -53.34799 | 2025-10-05 12:59:00 | TERRA_M-T | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 37.8 |
| 7db713ef-40af-354d-a662-be329ed10a20 | -16.3587 | -51.47988 | 2025-10-05 12:59:00 | TERRA_M-T | ARENÓPOLIS | GOIÁS | Brasil | 5202353 | 52 | 33 | nan | nan | nan | Cerrado | 52.3 |
| 34b1997b-57b2-3d91-a863-860a02594365 | -17.84724 | -57.61566 | 2025-10-05 12:59:00 | TERRA_M-T | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 15.7 |
| 617d47e9-61dd-38a9-8b43-29faefec9b80 | -15.30922 | -56.93592 | 2025-10-05 12:59:00 | TERRA_M-T | BARRA DO BUGRES | MATO GROSSO | Brasil | 5101704 | 51 | 33 | nan | nan | nan | Cerrado | 8.0 |
| ae3235ea-6a8f-3b79-802a-14ab9384742e | -16.07511 | -51.08529 | 2025-10-05 12:59:00 | TERRA_M-T | FAZENDA NOVA | GOIÁS | Brasil | 5207600 | 52 | 33 | nan | nan | nan | Cerrado | 36.6 |
| 55d8bad6-adac-314a-a220-11770d0a17eb | -13.73462 | -51.306 | 2025-10-05 12:59:00 | TERRA_M-T | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 486.2 |


[Clique aqui para ver as próximas entradas](README155.md)
