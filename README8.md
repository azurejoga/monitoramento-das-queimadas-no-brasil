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
| c4ee35b8-e0f4-3c4d-84c3-2256123e810e | -11.62641 | -54.93893 | 2025-05-10 05:10:00 | NOAA-20 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| b5909629-ac18-3a9e-9f70-5662ebb9689d | -13.04245 | -53.72507 | 2025-05-10 05:10:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 616f23e2-5a62-3159-b986-fc83a799ec1c | -13.3766 | -54.26246 | 2025-05-10 05:10:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| b4d24785-7667-33b8-8998-b9da5baae167 | -10.98568 | -44.43388 | 2025-05-10 05:10:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 544bc63d-75f9-3a56-91ae-56475d841fa2 | -12.6481 | -54.07017 | 2025-05-10 05:10:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 08fcd9f4-aa98-3625-be85-7e7871b408c5 | -13.97847 | -56.80385 | 2025-05-10 05:10:00 | NOAA-20 | DIAMANTINO | MATO GROSSO | Brasil | 5103502 | 51 | 33 | nan | nan | nan | Cerrado | 10.2 |
| 1eadb6b9-e063-3b0d-9a4c-4ff7d446cbac | -12.68415 | -58.12635 | 2025-05-10 05:10:00 | NOAA-20 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 80de041b-53c8-3205-a721-90361c79543e | -10.98793 | -44.44062 | 2025-05-10 05:10:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 80bc4e31-1c22-3e60-9e17-a1f100737b35 | -13.61886 | -54.88523 | 2025-05-10 05:10:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| f5c95079-ca06-3ce3-b49d-8debce86fd05 | -8.4672 | -49.61488 | 2025-05-10 05:10:00 | NOAA-20 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 9b0bba77-bbc6-361c-9b79-a6c6d56309c2 | -13.98353 | -56.80804 | 2025-05-10 05:10:00 | NOAA-20 | DIAMANTINO | MATO GROSSO | Brasil | 5103502 | 51 | 33 | nan | nan | nan | Cerrado | 17.7 |
| 754cb483-49b5-31bb-89bb-35ef5714ea12 | -11.62273 | -54.93836 | 2025-05-10 05:10:00 | NOAA-20 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| e3b57b34-00c2-3341-bad7-81ae88974f37 | -10.99118 | -44.44876 | 2025-05-10 05:10:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 4fbe5008-13c5-39fc-af3f-240ccf6874da | -11.61281 | -48.12385 | 2025-05-10 05:10:00 | NOAA-20 | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 6d6ba7c7-5989-36d9-9071-ce7275083151 | -13.97789 | -56.80771 | 2025-05-10 05:10:00 | NOAA-20 | DIAMANTINO | MATO GROSSO | Brasil | 5103502 | 51 | 33 | nan | nan | nan | Cerrado | 15.7 |
| 8a6b0f9b-2c78-3711-9dd4-c658d6367d83 | -8.69724 | -64.14429 | 2025-05-10 05:10:00 | NOAA-20 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 908174b2-dbe2-33f3-9cf6-cbae56cb618d | -11.37986 | -55.11877 | 2025-05-10 05:10:00 | NOAA-20 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| d50e6664-4867-32a3-919c-c2ead7f058a0 | -12.6908 | -58.14927 | 2025-05-10 05:10:00 | NOAA-20 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 328c0fff-8609-3b04-8aeb-e2b9a9b15616 | -12.6449 | -54.06455 | 2025-05-10 05:10:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 05ad86d0-f2b4-3a95-9d87-a46d6ffa7512 | -13.05508 | -53.72305 | 2025-05-10 05:10:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 1a8c6c35-cf02-3daf-a3a8-f2f4c3c1f442 | -19.06518 | -53.45329 | 2025-05-10 05:12:00 | NOAA-20 | CAMAPUÃ | MATO GROSSO DO SUL | Brasil | 5002605 | 50 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 1f5f7f88-d009-3a73-ac73-5280820e6c5f | -19.05341 | -53.45416 | 2025-05-10 05:12:00 | NOAA-20 | CAMAPUÃ | MATO GROSSO DO SUL | Brasil | 5002605 | 50 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 9f1bfa93-4366-3dff-a4a4-e3cdd472455c | -19.06071 | -53.45269 | 2025-05-10 05:12:00 | NOAA-20 | CAMAPUÃ | MATO GROSSO DO SUL | Brasil | 5002605 | 50 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 395e9fe1-8d93-3f6c-84da-a5ab212b7ece | -17.53249 | -52.117 | 2025-05-10 05:12:00 | NOAA-20 | PEROLÂNDIA | GOIÁS | Brasil | 5216452 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 8375c958-d541-3752-b308-2fb026be7333 | -15.37128 | -60.09637 | 2025-05-10 05:12:00 | NOAA-20 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| c6c87eb4-aa30-36a5-8569-1e5617f532c1 | -16.30378 | -53.83152 | 2025-05-10 05:12:00 | NOAA-20 | GUIRATINGA | MATO GROSSO | Brasil | 5104203 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 0aa9704d-2f8e-3308-821d-78a2f8a60e14 | -15.42933 | -60.19903 | 2025-05-10 05:12:00 | NOAA-20 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| f3c0212c-72df-381c-a031-577d66b1e4f6 | -15.37461 | -60.09694 | 2025-05-10 05:12:00 | NOAA-20 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 1243fd19-8cdd-349a-a2f6-d1bd84a47bb6 | -19.05787 | -53.45481 | 2025-05-10 05:12:00 | NOAA-20 | CAMAPUÃ | MATO GROSSO DO SUL | Brasil | 5002605 | 50 | 33 | nan | nan | nan | Cerrado | 2.3 |
| ae7c32f8-215d-3ecb-97f4-f30d88692bc6 | -19.06233 | -53.45545 | 2025-05-10 05:12:00 | NOAA-20 | CAMAPUÃ | MATO GROSSO DO SUL | Brasil | 5002605 | 50 | 33 | nan | nan | nan | Cerrado | 2.3 |
| b829131d-58b8-3749-a97d-67fda9fcc088 | -13.9902 | -56.8058 | 2025-05-10 05:20:00 | GOES-19 | DIAMANTINO | MATO GROSSO | Brasil | 5103502 | 51 | 33 | nan | nan | nan | Cerrado | 45.7 |
| 03b0aa01-26c0-3673-9267-b85e7135ff61 | -3.7772 | -41.65426 | 2025-05-10 05:27:00 | AQUA_M-M | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 6.3 |
| d2331753-8a41-3414-990b-c11ae321caee | -10.65314 | -44.48258 | 2025-05-10 05:29:00 | AQUA_M-M | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 7.0 |
| 4852fa8e-a1c9-390f-866f-ec8ca2342200 | -10.64433 | -44.48124 | 2025-05-10 05:29:00 | AQUA_M-M | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 48d2e6b6-adbc-3771-87af-fa6f9353686a | -6.94775 | -43.01635 | 2025-05-10 05:29:00 | AQUA_M-M | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 34.7 |
| 7dd4b17e-6223-30fe-a979-267b44a10996 | -6.94906 | -43.00754 | 2025-05-10 05:29:00 | AQUA_M-M | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 9.8 |
| b226c2fc-6ad9-3f8c-bc83-a21318ac1565 | -13.24766 | -50.12433 | 2025-05-10 05:29:00 | AQUA_M-M | SÃO MIGUEL DO ARAGUAIA | GOIÁS | Brasil | 5220207 | 52 | 33 | nan | nan | nan | Cerrado | 51.0 |
| afbd023d-d4d5-3fcf-9bab-98ccba1bcd0a | -6.94643 | -43.02515 | 2025-05-10 05:29:00 | AQUA_M-M | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 33.5 |
| b45f0168-89ee-397b-a873-73076668817b | -13.2564 | -50.11605 | 2025-05-10 05:29:00 | AQUA_M-M | SÃO MIGUEL DO ARAGUAIA | GOIÁS | Brasil | 5220207 | 52 | 33 | nan | nan | nan | Cerrado | 12.5 |
| b9d680e1-23b1-3c9e-82d2-feb1ac793799 | -10.98427 | -44.4394 | 2025-05-10 05:29:00 | AQUA_M-M | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 074c7809-fdb0-3b81-b277-f858140aa2c8 | -10.99307 | -44.44074 | 2025-05-10 05:29:00 | AQUA_M-M | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 0d006afa-c1ef-3abb-b31b-71c391f1de6c | -6.95654 | -43.01764 | 2025-05-10 05:29:00 | AQUA_M-M | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 33.3 |
| 3784c2a1-87b1-3ab7-98eb-54e9406eb55d | -10.49151 | -42.40039 | 2025-05-10 05:29:00 | AQUA_M-M | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Caatinga | 7.2 |
| d966061d-339e-39ab-9990-8e85677f8cde | -13.25351 | -50.13242 | 2025-05-10 05:29:00 | AQUA_M-M | SÃO MIGUEL DO ARAGUAIA | GOIÁS | Brasil | 5220207 | 52 | 33 | nan | nan | nan | Cerrado | 44.2 |
| 2ffa911f-74e4-31fb-bec1-961dee1746e1 | -6.94511 | -43.03395 | 2025-05-10 05:29:00 | AQUA_M-M | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 6.2 |
| 73d5a6bf-5591-3790-83a0-b519c62da47d | -6.95522 | -43.02644 | 2025-05-10 05:29:00 | AQUA_M-M | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 16.7 |
| c9f29470-2c5a-346a-a78f-1a88ae8c5c1a | -6.95786 | -43.00884 | 2025-05-10 05:29:00 | AQUA_M-M | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 14.8 |
| 1fffab55-c176-37af-ad72-d2d7802f9111 | -13.9902 | -56.8058 | 2025-05-10 05:30:00 | GOES-19 | DIAMANTINO | MATO GROSSO | Brasil | 5103502 | 51 | 33 | nan | nan | nan | Cerrado | 45.9 |
| e31195b0-dfe6-3dbe-8c61-f2313c3393f3 | -6.9589 | -43.023 | 2025-05-10 05:40:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 59.3 |
| bb30d4ee-d997-369b-9559-61eb381af6f4 | -11.97325 | -63.52754 | 2025-05-10 06:01:00 | NOAA-21 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 0b580e11-699b-332f-aa3a-5bf0de281aee | -12.37232 | -63.91795 | 2025-05-10 06:01:00 | NOAA-21 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| a88c3cb7-ad9e-3989-b151-3e33e6c8dfdd | -9.93778 | -65.01583 | 2025-05-10 06:01:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 393d0bee-cb3d-3503-84c1-3bb7ae016a28 | -9.92861 | -65.02012 | 2025-05-10 06:01:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 9d74ec69-9db6-3acd-8633-12a7af2a8dcb | -9.93819 | -65.01342 | 2025-05-10 06:01:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 9962d16f-09e1-3266-8933-2217142965cb | -11.97265 | -63.52793 | 2025-05-10 06:01:00 | NOAA-21 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 06392105-8ce3-3f90-8f4e-e4d6284a59bd | -12.37168 | -63.9231 | 2025-05-10 06:01:00 | NOAA-21 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 51ab3eba-1274-3144-94fd-0375bf6fc9f0 | -8.6902 | -64.14169 | 2025-05-10 06:01:00 | NOAA-21 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 8ff4c651-261d-33b1-a396-b21e3964a0c4 | -11.97255 | -63.53287 | 2025-05-10 06:01:00 | NOAA-21 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 3505a137-84bb-314a-8e76-97213c0995b7 | -6.5631 | -51.1126 | 2025-05-10 08:00:00 | GOES-19 | OURILÂNDIA DO NORTE | PARÁ | Brasil | 1505437 | 15 | 33 | nan | nan | nan | Amazônia | 53.4 |
| bb263153-99b8-316c-bead-68d28962bd1a | -3.959 | -41.48145 | 2025-05-10 12:17:00 | TERRA_M-T | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 7.5 |
| 274bab9f-c13c-3d34-aad7-ae07ab08afda | -5.16345 | -37.54937 | 2025-05-10 12:17:00 | TERRA_M-T | BARAÚNA | RIO GRANDE DO NORTE | Brasil | 2401453 | 24 | 33 | nan | nan | nan | Caatinga | 16.0 |
| 4c8ea11c-e1de-3116-8520-5a7bdab866f5 | -3.77494 | -41.65643 | 2025-05-10 12:17:00 | TERRA_M-T | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 11.3 |
| 135dea2b-a34e-3af5-8a69-ad558153189e | -4.38233 | -43.36285 | 2025-05-10 12:17:00 | TERRA_M-T | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 7.6 |
| 25c176b0-e739-30d6-8d8f-7f97bff200c5 | -9.66744 | -49.71032 | 2025-05-10 12:19:00 | TERRA_M-T | MARIANÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1712504 | 17 | 33 | nan | nan | nan | Cerrado | 42.5 |
| 0671d868-1962-3cbc-ac20-f5206be3115c | -12.76577 | -45.40478 | 2025-05-10 12:19:00 | TERRA_M-T | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 7.6 |
| d5a1c9c2-bddb-3608-8cc4-dac4881a567b | -10.98595 | -44.43678 | 2025-05-10 12:19:00 | TERRA_M-T | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 51e1c61f-7df1-33cd-b92b-db5262d2f569 | -7.84285 | -37.38963 | 2025-05-10 12:19:00 | TERRA_M-T | IGUARACY | PERNAMBUCO | Brasil | 2606903 | 26 | 33 | nan | nan | nan | Caatinga | 25.4 |
| 37022103-74e1-3085-8890-59fb87398231 | -13.04836 | -53.73049 | 2025-05-10 12:19:00 | TERRA_M-T | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 25.7 |
| 695be571-22a0-3955-9949-de2536c08cc2 | -11.97464 | -46.71877 | 2025-05-10 12:19:00 | TERRA_M-T | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 21.7 |
| 29dd19b7-4cbd-3c22-a186-ac55ad7d59e2 | -11.97106 | -45.16066 | 2025-05-10 12:19:00 | TERRA_M-T | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 1ac12429-1b2b-38e8-9787-a08aafa0afe1 | -7.83371 | -37.4054 | 2025-05-10 12:19:00 | TERRA_M-T | IGUARACY | PERNAMBUCO | Brasil | 2606903 | 26 | 33 | nan | nan | nan | Caatinga | 49.9 |
| db95994e-7298-36c5-be09-4f29816bfca9 | -11.06629 | -46.12664 | 2025-05-10 12:19:00 | TERRA_M-T | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 14.2 |
| e86140db-c370-3d43-b776-882bf3d1316d | -7.83998 | -37.4129 | 2025-05-10 12:19:00 | TERRA_M-T | IGUARACY | PERNAMBUCO | Brasil | 2606903 | 26 | 33 | nan | nan | nan | Caatinga | 37.8 |
| 4f378d99-ab7b-3cac-8bad-57507491f15b | -7.20505 | -43.08677 | 2025-05-10 12:19:00 | TERRA_M-T | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 12.8 |
| bf4bb83a-c779-3de2-b5d9-a563487f3840 | -11.97602 | -46.70944 | 2025-05-10 12:19:00 | TERRA_M-T | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 27c009b9-7cf7-3195-bbf8-aa36f0598e02 | -10.64688 | -44.48529 | 2025-05-10 12:19:00 | TERRA_M-T | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 6.6 |
| fddf932e-a5e0-36b9-9aa5-b6469dde1e06 | -11.06763 | -46.11756 | 2025-05-10 12:19:00 | TERRA_M-T | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 16.4 |
| f6100549-da45-33fc-b5f8-8696341c8b3e | -13.69467 | -45.41654 | 2025-05-10 12:19:00 | TERRA_M-T | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 22.2 |
| 000ab0a0-0053-3ca0-8b1a-d04a4c025f92 | -13.69338 | -45.42564 | 2025-05-10 12:19:00 | TERRA_M-T | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 11.1 |
| 4b86d495-6dba-3175-aa7a-346963b5241f | -7.61592 | -43.44026 | 2025-05-10 12:19:00 | TERRA_M-T | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 10df1164-b8b3-33c8-a543-23598e3fba5f | -13.93779 | -47.78743 | 2025-05-10 12:19:00 | TERRA_M-T | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 68aff48c-5b89-38ca-9978-2fe561e3ee8b | -14.21357 | -45.46383 | 2025-05-10 12:19:00 | TERRA_M-T | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 9.7 |
| 0d36ace8-07a1-3364-91bb-7005bc4bbfc8 | -10.4954 | -46.17563 | 2025-05-10 12:19:00 | TERRA_M-T | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 7.2 |
| 4696be4f-75a0-3d44-941a-1a68cc6876b1 | -10.48646 | -46.17433 | 2025-05-10 12:19:00 | TERRA_M-T | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 14.9 |
| 7da1867b-5971-374a-972b-dd895521957b | -12.76145 | -47.99194 | 2025-05-10 12:19:00 | TERRA_M-T | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 31.4 |
| 79371efd-97df-3a9b-ab3f-c23cc18f4cb9 | -17.67174 | -43.89386 | 2025-05-10 12:21:00 | TERRA_M-T | BOCAIÚVA | MINAS GERAIS | Brasil | 3107307 | 31 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 5170d6f5-1f86-3564-900b-33653c48bde5 | -16.72657 | -45.99718 | 2025-05-10 12:21:00 | TERRA_M-T | BRASILÂNDIA DE MINAS | MINAS GERAIS | Brasil | 3108552 | 31 | 33 | nan | nan | nan | Cerrado | 6.6 |
| bea4bbec-ee80-3c69-8e68-a4119e3f9774 | -16.30334 | -53.84187 | 2025-05-10 12:21:00 | TERRA_M-T | GUIRATINGA | MATO GROSSO | Brasil | 5104203 | 51 | 33 | nan | nan | nan | Cerrado | 31.0 |
| 9f9b1ad3-51a4-39e9-afc8-0d16eb748583 | -13.3749 | -54.2745 | 2025-05-10 12:30:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 78.0 |
| abbb37bc-d239-3b62-bc3b-1e2de1f61307 | -13.3752 | -54.2538 | 2025-05-10 12:30:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 71.8 |
| 3e825c5e-cac1-3a61-922c-3ecb8b52e93d | -13.3749 | -54.2745 | 2025-05-10 12:40:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 104.7 |
| 9bd5991e-8280-3179-9916-b2fedfe9f216 | -13.3752 | -54.2538 | 2025-05-10 12:40:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 115.4 |
| 789fcb25-218a-3e3e-a58e-04fbd6077ea9 | -13.3749 | -54.2745 | 2025-05-10 12:50:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 104.9 |
| 836215ce-3ea6-3fe7-9f0d-0f7e1f9e1626 | -13.3752 | -54.2538 | 2025-05-10 12:50:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 125.4 |
| 7b1d05ac-a0c9-3e52-9fce-dea104cd77a3 | -13.3749 | -54.2745 | 2025-05-10 13:00:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 97.0 |
| 35c79567-0a8e-38f1-a955-5f68896fa2ff | -13.3752 | -54.2538 | 2025-05-10 13:00:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 101.7 |
| 04e53594-b433-35da-84ba-1b61b1967fa3 | -13.9902 | -56.8058 | 2025-05-10 13:10:00 | GOES-19 | DIAMANTINO | MATO GROSSO | Brasil | 5103502 | 51 | 33 | nan | nan | nan | Cerrado | 82.7 |
| fd047a40-74f2-3c8b-ab19-2a607b164e37 | -13.3752 | -54.2538 | 2025-05-10 13:10:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 131.9 |
| 497b3a78-1df5-36f5-91c1-20bac3840a62 | -13.3749 | -54.2745 | 2025-05-10 13:10:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 122.7 |
| 1bbf78fc-ddc0-3070-a032-2616bec68375 | -13.9902 | -56.8058 | 2025-05-10 13:20:00 | GOES-19 | DIAMANTINO | MATO GROSSO | Brasil | 5103502 | 51 | 33 | nan | nan | nan | Cerrado | 85.9 |


[Clique aqui para ver as próximas entradas](README9.md)
