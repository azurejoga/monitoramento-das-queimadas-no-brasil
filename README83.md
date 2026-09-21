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

## Dados Diários - Página 83

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| fae5bf74-dbce-3a01-bffb-83f2cc98648a | -16.03059 | -52.50597 | 2026-09-21 05:08:00 | NOAA-21 | PONTAL DO ARAGUAIA | MATO GROSSO | Brasil | 5106653 | 51 | 33 | nan | nan | nan | Cerrado | 12.0 |
| 3d61102e-0794-30c2-8d5e-d981b910dd61 | -15.61541 | -52.72671 | 2026-09-21 05:08:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 26f3d0d2-f688-30ea-bd30-9c62a8c8a0de | -15.44876 | -48.46134 | 2026-09-21 05:08:00 | NOAA-21 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 0e401f31-f949-381b-a7f9-4c0da1f54921 | -15.85813 | -49.90365 | 2026-09-21 05:08:00 | NOAA-21 | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 4223fdff-975c-305d-a068-7ed3cc97fbc8 | -14.04365 | -52.07374 | 2026-09-21 05:08:00 | NOAA-21 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 4.2 |
| ceb36970-0182-34c8-8796-29bf076fa96b | -14.05759 | -52.11102 | 2026-09-21 05:08:00 | NOAA-21 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 3.2 |
| b1b55966-2785-313a-bd5c-ae47b70ca52f | -15.46139 | -48.47653 | 2026-09-21 05:08:00 | NOAA-21 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 23e3368e-1c45-39d1-bf39-401526c0f82b | -15.46261 | -48.43486 | 2026-09-21 05:08:00 | NOAA-21 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 9824346b-46b0-3d24-ac5c-7be443307203 | -16.04101 | -52.52327 | 2026-09-21 05:08:00 | NOAA-21 | PONTAL DO ARAGUAIA | MATO GROSSO | Brasil | 5106653 | 51 | 33 | nan | nan | nan | Cerrado | 3.3 |
| afa629d9-823e-30ca-9a19-6d2908b85b89 | -15.45716 | -48.46568 | 2026-09-21 05:08:00 | NOAA-21 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| cf923d02-24a8-38f1-9793-6b086c87b781 | -16.0481 | -52.5147 | 2026-09-21 05:08:00 | NOAA-21 | PONTAL DO ARAGUAIA | MATO GROSSO | Brasil | 5106653 | 51 | 33 | nan | nan | nan | Cerrado | 19.1 |
| 36a589d5-4a5e-389b-8001-36100a67b8cb | -17.65997 | -49.88833 | 2026-09-21 05:08:00 | NOAA-21 | VICENTINÓPOLIS | GOIÁS | Brasil | 5222054 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| f85afe4a-5c73-33a8-b8b7-4c7a49d30403 | -15.45881 | -48.4699 | 2026-09-21 05:08:00 | NOAA-21 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 8384c7b4-8ad9-34cf-ac9b-78a35b516d6e | -16.10202 | -49.81708 | 2026-09-21 05:08:00 | NOAA-21 | ITABERAÍ | GOIÁS | Brasil | 5210406 | 52 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 4dc6ad74-bd0e-3088-a8bd-73908f2132d2 | -14.98113 | -53.96111 | 2026-09-21 05:08:00 | NOAA-21 | PRIMAVERA DO LESTE | MATO GROSSO | Brasil | 5107040 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 53310b04-aa65-3edd-8f96-581bf7e4784b | -18.37788 | -49.39793 | 2026-09-21 05:08:00 | NOAA-21 | ITUMBIARA | GOIÁS | Brasil | 5211503 | 52 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 805bb8ab-a672-3bed-aee9-7e274475e6ac | -14.64547 | -52.09217 | 2026-09-21 05:08:00 | NOAA-21 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 9957ad6a-408a-31bb-a495-45152cc697e7 | -14.6591 | -54.46164 | 2026-09-21 05:08:00 | NOAA-21 | PLANALTO DA SERRA | MATO GROSSO | Brasil | 5106455 | 51 | 33 | nan | nan | nan | Cerrado | 2.6 |
| ca579eee-bbe5-37c0-931c-648482ebe611 | -14.04836 | -52.0703 | 2026-09-21 05:08:00 | NOAA-21 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 34248d6f-2cab-34ce-87eb-62797823bf26 | -14.10178 | -52.12905 | 2026-09-21 05:08:00 | NOAA-21 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 866bd1c0-2a23-354a-8ddb-fe818d9ed673 | -15.46178 | -48.47317 | 2026-09-21 05:08:00 | NOAA-21 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 66d004b2-d038-3f1c-98df-a8772690add7 | -15.45843 | -48.47338 | 2026-09-21 05:08:00 | NOAA-21 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| ee9e6a0e-5b0c-3f26-923e-9c1d9ff1da32 | -15.46316 | -48.48028 | 2026-09-21 05:08:00 | NOAA-21 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 41901718-7c80-3d65-8267-561a8d6f4ee8 | -14.0581 | -52.10704 | 2026-09-21 05:08:00 | NOAA-21 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 7550bae2-3411-3a97-8a3b-65c56d9fa0e7 | -15.86379 | -49.89807 | 2026-09-21 05:08:00 | NOAA-21 | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 11.5 |
| 511f7f35-2bba-3cf7-9743-484ff79f0371 | -16.10769 | -49.81187 | 2026-09-21 05:08:00 | NOAA-21 | ITABERAÍ | GOIÁS | Brasil | 5210406 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 3329445b-d959-3c8f-8c84-5080d72dc3b8 | -16.04569 | -52.51994 | 2026-09-21 05:08:00 | NOAA-21 | PONTAL DO ARAGUAIA | MATO GROSSO | Brasil | 5106653 | 51 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 47ef290b-d64c-30b7-b650-f5f06bc70f82 | -16.04309 | -52.5076 | 2026-09-21 05:08:00 | NOAA-21 | PONTAL DO ARAGUAIA | MATO GROSSO | Brasil | 5106653 | 51 | 33 | nan | nan | nan | Cerrado | 7.6 |
| 5695ba82-81ff-359e-a9d3-1497f3584164 | -15.45807 | -48.47665 | 2026-09-21 05:08:00 | NOAA-21 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| b465ea6e-b20c-30b5-a30d-b053801ab60f | -16.05031 | -52.53083 | 2026-09-21 05:08:00 | NOAA-21 | PONTAL DO ARAGUAIA | MATO GROSSO | Brasil | 5106653 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 373d53bf-4e24-31b9-8a37-d1ddcd5a121b | -15.4505 | -48.47587 | 2026-09-21 05:08:00 | NOAA-21 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 8a291690-0179-31de-9c05-78c08f3c3f3e | -14.66514 | -54.47141 | 2026-09-21 05:08:00 | NOAA-21 | PLANALTO DA SERRA | MATO GROSSO | Brasil | 5106455 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| d43f8365-2807-3dac-916f-e0eefa15d0ef | -14.07781 | -52.08562 | 2026-09-21 05:08:00 | NOAA-21 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 3.5 |
| a8b30cd1-2259-3597-870e-994dc9b5f926 | -15.46948 | -48.40678 | 2026-09-21 05:08:00 | NOAA-21 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 04c2a42a-3521-3e59-aff9-e4bae8ef3411 | -14.05253 | -52.07085 | 2026-09-21 05:08:00 | NOAA-21 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 13ff8cdf-6c0f-3000-b416-e7139082b93c | -16.03007 | -52.5099 | 2026-09-21 05:08:00 | NOAA-21 | PONTAL DO ARAGUAIA | MATO GROSSO | Brasil | 5106653 | 51 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 0e79e978-426e-3a63-90bd-e9dc85054624 | -14.05014 | -52.06992 | 2026-09-21 05:08:00 | NOAA-21 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 6.0 |
| f3446c7e-19ac-3362-91ef-fbf6437bf655 | -14.06175 | -52.11156 | 2026-09-21 05:08:00 | NOAA-21 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 850eb6bd-44fa-3ec9-991b-504717d0fab5 | -16.68835 | -47.88927 | 2026-09-21 05:08:00 | NOAA-21 | LUZIÂNIA | GOIÁS | Brasil | 5212501 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| e5b3f2d1-37c4-35c7-8a3d-36bebcd61542 | -16.04026 | -52.50963 | 2026-09-21 05:08:00 | NOAA-21 | PONTAL DO ARAGUAIA | MATO GROSSO | Brasil | 5106653 | 51 | 33 | nan | nan | nan | Cerrado | 30.3 |
| 2e049731-86fa-3f99-b215-0b7a9d4798e3 | -17.23226 | -51.7655 | 2026-09-21 05:08:00 | NOAA-21 | CAIAPÔNIA | GOIÁS | Brasil | 5204409 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| a51484fd-e1e5-3b60-ab6b-c729e76b0ddf | -16.04198 | -52.52976 | 2026-09-21 05:08:00 | NOAA-21 | PONTAL DO ARAGUAIA | MATO GROSSO | Brasil | 5106653 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 8c65e925-8282-3c3d-aef6-889c021d23f6 | -16.03733 | -52.53318 | 2026-09-21 05:08:00 | NOAA-21 | PONTAL DO ARAGUAIA | MATO GROSSO | Brasil | 5106653 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| db57611e-5394-35bc-8535-06efd2dbf445 | -14.10646 | -52.12566 | 2026-09-21 05:08:00 | NOAA-21 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 1b1cae49-fce2-36c2-88eb-9e4be3241b84 | -15.46991 | -48.40302 | 2026-09-21 05:08:00 | NOAA-21 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| e15cb6b7-8718-3c28-92d9-89dea9ecf812 | -14.92029 | -49.901 | 2026-09-21 05:08:00 | NOAA-21 | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 3.6 |
| cbaa541c-d8f8-39d2-9ec0-f092563de405 | -14.66878 | -54.47197 | 2026-09-21 05:08:00 | NOAA-21 | PLANALTO DA SERRA | MATO GROSSO | Brasil | 5106455 | 51 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 0627d603-04c0-318c-ad50-1c1a1ee9b5cf | -18.37294 | -49.39406 | 2026-09-21 05:08:00 | NOAA-21 | ITUMBIARA | GOIÁS | Brasil | 5211503 | 52 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 316b1e77-9d48-3e51-ad80-4ce769b9d213 | -16.04076 | -52.5057 | 2026-09-21 05:08:00 | NOAA-21 | PONTAL DO ARAGUAIA | MATO GROSSO | Brasil | 5106653 | 51 | 33 | nan | nan | nan | Cerrado | 21.8 |
| 31205324-00bb-32a2-a203-ea97817457fc | -16.03789 | -52.51489 | 2026-09-21 05:08:00 | NOAA-21 | PONTAL DO ARAGUAIA | MATO GROSSO | Brasil | 5106653 | 51 | 33 | nan | nan | nan | Cerrado | 16.9 |
| a54dac8d-d6b0-3163-843d-1a8c4fe80cf8 | -15.45671 | -48.46958 | 2026-09-21 05:08:00 | NOAA-21 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 5b12c0c1-55b2-3a46-9f9d-b8ff1d3c8bc5 | -16.32017 | -53.84457 | 2026-09-21 05:08:00 | NOAA-21 | GUIRATINGA | MATO GROSSO | Brasil | 5104203 | 51 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 9620b411-0bc1-3d6f-9d09-e8256d37d2e6 | -16.03372 | -52.51435 | 2026-09-21 05:08:00 | NOAA-21 | PONTAL DO ARAGUAIA | MATO GROSSO | Brasil | 5106653 | 51 | 33 | nan | nan | nan | Cerrado | 16.9 |
| c03a7a6d-b499-38ba-9d59-0f161b21244c | -16.04205 | -52.51545 | 2026-09-21 05:08:00 | NOAA-21 | PONTAL DO ARAGUAIA | MATO GROSSO | Brasil | 5106653 | 51 | 33 | nan | nan | nan | Cerrado | 9.3 |
| aa0229b0-f203-33e1-a07d-f32bb653c38b | -16.01553 | -52.52388 | 2026-09-21 05:08:00 | NOAA-21 | PONTAL DO ARAGUAIA | MATO GROSSO | Brasil | 5106653 | 51 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 1bc41275-d477-334a-b676-a906225bfe81 | -17.22835 | -51.76037 | 2026-09-21 05:08:00 | NOAA-21 | CAIAPÔNIA | GOIÁS | Brasil | 5204409 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 7ab14f95-482d-3fe8-a5ee-09e986e30210 | -15.46078 | -48.43439 | 2026-09-21 05:08:00 | NOAA-21 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| af983af0-b2e6-39de-839b-b28017cf4f87 | -17.22784 | -51.76464 | 2026-09-21 05:08:00 | NOAA-21 | CAIAPÔNIA | GOIÁS | Brasil | 5204409 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 3fdd2a40-c644-35c6-818c-39a01be2b4be | -14.65607 | -54.45677 | 2026-09-21 05:08:00 | NOAA-21 | PLANALTO DA SERRA | MATO GROSSO | Brasil | 5106455 | 51 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 5710c286-21db-39d4-bd3f-d95faaf26c00 | -14.62648 | -52.07385 | 2026-09-21 05:08:00 | NOAA-21 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 7500a1fd-a4dd-3410-9db6-143c576189e5 | -17.23277 | -51.76115 | 2026-09-21 05:08:00 | NOAA-21 | CAIAPÔNIA | GOIÁS | Brasil | 5204409 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 8c2932d9-74e0-3d5a-af47-4c8fe423ec99 | -15.45298 | -48.47314 | 2026-09-21 05:08:00 | NOAA-21 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 4.2 |
| ff81223f-3c09-3fdb-863d-91fb08a344ae | -14.67181 | -54.47678 | 2026-09-21 05:08:00 | NOAA-21 | PLANALTO DA SERRA | MATO GROSSO | Brasil | 5106455 | 51 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 790035b6-b246-3fd8-b889-8beb79fd4393 | -16.31695 | -53.83932 | 2026-09-21 05:08:00 | NOAA-21 | GUIRATINGA | MATO GROSSO | Brasil | 5104203 | 51 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 55da91f5-f0c9-3a87-8da7-6335692c345d | -14.09658 | -52.13641 | 2026-09-21 05:08:00 | NOAA-21 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 13.3 |
| 6a5c8c88-4830-3efb-92ce-5f5004bf8796 | -14.03476 | -52.07676 | 2026-09-21 05:08:00 | NOAA-21 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 3.2 |
| b05508bb-009b-3b23-8a87-c64bb6abef20 | -14.65668 | -54.45245 | 2026-09-21 05:08:00 | NOAA-21 | PLANALTO DA SERRA | MATO GROSSO | Brasil | 5106455 | 51 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 3894bf1f-2a67-38bc-b455-4fea847688e2 | -16.04345 | -52.51806 | 2026-09-21 05:08:00 | NOAA-21 | PONTAL DO ARAGUAIA | MATO GROSSO | Brasil | 5106653 | 51 | 33 | nan | nan | nan | Cerrado | 2.7 |
| b338426b-4fdd-32cd-b93a-ad882672af04 | -16.01502 | -52.52779 | 2026-09-21 05:08:00 | NOAA-21 | PONTAL DO ARAGUAIA | MATO GROSSO | Brasil | 5106653 | 51 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 1a4af92a-e405-36a6-b38c-817144220c1a | -16.68666 | -47.88392 | 2026-09-21 05:08:00 | NOAA-21 | LUZIÂNIA | GOIÁS | Brasil | 5212501 | 52 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 79c656b2-968f-3be1-87c1-8ec2769aa180 | -15.44635 | -48.46426 | 2026-09-21 05:08:00 | NOAA-21 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| f0f7c559-21ef-3dcc-b2d8-3793abd58f10 | -16.01867 | -52.53228 | 2026-09-21 05:08:00 | NOAA-21 | PONTAL DO ARAGUAIA | MATO GROSSO | Brasil | 5106653 | 51 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 1560a611-b9c6-39c9-a20a-0dab09e2e24a | -14.65971 | -54.45736 | 2026-09-21 05:08:00 | NOAA-21 | PLANALTO DA SERRA | MATO GROSSO | Brasil | 5106455 | 51 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 2743e34c-4400-3574-9b2f-3a39031bc677 | -16.31307 | -53.83903 | 2026-09-21 05:08:00 | NOAA-21 | GUIRATINGA | MATO GROSSO | Brasil | 5104203 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 349455e5-e4d8-3087-85a4-4f4c211e0f6c | -15.63519 | -52.70248 | 2026-09-21 05:08:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| f1c95f1e-2e2d-38e2-9edb-8a59aab89d64 | -16.39658 | -54.71623 | 2026-09-21 05:08:00 | NOAA-21 | RONDONÓPOLIS | MATO GROSSO | Brasil | 5107602 | 51 | 33 | nan | nan | nan | Cerrado | 7.7 |
| 422357b0-0621-3cfc-a6aa-0a737445e4e5 | -16.40025 | -54.71677 | 2026-09-21 05:08:00 | NOAA-21 | RONDONÓPOLIS | MATO GROSSO | Brasil | 5107602 | 51 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 675bec7b-dae6-3c31-a546-b270f39646c1 | -15.44834 | -48.44691 | 2026-09-21 05:08:00 | NOAA-21 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 8e45e53e-c95d-3c4b-9120-2775dc1055b2 | -16.03998 | -52.53107 | 2026-09-21 05:08:00 | NOAA-21 | PONTAL DO ARAGUAIA | MATO GROSSO | Brasil | 5106653 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 7c876add-4d59-3e00-ad4f-50643eaeb7ce | -14.67607 | -54.47292 | 2026-09-21 05:08:00 | NOAA-21 | PLANALTO DA SERRA | MATO GROSSO | Brasil | 5106455 | 51 | 33 | nan | nan | nan | Cerrado | 3.1 |
| b40c055d-4763-3b59-bed4-5a7482c2bf11 | -16.01086 | -52.52723 | 2026-09-21 05:08:00 | NOAA-21 | PONTAL DO ARAGUAIA | MATO GROSSO | Brasil | 5106653 | 51 | 33 | nan | nan | nan | Cerrado | 2.8 |
| d78f6ac2-b9f5-3eef-8943-4514cacaf732 | -16.32403 | -53.84503 | 2026-09-21 05:08:00 | NOAA-21 | GUIRATINGA | MATO GROSSO | Brasil | 5104203 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 1e7b1d73-b742-39a6-9d36-9231f4612a21 | -14.93052 | -49.89849 | 2026-09-21 05:08:00 | NOAA-21 | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 359b11fb-a13c-35df-99dc-356734493804 | -14.09294 | -52.13193 | 2026-09-21 05:08:00 | NOAA-21 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 24000074-97d3-3d5d-b6b0-525d614e74ae | -15.4639 | -48.47352 | 2026-09-21 05:08:00 | NOAA-21 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 057130c9-18f5-384b-8f5a-d4aa91639ed5 | -15.44984 | -48.45138 | 2026-09-21 05:08:00 | NOAA-21 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| c96fa151-0cb9-3dee-a308-daefbab9470b | -16.04621 | -52.51602 | 2026-09-21 05:08:00 | NOAA-21 | PONTAL DO ARAGUAIA | MATO GROSSO | Brasil | 5106653 | 51 | 33 | nan | nan | nan | Cerrado | 9.3 |
| d5cfd1b4-4fae-3285-a1eb-a44834a7c1ce | -14.61303 | -52.11192 | 2026-09-21 05:08:00 | NOAA-21 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 3.7 |
| cc0725c7-2cd5-3d2a-a02f-46ab73123d3b | -14.07217 | -52.1291 | 2026-09-21 05:08:00 | NOAA-21 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 9267f59e-b7bb-3eaa-848c-2f93dfdce1a3 | -15.63928 | -52.70303 | 2026-09-21 05:08:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| e08ca674-77c4-3a33-95de-1f62041d2ff9 | -16.99984 | -56.5197 | 2026-09-21 05:08:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.4 |
| b9b65e44-b944-3a59-b38b-f599bd338f7e | -16.04761 | -52.51864 | 2026-09-21 05:08:00 | NOAA-21 | PONTAL DO ARAGUAIA | MATO GROSSO | Brasil | 5106653 | 51 | 33 | nan | nan | nan | Cerrado | 17.7 |
| 83588f0b-edf3-334e-9c75-ab4712203670 | -16.32723 | -53.8504 | 2026-09-21 05:08:00 | NOAA-21 | GUIRATINGA | MATO GROSSO | Brasil | 5104203 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 4ecc9e31-1016-3ffe-a563-31fb3365327c | -15.45087 | -48.47267 | 2026-09-21 05:08:00 | NOAA-21 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 6676aa28-e8a3-3838-bfb0-f898179fdb56 | -16.68263 | -47.88872 | 2026-09-21 05:08:00 | NOAA-21 | LUZIÂNIA | GOIÁS | Brasil | 5212501 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| f2978223-8259-3bc5-9d95-5270f1b309e2 | -16.05812 | -52.53596 | 2026-09-21 05:08:00 | NOAA-21 | PONTAL DO ARAGUAIA | MATO GROSSO | Brasil | 5106653 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 3ed18c63-5e6b-3166-9a81-05dcf31bed56 | -15.46219 | -48.46964 | 2026-09-21 05:08:00 | NOAA-21 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| ad55457a-ed6b-36c7-aefd-405ac1b438a7 | -18.03458 | -50.93196 | 2026-09-21 05:08:00 | NOAA-21 | RIO VERDE | GOIÁS | Brasil | 5218805 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| f79470e3-4dc3-39f2-9904-e9c3400ba40b | -14.61724 | -52.11237 | 2026-09-21 05:08:00 | NOAA-21 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 2f4417f9-2f0c-3072-a9cb-18a5ea7f09b1 | -16.03475 | -52.50651 | 2026-09-21 05:08:00 | NOAA-21 | PONTAL DO ARAGUAIA | MATO GROSSO | Brasil | 5106653 | 51 | 33 | nan | nan | nan | Cerrado | 67.7 |


[Clique aqui para ver as próximas entradas](README84.md)
