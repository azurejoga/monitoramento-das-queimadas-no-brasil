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

## Dados Diários - Página 71

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 3ea8c1ee-9ab5-3b93-a60b-4e0cbd238f5b | -3.2017 | -51.75386 | 2024-10-12 04:57:00 | NOAA-21 | VITÓRIA DO XINGU | PARÁ | Brasil | 1508357 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 9acde650-c008-383a-a17d-519a8f535eb1 | -3.18624 | -51.24296 | 2024-10-12 04:57:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| d1c32890-09da-3851-ae95-af278de0fcd0 | -3.18279 | -51.24242 | 2024-10-12 04:57:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| e56cc04f-1c74-3a4a-9a02-357149090ba6 | -3.18261 | -51.60856 | 2024-10-12 04:57:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 572befeb-d2ac-3ecd-b53c-129d0a683889 | -3.18115 | -51.2346 | 2024-10-12 04:57:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 619d2ba9-d249-39bd-9123-8205f678ff67 | -3.18049 | -51.23428 | 2024-10-12 04:57:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 838ea6e7-9067-3184-8562-0d7f98c501b6 | -3.17996 | -51.24221 | 2024-10-12 04:57:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 2ee6b047-73f3-38df-b779-69337799b8d8 | -3.1771 | -51.23788 | 2024-10-12 04:57:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 697d0ddd-f713-3b70-8c73-bbb0aa102ca2 | -3.16991 | -51.30627 | 2024-10-12 04:57:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 5ba91279-a3fc-3604-8992-346468380e71 | -3.16956 | -51.30605 | 2024-10-12 04:57:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 5e313891-f305-3e2d-91c8-790aa7ba4e34 | -3.04626 | -50.99203 | 2024-10-12 04:57:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| ae4ae61e-59a4-351f-8d55-ac48a9ba7d4c | -3.04578 | -51.13312 | 2024-10-12 04:57:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 7.8 |
| 1a4d8729-b03e-31c0-81fc-54c6c77a4cc9 | -3.04291 | -51.12878 | 2024-10-12 04:57:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 2cefc461-aec6-35d2-ad91-4c5288351034 | -3.04232 | -51.13259 | 2024-10-12 04:57:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 7.8 |
| 570840d9-f4ea-3ad7-a9ca-e236d4de60f4 | -3.03974 | -51.03437 | 2024-10-12 04:57:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 1a54e192-4483-3fdb-8310-3fdd09135f1c | -3.03944 | -51.12825 | 2024-10-12 04:57:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| a4676570-4912-300c-940c-f84a9d3ea3bd | -3.03885 | -51.13206 | 2024-10-12 04:57:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| ef54205c-5a73-35fb-a564-41886eb3e8bd | -3.03598 | -51.1277 | 2024-10-12 04:57:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| bf79c2cc-2d61-335a-bbc4-86fcf06fe64b | -3.03539 | -51.13152 | 2024-10-12 04:57:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 05e81783-5ea1-3928-bf8b-b16f4f067b62 | -3.03252 | -51.12716 | 2024-10-12 04:57:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| d3e01a5c-5373-3a16-9512-f932558129a0 | -3.02617 | -51.35003 | 2024-10-12 04:57:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| daf7b403-2d16-3969-b23e-438202469a74 | -3.01281 | -51.43574 | 2024-10-12 04:57:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ecc1d7c2-7e0a-3464-9299-d1c59bad71a4 | -2.97582 | -51.35759 | 2024-10-12 04:57:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| c0c9f340-5db6-32d2-9a71-afddae0f0b83 | -2.97467 | -51.36506 | 2024-10-12 04:57:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 61c506e1-3829-36c2-bd39-af25f79273fe | -2.97239 | -51.35706 | 2024-10-12 04:57:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 4e5beff0-f71d-3738-8d50-3dbb273d4bc8 | -2.97223 | -51.11094 | 2024-10-12 04:57:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 879ae70e-0c31-3fe1-abc6-c8cabd01246f | -2.97182 | -51.36079 | 2024-10-12 04:57:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 0aaf29b4-a409-3f9e-89a5-9eca04f3e9b4 | -2.97125 | -51.36453 | 2024-10-12 04:57:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| dad8d8bb-3117-3e8c-b301-a452baa44306 | -2.97067 | -51.36827 | 2024-10-12 04:57:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 1c8b1bf8-d904-3274-af93-f5e92a6ca6ed | -2.9668 | -51.03195 | 2024-10-12 04:57:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 58c8c82e-e42c-3602-94f4-6236b00cd235 | -2.96621 | -51.03579 | 2024-10-12 04:57:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 3ddb5b59-9870-3053-a6f6-10fb60a2c54f | -2.96333 | -51.03142 | 2024-10-12 04:57:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 8f574634-fcef-3687-95a5-692b439bac12 | -2.96273 | -51.03526 | 2024-10-12 04:57:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e405e692-9cd3-3daf-ace3-d0c32d281911 | -2.95192 | -51.28569 | 2024-10-12 04:57:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| bd70c1c5-4405-375b-abc6-a333e961c6de | -2.95133 | -51.28946 | 2024-10-12 04:57:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 3d0434a2-cd3f-301e-a739-be5d221c2aa0 | -2.94848 | -51.28516 | 2024-10-12 04:57:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 697a7115-2f1f-3992-99e8-85f290d9350b | -2.94789 | -51.28891 | 2024-10-12 04:57:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| c1facd6e-2c24-3b34-80b4-915dccb5e39a | -2.92905 | -51.45686 | 2024-10-12 04:57:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 3f7b99a0-d726-3cff-8773-04bdf30a0ea5 | -2.92847 | -51.45746 | 2024-10-12 04:57:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 6692da9a-7d37-3b28-b359-4ff37b5a9553 | -2.91996 | -51.44479 | 2024-10-12 04:57:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 16043d22-c879-3505-a946-85c2f3b17141 | -2.91655 | -51.44427 | 2024-10-12 04:57:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| b2cdb164-0c0b-3378-9576-4fa424c04203 | -2.86639 | -51.02437 | 2024-10-12 04:57:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| d07111e2-45ed-3a22-b940-da30f54ba6e5 | -2.86579 | -51.02823 | 2024-10-12 04:57:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 5bf04cf5-3a66-3c8f-8ca5-6fc636b4620f | -2.82432 | -51.33868 | 2024-10-12 04:57:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 64.1 |
| a6251250-20ba-35c9-a3d7-9b04e23e0641 | -2.82374 | -51.34241 | 2024-10-12 04:57:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 64.1 |
| de868884-0618-3d3f-a957-ed29701d124e | -2.82031 | -51.34188 | 2024-10-12 04:57:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 64.1 |
| 3d023fe6-9dad-37de-b076-740620c2a6db | -2.81747 | -51.33762 | 2024-10-12 04:57:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 2e4f94ba-8866-3ef4-9623-f75e8f5e4753 | -2.81689 | -51.34135 | 2024-10-12 04:57:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 266652ee-76c2-36f9-8951-b1b1240565e7 | -2.81404 | -51.33709 | 2024-10-12 04:57:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| a138d792-842d-31e3-9c81-864fe28620f8 | -2.81346 | -51.34082 | 2024-10-12 04:57:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| debe5502-7a57-3b3b-97a0-c42129e564b6 | -2.80798 | -51.01139 | 2024-10-12 04:57:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| fadd06df-e40e-39a5-8d92-318f4cfd1f3f | -2.80739 | -51.01521 | 2024-10-12 04:57:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 917e5828-d29d-38e3-865e-bd58b4fe1ebc | -2.80681 | -51.01902 | 2024-10-12 04:57:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 0d6bbc91-e9fa-30ba-932b-6f4c41280155 | -2.80451 | -51.01085 | 2024-10-12 04:57:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 11e77cc5-7855-35f8-b5c9-653cf388d4e2 | -2.80392 | -51.01467 | 2024-10-12 04:57:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 2d74445a-31d2-3f71-a043-30be00b5397d | -2.80334 | -51.01847 | 2024-10-12 04:57:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 92131768-b891-314c-bc87-8b422eebe7db | -2.80045 | -51.01411 | 2024-10-12 04:57:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 7401a0eb-eedd-3ec6-b761-889b5b892a8f | -2.79987 | -51.01793 | 2024-10-12 04:57:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 7a2d929b-8844-3074-ac46-8b5a2d4e377d | -2.78828 | -51.36737 | 2024-10-12 04:57:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 3a139f1c-e4fd-32c2-9ddc-a4077ec0508b | -2.78771 | -51.37107 | 2024-10-12 04:57:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 4d8562cb-48e3-33c0-bfa6-899ad70be8d2 | -2.78544 | -51.36314 | 2024-10-12 04:57:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 24.6 |
| d9dc9184-0b72-3e51-a191-15ebd0756d08 | -2.78486 | -51.36684 | 2024-10-12 04:57:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 24.6 |
| d29c0178-c512-3150-8fa4-cd76362bbd39 | -2.78428 | -51.37055 | 2024-10-12 04:57:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 8.1 |
| b62d651a-e465-3a15-971a-09074e0ef987 | -2.78201 | -51.36261 | 2024-10-12 04:57:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 24.6 |
| 91e0bccc-440c-3bbd-af86-55efe641106f | -2.78144 | -51.36632 | 2024-10-12 04:57:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 24.6 |
| d0c3579e-dd6b-3234-96a5-cfb220759410 | -2.78086 | -51.37003 | 2024-10-12 04:57:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 8.1 |
| a91c072a-4576-3939-b77b-82fbf84b521e | -2.77801 | -51.3658 | 2024-10-12 04:57:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 10.6 |
| 0095b170-5387-30ac-94ca-ac4654f88bb4 | -2.77744 | -51.36951 | 2024-10-12 04:57:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 7.0 |
| d68f9eb0-3b6a-319f-898d-bc4f793ce859 | -2.77686 | -51.37321 | 2024-10-12 04:57:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 7.0 |
| 3a46bf80-0fa0-36fd-a593-cbb0b294f20d | -2.77402 | -51.36898 | 2024-10-12 04:57:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 7.0 |
| 815b76da-cfb4-3c6e-a2e2-b6ea0587792f | -2.77344 | -51.37268 | 2024-10-12 04:57:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 7.0 |
| 00822b6a-a38b-3c47-831c-75c92238aebe | -2.77059 | -51.36845 | 2024-10-12 04:57:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| f18caa49-40eb-34f1-99b6-2aa9089d184a | -2.77002 | -51.37216 | 2024-10-12 04:57:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 05bf1dff-19b7-3ccb-b449-c465e6e64e1e | -4.1455 | -51.10169 | 2024-10-12 04:57:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 4ce3e17a-4a10-39c9-a8f8-78c7af1c3576 | -4.14489 | -51.10565 | 2024-10-12 04:57:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| dcddd05c-7fe6-334a-9524-f1ffd01c6744 | -4.107 | -51.0956 | 2024-10-12 04:57:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 5027540c-52c8-3624-a645-a06549322ef9 | -4.10344 | -51.11889 | 2024-10-12 04:57:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 43bdd409-d351-38f4-a4e3-865845cf0d05 | -4.09254 | -51.02532 | 2024-10-12 04:57:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 9be47610-3c59-3e1d-8e67-87209196713d | -4.08552 | -51.02426 | 2024-10-12 04:57:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 2d7d982d-3d75-3e2a-b3cd-9cd9920708e7 | -4.08501 | -51.02146 | 2024-10-12 04:57:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| faab85c3-054d-3deb-8e45-8baddbfd3397 | -4.08493 | -51.02814 | 2024-10-12 04:57:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ece014e9-4012-30f8-a53f-302ead1d4d1b | -4.0844 | -51.02534 | 2024-10-12 04:57:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| c89cd0ce-7cb3-34ca-ba50-bddbab163600 | -4.0838 | -51.02921 | 2024-10-12 04:57:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| e89abdf7-86f6-31db-8ab9-58e972cdca64 | -4.0669 | -51.1146 | 2024-10-12 04:57:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 609d6f30-d37d-3c31-adb0-43f3f1b60d9d | -4.0634 | -51.11408 | 2024-10-12 04:57:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 7a856aec-3b9c-32ab-8316-53bdcfda7446 | -4.04834 | -51.0957 | 2024-10-12 04:57:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 874bd188-9df9-3885-8aed-ecb8b2db4151 | -4.04467 | -51.11943 | 2024-10-12 04:57:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| b37cec14-fa4d-34a8-96f5-1de7d9ff02e0 | -4.02866 | -51.19976 | 2024-10-12 04:57:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 51608f0f-e330-39ca-b747-347eb7b9368a | -4.02711 | -51.00048 | 2024-10-12 04:57:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 871d1d76-6bdf-3322-8489-2e0776573efd | -4.02651 | -51.0044 | 2024-10-12 04:57:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 62ee3297-f5ec-3d4c-a8d6-21ab5e75744e | -4.02517 | -51.19923 | 2024-10-12 04:57:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| efb2bbe2-58a8-3a9f-97c1-8cad322e0589 | -4.0236 | -50.99991 | 2024-10-12 04:57:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 6.9 |
| 08405146-23cc-33d4-b464-c0ae5945783d | -4.02301 | -51.00375 | 2024-10-12 04:57:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 6.9 |
| 0d33f661-d2cd-33c5-a460-050bda6d664f | -4.0195 | -51.00315 | 2024-10-12 04:57:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 6.9 |
| 6f087d04-2de4-36b7-92aa-e8276fcdb366 | -3.93619 | -52.25267 | 2024-10-12 04:57:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 06d0f327-e330-3859-ac2b-423c5960e03e | -3.93564 | -52.25622 | 2024-10-12 04:57:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 44805f78-9d8b-3ba3-bc23-c8538ad2951b | -3.92333 | -51.22387 | 2024-10-12 04:57:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 238e3c27-88dd-302e-b712-36a400502dea | -3.92273 | -51.22773 | 2024-10-12 04:57:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 2d39b405-4b0d-314d-8aca-26d8ae9d616f | -3.92213 | -51.23157 | 2024-10-12 04:57:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 38dac1ad-c478-3bbb-9250-e316fbda62b1 | -3.91926 | -51.22719 | 2024-10-12 04:57:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |


[Clique aqui para ver as próximas entradas](README72.md)
