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
| 5dd6aa76-410e-3f0e-86a1-60eece542e24 | -6.9605 | -42.8816 | 2025-06-07 01:10:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 40.3 |
| c3682002-6d1f-3592-a3a7-c2dce12c2d46 | -6.96 | -42.9288 | 2025-06-07 01:10:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 57.0 |
| 615d8a10-742a-31f9-9e74-13f64e5b1a83 | -7.0169 | -44.5954 | 2025-06-07 01:10:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 62.2 |
| f6be130d-d7bf-3b78-a71f-40c2425a473b | -5.6567 | -43.7161 | 2025-06-07 01:10:00 | GOES-19 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 64.2 |
| 8b69a18b-d204-39cc-a350-22f322b81ec9 | -17.2639 | -42.6527 | 2025-06-07 01:10:00 | GOES-19 | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 96.6 |
| 5da6eae5-da1b-309e-9aa9-c9b4482418f3 | -12.5236 | -58.3576 | 2025-06-07 01:10:00 | GOES-19 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 78.8 |
| e2c0eeb2-d22e-30d7-84c4-43bb4fae3125 | -11.2548 | -60.7957 | 2025-06-07 01:10:00 | GOES-19 | ESPIGÃO D'OESTE | RONDÔNIA | Brasil | 1100098 | 11 | 33 | nan | nan | nan | Amazônia | 60.2 |
| ac96bb05-3a9b-320d-9d0d-84d40e1bba19 | -13.4733 | -56.8557 | 2025-06-07 01:10:00 | GOES-19 | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Cerrado | 73.1 |
| fafbe371-057a-3deb-9772-3ceccc5035c8 | -7.7364 | -44.1592 | 2025-06-07 01:10:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 147.2 |
| d4b2f4fa-d5b9-358d-80a6-896705999f65 | -7.7176 | -44.1611 | 2025-06-07 01:10:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 126.4 |
| f2cc620f-e450-340b-b8ed-0e10d2bb0374 | -7.7361 | -44.1823 | 2025-06-07 01:10:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 101.9 |
| ed27129d-e200-3070-8796-a62212a99033 | -7.7361 | -44.1823 | 2025-06-07 01:20:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 106.1 |
| dd0246d1-98b1-363e-9456-83d16a3d769a | -7.7173 | -44.1842 | 2025-06-07 01:20:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 84.1 |
| 854b8974-4b88-3824-82d2-aa53aae60059 | -12.5425 | -58.3561 | 2025-06-07 01:20:00 | GOES-19 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 48.8 |
| 4b1c7fa5-5d55-3c12-896d-2685fed9f575 | -7.7364 | -44.1592 | 2025-06-07 01:20:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 167.1 |
| 9e3ac08d-f5dc-3310-bc65-fdb892c1bc90 | -7.7176 | -44.1611 | 2025-06-07 01:20:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 137.6 |
| 07b66224-fd3c-3fa6-be77-9a2c8c8556fb | -5.6379 | -43.7175 | 2025-06-07 01:20:00 | GOES-19 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 107.2 |
| 98d82fb5-c662-3f65-b135-b0faa5540ab8 | -11.2548 | -60.7957 | 2025-06-07 01:20:00 | GOES-19 | ESPIGÃO D'OESTE | RONDÔNIA | Brasil | 1100098 | 11 | 33 | nan | nan | nan | Amazônia | 55.2 |
| 0beda701-addd-335d-953c-e72cb0944fdf | -5.6567 | -43.7161 | 2025-06-07 01:20:00 | GOES-19 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 60.2 |
| 0af9de73-33a9-31d8-b95a-e2d430b2f165 | -7.0169 | -44.5954 | 2025-06-07 01:20:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 57.3 |
| a37b0e2c-d2d7-3725-949c-2a7bc07c98e7 | -11.7826 | -47.402 | 2025-06-07 01:20:00 | GOES-19 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 59.5 |
| 60f674c4-0cd6-345b-a412-b0875bf8b5dd | -12.5236 | -58.3576 | 2025-06-07 01:20:00 | GOES-19 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 80.6 |
| 5c582bf3-3341-39ab-8892-88856b3a32e5 | -6.9602 | -42.9052 | 2025-06-07 01:20:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 55.5 |
| 5b0564b5-7857-3beb-b5a2-703067f84a0e | -17.2639 | -42.6527 | 2025-06-07 01:20:00 | GOES-19 | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 97.4 |
| 3e43a7b7-175e-39cf-8b7d-72149b2d0b8c | -13.4733 | -56.8557 | 2025-06-07 01:20:00 | GOES-19 | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Cerrado | 61.1 |
| f497e4f2-7c40-3ce9-b0e5-09019e86160e | -7.0169 | -44.5954 | 2025-06-07 01:30:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 58.3 |
| 7e0ecb3f-8230-3220-9233-29d73202e7aa | -7.7173 | -44.1842 | 2025-06-07 01:30:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 93.9 |
| acd89428-4827-3a3c-9d6a-d8fddd10a1da | -7.7361 | -44.1823 | 2025-06-07 01:30:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 132.0 |
| f4042a09-f8a3-3282-8e88-6cc1c8dfa7f8 | -6.9602 | -42.9052 | 2025-06-07 01:30:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 53.2 |
| d3250238-2435-3821-a245-3660f90e377a | -5.6379 | -43.7175 | 2025-06-07 01:30:00 | GOES-19 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 101.2 |
| 521e13bc-7538-3c09-9b03-09b337f1781a | -11.2548 | -60.7957 | 2025-06-07 01:30:00 | GOES-19 | ESPIGÃO D'OESTE | RONDÔNIA | Brasil | 1100098 | 11 | 33 | nan | nan | nan | Amazônia | 55.8 |
| c6e958ff-78aa-36be-8f75-beffd2e6441f | -13.4733 | -56.8557 | 2025-06-07 01:30:00 | GOES-19 | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Cerrado | 66.5 |
| 803a8ff1-7bc7-3794-b0d2-e4e4f7bcdd72 | -7.7364 | -44.1592 | 2025-06-07 01:30:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 169.6 |
| 22a8227a-9634-320f-912f-2ba91a1414de | -11.7826 | -47.402 | 2025-06-07 01:30:00 | GOES-19 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 55.3 |
| 8d1f6de6-27ea-3e29-be40-7cbf7be4b306 | -12.5238 | -58.3378 | 2025-06-07 01:30:00 | GOES-19 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 49.0 |
| d44bd72a-f9b8-37c4-8e87-1bddc9953c07 | -12.5236 | -58.3576 | 2025-06-07 01:30:00 | GOES-19 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 68.6 |
| c2a82c2d-84f1-3185-a8bf-74cfde56d06f | -17.2639 | -42.6527 | 2025-06-07 01:30:00 | GOES-19 | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 87.6 |
| 75ad4daf-ccb0-3a4b-8f44-4bed2f37c60d | -7.7176 | -44.1611 | 2025-06-07 01:30:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 129.7 |
| 2f657863-3b1d-3c18-b432-25b6a3ebba83 | -5.6567 | -43.7161 | 2025-06-07 01:30:00 | GOES-19 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 69.4 |
| 60b68307-94cb-3ce0-b469-ef1833e10933 | -12.5262 | -58.339901 | 2025-06-07 01:36:00 | METOP-B | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 7677de81-947f-32ef-be94-6a7c78796264 | -12.5312 | -58.359001 | 2025-06-07 01:36:00 | METOP-B | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| c435114c-6a67-333e-904a-bb8c23e6419b | -11.2603 | -60.801701 | 2025-06-07 01:36:00 | METOP-B | ESPIGÃO D'OESTE | RONDÔNIA | Brasil | 1100098 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| d6fb8df2-52a4-3dda-b10f-2e1eb092f21b | -11.2569 | -60.787998 | 2025-06-07 01:36:00 | METOP-B | ESPIGÃO D'OESTE | RONDÔNIA | Brasil | 1100098 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| a8aa50d0-9bc2-3fa6-8dd0-62e293dac4ae | -11.3652 | -56.548199 | 2025-06-07 01:36:00 | METOP-B | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 4d7056ee-87a6-3c9c-95e4-31eddae65a46 | -11.2472 | -60.790501 | 2025-06-07 01:36:00 | METOP-B | ESPIGÃO D'OESTE | RONDÔNIA | Brasil | 1100098 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| ad25d3b5-31a5-3f79-b3bb-638cb91b8732 | -13.4599 | -56.866001 | 2025-06-07 01:36:00 | METOP-B | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 829711f8-586c-34e5-b3ac-9b74b7fc717c | -12.5165 | -58.342499 | 2025-06-07 01:36:00 | METOP-B | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| b95cc1a5-e73c-3d2a-874b-8036c41019d8 | -12.5215 | -58.361599 | 2025-06-07 01:36:00 | METOP-B | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| f4ac3542-ced0-3832-94dd-ec953df670da | -11.2535 | -60.7743 | 2025-06-07 01:36:00 | METOP-B | ESPIGÃO D'OESTE | RONDÔNIA | Brasil | 1100098 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| cee15219-d038-3e8c-b6e1-fdd7ac579504 | -13.4633 | -56.840099 | 2025-06-07 01:36:00 | METOP-B | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 56de615b-a103-30bf-aa52-8ef0730a8c31 | -13.4695 | -56.8633 | 2025-06-07 01:36:00 | METOP-B | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| efbef98f-ee5e-3296-b4fb-fb68546e29ae | -7.0169 | -44.5954 | 2025-06-07 01:40:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 44.1 |
| 67f456b3-5f19-38d6-8c56-baf6c66af18c | -6.9602 | -42.9052 | 2025-06-07 01:40:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 95.5 |
| 76be8bb0-8404-3823-9f51-8eb89629d824 | -5.6567 | -43.7161 | 2025-06-07 01:40:00 | GOES-19 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 62.0 |
| 092069e1-babd-3336-b868-aef5fa357c39 | -11.2548 | -60.7957 | 2025-06-07 01:40:00 | GOES-19 | ESPIGÃO D'OESTE | RONDÔNIA | Brasil | 1100098 | 11 | 33 | nan | nan | nan | Amazônia | 50.2 |
| 52ad96bc-5253-332b-8b74-6bdfd65f5082 | -11.7826 | -47.402 | 2025-06-07 01:40:00 | GOES-19 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 53.8 |
| a5ffefb5-b8ef-3a8f-8b69-6aa565e3120a | -7.7364 | -44.1592 | 2025-06-07 01:40:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 172.5 |
| 2c8da1cc-d8c2-3b54-838d-2b8327d471cd | -13.4733 | -56.8557 | 2025-06-07 01:40:00 | GOES-19 | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Cerrado | 58.7 |
| 5793a826-a633-3313-98ef-dcabc4c27852 | -7.7173 | -44.1842 | 2025-06-07 01:40:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 85.3 |
| b4c668c2-fd3c-39a8-807a-9e9d18db85fd | -17.2639 | -42.6527 | 2025-06-07 01:40:00 | GOES-19 | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 75.0 |
| 5d82e203-ed4c-3665-b108-7fba14a0fb8a | -7.7176 | -44.1611 | 2025-06-07 01:40:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 131.3 |
| 6ce076ba-1869-332f-af3a-c0486df8448a | -5.6379 | -43.7175 | 2025-06-07 01:40:00 | GOES-19 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 101.1 |
| e59bc1df-e025-3380-b06f-aedee69d6154 | -7.7361 | -44.1823 | 2025-06-07 01:40:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 122.1 |
| 3505d994-9a1e-3d0b-979b-27093de44e1f | -12.5425 | -58.3561 | 2025-06-07 01:40:00 | GOES-19 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 45.0 |
| a0ea4873-3dd5-3d97-94ef-930fdebd9cd2 | -12.5236 | -58.3576 | 2025-06-07 01:40:00 | GOES-19 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 71.3 |
| 5ea46d5d-0d5e-324d-afce-6b24f865400a | -7.7361 | -44.1823 | 2025-06-07 01:50:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 122.6 |
| fa3efa19-48f9-3b51-b6d0-8c852f33b3df | -11.2548 | -60.7957 | 2025-06-07 01:50:00 | GOES-19 | ESPIGÃO D'OESTE | RONDÔNIA | Brasil | 1100098 | 11 | 33 | nan | nan | nan | Amazônia | 57.3 |
| 8041ddcc-7618-3915-af6e-9f6e392ea6b2 | -7.0169 | -44.5954 | 2025-06-07 01:50:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 52.0 |
| f19f52eb-fbf8-3502-a15a-14d22b24305b | -9.496 | -40.3337 | 2025-06-07 01:50:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 59.2 |
| 62ce9656-681e-3879-97f2-e1b706c5ce46 | -11.7826 | -47.402 | 2025-06-07 01:50:00 | GOES-19 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 59.5 |
| 32e950c9-1be8-39df-9c8f-d3a309eecbd7 | -6.9605 | -42.8816 | 2025-06-07 01:50:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 56.3 |
| 87497b49-6678-354e-97ca-19b54cbb828e | -12.5238 | -58.3378 | 2025-06-07 01:50:00 | GOES-19 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 51.9 |
| 7e966f78-e526-3144-a3a3-373ce6ffd81e | -17.2639 | -42.6527 | 2025-06-07 01:50:00 | GOES-19 | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 55.8 |
| 27af6cfb-ce2d-3a2c-b324-78da45f2eda6 | -13.4733 | -56.8557 | 2025-06-07 01:50:00 | GOES-19 | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Cerrado | 46.9 |
| 9620fc55-0197-382e-82b3-fea9d05522aa | -7.7176 | -44.1611 | 2025-06-07 01:50:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 140.9 |
| 00be5de3-02c2-32b2-848f-27dbe9962016 | -7.7173 | -44.1842 | 2025-06-07 01:50:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 90.0 |
| a77cb491-b4f1-3341-b87a-858cac35e394 | -6.9602 | -42.9052 | 2025-06-07 01:50:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 165.7 |
| 2c69accc-90fd-3e4b-811c-e736a44c8b20 | -12.5236 | -58.3576 | 2025-06-07 01:50:00 | GOES-19 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 74.0 |
| ecfc3a88-f196-3993-99f5-f00f38edb109 | -5.6379 | -43.7175 | 2025-06-07 01:50:00 | GOES-19 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 101.7 |
| 01730540-e067-375f-a563-0673d54613f8 | -5.6567 | -43.7161 | 2025-06-07 01:50:00 | GOES-19 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 56.1 |
| 46e3ea81-53f7-32db-a4e0-8925403b1fd9 | -9.4964 | -40.3088 | 2025-06-07 01:50:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 100.6 |
| dceb52ed-f3bc-3b71-9cc0-05b66c365ed6 | -9.5156 | -40.3061 | 2025-06-07 01:50:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 58.5 |
| 16969fc7-33cf-3d1e-898c-4bd24e5e0934 | -6.9414 | -42.907 | 2025-06-07 01:50:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 54.3 |
| 9dd3e28a-c51f-365a-8270-ff4bcc270905 | -7.7364 | -44.1592 | 2025-06-07 01:50:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 164.4 |
| e563a946-63d6-3961-85ef-789556c21873 | -12.53023 | -58.3574 | 2025-06-07 01:56:00 | TERRA_M-M | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 123.9 |
| 70183cab-25ea-35d2-8ea1-c35c770ad75d | -13.45867 | -56.84761 | 2025-06-07 01:56:00 | TERRA_M-M | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Cerrado | 44.5 |
| d7132ebe-5432-3dbc-8764-06339b37acac | -11.25297 | -60.79427 | 2025-06-07 01:56:00 | TERRA_M-M | ESPIGÃO D'OESTE | RONDÔNIA | Brasil | 1100098 | 11 | 33 | nan | nan | nan | Amazônia | 71.3 |
| 2b3b961d-ff30-337e-9188-ae77a08f96eb | -11.37134 | -56.55168 | 2025-06-07 01:56:00 | TERRA_M-M | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 48.3 |
| 410692a2-6099-3f75-a2e3-9592563b5b9e | -11.26555 | -60.79205 | 2025-06-07 01:56:00 | TERRA_M-M | ESPIGÃO D'OESTE | RONDÔNIA | Brasil | 1100098 | 11 | 33 | nan | nan | nan | Amazônia | 29.2 |
| 2143af7f-db36-3e04-9adc-9946abdb781c | -13.46469 | -56.83967 | 2025-06-07 01:56:00 | TERRA_M-M | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Cerrado | 50.6 |
| bf1d3e68-f4e3-3993-8b39-28a7d1436a27 | -12.52905 | -58.35202 | 2025-06-07 01:56:00 | TERRA_M-M | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 144.5 |
| bcfd147c-0bec-332e-9a8b-c0f9c4e351bd | -13.47145 | -56.87595 | 2025-06-07 01:56:00 | TERRA_M-M | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Cerrado | 64.4 |
| 1d433798-1fa3-3707-ac85-b48aaee8cd6a | -6.2038 | -43.3475 | 2025-06-07 02:00:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 45.3 |
| d9b22f82-2783-3318-bb1f-d3673c621d98 | -12.5236 | -58.3576 | 2025-06-07 02:00:00 | GOES-19 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 63.3 |
| 1f6beaa4-20d2-39bb-8c0f-a675f420968d | -7.7364 | -44.1592 | 2025-06-07 02:00:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 158.4 |
| a7a952f7-04db-364a-8454-815edd8433a7 | -17.2639 | -42.6527 | 2025-06-07 02:00:00 | GOES-19 | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 48.7 |
| 2f5a3b3a-896a-3f6a-8d74-16a496e8cfa6 | -11.7826 | -47.402 | 2025-06-07 02:00:00 | GOES-19 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 51.9 |
| 714d6860-ed2d-3f5d-b199-3b48e66c70dd | -6.9602 | -42.9052 | 2025-06-07 02:00:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 160.1 |
| 2a1dc675-b1e4-39d4-8d45-d3ea2ae2e691 | -13.4733 | -56.8557 | 2025-06-07 02:00:00 | GOES-19 | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Cerrado | 58.8 |
| 43ea2061-23f1-3f01-a91e-cd9fcfc1469a | -5.6567 | -43.7161 | 2025-06-07 02:00:00 | GOES-19 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 59.9 |


[Clique aqui para ver as próximas entradas](README6.md)
