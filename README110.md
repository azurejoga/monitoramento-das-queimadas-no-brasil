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

## Dados Diários - Página 110

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 066cf10d-52bc-3c54-9576-253c0cd8c147 | -18.65547 | -57.33065 | 2024-10-24 05:25:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.3 |
| 9ff7dd81-9c33-3e81-b55b-95f83796ed2b | -18.65496 | -57.33481 | 2024-10-24 05:25:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.3 |
| b12f7eb9-b2a6-3fc1-9a6c-8ad6333f7143 | -18.65445 | -57.33895 | 2024-10-24 05:25:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.8 |
| e7dd879f-2a00-3246-a05c-92d1a0fd1ef4 | -18.6502 | -57.33837 | 2024-10-24 05:25:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.8 |
| ab9af368-65d0-395a-9813-915ec1e451ba | -1.5878 | -53.3089 | 2024-10-24 05:25:15 | GOES-16 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 53.5 |
| d0e25da0-dca9-3f94-bc1d-72c51b8d9d5e | -2.9763 | -50.4193 | 2024-10-24 05:25:23 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 42.6 |
| dc5c78ed-8ba6-34db-b949-b9d19a2300f8 | -3.9396 | -46.4229 | 2024-10-24 05:25:29 | GOES-16 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 82.1 |
| 4b365bb9-728d-3672-8b00-84a6b38e22b0 | -1.5878 | -53.3089 | 2024-10-24 05:35:15 | GOES-16 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 58.2 |
| a8d82b26-ac46-373e-9b51-e49c367eea21 | -3.9396 | -46.4229 | 2024-10-24 05:35:29 | GOES-16 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 76.7 |
| aceab7a0-b380-36ed-a9cb-70ce3726c4ff | -1.5878 | -53.3089 | 2024-10-24 05:45:15 | GOES-16 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 53.7 |
| a01282c2-22cc-3b18-b0e5-045fb7b67179 | -3.1607 | -50.4556 | 2024-10-24 05:45:24 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 51.1 |
| 2febb8a8-7bce-3186-9c4e-751b6dae06a7 | -3.9396 | -46.4229 | 2024-10-24 05:45:29 | GOES-16 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 76.5 |
| d917f720-7731-3292-a97a-18b68ba790f9 | -1.5878 | -53.3089 | 2024-10-24 05:55:15 | GOES-16 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 42.4 |
| 384e0bf8-9361-37e1-a72b-9cf9942c5d9a | -1.5878 | -53.3089 | 2024-10-24 06:05:15 | GOES-16 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 39.6 |
| 1626adff-5438-3bf9-b740-05c903d46169 | 4.82254 | -60.14605 | 2024-10-24 06:12:00 | NOAA-21 | UIRAMUTÃ | RORAIMA | Brasil | 1400704 | 14 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 8e0cddd5-3cba-3b73-9146-7483b8409a05 | 4.82245 | -60.14664 | 2024-10-24 06:12:00 | NOAA-21 | UIRAMUTÃ | RORAIMA | Brasil | 1400704 | 14 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 1cc06efa-7edf-3744-8ff3-df5f83bd2671 | 4.82191 | -60.14235 | 2024-10-24 06:12:00 | NOAA-21 | UIRAMUTÃ | RORAIMA | Brasil | 1400704 | 14 | 33 | nan | nan | nan | Amazônia | 2.0 |
| be330f0f-8052-3a9d-a5e3-750798128d3c | 4.82179 | -60.14292 | 2024-10-24 06:12:00 | NOAA-21 | UIRAMUTÃ | RORAIMA | Brasil | 1400704 | 14 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 7cf29092-a34d-32f4-9afb-7eb43c6bffcf | -0.77064 | -62.88454 | 2024-10-24 06:12:00 | NOAA-21 | BARCELOS | AMAZONAS | Brasil | 1300409 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 103ae892-ec92-38f6-8acf-0bf590cdbb36 | -8.20833 | -64.09928 | 2024-10-24 06:14:00 | NOAA-21 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| eebf962f-4422-32cd-98a4-121c0af9fef0 | -8.20456 | -64.09705 | 2024-10-24 06:14:00 | NOAA-21 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 20e26e4e-6b36-36a7-9e47-6e087798411d | -8.20336 | -64.09501 | 2024-10-24 06:14:00 | NOAA-21 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| f3c696ec-a0a1-3167-b690-983b51220539 | -8.20288 | -64.09853 | 2024-10-24 06:14:00 | NOAA-21 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 4b454d05-a146-3ee2-a6cc-d87f4181e24a | -7.49528 | -64.60889 | 2024-10-24 06:14:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 44f9f117-ec43-3b06-a8e7-59ecd6cb0c29 | -7.49434 | -64.60947 | 2024-10-24 06:14:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e517a87f-8fdc-3c0b-bac3-9e2518422c72 | -3.33281 | -68.7434 | 2024-10-24 06:14:00 | NOAA-21 | SÃO PAULO DE OLIVENÇA | AMAZONAS | Brasil | 1303908 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| e9c00329-30c1-398d-874a-3ef317d3c4c0 | -3.6646 | -54.26556 | 2024-10-24 06:22:00 | AQUA_M-M | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 22.0 |
| 0480e436-3a7b-3d43-9367-d1c6a972ea89 | -3.60415 | -55.50727 | 2024-10-24 06:22:00 | AQUA_M-M | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 11.0 |
| 48c1871e-404d-37a8-b2e7-8593d1c3e40a | -3.10783 | -54.14528 | 2024-10-24 06:22:00 | AQUA_M-M | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 25.3 |
| 36a713e4-6924-3c66-a34c-25c5c031109b | -3.10472 | -54.167 | 2024-10-24 06:22:00 | AQUA_M-M | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 19.3 |
| 1b722e10-7a9d-3159-9fa3-1290bb459461 | -3.09455 | -54.14353 | 2024-10-24 06:22:00 | AQUA_M-M | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 14.5 |
| c78b5db6-e8fd-392a-be8c-e2a73983624b | -3.07703 | -53.82078 | 2024-10-24 06:22:00 | AQUA_M-M | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 13.9 |
| c751505a-6769-32a5-b768-c64959c40911 | -3.07319 | -53.2394 | 2024-10-24 06:22:00 | AQUA_M-M | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 17.0 |
| 89aebb37-598a-31c9-be2c-40c4bc990992 | -3.06931 | -53.23399 | 2024-10-24 06:22:00 | AQUA_M-M | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 20.7 |
| 089fcc7f-d7e8-39e4-bc9a-6b2fe857e575 | -3.06342 | -53.8189 | 2024-10-24 06:22:00 | AQUA_M-M | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 13.1 |
| d9e742ae-b357-3089-a617-003beaedeae0 | -17.25188 | -57.2433 | 2024-10-24 06:25:00 | AQUA_M-M | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 15.1 |
| b0c8dc89-60de-3238-9384-6508ce635ee6 | -17.2417 | -57.23516 | 2024-10-24 06:25:00 | AQUA_M-M | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 25.3 |
| 7f8a4f96-57ae-33ea-97f8-6aec3a7ed008 | -17.22299 | -57.50573 | 2024-10-24 06:25:00 | AQUA_M-M | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 22.2 |
| a357bb90-85ae-3bed-a00d-17fbfc2e2eb3 | -17.22212 | -57.51253 | 2024-10-24 06:25:00 | AQUA_M-M | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 24.9 |
| 226405aa-8e4f-35ff-bc80-edd7e1f809d9 | -17.0574 | -57.47319 | 2024-10-24 06:25:00 | AQUA_M-M | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 15.6 |
| 991c4799-e008-32ee-ad7f-ead627779013 | -17.01908 | -57.46854 | 2024-10-24 06:25:00 | AQUA_M-M | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 28.1 |
| c8f37ef7-343b-3d96-bb3e-b7102c871053 | -17.0181 | -57.36515 | 2024-10-24 06:25:00 | AQUA_M-M | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 10.9 |
| 1323f50d-9d5b-3e4b-bed8-1589a88377a6 | -17.01673 | -57.48868 | 2024-10-24 06:25:00 | AQUA_M-M | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 43.8 |
| 1615f733-6d0a-3fdf-9ed5-602b042ce931 | -17.01438 | -57.50875 | 2024-10-24 06:25:00 | AQUA_M-M | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 50.8 |
| 3fa47c70-ab12-3869-a04c-6f8145df919d | -23.82738 | -55.27861 | 2024-10-24 06:27:00 | AQUA_M-M | PARANHOS | MATO GROSSO DO SUL | Brasil | 5006358 | 50 | 33 | nan | nan | nan | Mata Atlântica | 55.6 |
| 2b18553e-e431-3181-bdec-9f777cf66feb | -19.70911 | -56.72281 | 2024-10-24 06:27:00 | AQUA_M-M | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 17.7 |
| 0df3a73d-b39a-3ea6-bff5-8c3c6eeb6a17 | -19.66039 | -56.73585 | 2024-10-24 06:27:00 | AQUA_M-M | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 20.1 |
| 9f001cb2-e5bd-3e0d-a948-d401e1a4d8da | -19.65768 | -56.76127 | 2024-10-24 06:27:00 | AQUA_M-M | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 50.1 |
| 4c0472b3-3a4a-3af9-a982-37d04dc7e58c | -19.64961 | -56.83684 | 2024-10-24 06:27:00 | AQUA_M-M | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 25.8 |
| 6e4155c7-c625-367a-8b02-d9659bb283d7 | -19.649 | -56.70875 | 2024-10-24 06:27:00 | AQUA_M-M | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 34.4 |
| 69453912-6b4a-3fd4-9a24-a6ac03cb8d48 | -19.64631 | -56.73428 | 2024-10-24 06:27:00 | AQUA_M-M | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 143.9 |
| 86a063f4-4874-3ac6-bff9-89a47f9beae4 | -19.64363 | -56.75971 | 2024-10-24 06:27:00 | AQUA_M-M | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 68.4 |
| 6b1fcb3d-d3fb-3780-bb4a-739027e065c1 | -19.63564 | -56.83527 | 2024-10-24 06:27:00 | AQUA_M-M | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 33.9 |
| aa8b102d-2e1b-33c2-b5e8-ab685185666b | -19.63224 | -56.73272 | 2024-10-24 06:27:00 | AQUA_M-M | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 86.3 |
| e92edf0c-1d45-3300-982d-25f7e40675aa | -19.57617 | -56.66954 | 2024-10-24 06:27:00 | AQUA_M-M | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 83.1 |
| 117666e4-b7ae-3d58-8074-a71ee6da69c9 | -19.57344 | -56.69518 | 2024-10-24 06:27:00 | AQUA_M-M | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 40.6 |
| 416852dd-445c-3172-8946-1067e271df0a | -19.56204 | -56.66796 | 2024-10-24 06:27:00 | AQUA_M-M | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 93.1 |
| 117c7c8f-ddde-3638-9ded-7df0e3d24e59 | -19.55934 | -56.69361 | 2024-10-24 06:27:00 | AQUA_M-M | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 34.0 |
| 1282c1a3-8ba9-35aa-bfd0-3ed0c0fe7536 | -19.55329 | -56.61474 | 2024-10-24 06:27:00 | AQUA_M-M | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 31.1 |
| 4a5d6337-c994-3d3a-84bd-901b06a21ef9 | -19.54792 | -56.66638 | 2024-10-24 06:27:00 | AQUA_M-M | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 45.8 |
| e853bcd1-e4c7-30a7-b4b2-6f6c60a99a57 | -19.54524 | -56.69202 | 2024-10-24 06:27:00 | AQUA_M-M | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 30.6 |
| f3a59d6a-2a29-3bca-97a1-9161c8ffe29e | -19.53379 | -56.66479 | 2024-10-24 06:27:00 | AQUA_M-M | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 73.3 |
| 83a2c618-e870-31cf-8d45-5734b238f51e | -19.53115 | -56.69043 | 2024-10-24 06:27:00 | AQUA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 59.4 |
| 75671f3e-9a78-3138-8016-9ea7fc26f657 | -19.53026 | -56.65718 | 2024-10-24 06:27:00 | AQUA_M-M | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 43.2 |
| 45b7644a-2d7e-3ea2-a131-e51eec1117bf | -19.52744 | -56.6828 | 2024-10-24 06:27:00 | AQUA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 51.1 |
| 9cdbdbf7-4b7c-3ab9-b073-49ef3e3fa5c5 | -19.50553 | -56.66162 | 2024-10-24 06:27:00 | AQUA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 28.2 |
| 1e8745f4-5653-33fe-92ab-c7495d4b9016 | -19.50476 | -56.62835 | 2024-10-24 06:27:00 | AQUA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 37.4 |
| 5da65a96-2fbd-390b-bc1d-7420113dcecb | -19.50199 | -56.65408 | 2024-10-24 06:27:00 | AQUA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 77.4 |
| 0026a27d-5cfa-30e1-a15f-7885b3eec22d | -19.49397 | -56.63426 | 2024-10-24 06:27:00 | AQUA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 54.2 |
| ee46efb0-01f8-3a89-82d1-278da33aaa92 | -19.49141 | -56.66002 | 2024-10-24 06:27:00 | AQUA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 40.2 |
| 6ea233f8-dfe2-3886-8cb2-b264f5eb182d | -19.48786 | -56.65251 | 2024-10-24 06:27:00 | AQUA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 16.8 |
| 676c6e00-dd2b-324d-8dcc-cbbf78e25d5a | -18.65796 | -57.34938 | 2024-10-24 06:27:00 | AQUA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 17.6 |
| 08feacb2-1bce-35bc-8ea6-3c7809e8ccda | -18.30982 | -56.23117 | 2024-10-24 06:27:00 | AQUA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 24.3 |
| f9138578-2bd5-3436-a810-4407c4cd9eb4 | -18.30772 | -56.22352 | 2024-10-24 06:27:00 | AQUA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 37.4 |
| 31266385-4445-3acb-b1e1-be339f07b0e2 | -18.08158 | -57.28318 | 2024-10-24 06:27:00 | AQUA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 14.1 |
| f2c9b02b-9379-3f56-bc6d-84f998c05ce4 | -18.07912 | -57.28804 | 2024-10-24 06:27:00 | AQUA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 22.0 |
| ebb8ae2b-bdd3-39ca-880e-a5977064e723 | -18.07906 | -57.30487 | 2024-10-24 06:27:00 | AQUA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 20.4 |
| 60791498-d36d-3b21-a969-ea89f7da9ccf | -18.07676 | -57.30975 | 2024-10-24 06:27:00 | AQUA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 17.4 |
| 832f0cbe-2bb9-3b44-af27-8f2256c46ada | -17.93215 | -57.21385 | 2024-10-24 06:27:00 | AQUA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 13.7 |
| 9c8343d2-3d24-34d6-962d-b93d59f8c1b7 | -17.91653 | -57.23413 | 2024-10-24 06:27:00 | AQUA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 15.3 |
| 74e2c22a-58da-38e6-958d-e6e93909b677 | -17.7741 | -57.57567 | 2024-10-24 06:27:00 | AQUA_M-M | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 12.0 |
| ac2914e3-d6a0-325f-a3d9-3df6f5b36dd7 | -17.77033 | -57.49176 | 2024-10-24 06:27:00 | AQUA_M-M | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 11.3 |
| a28f220e-032f-35f7-841a-cd3a00b62a9f | -17.75212 | -57.54494 | 2024-10-24 06:27:00 | AQUA_M-M | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 22.6 |
| bdcc4609-ebd8-39d9-a16a-e663b3f242d3 | -17.7077 | -57.47689 | 2024-10-24 06:27:00 | AQUA_M-M | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 18.4 |
| 8c6f1042-3f3f-38ca-9b4a-6c76226b7f92 | -19.6438 | -56.8521 | 2024-10-24 06:56:56 | GOES-16 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 75.2 |
| 8c4e4b41-90de-3dd9-b953-b937b5a06bac | -19.5071 | -56.6619 | 2024-10-24 07:06:55 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 90.9 |
| 1c312d5d-0d8c-3029-a210-ab4e6835354a | -19.5075 | -56.6409 | 2024-10-24 07:06:55 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 73.3 |
| 55ea3a1b-aac4-3e56-bedc-59db2a45f375 | -19.5465 | -56.6983 | 2024-10-24 07:06:56 | GOES-16 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 70.9 |
| b395586d-c446-31de-92d9-702686dea64a | -19.5469 | -56.6773 | 2024-10-24 07:06:56 | GOES-16 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 101.4 |
| 6517270f-b403-359a-8139-d836780278e7 | -19.5666 | -56.6954 | 2024-10-24 07:06:56 | GOES-16 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 111.0 |
| bd13c6ec-41f3-3b16-a660-226ac30636ee | -19.5669 | -56.6744 | 2024-10-24 07:06:56 | GOES-16 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 123.3 |
| 7e993008-d5ce-3bd3-a3a3-89bb302bb0ba | -19.6438 | -56.8521 | 2024-10-24 07:06:56 | GOES-16 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 67.5 |
| 22485030-c1e3-3b29-a64d-aa0af6be1f93 | -19.6453 | -56.7681 | 2024-10-24 07:06:56 | GOES-16 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 78.2 |
| bb2daa44-1f2c-3264-a0fc-7bc6a9a81afc | -19.6457 | -56.7471 | 2024-10-24 07:06:56 | GOES-16 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 130.4 |
| fe323d8e-1482-3e80-b853-ce59f6fbf6c9 | -19.6461 | -56.7261 | 2024-10-24 07:06:56 | GOES-16 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 88.1 |
| 2a6420da-20fe-31ab-b2e3-ace620258712 | -19.6655 | -56.7653 | 2024-10-24 07:06:56 | GOES-16 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 75.4 |
| 4431c9a2-1b28-3239-b8b1-95f66ec9fe15 | -19.6658 | -56.7443 | 2024-10-24 07:06:56 | GOES-16 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 72.6 |
| 95d2dd53-8021-330d-96eb-e54a705ffd37 | -19.6662 | -56.7233 | 2024-10-24 07:06:56 | GOES-16 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 61.9 |
| 3581dc20-08f5-32e1-8224-e338c67433e9 | -23.836 | -55.3114 | 2024-10-24 07:07:18 | GOES-16 | PARANHOS | MATO GROSSO DO SUL | Brasil | 5006358 | 50 | 33 | nan | nan | nan | Mata Atlântica | 57.7 |
| 4462cdd6-751b-38e3-a357-e354087d39fe | -16.9596 | -57.5245 | 2024-10-24 07:16:42 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 97.2 |


[Clique aqui para ver as próximas entradas](README111.md)
