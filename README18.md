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

## Dados Diários - Página 18

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| beb3d9be-645d-303c-8f22-27fb99738e83 | -13.52817 | -52.94216 | 2026-07-08 04:25:00 | NOAA-20 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 1d79fa41-8bb7-3660-949d-87db9630ae28 | -13.95789 | -45.19714 | 2026-07-08 04:25:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 2cd7f58c-ed25-3233-ab49-fa1a4babb3b3 | -10.94554 | -43.04565 | 2026-07-08 04:25:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 543e4fe2-0156-3bae-a735-319486b42d83 | -13.28515 | -45.18861 | 2026-07-08 04:25:00 | NOAA-20 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| d618437e-e747-3ba9-80d1-cc543332ddd3 | -18.24018 | -54.5956 | 2026-07-08 04:27:00 | NOAA-20 | PEDRO GOMES | MATO GROSSO DO SUL | Brasil | 5006408 | 50 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 6abd42f3-657e-30a1-b498-b384a2c03cf0 | -20.97829 | -48.99774 | 2026-07-08 04:27:00 | NOAA-20 | TABAPUÃ | SÃO PAULO | Brasil | 3552601 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| acc09cbc-a14f-3ef9-b63b-4c38a126a6d2 | -20.66973 | -48.78644 | 2026-07-08 04:27:00 | NOAA-20 | BARRETOS | SÃO PAULO | Brasil | 3505500 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.2 |
| b5881330-7527-3711-962d-841076b824a3 | -16.4803 | -50.90826 | 2026-07-08 04:27:00 | NOAA-20 | MOIPORÁ | GOIÁS | Brasil | 5213400 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 5791dca4-bc33-320f-8cb0-545364b554d6 | -20.93734 | -44.08582 | 2026-07-08 04:27:00 | NOAA-20 | LAGOA DOURADA | MINAS GERAIS | Brasil | 3137403 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| a1e288f4-ab08-3105-963f-8ca20698a3e1 | -20.96351 | -48.6488 | 2026-07-08 04:27:00 | NOAA-20 | MONTE AZUL PAULISTA | SÃO PAULO | Brasil | 3531506 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 534053bc-af15-36b2-9f7b-a47557cda4bf | -18.74347 | -46.91592 | 2026-07-08 04:27:00 | NOAA-20 | PATROCÍNIO | MINAS GERAIS | Brasil | 3148103 | 31 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 6c460434-97b1-31fd-adb5-d1d2b7cafe78 | -20.96078 | -48.6445 | 2026-07-08 04:27:00 | NOAA-20 | MONTE AZUL PAULISTA | SÃO PAULO | Brasil | 3531506 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| 76921c3c-7296-3e26-b39e-4c5093e17371 | -21.77588 | -56.29251 | 2026-07-08 04:27:00 | NOAA-20 | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 32e69d02-4e61-319c-97d4-8d2c6c6d3837 | -21.79873 | -56.27612 | 2026-07-08 04:27:00 | NOAA-20 | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 7.3 |
| 37ee9fc9-e3df-398b-9e4b-50e3db829cac | -19.09272 | -40.08797 | 2026-07-08 04:27:00 | NOAA-20 | SOORETAMA | ESPÍRITO SANTO | Brasil | 3205010 | 32 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 51e34090-9d9e-34b6-a0b0-34d98509ce89 | -19.83273 | -44.63698 | 2026-07-08 04:27:00 | NOAA-20 | PARÁ DE MINAS | MINAS GERAIS | Brasil | 3147105 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| a914c13b-f287-39a8-96c8-20f0931f5e81 | -18.07815 | -54.02836 | 2026-07-08 04:27:00 | NOAA-20 | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 22b4a71f-87b0-3c9e-9761-84b53ddb4508 | -19.63312 | -47.59101 | 2026-07-08 04:27:00 | NOAA-20 | UBERABA | MINAS GERAIS | Brasil | 3170107 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 3f3f242c-91fd-303f-9ded-4d4746b3e7b2 | -21.41705 | -47.06316 | 2026-07-08 04:27:00 | NOAA-20 | MOCOCA | SÃO PAULO | Brasil | 3530508 | 35 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 448751d0-4859-394f-a72e-c37be1a27de8 | -21.7957 | -56.27786 | 2026-07-08 04:27:00 | NOAA-20 | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 1.7 |
| f86304b9-ce3c-3c4f-a5fc-42cfc43adc3c | -19.85464 | -49.07276 | 2026-07-08 04:27:00 | NOAA-20 | FRUTAL | MINAS GERAIS | Brasil | 3127107 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 47cb0e70-e1b2-3788-b303-4072006969a2 | -16.65773 | -47.52553 | 2026-07-08 04:27:00 | NOAA-20 | CRISTALINA | GOIÁS | Brasil | 5206206 | 52 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 17fb31c0-110d-365a-a0c7-7db3fbfdc0c8 | -21.06304 | -47.25285 | 2026-07-08 04:27:00 | NOAA-20 | ALTINÓPOLIS | SÃO PAULO | Brasil | 3501004 | 35 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 84972d21-1400-3bb4-8871-645eb8dd564a | -21.80696 | -52.71616 | 2026-07-08 04:27:00 | NOAA-20 | BATAGUASSU | MATO GROSSO DO SUL | Brasil | 5001904 | 50 | 33 | nan | nan | nan | Cerrado | 1.8 |
| abeac7e0-2740-3166-a14e-0c9b5d541737 | -22.29042 | -46.85891 | 2026-07-08 04:27:00 | NOAA-20 | MOGI GUAÇU | SÃO PAULO | Brasil | 3530706 | 35 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 2b76a615-8d23-3e44-aef5-213990e98725 | -21.3665 | -49.16452 | 2026-07-08 04:27:00 | NOAA-20 | ITAJOBI | SÃO PAULO | Brasil | 3521903 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.3 |
| 099ddc77-d498-3d66-9821-84b9eb629580 | -20.93357 | -44.08533 | 2026-07-08 04:27:00 | NOAA-20 | LAGOA DOURADA | MINAS GERAIS | Brasil | 3137403 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| e3ca4639-4d52-36f6-a12b-a46d1a6e562f | -17.11172 | -49.98539 | 2026-07-08 04:27:00 | NOAA-20 | INDIARA | GOIÁS | Brasil | 5209952 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 35cad080-ba15-3537-8cbf-0e773537947e | -17.51434 | -45.36571 | 2026-07-08 04:27:00 | NOAA-20 | BURITIZEIRO | MINAS GERAIS | Brasil | 3109402 | 31 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 976bb875-c6e3-37b4-8add-64ffcc6c0e9c | -20.75 | -48.06988 | 2026-07-08 04:27:00 | NOAA-20 | MORRO AGUDO | SÃO PAULO | Brasil | 3531902 | 35 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 694f4e49-4bf1-3123-a06b-9ba1e96155a8 | -20.93729 | -44.08786 | 2026-07-08 04:27:00 | NOAA-20 | LAGOA DOURADA | MINAS GERAIS | Brasil | 3137403 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 76286825-ffe5-325c-829a-1b800d7a9342 | -19.08858 | -40.0821 | 2026-07-08 04:27:00 | NOAA-20 | SOORETAMA | ESPÍRITO SANTO | Brasil | 3205010 | 32 | 33 | nan | nan | nan | Mata Atlântica | 2.4 |
| 21c8a3aa-9605-3799-b5c9-3ef6e2af9457 | -16.4811 | -50.90367 | 2026-07-08 04:27:00 | NOAA-20 | MOIPORÁ | GOIÁS | Brasil | 5213400 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| a85686f0-ae40-3a08-8499-23d3517195bd | -18.08248 | -54.02926 | 2026-07-08 04:27:00 | NOAA-20 | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 746a11d4-7569-3853-ada8-a033f41609d4 | -21.41984 | -47.06753 | 2026-07-08 04:27:00 | NOAA-20 | MOCOCA | SÃO PAULO | Brasil | 3530508 | 35 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 3f4b6358-2489-3ec8-ae27-a513cb74063d | -17.28046 | -50.01579 | 2026-07-08 04:27:00 | NOAA-20 | INDIARA | GOIÁS | Brasil | 5209952 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 1646a1c6-820d-3d70-a390-3bb3c8b325ce | -21.06248 | -47.25658 | 2026-07-08 04:27:00 | NOAA-20 | ALTINÓPOLIS | SÃO PAULO | Brasil | 3501004 | 35 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 464f43fd-f85d-319f-b94d-414e6f44c696 | -17.54187 | -54.0078 | 2026-07-08 04:27:00 | NOAA-20 | SONORA | MATO GROSSO DO SUL | Brasil | 5007935 | 50 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 54dcf23c-72da-3e00-ba09-52b83073c9f3 | -21.37044 | -49.16142 | 2026-07-08 04:27:00 | NOAA-20 | ITAJOBI | SÃO PAULO | Brasil | 3521903 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 890ce278-6a93-3e1c-ac8e-7f6f198874de | -17.53577 | -54.01606 | 2026-07-08 04:27:00 | NOAA-20 | SONORA | MATO GROSSO DO SUL | Brasil | 5007935 | 50 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 0460d03b-9da3-351d-9913-b4dc48c8ba7c | -21.36711 | -49.16079 | 2026-07-08 04:27:00 | NOAA-20 | ITAJOBI | SÃO PAULO | Brasil | 3521903 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| c8b8e233-f198-3416-b72f-a93740f49dbc | -21.41426 | -47.05879 | 2026-07-08 04:27:00 | NOAA-20 | MOCOCA | SÃO PAULO | Brasil | 3530508 | 35 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 2221d049-9d6b-318d-afd3-565812b966e5 | -21.27092 | -49.16213 | 2026-07-08 04:27:00 | NOAA-20 | MARAPOAMA | SÃO PAULO | Brasil | 3528858 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| b73f61fc-662e-3a35-9c9a-eaa832d1d8d5 | -17.53663 | -54.01151 | 2026-07-08 04:27:00 | NOAA-20 | SONORA | MATO GROSSO DO SUL | Brasil | 5007935 | 50 | 33 | nan | nan | nan | Cerrado | 4.8 |
| cdca4364-2d63-318f-addf-e29e33814afa | -18.08331 | -54.0249 | 2026-07-08 04:27:00 | NOAA-20 | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 1fce18b9-4345-3817-8581-4fb447f054b6 | -21.42933 | -47.07306 | 2026-07-08 04:27:00 | NOAA-20 | MOCOCA | SÃO PAULO | Brasil | 3530508 | 35 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 36368b4f-8720-3fbb-a501-4ceaed773063 | -17.27977 | -50.01983 | 2026-07-08 04:27:00 | NOAA-20 | INDIARA | GOIÁS | Brasil | 5209952 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 6e65fb82-fdf5-369e-be7a-526da50150b5 | -17.51377 | -45.36959 | 2026-07-08 04:27:00 | NOAA-20 | BURITIZEIRO | MINAS GERAIS | Brasil | 3109402 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 558cce76-75fa-3670-99a7-b1df197ff39a | -22.28985 | -46.8628 | 2026-07-08 04:27:00 | NOAA-20 | MOGI GUAÇU | SÃO PAULO | Brasil | 3530706 | 35 | 33 | nan | nan | nan | Cerrado | 1.5 |
| fa2f5d56-a586-3128-b2f2-e219104fd5ed | -21.79411 | -56.27489 | 2026-07-08 04:27:00 | NOAA-20 | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 7.3 |
| 4ec31cd6-6d7b-3ce1-82b1-58544454f9f6 | -21.8116 | -52.71214 | 2026-07-08 04:27:00 | NOAA-20 | BATAGUASSU | MATO GROSSO DO SUL | Brasil | 5001904 | 50 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 33fc304e-2e50-3a8b-b40a-4e4afaf7f07c | -21.4254 | -47.07631 | 2026-07-08 04:27:00 | NOAA-20 | MOCOCA | SÃO PAULO | Brasil | 3530508 | 35 | 33 | nan | nan | nan | Cerrado | 0.6 |
| f4e5af69-422a-33c8-8b61-60cacde85923 | -17.27557 | -50.02328 | 2026-07-08 04:27:00 | NOAA-20 | INDIARA | GOIÁS | Brasil | 5209952 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 3e75a311-dc88-3250-91e2-240841ed68a8 | -19.61715 | -47.58448 | 2026-07-08 04:27:00 | NOAA-20 | SACRAMENTO | MINAS GERAIS | Brasil | 3156908 | 31 | 33 | nan | nan | nan | Cerrado | 0.4 |
| be7386c7-e35e-32c3-bcd1-d10670b38817 | -21.36257 | -49.16762 | 2026-07-08 04:27:00 | NOAA-20 | ITAJOBI | SÃO PAULO | Brasil | 3521903 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.3 |
| 050f4984-fa21-347a-9e1f-8c0618ed28a6 | -19.44067 | -54.66461 | 2026-07-08 04:27:00 | NOAA-20 | SÃO GABRIEL DO OESTE | MATO GROSSO DO SUL | Brasil | 5007695 | 50 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 2bba3106-00ac-3315-8d99-dd60acb00082 | -21.80089 | -56.2655 | 2026-07-08 04:27:00 | NOAA-20 | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 4a96070b-6fda-3653-afd8-a589a1c742e0 | -20.10879 | -53.34077 | 2026-07-08 04:27:00 | NOAA-20 | RIBAS DO RIO PARDO | MATO GROSSO DO SUL | Brasil | 5007109 | 50 | 33 | nan | nan | nan | Cerrado | 0.8 |
| c7fc685e-8726-33ff-9709-129329b64b0a | -21.42205 | -47.07572 | 2026-07-08 04:27:00 | NOAA-20 | MOCOCA | SÃO PAULO | Brasil | 3530508 | 35 | 33 | nan | nan | nan | Cerrado | 0.5 |
| f95b80f8-50a9-3835-960b-f7e50669037d | -20.39405 | -41.59341 | 2026-07-08 04:27:00 | NOAA-20 | IÚNA | ESPÍRITO SANTO | Brasil | 3203007 | 32 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| e4c79255-c5de-3ee0-b8ef-aee634252f3f | -17.53751 | -54.00688 | 2026-07-08 04:27:00 | NOAA-20 | SONORA | MATO GROSSO DO SUL | Brasil | 5007935 | 50 | 33 | nan | nan | nan | Cerrado | 4.8 |
| ae396e3e-dd26-3351-beaa-959c58c0e0f5 | -21.0597 | -47.25231 | 2026-07-08 04:27:00 | NOAA-20 | ALTINÓPOLIS | SÃO PAULO | Brasil | 3501004 | 35 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 30c86973-bc4b-39a2-878a-4e371594da34 | -21.69981 | -45.89433 | 2026-07-08 04:27:00 | NOAA-20 | MACHADO | MINAS GERAIS | Brasil | 3139003 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 13e8f0c7-0e7b-3ba6-9a33-84eae4a479fb | -21.03836 | -46.78733 | 2026-07-08 04:27:00 | NOAA-20 | JACUÍ | MINAS GERAIS | Brasil | 3134806 | 31 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 013158ff-5c55-3977-b5fa-49f82d6dc8b3 | -22.28646 | -46.86221 | 2026-07-08 04:27:00 | NOAA-20 | MOGI GUAÇU | SÃO PAULO | Brasil | 3530706 | 35 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 5fb97f7c-8741-3765-a571-e8d616a225fb | -21.42991 | -47.06925 | 2026-07-08 04:27:00 | NOAA-20 | MOCOCA | SÃO PAULO | Brasil | 3530508 | 35 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 5f56a939-bc7e-32be-92cf-58f715b4c82d | -20.39766 | -41.59277 | 2026-07-08 04:27:00 | NOAA-20 | IÚNA | ESPÍRITO SANTO | Brasil | 3203007 | 32 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| f5848d37-8dea-3062-8a27-a6e1c6fc3815 | -20.10809 | -53.34444 | 2026-07-08 04:27:00 | NOAA-20 | RIBAS DO RIO PARDO | MATO GROSSO DO SUL | Brasil | 5007109 | 50 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 3e576a4b-b9d8-3e30-92c4-205206d73ae0 | -21.3659 | -49.16824 | 2026-07-08 04:27:00 | NOAA-20 | ITAJOBI | SÃO PAULO | Brasil | 3521903 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.3 |
| 04ad40b3-20ea-37dc-86ed-d7cbb3af7c65 | -20.74633 | -45.5745 | 2026-07-08 04:27:00 | NOAA-20 | CRISTAIS | MINAS GERAIS | Brasil | 3120201 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| fc12b1df-f347-3a30-9d5c-4eb877d0e769 | -20.10988 | -44.43867 | 2026-07-08 04:27:00 | NOAA-20 | MATEUS LEME | MINAS GERAIS | Brasil | 3140704 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 64329034-1fa0-3392-bd69-cbace0bd7d61 | -20.93351 | -44.08738 | 2026-07-08 04:27:00 | NOAA-20 | LAGOA DOURADA | MINAS GERAIS | Brasil | 3137403 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| c6e7db86-bc61-3547-94bc-37510ebba3b3 | -21.79907 | -56.26194 | 2026-07-08 04:27:00 | NOAA-20 | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 2b87c3a5-7260-3218-906b-628fa40297c5 | -21.81071 | -52.71698 | 2026-07-08 04:27:00 | NOAA-20 | BATAGUASSU | MATO GROSSO DO SUL | Brasil | 5001904 | 50 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 6eb5a31c-0df1-3c03-a0f8-53a1a3fb18b0 | -19.85131 | -49.07214 | 2026-07-08 04:27:00 | NOAA-20 | FRUTAL | MINAS GERAIS | Brasil | 3127107 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 62c804df-8820-3380-af13-a78a215aefea | -21.16004 | -48.58829 | 2026-07-08 04:27:00 | NOAA-20 | VISTA ALEGRE DO ALTO | SÃO PAULO | Brasil | 3556909 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| db521b60-9a0e-3c81-9446-7302ecad99c7 | -19.61658 | -47.58813 | 2026-07-08 04:27:00 | NOAA-20 | SACRAMENTO | MINAS GERAIS | Brasil | 3156908 | 31 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 5dcdb386-be6a-366f-a9ab-c2b6fc696c1a | -18.74015 | -46.91537 | 2026-07-08 04:27:00 | NOAA-20 | PATROCÍNIO | MINAS GERAIS | Brasil | 3148103 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 916adbe3-be40-31a9-adc1-06cdb1d2000e | -17.27908 | -50.02391 | 2026-07-08 04:27:00 | NOAA-20 | INDIARA | GOIÁS | Brasil | 5209952 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| f9d72d1a-2294-3de1-bfc2-d288f2d53424 | -21.79629 | -56.26421 | 2026-07-08 04:27:00 | NOAA-20 | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 62c5cc80-95a2-3dcb-b22c-b4a4dd599725 | -19.63153 | -47.57947 | 2026-07-08 04:27:00 | NOAA-20 | SACRAMENTO | MINAS GERAIS | Brasil | 3156908 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 6e001ff0-b343-386d-917a-65fd861ee05a | -19.62982 | -47.59043 | 2026-07-08 04:27:00 | NOAA-20 | UBERABA | MINAS GERAIS | Brasil | 3170107 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| db30da8c-05fb-3841-8fbc-0c577f1e3b23 | -16.71425 | -50.70757 | 2026-07-08 04:27:00 | NOAA-20 | CACHOEIRA DE GOIÁS | GOIÁS | Brasil | 5204201 | 52 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 25c69fed-dfcb-3eee-9d65-ea38d187009f | -19.78814 | -47.57616 | 2026-07-08 04:27:00 | NOAA-20 | CONQUISTA | MINAS GERAIS | Brasil | 3118205 | 31 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 66b49640-7872-35b1-b71a-3f0e02d8522c | -19.79145 | -47.57673 | 2026-07-08 04:27:00 | NOAA-20 | CONQUISTA | MINAS GERAIS | Brasil | 3118205 | 31 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 238cfc4e-ac6f-3276-ab47-6d6badef308f | -18.51988 | -47.24186 | 2026-07-08 04:27:00 | NOAA-20 | COROMANDEL | MINAS GERAIS | Brasil | 3119302 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 7da2d0af-b709-3ab3-9aec-d2a270cc3467 | -21.80256 | -56.26846 | 2026-07-08 04:27:00 | NOAA-20 | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 8.8 |
| a53d72b5-7fd1-3604-8c11-5d635810ae0e | -21.42041 | -47.06374 | 2026-07-08 04:27:00 | NOAA-20 | MOCOCA | SÃO PAULO | Brasil | 3530508 | 35 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 073e9554-63da-330f-a7cb-ebe1d3b1bd20 | -19.63484 | -47.58004 | 2026-07-08 04:27:00 | NOAA-20 | SACRAMENTO | MINAS GERAIS | Brasil | 3156908 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| a131dbd8-0520-3356-89ec-125fdad0339c | -16.66046 | -47.52969 | 2026-07-08 04:27:00 | NOAA-20 | CRISTALINA | GOIÁS | Brasil | 5206206 | 52 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 1ac9f61f-4067-3236-ad52-3d5906be8139 | -19.62103 | -47.58139 | 2026-07-08 04:27:00 | NOAA-20 | SACRAMENTO | MINAS GERAIS | Brasil | 3156908 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 2079868b-a7eb-3fb6-9510-aee256439d26 | -21.79982 | -56.27075 | 2026-07-08 04:27:00 | NOAA-20 | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 7.3 |
| a72bc7a0-2fe7-3a9a-8405-bd2d358ba6b7 | -19.63701 | -47.58793 | 2026-07-08 04:27:00 | NOAA-20 | SACRAMENTO | MINAS GERAIS | Brasil | 3156908 | 31 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 57a56c18-adc0-3576-97d8-ece84145d934 | -20.92974 | -44.08688 | 2026-07-08 04:27:00 | NOAA-20 | LAGOA DOURADA | MINAS GERAIS | Brasil | 3137403 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| a99383f6-fd45-3e53-8079-c3b9a5690e08 | -21.79521 | -56.26948 | 2026-07-08 04:27:00 | NOAA-20 | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 7.3 |
| 844e6cbf-2979-33f4-b30c-747bafa3154e | -17.541 | -54.01242 | 2026-07-08 04:27:00 | NOAA-20 | SONORA | MATO GROSSO DO SUL | Brasil | 5007935 | 50 | 33 | nan | nan | nan | Cerrado | 1.6 |
| daf21b59-2acf-3914-9358-23b44499218c | -21.79796 | -56.26717 | 2026-07-08 04:27:00 | NOAA-20 | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 8.8 |
| 515a3b66-98e3-3eaa-9d05-eb8a5c1921dd | -21.15585 | -50.18385 | 2026-07-08 04:27:00 | NOAA-20 | BREJO ALEGRE | SÃO PAULO | Brasil | 3507753 | 35 | 33 | nan | nan | nan | Mata Atlântica | 5.9 |
| f900a98b-c2b7-34c6-8add-1fd0f4ced3c9 | -16.73766 | -49.42552 | 2026-07-08 04:27:00 | NOAA-20 | ABADIA DE GOIÁS | GOIÁS | Brasil | 5200050 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 6dd93fa1-b0e2-3712-b637-e4e08ab8b1cc | -18.23925 | -54.6003 | 2026-07-08 04:27:00 | NOAA-20 | COXIM | MATO GROSSO DO SUL | Brasil | 5003306 | 50 | 33 | nan | nan | nan | Cerrado | 2.4 |


[Clique aqui para ver as próximas entradas](README19.md)
