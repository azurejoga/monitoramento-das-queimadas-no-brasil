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
| e641c1aa-0516-3089-9181-f78e7f5bf026 | 1.17334 | -60.37047 | 2026-02-20 04:57:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 15d04666-22ef-39de-96e7-5c382cf26495 | 1.37059 | -60.3137 | 2026-02-20 04:57:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 7adadace-eaf5-387a-af80-8a1eb29f0b93 | 0.4525 | -60.40292 | 2026-02-20 04:57:00 | NOAA-21 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 8.9 |
| 878c0e61-7bfe-39a6-a503-ff16f09eacf5 | 1.06285 | -60.56856 | 2026-02-20 04:57:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 6d61bc8b-b108-348f-a480-25ad5c0a0f7b | 1.36157 | -60.05729 | 2026-02-20 04:57:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.6 |
| a6b6cf92-3d5b-348e-9981-51eb66029892 | 1.53906 | -60.38622 | 2026-02-20 04:57:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 0e38b793-732d-3fbe-93f5-e11e71a1bee4 | 1.37196 | -60.31504 | 2026-02-20 04:57:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 3.9 |
| f7448c52-8d3c-37a5-8d6f-af34fdd593e5 | 0.45731 | -60.4022 | 2026-02-20 04:57:00 | NOAA-21 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 8.9 |
| 45e36fe1-b137-37f6-bb7e-363d79c97552 | 2.54461 | -60.72519 | 2026-02-20 04:57:00 | NOAA-21 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 4.0 |
| eb170fbc-0a12-38e3-8188-f0422642d965 | -9.72379 | -60.20364 | 2026-02-20 04:59:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 5c478b7f-6e46-3199-853c-85e0c5b0af3a | -10.66769 | -59.35775 | 2026-02-20 04:59:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 8975ef5b-9f5b-3030-855c-b4f8d8b81bdd | -10.16005 | -49.18061 | 2026-02-20 04:59:00 | NOAA-21 | CHAPADA DE AREIA | TOCANTINS | Brasil | 1704600 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 9d037f34-ec5b-3387-a521-86b258058a0d | -12.19559 | -47.96873 | 2026-02-20 04:59:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 9e76c1ed-b306-3564-836d-ee3bd1396d72 | -11.84447 | -49.2188 | 2026-02-20 04:59:00 | NOAA-21 | CARIRI DO TOCANTINS | TOCANTINS | Brasil | 1703867 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| a64c0f77-aea8-31c9-b352-7105e7637e72 | -10.67414 | -49.70361 | 2026-02-20 04:59:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| e5b13946-9fe2-3251-a6ac-2a84a3134940 | -10.67146 | -59.35838 | 2026-02-20 04:59:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| a6f494c0-b95a-38dd-84fc-de7940236578 | -11.84827 | -49.22374 | 2026-02-20 04:59:00 | NOAA-21 | CARIRI DO TOCANTINS | TOCANTINS | Brasil | 1703867 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| f796bafb-442c-3068-853c-3cfc1b1ee325 | -10.67682 | -59.34963 | 2026-02-20 04:59:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 1bed7da1-8f65-3464-b8f8-268746aa947d | -11.84391 | -49.22306 | 2026-02-20 04:59:00 | NOAA-21 | CARIRI DO TOCANTINS | TOCANTINS | Brasil | 1703867 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 108169f5-f4f0-3531-8e08-087a13aed01b | -10.67602 | -59.35434 | 2026-02-20 04:59:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| c283cc98-19c1-371f-b34f-e1ae34249f0e | -10.67523 | -59.35904 | 2026-02-20 04:59:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| cacb52e5-373b-3c6e-b9d3-a0de27a54188 | -10.66988 | -59.3677 | 2026-02-20 04:59:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 3d9c132b-87d0-330b-b585-c2ec729d06c6 | 2.5621 | -60.5458 | 2026-02-20 05:00:00 | GOES-19 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 56.9 |
| 9ea77d97-a571-3484-ab30-c45f92c09495 | 2.562 | -60.5648 | 2026-02-20 05:00:00 | GOES-19 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 88.3 |
| 2f57eaaa-3d05-3ce8-a173-d5bffd81be6b | -18.97491 | -52.931 | 2026-02-20 05:01:00 | NOAA-21 | PARAÍSO DAS ÁGUAS | MATO GROSSO DO SUL | Brasil | 5006275 | 50 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 43f4a90c-0c17-36ff-a012-a9b6a20cce86 | -11.83638 | -58.04511 | 2026-02-20 05:01:00 | NOAA-21 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 567241dc-6fdf-3262-b9c4-783fb474c56c | -18.81961 | -55.17368 | 2026-02-20 05:01:00 | NOAA-21 | RIO VERDE DE MATO GROSSO | MATO GROSSO DO SUL | Brasil | 5007406 | 50 | 33 | nan | nan | nan | Pantanal | 1.0 |
| df0b198d-b56b-3822-ab5a-a2e3612e9cc5 | -11.95631 | -58.73857 | 2026-02-20 05:01:00 | NOAA-21 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 0acdb596-bcb1-3bf6-8705-8bfbcc33bed9 | -18.31226 | -54.64501 | 2026-02-20 05:01:00 | NOAA-21 | COXIM | MATO GROSSO DO SUL | Brasil | 5003306 | 50 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 138d1020-b340-382d-9423-d15689353b02 | -20.47735 | -50.37347 | 2026-02-20 05:01:00 | NOAA-21 | SÃO JOÃO DE IRACEMA | SÃO PAULO | Brasil | 3549250 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| a5222270-090c-3666-b550-990d401df2d5 | -18.97558 | -52.92603 | 2026-02-20 05:01:00 | NOAA-21 | PARAÍSO DAS ÁGUAS | MATO GROSSO DO SUL | Brasil | 5006275 | 50 | 33 | nan | nan | nan | Cerrado | 5.9 |
| c9d14335-f45f-303a-b4bb-13022f5b5190 | -20.21399 | -50.74809 | 2026-02-20 05:01:00 | NOAA-21 | ASPÁSIA | SÃO PAULO | Brasil | 3503950 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| 29765215-d8ff-35c3-8656-18b5776ecc78 | -11.43773 | -60.94065 | 2026-02-20 05:01:00 | NOAA-21 | ESPIGÃO D'OESTE | RONDÔNIA | Brasil | 1100098 | 11 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 38a93752-f6ec-3043-ab71-0671d24aa78c | -18.97177 | -52.92548 | 2026-02-20 05:01:00 | NOAA-21 | PARAÍSO DAS ÁGUAS | MATO GROSSO DO SUL | Brasil | 5006275 | 50 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 52d7eee3-bce2-36fa-978d-d57ce69b952d | -13.49157 | -60.38482 | 2026-02-20 05:01:00 | NOAA-21 | COMODORO | MATO GROSSO | Brasil | 5103304 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| d542b5a3-4b33-3236-9307-e9213ec300e0 | -18.97111 | -52.93045 | 2026-02-20 05:01:00 | NOAA-21 | PARAÍSO DAS ÁGUAS | MATO GROSSO DO SUL | Brasil | 5006275 | 50 | 33 | nan | nan | nan | Cerrado | 5.9 |
| a7129ba4-5e22-366b-9736-a800223206e0 | -20.93653 | -48.66055 | 2026-02-20 05:03:00 | NOAA-21 | MONTE AZUL PAULISTA | SÃO PAULO | Brasil | 3531506 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.4 |
| eb1dca7e-0722-3e52-97f7-94d1231cef6c | -22.56419 | -53.49431 | 2026-02-20 05:03:00 | NOAA-21 | NOVA ANDRADINA | MATO GROSSO DO SUL | Brasil | 5006200 | 50 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| fd17b055-17df-3b91-a967-6caabf1f4436 | -20.93172 | -48.65672 | 2026-02-20 05:03:00 | NOAA-21 | MONTE AZUL PAULISTA | SÃO PAULO | Brasil | 3531506 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 7ec5f9fe-fb82-3523-8bad-091b0fff43ac | -20.93138 | -48.66003 | 2026-02-20 05:03:00 | NOAA-21 | MONTE AZUL PAULISTA | SÃO PAULO | Brasil | 3531506 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| b61a3e47-8978-317a-8f52-d0f2d35f3880 | -20.93687 | -48.65726 | 2026-02-20 05:03:00 | NOAA-21 | MONTE AZUL PAULISTA | SÃO PAULO | Brasil | 3531506 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.4 |
| f5b0546d-af27-355b-b5b8-45699ad3e755 | -21.88588 | -52.95871 | 2026-02-20 05:03:00 | NOAA-21 | ANAURILÂNDIA | MATO GROSSO DO SUL | Brasil | 5000807 | 50 | 33 | nan | nan | nan | Cerrado | 1.7 |
| ec41a384-0f58-3b5b-9f53-8e6cb5aad727 | -20.74301 | -50.53827 | 2026-02-20 05:03:00 | NOAA-21 | AURIFLAMA | SÃO PAULO | Brasil | 3504206 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.4 |
| 0e5f9b67-65bc-3b10-8120-9f847f4af042 | 2.562 | -60.5648 | 2026-02-20 05:10:00 | GOES-19 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 74.2 |
| 6f716054-b312-3ab6-ac96-5b867b7d7865 | 2.5621 | -60.5458 | 2026-02-20 05:10:00 | GOES-19 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 53.4 |
| 14373122-b329-3706-9234-78980ec66d29 | 2.5438 | -60.5651 | 2026-02-20 05:20:00 | GOES-19 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 54.3 |
| bdb80559-1d04-3378-b8fe-a42320e9a0df | 2.562 | -60.5648 | 2026-02-20 05:20:00 | GOES-19 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 76.3 |
| 53975c63-83ef-3d34-93ad-4a81e1d3ae77 | 3.64815 | -59.93738 | 2026-02-20 05:25:00 | NPP-375D | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d78f5558-8624-3d42-a5f6-fe73d59fa46f | 3.67247 | -60.76881 | 2026-02-20 05:25:00 | NPP-375D | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 7c012915-432c-3767-bad4-e2ac8757cdd3 | 2.68042 | -60.22234 | 2026-02-20 05:25:00 | NPP-375D | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 1066eb4f-9deb-302b-80f4-91236bbb47fb | 4.0597 | -61.10859 | 2026-02-20 05:25:00 | NPP-375D | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 1.6 |
| a8d9ee90-68fb-3139-9f73-0e41617c062f | 2.69469 | -60.24628 | 2026-02-20 05:25:00 | NPP-375D | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 584cd968-a265-3a8c-8682-e9d4adc20def | 2.68251 | -60.14749 | 2026-02-20 05:25:00 | NPP-375D | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 0.6 |
| e14e70c6-2852-3437-a5ba-a7662c759ab3 | 4.48039 | -60.56801 | 2026-02-20 05:25:00 | NPP-375D | UIRAMUTÃ | RORAIMA | Brasil | 1400704 | 14 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 585b5bca-30c9-38c9-9c93-a679b70d5e22 | 2.69488 | -60.22428 | 2026-02-20 05:25:00 | NPP-375D | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 1.2 |
| af7c24a5-c4fb-3c53-b4f9-9a69a5b9b05d | 2.69999 | -60.2347 | 2026-02-20 05:25:00 | NPP-375D | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 62a19551-ab8a-37ff-b524-df1537054f6f | 4.48087 | -60.56493 | 2026-02-20 05:25:00 | NPP-375D | UIRAMUTÃ | RORAIMA | Brasil | 1400704 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 6b64d2d3-8d73-3f1f-84eb-2d67f0d3170b | 2.68903 | -60.25465 | 2026-02-20 05:25:00 | NPP-375D | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 0.8 |
| b29670ae-6dfe-316b-ad13-2b934136be8c | 4.07439 | -60.18368 | 2026-02-20 05:25:00 | NPP-375D | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 73eb20be-6361-3057-a96f-50c170ac989a | 3.23086 | -61.19912 | 2026-02-20 05:25:00 | NPP-375D | ALTO ALEGRE | RORAIMA | Brasil | 1400050 | 14 | 33 | nan | nan | nan | Amazônia | 2.1 |
| d6e54aae-80b3-384b-8727-e1813f09ac4d | 2.69829 | -60.22374 | 2026-02-20 05:25:00 | NPP-375D | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d91f40e8-cee8-3b0f-b749-c5b53495ea05 | 4.47796 | -60.56935 | 2026-02-20 05:25:00 | NPP-375D | UIRAMUTÃ | RORAIMA | Brasil | 1400704 | 14 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 314ef363-3901-385f-939c-12d24178c0da | 2.68383 | -60.22181 | 2026-02-20 05:25:00 | NPP-375D | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 5111ba33-59c9-3bed-a9af-ac6ba515a7b7 | 4.16627 | -60.93257 | 2026-02-20 05:25:00 | NPP-375D | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 9a7856dd-61c2-3d7c-8474-03dbc5024bbe | 4.3732 | -60.33765 | 2026-02-20 05:25:00 | NPP-375D | UIRAMUTÃ | RORAIMA | Brasil | 1400704 | 14 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 874d35e0-36f4-3e07-907c-64e5634c1e5d | 4.83404 | -60.22232 | 2026-02-20 05:25:00 | NPP-375D | UIRAMUTÃ | RORAIMA | Brasil | 1400704 | 14 | 33 | nan | nan | nan | Amazônia | 0.4 |
| a240aa2b-c0bd-3337-ba49-2b0f1e0f28ef | 3.738 | -60.06549 | 2026-02-20 05:25:00 | NPP-375D | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 5c8b6ba8-d561-3f06-b6bf-f64901d2acfe | 2.69411 | -60.24262 | 2026-02-20 05:25:00 | NPP-375D | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 1.6 |
| d0283c9e-281a-3595-95e9-8b42af539d97 | 2.65868 | -60.12889 | 2026-02-20 05:25:00 | NPP-375D | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 69a49337-03e9-3b63-8240-b0880f49ad57 | 2.65529 | -60.12943 | 2026-02-20 05:25:00 | NPP-375D | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 5e98bd14-b571-3cb6-8dfc-43b27c322005 | 4.16274 | -60.93322 | 2026-02-20 05:25:00 | NPP-375D | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 5191872c-c35a-3c08-9266-d112340d5559 | 4.48145 | -60.5687 | 2026-02-20 05:25:00 | NPP-375D | UIRAMUTÃ | RORAIMA | Brasil | 1400704 | 14 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 6ad48fd4-b34e-38d3-99ed-a91ac239744a | 4.05613 | -61.10917 | 2026-02-20 05:25:00 | NPP-375D | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 4fc5ddd4-f422-37bb-8d32-670652a33e39 | 4.74291 | -60.37593 | 2026-02-20 05:25:00 | NPP-375D | UIRAMUTÃ | RORAIMA | Brasil | 1400704 | 14 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 0062049b-741a-3671-a531-f32cc7babe61 | 4.10731 | -60.64518 | 2026-02-20 05:25:00 | NPP-375D | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 2.9 |
| ff20d76c-4042-39c2-a8ef-1000d0c8e806 | 4.03827 | -60.13261 | 2026-02-20 05:25:00 | NPP-375D | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 2.5 |
| aabc8d68-53a6-3360-84b9-4df70ef6968f | 4.07781 | -60.18304 | 2026-02-20 05:25:00 | NPP-375D | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 698a28e8-b5fb-3a3b-b993-09745f57e12c | 2.7017 | -60.22321 | 2026-02-20 05:25:00 | NPP-375D | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 7fddf1b4-a338-34fd-ae16-8f6100473c54 | 2.68845 | -60.25099 | 2026-02-20 05:25:00 | NPP-375D | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e4916f4f-7f3e-3c3e-8c38-a626003bc209 | 4.06405 | -61.13689 | 2026-02-20 05:25:00 | NPP-375D | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 76da10f3-6e71-315d-9f15-7024449cf18c | 4.51654 | -60.93719 | 2026-02-20 05:25:00 | NPP-375D | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 95ada324-a15d-3e91-91d0-1ed4f657fae2 | 4.97482 | -60.5223 | 2026-02-20 05:25:00 | NPP-375D | UIRAMUTÃ | RORAIMA | Brasil | 1400704 | 14 | 33 | nan | nan | nan | Amazônia | 1.3 |
| acb342cd-e42c-37c1-997f-f63675e46021 | 4.0656 | -61.09938 | 2026-02-20 05:25:00 | NPP-375D | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ae7d94a8-b463-3db7-a310-d222121beade | 4.48493 | -60.56806 | 2026-02-20 05:25:00 | NPP-375D | UIRAMUTÃ | RORAIMA | Brasil | 1400704 | 14 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 2fbc9c0e-ecd9-303c-8729-10cd8610fda6 | 4.06203 | -61.09995 | 2026-02-20 05:25:00 | NPP-375D | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 2c075553-4280-39cf-b64b-a435c46fd944 | 2.76713 | -60.28417 | 2026-02-20 05:25:00 | NPP-375D | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 51422236-1058-3526-abd4-429205b3217a | 1.54012 | -60.38558 | 2026-02-20 05:27:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 2010ae2b-73b2-37b7-b601-d66a2f37c3f4 | 1.97713 | -60.69881 | 2026-02-20 05:27:00 | NPP-375D | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 7b48808e-29b9-3f3f-9477-a2d420b7e66a | 1.37804 | -60.31081 | 2026-02-20 05:27:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 3b9cffb9-083f-30ac-9461-5d981c32066b | 1.37077 | -60.37473 | 2026-02-20 05:27:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b3d90bf6-d857-3dc8-8eef-b9c461450ccd | 1.15077 | -60.33086 | 2026-02-20 05:27:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 2.1 |
| ff33c8cd-730e-3d85-8e63-c4ea977ed9df | 1.06306 | -60.56989 | 2026-02-20 05:27:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 549dedf0-02fb-3adf-b160-38fcf79d5dcd | 1.15754 | -60.3298 | 2026-02-20 05:27:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 0d8ff728-ca3c-3d66-9ffb-a52697e2111d | 2.53997 | -60.72578 | 2026-02-20 05:27:00 | NPP-375D | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 6770dd84-7207-3195-9fdd-6db345dee00b | 0.96402 | -60.23513 | 2026-02-20 05:27:00 | NPP-375D | SÃO LUIZ | RORAIMA | Brasil | 1400605 | 14 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 90c62e0b-0da5-32eb-a09b-0b99eefb9b0a | 0.45014 | -60.40273 | 2026-02-20 05:27:00 | NPP-375D | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 7d4c96b7-c896-3c9c-beb7-a8be91a5cdfa | 1.37409 | -60.30775 | 2026-02-20 05:27:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 93e623d5-7a1f-3901-96d1-daafcc0d600d | 1.3083 | -60.39878 | 2026-02-20 05:27:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 99c653e2-edab-39ab-8ce5-259ae7da3b82 | 0.45296 | -60.39862 | 2026-02-20 05:27:00 | NPP-375D | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 5099b4a2-c383-3eb0-b677-f8cf5271f161 | 1.37918 | -60.31802 | 2026-02-20 05:27:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.3 |


[Clique aqui para ver as próximas entradas](README6.md)
