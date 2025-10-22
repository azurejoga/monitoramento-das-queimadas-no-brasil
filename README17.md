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

## Dados Diários - Página 17

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 7831f747-c43f-3393-aa27-f8f7cdf52114 | -2.47853 | -49.25949 | 2025-10-22 05:14:00 | NOAA-20 | MOCAJUBA | PARÁ | Brasil | 1504604 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 17842e54-4eb8-39a9-9111-03ef33adbe43 | 2.05613 | -55.70716 | 2025-10-22 05:14:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| d2080e53-e5ec-3b26-9915-47a4d90e299d | 1.69346 | -55.70907 | 2025-10-22 05:14:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b36b991d-3f03-3564-8861-f833b059018b | -1.49115 | -47.81312 | 2025-10-22 05:14:00 | NOAA-20 | SÃO MIGUEL DO GUAMÁ | PARÁ | Brasil | 1507607 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| a5bce845-0cb3-3e6d-b68e-d8a25ccfaca1 | -1.48922 | -47.81311 | 2025-10-22 05:14:00 | NOAA-20 | SÃO MIGUEL DO GUAMÁ | PARÁ | Brasil | 1507607 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| c8d2ec13-30df-346e-a3d1-17bc5f8c82b1 | -2.27324 | -57.01567 | 2025-10-22 05:14:00 | NOAA-20 | NHAMUNDÁ | AMAZONAS | Brasil | 1303007 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| d8f84b2d-c8d3-3e26-bae4-fddaa740faa5 | -3.0273 | -49.4628 | 2025-10-22 05:14:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 5dd71cd4-b8cd-3ac9-a0d6-623ebf84c1a7 | -2.02589 | -56.88048 | 2025-10-22 05:14:00 | NOAA-20 | NHAMUNDÁ | AMAZONAS | Brasil | 1303007 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 407c0b97-f04a-3bea-b406-0133477c47e3 | 1.35164 | -50.90033 | 2025-10-22 05:14:00 | NOAA-20 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 9908e388-bbef-31ba-93d4-c878ae91cb34 | -1.89807 | -54.07464 | 2025-10-22 05:14:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 864a6ec1-6cd0-3f93-9d39-14b9b00da18b | -3.56592 | -49.48687 | 2025-10-22 05:14:00 | NOAA-20 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| a02df65a-b200-381f-aaf3-d2e00a4a46fc | -2.5028 | -56.19975 | 2025-10-22 05:14:00 | NOAA-20 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 8d1a0c82-7f23-3ef7-90a7-0200a84318f5 | -1.45535 | -55.50406 | 2025-10-22 05:14:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 1ca49379-82eb-35a4-8559-28c548cc8797 | -3.02684 | -49.4658 | 2025-10-22 05:14:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| fda9bc57-3e78-3d28-afb7-32d1bfad00b6 | -2.27046 | -57.01167 | 2025-10-22 05:14:00 | NOAA-20 | NHAMUNDÁ | AMAZONAS | Brasil | 1303007 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 09fd487e-6d32-3b13-89c0-98dbc29276dc | -2.27379 | -57.01218 | 2025-10-22 05:14:00 | NOAA-20 | NHAMUNDÁ | AMAZONAS | Brasil | 1303007 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| e6e6ec23-09a9-3318-a5e2-7b95efddcc36 | -3.5664 | -49.48372 | 2025-10-22 05:14:00 | NOAA-20 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| fc853a83-2ba4-3f8b-863e-5a4139fbcd2e | -3.57298 | -49.44004 | 2025-10-22 05:14:00 | NOAA-20 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 87bf2485-1619-3a7b-a1ca-38bb61430034 | 1.67448 | -55.74102 | 2025-10-22 05:14:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 1cc6e80d-1ad7-3a99-9215-52d743408abb | -2.92544 | -48.30761 | 2025-10-22 05:14:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 8.3 |
| 4d26060d-b300-3b7e-81ec-fa538e55b643 | -2.5062 | -56.20025 | 2025-10-22 05:14:00 | NOAA-20 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 3e6b4c5d-f510-3cf4-affe-4482e8f94853 | -2.02867 | -56.88449 | 2025-10-22 05:14:00 | NOAA-20 | NHAMUNDÁ | AMAZONAS | Brasil | 1303007 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 01db4e96-e257-396e-8021-5814394d868b | -2.02534 | -56.88396 | 2025-10-22 05:14:00 | NOAA-20 | NHAMUNDÁ | AMAZONAS | Brasil | 1303007 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 9cba4763-fec4-3e50-ad88-7f1156a797f2 | -10.05403 | -64.99102 | 2025-10-22 05:16:00 | NOAA-20 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 6a106608-e123-39ad-970b-5d9f9afc50b9 | -9.35929 | -65.88677 | 2025-10-22 05:16:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 5bd986ee-29c1-3dac-9a08-a7b8c77c2f36 | -9.48229 | -65.64709 | 2025-10-22 05:16:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f9a013ac-b638-3b01-892f-d4096fe472d3 | -9.56889 | -65.21983 | 2025-10-22 05:16:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.0 |
| efea4d52-1476-3834-98b5-ce6dd07ee034 | -9.7256 | -64.93829 | 2025-10-22 05:16:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 44399975-7d58-3830-80ad-9b583df9f793 | -9.00625 | -65.94347 | 2025-10-22 05:16:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 05c0425a-b325-3c40-b78b-44398c4a3657 | -9.11136 | -65.93689 | 2025-10-22 05:16:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 4c4e5781-667b-33e1-97af-adcde64d6277 | -9.57815 | -65.22118 | 2025-10-22 05:16:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| c198a05a-c714-3818-9237-3b6df9d0dd5a | -9.55247 | -66.65202 | 2025-10-22 05:16:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b4d06184-890f-3ff4-84e0-90bf9093d406 | -9.48731 | -65.64375 | 2025-10-22 05:16:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 84123480-c157-3d56-8c71-c03a488d3012 | -9.57397 | -65.22043 | 2025-10-22 05:16:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 4e879276-1df4-3d7b-a563-b607dfac7ce7 | -8.93327 | -66.90354 | 2025-10-22 05:16:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 673e3a79-2d0b-3c0e-a606-7565d9cc40ac | -9.57241 | -65.22451 | 2025-10-22 05:16:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 1e3e5e10-4274-32dd-8469-be7bdb08f68a | -8.87544 | -66.78138 | 2025-10-22 05:16:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| cbe8cec4-1936-34e3-a606-8bc19789ee43 | -9.47426 | -64.69759 | 2025-10-22 05:16:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 036892f3-f46a-35ff-8335-2e458fd87f3c | -9.91062 | -65.0274 | 2025-10-22 05:16:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c7463a85-ce9e-31df-b4a0-425a1ecac176 | -10.06014 | -63.53025 | 2025-10-22 05:16:00 | NOAA-20 | MONTE NEGRO | RONDÔNIA | Brasil | 1101401 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 9e7ddc3c-a872-3aaa-9a0a-58339abdd8e6 | -9.57327 | -65.22432 | 2025-10-22 05:16:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| acc7bc48-8724-3807-a703-074205c2a4f0 | -8.99022 | -65.90421 | 2025-10-22 05:16:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 2d0f8128-4065-3547-a0e8-7049c9cd4a11 | -9.89685 | -64.88763 | 2025-10-22 05:16:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| c5c9dc6a-a18e-34e9-87c3-2fb22b393016 | -9.5533 | -66.64725 | 2025-10-22 05:16:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| d6e39175-36ff-356a-b9db-355a2257454e | -9.55749 | -66.75129 | 2025-10-22 05:16:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 5fc1a2b8-5f14-39ac-bbdc-0626b2bd2163 | -9.08753 | -67.69024 | 2025-10-22 05:16:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| a2ebff93-d54b-3f93-8044-043f5574897d | -9.78329 | -63.81382 | 2025-10-22 05:16:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d5ad670b-abec-3acf-a78c-2410bf403588 | -7.93308 | -46.0187 | 2025-10-22 05:16:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 7.0 |
| e4789ab1-bdb6-3ac3-bafe-b4d65d3d3d82 | -9.55201 | -66.64973 | 2025-10-22 05:16:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 15e7c8dc-7cef-3c63-8e5a-ec81eb8e0523 | -9.00854 | -65.93016 | 2025-10-22 05:16:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 9.7 |
| 99a2f511-8045-3d76-82b0-54011a972667 | -9.64588 | -65.25346 | 2025-10-22 05:16:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| eb8e6946-4d5c-3213-a9f6-692865aaedac | -9.46894 | -64.70414 | 2025-10-22 05:16:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 204870f3-234f-3352-91aa-24a7f1e5c13e | -9.77947 | -63.81319 | 2025-10-22 05:16:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.3 |
| fddf4939-ac33-31a9-8290-0775d45c8622 | -9.00702 | -65.93901 | 2025-10-22 05:16:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 8150679e-fbbe-3779-9770-3f4320e4c237 | -9.85325 | -65.04031 | 2025-10-22 05:16:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| fdee670f-d5a1-38aa-90ed-e24574b75759 | -9.42895 | -65.4724 | 2025-10-22 05:16:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| e56e3b1f-b1bf-3dfc-91c1-19374bea09c5 | -9.72907 | -64.94274 | 2025-10-22 05:16:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 9164264b-99b5-37d0-96d0-fb0d9d353aad | -9.37642 | -64.49262 | 2025-10-22 05:16:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 01d50a32-35ba-362a-936b-b793c7de7322 | -9.97419 | -65.11539 | 2025-10-22 05:16:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b4136b40-982d-37c3-9b7e-d7bb837f12ca | -8.71629 | -68.94837 | 2025-10-22 05:16:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 0c752c57-716c-3fcc-8696-67e8c66c93d8 | -9.90651 | -65.02666 | 2025-10-22 05:16:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 5495c2da-2a03-3b57-a82f-051ca34098cd | -9.0064 | -65.91614 | 2025-10-22 05:16:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| d6651471-f084-31eb-8c40-c69c30586e46 | -8.99159 | -65.92258 | 2025-10-22 05:16:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| cd2cda2a-a562-3635-a210-17bd25273366 | -9.31094 | -65.38229 | 2025-10-22 05:16:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| fed82325-f43e-300e-be9f-f802bdf48f33 | -9.10771 | -65.93163 | 2025-10-22 05:16:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| e69cc6de-f731-34d7-9014-172341ab9aef | -8.99602 | -65.92337 | 2025-10-22 05:16:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 180dd50a-b52d-336c-9935-8bdd7cc290da | -9.90092 | -64.88837 | 2025-10-22 05:16:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.6 |
| a0020397-c9f3-3ecf-b278-1872102b7010 | -9.11212 | -65.93246 | 2025-10-22 05:16:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 3f7ac102-c8cd-3a53-be32-c05e0b960d4f | -10.05489 | -64.99117 | 2025-10-22 05:16:00 | NOAA-20 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 08a9f33f-8bf8-31bc-a982-189ae0c351df | -9.54788 | -66.6511 | 2025-10-22 05:16:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| cca5596e-e03b-384e-b986-e0c97555a5c6 | -9.00488 | -65.92496 | 2025-10-22 05:16:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 2c393e7f-06ef-3b7e-872d-dd70b54a8e30 | -9.01164 | -65.93271 | 2025-10-22 05:16:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 6d06d777-e54b-32b5-88c7-4d62d6cc99a0 | -9.56471 | -65.21906 | 2025-10-22 05:16:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 483a4fa9-e9b9-3070-9d7a-23147348c526 | -8.97482 | -65.88794 | 2025-10-22 05:16:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| f86fbd46-3754-3a42-a177-5ad7bd91da5b | -9.01007 | -65.92133 | 2025-10-22 05:16:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 4.1 |
| c8826ec2-ff0e-3f79-a3ec-80e44752a9f5 | -10.34537 | -62.83634 | 2025-10-22 05:16:00 | NOAA-20 | CACAULÂNDIA | RONDÔNIA | Brasil | 1100601 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 7a0d4d9a-be63-3dd3-8de6-82de11d30085 | -8.78868 | -66.72372 | 2025-10-22 05:16:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 94f642b9-54e2-37d1-8e42-2a6ab918cfb1 | -9.84604 | -66.37969 | 2025-10-22 05:16:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 6e5801ed-7525-3711-8ed8-25f7cb3fd704 | -9.92614 | -65.01096 | 2025-10-22 05:16:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 0f723687-b882-3d68-b56c-6ceef128ac41 | -9.6452 | -65.25735 | 2025-10-22 05:16:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d7e0f7ee-5d91-3655-b86d-8a924d068ffb | -9.01243 | -65.92831 | 2025-10-22 05:16:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 01502ebd-76b8-3135-bbe1-7eb742f2bc49 | -8.99816 | -65.93739 | 2025-10-22 05:16:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 4a6df960-d958-31ac-824e-5416ae4b194c | -9.57726 | -65.22137 | 2025-10-22 05:16:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f76a86d1-b542-34d4-a82c-262223cdc806 | -9.01084 | -65.93713 | 2025-10-22 05:16:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 8.4 |
| 757e4b30-fd50-310e-aae6-79db547b3e83 | -8.99099 | -65.89981 | 2025-10-22 05:16:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 6f8f4eb4-7618-3391-8a75-ce09d8dd665c | -10.34897 | -62.83694 | 2025-10-22 05:16:00 | NOAA-20 | CACAULÂNDIA | RONDÔNIA | Brasil | 1100601 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 587509f9-acc6-3bfc-a862-f04f41303e47 | -9.57307 | -65.2206 | 2025-10-22 05:16:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 25338c79-c41c-34bf-86b9-eed15b8131ce | -9.10695 | -65.93602 | 2025-10-22 05:16:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 3a5ee6b8-3585-3c99-90a4-6da5ea899c9e | -9.46958 | -64.7005 | 2025-10-22 05:16:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| a140255a-c947-32a8-b47e-e363f2ac6be9 | -9.01298 | -65.93094 | 2025-10-22 05:16:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 0dcfb730-743a-38b2-87a8-054da880e1a5 | -9.71954 | -64.99873 | 2025-10-22 05:16:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.2 |
| c775fa6b-277e-3936-884b-7d51063e6de9 | -10.07783 | -65.16916 | 2025-10-22 05:16:00 | NOAA-20 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 2.4 |
| a121ea29-fabc-33fb-8632-14e64b85e307 | -9.71606 | -64.99429 | 2025-10-22 05:16:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c28270a1-2b55-32b4-ad9d-c4507662e0e1 | -9.00411 | -65.92937 | 2025-10-22 05:16:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 9.7 |
| 3c185e53-c8a9-3ddc-8db9-a08f92f544d0 | -9.35924 | -65.88863 | 2025-10-22 05:16:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 9811e48c-ffa3-3c5d-9682-d98b192804eb | -9.01145 | -65.93981 | 2025-10-22 05:16:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 1700b7bb-1a93-3e44-a3b8-52ca3c31e03e | -9.86055 | -64.16734 | 2025-10-22 05:16:00 | NOAA-20 | BURITIS | RONDÔNIA | Brasil | 1100452 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 6d63bc31-afe4-3038-a27c-a6592c0fd2fa | -9.70792 | -64.94286 | 2025-10-22 05:16:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| c3d4733a-4fbd-3af5-a47d-1e296967dc44 | -9.00564 | -65.92055 | 2025-10-22 05:16:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 4.1 |
| eea8f3c7-315a-37a8-ad7a-5ca2796b1a67 | -9.89875 | -63.59094 | 2025-10-22 05:16:00 | NOAA-20 | ARIQUEMES | RONDÔNIA | Brasil | 1100023 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |


[Clique aqui para ver as próximas entradas](README18.md)
