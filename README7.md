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

## Dados Diários - Página 7

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 63442b34-45a1-340e-847e-f509c9bedb6a | -13.6676 | -48.79336 | 2026-07-19 04:19:00 | NOAA-20 | FORMOSO | GOIÁS | Brasil | 5208103 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| cd15388f-26b1-33be-b9d7-4d169c73e40c | -9.95692 | -50.5517 | 2026-07-19 04:19:00 | NOAA-20 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 8ec32c8c-e559-3e1a-a1b7-e527791c822c | -13.67214 | -48.78932 | 2026-07-19 04:19:00 | NOAA-20 | FORMOSO | GOIÁS | Brasil | 5208103 | 52 | 33 | nan | nan | nan | Cerrado | 27.8 |
| 61844ddd-9f49-3097-a91c-8545eb0565f0 | -10.91641 | -50.19362 | 2026-07-19 04:19:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 94e90ff5-8bf9-3381-85b5-a7371e048e34 | -12.52184 | -48.25203 | 2026-07-19 04:19:00 | NOAA-20 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| a3897c49-b116-37bb-876e-27d1e026083c | -9.07606 | -50.59497 | 2026-07-19 04:19:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| c05e9b37-44fc-303c-9bf1-20d480ad358a | -14.73746 | -44.67498 | 2026-07-19 04:19:00 | NOAA-20 | CÔNEGO MARINHO | MINAS GERAIS | Brasil | 3117836 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 79a4f230-6851-321f-93da-03ee0f587db2 | -11.60484 | -43.11389 | 2026-07-19 04:19:00 | NOAA-20 | MORPARÁ | BAHIA | Brasil | 2921609 | 29 | 33 | nan | nan | nan | Caatinga | 3.5 |
| fedd21fc-a8af-3599-b541-bc5a95ef2af9 | -11.64499 | -51.68364 | 2026-07-19 04:19:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| b7379bcf-f118-3b39-bdd4-70a5cb95de88 | -11.67752 | -54.58281 | 2026-07-19 04:19:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 3f2416f6-5977-3e3a-a357-7890959e2bc7 | -10.70134 | -46.61503 | 2026-07-19 04:19:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| b549f0c4-796e-39eb-9f28-fc9d4afcb658 | -2.78957 | -49.52174 | 2026-07-19 04:19:00 | NOAA-20 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| eb80d34a-8fb4-3b02-b112-1be9664410ec | -10.81713 | -50.23946 | 2026-07-19 04:19:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| b3f0771a-a15f-3158-8c99-7fc50e418fcc | -13.67746 | -48.78077 | 2026-07-19 04:19:00 | NOAA-20 | FORMOSO | GOIÁS | Brasil | 5208103 | 52 | 33 | nan | nan | nan | Cerrado | 16.3 |
| 44a4f1fa-909e-38c6-b5b5-35142f9bbe17 | -2.82991 | -48.86262 | 2026-07-19 04:19:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 6cd7a80d-b9d2-3b64-8b92-7ddda89dc06a | -10.70418 | -46.61953 | 2026-07-19 04:19:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| c974ee75-dfc6-3a69-a215-c13facc66f87 | -7.68911 | -55.36673 | 2026-07-19 04:19:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 67dd52b2-5af3-3432-bba9-0d563c74b033 | -10.68462 | -46.6081 | 2026-07-19 04:19:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 55480aa0-7383-3a15-acb0-2e48e34faeea | -11.98341 | -47.11108 | 2026-07-19 04:19:00 | NOAA-20 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 45096d82-5329-3f53-aa50-dcae59823f52 | -13.67588 | -48.78989 | 2026-07-19 04:19:00 | NOAA-20 | FORMOSO | GOIÁS | Brasil | 5208103 | 52 | 33 | nan | nan | nan | Cerrado | 27.8 |
| 7c3c7bbf-15df-35ba-9443-3b285568118c | -10.69787 | -46.61443 | 2026-07-19 04:19:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| a17368e4-e269-3509-9dda-6888f73182af | -11.97774 | -47.10191 | 2026-07-19 04:19:00 | NOAA-20 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| e1f35a6f-8f64-3962-bc7c-8936f9043ff1 | -10.81431 | -50.23055 | 2026-07-19 04:19:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| ec2117da-03ce-3a91-b474-eaa958993e5e | -13.18654 | -43.55367 | 2026-07-19 04:19:00 | NOAA-20 | BOM JESUS DA LAPA | BAHIA | Brasil | 2903904 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| fd41ebbf-dbca-3193-81df-74c94aefe1ba | -11.63135 | -47.95163 | 2026-07-19 04:19:00 | NOAA-20 | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 6eaab889-19ae-3985-810e-050c8b8494ab | -11.38179 | -47.51914 | 2026-07-19 04:19:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 2c3a6264-26be-3f50-b7d8-53077730aeb7 | -11.67678 | -54.58655 | 2026-07-19 04:19:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 3e51a853-034f-3892-a54c-29ff4eeb363a | -10.89845 | -50.31998 | 2026-07-19 04:19:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 210fedc3-e19d-3bb6-8a3d-449ebb61cd21 | -10.69944 | -46.62666 | 2026-07-19 04:19:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 7828857f-9a1a-3426-b255-b29ad1286ef3 | -11.96874 | -47.11262 | 2026-07-19 04:19:00 | NOAA-20 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 5.2 |
| a73d4f75-c07a-3414-9a02-5be29d6b87d0 | -10.902 | -50.32486 | 2026-07-19 04:19:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 68e63334-727a-3168-8daf-7416c4283a1a | -7.69008 | -55.36158 | 2026-07-19 04:19:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| ab88c34a-72d1-36e8-a974-a93f480d3866 | -11.96524 | -47.11201 | 2026-07-19 04:19:00 | NOAA-20 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 56dbbfb8-25b5-31f0-8109-31faccce1730 | -3.24257 | -47.91809 | 2026-07-19 04:19:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 31468d00-b587-3f52-beb6-7a0987da7be5 | -14.5666 | -52.08154 | 2026-07-19 04:19:00 | NOAA-20 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 49d14204-19bb-3b57-a1ab-29177f015dbc | -9.95802 | -48.85611 | 2026-07-19 04:19:00 | NOAA-20 | BARROLÂNDIA | TOCANTINS | Brasil | 1703107 | 17 | 33 | nan | nan | nan | Cerrado | 10.1 |
| ee0872d8-2fce-3a1d-8e5a-a5be4534c931 | -9.23811 | -49.30048 | 2026-07-19 04:19:00 | NOAA-20 | DOIS IRMÃOS DO TOCANTINS | TOCANTINS | Brasil | 1707207 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 409b81be-01c2-3ae7-aad1-b50d1e7109a1 | -12.65883 | -48.22009 | 2026-07-19 04:19:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 4.9 |
| ae35a447-e491-3473-9b48-b7c969dcae7a | -11.77025 | -45.97731 | 2026-07-19 04:19:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 66bbaa5f-ce15-30df-80f4-51a7f910bc94 | -10.69249 | -46.62546 | 2026-07-19 04:19:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| bbc36148-c787-358f-a26f-1cc1e4cfd92f | -8.9393 | -47.6083 | 2026-07-19 04:19:00 | NOAA-20 | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 8ec98539-b013-3207-9d90-dc160aa5e2b9 | -10.81927 | -50.22729 | 2026-07-19 04:19:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 293bd284-eb36-3a15-96b9-747add5fdcd3 | -9.10059 | -50.61348 | 2026-07-19 04:19:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| b2aebee7-760f-3c4d-b675-caddb24f08d8 | -13.67373 | -48.78017 | 2026-07-19 04:19:00 | NOAA-20 | FORMOSO | GOIÁS | Brasil | 5208103 | 52 | 33 | nan | nan | nan | Cerrado | 16.3 |
| 2b8be907-9250-3398-8328-d45f71c201e9 | -10.8221 | -50.23618 | 2026-07-19 04:19:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 2a52ac68-45a3-3863-8911-dad5a242d697 | -12.67132 | -48.21324 | 2026-07-19 04:19:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 3003ed2b-45f0-397c-acbc-0af9b843c813 | -9.17114 | -49.63935 | 2026-07-19 04:19:00 | NOAA-20 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 7e50e3de-da56-3195-9515-983b9f82dc6f | -2.82921 | -48.86699 | 2026-07-19 04:19:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 327b5415-e81a-33ab-86c7-86e888c57913 | -12.66325 | -48.21634 | 2026-07-19 04:19:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 27788a68-92cf-3ca7-bb41-8d6522f5c768 | -10.68965 | -46.62097 | 2026-07-19 04:19:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 329b8642-dc46-3eaa-a122-b1af88d91094 | -2.78053 | -49.4611 | 2026-07-19 04:19:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| fec88a8a-3e4b-382f-9fd3-8e686c7d8df7 | -13.66841 | -48.78872 | 2026-07-19 04:19:00 | NOAA-20 | FORMOSO | GOIÁS | Brasil | 5208103 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 5327c939-000d-35f6-849d-9e9016b81510 | -8.93262 | -47.60254 | 2026-07-19 04:19:00 | NOAA-20 | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 7.7 |
| 023ae531-aef2-3552-aec2-953838d91ff5 | -8.92891 | -47.60189 | 2026-07-19 04:19:00 | NOAA-20 | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| ec699db4-98b1-3f2d-b3c8-fce62488b918 | -11.9694 | -47.10865 | 2026-07-19 04:19:00 | NOAA-20 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 0e478400-a55f-38be-a50b-4914b37f1000 | -11.37892 | -47.51421 | 2026-07-19 04:19:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 62e067b7-a004-34ae-a343-6ba21fd21cae | -8.94082 | -47.59931 | 2026-07-19 04:19:00 | NOAA-20 | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 8.3 |
| a322fb07-0dd7-3724-9268-0d46fa3334d0 | -11.77481 | -45.97055 | 2026-07-19 04:19:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| ed79fb07-f610-33d6-a5c8-46e85501077a | -12.08053 | -53.34758 | 2026-07-19 04:19:00 | NOAA-20 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 3.4 |
| d1b52e7b-ab51-33bc-a7fb-2335e85dac97 | -13.6764 | -48.7786 | 2026-07-19 04:20:00 | GOES-19 | FORMOSO | GOIÁS | Brasil | 5208103 | 52 | 33 | nan | nan | nan | Cerrado | 81.3 |
| 3a81983b-b716-35a2-869e-ae9e2bc3ef42 | -22.91253 | -43.44259 | 2026-07-19 04:21:00 | NOAA-20 | RIO DE JANEIRO | RIO DE JANEIRO | Brasil | 3304557 | 33 | 33 | nan | nan | nan | Mata Atlântica | 3.1 |
| 626e2fb3-a997-31a3-9ecb-65dd1d09f4a2 | -23.37548 | -47.31985 | 2026-07-19 04:21:00 | NOAA-20 | ITU | SÃO PAULO | Brasil | 3523909 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 62f90ccc-015a-34e2-a263-01c2c37207b1 | -17.87083 | -45.54708 | 2026-07-19 04:21:00 | NOAA-20 | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| d1e50901-ab11-3db0-97d1-48b9a940d300 | -20.56806 | -54.57367 | 2026-07-19 04:21:00 | NOAA-20 | CAMPO GRANDE | MATO GROSSO DO SUL | Brasil | 5002704 | 50 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 97ff274a-3193-3f01-8614-74c6bef62f9c | -19.9865 | -43.9702 | 2026-07-19 04:21:00 | NOAA-20 | BELO HORIZONTE | MINAS GERAIS | Brasil | 3106200 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 28939de8-5b8e-3380-8d5a-c382e328f775 | -19.72833 | -48.03165 | 2026-07-19 04:21:00 | NOAA-20 | UBERABA | MINAS GERAIS | Brasil | 3170107 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| fc47f2e6-0073-3fa7-b08d-1a27909fdaad | -16.80884 | -54.59345 | 2026-07-19 04:21:00 | NOAA-20 | RONDONÓPOLIS | MATO GROSSO | Brasil | 5107602 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| bdb15498-bf6b-32cd-8f14-4a47625ac7cc | -19.72207 | -46.17087 | 2026-07-19 04:21:00 | NOAA-20 | CAMPOS ALTOS | MINAS GERAIS | Brasil | 3111507 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 25633d63-7898-3773-80ca-5513573149cc | -22.9089 | -43.44176 | 2026-07-19 04:21:00 | NOAA-20 | RIO DE JANEIRO | RIO DE JANEIRO | Brasil | 3304557 | 33 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| fdc2a363-f3ca-3e6a-b7c1-ed0ebc58dcc3 | -21.43092 | -41.16932 | 2026-07-19 04:21:00 | NOAA-20 | SÃO FRANCISCO DE ITABAPOANA | RIO DE JANEIRO | Brasil | 3304755 | 33 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 2c462f66-c7a3-3027-943d-db7814f53105 | -22.1887 | -45.82014 | 2026-07-19 04:21:00 | NOAA-20 | SÃO SEBASTIÃO DA BELA VISTA | MINAS GERAIS | Brasil | 3164407 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| 8a93040d-0fe7-3c90-92d1-c94d3a12deae | -17.37412 | -42.7206 | 2026-07-19 04:21:00 | NOAA-20 | VEREDINHA | MINAS GERAIS | Brasil | 3171071 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| bf3a8d54-5c1d-3b0a-8989-cadf27d33443 | -22.2527 | -52.88129 | 2026-07-19 04:21:00 | NOAA-20 | ANAURILÂNDIA | MATO GROSSO DO SUL | Brasil | 5000807 | 50 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| afd7fb88-623c-3e33-ae7f-553aef596639 | -23.22936 | -46.1361 | 2026-07-19 04:21:00 | NOAA-20 | IGARATÁ | SÃO PAULO | Brasil | 3520202 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 73ce0586-94c1-3154-ab21-fda5b3ee6c0a | -22.91058 | -43.44976 | 2026-07-19 04:21:00 | NOAA-20 | RIO DE JANEIRO | RIO DE JANEIRO | Brasil | 3304557 | 33 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| d90320f4-eca7-3a09-a5f2-3d9d3472c7c7 | -23.26884 | -47.17686 | 2026-07-19 04:21:00 | NOAA-20 | CABREÚVA | SÃO PAULO | Brasil | 3508405 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| fbc9d145-9a8e-3a9f-a788-39f7dfddf500 | -22.82679 | -46.15453 | 2026-07-19 04:21:00 | NOAA-20 | CAMANDUCAIA | MINAS GERAIS | Brasil | 3110509 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| f34b4392-2b50-3664-9e00-e03ace03f354 | -20.56815 | -54.57521 | 2026-07-19 04:21:00 | NOAA-20 | CAMPO GRANDE | MATO GROSSO DO SUL | Brasil | 5002704 | 50 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 749ecc50-d99f-3a91-967a-f7067483ada7 | -23.37217 | -47.31923 | 2026-07-19 04:21:00 | NOAA-20 | ITU | SÃO PAULO | Brasil | 3523909 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 41d14aaf-811c-3e53-bcf2-fc916f68b9ba | -18.48808 | -46.9201 | 2026-07-19 04:21:00 | NOAA-20 | COROMANDEL | MINAS GERAIS | Brasil | 3119302 | 31 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 71b64a65-a37e-38c5-9406-b4381e23ea7d | -21.53104 | -46.7616 | 2026-07-19 04:21:00 | NOAA-20 | TAPIRATIBA | SÃO PAULO | Brasil | 3553609 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.8 |
| 2f528efb-9fda-38df-922e-b8bfdfe3d4a7 | -22.80114 | -43.54701 | 2026-07-19 04:21:00 | NOAA-20 | NOVA IGUAÇU | RIO DE JANEIRO | Brasil | 3303500 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 0324a915-1c1b-3263-8d74-05d0f31c106c | -17.36761 | -42.71504 | 2026-07-19 04:21:00 | NOAA-20 | VEREDINHA | MINAS GERAIS | Brasil | 3171071 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 56fedc2d-fb1b-3e57-aaf3-b5b547ddf48b | -17.37118 | -42.71564 | 2026-07-19 04:21:00 | NOAA-20 | VEREDINHA | MINAS GERAIS | Brasil | 3171071 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| ce4882ef-f57d-3f60-830f-05f3aa11b681 | -15.35058 | -51.20071 | 2026-07-19 04:21:00 | NOAA-20 | BRITÂNIA | GOIÁS | Brasil | 5203807 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 63b094d9-8b9f-34f2-872e-92c258374b4c | -16.80946 | -54.59036 | 2026-07-19 04:21:00 | NOAA-20 | RONDONÓPOLIS | MATO GROSSO | Brasil | 5107602 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 3ace7330-f6d2-348c-b6ac-fec13244d2dd | -22.90755 | -43.45153 | 2026-07-19 04:21:00 | NOAA-20 | RIO DE JANEIRO | RIO DE JANEIRO | Brasil | 3304557 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 24e9e3eb-87ed-3801-916d-58ecf2b4b45e | -22.91123 | -43.44481 | 2026-07-19 04:21:00 | NOAA-20 | RIO DE JANEIRO | RIO DE JANEIRO | Brasil | 3304557 | 33 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| 4110ee6c-c264-3fb9-8121-6f8a5048f71c | -20.65217 | -41.90381 | 2026-07-19 04:21:00 | NOAA-20 | ESPERA FELIZ | MINAS GERAIS | Brasil | 3124203 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 91dc7c18-0206-39cc-bf38-ad0f61387b91 | -19.85072 | -57.9215 | 2026-07-19 04:21:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.2 |
| 78ef29ae-8e12-3462-8c69-e22d7c848434 | -15.45994 | -54.35265 | 2026-07-19 04:21:00 | NOAA-20 | PRIMAVERA DO LESTE | MATO GROSSO | Brasil | 5107040 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 7394093b-d75c-3f82-b7ac-3c710b55a585 | -15.95624 | -47.18894 | 2026-07-19 04:21:00 | NOAA-20 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| a8f3bb48-1289-32db-bce1-f82249b50d73 | -21.7823 | -48.83034 | 2026-07-19 04:21:00 | NOAA-20 | IBITINGA | SÃO PAULO | Brasil | 3519600 | 35 | 33 | nan | nan | nan | Cerrado | 0.7 |
| e52f3cee-9879-372e-a3cc-cfa7169247b9 | -23.29054 | -46.15442 | 2026-07-19 04:21:00 | NOAA-20 | SANTA ISABEL | SÃO PAULO | Brasil | 3546801 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 3124c7b1-def3-3e47-ba1f-04652f48eaa0 | -18.72985 | -54.20175 | 2026-07-19 04:21:00 | NOAA-20 | FIGUEIRÃO | MATO GROSSO DO SUL | Brasil | 5003900 | 50 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 57bb6fd3-53d1-3597-896e-343ffa87d8e7 | -22.79616 | -43.77702 | 2026-07-19 04:21:00 | NOAA-20 | SEROPÉDICA | RIO DE JANEIRO | Brasil | 3305554 | 33 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 22fe93ab-a460-3f3a-9d5c-1947b2c61195 | -23.22769 | -46.23774 | 2026-07-19 04:21:00 | NOAA-20 | SANTA ISABEL | SÃO PAULO | Brasil | 3546801 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.7 |
| f8f45018-3442-3fbe-a397-8135ee1816a5 | -20.52872 | -57.39732 | 2026-07-19 04:21:00 | NOAA-20 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 23961ebe-e769-3469-b3f1-c761e4f5f09b | -19.74597 | -46.47142 | 2026-07-19 04:21:00 | NOAA-20 | PRATINHA | MINAS GERAIS | Brasil | 3153004 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 42e0008f-fdb4-3533-9cac-603625a39f2d | -22.90227 | -43.43541 | 2026-07-19 04:21:00 | NOAA-20 | RIO DE JANEIRO | RIO DE JANEIRO | Brasil | 3304557 | 33 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |


[Clique aqui para ver as próximas entradas](README8.md)
