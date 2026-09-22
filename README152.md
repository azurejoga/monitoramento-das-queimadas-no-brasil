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

## Dados Diários - Página 152

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| dfd29f0a-c9c9-3a2e-9c8a-ec78d428e6ec | -3.4214 | -60.2086 | 2026-09-22 15:30:00 | GOES-19 | CAREIRO | AMAZONAS | Brasil | 1301100 | 13 | 33 | nan | nan | nan | Amazônia | 62.2 |
| 7a954f48-86ed-35ad-b3d3-9f41f8d44baa | -6.2024 | -47.5245 | 2026-09-22 15:30:00 | GOES-19 | TOCANTINÓPOLIS | TOCANTINS | Brasil | 1721208 | 17 | 33 | nan | nan | nan | Cerrado | 66.2 |
| 8ae69753-f31e-374f-a9e3-04fdd19a3d46 | -6.4671 | -59.9711 | 2026-09-22 15:30:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 101.3 |
| 0c036373-e8c3-3775-bd4f-956d9ebed077 | -11.1337 | -49.9978 | 2026-09-22 15:30:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 90.8 |
| 7268d01e-41f7-300b-b620-864e075444ec | -3.0719 | -61.1819 | 2026-09-22 15:30:00 | GOES-19 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 43.3 |
| 233d4c7a-183c-3b40-be47-8930de73ccb3 | 3.6753 | -60.9632 | 2026-09-22 15:30:00 | GOES-19 | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 73.4 |
| 196a9310-baed-3033-b7db-3e3332c2794b | -5.4179 | -60.2166 | 2026-09-22 15:30:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 123.7 |
| 8cb518cc-c877-3602-b307-20d942167604 | -6.8985 | -41.6976 | 2026-09-22 15:30:00 | GOES-19 | IPIRANGA DO PIAUÍ | PIAUÍ | Brasil | 2204808 | 22 | 33 | nan | nan | nan | Caatinga | 636.1 |
| 8ae0d82c-eb49-3801-bc4e-a4ebee85ddff | -3.6033 | -60.5664 | 2026-09-22 15:30:00 | GOES-19 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 119.0 |
| 584529d2-1cbe-31c2-ba88-98e90668487e | -8.1304 | -62.8763 | 2026-09-22 15:30:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 59.2 |
| e343b75d-1234-3fb5-8785-b50ce7362f0a | 1.9056 | -50.8414 | 2026-09-22 15:30:00 | GOES-19 | AMAPÁ | AMAPÁ | Brasil | 1600105 | 16 | 33 | nan | nan | nan | Amazônia | 61.8 |
| 8dde2efe-62ca-3656-976b-89fc0b1ddac2 | -3.2396 | -53.9417 | 2026-09-22 15:30:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 96.5 |
| ef0e9429-7922-3a16-a7c5-ec1583268ea3 | -3.132 | -59.029 | 2026-09-22 15:30:00 | GOES-19 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 151.0 |
| 447d7843-bafc-31cb-b3be-6d3094581dbb | 1.2794 | -50.8718 | 2026-09-22 15:30:00 | GOES-19 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 97.3 |
| d127e9f8-1184-399d-9e93-4da884f12c48 | -10.3171 | -50.2138 | 2026-09-22 15:30:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 92.1 |
| a1dbb860-86ec-317a-afe5-9a75f1123d8b | -8.1686 | -54.7634 | 2026-09-22 15:30:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 54.6 |
| 61402358-4fbe-3b4b-8d36-2adc3f29058b | 1.3817 | -56.0636 | 2026-09-22 15:30:00 | GOES-19 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 59.3 |
| feeac9f4-9c7e-3ada-982a-4b7367f72eb9 | -3.1851 | -59.6982 | 2026-09-22 15:30:00 | GOES-19 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 137.2 |
| 2af4542f-39c1-359f-84d9-aef5fbc4041c | 4.1314 | -61.2945 | 2026-09-22 15:30:00 | GOES-19 | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 69.7 |
| 403eab26-1e66-37b6-b84d-1cccaa6bf9a9 | -10.2787 | -50.2605 | 2026-09-22 15:30:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 80.7 |
| 570d5033-9adc-36b8-ab59-84c528fee7bd | -3.3309 | -59.8673 | 2026-09-22 15:30:00 | GOES-19 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 78.8 |
| 8257df9a-93cf-3464-af80-3df6df832359 | -3.2372 | -60.8007 | 2026-09-22 15:40:00 | GOES-19 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 64.0 |
| 0aa5bdbd-123b-3568-a89a-37eca74c8bca | -2.9709 | -57.7197 | 2026-09-22 15:40:00 | GOES-19 | BOA VISTA DO RAMOS | AMAZONAS | Brasil | 1300680 | 13 | 33 | nan | nan | nan | Amazônia | 55.4 |
| 51efe0c0-817f-3ce1-a904-9920ceadedec | -8.6173 | -54.5924 | 2026-09-22 15:40:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 48.3 |
| e996bf47-1266-3d35-9171-54f99eea8790 | -6.1111 | -57.6645 | 2026-09-22 15:40:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 173.0 |
| 977ae1ff-db9b-35b7-bff5-90fe88f00a73 | -11.3784 | -44.2195 | 2026-09-22 15:40:00 | GOES-19 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 378.8 |
| 1cc8ea9f-e6a7-3131-8494-5a22ec3c777e | -3.1718 | -57.8708 | 2026-09-22 15:40:00 | GOES-19 | BOA VISTA DO RAMOS | AMAZONAS | Brasil | 1300680 | 13 | 33 | nan | nan | nan | Amazônia | 52.7 |
| 3be2039b-286f-3dde-b3ae-84a02f557bfd | -3.5501 | -59.9584 | 2026-09-22 15:40:00 | GOES-19 | CAREIRO | AMAZONAS | Brasil | 1301100 | 13 | 33 | nan | nan | nan | Amazônia | 54.4 |
| 03317a92-7a5e-342f-87bc-4f661fd12a0c | -2.9997 | -60.8047 | 2026-09-22 15:40:00 | GOES-19 | IRANDUBA | AMAZONAS | Brasil | 1301852 | 13 | 33 | nan | nan | nan | Amazônia | 72.0 |
| a5330a50-6123-3ca8-9fd2-d49cdcee7539 | -3.1721 | -57.7932 | 2026-09-22 15:40:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 42.8 |
| f5149eda-8564-3992-a711-886f8ab92909 | -6.295 | -57.735 | 2026-09-22 15:40:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 98.0 |
| 4c7585e0-82d5-31d6-9fe1-83677b814f78 | -3.7181 | -58.8823 | 2026-09-22 15:40:00 | GOES-19 | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | 65.6 |
| 35e7f3c7-4898-3d00-9868-cbe3d748382b | -2.5873 | -57.3965 | 2026-09-22 15:40:00 | GOES-19 | PARINTINS | AMAZONAS | Brasil | 1303403 | 13 | 33 | nan | nan | nan | Amazônia | 48.0 |
| dc5476b2-d704-31e7-907b-268c2011500d | -3.1541 | -57.6772 | 2026-09-22 15:40:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 57.8 |
| 2587d371-e8d5-3b5a-af8a-415ed580bda8 | -3.3138 | -59.4472 | 2026-09-22 15:40:00 | GOES-19 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 83.1 |
| 3e11fb01-6ded-3b87-8329-56ae1b0e0e3d | 1.9056 | -50.8414 | 2026-09-22 15:40:00 | GOES-19 | AMAPÁ | AMAPÁ | Brasil | 1600105 | 16 | 33 | nan | nan | nan | Amazônia | 61.4 |
| b090dab4-2401-31d6-9fb7-2a9727ea22b0 | -3.6033 | -60.5664 | 2026-09-22 15:40:00 | GOES-19 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 218.9 |
| 910552e0-342f-33a5-a24c-1d8479a2e455 | -3.4368 | -61.3081 | 2026-09-22 15:40:00 | GOES-19 | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 56.0 |
| 7869e2fb-979f-32f8-b4d4-8e9a5fa855f5 | -12.4182 | -45.0385 | 2026-09-22 15:40:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 137.4 |
| f07689a3-4070-3a55-965a-cd88268bb6b2 | -6.4486 | -59.9717 | 2026-09-22 15:40:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 102.3 |
| bd2b6e4f-a6b5-338f-8d25-4afa2e8d2a42 | -10.2795 | -50.1963 | 2026-09-22 15:40:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 65.2 |
| 80485e2f-c227-3fba-95f9-4f4194042312 | -3.3183 | -57.8677 | 2026-09-22 15:40:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 64.0 |
| 1922d3e7-d73b-3edd-b620-0e2673792b81 | -1.9483 | -56.6064 | 2026-09-22 15:40:00 | GOES-19 | FARO | PARÁ | Brasil | 1503002 | 15 | 33 | nan | nan | nan | Amazônia | 42.2 |
| 53518b1f-04ab-3ba9-8398-c44f5ab50ae4 | -3.713 | -60.5452 | 2026-09-22 15:40:00 | GOES-19 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 65.8 |
| 5fb8ab25-8887-3d1a-8999-dfb0c6a9e8fd | -3.6449 | -58.8647 | 2026-09-22 15:40:00 | GOES-19 | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | 58.9 |
| b0ecc473-505c-38ce-8833-6eb59c10bd22 | -3.4214 | -60.2086 | 2026-09-22 15:40:00 | GOES-19 | CAREIRO | AMAZONAS | Brasil | 1301100 | 13 | 33 | nan | nan | nan | Amazônia | 67.0 |
| 10e17b85-c646-3dea-a0e0-4f5b3dcdbc82 | -3.3136 | -59.5046 | 2026-09-22 15:40:00 | GOES-19 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 52.0 |
| 4d256c4e-eb31-3e39-9df7-b4e3aa566ddf | 2.0963 | -55.8575 | 2026-09-22 15:40:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 54.9 |
| 4bd396f5-aeae-345f-9e22-9d9dc0e0e089 | -3.0719 | -61.163 | 2026-09-22 15:40:00 | GOES-19 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 41.8 |
| ac030f67-9fea-3db8-80fa-1820e0cbd1c6 | -10.336 | -50.2119 | 2026-09-22 15:40:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 104.0 |
| 3fcc64d3-1b37-3d87-ab8e-d8dbec1f0b65 | -9.7693 | -46.0615 | 2026-09-22 15:40:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 104.8 |
| 4a849521-943f-3e7c-a81f-4d4414dba921 | -6.3012 | -59.9962 | 2026-09-22 15:40:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 82.1 |
| f7e6134c-6543-3d8d-9adc-11d21ddac7ff | -8.1304 | -62.8763 | 2026-09-22 15:40:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 70.5 |
| 355f09e8-0833-3277-be7e-aaba172b4535 | -3.0535 | -61.2578 | 2026-09-22 15:40:00 | GOES-19 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 59.6 |
| 5d4c858d-2267-377e-9d01-2a72bf357b8a | 3.0199 | -59.9874 | 2026-09-22 15:40:00 | GOES-19 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 47.7 |
| e3fe417f-5519-38c8-88c3-98ffb87161ff | -3.1902 | -57.851 | 2026-09-22 15:40:00 | GOES-19 | BOA VISTA DO RAMOS | AMAZONAS | Brasil | 1300680 | 13 | 33 | nan | nan | nan | Amazônia | 52.5 |
| 1e6ad510-b589-34dd-ad7f-a8f926b31884 | -3.3309 | -59.8673 | 2026-09-22 15:40:00 | GOES-19 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 87.6 |
| f25f157c-9fa5-3685-9c29-f5da14c23e6b | -6.3195 | -60.0147 | 2026-09-22 15:40:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 64.1 |
| a15f4bfe-26e8-3953-ab46-643da6efb2c8 | -3.1358 | -57.6775 | 2026-09-22 15:40:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 54.8 |
| 792850f6-900b-310e-a4bb-e830745c7658 | -3.9509 | -60.5022 | 2026-09-22 15:40:00 | GOES-19 | CAREIRO | AMAZONAS | Brasil | 1301100 | 13 | 33 | nan | nan | nan | Amazônia | 129.1 |
| fc4fc09d-f95f-3bc4-aefd-c664870d6b1a | -3.6447 | -58.9224 | 2026-09-22 15:40:00 | GOES-19 | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | 159.5 |
| 9b547176-4416-3929-b1a1-ca7b64764d82 | -3.4059 | -59.2155 | 2026-09-22 15:40:00 | GOES-19 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 62.3 |
| 5b887d6c-007b-3154-a1e3-0a423ba7c2d1 | -12.283 | -50.7011 | 2026-09-22 15:40:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 101.3 |
| 13451119-246a-3c9c-8001-a6820baaada3 | -3.4241 | -59.2535 | 2026-09-22 15:40:00 | GOES-19 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 41.6 |
| bca286c2-b430-3cd4-8bb7-c71c40951383 | -3.6065 | -59.4413 | 2026-09-22 15:40:00 | GOES-19 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 93.1 |
| 94ac6b30-a025-362b-9320-8d24168efa1a | -9.2468 | -57.1686 | 2026-09-22 15:40:00 | GOES-19 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 199.5 |
| 34993a64-c775-3ea3-8523-dc80ab1c55cc | -6.3135 | -57.7342 | 2026-09-22 15:40:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 84.2 |
| db21d480-fe3b-3e5e-b54e-f6124c2180a2 | -9.247 | -57.1488 | 2026-09-22 15:40:00 | GOES-19 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 137.8 |
| 38644949-8383-3cb6-a7ea-365bf41f8875 | 1.5287 | -55.7468 | 2026-09-22 15:40:00 | GOES-19 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 81.2 |
| dc27b466-8042-360f-9b3c-5f3c6944f50a | -3.6448 | -58.9031 | 2026-09-22 15:40:00 | GOES-19 | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | 63.0 |
| 70ca17e9-e039-35ed-88bd-4caca4708dff | -3.6813 | -58.9216 | 2026-09-22 15:40:00 | GOES-19 | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | 69.6 |
| 7fcb1e21-f8ff-3477-9bc6-dfed70840454 | -7.6942 | -61.5473 | 2026-09-22 15:40:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 63.8 |
| b38ff8ab-a911-39d5-adb8-f757607dd9d5 | -2.4023 | -58.2715 | 2026-09-22 15:40:00 | GOES-19 | ITAPIRANGA | AMAZONAS | Brasil | 1302009 | 13 | 33 | nan | nan | nan | Amazônia | 46.6 |
| 954eb88c-c380-3207-af1d-4d61a2949152 | 1.5282 | -56.0424 | 2026-09-22 15:40:00 | GOES-19 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 61.1 |
| 8f3801b8-ea89-35c1-8580-489b36d4b4a7 | 1.4453 | -50.7655 | 2026-09-22 15:40:00 | GOES-19 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 72.8 |
| 2744e00e-2b75-3458-b6f5-dd2ae81600b4 | 1.4269 | -50.7657 | 2026-09-22 15:40:00 | GOES-19 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 59.6 |
| effcb3ff-3628-3ba0-92dd-4ff4e629f962 | -10.3921 | -50.2488 | 2026-09-22 15:40:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 101.6 |
| 16192f29-dafa-3651-89d8-fe687b1753d1 | -4.2042 | -56.3412 | 2026-09-22 15:40:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 134.4 |
| 77ea7a77-fefd-3f1d-b115-f74d80721b0a | -11.9493 | -50.0971 | 2026-09-22 15:40:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 94.5 |
| eaf1e945-7b03-381d-9c8e-36cc0160e562 | -6.0926 | -57.6652 | 2026-09-22 15:40:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 118.7 |
| 6fca939f-c622-3948-b3fe-be8e940501ef | -7.5661 | -61.3239 | 2026-09-22 15:40:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 56.6 |
| dd147702-b60d-3306-b978-f34b986b3cc4 | -6.3383 | -59.9374 | 2026-09-22 15:40:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 43.0 |
| d0a4cf62-6706-3338-ab58-d8ac2184f264 | 2.4212 | -50.9765 | 2026-09-22 15:40:00 | GOES-19 | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 64.7 |
| 0958eac0-1d5f-340c-97dc-39c372f9cead | -3.523 | -56.9089 | 2026-09-22 15:40:00 | GOES-19 | BARREIRINHA | AMAZONAS | Brasil | 1300508 | 13 | 33 | nan | nan | nan | Amazônia | 42.0 |
| 58c40f68-eb76-3077-a30f-944c237c8325 | -11.0237 | -49.7304 | 2026-09-22 15:40:00 | GOES-19 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 89.6 |
| 8d4ae223-0d7c-3c16-afc1-6b82b3843440 | -3.0534 | -61.2767 | 2026-09-22 15:40:00 | GOES-19 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 78.9 |
| b25682ad-6c2d-37c1-9774-643ab6c0871e | 2.4028 | -50.9561 | 2026-09-22 15:40:00 | GOES-19 | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 62.9 |
| 2db69054-87d3-3f42-8053-f80f9226bf72 | -2.6783 | -57.5893 | 2026-09-22 15:40:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 67.7 |
| d0f6a4f4-820c-3578-9669-7cc6853ff0d4 | 4.0579 | -61.4095 | 2026-09-22 15:40:00 | GOES-19 | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 54.0 |
| 9178e12b-cf32-3722-b53d-49993c844fa6 | -8.1686 | -54.7634 | 2026-09-22 15:40:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 60.8 |
| d4ca2e73-5e61-382c-9466-d7c40cd0311e | 3.9717 | -59.7202 | 2026-09-22 15:40:00 | GOES-19 | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 57.8 |
| f2d0e4a7-bebb-39bf-adfe-48480a1c68f3 | -10.3916 | -50.2916 | 2026-09-22 15:40:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 91.3 |
| eed3494a-e8b9-3557-8130-1b7791f05ed8 | -10.5425 | -43.9649 | 2026-09-22 15:40:00 | GOES-19 | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 113.9 |
| 6385da36-76c4-3e0b-b5a1-9a30b41a2d3d | -6.1839 | -47.5039 | 2026-09-22 15:40:00 | GOES-19 | TOCANTINÓPOLIS | TOCANTINS | Brasil | 1721208 | 17 | 33 | nan | nan | nan | Cerrado | 66.2 |
| 00b441a8-c9ce-3629-8c7a-b91fc2d2d726 | -3.331 | -59.8483 | 2026-09-22 15:40:00 | GOES-19 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 71.7 |
| b7a82ea4-d4cb-3356-b891-7ebdb8e39471 | -6.5953 | -45.4727 | 2026-09-22 15:40:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 105.5 |
| de317304-64c4-3f24-a5b7-db3216fe52ad | 0.884 | -60.5616 | 2026-09-22 15:40:00 | GOES-19 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 50.3 |
| 43dc71c4-3211-38b2-ac16-8329eced7227 | -3.4215 | -60.1896 | 2026-09-22 15:40:00 | GOES-19 | CAREIRO | AMAZONAS | Brasil | 1301100 | 13 | 33 | nan | nan | nan | Amazônia | 69.6 |
| b2074346-0bca-3d80-a5e0-dbc764f41c27 | -3.132 | -59.029 | 2026-09-22 15:40:00 | GOES-19 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 136.8 |
| 101b7905-39cb-3c3a-8279-1027770146d7 | -3.5136 | -59.9401 | 2026-09-22 15:40:00 | GOES-19 | CAREIRO | AMAZONAS | Brasil | 1301100 | 13 | 33 | nan | nan | nan | Amazônia | 49.3 |


[Clique aqui para ver as próximas entradas](README153.md)
