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
| 44b2fcce-e3f4-3cb5-a31f-6d33f7bfa753 | -6.81352 | -59.26972 | 2025-07-31 05:50:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 13d30764-56ff-37ea-8afe-5f1a5040519d | -6.65934 | -56.4031 | 2025-07-31 05:50:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 59829db8-17d3-3287-bcca-51ced5146ade | -6.66693 | -56.39131 | 2025-07-31 05:50:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 42aa3258-2a0e-30f4-b463-69ec52678eae | -6.66636 | -56.39544 | 2025-07-31 05:50:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 7b487a13-6225-3d0a-ac79-4250b4230cea | -10.07987 | -53.87008 | 2025-07-31 05:50:00 | NPP-375D | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 04ad012f-de50-3a1f-8058-1865c7ddeef5 | -6.52787 | -56.21049 | 2025-07-31 05:50:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 495d19bc-bdb3-3bf1-8a37-493856467d9f | -6.52134 | -56.21405 | 2025-07-31 05:50:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 35ce384e-6706-3e52-bc2b-f0400a8607bb | -6.5273 | -56.19218 | 2025-07-31 05:50:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| a17b32a0-760b-3f95-9dad-a90f41bf7354 | -6.55524 | -56.18788 | 2025-07-31 05:50:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 602f52c8-4544-31a7-b7c7-f520657447f6 | -6.3695 | -53.3325 | 2025-07-31 05:50:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 909bf399-b52b-33a0-a64f-b7e21073e3a9 | -6.54153 | -56.19928 | 2025-07-31 05:50:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 29d7e2b1-2732-38aa-9c77-83d18477ef71 | -6.66408 | -56.41211 | 2025-07-31 05:50:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 980cec28-c155-3df9-aef3-ea6c9f9cdf49 | -6.67045 | -56.40918 | 2025-07-31 05:50:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| f640744b-8ed8-32aa-9cfa-b4ca33092e32 | -6.54452 | -56.19896 | 2025-07-31 05:50:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| be34b02a-d11d-36b5-b7ac-0a2074d4ae92 | -6.64773 | -58.82499 | 2025-07-31 05:50:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 3.2 |
| bdf105f6-ef13-3063-9d9e-c086f17863ee | -6.5338 | -56.18879 | 2025-07-31 05:50:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 9a2924db-331b-33d9-ad81-37d749d8af2f | -6.55872 | -56.18321 | 2025-07-31 05:50:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a30d9f28-b784-3604-a0b8-3c720c8b921f | -6.81759 | -59.27581 | 2025-07-31 05:50:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| e7cd8ca7-1477-35bd-aadb-95f6750c3467 | -6.54095 | -56.20342 | 2025-07-31 05:50:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 8cf5180d-c839-3977-b1cf-fc4cb3b7e23a | -6.62367 | -59.97797 | 2025-07-31 05:50:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 8.5 |
| a9bd69f5-6bc2-3fe6-9a98-071ea20527eb | -6.39045 | -53.32019 | 2025-07-31 05:50:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a540d9cd-0d1c-33e1-a3d7-500087e2c493 | -6.66522 | -56.40382 | 2025-07-31 05:50:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| f0c4cb17-e13f-38ff-999d-28f67bd2ae41 | -6.51724 | -56.20021 | 2025-07-31 05:50:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 034f7163-2695-3938-a909-ce6818c7809a | -6.67738 | -56.40219 | 2025-07-31 05:50:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| d887b9dd-77dd-32e2-8a2f-7b96ea363b33 | -10.0878 | -53.86438 | 2025-07-31 05:50:00 | NPP-375D | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| c8a4c7aa-709d-3de9-950e-f03340775197 | -6.49057 | -56.21844 | 2025-07-31 05:50:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| acc033ff-b957-3d77-a8ed-95de16b9df9f | -6.49116 | -56.21416 | 2025-07-31 05:50:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 71624853-0c42-36a0-b2e5-61ca332bdb0c | -6.41509 | -53.36623 | 2025-07-31 05:50:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 90e98e75-5a7e-34c8-a101-48033dcef4ce | -6.54688 | -56.20417 | 2025-07-31 05:50:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c0827c6c-ad06-3cfc-9bd8-7272ece69577 | -6.68268 | -58.86443 | 2025-07-31 05:50:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 1e3182a3-6702-396d-a0fe-ce96a94e3356 | -6.66579 | -56.39964 | 2025-07-31 05:50:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 5c8126f4-af6d-3e09-8214-cd882f30c15c | -6.5499 | -56.20383 | 2025-07-31 05:50:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d02470cd-6ac0-35e4-8b95-2be231059e81 | -6.52024 | -56.19988 | 2025-07-31 05:50:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 2c033cc3-9224-3880-acc5-8a4d0ea14ab0 | -6.37745 | -53.32679 | 2025-07-31 05:50:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 6e6dd4c4-7cbf-36b2-969b-03b3803dc274 | -6.51192 | -56.19504 | 2025-07-31 05:50:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| b58d15a0-abe1-308c-a0bf-ddb4664b38ef | -6.55697 | -56.19621 | 2025-07-31 05:50:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| a588257e-c918-3772-94c6-79172345a79e | -6.56407 | -56.18839 | 2025-07-31 05:50:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 95bd82f3-6e57-3e51-b22d-f6e2ced1c42f | -6.54628 | -56.20842 | 2025-07-31 05:50:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b220d031-4e83-3bef-87bf-811184b0034b | -6.52673 | -56.19648 | 2025-07-31 05:50:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| afa0ee4e-b281-3210-bb24-2dfbf9bb8b33 | -6.55462 | -56.19223 | 2025-07-31 05:50:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| d8e0c9a9-e20c-3967-9255-5ea57d986e7f | -6.51664 | -56.20452 | 2025-07-31 05:50:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 27e21f67-8828-3bbe-aa94-c293424132db | -6.53087 | -56.18917 | 2025-07-31 05:50:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| f282a5b4-de25-30af-8bfd-1af23bf5a7f2 | -6.54933 | -56.20813 | 2025-07-31 05:50:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 679f4322-8e5b-3380-b489-21cca2b6601f | -6.56349 | -56.19269 | 2025-07-31 05:50:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 210e24d1-43ad-3d45-9697-39eb79f34d7a | -7.77768 | -61.36858 | 2025-07-31 05:50:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 23452174-594d-376d-87aa-cd3669d73d63 | -6.67771 | -58.86375 | 2025-07-31 05:50:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 326cb23d-e3e0-3683-b24c-c8ac61c1fa1e | -6.37551 | -53.32469 | 2025-07-31 05:50:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| e29acfa6-9595-32c6-bfca-993249a9e044 | -6.50537 | -56.19867 | 2025-07-31 05:50:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| a9d48d31-aeb8-312a-95c8-1ff9ed222ef3 | -6.52194 | -56.20974 | 2025-07-31 05:50:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 4ee38863-963d-385a-88ee-abcb491a901a | -7.9022 | -61.5216 | 2025-07-31 05:50:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 6e4c9af5-360b-3506-882a-9bfaadfb9bc5 | -6.51012 | -56.20795 | 2025-07-31 05:50:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d608a622-4320-3e60-8e0a-b8e4fac5910c | -6.40717 | -53.37169 | 2025-07-31 05:50:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| de0a7c2b-8e57-39f0-afba-67696706eb5a | -6.6722 | -56.39644 | 2025-07-31 05:50:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| d93c0b91-e55b-3c25-b7e0-18117a517304 | -6.53152 | -56.20586 | 2025-07-31 05:50:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 92a2c40f-06c9-3f58-801d-5896538d2ed2 | -6.49886 | -56.20214 | 2025-07-31 05:50:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| eccd3667-5146-33b1-9bcb-22d511c50a63 | -6.55221 | -56.18672 | 2025-07-31 05:50:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| ef2dc6e6-bfe0-38df-b078-b5f6533ef6c3 | -6.67279 | -56.39214 | 2025-07-31 05:50:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 01301807-497b-35db-8627-2ef055ef7dfb | -6.49944 | -56.19791 | 2025-07-31 05:50:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 8f8c3731-e2b5-37a8-bfff-0e5f9c972bee | -6.56466 | -56.18405 | 2025-07-31 05:50:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 70e44bd1-7704-368a-a5fe-6bfcf02b52fb | -6.62624 | -59.99248 | 2025-07-31 05:50:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 6a042eff-db57-3204-9dc4-a4b57d14e99b | -6.52435 | -56.19251 | 2025-07-31 05:50:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| a0b726b6-7a78-38be-a425-5be175752d51 | -6.51784 | -56.1959 | 2025-07-31 05:50:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| f99cc7fa-14ac-3bf5-9d34-bcd7a870c909 | -6.52559 | -56.20509 | 2025-07-31 05:50:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 1563d69f-0cdf-3208-baf6-7e951454fd22 | -6.52847 | -56.20625 | 2025-07-31 05:50:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 646beaf9-8c69-3b07-81e3-7c0a8b1ba72d | -6.51853 | -56.21283 | 2025-07-31 05:50:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| c7a7b0cb-0fbd-3bbf-baf4-e7714968ed07 | -6.55282 | -56.20489 | 2025-07-31 05:50:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 64b3fb3e-c3ed-33de-b70f-cd5b6b5c6a0f | -6.52616 | -56.20079 | 2025-07-31 05:50:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 0895b772-2c7c-37b6-ad12-46dec37be8e4 | -6.65342 | -56.40274 | 2025-07-31 05:50:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c69d6171-4477-3106-95bb-62a5bd7e4362 | -6.65399 | -56.39854 | 2025-07-31 05:50:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 391cc7c1-5839-3523-a0cc-1c37f915c4e4 | -6.67102 | -56.40506 | 2025-07-31 05:50:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 1d5bb86f-b4da-35a6-b79a-05e604ea48a2 | -6.5434 | -56.20733 | 2025-07-31 05:50:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e360e2b3-25cc-3695-a0d7-e57a3cba4201 | -6.50952 | -56.21229 | 2025-07-31 05:50:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 9e708f47-0c5e-3edb-aff7-e58b7b3fb061 | -6.48998 | -56.22271 | 2025-07-31 05:50:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a753d1df-685a-3fd1-af97-0e9f585027d9 | -10.03703 | -59.36082 | 2025-07-31 05:53:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b5773aef-3d07-3ceb-b575-9e4ac9960a7c | -10.69649 | -65.14772 | 2025-07-31 05:53:00 | NPP-375D | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 3d7d51e7-cb58-3f05-93ee-0578e97c28eb | -10.05544 | -59.11503 | 2025-07-31 05:53:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| b07cf619-f1a0-3215-8075-d0c8d24f26c4 | -10.0571 | -64.99557 | 2025-07-31 05:53:00 | NPP-375D | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 5ac143f7-af84-315d-8cb5-7ca1541ba89a | -10.48967 | -67.93909 | 2025-07-31 05:53:00 | NPP-375D | CAPIXABA | ACRE | Brasil | 1200179 | 12 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 8fc82b32-703b-3ee8-bfe3-754d4b2965e7 | -12.27933 | -63.80185 | 2025-07-31 05:53:00 | NPP-375D | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 17de4d26-c3a8-3253-8418-96834aefb2ea | -10.05584 | -59.11201 | 2025-07-31 05:53:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 380dca48-f116-3d31-a968-d380106b3f4f | -10.30958 | -54.15867 | 2025-07-31 05:53:00 | NPP-375D | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 90c44e9e-ba27-352d-8207-6cc28185ed0c | -10.03788 | -59.36034 | 2025-07-31 05:53:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b65b5f6a-4622-38dd-82fa-0c5e88fe2556 | -10.31738 | -54.15302 | 2025-07-31 05:53:00 | NPP-375D | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 43c6091d-3909-3351-b85d-6cb0317c6fb6 | -9.51517 | -63.52674 | 2025-07-31 05:53:00 | NPP-375D | ALTO PARAÍSO | RONDÔNIA | Brasil | 1100403 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 6eb3478e-af57-3ac3-aaad-f28a69b7899d | -8.07 | -43.1216 | 2025-07-31 06:00:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 73.0 |
| b14823ec-bc6f-317c-9c45-bc19cc118e5e | -8.051 | -43.1237 | 2025-07-31 06:00:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 86.7 |
| bd3117b3-dc96-3989-8260-31f01aca2b58 | -8.0513 | -43.1001 | 2025-07-31 06:00:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 103.8 |
| 7ab89d29-e4ef-3c86-b56c-7f3cb7f46c5a | -8.0703 | -43.0981 | 2025-07-31 06:00:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 87.4 |
| ef2058b4-8905-3b22-b9b4-4b404d29a72e | -6.6725 | -56.4029 | 2025-07-31 06:00:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 44.0 |
| 64d4d216-595d-35e7-ba01-452a9cdabc81 | -6.6725 | -56.4029 | 2025-07-31 06:10:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 47.2 |
| 2177af29-1cf3-33d5-a3fe-410d49fd2d53 | -8.07 | -43.1216 | 2025-07-31 06:10:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 66.9 |
| 4a6c926a-d71a-3518-9d8a-446a2f47e663 | -8.051 | -43.1237 | 2025-07-31 06:10:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 60.3 |
| f06adb9a-ad15-329a-a200-2d57273c2d13 | -8.0513 | -43.1001 | 2025-07-31 06:10:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 86.4 |
| f8c28d83-2d1c-3e13-bab7-cc7643d77410 | -8.0703 | -43.0981 | 2025-07-31 06:10:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 98.0 |
| eecdaf76-43d5-3078-87f2-58d1ee4debb7 | 4.31037 | -60.79818 | 2025-07-31 06:10:00 | NOAA-20 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 07f41efd-5391-3b1a-97c2-22d378f0e70f | -6.51614 | -56.20723 | 2025-07-31 06:12:00 | AQUA_M-M | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 19.8 |
| 23478d99-1743-3f36-a3c5-ffe584d299f0 | -6.55609 | -56.1906 | 2025-07-31 06:12:00 | AQUA_M-M | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 14.4 |
| 9cb929c7-2acc-31fb-ad2d-273a39cf6f4c | -12.63244 | -48.08404 | 2025-07-31 06:12:00 | AQUA_M-M | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 13.6 |
| 8cd1b39d-31b3-3bd3-9ba5-72b5d292dfff | -6.6589 | -56.40178 | 2025-07-31 06:12:00 | AQUA_M-M | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 22.5 |
| 3f6590aa-3c7a-32b3-8c5e-f2b6bb62b277 | -6.51831 | -56.19333 | 2025-07-31 06:12:00 | AQUA_M-M | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 32.6 |


[Clique aqui para ver as próximas entradas](README18.md)
