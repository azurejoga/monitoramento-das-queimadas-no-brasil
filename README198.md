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

## Dados Diários - Página 198

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 5904fc8a-e4e0-36a5-8d28-0e5320ed7753 | -16.9176 | -57.7131 | 2024-10-02 06:46:41 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 56.5 |
| 915f9ba9-edcd-308e-aa5f-446452d019e4 | -16.9179 | -57.6926 | 2024-10-02 06:46:41 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 59.2 |
| 93e678cc-b528-3382-a253-fd222f261a04 | -17.1288 | -56.7455 | 2024-10-02 06:46:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 65.8 |
| 3bb55c31-4183-3bde-a569-5692bcc06d3f | -17.1091 | -56.7479 | 2024-10-02 06:46:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 109.0 |
| cabc7a9a-4c7b-3daa-b136-542383252261 | -17.1088 | -56.7685 | 2024-10-02 06:46:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 117.4 |
| 5fb92f17-52c3-3bf0-ad9d-b4f2ccc86be9 | -17.0895 | -56.7503 | 2024-10-02 06:46:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 91.2 |
| dc5a095a-34b2-37e1-96c6-e788dc326cfc | -17.0695 | -56.7733 | 2024-10-02 06:46:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 60.1 |
| ceaaa3d0-6f3f-32cc-a165-43da817eb335 | -17.0892 | -56.7709 | 2024-10-02 06:46:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 102.5 |
| 645ac030-3887-3d11-9d12-e50f20d0420f | -22.3505 | -49.306 | 2024-10-02 06:47:09 | GOES-16 | DUARTINA | SÃO PAULO | Brasil | 3514502 | 35 | 33 | nan | nan | nan | Mata Atlântica | 70.6 |
| ee63aa3d-242c-326d-9cb1-ef733bdecd2f | -22.3713 | -49.3011 | 2024-10-02 06:47:09 | GOES-16 | PIRATININGA | SÃO PAULO | Brasil | 3539400 | 35 | 33 | nan | nan | nan | Mata Atlântica | 171.8 |
| 7a174212-995d-32d2-97ee-1c915066964d | -22.372 | -49.2777 | 2024-10-02 06:47:09 | GOES-16 | PIRATININGA | SÃO PAULO | Brasil | 3539400 | 35 | 33 | nan | nan | nan | Mata Atlântica | 140.1 |
| 5f29671d-d80b-3465-9669-3834b9437b00 | -22.3922 | -49.2961 | 2024-10-02 06:47:09 | GOES-16 | PIRATININGA | SÃO PAULO | Brasil | 3539400 | 35 | 33 | nan | nan | nan | Mata Atlântica | 155.0 |
| 4aacc231-06e6-3eb6-824d-c801d9264bdf | -22.3929 | -49.2727 | 2024-10-02 06:47:09 | GOES-16 | PIRATININGA | SÃO PAULO | Brasil | 3539400 | 35 | 33 | nan | nan | nan | Mata Atlântica | 86.6 |
| 5e919367-3559-379f-b884-89ca5ff9dc55 | -10.69687 | -69.39017 | 2024-10-02 06:52:00 | NPP-375D | BRASILÉIA | ACRE | Brasil | 1200104 | 12 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 23e6eba9-54b0-3939-896d-daa60b56c564 | -10.6977 | -69.38837 | 2024-10-02 06:52:00 | NPP-375D | BRASILÉIA | ACRE | Brasil | 1200104 | 12 | 33 | nan | nan | nan | Amazônia | 4.4 |
| d3da1eaa-bf6c-3f2d-b0b2-f786bee8d0fd | -10.69776 | -69.38259 | 2024-10-02 06:52:00 | NPP-375D | BRASILÉIA | ACRE | Brasil | 1200104 | 12 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 986a1d5f-8ae4-333b-bb40-43ba079c42a0 | -10.70507 | -69.38364 | 2024-10-02 06:52:00 | NPP-375D | BRASILÉIA | ACRE | Brasil | 1200104 | 12 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 336d9693-bb52-3167-998f-c8267a118873 | -10.86314 | -69.49803 | 2024-10-02 06:52:00 | NPP-375D | ASSIS BRASIL | ACRE | Brasil | 1200054 | 12 | 33 | nan | nan | nan | Amazônia | 7.0 |
| 21b7f204-d13a-3769-8d20-aeaf2ef579b9 | -10.86401 | -69.50018 | 2024-10-02 06:52:00 | NPP-375D | ASSIS BRASIL | ACRE | Brasil | 1200054 | 12 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 698cf169-a6fc-3143-89d6-e444dbbc6806 | -10.86486 | -69.49236 | 2024-10-02 06:52:00 | NPP-375D | ASSIS BRASIL | ACRE | Brasil | 1200054 | 12 | 33 | nan | nan | nan | Amazônia | 3.4 |
| c675b0c0-a7b0-3b57-9c7b-3ef0974f4ad2 | -7.21627 | -72.32004 | 2024-10-02 06:52:00 | NPP-375D | GUAJARÁ | AMAZONAS | Brasil | 1301654 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 8b7750df-7bf4-3547-ae86-31bc67ddd322 | -7.21684 | -72.31586 | 2024-10-02 06:52:00 | NPP-375D | GUAJARÁ | AMAZONAS | Brasil | 1301654 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 45d80c27-ec91-3214-874c-24e0ad891b98 | -8.06851 | -71.27177 | 2024-10-02 06:52:00 | NPP-375D | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 40e7d64d-9aa3-33e9-a738-d67b5335efde | -8.0742 | -71.27784 | 2024-10-02 06:52:00 | NPP-375D | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 0b2085c5-2d5e-3dc5-bb85-1810e76c81fa | -8.25533 | -71.14894 | 2024-10-02 06:52:00 | NPP-375D | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 5f06ff28-631e-3f84-9dde-581f0baa47b0 | -8.25582 | -71.14899 | 2024-10-02 06:52:00 | NPP-375D | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 1d84fce9-4b6c-3383-908d-83afaf8ec63c | -8.25601 | -71.14375 | 2024-10-02 06:52:00 | NPP-375D | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 032016c0-9be0-3a12-9481-354e31b6728a | -8.25646 | -71.14378 | 2024-10-02 06:52:00 | NPP-375D | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 34997b41-ceee-33ec-901a-b99eafd7389e | -9.9367 | -64.9179 | 2024-10-02 06:56:03 | GOES-16 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 59.9 |
| 45431131-d580-3d9f-a431-1a46c9d41109 | -12.6484 | -63.1214 | 2024-10-02 06:56:18 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 55.2 |
| 1c42ff6a-46d6-3c7a-b724-bf612e5c5d5a | -12.8593 | -62.7826 | 2024-10-02 06:56:19 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 34.6 |
| b45e46bc-d736-342e-828a-502c57f7d4bf | -15.5486 | -56.8873 | 2024-10-02 06:56:34 | GOES-16 | NOSSA SENHORA DO LIVRAMENTO | MATO GROSSO | Brasil | 5106109 | 51 | 33 | nan | nan | nan | Cerrado | 89.7 |
| fffc7938-1cdc-3e0b-a09d-2ba0a96d31ac | -16.9179 | -57.6926 | 2024-10-02 06:56:41 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 61.5 |
| 844fb85b-656c-3b20-96ba-04237f5ffc38 | -16.9176 | -57.7131 | 2024-10-02 06:56:41 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 61.9 |
| 67992eef-ec4d-37be-b3b7-7825a31aef67 | -16.8983 | -57.6949 | 2024-10-02 06:56:41 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 134.8 |
| ebac3637-0dc0-3d87-bc22-b156d90d4135 | -16.8695 | -55.848 | 2024-10-02 06:56:41 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 140.1 |
| 355ff855-0979-35c8-b2cf-bad0391dcaca | -16.8295 | -55.8945 | 2024-10-02 06:56:41 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 68.6 |
| 84066df4-951f-3ae4-baa3-b3653bb2e339 | -16.898 | -57.7153 | 2024-10-02 06:56:41 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 85.2 |
| 241ba091-1224-3fda-90af-488af69e3d34 | -16.8787 | -57.6971 | 2024-10-02 06:56:41 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 65.3 |
| 238f2c47-266b-37c5-9e55-51ce1383ef41 | -16.8894 | -55.8247 | 2024-10-02 06:56:41 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 144.9 |
| 59324f94-e627-3431-93b5-ea16e063b12e | -16.8891 | -55.8455 | 2024-10-02 06:56:41 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 226.5 |
| 49146678-48ea-3d18-bf59-4cbf8412f683 | -16.8698 | -55.8272 | 2024-10-02 06:56:41 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 96.2 |
| 2eb727b2-e2d4-3acb-8d9c-e2b57aeaffae | -16.8292 | -55.9152 | 2024-10-02 06:56:41 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 80.4 |
| aa73e177-8dba-31ec-99d8-58843f7b673c | -17.0892 | -56.7709 | 2024-10-02 06:56:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 90.2 |
| 306270a4-07df-3c07-b37e-3ba38b182b7e | -17.0895 | -56.7503 | 2024-10-02 06:56:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 70.3 |
| 2f12bf95-4b85-3f34-b7a1-57689184cd4d | -17.1088 | -56.7685 | 2024-10-02 06:56:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 134.1 |
| 8cdba80b-febf-3cd0-8189-1057c19be8c6 | -17.1091 | -56.7479 | 2024-10-02 06:56:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 108.5 |
| 8cd4ddfb-77ec-3d6d-b59e-39e91d7dec03 | -22.3929 | -49.2727 | 2024-10-02 06:57:09 | GOES-16 | PIRATININGA | SÃO PAULO | Brasil | 3539400 | 35 | 33 | nan | nan | nan | Mata Atlântica | 76.3 |
| c6ce26b7-a2c6-3fd1-87a3-a9aef81ce032 | -22.3922 | -49.2961 | 2024-10-02 06:57:09 | GOES-16 | PIRATININGA | SÃO PAULO | Brasil | 3539400 | 35 | 33 | nan | nan | nan | Mata Atlântica | 148.8 |
| 610fed0f-60dd-356f-9aed-46b464d5e615 | -22.372 | -49.2777 | 2024-10-02 06:57:09 | GOES-16 | PIRATININGA | SÃO PAULO | Brasil | 3539400 | 35 | 33 | nan | nan | nan | Mata Atlântica | 118.5 |
| 0388a48d-a310-327b-b09a-6ed818d761af | -22.3713 | -49.3011 | 2024-10-02 06:57:09 | GOES-16 | PIRATININGA | SÃO PAULO | Brasil | 3539400 | 35 | 33 | nan | nan | nan | Mata Atlântica | 147.4 |
| 1b535d19-1e2a-3962-8521-ee5c602ecba1 | -22.9006 | -45.1029 | 2024-10-02 06:57:11 | GOES-16 | GUARATINGUETÁ | SÃO PAULO | Brasil | 3518404 | 35 | 33 | nan | nan | nan | Mata Atlântica | 70.7 |
| a86932a1-43e9-33ca-84cb-903396132f6c | -16.59 | -58.26 | 2024-10-02 07:03:51 | MSG-03 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 643599ba-afec-3258-86a3-546bec4ad708 | -12.6484 | -63.1214 | 2024-10-02 07:06:18 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 61.7 |
| 0f6f3120-974b-3945-bafc-3d066871c159 | -12.8593 | -62.7826 | 2024-10-02 07:06:19 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 35.6 |
| ba11793d-1ded-375c-b824-540a31badde0 | -15.5486 | -56.8873 | 2024-10-02 07:06:34 | GOES-16 | NOSSA SENHORA DO LIVRAMENTO | MATO GROSSO | Brasil | 5106109 | 51 | 33 | nan | nan | nan | Cerrado | 101.7 |
| 761d6865-4d6d-305e-bc74-7473be99c9aa | -16.8695 | -55.848 | 2024-10-02 07:06:41 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 217.2 |
| 89d7ed90-41a4-3742-b389-afe06de30cd8 | -16.8891 | -55.8455 | 2024-10-02 07:06:41 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 266.3 |
| fd2800be-5d0c-366e-98cb-89ea718adda1 | -16.8894 | -55.8247 | 2024-10-02 07:06:41 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 172.2 |
| adea73f1-8674-3862-a408-15fd66ef708d | -16.8787 | -57.6971 | 2024-10-02 07:06:41 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 60.2 |
| a2bab5fa-81b6-3d95-988a-65e9e26e0010 | -16.898 | -57.7153 | 2024-10-02 07:06:41 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 102.9 |
| 89b1a0cf-9a7c-3910-a979-a2c0cf039e6e | -16.8983 | -57.6949 | 2024-10-02 07:06:41 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 139.1 |
| 6597e1ad-79cc-31d9-9dd5-707b6b6d77cf | -16.8986 | -57.6744 | 2024-10-02 07:06:41 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 55.7 |
| 77ee1111-45a4-32b9-b4ae-8dba612e042c | -16.9176 | -57.7131 | 2024-10-02 07:06:41 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 63.6 |
| 6c0bd87a-b886-37d3-bf98-8fbd6d977326 | -16.8698 | -55.8272 | 2024-10-02 07:06:41 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 155.6 |
| 1c769774-6a06-38fe-9184-b47829a77437 | -17.0892 | -56.7709 | 2024-10-02 07:06:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 123.4 |
| b2eb8b38-a8c8-3ff1-a17d-066e4c65f83a | -17.1288 | -56.7455 | 2024-10-02 07:06:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 64.4 |
| 0b33973c-8ec1-39d3-8a24-7b6443d53b85 | -17.1091 | -56.7479 | 2024-10-02 07:06:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 105.6 |
| e224e326-122a-317d-9a1d-fd103b5603b0 | -17.1088 | -56.7685 | 2024-10-02 07:06:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 132.2 |
| d7f4a2e7-9906-3b84-b386-0d4131dcc2dc | -17.0895 | -56.7503 | 2024-10-02 07:06:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 82.9 |
| 9b0b798d-c04f-3392-8768-825b3c61ec1f | -22.3922 | -49.2961 | 2024-10-02 07:07:09 | GOES-16 | PIRATININGA | SÃO PAULO | Brasil | 3539400 | 35 | 33 | nan | nan | nan | Mata Atlântica | 135.4 |
| bd783374-a153-3beb-9c5c-a4bc7cb44b7f | -22.3713 | -49.3011 | 2024-10-02 07:07:09 | GOES-16 | PIRATININGA | SÃO PAULO | Brasil | 3539400 | 35 | 33 | nan | nan | nan | Mata Atlântica | 151.3 |
| c2d3b1b2-722e-3496-9b15-294cf3b64eea | -22.372 | -49.2777 | 2024-10-02 07:07:09 | GOES-16 | PIRATININGA | SÃO PAULO | Brasil | 3539400 | 35 | 33 | nan | nan | nan | Mata Atlântica | 104.0 |
| 79f1958a-164e-35e6-b94a-6e2ec7151417 | -22.3929 | -49.2727 | 2024-10-02 07:07:09 | GOES-16 | PIRATININGA | SÃO PAULO | Brasil | 3539400 | 35 | 33 | nan | nan | nan | Mata Atlântica | 86.6 |
| 8228f8bb-3893-3117-aaa2-31c68bbabee8 | -22.7809 | -46.8154 | 2024-10-02 07:07:11 | GOES-16 | AMPARO | SÃO PAULO | Brasil | 3501905 | 35 | 33 | nan | nan | nan | Mata Atlântica | 88.2 |
| b9a8ca71-0b1b-342a-a464-4657f79ef3c1 | -12.6486 | -63.1022 | 2024-10-02 07:16:18 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 43.0 |
| 37f46ef5-1e55-3a47-b644-1ad08c679129 | -12.6484 | -63.1214 | 2024-10-02 07:16:18 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 64.8 |
| db4d3ce4-32d0-398d-9c60-ccbc27f26f67 | -15.5486 | -56.8873 | 2024-10-02 07:16:34 | GOES-16 | NOSSA SENHORA DO LIVRAMENTO | MATO GROSSO | Brasil | 5106109 | 51 | 33 | nan | nan | nan | Cerrado | 98.9 |
| 57d3cc76-fcf0-3204-adda-496cecabb979 | -16.8983 | -57.6949 | 2024-10-02 07:16:41 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 132.9 |
| c5084a77-820c-39dc-a955-f2476e3922ee | -16.8292 | -55.9152 | 2024-10-02 07:16:41 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 81.5 |
| f6234421-85ae-3111-96b0-0690f5d0104f | -16.8295 | -55.8945 | 2024-10-02 07:16:41 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 88.9 |
| 5769bc66-5e16-395a-9d26-7577266e3e33 | -16.8695 | -55.848 | 2024-10-02 07:16:41 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 158.6 |
| 4e074ca8-30a4-31a9-99bf-1327f9c685d9 | -16.8698 | -55.8272 | 2024-10-02 07:16:41 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 118.4 |
| af5e6342-5d67-3f1a-b52b-0cbf22c04273 | -16.8894 | -55.8247 | 2024-10-02 07:16:41 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 194.0 |
| bfa7f112-17ff-3765-9735-49ddb7b63b7f | -16.8891 | -55.8455 | 2024-10-02 07:16:41 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 268.9 |
| 342a2239-587d-3599-9d28-07f1d294e873 | -16.8787 | -57.6971 | 2024-10-02 07:16:41 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 62.5 |
| c59d47f5-d49c-3508-8eed-8721274c3c3f | -16.9176 | -57.7131 | 2024-10-02 07:16:41 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 62.1 |
| 9aa554c4-d657-3503-b3e5-ce4acf05b19e | -16.9179 | -57.6926 | 2024-10-02 07:16:41 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 54.6 |
| 32522d16-aeeb-362a-b840-9bb3bf9b5c27 | -16.898 | -57.7153 | 2024-10-02 07:16:41 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 119.7 |
| 34e2a03c-3eda-32c4-90e2-0418eb932edf | -17.0892 | -56.7709 | 2024-10-02 07:16:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 116.7 |
| 7d604243-cdcf-36df-a3d6-7b3c0bc15925 | -17.0895 | -56.7503 | 2024-10-02 07:16:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 84.6 |
| bfdb2d4d-eb92-3a40-b0af-a3fdbe88fbef | -17.1088 | -56.7685 | 2024-10-02 07:16:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 148.8 |
| f3dafcbd-1d0e-3832-b198-5e9cbe1326cb | -17.1288 | -56.7455 | 2024-10-02 07:16:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 68.4 |
| dfc785fe-6d0d-333a-977e-60188f041d63 | -17.1091 | -56.7479 | 2024-10-02 07:16:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 109.1 |
| c94e81ee-06e7-380d-a180-c7dc4be0b4d8 | -22.3713 | -49.3011 | 2024-10-02 07:17:09 | GOES-16 | PIRATININGA | SÃO PAULO | Brasil | 3539400 | 35 | 33 | nan | nan | nan | Mata Atlântica | 145.1 |
| 7417a2e5-0713-336d-9410-974933ab66a7 | -22.3922 | -49.2961 | 2024-10-02 07:17:09 | GOES-16 | PIRATININGA | SÃO PAULO | Brasil | 3539400 | 35 | 33 | nan | nan | nan | Mata Atlântica | 137.3 |
| fbac54ac-1f3a-35e2-836e-c4a15fb1954e | -22.3929 | -49.2727 | 2024-10-02 07:17:09 | GOES-16 | PIRATININGA | SÃO PAULO | Brasil | 3539400 | 35 | 33 | nan | nan | nan | Mata Atlântica | 82.1 |
| a0cb47bc-ff3d-3756-b02e-dd4b65cb05b2 | -22.372 | -49.2777 | 2024-10-02 07:17:09 | GOES-16 | PIRATININGA | SÃO PAULO | Brasil | 3539400 | 35 | 33 | nan | nan | nan | Mata Atlântica | 102.4 |
| 41e0aeab-0640-369c-bde9-2de895b66f4a | -22.7809 | -46.8154 | 2024-10-02 07:17:11 | GOES-16 | AMPARO | SÃO PAULO | Brasil | 3501905 | 35 | 33 | nan | nan | nan | Mata Atlântica | 79.2 |
| 7fdba57e-f812-33d9-82a4-856282939ddd | -12.6484 | -63.1214 | 2024-10-02 07:26:18 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 60.6 |


[Clique aqui para ver as próximas entradas](README199.md)
