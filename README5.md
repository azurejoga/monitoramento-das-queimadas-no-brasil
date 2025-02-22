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

## Dados Diários - Página 5

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| d9541c91-0e4d-3d3f-9a9f-db9297413161 | -14.44095 | -45.63363 | 2025-02-22 05:05:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 2690c13c-1b83-32d7-a54f-f8a08de907b4 | -14.43519 | -45.62762 | 2025-02-22 05:05:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 119e8ff2-25c0-3cb7-92bb-e21db27b0f81 | -15.07844 | -48.94521 | 2025-02-22 05:05:00 | NOAA-21 | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 11ad423f-efb9-30d1-9ceb-bd5c0eca75fe | -12.82165 | -44.99324 | 2025-02-22 05:05:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 05805c72-45d1-3e3a-91a6-d5933042a47e | -12.15759 | -54.9916 | 2025-02-22 05:05:00 | NOAA-21 | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| dd5cda59-7584-39a8-ae0b-b8be0252bddf | -12.82813 | -44.98629 | 2025-02-22 05:05:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 45030389-849a-3d38-bcec-8c7b085f7790 | -12.33122 | -52.47923 | 2025-02-22 05:05:00 | NOAA-21 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 55aa9b51-939f-3eaf-b292-f7ac1bee7289 | -19.09131 | -56.06079 | 2025-02-22 05:08:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 0.8 |
| e7448b9f-aed0-3847-81a3-a5250eaa5e38 | -19.0896 | -56.07316 | 2025-02-22 05:08:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.5 |
| b6c72966-2921-31f6-9e94-6b3a8ac97398 | -21.97039 | -57.58567 | 2025-02-22 05:08:00 | NOAA-21 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 38fd9307-b1b0-3896-9692-ff2fd3744006 | -18.57028 | -57.38428 | 2025-02-22 05:08:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.5 |
| 38a8ca65-b9a6-3430-adfb-e93d68614636 | -21.20116 | -56.49084 | 2025-02-22 05:08:00 | NOAA-21 | BONITO | MATO GROSSO DO SUL | Brasil | 5002209 | 50 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 32d70b7a-b5ae-389a-b139-a6f045aead10 | -19.0862 | -56.06585 | 2025-02-22 05:08:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.0 |
| 75310cde-808f-3480-8eed-2e50d8390e8d | -19.0954 | -56.05722 | 2025-02-22 05:08:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 0.8 |
| 5ed5f56d-8fae-3407-a1b4-3cde5f2237e0 | -19.09074 | -56.06492 | 2025-02-22 05:08:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.3 |
| c0472edc-4026-3e0b-9d58-c3fa5986531c | -20.99627 | -51.79516 | 2025-02-22 05:08:00 | NOAA-21 | TRÊS LAGOAS | MATO GROSSO DO SUL | Brasil | 5008305 | 50 | 33 | nan | nan | nan | Mata Atlântica | 2.8 |
| ae63a33b-99e6-3724-8297-f7fbadbdda7e | -19.09017 | -56.06904 | 2025-02-22 05:08:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.3 |
| c750ee36-e100-3728-8216-9ce49555c417 | -19.08561 | -56.06997 | 2025-02-22 05:08:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.0 |
| fd454dd7-a2c5-356d-96b3-b15670341514 | -22.05289 | -49.03316 | 2025-02-22 05:08:00 | NOAA-21 | AREALVA | SÃO PAULO | Brasil | 3503406 | 35 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 929403a2-7f0c-3695-be69-5cb140acb826 | -22.05433 | -49.03039 | 2025-02-22 05:08:00 | NOAA-21 | AREALVA | SÃO PAULO | Brasil | 3503406 | 35 | 33 | nan | nan | nan | Cerrado | 10.0 |
| b6253c39-6990-3bce-a197-d37ddf8c1f12 | -19.08912 | -56.07051 | 2025-02-22 05:08:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.3 |
| 029412ce-ade2-31cc-94c2-d1e8ab5bea71 | -19.08971 | -56.0664 | 2025-02-22 05:08:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.3 |
| b7a71fb1-28af-3387-a559-688b05171e2b | -20.59817 | -56.1024 | 2025-02-22 05:08:00 | NOAA-21 | ANASTÁCIO | MATO GROSSO DO SUL | Brasil | 5000708 | 50 | 33 | nan | nan | nan | Cerrado | 1.6 |
| b7e4a4f7-a39e-3f7c-b309-2461b694d9da | -19.09368 | -56.0696 | 2025-02-22 05:08:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.3 |
| 342b068c-b065-3352-9ef4-6deb60d1109e | -19.08738 | -56.05761 | 2025-02-22 05:08:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 0.8 |
| c17a812d-0b56-350c-bdfa-232f666f254c | -19.08387 | -56.05706 | 2025-02-22 05:08:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 0.8 |
| 266e2134-a013-3ced-bcc4-d21e55e5b357 | -21.07455 | -56.38726 | 2025-02-22 05:08:00 | NOAA-21 | BONITO | MATO GROSSO DO SUL | Brasil | 5002209 | 50 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 271ba2e3-d522-33ad-ae5e-7d7987eca21f | -19.14777 | -52.86545 | 2025-02-22 05:08:00 | NOAA-21 | CHAPADÃO DO SUL | MATO GROSSO DO SUL | Brasil | 5002951 | 50 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 3957778d-dac6-3c12-b14f-9a926ba81164 | -15.63164 | -57.31322 | 2025-02-22 05:08:00 | NOAA-21 | PORTO ESTRELA | MATO GROSSO | Brasil | 5106851 | 51 | 33 | nan | nan | nan | Cerrado | 2.8 |
| ddf7dbd6-932c-3306-a2f3-5555403cedf0 | -22.05881 | -49.03005 | 2025-02-22 05:08:00 | NOAA-21 | AREALVA | SÃO PAULO | Brasil | 3503406 | 35 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 4c201336-6b92-36f8-9877-382146a92c32 | -15.63496 | -57.31376 | 2025-02-22 05:08:00 | NOAA-21 | PORTO ESTRELA | MATO GROSSO | Brasil | 5106851 | 51 | 33 | nan | nan | nan | Cerrado | 2.8 |
| c38bce28-af8e-34db-9b0b-8839323cb563 | -19.08502 | -56.07408 | 2025-02-22 05:08:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.4 |
| e30fbb5e-95b3-36a2-a65e-74994d2dc455 | -19.09189 | -56.05666 | 2025-02-22 05:08:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 0.8 |
| 00d512ff-c894-3fb7-9245-cb1ccce7aa1b | -17.79419 | -55.06254 | 2025-02-22 05:08:00 | NOAA-21 | SONORA | MATO GROSSO DO SUL | Brasil | 5007935 | 50 | 33 | nan | nan | nan | Pantanal | 1.5 |
| 9eda49be-432f-3a90-8d40-bfc8628f1641 | -19.09089 | -56.05816 | 2025-02-22 05:08:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.3 |
| 9eeb66a5-7bf0-31de-bca3-0f199012c2bb | -20.77111 | -45.84101 | 2025-02-22 05:08:00 | NOAA-21 | GUAPÉ | MINAS GERAIS | Brasil | 3128105 | 31 | 33 | nan | nan | nan | Cerrado | 3.6 |
| b7014900-007a-35b2-9e6e-2b4f081f4187 | -19.0944 | -56.05872 | 2025-02-22 05:08:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.3 |
| e7366a82-7c49-3f16-83d0-88013495116c | -19.09322 | -56.06695 | 2025-02-22 05:08:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.3 |
| 5faea8ce-0bff-3c23-ad8f-ef30e82b5d45 | -19.09263 | -56.07107 | 2025-02-22 05:08:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.3 |
| fc21fc68-e988-300c-be50-445b64ceb8bb | -19.08211 | -56.06941 | 2025-02-22 05:08:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.0 |
| 6362dddb-158d-3998-8ddc-13cdd026b3da | -18.55855 | -57.3938 | 2025-02-22 05:08:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.1 |
| 8856a2dd-5ec2-3bf1-91da-d982a08860a8 | -20.84692 | -56.41424 | 2025-02-22 05:08:00 | NOAA-21 | BONITO | MATO GROSSO DO SUL | Brasil | 5002209 | 50 | 33 | nan | nan | nan | Cerrado | 1.2 |
| b4e20750-84c0-3974-b12e-2c1dc5987cd0 | -18.8248 | -48.21559 | 2025-02-22 05:08:00 | NOAA-21 | UBERLÂNDIA | MINAS GERAIS | Brasil | 3170206 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| d2195466-d9e9-394e-b00d-cd0dc72e75b9 | -22.05323 | -49.02921 | 2025-02-22 05:08:00 | NOAA-21 | AREALVA | SÃO PAULO | Brasil | 3503406 | 35 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 15f0ef51-0baf-333b-b1d5-97769fdb1ad2 | -18.5619 | -57.39435 | 2025-02-22 05:08:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.1 |
| a278091e-0dfd-3b90-8625-0f2f4694dd90 | -20.84633 | -56.41841 | 2025-02-22 05:08:00 | NOAA-21 | BONITO | MATO GROSSO DO SUL | Brasil | 5002209 | 50 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 484e51d2-e68b-3f47-95a1-83ad96bcf972 | -21.96699 | -57.5851 | 2025-02-22 05:08:00 | NOAA-21 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 7beab82a-0379-3204-8cf3-b31a11a84af0 | -30.22503 | -54.48806 | 2025-02-22 05:10:00 | NOAA-21 | SÃO GABRIEL | RIO GRANDE DO SUL | Brasil | 4318309 | 43 | 33 | nan | nan | nan | Pampa | 1.8 |
| 3c627f12-9b19-39f8-934a-663b104fa037 | 3.1179 | -61.27551 | 2025-02-22 05:29:00 | NPP-375D | ALTO ALEGRE | RORAIMA | Brasil | 1400050 | 14 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 0c3617bb-3d76-3ef6-92cc-c3027d9ba2cd | 4.78241 | -60.54423 | 2025-02-22 05:29:00 | NPP-375D | UIRAMUTÃ | RORAIMA | Brasil | 1400704 | 14 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 690d16e2-3a3a-3f28-826b-419be7005ae6 | 3.82485 | -60.17563 | 2025-02-22 05:29:00 | NPP-375D | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 2.0 |
| ee6f5691-80ed-3eb4-ad32-4e30ceaf3881 | 4.78186 | -60.54074 | 2025-02-22 05:29:00 | NPP-375D | UIRAMUTÃ | RORAIMA | Brasil | 1400704 | 14 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 581e36f0-f798-3585-880f-60939e992efe | 3.82817 | -60.17512 | 2025-02-22 05:29:00 | NPP-375D | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 4d366849-1569-374a-912a-acd262931931 | -12.15333 | -54.99606 | 2025-02-22 05:31:00 | NPP-375D | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| abfca296-ba3e-3fb3-a50b-4510066cae4a | -12.15883 | -54.99367 | 2025-02-22 05:31:00 | NPP-375D | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 506b9130-335e-3ba7-b93a-a9eba16d2c9e | -12.15845 | -54.99675 | 2025-02-22 05:31:00 | NPP-375D | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| fe9219ce-9561-3d91-b360-e5c2753bb3bd | -11.82856 | -58.80125 | 2025-02-22 05:31:00 | NPP-375D | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| c56a08dd-5ac4-35b7-933c-6111e4554ddf | -9.932 | -59.93673 | 2025-02-22 05:31:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 7e537d2f-d9af-36c5-af7a-55ee24fb887d | -12.15372 | -54.993 | 2025-02-22 05:31:00 | NPP-375D | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 12e3623f-aa14-3818-b3f7-64c879f89654 | -15.62914 | -57.31138 | 2025-02-22 05:31:00 | NPP-375D | PORTO ESTRELA | MATO GROSSO | Brasil | 5106851 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| b7e24d36-580f-37b6-acce-1e43e67aad7a | -11.82932 | -58.79606 | 2025-02-22 05:31:00 | NPP-375D | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 6623756b-ad6a-37ba-8edd-2cc3481e919d | -12.15807 | -54.9998 | 2025-02-22 05:31:00 | NPP-375D | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 7be9e348-9cba-3fc3-b11a-9ee715ffa943 | -15.63371 | -57.31214 | 2025-02-22 05:31:00 | NPP-375D | PORTO ESTRELA | MATO GROSSO | Brasil | 5106851 | 51 | 33 | nan | nan | nan | Cerrado | 3.5 |
| d418f592-db1a-3380-939c-3cd21b03ed82 | -9.92416 | -59.9398 | 2025-02-22 05:31:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 5527e726-057c-3109-aada-c3f2601a8f62 | -11.82769 | -58.79729 | 2025-02-22 05:31:00 | NPP-375D | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 45dcf0f5-d140-331f-ac1d-bb375a179d82 | -9.93228 | -59.9392 | 2025-02-22 05:31:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| b11b9298-f61e-30ac-8957-f4f3a8e565d1 | -19.0909 | -56.05741 | 2025-02-22 05:33:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 0.6 |
| 07f633fb-c2b4-33a8-8a77-38e6666cd73a | -21.97047 | -57.5876 | 2025-02-22 05:33:00 | NPP-375D | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 49d0ee7c-2651-3eb8-94e5-b6e6f459836a | -19.08422 | -56.06997 | 2025-02-22 05:33:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.1 |
| cb180ecc-d71a-322b-b07c-97dd64e0dec8 | -20.84821 | -56.41521 | 2025-02-22 05:33:00 | NPP-375D | BONITO | MATO GROSSO DO SUL | Brasil | 5002209 | 50 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 4c706fe1-4a7c-3a7e-a730-16dbb4d8ebfa | -19.08458 | -56.06669 | 2025-02-22 05:33:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.1 |
| 57e2bc1f-d283-3be6-b80e-0252b9204fd9 | -19.08945 | -56.0706 | 2025-02-22 05:33:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.2 |
| 1f39a69d-9f71-36c0-a55f-652253c7a63c | -21.96558 | -57.58686 | 2025-02-22 05:33:00 | NPP-375D | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 1213eec4-4d93-39b5-9eec-4012d8f9181c | -19.09054 | -56.06072 | 2025-02-22 05:33:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 0.9 |
| 92ae845f-2dfc-355f-93c4-2ff1d5daff8f | -19.08981 | -56.06732 | 2025-02-22 05:33:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.2 |
| b06ae87b-6003-3cd8-9f59-802fbc18eeee | -20.84298 | -56.41473 | 2025-02-22 05:33:00 | NPP-375D | BONITO | MATO GROSSO DO SUL | Brasil | 5002209 | 50 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 5c08808c-8d0a-38a7-89b8-a83216f17096 | -19.08386 | -56.07326 | 2025-02-22 05:33:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.0 |
| a88b156a-32d6-3d7a-904c-54e7132bd355 | 4.78095 | -60.54436 | 2025-02-22 05:50:00 | NOAA-20 | UIRAMUTÃ | RORAIMA | Brasil | 1400704 | 14 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 9b7d6756-fe62-39bc-bbb4-a8c2b426990f | 4.78507 | -60.54366 | 2025-02-22 05:50:00 | NOAA-20 | UIRAMUTÃ | RORAIMA | Brasil | 1400704 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |
| fec6c27f-051a-3ce1-9f91-c3f59efdda65 | -9.9315 | -59.93842 | 2025-02-22 05:54:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 788e8e03-f9d1-368a-a6e8-7937dd03c07c | -7.97095 | -57.91851 | 2025-02-22 05:54:00 | NOAA-20 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 0.0 |
| 664e8606-8787-35e7-8cb2-3115ee7e4a2a | -9.92564 | -59.94114 | 2025-02-22 05:54:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 29b62373-2e55-36cd-8697-4043e441f969 | -15.63223 | -57.31209 | 2025-02-22 05:57:00 | NOAA-20 | PORTO ESTRELA | MATO GROSSO | Brasil | 5106851 | 51 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 4df1b2a0-54c6-3d72-a1d1-5c46c6aed984 | -19.09221 | -56.0626 | 2025-02-22 06:05:00 | AQUA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 4.4 |
| 1d313ef4-4f4a-3036-9e1e-a29803785e1f | -19.08335 | -56.06117 | 2025-02-22 06:05:00 | AQUA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 12.6 |
| 1777571a-1a1c-38ae-83bc-809297c720cd | -19.08197 | -56.0705 | 2025-02-22 06:05:00 | AQUA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 10.8 |
| c496c205-f8b7-385a-a3ab-0452d33a6336 | -5.23533 | -39.3979 | 2025-02-22 12:16:00 | TERRA_M-T | QUIXERAMOBIM | CEARÁ | Brasil | 2311405 | 23 | 33 | nan | nan | nan | Caatinga | 18.1 |
| eeb55931-9696-3dfb-864d-a20467634021 | -7.01888 | -38.8297 | 2025-02-22 12:16:00 | TERRA_M-T | BARRO | CEARÁ | Brasil | 2302008 | 23 | 33 | nan | nan | nan | Caatinga | 25.9 |
| 8b19ec79-df44-396a-a8d4-70458d50898e | -8.28084 | -37.62701 | 2025-02-22 12:16:00 | TERRA_M-T | CUSTÓDIA | PERNAMBUCO | Brasil | 2605103 | 26 | 33 | nan | nan | nan | Caatinga | 13.3 |
| 940e0dc0-e0e8-3336-bd62-43a8ffd03154 | -9.22138 | -40.59593 | 2025-02-22 12:16:00 | TERRA_M-T | PETROLINA | PERNAMBUCO | Brasil | 2611101 | 26 | 33 | nan | nan | nan | Caatinga | 6.0 |
| b90f9448-b7dc-3e7e-b838-28852c3f6569 | -9.98299 | -38.54218 | 2025-02-22 12:16:00 | TERRA_M-T | JEREMOABO | BAHIA | Brasil | 2918100 | 29 | 33 | nan | nan | nan | Caatinga | 17.7 |
| 9d0cc025-b4b7-342a-a4ac-0e960696e57b | -6.44304 | -35.10391 | 2025-02-22 12:16:00 | TERRA_M-T | BAÍA FORMOSA | RIO GRANDE DO NORTE | Brasil | 2401404 | 24 | 33 | nan | nan | nan | Mata Atlântica | 21.9 |
| 2069362f-d3fb-3bae-a35b-e56be4b2925f | -7.88994 | -37.01911 | 2025-02-22 12:16:00 | TERRA_M-T | MONTEIRO | PARAÍBA | Brasil | 2509701 | 25 | 33 | nan | nan | nan | Caatinga | 15.5 |
| 8432a3d0-a9d0-3dd8-8698-3496342c34bf | -5.23341 | -39.39168 | 2025-02-22 12:16:00 | TERRA_M-T | QUIXERAMOBIM | CEARÁ | Brasil | 2311405 | 23 | 33 | nan | nan | nan | Caatinga | 28.6 |
| 31e8391e-0b3b-3401-8e84-8284e0d455f4 | -7.89221 | -37.00149 | 2025-02-22 12:16:00 | TERRA_M-T | MONTEIRO | PARAÍBA | Brasil | 2509701 | 25 | 33 | nan | nan | nan | Caatinga | 12.7 |
| 25579d26-9bad-349c-a369-671057f66479 | -7.02057 | -38.81732 | 2025-02-22 12:16:00 | TERRA_M-T | BARRO | CEARÁ | Brasil | 2302008 | 23 | 33 | nan | nan | nan | Caatinga | 30.8 |
| 801026e1-b1bc-3e13-bbcf-f47b310517f6 | -16.33382 | -45.04988 | 2025-02-22 12:18:00 | TERRA_M-T | ICARAÍ DE MINAS | MINAS GERAIS | Brasil | 3130051 | 31 | 33 | nan | nan | nan | Cerrado | 8.2 |
| 2f42f59c-26dc-31ee-9c46-71a7e2804eae | -14.4315 | -45.80253 | 2025-02-22 12:18:00 | TERRA_M-T | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 13.7 |
| 3683085e-4a32-3086-a64b-fce3cbf41f3b | -20.89155 | -46.16586 | 2025-02-22 12:18:00 | TERRA_M-T | CARMO DO RIO CLARO | MINAS GERAIS | Brasil | 3114402 | 31 | 33 | nan | nan | nan | Cerrado | 9.5 |
| b969a5ba-c233-37ac-abd0-4d8df361bb7f | -17.84101 | -42.7057 | 2025-02-22 12:18:00 | TERRA_M-T | ITAMARANDIBA | MINAS GERAIS | Brasil | 3132503 | 31 | 33 | nan | nan | nan | Mata Atlântica | 14.3 |


[Clique aqui para ver as próximas entradas](README6.md)
