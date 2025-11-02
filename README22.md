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

## Dados Diários - Página 22

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 5c7af2cf-a340-3ef2-adbe-a36c1d184042 | -15.24024 | -51.75023 | 2025-11-02 04:53:00 | NPP-375D | ARAGUAIANA | MATO GROSSO | Brasil | 5101001 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 70926e41-8705-3d01-b8d8-b564e3f089ab | -13.51223 | -57.24089 | 2025-11-02 04:53:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 838247a3-a1e0-32f8-911d-c160e33e7610 | -13.49035 | -61.45505 | 2025-11-02 04:53:00 | NPP-375D | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 36348f37-7a5b-3610-ba31-865fcaffe30f | -13.49486 | -61.44375 | 2025-11-02 04:53:00 | NPP-375D | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| c4428d4b-5715-346f-8fca-35edbff358df | -15.06558 | -52.79271 | 2025-11-02 04:53:00 | NPP-375D | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| dfed159f-fdd4-32b0-b4c7-37538d06ed3f | -15.62752 | -58.22895 | 2025-11-02 04:53:00 | NPP-375D | SÃO JOSÉ DOS QUATRO MARCOS | MATO GROSSO | Brasil | 5107107 | 51 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 7bf9bd6e-13c6-39b7-b086-eeef4110de3e | -15.62187 | -58.2307 | 2025-11-02 04:53:00 | NPP-375D | SÃO JOSÉ DOS QUATRO MARCOS | MATO GROSSO | Brasil | 5107107 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 53b8b371-fb08-396b-b47a-620c39b2f3f5 | -18.77413 | -47.30974 | 2025-11-02 04:53:00 | NPP-375D | MONTE CARMELO | MINAS GERAIS | Brasil | 3143104 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 9c92674b-c1df-332f-b07a-356cbe4d54d9 | -18.19977 | -54.01992 | 2025-11-02 04:53:00 | NPP-375D | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 0.3 |
| e2468f85-8886-3150-8962-0b8cd45da551 | -13.49038 | -61.43962 | 2025-11-02 04:53:00 | NPP-375D | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 27b29460-0c9e-31f7-802e-dec6fabf1137 | -19.33294 | -54.32031 | 2025-11-02 04:53:00 | NPP-375D | SÃO GABRIEL DO OESTE | MATO GROSSO DO SUL | Brasil | 5007695 | 50 | 33 | nan | nan | nan | Cerrado | 0.6 |
| b865c448-98e8-36be-8a62-ed0b3ee0c0d2 | -12.45023 | -63.12216 | 2025-11-02 04:53:00 | NPP-375D | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 2.3 |
| b10c7c31-5eb3-3a02-92ba-7271da12505c | -18.526 | -45.34563 | 2025-11-02 04:53:00 | NPP-375D | MORADA NOVA DE MINAS | MINAS GERAIS | Brasil | 3143500 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| ee267a31-ba11-38bb-952e-fda2186b1304 | -13.49304 | -61.453 | 2025-11-02 04:53:00 | NPP-375D | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 2.6 |
| a8221c81-2086-3ff4-8033-2b5a51268783 | -14.46947 | -55.98782 | 2025-11-02 04:53:00 | NPP-375D | NOBRES | MATO GROSSO | Brasil | 5105903 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 04111265-05f9-3c31-a7fa-b8633258d54e | -15.23968 | -51.75393 | 2025-11-02 04:53:00 | NPP-375D | ARAGUAIANA | MATO GROSSO | Brasil | 5101001 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| cbe6f183-c297-3d83-8e29-850842bba4a6 | -12.37166 | -63.88729 | 2025-11-02 04:53:00 | NPP-375D | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 1.9 |
| fc422d63-ab9f-3447-b0bf-93de00fcc13d | -13.49547 | -61.44067 | 2025-11-02 04:53:00 | NPP-375D | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ce23e681-8dc2-3083-bf72-81fa4deaeed7 | -12.44362 | -63.12508 | 2025-11-02 04:53:00 | NPP-375D | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 635e8ce6-0974-33d1-84ed-20301af45f70 | -13.49625 | -56.56735 | 2025-11-02 04:53:00 | NPP-375D | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| d3399b08-3c00-3243-bc54-fa656be73073 | -13.49545 | -61.4561 | 2025-11-02 04:53:00 | NPP-375D | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 2b506bc9-aa29-3d3e-907e-a2449b4b5d7b | -15.1141 | -47.24868 | 2025-11-02 04:53:00 | NPP-375D | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 78dd8cf7-cd9f-3ae0-9ced-a390c480e15f | -12.43364 | -63.1447 | 2025-11-02 04:53:00 | NPP-375D | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 41551270-a15c-3e23-bb7a-0663f8355a8b | -18.50138 | -46.96474 | 2025-11-02 04:53:00 | NPP-375D | COROMANDEL | MINAS GERAIS | Brasil | 3119302 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| c2fb44b5-5286-3a1a-98b9-9994ef3a06a4 | -14.45461 | -51.52949 | 2025-11-02 04:53:00 | NPP-375D | ARAGUAIANA | MATO GROSSO | Brasil | 5101001 | 51 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 3fd0ec30-d285-382b-a71d-bb8221f5b762 | -12.37926 | -63.88151 | 2025-11-02 04:53:00 | NPP-375D | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 71429d9f-a661-3d6e-b7c6-138267d07c43 | -16.86499 | -47.91565 | 2025-11-02 04:53:00 | NPP-375D | LUZIÂNIA | GOIÁS | Brasil | 5212501 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 83bf48b4-8ac6-3880-b34e-99c733096c6a | -13.49329 | -61.43961 | 2025-11-02 04:53:00 | NPP-375D | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| dc7ca9f0-c062-3d95-afea-ddfd9091f852 | -15.6268 | -58.22618 | 2025-11-02 04:53:00 | NPP-375D | SÃO JOSÉ DOS QUATRO MARCOS | MATO GROSSO | Brasil | 5107107 | 51 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 3219c90b-3fca-3d9d-a36e-6680f48c7249 | -12.37352 | -63.87792 | 2025-11-02 04:53:00 | NPP-375D | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a625744b-d31b-333b-a693-b9450e1eb001 | -17.61213 | -52.08428 | 2025-11-02 04:53:00 | NPP-375D | PEROLÂNDIA | GOIÁS | Brasil | 5216452 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 07be92a7-e0f4-3d6d-b115-b392a17503fc | -14.4518 | -51.52525 | 2025-11-02 04:53:00 | NPP-375D | ARAGUAIANA | MATO GROSSO | Brasil | 5101001 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 258ac28f-fcf3-3628-88ed-e625ce2b75c0 | -12.3783 | -63.88619 | 2025-11-02 04:53:00 | NPP-375D | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 1eb4c143-9a04-3d9a-9584-d8366cf1f7c8 | -17.8529 | -51.7325 | 2025-11-02 04:53:00 | NPP-375D | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| d252fad8-2edb-3124-9455-86ed81cd867a | -15.62654 | -58.23428 | 2025-11-02 04:53:00 | NPP-375D | SÃO JOSÉ DOS QUATRO MARCOS | MATO GROSSO | Brasil | 5107107 | 51 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 39d1822e-e814-35a9-a9dd-52053e1148ed | -15.30031 | -42.96072 | 2025-11-02 04:53:00 | NPP-375D | MONTE AZUL | MINAS GERAIS | Brasil | 3142908 | 31 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 2b2d8925-a340-3c04-800a-7cc4005a23d5 | -12.37958 | -63.87924 | 2025-11-02 04:53:00 | NPP-375D | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 771ca4f7-b832-3a1b-b8f7-0d503538dbff | -13.97333 | -52.44987 | 2025-11-02 04:53:00 | NPP-375D | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 0.5 |
| dd097aaa-a98c-3003-acc3-68ece177ba5c | -15.25771 | -51.74925 | 2025-11-02 04:53:00 | NPP-375D | ARAGUAIANA | MATO GROSSO | Brasil | 5101001 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 7c165f52-971e-3802-98a2-0c81b019fc69 | -13.49721 | -61.44684 | 2025-11-02 04:53:00 | NPP-375D | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 0.7 |
| b3e30bbe-1561-3785-9dca-cec2f9c5ee98 | -15.30261 | -59.23601 | 2025-11-02 04:53:00 | NPP-375D | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| c1a9f119-c8d1-3ff7-87f3-0adae6615949 | -15.29465 | -42.96004 | 2025-11-02 04:53:00 | NPP-375D | MONTE AZUL | MINAS GERAIS | Brasil | 3142908 | 31 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 353b74a8-e525-3220-b2cf-6a71fa852365 | -12.4287 | -63.13929 | 2025-11-02 04:53:00 | NPP-375D | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 3a50a733-9c31-3af1-9cc8-2b69872cc047 | -17.61206 | -52.08403 | 2025-11-02 04:53:00 | NPP-375D | PEROLÂNDIA | GOIÁS | Brasil | 5216452 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 0378a7f1-c505-31bd-84ea-f5c0c394d541 | -18.7747 | -47.30513 | 2025-11-02 04:53:00 | NPP-375D | PATROCÍNIO | MINAS GERAIS | Brasil | 3148103 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| fb2b955f-ab59-3411-8feb-d092ac49a631 | -20.29445 | -54.08303 | 2025-11-02 04:53:00 | NPP-375D | JARAGUARI | MATO GROSSO DO SUL | Brasil | 5004908 | 50 | 33 | nan | nan | nan | Cerrado | 3.7 |
| a5e33c36-fa09-392b-b98e-c95be3750774 | -15.24305 | -51.75448 | 2025-11-02 04:53:00 | NPP-375D | ARAGUAIANA | MATO GROSSO | Brasil | 5101001 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 5a4876dc-2889-3e57-b571-0cd14676e844 | -15.62354 | -58.22815 | 2025-11-02 04:53:00 | NPP-375D | SÃO JOSÉ DOS QUATRO MARCOS | MATO GROSSO | Brasil | 5107107 | 51 | 33 | nan | nan | nan | Amazônia | 4.4 |
| fa62c534-2bc9-3217-93e7-949828a0e3cb | -15.62451 | -58.22287 | 2025-11-02 04:53:00 | NPP-375D | SÃO JOSÉ DOS QUATRO MARCOS | MATO GROSSO | Brasil | 5107107 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 5fd2f463-3b48-39e6-a342-4fed2d01abb6 | -13.49839 | -61.44067 | 2025-11-02 04:53:00 | NPP-375D | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 0.2 |
| 908808dc-0fa1-3f66-96ca-3781c7280d1d | -18.45464 | -51.63264 | 2025-11-02 04:53:00 | NPP-375D | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | 0.4 |
| e54f1e26-a024-3c65-a444-45c5dd52875f | -15.62586 | -58.23149 | 2025-11-02 04:53:00 | NPP-375D | SÃO JOSÉ DOS QUATRO MARCOS | MATO GROSSO | Brasil | 5107107 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 82116b7a-fb95-3c9e-9c07-ecf38bb648da | -14.86946 | -51.80534 | 2025-11-02 04:53:00 | NPP-375D | ARAGUAIANA | MATO GROSSO | Brasil | 5101001 | 51 | 33 | nan | nan | nan | Cerrado | 0.6 |
| ed66676a-bf20-3f0b-9d09-06986062201f | -13.49153 | -61.44886 | 2025-11-02 04:53:00 | NPP-375D | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| f6b85831-10e8-3b3f-90ec-2abf8d5710e8 | -13.49212 | -61.44577 | 2025-11-02 04:53:00 | NPP-375D | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 8ae1827d-920d-37b2-b3c4-b68a1652758d | -17.08348 | -44.48512 | 2025-11-02 04:53:00 | NPP-375D | JEQUITAÍ | MINAS GERAIS | Brasil | 3135605 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| f4e4d2b3-d4a4-3e85-896e-bd7980f596ba | -12.4494 | -63.12633 | 2025-11-02 04:53:00 | NPP-375D | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 3443419e-7f21-386b-b2b6-25b94b872edd | -15.32786 | -43.88819 | 2025-11-02 04:53:00 | NPP-375D | JAÍBA | MINAS GERAIS | Brasil | 3135050 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 1bece914-4f99-3a50-9a32-fb53640c21db | -18.51987 | -53.49167 | 2025-11-02 04:53:00 | NPP-375D | COSTA RICA | MATO GROSSO DO SUL | Brasil | 5003256 | 50 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 20091eac-8303-3a55-93cf-cfe8b9e5cf1e | -14.29801 | -52.49536 | 2025-11-02 04:53:00 | NPP-375D | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 50c70925-0982-3e0b-99d3-a56a0113e9b1 | -18.50193 | -46.96029 | 2025-11-02 04:53:00 | NPP-375D | COROMANDEL | MINAS GERAIS | Brasil | 3119302 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| f99709ad-0e8c-3ce1-9911-5feec8e0e6bc | -12.44027 | -63.14175 | 2025-11-02 04:53:00 | NPP-375D | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 7025cf86-4ac3-365a-9fdb-a79f8b26ad0e | -15.24475 | -51.74337 | 2025-11-02 04:53:00 | NPP-375D | ARAGUAIANA | MATO GROSSO | Brasil | 5101001 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 0df6a809-cb6a-363a-ac3f-6c07d06de8b7 | -15.24813 | -51.74391 | 2025-11-02 04:53:00 | NPP-375D | ARAGUAIANA | MATO GROSSO | Brasil | 5101001 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 71531ab8-b9b1-3f94-b679-627c90a64d8d | -12.37319 | -63.88021 | 2025-11-02 04:53:00 | NPP-375D | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 258073d3-7074-35bd-802a-351a39a04ebb | -15.11826 | -47.24982 | 2025-11-02 04:53:00 | NPP-375D | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 417d110a-bdf5-39cb-9b29-308c39c557e2 | -14.45123 | -51.52895 | 2025-11-02 04:53:00 | NPP-375D | ARAGUAIANA | MATO GROSSO | Brasil | 5101001 | 51 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 3c3bef05-bc3c-3948-aef9-3d0e78cdcad1 | -18.51597 | -53.49476 | 2025-11-02 04:53:00 | NPP-375D | COSTA RICA | MATO GROSSO DO SUL | Brasil | 5003256 | 50 | 33 | nan | nan | nan | Cerrado | 1.5 |
| b85db6f2-84b3-3923-8fbc-21cc9a958b8f | -12.37259 | -63.88261 | 2025-11-02 04:53:00 | NPP-375D | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 0c996655-20e3-3877-a009-ac2b1558b631 | -13.48977 | -61.44271 | 2025-11-02 04:53:00 | NPP-375D | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 67a500da-c349-3b8a-a422-9fdb8b8317f7 | -12.37772 | -63.88862 | 2025-11-02 04:53:00 | NPP-375D | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 0f359a7b-21d8-3925-b7a9-8bb2a7873489 | -16.86551 | -47.91172 | 2025-11-02 04:53:00 | NPP-375D | LUZIÂNIA | GOIÁS | Brasil | 5212501 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 7fd03927-f11d-32f7-9640-34a9f2750f59 | -15.12952 | -46.23208 | 2025-11-02 04:53:00 | NPP-375D | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 14ddb86c-cb95-3935-bbce-765fe311e4ae | -20.25908 | -50.65512 | 2025-11-02 04:53:00 | NPP-375D | URÂNIA | SÃO PAULO | Brasil | 3555802 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 0087e74c-e5ed-3bfe-8630-783d8c46e0f2 | -18.49796 | -46.95516 | 2025-11-02 04:53:00 | NPP-375D | COROMANDEL | MINAS GERAIS | Brasil | 3119302 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 718bd145-0f08-334e-a7e7-07bb792d39ff | -14.45405 | -51.53319 | 2025-11-02 04:53:00 | NPP-375D | ARAGUAIANA | MATO GROSSO | Brasil | 5101001 | 51 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 0a019566-65c8-354a-a160-5b2bab3de76d | -13.4927 | -61.44269 | 2025-11-02 04:53:00 | NPP-375D | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 327a31a2-f804-3f5f-9d4c-4c7b7754abdc | -13.49242 | -61.45609 | 2025-11-02 04:53:00 | NPP-375D | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 87d732ac-adfb-3fce-a150-51966f558841 | -18.45174 | -51.62813 | 2025-11-02 04:53:00 | NPP-375D | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 8c1114f7-f15b-3d3d-9564-969e5a33de1b | -15.64725 | -53.48084 | 2025-11-02 04:53:00 | NPP-375D | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 6f181b96-e6bf-3a58-b5e1-c45e6645ef8e | -13.97277 | -52.45343 | 2025-11-02 04:53:00 | NPP-375D | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 84e20b5e-2854-3d91-99c7-2043f93e95f4 | -20.47914 | -55.83968 | 2025-11-02 04:53:00 | NPP-375D | ANASTÁCIO | MATO GROSSO DO SUL | Brasil | 5000708 | 50 | 33 | nan | nan | nan | Cerrado | 1.1 |
| a595cf0d-0726-3998-ada4-d004521f5675 | -15.24136 | -51.74282 | 2025-11-02 04:53:00 | NPP-375D | ARAGUAIANA | MATO GROSSO | Brasil | 5101001 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 369aef73-fa5c-3122-a238-ff3fe24a6459 | -17.07826 | -44.4843 | 2025-11-02 04:53:00 | NPP-375D | JEQUITAÍ | MINAS GERAIS | Brasil | 3135605 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 536e5136-f15e-38fd-853b-996070618b22 | -16.85928 | -52.49542 | 2025-11-02 04:53:00 | NPP-375D | DOVERLÂNDIA | GOIÁS | Brasil | 5207253 | 52 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 23a64da8-1347-3a45-91c7-c1cc34083642 | -14.43261 | -51.56002 | 2025-11-02 04:53:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| ddc56f3a-3470-3b17-8474-d1b226664028 | -16.969 | -51.88731 | 2025-11-02 04:53:00 | NPP-375D | CAIAPÔNIA | GOIÁS | Brasil | 5204409 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 342477d8-2771-30ff-97dd-254151e01394 | -16.98636 | -51.46479 | 2025-11-02 04:53:00 | NPP-375D | CAIAPÔNIA | GOIÁS | Brasil | 5204409 | 52 | 33 | nan | nan | nan | Cerrado | 0.5 |
| a973bce0-d8e8-3fbb-82f9-c8f13e5036ec | -18.49685 | -46.96424 | 2025-11-02 04:53:00 | NPP-375D | COROMANDEL | MINAS GERAIS | Brasil | 3119302 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 34895850-de51-385c-b517-807cc0b54861 | -18.47659 | -48.38347 | 2025-11-02 04:53:00 | NPP-375D | ARAGUARI | MINAS GERAIS | Brasil | 3103504 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 2f2e944c-a889-3d40-8c45-f657174d567d | -12.43448 | -63.14052 | 2025-11-02 04:53:00 | NPP-375D | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 17e12e89-63d7-39b3-a4c2-c1710e97e596 | -15.87787 | -54.398 | 2025-11-02 04:53:00 | NPP-375D | POXORÉU | MATO GROSSO | Brasil | 5107008 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 8be3635f-779d-358b-a781-881c38b636d5 | -15.2408 | -51.74653 | 2025-11-02 04:53:00 | NPP-375D | ARAGUAIANA | MATO GROSSO | Brasil | 5101001 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| ec9119d1-a27a-30a5-a161-2d50604a3b85 | -15.62256 | -58.23347 | 2025-11-02 04:53:00 | NPP-375D | SÃO JOSÉ DOS QUATRO MARCOS | MATO GROSSO | Brasil | 5107107 | 51 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 27b3d0e7-1b1d-3cb1-ab9d-a758b195e5ff | -12.37224 | -63.88488 | 2025-11-02 04:53:00 | NPP-375D | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 758f6107-b614-3167-b7fd-6c5c0354b08e | -13.51245 | -57.23952 | 2025-11-02 04:53:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| cfae7e46-bf99-3b01-8095-2ccccd76415c | -3.46415 | -50.22224 | 2025-11-02 05:08:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| b15f528d-8c91-3d81-9f79-f3610de8cd79 | -3.2337 | -50.58455 | 2025-11-02 05:08:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| e1b4ffb8-10ab-37bb-b60f-0e8dd10a52bc | -2.79321 | -50.28664 | 2025-11-02 05:08:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 98e48b1e-a45c-375f-a9a5-a3377faa66b4 | -2.37897 | -47.72073 | 2025-11-02 05:08:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |


[Clique aqui para ver as próximas entradas](README23.md)
