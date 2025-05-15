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

## Dados Diários - Página 2

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 78fa4a06-4d70-3a30-ab2b-61b4bccfa7da | -13.9713 | -56.7874 | 2025-05-15 01:10:00 | GOES-19 | DIAMANTINO | MATO GROSSO | Brasil | 5103502 | 51 | 33 | nan | nan | nan | Cerrado | 72.0 |
| b915377c-a388-387d-a507-f5d560515d23 | -13.2967 | -45.4299 | 2025-05-15 01:10:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 96.9 |
| 653b91ec-5fc2-3b4f-b3cc-cb82a69174a4 | -13.2585 | -45.4131 | 2025-05-15 01:10:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 73.3 |
| 7da63e22-cb13-32a7-9c4f-fb55fa33e1b9 | -13.2774 | -45.4331 | 2025-05-15 01:10:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 179.3 |
| b08811a0-a616-3e54-8cb2-f81ca73170c3 | -13.2778 | -45.4099 | 2025-05-15 01:10:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 243.6 |
| f3f88127-1011-31d6-8afe-f613da3ba4e0 | -13.2972 | -45.4067 | 2025-05-15 01:10:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 109.1 |
| e123bbdd-7485-39c7-b2f3-0666343ce35f | -9.4769 | -40.3365 | 2025-05-15 01:10:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 66.9 |
| 6692a71a-bf1c-3be0-b19c-f4be5a269909 | -9.4773 | -40.3116 | 2025-05-15 01:10:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 72.1 |
| b1e8c047-7c15-3441-8ebd-445df4913a7f | -13.9697 | -56.783798 | 2025-05-15 01:12:00 | METOP-B | DIAMANTINO | MATO GROSSO | Brasil | 5103502 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 1d6064e7-bde9-3660-b5c9-50610ffb1ce5 | -13.044 | -53.7188 | 2025-05-15 01:12:00 | METOP-B | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| e331d79b-e51e-3162-8c26-511bc6b8ec62 | -13.6742 | -53.9226 | 2025-05-15 01:12:00 | METOP-B | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 01aefa2e-b4de-3540-9395-d8a437bb1962 | -19.067301 | -53.449799 | 2025-05-15 01:12:00 | METOP-B | CAMAPUÃ | MATO GROSSO DO SUL | Brasil | 5002605 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| bb3d208f-edfb-37a3-8d25-ce618b0c1359 | -13.962 | -56.7953 | 2025-05-15 01:12:00 | METOP-B | DIAMANTINO | MATO GROSSO | Brasil | 5103502 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| f215711c-34bd-3801-a956-d9e9bb400e3d | -13.9718 | -56.7929 | 2025-05-15 01:12:00 | METOP-B | DIAMANTINO | MATO GROSSO | Brasil | 5103502 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 3b757899-8f2b-3701-beaa-920ef6b2b5e7 | -13.0405 | -53.704601 | 2025-05-15 01:12:00 | METOP-B | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 6c9de92e-0d36-3ad9-b732-4c5c643085a7 | -13.9675 | -56.774799 | 2025-05-15 01:12:00 | METOP-B | DIAMANTINO | MATO GROSSO | Brasil | 5103502 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| b593c69d-df2a-396c-8590-df4be0b60a82 | -13.9599 | -56.786301 | 2025-05-15 01:12:00 | METOP-B | DIAMANTINO | MATO GROSSO | Brasil | 5103502 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| be55e2b7-3945-3987-9758-b494105aca66 | -13.0537 | -53.716301 | 2025-05-15 01:12:00 | METOP-B | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 820db287-1655-365a-9f31-d818f72584f8 | -13.9521 | -56.7893 | 2025-05-15 01:20:00 | GOES-19 | DIAMANTINO | MATO GROSSO | Brasil | 5103502 | 51 | 33 | nan | nan | nan | Cerrado | 57.5 |
| 685c48e1-8b89-3b8e-acf4-f40574951d7f | -9.4964 | -40.3088 | 2025-05-15 01:20:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 72.5 |
| 2a706458-6e07-36ef-a347-90a73830958d | -13.2774 | -45.4331 | 2025-05-15 01:20:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 200.1 |
| c04879be-0b18-3429-a228-e254f0202fa5 | -13.2972 | -45.4067 | 2025-05-15 01:20:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 61.6 |
| 6142996c-65ab-318a-bddf-47f013dbcfdb | -13.2778 | -45.4099 | 2025-05-15 01:20:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 248.7 |
| 623657ce-b425-30e2-89d2-464dc49a6337 | -9.4773 | -40.3116 | 2025-05-15 01:20:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 237.9 |
| aec8aeda-44d8-3f08-8197-20d6c3bf6f37 | -9.4769 | -40.3365 | 2025-05-15 01:20:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 127.8 |
| af257d0b-3ba9-370a-a5c4-fcdbe3c8095b | -13.2967 | -45.4299 | 2025-05-15 01:20:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 87.8 |
| db546969-7271-3091-9a4b-da0767380798 | -13.2778 | -45.4099 | 2025-05-15 01:30:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 198.0 |
| 6be16256-46af-323b-8202-4f1e01e1d6c9 | -9.4773 | -40.3116 | 2025-05-15 01:30:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 281.7 |
| 0c03c2c4-ec23-330e-94bb-071400eed9ef | -13.2585 | -45.4131 | 2025-05-15 01:30:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 43.4 |
| c335e2ba-de92-3433-b430-42a7d031d4ae | -13.9521 | -56.7893 | 2025-05-15 01:30:00 | GOES-19 | DIAMANTINO | MATO GROSSO | Brasil | 5103502 | 51 | 33 | nan | nan | nan | Cerrado | 56.0 |
| 2614d4bb-fd97-3dee-b8c8-cd18c1d3faaf | -13.2774 | -45.4331 | 2025-05-15 01:30:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 172.9 |
| c8fd6738-9beb-3eed-abd0-c16dba90d0e2 | -9.4769 | -40.3365 | 2025-05-15 01:30:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 105.0 |
| 490e64bc-b4b2-3c95-a66b-3517f7fadeec | -13.2967 | -45.4299 | 2025-05-15 01:30:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 67.9 |
| 0d0b4e7a-3951-3a2c-8868-aeec4e4b895a | -13.2972 | -45.4067 | 2025-05-15 01:30:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 49.2 |
| 756efcbe-3552-31bb-8bff-9ee3a787e5b9 | -13.04385 | -53.70825 | 2025-05-15 01:32:00 | TERRA_M-M | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 24.8 |
| d7844db6-f8fe-3b90-aeef-4fa43c1d2fdc | -13.04721 | -53.72874 | 2025-05-15 01:32:00 | TERRA_M-M | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 37.2 |
| 289459a9-4a3d-38fa-b84f-95300e8182d7 | -13.67497 | -53.93991 | 2025-05-15 01:32:00 | TERRA_M-M | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Cerrado | 21.5 |
| aa954ba2-8f43-3fdf-a5c0-64824c1dec46 | -19.06461 | -53.45793 | 2025-05-15 01:32:00 | TERRA_M-M | CAMAPUÃ | MATO GROSSO DO SUL | Brasil | 5002605 | 50 | 33 | nan | nan | nan | Cerrado | 14.7 |
| a19c8296-e7a1-39bc-8332-2fc0f354641a | -13.97057 | -56.79258 | 2025-05-15 01:32:00 | TERRA_M-M | DIAMANTINO | MATO GROSSO | Brasil | 5103502 | 51 | 33 | nan | nan | nan | Cerrado | 16.9 |
| 497bbc4e-e9a0-37c9-86f5-d7ed920649a2 | -13.95873 | -56.78217 | 2025-05-15 01:32:00 | TERRA_M-M | DIAMANTINO | MATO GROSSO | Brasil | 5103502 | 51 | 33 | nan | nan | nan | Cerrado | 34.2 |
| 0786c0eb-ff83-3df3-bc9e-1349c5daa6b0 | -13.04586 | -53.72314 | 2025-05-15 01:32:00 | TERRA_M-M | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 54.3 |
| a06e0a36-4178-3a8a-a0c0-214a092d57e5 | -13.96056 | -56.79409 | 2025-05-15 01:32:00 | TERRA_M-M | DIAMANTINO | MATO GROSSO | Brasil | 5103502 | 51 | 33 | nan | nan | nan | Cerrado | 62.3 |
| 3b8d08da-d3ef-3e7e-90e0-7936df9a48d2 | -11.42229 | -54.32801 | 2025-05-15 01:34:00 | TERRA_M-M | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 15.7 |
| b182cc81-a15c-34b7-b602-eb0c363be831 | -11.65262 | -58.26531 | 2025-05-15 01:34:00 | TERRA_M-M | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 9.7 |
| 1269a9d6-6ed3-35b7-89ef-4cf8ab1c7925 | -11.42183 | -54.3346 | 2025-05-15 01:34:00 | TERRA_M-M | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 22.4 |
| 7d120c1e-cee4-3aab-80b3-3a210910ec94 | -13.2778 | -45.4099 | 2025-05-15 01:40:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 170.0 |
| bed34c53-7b18-3667-a3f4-9e06bca0e79f | -6.1791 | -48.0712 | 2025-05-15 01:40:00 | GOES-19 | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 75.2 |
| cf316477-d43e-379f-b490-d7afe58ce65c | -9.4769 | -40.3365 | 2025-05-15 01:40:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 67.9 |
| 63cb9643-845c-3fe4-9e78-0868677ba987 | -13.2972 | -45.4067 | 2025-05-15 01:40:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 49.5 |
| 274ded98-d6fa-3b06-b87c-838356cb4b0b | -13.2774 | -45.4331 | 2025-05-15 01:40:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 151.1 |
| cf14fb27-a303-3e52-9b87-de80621cd982 | -13.2967 | -45.4299 | 2025-05-15 01:40:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 81.2 |
| 7f24a87d-e372-3084-8744-6f5e8b02e7ad | -19.166 | -47.8122 | 2025-05-15 01:40:00 | GOES-19 | NOVA PONTE | MINAS GERAIS | Brasil | 3145000 | 31 | 33 | nan | nan | nan | Cerrado | 58.9 |
| 62efb379-602c-303c-b804-8517ebe789f9 | -13.9521 | -56.7893 | 2025-05-15 01:40:00 | GOES-19 | DIAMANTINO | MATO GROSSO | Brasil | 5103502 | 51 | 33 | nan | nan | nan | Cerrado | 53.7 |
| e1ecf73d-5d4e-380a-a2c1-5558ee51daad | -9.4773 | -40.3116 | 2025-05-15 01:40:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 146.0 |
| 7f747db2-f19e-37f2-9cbc-8126a4ac4e98 | -9.4964 | -40.3088 | 2025-05-15 01:50:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 60.7 |
| 0b618730-5da8-3ec1-9d06-83979e71ab25 | -9.4773 | -40.3116 | 2025-05-15 01:50:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 178.6 |
| fccdcf52-6bdc-3b2f-a30b-8401c8fd8fc0 | -13.2778 | -45.4099 | 2025-05-15 01:50:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 156.8 |
| e7835f7c-8b43-34d9-bc56-9a6845c1fab0 | -9.4769 | -40.3365 | 2025-05-15 01:50:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 57.2 |
| b8e73035-4110-34c2-8508-e0a5a0858d7d | -13.2774 | -45.4331 | 2025-05-15 01:50:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 133.7 |
| 5162a396-2769-3812-a9ce-6fa56df14aca | -19.166 | -47.8122 | 2025-05-15 01:50:00 | GOES-19 | NOVA PONTE | MINAS GERAIS | Brasil | 3145000 | 31 | 33 | nan | nan | nan | Cerrado | 50.6 |
| 0c80ccfc-f4e9-3fed-a8ef-d48248a80278 | -13.2967 | -45.4299 | 2025-05-15 01:50:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 50.9 |
| a76e194d-a2d3-39d9-a99d-3558f5723032 | -9.4773 | -40.3116 | 2025-05-15 02:00:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 135.6 |
| f543a0dd-ab51-3306-88dd-14c9894ea129 | -13.2778 | -45.4099 | 2025-05-15 02:00:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 126.9 |
| a7043f61-ed34-3869-97cd-ea06117bbc6b | -19.166 | -47.8122 | 2025-05-15 02:00:00 | GOES-19 | NOVA PONTE | MINAS GERAIS | Brasil | 3145000 | 31 | 33 | nan | nan | nan | Cerrado | 55.9 |
| 3b231d1f-a9c2-3492-8173-460875edde66 | -13.2967 | -45.4299 | 2025-05-15 02:00:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 55.5 |
| 383fff8c-db73-33ce-96f1-70e4d43a93d5 | -13.2774 | -45.4331 | 2025-05-15 02:00:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 109.6 |
| 59cf3b42-58c9-3b75-b439-0fd08316c624 | -13.9467 | -56.803299 | 2025-05-15 02:03:00 | METOP-C | DIAMANTINO | MATO GROSSO | Brasil | 5103502 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| a8a25c17-36db-3098-b9b4-12db4584c306 | -13.9372 | -56.806198 | 2025-05-15 02:03:00 | METOP-C | DIAMANTINO | MATO GROSSO | Brasil | 5103502 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 33011be3-5481-39d5-84f0-0e087fc3e88d | -13.2778 | -45.4099 | 2025-05-15 02:10:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 70.4 |
| b55a4482-1c57-315c-bfc0-08c6325a04cd | -9.4769 | -40.3365 | 2025-05-15 02:10:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 54.2 |
| eb47813d-fa00-316b-887b-eca44b7cbef3 | -13.2774 | -45.4331 | 2025-05-15 02:10:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 62.5 |
| 0040bfcf-f3da-3775-bbf2-bf11aa93e30b | -9.4773 | -40.3116 | 2025-05-15 02:10:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 102.3 |
| e245f233-0522-37b7-852f-ce054c5f71c0 | -19.166 | -47.8122 | 2025-05-15 02:10:00 | GOES-19 | NOVA PONTE | MINAS GERAIS | Brasil | 3145000 | 31 | 33 | nan | nan | nan | Cerrado | 49.8 |
| 01c1e383-2ea0-3c3c-beb8-dc90e8e9609e | -13.2774 | -45.4331 | 2025-05-15 02:20:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 67.0 |
| be642a4f-3639-3643-af49-c4c2de480a72 | -13.2778 | -45.4099 | 2025-05-15 02:20:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 79.8 |
| 8683e296-cf04-39ea-b809-819b20e7bceb | -9.4773 | -40.3116 | 2025-05-15 02:20:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 107.7 |
| d795b5f4-8d9a-3ae3-9fca-499e651ecc2f | -13.2778 | -45.4099 | 2025-05-15 02:30:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 70.8 |
| 94afb2cb-c78b-331d-80df-f31a1587d7fe | -13.2774 | -45.4331 | 2025-05-15 02:30:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 69.0 |
| bdef005d-71a7-3b49-b4c6-c2c99e231ee2 | -9.4773 | -40.3116 | 2025-05-15 02:30:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 62.3 |
| 7e632203-e299-3d52-9cef-6539c51a39d6 | -13.9713 | -56.7874 | 2025-05-15 02:30:00 | GOES-19 | DIAMANTINO | MATO GROSSO | Brasil | 5103502 | 51 | 33 | nan | nan | nan | Cerrado | 58.8 |
| 0442d00f-081a-3c25-8d13-5e217b6e4575 | -6.1791 | -48.0712 | 2025-05-15 02:30:00 | GOES-19 | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 60.4 |
| b5ffd54d-0f5a-3fd6-921c-3176c40cb98d | -13.2778 | -45.4099 | 2025-05-15 02:40:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 55.1 |
| c957c7ee-3431-3e2e-b02a-142eda09d259 | -13.9713 | -56.7874 | 2025-05-15 02:40:00 | GOES-19 | DIAMANTINO | MATO GROSSO | Brasil | 5103502 | 51 | 33 | nan | nan | nan | Cerrado | 52.7 |
| b361bee1-e472-323c-a3ff-114059a4fa05 | -13.2774 | -45.4331 | 2025-05-15 02:40:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 60.1 |
| dd44f3a4-0130-3f97-9e9c-9ca5cd390566 | -13.2778 | -45.4099 | 2025-05-15 02:50:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 52.0 |
| 59d5e64f-1b22-3f5c-8afc-21a2d56f25a2 | -22.2581 | -50.3621 | 2025-05-15 02:50:00 | GOES-19 | LUTÉCIA | SÃO PAULO | Brasil | 3527900 | 35 | 33 | nan | nan | nan | Mata Atlântica | 53.0 |
| 9e4d5840-6cfd-3665-aeb4-85a21e3c9b74 | -6.6503 | -41.9853 | 2025-05-15 02:50:00 | GOES-19 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 70.2 |
| d5675e55-7226-3541-b332-210b079a784e | -13.2774 | -45.4331 | 2025-05-15 02:50:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 50.3 |
| 7ac00e58-3e79-3a2f-a5a9-4e1a1b5eb203 | -13.9713 | -56.7874 | 2025-05-15 02:50:00 | GOES-19 | DIAMANTINO | MATO GROSSO | Brasil | 5103502 | 51 | 33 | nan | nan | nan | Cerrado | 52.0 |
| 595ffb34-ec17-3b27-9dc4-f6e3c148b6b8 | -6.1791 | -48.0712 | 2025-05-15 03:00:00 | GOES-19 | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 75.3 |
| 927f73b6-704f-3f9e-8335-687aafb8f37a | -13.9713 | -56.7874 | 2025-05-15 03:00:00 | GOES-19 | DIAMANTINO | MATO GROSSO | Brasil | 5103502 | 51 | 33 | nan | nan | nan | Cerrado | 51.9 |
| 231a25a6-137b-37ea-b0ac-684d8c6a7362 | -13.2778 | -45.4099 | 2025-05-15 03:00:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 49.6 |
| ca9c5444-70e1-3894-9192-f3b56192fa8a | -6.6503 | -41.9853 | 2025-05-15 03:00:00 | GOES-19 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 65.4 |
| d491e863-5343-345a-9c7c-d16f4211b883 | -6.6503 | -41.9853 | 2025-05-15 03:10:00 | GOES-19 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 65.2 |
| 5ff52219-402a-3d59-afc6-a114ddb90cc9 | -13.9713 | -56.7874 | 2025-05-15 03:10:00 | GOES-19 | DIAMANTINO | MATO GROSSO | Brasil | 5103502 | 51 | 33 | nan | nan | nan | Cerrado | 43.1 |
| f2d83206-587a-36e6-ad20-80a6b67413fa | -9.87823 | -36.84359 | 2025-05-15 03:13:00 | NPP-375D | GIRAU DO PONCIANO | ALAGOAS | Brasil | 2702900 | 27 | 33 | nan | nan | nan | Caatinga | 1.2 |
| dea815ff-4b8e-314e-8f78-c9ac82f5a83e | -9.4727 | -40.3138 | 2025-05-15 03:13:00 | NPP-375D | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 11bf6284-16b8-381b-9dfb-408be645f891 | -8.86254 | -37.78656 | 2025-05-15 03:13:00 | NPP-375D | MATA GRANDE | ALAGOAS | Brasil | 2705002 | 27 | 33 | nan | nan | nan | Caatinga | 0.8 |
| bc14a5e4-cc8f-3ba7-8133-a8e608e8cba5 | -9.47864 | -40.31964 | 2025-05-15 03:13:00 | NPP-375D | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 14e35b56-6d10-3fe0-9e36-85a2900d4c02 | -9.26075 | -40.23678 | 2025-05-15 03:13:00 | NPP-375D | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 1.7 |


[Clique aqui para ver as próximas entradas](README3.md)
