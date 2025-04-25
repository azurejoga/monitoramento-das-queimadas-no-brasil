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

## Dados Diários - Página 3

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 32ad6033-8a85-35f4-9209-d9323b54d567 | -28.58494 | -49.44153 | 2025-04-25 04:34:00 | NPP-375D | SIDERÓPOLIS | SANTA CATARINA | Brasil | 4217600 | 42 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| f121455e-4321-364c-b130-9e46070cd1da | -3.43631 | -51.2435 | 2025-04-25 04:46:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 8644dfff-b80f-3393-8720-d10f052bdeae | -11.27706 | -52.46753 | 2025-04-25 04:49:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| f062ebb2-98c0-378d-a44c-7aa87bde8cd0 | -8.33532 | -55.09279 | 2025-04-25 04:49:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| be1f2f28-0d55-37b5-86c9-8bb4aabf4df9 | -11.40384 | -52.94383 | 2025-04-25 04:49:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a6aa0934-8d86-324f-8470-a28b77e8550f | -11.39719 | -52.94277 | 2025-04-25 04:49:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 12be3036-9e27-3cda-83c1-9729765ad151 | -8.7897 | -49.80787 | 2025-04-25 04:49:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 938707c2-aac0-3e50-9c91-22a01f46471e | -11.39887 | -52.95393 | 2025-04-25 04:49:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 423d0ddd-bb6e-3c5b-9a3d-37d2dc06dece | -11.40275 | -52.95092 | 2025-04-25 04:49:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 4.2 |
| c5023319-2eba-3280-ae9a-ed118de5542c | -11.40106 | -52.93975 | 2025-04-25 04:49:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 7.7 |
| af028494-a1f4-373d-a70b-ddc4cfca7e48 | -8.10411 | -43.12107 | 2025-04-25 04:49:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 341605c0-9207-35ce-82c1-1e2d1fce1da9 | -5.30282 | -55.97207 | 2025-04-25 04:49:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| e063ac4d-614e-36de-b291-1b76b9e39aaf | -9.16303 | -61.95349 | 2025-04-25 04:49:00 | NOAA-20 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 13927364-f06a-3dde-a993-b20a52a770c7 | -8.08232 | -43.11437 | 2025-04-25 04:49:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 2b00732f-49f7-31af-987d-543134aab7dd | -9.34009 | -50.97898 | 2025-04-25 04:49:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 0.3 |
| 4aabe06f-972e-3b26-bdb8-a45193330ee5 | -9.34355 | -50.97951 | 2025-04-25 04:49:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| a59625c6-d5ab-3c3b-8dd1-7182d66c368b | -11.2709 | -52.46288 | 2025-04-25 04:49:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| ac914744-5bab-3e3e-8f14-101f5ca4d2d7 | -11.27481 | -52.45981 | 2025-04-25 04:49:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 0.3 |
| 21e9fe7f-f562-3adf-86a3-7932c4f41150 | -11.40662 | -52.9479 | 2025-04-25 04:49:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 67ecfbd4-ff06-3082-a79d-ab2f17eb539b | -11.2592 | -52.47207 | 2025-04-25 04:49:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a6993da1-1872-362d-87db-a78175421e4b | -11.32792 | -54.24774 | 2025-04-25 04:49:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 0e610c8c-cbc4-3672-a490-8721e3b99f08 | -11.40165 | -52.958 | 2025-04-25 04:49:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 03fc23e0-2bd2-3a34-b01a-bd7818b34c09 | -11.40995 | -52.94842 | 2025-04-25 04:49:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 78268a80-05a3-3584-8817-2761bb805d17 | -11.39942 | -52.95039 | 2025-04-25 04:49:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 3.4 |
| c9a1874e-43da-312a-81bf-0d38d0fd237e | -8.17671 | -46.70485 | 2025-04-25 04:49:00 | NOAA-20 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| e1e3b97c-467e-37c6-a391-74c7e21684f5 | -11.40439 | -52.94028 | 2025-04-25 04:49:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 2f5b5f9c-8ab7-3778-ae65-bc84f8cf95cb | -11.40607 | -52.95144 | 2025-04-25 04:49:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 4.2 |
| c043b644-b42f-30b8-be3b-7f5477bcaaf9 | -11.40329 | -52.94737 | 2025-04-25 04:49:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| bc179681-af1f-3bd2-86b4-db58138aba15 | -11.4094 | -52.95197 | 2025-04-25 04:49:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 3473f1c7-2b41-3cd9-9180-9411750b826f | -8.867 | -49.89114 | 2025-04-25 04:49:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 50250c6d-414a-3ab1-93fc-6bfd591da5cf | -8.10966 | -43.12197 | 2025-04-25 04:49:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 731a9a4f-efad-3bcc-b818-9b341aa47349 | -7.43728 | -45.42324 | 2025-04-25 04:49:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 26efe7b1-3ce8-3916-b4e3-18c2cf1d3fe8 | -11.40051 | -52.9433 | 2025-04-25 04:49:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 73823867-9c31-3af9-8743-4fd0826f3418 | -11.27426 | -52.46341 | 2025-04-25 04:49:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| d63f4749-511d-3228-8df0-f33ecaa16a28 | -8.86338 | -49.89059 | 2025-04-25 04:49:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| b2e52431-ae74-34fd-a3bd-86ab187d6385 | -11.39774 | -52.93922 | 2025-04-25 04:49:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 7.7 |
| 750f8c73-aef2-32f1-a03d-7c8b935e63b9 | -4.12971 | -54.89742 | 2025-04-25 04:49:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| ae3bd63a-1106-3479-aee9-b15dbe8374bd | -11.27761 | -52.46394 | 2025-04-25 04:49:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 8a392d51-cd7e-34ac-b0e4-907ff0a8d590 | -11.4022 | -52.95446 | 2025-04-25 04:49:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 4.2 |
| ba65cc44-81c1-35fb-9d76-daa12a6705c4 | -11.27816 | -52.46034 | 2025-04-25 04:49:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 0.3 |
| c6ea4bfc-545c-3c23-af04-1cb194805ccb | -8.79034 | -49.80363 | 2025-04-25 04:49:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 4f76dcac-34a8-3b95-8c5b-49d85980926e | -11.39997 | -52.94685 | 2025-04-25 04:49:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 86e281a8-c3ef-3384-a6a5-74022217bfc1 | -11.40553 | -52.95498 | 2025-04-25 04:49:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 06acc4b2-42ad-3afe-a545-7951ad45ab17 | -11.27371 | -52.467 | 2025-04-25 04:49:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| c2c692b5-8a88-34c6-b21d-5c477d2cce26 | -12.3652 | -60.80411 | 2025-04-25 04:51:00 | NOAA-20 | CHUPINGUAIA | RONDÔNIA | Brasil | 1100924 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 74e99ff7-770c-3902-838a-937c064ba846 | -12.01012 | -62.84576 | 2025-04-25 04:51:00 | NOAA-20 | SÃO MIGUEL DO GUAPORÉ | RONDÔNIA | Brasil | 1100320 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 0cd1d7b7-a388-32a9-bf30-ded82dc5e380 | -13.73868 | -53.38055 | 2025-04-25 04:51:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 013680eb-c1a3-399f-a789-a41c540cd206 | -12.00431 | -62.84791 | 2025-04-25 04:51:00 | NOAA-20 | SÃO MIGUEL DO GUAPORÉ | RONDÔNIA | Brasil | 1100320 | 11 | 33 | nan | nan | nan | Amazônia | 0.4 |
| b31f8e63-6366-347f-b1fe-839f86ea99c0 | -16.15841 | -59.24438 | 2025-04-25 04:51:00 | NOAA-20 | PORTO ESPERIDIÃO | MATO GROSSO | Brasil | 5106828 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 1e5da546-37d9-33a9-90a9-11cb34545330 | -29.95664 | -51.14888 | 2025-04-25 04:55:00 | NOAA-20 | CANOAS | RIO GRANDE DO SUL | Brasil | 4304606 | 43 | 33 | nan | nan | nan | Pampa | 0.6 |
| 72190d7c-2360-3bcc-abb3-5613f1cf31c6 | -26.3353 | -53.18872 | 2025-04-25 04:55:00 | NOAA-20 | FLOR DA SERRA DO SUL | PARANÁ | Brasil | 4107850 | 41 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 6fe04999-a2b6-3ec5-ba68-d643cdac6cd9 | -8.72168 | -44.0209 | 2025-04-25 05:33:00 | AQUA_M-M | CRISTINO CASTRO | PIAUÍ | Brasil | 2203107 | 22 | 33 | nan | nan | nan | Cerrado | 4.6 |
| f9dad33e-20ba-3969-8b9f-101442179016 | -11.40036 | -52.93438 | 2025-04-25 05:33:00 | AQUA_M-M | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 35.1 |
| f2217ff2-c95d-3bdd-9f1f-a55d328bafc7 | -8.10618 | -43.11718 | 2025-04-25 05:33:00 | AQUA_M-M | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 5.0 |
| 838f6eb9-634e-313b-b7db-6e5724b5e601 | -8.07833 | -43.11324 | 2025-04-25 05:33:00 | AQUA_M-M | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 4.8 |
| 43cce1f6-82e2-3798-bdf8-94766badd2e6 | 0.37156 | -60.52692 | 2025-04-25 05:40:00 | NOAA-21 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 4a6e6b1d-7b94-3aff-98e5-1d55da3a3aaf | 2.56001 | -61.31461 | 2025-04-25 05:40:00 | NOAA-21 | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 94c3bb1a-ee65-36f3-8df6-3e2314547ff2 | 2.30921 | -60.5891 | 2025-04-25 05:40:00 | NOAA-21 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 0df9440a-c01d-328f-ad9f-973d299c89d8 | -11.27216 | -52.46471 | 2025-04-25 05:42:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 714d54c2-2b1b-337f-baa9-566e3fbc7cd3 | -11.27927 | -52.46552 | 2025-04-25 05:42:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 442001fc-67af-3cdb-ad1e-93dc83972233 | -9.1636 | -61.95107 | 2025-04-25 05:42:00 | NOAA-21 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 20d21a6b-4bc9-3d3b-9740-ce631a4ee928 | -11.27494 | -52.46454 | 2025-04-25 05:42:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 4.0 |
| fd7f27de-f69f-3f20-bdff-f211ef419ba7 | -9.16293 | -61.95559 | 2025-04-25 05:42:00 | NOAA-21 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 367cdb20-5dbd-3af2-a8b0-062ce6ae95bf | -12.01127 | -62.84313 | 2025-04-25 05:44:00 | NOAA-21 | SÃO MIGUEL DO GUAPORÉ | RONDÔNIA | Brasil | 1100320 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| f83ab7c0-b76f-3857-bb07-ff19ea35291d | -12.36572 | -60.80563 | 2025-04-25 05:44:00 | NOAA-21 | CHUPINGUAIA | RONDÔNIA | Brasil | 1100924 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 9901274f-e580-393a-82e6-985f5d4c390a | -11.3963 | -52.9477 | 2025-04-25 06:50:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 46.0 |
| 42629e7a-5a98-3ff7-bae2-95ef8625102a | -11.3963 | -52.9477 | 2025-04-25 07:20:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 43.2 |
| 099aada0-7e0f-3906-89b0-5e202f67bcd9 | -11.3963 | -52.9477 | 2025-04-25 07:30:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 54.3 |
| 6dafd59f-3ef7-3b69-8d95-1e4d50a85c56 | -11.4152 | -52.9458 | 2025-04-25 08:30:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 44.6 |
| 1853854f-6d7f-32bc-8b10-be4594cbfab7 | -8.38748 | -40.07228 | 2025-04-25 12:14:00 | TERRA_M-T | SANTA MARIA DA BOA VISTA | PERNAMBUCO | Brasil | 2612604 | 26 | 33 | nan | nan | nan | Caatinga | 13.6 |
| 4172a687-c305-36c8-b595-7c5502dcf1c5 | -8.07913 | -43.10887 | 2025-04-25 12:14:00 | TERRA_M-T | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 6.5 |
| 4a67d149-0c90-33ac-9aa6-cfb14f0e7aff | -8.65554 | -39.43268 | 2025-04-25 12:14:00 | TERRA_M-T | CURAÇÁ | BAHIA | Brasil | 2909901 | 29 | 33 | nan | nan | nan | Caatinga | 9.9 |
| 3d8853f7-ca27-33fa-8c3b-011af932ac4d | -8.07786 | -43.11779 | 2025-04-25 12:14:00 | TERRA_M-T | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 5.7 |
| 412973b7-9dc4-39c8-857f-c8a1655ca836 | -13.1699 | -45.23162 | 2025-04-25 12:17:00 | TERRA_M-T | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 7.7 |
| 17f424e9-6b7d-3785-a9c5-af62edbe67b3 | -8.49194 | -44.47143 | 2025-04-25 12:17:00 | TERRA_M-T | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 266292ee-93c7-3b72-a810-005dc0328755 | -14.34075 | -44.58591 | 2025-04-25 12:17:00 | TERRA_M-T | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 5.7 |
| a181108a-fd1a-3125-b017-4c39c17f4dd0 | -8.99815 | -41.00312 | 2025-04-25 12:17:00 | TERRA_M-T | CASA NOVA | BAHIA | Brasil | 2907202 | 29 | 33 | nan | nan | nan | Caatinga | 9.1 |
| 09d3ce44-5fe2-3046-9bf0-da61bd7a07d1 | -11.80976 | -43.78721 | 2025-04-25 12:17:00 | TERRA_M-T | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 7.0 |
| 34303620-3142-312c-803d-a230e022b474 | -14.66842 | -42.67809 | 2025-04-25 12:17:00 | TERRA_M-T | URANDI | BAHIA | Brasil | 2932606 | 29 | 33 | nan | nan | nan | Caatinga | 11.0 |
| e9e3df29-5c0f-3664-8786-0275ff82db67 | -13.48788 | -42.96907 | 2025-04-25 12:17:00 | TERRA_M-T | RIACHO DE SANTANA | BAHIA | Brasil | 2926400 | 29 | 33 | nan | nan | nan | Caatinga | 9.8 |
| 63bd1ffd-657f-3d60-9d1b-81bb9eeda0df | -11.80848 | -43.79627 | 2025-04-25 12:17:00 | TERRA_M-T | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 13.4 |
| e395faca-2235-3bb9-86a6-84cdf189064f | -9.89802 | -38.31317 | 2025-04-25 12:17:00 | TERRA_M-T | JEREMOABO | BAHIA | Brasil | 2918100 | 29 | 33 | nan | nan | nan | Caatinga | 19.3 |
| c332a8c7-3544-3382-a44a-88627769f4fe | -13.48921 | -42.95915 | 2025-04-25 12:17:00 | TERRA_M-T | RIACHO DE SANTANA | BAHIA | Brasil | 2926400 | 29 | 33 | nan | nan | nan | Caatinga | 8.8 |
| 824b496a-68f8-3236-81fb-84437823a8e1 | -8.99963 | -40.99216 | 2025-04-25 12:17:00 | TERRA_M-T | CASA NOVA | BAHIA | Brasil | 2907202 | 29 | 33 | nan | nan | nan | Caatinga | 14.0 |
| 284db179-c426-397a-8397-aedaa974c0fa | -13.4779 | -42.49889 | 2025-04-25 12:17:00 | TERRA_M-T | TANQUE NOVO | BAHIA | Brasil | 2931053 | 29 | 33 | nan | nan | nan | Caatinga | 29.5 |
| f87cbd61-cb55-388c-9b32-a94e183903cb | -16.50207 | -45.14522 | 2025-04-25 12:19:00 | TERRA_M-T | SÃO ROMÃO | MINAS GERAIS | Brasil | 3164209 | 31 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 803ce87d-7fbe-31ae-907c-3bb6a4601337 | -18.9552 | -39.79637 | 2025-04-25 12:19:00 | TERRA_M-T | SÃO MATEUS | ESPÍRITO SANTO | Brasil | 3204906 | 32 | 33 | nan | nan | nan | Mata Atlântica | 19.6 |
| 12b87d3f-8d25-37a4-8e5e-ccb500c8b5a1 | -17.49563 | -45.28741 | 2025-04-25 12:19:00 | TERRA_M-T | BURITIZEIRO | MINAS GERAIS | Brasil | 3109402 | 31 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 4a2bf736-3e9a-3b26-b733-846e083a1604 | -26.86578 | -50.62967 | 2025-04-25 12:21:00 | TERRA_M-T | LEBON RÉGIS | SANTA CATARINA | Brasil | 4209706 | 42 | 33 | nan | nan | nan | Mata Atlântica | 5.6 |


