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

## Dados Diários - Página 93

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| bda6a2cd-2ce9-302a-85c7-88cf5f662c75 | -9.75887 | -47.92074 | 2025-08-28 12:34:00 | TERRA_M-T | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 22.7 |
| 5f0f1098-44f4-37ae-960d-d7366dd4bcc7 | -8.19734 | -45.07745 | 2025-08-28 12:34:00 | TERRA_M-T | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 19.2 |
| 7c44ec73-d626-388a-806d-b74c28d75021 | -12.72406 | -48.18899 | 2025-08-28 12:36:00 | TERRA_M-T | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 30.2 |
| 8b040023-8362-3cf2-ab07-cc4c84000dcf | -12.51504 | -47.24636 | 2025-08-28 12:36:00 | TERRA_M-T | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 52.7 |
| 5bb03155-d8df-3667-b4d1-5494210321e2 | -14.33617 | -53.33858 | 2025-08-28 12:36:00 | TERRA_M-T | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 9.0 |
| 1f8df87f-b051-31ed-bd7f-72d0d95aabdd | -13.50199 | -46.8484 | 2025-08-28 12:36:00 | TERRA_M-T | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 19.2 |
| 14e90faa-8606-3dc9-a80f-d165b9bd6762 | -12.31366 | -50.0091 | 2025-08-28 12:36:00 | TERRA_M-T | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 16.2 |
| fa1a80a7-4bb8-33dd-92c2-3932340f02b5 | -18.46331 | -46.91641 | 2025-08-28 12:36:00 | TERRA_M-T | COROMANDEL | MINAS GERAIS | Brasil | 3119302 | 31 | 33 | nan | nan | nan | Cerrado | 16.0 |
| 4c5c0c93-17e1-3ff2-a651-3533920c3758 | -13.04635 | -46.2841 | 2025-08-28 12:36:00 | TERRA_M-T | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 23.3 |
| 3aff7039-0d1c-302a-add6-cf025e4df6e3 | -14.25683 | -48.06024 | 2025-08-28 12:36:00 | TERRA_M-T | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 10.1 |
| ccf2f421-0bb1-31cd-b07f-6c9f86ef503d | -16.48288 | -49.08181 | 2025-08-28 12:36:00 | TERRA_M-T | TEREZÓPOLIS DE GOIÁS | GOIÁS | Brasil | 5221197 | 52 | 33 | nan | nan | nan | Cerrado | 7.9 |
| dcff0cca-03a3-3303-aef7-21066ff9d532 | -13.51524 | -46.93089 | 2025-08-28 12:36:00 | TERRA_M-T | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 31.5 |
| fc366509-20ad-3c0c-a5ff-733b4b6deed0 | -12.82161 | -48.14472 | 2025-08-28 12:36:00 | TERRA_M-T | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 28.8 |
| 370f67c9-fdc6-3f4c-b4f8-c5aee80dc900 | -16.37497 | -43.7833 | 2025-08-28 12:36:00 | TERRA_M-T | MONTES CLAROS | MINAS GERAIS | Brasil | 3143302 | 31 | 33 | nan | nan | nan | Cerrado | 21.8 |
| de0df156-71d1-3748-8819-41a0572ce55e | -15.42234 | -47.60529 | 2025-08-28 12:36:00 | TERRA_M-T | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 9.9 |
| 969a60c5-c94a-3477-b514-b08adceeeb22 | -14.26345 | -53.07748 | 2025-08-28 12:36:00 | TERRA_M-T | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 19.3 |
| bbe39971-5ecd-30cd-bbff-7cf483bb9c4f | -11.22842 | -55.05737 | 2025-08-28 12:36:00 | TERRA_M-T | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 41.4 |
| 2fa5ad53-ee26-3d64-9650-8ede8fbfad74 | -18.25852 | -47.87402 | 2025-08-28 12:36:00 | TERRA_M-T | OUVIDOR | GOIÁS | Brasil | 5215504 | 52 | 33 | nan | nan | nan | Cerrado | 18.1 |
| ca94699f-fbbb-3cc8-a7af-59d69385316f | -12.01192 | -50.65226 | 2025-08-28 12:36:00 | TERRA_M-T | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 9.6 |
| 4af4a483-72a1-364b-8cd1-4affb0f990bf | -13.55312 | -46.89157 | 2025-08-28 12:36:00 | TERRA_M-T | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 45.1 |
| a3477d09-eea2-3e9e-bd81-a09e919a7497 | -13.98324 | -46.33899 | 2025-08-28 12:36:00 | TERRA_M-T | GUARANI DE GOIÁS | GOIÁS | Brasil | 5209408 | 52 | 33 | nan | nan | nan | Cerrado | 33.9 |
| b99d1a2f-4ef1-3f60-b750-9ae02119ff43 | -16.03767 | -47.9967 | 2025-08-28 12:36:00 | TERRA_M-T | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 63.2 |
| 86bcac8c-af3e-3124-b85f-3bbaa5e4a55e | -12.71692 | -48.16327 | 2025-08-28 12:36:00 | TERRA_M-T | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 19.6 |
| 2ef23552-8a43-3d18-8c0a-cbcca66d2b0b | -13.22079 | -46.04592 | 2025-08-28 12:36:00 | TERRA_M-T | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 17.5 |
| 5a25403b-15b6-307a-9f10-6ec24995b362 | -15.63111 | -52.75061 | 2025-08-28 12:36:00 | TERRA_M-T | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 8.2 |
| ef795704-93d9-3a43-8395-c07aee5e5a73 | -13.37548 | -54.56774 | 2025-08-28 12:36:00 | TERRA_M-T | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 14.9 |
| f24b6bb3-e420-375e-a1cd-c69a3fcd9734 | -13.46171 | -46.9882 | 2025-08-28 12:36:00 | TERRA_M-T | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 18.7 |
| 0f807c4c-d5ab-3cc5-86ea-40b4e271bac2 | -16.42476 | -49.9249 | 2025-08-28 12:36:00 | TERRA_M-T | ANICUNS | GOIÁS | Brasil | 5201306 | 52 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 130ed1f5-59ea-3896-b1d9-36e7893f015a | -13.99086 | -46.33435 | 2025-08-28 12:36:00 | TERRA_M-T | GUARANI DE GOIÁS | GOIÁS | Brasil | 5209408 | 52 | 33 | nan | nan | nan | Cerrado | 25.6 |
| 5ac3ff77-4696-3077-add1-f5428677b16e | -14.32059 | -53.25372 | 2025-08-28 12:36:00 | TERRA_M-T | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 8.4 |
| 81bad24a-bc1d-3a2a-bd1b-df2c6158947a | -14.31301 | -53.24303 | 2025-08-28 12:36:00 | TERRA_M-T | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 21.6 |
| e217888c-50e3-3b78-afa5-b2f3b410cffe | -12.38906 | -45.03864 | 2025-08-28 12:36:00 | TERRA_M-T | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 33.0 |
| 0f5b4a04-133f-3cdc-981a-a4ae95c621cb | -12.87444 | -48.11951 | 2025-08-28 12:36:00 | TERRA_M-T | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 54.9 |
| a5979db7-64c0-34c6-b5e3-2fd48878bb4d | -13.99528 | -46.34127 | 2025-08-28 12:36:00 | TERRA_M-T | GUARANI DE GOIÁS | GOIÁS | Brasil | 5209408 | 52 | 33 | nan | nan | nan | Cerrado | 11.7 |
| e5f442eb-9f79-3393-bd42-f5951c04d746 | -19.32091 | -44.94226 | 2025-08-28 12:36:00 | TERRA_M-T | POMPÉU | MINAS GERAIS | Brasil | 3152006 | 31 | 33 | nan | nan | nan | Cerrado | 58.4 |
| cb7bd014-da8e-3115-947a-49a5525d944b | -13.52681 | -46.93167 | 2025-08-28 12:36:00 | TERRA_M-T | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 30.8 |
| 2005dafb-5ac6-3a77-8d8a-b215bcb1edf5 | -15.19973 | -53.79514 | 2025-08-28 12:36:00 | TERRA_M-T | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | 25.7 |
| 6dac5ab5-5bd4-3f50-8358-75606bba34b6 | -16.03592 | -48.01091 | 2025-08-28 12:36:00 | TERRA_M-T | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 13.1 |
| 189bf5f7-d8e6-3f32-b651-9f296b694224 | -13.00606 | -56.91783 | 2025-08-28 12:36:00 | TERRA_M-T | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 16.0 |
| 37b55216-2350-35f2-8a6a-f71386e3c7f3 | -13.08177 | -46.34468 | 2025-08-28 12:36:00 | TERRA_M-T | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 55.9 |
| abef16dc-041e-32d1-ac3f-024b0ea0257a | -12.50579 | -47.23053 | 2025-08-28 12:36:00 | TERRA_M-T | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 21.3 |
| 6daac044-b52c-39b0-a7d8-fa97b8febb78 | -13.55121 | -46.90758 | 2025-08-28 12:36:00 | TERRA_M-T | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 23.7 |
| b81be964-2fce-3b27-b39f-fc2db8be5c8a | -16.53919 | -43.51769 | 2025-08-28 12:36:00 | TERRA_M-T | FRANCISCO SÁ | MINAS GERAIS | Brasil | 3126703 | 31 | 33 | nan | nan | nan | Cerrado | 29.2 |
| c5d14f96-f975-3591-a831-cc6b166f5c31 | -12.68279 | -48.18381 | 2025-08-28 12:36:00 | TERRA_M-T | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 20.6 |
| 996cec5c-edb2-3b35-81de-b39d052b25fb | -13.43123 | -46.96383 | 2025-08-28 12:36:00 | TERRA_M-T | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 19.1 |
| 9eccdf38-9d2a-397e-990a-99dd81345b44 | -12.39165 | -45.01724 | 2025-08-28 12:36:00 | TERRA_M-T | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 23.4 |
| fa632f58-11ff-335b-a4df-42dabcf5dac3 | -18.45871 | -46.92915 | 2025-08-28 12:36:00 | TERRA_M-T | COROMANDEL | MINAS GERAIS | Brasil | 3119302 | 31 | 33 | nan | nan | nan | Cerrado | 66.4 |
| 3eda2177-6065-30e9-be4c-9021278141bc | -15.19829 | -53.80467 | 2025-08-28 12:36:00 | TERRA_M-T | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | 54.8 |
| bfacc95b-ad54-3053-90ef-f17861c01c6b | -14.33559 | -48.64459 | 2025-08-28 12:36:00 | TERRA_M-T | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 17.9 |
| c651172d-2420-339d-8c1e-bd3ff823f301 | -11.13884 | -54.32043 | 2025-08-28 12:36:00 | TERRA_M-T | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 42.0 |
| a25bd18a-5ffb-386a-81d3-aa864bd0dbf6 | -15.68119 | -47.63913 | 2025-08-28 12:36:00 | TERRA_M-T | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 9.6 |
| 32d01035-0657-3796-9229-3b8627796f1e | -12.6725 | -48.18229 | 2025-08-28 12:36:00 | TERRA_M-T | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 13.5 |
| 590048a8-4542-3a30-9c91-30f0953b1ea5 | -15.68421 | -52.75863 | 2025-08-28 12:36:00 | TERRA_M-T | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 8ffcb417-7e2e-376a-88e4-70daf87d0188 | -14.33117 | -51.90959 | 2025-08-28 12:36:00 | TERRA_M-T | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 20.5 |
| 53b3e80e-1d39-3005-89d6-427a3c10f11f | -16.04868 | -47.99791 | 2025-08-28 12:36:00 | TERRA_M-T | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 8.9 |
| 0f95773e-205b-358a-9d59-0e80845c460e | -11.14052 | -54.30964 | 2025-08-28 12:36:00 | TERRA_M-T | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 25.5 |
| ccfa2f77-a813-36a6-8f1f-b30112d5d6b7 | -15.01817 | -48.1804 | 2025-08-28 12:36:00 | TERRA_M-T | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 11.0 |
| f93fc771-71f6-3df8-8040-3f25743cf7ff | -14.25853 | -48.04665 | 2025-08-28 12:36:00 | TERRA_M-T | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 8.9 |
| 2be55b64-eb2e-3fc7-b243-a5e379443279 | -14.2648 | -53.06825 | 2025-08-28 12:36:00 | TERRA_M-T | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 12.7 |
| cb340d0e-6e12-3c1c-b307-600b358ea32c | -13.3173 | -45.21701 | 2025-08-28 12:36:00 | TERRA_M-T | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 25.7 |
| 88c6cde0-cb44-3e8f-b007-348b0daf740c | -14.32404 | -53.29239 | 2025-08-28 12:36:00 | TERRA_M-T | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 11.0 |
| 007972a1-c31b-3430-9486-1afe082cd1f6 | -13.07974 | -46.36181 | 2025-08-28 12:36:00 | TERRA_M-T | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 27.4 |
| bf7a27b8-f7f6-38f2-84bd-8ba5b5e40773 | -16.98184 | -47.24711 | 2025-08-28 12:36:00 | TERRA_M-T | CRISTALINA | GOIÁS | Brasil | 5206206 | 52 | 33 | nan | nan | nan | Cerrado | 22.1 |
| fe69a0e9-82d3-3f64-a71f-139190ce8053 | -12.68424 | -45.28925 | 2025-08-28 12:36:00 | TERRA_M-T | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 25.0 |
| d160ef7c-eb31-3ed4-aed2-ddb2a1929f00 | -14.2194 | -48.14338 | 2025-08-28 12:36:00 | TERRA_M-T | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 16.0 |
| 0da6f5a6-b9ea-3c07-93e0-0d99c12985d5 | -13.39726 | -46.86113 | 2025-08-28 12:36:00 | TERRA_M-T | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 14.8 |
| 31f8ae87-6ceb-3d12-891c-d07ee24cee42 | -14.21513 | -48.13591 | 2025-08-28 12:36:00 | TERRA_M-T | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 9.8 |
| c1720a6d-bd9b-32a3-a735-b9229709fad7 | -12.40176 | -45.02507 | 2025-08-28 12:36:00 | TERRA_M-T | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 48.9 |
| 7c116bf7-2c9a-3413-9951-6f49ae9d26de | -12.92706 | -46.31378 | 2025-08-28 12:36:00 | TERRA_M-T | LAVANDEIRA | TOCANTINS | Brasil | 1712157 | 17 | 33 | nan | nan | nan | Cerrado | 30.6 |
| dac63d30-03bc-3795-bbd5-cd5f1bb72401 | -14.21352 | -48.14909 | 2025-08-28 12:36:00 | TERRA_M-T | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 11.1 |
| b3046e22-3f5c-34bd-a778-09813eece7a1 | -13.45577 | -46.84251 | 2025-08-28 12:36:00 | TERRA_M-T | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 12.3 |
| 3211b0f1-1291-3187-be87-52b8b5800142 | -11.15019 | -54.31105 | 2025-08-28 12:36:00 | TERRA_M-T | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 28.0 |
| e62cc0b9-a2aa-3dad-806d-8a091a80af3e | -12.70656 | -48.1622 | 2025-08-28 12:36:00 | TERRA_M-T | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 31.0 |
| 406f23db-439a-3bc7-a046-70888631b7ea | -12.51683 | -47.23193 | 2025-08-28 12:36:00 | TERRA_M-T | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 32.5 |
| 5ea54f73-fbfb-3d9e-953b-5fee5e305779 | -13.72344 | -51.91292 | 2025-08-28 12:36:00 | TERRA_M-T | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 13.9 |
| f3eba20e-f29c-3062-a5ae-653ff0ad80b9 | -15.19263 | -52.33111 | 2025-08-28 12:36:00 | TERRA_M-T | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 71b4e9c1-68a7-385a-9580-2370310afcdb | -11.23028 | -55.04554 | 2025-08-28 12:36:00 | TERRA_M-T | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 12.0 |
| b9c4068e-8907-319d-854c-acca69e4e000 | -15.18925 | -53.80327 | 2025-08-28 12:36:00 | TERRA_M-T | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | 29.4 |
| c36c613f-bba6-3ced-ab86-81384424c274 | -13.97873 | -46.33289 | 2025-08-28 12:36:00 | TERRA_M-T | GUARANI DE GOIÁS | GOIÁS | Brasil | 5209408 | 52 | 33 | nan | nan | nan | Cerrado | 14.9 |
| 404b814f-000d-3922-9242-8c9e8adbbfd5 | -16.15612 | -49.64241 | 2025-08-28 12:36:00 | TERRA_M-T | ITAUÇU | GOIÁS | Brasil | 5211404 | 52 | 33 | nan | nan | nan | Cerrado | 8.5 |
| caaa570f-ddc4-3f2f-9247-4e681f1e4a83 | -15.19069 | -53.79374 | 2025-08-28 12:36:00 | TERRA_M-T | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | 21.5 |
| d2a5df08-2577-38fe-82d9-d2cb2095a7fb | -13.42949 | -46.97773 | 2025-08-28 12:36:00 | TERRA_M-T | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 34.6 |
| c47370b6-80e1-3419-8002-212fe618b371 | -16.36317 | -43.77497 | 2025-08-28 12:36:00 | TERRA_M-T | CAPITÃO ENÉAS | MINAS GERAIS | Brasil | 3112703 | 31 | 33 | nan | nan | nan | Cerrado | 24.3 |
| ce7ea644-2496-3266-b156-eaefcd78b664 | -15.57567 | -53.99674 | 2025-08-28 12:36:00 | TERRA_M-T | POXORÉU | MATO GROSSO | Brasil | 5107008 | 51 | 33 | nan | nan | nan | Cerrado | 4.9 |
| c89c4fef-3021-3632-ae4a-75f8f7ed0ca0 | -12.31502 | -49.99931 | 2025-08-28 12:36:00 | TERRA_M-T | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 13.5 |
| f45ab6d7-1bf7-398f-8ca3-89034a512cb4 | -16.68467 | -49.412 | 2025-08-28 12:36:00 | TERRA_M-T | GOIÂNIA | GOIÁS | Brasil | 5208707 | 52 | 33 | nan | nan | nan | Cerrado | 6.7 |
| d56f56ed-7589-313f-bbe8-640d659ddcaa | -14.36192 | -52.08698 | 2025-08-28 12:36:00 | TERRA_M-T | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 7.7 |
| 183c859a-4e78-3275-8289-17248b0f2d5d | -13.43379 | -46.84975 | 2025-08-28 12:36:00 | TERRA_M-T | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 30.7 |
| 21f81963-ebbd-37cc-85b1-9d77b9068a51 | -16.52225 | -50.85864 | 2025-08-28 12:36:00 | TERRA_M-T | IVOLÂNDIA | GOIÁS | Brasil | 5211602 | 52 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 98293fd6-1a83-3642-b3ba-6ab5e5d7eb3b | -12.686 | -48.15875 | 2025-08-28 12:36:00 | TERRA_M-T | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 23.1 |
| 3ca89336-99ed-345b-b1cb-9b97c7f363e7 | -12.89853 | -48.09646 | 2025-08-28 12:36:00 | TERRA_M-T | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 14.1 |
| 91408dcf-d50e-3d85-aba2-03e14ce67185 | -18.46137 | -46.93478 | 2025-08-28 12:36:00 | TERRA_M-T | COROMANDEL | MINAS GERAIS | Brasil | 3119302 | 31 | 33 | nan | nan | nan | Cerrado | 46.5 |
| 17efd524-e9f7-3759-a303-70ccc2252d87 | -12.50402 | -47.24493 | 2025-08-28 12:36:00 | TERRA_M-T | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 16.7 |
| df6fdfac-d108-3e9d-93b9-4675ba10b6a7 | -15.17495 | -52.32848 | 2025-08-28 12:36:00 | TERRA_M-T | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 5.6 |
| ca4faf8b-4a3a-376d-90ca-d8918ab49bd4 | -14.33247 | -51.90049 | 2025-08-28 12:36:00 | TERRA_M-T | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 13.0 |
| f9744062-fdb4-3b74-a763-1dbce600ff6a | -14.32987 | -51.91869 | 2025-08-28 12:36:00 | TERRA_M-T | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 8.8 |
| 09cb4cf6-adec-3193-907f-a4f982c028e6 | -14.31164 | -53.25236 | 2025-08-28 12:36:00 | TERRA_M-T | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 35.4 |
| d16760bf-1270-300f-9ece-7bddc59eb78a | -12.89689 | -48.10919 | 2025-08-28 12:36:00 | TERRA_M-T | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 29.5 |
| be03c7ce-7f97-3f20-aebb-734048847e47 | -19.3217 | -44.9489 | 2025-08-28 12:36:00 | TERRA_M-T | POMPÉU | MINAS GERAIS | Brasil | 3152006 | 31 | 33 | nan | nan | nan | Cerrado | 57.8 |
| df7a2504-6451-300e-8617-d827beb702ae | -14.32542 | -53.28305 | 2025-08-28 12:36:00 | TERRA_M-T | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 17.8 |


[Clique aqui para ver as próximas entradas](README94.md)
