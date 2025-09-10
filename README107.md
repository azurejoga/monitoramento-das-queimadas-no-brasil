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

## Dados Diários - Página 107

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 921e75d5-9173-3312-baf4-af9ba04f768e | -12.1885 | -50.6482 | 2025-09-10 12:30:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 168.6 |
| b7a862e2-a7ae-33bf-a627-4a43e0215ccb | -9.0605 | -49.8014 | 2025-09-10 12:30:00 | GOES-19 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 68.1 |
| 290aed7d-5312-305c-8242-4fd500695a41 | -9.0579 | -46.9688 | 2025-09-10 12:30:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 70.4 |
| c078b854-9ca1-3ca2-9976-962cd999e493 | -12.1889 | -50.6267 | 2025-09-10 12:30:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 137.7 |
| ec99ff9c-9ed0-374f-a927-c9cfa4f0cdb4 | -9.7223 | -48.0907 | 2025-09-10 12:30:00 | GOES-19 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 82.9 |
| 0e3860eb-bc33-30b2-bd09-dbdf7a363d58 | -12.0304 | -51.0296 | 2025-09-10 12:30:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 109.1 |
| 322989c2-690f-38fd-a1f4-62df0518be8e | -11.4515 | -50.3268 | 2025-09-10 12:30:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 103.9 |
| 51428678-3478-35a3-96c5-581c98048c01 | -9.0232 | -49.7834 | 2025-09-10 12:30:00 | GOES-19 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 76.8 |
| 7d21eb65-43bc-38b9-b66e-9fc8d10ed9c0 | -12.0307 | -51.0083 | 2025-09-10 12:30:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 97.7 |
| 2e64fb0e-579e-35c8-ad74-d6fae6de12ba | -9.0603 | -49.8228 | 2025-09-10 12:30:00 | GOES-19 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 126.4 |
| 2cbfc9b2-1afe-322c-b131-850c50b8ef2c | -7.4845 | -48.2349 | 2025-09-10 12:30:00 | GOES-19 | ARAGUAÍNA | TOCANTINS | Brasil | 1702109 | 17 | 33 | nan | nan | nan | Cerrado | 91.7 |
| 4ce6875d-b822-3b4e-a1cd-20dcf50809d7 | -7.4639 | -44.9433 | 2025-09-10 12:30:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 81.3 |
| 6a3d422f-1285-3dd0-99c7-ee83ffc2e412 | -11.507 | -50.4276 | 2025-09-10 12:30:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 95.6 |
| 5d7e3a35-944d-32c4-9566-ce4c4ddbb6c1 | -11.4657 | -43.6195 | 2025-09-10 12:30:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 131.1 |
| 2e32ac41-0c41-34e8-85a7-81376704b66c | -8.0796 | -48.619 | 2025-09-10 12:30:00 | GOES-19 | COLINAS DO TOCANTINS | TOCANTINS | Brasil | 1705508 | 17 | 33 | nan | nan | nan | Amazônia | 116.3 |
| 53eb4037-5bb4-3757-b2a2-04b1581a33cf | -11.4452 | -43.6934 | 2025-09-10 12:30:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 92.0 |
| 9a2fbbc6-e1c9-3b23-8ea3-9353f7e286af | -9.06 | -49.8442 | 2025-09-10 12:30:00 | GOES-19 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 67.6 |
| d8d00123-48cf-3281-8cfb-112a8ddc0eed | -10.3882 | -50.5477 | 2025-09-10 12:30:00 | GOES-19 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 308.5 |
| a1da6ce7-44d6-3fc5-a9b7-ab1dd93f4ac8 | -8.0794 | -48.6407 | 2025-09-10 12:30:00 | GOES-19 | BANDEIRANTES DO TOCANTINS | TOCANTINS | Brasil | 1703057 | 17 | 33 | nan | nan | nan | Amazônia | 251.6 |
| dc21d093-1ed4-30a8-b309-09ee5641dffb | -9.0768 | -46.9668 | 2025-09-10 12:30:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 104.4 |
| c808f827-8894-3f3c-86b6-f05567bc9707 | -9.3437 | -46.7603 | 2025-09-10 12:30:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 88.7 |
| 41a3c3f7-4ef8-36dd-814e-b3d57eb4855e | -11.4465 | -43.6224 | 2025-09-10 12:30:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 121.9 |
| 9b736076-5781-314d-8bda-ce66b323217c | -10.3885 | -50.5264 | 2025-09-10 12:30:00 | GOES-19 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 115.7 |
| 4a9175af-83ff-3951-8500-a8775f445054 | -8.0416 | -48.6656 | 2025-09-10 12:30:00 | GOES-19 | BANDEIRANTES DO TOCANTINS | TOCANTINS | Brasil | 1703057 | 17 | 33 | nan | nan | nan | Amazônia | 94.4 |
| d14ed7c0-2cd3-351c-a54f-a16cc7ae280e | -9.042 | -49.7817 | 2025-09-10 12:30:00 | GOES-19 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 116.6 |
| 523d418f-48cd-3aff-b3e8-24f27e2dbb41 | -8.49 | -45.6826 | 2025-09-10 12:30:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 90.3 |
| e6b96215-e742-302d-87bf-f425ed8ed94a | -6.2595 | -43.4129 | 2025-09-10 12:30:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 101.8 |
| 3fa4310b-648d-30dd-a080-48e1d9106e39 | -12.0495 | -51.0274 | 2025-09-10 12:30:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 119.0 |
| e71459ef-d0e8-3150-ab36-6c5a81833a83 | -6.8446 | -44.9075 | 2025-09-10 12:30:00 | GOES-19 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 90.3 |
| 9ce70b59-4936-3ed7-884c-1615330a9e9d | -14.5125 | -53.9367 | 2025-09-10 12:30:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 78.3 |
| b834eeb1-5618-3ceb-82fa-c54b8b927c45 | -5.4155 | -43.4552 | 2025-09-10 12:30:00 | GOES-19 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 71.8 |
| 7394d73d-9879-3c24-9772-0e2c7a7a783e | -12.9972 | -48.0354 | 2025-09-10 12:30:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 78.6 |
| ee9c633f-c321-356f-907b-2aea32f67756 | -14.4644 | -53.3361 | 2025-09-10 12:40:00 | GOES-19 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 75.6 |
| 2803a547-caa8-35a6-b9dc-b91c074adb8c | -6.8446 | -44.9075 | 2025-09-10 12:40:00 | GOES-19 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 81.1 |
| 0115a013-3f33-3d1e-9619-3abd72519fe9 | -8.0794 | -48.6407 | 2025-09-10 12:40:00 | GOES-19 | BANDEIRANTES DO TOCANTINS | TOCANTINS | Brasil | 1703057 | 17 | 33 | nan | nan | nan | Amazônia | 329.3 |
| 8f061d31-a5e1-3cae-bf43-9cae893eae97 | -11.3905 | -43.5365 | 2025-09-10 12:40:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 112.2 |
| c1c19db5-dda9-3d74-b5af-140e7e5295c1 | -6.8897 | -47.8897 | 2025-09-10 12:40:00 | GOES-19 | WANDERLÂNDIA | TOCANTINS | Brasil | 1722081 | 17 | 33 | nan | nan | nan | Cerrado | 97.1 |
| 6b3e6a8a-5de3-345a-8330-63775ff203ff | -8.4903 | -45.66 | 2025-09-10 12:40:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 113.8 |
| 0fa2c982-6862-3c69-9baa-5c1e1071970a | -9.4385 | -46.7276 | 2025-09-10 12:40:00 | GOES-19 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 72.4 |
| e36bd74d-3db3-3cec-921d-97cbcec53076 | -12.1889 | -50.6267 | 2025-09-10 12:40:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 105.9 |
| 5381cd1a-beb3-390a-9d6f-7b30681b001b | -8.0796 | -48.619 | 2025-09-10 12:40:00 | GOES-19 | COLINAS DO TOCANTINS | TOCANTINS | Brasil | 1705508 | 17 | 33 | nan | nan | nan | Amazônia | 138.6 |
| 35581269-4c1d-30d9-b714-10ffbabf604c | -11.4515 | -50.3268 | 2025-09-10 12:40:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 121.1 |
| c63743fb-5a0f-30ca-8f0b-879a02a5ce56 | -10.3885 | -50.5264 | 2025-09-10 12:40:00 | GOES-19 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 96.7 |
| 0eb56a5a-d700-3dcc-bf73-8ec44d52c345 | -6.2595 | -43.4129 | 2025-09-10 12:40:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 133.0 |
| e085aa61-011e-31a3-b169-461305057af4 | -6.8895 | -47.9115 | 2025-09-10 12:40:00 | GOES-19 | WANDERLÂNDIA | TOCANTINS | Brasil | 1722081 | 17 | 33 | nan | nan | nan | Cerrado | 96.3 |
| 11ab8acd-d929-3421-9a12-33b3271fe94b | -12.0495 | -51.0274 | 2025-09-10 12:40:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 129.8 |
| 0a947790-9376-333d-98c2-fe5f45b5883e | -17.3167 | -46.6991 | 2025-09-10 12:40:00 | GOES-19 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 75.6 |
| a4a9273a-ec99-3dc7-9d32-55c7991ed57d | -12.1885 | -50.6482 | 2025-09-10 12:40:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 144.5 |
| 6d63f834-d1f9-38ff-887f-aa1d98f3eed2 | -11.4097 | -43.5336 | 2025-09-10 12:40:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 138.4 |
| 2bd35e94-09db-3faa-9de6-c226fc867d0c | -9.0579 | -46.9688 | 2025-09-10 12:40:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 78.7 |
| 5b306c87-aef4-3268-b0d1-4ebe1b4738f7 | -12.0307 | -51.0083 | 2025-09-10 12:40:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 107.6 |
| 62f1c6b2-8c84-3f20-9e1a-5afa98409eea | -9.055 | -45.7583 | 2025-09-10 12:40:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 74.9 |
| fc811cdb-d615-35a2-8ece-b4f471da08c6 | -8.994 | -46.0808 | 2025-09-10 12:40:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 117.0 |
| 66a131a4-e9fa-3293-957a-57c8b62589c4 | -14.6658 | -44.0379 | 2025-09-10 12:40:00 | GOES-19 | MANGA | MINAS GERAIS | Brasil | 3139300 | 31 | 33 | nan | nan | nan | Caatinga | 108.7 |
| 66d02cf1-7f30-332d-85b7-0427b2cad257 | -6.8523 | -47.8925 | 2025-09-10 12:40:00 | GOES-19 | WANDERLÂNDIA | TOCANTINS | Brasil | 1722081 | 17 | 33 | nan | nan | nan | Cerrado | 93.4 |
| 402880cf-9cae-34f6-94bc-2ae33f16a41a | -8.49 | -45.6826 | 2025-09-10 12:40:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 223.1 |
| 74586900-84d8-3bb5-b878-ed9646792235 | -5.8582 | -44.2088 | 2025-09-10 12:40:00 | GOES-19 | JATOBÁ | MARANHÃO | Brasil | 2105450 | 21 | 33 | nan | nan | nan | Cerrado | 100.7 |
| 80363eb2-25bb-394c-84a8-8ca0173c8dc8 | -8.0416 | -48.6656 | 2025-09-10 12:40:00 | GOES-19 | BANDEIRANTES DO TOCANTINS | TOCANTINS | Brasil | 1703057 | 17 | 33 | nan | nan | nan | Amazônia | 90.0 |
| 16ada483-4446-36fd-8e29-a27cc204ec5b | -8.9943 | -46.0583 | 2025-09-10 12:40:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 97.7 |
| be5ae188-2644-3b42-943c-6bb72e8e2b3e | -9.0768 | -46.9668 | 2025-09-10 12:40:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 114.4 |
| ed42786d-94dd-3b6f-91a3-9335a5b26494 | -11.3393 | -46.5193 | 2025-09-10 12:40:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 119.5 |
| 0569bba0-bbc0-3ed2-baf6-629487a08202 | -12.0304 | -51.0296 | 2025-09-10 12:40:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 113.5 |
| 29979f8e-56ed-3ce2-bb85-ff69e3eb7085 | -6.8521 | -47.9143 | 2025-09-10 12:40:00 | GOES-19 | WANDERLÂNDIA | TOCANTINS | Brasil | 1722081 | 17 | 33 | nan | nan | nan | Cerrado | 130.7 |
| 26733bcf-bdbb-333f-9418-375b64dd31e7 | -10.3882 | -50.5477 | 2025-09-10 12:40:00 | GOES-19 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 259.3 |
| b89eff92-8264-3104-b504-a902f0b1349c | -7.5033 | -48.2334 | 2025-09-10 12:40:00 | GOES-19 | NOVA OLINDA | TOCANTINS | Brasil | 1714880 | 17 | 33 | nan | nan | nan | Cerrado | 115.6 |
| 9ba6c68c-1a08-375c-af08-070f0c804499 | -11.507 | -50.4276 | 2025-09-10 12:40:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 153.6 |
| 7aadd66a-b51f-38d5-b939-af7b573b1a8c | -6.8519 | -47.9361 | 2025-09-10 12:40:00 | GOES-19 | WANDERLÂNDIA | TOCANTINS | Brasil | 1722081 | 17 | 33 | nan | nan | nan | Cerrado | 147.8 |
| cc054ddf-1cfc-36a5-9c6a-cd19fb6b8cd1 | -7.4845 | -48.2349 | 2025-09-10 12:40:00 | GOES-19 | ARAGUAÍNA | TOCANTINS | Brasil | 1702109 | 17 | 33 | nan | nan | nan | Cerrado | 147.4 |
| 1a09b967-223f-3eaa-9d5e-bece0bf62198 | -14.5125 | -53.9367 | 2025-09-10 12:40:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 71.7 |
| c02a24e6-da71-3b2c-8ee0-182d221584dc | -11.1187 | -48.4369 | 2025-09-10 12:40:00 | GOES-19 | IPUEIRAS | TOCANTINS | Brasil | 1709807 | 17 | 33 | nan | nan | nan | Cerrado | 79.0 |
| 99f6ba25-7933-3145-ae0b-f5e3c13e96a5 | -11.3389 | -46.5419 | 2025-09-10 12:40:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 129.2 |
| f09bbc3e-96ed-3ed7-9286-1245ed0a99bf | -8.49 | -45.6826 | 2025-09-10 12:50:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 224.1 |
| 5b3cde3a-4c24-3e4a-a5a9-9054747d1d45 | -8.0796 | -48.619 | 2025-09-10 12:50:00 | GOES-19 | COLINAS DO TOCANTINS | TOCANTINS | Brasil | 1705508 | 17 | 33 | nan | nan | nan | Amazônia | 141.4 |
| 9f5c04c6-9a19-35ad-b32c-7caab8bfa653 | -11.1247 | -52.0149 | 2025-09-10 12:50:00 | GOES-19 | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Amazônia | 83.6 |
| 4485f0ad-5c73-39d5-8da7-ddcc43774237 | -14.5125 | -53.9367 | 2025-09-10 12:50:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 64.8 |
| 26a70614-d63b-3edd-9e4e-17a4bc482fbb | -11.4452 | -43.6934 | 2025-09-10 12:50:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 251.9 |
| c4a903aa-4df4-343b-8345-5bda028f3e2f | -10.3882 | -50.5477 | 2025-09-10 12:50:00 | GOES-19 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 273.8 |
| 19c28dbb-d881-3d81-b131-605819fa573f | -8.4903 | -45.66 | 2025-09-10 12:50:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 138.5 |
| a6d01bec-aa91-3faf-a823-e175ef41f989 | -12.1885 | -50.6482 | 2025-09-10 12:50:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 176.4 |
| 79c3a14a-5800-3194-b888-81d0a7d6e02d | -9.1142 | -46.9851 | 2025-09-10 12:50:00 | GOES-19 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 83.9 |
| 8194926b-1e7f-39fe-b1a9-7853f7da4b73 | -11.4097 | -43.5336 | 2025-09-10 12:50:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 99.3 |
| 2d588df7-a928-3698-a579-438c87f5f2bd | -8.0794 | -48.6407 | 2025-09-10 12:50:00 | GOES-19 | BANDEIRANTES DO TOCANTINS | TOCANTINS | Brasil | 1703057 | 17 | 33 | nan | nan | nan | Amazônia | 297.2 |
| 9338faf9-ea78-3432-a3df-4b4589c87544 | -7.4845 | -48.2349 | 2025-09-10 12:50:00 | GOES-19 | ARAGUAÍNA | TOCANTINS | Brasil | 1702109 | 17 | 33 | nan | nan | nan | Cerrado | 165.1 |
| 04ea3df6-8133-31f0-ba99-b742f0a787dd | -12.0307 | -51.0083 | 2025-09-10 12:50:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 145.6 |
| af482d36-c7ec-3c5e-95de-64d315c8e282 | -11.507 | -50.4276 | 2025-09-10 12:50:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 176.5 |
| 09c71f2f-cbc3-396f-b8de-83651d195658 | -12.0495 | -51.0274 | 2025-09-10 12:50:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 188.9 |
| c3dbaeb0-6814-387c-9431-9c6328887eaa | -10.1464 | -46.1973 | 2025-09-10 12:50:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 109.1 |
| 25109018-3987-38eb-870b-0799d004e214 | -9.3437 | -46.7603 | 2025-09-10 12:50:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 92.9 |
| 8ec2660a-c707-3120-8325-4ae47b052323 | -10.3885 | -50.5264 | 2025-09-10 12:50:00 | GOES-19 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 145.7 |
| e519de8f-3d78-3b64-b198-9962fc8f238c | -8.0416 | -48.6656 | 2025-09-10 12:50:00 | GOES-19 | BANDEIRANTES DO TOCANTINS | TOCANTINS | Brasil | 1703057 | 17 | 33 | nan | nan | nan | Amazônia | 102.3 |
| 9b1d23b5-2f98-3c70-98bb-63ea969ff08f | -11.488 | -50.4298 | 2025-09-10 12:50:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 125.2 |
| 1bf9eedf-3f2c-30d0-95ab-b58a600ab321 | -12.0304 | -51.0296 | 2025-09-10 12:50:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 161.6 |
| 491c6312-c06f-339d-a2b2-819d553ae001 | -11.4702 | -50.3461 | 2025-09-10 12:50:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 114.4 |
| cc969e26-11ba-3d63-b32c-269abe3589c0 | -11.4705 | -50.3247 | 2025-09-10 12:50:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 186.8 |
| 882cad3b-d7cb-3cba-a785-d0ce1ae69fb4 | -9.0768 | -46.9668 | 2025-09-10 12:50:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 120.1 |
| 9a060052-8cc3-32b9-a746-c0dbd803efc2 | -8.994 | -46.0808 | 2025-09-10 12:50:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 63.5 |
| 267d0de6-5444-3e50-962f-2a8be05739b5 | -14.6652 | -44.0617 | 2025-09-10 12:50:00 | GOES-19 | MANGA | MINAS GERAIS | Brasil | 3139300 | 31 | 33 | nan | nan | nan | Caatinga | 94.1 |
| eb4dcd6b-080e-3317-b69c-4301209027ba | -11.3905 | -43.5365 | 2025-09-10 12:50:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 134.8 |
| 6c297c48-be6f-37a0-bd6f-2e0518275baa | -11.4512 | -50.3483 | 2025-09-10 12:50:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 115.9 |
| b52f3842-17cb-3aba-ab10-d33bdd34364f | -10.1654 | -46.195 | 2025-09-10 12:50:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 142.4 |


[Clique aqui para ver as próximas entradas](README108.md)
