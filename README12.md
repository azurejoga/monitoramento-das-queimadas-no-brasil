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

## Dados Diários - Página 12

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 071b71eb-db66-3880-b8ce-29bc557f4814 | -8.01422 | -50.10258 | 2025-07-13 04:49:00 | NPP-375D | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 183e57ef-5656-373a-97cd-42a794eca099 | -8.5092 | -43.28892 | 2025-07-13 04:49:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 6.9 |
| b914081f-fd87-329f-a2ca-23bb28c0a5ee | -13.10952 | -47.30658 | 2025-07-13 04:49:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 306065fb-8c07-311b-b822-dd86cbde4b59 | -10.66963 | -56.54633 | 2025-07-13 04:49:00 | NPP-375D | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 368294bf-fe07-34ba-b77c-872ee8eb6747 | -8.50305 | -43.2886 | 2025-07-13 04:49:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 19d55d2e-8190-372e-a095-8b7871f01e06 | -8.50417 | -43.28822 | 2025-07-13 04:49:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 6.9 |
| 9bfb6a0d-7494-34d9-beca-df59f3f8949b | -8.91247 | -47.35196 | 2025-07-13 04:49:00 | NPP-375D | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 86e32f4d-ea25-312a-a241-449b373272d9 | -8.34928 | -45.63374 | 2025-07-13 04:49:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 9fd87426-a8c3-38a3-80c3-7e5f464a53c9 | -12.44759 | -50.4609 | 2025-07-13 04:49:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 6ff6f4c6-5042-3dbe-b782-da99884cdb84 | -10.56947 | -49.12785 | 2025-07-13 04:49:00 | NPP-375D | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| c5146339-c179-3a66-9492-b9b6b7ba401d | -8.50808 | -43.28931 | 2025-07-13 04:49:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 5.6 |
| 13fc6671-6287-325e-b92a-812ed029733b | -13.84853 | -46.89779 | 2025-07-13 04:49:00 | NPP-375D | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 34.2 |
| 6f0f8fed-36e7-3eb3-af03-2347c56d72f0 | -10.04786 | -59.11265 | 2025-07-13 04:49:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 9b08a3d7-d21e-360b-9ceb-90521eed8ccb | -13.02781 | -47.8261 | 2025-07-13 04:49:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| d17b5a66-5914-3473-adee-227a04bee352 | -13.11956 | -47.28473 | 2025-07-13 04:49:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 2609b9ce-6ae0-3acd-93e1-ce64c0bf5c93 | -10.57364 | -49.12436 | 2025-07-13 04:49:00 | NPP-375D | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 75e81111-cc19-3e44-b6ea-5bf7e8592dec | -11.8292 | -47.50609 | 2025-07-13 04:49:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 378b5a25-794d-3261-8e90-36a452c37491 | -8.12616 | -43.55118 | 2025-07-13 04:49:00 | NPP-375D | ELISEU MARTINS | PIAUÍ | Brasil | 2203602 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 628bd771-be14-3ba0-bb55-c3cdf13172aa | -10.50068 | -53.58864 | 2025-07-13 04:49:00 | NPP-375D | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 5233cf34-69d3-3899-9aa3-3ca40146db1b | -13.88543 | -44.46213 | 2025-07-13 04:49:00 | NPP-375D | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 129dd34e-f0b2-3f3f-b37e-26da1d764a35 | -12.42801 | -50.45878 | 2025-07-13 04:49:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 683e088e-9bf7-3f55-8b1d-10ef2805730e | -8.63944 | -47.68219 | 2025-07-13 04:49:00 | NPP-375D | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| dcbca9e3-4468-333b-a2ee-4ba799bd8011 | -11.73777 | -48.52678 | 2025-07-13 04:49:00 | NPP-375D | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| b0053536-7fc4-3c30-b908-c5af5080a213 | -8.35127 | -45.65018 | 2025-07-13 04:49:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 655a954f-7d7d-3a17-9e4a-f9a5f44db887 | -12.14649 | -50.23713 | 2025-07-13 04:49:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 489649b2-5b20-37c4-8424-0bd57ca17cdc | -12.01812 | -49.52224 | 2025-07-13 04:49:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 602fff80-75d2-3bfd-b347-b908753fe767 | -8.35181 | -45.64646 | 2025-07-13 04:49:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 3eefcad7-15ba-3fab-af4b-0ef387492114 | -8.50382 | -43.28276 | 2025-07-13 04:49:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| a2ee74d7-0e63-35ac-9f08-8f76c2fdcd86 | -9.79793 | -48.56382 | 2025-07-13 04:49:00 | NPP-375D | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 6c1bb74c-b301-3425-91ff-8db449cf566e | -9.53127 | -46.29756 | 2025-07-13 04:49:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 9c5e1e99-c5b3-3f7f-a4b3-ca5e121bf97a | -10.57425 | -49.12031 | 2025-07-13 04:49:00 | NPP-375D | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 12.1 |
| bd164ab6-0be7-39dc-84be-438be752059c | -10.0441 | -59.10683 | 2025-07-13 04:49:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 64060cec-615a-302f-8448-9f911d9eb04f | -10.95759 | -54.37674 | 2025-07-13 04:49:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| f2f872bf-0779-36a7-a3c5-5a472443cac7 | -10.0432 | -59.11179 | 2025-07-13 04:49:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 894baa96-d15e-3866-891a-ff57c09f9a40 | -9.02106 | -61.22332 | 2025-07-13 04:49:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 7df8335f-7cf6-3034-ad95-25dfff7d5c62 | -11.83317 | -47.50664 | 2025-07-13 04:49:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 43ca4f91-9685-3936-8294-33b1e9bb8a79 | -13.27908 | -43.60754 | 2025-07-13 04:49:00 | NPP-375D | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| e4428769-a731-3854-b8bb-619b41d5aee5 | -10.57598 | -49.13303 | 2025-07-13 04:49:00 | NPP-375D | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 7b516d65-be9c-3f76-8019-2e38ed6ff560 | -13.19332 | -47.2644 | 2025-07-13 04:49:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 40165bad-5010-33f1-8a87-1d52941a02d4 | -8.91465 | -47.3495 | 2025-07-13 04:49:00 | NPP-375D | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 28c2404f-04d1-3bcf-b677-29e01e5bcab5 | -13.84126 | -45.88963 | 2025-07-13 04:49:00 | NPP-375D | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 37862542-3106-3c9e-b0ba-898aeef98b34 | -9.24768 | -64.41172 | 2025-07-13 04:49:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 03d42d89-d6a8-37d9-bd15-a62cf99ea038 | -8.34705 | -45.64934 | 2025-07-13 04:49:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 377631e8-dbb6-3873-a078-78300ea72930 | -9.24879 | -64.40593 | 2025-07-13 04:49:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 59321ab6-33f4-34a1-81de-102128a179f1 | -10.56774 | -49.11513 | 2025-07-13 04:49:00 | NPP-375D | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 01ff06ae-65e4-3186-80bc-ceb608de697d | -13.1443 | -47.3175 | 2025-07-13 04:49:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| cebce927-1318-323e-b44d-8a13fc15de4b | -13.19798 | -47.261 | 2025-07-13 04:49:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 22bfbd48-1e6e-3476-80e0-da2981cef2b5 | -11.86211 | -58.70699 | 2025-07-13 04:49:00 | NPP-375D | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| b6287926-e226-3728-ae9d-3c90d49afc5a | -13.19439 | -47.2567 | 2025-07-13 04:49:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 64c933d2-b9d4-3574-b81a-377c5c45de83 | -10.64649 | -44.48564 | 2025-07-13 04:49:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 3444c940-d573-3a96-a78e-51c4ba2e6c90 | -10.5069 | -46.47397 | 2025-07-13 04:49:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 3e55fe43-8227-3bfa-b89a-f2bd2fec23c4 | -11.7319 | -47.46413 | 2025-07-13 04:49:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 3fdfe3ca-277b-34fc-a914-1e75c1623e06 | -8.17923 | -46.5002 | 2025-07-13 04:49:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 42da6d44-cebb-36b9-b530-b0bbc7fbb660 | -10.7967 | -49.62804 | 2025-07-13 04:49:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| efb679b1-4c31-33e2-ac86-c3a251929c5f | -13.84066 | -45.89437 | 2025-07-13 04:49:00 | NPP-375D | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 3.3 |
| b3819622-e69f-3c4b-84b2-5b361e6d2d12 | -11.86651 | -58.70778 | 2025-07-13 04:49:00 | NPP-375D | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 1e664b3d-822a-3129-a02d-492a091820d7 | -8.6395 | -47.68458 | 2025-07-13 04:49:00 | NPP-375D | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| f1ca8ddf-a89c-3fdf-bae2-fdc41995dc78 | -9.11815 | -48.53082 | 2025-07-13 04:49:00 | NPP-375D | FORTALEZA DO TABOCÃO | TOCANTINS | Brasil | 1708254 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| c1de3d7b-dd13-3286-903a-96609d3092e9 | -13.28434 | -43.60822 | 2025-07-13 04:49:00 | NPP-375D | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 4e005101-d9ba-32a7-ada3-23cdf4bf9e87 | -10.57131 | -49.11567 | 2025-07-13 04:49:00 | NPP-375D | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 12.1 |
| b0837c99-f2f6-33ae-8d57-8267411a3944 | -9.57837 | -48.56356 | 2025-07-13 04:49:00 | NPP-375D | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| f28df6bf-3b8f-3c6d-bff0-331f1f0279a4 | -10.18158 | -49.50344 | 2025-07-13 04:49:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 8ba16f70-a421-3ae2-9140-0d0d9bee7efb | -13.02457 | -47.82053 | 2025-07-13 04:49:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| b5c57c1c-1eb2-3101-aee3-f89a90671892 | -10.50409 | -53.58921 | 2025-07-13 04:49:00 | NPP-375D | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| d00740f7-68c1-3cd3-b507-37e6c759b02a | -8.35898 | -51.07895 | 2025-07-13 04:49:00 | NPP-375D | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| ffcc1666-eac6-38aa-87d8-76d6f4bb1b8c | -6.62792 | -56.28786 | 2025-07-13 04:49:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| af704a72-5615-3453-b3eb-1a2e75760e13 | -11.73262 | -47.45893 | 2025-07-13 04:49:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 77910040-c238-3557-96c4-3d2ffced6e0b | -13.11153 | -47.29228 | 2025-07-13 04:49:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 6a1d6c35-9d41-305d-82f0-80a97cb90301 | -10.64635 | -47.47798 | 2025-07-13 04:49:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| b94f0266-2978-35e9-a0ef-4041d41abff2 | -12.99499 | -46.26641 | 2025-07-13 04:49:00 | NPP-375D | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 8ba71f60-10c1-334f-b208-dc89a0ccfddd | -12.01751 | -49.52633 | 2025-07-13 04:49:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 0b1e6fbf-26eb-3c06-90ef-c9ab71b44e73 | -13.8474 | -46.8964 | 2025-07-13 04:50:00 | GOES-19 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 68.4 |
| 93d0d09d-5e16-3a6c-895f-c7c24ed2a985 | -12.09888 | -63.70948 | 2025-07-13 04:51:00 | NPP-375D | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 2.5 |
| e9292788-daa3-38eb-915d-4a8cd9d5adbc | -19.08893 | -56.04276 | 2025-07-13 04:51:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.9 |
| 1a0e676c-c196-3471-bb9c-68e751786f83 | -12.57838 | -56.9716 | 2025-07-13 04:51:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 34c3decc-e7da-39c8-ad5b-f7e96f1c5cda | -15.60051 | -46.87483 | 2025-07-13 04:51:00 | NPP-375D | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 814386af-bc06-3cd3-b9c0-490be4212992 | -15.0502 | -55.82537 | 2025-07-13 04:51:00 | NPP-375D | CHAPADA DOS GUIMARÃES | MATO GROSSO | Brasil | 5103007 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 32a996dd-1f75-3909-92fc-1d2350863bcd | -13.47254 | -60.91795 | 2025-07-13 04:51:00 | NPP-375D | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 2.5 |
| e19fd922-50ac-31d0-90be-6e1ffcac88af | -15.21495 | -46.81849 | 2025-07-13 04:51:00 | NPP-375D | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 4d0f1b1e-b686-3c86-b044-621e2107e2e9 | -12.09981 | -63.70485 | 2025-07-13 04:51:00 | NPP-375D | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 2649f85d-e1a4-380c-8c15-947b83c7d82d | -19.86612 | -54.39803 | 2025-07-13 04:51:00 | NPP-375D | BANDEIRANTES | MATO GROSSO DO SUL | Brasil | 5001508 | 50 | 33 | nan | nan | nan | Cerrado | 0.7 |
| eca480bd-18a9-3e21-81be-89852e8a2670 | -20.75043 | -49.33212 | 2025-07-13 04:51:00 | NPP-375D | SÃO JOSÉ DO RIO PRETO | SÃO PAULO | Brasil | 3549805 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| 08a0f52a-bf78-3922-82a3-da2643cc28e1 | -17.68786 | -54.01137 | 2025-07-13 04:51:00 | NPP-375D | PEDRO GOMES | MATO GROSSO DO SUL | Brasil | 5006408 | 50 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 020aa659-e9a1-3d22-9662-82979a5841d1 | -20.47733 | -53.67471 | 2025-07-13 04:51:00 | NPP-375D | RIBAS DO RIO PARDO | MATO GROSSO DO SUL | Brasil | 5007109 | 50 | 33 | nan | nan | nan | Cerrado | 0.8 |
| d5c83b6c-8fe9-301f-abf2-33bd0ec5d9ed | -13.9158 | -47.41748 | 2025-07-13 04:51:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| c816a34a-1280-3a2b-b972-a7864acc7f52 | -19.08483 | -56.04604 | 2025-07-13 04:51:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.9 |
| 73ed1e21-8225-3077-98eb-62e211c82d5b | -19.09237 | -56.0434 | 2025-07-13 04:51:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 0.9 |
| a3eadfa4-d5a0-3cac-a63c-245dba11e520 | -13.47246 | -60.9186 | 2025-07-13 04:51:00 | NPP-375D | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 40f47839-dad0-38cc-8933-ef945cd48501 | -14.85794 | -47.99178 | 2025-07-13 04:51:00 | NPP-375D | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 0.5 |
| f27701ac-d4fe-3b05-a6e3-624ad75da29d | -17.90853 | -54.13545 | 2025-07-13 04:51:00 | NPP-375D | PEDRO GOMES | MATO GROSSO DO SUL | Brasil | 5006408 | 50 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 9b7b2b62-2f68-370c-9327-75dc65c4bc57 | -17.65423 | -50.48085 | 2025-07-13 04:51:00 | NPP-375D | SANTA HELENA DE GOIÁS | GOIÁS | Brasil | 5219308 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| c5031b51-185d-38dc-9518-0effc3768964 | -12.35068 | -57.42618 | 2025-07-13 04:51:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 2b04247d-7d89-3aa8-bf22-45b18ad872b6 | -13.91171 | -47.4168 | 2025-07-13 04:51:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| e2a498fb-1e6a-3b57-9ea7-fb8a0ca6f04d | -12.02515 | -63.79157 | 2025-07-13 04:51:00 | NPP-375D | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 28f8991c-979c-35cd-abe0-bf688b5e36f9 | -16.06979 | -43.65106 | 2025-07-13 04:51:00 | NPP-375D | CAPITÃO ENÉAS | MINAS GERAIS | Brasil | 3112703 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 4a36a260-ddca-32c1-bfae-eab7875cd744 | -12.02104 | -63.7845 | 2025-07-13 04:51:00 | NPP-375D | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| aca5035d-8c30-3049-9643-8c3dce2c9da0 | -17.31374 | -44.92838 | 2025-07-13 04:51:00 | NPP-375D | PIRAPORA | MINAS GERAIS | Brasil | 3151206 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 5589368d-060d-3b4b-8ce7-89fca4fcac56 | -14.31879 | -52.74395 | 2025-07-13 04:51:00 | NPP-375D | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 4d639aa5-73a8-34c2-83ed-7000fb26b351 | -16.06938 | -43.65468 | 2025-07-13 04:51:00 | NPP-375D | CAPITÃO ENÉAS | MINAS GERAIS | Brasil | 3112703 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| ac876568-0ff3-37e7-abe3-1963c3fe5260 | -17.91186 | -54.13603 | 2025-07-13 04:51:00 | NPP-375D | PEDRO GOMES | MATO GROSSO DO SUL | Brasil | 5006408 | 50 | 33 | nan | nan | nan | Cerrado | 0.7 |


[Clique aqui para ver as próximas entradas](README13.md)
