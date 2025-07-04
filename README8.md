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

## Dados Diários - Página 8

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| d083f74b-790e-31fc-9f65-187265b49285 | -4.00955 | -43.23462 | 2025-07-04 04:14:00 | NPP-375D | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 049d7689-0a67-341e-a018-1b5d368288b6 | -5.92006 | -43.47973 | 2025-07-04 04:17:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 739eabb5-e2a1-370b-b6ec-cab7073aac39 | -5.75063 | -46.0834 | 2025-07-04 04:17:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| ab176aa2-23ae-32b6-8207-d7cd2c847356 | -9.73735 | -48.35673 | 2025-07-04 04:17:00 | NPP-375D | LAJEADO | TOCANTINS | Brasil | 1712009 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 65cac269-97d8-33ae-b04e-fb4fd13ef8f0 | -11.93036 | -45.39286 | 2025-07-04 04:17:00 | NPP-375D | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| aee7dd4b-0093-396f-8038-5b215e274b29 | -6.73869 | -43.18274 | 2025-07-04 04:17:00 | NPP-375D | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 0a801cb6-c553-3365-8fcf-e63753441a8e | -7.21737 | -43.08788 | 2025-07-04 04:17:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 0.5 |
| 49bbae0f-a3f6-3e2d-bc6f-f68d9370ec19 | -10.98941 | -45.09528 | 2025-07-04 04:17:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 1ff9d322-f4b8-3183-a609-7dfaf69fb9b5 | -6.73365 | -43.14995 | 2025-07-04 04:17:00 | NPP-375D | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 4b939aed-a86d-3b6e-afb8-4b0893711712 | -12.26681 | -43.65602 | 2025-07-04 04:17:00 | NPP-375D | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 1c284d3e-c68b-345e-9105-ce4a9e2d0f68 | -11.92933 | -45.37796 | 2025-07-04 04:17:00 | NPP-375D | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| ec00bdaa-5ac5-33ff-98c4-aa4452718d3f | -10.36739 | -47.55954 | 2025-07-04 04:17:00 | NPP-375D | LAGOA DO TOCANTINS | TOCANTINS | Brasil | 1711951 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 2e53f646-934c-3076-a547-512dba22feeb | -10.30617 | -57.14204 | 2025-07-04 04:17:00 | NPP-375D | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| e6213b54-f3da-3634-8945-b1d29003488e | -6.73974 | -43.15446 | 2025-07-04 04:17:00 | NPP-375D | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| dcb0bff4-efb3-33b8-ac38-324a9b0837ca | -15.56902 | -47.85554 | 2025-07-04 04:17:00 | NPP-375D | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 1.9 |
| a0d18596-1c9b-3fbc-b0db-169a6e91baff | -15.07694 | -48.94482 | 2025-07-04 04:17:00 | NPP-375D | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 14c0be1e-b551-3a7b-85c5-6648f372697d | -9.7297 | -49.05969 | 2025-07-04 04:17:00 | NPP-375D | DIVINÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1707108 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| b1e44da0-311b-337e-9119-22b08522af3a | -7.19607 | -43.58632 | 2025-07-04 04:17:00 | NPP-375D | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| f5753c85-eca6-3939-94c6-c90ddb4cdead | -6.66311 | -43.1709 | 2025-07-04 04:17:00 | NPP-375D | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 41a34f6c-c9c3-3edb-9396-c30f9a5fa441 | -6.77739 | -44.01017 | 2025-07-04 04:17:00 | NPP-375D | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 0.6 |
| c91ffdee-1daf-34a2-a820-37bcc2fd3695 | -10.25033 | -48.15165 | 2025-07-04 04:17:00 | NPP-375D | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| be5946b7-6436-3933-92ba-f564854009e8 | -6.01355 | -44.52865 | 2025-07-04 04:17:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| d95517c7-4827-3dd0-97ff-b44d1cc5bcd3 | -11.92656 | -45.37385 | 2025-07-04 04:17:00 | NPP-375D | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 0.4 |
| f02bc41d-1ba3-319f-aac5-1acc1aaf3164 | -11.92031 | -45.3912 | 2025-07-04 04:17:00 | NPP-375D | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 85960c72-3c38-3078-99b0-dd64eafac3c7 | -5.47741 | -49.57709 | 2025-07-04 04:17:00 | NPP-375D | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 1d82d74a-050e-37b3-b10d-e3333fe79ddd | -19.43962 | -44.34042 | 2025-07-04 04:17:00 | NPP-375D | SETE LAGOAS | MINAS GERAIS | Brasil | 3167202 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 720e437e-0fb0-3855-8221-c16ff47e4095 | -6.63119 | -56.27554 | 2025-07-04 04:17:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 6c5118c2-a7e9-3734-b4b0-a2c6ea1b87b1 | -7.19745 | -43.42992 | 2025-07-04 04:17:00 | NPP-375D | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 758f9af7-b9fa-38fe-ac37-9c6ec4eb9348 | -6.01297 | -44.53227 | 2025-07-04 04:17:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| ac191014-53fa-3451-92e4-75f73905d6f4 | -8.48994 | -49.85352 | 2025-07-04 04:17:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 3922d4f4-cbbf-31e6-b08c-2d5e38185740 | -7.39114 | -44.65422 | 2025-07-04 04:17:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 517e21da-17fa-3d30-a8ad-ea7c2bc41dde | -7.09449 | -49.17191 | 2025-07-04 04:17:00 | NPP-375D | SANTA FÉ DO ARAGUAIA | TOCANTINS | Brasil | 1718865 | 17 | 33 | nan | nan | nan | Amazônia | 7.9 |
| 7b87011e-3838-3ea4-89f6-a99a8cf17497 | -11.92469 | -45.40667 | 2025-07-04 04:17:00 | NPP-375D | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| a64fb60e-8d36-3392-b833-5f265d8d6bcd | -7.17878 | -44.01647 | 2025-07-04 04:17:00 | NPP-375D | MARCOS PARENTE | PIAUÍ | Brasil | 2206001 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| e1317ca9-9ea8-3135-b6b5-e7d79e99f622 | -6.49703 | -43.64219 | 2025-07-04 04:17:00 | NPP-375D | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 29e118c2-9096-315a-96d4-47fa1d75a7a6 | -11.44976 | -45.11922 | 2025-07-04 04:17:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 11.6 |
| 47913aac-a88b-316d-ade0-3aa522e8986f | -7.91067 | -44.53556 | 2025-07-04 04:17:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| e2bd380e-ecfe-3c95-bddd-8c7bb073a88c | -7.66127 | -44.34248 | 2025-07-04 04:17:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| ca10b2ce-dc55-3b88-ad45-ffc089ad70ab | -11.92598 | -45.37741 | 2025-07-04 04:17:00 | NPP-375D | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 4cb45aff-93e6-392f-a7d5-e5effe4767fe | -6.74193 | -43.14059 | 2025-07-04 04:17:00 | NPP-375D | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| da61e094-116b-3300-9390-45a0588d9a6a | -9.78437 | -48.57239 | 2025-07-04 04:17:00 | NPP-375D | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 736a8ab7-59d8-3b2e-a4d9-6df01bcb298b | -11.54213 | -43.24513 | 2025-07-04 04:17:00 | NPP-375D | MORPARÁ | BAHIA | Brasil | 2921609 | 29 | 33 | nan | nan | nan | Caatinga | 1.1 |
| e540c35c-e18d-3bab-b889-5b2cb34b70d5 | -11.9276 | -45.38871 | 2025-07-04 04:17:00 | NPP-375D | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| c31d54b0-824e-3c12-b5d5-83fbe4dcee83 | -11.86588 | -44.86351 | 2025-07-04 04:17:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| d59971e3-f1ff-38c4-8f5d-bab9244bc6e5 | -7.21791 | -43.0844 | 2025-07-04 04:17:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 0.5 |
| 60cfbd4c-c132-3eb1-92d4-15b853c1ac21 | -12.10696 | -43.65637 | 2025-07-04 04:17:00 | NPP-375D | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| ad75d24b-f37e-328d-b76e-d6ab7f5887ed | -11.92876 | -45.38154 | 2025-07-04 04:17:00 | NPP-375D | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| ffa92a86-154d-3ed4-b840-647dfbf26338 | -7.12759 | -43.16635 | 2025-07-04 04:17:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 64930f6b-7d48-3fca-8db3-0f60201fa144 | -6.65979 | -43.17038 | 2025-07-04 04:17:00 | NPP-375D | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 6e3faeaa-ae29-3fd6-bd49-7f141f356994 | -10.24306 | -47.67673 | 2025-07-04 04:17:00 | NPP-375D | SANTA TEREZA DO TOCANTINS | TOCANTINS | Brasil | 1719004 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| bb822891-04c2-346e-87f2-b693960acc22 | -11.85923 | -44.86993 | 2025-07-04 04:17:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 85e75310-b44b-3000-b80c-8eaccd795332 | -7.22901 | -43.1004 | 2025-07-04 04:17:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 2c5fc88e-6eeb-3e06-bf75-fc1cf9e3d878 | -11.77202 | -44.90277 | 2025-07-04 04:17:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 17d0e99d-a338-3cca-9304-b663b80387f6 | -7.09059 | -44.16843 | 2025-07-04 04:17:00 | NPP-375D | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 15109340-648e-34d7-9e3b-437c7b36fdb3 | -11.86481 | -44.85633 | 2025-07-04 04:17:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 49397538-13cb-3a30-9d9e-7af456251cba | -5.73979 | -44.94941 | 2025-07-04 04:17:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 48b0904f-8b42-3bbb-872f-899f118d1813 | -11.24601 | -44.88943 | 2025-07-04 04:17:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 7ddb182e-4dd1-3c4c-a848-dd9be0b49dfc | -7.0256 | -44.03896 | 2025-07-04 04:17:00 | NPP-375D | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| dffd473a-7ae7-3d34-a651-46163a5475b7 | -6.60878 | -43.89327 | 2025-07-04 04:17:00 | NPP-375D | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| d5579327-4615-376a-95e2-d2986434bd44 | -10.56216 | -49.13238 | 2025-07-04 04:17:00 | NPP-375D | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 22.2 |
| 4a358713-7a98-39cb-8f34-a53804c761a1 | -8.58373 | -48.20902 | 2025-07-04 04:17:00 | NPP-375D | GUARAÍ | TOCANTINS | Brasil | 1709302 | 17 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 472691b2-02ff-3e4e-a29e-bf09506d0420 | -11.86531 | -44.86705 | 2025-07-04 04:17:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| f4a1c293-a7e3-3be3-a17d-bae3a1f5cb83 | -11.54148 | -47.31188 | 2025-07-04 04:17:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 6813f1e7-2956-3a87-9266-eb763bd829fe | -10.5575 | -49.13527 | 2025-07-04 04:17:00 | NPP-375D | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 22.2 |
| 38229bcd-4a42-33cd-81ab-c995f5fe995a | -10.25123 | -47.67369 | 2025-07-04 04:17:00 | NPP-375D | SANTA TEREZA DO TOCANTINS | TOCANTINS | Brasil | 1719004 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 94e2a6f9-d47c-3cc7-8b27-cb53bc156ab5 | -10.30737 | -57.13601 | 2025-07-04 04:17:00 | NPP-375D | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 2818f8d3-1b56-3725-8de9-09e3a1ec9fe1 | -11.44366 | -45.11454 | 2025-07-04 04:17:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 851e0c0f-70e9-337b-9505-c0384674af66 | -16.61696 | -43.36873 | 2025-07-04 04:17:00 | NPP-375D | GRÃO MOGOL | MINAS GERAIS | Brasil | 3127800 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| eca6085b-a81d-33d4-9b81-c31d93fe2a62 | -6.28069 | -43.68329 | 2025-07-04 04:17:00 | NPP-375D | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| a258ab1c-899e-3336-8fac-dc64cfdaaeef | -11.93429 | -45.38984 | 2025-07-04 04:17:00 | NPP-375D | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| b89ba0a2-09d6-38fb-a752-126a30676a2b | -6.66904 | -47.87039 | 2025-07-04 04:17:00 | NPP-375D | DARCINÓPOLIS | TOCANTINS | Brasil | 1706506 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| f65a3e60-ce64-3820-9a4a-80da0a986f98 | -6.66643 | -43.17142 | 2025-07-04 04:17:00 | NPP-375D | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 8bde4d3d-a3dc-3e9a-af70-4b31a86dbcc0 | -6.74033 | -43.17233 | 2025-07-04 04:17:00 | NPP-375D | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 45cb2f57-abfd-30dc-9e32-44104c6d12a5 | -6.28179 | -43.67633 | 2025-07-04 04:17:00 | NPP-375D | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 1c4f29c5-c104-3b1a-bb89-b4297f2e0722 | -10.65062 | -44.48446 | 2025-07-04 04:17:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 8ee0272a-7337-3194-a8c3-7c61ec5f4fc6 | -6.73697 | -43.15047 | 2025-07-04 04:17:00 | NPP-375D | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 92b17d9f-6722-387e-abf8-9813e9cb99c2 | -7.21959 | -43.09535 | 2025-07-04 04:17:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 3.3 |
| 019d2ea4-1f79-3951-8181-ef5a94f9c20c | -8.85599 | -47.95517 | 2025-07-04 04:17:00 | NPP-375D | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 53ee02b8-9cfb-3d4a-a996-d16071b998c7 | -16.95085 | -46.08653 | 2025-07-04 04:17:00 | NPP-375D | BRASILÂNDIA DE MINAS | MINAS GERAIS | Brasil | 3108552 | 31 | 33 | nan | nan | nan | Cerrado | 2.6 |
| c5605a1d-1abc-3de0-a0bc-6118e7b9ad3e | -18.49596 | -45.90269 | 2025-07-04 04:17:00 | NPP-375D | VARJÃO DE MINAS | MINAS GERAIS | Brasil | 3170750 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 29e4df60-1429-3ffd-8a99-1f3b3089d899 | -6.73923 | -43.17927 | 2025-07-04 04:17:00 | NPP-375D | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Caatinga | 2.5 |
| d3f688bf-47cd-3aff-bc80-10920906e104 | -11.92527 | -45.40308 | 2025-07-04 04:17:00 | NPP-375D | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| f8476070-e8ce-35e2-bd0b-6d771c7962e8 | -6.74673 | -43.04535 | 2025-07-04 04:17:00 | NPP-375D | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| b1584d7c-f422-381e-8a0d-e93526e5b76d | -9.79397 | -47.74635 | 2025-07-04 04:17:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 908730e3-cfa6-3783-b2ad-e5781b901054 | -7.23233 | -43.10092 | 2025-07-04 04:17:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 700204f6-637a-3fe5-a9ee-78b31f748ea8 | -11.92308 | -45.39533 | 2025-07-04 04:17:00 | NPP-375D | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 2.9 |
| c36326ba-4a4e-3366-869a-7819542c3f1b | -11.62839 | -46.92012 | 2025-07-04 04:17:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| e7fed38e-0412-3737-8132-d1bea5252981 | -11.8598 | -44.86638 | 2025-07-04 04:17:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| ba675800-57f5-33bb-8d73-20142c805026 | -11.92541 | -45.38098 | 2025-07-04 04:17:00 | NPP-375D | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 623afeca-342d-3870-8126-d75692bdcd98 | -8.48483 | -49.85696 | 2025-07-04 04:17:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| abda6015-1001-3951-9eed-4c6a40054780 | -17.09514 | -43.80451 | 2025-07-04 04:17:00 | NPP-375D | BOCAIÚVA | MINAS GERAIS | Brasil | 3107307 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 10107a00-7245-32c9-a6f2-efc6f24b4746 | -11.46968 | -47.29968 | 2025-07-04 04:17:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 0.4 |
| ed75bc73-ac34-3d20-9018-f17b11fe09b0 | -11.9292 | -45.40004 | 2025-07-04 04:17:00 | NPP-375D | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| a73fcce0-6e93-3405-a1db-937bb6a55976 | -6.72865 | -43.1385 | 2025-07-04 04:17:00 | NPP-375D | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| c6769793-a419-3bd3-a47d-8242c12b8ad6 | -5.91565 | -43.4469 | 2025-07-04 04:17:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| f30f6eab-cf58-3e8c-9dbe-e74d63c97e31 | -11.44699 | -45.1151 | 2025-07-04 04:17:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 11.6 |
| e728576a-23ca-3f39-981a-67b257b28dfb | -8.52588 | -54.77435 | 2025-07-04 04:17:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 7c5f722f-fcce-3fba-9f16-076716f37cae | -17.65232 | -46.83146 | 2025-07-04 04:17:00 | NPP-375D | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 04701b9b-8fc1-3cfe-b56b-908721d7f792 | -7.63727 | -44.34229 | 2025-07-04 04:17:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 1060fc4e-d95d-3884-a5b0-f434c6c57878 | -6.28512 | -43.67685 | 2025-07-04 04:17:00 | NPP-375D | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 5.2 |


[Clique aqui para ver as próximas entradas](README9.md)
