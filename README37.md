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

## Dados Diários - Página 37

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 8abb7f39-f36c-36e8-a1ef-8ccb3a3ad701 | -3.0226 | -51.052601 | 2024-09-27 01:30:22 | METOP-C | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 1632e05e-62c2-35b0-b114-89f4e528c7c7 | -3.0271 | -51.071098 | 2024-09-27 01:30:22 | METOP-C | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| efe7c80b-97ce-3f19-8c65-fa683cf3cf1f | -3.013 | -51.054901 | 2024-09-27 01:30:22 | METOP-C | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 00c59d2d-0b21-34f7-b477-237924447a41 | -3.0174 | -51.073399 | 2024-09-27 01:30:22 | METOP-C | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| df47749f-3b07-39f0-97c0-b4b3de1661a5 | -4.2833 | -56.404701 | 2024-09-27 01:30:22 | METOP-C | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| bd12aa59-bfb4-3a9b-a862-1f07895c620a | -3.6411 | -54.027302 | 2024-09-27 01:30:23 | METOP-C | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 2289e1b4-1886-3b43-a85c-36ec00a61879 | -3.6438 | -54.0387 | 2024-09-27 01:30:23 | METOP-C | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f2e19866-5c07-3a10-86ad-98c5f938aa78 | -3.6465 | -54.049999 | 2024-09-27 01:30:23 | METOP-C | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 32b7d394-5588-3897-b072-70df96d7eb5d | -3.634 | -54.040901 | 2024-09-27 01:30:24 | METOP-C | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 67e47144-0f32-3418-a1f9-bde15564e8cf | -2.883 | -51.665298 | 2024-09-27 01:30:27 | METOP-C | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 2f4c2d78-ba6f-3698-a3a0-14545aac5e4d | -2.887 | -51.682098 | 2024-09-27 01:30:27 | METOP-C | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 66d1a39b-53b2-3e70-96b1-c7b48523a2ef | -2.8692 | -51.6506 | 2024-09-27 01:30:27 | METOP-C | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 59ece9ea-09ed-3e66-8971-e81fee9b40f7 | -2.8733 | -51.6675 | 2024-09-27 01:30:27 | METOP-C | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a76f84a1-e668-3f6f-8e20-984edc140fb5 | -2.8773 | -51.684399 | 2024-09-27 01:30:27 | METOP-C | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 015e33c9-de83-3d22-b735-0522e883c2d4 | -2.8635 | -51.6698 | 2024-09-27 01:30:27 | METOP-C | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b1d613d6-da41-3454-a392-0938bd7b952e | -3.3548 | -53.7743 | 2024-09-27 01:30:27 | METOP-C | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 10219441-0284-3dd1-9364-6808e67f309e | -3.3027 | -53.684898 | 2024-09-27 01:30:28 | METOP-C | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| bb8a2a55-1fb7-3fd6-9d17-9e067f0b5b69 | -3.3055 | -53.696999 | 2024-09-27 01:30:28 | METOP-C | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ad366909-187b-34c2-a65e-9fde13fccd06 | -2.9264 | -57.841702 | 2024-09-27 01:30:49 | METOP-C | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 79a79086-aed5-3622-ad5d-e1cdabc4d5df | -2.9281 | -57.848999 | 2024-09-27 01:30:49 | METOP-C | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| e9ca68fa-c81a-3866-a220-c8a735a6004b | -3.1199 | -59.1273 | 2024-09-27 01:30:51 | METOP-C | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 00bb64b7-04c3-3a85-b3f2-2245439acc40 | -3.1215 | -59.134201 | 2024-09-27 01:30:51 | METOP-C | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 3fc0c129-bfc5-314d-bbc9-41232ab755a7 | -3.1231 | -59.141102 | 2024-09-27 01:30:51 | METOP-C | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| e478cd0f-cab8-367e-a24c-a7d83eee36b5 | -2.7243 | -57.503101 | 2024-09-27 01:30:51 | METOP-C | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 7d05aa32-eaf6-3d9c-ae78-954053c01008 | -2.726 | -57.5107 | 2024-09-27 01:30:51 | METOP-C | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 707a31a4-1db4-3de7-a7b2-49f98138143f | -2.7145 | -57.505299 | 2024-09-27 01:30:52 | METOP-C | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 134020f8-3b40-3bd3-877a-c640292b0ab8 | -2.7162 | -57.512901 | 2024-09-27 01:30:52 | METOP-C | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 5bfaea2d-8951-3512-bd8d-535b4a9a2f6f | -2.7082 | -57.522701 | 2024-09-27 01:30:52 | METOP-C | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 0b41203d-d5ae-3404-b626-9e9e40e54790 | -2.6753 | -57.514198 | 2024-09-27 01:30:52 | METOP-C | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 80ea5e57-8700-3a2e-9b6f-8fb794f45a22 | -2.6655 | -57.516399 | 2024-09-27 01:30:52 | METOP-C | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 13f45b7f-033d-3d60-9b73-243d55b99dbf | -2.6672 | -57.523998 | 2024-09-27 01:30:52 | METOP-C | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| c116ab94-0a0b-3ac3-bf86-1fe321412001 | -2.6795 | -57.576801 | 2024-09-27 01:30:52 | METOP-C | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| e9e87ad1-eeee-3c6a-87d7-1908fa457a40 | -2.6812 | -57.584301 | 2024-09-27 01:30:52 | METOP-C | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| bf8d28aa-6a1f-3400-885c-3f77f6bf495e | -2.683 | -57.591801 | 2024-09-27 01:30:52 | METOP-C | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 4bbb1635-1969-372a-9c5a-a6d3b69fdda2 | -2.6847 | -57.5994 | 2024-09-27 01:30:52 | METOP-C | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 4b7ed97b-7149-3507-a68b-83db98aae93a | -2.6732 | -57.594101 | 2024-09-27 01:30:53 | METOP-C | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 357ca142-8e3a-3491-a8e7-464047607c06 | -2.6749 | -57.601601 | 2024-09-27 01:30:53 | METOP-C | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 988fa4bd-06b0-3ac9-9c1d-46c51d6944a3 | -2.6767 | -57.6091 | 2024-09-27 01:30:53 | METOP-C | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 4ab271e2-3e69-3e87-b5dd-d2a6611ec860 | -2.9774 | -60.979401 | 2024-09-27 01:31:00 | METOP-C | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 31639a39-0927-3338-8754-afa952917d00 | -2.86 | -60.917 | 2024-09-27 01:31:02 | METOP-C | IRANDUBA | AMAZONAS | Brasil | 1301852 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 4bbd4a41-0b14-3153-8ba2-3c7d3e3c9fa3 | -1.4651 | -55.497299 | 2024-09-27 01:31:04 | METOP-C | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 3a16e84d-6d4c-3776-840b-dc314d84ccc8 | -1.4674 | -55.507198 | 2024-09-27 01:31:04 | METOP-C | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e557ef71-d152-36c7-ae15-45b594eca85d | -1.4553 | -55.4995 | 2024-09-27 01:31:04 | METOP-C | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 49dc4a1b-f6a2-377c-ac46-5e1e10797054 | -1.4576 | -55.509399 | 2024-09-27 01:31:04 | METOP-C | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 7a36a269-83e9-3f69-8fd3-b26bfb6fdb5a | 0.9044 | -51.998299 | 2024-09-27 01:31:30 | METOP-C | SERRA DO NAVIO | AMAPÁ | Brasil | 1600055 | 16 | 33 | nan | nan | nan | Amazônia | nan |
| 94ed12c2-3028-3d99-a81f-c7843bbc8fa3 | -2.6783 | -57.5893 | 2024-09-27 01:35:22 | GOES-16 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 67.5 |
| c06175e2-69c2-3ec3-bdfc-2a49c988bc88 | -2.8611 | -51.6699 | 2024-09-27 01:35:22 | GOES-16 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 53.6 |
| 91f382b4-f183-359c-a8f0-67afb92a778b | -2.8795 | -51.6695 | 2024-09-27 01:35:23 | GOES-16 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 83.0 |
| 0dca1082-c238-358a-97ef-666ce850c4a4 | -3.0107 | -51.0652 | 2024-09-27 01:35:23 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 64.6 |
| 067260e8-98bf-3970-a023-5ac56e7a5cde | -3.2136 | -46.7843 | 2024-09-27 01:35:24 | GOES-16 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 77.9 |
| 2e3b7081-c6a2-341b-a996-58e78fd42c14 | -4.5614 | -48.0141 | 2024-09-27 01:35:32 | GOES-16 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 52.8 |
| 08055abe-2a01-3890-ad03-699acb05edf0 | -7.0912 | -46.4412 | 2024-09-27 01:35:46 | GOES-16 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 61.7 |
| 89d7178e-0c91-3847-9c0e-5ca71d277467 | -7.2905 | -61.106 | 2024-09-27 01:35:48 | GOES-16 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 48.2 |
| 022ee058-438a-3a64-b903-d0bdd0b719e8 | -7.2906 | -61.0869 | 2024-09-27 01:35:48 | GOES-16 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 60.6 |
| 536408ee-b87c-3b2f-8012-4c5de40b58d3 | -7.3089 | -61.1053 | 2024-09-27 01:35:48 | GOES-16 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 55.5 |
| 54f5950e-eecd-3aa7-b1f4-edc1cfd5c3de | -7.309 | -61.0862 | 2024-09-27 01:35:48 | GOES-16 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 86.9 |
| d27ee973-ad39-3fd2-8e79-dcdc0a67cd0e | -7.5289 | -61.3825 | 2024-09-27 01:35:49 | GOES-16 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 73.4 |
| 02a07509-21be-3c5e-96c6-97594c59916a | -7.529 | -61.3635 | 2024-09-27 01:35:49 | GOES-16 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 50.2 |
| 2719dbe6-f22b-3dbf-8f64-95b7e5cb0d70 | -7.77 | -61.2015 | 2024-09-27 01:35:51 | GOES-16 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 108.6 |
| e80dec5d-091c-3293-961e-5777a87aeb09 | -7.7701 | -61.1825 | 2024-09-27 01:35:51 | GOES-16 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 110.9 |
| d265bdb2-581e-360f-8828-060bebdaf591 | -7.8156 | -54.7252 | 2024-09-27 01:35:51 | GOES-16 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 119.3 |
| 21d88b1b-6773-398f-bc19-99ae97ac75de | -7.7885 | -61.2008 | 2024-09-27 01:35:51 | GOES-16 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 99.4 |
| af4b4e5d-28d6-3477-9b79-1f471ba7794d | -7.7886 | -61.1817 | 2024-09-27 01:35:51 | GOES-16 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 118.3 |
| 2234e23a-1f84-399b-9257-573e8f354e50 | -7.9174 | -61.2909 | 2024-09-27 01:35:52 | GOES-16 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 81.9 |
| 1ac654a5-4f59-3fad-8bc5-6102c046ef17 | -7.9175 | -61.2718 | 2024-09-27 01:35:52 | GOES-16 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 91.4 |
| 7e2afd7a-b713-3804-ab76-1ccfbfee3be6 | -7.9359 | -61.2901 | 2024-09-27 01:35:52 | GOES-16 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 63.2 |
| ddad0221-9028-36b6-b7b6-17c457ce3db5 | -7.936 | -61.271 | 2024-09-27 01:35:52 | GOES-16 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 66.7 |
| b869613d-8943-3c93-8b74-fdae2f506eed | -8.1394 | -61.2817 | 2024-09-27 01:35:53 | GOES-16 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 73.4 |
| 53a554e4-6b76-39df-bc9d-5c52d492eac2 | -8.556 | -49.6112 | 2024-09-27 01:35:55 | GOES-16 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 107.3 |
| f259b47a-99b5-3615-a069-e7c4a474d4cd | -8.7032 | -66.9907 | 2024-09-27 01:35:56 | GOES-16 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 72.0 |
| 7dbf3121-e110-34be-9819-0a3bc681f360 | -8.61 | -63.1415 | 2024-09-27 01:35:56 | GOES-16 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 80.4 |
| 8590f614-ecf4-3bc2-a825-2d11293c8247 | -8.6101 | -63.1226 | 2024-09-27 01:35:56 | GOES-16 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 102.5 |
| 175cc90e-6a57-3b9d-8afe-e0a89fd0676a | -8.6285 | -63.1408 | 2024-09-27 01:35:56 | GOES-16 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 153.0 |
| 5cfa1aa7-a3d8-3ac9-ad46-aadf346db23c | -8.6286 | -63.1219 | 2024-09-27 01:35:56 | GOES-16 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 243.5 |
| f7a51edd-9961-3847-8d93-3c0809f8b1c9 | -8.7033 | -66.9721 | 2024-09-27 01:35:56 | GOES-16 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 69.1 |
| 6fbe8107-bd4e-3fd3-99f5-cf4692255529 | -8.7034 | -66.9536 | 2024-09-27 01:35:56 | GOES-16 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 53.9 |
| 8d59f8f7-6893-32b1-ad31-49b9be91fd12 | -8.7218 | -66.9716 | 2024-09-27 01:35:56 | GOES-16 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 67.7 |
| 33ee48e0-a8f9-3042-90e5-9f090464877b | -8.7219 | -66.9531 | 2024-09-27 01:35:56 | GOES-16 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 71.6 |
| 9afd70de-5eed-35af-9cb2-ae649d911706 | -8.7931 | -67.6921 | 2024-09-27 01:35:57 | GOES-16 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 47.2 |
| bef9456a-c657-3ae6-8f48-ad2500c691a4 | -8.7932 | -67.6736 | 2024-09-27 01:35:57 | GOES-16 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 50.1 |
| d6883a2f-51d2-3642-9d80-723e5980c569 | -8.8116 | -67.6917 | 2024-09-27 01:35:57 | GOES-16 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 155.0 |
| 63c90699-0fca-344e-9d64-22b8b61819da | -8.8117 | -67.6732 | 2024-09-27 01:35:57 | GOES-16 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 176.8 |
| fc223af6-c86b-3e32-8545-925c62289c87 | -8.8302 | -67.6728 | 2024-09-27 01:35:57 | GOES-16 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 49.6 |
| aea6d3bd-8591-313a-b145-4a5c745e1e1e | -8.9977 | -67.3909 | 2024-09-27 01:35:58 | GOES-16 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 65.1 |
| 7821cbcc-dc06-310b-b5f3-2741cfba1148 | -8.9978 | -67.3724 | 2024-09-27 01:35:58 | GOES-16 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 206.3 |
| 002cc72a-691c-39ec-bbc7-cc9e126cfa29 | -8.9978 | -67.3538 | 2024-09-27 01:35:58 | GOES-16 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 126.0 |
| 0e6df207-5783-3e0d-b127-c76e2fbaa4b0 | -9.0163 | -67.3719 | 2024-09-27 01:35:58 | GOES-16 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 97.3 |
| c139b7f3-4c21-389b-85d6-f1ea9bbf4f66 | -9.0163 | -67.3534 | 2024-09-27 01:35:58 | GOES-16 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 71.4 |
| 04474ebc-311e-37ea-acd2-ed327c3f50cc | -9.0656 | -61.3934 | 2024-09-27 01:35:58 | GOES-16 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 54.5 |
| 3ee10751-9388-37d6-acb9-58774be2a377 | -9.0657 | -61.3743 | 2024-09-27 01:35:58 | GOES-16 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 51.1 |
| 80352c52-d59b-38f0-8f81-7577e022d23c | -9.086 | -61.1245 | 2024-09-27 01:35:58 | GOES-16 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 61.6 |
| 1db33685-f4a9-32ce-89b0-4793b0a022bb | -9.103 | -61.3534 | 2024-09-27 01:35:58 | GOES-16 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 46.5 |
| 87589519-8503-3576-a314-f12c80ccf73c | -9.1215 | -61.3717 | 2024-09-27 01:35:59 | GOES-16 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 48.8 |
| cff60e5a-cc7f-3769-9644-b5edeb8677e6 | -9.1216 | -61.3526 | 2024-09-27 01:35:59 | GOES-16 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 54.6 |
| d4b73c93-73ef-3177-86ab-a014084f3e73 | -9.1616 | -68.1643 | 2024-09-27 01:35:59 | GOES-16 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 48.1 |
| adc8d0ad-031b-3192-a59a-dc1b186f7bdb | -9.3381 | -65.7255 | 2024-09-27 01:36:00 | GOES-16 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 47.8 |
| b173bc93-7acc-3b70-9198-64526aa561b8 | -9.5829 | -50.137 | 2024-09-27 01:36:01 | GOES-16 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 76.4 |
| 7f06ac34-93a4-3bb7-aed7-714c42ae5f10 | -9.6018 | -50.1352 | 2024-09-27 01:36:01 | GOES-16 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 109.7 |
| ab52effc-c3c8-3f43-9968-1c873369515e | -10.3672 | -53.7858 | 2024-09-27 01:36:05 | GOES-16 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 144.5 |
| ea1b4b2b-662b-37e8-ba38-f173631646d0 | -10.6449 | -45.8862 | 2024-09-27 01:36:06 | GOES-16 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 58.5 |


[Clique aqui para ver as próximas entradas](README38.md)
