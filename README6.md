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
| 7969785c-1bb2-3852-9a13-56c72103e209 | -9.7177 | -54.8162 | 2026-09-18 00:10:00 | GOES-19 | GUARANTÃ DO NORTE | MATO GROSSO | Brasil | 5104104 | 51 | 33 | nan | nan | nan | Amazônia | 57.1 |
| 0f499e8d-389e-3fc9-b512-edb6395b9fab | -4.5587 | -42.9523 | 2026-09-18 00:10:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 446.9 |
| f6dc17b1-0eeb-348a-b119-89fdae7427bc | -12.2821 | -50.7654 | 2026-09-18 00:10:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 187.1 |
| c52bddf7-6edf-38ec-a60a-e327679e5fe8 | -6.1358 | -59.9638 | 2026-09-18 00:10:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 72.8 |
| 7fdefea6-12ba-3e91-84ec-1b42bcb4810c | -12.263 | -50.7677 | 2026-09-18 00:10:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 223.7 |
| e07364b9-35e1-3335-91fa-40eec07231d2 | -10.6153 | -46.5675 | 2026-09-18 00:10:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 63.0 |
| 5172cf9f-593d-31b1-9a10-64f18f904884 | -12.3394 | -50.7586 | 2026-09-18 00:10:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 118.9 |
| 3a07c3a3-ddce-3877-b5f0-b8794c4ac3d8 | -11.2787 | -43.3643 | 2026-09-18 00:10:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 223.0 |
| 5379e7f1-490b-33b9-8266-e7120f31273d | -3.4455 | -58.2134 | 2026-09-18 00:10:00 | GOES-19 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 85.2 |
| 952c76a5-d678-3522-aa53-3dcf5e95a988 | -2.81 | -50.4868 | 2026-09-18 00:10:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 67.2 |
| 4f645fc6-daea-38d4-a1d3-2705040c5db4 | -9.0934 | -45.7088 | 2026-09-18 00:10:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 75.5 |
| 0d629e34-f933-37f6-83ae-89ba436451f2 | -3.0465 | -51.3755 | 2026-09-18 00:10:00 | GOES-19 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 68.0 |
| 89b7bf2d-1316-36f9-8a9f-917149e5ff74 | -15.7951 | -52.5682 | 2026-09-18 00:10:00 | GOES-19 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 84.4 |
| 92a84e6b-91a1-36b9-9249-181d5d484938 | -12.3397 | -50.7371 | 2026-09-18 00:10:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 73.0 |
| e919510f-2d61-354b-bab7-5de1f00971db | -5.7382 | -45.0853 | 2026-09-18 00:10:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 69.0 |
| c6616cdf-f29f-3a3d-9f2e-e36eaad07c5e | -12.4551 | -50.6804 | 2026-09-18 00:10:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 105.6 |
| bca73abd-a45f-337c-adb9-1a2a3dde07fc | -12.6427 | -50.893 | 2026-09-18 00:10:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 88.8 |
| 7a637b90-1686-387e-9223-a4221240497d | -19.1812 | -48.7717 | 2026-09-18 00:10:00 | GOES-19 | PRATA | MINAS GERAIS | Brasil | 3152808 | 31 | 33 | nan | nan | nan | Cerrado | 120.7 |
| efffdf4b-78ba-3261-bdfa-ff613605a26a | -5.7569 | -45.084 | 2026-09-18 00:10:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 167.0 |
| f0875a2e-f52c-3fab-8d36-e31b2a6ef4ed | -6.5174 | -49.8944 | 2026-09-18 00:10:00 | GOES-19 | CANAÃ DOS CARAJÁS | PARÁ | Brasil | 1502152 | 15 | 33 | nan | nan | nan | Amazônia | 73.6 |
| 7ad5a6ed-e490-3437-a84b-00b8bf9158e2 | -15.8146 | -52.5655 | 2026-09-18 00:10:00 | GOES-19 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 94.7 |
| 972adcbe-e649-331f-b238-e1bd3721be1e | -4.5585 | -42.9758 | 2026-09-18 00:10:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 167.8 |
| fa9ebb7e-fda6-3766-bb86-01edc0e10d7b | -2.8101 | -50.4658 | 2026-09-18 00:10:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 105.0 |
| 44dfd478-7729-3f82-baee-e0c4c22ea280 | -4.5776 | -42.9277 | 2026-09-18 00:10:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 199.6 |
| 61b1eaf9-541e-37b8-8cc5-0aa24dd2a88c | -4.5774 | -42.9512 | 2026-09-18 00:10:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1172.5 |
| 5b65095c-86e8-3fea-a3a9-e8c608a48462 | -5.7431 | -57.5814 | 2026-09-18 00:10:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 98.6 |
| 0797969b-db09-302d-966c-87e6d22d3dbd | -6.1109 | -57.684 | 2026-09-18 00:10:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 60.3 |
| ae6b2b16-8de1-31bd-9257-0ffb2a60dffc | -12.3002 | -50.8274 | 2026-09-18 00:10:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 87.0 |
| 536f5ab4-a0e8-3a2b-986a-26d6ce375233 | -12.643 | -50.8716 | 2026-09-18 00:10:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 82.2 |
| 1fbad3c6-83bc-35bd-9173-4f631b21447d | -12.3193 | -50.8251 | 2026-09-18 00:10:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 73.0 |
| b1c801f1-fb6b-3556-8c20-93406f078ae3 | -11.2971 | -43.4088 | 2026-09-18 00:10:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 89.6 |
| 125efa93-a100-3169-8742-31789a05ef49 | -4.55 | -42.93 | 2026-09-18 00:15:00 | MSG-03 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| bb86fdde-d434-3d22-ab58-dab56a4971c7 | -4.55 | -42.97 | 2026-09-18 00:15:00 | MSG-03 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 6a952ae3-3552-3df4-b745-ac7cdf4d7e1c | -12.27 | -50.78 | 2026-09-18 00:15:00 | MSG-03 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 7c332ea8-1aa3-328c-90de-c5f832353235 | -4.58 | -42.93 | 2026-09-18 00:15:00 | MSG-03 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| d91a1827-963a-3e4d-86b1-4c36cbdda745 | -11.3 | -43.41 | 2026-09-18 00:15:00 | MSG-03 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 0ba31b8d-707e-3b10-bb67-4b558a61cfff | -4.58 | -42.97 | 2026-09-18 00:15:00 | MSG-03 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 15a7087a-d942-35af-9d6e-202d5df87268 | -11.3 | -43.36 | 2026-09-18 00:15:00 | MSG-03 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 2071d619-1bc5-3276-a83b-ad40ed81a68d | -12.24 | -50.77 | 2026-09-18 00:15:00 | MSG-03 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 3e6054ff-032d-3176-9476-1fd32a590680 | -12.5341 | -47.0964 | 2026-09-18 00:20:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 94.1 |
| d27bc98f-615e-3527-b8a3-0d8465c8083d | -17.8054 | -53.1249 | 2026-09-18 00:20:00 | GOES-19 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 180.9 |
| 262ff4c2-c0ef-3470-a4f0-4e8da3417145 | -15.7951 | -52.5682 | 2026-09-18 00:20:00 | GOES-19 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 138.4 |
| cc7381a0-6b62-38ab-a5ae-69610f66d3c6 | -4.5772 | -42.9746 | 2026-09-18 00:20:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 429.1 |
| 92472ba4-537c-3540-a9cc-90433c143967 | -3.4455 | -58.2134 | 2026-09-18 00:20:00 | GOES-19 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 80.4 |
| b7d82b87-2582-3513-bc86-bc91da230a9c | -4.5961 | -42.95 | 2026-09-18 00:20:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 216.3 |
| 9755df1b-2d90-3883-8876-3b2771131dfb | -2.8285 | -50.4653 | 2026-09-18 00:20:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 69.1 |
| 8a0871da-b32d-3a58-b519-9bfa1f5337a0 | -8.9479 | -51.4618 | 2026-09-18 00:20:00 | GOES-19 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 51.7 |
| 1ef8849e-0539-3888-9924-2eb898e47a11 | -6.1175 | -59.9452 | 2026-09-18 00:20:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 61.4 |
| 57014f50-3ae5-3a95-be56-2bd7dcd48eef | -3.3638 | -50.4492 | 2026-09-18 00:20:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 135.5 |
| 5f347c0f-f07b-3ef6-abd8-a0f422650be7 | -12.3206 | -50.7394 | 2026-09-18 00:20:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 88.6 |
| 343ab48b-2395-3522-89a3-25c9ecc03d0f | -4.5585 | -42.9758 | 2026-09-18 00:20:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 185.6 |
| c9a08fd2-a70a-3af4-a00d-b273a8d7b912 | -3.0465 | -51.3755 | 2026-09-18 00:20:00 | GOES-19 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 73.8 |
| c4ae57de-ef6c-3836-9068-d25eaca9960d | -6.1359 | -59.9446 | 2026-09-18 00:20:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 81.7 |
| 3a53270c-85d8-30ae-ab7a-dbb8f1b34271 | -12.3394 | -50.7586 | 2026-09-18 00:20:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 125.3 |
| a9173e7b-a525-3a88-aa0b-7a041e4ac23c | -13.7219 | -51.6757 | 2026-09-18 00:20:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 75.5 |
| 5bd8bf58-c6bd-3f76-b9cc-719b5846e9db | -5.7569 | -45.084 | 2026-09-18 00:20:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 185.9 |
| fd3b0bae-4a72-31da-a9ea-466747e09de1 | -15.8146 | -52.5655 | 2026-09-18 00:20:00 | GOES-19 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 131.9 |
| 3f3b960e-9ca2-3dae-ba24-0d797987ba92 | -3.3823 | -50.4486 | 2026-09-18 00:20:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 93.4 |
| 222dbc52-6e0c-34e7-b0ed-2cc1d99ac4e7 | -6.5174 | -49.8944 | 2026-09-18 00:20:00 | GOES-19 | CANAÃ DOS CARAJÁS | PARÁ | Brasil | 1502152 | 15 | 33 | nan | nan | nan | Amazônia | 70.2 |
| ad00782e-f06f-354d-9544-22f761bfc712 | -13.7223 | -51.6544 | 2026-09-18 00:20:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 91.3 |
| f8b2468c-e9d8-31a8-bb0f-41f368cc7e7a | -12.6427 | -50.893 | 2026-09-18 00:20:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 83.0 |
| 6bdc017f-0789-364a-b47a-74360fdd7111 | -4.5776 | -42.9277 | 2026-09-18 00:20:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 91.0 |
| e86994a1-9754-380d-b81b-6aa34f9f1847 | -19.1812 | -48.7717 | 2026-09-18 00:20:00 | GOES-19 | PRATA | MINAS GERAIS | Brasil | 3152808 | 31 | 33 | nan | nan | nan | Cerrado | 102.1 |
| e9bcef44-8165-3eee-941f-50c93551018f | -6.1174 | -59.9644 | 2026-09-18 00:20:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 63.8 |
| f7671f34-7d6d-3cd5-ac0f-81fc8475e94f | -12.263 | -50.7677 | 2026-09-18 00:20:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 165.3 |
| 8208ad16-23d3-34ff-9a05-1f633d581102 | -10.6153 | -46.5675 | 2026-09-18 00:20:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 66.3 |
| 8cf45426-b36d-3ca2-9663-4d368c7e4669 | -4.596 | -42.9734 | 2026-09-18 00:20:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 119.4 |
| b2e06fba-07a7-3b4e-a185-ec15548d46a4 | -12.2633 | -50.7463 | 2026-09-18 00:20:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 82.8 |
| 7bb4849c-04ef-3526-a29d-efd1ff0129d3 | -12.3397 | -50.7371 | 2026-09-18 00:20:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 101.7 |
| 0896ba87-2cc5-3ff3-9815-e022cafbe01d | -6.1358 | -59.9638 | 2026-09-18 00:20:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 83.1 |
| 0463c8e5-9db2-33e0-8a0f-63f48b3fe974 | -6.1109 | -57.684 | 2026-09-18 00:20:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 56.5 |
| 1b1e2aad-0e4a-329d-8ca9-239941be0b34 | -9.0934 | -45.7088 | 2026-09-18 00:20:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 64.6 |
| d0dc510e-2fad-32de-bbd6-0d9373084aed | -3.3637 | -50.4701 | 2026-09-18 00:20:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 47.0 |
| de597de4-260d-317c-b25d-c7c2fd01bfc9 | -17.7856 | -53.1279 | 2026-09-18 00:20:00 | GOES-19 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 106.0 |
| a2f7440e-397d-38ba-bf2f-050fbac298da | -12.2821 | -50.7654 | 2026-09-18 00:20:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 86.3 |
| b5d7fe61-4952-393d-9d40-1895b867d2c0 | -2.8284 | -50.4863 | 2026-09-18 00:20:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 63.0 |
| 6b370c75-2393-3e24-9f2d-91956c299998 | -12.3203 | -50.7608 | 2026-09-18 00:20:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 70.5 |
| aadc89c5-7eaa-3ea8-a6d3-81e6977dc37d | -9.7177 | -54.8162 | 2026-09-18 00:20:00 | GOES-19 | GUARANTÃ DO NORTE | MATO GROSSO | Brasil | 5104104 | 51 | 33 | nan | nan | nan | Amazônia | 79.2 |
| 4ac76b43-4656-3b8a-8638-9296a23424dd | -4.5589 | -42.9289 | 2026-09-18 00:20:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 75.9 |
| 8ee87f3a-c27c-31a1-a3c3-c64da06b3c59 | -4.5177 | -56.0751 | 2026-09-18 00:20:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 95.2 |
| 44c2436d-20c3-35e5-bc24-8be966eda408 | -4.5587 | -42.9523 | 2026-09-18 00:20:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 554.8 |
| 68823268-a4d8-3975-8f71-f6e35be007ba | -17.805 | -53.1464 | 2026-09-18 00:20:00 | GOES-19 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 71.6 |
| da98f525-42f8-3bb2-8cf7-054dfefa2e30 | -5.7567 | -45.1067 | 2026-09-18 00:20:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 130.9 |
| 4662c0d4-e01c-31e5-8abb-e74ef56858ed | -4.5774 | -42.9512 | 2026-09-18 00:20:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 969.2 |
| 4accec1d-870a-3655-b9ee-9600849ea90e | -2.81 | -50.4868 | 2026-09-18 00:20:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 53.4 |
| 40a0f05d-1002-32df-b56c-c6a637e330a1 | -2.8101 | -50.4658 | 2026-09-18 00:20:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 63.2 |
| 05ca7435-5e0e-3a55-9ac9-994cc3d69789 | -4.5589 | -42.9289 | 2026-09-18 00:30:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 85.9 |
| 2a3ff6e6-4df3-3881-8489-471f380ff0d9 | -19.1812 | -48.7717 | 2026-09-18 00:30:00 | GOES-19 | PRATA | MINAS GERAIS | Brasil | 3152808 | 31 | 33 | nan | nan | nan | Cerrado | 111.2 |
| b68b7cfa-9c72-3175-a110-5322645e5d1f | -2.81 | -50.4868 | 2026-09-18 00:30:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 106.9 |
| 666d4823-c52e-369a-8296-603c07c75ca1 | -3.0465 | -51.3755 | 2026-09-18 00:30:00 | GOES-19 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 63.2 |
| d422f743-520d-3c9b-a9c0-6213fff8eefd | -6.1175 | -59.9452 | 2026-09-18 00:30:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 58.2 |
| 85451ce4-859b-3a5a-b591-c88daccd15b1 | -5.7567 | -45.1067 | 2026-09-18 00:30:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 55.8 |
| ae6b5154-f524-39be-8489-1cbf175f5cc1 | -9.7177 | -54.8162 | 2026-09-18 00:30:00 | GOES-19 | GUARANTÃ DO NORTE | MATO GROSSO | Brasil | 5104104 | 51 | 33 | nan | nan | nan | Amazônia | 104.3 |
| c079d85c-4a63-3cb4-bc68-672c33a0720b | -6.5174 | -49.8944 | 2026-09-18 00:30:00 | GOES-19 | CANAÃ DOS CARAJÁS | PARÁ | Brasil | 1502152 | 15 | 33 | nan | nan | nan | Amazônia | 63.8 |
| 983e2fea-6450-3ebc-b657-e2bcb8acefa2 | -12.6235 | -50.8953 | 2026-09-18 00:30:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 93.7 |
| 39ab88c3-4678-384d-b1ab-fd7f72f42dae | -12.6239 | -50.8739 | 2026-09-18 00:30:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 111.4 |
| 18430b53-30f0-36f6-820b-ec114e586cbf | -6.1359 | -59.9446 | 2026-09-18 00:30:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 114.3 |
| daa26388-3faa-318c-8df0-98b4f28b1147 | -5.7569 | -45.084 | 2026-09-18 00:30:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 63.1 |
| 68380a26-eeb0-3e6a-9b8d-6341abfea985 | -4.596 | -42.9734 | 2026-09-18 00:30:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 117.7 |
| 129216f2-7a5c-3b25-9043-47a65019f75e | -3.3823 | -50.4486 | 2026-09-18 00:30:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 81.8 |


[Clique aqui para ver as próximas entradas](README7.md)
