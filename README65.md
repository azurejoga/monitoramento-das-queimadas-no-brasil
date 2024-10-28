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

## Dados Diários - Página 65

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 3a249aca-d951-39ae-a3a7-184126e1b90f | -1.17634 | -53.89239 | 2024-10-28 04:57:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 3745b256-e658-39b1-a546-428dd2362375 | -1.14481 | -53.63909 | 2024-10-28 04:57:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a39448c4-b5df-32bb-b897-683deebdd350 | -1.14426 | -53.64257 | 2024-10-28 04:57:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 849fffd9-cca5-326e-aa95-c85b1a4d1b6d | -1.08659 | -53.66127 | 2024-10-28 04:57:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| fcaaacb6-36b2-3468-be1e-edf1bb1080c6 | -1.08605 | -53.66474 | 2024-10-28 04:57:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 04a4020e-164b-3032-8e3b-45b87309633d | -1.0855 | -53.66822 | 2024-10-28 04:57:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 55b89919-d2cd-3049-b43e-53d949082f61 | -1.08496 | -53.6717 | 2024-10-28 04:57:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 3b8bf359-7667-312c-953b-e79292daf5f9 | -1.08436 | -53.65384 | 2024-10-28 04:57:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 4c30ccee-624c-3c06-87ae-1fa37e79ba51 | -1.08382 | -53.65729 | 2024-10-28 04:57:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| cc48d65f-25da-31b2-8e71-f1893635c09e | -1.08328 | -53.66074 | 2024-10-28 04:57:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| fdc058c2-a6d2-34db-8e00-4f05465948ef | -1.08274 | -53.66421 | 2024-10-28 04:57:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| afa23cfe-2b40-3e43-9d1e-fe1a6550c6a0 | -1.08219 | -53.66769 | 2024-10-28 04:57:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| f137cae9-4cf6-397f-88f2-3217f53f38ac | -1.08165 | -53.67117 | 2024-10-28 04:57:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 461d4f47-1ac2-3125-9943-8520dedb7f05 | -1.08105 | -53.65332 | 2024-10-28 04:57:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| cea44744-655b-3086-ae9e-00ec17f39de9 | -1.08051 | -53.65676 | 2024-10-28 04:57:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| fc99742b-c1ea-3fcf-a045-b60ab9d82825 | -1.07997 | -53.66021 | 2024-10-28 04:57:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 31117b1f-c351-3c4d-b669-b90abb6e4758 | -1.07943 | -53.66368 | 2024-10-28 04:57:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 174f001d-c332-316f-8321-c7846d4a14ea | -1.07888 | -53.66716 | 2024-10-28 04:57:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 57d1106e-8c16-367e-a5ce-3eeaa83be4fc | -1.07834 | -53.67065 | 2024-10-28 04:57:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 19e97a9c-8b16-3915-945f-5e74f9c892a0 | -1.07666 | -53.65971 | 2024-10-28 04:57:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| ecea9ab8-8edf-3e4a-a77a-84e3b570273b | -1.07497 | -53.6489 | 2024-10-28 04:57:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 91907c2d-c1fb-3b78-ab76-9129fb92e7ed | -1.07443 | -53.65233 | 2024-10-28 04:57:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 9ff512c6-bd4b-3d06-9628-c4a1eeb5b609 | -1.07281 | -53.66265 | 2024-10-28 04:57:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| c71cb323-d73d-3927-83e2-1e59a765764f | -1.07057 | -53.65527 | 2024-10-28 04:57:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 3154baaf-06a8-3f9d-b546-46e7c6fcd82b | -1.07003 | -53.65871 | 2024-10-28 04:57:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 6be470d6-a0c8-3a76-9016-8f0f29c5bed0 | -1.06949 | -53.66215 | 2024-10-28 04:57:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 7479ae31-d418-3545-ad61-383ad33bc318 | -1.06841 | -53.66908 | 2024-10-28 04:57:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| bdfbb9c7-edb6-3023-ae86-3247d6daf43e | -1.06672 | -53.6582 | 2024-10-28 04:57:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 11a6096e-3c3f-32b5-b085-b7ee4c6f3ea7 | -1.06618 | -53.66164 | 2024-10-28 04:57:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| bcd9171b-88cb-3bff-a1dc-6e9ac9b73af5 | -0.99563 | -53.70028 | 2024-10-28 04:57:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 17461759-e529-323d-8bc3-91db4dbf15ff | -0.99509 | -53.70374 | 2024-10-28 04:57:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| b756b8a8-350b-3fa4-ad4f-6c53bdcde0d6 | -0.9932 | -53.6926 | 2024-10-28 04:57:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 8b452f0f-5710-31cd-bb0b-6ef442644901 | -0.99266 | -53.69607 | 2024-10-28 04:57:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| d8bc61ae-9b17-34ad-b3fc-b5e24af59d49 | -0.99212 | -53.69953 | 2024-10-28 04:57:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| fdc80c7d-63ff-327b-8b30-957b74c9e3e4 | -0.99158 | -53.703 | 2024-10-28 04:57:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 229a92ec-5d34-317b-9987-0e95793bca90 | -0.99104 | -53.70646 | 2024-10-28 04:57:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 1a6e7a79-c9d1-3105-8327-b69a896172ce | -0.99043 | -53.68864 | 2024-10-28 04:57:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| e376062c-092a-3cfc-a460-a8a30b32363f | -0.98989 | -53.69209 | 2024-10-28 04:57:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 37dbb5fe-caa8-34bb-aaa4-5315c682f044 | -0.98935 | -53.69555 | 2024-10-28 04:57:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 034a23f3-c219-37f9-91f3-644d7ad574fc | -0.98881 | -53.69902 | 2024-10-28 04:57:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 3212001b-74ea-34e0-bcb2-0ef6de3e21f5 | -0.98826 | -53.70249 | 2024-10-28 04:57:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 010d0bbe-ea58-3a6b-925c-83f9547beb80 | -0.98772 | -53.70595 | 2024-10-28 04:57:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 27b35595-8aa8-358b-b1e4-2211bc21d3b7 | -0.98718 | -53.70939 | 2024-10-28 04:57:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 9f93ca18-2eca-3653-b728-216187ae0831 | -0.98712 | -53.68813 | 2024-10-28 04:57:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 4d666e04-f651-3fde-9769-dc603af3bbcd | -0.98658 | -53.69158 | 2024-10-28 04:57:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| c272c5fe-9a0a-33a5-bac8-3dcd9de92d47 | -0.9855 | -53.6985 | 2024-10-28 04:57:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 719e7cfe-0f63-37e3-a0e3-97f60efaabc6 | -0.98495 | -53.70197 | 2024-10-28 04:57:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| b7b560e1-832b-357d-838e-e05558691b37 | -0.98441 | -53.70544 | 2024-10-28 04:57:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 2a9ca8c8-933e-3ea9-95f8-cae380613085 | -0.98387 | -53.70888 | 2024-10-28 04:57:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 94ed9f55-2548-3b43-8e82-36d5c911d686 | -0.98327 | -53.69106 | 2024-10-28 04:57:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 79cbd17f-b515-361d-bb57-465312ccbf88 | -0.98273 | -53.6945 | 2024-10-28 04:57:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 628ce018-77e0-324a-80f3-d6931ae68f29 | -0.98218 | -53.69797 | 2024-10-28 04:57:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| c36db831-ab34-3df4-a14a-1c9a05fbe1d3 | -0.98164 | -53.70145 | 2024-10-28 04:57:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| d8a5599a-7b6f-39cc-aa7b-56d9d95ac546 | -0.9811 | -53.70493 | 2024-10-28 04:57:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 679ce9df-9eea-3e41-ab78-9c3fbd41b250 | -0.98056 | -53.70837 | 2024-10-28 04:57:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| b5dd56d2-8e08-3a20-b0ce-9e6ad45a7613 | -0.97941 | -53.69398 | 2024-10-28 04:57:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 3bf6b7a9-0097-3d23-bcb9-e19bf3d493f7 | -0.97887 | -53.69744 | 2024-10-28 04:57:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| d60a2107-88b2-32ee-b89b-e2baa1cc5498 | -0.97833 | -53.70093 | 2024-10-28 04:57:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| a2468f0d-b2d7-3c14-a604-3911020840b6 | -0.97778 | -53.7044 | 2024-10-28 04:57:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 28a4ee76-5c6a-3f50-bfab-e1645b8f8440 | -0.97724 | -53.70784 | 2024-10-28 04:57:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 34a04a2a-65f1-3b65-9794-24528fd03fb2 | -0.97671 | -53.71127 | 2024-10-28 04:57:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| f288da3a-65c0-344a-a57b-2d3e15537350 | -0.97556 | -53.69693 | 2024-10-28 04:57:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 37a8329a-900b-32a4-8268-84ae30e27087 | -0.87802 | -53.68914 | 2024-10-28 04:57:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d120b5c7-c854-33c1-971c-4465c31a7af1 | -1.25475 | -53.39178 | 2024-10-28 04:57:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 0eb43f62-22a9-3366-a41b-db361cc2f150 | -1.18909 | -53.50834 | 2024-10-28 04:57:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| eb99c494-cb86-381a-b8be-b1e1de839d04 | -1.18633 | -53.50438 | 2024-10-28 04:57:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 1ce8d72c-2403-36ae-94b9-bbadff8fbf27 | -1.18579 | -53.50782 | 2024-10-28 04:57:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 5faedad8-773e-336d-98b3-d74ce5929729 | -1.18524 | -53.51127 | 2024-10-28 04:57:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 7dc844f7-e107-382a-90e8-aa9ba958308c | -1.18302 | -53.50386 | 2024-10-28 04:57:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 5e9d02c8-f850-3cac-b63a-a426d37bffa2 | -1.18248 | -53.50731 | 2024-10-28 04:57:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 830c061f-6f07-362f-8781-384d65ef5472 | -1.17972 | -53.50335 | 2024-10-28 04:57:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 13.5 |
| 07e15b2f-5ed3-3351-bfa2-223ce19229fc | -1.17918 | -53.50679 | 2024-10-28 04:57:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 13.5 |
| cec2c53a-422d-3a26-8df2-8e91f8256f59 | -1.17863 | -53.51026 | 2024-10-28 04:57:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 2cd0da68-c4a9-3975-b1d6-8b75c2ddb76c | -1.17695 | -53.49941 | 2024-10-28 04:57:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 6e79d488-aba0-3149-9fb5-84824690fdb5 | -1.17665 | -53.39379 | 2024-10-28 04:57:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 2184bb7e-828f-3744-abcd-08ec983da868 | -1.17642 | -53.50283 | 2024-10-28 04:57:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 13.5 |
| 7fbb4ac1-ca2b-380c-a7db-280a4662231d | -1.17587 | -53.50628 | 2024-10-28 04:57:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 13.5 |
| b889ec5a-3d21-3b21-b801-07db398b7ca4 | -1.17533 | -53.50975 | 2024-10-28 04:57:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| e729257a-cac7-3258-8258-5b4b278fe0bc | -1.17365 | -53.4989 | 2024-10-28 04:57:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 50450b2d-eb1e-356f-b2ed-abb8b673aeeb | -1.17311 | -53.50233 | 2024-10-28 04:57:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| bd887ff0-464a-3b88-a536-66aa966f6b0e | -1.17257 | -53.50577 | 2024-10-28 04:57:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| f69d1f71-8036-3873-a5ec-98bec58b16bd | -1.17035 | -53.49839 | 2024-10-28 04:57:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 3ec88481-352f-345f-b8d3-ca6c043ecf1a | -1.16981 | -53.50182 | 2024-10-28 04:57:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| ff59eb1c-c8c2-3584-be5c-049d5c0165f2 | -1.03347 | -53.37078 | 2024-10-28 04:57:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| c93dbee5-d963-33ed-a3b6-f569d602c9d1 | -1.29173 | -54.19694 | 2024-10-28 04:57:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| ff7cf92a-20f8-3905-821c-57b0dfd8d536 | -1.27779 | -54.13362 | 2024-10-28 04:57:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 45a78083-845a-3219-b886-89bc7aa9f61c | -1.27499 | -54.12965 | 2024-10-28 04:57:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 9cb4918b-dd9e-3a25-a1f5-72f32ae27530 | -1.27445 | -54.13311 | 2024-10-28 04:57:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| c5fba997-ee9c-3031-8fe8-42444cce8508 | -1.23204 | -54.14458 | 2024-10-28 04:57:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| b7257390-46d4-3936-977c-d04a5b8d1a47 | -1.2042 | -54.16945 | 2024-10-28 04:57:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| ae96ebac-1f10-32fd-832d-4e88c9b66361 | -1.20242 | -54.52233 | 2024-10-28 04:57:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 92cd147f-1aff-3fff-a892-ddf512a6eab0 | -1.18138 | -54.11896 | 2024-10-28 04:57:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| eb5fe78c-d273-3e88-8499-1291f9c98a99 | -1.1758 | -54.19764 | 2024-10-28 04:57:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 2a491458-a542-3a0c-9f98-debff9cb2ba9 | -1.17579 | -54.52592 | 2024-10-28 04:57:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 5c6f00ec-8ace-34d3-a0a7-6daac85a7d0c | -1.13961 | -54.10543 | 2024-10-28 04:57:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 867cf234-f753-3db6-9f2c-4d26c505fad4 | -1.13627 | -54.10491 | 2024-10-28 04:57:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 3222b962-95f0-3828-b66d-6b2ea2ffb3c3 | -1.12131 | -54.13499 | 2024-10-28 04:57:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| b8117985-355e-30b8-9ec3-a7785f4fecc6 | -1.11852 | -54.13092 | 2024-10-28 04:57:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| baeee350-4333-3c5c-9e94-5f4eb570a60c | -1.11797 | -54.13445 | 2024-10-28 04:57:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 3e77507b-ac15-3815-b08d-9096a7e938fa | -1.11519 | -54.13036 | 2024-10-28 04:57:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |


[Clique aqui para ver as próximas entradas](README66.md)
