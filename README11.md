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

## Dados Diários - Página 11

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 2c825709-418d-3267-a9a7-538b574a5384 | -11.52241 | -51.92437 | 2025-08-24 00:50:00 | TERRA_M-M | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 33.7 |
| c6b48fac-579c-33c7-8c2e-749fd5490043 | -10.61152 | -44.32432 | 2025-08-24 00:50:00 | TERRA_M-M | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 120.9 |
| d7ca773e-5200-3923-a950-27769343cb73 | -5.45354 | -60.19889 | 2025-08-24 00:50:00 | TERRA_M-M | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 68.6 |
| 6c36c41f-cfb0-35a3-9d0c-adb17763d465 | -11.51501 | -51.87038 | 2025-08-24 00:50:00 | TERRA_M-M | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 99.1 |
| 11f4ae5c-1ddc-3a45-9bbb-f19075b739e0 | -5.41098 | -44.97489 | 2025-08-24 00:50:00 | TERRA_M-M | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 76.6 |
| eb864604-7f92-3344-8e2c-3803e1fbd815 | -9.15651 | -59.47593 | 2025-08-24 00:50:00 | TERRA_M-M | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 402.1 |
| 495406a5-8766-3d3a-8968-b5add8654adf | -9.14187 | -60.7812 | 2025-08-24 00:50:00 | TERRA_M-M | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 69.2 |
| 8c605fe7-b645-34e7-8572-220ec7d580df | -9.22875 | -60.9162 | 2025-08-24 00:50:00 | TERRA_M-M | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 42.9 |
| 52dabb59-95d2-3bbd-aba3-dcf5f275a26d | -5.61302 | -60.23933 | 2025-08-24 00:50:00 | TERRA_M-M | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 65.5 |
| 7478826b-f920-39ff-a2c1-30b959ffd130 | -8.77033 | -49.99959 | 2025-08-24 00:50:00 | TERRA_M-M | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| cd6c2e2a-d610-3874-9f14-0249d94f82f1 | -11.98785 | -61.028 | 2025-08-24 00:50:00 | TERRA_M-M | PIMENTA BUENO | RONDÔNIA | Brasil | 1100189 | 11 | 33 | nan | nan | nan | Amazônia | 117.4 |
| fc2f9aa1-ba08-30b1-bee5-22071a980d22 | -14.52054 | -52.04564 | 2025-08-24 00:50:00 | TERRA_M-M | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 11.2 |
| f850e3e0-dce2-3216-a937-fd2e24df2b42 | -8.75953 | -49.99094 | 2025-08-24 00:50:00 | TERRA_M-M | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 12.2 |
| b5b2e809-6408-35a3-9a7b-3e21b28a054f | -8.90645 | -62.43454 | 2025-08-24 00:50:00 | TERRA_M-M | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 114.8 |
| e3066e58-d7ba-3324-9de4-21473b62edb6 | -4.95917 | -55.81604 | 2025-08-24 00:50:00 | TERRA_M-M | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 119.0 |
| 4ba61077-c84d-3764-8df5-9c1f37e342a3 | -5.41949 | -60.15525 | 2025-08-24 00:50:00 | TERRA_M-M | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 55.4 |
| 143f779d-e8c7-3b31-ba90-d164f975af27 | -5.61819 | -60.23231 | 2025-08-24 00:50:00 | TERRA_M-M | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 44.5 |
| b6e4b97d-6f3c-37c3-a846-69b0af27209e | -11.52046 | -50.46477 | 2025-08-24 00:50:00 | TERRA_M-M | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 4245b194-cbf6-3793-9ce2-8290c03caa15 | -11.52178 | -50.47401 | 2025-08-24 00:50:00 | TERRA_M-M | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 9ceecf03-657a-342d-ada1-63873d1e6afa | -9.15376 | -59.45203 | 2025-08-24 00:50:00 | TERRA_M-M | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 273.9 |
| 5f61a933-ccf7-32de-8190-6cf5c34d3823 | -11.5327 | -51.8678 | 2025-08-24 00:50:00 | TERRA_M-M | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 7.7 |
| b0e2746b-2c80-389e-9a8d-c3904f02db5c | -10.81469 | -46.39938 | 2025-08-24 00:50:00 | TERRA_M-M | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 25.3 |
| 65d0ce8e-e49f-38a6-8c18-2e116b9c2b77 | -14.77659 | -55.41103 | 2025-08-24 00:50:00 | TERRA_M-M | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 22.2 |
| 15c8206d-bd3c-35a0-a338-4b5f5bc4f069 | -6.91495 | -52.85411 | 2025-08-24 00:50:00 | TERRA_M-M | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 25.4 |
| 4ae0badc-8ddd-3fa9-bcdf-8836c01d53ea | -14.75289 | -55.39928 | 2025-08-24 00:50:00 | TERRA_M-M | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 23.5 |
| 1217ebfe-38ba-3fea-ae59-ea27e6164eed | -13.47368 | -47.02264 | 2025-08-24 00:50:00 | TERRA_M-M | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 15.1 |
| 2c529ff0-393f-38ab-ae82-b606100e2bb9 | -10.60998 | -50.15472 | 2025-08-24 00:50:00 | TERRA_M-M | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 11.1 |
| 4b821f7e-d364-3666-a84b-a486c8329c92 | -14.8 | -59.63077 | 2025-08-24 00:50:00 | TERRA_M-M | NOVA LACERDA | MATO GROSSO | Brasil | 5106182 | 51 | 33 | nan | nan | nan | Amazônia | 61.5 |
| 3d5b9694-7977-3f56-81d4-ce594d309677 | -14.52336 | -51.93048 | 2025-08-24 00:50:00 | TERRA_M-M | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 10.0 |
| 2f51a7ff-ffea-38e2-9830-ac8271266b67 | -9.2 | -60.76822 | 2025-08-24 00:50:00 | TERRA_M-M | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 36.8 |
| 5168c5a0-456c-3d9f-8d53-1095a25dcab3 | -12.04019 | -50.35926 | 2025-08-24 00:50:00 | TERRA_M-M | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 8.1 |
| 2df32658-6fcb-3937-a534-a133aae0156b | -6.36743 | -45.5317 | 2025-08-24 00:50:00 | TERRA_M-M | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 17.0 |
| 15154447-d4b8-3fd8-b203-c4d314c57e34 | -11.13949 | -46.32825 | 2025-08-24 00:50:00 | TERRA_M-M | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 14.2 |
| 4885f08e-dde9-3ab7-a848-f1922f4c6cbd | -12.73286 | -48.12267 | 2025-08-24 00:50:00 | TERRA_M-M | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 20.7 |
| e036674c-b445-3099-8895-da05156274e5 | -10.40534 | -47.1693 | 2025-08-24 00:50:00 | TERRA_M-M | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 8.6 |
| 128c8e35-dde1-358e-b39b-561125a7ea57 | -8.8057 | -48.78362 | 2025-08-24 00:50:00 | TERRA_M-M | COLMÉIA | TOCANTINS | Brasil | 1716703 | 17 | 33 | nan | nan | nan | Amazônia | 6.5 |
| 4500f30c-9c5c-3fc3-8dcd-d4448ecb51e7 | -11.51377 | -51.86138 | 2025-08-24 00:50:00 | TERRA_M-M | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 90.8 |
| 6d49467c-5350-3263-a113-b7b281f693bd | -8.61939 | -62.61665 | 2025-08-24 00:50:00 | TERRA_M-M | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 79.0 |
| 4c66f48e-2cb4-3f4f-bd40-c9d0b79c7999 | -11.28289 | -44.97952 | 2025-08-24 00:50:00 | TERRA_M-M | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 23.4 |
| ab89b10d-cdba-31a8-a673-e78fb8cac869 | -5.43333 | -60.15345 | 2025-08-24 00:50:00 | TERRA_M-M | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 17.6 |
| 014cec8a-ad73-34bd-bc3b-67f622bc9b1c | -11.53764 | -51.90379 | 2025-08-24 00:50:00 | TERRA_M-M | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 7.3 |
| 57488510-0f8b-3813-9dd3-49a24a537a00 | -9.80442 | -61.20883 | 2025-08-24 00:50:00 | TERRA_M-M | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 42.7 |
| 75edd38a-efd6-3e5f-be27-2f87ef74f083 | -8.85813 | -52.03938 | 2025-08-24 00:50:00 | TERRA_M-M | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 8.8 |
| d78a3d4e-4a1e-3309-9f6f-cb8f523c9659 | -9.82822 | -47.75577 | 2025-08-24 00:50:00 | TERRA_M-M | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 11.1 |
| 14519e4e-3b76-35ce-b73e-6bbfe1ba6755 | -10.46495 | -46.8834 | 2025-08-24 00:50:00 | TERRA_M-M | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 9.4 |
| 9af63430-ceda-37cf-86e4-5753fbd75f8f | -5.44509 | -60.19349 | 2025-08-24 00:50:00 | TERRA_M-M | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 59.7 |
| 5920bb77-1b03-3c8d-9d3e-1140c69db6e0 | -7.02291 | -44.63457 | 2025-08-24 00:50:00 | TERRA_M-M | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 64.1 |
| fe6a5452-94cd-3196-a1b6-c320205e58eb | -10.5972 | -50.19561 | 2025-08-24 00:50:00 | TERRA_M-M | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 43.8 |
| a924c864-d94b-398c-aaac-38a36713bfa4 | -12.73106 | -48.11087 | 2025-08-24 00:50:00 | TERRA_M-M | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 15.4 |
| 6bd47ddd-aeef-3c44-b46d-125895942e5a | -5.95082 | -52.20792 | 2025-08-24 00:50:00 | TERRA_M-M | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| d2f11fb3-e3b0-3dac-9549-e3b7b06ebbc5 | -5.40889 | -44.98096 | 2025-08-24 00:50:00 | TERRA_M-M | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 119.2 |
| a987e4c2-828c-3e1a-907a-28509b562fb7 | -11.52262 | -51.86009 | 2025-08-24 00:50:00 | TERRA_M-M | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 13.5 |
| 749f1815-9cde-3b16-a338-d7b76f2db62e | -7.02704 | -44.66016 | 2025-08-24 00:50:00 | TERRA_M-M | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 46.8 |
| 3ed68314-d47d-327e-8389-d2fc5a2f9ae3 | -12.72461 | -48.13494 | 2025-08-24 00:50:00 | TERRA_M-M | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 23.5 |
| 5aafb201-2070-302f-9dd8-351198ebf4ad | -8.84007 | -49.91085 | 2025-08-24 00:50:00 | TERRA_M-M | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 7.2 |
| 61465faa-02fe-331e-a5f2-144e552b3d02 | -14.03052 | -54.07934 | 2025-08-24 00:50:00 | TERRA_M-M | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 10.9 |
| ac637477-83be-3c30-9552-44d602eba18a | -5.41437 | -60.17347 | 2025-08-24 00:50:00 | TERRA_M-M | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 26.0 |
| 5feaeac4-7327-3cd1-a778-00b000a96f85 | -11.5231 | -50.48325 | 2025-08-24 00:50:00 | TERRA_M-M | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 142f476a-819f-3cc6-be48-33a8e5b71384 | -9.23384 | -60.9207 | 2025-08-24 00:50:00 | TERRA_M-M | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 53.4 |
| ca7c8c80-7d4c-35ed-8cd8-143dc1770c64 | -4.4879 | -47.6804 | 2025-08-24 00:50:00 | TERRA_M-M | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 12.7 |
| d9d65358-e5b7-3f6d-92fa-6c2731530553 | -12.04915 | -50.35791 | 2025-08-24 00:50:00 | TERRA_M-M | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 6.4 |
| cdf5fe49-1df6-30ea-a4ae-fe01a80adc49 | -13.46902 | -47.02857 | 2025-08-24 00:50:00 | TERRA_M-M | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 11.8 |
| f4e70d0d-ff89-3a4d-b54d-0fd2aa98ec6f | -13.46314 | -47.02436 | 2025-08-24 00:50:00 | TERRA_M-M | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 8.6 |
| 0a0192b2-0e52-33ba-acfb-782c6bc57e84 | -6.31794 | -59.87888 | 2025-08-24 00:50:00 | TERRA_M-M | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 15.5 |
| 105fc600-8758-3359-86f2-e57920756544 | -10.59779 | -44.32674 | 2025-08-24 00:50:00 | TERRA_M-M | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 49.2 |
| dda59697-310e-359f-878f-2a39142b2087 | -11.53002 | -51.91407 | 2025-08-24 00:50:00 | TERRA_M-M | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 40.0 |
| af6d73cc-fa45-3aef-b2a3-c7d7b5b1eadd | -9.02639 | -47.64627 | 2025-08-24 00:50:00 | TERRA_M-M | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 9.8 |
| b99ba240-ce0f-3de1-a6c3-2d46708dd792 | -14.76561 | -55.41243 | 2025-08-24 00:50:00 | TERRA_M-M | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 47.8 |
| eed1dd70-35c7-3205-8a81-4eecb3204091 | -14.80949 | -55.97474 | 2025-08-24 00:50:00 | TERRA_M-M | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 14.3 |
| 0c068df0-47a2-327c-99a5-fcefe18dd81b | -13.48631 | -46.89632 | 2025-08-24 00:50:00 | TERRA_M-M | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 0637c0ed-e8cd-3888-95a0-694433b7bbc2 | -14.53233 | -51.92919 | 2025-08-24 00:50:00 | TERRA_M-M | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 8.2 |
| 680566fd-0681-3a5b-a1a4-4e4811f4fb21 | -6.43541 | -53.38519 | 2025-08-24 00:50:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 22.4 |
| b53f2d10-31e9-384d-8745-3f08eed258ec | -12.20665 | -47.11008 | 2025-08-24 00:50:00 | TERRA_M-M | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 16.0 |
| 0788b9c6-bb5c-3f29-b8bd-9eeb1b18bbed | -14.65999 | -56.57908 | 2025-08-24 00:50:00 | TERRA_M-M | ALTO PARAGUAI | MATO GROSSO | Brasil | 5100508 | 51 | 33 | nan | nan | nan | Cerrado | 18.6 |
| f8bbd477-46c7-3a1c-a208-91c7c895437a | -10.75726 | -48.27215 | 2025-08-24 00:50:00 | TERRA_M-M | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 1d9ab309-3638-3df8-8d8d-b5b4dcdb37fd | -11.31853 | -47.85424 | 2025-08-24 00:50:00 | TERRA_M-M | SANTA ROSA DO TOCANTINS | TOCANTINS | Brasil | 1718907 | 17 | 33 | nan | nan | nan | Cerrado | 26.2 |
| 3e3c6f3b-2586-33b4-99ab-bc04c744a5ff | -11.28124 | -44.97404 | 2025-08-24 00:50:00 | TERRA_M-M | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 26.9 |
| dbdb7287-e2d5-3620-a26e-44d8977f9e97 | -11.29892 | -53.95792 | 2025-08-24 00:50:00 | TERRA_M-M | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 6.9 |
| 69196fcb-fec5-3bb0-8929-fd4bde607eda | -14.25446 | -53.0303 | 2025-08-24 00:50:00 | TERRA_M-M | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 17.9 |
| d3d787f4-7f38-351b-82bf-4d1226d307af | -11.52442 | -50.49248 | 2025-08-24 00:50:00 | TERRA_M-M | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 67609dc4-918d-3a67-9c7a-465ad54935a9 | -9.15377 | -59.50694 | 2025-08-24 00:50:00 | TERRA_M-M | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 91.3 |
| bd82b1ac-dd01-3147-8bb5-5d147d8cd4c0 | -4.96063 | -55.82706 | 2025-08-24 00:50:00 | TERRA_M-M | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 138.4 |
| 58fddca5-2dd0-3b56-a8df-b66eba1678ff | -13.54994 | -51.54174 | 2025-08-24 00:50:00 | TERRA_M-M | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 12.7 |
| f5abf433-b2b3-372f-9539-d4018a14028e | -5.10081 | -56.97552 | 2025-08-24 00:50:00 | TERRA_M-M | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 7.3 |
| 80cf24c2-5548-3e9d-af5c-3a4942bbc7a7 | -8.18424 | -45.08779 | 2025-08-24 00:50:00 | TERRA_M-M | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 24.1 |
| 45234105-0a58-35c6-9b35-cded2b35cdb5 | -13.34657 | -54.39629 | 2025-08-24 00:50:00 | TERRA_M-M | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 7.8 |
| b3dc0f9e-47da-3707-96ac-4973663c157f | -6.68744 | -58.87334 | 2025-08-24 00:50:00 | TERRA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 20.2 |
| 15d2c39f-e354-3ad4-9a84-b75a2c310892 | -10.80591 | -46.41883 | 2025-08-24 00:50:00 | TERRA_M-M | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 39.2 |
| 28e0c48c-7883-3c19-b639-74c80c430a40 | -12.00425 | -61.02633 | 2025-08-24 00:50:00 | TERRA_M-M | PIMENTA BUENO | RONDÔNIA | Brasil | 1100189 | 11 | 33 | nan | nan | nan | Amazônia | 60.6 |
| 3a6c416b-dcdb-38bf-9557-4d7bbb4030d2 | -8.76887 | -49.98958 | 2025-08-24 00:50:00 | TERRA_M-M | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 40.3 |
| bb338e4e-2085-3d79-aec9-02525ef5f842 | -8.0646 | -49.6547 | 2025-08-24 00:50:00 | TERRA_M-M | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 12.9 |
| 2c6eb149-6332-3d0c-bb76-62ec1133d355 | -10.63166 | -51.62118 | 2025-08-24 00:50:00 | TERRA_M-M | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 7.9 |
| a53d429f-5e1d-36ee-9557-0a8d7b1226f7 | -11.32036 | -47.86625 | 2025-08-24 00:50:00 | TERRA_M-M | SANTA ROSA DO TOCANTINS | TOCANTINS | Brasil | 1718907 | 17 | 33 | nan | nan | nan | Cerrado | 9.1 |
| f5e89414-3142-3e49-a57e-92c0b52286c6 | -8.75262 | -46.75834 | 2025-08-24 00:50:00 | TERRA_M-M | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 17.0 |
| c54bfb80-1571-36f1-b204-5c5e9c39f357 | -4.97042 | -55.82576 | 2025-08-24 00:50:00 | TERRA_M-M | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 14.8 |
| 76dabaec-18e1-34cb-90c6-a3fbcdff6797 | -14.25576 | -53.04039 | 2025-08-24 00:50:00 | TERRA_M-M | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 10.9 |
| 514052e9-0c28-3519-a03a-2f55cb29e8f9 | -10.60087 | -50.15609 | 2025-08-24 00:50:00 | TERRA_M-M | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 23.2 |
| 327f9730-9393-3465-830a-d5c41f821d66 | -11.3289 | -47.85316 | 2025-08-24 00:50:00 | TERRA_M-M | SANTA ROSA DO TOCANTINS | TOCANTINS | Brasil | 1718907 | 17 | 33 | nan | nan | nan | Cerrado | 11.1 |
| 7f0e3679-7773-35f3-a8f0-345e74daec5b | -2.92239 | -53.69313 | 2025-08-24 00:52:00 | TERRA_M-M | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 6.6 |
| 86b2900c-08e5-38a8-9091-d42cd74aee75 | -3.05557 | -49.50919 | 2025-08-24 00:52:00 | TERRA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 7.5 |


[Clique aqui para ver as próximas entradas](README12.md)
