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

## Dados Diários - Página 30

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 5ffab5eb-2ef7-35bf-9a18-0c78c331bea5 | -20.39843 | -43.94042 | 2024-10-08 03:19:00 | NPP-375D | MOEDA | MINAS GERAIS | Brasil | 3142304 | 31 | 33 | nan | nan | nan | Mata Atlântica | 7.2 |
| 4b9986a4-3982-3ca5-b82a-5b293c5be4de | -20.39691 | -43.94706 | 2024-10-08 03:19:00 | NPP-375D | MOEDA | MINAS GERAIS | Brasil | 3142304 | 31 | 33 | nan | nan | nan | Mata Atlântica | 6.6 |
| 67679072-d92b-3f0f-9147-82be1fa3c6e3 | -20.39557 | -43.92506 | 2024-10-08 03:19:00 | NPP-375D | OURO PRETO | MINAS GERAIS | Brasil | 3146107 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| ec1f79af-c87a-3f0b-b660-55aa857ac5e7 | -20.39276 | -43.93736 | 2024-10-08 03:19:00 | NPP-375D | MOEDA | MINAS GERAIS | Brasil | 3142304 | 31 | 33 | nan | nan | nan | Mata Atlântica | 7.2 |
| 1e005a29-e4c7-3db1-8d2d-5fbf57d7e963 | -20.39115 | -43.94438 | 2024-10-08 03:19:00 | NPP-375D | MOEDA | MINAS GERAIS | Brasil | 3142304 | 31 | 33 | nan | nan | nan | Mata Atlântica | 6.6 |
| f7e7df9b-7b3b-31eb-a039-646611b34b8a | -20.38978 | -43.95033 | 2024-10-08 03:19:00 | NPP-375D | MOEDA | MINAS GERAIS | Brasil | 3142304 | 31 | 33 | nan | nan | nan | Mata Atlântica | 6.6 |
| ff768f40-0bbf-3927-b31e-d06733103700 | -20.38852 | -43.95584 | 2024-10-08 03:19:00 | NPP-375D | MOEDA | MINAS GERAIS | Brasil | 3142304 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| 94a438b7-41b2-3690-8e09-d91c8e670d1d | -20.38554 | -43.94103 | 2024-10-08 03:19:00 | NPP-375D | MOEDA | MINAS GERAIS | Brasil | 3142304 | 31 | 33 | nan | nan | nan | Mata Atlântica | 6.2 |
| 344c2a5a-4885-3dc0-aede-61f80ef2e4c7 | -20.38391 | -43.94812 | 2024-10-08 03:19:00 | NPP-375D | MOEDA | MINAS GERAIS | Brasil | 3142304 | 31 | 33 | nan | nan | nan | Mata Atlântica | 6.2 |
| 6c4aa609-ccb4-3918-bd1a-5ac40ab2c022 | -20.38259 | -43.95386 | 2024-10-08 03:19:00 | NPP-375D | MOEDA | MINAS GERAIS | Brasil | 3142304 | 31 | 33 | nan | nan | nan | Mata Atlântica | 7.1 |
| 900fa991-3d25-35b2-8faf-1a215404ec87 | -20.38142 | -43.93116 | 2024-10-08 03:19:00 | NPP-375D | MOEDA | MINAS GERAIS | Brasil | 3142304 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 9e0776fb-7cb9-3ba0-966c-0672187ab18e | -20.3813 | -43.95947 | 2024-10-08 03:19:00 | NPP-375D | MOEDA | MINAS GERAIS | Brasil | 3142304 | 31 | 33 | nan | nan | nan | Mata Atlântica | 7.1 |
| d76e2294-f3fb-35b8-8959-ca2ba63b98f3 | -20.37803 | -43.94595 | 2024-10-08 03:19:00 | NPP-375D | MOEDA | MINAS GERAIS | Brasil | 3142304 | 31 | 33 | nan | nan | nan | Mata Atlântica | 6.2 |
| 89185f72-b811-34a2-b766-d2a64bfe7146 | -20.37665 | -43.95191 | 2024-10-08 03:19:00 | NPP-375D | MOEDA | MINAS GERAIS | Brasil | 3142304 | 31 | 33 | nan | nan | nan | Mata Atlântica | 7.1 |
| 2f39655a-9501-3198-9d97-35174bc67988 | -20.37525 | -43.958 | 2024-10-08 03:19:00 | NPP-375D | MOEDA | MINAS GERAIS | Brasil | 3142304 | 31 | 33 | nan | nan | nan | Mata Atlântica | 7.1 |
| 9bf7b352-c50e-3b9a-8868-1c416de6c680 | -20.37416 | -43.93503 | 2024-10-08 03:19:00 | NPP-375D | MOEDA | MINAS GERAIS | Brasil | 3142304 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| d0df08c0-602b-3b52-a676-cafe5a31874a | -20.37391 | -43.96383 | 2024-10-08 03:19:00 | NPP-375D | MOEDA | MINAS GERAIS | Brasil | 3142304 | 31 | 33 | nan | nan | nan | Mata Atlântica | 8.9 |
| 3a6357dc-67a0-3c9e-bb0c-74e042ecce4d | -20.37239 | -43.94269 | 2024-10-08 03:19:00 | NPP-375D | MOEDA | MINAS GERAIS | Brasil | 3142304 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| c88539ac-014b-3def-8e83-e8d886a1ae56 | -20.37066 | -43.95018 | 2024-10-08 03:19:00 | NPP-375D | MOEDA | MINAS GERAIS | Brasil | 3142304 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 979351a5-e0ab-3c1a-86b7-4d913e96cb04 | -20.36819 | -43.93328 | 2024-10-08 03:19:00 | NPP-375D | ITABIRITO | MINAS GERAIS | Brasil | 3131901 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| e3adeead-ca9b-37ce-8008-6b50cd5a019f | -20.36494 | -43.94734 | 2024-10-08 03:19:00 | NPP-375D | MOEDA | MINAS GERAIS | Brasil | 3142304 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| bbce0048-3231-3bb9-bc90-ed4e94b2e44d | -20.36351 | -43.95353 | 2024-10-08 03:19:00 | NPP-375D | MOEDA | MINAS GERAIS | Brasil | 3142304 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| d9c00b74-f995-38a4-b458-8d0c438daf8e | -20.35946 | -43.94339 | 2024-10-08 03:19:00 | NPP-375D | MOEDA | MINAS GERAIS | Brasil | 3142304 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.6 |
| f82275ca-2cbd-3305-b0a8-933426730363 | -20.23387 | -44.44197 | 2024-10-08 03:19:00 | NPP-375D | ITATIAIUÇU | MINAS GERAIS | Brasil | 3133709 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 377f35b6-ed3f-3a3e-ba5e-60a7ec634ff3 | -20.22988 | -44.44196 | 2024-10-08 03:19:00 | NPP-375D | ITATIAIUÇU | MINAS GERAIS | Brasil | 3133709 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| bef8760d-e1cc-3a30-95d3-9bcc1f2dff86 | -20.22751 | -44.44101 | 2024-10-08 03:19:00 | NPP-375D | ITATIAIUÇU | MINAS GERAIS | Brasil | 3133709 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| 5a9308a1-6d87-3828-854d-8daae370c669 | -20.22361 | -44.44061 | 2024-10-08 03:19:00 | NPP-375D | ITATIAIUÇU | MINAS GERAIS | Brasil | 3133709 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| 9ad9bde7-6b32-367b-a8f9-ecf5106babea | -20.22126 | -44.43956 | 2024-10-08 03:19:00 | NPP-375D | ITATIAIUÇU | MINAS GERAIS | Brasil | 3133709 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| c0d96df0-ce80-379f-9da9-467444c2b922 | -20.13105 | -43.8563 | 2024-10-08 03:19:00 | NPP-375D | NOVA LIMA | MINAS GERAIS | Brasil | 3144805 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| b09ed96b-fbe2-3e75-b01b-d21dd746550e | -20.12978 | -43.86076 | 2024-10-08 03:19:00 | NPP-375D | NOVA LIMA | MINAS GERAIS | Brasil | 3144805 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.4 |
| 9d74aa14-c4e5-3a55-90a4-b45f550fbf43 | -20.12967 | -43.86245 | 2024-10-08 03:19:00 | NPP-375D | NOVA LIMA | MINAS GERAIS | Brasil | 3144805 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 25c1aa4a-ada2-3afd-a1ee-6b491b77d5a3 | -20.12855 | -43.86607 | 2024-10-08 03:19:00 | NPP-375D | NOVA LIMA | MINAS GERAIS | Brasil | 3144805 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.7 |
| bf39fad7-6d0e-340c-99ba-1b0c84fcdb58 | -19.8319 | -43.79757 | 2024-10-08 03:19:00 | NPP-375D | SANTA LUZIA | MINAS GERAIS | Brasil | 3157807 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 7089f6f4-bc2b-3f15-81c2-0689043052c0 | -19.27768 | -46.12846 | 2024-10-08 03:19:00 | NPP-375D | SÃO GOTARDO | MINAS GERAIS | Brasil | 3162104 | 31 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 7f02a17a-aa68-316d-8f0d-05afc5851a78 | -19.27613 | -46.13494 | 2024-10-08 03:19:00 | NPP-375D | RIO PARANAÍBA | MINAS GERAIS | Brasil | 3155504 | 31 | 33 | nan | nan | nan | Cerrado | 2.6 |
| ac21538b-7427-34dd-b3eb-4f4890c06b1d | -19.27567 | -46.12749 | 2024-10-08 03:19:00 | NPP-375D | SÃO GOTARDO | MINAS GERAIS | Brasil | 3162104 | 31 | 33 | nan | nan | nan | Cerrado | 6.4 |
| b06b47c8-dde8-34c0-92a9-294f0b5e2f8d | -19.27402 | -46.13416 | 2024-10-08 03:19:00 | NPP-375D | RIO PARANAÍBA | MINAS GERAIS | Brasil | 3155504 | 31 | 33 | nan | nan | nan | Cerrado | 8.2 |
| 878ca361-f012-397b-8f03-cf9e0f1250b2 | -19.27084 | -46.12625 | 2024-10-08 03:19:00 | NPP-375D | SÃO GOTARDO | MINAS GERAIS | Brasil | 3162104 | 31 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 8dc08f4a-5080-3462-901b-b426c89f2334 | -19.26914 | -46.13336 | 2024-10-08 03:19:00 | NPP-375D | RIO PARANAÍBA | MINAS GERAIS | Brasil | 3155504 | 31 | 33 | nan | nan | nan | Cerrado | 2.6 |
| b8b0a455-bbda-3c16-9973-a284f909d9e7 | -20.65247 | -45.92405 | 2024-10-08 03:19:00 | NPP-375D | GUAPÉ | MINAS GERAIS | Brasil | 3128105 | 31 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 17f55278-9217-3367-bf7c-6ec125ec12c0 | -20.65172 | -45.91945 | 2024-10-08 03:19:00 | NPP-375D | GUAPÉ | MINAS GERAIS | Brasil | 3128105 | 31 | 33 | nan | nan | nan | Cerrado | 2.9 |
| b6e2dcaf-b3da-30dd-bbf4-f9e0301374dd | -20.65004 | -45.92649 | 2024-10-08 03:19:00 | NPP-375D | GUAPÉ | MINAS GERAIS | Brasil | 3128105 | 31 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 2faed03d-329a-31b3-ae53-18a393e79344 | -20.64399 | -45.9296 | 2024-10-08 03:19:00 | NPP-375D | GUAPÉ | MINAS GERAIS | Brasil | 3128105 | 31 | 33 | nan | nan | nan | Cerrado | 2.8 |
| e2ea9bf0-1f50-31e1-a715-0e012ebd80a0 | -20.6415 | -45.93247 | 2024-10-08 03:19:00 | NPP-375D | GUAPÉ | MINAS GERAIS | Brasil | 3128105 | 31 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 4667edf7-cb94-38b3-a66c-4e63efd36bc1 | -20.32293 | -46.26778 | 2024-10-08 03:19:00 | NPP-375D | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 13.8 |
| 69e3ca71-3f39-3bda-b3cf-5cc2e6f4adb5 | -20.32217 | -46.26739 | 2024-10-08 03:19:00 | NPP-375D | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 24.8 |
| e82446f5-7bbd-3f46-b84d-6bc9157d56e9 | -20.32127 | -46.27466 | 2024-10-08 03:19:00 | NPP-375D | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 13.8 |
| d1d31c63-b3fb-3f9a-baee-f5f87a17d004 | -20.32047 | -46.27422 | 2024-10-08 03:19:00 | NPP-375D | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 30.8 |
| 3248324a-7d6a-3e04-ac62-d8882485e7b8 | -20.31621 | -46.26544 | 2024-10-08 03:19:00 | NPP-375D | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 13.8 |
| 86bcd80b-306a-3587-87ce-4700a05a09a6 | -20.31545 | -46.26507 | 2024-10-08 03:19:00 | NPP-375D | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 10.6 |
| 4babe486-4b41-39e3-9107-58c792745555 | -20.31454 | -46.27233 | 2024-10-08 03:19:00 | NPP-375D | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 13.8 |
| 2230358f-4b27-373a-b507-29be0047f488 | -20.31373 | -46.27195 | 2024-10-08 03:19:00 | NPP-375D | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 11.3 |
| dc18682a-8ef1-353b-b0fe-928b35a98871 | -19.8665 | -45.68544 | 2024-10-08 03:19:00 | NPP-375D | LUZ | MINAS GERAIS | Brasil | 3138807 | 31 | 33 | nan | nan | nan | Cerrado | 2.2 |
| e0f85da0-b8dd-3dcc-a497-d48b7e703391 | -19.85983 | -45.68357 | 2024-10-08 03:19:00 | NPP-375D | LUZ | MINAS GERAIS | Brasil | 3138807 | 31 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 87bf3217-6e57-3713-aca5-9f4a98c33006 | -21.8923 | -46.7167 | 2024-10-08 03:19:00 | NPP-375D | ÁGUAS DA PRATA | SÃO PAULO | Brasil | 3500402 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.1 |
| 4798c236-3a14-3cd8-8a59-622c0606d44f | -21.82358 | -45.68248 | 2024-10-08 03:19:00 | NPP-375D | CORDISLÂNDIA | MINAS GERAIS | Brasil | 3119005 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.1 |
| 471a24f6-110b-3ab4-9c36-8c1ba04fcc89 | -21.81728 | -45.68014 | 2024-10-08 03:19:00 | NPP-375D | CORDISLÂNDIA | MINAS GERAIS | Brasil | 3119005 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.3 |
| 0429c6ac-20b4-3154-a77a-f383bd416129 | -21.81579 | -45.68626 | 2024-10-08 03:19:00 | NPP-375D | CORDISLÂNDIA | MINAS GERAIS | Brasil | 3119005 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.7 |
| f9e94f98-79b9-3799-b066-6076e17e42f2 | -21.20469 | -45.79484 | 2024-10-08 03:19:00 | NPP-375D | CAMPOS GERAIS | MINAS GERAIS | Brasil | 3111606 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.4 |
| d3079a3a-9565-3dd4-b055-d64b95361a21 | -21.20312 | -45.80121 | 2024-10-08 03:19:00 | NPP-375D | CAMPOS GERAIS | MINAS GERAIS | Brasil | 3111606 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.4 |
| c602261c-0069-3094-a7c4-a73c67c8245c | -21.20156 | -45.79484 | 2024-10-08 03:19:00 | NPP-375D | CAMPOS GERAIS | MINAS GERAIS | Brasil | 3111606 | 31 | 33 | nan | nan | nan | Mata Atlântica | 6.3 |
| 6178dc18-02dc-3619-be1c-ed235f067941 | -21.20001 | -45.80125 | 2024-10-08 03:19:00 | NPP-375D | CAMPOS GERAIS | MINAS GERAIS | Brasil | 3111606 | 31 | 33 | nan | nan | nan | Mata Atlântica | 8.2 |
| f02eaa8f-5077-37cc-92be-5879377e2b7f | -21.19827 | -45.79253 | 2024-10-08 03:19:00 | NPP-375D | CAMPOS GERAIS | MINAS GERAIS | Brasil | 3111606 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.4 |
| 0e93c5f2-6272-3c3d-ac69-900190cb313a | -21.19668 | -45.79895 | 2024-10-08 03:19:00 | NPP-375D | CAMPOS GERAIS | MINAS GERAIS | Brasil | 3111606 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.4 |
| 280283bb-c86d-3633-b213-c7ecd43e3870 | -22.80216 | -46.75716 | 2024-10-08 03:19:00 | NPP-375D | AMPARO | SÃO PAULO | Brasil | 3501905 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.8 |
| fc8437a4-f526-3887-88d4-5e5099956ece | -22.80078 | -46.76255 | 2024-10-08 03:19:00 | NPP-375D | AMPARO | SÃO PAULO | Brasil | 3501905 | 35 | 33 | nan | nan | nan | Mata Atlântica | 5.2 |
| dc16e24e-80d0-3699-8933-6438290cff70 | -22.80011 | -46.75886 | 2024-10-08 03:19:00 | NPP-375D | AMPARO | SÃO PAULO | Brasil | 3501905 | 35 | 33 | nan | nan | nan | Mata Atlântica | 4.3 |
| 2473897b-d2b7-32e1-a1f1-e98cc1b5acce | -22.79925 | -46.76852 | 2024-10-08 03:19:00 | NPP-375D | AMPARO | SÃO PAULO | Brasil | 3501905 | 35 | 33 | nan | nan | nan | Mata Atlântica | 5.2 |
| 61cee052-90fd-3563-b0b6-d06c1064ca8f | -22.79867 | -46.76462 | 2024-10-08 03:19:00 | NPP-375D | AMPARO | SÃO PAULO | Brasil | 3501905 | 35 | 33 | nan | nan | nan | Mata Atlântica | 8.6 |
| 77cd9da7-9f19-3847-b403-477e03b022f4 | -22.58405 | -46.66863 | 2024-10-08 03:19:00 | NPP-375D | SERRA NEGRA | SÃO PAULO | Brasil | 3551603 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| 3e5687bc-c7c0-3312-9c0b-dc3ca9f1b283 | -22.58059 | -46.66053 | 2024-10-08 03:19:00 | NPP-375D | SERRA NEGRA | SÃO PAULO | Brasil | 3551603 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.8 |
| fbbd1d64-d0ad-3726-a459-fc610c0b3a42 | -22.57853 | -46.66856 | 2024-10-08 03:19:00 | NPP-375D | SERRA NEGRA | SÃO PAULO | Brasil | 3551603 | 35 | 33 | nan | nan | nan | Mata Atlântica | 5.4 |
| f5836499-2b16-3afa-b532-6413804e73ff | -22.57738 | -46.70089 | 2024-10-08 03:19:00 | NPP-375D | SERRA NEGRA | SÃO PAULO | Brasil | 3551603 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.8 |
| 6d85b9db-ac43-394d-92b5-cd684bd348a0 | -22.57717 | -46.66758 | 2024-10-08 03:19:00 | NPP-375D | SERRA NEGRA | SÃO PAULO | Brasil | 3551603 | 35 | 33 | nan | nan | nan | Mata Atlântica | 4.3 |
| ab1b1310-ce40-3294-a154-b8d9b0ce7504 | -22.57613 | -46.70028 | 2024-10-08 03:19:00 | NPP-375D | SERRA NEGRA | SÃO PAULO | Brasil | 3551603 | 35 | 33 | nan | nan | nan | Mata Atlântica | 5.7 |
| eb29ddb2-3011-3974-a854-67d6b94ebe52 | -22.57248 | -46.69208 | 2024-10-08 03:19:00 | NPP-375D | SERRA NEGRA | SÃO PAULO | Brasil | 3551603 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.8 |
| e060c157-ea6c-390a-abeb-83a7fc9f6ae4 | -22.57025 | -46.70071 | 2024-10-08 03:19:00 | NPP-375D | SERRA NEGRA | SÃO PAULO | Brasil | 3551603 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.8 |
| 767afbac-9244-339f-a990-d12fce2b5478 | -22.56906 | -46.69992 | 2024-10-08 03:19:00 | NPP-375D | SERRA NEGRA | SÃO PAULO | Brasil | 3551603 | 35 | 33 | nan | nan | nan | Mata Atlântica | 5.3 |
| 4a7b7bbc-870e-332d-be76-b54ce8a3dfde | -22.40929 | -46.61996 | 2024-10-08 03:19:00 | NPP-375D | MONTE SIÃO | MINAS GERAIS | Brasil | 3143401 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.3 |
| 2ea4ac1b-af61-3bca-8785-02f8925e16f2 | -21.59927 | -47.71646 | 2024-10-08 03:19:00 | NPP-375D | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 6d18e605-bf70-3bb0-a7db-cdc6e162aab0 | -21.59886 | -47.71734 | 2024-10-08 03:19:00 | NPP-375D | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 9d7f9a18-bb1c-38f1-9604-6c57212190a7 | -21.59738 | -47.7239 | 2024-10-08 03:19:00 | NPP-375D | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 3.1 |
| b05c49ee-b62d-3470-9fe2-e0e58ad4a4e7 | -21.59689 | -47.72491 | 2024-10-08 03:19:00 | NPP-375D | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 447f2cf6-aee3-368d-912f-4e02c95010b2 | -21.59251 | -47.71276 | 2024-10-08 03:19:00 | NPP-375D | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 2.0 |
| fafb76e8-28cb-3a7e-ba50-aef62abada12 | -21.59211 | -47.71366 | 2024-10-08 03:19:00 | NPP-375D | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 1.1 |
| db24fb08-9e74-3dd5-a802-b461fe39868b | -21.09075 | -47.22871 | 2024-10-08 03:19:00 | NPP-375D | SANTO ANTÔNIO DA ALEGRIA | SÃO PAULO | Brasil | 3547908 | 35 | 33 | nan | nan | nan | Cerrado | 3.0 |
| eeeae2d8-ecce-361d-8fa0-daa473bd78be | -21.09043 | -47.22311 | 2024-10-08 03:19:00 | NPP-375D | SANTO ANTÔNIO DA ALEGRIA | SÃO PAULO | Brasil | 3547908 | 35 | 33 | nan | nan | nan | Cerrado | 1.8 |
| f0967957-c924-3c8d-9b76-5015f1800028 | -21.08838 | -47.2314 | 2024-10-08 03:19:00 | NPP-375D | SANTO ANTÔNIO DA ALEGRIA | SÃO PAULO | Brasil | 3547908 | 35 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 8414e423-ffc2-3709-b593-fb51672f753e | -21.08576 | -47.21858 | 2024-10-08 03:19:00 | NPP-375D | SANTO ANTÔNIO DA ALEGRIA | SÃO PAULO | Brasil | 3547908 | 35 | 33 | nan | nan | nan | Cerrado | 2.2 |
| ae70d9d7-f329-33a2-9f25-6eb24305b952 | -21.08378 | -47.22633 | 2024-10-08 03:19:00 | NPP-375D | ALTINÓPOLIS | SÃO PAULO | Brasil | 3501004 | 35 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 84f79413-a57f-3527-b882-e2e281039553 | -21.08356 | -47.22034 | 2024-10-08 03:19:00 | NPP-375D | SANTO ANTÔNIO DA ALEGRIA | SÃO PAULO | Brasil | 3547908 | 35 | 33 | nan | nan | nan | Cerrado | 1.8 |
| c923a23b-88ea-39c5-80e0-5ba0505b8648 | -21.07609 | -47.21996 | 2024-10-08 03:19:00 | NPP-375D | SANTO ANTÔNIO DA ALEGRIA | SÃO PAULO | Brasil | 3547908 | 35 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 187a7de4-9652-346d-97fc-c25ee508dc92 | -21.07435 | -47.22692 | 2024-10-08 03:19:00 | NPP-375D | SANTO ANTÔNIO DA ALEGRIA | SÃO PAULO | Brasil | 3547908 | 35 | 33 | nan | nan | nan | Cerrado | 2.5 |
| a48b7d09-9c7d-3bfe-9c8d-b5591a43d860 | -21.06904 | -47.22471 | 2024-10-08 03:19:00 | NPP-375D | SANTO ANTÔNIO DA ALEGRIA | SÃO PAULO | Brasil | 3547908 | 35 | 33 | nan | nan | nan | Cerrado | 4.1 |
| c84e232d-1a1f-3614-b8a6-12fda30cc9b7 | -21.06748 | -47.23077 | 2024-10-08 03:19:00 | NPP-375D | SANTO ANTÔNIO DA ALEGRIA | SÃO PAULO | Brasil | 3547908 | 35 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 92f79903-fe81-32ac-a781-42628657ed1c | -21.06695 | -47.22624 | 2024-10-08 03:19:00 | NPP-375D | SANTO ANTÔNIO DA ALEGRIA | SÃO PAULO | Brasil | 3547908 | 35 | 33 | nan | nan | nan | Cerrado | 2.5 |
| c2a04552-7ea3-3bcf-8d75-e6114f98b8ec | -21.06577 | -47.23743 | 2024-10-08 03:19:00 | NPP-375D | ALTINÓPOLIS | SÃO PAULO | Brasil | 3501004 | 35 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 88061035-5a33-3afe-aa8c-841defa45fe4 | -21.06542 | -47.23235 | 2024-10-08 03:19:00 | NPP-375D | SANTO ANTÔNIO DA ALEGRIA | SÃO PAULO | Brasil | 3547908 | 35 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 893c2002-4679-3787-be4f-ee2b77b20b75 | -21.06369 | -47.23927 | 2024-10-08 03:19:00 | NPP-375D | ALTINÓPOLIS | SÃO PAULO | Brasil | 3501004 | 35 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 0ba1d69e-b66e-3128-b7d4-47cd21b49899 | -21.06168 | -47.22386 | 2024-10-08 03:19:00 | NPP-375D | SANTO ANTÔNIO DA ALEGRIA | SÃO PAULO | Brasil | 3547908 | 35 | 33 | nan | nan | nan | Cerrado | 2.2 |


[Clique aqui para ver as próximas entradas](README31.md)
