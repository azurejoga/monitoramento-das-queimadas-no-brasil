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

## Dados Diários - Página 60

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| a8550476-7bb3-35eb-943f-ea2f3578debc | -11.31533 | -47.2675 | 2026-09-19 04:40:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| aabb5b83-57c3-33ec-be8b-7ab97d3a9a5e | -14.66369 | -46.655 | 2026-09-19 04:40:00 | NPP-375D | ALVORADA DO NORTE | GOIÁS | Brasil | 5200803 | 52 | 33 | nan | nan | nan | Cerrado | 7.5 |
| d48987b3-e11f-34b4-96ec-407c1273d28e | -13.73611 | -48.80278 | 2026-09-19 04:40:00 | NPP-375D | FORMOSO | GOIÁS | Brasil | 5208103 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 64349ee1-5ca6-3521-b8c7-fc53b7d7cf99 | -9.88322 | -46.55112 | 2026-09-19 04:40:00 | NPP-375D | SÃO FÉLIX DO TOCANTINS | TOCANTINS | Brasil | 1720150 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 77c7efc4-8b5e-3ec1-9019-83c1d90daa4f | -9.56867 | -45.48244 | 2026-09-19 04:40:00 | NPP-375D | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 59c68fd2-7fda-3ac6-9a72-1aa4cbceddbe | -10.92609 | -53.97207 | 2026-09-19 04:40:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| cd97c59b-2c0c-398b-9a40-38eba102fb0b | -15.05801 | -48.60047 | 2026-09-19 04:40:00 | NPP-375D | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 020c9e43-e170-3841-843d-83d06a41df86 | -11.7689 | -47.43852 | 2026-09-19 04:40:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 0e1dfa50-fe34-38d9-ab17-7b874057e917 | -10.87764 | -54.06151 | 2026-09-19 04:40:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 0353348b-177b-3916-9177-fff3204626b2 | -10.86461 | -56.18871 | 2026-09-19 04:40:00 | NPP-375D | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 72664bc7-8d0e-3a5c-a1a0-e54890f15eef | -15.05698 | -48.58554 | 2026-09-19 04:40:00 | NPP-375D | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 6ae193ab-b7d7-312e-a33d-dbf8a1244497 | -9.8871 | -46.54814 | 2026-09-19 04:40:00 | NPP-375D | SÃO FÉLIX DO TOCANTINS | TOCANTINS | Brasil | 1720150 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| d81cd444-6655-39c2-a7ab-56f09656d450 | -14.78929 | -48.58448 | 2026-09-19 04:40:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 2879f1de-94ee-3129-985c-59b8762eb0e7 | -12.97334 | -46.98532 | 2026-09-19 04:40:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 60932558-87da-31a5-b285-8e3a72bbd303 | -9.25014 | -46.20906 | 2026-09-19 04:40:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| ae506271-4716-3e02-ba7d-0aab45eddb98 | -7.83584 | -55.4135 | 2026-09-19 04:40:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 18a8b5bb-be6c-3195-afb9-75c8c08bdf92 | -9.20669 | -46.76708 | 2026-09-19 04:40:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| e4f51140-b2f3-314f-a1b5-5037df3d3c30 | -9.78695 | -45.06262 | 2026-09-19 04:40:00 | NPP-375D | MONTE ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2206605 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 4256fffd-1d7b-398c-abb6-3e3397f8f60b | -12.28334 | -49.16304 | 2026-09-19 04:40:00 | NPP-375D | ALVORADA | TOCANTINS | Brasil | 1700707 | 17 | 33 | nan | nan | nan | Cerrado | 5.0 |
| c1567023-5437-310e-b603-8cd1408b3015 | -10.92081 | -48.41755 | 2026-09-19 04:40:00 | NPP-375D | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 1d771606-702f-3cb7-852b-31075f89c2a8 | -11.37464 | -47.30239 | 2026-09-19 04:40:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 0.4 |
| d3c6b708-37bc-37b7-85a2-118a4e5987b0 | -12.13864 | -46.99771 | 2026-09-19 04:40:00 | NPP-375D | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| d2bedad9-57a5-3de3-be41-fdbafca65a40 | -9.84035 | -50.65231 | 2026-09-19 04:40:00 | NPP-375D | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 73e902d1-4e83-34f2-b286-7da80653d4f5 | -14.17717 | -48.75484 | 2026-09-19 04:40:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 3db14c3c-8837-31b7-a508-1d6d042632a6 | -12.33706 | -50.733 | 2026-09-19 04:40:00 | NPP-375D | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 09959db6-5269-3738-a328-276cd21f93f5 | -8.16122 | -54.82475 | 2026-09-19 04:40:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 8936a6ce-66cd-37d5-a926-99657d9942d8 | -13.73847 | -48.78815 | 2026-09-19 04:40:00 | NPP-375D | FORMOSO | GOIÁS | Brasil | 5208103 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 410dcc25-ea97-3a7f-9a68-ff7b34ac5c85 | -11.32087 | -47.27562 | 2026-09-19 04:40:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 8f1b81b2-fb75-35c8-83ac-73b4fb6ddd1a | -10.12181 | -45.55996 | 2026-09-19 04:40:00 | NPP-375D | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 01b399a9-a635-3b4d-b660-21ee0cc84c5e | -11.0506 | -48.30585 | 2026-09-19 04:40:00 | NPP-375D | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| c0e91ee9-e015-33ad-b102-e514b8ae48d8 | -12.40491 | -45.05746 | 2026-09-19 04:40:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 983590bb-253f-34bf-a83d-87ca778f68de | -11.478 | -45.73991 | 2026-09-19 04:40:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 5.3 |
| cc9979a9-c232-3cbf-a3f5-3cb5ab455d9b | -11.27642 | -54.11879 | 2026-09-19 04:40:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 8706e487-84a0-3c74-8ca2-bbd810b83ddf | -9.71764 | -54.81012 | 2026-09-19 04:40:00 | NPP-375D | GUARANTÃ DO NORTE | MATO GROSSO | Brasil | 5104104 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| c384104d-7959-346a-90dc-3044a01347d9 | -11.07528 | -48.30231 | 2026-09-19 04:40:00 | NPP-375D | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 4.3 |
| d60d10ec-3f1f-3319-8123-139c4e8c3dc3 | -14.68749 | -46.65882 | 2026-09-19 04:40:00 | NPP-375D | ALVORADA DO NORTE | GOIÁS | Brasil | 5200803 | 52 | 33 | nan | nan | nan | Cerrado | 33.5 |
| 76d2fb94-53a6-365a-af0c-04980c5a9d5d | -8.84125 | -50.44928 | 2026-09-19 04:40:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 33859028-a603-3742-942d-fce27e34162e | -10.70267 | -50.2548 | 2026-09-19 04:40:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| e6f271d1-02a8-3e73-a4a2-50c5bb2e0d66 | -10.62293 | -48.71844 | 2026-09-19 04:40:00 | NPP-375D | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 0117ff8c-ca37-3dda-a51c-937194abc2e8 | -11.48596 | -45.73357 | 2026-09-19 04:40:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 3.1 |
| a61b8b1e-8f80-3946-b02e-5750182b8fba | -10.93076 | -47.85569 | 2026-09-19 04:40:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 8dc5425c-1e52-3d87-929b-efec93eee7ad | -11.05673 | -48.31052 | 2026-09-19 04:40:00 | NPP-375D | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 38633267-0b0d-366b-93f8-7842bdd5caa7 | -13.2357 | -46.94123 | 2026-09-19 04:40:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 2778a68b-a462-39c6-bbf8-fe957aab581e | -11.065 | -49.76683 | 2026-09-19 04:40:00 | NPP-375D | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 2dadeaf8-c101-3926-a642-5cdac15c4aff | -11.47369 | -47.65472 | 2026-09-19 04:40:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 2a9d0e79-867c-37be-877d-dbec51fa0d03 | -9.79295 | -46.08691 | 2026-09-19 04:40:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| a0e761ec-54a8-31bd-bb59-90681cc2feb6 | -13.61292 | -48.32974 | 2026-09-19 04:40:00 | NPP-375D | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| d173ba2f-3c0b-3409-af4f-2fa1f66c8d66 | -14.66993 | -46.65982 | 2026-09-19 04:40:00 | NPP-375D | ALVORADA DO NORTE | GOIÁS | Brasil | 5200803 | 52 | 33 | nan | nan | nan | Cerrado | 5.1 |
| dac25d4a-2e31-3a45-9b56-63c128863ac1 | -13.18898 | -47.03375 | 2026-09-19 04:40:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| e65d9578-18ac-3669-9fc0-2138673544e6 | -10.69841 | -60.73908 | 2026-09-19 04:40:00 | NPP-375D | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 4.0 |
| a323cb2b-0813-3f51-8782-b020c94d93db | -13.6841 | -48.60214 | 2026-09-19 04:40:00 | NPP-375D | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 992bfff8-1d06-346d-a471-fc9326c0b944 | -9.24672 | -45.93544 | 2026-09-19 04:40:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| d9173f96-91a2-3878-af06-09a44fb09c15 | -12.1754 | -48.94883 | 2026-09-19 04:40:00 | NPP-375D | SUCUPIRA | TOCANTINS | Brasil | 1720853 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 2a137feb-d0c3-3dab-b4b6-61e624c439bf | -9.75393 | -46.59935 | 2026-09-19 04:40:00 | NPP-375D | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| d1d24042-ea51-395a-83e5-67578e444252 | -13.39244 | -49.45408 | 2026-09-19 04:40:00 | NPP-375D | PORANGATU | GOIÁS | Brasil | 5218003 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 7f6c8b59-18ef-3ab0-be0c-f8b68b9c566f | -8.61299 | -54.59412 | 2026-09-19 04:40:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| dbf89446-149b-37a7-9253-17eace512ea8 | -15.02712 | -48.55844 | 2026-09-19 04:40:00 | NPP-375D | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| ca91a5bb-aaca-3c00-8383-f415254863ce | -11.0815 | -48.28515 | 2026-09-19 04:40:00 | NPP-375D | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| a6938cd9-c6c0-3794-ab55-c7d4aa4c1368 | -15.05468 | -48.59991 | 2026-09-19 04:40:00 | NPP-375D | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 6113a47a-ecfa-35c6-8c35-f2f47f4da4ac | -12.55521 | -47.07885 | 2026-09-19 04:40:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| c7be48c0-4b60-3572-a9ca-112325dd78ba | -11.83954 | -46.83669 | 2026-09-19 04:40:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| c0dffd67-30a2-397c-bf95-daf5ae0c02a0 | -12.39491 | -45.05191 | 2026-09-19 04:40:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 96856abb-1ddd-3d26-83c7-508c65e627f5 | -9.53817 | -48.68571 | 2026-09-19 04:40:00 | NPP-375D | MIRANORTE | TOCANTINS | Brasil | 1713304 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| e98364cf-2b85-3ed3-aa89-41a7512570f4 | -8.61013 | -54.61007 | 2026-09-19 04:40:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 40089e0a-179e-315b-84b4-c052c50a52ef | -10.69976 | -60.73265 | 2026-09-19 04:40:00 | NPP-375D | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 8.9 |
| 4a67dc6d-ac75-3048-96b0-5038288db5b3 | -11.80339 | -46.79102 | 2026-09-19 04:40:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| edaf23f9-7aae-301e-b741-0d8a3602e7b7 | -16.09323 | -45.13199 | 2026-09-19 04:40:00 | NPP-375D | PINTÓPOLIS | MINAS GERAIS | Brasil | 3150570 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 2a06475b-e442-3f83-9a4e-a3d69ab878ba | -12.54742 | -47.08485 | 2026-09-19 04:40:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| a33d45df-21bf-31e6-882e-93fc88367e42 | -12.27995 | -49.16245 | 2026-09-19 04:40:00 | NPP-375D | ALVORADA | TOCANTINS | Brasil | 1700707 | 17 | 33 | nan | nan | nan | Cerrado | 9.6 |
| 95c11fbb-ab3e-382f-af96-fda346de7ded | -12.68917 | -45.95901 | 2026-09-19 04:40:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 95af6305-5028-3dce-9fe3-e505cb0c8f90 | -11.81599 | -48.83702 | 2026-09-19 04:40:00 | NPP-375D | GURUPI | TOCANTINS | Brasil | 1709500 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| dec898ae-424e-38c3-8392-515af0b15a0e | -9.84109 | -50.6479 | 2026-09-19 04:40:00 | NPP-375D | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 5f9071b8-d791-3636-bb94-a55079c6d4e9 | -10.92476 | -48.4145 | 2026-09-19 04:40:00 | NPP-375D | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 14656754-7934-3c00-9ab0-0f319960af7f | -9.69899 | -48.32092 | 2026-09-19 04:40:00 | NPP-375D | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| f30a6b0b-1992-32c0-85dd-bf500d9670bc | -9.71225 | -45.99775 | 2026-09-19 04:40:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 26bca624-bb11-3849-a9b8-1283361aaead | -12.15256 | -46.9743 | 2026-09-19 04:40:00 | NPP-375D | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 4.8 |
| b51ade12-9546-34c6-9a7b-86f4266eae71 | -9.60546 | -45.37902 | 2026-09-19 04:40:00 | NPP-375D | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 26cd32e1-5377-37b5-884d-28daa9f1194d | -10.62147 | -48.98421 | 2026-09-19 04:40:00 | NPP-375D | NOVA ROSALÂNDIA | TOCANTINS | Brasil | 1715002 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 7d721356-42de-377b-9661-8517e15d215a | -10.9681 | -49.74268 | 2026-09-19 04:40:00 | NPP-375D | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| f1f60859-d97c-3a87-8316-40b3d398c62e | -10.52602 | -44.8451 | 2026-09-19 04:40:00 | NPP-375D | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| ae9ed375-d071-354a-b82b-d003a45bed5b | -10.53301 | -46.73789 | 2026-09-19 04:40:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 21bbf275-45f0-319b-b2bd-02048b703e7b | -11.94468 | -50.12178 | 2026-09-19 04:40:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 9.0 |
| 2478e0a9-2e2c-37e9-9ed5-46f0c95bec9a | -12.41615 | -45.04967 | 2026-09-19 04:40:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 717120cd-5e05-3eae-9e03-4d66db1555f9 | -9.78295 | -45.04265 | 2026-09-19 04:40:00 | NPP-375D | MONTE ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2206605 | 22 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 8e22c7cd-562b-31fe-a107-df571d5655d5 | -12.58684 | -49.10396 | 2026-09-19 04:40:00 | NPP-375D | ALVORADA | TOCANTINS | Brasil | 1700707 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| ff3405a5-520f-34e3-9b01-217556b746f3 | -13.74574 | -48.78566 | 2026-09-19 04:40:00 | NPP-375D | CAMPINORTE | GOIÁS | Brasil | 5204706 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 57c9b486-089e-3d91-8db3-6be341467c1f | -14.18162 | -47.85424 | 2026-09-19 04:40:00 | NPP-375D | ALTO PARAÍSO DE GOIÁS | GOIÁS | Brasil | 5200605 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 22ab9c7a-61b2-3d89-8c7b-e7643f97468c | -10.69153 | -60.7377 | 2026-09-19 04:40:00 | NPP-375D | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 990d644f-4df0-3d4c-bab7-59c9ed1580ca | -9.79911 | -46.09151 | 2026-09-19 04:40:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 290b0d40-d588-33a8-9cb9-9e336075c73f | -9.81276 | -46.39916 | 2026-09-19 04:40:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 34e3eaeb-4cf5-3a5a-9a75-d33b24821d80 | -10.2745 | -50.00431 | 2026-09-19 04:40:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| ce7e5377-ffab-3bd4-adec-708de80658e7 | -8.78046 | -48.68482 | 2026-09-19 04:40:00 | NPP-375D | GUARAÍ | TOCANTINS | Brasil | 1709302 | 17 | 33 | nan | nan | nan | Amazônia | 19.5 |
| ca9dd4dd-0c9d-360b-9732-75083aa528ec | -9.7051 | -54.82446 | 2026-09-19 04:40:00 | NPP-375D | GUARANTÃ DO NORTE | MATO GROSSO | Brasil | 5104104 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 8c9d84fd-77be-37d9-9545-a2e1d85da9b1 | -14.80043 | -48.57901 | 2026-09-19 04:40:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| b5879e95-4af5-3c08-9bb6-c1767989d49b | -11.46504 | -47.64989 | 2026-09-19 04:40:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| dd692fc5-babb-3133-82c9-e9a3be2c1166 | -11.11849 | -45.28415 | 2026-09-19 04:40:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 54360d26-f5bf-30c6-b6d5-79c9dc2f5800 | -10.91737 | -50.86744 | 2026-09-19 04:40:00 | NPP-375D | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 85f293ce-e035-3364-a192-db28c821566c | -11.30885 | -51.72844 | 2026-09-19 04:40:00 | NPP-375D | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 74963e38-2c23-3cbd-896c-171aca960649 | -10.77002 | -46.30604 | 2026-09-19 04:40:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| d71b9feb-24c0-32d6-9e5f-f102db654f30 | -10.87191 | -54.0933 | 2026-09-19 04:40:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |


[Clique aqui para ver as próximas entradas](README61.md)
