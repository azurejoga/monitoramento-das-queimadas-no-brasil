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

## Dados Diários - Página 5

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| e18992b2-3ee3-335e-86e4-ed15218f2d42 | -10.3039 | -57.1418 | 2026-06-27 01:17:00 | METOP-C | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| dea7f977-fa22-3660-8744-36c0c0b93dbb | -12.9443 | -56.646999 | 2026-06-27 01:17:00 | METOP-C | NOVA MUTUM | MATO GROSSO | Brasil | 5106224 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| e475eac1-3dac-30c6-8aa7-f4e1143de222 | -12.9345 | -56.6493 | 2026-06-27 01:17:00 | METOP-C | NOVA MUTUM | MATO GROSSO | Brasil | 5106224 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 200446ad-7db4-34c4-8fd6-bb3acff8f7b1 | -12.2233 | -56.561199 | 2026-06-27 01:17:00 | METOP-C | ITANHANGÁ | MATO GROSSO | Brasil | 5104542 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 4810ac10-e8f6-3081-b9d6-52a9a2ec9be4 | -13.2512 | -54.417702 | 2026-06-27 01:17:00 | METOP-C | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 52909d40-1d38-3725-9c1a-fe09eafd724e | -13.675 | -53.940102 | 2026-06-27 01:17:00 | METOP-C | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 1edb6d53-1454-39b1-a779-fd6910943c9b | -12.4639 | -58.494099 | 2026-06-27 01:17:00 | METOP-C | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 4d1cb759-7621-3bba-b220-98a0c807c844 | -12.4557 | -58.503399 | 2026-06-27 01:17:00 | METOP-C | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| d4575776-c442-3ff1-9fa0-4bf9819a89d5 | -12.1759 | -59.755699 | 2026-06-27 01:17:00 | METOP-C | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 3045e0bb-ee61-35fa-80fe-dedc96dcb0ee | -12.9427 | -56.6399 | 2026-06-27 01:17:00 | METOP-C | NOVA MUTUM | MATO GROSSO | Brasil | 5106224 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| d5858fde-3a90-3812-963d-1bca2b3f9215 | -10.6338 | -50.2113 | 2026-06-27 01:17:00 | METOP-C | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 0c7c1d85-6e7d-3ae3-9f6c-e79b833074bb | -14.8833 | -54.544998 | 2026-06-27 01:17:00 | METOP-C | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 18b011b4-dbfe-30b8-a0ac-87a1295df7bf | -12.6189 | -57.896198 | 2026-06-27 01:17:00 | METOP-C | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 9820a861-4da7-3b17-8143-2a230cb868e1 | -11.6467 | -54.884998 | 2026-06-27 01:17:00 | METOP-C | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 23159a14-a6cc-31b4-820f-aa91bee57125 | -9.0393 | -61.331402 | 2026-06-27 01:17:00 | METOP-C | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 77861f3c-fb5c-390a-a985-a90a7ebe6e97 | -13.2317 | -54.422501 | 2026-06-27 01:17:00 | METOP-C | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| d799e8d0-7b87-35af-93bc-76cd15a0bb79 | -12.9394 | -56.625702 | 2026-06-27 01:17:00 | METOP-C | NOVA MUTUM | MATO GROSSO | Brasil | 5106224 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| ecc42ebe-0255-3cd9-8c8d-19b5aeb44946 | -12.6286 | -57.894001 | 2026-06-27 01:17:00 | METOP-C | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 078689b0-9ec3-3578-a6ff-c6ceddf161ce | -12.4655 | -58.501202 | 2026-06-27 01:17:00 | METOP-C | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 033fe471-8293-3a58-ab2c-6ad0dcb63fc7 | -13.2336 | -54.430801 | 2026-06-27 01:17:00 | METOP-C | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 1e816c2b-2c41-3e56-b9cb-44c919ea4981 | -11.3213 | -54.471199 | 2026-06-27 01:17:00 | METOP-C | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| bf899021-33af-33c9-ba25-6c65cbc67299 | -10.704 | -50.2439 | 2026-06-27 01:17:00 | METOP-C | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 5cdc3584-9235-3ef9-b2e6-0ed99c3d1d55 | -10.908 | -56.852901 | 2026-06-27 01:17:00 | METOP-C | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| ac3a7121-05cc-34bc-855c-65dd4738e1ca | -10.9373 | -56.8461 | 2026-06-27 01:17:00 | METOP-C | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| fc455ad3-4c2a-340f-962a-3a227f215f46 | -12.6173 | -57.889198 | 2026-06-27 01:17:00 | METOP-C | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 78d233c1-1caa-3353-91e8-6a4c80195b9f | -9.5954 | -56.931999 | 2026-06-27 01:17:00 | METOP-C | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| be89f57f-3d0e-3350-a828-572da033c777 | -12.4525 | -58.489201 | 2026-06-27 01:17:00 | METOP-C | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 347e46a5-eae6-3ccd-9a10-349233a2d0b8 | -10.6516 | -50.240601 | 2026-06-27 01:17:00 | METOP-C | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 659cdbde-fc2b-3764-8fe1-7179c829767b | -12.9329 | -56.6422 | 2026-06-27 01:17:00 | METOP-C | NOVA MUTUM | MATO GROSSO | Brasil | 5106224 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 2ea0449a-6c94-30d2-b267-4b0e7b01dc5b | -10.3055 | -57.148899 | 2026-06-27 01:17:00 | METOP-C | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 87d750a8-e1a2-3225-a484-95cf934d8b0d | -10.5389 | -53.7075 | 2026-06-27 01:17:00 | METOP-C | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 2738a045-4fa1-3da8-a690-9922f6525218 | -13.2473 | -54.401299 | 2026-06-27 01:17:00 | METOP-C | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 76fc1043-d1bb-3b65-b7c1-bc9acb931f5d | -12.6059 | -57.884499 | 2026-06-27 01:17:00 | METOP-C | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| bb171a46-43ef-3425-af1d-75f26828ad48 | -12.4541 | -58.4963 | 2026-06-27 01:17:00 | METOP-C | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 7d5bf19c-a2a6-33e8-9b6a-69e073fa40b5 | -14.8796 | -54.529301 | 2026-06-27 01:17:00 | METOP-C | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 5026132f-2cb1-305e-b17e-5c3956724357 | -12.6043 | -57.877499 | 2026-06-27 01:17:00 | METOP-C | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| fa2c9a0e-be60-318e-869d-55ebbb5d362a | -11.6487 | -54.893101 | 2026-06-27 01:17:00 | METOP-C | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 291d9816-392d-3412-8eef-8914877521ca | -10.9097 | -56.860001 | 2026-06-27 01:17:00 | METOP-C | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 718e3889-26c8-3f84-a099-d928ce1db35e | -13.6439 | -55.296001 | 2026-06-27 01:17:00 | METOP-C | SANTA RITA DO TRIVELATO | MATO GROSSO | Brasil | 5107768 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| abcfcd11-6ae0-3b13-9bf9-39d3dee72c1a | -12.9313 | -56.635101 | 2026-06-27 01:17:00 | METOP-C | NOVA MUTUM | MATO GROSSO | Brasil | 5106224 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 8def755d-0900-30fe-bf62-d8df08a91fa2 | -6.5835 | -51.112202 | 2026-06-27 01:17:00 | METOP-C | OURILÂNDIA DO NORTE | PARÁ | Brasil | 1505437 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 8652ee9a-5a99-3ec1-a13c-4f70b7483a27 | -10.7936 | -56.759499 | 2026-06-27 01:17:00 | METOP-C | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 379cef5e-7e28-3ddb-bc28-3ee3e9b04557 | -13.261 | -54.415401 | 2026-06-27 01:17:00 | METOP-C | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 6bae31bd-187a-3463-a8bf-9c5585f56633 | -12.4608 | -58.4799 | 2026-06-27 01:17:00 | METOP-C | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| ce8cd8e0-30ac-3efc-9a9e-aeff817ae13e | -11.9219 | -57.409901 | 2026-06-27 01:17:00 | METOP-C | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 4d790c8a-35f4-3605-b792-17a06e0759f7 | -13.6632 | -53.933998 | 2026-06-27 01:17:00 | METOP-C | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 200447cc-5064-3714-9805-97232f3232ee | -12.6157 | -57.882198 | 2026-06-27 01:17:00 | METOP-C | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| a9838bca-febf-31af-ad55-3a4aec830b98 | -12.6302 | -57.901001 | 2026-06-27 01:17:00 | METOP-C | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| c070302d-4232-34a0-acaf-0c25c8c3ea30 | -12.4623 | -58.487 | 2026-06-27 01:17:00 | METOP-C | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| b7402ea0-ca7d-3b4e-b574-627fa601fcf5 | -14.8814 | -54.537102 | 2026-06-27 01:17:00 | METOP-C | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 54f418a7-c2ef-347b-b210-af9c7e9d8a13 | -10.3153 | -57.146599 | 2026-06-27 01:17:00 | METOP-C | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 04972a17-3f75-38e2-8d04-00f63b096232 | -13.2493 | -54.4095 | 2026-06-27 01:17:00 | METOP-C | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 92e08fba-9485-3662-85c1-0709895f5d65 | -12.7983 | -54.861599 | 2026-06-27 01:17:00 | METOP-C | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| b1ba0d7c-499c-344d-9b42-e84255a7c05a | -12.6271 | -57.887001 | 2026-06-27 01:17:00 | METOP-C | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| cc7e02b3-66d0-3df9-9ba0-0df91476e4c3 | -10.551 | -53.714699 | 2026-06-27 01:17:00 | METOP-C | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| c928c0d4-bbe9-3ab1-8994-8123e1cda07e | -13.259 | -54.407101 | 2026-06-27 01:17:00 | METOP-C | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| a7329615-bb65-3349-81ac-dc1784c6cbfe | -11.6506 | -54.901199 | 2026-06-27 01:17:00 | METOP-C | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| cb3498a3-d942-3d36-9c26-ae0e1cc66276 | -10.6395 | -50.192902 | 2026-06-27 01:17:00 | METOP-C | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 70c0ba50-b417-3c3d-96e0-4c135c655ff3 | -10.3494 | -50.1479 | 2026-06-27 01:17:00 | METOP-C | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| fddecdba-ee24-32ff-938b-054a9d46590e | -9.0376 | -61.323299 | 2026-06-27 01:17:00 | METOP-C | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| d9582186-2991-3c95-8a77-990796fa7b4f | -9.5921 | -56.917702 | 2026-06-27 01:17:00 | METOP-C | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| f928de29-ce35-3018-8159-82ee49d1b0c5 | -12.6075 | -57.891499 | 2026-06-27 01:17:00 | METOP-C | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 752fcae0-bc5f-375a-9bb1-3325fcd8e439 | -11.9138 | -57.419102 | 2026-06-27 01:17:00 | METOP-C | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 3195996d-6e71-37d4-bba5-6ce70a2b1078 | -10.6613 | -50.238098 | 2026-06-27 01:17:00 | METOP-C | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| d2b81e90-be82-32b8-93a4-1f6b30a4f7eb | -10.5412 | -53.717098 | 2026-06-27 01:17:00 | METOP-C | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 5da40ef0-4b92-379e-afdc-bf66613db9d6 | -10.6379 | -50.2272 | 2026-06-27 01:17:00 | METOP-C | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| b3d70daf-dd14-3271-9455-3cf49e8c5be8 | -10.3137 | -57.1395 | 2026-06-27 01:17:00 | METOP-C | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 41d18a3f-7dd0-3d70-985b-c3b1f3537091 | -13.6652 | -53.942501 | 2026-06-27 01:17:00 | METOP-C | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| c07cb9ec-30b6-3d88-a25b-282663422a4e | -10.6573 | -50.222198 | 2026-06-27 01:17:00 | METOP-C | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 442d99c6-abf9-3291-a0dc-e75b048659ff | -10.6476 | -50.224701 | 2026-06-27 01:17:00 | METOP-C | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 2aafc4e1-a773-3456-b47f-73efca0efc29 | -10.9406 | -56.860298 | 2026-06-27 01:17:00 | METOP-C | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| e9f8f16f-2dc0-35b6-a9da-800a2ce41e48 | -9.5938 | -56.9249 | 2026-06-27 01:17:00 | METOP-C | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 64e67245-d7dc-3716-9e36-b1c3ea8d3ca4 | -10.792 | -56.752399 | 2026-06-27 01:17:00 | METOP-C | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 8ec90d86-53f8-3169-8a95-2f94ff0dd538 | -11.9095 | -57.4134 | 2026-06-27 01:20:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 46.5 |
| ada02c76-de94-38c1-acc5-d64fddec9676 | -12.4654 | -58.481 | 2026-06-27 01:20:00 | GOES-19 | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 83.4 |
| a027769e-8386-3aa3-92bf-650b8855cdec | -12.8161 | -44.3689 | 2026-06-27 01:20:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 54.8 |
| 91caf339-503f-38e1-a67e-501a931825a3 | -13.6671 | -53.9314 | 2026-06-27 01:20:00 | GOES-19 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Cerrado | 50.6 |
| 4d3389b3-8056-3652-a79a-a433b68f26ae | -5.7758 | -45.0599 | 2026-06-27 01:20:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 111.4 |
| 1076a47a-f859-3a70-8720-9c811d33d616 | -7.755 | -44.1805 | 2026-06-27 01:20:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 72.7 |
| 214c6abb-8743-3e1b-823a-62c16813bb55 | -12.4651 | -58.5009 | 2026-06-27 01:20:00 | GOES-19 | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 108.8 |
| 1374f563-4544-3648-a014-b9daeec51779 | -12.6236 | -57.8926 | 2026-06-27 01:20:00 | GOES-19 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 112.9 |
| 9acb5bfb-f29d-3683-81d5-8756dcb39550 | -10.6571 | -50.2212 | 2026-06-27 01:20:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 46.4 |
| 7d9287f6-e71c-322a-99dd-fc8bdb0efee3 | -12.8359 | -44.3422 | 2026-06-27 01:20:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 200.3 |
| cada15ed-4b5c-3ff1-af9a-3e5fdb2f843e | -5.7756 | -45.0826 | 2026-06-27 01:20:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 66.1 |
| 233f5236-524a-36b1-b70b-0ad17354f24a | -10.6385 | -50.2018 | 2026-06-27 01:20:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 83.1 |
| 460dc754-2e7a-3c43-84cc-685b8c903fc9 | -10.6382 | -50.2232 | 2026-06-27 01:20:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 89.7 |
| 97bfedea-0b3e-3dc5-a9eb-a4de52f2ba8d | -5.7945 | -45.0586 | 2026-06-27 01:20:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 57.3 |
| 96bef751-3b99-35d0-92d7-7c80c5209670 | -12.4462 | -58.5023 | 2026-06-27 01:20:00 | GOES-19 | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 48.6 |
| f59cfc19-f5fa-3e95-be43-f3155f65c074 | -12.8354 | -44.3657 | 2026-06-27 01:20:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 102.8 |
| 23cc339e-7bbf-353e-807a-981f501164aa | -12.8165 | -44.3454 | 2026-06-27 01:20:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 153.2 |
| ba54c88b-e76d-368a-8c13-61491ec88003 | -7.7361 | -44.1823 | 2026-06-27 01:20:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 133.5 |
| 2ec1cf71-a60d-3573-b4c5-e67ee24c2801 | -10.5634 | -46.2362 | 2026-06-27 01:20:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 106.5 |
| e8b20029-9f3c-3dcd-9e38-c9fa2e05025f | -12.6046 | -57.8942 | 2026-06-27 01:20:00 | GOES-19 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 71.8 |
| d698b449-4cd4-3fe4-8716-b9fb8f868df3 | -5.7758 | -45.0599 | 2026-06-27 01:30:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 125.1 |
| d9c13f23-e210-31c3-8081-88325602134c | -10.6382 | -50.2232 | 2026-06-27 01:30:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 71.6 |
| 40b17bda-2104-39f2-8ffb-209d793f8121 | -12.4464 | -58.4825 | 2026-06-27 01:30:00 | GOES-19 | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 42.2 |
| d250d697-b426-3845-b214-b616b3a57f93 | -12.4651 | -58.5009 | 2026-06-27 01:30:00 | GOES-19 | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 100.4 |
| 17e48b1c-5ef6-3fa4-a1af-899a6721de84 | -12.8359 | -44.3422 | 2026-06-27 01:30:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 235.5 |
| 180eeea3-823f-3eb5-ad52-7a1363a7f557 | -7.755 | -44.1805 | 2026-06-27 01:30:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 84.1 |
| 3e3e79a3-c519-3358-9e3e-c6aa89dfe9da | -12.6046 | -57.8942 | 2026-06-27 01:30:00 | GOES-19 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 60.0 |


[Clique aqui para ver as próximas entradas](README6.md)
