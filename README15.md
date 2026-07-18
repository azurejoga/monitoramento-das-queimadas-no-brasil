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

## Dados Diários - Página 15

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| c5f9673e-307f-3ee1-a70c-12d2e498aa51 | -12.9389 | -56.64739 | 2026-07-18 05:25:00 | NOAA-21 | NOVA MUTUM | MATO GROSSO | Brasil | 5106224 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| fd0ee09c-16a2-3dcb-86ff-1c6d591b9df4 | -18.72777 | -54.2021 | 2026-07-18 05:25:00 | NOAA-21 | FIGUEIRÃO | MATO GROSSO DO SUL | Brasil | 5003900 | 50 | 33 | nan | nan | nan | Cerrado | 14.9 |
| 739e5357-4939-35a8-accb-347d10b4ea7a | -12.45882 | -49.59193 | 2026-07-18 05:25:00 | NOAA-21 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 7a469981-9d91-3ec5-8c25-b1ea020de877 | -18.72707 | -54.20288 | 2026-07-18 05:25:00 | NOAA-21 | FIGUEIRÃO | MATO GROSSO DO SUL | Brasil | 5003900 | 50 | 33 | nan | nan | nan | Cerrado | 13.1 |
| 4630391b-15a2-3ab0-b1b5-5bcc21a3abf9 | -9.91819 | -65.00487 | 2026-07-18 05:25:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 4b74f1e9-5027-308e-a1d3-2889bbbca8cc | -8.12689 | -47.87037 | 2026-07-18 05:25:00 | NOAA-21 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| e2c15182-bae7-309b-8a94-78ca7ed05397 | -12.45185 | -49.59166 | 2026-07-18 05:25:00 | NOAA-21 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 4.5 |
| e242022f-a586-32cd-9ca0-bb856f02b360 | -18.73329 | -54.19978 | 2026-07-18 05:25:00 | NOAA-21 | FIGUEIRÃO | MATO GROSSO DO SUL | Brasil | 5003900 | 50 | 33 | nan | nan | nan | Cerrado | 14.9 |
| 3bc47fee-018a-385a-8ad9-9ab19306a8e8 | -13.99885 | -54.00749 | 2026-07-18 05:25:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 5a26a8b3-566f-38a3-b094-e1e8321da109 | -18.73779 | -54.20157 | 2026-07-18 05:25:00 | NOAA-21 | FIGUEIRÃO | MATO GROSSO DO SUL | Brasil | 5003900 | 50 | 33 | nan | nan | nan | Cerrado | 21.5 |
| ca1a85be-1099-362e-9aa6-d9df2b32f299 | -11.74915 | -57.81601 | 2026-07-18 05:25:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 2346b5f4-b338-32a8-b696-696e9a06699a | -13.98963 | -54.00023 | 2026-07-18 05:25:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| b1471010-9bf8-3ec9-8dc8-1835200ec5eb | -13.98893 | -54.00608 | 2026-07-18 05:25:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 6c988c56-b12f-36cc-8a5d-4ef12d96b7e7 | -18.73225 | -54.20378 | 2026-07-18 05:25:00 | NOAA-21 | FIGUEIRÃO | MATO GROSSO DO SUL | Brasil | 5003900 | 50 | 33 | nan | nan | nan | Cerrado | 13.1 |
| fd6e273c-ed3b-3c6b-81b6-741141c2b75d | -13.99956 | -54.00158 | 2026-07-18 05:25:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| d2ccfd0a-7a97-30a3-aeba-434f20304326 | -18.7319 | -54.20705 | 2026-07-18 05:25:00 | NOAA-21 | FIGUEIRÃO | MATO GROSSO DO SUL | Brasil | 5003900 | 50 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 4d1fdf84-211a-33c2-a19e-85fdf9fc6e4e | -12.45834 | -49.59231 | 2026-07-18 05:25:00 | NOAA-21 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 757f83a8-d371-3723-93e9-df755112d77e | -13.1249 | -52.51413 | 2026-07-18 05:25:00 | NOAA-21 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 7b4976a4-d8e9-3b63-83ba-4b1be523341f | -18.73298 | -54.19721 | 2026-07-18 05:25:00 | NOAA-21 | FIGUEIRÃO | MATO GROSSO DO SUL | Brasil | 5003900 | 50 | 33 | nan | nan | nan | Cerrado | 6.1 |
| f66d48bb-c029-3d9f-8fa4-abe95514e971 | -18.73813 | -54.20417 | 2026-07-18 05:25:00 | NOAA-21 | FIGUEIRÃO | MATO GROSSO DO SUL | Brasil | 5003900 | 50 | 33 | nan | nan | nan | Cerrado | 17.7 |
| 689fa288-7bda-3c46-8d41-9378c78842ce | -18.73847 | -54.20085 | 2026-07-18 05:25:00 | NOAA-21 | FIGUEIRÃO | MATO GROSSO DO SUL | Brasil | 5003900 | 50 | 33 | nan | nan | nan | Cerrado | 17.7 |
| e53b57ea-70fa-3e50-8c77-c1dfe868ce5f | -18.73262 | -54.20636 | 2026-07-18 05:25:00 | NOAA-21 | FIGUEIRÃO | MATO GROSSO DO SUL | Brasil | 5003900 | 50 | 33 | nan | nan | nan | Cerrado | 7.4 |
| e75fa310-96d9-34fb-be50-3db00122bfb2 | -18.73261 | -54.2005 | 2026-07-18 05:25:00 | NOAA-21 | FIGUEIRÃO | MATO GROSSO DO SUL | Brasil | 5003900 | 50 | 33 | nan | nan | nan | Cerrado | 13.1 |
| 0e575fe2-8b2f-3ea4-8ed2-52647fe8b337 | -18.73882 | -54.19749 | 2026-07-18 05:25:00 | NOAA-21 | FIGUEIRÃO | MATO GROSSO DO SUL | Brasil | 5003900 | 50 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 3747f5ff-f366-35c3-a3ff-ba5a969e3d70 | -12.45233 | -49.59128 | 2026-07-18 05:25:00 | NOAA-21 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 75b1e990-ffaf-3d42-818b-f4f07c95a311 | -6.91902 | -51.94273 | 2026-07-18 05:25:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 1a37ee84-e9f8-3843-94ea-8704006440e6 | -14.00381 | -54.00818 | 2026-07-18 05:25:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 18ba7a6a-2e2e-3f8c-af6f-bebfeebff912 | -6.1321 | -55.81191 | 2026-07-18 05:25:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 673cfdee-c443-3da1-846d-868de4d76572 | -18.73742 | -54.20488 | 2026-07-18 05:25:00 | NOAA-21 | FIGUEIRÃO | MATO GROSSO DO SUL | Brasil | 5003900 | 50 | 33 | nan | nan | nan | Cerrado | 21.5 |
| 2a713ead-94f0-323c-9b3c-564d834ac2ba | -10.0156 | -65.05135 | 2026-07-18 05:25:00 | NOAA-21 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 6eb9448e-7587-3bf9-bacb-564c8f4dc6f6 | -18.73779 | -54.20747 | 2026-07-18 05:25:00 | NOAA-21 | FIGUEIRÃO | MATO GROSSO DO SUL | Brasil | 5003900 | 50 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 4ce37959-ad15-3f0a-b07f-52f9fb79659e | -18.73815 | -54.19824 | 2026-07-18 05:25:00 | NOAA-21 | FIGUEIRÃO | MATO GROSSO DO SUL | Brasil | 5003900 | 50 | 33 | nan | nan | nan | Cerrado | 6.5 |
| a6fe7db4-4e42-33d5-b78d-6bab325d609a | -18.73295 | -54.20308 | 2026-07-18 05:25:00 | NOAA-21 | FIGUEIRÃO | MATO GROSSO DO SUL | Brasil | 5003900 | 50 | 33 | nan | nan | nan | Cerrado | 14.9 |
| f64f2803-609b-35a1-bd2c-e688ff393fe5 | -14.00453 | -54.0022 | 2026-07-18 05:25:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| ae55284e-1f1a-3dc9-a4a0-4ad2821b4633 | -10.94161 | -68.74705 | 2026-07-18 05:25:00 | NOAA-21 | BRASILÉIA | ACRE | Brasil | 1200104 | 12 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 05b1b6a2-aa6f-306d-9d09-e2c7774ad649 | -8.12615 | -47.87638 | 2026-07-18 05:25:00 | NOAA-21 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 05881121-5367-357b-ae39-faf7ddc5d0b1 | -11.74605 | -57.81082 | 2026-07-18 05:25:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 050f9858-5f2f-3aac-a49f-34083381ce6b | -18.73363 | -54.19647 | 2026-07-18 05:25:00 | NOAA-21 | FIGUEIRÃO | MATO GROSSO DO SUL | Brasil | 5003900 | 50 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 49b77f4e-2842-3c66-83f2-5e7cae615263 | -6.91857 | -51.94591 | 2026-07-18 05:25:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 590a479c-5238-3d34-a2ce-e82e862f5b79 | -11.7423 | -57.81025 | 2026-07-18 05:25:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| ddd52b32-8afb-30e2-bb79-16addd816400 | -15.64036 | -58.07986 | 2026-07-18 05:25:00 | NOAA-21 | MIRASSOL D'OESTE | MATO GROSSO | Brasil | 5105622 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a41491da-f96f-3da4-8878-089f5ee0152b | -19.81231 | -57.93822 | 2026-07-18 05:27:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 4.2 |
| fd849a90-23fe-31b1-9fad-e5d437636dc9 | -22.25694 | -52.87288 | 2026-07-18 05:27:00 | NOAA-21 | ANAURILÂNDIA | MATO GROSSO DO SUL | Brasil | 5000807 | 50 | 33 | nan | nan | nan | Mata Atlântica | 2.3 |
| f3d149a5-b2a2-3cca-9b04-d496636b75d5 | -19.81278 | -57.93427 | 2026-07-18 05:27:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 4.2 |
| 6f6949f3-eb00-3931-99ef-693edb2fb55b | -22.24721 | -52.87116 | 2026-07-18 05:27:00 | NOAA-21 | ANAURILÂNDIA | MATO GROSSO DO SUL | Brasil | 5000807 | 50 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| e842027a-05ac-307f-8976-e75ddb2b4445 | -19.81693 | -57.93486 | 2026-07-18 05:27:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 4.2 |
| 5d1e5787-2cf5-3c4d-baba-bce5fe09f874 | -22.28191 | -56.07386 | 2026-07-18 05:27:00 | NOAA-21 | ANTÔNIO JOÃO | MATO GROSSO DO SUL | Brasil | 5000906 | 50 | 33 | nan | nan | nan | Cerrado | 4.3 |
| afb93c40-87e4-38f7-b061-21f3a7fd50e4 | -19.82633 | -57.99624 | 2026-07-18 05:27:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.8 |
| 83fb1aed-7f8f-37f9-a511-6e91760c72e3 | -20.77491 | -57.9412 | 2026-07-18 05:27:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.0 |
| 729286c9-6788-39b5-8c69-063dd2e5fe8f | -22.25101 | -52.87236 | 2026-07-18 05:27:00 | NOAA-21 | ANAURILÂNDIA | MATO GROSSO DO SUL | Brasil | 5000807 | 50 | 33 | nan | nan | nan | Mata Atlântica | 2.3 |
| caf6d156-e9ec-3035-b453-86bd22c06730 | -19.82268 | -57.99174 | 2026-07-18 05:27:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.8 |
| 4bf6ab78-3a94-35f4-85f4-a750ede59274 | -20.77539 | -57.93712 | 2026-07-18 05:27:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.5 |
| 4e918729-0dcc-32f7-8f37-7177c730a4cf | -22.2514 | -52.8676 | 2026-07-18 05:27:00 | NOAA-21 | ANAURILÂNDIA | MATO GROSSO DO SUL | Brasil | 5000807 | 50 | 33 | nan | nan | nan | Mata Atlântica | 2.4 |
| 8b9d0e3a-8548-34f3-9a58-d3e8255be8aa | -19.82154 | -57.9315 | 2026-07-18 05:27:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.2 |
| 64a6f7db-e26d-31bb-b627-6e987083a465 | -19.87296 | -57.9589 | 2026-07-18 05:27:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.9 |
| cdeffbe2-c731-3690-a2c3-cabb38da27c8 | -22.2468 | -52.87582 | 2026-07-18 05:27:00 | NOAA-21 | ANAURILÂNDIA | MATO GROSSO DO SUL | Brasil | 5000807 | 50 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| 6e30e64c-7849-3e6b-b451-a4cf2ec1af9e | -19.81124 | -57.98212 | 2026-07-18 05:27:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.6 |
| f1b99d94-8258-367e-9fe3-851865505a79 | -20.78474 | -57.93011 | 2026-07-18 05:27:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 10.0 |
| de1230fd-133d-3493-84a1-6bb57edaffa8 | -21.7724 | -56.3023 | 2026-07-18 05:27:00 | NOAA-21 | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 4.4 |
| ea90905f-01b1-31f8-832d-84f033f9a85e | -22.25273 | -52.87632 | 2026-07-18 05:27:00 | NOAA-21 | ANAURILÂNDIA | MATO GROSSO DO SUL | Brasil | 5000807 | 50 | 33 | nan | nan | nan | Mata Atlântica | 2.6 |
| 4aa137f5-3232-3352-a556-499184a990c9 | -19.83046 | -57.99683 | 2026-07-18 05:27:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.4 |
| dcf65c9a-3852-3db5-912b-286d0bc92ac6 | -20.77958 | -57.93771 | 2026-07-18 05:27:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.7 |
| 0c44c4f8-5e82-3c8d-91f2-a39d6fe41c70 | -21.66688 | -56.33494 | 2026-07-18 05:27:00 | NOAA-21 | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 1.8 |
| c9e65616-2e4e-3459-ac2a-9182a976db92 | -19.8174 | -57.9309 | 2026-07-18 05:27:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 8.4 |
| 2fe3cdc7-26e6-35ad-a5a6-34f661498aa4 | -22.25356 | -52.8669 | 2026-07-18 05:27:00 | NOAA-21 | ANAURILÂNDIA | MATO GROSSO DO SUL | Brasil | 5000807 | 50 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| 5c9c6cba-3a90-322e-945b-b577434c8938 | -19.81171 | -57.9782 | 2026-07-18 05:27:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.5 |
| 734fedee-e54e-3f19-906a-7ef527992a9f | -19.83458 | -57.99742 | 2026-07-18 05:27:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.4 |
| 9f43638a-7ed1-31b7-b1b7-ad5908f4d33e | -19.81903 | -57.98723 | 2026-07-18 05:27:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.3 |
| 35d8d7f2-70d3-36e7-ae90-6f22c21cd890 | -19.86931 | -57.95437 | 2026-07-18 05:27:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 4.4 |
| 5bd407c8-6843-3b26-bf8b-c84219a72750 | -19.82681 | -57.99233 | 2026-07-18 05:27:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.8 |
| 94c9b048-5fba-306c-b599-b6d07086635e | -22.28272 | -56.07404 | 2026-07-18 05:27:00 | NOAA-21 | ANTÔNIO JOÃO | MATO GROSSO DO SUL | Brasil | 5000906 | 50 | 33 | nan | nan | nan | Cerrado | 4.8 |
| d5ec3943-ffbc-3a68-bcdf-d0b7705d7f2c | -19.82202 | -57.92754 | 2026-07-18 05:27:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.2 |
| 4b5419ad-9182-3b60-96fd-5ea8791a323c | -22.25063 | -52.87701 | 2026-07-18 05:27:00 | NOAA-21 | ANAURILÂNDIA | MATO GROSSO DO SUL | Brasil | 5000807 | 50 | 33 | nan | nan | nan | Mata Atlântica | 2.3 |
| 4f36a973-8308-30bd-b7ad-04349ce41eb2 | -20.77424 | -57.9391 | 2026-07-18 05:27:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.6 |
| fcf0b8f8-7758-3ef4-9497-740ac9c8e6bc | -22.25314 | -52.87167 | 2026-07-18 05:27:00 | NOAA-21 | ANAURILÂNDIA | MATO GROSSO DO SUL | Brasil | 5000807 | 50 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| 24303e81-927d-320b-9682-62efbf9ea3ef | -29.07529 | -50.72523 | 2026-07-18 05:29:00 | NOAA-21 | SÃO FRANCISCO DE PAULA | RIO GRANDE DO SUL | Brasil | 4318200 | 43 | 33 | nan | nan | nan | Mata Atlântica | 4.2 |
| 5fcb086f-f2ac-3a68-a8ef-872f812e13c4 | -29.07845 | -50.72179 | 2026-07-18 05:29:00 | NOAA-21 | SÃO FRANCISCO DE PAULA | RIO GRANDE DO SUL | Brasil | 4318200 | 43 | 33 | nan | nan | nan | Mata Atlântica | 3.2 |
| 464a8f76-b370-36b9-b2c7-fd4fecde4b7c | -31.12695 | -54.40393 | 2026-07-18 05:29:00 | NOAA-21 | DOM PEDRITO | RIO GRANDE DO SUL | Brasil | 4306601 | 43 | 33 | nan | nan | nan | Pampa | 2.5 |
| 2caa2712-f4bf-3126-aba6-49ac4ecb6128 | -31.12666 | -54.40874 | 2026-07-18 05:29:00 | NOAA-21 | DOM PEDRITO | RIO GRANDE DO SUL | Brasil | 4306601 | 43 | 33 | nan | nan | nan | Pampa | 2.5 |
| 1941bdfa-c7d6-3f57-ad38-bf66425e0dd6 | -31.13284 | -54.40455 | 2026-07-18 05:29:00 | NOAA-21 | DOM PEDRITO | RIO GRANDE DO SUL | Brasil | 4306601 | 43 | 33 | nan | nan | nan | Pampa | 1.1 |
| b9dea273-1332-397a-b18e-fd84e76f88de | -31.13256 | -54.40931 | 2026-07-18 05:29:00 | NOAA-21 | DOM PEDRITO | RIO GRANDE DO SUL | Brasil | 4306601 | 43 | 33 | nan | nan | nan | Pampa | 1.1 |
| 1c5c3e2a-a301-337d-9449-3917bff4983a | -29.07814 | -50.72903 | 2026-07-18 05:29:00 | NOAA-21 | SÃO FRANCISCO DE PAULA | RIO GRANDE DO SUL | Brasil | 4318200 | 43 | 33 | nan | nan | nan | Mata Atlântica | 3.3 |
| a3a76a44-1f47-325c-8c57-a54120b8e48a | -13.3023 | -45.1511 | 2026-07-18 05:30:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 147.8 |
| 59c00cab-a2d5-3c55-9bbe-38d603c34443 | -18.7364 | -54.1988 | 2026-07-18 05:30:00 | GOES-19 | FIGUEIRÃO | MATO GROSSO DO SUL | Brasil | 5003900 | 50 | 33 | nan | nan | nan | Cerrado | 59.9 |
| 6077c6b1-e58b-3da4-a597-61fdd91c7b0e | -22.4687 | -43.0843 | 2026-07-18 05:30:00 | GOES-19 | PETRÓPOLIS | RIO DE JANEIRO | Brasil | 3303906 | 33 | 33 | nan | nan | nan | Mata Atlântica | 55.6 |
| 14fdf0c9-d77f-3f85-a224-718e53e79dca | -13.3028 | -45.1278 | 2026-07-18 05:30:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 107.4 |
| d8142ece-7b60-3676-8a80-58b7450fbfaf | -13.3221 | -45.1246 | 2026-07-18 05:30:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 303.0 |
| 1825c2a9-1ae1-3bcf-8c5b-8d818dc8e2ff | -13.3217 | -45.1479 | 2026-07-18 05:30:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 433.1 |
| a4ead5be-03e0-3329-a431-18b4dbfb566d | -22.4687 | -43.0843 | 2026-07-18 05:40:00 | GOES-19 | PETRÓPOLIS | RIO DE JANEIRO | Brasil | 3303906 | 33 | 33 | nan | nan | nan | Mata Atlântica | 58.1 |
| 774d112e-dfef-31a0-87f6-1dfbefe5398f | -13.3023 | -45.1511 | 2026-07-18 05:40:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 166.7 |
| 3182c227-40ac-3817-94d0-f11be1565656 | -13.3221 | -45.1246 | 2026-07-18 05:40:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 274.1 |
| 8a6bee42-610f-3793-9b71-64990e6009a2 | -13.3028 | -45.1278 | 2026-07-18 05:40:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 133.1 |
| ef0bd588-0167-3ecb-9ac1-d99ecd44c9dd | -13.3217 | -45.1479 | 2026-07-18 05:40:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 346.9 |
| da1b1297-dc45-3a78-b7de-a96c838bfb92 | -18.7364 | -54.1988 | 2026-07-18 05:40:00 | GOES-19 | FIGUEIRÃO | MATO GROSSO DO SUL | Brasil | 5003900 | 50 | 33 | nan | nan | nan | Cerrado | 57.6 |
| af341f62-b785-3aa1-8c6c-588b6fd74c9e | -20.0252 | -57.9468 | 2026-07-18 05:40:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 60.5 |
| aa2fc539-bcf3-3570-bef9-b9d9717bcf7a | -13.3023 | -45.1511 | 2026-07-18 05:50:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 146.2 |
| 48f83804-34c1-3dbf-98e9-86df3621cdbd | -13.3221 | -45.1246 | 2026-07-18 05:50:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 199.1 |
| 66ffb77f-37b2-3769-b295-6c1dc3d05d7c | -13.3217 | -45.1479 | 2026-07-18 05:50:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 223.3 |
| f9f2a3df-b476-3fb0-b002-34c2794403b6 | -13.3028 | -45.1278 | 2026-07-18 05:50:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 132.6 |
| 1a7bbdd5-8857-346d-87fc-c52e66a8a9c9 | -18.7364 | -54.1988 | 2026-07-18 05:50:00 | GOES-19 | FIGUEIRÃO | MATO GROSSO DO SUL | Brasil | 5003900 | 50 | 33 | nan | nan | nan | Cerrado | 67.7 |


[Clique aqui para ver as próximas entradas](README16.md)
