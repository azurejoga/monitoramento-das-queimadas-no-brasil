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

## Dados Diários - Página 2

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 2e62230e-50fa-3761-a810-133c5357391a | -17.50334 | -50.76271 | 2026-04-19 04:25:00 | NOAA-20 | RIO VERDE | GOIÁS | Brasil | 5218805 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 111a048f-7913-3a21-bebe-e814ccdaec2b | -19.10194 | -56.06142 | 2026-04-19 04:25:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.4 |
| 859a67b3-e6a9-3ea6-ab54-7d4dcdc530e6 | -15.70759 | -51.24435 | 2026-04-19 04:25:00 | NOAA-20 | SANTA FÉ DE GOIÁS | GOIÁS | Brasil | 5219258 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| f64c8d95-6cc1-34d9-91e8-a4239a45fd49 | -17.4997 | -50.76204 | 2026-04-19 04:25:00 | NOAA-20 | RIO VERDE | GOIÁS | Brasil | 5218805 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 122ec62a-1a7c-366b-a2cc-010241ca0ce5 | -18.07387 | -46.37111 | 2026-04-19 04:25:00 | NOAA-20 | PRESIDENTE OLEGÁRIO | MINAS GERAIS | Brasil | 3153400 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 2d76edb8-4447-39f9-9848-bdb3054368b4 | -17.50296 | -50.76418 | 2026-04-19 04:25:00 | NOAA-20 | RIO VERDE | GOIÁS | Brasil | 5218805 | 52 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 88096d64-d39c-3a9f-bbe2-92a87970a85e | -18.64294 | -45.02885 | 2026-04-19 04:25:00 | NOAA-20 | FELIXLÂNDIA | MINAS GERAIS | Brasil | 3125705 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| f6ed4529-8ded-3ce6-881a-2f1db17511cf | -17.51061 | -50.76406 | 2026-04-19 04:25:00 | NOAA-20 | RIO VERDE | GOIÁS | Brasil | 5218805 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 40272f2b-ccbd-3a91-8837-671eee161c13 | -28.6412 | -49.3657 | 2026-04-19 04:27:00 | NOAA-20 | CRICIÚMA | SANTA CATARINA | Brasil | 4204608 | 42 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 71b6277b-7a47-30e3-9217-d069cdd728b0 | -26.9825 | -51.02155 | 2026-04-19 04:27:00 | NOAA-20 | FRAIBURGO | SANTA CATARINA | Brasil | 4205506 | 42 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| ed6888be-d4cd-3b8c-bfeb-97738818fd5b | -23.78342 | -52.24065 | 2026-04-19 04:27:00 | NOAA-20 | ENGENHEIRO BELTRÃO | PARANÁ | Brasil | 4107504 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 8eb57723-d068-337d-8bd3-edd472dc938f | -22.76402 | -53.06187 | 2026-04-19 04:27:00 | NOAA-20 | MARILENA | PARANÁ | Brasil | 4115002 | 41 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 3bdf6abb-bea7-334c-ac9a-60e8dc593d06 | -25.5228 | -49.10167 | 2026-04-19 04:27:00 | NOAA-20 | SÃO JOSÉ DOS PINHAIS | PARANÁ | Brasil | 4125506 | 41 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 252ff410-1eb1-3408-9847-aec65e84e65f | -26.61684 | -49.97844 | 2026-04-19 04:27:00 | NOAA-20 | SANTA TEREZINHA | SANTA CATARINA | Brasil | 4215679 | 42 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 1b938b2b-a786-38f2-9fd5-5964fa28f5a0 | -23.64742 | -47.99988 | 2026-04-19 04:27:00 | NOAA-20 | ITAPETININGA | SÃO PAULO | Brasil | 3522307 | 35 | 33 | nan | nan | nan | Cerrado | 1.5 |
| ed7cf92b-bca8-3907-80dd-5ea9d381caff | -22.76176 | -53.05979 | 2026-04-19 04:27:00 | NOAA-20 | MARILENA | PARANÁ | Brasil | 4115002 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 305f0df5-d96e-3360-856a-59287f4dcc7f | -23.78701 | -52.24141 | 2026-04-19 04:27:00 | NOAA-20 | ENGENHEIRO BELTRÃO | PARANÁ | Brasil | 4107504 | 41 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| fbc8f215-cf6a-3ff0-b32e-726d4e51d3c3 | -23.6425 | -47.98727 | 2026-04-19 04:27:00 | NOAA-20 | ITAPETININGA | SÃO PAULO | Brasil | 3522307 | 35 | 33 | nan | nan | nan | Cerrado | 0.5 |
| e9993312-1f6b-315f-9347-98d4b4dd66ef | -27.1254 | -51.38217 | 2026-04-19 04:27:00 | NOAA-20 | IBICARÉ | SANTA CATARINA | Brasil | 4206801 | 42 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 57430f63-3ebc-3edd-b5c4-28e63c36c2fc | -27.1076 | -50.80135 | 2026-04-19 04:27:00 | NOAA-20 | FRAIBURGO | SANTA CATARINA | Brasil | 4205506 | 42 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 3f0c3d9f-4211-3a75-8617-b8c4048e0ff2 | -25.88029 | -49.4437 | 2026-04-19 04:27:00 | NOAA-20 | QUITANDINHA | PARANÁ | Brasil | 4121208 | 41 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| a1f2d101-19d6-33dd-b6ae-50528d8d8b63 | -25.8805 | -49.02951 | 2026-04-19 04:27:00 | NOAA-20 | TIJUCAS DO SUL | PARANÁ | Brasil | 4127601 | 41 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| e0323600-663b-36a1-8af9-52626cd03c00 | -25.17388 | -49.39788 | 2026-04-19 04:27:00 | NOAA-20 | RIO BRANCO DO SUL | PARANÁ | Brasil | 4122206 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| ebc2446e-775a-3430-b01e-6603cc7929c5 | -25.0936 | -49.3475 | 2026-04-19 04:27:00 | NOAA-20 | RIO BRANCO DO SUL | PARANÁ | Brasil | 4122206 | 41 | 33 | nan | nan | nan | Mata Atlântica | 2.4 |
| d94f39ef-9772-30ed-8948-831be978ce66 | -27.36258 | -53.57309 | 2026-04-19 04:27:00 | NOAA-20 | PALMITINHO | RIO GRANDE DO SUL | Brasil | 4313805 | 43 | 33 | nan | nan | nan | Mata Atlântica | 0.4 |
| cbc17dba-6dca-39c7-9d50-b23528041ee0 | -25.09029 | -49.34687 | 2026-04-19 04:27:00 | NOAA-20 | RIO BRANCO DO SUL | PARANÁ | Brasil | 4122206 | 41 | 33 | nan | nan | nan | Mata Atlântica | 0.3 |
| fc95744f-0771-3b3c-afcd-92f5d4c695d1 | -28.061 | -48.67879 | 2026-04-19 04:27:00 | NOAA-20 | GAROPABA | SANTA CATARINA | Brasil | 4205704 | 42 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| a34368d2-ac0d-3ea7-8714-f81663db4081 | -25.08468 | -50.91518 | 2026-04-19 04:27:00 | NOAA-20 | GUAMIRANGA | PARANÁ | Brasil | 4108957 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 480c658d-21e8-35b3-8c8f-8abfe0883124 | -23.2704 | -55.18444 | 2026-04-19 04:27:00 | NOAA-20 | AMAMBAI | MATO GROSSO DO SUL | Brasil | 5000609 | 50 | 33 | nan | nan | nan | Mata Atlântica | 2.4 |
| 92efd6c0-7250-304c-9a81-d192b73d6497 | -25.09421 | -49.3437 | 2026-04-19 04:27:00 | NOAA-20 | RIO BRANCO DO SUL | PARANÁ | Brasil | 4122206 | 41 | 33 | nan | nan | nan | Mata Atlântica | 2.4 |
| c7cd66f6-88d4-3fcf-9355-e713d6494c13 | -23.78575 | -52.24285 | 2026-04-19 04:27:00 | NOAA-20 | ENGENHEIRO BELTRÃO | PARANÁ | Brasil | 4107504 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| 3280dedd-9a9b-3c43-a93b-260d0cdcb109 | -23.64583 | -47.98787 | 2026-04-19 04:27:00 | NOAA-20 | ITAPETININGA | SÃO PAULO | Brasil | 3522307 | 35 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 425cf0cb-0968-3314-a311-637c96fa7704 | -23.26617 | -55.18337 | 2026-04-19 04:27:00 | NOAA-20 | AMAMBAI | MATO GROSSO DO SUL | Brasil | 5000609 | 50 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| b3c9d673-5b19-3f65-8d5c-9cb244781592 | -11.35851 | -55.30128 | 2026-04-19 05:12:00 | NOAA-21 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| bc1ba4a8-90cc-3b84-b964-56c748d97211 | -11.35791 | -55.30547 | 2026-04-19 05:12:00 | NOAA-21 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 73bde373-ba49-32fd-b7aa-9030ba76288d | -11.36209 | -55.30184 | 2026-04-19 05:12:00 | NOAA-21 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 8720a14b-a26a-3a32-beb3-f0c6f809a833 | -11.35013 | -55.30856 | 2026-04-19 05:12:00 | NOAA-21 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| dd5b0369-e4a1-3052-8814-242da93da327 | -19.09945 | -56.05949 | 2026-04-19 05:14:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.4 |
| b350b08b-eb62-33f8-b80a-b69ae66a0708 | -19.10322 | -56.06006 | 2026-04-19 05:14:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.6 |
| 927f1a00-6d21-32c4-92d2-084ed5bdfbac | -19.09567 | -56.05893 | 2026-04-19 05:14:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.4 |
| ed213711-7d32-32a4-b939-b0b2eb8169da | -17.51007 | -50.76413 | 2026-04-19 05:14:00 | NOAA-21 | RIO VERDE | GOIÁS | Brasil | 5218805 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| b97b90ec-5979-32e7-9da5-3d93c75f5a66 | -17.5034 | -50.76428 | 2026-04-19 05:14:00 | NOAA-21 | RIO VERDE | GOIÁS | Brasil | 5218805 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| a1fc7f11-47ec-3c2b-8460-0003dcb89009 | -17.50897 | -50.76158 | 2026-04-19 05:14:00 | NOAA-21 | RIO VERDE | GOIÁS | Brasil | 5218805 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 210c8d7e-4db8-3fb0-91fb-169036191f38 | -17.51527 | -50.76474 | 2026-04-19 05:14:00 | NOAA-21 | RIO VERDE | GOIÁS | Brasil | 5218805 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 74226b1c-9612-3cca-b4ec-3353b5d648ca | -17.5038 | -50.76079 | 2026-04-19 05:14:00 | NOAA-21 | RIO VERDE | GOIÁS | Brasil | 5218805 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 09f30981-b3e2-32d2-93a7-91a1da6da8e2 | -23.27279 | -55.18476 | 2026-04-19 05:16:00 | NOAA-21 | AMAMBAI | MATO GROSSO DO SUL | Brasil | 5000609 | 50 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| 1fbba23c-95d3-355d-b6c1-99e7556645e7 | -23.26906 | -55.18007 | 2026-04-19 05:16:00 | NOAA-21 | AMAMBAI | MATO GROSSO DO SUL | Brasil | 5000609 | 50 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| a4ae7385-8e34-39c0-b3c9-8e7c2456fafd | -20.62744 | -51.70887 | 2026-04-19 05:16:00 | NOAA-21 | TRÊS LAGOAS | MATO GROSSO DO SUL | Brasil | 5008305 | 50 | 33 | nan | nan | nan | Cerrado | 1.3 |
| e62a129c-0715-31a4-8856-18ff27c0d7b0 | -23.26858 | -55.18422 | 2026-04-19 05:16:00 | NOAA-21 | AMAMBAI | MATO GROSSO DO SUL | Brasil | 5000609 | 50 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| 64fbaf16-f1c4-3a14-be45-780b7141d55e | -23.27327 | -55.18062 | 2026-04-19 05:16:00 | NOAA-21 | AMAMBAI | MATO GROSSO DO SUL | Brasil | 5000609 | 50 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 2dfc82c7-60aa-3780-844c-59beb81c9c84 | -20.62808 | -51.70257 | 2026-04-19 05:16:00 | NOAA-21 | TRÊS LAGOAS | MATO GROSSO DO SUL | Brasil | 5008305 | 50 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 225328b5-2c62-3667-905e-8c659e8c9f37 | -29.77283 | -51.09874 | 2026-04-19 05:18:00 | NOAA-21 | SÃO LEOPOLDO | RIO GRANDE DO SUL | Brasil | 4318705 | 43 | 33 | nan | nan | nan | Pampa | 1.2 |
| 2a10c6e8-1335-3a46-a5f2-d9fbd46043b0 | -29.76743 | -51.09819 | 2026-04-19 05:18:00 | NOAA-21 | SÃO LEOPOLDO | RIO GRANDE DO SUL | Brasil | 4318705 | 43 | 33 | nan | nan | nan | Pampa | 2.7 |
| c0214726-7197-34ed-a592-e7d5cd2ec691 | -29.76702 | -51.09782 | 2026-04-19 05:18:00 | NOAA-21 | SÃO LEOPOLDO | RIO GRANDE DO SUL | Brasil | 4318705 | 43 | 33 | nan | nan | nan | Pampa | 1.7 |
| 8549871c-d6dc-3ecd-8e9c-703497d639a9 | -23.26647 | -55.18198 | 2026-04-19 05:48:00 | NPP-375D | AMAMBAI | MATO GROSSO DO SUL | Brasil | 5000609 | 50 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| e77e4f09-f7d0-3cdb-b1d6-0378c05a31a8 | -23.27287 | -55.18242 | 2026-04-19 05:48:00 | NPP-375D | AMAMBAI | MATO GROSSO DO SUL | Brasil | 5000609 | 50 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| d745b729-013b-389e-b454-225e5fdb7103 | -17.79688 | -46.02219 | 2026-04-19 11:45:00 | TERRA_M-M | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 55fbd34e-8e11-3eda-8d72-f30e7dcd35c4 | -19.49741 | -40.17273 | 2026-04-19 11:45:00 | TERRA_M-M | LINHARES | ESPÍRITO SANTO | Brasil | 3203205 | 32 | 33 | nan | nan | nan | Mata Atlântica | 11.1 |
| a18fcbac-d723-35b7-9f28-eff9b2d5c972 | -19.77371 | -40.35952 | 2026-04-19 11:47:00 | TERRA_M-M | IBIRAÇU | ESPÍRITO SANTO | Brasil | 3202504 | 32 | 33 | nan | nan | nan | Mata Atlântica | 9.0 |
| 1e3ed98d-7501-3fb9-a6e0-de84ee11bb7e | -20.53104 | -43.51004 | 2026-04-19 11:47:00 | TERRA_M-M | OURO PRETO | MINAS GERAIS | Brasil | 3146107 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.5 |
| 6ba5d8ab-a693-3491-afb0-f6f6ed004595 | -19.77183 | -40.37627 | 2026-04-19 11:47:00 | TERRA_M-M | JOÃO NEIVA | ESPÍRITO SANTO | Brasil | 3203130 | 32 | 33 | nan | nan | nan | Mata Atlântica | 9.1 |
| 851254df-bfc1-35f3-a2af-81e7d3ae1ac7 | -17.499 | -50.7668 | 2026-04-19 13:10:00 | GOES-19 | RIO VERDE | GOIÁS | Brasil | 5218805 | 52 | 33 | nan | nan | nan | Cerrado | 71.7 |
| 14cb5aae-fbed-3280-b76f-484ef88e6f8a | -17.499 | -50.7668 | 2026-04-19 13:20:00 | GOES-19 | RIO VERDE | GOIÁS | Brasil | 5218805 | 52 | 33 | nan | nan | nan | Cerrado | 71.0 |
| ea95257f-50dc-34a0-9e72-dd0d33cc23d4 | -17.499 | -50.7668 | 2026-04-19 13:30:00 | GOES-19 | RIO VERDE | GOIÁS | Brasil | 5218805 | 52 | 33 | nan | nan | nan | Cerrado | 92.4 |
| d2ca34ff-34fc-332e-910b-2607ab99bf86 | -17.499 | -50.7668 | 2026-04-19 13:40:00 | GOES-19 | RIO VERDE | GOIÁS | Brasil | 5218805 | 52 | 33 | nan | nan | nan | Cerrado | 85.7 |
| 0d245805-c96b-3313-bfcf-7dcec757ba8f | -17.499 | -50.7668 | 2026-04-19 13:50:00 | GOES-19 | RIO VERDE | GOIÁS | Brasil | 5218805 | 52 | 33 | nan | nan | nan | Cerrado | 100.9 |
| 0160d3ff-8b78-3632-b3db-afdc649b6ed3 | -17.499 | -50.7668 | 2026-04-19 14:00:00 | GOES-19 | RIO VERDE | GOIÁS | Brasil | 5218805 | 52 | 33 | nan | nan | nan | Cerrado | 97.5 |


