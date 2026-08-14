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

## Dados Diários - Página 22

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 1ed6504a-3ff9-3a56-a709-cb7793246c02 | -14.49538 | -53.07557 | 2026-08-14 04:34:00 | NOAA-20 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 6fa13786-56ce-3fa1-ac80-1227aab0e76e | -14.45741 | -45.69844 | 2026-08-14 04:34:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 1cac516f-9c19-355a-88b4-21b78756f935 | -10.97768 | -50.53348 | 2026-08-14 04:34:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 4.9 |
| eb509fa3-0126-355f-a946-14fa083cb117 | -14.05942 | -53.61123 | 2026-08-14 04:34:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| ded978bf-8e42-396f-acb9-df7b5ac77e2a | -16.54431 | -39.6631 | 2026-08-14 04:34:00 | NOAA-20 | ITABELA | BAHIA | Brasil | 2914653 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 2bd41bb2-f48e-3522-8427-aabd14b6bdd1 | -13.28401 | -54.22992 | 2026-08-14 04:34:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 472f266f-6bdf-3115-b7d8-f3bc79cffb4b | -11.88568 | -50.24614 | 2026-08-14 04:34:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| ba11a866-a249-35f9-adde-82f1c457455d | -14.04318 | -53.58493 | 2026-08-14 04:34:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 4d23ecff-6e8b-38a6-b5ba-c0d36e0f7dcb | -14.06823 | -53.60913 | 2026-08-14 04:34:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 3.5 |
| a9cbaf68-6a8c-37b1-b59e-b4bff7c57706 | -16.91502 | -54.14658 | 2026-08-14 04:34:00 | NOAA-20 | PEDRA PRETA | MATO GROSSO | Brasil | 5106372 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| e43ac56d-2e35-3a6b-9a4a-9079f29ffa8d | -14.72181 | -52.8935 | 2026-08-14 04:34:00 | NOAA-20 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 1766ebeb-5cba-3061-b057-eaa34cbc8ac3 | -12.71143 | -48.44862 | 2026-08-14 04:34:00 | NOAA-20 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 15acf8d3-0f20-3b51-885b-bc04eb409c65 | -12.71313 | -48.43807 | 2026-08-14 04:34:00 | NOAA-20 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 11c97aac-8088-3c67-afe5-18d522ffbf37 | -13.20879 | -50.57895 | 2026-08-14 04:34:00 | NOAA-20 | SÃO MIGUEL DO ARAGUAIA | GOIÁS | Brasil | 5220207 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| ec140008-e35e-3fbb-b28f-223216354110 | -10.9734 | -50.537 | 2026-08-14 04:34:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 7.3 |
| ea5fceab-7e2a-32c9-9eab-5d7b735765dd | -14.71117 | -52.88621 | 2026-08-14 04:34:00 | NOAA-20 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| ae9a8a67-f585-3bf5-ae7c-0ace0a5d6d64 | -15.00776 | -41.94659 | 2026-08-14 04:34:00 | NOAA-20 | CORDEIROS | BAHIA | Brasil | 2909000 | 29 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 0f9de5da-7bd8-3910-8bb6-7cca9d39bf1b | -11.50665 | -54.61085 | 2026-08-14 04:34:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 89d0ba5b-ebc8-3902-9d67-f762aa03df3e | -14.30647 | -53.07291 | 2026-08-14 04:34:00 | NOAA-20 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 62d0780c-656b-3560-822a-d53a8934afb8 | -14.47444 | -45.68344 | 2026-08-14 04:34:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 3.1 |
| beda83a7-2bba-340c-aa02-31c2ce12a1b7 | -11.86264 | -51.95705 | 2026-08-14 04:34:00 | NOAA-20 | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b0314d99-0e04-388e-bf8c-72a11127ed70 | -13.68241 | -46.26786 | 2026-08-14 04:34:00 | NOAA-20 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 11.7 |
| 2c33b355-c486-3829-8def-37e4ca9d2ca9 | -13.24541 | -54.21129 | 2026-08-14 04:34:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 1206e3d3-c8bb-3129-91d7-298b1d14c5bb | -18.42454 | -45.20071 | 2026-08-14 04:34:00 | NOAA-20 | TRÊS MARIAS | MINAS GERAIS | Brasil | 3169356 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| e29f42fc-b172-3fa5-8c0a-8813c504b999 | -11.48959 | -54.62692 | 2026-08-14 04:34:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 8.2 |
| 23d5dce4-3aca-3b0a-9503-63bb71e61fe2 | -16.91171 | -54.14197 | 2026-08-14 04:34:00 | NOAA-20 | PEDRA PRETA | MATO GROSSO | Brasil | 5106372 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 16d89f69-addc-33a8-b03f-d816243ca2e7 | -14.05613 | -53.65247 | 2026-08-14 04:34:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| c1eef5a8-1d44-3edb-aefc-43cf32fc9b48 | -14.95632 | -46.61247 | 2026-08-14 04:34:00 | NOAA-20 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 7f053b4f-1165-3607-8ce6-625a43ca305b | -9.76728 | -60.76697 | 2026-08-14 04:34:00 | NOAA-20 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 50111aed-f827-3ae2-858f-5f831dfbc776 | -15.09448 | -48.65174 | 2026-08-14 04:34:00 | NOAA-20 | VILA PROPÍCIO | GOIÁS | Brasil | 5222302 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 48a5470e-da66-3a17-a01a-f8e605fd27d1 | -14.44628 | -45.70084 | 2026-08-14 04:34:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 092f57c3-4d79-3e20-b3a8-ba8a06451773 | -11.85882 | -51.95639 | 2026-08-14 04:34:00 | NOAA-20 | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 03e0c578-3792-3898-8086-5fad441b5319 | -15.13582 | -41.56578 | 2026-08-14 04:34:00 | NOAA-20 | TREMEDAL | BAHIA | Brasil | 2931806 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 195c8b99-29a4-3190-a23a-460c16a744f8 | -11.4714 | -54.6235 | 2026-08-14 04:34:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 73e2e4fe-b68b-315a-b24d-2b6669ef4474 | -14.4762 | -45.69607 | 2026-08-14 04:34:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| fd5bef54-ef46-3491-bf14-805e730d91d2 | -14.47034 | -45.68692 | 2026-08-14 04:34:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 5.2 |
| da2f15d4-71b6-3c87-8b67-17c94598ce54 | -14.46741 | -45.68234 | 2026-08-14 04:34:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 0f9b5167-a526-3875-8a00-0df8f06ebce0 | -11.495 | -54.6231 | 2026-08-14 04:34:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 8.2 |
| 2075b2c7-bf8a-3928-8e57-f53f644c5270 | -14.29711 | -45.2704 | 2026-08-14 04:34:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 65bae653-d3a4-37aa-a0b8-c1c975a57021 | -11.88219 | -50.24554 | 2026-08-14 04:34:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| f71a07dc-23f7-33c6-ac30-027726f71937 | -14.46255 | -51.92126 | 2026-08-14 04:34:00 | NOAA-20 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| ae437053-7294-3894-958b-3e7d9a010780 | -16.25281 | -53.70976 | 2026-08-14 04:34:00 | NOAA-20 | GUIRATINGA | MATO GROSSO | Brasil | 5104203 | 51 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 95104239-1063-3176-84ff-616529ec0ea1 | -12.51855 | -55.78236 | 2026-08-14 04:34:00 | NOAA-20 | SORRISO | MATO GROSSO | Brasil | 5107925 | 51 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 7cbabdf9-4e99-3b8f-a5c8-c730ef5e209b | -16.90637 | -54.14832 | 2026-08-14 04:34:00 | NOAA-20 | PEDRA PRETA | MATO GROSSO | Brasil | 5106372 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 490e413a-dbe7-351e-9896-3c91b0873c82 | -14.0303 | -53.58633 | 2026-08-14 04:34:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 509d5582-7a51-318d-9276-8562c991c12f | -14.08863 | -53.63616 | 2026-08-14 04:34:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| fe2f46d1-845f-3672-b5d6-44d17505dade | -11.47392 | -44.56202 | 2026-08-14 04:34:00 | NOAA-20 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| b282a3d3-6405-3164-af22-b9e72fb18ef5 | -13.561 | -46.2605 | 2026-08-14 04:34:00 | NOAA-20 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 6.4 |
| f89c3608-2314-3504-af6c-1c49c2f5f7ea | -14.46625 | -45.69041 | 2026-08-14 04:34:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 517c9367-2aff-3bb4-bb80-7c8a4a818ca7 | -13.28202 | -54.21672 | 2026-08-14 04:34:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 97bdb319-2da9-35da-9836-0736396d0293 | -13.23051 | -54.26913 | 2026-08-14 04:34:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 0c8cb4a7-dfee-36ac-abb2-564d5941f210 | -12.72081 | -48.45391 | 2026-08-14 04:34:00 | NOAA-20 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| b8d51c71-5363-3a04-9a7b-5f1a219e8c0d | -14.44337 | -45.69627 | 2026-08-14 04:34:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| f84fff18-541f-3888-bf12-9ef38f8efba3 | -10.70851 | -50.52087 | 2026-08-14 04:34:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| e5135e81-c37a-3f13-b1e6-f638850a0d31 | -10.82478 | -50.32424 | 2026-08-14 04:34:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 861a2404-64ed-3460-885d-8b48ca57b45f | -14.94724 | -46.62635 | 2026-08-14 04:34:00 | NOAA-20 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 195daf18-5478-3a98-98d7-a67f51981c3c | -9.76174 | -60.75896 | 2026-08-14 04:34:00 | NOAA-20 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 4e68ce19-a4d7-3cde-af5d-6838fa814895 | -13.56497 | -46.2573 | 2026-08-14 04:34:00 | NOAA-20 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 11.2 |
| 5e3d975e-77d8-3265-ac03-f4f1a1db3c79 | -13.24446 | -54.24119 | 2026-08-14 04:34:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 422e65f5-90e7-35d6-b190-c84848cef6bf | -14.95518 | -46.61996 | 2026-08-14 04:34:00 | NOAA-20 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| c018a600-955a-3a7a-82d9-8374aee3736d | -13.75204 | -53.41387 | 2026-08-14 04:34:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 70197da8-a170-3118-b36c-ce89af308780 | -18.16928 | -43.98278 | 2026-08-14 04:34:00 | NOAA-20 | AUGUSTO DE LIMA | MINAS GERAIS | Brasil | 3104809 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 6d2608ca-abed-3924-9bb6-5f2fc1624073 | -14.72445 | -52.87881 | 2026-08-14 04:34:00 | NOAA-20 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| c22e8191-63de-305a-b218-2f299135e363 | -11.46971 | -44.56564 | 2026-08-14 04:34:00 | NOAA-20 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| e2793824-ca85-32a6-b90a-a1292861d1f5 | -14.29946 | -45.26929 | 2026-08-14 04:34:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 6b3a8dc8-de86-34f0-aa7f-c83ae3f662a7 | -14.29063 | -51.96315 | 2026-08-14 04:34:00 | NOAA-20 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 13.5 |
| 0ef848e0-5ca8-300d-892f-008ed1a6994b | -13.56268 | -46.24934 | 2026-08-14 04:34:00 | NOAA-20 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 099217da-6dc2-3c0d-9b99-2d4471f2690b | -13.68527 | -46.27206 | 2026-08-14 04:34:00 | NOAA-20 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 38.7 |
| f7ae6336-35b5-3fd1-a7f8-97376e9c29b2 | -14.95413 | -46.60394 | 2026-08-14 04:34:00 | NOAA-20 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 8b136603-fc8e-33fa-98f5-49d40f0452be | -13.56156 | -46.25676 | 2026-08-14 04:34:00 | NOAA-20 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 11.2 |
| 5f386d96-eac0-3d0a-bc91-8f08af2108f9 | -14.23957 | -45.41397 | 2026-08-14 04:34:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 9b2c7929-f332-321f-924d-4e8669920937 | -14.29772 | -45.26625 | 2026-08-14 04:34:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| e27b8458-9fdd-3ddc-91aa-4a2675266772 | -14.03643 | -53.62168 | 2026-08-14 04:34:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 47191f37-1b17-3313-bc6e-6f6770f483ae | -14.44181 | -51.86714 | 2026-08-14 04:34:00 | NOAA-20 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| a20a0c9d-8004-3c74-b6a7-7ab2728a6bf8 | -14.9924 | -46.60559 | 2026-08-14 04:34:00 | NOAA-20 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 9921d3be-ec3e-34e9-b938-9e9b32c98111 | -16.87964 | -54.13541 | 2026-08-14 04:34:00 | NOAA-20 | PEDRA PRETA | MATO GROSSO | Brasil | 5106372 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| ca958dc6-0eda-3918-bda7-39355e5533b5 | -14.95807 | -46.62399 | 2026-08-14 04:34:00 | NOAA-20 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 4c31b242-22bc-3a90-89f5-712f40f702d4 | -14.08049 | -53.6345 | 2026-08-14 04:34:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 4.8 |
| bb514e4d-240e-3f65-b4e0-8fdfc20d05bf | -14.96602 | -46.61755 | 2026-08-14 04:34:00 | NOAA-20 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 70fcfed3-0788-3d3b-a99f-c44e0203b9bb | -13.74934 | -53.42869 | 2026-08-14 04:34:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| f5528650-1349-39b5-884c-3d58d01ca916 | -16.91432 | -54.15038 | 2026-08-14 04:34:00 | NOAA-20 | PEDRA PRETA | MATO GROSSO | Brasil | 5106372 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 2cef280e-2fd9-3fff-a33b-e73fa7ea3c7c | -14.94041 | -46.62541 | 2026-08-14 04:34:00 | NOAA-20 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 86245177-c83b-385e-9033-ed627119581b | -14.4727 | -52.01529 | 2026-08-14 04:34:00 | NOAA-20 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 735804cc-a362-358c-af12-c74d58334e7b | -11.49954 | -54.62401 | 2026-08-14 04:34:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 1e83d84f-0b57-3480-9528-1fff93ec91e5 | -13.92661 | -53.95499 | 2026-08-14 04:34:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 602c2340-a1d1-3e44-88ee-bc3b8e521c58 | -18.42451 | -45.20293 | 2026-08-14 04:34:00 | NOAA-20 | TRÊS MARIAS | MINAS GERAIS | Brasil | 3169356 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| d9ae95fd-c049-360e-8abc-805d635c4096 | -15.70039 | -48.32103 | 2026-08-14 04:34:00 | NOAA-20 | COCALZINHO DE GOIÁS | GOIÁS | Brasil | 5205513 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 7018441e-7f40-368f-aa34-50bd38407a78 | -15.17076 | -52.82044 | 2026-08-14 04:34:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 507172d4-f70a-3bfe-b480-cfb151fe5f68 | -14.05533 | -53.58753 | 2026-08-14 04:34:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 916cfbad-25e9-37d6-bfbc-306309e39db5 | -14.45099 | -45.69333 | 2026-08-14 04:34:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 35a6657f-48c2-3a9f-9119-c8d2815d7f87 | -14.47386 | -45.68747 | 2026-08-14 04:34:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 1bbd5414-2aab-3996-b6a0-167e05c3c816 | -13.76081 | -53.41161 | 2026-08-14 04:34:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 0c3e2dbb-c796-35e3-b2d8-b02a16c2610f | -11.49694 | -54.63823 | 2026-08-14 04:34:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 7.1 |
| aea1f85f-173f-3c58-80f7-3915681b7e82 | -11.86347 | -51.95225 | 2026-08-14 04:34:00 | NOAA-20 | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 31441906-2f6a-3841-981b-81ed38e95ef8 | -11.59428 | -54.67441 | 2026-08-14 04:34:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d1c1f799-c234-38b1-94b1-eaf43395f756 | -12.72364 | -48.43612 | 2026-08-14 04:34:00 | NOAA-20 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| d611a38e-62cd-369a-ac67-052a4d1936b9 | -17.12131 | -51.68908 | 2026-08-14 04:34:00 | NOAA-20 | CAIAPÔNIA | GOIÁS | Brasil | 5204409 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 8f6575b1-e442-3a87-9dd7-7540db577c62 | -13.55815 | -46.25622 | 2026-08-14 04:34:00 | NOAA-20 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 1e91a8e8-3f01-3f85-a726-349bee82c4ff | -14.45806 | -45.69739 | 2026-08-14 04:34:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| d3ba6922-9d70-3e56-9327-9ba911e6437f | -12.65227 | -54.75286 | 2026-08-14 04:34:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |


[Clique aqui para ver as próximas entradas](README23.md)
