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

## Dados Diários - Página 21

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 1dae99ba-09e2-3a3a-85e8-3f9f1cb3c06f | -14.96023 | -47.53737 | 2026-09-20 03:47:00 | NOAA-21 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| f803be6d-a7e5-3388-b64a-f92040e326bb | -16.57572 | -51.6282 | 2026-09-20 03:47:00 | NOAA-21 | PIRANHAS | GOIÁS | Brasil | 5217203 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 89f89611-37d1-3d57-bcbb-c09ddf96188f | -15.17335 | -48.1586 | 2026-09-20 03:47:00 | NOAA-21 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 47ce8f43-c394-3c0d-b7ac-9520db986281 | -14.59514 | -48.10131 | 2026-09-20 03:47:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 7.2 |
| 2a163fa3-bb91-3177-8384-dc7c4c7eab57 | -13.96067 | -47.84679 | 2026-09-20 03:47:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 48ace2fa-9298-39b8-b68a-99b5fdfb4a6b | -14.6827 | -46.69707 | 2026-09-20 03:47:00 | NOAA-21 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 10.3 |
| 1fcfc464-8851-3a24-a798-562f0f848d59 | -15.46452 | -48.44158 | 2026-09-20 03:47:00 | NOAA-21 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 6166fab4-f8fa-30c1-bf1e-10abd0339ef2 | -14.11111 | -44.8366 | 2026-09-20 03:47:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 4.7 |
| aab8cd30-a6e6-33c6-ad4e-730a1a279dec | -14.69395 | -46.69582 | 2026-09-20 03:47:00 | NOAA-21 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 12.7 |
| b5c43c5a-fe64-3257-befb-1c3def49907c | -17.57792 | -45.38512 | 2026-09-20 03:47:00 | NOAA-21 | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| aec4ce0f-1836-3be5-85de-77dd43140b67 | -13.88525 | -48.58377 | 2026-09-20 03:47:00 | NOAA-21 | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 6.6 |
| c50caa03-0a7d-3149-9f03-42d256d49538 | -14.12372 | -45.60204 | 2026-09-20 03:47:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 84ee23d2-e3d8-3fa3-bf82-07db80084f8f | -15.86448 | -49.91642 | 2026-09-20 03:47:00 | NOAA-21 | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 3477a51c-8319-338d-b906-5f044efc2259 | -14.91787 | -49.91633 | 2026-09-20 03:47:00 | NOAA-21 | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| ab249815-51a0-34cb-90fc-fa6fd6574b56 | -13.94831 | -47.84853 | 2026-09-20 03:47:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| d07d5cc3-85ad-3786-9159-87b92087223d | -16.59813 | -45.33691 | 2026-09-20 03:47:00 | NOAA-21 | SANTA FÉ DE MINAS | MINAS GERAIS | Brasil | 3157609 | 31 | 33 | nan | nan | nan | Cerrado | 3.3 |
| af0465fa-6f6e-31ae-90a7-f72bd44a19cb | -15.8742 | -49.91573 | 2026-09-20 03:47:00 | NOAA-21 | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 82b71849-7b2e-3e40-ad27-3e181d5f012c | -13.8911 | -48.5859 | 2026-09-20 03:47:00 | NOAA-21 | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 3.7 |
| a0971b7b-a925-3306-a2ce-d44382a70775 | -20.2633 | -45.55991 | 2026-09-20 03:47:00 | NOAA-21 | ARCOS | MINAS GERAIS | Brasil | 3104205 | 31 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 2f6f6422-93f0-3ea1-9ff1-69a377c90e9c | -16.45275 | -46.73967 | 2026-09-20 03:47:00 | NOAA-21 | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 1aeec606-c445-3533-b31f-c1be7429ed7e | -16.82899 | -47.63668 | 2026-09-20 03:47:00 | NOAA-21 | CRISTALINA | GOIÁS | Brasil | 5206206 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| ac8bb20c-2eb1-3791-a887-15275828ea6d | -14.18441 | -47.87128 | 2026-09-20 03:47:00 | NOAA-21 | ALTO PARAÍSO DE GOIÁS | GOIÁS | Brasil | 5200605 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 55d5d6a2-4c17-33b4-9450-749a6fd6222c | -14.6978 | -46.6972 | 2026-09-20 03:47:00 | NOAA-21 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 10.5 |
| c8f2486e-1d60-37af-8412-48f2bdd1afbf | -20.26773 | -45.56083 | 2026-09-20 03:47:00 | NOAA-21 | ARCOS | MINAS GERAIS | Brasil | 3104205 | 31 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 7fc33981-665b-397c-92cb-2a49661dbf2f | -15.99416 | -46.74141 | 2026-09-20 03:47:00 | NOAA-21 | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| f1063204-feed-3351-847e-ff8174e197e6 | -14.69712 | -46.70057 | 2026-09-20 03:47:00 | NOAA-21 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 83c3670b-27b1-3652-a521-9798ca84b068 | -17.02233 | -47.14961 | 2026-09-20 03:47:00 | NOAA-21 | CRISTALINA | GOIÁS | Brasil | 5206206 | 52 | 33 | nan | nan | nan | Cerrado | 11.3 |
| e3221b98-d3a1-37ff-8542-83dae0a5690c | -14.1091 | -44.84708 | 2026-09-20 03:47:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 32fc3a27-1b02-334b-88e7-505b4d946265 | -14.80006 | -48.53466 | 2026-09-20 03:47:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 8e2b68e6-f740-3475-8dde-a3d718341830 | -15.47012 | -48.41497 | 2026-09-20 03:47:00 | NOAA-21 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 8b356465-7fe8-3082-b904-76e296faea95 | -13.7349 | -48.78553 | 2026-09-20 03:47:00 | NOAA-21 | FORMOSO | GOIÁS | Brasil | 5208103 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 67c9e2c6-6a57-35c7-b4f3-e94082342832 | -14.67809 | -46.69257 | 2026-09-20 03:47:00 | NOAA-21 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 8636c276-10c3-3fac-ba18-cca240ea8ed3 | -14.95671 | -47.53286 | 2026-09-20 03:47:00 | NOAA-21 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 2cfff293-694a-3089-9c89-a162e6f2c847 | -14.66954 | -46.68013 | 2026-09-20 03:47:00 | NOAA-21 | ALVORADA DO NORTE | GOIÁS | Brasil | 5200803 | 52 | 33 | nan | nan | nan | Cerrado | 7.2 |
| 70e1745b-ca67-39ad-b83d-7b2d7fef2866 | -16.82822 | -47.64038 | 2026-09-20 03:47:00 | NOAA-21 | CRISTALINA | GOIÁS | Brasil | 5206206 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 5edda90b-6a4d-306b-9e5c-13f8f2f6d406 | -17.02299 | -47.1464 | 2026-09-20 03:47:00 | NOAA-21 | CRISTALINA | GOIÁS | Brasil | 5206206 | 52 | 33 | nan | nan | nan | Cerrado | 7.4 |
| 1e1f1504-24df-3190-a720-307bc0bd8f37 | -15.86927 | -49.90819 | 2026-09-20 03:47:00 | NOAA-21 | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 0b6b78bc-f5b3-3116-ad44-edcf8d1cc05f | -15.06185 | -48.58489 | 2026-09-20 03:47:00 | NOAA-21 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| c0ab14b3-1921-3f24-b77f-03399e4e890c | -14.6728 | -46.69148 | 2026-09-20 03:47:00 | NOAA-21 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 6.2 |
| e91646a8-0a8a-357a-8b84-de3b804eecfe | -14.69329 | -46.69921 | 2026-09-20 03:47:00 | NOAA-21 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 8.2 |
| 066c6b5d-35e4-367f-bd18-c0157b736c84 | -14.76057 | -48.41066 | 2026-09-20 03:47:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 7.9 |
| fa6fb327-3491-3dfa-b314-a943f461f731 | -17.98738 | -49.20839 | 2026-09-20 03:47:00 | NOAA-21 | GOIATUBA | GOIÁS | Brasil | 5209101 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| a63f13d6-2631-3c9c-842f-1146a19ff233 | -15.87189 | -49.91258 | 2026-09-20 03:47:00 | NOAA-21 | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 2afd5d83-aadc-3d14-9c26-4eed1285ee49 | -17.01254 | -47.14346 | 2026-09-20 03:47:00 | NOAA-21 | CRISTALINA | GOIÁS | Brasil | 5206206 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 6a758c3d-a767-3416-8f55-0f5d6ac65341 | -15.17174 | -48.16656 | 2026-09-20 03:47:00 | NOAA-21 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 193938bb-e190-3779-a171-37e3ccd10e53 | -14.91943 | -49.91337 | 2026-09-20 03:47:00 | NOAA-21 | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| a7399733-c6f9-32c2-b081-2ed283249598 | -14.79924 | -48.53858 | 2026-09-20 03:47:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| c1d099cb-c75e-36f8-8081-e38f0d0935c5 | -14.18347 | -47.87589 | 2026-09-20 03:47:00 | NOAA-21 | ALTO PARAÍSO DE GOIÁS | GOIÁS | Brasil | 5200605 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| ccc066e4-3f7f-3335-a909-f61fdc48783c | -17.01647 | -47.15165 | 2026-09-20 03:47:00 | NOAA-21 | CRISTALINA | GOIÁS | Brasil | 5206206 | 52 | 33 | nan | nan | nan | Cerrado | 11.3 |
| 5bf53a01-73ee-31f9-8eb6-d35943715665 | -18.37504 | -49.39713 | 2026-09-20 03:47:00 | NOAA-21 | ITUMBIARA | GOIÁS | Brasil | 5211503 | 52 | 33 | nan | nan | nan | Cerrado | 8.7 |
| da9e9679-e00c-3f6e-83c4-2f2532442893 | -14.67876 | -46.68914 | 2026-09-20 03:47:00 | NOAA-21 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 617b41f2-1d1d-3ac2-b01e-839afa1cccb4 | -15.87125 | -49.89926 | 2026-09-20 03:47:00 | NOAA-21 | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| dd947ea9-7f0d-3c7f-9198-52dc12e011f7 | -20.33951 | -47.49393 | 2026-09-20 03:47:00 | NOAA-21 | CRISTAIS PAULISTA | SÃO PAULO | Brasil | 3513207 | 35 | 33 | nan | nan | nan | Cerrado | 9.3 |
| 039c2106-be07-3cd8-9323-9a2c4317f217 | -18.37403 | -49.40163 | 2026-09-20 03:47:00 | NOAA-21 | ITUMBIARA | GOIÁS | Brasil | 5211503 | 52 | 33 | nan | nan | nan | Cerrado | 7.3 |
| db988dbf-eacd-3d27-8225-4bacb647cfc6 | -18.37523 | -49.4016 | 2026-09-20 03:47:00 | NOAA-21 | ITUMBIARA | GOIÁS | Brasil | 5211503 | 52 | 33 | nan | nan | nan | Cerrado | 8.2 |
| 48b0586e-6c93-37f1-bf0e-bacb3455769e | -14.11011 | -44.84185 | 2026-09-20 03:47:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 48037315-ea86-38d3-995f-81156a7b05bf | -15.4683 | -48.4236 | 2026-09-20 03:47:00 | NOAA-21 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 4.7 |
| d46bf164-8793-3810-961f-fa8782cf1fba | -14.18528 | -47.86703 | 2026-09-20 03:47:00 | NOAA-21 | ALTO PARAÍSO DE GOIÁS | GOIÁS | Brasil | 5200605 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 2feb5a99-b56c-3a4c-8b42-464d1a312aa6 | -13.87796 | -48.583 | 2026-09-20 03:47:00 | NOAA-21 | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 5.1 |
| bb056cb6-848e-3246-a325-5438cfa5774c | -14.59608 | -48.09673 | 2026-09-20 03:47:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 6.0 |
| b0392e63-cf3d-3466-afce-305084f8d49d | -13.8864 | -48.5783 | 2026-09-20 03:47:00 | NOAA-21 | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 7.9 |
| 863e384e-eb94-37ef-9075-1d2b94aa86bc | -19.89322 | -40.82238 | 2026-09-20 03:47:00 | NOAA-21 | ITARANA | ESPÍRITO SANTO | Brasil | 3202900 | 32 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| ccf32773-1708-3e90-926c-2d4015b36494 | -13.88416 | -48.58342 | 2026-09-20 03:47:00 | NOAA-21 | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 6.4 |
| b38bc7be-66d3-34cb-9060-b2e46134c244 | -19.08323 | -46.65597 | 2026-09-20 03:47:00 | NOAA-21 | SERRA DO SALITRE | MINAS GERAIS | Brasil | 3166808 | 31 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 2d53eff3-5b44-337d-a789-8edfbe2f01a2 | -17.98836 | -49.20396 | 2026-09-20 03:47:00 | NOAA-21 | GOIATUBA | GOIÁS | Brasil | 5209101 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| bb072929-fc06-3c76-af84-a6af1451d029 | -13.72782 | -48.78736 | 2026-09-20 03:47:00 | NOAA-21 | FORMOSO | GOIÁS | Brasil | 5208103 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 39302750-c111-3e16-ac65-f138d7304951 | -15.99352 | -46.74463 | 2026-09-20 03:47:00 | NOAA-21 | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| af424cab-50f8-3b15-9be9-20696dc2b771 | -15.89787 | -48.06993 | 2026-09-20 03:47:00 | NOAA-21 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 1.1 |
| a3bf3a56-9fd4-3d83-a5f2-e51316e2047f | -14.69182 | -46.69951 | 2026-09-20 03:47:00 | NOAA-21 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 0aa9639a-2a10-37b6-914c-c4a191c73a74 | -13.74205 | -48.78178 | 2026-09-20 03:47:00 | NOAA-21 | CAMPINORTE | GOIÁS | Brasil | 5204706 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| bc2513b3-edc1-39c9-b6c2-c6a5afad5fb2 | -14.96092 | -47.53403 | 2026-09-20 03:47:00 | NOAA-21 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| c3f95e82-1ce6-3456-a254-32cfcb6feda9 | -15.87066 | -49.91834 | 2026-09-20 03:47:00 | NOAA-21 | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 3.4 |
| dcb317a0-ea0c-36b8-a680-4f320de947e0 | -14.95606 | -47.5361 | 2026-09-20 03:47:00 | NOAA-21 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 83a2b83c-84fc-3191-a9e9-d2d806a227a5 | -16.59444 | -45.3308 | 2026-09-20 03:47:00 | NOAA-21 | SANTA FÉ DE MINAS | MINAS GERAIS | Brasil | 3157609 | 31 | 33 | nan | nan | nan | Cerrado | 13.0 |
| 4010cce9-5def-394f-b905-d190856a6451 | -15.87643 | -49.90564 | 2026-09-20 03:47:00 | NOAA-21 | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| fa445958-eea2-35c2-ba13-513cc39c01de | -17.01779 | -47.14528 | 2026-09-20 03:47:00 | NOAA-21 | CRISTALINA | GOIÁS | Brasil | 5206206 | 52 | 33 | nan | nan | nan | Cerrado | 7.4 |
| 3a53cc26-37f1-3c45-9fba-539fbc3a0254 | -13.8901 | -48.58514 | 2026-09-20 03:47:00 | NOAA-21 | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 6d4fcb52-1418-3b02-8395-5b144657a1cb | -13.95093 | -47.83578 | 2026-09-20 03:47:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| cb143631-7d6e-3733-b5bf-00b3f003a06c | -14.78747 | -48.5358 | 2026-09-20 03:47:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| e7907819-1367-3ae4-9cc0-81a812525ea1 | -16.45337 | -46.73666 | 2026-09-20 03:47:00 | NOAA-21 | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 18766587-1497-3b82-8bed-09c6ca91f775 | -17.01258 | -47.14417 | 2026-09-20 03:47:00 | NOAA-21 | CRISTALINA | GOIÁS | Brasil | 5206206 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| a9ec2f5f-8e96-3299-9619-839ca20f40f5 | -18.66263 | -47.3609 | 2026-09-20 03:47:00 | NOAA-21 | MONTE CARMELO | MINAS GERAIS | Brasil | 3143104 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| fbb7406d-8724-3021-b43f-bc03c9cd41da | -15.45787 | -48.44432 | 2026-09-20 03:47:00 | NOAA-21 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 4547757e-a227-37c6-a242-ebc200a0a214 | -14.68932 | -46.69134 | 2026-09-20 03:47:00 | NOAA-21 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 6a941540-95a0-3fd3-9d31-c6245fa7b97e | -14.68866 | -46.69475 | 2026-09-20 03:47:00 | NOAA-21 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 34848b5a-5975-331b-bf74-ac7cb17a0f15 | -16.59492 | -45.33948 | 2026-09-20 03:47:00 | NOAA-21 | SANTA FÉ DE MINAS | MINAS GERAIS | Brasil | 3157609 | 31 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 0893c8ce-42f3-341c-bb86-71f68764045f | -15.17254 | -48.16261 | 2026-09-20 03:47:00 | NOAA-21 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 28e8751c-49c3-39fe-ab13-49b45f3cc4b0 | -14.6932 | -46.69275 | 2026-09-20 03:47:00 | NOAA-21 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 10.5 |
| ef2001ce-cd18-3c2d-bb2b-03f2faf4f2a0 | -16.09801 | -46.85067 | 2026-09-20 03:47:00 | NOAA-21 | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 7d104604-29ec-3455-84b5-4149f29f204a | -13.74824 | -48.78269 | 2026-09-20 03:47:00 | NOAA-21 | CAMPINORTE | GOIÁS | Brasil | 5204706 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 2d0d556e-82bf-3fd6-a258-d86ebc59ee33 | -14.12428 | -45.59909 | 2026-09-20 03:47:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| d56b9b1c-cbd7-3fca-8f3e-b865a4ffeef6 | -14.12315 | -45.605 | 2026-09-20 03:47:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 345284e1-3797-3260-ab46-ee6fa51c2782 | -13.73369 | -48.79148 | 2026-09-20 03:47:00 | NOAA-21 | FORMOSO | GOIÁS | Brasil | 5208103 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 53046b91-0e00-3ccf-8572-65b234d0a425 | -15.47207 | -48.43454 | 2026-09-20 03:47:00 | NOAA-21 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 57ca999c-ecf4-39ee-b469-8276a08d01a0 | -13.74141 | -48.78354 | 2026-09-20 03:47:00 | NOAA-21 | CAMPINORTE | GOIÁS | Brasil | 5204706 | 52 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 7c73169a-11c9-3362-a0ee-fbb9298f4e24 | -16.58377 | -51.62627 | 2026-09-20 03:47:00 | NOAA-21 | PIRANHAS | GOIÁS | Brasil | 5217203 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| fd452f1b-f909-3408-afb9-2061c75ea547 | -15.86673 | -49.90593 | 2026-09-20 03:47:00 | NOAA-21 | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| e5caeed2-6b1b-3ae6-8713-c0fc88a2e27d | -14.78655 | -48.54015 | 2026-09-20 03:47:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 7643b954-1b57-35f4-a0bf-4f3915ef5377 | -15.46923 | -48.41919 | 2026-09-20 03:47:00 | NOAA-21 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 3754345f-8242-3256-afb9-e93a1e96ff1c | -13.87906 | -48.58331 | 2026-09-20 03:47:00 | NOAA-21 | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 6.6 |


[Clique aqui para ver as próximas entradas](README22.md)
