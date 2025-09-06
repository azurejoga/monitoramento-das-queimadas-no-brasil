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

## Dados Diários - Página 60

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| c85eb57d-b213-3e13-aca8-6afcaf045ac4 | -8.18476 | -49.58673 | 2025-09-06 04:38:00 | NOAA-20 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| b48f43ab-2964-39e7-b288-d038440d33eb | -3.32665 | -54.91333 | 2025-09-06 04:38:00 | NOAA-20 | BELTERRA | PARÁ | Brasil | 1501451 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| e066d9fd-14f6-3582-8c92-eef9c609c2b0 | -5.73114 | -45.36956 | 2025-09-06 04:38:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 89695675-64d6-3dfa-a788-14d6d384f91e | -5.86127 | -57.77486 | 2025-09-06 04:38:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 8a28763c-3656-3b50-9d08-03fb76626a12 | -6.19271 | -53.25008 | 2025-09-06 04:38:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 342cbb77-efd2-3259-b948-1d399e3b8ee2 | -4.86279 | -50.82565 | 2025-09-06 04:38:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 6.6 |
| 90c4fafc-0fb6-325a-b368-5f6273c77898 | -6.21545 | -43.57962 | 2025-09-06 04:38:00 | NOAA-20 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 528aac02-6437-3743-a57a-8db993675fbe | -8.36345 | -48.27398 | 2025-09-06 04:38:00 | NOAA-20 | PRESIDENTE KENNEDY | TOCANTINS | Brasil | 1718402 | 17 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 01d1a8f6-1e85-3cf5-9576-1785d6a3ed60 | -6.17363 | -53.50613 | 2025-09-06 04:38:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 43ca6d26-b752-39b1-9da2-943eb473c364 | -7.59585 | -44.66753 | 2025-09-06 04:38:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| cabc27bf-0edb-369c-a2ab-45c2b1830d50 | -8.34467 | -46.95809 | 2025-09-06 04:38:00 | NOAA-20 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| c428c3d0-cadd-345c-ad2b-cd7d7f1a9869 | -5.8568 | -57.77056 | 2025-09-06 04:38:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| e747d644-f293-3140-98ce-219d01989392 | -5.90021 | -57.73051 | 2025-09-06 04:38:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| a60e4e12-e28d-309e-84ab-a8d0243480b8 | -8.45297 | -45.03309 | 2025-09-06 04:38:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 3a0821e4-0821-3398-a2b8-842ea0dd3bda | -5.26091 | -44.45284 | 2025-09-06 04:38:00 | NOAA-20 | PRESIDENTE DUTRA | MARANHÃO | Brasil | 2109106 | 21 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 031f4455-8d87-3d5a-88e7-72ae24c3b2d1 | -6.29448 | -44.7945 | 2025-09-06 04:38:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| c0ade095-240d-3f4d-8e85-490856b0eff1 | -5.94305 | -45.66298 | 2025-09-06 04:38:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 8febb513-16ea-3108-b06f-5382c602e73f | -5.86234 | -46.10256 | 2025-09-06 04:38:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 43aa8347-730c-3fb2-81f8-df41180bccb3 | -7.59265 | -44.68904 | 2025-09-06 04:38:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 7a274975-baa4-3973-9db6-9b183bffe34f | -3.24326 | -50.80114 | 2025-09-06 04:38:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 56588612-44cb-3239-b872-e6238c9b4702 | -6.39832 | -46.0934 | 2025-09-06 04:38:00 | NOAA-20 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 212869d4-bfaf-3e45-88e4-1c871881cda7 | -7.26843 | -48.26081 | 2025-09-06 04:38:00 | NOAA-20 | ARAGUAÍNA | TOCANTINS | Brasil | 1702109 | 17 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f76cbe60-219a-33ed-a4d5-653c083d9d79 | -6.27147 | -53.4297 | 2025-09-06 04:38:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| e71659f0-723d-3255-a90b-739430f89a1e | -7.71076 | -50.33018 | 2025-09-06 04:38:00 | NOAA-20 | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| f163b3ff-58a6-3ece-86d9-ed24254d36fe | -7.60746 | -44.67678 | 2025-09-06 04:38:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 91e45b28-ff36-3bab-a4c3-92c9b06aea81 | -7.73934 | -47.42584 | 2025-09-06 04:38:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| dea09a0e-3ba0-31f9-87c9-b68e0f0d4032 | -8.90657 | -45.10953 | 2025-09-06 04:38:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 7f2655ca-2ced-39db-bdae-f8b49122f0e1 | -8.3441 | -46.95258 | 2025-09-06 04:38:00 | NOAA-20 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 572ef6d6-5050-30ec-bd2e-2e21bca68dea | -5.96301 | -44.73454 | 2025-09-06 04:38:00 | NOAA-20 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 45b2f32b-963d-391f-b9cb-93172c9015b9 | -8.09712 | -55.72876 | 2025-09-06 04:38:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d0134709-aa4c-3f9e-affd-dff1299b22c4 | -8.05196 | -52.3714 | 2025-09-06 04:38:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| aa56d7e5-5a43-39b5-8580-352b2e213e96 | -8.3571 | -52.52034 | 2025-09-06 04:38:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 605c6dc9-a239-30c8-bdae-3038cbea8512 | -5.03627 | -49.75853 | 2025-09-06 04:38:00 | NOAA-20 | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 5ab160f0-cdc1-364f-85f9-464e881873a4 | -9.05401 | -50.44928 | 2025-09-06 04:38:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 748b92b5-480f-3fb2-82a9-894687259e16 | -2.55142 | -48.39152 | 2025-09-06 04:38:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 8eaad96a-692c-3f59-bb22-199d4e90f5d4 | -6.62724 | -53.15926 | 2025-09-06 04:38:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 7720c017-fcee-3ccb-80c8-439fcb9d3b92 | -8.44899 | -45.03238 | 2025-09-06 04:38:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 52e4f9b4-f2bd-35c9-9634-4cc095996b46 | -6.81288 | -52.80805 | 2025-09-06 04:38:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 8.0 |
| 887480b6-9741-33db-b1bd-e1204fe81b00 | -6.92659 | -44.96198 | 2025-09-06 04:38:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| b479cbcb-067e-38f9-98a3-08b1b3a7ad6b | -4.9942 | -56.25406 | 2025-09-06 04:38:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 9af00229-06dc-3d77-8afc-e166c35d7bbc | -8.52684 | -51.307 | 2025-09-06 04:38:00 | NOAA-20 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 70cdda17-fd1f-373d-887b-c961b3234ecb | -5.94984 | -46.16575 | 2025-09-06 04:38:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 8c533009-7263-333e-8209-f8ec61aed0ca | -3.96333 | -43.24334 | 2025-09-06 04:38:00 | NOAA-20 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 7ff1a78c-fcc8-3376-825e-d63d80d1b3a1 | -6.86322 | -44.82195 | 2025-09-06 04:38:00 | NOAA-20 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| e03172ab-57cf-3a1f-997b-450e1f45deb1 | -6.01225 | -46.70124 | 2025-09-06 04:38:00 | NOAA-20 | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 31ec0757-3753-30e2-8db0-5d94b71a9ff3 | -6.00932 | -46.69671 | 2025-09-06 04:38:00 | NOAA-20 | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 4d778da2-dddf-319f-b369-fbc77d3ee1ca | -4.99972 | -56.25744 | 2025-09-06 04:38:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 88734a5a-35e4-3d47-a6b6-1a0934a1415b | -8.91166 | -45.8146 | 2025-09-06 04:38:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| e730a32f-478c-3741-9b5c-998b30ff48e3 | -6.94065 | -50.96424 | 2025-09-06 04:38:00 | NOAA-20 | OURILÂNDIA DO NORTE | PARÁ | Brasil | 1505437 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| dec0ac3a-4c2c-362a-983d-06add5653cc8 | -6.87628 | -52.784 | 2025-09-06 04:38:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ad183e60-acfe-32d8-86af-b2aab2c78fe7 | -6.59456 | -44.55419 | 2025-09-06 04:38:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 8.6 |
| 5b1dca7b-550d-37b2-bdcc-4a45a2280405 | -7.28086 | -43.70175 | 2025-09-06 04:38:00 | NOAA-20 | CANAVIEIRA | PIAUÍ | Brasil | 2202251 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 27d93219-17bb-3d6d-b14d-64cd22bbdfd4 | -6.27826 | -53.43553 | 2025-09-06 04:38:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 33c3420b-f29c-3757-997a-e16a7ee5f9fd | -3.37674 | -50.84521 | 2025-09-06 04:38:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 7511e4d3-a935-3daf-bbe2-a875bd0e00e1 | -7.72834 | -50.32618 | 2025-09-06 04:38:00 | NOAA-20 | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| ae17c0ae-6818-303a-a10c-79a4a1fe95ae | -5.72807 | -45.3644 | 2025-09-06 04:38:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| e2c5857a-a058-3e8c-85f3-efe7558526a5 | -3.30571 | -48.7148 | 2025-09-06 04:38:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 6390fa61-60cd-3695-9105-9230de5b1729 | -7.0792 | -43.86926 | 2025-09-06 04:38:00 | NOAA-20 | MARCOS PARENTE | PIAUÍ | Brasil | 2206001 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 2613d506-8232-35dc-85e1-4e12ccf775e7 | -8.44103 | -45.03096 | 2025-09-06 04:38:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 1215a199-d8c6-3586-a2fe-a9e6011d9ade | -6.55392 | -42.94801 | 2025-09-06 04:38:00 | NOAA-20 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 9bcb0789-4320-37c8-8b4c-8674bbba6abb | -5.91296 | -43.22487 | 2025-09-06 04:38:00 | NOAA-20 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 004e5e8f-2f29-36b9-ae9e-eb080d090eb4 | -6.16405 | -53.68383 | 2025-09-06 04:38:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 2ac52d82-a6e0-32f3-889c-af3bd1feffc0 | -4.32796 | -48.39079 | 2025-09-06 04:38:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 9ec229d4-f166-3c97-bc2a-cbca8f2b1d1c | -5.61328 | -47.43935 | 2025-09-06 04:38:00 | NOAA-20 | IMPERATRIZ | MARANHÃO | Brasil | 2105302 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 543a745d-138d-3f05-9fca-92f14228d79a | -4.89275 | -55.99499 | 2025-09-06 04:38:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 6f69383a-1025-361a-ba13-ac374923175f | -2.51115 | -51.91575 | 2025-09-06 04:38:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ca5b07ec-a6ad-3f68-948f-b389c2614dd9 | -9.06119 | -50.44685 | 2025-09-06 04:38:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 689144cd-b163-3f1d-bd25-941e3a7186dc | -7.25664 | -41.89458 | 2025-09-06 04:38:00 | NOAA-20 | WALL FERRAZ | PIAUÍ | Brasil | 2211704 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 4831aa5e-3201-32ee-8065-e612c45bd5f1 | -7.70966 | -50.33717 | 2025-09-06 04:38:00 | NOAA-20 | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 441f6815-e62a-36cf-bc8d-f5c61ea057bd | -6.2677 | -53.42906 | 2025-09-06 04:38:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 23b99947-ab37-3633-9c94-2ceb66bd3b38 | -6.84132 | -52.83894 | 2025-09-06 04:38:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 42d9daf1-25b9-39be-ae7e-05ab22a09f3b | -6.8158 | -52.81289 | 2025-09-06 04:38:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 8.0 |
| 2d9a6c4b-ae08-3b77-bbe9-34b0f05aaecf | -8.07843 | -50.19628 | 2025-09-06 04:38:00 | NOAA-20 | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| d6556321-1465-3066-b49c-81ee19c7491b | -6.2366 | -43.28565 | 2025-09-06 04:38:00 | NOAA-20 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 1791d46a-82bc-3227-9931-a2cc580aa017 | -3.31672 | -48.70947 | 2025-09-06 04:38:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 73492770-4713-3a05-ab3e-a6e4d7bfe870 | -7.34412 | -43.94724 | 2025-09-06 04:38:00 | NOAA-20 | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 4.2 |
| e0c63888-b103-30c3-8b60-5eb45348dbf2 | -6.15481 | -43.19797 | 2025-09-06 04:38:00 | NOAA-20 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 98e9ebc8-a996-3983-8d13-a4176b1dda0a | -8.86899 | -47.9153 | 2025-09-06 04:38:00 | NOAA-20 | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 6507e2f1-d30f-3624-94d4-06a40c10e4c1 | -3.23685 | -50.05037 | 2025-09-06 04:38:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| bd08fc2b-da87-3af3-922b-5181450b4b4d | -5.67578 | -45.17389 | 2025-09-06 04:38:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 5721f6ce-5824-3b9c-8817-cefd447491aa | -6.01697 | -46.69387 | 2025-09-06 04:38:00 | NOAA-20 | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| e349ccb9-8b98-33db-a897-7894cebea2da | -5.68025 | -43.5769 | 2025-09-06 04:38:00 | NOAA-20 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 9f9a8e97-ccf3-3209-9ddf-77399cd5d9b7 | -8.0513 | -52.37538 | 2025-09-06 04:38:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 00027ac0-7284-3882-90da-ad0812e39b73 | -4.26886 | -48.18187 | 2025-09-06 04:38:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 5e06f7e5-d099-326b-ae78-e253f020f215 | -5.03295 | -49.758 | 2025-09-06 04:38:00 | NOAA-20 | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 2412b136-c1e5-382f-9ba8-4c8ac6231329 | -5.18158 | -43.03464 | 2025-09-06 04:38:00 | NOAA-20 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| ddafef55-10cc-30b7-9ee1-b45aeaf70a58 | -5.72992 | -43.91171 | 2025-09-06 04:38:00 | NOAA-20 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 5ad43c69-f693-39a9-ad68-da397f877d83 | -8.6558 | -54.84912 | 2025-09-06 04:38:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 314e7128-ce13-32a0-8c7b-f0e655b3a53f | -8.35541 | -52.55234 | 2025-09-06 04:38:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 9c0bb39c-d821-3dda-b537-0530d0ba3ef0 | -7.73165 | -50.32674 | 2025-09-06 04:38:00 | NOAA-20 | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 0d711bea-a5d4-3500-9760-84974d2d91e8 | -8.90891 | -45.77993 | 2025-09-06 04:38:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 897e8200-1f66-3f98-b5e8-c19667e52c6f | -7.3024 | -43.73392 | 2025-09-06 04:38:00 | NOAA-20 | CANAVIEIRA | PIAUÍ | Brasil | 2202251 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 0641e1b3-f593-3b71-88f2-c7052051dab3 | -8.34351 | -46.95663 | 2025-09-06 04:38:00 | NOAA-20 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 96d976d5-0052-35df-919d-66e800b31df4 | -9.01365 | -49.80059 | 2025-09-06 04:38:00 | NOAA-20 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 265a1f4b-66ab-39e9-bda1-adeb8d3f15b8 | -8.63931 | -45.75228 | 2025-09-06 04:38:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 434d5433-99f6-32f8-9361-c21b2adeb522 | -5.95002 | -53.78672 | 2025-09-06 04:38:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 2e29003c-e9df-3efd-8ddc-1a98745bde53 | -7.41724 | -44.949 | 2025-09-06 04:38:00 | NOAA-20 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| f2a8aa99-3202-347f-a618-c5bf4e6d8415 | -6.0205 | -46.69444 | 2025-09-06 04:38:00 | NOAA-20 | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| cd982648-41d5-3d61-831a-16515e9d1331 | -5.65703 | -43.6171 | 2025-09-06 04:38:00 | NOAA-20 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 7c38d0e2-c5d1-330e-bbb9-26b46b227161 | -5.90277 | -57.74583 | 2025-09-06 04:38:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 0.2 |


[Clique aqui para ver as próximas entradas](README61.md)
