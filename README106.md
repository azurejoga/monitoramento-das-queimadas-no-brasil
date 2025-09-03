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

## Dados Diários - Página 106

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 3514c414-eec7-3f22-9205-6d9bd3009818 | -11.853 | -51.53396 | 2025-09-03 05:36:00 | NOAA-20 | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| d05d0f92-e06a-3876-8a90-ad9a2e23ba83 | -10.45369 | -53.62031 | 2025-09-03 05:36:00 | NOAA-20 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 2fdd9059-833b-3e5f-a044-1e6eaebf15a1 | -11.67007 | -57.35509 | 2025-09-03 05:36:00 | NOAA-20 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 5.5 |
| e623bcbe-a6b0-3b2a-96a6-112c46d2457b | -12.94464 | -56.97431 | 2025-09-03 05:36:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 10ac0b79-3759-3e1d-beac-fb8848176ded | -12.90196 | -56.94966 | 2025-09-03 05:36:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| eeb3d6d2-236b-34c4-ae78-c0dd32f0323e | -7.55166 | -61.34157 | 2025-09-03 05:36:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| da8ef3bf-70cb-37e0-9d28-af0c2c9582d9 | -7.54753 | -61.34504 | 2025-09-03 05:36:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 2.8 |
| a23bdd29-0d8a-39ce-af06-6bab8690ef41 | -11.65507 | -57.3561 | 2025-09-03 05:36:00 | NOAA-20 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| f829b85e-3020-3a8d-9151-91e0285cc92d | -11.62449 | -52.13298 | 2025-09-03 05:36:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 1dbf1b3d-132b-30e8-94f5-ce84b6906355 | -12.975 | -54.76826 | 2025-09-03 05:36:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 74d97dd9-11ec-363d-9aaa-3a03b251ce03 | -11.59703 | -52.10823 | 2025-09-03 05:36:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 8.7 |
| 63812fe8-21af-37b9-92bd-6c01304fad25 | -11.66463 | -57.35965 | 2025-09-03 05:36:00 | NOAA-20 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 55d4d70e-56b2-319c-ae16-4ab19856d8d2 | -11.61856 | -52.06564 | 2025-09-03 05:36:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| e9d707eb-3cea-3c63-a0e0-69e72ac54015 | -11.85227 | -51.42535 | 2025-09-03 05:36:00 | NOAA-20 | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 29eff429-0e8c-38b8-9f23-208da9a2cf52 | -7.54813 | -61.34105 | 2025-09-03 05:36:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 2.8 |
| fdeeaf51-c571-3434-9e2e-4c5868174856 | -7.54085 | -61.34106 | 2025-09-03 05:36:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 88ad0714-409c-3b5b-874a-7d747e0a4998 | -11.60573 | -52.11872 | 2025-09-03 05:36:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| c55d6008-47e1-36ed-aced-7ef02da15358 | -10.92237 | -50.86071 | 2025-09-03 05:36:00 | NOAA-20 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 3.4 |
| fc8d3640-e220-3889-98ac-36b264814b56 | -6.92511 | -62.94551 | 2025-09-03 05:36:00 | NOAA-20 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 0.3 |
| 61ce230a-e9ec-316a-be6f-4ab4e5854250 | -12.62675 | -56.99264 | 2025-09-03 05:36:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 62e4c8a3-3298-33f0-a500-d5026007d438 | -12.94179 | -56.95639 | 2025-09-03 05:36:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 6.6 |
| 78a6bd11-087b-30e2-9979-df28f30f729a | -11.02588 | -51.48537 | 2025-09-03 05:36:00 | NOAA-20 | PORTO ALEGRE DO NORTE | MATO GROSSO | Brasil | 5106778 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 29d4fc4f-2ffe-376f-a15e-28a305e21a2c | -12.91922 | -56.9343 | 2025-09-03 05:36:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 0c9a5b27-692d-3c58-9284-7ac53c6403b6 | -7.5499 | -61.32911 | 2025-09-03 05:36:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 8c6683ba-ed36-37d7-8e03-ebc92f69f676 | -11.60505 | -52.12469 | 2025-09-03 05:36:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| dc0800e8-2d21-39b4-bfce-d72631679a16 | -10.09481 | -54.76278 | 2025-09-03 05:36:00 | NOAA-20 | MATUPÁ | MATO GROSSO | Brasil | 5105606 | 51 | 33 | nan | nan | nan | Amazônia | 3.7 |
| f8f16e53-06d7-314e-92b0-b51ed68a1520 | -9.27309 | -59.75127 | 2025-09-03 05:36:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 1d09f101-087d-3837-9878-502183d2721d | -11.59769 | -52.12978 | 2025-09-03 05:36:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 88cefcb5-9f0e-3675-ac4a-1189adf40232 | -7.54852 | -61.3381 | 2025-09-03 05:36:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| c50b034f-7713-3ebd-86c2-93de536a74bc | -12.92039 | -57.00608 | 2025-09-03 05:36:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 7d4c1c51-24d7-3c9d-96e5-dc59bd0c68cf | -10.47063 | -53.63202 | 2025-09-03 05:36:00 | NOAA-20 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| a8cdee90-3800-37ea-9bdc-44bd10f8bd57 | -12.90755 | -56.94549 | 2025-09-03 05:36:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 681b2369-068e-31fe-b410-500bbbd03cc6 | -7.54316 | -61.34951 | 2025-09-03 05:36:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 93d2ae21-3c62-3a3c-b2df-1a5f0f407646 | -10.44768 | -53.61937 | 2025-09-03 05:36:00 | NOAA-20 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| b3265eb7-bf7d-3a2a-800d-353d32f75896 | -7.76125 | -61.1997 | 2025-09-03 05:36:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| ca024314-e691-39af-be3b-34ae5207990f | -11.5836 | -52.10678 | 2025-09-03 05:36:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 3111e8df-a8ea-301d-8a06-c51fbba58806 | -7.54499 | -61.3376 | 2025-09-03 05:36:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 36cb8a3d-3c37-3f27-a77f-1399695f430c | -12.91953 | -56.93074 | 2025-09-03 05:36:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 7e8d7e78-feee-3be4-9529-7248db679025 | -11.58493 | -52.12243 | 2025-09-03 05:36:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 10.9 |
| 2d61ad7d-c07d-3aa5-b071-5e27eac00d1d | -10.24829 | -61.765 | 2025-09-03 05:36:00 | NOAA-20 | JI-PARANÁ | RONDÔNIA | Brasil | 1100122 | 11 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 21ea4b15-8677-3900-8cb3-914a7c0a0eb3 | -11.85141 | -51.41766 | 2025-09-03 05:36:00 | NOAA-20 | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Cerrado | 2.9 |
| ea866a6c-7572-32be-89c7-2c9003eba1e8 | -11.59031 | -52.10754 | 2025-09-03 05:36:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 8.7 |
| 95250457-ac6d-3812-a965-a7461c89ee91 | -10.24769 | -61.76905 | 2025-09-03 05:36:00 | NOAA-20 | JI-PARANÁ | RONDÔNIA | Brasil | 1100122 | 11 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 8cd203f5-1cbc-38c1-932a-41e946660906 | -6.94187 | -62.99136 | 2025-09-03 05:36:00 | NOAA-20 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| a1990eb7-aa95-30dd-96c6-0e8fd2f92c9d | -7.5473 | -61.34607 | 2025-09-03 05:36:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 199383a8-da20-34f0-a9e1-f79790c3a6a8 | -14.32868 | -60.34062 | 2025-09-03 05:38:00 | NOAA-20 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 7edf6306-fffd-34ad-a443-7cb30f018eff | -15.72458 | -53.64302 | 2025-09-03 05:38:00 | NOAA-20 | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 4745a5bc-3e5e-3f86-9c02-98d7de1f36ca | -15.71867 | -53.63714 | 2025-09-03 05:38:00 | NOAA-20 | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 99aa3f59-9cf2-3bba-8e4a-31c2ec964e7d | -14.34368 | -52.80389 | 2025-09-03 05:38:00 | NOAA-20 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 235ccf49-ecae-3ffe-9fc4-3748bca99dc6 | -14.30075 | -53.09411 | 2025-09-03 05:38:00 | NOAA-20 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| dd97f09d-48a7-3b9f-b509-e539a45fe5d3 | -14.34424 | -52.79846 | 2025-09-03 05:38:00 | NOAA-20 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| ee828d6a-42a6-3b1b-911a-88514a2ab5d5 | -16.29473 | -52.95845 | 2025-09-03 05:38:00 | NOAA-20 | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 3.1 |
| c6122496-ccd2-38eb-a4af-3ac164630fd0 | -16.03491 | -59.76441 | 2025-09-03 05:38:00 | NOAA-20 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 2ba089ba-4f41-39e8-aea8-1fe48369a711 | -15.16371 | -52.35689 | 2025-09-03 05:38:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 7d54ce2d-dac4-3b0a-99f9-a79683b40e54 | -14.35211 | -52.80847 | 2025-09-03 05:38:00 | NOAA-20 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 970fbd3e-8247-3460-96fd-0ba5e46753e2 | -14.33268 | -60.34172 | 2025-09-03 05:38:00 | NOAA-20 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 6138766d-cfbb-3f5e-bc27-735d37c1d871 | -14.8451 | -60.04697 | 2025-09-03 05:38:00 | NOAA-20 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 0544b03a-d242-3a93-8717-c2354e54cb2a | -15.71612 | -53.64595 | 2025-09-03 05:38:00 | NOAA-20 | GENERAL CARNEIRO | MATO GROSSO | Brasil | 5103908 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 95b62151-7b65-3c60-a58f-3c9722beb277 | -14.34548 | -52.80763 | 2025-09-03 05:38:00 | NOAA-20 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 97238aeb-5bc8-3512-b386-12c9ce679f86 | -14.3077 | -53.0929 | 2025-09-03 05:38:00 | NOAA-20 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 7c6377e5-350e-3131-9d12-087c5d9b7464 | -15.71812 | -53.64274 | 2025-09-03 05:38:00 | NOAA-20 | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| c9da9f49-349d-3e28-8c4a-2491f63ab2d3 | -15.75218 | -53.69093 | 2025-09-03 05:38:00 | NOAA-20 | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 72f078db-fcf0-3c2f-b284-fe93e8dadce8 | -15.14904 | -52.36472 | 2025-09-03 05:38:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 7d4fa24a-e222-3259-9cb4-287d1c124aed | -16.30533 | -52.96011 | 2025-09-03 05:38:00 | NOAA-20 | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 98691fe7-8727-3cc8-bce2-ceb1a9721631 | -15.75272 | -53.68556 | 2025-09-03 05:38:00 | NOAA-20 | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 730cfc66-3a21-3981-a7b4-14a63901c6cf | -16.29812 | -52.96437 | 2025-09-03 05:38:00 | NOAA-20 | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 37fd278e-7399-3635-a16c-be260da73926 | -14.32471 | -60.33941 | 2025-09-03 05:38:00 | NOAA-20 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 89b925dd-0400-3f3c-b570-c80656e38b81 | -15.71755 | -53.64856 | 2025-09-03 05:38:00 | NOAA-20 | GENERAL CARNEIRO | MATO GROSSO | Brasil | 5103908 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 62bb38a9-4950-3e43-860e-05fbfa49b94d | -14.35033 | -52.80463 | 2025-09-03 05:38:00 | NOAA-20 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 6523cba3-62ae-32a1-9945-e60e0262cb46 | -15.72399 | -53.64896 | 2025-09-03 05:38:00 | NOAA-20 | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 17863539-bfbe-3579-a49c-e9acb684cf67 | -15.57552 | -54.32216 | 2025-09-03 05:38:00 | NOAA-20 | PRIMAVERA DO LESTE | MATO GROSSO | Brasil | 5107040 | 51 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 3792bf89-2d6a-35ff-afd8-119998c0dffc | -16.30806 | -52.96113 | 2025-09-03 05:38:00 | NOAA-20 | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 31b23887-5d55-356c-94cc-5849097d2c6c | -16.30756 | -52.96654 | 2025-09-03 05:38:00 | NOAA-20 | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| f2b8beae-e781-36f3-869a-274e0d5fb21b | -16.29142 | -52.96352 | 2025-09-03 05:38:00 | NOAA-20 | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| f02833e0-96db-349f-b684-b3f70d7e5ec0 | -16.2942 | -52.96425 | 2025-09-03 05:38:00 | NOAA-20 | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 1382c744-1a88-311b-adda-5ebeef20e705 | -14.34666 | -52.79676 | 2025-09-03 05:38:00 | NOAA-20 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 29bb7fc6-596c-3863-806d-1e8229da9a42 | -15.72256 | -53.64637 | 2025-09-03 05:38:00 | NOAA-20 | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 621c14d9-cb1f-36ac-8c33-e0005bf245fc | -14.34608 | -52.80214 | 2025-09-03 05:38:00 | NOAA-20 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 69b00260-e325-3620-ac72-1e0c974a954e | -15.71672 | -53.64024 | 2025-09-03 05:38:00 | NOAA-20 | GENERAL CARNEIRO | MATO GROSSO | Brasil | 5103908 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 5b46478c-67d2-35ff-8672-b9be237d9bb3 | -15.73935 | -53.68983 | 2025-09-03 05:38:00 | NOAA-20 | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | 3.1 |
| fb970b24-7ac4-3aa0-a902-634b31e68f1b | -15.58174 | -54.32214 | 2025-09-03 05:38:00 | NOAA-20 | POXORÉU | MATO GROSSO | Brasil | 5107008 | 51 | 33 | nan | nan | nan | Cerrado | 3.0 |
| b782cd5b-e252-32d0-b230-eea2659e2643 | -14.34976 | -52.81017 | 2025-09-03 05:38:00 | NOAA-20 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| cc8139a9-f2fd-3b08-9082-0ee34938f76f | -14.30001 | -53.10291 | 2025-09-03 05:38:00 | NOAA-20 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 79e5cbcc-3f95-3a0e-a378-0204f4db6e70 | -15.16293 | -52.36479 | 2025-09-03 05:38:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| b03bb556-1a55-349a-8a43-d4d3253ad4a7 | -15.73707 | -53.69265 | 2025-09-03 05:38:00 | NOAA-20 | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 26c14626-718b-323c-9a71-dbe16c9ed5d4 | -14.30061 | -53.09739 | 2025-09-03 05:38:00 | NOAA-20 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| a8bfb2f6-3b13-3946-b4d1-cafcb3690736 | -14.30019 | -53.09955 | 2025-09-03 05:38:00 | NOAA-20 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 520af8bd-547f-3c89-acc6-def41711ab5a | -15.74576 | -53.69044 | 2025-09-03 05:38:00 | NOAA-20 | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 5651bb17-60dc-3259-b3e1-e6d2e9dca710 | -16.29202 | -52.95747 | 2025-09-03 05:38:00 | NOAA-20 | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 90cdd6c0-6471-3799-87ac-a21669e40118 | -16.3014 | -52.95976 | 2025-09-03 05:38:00 | NOAA-20 | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 6474acb8-d3d4-37e8-beef-fc3e67b0eaaa | -14.35088 | -52.79917 | 2025-09-03 05:38:00 | NOAA-20 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| ede3c116-46ba-3bd4-b7f8-1e9e00a2d384 | -16.30479 | -52.96554 | 2025-09-03 05:38:00 | NOAA-20 | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 301c8d8b-eb4b-3a08-9cd8-dc44efee48cc | -15.74792 | -53.66892 | 2025-09-03 05:38:00 | NOAA-20 | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 4b4dfa7e-09cb-315b-bdbc-0ed556a0836b | -15.74628 | -53.68521 | 2025-09-03 05:38:00 | NOAA-20 | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 7a3a8c33-3688-34d5-94fe-483bd82f91d6 | -15.72319 | -53.64043 | 2025-09-03 05:38:00 | NOAA-20 | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| a9e6ef21-630a-348c-a60c-bd6d95780893 | -20.94533 | -54.95764 | 2025-09-03 05:38:00 | NOAA-20 | SIDROLÂNDIA | MATO GROSSO DO SUL | Brasil | 5007901 | 50 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 21817a75-ecb1-3994-aa78-ade049c67229 | -15.74155 | -53.66785 | 2025-09-03 05:38:00 | NOAA-20 | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 64ba44dd-5a44-3156-ac68-6a2ca717288a | -16.30089 | -52.96529 | 2025-09-03 05:38:00 | NOAA-20 | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| b8b88d7f-906b-3b79-a66a-6b547e45955a | -15.74523 | -53.69563 | 2025-09-03 05:38:00 | NOAA-20 | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 70bbbe42-b57c-387f-a3af-c9a29b79ebbd | -7.5476 | -61.3437 | 2025-09-03 05:40:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 61.8 |


[Clique aqui para ver as próximas entradas](README107.md)
