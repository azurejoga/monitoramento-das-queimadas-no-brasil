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

## Dados Diários - Página 97

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 0e44d1e0-8e2d-3803-8ead-f35034a6388e | -9.12674 | -65.86762 | 2026-09-22 05:23:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 8efc7b27-e8a4-3bf6-ab06-6a02924a771d | -9.76232 | -65.06137 | 2026-09-22 05:23:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.6 |
| c47405d3-512b-31c0-bef8-c882456b448b | -5.13443 | -49.93761 | 2026-09-22 05:23:00 | NPP-375D | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 287691b8-ba6d-3961-8e65-c30396d6aaec | -14.04895 | -52.05727 | 2026-09-22 05:23:00 | NPP-375D | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| e5d6caa1-7514-3aaf-bc0b-f17497a14371 | -6.77193 | -59.62991 | 2026-09-22 05:23:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 74206838-0358-303c-b51c-47ab70bc7c24 | -4.38539 | -55.03002 | 2026-09-22 05:23:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 75140a1f-f208-3eb1-944b-331c52257beb | -6.43367 | -55.6072 | 2026-09-22 05:23:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 2e527e10-5aa8-323d-8d49-d03a57d7afc3 | -6.78882 | -59.13781 | 2026-09-22 05:23:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 927b445b-df6d-388b-a712-d834b0ae71cc | -5.98234 | -57.70233 | 2026-09-22 05:23:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| dba3d6fb-e8a7-3752-a3f7-bab4112e50c3 | -12.78905 | -54.03841 | 2026-09-22 05:23:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 2748f81f-072f-370a-8ddf-d1e30ee85195 | -6.77691 | -58.60837 | 2026-09-22 05:23:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 838fe2ce-2b16-3fba-b544-6312da094b15 | -12.29177 | -50.71679 | 2026-09-22 05:23:00 | NPP-375D | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 7711172d-733d-32ca-b5e1-7d5b6d48e23d | -6.13542 | -59.87955 | 2026-09-22 05:23:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 4393fe97-c1dc-3276-a046-1290cfdfe02a | -11.49955 | -51.51057 | 2026-09-22 05:23:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 5119f55b-a41e-386a-b6bf-31a6906b1b47 | -2.86018 | -57.8059 | 2026-09-22 05:23:00 | NPP-375D | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 870e4046-ddeb-346f-b677-8d8641b21d71 | -4.18393 | -51.23964 | 2026-09-22 05:23:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 0256aa00-e3aa-3e89-90d9-ddb9b20af233 | -9.55332 | -66.03306 | 2026-09-22 05:23:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 97376062-1331-3e0e-9e2c-496a32e41d9b | -10.09869 | -69.12868 | 2026-09-22 05:23:00 | NPP-375D | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 0.8 |
| a42901ec-3b16-39d9-8c50-c47dea473a48 | -5.76105 | -45.09492 | 2026-09-22 05:23:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| e2bb1748-d679-3fec-923e-738bd10f46cb | -5.30999 | -56.00941 | 2026-09-22 05:23:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 8cf6d348-6164-3611-be5f-7685f2746621 | -1.74634 | -47.13992 | 2026-09-22 05:23:00 | NPP-375D | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 0126d914-3fcb-35de-b525-7a232d710f75 | -7.33122 | -55.60143 | 2026-09-22 05:23:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| e4ec5797-2795-37f3-b3e7-79004100b581 | -7.56696 | -57.67669 | 2026-09-22 05:23:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 086f0ec3-5c42-3630-8c80-b47fb5dbcbfe | -7.40082 | -55.22171 | 2026-09-22 05:23:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f3587810-0a26-3008-bdbd-26322dac46a9 | -2.40794 | -58.27693 | 2026-09-22 05:23:00 | NPP-375D | ITAPIRANGA | AMAZONAS | Brasil | 1302009 | 13 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 202ca818-831f-33ac-8806-60abf1735dd1 | -6.28686 | -57.74331 | 2026-09-22 05:23:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 236e9af5-437c-34a5-b450-e6a7c24cf2f3 | -6.35923 | -58.29079 | 2026-09-22 05:23:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 3.4 |
| a5e6f6a7-1d40-3988-af56-f23ac0c06fcb | -6.86043 | -59.90436 | 2026-09-22 05:23:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 2d4f523f-bfd6-3d0e-b476-99910d5391af | -5.84807 | -49.78852 | 2026-09-22 05:23:00 | NPP-375D | CURIONÓPOLIS | PARÁ | Brasil | 1502772 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e3ccf747-4446-35ba-b87d-e22cafc0230d | -10.91793 | -53.95279 | 2026-09-22 05:23:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| acacf70a-6136-30ee-813b-1331be8255a8 | -2.9657 | -57.62971 | 2026-09-22 05:23:00 | NPP-375D | BOA VISTA DO RAMOS | AMAZONAS | Brasil | 1300680 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 8f61f213-560b-34bb-be27-8908dca700d0 | -3.3397 | -59.85043 | 2026-09-22 05:23:00 | NPP-375D | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 11362b6b-0151-3e38-a033-e3cf36bd7876 | -9.09842 | -65.37294 | 2026-09-22 05:23:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 7941944d-3037-31e3-801c-e770592c3652 | -8.14739 | -54.80968 | 2026-09-22 05:23:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 3847bcf0-7b0d-3603-a9c1-27e38abbe93d | -9.55522 | -66.05042 | 2026-09-22 05:23:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 3778b8bd-3b47-3710-8970-b9cea913aad7 | -3.01502 | -54.18345 | 2026-09-22 05:23:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 54178d1c-ea64-3cc7-a5a6-e32d86ffb807 | -7.39616 | -55.22868 | 2026-09-22 05:23:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 53376cc3-b079-3c8a-80b2-8757432ba43a | -9.56221 | -66.01201 | 2026-09-22 05:23:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 30d59d63-c5ef-349b-b1a1-917cace38854 | -3.60728 | -60.57523 | 2026-09-22 05:23:00 | NPP-375D | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 4.2 |
| f99ec0de-3e45-33ef-9eea-f10009bf2e1d | -9.39914 | -65.91636 | 2026-09-22 05:23:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 3.3 |
| bd44e688-851e-31c8-8f21-9e5f745c4993 | -6.35125 | -57.76783 | 2026-09-22 05:23:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ea06c0aa-4556-3cab-891f-3b38b9c08045 | -6.3481 | -57.88948 | 2026-09-22 05:23:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 7.0 |
| f5db4f7a-b689-337c-a091-4fa60eb23237 | -3.92087 | -56.04981 | 2026-09-22 05:23:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| ad070ae4-0a74-3745-82b5-1ee328031897 | -5.42145 | -60.21801 | 2026-09-22 05:23:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 33ff9280-3052-3d4e-acbc-50e2a21b2eed | -7.2327 | -55.58677 | 2026-09-22 05:23:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 1f844e07-bb59-31d3-a9bd-6ca34ce83601 | -4.12594 | -54.29453 | 2026-09-22 05:23:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 6d82142f-0d3c-3fe3-bdb0-1a564b464d16 | -12.2967 | -50.71746 | 2026-09-22 05:23:00 | NPP-375D | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| ade54d97-3cb8-34b4-af39-35f7aef3ec7c | -11.04853 | -54.155 | 2026-09-22 05:23:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| f5d3501d-76db-3102-8add-8a9acf3c8cb8 | -7.60442 | -55.35675 | 2026-09-22 05:23:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| b4a92cd7-92a7-32ef-a0a2-7cbaa594ff78 | -11.31593 | -54.03957 | 2026-09-22 05:23:00 | NPP-375D | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 5324f1d0-b862-310b-84c6-f8d292c805dc | -6.64862 | -59.91966 | 2026-09-22 05:23:00 | NPP-375D | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 9db2bb3d-d600-3aea-ab0a-fa08897253d6 | -5.84784 | -49.78979 | 2026-09-22 05:23:00 | NPP-375D | CURIONÓPOLIS | PARÁ | Brasil | 1502772 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| cc5e6e75-2ef1-379b-8576-bdc957a4b61d | -9.2757 | -46.18022 | 2026-09-22 05:23:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 67b17e86-d5af-3245-9012-5f257fb98a8c | -6.09999 | -57.68521 | 2026-09-22 05:23:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 5d2168bb-9e4c-3a97-a71c-37e212c4040d | -7.42272 | -49.83704 | 2026-09-22 05:23:00 | NPP-375D | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 96082740-e1da-3eb1-b65b-eb8b159ce94f | -3.78756 | -60.74966 | 2026-09-22 05:23:00 | NPP-375D | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 2671bbf6-eb82-3b5e-b5b3-5de00b05875d | -1.38215 | -49.32366 | 2026-09-22 05:23:00 | NPP-375D | MUANÁ | PARÁ | Brasil | 1504901 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 76936271-0718-34f0-b2e7-7fc357c9ffa5 | -6.89908 | -46.01279 | 2026-09-22 05:23:00 | NPP-375D | FORTALEZA DOS NOGUEIRAS | MARANHÃO | Brasil | 2104107 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| afb8b992-ef03-345b-9c33-169f3fd8b9b3 | -3.98177 | -60.03133 | 2026-09-22 05:23:00 | NPP-375D | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 366d0eb6-6d5b-3741-b52a-45aa04cd56b4 | -10.90409 | -53.96585 | 2026-09-22 05:23:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 4ddfcd57-1c65-316f-98db-ef3efc8ce5a7 | -2.61429 | -51.72358 | 2026-09-22 05:23:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 9e970354-b4b3-3170-93fb-62b8044388af | -2.9477 | -51.04535 | 2026-09-22 05:23:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 35f68bd6-cc79-3174-8f3d-5149cc0966aa | -4.3029 | -56.26328 | 2026-09-22 05:23:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 15821820-ade4-3829-ba94-2e7db8c4c776 | -6.13997 | -57.77728 | 2026-09-22 05:23:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 2db65a69-22c2-3473-93a2-699bddff0e42 | -4.18335 | -51.24351 | 2026-09-22 05:23:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| f67ae344-1aeb-31db-bfb5-86a0714a0682 | -2.95838 | -51.42559 | 2026-09-22 05:23:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 7aba9c17-9a5e-3595-94f7-c96d1f5a04f1 | -3.07463 | -61.17458 | 2026-09-22 05:23:00 | NPP-375D | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 85fa95eb-0ad5-3c77-a52f-e37d9d2feacf | -10.90726 | -53.97141 | 2026-09-22 05:23:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 056a7917-ac20-3ea4-ab24-3a956c89b942 | -1.4521 | -54.24211 | 2026-09-22 05:23:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 1582ba91-1079-3a42-9a74-68bce4b540d9 | -3.06325 | -61.27036 | 2026-09-22 05:23:00 | NPP-375D | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 43dced3a-7f77-3819-a77f-7b49a0dd1d12 | -4.29859 | -55.07413 | 2026-09-22 05:23:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a501aebc-6cb3-391a-9c30-02c06a7b3220 | -4.14007 | -59.39169 | 2026-09-22 05:23:00 | NPP-375D | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c923f5ca-aa5b-3cbe-ae66-07f5acd6084a | -6.73667 | -55.0686 | 2026-09-22 05:23:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 00b8d820-3c78-37c0-9983-5865d5859c92 | -3.37697 | -50.4415 | 2026-09-22 05:23:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| ce1c6ea0-8b19-3a4f-97a5-18fef679e0c4 | -1.33324 | -54.66463 | 2026-09-22 05:23:00 | NPP-375D | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 7.0 |
| 2da0f249-7ba5-3673-b1e4-1900bea2302c | -12.77525 | -52.85379 | 2026-09-22 05:23:00 | NPP-375D | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 903b72d5-a480-3726-9d7e-2cc7348b6a62 | -3.4032 | -61.29499 | 2026-09-22 05:23:00 | NPP-375D | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 2.9 |
| ce2191e5-0a46-397f-bee2-582601a0d6ec | -6.14263 | -59.94569 | 2026-09-22 05:23:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 7b2fa010-b5e2-3688-9340-cb01d9f28784 | -6.51853 | -58.30505 | 2026-09-22 05:23:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| dd2372e5-554d-3bcb-ae59-74c73bbe02e2 | -6.09334 | -56.46725 | 2026-09-22 05:23:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 2373f0be-2088-33ed-b4cb-765c853a3baf | -3.68717 | -60.58123 | 2026-09-22 05:23:00 | NPP-375D | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 4.9 |
| d6c1db38-226c-35cc-b73f-b13c929c99a1 | -8.83805 | -50.48683 | 2026-09-22 05:23:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 23737263-2df3-3c88-b8b3-d30aa3452d48 | -3.8212 | -58.88965 | 2026-09-22 05:23:00 | NPP-375D | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 13c2780c-eabe-32a1-8f1c-f35eb96d3f33 | -13.33344 | -51.28142 | 2026-09-22 05:23:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 7557b613-7bd1-3b15-8465-ca74d5ed18da | -9.1362 | -67.95267 | 2026-09-22 05:23:00 | NPP-375D | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 85ea4ba7-fd5b-3df3-92db-62d2ae312941 | -6.9234 | -55.61986 | 2026-09-22 05:23:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 8d4152d2-e059-3c20-8a4d-64f3d251cf93 | -4.54978 | -54.93299 | 2026-09-22 05:23:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 8f5104ef-e56d-3c55-882f-d50a120c2a37 | -15.25385 | -47.60845 | 2026-09-22 05:23:00 | NPP-375D | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| fbdf86a2-d905-3e41-bdfd-a5994b04cc5b | -5.81849 | -57.73663 | 2026-09-22 05:23:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| daf1683d-cbc6-37a9-a290-96c9a182b956 | -7.33351 | -55.60937 | 2026-09-22 05:23:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e0d7bda7-c349-3268-85d4-388366038608 | -4.85671 | -56.07328 | 2026-09-22 05:23:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| f468bdae-b796-3f1c-a5b5-b36ae779dd6a | -2.78926 | -59.88619 | 2026-09-22 05:23:00 | NPP-375D | MANAUS | AMAZONAS | Brasil | 1302603 | 13 | 33 | nan | nan | nan | Amazônia | 3.2 |
| afba1e3d-ed29-38ba-9a46-61c28a44cd4b | -3.04824 | -61.26272 | 2026-09-22 05:23:00 | NPP-375D | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 913376d1-e480-3988-a319-9547105ebcf4 | -4.50595 | -59.5603 | 2026-09-22 05:23:00 | NPP-375D | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 10accdbb-391c-3ebe-8637-9e2b57e23a23 | -7.45433 | -44.74964 | 2026-09-22 05:23:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.8 |
| bcc5c642-1ecf-37a1-9def-c065ab0dc28e | -3.4785 | -59.59702 | 2026-09-22 05:23:00 | NPP-375D | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 6a34aeae-d5c0-3406-946c-b767143dc3c7 | -6.15437 | -57.70814 | 2026-09-22 05:23:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| de811a6a-c19a-3cbf-a77f-75b81f063891 | -6.01056 | -45.24967 | 2026-09-22 05:23:00 | NPP-375D | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 9.6 |
| 3f124552-d196-326e-93fc-e72db89e3498 | -5.41784 | -60.21742 | 2026-09-22 05:23:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| fe013e0a-3cd4-39c8-b8e0-e1560fb23c8f | -6.22647 | -56.04481 | 2026-09-22 05:23:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |


[Clique aqui para ver as próximas entradas](README98.md)
