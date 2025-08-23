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

## Dados Diários - Página 57

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 8ec87b60-bf99-31ad-8ba4-3b85819b564a | -20.87351 | -54.99854 | 2025-08-23 04:55:00 | NOAA-21 | SIDROLÂNDIA | MATO GROSSO DO SUL | Brasil | 5007901 | 50 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 4971c842-8460-3014-aeba-39b8851364d1 | -20.87407 | -54.99479 | 2025-08-23 04:55:00 | NOAA-21 | SIDROLÂNDIA | MATO GROSSO DO SUL | Brasil | 5007901 | 50 | 33 | nan | nan | nan | Cerrado | 1.9 |
| e7986384-cf71-36e0-a3bb-e1d660dfa4a2 | -17.67828 | -50.123 | 2025-08-23 04:55:00 | NOAA-21 | EDÉIA | GOIÁS | Brasil | 5207402 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 89c39846-9eea-3a0e-aa09-8572a7fd346d | -17.59616 | -46.56247 | 2025-08-23 04:55:00 | NOAA-21 | LAGOA GRANDE | MINAS GERAIS | Brasil | 3137536 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 11b43b43-8be7-361f-ba6c-67864092dc3d | -20.11855 | -47.78401 | 2025-08-23 04:55:00 | NOAA-21 | ARAMINA | SÃO PAULO | Brasil | 3503000 | 35 | 33 | nan | nan | nan | Cerrado | 1.1 |
| e1697dd0-b4a9-30d1-bf88-9cad9129b427 | -18.83602 | -51.28769 | 2025-08-23 04:55:00 | NOAA-21 | ITARUMÃ | GOIÁS | Brasil | 5211305 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 867da062-fa21-3030-a766-9f002f0af325 | -21.95282 | -45.59423 | 2025-08-23 04:55:00 | NOAA-21 | SÃO GONÇALO DO SAPUCAÍ | MINAS GERAIS | Brasil | 3162005 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| 1fb3e029-4cf1-35e6-b6b5-532e8c65c758 | -17.68564 | -51.9059 | 2025-08-23 04:55:00 | NOAA-21 | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| b9dc112c-258f-3c6d-bc8f-61ea6fb98627 | -22.64479 | -47.44356 | 2025-08-23 04:55:00 | NOAA-21 | LIMEIRA | SÃO PAULO | Brasil | 3526902 | 35 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 8997a524-1865-32f9-8220-15058a6a45d2 | -26.52971 | -51.69567 | 2025-08-23 04:57:00 | NOAA-21 | PALMAS | PARANÁ | Brasil | 4117602 | 41 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 642b7727-1c6b-34ac-8de8-ba6dd2d7dc89 | -25.56756 | -51.0611 | 2025-08-23 04:57:00 | NOAA-21 | INÁCIO MARTINS | PARANÁ | Brasil | 4110201 | 41 | 33 | nan | nan | nan | Mata Atlântica | 4.3 |
| e5e458a7-9364-3696-b2bc-a2cb26624c15 | -26.25128 | -49.58079 | 2025-08-23 04:57:00 | NOAA-21 | RIO NEGRINHO | SANTA CATARINA | Brasil | 4215000 | 42 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 62946300-a8fd-3a77-956a-e3f1b2a46ecc | -25.57652 | -51.05791 | 2025-08-23 04:57:00 | NOAA-21 | INÁCIO MARTINS | PARANÁ | Brasil | 4110201 | 41 | 33 | nan | nan | nan | Mata Atlântica | 6.2 |
| 846b9e36-eb15-3947-8fb8-5c542137286f | -25.56798 | -51.05922 | 2025-08-23 04:57:00 | NOAA-21 | INÁCIO MARTINS | PARANÁ | Brasil | 4110201 | 41 | 33 | nan | nan | nan | Mata Atlântica | 9.1 |
| bb7d9f7f-a503-37a6-a03a-e0130adb4b54 | -25.15064 | -49.5345 | 2025-08-23 04:57:00 | NOAA-21 | ITAPERUÇU | PARANÁ | Brasil | 4111258 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 55cb63a5-ea11-34fc-b519-f25c4310b91f | -24.75565 | -50.147 | 2025-08-23 04:57:00 | NOAA-21 | CASTRO | PARANÁ | Brasil | 4104907 | 41 | 33 | nan | nan | nan | Mata Atlântica | 2.4 |
| 944463de-e0f0-3bbf-ad2b-7026395ae0c3 | -25.16853 | -50.07579 | 2025-08-23 04:57:00 | NOAA-21 | PONTA GROSSA | PARANÁ | Brasil | 4119905 | 41 | 33 | nan | nan | nan | Mata Atlântica | 6.3 |
| a32187bc-9922-3be4-a2eb-36dbe955d74c | -25.57228 | -51.05729 | 2025-08-23 04:57:00 | NOAA-21 | INÁCIO MARTINS | PARANÁ | Brasil | 4110201 | 41 | 33 | nan | nan | nan | Mata Atlântica | 6.2 |
| 76a57c7f-a11d-344e-b661-56429efd4140 | -25.43016 | -49.74778 | 2025-08-23 04:57:00 | NOAA-21 | BALSA NOVA | PARANÁ | Brasil | 4102307 | 41 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 40720421-1c39-35a4-9d96-dd1881128cc9 | -26.24845 | -49.58072 | 2025-08-23 04:57:00 | NOAA-21 | RIO NEGRINHO | SANTA CATARINA | Brasil | 4215000 | 42 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 251c2d23-9521-3741-a18d-8dbac2b1e46f | -25.16802 | -50.0806 | 2025-08-23 04:57:00 | NOAA-21 | PONTA GROSSA | PARANÁ | Brasil | 4119905 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| 49a42ec3-acf8-35f6-bcf4-d88b7d01d399 | -25.57222 | -51.05975 | 2025-08-23 04:57:00 | NOAA-21 | INÁCIO MARTINS | PARANÁ | Brasil | 4110201 | 41 | 33 | nan | nan | nan | Mata Atlântica | 9.1 |
| 45804ac9-c322-3d70-8fd1-c96f1dc2bd44 | -25.57181 | -51.06164 | 2025-08-23 04:57:00 | NOAA-21 | INÁCIO MARTINS | PARANÁ | Brasil | 4110201 | 41 | 33 | nan | nan | nan | Mata Atlântica | 6.2 |
| b77791a8-1f6b-3d4b-a12f-866d84686e7d | -25.17252 | -50.08111 | 2025-08-23 04:57:00 | NOAA-21 | PONTA GROSSA | PARANÁ | Brasil | 4119905 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| 28825fdc-5820-37cf-96fa-70535ed3fabe | -26.91214 | -51.99632 | 2025-08-23 04:57:00 | NOAA-21 | PONTE SERRADA | SANTA CATARINA | Brasil | 4213401 | 42 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 5a14f6de-2be9-331f-aa9f-0972b49a918e | -24.91113 | -49.27661 | 2025-08-23 04:57:00 | NOAA-21 | CERRO AZUL | PARANÁ | Brasil | 4105201 | 41 | 33 | nan | nan | nan | Mata Atlântica | 2.3 |
| 43a8b9f2-90aa-3a97-b9b4-ab49b996bc76 | -25.57605 | -51.06221 | 2025-08-23 04:57:00 | NOAA-21 | INÁCIO MARTINS | PARANÁ | Brasil | 4110201 | 41 | 33 | nan | nan | nan | Mata Atlântica | 6.2 |
| 30f40f09-2b27-37fc-8d07-7c4ffbb9eb23 | -24.90936 | -49.27507 | 2025-08-23 04:57:00 | NOAA-21 | CERRO AZUL | PARANÁ | Brasil | 4105201 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| a004a9b4-2277-323d-a070-b31bb465cf6c | -24.96087 | -53.51643 | 2025-08-23 04:57:00 | NOAA-21 | CASCAVEL | PARANÁ | Brasil | 4104808 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 89accc77-6ff0-3f60-ad80-c485cb0955a4 | -9.9681 | -60.1743 | 2025-08-23 05:00:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 82.7 |
| df660e44-4ba9-3fe9-8f96-32b35937aa88 | -22.6564 | -47.4462 | 2025-08-23 05:00:00 | GOES-19 | LIMEIRA | SÃO PAULO | Brasil | 3526902 | 35 | 33 | nan | nan | nan | Cerrado | 50.4 |
| e74587f7-e745-3368-8745-fe77c5d5e138 | -9.968 | -60.1937 | 2025-08-23 05:00:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 214.2 |
| 8ce6bcbf-c852-38aa-bae3-ac332a73c264 | -17.5985 | -46.5481 | 2025-08-23 05:00:00 | GOES-19 | LAGOA GRANDE | MINAS GERAIS | Brasil | 3137536 | 31 | 33 | nan | nan | nan | Cerrado | 51.8 |
| 2ce2f6eb-a881-3732-9b91-d20d2901db1c | -20.4042 | -45.592 | 2025-08-23 05:00:00 | GOES-19 | PAINS | MINAS GERAIS | Brasil | 3146503 | 31 | 33 | nan | nan | nan | Cerrado | 52.6 |
| 3877c97f-91c9-3c24-8509-e567285fc957 | -5.7615 | -57.5807 | 2025-08-23 05:00:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 59.5 |
| b6494364-d28d-33de-a757-e7579e2c02f5 | -9.9493 | -60.1947 | 2025-08-23 05:00:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 450.3 |
| a06a874a-e46a-39e6-b82f-51e213482fa4 | -5.7431 | -57.5814 | 2025-08-23 05:00:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 69.5 |
| d7c0de0d-9ca4-3b2d-8655-01743acb7fa9 | -9.9492 | -60.2141 | 2025-08-23 05:00:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 66.3 |
| 404ddda9-ca4c-36a4-a3c4-afc02a72b850 | -5.7429 | -57.6009 | 2025-08-23 05:00:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 69.1 |
| 33b0b60d-8831-3ce3-81be-04faf4a6a428 | -9.9495 | -60.1754 | 2025-08-23 05:00:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 146.4 |
| eaf9b0c9-dc82-3fa5-913d-4ba53e5cbcbb | -5.7614 | -57.6002 | 2025-08-23 05:00:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 36.1 |
| e969e343-5448-3e0d-936f-ec83d2b9ba83 | -12.9921 | -45.2252 | 2025-08-23 05:00:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 72.1 |
| 6c4aabc6-6937-388d-a5ca-ca14eb675d67 | -9.1897 | -59.6171 | 2025-08-23 05:00:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 52.3 |
| cef80d4b-9cfd-3e25-a345-a0b2750e7b2e | -6.6044 | -44.5624 | 2025-08-23 05:00:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 71.0 |
| c4e5a426-815a-388b-baf7-13b228c2a87a | -17.5785 | -46.5523 | 2025-08-23 05:00:00 | GOES-19 | LAGOA GRANDE | MINAS GERAIS | Brasil | 3137536 | 31 | 33 | nan | nan | nan | Cerrado | 52.4 |
| 618bb246-b970-3528-b38f-95a87a357a22 | -9.1897 | -59.6171 | 2025-08-23 05:10:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 51.9 |
| 70613339-2529-373c-bacd-8ebc7377ff90 | -17.5785 | -46.5523 | 2025-08-23 05:10:00 | GOES-19 | LAGOA GRANDE | MINAS GERAIS | Brasil | 3137536 | 31 | 33 | nan | nan | nan | Cerrado | 53.0 |
| c10b39a9-eca8-3052-9604-38489b7421cd | -20.4042 | -45.592 | 2025-08-23 05:10:00 | GOES-19 | PAINS | MINAS GERAIS | Brasil | 3146503 | 31 | 33 | nan | nan | nan | Cerrado | 53.5 |
| 8478a3cf-080a-39d6-816d-06c240a48157 | -5.7429 | -57.6009 | 2025-08-23 05:10:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 79.6 |
| deddac6a-1f78-3f15-8f14-da63ac73e606 | -17.5985 | -46.5481 | 2025-08-23 05:10:00 | GOES-19 | LAGOA GRANDE | MINAS GERAIS | Brasil | 3137536 | 31 | 33 | nan | nan | nan | Cerrado | 51.6 |
| a3776c63-b168-3f55-b482-d53d2ddd056a | -12.9921 | -45.2252 | 2025-08-23 05:10:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 64.8 |
| 3bfed740-0860-3d6c-a8d8-d7ef046af222 | -9.9495 | -60.1754 | 2025-08-23 05:10:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 151.5 |
| 5ab98d2e-27ba-3a04-8774-356700295667 | -6.6044 | -44.5624 | 2025-08-23 05:10:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 62.7 |
| f38d5d17-3a85-3dd9-a0a1-4dd27ea194f6 | -5.7615 | -57.5807 | 2025-08-23 05:10:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 84.7 |
| 39b33b3c-55fc-325c-96e1-b8b46291a902 | -5.7614 | -57.6002 | 2025-08-23 05:10:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 62.4 |
| 13a59a87-4f23-38b3-af00-0dd6aeb30c36 | -9.9493 | -60.1947 | 2025-08-23 05:10:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 320.3 |
| 853e53f5-1fbe-37bf-9290-fdde88cbea0a | -9.9681 | -60.1743 | 2025-08-23 05:10:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 102.1 |
| f28af833-19e9-327f-b868-e2dbf94bc023 | -9.968 | -60.1937 | 2025-08-23 05:10:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 200.7 |
| 54f12246-07d7-31bd-b7c1-c8e6aad81646 | -5.7431 | -57.5814 | 2025-08-23 05:10:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 82.0 |
| 1a7949cd-70b3-3638-9c96-7736b8d1339a | -15.0761 | -48.4957 | 2025-08-23 05:10:00 | GOES-19 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 39.8 |
| e986e5cd-f45a-3548-852c-32e29e49fba0 | 3.79775 | -60.95918 | 2025-08-23 05:16:00 | NPP-375D | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 3f707d23-4913-3776-ac42-587936193c4e | -5.87859 | -57.7574 | 2025-08-23 05:18:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 58aeb115-ddbc-3923-90cf-4ea7acbc49aa | -5.61556 | -60.22873 | 2025-08-23 05:18:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 60c20423-351c-3b2f-a746-7bc1b4f1c18f | -6.45807 | -53.38797 | 2025-08-23 05:18:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 2d5e39e2-de20-3547-9f2c-9d56d6ed6b7c | -5.43395 | -60.16256 | 2025-08-23 05:18:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 090a20f9-6487-3545-89b0-2249efa8e1c6 | -5.87749 | -57.76443 | 2025-08-23 05:18:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 7.5 |
| 75b2205c-5ed6-3abb-935a-e0feba9dd638 | -6.37232 | -45.54333 | 2025-08-23 05:18:00 | NPP-375D | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 0c0121f3-b262-3d35-b96d-3cb18a00ec83 | -6.16149 | -53.77342 | 2025-08-23 05:18:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 4fe6e52c-d149-316a-a141-bf4d5b206b9f | -5.88094 | -53.6277 | 2025-08-23 05:18:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| bb39fca9-6518-3cb0-a4ed-cda08c7cb7d3 | -7.17351 | -48.4169 | 2025-08-23 05:18:00 | NPP-375D | ARAGUAÍNA | TOCANTINS | Brasil | 1702109 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| be8f30ba-edb7-31a7-8ee4-e9591628c79d | -5.75411 | -57.5858 | 2025-08-23 05:18:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 12.9 |
| a56d4b18-5f84-3dca-86b1-b5d03bb11ddc | -6.65264 | -58.82166 | 2025-08-23 05:18:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 131debfb-b967-33dc-aeaf-24f92a830b38 | -6.68611 | -58.86287 | 2025-08-23 05:18:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 3bb25449-bf50-3683-9781-83ff2d7faf9e | -4.561 | -55.96458 | 2025-08-23 05:18:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 18e61835-d55f-33cb-accc-5438d159be2f | -6.16098 | -53.77691 | 2025-08-23 05:18:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| bfe75b90-2039-3435-a8f0-7671aa32fbfa | -6.28053 | -52.82862 | 2025-08-23 05:18:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 2e6edccf-15b8-3137-afd6-9b19269b3d56 | -5.74518 | -57.59894 | 2025-08-23 05:18:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 9.0 |
| 47b785cb-c436-3b1c-9975-8ad3f995b50a | -6.43671 | -53.3887 | 2025-08-23 05:18:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 4b2b37f0-82cb-35de-902e-fecee63733b5 | -6.44504 | -53.3899 | 2025-08-23 05:18:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| d279c278-d79f-38c4-8371-784ca64cb6f1 | -3.65884 | -54.75488 | 2025-08-23 05:18:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 5415c1f2-26c6-3f80-b31d-331a13f886a8 | -5.80849 | -59.21491 | 2025-08-23 05:18:00 | NPP-375D | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| b55eee22-ea2c-3dfa-a3c8-7191f4cc2f2d | -6.66997 | -58.81409 | 2025-08-23 05:18:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c2ac2c43-8490-3818-86b4-0d471bd4a05f | -6.68666 | -58.8594 | 2025-08-23 05:18:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 3.8 |
| cda1ea26-cd74-3d8d-9541-e380848421cc | -5.74463 | -57.60247 | 2025-08-23 05:18:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 13.6 |
| f5a4acd1-16cd-3819-8a5b-cfb25eb0c0bd | -6.36984 | -45.55623 | 2025-08-23 05:18:00 | NPP-375D | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 4be8dcdd-43b2-34c6-9205-e36af8323c23 | -6.14954 | -57.71576 | 2025-08-23 05:18:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 03837f13-1802-344e-829f-88818cc760af | -6.06164 | -53.89021 | 2025-08-23 05:18:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| b248d117-5bd9-38c4-a182-ad426962e5b2 | -6.72754 | -51.97789 | 2025-08-23 05:18:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 45e370b1-2bb4-37f1-aaad-168f812d57f1 | -5.74407 | -57.60601 | 2025-08-23 05:18:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 13.6 |
| 9186e40e-61a8-30d2-ba8b-402f58c6ae41 | -7.64084 | -46.27895 | 2025-08-23 05:18:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 4379111e-1973-35a2-b978-0f4e1d5f7044 | -6.62549 | -58.53987 | 2025-08-23 05:18:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 583184cf-cd52-3b66-b477-7f24cb6e3d28 | -4.89492 | -55.80878 | 2025-08-23 05:18:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| dc405863-3414-304a-b09c-08c00f2652f6 | -5.87635 | -53.63065 | 2025-08-23 05:18:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 87ed3037-e0aa-3d56-a4d3-c4d8c3017ac8 | -5.88251 | -53.61705 | 2025-08-23 05:18:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 1a686e7c-546e-39c1-b50e-0a0b7a549569 | -5.74798 | -57.60299 | 2025-08-23 05:18:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 13.6 |
| 38264cf4-11f3-3343-b423-2123a6852369 | -5.75692 | -57.58987 | 2025-08-23 05:18:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 14.1 |
| 7d0f2ac1-4c7e-383f-a203-7f7f176e13ef | -6.58026 | -59.87379 | 2025-08-23 05:18:00 | NPP-375D | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 35c717db-a456-321e-bf90-864ef871420d | -6.13377 | -62.61842 | 2025-08-23 05:18:00 | NPP-375D | TAPAUÁ | AMAZONAS | Brasil | 1304104 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 3f19beb4-a938-3442-b5ca-5b606d71ba01 | -6.25841 | -53.6789 | 2025-08-23 05:18:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 37592ffe-716c-308c-b27a-72a16e97ced6 | -6.25596 | -53.66752 | 2025-08-23 05:18:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |


[Clique aqui para ver as próximas entradas](README58.md)
