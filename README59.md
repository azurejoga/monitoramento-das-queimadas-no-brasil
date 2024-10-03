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

## Dados Diários - Página 59

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| bfc84d46-26ec-3033-bec5-e36892f7a763 | -19.31021 | -42.61453 | 2024-10-03 03:15:00 | NPP-375D | MESQUITA | MINAS GERAIS | Brasil | 3141702 | 31 | 33 | nan | nan | nan | Mata Atlântica | 7.4 |
| 22d92635-8645-36a2-b268-5813c4fcb604 | -19.30548 | -42.60643 | 2024-10-03 03:15:00 | NPP-375D | MESQUITA | MINAS GERAIS | Brasil | 3141702 | 31 | 33 | nan | nan | nan | Mata Atlântica | 20.9 |
| d5d3bd86-9834-39c1-b93b-2980c5368d3c | -19.3033 | -42.61595 | 2024-10-03 03:15:00 | NPP-375D | MESQUITA | MINAS GERAIS | Brasil | 3141702 | 31 | 33 | nan | nan | nan | Mata Atlântica | 31.4 |
| 48c52e72-57af-3872-aedc-15a713a76a1c | -19.30195 | -42.59311 | 2024-10-03 03:15:00 | NPP-375D | MESQUITA | MINAS GERAIS | Brasil | 3141702 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.1 |
| 84f37e9c-5660-32d0-a827-e06f4ca326cd | -19.29549 | -42.59258 | 2024-10-03 03:15:00 | NPP-375D | MESQUITA | MINAS GERAIS | Brasil | 3141702 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.7 |
| 35650fbf-0d79-39df-acde-c415a2039f5f | -19.27244 | -42.36422 | 2024-10-03 03:15:00 | NPP-375D | BELO ORIENTE | MINAS GERAIS | Brasil | 3106309 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| d4fe4e2a-a2ac-379f-8c0e-023bfc809da9 | -19.27132 | -42.36918 | 2024-10-03 03:15:00 | NPP-375D | BELO ORIENTE | MINAS GERAIS | Brasil | 3106309 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| 6af16a03-fef0-3afb-944d-781964f5340f | -19.24339 | -42.46359 | 2024-10-03 03:15:00 | NPP-375D | BELO ORIENTE | MINAS GERAIS | Brasil | 3106309 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 62b9de87-ac44-3a0a-9777-901f535d4338 | -19.23724 | -42.46192 | 2024-10-03 03:15:00 | NPP-375D | BELO ORIENTE | MINAS GERAIS | Brasil | 3106309 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 2621c90c-902f-3bbf-a66b-5541594e7c68 | -18.08336 | -42.60701 | 2024-10-03 03:15:00 | NPP-375D | SÃO SEBASTIÃO DO MARANHÃO | MINAS GERAIS | Brasil | 3164506 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| bfdefa68-bb39-3ea3-bac4-cff5fb7fc6aa | -18.08137 | -42.64508 | 2024-10-03 03:15:00 | NPP-375D | SÃO SEBASTIÃO DO MARANHÃO | MINAS GERAIS | Brasil | 3164506 | 31 | 33 | nan | nan | nan | Mata Atlântica | 9.9 |
| b2cccfe5-3d9f-33d0-9d11-ebc2af1cc3a6 | -18.07592 | -42.6101 | 2024-10-03 03:15:00 | NPP-375D | SÃO SEBASTIÃO DO MARANHÃO | MINAS GERAIS | Brasil | 3164506 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.0 |
| 6f78af9b-5156-3fba-8b0a-15449b8d88d6 | -18.07563 | -42.6088 | 2024-10-03 03:15:00 | NPP-375D | SÃO SEBASTIÃO DO MARANHÃO | MINAS GERAIS | Brasil | 3164506 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.3 |
| f93cecc2-890b-3b87-bc02-7d213e571e85 | -18.07475 | -42.61522 | 2024-10-03 03:15:00 | NPP-375D | SÃO SEBASTIÃO DO MARANHÃO | MINAS GERAIS | Brasil | 3164506 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.3 |
| ec347f20-fe71-34c5-a3ca-d274bc99029e | -18.07452 | -42.61381 | 2024-10-03 03:15:00 | NPP-375D | SÃO SEBASTIÃO DO MARANHÃO | MINAS GERAIS | Brasil | 3164506 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.3 |
| 4dbdface-0277-3143-bf5d-98b8d2bd1494 | -18.07349 | -42.62068 | 2024-10-03 03:15:00 | NPP-375D | SÃO SEBASTIÃO DO MARANHÃO | MINAS GERAIS | Brasil | 3164506 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.3 |
| c208235c-8f1c-3515-8680-8ad16e292d8e | -18.07331 | -42.61922 | 2024-10-03 03:15:00 | NPP-375D | SÃO SEBASTIÃO DO MARANHÃO | MINAS GERAIS | Brasil | 3164506 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| 01c4a179-615f-3915-8ea4-ed3439d5c133 | -18.06961 | -42.60827 | 2024-10-03 03:15:00 | NPP-375D | SÃO SEBASTIÃO DO MARANHÃO | MINAS GERAIS | Brasil | 3164506 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.0 |
| cf8c825c-e684-39c7-8911-a9316aafc41a | -18.06929 | -42.60708 | 2024-10-03 03:15:00 | NPP-375D | SÃO SEBASTIÃO DO MARANHÃO | MINAS GERAIS | Brasil | 3164506 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.3 |
| 2a97fa3e-fe79-3686-b8bb-2b1f218d96ce | -18.05861 | -42.62681 | 2024-10-03 03:15:00 | NPP-375D | SÃO SEBASTIÃO DO MARANHÃO | MINAS GERAIS | Brasil | 3164506 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.7 |
| c87689b5-84c4-3318-a8b3-e18b54226209 | -18.05847 | -42.6254 | 2024-10-03 03:15:00 | NPP-375D | SÃO SEBASTIÃO DO MARANHÃO | MINAS GERAIS | Brasil | 3164506 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.9 |
| a7c5a06c-0678-3af1-8229-39b63aee26d5 | -18.05239 | -42.62452 | 2024-10-03 03:15:00 | NPP-375D | SÃO SEBASTIÃO DO MARANHÃO | MINAS GERAIS | Brasil | 3164506 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.7 |
| 3b695bbd-b572-3ae6-95ff-63af76a3107f | -18.05227 | -42.62302 | 2024-10-03 03:15:00 | NPP-375D | SÃO SEBASTIÃO DO MARANHÃO | MINAS GERAIS | Brasil | 3164506 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.9 |
| fc82cbd2-2605-3a27-910a-43606430c095 | -19.03884 | -43.20583 | 2024-10-03 03:15:00 | NPP-375D | CARMÉSIA | MINAS GERAIS | Brasil | 3113800 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.6 |
| 40af5ef5-0cd9-3d29-bab7-d52accdf4e39 | -19.03278 | -43.20246 | 2024-10-03 03:15:00 | NPP-375D | CARMÉSIA | MINAS GERAIS | Brasil | 3113800 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| d09276b8-9c02-38d4-a234-6c908caa0256 | -19.02666 | -43.19933 | 2024-10-03 03:15:00 | NPP-375D | CARMÉSIA | MINAS GERAIS | Brasil | 3113800 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| ab4f55eb-f368-3bab-aa5d-6e087a960086 | -19.02502 | -43.20633 | 2024-10-03 03:15:00 | NPP-375D | CARMÉSIA | MINAS GERAIS | Brasil | 3113800 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.2 |
| f639b3dc-49b2-3406-9f89-2c179ac85165 | -19.02175 | -43.19647 | 2024-10-03 03:15:00 | NPP-375D | CARMÉSIA | MINAS GERAIS | Brasil | 3113800 | 31 | 33 | nan | nan | nan | Mata Atlântica | 14.2 |
| 97c4b246-a083-33ce-8d79-c555b624e62e | -19.02035 | -43.19704 | 2024-10-03 03:15:00 | NPP-375D | CARMÉSIA | MINAS GERAIS | Brasil | 3113800 | 31 | 33 | nan | nan | nan | Mata Atlântica | 16.1 |
| 081d4b99-b435-3962-9a09-c9ce06b45007 | -19.02032 | -43.20277 | 2024-10-03 03:15:00 | NPP-375D | CARMÉSIA | MINAS GERAIS | Brasil | 3113800 | 31 | 33 | nan | nan | nan | Mata Atlântica | 14.2 |
| bb51274d-ed9b-33e4-aae0-befbc8cf5e5d | -19.0188 | -43.20365 | 2024-10-03 03:15:00 | NPP-375D | CARMÉSIA | MINAS GERAIS | Brasil | 3113800 | 31 | 33 | nan | nan | nan | Mata Atlântica | 21.6 |
| 71a11526-6b41-3e68-989e-a9dd2414d61b | -19.01835 | -43.21146 | 2024-10-03 03:15:00 | NPP-375D | CARMÉSIA | MINAS GERAIS | Brasil | 3113800 | 31 | 33 | nan | nan | nan | Mata Atlântica | 10.5 |
| 70599749-68e0-3a71-85af-49bb810aa121 | -18.97557 | -43.21876 | 2024-10-03 03:15:00 | NPP-375D | DOM JOAQUIM | MINAS GERAIS | Brasil | 3122603 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 56c2cbb2-68ab-3643-8862-6c8d7f4fef27 | -18.97413 | -43.22499 | 2024-10-03 03:15:00 | NPP-375D | DOM JOAQUIM | MINAS GERAIS | Brasil | 3122603 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| 37541fd6-8569-3143-9b8d-d68c3f4a7fa6 | -18.97393 | -43.21943 | 2024-10-03 03:15:00 | NPP-375D | DOM JOAQUIM | MINAS GERAIS | Brasil | 3122603 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 3d383f5a-cbe9-3084-a64f-23f8e29ec01c | -18.97245 | -43.22565 | 2024-10-03 03:15:00 | NPP-375D | DOM JOAQUIM | MINAS GERAIS | Brasil | 3122603 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| a30da4de-7905-3f2d-a06d-8cc2284e0ce4 | -18.84674 | -42.92863 | 2024-10-03 03:15:00 | NPP-375D | GUANHÃES | MINAS GERAIS | Brasil | 3128006 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.7 |
| 352c0a59-a231-3af2-a33e-22523bf34092 | -18.84631 | -42.93019 | 2024-10-03 03:15:00 | NPP-375D | GUANHÃES | MINAS GERAIS | Brasil | 3128006 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.1 |
| 0502e3bb-03aa-3145-9e04-c55d087a7172 | -18.84539 | -42.93436 | 2024-10-03 03:15:00 | NPP-375D | GUANHÃES | MINAS GERAIS | Brasil | 3128006 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.7 |
| 4e708642-cdad-341f-96fc-c511ef9aac8c | -18.84502 | -42.93584 | 2024-10-03 03:15:00 | NPP-375D | GUANHÃES | MINAS GERAIS | Brasil | 3128006 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.1 |
| f5e88f83-05a1-3e26-9d86-4dedc1c26d6a | -18.84156 | -42.92134 | 2024-10-03 03:15:00 | NPP-375D | GUANHÃES | MINAS GERAIS | Brasil | 3128006 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.4 |
| 1b43fbcf-bb59-3a9b-9591-675edf71c370 | -18.84049 | -42.92643 | 2024-10-03 03:15:00 | NPP-375D | GUANHÃES | MINAS GERAIS | Brasil | 3128006 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.4 |
| 1f1165cf-48cb-3faa-87ec-244ddd98b585 | -18.84002 | -42.92815 | 2024-10-03 03:15:00 | NPP-375D | GUANHÃES | MINAS GERAIS | Brasil | 3128006 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.1 |
| 79e8be31-aa6d-3f29-b58c-c08e6d624dbe | -18.83899 | -42.93282 | 2024-10-03 03:15:00 | NPP-375D | GUANHÃES | MINAS GERAIS | Brasil | 3128006 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.4 |
| c4df48c1-e9c4-3a8c-a67e-28a170138862 | -18.83859 | -42.93442 | 2024-10-03 03:15:00 | NPP-375D | GUANHÃES | MINAS GERAIS | Brasil | 3128006 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.1 |
| 70539040-626b-334a-9b17-ad71a534bd1d | -18.83405 | -42.92502 | 2024-10-03 03:15:00 | NPP-375D | GUANHÃES | MINAS GERAIS | Brasil | 3128006 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.4 |
| 253aceaa-d6b9-38b4-80a7-5ef2721f7140 | -18.83359 | -42.9267 | 2024-10-03 03:15:00 | NPP-375D | GUANHÃES | MINAS GERAIS | Brasil | 3128006 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.1 |
| 385b9384-3868-387e-8f19-48053b893f4b | -18.62605 | -41.84135 | 2024-10-03 03:15:00 | NPP-375D | MATHIAS LOBATO | MINAS GERAIS | Brasil | 3171501 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.4 |
| f94055c1-c73b-354a-9d89-168366ce09f5 | -18.54279 | -42.24283 | 2024-10-03 03:15:00 | NPP-375D | COROACI | MINAS GERAIS | Brasil | 3119203 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| 96a8bbc6-2991-3e46-99da-6ee387db3de5 | -18.53873 | -42.23185 | 2024-10-03 03:15:00 | NPP-375D | COROACI | MINAS GERAIS | Brasil | 3119203 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| 9218b20c-6b96-383b-93b8-31daa7774c9f | -18.53656 | -42.24152 | 2024-10-03 03:15:00 | NPP-375D | VIRGOLÂNDIA | MINAS GERAIS | Brasil | 3171907 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.7 |
| a4a5b553-a709-3a78-9bab-88fd220ac84f | -18.53521 | -42.24752 | 2024-10-03 03:15:00 | NPP-375D | VIRGOLÂNDIA | MINAS GERAIS | Brasil | 3171907 | 31 | 33 | nan | nan | nan | Mata Atlântica | 6.4 |
| 32b0e413-17c9-3c51-91c8-9bf098e691c2 | -18.53387 | -42.2535 | 2024-10-03 03:15:00 | NPP-375D | VIRGOLÂNDIA | MINAS GERAIS | Brasil | 3171907 | 31 | 33 | nan | nan | nan | Mata Atlântica | 6.4 |
| fdda6284-9481-3d44-83fa-074aea254d1f | -18.53241 | -42.23094 | 2024-10-03 03:15:00 | NPP-375D | VIRGOLÂNDIA | MINAS GERAIS | Brasil | 3171907 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| 62388e87-8b80-329e-8fd0-1f7e4b8df533 | -18.52979 | -42.2426 | 2024-10-03 03:15:00 | NPP-375D | VIRGOLÂNDIA | MINAS GERAIS | Brasil | 3171907 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.7 |
| e581ab5f-8a1d-31e4-88e5-b03cf253cc4e | -18.52852 | -42.24827 | 2024-10-03 03:15:00 | NPP-375D | VIRGOLÂNDIA | MINAS GERAIS | Brasil | 3171907 | 31 | 33 | nan | nan | nan | Mata Atlântica | 6.4 |
| 8ab2597d-b0b8-3f09-8cb0-48ca901ee845 | -18.52612 | -42.2299 | 2024-10-03 03:15:00 | NPP-375D | NACIP RAYDAN | MINAS GERAIS | Brasil | 3144201 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 9a8b3b79-7781-34b4-bf5c-eade65561b9e | -18.52499 | -42.23493 | 2024-10-03 03:15:00 | NPP-375D | VIRGOLÂNDIA | MINAS GERAIS | Brasil | 3171907 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.8 |
| d2175bfc-3db3-37a4-81c2-341f8ce832c7 | -18.52233 | -42.24675 | 2024-10-03 03:15:00 | NPP-375D | VIRGOLÂNDIA | MINAS GERAIS | Brasil | 3171907 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 924300e2-1085-3d45-bb23-1bcafc4a9ba9 | -18.51648 | -42.24371 | 2024-10-03 03:15:00 | NPP-375D | VIRGOLÂNDIA | MINAS GERAIS | Brasil | 3171907 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| dd480e4f-a474-34e0-9257-637ab8439092 | -18.51512 | -42.24972 | 2024-10-03 03:15:00 | NPP-375D | VIRGOLÂNDIA | MINAS GERAIS | Brasil | 3171907 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| bde77a33-c840-39d5-81ce-e09aa5f20cdb | -18.29642 | -42.17348 | 2024-10-03 03:15:00 | NPP-375D | SÃO JOSÉ DA SAFIRA | MINAS GERAIS | Brasil | 3163003 | 31 | 33 | nan | nan | nan | Mata Atlântica | 17.4 |
| c9ea330e-4afd-3dd7-bda0-95971d68802a | -20.54871 | -43.37032 | 2024-10-03 03:15:00 | NPP-375D | MARIANA | MINAS GERAIS | Brasil | 3140001 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| d416d5b0-c3b5-3f5c-8c11-6f41effcfae0 | -20.54735 | -43.37609 | 2024-10-03 03:15:00 | NPP-375D | MARIANA | MINAS GERAIS | Brasil | 3140001 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| af4b2202-6bed-3963-88a9-0120f927106e | -20.54236 | -43.36874 | 2024-10-03 03:15:00 | NPP-375D | MARIANA | MINAS GERAIS | Brasil | 3140001 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 60ddef29-e37f-3c06-b79d-d8dedad37b0f | -20.4772 | -43.18398 | 2024-10-03 03:15:00 | NPP-375D | DIOGO DE VASCONCELOS | MINAS GERAIS | Brasil | 3121704 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 0dd51d9c-f2cd-345f-8ef3-480331842e73 | -20.28227 | -43.52451 | 2024-10-03 03:15:00 | NPP-375D | OURO PRETO | MINAS GERAIS | Brasil | 3146107 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.3 |
| 345e5b6b-8674-30f0-a002-152a4c5e1962 | -20.27605 | -43.52201 | 2024-10-03 03:15:00 | NPP-375D | OURO PRETO | MINAS GERAIS | Brasil | 3146107 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.3 |
| 6af0d883-b29b-3f65-aa07-5ba6dec27d45 | -20.27476 | -43.52744 | 2024-10-03 03:15:00 | NPP-375D | OURO PRETO | MINAS GERAIS | Brasil | 3146107 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.3 |
| 370df303-5bc9-355d-a6f0-44ac4533b935 | -20.07029 | -43.21677 | 2024-10-03 03:15:00 | NPP-375D | ALVINÓPOLIS | MINAS GERAIS | Brasil | 3102308 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| eb890a0e-505b-366b-8c22-66e47485f521 | -20.06892 | -43.2227 | 2024-10-03 03:15:00 | NPP-375D | ALVINÓPOLIS | MINAS GERAIS | Brasil | 3102308 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| aba6ad89-2e58-34b1-874e-43ebf3f994f4 | -19.87638 | -43.14959 | 2024-10-03 03:15:00 | NPP-375D | JOÃO MONLEVADE | MINAS GERAIS | Brasil | 3136207 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.7 |
| 29f30559-f73d-3046-987d-27c5905940d5 | -19.87343 | -43.16592 | 2024-10-03 03:15:00 | NPP-375D | JOÃO MONLEVADE | MINAS GERAIS | Brasil | 3136207 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.9 |
| 698764aa-45ff-384e-95d3-e0cba0dae643 | -19.87295 | -43.16444 | 2024-10-03 03:15:00 | NPP-375D | JOÃO MONLEVADE | MINAS GERAIS | Brasil | 3136207 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.0 |
| 3ad9fcd8-21df-3675-954b-3052d39acc49 | -19.86838 | -43.15884 | 2024-10-03 03:15:00 | NPP-375D | JOÃO MONLEVADE | MINAS GERAIS | Brasil | 3136207 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.4 |
| dbffa434-eb61-36ec-934a-d68c7dcf5934 | -19.8673 | -43.16334 | 2024-10-03 03:15:00 | NPP-375D | JOÃO MONLEVADE | MINAS GERAIS | Brasil | 3136207 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.6 |
| cbc5d1fa-6648-36c5-9e87-b9c2bbac7997 | -19.86683 | -43.16181 | 2024-10-03 03:15:00 | NPP-375D | JOÃO MONLEVADE | MINAS GERAIS | Brasil | 3136207 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.2 |
| ce6dbf3a-f56e-3631-a5ca-44fd135fde1c | -19.86578 | -43.16636 | 2024-10-03 03:15:00 | NPP-375D | JOÃO MONLEVADE | MINAS GERAIS | Brasil | 3136207 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.3 |
| ba5bb39b-9bad-37df-9461-bca770fb8515 | -19.5093 | -42.87224 | 2024-10-03 03:15:00 | NPP-375D | ANTÔNIO DIAS | MINAS GERAIS | Brasil | 3103009 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 0257d970-3f86-35a5-b1ec-a3dc5c5a1cb7 | -19.50775 | -42.87045 | 2024-10-03 03:15:00 | NPP-375D | ANTÔNIO DIAS | MINAS GERAIS | Brasil | 3103009 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.4 |
| 4a54ef01-fde0-3ddb-a489-cb5349c0f201 | -19.50445 | -42.89287 | 2024-10-03 03:15:00 | NPP-375D | ANTÔNIO DIAS | MINAS GERAIS | Brasil | 3103009 | 31 | 33 | nan | nan | nan | Mata Atlântica | 5.9 |
| 951b8eea-e464-3b85-9cf8-115bfb74a1b8 | -19.50332 | -42.88982 | 2024-10-03 03:15:00 | NPP-375D | ANTÔNIO DIAS | MINAS GERAIS | Brasil | 3103009 | 31 | 33 | nan | nan | nan | Mata Atlântica | 5.8 |
| c5ed2c2e-c43d-3332-8dc9-961420225009 | -19.5031 | -42.87028 | 2024-10-03 03:15:00 | NPP-375D | ANTÔNIO DIAS | MINAS GERAIS | Brasil | 3103009 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.9 |
| 7a447e55-a211-3c52-b72b-05fe285f911b | -19.50212 | -42.87441 | 2024-10-03 03:15:00 | NPP-375D | ANTÔNIO DIAS | MINAS GERAIS | Brasil | 3103009 | 31 | 33 | nan | nan | nan | Mata Atlântica | 9.6 |
| 1a789870-dd81-3a45-ae13-cb61bdaa328e | -19.50164 | -42.8972 | 2024-10-03 03:15:00 | NPP-375D | ANTÔNIO DIAS | MINAS GERAIS | Brasil | 3103009 | 31 | 33 | nan | nan | nan | Mata Atlântica | 5.8 |
| c624f95c-6f8d-3b2f-bd41-ba26a4415675 | -19.50155 | -42.86843 | 2024-10-03 03:15:00 | NPP-375D | ANTÔNIO DIAS | MINAS GERAIS | Brasil | 3103009 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.8 |
| 76765b06-ae02-3023-9187-85b1030f4058 | -19.50123 | -42.87821 | 2024-10-03 03:15:00 | NPP-375D | ANTÔNIO DIAS | MINAS GERAIS | Brasil | 3103009 | 31 | 33 | nan | nan | nan | Mata Atlântica | 9.6 |
| 020fc07a-8f54-39e0-a830-e49d128ad640 | -19.50054 | -42.87283 | 2024-10-03 03:15:00 | NPP-375D | ANTÔNIO DIAS | MINAS GERAIS | Brasil | 3103009 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.8 |
| fd420846-f29d-39c1-a6f8-78a662bba58a | -19.50006 | -42.88316 | 2024-10-03 03:15:00 | NPP-375D | ANTÔNIO DIAS | MINAS GERAIS | Brasil | 3103009 | 31 | 33 | nan | nan | nan | Mata Atlântica | 13.4 |
| 9bd836b5-d161-35b6-9a8e-df07c92786ff | -19.49971 | -42.87646 | 2024-10-03 03:15:00 | NPP-375D | ANTÔNIO DIAS | MINAS GERAIS | Brasil | 3103009 | 31 | 33 | nan | nan | nan | Mata Atlântica | 9.7 |
| bb460abc-f403-3855-b7d9-976e0c569c23 | -19.49873 | -42.88073 | 2024-10-03 03:15:00 | NPP-375D | ANTÔNIO DIAS | MINAS GERAIS | Brasil | 3103009 | 31 | 33 | nan | nan | nan | Mata Atlântica | 9.7 |
| c790937a-bfae-3b47-9ab2-19c3a7cc243b | -19.49853 | -42.88968 | 2024-10-03 03:15:00 | NPP-375D | ANTÔNIO DIAS | MINAS GERAIS | Brasil | 3103009 | 31 | 33 | nan | nan | nan | Mata Atlântica | 13.4 |
| 7678c7bd-3c2f-37a4-8004-61cd135d30e0 | -19.49734 | -42.88679 | 2024-10-03 03:15:00 | NPP-375D | ANTÔNIO DIAS | MINAS GERAIS | Brasil | 3103009 | 31 | 33 | nan | nan | nan | Mata Atlântica | 9.9 |
| e11a3ed2-1c0c-3328-88f1-29c9fa23b119 | -19.49506 | -42.87609 | 2024-10-03 03:15:00 | NPP-375D | ANTÔNIO DIAS | MINAS GERAIS | Brasil | 3103009 | 31 | 33 | nan | nan | nan | Mata Atlântica | 9.6 |
| 04c997b4-d4c9-3f4f-9aed-565cee88da6f | -19.49413 | -42.88004 | 2024-10-03 03:15:00 | NPP-375D | ANTÔNIO DIAS | MINAS GERAIS | Brasil | 3103009 | 31 | 33 | nan | nan | nan | Mata Atlântica | 13.4 |
| c977e719-e8ff-31c7-bd72-7ab6571d9e35 | -19.49347 | -42.87465 | 2024-10-03 03:15:00 | NPP-375D | ANTÔNIO DIAS | MINAS GERAIS | Brasil | 3103009 | 31 | 33 | nan | nan | nan | Mata Atlântica | 9.7 |
| 5844ac30-6148-3913-91e3-fb5540dc64ec | -19.49261 | -42.87835 | 2024-10-03 03:15:00 | NPP-375D | ANTÔNIO DIAS | MINAS GERAIS | Brasil | 3103009 | 31 | 33 | nan | nan | nan | Mata Atlântica | 9.7 |
| 95e63855-1ba3-31bc-a318-d67448b84318 | -19.49136 | -42.88381 | 2024-10-03 03:15:00 | NPP-375D | ANTÔNIO DIAS | MINAS GERAIS | Brasil | 3103009 | 31 | 33 | nan | nan | nan | Mata Atlântica | 9.9 |
| 266c9fa7-3cae-3e04-96ea-ff58e44fa418 | -20.85558 | -42.23424 | 2024-10-03 03:15:00 | NPP-375D | VIEIRAS | MINAS GERAIS | Brasil | 3171402 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| fefade30-b36d-3ab0-bb1d-d654a07955de | -20.8524 | -42.22908 | 2024-10-03 03:15:00 | NPP-375D | VIEIRAS | MINAS GERAIS | Brasil | 3171402 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.8 |


[Clique aqui para ver as próximas entradas](README60.md)
