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

## Dados Diários - Página 15

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 4766e47c-8ad5-38b3-a3ff-d3c4624875fc | -13.2904 | -57.09266 | 2025-06-12 04:29:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| e9f3f653-f104-3b4c-b52a-b2239b446a1b | -12.13573 | -54.65724 | 2025-06-12 04:29:00 | NPP-375D | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| a0b79895-82bb-39c8-9732-d5538420d72f | -13.28774 | -57.07284 | 2025-06-12 04:29:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 8f486e40-f0d4-3b4f-80b2-03c3957af36e | -12.70848 | -58.0402 | 2025-06-12 04:29:00 | NPP-375D | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| ee76f292-85bc-3404-b8b3-9d2bec78e38f | -12.39765 | -40.90943 | 2025-06-12 04:29:00 | NPP-375D | LAJEDINHO | BAHIA | Brasil | 2919009 | 29 | 33 | nan | nan | nan | Caatinga | 2.3 |
| af301d77-605a-3f1a-8549-2cbc244bbcbc | -14.42072 | -47.89498 | 2025-06-12 04:29:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 71b4ecce-1872-3da2-9507-d0540b224b33 | -10.867 | -54.32619 | 2025-06-12 04:29:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 9a079f5d-a3b0-34aa-9158-30cc74894824 | -12.22394 | -55.523 | 2025-06-12 04:29:00 | NPP-375D | VERA | MATO GROSSO | Brasil | 5108501 | 51 | 33 | nan | nan | nan | Amazônia | 4.1 |
| e0cca9d3-1920-38bb-9570-5c3b56855244 | -12.52718 | -57.23348 | 2025-06-12 04:29:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 414071b7-b574-3129-b10b-c33793096a99 | -11.61046 | -46.99036 | 2025-06-12 04:29:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| c71ec440-7b9c-3890-ba87-f7e5b7b17414 | -12.13486 | -54.66189 | 2025-06-12 04:29:00 | NPP-375D | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| d7f4c681-1e30-3d94-8983-ef650af19fc4 | -13.9056 | -54.6498 | 2025-06-12 04:30:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 55.5 |
| b9b48b1c-f118-36e0-9689-e7b717c8ed7d | -20.72378 | -56.65809 | 2025-06-12 04:32:00 | NPP-375D | BODOQUENA | MATO GROSSO DO SUL | Brasil | 5002159 | 50 | 33 | nan | nan | nan | Cerrado | 1.0 |
| ca0472db-dd2c-3e88-807a-0f8102b177ed | -22.54024 | -48.81444 | 2025-06-12 04:32:00 | NPP-375D | MACATUBA | SÃO PAULO | Brasil | 3528007 | 35 | 33 | nan | nan | nan | Cerrado | 1.1 |
| c4a45395-5b4c-3c17-8838-94fdba22bd2f | -19.9696 | -44.21737 | 2025-06-12 04:32:00 | NPP-375D | BETIM | MINAS GERAIS | Brasil | 3106705 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 302055f0-e2b7-3183-85fe-695a5007c03f | -18.6518 | -55.72169 | 2025-06-12 04:32:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.2 |
| d9152f55-0111-304b-8af3-fa42e2c40406 | -19.68334 | -46.46638 | 2025-06-12 04:32:00 | NPP-375D | PRATINHA | MINAS GERAIS | Brasil | 3153004 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| aecd95f5-5219-3662-a2c3-8c39e3f94839 | -18.6614 | -55.73964 | 2025-06-12 04:32:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 0.8 |
| 34936e87-9eec-318c-bfff-d568567600cc | -18.6649 | -55.74499 | 2025-06-12 04:32:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 0.8 |
| 880fd573-32f7-31bc-8264-d08d482c7459 | -20.60504 | -48.87222 | 2025-06-12 04:32:00 | NPP-375D | OLÍMPIA | SÃO PAULO | Brasil | 3533908 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 6d05b78a-ad56-3e7e-8176-98289f27becb | -20.44542 | -46.40115 | 2025-06-12 04:32:00 | NPP-375D | VARGEM BONITA | MINAS GERAIS | Brasil | 3170602 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 810056b1-666e-3714-9ab8-649d7418b6bc | -20.60447 | -48.87595 | 2025-06-12 04:32:00 | NPP-375D | OLÍMPIA | SÃO PAULO | Brasil | 3533908 | 35 | 33 | nan | nan | nan | Mata Atlântica | 6.5 |
| 0815adec-db34-3bd7-9cf7-be2bb0d50eb9 | -20.43328 | -46.40904 | 2025-06-12 04:32:00 | NPP-375D | VARGEM BONITA | MINAS GERAIS | Brasil | 3170602 | 31 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 7fceadb1-4413-3815-8795-d52fc23adeda | -19.57698 | -49.10508 | 2025-06-12 04:32:00 | NPP-375D | PRATA | MINAS GERAIS | Brasil | 3152808 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 93a9491f-2534-3a25-b365-32e0986be071 | -18.66054 | -55.74405 | 2025-06-12 04:32:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 0.8 |
| 529537d4-7d90-333b-bc40-c85027b007cf | -20.56108 | -50.104 | 2025-06-12 04:32:00 | NPP-375D | NHANDEARA | SÃO PAULO | Brasil | 3532603 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| fbcbfb1d-678a-3441-9f1d-fa03d7117ae5 | -19.02253 | -57.62225 | 2025-06-12 04:32:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.5 |
| d96caafc-c373-3f70-b4f6-d65d12b56885 | -21.612 | -57.57644 | 2025-06-12 04:32:00 | NPP-375D | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 66e9d168-5c2a-3226-8595-60102afb16d8 | -19.57756 | -49.10141 | 2025-06-12 04:32:00 | NPP-375D | PRATA | MINAS GERAIS | Brasil | 3152808 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 03ddb922-03a8-36c3-832e-6c8c3d14cd44 | -21.82841 | -56.27008 | 2025-06-12 04:32:00 | NPP-375D | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 4987fd58-66fc-3391-a393-33633a2e6c06 | -19.99856 | -46.44019 | 2025-06-12 04:32:00 | NPP-375D | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 0331ebc8-0c43-3862-ad78-d00b2db80a96 | -20.72913 | -56.65445 | 2025-06-12 04:32:00 | NPP-375D | BODOQUENA | MATO GROSSO DO SUL | Brasil | 5002159 | 50 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 8d2d67a7-8039-3711-865c-7b2dc1a42014 | -20.44839 | -46.40638 | 2025-06-12 04:32:00 | NPP-375D | VARGEM BONITA | MINAS GERAIS | Brasil | 3170602 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 51cfbe8c-38b4-3d9b-9f21-d6d4870a3a71 | -20.37374 | -55.03708 | 2025-06-12 04:32:00 | NPP-375D | TERENOS | MATO GROSSO DO SUL | Brasil | 5008008 | 50 | 33 | nan | nan | nan | Cerrado | 0.8 |
| a84fdf59-63e9-394a-809f-3df295397b6e | -19.57641 | -49.10875 | 2025-06-12 04:32:00 | NPP-375D | PRATA | MINAS GERAIS | Brasil | 3152808 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 29f36907-c5df-3cdc-a6b2-b20f86beb386 | -20.56049 | -50.10771 | 2025-06-12 04:32:00 | NPP-375D | NHANDEARA | SÃO PAULO | Brasil | 3532603 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.5 |
| ba608353-af48-32f0-bda8-470dfa954162 | -18.66313 | -55.73081 | 2025-06-12 04:32:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.0 |
| 9b404a47-3724-3619-b3c4-bca6f3568a88 | -19.89182 | -54.66903 | 2025-06-12 04:32:00 | NPP-375D | ROCHEDO | MATO GROSSO DO SUL | Brasil | 5007505 | 50 | 33 | nan | nan | nan | Cerrado | 0.8 |
| bd751983-1ba8-3cd6-901d-fdeb4b24ea13 | -18.65877 | -55.72988 | 2025-06-12 04:32:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.0 |
| 9002e69b-b338-361f-ac1f-da187614e56f | -18.38026 | -44.50811 | 2025-06-12 04:32:00 | NPP-375D | CORINTO | MINAS GERAIS | Brasil | 3119104 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 72718b71-3e64-370a-a126-b86f3aa9632e | -21.19645 | -44.93538 | 2025-06-12 04:32:00 | NPP-375D | IJACI | MINAS GERAIS | Brasil | 3130408 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 5c073387-8b0e-3dbe-b39e-2e881e081479 | -20.73362 | -56.65522 | 2025-06-12 04:32:00 | NPP-375D | BODOQUENA | MATO GROSSO DO SUL | Brasil | 5002159 | 50 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 3669fb89-51d9-330c-91ad-aaa854e84161 | -20.44052 | -46.41003 | 2025-06-12 04:32:00 | NPP-375D | VARGEM BONITA | MINAS GERAIS | Brasil | 3170602 | 31 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 38825eae-5453-398e-8473-0678f3e5d6b7 | -21.82925 | -56.26585 | 2025-06-12 04:32:00 | NPP-375D | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 8a71f8cb-35c5-35ec-a8c4-c40219aa29ae | -20.3778 | -55.03788 | 2025-06-12 04:32:00 | NPP-375D | TERENOS | MATO GROSSO DO SUL | Brasil | 5008008 | 50 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 4e7ccbc1-4a9f-30f9-a405-752a6c0e188e | -20.7328 | -56.65938 | 2025-06-12 04:32:00 | NPP-375D | BODOQUENA | MATO GROSSO DO SUL | Brasil | 5002159 | 50 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 6c5a8775-97f8-3e45-a7ce-1116a71dc450 | -20.55715 | -50.10711 | 2025-06-12 04:32:00 | NPP-375D | NHANDEARA | SÃO PAULO | Brasil | 3532603 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.5 |
| a3ddd4fb-3159-395d-8f99-6c0cecb08038 | -22.77406 | -49.32008 | 2025-06-12 04:32:00 | NPP-375D | ÁGUAS DE SANTA BÁRBARA | SÃO PAULO | Brasil | 3500550 | 35 | 33 | nan | nan | nan | Cerrado | 3.0 |
| cf31ead2-58db-3a9f-9011-e2323ddceae8 | -20.43689 | -46.40958 | 2025-06-12 04:32:00 | NPP-375D | VARGEM BONITA | MINAS GERAIS | Brasil | 3170602 | 31 | 33 | nan | nan | nan | Cerrado | 2.3 |
| abbcc1c7-a710-3add-bbee-8748a86a1a44 | -21.82418 | -56.26905 | 2025-06-12 04:32:00 | NPP-375D | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 161e58e3-91e2-390c-a1ce-b3d4a0d5f044 | -19.99502 | -43.97909 | 2025-06-12 04:32:00 | NPP-375D | BELO HORIZONTE | MINAS GERAIS | Brasil | 3106200 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 688015bc-f1d7-3553-86a2-b0ed2878fc70 | -20.92246 | -49.09369 | 2025-06-12 04:32:00 | NPP-375D | TABAPUÃ | SÃO PAULO | Brasil | 3552601 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| f8233eb8-d17c-3196-82ff-c9574dd1e47b | -19.08399 | -53.46404 | 2025-06-12 04:32:00 | NPP-375D | CAMAPUÃ | MATO GROSSO DO SUL | Brasil | 5002605 | 50 | 33 | nan | nan | nan | Cerrado | 1.5 |
| b54f14a1-f8c4-3298-b840-ee59cb0d913d | -19.08021 | -53.46329 | 2025-06-12 04:32:00 | NPP-375D | CAMAPUÃ | MATO GROSSO DO SUL | Brasil | 5002605 | 50 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 8fa259ca-7fe5-3a53-ad1c-e1e24705d943 | -23.238 | -51.28479 | 2025-06-12 04:32:00 | NPP-375D | CAMBÉ | PARANÁ | Brasil | 4103701 | 41 | 33 | nan | nan | nan | Mata Atlântica | 6.8 |
| 28108982-22e0-3b64-a3c2-d883c14b4d7d | -20.55775 | -50.1034 | 2025-06-12 04:32:00 | NPP-375D | NHANDEARA | SÃO PAULO | Brasil | 3532603 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 018eaf3e-d421-30c1-b4db-51659b106531 | -21.82502 | -56.26481 | 2025-06-12 04:32:00 | NPP-375D | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 73f0bd20-0b9d-35c5-809b-61d926e13316 | -20.7283 | -56.6587 | 2025-06-12 04:32:00 | NPP-375D | BODOQUENA | MATO GROSSO DO SUL | Brasil | 5002159 | 50 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 2aaa63aa-11c0-3efd-8482-5697d9a65c3e | -18.66227 | -55.73522 | 2025-06-12 04:32:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.0 |
| 71b7f582-2267-3354-9b94-2b7f441f9b2a | -21.63417 | -49.84282 | 2025-06-12 04:32:00 | NPP-375D | PROMISSÃO | SÃO PAULO | Brasil | 3541604 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| fad31c6a-81b4-3c3d-94d3-dc1202fe50eb | -20.44903 | -46.40174 | 2025-06-12 04:32:00 | NPP-375D | VARGEM BONITA | MINAS GERAIS | Brasil | 3170602 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 62425977-c37b-3add-9f5f-a42fb77da81f | -19.02127 | -57.62128 | 2025-06-12 04:32:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.1 |
| 60ec4fdf-84e5-3c78-9d6d-607e0ada47c1 | -22.7707 | -49.3195 | 2025-06-12 04:32:00 | NPP-375D | ÁGUAS DE SANTA BÁRBARA | SÃO PAULO | Brasil | 3500550 | 35 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 98dc1474-c89e-341b-92ee-a868d1cffe4e | -19.45438 | -45.30488 | 2025-06-12 04:32:00 | NPP-375D | MARTINHO CAMPOS | MINAS GERAIS | Brasil | 3140506 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 68ab2d35-a317-3e30-a4e1-c7e5c20491d3 | -20.99517 | -51.79144 | 2025-06-12 04:32:00 | NPP-375D | TRÊS LAGOAS | MATO GROSSO DO SUL | Brasil | 5008305 | 50 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 0e620817-df8c-3369-9fa1-fa75692780e2 | -19.05063 | -53.46073 | 2025-06-12 04:32:00 | NPP-375D | CAMAPUÃ | MATO GROSSO DO SUL | Brasil | 5002605 | 50 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 33329334-7ead-3d6e-bbef-daff851d36ff | -28.58774 | -49.44117 | 2025-06-12 04:34:00 | NPP-375D | SIDERÓPOLIS | SANTA CATARINA | Brasil | 4217600 | 42 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 4ceb80fb-6609-3606-a19d-ff28c2b826c2 | -29.9173 | -56.13144 | 2025-06-12 04:34:00 | NPP-375D | ALEGRETE | RIO GRANDE DO SUL | Brasil | 4300406 | 43 | 33 | nan | nan | nan | Pampa | 1.0 |
| 7e40e8cd-59c4-3ae1-930d-bc20eef6e4c1 | -25.19082 | -49.32738 | 2025-06-12 04:34:00 | NPP-375D | RIO BRANCO DO SUL | PARANÁ | Brasil | 4122206 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| ea942ab2-0645-33f2-85cf-4dfca82d7bc3 | -26.72711 | -50.12316 | 2025-06-12 04:34:00 | NPP-375D | PAPANDUVA | SANTA CATARINA | Brasil | 4212205 | 42 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| d948ab4c-c8bf-30fa-85d8-bac26fb9cb0b | -30.80236 | -55.38047 | 2025-06-12 04:34:00 | NPP-375D | SANT'ANA DO LIVRAMENTO | RIO GRANDE DO SUL | Brasil | 4317103 | 43 | 33 | nan | nan | nan | Pampa | 0.8 |
| 0581faa4-4edd-3980-a5ca-a4c042b192b8 | -27.60227 | -50.0231 | 2025-06-12 04:34:00 | NPP-375D | LAGES | SANTA CATARINA | Brasil | 4209300 | 42 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 15f2f738-4900-338e-adb5-27070e4166e6 | -13.8864 | -54.6519 | 2025-06-12 04:40:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 55.8 |
| 2cc06d65-6a6e-33a4-8a49-33f389fdf28a | -8.96569 | -47.9652 | 2025-06-12 04:49:00 | NOAA-20 | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 60290472-9df1-38de-aebc-fa88c5070e29 | -6.96055 | -42.80976 | 2025-06-12 04:49:00 | NOAA-20 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 3.3 |
| 21ccbd77-7fbc-3b63-8d4a-aa1540809a85 | -5.91486 | -43.45977 | 2025-06-12 04:49:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 27ddf84d-ec13-3a05-914e-5d9e263191eb | -9.02261 | -49.58665 | 2025-06-12 04:49:00 | NOAA-20 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 831bf0a5-2f92-3e69-a230-fa67804c0c93 | -9.27556 | -48.26077 | 2025-06-12 04:49:00 | NOAA-20 | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 942afa25-bde5-3b66-a674-0f428045a121 | -10.03977 | -48.78254 | 2025-06-12 04:49:00 | NOAA-20 | PARAÍSO DO TOCANTINS | TOCANTINS | Brasil | 1716109 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 5d5b17e3-8368-345b-aa11-6f1fc02d85a2 | -7.11283 | -55.64643 | 2025-06-12 04:49:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 3ef20486-2fc5-3017-83ae-cc0aac178c29 | -5.78013 | -43.61729 | 2025-06-12 04:49:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 9978d0cf-dbee-350f-a2c2-e5b63abafba0 | -7.24181 | -55.41174 | 2025-06-12 04:49:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| dba10114-43c2-3746-9346-a3e8f7f3a704 | -4.71183 | -48.4288 | 2025-06-12 04:49:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 2cb91c23-7c6d-3800-91b8-1d7927567545 | -2.90559 | -54.48969 | 2025-06-12 04:49:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 2a3a28ff-9680-32f1-943a-190362327a07 | -9.76513 | -48.58076 | 2025-06-12 04:49:00 | NOAA-20 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 080f68eb-9855-3068-91de-e1fa8d7d117e | -8.30798 | -47.91858 | 2025-06-12 04:49:00 | NOAA-20 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 03ea1259-f408-3ced-8a76-13766b66fac4 | -9.6042 | -49.02079 | 2025-06-12 04:49:00 | NOAA-20 | ABREULÂNDIA | TOCANTINS | Brasil | 1700251 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 47b9a2af-2dd1-3b03-a851-9244444aa584 | -8.59106 | -47.09134 | 2025-06-12 04:49:00 | NOAA-20 | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 91a06e95-8efb-37b0-8717-7a8dc362dc22 | -9.3903 | -48.42591 | 2025-06-12 04:49:00 | NOAA-20 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 76e1c562-5bc6-3d4f-90a7-b655120c920a | -6.94359 | -44.56824 | 2025-06-12 04:49:00 | NOAA-20 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 0b1a9c83-f6fb-3ba1-9a8c-5d7db0da3186 | -10.17726 | -49.35149 | 2025-06-12 04:49:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 3e92b643-255a-3ff8-bfd1-9ab725fe909c | -9.84968 | -47.88001 | 2025-06-12 04:49:00 | NOAA-20 | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 397779f2-34d4-3ee5-a71e-d01d83080743 | -8.96465 | -47.97247 | 2025-06-12 04:49:00 | NOAA-20 | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 935ac7fd-72a1-33d1-b495-1195d07c2148 | -5.77969 | -43.62045 | 2025-06-12 04:49:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| f236332a-1c3b-3ed6-a712-56d109deae78 | -6.15946 | -47.26912 | 2025-06-12 04:49:00 | NOAA-20 | CAMPESTRE DO MARANHÃO | MARANHÃO | Brasil | 2102556 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 9a644534-16e7-34fc-add5-2296c682f8c5 | -8.96872 | -47.97304 | 2025-06-12 04:49:00 | NOAA-20 | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 70d72769-8ccd-35b7-a302-11c5d12675c1 | -8.71611 | -47.85122 | 2025-06-12 04:49:00 | NOAA-20 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 3bcbaa43-2b18-3ae7-9033-81448d0e9f1b | -8.96924 | -47.96942 | 2025-06-12 04:49:00 | NOAA-20 | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 12b65330-2b89-3333-816d-f93b31510f98 | -4.71368 | -48.42656 | 2025-06-12 04:49:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 872b842b-a24f-39fa-a31e-90242359e3b7 | -2.91236 | -48.23389 | 2025-06-12 04:49:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |


[Clique aqui para ver as próximas entradas](README16.md)
