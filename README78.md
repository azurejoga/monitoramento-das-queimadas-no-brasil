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

## Dados Diários - Página 78

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 9fab9c45-46c4-3d36-a881-0cad8f35f877 | -17.26029 | -46.08357 | 2025-09-11 04:25:00 | NPP-375D | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 82c69c20-5d9d-3ae5-81eb-54022d93058e | -18.05356 | -50.72457 | 2025-09-11 04:25:00 | NPP-375D | RIO VERDE | GOIÁS | Brasil | 5218805 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| b0e61af6-753c-346d-8d58-9613baa3d6a5 | -19.23068 | -48.00879 | 2025-09-11 04:25:00 | NPP-375D | UBERLÂNDIA | MINAS GERAIS | Brasil | 3170206 | 31 | 33 | nan | nan | nan | Cerrado | 26.4 |
| 3f2088ce-f7fc-3601-85ab-d364d761fa47 | -22.84291 | -47.46558 | 2025-09-11 04:25:00 | NPP-375D | SANTA BÁRBARA D'OESTE | SÃO PAULO | Brasil | 3545803 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.8 |
| f7d94949-a54c-3a29-a36f-f86674cb6570 | -17.74817 | -44.4967 | 2025-09-11 04:25:00 | NPP-375D | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| e17c683c-ba0b-3c73-a4a5-0aa5c6835158 | -15.87487 | -54.9361 | 2025-09-11 04:25:00 | NPP-375D | DOM AQUINO | MATO GROSSO | Brasil | 5103601 | 51 | 33 | nan | nan | nan | Cerrado | 13.3 |
| 9a78ebe9-fd51-3047-bde0-747a8c7ea945 | -16.58639 | -50.08434 | 2025-09-11 04:25:00 | NPP-375D | TURVÂNIA | GOIÁS | Brasil | 5221502 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| ffce86ae-d757-31d5-b173-291cdc5d71ef | -15.6045 | -52.74762 | 2025-09-11 04:25:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 2df8da52-b78f-3328-9860-1c25a2580d78 | -22.79424 | -45.62184 | 2025-09-11 04:25:00 | NPP-375D | CAMPOS DO JORDÃO | SÃO PAULO | Brasil | 3509700 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| 7fa4985f-c3ab-3f8b-918a-822eed2441e6 | -15.6759 | -47.02735 | 2025-09-11 04:25:00 | NPP-375D | CABECEIRAS | GOIÁS | Brasil | 5204003 | 52 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 6fa389cf-6e49-3b88-b650-5253bd79421a | -17.99028 | -49.37445 | 2025-09-11 04:25:00 | NPP-375D | GOIATUBA | GOIÁS | Brasil | 5209101 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| d8b04ac1-8d37-3592-a1ce-10abc052a237 | -19.97018 | -46.87882 | 2025-09-11 04:25:00 | NPP-375D | TAPIRA | MINAS GERAIS | Brasil | 3168101 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 5f0de363-80a7-3d64-8d9f-a4815d8b1ace | -15.11756 | -52.40489 | 2025-09-11 04:25:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 1acfd640-5a8b-3b1a-9f22-3c339a6dd5a6 | -17.28838 | -46.68089 | 2025-09-11 04:25:00 | NPP-375D | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 67e5bfbc-c273-39b1-b158-5c15bf1222cc | -19.10995 | -43.22162 | 2025-09-11 04:25:00 | NPP-375D | CARMÉSIA | MINAS GERAIS | Brasil | 3113800 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.9 |
| 9c92b58d-75ac-36df-9f54-9cdc65f50746 | -20.91501 | -49.4697 | 2025-09-11 04:25:00 | NPP-375D | BADY BASSITT | SÃO PAULO | Brasil | 3504602 | 35 | 33 | nan | nan | nan | Mata Atlântica | 11.6 |
| 32762348-071e-34b5-b158-f65618b5fa22 | -20.4827 | -49.73269 | 2025-09-11 04:25:00 | NPP-375D | COSMORAMA | SÃO PAULO | Brasil | 3512902 | 35 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 83abd625-8463-3fbc-a3cf-916c217f2d35 | -17.37623 | -52.92793 | 2025-09-11 04:25:00 | NPP-375D | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 2cd755ba-5cbf-3003-9bec-9cef88a2e2c7 | -17.73257 | -44.4529 | 2025-09-11 04:25:00 | NPP-375D | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 2c956bf9-b814-399b-b891-68688be68f76 | -14.89749 | -55.84715 | 2025-09-11 04:25:00 | NPP-375D | CHAPADA DOS GUIMARÃES | MATO GROSSO | Brasil | 5103007 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| de656aad-005a-39ec-b867-62731fd8da4a | -16.17217 | -48.6845 | 2025-09-11 04:25:00 | NPP-375D | ABADIÂNIA | GOIÁS | Brasil | 5200100 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 6605af24-2637-3f01-bee2-12b1d6a87e88 | -18.4075 | -43.48363 | 2025-09-11 04:25:00 | NPP-375D | SERRO | MINAS GERAIS | Brasil | 3167103 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| fc5abc70-86b4-3c7d-a2af-55d9053f5dfd | -14.50417 | -53.93678 | 2025-09-11 04:25:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 2.9 |
| ef677b3a-adb0-33b6-a95e-ebd647e6cae6 | -21.30008 | -45.95777 | 2025-09-11 04:25:00 | NPP-375D | ALFENAS | MINAS GERAIS | Brasil | 3101607 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 7d002ad1-bfd0-35b1-a6a8-dca3b9c174bb | -15.81928 | -52.2253 | 2025-09-11 04:25:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| add3b936-dc35-3048-a9dc-8ae327b06fbd | -20.36316 | -42.19217 | 2025-09-11 04:25:00 | NPP-375D | SANTA MARGARIDA | MINAS GERAIS | Brasil | 3157906 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| bd207ab1-8866-34fc-9b70-21cb35c2125c | -19.95779 | -46.88527 | 2025-09-11 04:25:00 | NPP-375D | TAPIRA | MINAS GERAIS | Brasil | 3168101 | 31 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 18d1e2e3-de25-3a7d-9277-d61439273316 | -17.39121 | -44.9307 | 2025-09-11 04:25:00 | NPP-375D | PIRAPORA | MINAS GERAIS | Brasil | 3151206 | 31 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 62bdbb2b-e574-343b-a78d-3e5a54f31b6c | -18.33171 | -42.82412 | 2025-09-11 04:25:00 | NPP-375D | COLUNA | MINAS GERAIS | Brasil | 3116803 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 0870cf90-5009-351e-bf32-88f5e7596b6d | -20.6997 | -46.07415 | 2025-09-11 04:25:00 | NPP-375D | GUAPÉ | MINAS GERAIS | Brasil | 3128105 | 31 | 33 | nan | nan | nan | Cerrado | 12.8 |
| 31a6f4cc-79ad-3131-8475-6032a815477d | -22.84233 | -47.46941 | 2025-09-11 04:25:00 | NPP-375D | SANTA BÁRBARA D'OESTE | SÃO PAULO | Brasil | 3545803 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.8 |
| 65fadbea-a019-3776-909e-28bd34e70bec | -15.60189 | -52.74422 | 2025-09-11 04:25:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 2c97331f-da80-36eb-9a8a-d50d615e1ab4 | -17.24644 | -46.75998 | 2025-09-11 04:25:00 | NPP-375D | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 17e2164f-8948-3dc1-a9c3-3909cbc1b996 | -20.14385 | -43.66566 | 2025-09-11 04:25:00 | NPP-375D | ITABIRITO | MINAS GERAIS | Brasil | 3131901 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| 74a5e05a-fe30-363a-9822-75a0cb427467 | -18.68216 | -47.66949 | 2025-09-11 04:25:00 | NPP-375D | ESTRELA DO SUL | MINAS GERAIS | Brasil | 3124807 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| ea118c1d-656a-3e5d-99a3-5dfa3218272d | -17.94844 | -44.47528 | 2025-09-11 04:25:00 | NPP-375D | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 9adae6b6-bef2-37fe-bf1a-c4575aed2c1c | -18.34701 | -49.33388 | 2025-09-11 04:25:00 | NPP-375D | ITUMBIARA | GOIÁS | Brasil | 5211503 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 38430a93-bafb-3ab0-abf2-2b9aaa90bf62 | -17.72839 | -44.43092 | 2025-09-11 04:25:00 | NPP-375D | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 4aaa6759-ce9c-36bc-bc62-ff789b1c8ef4 | -15.95969 | -50.22551 | 2025-09-11 04:25:00 | NPP-375D | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 68984f0f-1aab-3bec-b8fc-9acf9d476c18 | -14.89456 | -55.84183 | 2025-09-11 04:25:00 | NPP-375D | CHAPADA DOS GUIMARÃES | MATO GROSSO | Brasil | 5103007 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 49e28339-8a3a-3d5f-8447-4808c944c02b | -19.96605 | -43.81641 | 2025-09-11 04:25:00 | NPP-375D | RAPOSOS | MINAS GERAIS | Brasil | 3153905 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| b2c801d8-ebca-3c72-a415-e49ab85e15e3 | -16.63087 | -49.76026 | 2025-09-11 04:25:00 | NPP-375D | NAZÁRIO | GOIÁS | Brasil | 5214408 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 1c6b4a58-a13b-36dc-b302-a8a41893e9ee | -15.55629 | -54.77505 | 2025-09-11 04:25:00 | NPP-375D | DOM AQUINO | MATO GROSSO | Brasil | 5103601 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| fbc56aaa-101f-3f9e-9895-af402aef2156 | -18.59583 | -43.87614 | 2025-09-11 04:25:00 | NPP-375D | GOUVEIA | MINAS GERAIS | Brasil | 3127602 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 67dd113c-a059-37a8-9814-c00e1ec42906 | -15.15562 | -52.40927 | 2025-09-11 04:25:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 13a05018-2e60-3234-9304-039a4a4ba1db | -16.32664 | -43.75862 | 2025-09-11 04:25:00 | NPP-375D | CAPITÃO ENÉAS | MINAS GERAIS | Brasil | 3112703 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 55f97645-63b3-3cdb-8a81-0705bcd50ce9 | -17.75574 | -44.44346 | 2025-09-11 04:25:00 | NPP-375D | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 9056da22-713e-3761-b70c-59ba373d1467 | -17.32344 | -46.67558 | 2025-09-11 04:25:00 | NPP-375D | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 733ace24-3261-3619-97c2-ed1525a1a2a3 | -17.94165 | -44.48426 | 2025-09-11 04:25:00 | NPP-375D | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 6092505e-8ed4-38b9-91b4-e2bb0bcae773 | -19.98828 | -47.61891 | 2025-09-11 04:25:00 | NPP-375D | CONQUISTA | MINAS GERAIS | Brasil | 3118205 | 31 | 33 | nan | nan | nan | Cerrado | 9.1 |
| cd6de5f9-7d18-326c-a50c-b9c7ad097c2d | -15.67704 | -47.0202 | 2025-09-11 04:25:00 | NPP-375D | CABECEIRAS | GOIÁS | Brasil | 5204003 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| dfb1e61c-7891-309d-a8d1-ab9b3a272783 | -17.26365 | -46.08412 | 2025-09-11 04:25:00 | NPP-375D | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 69282bec-6291-3ca3-8ecb-397c73e6e119 | -22.14483 | -48.63191 | 2025-09-11 04:25:00 | NPP-375D | BOCAINA | SÃO PAULO | Brasil | 3506805 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 89687208-6b7c-3e1d-af76-556051a10ac3 | -19.00879 | -46.25332 | 2025-09-11 04:25:00 | NPP-375D | CARMO DO PARANAÍBA | MINAS GERAIS | Brasil | 3114303 | 31 | 33 | nan | nan | nan | Cerrado | 8.0 |
| 71f00b16-8ae0-3c41-ab64-31bbba2dca75 | -14.93255 | -55.9452 | 2025-09-11 04:25:00 | NPP-375D | CHAPADA DOS GUIMARÃES | MATO GROSSO | Brasil | 5103007 | 51 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 1d955bd8-7074-38ec-82d1-81a220a19ceb | -20.07778 | -44.74746 | 2025-09-11 04:25:00 | NPP-375D | CARMO DO CAJURU | MINAS GERAIS | Brasil | 3114204 | 31 | 33 | nan | nan | nan | Cerrado | 2.8 |
| ddfaea92-fc27-3a58-afca-07c567715b00 | -16.29968 | -50.05948 | 2025-09-11 04:25:00 | NPP-375D | ANICUNS | GOIÁS | Brasil | 5201306 | 52 | 33 | nan | nan | nan | Cerrado | 8.9 |
| d7ab7781-8ff0-39a1-8dab-718afdb37a2b | -19.99596 | -47.63542 | 2025-09-11 04:25:00 | NPP-375D | CONQUISTA | MINAS GERAIS | Brasil | 3118205 | 31 | 33 | nan | nan | nan | Cerrado | 10.0 |
| dc07200f-8598-3143-9139-7c46d54718c9 | -17.8304 | -46.73677 | 2025-09-11 04:25:00 | NPP-375D | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 2.2 |
| e462f679-fb3e-3780-89da-077fb6f68a69 | -15.81579 | -48.95636 | 2025-09-11 04:25:00 | NPP-375D | PIRENÓPOLIS | GOIÁS | Brasil | 5217302 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| c8a13aef-7de6-3f4f-859f-0769c005c9c2 | -21.40206 | -44.15072 | 2025-09-11 04:25:00 | NPP-375D | PIEDADE DO RIO GRANDE | MINAS GERAIS | Brasil | 3150307 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| dabeb58b-63d3-3720-9f60-f35e569321cc | -20.07476 | -44.74266 | 2025-09-11 04:25:00 | NPP-375D | CARMO DO CAJURU | MINAS GERAIS | Brasil | 3114204 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 28b1c90f-51cb-3ac2-bf59-0f566614cd8b | -19.25625 | -48.01295 | 2025-09-11 04:25:00 | NPP-375D | UBERABA | MINAS GERAIS | Brasil | 3170107 | 31 | 33 | nan | nan | nan | Cerrado | 4.8 |
| e67ce293-2e44-3a86-8368-cec54e8862e9 | -14.92179 | -55.83509 | 2025-09-11 04:25:00 | NPP-375D | CHAPADA DOS GUIMARÃES | MATO GROSSO | Brasil | 5103007 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 28dbad01-bc0e-3214-b7d0-a6dc289cd998 | -16.29288 | -45.68617 | 2025-09-11 04:25:00 | NPP-375D | SÃO ROMÃO | MINAS GERAIS | Brasil | 3164209 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| c1752b27-d153-3e42-8fb5-038a8ed8fbea | -15.5953 | -49.38942 | 2025-09-11 04:25:00 | NPP-375D | JARAGUÁ | GOIÁS | Brasil | 5211800 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 810144d7-ca27-3658-9d43-39f55a319f8d | -15.89503 | -48.181 | 2025-09-11 04:25:00 | NPP-375D | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 1.9 |
| a7e120b1-ae8a-3335-b2f7-241c610b7632 | -14.89199 | -55.8742 | 2025-09-11 04:25:00 | NPP-375D | CHAPADA DOS GUIMARÃES | MATO GROSSO | Brasil | 5103007 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| dfaa5693-7661-3a9e-b5e7-1eb2208efa19 | -15.80548 | -52.23122 | 2025-09-11 04:25:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| f63cf533-aac2-3fd6-a796-d8f7d15caa43 | -17.56052 | -44.55548 | 2025-09-11 04:25:00 | NPP-375D | VÁRZEA DA PALMA | MINAS GERAIS | Brasil | 3170800 | 31 | 33 | nan | nan | nan | Cerrado | 5.4 |
| cd4471e0-402b-381a-841d-abcd77e17f05 | -16.61963 | -49.78329 | 2025-09-11 04:25:00 | NPP-375D | NAZÁRIO | GOIÁS | Brasil | 5214408 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| b157f4e3-f9eb-308d-9fa2-17f004de91bd | -15.14118 | -48.61462 | 2025-09-11 04:25:00 | NPP-375D | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 675d1842-c287-3a01-a8ed-0335e60e51c0 | -16.29698 | -50.04722 | 2025-09-11 04:25:00 | NPP-375D | ANICUNS | GOIÁS | Brasil | 5201306 | 52 | 33 | nan | nan | nan | Cerrado | 3.5 |
| fe2b743b-f697-38af-95bb-4767e853e651 | -22.99339 | -43.49945 | 2025-09-11 04:25:00 | NPP-375D | RIO DE JANEIRO | RIO DE JANEIRO | Brasil | 3304557 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| f2afe66e-5c0f-3364-8db0-60909bc8e7e5 | -15.12359 | -50.13011 | 2025-09-11 04:25:00 | NPP-375D | ARAGUAPAZ | GOIÁS | Brasil | 5202155 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| fab0fcbb-ca1d-3f54-8b4d-d851e87c6560 | -15.15838 | -52.41774 | 2025-09-11 04:25:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 4dfcdd40-8b51-32f7-b0c5-22e0bab80896 | -15.11773 | -52.40352 | 2025-09-11 04:25:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 0bf0f3dd-e75e-3f8d-b343-6ea7a572735b | -19.25292 | -48.01236 | 2025-09-11 04:25:00 | NPP-375D | UBERABA | MINAS GERAIS | Brasil | 3170107 | 31 | 33 | nan | nan | nan | Cerrado | 10.0 |
| 015348c2-9403-3dfd-a9aa-5ada3497b387 | -15.79268 | -52.26536 | 2025-09-11 04:25:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 9374e139-3b2b-3aee-bc2c-260f2bc82080 | -15.56918 | -54.7607 | 2025-09-11 04:25:00 | NPP-375D | DOM AQUINO | MATO GROSSO | Brasil | 5103601 | 51 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 6109e2e1-ee41-3d05-8aa4-9aab59911577 | -19.03411 | -42.14784 | 2025-09-11 04:25:00 | NPP-375D | GOVERNADOR VALADARES | MINAS GERAIS | Brasil | 3127701 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| dfe7e345-9b1e-3971-ab97-18518c6c2f7e | -17.56523 | -44.54795 | 2025-09-11 04:25:00 | NPP-375D | VÁRZEA DA PALMA | MINAS GERAIS | Brasil | 3170800 | 31 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 2b42427d-ad30-3479-a80d-66e1d3ac9f24 | -16.06406 | -49.96794 | 2025-09-11 04:25:00 | NPP-375D | ITABERAÍ | GOIÁS | Brasil | 5210406 | 52 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 81e931d8-a6e5-3104-a806-48812e8313b9 | -15.60612 | -52.74509 | 2025-09-11 04:25:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 7bf3d98e-d3a8-3143-b0d4-ba67de29ebff | -19.955 | -46.88102 | 2025-09-11 04:25:00 | NPP-375D | TAPIRA | MINAS GERAIS | Brasil | 3168101 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 29c96d3e-d95e-3349-b2ab-f31596daacbc | -20.09301 | -44.47905 | 2025-09-11 04:25:00 | NPP-375D | ITAÚNA | MINAS GERAIS | Brasil | 3133808 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 81b90ed2-39a9-3b4c-828e-3dcb611f53ac | -16.88201 | -45.75332 | 2025-09-11 04:25:00 | NPP-375D | BRASILÂNDIA DE MINAS | MINAS GERAIS | Brasil | 3108552 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 0770c017-7611-3022-b9f5-74f36a5ecf04 | -15.12727 | -52.42197 | 2025-09-11 04:25:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 67dcbbd0-5c16-3d13-952c-bc17a06034ec | -22.26765 | -46.84037 | 2025-09-11 04:25:00 | NPP-375D | MOGI GUAÇU | SÃO PAULO | Brasil | 3530706 | 35 | 33 | nan | nan | nan | Cerrado | 0.6 |
| a25bb1b1-84b7-389e-9e82-ad07ead12c29 | -14.90848 | -55.87391 | 2025-09-11 04:25:00 | NPP-375D | CHAPADA DOS GUIMARÃES | MATO GROSSO | Brasil | 5103007 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 9cfe0021-f5d6-3f71-9349-ac9b62b6a126 | -17.93525 | -50.54402 | 2025-09-11 04:25:00 | NPP-375D | SANTA HELENA DE GOIÁS | GOIÁS | Brasil | 5219308 | 52 | 33 | nan | nan | nan | Cerrado | 3.7 |
| ed98cdad-90e6-31c7-9500-2c5efffd9835 | -16.5323 | -55.18017 | 2025-09-11 04:25:00 | NPP-375D | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 3.3 |
| 1e1a468e-a881-346d-91bd-93f6ef50a59b | -20.91629 | -49.462 | 2025-09-11 04:25:00 | NPP-375D | BADY BASSITT | SÃO PAULO | Brasil | 3504602 | 35 | 33 | nan | nan | nan | Mata Atlântica | 11.2 |
| a1be2489-efae-3ad8-92c5-ad01d8d0c3f0 | -15.12119 | -52.40814 | 2025-09-11 04:25:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 50ef65eb-fe3a-35b4-a65b-0f25d1cb439a | -19.99885 | -47.617 | 2025-09-11 04:25:00 | NPP-375D | CONQUISTA | MINAS GERAIS | Brasil | 3118205 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| a40d97db-6909-3d18-a6ff-7114e79c577e | -19.18705 | -48.80053 | 2025-09-11 04:25:00 | NPP-375D | PRATA | MINAS GERAIS | Brasil | 3152808 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| e2db4ed9-9873-3cb0-9578-41f2bb76933c | -17.83261 | -46.74463 | 2025-09-11 04:25:00 | NPP-375D | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 16b107d7-6336-3ffc-9015-2194eb8aadb3 | -17.55404 | -44.55028 | 2025-09-11 04:25:00 | NPP-375D | VÁRZEA DA PALMA | MINAS GERAIS | Brasil | 3170800 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 934964b2-56ac-34d8-aee3-1a7b5dd036ce | -20.05888 | -47.51771 | 2025-09-11 04:25:00 | NPP-375D | IGARAPAVA | SÃO PAULO | Brasil | 3520103 | 35 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 5260f599-73fc-35f2-bab7-ae5935d5947e | -20.24331 | -43.57627 | 2025-09-11 04:25:00 | NPP-375D | OURO PRETO | MINAS GERAIS | Brasil | 3146107 | 31 | 33 | nan | nan | nan | Mata Atlântica | 7.9 |


[Clique aqui para ver as próximas entradas](README79.md)
