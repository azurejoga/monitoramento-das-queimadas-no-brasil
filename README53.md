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

## Dados Diários - Página 53

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 596b3263-6149-37f3-8547-18fde46c5925 | -3.1182 | -54.60954 | 2024-12-04 05:29:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 517d690e-6567-3067-bf89-02b322562842 | -2.98108 | -53.88009 | 2024-12-04 05:29:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| ac33d077-37b5-3d7a-bcc1-fdc1e4659abc | -3.06797 | -53.26893 | 2024-12-04 05:29:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 1eb0d442-692b-3b69-a2c6-12c00cc98be3 | -1.38188 | -53.55791 | 2024-12-04 05:29:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 5860de60-b4db-31e5-9877-8ac74b42b2ed | -3.76215 | -52.08154 | 2024-12-04 05:29:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 9e33c5d9-d9f0-3280-af73-1809de23fced | -2.69413 | -51.86341 | 2024-12-04 05:29:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| b0477885-147f-3548-8f8f-0c59060a1e3d | -2.88569 | -54.16268 | 2024-12-04 05:29:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f7a0792c-95df-37d5-b11f-6bd6e67fccc5 | -1.75347 | -52.62082 | 2024-12-04 05:29:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 3542aa95-ae6b-38ed-8749-099985f17de1 | -2.57562 | -54.80698 | 2024-12-04 05:29:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 62690f06-7fb6-3216-9906-408b6d28feeb | -4.26949 | -50.68222 | 2024-12-04 05:29:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| ec5bbfd7-8740-37cc-88fb-228a56214cdf | -2.99946 | -53.82337 | 2024-12-04 05:29:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 5bb3e73b-8e5e-3cf5-8c05-bcfb07a0e108 | -1.62522 | -53.52987 | 2024-12-04 05:29:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 73bf5ae2-4a75-3521-b04a-d59dd837ef46 | -3.05556 | -54.50277 | 2024-12-04 05:29:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 7935c297-f462-328d-8f44-21298e5109a4 | -2.81581 | -53.05271 | 2024-12-04 05:29:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 532eded3-cb9a-31ce-ae98-d94cfe414da2 | -3.3749 | -52.78838 | 2024-12-04 05:29:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| deb24566-29e3-3c1f-9c65-853518e738b3 | -3.49518 | -51.55863 | 2024-12-04 05:29:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 8a727973-c8f2-3f46-99e5-474cb830a257 | -3.41366 | -63.49739 | 2024-12-04 05:29:00 | NPP-375D | COARI | AMAZONAS | Brasil | 1301209 | 13 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 57dbec93-6f0a-39e2-8e7d-6e161f7b92b0 | -3.55054 | -51.33744 | 2024-12-04 05:29:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| b581ac9a-9bbb-32dd-b75d-41b902c72351 | -1.6288 | -53.89318 | 2024-12-04 05:29:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| bdb92d96-38ef-3503-ad41-8a1f0326016c | -2.9935 | -54.09519 | 2024-12-04 05:29:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 2e968cc5-0295-30a6-9e2a-3884182b3d8b | -1.65557 | -52.38306 | 2024-12-04 05:29:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 6.3 |
| d9f77a46-50e8-3db7-bdf3-a65774808abe | -1.45943 | -54.95705 | 2024-12-04 05:29:00 | NPP-375D | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 1d91c0e3-dda7-3c77-87d4-e0b1b211bf0a | -1.89662 | -52.85112 | 2024-12-04 05:29:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ca4dbc91-6e3d-38e8-86ce-1d70eef36fc5 | -3.21919 | -53.72281 | 2024-12-04 05:29:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 2c83c929-10c5-378d-9eb1-f193eb78c71c | -3.06628 | -54.06035 | 2024-12-04 05:29:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 03ccf3cd-8445-3a5f-b7e6-b58c9c8896fc | -3.07101 | -54.06102 | 2024-12-04 05:29:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 0cce5421-1a5a-3cbc-bd5c-3baf6324f3ce | -1.44406 | -60.07757 | 2024-12-04 05:29:00 | NPP-375D | PRESIDENTE FIGUEIREDO | AMAZONAS | Brasil | 1303536 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d509b5cd-841f-3a34-a44a-cd840f63bb1f | -1.57978 | -52.24918 | 2024-12-04 05:29:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 569532ad-4ed2-38cb-a37c-af2e55bafd15 | -3.10091 | -54.05543 | 2024-12-04 05:29:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 61d3b9f7-b2a4-39fe-8e4c-f6e2af0fff4c | -3.12204 | -54.61488 | 2024-12-04 05:29:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 23.2 |
| 86aa8632-c1dd-3361-be6d-b882411c2976 | 1.08673 | -59.64592 | 2024-12-04 05:29:00 | NPP-375D | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ee22a1b9-6034-3521-b5d4-11a63c47c0db | -2.80942 | -53.06066 | 2024-12-04 05:29:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 6cb8bdca-44bd-36bf-9315-a30aa43b3af2 | -3.07253 | -54.05101 | 2024-12-04 05:29:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| b87ba6c5-ba1c-3bfb-a5b1-f4a7279c49c5 | -3.29489 | -53.66928 | 2024-12-04 05:29:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 275201ff-9193-37f4-b7e8-036cbcaff903 | -2.87992 | -54.03416 | 2024-12-04 05:29:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| aef4bccc-c55d-39f0-ac24-b3d773f68cb8 | -1.65084 | -52.37914 | 2024-12-04 05:29:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 0ca6d70e-4c30-3712-bd0a-b6d81fcbb3fb | -3.30953 | -53.36126 | 2024-12-04 05:29:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 59e88190-b1a0-32b3-be12-58b3f03a3116 | -1.64991 | -52.38538 | 2024-12-04 05:29:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| c58e7dbe-ea55-3012-aa50-3fdfee0607b8 | 1.04414 | -59.52741 | 2024-12-04 05:29:00 | NPP-375D | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 84e94520-a8cd-387c-8e16-5f88b96c471c | -1.76234 | -52.63139 | 2024-12-04 05:29:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 11.9 |
| c8f6528c-6de9-3452-85d8-825e226b7a63 | -3.13214 | -54.61378 | 2024-12-04 05:29:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 9.5 |
| 2dcc01c9-e111-3e28-83a6-90ab507dabcf | -2.88642 | -54.15773 | 2024-12-04 05:29:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 0575caf6-700e-34bd-af3a-f257754a5def | -1.89751 | -52.85207 | 2024-12-04 05:29:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| b7536caa-11be-315c-a057-fcdf4475d749 | -2.9475 | -51.40999 | 2024-12-04 05:29:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| d09af0e5-b2c0-3186-8e3e-613fedccc1fc | -3.05629 | -54.49808 | 2024-12-04 05:29:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 6bf1f378-0454-3c49-af10-992d43884ed0 | -2.89955 | -51.57589 | 2024-12-04 05:29:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| e9bbf42b-cdc6-3a20-8b19-f346825d4845 | -3.82436 | -52.11515 | 2024-12-04 05:29:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 22944680-2ed6-38a6-8f2b-492dafcd2f0d | -3.17747 | -54.33662 | 2024-12-04 05:29:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| fa6ca92c-e81a-3651-ab56-96468837a3dc | -1.03623 | -53.55079 | 2024-12-04 05:29:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b02b5935-c7f6-34ff-87e9-1aae2af864e4 | -1.74368 | -52.61623 | 2024-12-04 05:29:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 17.1 |
| 08d4d7a1-06ba-3822-be23-2c07c9295a6c | -1.75301 | -52.62383 | 2024-12-04 05:29:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 148b32f7-2a93-347b-bf90-76ed9a627781 | -2.80438 | -53.05988 | 2024-12-04 05:29:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 6f852208-ee4f-34c1-b98f-9883926bc65d | -1.26906 | -54.1155 | 2024-12-04 05:29:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 4193b27f-fc33-3bbb-ad46-48ec64ace06a | -2.78126 | -55.37141 | 2024-12-04 05:29:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| aa4e506b-0952-3f2b-84c7-52315362ce67 | -2.20805 | -53.77098 | 2024-12-04 05:29:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| f6446ac2-84e8-344a-979f-1fa875b47d67 | -1.75676 | -52.63362 | 2024-12-04 05:29:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 11.9 |
| 8674dbd7-8720-331c-a634-a7de8d610f39 | -1.75256 | -52.62683 | 2024-12-04 05:29:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 41cf3782-3959-3070-86ca-7e1c8c21388e | -2.63615 | -53.35896 | 2024-12-04 05:29:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 75fa474d-8d88-3530-ad5d-14bad320756f | -2.99708 | -54.12447 | 2024-12-04 05:29:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 720772b7-3803-3c2b-be6e-f0a1fd71b941 | -3.1154 | -54.62777 | 2024-12-04 05:29:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 2bd3bca5-6be0-3618-b0d3-edce9fa10075 | -3.19007 | -51.17438 | 2024-12-04 05:29:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e4321ce9-559f-329a-a49a-4eca9aae3028 | -2.95375 | -51.40691 | 2024-12-04 05:29:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| c83e1a10-df1a-3fb4-bab5-d61b1e325e84 | -2.9481 | -51.40603 | 2024-12-04 05:29:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| ae2be884-4ad6-3c0a-8580-c73f4921d62f | -2.81165 | -53.0461 | 2024-12-04 05:29:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| cc512eef-b07d-367d-8d64-2623129a1d36 | -3.81197 | -51.65971 | 2024-12-04 05:29:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 7a8789d2-dc8f-3e94-8973-497b3cbf4396 | -1.64539 | -52.37822 | 2024-12-04 05:29:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| e7d1c926-8a5a-39ea-a578-2e5165ed3e15 | -1.29331 | -54.20214 | 2024-12-04 05:29:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| d242e892-1a18-3573-8ea4-573083f4321b | -3.92412 | -52.39677 | 2024-12-04 05:29:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| a8811bf9-64e9-386c-995f-03c2bdd7c541 | -3.24043 | -50.41914 | 2024-12-04 05:29:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| fabfb571-0c62-39ea-acfa-bf7add73d505 | -3.03639 | -54.06618 | 2024-12-04 05:29:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 5a897fba-7bcb-34dd-8eb6-8846b7b83c49 | -2.82636 | -53.05132 | 2024-12-04 05:29:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| bbdba4cd-addd-30bb-a544-afa0a71707f0 | -1.0755 | -53.45361 | 2024-12-04 05:29:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 27265349-2478-3437-9990-5222bd38bfd8 | -3.82383 | -52.11885 | 2024-12-04 05:29:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| cefedf84-24cc-3b78-9755-06952fbc30b4 | -2.57762 | -53.67922 | 2024-12-04 05:29:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| ff4045dc-4aa3-3cce-aebb-70ae0446d0e4 | -1.74459 | -52.61022 | 2024-12-04 05:29:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 8.5 |
| 81207a7e-661b-39b0-a671-c1266d1ed972 | -2.20587 | -59.82194 | 2024-12-04 05:29:00 | NPP-375D | RIO PRETO DA EVA | AMAZONAS | Brasil | 1303569 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 9f886c43-f4b0-364d-8e22-d61f5d94f5f9 | -3.05965 | -54.50169 | 2024-12-04 05:29:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| fc44efc6-4b84-3dab-95f7-05a8c38ef759 | -1.64802 | -52.04888 | 2024-12-04 05:29:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 39861e8c-86b0-3b23-aba5-938528da3df6 | -1.61486 | -53.53339 | 2024-12-04 05:29:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 31d0fcca-8fbb-3065-8293-fc2df77f30ee | -3.19355 | -50.64688 | 2024-12-04 05:29:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 397d67a4-4cfa-3d20-bf04-8ee40ea44764 | -3.27928 | -50.32609 | 2024-12-04 05:29:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 6ca8214a-b72b-3020-bfe1-0cb62a47d496 | -3.11156 | -54.62247 | 2024-12-04 05:29:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| ce4cd71f-4089-39cd-89b4-363e1c83999d | -3.4057 | -50.23303 | 2024-12-04 05:29:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| aab8996b-58a0-36bf-a424-a2b98c7bb8c3 | -3.13016 | -54.62725 | 2024-12-04 05:29:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 11.7 |
| 5bc5146b-f6b1-31d8-a7e3-950af13d80e5 | -1.08505 | -53.45517 | 2024-12-04 05:29:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 9d515e67-b275-36e6-8ce8-b2fc92217225 | -2.20283 | -47.24405 | 2024-12-04 05:29:00 | NPP-375D | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 008dd688-87a4-3571-bcb1-79a82038472d | -3.12047 | -53.99144 | 2024-12-04 05:29:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 871084e4-ea76-3dcd-9a9e-5c1b98d34a0d | -3.2856 | -53.71092 | 2024-12-04 05:29:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 1fa202bc-4fb2-3b6f-aa6e-62c5434e128d | -3.18549 | -51.16556 | 2024-12-04 05:29:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f21c8c5b-c0cb-3138-a387-2ec3e4a42f3c | -1.7521 | -52.62983 | 2024-12-04 05:29:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 5d949252-6abb-3d77-b7bd-55819a6d55aa | -1.36713 | -53.65516 | 2024-12-04 05:29:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 26b8041a-69ef-30d5-8046-b1d5e197f703 | -2.80022 | -53.05326 | 2024-12-04 05:29:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| aca5ebd4-ae1c-3f91-827a-cd58c0a53466 | -0.8578 | -52.70854 | 2024-12-04 05:29:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 5c17ff00-1230-385e-9df3-105b2b261984 | -1.72682 | -52.60693 | 2024-12-04 05:29:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a4361cf0-a644-346b-9198-4fb2355ffce8 | -3.81251 | -51.65598 | 2024-12-04 05:29:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| fed1d944-d8dc-3b00-8a9f-bb3971d3a249 | -1.67356 | -53.94488 | 2024-12-04 05:29:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 594e73d6-e6bb-322e-88db-a1f8ae8d61b9 | -3.42307 | -53.41889 | 2024-12-04 05:29:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| a3cb822a-a20a-3948-89e3-0bf2c6163300 | -2.79302 | -55.35233 | 2024-12-04 05:29:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| ebf97715-c0ca-39ae-a073-977dbaf6405e | -3.34111 | -49.76994 | 2024-12-04 05:29:00 | NPP-375D | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| e9f1ffb6-b3f6-37ab-9ddd-f741f56dbfe6 | -3.21738 | -53.12606 | 2024-12-04 05:29:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |


[Clique aqui para ver as próximas entradas](README54.md)
