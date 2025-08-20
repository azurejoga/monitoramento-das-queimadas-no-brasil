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

## Dados Diários - Página 62

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 17d0aac7-ae6d-3d4c-94c9-52a943a22e6b | -5.9713 | -44.1312 | 2025-08-20 12:20:00 | GOES-19 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 78.1 |
| a27136bb-cd18-3097-84ad-e44da230513f | -6.9605 | -42.8816 | 2025-08-20 12:20:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 92.3 |
| 8398fa8b-0db8-361d-8e04-a679d73440e4 | -10.7043 | -48.2226 | 2025-08-20 12:20:00 | GOES-19 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 113.1 |
| c0a39fde-f5a7-39b6-8a3b-7802d2105a9e | -6.9607 | -42.858 | 2025-08-20 12:20:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 87.2 |
| 1cf8443e-551c-3702-9b35-4b55755896dc | -12.6698 | -44.9525 | 2025-08-20 12:20:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 149.3 |
| e66b6e69-d111-3120-9880-2a0ddabf0ea9 | -13.8748 | -45.5411 | 2025-08-20 12:20:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 98.6 |
| 47d29b22-ca73-3f53-bb89-a469283ecaee | -12.9925 | -45.202 | 2025-08-20 12:20:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 376.2 |
| 1717d648-ec5f-3be3-ae14-bdd5f3a00dac | -8.7945 | -45.4693 | 2025-08-20 12:20:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 95.1 |
| 177ccd3c-0c67-3fa1-9703-ca8af7a9e79b | -13.3349 | -54.4027 | 2025-08-20 12:20:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 70.8 |
| bf4859dd-9a4b-3936-9556-a02c701f033f | -5.9711 | -44.1542 | 2025-08-20 12:20:00 | GOES-19 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 155.9 |
| 89b34b45-aed2-3f65-914e-b84402cdd7a1 | -5.9711 | -44.1542 | 2025-08-20 12:30:00 | GOES-19 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 187.9 |
| 2e4495bc-7d88-3ca0-8295-66a25da1bd92 | -12.9732 | -45.2051 | 2025-08-20 12:30:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 101.5 |
| 444c3c58-facc-3b3a-b05d-5a8d435113bc | -12.9925 | -45.202 | 2025-08-20 12:30:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 531.0 |
| 2b69870e-c119-36c2-b632-cf68013fa0ec | -12.9921 | -45.2252 | 2025-08-20 12:30:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 164.2 |
| 5eca4926-a5b8-35aa-a1f8-917866791684 | -12.6698 | -44.9525 | 2025-08-20 12:30:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 174.2 |
| 21ff0569-3206-3402-bd93-6e98b1027a47 | -5.9713 | -44.1312 | 2025-08-20 12:30:00 | GOES-19 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 107.0 |
| ba5de56e-1904-3723-928c-bd908c6712eb | -13.1555 | -54.9357 | 2025-08-20 12:30:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 70.6 |
| 1ebcec73-4048-338f-9960-dbb7b6d05a61 | -12.993 | -45.1787 | 2025-08-20 12:30:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 99.1 |
| 65a7cf59-fec0-34e4-a6af-03de0808f6dd | -6.9605 | -42.8816 | 2025-08-20 12:30:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 94.7 |
| d6b755a6-b6ce-3279-960b-74f9aacba1fc | -13.3346 | -54.4233 | 2025-08-20 12:30:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 108.1 |
| 2d969f49-ddcb-3b7c-8715-d0c302fc5d96 | -13.3349 | -54.4027 | 2025-08-20 12:30:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 96.1 |
| 4ec14b22-d65e-3eda-b0a0-ccbf71fd126a | -6.9607 | -42.858 | 2025-08-20 12:30:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 100.9 |
| c84c3780-f125-36a1-b20e-a99c1590ce06 | -10.7043 | -48.2226 | 2025-08-20 12:30:00 | GOES-19 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 108.4 |
| 86fa86fa-df22-3547-8c0d-ee9ffc1cdb8d | -13.8748 | -45.5411 | 2025-08-20 12:30:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 89.2 |
| 41b927b2-fef9-32bb-9be0-de051604ecb6 | -8.7945 | -45.4693 | 2025-08-20 12:30:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 111.9 |
| b5213072-67a0-357e-95d1-82d406529030 | -12.9546 | -46.1732 | 2025-08-20 12:30:00 | GOES-19 | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 131.3 |
| 3bb802f4-e2cf-3370-a496-a102fd58b901 | -13.8743 | -45.5643 | 2025-08-20 12:40:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 81.4 |
| 08fd45ca-2f27-39e8-ac92-3d860c30700f | -12.9921 | -45.2252 | 2025-08-20 12:40:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 151.6 |
| 3b16625d-2b37-3145-a044-fcff28036023 | -12.993 | -45.1787 | 2025-08-20 12:40:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 143.7 |
| 7ab0cda2-456d-37b1-b177-f6bef239801c | -6.9607 | -42.858 | 2025-08-20 12:40:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 94.6 |
| 5fb035b5-7855-31d9-9cc1-09c1d104c28e | -6.9605 | -42.8816 | 2025-08-20 12:40:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 95.7 |
| ce94de8a-a90a-3294-b151-855feb8077b6 | -13.354 | -54.4006 | 2025-08-20 12:40:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 71.9 |
| 9a8ea0e0-2fe6-320a-83d6-7116ef7cdde2 | -13.3349 | -54.4027 | 2025-08-20 12:40:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 160.4 |
| 280561fc-9882-36d7-a312-527e56f6716b | -12.6698 | -44.9525 | 2025-08-20 12:40:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 191.2 |
| 8c781ffd-8ce3-34a5-af62-220ebf2d082e | -7.6672 | -45.2428 | 2025-08-20 12:40:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 113.3 |
| ff34b526-8fe9-3609-961d-cff27360d99f | -6.8497 | -44.4267 | 2025-08-20 12:40:00 | GOES-19 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 78.9 |
| 9ee5a77c-ba6d-34dd-b51b-a44f21c85cf1 | -13.8748 | -45.5411 | 2025-08-20 12:40:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 97.2 |
| bdf215b0-6d98-3f96-81f3-fb14d3a60756 | -12.9732 | -45.2051 | 2025-08-20 12:40:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 199.4 |
| fc77f19d-15ae-3585-864c-2610f2726325 | -5.9713 | -44.1312 | 2025-08-20 12:40:00 | GOES-19 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 99.3 |
| bf0a3ec9-b751-356a-9983-32ce1eae43bf | -13.3346 | -54.4233 | 2025-08-20 12:40:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 133.2 |
| 5fe661ff-07b4-30b4-981c-5e12f1501b96 | -13.0119 | -45.1988 | 2025-08-20 12:40:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 81.3 |
| 3465e703-99a5-3b62-86eb-ff4dbbf68a79 | -13.1558 | -54.9151 | 2025-08-20 12:40:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 72.9 |
| 216a252f-5e1d-39f4-91dc-750be28d7a1c | -13.1555 | -54.9357 | 2025-08-20 12:40:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 69.0 |
| 79bfd696-f262-3296-8090-6be9bb71a9db | -12.9736 | -45.1819 | 2025-08-20 12:40:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 86.9 |
| f748aa5b-0ca6-3bef-81ed-6134f9f587b4 | -12.9925 | -45.202 | 2025-08-20 12:40:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 476.3 |
| ca16ec4d-684b-3fb5-9f1a-41c9434b2fcf | -5.9711 | -44.1542 | 2025-08-20 12:40:00 | GOES-19 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 191.5 |
| 17cc4243-18f6-3718-995b-00a02372dead | -6.8497 | -44.4267 | 2025-08-20 12:50:00 | GOES-19 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 99.8 |
| eba3eccc-e376-3361-8c0a-14c3129fffa1 | -12.993 | -45.1787 | 2025-08-20 12:50:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 208.9 |
| 13b09db0-b2eb-34cf-90e0-3804e266f72b | -5.9711 | -44.1542 | 2025-08-20 12:50:00 | GOES-19 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 201.3 |
| de841cc1-28f9-3885-b306-cfecd065a8f2 | -13.354 | -54.4006 | 2025-08-20 12:50:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 76.7 |
| a3974a40-f9f5-3efc-abb1-fef0df574186 | -13.3346 | -54.4233 | 2025-08-20 12:50:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 191.3 |
| 80113da5-a4c2-3376-8ad4-c819da220637 | -12.9925 | -45.202 | 2025-08-20 12:50:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 588.6 |
| e3db23b7-e184-3849-b803-10486321a280 | -8.297 | -47.64 | 2025-08-20 12:50:00 | GOES-19 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 115.8 |
| 3f5cd6cd-8492-3f78-950b-92106d0af29c | -12.9732 | -45.2051 | 2025-08-20 12:50:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 196.6 |
| 209943c6-dd96-3369-ac9b-eb14bbe484bf | -10.7043 | -48.2226 | 2025-08-20 12:50:00 | GOES-19 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 83.2 |
| 75747848-d472-3b62-a496-0c31daeeb2ae | -13.1558 | -54.9151 | 2025-08-20 12:50:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 76.9 |
| e94c6fc1-a0cb-3b2f-810e-ee6f4d9d88de | -13.3349 | -54.4027 | 2025-08-20 12:50:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 200.8 |
| 43261eaa-7595-39cc-8495-680ea51a21c3 | -12.6147 | -46.8821 | 2025-08-20 12:50:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 99.6 |
| e38fad1c-cd49-3c6d-bad6-c8da6ceda733 | -13.1555 | -54.9357 | 2025-08-20 12:50:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 86.8 |
| 6d3b85b2-40ff-30eb-8e67-578245235104 | -7.6672 | -45.2428 | 2025-08-20 12:50:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 89.4 |
| 3f01badc-be3d-300e-9842-0c6dd3c56036 | -7.2901 | -43.6929 | 2025-08-20 12:50:00 | GOES-19 | CANAVIEIRA | PIAUÍ | Brasil | 2202251 | 22 | 33 | nan | nan | nan | Cerrado | 94.6 |
| 3217d094-9062-3d99-b53c-7722ba52276d | -7.3089 | -43.6911 | 2025-08-20 12:50:00 | GOES-19 | CANAVIEIRA | PIAUÍ | Brasil | 2202251 | 22 | 33 | nan | nan | nan | Cerrado | 145.1 |
| 42974a6d-445e-3679-b867-dde258f30af7 | -8.7945 | -45.4693 | 2025-08-20 12:50:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 67.0 |
| 1505dee3-6f64-3b04-b89e-eaf241df5c18 | -5.9713 | -44.1312 | 2025-08-20 12:50:00 | GOES-19 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 116.5 |
| 78382ca9-902d-35c0-aaa0-d6612a85fe75 | -12.6698 | -44.9525 | 2025-08-20 12:50:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 163.1 |
| 74428ac3-f6f2-3e02-af29-73a28e4161b2 | -13.8748 | -45.5411 | 2025-08-20 12:50:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 98.9 |
| b7b4e0d2-8111-38b5-8f79-ef2906d7bb99 | -6.9607 | -42.858 | 2025-08-20 12:50:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 109.8 |
| 64b944be-cbf7-391a-aa3a-53ef2506d3f4 | -12.9736 | -45.1819 | 2025-08-20 12:50:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 117.0 |
| 20dba885-5a38-3f12-9ecd-3567aa504306 | -7.3086 | -43.7144 | 2025-08-20 12:50:00 | GOES-19 | CANAVIEIRA | PIAUÍ | Brasil | 2202251 | 22 | 33 | nan | nan | nan | Cerrado | 97.6 |
| 0a6bf5da-39c5-3e6b-9889-66bded3569f9 | -13.8743 | -45.5643 | 2025-08-20 12:50:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 89.4 |
| fbc1145d-1745-3ca5-a736-2e95691e09dd | -12.9921 | -45.2252 | 2025-08-20 12:50:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 116.6 |
| 9b1579ef-9e5a-3791-a3c0-7d5492c7f9f7 | -8.297 | -47.64 | 2025-08-20 13:00:00 | GOES-19 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 147.0 |
| b28c4036-61ba-38b3-95fa-43c6d77dd629 | -13.1558 | -54.9151 | 2025-08-20 13:00:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 92.8 |
| f6ad6138-5c42-3681-a1d7-9b22c798a4fe | -13.1555 | -54.9357 | 2025-08-20 13:00:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 96.4 |
| e13cafb8-0ca8-3ba7-9408-168dbb17062f | -13.3349 | -54.4027 | 2025-08-20 13:00:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 187.9 |
| 5c3a6aa8-1199-3597-a9b1-6a122d17396d | -5.9711 | -44.1542 | 2025-08-20 13:00:00 | GOES-19 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 222.0 |
| 25b3bf8f-e8d3-34c6-bc22-77a87ac5bb55 | -13.3537 | -54.4213 | 2025-08-20 13:00:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 85.6 |
| 7a272f43-3d6f-37a0-a9f2-b7c6da8f4af5 | -13.1364 | -54.9376 | 2025-08-20 13:00:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 80.8 |
| bf988ab1-20f0-3313-bad6-1979258f0a6b | -5.9713 | -44.1312 | 2025-08-20 13:00:00 | GOES-19 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 97.8 |
| fa3495b9-7515-32b4-9694-f3ca0bca8597 | -15.0002 | -54.8135 | 2025-08-20 13:00:00 | GOES-19 | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 71.2 |
| 0d47048e-2686-3bfd-86f6-c9260ffdc7a2 | -12.9925 | -45.202 | 2025-08-20 13:00:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 463.9 |
| 94a228ed-e4df-3466-b813-5ffa83871a76 | -13.8743 | -45.5643 | 2025-08-20 13:00:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 85.3 |
| 67107b9c-0692-307c-b26f-0c687d2f14c2 | -6.9607 | -42.858 | 2025-08-20 13:00:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 115.7 |
| c0aafa34-3bab-32d0-97bd-b8562b911183 | -12.9736 | -45.1819 | 2025-08-20 13:00:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 200.9 |
| 92c273a0-0708-3143-9f59-c6e05c6b18e8 | -12.9732 | -45.2051 | 2025-08-20 13:00:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 306.1 |
| 17cf9e9b-49f7-32fd-a89b-be002af04cd0 | -8.7942 | -45.492 | 2025-08-20 13:00:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 97.1 |
| 936f9e61-0798-3f0c-a8f8-dd312c61b662 | -13.354 | -54.4006 | 2025-08-20 13:00:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 78.8 |
| ead7b8bf-7fbf-3762-ad85-69c96773235a | -10.7043 | -48.2226 | 2025-08-20 13:00:00 | GOES-19 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 73.5 |
| e84b2748-daae-3fe6-aa27-a9ddd6613e3a | -12.993 | -45.1787 | 2025-08-20 13:00:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 213.5 |
| c911c3f3-ba04-3f8c-90ae-fd5723c1afc7 | -12.6698 | -44.9525 | 2025-08-20 13:00:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 148.4 |
| 04cb7282-36d3-3b4c-84a6-ca5bb6b163b1 | -12.9921 | -45.2252 | 2025-08-20 13:00:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 123.0 |
| c7478247-473b-3fbc-bdff-6347c719f97d | -13.3346 | -54.4233 | 2025-08-20 13:00:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 227.1 |
| f3a7311c-0d02-34fe-91e8-9604a1de0bf7 | -8.7945 | -45.4693 | 2025-08-20 13:00:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 199.6 |
| f5b6db6c-0fc4-34a5-bef4-6f2dd3684aa2 | -13.8748 | -45.5411 | 2025-08-20 13:00:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 87.6 |
| 38e81b63-a1bb-32a6-a42f-a3bcc136ae08 | -12.6147 | -46.8821 | 2025-08-20 13:00:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 115.3 |
| 1080f7fa-4e79-3017-a452-9d4c7d845ff4 | -13.8743 | -45.5643 | 2025-08-20 13:10:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 74.6 |
| 488402c5-5978-30f6-803c-344a6fcabfa3 | -12.993 | -45.1787 | 2025-08-20 13:10:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 188.3 |
| b0732ce7-325d-3b37-92eb-941b0dca02b0 | -14.9999 | -54.8343 | 2025-08-20 13:10:00 | GOES-19 | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 70.1 |
| 76cd6a73-6ca4-3bc5-9d6d-7317b260cb40 | -6.9607 | -42.858 | 2025-08-20 13:10:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 100.8 |
| 1ad92c1b-bd38-3be2-b77a-6dc3ab1c5d90 | -6.8497 | -44.4267 | 2025-08-20 13:10:00 | GOES-19 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 84.5 |


[Clique aqui para ver as próximas entradas](README63.md)
