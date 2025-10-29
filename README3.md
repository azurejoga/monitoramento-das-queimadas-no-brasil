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

## Dados Diários - Página 3

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 961fef70-004d-3657-ac34-ebb4a1aec285 | -17.8789 | -40.0946 | 2025-10-29 01:30:00 | GOES-19 | MUCURI | BAHIA | Brasil | 2922003 | 29 | 33 | nan | nan | nan | Mata Atlântica | 54.5 |
| d42d5810-54b5-3dcf-836f-09943dbc28b5 | -6.2939 | -41.8744 | 2025-10-29 01:30:00 | GOES-19 | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 111.3 |
| 4c3ee007-8f28-3d7e-b5cd-51fa4186530a | -7.8037 | -46.4458 | 2025-10-29 01:30:00 | GOES-19 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 60.1 |
| dd07307d-8360-3abf-8fdc-6d86acce52ba | -2.4264 | -49.2948 | 2025-10-29 01:30:00 | GOES-19 | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 49.6 |
| ab8372b1-6ef8-3e51-8854-166fd090368b | -2.4263 | -49.3161 | 2025-10-29 01:30:00 | GOES-19 | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 43.1 |
| 57db0789-1941-3e06-9e66-11de2bcfe797 | -12.19683 | -63.44475 | 2025-10-29 01:32:00 | TERRA_M-M | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 6.9 |
| fe181a20-f890-3077-aa07-2962d526abf5 | 0.45363 | -60.49802 | 2025-10-29 01:34:00 | TERRA_M-M | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 12.6 |
| 35dde314-9483-323f-8b9b-ab9ba4c6f46d | 3.14139 | -60.68897 | 2025-10-29 01:34:00 | TERRA_M-M | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 15.3 |
| f1ef18c7-d0c6-33f7-8db0-8c45c4fc5280 | 0.45614 | -60.48059 | 2025-10-29 01:34:00 | TERRA_M-M | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 21.9 |
| cffdb4eb-42e9-382d-a891-42baf7987d38 | 0.44838 | -60.48528 | 2025-10-29 01:34:00 | TERRA_M-M | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 31.4 |
| a6057a3f-9d8f-37ae-ac39-8a7864fb3683 | -4.2156 | -50.1022 | 2025-10-29 01:40:00 | GOES-19 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 108.9 |
| 9f0f0171-31f0-3bf1-af2e-695864d9b3a2 | -4.5188 | -45.9937 | 2025-10-29 01:40:00 | GOES-19 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 47.6 |
| 42016698-4acb-3eda-83e6-3ca4e3f68e03 | -9.457 | -40.3889 | 2025-10-29 01:40:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 63.6 |
| 07e1629e-d2b8-3a39-871f-f5bbb7158ca0 | -15.1006 | -43.8333 | 2025-10-29 01:40:00 | GOES-19 | MATIAS CARDOSO | MINAS GERAIS | Brasil | 3140852 | 31 | 33 | nan | nan | nan | Cerrado | 87.2 |
| 3f3a8594-884f-3303-b776-27feb23f44e8 | -4.1971 | -50.103 | 2025-10-29 01:40:00 | GOES-19 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 59.8 |
| 3f21849b-dae7-3b64-b4af-4075bae0372e | 1.9606 | -50.9653 | 2025-10-29 01:40:00 | GOES-19 | AMAPÁ | AMAPÁ | Brasil | 1600105 | 16 | 33 | nan | nan | nan | Amazônia | 58.0 |
| 354b5496-5d46-39b1-a953-76d994e88de6 | -6.2939 | -41.8744 | 2025-10-29 01:40:00 | GOES-19 | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 36.7 |
| 6f8bc6e2-1fe1-3d98-9af9-44db885192b4 | -4.4805 | -43.4237 | 2025-10-29 01:40:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 60.3 |
| 85b7c1f4-4f5b-301f-b8e2-f40257929b7e | -12.1958 | -46.717 | 2025-10-29 01:40:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 72.5 |
| 7c7fde8b-f54f-32f8-9e90-5954d51b5d15 | -19.4214 | -48.0566 | 2025-10-29 01:40:00 | GOES-19 | UBERABA | MINAS GERAIS | Brasil | 3170107 | 31 | 33 | nan | nan | nan | Cerrado | 63.2 |
| d3b55c29-0d97-3af4-a958-31d13a4afb62 | -9.4574 | -40.3641 | 2025-10-29 01:40:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 66.7 |
| 7e2a9f74-b3a2-3df8-955f-2846cdf860cf | 1.9606 | -50.9445 | 2025-10-29 01:40:00 | GOES-19 | AMAPÁ | AMAPÁ | Brasil | 1600105 | 16 | 33 | nan | nan | nan | Amazônia | 49.4 |
| 8213bb91-3a0e-335c-8cbd-8c668f936594 | -4.1972 | -50.0819 | 2025-10-29 01:40:00 | GOES-19 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 123.8 |
| b9b5d937-e8d4-3f3b-8448-241d8ee57ba4 | -10.6506 | -48.009 | 2025-10-29 01:40:00 | GOES-19 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 63.8 |
| fa8080c2-c26b-3b00-822f-6b3bd6e26848 | -9.4379 | -40.3917 | 2025-10-29 01:40:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 101.2 |
| ee358ba7-794e-397a-a94a-e7da68ee29cf | -2.4264 | -49.2948 | 2025-10-29 01:40:00 | GOES-19 | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 42.2 |
| 8dc20e64-5fcc-32d4-b7bc-a676b08a4fb3 | -7.8037 | -46.4458 | 2025-10-29 01:40:00 | GOES-19 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 66.4 |
| bb07d39c-8d60-3ef3-a4b9-6c500539c969 | -9.4383 | -40.3668 | 2025-10-29 01:40:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 109.2 |
| 2b1256c6-c261-3754-8325-e34b0cdc75cf | -12.0032 | -46.7892 | 2025-10-29 01:40:00 | GOES-19 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 82.2 |
| 1fd736b2-2a94-3bfa-b26a-d3a744a7de02 | -10.6509 | -47.9869 | 2025-10-29 01:40:00 | GOES-19 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 54.1 |
| f47a3375-f0f7-3fe4-8461-e8c6852c3de4 | -12.0036 | -46.7667 | 2025-10-29 01:40:00 | GOES-19 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 94.8 |
| 4338f8ef-fb1f-35d8-848c-8dfbf73ecedb | -4.4804 | -43.447 | 2025-10-29 01:40:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 81.9 |
| 6aa74222-680c-38fc-90b8-d8cdca81346d | -4.2157 | -50.0812 | 2025-10-29 01:40:00 | GOES-19 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 247.7 |
| c1a50cd2-a689-3f45-baa8-2716783872ef | -19.4214 | -48.0566 | 2025-10-29 01:50:00 | GOES-19 | UBERABA | MINAS GERAIS | Brasil | 3170107 | 31 | 33 | nan | nan | nan | Cerrado | 91.2 |
| 1ef5c309-2c82-3e10-ae93-2811bc4ec13f | -12.0036 | -46.7667 | 2025-10-29 01:50:00 | GOES-19 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 95.2 |
| edbebcb3-7c19-34c6-bf60-cc2207b8a9db | -4.4805 | -43.4237 | 2025-10-29 01:50:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 58.8 |
| fd11d4e2-0050-3fbf-97cb-a7df1cb61323 | -15.1006 | -43.8333 | 2025-10-29 01:50:00 | GOES-19 | MATIAS CARDOSO | MINAS GERAIS | Brasil | 3140852 | 31 | 33 | nan | nan | nan | Cerrado | 100.7 |
| faba7512-12a2-31fd-b23c-da5c3f9698d9 | -12.0032 | -46.7892 | 2025-10-29 01:50:00 | GOES-19 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 89.2 |
| 6a689388-3e59-315b-8f32-20942cc3f4c0 | -4.2156 | -50.1022 | 2025-10-29 01:50:00 | GOES-19 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 95.7 |
| 4145b0b6-9d12-3ad7-81a6-679589b8a2ed | -6.2939 | -41.8744 | 2025-10-29 01:50:00 | GOES-19 | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 39.6 |
| ca9c1939-ff95-38bb-9610-5673ab2062cd | -4.1972 | -50.0819 | 2025-10-29 01:50:00 | GOES-19 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 81.0 |
| b7dbea1a-a8c6-3e22-b351-9c8175e925df | -4.4804 | -43.447 | 2025-10-29 01:50:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 79.2 |
| 4d110aa2-c345-3684-bf4b-bb9a6a5abefb | -2.4264 | -49.2948 | 2025-10-29 01:50:00 | GOES-19 | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 46.7 |
| 734d5be5-8362-341f-bc25-7b29f32841bd | -7.8037 | -46.4458 | 2025-10-29 01:50:00 | GOES-19 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 69.4 |
| 5ec062ee-4a6a-3c23-a2eb-2d0e1efe9337 | -12.1958 | -46.717 | 2025-10-29 01:50:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 69.7 |
| aec8259c-b454-33a8-8b1d-17b723103f60 | -4.2157 | -50.0812 | 2025-10-29 01:50:00 | GOES-19 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 194.6 |
| b5822a66-732e-399e-9975-7081e95318b8 | -12.1958 | -46.717 | 2025-10-29 02:00:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 65.0 |
| a723bf98-5371-3b88-a214-98e3e83d4a71 | -6.2939 | -41.8744 | 2025-10-29 02:00:00 | GOES-19 | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 111.0 |
| 49eb5fc4-e4d1-32eb-8f45-c4a224b31ca6 | -2.4264 | -49.2948 | 2025-10-29 02:00:00 | GOES-19 | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 47.4 |
| 21e66f15-1c93-3c99-8beb-e9498dfcd790 | -6.2936 | -41.8984 | 2025-10-29 02:00:00 | GOES-19 | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 42.1 |
| 63455ca1-4c98-3fb6-be82-a22a0583025e | -4.2157 | -50.0812 | 2025-10-29 02:00:00 | GOES-19 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 161.1 |
| f4f9811b-166f-3e46-947f-a5bd7e7eb5e2 | -2.4263 | -49.3161 | 2025-10-29 02:00:00 | GOES-19 | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 41.0 |
| e25a88b9-81f8-31dd-b54d-e83b4f20ba21 | -12.0036 | -46.7667 | 2025-10-29 02:00:00 | GOES-19 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 91.1 |
| 4959c599-021a-34f5-a78c-afe6d5c7f9b5 | -4.4804 | -43.447 | 2025-10-29 02:00:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 79.9 |
| ef1e1194-2783-331b-9b41-2b9f27084572 | -13.6426 | -46.4976 | 2025-10-29 02:00:00 | GOES-19 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 92.4 |
| d6f141a9-14ed-3e53-9f82-daf83c80dad8 | -12.0032 | -46.7892 | 2025-10-29 02:00:00 | GOES-19 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 103.8 |
| b1bd96a8-3604-3792-850b-4eb4aeb7c41c | -4.2156 | -50.1022 | 2025-10-29 02:00:00 | GOES-19 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 69.8 |
| f9628209-e838-3132-ba0c-b4b93ff5cd38 | -4.1972 | -50.0819 | 2025-10-29 02:00:00 | GOES-19 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 80.8 |
| 42e928cb-f780-38c9-8d3a-e3207372355f | -6.3127 | -41.8727 | 2025-10-29 02:00:00 | GOES-19 | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 79.4 |
| 520ac126-d3e6-3fa0-9408-4ceb396c9554 | -10.6509 | -47.9869 | 2025-10-29 02:00:00 | GOES-19 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 102.8 |
| 7ef97f48-b940-3171-86d6-f863a74fe3ba | -7.8037 | -46.4458 | 2025-10-29 02:00:00 | GOES-19 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 67.6 |
| 4c912dd8-b1a8-312f-bf01-62e39dac587b | -10.6506 | -48.009 | 2025-10-29 02:00:00 | GOES-19 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 102.1 |
| 0e987030-15e7-382c-bc6c-55934de81078 | -15.1006 | -43.8333 | 2025-10-29 02:00:00 | GOES-19 | MATIAS CARDOSO | MINAS GERAIS | Brasil | 3140852 | 31 | 33 | nan | nan | nan | Cerrado | 141.9 |
| a310e5ca-a4ec-37bc-b97a-8bbeed971b7c | -4.2156 | -50.1022 | 2025-10-29 02:10:00 | GOES-19 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 71.2 |
| 0f5b6031-8628-363f-982c-059a00ce4632 | -4.4805 | -43.4237 | 2025-10-29 02:10:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 55.0 |
| d960f4ea-06cb-3116-899f-8d49999ff620 | -6.2939 | -41.8744 | 2025-10-29 02:10:00 | GOES-19 | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 100.2 |
| c902a654-f3ac-36bd-8974-e281a7d90ff2 | -9.0456 | -45.0541 | 2025-10-29 02:10:00 | GOES-19 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 76.0 |
| 12929b47-d93e-3e58-8f85-c28fe914216f | -13.6426 | -46.4976 | 2025-10-29 02:10:00 | GOES-19 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 102.0 |
| b440320b-8222-3ce3-b202-b9c03f0fd6f0 | -15.1202 | -43.8294 | 2025-10-29 02:10:00 | GOES-19 | JAÍBA | MINAS GERAIS | Brasil | 3135050 | 31 | 33 | nan | nan | nan | Cerrado | 72.5 |
| 5e955aad-00fc-391b-b336-dcda3cb2d14b | -4.4804 | -43.447 | 2025-10-29 02:10:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 86.8 |
| 7934f611-6c0d-31c0-86a7-4b91482ce67d | -10.6509 | -47.9869 | 2025-10-29 02:10:00 | GOES-19 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 100.7 |
| 568ad54b-ac47-3c31-aa1b-ea08f6931bc4 | -4.1972 | -50.0819 | 2025-10-29 02:10:00 | GOES-19 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 78.0 |
| 6392ab53-1712-3a5c-8384-a38b0f00f64d | -12.0036 | -46.7667 | 2025-10-29 02:10:00 | GOES-19 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 81.2 |
| 06f12cef-0b4a-3401-b249-0de71532e20f | -9.5106 | -46.9872 | 2025-10-29 02:10:00 | GOES-19 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 65.6 |
| a34fd13d-acb8-3761-9863-146d824538a6 | -7.8037 | -46.4458 | 2025-10-29 02:10:00 | GOES-19 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 66.8 |
| 1fed1c91-06cf-377e-8bfc-385990a04ad0 | -9.0646 | -45.052 | 2025-10-29 02:10:00 | GOES-19 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 66.5 |
| 5f945ede-8330-3da5-b552-f8978ca7885b | -10.6506 | -48.009 | 2025-10-29 02:10:00 | GOES-19 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 102.9 |
| cedba2cc-426f-3ea5-83a4-4582a5bceccf | -2.4264 | -49.2948 | 2025-10-29 02:10:00 | GOES-19 | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 41.6 |
| ebd7ad6f-7d03-3691-91ae-97422464e23b | -6.2936 | -41.8984 | 2025-10-29 02:10:00 | GOES-19 | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 54.4 |
| 1c15dd21-56fe-356a-bb4d-d648e473883b | -6.3127 | -41.8727 | 2025-10-29 02:10:00 | GOES-19 | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 87.1 |
| fbdb9a48-58d9-3c85-b96f-2b32b71ed2b6 | -15.0809 | -43.8372 | 2025-10-29 02:10:00 | GOES-19 | MATIAS CARDOSO | MINAS GERAIS | Brasil | 3140852 | 31 | 33 | nan | nan | nan | Caatinga | 71.2 |
| c4c270ea-c014-37d6-abf1-a66313cf1dcd | -12.0032 | -46.7892 | 2025-10-29 02:10:00 | GOES-19 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 93.9 |
| e1033ea9-148f-3ae2-9208-0bc16282d0eb | -12.1958 | -46.717 | 2025-10-29 02:10:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 84.4 |
| 42bcf5dc-b8c5-33ae-a7ce-8db2fbcd2a91 | -15.1006 | -43.8333 | 2025-10-29 02:10:00 | GOES-19 | MATIAS CARDOSO | MINAS GERAIS | Brasil | 3140852 | 31 | 33 | nan | nan | nan | Cerrado | 192.8 |
| 75710a1e-523b-36f8-ae88-359659f0cef5 | -4.2157 | -50.0812 | 2025-10-29 02:10:00 | GOES-19 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 137.5 |
| c6c3cffd-60ab-34df-8797-909e9e41f0d0 | -9.4913 | -47.0115 | 2025-10-29 02:10:00 | GOES-19 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 110.1 |
| bcedebfd-97c6-38de-98e9-58456e836b59 | -9.4916 | -46.9893 | 2025-10-29 02:10:00 | GOES-19 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 93.5 |
| c6fe6afd-8fc0-339e-99b5-eeb0b6c679c6 | -4.4805 | -43.4237 | 2025-10-29 02:20:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 53.4 |
| 0096d560-4a2d-3919-8814-a070d05e2df5 | -9.5103 | -47.0095 | 2025-10-29 02:20:00 | GOES-19 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 54.4 |
| 09a1b492-096d-3de6-b4fe-0db8ae528e31 | -19.4417 | -48.0522 | 2025-10-29 02:20:00 | GOES-19 | UBERABA | MINAS GERAIS | Brasil | 3170107 | 31 | 33 | nan | nan | nan | Cerrado | 85.2 |
| 6b20b270-6bda-3c7d-8af9-35a10a1eaa73 | -9.4916 | -46.9893 | 2025-10-29 02:20:00 | GOES-19 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 137.9 |
| fea23cd6-f1fd-3939-a133-74f51e88a096 | -4.2156 | -50.1022 | 2025-10-29 02:20:00 | GOES-19 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 74.3 |
| bb5777d0-1079-33f9-9454-5b1515f54b42 | -15.1202 | -43.8294 | 2025-10-29 02:20:00 | GOES-19 | JAÍBA | MINAS GERAIS | Brasil | 3135050 | 31 | 33 | nan | nan | nan | Cerrado | 117.2 |
| d230d1cf-a400-34d0-8423-72854cd69005 | -9.4913 | -47.0115 | 2025-10-29 02:20:00 | GOES-19 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 185.5 |
| 803df717-36df-39de-98d3-efcb5025273b | -4.4804 | -43.447 | 2025-10-29 02:20:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 79.3 |
| ea7e3dfc-eaaa-3455-b238-4341e7f2b4ec | -2.4264 | -49.2948 | 2025-10-29 02:20:00 | GOES-19 | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 45.7 |
| c67cc606-ce3d-38de-a66a-6d6c19f03612 | -15.1006 | -43.8333 | 2025-10-29 02:20:00 | GOES-19 | MATIAS CARDOSO | MINAS GERAIS | Brasil | 3140852 | 31 | 33 | nan | nan | nan | Cerrado | 361.9 |
| db0f12ba-db5f-36e7-b823-08b4852b81df | -9.5109 | -46.9649 | 2025-10-29 02:20:00 | GOES-19 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 73.1 |
| 99ea301d-d82c-37ff-a626-098e986a0ded | -4.2157 | -50.0812 | 2025-10-29 02:20:00 | GOES-19 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 131.8 |
| 39840d9e-3d4c-3749-87d9-9e94b7d1102b | -12.0036 | -46.7667 | 2025-10-29 02:20:00 | GOES-19 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 92.6 |


[Clique aqui para ver as próximas entradas](README4.md)
