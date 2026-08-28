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

## Dados Diários - Página 10

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 4e7102f8-ba15-3b9b-a159-b9665f955408 | -10.4981 | -64.5005 | 2026-08-28 02:10:00 | GOES-19 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 72.2 |
| c949499d-c0eb-366c-a074-8392e941d48c | -11.2879 | -54.0317 | 2026-08-28 02:10:00 | GOES-19 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 577.5 |
| 18e16c40-b04f-3e7c-bd99-411725691aef | -4.8583 | -45.3915 | 2026-08-28 02:10:00 | GOES-19 | LAGOA GRANDE DO MARANHÃO | MARANHÃO | Brasil | 2105963 | 21 | 33 | nan | nan | nan | Cerrado | 85.4 |
| 4a96e744-706e-3810-8ace-0e3abdd4c08a | -10.4081 | -61.2492 | 2026-08-28 02:10:00 | GOES-19 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 46.6 |
| 9aff7186-7692-3919-a992-23da8906bf45 | -7.2471 | -45.8685 | 2026-08-28 02:10:00 | GOES-19 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 246.4 |
| 51c0f41f-372a-3333-ac72-fb1f63fd1efc | -10.7596 | -54.0384 | 2026-08-28 02:10:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 71.4 |
| d1544229-eca3-3ee3-aeb0-14113d87a54f | -6.1472 | -57.7995 | 2026-08-28 02:10:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 72.2 |
| 29c5e292-8f47-3c62-b117-068c6a197879 | -16.1444 | -58.6073 | 2026-08-28 02:10:00 | GOES-19 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 112.9 |
| d2569cc8-a71c-3c5d-9f33-f214564e4fe0 | -10.3894 | -61.2502 | 2026-08-28 02:10:00 | GOES-19 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 104.9 |
| da3ec07a-b03d-34c1-9e82-3005f1165717 | -11.269 | -54.0334 | 2026-08-28 02:10:00 | GOES-19 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 134.2 |
| 67d01939-394d-3921-a5cd-52c3eb5c33a2 | -11.2882 | -54.0111 | 2026-08-28 02:10:00 | GOES-19 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 233.6 |
| 702e8cec-e04a-33b6-951e-17cdcd7b856b | -7.2661 | -45.8443 | 2026-08-28 02:10:00 | GOES-19 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 204.4 |
| 6a7b1ada-ec68-350d-bafa-14768aa3b49b | -6.1656 | -57.7988 | 2026-08-28 02:10:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 130.5 |
| 6e912f60-538d-3114-b935-5292e8de9dd8 | -8.5968 | -54.7957 | 2026-08-28 02:10:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 38.2 |
| 3bb461d1-290d-358a-93bf-8958a44eb469 | -11.3068 | -54.0299 | 2026-08-28 02:10:00 | GOES-19 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 144.5 |
| 1c12cbf3-b72a-3876-b5e8-bb09328d40f2 | -11.5659 | -45.5338 | 2026-08-28 02:10:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 86.7 |
| 70f810ff-6f41-33e5-b467-7c911e4dfab2 | -6.1657 | -57.7793 | 2026-08-28 02:10:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 78.6 |
| be564188-229b-3a87-8b25-69b583e7e8e6 | -16.1641 | -58.5851 | 2026-08-28 02:10:00 | GOES-19 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 330.8 |
| a2794a1b-63ec-3fee-86cc-17fc7cc7d845 | -8.5969 | -54.7755 | 2026-08-28 02:10:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 55.5 |
| af3ab30b-6d4b-3bb0-a651-f97b791a1c2c | -11.2317 | -53.9958 | 2026-08-28 02:10:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 75.6 |
| 198a7c70-31ab-37bf-9792-67a4fb6f2dee | -10.9367 | -50.5332 | 2026-08-28 02:10:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 69.5 |
| 15e30499-dd07-38b3-b11c-7dca214e86af | -10.4082 | -61.23 | 2026-08-28 02:10:00 | GOES-19 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 45.6 |
| d1fa7f37-1d78-33f7-b1e5-f2c670f9b41e | -11.2877 | -54.0522 | 2026-08-28 02:10:00 | GOES-19 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 79.1 |
| 1ce7b6b5-ef1e-3c63-b3f5-2b51b0b226fe | -7.2474 | -45.846 | 2026-08-28 02:10:00 | GOES-19 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 165.7 |
| 8685983f-ee63-3ca3-8e0c-cb669444c0f0 | -12.4305 | -43.3944 | 2026-08-28 02:10:00 | GOES-19 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 104.7 |
| b6322712-a7d3-39be-a9cb-b10b36c7c67d | -10.3895 | -61.231 | 2026-08-28 02:10:00 | GOES-19 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 98.7 |
| 8c875dc8-ab60-352d-8080-5ee9c6e3e481 | -16.1638 | -58.6053 | 2026-08-28 02:10:00 | GOES-19 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 216.5 |
| 3ba5dbb2-f1ec-367f-bd47-d73ec0279faf | -4.8397 | -45.3926 | 2026-08-28 02:10:00 | GOES-19 | LAGOA GRANDE DO MARANHÃO | MARANHÃO | Brasil | 2105963 | 21 | 33 | nan | nan | nan | Cerrado | 65.9 |
| 1765610f-3ae7-37a9-8f97-4dc3335634f8 | -11.56 | -45.51 | 2026-08-28 02:15:00 | MSG-03 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 3aa58c74-a0fd-3927-8512-e20d641b7b8b | -11.26 | -54.02 | 2026-08-28 02:15:00 | MSG-03 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| f1b116a0-8c38-367a-80ae-d62912e75312 | -11.32 | -54.04 | 2026-08-28 02:15:00 | MSG-03 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| e0b389ff-66bc-33d1-aa32-17edc90bf296 | -11.56 | -45.56 | 2026-08-28 02:15:00 | MSG-03 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| cd04b1e1-dce4-3c22-91a8-01e06ac08ce1 | -7.22 | -45.87 | 2026-08-28 02:15:00 | MSG-03 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 358c9c21-9fae-36dc-b105-cccdc5ed86b3 | -14.85 | -52.56 | 2026-08-28 02:15:00 | MSG-03 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| a39b3247-1f67-3d60-b653-650bdc0c66cb | -7.25 | -45.83 | 2026-08-28 02:15:00 | MSG-03 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 3c7bfc30-8333-39b3-9099-ec0b529adc57 | -14.85 | -52.62 | 2026-08-28 02:15:00 | MSG-03 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 17a7ff4f-a783-37c1-be3e-bdd37f997ebd | -7.25 | -45.88 | 2026-08-28 02:15:00 | MSG-03 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 5736215f-fb0a-3268-ac55-2c825498113f | -11.29 | -54.03 | 2026-08-28 02:15:00 | MSG-03 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| f7baff89-b016-3c1f-9c3d-799ff11eed4a | -11.59 | -45.57 | 2026-08-28 02:15:00 | MSG-03 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| a796341e-f001-3505-8e6a-f27b652242b2 | -11.28 | -53.97 | 2026-08-28 02:15:00 | MSG-03 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| f78ce289-c419-3d4a-a360-6c5058c4251d | -11.29 | -54.1 | 2026-08-28 02:15:00 | MSG-03 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 9ebd47e8-f7a0-3e5e-863d-4672c5fa787d | -6.1656 | -57.7988 | 2026-08-28 02:20:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 111.2 |
| 0b1916ae-c8c0-346e-ae2c-4e9f56a5d9e1 | -11.2879 | -54.0317 | 2026-08-28 02:20:00 | GOES-19 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 135.5 |
| 4737c68c-56d3-3f2c-906e-eec8be4d9173 | -10.9177 | -50.5352 | 2026-08-28 02:20:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 73.5 |
| 4df03ead-22f2-3770-b32e-3f7a3cae6364 | -16.1444 | -58.6073 | 2026-08-28 02:20:00 | GOES-19 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 112.4 |
| 0dab178d-574c-326c-9908-818ebb1d1747 | -10.4082 | -61.23 | 2026-08-28 02:20:00 | GOES-19 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 84.0 |
| 1a4429e8-6a4a-3669-9330-c89ae63a0f0c | -11.2693 | -54.0129 | 2026-08-28 02:20:00 | GOES-19 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 54.6 |
| 7892f2eb-8acb-329d-bcc3-b409627e78cb | -16.1641 | -58.5851 | 2026-08-28 02:20:00 | GOES-19 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 316.6 |
| b86f6414-d1ab-31ff-ad3f-b91fb7236acd | -16.1447 | -58.5871 | 2026-08-28 02:20:00 | GOES-19 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 204.4 |
| 227f8869-b9bd-36b9-93db-4fb904566dcf | -10.7596 | -54.0384 | 2026-08-28 02:20:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 59.5 |
| b630e08e-1136-39d6-9411-b4b2b52e1ffc | -8.0301 | -48.0145 | 2026-08-28 02:20:00 | GOES-19 | PALMEIRANTE | TOCANTINS | Brasil | 1715705 | 17 | 33 | nan | nan | nan | Cerrado | 80.8 |
| e8790832-1486-36dd-99be-675184d287e4 | -10.3894 | -61.2502 | 2026-08-28 02:20:00 | GOES-19 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 189.5 |
| 20b81737-e805-388c-afba-3d7f00cf97de | -4.8583 | -45.3915 | 2026-08-28 02:20:00 | GOES-19 | LAGOA GRANDE DO MARANHÃO | MARANHÃO | Brasil | 2105963 | 21 | 33 | nan | nan | nan | Cerrado | 58.9 |
| d26e4e64-6166-3510-a4c9-8d453806856d | -11.8239 | -47.2178 | 2026-08-28 02:20:00 | GOES-19 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 72.6 |
| 0962fbf8-3916-3c83-972c-0309bfcbbffc | -6.1473 | -57.78 | 2026-08-28 02:20:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 39.4 |
| e9ca0074-0448-334c-b486-827393bbfead | -11.2317 | -53.9958 | 2026-08-28 02:20:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 70.7 |
| f257a254-1bef-3d1a-ad98-a82ad01d409b | -11.269 | -54.0334 | 2026-08-28 02:20:00 | GOES-19 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 60.1 |
| 50129176-fb91-30c9-91a7-ec3bffb6484c | -12.4305 | -43.3944 | 2026-08-28 02:20:00 | GOES-19 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 100.6 |
| b8758c14-1ca9-3a88-a877-f37647a97bb3 | -4.8397 | -45.3926 | 2026-08-28 02:20:00 | GOES-19 | LAGOA GRANDE DO MARANHÃO | MARANHÃO | Brasil | 2105963 | 21 | 33 | nan | nan | nan | Cerrado | 84.1 |
| fdfaef77-d1b2-3c05-9e6a-4650813590b4 | -7.2659 | -45.8668 | 2026-08-28 02:20:00 | GOES-19 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 279.4 |
| c677971b-8881-3862-b0e9-2961fa93be7e | -7.2474 | -45.846 | 2026-08-28 02:20:00 | GOES-19 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 137.0 |
| 2bbada24-b638-3f3e-8b80-d67dc26fc366 | -7.2661 | -45.8443 | 2026-08-28 02:20:00 | GOES-19 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 154.4 |
| cce1aaa7-9945-37ae-b453-ce467ad40a41 | -16.1638 | -58.6053 | 2026-08-28 02:20:00 | GOES-19 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 153.5 |
| 3568823c-7792-3f79-b82b-848c7198fac0 | -10.4081 | -61.2492 | 2026-08-28 02:20:00 | GOES-19 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 92.7 |
| a0a82c71-ba68-3998-af3e-7fdd8296bb19 | -12.43 | -43.4182 | 2026-08-28 02:20:00 | GOES-19 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 150.2 |
| efc4b2dc-1e2b-33b7-8e7b-0a704a5c245f | -15.5403 | -41.9175 | 2026-08-28 02:20:00 | GOES-19 | SÃO JOÃO DO PARAÍSO | MINAS GERAIS | Brasil | 3162708 | 31 | 33 | nan | nan | nan | Mata Atlântica | 59.9 |
| e5fdf5a5-4299-3e7a-8837-d2cdb6e5e012 | -10.4981 | -64.5005 | 2026-08-28 02:20:00 | GOES-19 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 84.0 |
| bf1cf16a-f9b8-36d4-9a9d-604770003718 | -6.1657 | -57.7793 | 2026-08-28 02:20:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 76.6 |
| 07ccca49-ace8-3813-87dd-9c81cd60ed86 | -8.5968 | -54.7957 | 2026-08-28 02:20:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 40.4 |
| cca88f8c-f340-388c-a3bc-d11487fc7ea4 | -13.4191 | -51.4159 | 2026-08-28 02:20:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 61.1 |
| cc3d0564-cdc7-3403-a9d1-0d10227a6f1d | -6.184 | -57.7981 | 2026-08-28 02:20:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 38.5 |
| 6ced5f90-00c7-379b-b646-2ebcccb8bcd7 | -7.2471 | -45.8685 | 2026-08-28 02:20:00 | GOES-19 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 247.9 |
| 5b15b280-f2e4-3dd8-ae3a-8e45c529ff5e | -10.9367 | -50.5332 | 2026-08-28 02:20:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 80.1 |
| 99d10ce1-a050-3787-a1e9-9b8065e45ae1 | -8.5969 | -54.7755 | 2026-08-28 02:20:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 50.9 |
| 7cc69d73-ff07-32b6-ae21-fb026c5994b5 | -10.3895 | -61.231 | 2026-08-28 02:20:00 | GOES-19 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 165.5 |
| fd4c7808-9e56-34a5-998a-db935993c064 | -6.1472 | -57.7995 | 2026-08-28 02:20:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 64.7 |
| 83b4930b-a5ed-3211-80e4-047df3efc3e2 | -11.2882 | -54.0111 | 2026-08-28 02:20:00 | GOES-19 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 81.3 |
| b6d1fdb0-1809-389e-8173-462e9dc1b001 | -13.3998 | -51.4183 | 2026-08-28 02:20:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 60.2 |
| 3cb8d27f-56fd-33dd-9edb-e4bf28b94ea1 | -11.2317 | -53.9958 | 2026-08-28 02:30:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 61.3 |
| 9f24f18c-43d3-3395-a6d8-ae0f56779475 | -14.8825 | -52.5868 | 2026-08-28 02:30:00 | GOES-19 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 264.2 |
| 0591b2be-7840-3223-ae04-e25eea0b5424 | -10.4981 | -64.5005 | 2026-08-28 02:30:00 | GOES-19 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 77.4 |
| 54cc6c1f-6a0f-3dda-8d73-705d871ae3c1 | -10.7596 | -54.0384 | 2026-08-28 02:30:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 60.5 |
| a7c21df3-6cad-3912-a37f-ac0719f590e0 | -11.8239 | -47.2178 | 2026-08-28 02:30:00 | GOES-19 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 64.5 |
| cb5ec5bc-f03a-3022-93bd-9083e791b735 | -7.2659 | -45.8668 | 2026-08-28 02:30:00 | GOES-19 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 206.0 |
| 38d6a959-af01-3564-8356-99638daf8040 | -14.8631 | -52.5893 | 2026-08-28 02:30:00 | GOES-19 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 300.4 |
| d9a6db7c-47f4-382c-bd12-63099a838e68 | -8.5969 | -54.7755 | 2026-08-28 02:30:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 54.8 |
| b5d8da71-61cd-31b1-9c00-b762e1ef3ba4 | -7.2471 | -45.8685 | 2026-08-28 02:30:00 | GOES-19 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 242.0 |
| 5aebd4a6-55be-393d-b0f6-bb54b1d3613c | -16.1444 | -58.6073 | 2026-08-28 02:30:00 | GOES-19 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 106.7 |
| affec7bf-d65c-32db-8b3a-499882320564 | -14.8821 | -52.608 | 2026-08-28 02:30:00 | GOES-19 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 135.9 |
| 4faadc6d-c1fd-359a-877f-eb712f64382c | -6.1657 | -57.7793 | 2026-08-28 02:30:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 61.0 |
| ab456a94-168f-3906-a3fa-259e592d283e | -11.2879 | -54.0317 | 2026-08-28 02:30:00 | GOES-19 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 90.0 |
| a32419d6-9960-3a00-bde0-0d7d07e6a7f3 | -11.6411 | -46.7265 | 2026-08-28 02:30:00 | GOES-19 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 49.5 |
| df0b99be-ed75-3544-95d3-92b654fd733b | -16.1638 | -58.6053 | 2026-08-28 02:30:00 | GOES-19 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 159.7 |
| 7bdb1208-a807-337d-86a4-dedeb0f17cc1 | -11.2882 | -54.0111 | 2026-08-28 02:30:00 | GOES-19 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 56.1 |
| 82779231-4057-3f5b-b489-8232099ea24f | -10.4081 | -61.2492 | 2026-08-28 02:30:00 | GOES-19 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 79.4 |
| 7f7fb74b-fc51-32b5-abb5-c73e9c712fb4 | -7.2474 | -45.846 | 2026-08-28 02:30:00 | GOES-19 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 126.1 |
| fd4517f9-4168-3f48-b6a9-67478288dd4f | -8.5968 | -54.7957 | 2026-08-28 02:30:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 47.4 |
| d06599e5-3c70-3200-a985-1c7c34ab527b | -12.43 | -43.4182 | 2026-08-28 02:30:00 | GOES-19 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 134.5 |
| 6fbadbbe-3380-37ea-a953-e3b68cf9f7b4 | -4.8583 | -45.3915 | 2026-08-28 02:30:00 | GOES-19 | LAGOA GRANDE DO MARANHÃO | MARANHÃO | Brasil | 2105963 | 21 | 33 | nan | nan | nan | Cerrado | 62.8 |
| aee4d510-992c-37cd-ad98-d9bba602ffa0 | -6.1656 | -57.7988 | 2026-08-28 02:30:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 94.2 |


[Clique aqui para ver as próximas entradas](README11.md)
