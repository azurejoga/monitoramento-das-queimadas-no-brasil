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

## Dados Diários - Página 38

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 05cb73c2-ca79-31ed-b8a9-7ee5b9c97736 | -12.89345 | -48.01165 | 2025-09-06 04:17:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| b35cb66b-5922-32c6-82a4-cc5b346ada43 | -6.55386 | -42.95006 | 2025-09-06 04:17:00 | NPP-375D | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 8850eccd-f810-39de-bff3-6913ee9f5d51 | -6.39924 | -46.08939 | 2025-09-06 04:17:00 | NPP-375D | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 352539f8-4839-33ec-9171-d2d6628407f4 | -14.58224 | -48.03603 | 2025-09-06 04:17:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| f14d82e6-7776-382d-a380-74028a252b01 | -5.8368 | -44.12481 | 2025-09-06 04:17:00 | NPP-375D | JATOBÁ | MARANHÃO | Brasil | 2105450 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 48430061-cad9-3e58-9baa-cf17c5132b6b | -10.4829 | -46.75101 | 2025-09-06 04:17:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 1fc125f3-5fbe-3a80-be68-241de82a381c | -8.03115 | -45.41828 | 2025-09-06 04:17:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| db68f662-a2be-37a3-ad87-70550b29412e | -6.26665 | -53.44043 | 2025-09-06 04:17:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 63dc9d4a-8526-32f1-8b4b-b34ea9d84623 | -10.0932 | -48.08316 | 2025-09-06 04:17:00 | NPP-375D | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| f0e4cc34-385d-38b4-ae34-7ca6004135bc | -5.44624 | -42.80749 | 2025-09-06 04:17:00 | NPP-375D | NAZÁRIA | PIAUÍ | Brasil | 2206720 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| ea665721-6461-303f-8c65-d0271c1a52e3 | -6.17112 | -44.30976 | 2025-09-06 04:17:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| b764bb63-60fa-3b89-bd65-20987964daf9 | -7.33237 | -48.49731 | 2025-09-06 04:17:00 | NPP-375D | ARAGUAÍNA | TOCANTINS | Brasil | 1702109 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 9a0193ae-ab9b-3320-9180-b8cd748f502e | -13.93953 | -53.99224 | 2025-09-06 04:17:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 7a872b8b-c68d-3604-84e2-ecc682acf3cf | -6.01963 | -43.69679 | 2025-09-06 04:17:00 | NPP-375D | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| e6877fd7-1c4b-36ba-8c5b-c465e4acede2 | -8.3497 | -52.5158 | 2025-09-06 04:17:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| b10d73c6-ac7c-3798-91c2-59308fc5f9ce | -9.81209 | -46.00371 | 2025-09-06 04:17:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 3624510e-bee7-3eaf-b646-bb7186aa25ca | -3.16702 | -48.60406 | 2025-09-06 04:17:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 8601ea06-9698-33ba-b3b6-277e1ea10ead | -5.95048 | -46.16521 | 2025-09-06 04:17:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| aebef76c-32bc-3f80-aebf-846da30e2320 | -5.84998 | -45.3085 | 2025-09-06 04:17:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 08f4e560-45c3-3775-866d-c569d12db625 | -6.16264 | -43.17698 | 2025-09-06 04:17:00 | NPP-375D | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 44e1cd29-94f5-3f57-9107-6e2cb669f43b | -9.70504 | -49.48906 | 2025-09-06 04:17:00 | NPP-375D | MARIANÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1712504 | 17 | 33 | nan | nan | nan | Cerrado | 9.2 |
| a674f6fb-0c9e-36a7-ba7e-8a2d6dc89c25 | -7.3334 | -43.94184 | 2025-09-06 04:17:00 | NPP-375D | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 252a7b8f-0ffc-3d30-bc02-98381d4baf8e | -7.21915 | -44.98027 | 2025-09-06 04:17:00 | NPP-375D | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| bd4fa012-97dc-3682-9ec0-48b6a87f3ab3 | -14.96111 | -47.59295 | 2025-09-06 04:17:00 | NPP-375D | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 9f7e18df-c591-38d9-b39a-373b906c175c | -7.16341 | -43.88633 | 2025-09-06 04:17:00 | NPP-375D | MARCOS PARENTE | PIAUÍ | Brasil | 2206001 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 3306a3d9-9b0b-3667-b1cb-293b9ce5bc9f | -5.83851 | -44.11409 | 2025-09-06 04:17:00 | NPP-375D | JATOBÁ | MARANHÃO | Brasil | 2105450 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 9fd5f22c-8c66-3feb-8201-938b6b9abbcb | -6.3987 | -46.09641 | 2025-09-06 04:17:00 | NPP-375D | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 00185b15-7144-3d8e-a9ce-f6a567e660f0 | -6.21252 | -42.62291 | 2025-09-06 04:17:00 | NPP-375D | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 5b687804-7a96-39f1-a5c0-429d79aafc76 | -15.84877 | -52.28155 | 2025-09-06 04:17:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 31330657-d09a-3201-b886-594e3e65a504 | -15.36409 | -46.41463 | 2025-09-06 04:17:00 | NPP-375D | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| ef71e056-38f4-3260-b73a-95ed95419364 | -2.5615 | -48.96622 | 2025-09-06 04:17:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| b815c215-d4af-3e7d-9bcf-415a198889a5 | -6.03457 | -43.70322 | 2025-09-06 04:17:00 | NPP-375D | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 2435c31c-db4e-3bd3-b731-850d9df22a08 | -5.95358 | -43.02267 | 2025-09-06 04:17:00 | NPP-375D | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 1a3cc204-bced-364f-ac8c-c7a82e38d754 | -12.99437 | -54.81662 | 2025-09-06 04:17:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| a8e9407c-dc84-3050-9255-dd4af96b3b88 | -8.44728 | -45.03275 | 2025-09-06 04:17:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 0e8e4edb-8adc-3a66-ada1-5eeb949debdd | -6.33883 | -43.56109 | 2025-09-06 04:17:00 | NPP-375D | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| da727cd7-1a26-3ca6-b9d2-2cc37c328e2e | -10.6045 | -44.32689 | 2025-09-06 04:17:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 32.0 |
| 6dd88c35-d318-3355-9eff-33b0b8ed253a | -5.26092 | -44.4524 | 2025-09-06 04:17:00 | NPP-375D | PRESIDENTE DUTRA | MARANHÃO | Brasil | 2109106 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 209db8d3-fe5b-306f-89d4-8ee8bc05c993 | -6.06875 | -43.30042 | 2025-09-06 04:17:00 | NPP-375D | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 14a4f759-1350-39a9-855a-278b1eedc140 | -5.9305 | -43.71862 | 2025-09-06 04:17:00 | NPP-375D | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 07597c2a-c977-369b-8e83-e7c222960f3b | -6.34373 | -53.44307 | 2025-09-06 04:17:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 86d7c9cb-126f-3240-adac-2ca3fb87eec9 | -6.17214 | -53.50628 | 2025-09-06 04:17:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| d45d2d7e-6e4b-3ba5-85f3-88c703a4d5f5 | -7.21359 | -43.9913 | 2025-09-06 04:17:00 | NPP-375D | MARCOS PARENTE | PIAUÍ | Brasil | 2206001 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| b769ffb2-087f-353e-8952-dfa788742de9 | -14.57359 | -48.02151 | 2025-09-06 04:17:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 70c04247-e659-3a7f-a744-5ac0f9fde4c7 | -5.74166 | -43.69601 | 2025-09-06 04:17:00 | NPP-375D | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 0c5ba2f8-d241-3d03-be9c-d1b7bc260ce9 | -5.55968 | -46.53768 | 2025-09-06 04:17:00 | NPP-375D | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 513ec02f-decb-3805-bd5b-45cb83163cf1 | -3.24313 | -50.80566 | 2025-09-06 04:17:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| f10b56c3-01eb-3e52-a0ba-38cc89919f09 | -6.24533 | -42.43534 | 2025-09-06 04:17:00 | NPP-375D | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 67eac301-4c28-30d1-a4c5-d819abf5d582 | -9.00825 | -49.79913 | 2025-09-06 04:17:00 | NPP-375D | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 0980b9c2-46fc-3bfe-9e34-5c8b3736cb91 | -6.61753 | -43.9794 | 2025-09-06 04:17:00 | NPP-375D | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 1e42a282-9ee0-3a5b-9b1a-c1d1026ac57d | -7.95841 | -44.94323 | 2025-09-06 04:17:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| feb01e33-46a9-3232-ae67-585fbd8f516e | -2.56532 | -48.97166 | 2025-09-06 04:17:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 858f9c2f-2627-3d54-9e28-2c7bb6d4dba6 | -4.0332 | -42.52155 | 2025-09-06 04:17:00 | NPP-375D | NOSSA SENHORA DOS REMÉDIOS | PIAUÍ | Brasil | 2206803 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| f6b0bbec-0e2d-347c-b7f1-e6019a2b2029 | -5.96944 | -53.59875 | 2025-09-06 04:17:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 352310bd-de03-3d66-8daf-4aa75d850e90 | -13.66392 | -46.95242 | 2025-09-06 04:17:00 | NPP-375D | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 3dc9e534-0032-3ee1-8fbd-8bff0045bed0 | -13.85193 | -46.26204 | 2025-09-06 04:17:00 | NPP-375D | GUARANI DE GOIÁS | GOIÁS | Brasil | 5209408 | 52 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 58a7f8c6-92e0-3210-8330-7cb81bbb2b11 | -9.33537 | -42.4397 | 2025-09-06 04:17:00 | NPP-375D | DIRCEU ARCOVERDE | PIAUÍ | Brasil | 2203354 | 22 | 33 | nan | nan | nan | Caatinga | 0.5 |
| 3dda1acb-87a2-3d55-a5ce-c1bae027d50a | -5.87095 | -52.16768 | 2025-09-06 04:17:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| af2e7c4d-b658-3d31-9af2-f3d3644c77a2 | -14.1813 | -53.0621 | 2025-09-06 04:17:00 | NPP-375D | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 13.0 |
| 76cf18c9-a0b3-3950-a4cd-19cac321b65f | -5.58225 | -51.91479 | 2025-09-06 04:17:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 1157ad73-2228-3159-be42-c567381d5073 | -6.41131 | -44.46566 | 2025-09-06 04:17:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 1960ae44-2c50-3cc2-9fa3-db4fdfaf78cf | -14.83145 | -48.19798 | 2025-09-06 04:17:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| cca4d8fa-90e0-3b3f-a81e-3fbd11bc5d27 | -5.94543 | -46.1731 | 2025-09-06 04:17:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| ecb4b311-d8a3-3d36-ba0d-395af0fe4032 | -11.48005 | -55.55213 | 2025-09-06 04:17:00 | NPP-375D | SINOP | MATO GROSSO | Brasil | 5107909 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 93f79558-fb94-3503-a9a9-c6e14b829f58 | -8.18462 | -49.58792 | 2025-09-06 04:17:00 | NPP-375D | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 9f68dc72-f5fc-36fc-b944-21c91cad5caa | -12.48644 | -53.85859 | 2025-09-06 04:17:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 846903d1-1745-34b7-a358-7693c77adb7c | -13.74531 | -46.92229 | 2025-09-06 04:17:00 | NPP-375D | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 2445ebc7-18b8-327b-a606-3929295d807f | -6.55222 | -42.96048 | 2025-09-06 04:17:00 | NPP-375D | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 4a926c45-9408-3ec0-96aa-3c9d307c2b53 | -8.75529 | -39.81414 | 2025-09-06 04:17:00 | NPP-375D | SANTA MARIA DA BOA VISTA | PERNAMBUCO | Brasil | 2612604 | 26 | 33 | nan | nan | nan | Caatinga | 2.7 |
| 5337c816-307c-355e-b8bf-cab0cb1901d7 | -2.55511 | -48.39128 | 2025-09-06 04:17:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 652e7889-a9ec-3534-bea3-7af96488fa93 | -6.24275 | -43.28911 | 2025-09-06 04:17:00 | NPP-375D | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 3c45ae8e-42bf-3be2-b1e6-ef870cb19f7d | -6.26883 | -53.42828 | 2025-09-06 04:17:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 9888e09c-7225-3037-b0d2-9a333683cb00 | -16.92251 | -45.7592 | 2025-09-06 04:17:00 | NPP-375D | BRASILÂNDIA DE MINAS | MINAS GERAIS | Brasil | 3108552 | 31 | 33 | nan | nan | nan | Cerrado | 23.8 |
| 7e4da333-332b-34eb-995b-e8f82e547233 | -12.95486 | -54.79659 | 2025-09-06 04:17:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 41710d8e-16e2-3ea0-8015-2ca6863c5dbd | -5.20142 | -43.69001 | 2025-09-06 04:17:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 02bf359d-b118-3700-a4de-789985927e23 | -5.9569 | -43.02319 | 2025-09-06 04:17:00 | NPP-375D | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 3685cb3d-b3a8-3869-b470-149510ea7809 | -9.01694 | -49.80069 | 2025-09-06 04:17:00 | NPP-375D | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| ef091ac9-4b95-34f3-a673-3b9c0d32dd11 | -2.99007 | -47.4521 | 2025-09-06 04:17:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 209a2cbe-7e4e-3253-9859-043781d328f4 | -5.91453 | -43.22627 | 2025-09-06 04:17:00 | NPP-375D | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 933060b5-3af7-3a6c-81ea-f74b7b3e7352 | -10.09242 | -48.08767 | 2025-09-06 04:17:00 | NPP-375D | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 20f6cc46-8912-3b04-8303-bdd2f1ad3fcb | -6.00899 | -46.69415 | 2025-09-06 04:17:00 | NPP-375D | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 1d28f005-1f75-327f-8ec1-0e798edcfb7b | -13.59256 | -43.34992 | 2025-09-06 04:17:00 | NPP-375D | BOM JESUS DA LAPA | BAHIA | Brasil | 2903904 | 29 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 101be0a1-2694-376b-8801-2349a247d3b2 | -6.54733 | -43.92464 | 2025-09-06 04:17:00 | NPP-375D | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 26437b7d-af49-3594-998c-07532652d46a | -9.78102 | -46.90922 | 2025-09-06 04:17:00 | NPP-375D | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 0e5d1014-7e6a-303a-b8f1-946df2875435 | -13.84392 | -46.26828 | 2025-09-06 04:17:00 | NPP-375D | GUARANI DE GOIÁS | GOIÁS | Brasil | 5209408 | 52 | 33 | nan | nan | nan | Cerrado | 7.2 |
| bb04f060-9794-3dec-9acc-ed38b413a3c2 | -6.16424 | -53.68801 | 2025-09-06 04:17:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| f02943aa-b83f-3980-a00e-94dfedce72e0 | -10.06556 | -48.07167 | 2025-09-06 04:17:00 | NPP-375D | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 37f66dda-3feb-3f9a-ae92-66faeeed2a8d | -14.83509 | -48.19849 | 2025-09-06 04:17:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 3d7001f1-5aee-3137-a902-8e0a19605359 | -13.00094 | -54.84269 | 2025-09-06 04:17:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 75d8e418-efb7-338a-ae81-eadd3e51685c | -6.26446 | -53.45266 | 2025-09-06 04:17:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 21eee281-3faa-398a-8479-caabef3511ca | -4.61077 | -41.54086 | 2025-09-06 04:17:00 | NPP-375D | MILTON BRANDÃO | PIAUÍ | Brasil | 2206357 | 22 | 33 | nan | nan | nan | Caatinga | 3.0 |
| 26aa1c17-efeb-3866-a138-37cf6af10752 | -5.72298 | -43.92077 | 2025-09-06 04:17:00 | NPP-375D | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| cca7646d-d0c0-3c2d-a5d2-c9a64279f966 | -7.05146 | -44.3508 | 2025-09-06 04:17:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 6e507383-636b-3062-910e-05fb610fd10f | -5.94557 | -53.79671 | 2025-09-06 04:17:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 66aa4b1b-dc71-39d6-854a-92ec72ae1ac9 | -7.33285 | -43.94534 | 2025-09-06 04:17:00 | NPP-375D | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| c856f0b8-21e2-3a4b-89c2-1292bf847f25 | -5.21482 | -43.69212 | 2025-09-06 04:17:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| ffd10525-d9d1-362e-8c9e-2cf6a46435ba | -12.96379 | -54.82276 | 2025-09-06 04:17:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 280a94b3-a0f4-3fae-af6a-efb7803bf5c1 | -8.45068 | -45.03328 | 2025-09-06 04:17:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 5.6 |
| f6cf585f-af85-3140-b9e5-97bb52dbaee7 | -8.06209 | -52.38363 | 2025-09-06 04:17:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| f1a5afa4-b588-3cfa-a5a4-b1315207c827 | -6.00013 | -44.15463 | 2025-09-06 04:17:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |


[Clique aqui para ver as próximas entradas](README39.md)
