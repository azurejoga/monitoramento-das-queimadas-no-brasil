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

## Dados Diários - Página 7

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 35068247-ae65-3597-96e2-b0f580bbe618 | -13.70958 | -45.69571 | 2025-07-23 03:45:00 | NOAA-20 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 42853866-34e0-3bfa-b389-5f7d55d99b14 | -15.77908 | -46.06286 | 2025-07-23 03:45:00 | NOAA-20 | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 0dce47cd-47d2-3249-b86e-ac26d2737ca1 | -13.65466 | -45.71894 | 2025-07-23 03:45:00 | NOAA-20 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 52e7a9b3-0228-3cf6-821e-5cb1eb39d50e | -13.67537 | -44.2254 | 2025-07-23 03:45:00 | NOAA-20 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 3c2894ee-c072-31c2-816c-addb80d0e045 | -12.66225 | -45.04265 | 2025-07-23 03:45:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 28736283-8023-3b0e-b6e7-9bb30764c3fd | -14.18259 | -45.34062 | 2025-07-23 03:45:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| fa439808-d6d3-337e-a802-4eec03903071 | -14.17815 | -45.35622 | 2025-07-23 03:45:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 09d415c0-e061-3893-82c9-994e5a36118c | -17.56967 | -47.51367 | 2025-07-23 03:45:00 | NOAA-20 | CATALÃO | GOIÁS | Brasil | 5205109 | 52 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 99acc5d3-f383-3914-8e09-487f6f560890 | -13.65407 | -45.72205 | 2025-07-23 03:45:00 | NOAA-20 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 93723501-2102-31da-8df4-cc39df1a1a9c | -13.68934 | -45.69157 | 2025-07-23 03:45:00 | NOAA-20 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 03a976ce-af33-3817-9da6-f0d5e354a604 | -13.69261 | -45.70174 | 2025-07-23 03:45:00 | NOAA-20 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 0efc5ee6-5d70-3b50-ab45-a00cacd12d57 | -13.70511 | -45.69164 | 2025-07-23 03:45:00 | NOAA-20 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 3.9 |
| deaaed28-b787-3690-bac9-7b54f5365046 | -16.03626 | -43.72688 | 2025-07-23 03:45:00 | NOAA-20 | SÃO JOÃO DA PONTE | MINAS GERAIS | Brasil | 3162401 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 01e1db8f-fbf4-3807-91a5-b228041c1ad9 | -17.8418 | -42.63878 | 2025-07-23 03:45:00 | NOAA-20 | ARICANDUVA | MINAS GERAIS | Brasil | 3104452 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 83beb29d-d8cd-338f-b4c0-27aa3635787d | -13.71018 | -45.69266 | 2025-07-23 03:45:00 | NOAA-20 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 2df196a8-22df-390a-8230-131592160e3c | -13.54502 | -43.70943 | 2025-07-23 03:45:00 | NOAA-20 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| d0aef282-7699-313b-87d1-4eb202e5854f | -21.38704 | -48.67419 | 2025-07-23 03:47:00 | NOAA-20 | TAQUARITINGA | SÃO PAULO | Brasil | 3553708 | 35 | 33 | nan | nan | nan | Cerrado | 0.9 |
| d9053918-9b90-34b6-9339-1c62903c2ef7 | -23.59359 | -54.32978 | 2025-07-23 03:47:00 | NOAA-20 | ELDORADO | MATO GROSSO DO SUL | Brasil | 5003751 | 50 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| 838bfdb3-433f-3bc6-9368-2413687d91d4 | -23.57213 | -47.05408 | 2025-07-23 03:47:00 | NOAA-20 | SÃO ROQUE | SÃO PAULO | Brasil | 3550605 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 0f012396-13d9-39e0-b607-1327bde54f81 | -23.39618 | -47.00954 | 2025-07-23 03:47:00 | NOAA-20 | PIRAPORA DO BOM JESUS | SÃO PAULO | Brasil | 3539103 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 7546fe3e-3cd0-3f30-991d-a6871c1e116e | -19.60903 | -41.47817 | 2025-07-23 03:47:00 | NOAA-20 | POCRANE | MINAS GERAIS | Brasil | 3151909 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.2 |
| f50d125d-ac7f-3184-8d87-4e5a0de58320 | -22.15422 | -52.68226 | 2025-07-23 03:47:00 | NOAA-20 | ANAURILÂNDIA | MATO GROSSO DO SUL | Brasil | 5000807 | 50 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| dcd9b27d-5b6e-3ec3-a7fb-31d4691681ce | -22.80125 | -52.48616 | 2025-07-23 03:47:00 | NOAA-20 | PARANAVAÍ | PARANÁ | Brasil | 4118402 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| de1b97a9-b557-315f-8af0-27c522dd6651 | -19.58008 | -40.55 | 2025-07-23 03:47:00 | NOAA-20 | COLATINA | ESPÍRITO SANTO | Brasil | 3201506 | 32 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 6927e4b8-f618-39d7-81c8-15e6efb2a2d3 | -22.7999 | -52.49165 | 2025-07-23 03:47:00 | NOAA-20 | PARANAVAÍ | PARANÁ | Brasil | 4118402 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| 18248ec4-8d1d-3d3b-8b05-3f206dae0ec6 | -21.36866 | -48.60648 | 2025-07-23 03:47:00 | NOAA-20 | CÂNDIDO RODRIGUES | SÃO PAULO | Brasil | 3510104 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| b0ae3023-1579-35e8-9c94-7b9374cb2295 | -22.15201 | -52.68213 | 2025-07-23 03:47:00 | NOAA-20 | ANAURILÂNDIA | MATO GROSSO DO SUL | Brasil | 5000807 | 50 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| fc2c348c-f194-37fd-9f36-ab4ba6b67ec1 | -20.1302 | -43.72405 | 2025-07-23 03:47:00 | NOAA-20 | RIO ACIMA | MINAS GERAIS | Brasil | 3154804 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 149fc45a-fee2-3642-91fd-569098c59446 | -20.13153 | -43.71687 | 2025-07-23 03:47:00 | NOAA-20 | RIO ACIMA | MINAS GERAIS | Brasil | 3154804 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| da7cf0b9-8126-3406-a964-b7b53eba230c | -22.69709 | -43.34796 | 2025-07-23 03:47:00 | NOAA-20 | DUQUE DE CAXIAS | RIO DE JANEIRO | Brasil | 3301702 | 33 | 33 | nan | nan | nan | Mata Atlântica | 0.4 |
| 5327a863-93d1-3b4c-afb8-d05ec7ed782f | -22.15934 | -52.68975 | 2025-07-23 03:47:00 | NOAA-20 | ANAURILÂNDIA | MATO GROSSO DO SUL | Brasil | 5000807 | 50 | 33 | nan | nan | nan | Mata Atlântica | 2.3 |
| 88d08b9d-00cf-3dc6-883f-30977a4a9ab8 | -20.32679 | -41.9887 | 2025-07-23 03:47:00 | NOAA-20 | MANHUMIRIM | MINAS GERAIS | Brasil | 3139508 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.4 |
| 177c15bc-6178-3070-a391-991dce1dfd2f | -22.39585 | -49.79359 | 2025-07-23 03:47:00 | NOAA-20 | LUPÉRCIO | SÃO PAULO | Brasil | 3527801 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| 36489c4d-2db4-376b-8152-df9addaf4b93 | -22.15711 | -52.68953 | 2025-07-23 03:47:00 | NOAA-20 | ANAURILÂNDIA | MATO GROSSO DO SUL | Brasil | 5000807 | 50 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| 58360022-66a5-3056-b9f8-a3f5ba7b9208 | -22.15858 | -52.68367 | 2025-07-23 03:47:00 | NOAA-20 | ANAURILÂNDIA | MATO GROSSO DO SUL | Brasil | 5000807 | 50 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| dfb74057-46a0-349e-b43a-c626a9ce4ae0 | -22.15279 | -52.68817 | 2025-07-23 03:47:00 | NOAA-20 | ANAURILÂNDIA | MATO GROSSO DO SUL | Brasil | 5000807 | 50 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| faa9f282-bcb5-341a-9507-6719d3dba21b | -20.63986 | -41.96302 | 2025-07-23 03:47:00 | NOAA-20 | ESPERA FELIZ | MINAS GERAIS | Brasil | 3124203 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| a7d71a28-8be0-37a9-af93-a758679bf379 | -22.91625 | -44.04297 | 2025-07-23 03:47:00 | NOAA-20 | MANGARATIBA | RIO DE JANEIRO | Brasil | 3302601 | 33 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| f8c56cbc-6654-3b4b-bd18-17ca2c42a32b | -23.21944 | -46.64548 | 2025-07-23 03:47:00 | NOAA-20 | ATIBAIA | SÃO PAULO | Brasil | 3504107 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| e9cc4810-29ea-3f5d-90da-bc3f61805076 | -22.39808 | -49.79128 | 2025-07-23 03:47:00 | NOAA-20 | LUPÉRCIO | SÃO PAULO | Brasil | 3527801 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| acaa38cd-d959-3afd-a65b-97089f7158e8 | -18.57063 | -46.48756 | 2025-07-23 03:47:00 | NOAA-20 | PATOS DE MINAS | MINAS GERAIS | Brasil | 3148004 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| c7bddd9b-7273-3f4a-944c-07f1652f3ddf | -22.80751 | -52.4883 | 2025-07-23 03:47:00 | NOAA-20 | PARANAVAÍ | PARANÁ | Brasil | 4118402 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| f1fe8f27-6d34-3840-a659-1bb2538b7a29 | -21.48298 | -41.0799 | 2025-07-23 03:47:00 | NOAA-20 | SÃO FRANCISCO DE ITABAPOANA | RIO DE JANEIRO | Brasil | 3304755 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| d78cc440-9a8b-3ac5-9786-7714063159a1 | -25.09519 | -49.51205 | 2025-07-23 03:47:00 | NOAA-20 | ITAPERUÇU | PARANÁ | Brasil | 4111258 | 41 | 33 | nan | nan | nan | Mata Atlântica | 2.3 |
| ceac02a7-e73e-37ee-a600-ac87303903b8 | -20.59562 | -41.04689 | 2025-07-23 03:47:00 | NOAA-20 | VARGEM ALTA | ESPÍRITO SANTO | Brasil | 3205036 | 32 | 33 | nan | nan | nan | Mata Atlântica | 0.4 |
| 3f9d8540-eba4-3683-9a35-93ad99a740b5 | -22.3972 | -49.79523 | 2025-07-23 03:47:00 | NOAA-20 | LUPÉRCIO | SÃO PAULO | Brasil | 3527801 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| 83ca0923-d802-3cb1-8f9a-043f7dd010e2 | -27.68787 | -48.75216 | 2025-07-23 03:49:00 | NOAA-20 | SANTO AMARO DA IMPERATRIZ | SANTA CATARINA | Brasil | 4215703 | 42 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 0c62735b-9d56-378f-9d4a-ff6a01c0795a | -3.1833 | -49.4429 | 2025-07-23 03:50:00 | GOES-19 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 80.5 |
| 8b9eef76-a049-3519-9e46-2089c77d30aa | -3.1649 | -49.4435 | 2025-07-23 03:50:00 | GOES-19 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 56.3 |
| ae345131-f01c-31fa-a9e5-2e9a031e3742 | -3.1648 | -49.4648 | 2025-07-23 03:50:00 | GOES-19 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 62.9 |
| 4d448d18-f34c-320a-8a47-1cc6802fb38a | -7.7569 | -44.0183 | 2025-07-23 03:50:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 67.7 |
| 5a10cfd3-fa6a-3dd2-ac33-9a5ba0fc34e9 | -3.1832 | -49.4642 | 2025-07-23 03:50:00 | GOES-19 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 96.4 |
| 1455237e-83d0-36e2-a8f4-771d5b947a1b | -3.1648 | -49.4648 | 2025-07-23 04:00:00 | GOES-19 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 67.0 |
| a7bea14e-071b-30b9-8bac-2fedb5714c9b | -3.1649 | -49.4435 | 2025-07-23 04:00:00 | GOES-19 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 53.5 |
| 2ded3310-1f16-3035-b97f-3953b6524713 | -3.1833 | -49.4429 | 2025-07-23 04:00:00 | GOES-19 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 78.0 |
| 9075d184-f0fb-32ac-87a5-c7103f382695 | -3.1832 | -49.4642 | 2025-07-23 04:00:00 | GOES-19 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 105.0 |
| 01a06836-a965-31d1-9305-b99165871612 | -7.7569 | -44.0183 | 2025-07-23 04:00:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 58.6 |
| 758d862d-a83b-3574-a4d5-d7ed70520652 | -3.1833 | -49.4429 | 2025-07-23 04:10:00 | GOES-19 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 55.5 |
| b52105d7-298c-3633-ac0b-e5f8cf0850dd | -3.1832 | -49.4642 | 2025-07-23 04:10:00 | GOES-19 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 67.0 |
| 464983ed-15f9-3905-8046-895b0e11b6a8 | -3.1648 | -49.4648 | 2025-07-23 04:10:00 | GOES-19 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 92.6 |
| cad29a9c-7677-370e-a6a9-d3ed0c36df66 | -3.1649 | -49.4435 | 2025-07-23 04:10:00 | GOES-19 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 78.8 |
| 3b08f5d9-d839-3283-afb9-5c4ec6e9d788 | -22.8016 | -52.482 | 2025-07-23 04:20:00 | GOES-19 | PARANAVAÍ | PARANÁ | Brasil | 4118402 | 41 | 33 | nan | nan | nan | Mata Atlântica | 127.5 |
| 2d2c46c1-edb5-3310-ba9b-c6c0a531a5a3 | -7.7569 | -44.0183 | 2025-07-23 04:20:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 59.6 |
| a78aa231-46bc-33ae-9e6a-f4f28cf2cf66 | -3.1833 | -49.4429 | 2025-07-23 04:20:00 | GOES-19 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 50.7 |
| 7696fc9d-a4e1-39d3-b75a-557f46775b15 | -3.1649 | -49.4435 | 2025-07-23 04:20:00 | GOES-19 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 72.4 |
| d033e043-b508-36d6-b3e1-e9c1c4a6cf86 | -3.1648 | -49.4648 | 2025-07-23 04:20:00 | GOES-19 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 87.8 |
| b4bc60c7-aa0d-3b1e-ac89-a7695df308d1 | -3.1832 | -49.4642 | 2025-07-23 04:20:00 | GOES-19 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 60.0 |
| 9c8f39be-8c03-392f-be8f-1d1c9cc7bd77 | -3.1832 | -49.4642 | 2025-07-23 04:30:00 | GOES-19 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 68.5 |
| e98fe87c-4f6b-3d1e-89b3-5c158164efd6 | -3.1648 | -49.4648 | 2025-07-23 04:30:00 | GOES-19 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 91.9 |
| 5e57ce47-570e-304a-a302-d2555d588a3c | -3.1649 | -49.4435 | 2025-07-23 04:30:00 | GOES-19 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 63.1 |
| 4445a47c-ccc5-31f7-9059-4defb3914b79 | -5.6905 | -43.67305 | 2025-07-23 04:32:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 0690e373-293b-3a83-833a-11d34ebcca80 | -4.31911 | -47.987 | 2025-07-23 04:32:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| e87c4f67-d84d-3dc3-bfd6-aa0cad85e6f3 | -3.82719 | -43.01843 | 2025-07-23 04:32:00 | NOAA-21 | BURITI | MARANHÃO | Brasil | 2102200 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| aba72212-a386-3178-908e-5255a24657db | -6.94501 | -43.96315 | 2025-07-23 04:32:00 | NOAA-21 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 7a0d5b48-a4a7-3ce3-baef-9c3a1e3aab2b | -4.54695 | -48.00889 | 2025-07-23 04:32:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 1f2198a1-62c4-3694-ae4a-95747739407a | -3.11802 | -47.01237 | 2025-07-23 04:32:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 2103ae83-3ff8-3694-b481-32541e4b19a6 | -3.04637 | -47.38093 | 2025-07-23 04:32:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 955a5e47-5c32-3b05-850b-c5075c2c68b6 | -0.74986 | -47.75357 | 2025-07-23 04:32:00 | NOAA-21 | MARAPANIM | PARÁ | Brasil | 1504406 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 55651e1b-44db-3375-acca-1572b5bf9a7b | -4.25503 | -39.2278 | 2025-07-23 04:32:00 | NOAA-21 | CARIDADE | CEARÁ | Brasil | 2303006 | 23 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 36d82f6f-58c0-3f8d-a8d7-ef6b5bb5d583 | -3.74769 | -49.04799 | 2025-07-23 04:32:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 1acf376d-4160-3ea0-a1e7-89a89a9894f6 | -3.03903 | -47.8631 | 2025-07-23 04:32:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 9c1424c4-4517-30c7-944e-43a36f7bbc86 | -5.68668 | -43.67247 | 2025-07-23 04:32:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 5.1 |
| e07152ae-3ce7-3f1b-8e4e-460bf4304317 | -4.8435 | -45.30628 | 2025-07-23 04:32:00 | NOAA-21 | LAGOA GRANDE DO MARANHÃO | MARANHÃO | Brasil | 2105963 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 09c60b3e-2f37-3da7-a0e3-b1bb046b9c3d | -3.0349 | -49.42939 | 2025-07-23 04:32:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| ed41e924-1d3f-3a32-938b-5251bd5aac52 | -5.67637 | -43.66917 | 2025-07-23 04:32:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 607557da-6c3c-3d76-8b4b-6006b3dc4fa8 | -3.9439 | -41.48388 | 2025-07-23 04:32:00 | NOAA-21 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 649d440d-c961-38eb-9b66-2985e59a216e | -6.84868 | -42.73862 | 2025-07-23 04:32:00 | NOAA-21 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| a8953082-4f26-3930-8334-44e12e9d1796 | -5.83154 | -44.1012 | 2025-07-23 04:32:00 | NOAA-21 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 12e558c8-59fc-3140-a07c-80af477c6bdd | -4.04753 | -42.51479 | 2025-07-23 04:32:00 | NOAA-21 | NOSSA SENHORA DOS REMÉDIOS | PIAUÍ | Brasil | 2206803 | 22 | 33 | nan | nan | nan | Caatinga | 14.1 |
| 204d7b2b-0237-3c95-b4d4-1fed69d7a37c | -4.38485 | -43.29277 | 2025-07-23 04:32:00 | NOAA-21 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 87540804-fa21-3ad1-89f6-612c487833df | -4.09382 | -46.92504 | 2025-07-23 04:32:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 2105c8df-5eb5-39e5-bf99-eb07aabff77f | -5.49695 | -45.84758 | 2025-07-23 04:32:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| e0cee039-1286-3ed7-825d-87b76d4529ee | -4.52463 | -42.07063 | 2025-07-23 04:32:00 | NOAA-21 | BOQUEIRÃO DO PIAUÍ | PIAUÍ | Brasil | 2201945 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 6183861e-52cc-37a7-bc19-4dec896779d1 | -5.83527 | -44.10177 | 2025-07-23 04:32:00 | NOAA-21 | JATOBÁ | MARANHÃO | Brasil | 2105450 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| a6bbb71d-a24f-3bfc-a830-ac149d495345 | -5.88158 | -42.40568 | 2025-07-23 04:32:00 | NOAA-21 | PASSAGEM FRANCA DO PIAUÍ | PIAUÍ | Brasil | 2207751 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 72b63a92-5146-337f-a6bc-976af65c4145 | -5.68286 | -43.67184 | 2025-07-23 04:32:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 75e6caf4-64e5-3fe0-ac07-ad7bdfe04aa8 | -6.1849 | -44.40909 | 2025-07-23 04:32:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 3d1017e4-1e9a-3a24-8bed-05ab81b331a1 | -6.9681 | -44.3774 | 2025-07-23 04:32:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 2e6e6262-1244-3e80-bf58-bd44606e9260 | -4.89588 | -44.96292 | 2025-07-23 04:32:00 | NOAA-21 | ESPERANTINÓPOLIS | MARANHÃO | Brasil | 2104008 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| bbabc3eb-6982-3707-af74-392d2b200657 | -2.9779 | -49.52139 | 2025-07-23 04:32:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |


[Clique aqui para ver as próximas entradas](README8.md)
