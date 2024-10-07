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

## Dados Diários - Página 69

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| bc0c7a57-9155-3a0e-9e3e-69c2307f4425 | -21.28393 | -47.38744 | 2024-10-07 04:04:00 | NOAA-20 | CAJURU | SÃO PAULO | Brasil | 3509403 | 35 | 33 | nan | nan | nan | Cerrado | 1.8 |
| e6206c79-f7bc-34c3-9ad8-708087aa7f59 | -21.28326 | -47.38507 | 2024-10-07 04:04:00 | NOAA-20 | CAJURU | SÃO PAULO | Brasil | 3509403 | 35 | 33 | nan | nan | nan | Cerrado | 1.4 |
| da425558-b2e3-30f0-acb0-2159c9d441af | -21.28304 | -47.39226 | 2024-10-07 04:04:00 | NOAA-20 | CAJURU | SÃO PAULO | Brasil | 3509403 | 35 | 33 | nan | nan | nan | Cerrado | 16.1 |
| 41f636ee-1eac-3b77-8938-d44ee4fcbfac | -21.28215 | -47.39707 | 2024-10-07 04:04:00 | NOAA-20 | CAJURU | SÃO PAULO | Brasil | 3509403 | 35 | 33 | nan | nan | nan | Cerrado | 16.1 |
| f72b1dab-609c-3111-9c40-cc8fd809d98a | -21.28154 | -47.3947 | 2024-10-07 04:04:00 | NOAA-20 | CAJURU | SÃO PAULO | Brasil | 3509403 | 35 | 33 | nan | nan | nan | Cerrado | 14.8 |
| 2212b091-45b3-3e37-8720-e549ef65658c | -21.28068 | -47.39952 | 2024-10-07 04:04:00 | NOAA-20 | SANTA CRUZ DA ESPERANÇA | SÃO PAULO | Brasil | 3546256 | 35 | 33 | nan | nan | nan | Cerrado | 14.8 |
| 3a11058a-e208-3c82-8de5-5163bb959b1f | -21.27845 | -47.39624 | 2024-10-07 04:04:00 | NOAA-20 | CAJURU | SÃO PAULO | Brasil | 3509403 | 35 | 33 | nan | nan | nan | Cerrado | 16.1 |
| 3602c2d7-f2e8-3ec1-a5dc-1b24617751c2 | -21.27698 | -47.39868 | 2024-10-07 04:04:00 | NOAA-20 | SANTA CRUZ DA ESPERANÇA | SÃO PAULO | Brasil | 3546256 | 35 | 33 | nan | nan | nan | Cerrado | 14.8 |
| 16b10546-aab5-3983-869a-cac116676caf | -21.27666 | -47.4059 | 2024-10-07 04:04:00 | NOAA-20 | SANTA CRUZ DA ESPERANÇA | SÃO PAULO | Brasil | 3546256 | 35 | 33 | nan | nan | nan | Cerrado | 1.8 |
| b9bfdedf-723a-39ba-900c-aad617c53acf | -21.27611 | -47.40352 | 2024-10-07 04:04:00 | NOAA-20 | SANTA CRUZ DA ESPERANÇA | SÃO PAULO | Brasil | 3546256 | 35 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 4f423700-f36f-3414-9f97-c503f7350df4 | -21.27327 | -47.39786 | 2024-10-07 04:04:00 | NOAA-20 | SANTA CRUZ DA ESPERANÇA | SÃO PAULO | Brasil | 3546256 | 35 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 62000122-7c4d-3c25-af77-f2b14887652e | -21.26869 | -47.40192 | 2024-10-07 04:04:00 | NOAA-20 | SANTA CRUZ DA ESPERANÇA | SÃO PAULO | Brasil | 3546256 | 35 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 0e990ce3-ab64-33c3-81ac-58dec463f1c9 | -21.1476 | -47.74635 | 2024-10-07 04:04:00 | NOAA-20 | RIBEIRÃO PRETO | SÃO PAULO | Brasil | 3543402 | 35 | 33 | nan | nan | nan | Cerrado | 1.2 |
| a3854c0d-3c25-3253-a4c8-f8b601297da1 | -21.08413 | -47.23561 | 2024-10-07 04:04:00 | NOAA-20 | SANTO ANTÔNIO DA ALEGRIA | SÃO PAULO | Brasil | 3547908 | 35 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 004f6fb9-54bb-3890-8076-d06a29f3c6a7 | -21.08325 | -47.24057 | 2024-10-07 04:04:00 | NOAA-20 | SANTO ANTÔNIO DA ALEGRIA | SÃO PAULO | Brasil | 3547908 | 35 | 33 | nan | nan | nan | Cerrado | 5.0 |
| cd6d3d7d-3c69-345b-99cc-456f2e9d49bf | -21.08135 | -47.22966 | 2024-10-07 04:04:00 | NOAA-20 | SANTO ANTÔNIO DA ALEGRIA | SÃO PAULO | Brasil | 3547908 | 35 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 80c9b7ba-07a4-32d7-86e0-1c9e9c1ebf6b | -21.08045 | -47.23473 | 2024-10-07 04:04:00 | NOAA-20 | ALTINÓPOLIS | SÃO PAULO | Brasil | 3501004 | 35 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 777752ac-3f9f-3f17-ad4c-a4080bf85ed3 | -21.07957 | -47.23972 | 2024-10-07 04:04:00 | NOAA-20 | ALTINÓPOLIS | SÃO PAULO | Brasil | 3501004 | 35 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 57162099-17a0-3411-8cea-2e73e7d64939 | -21.07766 | -47.22887 | 2024-10-07 04:04:00 | NOAA-20 | SANTO ANTÔNIO DA ALEGRIA | SÃO PAULO | Brasil | 3547908 | 35 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 62f26888-6df0-3720-9d5b-6171112aa72c | -21.07679 | -47.23379 | 2024-10-07 04:04:00 | NOAA-20 | ALTINÓPOLIS | SÃO PAULO | Brasil | 3501004 | 35 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 5e468a04-aeb8-39f4-999a-662d6de2bdf1 | -21.07591 | -47.2387 | 2024-10-07 04:04:00 | NOAA-20 | ALTINÓPOLIS | SÃO PAULO | Brasil | 3501004 | 35 | 33 | nan | nan | nan | Cerrado | 3.6 |
| de1d0594-4c05-3286-bd0a-0bfbd3594fd8 | -21.07503 | -47.24367 | 2024-10-07 04:04:00 | NOAA-20 | ALTINÓPOLIS | SÃO PAULO | Brasil | 3501004 | 35 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 96b621bb-55be-3c6b-9872-b6b15fc98192 | -21.07396 | -47.22816 | 2024-10-07 04:04:00 | NOAA-20 | SANTO ANTÔNIO DA ALEGRIA | SÃO PAULO | Brasil | 3547908 | 35 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 030160f1-5cd2-3531-bd52-40902bfb36cf | -21.07312 | -47.23286 | 2024-10-07 04:04:00 | NOAA-20 | SANTO ANTÔNIO DA ALEGRIA | SÃO PAULO | Brasil | 3547908 | 35 | 33 | nan | nan | nan | Cerrado | 3.4 |
| b5eac7eb-fc47-3682-af05-28df7120de46 | -21.07227 | -47.23763 | 2024-10-07 04:04:00 | NOAA-20 | ALTINÓPOLIS | SÃO PAULO | Brasil | 3501004 | 35 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 599bb666-4f75-3be9-9267-ce4c4d488230 | -21.07137 | -47.24268 | 2024-10-07 04:04:00 | NOAA-20 | ALTINÓPOLIS | SÃO PAULO | Brasil | 3501004 | 35 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 41ca2744-d58e-38a1-93cd-68381d230997 | -21.06943 | -47.23206 | 2024-10-07 04:04:00 | NOAA-20 | SANTO ANTÔNIO DA ALEGRIA | SÃO PAULO | Brasil | 3547908 | 35 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 41f9de42-0a2c-3958-b4c8-cffdbb9a4c18 | -21.0686 | -47.2367 | 2024-10-07 04:04:00 | NOAA-20 | ALTINÓPOLIS | SÃO PAULO | Brasil | 3501004 | 35 | 33 | nan | nan | nan | Cerrado | 4.3 |
| cf19e978-15dd-36cb-8570-c67dcdae6e0e | -21.06771 | -47.24169 | 2024-10-07 04:04:00 | NOAA-20 | ALTINÓPOLIS | SÃO PAULO | Brasil | 3501004 | 35 | 33 | nan | nan | nan | Cerrado | 4.3 |
| a113f582-6e08-33d0-ae27-a7bdc32fee95 | -21.06404 | -47.24072 | 2024-10-07 04:04:00 | NOAA-20 | ALTINÓPOLIS | SÃO PAULO | Brasil | 3501004 | 35 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 64c94ab4-8038-3585-83c0-7252a6a3d02e | -21.58554 | -47.73932 | 2024-10-07 04:04:00 | NOAA-20 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 34662bd6-dc90-305b-819e-5445e247e198 | -21.58462 | -47.74434 | 2024-10-07 04:04:00 | NOAA-20 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 5cdd6958-8418-351b-95d9-5fab5477a962 | -21.57712 | -47.72136 | 2024-10-07 04:04:00 | NOAA-20 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 72a5cf5a-4c78-385b-88d5-7e7b2ec5390e | -21.57616 | -47.74776 | 2024-10-07 04:04:00 | NOAA-20 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 8.1 |
| e400be82-96c2-3c1f-936c-0a8b4a5f0c01 | -21.57425 | -47.7369 | 2024-10-07 04:04:00 | NOAA-20 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 3.1 |
| da10089a-3e85-342e-a965-a122c44aef6b | -21.57238 | -47.74699 | 2024-10-07 04:04:00 | NOAA-20 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 8.1 |
| 98e0831e-26aa-3ef0-9fc9-828dcac8f846 | -21.56961 | -47.76197 | 2024-10-07 04:04:00 | NOAA-20 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 8.0 |
| 4cea5f43-a2ff-3ca5-92c8-41ed5625221a | -21.56959 | -47.71983 | 2024-10-07 04:04:00 | NOAA-20 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 1.3 |
| be0f4654-687e-3039-9de6-d1de70ebf065 | -21.56861 | -47.74622 | 2024-10-07 04:04:00 | NOAA-20 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 31e2dc23-eeb0-358e-9c90-c0972d1a7d2d | -21.56769 | -47.73006 | 2024-10-07 04:04:00 | NOAA-20 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 20de019e-afc3-3908-a48d-638c47834a74 | -21.56485 | -47.72429 | 2024-10-07 04:04:00 | NOAA-20 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 58be8468-5468-3753-a406-772462111f75 | -21.56202 | -47.73954 | 2024-10-07 04:04:00 | NOAA-20 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 2d722e97-e623-3685-9166-f68668ca6f48 | -21.56015 | -47.74957 | 2024-10-07 04:04:00 | NOAA-20 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 1.9 |
| a16f4909-59e2-3253-9145-ff74c2e4e9dc | -21.55826 | -47.7387 | 2024-10-07 04:04:00 | NOAA-20 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 525d99c6-3e4f-3334-8059-55ede63631a4 | -21.55636 | -47.72787 | 2024-10-07 04:04:00 | NOAA-20 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 4.7 |
| a748e34a-b13c-38b6-be3c-884137d66432 | -21.55439 | -47.74044 | 2024-10-07 04:04:00 | NOAA-20 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 3.4 |
| bf5dbe8c-e9cc-32a3-852c-106d1f60d0b2 | -21.53554 | -48.05222 | 2024-10-07 04:04:00 | NOAA-20 | RINCÃO | SÃO PAULO | Brasil | 3543709 | 35 | 33 | nan | nan | nan | Cerrado | 1.0 |
| e9789cf7-3850-3cf6-805f-20d1b454a2d2 | -21.58647 | -47.7343 | 2024-10-07 04:04:00 | NOAA-20 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 22.4 |
| 7f6437c4-14ea-3569-8b2c-02e3ba5a8a64 | -21.58271 | -47.73344 | 2024-10-07 04:04:00 | NOAA-20 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 22.4 |
| dca78a7b-65c5-3283-b7ac-73a0177452ef | -21.58179 | -47.71725 | 2024-10-07 04:04:00 | NOAA-20 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 47621530-c69d-3a47-a032-1045cf800d41 | -21.58178 | -47.73849 | 2024-10-07 04:04:00 | NOAA-20 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 6.8 |
| be5cf578-e9ac-363f-8cc4-317717c3fd17 | -21.58085 | -47.74352 | 2024-10-07 04:04:00 | NOAA-20 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 6.8 |
| c4f70fe1-3e05-3c0e-9734-528c386dbefe | -21.57896 | -47.73257 | 2024-10-07 04:04:00 | NOAA-20 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 78811773-f3dc-38f8-a468-5d47e852d7c4 | -21.57331 | -47.74196 | 2024-10-07 04:04:00 | NOAA-20 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 3c5ee1e5-895a-354c-88ca-97661a6210ca | -21.57145 | -47.75202 | 2024-10-07 04:04:00 | NOAA-20 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 8.1 |
| 99918dab-91da-3c6b-b1f3-ba18b8c34994 | -21.57053 | -47.75702 | 2024-10-07 04:04:00 | NOAA-20 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 8.0 |
| bac8ca2d-86fc-33fe-b4d7-b0fb6a44a3a7 | -21.56954 | -47.74119 | 2024-10-07 04:04:00 | NOAA-20 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 8f221670-a9fe-3eea-bbbf-17a0698417da | -21.56676 | -47.75618 | 2024-10-07 04:04:00 | NOAA-20 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 7a0eae32-9003-3635-b2c0-13c6fa630d1b | -21.56578 | -47.74038 | 2024-10-07 04:04:00 | NOAA-20 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 5.0 |
| f4593585-c5e7-3e7c-86b6-fda1bc8acc51 | -21.56494 | -47.76603 | 2024-10-07 04:04:00 | NOAA-20 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 7.6 |
| 3809a8aa-7156-3559-ad12-64f53b8cffeb | -21.56296 | -47.73447 | 2024-10-07 04:04:00 | NOAA-20 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 36975f00-ad87-35f6-9536-8e35075e8fd3 | -21.56209 | -47.76024 | 2024-10-07 04:04:00 | NOAA-20 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 5.4 |
| c6e6485c-febd-36c8-95cf-67e3142feb41 | -21.56107 | -47.74463 | 2024-10-07 04:04:00 | NOAA-20 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 7d440dca-5fc8-30f8-bab4-637018b926d2 | -21.56106 | -47.72364 | 2024-10-07 04:04:00 | NOAA-20 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 5.1 |
| afb4736f-af23-3c43-8e66-d0b52b02740e | -21.55919 | -47.73367 | 2024-10-07 04:04:00 | NOAA-20 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 3fd6cdb4-fbbc-3e55-aded-ce5d97c1677f | -21.55732 | -47.74374 | 2024-10-07 04:04:00 | NOAA-20 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 61d447ea-553e-35a9-b09a-463e67e31829 | -21.55543 | -47.73286 | 2024-10-07 04:04:00 | NOAA-20 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 5.0 |
| ec027d39-91cd-3963-b6c1-dbbd1c7e3156 | -21.55529 | -47.73543 | 2024-10-07 04:04:00 | NOAA-20 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 7ed70f91-9151-3822-83bd-2cf25637f608 | -21.40533 | -47.81026 | 2024-10-07 04:04:00 | NOAA-20 | CRAVINHOS | SÃO PAULO | Brasil | 3513108 | 35 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 890ea289-459d-3d32-ac2e-10d1008fee7b | -22.20851 | -48.16982 | 2024-10-07 04:04:00 | NOAA-20 | BROTAS | SÃO PAULO | Brasil | 3507902 | 35 | 33 | nan | nan | nan | Cerrado | 0.9 |
| c06bf522-0e2f-3bce-97bc-dfe3b1e0cdd6 | -22.20756 | -48.175 | 2024-10-07 04:04:00 | NOAA-20 | BROTAS | SÃO PAULO | Brasil | 3507902 | 35 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 24ede03d-45f6-3a72-b0f6-da0a023d2680 | -22.2047 | -48.16895 | 2024-10-07 04:04:00 | NOAA-20 | BROTAS | SÃO PAULO | Brasil | 3507902 | 35 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 971a2923-956c-379a-b34a-9b9469a09a1e | -22.19995 | -48.17319 | 2024-10-07 04:04:00 | NOAA-20 | BROTAS | SÃO PAULO | Brasil | 3507902 | 35 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 4e0c18f5-0af1-3f60-ba6e-86e82b8dd8be | -22.19899 | -48.17839 | 2024-10-07 04:04:00 | NOAA-20 | BROTAS | SÃO PAULO | Brasil | 3507902 | 35 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 42c8d886-8f93-3353-929a-86db06ad6e61 | -22.19614 | -48.17229 | 2024-10-07 04:04:00 | NOAA-20 | BROTAS | SÃO PAULO | Brasil | 3507902 | 35 | 33 | nan | nan | nan | Cerrado | 1.5 |
| e4eb306c-5dc8-3267-8ce5-aae7a5958449 | -22.19518 | -48.17753 | 2024-10-07 04:04:00 | NOAA-20 | BROTAS | SÃO PAULO | Brasil | 3507902 | 35 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 438ade82-259d-3af1-9383-19e3c28b6e03 | -21.66095 | -47.73122 | 2024-10-07 04:04:00 | NOAA-20 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 18b648f8-d280-34f0-a9e9-2e40aac495ad | -21.66059 | -47.7351 | 2024-10-07 04:04:00 | NOAA-20 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 7e8dee6c-f4ee-3c61-bec8-8935fa57b0f2 | -21.65813 | -47.7254 | 2024-10-07 04:04:00 | NOAA-20 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 5.1 |
| eb7f5a26-c5ca-3021-8c0a-8b0b05b47846 | -21.65163 | -47.73932 | 2024-10-07 04:04:00 | NOAA-20 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 0.6 |
| cf454736-947f-3bfd-8e0b-85aba3d60074 | -21.65112 | -47.72259 | 2024-10-07 04:04:00 | NOAA-20 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 4412417d-c9cc-39c0-ba49-360e9d4b54c4 | -21.65023 | -47.72753 | 2024-10-07 04:04:00 | NOAA-20 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 1f928cf2-4da9-39f3-8a78-3658124664da | -21.64934 | -47.73248 | 2024-10-07 04:04:00 | NOAA-20 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 0245371c-53ba-3a36-ad6b-5a14b9f68dc7 | -21.62584 | -47.73284 | 2024-10-07 04:04:00 | NOAA-20 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 5c22732e-7290-38de-a756-18cfab5fcf5a | -21.62206 | -47.73212 | 2024-10-07 04:04:00 | NOAA-20 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 0.8 |
| e5ae527a-4370-3fc3-9375-43a0cd0017a2 | -21.59956 | -47.72691 | 2024-10-07 04:04:00 | NOAA-20 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 7f57dd58-fe44-3b71-9674-cc678e4663f3 | -21.59674 | -47.72095 | 2024-10-07 04:04:00 | NOAA-20 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 1177da82-e501-3476-8af7-941e0991071f | -21.59583 | -47.72594 | 2024-10-07 04:04:00 | NOAA-20 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 6.5 |
| dd8c32b8-cce3-3a15-89f8-7e045feddcf2 | -21.5939 | -47.71516 | 2024-10-07 04:04:00 | NOAA-20 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 1a951734-4b4f-32d8-ae5d-5965b7e1e4e5 | -21.59209 | -47.72501 | 2024-10-07 04:04:00 | NOAA-20 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 4b725ec1-8ff2-3a20-965a-d6b7bd2c6677 | -21.59022 | -47.73516 | 2024-10-07 04:04:00 | NOAA-20 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 20.3 |
| 58cf10b0-6687-3c7c-8631-fb71277c21b0 | -21.58928 | -47.71901 | 2024-10-07 04:04:00 | NOAA-20 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 4.1 |
| df79c935-6239-39ff-9d1a-bf438c120153 | -21.66434 | -47.73594 | 2024-10-07 04:04:00 | NOAA-20 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 1.2 |
| b9d0b977-aa3a-36b3-98da-d7d4535dc500 | -21.66147 | -47.7302 | 2024-10-07 04:04:00 | NOAA-20 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 79041714-1a30-35ec-a6fe-fae2963f80ad | -21.65721 | -47.73035 | 2024-10-07 04:04:00 | NOAA-20 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 47a27f87-948f-3635-b672-5e3b4a887b51 | -21.65538 | -47.74014 | 2024-10-07 04:04:00 | NOAA-20 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 1e679650-7fca-3a4f-b17b-517835cd8301 | -21.65439 | -47.72452 | 2024-10-07 04:04:00 | NOAA-20 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 2068afa8-1b58-3e98-9ea1-8d7f6ee96fa9 | -21.65254 | -47.73441 | 2024-10-07 04:04:00 | NOAA-20 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 18b32cf6-a919-370b-a3a7-66c724241035 | -21.64559 | -47.7316 | 2024-10-07 04:04:00 | NOAA-20 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 0.9 |
| e287464c-5b72-3cc2-a9b4-b7753f5910aa | -21.63985 | -47.72018 | 2024-10-07 04:04:00 | NOAA-20 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 3.1 |


[Clique aqui para ver as próximas entradas](README70.md)
