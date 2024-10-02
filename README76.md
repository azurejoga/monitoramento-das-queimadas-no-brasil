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

## Dados Diários - Página 76

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| a55ede96-6bbd-388e-8300-5f89dea31efe | -21.3441 | -55.69167 | 2024-10-02 03:57:00 | NOAA-20 | MARACAJU | MATO GROSSO DO SUL | Brasil | 5005400 | 50 | 33 | nan | nan | nan | Cerrado | 10.5 |
| f7a419ab-0d9b-3ed0-bb9e-cd84bfb3d159 | -21.34383 | -55.70263 | 2024-10-02 03:57:00 | NOAA-20 | NIOAQUE | MATO GROSSO DO SUL | Brasil | 5005806 | 50 | 33 | nan | nan | nan | Cerrado | 21.2 |
| b5b0f4ee-8972-39f5-a722-f439fc435a3c | -21.34239 | -55.69878 | 2024-10-02 03:57:00 | NOAA-20 | NIOAQUE | MATO GROSSO DO SUL | Brasil | 5005806 | 50 | 33 | nan | nan | nan | Cerrado | 10.5 |
| dc8757e7-0dd5-35ee-aee2-8d06afa66124 | -21.33706 | -55.70134 | 2024-10-02 03:57:00 | NOAA-20 | NIOAQUE | MATO GROSSO DO SUL | Brasil | 5005806 | 50 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 1ad3fff1-2230-33aa-8704-d13f0a23d94f | -20.04716 | -55.96957 | 2024-10-02 03:57:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 3.0 |
| f91e2d12-ceda-3cd8-b51e-21a355177e0f | -20.04546 | -55.97659 | 2024-10-02 03:57:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 3.0 |
| 23490f6d-5fbb-3cfb-8011-7a7670d5f248 | -20.04515 | -55.9707 | 2024-10-02 03:57:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 4.3 |
| 29fcac06-ce5b-3c56-914d-3584ca255247 | -20.0434 | -55.97769 | 2024-10-02 03:57:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 3.1 |
| bce9ce17-67bc-3b6e-9443-3bce91ad1fe4 | -20.04029 | -55.96762 | 2024-10-02 03:57:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 2.9 |
| 6eb4220a-9047-31cb-b0be-0fa62c88cb19 | -20.03858 | -55.97462 | 2024-10-02 03:57:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 2.9 |
| 53bf4f24-e654-3249-80b6-d4d02050d3cf | -20.03826 | -55.96878 | 2024-10-02 03:57:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 4.3 |
| ada56a3e-2dc5-38ed-8cbc-68c9fb926654 | -20.03652 | -55.97575 | 2024-10-02 03:57:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 3.1 |
| ff4c6261-e14d-3b3f-98ca-e536147290c9 | -20.03518 | -55.98863 | 2024-10-02 03:57:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 3.9 |
| cac61344-dec5-301a-92af-06e1f987c8b8 | -20.03478 | -55.98272 | 2024-10-02 03:57:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 3.1 |
| eb3cf98c-5b6c-3bcf-b530-be687e8772bc | -20.03303 | -55.98972 | 2024-10-02 03:57:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 2.5 |
| 44b59164-09f0-3311-8626-a7e87f15ea38 | -20.0317 | -55.97267 | 2024-10-02 03:57:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 2.9 |
| 75550ab8-be9b-3cd2-aedb-3c1cf9e9f816 | -20.03 | -55.97966 | 2024-10-02 03:57:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 3.9 |
| db877ee9-e6fa-3232-bd5e-9920389c65f7 | -20.02964 | -55.97383 | 2024-10-02 03:57:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 2.8 |
| 25a54ea1-af89-3978-a81c-054bd19c3b43 | -20.02789 | -55.9808 | 2024-10-02 03:57:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 2.8 |
| 8c6e97c5-0361-36f0-b3ef-14b1d825d5d1 | -22.304 | -41.87927 | 2024-10-02 03:57:00 | NOAA-20 | MACAÉ | RIO DE JANEIRO | Brasil | 3302403 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| b5e03bdb-ad3d-34a9-93cd-ab11c3a3f17e | -22.30342 | -41.88299 | 2024-10-02 03:57:00 | NOAA-20 | MACAÉ | RIO DE JANEIRO | Brasil | 3302403 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 071d32d6-300e-3b04-9541-8b2bc7102646 | -22.34743 | -43.35834 | 2024-10-02 03:57:00 | NOAA-20 | PATY DO ALFERES | RIO DE JANEIRO | Brasil | 3303856 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 179d3488-2c1f-35a3-8ddc-1a86474c7fe8 | -22.34471 | -43.35385 | 2024-10-02 03:57:00 | NOAA-20 | PATY DO ALFERES | RIO DE JANEIRO | Brasil | 3303856 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| e7db64ad-44d5-3017-bf31-07a22ad2c329 | -22.34407 | -43.35772 | 2024-10-02 03:57:00 | NOAA-20 | PATY DO ALFERES | RIO DE JANEIRO | Brasil | 3303856 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 3465a356-9d5a-3c5a-b3e8-cf48a9a964b8 | -22.21801 | -43.15832 | 2024-10-02 03:57:00 | NOAA-20 | AREAL | RIO DE JANEIRO | Brasil | 3300225 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 0c019847-aead-3212-9658-f697f940078b | -22.21466 | -43.15769 | 2024-10-02 03:57:00 | NOAA-20 | AREAL | RIO DE JANEIRO | Brasil | 3300225 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| f2d43c1f-4cd6-36da-8fec-99a996107ca5 | -22.21402 | -43.16158 | 2024-10-02 03:57:00 | NOAA-20 | AREAL | RIO DE JANEIRO | Brasil | 3300225 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 481cc58d-46d9-38ff-a51c-c4c3c4d442dc | -22.07643 | -42.62696 | 2024-10-02 03:57:00 | NOAA-20 | SUMIDOURO | RIO DE JANEIRO | Brasil | 3305703 | 33 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| e47e7dc6-e5ff-37cd-a96f-6421ad41b0da | -22.07582 | -42.6307 | 2024-10-02 03:57:00 | NOAA-20 | SUMIDOURO | RIO DE JANEIRO | Brasil | 3305703 | 33 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| f740fd87-d67f-3251-bf1c-603a49c0a818 | -22.03169 | -42.48033 | 2024-10-02 03:57:00 | NOAA-20 | DUAS BARRAS | RIO DE JANEIRO | Brasil | 3301603 | 33 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| dbaf6572-48ad-3878-978e-1857c110d209 | -22.02897 | -42.47599 | 2024-10-02 03:57:00 | NOAA-20 | DUAS BARRAS | RIO DE JANEIRO | Brasil | 3301603 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| fe24741c-8020-32c6-b912-83828dfaf59a | -22.93955 | -43.23639 | 2024-10-02 03:57:00 | NOAA-20 | RIO DE JANEIRO | RIO DE JANEIRO | Brasil | 3304557 | 33 | 33 | nan | nan | nan | Mata Atlântica | 2.7 |
| 95a9e7cf-c498-396c-aeb2-5084511f5ec8 | -22.93491 | -43.73213 | 2024-10-02 03:57:00 | NOAA-20 | RIO DE JANEIRO | RIO DE JANEIRO | Brasil | 3304557 | 33 | 33 | nan | nan | nan | Mata Atlântica | 6.6 |
| 0c0aec40-7497-3eb4-bdcf-f844533d77cd | -22.93218 | -43.72758 | 2024-10-02 03:57:00 | NOAA-20 | RIO DE JANEIRO | RIO DE JANEIRO | Brasil | 3304557 | 33 | 33 | nan | nan | nan | Mata Atlântica | 6.6 |
| 3ffafa96-cbb9-31ba-85e5-be40833fa263 | -22.93153 | -43.73148 | 2024-10-02 03:57:00 | NOAA-20 | RIO DE JANEIRO | RIO DE JANEIRO | Brasil | 3304557 | 33 | 33 | nan | nan | nan | Mata Atlântica | 6.6 |
| 7efc9986-7c78-3fc1-a1b8-73c046e390e0 | -22.93087 | -43.73537 | 2024-10-02 03:57:00 | NOAA-20 | RIO DE JANEIRO | RIO DE JANEIRO | Brasil | 3304557 | 33 | 33 | nan | nan | nan | Mata Atlântica | 13.0 |
| f8e44372-97e8-3f14-8732-6d895262fbf4 | -22.92881 | -43.72692 | 2024-10-02 03:57:00 | NOAA-20 | RIO DE JANEIRO | RIO DE JANEIRO | Brasil | 3304557 | 33 | 33 | nan | nan | nan | Mata Atlântica | 10.2 |
| bbff595b-6cdf-3705-a004-d37c20db3571 | -22.92815 | -43.73082 | 2024-10-02 03:57:00 | NOAA-20 | RIO DE JANEIRO | RIO DE JANEIRO | Brasil | 3304557 | 33 | 33 | nan | nan | nan | Mata Atlântica | 10.2 |
| 38508795-d44d-321e-a093-0c299d204189 | -22.9275 | -43.73471 | 2024-10-02 03:57:00 | NOAA-20 | RIO DE JANEIRO | RIO DE JANEIRO | Brasil | 3304557 | 33 | 33 | nan | nan | nan | Mata Atlântica | 10.5 |
| 76fbda62-e5ed-31ad-90ba-91b72e0f3436 | -22.92609 | -43.72236 | 2024-10-02 03:57:00 | NOAA-20 | RIO DE JANEIRO | RIO DE JANEIRO | Brasil | 3304557 | 33 | 33 | nan | nan | nan | Mata Atlântica | 6.2 |
| b0e691e9-5ed3-3510-82ec-5422cd40beba | -22.92543 | -43.72626 | 2024-10-02 03:57:00 | NOAA-20 | RIO DE JANEIRO | RIO DE JANEIRO | Brasil | 3304557 | 33 | 33 | nan | nan | nan | Mata Atlântica | 10.2 |
| 398ac530-13d2-370f-8f3f-79710af83612 | -22.91487 | -43.3026 | 2024-10-02 03:57:00 | NOAA-20 | RIO DE JANEIRO | RIO DE JANEIRO | Brasil | 3304557 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| ebbaa654-1f67-3572-8544-2f118c2f895c | -22.85502 | -42.98199 | 2024-10-02 03:57:00 | NOAA-20 | SÃO GONÇALO | RIO DE JANEIRO | Brasil | 3304904 | 33 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| aa5f5256-5916-3d5e-bdb4-806f32667a3d | -22.82915 | -42.70271 | 2024-10-02 03:57:00 | NOAA-20 | TANGUÁ | RIO DE JANEIRO | Brasil | 3305752 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| 0fbd0d2d-b75f-324f-81b1-8449eae3f9d5 | -22.82854 | -42.70648 | 2024-10-02 03:57:00 | NOAA-20 | TANGUÁ | RIO DE JANEIRO | Brasil | 3305752 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| e21607a1-44a9-3b66-94f1-ec537c93b1d1 | -22.78621 | -43.75696 | 2024-10-02 03:57:00 | NOAA-20 | SEROPÉDICA | RIO DE JANEIRO | Brasil | 3305554 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| 47830673-ffda-3165-af81-bf6796e0e16c | -22.77234 | -43.79825 | 2024-10-02 03:57:00 | NOAA-20 | ITAGUAÍ | RIO DE JANEIRO | Brasil | 3302007 | 33 | 33 | nan | nan | nan | Mata Atlântica | 3.8 |
| 8482051f-4216-32e0-8ab5-f8b569f7ab2f | -22.7717 | -43.80204 | 2024-10-02 03:57:00 | NOAA-20 | ITAGUAÍ | RIO DE JANEIRO | Brasil | 3302007 | 33 | 33 | nan | nan | nan | Mata Atlântica | 3.6 |
| ff0b86e7-3bb2-3654-aee2-f1dc0e43917d | -22.77107 | -43.80581 | 2024-10-02 03:57:00 | NOAA-20 | ITAGUAÍ | RIO DE JANEIRO | Brasil | 3302007 | 33 | 33 | nan | nan | nan | Mata Atlântica | 3.6 |
| f4d9c408-120e-3741-be29-cfe779388e38 | -22.77015 | -43.76947 | 2024-10-02 03:57:00 | NOAA-20 | SEROPÉDICA | RIO DE JANEIRO | Brasil | 3305554 | 33 | 33 | nan | nan | nan | Mata Atlântica | 2.5 |
| bd7fc156-da7e-3126-a99b-dedbbdc9b35d | -22.76896 | -43.79753 | 2024-10-02 03:57:00 | NOAA-20 | ITAGUAÍ | RIO DE JANEIRO | Brasil | 3302007 | 33 | 33 | nan | nan | nan | Mata Atlântica | 13.6 |
| 0a6dab7e-04ce-37ea-bd4f-acd48a496174 | -22.76832 | -43.80134 | 2024-10-02 03:57:00 | NOAA-20 | ITAGUAÍ | RIO DE JANEIRO | Brasil | 3302007 | 33 | 33 | nan | nan | nan | Mata Atlântica | 5.0 |
| 475e4fbb-0692-3b34-8921-2573e8a15f10 | -22.76741 | -43.765 | 2024-10-02 03:57:00 | NOAA-20 | SEROPÉDICA | RIO DE JANEIRO | Brasil | 3305554 | 33 | 33 | nan | nan | nan | Mata Atlântica | 3.4 |
| dcfda14f-70a9-30ee-9c6e-207d3e08175c | -22.76402 | -43.76438 | 2024-10-02 03:57:00 | NOAA-20 | SEROPÉDICA | RIO DE JANEIRO | Brasil | 3305554 | 33 | 33 | nan | nan | nan | Mata Atlântica | 3.4 |
| 5b69f1ce-259f-3e06-baee-f8492e4ca896 | -22.76339 | -43.76816 | 2024-10-02 03:57:00 | NOAA-20 | SEROPÉDICA | RIO DE JANEIRO | Brasil | 3305554 | 33 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| a8a76b2b-079c-362e-9593-4e152990466e | -22.75128 | -43.77794 | 2024-10-02 03:57:00 | NOAA-20 | ITAGUAÍ | RIO DE JANEIRO | Brasil | 3302007 | 33 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| 856a5eb0-9b27-3cd3-a945-4c5c0e9db3b8 | -22.74048 | -43.77983 | 2024-10-02 03:57:00 | NOAA-20 | ITAGUAÍ | RIO DE JANEIRO | Brasil | 3302007 | 33 | 33 | nan | nan | nan | Mata Atlântica | 2.9 |
| ec182a2c-c80f-3074-9f54-5fec6b24387b | -22.73714 | -43.79974 | 2024-10-02 03:57:00 | NOAA-20 | ITAGUAÍ | RIO DE JANEIRO | Brasil | 3302007 | 33 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 107191c4-5223-3389-b8ea-aec0a4b28040 | -22.67498 | -42.85634 | 2024-10-02 03:57:00 | NOAA-20 | ITABORAÍ | RIO DE JANEIRO | Brasil | 3301900 | 33 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 82ba3c5d-f2e1-32cd-92dd-395195afdb46 | -22.67231 | -43.70373 | 2024-10-02 03:57:00 | NOAA-20 | SEROPÉDICA | RIO DE JANEIRO | Brasil | 3305554 | 33 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| 138876d7-e0ab-323f-b4cd-ff39fcab0455 | -22.67166 | -43.70769 | 2024-10-02 03:57:00 | NOAA-20 | SEROPÉDICA | RIO DE JANEIRO | Brasil | 3305554 | 33 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| 92cee2ae-ad4e-30a9-b5dd-95e5a5fc41e9 | -22.67098 | -43.71175 | 2024-10-02 03:57:00 | NOAA-20 | SEROPÉDICA | RIO DE JANEIRO | Brasil | 3305554 | 33 | 33 | nan | nan | nan | Mata Atlântica | 5.1 |
| aa11f5ed-aea8-357c-8a56-da991a282bc3 | -22.66893 | -43.70308 | 2024-10-02 03:57:00 | NOAA-20 | SEROPÉDICA | RIO DE JANEIRO | Brasil | 3305554 | 33 | 33 | nan | nan | nan | Mata Atlântica | 5.4 |
| 8a1da5b6-1b77-3e03-8622-b1aba3b3c599 | -22.66826 | -43.70713 | 2024-10-02 03:57:00 | NOAA-20 | SEROPÉDICA | RIO DE JANEIRO | Brasil | 3305554 | 33 | 33 | nan | nan | nan | Mata Atlântica | 5.4 |
| 50611bfc-9210-3dca-95b9-8ce3099a03a7 | -22.66554 | -43.70255 | 2024-10-02 03:57:00 | NOAA-20 | SEROPÉDICA | RIO DE JANEIRO | Brasil | 3305554 | 33 | 33 | nan | nan | nan | Mata Atlântica | 5.4 |
| 7875402b-ad65-3d66-b982-dde80e877836 | -22.66487 | -43.70655 | 2024-10-02 03:57:00 | NOAA-20 | SEROPÉDICA | RIO DE JANEIRO | Brasil | 3305554 | 33 | 33 | nan | nan | nan | Mata Atlântica | 5.4 |
| 60ba56fc-c73c-383b-90c4-a5c2f8e57f33 | -22.64916 | -43.57112 | 2024-10-02 03:57:00 | NOAA-20 | JAPERI | RIO DE JANEIRO | Brasil | 3302270 | 33 | 33 | nan | nan | nan | Mata Atlântica | 2.5 |
| 74d6945b-7b86-369f-bc15-5d9681b0a1cc | -22.55405 | -43.82221 | 2024-10-02 03:57:00 | NOAA-20 | PIRAÍ | RIO DE JANEIRO | Brasil | 3304003 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| e34b308c-f012-34ed-bbfe-d88fc5eb644b | -22.52671 | -43.5476 | 2024-10-02 03:57:00 | NOAA-20 | MIGUEL PEREIRA | RIO DE JANEIRO | Brasil | 3302908 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| 7e175f3a-29b8-3c0d-b005-3213901a7aba | -22.52334 | -43.54695 | 2024-10-02 03:57:00 | NOAA-20 | MIGUEL PEREIRA | RIO DE JANEIRO | Brasil | 3302908 | 33 | 33 | nan | nan | nan | Mata Atlântica | 3.2 |
| 66b0f687-19c7-3da8-b7e2-37ae4d6276ba | -22.51282 | -43.83834 | 2024-10-02 03:57:00 | NOAA-20 | PIRAÍ | RIO DE JANEIRO | Brasil | 3304003 | 33 | 33 | nan | nan | nan | Mata Atlântica | 14.0 |
| 17e8d1f6-eac0-3617-81d8-dc85fc07623a | -22.50943 | -43.83766 | 2024-10-02 03:57:00 | NOAA-20 | BARRA DO PIRAÍ | RIO DE JANEIRO | Brasil | 3300308 | 33 | 33 | nan | nan | nan | Mata Atlântica | 2.5 |
| bf096284-6ee8-3f44-bb8c-19b95a691bc7 | -22.49806 | -43.54649 | 2024-10-02 03:57:00 | NOAA-20 | MIGUEL PEREIRA | RIO DE JANEIRO | Brasil | 3302908 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 9a5ed681-4c2f-3b8b-90cf-af85a5d98865 | -22.49743 | -43.55028 | 2024-10-02 03:57:00 | NOAA-20 | VASSOURAS | RIO DE JANEIRO | Brasil | 3306206 | 33 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 3d38306c-5ef1-37e8-aa9d-60b5977195d3 | -22.4947 | -43.54581 | 2024-10-02 03:57:00 | NOAA-20 | MIGUEL PEREIRA | RIO DE JANEIRO | Brasil | 3302908 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 4ae68807-b321-3680-ad3d-7eeb3183eb6e | -22.49406 | -43.54963 | 2024-10-02 03:57:00 | NOAA-20 | VASSOURAS | RIO DE JANEIRO | Brasil | 3306206 | 33 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 5ece3e17-a6f5-375c-8a81-e464dbf0bfaf | -22.39793 | -43.53507 | 2024-10-02 03:57:00 | NOAA-20 | VASSOURAS | RIO DE JANEIRO | Brasil | 3306206 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 31e57da4-4e2b-339d-92bb-4af1561a4453 | -22.39456 | -43.53444 | 2024-10-02 03:57:00 | NOAA-20 | VASSOURAS | RIO DE JANEIRO | Brasil | 3306206 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 8cd63fc9-f5da-30c8-8c64-81ab6c76552d | -22.39119 | -43.53385 | 2024-10-02 03:57:00 | NOAA-20 | VASSOURAS | RIO DE JANEIRO | Brasil | 3306206 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 1c03bee7-6774-37c1-8c60-d8aa4246298e | -22.38638 | -43.52082 | 2024-10-02 03:57:00 | NOAA-20 | VASSOURAS | RIO DE JANEIRO | Brasil | 3306206 | 33 | 33 | nan | nan | nan | Mata Atlântica | 6.0 |
| fbbf8378-54a4-3025-977b-9a7d2c4666b3 | -22.38574 | -43.52476 | 2024-10-02 03:57:00 | NOAA-20 | VASSOURAS | RIO DE JANEIRO | Brasil | 3306206 | 33 | 33 | nan | nan | nan | Mata Atlântica | 6.0 |
| 903ad07d-bfef-35af-b47b-1ac80461f2e8 | -22.38301 | -43.52028 | 2024-10-02 03:57:00 | NOAA-20 | VASSOURAS | RIO DE JANEIRO | Brasil | 3306206 | 33 | 33 | nan | nan | nan | Mata Atlântica | 6.0 |
| ad2ad0ae-8359-3da9-913c-798542b26c3e | -22.38236 | -43.52422 | 2024-10-02 03:57:00 | NOAA-20 | VASSOURAS | RIO DE JANEIRO | Brasil | 3306206 | 33 | 33 | nan | nan | nan | Mata Atlântica | 6.0 |
| 6cf952ad-3cb2-374a-abee-1f54b87db58c | -22.61477 | -43.96357 | 2024-10-02 03:57:00 | NOAA-20 | PIRAÍ | RIO DE JANEIRO | Brasil | 3304003 | 33 | 33 | nan | nan | nan | Mata Atlântica | 4.9 |
| cfd1e819-2ae8-36a9-b86c-1d9b3dcce04e | -22.61137 | -43.96288 | 2024-10-02 03:57:00 | NOAA-20 | PIRAÍ | RIO DE JANEIRO | Brasil | 3304003 | 33 | 33 | nan | nan | nan | Mata Atlântica | 4.3 |
| 53489f7f-75aa-352b-87ae-34aef7ddd7ed | -22.60797 | -43.9622 | 2024-10-02 03:57:00 | NOAA-20 | PIRAÍ | RIO DE JANEIRO | Brasil | 3304003 | 33 | 33 | nan | nan | nan | Mata Atlântica | 4.3 |
| d55ea690-7669-37d7-b4a8-afa588f7a63f | -22.60457 | -43.96152 | 2024-10-02 03:57:00 | NOAA-20 | PIRAÍ | RIO DE JANEIRO | Brasil | 3304003 | 33 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 4c6c1f24-1ad4-32b2-824d-2cb1cea7409a | -22.35617 | -44.0169 | 2024-10-02 03:57:00 | NOAA-20 | BARRA DO PIRAÍ | RIO DE JANEIRO | Brasil | 3300308 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 5b64c589-2fdd-35bb-b4ae-7c7d346164f4 | -22.35549 | -44.02086 | 2024-10-02 03:57:00 | NOAA-20 | BARRA DO PIRAÍ | RIO DE JANEIRO | Brasil | 3300308 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| d3bc9a42-042a-3391-9320-c43c52264b0a | -21.68586 | -43.96817 | 2024-10-02 03:57:00 | NOAA-20 | LIMA DUARTE | MINAS GERAIS | Brasil | 3138609 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 2ea39e3e-2e05-3061-bca4-14b8470699c8 | -21.67469 | -43.95426 | 2024-10-02 03:57:00 | NOAA-20 | LIMA DUARTE | MINAS GERAIS | Brasil | 3138609 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.6 |
| e85f0817-1d37-3603-98a5-e4fc5d38e043 | -21.67424 | -43.95343 | 2024-10-02 03:57:00 | NOAA-20 | LIMA DUARTE | MINAS GERAIS | Brasil | 3138609 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.8 |
| 04f86b5c-9003-3d0b-bf0a-210004c5916b | -21.67127 | -43.95356 | 2024-10-02 03:57:00 | NOAA-20 | LIMA DUARTE | MINAS GERAIS | Brasil | 3138609 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.6 |
| 47077b31-0464-39b4-abcc-675e220774fc | -21.66856 | -43.96974 | 2024-10-02 03:57:00 | NOAA-20 | LIMA DUARTE | MINAS GERAIS | Brasil | 3138609 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.5 |
| 65d3b137-e309-397f-9afb-b350bef992e7 | -21.66785 | -43.95293 | 2024-10-02 03:57:00 | NOAA-20 | LIMA DUARTE | MINAS GERAIS | Brasil | 3138609 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| d5010a09-d645-38f6-bbb7-5799ba8d5fa6 | -21.66717 | -43.95698 | 2024-10-02 03:57:00 | NOAA-20 | LIMA DUARTE | MINAS GERAIS | Brasil | 3138609 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 5661b08a-3fc8-3049-893b-9b6404bc7d0d | -21.66513 | -43.96908 | 2024-10-02 03:57:00 | NOAA-20 | LIMA DUARTE | MINAS GERAIS | Brasil | 3138609 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 04c896a9-078e-3a50-9e23-bd40efcc8aea | -21.65699 | -43.99637 | 2024-10-02 03:57:00 | NOAA-20 | SANTANA DO GARAMBÉU | MINAS GERAIS | Brasil | 3158706 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 5da688bc-12ec-344d-a1b5-90de4f39f1f3 | -21.47714 | -44.5836 | 2024-10-02 03:57:00 | NOAA-20 | CARRANCAS | MINAS GERAIS | Brasil | 3114600 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.4 |
| bdf9cb9b-fcaf-38ff-9300-c933028b9a2e | -22.48022 | -44.13543 | 2024-10-02 03:57:00 | NOAA-20 | VOLTA REDONDA | RIO DE JANEIRO | Brasil | 3306305 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |


[Clique aqui para ver as próximas entradas](README77.md)
