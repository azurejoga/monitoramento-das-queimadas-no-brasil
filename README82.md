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

## Dados Diários - Página 82

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| ea26d354-1f5d-3248-a651-46afcd35c3ef | -6.04389 | -51.14918 | 2024-10-26 04:44:00 | NOAA-20 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 4a433ebe-203d-389f-8818-d5cdff0c73a0 | -5.94597 | -50.86587 | 2024-10-26 04:44:00 | NOAA-20 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 2b19a538-c3a8-384d-bb82-7bee4fc2f276 | -5.94213 | -50.8688 | 2024-10-26 04:44:00 | NOAA-20 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 2bb61910-dd50-3dec-8b5b-985952581427 | -5.94159 | -50.87225 | 2024-10-26 04:44:00 | NOAA-20 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b8ad13ca-53bc-3bf1-98d2-725eaa38370b | -5.94104 | -50.87569 | 2024-10-26 04:44:00 | NOAA-20 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 793b429e-ffb9-3fed-8d9f-1307c3c2c238 | -5.84928 | -50.35499 | 2024-10-26 04:44:00 | NOAA-20 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b698db8e-84a4-3f5f-9514-34734f756165 | -5.83063 | -51.14403 | 2024-10-26 04:44:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 84c90b56-227e-3a0a-b325-15db9340d735 | -5.5755 | -51.08237 | 2024-10-26 04:44:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 0cfcae43-2f27-34dd-8b62-41b2b6e4eda4 | -7.57746 | -50.70742 | 2024-10-26 04:44:00 | NOAA-20 | BANNACH | PARÁ | Brasil | 1501253 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| b0753be0-c3ce-3d47-8c7b-fccf22f157a0 | -7.11533 | -50.5568 | 2024-10-26 04:44:00 | NOAA-20 | OURILÂNDIA DO NORTE | PARÁ | Brasil | 1505437 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| fc318bca-ddea-3a8e-bf81-8aace41ecea9 | -6.89825 | -50.31506 | 2024-10-26 04:44:00 | NOAA-20 | ÁGUA AZUL DO NORTE | PARÁ | Brasil | 1500347 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 21932858-44ba-36db-97f9-6fd3e96398e3 | -6.89493 | -50.31454 | 2024-10-26 04:44:00 | NOAA-20 | ÁGUA AZUL DO NORTE | PARÁ | Brasil | 1500347 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 94af89cd-fe95-3454-81a7-e14724b07e2e | -6.84252 | -50.75925 | 2024-10-26 04:44:00 | NOAA-20 | ÁGUA AZUL DO NORTE | PARÁ | Brasil | 1500347 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| a3a2ecd8-e3ea-32f0-b6d1-70b2a4f1073b | -6.79823 | -50.8692 | 2024-10-26 04:44:00 | NOAA-20 | OURILÂNDIA DO NORTE | PARÁ | Brasil | 1505437 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| db42c8e8-5a54-36e8-9c4e-cf50d67e98d3 | -6.79769 | -50.87265 | 2024-10-26 04:44:00 | NOAA-20 | OURILÂNDIA DO NORTE | PARÁ | Brasil | 1505437 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| aecc4974-6160-329c-8132-2a94197a0238 | -6.68184 | -49.97844 | 2024-10-26 04:44:00 | NOAA-20 | ÁGUA AZUL DO NORTE | PARÁ | Brasil | 1500347 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 100720e3-f4a3-3a2b-b23b-61b67a96ed57 | -6.68129 | -49.98196 | 2024-10-26 04:44:00 | NOAA-20 | ÁGUA AZUL DO NORTE | PARÁ | Brasil | 1500347 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| a55ca690-cc14-3ef0-b1a5-1d8e494a173e | -6.89438 | -50.31804 | 2024-10-26 04:44:00 | NOAA-20 | ÁGUA AZUL DO NORTE | PARÁ | Brasil | 1500347 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 440249eb-ebeb-3d1c-888a-7a78cb95bd70 | -6.85244 | -50.76081 | 2024-10-26 04:44:00 | NOAA-20 | ÁGUA AZUL DO NORTE | PARÁ | Brasil | 1500347 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 25af5fce-26d5-3dab-b7e3-09ed1dea5ee4 | -6.80489 | -50.8915 | 2024-10-26 04:44:00 | NOAA-20 | OURILÂNDIA DO NORTE | PARÁ | Brasil | 1505437 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 98d33fef-34f9-3faa-9a96-57ccb40f5f35 | -6.77601 | -50.48881 | 2024-10-26 04:44:00 | NOAA-20 | ÁGUA AZUL DO NORTE | PARÁ | Brasil | 1500347 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 2e8247ea-85a3-3833-944d-ef72d5eea77b | -9.25795 | -50.68882 | 2024-10-26 04:44:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 9263b1a6-ec60-33b2-a132-e0f5c209adfd | -9.25406 | -50.69184 | 2024-10-26 04:44:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 2474dda9-f26f-3d4b-af16-aca9ab5d2d37 | -8.22301 | -50.66092 | 2024-10-26 04:44:00 | NOAA-20 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f69063bf-0d83-3a4d-bb6d-810256db6ce1 | -9.25461 | -50.6883 | 2024-10-26 04:44:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 9f4565a7-8699-3304-b067-25dc9a7edd61 | -9.15215 | -50.55936 | 2024-10-26 04:44:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 524ff994-edb2-3781-8be7-ac6f2ed2ecbd | -9.1056 | -50.63946 | 2024-10-26 04:44:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 2885005d-d8c5-3e33-b777-dfaf6ba4a839 | -9.10227 | -50.63894 | 2024-10-26 04:44:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 13b493d7-d347-3368-90e3-1b10e379f22a | -9.10172 | -50.64249 | 2024-10-26 04:44:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 58bf9291-d772-3888-97c1-dc23cc596e5b | -8.39617 | -50.42056 | 2024-10-26 04:44:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c1ea197f-a95e-3887-8b60-b59a383b4085 | -8.37121 | -50.44936 | 2024-10-26 04:44:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 5a331f4f-a574-3abb-901a-9cb597dd3b99 | -8.36788 | -50.44884 | 2024-10-26 04:44:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 791b759c-5f15-372f-8d53-224adb667423 | -9.4781 | -50.82053 | 2024-10-26 04:44:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 0.3 |
| e787cb02-34b6-302f-b67f-73a581e69ef5 | -9.47589 | -50.8167 | 2024-10-26 04:44:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 6bedb5df-3889-31df-9b3d-278af4c492f1 | -9.47534 | -50.82023 | 2024-10-26 04:44:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d1de084d-ba01-3c96-984d-4511e64d1b13 | -3.60824 | -51.46988 | 2024-10-26 04:44:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 2b56b65d-b86c-3bc0-9eda-67576ce8585d | -3.60769 | -51.47339 | 2024-10-26 04:44:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 406cfb17-0b25-3453-9e45-5e592d24e6ed | -3.6049 | -51.46936 | 2024-10-26 04:44:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 8e68f0db-243c-35e5-b400-b8061011b3cb | -3.60435 | -51.47288 | 2024-10-26 04:44:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 08d5b335-6e25-376a-a378-eaedf4795582 | -3.58748 | -51.21228 | 2024-10-26 04:44:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 47f1ad37-ed08-3cb7-8e27-6f0e389fc6d7 | -3.58416 | -51.21177 | 2024-10-26 04:44:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 93e1ff4e-d763-3ceb-97e9-3bfb8f8e07ca | -3.58361 | -51.21524 | 2024-10-26 04:44:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| b5933ab0-7027-3e58-b9fe-0d86694e8e91 | -3.58306 | -51.21873 | 2024-10-26 04:44:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| cee35fc5-7db1-3a9d-8b5c-6e9e4459eb74 | -3.58139 | -51.20776 | 2024-10-26 04:44:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 70123a59-845d-3fe5-a096-1b3d40c6ebbc | -3.58084 | -51.21125 | 2024-10-26 04:44:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| ebc91cc9-c9f1-3c3c-957e-f641707f7454 | -3.58029 | -51.21473 | 2024-10-26 04:44:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 36d3126d-7bdf-3873-9753-e16eced0155a | -3.57974 | -51.21821 | 2024-10-26 04:44:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 26e109a0-d68d-35ef-8568-3262bc188c42 | -3.55985 | -51.49475 | 2024-10-26 04:44:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 77477141-b0e6-32cc-a91f-e22062d552d5 | -3.55875 | -51.43692 | 2024-10-26 04:44:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 0f5acb6b-d73e-36cf-b2bb-3047ef5a42df | -3.75399 | -52.19644 | 2024-10-26 04:44:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| ce58f959-5b86-3dba-af0f-e868a914cfe2 | -3.73272 | -51.08949 | 2024-10-26 04:44:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 7f03d464-4a5e-32ef-88a4-fc1a6acf02a0 | -3.70981 | -51.34247 | 2024-10-26 04:44:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 66006c59-9d45-3a61-8654-3dcbea7095f7 | -3.70964 | -52.11905 | 2024-10-26 04:44:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 202527d8-8375-322a-9110-4c77398f98e4 | -3.70907 | -52.12268 | 2024-10-26 04:44:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 1f60bbb8-817f-3451-87f0-e04df5e6a144 | -3.70625 | -52.11851 | 2024-10-26 04:44:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 2dcd8f95-1fcc-38fe-a9e6-b6b10159a08e | -3.69445 | -51.63533 | 2024-10-26 04:44:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 636ca286-682a-322f-bad9-cc4eeb31fc84 | -3.6911 | -51.63483 | 2024-10-26 04:44:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| d821ab00-8637-3738-bbe7-9c762781e14f | -3.68683 | -52.00032 | 2024-10-26 04:44:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| c22d51fb-65dd-3c4a-8d19-921107505096 | -3.68504 | -51.83804 | 2024-10-26 04:44:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 0a4adfb2-2ac4-3e5a-aa79-99fe63de99b6 | -3.68345 | -51.99979 | 2024-10-26 04:44:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| c00da24f-fde6-3bb9-9524-f99d575dc310 | -3.67053 | -52.14647 | 2024-10-26 04:44:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 3931f1da-3eb2-31eb-ab00-7036b4b2d33b | -3.65214 | -51.93579 | 2024-10-26 04:44:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| db2dbdcb-3d80-3986-bb96-a075659102ff | -3.57468 | -52.13169 | 2024-10-26 04:44:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 28a97601-57f0-390e-a00d-a9e316ccae2c | -4.66537 | -50.97069 | 2024-10-26 04:44:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 8ad7912e-4675-32ee-8ecc-585aa2535ad2 | -4.62079 | -50.97429 | 2024-10-26 04:44:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 66727e41-fba5-30f7-b3f5-1b055d04792b | -4.53945 | -50.97176 | 2024-10-26 04:44:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 96a0f6f1-9808-36a0-807b-76ae8ddf1501 | -3.88817 | -50.98626 | 2024-10-26 04:44:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| c718b607-241c-345c-8e06-5a6e0183d60e | -4.13554 | -51.09956 | 2024-10-26 04:44:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f082d886-aa9b-3a0f-a758-545e301229de | -4.1234 | -51.09054 | 2024-10-26 04:44:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 3e87c0ee-c7be-3091-8315-885f51a6a150 | -3.96969 | -51.05191 | 2024-10-26 04:44:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 1050909a-2137-3147-a230-2f58a2583bfd | -3.94851 | -52.25293 | 2024-10-26 04:44:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 884d6cee-671b-3b05-b5b8-817fbf4eabb1 | -3.94792 | -52.2566 | 2024-10-26 04:44:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 5290bb9a-dbc0-3c1a-af12-75d56d2045cb | -3.94452 | -52.25606 | 2024-10-26 04:44:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| f1219a43-26ed-3327-b4e5-d37eb88baea3 | -3.94393 | -52.25974 | 2024-10-26 04:44:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 77872d26-1a85-32c4-a081-307f3b70ca0e | -3.91142 | -52.26215 | 2024-10-26 04:44:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 39758ac2-d8bf-33d3-b61c-6fe4a085e35f | -3.85013 | -51.3144 | 2024-10-26 04:44:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 2f473ac5-003c-3f8b-89f6-cb45f897cb46 | -3.78313 | -51.37179 | 2024-10-26 04:44:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| b676fbb6-a38b-3410-beb0-719343d99ce2 | -3.78258 | -51.37528 | 2024-10-26 04:44:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 61ad5681-247d-3f10-90a1-b6539db3f8a3 | -4.66591 | -50.96724 | 2024-10-26 04:44:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 0a9a34eb-a0e5-346c-a852-82cc3617d738 | -4.63613 | -50.94138 | 2024-10-26 04:44:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 43bb4b52-df68-3db2-8897-e1e12212351e | -4.63608 | -50.92022 | 2024-10-26 04:44:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 0609eb8f-0812-3a3b-9352-1ccaa27c70ba | -4.63282 | -50.94087 | 2024-10-26 04:44:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 0429ad44-870d-39d8-bb38-7eee0b283171 | -4.53614 | -50.97124 | 2024-10-26 04:44:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 0b54eb36-2876-3434-bb08-8b7047f3062e | -6.14507 | -52.64528 | 2024-10-26 04:44:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f06c0785-968b-36a9-abad-a81057ce7ecf | -6.07112 | -51.36613 | 2024-10-26 04:44:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 68cfdb21-774f-33d6-a2df-254eb18773ae | -6.02605 | -51.30554 | 2024-10-26 04:44:00 | NOAA-20 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 72f49076-0756-386d-b1f7-26b5e3cd8104 | -9.32877 | -52.85044 | 2024-10-26 04:44:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d3f34644-8da1-33f1-8110-7c17a82cedef | -9.97315 | -52.23906 | 2024-10-26 04:44:00 | NOAA-20 | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| d7dd38dd-65ae-3ff5-9d2e-cef99023e15e | -9.96984 | -52.23853 | 2024-10-26 04:44:00 | NOAA-20 | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 54226015-83cd-3443-b51b-da6aef3ac935 | -3.2324 | -53.27881 | 2024-10-26 04:44:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 36ec310e-bfab-3c52-9fd5-ecd58ac670a8 | -3.21851 | -53.36458 | 2024-10-26 04:44:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 0b651bdf-89b9-3d12-a527-ee8ae0099fd0 | -3.21785 | -53.36867 | 2024-10-26 04:44:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| d83fad0d-060b-3e36-bbe5-23739361ebdc | -3.21494 | -53.36397 | 2024-10-26 04:44:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 418eeb5f-21c5-3b76-8b38-828ace30732a | -3.21428 | -53.36806 | 2024-10-26 04:44:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f7e552fe-e410-30c5-92c2-33546984cee4 | -3.21136 | -53.36337 | 2024-10-26 04:44:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 65c065c7-925c-3610-8606-feff0dd7ea9a | -3.5079 | -53.14399 | 2024-10-26 04:44:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 9.0 |
| effbef80-99d6-37d7-8188-53f499a74118 | -3.44139 | -52.63629 | 2024-10-26 04:44:00 | NOAA-20 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 01587716-6142-3a32-a77b-d16f6afb666a | -3.42154 | -52.71529 | 2024-10-26 04:44:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| b381405d-6642-329f-93f8-55576719db4c | -3.38224 | -52.41501 | 2024-10-26 04:44:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 1dffe924-f116-3d79-b6a1-92bcbd17f9bc | -3.28706 | -53.68162 | 2024-10-26 04:44:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |


[Clique aqui para ver as próximas entradas](README83.md)
