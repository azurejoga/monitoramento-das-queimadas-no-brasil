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
| 64cdde9a-e873-3820-a32f-cb0b4bba6c68 | -29.50096 | -54.76159 | 2026-01-20 04:46:00 | NOAA-21 | JAGUARI | RIO GRANDE DO SUL | Brasil | 4311106 | 43 | 33 | nan | nan | nan | Pampa | 0.3 |
| 347e9dd2-290e-380c-abd1-bf4f3e2f95a1 | -27.56576 | -48.65958 | 2026-01-20 04:46:00 | NOAA-21 | SÃO JOSÉ | SANTA CATARINA | Brasil | 4216602 | 42 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 620ad098-43db-3264-b0d0-8b59c5b84191 | -31.55169 | -53.74026 | 2026-01-20 04:46:00 | NOAA-21 | CANDIOTA | RIO GRANDE DO SUL | Brasil | 4304358 | 43 | 33 | nan | nan | nan | Pampa | 1.1 |
| 6b869623-56f4-3fc7-a633-dc125131293d | -29.49802 | -54.76148 | 2026-01-20 04:46:00 | NOAA-21 | JAGUARI | RIO GRANDE DO SUL | Brasil | 4311106 | 43 | 33 | nan | nan | nan | Pampa | 0.6 |
| 642a35c3-d66c-3cbf-92d0-ee76bdb99c1b | 2.67207 | -60.08172 | 2026-01-20 05:08:00 | NPP-375D | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 1.7 |
| d765e4de-9561-3c06-b810-d4b009337246 | 2.05182 | -60.8672 | 2026-01-20 05:08:00 | NPP-375D | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 2.2 |
| f0120cee-6545-3c2d-8631-6caa150208cc | -1.36487 | -46.64067 | 2026-01-20 05:08:00 | NPP-375D | BRAGANÇA | PARÁ | Brasil | 1501709 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 6e8254d3-e369-38de-93dc-9fcc8168c6c7 | 1.13506 | -60.52239 | 2026-01-20 05:08:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 7ac65f41-7188-3152-8665-3b21e8fe2709 | 1.1313 | -60.5274 | 2026-01-20 05:08:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 8d378c10-b8b5-3689-8fe1-1d6543eaabc7 | 2.56232 | -60.38617 | 2026-01-20 05:08:00 | NPP-375D | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 987fe0a3-b0ac-309f-a8f9-f42ebba941b0 | 0.75621 | -59.66079 | 2026-01-20 05:08:00 | NPP-375D | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 507cc2cb-4081-376e-be03-c14474c946fd | 3.20216 | -60.38305 | 2026-01-20 05:08:00 | NPP-375D | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 02ff10b8-6d62-3bd9-829a-dc932255357d | 1.13064 | -60.52309 | 2026-01-20 05:08:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 3c3160f7-286b-3c69-8245-be60eef7d6e9 | 2.68276 | -60.09304 | 2026-01-20 05:08:00 | NPP-375D | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 80024459-626c-30a4-b799-0c9ce0cce443 | 2.55836 | -59.98213 | 2026-01-20 05:08:00 | NPP-375D | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 2.8 |
| e125f798-4af9-328e-aa60-2b95930b7768 | 3.32211 | -59.96501 | 2026-01-20 05:08:00 | NPP-375D | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 1bb1844e-0d5a-3a88-9573-55771acb7ba7 | 2.68403 | -60.1015 | 2026-01-20 05:08:00 | NPP-375D | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 2.9 |
| d5bf8fcb-d51b-3fc5-8150-cf5a50735a88 | -1.35984 | -46.63995 | 2026-01-20 05:08:00 | NPP-375D | BRAGANÇA | PARÁ | Brasil | 1501709 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c2d91c14-9658-33a4-b09d-ac5dce7c885f | 1.13881 | -60.5174 | 2026-01-20 05:08:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 0.8 |
| acaac31a-c639-396d-966d-1b925759d192 | 2.75944 | -60.72615 | 2026-01-20 05:08:00 | NPP-375D | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 1.6 |
| bd67310e-9b05-3ff9-bde1-bc3b52eeca94 | -2.35787 | -51.89472 | 2026-01-20 05:08:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 1328589f-be4c-30de-9456-92eb7ba52237 | 1.13572 | -60.5267 | 2026-01-20 05:08:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 1dcc904e-a36d-3291-ab72-5fe3cad6ad85 | 1.1344 | -60.51809 | 2026-01-20 05:08:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 0.8 |
| ba14a358-96b0-39ff-a8e0-379376c3d3e8 | 1.12687 | -60.52808 | 2026-01-20 05:08:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 2.2 |
| ef0593e7-c8f6-35e9-a60c-206b6e592153 | -2.4584 | -48.06158 | 2026-01-20 05:08:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| da5cb462-7e55-3b3a-a5a2-b3aa368a815d | -2.35852 | -51.89056 | 2026-01-20 05:08:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| f10b7ffb-27ee-3d9e-b3d5-53c9453cc8ce | 3.31206 | -59.98812 | 2026-01-20 05:08:00 | NPP-375D | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 9718a992-7a93-3c50-9f5b-48330f0ee3ed | -2.35555 | -51.88586 | 2026-01-20 05:08:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 6a41e7b0-47c3-3295-8f3f-6f331d2a28ef | 0.75561 | -59.65707 | 2026-01-20 05:08:00 | NPP-375D | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 492e815b-937a-3b10-86bd-97b80135e40c | 2.55401 | -59.9828 | 2026-01-20 05:08:00 | NPP-375D | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 43680d22-b06b-3e2d-9f1f-60dd849c8f22 | -2.36215 | -51.89112 | 2026-01-20 05:08:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 07365d67-2c41-3c24-8375-f7dffe921ee6 | 2.55115 | -60.58513 | 2026-01-20 05:08:00 | NPP-375D | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 701b2ee1-7bfd-3d70-a44e-e4f2a44a60c3 | 3.31269 | -59.99231 | 2026-01-20 05:08:00 | NPP-375D | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 64e9225c-7403-39d9-a49b-647dd9e176bf | 2.68339 | -60.09726 | 2026-01-20 05:08:00 | NPP-375D | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 2.9 |
| d7b2c2fe-6b31-3120-8659-df9b0d103c13 | 1.47011 | -59.9587 | 2026-01-20 05:08:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 81f45b38-1861-3ec9-88ae-5d3d880543f4 | 2.5668 | -60.38551 | 2026-01-20 05:08:00 | NPP-375D | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 6d4e212e-00cb-38f7-8769-7cc28fe194a3 | 2.04726 | -60.86812 | 2026-01-20 05:08:00 | NPP-375D | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 119b0a20-faa2-3330-ad7f-fcc044318125 | -6.97426 | -42.87259 | 2026-01-20 05:10:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 4.7 |
| 7c0d0641-856f-3a61-9da6-90b97d4821e2 | -6.98811 | -42.87452 | 2026-01-20 05:10:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 3.3 |
| a33b7601-5843-36b0-b50a-94694c36b073 | -9.10613 | -50.53433 | 2026-01-20 05:10:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| f5cb9fb9-ccff-31db-86b7-88253769f77f | -6.59498 | -44.32477 | 2026-01-20 05:10:00 | NPP-375D | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| d3f102a9-ba1e-31a4-b171-727b64822094 | -9.1067 | -50.53027 | 2026-01-20 05:10:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| ee588526-eee0-3461-b2b8-ed91da61f38a | -9.11103 | -50.53086 | 2026-01-20 05:10:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 1bed1560-dd25-3078-935c-824b24552798 | -6.97512 | -42.86605 | 2026-01-20 05:10:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 4.4 |
| 128b72df-bc02-3cb7-af30-b71e972179ec | -6.9734 | -42.8791 | 2026-01-20 05:10:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 4.7 |
| 1ed42afe-2924-36cb-bb7a-8cbef10890a7 | -9.11046 | -50.53491 | 2026-01-20 05:10:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 4238877d-5063-34da-bd0b-bd88c388394d | -6.99505 | -42.87534 | 2026-01-20 05:10:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 9.8 |
| ec8c8b3e-0cc4-3852-ab4a-609670b1bfa3 | -10.31629 | -59.05577 | 2026-01-20 05:12:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 212d6dbb-e0e5-36fb-9017-88898cf0c777 | -10.31217 | -59.05906 | 2026-01-20 05:12:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| f373f699-c9ac-3258-afe5-b299d50d9c13 | -10.31565 | -59.05965 | 2026-01-20 05:12:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| af6e7236-f32c-3e5a-8c0a-4911540b1efa | -19.43318 | -57.22351 | 2026-01-20 05:14:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 7.1 |
| e38c0bb3-4def-3731-83c8-5de25ae9c540 | -21.94637 | -52.90717 | 2026-01-20 05:14:00 | NPP-375D | ANAURILÂNDIA | MATO GROSSO DO SUL | Brasil | 5000807 | 50 | 33 | nan | nan | nan | Cerrado | 0.9 |
| e00121c7-9f12-33c8-ada4-b5f3c617ae61 | -22.88138 | -52.27732 | 2026-01-20 05:14:00 | NPP-375D | SÃO JOÃO DO CAIUÁ | PARANÁ | Brasil | 4124905 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 8822b2b9-9ba8-3fc8-a5de-e14df4c522e6 | -20.70632 | -48.82452 | 2026-01-20 05:14:00 | NPP-375D | OLÍMPIA | SÃO PAULO | Brasil | 3533908 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.3 |
| f7d37487-be08-38bd-8282-934bd1516a64 | -21.25888 | -53.16415 | 2026-01-20 05:14:00 | NPP-375D | RIBAS DO RIO PARDO | MATO GROSSO DO SUL | Brasil | 5007109 | 50 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 032f9af0-80a3-3265-b69d-228b0a5bc764 | -19.43946 | -57.22853 | 2026-01-20 05:14:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 0.8 |
| 5410a9af-aa74-37f3-8464-5693a85ad392 | -19.43033 | -57.21907 | 2026-01-20 05:14:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 7.1 |
| a57fd52e-edb6-3e29-980c-05a878ee2976 | -19.29583 | -53.17664 | 2026-01-20 05:14:00 | NPP-375D | PARAÍSO DAS ÁGUAS | MATO GROSSO DO SUL | Brasil | 5006275 | 50 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 0b446128-3404-3f37-a628-d753e1c4aee3 | -20.7067 | -48.82051 | 2026-01-20 05:14:00 | NPP-375D | OLÍMPIA | SÃO PAULO | Brasil | 3533908 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.4 |
| f5b855d4-d9cd-3847-82b0-0c00e025292f | -18.81625 | -51.61225 | 2026-01-20 05:14:00 | NPP-375D | ITAJÁ | GOIÁS | Brasil | 5210802 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 99242ab9-fb28-35f9-add5-8bdb0b444d7e | -19.4366 | -57.22408 | 2026-01-20 05:14:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.1 |
| ce54a864-3496-3e14-b70e-2774ab7e2593 | -23.69348 | -55.26483 | 2026-01-20 05:14:00 | NPP-375D | PARANHOS | MATO GROSSO DO SUL | Brasil | 5006358 | 50 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| e47408ae-7a27-3e06-9ea9-2331b1fb9071 | -19.43375 | -57.21964 | 2026-01-20 05:14:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 7.1 |
| fa769a5a-2161-3e4b-b25f-2983dce4e3a9 | -19.42976 | -57.22295 | 2026-01-20 05:14:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 7.1 |
| 16d1433a-44ac-3856-bba9-f29b7d4e898c | -19.44116 | -57.24073 | 2026-01-20 05:14:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.0 |
| d3446228-ee05-3aee-9494-9a3a82e28302 | -20.712 | -48.82496 | 2026-01-20 05:14:00 | NPP-375D | OLÍMPIA | SÃO PAULO | Brasil | 3533908 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.3 |
| 117d833a-1c7d-3676-851d-4429544d499b | -20.85292 | -54.81871 | 2026-01-20 05:14:00 | NPP-375D | SIDROLÂNDIA | MATO GROSSO DO SUL | Brasil | 5007901 | 50 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 6f56cf56-69f5-3227-9740-b58339141f6c | -20.85679 | -54.8193 | 2026-01-20 05:14:00 | NPP-375D | SIDROLÂNDIA | MATO GROSSO DO SUL | Brasil | 5007901 | 50 | 33 | nan | nan | nan | Cerrado | 1.0 |
| cdfa57d9-bdf1-3659-94f8-6f0153120bef | -19.43888 | -57.23241 | 2026-01-20 05:14:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 0.8 |
| 97eff2e0-1d05-3da6-b409-9eedcd828cfc | -19.43603 | -57.22796 | 2026-01-20 05:14:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 0.8 |
| 57963bb4-66d7-3214-a7bc-fb5779a765a0 | -19.4269 | -57.21851 | 2026-01-20 05:14:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 0.8 |
| 403218f6-a4ea-3ffc-92eb-f2171c029da8 | -20.71239 | -48.82092 | 2026-01-20 05:14:00 | NPP-375D | OLÍMPIA | SÃO PAULO | Brasil | 3533908 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.4 |
| bd936ff0-9b21-35fe-9445-e68f5889ac66 | -19.42634 | -57.22239 | 2026-01-20 05:14:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 0.8 |
| 3eacdfae-140c-359d-a967-663a9b3cc11d | -31.551 | -53.73683 | 2026-01-20 05:16:00 | NPP-375D | CANDIOTA | RIO GRANDE DO SUL | Brasil | 4304358 | 43 | 33 | nan | nan | nan | Pampa | 1.5 |
| cf777ff4-4e9a-36f0-9c62-6c23fbbfc147 | 1.13112 | -60.52509 | 2026-01-20 05:29:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 55a0b603-db70-3d3d-955a-cd437364e013 | 2.20267 | -60.70493 | 2026-01-20 05:29:00 | NOAA-20 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 2bf470d0-ccde-3d5c-95b9-b26d975da91b | 2.5629 | -60.38368 | 2026-01-20 05:29:00 | NOAA-20 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 2.3 |
| a7af925b-9658-344b-814b-2b45589212a2 | 1.13443 | -60.52457 | 2026-01-20 05:29:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 3459fff2-9aa0-36af-bd55-1f129306003f | 3.31374 | -59.99455 | 2026-01-20 05:29:00 | NOAA-20 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 59663274-e929-39dd-9e70-c494d4f2078a | 3.3193 | -59.96551 | 2026-01-20 05:29:00 | NOAA-20 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e55f85c2-433b-32ac-97f2-cff172a06051 | 2.05188 | -60.86949 | 2026-01-20 05:29:00 | NOAA-20 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 224b389a-5a1c-36f7-8a9d-d8a203437391 | 0.75242 | -59.65644 | 2026-01-20 05:29:00 | NOAA-20 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 711f6c00-d363-3b12-8374-66476cd71bb5 | 2.56621 | -60.38317 | 2026-01-20 05:29:00 | NOAA-20 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 2.3 |
| bffc6091-035e-3fc8-b711-0b7a9e8e7fec | 2.68491 | -60.10086 | 2026-01-20 05:29:00 | NOAA-20 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 5f78065d-f8ba-3125-a4a9-d071af8c1aa8 | 2.05134 | -60.86604 | 2026-01-20 05:29:00 | NOAA-20 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 2.0 |
| f2fc9f25-249a-3608-a897-25f682ff2217 | 2.67504 | -60.0813 | 2026-01-20 05:29:00 | NOAA-20 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 53f703a1-c890-3109-b1e4-3affd628ce74 | 3.31265 | -59.98768 | 2026-01-20 05:29:00 | NOAA-20 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 0da07580-826a-3d66-94ba-bed6367f7fc5 | 3.31102 | -59.97738 | 2026-01-20 05:29:00 | NOAA-20 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 2f2c65dc-6c57-349e-aae8-b6740dc086c2 | 2.51512 | -60.98495 | 2026-01-20 05:29:00 | NOAA-20 | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a520c1a0-66aa-35cf-8e68-d5ba06c2ecbf | 2.55364 | -60.58232 | 2026-01-20 05:29:00 | NOAA-20 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 0.9 |
| bf3ba18e-31ae-338e-ad3c-dea222257eb7 | 2.04803 | -60.86657 | 2026-01-20 05:29:00 | NOAA-20 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 458e5607-70c8-376b-b8dd-6c68722d550c | 1.12782 | -60.5256 | 2026-01-20 05:29:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.9 |
| a48d4ed3-aead-3099-8091-2e013c252924 | 0.86355 | -59.69253 | 2026-01-20 05:29:00 | NOAA-20 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 0.7 |
| fa0a3894-a970-353b-a6fd-9b0896d281ca | 2.68382 | -60.09399 | 2026-01-20 05:29:00 | NOAA-20 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 3f55e300-0210-37a2-ad6f-362f956ab699 | 1.46943 | -59.95699 | 2026-01-20 05:29:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 8acb418f-1b1e-3b48-8ba9-c6ae9324fbfd | 1.13389 | -60.52114 | 2026-01-20 05:29:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 27022c55-04b7-36fb-92d0-355a1fb9f712 | 1.13665 | -60.51719 | 2026-01-20 05:29:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.4 |
| ed7a9622-1164-31b2-bc4a-c007609445b1 | 1.13719 | -60.52063 | 2026-01-20 05:29:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 0.8 |
| fae72828-d601-3efb-a9f0-5ba0c47c4847 | 2.5564 | -59.97645 | 2026-01-20 05:29:00 | NOAA-20 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 47999948-70d4-32ed-90e3-80782b6d7373 | 3.32206 | -59.96156 | 2026-01-20 05:29:00 | NOAA-20 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 0.9 |


[Clique aqui para ver as próximas entradas](README4.md)
