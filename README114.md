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

## Dados Diários - Página 114

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 6f525787-da62-32f2-ae75-b6e890251d50 | -13.80199 | -48.1272 | 2024-09-26 04:59:00 | NOAA-21 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 1a4244bb-3dc2-317e-8684-7901cd2b7dc2 | -13.79907 | -48.07263 | 2024-09-26 04:59:00 | NOAA-21 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 8a95d04a-4825-3b31-b96c-c469379b19af | -13.79846 | -48.07742 | 2024-09-26 04:59:00 | NOAA-21 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 67c73217-fbab-3fd3-855a-9b6f9c9100b4 | -13.79787 | -48.12118 | 2024-09-26 04:59:00 | NOAA-21 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 5.4 |
| c74e2e09-571d-3c52-8a32-249bb31ca2f1 | -13.79485 | -48.06723 | 2024-09-26 04:59:00 | NOAA-21 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 95d0c80b-6aed-349e-bb0d-82defd11850a | -13.79431 | -48.07151 | 2024-09-26 04:59:00 | NOAA-21 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| d7477808-8efd-3916-8884-568932f60bdc | -13.79316 | -48.11982 | 2024-09-26 04:59:00 | NOAA-21 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| b27e28a8-6171-39e0-8be8-f259e8e4b305 | -13.7902 | -48.10457 | 2024-09-26 04:59:00 | NOAA-21 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 05e908d6-741c-3c54-a594-0c14e4ca6d3c | -13.78901 | -48.11401 | 2024-09-26 04:59:00 | NOAA-21 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 2482fae3-b97f-36d6-89a1-ab48bdc41354 | -13.78488 | -48.10804 | 2024-09-26 04:59:00 | NOAA-21 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 3dc098f4-ae9b-3290-9532-1ee6cac20f8b | -13.7843 | -48.11271 | 2024-09-26 04:59:00 | NOAA-21 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 4b8174ad-6d8e-33da-b020-5254d56a9ca1 | -13.78213 | -48.09084 | 2024-09-26 04:59:00 | NOAA-21 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 48baf288-70ad-39e3-9177-03a13ab9ac51 | -13.78139 | -48.09688 | 2024-09-26 04:59:00 | NOAA-21 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| e4c46cd9-34eb-3a4a-90ed-6495f41b791a | -13.78076 | -48.10191 | 2024-09-26 04:59:00 | NOAA-21 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 3.3 |
| ed97c14e-5d37-350e-92ac-9343f5f1fb01 | -13.78017 | -48.10672 | 2024-09-26 04:59:00 | NOAA-21 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 6921cd31-6b08-39d6-b125-74b93bd48844 | -15.56944 | -47.85718 | 2024-09-26 04:59:00 | NOAA-21 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 2.0 |
| f39b3dae-d63b-304e-9410-637d8e96c839 | -16.35059 | -47.71162 | 2024-09-26 04:59:00 | NOAA-21 | LUZIÂNIA | GOIÁS | Brasil | 5212501 | 52 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 465bab87-0d10-3347-8965-accbf902cc17 | -16.35022 | -47.71473 | 2024-09-26 04:59:00 | NOAA-21 | LUZIÂNIA | GOIÁS | Brasil | 5212501 | 52 | 33 | nan | nan | nan | Cerrado | 3.8 |
| f36f40d1-0484-3f3f-aea4-2652e9e904eb | -16.34908 | -47.70922 | 2024-09-26 04:59:00 | NOAA-21 | LUZIÂNIA | GOIÁS | Brasil | 5212501 | 52 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 273f1f6c-75fc-3172-8655-fb04aeea7455 | -16.34874 | -47.71232 | 2024-09-26 04:59:00 | NOAA-21 | LUZIÂNIA | GOIÁS | Brasil | 5212501 | 52 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 15207dfb-d35e-355c-840f-8c4cfd5dd07d | -16.34839 | -47.71546 | 2024-09-26 04:59:00 | NOAA-21 | LUZIÂNIA | GOIÁS | Brasil | 5212501 | 52 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 4ace10b0-8b5b-3a4e-ae6c-c5edbabcf538 | -16.3462 | -47.70492 | 2024-09-26 04:59:00 | NOAA-21 | LUZIÂNIA | GOIÁS | Brasil | 5212501 | 52 | 33 | nan | nan | nan | Cerrado | 6.1 |
| fb1bd78f-c2fe-317b-9781-e1a8210906b9 | -16.34584 | -47.70801 | 2024-09-26 04:59:00 | NOAA-21 | LUZIÂNIA | GOIÁS | Brasil | 5212501 | 52 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 63d07daa-b109-3edc-9bc0-5504bc4b86f5 | -16.34431 | -47.70553 | 2024-09-26 04:59:00 | NOAA-21 | LUZIÂNIA | GOIÁS | Brasil | 5212501 | 52 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 66c89f36-78ca-3746-aee7-db46b360446f | -16.34397 | -47.70867 | 2024-09-26 04:59:00 | NOAA-21 | LUZIÂNIA | GOIÁS | Brasil | 5212501 | 52 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 84f4486e-1864-3477-8e73-d92f7cd40d09 | -15.32416 | -47.46888 | 2024-09-26 04:59:00 | NOAA-21 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| e377076e-4ea8-301a-b20a-19c40998d24f | -15.32367 | -47.47326 | 2024-09-26 04:59:00 | NOAA-21 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 536e2773-e6f6-3575-8014-8bc2e33c8175 | -15.23399 | -48.03306 | 2024-09-26 04:59:00 | NOAA-21 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 6.2 |
| d6494d34-100d-34d9-823d-635693999fda | -15.23196 | -48.03138 | 2024-09-26 04:59:00 | NOAA-21 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| f63aa0b0-0610-37b7-a536-831878f3ab3e | -15.23125 | -48.03712 | 2024-09-26 04:59:00 | NOAA-21 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 0e5f1ef8-b0fe-3d4e-af5c-c67dd57d21d4 | -15.23038 | -48.27634 | 2024-09-26 04:59:00 | NOAA-21 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 93dae48d-feda-34b3-8420-32262f54c95c | -15.21 | -47.96483 | 2024-09-26 04:59:00 | NOAA-21 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| b7b25213-3077-36fe-a6cb-5ffbda413786 | -15.20434 | -47.97012 | 2024-09-26 04:59:00 | NOAA-21 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 58037dc6-844b-3b6b-9469-7f0b79c92590 | -15.02769 | -51.34886 | 2024-09-26 04:59:00 | NOAA-21 | BRITÂNIA | GOIÁS | Brasil | 5203807 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 768afb05-c5b5-3df2-8f7f-1a229bcfff41 | -11.72405 | -47.86114 | 2024-09-26 04:59:00 | NOAA-21 | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 487741e0-24f3-353a-84c6-41cc8b300f8e | -11.72318 | -47.85891 | 2024-09-26 04:59:00 | NOAA-21 | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 36fc1caf-1364-3943-80ca-e936ca52f0af | -11.7193 | -47.86054 | 2024-09-26 04:59:00 | NOAA-21 | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 5.7 |
| b725a2f4-e1a0-3c65-b690-c75682da7cd4 | -11.71843 | -47.85832 | 2024-09-26 04:59:00 | NOAA-21 | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 5.1 |
| c5739ed4-2cd6-39be-9c86-2fde8dbb8d48 | -11.71775 | -47.86344 | 2024-09-26 04:59:00 | NOAA-21 | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| db2420a6-9508-3e95-be20-8da2209a96b4 | -11.71506 | -47.84739 | 2024-09-26 04:59:00 | NOAA-21 | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 99a734e4-675d-36cb-9b29-8e9be2e721a6 | -11.71455 | -47.85994 | 2024-09-26 04:59:00 | NOAA-21 | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 55996386-a83b-364a-b6c3-30626d685c76 | -11.71369 | -47.85772 | 2024-09-26 04:59:00 | NOAA-21 | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 2a7a2106-f50a-33bd-8bce-42be962da9b9 | -11.71301 | -47.86284 | 2024-09-26 04:59:00 | NOAA-21 | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 99ba2ff4-234b-395a-8ca4-eed54f1789d4 | -11.71031 | -47.84676 | 2024-09-26 04:59:00 | NOAA-21 | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| c3c78826-3cac-3a42-8964-549aa36d9752 | -11.70895 | -47.85706 | 2024-09-26 04:59:00 | NOAA-21 | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 1bdc7c5b-8836-3193-a5d5-b9c6fa673ec3 | -11.70827 | -47.86218 | 2024-09-26 04:59:00 | NOAA-21 | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 9108e8b9-0d75-37e3-8191-75d2f46f25a4 | -11.70354 | -47.86151 | 2024-09-26 04:59:00 | NOAA-21 | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| a45f62f0-60cc-39fc-83e5-8b365b43e3d9 | -13.40205 | -48.91332 | 2024-09-26 04:59:00 | NOAA-21 | SANTA TEREZA DE GOIÁS | GOIÁS | Brasil | 5219605 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 605023e8-f06c-330c-9e60-4c3831619522 | -13.14246 | -48.54099 | 2024-09-26 04:59:00 | NOAA-21 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| b7ae9dde-404e-3c9f-b574-cecd164f4a01 | -13.1419 | -48.54522 | 2024-09-26 04:59:00 | NOAA-21 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 5a4c83f9-e101-3fdb-8796-9d63735c92cf | -13.14172 | -48.54203 | 2024-09-26 04:59:00 | NOAA-21 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 4.2 |
| e2bb4891-b34e-3477-ae56-5eaaa8430785 | -13.14133 | -48.54952 | 2024-09-26 04:59:00 | NOAA-21 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| e4cd94ba-8e4f-3076-bffd-1c21ab2f3ed1 | -13.14119 | -48.54626 | 2024-09-26 04:59:00 | NOAA-21 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 04965fb4-ecd5-32a5-b98d-5f021be91fde | -13.13674 | -48.54872 | 2024-09-26 04:59:00 | NOAA-21 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 10a76f2b-b679-3bd7-b630-c48b2a9abf2a | -13.13605 | -48.5498 | 2024-09-26 04:59:00 | NOAA-21 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 5e6754a5-5825-39ae-a4bc-c5a893a78229 | -12.71684 | -48.42954 | 2024-09-26 04:59:00 | NOAA-21 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 898a0b12-69d8-3869-a8a8-56a560575ada | -12.51212 | -48.92524 | 2024-09-26 04:59:00 | NOAA-21 | TALISMÃ | TOCANTINS | Brasil | 1720978 | 17 | 33 | nan | nan | nan | Cerrado | 26.7 |
| d3a55215-0185-3656-81a2-8c3723e605fb | -12.51153 | -48.9297 | 2024-09-26 04:59:00 | NOAA-21 | TALISMÃ | TOCANTINS | Brasil | 1720978 | 17 | 33 | nan | nan | nan | Cerrado | 26.7 |
| 8f7a46ba-0555-359f-ba87-08445ccac227 | -12.51094 | -48.93419 | 2024-09-26 04:59:00 | NOAA-21 | TALISMÃ | TOCANTINS | Brasil | 1720978 | 17 | 33 | nan | nan | nan | Cerrado | 21.4 |
| a21e9821-83fe-375c-b869-12603908d4e8 | -12.50826 | -48.92014 | 2024-09-26 04:59:00 | NOAA-21 | TALISMÃ | TOCANTINS | Brasil | 1720978 | 17 | 33 | nan | nan | nan | Cerrado | 8.4 |
| 0aed691f-441b-39e0-b990-95af7a17e997 | -12.50767 | -48.92461 | 2024-09-26 04:59:00 | NOAA-21 | TALISMÃ | TOCANTINS | Brasil | 1720978 | 17 | 33 | nan | nan | nan | Cerrado | 15.2 |
| ea192f1e-ff48-39e4-8d2a-005fb545425e | -12.50708 | -48.92907 | 2024-09-26 04:59:00 | NOAA-21 | TALISMÃ | TOCANTINS | Brasil | 1720978 | 17 | 33 | nan | nan | nan | Cerrado | 15.2 |
| 0c922e0d-a347-3d4b-bd67-f4b0f6903965 | -12.5044 | -48.915 | 2024-09-26 04:59:00 | NOAA-21 | TALISMÃ | TOCANTINS | Brasil | 1720978 | 17 | 33 | nan | nan | nan | Cerrado | 8.4 |
| f4f29e39-06e8-3c0f-b824-a00356c83398 | -12.50381 | -48.91948 | 2024-09-26 04:59:00 | NOAA-21 | TALISMÃ | TOCANTINS | Brasil | 1720978 | 17 | 33 | nan | nan | nan | Cerrado | 8.4 |
| 236c7801-67d4-342b-94c6-68bd341d1963 | -12.50322 | -48.92397 | 2024-09-26 04:59:00 | NOAA-21 | TALISMÃ | TOCANTINS | Brasil | 1720978 | 17 | 33 | nan | nan | nan | Cerrado | 15.2 |
| c6259856-0a5c-31b6-90ca-47a77301b1a8 | -12.50263 | -48.92845 | 2024-09-26 04:59:00 | NOAA-21 | TALISMÃ | TOCANTINS | Brasil | 1720978 | 17 | 33 | nan | nan | nan | Cerrado | 15.2 |
| f956e6eb-2c28-372d-b482-331c3011727a | -12.49935 | -48.91884 | 2024-09-26 04:59:00 | NOAA-21 | TALISMÃ | TOCANTINS | Brasil | 1720978 | 17 | 33 | nan | nan | nan | Cerrado | 9.9 |
| 414d5b4b-6353-3e94-a0fa-d47a5ce09544 | -12.49876 | -48.92333 | 2024-09-26 04:59:00 | NOAA-21 | TALISMÃ | TOCANTINS | Brasil | 1720978 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| bbfced69-b2af-3b31-9c41-a0eee0831afd | -12.27678 | -49.20842 | 2024-09-26 04:59:00 | NOAA-21 | ALVORADA | TOCANTINS | Brasil | 1700707 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 40039b94-78c2-3341-87e4-8c4ab9dacbfb | -12.9782 | -49.33768 | 2024-09-26 04:59:00 | NOAA-21 | ARAGUAÇU | TOCANTINS | Brasil | 1702000 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 4f7c617a-fc2b-38c4-b3b1-91202f5b010e | -14.83735 | -48.90946 | 2024-09-26 04:59:00 | NOAA-21 | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 512425d2-466f-381d-baef-4c296a8737fb | -14.83698 | -48.87413 | 2024-09-26 04:59:00 | NOAA-21 | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| cba1bf70-d72e-3593-881a-1025522f897c | -14.83682 | -48.91375 | 2024-09-26 04:59:00 | NOAA-21 | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 2e24cd59-bb1a-39b7-b26d-40bbded5e39d | -14.82809 | -48.90863 | 2024-09-26 04:59:00 | NOAA-21 | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 51b05848-6c23-3023-a942-d06f3f4b9d44 | -14.81755 | -48.84795 | 2024-09-26 04:59:00 | NOAA-21 | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| f7322c81-91bb-31e4-b89f-9b186f3698ce | -14.81698 | -48.84509 | 2024-09-26 04:59:00 | NOAA-21 | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| e0176936-46ad-3574-acb7-1a6c39455b36 | -14.81358 | -48.84219 | 2024-09-26 04:59:00 | NOAA-21 | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 3.4 |
| fde48b71-f966-3f7b-8041-f236e726569a | -14.81297 | -48.83927 | 2024-09-26 04:59:00 | NOAA-21 | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 3b20b7b4-94be-3788-b795-2678cd606178 | -14.80961 | -48.83633 | 2024-09-26 04:59:00 | NOAA-21 | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 105b0f24-8a77-3186-83a3-3eb412e0b001 | -14.78555 | -48.87777 | 2024-09-26 04:59:00 | NOAA-21 | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 7fd74e73-05c0-3f52-8499-f615713a03ae | -14.78491 | -48.88283 | 2024-09-26 04:59:00 | NOAA-21 | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 7ca06dad-c2bd-3da0-bd0a-5d13097d817b | -14.78368 | -48.89255 | 2024-09-26 04:59:00 | NOAA-21 | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 791d7856-b18a-32cf-a32b-703cd37b4352 | -14.77969 | -48.88702 | 2024-09-26 04:59:00 | NOAA-21 | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 1e9b4966-3944-3f3c-9a6c-c2737cb9b080 | -14.64699 | -48.71066 | 2024-09-26 04:59:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| cdf639cc-0550-3b61-94b3-d0ea294fc5d4 | -14.64638 | -48.71566 | 2024-09-26 04:59:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 42982239-6bca-313b-be6a-1ffa1bcb1a80 | -14.63707 | -48.71432 | 2024-09-26 04:59:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| ad30b350-ca8c-359d-a84f-4dc44ea121df | -14.63424 | -48.71281 | 2024-09-26 04:59:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| b85ba7c7-fefa-3b6b-a8f2-4f31256271f1 | -15.17586 | -48.81212 | 2024-09-26 04:59:00 | NOAA-21 | VILA PROPÍCIO | GOIÁS | Brasil | 5222302 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 830dfb2d-4172-3b6f-8946-9f1264704828 | -15.15672 | -48.7741 | 2024-09-26 04:59:00 | NOAA-21 | VILA PROPÍCIO | GOIÁS | Brasil | 5222302 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| f6da23e7-9fb0-3c1d-8a8f-9fbc9d73f922 | -15.15611 | -48.77921 | 2024-09-26 04:59:00 | NOAA-21 | VILA PROPÍCIO | GOIÁS | Brasil | 5222302 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| e5139915-0f49-325d-9bb3-b366973410e3 | -15.03026 | -49.91411 | 2024-09-26 04:59:00 | NOAA-21 | NOVA AMÉRICA | GOIÁS | Brasil | 5214705 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 0681069a-35e5-3e22-aeb6-d3c9eb21625e | -15.02974 | -49.91823 | 2024-09-26 04:59:00 | NOAA-21 | NOVA AMÉRICA | GOIÁS | Brasil | 5214705 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 1cfc1cd1-14f2-3e61-8a35-1edeac635966 | -16.7123 | -48.91462 | 2024-09-26 04:59:00 | NOAA-21 | CALDAZINHA | GOIÁS | Brasil | 5204557 | 52 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 9289a2e2-e583-3964-8dca-25bf95282132 | -16.71165 | -48.91999 | 2024-09-26 04:59:00 | NOAA-21 | CALDAZINHA | GOIÁS | Brasil | 5204557 | 52 | 33 | nan | nan | nan | Cerrado | 9.5 |
| 4543a2a4-1cbe-3150-89f8-eee7140b9814 | -16.68491 | -49.14067 | 2024-09-26 04:59:00 | NOAA-21 | SENADOR CANEDO | GOIÁS | Brasil | 5220454 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 847bb381-c2a4-35e9-8afb-10762cf8340e | -16.45945 | -49.03563 | 2024-09-26 04:59:00 | NOAA-21 | GOIANÁPOLIS | GOIÁS | Brasil | 5208400 | 52 | 33 | nan | nan | nan | Cerrado | 4.4 |
| e13465cc-4404-3ee7-a05e-3798a797756e | -16.36286 | -49.93308 | 2024-09-26 04:59:00 | NOAA-21 | ANICUNS | GOIÁS | Brasil | 5201306 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| a8390b47-036b-3194-b637-1c33cd1c9c39 | -16.35847 | -49.93249 | 2024-09-26 04:59:00 | NOAA-21 | ANICUNS | GOIÁS | Brasil | 5201306 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| e83455f8-5dcf-320f-ab79-d21f96517229 | -10.80225 | -50.11672 | 2024-09-26 04:59:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| b40cd14a-d7c6-306d-8530-e933e1d27f69 | -10.79823 | -50.11612 | 2024-09-26 04:59:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |


[Clique aqui para ver as próximas entradas](README115.md)
