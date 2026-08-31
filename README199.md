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

## Dados Diários - Página 199

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| f86f1b30-0924-32fc-b724-27ef8c80bdc8 | -10.4634 | -46.5638 | 2026-08-31 19:40:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 71.9 |
| 9c420316-25f7-3e9f-a66a-77e66c28f726 | -8.8521 | -66.7641 | 2026-08-31 19:40:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 90.4 |
| 98b51a97-8efd-3425-8c5b-881edbf904d1 | -10.8631 | -45.333 | 2026-08-31 19:40:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 461.8 |
| f41f2d31-ae7e-345f-9f79-8d474a33ec0e | -14.6721 | -53.6038 | 2026-08-31 19:40:00 | GOES-19 | SANTO ANTÔNIO DO LESTE | MATO GROSSO | Brasil | 5107792 | 51 | 33 | nan | nan | nan | Cerrado | 71.0 |
| 1094959e-89e8-3f6b-b86f-168e8fa295c9 | -8.5179 | -67.1436 | 2026-08-31 19:40:00 | GOES-19 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 119.2 |
| 8ad8f91e-510d-37cf-a0d9-af8359134d87 | -3.1266 | -61.2 | 2026-08-31 19:40:00 | GOES-19 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 53.1 |
| 9e54a724-32de-3ac6-83b3-8094791a783d | -16.5581 | -52.5004 | 2026-08-31 19:40:00 | GOES-19 | DOVERLÂNDIA | GOIÁS | Brasil | 5207253 | 52 | 33 | nan | nan | nan | Cerrado | 57.4 |
| f5740615-68ed-38fa-b4e1-131e03ade5a6 | -14.6145 | -53.59 | 2026-08-31 19:40:00 | GOES-19 | SANTO ANTÔNIO DO LESTE | MATO GROSSO | Brasil | 5107792 | 51 | 33 | nan | nan | nan | Cerrado | 190.4 |
| 7df0af80-b909-342d-b347-8a419935d053 | -10.3199 | -49.9996 | 2026-08-31 19:40:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 58.2 |
| a9c3e374-86cd-35f0-b372-3996992a7644 | -7.3487 | -60.5883 | 2026-08-31 19:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 346.2 |
| 100afe7e-cab9-3c8e-a981-c9c962b3ff2b | -17.9064 | -52.0737 | 2026-08-31 19:40:00 | GOES-19 | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | 81.3 |
| 464a7438-9ff0-3e14-9ee2-22cdc27c91b8 | -7.9239 | -44.2327 | 2026-08-31 19:40:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 163.0 |
| 8e9607da-e419-3251-ab61-c5fe85161058 | -11.1995 | -55.1008 | 2026-08-31 19:40:00 | GOES-19 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 83.9 |
| e30e8221-86e1-34c2-8875-3128174b4ae8 | -3.1267 | -61.1811 | 2026-08-31 19:40:00 | GOES-19 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 116.4 |
| bc04cec2-c361-3b41-8971-0ae5a5f09d53 | -8.8705 | -66.7822 | 2026-08-31 19:40:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 237.8 |
| 276b1ba1-2b82-38b7-861f-65c8e9196be2 | -7.5526 | -60.4651 | 2026-08-31 19:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 53.3 |
| 1e440439-4e71-3ea5-9b8d-e0874944e9ec | -6.9367 | -55.636 | 2026-08-31 19:40:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 207.2 |
| e4722dfa-66f1-3ff0-b216-133a5e041b20 | -15.8844 | -56.4819 | 2026-08-31 19:40:00 | GOES-19 | NOSSA SENHORA DO LIVRAMENTO | MATO GROSSO | Brasil | 5106109 | 51 | 33 | nan | nan | nan | Cerrado | 79.9 |
| 4745e47a-67db-3f11-8ce5-daf846356c61 | -3.1083 | -61.2191 | 2026-08-31 19:40:00 | GOES-19 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 61.9 |
| 5f562bd2-387b-3ce5-a488-99a00c38fe75 | -9.4908 | -57.0144 | 2026-08-31 19:40:00 | GOES-19 | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 78.3 |
| e4e1d5b2-797a-3393-a7a6-09d450e1776a | -4.9604 | -55.8424 | 2026-08-31 19:40:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 96.7 |
| 9f5d8bb6-13b4-3ff1-b258-7c0dfc4ed403 | -7.6804 | -55.3555 | 2026-08-31 19:40:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 65.9 |
| 0ac06e61-69ac-3488-8fc5-adddfbb14778 | -9.4721 | -57.0156 | 2026-08-31 19:40:00 | GOES-19 | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 121.4 |
| 77c40093-11af-3f04-a7ad-dd213564ec1e | -3.1839 | -60.1559 | 2026-08-31 19:40:00 | GOES-19 | IRANDUBA | AMAZONAS | Brasil | 1301852 | 13 | 33 | nan | nan | nan | Amazônia | 62.9 |
| cc13747c-d1b2-3db4-a2aa-f3b99cdee84e | -8.6852 | -62.9496 | 2026-08-31 19:40:00 | GOES-19 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 60.9 |
| 3bed154c-15f7-347c-b068-b8136c99d887 | -7.0293 | -55.6312 | 2026-08-31 19:40:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 94.3 |
| f2ae1bd3-5184-3a9b-b9a0-573525bfd095 | -6.3618 | -55.8632 | 2026-08-31 19:40:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 62.7 |
| be5bdcbc-8ffa-38e3-b13f-e27b1a30e930 | -6.8568 | -59.4757 | 2026-08-31 19:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 61.8 |
| f1affb8d-de5e-3c18-9281-11a30a56da52 | -5.5831 | -60.2307 | 2026-08-31 19:40:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 68.4 |
| 59ac3ed8-3197-3478-877d-841c54f8d8d0 | -11.5279 | -45.5162 | 2026-08-31 19:40:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 120.2 |
| 96753f47-7aef-39ba-98bd-9f5c7a698bae | -6.3875 | -54.7646 | 2026-08-31 19:40:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 144.2 |
| fa32df8a-e779-3e58-abbf-013216d9de2c | -3.4185 | -61.3461 | 2026-08-31 19:40:00 | GOES-19 | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 91.6 |
| 9b30adaf-20b4-3f85-95bf-66611103ac16 | -6.7885 | -55.6436 | 2026-08-31 19:40:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 49.1 |
| d4a8716f-4a32-3ffd-a995-099ab71c0a89 | -9.1532 | -59.5221 | 2026-08-31 19:40:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 86.5 |
| f0b80a30-b612-3459-a900-b1155a13612e | -8.9428 | -63.2797 | 2026-08-31 19:40:00 | GOES-19 | ITAPUÃ DO OESTE | RONDÔNIA | Brasil | 1101104 | 11 | 33 | nan | nan | nan | Amazônia | 61.6 |
| ba105e66-dcb0-314b-b628-de615add1a26 | -9.4164 | -56.9796 | 2026-08-31 19:40:00 | GOES-19 | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 66.0 |
| c23e6873-b9b2-3d35-bbf8-d2f33cf199f2 | -7.3302 | -60.589 | 2026-08-31 19:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 99.8 |
| a2688db8-5fc4-3f27-a046-e7b208df68b2 | -6.8778 | -59.031 | 2026-08-31 19:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 45.2 |
| c2a3f37f-c25d-3301-b473-ee130ae0da16 | -7.6264 | -57.615 | 2026-08-31 19:40:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 48.2 |
| 34ece206-f0b4-3699-9f4f-84fe7129618a | -11.9378 | -45.0656 | 2026-08-31 19:40:00 | GOES-19 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 70.3 |
| 37ecbab6-b70c-3720-8f2a-6ddb38cd00df | -9.4351 | -56.9784 | 2026-08-31 19:40:00 | GOES-19 | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 106.6 |
| b65c3ddd-bb16-35ed-811e-03c9725b9038 | -9.4153 | -45.6726 | 2026-08-31 19:40:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 72.0 |
| 770181b1-8118-3b34-bc46-ef0359d52242 | -10.1134 | -45.8621 | 2026-08-31 19:40:00 | GOES-19 | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 95.3 |
| b6ac2045-0988-3fbc-895b-843cc93093da | -3.6398 | -60.5656 | 2026-08-31 19:40:00 | GOES-19 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 83.0 |
| d0a06137-d95e-3894-b511-57729a83724c | -10.4961 | -59.6195 | 2026-08-31 19:40:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 56.4 |
| 410faf34-c3a6-34e3-885f-580316de7dbd | -9.445 | -66.7289 | 2026-08-31 19:40:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 50.3 |
| ca6040be-fdc6-3fed-ad29-33b70fffd02a | -11.0933 | -51.5345 | 2026-08-31 19:40:00 | GOES-19 | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Cerrado | 255.4 |
| 3113836c-1ce5-3fba-883f-51cf0b225bbe | -3.6216 | -60.547 | 2026-08-31 19:40:00 | GOES-19 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 136.2 |
| 6dd002eb-98ea-3e3c-b151-0943e81fa8a2 | -6.4054 | -49.9441 | 2026-08-31 19:40:00 | GOES-19 | CANAÃ DOS CARAJÁS | PARÁ | Brasil | 1502152 | 15 | 33 | nan | nan | nan | Amazônia | 132.7 |
| 31126716-adef-3920-8245-31779acded11 | -8.4988 | -55.3252 | 2026-08-31 19:40:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 51.8 |
| 606e2edb-1b79-3ede-b4c3-deb5c60d8ae2 | -16.0348 | -54.4143 | 2026-08-31 19:40:00 | GOES-19 | POXORÉU | MATO GROSSO | Brasil | 5107008 | 51 | 33 | nan | nan | nan | Cerrado | 119.5 |
| 6c7cd3ba-a8e4-3211-a023-edd89013dbec | -3.0637 | -43.1229 | 2026-08-31 19:40:00 | GOES-19 | BARREIRINHAS | MARANHÃO | Brasil | 2101707 | 21 | 33 | nan | nan | nan | Cerrado | 91.1 |
| b8836a60-0acb-35ba-a798-5064b9e2147e | -6.4055 | -49.9228 | 2026-08-31 19:40:00 | GOES-19 | CANAÃ DOS CARAJÁS | PARÁ | Brasil | 1502152 | 15 | 33 | nan | nan | nan | Amazônia | 65.3 |
| d2cd84d0-f105-352f-aa92-f8cf97b5b9c0 | -5.8866 | -52.2507 | 2026-08-31 19:40:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 47.3 |
| 6dd38578-bb99-3892-946e-339a4b3c16e8 | -15.7349 | -56.1093 | 2026-08-31 19:40:00 | GOES-19 | VÁRZEA GRANDE | MATO GROSSO | Brasil | 5108402 | 51 | 33 | nan | nan | nan | Pantanal | 86.1 |
| d3a5691e-324a-331b-823d-b84335c95ec0 | -9.1709 | -59.6374 | 2026-08-31 19:40:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 82.4 |
| a9b0197d-18a0-32c6-bed2-1af16696c450 | -8.2605 | -62.758 | 2026-08-31 19:40:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 78.5 |
| 9f13d730-9423-32f6-a651-8126b130e33e | -8.6012 | -70.2192 | 2026-08-31 19:40:00 | GOES-19 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 90.6 |
| 2a2fd402-43bd-3a20-908b-f0f37c84d782 | -9.9266 | -67.0126 | 2026-08-31 19:40:00 | GOES-19 | ACRELÂNDIA | ACRE | Brasil | 1200013 | 12 | 33 | nan | nan | nan | Amazônia | 60.9 |
| e5eae286-91b8-3dec-b557-9b52b563fd75 | -7.0242 | -59.2374 | 2026-08-31 19:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 55.2 |
| fe3410f3-7756-3169-ba59-0e725980e2c4 | -11.2103 | -45.1017 | 2026-08-31 19:40:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 111.8 |
| 39b92ffe-7b5a-3944-9614-330c1eb5a2a3 | -7.905 | -44.2346 | 2026-08-31 19:40:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 222.9 |
| 8df2a294-693b-3bbd-95c5-a19c5bc798f9 | -3.4002 | -61.3276 | 2026-08-31 19:40:00 | GOES-19 | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 61.9 |
| 990b0088-6ae2-30a8-b8a5-f4ff5db09cc1 | -7.2996 | -56.6878 | 2026-08-31 19:40:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 47.6 |
| 8d159bd8-2e23-3259-a03b-da60afcc61fa | -7.6805 | -55.3355 | 2026-08-31 19:40:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 93.3 |
| 7968f4b3-892f-3c01-be3c-f3325151a977 | -2.8512 | -61.9767 | 2026-08-31 19:40:00 | GOES-19 | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 70.4 |
| bad1e5b2-b481-324a-95e5-158daf83e86a | -10.5719 | -57.495 | 2026-08-31 19:40:00 | GOES-19 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 90.5 |
| c2b5b9a0-5671-3a58-928c-97f7a42f60d1 | -8.5363 | -67.1617 | 2026-08-31 19:40:00 | GOES-19 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 72.6 |
| df3d4702-40da-3f3c-9591-f4043605dd13 | -9.6049 | -68.5979 | 2026-08-31 19:40:00 | GOES-19 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 55.3 |
| 1a06fe8d-9775-3023-9f69-fd7e950326f8 | -9.208 | -65.8044 | 2026-08-31 19:40:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 53.8 |
| 8be8e8ac-8a47-3099-a57a-5654cdaeab0a | -2.8568 | -43.5029 | 2026-08-31 19:40:00 | GOES-19 | HUMBERTO DE CAMPOS | MARANHÃO | Brasil | 2105005 | 21 | 33 | nan | nan | nan | Cerrado | 82.8 |
| a946231c-e3c0-30a9-8875-11f1cd602eb0 | -8.8886 | -66.893 | 2026-08-31 19:40:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 345.7 |
| d1a7c89b-911b-302d-a4f6-29358d9654c7 | -17.9059 | -52.0955 | 2026-08-31 19:40:00 | GOES-19 | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | 104.7 |
| 045803b9-cdd7-39fb-bb27-1e38d1277665 | -8.5971 | -54.7553 | 2026-08-31 19:40:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 72.0 |
| b7e34853-1bf2-3039-9ecc-f863f337d5cf | -8.5783 | -54.7768 | 2026-08-31 19:40:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 89.1 |
| 5e65b4fa-e826-30ac-93bc-fc271934400d | -11.6975 | -54.5467 | 2026-08-31 19:40:00 | GOES-19 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 91.4 |
| 4aae4bba-55a5-37aa-8364-a9498217cc83 | -8.8885 | -66.9116 | 2026-08-31 19:40:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 107.3 |
| 8d160dfe-af4e-3d80-9c93-2ba07026887e | -9.4719 | -57.0354 | 2026-08-31 19:40:00 | GOES-19 | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 86.3 |
| 56165a00-e0eb-37fe-bf89-7c578ca34473 | -7.77 | -61.2015 | 2026-08-31 19:40:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 53.4 |
| ec76ed1e-5544-37ba-b7b8-f0f2dcb4dbff | -9.4906 | -57.0342 | 2026-08-31 19:40:00 | GOES-19 | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 67.6 |
| a910c286-d853-388e-b0dc-d2588ea052d7 | -7.1822 | -60.6713 | 2026-08-31 19:40:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 67.8 |
| 4fdeaba0-37eb-3c68-9297-38085d67e663 | -6.8193 | -59.5734 | 2026-08-31 19:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 88.4 |
| fbdcefa3-520b-3b39-91fc-6bc3a1cb501c | -3.1449 | -61.1808 | 2026-08-31 19:40:00 | GOES-19 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 72.1 |
| 48fcd2e4-285d-390c-be10-c0a0dbd1c127 | -6.6765 | -58.7492 | 2026-08-31 19:40:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 129.8 |
| d13a3bfa-d2a8-345a-80e2-a7fc9e771ad7 | -7.6066 | -55.2998 | 2026-08-31 19:40:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 72.7 |
| c2e4a578-6c46-3102-be38-16cf765025d9 | -6.1294 | -57.6833 | 2026-08-31 19:40:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 66.0 |
| 3b2c3f43-8a40-3ddf-851e-06ada4b6dac7 | -10.7409 | -54.0196 | 2026-08-31 19:40:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 119.9 |
| 040e2e91-d478-329f-ad7a-556cdcd442b4 | -11.4968 | -45.1071 | 2026-08-31 19:40:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 82.9 |
| 4b8ba4d9-55fa-3cd8-8729-da482eb50cc2 | -6.2537 | -55.4308 | 2026-08-31 19:40:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 59.3 |
| 3eebf797-4f08-3e27-8646-a2c4501fe297 | -7.3119 | -60.5706 | 2026-08-31 19:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 78.2 |
| 26a1a13d-3984-3d25-8528-a28bbf97303f | -9.908 | -67.0131 | 2026-08-31 19:40:00 | GOES-19 | ACRELÂNDIA | ACRE | Brasil | 1200013 | 12 | 33 | nan | nan | nan | Amazônia | 63.5 |
| e4662f98-9316-3634-bcb6-6c823080d7ce | -4.1516 | -60.6878 | 2026-08-31 19:40:00 | GOES-19 | CAREIRO | AMAZONAS | Brasil | 1301100 | 13 | 33 | nan | nan | nan | Amazônia | 64.0 |
| 40d24f02-50bc-334e-95e5-1e60ac5a1915 | -11.6786 | -54.5484 | 2026-08-31 19:40:00 | GOES-19 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 62.3 |
| 08cf5f36-aed0-363f-bbdd-909229dcdbe6 | -7.0517 | -52.7187 | 2026-08-31 19:40:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 171.4 |
| 2bd1ee43-3ac5-3523-8a97-0bfbea429503 | -8.87 | -66.8935 | 2026-08-31 19:40:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 381.4 |
| 2a80964f-a7af-31ad-a4a2-f0dd188011d7 | -12.9032 | -45.8382 | 2026-08-31 19:40:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 69.1 |
| 1f86a084-694c-3a26-a96e-f01ac1c73a47 | -11.0744 | -51.5365 | 2026-08-31 19:40:00 | GOES-19 | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Cerrado | 119.7 |
| f8f36a80-1271-3307-9af9-a4e54bab053d | -11.6972 | -54.5672 | 2026-08-31 19:40:00 | GOES-19 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 55.8 |
| 93ae6afa-d04f-3dd8-b65e-92098192d7b3 | -10.3394 | -49.9547 | 2026-08-31 19:40:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 62.6 |
| b297ab7d-8a67-3e80-b362-f40b34e89e93 | -3.1083 | -61.238 | 2026-08-31 19:40:00 | GOES-19 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 55.0 |


[Clique aqui para ver as próximas entradas](README200.md)
