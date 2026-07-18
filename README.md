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

## Dados Diários - Página 1

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 5469fbd0-1942-3001-871c-b36b97d7b88a | -18.7364 | -54.1988 | 2026-07-18 00:00:00 | GOES-19 | FIGUEIRÃO | MATO GROSSO DO SUL | Brasil | 5003900 | 50 | 33 | nan | nan | nan | Cerrado | 41.6 |
| ff7c931e-96e8-3627-a75a-434c3b6a8633 | -18.7364 | -54.1988 | 2026-07-18 00:10:00 | GOES-19 | FIGUEIRÃO | MATO GROSSO DO SUL | Brasil | 5003900 | 50 | 33 | nan | nan | nan | Cerrado | 78.3 |
| c6911856-9508-3dd0-bf5d-4bc0f2c80006 | -20.064 | -58.0248 | 2026-07-18 00:10:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 76.6 |
| 5fa6c9c9-d5b0-3516-8080-dcd8b44c9f75 | -20.064 | -58.0248 | 2026-07-18 00:20:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 52.0 |
| 571f7777-42ee-39c6-b339-f1a2252b8ae9 | -18.7364 | -54.1988 | 2026-07-18 00:20:00 | GOES-19 | FIGUEIRÃO | MATO GROSSO DO SUL | Brasil | 5003900 | 50 | 33 | nan | nan | nan | Cerrado | 97.2 |
| 14d8728d-ed2f-3125-ae24-d8667de315ba | -22.4122 | -51.5309 | 2026-07-18 00:20:00 | GOES-19 | NARANDIBA | SÃO PAULO | Brasil | 3532207 | 35 | 33 | nan | nan | nan | Mata Atlântica | 66.9 |
| 5e814589-060e-3de8-893c-28271bcf97fc | -20.9834 | -40.899101 | 2026-07-18 00:20:00 | METOP-B | ITAPEMIRIM | ESPÍRITO SANTO | Brasil | 3202801 | 32 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 60c2c4f0-6d72-3434-b9bc-019eeb9a187d | -2.791 | -49.518799 | 2026-07-18 00:20:00 | METOP-B | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b6d43787-a883-30ae-915c-51b845b9cd0a | -22.249001 | -52.859001 | 2026-07-18 00:20:00 | METOP-B | ANAURILÂNDIA | MATO GROSSO DO SUL | Brasil | 5000807 | 50 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 04c37e84-bf55-33a7-a409-2ede81c5ffc4 | -18.7285 | -54.180199 | 2026-07-18 00:20:00 | METOP-B | FIGUEIRÃO | MATO GROSSO DO SUL | Brasil | 5003900 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| 7d3eeabb-b076-35ee-a365-f9cf2898bfbf | -7.4808 | -46.6558 | 2026-07-18 00:20:00 | METOP-B | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| d7e550fc-e72e-3c6b-ad9a-b489b574a836 | -8.129 | -47.8699 | 2026-07-18 00:20:00 | METOP-B | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 044d4e64-cb07-3581-99f0-20c432ba02f3 | -20.0606 | -57.995399 | 2026-07-18 00:20:00 | METOP-B | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 6035a33b-6497-3d1c-9c98-976b1464d163 | -21.2682 | -49.144001 | 2026-07-18 00:20:00 | METOP-B | MARAPOAMA | SÃO PAULO | Brasil | 3528858 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 298c4dd1-9f9f-33e7-ada9-f583b459a20c | -5.918 | -43.633499 | 2026-07-18 00:20:00 | METOP-B | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| bb0808db-8d5e-3bd3-a12b-14ed42b2c37f | -20.9093 | -43.937901 | 2026-07-18 00:20:00 | METOP-B | CASA GRANDE | MINAS GERAIS | Brasil | 3114907 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| df1c3059-0960-3f0d-8297-8b5e34753610 | -20.906799 | -43.9277 | 2026-07-18 00:20:00 | METOP-B | CASA GRANDE | MINAS GERAIS | Brasil | 3114907 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 9997c6d3-24d2-3a97-bac0-fcc0acc4a2f2 | -4.1003 | -49.344002 | 2026-07-18 00:20:00 | METOP-B | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| bdb0d3fe-e4a1-3d73-a859-edd1cfd006a1 | -1.5893 | -50.434502 | 2026-07-18 00:20:00 | METOP-B | BREVES | PARÁ | Brasil | 1501808 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 8bec5954-14af-3fbc-8ee2-61697a489763 | -20.625099 | -41.3941 | 2026-07-18 00:20:00 | METOP-B | ALEGRE | ESPÍRITO SANTO | Brasil | 3200201 | 32 | 33 | nan | nan | nan | Mata Atlântica | nan |
| f842d313-c5fe-3ce6-b338-35336e6d4773 | -14.0831 | -50.355 | 2026-07-18 00:20:00 | METOP-B | NOVA CRIXÁS | GOIÁS | Brasil | 5214838 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 252bbc77-bf73-3a44-87ae-19a739ec3d70 | -8.7169 | -49.6003 | 2026-07-18 00:20:00 | METOP-B | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 40978638-1bd0-3936-a820-86b104a42cbd | -6.6727 | -47.5103 | 2026-07-18 00:20:00 | METOP-B | PALMEIRAS DO TOCANTINS | TOCANTINS | Brasil | 1713809 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| dd03a5aa-6462-325e-b788-e8b6f801ec91 | -9.3025 | -51.912701 | 2026-07-18 00:20:00 | METOP-B | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 3a1603e1-233b-3307-86cf-2258278eed79 | -7.2786 | -46.240101 | 2026-07-18 00:20:00 | METOP-B | NOVA COLINAS | MARANHÃO | Brasil | 2107258 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 0b25a562-8f2f-3d08-980b-f963f2083033 | -10.649 | -47.220501 | 2026-07-18 00:20:00 | METOP-B | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| fa92f4a7-979a-35c9-8c93-f005fa2d2acf | -18.740299 | -54.1889 | 2026-07-18 00:20:00 | METOP-B | FIGUEIRÃO | MATO GROSSO DO SUL | Brasil | 5003900 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| fdd3e119-0708-3843-9f97-07c5a929653e | -9.0749 | -50.5807 | 2026-07-18 00:20:00 | METOP-B | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 540cebc8-abd2-34bd-82ff-0a127741e6c5 | -9.1009 | -50.604099 | 2026-07-18 00:20:00 | METOP-B | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 82587b18-30a3-3578-a81d-4af127d67de2 | -5.5214 | -45.2649 | 2026-07-18 00:20:00 | METOP-B | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 94c2cf9c-727f-36ce-a414-8d4746408e9e | -20.356501 | -48.310001 | 2026-07-18 00:20:00 | METOP-B | GUAÍRA | SÃO PAULO | Brasil | 3517406 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| 1f4c6fc9-dbe0-3a71-b0dd-5ced9a9af3f4 | -20.6213 | -41.379601 | 2026-07-18 00:20:00 | METOP-B | CASTELO | ESPÍRITO SANTO | Brasil | 3201407 | 32 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 7f7b085c-d76c-3da8-8153-f722dd502b17 | -22.2509 | -52.869301 | 2026-07-18 00:20:00 | METOP-B | ANAURILÂNDIA | MATO GROSSO DO SUL | Brasil | 5000807 | 50 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 3b06a581-6774-31a5-bd44-1e3f3c1fec27 | -8.945 | -47.6105 | 2026-07-18 00:20:00 | METOP-B | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| e63b10e6-6d5d-3ec6-b887-21f160d6b530 | -11.4721 | -47.338402 | 2026-07-18 00:20:00 | METOP-B | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 8cc1a4f8-1751-3474-91f9-431199ff0269 | -7.2813 | -46.2514 | 2026-07-18 00:20:00 | METOP-B | NOVA COLINAS | MARANHÃO | Brasil | 2107258 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 2009a167-abed-3c8d-8aec-196f493293c9 | -9.1417 | -49.833 | 2026-07-18 00:20:00 | METOP-B | CASEARA | TOCANTINS | Brasil | 1703909 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 34b44705-4858-3918-8234-272a8837f317 | -12.4554 | -49.576199 | 2026-07-18 00:20:00 | METOP-B | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 6c22db41-0a72-3cde-b946-c11c39d7f9cb | -22.4811 | -50.490501 | 2026-07-18 00:20:00 | METOP-B | PARAGUAÇU PAULISTA | SÃO PAULO | Brasil | 3535507 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| cca39e17-8bff-376e-a5a6-813ccac38d9f | -1.5876 | -50.426701 | 2026-07-18 00:20:00 | METOP-B | BREVES | PARÁ | Brasil | 1501808 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 01a80498-9e87-3954-a96d-1459c59f9877 | -18.738199 | -54.1782 | 2026-07-18 00:20:00 | METOP-B | FIGUEIRÃO | MATO GROSSO DO SUL | Brasil | 5003900 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| 27d706a4-9335-3801-9651-0a8a340b5654 | -9.0765 | -50.587601 | 2026-07-18 00:20:00 | METOP-B | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f9317dd1-caf4-3f0a-928b-6fb502d1b64c | -12.1216 | -49.922901 | 2026-07-18 00:20:00 | METOP-B | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 9e593a04-5fd6-390b-a5dc-db1369f595aa | -10.529 | -48.158199 | 2026-07-18 00:20:00 | METOP-B | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| bb4a0d96-e49a-3969-80f2-d1216a532f91 | -8.4758 | -50.213001 | 2026-07-18 00:20:00 | METOP-B | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0f0eb02b-f763-3fa3-bdc1-7393dbba6e79 | -8.1171 | -47.8633 | 2026-07-18 00:20:00 | METOP-B | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| bdea1d3f-47ab-3dec-8784-0b9accc568ab | -20.5639 | -57.3521 | 2026-07-18 00:20:00 | METOP-B | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| 5418a2cb-f98a-3f60-b0df-0268ea40a25b | -9.0911 | -50.6063 | 2026-07-18 00:20:00 | METOP-B | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c983ccfb-fe4d-3c5d-949f-c937bca106d3 | -9.6991 | -47.700802 | 2026-07-18 00:20:00 | METOP-B | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 4dfd2c8c-9e4e-3d69-8c19-de606ddebcc0 | -22.401699 | -51.5313 | 2026-07-18 00:20:00 | METOP-B | NARANDIBA | SÃO PAULO | Brasil | 3532207 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 7603a1ae-c31a-3fca-a093-a73141bfdb74 | -8.9429 | -47.601601 | 2026-07-18 00:20:00 | METOP-B | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| dfc07400-9c60-3e38-960b-dcd05e8fe413 | -22.4828 | -50.4986 | 2026-07-18 00:20:00 | METOP-B | PARAGUAÇU PAULISTA | SÃO PAULO | Brasil | 3535507 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| 971cff76-4189-3f27-8feb-203365f9edb5 | -7.2883 | -46.237801 | 2026-07-18 00:20:00 | METOP-B | NOVA COLINAS | MARANHÃO | Brasil | 2107258 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 82e257b7-9df1-3652-ae59-8dd5d7c06901 | -20.069599 | -43.690701 | 2026-07-18 00:20:00 | METOP-B | SANTA BÁRBARA | MINAS GERAIS | Brasil | 3157203 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| f4708d47-3c77-342e-ad54-44d81871c502 | -19.823999 | -57.957298 | 2026-07-18 00:20:00 | METOP-B | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| f43a0af8-90e1-3df0-a1cb-e095cc8d8541 | -28.861799 | -52.570999 | 2026-07-18 00:20:00 | METOP-B | SOLEDADE | RIO GRANDE DO SUL | Brasil | 4320800 | 43 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 675e8790-8297-3afd-8650-d74dd9c83d2f | -7.8486 | -48.3908 | 2026-07-18 00:20:00 | METOP-B | PALMEIRANTE | TOCANTINS | Brasil | 1715705 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 305297b7-c7ee-3cb7-9bb0-ad5108ebedc8 | -9.0813 | -50.608601 | 2026-07-18 00:20:00 | METOP-B | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 5c382a9f-7d4f-38d5-a4f3-137c7c4a27c5 | -6.9276 | -51.930801 | 2026-07-18 00:20:00 | METOP-B | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c9f15673-5016-3b3d-81ae-2d82c98d3d3e | -6.9193 | -51.939899 | 2026-07-18 00:20:00 | METOP-B | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 21b20aef-6070-3edf-aa89-9e123007080d | -2.7677 | -49.462299 | 2026-07-18 00:20:00 | METOP-B | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 24def714-9263-39bc-871f-ffc7048c3c2e | -8.6924 | -49.852699 | 2026-07-18 00:20:00 | METOP-B | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e59b930e-63df-38e2-99b6-35b69c06d162 | -18.732599 | -54.201698 | 2026-07-18 00:20:00 | METOP-B | FIGUEIRÃO | MATO GROSSO DO SUL | Brasil | 5003900 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| 6d8bee8f-5797-3c4d-88a8-14ce0fe9376c | -22.411501 | -51.529099 | 2026-07-18 00:20:00 | METOP-B | NARANDIBA | SÃO PAULO | Brasil | 3532207 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| a4bb6ea9-a8f1-3fba-b2df-cb95a7fa8770 | -8.7415 | -49.438099 | 2026-07-18 00:20:00 | METOP-B | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 98581005-f696-3df8-8b42-743a10638f3a | -9.9039 | -53.382 | 2026-07-18 00:20:00 | METOP-B | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 2ef7bfdb-d526-3c7d-b891-5bfda4f0ccb8 | -19.9242 | -57.898701 | 2026-07-18 00:20:00 | METOP-B | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| d8d463a9-121a-3463-9916-32858f2b3490 | -22.247101 | -52.848801 | 2026-07-18 00:20:00 | METOP-B | ANAURILÂNDIA | MATO GROSSO DO SUL | Brasil | 5000807 | 50 | 33 | nan | nan | nan | Mata Atlântica | nan |
| e308937c-6662-3dd1-babe-c3f56fce475e | -20.566999 | -57.370499 | 2026-07-18 00:20:00 | METOP-B | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| 0b5aa093-4c0c-3271-8a8e-57166b503850 | -12.457 | -49.583401 | 2026-07-18 00:20:00 | METOP-B | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 9ea73865-e514-3e4e-abfa-d9eaf51d5668 | -12.1232 | -49.93 | 2026-07-18 00:20:00 | METOP-B | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| d186a221-d9bd-3464-b92b-88403fbff7c5 | -20.063999 | -58.015301 | 2026-07-18 00:20:00 | METOP-B | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| ec7ab56a-e7bd-3f46-b576-3f96514ca7ae | -9.1401 | -49.825699 | 2026-07-18 00:20:00 | METOP-B | CASEARA | TOCANTINS | Brasil | 1703909 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 8941ad71-37b8-3b13-8bf3-be72ee5fba9f | -6.9178 | -51.932999 | 2026-07-18 00:20:00 | METOP-B | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 758fbeec-5064-3a2d-80fe-d9b5a17f0d91 | -9.5192 | -47.114899 | 2026-07-18 00:20:00 | METOP-B | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 42d58610-9a21-3eee-a690-e397c24aa9ec | -18.7423 | -54.199699 | 2026-07-18 00:20:00 | METOP-B | FIGUEIRÃO | MATO GROSSO DO SUL | Brasil | 5003900 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| 0365b78a-6817-356f-a860-36af23e7aa47 | -22.7976 | -49.334202 | 2026-07-18 00:20:00 | METOP-B | ÁGUAS DE SANTA BÁRBARA | SÃO PAULO | Brasil | 3500550 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| 2001bf20-6229-3cea-ae8d-8cab6bebf17f | -22.4646 | -43.090599 | 2026-07-18 00:20:00 | METOP-B | PETRÓPOLIS | RIO DE JANEIRO | Brasil | 3303906 | 33 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 1e196521-23d1-36e6-98b8-206a3a6c8044 | -9.529 | -47.112499 | 2026-07-18 00:20:00 | METOP-B | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 7465f7fb-589d-35d9-95b2-538a01ae2738 | -20.631001 | -41.376701 | 2026-07-18 00:20:00 | METOP-B | ALEGRE | ESPÍRITO SANTO | Brasil | 3200201 | 32 | 33 | nan | nan | nan | Mata Atlântica | nan |
| e88b9e60-4f9b-38ce-a71e-0dc078fdf4d1 | -11.5522 | -48.251499 | 2026-07-18 00:20:00 | METOP-B | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| f03252a6-57e5-383b-9ca8-7fb006c9777b | -22.796 | -49.326599 | 2026-07-18 00:20:00 | METOP-B | ÁGUAS DE SANTA BÁRBARA | SÃO PAULO | Brasil | 3500550 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| 13da6745-347a-3828-86d0-e5de37a9458b | -9.697 | -47.692101 | 2026-07-18 00:20:00 | METOP-B | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| cf6752ce-bcce-34d4-ad36-f1f63dc7ec07 | -22.258699 | -52.856899 | 2026-07-18 00:20:00 | METOP-B | ANAURILÂNDIA | MATO GROSSO DO SUL | Brasil | 5000807 | 50 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 0179b66f-1eed-3c4f-8e4c-3f37c0398054 | -4.1022 | -49.3522 | 2026-07-18 00:20:00 | METOP-B | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c007b612-cda4-33b2-9e84-687d80606650 | -19.933901 | -57.8969 | 2026-07-18 00:20:00 | METOP-B | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| a2cf7247-e334-3b06-8c00-0e86e7399a4b | -22.4 | -51.522499 | 2026-07-18 00:20:00 | METOP-B | NARANDIBA | SÃO PAULO | Brasil | 3532207 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| d6ab7a93-728b-37d5-b1b7-88bc38a836f5 | -19.814199 | -57.959099 | 2026-07-18 00:20:00 | METOP-B | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| ec23e546-9aac-3849-a76a-ff9dcdd76fe0 | -19.8141 | -57.898899 | 2026-07-18 00:20:00 | METOP-B | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| bfc336c6-7966-3b8f-9ff7-039c7a0a9895 | -21.269699 | -49.151299 | 2026-07-18 00:20:00 | METOP-B | MARAPOAMA | SÃO PAULO | Brasil | 3528858 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| e93f51f2-db6d-3410-9dc6-da80a7d700fc | -8.1269 | -47.861 | 2026-07-18 00:20:00 | METOP-B | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 2ed54fd6-d225-34af-87e4-5fe20d3d9508 | -22.3983 | -51.513599 | 2026-07-18 00:20:00 | METOP-B | NARANDIBA | SÃO PAULO | Brasil | 3532207 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 2748c8b9-080f-384c-886b-8f5ccbfbfee4 | -22.461901 | -43.0798 | 2026-07-18 00:20:00 | METOP-B | PETRÓPOLIS | RIO DE JANEIRO | Brasil | 3303906 | 33 | 33 | nan | nan | nan | Mata Atlântica | nan |
| a4771fae-4945-388e-8e0e-e3aa6d13b35c | -8.4774 | -50.2201 | 2026-07-18 00:20:00 | METOP-B | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e2a08bbc-bec0-3760-ab91-4b5af8d339f1 | -12.4586 | -49.5905 | 2026-07-18 00:20:00 | METOP-B | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 8f2abd5a-37ca-3c2d-bdd9-829814fdeeab | -10.5252 | -48.141899 | 2026-07-18 00:20:00 | METOP-B | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 627c64b4-7d4b-3fab-b856-64b9fed76e70 | -7.8466 | -48.382401 | 2026-07-18 00:20:00 | METOP-B | PALMEIRANTE | TOCANTINS | Brasil | 1715705 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 8971e186-3428-30ef-b156-30a038d1e5ae | -19.788401 | -48.257401 | 2026-07-18 00:20:00 | METOP-B | UBERABA | MINAS GERAIS | Brasil | 3170107 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| bb705886-2e78-3fa1-8900-e0b213714317 | -22.922001 | -49.1926 | 2026-07-18 00:20:00 | METOP-B | ÁGUAS DE SANTA BÁRBARA | SÃO PAULO | Brasil | 3500550 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| 5e3a2cf2-51c9-3c71-abc2-5d330857fc91 | -22.4035 | -51.540199 | 2026-07-18 00:20:00 | METOP-B | NARANDIBA | SÃO PAULO | Brasil | 3532207 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |


[Clique aqui para ver as próximas entradas](README2.md)
