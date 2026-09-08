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

## Dados Diários - Página 12

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| c3a06d8f-cf9e-3cfa-9b6e-ea8c928c566f | -9.76475 | -43.46069 | 2026-09-08 04:08:00 | NOAA-21 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 10d36fd6-7c43-380b-b04b-20597a87a19b | -6.75704 | -45.48663 | 2026-09-08 04:08:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 65dee228-d0b6-3fb1-b8a7-da545b57a7ac | -14.25218 | -43.71627 | 2026-09-08 04:10:00 | NOAA-21 | MALHADA | BAHIA | Brasil | 2920205 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| f0a02262-5be1-39d9-a77a-1dc8ee2abd37 | -9.96045 | -45.39497 | 2026-09-08 04:10:00 | NOAA-21 | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| aed2a6e5-41fc-3a83-acca-7fc6b23eae79 | -13.43128 | -43.80944 | 2026-09-08 04:10:00 | NOAA-21 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 28e290bf-b12b-364f-baa4-90f130e948b3 | -13.43734 | -43.81408 | 2026-09-08 04:10:00 | NOAA-21 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 6.8 |
| e451a071-735c-3382-b83f-1c0e3f92d992 | -10.7127 | -45.90164 | 2026-09-08 04:10:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| bdc80003-db95-3213-836b-f8943a5b9964 | -11.13092 | -41.85541 | 2026-09-08 04:10:00 | NOAA-21 | SÃO GABRIEL | BAHIA | Brasil | 2929255 | 29 | 33 | nan | nan | nan | Caatinga | 8.3 |
| a0c248b3-9f50-3bd3-9072-a6f4d98ea16a | -11.36672 | -45.74028 | 2026-09-08 04:10:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 774fe3ec-dad3-31b6-ac29-0fd3c0a10928 | -14.25274 | -43.71272 | 2026-09-08 04:10:00 | NOAA-21 | MALHADA | BAHIA | Brasil | 2920205 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| c66a8032-4541-3460-a92f-360b6f40872e | -11.35028 | -45.72916 | 2026-09-08 04:10:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| bcc7cb1c-34e0-3310-a684-d6fa76908e85 | -11.65933 | -39.8385 | 2026-09-08 04:10:00 | NOAA-21 | CAPELA DO ALTO ALEGRE | BAHIA | Brasil | 2906857 | 29 | 33 | nan | nan | nan | Caatinga | 1.1 |
| c345fcdd-6922-3d48-9cd9-3cd5889619be | -11.31562 | -45.06262 | 2026-09-08 04:10:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 4302bb64-38f6-3fc8-902f-a5d14ba96042 | -10.71202 | -45.90577 | 2026-09-08 04:10:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 483f3deb-1aa8-3e00-b826-fc9a9e53a58a | -11.34672 | -45.72858 | 2026-09-08 04:10:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 52c890ea-f279-3e66-bf7a-1b815aaeac09 | -14.69046 | -55.17402 | 2026-09-08 04:10:00 | NOAA-21 | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 3a0d5c04-be91-3aa9-89cc-b6d0f4e0c40b | -12.94773 | -44.72834 | 2026-09-08 04:10:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| abd63b16-5490-3814-9aa5-98968d3241c8 | -13.24848 | -45.10728 | 2026-09-08 04:10:00 | NOAA-21 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 06dcb36f-9602-3731-9c22-aecb0ffafbd0 | -14.28137 | -42.69316 | 2026-09-08 04:10:00 | NOAA-21 | GUANAMBI | BAHIA | Brasil | 2911709 | 29 | 33 | nan | nan | nan | Caatinga | 4.1 |
| d6304c0c-1160-3110-b9c5-9620eb204fd7 | -11.37028 | -45.74087 | 2026-09-08 04:10:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 45c04397-a036-3580-b142-b89cbc233eab | -11.9395 | -49.74495 | 2026-09-08 04:10:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 16a25895-b916-32fb-88ef-80abee96ab66 | -14.68948 | -55.1787 | 2026-09-08 04:10:00 | NOAA-21 | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 55f2b0c1-c3e1-32b3-a1bd-4d1c89d0444d | -15.64488 | -54.1806 | 2026-09-08 04:10:00 | NOAA-21 | PRIMAVERA DO LESTE | MATO GROSSO | Brasil | 5107040 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 12dc54cf-574d-3e22-9952-9a56b407a28c | -14.2847 | -42.69365 | 2026-09-08 04:10:00 | NOAA-21 | GUANAMBI | BAHIA | Brasil | 2911709 | 29 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 8b606485-e771-37b7-80a7-5917e0fb0bf9 | -11.31497 | -45.06654 | 2026-09-08 04:10:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| ee82267d-3eb7-368f-b241-14f543b05c86 | -15.63928 | -54.1795 | 2026-09-08 04:10:00 | NOAA-21 | PRIMAVERA DO LESTE | MATO GROSSO | Brasil | 5107040 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 7f2a75fa-0a42-3cde-9783-f52af7d82c34 | -12.94435 | -44.72778 | 2026-09-08 04:10:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 8de5bc30-7986-3f2b-9aaf-b096af8e170e | -13.86105 | -43.62945 | 2026-09-08 04:10:00 | NOAA-21 | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 0fd16580-585e-3278-806d-62452bd8f58f | -12.37781 | -43.43681 | 2026-09-08 04:10:00 | NOAA-21 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 428869b4-d9c8-33ed-9f1e-957313391963 | -9.87127 | -46.68993 | 2026-09-08 04:10:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 7e414406-39ca-3d95-9395-c5632c10c5d6 | -11.65837 | -39.83666 | 2026-09-08 04:10:00 | NOAA-21 | CAPELA DO ALTO ALEGRE | BAHIA | Brasil | 2906857 | 29 | 33 | nan | nan | nan | Caatinga | 1.0 |
| c78502ba-cf70-3f2e-b074-dc221371dd00 | -10.24472 | -45.21214 | 2026-09-08 04:10:00 | NOAA-21 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 42695332-da99-378f-afa5-d2911ee8a118 | -12.73263 | -44.84093 | 2026-09-08 04:10:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 559cacd6-bc13-36d5-8165-aceadc85d264 | -13.4274 | -43.81245 | 2026-09-08 04:10:00 | NOAA-21 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 9ce9ab93-7172-3a39-a810-cdd99e8b4e98 | -13.43403 | -43.81354 | 2026-09-08 04:10:00 | NOAA-21 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 008b5ac9-8aa1-36f5-b580-cd992e8fdcbe | -13.43459 | -43.80999 | 2026-09-08 04:10:00 | NOAA-21 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 6d7e0113-ac7b-38ad-9634-f1b979e87f57 | -11.3674 | -45.73613 | 2026-09-08 04:10:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 5f9d91c6-932c-3ba8-9dc8-99f0aad13bfd | -9.95258 | -48.17174 | 2026-09-08 04:10:00 | NOAA-21 | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 8739f63a-2fa4-3d14-9be1-038e77fa6780 | -11.36316 | -45.73969 | 2026-09-08 04:10:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 11290ff1-480a-31ae-9f5a-4219c57e77b9 | -14.69143 | -55.1694 | 2026-09-08 04:10:00 | NOAA-21 | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 5.5 |
| a92559bf-291e-3b2f-8f9e-f57e8d312a63 | -13.40172 | -44.14456 | 2026-09-08 04:10:00 | NOAA-21 | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| a84b982f-c54b-3d61-a58f-806e3a5f9003 | -13.44066 | -43.81461 | 2026-09-08 04:10:00 | NOAA-21 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 19ca3854-6282-31fc-a656-ac9d7dc52924 | -13.42796 | -43.8089 | 2026-09-08 04:10:00 | NOAA-21 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 0aa48855-3189-3d62-94e5-638d681aa003 | -10.48959 | -43.5452 | 2026-09-08 04:10:00 | NOAA-21 | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 761beda1-1efd-3e49-a72e-f1188e99c467 | -13.25188 | -45.10784 | 2026-09-08 04:10:00 | NOAA-21 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 37049397-2117-3a14-af2f-b83ba844608c | -13.87259 | -43.66403 | 2026-09-08 04:10:00 | NOAA-21 | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| b96ff751-37fa-3837-bf5e-bca66ea2c7f0 | -15.05402 | -41.32861 | 2026-09-08 04:10:00 | NOAA-21 | TREMEDAL | BAHIA | Brasil | 2931806 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 2324f29d-1a8a-3514-a371-dbf6a3c73481 | -11.18971 | -40.18108 | 2026-09-08 04:10:00 | NOAA-21 | JACOBINA | BAHIA | Brasil | 2917508 | 29 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 8c5d5fe4-b117-3d65-92c8-dbe29e5f67f4 | -13.43072 | -43.81299 | 2026-09-08 04:10:00 | NOAA-21 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 399a2878-fe4a-3323-b187-9a37f6e63051 | -13.68904 | -43.61963 | 2026-09-08 04:10:00 | NOAA-21 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| f67e813d-a427-3d05-8b64-b652d131cddb | -11.93502 | -49.74412 | 2026-09-08 04:10:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| f27f78f0-61c2-3cfe-b77c-5d18651fe197 | -13.41319 | -44.17955 | 2026-09-08 04:10:00 | NOAA-21 | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 8692c393-2fa1-389f-b849-e82e62136f9b | -11.36164 | -45.72675 | 2026-09-08 04:10:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| b2c8034c-f307-3897-b6e2-23ddad636282 | -12.74599 | -44.73641 | 2026-09-08 04:10:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 8284f399-fd3d-31a7-b456-082b3055337c | -11.36959 | -45.74504 | 2026-09-08 04:10:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 95880881-8737-3a33-8f4c-b4090bc28a71 | -11.3652 | -45.72733 | 2026-09-08 04:10:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| a95e45d4-236d-3b89-a257-bb9402e7c0d8 | -11.94482 | -49.7412 | 2026-09-08 04:10:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| a9725b62-4257-3d7f-8648-07126459ba8a | -11.34317 | -45.728 | 2026-09-08 04:10:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| e6f84ee0-bffa-3f7c-816b-1ac640a90b28 | -11.27611 | -45.69614 | 2026-09-08 04:10:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 89566980-247e-37cc-8bf0-f27c6a55b1fa | -11.9493 | -49.74202 | 2026-09-08 04:10:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| ff28a605-4fff-3d89-9665-a0a1885c964f | -21.97965 | -56.04914 | 2026-09-08 04:12:00 | NOAA-21 | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 921f5676-d234-34f0-a393-a20f3121e406 | -18.69639 | -47.49721 | 2026-09-08 04:12:00 | NOAA-21 | MONTE CARMELO | MINAS GERAIS | Brasil | 3143104 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| d4e217ba-c93e-32b6-be7d-147f972466ad | -15.83706 | -56.6093 | 2026-09-08 04:12:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| e46e3441-9db8-32bc-8b82-011d8818752a | -18.33731 | -49.22106 | 2026-09-08 04:12:00 | NOAA-21 | ITUMBIARA | GOIÁS | Brasil | 5211503 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| fee41ad7-5959-3ee4-829f-7b807665b409 | -17.09924 | -56.87334 | 2026-09-08 04:12:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.1 |
| f48e46e6-e746-3970-b3f4-8e3906534605 | -17.09288 | -56.87183 | 2026-09-08 04:12:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.1 |
| b81da232-f93e-35cc-ab1a-93263e59c6a2 | -18.7714 | -49.43448 | 2026-09-08 04:12:00 | NOAA-21 | CAPINÓPOLIS | MINAS GERAIS | Brasil | 3112604 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 22099dac-d37f-3d9f-afd5-ef4669772b89 | -21.97246 | -56.05507 | 2026-09-08 04:12:00 | NOAA-21 | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 5668f226-45a6-3158-94cc-a7bb24d1f706 | -18.77829 | -49.44118 | 2026-09-08 04:12:00 | NOAA-21 | CAPINÓPOLIS | MINAS GERAIS | Brasil | 3112604 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 2ba82306-0810-3411-a995-bd2e18306223 | -15.83643 | -56.61044 | 2026-09-08 04:12:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 3cfb5a03-2948-331f-a4bc-601d09915394 | -21.44926 | -51.61978 | 2026-09-08 04:12:00 | NOAA-21 | DRACENA | SÃO PAULO | Brasil | 3514403 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| bc16bd66-a25a-39d5-9273-cadfa405cacf | -19.15026 | -49.21816 | 2026-09-08 04:12:00 | NOAA-21 | PRATA | MINAS GERAIS | Brasil | 3152808 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 78208e91-2a00-3cdf-b261-405538a1de48 | -21.97337 | -56.05107 | 2026-09-08 04:12:00 | NOAA-21 | PONTA PORÃ | MATO GROSSO DO SUL | Brasil | 5006606 | 50 | 33 | nan | nan | nan | Cerrado | 1.2 |
| ab8eda21-c5a7-380e-8363-ada8798d1c3d | -28.94253 | -50.82131 | 2026-09-08 04:14:00 | NOAA-21 | CAXIAS DO SUL | RIO GRANDE DO SUL | Brasil | 4305108 | 43 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 79ff1df8-2d3e-328f-9cb2-6b42b5a2f834 | -29.7335 | -51.08044 | 2026-09-08 04:14:00 | NOAA-21 | NOVO HAMBURGO | RIO GRANDE DO SUL | Brasil | 4313409 | 43 | 33 | nan | nan | nan | Pampa | 1.4 |
| 97adc913-6fa7-3533-868a-ddfde772eda9 | -3.26991 | -50.02412 | 2026-09-08 04:44:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 7f9c06c9-358b-3078-a48a-fc609ef48e19 | -3.65112 | -49.4007 | 2026-09-08 04:44:00 | NPP-375D | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 2dfda800-68ea-33a4-a86a-e83cb3919f52 | -2.96847 | -49.5619 | 2026-09-08 04:44:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 25c92b44-ca06-3e9f-bbf7-9c1305219e5d | -6.7649 | -45.49416 | 2026-09-08 04:44:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 4e75dddb-5c05-3504-8dfa-af3be6ccfe5c | -3.69899 | -58.9435 | 2026-09-08 04:44:00 | NPP-375D | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | 8.5 |
| 4218bcd7-3ea9-3ca9-aa46-e066721be907 | -4.36408 | -47.77507 | 2026-09-08 04:44:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| d5fb8283-b6d6-31e6-ae70-0fc81fecd353 | -4.82015 | -42.91563 | 2026-09-08 04:44:00 | NPP-375D | UNIÃO | PIAUÍ | Brasil | 2211100 | 22 | 33 | nan | nan | nan | Cerrado | 4.0 |
| b43a52dd-d819-3a57-8cf8-0ac95a7d259f | -5.03286 | -47.65697 | 2026-09-08 04:44:00 | NPP-375D | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 0.5 |
| e1cc0e58-ed41-3172-a4a3-d388a3507cb8 | -3.44447 | -53.04967 | 2026-09-08 04:44:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d6109f3e-d44c-3614-8ce3-3d27fdc3c9c9 | -2.55906 | -54.74769 | 2026-09-08 04:44:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| f1c48b8c-e591-358a-9a8a-6d901a6c117a | -7.79457 | -49.20084 | 2026-09-08 04:44:00 | NPP-375D | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 51418d61-65a4-342d-afb5-e6fa692c57c2 | -7.79514 | -49.1973 | 2026-09-08 04:44:00 | NPP-375D | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| fc5eb3ed-50b2-3eb5-9da6-5fa2e32cda45 | -3.0686 | -49.52197 | 2026-09-08 04:44:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 376347f2-d9bf-3e76-99de-fe72f91ea1d1 | -4.93298 | -42.87865 | 2026-09-08 04:44:00 | NPP-375D | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 7.4 |
| dd0b9600-3e31-3ea2-9f41-b7f73d594ecf | -4.36075 | -47.77454 | 2026-09-08 04:44:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 9d3a32b8-3876-3a91-9b99-a73af9fb4de6 | -4.04293 | -50.87756 | 2026-09-08 04:44:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 7ed357a8-0a7b-3ce1-8419-91bed98f0f61 | -6.33133 | -43.35511 | 2026-09-08 04:44:00 | NPP-375D | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 7.0 |
| c53cc26b-0d7a-3731-96a9-3edd039fb351 | -2.732 | -51.82591 | 2026-09-08 04:44:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| b19b35a6-2616-3779-bd52-01329d6467a8 | -4.57307 | -47.18085 | 2026-09-08 04:44:00 | NPP-375D | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d2739358-3f1a-3b03-9f5c-6b46632b6308 | -2.6377 | -46.77318 | 2026-09-08 04:44:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 60ada580-c311-377d-88b6-49445ca272f1 | -2.42823 | -48.63832 | 2026-09-08 04:44:00 | NPP-375D | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 4eaa247e-a400-3a89-82e0-b11de5d17e85 | -4.2756 | -48.66249 | 2026-09-08 04:44:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 5447de66-cf6c-35c2-8e5f-2cfa010693df | -7.69667 | -44.31266 | 2026-09-08 04:44:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 5f23d62e-866c-3ffd-86b5-4500a7a180d4 | -4.93549 | -42.87633 | 2026-09-08 04:44:00 | NPP-375D | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 12.1 |
| 9b641f2f-f44e-3c5c-ae07-596ce59be31b | -6.78381 | -48.66646 | 2026-09-08 04:44:00 | NPP-375D | ARAGOMINAS | TOCANTINS | Brasil | 1701309 | 17 | 33 | nan | nan | nan | Amazônia | 1.1 |


[Clique aqui para ver as próximas entradas](README13.md)
