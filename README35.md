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

## Dados Diários - Página 35

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 801da1e2-3b37-3107-b9f4-77e8b3c0d14e | -22.27749 | -48.66133 | 2024-09-29 04:06:00 | NOAA-21 | ITAPUÍ | SÃO PAULO | Brasil | 3522901 | 35 | 33 | nan | nan | nan | Mata Atlântica | 17.9 |
| 83927698-0ad9-35fe-b1e6-585c3c09d406 | -22.27446 | -48.65765 | 2024-09-29 04:06:00 | NOAA-21 | ITAPUÍ | SÃO PAULO | Brasil | 3522901 | 35 | 33 | nan | nan | nan | Mata Atlântica | 15.2 |
| 55779d06-7dac-3942-966f-942b94628f8d | -22.2736 | -48.66042 | 2024-09-29 04:06:00 | NOAA-21 | ITAPUÍ | SÃO PAULO | Brasil | 3522901 | 35 | 33 | nan | nan | nan | Mata Atlântica | 17.9 |
| d617a1c5-ed9a-3238-93e0-8553a79ccbcd | -22.27346 | -48.66306 | 2024-09-29 04:06:00 | NOAA-21 | ITAPUÍ | SÃO PAULO | Brasil | 3522901 | 35 | 33 | nan | nan | nan | Mata Atlântica | 15.2 |
| f90a0fbd-58b5-30e8-a86a-41c337a62e70 | -21.64281 | -49.75221 | 2024-09-29 04:06:00 | NOAA-21 | LINS | SÃO PAULO | Brasil | 3527108 | 35 | 33 | nan | nan | nan | Mata Atlântica | 6.3 |
| 78da74ff-216c-345b-904d-d51a9d3654f5 | -21.64199 | -49.75632 | 2024-09-29 04:06:00 | NOAA-21 | LINS | SÃO PAULO | Brasil | 3527108 | 35 | 33 | nan | nan | nan | Mata Atlântica | 6.3 |
| ea88ac45-9e8e-3bea-838e-34f868f90282 | -21.63421 | -49.6856 | 2024-09-29 04:06:00 | NOAA-21 | LINS | SÃO PAULO | Brasil | 3527108 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| e44e2851-da23-3ca6-944a-773792eb2ecf | -21.15925 | -48.91101 | 2024-09-29 04:06:00 | NOAA-21 | PINDORAMA | SÃO PAULO | Brasil | 3538105 | 35 | 33 | nan | nan | nan | Mata Atlântica | 50.4 |
| 4bd80a0a-3893-3ca2-a4b1-df180a6f555e | -21.15595 | -48.90631 | 2024-09-29 04:06:00 | NOAA-21 | PINDORAMA | SÃO PAULO | Brasil | 3538105 | 35 | 33 | nan | nan | nan | Mata Atlântica | 50.4 |
| 05456b8d-c520-3eac-ad42-feed43ed3bac | -21.15522 | -48.91012 | 2024-09-29 04:06:00 | NOAA-21 | PINDORAMA | SÃO PAULO | Brasil | 3538105 | 35 | 33 | nan | nan | nan | Mata Atlântica | 50.4 |
| 5155c26b-e7fb-37d0-aab0-bf4aaa3a6de4 | -21.15449 | -48.91388 | 2024-09-29 04:06:00 | NOAA-21 | PINDORAMA | SÃO PAULO | Brasil | 3538105 | 35 | 33 | nan | nan | nan | Mata Atlântica | 20.2 |
| 08e7a188-d97f-3cb9-bb85-754135392aac | -21.15119 | -48.90921 | 2024-09-29 04:06:00 | NOAA-21 | PINDORAMA | SÃO PAULO | Brasil | 3538105 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 4ec66584-601e-3deb-93eb-2bf7f3dfe069 | -21.09588 | -49.13614 | 2024-09-29 04:06:00 | NOAA-21 | IBIRÁ | SÃO PAULO | Brasil | 3519402 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 4a957d02-3300-338a-aec2-f537fddae477 | -21.09448 | -49.13524 | 2024-09-29 04:06:00 | NOAA-21 | IBIRÁ | SÃO PAULO | Brasil | 3519402 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| f2a8af9f-7476-38a9-b729-50e13e7aa1a4 | -21.09182 | -49.13511 | 2024-09-29 04:06:00 | NOAA-21 | IBIRÁ | SÃO PAULO | Brasil | 3519402 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 56da8ddc-4406-342b-bd99-06b536351a08 | -23.37539 | -50.22877 | 2024-09-29 04:06:00 | NOAA-21 | JUNDIAÍ DO SUL | PARANÁ | Brasil | 4112900 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 5ab82ace-154e-3638-8d02-0b92639ca13d | -23.37202 | -50.22361 | 2024-09-29 04:06:00 | NOAA-21 | SANTO ANTÔNIO DA PLATINA | PARANÁ | Brasil | 4124103 | 41 | 33 | nan | nan | nan | Mata Atlântica | 3.3 |
| 6bf056d3-5e65-3f39-a718-cacf978bf899 | -23.37121 | -50.22771 | 2024-09-29 04:06:00 | NOAA-21 | JUNDIAÍ DO SUL | PARANÁ | Brasil | 4112900 | 41 | 33 | nan | nan | nan | Mata Atlântica | 3.3 |
| 759303af-b6d1-3f8d-9aff-a69d8c7edfb9 | -23.37035 | -50.23212 | 2024-09-29 04:06:00 | NOAA-21 | JUNDIAÍ DO SUL | PARANÁ | Brasil | 4112900 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| aac37729-b9f7-3117-9559-aeec630eae7d | -22.54122 | -48.81131 | 2024-09-29 04:06:00 | NOAA-21 | MACATUBA | SÃO PAULO | Brasil | 3528007 | 35 | 33 | nan | nan | nan | Cerrado | 1.6 |
| c63d9ab0-858a-37cd-a09e-ceace58adac0 | -19.08097 | -50.8799 | 2024-09-29 04:06:00 | NOAA-21 | ITARUMÃ | GOIÁS | Brasil | 5211305 | 52 | 33 | nan | nan | nan | Cerrado | 4.2 |
| ae62f8f8-d615-3ece-a9fa-9a2f3921e518 | -19.07727 | -50.87365 | 2024-09-29 04:06:00 | NOAA-21 | ITARUMÃ | GOIÁS | Brasil | 5211305 | 52 | 33 | nan | nan | nan | Cerrado | 103.8 |
| c9a53a94-a271-395d-97b2-886838a48e90 | -19.0762 | -50.87895 | 2024-09-29 04:06:00 | NOAA-21 | ITARUMÃ | GOIÁS | Brasil | 5211305 | 52 | 33 | nan | nan | nan | Cerrado | 103.8 |
| ff6e49c1-e27f-32c9-9387-1db071685ff5 | -19.07513 | -50.88427 | 2024-09-29 04:06:00 | NOAA-21 | ITARUMÃ | GOIÁS | Brasil | 5211305 | 52 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 55503a60-094e-38b5-ab88-a8ba7e68aedf | -19.07357 | -50.86737 | 2024-09-29 04:06:00 | NOAA-21 | ITARUMÃ | GOIÁS | Brasil | 5211305 | 52 | 33 | nan | nan | nan | Cerrado | 13.8 |
| 071f0932-3677-356e-8ff1-545a50e4dce5 | -19.07251 | -50.87266 | 2024-09-29 04:06:00 | NOAA-21 | ITARUMÃ | GOIÁS | Brasil | 5211305 | 52 | 33 | nan | nan | nan | Cerrado | 103.8 |
| a475c52d-566b-32f3-9a19-5dee025730bd | -19.07144 | -50.87799 | 2024-09-29 04:06:00 | NOAA-21 | ITARUMÃ | GOIÁS | Brasil | 5211305 | 52 | 33 | nan | nan | nan | Cerrado | 103.8 |
| befbcc8c-1022-3ea5-aae9-fbc6f2149eee | -19.07036 | -50.88336 | 2024-09-29 04:06:00 | NOAA-21 | ITARUMÃ | GOIÁS | Brasil | 5211305 | 52 | 33 | nan | nan | nan | Cerrado | 3.3 |
| a4b4eeb8-e6ab-3a8d-a930-9c34ee792c8d | -19.06926 | -50.8888 | 2024-09-29 04:06:00 | NOAA-21 | ITARUMÃ | GOIÁS | Brasil | 5211305 | 52 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 1fd162be-448a-3895-b5d4-1564f59fee72 | -19.06775 | -50.8717 | 2024-09-29 04:06:00 | NOAA-21 | ITARUMÃ | GOIÁS | Brasil | 5211305 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 65f4db8d-891b-32d6-972f-e437c7509f41 | -19.06667 | -50.87706 | 2024-09-29 04:06:00 | NOAA-21 | ITARUMÃ | GOIÁS | Brasil | 5211305 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 9a3a09da-d0d7-39fb-821a-36484021750d | -19.06558 | -50.88247 | 2024-09-29 04:06:00 | NOAA-21 | ITARUMÃ | GOIÁS | Brasil | 5211305 | 52 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 04836224-794f-3d0f-a886-bd270d87f1c9 | -19.06298 | -50.87077 | 2024-09-29 04:06:00 | NOAA-21 | ITARUMÃ | GOIÁS | Brasil | 5211305 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| bd4c4c7e-4741-3663-a999-2b44784914e2 | -19.0619 | -50.87614 | 2024-09-29 04:06:00 | NOAA-21 | ITARUMÃ | GOIÁS | Brasil | 5211305 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| f04fda7c-c656-35a7-b89f-a6d4d235bf29 | -19.05821 | -50.86984 | 2024-09-29 04:06:00 | NOAA-21 | ITARUMÃ | GOIÁS | Brasil | 5211305 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 7f718af8-779a-3b06-81bc-bd22115f2c15 | -19.57293 | -49.74841 | 2024-09-29 04:06:00 | NOAA-21 | CAMPINA VERDE | MINAS GERAIS | Brasil | 3111101 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.3 |
| 1b9f9e63-1bf6-37cc-8747-6e12ddaef13c | -19.57205 | -49.7528 | 2024-09-29 04:06:00 | NOAA-21 | CAMPINA VERDE | MINAS GERAIS | Brasil | 3111101 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.3 |
| c6e7d86c-ac47-313b-a090-fe65c0f7b33f | -20.71947 | -50.62266 | 2024-09-29 04:06:00 | NOAA-21 | AURIFLAMA | SÃO PAULO | Brasil | 3504206 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.3 |
| d0c2b6e0-6880-34f0-a250-a6f886fde077 | -20.7185 | -50.62744 | 2024-09-29 04:06:00 | NOAA-21 | AURIFLAMA | SÃO PAULO | Brasil | 3504206 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| 33846cd3-bace-3583-a0e0-eca9d06ff8b6 | -21.26651 | -50.31018 | 2024-09-29 04:06:00 | NOAA-21 | BIRIGUI | SÃO PAULO | Brasil | 3506508 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 1b0afa74-36bc-3f7b-b3b1-ad7a3ac4aba4 | -23.39237 | -51.12457 | 2024-09-29 04:06:00 | NOAA-21 | LONDRINA | PARANÁ | Brasil | 4113700 | 41 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 6da91abf-2530-31be-99af-34650b283541 | -22.42667 | -51.373 | 2024-09-29 04:06:00 | NOAA-21 | TACIBA | SÃO PAULO | Brasil | 3552908 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.4 |
| 640e324b-86ed-3ff2-a988-d4e8404cc0f5 | -24.24201 | -50.74038 | 2024-09-29 04:06:00 | NOAA-21 | ORTIGUEIRA | PARANÁ | Brasil | 4117305 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| 3f0fc426-e8ad-3a91-8544-e1e65b8a954c | -18.84155 | -54.5033 | 2024-09-29 04:06:00 | NOAA-21 | SÃO GABRIEL DO OESTE | MATO GROSSO DO SUL | Brasil | 5007695 | 50 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 0f90bebb-7cab-31b5-b8d7-c0b71b49835c | -18.8404 | -54.50843 | 2024-09-29 04:06:00 | NOAA-21 | SÃO GABRIEL DO OESTE | MATO GROSSO DO SUL | Brasil | 5007695 | 50 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 53205867-3b70-3f98-b680-a9227ae57524 | -22.17078 | -56.03763 | 2024-09-29 04:06:00 | NOAA-21 | ANTÔNIO JOÃO | MATO GROSSO DO SUL | Brasil | 5000906 | 50 | 33 | nan | nan | nan | Cerrado | 13.1 |
| 29828662-f3d9-311f-9278-71166cdffbc8 | -22.16479 | -56.03566 | 2024-09-29 04:06:00 | NOAA-21 | ANTÔNIO JOÃO | MATO GROSSO DO SUL | Brasil | 5000906 | 50 | 33 | nan | nan | nan | Cerrado | 13.1 |
| fc927dbe-a12c-37ac-b8d1-114d686543d6 | -22.16346 | -56.04119 | 2024-09-29 04:06:00 | NOAA-21 | ANTÔNIO JOÃO | MATO GROSSO DO SUL | Brasil | 5000906 | 50 | 33 | nan | nan | nan | Cerrado | 13.1 |
| 8b97ec2f-82d6-33e3-bdff-bc2b03670746 | -23.92789 | -55.40075 | 2024-09-29 04:06:00 | NOAA-21 | PARANHOS | MATO GROSSO DO SUL | Brasil | 5006358 | 50 | 33 | nan | nan | nan | Mata Atlântica | 3.0 |
| a187b2f6-ea02-3d3e-9fe9-2451c030f01d | -23.92431 | -55.39641 | 2024-09-29 04:06:00 | NOAA-21 | PARANHOS | MATO GROSSO DO SUL | Brasil | 5006358 | 50 | 33 | nan | nan | nan | Mata Atlântica | 2.5 |
| e727be96-ee7f-3048-b3d4-5cc75ad5bc2c | -23.92332 | -55.40058 | 2024-09-29 04:06:00 | NOAA-21 | PARANHOS | MATO GROSSO DO SUL | Brasil | 5006358 | 50 | 33 | nan | nan | nan | Mata Atlântica | 2.5 |
| 9440c40b-6c64-3a6f-87ba-746efaacd3dc | -21.0107 | -57.51077 | 2024-09-29 04:06:00 | NOAA-21 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Pantanal | 4.6 |
| 1f0f6120-9da7-3b9a-a24b-1bca09768fe3 | -21.01041 | -57.50679 | 2024-09-29 04:06:00 | NOAA-21 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Pantanal | 3.1 |
| 82a8d157-ee14-3d62-bf63-176cd6677e40 | -21.00891 | -57.51294 | 2024-09-29 04:06:00 | NOAA-21 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Pantanal | 6.1 |
| ed81ef56-be96-361e-8c4f-591014eac10f | -21.00388 | -57.50938 | 2024-09-29 04:06:00 | NOAA-21 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Pantanal | 2.9 |
| 8b03a9a1-34dc-3d40-9f61-e6ef5debedb5 | -20.44089 | -42.00705 | 2024-09-29 04:06:00 | NOAA-21 | LUISBURGO | MINAS GERAIS | Brasil | 3138674 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| e0915615-14e1-346d-a099-c29bc87a2998 | -20.43811 | -42.00278 | 2024-09-29 04:06:00 | NOAA-21 | ALTO JEQUITIBÁ | MINAS GERAIS | Brasil | 3153509 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 630ce240-c5e1-373e-9540-14655759d890 | -20.43535 | -41.99834 | 2024-09-29 04:06:00 | NOAA-21 | ALTO JEQUITIBÁ | MINAS GERAIS | Brasil | 3153509 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| edaeeedd-db11-3116-83c2-9431ee61422b | -20.43477 | -42.00219 | 2024-09-29 04:06:00 | NOAA-21 | ALTO JEQUITIBÁ | MINAS GERAIS | Brasil | 3153509 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 3a424275-66fc-3f7b-988d-8e1bfa469377 | -21.32231 | -41.73842 | 2024-09-29 04:06:00 | NOAA-21 | ITAPERUNA | RIO DE JANEIRO | Brasil | 3302205 | 33 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| a64061f5-9fea-3516-bc29-334bfce376d1 | -21.31948 | -41.73403 | 2024-09-29 04:06:00 | NOAA-21 | ITAPERUNA | RIO DE JANEIRO | Brasil | 3302205 | 33 | 33 | nan | nan | nan | Mata Atlântica | 2.8 |
| 7a3d6168-e0b3-38d0-9f99-42ce98ef3242 | -21.31892 | -41.73787 | 2024-09-29 04:06:00 | NOAA-21 | ITAPERUNA | RIO DE JANEIRO | Brasil | 3302205 | 33 | 33 | nan | nan | nan | Mata Atlântica | 2.8 |
| 3f01473b-f41d-3169-b6e8-989e2316bbc7 | -21.3161 | -41.73347 | 2024-09-29 04:06:00 | NOAA-21 | ITAPERUNA | RIO DE JANEIRO | Brasil | 3302205 | 33 | 33 | nan | nan | nan | Mata Atlântica | 2.8 |
| d946523e-76d1-3e7b-9dc7-05f4a8878f38 | -22.60217 | -42.2109 | 2024-09-29 04:06:00 | NOAA-21 | ARARUAMA | RIO DE JANEIRO | Brasil | 3300209 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| e9292ce6-2e52-325c-b9fe-927eaca5bd31 | -20.41586 | -43.55261 | 2024-09-29 04:06:00 | NOAA-21 | OURO PRETO | MINAS GERAIS | Brasil | 3146107 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| d7aa8b1d-943d-390f-959f-e5aed403b747 | -20.45947 | -44.54672 | 2024-09-29 04:06:00 | NOAA-21 | ITAGUARA | MINAS GERAIS | Brasil | 3132206 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 5d6bed1e-e94b-300d-83ae-c53eb9b2cc82 | -20.15294 | -44.91198 | 2024-09-29 04:06:00 | NOAA-21 | DIVINÓPOLIS | MINAS GERAIS | Brasil | 3122306 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 724eddd3-44ab-3373-8bca-ed1712375885 | -20.25759 | -44.07053 | 2024-09-29 04:06:00 | NOAA-21 | BRUMADINHO | MINAS GERAIS | Brasil | 3109006 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| aa29adc9-62f9-336f-8712-f08e21f9d4da | -20.12914 | -44.48272 | 2024-09-29 04:06:00 | NOAA-21 | ITAÚNA | MINAS GERAIS | Brasil | 3133808 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| b2880f0c-4a33-3f79-9387-227e5c5e4488 | -20.12579 | -44.48211 | 2024-09-29 04:06:00 | NOAA-21 | ITAÚNA | MINAS GERAIS | Brasil | 3133808 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 253dbe5d-4ec0-3848-a4aa-e5800a756448 | -20.12454 | -44.48965 | 2024-09-29 04:06:00 | NOAA-21 | ITAÚNA | MINAS GERAIS | Brasil | 3133808 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| d44913b2-c0b9-32a5-b56b-ce96fa67346f | -20.12392 | -44.49345 | 2024-09-29 04:06:00 | NOAA-21 | ITAÚNA | MINAS GERAIS | Brasil | 3133808 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 204ac782-54b7-3260-a2fe-5f57b1c3e0a5 | -20.12305 | -44.47778 | 2024-09-29 04:06:00 | NOAA-21 | ITAÚNA | MINAS GERAIS | Brasil | 3133808 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| c14d70e4-a965-314f-a1fb-753c4c0dde07 | -20.12244 | -44.48151 | 2024-09-29 04:06:00 | NOAA-21 | ITAÚNA | MINAS GERAIS | Brasil | 3133808 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 7cf025ba-ca9c-3a2d-a35e-5952868386db | -20.1212 | -44.489 | 2024-09-29 04:06:00 | NOAA-21 | ITAÚNA | MINAS GERAIS | Brasil | 3133808 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| c116ff95-6c63-3e23-9a9d-9ce7b1b928f5 | -20.11969 | -44.4772 | 2024-09-29 04:06:00 | NOAA-21 | ITAÚNA | MINAS GERAIS | Brasil | 3133808 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 0af859b7-eeda-370c-96fb-8483b1f7b5b8 | -20.11908 | -44.48092 | 2024-09-29 04:06:00 | NOAA-21 | ITAÚNA | MINAS GERAIS | Brasil | 3133808 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 55b7ae6a-ca75-37da-aff0-db3568b78ab2 | -22.76553 | -45.66082 | 2024-09-29 04:06:00 | NOAA-21 | CAMPOS DO JORDÃO | SÃO PAULO | Brasil | 3509700 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| 2a7c97fe-0694-30f5-a34f-0d69d8f15475 | -27.48814 | -48.39405 | 2024-09-29 04:08:00 | NOAA-21 | FLORIANÓPOLIS | SANTA CATARINA | Brasil | 4205407 | 42 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 29b4fec5-9d22-3d53-a87e-6bcae3a78290 | -26.36728 | -49.95016 | 2024-09-29 04:08:00 | NOAA-21 | ITAIÓPOLIS | SANTA CATARINA | Brasil | 4208104 | 42 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 2fedc3a6-6282-360c-8ac0-44d2b18164c4 | -26.28139 | -50.28244 | 2024-09-29 04:08:00 | NOAA-21 | TRÊS BARRAS | SANTA CATARINA | Brasil | 4218301 | 42 | 33 | nan | nan | nan | Mata Atlântica | 3.5 |
| e093b730-479e-306e-9015-6dee93a70c93 | -26.28062 | -50.28632 | 2024-09-29 04:08:00 | NOAA-21 | TRÊS BARRAS | SANTA CATARINA | Brasil | 4218301 | 42 | 33 | nan | nan | nan | Mata Atlântica | 3.5 |
| b2a945a9-f6cc-3151-92d5-77c3c1fe71e7 | -26.27986 | -50.29018 | 2024-09-29 04:08:00 | NOAA-21 | TRÊS BARRAS | SANTA CATARINA | Brasil | 4218301 | 42 | 33 | nan | nan | nan | Mata Atlântica | 2.4 |
| a5ba5ccd-8dca-3713-b98f-98db4ab20689 | -26.2774 | -50.28149 | 2024-09-29 04:08:00 | NOAA-21 | TRÊS BARRAS | SANTA CATARINA | Brasil | 4218301 | 42 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 8afbb3c2-e91f-34ca-9e24-8149f7ca9ad6 | -26.27587 | -50.28923 | 2024-09-29 04:08:00 | NOAA-21 | TRÊS BARRAS | SANTA CATARINA | Brasil | 4218301 | 42 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| c553a710-8f06-36e0-891b-edd98a893ea4 | -26.27496 | -50.27273 | 2024-09-29 04:08:00 | NOAA-21 | TRÊS BARRAS | SANTA CATARINA | Brasil | 4218301 | 42 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| aca43b68-df49-3cb2-abd6-191e6ae80f90 | -26.27175 | -50.26788 | 2024-09-29 04:08:00 | NOAA-21 | TRÊS BARRAS | SANTA CATARINA | Brasil | 4218301 | 42 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| e2326721-7440-3e8c-94c2-b15bd0c8980f | -26.26776 | -50.26695 | 2024-09-29 04:08:00 | NOAA-21 | TRÊS BARRAS | SANTA CATARINA | Brasil | 4218301 | 42 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 0c3e3a06-9e15-34ee-87c4-1f8586037f69 | -29.816 | -51.17709 | 2024-09-29 04:08:00 | NOAA-21 | SAPUCAIA DO SUL | RIO GRANDE DO SUL | Brasil | 4320008 | 43 | 33 | nan | nan | nan | Pampa | 1.2 |
| b539715a-3985-3203-875c-c5a380968043 | -26.02816 | -53.75692 | 2024-09-29 04:08:00 | NOAA-21 | PRANCHITA | PARANÁ | Brasil | 4120358 | 41 | 33 | nan | nan | nan | Mata Atlântica | 2.5 |
| 1795d43f-ab1f-3543-9554-89b487fa1445 | -3.95682 | -41.48788 | 2024-09-29 04:23:00 | AQUA_M-M | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 43.6 |
| edff11d0-d9a3-3cdf-9e0d-7b1a6e403d8d | -3.94848 | -41.49133 | 2024-09-29 04:23:00 | AQUA_M-M | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 74.6 |
| 1dfa0d9f-b6eb-388f-b042-2411759b3a39 | -15.83767 | -42.15649 | 2024-09-29 04:27:00 | AQUA_M-M | TAIOBEIRAS | MINAS GERAIS | Brasil | 3168002 | 31 | 33 | nan | nan | nan | Mata Atlântica | 46.5 |
| 6e18eabf-b28b-382b-ad4c-da83589d660f | -15.8288 | -42.16198 | 2024-09-29 04:27:00 | AQUA_M-M | TAIOBEIRAS | MINAS GERAIS | Brasil | 3168002 | 31 | 33 | nan | nan | nan | Mata Atlântica | 49.5 |
| 47ebf168-98ff-327f-a6dc-09ed6c273a9c | -12.80671 | -44.79499 | 2024-09-29 04:27:00 | AQUA_M-M | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 50.3 |
| ec65fb3f-4133-3026-be5c-52977584f031 | -12.80435 | -44.8024 | 2024-09-29 04:27:00 | AQUA_M-M | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 72.1 |
| 3eabd086-7815-301d-971f-f949e0371546 | -19.74136 | -41.62223 | 2024-09-29 04:29:00 | AQUA_M-M | TAPARUBA | MINAS GERAIS | Brasil | 3168051 | 31 | 33 | nan | nan | nan | Mata Atlântica | 28.1 |
| b3727c9b-ae57-3d44-81b0-f555692db446 | -19.73676 | -41.61581 | 2024-09-29 04:29:00 | AQUA_M-M | TAPARUBA | MINAS GERAIS | Brasil | 3168051 | 31 | 33 | nan | nan | nan | Mata Atlântica | 26.7 |
| ade9ce7e-d580-3728-a334-e579f2e3e6c0 | -18.83144 | -41.9515 | 2024-09-29 04:29:00 | AQUA_M-M | GOVERNADOR VALADARES | MINAS GERAIS | Brasil | 3127701 | 31 | 33 | nan | nan | nan | Mata Atlântica | 34.3 |
| c304ed55-92f2-3f54-b0de-55c1d30ddbe6 | -18.82985 | -41.95858 | 2024-09-29 04:29:00 | AQUA_M-M | GOVERNADOR VALADARES | MINAS GERAIS | Brasil | 3127701 | 31 | 33 | nan | nan | nan | Mata Atlântica | 47.2 |


[Clique aqui para ver as próximas entradas](README36.md)
