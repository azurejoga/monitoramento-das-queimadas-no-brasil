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

## Dados Diários - Página 53

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 60db93a7-0443-30f0-abc2-8c77a144f261 | -10.7963 | -50.82134 | 2026-09-21 04:21:00 | NOAA-20 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 6fc270c4-d8eb-3196-ba2c-31c165cf3808 | -10.26445 | -49.9889 | 2026-09-21 04:21:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 1b2b33c5-9360-3ec4-aa07-0c1fe67b6f7d | -9.71262 | -47.0996 | 2026-09-21 04:21:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 44de23c9-2557-3cd5-a61d-8b3f11579b28 | -10.09452 | -50.26365 | 2026-09-21 04:21:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 13.4 |
| c07898ec-2304-38b5-acd1-a9398589a47a | -16.03379 | -52.51318 | 2026-09-21 04:21:00 | NOAA-20 | PONTAL DO ARAGUAIA | MATO GROSSO | Brasil | 5106653 | 51 | 33 | nan | nan | nan | Cerrado | 164.8 |
| 87c28827-e259-31db-9e03-214af17cfc8b | -11.1981 | -42.86209 | 2026-09-21 04:21:00 | NOAA-20 | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Caatinga | 1.3 |
| ea9caefe-2335-36ff-a08e-61c331c04874 | -10.54322 | -54.49479 | 2026-09-21 04:21:00 | NOAA-20 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| cc52ba54-6219-3025-955e-dd04398b5bab | -16.31147 | -53.87081 | 2026-09-21 04:23:00 | NOAA-20 | GUIRATINGA | MATO GROSSO | Brasil | 5104203 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| f9306482-d652-3e89-bcdf-e76222e64ddc | -19.41071 | -46.39862 | 2026-09-21 04:23:00 | NOAA-20 | IBIÁ | MINAS GERAIS | Brasil | 3129509 | 31 | 33 | nan | nan | nan | Cerrado | 7.0 |
| 22be1e24-079a-3948-ab30-fd5de31914ab | -17.75553 | -46.99344 | 2026-09-21 04:23:00 | NOAA-20 | GUARDA-MOR | MINAS GERAIS | Brasil | 3128600 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 734bf610-b791-342d-8eee-a9baf5ffec0a | -17.22989 | -51.7625 | 2026-09-21 04:23:00 | NOAA-20 | CAIAPÔNIA | GOIÁS | Brasil | 5204409 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| d6cfc60e-ca55-3e0d-9971-9c2d01b1388a | -16.39492 | -54.72057 | 2026-09-21 04:23:00 | NOAA-20 | RONDONÓPOLIS | MATO GROSSO | Brasil | 5107602 | 51 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 2be3686f-3ac3-3d10-a992-8830a4f9ffb5 | -20.15645 | -45.42136 | 2026-09-21 04:23:00 | NOAA-20 | SANTO ANTÔNIO DO MONTE | MINAS GERAIS | Brasil | 3160405 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 73b67751-45d2-3856-a89b-a87b7dd50c89 | -18.97713 | -43.75673 | 2026-09-21 04:23:00 | NOAA-20 | SANTANA DE PIRAPAMA | MINAS GERAIS | Brasil | 3158508 | 31 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 9f4092d2-9375-357a-9170-5e34915ac5aa | -19.12346 | -46.60308 | 2026-09-21 04:23:00 | NOAA-20 | SERRA DO SALITRE | MINAS GERAIS | Brasil | 3166808 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 0775acfd-7d9f-358e-9a2c-b4981113ca30 | -19.08157 | -46.65195 | 2026-09-21 04:23:00 | NOAA-20 | SERRA DO SALITRE | MINAS GERAIS | Brasil | 3166808 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| d0d1dbd3-86a6-3285-a42b-a76961e59079 | -19.41791 | -46.39614 | 2026-09-21 04:23:00 | NOAA-20 | IBIÁ | MINAS GERAIS | Brasil | 3129509 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 3ddce3cc-defd-3438-a82d-55953a832657 | -17.23411 | -51.76316 | 2026-09-21 04:23:00 | NOAA-20 | CAIAPÔNIA | GOIÁS | Brasil | 5204409 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 855ada88-65f7-362b-b2af-151ee09aad0f | -16.3189 | -53.84417 | 2026-09-21 04:23:00 | NOAA-20 | GUIRATINGA | MATO GROSSO | Brasil | 5104203 | 51 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 2bc55e1b-0802-36fb-a0d2-fc9e8442cbf5 | -16.31245 | -53.83966 | 2026-09-21 04:23:00 | NOAA-20 | GUIRATINGA | MATO GROSSO | Brasil | 5104203 | 51 | 33 | nan | nan | nan | Cerrado | 2.7 |
| b9be0c86-6e59-346f-954e-c909b1022354 | -19.41228 | -46.41015 | 2026-09-21 04:23:00 | NOAA-20 | IBIÁ | MINAS GERAIS | Brasil | 3129509 | 31 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 0b66b53e-b96d-36b3-ae5e-c71ade1442d1 | -19.41559 | -46.41074 | 2026-09-21 04:23:00 | NOAA-20 | IBIÁ | MINAS GERAIS | Brasil | 3129509 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 4ddf1dde-0bbc-3d44-93ee-6976ed594baa | -16.30936 | -53.84111 | 2026-09-21 04:23:00 | NOAA-20 | GUIRATINGA | MATO GROSSO | Brasil | 5104203 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| dbffa558-7063-358d-9ebe-cfb5444dbec9 | -19.41832 | -46.41497 | 2026-09-21 04:23:00 | NOAA-20 | IBIÁ | MINAS GERAIS | Brasil | 3129509 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| c06a51ae-99e4-34e5-99d3-2f001fba6830 | -16.3956 | -54.71726 | 2026-09-21 04:23:00 | NOAA-20 | RONDONÓPOLIS | MATO GROSSO | Brasil | 5107602 | 51 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 8a5dc3be-ad6a-3d10-b87a-8943395378f0 | -16.32736 | -53.85262 | 2026-09-21 04:23:00 | NOAA-20 | GUIRATINGA | MATO GROSSO | Brasil | 5104203 | 51 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 7dc49125-5614-3dd6-9cde-db1689a63641 | -18.79131 | -46.47099 | 2026-09-21 04:23:00 | NOAA-20 | LAGOA FORMOSA | MINAS GERAIS | Brasil | 3137502 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| f123f9db-9570-3195-bcd4-2801c4848013 | -18.8515 | -48.21858 | 2026-09-21 04:23:00 | NOAA-20 | UBERLÂNDIA | MINAS GERAIS | Brasil | 3170206 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 6d151edd-aa55-3f12-900d-fc9a2fe97ca2 | -19.42122 | -46.39673 | 2026-09-21 04:23:00 | NOAA-20 | IBIÁ | MINAS GERAIS | Brasil | 3129509 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 9cadc91a-7331-3406-8fe2-0685cd864be0 | -18.03222 | -50.93692 | 2026-09-21 04:23:00 | NOAA-20 | RIO VERDE | GOIÁS | Brasil | 5218805 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 07f7a2bf-7300-3491-8fd6-1a837090b154 | -18.85281 | -48.2108 | 2026-09-21 04:23:00 | NOAA-20 | UBERLÂNDIA | MINAS GERAIS | Brasil | 3170206 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 6d6fb819-4ea2-3bd5-a5ba-ede912770581 | -19.41848 | -46.3925 | 2026-09-21 04:23:00 | NOAA-20 | IBIÁ | MINAS GERAIS | Brasil | 3129509 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 93571264-2467-3171-b530-7a0dccf1a29b | -16.31417 | -53.84245 | 2026-09-21 04:23:00 | NOAA-20 | GUIRATINGA | MATO GROSSO | Brasil | 5104203 | 51 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 4c44eb90-ecb0-314e-bf3d-a21345059dbb | -16.40005 | -54.72176 | 2026-09-21 04:23:00 | NOAA-20 | RONDONÓPOLIS | MATO GROSSO | Brasil | 5107602 | 51 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 36a727d1-8848-3aaa-bd0b-efcd1455f191 | -16.32369 | -53.84558 | 2026-09-21 04:23:00 | NOAA-20 | GUIRATINGA | MATO GROSSO | Brasil | 5104203 | 51 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 1bcf3d4f-9c64-3c85-93c3-2998625141fe | -18.5416 | -48.20376 | 2026-09-21 04:23:00 | NOAA-20 | ARAGUARI | MINAS GERAIS | Brasil | 3103504 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 443ac2f3-0806-3154-ac6f-13f8d6566eea | -16.31719 | -53.8414 | 2026-09-21 04:23:00 | NOAA-20 | GUIRATINGA | MATO GROSSO | Brasil | 5104203 | 51 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 9fc89398-a7a6-3e55-9965-909bbdee5098 | -17.22567 | -51.76178 | 2026-09-21 04:23:00 | NOAA-20 | CAIAPÔNIA | GOIÁS | Brasil | 5204409 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 61e893ad-4aba-30b0-9678-f4df9670c58e | -18.03615 | -50.93768 | 2026-09-21 04:23:00 | NOAA-20 | RIO VERDE | GOIÁS | Brasil | 5218805 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 8558a8fb-854b-3646-a6ff-63449219ce3e | -18.8536 | -48.2271 | 2026-09-21 04:23:00 | NOAA-20 | UBERLÂNDIA | MINAS GERAIS | Brasil | 3170206 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 2555cd7b-e11e-397d-abb4-deb7a7267a71 | -18.04105 | -50.93316 | 2026-09-21 04:23:00 | NOAA-20 | RIO VERDE | GOIÁS | Brasil | 5218805 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 6e735aa3-686a-3e14-befe-5b7d6894e7e3 | -19.4146 | -46.39556 | 2026-09-21 04:23:00 | NOAA-20 | IBIÁ | MINAS GERAIS | Brasil | 3129509 | 31 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 64002bc1-dbd6-3ab9-bc76-7aced7d14bea | -17.66102 | -49.88853 | 2026-09-21 04:23:00 | NOAA-20 | VICENTINÓPOLIS | GOIÁS | Brasil | 5222054 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| bd0d43e5-7a05-3d97-8b01-ced45c4d035e | -19.87151 | -42.6389 | 2026-09-21 04:23:00 | NOAA-20 | DIONÍSIO | MINAS GERAIS | Brasil | 3121803 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| e7159200-5a21-3f6c-999b-aff80a976877 | -16.30452 | -53.83991 | 2026-09-21 04:23:00 | NOAA-20 | GUIRATINGA | MATO GROSSO | Brasil | 5104203 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 65912168-c469-31ee-a558-0f2004de5124 | -19.41129 | -46.39497 | 2026-09-21 04:23:00 | NOAA-20 | IBIÁ | MINAS GERAIS | Brasil | 3129509 | 31 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 22117f94-6081-309b-87c1-710c35aa8a49 | -18.53818 | -48.20312 | 2026-09-21 04:23:00 | NOAA-20 | ARAGUARI | MINAS GERAIS | Brasil | 3103504 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 37262e4a-ee1f-3cac-b0cd-ed2c7210c424 | -16.32196 | -53.84299 | 2026-09-21 04:23:00 | NOAA-20 | GUIRATINGA | MATO GROSSO | Brasil | 5104203 | 51 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 65cd8a13-3cc5-3e8d-b05a-b6c2f9dd80ff | -16.30762 | -53.83842 | 2026-09-21 04:23:00 | NOAA-20 | GUIRATINGA | MATO GROSSO | Brasil | 5104203 | 51 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 60eb2e7b-7b99-391d-9095-ab82dc2a725c | -16.32566 | -53.85004 | 2026-09-21 04:23:00 | NOAA-20 | GUIRATINGA | MATO GROSSO | Brasil | 5104203 | 51 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 4f9bca5f-abee-3bbd-a3f3-06b3fb83d9fc | -17.23332 | -51.76736 | 2026-09-21 04:23:00 | NOAA-20 | CAIAPÔNIA | GOIÁS | Brasil | 5204409 | 52 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 833b3f3d-5ddb-3b9d-b732-e465544d033d | -21.59312 | -41.33167 | 2026-09-21 04:23:00 | NOAA-20 | CAMPOS DOS GOYTACAZES | RIO DE JANEIRO | Brasil | 3301009 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 2750bff4-b2db-3392-aa72-3d463350bb89 | -17.42289 | -46.67492 | 2026-09-21 04:23:00 | NOAA-20 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| fe14cbf0-0471-3af7-a9ee-d38e79a2fc44 | -19.41344 | -46.40285 | 2026-09-21 04:23:00 | NOAA-20 | IBIÁ | MINAS GERAIS | Brasil | 3129509 | 31 | 33 | nan | nan | nan | Cerrado | 7.0 |
| 5d3c8076-6313-31b5-ac8e-2e827a54a910 | -19.06355 | -47.0179 | 2026-09-21 04:23:00 | NOAA-20 | PATROCÍNIO | MINAS GERAIS | Brasil | 3148103 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 2103773a-f86e-3237-8fae-0590aed7b870 | -18.85216 | -48.21467 | 2026-09-21 04:23:00 | NOAA-20 | UBERLÂNDIA | MINAS GERAIS | Brasil | 3170206 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| b5ea5187-3e05-32a7-9f7a-a62079380ef2 | -19.41501 | -46.41438 | 2026-09-21 04:23:00 | NOAA-20 | IBIÁ | MINAS GERAIS | Brasil | 3129509 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| d844c0b0-3ed7-39bc-a6e1-fe15fa40f422 | -19.41286 | -46.40651 | 2026-09-21 04:23:00 | NOAA-20 | IBIÁ | MINAS GERAIS | Brasil | 3129509 | 31 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 8113779c-d0be-3fc5-ba4b-65c9e42332b5 | -19.41518 | -46.39191 | 2026-09-21 04:23:00 | NOAA-20 | IBIÁ | MINAS GERAIS | Brasil | 3129509 | 31 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 1b1cc7d2-edb2-3829-9435-321a673aa6fe | -16.30643 | -53.84454 | 2026-09-21 04:23:00 | NOAA-20 | GUIRATINGA | MATO GROSSO | Brasil | 5104203 | 51 | 33 | nan | nan | nan | Cerrado | 2.7 |
| faf7c2b3-c90f-3f94-b563-6c190b856c80 | -18.63037 | -46.85862 | 2026-09-21 04:23:00 | NOAA-20 | COROMANDEL | MINAS GERAIS | Brasil | 3119302 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 83fd9666-ad10-3460-ae4b-fe34ca7ee2fb | -18.97771 | -43.75277 | 2026-09-21 04:23:00 | NOAA-20 | SANTANA DE PIRAPAMA | MINAS GERAIS | Brasil | 3158508 | 31 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 7546fe8b-954d-3fe6-91ff-08076c8cdb00 | -16.31258 | -53.86511 | 2026-09-21 04:23:00 | NOAA-20 | GUIRATINGA | MATO GROSSO | Brasil | 5104203 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 790e86a9-80cd-352d-8763-12fbeb049cf6 | -19.04364 | -46.90847 | 2026-09-21 04:23:00 | NOAA-20 | PATROCÍNIO | MINAS GERAIS | Brasil | 3148103 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| e48d7a2a-7c08-30b8-8664-630aab2fbfce | -28.52459 | -48.83158 | 2026-09-21 04:25:00 | NOAA-20 | LAGUNA | SANTA CATARINA | Brasil | 4209409 | 42 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| b6cd1689-f4d4-383f-9729-deda82ce37aa | -26.75269 | -49.59746 | 2026-09-21 04:25:00 | NOAA-20 | DOUTOR PEDRINHO | SANTA CATARINA | Brasil | 4205159 | 42 | 33 | nan | nan | nan | Mata Atlântica | 2.5 |
| 7dfbc782-d71d-3fd9-b075-9a2bc0e16e55 | -22.03708 | -56.05663 | 2026-09-21 04:25:00 | NOAA-20 | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 2.6 |
| c43fc217-242f-387e-8194-7e3255f17c68 | -28.73955 | -49.3531 | 2026-09-21 04:25:00 | NOAA-20 | CRICIÚMA | SANTA CATARINA | Brasil | 4204608 | 42 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 3b48e896-51c5-36eb-b008-b9598cde833b | -26.75336 | -49.59348 | 2026-09-21 04:25:00 | NOAA-20 | DOUTOR PEDRINHO | SANTA CATARINA | Brasil | 4205159 | 42 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| d3664111-9039-3bee-8993-a2cded4f315e | -9.5593 | -66.0545 | 2026-09-21 04:30:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 42.4 |
| ffdca9a3-764f-3f68-860f-351ea07d8ba7 | 1.54504 | -55.80236 | 2026-09-21 05:01:00 | NOAA-21 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| cc652b32-6d88-332b-8d1c-3b7295bd9ea0 | 1.74283 | -60.57068 | 2026-09-21 05:01:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 1f4537a3-f384-3819-87e1-c2ee18c31a89 | 2.34522 | -60.91331 | 2026-09-21 05:01:00 | NOAA-21 | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b7fb7aef-64c5-33c7-afa7-db695e8f8430 | 1.44483 | -50.76659 | 2026-09-21 05:01:00 | NOAA-21 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b468e8e4-7e60-3e12-94e6-c9e7fc3f02d5 | 1.38741 | -50.92342 | 2026-09-21 05:01:00 | NOAA-21 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 1.2 |
| bc392f72-c9bb-3e9a-8200-486eaf9d0d46 | 1.65816 | -50.93134 | 2026-09-21 05:01:00 | NOAA-21 | PRACUÚBA | AMAPÁ | Brasil | 1600550 | 16 | 33 | nan | nan | nan | Amazônia | 0.9 |
| d5d9a29b-1096-3beb-8d2c-1ccd1596848a | 4.527 | -60.85978 | 2026-09-21 05:01:00 | NOAA-21 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 7.1 |
| 8bc72751-8020-3fc7-8570-bb84ade9e036 | 1.53828 | -55.8034 | 2026-09-21 05:01:00 | NOAA-21 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 3fc3c366-842b-342b-83a9-551f4437893a | 1.67262 | -50.92907 | 2026-09-21 05:01:00 | NOAA-21 | PRACUÚBA | AMAPÁ | Brasil | 1600550 | 16 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 747bd14c-5583-3e70-a1fe-0ad574e3c380 | 1.54166 | -55.80288 | 2026-09-21 05:01:00 | NOAA-21 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 382f981a-d765-377b-a5e9-36e37a314548 | 4.52581 | -60.86349 | 2026-09-21 05:01:00 | NOAA-21 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 8.6 |
| 51b76680-86f1-3811-8ca9-e9c5cfceab5c | 4.08091 | -61.40347 | 2026-09-21 05:01:00 | NOAA-21 | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 1565b7d5-cebd-3bd3-ab8f-28b540c5b36b | 1.77273 | -60.23359 | 2026-09-21 05:01:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 95ac229c-4b05-300c-976f-7e045226bb97 | 2.31774 | -60.91737 | 2026-09-21 05:01:00 | NOAA-21 | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 1.8 |
| e0511016-559f-35a8-a161-84ab899f4614 | 1.669 | -50.92963 | 2026-09-21 05:01:00 | NOAA-21 | PRACUÚBA | AMAPÁ | Brasil | 1600550 | 16 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 542fb913-42b4-3d52-8d33-e9067c3fefd5 | 1.54223 | -55.80652 | 2026-09-21 05:01:00 | NOAA-21 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| c4f54e55-92b8-3dc5-b207-8296f352089f | 3.6809 | -61.86703 | 2026-09-21 05:01:00 | NOAA-21 | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d71e1bdb-33c0-326e-8185-e27c548612e0 | 1.94211 | -50.96735 | 2026-09-21 05:01:00 | NOAA-21 | AMAPÁ | AMAPÁ | Brasil | 1600105 | 16 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 8b5a22df-0e5b-3ab9-8f1a-8f7949863fb0 | 4.52236 | -60.86106 | 2026-09-21 05:01:00 | NOAA-21 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 4.0 |
| f28d5203-e5dc-33ca-8e4b-3f6ccc822059 | 4.12513 | -61.29902 | 2026-09-21 05:01:00 | NOAA-21 | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 1aec8af6-f9b2-3c95-ab5e-464424ca153d | 2.40653 | -50.96594 | 2026-09-21 05:01:00 | NOAA-21 | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c441c2e1-f8ed-36ac-9306-94b7af4f33a9 | 0.84257 | -52.58372 | 2026-09-21 05:01:00 | NOAA-21 | PEDRA BRANCA DO AMAPARI | AMAPÁ | Brasil | 1600154 | 16 | 33 | nan | nan | nan | Amazônia | 0.7 |
| be97af24-284b-3b99-a556-d619d97a0ea1 | 4.53218 | -60.8623 | 2026-09-21 05:01:00 | NOAA-21 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 1e5bbb22-80aa-396e-b313-2199c351d5e4 | 1.21926 | -50.97714 | 2026-09-21 05:01:00 | NOAA-21 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 1.5 |
| c90df718-154b-3032-a027-259e7c2c1f8a | 1.66835 | -50.92545 | 2026-09-21 05:01:00 | NOAA-21 | PRACUÚBA | AMAPÁ | Brasil | 1600550 | 16 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 79aba2fa-504a-3d91-81c3-fd41d0811f7b | 1.55236 | -55.80492 | 2026-09-21 05:01:00 | NOAA-21 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 6dc4e035-5c77-3315-8e42-f4d464e6b94a | 4.12997 | -61.29833 | 2026-09-21 05:01:00 | NOAA-21 | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 91c6eda8-7577-35ce-a3c5-ca858c3e1aa1 | 1.55127 | -55.82016 | 2026-09-21 05:01:00 | NOAA-21 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 20a7e41f-d12c-3a01-a835-49b2647a6e97 | 1.53885 | -55.80705 | 2026-09-21 05:01:00 | NOAA-21 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a99e7915-6359-315d-8077-6d17df05e6ce | 1.05684 | -51.18748 | 2026-09-21 05:01:00 | NOAA-21 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 1.4 |


[Clique aqui para ver as próximas entradas](README54.md)
