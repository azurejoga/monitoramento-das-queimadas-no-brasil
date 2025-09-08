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
| dfce551d-6526-335e-b8e9-b9bb86da14e2 | -9.05832 | -50.466 | 2025-09-08 04:02:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 8399c380-ac4c-3599-8690-6a0813580330 | -14.79371 | -48.10382 | 2025-09-08 04:02:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| ac1af561-99ec-3a92-8901-856546f73aa7 | -13.83024 | -46.2412 | 2025-09-08 04:02:00 | NOAA-20 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 1a64efa2-7b69-3ee8-b666-d6e664b55cff | -11.282 | -46.50167 | 2025-09-08 04:02:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 94fe7bca-a59c-3372-92d5-db6b5bd01a75 | -11.20413 | -55.00627 | 2025-09-08 04:02:00 | NOAA-20 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 14.1 |
| 4948ba65-f3fc-31e5-b240-381c7a6889af | -12.83359 | -47.99252 | 2025-09-08 04:02:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| dd3a3905-13c0-3220-bb87-b1a686d60602 | -8.82735 | -45.89347 | 2025-09-08 04:02:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 48cb8fb3-9585-3c58-9e55-90ab901d79e5 | -15.38118 | -46.42551 | 2025-09-08 04:02:00 | NOAA-20 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 2.2 |
| e4be88ea-3e33-3628-a185-8c0a0abda748 | -9.81377 | -53.32999 | 2025-09-08 04:02:00 | NOAA-20 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 11.3 |
| 7bc472b4-3b8d-3877-8001-d42088b565bf | -10.13942 | -46.17751 | 2025-09-08 04:02:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 638182bb-e345-300a-a0a4-73a060ef8d52 | -11.90397 | -50.99017 | 2025-09-08 04:02:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| f3e7c553-cf53-3305-bcde-541745fac3b3 | -11.99909 | -47.7817 | 2025-09-08 04:02:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 12.6 |
| 0e4983cb-2815-3435-b834-2bb160ddbbfc | -11.61089 | -47.14475 | 2025-09-08 04:02:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| a071601e-0f3f-3edc-bac8-4c898bbee3cb | -12.81463 | -47.02926 | 2025-09-08 04:02:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 563587da-5ee6-3147-9428-4d381428e298 | -11.40986 | -43.58099 | 2025-09-08 04:02:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 1eaf1cda-b2da-3de4-9693-7323e9c3cae3 | -13.6466 | -43.80237 | 2025-09-08 04:02:00 | NOAA-20 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 9.7 |
| 6f6579b0-9d36-3e81-a100-d92d48253d33 | -10.80233 | -47.7338 | 2025-09-08 04:02:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 0ca95dc8-b4de-3fb0-a26b-237d362f1eed | -9.19385 | -46.04128 | 2025-09-08 04:02:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| ae5b0802-b7af-3a91-ae94-32b8358c9a50 | -14.2928 | -44.87943 | 2025-09-08 04:02:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 07fef0fd-a5d0-3e5a-a81d-6980d0a5237e | -11.86187 | -51.06097 | 2025-09-08 04:02:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 6.6 |
| e4645b05-ffe7-3bc5-8a36-1dafe5f0e0b3 | -12.60629 | -44.64568 | 2025-09-08 04:02:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 5376b88c-9adf-3dc8-91f0-a494fe24f8a7 | -9.0521 | -50.46851 | 2025-09-08 04:02:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 69d405c5-e127-334e-95ba-05762d21ff6c | -11.86594 | -51.06937 | 2025-09-08 04:02:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 72b5351c-004b-3ab2-bd61-cc29ca48d48a | -8.19413 | -50.13297 | 2025-09-08 04:02:00 | NOAA-20 | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 5a4ef8ae-8e6c-357c-8b44-374e8c3b0bf1 | -9.20146 | -46.0464 | 2025-09-08 04:02:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 398e8572-6905-3b07-b8b2-0eb047da62d6 | -9.15367 | -46.07633 | 2025-09-08 04:02:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 82360429-2ef7-3e11-8448-254146d7780d | -14.51527 | -48.80167 | 2025-09-08 04:02:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 98cb6c90-45ac-3dfe-b44c-1efca043a44d | -11.86789 | -50.97145 | 2025-09-08 04:02:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 328921fb-ec4b-30ad-a85f-d97c4c0f79cc | -13.03413 | -47.13741 | 2025-09-08 04:02:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 62a701da-a562-3a10-ac96-b0762b108030 | -14.81615 | -45.3064 | 2025-09-08 04:02:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 4c1b54d9-555f-39a7-9859-343b5c6e7c06 | -9.69858 | -43.51804 | 2025-09-08 04:02:00 | NOAA-20 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 7a09edd8-9b33-3255-9c4e-b7978b0e86b6 | -14.69416 | -44.78408 | 2025-09-08 04:02:00 | NOAA-20 | BONITO DE MINAS | MINAS GERAIS | Brasil | 3108255 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 470e240d-4133-362a-9267-55d87eb5ed47 | -15.29099 | -43.38594 | 2025-09-08 04:02:00 | NOAA-20 | JAÍBA | MINAS GERAIS | Brasil | 3135050 | 31 | 33 | nan | nan | nan | Caatinga | 3.9 |
| 009ede72-389f-3e91-9d26-da742cdbb959 | -11.40701 | -43.57647 | 2025-09-08 04:02:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| d0a27112-aec9-3580-bf15-c140125ad8a2 | -15.66673 | -48.21063 | 2025-09-08 04:02:00 | NOAA-20 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 2e6557f7-5402-3c7d-9fd2-deed8db34231 | -12.19417 | -53.90892 | 2025-09-08 04:02:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 0cbf16cc-8730-3253-8dc9-fb619933819b | -13.55191 | -48.10326 | 2025-09-08 04:02:00 | NOAA-20 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 7ac34b2c-c119-32de-b4de-c4e3f391fe18 | -12.16988 | -43.94082 | 2025-09-08 04:02:00 | NOAA-20 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| fc2b98bb-5b73-3bc3-b11f-e6620c7ef5ee | -12.83435 | -47.98842 | 2025-09-08 04:02:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| b469a03b-7ae8-3af3-9547-23f0d29011b9 | -9.82262 | -53.31951 | 2025-09-08 04:02:00 | NOAA-20 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 3.4 |
| bdd6e3ca-f1ff-30de-a5b1-fcf9257781e1 | -8.69711 | -45.30695 | 2025-09-08 04:02:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 5.0 |
| eebe8cae-f8ee-3bf0-a07e-a03187bf17af | -9.04644 | -50.46803 | 2025-09-08 04:02:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| e6a67447-b1ae-3043-af08-b137ff8aa252 | -13.80837 | -46.27388 | 2025-09-08 04:02:00 | NOAA-20 | GUARANI DE GOIÁS | GOIÁS | Brasil | 5209408 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 6bc5fed7-b239-3c5b-8bb9-2595995525f6 | -11.31793 | -46.53859 | 2025-09-08 04:02:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 66c51748-699b-3747-8557-3e24e7d3c393 | -7.67762 | -50.25837 | 2025-09-08 04:02:00 | NOAA-20 | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| bb59b4af-d50a-3312-81d7-f86a847a8213 | -14.8068 | -48.17735 | 2025-09-08 04:02:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 51ae87a9-a820-3317-87dd-7c1a2235f352 | -13.90563 | -53.96809 | 2025-09-08 04:02:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 3a61c5d8-acef-341f-be25-2aa72f7585f1 | -14.59073 | -48.07276 | 2025-09-08 04:02:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 172730fb-bef9-38cb-88fb-1bc0747b6c3d | -11.03192 | -45.95319 | 2025-09-08 04:02:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 8f227f6d-9254-3aaf-b9e4-04d21efd0925 | -9.4477 | -49.44179 | 2025-09-08 04:02:00 | NOAA-20 | ABREULÂNDIA | TOCANTINS | Brasil | 1700251 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 7339c14c-de72-384e-b287-d05ff35bda21 | -13.71541 | -46.88396 | 2025-09-08 04:02:00 | NOAA-20 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 5aeff793-a49b-3d22-86ab-f4348b2dbdeb | -14.29639 | -44.88005 | 2025-09-08 04:02:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 047e6447-c5f9-303c-abbc-039672376688 | -10.16179 | -46.21901 | 2025-09-08 04:02:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| c271f085-7696-3dd6-b27e-09e19a0e0803 | -11.40921 | -43.58495 | 2025-09-08 04:02:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| f733adaf-3514-3ad4-86fc-bc2039a65430 | -11.4127 | -43.58554 | 2025-09-08 04:02:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 331ca25b-b27e-341c-80ca-7db1ec770886 | -14.51312 | -48.79345 | 2025-09-08 04:02:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 0eb6e7c9-25ba-32f4-a1e1-76d6ce734ca6 | -13.70448 | -46.87506 | 2025-09-08 04:02:00 | NOAA-20 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 7.5 |
| 34075b0b-2153-310a-98d0-f7a936407cdd | -8.18079 | -50.14699 | 2025-09-08 04:02:00 | NOAA-20 | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 4be140a1-605c-3497-bc01-be0d97ca95b2 | -15.73087 | -48.37843 | 2025-09-08 04:02:00 | NOAA-20 | COCALZINHO DE GOIÁS | GOIÁS | Brasil | 5205513 | 52 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 9e55a01e-3b2e-32c6-8d2d-9f673658aeda | -9.70144 | -43.52267 | 2025-09-08 04:02:00 | NOAA-20 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| c8bd5f1f-9a9d-3d00-8563-d58cec7b9d93 | -11.61446 | -47.14938 | 2025-09-08 04:02:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 4.6 |
| ac2c82e2-364f-3b2d-ba18-4b5447fff2f7 | -14.51219 | -48.79829 | 2025-09-08 04:02:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 2b900895-f691-31eb-b989-70476bf97a4f | -12.45614 | -44.64701 | 2025-09-08 04:02:00 | NOAA-20 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| f4168aa0-7aab-3267-9d33-01a2452fb9cf | -9.85165 | -48.8465 | 2025-09-08 04:02:00 | NOAA-20 | BARROLÂNDIA | TOCANTINS | Brasil | 1703107 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 574bd9bc-1490-3c56-ad9d-7c721e5e1ebf | -15.1726 | -47.96338 | 2025-09-08 04:02:00 | NOAA-20 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 78294cc0-1cc8-3634-bd19-0bde79ddd9d8 | -14.5231 | -48.76585 | 2025-09-08 04:02:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 4.0 |
| ac7b25ff-e874-3b98-9d96-e1f37af7825f | -9.82729 | -47.77492 | 2025-09-08 04:02:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| f010bd93-cd4e-33fe-90ab-5ccbbac65e5a | -14.52388 | -53.98165 | 2025-09-08 04:02:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| e5a4e098-ccf4-37f4-b383-bb3c63c3d855 | -13.81421 | -46.28627 | 2025-09-08 04:02:00 | NOAA-20 | GUARANI DE GOIÁS | GOIÁS | Brasil | 5209408 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| fb5c223a-cc45-3d53-9871-da88eeee39eb | -12.00064 | -47.77292 | 2025-09-08 04:02:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 13.1 |
| 86d29d64-88a7-39f6-bd19-bff017314ae0 | -9.15845 | -46.07335 | 2025-09-08 04:02:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 38c672ce-561b-3825-bb2e-ecc59f4c515b | -7.67195 | -50.25765 | 2025-09-08 04:02:00 | NOAA-20 | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 7d9b3e44-5b22-3af5-bcab-9c7ab30a3fd4 | -14.77834 | -48.11465 | 2025-09-08 04:02:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| b1406938-9a5e-3bd0-94f4-62f6de33a43a | -14.60615 | -48.08574 | 2025-09-08 04:02:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| c3fc3606-3a54-3216-a76f-5627fc8196fd | -14.65158 | -46.84041 | 2025-09-08 04:02:00 | NOAA-20 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| f986824a-311c-3b05-bd5e-a30a6baca27d | -14.51076 | -48.80075 | 2025-09-08 04:02:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 05a373ce-c995-392c-97a5-21745a18beba | -12.82022 | -52.88844 | 2025-09-08 04:02:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 5e61de1b-f372-378e-a94b-917cfc889170 | -11.41065 | -50.36549 | 2025-09-08 04:02:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| b5e5a9a3-d0f8-3d6d-a7f8-fb528538c34b | -11.62304 | -47.15063 | 2025-09-08 04:02:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 43d09aef-7619-3b37-8989-a0da847155be | -15.42425 | -47.68487 | 2025-09-08 04:02:00 | NOAA-20 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 749a32b3-5237-3dda-8057-b5e1d323a81f | -11.37978 | -50.42218 | 2025-09-08 04:02:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 80284741-7152-38ca-8c67-71df0f9e1f44 | -14.99338 | -48.01802 | 2025-09-08 04:02:00 | NOAA-20 | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 3ea6ec45-9933-338e-9a9a-2744fbf6ef2f | -15.29436 | -43.38652 | 2025-09-08 04:02:00 | NOAA-20 | JAÍBA | MINAS GERAIS | Brasil | 3135050 | 31 | 33 | nan | nan | nan | Caatinga | 3.9 |
| 27370369-1841-31e4-961a-f5e77c28a8f4 | -10.28985 | -48.80761 | 2025-09-08 04:02:00 | NOAA-20 | PARAÍSO DO TOCANTINS | TOCANTINS | Brasil | 1716109 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 3de78163-0ccb-3c24-9ec6-36b04817f2da | -11.57228 | -44.6577 | 2025-09-08 04:02:00 | NOAA-20 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 5.9 |
| be22b4fc-670a-3b7d-835e-d4b9f9d98b20 | -12.94526 | -54.78655 | 2025-09-08 04:02:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 6.2 |
| b151fd60-36e9-3a80-9a7c-75e8bf8fca53 | -12.19943 | -53.91613 | 2025-09-08 04:02:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 9ebd5605-1331-376f-813e-81cc1559e5a5 | -14.51971 | -48.77758 | 2025-09-08 04:02:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 040b2ff4-81d2-3b4d-bd7d-cb9de354c47d | -9.19823 | -46.06508 | 2025-09-08 04:02:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 19d1f002-95cc-31b9-a4ad-855ea0377c01 | -13.81222 | -46.27486 | 2025-09-08 04:02:00 | NOAA-20 | GUARANI DE GOIÁS | GOIÁS | Brasil | 5209408 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| d9e20a42-eb5c-37c9-8ef4-d95b02e72428 | -9.20014 | -46.05406 | 2025-09-08 04:02:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 2a77bebd-7831-31d1-88d1-71d0ac608087 | -9.6979 | -43.52207 | 2025-09-08 04:02:00 | NOAA-20 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| cf90e1ac-cdde-3248-9f47-d9ef939ec9ec | -8.69401 | -45.30113 | 2025-09-08 04:02:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 279d9548-12ec-3090-b869-5af185edf269 | -13.00749 | -45.21397 | 2025-09-08 04:02:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 8d98de67-37e7-32c8-8485-ef5388b40355 | -11.38042 | -50.41879 | 2025-09-08 04:02:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| eaf1c15f-901c-3f75-a606-5e37eb34117a | -8.92885 | -45.81163 | 2025-09-08 04:02:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 93c61a0d-98ca-39c5-b300-df2b8727227f | -11.24626 | -47.56385 | 2025-09-08 04:02:00 | NOAA-20 | PINDORAMA DO TOCANTINS | TOCANTINS | Brasil | 1717008 | 17 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 69333441-dd83-349b-a5fe-de099359087c | -11.40137 | -50.39502 | 2025-09-08 04:02:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 5.2 |
| b42570da-5eee-35d5-aee2-71929d1c774c | -16.08148 | -43.63241 | 2025-09-08 04:02:00 | NOAA-20 | CAPITÃO ENÉAS | MINAS GERAIS | Brasil | 3112703 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 37d782a8-85f3-3ae0-95b8-ef7acb99244f | -9.95863 | -51.19258 | 2025-09-08 04:02:00 | NOAA-20 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 4.2 |


[Clique aqui para ver as próximas entradas](README39.md)
