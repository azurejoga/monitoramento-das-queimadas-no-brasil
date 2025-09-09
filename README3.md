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

## Dados Diários - Página 3

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 4b46d58e-3424-34d0-843a-1fd4a427c9e1 | -11.3018 | -46.4792 | 2025-09-09 00:50:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 107.4 |
| 1d2dc785-d002-32a3-bbce-836c3e290ccf | -9.2181 | -60.8305 | 2025-09-09 00:50:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 51.0 |
| 4b1ccb6e-0f27-3c52-b08e-03a779add0af | -5.589 | -45.0505 | 2025-09-09 00:50:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 257.7 |
| aba223de-416a-3e5f-b899-22881d57e724 | -10.0111 | -64.9151 | 2025-09-09 00:50:00 | GOES-19 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 68.6 |
| 92f021c7-e0e4-3ca1-b9cb-dd21ebe4fb22 | -11.3905 | -43.5365 | 2025-09-09 00:50:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 62.7 |
| 279bd6b8-f163-349a-83e8-9406ae3c8b68 | -5.6925 | -43.8986 | 2025-09-09 01:00:00 | GOES-19 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 76.2 |
| c7868248-43f2-398b-a516-60452dc0b65b | -11.3014 | -46.5018 | 2025-09-09 01:00:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 62.3 |
| 176a5064-831f-336a-9679-0544c80d8188 | -9.0802 | -65.3789 | 2025-09-09 01:00:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 48.3 |
| 72b12f3d-06a8-3e5c-8c40-17a662ea1300 | -10.0111 | -64.9151 | 2025-09-09 01:00:00 | GOES-19 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 82.8 |
| ce49f824-d4e8-3d3e-b228-b1e5dedcd05e | -5.5506 | -45.1664 | 2025-09-09 01:00:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 61.1 |
| 59ef76c0-095e-3512-a701-bf0e16f62a3d | -12.9482 | -54.7519 | 2025-09-09 01:00:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 59.1 |
| 1ca4521b-521d-3ff3-a769-a9a184267985 | -5.589 | -45.0505 | 2025-09-09 01:00:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 225.4 |
| 10f3918b-3ef2-3f77-8351-fab858005fe0 | -5.5892 | -45.0278 | 2025-09-09 01:00:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 86.6 |
| b85cea83-d2b8-3bb8-b235-7745d7f817cc | -12.1988 | -53.9024 | 2025-09-09 01:00:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 119.3 |
| 53f66d3d-9035-3022-bd70-b79d7b63426b | -11.3018 | -46.4792 | 2025-09-09 01:00:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 69.5 |
| 0cb033f4-17ab-3477-a87a-6ddeafb57274 | -15.5465 | -48.3727 | 2025-09-09 01:00:00 | GOES-19 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 64.9 |
| 00ecd48c-0430-3381-9887-582d95d6e4a2 | -5.5705 | -45.0291 | 2025-09-09 01:00:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 83.5 |
| b2f51f25-a3b8-3704-8a90-f30e58b69b8f | -16.6981 | -48.6197 | 2025-09-09 01:00:00 | GOES-19 | SILVÂNIA | GOIÁS | Brasil | 5220603 | 52 | 33 | nan | nan | nan | Cerrado | 57.8 |
| b31bb7d7-518b-3f9b-a185-160fbe225c7f | -16.6976 | -48.6423 | 2025-09-09 01:00:00 | GOES-19 | SILVÂNIA | GOIÁS | Brasil | 5220603 | 52 | 33 | nan | nan | nan | Cerrado | 59.2 |
| c864a4d3-1581-313d-967f-f592346b3046 | -10.011 | -64.9339 | 2025-09-09 01:00:00 | GOES-19 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 59.6 |
| 36e4ad5c-4bd9-352a-a985-3ad9e55fc48f | -12.0295 | -51.0935 | 2025-09-09 01:00:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 66.9 |
| d80af71e-d4cb-38f9-9dae-08a3de4d8c36 | -12.1991 | -53.8817 | 2025-09-09 01:00:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 90.4 |
| 624b3236-b0d2-361b-92fe-00ae58fbd89a | -12.948 | -54.7724 | 2025-09-09 01:00:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 55.1 |
| a53dd70f-1e55-3a7a-a2e5-02f1f0bf7e29 | -11.4277 | -43.6017 | 2025-09-09 01:00:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 70.9 |
| c66c8e68-66f6-3fbd-94d9-8c6b53cec4ff | -5.5703 | -45.0518 | 2025-09-09 01:00:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 215.0 |
| 643bff4b-742b-35ed-9b70-84d267ef44ef | -12.0291 | -51.1149 | 2025-09-09 01:10:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 67.1 |
| 15a86e3c-52e7-3d81-ba97-491eb1f3d199 | -12.1988 | -53.9024 | 2025-09-09 01:10:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 89.4 |
| 6b5bfee9-1feb-3b73-9427-d51eb3bacd3c | -11.4277 | -43.6017 | 2025-09-09 01:10:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 81.0 |
| 240ca5fe-f860-3d43-a308-631a2b219158 | -10.011 | -64.9339 | 2025-09-09 01:10:00 | GOES-19 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 77.5 |
| 86e54bb3-e0f2-3d33-b8f8-6c819be5209f | -5.5703 | -45.0518 | 2025-09-09 01:10:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 188.8 |
| 83d19dd3-f6c0-32a1-9008-1b97fe7e3750 | -9.0987 | -65.3783 | 2025-09-09 01:10:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 37.8 |
| f383eb49-f4c3-3c5f-9072-90f07fb50b67 | -19.9025 | -48.2047 | 2025-09-09 01:10:00 | GOES-19 | CONCEIÇÃO DAS ALAGOAS | MINAS GERAIS | Brasil | 3117306 | 31 | 33 | nan | nan | nan | Cerrado | 63.2 |
| a337ba1f-e820-3def-932a-128b7a02568c | -15.8275 | -48.9505 | 2025-09-09 01:10:00 | GOES-19 | PIRENÓPOLIS | GOIÁS | Brasil | 5217302 | 52 | 33 | nan | nan | nan | Cerrado | 73.0 |
| c86e63b5-e439-385c-bc2f-ce14e1ce86c7 | -12.0295 | -51.0935 | 2025-09-09 01:10:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 120.5 |
| 607761e5-6e12-3a04-9780-2484a23a35f3 | -10.0111 | -64.9151 | 2025-09-09 01:10:00 | GOES-19 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 82.9 |
| a236c994-d7bd-3305-97ab-590c55730009 | -5.5705 | -45.0291 | 2025-09-09 01:10:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 107.8 |
| fa839a73-74f0-30ae-8929-247e204aa63c | -15.5465 | -48.3727 | 2025-09-09 01:10:00 | GOES-19 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 123.4 |
| 01bac588-525d-3996-a400-048cbe9b0ccf | -9.0802 | -65.3789 | 2025-09-09 01:10:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 42.4 |
| 003b5a45-6c6e-346b-a651-9a95330dbe03 | -5.589 | -45.0505 | 2025-09-09 01:10:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 148.2 |
| 3e9210ec-51c6-32f8-9111-f9f26a16c850 | -5.5892 | -45.0278 | 2025-09-09 01:10:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 86.7 |
| a077aba3-f677-30ce-9265-8e23fa98bfc7 | -12.9482 | -54.7519 | 2025-09-09 01:10:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 64.0 |
| 848497e0-b3bf-374a-b868-9495ffdca1db | -12.1991 | -53.8817 | 2025-09-09 01:10:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 86.0 |
| 116cfdbc-a61c-3838-b148-383e861b0925 | -11.2007 | -54.9992 | 2025-09-09 01:10:00 | GOES-19 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 53.3 |
| 8ffa5cbc-17d8-3bba-ac2e-297eaeeb782e | -12.6343 | -56.9725 | 2025-09-09 01:10:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 56.4 |
| f5f4834a-0388-37a8-968b-7fe9175a90ce | -11.4456 | -43.6697 | 2025-09-09 01:20:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 59.1 |
| 455df466-b0e1-3186-8538-2a9fd68eaae6 | -12.0291 | -51.1149 | 2025-09-09 01:20:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 62.2 |
| 23da792d-1bb1-359f-85c3-a811c888ce86 | -5.589 | -45.0505 | 2025-09-09 01:20:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 176.8 |
| 16e89a75-e16f-3152-93a9-d49d8a565b90 | -11.4452 | -43.6934 | 2025-09-09 01:20:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 70.7 |
| 98a5f5cb-22c6-3990-b3fb-ff713f800bdc | -12.948 | -54.7724 | 2025-09-09 01:20:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 60.3 |
| 353f4916-e2c1-3b7a-b4ef-a0822defacba | -8.0606 | -48.6423 | 2025-09-09 01:20:00 | GOES-19 | BANDEIRANTES DO TOCANTINS | TOCANTINS | Brasil | 1703057 | 17 | 33 | nan | nan | nan | Amazônia | 61.5 |
| 45503d03-7f84-3412-bb20-ee849e190bc0 | -12.0485 | -51.0914 | 2025-09-09 01:20:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 56.9 |
| 93a9b63a-9dde-3838-bbdd-495ca0527cf2 | -12.9482 | -54.7519 | 2025-09-09 01:20:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 75.3 |
| 27a224b1-91ca-379b-ac03-4333bebfcbb1 | -12.1991 | -53.8817 | 2025-09-09 01:20:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 72.0 |
| 7ede3ef3-0184-32dd-8d14-5809c427a518 | -10.011 | -64.9339 | 2025-09-09 01:20:00 | GOES-19 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 49.6 |
| d0014917-2495-3662-822f-ab63a3f1f67e | -5.5705 | -45.0291 | 2025-09-09 01:20:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 111.5 |
| f50bdde0-ec1e-39c4-99ea-c1c039b0c909 | -15.8275 | -48.9505 | 2025-09-09 01:20:00 | GOES-19 | PIRENÓPOLIS | GOIÁS | Brasil | 5217302 | 52 | 33 | nan | nan | nan | Cerrado | 68.9 |
| 337eb99f-4a64-31a5-9e9b-0622147ddbdb | -9.0802 | -65.3789 | 2025-09-09 01:20:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 44.9 |
| 38bb4a71-e706-3940-bb96-7849c09cfc69 | -11.4277 | -43.6017 | 2025-09-09 01:20:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 77.8 |
| 6d8df059-28e2-3f77-8436-46178eb02589 | -12.0295 | -51.0935 | 2025-09-09 01:20:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 122.0 |
| 1d7bc1ed-f0a0-3525-bf70-cc8515c5ed41 | -5.6736 | -43.9231 | 2025-09-09 01:20:00 | GOES-19 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 54.8 |
| 1aec6132-d281-3772-bf22-3a2b610dfcaf | -5.6738 | -43.9 | 2025-09-09 01:20:00 | GOES-19 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 95.9 |
| 75d9872e-1116-3e9b-9422-f98c1bdb98f8 | -5.5703 | -45.0518 | 2025-09-09 01:20:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 215.1 |
| 3e0e6aa5-2aa3-380a-a7e9-83785aa05732 | -18.4808 | -49.5447 | 2025-09-09 01:20:00 | GOES-19 | CACHOEIRA DOURADA | GOIÁS | Brasil | 5204250 | 52 | 33 | nan | nan | nan | Cerrado | 77.4 |
| 704cea9e-39c9-34c1-a66e-252712970cab | -17.2757 | -46.7538 | 2025-09-09 01:20:00 | GOES-19 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 66.7 |
| ac5171a4-e54a-367b-bb19-94fbd274aa25 | -11.426 | -43.6963 | 2025-09-09 01:20:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 53.2 |
| fea4fd9a-ef9c-357b-b8ba-85639f85e916 | -11.2196 | -54.9975 | 2025-09-09 01:20:00 | GOES-19 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 55.5 |
| a9bd253a-3483-3608-b112-f7c35fd1fb10 | -10.0111 | -64.9151 | 2025-09-09 01:20:00 | GOES-19 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 74.8 |
| 780c37ec-17ab-3bbb-98b9-aeccc55e0d2f | -5.6925 | -43.8986 | 2025-09-09 01:20:00 | GOES-19 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 86.6 |
| b346cecc-0d6d-3346-948e-bd11298c9009 | -18.4607 | -49.5485 | 2025-09-09 01:20:00 | GOES-19 | CACHOEIRA DOURADA | GOIÁS | Brasil | 5204250 | 52 | 33 | nan | nan | nan | Cerrado | 77.4 |
| bcb0e717-f6af-315c-82eb-10cc7ce45d2e | -12.1988 | -53.9024 | 2025-09-09 01:20:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 94.6 |
| 1a78ec92-9a03-33c9-a6dd-cd8afd52c005 | -5.5892 | -45.0278 | 2025-09-09 01:20:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 100.4 |
| 10c860ca-5dc5-3286-bf93-b41053ac04d0 | -17.68101 | -52.2613 | 2025-09-09 01:26:00 | TERRA_M-M | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 72.8 |
| cf4da726-ca03-3f27-8280-1d8c5c531d49 | -17.68139 | -52.25465 | 2025-09-09 01:26:00 | TERRA_M-M | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 64.1 |
| 0ca6339a-9ee1-31eb-8245-e3d64734ee5d | -21.11148 | -49.02242 | 2025-09-09 01:26:00 | TERRA_M-M | CATANDUVA | SÃO PAULO | Brasil | 3511102 | 35 | 33 | nan | nan | nan | Mata Atlântica | 41.4 |
| 6bf36d27-db3d-3211-b17e-94dc8da3668a | -18.4765 | -49.56205 | 2025-09-09 01:26:00 | TERRA_M-M | CACHOEIRA DOURADA | GOIÁS | Brasil | 5204250 | 52 | 33 | nan | nan | nan | Cerrado | 95.1 |
| 8b3374ec-488d-3bb4-bbe0-0285c33b93a9 | -18.83277 | -49.67524 | 2025-09-09 01:26:00 | TERRA_M-M | ITUIUTABA | MINAS GERAIS | Brasil | 3134202 | 31 | 33 | nan | nan | nan | Mata Atlântica | 71.1 |
| 490169f0-21ba-3f8f-a972-0bbba6fcd5e0 | -18.83088 | -49.68256 | 2025-09-09 01:26:00 | TERRA_M-M | ITUIUTABA | MINAS GERAIS | Brasil | 3134202 | 31 | 33 | nan | nan | nan | Cerrado | 99.4 |
| a4979f85-f510-329b-98b0-229cbb0e229d | -18.47612 | -49.56947 | 2025-09-09 01:26:00 | TERRA_M-M | CACHOEIRA DOURADA | GOIÁS | Brasil | 5204250 | 52 | 33 | nan | nan | nan | Cerrado | 84.0 |
| 34c342e0-3ed1-3082-8e70-448560d20c9b | -22.92807 | -49.1561 | 2025-09-09 01:26:00 | TERRA_M-M | IARAS | SÃO PAULO | Brasil | 3519253 | 35 | 33 | nan | nan | nan | Cerrado | 67.2 |
| d08456ad-f0ea-3d5f-9143-be1e1420a3d6 | -12.95683 | -54.76151 | 2025-09-09 01:28:00 | TERRA_M-M | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 95.0 |
| 66c1b132-18a6-30c3-986f-30b75c63e47c | -15.99808 | -55.95565 | 2025-09-09 01:28:00 | TERRA_M-M | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 13.5 |
| 6f1a2b42-202f-3d22-af27-70d37ba8f829 | -16.3314 | -52.93417 | 2025-09-09 01:28:00 | TERRA_M-M | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 38.4 |
| 628a1732-f98d-38b0-9b5c-76895a73b6d4 | -11.20741 | -55.00554 | 2025-09-09 01:28:00 | TERRA_M-M | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 66.0 |
| 7e348524-68b3-3e58-9b30-f4da2efc6f39 | -12.88134 | -62.08952 | 2025-09-09 01:28:00 | TERRA_M-M | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 9.0 |
| a256d5f3-a01f-33b2-9d8a-1567389ff83c | -12.42529 | -63.89709 | 2025-09-09 01:28:00 | TERRA_M-M | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 11.3 |
| 0099305f-0ec3-37fd-b7e8-921c301a6f7e | -12.63401 | -56.982 | 2025-09-09 01:28:00 | TERRA_M-M | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 21.4 |
| c375ae38-e59a-3907-a269-51e4592f2f61 | -12.95641 | -54.77732 | 2025-09-09 01:28:00 | TERRA_M-M | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 37.1 |
| ce644506-61b8-3411-84aa-f130c3efc0c6 | -12.42399 | -63.8871 | 2025-09-09 01:28:00 | TERRA_M-M | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 12.0 |
| 298d51b5-aa98-3962-bf51-ce2f94242fd1 | -12.84913 | -52.94213 | 2025-09-09 01:28:00 | TERRA_M-M | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 36.5 |
| 884edc11-031e-3c4f-885d-dc8845e68342 | -14.90598 | -55.82591 | 2025-09-09 01:28:00 | TERRA_M-M | CHAPADA DOS GUIMARÃES | MATO GROSSO | Brasil | 5103007 | 51 | 33 | nan | nan | nan | Cerrado | 11.0 |
| a96d0d52-6d25-3d45-971c-702279c56454 | -11.20366 | -54.98289 | 2025-09-09 01:28:00 | TERRA_M-M | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 15.8 |
| 0f775347-b62f-3488-960f-1fe0339010ae | -14.90869 | -55.84287 | 2025-09-09 01:28:00 | TERRA_M-M | CHAPADA DOS GUIMARÃES | MATO GROSSO | Brasil | 5103007 | 51 | 33 | nan | nan | nan | Cerrado | 39.3 |
| 99c3a5fe-c140-3831-8256-2e248a0f4e02 | -15.1769 | -56.013 | 2025-09-09 01:28:00 | TERRA_M-M | CUIABÁ | MATO GROSSO | Brasil | 5103403 | 51 | 33 | nan | nan | nan | Cerrado | 14.0 |
| e245f872-a13d-3764-b37b-a5b5c392c6ff | -12.94362 | -54.764 | 2025-09-09 01:28:00 | TERRA_M-M | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 36.3 |
| 0a456b30-3084-3281-a269-60f532be43d3 | -12.87251 | -62.09081 | 2025-09-09 01:28:00 | TERRA_M-M | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 3acbf18f-d254-35e9-b3ba-df1701007a67 | -15.25245 | -53.79672 | 2025-09-09 01:28:00 | TERRA_M-M | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | 20.9 |
| 9ab3759c-9521-3c72-b33c-89e3ce6779e9 | -14.7157 | -60.24842 | 2025-09-09 01:28:00 | TERRA_M-M | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 7.8 |
| 1e8103bf-e1b5-3931-80ba-8040d8c41e86 | -12.86616 | -62.11014 | 2025-09-09 01:28:00 | TERRA_M-M | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 233e1189-cc06-3927-aaf2-10bbbb0566fd | -12.93039 | -54.76635 | 2025-09-09 01:28:00 | TERRA_M-M | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 21.5 |
| ba3f6733-98f0-3e0d-a196-31b1c5a6e870 | -15.82391 | -52.27315 | 2025-09-09 01:28:00 | TERRA_M-M | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 41.0 |


[Clique aqui para ver as próximas entradas](README4.md)
