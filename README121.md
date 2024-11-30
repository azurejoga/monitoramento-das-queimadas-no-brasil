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

## Dados Diários - Página 121

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 4035b34e-c314-3d15-bd8b-fb535a33506c | -3.63986 | -54.44512 | 2024-11-30 05:27:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| e39daeac-aa60-3edb-8a38-cbe8410870c2 | -2.33148 | -54.50319 | 2024-11-30 05:27:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 00943687-2461-3a7e-b0ff-b1302ffa1ef5 | -2.62447 | -54.21708 | 2024-11-30 05:27:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 3271bd57-df12-3ddd-bc4d-c6f114093707 | -3.11101 | -53.11262 | 2024-11-30 05:27:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 4e3aecf3-f6e6-3b7c-b1fa-9d9e75a5816b | -1.63212 | -53.86955 | 2024-11-30 05:27:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 0eae24cf-657a-32a2-9b92-dad1d5a864aa | -1.58976 | -52.28593 | 2024-11-30 05:27:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 06ea8d9a-6604-3f27-88b8-a5cd90ec406a | 1.18334 | -55.97941 | 2024-11-30 05:27:00 | NOAA-20 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| f48aaae3-98f2-35e4-b90e-e7203a4b540f | -3.1471 | -53.82891 | 2024-11-30 05:27:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| f894748f-cd03-33e6-8fa2-31bb463ba146 | -2.19945 | -53.74749 | 2024-11-30 05:27:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 05a4481f-9e06-3ba2-a46d-deec19255f9c | -2.90051 | -54.77731 | 2024-11-30 05:27:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| acabe096-1ff5-348c-bd29-2d7965829cd7 | -3.09074 | -51.41213 | 2024-11-30 05:27:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 0abaf33b-e530-334d-ab51-672a7f677b9a | -1.74198 | -52.31433 | 2024-11-30 05:27:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| f5946a69-dfbd-398b-93c1-f3641802859c | -2.82698 | -54.09201 | 2024-11-30 05:27:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 195b8981-4f14-38fa-92b5-9a73239ada43 | -0.09408 | -51.7474 | 2024-11-30 05:27:00 | NOAA-20 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 1179c588-a9dc-36aa-bd05-f6c686da6307 | -1.3417 | -55.90736 | 2024-11-30 05:27:00 | NOAA-20 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 4bbe570d-562b-3b96-9546-fe48731749f7 | -4.19794 | -50.69062 | 2024-11-30 05:27:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 449d95a3-076f-3b98-8836-08adf691699e | -3.50337 | -53.83508 | 2024-11-30 05:27:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 8e564662-6d3e-36cf-b350-83695f8482f6 | -1.65294 | -52.73116 | 2024-11-30 05:27:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| e0edecac-0c3a-3e25-9078-915fc830c82b | -3.35182 | -50.51879 | 2024-11-30 05:27:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 2dbb667b-dd26-3562-a4a9-8af1f9d24f6b | -1.36292 | -54.6519 | 2024-11-30 05:27:00 | NOAA-20 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 6ec03dcc-299c-3268-aa8a-69982182c604 | 0.93549 | -50.74562 | 2024-11-30 05:27:00 | NOAA-20 | CUTIAS | AMAPÁ | Brasil | 1600212 | 16 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 4f371daa-f4ef-3071-85c9-230967616ace | 1.44107 | -55.87863 | 2024-11-30 05:27:00 | NOAA-20 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| d4634d5f-a588-37ea-b126-5535a9f1ef34 | -3.14559 | -53.839 | 2024-11-30 05:27:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 6.9 |
| 21df8f00-8a9a-3cc4-bc01-552a22d6dc32 | -2.98292 | -53.28766 | 2024-11-30 05:27:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| ccf4fa7e-d147-36c8-94a3-e82ffaf92a0f | -4.07859 | -50.02672 | 2024-11-30 05:27:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 7.6 |
| 59a12d82-450d-3ca5-b645-bd819b2b3903 | -1.04176 | -51.7387 | 2024-11-30 05:27:00 | NOAA-20 | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 647813e8-174e-33d0-b76c-a5c060995c28 | -1.679 | -52.50436 | 2024-11-30 05:27:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 032e3214-68ec-3c66-8ccd-9ad271b58c36 | -1.98844 | -53.29651 | 2024-11-30 05:27:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 4e8d24ca-3407-3bab-9b1b-db921233ad14 | -3.07551 | -50.33193 | 2024-11-30 05:27:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 45124694-e592-34db-918e-a20f72401579 | -3.38517 | -53.50983 | 2024-11-30 05:27:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 1093d0fb-8c4a-3ad2-b390-dcca6d7c357f | -1.58247 | -53.8521 | 2024-11-30 05:27:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| bcc27fed-a194-3990-8c51-d356a1c9888b | -1.42755 | -55.27761 | 2024-11-30 05:27:00 | NOAA-20 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 6c868f58-c8e8-31a5-baff-3c7f09d16e11 | -1.71709 | -52.7823 | 2024-11-30 05:27:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ac850b02-7bd3-32b6-996c-a8bd07169f7e | -0.96183 | -51.65463 | 2024-11-30 05:27:00 | NOAA-20 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f91ed3c2-575b-3d70-9f0f-a785c674ec9f | -2.72603 | -54.14023 | 2024-11-30 05:27:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| f433fb88-57c9-3e1d-86d4-30c04d0fe906 | -3.82498 | -50.14185 | 2024-11-30 05:27:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| d079d9b7-d5d3-3ede-8758-b764fd178981 | -3.2466 | -50.59333 | 2024-11-30 05:27:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| abef12c8-c748-3662-9d8e-aefdea73393d | -2.61133 | -54.2104 | 2024-11-30 05:27:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 6b2b8a4a-03bb-3cfc-ba23-8de7ed47834c | 0.99245 | -50.26619 | 2024-11-30 05:27:00 | NOAA-20 | CUTIAS | AMAPÁ | Brasil | 1600212 | 16 | 33 | nan | nan | nan | Amazônia | 1.5 |
| dbe0cb09-e481-350f-9062-4cf04d712d2f | -1.24786 | -54.55096 | 2024-11-30 05:27:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| f82b5443-f161-34af-a0ff-332d86e30d8f | -3.05625 | -53.17102 | 2024-11-30 05:27:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 7bfe722c-fc2a-3e72-a96c-05113b8cee40 | -3.73689 | -51.83881 | 2024-11-30 05:27:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| e9aa2925-2e26-3d69-bed1-8ea42ef3b3fd | -3.29933 | -53.69548 | 2024-11-30 05:27:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 3e88a2b5-d636-320a-8db1-54ca5405e2e1 | -3.45358 | -54.56498 | 2024-11-30 05:27:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 968d00bc-6c91-317a-b26f-3452272b4107 | -3.24767 | -53.64445 | 2024-11-30 05:27:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| b5c3b5f8-0913-3bbb-b5ec-07b5e333337e | -1.99512 | -52.09618 | 2024-11-30 05:27:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 8b4d74aa-2119-37e2-b764-ac74c1201f12 | 1.97511 | -60.92041 | 2024-11-30 05:27:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 393e2cb2-45ab-3246-8b62-e8efd710161a | -1.62049 | -53.88341 | 2024-11-30 05:27:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 5e593392-5a78-3292-b996-4e9b0a621e80 | -1.6422 | -53.86583 | 2024-11-30 05:27:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 34.4 |
| 1fb9d33b-8690-36d7-b5ee-85e9996e0a48 | -1.60999 | -52.29216 | 2024-11-30 05:27:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 0bb01496-80d2-3e11-8e0d-af7b18386111 | -2.88994 | -54.16842 | 2024-11-30 05:27:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| faf3024b-bdc9-30f0-b014-aab51054894a | -3.03414 | -59.11935 | 2024-11-30 05:27:00 | NOAA-20 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| fe786004-3dfc-3c53-b758-6f70a0fcdb10 | 2.36823 | -61.26112 | 2024-11-30 05:27:00 | NOAA-20 | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 06d7e8d3-8455-37f0-96a2-97559cefc958 | -2.8249 | -54.09436 | 2024-11-30 05:27:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| caa4bf55-c2a9-3d57-8084-dceabae5fa4e | -3.24873 | -53.86836 | 2024-11-30 05:27:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 31b9d5f3-4b67-37ac-bc37-dcb56473dcdf | -3.06918 | -54.40818 | 2024-11-30 05:27:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 7b32b071-be5d-3351-83fd-0fb866d01a81 | -1.69394 | -52.45798 | 2024-11-30 05:27:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a3e18005-2546-3e3a-a781-29f6a43c4a8d | -1.32978 | -55.85155 | 2024-11-30 05:27:00 | NOAA-20 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 8d0970d0-0c62-37ec-bc9d-e617e58ecc62 | -4.0799 | -50.02899 | 2024-11-30 05:27:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 737d3959-af66-38e4-b4fc-c2b2f0bf5aa1 | -1.70427 | -52.76559 | 2024-11-30 05:27:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 94ca2f73-8b56-3073-aa99-c7bd72de09b0 | -3.24778 | -51.34702 | 2024-11-30 05:27:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 40b480b0-685a-3a8c-b870-ae46f3b18de3 | 0.93596 | -50.74794 | 2024-11-30 05:27:00 | NOAA-20 | CUTIAS | AMAPÁ | Brasil | 1600212 | 16 | 33 | nan | nan | nan | Amazônia | 3.8 |
| a0c75ecc-6f3e-3a8b-8cd3-dc2414b4e1d8 | -1.40696 | -51.58485 | 2024-11-30 05:27:00 | NOAA-20 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| bc93d69d-876f-354b-93c2-cfd43f933145 | -3.46216 | -53.8812 | 2024-11-30 05:27:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| a6d7e091-d5fa-383b-8c0b-834ddcd16ff0 | -3.35426 | -49.10083 | 2024-11-30 05:27:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 907ea60f-23aa-35da-9b17-00f9bd565bff | -1.37233 | -53.64264 | 2024-11-30 05:27:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| be43f4aa-10d8-3159-9008-518050909a44 | -1.62456 | -52.38111 | 2024-11-30 05:27:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 1cb21ca0-03f1-338a-b1dc-67c2e9e15184 | -2.84715 | -54.085 | 2024-11-30 05:27:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 690813b0-a019-3d02-b4f3-571cf4cf918c | 1.19111 | -55.95351 | 2024-11-30 05:27:00 | NOAA-20 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 96316c2e-bfc8-31d8-8d76-dd452473b17b | -3.52097 | -62.84743 | 2024-11-30 05:27:00 | NOAA-20 | CODAJÁS | AMAZONAS | Brasil | 1301308 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 089b894f-9e51-3806-8bf4-7febec87f70c | -3.96111 | -50.19389 | 2024-11-30 05:27:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 58eb9edf-c5b3-39a0-98ff-4576c2d09bb0 | 1.87535 | -55.73213 | 2024-11-30 05:27:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 799925b5-006b-3e24-b661-fe106bbd362c | -2.44421 | -53.62043 | 2024-11-30 05:27:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 9574684b-da06-3a15-8b0e-fd35370f73a7 | -1.30479 | -51.73317 | 2024-11-30 05:27:00 | NOAA-20 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 4046966d-4ffb-3b01-a103-f004be94cd16 | -1.42335 | -55.27699 | 2024-11-30 05:27:00 | NOAA-20 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 0b4eeb43-c75a-3220-95c8-5e912d973f48 | -2.53375 | -54.03838 | 2024-11-30 05:27:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| c2657dae-7680-3b26-9ba1-ceba04d067f8 | -1.58349 | -53.85457 | 2024-11-30 05:27:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 5fbff8d5-de8b-39b6-82c8-9b43c450216b | -3.34338 | -50.7469 | 2024-11-30 05:27:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 840461cd-3e5e-3177-ba83-ef995df4e91e | -3.24738 | -54.21548 | 2024-11-30 05:27:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| b338edcb-5810-3b57-ac0e-7f03d4f8ddca | -3.2209 | -54.18037 | 2024-11-30 05:27:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 733d467d-a1fa-3cfa-a197-618c86ff8e83 | -1.07427 | -53.63277 | 2024-11-30 05:27:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 10.0 |
| 68b80b44-0bd9-3ddb-bb75-7e30c9214fe0 | -3.24283 | -53.64369 | 2024-11-30 05:27:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| ca2a533c-46be-3090-b1b7-f4d7dda7ad54 | -2.44526 | -57.88745 | 2024-11-30 05:27:00 | NOAA-20 | SÃO SEBASTIÃO DO UATUMÃ | AMAZONAS | Brasil | 1303957 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| bb4c27d4-1ba8-34dd-87cd-d3b1bbeaa95b | -3.48725 | -53.81189 | 2024-11-30 05:27:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 8.3 |
| 8071df1a-d2e2-37d1-99d9-7f3cfa7d4594 | -0.26634 | -51.64515 | 2024-11-30 05:27:00 | NOAA-20 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 0.9 |
| fa63adc9-7e15-30cf-9e09-01424255d562 | -2.43862 | -53.62498 | 2024-11-30 05:27:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 6b0e0455-dbae-3e46-a368-8285fd216791 | -1.99463 | -52.09943 | 2024-11-30 05:27:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| b7d39da8-54cf-3780-90f0-7614c15a7b11 | -4.28739 | -59.68664 | 2024-11-30 05:27:00 | NOAA-20 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 3132a533-b59c-3dea-a303-aac78e47c94d | -3.65075 | -50.22055 | 2024-11-30 05:27:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 34ebe575-bf3d-3717-8b76-990c014e6dda | -1.33817 | -54.98758 | 2024-11-30 05:27:00 | NOAA-20 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 8.2 |
| 521fc46b-96b5-3a0d-a103-8d29b072c791 | -3.46828 | -50.53366 | 2024-11-30 05:27:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 2b75d04c-c16c-3cee-80ed-dd7c565d239a | 0.74091 | -50.87193 | 2024-11-30 05:27:00 | NOAA-20 | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 35f90a2c-7351-36f2-bf05-5d3ff2d64a98 | -2.02647 | -53.50213 | 2024-11-30 05:27:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 491ef8b9-d997-3751-b93c-7e5ea78847d6 | -1.32488 | -54.63507 | 2024-11-30 05:27:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| db7e51d3-0615-33e5-b555-3989a5d007bb | -2.61985 | -54.21647 | 2024-11-30 05:27:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| a2688fc5-be3a-3870-b5c2-4344d3eb0db1 | -3.51086 | -62.84583 | 2024-11-30 05:27:00 | NOAA-20 | CODAJÁS | AMAZONAS | Brasil | 1301308 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 63b8a1db-b93f-3d0e-a7d8-ee3770c08da6 | -2.86965 | -53.98547 | 2024-11-30 05:27:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 7307c653-809b-3cb3-a18b-443439c23973 | 0.06516 | -51.49479 | 2024-11-30 05:27:00 | NOAA-20 | SANTANA | AMAPÁ | Brasil | 1600600 | 16 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 81abe85b-b055-3c73-b8ff-9ae2bcfa900b | -3.25172 | -53.6505 | 2024-11-30 05:27:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 0ab5b2df-2faa-33ce-aca1-981a1ec95746 | -3.10371 | -50.36138 | 2024-11-30 05:27:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |


[Clique aqui para ver as próximas entradas](README122.md)
