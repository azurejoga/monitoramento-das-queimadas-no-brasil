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

## Dados Diários - Página 17

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 953990f3-0759-34fd-81ab-b88c19b801ea | -19.42537 | -54.77678 | 2025-06-13 04:34:00 | NOAA-20 | SÃO GABRIEL DO OESTE | MATO GROSSO DO SUL | Brasil | 5007695 | 50 | 33 | nan | nan | nan | Cerrado | 1.2 |
| d24648d8-ae88-302e-aefd-9fcc88924f91 | -13.89603 | -54.63129 | 2025-06-13 04:34:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 4fcf0e0f-c060-3954-a58b-d6e545252291 | -17.65537 | -47.45943 | 2025-06-13 04:34:00 | NOAA-20 | CATALÃO | GOIÁS | Brasil | 5205109 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 499c4c04-6445-3c2d-9cd7-d400276d89ff | -14.68025 | -53.37347 | 2025-06-13 04:34:00 | NOAA-20 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 7.6 |
| 21e65618-db13-3692-845c-8c7fb836fd55 | -17.65874 | -47.45443 | 2025-06-13 04:34:00 | NOAA-20 | CATALÃO | GOIÁS | Brasil | 5205109 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| a30c9121-a018-3dfa-9dee-b91d377e41dc | -13.97451 | -54.44546 | 2025-06-13 04:34:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 3.3 |
| f3ce3927-f15c-3073-9f9f-21b75d41435d | -15.36 | -47.87865 | 2025-06-13 04:34:00 | NOAA-20 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 8518499d-1ef6-3f81-8223-0354eb439193 | -13.87562 | -47.30722 | 2025-06-13 04:34:00 | NOAA-20 | TERESINA DE GOIÁS | GOIÁS | Brasil | 5221080 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| fa253853-43d9-3178-954a-5dc3c1d93ece | -12.52173 | -57.23271 | 2025-06-13 04:34:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 87635e7a-7dd3-3ad8-9fcc-73b0072ba5cd | -13.97056 | -54.44475 | 2025-06-13 04:34:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 9aa303c7-ecf5-382c-88d0-c5de65c15fc2 | -14.20668 | -57.40115 | 2025-06-13 04:34:00 | NOAA-20 | NOVA MARILÂNDIA | MATO GROSSO | Brasil | 5108857 | 51 | 33 | nan | nan | nan | Amazônia | 11.9 |
| efb5cf47-10e2-319f-a718-d1800ea5910c | -19.57911 | -49.1118 | 2025-06-13 04:34:00 | NOAA-20 | PRATA | MINAS GERAIS | Brasil | 3152808 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| fc9a5ef6-e39f-3cda-9d39-04725620575e | -13.65625 | -53.93969 | 2025-06-13 04:34:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 601459ff-052f-3a40-9147-dff684acdead | -12.42857 | -54.87127 | 2025-06-13 04:34:00 | NOAA-20 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| e65fbdba-65e2-3516-b935-ebef5e71767e | -17.65814 | -47.45872 | 2025-06-13 04:34:00 | NOAA-20 | CATALÃO | GOIÁS | Brasil | 5205109 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| dd8ddc60-c40a-3091-91cf-e4c3b4269e43 | -13.08991 | -52.28558 | 2025-06-13 04:34:00 | NOAA-20 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| b65287cd-b318-3986-a270-39ce3b7aabbb | -17.65304 | -47.45037 | 2025-06-13 04:34:00 | NOAA-20 | CATALÃO | GOIÁS | Brasil | 5205109 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 64ea6d9a-970a-333b-b572-e598236a7e23 | -13.89073 | -54.6377 | 2025-06-13 04:34:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 10.8 |
| 98edd9bf-ef0d-35aa-a1a3-2a2450d6de4f | -14.67658 | -53.37282 | 2025-06-13 04:34:00 | NOAA-20 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 7.6 |
| f9826287-6d89-3c36-9da7-73c4566c2d87 | -19.08032 | -53.46519 | 2025-06-13 04:34:00 | NOAA-20 | CAMAPUÃ | MATO GROSSO DO SUL | Brasil | 5002605 | 50 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 9455bb60-5948-3cb6-bb9e-c9c794a0c0fa | -11.91053 | -57.46774 | 2025-06-13 04:34:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 6b2d1432-493d-391d-a12d-24f3d3367544 | -12.52427 | -57.23532 | 2025-06-13 04:34:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 2c1d10f6-f32e-3265-b2de-143a112d60ea | -13.25046 | -49.51531 | 2025-06-13 04:34:00 | NOAA-20 | NOVO PLANALTO | GOIÁS | Brasil | 5215256 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| b7f69a45-1f63-3a8b-9760-bb57f6e91934 | -15.36287 | -47.88295 | 2025-06-13 04:34:00 | NOAA-20 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| b07194f2-971a-31f3-b445-f156342cb0c2 | -13.45498 | -48.21873 | 2025-06-13 04:34:00 | NOAA-20 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 722be9c8-e337-333f-a578-e05d1b384718 | -17.37798 | -53.82144 | 2025-06-13 04:34:00 | NOAA-20 | SONORA | MATO GROSSO DO SUL | Brasil | 5007935 | 50 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 34a997ff-9323-3408-ac7c-cd3870cb59d0 | -14.54635 | -53.6706 | 2025-06-13 04:34:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 42245578-c411-3c9e-8212-e8fcf310a104 | -13.89744 | -54.64632 | 2025-06-13 04:34:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 54008069-02af-3f8a-913a-8a819be5d1fe | -12.52071 | -57.23821 | 2025-06-13 04:34:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| fe3202a9-d5d7-301c-b705-f9f38a3a9cd8 | -14.2124 | -57.39699 | 2025-06-13 04:34:00 | NOAA-20 | NOVA MARILÂNDIA | MATO GROSSO | Brasil | 5108857 | 51 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 9e55b4dd-3f08-30a2-88bd-7ad203a6fbe0 | -14.03217 | -55.12527 | 2025-06-13 04:34:00 | NOAA-20 | SANTA RITA DO TRIVELATO | MATO GROSSO | Brasil | 5107768 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| e401d6e6-1e9c-3d1d-a34c-2497449a020c | -15.13711 | -49.54502 | 2025-06-13 04:34:00 | NOAA-20 | NOVA GLÓRIA | GOIÁS | Brasil | 5214861 | 52 | 33 | nan | nan | nan | Cerrado | 0.4 |
| c3efa0a8-8635-37c6-ab9e-ad437ce6d261 | -17.04585 | -48.93425 | 2025-06-13 04:34:00 | NOAA-20 | BELA VISTA DE GOIÁS | GOIÁS | Brasil | 5203302 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 1031ac83-0734-320a-90c2-d1ee09cdf9ce | -14.67081 | -53.36245 | 2025-06-13 04:34:00 | NOAA-20 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 7eb73701-cd47-3ce7-9e15-8e046433067c | -13.89937 | -54.63567 | 2025-06-13 04:34:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 4f72e2b6-a0f1-3d50-bd96-0e2230fedde5 | -16.67849 | -47.22775 | 2025-06-13 04:34:00 | NOAA-20 | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| fc9b92a8-d86b-379f-991f-90cca1663124 | -13.8906 | -54.61573 | 2025-06-13 04:34:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 94d90a96-6ea2-3629-8bce-a170b15e927d | -13.09347 | -52.28621 | 2025-06-13 04:34:00 | NOAA-20 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 4.8 |
| efae354a-3012-37d1-900a-3053e7e07ce6 | -11.91443 | -57.47452 | 2025-06-13 04:34:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 38a277f5-7871-3f71-a965-e4d8db1d1c83 | -12.43272 | -54.87205 | 2025-06-13 04:34:00 | NOAA-20 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 615ee384-0229-39d6-938f-b1840080370a | -17.00829 | -49.77898 | 2025-06-13 04:34:00 | NOAA-20 | CEZARINA | GOIÁS | Brasil | 5205455 | 52 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 65413faf-4d3c-3412-8594-83d7baf83fbc | -13.89872 | -54.63922 | 2025-06-13 04:34:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 3.6 |
| fb364725-5a4d-3e34-b717-9a25d40c1cf8 | -14.21144 | -57.40208 | 2025-06-13 04:34:00 | NOAA-20 | NOVA MARILÂNDIA | MATO GROSSO | Brasil | 5108857 | 51 | 33 | nan | nan | nan | Amazônia | 7.8 |
| ed3635e1-74fa-34b2-9a8c-0e9c51341444 | -15.38945 | -55.37465 | 2025-06-13 04:34:00 | NOAA-20 | CHAPADA DOS GUIMARÃES | MATO GROSSO | Brasil | 5103007 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 74677920-6954-3546-991a-b7141bc9eb93 | -15.02769 | -47.03994 | 2025-06-13 04:34:00 | NOAA-20 | VILA BOA | GOIÁS | Brasil | 5222203 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| c8c8f052-0415-3579-b2c4-33a6c666da0b | -11.91134 | -57.46341 | 2025-06-13 04:34:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 317f4543-7cdd-3769-8655-60faa50bcbaf | -14.03901 | -55.1344 | 2025-06-13 04:34:00 | NOAA-20 | SANTA RITA DO TRIVELATO | MATO GROSSO | Brasil | 5107768 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 77e1139a-808d-3dd0-9bb9-ba784b93ebe1 | -15.36116 | -47.87082 | 2025-06-13 04:34:00 | NOAA-20 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 4d9a1a50-9495-38bb-af1f-812cc1099395 | -11.91631 | -57.46444 | 2025-06-13 04:34:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 2adff452-efa6-3f40-9bbc-ab9fb2e891d2 | -11.9194 | -57.47552 | 2025-06-13 04:34:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 00931574-b1b9-3401-a3ea-4b6deaf54c89 | -11.91551 | -57.46874 | 2025-06-13 04:34:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 5dd31723-341f-327a-975a-b64e6d37e2f7 | -14.19047 | -57.40849 | 2025-06-13 04:34:00 | NOAA-20 | NOVA MARILÂNDIA | MATO GROSSO | Brasil | 5108857 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 4783737f-1342-3707-926c-705ff7c77ca5 | -17.6617 | -47.45927 | 2025-06-13 04:34:00 | NOAA-20 | CATALÃO | GOIÁS | Brasil | 5205109 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 2d9fab1d-e01b-3b6a-81af-c0d3a0e74aac | -13.97754 | -54.45138 | 2025-06-13 04:34:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| d1df15a0-fad2-39c6-966b-5159f7bacf15 | -13.98149 | -54.45211 | 2025-06-13 04:34:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 00a2f9ab-d069-3f5b-9131-c471f067598f | -17.6566 | -47.45092 | 2025-06-13 04:34:00 | NOAA-20 | CATALÃO | GOIÁS | Brasil | 5205109 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| a97a45c6-9de0-36ce-b8a5-7a81ceddea22 | -19.07962 | -53.46934 | 2025-06-13 04:34:00 | NOAA-20 | CAMAPUÃ | MATO GROSSO DO SUL | Brasil | 5002605 | 50 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 80f5da53-7853-30c7-8eb5-a4b16d703cae | -12.43202 | -54.87588 | 2025-06-13 04:34:00 | NOAA-20 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 049a9897-5745-3cb6-a4d9-7487dcfe0ddc | -15.02711 | -47.04399 | 2025-06-13 04:34:00 | NOAA-20 | VILA BOA | GOIÁS | Brasil | 5222203 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 72a34c86-089a-3563-aea8-d711f6871ad3 | -13.97359 | -54.45069 | 2025-06-13 04:34:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 91b4ab29-8ef0-3b05-9a0e-72a9c35909f8 | -17.65161 | -47.45334 | 2025-06-13 04:34:00 | NOAA-20 | CATALÃO | GOIÁS | Brasil | 5205109 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 13a572da-bfc0-3d0f-943d-d955a38c1123 | -11.91497 | -57.47161 | 2025-06-13 04:34:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| b553d7bc-a0c4-31e7-9a62-c2acc75bcb75 | -17.38161 | -53.8221 | 2025-06-13 04:34:00 | NOAA-20 | SONORA | MATO GROSSO DO SUL | Brasil | 5007935 | 50 | 33 | nan | nan | nan | Cerrado | 0.8 |
| b171d2b8-b084-365f-bd36-dd58c4b3e265 | -17.6623 | -47.45498 | 2025-06-13 04:34:00 | NOAA-20 | CATALÃO | GOIÁS | Brasil | 5205109 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 9b575226-c9ac-38b7-be2b-b0497060a9bd | -14.19618 | -57.40442 | 2025-06-13 04:34:00 | NOAA-20 | NOVA MARILÂNDIA | MATO GROSSO | Brasil | 5108857 | 51 | 33 | nan | nan | nan | Amazônia | 6.4 |
| 99e8339d-a158-368b-945f-6c6bbbd50aab | -12.42927 | -54.86743 | 2025-06-13 04:34:00 | NOAA-20 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| d7de5541-f1da-300f-ad69-fedd1cc827c9 | -13.96849 | -54.43348 | 2025-06-13 04:34:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 441a3556-7602-3093-b060-c9aaeadcb42b | -14.1895 | -57.41352 | 2025-06-13 04:34:00 | NOAA-20 | NOVA MARILÂNDIA | MATO GROSSO | Brasil | 5108857 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| b14526d2-2d80-3f83-b9a1-cb2f419060bc | -20.46095 | -49.74932 | 2025-06-13 04:34:00 | NOAA-20 | COSMORAMA | SÃO PAULO | Brasil | 3512902 | 35 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 8f8f693b-6e98-3021-ad2c-e07581494cc7 | -18.82149 | -47.92694 | 2025-06-13 04:34:00 | NOAA-20 | ARAGUARI | MINAS GERAIS | Brasil | 3103504 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| b9bff245-9813-335d-a664-7ecca6de3ffd | -13.89203 | -54.63054 | 2025-06-13 04:34:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 4.5 |
| d4d9b530-1088-39dc-a44f-d80c2e9b408f | -20.09425 | -50.86539 | 2025-06-13 04:34:00 | NOAA-20 | SANTA CLARA D'OESTE | SÃO PAULO | Brasil | 3546108 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| b006f453-d364-3042-989e-e1cfbac19ba6 | -18.66171 | -55.74416 | 2025-06-13 04:34:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 0.9 |
| 2f9fabb1-0e36-3593-a77a-a45746aa88f1 | -14.03286 | -55.12152 | 2025-06-13 04:34:00 | NOAA-20 | SANTA RITA DO TRIVELATO | MATO GROSSO | Brasil | 5107768 | 51 | 33 | nan | nan | nan | Cerrado | 3.3 |
| eacb7080-0bae-380d-b18c-9ae4f05d1046 | -13.89138 | -54.63412 | 2025-06-13 04:34:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 10.8 |
| ceabedfa-aaff-3f9a-b5ec-1f381193f76b | -14.0397 | -55.13065 | 2025-06-13 04:34:00 | NOAA-20 | SANTA RITA DO TRIVELATO | MATO GROSSO | Brasil | 5107768 | 51 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 6201cc62-53f6-3d29-a389-8779bb367f94 | -12.70485 | -58.03475 | 2025-06-13 04:34:00 | NOAA-20 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| c6160ec4-ff20-3c84-903d-33a50f23488a | -12.70224 | -58.03522 | 2025-06-13 04:34:00 | NOAA-20 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 6914b935-035f-3709-804a-54906d62c2af | -13.8973 | -54.62425 | 2025-06-13 04:34:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 8.8 |
| 22c1ffb8-f4c2-3b91-a6f6-d6391e8504a1 | -13.89667 | -54.62775 | 2025-06-13 04:34:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 76597e72-e227-35ab-bb44-ab4503ed6113 | -20.09756 | -50.86597 | 2025-06-13 04:34:00 | NOAA-20 | SANTA CLARA D'OESTE | SÃO PAULO | Brasil | 3546108 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 263bad15-637e-3f22-b9c3-0c7b0b8f9693 | -11.92048 | -57.46978 | 2025-06-13 04:34:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 95d23dde-0f8c-3bd6-aedf-bea24dd28223 | -15.36917 | -47.86415 | 2025-06-13 04:34:00 | NOAA-20 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| b656603f-c936-3450-a819-ac1d57808197 | -17.65119 | -47.46314 | 2025-06-13 04:34:00 | NOAA-20 | CATALÃO | GOIÁS | Brasil | 5205109 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 1c6dab8c-3036-3301-8aaf-a2fb671a8ec1 | -13.89395 | -54.61998 | 2025-06-13 04:34:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 8.8 |
| 13774b2f-2029-3a7a-a4d7-e7eb00aa8778 | -14.84814 | -48.30939 | 2025-06-13 04:34:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| a11d0468-4c98-30fc-94d8-153ab8e884d4 | -12.46781 | -58.47069 | 2025-06-13 04:34:00 | NOAA-20 | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| eef1ed1c-c91b-36ce-864a-f6ef2ca6b4f3 | -15.56977 | -47.85443 | 2025-06-13 04:34:00 | NOAA-20 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 1.3 |
| a4b83858-8064-35cb-b27d-3dbe4c1af9c0 | -13.97243 | -54.43423 | 2025-06-13 04:34:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| ec0f8be0-3c3b-3e5a-a82d-f6e85941711e | -13.89459 | -54.61647 | 2025-06-13 04:34:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 17.2 |
| 98704e03-655e-3960-b039-5a3bae80e874 | -15.36174 | -47.86692 | 2025-06-13 04:34:00 | NOAA-20 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 7cff0938-0696-3a7a-af3f-2d08f99f6ca9 | -14.02806 | -55.12449 | 2025-06-13 04:34:00 | NOAA-20 | SANTA RITA DO TRIVELATO | MATO GROSSO | Brasil | 5107768 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 96e8f2dc-0a87-3319-b30d-0432ad39bfaa | -13.24898 | -56.53743 | 2025-06-13 04:34:00 | NOAA-20 | NOVA MUTUM | MATO GROSSO | Brasil | 5106224 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| f1c86d2c-140d-3fad-9872-570429f6c82e | -15.36858 | -47.86809 | 2025-06-13 04:34:00 | NOAA-20 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 6764549b-cc99-3605-8dcc-03efe3221813 | -14.67736 | -53.36831 | 2025-06-13 04:34:00 | NOAA-20 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 7.6 |
| 94159084-c5cb-3e12-b867-e42c2a622b9e | -17.65242 | -47.45461 | 2025-06-13 04:34:00 | NOAA-20 | CATALÃO | GOIÁS | Brasil | 5205109 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 1b7c9121-9766-3a67-8dfb-81cb09d119bc | -12.47369 | -58.46857 | 2025-06-13 04:34:00 | NOAA-20 | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| a2b05875-0332-399f-8e79-d4c3c8ead9c0 | -14.19423 | -57.41467 | 2025-06-13 04:34:00 | NOAA-20 | NOVA MARILÂNDIA | MATO GROSSO | Brasil | 5108857 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 276922f2-3994-3376-a0f7-add5e9e2425e | -15.38458 | -47.87857 | 2025-06-13 04:34:00 | NOAA-20 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 0.5 |
| eef1d95d-8955-3952-ac5a-c1407470a698 | -12.70734 | -58.03623 | 2025-06-13 04:34:00 | NOAA-20 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |


[Clique aqui para ver as próximas entradas](README18.md)
