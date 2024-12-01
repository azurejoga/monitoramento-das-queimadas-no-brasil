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

## Dados Diários - Página 55

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 3a58989b-a33c-3b87-acbb-ece26ba7cf7d | -4.05085 | -46.81876 | 2024-12-01 04:44:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e6b9bfec-50f9-377d-b63f-eb6e62611fcb | -1.16861 | -51.94026 | 2024-12-01 04:44:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| ff1184c9-c3f2-3270-8b06-e8902c145a33 | -3.25612 | -53.62738 | 2024-12-01 04:44:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |
| e9d3e1d9-2269-3549-8b9c-a8f734f60d13 | 1.077 | -60.32312 | 2024-12-01 04:44:00 | NPP-375D | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 152f550b-3d5f-387c-8ea6-1c651d75eb75 | -2.87377 | -54.01205 | 2024-12-01 04:44:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 395809ed-de84-3b15-917d-c25b3a2fcdc1 | -2.42301 | -50.39335 | 2024-12-01 04:44:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 25cb2416-6ae5-3532-ac55-19002945fb2c | -3.36664 | -51.12828 | 2024-12-01 04:44:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| f72ea45d-b7f0-3284-a637-2752cd757df7 | -2.95254 | -51.78546 | 2024-12-01 04:44:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 0b0afb33-97be-3fcd-af38-d61c83ce36e7 | -4.03946 | -54.11322 | 2024-12-01 04:44:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| a3ec6c10-255f-3350-a236-f0fea7a14739 | -4.55423 | -45.72635 | 2024-12-01 04:44:00 | NPP-375D | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 22.2 |
| 2dc50b5c-3623-36d4-91b8-7d851474919b | -4.03312 | -46.93214 | 2024-12-01 04:44:00 | NPP-375D | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 2.7 |
| f52ad254-3d20-3fbb-af1c-e1df0e1ade03 | -2.46318 | -53.70773 | 2024-12-01 04:44:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 86834db4-6549-3588-85b8-9669296a4a8b | -1.92121 | -52.65878 | 2024-12-01 04:44:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 69e6b693-ca7f-380f-9666-717b8f8cb2d1 | -3.056 | -54.05595 | 2024-12-01 04:44:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d3840207-f47c-3aca-9445-ccb718461595 | -4.01796 | -47.00504 | 2024-12-01 04:44:00 | NPP-375D | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 1df435b5-1e52-3a06-90b0-9a3b12482b3f | -2.63089 | -54.22797 | 2024-12-01 04:44:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| ef2afc50-a70f-3951-b365-4c509cd7eeaa | -3.50542 | -53.83459 | 2024-12-01 04:44:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 7.5 |
| 532da26a-85b6-372d-b19d-5e92376f7761 | -1.16935 | -53.41393 | 2024-12-01 04:44:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| edf91f59-291a-317b-ae77-620f313fc39a | -3.25275 | -50.754 | 2024-12-01 04:44:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 96180dc0-8329-364d-8aa6-ecf830c27852 | -2.6346 | -54.20464 | 2024-12-01 04:44:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 79b4e117-e0c0-347b-8cf8-88670b614025 | -2.73828 | -54.03933 | 2024-12-01 04:44:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| d09ea79d-f48f-3531-a63d-17b1720b3cd3 | -2.2644 | -53.45787 | 2024-12-01 04:44:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| bf15e264-3c49-3f1d-9b2d-bc3f525fe754 | -5.58504 | -45.21515 | 2024-12-01 04:44:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 7.9 |
| 88820fce-1535-3980-a9e6-557b3a173fa6 | -2.95127 | -49.4453 | 2024-12-01 04:44:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e8c9d44a-65e1-33a5-bc07-28972424c714 | -3.90939 | -52.33581 | 2024-12-01 04:44:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 71efffe6-a638-36a3-b945-13ab4edb43b8 | -2.68138 | -46.60506 | 2024-12-01 04:44:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 9fa9ddc6-ddc6-395e-a419-4c856f9e77cb | -1.11847 | -51.9208 | 2024-12-01 04:44:00 | NPP-375D | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 38724640-bd7b-3141-94ad-273dbabc75a4 | -2.3288 | -50.6694 | 2024-12-01 04:44:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c82a7dd9-9bb1-3ba9-9f60-d3d6209d17ee | -2.65851 | -51.87819 | 2024-12-01 04:44:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 15.3 |
| e3a6776b-6f7e-3378-98d9-080088f61c36 | -1.26687 | -51.75546 | 2024-12-01 04:44:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 98a074c5-1b25-3e35-8936-753157962c54 | -4.55977 | -45.71657 | 2024-12-01 04:44:00 | NPP-375D | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 40f5e2f9-998f-3a7b-ad85-6f8658a7a6a5 | -2.59586 | -53.98857 | 2024-12-01 04:44:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| ca1b39a2-d90e-3d89-b502-30ccb4157ae5 | -4.49704 | -49.63798 | 2024-12-01 04:44:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e1b027f7-1761-3b93-a73f-2d02d30f54e9 | -1.19998 | -52.56281 | 2024-12-01 04:44:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| c82db48c-c2c4-3594-aaf7-0fad4b2099c1 | -4.20727 | -48.12517 | 2024-12-01 04:44:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| e685adf5-6651-3273-9daf-c62861715183 | -3.21739 | -54.22673 | 2024-12-01 04:44:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 8a8a7b21-720c-344b-bc3b-456f8956ed0c | -3.22245 | -53.62652 | 2024-12-01 04:44:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c7d44e6e-e335-32b3-9917-919567cc3279 | -3.34807 | -50.14976 | 2024-12-01 04:44:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 687379fb-0073-3470-8f92-d6383ffe390d | -2.85316 | -54.09253 | 2024-12-01 04:44:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 0d57f04e-437a-39ce-bb27-2b88ecaf2580 | -3.3803 | -50.69574 | 2024-12-01 04:44:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 30305852-f8cb-38d2-b488-5d3ec37de339 | -3.48148 | -50.44255 | 2024-12-01 04:44:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e8da2579-d77f-3c65-86bc-8aae07ea36ab | -1.82101 | -55.16826 | 2024-12-01 04:44:00 | NPP-375D | CURUÁ | PARÁ | Brasil | 1502855 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 6532661d-1184-392a-afae-867aba942d4a | -2.47948 | -50.40216 | 2024-12-01 04:44:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 90c6a147-c567-325f-b432-13749208a411 | -1.07503 | -53.22735 | 2024-12-01 04:44:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 605c183e-5c0b-360e-a92e-1c518aa387f5 | -2.73678 | -47.98283 | 2024-12-01 04:44:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 25800ba6-c0c8-3203-837c-89705006ddbb | -3.94348 | -49.76001 | 2024-12-01 04:44:00 | NPP-375D | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 7f5dc991-b3b6-3f14-8e76-d0b3a85bb58d | -3.69478 | -51.81553 | 2024-12-01 04:44:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 3ea9a915-89c2-337b-b2dc-81a002c1833d | -3.12145 | -53.2785 | 2024-12-01 04:44:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 2edaa6b5-4fa0-3f14-9206-a885748ec9d4 | -2.899 | -51.57428 | 2024-12-01 04:44:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 065c13f4-edef-3c95-a2bd-62d4993b7e9f | -2.63243 | -46.87825 | 2024-12-01 04:44:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 77250456-3bfc-3c1b-abe6-3466ececcf3d | -3.18973 | -54.33434 | 2024-12-01 04:44:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 8b9a84d7-ee77-392c-85f3-4dd2b2741e36 | -3.50245 | -53.82954 | 2024-12-01 04:44:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 7.5 |
| e148891f-ab50-3243-acad-99e8e388e72c | -1.13938 | -52.58304 | 2024-12-01 04:44:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 88068b65-6a79-3e39-935f-d486f99bf247 | -3.93217 | -46.71704 | 2024-12-01 04:44:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 726a64db-4f4d-315c-a871-5ca6deaac74c | -3.21972 | -45.7674 | 2024-12-01 04:44:00 | NPP-375D | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| a4130f66-0880-3dfa-92d1-10bc0973e7b4 | -4.18833 | -50.68125 | 2024-12-01 04:44:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 4dd458a2-79f7-396c-adf0-fc86dfbe28ba | -2.4588 | -46.57425 | 2024-12-01 04:44:00 | NPP-375D | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 9d7ce3ef-0528-3387-8b41-e9c9073370c5 | -1.72977 | -52.50087 | 2024-12-01 04:44:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 1029324e-8441-39e4-a1b9-98050e0e86b2 | -3.32496 | -50.18857 | 2024-12-01 04:44:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| ddef69a1-26f0-3d92-8952-0845c9750842 | -3.36998 | -51.12881 | 2024-12-01 04:44:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 861a76b0-add2-33cf-85eb-56d8656825d4 | -1.18825 | -54.03636 | 2024-12-01 04:44:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 1842bee7-20cb-3c1d-8490-1e507c0bbf49 | -1.69385 | -52.63693 | 2024-12-01 04:44:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 374ded29-5985-343d-a116-11cc1e875474 | -3.33651 | -54.06681 | 2024-12-01 04:44:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 4a9c7839-4f6f-3ae0-b36e-cca5475b5e5a | -4.01498 | -47.00001 | 2024-12-01 04:44:00 | NPP-375D | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 44ff5c7b-1ad9-3c6e-920a-49848d5b2e39 | -1.27003 | -51.82465 | 2024-12-01 04:44:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| b6c45501-f05a-3c8e-8221-04e780ad3b05 | -3.5468 | -50.41446 | 2024-12-01 04:44:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 9feda380-2f32-3503-b06b-1134d2ec2716 | -1.17723 | -51.95322 | 2024-12-01 04:44:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 6442397b-8584-3f84-9ab1-263f1f91899e | -4.25158 | -50.83622 | 2024-12-01 04:44:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| abb124fc-9aa2-3404-9104-38ce9a2fd704 | -3.14518 | -53.8337 | 2024-12-01 04:44:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 59323f22-3dbd-33f9-8120-c830ce147c4b | -3.01316 | -54.05836 | 2024-12-01 04:44:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 4ec5959f-c5c7-3a51-8725-3383e9f86a62 | -2.95406 | -49.4493 | 2024-12-01 04:44:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 0eeb572c-5f77-3669-9a8f-b3cf99a20030 | -1.19513 | -51.74871 | 2024-12-01 04:44:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 57b7deb8-0645-3187-9f29-80d0c029b5e3 | -2.84055 | -49.8899 | 2024-12-01 04:44:00 | NPP-375D | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 869e0594-dd5e-30de-8898-fa27b457912d | -3.8511 | -46.54146 | 2024-12-01 04:44:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 469e20c0-79eb-3b2e-84f3-a2a8768ab513 | -3.85842 | -47.04781 | 2024-12-01 04:44:00 | NPP-375D | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 61b8587d-e791-305d-a7f9-e568b7efa40e | -3.47842 | -59.46067 | 2024-12-01 04:44:00 | NPP-375D | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 368296f5-9a57-34fd-bc14-0f0c60661172 | -3.32991 | -52.59875 | 2024-12-01 04:44:00 | NPP-375D | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 16528262-6a19-333e-b646-606b18e38844 | -2.83805 | -54.09011 | 2024-12-01 04:44:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 1fb7e5e1-3f29-3b60-88f9-b7ca8e9c918e | -3.03618 | -49.50849 | 2024-12-01 04:44:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 35fe4378-96b3-3707-9573-d2f32f46d594 | -3.12146 | -51.30984 | 2024-12-01 04:44:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 75a446a0-eb80-36a2-ad99-03f091fd05bd | -1.2932 | -51.36939 | 2024-12-01 04:44:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 556dcf06-de2f-3e6b-a9b4-fe958c5591d0 | -1.70189 | -46.14833 | 2024-12-01 04:44:00 | NPP-375D | BOA VISTA DO GURUPI | MARANHÃO | Brasil | 2101970 | 21 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 0c746d12-c6a2-3d4f-ab4c-d13a9936cb58 | -2.61646 | -51.81187 | 2024-12-01 04:44:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 85b20840-e96c-3a1b-8671-0b398a558479 | -2.48378 | -50.35332 | 2024-12-01 04:44:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 05299f0b-3294-3c9e-83c4-81edc5812f41 | -3.25476 | -53.63586 | 2024-12-01 04:44:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| c3cc8c8d-a441-3e81-8157-5d8919808209 | -1.15348 | -51.70037 | 2024-12-01 04:44:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 74bccebb-179e-36be-a562-fa10bb3289b5 | -3.11849 | -53.27383 | 2024-12-01 04:44:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 9242ae33-3a69-30f3-b043-cd14c911efba | -3.49888 | -52.12831 | 2024-12-01 04:44:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 86a06810-7cb9-3b24-9a63-2b511c6d1a20 | -3.69402 | -51.34137 | 2024-12-01 04:44:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| ede723d4-2239-306e-82ea-59261b8bd7ad | -3.03694 | -51.78024 | 2024-12-01 04:44:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 73f870b8-7ea7-3bd1-bcb1-815dee2572cb | -1.28377 | -51.67089 | 2024-12-01 04:44:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 7a469a68-61a1-310b-936e-6ec5a04da09c | -1.94805 | -53.33821 | 2024-12-01 04:44:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 305ab805-bc99-302f-9299-889371593c3b | -2.37667 | -50.51707 | 2024-12-01 04:44:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 78e561b7-ab7f-3111-9f72-8b90a9236f2a | -2.69303 | -51.72665 | 2024-12-01 04:44:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| e460554a-802c-3629-ac1d-1ba763ba8709 | -3.11755 | -51.31284 | 2024-12-01 04:44:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 0fae0923-0086-3287-a340-39731783c41c | -2.89906 | -51.36911 | 2024-12-01 04:44:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 0871cfe3-e79e-38be-a5d5-e1f2970a3a7c | -3.88939 | -47.06567 | 2024-12-01 04:44:00 | NPP-375D | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 2.6 |
| c2e38dff-3dbe-35c5-ba7a-36ec918e3484 | -4.3165 | -48.21177 | 2024-12-01 04:44:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| fca83d14-8d24-3bab-b29a-4e41aca21309 | -3.02585 | -54.02801 | 2024-12-01 04:44:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| eda30145-807b-3884-b5b2-dfc8cc5d5436 | -1.23392 | -51.80751 | 2024-12-01 04:44:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |


[Clique aqui para ver as próximas entradas](README56.md)
