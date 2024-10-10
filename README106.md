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

## Dados Diários - Página 106

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 95e22340-8ea4-3355-a4b8-63a80cd16a21 | -9.75074 | -50.6448 | 2024-10-10 04:44:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| cfb8707f-28fe-3e14-8ebe-4cc274b90c4c | -9.75019 | -50.64837 | 2024-10-10 04:44:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| f22de915-ed4d-36fb-b767-d585b726557f | -9.74016 | -50.6468 | 2024-10-10 04:44:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| dc89e6cc-0ad1-3517-92f1-7ff5ae5e6486 | -9.49574 | -50.97883 | 2024-10-10 04:44:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 1c00d914-be83-39a6-91de-63614edd4def | -9.4952 | -50.98236 | 2024-10-10 04:44:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 90092856-c154-3343-bca6-04441e0cdbb7 | -9.49188 | -50.98183 | 2024-10-10 04:44:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| e7110d67-4977-3a00-a8d4-eaa8d97e36a1 | -9.49133 | -50.98536 | 2024-10-10 04:44:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 11469125-df12-36e3-aac8-eaf3e2b1104c | -9.48801 | -50.98483 | 2024-10-10 04:44:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 0c00f62c-429a-3b5a-8ff1-c428e843ae37 | -10.85421 | -51.06443 | 2024-10-10 04:44:00 | NOAA-20 | PORTO ALEGRE DO NORTE | MATO GROSSO | Brasil | 5106778 | 51 | 33 | nan | nan | nan | Cerrado | 4.0 |
| f1aaf10d-21d2-3947-9e28-e7e0d41a9a20 | -10.81328 | -51.15252 | 2024-10-10 04:44:00 | NOAA-20 | PORTO ALEGRE DO NORTE | MATO GROSSO | Brasil | 5106778 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 0b1a2060-d6d5-33af-9a86-330ef8182681 | -10.81105 | -51.14491 | 2024-10-10 04:44:00 | NOAA-20 | PORTO ALEGRE DO NORTE | MATO GROSSO | Brasil | 5106778 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 27ffeccc-4781-3b3b-b165-59bc1d1c16ba | -10.8105 | -51.14845 | 2024-10-10 04:44:00 | NOAA-20 | PORTO ALEGRE DO NORTE | MATO GROSSO | Brasil | 5106778 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 6f00f75b-ba31-3526-9ef2-69032c2e9cc2 | -10.80772 | -51.14438 | 2024-10-10 04:44:00 | NOAA-20 | PORTO ALEGRE DO NORTE | MATO GROSSO | Brasil | 5106778 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| af0ebae3-0118-34b0-b783-ded0c1c103c9 | -10.80385 | -51.1474 | 2024-10-10 04:44:00 | NOAA-20 | PORTO ALEGRE DO NORTE | MATO GROSSO | Brasil | 5106778 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| f55d17e9-5d0c-32df-9902-4e5c748adffc | -10.68999 | -51.11571 | 2024-10-10 04:44:00 | NOAA-20 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 2.6 |
| a8b45239-ffcc-3f2a-8c9a-1132eaa8e364 | -10.68725 | -51.13342 | 2024-10-10 04:44:00 | NOAA-20 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 224af732-e459-3ca9-95a2-ebf12a85e238 | -10.68447 | -51.12934 | 2024-10-10 04:44:00 | NOAA-20 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 48c4b430-9028-34fd-9311-03acd95d2ac9 | -10.68446 | -50.90715 | 2024-10-10 04:44:00 | NOAA-20 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 259e66a0-15fb-354e-80d2-d6ad2a740deb | -10.68219 | -51.09995 | 2024-10-10 04:44:00 | NOAA-20 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 2.6 |
| a11785aa-07c6-3c28-b00a-0138e3bfd48a | -10.68164 | -51.10349 | 2024-10-10 04:44:00 | NOAA-20 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 866da86a-bf9c-3455-96ad-882826238ec9 | -10.67941 | -51.09587 | 2024-10-10 04:44:00 | NOAA-20 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 29.0 |
| 2b5c647d-076e-35f0-9bdb-40da222ecd83 | -10.67886 | -51.09942 | 2024-10-10 04:44:00 | NOAA-20 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 29.0 |
| 3a94e74e-da6d-3bef-9476-f615328a1bbf | -10.67608 | -51.09534 | 2024-10-10 04:44:00 | NOAA-20 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 29.0 |
| b9b5d60c-b01d-3455-bbb4-f8ca55a56831 | -10.67396 | -50.93111 | 2024-10-10 04:44:00 | NOAA-20 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 0b77e57d-2543-3dea-a148-7bfee91cbeba | -10.67275 | -51.09482 | 2024-10-10 04:44:00 | NOAA-20 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 8.0 |
| ae8debb0-7b52-326f-adea-a9788c8f1aee | -10.6722 | -51.09837 | 2024-10-10 04:44:00 | NOAA-20 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 8.0 |
| d95632d0-0cf5-3c4a-8cac-40aed9ba417b | -10.67007 | -50.93415 | 2024-10-10 04:44:00 | NOAA-20 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| cf24cbc2-1b76-335f-b572-504883d25f33 | -10.66942 | -51.0943 | 2024-10-10 04:44:00 | NOAA-20 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 8.0 |
| 4983e8d4-69e9-3c06-821a-d49bd6b7c5f3 | -10.66887 | -51.09785 | 2024-10-10 04:44:00 | NOAA-20 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 8.0 |
| 3a585a63-8a9f-36ae-9e2f-0fe9dd708ab9 | -10.66554 | -51.09732 | 2024-10-10 04:44:00 | NOAA-20 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 2c06bdd5-6a23-3340-9b87-e742eb14c113 | -10.41717 | -50.72609 | 2024-10-10 04:44:00 | NOAA-20 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 7f43631f-fb58-35a7-93e4-d88c9b9c6c73 | -10.41657 | -50.70762 | 2024-10-10 04:44:00 | NOAA-20 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 2.8 |
| be057d5d-3d14-39cb-9529-495b773ed556 | -10.41602 | -50.71121 | 2024-10-10 04:44:00 | NOAA-20 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 2.8 |
| fa34de00-5527-33d0-97fa-c3c63af96549 | -10.41547 | -50.7148 | 2024-10-10 04:44:00 | NOAA-20 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 2.8 |
| e41e6130-07ae-3f72-8fbf-0b7da7c33e0a | -10.41492 | -50.71838 | 2024-10-10 04:44:00 | NOAA-20 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 5d47c899-f892-3c70-84eb-435fb4417654 | -10.41437 | -50.72197 | 2024-10-10 04:44:00 | NOAA-20 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 715b53ef-4b4e-3734-abfc-fe9a228151b8 | -9.99402 | -51.59546 | 2024-10-10 04:44:00 | NOAA-20 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 5102500b-b88c-3a0f-a527-2b67e74f314d | -9.65365 | -51.79407 | 2024-10-10 04:44:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 555fc101-7cd4-3cbd-98c1-479aa373de40 | -9.6531 | -51.79755 | 2024-10-10 04:44:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a905a76f-7a72-33c5-8548-4267a2b80ec7 | -10.44831 | -51.88249 | 2024-10-10 04:44:00 | NOAA-20 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| b71dad44-b948-3ae3-b383-3d1a2fee8091 | -10.44501 | -51.88196 | 2024-10-10 04:44:00 | NOAA-20 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| a8715d33-0786-3a3a-8dbc-63f01a8b64d8 | -11.3009 | -51.04655 | 2024-10-10 04:44:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 9c78f190-cb9a-30d7-a71f-3cc4daf6638c | -11.30035 | -51.05014 | 2024-10-10 04:44:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 5.1 |
| bbd1412e-f071-3aa2-ad72-22136736c091 | -11.2983 | -51.04658 | 2024-10-10 04:44:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 5.3 |
| af9256ee-66d0-3ddc-bc6a-73b02866aa03 | -11.29774 | -51.05016 | 2024-10-10 04:44:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 9632a18c-052c-320d-b0a5-7f6fa5c5dc08 | -11.29719 | -51.05375 | 2024-10-10 04:44:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 5e3ef660-f97e-3914-b487-d8feccb11c9a | -11.29498 | -51.06805 | 2024-10-10 04:44:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 2964c87c-ec1d-367c-8b81-a63b41c9a8ca | -11.2944 | -51.04964 | 2024-10-10 04:44:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 5.3 |
| adc8910c-0bdc-325a-ad0e-aa311e29750f | -11.29385 | -51.05322 | 2024-10-10 04:44:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 7ffe37c9-a7f7-3d45-a2db-a9c8b2e9a870 | -11.29277 | -51.08233 | 2024-10-10 04:44:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 4ae8550c-2ead-3098-a481-439f53551d75 | -11.29164 | -51.06752 | 2024-10-10 04:44:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 08ec6638-404e-395d-8853-0987bebbc7f2 | -11.28996 | -51.05627 | 2024-10-10 04:44:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| d2f72162-613e-3621-844a-7da7c5afb7a2 | -11.28717 | -51.05216 | 2024-10-10 04:44:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 88036d5b-0170-35f4-9d4d-9d57f4e24eca | -11.26716 | -51.28935 | 2024-10-10 04:44:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| d87d73a1-3a54-372a-a1c2-5fcc51f1e2f9 | -11.25857 | -51.28111 | 2024-10-10 04:44:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 9638415d-03ec-3da8-ac43-2ee688c1a6df | -11.25634 | -51.27348 | 2024-10-10 04:44:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 159368b5-145d-315f-80ae-0e74e04ab885 | -11.25579 | -51.27703 | 2024-10-10 04:44:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| e7d88f0a-d710-3c0e-a15e-ac7833ce5bdc | -11.24077 | -51.24194 | 2024-10-10 04:44:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| e3383d86-f0ce-3502-9e95-e26afec448cd | -11.23744 | -51.24141 | 2024-10-10 04:44:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| ba74fd89-1a1d-36bd-9c05-9f2b756b7611 | -11.23724 | -51.13208 | 2024-10-10 04:44:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| b1c6f50b-eb28-3b4c-b5ac-de844c41a738 | -11.23403 | -51.1972 | 2024-10-10 04:44:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 9e392246-2ea9-34c1-ab25-071c11e4789c | -11.00054 | -51.25834 | 2024-10-10 04:44:00 | NOAA-20 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 2d56a554-b9c3-3b0d-b1e8-9d7c7f6c4a8e | -10.99721 | -51.25781 | 2024-10-10 04:44:00 | NOAA-20 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 88e32eb6-e746-3c97-9dcb-1e272169dc42 | -11.50929 | -51.80858 | 2024-10-10 04:44:00 | NOAA-20 | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 2c91fe23-0589-3062-8723-3fda64adefb6 | -11.48394 | -51.86215 | 2024-10-10 04:44:00 | NOAA-20 | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| d2e919d7-0d97-3f67-ac85-c2dfb9ffbb0b | -11.48339 | -51.86566 | 2024-10-10 04:44:00 | NOAA-20 | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 3bdae313-401f-390d-a0c6-35113373bc14 | -11.48118 | -51.8581 | 2024-10-10 04:44:00 | NOAA-20 | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| b7dac2bb-4a79-3367-a3c0-39063bed2257 | -11.48063 | -51.86161 | 2024-10-10 04:44:00 | NOAA-20 | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 169e8ff2-8867-3baa-8f46-fc39ef3c0b54 | -11.48009 | -51.86513 | 2024-10-10 04:44:00 | NOAA-20 | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 722ad724-0790-3eb3-9a69-b8058174d5f9 | -11.47788 | -51.85757 | 2024-10-10 04:44:00 | NOAA-20 | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| c9d36dbb-2839-32da-b24d-626e4ff6b21d | -11.47733 | -51.86108 | 2024-10-10 04:44:00 | NOAA-20 | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| fb07decc-fcac-330c-9292-19d68065f73e | -11.32558 | -51.41829 | 2024-10-10 04:44:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 051c813b-3d7c-37f1-b562-e5048a235e4b | -11.32448 | -51.42536 | 2024-10-10 04:44:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| ce7b60a2-c532-3a61-a2ed-b1c94962c46e | -11.32171 | -51.4213 | 2024-10-10 04:44:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| a79ea0fc-90a4-3be1-816e-98382113765a | -11.32116 | -51.42484 | 2024-10-10 04:44:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 8d1c98ba-406a-3373-86fd-afe308daeee8 | -11.30276 | -51.34581 | 2024-10-10 04:44:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 1450004a-2743-3961-a892-08060622f1f7 | -11.27303 | -51.42805 | 2024-10-10 04:44:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| a6e427fb-74c6-336f-ba2d-df727c69a7d4 | -11.24535 | -51.34433 | 2024-10-10 04:44:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 69119cb1-47bd-3984-a9f2-eeea4d4abd6d | -11.24148 | -51.34734 | 2024-10-10 04:44:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 5287657a-7f74-39f4-bc84-1357dd88b667 | -11.23824 | -51.41201 | 2024-10-10 04:44:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 8f54b366-22ef-3fca-9dec-2ad3a9ca5cc2 | -11.21712 | -51.35073 | 2024-10-10 04:44:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| bc092131-e3db-3ce6-8358-37d796192969 | -11.21434 | -51.34667 | 2024-10-10 04:44:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 9deb6998-1bc4-308b-8ad6-669f7aaa3e2a | -11.21102 | -51.34614 | 2024-10-10 04:44:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 680b54c7-9518-38ff-8d30-a0304b84bc01 | -11.2077 | -51.34561 | 2024-10-10 04:44:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| cba8d80b-9ace-3dee-8989-a0a091cf6029 | -11.20715 | -51.34915 | 2024-10-10 04:44:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| d1709290-39c8-3312-aada-e20f988c261f | -11.2066 | -51.35269 | 2024-10-10 04:44:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 5add420a-a575-30ab-9b75-993d8fd3349a | -11.20605 | -51.35622 | 2024-10-10 04:44:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 1a0e4341-2d3f-3241-8d54-a7a12573eb47 | -11.20382 | -51.34863 | 2024-10-10 04:44:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 052cfc5a-0e59-3a01-a2bb-6fb926845518 | -11.1939 | -51.36878 | 2024-10-10 04:44:00 | NOAA-20 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 0bd1294c-19b2-31ea-9c0b-3d197758a22c | -4.61803 | -50.95929 | 2024-10-10 04:44:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 485e24a3-58e2-36c3-b716-e042e94167de | -4.16247 | -51.04701 | 2024-10-10 04:44:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 6.7 |
| bf476114-39dd-38c6-8439-611cacd6d572 | -4.16193 | -51.05046 | 2024-10-10 04:44:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 9.7 |
| 658fda59-0a03-33bb-b109-97f869360237 | -4.15916 | -51.04647 | 2024-10-10 04:44:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 068222c1-3f77-35ef-9f9f-d4782c1e1ec3 | -4.15862 | -51.04992 | 2024-10-10 04:44:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 43a01309-c800-3a13-814d-6ea77e8b053b | -4.15807 | -51.05338 | 2024-10-10 04:44:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 9410f644-b2fd-3c33-a974-e8fd28fb8f80 | -4.15752 | -51.05685 | 2024-10-10 04:44:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 6a710c71-87d9-3845-9f66-1a23799cef7e | -4.15309 | -51.04196 | 2024-10-10 04:44:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 888a5e52-697f-3a45-87a0-1df2e0379129 | -4.14977 | -51.04144 | 2024-10-10 04:44:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 0b128e27-bdff-321f-bd39-530971c5cc27 | -4.14923 | -51.04489 | 2024-10-10 04:44:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| cade1061-10ea-34d0-b810-ade363086b9c | -4.14378 | -51.1008 | 2024-10-10 04:44:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |


[Clique aqui para ver as próximas entradas](README107.md)
