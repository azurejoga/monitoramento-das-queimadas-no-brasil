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

## Dados Diários - Página 6

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 7b5342e3-c7a0-309b-aa46-6b1dc9d4cea0 | -15.32417 | -43.89239 | 2025-11-02 03:32:00 | NOAA-20 | JAÍBA | MINAS GERAIS | Brasil | 3135050 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 66d0a09d-f107-343d-af1b-be520cc9afcc | -15.29392 | -42.96062 | 2025-11-02 03:32:00 | NOAA-20 | MONTE AZUL | MINAS GERAIS | Brasil | 3142908 | 31 | 33 | nan | nan | nan | Caatinga | 2.6 |
| c8e728e4-9a5a-3f16-8879-bca129e9eacb | -14.66024 | -46.61527 | 2025-11-02 03:32:00 | NOAA-20 | ALVORADA DO NORTE | GOIÁS | Brasil | 5200803 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| f02950d0-82dd-3623-a135-78caf5698c24 | -13.31127 | -43.462 | 2025-11-02 03:32:00 | NOAA-20 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 28e25587-7743-3888-8b98-66b0df6ed67b | -14.02566 | -43.4841 | 2025-11-02 03:32:00 | NOAA-20 | MALHADA | BAHIA | Brasil | 2920205 | 29 | 33 | nan | nan | nan | Cerrado | 22.8 |
| 73916eab-15bd-3475-8c7a-df587b1cde46 | -16.84923 | -40.70129 | 2025-11-02 03:32:00 | NOAA-20 | SANTA HELENA DE MINAS | MINAS GERAIS | Brasil | 3157658 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.7 |
| 3b38b43e-48d8-3449-aa2a-a512e7c48bad | -14.02024 | -43.48293 | 2025-11-02 03:32:00 | NOAA-20 | MALHADA | BAHIA | Brasil | 2920205 | 29 | 33 | nan | nan | nan | Cerrado | 50.8 |
| e5e4add9-0556-3fd3-acf4-eef0ffd2b8f3 | -15.29742 | -42.95995 | 2025-11-02 03:32:00 | NOAA-20 | MONTE AZUL | MINAS GERAIS | Brasil | 3142908 | 31 | 33 | nan | nan | nan | Caatinga | 1.9 |
| d076359a-0502-3c3c-8f2e-85055579f989 | -13.44884 | -42.94931 | 2025-11-02 03:32:00 | NOAA-20 | RIACHO DE SANTANA | BAHIA | Brasil | 2926400 | 29 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 6fc04bc8-9cb1-3868-8443-bef6e41d347a | -15.81422 | -41.99987 | 2025-11-02 03:32:00 | NOAA-20 | TAIOBEIRAS | MINAS GERAIS | Brasil | 3168002 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| 98e18c1a-5e25-3ef5-8351-aa8822b50f53 | -14.0351 | -43.4906 | 2025-11-02 03:40:00 | GOES-19 | MALHADA | BAHIA | Brasil | 2920205 | 29 | 33 | nan | nan | nan | Cerrado | 82.0 |
| d794e318-40e5-3a1b-96e4-acc658f8560c | -14.0356 | -43.4666 | 2025-11-02 03:40:00 | GOES-19 | PALMAS DE MONTE ALTO | BAHIA | Brasil | 2923407 | 29 | 33 | nan | nan | nan | Cerrado | 89.3 |
| cf9ee989-a111-3a24-bcbd-e2a6d6d88653 | -15.6264 | -58.2166 | 2025-11-02 03:40:00 | GOES-19 | SÃO JOSÉ DOS QUATRO MARCOS | MATO GROSSO | Brasil | 5107107 | 51 | 33 | nan | nan | nan | Amazônia | 37.1 |
| cfa6b1ef-d356-3ebb-9183-2f5153a86dff | -14.0161 | -43.4703 | 2025-11-02 03:40:00 | GOES-19 | PALMAS DE MONTE ALTO | BAHIA | Brasil | 2923407 | 29 | 33 | nan | nan | nan | Cerrado | 121.0 |
| 1ccca087-58f8-349b-a6f9-8d085f27b1b4 | -14.0155 | -43.4943 | 2025-11-02 03:40:00 | GOES-19 | MALHADA | BAHIA | Brasil | 2920205 | 29 | 33 | nan | nan | nan | Cerrado | 108.8 |
| 4058aad9-7cb3-377e-a224-e1597397d5c7 | -14.0161 | -43.4703 | 2025-11-02 03:50:00 | GOES-19 | PALMAS DE MONTE ALTO | BAHIA | Brasil | 2923407 | 29 | 33 | nan | nan | nan | Cerrado | 89.3 |
| 075f3f0c-47cf-3396-b93d-9afd18ba5097 | -15.6261 | -58.2368 | 2025-11-02 03:50:00 | GOES-19 | SÃO JOSÉ DOS QUATRO MARCOS | MATO GROSSO | Brasil | 5107107 | 51 | 33 | nan | nan | nan | Amazônia | 40.9 |
| 6e511592-d038-3d3b-a06c-6d30f7ed31e5 | -14.0351 | -43.4906 | 2025-11-02 03:50:00 | GOES-19 | MALHADA | BAHIA | Brasil | 2920205 | 29 | 33 | nan | nan | nan | Cerrado | 88.3 |
| fb9505d7-c5fe-34cc-a34f-3b1bdb8aa9b9 | -3.9062 | -45.7565 | 2025-11-02 03:50:00 | GOES-19 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 70.7 |
| e92c5335-d5b4-35bd-a66e-634eace31476 | -14.0356 | -43.4666 | 2025-11-02 03:50:00 | GOES-19 | PALMAS DE MONTE ALTO | BAHIA | Brasil | 2923407 | 29 | 33 | nan | nan | nan | Cerrado | 84.7 |
| 1ed434fc-a970-3281-a2a4-dc400628869f | -13.3177 | -43.4552 | 2025-11-02 03:50:00 | GOES-19 | BOM JESUS DA LAPA | BAHIA | Brasil | 2903904 | 29 | 33 | nan | nan | nan | Cerrado | 57.3 |
| 8193baff-c99f-34c4-a0d5-92e1a61b4aff | -14.0155 | -43.4943 | 2025-11-02 03:50:00 | GOES-19 | MALHADA | BAHIA | Brasil | 2920205 | 29 | 33 | nan | nan | nan | Cerrado | 94.8 |
| f6933ddc-0742-3d2c-be92-ef4fb5429c85 | -4.1361 | -51.152 | 2025-11-02 03:50:00 | GOES-19 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 63.9 |
| d5a42194-e1aa-3c78-8ed2-f3a903b704a7 | -14.0351 | -43.4906 | 2025-11-02 04:00:00 | GOES-19 | MALHADA | BAHIA | Brasil | 2920205 | 29 | 33 | nan | nan | nan | Cerrado | 84.8 |
| 3e2d1d64-0a94-33cf-a228-9d4d7d461fc3 | -14.0161 | -43.4703 | 2025-11-02 04:00:00 | GOES-19 | PALMAS DE MONTE ALTO | BAHIA | Brasil | 2923407 | 29 | 33 | nan | nan | nan | Cerrado | 71.7 |
| 6ef64d09-6022-3d7a-975d-26c5720e0a07 | -14.0356 | -43.4666 | 2025-11-02 04:00:00 | GOES-19 | PALMAS DE MONTE ALTO | BAHIA | Brasil | 2923407 | 29 | 33 | nan | nan | nan | Cerrado | 83.1 |
| e51d5d8f-6c2f-3b3f-871e-fd84755d9c5d | -14.0155 | -43.4943 | 2025-11-02 04:00:00 | GOES-19 | MALHADA | BAHIA | Brasil | 2920205 | 29 | 33 | nan | nan | nan | Cerrado | 74.4 |
| ddd8e5a5-e6be-319c-aad2-f6b3bc53c663 | -13.3177 | -43.4552 | 2025-11-02 04:00:00 | GOES-19 | BOM JESUS DA LAPA | BAHIA | Brasil | 2903904 | 29 | 33 | nan | nan | nan | Cerrado | 57.5 |
| 86697ab3-f140-3c76-9083-a4a1abdda79e | -14.0351 | -43.4906 | 2025-11-02 04:10:00 | GOES-19 | MALHADA | BAHIA | Brasil | 2920205 | 29 | 33 | nan | nan | nan | Cerrado | 66.4 |
| 28bc9f42-fdf1-3b7c-8f15-c5480f5e1480 | -13.3177 | -43.4552 | 2025-11-02 04:10:00 | GOES-19 | BOM JESUS DA LAPA | BAHIA | Brasil | 2903904 | 29 | 33 | nan | nan | nan | Cerrado | 73.5 |
| 5b05083b-eacb-356a-925b-45b22db9aebf | -14.0161 | -43.4703 | 2025-11-02 04:10:00 | GOES-19 | PALMAS DE MONTE ALTO | BAHIA | Brasil | 2923407 | 29 | 33 | nan | nan | nan | Cerrado | 63.0 |
| fbcb3d9f-c8d1-3655-ae8b-df9ed7bb3f2a | -14.0356 | -43.4666 | 2025-11-02 04:10:00 | GOES-19 | PALMAS DE MONTE ALTO | BAHIA | Brasil | 2923407 | 29 | 33 | nan | nan | nan | Cerrado | 72.4 |
| ebe2a93d-eb0c-35aa-89a0-b321cfaba4ee | 1.01928 | -51.19712 | 2025-11-02 04:18:00 | NOAA-21 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 0.8 |
| ab4deab9-ebb5-3226-96a8-33db4c79d21a | -4.7234 | -45.69258 | 2025-11-02 04:18:00 | NOAA-21 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 083e4c8b-536e-3634-ab87-c38baca0c6d7 | -2.37745 | -47.71576 | 2025-11-02 04:18:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| e87e33bc-aa56-3866-bdf3-11d144ea77e4 | -3.63334 | -49.88842 | 2025-11-02 04:18:00 | NOAA-21 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| bf4d21b1-1318-3be2-ae69-51570968c703 | -5.17538 | -44.25357 | 2025-11-02 04:18:00 | NOAA-21 | GONÇALVES DIAS | MARANHÃO | Brasil | 2104404 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 308e7507-f2d0-321f-8a99-84e0358e1a84 | -4.62951 | -45.83755 | 2025-11-02 04:18:00 | NOAA-21 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 79fffcbc-a219-3db1-b5f9-8974c8479ac2 | -3.38399 | -52.37078 | 2025-11-02 04:18:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f03748f4-5f73-3b2e-896e-97a85f9e77b8 | -3.41135 | -46.90258 | 2025-11-02 04:18:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f502c67d-e330-36dc-a60e-3a938104718a | -3.14462 | -49.42463 | 2025-11-02 04:18:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| ed188332-6c9a-33ac-b137-88d8ffecc001 | -5.12508 | -43.37547 | 2025-11-02 04:18:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 478b34e4-1d25-3777-8927-92b36dc48a36 | -4.23038 | -45.80546 | 2025-11-02 04:18:00 | NOAA-21 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 393aa893-cc87-3695-b4d1-5fadd724e133 | -4.31691 | -45.6397 | 2025-11-02 04:18:00 | NOAA-21 | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 42c704b6-a1f4-313e-af36-40a01e879128 | -2.83954 | -49.40481 | 2025-11-02 04:18:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 3d55d806-38e4-35cf-972d-7f70b210e633 | -4.54348 | -46.02731 | 2025-11-02 04:18:00 | NOAA-21 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| f6cc87d7-8147-38a6-997d-502ea86d02b2 | -3.01652 | -49.43933 | 2025-11-02 04:18:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 9.1 |
| b89b6040-cf0e-34d5-8fd5-9413126d2004 | -3.33711 | -49.92707 | 2025-11-02 04:18:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 1d608432-2237-36b4-8e21-2b5c43f9b304 | -3.23977 | -50.79766 | 2025-11-02 04:18:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 662e8fe7-e0ad-3eb1-a940-c7be1051ee27 | -4.37417 | -45.87683 | 2025-11-02 04:18:00 | NOAA-21 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 860f125e-d5c9-3bdf-8808-4a668a1e74f3 | -3.55811 | -50.15696 | 2025-11-02 04:18:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| d3d80940-9be5-3a92-be3f-edc477bedfbd | -3.02072 | -49.43998 | 2025-11-02 04:18:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 9.1 |
| 95a8c4ce-3b65-39a8-b8d1-191ef04c0a09 | -3.4571 | -50.22062 | 2025-11-02 04:18:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 6.8 |
| 0f5e210a-220c-3a4b-a3bf-467cf196dadf | -2.6537 | -48.5102 | 2025-11-02 04:18:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 40559003-8731-30dc-9ffc-09f7b4e1b3f2 | -3.02595 | -51.22892 | 2025-11-02 04:18:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 02889f8f-590b-336b-b534-48b2a333c449 | -4.14509 | -46.2805 | 2025-11-02 04:18:00 | NOAA-21 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d2803b1a-413c-36bc-95f6-582dac207119 | -2.83892 | -49.40866 | 2025-11-02 04:18:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 7d730eb4-5c81-3563-b132-dc54c2e747a3 | -2.3111 | -48.58962 | 2025-11-02 04:18:00 | NOAA-21 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f2bb5f14-8ad9-3bbe-8c38-99fa051fd673 | -3.22753 | -50.58199 | 2025-11-02 04:18:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 17848497-7276-310d-896d-d91742725733 | -3.93705 | -52.20653 | 2025-11-02 04:18:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 1d5146c7-ac80-3435-8ff5-c599b6640060 | -3.8105 | -52.41459 | 2025-11-02 04:18:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 81a38e2b-0a26-35b6-9b34-fb908f3d5eb1 | -4.5469 | -46.02783 | 2025-11-02 04:18:00 | NOAA-21 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 188dcc62-8af4-3e7b-b6f2-8726b357c55d | -5.7928 | -40.83206 | 2025-11-02 04:18:00 | NOAA-21 | QUITERIANÓPOLIS | CEARÁ | Brasil | 2311264 | 23 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 45004ad6-dda8-342f-b007-02c32a8b99c0 | -5.61939 | -41.09451 | 2025-11-02 04:18:00 | NOAA-21 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| e460739b-435e-3f83-bfc8-3d6fdc828d17 | -3.73538 | -49.68858 | 2025-11-02 04:18:00 | NOAA-21 | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 86da0580-d899-354a-b25e-0de2cd2dc003 | -2.83534 | -49.40413 | 2025-11-02 04:18:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 36c2913d-7c56-35e5-bc2c-4ec569aed56e | -4.81664 | -45.85572 | 2025-11-02 04:18:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 4775ed88-8a0c-31a9-9200-2d4835a9ff91 | -4.67892 | -44.61966 | 2025-11-02 04:18:00 | NOAA-21 | BERNARDO DO MEARIM | MARANHÃO | Brasil | 2101939 | 21 | 33 | nan | nan | nan | Cerrado | 4.7 |
| cc6940fd-be3a-3352-bbd8-ad9b4ae95b9d | -3.5176 | -49.71849 | 2025-11-02 04:18:00 | NOAA-21 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| f2d7e09e-5118-398e-8b2d-b521b1bc6088 | -5.12895 | -43.37248 | 2025-11-02 04:18:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 1dd66c28-10fd-3a46-bd5f-26991683c8ca | -4.31748 | -45.63609 | 2025-11-02 04:18:00 | NOAA-21 | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 56f6f20c-a832-3b54-8a46-c91fb4531200 | -3.223 | -50.58126 | 2025-11-02 04:18:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| c61df558-d02b-3891-95d7-0b4e29c2d809 | -4.30083 | -45.89481 | 2025-11-02 04:18:00 | NOAA-21 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 9010709a-16bc-3a96-8b41-fd24546f204f | -2.84016 | -49.40099 | 2025-11-02 04:18:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f4e1a0d0-2260-39ba-99e8-edd0c8236dce | -4.14568 | -46.27672 | 2025-11-02 04:18:00 | NOAA-21 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 31a10f73-4d61-39d4-816e-26ed7e17db49 | -5.623 | -41.09509 | 2025-11-02 04:18:00 | NOAA-21 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| d99e3b34-ce69-394a-91f1-afa3ca941803 | -4.6384 | -38.57171 | 2025-11-02 04:18:00 | NOAA-21 | OCARA | CEARÁ | Brasil | 2309458 | 23 | 33 | nan | nan | nan | Caatinga | 9.3 |
| 8eebe4a3-c701-32b6-8c98-cbe2169b7cda | -4.81606 | -45.85934 | 2025-11-02 04:18:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| fcf32ba5-a074-3fc3-a19a-a506c902fa72 | -3.72495 | -50.04597 | 2025-11-02 04:18:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| fe5a14f7-cdcf-3ee0-b557-a0fba9a83e07 | -3.01525 | -49.44706 | 2025-11-02 04:18:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 10.1 |
| a709d45d-58ea-37b8-b021-3b2ce0be566a | -3.38449 | -52.36782 | 2025-11-02 04:18:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 825d2d2c-89e3-33ee-ba43-7d0388854e34 | -3.34947 | -51.68151 | 2025-11-02 04:18:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 622d1e76-d9ec-3306-86c1-f7619a587b22 | -3.42725 | -45.91184 | 2025-11-02 04:18:00 | NOAA-21 | GOVERNADOR NEWTON BELLO | MARANHÃO | Brasil | 2104651 | 21 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 3873d093-392d-37c1-bdc6-1857db2c6435 | -4.32086 | -45.63661 | 2025-11-02 04:18:00 | NOAA-21 | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 9ea65486-eabd-32a9-8004-f143f207bc12 | -3.31049 | -50.31468 | 2025-11-02 04:18:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 12763423-af35-3820-bfed-840938034e59 | -4.32028 | -45.64024 | 2025-11-02 04:18:00 | NOAA-21 | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 48e49642-bd32-3a6d-920a-004227b3f806 | -4.62771 | -46.40162 | 2025-11-02 04:18:00 | NOAA-21 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| de868097-de98-3eef-9b5c-abc6f915e715 | -3.7115 | -45.89097 | 2025-11-02 04:18:00 | NOAA-21 | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| c81971db-ee59-37af-982e-6a77190dda9c | -3.72862 | -51.70314 | 2025-11-02 04:18:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| b442c1c8-a29d-3fd6-a49f-e11c73ce3613 | -2.4903 | -48.14977 | 2025-11-02 04:18:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 394fa4cc-b555-3f31-aefe-f8225602edff | -4.42253 | -40.90406 | 2025-11-02 04:18:00 | NOAA-21 | CROATÁ | CEARÁ | Brasil | 2304236 | 23 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 22fb552b-8937-370a-b9ef-9977574540fc | -3.89386 | -52.09651 | 2025-11-02 04:18:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| ecccf586-290e-3e9b-b846-ce1df5b546ae | -3.3842 | -49.9768 | 2025-11-02 04:18:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 295b8554-cb77-3a86-96fe-cabafbc6cb94 | -4.30156 | -48.06812 | 2025-11-02 04:18:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c29fbaef-5b8b-3817-b35a-dbdcf7cbaef0 | -4.77901 | -45.29978 | 2025-11-02 04:18:00 | NOAA-21 | LAGO DA PEDRA | MARANHÃO | Brasil | 2105708 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| f8e6f9e7-1f84-31c4-b07c-03bd127de930 | -4.21627 | -48.35434 | 2025-11-02 04:18:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| f10003d2-6bd7-3b68-93bf-4b731de0ee76 | -4.81052 | -45.69883 | 2025-11-02 04:18:00 | NOAA-21 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 2ce0be11-b3c6-3e45-95cf-dfc2b3638d86 | -3.45576 | -45.57656 | 2025-11-02 04:18:00 | NOAA-21 | GOVERNADOR NEWTON BELLO | MARANHÃO | Brasil | 2104651 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 1ecf79b3-86e0-3d71-b0bf-68b0dadbd536 | -5.07142 | -43.67652 | 2025-11-02 04:18:00 | NOAA-21 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 9c338b8c-f69f-367e-97e0-99eaf0078816 | -2.27043 | -47.85517 | 2025-11-02 04:18:00 | NOAA-21 | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |


[Clique aqui para ver as próximas entradas](README7.md)
