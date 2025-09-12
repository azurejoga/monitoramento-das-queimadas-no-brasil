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

## Dados Diários - Página 54

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| da1c7138-4737-30a7-b9d6-289de656ec13 | -20.57247 | -43.78162 | 2025-09-12 04:08:00 | NPP-375D | CONSELHEIRO LAFAIETE | MINAS GERAIS | Brasil | 3118304 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| 014070dc-470f-3b0d-9d7e-ebffb08f7226 | -22.85087 | -47.34378 | 2025-09-12 04:08:00 | NPP-375D | SUMARÉ | SÃO PAULO | Brasil | 3552403 | 35 | 33 | nan | nan | nan | Mata Atlântica | 5.5 |
| a8bc58af-ffca-333e-89c1-9f69f79635da | -21.62761 | -46.79203 | 2025-09-12 04:08:00 | NPP-375D | SÃO JOSÉ DO RIO PARDO | SÃO PAULO | Brasil | 3549706 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| fe6fe6fe-8262-3eb2-8f06-70e9840a75b6 | -23.38952 | -47.01236 | 2025-09-12 04:08:00 | NPP-375D | PIRAPORA DO BOM JESUS | SÃO PAULO | Brasil | 3539103 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 307da490-419f-3ee3-8377-9fda2cf2181e | -23.10022 | -46.67959 | 2025-09-12 04:08:00 | NPP-375D | JARINU | SÃO PAULO | Brasil | 3525201 | 35 | 33 | nan | nan | nan | Mata Atlântica | 5.7 |
| fa9f76fa-5bc8-3771-834f-5b72b0f80236 | -23.10992 | -47.50171 | 2025-09-12 04:08:00 | NPP-375D | PORTO FELIZ | SÃO PAULO | Brasil | 3540606 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| d9b6e6cc-b8fb-3bd8-8619-7d3a83912aac | -19.7514 | -46.09308 | 2025-09-12 04:08:00 | NPP-375D | CÓRREGO DANTA | MINAS GERAIS | Brasil | 3119807 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 3788ad1c-2511-3d9b-99de-0f17d14a911c | -22.69582 | -48.694 | 2025-09-12 04:08:00 | NPP-375D | LENÇÓIS PAULISTA | SÃO PAULO | Brasil | 3526803 | 35 | 33 | nan | nan | nan | Cerrado | 1.7 |
| c6b13bb7-b889-380c-b43d-627093a3bba7 | -19.99494 | -46.91346 | 2025-09-12 04:08:00 | NPP-375D | TAPIRA | MINAS GERAIS | Brasil | 3168101 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 3001addd-29c3-3d29-87e0-8730718b42fb | -19.63758 | -41.58742 | 2025-09-12 04:08:00 | NPP-375D | POCRANE | MINAS GERAIS | Brasil | 3151909 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.5 |
| 8b878b84-a5b5-3169-80d3-67b1e0eb7768 | -21.57738 | -45.38086 | 2025-09-12 04:08:00 | NPP-375D | VARGINHA | MINAS GERAIS | Brasil | 3170701 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| e7666db3-9f87-34f2-aa9b-b1249f4f2fe2 | -20.39524 | -42.19537 | 2025-09-12 04:08:00 | NPP-375D | SANTA MARGARIDA | MINAS GERAIS | Brasil | 3157906 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| e2cd9562-252f-3da6-ac87-4bbe553bd262 | -23.11615 | -47.48853 | 2025-09-12 04:08:00 | NPP-375D | PORTO FELIZ | SÃO PAULO | Brasil | 3540606 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.4 |
| 7fd9421e-2d9d-3e7d-9f99-a7cb81814f24 | -19.66404 | -44.90221 | 2025-09-12 04:08:00 | NPP-375D | PITANGUI | MINAS GERAIS | Brasil | 3151404 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| a2477605-677e-3301-ab04-c567f365c4aa | -21.91604 | -47.91214 | 2025-09-12 04:08:00 | NPP-375D | SÃO CARLOS | SÃO PAULO | Brasil | 3548906 | 35 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 042d019b-2ae2-3e1c-aa43-99db8b11e325 | -19.95301 | -49.27233 | 2025-09-12 04:08:00 | NPP-375D | ITAPAGIPE | MINAS GERAIS | Brasil | 3133402 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| 13c4e858-72d1-3590-ad1c-06c349bdfeb7 | -20.00289 | -47.63975 | 2025-09-12 04:08:00 | NPP-375D | CONQUISTA | MINAS GERAIS | Brasil | 3118205 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 0ee01eac-4660-396c-be5b-7ccc90b610df | -19.1706 | -47.96283 | 2025-09-12 04:08:00 | NPP-375D | UBERLÂNDIA | MINAS GERAIS | Brasil | 3170206 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 3e912930-254d-3cb4-888c-4ec71609f583 | -19.87916 | -41.41784 | 2025-09-12 04:08:00 | NPP-375D | MUTUM | MINAS GERAIS | Brasil | 3144003 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| 87175262-023d-3dac-9369-16366655c0a5 | -18.99212 | -48.86246 | 2025-09-12 04:08:00 | NPP-375D | MONTE ALEGRE DE MINAS | MINAS GERAIS | Brasil | 3142809 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 951c3242-c111-3dc3-9948-ede057edba91 | -18.75106 | -47.62056 | 2025-09-12 04:08:00 | NPP-375D | ESTRELA DO SUL | MINAS GERAIS | Brasil | 3124807 | 31 | 33 | nan | nan | nan | Cerrado | 3.6 |
| b58ec8ff-27a8-389c-86fe-ddfec6295847 | -21.1716 | -45.11175 | 2025-09-12 04:08:00 | NPP-375D | LAVRAS | MINAS GERAIS | Brasil | 3138203 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 38bc30a7-d8f2-326a-a4a2-199fb8b0948c | -19.70068 | -45.27303 | 2025-09-12 04:08:00 | NPP-375D | BOM DESPACHO | MINAS GERAIS | Brasil | 3107406 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 52113cc0-0965-3fef-a9dd-0f2f60f3f2de | -18.77015 | -48.54639 | 2025-09-12 04:08:00 | NPP-375D | TUPACIGUARA | MINAS GERAIS | Brasil | 3169604 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 1d446ec7-df87-34b1-80f6-548cd1d8404d | -23.14558 | -49.65134 | 2025-09-12 04:08:00 | NPP-375D | TIMBURI | SÃO PAULO | Brasil | 3554607 | 35 | 33 | nan | nan | nan | Mata Atlântica | 4.4 |
| ece1a714-f0ed-37c1-9a4c-572820f48487 | -20.12727 | -47.68353 | 2025-09-12 04:08:00 | NPP-375D | IGARAPAVA | SÃO PAULO | Brasil | 3520103 | 35 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 8b7eac4d-4280-3fe2-b857-da844e323c76 | -21.9726 | -47.56014 | 2025-09-12 04:08:00 | NPP-375D | DESCALVADO | SÃO PAULO | Brasil | 3513702 | 35 | 33 | nan | nan | nan | Cerrado | 1.5 |
| bb1c09eb-18d5-3c83-ae78-1b6cd9004079 | -22.19504 | -49.59101 | 2025-09-12 04:08:00 | NPP-375D | GARÇA | SÃO PAULO | Brasil | 3516705 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| c81e63f5-8bde-38a4-af4a-0c1ef26bdef3 | -21.19376 | -47.53131 | 2025-09-12 04:08:00 | NPP-375D | ALTINÓPOLIS | SÃO PAULO | Brasil | 3501004 | 35 | 33 | nan | nan | nan | Cerrado | 30.5 |
| d9a48157-91a9-332b-a438-9e948095926c | -18.62465 | -48.26607 | 2025-09-12 04:08:00 | NPP-375D | ARAGUARI | MINAS GERAIS | Brasil | 3103504 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.7 |
| 6393b9fc-17f0-3d26-be2b-fc2dfb6ce891 | -20.4382 | -42.78609 | 2025-09-12 04:08:00 | NPP-375D | ORATÓRIOS | MINAS GERAIS | Brasil | 3145851 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| cdeed743-a3aa-36ad-88bb-3574db6a9dce | -23.28049 | -46.4783 | 2025-09-12 04:08:00 | NPP-375D | MAIRIPORÃ | SÃO PAULO | Brasil | 3528502 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.3 |
| 0eeba590-8021-35e2-9d8c-3b6ef13e9457 | -18.74791 | -47.62398 | 2025-09-12 04:08:00 | NPP-375D | ESTRELA DO SUL | MINAS GERAIS | Brasil | 3124807 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 59295e76-9569-3443-af18-1cdeedf6b16c | -20.00097 | -47.65025 | 2025-09-12 04:08:00 | NPP-375D | CONQUISTA | MINAS GERAIS | Brasil | 3118205 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| aedfbe3d-b049-3775-9e0e-a93604958f63 | -18.55754 | -46.5605 | 2025-09-12 04:08:00 | NPP-375D | PATOS DE MINAS | MINAS GERAIS | Brasil | 3148004 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 1880d21b-03a8-36b7-a873-0e034c9a6cbc | -23.19372 | -49.64614 | 2025-09-12 04:08:00 | NPP-375D | TIMBURI | SÃO PAULO | Brasil | 3554607 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| 288b319c-d15b-38e7-a83e-82d78a31d2b1 | -22.63705 | -53.09037 | 2025-09-12 04:08:00 | NPP-375D | ROSANA | SÃO PAULO | Brasil | 3544251 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| fa139246-2e17-345d-80b8-586dc28c1e1f | -22.61032 | -47.28378 | 2025-09-12 04:08:00 | NPP-375D | LIMEIRA | SÃO PAULO | Brasil | 3526902 | 35 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 725934a2-f4f3-35ec-af5a-9031588b5985 | -21.19288 | -47.53611 | 2025-09-12 04:08:00 | NPP-375D | SERRANA | SÃO PAULO | Brasil | 3551504 | 35 | 33 | nan | nan | nan | Cerrado | 30.5 |
| 8da67cd1-6730-318c-afe7-c64c659acb86 | -21.18805 | -47.5199 | 2025-09-12 04:08:00 | NPP-375D | ALTINÓPOLIS | SÃO PAULO | Brasil | 3501004 | 35 | 33 | nan | nan | nan | Cerrado | 217.9 |
| a40e7a25-1254-3339-887f-d1bca8d14fba | -19.81571 | -45.00258 | 2025-09-12 04:08:00 | NPP-375D | NOVA SERRANA | MINAS GERAIS | Brasil | 3145208 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 36516379-be57-388b-826b-d0311b151ced | -23.13722 | -47.4978 | 2025-09-12 04:08:00 | NPP-375D | PORTO FELIZ | SÃO PAULO | Brasil | 3540606 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| fe1f0b42-e005-3bfb-ad58-ee066000fa4e | -19.83986 | -44.58712 | 2025-09-12 04:08:00 | NPP-375D | PARÁ DE MINAS | MINAS GERAIS | Brasil | 3147105 | 31 | 33 | nan | nan | nan | Mata Atlântica | 5.1 |
| 763a83b4-3701-36d2-913b-c7ec8232fc11 | -19.98633 | -47.62112 | 2025-09-12 04:08:00 | NPP-375D | CONQUISTA | MINAS GERAIS | Brasil | 3118205 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| d43fc614-6776-3c12-bfbe-f935921ddc0a | -18.30049 | -50.42663 | 2025-09-12 04:08:00 | NPP-375D | QUIRINÓPOLIS | GOIÁS | Brasil | 5218508 | 52 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 3ab192bc-371d-3fe7-8781-1b3984009684 | -21.3821 | -45.19088 | 2025-09-12 04:08:00 | NPP-375D | CARMO DA CACHOEIRA | MINAS GERAIS | Brasil | 3113909 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 35b6d213-4040-3f01-9edb-dc45b770e733 | -22.60705 | -47.28525 | 2025-09-12 04:08:00 | NPP-375D | LIMEIRA | SÃO PAULO | Brasil | 3526902 | 35 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 1bc260bd-8748-3958-b0f7-e3041f4eaf91 | -18.31213 | -50.42006 | 2025-09-12 04:08:00 | NPP-375D | QUIRINÓPOLIS | GOIÁS | Brasil | 5218508 | 52 | 33 | nan | nan | nan | Cerrado | 15.1 |
| 9140bccd-8d84-3b03-99b9-39fc361aba10 | -17.80699 | -50.00406 | 2025-09-12 04:08:00 | NPP-375D | GOIATUBA | GOIÁS | Brasil | 5209101 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 21413d74-994f-3303-b3ba-b8ea86b9bb01 | -18.65941 | -47.66169 | 2025-09-12 04:08:00 | NPP-375D | ESTRELA DO SUL | MINAS GERAIS | Brasil | 3124807 | 31 | 33 | nan | nan | nan | Cerrado | 2.7 |
| c5840097-ee4f-32e3-b9e5-387fd4f93120 | -21.94652 | -47.55473 | 2025-09-12 04:08:00 | NPP-375D | DESCALVADO | SÃO PAULO | Brasil | 3513702 | 35 | 33 | nan | nan | nan | Cerrado | 1.2 |
| f12ebec9-d804-3487-afda-7c94aaa94823 | -19.95226 | -44.45753 | 2025-09-12 04:08:00 | NPP-375D | MATEUS LEME | MINAS GERAIS | Brasil | 3140704 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 49955b85-da98-32f5-a4be-e8e31ab2411c | -24.16303 | -51.04162 | 2025-09-12 04:08:00 | NPP-375D | ORTIGUEIRA | PARANÁ | Brasil | 4117305 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 59e45934-457f-369d-897d-8991c78a6f8a | -23.11277 | -47.4953 | 2025-09-12 04:08:00 | NPP-375D | PORTO FELIZ | SÃO PAULO | Brasil | 3540606 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.3 |
| 8e1a23df-eb75-3478-b2a1-0c8d50498277 | -22.81808 | -46.4323 | 2025-09-12 04:08:00 | NPP-375D | PEDRA BELA | SÃO PAULO | Brasil | 3536802 | 35 | 33 | nan | nan | nan | Mata Atlântica | 12.7 |
| 7802b687-90f9-390b-954d-4d4e59073dc5 | -23.34621 | -47.2144 | 2025-09-12 04:08:00 | NPP-375D | ITU | SÃO PAULO | Brasil | 3523909 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 687ef42a-cc66-396e-b0a4-1c19a0a40731 | -22.18845 | -49.60234 | 2025-09-12 04:08:00 | NPP-375D | GARÇA | SÃO PAULO | Brasil | 3516705 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| 9f738877-e582-354c-84d2-801ec32604b3 | -21.9577 | -47.55705 | 2025-09-12 04:08:00 | NPP-375D | DESCALVADO | SÃO PAULO | Brasil | 3513702 | 35 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 5e8639ed-deea-38cf-b90d-f4ca7f084652 | -20.01827 | -47.64309 | 2025-09-12 04:08:00 | NPP-375D | CONQUISTA | MINAS GERAIS | Brasil | 3118205 | 31 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 2d3babc0-c132-3cf7-8b1b-0142a2ac1b1a | -21.38893 | -45.19217 | 2025-09-12 04:08:00 | NPP-375D | CARMO DA CACHOEIRA | MINAS GERAIS | Brasil | 3113909 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 1f531d5a-4a39-3e17-b0c9-0bbb2781ea4a | -18.62107 | -48.25026 | 2025-09-12 04:08:00 | NPP-375D | ARAGUARI | MINAS GERAIS | Brasil | 3103504 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| adbd6128-1f46-3e63-82c2-042374262e87 | -21.95483 | -47.55161 | 2025-09-12 04:08:00 | NPP-375D | DESCALVADO | SÃO PAULO | Brasil | 3513702 | 35 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 0e09bfe1-3085-31bb-b18f-10af9ffa1304 | -20.72672 | -42.1492 | 2025-09-12 04:08:00 | NPP-375D | CARANGOLA | MINAS GERAIS | Brasil | 3113305 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.3 |
| 9ce66005-7932-32ea-97b5-87b3ea7a6558 | -18.32324 | -52.08207 | 2025-09-12 04:08:00 | NPP-375D | SERRANÓPOLIS | GOIÁS | Brasil | 5220504 | 52 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 9b483e6c-3c96-3e20-a575-1ab6b03f964b | -23.84134 | -51.07607 | 2025-09-12 04:08:00 | NPP-375D | TAMARANA | PARANÁ | Brasil | 4126678 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| c8b3e73f-04a1-3d6e-b1c2-3a4d6161e8e9 | -22.6987 | -48.70027 | 2025-09-12 04:08:00 | NPP-375D | LENÇÓIS PAULISTA | SÃO PAULO | Brasil | 3526803 | 35 | 33 | nan | nan | nan | Cerrado | 36.0 |
| 0cfe5b2f-0fba-33d7-9aad-b4bb53ac6f21 | -20.56784 | -43.74638 | 2025-09-12 04:08:00 | NPP-375D | OURO BRANCO | MINAS GERAIS | Brasil | 3145901 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 7aa6b989-384d-3988-922a-0f9584736df2 | -21.18249 | -47.52888 | 2025-09-12 04:08:00 | NPP-375D | SERRANA | SÃO PAULO | Brasil | 3551504 | 35 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 784515fa-a557-3f6d-80b5-55911461a344 | -19.70895 | -44.2395 | 2025-09-12 04:08:00 | NPP-375D | ESMERALDAS | MINAS GERAIS | Brasil | 3124104 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| eb93d3b4-80ea-3463-90a3-10aef0407310 | -18.41983 | -46.48781 | 2025-09-12 04:08:00 | NPP-375D | PRESIDENTE OLEGÁRIO | MINAS GERAIS | Brasil | 3153400 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| cdd39122-d971-31bb-b3cc-14e769f9e663 | -22.13961 | -47.83556 | 2025-09-12 04:08:00 | NPP-375D | SÃO CARLOS | SÃO PAULO | Brasil | 3548906 | 35 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 91de6298-3a79-39ae-a063-90e04f4ecd7a | -18.62514 | -48.25113 | 2025-09-12 04:08:00 | NPP-375D | ARAGUARI | MINAS GERAIS | Brasil | 3103504 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| e798b6ef-b066-3d9d-a266-a77178a2c5de | -21.9419 | -47.55882 | 2025-09-12 04:08:00 | NPP-375D | DESCALVADO | SÃO PAULO | Brasil | 3513702 | 35 | 33 | nan | nan | nan | Cerrado | 2.9 |
| c9bc2f60-c0ca-3fa9-b27c-787e459a2704 | -21.4917 | -45.94341 | 2025-09-12 04:08:00 | NPP-375D | ALFENAS | MINAS GERAIS | Brasil | 3101607 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| b32eb242-408d-31fa-9e24-3fc669e91d82 | -21.33965 | -45.02992 | 2025-09-12 04:08:00 | NPP-375D | LAVRAS | MINAS GERAIS | Brasil | 3138203 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.9 |
| d172aa58-03b9-3e1b-bb1d-5f3624d04572 | -20.12054 | -44.89262 | 2025-09-12 04:08:00 | NPP-375D | DIVINÓPOLIS | MINAS GERAIS | Brasil | 3122306 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 1da69a3b-ad70-3312-8b54-3d8920a4431b | -23.1482 | -48.26004 | 2025-09-12 04:08:00 | NPP-375D | BOFETE | SÃO PAULO | Brasil | 3506904 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| 454ca9fe-204c-3d0b-8e01-6721995ae9c9 | -22.28028 | -45.38431 | 2025-09-12 04:08:00 | NPP-375D | MARIA DA FÉ | MINAS GERAIS | Brasil | 3139904 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| fd6f5450-4981-3a50-bda8-4c54615d617f | -23.14061 | -49.6548 | 2025-09-12 04:08:00 | NPP-375D | TIMBURI | SÃO PAULO | Brasil | 3554607 | 35 | 33 | nan | nan | nan | Mata Atlântica | 4.4 |
| ff909675-261b-3c95-b948-c21ba4c9cb1d | -18.74885 | -47.61875 | 2025-09-12 04:08:00 | NPP-375D | MONTE CARMELO | MINAS GERAIS | Brasil | 3143104 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 53b99881-1f8b-3e07-aee4-e4b9a9ea1b29 | -21.95683 | -47.56177 | 2025-09-12 04:08:00 | NPP-375D | DESCALVADO | SÃO PAULO | Brasil | 3513702 | 35 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 903edcf5-cd2a-34e0-9a4c-2511531a2b13 | -18.68503 | -47.6779 | 2025-09-12 04:08:00 | NPP-375D | ESTRELA DO SUL | MINAS GERAIS | Brasil | 3124807 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 0505181c-7bf6-3712-9181-93442f2331aa | -20.17618 | -44.62408 | 2025-09-12 04:08:00 | NPP-375D | CARMO DO CAJURU | MINAS GERAIS | Brasil | 3114204 | 31 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 16389593-8f07-31d2-9842-1ad006ea4430 | -20.14427 | -43.68663 | 2025-09-12 04:08:00 | NPP-375D | ITABIRITO | MINAS GERAIS | Brasil | 3131901 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| f7f9efa1-403d-3941-b598-332a418574e7 | -20.1582 | -43.68538 | 2025-09-12 04:08:00 | NPP-375D | ITABIRITO | MINAS GERAIS | Brasil | 3131901 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.9 |
| 5646421c-38a8-34cb-b66a-21911a7a90fb | -20.00805 | -46.92593 | 2025-09-12 04:08:00 | NPP-375D | TAPIRA | MINAS GERAIS | Brasil | 3168101 | 31 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 68f0f355-6df4-30fc-a8eb-534977ab14b4 | -18.44585 | -47.18034 | 2025-09-12 04:08:00 | NPP-375D | COROMANDEL | MINAS GERAIS | Brasil | 3119302 | 31 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 375e052e-1942-3094-9478-f0a4ade06372 | -18.77501 | -48.54345 | 2025-09-12 04:08:00 | NPP-375D | TUPACIGUARA | MINAS GERAIS | Brasil | 3169604 | 31 | 33 | nan | nan | nan | Cerrado | 3.8 |
| c8b6aecb-d8c8-345c-805e-a6322f40131a | -22.19344 | -49.59909 | 2025-09-12 04:08:00 | NPP-375D | GARÇA | SÃO PAULO | Brasil | 3516705 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| cb74e1c2-78d1-34ad-ae18-5742c164f8c9 | -22.61044 | -46.41943 | 2025-09-12 04:08:00 | NPP-375D | SOCORRO | SÃO PAULO | Brasil | 3552106 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.3 |
| e40214ba-af29-3267-96f5-e207df7040c7 | -21.95024 | -47.55552 | 2025-09-12 04:08:00 | NPP-375D | DESCALVADO | SÃO PAULO | Brasil | 3513702 | 35 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 50403000-dd8a-379e-a8b1-075709ba9a9f | -20.5849 | -48.57507 | 2025-09-12 04:08:00 | NPP-375D | BARRETOS | SÃO PAULO | Brasil | 3505500 | 35 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 660f3594-03fc-3b12-941c-ee65c2c8c26e | -19.9843 | -47.61051 | 2025-09-12 04:08:00 | NPP-375D | CONQUISTA | MINAS GERAIS | Brasil | 3118205 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| f57e0d16-4a32-3b99-ad46-abbdfa3045d0 | -22.65981 | -53.11335 | 2025-09-12 04:08:00 | NPP-375D | MARILENA | PARANÁ | Brasil | 4115002 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 244f6b00-7a95-349a-bea9-f92bebfd7a39 | -18.99133 | -48.8666 | 2025-09-12 04:08:00 | NPP-375D | MONTE ALEGRE DE MINAS | MINAS GERAIS | Brasil | 3142809 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 91605ee6-e3d3-3c7b-8afb-a76a4dee2a39 | -21.64953 | -46.40971 | 2025-09-12 04:08:00 | NPP-375D | BOTELHOS | MINAS GERAIS | Brasil | 3108404 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 33d6b55c-5b26-3acb-9a12-54cec158e3e4 | -21.18715 | -47.52483 | 2025-09-12 04:08:00 | NPP-375D | ALTINÓPOLIS | SÃO PAULO | Brasil | 3501004 | 35 | 33 | nan | nan | nan | Cerrado | 217.9 |
| 5624fcac-3343-3db6-b79b-f3a05575df0b | -18.6584 | -47.66711 | 2025-09-12 04:08:00 | NPP-375D | ESTRELA DO SUL | MINAS GERAIS | Brasil | 3124807 | 31 | 33 | nan | nan | nan | Cerrado | 4.2 |
| d3d8dc89-7897-3fcb-b5da-d19ac63adc06 | -21.94475 | -47.56439 | 2025-09-12 04:08:00 | NPP-375D | DESCALVADO | SÃO PAULO | Brasil | 3513702 | 35 | 33 | nan | nan | nan | Cerrado | 2.9 |
| a074ba7a-8955-3369-adb1-f58a737c959e | -21.94738 | -47.55004 | 2025-09-12 04:08:00 | NPP-375D | DESCALVADO | SÃO PAULO | Brasil | 3513702 | 35 | 33 | nan | nan | nan | Cerrado | 1.2 |


[Clique aqui para ver as próximas entradas](README55.md)
