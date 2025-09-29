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

## Dados Diários - Página 39

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 9da51747-8df7-3834-ad0a-96c3672c8623 | -11.35968 | -45.07236 | 2025-09-29 04:08:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 095663e4-b367-3580-b6f0-060bc7764d93 | -12.41733 | -44.10359 | 2025-09-29 04:08:00 | NOAA-20 | TABOCAS DO BREJO VELHO | BAHIA | Brasil | 2930907 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 555c95b0-8779-32c6-be2b-adb2e0e8bdfa | -11.34857 | -45.07433 | 2025-09-29 04:08:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| b68180fd-a59a-36ea-bb02-a005e8523f98 | -13.38319 | -48.1576 | 2025-09-29 04:08:00 | NOAA-20 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 5.4 |
| f42c63d5-84e6-3b62-b295-8717a0fd4739 | -9.64016 | -48.12574 | 2025-09-29 04:08:00 | NOAA-20 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| efeeab7d-48f9-3830-875f-8433390d7a67 | -9.77486 | -46.19804 | 2025-09-29 04:08:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| c95938e9-d211-3c3b-99be-a14c145cb434 | -9.85493 | -47.31565 | 2025-09-29 04:08:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| babda9bb-6feb-3c22-b689-a0a1a98a7ff1 | -14.5894 | -45.02169 | 2025-09-29 04:08:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| dfeae91c-3c5a-3554-a863-2507bb01985d | -15.28164 | -49.4919 | 2025-09-29 04:08:00 | NOAA-20 | SANTA ISABEL | GOIÁS | Brasil | 5219357 | 52 | 33 | nan | nan | nan | Cerrado | 3.6 |
| c2b4e60a-bfb5-3ba3-b186-0f65a696dc40 | -13.79008 | -47.8672 | 2025-09-29 04:08:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| b0d1f7a5-75ea-3bf9-a5b6-8bd0e0fd49e4 | -15.27094 | -48.76216 | 2025-09-29 04:08:00 | NOAA-20 | VILA PROPÍCIO | GOIÁS | Brasil | 5222302 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 106613b0-ff1d-350a-aa91-ebda517c0c25 | -9.1002 | -45.84869 | 2025-09-29 04:08:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 8.5 |
| 991db9ff-2317-34ce-9447-c30f1496271b | -14.58663 | -45.01735 | 2025-09-29 04:08:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 5.8 |
| de4143c8-08fe-38a7-af39-bbbf31882ea3 | -13.3939 | -47.92336 | 2025-09-29 04:08:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| f650dedc-1a85-3b5e-9b2a-9544ed85e194 | -12.68651 | -46.86502 | 2025-09-29 04:08:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| ed8698e6-ea3a-3ab6-8ceb-081c58fa6d3c | -9.04624 | -46.70669 | 2025-09-29 04:08:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 66c6ede8-eae4-35fc-ab7c-2826765770e3 | -12.68275 | -46.86439 | 2025-09-29 04:08:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 27f11abc-20d9-3864-8c6d-e68f8aa4d759 | -12.6519 | -46.93097 | 2025-09-29 04:08:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 7aa1cac0-dfec-30fc-9e4b-e60ac508291f | -9.0828 | -45.88318 | 2025-09-29 04:08:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 7db7e2fa-0d9a-3f95-ad5d-1a8bd2a7ef7d | -15.49246 | -45.87455 | 2025-09-29 04:08:00 | NOAA-20 | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| b09014a9-803f-36a5-bc59-0dc6b147b28d | -11.62591 | -52.84592 | 2025-09-29 04:08:00 | NOAA-20 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| aaf57099-bbb0-3e1e-9db9-eed873cee397 | -11.62226 | -52.86512 | 2025-09-29 04:08:00 | NOAA-20 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| b06c1f04-b0bd-332f-99a4-c0a0277968d7 | -15.26761 | -48.75747 | 2025-09-29 04:08:00 | NOAA-20 | VILA PROPÍCIO | GOIÁS | Brasil | 5222302 | 52 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 66b5f2f7-d3b0-3a11-8c8e-1d59a6c6bb90 | -9.54173 | -44.66636 | 2025-09-29 04:08:00 | NOAA-20 | REDENÇÃO DO GURGUÉIA | PIAUÍ | Brasil | 2208700 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 84b96dba-e5b5-31f7-a443-234c1f4b695a | -15.28237 | -49.50792 | 2025-09-29 04:08:00 | NOAA-20 | SANTA ISABEL | GOIÁS | Brasil | 5219357 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 1cf59c4a-b899-33f4-8b11-05447413778a | -9.07985 | -45.87791 | 2025-09-29 04:08:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 2.6 |
| e2744947-7e92-3654-996d-5080db3351c6 | -16.24927 | -42.21357 | 2025-09-29 04:08:00 | NOAA-20 | SALINAS | MINAS GERAIS | Brasil | 3157005 | 31 | 33 | nan | nan | nan | Mata Atlântica | 7.0 |
| f4ba9447-7d74-37dd-aa62-fbfc10e64f42 | -11.82005 | -51.78551 | 2025-09-29 04:08:00 | NOAA-20 | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Amazônia | 10.5 |
| facbb74e-c552-3586-9d04-f57cf55288ed | -11.4312 | -44.95101 | 2025-09-29 04:08:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 5e67fa8f-bfe1-3669-9f75-ff06ac3f3652 | -15.28449 | -49.50032 | 2025-09-29 04:08:00 | NOAA-20 | SANTA ISABEL | GOIÁS | Brasil | 5219357 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| b3b9d9bb-63f4-3a26-8514-868e4ac03eaf | -9.99925 | -45.4087 | 2025-09-29 04:08:00 | NOAA-20 | SÃO GONÇALO DO GURGUÉIA | PIAUÍ | Brasil | 2209757 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 35447d85-fab9-3630-8ff3-cf64268e664b | -14.54221 | -48.43923 | 2025-09-29 04:08:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 3e24b306-006b-3541-8e9f-18d10b71957b | -11.93841 | -43.91697 | 2025-09-29 04:08:00 | NOAA-20 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 1b3cec8c-a204-3343-a6e5-232b8c4e1066 | -10.07923 | -47.18074 | 2025-09-29 04:08:00 | NOAA-20 | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 6f905ecf-556e-3c77-8d33-ade37670bbf4 | -15.87213 | -46.22237 | 2025-09-29 04:08:00 | NOAA-20 | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 0bb40b60-314b-30af-9684-fbe28e156ac5 | -12.17563 | -43.56248 | 2025-09-29 04:08:00 | NOAA-20 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 376aea02-7dee-39e7-9264-5600e06fed94 | -13.59757 | -48.06183 | 2025-09-29 04:08:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 1932e8eb-6d8c-3cc8-b795-a2a5b761bd71 | -10.40059 | -48.14753 | 2025-09-29 04:08:00 | NOAA-20 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| a6aca0fd-5f44-37f2-871f-b23a7fd62bbe | -10.04615 | -50.21327 | 2025-09-29 04:08:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 75bd5c0c-ff89-35d6-89b7-623ac4da6275 | -15.0348 | -46.97568 | 2025-09-29 04:08:00 | NOAA-20 | VILA BOA | GOIÁS | Brasil | 5222203 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| bc51b277-51b0-3dbd-8bec-f6765a09290b | -15.8741 | -46.83046 | 2025-09-29 04:08:00 | NOAA-20 | CABECEIRAS | GOIÁS | Brasil | 5204003 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| f990d315-e644-3e66-81be-045d5456b1b6 | -9.77198 | -46.1907 | 2025-09-29 04:08:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| edd89662-4498-3da5-9918-c17561562d23 | -11.72227 | -44.42366 | 2025-09-29 04:08:00 | NOAA-20 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| f7260bf2-b4ea-37b1-8995-a6ff683232f2 | -12.88869 | -45.2182 | 2025-09-29 04:08:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 4.4 |
| a1ccc3f7-1610-3aa1-982d-c84f158c62a1 | -13.76667 | -43.98045 | 2025-09-29 04:08:00 | NOAA-20 | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 9fe28604-6e31-37bc-a746-c98c684c1ac6 | -12.79935 | -47.74797 | 2025-09-29 04:08:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| a9c5e911-46e7-3241-b291-e9905b435f8e | -13.17256 | -49.99784 | 2025-09-29 04:08:00 | NOAA-20 | SÃO MIGUEL DO ARAGUAIA | GOIÁS | Brasil | 5220207 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| a5f76e0d-89ea-3d5f-bfbf-bceea4f86c2a | -10.96603 | -49.56987 | 2025-09-29 04:08:00 | NOAA-20 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 49801804-3608-3e66-b1a2-fae700b377f8 | -13.55727 | -47.26744 | 2025-09-29 04:08:00 | NOAA-20 | TERESINA DE GOIÁS | GOIÁS | Brasil | 5221080 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| ec7cda1c-88c0-398f-b152-8313bb293640 | -14.5382 | -48.43851 | 2025-09-29 04:08:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 5.9 |
| c60a491e-25ed-352b-a81d-aacba63e8469 | -10.71478 | -53.80265 | 2025-09-29 04:08:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 61d996b3-ce5f-3d42-9656-f9db3ac94330 | -11.7052 | -44.33342 | 2025-09-29 04:08:00 | NOAA-20 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 5f146fc3-c0bf-3178-a9d4-b3acfbcc9c6e | -12.20799 | -43.74363 | 2025-09-29 04:08:00 | NOAA-20 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| a420dc6e-9e2f-34f7-bd8d-d92be38a2a89 | -13.63145 | -47.30822 | 2025-09-29 04:08:00 | NOAA-20 | TERESINA DE GOIÁS | GOIÁS | Brasil | 5221080 | 52 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 17c1919d-219a-3420-9f3a-e6175f11fe7a | -12.21074 | -43.74783 | 2025-09-29 04:08:00 | NOAA-20 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 22994065-768c-3eee-b7bf-02496ebe69b8 | -11.9297 | -48.02637 | 2025-09-29 04:08:00 | NOAA-20 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 15.4 |
| eee991d3-bbed-31be-9c2c-195a751c8f7a | -11.43847 | -45.0362 | 2025-09-29 04:08:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| c666459b-8b37-3727-8dbe-c4ce6c4d2e85 | -15.53169 | -47.91268 | 2025-09-29 04:08:00 | NOAA-20 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 03639481-161a-3abc-bfe3-735e953723af | -9.76651 | -47.79946 | 2025-09-29 04:08:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 9b5e0742-0e06-33a6-9108-2bb8d3ff5856 | -12.42069 | -44.10414 | 2025-09-29 04:08:00 | NOAA-20 | TABOCAS DO BREJO VELHO | BAHIA | Brasil | 2930907 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| d481e463-3b8f-3039-9baa-ea110d490d84 | -15.90426 | -46.24547 | 2025-09-29 04:08:00 | NOAA-20 | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 12484c8a-01f9-3d99-96e5-20d5d7307d3c | -15.4899 | -45.87871 | 2025-09-29 04:08:00 | NOAA-20 | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 6484abb3-76b2-301c-bc8d-9a7d334add12 | -13.59974 | -48.0498 | 2025-09-29 04:08:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.5 |
| f42ad129-e7d8-35cb-afd2-5324390ea57d | -11.67054 | -44.28949 | 2025-09-29 04:08:00 | NOAA-20 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 32c3a4af-1b4e-39b4-8050-be3b6a28ccd7 | -11.45029 | -47.28555 | 2025-09-29 04:08:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 1ba55918-d5d8-3ad7-99e0-54c70328c8b3 | -15.27519 | -49.50324 | 2025-09-29 04:08:00 | NOAA-20 | SANTA ISABEL | GOIÁS | Brasil | 5219357 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| cbf8f555-2619-37e0-812f-4d496f8da78d | -15.28018 | -49.49994 | 2025-09-29 04:08:00 | NOAA-20 | SANTA ISABEL | GOIÁS | Brasil | 5219357 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 55ca5132-3411-3972-b549-be1feb53edf0 | -14.57145 | -48.27716 | 2025-09-29 04:08:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 862c6bb0-81a7-3dc0-a6d8-1b383a23afeb | -8.86146 | -45.03407 | 2025-09-29 04:08:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 2.8 |
| b3ea945b-4ba5-3774-9b47-a1209b450257 | -10.91878 | -45.71872 | 2025-09-29 04:08:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| d11a95d4-f415-3950-8e0d-b364449a0d1a | -11.36475 | -45.08516 | 2025-09-29 04:08:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 31253268-eae2-305f-a441-4eca07e5a80a | -12.73952 | -48.36559 | 2025-09-29 04:08:00 | NOAA-20 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 4f2f5ec9-f1ea-3d2e-9a24-68ff7fe63659 | -11.91688 | -44.754 | 2025-09-29 04:08:00 | NOAA-20 | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 447edd4b-de99-345b-a6a0-0f1a692f7c9b | -15.25681 | -48.77093 | 2025-09-29 04:08:00 | NOAA-20 | VILA PROPÍCIO | GOIÁS | Brasil | 5222302 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| ad61cdec-2a6b-3f98-a816-c68cc7afb338 | -15.28473 | -49.49545 | 2025-09-29 04:08:00 | NOAA-20 | SANTA ISABEL | GOIÁS | Brasil | 5219357 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| f3ab34f6-86b9-372f-a2da-e1d17095d5a6 | -13.84464 | -47.94474 | 2025-09-29 04:08:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 397a22a4-22c1-318a-9ae1-b73deaf860b3 | -11.34985 | -45.06664 | 2025-09-29 04:08:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 5231a106-dfef-36da-b6cb-72a9a311c0f2 | -13.80024 | -47.94751 | 2025-09-29 04:08:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 4.3 |
| e37c6f16-48c7-3095-90c2-0b864611564b | -11.6495 | -45.33625 | 2025-09-29 04:08:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 55c7c00f-292c-3061-876b-14e49c3a6cb4 | -15.03637 | -46.96661 | 2025-09-29 04:08:00 | NOAA-20 | VILA BOA | GOIÁS | Brasil | 5222203 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 0421bb04-7fce-3b05-bb7e-df6c26ab37ed | -15.8693 | -46.21785 | 2025-09-29 04:08:00 | NOAA-20 | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 3.2 |
| c2295b61-843f-3b11-ad8c-2416d5af1a31 | -11.806 | -51.80067 | 2025-09-29 04:08:00 | NOAA-20 | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 294ec6b9-1bfd-3c3b-adeb-e7499ebf3494 | -15.17234 | -50.08551 | 2025-09-29 04:08:00 | NOAA-20 | ARAGUAPAZ | GOIÁS | Brasil | 5202155 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| c51187b7-54ba-389a-b8f2-07c6c0783f0b | -8.38778 | -47.99417 | 2025-09-29 04:08:00 | NOAA-20 | ITAPIRATINS | TOCANTINS | Brasil | 1710904 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| baa63564-dac9-3f0e-991b-1533d5278287 | -11.67332 | -44.29377 | 2025-09-29 04:08:00 | NOAA-20 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| e65c2033-32a4-396e-bbd9-35cfda7540ef | -16.42974 | -42.40931 | 2025-09-29 04:08:00 | NOAA-20 | RUBELITA | MINAS GERAIS | Brasil | 3156502 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 93e52869-c936-32bb-8ad4-7192a8c04d6c | -13.78544 | -47.87053 | 2025-09-29 04:08:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 0a2a35e4-3dca-3fca-8a30-c00a5b3634f8 | -15.28395 | -49.49956 | 2025-09-29 04:08:00 | NOAA-20 | SANTA ISABEL | GOIÁS | Brasil | 5219357 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| ec473b4d-49bb-31d9-9288-90f312f03845 | -13.38447 | -48.15049 | 2025-09-29 04:08:00 | NOAA-20 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 16.3 |
| 01084b87-4b8d-310d-9e68-e73b50064fb1 | -11.44242 | -47.28749 | 2025-09-29 04:08:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| f14db7aa-9aea-3047-9ec1-c1319421eb39 | -15.86617 | -46.8335 | 2025-09-29 04:08:00 | NOAA-20 | CABECEIRAS | GOIÁS | Brasil | 5204003 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| a5df5931-128c-3517-a13c-95620cd56088 | -11.41062 | -44.90331 | 2025-09-29 04:08:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| ef868991-48cd-35b6-82cd-1e80d08ea7b8 | -14.52076 | -48.39774 | 2025-09-29 04:08:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 0aa85606-fe41-3e37-9d20-a2af043a0764 | -11.91958 | -48.03612 | 2025-09-29 04:08:00 | NOAA-20 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 900fa44e-4c90-3afb-81d6-bdc9510066e0 | -9.05018 | -46.70728 | 2025-09-29 04:08:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 5.1 |
| aa4b521e-9b88-3b83-8890-8755b8511d82 | -14.44499 | -46.3713 | 2025-09-29 04:08:00 | NOAA-20 | BURITINÓPOLIS | GOIÁS | Brasil | 5203962 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| bbee132b-2f92-3a29-87e1-babce3532934 | -11.4325 | -46.63449 | 2025-09-29 04:08:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 5c95c86e-3b91-3270-94f3-cb4e7c302e02 | -9.51051 | -47.69285 | 2025-09-29 04:08:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 4fe71c73-a3aa-357e-8279-88f0a9a654bc | -9.96077 | -43.58171 | 2025-09-29 04:08:00 | NOAA-20 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 38a93a42-9d38-3536-a23e-ca8481fc218f | -15.27027 | -48.76593 | 2025-09-29 04:08:00 | NOAA-20 | VILA PROPÍCIO | GOIÁS | Brasil | 5222302 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |


[Clique aqui para ver as próximas entradas](README40.md)
