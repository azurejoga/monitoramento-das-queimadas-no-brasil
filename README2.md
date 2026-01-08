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

## Dados Diários - Página 2

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 366c7fcd-3d90-380d-920e-873aa157f4be | -4.2539 | -43.7843 | 2026-01-08 01:20:00 | GOES-19 | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 61.6 |
| 45c17565-c7ac-3a0f-9918-21da78decc79 | -4.2726 | -43.7832 | 2026-01-08 01:20:00 | GOES-19 | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 104.5 |
| 32d1f012-70f0-3b38-a610-533a8ab3976b | -1.3309 | -53.1907 | 2026-01-08 01:20:00 | GOES-19 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 48.8 |
| 067286f2-3695-343a-8122-e6e79af0e4bf | -4.2728 | -43.7601 | 2026-01-08 01:20:00 | GOES-19 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 108.9 |
| d4e401dd-9bcf-3c36-b735-29449114d427 | -3.7136 | -46.9843 | 2026-01-08 01:20:00 | GOES-19 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 58.9 |
| 0fbc7fd6-8d20-3902-a55d-a6855e71dc53 | -3.695 | -46.9851 | 2026-01-08 01:20:00 | GOES-19 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 63.1 |
| 41db95eb-40da-314c-aa18-463222692997 | -4.2726 | -43.7832 | 2026-01-08 01:30:00 | GOES-19 | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 111.9 |
| 3290310b-f026-3b2e-bf07-cc3f5add33e1 | -4.2539 | -43.7843 | 2026-01-08 01:30:00 | GOES-19 | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 79.8 |
| 2769ce37-9a67-32d4-9f21-0467ed6a70a5 | -4.2728 | -43.7601 | 2026-01-08 01:30:00 | GOES-19 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 140.3 |
| b32aa9b6-d0ff-3110-9470-7c86d6e15026 | -4.2541 | -43.7612 | 2026-01-08 01:30:00 | GOES-19 | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 69.1 |
| 02ba3da3-154a-32a1-8141-519cd673908e | 3.2859 | -60.071602 | 2026-01-08 01:39:00 | METOP-C | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| 86f38c3e-ed76-3952-88cd-c1397e769ff6 | -20.8927 | -52.33 | 2026-01-08 01:40:00 | GOES-19 | TRÊS LAGOAS | MATO GROSSO DO SUL | Brasil | 5008305 | 50 | 33 | nan | nan | nan | Cerrado | 84.3 |
| ef941604-924b-35b6-9c3a-129c0ddd5f5e | -4.2726 | -43.7832 | 2026-01-08 01:40:00 | GOES-19 | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 157.3 |
| 74e26afe-6c06-3320-8e8f-fd193a8b4738 | -20.8921 | -52.3522 | 2026-01-08 01:40:00 | GOES-19 | TRÊS LAGOAS | MATO GROSSO DO SUL | Brasil | 5008305 | 50 | 33 | nan | nan | nan | Cerrado | 86.3 |
| 8c07e1a5-e61d-372d-bb10-3ecf65f99d1e | -4.2728 | -43.7601 | 2026-01-08 01:40:00 | GOES-19 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 186.4 |
| 1ae44401-c898-30e0-becd-5bda8740a814 | -4.2539 | -43.7843 | 2026-01-08 01:40:00 | GOES-19 | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 98.1 |
| e3a4694e-0f2e-37ae-9b81-566f1b2530fc | -4.2541 | -43.7612 | 2026-01-08 01:40:00 | GOES-19 | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 80.2 |
| 1e5f9e79-7902-36f8-81de-4ce0eef90a9c | -4.2539 | -43.7843 | 2026-01-08 01:50:00 | GOES-19 | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 108.0 |
| 598732fa-5b64-3c22-9baa-c9f55026bb82 | -4.2728 | -43.7601 | 2026-01-08 01:50:00 | GOES-19 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 210.9 |
| 0195a689-b73c-3d25-896d-f9989c9b8fea | -22.8293 | -49.2836 | 2026-01-08 01:50:00 | GOES-19 | ÁGUAS DE SANTA BÁRBARA | SÃO PAULO | Brasil | 3500550 | 35 | 33 | nan | nan | nan | Cerrado | 101.7 |
| edfcc941-659d-3027-bc17-7dfb7bb19ff1 | -20.8927 | -52.33 | 2026-01-08 01:50:00 | GOES-19 | TRÊS LAGOAS | MATO GROSSO DO SUL | Brasil | 5008305 | 50 | 33 | nan | nan | nan | Cerrado | 87.6 |
| 6ca33f72-5732-3527-8397-59e171cd257e | -20.8921 | -52.3522 | 2026-01-08 01:50:00 | GOES-19 | TRÊS LAGOAS | MATO GROSSO DO SUL | Brasil | 5008305 | 50 | 33 | nan | nan | nan | Cerrado | 91.9 |
| 90ff9d4d-da58-30a2-b709-027b413bedde | -4.2726 | -43.7832 | 2026-01-08 01:50:00 | GOES-19 | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 177.4 |
| 96520243-2a63-3c3c-9cb8-73daa07e6b20 | -4.2541 | -43.7612 | 2026-01-08 01:50:00 | GOES-19 | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 82.2 |
| 565b2c63-894e-3d04-b037-01cc216a0c6c | -4.2914 | -43.7591 | 2026-01-08 02:00:00 | GOES-19 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 94.3 |
| 1ab68b10-3bf2-3533-9343-2ef700db33d8 | -4.2541 | -43.7612 | 2026-01-08 02:00:00 | GOES-19 | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 69.2 |
| 45b419a1-cbfa-345f-aa3b-a2bddf9cef53 | -4.2728 | -43.7601 | 2026-01-08 02:00:00 | GOES-19 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 249.3 |
| 2db5637c-5190-3393-9247-e2227a67783b | -4.2913 | -43.7822 | 2026-01-08 02:00:00 | GOES-19 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 77.8 |
| 675e2e03-6358-3b32-afd4-70ad0761450b | -4.2726 | -43.7832 | 2026-01-08 02:00:00 | GOES-19 | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 218.1 |
| 5a5b8215-4cee-3687-840a-2d51b8d3da7b | -20.8921 | -52.3522 | 2026-01-08 02:00:00 | GOES-19 | TRÊS LAGOAS | MATO GROSSO DO SUL | Brasil | 5008305 | 50 | 33 | nan | nan | nan | Cerrado | 80.6 |
| 3b99a7c9-6944-310c-a54c-c50b740a6fd5 | -4.2539 | -43.7843 | 2026-01-08 02:00:00 | GOES-19 | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 85.6 |
| e9416f1c-1f17-3744-9ada-d93ab54ea058 | -4.2726 | -43.7832 | 2026-01-08 02:10:00 | GOES-19 | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 225.4 |
| bfcc3eb4-65f1-3cbf-8ff6-0251c8f77cc2 | -4.2541 | -43.7612 | 2026-01-08 02:10:00 | GOES-19 | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 57.2 |
| 6afb5c53-58d3-306b-a2e4-bf8c5741c09f | -4.2539 | -43.7843 | 2026-01-08 02:10:00 | GOES-19 | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 72.8 |
| 8ccf6dff-85c3-3c6b-b48d-423b2f9aa34c | -4.2728 | -43.7601 | 2026-01-08 02:10:00 | GOES-19 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 274.0 |
| 29cdd936-3532-36b3-aec6-0b8d5383da7e | -4.2913 | -43.7822 | 2026-01-08 02:10:00 | GOES-19 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 72.5 |
| a3c28fb6-ef85-3087-ad26-7c64391af3e3 | -22.8293 | -49.2836 | 2026-01-08 02:10:00 | GOES-19 | ÁGUAS DE SANTA BÁRBARA | SÃO PAULO | Brasil | 3500550 | 35 | 33 | nan | nan | nan | Cerrado | 97.7 |
| f2c5d8b5-bc9f-3824-9d78-a8fcfa21cac7 | -4.2914 | -43.7591 | 2026-01-08 02:10:00 | GOES-19 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 90.4 |
| dfa7b8e7-cf5d-3f99-bf58-41ac318e3ba9 | -4.2914 | -43.7591 | 2026-01-08 02:20:00 | GOES-19 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 88.9 |
| 3ef3f052-33e5-359c-baa1-524998bc3ca5 | -4.2539 | -43.7843 | 2026-01-08 02:20:00 | GOES-19 | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 63.7 |
| 865050d7-0352-3d10-931f-445737a9c61e | -4.2726 | -43.7832 | 2026-01-08 02:20:00 | GOES-19 | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 239.9 |
| 4c2508c7-93d1-346e-8be5-6d2b738ee4bd | -4.2541 | -43.7612 | 2026-01-08 02:20:00 | GOES-19 | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 54.7 |
| e1f3f9ac-0886-35ea-957f-b51c06b8a330 | -4.2728 | -43.7601 | 2026-01-08 02:20:00 | GOES-19 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 262.3 |
| 00004c25-3f87-3ad0-9696-39ae20e0b9b7 | -4.2913 | -43.7822 | 2026-01-08 02:20:00 | GOES-19 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 80.5 |
| d8e095b7-9a5a-3afa-952f-d5675a66be90 | -4.2728 | -43.7601 | 2026-01-08 02:30:00 | GOES-19 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 267.4 |
| 511c807b-c01e-3f57-9e8b-39c754e2af40 | -4.2726 | -43.7832 | 2026-01-08 02:30:00 | GOES-19 | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 276.2 |
| a24755fd-be54-354c-89ea-1b1a75f99493 | -4.2539 | -43.7843 | 2026-01-08 02:30:00 | GOES-19 | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 62.2 |
| 14592c40-312f-3533-b290-12af7bc1d9ba | -10.1806 | -36.2962 | 2026-01-08 02:30:00 | GOES-19 | CORURIPE | ALAGOAS | Brasil | 2702306 | 27 | 33 | nan | nan | nan | Mata Atlântica | 97.5 |
| 4f9056df-54cb-35b8-9cbd-15083dd14ab6 | -4.2914 | -43.7591 | 2026-01-08 02:30:00 | GOES-19 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 100.2 |
| c0370f48-49a3-3dd5-8563-1881158cb5ec | -4.2913 | -43.7822 | 2026-01-08 02:30:00 | GOES-19 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 102.0 |
| 89264ec6-87f0-347e-a69f-f850fea3f4c1 | -4.2726 | -43.7832 | 2026-01-08 02:40:00 | GOES-19 | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 168.3 |
| 44f5258c-ba34-3ce7-9bd8-a0c77708431c | -4.2728 | -43.7601 | 2026-01-08 02:40:00 | GOES-19 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 229.7 |
| e4165463-d5c7-3ac5-b257-5cc8d99e6187 | -4.2913 | -43.7822 | 2026-01-08 02:40:00 | GOES-19 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 59.3 |
| 4929ecf5-0142-346f-82c4-f394405e1b11 | -4.2914 | -43.7591 | 2026-01-08 02:40:00 | GOES-19 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 74.1 |
| 5ea97ceb-bfd1-3a48-bc2f-f3b66f3578b1 | -4.2726 | -43.7832 | 2026-01-08 02:50:00 | GOES-19 | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 138.3 |
| 3203748b-0fa9-367f-8e51-581c19558630 | -4.2728 | -43.7601 | 2026-01-08 02:50:00 | GOES-19 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 132.5 |
| bae6b796-6d10-3be0-ab91-1e59e4682add | -4.2914 | -43.7591 | 2026-01-08 03:00:00 | GOES-19 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 53.2 |
| 322932fb-418c-357e-b534-bb67b38c5ce8 | -4.2728 | -43.7601 | 2026-01-08 03:00:00 | GOES-19 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 143.8 |
| 5d8b0c20-1e76-3b96-a69b-2da847561e42 | -22.8293 | -49.2836 | 2026-01-08 03:00:00 | GOES-19 | ÁGUAS DE SANTA BÁRBARA | SÃO PAULO | Brasil | 3500550 | 35 | 33 | nan | nan | nan | Cerrado | 89.1 |
| 952afd06-dcce-3b4e-9382-5e06c90be4b7 | -4.2726 | -43.7832 | 2026-01-08 03:00:00 | GOES-19 | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 122.9 |
| 5f861334-38bc-3066-924b-1f0ceed94b4e | -4.2726 | -43.7832 | 2026-01-08 03:10:00 | GOES-19 | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 136.2 |
| 4c84348e-519a-339c-ac1e-03864aca75db | -4.2914 | -43.7591 | 2026-01-08 03:10:00 | GOES-19 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 51.4 |
| 7f388a09-6cfc-30ef-a88c-95a133bd3106 | -4.2728 | -43.7601 | 2026-01-08 03:10:00 | GOES-19 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 119.9 |
| d0fe1dc4-7169-30b2-98e8-46a3057cb1b6 | -22.8293 | -49.2836 | 2026-01-08 03:10:00 | GOES-19 | ÁGUAS DE SANTA BÁRBARA | SÃO PAULO | Brasil | 3500550 | 35 | 33 | nan | nan | nan | Cerrado | 89.7 |
| f5e8385c-d6de-3b1c-8514-d984434bc9bf | -4.2913 | -43.7822 | 2026-01-08 03:10:00 | GOES-19 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 53.6 |
| 925e134d-84d9-3f38-bbaa-72e8df7cddbe | -4.2726 | -43.7832 | 2026-01-08 03:20:00 | GOES-19 | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 44.6 |
| abc0a3b5-1921-34af-9360-3a2f3ef5b5a9 | -4.2728 | -43.7601 | 2026-01-08 03:20:00 | GOES-19 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 49.4 |
| f31f8cf3-be0d-356d-b7f0-d2c6c7dd9566 | -4.2914 | -43.7591 | 2026-01-08 03:30:00 | GOES-19 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 53.5 |
| 786798de-1ad3-3512-8d88-5e7ca1683d86 | -4.2726 | -43.7832 | 2026-01-08 03:30:00 | GOES-19 | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 84.1 |
| fa179e21-433e-3e39-98b7-80d5f7c03338 | -4.2728 | -43.7601 | 2026-01-08 03:30:00 | GOES-19 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 90.9 |
| 8f07b382-6d67-3d79-a78c-b87f8d0b5f8d | -4.2728 | -43.7601 | 2026-01-08 03:40:00 | GOES-19 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 74.3 |
| 284d0a94-cf27-384a-80a7-6aa08a4db774 | -4.2726 | -43.7832 | 2026-01-08 03:40:00 | GOES-19 | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 67.1 |
| 1d5b2471-5bba-3b9f-aaea-31aa134acfb2 | -3.23547 | -41.80013 | 2026-01-08 03:51:00 | NPP-375D | BURITI DOS LOPES | PIAUÍ | Brasil | 2202000 | 22 | 33 | nan | nan | nan | Caatinga | 4.6 |
| 56501a2e-7eb2-35c4-b528-cc991f088610 | -2.93909 | -41.79422 | 2026-01-08 03:51:00 | NPP-375D | PARNAÍBA | PIAUÍ | Brasil | 2207702 | 22 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 5874737c-965f-39ba-a301-a52657c14f57 | -2.92315 | -40.37201 | 2026-01-08 03:51:00 | NPP-375D | CRUZ | CEARÁ | Brasil | 2304251 | 23 | 33 | nan | nan | nan | Caatinga | 11.1 |
| b716ab8b-5423-3a51-a297-b5ec89aea9a4 | -3.93674 | -41.8944 | 2026-01-08 03:51:00 | NPP-375D | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 5d1a5a16-f46d-3a07-a26f-70a970f44301 | -3.48342 | -42.42949 | 2026-01-08 03:51:00 | NPP-375D | JOCA MARQUES | PIAUÍ | Brasil | 2205458 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| d7b1146c-89f6-3bf0-a01e-4f5256bdb882 | -2.93971 | -41.7903 | 2026-01-08 03:51:00 | NPP-375D | PARNAÍBA | PIAUÍ | Brasil | 2207702 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 33aa0168-88e8-3536-945f-25745ca7d8e4 | -2.92238 | -40.3768 | 2026-01-08 03:51:00 | NPP-375D | CRUZ | CEARÁ | Brasil | 2304251 | 23 | 33 | nan | nan | nan | Caatinga | 9.2 |
| f37e8093-38e6-3af8-83a0-38bda8de928a | -2.99666 | -40.10963 | 2026-01-08 03:51:00 | NPP-375D | ACARAÚ | CEARÁ | Brasil | 2300200 | 23 | 33 | nan | nan | nan | Caatinga | 7.6 |
| 7f96aa7b-bda8-3294-af28-4669825adc64 | -10.18016 | -39.05191 | 2026-01-08 03:53:00 | NPP-375D | CANUDOS | BAHIA | Brasil | 2906824 | 29 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 92854881-5c37-3d3c-92bf-bed6cd2e3426 | -5.24809 | -37.50352 | 2026-01-08 03:53:00 | NPP-375D | MOSSORÓ | RIO GRANDE DO NORTE | Brasil | 2408003 | 24 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 6c40b2f7-5f48-36b7-a83f-60462356d9cb | -7.71279 | -45.62209 | 2026-01-08 03:53:00 | NPP-375D | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| c2787612-b640-3d9c-9462-c8f0e99d8496 | -4.27543 | -43.78389 | 2026-01-08 03:53:00 | NPP-375D | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 5ba7a970-a212-358b-9e37-79999204646e | -7.56422 | -45.62989 | 2026-01-08 03:53:00 | NPP-375D | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 0e8eecc1-fdc8-369c-bb43-a825fd00cec4 | -5.2845 | -45.83229 | 2026-01-08 03:53:00 | NPP-375D | ITAIPAVA DO GRAJAÚ | MARANHÃO | Brasil | 2105351 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| db478e68-4347-3288-a020-579acdaec961 | -6.33961 | -43.38367 | 2026-01-08 03:53:00 | NPP-375D | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 53701af7-da2c-38d6-97a3-8846fe5e89c3 | -5.15949 | -38.08125 | 2026-01-08 03:53:00 | NPP-375D | LIMOEIRO DO NORTE | CEARÁ | Brasil | 2307601 | 23 | 33 | nan | nan | nan | Caatinga | 0.5 |
| c1244df4-4b9c-3966-917e-7c6c7dd7bc94 | -8.82294 | -39.82766 | 2026-01-08 03:53:00 | NPP-375D | CURAÇÁ | BAHIA | Brasil | 2909901 | 29 | 33 | nan | nan | nan | Caatinga | 3.4 |
| c39fb4db-3347-30c7-9790-c3b00f100760 | -5.75286 | -45.11345 | 2026-01-08 03:53:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 0.4 |
| a0f7d0d2-a49e-3e68-a61b-c8e92aa0eef2 | -5.1756 | -37.76377 | 2026-01-08 03:53:00 | NPP-375D | BARAÚNA | RIO GRANDE DO NORTE | Brasil | 2401453 | 24 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 07d8e5ac-ff0c-3b3e-a6b7-3995f35e1187 | -7.56984 | -45.62777 | 2026-01-08 03:53:00 | NPP-375D | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 797190d9-7789-3c86-bbde-60d2c88520aa | -5.93918 | -44.44902 | 2026-01-08 03:53:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 2da29ad3-f4cb-35a7-a4c6-e36354716cdb | -5.09959 | -37.95689 | 2026-01-08 03:53:00 | NPP-375D | QUIXERÉ | CEARÁ | Brasil | 2311504 | 23 | 33 | nan | nan | nan | Caatinga | 1.7 |
| f9b10e02-5bad-3d87-b265-508f33a73f82 | -6.27544 | -39.89318 | 2026-01-08 03:53:00 | NPP-375D | CATARINA | CEARÁ | Brasil | 2303600 | 23 | 33 | nan | nan | nan | Caatinga | 1.8 |
| ff47f173-4ed7-3e9c-923a-63750a89242d | -6.56261 | -38.17409 | 2026-01-08 03:53:00 | NPP-375D | LASTRO | PARAÍBA | Brasil | 2508406 | 25 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 17923278-019f-33f2-9b08-6988507d3077 | -4.28103 | -43.77959 | 2026-01-08 03:53:00 | NPP-375D | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 8.0 |
| d78d3e16-f339-344c-b990-4372a35cd7c1 | -4.27801 | -43.76868 | 2026-01-08 03:53:00 | NPP-375D | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 13.0 |
| b86fa3c0-59ca-3bb6-b25a-ac5f95e16db5 | -5.944 | -44.44991 | 2026-01-08 03:53:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 1b92c6ee-1e2b-3705-93f4-37bab492525c | -5.09621 | -37.95636 | 2026-01-08 03:53:00 | NPP-375D | QUIXERÉ | CEARÁ | Brasil | 2311504 | 23 | 33 | nan | nan | nan | Caatinga | 7.2 |


[Clique aqui para ver as próximas entradas](README3.md)
