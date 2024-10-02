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

## Dados Diários - Página 123

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| ea888066-ba67-3b77-8059-047230befc5f | -17.20495 | -56.1911 | 2024-10-02 04:51:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.9 |
| afe91858-c68b-3630-8539-208d898ec0f2 | -17.20425 | -56.19518 | 2024-10-02 04:51:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.9 |
| a2df5200-db02-3214-8dbb-6f7e0cdc6ed2 | -17.19234 | -56.18039 | 2024-10-02 04:51:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 11.0 |
| 70cf41aa-9d4d-36aa-9e26-742e4d75b4db | -17.19025 | -56.19262 | 2024-10-02 04:51:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.9 |
| d9e6cd72-f364-31c5-8b27-25c54796b227 | -17.18956 | -56.19669 | 2024-10-02 04:51:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 3.2 |
| 7d38409e-f573-3c97-bf1b-8c1ad31808d7 | -17.18954 | -56.17569 | 2024-10-02 04:51:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 4.1 |
| 11e563dd-98dd-39d7-8961-05275c2d15ed | -17.18884 | -56.17975 | 2024-10-02 04:51:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 11.0 |
| f95048ea-39f4-36ad-a834-562c3aa9c09d | -17.18814 | -56.18382 | 2024-10-02 04:51:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 11.0 |
| 68ae2ae5-6b63-3dca-bcc8-2a139bd8f418 | -17.18675 | -56.19197 | 2024-10-02 04:51:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.9 |
| 3a4aab5d-71fa-3850-93df-b900a2ef1a98 | -17.18534 | -56.17912 | 2024-10-02 04:51:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 3.5 |
| 1ddacb0f-6bad-3aad-b8e3-90669a2882bf | -17.18465 | -56.18319 | 2024-10-02 04:51:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 3.5 |
| f32c8212-df7b-3dc3-aed1-74dfd1250ab0 | -17.18115 | -56.18255 | 2024-10-02 04:51:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 3.5 |
| e4c4252b-6be3-369b-a447-7880badb0ed2 | -17.17693 | -56.14407 | 2024-10-02 04:51:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.1 |
| 684859d0-90a0-3efa-ad7a-10a0e457a00b | -17.28283 | -56.41631 | 2024-10-02 04:51:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.8 |
| d668bb05-8353-3c2a-b872-baa01f1ca039 | -17.20152 | -56.25366 | 2024-10-02 04:51:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.8 |
| 64b78fc4-fcf8-3bdd-b11b-3e563a3f188b | -17.19945 | -56.2871 | 2024-10-02 04:51:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.7 |
| 88feb799-789b-32c0-9e57-58ece63f23fd | -17.19732 | -56.25711 | 2024-10-02 04:51:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.4 |
| 85bb3c9a-70fa-3f30-b1b4-10314b2d2d47 | -17.19524 | -56.29055 | 2024-10-02 04:51:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.6 |
| 41bbd6dd-8901-3c65-8356-ea60b48de5e9 | -17.19453 | -56.27349 | 2024-10-02 04:51:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.3 |
| f14bff79-1ecc-3dea-8390-c8eba356f679 | -17.19173 | -56.28991 | 2024-10-02 04:51:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.6 |
| 3bc2bcb4-a617-3c60-b7b5-c978ef48aac3 | -17.19101 | -56.27285 | 2024-10-02 04:51:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.2 |
| e05dab80-0594-3dc8-8033-07e929347413 | -17.19032 | -56.27694 | 2024-10-02 04:51:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.2 |
| 5e909d26-0d33-3b30-9012-caaf0fa47b84 | -17.1889 | -56.264 | 2024-10-02 04:51:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.8 |
| 6974adea-6ed8-3e07-a4c0-aaddfb317f12 | -17.1875 | -56.2722 | 2024-10-02 04:51:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.2 |
| d810db59-7ce1-3e5c-9558-fd8c8f7d9f86 | -17.1868 | -56.27629 | 2024-10-02 04:51:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.2 |
| ece69349-6a77-36fd-b517-63846ee63a89 | -17.1861 | -56.2804 | 2024-10-02 04:51:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 3.5 |
| 8999525d-ba99-31a7-b925-02727aeb9434 | -17.18259 | -56.27976 | 2024-10-02 04:51:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.1 |
| 51864cd3-f6a9-394f-84dd-c816e0f6b5d2 | -17.17978 | -56.27501 | 2024-10-02 04:51:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.4 |
| eaad554f-3096-31f0-866d-6d415ebd5cbb | -17.11616 | -56.39107 | 2024-10-02 04:51:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.4 |
| f7bffb59-32c7-35c8-bc4e-2b99c5a5220c | -17.11399 | -56.40353 | 2024-10-02 04:51:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.5 |
| 1d89b55d-3224-39d8-9079-39146c00f838 | -17.11057 | -56.40342 | 2024-10-02 04:51:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.5 |
| 4622225c-8892-3866-a939-98bb2f097979 | -17.11046 | -56.40287 | 2024-10-02 04:51:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.4 |
| b8e7ba2a-e707-3701-b2cb-48b01696a015 | -17.10838 | -56.68959 | 2024-10-02 04:51:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.3 |
| 3905b79d-45d5-3a4a-bd8e-d510c7314d89 | -17.10764 | -56.69387 | 2024-10-02 04:51:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.3 |
| 5db7cb89-2152-3ee7-87ae-d078a2a63355 | -17.10406 | -56.69321 | 2024-10-02 04:51:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.9 |
| 8a221257-d70e-399f-b420-32499b638015 | -17.10034 | -56.7146 | 2024-10-02 04:51:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.3 |
| 269357f0-bc5a-3330-8344-b2ce99e915ac | -17.09676 | -56.71393 | 2024-10-02 04:51:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.3 |
| 115bcbea-fbeb-383c-8ad6-fed0d17afe06 | -17.09615 | -56.69616 | 2024-10-02 04:51:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.9 |
| 9c2d8f8c-7060-38ed-a16e-47f7fc71937b | -17.0954 | -56.70043 | 2024-10-02 04:51:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.9 |
| 630454b9-91c9-3892-bdd2-ac7437d400a4 | -17.09108 | -56.70404 | 2024-10-02 04:51:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.4 |
| 53317432-b44d-3555-86da-26cf7e44a0ca | -17.09033 | -56.70832 | 2024-10-02 04:51:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.4 |
| a8fefd86-5cc9-3ae0-815d-bb40f06889e8 | -17.08959 | -56.7126 | 2024-10-02 04:51:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.7 |
| 7a0d89ab-e51c-3063-86a2-a9292fb911c8 | -17.0875 | -56.70337 | 2024-10-02 04:51:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.4 |
| 262359a0-c984-3acb-8022-14bb323916a5 | -17.08675 | -56.70765 | 2024-10-02 04:51:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.4 |
| ae961140-42ef-3021-81df-14262f05ad1a | -17.086 | -56.71193 | 2024-10-02 04:51:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 4.0 |
| e33041a6-6701-3002-8902-95f9738044e1 | -17.08391 | -56.70271 | 2024-10-02 04:51:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.4 |
| 4f04711b-d676-3691-a98d-6a724d58eb16 | -17.08317 | -56.70698 | 2024-10-02 04:51:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.4 |
| a73bb47a-47d7-37c3-8031-b8eff2ad17c2 | -17.08033 | -56.70204 | 2024-10-02 04:51:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.5 |
| d1afd192-8f01-30df-b2b2-9c4ff775e92b | -17.07749 | -56.69711 | 2024-10-02 04:51:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.2 |
| 1239feb8-1681-361d-93f0-b22d49be2605 | -17.07674 | -56.70137 | 2024-10-02 04:51:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.5 |
| 7ce930e0-4f0b-31a1-929c-b4cb8f9af10a | -17.076 | -56.70565 | 2024-10-02 04:51:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.5 |
| 7ea2f22a-3c3e-355f-8c32-bf893981741f | -17.07525 | -56.70993 | 2024-10-02 04:51:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.9 |
| 84fe397a-aef9-386a-afb4-3a9ba0ef2769 | -17.07391 | -56.69644 | 2024-10-02 04:51:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 6.8 |
| 21b227d8-43fc-3cb8-8315-e365b65829d6 | -17.07316 | -56.70071 | 2024-10-02 04:51:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.6 |
| 3338a905-e6a3-36a9-ab1f-92581aa5b96f | -17.07241 | -56.70498 | 2024-10-02 04:51:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.6 |
| 42cc2823-5def-34a8-98d1-28563687c1e6 | -17.07166 | -56.70927 | 2024-10-02 04:51:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 4.0 |
| 47c9e3e2-b8ff-33ee-b653-ec537bb26b09 | -17.07032 | -56.69577 | 2024-10-02 04:51:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 6.8 |
| 9dfa29a9-e675-3cdd-8f0f-321e57218e48 | -17.06958 | -56.70005 | 2024-10-02 04:51:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.6 |
| 7feab717-4b3a-3bd3-b851-9b5544585bd4 | -17.06883 | -56.70432 | 2024-10-02 04:51:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.6 |
| 4424d85d-c3c1-32ef-8569-2dcae1f32754 | -17.06599 | -56.69938 | 2024-10-02 04:51:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 7.1 |
| ae49577e-dd04-3cf2-8ecd-a3b7e79cf816 | -17.06524 | -56.70366 | 2024-10-02 04:51:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 7.1 |
| 82840150-6e11-360c-a91d-5f6d8ccc199b | -17.06449 | -56.70794 | 2024-10-02 04:51:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.5 |
| ee9af472-958f-379e-8a61-3065fd539c24 | -17.06166 | -56.70299 | 2024-10-02 04:51:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 7.1 |
| 39522acd-125c-3e96-862e-e3fa1f5561c9 | -17.0597 | -56.70339 | 2024-10-02 04:51:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.3 |
| d3662467-f8ac-34d3-a55c-7828b6fb2450 | -17.05807 | -56.70233 | 2024-10-02 04:51:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.2 |
| 9178834f-ca9c-3d65-900e-5cd08712e723 | -17.05612 | -56.70273 | 2024-10-02 04:51:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.3 |
| 93567c79-f62f-3622-80b0-22f6e839eb54 | -17.05373 | -56.70595 | 2024-10-02 04:51:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.9 |
| fa4c0382-fdc0-3ee1-b36f-9b39724508f1 | -17.21202 | -56.23448 | 2024-10-02 04:51:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.9 |
| d2f241e6-cdcd-3fa2-848d-01ca047a83a8 | -17.20987 | -56.20461 | 2024-10-02 04:51:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.1 |
| 80f138c2-90b8-37d5-8b45-f6811bc12e07 | -17.20851 | -56.23384 | 2024-10-02 04:51:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.9 |
| 06b9b5ba-2967-3a89-83f1-6fdb46eceb2c | -17.20782 | -56.23793 | 2024-10-02 04:51:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.9 |
| 1329573e-3e05-3d2c-be5a-138924fb1dfb | -17.20712 | -56.24203 | 2024-10-02 04:51:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.5 |
| e08f9825-6218-3f44-b959-ac2cd55f7b90 | -17.20709 | -56.22093 | 2024-10-02 04:51:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 4.7 |
| df1130c4-4c96-3e1f-950a-d7e2e37cfe96 | -17.2064 | -56.22501 | 2024-10-02 04:51:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 3.7 |
| 97a93f8e-c5a7-3107-a642-ee803cc61619 | -17.2057 | -56.2291 | 2024-10-02 04:51:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 3.7 |
| 479f64d6-27ef-359b-b389-83d21ca60095 | -17.20501 | -56.23319 | 2024-10-02 04:51:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.2 |
| 479c3331-f8c6-31ba-859b-b97a60713f3d | -17.20431 | -56.23729 | 2024-10-02 04:51:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.2 |
| 22814671-5bb6-30c4-adc1-0ee4e2a20556 | -17.20364 | -56.26249 | 2024-10-02 04:51:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.9 |
| a6fbe872-e0de-3f90-8036-868a52d7a886 | -17.20361 | -56.24138 | 2024-10-02 04:51:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.0 |
| fc1082f2-12de-3bb5-8e04-3e4050f8c7e7 | -17.20359 | -56.22028 | 2024-10-02 04:51:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 4.7 |
| 9d26199b-9b5a-33be-b381-188de8b14705 | -17.20292 | -56.24548 | 2024-10-02 04:51:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.0 |
| 3d62bbe9-2a80-3420-9db7-1ea9c7a3a684 | -17.20289 | -56.22437 | 2024-10-02 04:51:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 3.7 |
| e4d43a85-5d74-3a52-bbe2-6301d58a1fc6 | -17.2022 | -56.22846 | 2024-10-02 04:51:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 3.7 |
| 1328e172-05f4-37a3-aa24-e92bc125c82e | -17.2015 | -56.23256 | 2024-10-02 04:51:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.2 |
| dab9ea04-29ef-367a-83b9-6c3ef3a1e060 | -17.20083 | -56.25776 | 2024-10-02 04:51:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.4 |
| f095bfc0-d4d1-35c2-9d84-e93eefb6fd40 | -17.2008 | -56.23664 | 2024-10-02 04:51:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.2 |
| 836b00f5-2da6-30e4-93c0-f32f1284bc69 | -17.20078 | -56.21556 | 2024-10-02 04:51:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.3 |
| 41f16cf8-b2b1-368b-94c4-8d49d24044b1 | -17.20013 | -56.26185 | 2024-10-02 04:51:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.4 |
| 32b43bf8-1915-31bc-a7ce-43d7465caab3 | -17.20011 | -56.24074 | 2024-10-02 04:51:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.0 |
| 7c3484be-2b72-39f1-b3d2-a2f651cf652d | -17.20009 | -56.21964 | 2024-10-02 04:51:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.3 |
| 3f239610-cfad-3f22-8b06-f88e4c8cbc6a | -17.19939 | -56.22373 | 2024-10-02 04:51:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.9 |
| b2b3e51c-bb66-3003-9191-78d5c1393f5c | -17.19867 | -56.20677 | 2024-10-02 04:51:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.6 |
| 35ed2856-1622-32f7-ba45-be760f61b6e6 | -17.19802 | -56.25302 | 2024-10-02 04:51:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.8 |
| f9a77210-a1d8-39ce-a266-519978a21e85 | -17.19799 | -56.23191 | 2024-10-02 04:51:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.9 |
| e93df7d3-1d6f-3efa-bb1a-218e23117721 | -17.19797 | -56.21085 | 2024-10-02 04:51:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.6 |
| e6ea1c62-d01a-3c78-b3ad-fbd07769099b | -17.1973 | -56.236 | 2024-10-02 04:51:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.9 |
| 82ffb4bc-39b9-37f4-acf4-7d68c305d413 | -17.19728 | -56.21492 | 2024-10-02 04:51:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.3 |
| bb27d918-97fb-31cc-b0c4-2c41b066059c | -17.19658 | -56.219 | 2024-10-02 04:51:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.3 |
| 95b220a0-5c2f-3599-a5ef-a0de37337065 | -17.19594 | -56.28645 | 2024-10-02 04:51:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.0 |
| f575e058-752f-3094-b1ab-cd5bb5e33681 | -17.19522 | -56.2694 | 2024-10-02 04:51:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.5 |


[Clique aqui para ver as próximas entradas](README124.md)
