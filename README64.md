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

## Dados Diários - Página 64

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 4275fd9d-4520-3d26-8136-24a39ea2e2cb | -17.93678 | -57.36722 | 2024-10-14 04:23:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 8.6 |
| 7a2ceb07-cfe0-39dc-b838-f3706cc921ab | -17.9367 | -57.37469 | 2024-10-14 04:23:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.1 |
| 9274ca07-c9c4-3c2a-addc-384646316240 | -17.93603 | -57.37088 | 2024-10-14 04:23:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.6 |
| d3d6590b-776c-3a7a-88ee-b697633317ff | -17.93527 | -57.37453 | 2024-10-14 04:23:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.6 |
| 02724872-6143-3bfb-9c76-31d2e46eb982 | -17.93208 | -57.36982 | 2024-10-14 04:23:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.0 |
| afdbe6a5-2bf9-3c0f-a582-a91b3045246a | -17.93129 | -57.37347 | 2024-10-14 04:23:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.0 |
| c94dd77a-58b8-3302-b29f-ad23790b87cc | -17.93063 | -57.36963 | 2024-10-14 04:23:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.6 |
| 8688bb20-836d-3dcb-9b42-63041d5e2901 | -17.92987 | -57.37329 | 2024-10-14 04:23:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.6 |
| 80e66dd7-f665-37fb-a956-32fef510c95e | -17.92671 | -57.36847 | 2024-10-14 04:23:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.0 |
| 7179e69f-2038-3467-9b1b-066290e0240b | -17.92593 | -57.37208 | 2024-10-14 04:23:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.0 |
| 26e1cf2e-257c-3b47-99eb-d352ef78ba41 | -17.92528 | -57.36816 | 2024-10-14 04:23:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.7 |
| 2a14b247-5c5c-3d4c-95ab-270285a93128 | -17.92453 | -57.37178 | 2024-10-14 04:23:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.7 |
| 4b5c1a2c-e62a-37e6-b60e-7eee13750efe | -17.9138 | -57.36893 | 2024-10-14 04:23:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 5.1 |
| 18853319-e6d2-3e9d-b447-eada8338ab40 | -17.90835 | -57.36797 | 2024-10-14 04:23:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 5.1 |
| 5ed05064-5710-3018-b4d1-ea4b5ba1add4 | -17.90759 | -57.37159 | 2024-10-14 04:23:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 6.7 |
| 45fe0bcc-46b2-3a45-81a2-9f5b2310a233 | -17.90213 | -57.37061 | 2024-10-14 04:23:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 10.8 |
| 488e76b1-bc40-391a-9867-24b439227a5b | -17.90135 | -57.37432 | 2024-10-14 04:23:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 10.8 |
| 9582d911-5f29-38f0-9597-f3e982a7f655 | -17.89593 | -57.37318 | 2024-10-14 04:23:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 10.8 |
| 65c92d1d-5ca7-346a-98a7-904c5403c4e8 | -17.89052 | -57.372 | 2024-10-14 04:23:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 7.5 |
| 22bd115a-86b2-331f-b1f7-618e2b00a394 | -17.2206 | -57.3145 | 2024-10-14 04:23:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.1 |
| 7473573f-3788-3a6b-9178-8c363b28cdd3 | -17.21981 | -57.31823 | 2024-10-14 04:23:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.1 |
| ab681df1-f8bf-3d30-b831-09d5830b0665 | -17.15128 | -56.84486 | 2024-10-14 04:23:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.6 |
| 8d4277a9-dc91-3078-ab9b-bfc435dfbc3b | -17.14699 | -56.86578 | 2024-10-14 04:23:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.4 |
| 64f2a81b-3367-3390-bc4c-b552729d034e | -17.14627 | -56.86929 | 2024-10-14 04:23:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.4 |
| 0d927a11-7bb0-32b5-99c6-4e58360dc506 | -17.14555 | -56.87279 | 2024-10-14 04:23:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.8 |
| 5362e934-c4f0-3de6-946a-502edda0cb9b | -17.14382 | -56.85414 | 2024-10-14 04:23:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.9 |
| 016d16af-b972-3325-b2e5-daee31b4903c | -17.14311 | -56.85762 | 2024-10-14 04:23:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.9 |
| 5b546227-748f-37d7-a51a-29e1dc695fe9 | -17.14239 | -56.86111 | 2024-10-14 04:23:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.9 |
| bbca5fb4-a972-3872-bdd4-de56da08767e | -17.14167 | -56.8646 | 2024-10-14 04:23:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.4 |
| 3b5b01f9-e70e-31ef-8cb8-f6fffa34f10a | -17.14095 | -56.86811 | 2024-10-14 04:23:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.4 |
| 7748cc93-9be2-3a7e-ab33-212035d4359e | -17.13636 | -56.86343 | 2024-10-14 04:23:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.0 |
| dffc98b9-4f28-30a0-a972-920a48c6a24c | -17.13564 | -56.86694 | 2024-10-14 04:23:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.0 |
| 47b0e9d9-1144-3b3e-8f6e-67da876c3c8e | -17.13491 | -56.87045 | 2024-10-14 04:23:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.8 |
| 930d6246-d2fc-3e1a-993b-90b161aa05fb | -17.13104 | -56.86227 | 2024-10-14 04:23:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.0 |
| adc8003e-20f3-3997-ae5a-b8da4bb052da | -17.13032 | -56.86576 | 2024-10-14 04:23:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.0 |
| c72de09b-fef0-350a-b185-258b8c260189 | -17.12959 | -56.86927 | 2024-10-14 04:23:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.8 |
| 9575685c-b0be-36cd-8ca0-395b343e4dae | -17.12428 | -56.8681 | 2024-10-14 04:23:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.3 |
| c3fcdff7-2d28-3453-aa10-cc40936c6f7e | -17.12355 | -56.87159 | 2024-10-14 04:23:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.3 |
| b0f3aa46-0d85-30d3-8e6e-b83d482b26b3 | -17.11969 | -56.86341 | 2024-10-14 04:23:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.1 |
| 331fc41d-46ca-302c-9d14-fc153c6904f9 | -17.11896 | -56.86691 | 2024-10-14 04:23:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.3 |
| 91f421b6-6064-3de2-b752-abbf7675dc37 | -17.11823 | -56.87041 | 2024-10-14 04:23:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.3 |
| e2d94f16-2ed2-343b-a9e8-dbff0117790f | -17.93045 | -57.31623 | 2024-10-14 04:23:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.8 |
| 28bccaee-d7d8-3150-8328-08b065d10ea1 | -17.9297 | -57.31985 | 2024-10-14 04:23:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.8 |
| 22d3100c-45f6-3b29-8a7d-3929af4b47dc | -17.92894 | -57.32349 | 2024-10-14 04:23:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.0 |
| c28206c6-618d-36ec-8980-253fce58983c | -17.92818 | -57.32712 | 2024-10-14 04:23:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.0 |
| e778cbc3-4139-3a37-ab35-8061a9771fa8 | -17.9281 | -57.30051 | 2024-10-14 04:23:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 8.6 |
| ecccfc8a-2f32-3da4-9405-6f25170edc1c | -17.92735 | -57.30413 | 2024-10-14 04:23:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 8.6 |
| c21a9bef-19e7-3d48-a96c-5d7488ac44c5 | -17.92659 | -57.30776 | 2024-10-14 04:23:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.4 |
| 7468e973-c04c-3b5f-8bd9-12da00089d74 | -17.92583 | -57.31139 | 2024-10-14 04:23:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.4 |
| cfab607b-920d-32cd-8779-ebb157d5ec0c | -17.92507 | -57.31501 | 2024-10-14 04:23:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.7 |
| 52d35af4-419c-3e50-adda-1339fc3d947b | -17.92431 | -57.31864 | 2024-10-14 04:23:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.7 |
| 067b6af5-d410-3f73-950d-90f947173892 | -17.92272 | -57.2993 | 2024-10-14 04:23:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 8.6 |
| 7b3439b8-cf27-309a-8609-056b491a59f9 | -17.9181 | -57.29445 | 2024-10-14 04:23:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 76.5 |
| 511b289a-6e27-3db2-a529-eca36c9732cc | -17.90892 | -57.31133 | 2024-10-14 04:23:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 6.0 |
| d11aca80-ec3e-399c-834d-0fa4a65ebc11 | -17.90659 | -57.29563 | 2024-10-14 04:23:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 62.0 |
| a6c4c2f1-64a1-3bd3-99ff-d49a2230c2ba | -17.90121 | -57.29439 | 2024-10-14 04:23:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 62.0 |
| da286c7d-d03f-3d4b-a11f-079488e93ffd | -17.89816 | -57.30887 | 2024-10-14 04:23:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 5.6 |
| 1dafca82-b7bd-334c-a148-bfe4c07798c5 | -17.89355 | -57.30402 | 2024-10-14 04:23:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 11.5 |
| 556ab83b-3ac2-3765-9c5f-3cf7cb4e3ebb | -17.89278 | -57.30765 | 2024-10-14 04:23:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.4 |
| 053d0d14-12e2-3ef9-9768-b943859ac978 | -17.89201 | -57.31128 | 2024-10-14 04:23:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.4 |
| 2b76f49d-1de5-3145-90c6-5f32c9eb0fd8 | -17.89122 | -57.28833 | 2024-10-14 04:23:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 9.9 |
| d343f2b9-a850-32f1-912f-6629657bded0 | -17.8897 | -57.29554 | 2024-10-14 04:23:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 82.0 |
| baa8a742-edbb-3704-ade5-86cf4949e2e0 | -17.8874 | -57.30643 | 2024-10-14 04:23:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.4 |
| 5e88c092-2cc5-37f5-806c-59819c890bda | -17.88355 | -57.29796 | 2024-10-14 04:23:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 11.8 |
| 2d00b519-c539-3110-ae11-ef7bffde5467 | -17.87971 | -57.28948 | 2024-10-14 04:23:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 39.5 |
| ad9b8d33-0f57-34b7-81ec-a43b586fc064 | -17.86971 | -57.31003 | 2024-10-14 04:23:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 0.9 |
| e0e58913-62c4-3019-a7ad-e54ee9bf6868 | -17.86896 | -57.28703 | 2024-10-14 04:23:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 10.4 |
| 716f94d1-e93a-3477-ad85-9183a4584620 | -17.86893 | -57.31365 | 2024-10-14 04:23:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 0.9 |
| 46c570b3-fbce-3a7c-8f4c-fced71d39df1 | -17.86741 | -57.29429 | 2024-10-14 04:23:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 26.7 |
| 08404447-8164-39a0-9cda-c6417b48ba18 | -17.86586 | -57.30156 | 2024-10-14 04:23:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 4.0 |
| 1c92df89-4962-392a-96d1-5dd679dbba9f | -17.86432 | -57.3088 | 2024-10-14 04:23:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 0.9 |
| 995bf4fc-fa73-3b34-b9e7-3c5987f10472 | -17.86357 | -57.28584 | 2024-10-14 04:23:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 8.4 |
| 4927f703-8a0b-3c40-b4e7-217ba7c54012 | -17.86354 | -57.31243 | 2024-10-14 04:23:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 0.9 |
| 2c577dcb-f080-39bd-a9fa-32c1aa883a48 | -17.85896 | -57.28104 | 2024-10-14 04:23:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.5 |
| 7592a308-5f0c-3f3f-ba82-3fb580fafbb4 | -17.85893 | -57.30759 | 2024-10-14 04:23:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.7 |
| 39180ee9-f5d2-3b01-82ac-50e94a752001 | -17.85432 | -57.30275 | 2024-10-14 04:23:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 9.7 |
| 9e9506c4-f6e5-3948-a633-73dd6e0e753f | -17.85184 | -57.27931 | 2024-10-14 04:23:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 0.5 |
| 1becad7d-a9ed-325c-a5b7-7f5052070567 | -17.85049 | -57.29428 | 2024-10-14 04:23:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 21.0 |
| 4f3af4b5-32fa-377a-8311-a8b5d0362fd5 | -17.84894 | -57.30152 | 2024-10-14 04:23:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 15.7 |
| 0577240e-b977-3df7-8ae1-276f963ba99a | -17.8451 | -57.29307 | 2024-10-14 04:23:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 21.0 |
| c4753d63-2d1b-32e2-9449-2f77f93c6140 | -17.84355 | -57.3003 | 2024-10-14 04:23:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 15.7 |
| 24a80780-ffc2-32b0-b89a-4ca2735382dd | -17.83971 | -57.31069 | 2024-10-14 04:23:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 17.3 |
| 9a373181-e251-3cae-8ac0-96fb99a0d53d | -17.83816 | -57.29911 | 2024-10-14 04:23:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 15.0 |
| 01e7ea68-b7fc-3465-8607-9c5451f87855 | -17.83739 | -57.30271 | 2024-10-14 04:23:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 23.9 |
| af1a7594-de0f-353b-869d-1166c5962267 | -17.83732 | -57.29498 | 2024-10-14 04:23:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 12.1 |
| d6adda72-0c31-3f17-acbf-f6259a1cc033 | -17.83583 | -57.30994 | 2024-10-14 04:23:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 13.9 |
| 5d6c0cbd-b6c8-3639-bcbb-562312b73103 | -17.83505 | -57.31358 | 2024-10-14 04:23:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 13.9 |
| 3d56bdca-72b5-3afb-b8c7-20405e856ce1 | -17.83431 | -57.30947 | 2024-10-14 04:23:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 17.3 |
| 6d888ba0-4089-38f0-b6be-be235807aaa0 | -17.83356 | -57.31311 | 2024-10-14 04:23:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 17.3 |
| 9e35d648-d2a1-311e-91b6-38218be159ac | -17.83122 | -57.30512 | 2024-10-14 04:23:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 23.9 |
| ef05ca87-24aa-333e-9232-e3b3d448edbe | -17.82892 | -57.30825 | 2024-10-14 04:23:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 10.0 |
| 0b35d5f9-ea92-339d-8120-8a87780bec0d | -17.82887 | -57.316 | 2024-10-14 04:23:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 8.5 |
| 271b0c81-7e09-3f16-8842-8879132eef67 | -17.82817 | -57.31189 | 2024-10-14 04:23:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 10.0 |
| f9600df5-a823-3d23-ae98-65592276fbf2 | -17.82809 | -57.31964 | 2024-10-14 04:23:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 8.5 |
| 0d5e98fb-dff1-324d-897c-88771ef87859 | -17.82741 | -57.31553 | 2024-10-14 04:23:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 12.3 |
| ecb53511-a9fc-3f9e-8472-ba917924b08e | -17.82731 | -57.32327 | 2024-10-14 04:23:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 5.7 |
| bda04698-083e-3f75-9c3d-b93926ff58e8 | -17.82665 | -57.31917 | 2024-10-14 04:23:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 12.3 |
| cb58c155-cdc9-3df5-b77a-bb0ff672a143 | -17.8259 | -57.32281 | 2024-10-14 04:23:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 8.0 |
| b9b4c30c-bb49-3ac0-be83-a5c81a093cf4 | -17.91582 | -57.30534 | 2024-10-14 04:23:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 11.9 |
| acf395af-e7e4-384f-96a4-4eb866741d40 | -17.90735 | -57.29201 | 2024-10-14 04:23:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 64.5 |


[Clique aqui para ver as próximas entradas](README65.md)
