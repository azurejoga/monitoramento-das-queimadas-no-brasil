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

## Dados Diários - Página 11

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| e47a3f1c-7cf4-3004-aa16-8a0e772d40dc | -5.6079 | -45.0265 | 2025-09-05 01:20:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 72.9 |
| 4130239b-1fdb-35b5-a49d-1fa468b665e4 | -8.0035 | -45.4373 | 2025-09-05 01:20:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 65.6 |
| 908139cc-113a-3b34-94e7-761d98828d72 | -9.2102 | -57.0918 | 2025-09-05 01:20:00 | GOES-19 | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 53.2 |
| a5fc9852-dec3-3d36-ae81-1317f3b0027f | -9.2477 | -57.0697 | 2025-09-05 01:20:00 | GOES-19 | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 48.8 |
| c5dd9812-e9b7-3a57-8dea-c6eeea53a363 | -5.4799 | -60.128399 | 2025-09-05 01:25:00 | METOP-C | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 997742b0-862f-31bb-9c0a-1f009fee4b9f | -12.8778 | -56.9431 | 2025-09-05 01:25:00 | METOP-C | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| b69197e9-d2bb-37b8-b0bd-26675bfbec0c | -9.2938 | -56.809101 | 2025-09-05 01:25:00 | METOP-C | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 311ffd31-87e0-3ab7-837c-39ee62bb0112 | -12.8893 | -56.948101 | 2025-09-05 01:25:00 | METOP-C | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| bae11173-e5d4-3614-ad36-289824a195af | -15.192 | -52.372501 | 2025-09-05 01:25:00 | METOP-C | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 8bd6f574-c4f5-3659-8da3-74b6554f9e0a | -15.2143 | -52.378601 | 2025-09-05 01:25:00 | METOP-C | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 0baeaa05-2dcd-35ef-9e82-01de71647727 | -10.5191 | -57.769798 | 2025-09-05 01:25:00 | METOP-C | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| d59fe510-e9f4-3e57-a78a-9d5df9bc891b | -12.901 | -56.998798 | 2025-09-05 01:25:00 | METOP-C | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 2f5b80b2-b311-3f05-ad6a-05c7625c2fc9 | -9.0594 | -47.002399 | 2025-09-05 01:25:00 | METOP-C | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 9ec7cd47-a551-356c-adff-2017756d900c | -12.4807 | -53.842899 | 2025-09-05 01:25:00 | METOP-C | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| c342b764-72ff-3e70-acc3-0b7719efc735 | -17.6574 | -52.279301 | 2025-09-05 01:25:00 | METOP-C | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 342f1d38-61d2-392b-b886-649cea1396bf | -12.9959 | -54.815601 | 2025-09-05 01:25:00 | METOP-C | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 551eae6f-5a41-394c-a2c6-2b01f9079b4e | -12.982 | -54.800499 | 2025-09-05 01:25:00 | METOP-C | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| a0dd0d0e-37d4-3426-9939-d29c8e478f07 | -15.199 | -52.358898 | 2025-09-05 01:25:00 | METOP-C | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 47942012-dd36-3bc4-9450-479bcd5d91d9 | -10.4174 | -60.7383 | 2025-09-05 01:25:00 | METOP-C | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 23702ab6-8443-33ec-871d-b892f367138c | -12.8795 | -56.950401 | 2025-09-05 01:25:00 | METOP-C | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 5473997a-f8e1-33fd-9cfa-fda61a89fed2 | -7.5179 | -61.668301 | 2025-09-05 01:25:00 | METOP-C | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 60037cac-2d9b-3c75-848c-b48c5cc40477 | -11.6371 | -54.542099 | 2025-09-05 01:25:00 | METOP-C | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 14b3f3a7-87a7-3952-929d-af5b5be6f6f2 | -15.7187 | -53.621601 | 2025-09-05 01:25:00 | METOP-C | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| c359a4bd-ddd4-3afc-8978-a4ea2d9dae8b | -9.2316 | -57.072102 | 2025-09-05 01:25:00 | METOP-C | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 57db75de-42cc-35a1-9f04-e4ddbb4c2c0b | -16.308599 | -52.944 | 2025-09-05 01:25:00 | METOP-C | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 220f3294-9693-36b4-8b74-703658807d1f | -5.4897 | -60.126202 | 2025-09-05 01:25:00 | METOP-C | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| e97d1e1f-ec4b-3452-ae27-7846f801543b | -13.0 | -54.832901 | 2025-09-05 01:25:00 | METOP-C | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| f212e8b6-182c-3158-86a6-71407bdc9cb0 | -12.9841 | -54.809299 | 2025-09-05 01:25:00 | METOP-C | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 6c845219-7ffe-37ea-a99a-40247e1889b1 | -9.2138 | -57.084301 | 2025-09-05 01:25:00 | METOP-C | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 153e7397-1c2a-36e3-a27d-754b815724fe | -11.1932 | -55.016701 | 2025-09-05 01:25:00 | METOP-C | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| c6e88868-a1ac-3b71-8abc-f2bd7cc11663 | -10.5208 | -57.776901 | 2025-09-05 01:25:00 | METOP-C | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| e7803bb5-4176-36f6-93c0-beb1385b68ea | -15.7164 | -53.612301 | 2025-09-05 01:25:00 | METOP-C | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 58cb4876-1df8-3024-b3db-d1b40c1a22b2 | -15.8461 | -52.294102 | 2025-09-05 01:25:00 | METOP-C | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 64098dbf-d426-3f15-b9ca-39b1fe19b0ef | -12.9882 | -54.826599 | 2025-09-05 01:25:00 | METOP-C | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 4200c218-861b-37b3-affb-64cd833aca45 | -9.069 | -46.999802 | 2025-09-05 01:25:00 | METOP-C | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 58e85028-a3c3-3f2d-bec9-3cd17038b096 | -12.9638 | -54.768002 | 2025-09-05 01:25:00 | METOP-C | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| dec38e60-9fd6-3d9c-93f7-2551184e1b23 | -12.9603 | -54.7966 | 2025-09-05 01:25:00 | METOP-C | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| a908531b-baf0-3198-a26a-ab615a7321c8 | -12.9979 | -54.8242 | 2025-09-05 01:25:00 | METOP-C | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| be5d33b6-505f-3a62-be45-64bf95da6f15 | -12.9778 | -54.7831 | 2025-09-05 01:25:00 | METOP-C | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 73624327-29e9-3773-9a27-3e804c97300b | -9.7008 | -51.0728 | 2025-09-05 01:25:00 | METOP-C | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 6ee72f61-2d4d-3f1f-934c-1b3044ce70bf | -20.8862 | -54.986401 | 2025-09-05 01:25:00 | METOP-C | SIDROLÂNDIA | MATO GROSSO DO SUL | Brasil | 5007901 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| 77787794-f3cc-3596-90f0-09778d0081e0 | -9.212 | -57.076698 | 2025-09-05 01:25:00 | METOP-C | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 6e652fac-e6fc-3ece-8d80-b358e4a55ca5 | -22.4874 | -52.766399 | 2025-09-05 01:25:00 | METOP-C | ROSANA | SÃO PAULO | Brasil | 3544251 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| a6e03629-1cae-38aa-90de-29bc9bdb67b4 | -11.6195 | -52.205502 | 2025-09-05 01:25:00 | METOP-C | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 9006691a-e429-3f48-bacc-72548ed9ba9d | -5.5011 | -60.130901 | 2025-09-05 01:25:00 | METOP-C | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 9e7eacd2-348f-3ea7-9554-805db06b0cae | -12.968 | -54.7855 | 2025-09-05 01:25:00 | METOP-C | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 5d701e1c-a25d-361e-9dbb-0d9e0bc43289 | -8.5204 | -51.338501 | 2025-09-05 01:25:00 | METOP-C | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b5294c79-cd34-387f-b139-e363acd9cd1a | -5.4815 | -60.1353 | 2025-09-05 01:25:00 | METOP-C | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| fd171ae1-0ef0-367d-bd50-3e82ca188a58 | -7.5163 | -61.6609 | 2025-09-05 01:25:00 | METOP-C | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| cd414d07-fb44-319a-afa6-266967608094 | -12.9659 | -54.776798 | 2025-09-05 01:25:00 | METOP-C | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| ec580e3a-35fa-3908-83b0-924ea8aeda96 | -10.2246 | -50.537998 | 2025-09-05 01:25:00 | METOP-C | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 4f4536cf-f065-3301-a65a-6410750d2247 | -9.5114 | -57.786301 | 2025-09-05 01:25:00 | METOP-C | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| ff59ff95-1d9c-3cc4-9cb0-0ec51dfbf139 | -9.2334 | -57.0797 | 2025-09-05 01:25:00 | METOP-C | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 78c2bb75-76a1-3181-a58f-a4fa373109e0 | -9.253 | -57.0751 | 2025-09-05 01:25:00 | METOP-C | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| a41399ae-8b8a-3e19-aa06-435b14e406bb | -12.9582 | -54.787899 | 2025-09-05 01:25:00 | METOP-C | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| a94a2bed-0665-3164-a9a3-1a821bd1fc16 | -12.9862 | -54.818001 | 2025-09-05 01:25:00 | METOP-C | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 805a9889-14fd-33f6-b1ed-7ba6235e3602 | -9.4984 | -57.819401 | 2025-09-05 01:25:00 | METOP-C | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 19281e8c-1301-3934-ada9-9875899e1086 | -11.6446 | -54.530399 | 2025-09-05 01:25:00 | METOP-C | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| d003ac55-35a6-3555-954a-e02a2ba75bb6 | -10.511 | -57.779202 | 2025-09-05 01:25:00 | METOP-C | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| d966d197-c569-3f43-ab5b-5444327c8f38 | -11.6424 | -54.521099 | 2025-09-05 01:25:00 | METOP-C | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| ad1dcf57-1d83-38fd-9701-b5c142eb6535 | -16.545401 | -55.125999 | 2025-09-05 01:25:00 | METOP-C | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 903b9cbd-5315-3d08-a76c-d2bb989a8a21 | -5.4979 | -60.117199 | 2025-09-05 01:25:00 | METOP-C | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 08573e22-5336-33df-8e52-c2a860380fca | -12.9903 | -54.8353 | 2025-09-05 01:25:00 | METOP-C | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 53ea7b01-2544-3692-8837-02d53252870d | 0.3073 | -59.494301 | 2025-09-05 01:25:00 | METOP-C | SÃO JOÃO DA BALIZA | RORAIMA | Brasil | 1400506 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| 8e6c979c-6eab-3f09-bd65-bb9a0eea7dd2 | -9.9876 | -60.010201 | 2025-09-05 01:25:00 | METOP-C | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| f5c6efca-272d-3ff1-8eba-1c0e9e8bb3b8 | -11.6324 | -52.2159 | 2025-09-05 01:25:00 | METOP-C | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 355b8cf0-77cd-391c-94c2-95a9715b0f3f | -9.2512 | -57.067501 | 2025-09-05 01:25:00 | METOP-C | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| fe541e5d-929a-3603-90d8-d7ad3b1d4c31 | -12.9561 | -54.779202 | 2025-09-05 01:25:00 | METOP-C | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| f5df12f2-3e51-3d3c-a6e9-7e583f0a2edb | -13.8028 | -56.5681 | 2025-09-05 01:25:00 | METOP-C | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 5b744763-108b-3384-8a54-0063094369ad | -13.0926 | -57.112999 | 2025-09-05 01:25:00 | METOP-C | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 3a4bf775-5f4f-363c-87af-56987a86b9e0 | -15.2018 | -52.369999 | 2025-09-05 01:25:00 | METOP-C | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 1a18a92b-ad6b-3161-8b7e-02431c76bbce | -5.7247 | -49.298599 | 2025-09-05 01:25:00 | METOP-C | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 8682d162-ae19-34a9-8b2d-630a05992dc3 | -7.7218 | -61.521599 | 2025-09-05 01:25:00 | METOP-C | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 3d5db7e6-f706-32ec-90aa-e0c4757d127d | -11.1911 | -55.007801 | 2025-09-05 01:25:00 | METOP-C | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| c4699e0b-81e3-36e7-a309-e4383fcbf913 | -11.6349 | -54.532799 | 2025-09-05 01:25:00 | METOP-C | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 7c9e5505-8eb3-37e9-bfa9-02dcc333253e | -20.882799 | -54.971199 | 2025-09-05 01:25:00 | METOP-C | SIDROLÂNDIA | MATO GROSSO DO SUL | Brasil | 5007901 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| 0a3911c7-749c-321c-93c4-88b63bd00ff3 | -11.6469 | -54.5397 | 2025-09-05 01:25:00 | METOP-C | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 0d588aad-bcf2-3f97-a496-326b27233852 | -9.3259 | -55.202499 | 2025-09-05 01:25:00 | METOP-C | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 74a27282-a191-3e89-bfdc-21fbab650bc0 | -10.4609 | -53.6189 | 2025-09-05 01:25:00 | METOP-C | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| f9cdc0da-e155-366c-bb00-a87ec2ca34e9 | -9.2155 | -57.091801 | 2025-09-05 01:25:00 | METOP-C | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 0fabaa89-06a8-3e71-8fc6-2be00879813c | -10.5093 | -57.772099 | 2025-09-05 01:25:00 | METOP-C | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 2c9931bd-8d77-3449-bb55-071dfdfbe51a | -5.4881 | -60.1194 | 2025-09-05 01:25:00 | METOP-C | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| e035d4dd-5ec9-33ee-9685-41ae7b164ddd | -8.5163 | -51.321899 | 2025-09-05 01:25:00 | METOP-C | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 1055c00c-a955-3c2a-914f-8ceb0ee06319 | -20.884501 | -54.978802 | 2025-09-05 01:25:00 | METOP-C | SIDROLÂNDIA | MATO GROSSO DO SUL | Brasil | 5007901 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| 6c054e4b-72ee-3205-a0d8-91b4bbec8eee | -12.9764 | -54.8204 | 2025-09-05 01:25:00 | METOP-C | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| bc6e4622-9b27-3bfc-9627-f63947071729 | -5.8532 | -57.767799 | 2025-09-05 01:25:00 | METOP-C | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 06c3f426-9dab-3150-bac4-c6ea4a8ab314 | -16.553301 | -55.115799 | 2025-09-05 01:25:00 | METOP-C | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 33b5d1e5-347c-33a5-9ba2-22033e4b816a | -10.4995 | -57.7743 | 2025-09-05 01:25:00 | METOP-C | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 75b533b5-d6f4-3dc0-9932-36f862dac4e7 | -12.5246 | -53.810699 | 2025-09-05 01:25:00 | METOP-C | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| e1fd9d19-d681-3b75-b757-adf88a12b057 | -9.2432 | -57.0774 | 2025-09-05 01:25:00 | METOP-C | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 7a20d6bd-8cb4-37fd-ae1d-acd18fe1eae8 | -10.2342 | -50.5355 | 2025-09-05 01:25:00 | METOP-C | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| bc86c9b8-dce7-39ae-a27a-f2b650feb5ee | -16.555201 | -55.1236 | 2025-09-05 01:25:00 | METOP-C | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 677ff2ed-54cc-38a3-877f-24aa043027ad | -13.2985 | -51.643101 | 2025-09-05 01:25:00 | METOP-C | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 3a595cf0-dd55-36ba-b240-f196071a119e | -10.1421 | -55.158699 | 2025-09-05 01:25:00 | METOP-C | MATUPÁ | MATO GROSSO | Brasil | 5105606 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 608d159c-a6c7-3f75-968b-f03eac8a4d9f | -10.4706 | -53.616501 | 2025-09-05 01:25:00 | METOP-C | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| d75103ce-52d8-3eee-b008-da6a4344e90e | -5.7183 | -49.273102 | 2025-09-05 01:25:00 | METOP-C | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| cb06083d-c4f5-3089-a27f-082fd932bc9e | -7.2273 | -56.8475 | 2025-09-05 01:25:00 | METOP-C | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 4ba8eb04-60c1-314c-92c3-9ad55202cd12 | -9.986 | -60.003201 | 2025-09-05 01:25:00 | METOP-C | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 752414b3-1ea7-301e-b756-65cd9cd652b7 | -11.5806 | -52.174198 | 2025-09-05 01:25:00 | METOP-C | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 70c2a1a5-0b21-3b67-98cf-7076bd38328a | -15.7518 | -53.672298 | 2025-09-05 01:25:00 | METOP-C | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | nan |


[Clique aqui para ver as próximas entradas](README12.md)
