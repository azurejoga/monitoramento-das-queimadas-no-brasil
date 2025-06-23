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

## Dados Diários - Página 1

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| f27e5ba5-add3-3870-a586-74dceccff637 | -11.617 | -58.289 | 2025-06-23 00:00:00 | GOES-19 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 143.4 |
| 0691d625-dcb4-322a-8adf-a2087faa51aa | -13.2343 | -49.8475 | 2025-06-23 00:00:00 | GOES-19 | SÃO MIGUEL DO ARAGUAIA | GOIÁS | Brasil | 5220207 | 52 | 33 | nan | nan | nan | Cerrado | 74.4 |
| c164d19d-6255-39b6-821b-66e13c9b23f9 | -11.6359 | -58.2876 | 2025-06-23 00:00:00 | GOES-19 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 89.5 |
| 05674ef6-572c-3a5d-a74b-25294cd44ab9 | -17.3844 | -42.6235 | 2025-06-23 00:00:00 | GOES-19 | TURMALINA | MINAS GERAIS | Brasil | 3169703 | 31 | 33 | nan | nan | nan | Cerrado | 72.8 |
| b662372a-1351-398e-9fa2-bb179ab499f4 | -11.6172 | -58.2693 | 2025-06-23 00:00:00 | GOES-19 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 82.4 |
| 9d35cb74-2ff6-3253-a4bf-1da9f2b8f3c6 | -17.4045 | -42.6186 | 2025-06-23 00:00:00 | GOES-19 | TURMALINA | MINAS GERAIS | Brasil | 3169703 | 31 | 33 | nan | nan | nan | Cerrado | 77.5 |
| 526c86fa-c1fb-35fd-9def-855b2b4f5268 | -13.2346 | -49.8258 | 2025-06-23 00:00:00 | GOES-19 | SÃO MIGUEL DO ARAGUAIA | GOIÁS | Brasil | 5220207 | 52 | 33 | nan | nan | nan | Cerrado | 71.5 |
| 8cf310d4-8797-3052-b369-52a2ed201fb6 | -11.617 | -58.289 | 2025-06-23 00:10:00 | GOES-19 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 104.5 |
| 097f1da4-7286-3881-a10e-e0c4327d9785 | -11.5812 | -44.6554 | 2025-06-23 00:10:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 40.5 |
| ba2223a9-a585-3992-be08-f56cd1c800b5 | -11.6172 | -58.2693 | 2025-06-23 00:10:00 | GOES-19 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 66.6 |
| 0ea6157e-d532-3365-9c3f-918401024e2f | -13.2539 | -49.8232 | 2025-06-23 00:10:00 | GOES-19 | NOVO PLANALTO | GOIÁS | Brasil | 5215256 | 52 | 33 | nan | nan | nan | Cerrado | 50.8 |
| 019333ea-c0c8-3e4f-a70c-ad22cf1b371b | -13.2346 | -49.8258 | 2025-06-23 00:10:00 | GOES-19 | SÃO MIGUEL DO ARAGUAIA | GOIÁS | Brasil | 5220207 | 52 | 33 | nan | nan | nan | Cerrado | 57.9 |
| 45a2ec9d-19f7-36c2-9e6c-df8df888676f | -17.4045 | -42.6186 | 2025-06-23 00:10:00 | GOES-19 | TURMALINA | MINAS GERAIS | Brasil | 3169703 | 31 | 33 | nan | nan | nan | Cerrado | 100.6 |
| 2ba50e01-bd27-3aa2-95d5-618aabccdec7 | -8.0703 | -43.0981 | 2025-06-23 00:10:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 41.3 |
| 81ef29b7-b97b-3fda-ae23-3695d3fb3dea | -13.2535 | -49.845 | 2025-06-23 00:10:00 | GOES-19 | SÃO MIGUEL DO ARAGUAIA | GOIÁS | Brasil | 5220207 | 52 | 33 | nan | nan | nan | Cerrado | 53.5 |
| 955758d1-58c2-3926-8a30-eeb633c409ea | -8.07 | -43.1216 | 2025-06-23 00:10:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 45.4 |
| 6d515c77-6e5d-3031-ab3b-c64dda943839 | -11.6359 | -58.2876 | 2025-06-23 00:10:00 | GOES-19 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 68.2 |
| db101ba9-57b1-3bef-95a0-a00579de0818 | -13.2343 | -49.8475 | 2025-06-23 00:10:00 | GOES-19 | SÃO MIGUEL DO ARAGUAIA | GOIÁS | Brasil | 5220207 | 52 | 33 | nan | nan | nan | Cerrado | 60.6 |
| 6aef484b-de64-37cd-84b2-14caf3672318 | -17.3844 | -42.6235 | 2025-06-23 00:10:00 | GOES-19 | TURMALINA | MINAS GERAIS | Brasil | 3169703 | 31 | 33 | nan | nan | nan | Cerrado | 100.1 |
| 1c45bb7f-090b-3197-8411-fbff5212c176 | -11.6359 | -58.2876 | 2025-06-23 00:20:00 | GOES-19 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 65.1 |
| 1c4b8d2c-636c-34c0-83e0-53f1f729c732 | -17.4038 | -42.6435 | 2025-06-23 00:20:00 | GOES-19 | TURMALINA | MINAS GERAIS | Brasil | 3169703 | 31 | 33 | nan | nan | nan | Cerrado | 54.3 |
| 2443383e-3c48-3aae-b2dc-b4d8c24e024b | -11.617 | -58.289 | 2025-06-23 00:20:00 | GOES-19 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 99.2 |
| 200e4608-dd03-30b0-92b3-9909dcd20ab7 | -17.3844 | -42.6235 | 2025-06-23 00:20:00 | GOES-19 | TURMALINA | MINAS GERAIS | Brasil | 3169703 | 31 | 33 | nan | nan | nan | Cerrado | 100.8 |
| 94247466-0fdd-39ec-a596-98dbb00e294d | -8.0703 | -43.0981 | 2025-06-23 00:20:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 46.4 |
| 6e7bc006-f85b-3d2d-a9d4-c759485f9e22 | -8.07 | -43.1216 | 2025-06-23 00:20:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 48.2 |
| ee98a496-08a0-3613-b440-6cdd2d962472 | -13.2346 | -49.8258 | 2025-06-23 00:20:00 | GOES-19 | SÃO MIGUEL DO ARAGUAIA | GOIÁS | Brasil | 5220207 | 52 | 33 | nan | nan | nan | Cerrado | 63.4 |
| ea6170ce-aa86-36a8-b20e-0beeff7ddb19 | -17.3837 | -42.6483 | 2025-06-23 00:20:00 | GOES-19 | TURMALINA | MINAS GERAIS | Brasil | 3169703 | 31 | 33 | nan | nan | nan | Cerrado | 54.9 |
| be546891-29cf-3019-bfc4-73310d5a3e22 | -13.2343 | -49.8475 | 2025-06-23 00:20:00 | GOES-19 | SÃO MIGUEL DO ARAGUAIA | GOIÁS | Brasil | 5220207 | 52 | 33 | nan | nan | nan | Cerrado | 50.9 |
| 8433b239-7306-3450-996c-46ea968c3237 | -17.4045 | -42.6186 | 2025-06-23 00:20:00 | GOES-19 | TURMALINA | MINAS GERAIS | Brasil | 3169703 | 31 | 33 | nan | nan | nan | Cerrado | 103.0 |
| 9001fc36-5bc1-3fbc-b0d6-3f6588135f1e | -11.6172 | -58.2693 | 2025-06-23 00:30:00 | GOES-19 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 76.6 |
| a8ad23b7-774a-30f6-89e6-69ad3e1ddb72 | -17.3844 | -42.6235 | 2025-06-23 00:30:00 | GOES-19 | TURMALINA | MINAS GERAIS | Brasil | 3169703 | 31 | 33 | nan | nan | nan | Cerrado | 123.3 |
| 86d9eae3-eef7-3ed8-8c94-42d64ee6537d | -11.6359 | -58.2876 | 2025-06-23 00:30:00 | GOES-19 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 69.0 |
| ff245423-c0e0-3707-bb87-3ebdd7c7f985 | -17.3837 | -42.6483 | 2025-06-23 00:30:00 | GOES-19 | TURMALINA | MINAS GERAIS | Brasil | 3169703 | 31 | 33 | nan | nan | nan | Cerrado | 52.4 |
| acf6d48e-fe31-3cce-acc3-28ebc9000785 | -11.617 | -58.289 | 2025-06-23 00:30:00 | GOES-19 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 145.8 |
| b1276843-26e0-316a-abf9-db99f0cc94c9 | -17.4038 | -42.6435 | 2025-06-23 00:30:00 | GOES-19 | TURMALINA | MINAS GERAIS | Brasil | 3169703 | 31 | 33 | nan | nan | nan | Cerrado | 53.9 |
| 379737ef-9ec8-3379-9441-523327aed79b | -17.4045 | -42.6186 | 2025-06-23 00:30:00 | GOES-19 | TURMALINA | MINAS GERAIS | Brasil | 3169703 | 31 | 33 | nan | nan | nan | Cerrado | 131.1 |
| 379c42eb-07ff-32b3-b434-b87734962917 | -13.2343 | -49.8475 | 2025-06-23 00:40:00 | GOES-19 | SÃO MIGUEL DO ARAGUAIA | GOIÁS | Brasil | 5220207 | 52 | 33 | nan | nan | nan | Cerrado | 52.1 |
| 10b389ba-9991-31f5-afe6-53d3c6212e08 | -13.2346 | -49.8258 | 2025-06-23 00:40:00 | GOES-19 | SÃO MIGUEL DO ARAGUAIA | GOIÁS | Brasil | 5220207 | 52 | 33 | nan | nan | nan | Cerrado | 54.5 |
| 465dc5f9-339f-3869-b42f-b6d13e7494c4 | -17.3844 | -42.6235 | 2025-06-23 00:40:00 | GOES-19 | TURMALINA | MINAS GERAIS | Brasil | 3169703 | 31 | 33 | nan | nan | nan | Cerrado | 129.8 |
| 9d32bb2f-d732-3b8a-952a-c2af0ebec7fc | -11.6172 | -58.2693 | 2025-06-23 00:40:00 | GOES-19 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 68.8 |
| 59ac4eea-7ea8-37ed-9df2-a0c948a8c1b3 | -17.3837 | -42.6483 | 2025-06-23 00:40:00 | GOES-19 | TURMALINA | MINAS GERAIS | Brasil | 3169703 | 31 | 33 | nan | nan | nan | Cerrado | 68.1 |
| 4a5d54c2-530c-3223-960c-86e36fa92279 | -17.4038 | -42.6435 | 2025-06-23 00:40:00 | GOES-19 | TURMALINA | MINAS GERAIS | Brasil | 3169703 | 31 | 33 | nan | nan | nan | Cerrado | 59.8 |
| 8103932d-f526-30cf-a24f-a3db101f793d | -11.6359 | -58.2876 | 2025-06-23 00:40:00 | GOES-19 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 74.9 |
| 83d02b78-ab41-397d-bfc9-47fdc7a3e12a | -17.4045 | -42.6186 | 2025-06-23 00:40:00 | GOES-19 | TURMALINA | MINAS GERAIS | Brasil | 3169703 | 31 | 33 | nan | nan | nan | Cerrado | 118.0 |
| a125693e-f858-31d8-be7b-93bf3e452753 | -8.0703 | -43.0981 | 2025-06-23 00:40:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 70.0 |
| fd6d353a-8394-30ab-aded-c90d709c9cd5 | -8.07 | -43.1216 | 2025-06-23 00:40:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 71.3 |
| e25373b8-4ac3-38bf-a8ec-0fe6d3fb6561 | -11.617 | -58.289 | 2025-06-23 00:40:00 | GOES-19 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 117.1 |
| 3068735f-a973-37c3-af25-f4969bd6ad77 | -11.6172 | -58.2693 | 2025-06-23 00:50:00 | GOES-19 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 63.8 |
| 8e4b7e34-0570-3dad-b9f6-6bdb3e866401 | -17.3837 | -42.6483 | 2025-06-23 00:50:00 | GOES-19 | TURMALINA | MINAS GERAIS | Brasil | 3169703 | 31 | 33 | nan | nan | nan | Cerrado | 73.2 |
| 80b1888b-534e-3145-ad6d-5ec0a726eba6 | -11.617 | -58.289 | 2025-06-23 00:50:00 | GOES-19 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 115.5 |
| b553cc42-8978-366a-b231-e75d31318cbb | -11.6359 | -58.2876 | 2025-06-23 00:50:00 | GOES-19 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 77.0 |
| ba838402-43de-3daf-a28c-6d82560f5c8e | -8.07 | -43.1216 | 2025-06-23 00:50:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 83.4 |
| 89eb8fad-4bf4-3b18-af73-53edefb61f9d | -17.3844 | -42.6235 | 2025-06-23 00:50:00 | GOES-19 | TURMALINA | MINAS GERAIS | Brasil | 3169703 | 31 | 33 | nan | nan | nan | Cerrado | 136.1 |
| 251b221f-774a-36b0-bc0e-4e676858d78a | -8.0703 | -43.0981 | 2025-06-23 00:50:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 76.4 |
| 7d63238e-4a8f-3e17-be7c-c530c6e6d2da | -13.2346 | -49.8258 | 2025-06-23 00:50:00 | GOES-19 | SÃO MIGUEL DO ARAGUAIA | GOIÁS | Brasil | 5220207 | 52 | 33 | nan | nan | nan | Cerrado | 53.0 |
| 04552c61-8fed-38ad-a231-d694e3815f02 | -17.4045 | -42.6186 | 2025-06-23 00:50:00 | GOES-19 | TURMALINA | MINAS GERAIS | Brasil | 3169703 | 31 | 33 | nan | nan | nan | Cerrado | 121.6 |
| a994fb07-8e73-3d16-ad2a-1da57d088d24 | -17.4038 | -42.6435 | 2025-06-23 00:50:00 | GOES-19 | TURMALINA | MINAS GERAIS | Brasil | 3169703 | 31 | 33 | nan | nan | nan | Cerrado | 63.7 |
| 50057b50-1d8a-3cb1-ae5e-c371d69be8fd | -22.25122 | -50.0384 | 2025-06-23 00:56:00 | TERRA_M-M | MARÍLIA | SÃO PAULO | Brasil | 3529005 | 35 | 33 | nan | nan | nan | Mata Atlântica | 16.5 |
| d4d2742e-0224-3467-8578-6432bed56bae | -22.26011 | -50.03685 | 2025-06-23 00:56:00 | TERRA_M-M | MARÍLIA | SÃO PAULO | Brasil | 3529005 | 35 | 33 | nan | nan | nan | Mata Atlântica | 10.3 |
| dae15b42-3c4a-3aaa-ab27-f3ecb49bfec1 | -22.2526 | -50.048 | 2025-06-23 00:56:00 | TERRA_M-M | MARÍLIA | SÃO PAULO | Brasil | 3529005 | 35 | 33 | nan | nan | nan | Mata Atlântica | 6.8 |
| 3bc0b373-7f94-3a2c-a2d9-9dc90eb7bd24 | -17.3902 | -42.63769 | 2025-06-23 00:58:00 | TERRA_M-M | TURMALINA | MINAS GERAIS | Brasil | 3169703 | 31 | 33 | nan | nan | nan | Cerrado | 245.2 |
| a181623c-e2c8-38d5-8f77-14cb5ba4e73f | -17.38514 | -42.63219 | 2025-06-23 00:58:00 | TERRA_M-M | TURMALINA | MINAS GERAIS | Brasil | 3169703 | 31 | 33 | nan | nan | nan | Cerrado | 173.9 |
| 41ea323b-ab06-3dc3-b18e-89b8766a4242 | -17.39127 | -42.66421 | 2025-06-23 00:58:00 | TERRA_M-M | TURMALINA | MINAS GERAIS | Brasil | 3169703 | 31 | 33 | nan | nan | nan | Cerrado | 37.3 |
| 5b855155-9991-3996-a928-bca0e5c7bdc2 | -16.98738 | -50.24648 | 2025-06-23 00:58:00 | TERRA_M-M | JANDAIA | GOIÁS | Brasil | 5211701 | 52 | 33 | nan | nan | nan | Cerrado | 12.8 |
| 49d57a9c-ff99-3492-b204-46a0b43d5386 | -19.69974 | -54.60879 | 2025-06-23 00:58:00 | TERRA_M-M | BANDEIRANTES | MATO GROSSO DO SUL | Brasil | 5001508 | 50 | 33 | nan | nan | nan | Cerrado | 13.4 |
| e50183ce-8bb2-3cf1-a0d1-dc547eec927c | -17.40061 | -42.6289 | 2025-06-23 00:58:00 | TERRA_M-M | TURMALINA | MINAS GERAIS | Brasil | 3169703 | 31 | 33 | nan | nan | nan | Cerrado | 156.4 |
| 8c362ecc-4ab4-3aab-aaf9-80e7dfde6974 | -8.0703 | -43.0981 | 2025-06-23 01:00:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 68.7 |
| a845c340-87f6-3027-aae3-b07f5acbd0fa | -11.6359 | -58.2876 | 2025-06-23 01:00:00 | GOES-19 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 68.7 |
| 9dcae064-244c-3b34-b6ef-da30a286467d | -17.3844 | -42.6235 | 2025-06-23 01:00:00 | GOES-19 | TURMALINA | MINAS GERAIS | Brasil | 3169703 | 31 | 33 | nan | nan | nan | Cerrado | 125.7 |
| dd23d660-ec79-35b0-b62c-242fedc458a6 | -11.617 | -58.289 | 2025-06-23 01:00:00 | GOES-19 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 144.8 |
| 9a878c0f-12c9-33b7-b57b-e2a1f5fb0d67 | -17.3837 | -42.6483 | 2025-06-23 01:00:00 | GOES-19 | TURMALINA | MINAS GERAIS | Brasil | 3169703 | 31 | 33 | nan | nan | nan | Cerrado | 51.7 |
| f86e95e6-070c-3b52-baea-137b0bc0a1c6 | -17.4038 | -42.6435 | 2025-06-23 01:00:00 | GOES-19 | TURMALINA | MINAS GERAIS | Brasil | 3169703 | 31 | 33 | nan | nan | nan | Cerrado | 70.5 |
| b06f1ed9-82e3-3398-9416-1ec8ac148014 | -17.4045 | -42.6186 | 2025-06-23 01:00:00 | GOES-19 | TURMALINA | MINAS GERAIS | Brasil | 3169703 | 31 | 33 | nan | nan | nan | Cerrado | 172.0 |
| aaeb2091-68c0-388e-a30d-f55d13755183 | -11.95156 | -58.74001 | 2025-06-23 01:00:00 | TERRA_M-M | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 23.6 |
| 1deb885d-f550-3f4a-ae48-ababeea96e18 | -11.6239 | -58.27591 | 2025-06-23 01:00:00 | TERRA_M-M | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 49.4 |
| 91a1f29e-d69d-3406-b610-44a6255da084 | -11.58744 | -44.6548 | 2025-06-23 01:00:00 | TERRA_M-M | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 26.8 |
| df42cb1f-44c0-30d6-9b75-78b20f3105e1 | -11.61443 | -58.29295 | 2025-06-23 01:00:00 | TERRA_M-M | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 73.2 |
| 7518e037-b674-34aa-8499-5552bdff5b90 | -11.62587 | -58.29143 | 2025-06-23 01:00:00 | TERRA_M-M | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 64.4 |
| 016f12c9-5ac6-3aa7-98c1-d35786cac48c | -12.11528 | -54.6703 | 2025-06-23 01:00:00 | TERRA_M-M | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 6.4 |
| f5a2d67a-a532-3d81-a48c-1ff1917807ca | -11.18651 | -54.40251 | 2025-06-23 01:00:00 | TERRA_M-M | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 9.4 |
| 517c3295-b0da-3609-add7-90622fbf48d7 | -11.95776 | -58.74491 | 2025-06-23 01:00:00 | TERRA_M-M | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 13.3 |
| dfc15e1e-341f-3f0d-ad84-100b4d87ad7e | -12.19425 | -49.62251 | 2025-06-23 01:00:00 | TERRA_M-M | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 7.7 |
| a4fb3950-019b-37ed-8ece-5078041a5fd8 | -10.1471 | -48.99086 | 2025-06-23 01:00:00 | TERRA_M-M | PARAÍSO DO TOCANTINS | TOCANTINS | Brasil | 1716109 | 17 | 33 | nan | nan | nan | Cerrado | 11.2 |
| 65db4007-89a2-360c-84c6-b9f4b7f48caf | -11.18777 | -54.41176 | 2025-06-23 01:00:00 | TERRA_M-M | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 7.6 |
| 3f1c3447-09cf-3134-b603-2b64d25fb978 | -13.24282 | -49.83786 | 2025-06-23 01:00:00 | TERRA_M-M | SÃO MIGUEL DO ARAGUAIA | GOIÁS | Brasil | 5220207 | 52 | 33 | nan | nan | nan | Cerrado | 134.1 |
| 0a60fc6d-92fd-3d6d-9c2f-848a767c67bc | -11.91374 | -54.81852 | 2025-06-23 01:00:00 | TERRA_M-M | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 8.1 |
| 516d6744-2433-3230-ad35-e0870fd231f0 | -13.08712 | -54.85109 | 2025-06-23 01:00:00 | TERRA_M-M | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 22.3 |
| 06597848-3446-3e91-b471-3431e0f49299 | -11.62367 | -58.28539 | 2025-06-23 01:00:00 | TERRA_M-M | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 164.7 |
| 0acf3b14-e753-3e89-9fde-692c78019306 | -11.14198 | -53.94365 | 2025-06-23 01:00:00 | TERRA_M-M | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 9.2 |
| 6c698514-cee4-3da6-b439-6b6372cae88f | -13.08581 | -54.84119 | 2025-06-23 01:00:00 | TERRA_M-M | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 12.2 |
| 94e486e8-473a-3162-a26d-6cf56b50aa4e | -11.14073 | -53.93461 | 2025-06-23 01:00:00 | TERRA_M-M | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 31e55579-aeda-3351-be2f-8adaf392d65e | -11.61248 | -58.27745 | 2025-06-23 01:00:00 | TERRA_M-M | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 35.4 |
| c4396e14-3c45-3d3a-b5cd-c3bc3990d872 | -11.57247 | -44.65757 | 2025-06-23 01:00:00 | TERRA_M-M | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 33.8 |
| 5a973cf6-4439-382a-83a6-54aa9e0899c6 | -11.61223 | -58.28697 | 2025-06-23 01:00:00 | TERRA_M-M | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 73.1 |
| adb17d0d-6e20-34fc-8f2b-096f52f26f72 | -11.58574 | -44.64978 | 2025-06-23 01:00:00 | TERRA_M-M | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 33.5 |
| f3d7b67c-e225-3574-906e-549fa6e3d306 | -13.24109 | -49.82658 | 2025-06-23 01:00:00 | TERRA_M-M | SÃO MIGUEL DO ARAGUAIA | GOIÁS | Brasil | 5220207 | 52 | 33 | nan | nan | nan | Cerrado | 9.6 |
| 515f0c11-ca32-3d3a-ad29-1bc96f093a8b | -13.64606 | -53.93795 | 2025-06-23 01:00:00 | TERRA_M-M | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Cerrado | 4.8 |
| b4efc099-b39a-3031-bbc8-08402cb765aa | -11.62553 | -58.30104 | 2025-06-23 01:00:00 | TERRA_M-M | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 17.5 |
| a7c2c567-d0fe-3cc8-ad85-c3d7bf5b4953 | -13.07787 | -54.85241 | 2025-06-23 01:00:00 | TERRA_M-M | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 6fcf26fb-80bb-3d10-b86d-8869f5b5dee4 | -9.42104 | -48.40998 | 2025-06-23 01:02:00 | TERRA_M-M | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 18.0 |


[Clique aqui para ver as próximas entradas](README2.md)
