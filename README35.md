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

## Dados Diários - Página 35

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| b70b8680-f4a2-3d1e-8202-0ec0389c2e0c | -15.35285 | -47.98499 | 2025-10-06 04:27:00 | NOAA-21 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| cff1e9c3-b0a3-3194-9d5b-b8420dd04737 | -17.07685 | -43.38451 | 2025-10-06 04:27:00 | NOAA-21 | ITACAMBIRA | MINAS GERAIS | Brasil | 3132008 | 31 | 33 | nan | nan | nan | Cerrado | 4.0 |
| dfd17d30-23c9-3d4f-8790-d53c857bc15a | -11.14064 | -47.16045 | 2025-10-06 04:27:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| bca2444f-525c-39ba-aac6-9514a7b520a1 | -14.75378 | -54.68499 | 2025-10-06 04:27:00 | NOAA-21 | PLANALTO DA SERRA | MATO GROSSO | Brasil | 5106455 | 51 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 1e44a147-9852-3811-9e0a-740be2321d2d | -13.2865 | -47.57864 | 2025-10-06 04:27:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| bbc4edb9-9e8f-30f0-8970-f75e0714d75f | -11.84241 | -45.07364 | 2025-10-06 04:27:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 55f28349-6aba-3922-ae6b-4e93cb587ecb | -13.29641 | -48.08233 | 2025-10-06 04:27:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 4bc1efff-c1e6-3712-97aa-61bf7c01a80c | -14.54334 | -46.96311 | 2025-10-06 04:27:00 | NOAA-21 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 125f13f4-64da-3590-825f-1d7460a5b041 | -14.69869 | -48.29568 | 2025-10-06 04:27:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 9215f678-913a-375d-b02e-79e4b0854af8 | -12.38677 | -51.10773 | 2025-10-06 04:27:00 | NOAA-21 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 2c5c7a60-4cf3-33fc-bb84-7e1dc302ae59 | -14.93268 | -47.12874 | 2025-10-06 04:27:00 | NOAA-21 | VILA BOA | GOIÁS | Brasil | 5222203 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 6a7bd60d-f7b1-3d9a-afc7-4e6a95cd9736 | -11.86517 | -44.94449 | 2025-10-06 04:27:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| d605e5d8-8d9b-349b-89bb-b4b25b288f50 | -14.33201 | -47.65842 | 2025-10-06 04:27:00 | NOAA-21 | ALTO PARAÍSO DE GOIÁS | GOIÁS | Brasil | 5200605 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| d7d656ea-4a9b-3367-9917-d42f03c70496 | -10.78859 | -48.58608 | 2025-10-06 04:27:00 | NOAA-21 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| e8103957-680b-375f-b81a-e5d681ff50bd | -10.73348 | -47.65252 | 2025-10-06 04:27:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| a0bcd847-e125-3fa9-9acd-99b2c33de31f | -15.93281 | -48.60688 | 2025-10-06 04:27:00 | NOAA-21 | CORUMBÁ DE GOIÁS | GOIÁS | Brasil | 5205802 | 52 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 3239d0e8-727c-3e4c-ac7a-8454f8e39253 | -11.84356 | -45.08979 | 2025-10-06 04:27:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 8d675483-9d8c-3b92-ade8-f07e53852408 | -15.59478 | -52.54366 | 2025-10-06 04:27:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 4a589081-9621-36ae-b4e2-7a011ab45bfa | -10.55671 | -49.44413 | 2025-10-06 04:27:00 | NOAA-21 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 81f0d8d5-321c-3d59-8391-91250c0288ac | -10.67469 | -48.47205 | 2025-10-06 04:27:00 | NOAA-21 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 910c9723-c4e6-3e74-9340-0f06ea364959 | -12.5514 | -48.16533 | 2025-10-06 04:27:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| b5f902af-81ab-3415-bf7d-bb9636759156 | -13.09199 | -47.93302 | 2025-10-06 04:27:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 77a32823-159c-3b9a-bf15-52d0bad289f6 | -15.20881 | -56.80877 | 2025-10-06 04:27:00 | NOAA-21 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 5c3879e9-77aa-3016-a2eb-077df2bb44ab | -15.43929 | -45.86888 | 2025-10-06 04:27:00 | NOAA-21 | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| e14a1321-2c12-3a16-be8e-771347807438 | -12.23801 | -43.77397 | 2025-10-06 04:27:00 | NOAA-21 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| a2056018-0f16-39d5-94c3-ed9f78364f09 | -11.0323 | -54.3895 | 2025-10-06 04:27:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a3befeb5-75a1-3e1b-ac70-50ca3050734c | -9.54848 | -54.5922 | 2025-10-06 04:27:00 | NOAA-21 | GUARANTÃ DO NORTE | MATO GROSSO | Brasil | 5104104 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 915c93f6-168b-368a-847f-4a9102b7c7f3 | -14.69636 | -48.37518 | 2025-10-06 04:27:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 7.6 |
| da0f9aa2-414a-3bdf-93cc-a2eef868ea15 | -15.34899 | -47.98801 | 2025-10-06 04:27:00 | NOAA-21 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 1ef0c91e-0279-34d8-aebc-ccc4e61bfdd5 | -12.25264 | -49.2008 | 2025-10-06 04:27:00 | NOAA-21 | FIGUEIRÓPOLIS | TOCANTINS | Brasil | 1707652 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| f6b84ddf-3040-3cc1-83c4-2ef703f62e9b | -11.10143 | -47.88469 | 2025-10-06 04:27:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 1a58c75d-ebab-3838-83b7-17275edbb9c0 | -12.38462 | -51.07627 | 2025-10-06 04:27:00 | NOAA-21 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| a78f325b-9de7-387e-9732-6fda192984b2 | -11.0287 | -46.54184 | 2025-10-06 04:27:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 1bb0ecba-d57f-3c28-9f39-79e00d750ee8 | -14.5671 | -46.66618 | 2025-10-06 04:27:00 | NOAA-21 | ALVORADA DO NORTE | GOIÁS | Brasil | 5200803 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 9d2c8624-5822-33d4-bccb-561fe948f146 | -13.27499 | -47.63089 | 2025-10-06 04:27:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 3bed2a56-bce7-3e18-b366-1a263a9a8959 | -13.0832 | -47.92438 | 2025-10-06 04:27:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| bfccfca5-07ed-3dee-9ce5-e79780b68ac9 | -14.68094 | -48.38716 | 2025-10-06 04:27:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| c247d80b-1666-3207-af85-d1bb9bd0b24c | -15.37706 | -47.93782 | 2025-10-06 04:27:00 | NOAA-21 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 614d2527-d468-34e3-a019-c62deaede190 | -13.36489 | -47.24715 | 2025-10-06 04:27:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| c947323b-7f7a-3545-a56a-37e1f31c821d | -16.03412 | -51.03141 | 2025-10-06 04:27:00 | NOAA-21 | FAZENDA NOVA | GOIÁS | Brasil | 5207600 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 4c778789-6991-318c-ae54-b6c6566daebc | -10.70118 | -47.9848 | 2025-10-06 04:27:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| f4f4e87a-722d-3223-96c0-a7844a1a1ef3 | -11.84417 | -45.06175 | 2025-10-06 04:27:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 2d184807-edeb-3185-b374-9f970003ef06 | -13.73872 | -47.95251 | 2025-10-06 04:27:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| b1cb0e74-fcce-3261-9304-918f5cae7099 | -11.49198 | -44.97489 | 2025-10-06 04:27:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 18af0de1-0fac-3b15-8a17-ce0c7a9a39d0 | -14.72317 | -49.23341 | 2025-10-06 04:27:00 | NOAA-21 | URUAÇU | GOIÁS | Brasil | 5221601 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| b484f3d1-be4d-3234-b574-44cfca4ca8b0 | -11.45995 | -51.5226 | 2025-10-06 04:27:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| fd963e17-a177-3e84-b8b0-2a63b2d10074 | -16.05754 | -50.93346 | 2025-10-06 04:27:00 | NOAA-21 | FAZENDA NOVA | GOIÁS | Brasil | 5207600 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| bef9b378-577c-3e94-8908-02beb2ce755b | -15.1923 | -56.83673 | 2025-10-06 04:27:00 | NOAA-21 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 6b73ee30-545f-3c7c-80f5-d55417dca578 | -14.70245 | -48.35799 | 2025-10-06 04:27:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 69892cf4-2457-3c0a-909b-c1bf8b648e4f | -12.32141 | -55.12416 | 2025-10-06 04:27:00 | NOAA-21 | VERA | MATO GROSSO | Brasil | 5108501 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| b2a3b112-34a8-356f-be7f-c0cb1b4171c0 | -13.68365 | -47.95454 | 2025-10-06 04:27:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 6ecbcce8-d440-3c8a-a863-42290ada3c10 | -10.69842 | -47.98076 | 2025-10-06 04:27:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| ef108f9b-f91b-3aff-b8d8-a5d839976934 | -13.28075 | -47.17568 | 2025-10-06 04:27:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 69aac63f-cbbb-36e2-9e14-81f3b42eca35 | -16.05621 | -50.94152 | 2025-10-06 04:27:00 | NOAA-21 | FAZENDA NOVA | GOIÁS | Brasil | 5207600 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 587a9b21-6e96-3e11-97c7-4d8250d73bab | -14.62636 | -52.509 | 2025-10-06 04:27:00 | NOAA-21 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 22672f12-57e0-3db3-bd20-409c3eaa3790 | -13.35436 | -47.18331 | 2025-10-06 04:27:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 9998b192-a88b-314d-92f9-f985820f213e | -10.14392 | -45.45835 | 2025-10-06 04:27:00 | NOAA-21 | SÃO GONÇALO DO GURGUÉIA | PIAUÍ | Brasil | 2209757 | 22 | 33 | nan | nan | nan | Cerrado | 2.6 |
| ddd4e3b0-ef0b-3566-beae-ae9e65de691f | -13.25746 | -47.80856 | 2025-10-06 04:27:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 0c09502b-da8e-3947-b64b-440fd2ecd847 | -12.89609 | -54.75606 | 2025-10-06 04:27:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 902b08fe-9e40-3bf4-9926-e33dd94f5134 | -13.07878 | -47.95252 | 2025-10-06 04:27:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 25d874fe-b2f5-3c07-9207-6062f6aaf151 | -15.37982 | -47.9858 | 2025-10-06 04:27:00 | NOAA-21 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 2fedc604-b798-381d-b7f9-0f53964f0fa1 | -14.91509 | -46.86432 | 2025-10-06 04:27:00 | NOAA-21 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 471915c8-186d-3344-9a65-d5ce3099769a | -12.44392 | -45.57308 | 2025-10-06 04:27:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 4.8 |
| d6331bfe-4739-3ebe-8c69-fa0ff6f11328 | -12.24808 | -49.20756 | 2025-10-06 04:27:00 | NOAA-21 | FIGUEIRÓPOLIS | TOCANTINS | Brasil | 1707652 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 4b7085e8-547a-34d5-b47e-5e80c96d814d | -12.39575 | -45.0029 | 2025-10-06 04:27:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 3.5 |
| d74b57fc-e576-370b-9ae0-697a2bcd8dae | -13.33824 | -48.05302 | 2025-10-06 04:27:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 0742dd39-1fd8-3510-ba8c-c40313918155 | -15.98584 | -50.85172 | 2025-10-06 04:27:00 | NOAA-21 | JUSSARA | GOIÁS | Brasil | 5212204 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 0cd6e85f-9bc4-3e89-91c6-539a3703bd45 | -12.23431 | -43.77321 | 2025-10-06 04:27:00 | NOAA-21 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 59d5c2ec-b23e-3f9c-928b-c23e6661d6a1 | -14.6881 | -48.38471 | 2025-10-06 04:27:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 8f5abca9-eb1d-3588-bd47-af4b31d3dac4 | -14.68698 | -48.3918 | 2025-10-06 04:27:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| cfbbb161-2157-3d1e-af67-7722b13cb20b | -14.63224 | -52.52016 | 2025-10-06 04:27:00 | NOAA-21 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 74b95c37-42a2-327e-9047-2aed3fd3a2fd | -13.72768 | -48.06642 | 2025-10-06 04:27:00 | NOAA-21 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| c70b43ea-0ef5-3c70-9b75-3eb07868dd40 | -15.30526 | -47.31867 | 2025-10-06 04:27:00 | NOAA-21 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 43e57f03-4edc-3637-89e5-db4b56a41287 | -11.44077 | -55.0498 | 2025-10-06 04:27:00 | NOAA-21 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 10ab5347-15a3-3465-84bf-8352972a0510 | -11.11976 | -47.16427 | 2025-10-06 04:27:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 1c1a9296-1f6d-30da-a10d-c0b469bd2998 | -12.82121 | -46.84705 | 2025-10-06 04:27:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 1c141f34-731b-398c-829a-58df5d09036d | -13.2657 | -47.84231 | 2025-10-06 04:27:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 7.1 |
| fadedd4c-5feb-3a2f-9054-0814de08088e | -12.45527 | -45.54356 | 2025-10-06 04:27:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| d818fca1-0140-3fc0-9d7f-9ae8c0704958 | -13.25793 | -47.61009 | 2025-10-06 04:27:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| eefbd249-1e0a-3cc3-bfa8-1bc29479677f | -11.06614 | -47.91493 | 2025-10-06 04:27:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 5644e0e6-60a4-35d5-96de-97b9a3a50439 | -11.03655 | -47.78076 | 2025-10-06 04:27:00 | NOAA-21 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 6.3 |
| fa011ad8-1a85-382b-94e7-389330cc182e | -14.92934 | -47.1282 | 2025-10-06 04:27:00 | NOAA-21 | VILA BOA | GOIÁS | Brasil | 5222203 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 4f64f316-5328-3343-918f-9757906386ee | -11.81971 | -44.88791 | 2025-10-06 04:27:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 2f655077-a2fc-37aa-b7c1-1f0f72c6807e | -13.35934 | -47.19507 | 2025-10-06 04:27:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 700f31fa-f99b-387a-b938-0d0d188b473f | -15.30139 | -47.32172 | 2025-10-06 04:27:00 | NOAA-21 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 802f1bb8-39b0-35d1-bbb4-7073b349295f | -13.38221 | -47.55468 | 2025-10-06 04:27:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 06f8471d-ef82-3b4c-aa52-d5d482811dfe | -16.01292 | -50.96585 | 2025-10-06 04:27:00 | NOAA-21 | JUSSARA | GOIÁS | Brasil | 5212204 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 73668937-f6cd-37c2-8d27-c70a9d0b089d | -15.3523 | -47.98855 | 2025-10-06 04:27:00 | NOAA-21 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| c6a047d0-93d2-3282-a43e-0e3cbb81351e | -13.3608 | -48.03864 | 2025-10-06 04:27:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 6a2f0c1e-ccec-37b7-af86-64d75d5de403 | -13.56014 | -47.23824 | 2025-10-06 04:27:00 | NOAA-21 | TERESINA DE GOIÁS | GOIÁS | Brasil | 5221080 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 4814f807-277e-38c1-80a2-3dd7ce9238e7 | -13.37564 | -47.59721 | 2025-10-06 04:27:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| fd46c65e-7a2f-3dab-ba61-b4d916812feb | -12.95248 | -54.72847 | 2025-10-06 04:27:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 5b2f2ba4-a680-35f4-a4df-8407e415f13d | -9.25638 | -51.81215 | 2025-10-06 04:27:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 565454cf-2b13-357e-a3ff-271418dc0154 | -13.35381 | -47.1869 | 2025-10-06 04:27:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 9f365ca6-d728-3ecf-bd38-4fea27ecd034 | -11.84299 | -45.06968 | 2025-10-06 04:27:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| fe6067f0-26bd-37e3-98d8-8540551488ab | -14.6848 | -48.38416 | 2025-10-06 04:27:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 3ed5fbc6-44dd-3eab-aef2-45bd439b04b4 | -13.26509 | -47.62929 | 2025-10-06 04:27:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 4deee844-4acf-3c50-a150-fde6ce50d7c0 | -11.04316 | -47.78183 | 2025-10-06 04:27:00 | NOAA-21 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 8c7dce1b-dfee-376e-97ec-2c56e52aca96 | -12.25997 | -49.19827 | 2025-10-06 04:27:00 | NOAA-21 | FIGUEIRÓPOLIS | TOCANTINS | Brasil | 1707652 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 9dd07ede-faac-3016-b81b-b1d0201fc050 | -11.52851 | -47.15809 | 2025-10-06 04:27:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |


[Clique aqui para ver as próximas entradas](README36.md)
