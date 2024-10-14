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

## Dados Diários - Página 114

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 04e6ad19-25aa-352d-ad1d-f1cd58171454 | -11.25405 | -51.32327 | 2024-10-14 05:10:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 3bd1917f-1f1b-3fcf-880a-497aa5a25cd7 | -11.23423 | -51.33045 | 2024-10-14 05:10:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 0bed865d-e0e7-3b09-b6b0-982fea35f9ed | -11.22961 | -51.32982 | 2024-10-14 05:10:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 40638c9b-4b0d-3077-9bfb-83dabed04408 | -11.22499 | -51.32918 | 2024-10-14 05:10:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| dc594893-84f0-3310-af23-40d196934a2b | -9.33761 | -52.84787 | 2024-10-14 05:10:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 520fb163-e9d2-3bb9-87fd-e1d384d74064 | -9.33743 | -52.84814 | 2024-10-14 05:10:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 4d4464d3-a8ab-3cfb-baed-0dcd01d39dc6 | -9.33712 | -52.85137 | 2024-10-14 05:10:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 3333eade-649d-3c6e-9939-46fbcb414794 | -9.33692 | -52.85163 | 2024-10-14 05:10:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 913c692e-d3b9-3576-84c4-2f093f171096 | -9.33385 | -52.84423 | 2024-10-14 05:10:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 6.5 |
| ae38008f-a9c7-3e97-ab7f-ef8861e72dcc | -9.33335 | -52.84772 | 2024-10-14 05:10:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 6.5 |
| 9513ac49-265f-3f63-8322-63a72408d1d9 | -9.33284 | -52.8512 | 2024-10-14 05:10:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 001394aa-8735-364e-9101-8d7caaac8a88 | -9.06581 | -52.94726 | 2024-10-14 05:10:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 6c8d6e94-4059-3b7d-99f2-00f41ed79ad9 | -9.05364 | -53.00344 | 2024-10-14 05:10:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 5cfaceb0-8f29-3c74-8bef-313341ac22a7 | -9.04961 | -53.00309 | 2024-10-14 05:10:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 69a2db82-d220-3ea1-8ce9-21c459941041 | -9.04213 | -52.99826 | 2024-10-14 05:10:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 2142a3bb-f899-3617-bd17-4f10b76570a4 | -9.04159 | -53.00201 | 2024-10-14 05:10:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 91605b3d-f72a-3e0c-8d51-64e4a97f70d9 | -9.03816 | -52.9399 | 2024-10-14 05:10:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 7d0571ae-e216-3db4-b1d5-c7d426f7deee | -9.03815 | -52.99749 | 2024-10-14 05:10:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 07f83ef1-e6ed-31c6-ad99-4a4409d405c4 | -9.03363 | -52.94292 | 2024-10-14 05:10:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 73bee837-ee04-3fc2-8d20-a09dcb9afa54 | -9.03312 | -52.94649 | 2024-10-14 05:10:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 30433458-c5ab-3bfa-88b5-c4cf16404d19 | -8.92265 | -52.84712 | 2024-10-14 05:10:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 3bb8e097-0d9a-3920-a76b-d57b199e9466 | -8.85395 | -53.03104 | 2024-10-14 05:10:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 3a554117-64cf-34e7-8919-36a992bbd935 | -8.85347 | -53.03435 | 2024-10-14 05:10:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| ab232b24-df73-31f4-9efb-b6d821e7904b | -8.85141 | -53.02058 | 2024-10-14 05:10:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| cd203062-a5b3-3532-9931-01a26d95a69a | -8.85098 | -52.99548 | 2024-10-14 05:10:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 3b10ce6b-c762-39f2-b41b-71cd1aee77af | -8.85093 | -53.02387 | 2024-10-14 05:10:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 915069ba-a6a2-326a-9e3e-65eed7c60c35 | -9.43706 | -53.20115 | 2024-10-14 05:10:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 3c7e2435-72b4-3e53-b801-23658e8a4e79 | -9.43378 | -53.19572 | 2024-10-14 05:10:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 7675cfea-950d-3b66-b093-11a9010aac5d | -9.43308 | -53.20067 | 2024-10-14 05:10:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 7c52d1d4-cfd1-3be6-8237-a09a05427a90 | -9.43055 | -53.1899 | 2024-10-14 05:10:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| ffdccabd-b99d-355d-8fa5-5cb31e05c5fc | -9.885 | -52.28297 | 2024-10-14 05:10:00 | NOAA-20 | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 8299230e-98ea-3161-9ab3-81a18505217b | -9.8813 | -52.27839 | 2024-10-14 05:10:00 | NOAA-20 | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| d88cc07e-9e79-3659-979a-c121b41eba83 | -9.88075 | -52.28241 | 2024-10-14 05:10:00 | NOAA-20 | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 7b0fb00d-a945-3c98-9555-78d8c2244ed6 | -9.73261 | -52.84386 | 2024-10-14 05:10:00 | NOAA-20 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 223048f3-7764-3720-88f1-ba7e5c5e2d24 | -9.73207 | -52.84759 | 2024-10-14 05:10:00 | NOAA-20 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 43da5b80-8ab9-3bd2-a0cf-e6d290ee2bcc | -9.73155 | -52.85129 | 2024-10-14 05:10:00 | NOAA-20 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| ed1e902e-7682-3269-97ea-17c523a0f4ed | -9.73102 | -52.85499 | 2024-10-14 05:10:00 | NOAA-20 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 81baf0d5-8ab4-3ef5-b4ca-106f9366894c | -9.73049 | -52.85873 | 2024-10-14 05:10:00 | NOAA-20 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 4df2741e-5e8c-3ce1-bdc7-809c6cf27d78 | -9.72852 | -52.84332 | 2024-10-14 05:10:00 | NOAA-20 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 3834d461-8d17-3021-bce9-aed1f1439970 | -9.72756 | -52.82066 | 2024-10-14 05:10:00 | NOAA-20 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 919ac5a5-6be8-3239-957c-092cba237443 | -9.72644 | -52.85796 | 2024-10-14 05:10:00 | NOAA-20 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 9aa562bd-6b42-345a-ac1c-acf00430b531 | -9.72398 | -52.81651 | 2024-10-14 05:10:00 | NOAA-20 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 9acf47b3-6ffa-3c86-8b81-2943d4bd4223 | -9.72136 | -52.86438 | 2024-10-14 05:10:00 | NOAA-20 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 190043d2-d8e0-348d-9d61-6a39aa8e197e | -9.71987 | -52.81607 | 2024-10-14 05:10:00 | NOAA-20 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| bd4940d2-44a2-3cf4-a458-d3ab599cb396 | -9.71727 | -52.8639 | 2024-10-14 05:10:00 | NOAA-20 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 6e5d0bd9-d082-325b-8611-168aa14b314b | -9.71574 | -52.81573 | 2024-10-14 05:10:00 | NOAA-20 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 9cfb9ab7-3404-3309-b2b9-a1a0fdcdf070 | -9.71368 | -52.8599 | 2024-10-14 05:10:00 | NOAA-20 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 0638e8fa-eb13-3396-a00b-ebc5d2c29307 | -9.71316 | -52.86353 | 2024-10-14 05:10:00 | NOAA-20 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| f524685e-8b9d-3f70-8236-f382ec59e975 | -9.71164 | -52.81525 | 2024-10-14 05:10:00 | NOAA-20 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 63a4faa5-1bde-38ef-b006-189f8347aac6 | -9.71112 | -52.81895 | 2024-10-14 05:10:00 | NOAA-20 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 3d603f04-ea5c-3210-95ab-205b00095b0f | -9.71013 | -52.85558 | 2024-10-14 05:10:00 | NOAA-20 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 27fbac5e-8018-3639-b5cd-167693f84d3f | -9.70962 | -52.85918 | 2024-10-14 05:10:00 | NOAA-20 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 408cd9e1-18be-327a-a321-47d98d37cdc2 | -9.70708 | -52.81802 | 2024-10-14 05:10:00 | NOAA-20 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| d6c79eb9-2f82-3af6-abb1-0c71a382b54f | -9.70655 | -52.82178 | 2024-10-14 05:10:00 | NOAA-20 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 61c0b69a-7205-3ad4-8b3c-0aad87ce82d0 | -9.70609 | -52.85467 | 2024-10-14 05:10:00 | NOAA-20 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| a8277999-5272-3866-8cd9-c92577112fd5 | -9.70604 | -52.8254 | 2024-10-14 05:10:00 | NOAA-20 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a5403a5f-f0a4-32bd-9e33-375b718f77e9 | -9.702 | -52.82453 | 2024-10-14 05:10:00 | NOAA-20 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| ae48912d-02cb-3193-bf76-f8a1989999bd | -9.70149 | -52.82814 | 2024-10-14 05:10:00 | NOAA-20 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| a63eef91-6e7b-34e1-b8f3-20171563fecd | -9.70049 | -52.83526 | 2024-10-14 05:10:00 | NOAA-20 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 3dbf7ddc-2559-38b1-8e37-09de1dd71a81 | -9.69999 | -52.83883 | 2024-10-14 05:10:00 | NOAA-20 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| fa538e8b-d661-3230-966a-5f72c74113ff | -10.69199 | -53.01529 | 2024-10-14 05:10:00 | NOAA-20 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 055c29ce-a0c3-3f20-8ff9-c9f64f74a79d | -10.69147 | -53.019 | 2024-10-14 05:10:00 | NOAA-20 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 70ad50e5-71bd-382c-93d9-525d45e21b6f | -10.22445 | -52.68781 | 2024-10-14 05:10:00 | NOAA-20 | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 8c71e395-a48a-3197-b853-fb6c35398217 | -10.22176 | -52.68959 | 2024-10-14 05:10:00 | NOAA-20 | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| b21ab75a-4adc-3cfc-ac00-4500dbc2b7c3 | -10.20612 | -52.33039 | 2024-10-14 05:10:00 | NOAA-20 | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| eb7fb03e-98ad-34f8-95a5-b6a16d6530ca | -10.20556 | -52.33444 | 2024-10-14 05:10:00 | NOAA-20 | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 8738f770-ee1d-30b3-988e-6fa461f998b0 | -10.20242 | -52.32573 | 2024-10-14 05:10:00 | NOAA-20 | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 98b53624-fc17-3f97-833a-e70e07f392ea | -10.20186 | -52.32978 | 2024-10-14 05:10:00 | NOAA-20 | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| e1f5b39c-b125-3efe-a7a0-10cf79614653 | -10.20131 | -52.33383 | 2024-10-14 05:10:00 | NOAA-20 | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 70742fb7-f84e-3601-b102-a1eb2fa9580e | -10.15916 | -52.38913 | 2024-10-14 05:10:00 | NOAA-20 | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| f8625f56-24f6-36eb-828d-1bd8531c1d6a | -10.15914 | -52.38969 | 2024-10-14 05:10:00 | NOAA-20 | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 5d981e29-975f-35e0-9bc0-7665654f155f | -11.56339 | -53.86163 | 2024-10-14 05:10:00 | NOAA-20 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 0c41960f-5ea2-3acf-8805-79c1452aa079 | -11.55997 | -53.85926 | 2024-10-14 05:10:00 | NOAA-20 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| af08a13a-a5b6-301f-a7c5-a9edb6cdc395 | -11.55925 | -53.86428 | 2024-10-14 05:10:00 | NOAA-20 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ba11eae9-3b5a-38e5-92b7-1774c6d25e13 | -11.55677 | -53.85365 | 2024-10-14 05:10:00 | NOAA-20 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 543737b1-b389-34fd-bb8c-1a7e14f9695b | -11.55605 | -53.85869 | 2024-10-14 05:10:00 | NOAA-20 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 95d7aa4e-a9b7-3820-b89c-23167dca1430 | -11.55533 | -53.8637 | 2024-10-14 05:10:00 | NOAA-20 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| df9f0d5b-d323-3a75-ba45-330dee2153f5 | -11.55358 | -53.84796 | 2024-10-14 05:10:00 | NOAA-20 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| ba7640f9-358b-35b4-b06e-b38d3675e659 | -11.55285 | -53.85307 | 2024-10-14 05:10:00 | NOAA-20 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| c9f0fb75-dc17-3e28-aaeb-bac92d4bb9e4 | -11.54965 | -53.84739 | 2024-10-14 05:10:00 | NOAA-20 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 14d3b0fb-bca3-3ade-b8ac-c0b2f5591eb3 | -11.54573 | -53.84681 | 2024-10-14 05:10:00 | NOAA-20 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| deb2673e-bd17-3ac7-906d-472bb8a1adb4 | -11.5386 | -53.84053 | 2024-10-14 05:10:00 | NOAA-20 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 38ca5048-807c-3e2c-ae57-9be56646d4c4 | -12.89419 | -53.52599 | 2024-10-14 05:10:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 68274913-565a-3ea8-8111-d5f5fd1c0205 | -12.88705 | -53.54741 | 2024-10-14 05:10:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 8a4e8f36-9a25-3781-b74e-8e34d70f6801 | -12.885 | -53.53217 | 2024-10-14 05:10:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| b713e54b-00da-371f-a300-0d6ede1df803 | -12.88399 | -53.53952 | 2024-10-14 05:10:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| fb23d3b1-2c21-38d4-9d19-575449472c1a | -12.87787 | -53.52358 | 2024-10-14 05:10:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 6c2873d8-e8fa-30ed-9e5d-09fd99ab3dc6 | -12.87635 | -53.53463 | 2024-10-14 05:10:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| add3e0a8-7ed0-371e-b878-2cb769e26b9f | -12.87584 | -53.53831 | 2024-10-14 05:10:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 9ea7c9c2-2e46-3050-b6aa-988cdcdfded8 | -12.87329 | -53.52663 | 2024-10-14 05:10:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 1b4419d1-8328-3abc-a9c7-d6885856ca83 | -12.87278 | -53.53033 | 2024-10-14 05:10:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 6025ed5c-d6dd-383d-835a-74459ca26e41 | -12.88908 | -53.53278 | 2024-10-14 05:10:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 26d63d5a-97ff-378e-bf61-4fcb4c91c119 | -12.88857 | -53.53645 | 2024-10-14 05:10:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 280b576e-00bd-3800-8652-db0fc0e285c8 | -12.88807 | -53.54012 | 2024-10-14 05:10:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| c18c4cbb-ff6c-318c-a4ac-1eef08df5b1b | -12.88756 | -53.54377 | 2024-10-14 05:10:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| b7a3f59f-060d-3a96-858c-81ff7f7c4106 | -12.88551 | -53.5285 | 2024-10-14 05:10:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 806059aa-d363-3d1a-b5e4-3b2a902844c2 | -12.8845 | -53.53585 | 2024-10-14 05:10:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| aeb19c03-c72e-3182-91a9-b84766dec17b | -12.88348 | -53.54318 | 2024-10-14 05:10:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 88b79f61-4f0f-30fb-ad32-4291b17ffbe2 | -12.88298 | -53.54683 | 2024-10-14 05:10:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 94925223-27a4-3152-97d5-5816b244fd05 | -12.88144 | -53.52789 | 2024-10-14 05:10:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |


[Clique aqui para ver as próximas entradas](README115.md)
