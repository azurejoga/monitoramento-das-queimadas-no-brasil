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

## Dados Diários - Página 188

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 0faf45da-7aa7-3e70-9fea-7a60d184bf25 | -5.9335 | -53.5159 | 2026-09-21 18:30:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 70.4 |
| ad80d6de-b889-3867-8762-cb11cb45628d | -11.3422 | -51.3394 | 2026-09-21 18:30:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 49.3 |
| 16b2d19b-fef4-304b-8230-8c3db37709b8 | -9.0286 | -44.9187 | 2026-09-21 18:30:00 | GOES-19 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 129.2 |
| 56f1774d-1c7c-3b58-a255-d8a642ccf12f | -6.571 | -44.1516 | 2026-09-21 18:30:00 | GOES-19 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 292.6 |
| eb68fffa-9d08-3061-a5a6-657198989821 | -5.977 | -55.3639 | 2026-09-21 18:30:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 59.1 |
| 83c1a02c-16ab-3e18-8915-e7a6f1a2da6f | -6.5708 | -44.1747 | 2026-09-21 18:30:00 | GOES-19 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 88.1 |
| 6b84c5b6-61e1-32bc-994c-ae843d14f362 | -7.252 | -55.5794 | 2026-09-21 18:30:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 102.5 |
| 9c53cc17-ea4c-356e-98c0-8472e21ba679 | -11.0221 | -54.1584 | 2026-09-21 18:30:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 141.1 |
| a1abfcc0-8ca9-3106-8056-3cf479ef8efb | -6.9297 | -59.6267 | 2026-09-21 18:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 97.4 |
| 9d8b0909-2993-3303-b9af-867ae261b25c | -3.8651 | -58.7056 | 2026-09-21 18:30:00 | GOES-19 | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | 46.8 |
| bdb40438-1e53-348c-90d8-52ee44762632 | -9.0529 | -60.5312 | 2026-09-21 18:30:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 99.1 |
| 3278610b-93ff-38b6-9860-33c188c6ef95 | -11.6605 | -43.4476 | 2026-09-21 18:30:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 126.2 |
| 94b672ec-3bc5-3636-b6b5-6045686519c2 | -12.0451 | -50.064 | 2026-09-21 18:30:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 126.4 |
| 97bd7db4-1a75-3c4b-ab68-3af3f6c44ea6 | -12.3212 | -50.6965 | 2026-09-21 18:30:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 86.1 |
| 8786e401-3c88-38c4-b063-3b7b765674cd | -10.0709 | -50.2814 | 2026-09-21 18:30:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 72.8 |
| 0895cc5a-dd35-3af8-b1d3-dd3fe77e0bba | -8.882 | -68.8166 | 2026-09-21 18:30:00 | GOES-19 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 64.3 |
| dbb40059-def5-3d33-8ba6-cdac2142f55c | -5.8116 | -52.3781 | 2026-09-21 18:30:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 49.1 |
| 71a20887-e141-30d1-8b8f-4ca2fe7aabc5 | -9.6111 | -43.9243 | 2026-09-21 18:30:00 | GOES-19 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 191.7 |
| e41e3103-acc1-3fc2-837c-72bb76ee4ce7 | -6.2313 | -56.0476 | 2026-09-21 18:30:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 54.9 |
| fc294f87-21ca-3f1a-a5a7-124790745a0b | -5.7304 | -53.465 | 2026-09-21 18:30:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 47.7 |
| 83e2cb47-3d15-3c56-a1ef-2a7909086078 | -10.8282 | -50.1601 | 2026-09-21 18:30:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 144.2 |
| 28d1b5a0-23b1-344e-8927-8e70093026dd | -10.1964 | -53.9232 | 2026-09-21 18:30:00 | GOES-19 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 55.1 |
| 5a0ea680-7f70-354d-a826-1bcd1480cd52 | -3.7707 | -59.5909 | 2026-09-21 18:30:00 | GOES-19 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 49.0 |
| cf228943-3424-3a1f-a0bc-74a9be2f2d4c | -11.4213 | -47.338 | 2026-09-21 18:30:00 | GOES-19 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 172.9 |
| e4180a3e-328e-3482-8af6-42df0f96829c | -11.4349 | -45.3689 | 2026-09-21 18:30:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 109.7 |
| 3117d27a-c0ca-3bd3-a5c7-5b8ba08f7a83 | -4.3754 | -55.0288 | 2026-09-21 18:30:00 | GOES-19 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 39.6 |
| 8188875b-2f73-36f6-95ac-cdf51111348d | -9.3704 | -60.3418 | 2026-09-21 18:30:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 100.2 |
| 8be52724-2117-3906-bcd5-740e916e1e46 | -5.9846 | -44.7261 | 2026-09-21 18:30:00 | GOES-19 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 232.7 |
| 109b3145-b5b8-3820-bf77-f9a9bf0c0ff7 | -5.9151 | -59.9522 | 2026-09-21 18:30:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 67.3 |
| 53b1a5f7-3892-3eab-a151-197e74c5f47e | -6.7119 | -58.9992 | 2026-09-21 18:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 309.4 |
| 88946723-499c-30aa-b5ed-843c58e20848 | -6.8796 | -41.6995 | 2026-09-21 18:30:00 | GOES-19 | IPIRANGA DO PIAUÍ | PIAUÍ | Brasil | 2204808 | 22 | 33 | nan | nan | nan | Caatinga | 84.2 |
| a21d69a9-9faf-3c7a-bf18-a223891ea0a3 | -3.5356 | -58.6939 | 2026-09-21 18:30:00 | GOES-19 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 49.1 |
| 1caebe65-7228-37a2-9429-0e0a549cbdd6 | -9.0287 | -69.2191 | 2026-09-21 18:30:00 | GOES-19 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 62.6 |
| f8e604ab-2864-393c-8921-a5941224a955 | -2.9709 | -57.7197 | 2026-09-21 18:30:00 | GOES-19 | BOA VISTA DO RAMOS | AMAZONAS | Brasil | 1300680 | 13 | 33 | nan | nan | nan | Amazônia | 88.7 |
| 88791cd7-e048-3fc2-a5e2-89cd29077d9a | -12.3105 | -50.161 | 2026-09-21 18:30:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 62.7 |
| cf401334-7b83-3c3a-93a7-85c59d706e67 | -9.3706 | -60.3225 | 2026-09-21 18:30:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 118.4 |
| 3a0687f0-01b9-3aeb-ad1c-b77153d9c04f | -6.6549 | -45.1282 | 2026-09-21 18:30:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 123.4 |
| c1191fb7-4461-3fb2-b4e6-73fd5d976d81 | -11.3734 | -46.7624 | 2026-09-21 18:30:00 | GOES-19 | RIO DA CONCEIÇÃO | TOCANTINS | Brasil | 1718659 | 17 | 33 | nan | nan | nan | Cerrado | 148.6 |
| 64dfc84b-da93-3d88-9a1d-e40d498cfc3a | -2.9999 | -54.1688 | 2026-09-21 18:30:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 69.4 |
| c789c96b-c5df-380a-a274-b7ac0064451a | -6.9223 | -42.9323 | 2026-09-21 18:30:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 101.8 |
| 8d1db884-fd89-3999-a372-af9edcdb299e | -8.7537 | -44.2821 | 2026-09-21 18:30:00 | GOES-19 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 80.0 |
| 67e86032-4905-32d3-91f9-7e9758296690 | -8.7726 | -44.28 | 2026-09-21 18:30:00 | GOES-19 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 273.6 |
| 6c0fe50b-bb83-394d-9cf3-3063fb033142 | -10.2152 | -53.9216 | 2026-09-21 18:30:00 | GOES-19 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 117.1 |
| bf8b602a-ec16-34c3-827c-27a91520cb8f | 0.7937 | -59.2099 | 2026-09-21 18:30:00 | GOES-19 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 174.8 |
| 8662fef5-f712-3c6c-b58b-c9bed5d0fb62 | -2.8791 | -57.799 | 2026-09-21 18:30:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 147.4 |
| b50e87cd-6bab-3a9e-9a8c-38b3a7e3c3e6 | -8.7706 | -45.8567 | 2026-09-21 18:30:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 72.4 |
| 55ca0d7f-280e-33cd-9a10-915cab466d50 | -2.8791 | -57.8184 | 2026-09-21 18:30:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 101.1 |
| 40b3cc2e-c2c3-3db9-b3b0-fb0780c4ceaf | -5.3645 | -56.0447 | 2026-09-21 18:30:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 55.0 |
| c987f8d9-2715-34bf-a27c-1ea605f98d6c | -3.6449 | -58.8647 | 2026-09-21 18:30:00 | GOES-19 | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | 66.6 |
| fe13922f-4b52-3551-9495-bafad1ae1a79 | -11.8495 | -46.833 | 2026-09-21 18:30:00 | GOES-19 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 118.3 |
| a899d178-d8bb-3347-aefe-c8b5a9e8e935 | -8.81 | -48.7484 | 2026-09-21 18:30:00 | GOES-19 | COLMÉIA | TOCANTINS | Brasil | 1716703 | 17 | 33 | nan | nan | nan | Amazônia | 69.9 |
| 86f5859d-837e-37e4-acbd-0b49acfde590 | -7.7346 | -49.3799 | 2026-09-21 18:30:00 | GOES-19 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 58.1 |
| ca735a89-00d1-3d79-b90f-0a17abff27c6 | -5.9335 | -59.9515 | 2026-09-21 18:30:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 81.0 |
| 42b93868-d63a-3cd6-b51d-623001a28376 | -10.1814 | -68.4175 | 2026-09-21 18:30:00 | GOES-19 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 107.8 |
| 0627331b-e160-3d5d-8201-2b130e5d45fe | -3.4579 | -60.246 | 2026-09-21 18:30:00 | GOES-19 | CAREIRO | AMAZONAS | Brasil | 1301100 | 13 | 33 | nan | nan | nan | Amazônia | 61.1 |
| cbc359fc-d273-39c7-9229-1210c9b75efa | -10.8475 | -50.1366 | 2026-09-21 18:30:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 253.3 |
| 88033a6f-db1b-31a3-901e-48c8923bb741 | -5.9934 | -55.7014 | 2026-09-21 18:30:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 40.6 |
| f0c66ef8-3709-3d6a-9108-7ec8841f3cfa | -0.7471 | -49.2161 | 2026-09-21 18:30:00 | GOES-19 | PONTA DE PEDRAS | PARÁ | Brasil | 1505700 | 15 | 33 | nan | nan | nan | Amazônia | 119.6 |
| d2dceed1-500d-3045-842f-1b7ea542c1c7 | -11.0412 | -54.1362 | 2026-09-21 18:30:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 185.2 |
| e47121b6-0829-3117-8069-b338460b8d45 | -8.8097 | -60.7926 | 2026-09-21 18:30:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 115.0 |
| 724aff0b-cf6d-3064-8e09-18565ad27e83 | -4.2964 | -56.2596 | 2026-09-21 18:30:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 51.2 |
| f39d6353-263c-39b0-86db-e9615c375da4 | -1.3742 | -49.3367 | 2026-09-21 18:30:00 | GOES-19 | MUANÁ | PARÁ | Brasil | 1504901 | 15 | 33 | nan | nan | nan | Amazônia | 57.3 |
| 8f3bbdfc-f19d-3a56-83ae-2eb4287bdd01 | -7.6942 | -61.5473 | 2026-09-21 18:30:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 114.7 |
| d957da19-dfbb-3010-b7e0-4620fd71a14c | -3.1698 | -58.5859 | 2026-09-21 18:30:00 | GOES-19 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 65.2 |
| 052afd94-558a-3f26-98d9-37faf9d12e17 | -3.5357 | -58.6553 | 2026-09-21 18:30:00 | GOES-19 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 52.1 |
| 3ed010f9-965d-3ebf-b1f5-bacae1923ccc | -12.0448 | -50.0856 | 2026-09-21 18:30:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 172.6 |
| 578b2115-e22b-368f-b0e0-cda1f60379ee | -11.6609 | -43.4239 | 2026-09-21 18:30:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 86.8 |
| 0f8631c1-990d-3b4e-b09b-9de55a0c971c | -7.8891 | -48.916 | 2026-09-21 18:30:00 | GOES-19 | BERNARDO SAYÃO | TOCANTINS | Brasil | 1703206 | 17 | 33 | nan | nan | nan | Amazônia | 78.5 |
| aee3c1ca-da75-34f8-a0ac-f3312d91cb6b | -9.1206 | -58.9218 | 2026-09-21 18:30:00 | GOES-19 | COTRIGUAÇU | MATO GROSSO | Brasil | 5103379 | 51 | 33 | nan | nan | nan | Amazônia | 92.7 |
| 6e4743e8-0edb-3f8a-b129-67e75c02e3a5 | -7.9519 | -72.9869 | 2026-09-21 18:30:00 | GOES-19 | CRUZEIRO DO SUL | ACRE | Brasil | 1200203 | 12 | 33 | nan | nan | nan | Amazônia | 55.2 |
| 5aec0a66-3766-3dbf-825b-a75a9c905bfb | -2.9157 | -57.7983 | 2026-09-21 18:30:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 77.9 |
| 2fee3df7-fe57-3d01-beb5-9420321bdcdf | -10.473 | -51.2808 | 2026-09-21 18:30:00 | GOES-19 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 58.2 |
| 275b3f6d-2bce-3c2b-abc9-8b3b424a7b1f | -3.7887 | -59.7052 | 2026-09-21 18:30:00 | GOES-19 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 42.4 |
| becaff3c-989c-3145-a467-12adef95f548 | -7.5477 | -61.3247 | 2026-09-21 18:30:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 116.8 |
| 0992b6b6-7c13-37c4-8a84-2f9cf3e904e9 | -10.0898 | -50.2795 | 2026-09-21 18:30:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 95.8 |
| a18f077a-7b80-3b82-ad72-20213b6394eb | -3.3358 | -58.1384 | 2026-09-21 18:30:00 | GOES-19 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 46.4 |
| 702d3921-62de-35f8-b9d5-6c56c12dc7e4 | -6.3842 | -55.265 | 2026-09-21 18:30:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 91.2 |
| 174441bd-12f7-317a-acfd-6014f089c9d4 | -6.4372 | -55.6411 | 2026-09-21 18:30:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 48.7 |
| 34da200a-a3ce-31e6-b453-28f88ea6d921 | -7.0826 | -42.0868 | 2026-09-21 18:30:00 | GOES-19 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 102.0 |
| 710fd7b9-7c93-336f-b41e-85ccf8e3a55b | -10.4728 | -51.302 | 2026-09-21 18:30:00 | GOES-19 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 88.0 |
| 41309ccb-6d46-366a-b4eb-ee2da8b55c02 | -3.4963 | -59.5775 | 2026-09-21 18:30:00 | GOES-19 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 92.6 |
| e7c6e782-dd4c-3249-80f8-06ec7cf57d6c | -9.1744 | -56.916 | 2026-09-21 18:30:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 154.5 |
| 3186d73a-4994-356c-894f-19e193027bb1 | -6.3011 | -60.0154 | 2026-09-21 18:30:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 60.5 |
| abd41691-80d3-3be5-84d2-a087ffdc5bf2 | -5.5846 | -45.5703 | 2026-09-21 18:30:00 | GOES-19 | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 82.6 |
| edfff517-b69a-3319-a0b7-99517eb8e560 | -10.7061 | -50.7915 | 2026-09-21 18:30:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 87.0 |
| 06f75781-73fd-385d-a7c7-b5d31da05b78 | -7.9708 | -72.4761 | 2026-09-21 18:30:00 | GOES-19 | CRUZEIRO DO SUL | ACRE | Brasil | 1200203 | 12 | 33 | nan | nan | nan | Amazônia | 58.8 |
| 0a659395-be09-3e5f-bfaf-c4a6985085c7 | -4.1668 | -40.1448 | 2026-09-21 18:30:00 | GOES-19 | SANTA QUITÉRIA | CEARÁ | Brasil | 2312205 | 23 | 33 | nan | nan | nan | Caatinga | 87.8 |
| 05747dfa-bf42-3d6a-b97d-fa1b2a302940 | -2.9157 | -57.8177 | 2026-09-21 18:30:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 73.0 |
| cee6e216-a76b-35fd-872c-dc32dc8a412d | -7.566 | -61.343 | 2026-09-21 18:30:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 100.3 |
| 2f7efa8e-c9cd-3e81-a1bb-135b89ed725c | -3.0182 | -54.1684 | 2026-09-21 18:30:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 39.2 |
| 51967e6c-13b5-3835-b8af-7f61e680f328 | -11.6793 | -43.4684 | 2026-09-21 18:30:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 141.5 |
| 04808906-aa09-3560-9598-1a657ed9d5b3 | -2.8608 | -57.7994 | 2026-09-21 18:30:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 181.9 |
| da8416a4-7434-3fb8-b0cb-d45c3a153940 | -5.7975 | -57.7353 | 2026-09-21 18:30:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 52.4 |
| aa623e48-7f5a-3a79-b1a2-80a31ec3388e | -5.9818 | -57.7087 | 2026-09-21 18:30:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 47.6 |
| 629dd976-a576-34c1-b3e9-a2fb7edf1439 | -2.8608 | -57.8188 | 2026-09-21 18:30:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 129.6 |
| 49c69a0d-eb46-3e14-a152-ec4db0333c1b | -6.0739 | -57.7245 | 2026-09-21 18:30:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 48.4 |
| 0765b2ad-fe0e-372d-8a99-5c4f68adcc0a | -8.791 | -60.8127 | 2026-09-21 18:30:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 148.5 |
| 1789979b-1f14-344d-bee4-95c223e30807 | -12.0638 | -50.0833 | 2026-09-21 18:30:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 126.9 |
| 026609e9-0780-3b9d-bba3-1294604f901e | -6.7463 | -59.4416 | 2026-09-21 18:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 75.8 |
| e87d3bec-77a8-331e-86d3-55f5edb9bf78 | -12.4204 | -47.0228 | 2026-09-21 18:30:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 98.8 |


[Clique aqui para ver as próximas entradas](README189.md)
