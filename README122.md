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

## Dados Diários - Página 122

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| a2d51fd2-0969-355f-a4b0-c8ea5d7f90c8 | -13.76091 | -48.68945 | 2025-10-02 04:51:00 | NOAA-20 | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 8268f8fa-133b-3275-8646-df13b92f94c4 | -14.92447 | -47.22654 | 2025-10-02 04:51:00 | NOAA-20 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 3c39d29e-87a0-36cd-932c-03ba29292c8b | -12.20754 | -47.79523 | 2025-10-02 04:51:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 3bdac42e-dd8f-3827-8c5d-a58609143596 | -13.75046 | -48.01133 | 2025-10-02 04:51:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 928b40d3-3ba7-3125-9dac-55c7cceec9f8 | -11.86293 | -45.00126 | 2025-10-02 04:51:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 63661847-9dbc-3aad-99c2-8793341199da | -16.04537 | -50.87424 | 2025-10-02 04:51:00 | NOAA-20 | FAZENDA NOVA | GOIÁS | Brasil | 5207600 | 52 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 581eedd0-bc24-3280-9893-492e63147256 | -13.0815 | -47.0856 | 2025-10-02 04:51:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 2b9119cb-8af8-30b4-a315-3488b6f88e35 | -12.83764 | -46.95245 | 2025-10-02 04:51:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 2fe9f847-bb9b-398a-b7f8-2a20444c777d | -14.88354 | -48.33703 | 2025-10-02 04:51:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 2670d097-bb5d-3969-a6ce-37291025a36f | -12.70208 | -48.57367 | 2025-10-02 04:51:00 | NOAA-20 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 50c98130-0db2-303c-8400-2f2b7f19fe4c | -11.58872 | -50.17593 | 2025-10-02 04:51:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 4.5 |
| a2ce8def-f431-3ee2-a29f-7187d7ddcbe9 | -13.91329 | -48.07298 | 2025-10-02 04:51:00 | NOAA-20 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| ef97cc6b-e7ce-3324-83c2-beb498dc6081 | -13.94305 | -48.13164 | 2025-10-02 04:51:00 | NOAA-20 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 28ae1367-2ebe-37ce-817a-4baf9d6e8a0b | -11.61335 | -45.03558 | 2025-10-02 04:51:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| b60a0ba3-7b56-3414-a4fb-7f7a790e09f8 | -12.22069 | -43.76523 | 2025-10-02 04:51:00 | NOAA-20 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 2.9 |
| e5a98366-58f7-3b9b-9581-66ce5f611d18 | -10.81705 | -46.63136 | 2025-10-02 04:51:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 55b8083c-4582-3061-912a-a54723c6ea69 | -12.08707 | -44.91985 | 2025-10-02 04:51:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 4053f713-a9f6-3d78-9b6b-94a47909d721 | -13.79541 | -48.05256 | 2025-10-02 04:51:00 | NOAA-20 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 9e54b5c0-f85a-3a3c-bc21-cadfc85eda6b | -12.63409 | -44.85648 | 2025-10-02 04:51:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 064d4ada-aa8d-3ed6-b7e0-40601181b264 | -13.77407 | -48.04779 | 2025-10-02 04:51:00 | NOAA-20 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 642fe968-1736-33cc-a104-b42e412f03a6 | -15.83089 | -42.62757 | 2025-10-02 04:51:00 | NOAA-20 | RIO PARDO DE MINAS | MINAS GERAIS | Brasil | 3155603 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.1 |
| 7017fc73-cb2b-31a0-b658-62451a22997e | -13.30373 | -47.83887 | 2025-10-02 04:51:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 4.3 |
| bbdfbd10-56e1-3002-bc25-e4cab5e5e1e7 | -11.87607 | -45.02147 | 2025-10-02 04:51:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 2e4302d1-6f65-30b9-a136-2dbdf47df419 | -11.46377 | -45.00061 | 2025-10-02 04:51:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| f1077f68-6411-348f-81a6-5f49ddf695e5 | -14.36424 | -45.9436 | 2025-10-02 04:51:00 | NOAA-20 | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 74823a76-513a-325d-abad-f0a94a1a988a | -12.85814 | -46.93841 | 2025-10-02 04:51:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 1fe5cc42-d0bb-3b03-972c-e394452f2a21 | -14.22292 | -46.10519 | 2025-10-02 04:51:00 | NOAA-20 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 7144ffe7-e048-30d0-b059-4fd6f5ff8f63 | -15.2583 | -49.28363 | 2025-10-02 04:51:00 | NOAA-20 | GOIANÉSIA | GOIÁS | Brasil | 5208608 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 9e72f19e-22c9-3678-916a-a5447b58ac9a | -13.56993 | -47.58965 | 2025-10-02 04:51:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| d2e9dc67-bd7c-3404-8d4b-203bf9bc824b | -13.80451 | -47.54415 | 2025-10-02 04:51:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 10.3 |
| dedc5121-2b80-306e-9326-1b9197675e2e | -10.47389 | -49.11065 | 2025-10-02 04:51:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 4623b81b-e81d-3deb-b14d-12270f97fb9f | -12.87206 | -47.01031 | 2025-10-02 04:51:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 43b2bbcc-1c41-33c3-a742-40100abf2a29 | -10.42984 | -47.47697 | 2025-10-02 04:51:00 | NOAA-20 | LAGOA DO TOCANTINS | TOCANTINS | Brasil | 1711951 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 92c7f254-7251-3477-b81f-3278527f7b33 | -14.29851 | -45.90075 | 2025-10-02 04:51:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| ee19bb80-38a7-3273-b522-7a1e0ac750dd | -11.38842 | -45.04169 | 2025-10-02 04:51:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| de3af700-7418-3a97-9b8b-a113c868fadf | -13.64589 | -47.19214 | 2025-10-02 04:51:00 | NOAA-20 | TERESINA DE GOIÁS | GOIÁS | Brasil | 5221080 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 734fbf50-bbe0-3160-b5c5-fa090c276504 | -14.67851 | -49.61495 | 2025-10-02 04:51:00 | NOAA-20 | SANTA TEREZINHA DE GOIÁS | GOIÁS | Brasil | 5219704 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 1dedd06b-9e78-3e45-beff-102c3e556296 | -11.87006 | -45.02734 | 2025-10-02 04:51:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 616afcb8-7078-35fb-8a17-bc54ee5dc778 | -13.86134 | -47.95539 | 2025-10-02 04:51:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 192c70ce-5371-3a09-9259-440caf9a3bf2 | -13.94901 | -48.13368 | 2025-10-02 04:51:00 | NOAA-20 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 898b152b-8597-3cc1-947c-e7d7cdf3dab7 | -13.14593 | -47.85258 | 2025-10-02 04:51:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 367dbfea-6702-3a1c-a8cb-ba7058120918 | -10.21772 | -50.28647 | 2025-10-02 04:51:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 4b46a084-357d-3710-ae40-92fbac057054 | -14.40298 | -46.08302 | 2025-10-02 04:51:00 | NOAA-20 | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 3974cc25-91f9-32e8-b028-12b7d0fb1258 | -11.18168 | -47.26008 | 2025-10-02 04:51:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 0df6760b-16ed-3d12-b9e9-fee1108788b7 | -11.58936 | -50.17155 | 2025-10-02 04:51:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 4.5 |
| ee8a8336-c25f-3523-9293-741dda56f218 | -14.64681 | -48.1511 | 2025-10-02 04:51:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| c30c37eb-4fd6-31f7-82f1-0b50589ce338 | -9.56466 | -50.94092 | 2025-10-02 04:51:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 89e52686-93b1-3dd4-ba0c-0acaa104cac8 | -14.61138 | -51.33505 | 2025-10-02 04:51:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 8c910d15-bb7d-3852-a168-5333dd0477b6 | -11.2694 | -47.82397 | 2025-10-02 04:51:00 | NOAA-20 | SANTA ROSA DO TOCANTINS | TOCANTINS | Brasil | 1718907 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 1c36c0d8-3209-3450-bdd5-b3f7b0b98b3b | -11.17013 | -47.2797 | 2025-10-02 04:51:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 11.3 |
| 8b0dbf23-1576-3d61-bca9-ffda20a9ab50 | -9.92816 | -50.48927 | 2025-10-02 04:51:00 | NOAA-20 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 47f961a5-260a-3dc6-bbea-445a1db85c48 | -15.59685 | -46.92036 | 2025-10-02 04:51:00 | NOAA-20 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| b9bfb941-04ef-3b02-be28-c78ad9cd068e | -13.30717 | -48.7017 | 2025-10-02 04:51:00 | NOAA-20 | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 95ac3c2f-2192-327f-a6be-1caba307cd95 | -13.50816 | -48.20435 | 2025-10-02 04:51:00 | NOAA-20 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 0b6e5f25-cc05-3c76-8f49-fb627b9f386e | -13.86224 | -47.95704 | 2025-10-02 04:51:00 | NOAA-20 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 24fa0970-6a46-339f-a633-d9a42ee433fd | -13.74817 | -48.01 | 2025-10-02 04:51:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 4a0abfa1-7306-3b10-a7d9-28864a0398aa | -14.4299 | -46.10986 | 2025-10-02 04:51:00 | NOAA-20 | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 9b9e09b7-0b33-362c-9637-9cb91e4b2f4a | -14.42711 | -46.0998 | 2025-10-02 04:51:00 | NOAA-20 | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| da57c68a-37c2-3f36-8650-787f6a134f44 | -11.43703 | -43.89293 | 2025-10-02 04:51:00 | NOAA-20 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| fad4aa8a-7df1-3986-9f0a-c5e365805692 | -11.46298 | -44.96476 | 2025-10-02 04:51:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| ff9aab06-3f9f-3574-afe9-a1d3c1efbf7f | -14.6917 | -48.2597 | 2025-10-02 04:51:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 6911c032-c32e-3ad7-b43a-2b00e12ba0b3 | -14.60162 | -48.32952 | 2025-10-02 04:51:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 97943e86-b0f8-3b19-bf0a-a9c11d0e27c1 | -15.25655 | -56.77373 | 2025-10-02 04:51:00 | NOAA-20 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 6b7d76cc-dee9-34ee-a43a-1a31c640fca7 | -11.86305 | -48.01885 | 2025-10-02 04:51:00 | NOAA-20 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| cd9f0c6b-402c-3251-aaaf-915b7282c442 | -13.3262 | -47.20861 | 2025-10-02 04:51:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 4.1 |
| b770d709-f08b-3288-a4ec-8b41c84d8d7a | -10.91946 | -44.31515 | 2025-10-02 04:51:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 388117f2-93dc-3f98-96d5-8e8301eca4a8 | -12.81922 | -47.05956 | 2025-10-02 04:51:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 4.3 |
| eb600524-bfa0-3b71-9c23-51e769e49ac8 | -9.9253 | -43.73667 | 2025-10-02 04:51:00 | NOAA-20 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 37.4 |
| c8bfd337-f0f5-3511-8f24-ea43ba33193d | -15.26258 | -49.31324 | 2025-10-02 04:51:00 | NOAA-20 | GOIANÉSIA | GOIÁS | Brasil | 5208608 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 9d291d26-174f-3937-a237-33337a50b9eb | -12.77642 | -44.91135 | 2025-10-02 04:51:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| a5b0e6b0-cb52-31ec-acc0-56ff070e7307 | -14.36389 | -45.94649 | 2025-10-02 04:51:00 | NOAA-20 | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| bdc50876-eb49-3f1e-b241-def9ee76147a | -11.8005 | -44.99651 | 2025-10-02 04:51:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 809ccf91-3655-3eed-a779-d4d7101d3831 | -11.58984 | -45.05633 | 2025-10-02 04:51:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 796b8444-55f7-3fda-9cdb-846857985e42 | -11.86643 | -45.0148 | 2025-10-02 04:51:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 6fcea0c8-8e7b-3827-affb-6ef956fa06a2 | -13.29297 | -47.2502 | 2025-10-02 04:51:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 6726756d-cd6e-342a-9b20-752730b0fbfd | -15.31389 | -46.29316 | 2025-10-02 04:51:00 | NOAA-20 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 750fedb4-684d-3faa-a95d-23b69fa4fa6e | -12.26418 | -47.81739 | 2025-10-02 04:51:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 9f3aa89e-a3cd-361a-a794-a8db7a69de85 | -13.96594 | -48.12406 | 2025-10-02 04:51:00 | NOAA-20 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 6f83bccf-455a-3f37-844e-4a4be57b0c11 | -13.40423 | -44.39392 | 2025-10-02 04:51:00 | NOAA-20 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 2aec0969-948c-3f91-a30c-a92a342a2771 | -9.93745 | -43.77746 | 2025-10-02 04:51:00 | NOAA-20 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 8ac06ac7-92ac-3052-8221-93ed2939c183 | -10.34932 | -48.20105 | 2025-10-02 04:51:00 | NOAA-20 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| fc5cccff-1c6d-3fce-a51e-20766e3788f7 | -13.3679 | -46.34251 | 2025-10-02 04:51:00 | NOAA-20 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 7.6 |
| 3d7a9620-7492-3ee0-9026-fb8e0348d7d2 | -10.22552 | -50.28339 | 2025-10-02 04:51:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 1f4f2d4f-a4e1-3f5d-a762-f33114ab05fb | -14.484 | -48.43937 | 2025-10-02 04:51:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 8724ebdd-746a-3f02-b1ad-10052b25a2c0 | -12.5901 | -49.90424 | 2025-10-02 04:51:00 | NOAA-20 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| bd8f90b4-4836-3ea3-a188-12aa313b0643 | -13.22074 | -48.51516 | 2025-10-02 04:51:00 | NOAA-20 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 66119496-b38c-3cf7-8efb-8c8b09def0ae | -15.22632 | -50.10796 | 2025-10-02 04:51:00 | NOAA-20 | ARAGUAPAZ | GOIÁS | Brasil | 5202155 | 52 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 0f3ce6cc-640a-35fe-b63a-be5df62e0521 | -15.3501 | -46.28582 | 2025-10-02 04:51:00 | NOAA-20 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 2cb42174-4d08-305b-9cd2-2f0c6f1315ca | -13.87118 | -47.94818 | 2025-10-02 04:51:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 0fd44742-1b67-39b3-947b-cd9735489a53 | -15.27799 | -56.79396 | 2025-10-02 04:51:00 | NOAA-20 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| d7c1d072-9aec-308c-bacd-993208c8c4bf | -13.95328 | -48.1345 | 2025-10-02 04:51:00 | NOAA-20 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 229b6c00-7a60-30c5-9821-1e7e77859ec7 | -11.00464 | -46.58911 | 2025-10-02 04:51:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 86fb7117-4076-3ff7-9907-d5a1033016aa | -13.96441 | -48.1358 | 2025-10-02 04:51:00 | NOAA-20 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 20.3 |
| 09d24568-a670-375c-ac6f-8426796a6e3c | -9.81436 | -48.2815 | 2025-10-02 04:51:00 | NOAA-20 | LAJEADO | TOCANTINS | Brasil | 1712009 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 53ae71c0-28fc-3b44-ad49-a62d6c86a7af | -13.79718 | -48.03918 | 2025-10-02 04:51:00 | NOAA-20 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| fb7f5341-db10-3a3b-8dc4-19eb5808a2a0 | -15.15571 | -52.79869 | 2025-10-02 04:51:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| bbbc3bc5-ad95-3f30-a962-0ebc9d548d91 | -12.7943 | -46.85572 | 2025-10-02 04:51:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| aad55e06-9e38-3f70-84d9-6a76c2661377 | -16.36093 | -47.03453 | 2025-10-02 04:51:00 | NOAA-20 | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| b884dcaf-28c6-3a9d-931b-468f3497b5cc | -10.19123 | -50.27922 | 2025-10-02 04:51:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| eb44b223-318c-3ed9-b715-d93e109e43c5 | -11.83113 | -45.00343 | 2025-10-02 04:51:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |


[Clique aqui para ver as próximas entradas](README123.md)
