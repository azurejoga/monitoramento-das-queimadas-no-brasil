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

## Dados Diários - Página 98

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 4af3ddda-88ed-3b01-a21d-1c6d8a846d43 | -4.13227 | -55.04701 | 2024-10-24 05:21:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 8e840a18-7aee-36e1-9aab-5efbb4350cc1 | -4.13097 | -55.02843 | 2024-10-24 05:21:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 45b2d5f7-b94a-3976-8a5f-68d5a399b75b | -4.12751 | -55.02413 | 2024-10-24 05:21:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 8fd09510-c0df-358f-8c79-0f232fd3faa3 | -3.86138 | -55.3513 | 2024-10-24 05:21:00 | NOAA-20 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 6586b23b-07f4-317e-a558-049546f2725f | -3.98663 | -53.98454 | 2024-10-24 05:21:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 1cbf4e78-4378-32f6-ae6a-bd9a9996d38e | -3.97427 | -54.09431 | 2024-10-24 05:21:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 6f59ac67-3799-3a73-a5f1-f9b25016cb43 | -3.88869 | -54.14133 | 2024-10-24 05:21:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 9dfdc91f-d0af-334f-b492-04e7602fd81d | -3.8881 | -54.14531 | 2024-10-24 05:21:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 9b9d08f8-54b2-3c47-988d-4cb2bed58e16 | -3.88443 | -54.14068 | 2024-10-24 05:21:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 1292993c-b3ac-32d1-a920-13ea9eb90714 | -3.88385 | -54.14465 | 2024-10-24 05:21:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 1f58633c-9a5d-3cfd-9a26-6fa564c57932 | -4.11774 | -54.68044 | 2024-10-24 05:21:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 6c1ac57f-ca87-35af-bf31-343ee13672ba | -4.09466 | -54.29706 | 2024-10-24 05:21:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| edb6223b-a56a-3e67-8477-74882d7b73b7 | -4.09159 | -54.28861 | 2024-10-24 05:21:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| c45f0d85-5dcf-3a93-b55e-ef84bb821295 | -4.09101 | -54.29255 | 2024-10-24 05:21:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 1c2003f2-fe78-33fa-afbc-f706126f2f4c | -4.09031 | -54.26795 | 2024-10-24 05:21:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c24f67d4-6a8e-36aa-bb87-3bc239112ca8 | -4.08669 | -54.26318 | 2024-10-24 05:21:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 6a6aeeba-2056-3b01-ade9-586a990f4a9c | -4.05347 | -54.28254 | 2024-10-24 05:21:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| fab91f96-b335-3b7d-868b-04b245a11219 | -4.00798 | -54.38365 | 2024-10-24 05:21:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 2d47ec93-f846-3053-806c-df878e0df776 | -4.00378 | -54.38306 | 2024-10-24 05:21:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 82c14720-7ac5-3bab-ab91-b511fcee27ae | -3.99116 | -54.46685 | 2024-10-24 05:21:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| a88cd093-83c4-3bb6-9c95-450a1dd64996 | -3.99059 | -54.47063 | 2024-10-24 05:21:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| c8cbd012-0382-37e5-bc49-c0761b9be483 | -3.98265 | -54.35215 | 2024-10-24 05:21:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 2e24d823-b8ef-3dff-b180-478376d39e93 | -3.97846 | -54.35143 | 2024-10-24 05:21:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| eb6d6717-70fd-3515-8d4d-94d2daba01a4 | -3.97428 | -54.35065 | 2024-10-24 05:21:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 8f33e355-d3ee-3872-9a26-aff3a4a6ab4c | -3.96546 | -54.43896 | 2024-10-24 05:21:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 75cae613-7a8b-35b8-9720-bdc17a633827 | -3.92902 | -54.54149 | 2024-10-24 05:21:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| d23294b6-806d-328d-9235-eba033816d75 | -3.85077 | -54.76426 | 2024-10-24 05:21:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 937782fb-e558-37b5-ae12-fb9a708473de | -3.85023 | -54.76779 | 2024-10-24 05:21:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 9a2c6394-a080-3e34-98f9-50a5197208f9 | -3.82308 | -54.55679 | 2024-10-24 05:21:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| efacd8a1-5bdc-3543-b18a-d0a2f26bdb30 | -3.81894 | -54.55622 | 2024-10-24 05:21:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 74b69ed6-da71-3396-990e-39c8b198aa47 | -3.80831 | -54.47125 | 2024-10-24 05:21:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 898b9acf-2e34-3074-bde8-569987881bd9 | -3.67933 | -54.55246 | 2024-10-24 05:21:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 814c3f22-9ffc-3204-8463-2c80440da14a | -3.6752 | -54.55187 | 2024-10-24 05:21:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| baa6271a-43ad-3c9e-9d32-b655d1280a4c | -3.6669 | -54.26806 | 2024-10-24 05:21:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c393436d-2291-3c6c-9fc6-cceec02d80a9 | -3.66633 | -54.27184 | 2024-10-24 05:21:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| a0c84349-483a-34ec-b115-38215921733c | -3.66576 | -54.27567 | 2024-10-24 05:21:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 5febaf69-2a77-3212-ba9f-a9527b182732 | -3.66268 | -54.26751 | 2024-10-24 05:21:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 14.6 |
| a888a925-374a-3322-a06b-dcc28c797146 | -3.66212 | -54.27127 | 2024-10-24 05:21:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 3d61a272-7785-3805-a525-33a915f8b253 | -3.66155 | -54.27507 | 2024-10-24 05:21:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| ef4e596c-f0d3-3991-b14e-84ce3449b9d9 | -3.65497 | -54.51816 | 2024-10-24 05:21:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 3708e1fb-89b6-383c-995e-d91e3d0517d8 | -3.65003 | -54.79774 | 2024-10-24 05:21:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 8a9a6b55-d365-3c8d-a7ec-c33b76038e91 | -3.6465 | -54.79373 | 2024-10-24 05:21:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 0b3007e6-d7c6-31a4-a6c9-44d52febd6bd | -3.64596 | -54.79723 | 2024-10-24 05:21:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 9f1130d4-bf85-3ffb-ae4b-1af0faf542dd | -3.63802 | -54.68554 | 2024-10-24 05:21:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 12b2b83d-4236-34a8-ae4f-1a427d800487 | -3.63395 | -54.68485 | 2024-10-24 05:21:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 320b893c-0424-3f1c-b29f-ac4f8b766c24 | 1.56475 | -55.66059 | 2024-10-24 05:21:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| cb6e41bb-717b-3956-8dea-2f231172b6b9 | 1.56325 | -55.66178 | 2024-10-24 05:21:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 09ad40d4-2992-36d8-98a8-51027906b7db | 1.56179 | -55.66526 | 2024-10-24 05:21:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b3edd602-b8f2-3c7f-92c7-395954d24a0e | 1.5582 | -55.66581 | 2024-10-24 05:21:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 6c55dc2a-0ad0-3f84-aaa0-68f273b60a84 | -2.00196 | -56.4004 | 2024-10-24 05:21:00 | NOAA-20 | TERRA SANTA | PARÁ | Brasil | 1507979 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| eb4c6e27-1524-312c-93d9-06d25c664d3d | -2.05077 | -56.1144 | 2024-10-24 05:21:00 | NOAA-20 | NHAMUNDÁ | AMAZONAS | Brasil | 1303007 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 7038f340-39e2-33ba-9a03-17bd6503d041 | -2.05013 | -56.11745 | 2024-10-24 05:21:00 | NOAA-20 | NHAMUNDÁ | AMAZONAS | Brasil | 1303007 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| e9f314ea-318b-3d28-a428-35a9a6a83340 | -2.02871 | -55.89307 | 2024-10-24 05:21:00 | NOAA-20 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 3918007d-3ad9-3842-8cfc-d06fd0af61cb | -2.02432 | -55.8969 | 2024-10-24 05:21:00 | NOAA-20 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 9b8a554c-c272-373a-8392-c6bc42d1cc5b | -1.87593 | -55.62714 | 2024-10-24 05:21:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 1093a59b-3cd0-3d16-96ad-8cd59adfb906 | -1.8577 | -55.30052 | 2024-10-24 05:21:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 40a8b60e-11b6-39bb-93fe-2df21b7ea4e0 | -1.85589 | -55.30236 | 2024-10-24 05:21:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 42baca6a-7ae9-363f-a69a-3cad3f5a45c0 | -1.80153 | -55.25799 | 2024-10-24 05:21:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 128504f5-d201-3647-b115-ec18e841fd19 | -1.72801 | -55.75854 | 2024-10-24 05:21:00 | NOAA-20 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 82e5238b-7965-3df3-9115-a6620f26878c | -1.72282 | -55.64346 | 2024-10-24 05:21:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 532ffa53-77b2-316f-aacb-1752d26edae0 | -1.71011 | -55.04424 | 2024-10-24 05:21:00 | NOAA-20 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 9fc2fab0-2159-3901-85f3-2c4cb31890eb | -1.70937 | -55.04905 | 2024-10-24 05:21:00 | NOAA-20 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f1e3ea18-ad01-3819-899b-fb2800817eca | -1.69196 | -55.11103 | 2024-10-24 05:21:00 | NOAA-20 | CURUÁ | PARÁ | Brasil | 1502855 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f5521e7d-4b1a-3b7d-8f67-6aa11e57f861 | -1.61449 | -55.11669 | 2024-10-24 05:21:00 | NOAA-20 | CURUÁ | PARÁ | Brasil | 1502855 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 1aad22f7-abcf-339a-a447-901cb1c32177 | -1.61063 | -55.11608 | 2024-10-24 05:21:00 | NOAA-20 | CURUÁ | PARÁ | Brasil | 1502855 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e069aecc-dd87-32b7-831a-c9fc48ac17a1 | -1.60231 | -55.84457 | 2024-10-24 05:21:00 | NOAA-20 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 72eb6b55-16f9-3f7b-be89-960be892086f | -1.54634 | -55.89586 | 2024-10-24 05:21:00 | NOAA-20 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| ceb52338-a2a0-3c22-b9ab-49d3782d05fe | -1.54566 | -55.90018 | 2024-10-24 05:21:00 | NOAA-20 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| eedda35c-efcc-33cd-91bd-a2e54d4b8508 | -1.54494 | -55.89831 | 2024-10-24 05:21:00 | NOAA-20 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 830fbce3-8be6-39f9-a69b-d4f20e95d44e | -1.54428 | -55.90264 | 2024-10-24 05:21:00 | NOAA-20 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 68356510-e56b-38aa-aa74-a945b89ccd07 | -1.54354 | -55.34821 | 2024-10-24 05:21:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 643d41f8-0df1-31bc-9f23-c510f1788a33 | -1.54282 | -55.35287 | 2024-10-24 05:21:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 418cb03b-8caa-3311-ad8f-7634ea841b33 | -1.54197 | -55.89964 | 2024-10-24 05:21:00 | NOAA-20 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| d235c1b0-3bd1-3fb0-9903-2ad91c0c46ba | -1.54125 | -55.89778 | 2024-10-24 05:21:00 | NOAA-20 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 68291308-f7e9-3fbf-94c9-acbccb6b217c | -1.53973 | -55.34763 | 2024-10-24 05:21:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| cda18744-1800-300c-8a0a-87c9b2a2a833 | -1.48868 | -55.10092 | 2024-10-24 05:21:00 | NOAA-20 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 5f2685c9-e960-32ee-bcf2-58fbe3717fad | -1.48481 | -55.10038 | 2024-10-24 05:21:00 | NOAA-20 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 76528a55-832a-3c8b-b26d-6844e3c55e40 | -1.17472 | -55.70584 | 2024-10-24 05:21:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| e2e7929b-3a43-3152-a3a5-76bca3fbebaf | -1.56084 | -54.89211 | 2024-10-24 05:21:00 | NOAA-20 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| b7051af8-ede0-3b34-8c1f-59581812a25c | -2.48566 | -55.71734 | 2024-10-24 05:21:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| b16dd9b8-fec0-328c-ab25-5843db42d760 | -2.48495 | -55.72197 | 2024-10-24 05:21:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 20a5c81d-9d76-3074-aa38-1eb2eeac6225 | -2.48424 | -55.7266 | 2024-10-24 05:21:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 4ba217e5-8439-37a9-9f4d-a91f87e8239b | -2.48118 | -55.72139 | 2024-10-24 05:21:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 5d3070b5-deae-3a2d-84e0-db1644f8e943 | -2.42684 | -55.69667 | 2024-10-24 05:21:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f22fe199-73b3-38d8-91e9-bedb77c40b62 | -3.62976 | -55.44995 | 2024-10-24 05:21:00 | NOAA-20 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 763af567-f2ff-30bc-b3eb-ab10d0125131 | -3.62814 | -55.43447 | 2024-10-24 05:21:00 | NOAA-20 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c3cbfe8b-150f-3302-b75b-0fa830b812a0 | -3.62542 | -55.50434 | 2024-10-24 05:21:00 | NOAA-20 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 663146ef-14cb-3955-a6e4-25ec62fa5207 | -3.62469 | -55.50916 | 2024-10-24 05:21:00 | NOAA-20 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| adfd1849-af7b-39a3-8fad-6fe3f2652e1d | -3.62155 | -55.50373 | 2024-10-24 05:21:00 | NOAA-20 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 7a54d5c7-c272-301f-8265-2a0988916c46 | -3.62082 | -55.50855 | 2024-10-24 05:21:00 | NOAA-20 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 2966916b-124a-3f8c-a02d-4e2eb7f02a31 | -3.60847 | -55.51154 | 2024-10-24 05:21:00 | NOAA-20 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 12b06f23-c2c3-3528-be6d-5bd3c5fa2ef0 | -3.60773 | -55.51638 | 2024-10-24 05:21:00 | NOAA-20 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 67071761-a7f9-3056-8e67-67c63ecaa855 | -3.6046 | -55.5109 | 2024-10-24 05:21:00 | NOAA-20 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 2c45445b-d564-393e-9b17-c45f15a5c507 | -3.60386 | -55.51575 | 2024-10-24 05:21:00 | NOAA-20 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 53be1c30-cd6a-394d-9d2e-c232f1ed0b54 | -4.53911 | -55.75074 | 2024-10-24 05:21:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 8570ad50-3bce-32ad-b1f5-216610b2650b | -4.53839 | -55.7555 | 2024-10-24 05:21:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d7b469c1-5969-365d-ab8b-6bebdaf1465e | -4.53453 | -55.75492 | 2024-10-24 05:21:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 077546db-d8b9-3045-9711-bd0754781000 | -4.51259 | -55.66259 | 2024-10-24 05:21:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| fd27e648-e287-329a-a64d-ed593fb22823 | -4.20295 | -55.55664 | 2024-10-24 05:21:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 2a53fc42-5ef6-3580-b0e1-d698c247ab96 | -4.19943 | -55.55736 | 2024-10-24 05:21:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 10.5 |


[Clique aqui para ver as próximas entradas](README99.md)
