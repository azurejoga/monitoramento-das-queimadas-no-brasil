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

## Dados Diários - Página 18

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 0cb6e53d-d938-32c0-a932-e58d1d76433f | -7.3322 | -48.5074 | 2025-09-06 02:10:00 | GOES-19 | ARAGUAÍNA | TOCANTINS | Brasil | 1702109 | 17 | 33 | nan | nan | nan | Cerrado | 49.3 |
| 09eeb0e4-270d-31d8-b622-6e33b171bb80 | -9.7041 | -49.4825 | 2025-09-06 02:10:00 | GOES-19 | MARIANÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1712504 | 17 | 33 | nan | nan | nan | Cerrado | 109.7 |
| 7574e398-1778-3707-9d55-2afa9bdca6cb | -10.6131 | -44.3051 | 2025-09-06 02:10:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 83.0 |
| 241f49fa-e979-3058-af6b-74b21600767a | -22.2424 | -48.7513 | 2025-09-06 02:20:00 | GOES-19 | ITAPUÍ | SÃO PAULO | Brasil | 3522901 | 35 | 33 | nan | nan | nan | Mata Atlântica | 201.8 |
| dcfaa40d-7d6e-35af-88a8-3d228ae923d2 | -16.8927 | -49.6127 | 2025-09-06 02:20:00 | GOES-19 | GUAPÓ | GOIÁS | Brasil | 5209200 | 52 | 33 | nan | nan | nan | Cerrado | 83.6 |
| cdd5c007-93d2-37db-8336-375272692b86 | -16.8729 | -49.6162 | 2025-09-06 02:20:00 | GOES-19 | GUAPÓ | GOIÁS | Brasil | 5209200 | 52 | 33 | nan | nan | nan | Cerrado | 61.5 |
| 10d2d5ad-0297-382f-8db0-bd9db390fa1d | -22.2633 | -48.7463 | 2025-09-06 02:20:00 | GOES-19 | ITAPUÍ | SÃO PAULO | Brasil | 3522901 | 35 | 33 | nan | nan | nan | Mata Atlântica | 190.0 |
| f7e4bb5e-383b-38d6-98d7-a08d5edbd058 | -4.5031 | -42.8854 | 2025-09-06 02:20:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 148.0 |
| 110ca8e0-9cec-3bf6-afc9-fd57bba1f0dd | -4.5033 | -42.862 | 2025-09-06 02:20:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 46.5 |
| dfe8f97c-61e8-311a-9ae0-3695f5c91f68 | -10.6131 | -44.3051 | 2025-09-06 02:20:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 93.6 |
| dda3a801-08fe-34a0-b844-0fd96ef422d2 | -9.7038 | -49.504 | 2025-09-06 02:20:00 | GOES-19 | MARIANÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1712504 | 17 | 33 | nan | nan | nan | Cerrado | 66.1 |
| ac2ce872-89fa-395b-8216-0ea3de63c7e1 | -16.8922 | -49.635 | 2025-09-06 02:20:00 | GOES-19 | GUAPÓ | GOIÁS | Brasil | 5209200 | 52 | 33 | nan | nan | nan | Cerrado | 295.2 |
| 6e1cde08-3450-3120-b81f-1870e430a194 | -4.5029 | -42.9089 | 2025-09-06 02:20:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 62.0 |
| a2f53a5e-447b-3423-b41c-7baf8c8ea38b | -12.5036 | -53.8505 | 2025-09-06 02:20:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 70.7 |
| 840ee082-13d6-31fb-a34d-00399d2b288b | -13.0235 | -54.8262 | 2025-09-06 02:20:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 57.0 |
| 7e288905-e1c7-3ac0-9468-3e9e9628bdcb | -10.5937 | -44.331 | 2025-09-06 02:20:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 177.4 |
| eb0b7fec-71c8-3061-b93c-77831639735f | -10.6128 | -44.3284 | 2025-09-06 02:20:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 249.6 |
| cfc5404d-b9f9-3fde-ae48-0d6961c81f8c | -15.5747 | -52.9175 | 2025-09-06 02:20:00 | GOES-19 | GENERAL CARNEIRO | MATO GROSSO | Brasil | 5103908 | 51 | 33 | nan | nan | nan | Cerrado | 77.4 |
| 48bafb33-c59a-3189-a87f-89b0a49646f9 | -13.0047 | -54.8076 | 2025-09-06 02:20:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 47.4 |
| 7a5dc1b1-0ca5-3735-aa6d-699cc61dbb6e | -13.0044 | -54.8282 | 2025-09-06 02:20:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 87.4 |
| d47387fd-44ad-3a44-ad97-c8d9498fe3d0 | -15.5558 | -49.8134 | 2025-09-06 02:20:00 | GOES-19 | ITAPURANGA | GOIÁS | Brasil | 5211206 | 52 | 33 | nan | nan | nan | Cerrado | 47.2 |
| e2806f2e-65b1-3d83-a622-d85a435fc0f1 | -12.9668 | -54.791 | 2025-09-06 02:20:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 55.4 |
| ed74e1ae-6772-3480-ae54-d1b2e655cc8a | -3.2516 | -50.8082 | 2025-09-06 02:20:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 49.4 |
| a03396dd-2e07-3d95-b512-8b84de61b845 | -12.4846 | -53.8525 | 2025-09-06 02:20:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 56.8 |
| 28ffbded-046a-355e-91dd-f4bb5a65e378 | -12.9665 | -54.8116 | 2025-09-06 02:20:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | 70.4 |
| 20cbcb08-3ae4-35ec-a2c0-0a64179a76e6 | -14.9015 | -49.454 | 2025-09-06 02:20:00 | GOES-19 | ITAPACI | GOIÁS | Brasil | 5210901 | 52 | 33 | nan | nan | nan | Cerrado | 138.0 |
| 01533e88-9511-3d6a-804d-afbc823f16ac | -16.8724 | -49.6385 | 2025-09-06 02:20:00 | GOES-19 | GUAPÓ | GOIÁS | Brasil | 5209200 | 52 | 33 | nan | nan | nan | Cerrado | 211.8 |
| 534e7658-5509-381c-a3c5-6cb22be5d760 | -10.594 | -44.3077 | 2025-09-06 02:20:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 71.1 |
| bcd94e8c-c166-3a42-986e-b28f7b5fa100 | -9.7041 | -49.4825 | 2025-09-06 02:20:00 | GOES-19 | MARIANÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1712504 | 17 | 33 | nan | nan | nan | Cerrado | 90.0 |
| 3bf29012-4141-3998-a3a7-e6fc9b55cf4b | -4.5218 | -42.8843 | 2025-09-06 02:20:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 60.0 |
| 71f58442-165d-3038-8661-b29f797b2f35 | -4.5218 | -42.8843 | 2025-09-06 02:30:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 32.7 |
| 2ceef623-1828-349f-9140-189c424a03f0 | -10.6128 | -44.3284 | 2025-09-06 02:30:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 205.3 |
| 6a060a00-312a-3437-b99b-f458a1dbe5d2 | -9.0951 | -47.0093 | 2025-09-06 02:30:00 | GOES-19 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 77.4 |
| e8a569ca-b104-3864-a1e8-386c60792ceb | -9.0762 | -47.0113 | 2025-09-06 02:30:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 58.1 |
| f4c6d796-a2ea-3316-bf47-2465b2ae5442 | -16.8724 | -49.6385 | 2025-09-06 02:30:00 | GOES-19 | GUAPÓ | GOIÁS | Brasil | 5209200 | 52 | 33 | nan | nan | nan | Cerrado | 66.3 |
| 1d722675-1427-3299-8e8b-46e9aadfa508 | -9.7038 | -49.504 | 2025-09-06 02:30:00 | GOES-19 | MARIANÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1712504 | 17 | 33 | nan | nan | nan | Cerrado | 66.1 |
| 539fefaa-7a10-3ed8-a69d-bfff92359f61 | -14.9015 | -49.454 | 2025-09-06 02:30:00 | GOES-19 | ITAPACI | GOIÁS | Brasil | 5210901 | 52 | 33 | nan | nan | nan | Cerrado | 467.1 |
| cc9f883b-ae9a-3108-9731-a2a36c9ded04 | -16.8922 | -49.635 | 2025-09-06 02:30:00 | GOES-19 | GUAPÓ | GOIÁS | Brasil | 5209200 | 52 | 33 | nan | nan | nan | Cerrado | 101.6 |
| eecf5149-43ef-30bd-a658-d223fce30f96 | -14.9019 | -49.4319 | 2025-09-06 02:30:00 | GOES-19 | ITAPACI | GOIÁS | Brasil | 5210901 | 52 | 33 | nan | nan | nan | Cerrado | 135.3 |
| 16243a8c-71ce-3564-97de-63fdd977c5c5 | -14.882 | -49.457 | 2025-09-06 02:30:00 | GOES-19 | ITAPACI | GOIÁS | Brasil | 5210901 | 52 | 33 | nan | nan | nan | Cerrado | 134.7 |
| d31a3bf8-44d1-3f4d-9eb3-26cb04c9df30 | -13.0047 | -54.8076 | 2025-09-06 02:30:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 45.3 |
| 89afc7b6-0e27-317c-9fac-f1c970bff305 | -22.2424 | -48.7513 | 2025-09-06 02:30:00 | GOES-19 | ITAPUÍ | SÃO PAULO | Brasil | 3522901 | 35 | 33 | nan | nan | nan | Mata Atlântica | 260.3 |
| e8729f43-4774-3ea0-b404-e0fbc7875f3d | -22.2633 | -48.7463 | 2025-09-06 02:30:00 | GOES-19 | ITAPUÍ | SÃO PAULO | Brasil | 3522901 | 35 | 33 | nan | nan | nan | Mata Atlântica | 235.2 |
| 2fa04708-4e4b-3588-85c9-ff8de2aa15f8 | -4.5029 | -42.9089 | 2025-09-06 02:30:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 57.2 |
| aa593fcd-3e13-3cb0-a583-4a5511c223ad | -10.594 | -44.3077 | 2025-09-06 02:30:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 79.1 |
| e668a0d6-0449-31e9-a47a-349201f700ce | -12.9665 | -54.8116 | 2025-09-06 02:30:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | 57.2 |
| 24688107-0224-34f3-9654-9c42eb32e270 | -15.5747 | -52.9175 | 2025-09-06 02:30:00 | GOES-19 | GENERAL CARNEIRO | MATO GROSSO | Brasil | 5103908 | 51 | 33 | nan | nan | nan | Cerrado | 64.5 |
| 0044500b-5c5a-3e93-9d5a-0909d7b1f0b4 | -22.2431 | -48.7279 | 2025-09-06 02:30:00 | GOES-19 | ITAPUÍ | SÃO PAULO | Brasil | 3522901 | 35 | 33 | nan | nan | nan | Mata Atlântica | 81.3 |
| 804cbf55-cf9e-36ea-83e5-f8b9726e12a5 | -13.0044 | -54.8282 | 2025-09-06 02:30:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 89.2 |
| 8fe1f6b4-d1d6-3d8f-a1bf-4cf9eb9040c3 | -12.5036 | -53.8505 | 2025-09-06 02:30:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 64.2 |
| ad312590-7352-3f97-a3b0-dc797ad552ac | -14.901 | -49.4761 | 2025-09-06 02:30:00 | GOES-19 | ITAPACI | GOIÁS | Brasil | 5210901 | 52 | 33 | nan | nan | nan | Cerrado | 63.6 |
| 72c8a169-07f1-3c3d-836e-daa2eb95c2af | -10.6131 | -44.3051 | 2025-09-06 02:30:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 86.6 |
| d15040ff-9b1e-3142-9c3f-02e664807c92 | -4.5031 | -42.8854 | 2025-09-06 02:30:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 183.5 |
| 805b21fa-7b42-31be-8902-7a2395bbee6b | -4.5033 | -42.862 | 2025-09-06 02:30:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 32.9 |
| d3b0315a-c3ad-3b8a-a72d-ae33285b8911 | -5.4917 | -60.138 | 2025-09-06 02:30:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 39.9 |
| 05d2496e-3b3a-3a96-9891-30557759238d | -10.5937 | -44.331 | 2025-09-06 02:30:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 190.0 |
| 7bfdc035-c00d-3b6f-aed2-d529bded5d8b | -9.7041 | -49.4825 | 2025-09-06 02:30:00 | GOES-19 | MARIANÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1712504 | 17 | 33 | nan | nan | nan | Cerrado | 87.0 |
| 1f2aec1b-76a3-304c-9295-65052f9b3a64 | -14.9209 | -49.451 | 2025-09-06 02:30:00 | GOES-19 | ITAPACI | GOIÁS | Brasil | 5210901 | 52 | 33 | nan | nan | nan | Cerrado | 54.1 |
| 73c02af6-3604-359e-b067-d97f265137b7 | -22.2424 | -48.7513 | 2025-09-06 02:40:00 | GOES-19 | ITAPUÍ | SÃO PAULO | Brasil | 3522901 | 35 | 33 | nan | nan | nan | Mata Atlântica | 370.2 |
| 0b61ccc1-adb2-328f-b017-eb628c83d373 | -22.264 | -48.7228 | 2025-09-06 02:40:00 | GOES-19 | ITAPUÍ | SÃO PAULO | Brasil | 3522901 | 35 | 33 | nan | nan | nan | Mata Atlântica | 162.0 |
| 4030f165-99d1-3ad9-b4fc-e27bc6bda265 | -10.594 | -44.3077 | 2025-09-06 02:40:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 78.3 |
| c9ee9e97-c04a-362c-985c-db9a464d2ca5 | -12.9665 | -54.8116 | 2025-09-06 02:40:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | 51.7 |
| bbff9e57-2ac8-322e-b137-633d3481bd6e | -12.9668 | -54.791 | 2025-09-06 02:40:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 51.8 |
| a8fad144-e7b9-3949-a627-77547793e3f8 | -15.5942 | -52.9149 | 2025-09-06 02:40:00 | GOES-19 | GENERAL CARNEIRO | MATO GROSSO | Brasil | 5103908 | 51 | 33 | nan | nan | nan | Cerrado | 45.0 |
| 24f2249f-e142-32c1-b66f-3d8277469dd2 | -16.8922 | -49.635 | 2025-09-06 02:40:00 | GOES-19 | GUAPÓ | GOIÁS | Brasil | 5209200 | 52 | 33 | nan | nan | nan | Cerrado | 66.8 |
| 46915ec8-255e-3213-871a-2193fb484e02 | -22.2431 | -48.7279 | 2025-09-06 02:40:00 | GOES-19 | ITAPUÍ | SÃO PAULO | Brasil | 3522901 | 35 | 33 | nan | nan | nan | Mata Atlântica | 141.2 |
| b3c6c9e5-df0d-3374-b32e-582151438b1a | -10.6131 | -44.3051 | 2025-09-06 02:40:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 85.5 |
| 26e18d81-cd37-371e-952f-0562123ecc2f | -9.7038 | -49.504 | 2025-09-06 02:40:00 | GOES-19 | MARIANÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1712504 | 17 | 33 | nan | nan | nan | Cerrado | 63.6 |
| 0cb6853a-6047-3356-a40f-25b598476746 | -4.5031 | -42.8854 | 2025-09-06 02:40:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 62.5 |
| 0f0efbee-9ef0-3b28-919c-0a434b022691 | -10.5937 | -44.331 | 2025-09-06 02:40:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 198.6 |
| 7d67daf3-4810-3fec-8970-7b6f088a8162 | -10.6128 | -44.3284 | 2025-09-06 02:40:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 225.5 |
| b5b84da7-8f1a-3e8e-ac93-dd60841de253 | -9.7041 | -49.4825 | 2025-09-06 02:40:00 | GOES-19 | MARIANÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1712504 | 17 | 33 | nan | nan | nan | Cerrado | 79.2 |
| 5996165a-93ba-3aaf-9c13-d231cf82b332 | -22.2633 | -48.7463 | 2025-09-06 02:40:00 | GOES-19 | ITAPUÍ | SÃO PAULO | Brasil | 3522901 | 35 | 33 | nan | nan | nan | Mata Atlântica | 405.8 |
| f113f1a0-89d9-33ad-9905-d2fa44297406 | -13.0044 | -54.8282 | 2025-09-06 02:40:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 88.9 |
| 604ede38-45d2-3b8f-b4e0-de47d7928b20 | -10.594 | -44.3077 | 2025-09-06 02:50:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 54.5 |
| ba891e72-61e4-3061-b39d-bf099c0be3d7 | -3.2516 | -50.8082 | 2025-09-06 02:50:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 45.9 |
| 8b48d571-5455-3066-b592-e51be28820fb | -12.5033 | -53.8712 | 2025-09-06 02:50:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 37.7 |
| 1e68abe1-affd-3309-a238-47f646c27b91 | -22.2633 | -48.7463 | 2025-09-06 02:50:00 | GOES-19 | ITAPUÍ | SÃO PAULO | Brasil | 3522901 | 35 | 33 | nan | nan | nan | Mata Atlântica | 100.8 |
| 123aee11-d000-306a-9d03-4fe6b5dfd376 | -10.6128 | -44.3284 | 2025-09-06 02:50:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 272.1 |
| a7841f84-7ca0-3091-8c5a-901cbb0b5b26 | -13.0044 | -54.8282 | 2025-09-06 02:50:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 71.3 |
| 3b82a35a-ddbe-3319-9a77-3cf2e11783fd | -12.9473 | -46.5611 | 2025-09-06 02:50:00 | GOES-19 | NOVO ALEGRE | TOCANTINS | Brasil | 1715150 | 17 | 33 | nan | nan | nan | Cerrado | 65.3 |
| 41bd0191-d3e7-3f23-b2f1-769ade8f4d9b | -22.2424 | -48.7513 | 2025-09-06 02:50:00 | GOES-19 | ITAPUÍ | SÃO PAULO | Brasil | 3522901 | 35 | 33 | nan | nan | nan | Mata Atlântica | 126.4 |
| 9922247e-6c3c-39ee-9222-9cab86c1978c | -10.5937 | -44.331 | 2025-09-06 02:50:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 197.4 |
| 5c55902d-764f-3dec-b5ad-ec6b0b1ee7a7 | -10.6131 | -44.3051 | 2025-09-06 02:50:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 68.5 |
| 5a35ab45-1e21-3d67-ac55-6d4bcf69b86e | -9.7041 | -49.4825 | 2025-09-06 02:50:00 | GOES-19 | MARIANÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1712504 | 17 | 33 | nan | nan | nan | Cerrado | 77.7 |
| 21e5abac-98e4-3b38-a21b-1d0cba3c95ad | -12.9665 | -54.8116 | 2025-09-06 02:50:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | 70.2 |
| 5cfefebe-c619-38d8-af51-1dde961ddf18 | -12.9665 | -54.8116 | 2025-09-06 03:00:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | 62.0 |
| a6a7d639-5b15-3da3-95c8-06fba8556938 | -10.594 | -44.3077 | 2025-09-06 03:00:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 76.7 |
| 8ca6b9f7-d637-39ad-a43b-f2468a06a58d | -13.0044 | -54.8282 | 2025-09-06 03:00:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 49.2 |
| d555e8b6-1d41-3442-85a9-44f9e38dfbae | -10.5937 | -44.331 | 2025-09-06 03:00:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 211.5 |
| f49ccdba-b169-3809-a8a0-c6cb90b52379 | -10.314 | -46.4022 | 2025-09-06 03:00:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 52.6 |
| 248940d1-e439-3404-a4a6-180458eb41ab | -4.5031 | -42.8854 | 2025-09-06 03:00:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 78.6 |
| 8901a5bc-2404-37b1-a790-d1e0602cd273 | -22.2633 | -48.7463 | 2025-09-06 03:00:00 | GOES-19 | ITAPUÍ | SÃO PAULO | Brasil | 3522901 | 35 | 33 | nan | nan | nan | Mata Atlântica | 98.9 |
| f7fe07ab-dd01-3cc7-93e3-27f110490dbc | -3.2516 | -50.8082 | 2025-09-06 03:00:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 38.1 |
| c52bf7c2-b95b-34ee-ba52-6f0ac1fb506e | -22.2424 | -48.7513 | 2025-09-06 03:00:00 | GOES-19 | ITAPUÍ | SÃO PAULO | Brasil | 3522901 | 35 | 33 | nan | nan | nan | Mata Atlântica | 77.3 |
| 8c867309-1aa0-3a1c-b041-a8f2ae586bfe | -9.7041 | -49.4825 | 2025-09-06 03:00:00 | GOES-19 | MARIANÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1712504 | 17 | 33 | nan | nan | nan | Cerrado | 76.7 |
| 9ff80af9-c1c5-3524-bb1d-b504db8bc754 | -15.5747 | -52.9175 | 2025-09-06 03:00:00 | GOES-19 | GENERAL CARNEIRO | MATO GROSSO | Brasil | 5103908 | 51 | 33 | nan | nan | nan | Cerrado | 84.1 |
| 93e2e9e0-97fa-3d1a-ad1b-98aaa13f59c8 | -10.6128 | -44.3284 | 2025-09-06 03:00:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 215.9 |
| d7740029-54db-3aff-9dec-15d56e18ab88 | -10.6131 | -44.3051 | 2025-09-06 03:00:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 80.4 |
| 9908723a-e958-34ad-8b27-618b45dc00c2 | -12.5036 | -53.8505 | 2025-09-06 03:10:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 52.7 |


[Clique aqui para ver as próximas entradas](README19.md)
