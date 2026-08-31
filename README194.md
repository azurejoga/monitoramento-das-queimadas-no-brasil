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

## Dados Diários - Página 194

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 439212e8-2c4d-3884-8880-64579e7a3146 | -6.9521 | -58.9506 | 2026-08-31 19:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 55.6 |
| eedf02ab-f915-3540-99b1-d789b6e81879 | -13.967 | -54.395 | 2026-08-31 19:10:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 56.1 |
| 25f06079-cda6-3890-aa53-8229860616bd | -7.6804 | -55.3555 | 2026-08-31 19:10:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 59.9 |
| 94f6a673-72d5-3ecd-85f1-6422f1b1dfe3 | -13.5729 | -55.1382 | 2026-08-31 19:10:00 | GOES-19 | SORRISO | MATO GROSSO | Brasil | 5107925 | 51 | 33 | nan | nan | nan | Cerrado | 101.1 |
| 5b2d8ad2-d337-368a-b967-226dd763169b | -6.8568 | -59.4757 | 2026-08-31 19:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 73.7 |
| 4d9005a5-c080-3e04-ad49-4934696a7ff8 | -9.4719 | -57.0354 | 2026-08-31 19:10:00 | GOES-19 | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 116.4 |
| 3af420d2-2a4a-30c2-990b-9d037ca3c0d4 | -11.2103 | -45.1017 | 2026-08-31 19:10:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 213.8 |
| d38cc3a2-86c0-3f74-8b6b-b33e4fe72a8a | -10.0353 | -48.6908 | 2026-08-31 19:10:00 | GOES-19 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 64.0 |
| 6bb762b6-06c5-33d7-a380-403195e1b48b | -15.6333 | -56.4081 | 2026-08-31 19:10:00 | GOES-19 | NOSSA SENHORA DO LIVRAMENTO | MATO GROSSO | Brasil | 5106109 | 51 | 33 | nan | nan | nan | Cerrado | 84.7 |
| ea89084b-9fb7-324b-8560-f472b4353a49 | -11.2482 | -45.1194 | 2026-08-31 19:10:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 66.1 |
| 145975a9-8de1-382d-adea-909c1a784680 | -6.8571 | -59.4179 | 2026-08-31 19:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 51.1 |
| 79d1dba7-5e86-36e1-96bb-10609334ebf9 | -9.6683 | -50.8511 | 2026-08-31 19:10:00 | GOES-19 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 70.1 |
| 004f7fe2-69e0-3793-b2f4-9794cb2806bd | -14.1456 | -52.8082 | 2026-08-31 19:10:00 | GOES-19 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 72.1 |
| e2a10ae9-5f6a-341b-bfdd-27b2f06e577a | -9.694 | -65.0958 | 2026-08-31 19:10:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 52.7 |
| bde1aa2d-9ac6-367e-9f04-ab0436881eaf | -5.9635 | -57.6899 | 2026-08-31 19:10:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 115.1 |
| 9e955971-0875-3104-9151-42518aeba013 | -6.6765 | -58.7492 | 2026-08-31 19:10:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 61.4 |
| 89757dad-ef3e-3aec-8671-ad15d124f8f1 | -17.9059 | -52.0955 | 2026-08-31 19:10:00 | GOES-19 | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | 75.7 |
| fd2c89d1-7aac-3d8a-a234-3fe2ef553c0c | -7.0517 | -52.7187 | 2026-08-31 19:10:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 180.8 |
| 031c415b-f0fa-3c3e-bb50-8aba69b2a5cb | -11.2503 | -54.0146 | 2026-08-31 19:10:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 47.4 |
| d1942751-0e13-3e32-801c-62bb1b0e4a16 | -3.1998 | -61.161 | 2026-08-31 19:10:00 | GOES-19 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 64.9 |
| cf70c40c-ed39-3a90-aafc-9be4df481455 | -15.2278 | -56.3512 | 2026-08-31 19:10:00 | GOES-19 | ACORIZAL | MATO GROSSO | Brasil | 5100102 | 51 | 33 | nan | nan | nan | Cerrado | 90.7 |
| 85309e59-25b0-3e68-aad4-8b81d527c972 | -7.3453 | -72.9539 | 2026-08-31 19:10:00 | GOES-19 | GUAJARÁ | AMAZONAS | Brasil | 1301654 | 13 | 33 | nan | nan | nan | Amazônia | 79.9 |
| 830e2c8b-6313-3e3e-974a-a5b3884be5bb | -12.9054 | -59.8857 | 2026-08-31 19:10:00 | GOES-19 | COMODORO | MATO GROSSO | Brasil | 5103304 | 51 | 33 | nan | nan | nan | Cerrado | 68.1 |
| 060a6325-c8d2-3d3b-a1e2-32e3d9f785bc | -8.3785 | -70.8456 | 2026-08-31 19:10:00 | GOES-19 | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 76.7 |
| c9681d3e-9f28-3305-bd2a-6f9872bc9e9f | -10.9672 | -48.4111 | 2026-08-31 19:10:00 | GOES-19 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 235.8 |
| 1a8e44df-3586-3ad3-94f0-c1857441f291 | -9.173 | -59.3659 | 2026-08-31 19:10:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 66.2 |
| ac65c1ae-f38a-3746-98f8-ac088f98d1af | -7.9172 | -61.329 | 2026-08-31 19:10:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 102.8 |
| ac8d9fa6-3c65-3c99-b155-a23aaa9ebfe7 | -3.6399 | -60.5466 | 2026-08-31 19:10:00 | GOES-19 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 72.0 |
| 549165ef-a2c3-3bd2-9403-28201cbb7a1d | -7.0293 | -55.6312 | 2026-08-31 19:10:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 62.3 |
| c59cd6f6-5312-3b31-96d4-5983a3258273 | -4.5963 | -42.9266 | 2026-08-31 19:10:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 111.2 |
| 587586bf-910e-3146-bd84-bf8c61e2030a | -6.2537 | -55.4308 | 2026-08-31 19:10:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 59.0 |
| 12cefd53-2140-3c0b-940e-344c83f408ce | -11.1807 | -55.1024 | 2026-08-31 19:10:00 | GOES-19 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 64.3 |
| 57edaebb-659a-3fd6-8b9c-92613ace9326 | -14.9863 | -48.1304 | 2026-08-31 19:10:00 | GOES-19 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 87.3 |
| 3d9545fa-c30c-3699-a862-a16c0665dfda | -4.2275 | -59.8671 | 2026-08-31 19:10:00 | GOES-19 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 70.5 |
| 7a5cff90-8ac9-345b-84ae-414a3104dd62 | -20.2982 | -47.8378 | 2026-08-31 19:10:00 | GOES-19 | ITUVERAVA | SÃO PAULO | Brasil | 3524105 | 35 | 33 | nan | nan | nan | Cerrado | 101.8 |
| 2fd32ce5-22f2-3dba-a257-fbf95bd72b30 | -3.1839 | -60.1559 | 2026-08-31 19:10:00 | GOES-19 | IRANDUBA | AMAZONAS | Brasil | 1301852 | 13 | 33 | nan | nan | nan | Amazônia | 81.6 |
| 0840a7c4-6951-3720-9f9c-19d974011e4a | -8.6674 | -62.8179 | 2026-08-31 19:10:00 | GOES-19 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 56.4 |
| b90546fb-b570-338d-935e-cecae344ac43 | -8.8521 | -66.7641 | 2026-08-31 19:10:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 97.7 |
| c6842c0f-a90e-3dc1-8ff0-d5e25da9790d | -6.4054 | -49.9441 | 2026-08-31 19:10:00 | GOES-19 | CANAÃ DOS CARAJÁS | PARÁ | Brasil | 1502152 | 15 | 33 | nan | nan | nan | Amazônia | 125.3 |
| 5d6ff56a-932c-31e3-841e-3ec2f26982ad | -3.218 | -61.1796 | 2026-08-31 19:10:00 | GOES-19 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 51.8 |
| 2772c5df-08bd-328a-a4b7-aa1fc95154f5 | -5.2548 | -55.8907 | 2026-08-31 19:10:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 50.8 |
| 4c2b2a37-b648-3618-acf3-19326a26e6e4 | -11.1809 | -55.0821 | 2026-08-31 19:10:00 | GOES-19 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 70.3 |
| eb033967-0deb-3b52-90a7-d04a3e6fb28e | -9.9708 | -53.9419 | 2026-08-31 19:10:00 | GOES-19 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 90.2 |
| 5c461168-f87c-3c30-b991-05d907b4920a | -11.0933 | -51.5345 | 2026-08-31 19:10:00 | GOES-19 | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Cerrado | 115.3 |
| 16200b9b-63b9-3f99-a4d7-b305872a8e8d | -10.4961 | -59.6195 | 2026-08-31 19:10:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 45.6 |
| af35873d-f146-38f9-86cf-0b020c279264 | -8.499 | -55.3051 | 2026-08-31 19:10:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 68.7 |
| d48991e1-c6c0-3791-a844-8e0bc49d1947 | -3.9707 | -60.0258 | 2026-08-31 19:10:00 | GOES-19 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 47.2 |
| c46c046a-dbe3-3d84-bc52-5df85b54d027 | -10.8444 | -45.3126 | 2026-08-31 19:10:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 152.9 |
| c2c84bae-b884-38e1-a291-b4bd6a1a8fe5 | -9.153 | -59.5415 | 2026-08-31 19:10:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 148.6 |
| 1b2e55ea-1bb9-3e17-b44c-3cb089e0b6b7 | -7.685 | -63.3255 | 2026-08-31 19:10:00 | GOES-19 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 51.6 |
| 5e9962c9-54b2-35e7-8f06-e7e6a6e598b8 | -3.6076 | -59.0769 | 2026-08-31 19:10:00 | GOES-19 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 73.5 |
| 376bcc2f-1600-3df8-88aa-9671f70af3a8 | -6.3875 | -54.7646 | 2026-08-31 19:10:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 112.3 |
| 94e29ff3-a8e8-3799-9984-aaf5b6ca9ad4 | -7.905 | -44.2346 | 2026-08-31 19:10:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 50.4 |
| 6a09d5c6-e014-3c96-af97-dba8fc9c4bd0 | -5.8537 | -57.5576 | 2026-08-31 19:10:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 57.3 |
| 29263b4e-11d2-3b89-9468-3d8d4dfe0834 | -3.6216 | -60.547 | 2026-08-31 19:10:00 | GOES-19 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 121.4 |
| 221d4130-d615-39b5-a8e9-bf0945de7dd1 | -19.1543 | -57.377 | 2026-08-31 19:10:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 141.7 |
| f6f241ff-fa99-3781-ac20-0135c96599cb | -8.8706 | -66.7636 | 2026-08-31 19:10:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 199.4 |
| 207a433b-5c16-3e55-8e67-c7bc211b8dc5 | -6.3433 | -55.864 | 2026-08-31 19:10:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 53.9 |
| a442f062-1741-3534-9680-61387212bd4f | -10.11 | -50.33 | 2026-08-31 19:15:00 | MSG-03 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 185ba1c3-c038-3537-9b23-dbd486ff2db5 | -19.98 | -47.84 | 2026-08-31 19:15:00 | MSG-03 | DELTA | MINAS GERAIS | Brasil | 3121258 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 5f98e329-414d-3f8c-9dc6-f260109e697e | -17.91 | -50.53 | 2026-08-31 19:15:00 | MSG-03 | SANTA HELENA DE GOIÁS | GOIÁS | Brasil | 5219308 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 9b3a809e-1e9d-3788-b9ab-86e7838a58c1 | -3.87 | -44.07 | 2026-08-31 19:15:00 | MSG-03 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| a1246579-8885-3357-bdd8-2a4f6762cd97 | -10.14 | -50.34 | 2026-08-31 19:15:00 | MSG-03 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 8b5143a7-5a31-3d5d-a938-a6de014b0d7f | -10.01 | -44.72 | 2026-08-31 19:15:00 | MSG-03 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 055c07b4-a390-3f3f-bf6c-3578503b7ddf | -11.1 | -51.52 | 2026-08-31 19:15:00 | MSG-03 | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 7bb876c8-e805-3d2f-b04e-0cf90eb089d9 | -3.84 | -44.07 | 2026-08-31 19:15:00 | MSG-03 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| b02e3177-038d-321e-937c-d5b47ea4e86c | -10.12 | -45.88 | 2026-08-31 19:15:00 | MSG-03 | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 80fbbb1c-5de9-3a0d-8cbc-f3fc139e6fb4 | -17.88 | -50.51 | 2026-08-31 19:15:00 | MSG-03 | SANTA HELENA DE GOIÁS | GOIÁS | Brasil | 5219308 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 70bf9e79-5e9f-380f-8315-fee8989b8798 | -18.26 | -52.71 | 2026-08-31 19:15:00 | MSG-03 | CHAPADÃO DO CÉU | GOIÁS | Brasil | 5205471 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 72fcc1d8-fbf5-3e1b-8e5c-e59e489bc112 | -17.32 | -42.7 | 2026-08-31 19:15:00 | MSG-03 | TURMALINA | MINAS GERAIS | Brasil | 3169703 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 7177064a-a523-3992-b7ee-a5088d2a6def | -17.85 | -50.44 | 2026-08-31 19:15:00 | MSG-03 | SANTA HELENA DE GOIÁS | GOIÁS | Brasil | 5219308 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 6d13e4c6-ec3c-362f-a2ad-bbed428338d4 | -19.95 | -47.83 | 2026-08-31 19:15:00 | MSG-03 | DELTA | MINAS GERAIS | Brasil | 3121258 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 585cfb34-eb89-3ada-beb2-ac3a170daf89 | -17.88 | -50.45 | 2026-08-31 19:15:00 | MSG-03 | SANTA HELENA DE GOIÁS | GOIÁS | Brasil | 5219308 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 45e63058-f575-3ede-83f1-4d3349677ebd | -10.12 | -45.83 | 2026-08-31 19:15:00 | MSG-03 | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 4930651e-800a-34fa-b96f-bd3fb7c9007e | -17.85 | -50.49 | 2026-08-31 19:15:00 | MSG-03 | SANTA HELENA DE GOIÁS | GOIÁS | Brasil | 5219308 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 96c87d6f-a9e1-31b0-a3ad-3c2ae7d3abd5 | -19.89 | -47.9 | 2026-08-31 19:15:00 | MSG-03 | UBERABA | MINAS GERAIS | Brasil | 3170107 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| b6888865-86ef-3315-b7a8-225feaaf9dcc | -3.87 | -44.12 | 2026-08-31 19:15:00 | MSG-03 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 0f8710ca-66d7-3da9-b14b-3f8abe5b8d34 | -17.32 | -42.74 | 2026-08-31 19:15:00 | MSG-03 | TURMALINA | MINAS GERAIS | Brasil | 3169703 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| d06a29f8-1dac-31fb-9811-3657cedf3c28 | -10.12 | -45.92 | 2026-08-31 19:15:00 | MSG-03 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| f8922029-f800-3bb0-a1bf-b18c34bb283c | -7.6251 | -55.2987 | 2026-08-31 19:20:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 304.8 |
| d9ef736c-1960-35e2-bb68-74d91857413e | -6.1109 | -57.684 | 2026-08-31 19:20:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 56.2 |
| bdba5f2e-bb32-3347-87f5-d7b60294c00e | -5.5831 | -45.7501 | 2026-08-31 19:20:00 | GOES-19 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 63.4 |
| ae59ade5-d069-3d40-b506-3dd4e8c6155b | -15.015 | -52.7599 | 2026-08-31 19:20:00 | GOES-19 | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | 88.3 |
| 51dc3c2c-c9ad-396b-8570-1fb6506ea30c | -10.1134 | -45.8621 | 2026-08-31 19:20:00 | GOES-19 | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 222.6 |
| 03603d79-a264-3d22-8b78-a4117baac104 | -6.7834 | -59.4016 | 2026-08-31 19:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 62.5 |
| 3ee546be-5551-3671-ad8e-3528e5eef891 | -15.8649 | -56.4841 | 2026-08-31 19:20:00 | GOES-19 | NOSSA SENHORA DO LIVRAMENTO | MATO GROSSO | Brasil | 5106109 | 51 | 33 | nan | nan | nan | Cerrado | 85.6 |
| dbb612dd-f4c9-3a5a-9357-e9549a5217ec | -7.4734 | -61.4037 | 2026-08-31 19:20:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 65.7 |
| bc2643c1-b384-3e0d-ad8a-cfe001e85727 | -10.8043 | -50.5259 | 2026-08-31 19:20:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 67.1 |
| 702c752f-82a5-3bd2-8fe7-6503b87d432c | -6.3433 | -55.864 | 2026-08-31 19:20:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 77.6 |
| 4238eb91-86e3-3b55-a19e-95f195847732 | -6.3844 | -55.2251 | 2026-08-31 19:20:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 55.4 |
| 7c760209-8034-38c7-9145-3dd695066cf8 | -10.8631 | -45.333 | 2026-08-31 19:20:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 128.0 |
| 318e39c4-8857-3ae2-8eb1-4e9d89c6b19e | -9.6049 | -68.5979 | 2026-08-31 19:20:00 | GOES-19 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 64.7 |
| 74e96b1c-8a11-3bd6-9552-6a423cb82f7c | -8.9428 | -63.2797 | 2026-08-31 19:20:00 | GOES-19 | ITAPUÃ DO OESTE | RONDÔNIA | Brasil | 1101104 | 11 | 33 | nan | nan | nan | Amazônia | 53.6 |
| 624584f6-12ec-3268-bb75-be14ede52748 | -8.5363 | -67.1617 | 2026-08-31 19:20:00 | GOES-19 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 104.5 |
| 10ddd1a3-1e98-34cb-a4e1-5adc99b078b3 | -11.1807 | -55.1024 | 2026-08-31 19:20:00 | GOES-19 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 64.9 |
| 2fb47f78-6a77-3b07-99c7-6916856973be | -6.6765 | -58.7492 | 2026-08-31 19:20:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 73.6 |
| 9ab19d74-1b48-3cab-9c24-75d6aac102e2 | -7.6805 | -55.3355 | 2026-08-31 19:20:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 116.2 |
| 18730311-941e-3232-887c-ac5d06fc20a8 | -13.471 | -57.0373 | 2026-08-31 19:20:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Cerrado | 105.9 |
| 14bdb562-4a78-3b39-b18f-3453a9313212 | -5.2362 | -55.9112 | 2026-08-31 19:20:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 49.4 |
| 6449d870-97da-3e48-b359-79d444d1a043 | -2.8568 | -43.5029 | 2026-08-31 19:20:00 | GOES-19 | HUMBERTO DE CAMPOS | MARANHÃO | Brasil | 2105005 | 21 | 33 | nan | nan | nan | Cerrado | 62.8 |


[Clique aqui para ver as próximas entradas](README195.md)
