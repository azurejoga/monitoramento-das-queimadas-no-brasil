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

## Dados Diários - Página 177

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 2e66b47f-4323-387e-89e2-b2e83b08f3cf | -18.9102 | -49.1674 | 2024-09-26 12:16:51 | GOES-16 | MONTE ALEGRE DE MINAS | MINAS GERAIS | Brasil | 3142809 | 31 | 33 | nan | nan | nan | Mata Atlântica | 241.9 |
| 3988c420-f8a9-35f8-a0fd-7aa631086436 | -20.7971 | -48.9496 | 2024-09-26 12:17:01 | GOES-16 | OLÍMPIA | SÃO PAULO | Brasil | 3533908 | 35 | 33 | nan | nan | nan | Mata Atlântica | 126.7 |
| efd5ac9a-8744-3588-864a-47cd11c459d2 | -20.7223 | -49.4471 | 2024-09-26 12:17:01 | GOES-16 | SÃO JOSÉ DO RIO PRETO | SÃO PAULO | Brasil | 3549805 | 35 | 33 | nan | nan | nan | Cerrado | 164.5 |
| bb111aec-d465-372e-8ee2-6dec05efcbad | -21.2733 | -51.0061 | 2024-09-26 12:17:04 | GOES-16 | VALPARAÍSO | SÃO PAULO | Brasil | 3556305 | 35 | 33 | nan | nan | nan | Mata Atlântica | 150.8 |
| f6387287-41d5-348b-b926-5a4848567c94 | -22.2243 | -48.6625 | 2024-09-26 12:17:09 | GOES-16 | ITAPUÍ | SÃO PAULO | Brasil | 3522901 | 35 | 33 | nan | nan | nan | Mata Atlântica | 216.0 |
| e6a93ede-eaa4-3097-91b2-50cb70c7d025 | -7.2905 | -61.106 | 2024-09-26 12:25:48 | GOES-16 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 78.0 |
| b5cbf70a-4bf1-31fa-8d21-2c2218919402 | -9.4168 | -51.4636 | 2024-09-26 12:26:00 | GOES-16 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 380.0 |
| 2f4a78c3-5fca-3aea-ae6a-912724986c75 | -9.4165 | -51.4846 | 2024-09-26 12:26:00 | GOES-16 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 147.1 |
| f8ba4fe1-27ab-3992-9d95-56853ed38740 | -10.2034 | -46.1904 | 2024-09-26 12:26:04 | GOES-16 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 101.7 |
| 6dc61833-7124-32c4-a8ce-c8e68402d15e | -10.032 | -53.5065 | 2024-09-26 12:26:04 | GOES-16 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 208.4 |
| 98488392-a820-3263-b047-3b392340e924 | -10.6073 | -51.1196 | 2024-09-26 12:26:07 | GOES-16 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 84.4 |
| da75e77d-b1af-32d8-83a0-0b99f756f6d6 | -11.1351 | -46.185 | 2024-09-26 12:26:09 | GOES-16 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 145.4 |
| 22c9fc57-7ad3-3f9a-bf7a-0ea771cd3ce9 | -11.1354 | -46.1623 | 2024-09-26 12:26:09 | GOES-16 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 120.6 |
| 87f00474-e4f8-3a1e-aeb0-34afacb67f4e | -11.6985 | -47.8798 | 2024-09-26 12:26:12 | GOES-16 | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 94.4 |
| b773bb3b-7bbc-3625-bb9b-59b64236f91c | -11.7179 | -47.8551 | 2024-09-26 12:26:12 | GOES-16 | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 162.9 |
| dc034970-98da-3b3e-9b70-b4d69d3d8689 | -11.6988 | -47.8576 | 2024-09-26 12:26:12 | GOES-16 | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 96.7 |
| 68f8c661-cf53-3a48-9f70-f7737e604191 | -11.8422 | -49.635 | 2024-09-26 12:26:13 | GOES-16 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 75.7 |
| d85c2df8-f463-3ecb-8ec4-4bdc9029292e | -11.8419 | -49.6567 | 2024-09-26 12:26:13 | GOES-16 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 73.9 |
| 8f07023c-0eec-3e4c-b4a4-7f218e9db03c | -11.9365 | -47.3367 | 2024-09-26 12:26:14 | GOES-16 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 90.9 |
| 2320ad84-e718-3443-ad6f-a8bf01269452 | -12.2179 | -45.4844 | 2024-09-26 12:26:15 | GOES-16 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 258.3 |
| ab304c53-3526-39e4-baf2-dc41d78c8047 | -12.2367 | -45.5045 | 2024-09-26 12:26:15 | GOES-16 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 240.6 |
| fd248177-613c-3e3a-b74a-8a7e57882dd6 | -12.5273 | -53.5168 | 2024-09-26 12:26:17 | GOES-16 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 86.7 |
| a4fb0092-eca0-37d0-a42f-27054614d79e | -12.5026 | -48.9198 | 2024-09-26 12:26:17 | GOES-16 | TALISMÃ | TOCANTINS | Brasil | 1720978 | 17 | 33 | nan | nan | nan | Cerrado | 150.8 |
| 06a73b8c-e45d-3c02-aa94-0fe88287c2be | -12.4835 | -48.9224 | 2024-09-26 12:26:17 | GOES-16 | TALISMÃ | TOCANTINS | Brasil | 1720978 | 17 | 33 | nan | nan | nan | Cerrado | 79.6 |
| dccc92dc-b718-3a0a-b12c-a30f9143129f | -12.4612 | -47.9774 | 2024-09-26 12:26:17 | GOES-16 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 203.8 |
| 8ad7d988-0ebf-3e9b-8a08-ffb94ca937c3 | -12.5464 | -53.5147 | 2024-09-26 12:26:18 | GOES-16 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 163.8 |
| 1f0bc7a4-80f1-350c-b64f-7a9994b130ba | -12.9516 | -45.3242 | 2024-09-26 12:26:19 | GOES-16 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 103.7 |
| b1805559-a437-3289-9dc9-ca703dec4f1f | -12.952 | -45.301 | 2024-09-26 12:26:19 | GOES-16 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 108.4 |
| 5ca0c108-0abb-39bd-a190-2e0b89e67ce4 | -12.7914 | -51.1525 | 2024-09-26 12:26:19 | GOES-16 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 305.0 |
| 033606e2-56e6-329a-a97a-75a2b1d6be16 | -12.9714 | -45.2979 | 2024-09-26 12:26:19 | GOES-16 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 168.9 |
| 5e014077-abac-3636-aec8-78e0d4ece560 | -12.7911 | -51.1739 | 2024-09-26 12:26:19 | GOES-16 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 169.7 |
| eeeb6fff-f050-3cf1-ac9b-df73a7088d4b | -12.8102 | -51.1716 | 2024-09-26 12:26:19 | GOES-16 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 240.3 |
| 39e1f7a9-8c8d-3749-bad1-4d037b4f06cc | -13.1963 | -45.6308 | 2024-09-26 12:26:20 | GOES-16 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 92.3 |
| 61db3f2a-873d-3072-804c-402436dfa132 | -13.2985 | -46.3247 | 2024-09-26 12:26:21 | GOES-16 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 70.8 |
| eaf51ec7-3d2e-3cef-bb08-1d62eeef86bb | -14.5705 | -45.6973 | 2024-09-26 12:26:28 | GOES-16 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 69.8 |
| 8f7d72f6-24b1-393b-a68f-6583b1fe2fe3 | -14.571 | -45.674 | 2024-09-26 12:26:28 | GOES-16 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 70.3 |
| b1bc6cfa-d7ae-3b97-9ec7-d69ebd545cae | -14.8828 | -51.4777 | 2024-09-26 12:26:30 | GOES-16 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 60.3 |
| 5ff1077c-f242-32a5-90f2-efa040b181cd | -16.3138 | -45.6693 | 2024-09-26 12:26:37 | GOES-16 | SÃO ROMÃO | MINAS GERAIS | Brasil | 3164209 | 31 | 33 | nan | nan | nan | Cerrado | 68.4 |
| add8141f-2010-38fc-85d7-12b464433d86 | -17.8851 | -47.0217 | 2024-09-26 12:26:46 | GOES-16 | GUARDA-MOR | MINAS GERAIS | Brasil | 3128600 | 31 | 33 | nan | nan | nan | Cerrado | 77.0 |
| 3b4610aa-ef8a-3702-b419-192c6dd92fa9 | -18.9102 | -49.1674 | 2024-09-26 12:26:51 | GOES-16 | MONTE ALEGRE DE MINAS | MINAS GERAIS | Brasil | 3142809 | 31 | 33 | nan | nan | nan | Mata Atlântica | 294.0 |
| c8549ad0-5b34-35b2-8032-9607ee520b04 | -20.7971 | -48.9496 | 2024-09-26 12:27:01 | GOES-16 | OLÍMPIA | SÃO PAULO | Brasil | 3533908 | 35 | 33 | nan | nan | nan | Mata Atlântica | 157.3 |
| 5c6fbbb6-b96d-3654-8956-3b645fbb3027 | -21.2733 | -51.0061 | 2024-09-26 12:27:04 | GOES-16 | VALPARAÍSO | SÃO PAULO | Brasil | 3556305 | 35 | 33 | nan | nan | nan | Mata Atlântica | 226.7 |
| b0f8a509-91d7-3a1f-85e4-c32c09e104ff | -21.9374 | -48.5688 | 2024-09-26 12:27:07 | GOES-16 | BOA ESPERANÇA DO SUL | SÃO PAULO | Brasil | 3506706 | 35 | 33 | nan | nan | nan | Cerrado | 121.8 |
| eb9c858a-d2ad-3ea3-8a63-a74d87dfa3fd | -22.2243 | -48.6625 | 2024-09-26 12:27:09 | GOES-16 | ITAPUÍ | SÃO PAULO | Brasil | 3522901 | 35 | 33 | nan | nan | nan | Mata Atlântica | 198.6 |
| 0c97e652-1500-36e5-a330-8fa648616578 | -8.6722 | -38.149 | 2024-09-26 12:35:55 | GOES-16 | FLORESTA | PERNAMBUCO | Brasil | 2605707 | 26 | 33 | nan | nan | nan | Caatinga | 113.6 |
| 3e240981-2919-3203-bb39-40110dd07bf9 | -10.2224 | -46.188 | 2024-09-26 12:36:04 | GOES-16 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 83.5 |
| 6e1f9301-97f4-3c4d-9e82-0ba571225214 | -10.2034 | -46.1904 | 2024-09-26 12:36:04 | GOES-16 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 134.1 |
| 847f34be-6bcf-3b1c-919d-2eeeefbb0113 | -10.032 | -53.5065 | 2024-09-26 12:36:04 | GOES-16 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 237.2 |
| ea0baf22-d5e4-3492-ae80-b40995de9127 | -10.4371 | -45.7992 | 2024-09-26 12:36:05 | GOES-16 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 73.7 |
| 16a31653-8261-3987-a33e-0e1436e5e1a7 | -10.8352 | -45.8843 | 2024-09-26 12:36:07 | GOES-16 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 122.4 |
| f4661b58-d04e-346a-8854-5a920ab4cd8f | -10.8348 | -45.907 | 2024-09-26 12:36:07 | GOES-16 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 136.0 |
| ae6108e5-aa1c-3be4-83c8-805274d01b83 | -10.6073 | -51.1196 | 2024-09-26 12:36:07 | GOES-16 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 81.5 |
| bee2db72-d9be-3e8e-bd20-9cfef9aa19b3 | -10.8542 | -45.8818 | 2024-09-26 12:36:08 | GOES-16 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 95.1 |
| 86cec968-d320-324f-ae3d-df0e80ff6f41 | -10.8522 | -51.1792 | 2024-09-26 12:36:08 | GOES-16 | PORTO ALEGRE DO NORTE | MATO GROSSO | Brasil | 5106778 | 51 | 33 | nan | nan | nan | Cerrado | 74.1 |
| f283babe-6e79-3f78-b6e1-f189b4d25b24 | -10.8525 | -51.1581 | 2024-09-26 12:36:08 | GOES-16 | PORTO ALEGRE DO NORTE | MATO GROSSO | Brasil | 5106778 | 51 | 33 | nan | nan | nan | Cerrado | 119.3 |
| 210415bd-1532-3c7a-bfb3-32c169190998 | -10.8714 | -51.1561 | 2024-09-26 12:36:08 | GOES-16 | PORTO ALEGRE DO NORTE | MATO GROSSO | Brasil | 5106778 | 51 | 33 | nan | nan | nan | Cerrado | 87.0 |
| 97d6857a-61e8-3a90-88a3-097c4ec04cd3 | -11.1351 | -46.185 | 2024-09-26 12:36:09 | GOES-16 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 208.9 |
| 0e89ffdf-8bbd-3767-beaf-855b2d9e429c | -11.1354 | -46.1623 | 2024-09-26 12:36:09 | GOES-16 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 174.1 |
| d298f1e5-50cf-36aa-9aea-e7e8c2ae00bc | -11.6988 | -47.8576 | 2024-09-26 12:36:12 | GOES-16 | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 72.1 |
| 29b4c2fa-3876-3873-9208-d01e8234ba6c | -11.7179 | -47.8551 | 2024-09-26 12:36:12 | GOES-16 | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 116.7 |
| b3988fa2-cbdb-3dd1-83f8-e0c9a57d00aa | -11.8422 | -49.635 | 2024-09-26 12:36:13 | GOES-16 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 86.2 |
| c74e3440-ceb6-38d4-9211-e8c82e214811 | -11.8419 | -49.6567 | 2024-09-26 12:36:13 | GOES-16 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 77.5 |
| f4289e71-94ea-397f-9ee9-4e80e496807d | -11.9365 | -47.3367 | 2024-09-26 12:36:14 | GOES-16 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 67.2 |
| e6e77b03-c3fd-31f8-81c1-8a004d3041d3 | -12.2367 | -45.5045 | 2024-09-26 12:36:15 | GOES-16 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 229.0 |
| 66fc59d3-6762-3cbd-9b1c-3fb4fdefec7b | -12.2179 | -45.4844 | 2024-09-26 12:36:15 | GOES-16 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 259.9 |
| 193e3cff-b0b3-34d7-b1cf-1dfd342a812b | -12.5026 | -48.9198 | 2024-09-26 12:36:17 | GOES-16 | TALISMÃ | TOCANTINS | Brasil | 1720978 | 17 | 33 | nan | nan | nan | Cerrado | 157.1 |
| 665d5242-253b-360e-83d1-8d3c7be09580 | -12.5273 | -53.5168 | 2024-09-26 12:36:17 | GOES-16 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 100.4 |
| 79e6db21-7c29-3ef7-87b8-85b0eea69bdf | -12.4835 | -48.9224 | 2024-09-26 12:36:17 | GOES-16 | TALISMÃ | TOCANTINS | Brasil | 1720978 | 17 | 33 | nan | nan | nan | Cerrado | 82.8 |
| 8629b216-bfe3-30bd-9449-84f7cf409b1f | -12.4612 | -47.9774 | 2024-09-26 12:36:17 | GOES-16 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 183.9 |
| ada30801-255c-3a16-81f9-620824656cd8 | -12.7158 | -45.569 | 2024-09-26 12:36:18 | GOES-16 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 107.0 |
| f54c63c6-36e6-3e56-8431-8f9f2b0cab25 | -12.5464 | -53.5147 | 2024-09-26 12:36:18 | GOES-16 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 198.8 |
| ba9129e5-5207-3e98-be4a-ba2715d3979d | -12.8106 | -51.1502 | 2024-09-26 12:36:19 | GOES-16 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 338.8 |
| a66ed715-5320-3cdb-9500-bcf16d1873ed | -12.7911 | -51.1739 | 2024-09-26 12:36:19 | GOES-16 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 65.1 |
| 2da483c0-31db-34ef-803b-1cda57acd56f | -12.8102 | -51.1716 | 2024-09-26 12:36:19 | GOES-16 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 92.5 |
| a840c471-712e-324a-a2ef-71158a13dd6d | -12.7914 | -51.1525 | 2024-09-26 12:36:19 | GOES-16 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 186.4 |
| c8633970-feb1-3748-a221-adf279ddf058 | -13.1603 | -45.4983 | 2024-09-26 12:36:20 | GOES-16 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 111.6 |
| 9e8c9b82-e4c2-3645-aff3-e0f4e36ff672 | -13.1796 | -45.4952 | 2024-09-26 12:36:20 | GOES-16 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 171.2 |
| 423fffbf-e12e-3b25-ad3c-9eb8b43941c3 | -13.1963 | -45.6308 | 2024-09-26 12:36:20 | GOES-16 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 96.3 |
| 279d10b0-b93f-391e-b5e7-13e18f3fb63b | -13.1418 | -48.5464 | 2024-09-26 12:36:20 | GOES-16 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 108.2 |
| eebeb71e-1278-33d9-9701-95d409f39376 | -13.1607 | -45.4752 | 2024-09-26 12:36:20 | GOES-16 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 143.7 |
| 7be96b19-184c-32c7-b91a-811870742a48 | -14.5705 | -45.6973 | 2024-09-26 12:36:28 | GOES-16 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 73.9 |
| 83d32bc0-f364-3392-b356-940530dad32f | -14.571 | -45.674 | 2024-09-26 12:36:28 | GOES-16 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 147.6 |
| 055ee71c-31e7-36f5-b97d-0f5a9bf4e392 | -14.5515 | -45.6775 | 2024-09-26 12:36:28 | GOES-16 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 78.8 |
| bacdc81a-dee6-3119-8330-249587a5841d | -14.8828 | -51.4777 | 2024-09-26 12:36:30 | GOES-16 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 93.3 |
| 6b481524-8bf1-3bac-8b33-c3625f72765f | -15.6998 | -41.0835 | 2024-09-26 12:36:33 | GOES-16 | ENCRUZILHADA | BAHIA | Brasil | 2910404 | 29 | 33 | nan | nan | nan | Mata Atlântica | 100.0 |
| 2b6441de-e131-390f-ba18-3b4e65d49d61 | -15.7197 | -41.0789 | 2024-09-26 12:36:33 | GOES-16 | ENCRUZILHADA | BAHIA | Brasil | 2910404 | 29 | 33 | nan | nan | nan | Mata Atlântica | 83.6 |
| 70f41931-6209-3736-a213-be86de6b5f45 | -16.3138 | -45.6693 | 2024-09-26 12:36:37 | GOES-16 | SÃO ROMÃO | MINAS GERAIS | Brasil | 3164209 | 31 | 33 | nan | nan | nan | Cerrado | 90.4 |
| 49901651-d50a-309a-9842-5e736896922c | -17.9929 | -44.4514 | 2024-09-26 12:36:46 | GOES-16 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 86.8 |
| 75c52e2d-e8e0-3e5d-9c76-71648376cb57 | -18.9102 | -49.1674 | 2024-09-26 12:36:51 | GOES-16 | MONTE ALEGRE DE MINAS | MINAS GERAIS | Brasil | 3142809 | 31 | 33 | nan | nan | nan | Mata Atlântica | 148.9 |
| 31580bbd-9b65-3979-97c7-daa7aa7d44fb | -21.2733 | -51.0061 | 2024-09-26 12:37:04 | GOES-16 | VALPARAÍSO | SÃO PAULO | Brasil | 3556305 | 35 | 33 | nan | nan | nan | Mata Atlântica | 350.1 |
| 05bb8b41-a413-36dc-8df2-ca343caf22bf | -21.9381 | -48.5453 | 2024-09-26 12:37:07 | GOES-16 | BOA ESPERANÇA DO SUL | SÃO PAULO | Brasil | 3506706 | 35 | 33 | nan | nan | nan | Cerrado | 124.9 |
| 453f6755-044a-38f2-8b01-5a624dae6c80 | -21.9374 | -48.5688 | 2024-09-26 12:37:07 | GOES-16 | BOA ESPERANÇA DO SUL | SÃO PAULO | Brasil | 3506706 | 35 | 33 | nan | nan | nan | Cerrado | 134.4 |
| 76179b10-0a4d-3844-8f15-3e6beb127fc6 | -22.2243 | -48.6625 | 2024-09-26 12:37:09 | GOES-16 | ITAPUÍ | SÃO PAULO | Brasil | 3522901 | 35 | 33 | nan | nan | nan | Mata Atlântica | 306.8 |
| 5b723228-5319-3ba7-9f7e-5fafd64c7147 | -5.8808 | -48.0908 | 2024-09-26 12:45:40 | GOES-16 | ARAGUATINS | TOCANTINS | Brasil | 1702208 | 17 | 33 | nan | nan | nan | Cerrado | 69.3 |
| f153987b-3932-3da7-8bc3-23198a4cfd38 | -6.8024 | -59.3044 | 2024-09-26 12:45:45 | GOES-16 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 79.5 |
| 6cd54d9e-ca69-3fa5-b357-5718a0cc79eb | -7.2906 | -61.0869 | 2024-09-26 12:45:48 | GOES-16 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 75.9 |
| fdce10ff-f0bf-384f-ab71-d2786e94a031 | -8.3155 | -54.9956 | 2024-09-26 12:45:54 | GOES-16 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 69.2 |
| f2947113-0268-3325-8347-e5257dc32516 | -8.6722 | -38.149 | 2024-09-26 12:45:55 | GOES-16 | FLORESTA | PERNAMBUCO | Brasil | 2605707 | 26 | 33 | nan | nan | nan | Caatinga | 121.1 |
| bb57fae0-55a4-30f5-a494-7b1e2ec8b030 | -9.4165 | -51.4846 | 2024-09-26 12:46:00 | GOES-16 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 96.0 |
| f2d51318-3388-357f-81b9-0e75207bd752 | -9.4168 | -51.4636 | 2024-09-26 12:46:00 | GOES-16 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 321.6 |


[Clique aqui para ver as próximas entradas](README178.md)
