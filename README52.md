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

## Dados Diários - Página 52

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| d3d271da-c3e3-35c4-8ee1-66747ed561ec | -4.03988 | -47.95217 | 2024-10-23 05:14:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 4299e0f2-872d-3f0a-8ccb-e7b5385f50b7 | -4.03407 | -47.95116 | 2024-10-23 05:14:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 8122144c-cb4d-3ed4-bdbd-2b46d814a770 | -3.98125 | -49.02071 | 2024-10-23 05:14:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 2ca55be0-135b-3e7a-968a-6e830e77510e | -3.98073 | -49.0242 | 2024-10-23 05:14:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 89d59da1-85d1-3916-b89a-6e9cbe808fa7 | -3.97759 | -49.01957 | 2024-10-23 05:14:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| b6dd79f8-8e5a-3503-9e14-5a9664826d2e | -3.97709 | -49.02308 | 2024-10-23 05:14:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 64f77086-fd0d-33a5-94a8-c6937022b8a5 | -3.9758 | -49.02007 | 2024-10-23 05:14:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| da845598-c587-3af5-903c-1e00c933d123 | -3.97528 | -49.02355 | 2024-10-23 05:14:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 584d5ce2-9f69-300a-aac0-a7bfd301a868 | -3.82479 | -48.87009 | 2024-10-23 05:14:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| b17f3aa9-ad69-3d9c-ac17-abd5c376ae49 | -3.82428 | -48.87359 | 2024-10-23 05:14:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| b1747bae-cf79-3485-a6fc-8c6f085205b5 | -3.82377 | -48.87709 | 2024-10-23 05:14:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| e10e5389-2d18-3ee3-8aed-f99df4f3b9ac | -3.80325 | -47.79905 | 2024-10-23 05:14:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 476ca2f9-d616-3b6d-a482-886fbc6f36bc | -3.798 | -47.79403 | 2024-10-23 05:14:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 0462c60d-803f-3926-9201-604ac02de288 | -3.6921 | -49.04639 | 2024-10-23 05:14:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| c30b76c6-a099-3201-8b3f-5a5fc8e4af80 | -3.69161 | -49.0498 | 2024-10-23 05:14:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 0cd8ba66-5dbe-3ff0-b8e8-73fa35fc627c | -2.39005 | -50.31174 | 2024-10-23 05:14:00 | NPP-375D | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 8f7272f5-a747-3e09-91d0-dcf28e090c0f | -2.38744 | -50.3104 | 2024-10-23 05:14:00 | NPP-375D | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 2d30f026-a70d-3e26-b1a7-027ed0bd01a4 | -2.38521 | -50.311 | 2024-10-23 05:14:00 | NPP-375D | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| c65cda24-6d38-3245-ab81-4723c23a7bca | -2.22609 | -50.30596 | 2024-10-23 05:14:00 | NPP-375D | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| ab655e42-01ea-3d2b-bcd6-35e922f9431d | -2.22529 | -50.31123 | 2024-10-23 05:14:00 | NPP-375D | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 8fa91563-526b-38c1-9e71-75cd87789a10 | -2.84984 | -49.54623 | 2024-10-23 05:14:00 | NPP-375D | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 5c9cf49a-0144-3ebb-acd4-86ccc54e2a3a | -2.8447 | -49.54545 | 2024-10-23 05:14:00 | NPP-375D | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 5e1b6779-9b94-32bc-bc04-436ddae0ba25 | -2.84271 | -49.54477 | 2024-10-23 05:14:00 | NPP-375D | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| a3a0edc2-a7cb-3465-a1d3-5d330347ea6a | -2.84225 | -49.54777 | 2024-10-23 05:14:00 | NPP-375D | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 086a7ee6-a5da-3f29-9e16-654d34606967 | -2.79934 | -49.58773 | 2024-10-23 05:14:00 | NPP-375D | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b471feec-c994-3cfb-856e-f68698dab683 | -2.79422 | -49.58696 | 2024-10-23 05:14:00 | NPP-375D | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 59ed1af6-f2c3-3ead-a03b-3fcc54b3ec9a | -2.76316 | -49.30004 | 2024-10-23 05:14:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| e9dd78f7-a573-328e-917a-696dabeae853 | -2.76267 | -49.3032 | 2024-10-23 05:14:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 6686a34c-94e2-3b55-a016-65b011300e9a | -2.76264 | -49.30157 | 2024-10-23 05:14:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 8c5312be-24b7-3795-8fa2-f056a0a7d7ab | -2.76219 | -49.30634 | 2024-10-23 05:14:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| bd73ade0-f112-3de1-b34e-a3a7134a6cb6 | -2.76218 | -49.30472 | 2024-10-23 05:14:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 90312bad-a130-3534-9a58-f0df4d5e9191 | -2.76172 | -49.30786 | 2024-10-23 05:14:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 324c18c3-db55-3708-9e35-44a3c3d12f68 | -2.7617 | -49.30947 | 2024-10-23 05:14:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c3cf916c-a011-3b00-ba71-811dd07f8bf9 | -2.76122 | -49.3126 | 2024-10-23 05:14:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 63835f2a-d935-324d-a10b-1f44582a0ac7 | -2.76074 | -49.31573 | 2024-10-23 05:14:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 34043c17-a3ce-3044-a4ba-94338091b901 | -2.7593 | -49.32507 | 2024-10-23 05:14:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 76f1a7ca-9d48-3439-8337-3c93e5fbabcf | -2.75745 | -49.30239 | 2024-10-23 05:14:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 986671b1-c94b-340c-b33a-9565bb37c4ed | -2.75697 | -49.30552 | 2024-10-23 05:14:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 46101861-403d-3294-8c87-8d2ef9703265 | -2.75696 | -49.3039 | 2024-10-23 05:14:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 81a1dbaa-54d1-38f5-a1bc-cb1e1180e005 | -2.7565 | -49.30703 | 2024-10-23 05:14:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f14a2150-c3e5-32c1-993b-e8036de91d2d | -2.75649 | -49.30865 | 2024-10-23 05:14:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 1baa261b-e78d-3f72-a59a-e296d4da2cc7 | -2.75604 | -49.31017 | 2024-10-23 05:14:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f8622c9f-7e9c-36e1-9d71-a6d13818cef3 | -2.756 | -49.3118 | 2024-10-23 05:14:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 2f0337c1-694a-332e-a018-d7abecc0e70f | -2.75558 | -49.3133 | 2024-10-23 05:14:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| b75eb9fa-4d9f-3950-9621-9167c2a3ea93 | -2.75552 | -49.31493 | 2024-10-23 05:14:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 5a910362-6b88-3700-beac-455735bd039c | -2.75513 | -49.31644 | 2024-10-23 05:14:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 083080e6-0ea2-3791-8d7f-4be1563d46df | -2.75504 | -49.31806 | 2024-10-23 05:14:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 7b4f78cf-93a6-3d67-b863-f82730194dcb | -2.75467 | -49.31956 | 2024-10-23 05:14:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| cb93bb8a-f486-3a03-8504-5305557f28aa | -2.75456 | -49.32117 | 2024-10-23 05:14:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 762d71ad-dd9d-383a-b9bf-8a8c38982986 | -2.75421 | -49.32272 | 2024-10-23 05:14:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 1b922db9-bab2-303b-8f73-965705ff54fe | -2.75408 | -49.32429 | 2024-10-23 05:14:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 8ebd057e-7af3-3635-b030-bab48511826e | -2.75127 | -49.30783 | 2024-10-23 05:14:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 78c71b1f-5784-3826-ab7a-ce4ea7c65ab5 | -2.75079 | -49.31094 | 2024-10-23 05:14:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| a7fac8ad-43d5-3990-8d3a-5b1971b6bc54 | -2.75032 | -49.31403 | 2024-10-23 05:14:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 0188752b-5a4f-329f-b347-920b6c1de681 | -2.74984 | -49.31718 | 2024-10-23 05:14:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| ef338112-6036-3c29-8039-9cb42fd9bf2f | -2.74936 | -49.32032 | 2024-10-23 05:14:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 5adf056b-5abe-35c8-863d-7257b351392e | -3.54731 | -50.30713 | 2024-10-23 05:14:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 700fdd3e-25ec-3324-ad48-057378a46803 | -3.26453 | -50.15481 | 2024-10-23 05:14:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 211d2bc1-04ed-3270-bef3-5553893ea9f9 | -3.26451 | -50.15413 | 2024-10-23 05:14:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 2481d005-ec28-31d2-bf29-c884130d0f87 | -3.25955 | -50.15335 | 2024-10-23 05:14:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 78ca9615-cbad-3417-b8de-8add0aaa762a | -3.25036 | -50.18048 | 2024-10-23 05:14:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 8.4 |
| ca278da2-1710-350d-96b0-a7dc2c37214d | -3.24951 | -50.18608 | 2024-10-23 05:14:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 7.7 |
| deb76929-0081-37f2-9775-029871e69d7c | -3.24626 | -50.17407 | 2024-10-23 05:14:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 8.4 |
| b6953065-35f8-3e1a-8d1e-e9390b7376a5 | -3.2454 | -50.17976 | 2024-10-23 05:14:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 8.4 |
| d53d57ad-bff3-310c-9a6d-5d8653e634b0 | -3.24456 | -50.18534 | 2024-10-23 05:14:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 7.7 |
| 271ab57b-e178-33c3-b310-d6dc4b4d57a6 | -3.24132 | -50.17326 | 2024-10-23 05:14:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 5bd9aaca-710b-3d96-b179-14a96f92ec37 | -3.24046 | -50.17894 | 2024-10-23 05:14:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 6aed840e-c3f3-3974-aef1-2725db43d98e | -3.16511 | -50.3803 | 2024-10-23 05:14:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| e3634eab-cec6-3956-b889-2ac1c9937c71 | -3.16023 | -50.37956 | 2024-10-23 05:14:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| da5197dd-3064-3894-a206-16d4af020ab0 | -3.07429 | -50.5013 | 2024-10-23 05:14:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 511385fc-c321-32ae-a4ae-4105e9840cc6 | -3.07349 | -50.50656 | 2024-10-23 05:14:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 46e0d596-33ae-3c12-81ba-5691cb868737 | -3.06946 | -50.50056 | 2024-10-23 05:14:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 34d63ec7-ace2-35a0-8d6c-8bdff3c15674 | -3.06866 | -50.50582 | 2024-10-23 05:14:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 1b300d4f-d469-318a-8e04-977e1e957e55 | -3.03527 | -50.25132 | 2024-10-23 05:14:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 7c6eacf9-624d-3dc7-abd7-dd083f7a5abd | -2.96381 | -50.52487 | 2024-10-23 05:14:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| ce6ae0bb-9815-3586-85b4-52c5ec67c2e5 | -2.95978 | -50.51891 | 2024-10-23 05:14:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| e92fe996-df48-321c-85f0-88df7ab5069d | -2.95899 | -50.52414 | 2024-10-23 05:14:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| d7b3d7a0-8934-31a2-9b41-a338527c60a0 | -2.9582 | -50.52935 | 2024-10-23 05:14:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| c996eeb3-52c0-3efd-95a5-8546cf2ce43f | -2.95497 | -50.51813 | 2024-10-23 05:14:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 1b86dd39-5b7c-394c-8a07-604d89364d6e | -2.95417 | -50.5234 | 2024-10-23 05:14:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 8492203b-6910-3705-b4fc-d35a889490bd | -2.95339 | -50.52863 | 2024-10-23 05:14:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 0534a77b-56c8-3398-981a-50a2894b0de7 | -2.82109 | -50.4963 | 2024-10-23 05:14:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 1479aa37-4404-3b8c-8783-e564b53af654 | -2.7689 | -50.46037 | 2024-10-23 05:14:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| fc59b9f9-1910-3e48-a38f-86a969149c39 | -2.65122 | -49.99201 | 2024-10-23 05:14:00 | NPP-375D | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| eada2b1a-8cf6-36f4-bbec-330e0100eaa0 | -2.64164 | -49.98844 | 2024-10-23 05:14:00 | NPP-375D | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 332e357a-ab7a-36f6-b588-74d91ab861c1 | -2.62174 | -49.98545 | 2024-10-23 05:14:00 | NPP-375D | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| bea833dc-769a-337d-ad76-1205551b7eab | -2.58975 | -49.82359 | 2024-10-23 05:14:00 | NPP-375D | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 6cc1df6a-fb62-3470-a1cb-ddc476d9d94b | -3.22821 | -49.11235 | 2024-10-23 05:14:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 65bb7797-fd64-30b6-a4ec-8251a3a7e44b | -3.22773 | -49.11565 | 2024-10-23 05:14:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 9077aade-e3a1-3eb6-bf2d-33596601621c | -3.22503 | -49.11396 | 2024-10-23 05:14:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 5f400eee-3b36-3013-aacb-10f33b4f9c3d | -3.22453 | -49.11724 | 2024-10-23 05:14:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c6422bf0-94ca-3d1f-839a-780b23f6109b | -3.22288 | -49.11152 | 2024-10-23 05:14:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| ae0a046c-5364-37c7-b947-9e331442e272 | -2.47746 | -49.10394 | 2024-10-23 05:14:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 5b34b3ea-2be1-387e-8b9c-0b4471b4819c | -2.47696 | -49.10713 | 2024-10-23 05:14:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 80af7305-1687-3756-bbb3-b7975ae9b911 | -2.47682 | -49.10373 | 2024-10-23 05:14:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 20c6ba2b-d7e6-35e3-8ea6-3ad88180397e | -2.47634 | -49.10696 | 2024-10-23 05:14:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 62d09b57-a4c7-3ae2-bced-4c26e3831721 | -2.46742 | -49.09908 | 2024-10-23 05:14:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 95113986-661b-3e08-8627-2f507f468e3a | -2.46675 | -49.09887 | 2024-10-23 05:14:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 25ba842f-16af-3a73-9d7b-1c549580109b | -3.79834 | -50.02747 | 2024-10-23 05:14:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| e11b646f-0f0f-3fc7-a760-bec1d6e5f487 | -3.79791 | -50.03036 | 2024-10-23 05:14:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |


[Clique aqui para ver as próximas entradas](README53.md)
