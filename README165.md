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

## Dados Diários - Página 165

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 37b176b8-dbcb-3358-a208-6d06a96ffbb5 | -8.82969 | -63.703 | 2024-09-26 05:48:00 | NOAA-20 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 5.3 |
| eba499d2-4a17-3fdb-9318-a078b5562d4f | -8.82903 | -63.70739 | 2024-09-26 05:48:00 | NOAA-20 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 4.7 |
| f0ae80d7-5ff5-386d-a2ab-c5a870837ad4 | -8.82903 | -63.70065 | 2024-09-26 05:48:00 | NOAA-20 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 0aa5146c-3a14-3fa4-86d3-6bbe9f911c40 | -8.82839 | -63.70504 | 2024-09-26 05:48:00 | NOAA-20 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 8.5 |
| 8dcb4d46-93b6-3d67-8a24-68d73eaf1bdb | -8.82837 | -63.71176 | 2024-09-26 05:48:00 | NOAA-20 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 4.7 |
| ea196ceb-0b29-3ce6-b38e-71a72ee72d14 | -8.82776 | -63.70942 | 2024-09-26 05:48:00 | NOAA-20 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 8.5 |
| df9c1106-13dc-3068-8096-cf84eadced80 | -8.82666 | -63.69804 | 2024-09-26 05:48:00 | NOAA-20 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 1145f303-27ac-3a06-aaae-fa5450eeab1e | -8.826 | -63.70243 | 2024-09-26 05:48:00 | NOAA-20 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 49b15992-790e-3786-bc87-40c8f732faf2 | -8.82535 | -63.70681 | 2024-09-26 05:48:00 | NOAA-20 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 232945a1-8d90-3d38-b3d2-de92150ec454 | -8.82534 | -63.70007 | 2024-09-26 05:48:00 | NOAA-20 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 440a33a5-4d55-3c2c-92af-df2d24bf0259 | -8.82471 | -63.70447 | 2024-09-26 05:48:00 | NOAA-20 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 8.5 |
| 04319cdf-520b-3206-ab9b-40b0d184f29b | -10.7061 | -63.532 | 2024-09-26 05:48:00 | NOAA-20 | GOVERNADOR JORGE TEIXEIRA | RONDÔNIA | Brasil | 1101005 | 11 | 33 | nan | nan | nan | Amazônia | 1.9 |
| e7014aa3-9571-32d6-b766-8dbd73501738 | -10.69993 | -63.47506 | 2024-09-26 05:48:00 | NOAA-20 | GOVERNADOR JORGE TEIXEIRA | RONDÔNIA | Brasil | 1101005 | 11 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 1e7238a9-52ae-36e0-8a8b-ddc926bd6fb2 | -10.69888 | -63.47217 | 2024-09-26 05:48:00 | NOAA-20 | GOVERNADOR JORGE TEIXEIRA | RONDÔNIA | Brasil | 1101005 | 11 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 8dbf1ec8-95ef-346d-bcb1-7dc43a2dd6fa | -10.6954 | -63.47931 | 2024-09-26 05:48:00 | NOAA-20 | GOVERNADOR JORGE TEIXEIRA | RONDÔNIA | Brasil | 1101005 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 217a61f8-ed2f-313a-90fe-785c6bca9c08 | -10.69471 | -63.48403 | 2024-09-26 05:48:00 | NOAA-20 | GOVERNADOR JORGE TEIXEIRA | RONDÔNIA | Brasil | 1101005 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| cec5afdc-5c38-3558-95a4-00007bd06544 | -10.69438 | -63.47643 | 2024-09-26 05:48:00 | NOAA-20 | GOVERNADOR JORGE TEIXEIRA | RONDÔNIA | Brasil | 1101005 | 11 | 33 | nan | nan | nan | Amazônia | 2.6 |
| b441a69f-3203-3fd1-b383-6ecbf2aa9b91 | -10.69371 | -63.48123 | 2024-09-26 05:48:00 | NOAA-20 | GOVERNADOR JORGE TEIXEIRA | RONDÔNIA | Brasil | 1101005 | 11 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 43fe8499-5610-3097-99cd-cb805d56c9d6 | -10.69157 | -63.47876 | 2024-09-26 05:48:00 | NOAA-20 | GOVERNADOR JORGE TEIXEIRA | RONDÔNIA | Brasil | 1101005 | 11 | 33 | nan | nan | nan | Amazônia | 2.5 |
| e93f0493-a998-3b3f-a29a-9f7c3dab9450 | -10.69088 | -63.48349 | 2024-09-26 05:48:00 | NOAA-20 | GOVERNADOR JORGE TEIXEIRA | RONDÔNIA | Brasil | 1101005 | 11 | 33 | nan | nan | nan | Amazônia | 2.5 |
| cd33dcf1-734a-303d-9c88-0d14226279be | -10.69063 | -64.14424 | 2024-09-26 05:48:00 | NOAA-20 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| af294829-b999-3c10-ac7e-39dbad7eabbc | -10.68706 | -63.48294 | 2024-09-26 05:48:00 | NOAA-20 | GOVERNADOR JORGE TEIXEIRA | RONDÔNIA | Brasil | 1101005 | 11 | 33 | nan | nan | nan | Amazônia | 2.5 |
| f82741ef-4b64-3675-b5c8-140263a507f1 | -10.68694 | -64.14368 | 2024-09-26 05:48:00 | NOAA-20 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 5df8c2ad-94f2-36b2-ab41-f283b899144e | -10.56872 | -64.0061 | 2024-09-26 05:48:00 | NOAA-20 | CAMPO NOVO DE RONDÔNIA | RONDÔNIA | Brasil | 1100700 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 5ceb0819-55fb-3bd6-acd6-a48a1899f1a4 | -10.5644 | -64.00974 | 2024-09-26 05:48:00 | NOAA-20 | CAMPO NOVO DE RONDÔNIA | RONDÔNIA | Brasil | 1100700 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 96c8d5f1-41dc-3251-b8b2-f7000d28bfe3 | -10.55046 | -64.48552 | 2024-09-26 05:48:00 | NOAA-20 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 60154525-0827-3f55-bc3f-04021ed032eb | -10.11201 | -64.42085 | 2024-09-26 05:48:00 | NOAA-20 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 2.4 |
| aafef6ad-f373-33ac-8ee0-87ea8558f7d7 | -10.11076 | -64.42921 | 2024-09-26 05:48:00 | NOAA-20 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 3f83f2e5-27ee-3e8b-8f6a-70e071f5f493 | -10.10715 | -64.4287 | 2024-09-26 05:48:00 | NOAA-20 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 14d4b2be-f806-3db8-8619-fdbfeaf25015 | -9.33182 | -64.24492 | 2024-09-26 05:48:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 71f43db8-fb20-30ae-bf3d-2646b3abf153 | -10.86106 | -64.17582 | 2024-09-26 05:48:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c74e7e39-a41c-3437-b79d-6bf4d6302ea4 | -10.86038 | -64.1805 | 2024-09-26 05:48:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 6600b130-07e0-3827-a615-ed1a4e5676c9 | -10.85671 | -64.17988 | 2024-09-26 05:48:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 0e6954d2-a2b2-3edd-9ba7-80c74f5baa60 | -10.85609 | -64.18417 | 2024-09-26 05:48:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 177004db-22aa-33e6-a49b-7c4378dc357f | -10.85242 | -64.18352 | 2024-09-26 05:48:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 2.6 |
| c0d4bcf2-938f-3330-ad03-c7b9cf0fafe9 | -10.85181 | -64.18774 | 2024-09-26 05:48:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 1f2d3739-44b3-3390-b91e-8f0f3a103475 | -10.84855 | -64.21031 | 2024-09-26 05:48:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 2a9cf8d6-bdb3-342f-8384-759bf4a31d19 | -10.84792 | -64.21474 | 2024-09-26 05:48:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 9e4d38d9-ff4c-3e8e-9fb8-147bb12d9bc0 | -10.84488 | -64.20975 | 2024-09-26 05:48:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 6ec74fcc-2c1e-37c4-a85a-681535b94a11 | -10.84424 | -64.21415 | 2024-09-26 05:48:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a598d662-9371-3acd-9c02-a84579cac692 | -9.32262 | -65.36454 | 2024-09-26 05:48:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c6744482-d24a-3d96-8def-6ccc60816e31 | -9.32094 | -65.30627 | 2024-09-26 05:48:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| a46b5263-1313-3d40-9fe3-198be13441d1 | -9.3175 | -65.30576 | 2024-09-26 05:48:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| e50d33b2-fbb0-3885-b7f0-b241edbb76b8 | -9.31349 | -65.35527 | 2024-09-26 05:48:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 2c2252ff-b080-3363-bf48-ffb15130eb46 | -9.31174 | -65.34364 | 2024-09-26 05:48:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 1016a7d4-2f22-39c1-9a5f-67a4215a01e6 | -9.2603 | -65.38171 | 2024-09-26 05:48:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 4a6a2b83-485e-3325-a07a-a7476fe2d12a | -9.31292 | -65.35901 | 2024-09-26 05:48:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| cb3b4ce9-0a2e-3889-8bd6-4a4706d8f5e3 | -9.31062 | -65.35104 | 2024-09-26 05:48:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 8e4fde96-7dba-393e-b5bb-6295404615ec | -9.25687 | -65.38119 | 2024-09-26 05:48:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 7992a8db-0b23-3a2f-81c7-22edeed97804 | -9.254 | -65.37691 | 2024-09-26 05:48:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ec1d4134-c72c-399c-9f75-9eea2bfd6e00 | -9.23252 | -65.3584 | 2024-09-26 05:48:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ed2cb2c0-95fc-37d1-bd23-c6e38e244257 | -9.23223 | -65.35811 | 2024-09-26 05:48:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 68f5c116-6142-30b7-9433-51835e7cfa59 | -9.03 | -65.4702 | 2024-09-26 05:48:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 45ecc73a-2bf3-3009-bcf4-c2f90ce0d342 | -9.40652 | -64.37409 | 2024-09-26 05:48:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 99838b68-b125-3f80-8695-77d26f1cc494 | -9.31692 | -65.30957 | 2024-09-26 05:48:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 693e7ed9-4ecd-34d0-8ca8-65a56fea3a21 | -9.31177 | -65.32031 | 2024-09-26 05:48:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d5065e7f-58d2-3a5e-94c7-9cb9425bd6ea | -9.31006 | -65.35471 | 2024-09-26 05:48:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 07a02dd7-f26a-34e1-9c85-d7897f5f699f | -9.30775 | -65.34679 | 2024-09-26 05:48:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e1e2783e-20ee-3361-9c61-0719ef6c0cf2 | -9.24477 | -65.66881 | 2024-09-26 05:48:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 682c5996-9d43-3578-a90a-3253c51cc7d4 | -9.23567 | -65.35864 | 2024-09-26 05:48:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| cb63577f-cb8e-3f2c-b992-8fbd6f14cd05 | -9.76455 | -65.28915 | 2024-09-26 05:48:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 941a858e-567a-37c1-b25c-3b6dbbee1fe4 | -9.76397 | -65.29296 | 2024-09-26 05:48:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 02fac438-03f0-3bc4-bb0f-55a21a05d2e8 | -9.75764 | -65.28809 | 2024-09-26 05:48:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 6bfb1f80-d87d-306b-b391-478357884224 | -9.54543 | -65.48548 | 2024-09-26 05:48:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 6a189915-bb21-3436-978b-ca20608c89ae | -9.53339 | -65.68194 | 2024-09-26 05:48:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 4f360d6a-a7af-3c75-9cca-1952b13636a6 | -9.52998 | -65.68141 | 2024-09-26 05:48:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 1283fce1-7913-387f-96a0-2b0d0a85cd43 | -9.49877 | -65.40197 | 2024-09-26 05:48:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 71929977-7070-3f6c-b945-16e61cd470e9 | -9.4315 | -65.45348 | 2024-09-26 05:48:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 8.4 |
| ea5f2f2c-466c-3ec8-a9f9-426f4d313eae | -9.42984 | -65.39543 | 2024-09-26 05:48:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 2c902f8c-7690-3f68-a5d7-6fb33b5ee3aa | -9.42927 | -65.39921 | 2024-09-26 05:48:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 973b1d0c-6dbe-337d-8119-5082849810f5 | -9.4275 | -65.4567 | 2024-09-26 05:48:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 12.8 |
| 4bbd5918-d9e9-337e-b24d-f49649a5c9fd | -9.42693 | -65.46043 | 2024-09-26 05:48:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 252a8914-616f-332e-9bb3-970d69733ea5 | -9.42465 | -65.45242 | 2024-09-26 05:48:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 12.8 |
| 169de3c9-744a-3ac2-99fb-45241197442d | -9.4235 | -65.4599 | 2024-09-26 05:48:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 19a65c1f-670c-3173-ba02-f8eeef719960 | -9.42238 | -65.42131 | 2024-09-26 05:48:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 6c4b5052-06e3-3d76-9de8-2a830f3c09c2 | -9.42008 | -65.45937 | 2024-09-26 05:48:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 37c5390a-39ea-31bd-a31c-8fb1b2574a9f | -9.41951 | -65.46311 | 2024-09-26 05:48:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 706f7d8f-d558-3e38-9c0d-6b82326ef705 | -9.41432 | -65.56555 | 2024-09-26 05:48:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 952de4fd-7e49-3dbf-9f7a-4ddb40090846 | -9.3666 | -65.6266 | 2024-09-26 05:48:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 7a77b9d6-2a96-329d-9619-a7fa919ca156 | -9.35979 | -65.62554 | 2024-09-26 05:48:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.3 |
| 4296261e-c0df-3483-8496-834840887c84 | -9.35638 | -65.62502 | 2024-09-26 05:48:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.3 |
| bac8869e-2fee-393d-a242-7819da74a731 | -9.35562 | -65.49162 | 2024-09-26 05:48:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 9e4f1506-80a3-3387-872a-3f78a4e12dac | -9.34414 | -65.79649 | 2024-09-26 05:48:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| c240830b-1ea2-3d2d-881c-b7d08e566610 | -9.34406 | -65.72882 | 2024-09-26 05:48:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 851b25bb-4be6-3e7e-8def-406c8cc07041 | -9.33615 | -65.73513 | 2024-09-26 05:48:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 31604949-1f0e-32a3-9f56-91e89343ea45 | -9.33559 | -65.73879 | 2024-09-26 05:48:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 4b2dedad-8316-3b61-98ee-b4e7defd9c55 | -9.36319 | -65.62607 | 2024-09-26 05:48:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 005f811c-15f9-38ab-aada-4212c6b1018e | -9.34753 | -65.79701 | 2024-09-26 05:48:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 84e5470a-d6f1-386f-96d5-2695b3751205 | -9.76339 | -65.29678 | 2024-09-26 05:48:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 77903ab2-a119-3169-909f-a942a7259a51 | -9.76109 | -65.28862 | 2024-09-26 05:48:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.9 |
| e6887485-f465-3cbc-94ad-2a5b9856e8db | -9.72023 | -65.69469 | 2024-09-26 05:48:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 8dcf06df-119a-3bfb-8338-59137fab7970 | -9.71965 | -65.69841 | 2024-09-26 05:48:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 69963f96-6553-3d16-b498-af22d39ab47a | -9.71908 | -65.70213 | 2024-09-26 05:48:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 7a2abdea-05b4-3a62-9012-6d06959bc2b5 | -9.43328 | -65.39597 | 2024-09-26 05:48:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 630d4650-2ae6-350e-be70-21cd1ad2e7f2 | -9.43207 | -65.44972 | 2024-09-26 05:48:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 173e2680-015c-3c25-a224-c6da366886b6 | -9.43093 | -65.45722 | 2024-09-26 05:48:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 8.4 |
| 96f66b11-bbc8-3c81-935b-51538a484d67 | -9.42865 | -65.4492 | 2024-09-26 05:48:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 87d42ebc-a09b-353e-8261-0a7e71cdbeec | -9.42807 | -65.45295 | 2024-09-26 05:48:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 12.8 |
| 1681cb70-5632-3628-b834-937de06ff52e | -9.42524 | -65.4256 | 2024-09-26 05:48:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 22a3d5dd-2965-3628-8ffb-d236292bda34 | -9.42408 | -65.45615 | 2024-09-26 05:48:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 12.8 |


[Clique aqui para ver as próximas entradas](README166.md)
