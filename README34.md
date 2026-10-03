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

## Dados Diários - Página 34

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 1fe84ae5-0c70-37ba-bb60-b7b736aca0fd | -3.13965 | -53.74644 | 2026-10-03 05:16:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 677a087c-7c55-3dc7-92f9-514b2e93c7dc | -3.85237 | -55.97201 | 2026-10-03 05:16:00 | NPP-375D | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 4748a583-1dad-3351-a1e4-c2d904a0040c | -6.0741 | -57.80753 | 2026-10-03 05:16:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 03813b4e-6de6-39e1-a544-2c5a1a270fd9 | -7.46026 | -54.98704 | 2026-10-03 05:16:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 20030425-cf1b-3057-ab60-f3ba474bbf7e | -2.53658 | -54.01089 | 2026-10-03 05:16:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| a9414b45-4122-3354-9dd4-56a3df67d11e | -2.25569 | -51.92737 | 2026-10-03 05:16:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a0e2a6f3-6146-3761-b826-a636d8d17538 | -3.07801 | -54.39923 | 2026-10-03 05:16:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 199dfd7e-508b-39c5-9328-aaacabd965b4 | -3.14188 | -53.73218 | 2026-10-03 05:16:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 4155c8db-cc06-3197-a948-9c77fc1c09ff | -4.78803 | -55.7093 | 2026-10-03 05:16:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 53ec2ece-8e29-3f5a-9a92-c4e7e5e69bfd | -2.92917 | -54.101 | 2026-10-03 05:16:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| eaf0a30f-e04f-36f1-b175-957ee3ced3aa | -3.01897 | -54.19746 | 2026-10-03 05:16:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e8446164-bc9d-39b0-9be8-aed1d2b1039d | -3.13402 | -53.73826 | 2026-10-03 05:16:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| df44ba9e-56ea-34b5-a76b-6c16aba4d111 | -3.86129 | -59.63427 | 2026-10-03 05:16:00 | NPP-375D | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| efc4cf07-cf53-3e68-961b-eb660d69198c | -2.97602 | -53.27449 | 2026-10-03 05:16:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 33e13dde-5063-3205-9087-918534dc8b3c | -2.91355 | -54.09137 | 2026-10-03 05:16:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 8ef3d24f-8d05-324a-8847-8f7add8f32d1 | -2.89685 | -54.1103 | 2026-10-03 05:16:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| ec9017df-7ee8-3e21-aad8-82211ec80b24 | -3.00686 | -53.88238 | 2026-10-03 05:16:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 666fa716-fc81-390f-80d3-0563292aa898 | -3.29711 | -53.8516 | 2026-10-03 05:16:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 73f87fa0-8683-39dc-8be2-ceb8c1cd815e | -4.36002 | -47.7762 | 2026-10-03 05:16:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 17.2 |
| 2186b3bb-1cd7-3b92-a77b-5c0dde86bcc5 | -3.12727 | -53.73721 | 2026-10-03 05:16:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 7.3 |
| a4e92599-0a0a-3b06-9046-7428d4c5501f | -5.13338 | -45.57958 | 2026-10-03 05:16:00 | NPP-375D | ITAIPAVA DO GRAJAÚ | MARANHÃO | Brasil | 2105351 | 21 | 33 | nan | nan | nan | Cerrado | 7.0 |
| ebdb879c-08c6-3697-981d-9b6065801877 | -3.84902 | -55.97148 | 2026-10-03 05:16:00 | NPP-375D | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 2b71ef39-3694-349a-b69d-25ac8547985f | -3.13628 | -53.74591 | 2026-10-03 05:16:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 8b5088cf-3814-37aa-85e8-f9cae2b34113 | -3.07774 | -51.27765 | 2026-10-03 05:16:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| d7a7287b-cc6b-3b9a-a455-c6728be7bdb5 | -4.41043 | -49.96989 | 2026-10-03 05:16:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 98f09caf-f6de-3dba-a01c-e3425e576d44 | -2.258 | -51.936 | 2026-10-03 05:16:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| e110dff3-e4cb-3b40-b068-8fc66c5c3557 | -4.81586 | -46.82225 | 2026-10-03 05:16:00 | NPP-375D | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 0.5 |
| bed2b7f1-860b-3675-a9f7-46356baa69c6 | -3.27971 | -53.83065 | 2026-10-03 05:16:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 7f8de0d2-b934-3553-beda-07b4243e31d9 | -3.11749 | -50.27744 | 2026-10-03 05:16:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 8068bca8-d1f6-3653-bd06-26d571c2a337 | -4.81173 | -46.82188 | 2026-10-03 05:16:00 | NPP-375D | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 0aa73b12-2f6c-3bfb-9917-0826aed3f783 | -2.15009 | -47.75067 | 2026-10-03 05:16:00 | NPP-375D | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| e1b0a1c7-dbd8-35bd-a77a-a96127b06f90 | -4.26736 | -50.75106 | 2026-10-03 05:16:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| a67b6f22-b547-3ae9-aa9a-8ee5f327444c | -6.21238 | -60.01871 | 2026-10-03 05:16:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 12f85ed2-cce8-3f8c-b358-9e08d60ab3ec | -3.18209 | -54.10118 | 2026-10-03 05:16:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 7651cce7-7722-3acb-abee-a1c4573912a9 | -3.24548 | -54.51474 | 2026-10-03 05:16:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| b824767f-a54b-3f32-8f1f-9f097cc0eaa6 | -3.57473 | -51.48454 | 2026-10-03 05:16:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 87c2a883-2df3-3cb0-bab0-bc0663c7fe53 | -3.07907 | -54.37091 | 2026-10-03 05:16:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| c464ee3a-aa99-361c-8ca0-e4456e27ddf4 | -2.91969 | -54.09592 | 2026-10-03 05:16:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| cb71fa1e-ea3e-37de-8e77-9c864181e584 | -2.89077 | -54.14876 | 2026-10-03 05:16:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| c7b48c72-ca11-389d-b2a7-9ac3fb2a63b6 | -5.85533 | -53.47228 | 2026-10-03 05:16:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| bbcf6624-ef66-3627-af6f-2dd08c558c4a | -5.61325 | -44.38121 | 2026-10-03 05:16:00 | NPP-375D | SÃO DOMINGOS DO MARANHÃO | MARANHÃO | Brasil | 2110708 | 21 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 6246837b-a02d-3ea2-9aeb-dd22aed085c3 | -3.10209 | -48.67134 | 2026-10-03 05:16:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 748a110e-57aa-31d3-b24c-867a2be4b5b6 | -3.7108 | -50.65852 | 2026-10-03 05:16:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 23ca2034-ba2d-3d97-814a-164e3fc15323 | -3.17346 | -54.07775 | 2026-10-03 05:16:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 41906d6a-15bf-3fda-9df7-93a9f7435eca | -3.1065 | -50.29652 | 2026-10-03 05:16:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| cecbc4fe-371a-3fca-b245-d4d2524cd5d2 | -2.89848 | -54.07825 | 2026-10-03 05:16:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| c9dc706d-d369-3c55-822d-13b0e5d6fbfd | -5.97099 | -55.37783 | 2026-10-03 05:16:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e5623ffe-3a84-3eea-a0c6-dbcb017aea12 | -2.97522 | -53.26015 | 2026-10-03 05:16:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 9823fa80-35d1-3bde-bf66-5b4ad8c03d45 | -2.99406 | -54.90755 | 2026-10-03 05:16:00 | NPP-375D | BELTERRA | PARÁ | Brasil | 1501451 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| f75749a5-481d-3eaf-8e51-760e5330b9d8 | -1.26343 | -54.55378 | 2026-10-03 05:16:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 6b847a5d-b7d8-340b-b6b9-8a62d8702dc1 | -3.05698 | -54.16376 | 2026-10-03 05:16:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| ce27df66-37f7-3cd0-a6f7-b032b0b6f81b | -5.09118 | -56.25441 | 2026-10-03 05:16:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 764e87c4-fe38-39d7-8f2d-b0c131b80f5b | -3.28813 | -53.84292 | 2026-10-03 05:16:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c32f1582-f778-3e2a-8008-67c97b166c30 | -1.26289 | -54.55724 | 2026-10-03 05:16:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| c691c565-5a7a-35be-bc00-9d72b0f743a8 | -3.17814 | -54.08256 | 2026-10-03 05:16:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 7d8f613f-1785-3bb9-a4f0-091d8d666e4f | -2.89522 | -54.1423 | 2026-10-03 05:16:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c5f62c72-a4d5-3198-b0f4-82c73afcaa49 | -3.21649 | -53.94773 | 2026-10-03 05:16:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 888c34b0-b72b-3a16-aec2-fa400758a1e4 | -5.25168 | -55.92493 | 2026-10-03 05:16:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b6c24f4e-040b-3454-8369-047e1c1cff58 | -2.89353 | -54.13129 | 2026-10-03 05:16:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| af937701-f500-3f62-8e92-b9dc7c988bad | -3.07185 | -54.37333 | 2026-10-03 05:16:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 025e259f-86a0-3268-bd64-83a8760d5142 | -3.22086 | -54.31153 | 2026-10-03 05:16:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 4610b63d-f35b-389c-accd-62509e69f0eb | -3.09751 | -51.09668 | 2026-10-03 05:16:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 27ccb580-8272-3a20-9a28-6cfd4bd67320 | -2.26423 | -54.49569 | 2026-10-03 05:16:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| ecae66e4-e00e-3d62-b7a0-1327ee5bd004 | -1.26899 | -54.56173 | 2026-10-03 05:16:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 32b02b97-6767-32c0-b751-f6dcae605789 | -2.91081 | -54.13041 | 2026-10-03 05:16:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| d2a19b93-d415-3e32-8ec8-138e60e1a3d8 | -3.01022 | -53.88291 | 2026-10-03 05:16:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| dca01ef7-a1fe-318d-808a-8bf185dfc1b0 | -3.8485 | -55.96387 | 2026-10-03 05:16:00 | NPP-375D | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| bf217632-59aa-3fa8-a26a-00fce019947b | -3.18264 | -54.09767 | 2026-10-03 05:16:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 93bf48a2-5735-3e5a-a779-082feb2ad31e | -6.5078 | -41.74373 | 2026-10-03 05:16:00 | NPP-375D | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 2.8 |
| 6e87c762-ed9e-3eed-be6e-2e0f1e302285 | -2.96868 | -54.10356 | 2026-10-03 05:16:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 5aeb61c8-6b91-30db-be93-fd8cdf6f14cc | -6.32259 | -43.34872 | 2026-10-03 05:16:00 | NPP-375D | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| a39ba04d-c0f1-3722-8d68-610b1765b785 | -7.46641 | -54.99164 | 2026-10-03 05:16:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d5badfc5-90aa-33ca-9cea-a1dc62796a35 | -6.24703 | -52.68639 | 2026-10-03 05:16:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 28b49e24-a4c2-3fd1-a514-7d1977852f33 | -3.13121 | -53.73417 | 2026-10-03 05:16:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 7.3 |
| 1c62369e-596a-3043-8440-f2d8e17eefae | -3.6154 | -55.50928 | 2026-10-03 05:16:00 | NPP-375D | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| eb64667f-374f-3b8f-9053-94d203bc76ff | -4.41456 | -49.97049 | 2026-10-03 05:16:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 00a05af2-0a35-3c5a-92c2-b78683c4a260 | -7.46697 | -54.98809 | 2026-10-03 05:16:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| fec4ad04-1f72-3997-a543-3a37b7291397 | -1.76419 | -55.02557 | 2026-10-03 05:16:00 | NPP-375D | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| e14c3c97-cfff-3d47-ab6e-c92c5de9db9a | -3.13176 | -53.73061 | 2026-10-03 05:16:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 10.2 |
| fbf41af0-c618-3f0f-a379-4a4420aa1c91 | -3.02981 | -53.86783 | 2026-10-03 05:16:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ed33f928-3d13-3f6b-921c-44e7c1c42cc6 | -3.64092 | -55.49909 | 2026-10-03 05:16:00 | NPP-375D | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 224f4132-d45c-36dc-adc8-9b86d7d8c314 | -5.73267 | -43.28167 | 2026-10-03 05:16:00 | NPP-375D | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 1b7a0723-c3bc-3049-ad6a-48c89021316b | -3.12502 | -53.72955 | 2026-10-03 05:16:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| e82719f1-69a3-3501-a8c7-371e4d241f1f | -3.72759 | -55.95564 | 2026-10-03 05:16:00 | NPP-375D | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 4a65efaa-05d3-37ce-84c5-c48e87bcff84 | -2.71649 | -54.50299 | 2026-10-03 05:16:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 99cc4e84-8cac-3592-a3fa-2e5ab62ffce3 | -1.27648 | -55.41181 | 2026-10-03 05:16:00 | NPP-375D | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 88f5f1ce-ea54-3c8e-8307-64d351a1ada2 | -1.6107 | -54.75731 | 2026-10-03 05:16:00 | NPP-375D | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 04883c2c-058e-3586-98aa-0b1484ae8235 | -3.24826 | -54.51874 | 2026-10-03 05:16:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| d837a5b5-f4ff-3288-8361-280312f799e1 | -3.13068 | -53.75964 | 2026-10-03 05:16:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 7e13f13d-690a-342b-9b69-6e6a71ea93c6 | -3.28701 | -53.82818 | 2026-10-03 05:16:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 8.1 |
| df0c812b-2d26-3077-8cf4-5ad5fafc2469 | -3.17148 | -54.10315 | 2026-10-03 05:16:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 7666699b-dadc-335e-88d1-bb47a11a2c1e | -3.84955 | -55.80636 | 2026-10-03 05:16:00 | NPP-375D | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c69b1201-0b9f-3b70-86ec-463608ee9e4a | -5.86164 | -53.47727 | 2026-10-03 05:16:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| ad1ebe46-5436-339c-8c61-46fac50abe66 | -3.2842 | -53.84593 | 2026-10-03 05:16:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 6c6e2629-5bb5-3986-beb3-66e289f104c4 | -3.51623 | -54.60318 | 2026-10-03 05:16:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| b79627ce-e6d2-353e-8375-378bf384e488 | -3.32291 | -51.67636 | 2026-10-03 05:16:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 233a1633-ed7c-37cd-b9fc-c6b4ad10b1b6 | -4.78693 | -55.71624 | 2026-10-03 05:16:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 307a4d75-faa6-31d5-a978-c4c60e5daab7 | -2.92024 | -54.09242 | 2026-10-03 05:16:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 5eeba8f3-b341-3231-881e-d8b3a252e5fc | -2.48416 | -56.09363 | 2026-10-03 05:16:00 | NPP-375D | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 7c4eecce-ae38-38bd-8aec-0f022447e191 | -3.13516 | -53.75304 | 2026-10-03 05:16:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |


[Clique aqui para ver as próximas entradas](README35.md)
