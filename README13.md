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

## Dados Diários - Página 13

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 4d984ab6-0b5f-36be-a34e-a1552e18c70d | -18.83924 | -53.62881 | 2025-12-27 04:44:00 | NOAA-20 | FIGUEIRÃO | MATO GROSSO DO SUL | Brasil | 5003900 | 50 | 33 | nan | nan | nan | Cerrado | 0.6 |
| ca0e4ad3-387a-31dc-8018-5fa8b459e1c8 | -20.28473 | -50.57272 | 2025-12-27 04:44:00 | NOAA-20 | JALES | SÃO PAULO | Brasil | 3524808 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| 35599a5a-e53e-3ec3-bff3-724bbd7084c4 | -21.30945 | -48.17776 | 2025-12-27 04:44:00 | NOAA-20 | JABOTICABAL | SÃO PAULO | Brasil | 3524303 | 35 | 33 | nan | nan | nan | Cerrado | 0.0 |
| e0b0c360-80e2-3c7c-a7c2-ec3cc83ef06d | -18.84259 | -53.62941 | 2025-12-27 04:44:00 | NOAA-20 | FIGUEIRÃO | MATO GROSSO DO SUL | Brasil | 5003900 | 50 | 33 | nan | nan | nan | Cerrado | 0.6 |
| b69d8e0a-c65b-3601-8a96-77249e80a3de | -19.31517 | -43.5253 | 2025-12-27 04:44:00 | NOAA-20 | SANTANA DO RIACHO | MINAS GERAIS | Brasil | 3159001 | 31 | 33 | nan | nan | nan | Cerrado | 3.6 |
| ad1fd327-1d6c-30da-a327-3a7fa768c19f | -29.97867 | -51.20431 | 2025-12-27 04:46:00 | NOAA-20 | PORTO ALEGRE | RIO GRANDE DO SUL | Brasil | 4314902 | 43 | 33 | nan | nan | nan | Pampa | 0.8 |
| b363a32c-e59b-34ca-8a8e-971679b8df4d | -0.0828 | -51.2738 | 2025-12-27 04:50:00 | GOES-19 | SANTANA | AMAPÁ | Brasil | 1600600 | 16 | 33 | nan | nan | nan | Amazônia | 82.2 |
| 30c3c9cb-9a31-3c1b-8807-d324adf2c0af | -10.4889 | -44.9235 | 2025-12-27 04:50:00 | GOES-19 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 67.2 |
| 47d9b82f-013f-3794-8dfb-d62cd553f775 | 2.5247 | -60.982 | 2025-12-27 04:50:00 | GOES-19 | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 73.6 |
| b2ae6995-be33-31b6-8684-e976a1977110 | -0.0828 | -51.2946 | 2025-12-27 04:50:00 | GOES-19 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 60.8 |
| db7c4415-64af-33b4-97de-b1242c230a78 | 2.5247 | -61.0009 | 2025-12-27 04:50:00 | GOES-19 | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 56.2 |
| d13e8419-9f9a-38bc-8961-1549d9668cfa | 2.5065 | -60.9822 | 2025-12-27 04:50:00 | GOES-19 | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 56.0 |
| 3e251a9c-68b6-36d1-b7f1-5e0304eca69e | -0.0828 | -51.2738 | 2025-12-27 05:00:00 | GOES-19 | SANTANA | AMAPÁ | Brasil | 1600600 | 16 | 33 | nan | nan | nan | Amazônia | 82.0 |
| c5763ae8-32dc-312a-b498-46dc56aecb59 | -0.0828 | -51.2946 | 2025-12-27 05:00:00 | GOES-19 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 59.0 |
| dabdc68f-f965-3388-8c51-94848195045e | -10.4889 | -44.9235 | 2025-12-27 05:00:00 | GOES-19 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 59.4 |
| 05de4308-bdde-3f2b-ac07-2a0941b66198 | 2.5065 | -60.9822 | 2025-12-27 05:00:00 | GOES-19 | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 59.3 |
| f53eec4c-24e7-3d51-95b5-4a2094f5b58d | 2.5247 | -60.982 | 2025-12-27 05:00:00 | GOES-19 | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 66.5 |
| 860c86eb-a08f-3f26-9af9-48516836d9cb | -0.1012 | -51.2738 | 2025-12-27 05:00:00 | GOES-19 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 55.9 |
| 1a2065be-8bed-38c5-a3b3-49325e146553 | -10.4889 | -44.9235 | 2025-12-27 05:10:00 | GOES-19 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 65.6 |
| cadce7ed-7212-381f-baa4-e249b08c3d7f | -0.1012 | -51.2738 | 2025-12-27 05:10:00 | GOES-19 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 57.8 |
| 588ae1d8-ac97-3451-9417-f585731f861c | -0.0828 | -51.2738 | 2025-12-27 05:10:00 | GOES-19 | SANTANA | AMAPÁ | Brasil | 1600600 | 16 | 33 | nan | nan | nan | Amazônia | 97.0 |
| 72fda56a-1feb-327d-a172-1f373874a932 | -0.0828 | -51.2946 | 2025-12-27 05:10:00 | GOES-19 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 56.6 |
| a0c3d0c2-cde2-3ed2-9bf0-309b323d82ab | 2.5247 | -60.982 | 2025-12-27 05:10:00 | GOES-19 | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 43.9 |
| aee5fad6-444e-3359-8744-32147bf975b4 | -0.1012 | -51.2738 | 2025-12-27 05:20:00 | GOES-19 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 64.0 |
| bf855a15-6fcd-3379-a414-16d5bd7d9e95 | -0.0828 | -51.2946 | 2025-12-27 05:20:00 | GOES-19 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 55.7 |
| e45834f9-eda0-3f75-a8b7-c450d48719aa | -0.0828 | -51.2738 | 2025-12-27 05:20:00 | GOES-19 | SANTANA | AMAPÁ | Brasil | 1600600 | 16 | 33 | nan | nan | nan | Amazônia | 95.3 |
| 8a464f13-9388-32c0-b3f1-455ee3cca9ec | 2.5247 | -60.982 | 2025-12-27 05:20:00 | GOES-19 | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 54.2 |
| 06f4c145-c130-3d3d-ae8b-3cb0cace4fc0 | -10.4889 | -44.9235 | 2025-12-27 05:20:00 | GOES-19 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 55.6 |
| 6bfe4eb8-16ca-3359-a86f-e63f3bd6f238 | 2.5065 | -60.9822 | 2025-12-27 05:20:00 | GOES-19 | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 56.6 |
| 379f4cf2-6840-3e47-9103-a1b6275eb72b | -3.90262 | -42.56366 | 2025-12-27 05:22:00 | AQUA_M-M | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 22.1 |
| 270d8d39-92c4-3309-97c6-640828058cae | -3.90672 | -42.53821 | 2025-12-27 05:22:00 | AQUA_M-M | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 24.8 |
| 1e4bacf7-cded-356b-8a44-55b0151ed8aa | -15.89248 | -43.43799 | 2025-12-27 05:25:00 | AQUA_M-M | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 21.8 |
| d730934e-d482-34e6-9eab-40f29b5cac8d | -15.88408 | -43.4498 | 2025-12-27 05:25:00 | AQUA_M-M | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 40.8 |
| 65c2cfe6-a1d1-3671-83b4-750d186965fe | -10.49029 | -44.92094 | 2025-12-27 05:25:00 | AQUA_M-M | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 72.4 |
| 26180b32-7e6c-37cc-b519-6a6cb72aacb0 | -15.88916 | -43.45619 | 2025-12-27 05:25:00 | AQUA_M-M | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 27.0 |
| ced92644-8241-38cb-b2be-7db70d7408aa | 2.51224 | -60.9828 | 2025-12-27 05:29:00 | NOAA-21 | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 179ab4ee-aee8-3852-9252-f578d7643be1 | -2.46164 | -47.77711 | 2025-12-27 05:29:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 8d3741cc-3bfa-369c-bd92-5bb41b96ba1e | -1.47835 | -54.2017 | 2025-12-27 05:29:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| d907950f-117f-30f8-922e-c17f8efb4210 | 2.51996 | -60.98871 | 2025-12-27 05:29:00 | NOAA-21 | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 9.6 |
| 374d2a07-3594-32f5-8d0a-08ac2180ffb2 | 2.51664 | -60.98922 | 2025-12-27 05:29:00 | NOAA-21 | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 9.6 |
| edd7e179-6c3a-3b5a-a23d-eb966d6d0e03 | -3.13143 | -52.85037 | 2025-12-27 05:29:00 | NOAA-21 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 4d7c05c2-51b3-35ef-b787-4446ec3b1989 | -2.45712 | -47.77514 | 2025-12-27 05:29:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 9.9 |
| b5e98254-b800-368d-ae40-291ab5ee8b85 | -3.02876 | -51.77596 | 2025-12-27 05:29:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 94df2cb5-74d9-3fac-a7b4-7d8664fb05fe | 2.51555 | -60.98228 | 2025-12-27 05:29:00 | NOAA-21 | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 2fda74fd-7579-3582-8c8d-d6d890f0ab14 | -0.11185 | -60.78131 | 2025-12-27 05:29:00 | NOAA-21 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 4ea8c25b-ded8-35a5-8a57-10ede03ffc1e | -2.3709 | -51.9094 | 2025-12-27 05:29:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 3c828bf1-8042-3a24-949c-a4431004b5eb | 2.39925 | -60.38983 | 2025-12-27 05:29:00 | NOAA-21 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 1.4 |
| c9dd10d0-e81f-3183-91b6-d00efcd6a0b0 | 2.51278 | -60.98627 | 2025-12-27 05:29:00 | NOAA-21 | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 4e71a8c4-656e-30b9-8ab6-2b797f8551a4 | 3.47671 | -60.23111 | 2025-12-27 05:29:00 | NOAA-21 | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 0.9 |
| a581ff24-6556-313d-a27f-fbd52abd2d3b | 1.82843 | -60.87379 | 2025-12-27 05:29:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 8.8 |
| e6ccb50c-cb52-3e7e-a082-8421a663ce3e | -3.13348 | -52.85003 | 2025-12-27 05:29:00 | NOAA-21 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 3bfd9447-1dfd-3eb4-a27a-c780595414cf | -0.09432 | -51.27723 | 2025-12-27 05:29:00 | NOAA-21 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 599d2bdf-752d-3bc9-a505-53ad759bafe8 | 3.38687 | -60.41814 | 2025-12-27 05:29:00 | NOAA-21 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 1.7 |
| f095ec1c-65f5-3639-b024-67c3c769e784 | 2.40255 | -60.38933 | 2025-12-27 05:29:00 | NOAA-21 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 8ab80b3e-eab3-3b95-8827-505e4ec403c7 | 2.50892 | -60.98331 | 2025-12-27 05:29:00 | NOAA-21 | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 7265b6ed-04a5-3627-b325-fd795ca75b7c | -0.08773 | -51.28347 | 2025-12-27 05:29:00 | NOAA-21 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 53.7 |
| b25274cf-5f1b-3516-afd9-9e2da4f529ce | -0.0932 | -51.28439 | 2025-12-27 05:29:00 | NOAA-21 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 0131fcf8-f7f3-35f0-8f74-823dbf1e19a7 | 2.51 | -60.99025 | 2025-12-27 05:29:00 | NOAA-21 | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 2.1 |
| dcbf2465-b6d7-330e-b317-abd40e38d852 | -3.00431 | -52.87587 | 2025-12-27 05:29:00 | NOAA-21 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 41a297f9-6216-3b02-9006-8a903a817520 | -2.89722 | -52.58882 | 2025-12-27 05:29:00 | NOAA-21 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 5dea2eaf-e289-3214-8b20-63271479cbe8 | 2.30588 | -61.62221 | 2025-12-27 05:29:00 | NOAA-21 | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 99b1fcdf-cf32-357f-9b84-a7ff61f7fc50 | 2.50946 | -60.98678 | 2025-12-27 05:29:00 | NOAA-21 | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 2.4 |
| b1f5e26e-e105-3e63-bec8-a08b179caf7e | -2.3758 | -51.91385 | 2025-12-27 05:29:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 6d48a578-119f-32f6-af41-d56dcbb892da | -3.74978 | -49.72229 | 2025-12-27 05:29:00 | NOAA-21 | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 2c89a5a4-a513-3278-aa59-95e6dd280309 | -3.02321 | -51.77515 | 2025-12-27 05:29:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 79110c3f-4b8e-3c4d-b7a3-00a1bc55e079 | -0.09376 | -51.28082 | 2025-12-27 05:29:00 | NOAA-21 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 793c5b9e-b6f5-3630-9b29-739564f659db | -0.0883 | -51.27984 | 2025-12-27 05:29:00 | NOAA-21 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 53.7 |
| d5835626-bdcf-3371-8c33-1a2be96fb0ef | -3.75548 | -49.728 | 2025-12-27 05:29:00 | NOAA-21 | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| a5045f2c-a6b2-3dc8-92e1-de94625a6d9b | -1.48295 | -54.20234 | 2025-12-27 05:29:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 99196efa-5973-3d37-9d68-a8dfe8a69d6e | -2.37143 | -51.90594 | 2025-12-27 05:29:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 84208bf7-d64e-3229-a0aa-79f46298c2a5 | 3.34127 | -60.41126 | 2025-12-27 05:29:00 | NOAA-21 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 59461c00-c730-3d47-89d1-2fc2a03730d6 | 0.75143 | -60.49508 | 2025-12-27 05:29:00 | NOAA-21 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b111191e-ac3c-3146-ba0f-c92665467e4c | 1.32926 | -60.73057 | 2025-12-27 05:29:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 038f70c4-f029-3d7b-9b13-aa56fa0c3bcd | -2.37685 | -51.9069 | 2025-12-27 05:29:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 330bd7dc-b5de-3f89-8d21-b2cd0e6c574f | -0.08886 | -51.27626 | 2025-12-27 05:29:00 | NOAA-21 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 19.0 |
| 86624346-ce1e-3bf0-ba99-f96f7376882b | 2.51386 | -60.9932 | 2025-12-27 05:29:00 | NOAA-21 | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 2.1 |
| de1476d6-fec6-3419-99c2-79949932cb2d | -2.98213 | -52.63334 | 2025-12-27 05:29:00 | NOAA-21 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 7099fa19-dc7e-35d0-938c-869f4ae7c5c3 | 0.44826 | -60.6235 | 2025-12-27 05:29:00 | NOAA-21 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 0.5 |
| f3665931-cbb5-359a-998a-5a1a7b4a6f17 | 3.25607 | -60.5196 | 2025-12-27 05:29:00 | NOAA-21 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 1.1 |
| de38ebe6-bf82-360f-bbce-9320d32145bc | -2.45616 | -47.78157 | 2025-12-27 05:29:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 9.9 |
| b2f4b0da-ad22-3091-aa67-b6bedce71a3a | 4.25365 | -60.87246 | 2025-12-27 05:29:00 | NOAA-21 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 3.5 |
| ba09038a-7a22-317f-86ce-249746b03919 | 2.51941 | -60.98524 | 2025-12-27 05:29:00 | NOAA-21 | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 5.0 |
| a0f14a5d-bc69-3462-bbcd-aea3f03b2d29 | 3.22843 | -61.19035 | 2025-12-27 05:29:00 | NOAA-21 | ALTO ALEGRE | RORAIMA | Brasil | 1400050 | 14 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 0a5ccd6a-b8d7-3f58-8cca-06faff635b29 | 3.22898 | -61.19387 | 2025-12-27 05:29:00 | NOAA-21 | ALTO ALEGRE | RORAIMA | Brasil | 1400050 | 14 | 33 | nan | nan | nan | Amazônia | 1.5 |
| b09a217f-a727-3010-b6a1-004f2b62a5ce | 2.51887 | -60.98177 | 2025-12-27 05:29:00 | NOAA-21 | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 075dbb38-ff3a-3e1f-ba0b-b1dea453eee9 | 2.51332 | -60.98973 | 2025-12-27 05:29:00 | NOAA-21 | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 0c4b522d-cb17-3e38-bc6f-139904a47a7f | 2.51718 | -60.99269 | 2025-12-27 05:29:00 | NOAA-21 | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 9.6 |
| f5b1def3-513a-38a1-bbd4-c20ffe459d2e | -0.08941 | -51.2727 | 2025-12-27 05:29:00 | NOAA-21 | SANTANA | AMAPÁ | Brasil | 1600600 | 16 | 33 | nan | nan | nan | Amazônia | 19.0 |
| fcde4dca-dbd4-3583-a29f-c7825f81061c | 2.5161 | -60.98575 | 2025-12-27 05:29:00 | NOAA-21 | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 9ea215f4-ae7b-3bbf-a5fc-bf3ea516583d | -0.10855 | -60.7808 | 2025-12-27 05:29:00 | NOAA-21 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 33b7e95b-2bcc-30d6-ab92-52df769ca418 | -2.37632 | -51.91038 | 2025-12-27 05:29:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| e98dc324-b6ad-3343-92e1-4e3f1bfde6b8 | 3.33839 | -61.21987 | 2025-12-27 05:29:00 | NOAA-21 | ALTO ALEGRE | RORAIMA | Brasil | 1400050 | 14 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 9c1376f7-0f73-3288-883d-5a8ff6265512 | -2.89672 | -52.59215 | 2025-12-27 05:29:00 | NOAA-21 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 31609279-3c58-3cdb-b450-181e3e76e26a | 3.47725 | -60.23456 | 2025-12-27 05:29:00 | NOAA-21 | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 0.9 |
| ea52432c-5334-3016-9691-43ddec796d2e | 2.51169 | -60.97933 | 2025-12-27 05:29:00 | NOAA-21 | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 229bd2fa-84a7-3cc3-b60b-8a7f602d3ab7 | 3.47617 | -60.22768 | 2025-12-27 05:29:00 | NOAA-21 | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c32988e9-34ff-3739-8dbd-af287793f5e2 | 2.5065 | -60.9822 | 2025-12-27 05:30:00 | GOES-19 | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 51.6 |
| 3fa63b5e-1e29-331d-bdf4-c278c5198e3c | -0.0828 | -51.2738 | 2025-12-27 05:30:00 | GOES-19 | SANTANA | AMAPÁ | Brasil | 1600600 | 16 | 33 | nan | nan | nan | Amazônia | 89.1 |
| 924b997a-1dcc-3bee-91ec-367c086dbfaa | 2.5247 | -60.982 | 2025-12-27 05:30:00 | GOES-19 | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 50.1 |
| 99025664-6f99-391b-9d46-4e6f6d3ed7e8 | -0.0828 | -51.2946 | 2025-12-27 05:30:00 | GOES-19 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 58.5 |


[Clique aqui para ver as próximas entradas](README14.md)
