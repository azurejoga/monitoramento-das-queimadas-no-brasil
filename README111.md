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

## Dados Diários - Página 111

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 9613d69b-d735-39c5-b472-8e9214144f5e | -17.23646 | -50.2326 | 2025-09-13 05:27:00 | NPP-375D | JANDAIA | GOIÁS | Brasil | 5211701 | 52 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 84bdb85c-28af-368b-be2d-ae80602c2391 | -15.16593 | -52.48774 | 2025-09-13 05:27:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 1a1d4553-dfff-3413-a78b-faa350d89469 | -12.38637 | -62.20887 | 2025-09-13 05:27:00 | NPP-375D | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 2.9 |
| b3622e55-d2c4-3b0a-91f7-696c1ec5654f | -12.80546 | -47.9964 | 2025-09-13 05:27:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 17dce95e-ebd1-30ce-a169-312e4048b16a | -11.37193 | -59.14359 | 2025-09-13 05:27:00 | NPP-375D | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 1d622e92-0802-30b6-be4a-b7231e10d346 | -13.47264 | -48.45021 | 2025-09-13 05:27:00 | NPP-375D | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| eaf36ceb-a6e7-394a-88d3-4d09010ce37b | -12.86297 | -62.12713 | 2025-09-13 05:27:00 | NPP-375D | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 150497ba-fcfb-3142-848f-807d7d813d90 | -14.72052 | -59.72052 | 2025-09-13 05:27:00 | NPP-375D | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| b89975f8-6a10-398b-97dc-bbd27a150e5e | -17.41766 | -49.2408 | 2025-09-13 05:27:00 | NPP-375D | PROFESSOR JAMIL | GOIÁS | Brasil | 5218391 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 4a93b90c-1d1c-3df5-9016-b21d2dd1467d | -16.55643 | -49.24167 | 2025-09-13 05:27:00 | NPP-375D | GOIÂNIA | GOIÁS | Brasil | 5208707 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 18922311-3fcb-34b7-9e57-42fbc23f54d4 | -17.29396 | -48.74685 | 2025-09-13 05:27:00 | NPP-375D | SANTA CRUZ DE GOIÁS | GOIÁS | Brasil | 5219209 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 554476cb-29dd-3cb1-8ff3-2fcbd2a83f69 | -12.94442 | -48.00644 | 2025-09-13 05:27:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 5d5d62a1-4e2c-383a-8bbc-706cc352e9b3 | -16.49797 | -55.1391 | 2025-09-13 05:27:00 | NPP-375D | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 2.4 |
| 17c6b9ab-654a-3592-bffd-ba38c3562cae | -15.13042 | -52.49952 | 2025-09-13 05:27:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 516fb414-338d-3c1a-a861-8ebf568a29be | -16.50541 | -55.11735 | 2025-09-13 05:27:00 | NPP-375D | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 2.1 |
| 97507763-029a-301a-a447-397dcc99c6f4 | -16.35879 | -51.51638 | 2025-09-13 05:27:00 | NPP-375D | ARENÓPOLIS | GOIÁS | Brasil | 5202353 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| c028b9f2-b575-36ed-9b94-f7921c634511 | -14.74788 | -55.61617 | 2025-09-13 05:27:00 | NPP-375D | CHAPADA DOS GUIMARÃES | MATO GROSSO | Brasil | 5103007 | 51 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 4abc266d-62e1-37db-b17c-0afe79af1b6a | -16.36448 | -51.53392 | 2025-09-13 05:27:00 | NPP-375D | ARENÓPOLIS | GOIÁS | Brasil | 5202353 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| bb038e70-0714-3e89-8c46-e781bef02f94 | -11.38308 | -63.35573 | 2025-09-13 05:27:00 | NPP-375D | SÃO MIGUEL DO GUAPORÉ | RONDÔNIA | Brasil | 1100320 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| dcf66bfb-1395-3590-8a05-1a9c3bdbefeb | -16.52828 | -51.75311 | 2025-09-13 05:27:00 | NPP-375D | PIRANHAS | GOIÁS | Brasil | 5217203 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 9a635822-9adb-3ab9-aceb-1001fb260aef | -12.95434 | -47.98202 | 2025-09-13 05:27:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 8402eabd-2367-3880-8489-1e2d660487cf | -15.57775 | -54.73991 | 2025-09-13 05:27:00 | NPP-375D | DOM AQUINO | MATO GROSSO | Brasil | 5103601 | 51 | 33 | nan | nan | nan | Cerrado | 5.3 |
| bd02920c-2807-32da-9796-9befac64a55f | -12.95389 | -48.01182 | 2025-09-13 05:27:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 11.2 |
| f6328a28-b07e-33b6-81b5-e3cc2dc1ae4e | -12.25461 | -59.3521 | 2025-09-13 05:27:00 | NPP-375D | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 3dbcb436-94a8-3ebc-adb7-c661eb6ae102 | -10.88411 | -59.23293 | 2025-09-13 05:27:00 | NPP-375D | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 9d006f2c-567d-39d1-bcc4-7d79d40c4f32 | -11.77762 | -64.94209 | 2025-09-13 05:27:00 | NPP-375D | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 5.2 |
| e6290231-b2c7-3868-89aa-e450dd7573b2 | -15.13694 | -52.49222 | 2025-09-13 05:27:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| c125a4d3-4602-3244-8c1a-8ac4f11a03b2 | -16.5654 | -49.22132 | 2025-09-13 05:27:00 | NPP-375D | GOIÂNIA | GOIÁS | Brasil | 5208707 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 3fde466a-7e30-3d6f-887b-25b3f80f47e3 | -15.16639 | -52.48375 | 2025-09-13 05:27:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 385e4659-1881-3bda-8d62-4e32bc3e1318 | -12.95513 | -47.99966 | 2025-09-13 05:27:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 11.8 |
| 34535428-0e3d-3018-9b14-402e4dc39b05 | -15.21494 | -56.68443 | 2025-09-13 05:27:00 | NPP-375D | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 3e1f9afa-a260-3048-a044-0df1f26b647e | -10.15815 | -64.7322 | 2025-09-13 05:27:00 | NPP-375D | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 15.2 |
| 351b12cc-a080-3fdc-b2b8-dd458f40662f | -12.86349 | -62.14536 | 2025-09-13 05:27:00 | NPP-375D | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| d4cc49dd-0308-3819-9f36-04c761f33277 | -15.05641 | -47.99156 | 2025-09-13 05:27:00 | NPP-375D | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| f5334d13-0601-3f6b-bd39-262d2f225f75 | -15.7051 | -50.58436 | 2025-09-13 05:27:00 | NPP-375D | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 09951c8b-7dc0-3490-b9f1-685816c857cf | -11.93016 | -51.13317 | 2025-09-13 05:27:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| d40b7720-68e9-3cd9-a38d-f975919951bb | -14.38439 | -60.28776 | 2025-09-13 05:27:00 | NPP-375D | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| fc6b4248-8675-3ef9-acde-825d066e461a | -9.96102 | -64.96571 | 2025-09-13 05:27:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.2 |
| c48f95f4-39cc-3e1f-ac4f-8c15dc28fc0f | -11.37443 | -63.36575 | 2025-09-13 05:27:00 | NPP-375D | SÃO MIGUEL DO GUAPORÉ | RONDÔNIA | Brasil | 1100320 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| cb9394dc-e645-3d21-8f27-af75205e33cb | -16.41602 | -49.04799 | 2025-09-13 05:27:00 | NPP-375D | TEREZÓPOLIS DE GOIÁS | GOIÁS | Brasil | 5221197 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| fbbb1394-3a2b-352a-a712-fc0169715a2d | -16.87211 | -49.34695 | 2025-09-13 05:27:00 | NPP-375D | HIDROLÂNDIA | GOIÁS | Brasil | 5209705 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| d4f956ea-73a5-31b2-89ad-ba21eaf6b7d0 | -16.55134 | -49.22117 | 2025-09-13 05:27:00 | NPP-375D | GOIÂNIA | GOIÁS | Brasil | 5208707 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 00f93d2a-e283-3940-8b48-57eb1c731856 | -15.21737 | -56.68828 | 2025-09-13 05:27:00 | NPP-375D | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 4.6 |
| f7414411-3f24-38cd-a799-1f523571d70d | -15.86106 | -49.94456 | 2025-09-13 05:27:00 | NPP-375D | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 2dfc247a-e54c-31fc-a5f1-e521bc08b0ab | -15.76916 | -52.24279 | 2025-09-13 05:27:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 3.4 |
| eb96ab55-3045-32f2-83b3-0605f4214315 | -18.15354 | -49.19581 | 2025-09-13 05:27:00 | NPP-375D | BURITI ALEGRE | GOIÁS | Brasil | 5203906 | 52 | 33 | nan | nan | nan | Mata Atlântica | 16.9 |
| dd4d96f0-4a52-364a-b84d-de8c707350a8 | -11.77038 | -64.94079 | 2025-09-13 05:27:00 | NPP-375D | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 49829592-6d61-3438-94c9-9cd6931ce494 | -10.15376 | -64.73589 | 2025-09-13 05:27:00 | NPP-375D | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 4.8 |
| dcc586d7-450d-35b4-b61d-eca9f4475a84 | -15.59325 | -54.77562 | 2025-09-13 05:27:00 | NPP-375D | DOM AQUINO | MATO GROSSO | Brasil | 5103601 | 51 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 039a54be-ab86-3af3-87fe-50a0509c7ef5 | -17.42123 | -49.2611 | 2025-09-13 05:27:00 | NPP-375D | PROFESSOR JAMIL | GOIÁS | Brasil | 5218391 | 52 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 18730fe1-3493-3bc4-bd94-284e0af3bf2a | -16.35923 | -51.51229 | 2025-09-13 05:27:00 | NPP-375D | ARENÓPOLIS | GOIÁS | Brasil | 5202353 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| ce5195b6-3cef-3cbc-ba00-2c5839b3e7a3 | -16.33929 | -51.54054 | 2025-09-13 05:27:00 | NPP-375D | ARENÓPOLIS | GOIÁS | Brasil | 5202353 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| c301cea1-f019-34e2-9ef6-33109ffc9456 | -15.69171 | -50.57762 | 2025-09-13 05:27:00 | NPP-375D | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 2de700f8-63ee-3c9b-8131-97dd1f3414d6 | -18.16101 | -49.19193 | 2025-09-13 05:27:00 | NPP-375D | BURITI ALEGRE | GOIÁS | Brasil | 5203906 | 52 | 33 | nan | nan | nan | Mata Atlântica | 5.9 |
| 1731b7e3-039d-3f53-a12d-dcd5ac29ae0e | -15.17297 | -52.32533 | 2025-09-13 05:27:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 1aad6da9-bbd4-369d-8989-b8fa128408bb | -15.17054 | -52.49723 | 2025-09-13 05:27:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| d605844f-2200-3bac-a47d-e527030df94d | -11.25422 | -61.56533 | 2025-09-13 05:27:00 | NPP-375D | MINISTRO ANDREAZZA | RONDÔNIA | Brasil | 1101203 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 137b1d98-39ab-32ff-9847-f3a0418c7743 | -12.95169 | -48.00655 | 2025-09-13 05:27:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 9.5 |
| 9b04e36f-cfb8-37b5-bfb6-1c04431fc3c0 | -15.32403 | -52.90427 | 2025-09-13 05:27:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 796d6f40-02cd-3caa-98dc-fd19bb7488bd | -15.552 | -54.80334 | 2025-09-13 05:27:00 | NPP-375D | DOM AQUINO | MATO GROSSO | Brasil | 5103601 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 1f8377b4-e73b-305b-9daa-1f629acf8736 | -15.22161 | -56.68893 | 2025-09-13 05:27:00 | NPP-375D | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 8dda12d9-7708-36d0-8a67-93cda4531a14 | -17.40718 | -49.25993 | 2025-09-13 05:27:00 | NPP-375D | PROFESSOR JAMIL | GOIÁS | Brasil | 5218391 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 619c1fb6-823a-3dbc-a6d5-c7ca4613959b | -14.7187 | -59.68292 | 2025-09-13 05:27:00 | NPP-375D | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| ba179013-259f-33cb-bc73-95f1c4116cac | -18.15757 | -49.19239 | 2025-09-13 05:27:00 | NPP-375D | BURITI ALEGRE | GOIÁS | Brasil | 5203906 | 52 | 33 | nan | nan | nan | Mata Atlântica | 9.0 |
| 81032d55-c20e-3701-bfea-78070dd0bd68 | -12.8663 | -62.12768 | 2025-09-13 05:27:00 | NPP-375D | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 7f167160-84a3-3ed2-b7cc-c02a7344d20a | -15.05575 | -47.99818 | 2025-09-13 05:27:00 | NPP-375D | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 3139f1ed-8a7d-3ef7-80d7-32327c1817c2 | -16.36857 | -51.53945 | 2025-09-13 05:27:00 | NPP-375D | ARENÓPOLIS | GOIÁS | Brasil | 5202353 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 84319e70-deda-3983-b536-cce98b0a44b3 | -16.50081 | -55.15633 | 2025-09-13 05:27:00 | NPP-375D | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 2.6 |
| 9f76fa14-1b48-390d-b2df-15379a225111 | -15.37932 | -52.1081 | 2025-09-13 05:27:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 73b07fd0-8cd4-3308-a2c4-cbd5217f3ad9 | -11.77691 | -64.94635 | 2025-09-13 05:27:00 | NPP-375D | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| c6a94373-bcf6-3e7e-945c-2fde5c975e39 | -15.76892 | -52.24305 | 2025-09-13 05:27:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 6a492f7d-8c5a-33d6-a19b-a2f3786dea61 | -15.21313 | -56.68761 | 2025-09-13 05:27:00 | NPP-375D | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 6196e56d-8999-3896-a818-e435949d0899 | -14.38872 | -60.29578 | 2025-09-13 05:27:00 | NPP-375D | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 8fe07211-bc8c-32d3-9125-f5ac384a156a | -16.87348 | -49.34844 | 2025-09-13 05:27:00 | NPP-375D | HIDROLÂNDIA | GOIÁS | Brasil | 5209705 | 52 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 7c536843-8933-3149-9128-b2ad0d9f4d72 | -11.38247 | -63.35945 | 2025-09-13 05:27:00 | NPP-375D | SÃO MIGUEL DO GUAPORÉ | RONDÔNIA | Brasil | 1100320 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| cbee7989-7ef0-3af2-b8e3-9c12a8427f54 | -15.12483 | -52.49861 | 2025-09-13 05:27:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| f14545a7-bace-3744-87d5-d4ade793f57b | -11.36782 | -59.14702 | 2025-09-13 05:27:00 | NPP-375D | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 71c6eb60-b351-3ff3-99bc-12546011fec0 | -17.23699 | -50.22691 | 2025-09-13 05:27:00 | NPP-375D | JANDAIA | GOIÁS | Brasil | 5211701 | 52 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 0bb184b5-aaa8-35a3-89a9-c064cdb9275d | -12.79813 | -47.99699 | 2025-09-13 05:27:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 45de8065-bb78-306b-9e70-3148d38430f4 | -12.86633 | -62.10587 | 2025-09-13 05:27:00 | NPP-375D | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 2f5d99da-bc48-3758-936d-dbd3e15f8107 | -16.40731 | -49.04611 | 2025-09-13 05:27:00 | NPP-375D | TEREZÓPOLIS DE GOIÁS | GOIÁS | Brasil | 5221197 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| e59a4791-72cb-3d36-8d6c-4783799c433d | -17.23994 | -50.2277 | 2025-09-13 05:27:00 | NPP-375D | JANDAIA | GOIÁS | Brasil | 5211701 | 52 | 33 | nan | nan | nan | Cerrado | 4.4 |
| c41f0821-5670-372d-938f-b236138009c8 | -12.93738 | -48.00418 | 2025-09-13 05:27:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 0525f3d4-0259-3288-bf9a-fb68188bf605 | -16.86712 | -49.3416 | 2025-09-13 05:27:00 | NPP-375D | HIDROLÂNDIA | GOIÁS | Brasil | 5209705 | 52 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 1391d658-c7a0-3521-8f6b-d2b4c236a19a | -15.20646 | -56.6831 | 2025-09-13 05:27:00 | NPP-375D | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 181e4bfd-21d9-3a72-8b06-ee7756465e9d | -12.8669 | -62.10233 | 2025-09-13 05:27:00 | NPP-375D | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b49a9aed-fcc5-36f2-bc30-17cd0f3cb801 | -12.93796 | -47.9988 | 2025-09-13 05:27:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 7.5 |
| d988a565-8aa6-3910-a64f-37a5f4a58dc6 | -13.26516 | -51.70818 | 2025-09-13 05:27:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 2b6878a2-1e06-3250-9f21-797b4b6d0594 | -14.46395 | -55.95475 | 2025-09-13 05:27:00 | NPP-375D | NOBRES | MATO GROSSO | Brasil | 5105903 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 868d00bd-efa3-30f1-9aa4-6e20b6161c15 | -16.55708 | -49.23483 | 2025-09-13 05:27:00 | NPP-375D | GOIÂNIA | GOIÁS | Brasil | 5208707 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| f25a55c1-009a-3b09-8e74-ce8e4c03323a | -15.69751 | -50.58378 | 2025-09-13 05:27:00 | NPP-375D | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| be42b79b-33d1-3b2d-a6bb-915e8196346c | -17.376 | -52.90667 | 2025-09-13 05:27:00 | NPP-375D | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 53c4dcc9-1f50-3265-b3df-1e5a1930498a | -16.33125 | -51.54444 | 2025-09-13 05:27:00 | NPP-375D | ARENÓPOLIS | GOIÁS | Brasil | 5202353 | 52 | 33 | nan | nan | nan | Cerrado | 10.4 |
| e2aa5702-8693-3933-b4a4-c84bad6223f0 | -15.55269 | -54.79777 | 2025-09-13 05:27:00 | NPP-375D | DOM AQUINO | MATO GROSSO | Brasil | 5103601 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 6f60d81c-3f4f-3276-842b-70dba15f92a6 | -14.38601 | -60.30043 | 2025-09-13 05:27:00 | NPP-375D | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| df2bc69f-8d2d-33a1-b000-93024f30563f | -15.67411 | -49.90049 | 2025-09-13 05:27:00 | NPP-375D | ITAPURANGA | GOIÁS | Brasil | 5211206 | 52 | 33 | nan | nan | nan | Cerrado | 7.2 |
| 2c08aaba-c3cc-350b-bcbc-ab7c993805d5 | -16.49385 | -55.13268 | 2025-09-13 05:27:00 | NPP-375D | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 3.9 |
| 86a67454-59c6-35bc-89a4-16f188a2db02 | -16.53283 | -51.74349 | 2025-09-13 05:27:00 | NPP-375D | PIRANHAS | GOIÁS | Brasil | 5217203 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 062bf18c-dafd-31e5-bcbc-58037028d471 | -12.87123 | -62.16119 | 2025-09-13 05:27:00 | NPP-375D | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 6ba9dd17-d16a-3865-957f-808f10a79a8e | -18.15004 | -49.19662 | 2025-09-13 05:27:00 | NPP-375D | BURITI ALEGRE | GOIÁS | Brasil | 5203906 | 52 | 33 | nan | nan | nan | Mata Atlântica | 9.4 |


[Clique aqui para ver as próximas entradas](README112.md)
