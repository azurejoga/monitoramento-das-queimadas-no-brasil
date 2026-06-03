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
| 9f7ca61a-9a74-3b33-af4a-80d3106f14c2 | -12.7272 | -54.1988 | 2026-06-03 13:40:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 78.7 |
| 0f8b7c2b-9c5a-36c7-84ae-332ae137fa62 | -12.7463 | -54.1969 | 2026-06-03 13:40:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 113.3 |
| 672bad1d-90b9-3a12-844f-6ccb8064eb02 | -12.556 | -57.1798 | 2026-06-03 13:40:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 176.6 |
| d790beb8-a79d-31cc-a73f-3cc9260b938a | -12.0195 | -45.8573 | 2026-06-03 13:50:00 | GOES-19 | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 106.6 |
| 0a6c70cc-fc64-33ab-a985-751f2073b9b6 | -12.7463 | -54.1969 | 2026-06-03 13:50:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 133.4 |
| 13e5b110-aae1-39a4-b816-50111246ff88 | -12.556 | -57.1798 | 2026-06-03 13:50:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 160.3 |
| 6983237b-231c-30a7-a2f5-20566eb96e49 | -12.537 | -57.1814 | 2026-06-03 13:50:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 156.0 |
| 6a076014-5a81-3fa2-aeed-733a22120a38 | -12.537 | -57.1814 | 2026-06-03 14:00:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 105.0 |
| d8871481-9c1b-3f3d-9bce-671d4e0d351c | -12.7463 | -54.1969 | 2026-06-03 14:00:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 133.8 |
| fc7b2e9e-8cbc-3ba9-b94e-ce52acd89e9e | -11.614 | -55.1861 | 2026-06-03 14:00:00 | GOES-19 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 75.1 |
| affd777d-985a-37b2-98ae-cc4373cea44d | -12.7272 | -54.1988 | 2026-06-03 14:00:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 109.6 |
| e326d054-764d-311a-874b-af0b09cfdca2 | -12.556 | -57.1798 | 2026-06-03 14:00:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 185.0 |
| 3b315993-2a55-33e7-8804-33e24dd3610c | -11.6329 | -55.1844 | 2026-06-03 14:00:00 | GOES-19 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 73.2 |
| da053584-3470-34f8-b1d9-070e834d6c57 | -12.537 | -57.1814 | 2026-06-03 14:10:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 103.6 |
| 2b3d5ef8-29e5-3252-8d05-0f9208ed6dc7 | -11.6329 | -55.1844 | 2026-06-03 14:10:00 | GOES-19 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 95.3 |
| b247e152-0eb2-3e65-8368-1dd4fe68aa58 | -12.556 | -57.1798 | 2026-06-03 14:10:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 153.7 |
| f2373ad3-281e-3ef3-9acd-348fcbe59059 | -11.614 | -55.1861 | 2026-06-03 14:10:00 | GOES-19 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 92.5 |
| b260e9c4-5330-386e-a4da-3100a5d004e7 | -12.7272 | -54.1988 | 2026-06-03 14:10:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 97.4 |
| 0ab5f62a-2d28-3b5a-89b9-6e47fa4e1884 | -12.7463 | -54.1969 | 2026-06-03 14:10:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 129.6 |
| 696a207b-b6e4-3829-96e4-8a87668473c9 | -12.7463 | -54.1969 | 2026-06-03 14:20:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 82.9 |
| d09d5e7a-ed53-331f-8563-bc33d5d4c44e | -11.886 | -57.8329 | 2026-06-03 14:20:00 | GOES-19 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 71.6 |
| 5835879e-2253-35fd-9439-705de668bf5d | -12.7272 | -54.1988 | 2026-06-03 14:20:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 95.6 |
| 3ec615d2-9285-39e6-b16b-4295c93324ff | -12.556 | -57.1798 | 2026-06-03 14:20:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 160.0 |
| 5808ab19-7785-3807-b3d4-2de4b59a428d | -12.537 | -57.1814 | 2026-06-03 14:20:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 91.9 |
| f0f48bab-ba39-32e1-bc1c-75292a676e07 | -12.4473 | -58.4033 | 2026-06-03 14:20:00 | GOES-19 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 71.3 |
| f0f4fcd3-d543-38ee-9505-966dd87edc5f | -11.614 | -55.1861 | 2026-06-03 14:30:00 | GOES-19 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 103.2 |
| 827b41e8-506d-3807-9663-a5ccc4d8fc66 | -12.4283 | -58.4048 | 2026-06-03 14:30:00 | GOES-19 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 78.3 |
| 4a414292-ced4-36ef-8e78-b9af6c31382b | -11.6329 | -55.1844 | 2026-06-03 14:30:00 | GOES-19 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 123.1 |
| 7f99a02f-0376-3811-a11f-7676e27b369d | -12.556 | -57.1798 | 2026-06-03 14:30:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 105.2 |
| 8f8590f2-b582-37bb-8270-f9c2ff46116c | -12.4473 | -58.4033 | 2026-06-03 14:40:00 | GOES-19 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 73.5 |
| b8e73887-1d3e-3e2c-bf80-fb816c768b10 | -11.6329 | -55.1844 | 2026-06-03 14:40:00 | GOES-19 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 149.3 |
| 4160f33f-2e39-3229-b0ec-73816559a860 | -12.4283 | -58.4048 | 2026-06-03 14:40:00 | GOES-19 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 88.7 |
| 2a51ce9d-6199-3b90-a460-7e996e6efa9a | -10.8573 | -53.7425 | 2026-06-03 14:40:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 84.8 |
| 319540f4-1a98-3087-bab5-5b917df6bda8 | -12.537 | -57.1814 | 2026-06-03 14:40:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 96.1 |
| 2a5df465-7128-3c9a-bb95-02a206932c89 | -11.614 | -55.1861 | 2026-06-03 14:40:00 | GOES-19 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 102.3 |
| c74b5dd5-fad4-3889-bc20-efb48376ab4a | -12.556 | -57.1798 | 2026-06-03 14:40:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 108.4 |
| 8f4b4eae-3a20-3150-b5c1-45af25176ed7 | -14.1541 | -58.9755 | 2026-06-03 14:50:00 | GOES-19 | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | 288.5 |
| e49003f4-f52f-3e1a-9823-247b59c2991e | -11.6329 | -55.1844 | 2026-06-03 14:50:00 | GOES-19 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 130.5 |
| f9661599-26f1-34c6-a015-0c303a32c4e0 | -12.4283 | -58.4048 | 2026-06-03 14:50:00 | GOES-19 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 66.7 |
| b76f02cc-c305-3400-a1e7-a93efbeb7657 | -14.1735 | -58.9539 | 2026-06-03 14:50:00 | GOES-19 | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | 277.2 |
| d5ed2498-aeb5-3955-99c1-e1144278f223 | -14.1737 | -58.934 | 2026-06-03 14:50:00 | GOES-19 | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | 74.7 |
| b48e852d-f370-3d50-99e8-ea279cb34025 | -14.0919 | -59.3777 | 2026-06-03 14:50:00 | GOES-19 | NOVA LACERDA | MATO GROSSO | Brasil | 5106182 | 51 | 33 | nan | nan | nan | Cerrado | 61.0 |
| 7c645db7-77b9-32f0-89d4-143c228c8755 | -11.614 | -55.1861 | 2026-06-03 14:50:00 | GOES-19 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 106.7 |
| a46f926d-4ffe-37e8-a68a-c4de73cd054c | -12.556 | -57.1798 | 2026-06-03 14:50:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 95.7 |
| c77ef988-a5ba-3919-aacb-6d4908004121 | -12.7463 | -54.1969 | 2026-06-03 14:50:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 84.0 |
| a4dcc499-7357-3015-9fe9-98b327457d1d | -12.7463 | -54.1969 | 2026-06-03 15:00:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 74.0 |
| cff3a0e8-3f01-3e7f-b8b7-2b38f3a0a675 | -14.1541 | -58.9755 | 2026-06-03 15:00:00 | GOES-19 | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | 121.3 |
| 7c101f73-d767-3a1c-a578-6b62860a79e0 | -11.6329 | -55.1844 | 2026-06-03 15:00:00 | GOES-19 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 165.0 |
| 78f45199-1a8c-3190-8c13-2c0bd6bdc320 | -12.4473 | -58.4033 | 2026-06-03 15:00:00 | GOES-19 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 87.4 |
| 4b9a45b2-f239-3e68-a360-f82d65be9be7 | -12.4283 | -58.4048 | 2026-06-03 15:00:00 | GOES-19 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 89.6 |
| a3ad3f1f-e55f-3e48-a7a8-70cac56b68bd | -14.1735 | -58.9539 | 2026-06-03 15:00:00 | GOES-19 | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | 108.7 |
| 5f6cb25c-e0b6-33b0-a1d7-45e30e8e7d69 | -12.7272 | -54.1988 | 2026-06-03 15:00:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 74.5 |
| a1db350e-b618-37fd-8ad9-775310e5a04a | -10.8573 | -53.7425 | 2026-06-03 15:00:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 84.6 |
| 65a9c8a9-0156-3c27-b8fc-a847ce03851a | -11.614 | -55.1861 | 2026-06-03 15:00:00 | GOES-19 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 98.2 |
| fed1bb9c-d78b-309d-8ecf-f2f7891defd2 | -14.0919 | -59.3777 | 2026-06-03 15:00:00 | GOES-19 | NOVA LACERDA | MATO GROSSO | Brasil | 5106182 | 51 | 33 | nan | nan | nan | Cerrado | 61.1 |
| b9d6f5a8-558a-3038-b491-943ebb79ba61 | -14.0917 | -59.3975 | 2026-06-03 15:10:00 | GOES-19 | NOVA LACERDA | MATO GROSSO | Brasil | 5106182 | 51 | 33 | nan | nan | nan | Cerrado | 91.9 |
| 2844d645-619f-31f8-921a-cda393374560 | -12.4283 | -58.4048 | 2026-06-03 15:10:00 | GOES-19 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 122.1 |
| e551d7c3-dd36-34e7-9f6a-16b2cd33bd0b | -14.0919 | -59.3777 | 2026-06-03 15:10:00 | GOES-19 | NOVA LACERDA | MATO GROSSO | Brasil | 5106182 | 51 | 33 | nan | nan | nan | Cerrado | 85.8 |
| 163c63c1-0160-3426-9748-00dd84b5c24b | -14.1541 | -58.9755 | 2026-06-03 15:10:00 | GOES-19 | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | 108.9 |
| 2d83d8a0-53c8-31bf-bd4c-e2e326f813f7 | -12.4473 | -58.4033 | 2026-06-03 15:10:00 | GOES-19 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 74.9 |
| 63913a37-ff84-305f-a106-b1808edb993f | -10.5736 | -57.3165 | 2026-06-03 15:10:00 | GOES-19 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 58.2 |
| 3383405c-7fe1-3ed9-8a5b-265d4dd0b05e | -11.614 | -55.1861 | 2026-06-03 15:10:00 | GOES-19 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 118.1 |
| a4734e9f-24e6-3850-b1a0-a276132cc320 | -14.0919 | -59.3777 | 2026-06-03 15:20:00 | GOES-19 | NOVA LACERDA | MATO GROSSO | Brasil | 5106182 | 51 | 33 | nan | nan | nan | Cerrado | 91.9 |
| e614c035-1918-3dbd-8588-b57805105d68 | -12.4473 | -58.4033 | 2026-06-03 15:20:00 | GOES-19 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 98.3 |
| 0852f3fc-8e6c-337c-90fd-bbca2967a31b | -14.1541 | -58.9755 | 2026-06-03 15:20:00 | GOES-19 | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | 104.2 |
| 8c437698-a580-3802-b1fe-92d116ab8f0b | -14.0917 | -59.3975 | 2026-06-03 15:20:00 | GOES-19 | NOVA LACERDA | MATO GROSSO | Brasil | 5106182 | 51 | 33 | nan | nan | nan | Cerrado | 84.3 |
| a84c0f5b-1963-3778-a5af-fb7fb245dc36 | -11.614 | -55.1861 | 2026-06-03 15:20:00 | GOES-19 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 103.5 |
| 62cd9f07-75d1-3976-b101-22a9d521a2d1 | -10.5736 | -57.3165 | 2026-06-03 15:20:00 | GOES-19 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 69.8 |
| b58e305c-0587-3dd9-b4e7-c27212a2f3d5 | -12.4283 | -58.4048 | 2026-06-03 15:20:00 | GOES-19 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 103.2 |
| 4fa7d860-b911-3eac-8719-f77104c49a25 | -14.1735 | -58.9539 | 2026-06-03 15:20:00 | GOES-19 | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | 76.9 |
| 1084aba2-e7e2-34fb-a053-fd7c7e80271f | -14.1541 | -58.9755 | 2026-06-03 15:30:00 | GOES-19 | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | 122.3 |
| ba78a24f-0131-3055-ae05-7f6b021cfd60 | -14.0917 | -59.3975 | 2026-06-03 15:30:00 | GOES-19 | NOVA LACERDA | MATO GROSSO | Brasil | 5106182 | 51 | 33 | nan | nan | nan | Cerrado | 91.3 |
| 1aa97e89-1eca-368a-8c92-b8dd15ff8acb | -12.4473 | -58.4033 | 2026-06-03 15:30:00 | GOES-19 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 99.6 |
| 81558625-1c6b-34ad-b60d-1141a95d0dbc | -10.8573 | -53.7425 | 2026-06-03 15:30:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 79.2 |
| 28348cf7-a90f-3f1f-a103-d9c051d518e3 | -12.4283 | -58.4048 | 2026-06-03 15:30:00 | GOES-19 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 104.7 |
| 04aba0f5-1211-3f2c-8d32-038668715c89 | -14.1735 | -58.9539 | 2026-06-03 15:30:00 | GOES-19 | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | 79.4 |
| c9babcb9-0780-35d1-acb1-010dc5aedca9 | -10.5736 | -57.3165 | 2026-06-03 15:30:00 | GOES-19 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 66.4 |
| dd448151-7417-3615-ac62-99092cf63e01 | -14.0919 | -59.3777 | 2026-06-03 15:30:00 | GOES-19 | NOVA LACERDA | MATO GROSSO | Brasil | 5106182 | 51 | 33 | nan | nan | nan | Cerrado | 86.3 |
| 1d3c6ac0-de39-3a4d-9823-eaf1672a0f7c | -11.614 | -55.1861 | 2026-06-03 15:30:00 | GOES-19 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 104.0 |
| 42b40911-cdff-39da-8ef3-76a4fd991e15 | -10.3675 | -64.5058 | 2026-06-03 15:30:00 | GOES-19 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 54.7 |
| 7373449d-94ad-3f1b-bf9d-ae5db01c9198 | -10.8573 | -53.7425 | 2026-06-03 15:40:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 91.9 |
| 1a510d77-e35f-321c-a66b-eb8c4dc0c344 | -14.0919 | -59.3777 | 2026-06-03 15:40:00 | GOES-19 | NOVA LACERDA | MATO GROSSO | Brasil | 5106182 | 51 | 33 | nan | nan | nan | Cerrado | 114.9 |
| f932ef87-3381-370b-8a6b-f1beade9a9c2 | -10.5736 | -57.3165 | 2026-06-03 15:40:00 | GOES-19 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 68.7 |
| ac532893-b8fa-3565-b6e9-711fcf14a352 | -12.4283 | -58.4048 | 2026-06-03 15:40:00 | GOES-19 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 121.0 |
| 115c611e-7a93-32d5-8788-38cbb5a26291 | -14.1735 | -58.9539 | 2026-06-03 15:40:00 | GOES-19 | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | 77.5 |
| 514d9268-8f38-3924-9464-1bfc44302654 | -11.614 | -55.1861 | 2026-06-03 15:40:00 | GOES-19 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 110.9 |
| 7a11f1e4-a286-3444-af70-d1dd9fd1183b | -14.1541 | -58.9755 | 2026-06-03 15:40:00 | GOES-19 | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | 168.0 |
| 9adfc0bd-7b7e-3ec4-8066-8d65e488c552 | -14.0917 | -59.3975 | 2026-06-03 15:40:00 | GOES-19 | NOVA LACERDA | MATO GROSSO | Brasil | 5106182 | 51 | 33 | nan | nan | nan | Cerrado | 99.4 |
| e4a95926-2c0d-331d-b4e3-d8de85d760b9 | -12.4473 | -58.4033 | 2026-06-03 15:40:00 | GOES-19 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 74.9 |
| a513a260-17f6-3c02-9d5a-5b3ac3a56bea | -12.4473 | -58.4033 | 2026-06-03 15:50:00 | GOES-19 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 87.0 |
| f59173cb-c5a7-3032-bba0-58e443c9d8d9 | -10.5736 | -57.3165 | 2026-06-03 15:50:00 | GOES-19 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 78.5 |
| 3230cd1a-ed76-3b91-bebd-39c62f0b868f | -14.0919 | -59.3777 | 2026-06-03 15:50:00 | GOES-19 | NOVA LACERDA | MATO GROSSO | Brasil | 5106182 | 51 | 33 | nan | nan | nan | Cerrado | 111.1 |
| f94b844a-8b87-36ec-a3b1-7b92980e3706 | -12.4283 | -58.4048 | 2026-06-03 15:50:00 | GOES-19 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 89.1 |
| 3d515443-84b5-3941-9bdd-c7dc30733fae | -14.1541 | -58.9755 | 2026-06-03 15:50:00 | GOES-19 | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | 94.9 |
| a8a61374-3235-3d64-99cd-aab172196122 | -11.614 | -55.1861 | 2026-06-03 15:50:00 | GOES-19 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 82.4 |
| 3322bf55-9c2a-3836-9feb-f541231bdd58 | -10.8573 | -53.7425 | 2026-06-03 15:50:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 93.6 |
| cbfa91bd-4bb5-35b1-99ad-3466d4884331 | -10.5966 | -53.478 | 2026-06-03 16:00:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 75.7 |
| 8ac7408a-46fd-38dc-8106-5c393c3a7a43 | -11.614 | -55.1861 | 2026-06-03 16:00:00 | GOES-19 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 87.4 |
| 0c1ed8b9-c0b5-3bed-8c7a-fe110f468f7e | -14.1541 | -58.9755 | 2026-06-03 16:00:00 | GOES-19 | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | 176.7 |
| 3467e7cb-846f-3e50-9af6-b6ef6c85a686 | -14.1735 | -58.9539 | 2026-06-03 16:00:00 | GOES-19 | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | 140.5 |


[Clique aqui para ver as próximas entradas](README13.md)
