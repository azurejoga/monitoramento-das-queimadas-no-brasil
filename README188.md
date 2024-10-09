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

## Dados Diários - Página 188

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 72d849d7-a681-3761-b415-4f4fef4029d0 | -18.62317 | -57.22959 | 2024-10-09 05:06:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.3 |
| e0270765-a626-3fc0-b58d-e864654bf49c | -18.59793 | -57.26 | 2024-10-09 05:06:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 5.6 |
| 9e42bf19-a446-38e6-a0b5-cbed72f79237 | -19.11122 | -57.52269 | 2024-10-09 05:06:00 | NOAA-20 | LADÁRIO | MATO GROSSO DO SUL | Brasil | 5005202 | 50 | 33 | nan | nan | nan | Pantanal | 3.6 |
| 8948caa2-c727-3132-949b-75a649b323cf | -19.10787 | -57.52213 | 2024-10-09 05:06:00 | NOAA-20 | LADÁRIO | MATO GROSSO DO SUL | Brasil | 5005202 | 50 | 33 | nan | nan | nan | Pantanal | 1.7 |
| f0b8f862-99f3-3c16-8f2e-bca484bac863 | -19.10452 | -57.52156 | 2024-10-09 05:06:00 | NOAA-20 | LADÁRIO | MATO GROSSO DO SUL | Brasil | 5005202 | 50 | 33 | nan | nan | nan | Pantanal | 1.7 |
| 93674101-9c2d-3f8b-9eed-06b1fe0db51a | -18.72174 | -57.36453 | 2024-10-09 05:06:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.0 |
| 086e5e05-9f60-30ed-9483-ddf4f6890fd1 | -18.72117 | -57.36827 | 2024-10-09 05:06:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.0 |
| 31fdd6eb-acf3-3180-830f-cf1ac3e33943 | -18.71062 | -57.27836 | 2024-10-09 05:06:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 0.7 |
| 8c3a58e1-26aa-3a9d-b7b9-7e1076586a56 | -18.68317 | -57.23156 | 2024-10-09 05:06:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 0.5 |
| 8d92c9d6-c8ec-3df6-87ec-f50909885216 | -18.68205 | -57.30818 | 2024-10-09 05:06:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.3 |
| 7c2926cb-d706-3b21-9901-e2cd0573eb9b | -18.67867 | -57.21542 | 2024-10-09 05:06:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 0.8 |
| e6a75bd3-c27b-38a2-ba73-afbdac4ee91f | -18.65511 | -57.21154 | 2024-10-09 05:06:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.0 |
| 32cf486f-de17-3dc3-ba4a-2d7712584f60 | -18.65348 | -57.21151 | 2024-10-09 05:06:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.2 |
| 585948c5-07d1-3ecb-ad60-8ce2dbdb878b | -18.65291 | -57.21526 | 2024-10-09 05:06:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.1 |
| 5a217965-bbfe-3f84-8398-78d19def3577 | -18.65011 | -57.21095 | 2024-10-09 05:06:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.2 |
| 8add9868-8aea-39f2-b414-605ffa2d87da | -18.64955 | -57.21471 | 2024-10-09 05:06:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.1 |
| 0152fac6-d272-3dc4-ad58-d8499a8a1041 | -18.64675 | -57.2104 | 2024-10-09 05:06:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.9 |
| 0dbb2f9f-e1c9-3c57-a52e-aa1cc8c92ef2 | -18.64002 | -57.20929 | 2024-10-09 05:06:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 0.7 |
| 0cc39f83-a1d2-3a68-aad6-95532628892a | -18.60859 | -57.23488 | 2024-10-09 05:06:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.2 |
| 228f9207-8809-301d-b020-54618b196d06 | -18.60803 | -57.23862 | 2024-10-09 05:06:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.1 |
| 076a1d3f-472c-32f7-9539-724d41264696 | -18.60072 | -57.2643 | 2024-10-09 05:06:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.2 |
| aa30a415-9ed5-3c91-8567-38f905acca32 | -18.60016 | -57.26804 | 2024-10-09 05:06:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.4 |
| 8b9b3ffd-b67b-32f6-be58-9c5b34c5e0d9 | -18.59625 | -57.24821 | 2024-10-09 05:06:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.3 |
| ff82f01f-defa-338f-ab45-3c44a02a1609 | -18.73254 | -57.22428 | 2024-10-09 05:06:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.3 |
| 09ea35f9-9432-316a-8e2f-1e58e3571d1b | -18.70783 | -57.27406 | 2024-10-09 05:06:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 0.8 |
| 99d9f16b-f063-3202-9c0a-ecbd947d4e91 | -18.70168 | -57.22306 | 2024-10-09 05:06:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.3 |
| 1dc56821-227a-301d-b541-e4c2f82d6232 | -18.68092 | -57.22349 | 2024-10-09 05:06:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.0 |
| f1a8035b-8019-3dd8-a249-0a84245c326e | -18.65848 | -57.2121 | 2024-10-09 05:06:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.0 |
| 90d522fc-0c05-3459-89f7-20013bb7c0f5 | -18.64338 | -57.20984 | 2024-10-09 05:06:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.9 |
| ffeb9123-bacc-354c-a166-75740f2db9dc | -18.63932 | -57.30516 | 2024-10-09 05:06:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.0 |
| 77a91576-191c-3985-ac6c-23378661ff8f | -18.62373 | -57.22584 | 2024-10-09 05:06:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.3 |
| 33356d12-fc4e-3ee7-b93c-3c23d45dff8e | -18.59736 | -57.26374 | 2024-10-09 05:06:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 5.6 |
| 4d06c779-a50e-3f21-8862-6650c4f1d1e1 | -18.5968 | -57.26749 | 2024-10-09 05:06:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.7 |
| 66f9a024-be76-3e9c-80de-8794d2e76a53 | -18.59569 | -57.25196 | 2024-10-09 05:06:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.2 |
| b91dd618-1e1a-3f70-8ff9-88523c452333 | -18.59513 | -57.2557 | 2024-10-09 05:06:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.2 |
| 6d84c9d8-5df6-3e5e-90e6-8690d1449e65 | -18.59456 | -57.25945 | 2024-10-09 05:06:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 5.6 |
| b02d053e-f27c-3583-aab8-95640a5a3e68 | -18.59401 | -57.24017 | 2024-10-09 05:06:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.0 |
| ea4c77d3-6e80-362f-8e79-c4fcbf92ebec | -18.594 | -57.26319 | 2024-10-09 05:06:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 5.6 |
| 8e38aae4-4be2-3d2f-828d-682be8c6a5bd | -18.59345 | -57.24391 | 2024-10-09 05:06:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.4 |
| a4b308a4-78b0-316c-9d73-0e6b9475f5f5 | -18.59344 | -57.26693 | 2024-10-09 05:06:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.7 |
| 25e86ee0-d70d-3f29-b340-550f26077f2e | -18.59289 | -57.24766 | 2024-10-09 05:06:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.4 |
| 644f3635-0571-33d5-841d-6b76dcdcf00a | -18.59233 | -57.2514 | 2024-10-09 05:06:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.1 |
| 0165be5b-7b67-37da-bc67-af7731411f55 | -18.59176 | -57.25514 | 2024-10-09 05:06:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.1 |
| 22ba1238-16e8-3c36-8ebc-fb4084cbdbfc | -18.5912 | -57.25889 | 2024-10-09 05:06:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.0 |
| bb3db9bd-9466-3b5c-86e0-3add9c4959b3 | -18.59064 | -57.26263 | 2024-10-09 05:06:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.0 |
| 148de012-69c1-3c1e-8d9a-fa048888d0ac | -18.59008 | -57.26638 | 2024-10-09 05:06:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 0.5 |
| 76ad3b5f-6ef2-3bcb-8265-87090fdfc42e | -18.58896 | -57.25085 | 2024-10-09 05:06:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.1 |
| 3294c52c-e9f1-3801-9235-4f09f60bf737 | -18.5884 | -57.25459 | 2024-10-09 05:06:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.1 |
| e9ac07cb-b81c-3aa6-bd82-2757780f731f | -18.58784 | -57.25834 | 2024-10-09 05:06:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.0 |
| 4f2d422b-f12e-359a-878f-cde33553cbd5 | -18.7056 | -57.21986 | 2024-10-09 05:06:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 0.7 |
| 9dc8bf6f-ace0-313a-a59d-ea2ef178fb8a | -18.66521 | -57.21321 | 2024-10-09 05:06:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 0.6 |
| c208b3b4-fa60-3999-a83d-9877fd3ef712 | -18.6624 | -57.2089 | 2024-10-09 05:06:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 0.6 |
| c295195c-69f2-3b32-873b-0f6ac93d5448 | -18.66184 | -57.21265 | 2024-10-09 05:06:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 0.6 |
| 9bae4e08-ef7c-38fa-8cb3-c05e0a1ba81b | -18.63709 | -57.29713 | 2024-10-09 05:06:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 0.5 |
| 960b5ebf-b80f-3221-ba25-65d209657370 | -18.63597 | -57.3046 | 2024-10-09 05:06:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.0 |
| 4972de07-ac1b-3eab-800a-986e8ac8b563 | -18.63094 | -57.29228 | 2024-10-09 05:06:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 0.7 |
| c487088e-adbb-38dc-975c-86eaf5148ee0 | -18.62261 | -57.23334 | 2024-10-09 05:06:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.4 |
| 21b4ebe6-c63f-369e-9a55-817cfb9e44fe | -18.60466 | -57.23808 | 2024-10-09 05:06:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.1 |
| 2da3113b-a014-3f8d-b199-58e2ff149ddc | -18.60129 | -57.26056 | 2024-10-09 05:06:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.2 |
| cbaedec7-c97b-306d-9284-62cb4ce8ebbb | -18.59849 | -57.25626 | 2024-10-09 05:06:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.2 |
| 25b6f67f-9385-3706-b183-9641cde3079c | -18.59737 | -57.24072 | 2024-10-09 05:06:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 4.5 |
| 98b21844-c999-37e7-a3b6-ae4fbfc29fb3 | -18.59681 | -57.24446 | 2024-10-09 05:06:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.3 |
| f04a6915-f127-3100-8b02-9cf00ae55ed2 | -21.62606 | -44.64574 | 2024-10-09 05:06:00 | NOAA-20 | CARRANCAS | MINAS GERAIS | Brasil | 3114600 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.8 |
| 89aeb280-321f-322f-a192-2e77ccef507c | -20.66753 | -45.8992 | 2024-10-09 05:06:00 | NOAA-20 | GUAPÉ | MINAS GERAIS | Brasil | 3128105 | 31 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 9be74570-3813-3d46-ada2-6433aa34ac12 | -20.66706 | -45.90492 | 2024-10-09 05:06:00 | NOAA-20 | GUAPÉ | MINAS GERAIS | Brasil | 3128105 | 31 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 9b15c412-f543-3283-9261-a114817feda3 | -20.66658 | -45.91074 | 2024-10-09 05:06:00 | NOAA-20 | GUAPÉ | MINAS GERAIS | Brasil | 3128105 | 31 | 33 | nan | nan | nan | Cerrado | 2.2 |
| b40d43a2-3f55-3e78-8e3b-6f5e4b72e84f | -20.65979 | -45.91209 | 2024-10-09 05:06:00 | NOAA-20 | GUAPÉ | MINAS GERAIS | Brasil | 3128105 | 31 | 33 | nan | nan | nan | Cerrado | 2.2 |
| e216a677-c394-3bfd-b0da-df2c5cbc8433 | -20.65938 | -45.91717 | 2024-10-09 05:06:00 | NOAA-20 | GUAPÉ | MINAS GERAIS | Brasil | 3128105 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| f4980077-5185-38d5-910c-867ff72b386a | -20.65396 | -45.9016 | 2024-10-09 05:06:00 | NOAA-20 | GUAPÉ | MINAS GERAIS | Brasil | 3128105 | 31 | 33 | nan | nan | nan | Cerrado | 2.2 |
| dc7bb1ec-e27d-3db3-9da5-494ead535f9d | -20.64782 | -45.89474 | 2024-10-09 05:06:00 | NOAA-20 | GUAPÉ | MINAS GERAIS | Brasil | 3128105 | 31 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 7ad4b4da-b674-373e-ad50-17ae38445787 | -20.63857 | -45.92669 | 2024-10-09 05:06:00 | NOAA-20 | GUAPÉ | MINAS GERAIS | Brasil | 3128105 | 31 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 1207c546-90e9-3e7f-9bff-c708f4935568 | -20.63811 | -45.9324 | 2024-10-09 05:06:00 | NOAA-20 | GUAPÉ | MINAS GERAIS | Brasil | 3128105 | 31 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 864d38ea-2988-3576-b22a-cd05913866a9 | -20.63279 | -45.91544 | 2024-10-09 05:06:00 | NOAA-20 | GUAPÉ | MINAS GERAIS | Brasil | 3128105 | 31 | 33 | nan | nan | nan | Cerrado | 8.1 |
| 8159f840-5422-3ce9-933b-231944d8aaa8 | -20.6324 | -45.92039 | 2024-10-09 05:06:00 | NOAA-20 | GUAPÉ | MINAS GERAIS | Brasil | 3128105 | 31 | 33 | nan | nan | nan | Cerrado | 8.1 |
| ebde9cf6-f4a5-331d-9ffb-c3d3a576ff61 | -20.62838 | -45.9126 | 2024-10-09 05:06:00 | NOAA-20 | GUAPÉ | MINAS GERAIS | Brasil | 3128105 | 31 | 33 | nan | nan | nan | Cerrado | 3.9 |
| b74db78f-e73c-3918-bc66-a9e3910735a3 | -20.62791 | -45.91802 | 2024-10-09 05:06:00 | NOAA-20 | GUAPÉ | MINAS GERAIS | Brasil | 3128105 | 31 | 33 | nan | nan | nan | Cerrado | 6.8 |
| bb75fd01-da3d-3d09-ba7a-bdccd64f40c9 | -22.06009 | -46.89184 | 2024-10-09 05:06:00 | NOAA-20 | AGUAÍ | SÃO PAULO | Brasil | 3500303 | 35 | 33 | nan | nan | nan | Cerrado | 0.9 |
| b56a7720-8d30-3507-ba9c-499621895dd9 | -22.05372 | -46.89144 | 2024-10-09 05:06:00 | NOAA-20 | AGUAÍ | SÃO PAULO | Brasil | 3500303 | 35 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 901efd4b-5d68-32f8-acd5-fe0fa2c2a20a | -21.00491 | -46.09865 | 2024-10-09 05:06:00 | NOAA-20 | CARMO DO RIO CLARO | MINAS GERAIS | Brasil | 3114402 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| 136523b9-601c-3361-baa4-b1c6e7e68d0b | -21.00347 | -46.10074 | 2024-10-09 05:06:00 | NOAA-20 | CARMO DO RIO CLARO | MINAS GERAIS | Brasil | 3114402 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 4ebfcf68-9129-3fd3-97c1-133118051060 | -20.92196 | -46.46405 | 2024-10-09 05:06:00 | NOAA-20 | ALPINÓPOLIS | MINAS GERAIS | Brasil | 3101904 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.6 |
| 0e131947-f7fd-3d36-8a04-ead848619121 | -20.92153 | -46.46932 | 2024-10-09 05:06:00 | NOAA-20 | ALPINÓPOLIS | MINAS GERAIS | Brasil | 3101904 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.6 |
| 6edab0e0-4650-33ae-8546-02847b9d7565 | -21.30364 | -46.1267 | 2024-10-09 05:06:00 | NOAA-20 | ALTEROSA | MINAS GERAIS | Brasil | 3102001 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| e1eae501-f618-36f2-b7be-b085c39668a0 | -21.29712 | -46.12526 | 2024-10-09 05:06:00 | NOAA-20 | ALTEROSA | MINAS GERAIS | Brasil | 3102001 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| ad33f98b-7064-3bcb-a4a4-7f9f90d71a19 | -22.74983 | -47.12745 | 2024-10-09 05:06:00 | NOAA-20 | PAULÍNIA | SÃO PAULO | Brasil | 3536505 | 35 | 33 | nan | nan | nan | Cerrado | 2.1 |
| bffd2098-6202-3b3c-a825-40e25af409d3 | -22.7494 | -47.13284 | 2024-10-09 05:06:00 | NOAA-20 | PAULÍNIA | SÃO PAULO | Brasil | 3536505 | 35 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 2e43532c-a31b-35bc-b69e-8c92a6e8b04c | -22.75276 | -47.00795 | 2024-10-09 05:06:00 | NOAA-20 | CAMPINAS | SÃO PAULO | Brasil | 3509502 | 35 | 33 | nan | nan | nan | Mata Atlântica | 4.1 |
| 8909b4da-474a-3a2d-a227-f6aaa4006379 | -22.57574 | -46.66919 | 2024-10-09 05:06:00 | NOAA-20 | SERRA NEGRA | SÃO PAULO | Brasil | 3551603 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| d9360a1b-f83a-30f2-874f-ca6a49518578 | -19.86087 | -47.87689 | 2024-10-09 05:06:00 | NOAA-20 | UBERABA | MINAS GERAIS | Brasil | 3170107 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| dec5991e-1849-3d02-97ad-4a0eb23846d8 | -19.86047 | -47.88113 | 2024-10-09 05:06:00 | NOAA-20 | UBERABA | MINAS GERAIS | Brasil | 3170107 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 5eef21ee-c302-3e54-8a90-3f24b900733c | -22.19225 | -48.15936 | 2024-10-09 05:06:00 | NOAA-20 | BROTAS | SÃO PAULO | Brasil | 3507902 | 35 | 33 | nan | nan | nan | Cerrado | 2.1 |
| b13ab381-f2a6-3c9c-9553-7f819d91aea7 | -22.19184 | -48.16383 | 2024-10-09 05:06:00 | NOAA-20 | BROTAS | SÃO PAULO | Brasil | 3507902 | 35 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 95028a7e-454e-3d5d-bc1e-bc140d115e0b | -22.19061 | -48.15666 | 2024-10-09 05:06:00 | NOAA-20 | BROTAS | SÃO PAULO | Brasil | 3507902 | 35 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 4920e707-699e-3995-95d9-42922ccf13b5 | -22.19025 | -48.16105 | 2024-10-09 05:06:00 | NOAA-20 | BROTAS | SÃO PAULO | Brasil | 3507902 | 35 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 42d6f2d2-9646-32e4-8691-2d37004adce1 | -22.18987 | -48.16552 | 2024-10-09 05:06:00 | NOAA-20 | BROTAS | SÃO PAULO | Brasil | 3507902 | 35 | 33 | nan | nan | nan | Cerrado | 1.8 |
| acd2b381-d00a-3e06-9477-4d3813d0c3bc | -22.18634 | -48.15886 | 2024-10-09 05:06:00 | NOAA-20 | BROTAS | SÃO PAULO | Brasil | 3507902 | 35 | 33 | nan | nan | nan | Cerrado | 2.1 |
| a8595443-4562-3409-9354-675e0d5d7c73 | -22.18595 | -48.16323 | 2024-10-09 05:06:00 | NOAA-20 | BROTAS | SÃO PAULO | Brasil | 3507902 | 35 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 283d04fd-5023-3309-b807-4d5ba312682d | -22.18397 | -48.16498 | 2024-10-09 05:06:00 | NOAA-20 | BROTAS | SÃO PAULO | Brasil | 3507902 | 35 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 36727e52-0b24-3bae-b15f-21c5792d6732 | -22.17925 | -48.1716 | 2024-10-09 05:06:00 | NOAA-20 | BROTAS | SÃO PAULO | Brasil | 3507902 | 35 | 33 | nan | nan | nan | Cerrado | 2.8 |
| c253f0db-9256-32b8-a8e8-5215de5ae845 | -22.15691 | -48.08752 | 2024-10-09 05:06:00 | NOAA-20 | RIBEIRÃO BONITO | SÃO PAULO | Brasil | 3542909 | 35 | 33 | nan | nan | nan | Cerrado | 1.6 |


[Clique aqui para ver as próximas entradas](README189.md)
