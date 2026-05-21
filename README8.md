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

## Dados Diários - Página 8

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 65921733-774c-3fe6-8637-764f53674c6d | -14.62963 | -48.03263 | 2026-05-21 04:25:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| f1826e32-f5d2-35f2-a669-988acb917b89 | -14.90013 | -47.75014 | 2026-05-21 04:25:00 | NOAA-20 | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 0dde82d6-a753-39a2-bc81-fadeaa6c68fa | -16.89534 | -46.78626 | 2026-05-21 04:25:00 | NOAA-20 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 22b634d8-10ff-3536-8f58-a8717979eb7b | -19.7694 | -54.07232 | 2026-05-21 04:25:00 | NOAA-20 | BANDEIRANTES | MATO GROSSO DO SUL | Brasil | 5001508 | 50 | 33 | nan | nan | nan | Cerrado | 2.3 |
| c7c5e3c5-bcd4-3b03-b8d8-9b6de77e83b1 | -19.76434 | -54.07558 | 2026-05-21 04:25:00 | NOAA-20 | BANDEIRANTES | MATO GROSSO DO SUL | Brasil | 5001508 | 50 | 33 | nan | nan | nan | Cerrado | 1.4 |
| b8a02745-bf67-3669-987a-02c8bf3a2d8b | -16.8959 | -46.78267 | 2026-05-21 04:25:00 | NOAA-20 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 9bd02cbf-a611-34fd-bc56-58408ed97726 | -14.63024 | -48.02889 | 2026-05-21 04:25:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 8a4d4a78-9f05-3a9b-b514-1aa33c4c6398 | -14.93281 | -47.75179 | 2026-05-21 04:25:00 | NOAA-20 | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 0.5 |
| a708db66-0ac7-3460-9c07-fe0fead1d005 | -15.91987 | -48.32231 | 2026-05-21 04:25:00 | NOAA-20 | SANTO ANTÔNIO DO DESCOBERTO | GOIÁS | Brasil | 5219753 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| d5540e6c-3825-35bd-8e9d-cdf492db9552 | -14.92947 | -47.75121 | 2026-05-21 04:25:00 | NOAA-20 | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 45078b72-4294-3872-a9bd-a463f6e55bda | -20.76586 | -48.56516 | 2026-05-21 04:25:00 | NOAA-20 | COLINA | SÃO PAULO | Brasil | 3512001 | 35 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 87b3c766-d4fa-3b9c-8a42-1f46a9f044e0 | -16.46005 | -51.7156 | 2026-05-21 04:25:00 | NOAA-20 | PIRANHAS | GOIÁS | Brasil | 5217203 | 52 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 9d1a9834-cd1b-36a3-acc8-fc00842d0892 | -14.90406 | -47.74711 | 2026-05-21 04:25:00 | NOAA-20 | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 5aa96c6a-b1c9-3ac3-9b13-d7efe0c1d9f0 | -14.90071 | -47.74651 | 2026-05-21 04:25:00 | NOAA-20 | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| d27314c2-6029-31bf-8635-5d0d09497a8a | -19.77214 | -54.07197 | 2026-05-21 04:25:00 | NOAA-20 | BANDEIRANTES | MATO GROSSO DO SUL | Brasil | 5001508 | 50 | 33 | nan | nan | nan | Cerrado | 0.7 |
| a62eab2e-ef2d-3919-962a-4b6fa5a9664a | -19.77022 | -54.06801 | 2026-05-21 04:25:00 | NOAA-20 | BANDEIRANTES | MATO GROSSO DO SUL | Brasil | 5001508 | 50 | 33 | nan | nan | nan | Cerrado | 1.5 |
| ef2f446d-480b-3d39-bb6c-dd69689a405b | -14.92612 | -47.75062 | 2026-05-21 04:25:00 | NOAA-20 | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| ff08f092-8df9-3154-ad74-ea2cd703835e | -19.96626 | -44.71732 | 2026-05-21 04:25:00 | NOAA-20 | IGARATINGA | MINAS GERAIS | Brasil | 3130200 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 3d742d33-7a91-3a2a-88cd-9b106559470a | -14.90131 | -47.74287 | 2026-05-21 04:25:00 | NOAA-20 | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| df06e6ce-7f6c-35a3-8d8d-9002e00a809a | -19.78373 | -45.39196 | 2026-05-21 04:25:00 | NOAA-20 | MOEMA | MINAS GERAIS | Brasil | 3142403 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 5634cea3-da00-3016-a21f-4f0a6b725cbe | -19.76857 | -54.07666 | 2026-05-21 04:25:00 | NOAA-20 | BANDEIRANTES | MATO GROSSO DO SUL | Brasil | 5001508 | 50 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 093eba9f-3ea4-3cb1-b02c-b5fbee95f275 | -14.63422 | -48.02577 | 2026-05-21 04:25:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 0fd01568-a4f1-3f3d-8992-d8cc32b952fc | -14.89953 | -47.75377 | 2026-05-21 04:25:00 | NOAA-20 | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| b724c807-66cb-318f-bd17-c872cc28bc2e | -19.77128 | -54.07627 | 2026-05-21 04:25:00 | NOAA-20 | BANDEIRANTES | MATO GROSSO DO SUL | Brasil | 5001508 | 50 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 85f7a572-61f0-3330-bba3-277a4e601f8f | -16.45615 | -51.71479 | 2026-05-21 04:25:00 | NOAA-20 | PIRANHAS | GOIÁS | Brasil | 5217203 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 267f1045-e78e-3521-8dd2-491aa760f83f | -14.21358 | -54.60387 | 2026-05-21 04:25:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| cf04bba3-7bb9-3d47-b211-1c784ac86bd7 | -17.35152 | -50.37715 | 2026-05-21 04:25:00 | NOAA-20 | ACREÚNA | GOIÁS | Brasil | 5200134 | 52 | 33 | nan | nan | nan | Cerrado | 0.5 |
| b0b87169-28e5-394a-b742-8f0ec7e3826d | -14.6336 | -48.02956 | 2026-05-21 04:25:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 68ab13eb-cbba-3d54-8a0c-5c525fb0cf55 | -14.62687 | -48.02825 | 2026-05-21 04:25:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| b2ada139-a572-397d-ab35-cb8c6ee8619c | -14.6287 | -48.01708 | 2026-05-21 04:25:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 9bd49f52-0d4f-3a32-8bd0-af4a579f385f | -16.89922 | -46.78323 | 2026-05-21 04:25:00 | NOAA-20 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 59a2defb-0ec4-3d9e-9572-1eca048f2e9b | -14.62748 | -48.02452 | 2026-05-21 04:25:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 1468c412-715a-36fe-adde-7146e9333edb | -23.40587 | -46.85567 | 2026-05-21 04:27:00 | NOAA-20 | CAJAMAR | SÃO PAULO | Brasil | 3509205 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 40dbcbd5-6dfd-3760-9cde-c46b6fd7849e | -27.6091 | -49.94167 | 2026-05-21 04:27:00 | NOAA-20 | OTACÍLIO COSTA | SANTA CATARINA | Brasil | 4211751 | 42 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 32b9add5-c662-3ed8-9c40-3de277f414dc | -28.7428 | -49.38293 | 2026-05-21 04:27:00 | NOAA-20 | CRICIÚMA | SANTA CATARINA | Brasil | 4204608 | 42 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 89916f16-290f-3e5e-99d5-4e592f92c153 | -28.79555 | -51.37656 | 2026-05-21 04:27:00 | NOAA-20 | IPÊ | RIO GRANDE DO SUL | Brasil | 4310439 | 43 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 9d2767ff-9c8b-3eb0-8e57-b4bd16da8c4d | -23.25928 | -50.37831 | 2026-05-21 04:27:00 | NOAA-20 | SANTA AMÉLIA | PARANÁ | Brasil | 4123105 | 41 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 95ac6137-535f-3bcb-85bb-7eb656bdfd02 | -27.65645 | -48.69878 | 2026-05-21 04:27:00 | NOAA-20 | PALHOÇA | SANTA CATARINA | Brasil | 4211900 | 42 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 78bc53af-7995-3216-8768-1fc16f1b881d | -27.84163 | -50.40149 | 2026-05-21 04:27:00 | NOAA-20 | LAGES | SANTA CATARINA | Brasil | 4209300 | 42 | 33 | nan | nan | nan | Mata Atlântica | 0.4 |
| c5a18c65-23eb-3153-bc9b-2b5ca3f8ce4b | -31.58408 | -51.31324 | 2026-05-21 04:29:00 | NOAA-20 | SÃO JOSÉ DO NORTE | RIO GRANDE DO SUL | Brasil | 4318507 | 43 | 33 | nan | nan | nan | Pampa | 0.6 |
| 5cfde01d-2ca8-3a6d-a855-8819d89a9a25 | -31.85398 | -51.76697 | 2026-05-21 04:29:00 | NOAA-20 | SÃO JOSÉ DO NORTE | RIO GRANDE DO SUL | Brasil | 4318507 | 43 | 33 | nan | nan | nan | Pampa | 0.8 |
| afc71bca-dc75-3dd4-9619-44aca3771edd | -29.33437 | -55.98333 | 2026-05-21 04:29:00 | NOAA-20 | ITAQUI | RIO GRANDE DO SUL | Brasil | 4310603 | 43 | 33 | nan | nan | nan | Pampa | 2.5 |
| 2636000f-8641-3354-bbee-0df56dd588b8 | -9.3045 | -45.4809 | 2026-05-21 04:30:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 52.8 |
| 0f2b1e71-406c-3185-bfb4-078d64cbba43 | -6.7569 | -45.01767 | 2026-05-21 05:10:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 2878fda8-92c0-3dd4-aa84-de71d9b59939 | -6.30139 | -43.64109 | 2026-05-21 05:10:00 | NOAA-21 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| dce19016-bd14-311f-891e-b8c694b4acc3 | -7.05535 | -45.06413 | 2026-05-21 05:10:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| c3797ab4-55c7-3d1a-a06b-3263f34b6f46 | -6.39446 | -44.17412 | 2026-05-21 05:10:00 | NOAA-21 | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 0a636816-6508-3ea3-ab7f-c0d61be87c7a | -6.39527 | -44.16775 | 2026-05-21 05:10:00 | NOAA-21 | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 6e4898c7-a2cb-3bcc-accf-9c25cc7dd3b3 | -5.95467 | -43.48912 | 2026-05-21 05:10:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 5.3 |
| c47b1418-708d-3f12-a324-cfd76702b878 | -7.04878 | -45.06339 | 2026-05-21 05:10:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 4f6cd671-47c1-374e-857b-c2795f201890 | -6.39429 | -44.16865 | 2026-05-21 05:10:00 | NOAA-21 | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 8.4 |
| d32b8532-02df-3e0e-a56e-9a3a974403ec | -6.30228 | -43.63424 | 2026-05-21 05:10:00 | NOAA-21 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| d1d8eb15-a71f-3a65-883a-d18e2c65d97f | -5.94985 | -43.49104 | 2026-05-21 05:10:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 705bd245-0d05-35bc-ba17-8d36703be371 | -11.34089 | -48.00285 | 2026-05-21 05:12:00 | NOAA-21 | SANTA ROSA DO TOCANTINS | TOCANTINS | Brasil | 1718907 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| fa22c6f7-3806-3ba0-af22-1094272d643c | -10.44098 | -47.95493 | 2026-05-21 05:12:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| cc6ecff3-c453-3f69-88a1-0ca3b752c5c3 | -10.48843 | -49.36062 | 2026-05-21 05:12:00 | NOAA-21 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 10.8 |
| b9b94b0b-5f8d-3f35-8eef-8a3819d3bbfa | -11.30798 | -54.71421 | 2026-05-21 05:12:00 | NOAA-21 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 7b018709-c280-3791-8ea4-2f907f06c169 | -11.33947 | -48.00351 | 2026-05-21 05:12:00 | NOAA-21 | SANTA ROSA DO TOCANTINS | TOCANTINS | Brasil | 1718907 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 67448455-ec84-31da-9452-55c03bcd1528 | -10.09039 | -52.18515 | 2026-05-21 05:12:00 | NOAA-21 | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 2b219e35-443a-3c02-a3d6-415a900f545c | -10.11081 | -52.41109 | 2026-05-21 05:12:00 | NOAA-21 | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| cf2abad5-f688-31ed-a967-45002fa931b8 | -10.39678 | -49.44579 | 2026-05-21 05:12:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| bc65cdf1-82ac-3785-9126-9909fb5e28ab | -11.67617 | -54.5849 | 2026-05-21 05:12:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 207d8869-2752-3d71-be1c-a6d2069b86f0 | -11.98639 | -47.37612 | 2026-05-21 05:12:00 | NOAA-21 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 3ba4353a-30a2-319a-aafd-d9af491fa0d7 | -8.5537 | -45.98886 | 2026-05-21 05:12:00 | NOAA-21 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 11.3 |
| 41f01420-809a-3a0a-b2aa-5c008eba89dd | -11.03571 | -48.91541 | 2026-05-21 05:12:00 | NOAA-21 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| c7dcb98b-5293-3cb5-854a-1fda41ea3d7c | -10.11555 | -52.40789 | 2026-05-21 05:12:00 | NOAA-21 | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 93d02d44-429e-3300-b667-a89f04c989a0 | -8.73672 | -47.9822 | 2026-05-21 05:12:00 | NOAA-21 | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 68b8e166-97e1-31c3-936f-2dea5acbf68f | -8.55436 | -45.98359 | 2026-05-21 05:12:00 | NOAA-21 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 11.3 |
| c5d9e3b4-b8a0-33df-8af1-33933f509820 | -8.6161 | -46.00256 | 2026-05-21 05:12:00 | NOAA-21 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| aed004d5-54b8-3ff3-b9d7-6f5dff98c9be | -11.47938 | -52.92322 | 2026-05-21 05:12:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 6d9d4ac9-ba94-34ab-8b74-b3c1652fde1a | -11.18617 | -55.91347 | 2026-05-21 05:12:00 | NOAA-21 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 775a474e-02ca-373b-a1ca-476c74b7bee9 | -9.93049 | -59.92094 | 2026-05-21 05:12:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| aef9fdca-a82e-3ec0-85b2-d86b17c31f76 | -11.46334 | -52.91702 | 2026-05-21 05:12:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 260da5d5-1457-32e5-a1ce-ed3981db8cfc | -8.61366 | -45.99926 | 2026-05-21 05:12:00 | NOAA-21 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 950e7b2e-01e1-3607-9ab8-f73a934e38f3 | -11.46747 | -52.91763 | 2026-05-21 05:12:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| e466dfc9-78be-35eb-b021-975f696d049b | -9.96343 | -52.44915 | 2026-05-21 05:12:00 | NOAA-21 | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 906bbfda-fc7d-32d0-a183-cc6ea4713fd5 | -10.32514 | -53.58183 | 2026-05-21 05:12:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 3.7 |
| c26c5a7a-686e-3996-9126-fec060337210 | -11.98086 | -47.37089 | 2026-05-21 05:12:00 | NOAA-21 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 34d564c9-2d24-3027-bc72-fd6f849e7e8b | -9.30247 | -45.49461 | 2026-05-21 05:12:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 10.2 |
| 72e41681-7db6-3e82-b170-0a9ba684e24e | -9.3034 | -45.49331 | 2026-05-21 05:12:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 19.8 |
| 9c61b7e0-5b35-33a2-a386-228ad2c60047 | -9.30314 | -45.48889 | 2026-05-21 05:12:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 10.2 |
| 87c49faf-e087-3186-8c81-8a322ba60a3a | -10.11135 | -52.40724 | 2026-05-21 05:12:00 | NOAA-21 | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 0acd2ac6-9fa3-37a0-ae9d-c0058846e648 | -11.4623 | -55.11668 | 2026-05-21 05:12:00 | NOAA-21 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 90ad407d-fbc5-3394-9d05-aadf3d23d8f4 | -11.9183 | -54.10173 | 2026-05-21 05:12:00 | NOAA-21 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 7b46a32c-09f3-3510-b53b-1e2fe75a6d36 | -8.60606 | -45.95619 | 2026-05-21 05:12:00 | NOAA-21 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 077a56f6-d850-3f6f-92ab-762973d94b91 | -11.83777 | -47.09511 | 2026-05-21 05:12:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 21c8bdd3-d48d-328e-87d4-cb7e7e06f89e | -11.30363 | -54.71812 | 2026-05-21 05:12:00 | NOAA-21 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 4f515846-9741-39ee-849b-019ba9c4fa43 | -9.29824 | -45.48116 | 2026-05-21 05:12:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 9.1 |
| 79213fd5-ac86-3d88-9b2f-20521188d9c7 | -11.30494 | -54.70916 | 2026-05-21 05:12:00 | NOAA-21 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d530a9b6-f8e2-3060-96bc-8c79dc9bc05b | -8.73719 | -47.9786 | 2026-05-21 05:12:00 | NOAA-21 | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 80a73b68-7eec-3737-a419-723b54d9f09c | -11.43817 | -55.10428 | 2026-05-21 05:12:00 | NOAA-21 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 0864b789-af6d-3897-b289-3b93be5fa511 | -8.62246 | -45.9798 | 2026-05-21 05:12:00 | NOAA-21 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| d11fa8d3-d163-388c-bf18-5dd47f9ce2cc | -11.30733 | -54.71868 | 2026-05-21 05:12:00 | NOAA-21 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| df81f3d4-f9dc-3030-bf40-d72f433c05de | -10.7139 | -56.24088 | 2026-05-21 05:12:00 | NOAA-21 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 0.4 |
| d032a8bb-63d8-3026-9e37-eba84de3a1d6 | -9.30998 | -45.49404 | 2026-05-21 05:12:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 13.3 |
| 7df04669-1627-306a-8301-bb463e0518d5 | -11.18269 | -55.91293 | 2026-05-21 05:12:00 | NOAA-21 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 6.3 |
| ac8a1875-8aba-3188-89cb-3574dceef7d3 | -9.30972 | -45.48964 | 2026-05-21 05:12:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 8.5 |
| e128a431-2851-3008-89ec-62623e302257 | -10.0835 | -51.64132 | 2026-05-21 05:12:00 | NOAA-21 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 23add886-77b6-3e81-a618-edbe9ade7730 | -10.22796 | -52.66399 | 2026-05-21 05:12:00 | NOAA-21 | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 82c05f77-26b0-3dfb-895d-213efeb9a8dc | -11.30124 | -54.7086 | 2026-05-21 05:12:00 | NOAA-21 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |


[Clique aqui para ver as próximas entradas](README9.md)
