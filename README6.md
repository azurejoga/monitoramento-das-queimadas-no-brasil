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
| af43d487-765d-3358-8652-db717940eec9 | -14.39806 | -48.06279 | 2026-07-31 03:55:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 31cd984f-9a5b-3374-aa34-9c9050b35ac4 | -14.37047 | -48.03638 | 2026-07-31 03:55:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 17b119ed-bc54-3af2-942a-75aceb0fed88 | -12.61332 | -44.63225 | 2026-07-31 03:55:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 4.1 |
| f268d730-d4f1-329c-bec7-c4aab6407c28 | -13.96227 | -41.5105 | 2026-07-31 03:55:00 | NOAA-20 | BRUMADO | BAHIA | Brasil | 2904605 | 29 | 33 | nan | nan | nan | Caatinga | 0.3 |
| 9eddf981-353d-3182-b10a-aa4c15910d07 | -14.38652 | -48.06592 | 2026-07-31 03:55:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 802339e3-fc9b-3149-9754-1eababac2579 | -14.38083 | -48.06709 | 2026-07-31 03:55:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 20185ba6-7b78-315a-9925-fefd460c1236 | -17.9392 | -44.32616 | 2026-07-31 03:55:00 | NOAA-20 | BUENÓPOLIS | MINAS GERAIS | Brasil | 3109204 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 4cf1a46d-6327-37a7-ac6f-3ac37337ca16 | -13.94215 | -46.18579 | 2026-07-31 03:55:00 | NOAA-20 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| d7542f35-2494-3db0-b287-876028fcb0e7 | -14.36403 | -48.04137 | 2026-07-31 03:55:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 693aba38-e310-3a56-8b4c-04957d5fc549 | -14.38136 | -48.06115 | 2026-07-31 03:55:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 12f88255-2721-3c9d-878e-80c1cb464974 | -12.61841 | -44.62884 | 2026-07-31 03:55:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| a6782c92-ca74-3f86-9d02-ce38bafdc6ba | -12.84801 | -44.39103 | 2026-07-31 03:55:00 | NOAA-20 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 2be3a41e-8a3c-3b96-860c-e66962844460 | -14.38261 | -48.055 | 2026-07-31 03:55:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 0e875a21-b829-36de-8565-68e087129e6c | -12.33952 | -48.21841 | 2026-07-31 03:55:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| b4d57e8e-84c7-33cc-add8-f8433e287dd9 | -12.45946 | -43.52868 | 2026-07-31 03:55:00 | NOAA-20 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| f4614142-86b0-3316-83a4-4eee2a2f8f3f | -12.59247 | -44.62394 | 2026-07-31 03:55:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| bd3610b1-0dca-359d-bad3-2dc996d3f60c | -12.03895 | -40.67459 | 2026-07-31 03:55:00 | NOAA-20 | MUNDO NOVO | BAHIA | Brasil | 2922102 | 29 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 0768a705-be8f-38c3-aa72-361d47049ee3 | -14.39947 | -48.02752 | 2026-07-31 03:55:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 9d69810f-6e30-35d3-9cd9-a9195b94ea02 | -14.37759 | -48.05569 | 2026-07-31 03:55:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.4 |
| fb4927d9-6fe9-3992-b382-5058b6d398cd | -13.95546 | -49.15255 | 2026-07-31 03:55:00 | NOAA-20 | MARA ROSA | GOIÁS | Brasil | 5212808 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 0c6065ee-6a2a-3f73-8831-7fefc1c90dc9 | -14.78054 | -46.81133 | 2026-07-31 03:55:00 | NOAA-20 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 07411e16-49f9-3743-a42b-b08799c31112 | -11.83317 | -45.60271 | 2026-07-31 03:55:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 8a2458aa-a3e0-3108-aea9-2d7b1dab7acd | -14.36007 | -48.06146 | 2026-07-31 03:55:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 6e8745e5-6751-3d3f-9268-0e0fa67189ad | -14.37497 | -48.06907 | 2026-07-31 03:55:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 1f055be5-b5b9-3392-bc9c-009e951d18b8 | -14.06412 | -46.21755 | 2026-07-31 03:55:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 85cdd636-a2a3-3f9b-ad66-7f20c726cb0f | -14.37315 | -48.05051 | 2026-07-31 03:55:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 3077f08d-5715-3ed7-9743-699c770777f4 | -12.60421 | -44.60855 | 2026-07-31 03:55:00 | NOAA-20 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 71d060ec-d6be-38ec-b82c-be8242e2e1f7 | -18.12048 | -44.63351 | 2026-07-31 03:55:00 | NOAA-20 | CORINTO | MINAS GERAIS | Brasil | 3119104 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 8b7b4ca5-952a-3c5c-a64f-b68db0e99004 | -12.10011 | -44.12468 | 2026-07-31 03:55:00 | NOAA-20 | CRISTÓPOLIS | BAHIA | Brasil | 2909703 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 87b7427f-2d41-342d-bf38-aa5e725e4f71 | -17.53636 | -45.30457 | 2026-07-31 03:55:00 | NOAA-20 | BURITIZEIRO | MINAS GERAIS | Brasil | 3109402 | 31 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 695c6319-82af-37b3-bb6a-77f133fbfd56 | -12.61006 | -44.60092 | 2026-07-31 03:55:00 | NOAA-20 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| d5d9488d-6395-3aca-87be-516618a0d9c4 | -16.40012 | -53.33671 | 2026-07-31 03:55:00 | NOAA-20 | GUIRATINGA | MATO GROSSO | Brasil | 5104203 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| e68249aa-9185-3309-af22-55918d9120a5 | -14.39671 | -48.06974 | 2026-07-31 03:55:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 7.7 |
| a9174d43-05dc-36b5-abbb-1d26f6b6027b | -18.0244 | -44.36615 | 2026-07-31 03:55:00 | NOAA-20 | BUENÓPOLIS | MINAS GERAIS | Brasil | 3109204 | 31 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 0c2de254-57c7-325a-885b-edf34e643a6a | -18.02053 | -44.36529 | 2026-07-31 03:55:00 | NOAA-20 | BUENÓPOLIS | MINAS GERAIS | Brasil | 3109204 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| fb967048-233d-3ee6-8db0-96e06d8d20d7 | -14.82821 | -48.53118 | 2026-07-31 03:55:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| d72905b1-201d-3827-89eb-964ad87c7da9 | -12.61083 | -44.59669 | 2026-07-31 03:55:00 | NOAA-20 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 75356974-5029-3bcd-ae99-986cc7bb11b7 | -14.83054 | -48.51986 | 2026-07-31 03:55:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 503f1d7c-4800-3734-96c4-34f5fba76241 | -17.93905 | -44.32375 | 2026-07-31 03:55:00 | NOAA-20 | BUENÓPOLIS | MINAS GERAIS | Brasil | 3109204 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| f7c91ad6-6472-314d-bcfc-c78afb5a5241 | -11.83408 | -45.59768 | 2026-07-31 03:55:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 949cc26c-b3ed-3454-8353-11ea5983484c | -12.59835 | -44.61621 | 2026-07-31 03:55:00 | NOAA-20 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| d287e6f3-3391-3f74-b1c5-eaec79b2925f | -14.3757 | -48.06533 | 2026-07-31 03:55:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 8.3 |
| 2c359634-265f-30e6-968d-466fb1fa7256 | -14.3615 | -48.05419 | 2026-07-31 03:55:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 8f529050-bde3-318a-b5c5-2b1802313cb1 | -14.39215 | -48.06184 | 2026-07-31 03:55:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 7.5 |
| d9194a5f-27ae-3773-a6b1-01050921dfa7 | -14.37418 | -48.0731 | 2026-07-31 03:55:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 752deebe-7102-378c-95c8-bb137e4067e9 | -16.10143 | -47.90855 | 2026-07-31 03:55:00 | NOAA-20 | CIDADE OCIDENTAL | GOIÁS | Brasil | 5205497 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 36ea4452-576e-3727-9969-78403b605c7a | -12.60899 | -44.63147 | 2026-07-31 03:55:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 4.1 |
| ba00b1e9-fedc-32cb-8121-1d5bf2527d2a | -12.61437 | -44.60178 | 2026-07-31 03:55:00 | NOAA-20 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| ae86e4ac-faf1-36fb-83b0-495c5dd2dbab | -23.45972 | -47.38356 | 2026-07-31 03:57:00 | NOAA-20 | SOROCABA | SÃO PAULO | Brasil | 3552205 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 613f054d-3446-395b-b56b-6151275ab387 | -18.80779 | -53.14812 | 2026-07-31 03:57:00 | NOAA-20 | COSTA RICA | MATO GROSSO DO SUL | Brasil | 5003256 | 50 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 3479f63e-d3b3-38e2-8211-2d254919b4e0 | -22.15445 | -56.01593 | 2026-07-31 03:57:00 | NOAA-20 | ANTÔNIO JOÃO | MATO GROSSO DO SUL | Brasil | 5000906 | 50 | 33 | nan | nan | nan | Cerrado | 4.5 |
| ac875bd2-d701-3bc7-a298-c220500893ff | -18.81347 | -53.14424 | 2026-07-31 03:57:00 | NOAA-20 | COSTA RICA | MATO GROSSO DO SUL | Brasil | 5003256 | 50 | 33 | nan | nan | nan | Cerrado | 1.8 |
| d2ba2877-593a-3309-8d3e-d66d1a11582c | -22.51956 | -44.20584 | 2026-07-31 03:57:00 | NOAA-20 | BARRA MANSA | RIO DE JANEIRO | Brasil | 3300407 | 33 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 2003282f-24ee-3058-9768-116c5dc22831 | -22.16125 | -56.01905 | 2026-07-31 03:57:00 | NOAA-20 | ANTÔNIO JOÃO | MATO GROSSO DO SUL | Brasil | 5000906 | 50 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 11187949-0151-3a3b-8dfd-3442141341e8 | -20.5576 | -41.98967 | 2026-07-31 03:57:00 | NOAA-20 | CAPARAÓ | MINAS GERAIS | Brasil | 3112109 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 99d46cc8-040e-33a1-a5f8-0e6acaa4ea02 | -21.44809 | -43.78339 | 2026-07-31 03:57:00 | NOAA-20 | ANTÔNIO CARLOS | MINAS GERAIS | Brasil | 3102902 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 35ae6342-0e3d-32e2-aae1-51ed82a93c17 | -21.36918 | -44.64639 | 2026-07-31 03:57:00 | NOAA-20 | ITUTINGA | MINAS GERAIS | Brasil | 3134509 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| b17c1ba0-48d8-34a0-aeab-ae7f2fcc1dbb | -18.80695 | -53.14259 | 2026-07-31 03:57:00 | NOAA-20 | COSTA RICA | MATO GROSSO DO SUL | Brasil | 5003256 | 50 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 0e19cac8-a0d1-3530-958a-f851466d94e7 | -23.45637 | -47.38395 | 2026-07-31 03:57:00 | NOAA-20 | SOROCABA | SÃO PAULO | Brasil | 3552205 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| d3c2ede6-9beb-3b53-81a8-57336d1c9c9a | -18.93407 | -47.45742 | 2026-07-31 03:57:00 | NOAA-20 | MONTE CARMELO | MINAS GERAIS | Brasil | 3143104 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| eacfd55e-4e2e-3cbe-a0dc-dac5f82999fc | -19.99346 | -44.30494 | 2026-07-31 03:57:00 | NOAA-20 | JUATUBA | MINAS GERAIS | Brasil | 3136652 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| 0d633537-ba5d-386f-bbe8-097dd5789e75 | -22.15925 | -56.02669 | 2026-07-31 03:57:00 | NOAA-20 | ANTÔNIO JOÃO | MATO GROSSO DO SUL | Brasil | 5000906 | 50 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 8c764e5b-94f0-3d65-98b8-2423fada8ac7 | -20.11077 | -50.74468 | 2026-07-31 03:57:00 | NOAA-20 | SANTA RITA D'OESTE | SÃO PAULO | Brasil | 3547403 | 35 | 33 | nan | nan | nan | Mata Atlântica | 7.3 |
| f37de741-a186-30df-9082-2cd2313e45a0 | -18.37262 | -47.20092 | 2026-07-31 03:57:00 | NOAA-20 | COROMANDEL | MINAS GERAIS | Brasil | 3119302 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 2a53f895-8506-34e8-aa92-c4ffed107460 | -21.73702 | -45.26875 | 2026-07-31 03:57:00 | NOAA-20 | TRÊS CORAÇÕES | MINAS GERAIS | Brasil | 3169307 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| be636ade-a172-3026-8b77-691fdbe3d8e5 | -22.15934 | -56.0173 | 2026-07-31 03:57:00 | NOAA-20 | ANTÔNIO JOÃO | MATO GROSSO DO SUL | Brasil | 5000906 | 50 | 33 | nan | nan | nan | Cerrado | 11.5 |
| 9310736e-e0a9-36b5-ad06-da213c203650 | -18.8091 | -53.14245 | 2026-07-31 03:57:00 | NOAA-20 | COSTA RICA | MATO GROSSO DO SUL | Brasil | 5003256 | 50 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 8722b225-64a0-3c33-876b-622d79dd6823 | -20.68944 | -45.33805 | 2026-07-31 03:57:00 | NOAA-20 | CANDEIAS | MINAS GERAIS | Brasil | 3112000 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 2544c1fc-dc56-33df-8f25-edd57ebcb833 | -20.69177 | -45.34006 | 2026-07-31 03:57:00 | NOAA-20 | CANDEIAS | MINAS GERAIS | Brasil | 3112000 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| e2750893-96c7-33ad-8d58-78f70add1c62 | -20.46874 | -43.34388 | 2026-07-31 03:57:00 | NOAA-20 | MARIANA | MINAS GERAIS | Brasil | 3140001 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.4 |
| 0bf8bbc1-bfd2-3206-bf50-6a64f36e658d | -19.16066 | -47.31852 | 2026-07-31 03:57:00 | NOAA-20 | PERDIZES | MINAS GERAIS | Brasil | 3149804 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 76851e15-b33c-3fda-9a5f-5a67d52d683f | -22.16419 | -56.02813 | 2026-07-31 03:57:00 | NOAA-20 | ANTÔNIO JOÃO | MATO GROSSO DO SUL | Brasil | 5000906 | 50 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 7a0950b9-943e-396a-b7e1-168c9a850c0a | -18.80559 | -53.14829 | 2026-07-31 03:57:00 | NOAA-20 | COSTA RICA | MATO GROSSO DO SUL | Brasil | 5003256 | 50 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 3fe5f508-4ec3-3631-a5fb-754bc5a613b9 | -21.44888 | -43.77898 | 2026-07-31 03:57:00 | NOAA-20 | ANTÔNIO CARLOS | MINAS GERAIS | Brasil | 3102902 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 112b419c-ce50-3566-b2c9-91519ffa6071 | -19.9926 | -44.3097 | 2026-07-31 03:57:00 | NOAA-20 | JUATUBA | MINAS GERAIS | Brasil | 3136652 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 0a4c8ea6-5776-30a2-8de8-76b174aa4aaa | -22.15739 | -56.02495 | 2026-07-31 03:57:00 | NOAA-20 | ANTÔNIO JOÃO | MATO GROSSO DO SUL | Brasil | 5000906 | 50 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 73bb0698-04c2-33f1-b4e9-08ab94e8b512 | -20.10991 | -50.74861 | 2026-07-31 03:57:00 | NOAA-20 | SANTA RITA D'OESTE | SÃO PAULO | Brasil | 3547403 | 35 | 33 | nan | nan | nan | Mata Atlântica | 7.3 |
| 3193f60b-9710-3748-8caf-b9705d4544a1 | -14.3855 | -48.071 | 2026-07-31 04:00:00 | GOES-19 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 77.2 |
| 704b678a-d4a1-3ba9-a28f-9fd1834fdaa9 | -14.386 | -48.0485 | 2026-07-31 04:00:00 | GOES-19 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 65.5 |
| 86491a6c-da0a-3c8e-bb6b-dda3b65645bd | -28.73662 | -49.35551 | 2026-07-31 04:00:00 | NOAA-20 | CRICIÚMA | SANTA CATARINA | Brasil | 4204608 | 42 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| a074c664-5dca-3958-abe7-8453e7710bfb | -3.96497 | -48.12451 | 2026-07-31 04:38:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 6.4 |
| 9300fee4-7adc-38ae-be02-b25aa5f1baed | -3.05281 | -48.74085 | 2026-07-31 04:38:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| f920fd11-7a3b-33ae-8fee-23f8c8019461 | 1.0984 | -60.50395 | 2026-07-31 04:38:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 408e76ee-a023-32cf-91f8-bfeea9c620d4 | -4.16105 | -48.93979 | 2026-07-31 04:38:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 65353d85-f99c-339e-8cb5-c1cd40ee3590 | -2.89043 | -48.01385 | 2026-07-31 04:38:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 335ec87a-1939-3bde-97d1-d64a00ebdd87 | -4.03123 | -43.27037 | 2026-07-31 04:38:00 | NOAA-21 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| a14a0b67-aa8e-34c6-951c-625f02068005 | -4.37025 | -47.76618 | 2026-07-31 04:38:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 0a727e3f-7768-3ffb-baa2-358e2fb99cb9 | -3.96443 | -48.12799 | 2026-07-31 04:38:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 12.9 |
| bf6b97f8-a1f0-3bd1-8560-96257b364903 | -2.64469 | -47.97609 | 2026-07-31 04:38:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| a675db8e-b33c-3f45-8a1f-2a44ac684810 | -4.95232 | -45.14766 | 2026-07-31 04:38:00 | NOAA-21 | LAGO DA PEDRA | MARANHÃO | Brasil | 2105708 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 5657b81b-ebb1-38e2-a124-e1cf18a5c7dd | -3.11457 | -47.90681 | 2026-07-31 04:38:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| e87e48a3-1ca1-36a9-b6bf-5a9a9fc182d1 | -4.16696 | -48.77175 | 2026-07-31 04:38:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 38d6eadf-748b-3693-a389-64b8191ad16a | -3.67436 | -50.94977 | 2026-07-31 04:38:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 33e6c873-7bc2-3329-8a8e-ae225bc1489f | -1.57404 | -47.75252 | 2026-07-31 04:38:00 | NOAA-21 | SÃO MIGUEL DO GUAMÁ | PARÁ | Brasil | 1507607 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 553be10c-c643-33b2-b225-ec41f3e1805f | -5.60799 | -44.02846 | 2026-07-31 04:38:00 | NOAA-21 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 539f03d2-ba37-388d-b7f1-84d2ca14ac40 | 1.09488 | -60.50363 | 2026-07-31 04:38:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 4b1a2989-0d74-363f-b88e-208be8b77ffc | -2.90983 | -40.39604 | 2026-07-31 04:38:00 | NOAA-21 | CRUZ | CEARÁ | Brasil | 2304251 | 23 | 33 | nan | nan | nan | Caatinga | 2.3 |
| ad967442-cd4d-3222-b518-5d727559f263 | -3.11402 | -47.91029 | 2026-07-31 04:38:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 8.3 |
| 8dc23890-541c-3ad9-b78e-f014a94ba00f | -4.90548 | -43.47585 | 2026-07-31 04:38:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 8bd848f6-1103-349a-a4e8-0752c83a081e | 1.10424 | -60.52023 | 2026-07-31 04:38:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 4.0 |


[Clique aqui para ver as próximas entradas](README7.md)
