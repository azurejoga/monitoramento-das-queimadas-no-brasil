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

## Dados Diários - Página 12

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 2caee9e8-0734-3fb4-8e45-fc75e614089e | 0.66603 | -60.31039 | 2026-03-05 06:24:00 | NPP-375D | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 04c4ae70-e68d-3b3a-a1db-9ae7a11dc5ef | 0.66596 | -60.30782 | 2026-03-05 06:24:00 | NPP-375D | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 518fec58-fc4f-35f4-a5af-13b5618144d6 | 2.96725 | -61.08942 | 2026-03-05 06:24:00 | NPP-375D | ALTO ALEGRE | RORAIMA | Brasil | 1400050 | 14 | 33 | nan | nan | nan | Amazônia | 1.8 |
| aeb9424b-c77e-3385-a638-565057b9c929 | 2.78614 | -60.34143 | 2026-03-05 06:24:00 | NPP-375D | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 13.4 |
| 1024c90e-347d-36b6-9940-5d81fc9813d5 | 0.03796 | -61.00035 | 2026-03-05 06:24:00 | NPP-375D | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 3a035b7f-d377-3949-a642-1d823514da20 | 1.51036 | -59.91105 | 2026-03-05 06:24:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 76830568-6812-3ad0-a427-1fd68b7a4236 | 3.03423 | -60.81517 | 2026-03-05 06:24:00 | NPP-375D | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 3.1 |
| b33129a0-a40a-31c7-9ee9-b8e540de4d0f | 2.96182 | -61.0955 | 2026-03-05 06:24:00 | NPP-375D | ALTO ALEGRE | RORAIMA | Brasil | 1400050 | 14 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 312d11b2-51ea-3c8a-9643-60fc856a358a | 3.18586 | -60.57284 | 2026-03-05 06:24:00 | NPP-375D | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 2a7f5d8a-5a4a-35a9-9ece-cfe30b6acc65 | 2.72452 | -60.67472 | 2026-03-05 06:24:00 | NPP-375D | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 1.9 |
| a3f7cc07-aca8-3bf5-a148-3740f6f5f64d | 3.18492 | -60.56739 | 2026-03-05 06:24:00 | NPP-375D | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 01d75c10-fd38-3d2e-887a-3531b7931c92 | 2.7816 | -60.3528 | 2026-03-05 06:30:00 | GOES-19 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 51.2 |
| de0103c7-7db1-39c2-bd0c-4fc67ab57831 | 2.7816 | -60.3338 | 2026-03-05 06:30:00 | GOES-19 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 83.2 |
| 2e8cac2e-20a7-3445-880c-cc670174d84a | 2.7816 | -60.3528 | 2026-03-05 06:40:00 | GOES-19 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 64.9 |
| dece2fdc-ef04-32a5-a6b8-810593763527 | 2.7816 | -60.3338 | 2026-03-05 06:40:00 | GOES-19 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 92.8 |
| ffc7cacb-ffb5-322a-a361-17de6c9aebac | 2.7816 | -60.3338 | 2026-03-05 06:50:00 | GOES-19 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 90.5 |
| dea27846-377b-31a9-afb3-c741b55f134c | 2.7816 | -60.3528 | 2026-03-05 07:00:00 | GOES-19 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 60.2 |
| 8d3f089b-287e-3cdb-9974-5d8cbf591303 | 2.7816 | -60.3338 | 2026-03-05 07:00:00 | GOES-19 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 86.0 |
| be5caa69-09ad-3df0-bdda-d68324505ba7 | 2.7816 | -60.3338 | 2026-03-05 07:10:00 | GOES-19 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 67.3 |
| 08e3dd94-4db3-328f-9344-94d4f04bd595 | 2.7816 | -60.3338 | 2026-03-05 07:20:00 | GOES-19 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 71.6 |
| a17c3b38-f7d9-317b-beb0-5b8e22e0af64 | 2.7816 | -60.3528 | 2026-03-05 07:30:00 | GOES-19 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 62.0 |
| ad1f2b49-5d1e-3c06-8c00-13be2f9cf9fc | 2.7816 | -60.3338 | 2026-03-05 07:30:00 | GOES-19 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 91.2 |
| 7a780039-c8c0-3188-9ebe-31fea738b499 | 2.7816 | -60.3528 | 2026-03-05 07:40:00 | GOES-19 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 64.4 |
| 2877e4f2-cb88-324a-b9e3-69eb74e7a40c | 2.7816 | -60.3338 | 2026-03-05 07:40:00 | GOES-19 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 91.8 |
| 857a6724-0ba4-3399-b2f6-a3c00c56dde0 | 2.7816 | -60.3528 | 2026-03-05 07:50:00 | GOES-19 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 58.7 |
| 7c76f46c-ba60-327a-bb45-190309b06b0b | 2.7816 | -60.3338 | 2026-03-05 07:50:00 | GOES-19 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 92.4 |
| 4ffd004e-6ad9-3c14-ae77-d022f1b6887b | 2.77694 | -60.33198 | 2026-03-05 07:50:00 | AQUA_M-M | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 28.9 |
| 6deebde7-aa73-3be9-9f91-05e56d251022 | 2.79171 | -60.32973 | 2026-03-05 07:50:00 | AQUA_M-M | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 119.4 |
| 5dff07a8-1330-34c3-be12-e1b0f45cadbc | 2.78811 | -60.309 | 2026-03-05 07:50:00 | AQUA_M-M | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 32.4 |
| 5cceed1a-eaa9-3050-a027-39ee670f3722 | 2.77761 | -60.33892 | 2026-03-05 07:50:00 | AQUA_M-M | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 17.4 |
| fcca5d0b-ffc4-3dae-aa72-20b970b216ca | 0.0475 | -60.96754 | 2026-03-05 07:50:00 | AQUA_M-M | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 23.2 |
| 1f6a2f47-eb51-32c9-a58f-26a10c3121da | 2.79237 | -60.33662 | 2026-03-05 07:50:00 | AQUA_M-M | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 122.2 |
| 04cefb5d-8c06-3e37-8ba2-0d974c3abfe3 | 2.7816 | -60.3528 | 2026-03-05 08:00:00 | GOES-19 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 57.5 |
| 85d28e36-0e37-39de-bbee-a4799a0b8808 | 2.7816 | -60.3338 | 2026-03-05 08:00:00 | GOES-19 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 79.8 |
| 5ac35317-4ba2-3485-9866-85af9367a206 | 2.7816 | -60.3338 | 2026-03-05 08:10:00 | GOES-19 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 63.8 |
| 8c842d04-d9d7-324d-ab40-ffa46c5b2c15 | 2.7816 | -60.3528 | 2026-03-05 08:20:00 | GOES-19 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 50.8 |
| 011085c8-2092-352a-8b56-c69eb5d26a9d | 2.7816 | -60.3338 | 2026-03-05 08:20:00 | GOES-19 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 69.8 |
| 476b521f-ca53-32c7-9285-af9e15cefb49 | 2.7816 | -60.3338 | 2026-03-05 08:30:00 | GOES-19 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 54.7 |
| 114f2f54-5031-33b4-82c6-6e77d9e709df | 2.7816 | -60.3338 | 2026-03-05 12:10:00 | GOES-19 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 77.5 |
| 7f0102bb-4362-3117-abec-283ad53d1475 | 2.7816 | -60.3338 | 2026-03-05 12:20:00 | GOES-19 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 71.3 |
| 9d98054c-3e7c-35d8-b747-4526cf6e1080 | 2.6896 | -60.6578 | 2026-03-05 12:30:00 | GOES-19 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 77.2 |
| 4cd1e83c-13ac-3a49-84c9-b35eb4f2281d | 2.7816 | -60.3338 | 2026-03-05 12:30:00 | GOES-19 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 69.0 |
| 6e463655-3319-3cd4-a7bc-8906d59238c9 | 2.7817 | -60.3148 | 2026-03-05 12:40:00 | GOES-19 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 68.0 |
| 164c34c6-1a54-3b82-a648-dac74cb831fa | 2.7816 | -60.3338 | 2026-03-05 12:40:00 | GOES-19 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 105.0 |
| ede75ddb-f299-3384-8d74-67c767f769c5 | 2.7817 | -60.3148 | 2026-03-05 12:50:00 | GOES-19 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 70.0 |
| 1087128d-4474-3575-a136-5e718f657832 | 2.7816 | -60.3338 | 2026-03-05 12:50:00 | GOES-19 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 108.8 |
| 07689b13-f90a-356a-9d0c-37483e7a2689 | 2.7817 | -60.3148 | 2026-03-05 13:00:00 | GOES-19 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 68.1 |
| 6e40752b-f6cd-363f-82fc-b4c879e8f76d | 2.7816 | -60.3338 | 2026-03-05 13:00:00 | GOES-19 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 92.5 |
| 8e962723-cd4f-3b22-955d-90955ec04fbf | 3.0179 | -60.8233 | 2026-03-05 13:10:00 | GOES-19 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 116.6 |
| 24b4dcff-64ae-3e3e-b950-8f4052a61952 | 3.0362 | -60.823 | 2026-03-05 13:10:00 | GOES-19 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 73.6 |
| 33539660-b2c0-3fe0-883f-1090b58f5506 | 2.7817 | -60.3148 | 2026-03-05 13:10:00 | GOES-19 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 75.0 |
| 3d2f2887-992d-3698-9331-d733b73624e9 | 2.7816 | -60.3338 | 2026-03-05 13:10:00 | GOES-19 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 101.9 |
| 9ad29ae2-cb70-39ff-adec-c6030e3539a3 | 2.7817 | -60.3148 | 2026-03-05 13:20:00 | GOES-19 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 110.7 |
| 03c814bf-325f-3bd4-afdf-d935c8defc64 | 3.0362 | -60.8041 | 2026-03-05 13:20:00 | GOES-19 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 86.0 |
| eb859c30-8a62-34d1-b13f-8ecb83e62eaa | 2.6896 | -60.6578 | 2026-03-05 13:20:00 | GOES-19 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 68.2 |
| ae1b0980-838e-3346-8a6f-83b3b945db00 | 2.7816 | -60.3338 | 2026-03-05 13:20:00 | GOES-19 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 157.8 |
| 6b034545-9835-3220-af6b-76b09c017a27 | 3.0179 | -60.8233 | 2026-03-05 13:20:00 | GOES-19 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 98.9 |
| 51ed8db6-2991-3603-9b35-c017eaf00fe0 | 3.0362 | -60.823 | 2026-03-05 13:20:00 | GOES-19 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 79.4 |
| 9bbec47e-efe9-3102-bb86-be895b5b3f26 | 2.7817 | -60.3148 | 2026-03-05 13:30:00 | GOES-19 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 130.9 |
| 0cd27ce0-b1d6-3769-9e6f-467dde6aae0a | 2.7816 | -60.3338 | 2026-03-05 13:30:00 | GOES-19 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 172.9 |
| 23d60c38-00e6-3cf7-a27d-69d4465cfb59 | 3.0183 | -60.6528 | 2026-03-05 13:40:00 | GOES-19 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 83.1 |
| 8f62701a-f239-31f5-8889-fa18337ef8a1 | 2.7817 | -60.3148 | 2026-03-05 13:40:00 | GOES-19 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 136.5 |
| 4d80e5de-86ed-33e0-849b-5c8e040931b8 | 2.7816 | -60.3338 | 2026-03-05 13:40:00 | GOES-19 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 178.2 |
| 3274a278-39dc-3244-b23e-e2b2d5b7c580 | 3.0184 | -60.6338 | 2026-03-05 13:40:00 | GOES-19 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 71.9 |
| 8880740e-943c-3ae3-88c9-f41b2c6cb22b | 2.6896 | -60.6578 | 2026-03-05 13:40:00 | GOES-19 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 82.7 |
| 198f07e3-d1d7-39c8-b11f-adadfd4569e2 | 2.6896 | -60.6768 | 2026-03-05 13:50:00 | GOES-19 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 74.3 |
| 2a95f588-f0ae-3bed-a79f-40ff7a6b2fe5 | 2.7817 | -60.3148 | 2026-03-05 13:50:00 | GOES-19 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 147.2 |
| f2bee17e-c8b5-39c6-b7d3-2333fd3a2a62 | 2.6896 | -60.6578 | 2026-03-05 13:50:00 | GOES-19 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 111.2 |
| 3a4c771c-b145-3263-9bb4-acb9db93d8c1 | 2.7816 | -60.3338 | 2026-03-05 13:50:00 | GOES-19 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 162.1 |
| 019d38f6-5f3a-34b9-aaee-22d52123e51d | 2.7079 | -60.6575 | 2026-03-05 13:50:00 | GOES-19 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 68.1 |
| 40924ce1-a4fa-32de-b10a-214a1ea182eb | 2.6896 | -60.6578 | 2026-03-05 14:00:00 | GOES-19 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 70.0 |
| 5acca873-6e30-3092-be5a-ff6823af8fb2 | 2.7817 | -60.3148 | 2026-03-05 14:00:00 | GOES-19 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 500.5 |
| 4de24520-dc45-322d-8b7c-aab7eec07fc1 | 2.7816 | -60.3338 | 2026-03-05 14:00:00 | GOES-19 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 415.6 |
| 53652904-f008-3747-918e-e06a9a67e83a | 3.0179 | -60.8233 | 2026-03-05 14:00:00 | GOES-19 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 69.7 |
| 134f665d-3b8e-321b-a7d1-7d1e1d5714df | 1.1572 | -60.8818 | 2026-03-05 14:10:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 74.9 |
| da2530ff-450d-3847-a792-7ecebb1aca4b | 2.7816 | -60.3338 | 2026-03-05 14:10:00 | GOES-19 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 311.2 |
| e594dfdb-0af8-3ee6-8851-ce46ea25515f | 2.7817 | -60.3148 | 2026-03-05 14:10:00 | GOES-19 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 275.5 |
| ca6a3497-d38a-37f3-b9cf-1e13f9998a04 | 2.6896 | -60.6578 | 2026-03-05 14:10:00 | GOES-19 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 71.5 |
| c3722d6f-3df5-372f-b5ad-01db3b8d3cde | 2.7816 | -60.3528 | 2026-03-05 14:30:00 | GOES-19 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 86.9 |
| fd2c7263-9b57-3101-aac3-92cd5b13d6d2 | 2.7816 | -60.3338 | 2026-03-05 14:30:00 | GOES-19 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 213.2 |
| 062f491f-d380-3037-828c-25d72fad51ae | 2.7817 | -60.3148 | 2026-03-05 14:30:00 | GOES-19 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 168.4 |
| 2c3bae3c-86cb-36f2-8e3b-603066d44cc9 | 2.6896 | -60.6578 | 2026-03-05 14:30:00 | GOES-19 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 76.4 |
| 66c5b596-7f0d-35ed-a121-661446605629 | 1.1572 | -60.8818 | 2026-03-05 14:30:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 78.7 |
| eab0fd38-65d9-37e0-b497-0e92d100d2b8 | 1.1572 | -60.9007 | 2026-03-05 14:40:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 78.5 |
| ae82b3f3-db6c-3194-8127-6d7e3e4efea5 | 1.1572 | -60.8818 | 2026-03-05 14:40:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 87.5 |
| e5d3645b-622f-30a1-8fa9-d5a8998f6da0 | 2.7816 | -60.3338 | 2026-03-05 14:40:00 | GOES-19 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 183.7 |
| f7a5fa8b-23b0-31d8-8987-0393781f8ae3 | 2.7816 | -60.3528 | 2026-03-05 14:40:00 | GOES-19 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 98.6 |
| 4b9e915d-323a-3cc5-af28-91bbd9b378b0 | 2.7817 | -60.3148 | 2026-03-05 14:40:00 | GOES-19 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 111.6 |


