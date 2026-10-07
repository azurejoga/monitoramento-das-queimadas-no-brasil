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

## Dados Diários - Página 73

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| bdbaf37f-f225-3eff-84bc-98007b012a31 | -1.25723 | -49.05308 | 2026-10-07 05:04:00 | NOAA-21 | PONTA DE PEDRAS | PARÁ | Brasil | 1505700 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 5b052c37-d731-3af9-ac0f-855170d1e776 | -3.67992 | -55.95014 | 2026-10-07 05:04:00 | NOAA-21 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| d2e23be9-41e5-3ea6-b3d0-582704082c33 | -2.94081 | -54.16464 | 2026-10-07 05:04:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 19f5af56-5b5c-3d4c-a65a-90db1eb4389b | -3.67896 | -59.62488 | 2026-10-07 05:04:00 | NOAA-21 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 3522c849-2390-324e-9c28-44fb9dbc715c | -3.81138 | -51.54093 | 2026-10-07 05:04:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| eb181463-0f46-378c-995c-6df031efd5d2 | -4.4624 | -54.97084 | 2026-10-07 05:04:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 9d802ec5-52df-38b1-a1ad-919806ea0938 | -2.93901 | -54.11052 | 2026-10-07 05:04:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| b04e001e-58c8-3bee-8735-bb841e095908 | -2.76787 | -54.09447 | 2026-10-07 05:04:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 9.0 |
| a464b6ca-bc9a-3114-b803-be161332d73f | -2.93022 | -54.14507 | 2026-10-07 05:04:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| af58389c-ae51-3056-ac0a-8def448a0453 | -3.44856 | -56.49178 | 2026-10-07 05:04:00 | NOAA-21 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| eca1cc49-ba41-311f-a832-1d1e8ae5b485 | -3.05931 | -54.23291 | 2026-10-07 05:04:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 33ad57fb-27c8-34eb-8f3a-38cb0ac5b446 | -3.06308 | -54.20841 | 2026-10-07 05:04:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 68e5e120-e68d-343a-9bb8-389ac86c1884 | -5.8936 | -53.63769 | 2026-10-07 05:04:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 62665083-680c-3910-8b21-38c7218cf455 | -3.2955 | -54.06793 | 2026-10-07 05:04:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 20076173-4da4-378d-81bf-e3193a7f0980 | -3.00045 | -54.13055 | 2026-10-07 05:04:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| ada43619-f8d0-32eb-a688-7b78b1574302 | -2.26087 | -47.00434 | 2026-10-07 05:04:00 | NOAA-21 | GARRAFÃO DO NORTE | PARÁ | Brasil | 1503077 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 4fd1c7b6-56e1-3d3c-b7d7-29fb333f88cc | -3.03374 | -53.91523 | 2026-10-07 05:04:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 970e74e2-49c5-33fe-838b-2b0cf7206eb1 | -2.77841 | -54.0925 | 2026-10-07 05:04:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 0cfb635d-5919-3fdf-bede-a048417d7ae5 | -1.10917 | -54.15073 | 2026-10-07 05:04:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 3ed85372-77d0-3d5a-a4eb-6fb4bcad1734 | -2.99573 | -54.05059 | 2026-10-07 05:04:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| b10e4e29-e75e-3dcd-b797-62b6c7cbec47 | -2.95721 | -54.14541 | 2026-10-07 05:04:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 07f6e887-10c2-3b81-a25e-45b19b6b745c | -2.37431 | -56.13659 | 2026-10-07 05:04:00 | NOAA-21 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 32ccf764-57a0-3087-84ef-6d708689cbf6 | -3.37837 | -58.1905 | 2026-10-07 05:04:00 | NOAA-21 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 4671e267-a352-369e-84f8-510116d9f0d6 | -7.25116 | -45.26351 | 2026-10-07 05:04:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| c14cb39d-1d8c-373a-bde8-bbe75540cbf9 | -4.37018 | -43.91057 | 2026-10-07 05:04:00 | NOAA-21 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 568cfd33-3bb9-3349-9536-071df51cc01d | -2.41305 | -51.30433 | 2026-10-07 05:04:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 32816d58-4195-31fa-9529-72bbc02ac6c5 | -3.2448 | -57.86994 | 2026-10-07 05:04:00 | NOAA-21 | BOA VISTA DO RAMOS | AMAZONAS | Brasil | 1300680 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| cbf13d5c-cc31-358d-8273-60c5c280e456 | -3.53928 | -54.64952 | 2026-10-07 05:04:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 7.8 |
| 3c0356b0-2909-3722-8de9-7b5c15af63ea | -3.2789 | -54.04746 | 2026-10-07 05:04:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| cf267084-a5e5-31d5-9252-0ce6f6e0f8b8 | -3.50044 | -51.69521 | 2026-10-07 05:04:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 7.1 |
| 74d47e98-93a0-33c5-9f59-68e4946f0363 | -7.27113 | -45.57546 | 2026-10-07 05:04:00 | NOAA-21 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 5.3 |
| cf868662-79da-339e-beaa-e9832ba3b514 | -3.85745 | -55.98816 | 2026-10-07 05:04:00 | NOAA-21 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 827ed0f2-5851-3a71-9904-6b5f773bde88 | -3.17353 | -58.63332 | 2026-10-07 05:04:00 | NOAA-21 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| edd99869-5b39-3107-80ad-98ac1d23667a | -1.79701 | -57.10604 | 2026-10-07 05:04:00 | NOAA-21 | NHAMUNDÁ | AMAZONAS | Brasil | 1303007 | 13 | 33 | nan | nan | nan | Amazônia | 4.1 |
| bebd114a-90cd-3f36-b6b0-680863e92632 | -3.28161 | -54.00802 | 2026-10-07 05:04:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| b2269b6f-c845-30ee-bbc6-850b9d08e794 | -5.28573 | -56.02001 | 2026-10-07 05:04:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 6bd4d5c6-22e3-38c6-b378-1f6604ce91f9 | -3.68046 | -55.94669 | 2026-10-07 05:04:00 | NOAA-21 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 6e686e52-fda3-3790-90ba-7261fb169260 | -2.85657 | -59.11184 | 2026-10-07 05:04:00 | NOAA-21 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 3.8 |
| b52ef894-c578-3713-bdb9-fff2eeaef088 | -6.1488 | -47.34871 | 2026-10-07 05:04:00 | NOAA-21 | CAMPESTRE DO MARANHÃO | MARANHÃO | Brasil | 2102556 | 21 | 33 | nan | nan | nan | Cerrado | 4.3 |
| d379fbc9-0752-3a1e-b0b0-afc91691dcf1 | -3.29 | -54.02017 | 2026-10-07 05:04:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 9.4 |
| a1e74a74-ac7d-3def-a3da-fc194fdb2b38 | -2.78707 | -51.68153 | 2026-10-07 05:04:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 14.3 |
| e587b0e2-91c9-3271-ba85-34745e556bdf | -7.09438 | -45.56987 | 2026-10-07 05:04:00 | NOAA-21 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 95e00e4b-c839-312d-9412-55b3968c7bac | -3.062 | -54.2154 | 2026-10-07 05:04:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 067410f0-ad92-389c-b33c-ad36e1fe1c3e | -2.88575 | -54.12388 | 2026-10-07 05:04:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 0e1ee2b1-0c9d-362b-9274-bbaa45e26ff0 | -2.95677 | -54.10604 | 2026-10-07 05:04:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 0b462069-e704-35d4-9d48-72a29aab6475 | -1.76769 | -55.03388 | 2026-10-07 05:04:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| b486049c-d2a9-3f27-9342-50dec6b21baa | -3.29993 | -54.06137 | 2026-10-07 05:04:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 7.9 |
| fc6fecce-25f5-3bbf-b95d-837e195fce6e | -3.45865 | -54.5982 | 2026-10-07 05:04:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 5191ff59-0af1-369a-9f3f-0fdaa7a11e05 | -3.5647 | -54.2215 | 2026-10-07 05:04:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 3357de11-afbe-35b3-80ea-cc5392d79918 | -3.00029 | -51.00964 | 2026-10-07 05:04:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e8ad40b9-8102-3747-ad1f-7a4f84cb1e01 | -4.25284 | -50.72796 | 2026-10-07 05:04:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 0fbf605a-39c5-3305-a16a-6e428092770a | -3.04214 | -53.92743 | 2026-10-07 05:04:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 899dd52f-58ad-35d4-a65d-ff3d4f14b146 | -2.99897 | -54.18413 | 2026-10-07 05:04:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 5cb2c2ee-a6db-3e3a-9424-c9641d86c31a | -3.28184 | -53.82942 | 2026-10-07 05:04:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 9c1cc893-041e-33cf-90f5-adbd8149c6d3 | -3.71808 | -58.81701 | 2026-10-07 05:04:00 | NOAA-21 | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 793cd1dc-d6eb-302d-9d58-1d93bf9e5039 | -3.04935 | -54.14526 | 2026-10-07 05:04:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 4ed8f630-7029-3d0a-b038-2e772b901245 | -3.85967 | -55.99558 | 2026-10-07 05:04:00 | NOAA-21 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| c0333a67-41b9-3c85-8258-247d1183bd73 | -3.08446 | -54.29044 | 2026-10-07 05:04:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 15d9ceaf-b9fe-39cb-916c-de9e23edb5c3 | -3.04384 | -53.93858 | 2026-10-07 05:04:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 231afd87-03be-3e5d-aae7-b60cb1cb7d61 | -2.92798 | -54.13755 | 2026-10-07 05:04:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 19ed1e4d-e541-33dd-ac88-702e41aa03a4 | -3.43919 | -49.25566 | 2026-10-07 05:04:00 | NOAA-21 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 71fd2c15-1e1e-3e18-986e-826ccedb303e | 0.44471 | -60.53675 | 2026-10-07 05:04:00 | NOAA-21 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 2.2 |
| cce7bf34-3d0c-31c8-aa7e-59e1257b2aac | -3.14444 | -53.7237 | 2026-10-07 05:04:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| afe61ef4-2de5-3d05-97ab-47ac374c5738 | -2.00417 | -56.95031 | 2026-10-07 05:04:00 | NOAA-21 | NHAMUNDÁ | AMAZONAS | Brasil | 1303007 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| ea4a0ca4-c029-3488-b008-2d01e86ed922 | -3.1863 | -50.56212 | 2026-10-07 05:04:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 14.0 |
| 06cf7a11-77e9-301d-80d3-922e21512dc0 | -2.98066 | -54.03743 | 2026-10-07 05:04:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f734a47f-239d-3ed4-88d8-9c59c92978f2 | -3.03989 | -53.9198 | 2026-10-07 05:04:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| a3346189-4444-36f0-a8ea-e34e799892ec | -2.77174 | -54.09148 | 2026-10-07 05:04:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 9.0 |
| ae13dc70-5857-3ba2-a341-8fcacb461515 | -4.08014 | -54.88982 | 2026-10-07 05:04:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 6f0367c6-5c62-393c-baa5-1c3146a0dc7b | -3.26946 | -54.06409 | 2026-10-07 05:04:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| c4853ee2-08e6-36fd-a6e0-a4b684e35b32 | -1.28608 | -54.56563 | 2026-10-07 05:04:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 30bfaa2b-adcc-3346-8daf-fff0e849c737 | -3.27549 | -50.42344 | 2026-10-07 05:04:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 3241602d-f0c1-3254-b8e6-2e983b85b485 | -2.90002 | -54.07574 | 2026-10-07 05:04:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 5bb06fcb-4059-3d6c-9494-6576e550f074 | -3.28448 | -54.05555 | 2026-10-07 05:04:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 9586a712-ed9f-3110-a0e6-131a27b2b863 | -3.00603 | -54.13859 | 2026-10-07 05:04:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 20027909-019d-3375-a310-667f8860b7de | -4.12565 | -54.41971 | 2026-10-07 05:04:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| cc81f53b-bcb4-3398-bd6f-22109a8b3ec3 | -3.26856 | -50.41542 | 2026-10-07 05:04:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 40f360fc-f2cd-37d7-8584-27c3856e4362 | -3.64275 | -58.88888 | 2026-10-07 05:04:00 | NOAA-21 | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e1c69ce7-098a-3bf6-bd12-cc42aee571ac | -3.28724 | -54.03787 | 2026-10-07 05:04:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 11.0 |
| 8efd4bb2-81e4-3897-9d87-6258a8cff4f1 | -2.49617 | -56.11951 | 2026-10-07 05:04:00 | NOAA-21 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 6b7965b9-12f5-3167-9410-61ad9d010feb | -3.02697 | -53.89237 | 2026-10-07 05:04:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| c8ee952b-ca02-36af-a791-abeb7ec389c9 | -2.5615 | -54.59251 | 2026-10-07 05:04:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| d93ac5ea-8129-38c2-82d7-65a22d5c2c5a | -2.99208 | -54.11846 | 2026-10-07 05:04:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 1c4d2a6d-b65d-3453-9866-601744085a2a | -5.5842 | -48.95143 | 2026-10-07 05:04:00 | NOAA-21 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 8fc689da-06e6-3bd6-af05-1e22be2446e1 | -1.28662 | -54.5622 | 2026-10-07 05:04:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| a5d0da8b-4eea-3ccb-98c0-05297c127432 | -2.77453 | -54.09549 | 2026-10-07 05:04:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| f4d4e5fc-4645-3e10-ae3b-33f2f3ca2a61 | -2.77903 | -54.11054 | 2026-10-07 05:04:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 9a43a452-0042-3e52-b590-0f8f551b89c5 | -4.15406 | -55.15871 | 2026-10-07 05:04:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 5e000646-ee2f-37ba-b23a-0fff848659c1 | -3.24365 | -57.86979 | 2026-10-07 05:04:00 | NOAA-21 | BOA VISTA DO RAMOS | AMAZONAS | Brasil | 1300680 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| bb767842-ab8f-3304-811a-50f037894446 | -3.05427 | -54.22138 | 2026-10-07 05:04:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| d0c72f93-d419-30cc-82f0-dce74a6371bd | -3.50983 | -51.68327 | 2026-10-07 05:04:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 48912e62-1335-3218-bff9-9031e670d310 | -3.03874 | -53.90509 | 2026-10-07 05:04:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| d42cb394-ebaf-3596-8f43-b2cbdcc9a781 | -2.8839 | -56.6659 | 2026-10-07 05:04:00 | NOAA-21 | PARINTINS | AMAZONAS | Brasil | 1303403 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 2e250b51-0953-324e-b7fd-b1a9591e5105 | -7.46486 | -47.6005 | 2026-10-07 05:04:00 | NOAA-21 | BARRA DO OURO | TOCANTINS | Brasil | 1703073 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 9816feb7-86a5-36c2-8ff8-7feaae510d4a | -3.27445 | -50.43027 | 2026-10-07 05:04:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 66b62ac8-ecca-31c4-9f3c-6f969f21b949 | -4.31792 | -50.77964 | 2026-10-07 05:04:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| dbd8310c-25a5-3370-aeec-570b1e3adaa8 | -4.55662 | -49.35116 | 2026-10-07 05:04:00 | NOAA-21 | JACUNDÁ | PARÁ | Brasil | 1503804 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| d5cb0485-cc18-35e7-acea-901ff38bcf56 | -3.15376 | -54.08564 | 2026-10-07 05:04:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 361308f8-a257-307b-8b12-13915e1a07e0 | -2.98129 | -54.05557 | 2026-10-07 05:04:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 7ed09be3-c6a5-31ae-80bf-f9defc735929 | -3.28052 | -50.41716 | 2026-10-07 05:04:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |


[Clique aqui para ver as próximas entradas](README74.md)
