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

## Dados Diários - Página 80

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| fd863c92-d756-38f5-a518-2af669a56d2f | -2.26455 | -53.66515 | 2024-11-02 05:04:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 330245fe-91fd-3d2a-8ae5-0053b9037811 | -2.38914 | -53.84658 | 2024-11-02 05:04:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| b8f26c17-9760-3155-bf04-2dcb020af50d | -2.38581 | -53.84607 | 2024-11-02 05:04:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| a4d2b823-6746-358d-ac4b-f68d76a11b89 | -2.37091 | -53.70348 | 2024-11-02 05:04:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 86523717-5aa3-304e-81e3-efc4a0a9109a | -2.37036 | -53.707 | 2024-11-02 05:04:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| b0682ff7-61d4-3f66-859e-57c6046ea455 | -2.36757 | -53.70296 | 2024-11-02 05:04:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| e37a8d67-3718-3606-999f-7ee88e6b6dec | -2.36702 | -53.70648 | 2024-11-02 05:04:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 4bee5b76-9e68-3d76-ab2b-d2ca11975ae4 | -2.36428 | -53.72409 | 2024-11-02 05:04:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f88dfd29-6daa-3293-add8-b311bd10a220 | -2.36373 | -53.72762 | 2024-11-02 05:04:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 305f4828-023a-3af8-a0b7-e8242db3a881 | -2.36368 | -53.70597 | 2024-11-02 05:04:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 93b8e0e7-32d6-3715-a29e-274ec5200c06 | -2.36318 | -53.73114 | 2024-11-02 05:04:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 4b7228c2-98d3-3db0-8de3-ab9949576306 | -2.36094 | -53.72359 | 2024-11-02 05:04:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 8844ef1b-bb08-36d6-a72e-b024fdd256c6 | -2.36039 | -53.72712 | 2024-11-02 05:04:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 736918b8-87e9-38de-92b1-dce862cf87b4 | -2.35984 | -53.73064 | 2024-11-02 05:04:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 2d36b72d-fc10-35ee-8005-6b85e6e1110a | -2.35814 | -53.71956 | 2024-11-02 05:04:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 164ca761-1138-356d-a085-46812f5830cc | -2.35759 | -53.72309 | 2024-11-02 05:04:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| ce8628ea-8065-31a4-9a43-2de9b3fa3152 | -2.35704 | -53.72662 | 2024-11-02 05:04:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 3305de8b-e15f-3c93-acf9-35268ec75ae4 | -2.32371 | -53.74313 | 2024-11-02 05:04:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| bdc435e2-4583-3924-ba2a-eaf5d14c724b | -2.32317 | -53.74665 | 2024-11-02 05:04:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 380d3da1-3fe2-35f8-8de8-cb87b4f20891 | -2.30337 | -53.8083 | 2024-11-02 05:04:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 25b7f61a-9d0b-3db7-8d9c-68af0078e9ce | -2.30003 | -53.80779 | 2024-11-02 05:04:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| a295933e-c7e9-34dd-8c04-a7a072376b70 | -2.29499 | -53.79625 | 2024-11-02 05:04:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 02844313-7785-3459-bb09-1a6549c1d5a8 | -2.27941 | -53.78667 | 2024-11-02 05:04:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 1c575e5d-edc1-3ec7-8a89-2a0911796aa8 | -2.27607 | -53.78616 | 2024-11-02 05:04:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| b588cf86-3275-3219-8e13-0a3e61dcd71c | -2.27481 | -53.75 | 2024-11-02 05:04:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 51e8f7dd-d4c8-306d-bb17-37f1260c4546 | -2.27427 | -53.75351 | 2024-11-02 05:04:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| d9910c86-8ee0-33c2-9b7d-f60a730173b7 | -2.2731 | -53.73894 | 2024-11-02 05:04:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 028f69e4-a489-35e6-ac51-002c03bfc2a2 | -2.27301 | -53.72057 | 2024-11-02 05:04:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 8832665c-d29b-3465-bdc9-b74bac21ad4d | -2.27256 | -53.74245 | 2024-11-02 05:04:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| c90a010b-92e9-3498-a7f6-42086107a626 | -2.27202 | -53.74597 | 2024-11-02 05:04:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 2af1a97c-9f40-3045-b118-30699e43a216 | -2.27148 | -53.74949 | 2024-11-02 05:04:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| bacdafdd-5d30-300a-ac0b-88b8a99d4427 | -2.27094 | -53.75301 | 2024-11-02 05:04:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| b63b8c67-2a18-3de9-a569-53e9489c0a2d | -2.27081 | -53.73464 | 2024-11-02 05:04:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 442ba3bd-2c81-318a-b589-b1891d84f2eb | -2.27026 | -53.73815 | 2024-11-02 05:04:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 10f3c668-c11e-3b5b-a7d6-bb43c1e7f7f2 | -2.26971 | -53.74167 | 2024-11-02 05:04:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 21.6 |
| eb82126c-bff7-3d2e-ba4b-49bb20d0ceb4 | -2.26916 | -53.74518 | 2024-11-02 05:04:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 21.6 |
| 28ecbebf-59fe-3891-b4c7-3effd879523e | -2.26861 | -53.7487 | 2024-11-02 05:04:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 50f0d5ed-df28-3696-b515-8ed03e24256e | -2.26802 | -53.73061 | 2024-11-02 05:04:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 1ddc5877-ac7b-363b-aa2e-cb99b1fc62c9 | -2.26747 | -53.73413 | 2024-11-02 05:04:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 73504cb4-7dc9-3615-963c-34dd0c442374 | -2.26637 | -53.74115 | 2024-11-02 05:04:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 21.6 |
| c8f5b72c-40b5-31ca-bdfd-4fef6d98a92f | -2.26582 | -53.74467 | 2024-11-02 05:04:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 21.6 |
| cf6fd953-6c61-3f48-9ade-dc68cd1a080f | -2.26523 | -53.72658 | 2024-11-02 05:04:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| eecb584e-6740-3548-95f4-5b2de01b809a | -2.26468 | -53.7301 | 2024-11-02 05:04:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 56029447-1a4c-3644-9f04-49868df0a4a0 | -2.26244 | -53.72256 | 2024-11-02 05:04:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| a582b6d6-5ddd-3fb5-9bd8-0b82afc3ce51 | -2.50863 | -54.10762 | 2024-11-02 05:04:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 70402f07-727a-334f-bbf6-d0a6cb0645bd | -2.50538 | -54.12848 | 2024-11-02 05:04:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 599158bf-285c-3347-8433-90cc380de48e | -2.50484 | -54.13195 | 2024-11-02 05:04:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 63d00923-00ce-3d07-8ed0-1882e93829de | -2.50206 | -54.12796 | 2024-11-02 05:04:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 27556106-fa30-3dd5-a8d5-54efe9743511 | -2.50152 | -54.13144 | 2024-11-02 05:04:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| a30454bc-2f75-320f-b437-912d04f1087c | -2.49045 | -53.98372 | 2024-11-02 05:04:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 7e37e5d5-a1f1-328f-8b42-323d21cdffbb | -2.48991 | -53.98721 | 2024-11-02 05:04:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 3734884d-4f9d-3d12-8dff-31369f76ac10 | -2.48659 | -53.9867 | 2024-11-02 05:04:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 343daaad-2af9-3826-9b12-f06fc9cba9a3 | -2.47715 | -53.98168 | 2024-11-02 05:04:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 15a6a8b4-4a12-3a7b-90c7-2e295d761622 | -2.47526 | -54.0598 | 2024-11-02 05:04:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| ece59234-eac8-3f01-befd-e11449e2d038 | -2.47383 | -53.98118 | 2024-11-02 05:04:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 597109fd-4cee-3468-8a92-65d0e687f5a2 | -2.47194 | -54.05929 | 2024-11-02 05:04:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 10.6 |
| 6db145a4-775e-32c1-bd5b-d90e67fb32e6 | -2.4705 | -53.98067 | 2024-11-02 05:04:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| e67745e6-9a59-36e4-b7c9-36df3b2d5965 | -2.46996 | -53.98415 | 2024-11-02 05:04:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| b9760cb4-8b91-3ca6-b452-163c02d6aeb7 | -2.46907 | -54.03391 | 2024-11-02 05:04:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ac73eb38-0e34-3bbe-aaa8-1c5b4ecfc5e2 | -2.46629 | -54.02992 | 2024-11-02 05:04:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ce04952a-e43a-3df8-ae54-56e3e68c12b5 | -2.46584 | -54.05479 | 2024-11-02 05:04:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 7a45582c-2be0-39d7-b255-c4999b257b69 | -2.46413 | -54.04384 | 2024-11-02 05:04:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| bc33fc3b-0d99-35c0-b658-779d2525ed3a | -2.46359 | -54.04732 | 2024-11-02 05:04:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 775f1371-8f48-3b9d-bee2-b694a5fb63ed | -2.46081 | -54.04332 | 2024-11-02 05:04:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 3521dc86-587e-362c-a4d0-bbb5e0117790 | -2.46027 | -54.04681 | 2024-11-02 05:04:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 3cf70e38-c4e1-3c54-bb5b-16eb658d4d50 | -2.46019 | -54.15701 | 2024-11-02 05:04:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 42fe2e86-2978-3e82-92a4-bc62651dfa22 | -2.45974 | -54.05028 | 2024-11-02 05:04:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 68c2cef1-8f28-34d6-9d62-be72b2d7c5a1 | -2.45966 | -54.16047 | 2024-11-02 05:04:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 05a03c73-735c-33b6-aded-5031575922b7 | -2.45749 | -54.04281 | 2024-11-02 05:04:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f2b14d6c-814b-343f-89f9-62e49138275f | -2.45742 | -54.15303 | 2024-11-02 05:04:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 6ef1159c-8414-31b9-a223-943931d2f300 | -2.45688 | -54.15649 | 2024-11-02 05:04:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| c619aa4d-b526-3c56-89db-bd643df66c8f | -2.45685 | -54.02491 | 2024-11-02 05:04:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f389df94-24ea-3691-bdc9-a07d5ee5af14 | -2.4541 | -54.1525 | 2024-11-02 05:04:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| ec1d2caa-7a8a-394c-9d15-cff28f0916ea | -2.42151 | -53.90171 | 2024-11-02 05:04:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| d2cadc09-e8c3-3b68-8706-2971936a0dc2 | -2.34319 | -53.94678 | 2024-11-02 05:04:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 4168bb4e-9225-3e85-b6c0-42a3e99b3152 | -2.33986 | -53.94627 | 2024-11-02 05:04:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 74f281c0-8eb0-364e-86da-e9ba9f4f1a59 | -2.33871 | -53.93183 | 2024-11-02 05:04:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 8581c5e5-7c26-31e1-8af8-6241f3dbd84e | -2.33817 | -53.93531 | 2024-11-02 05:04:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 899be9f7-8aee-3caa-8786-c4217fe5a11c | -2.33599 | -53.94924 | 2024-11-02 05:04:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 59ccc8c4-47d0-3d4c-bac4-4b0118d7b9b1 | -2.33253 | -53.90589 | 2024-11-02 05:04:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| ed8b111f-96f8-3740-abde-fc4904c3e366 | -2.31929 | -53.92529 | 2024-11-02 05:04:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| f958f62b-bf1a-3ef4-9fd8-8c6ee0a6e981 | -2.31394 | -53.98151 | 2024-11-02 05:04:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 2fa9fd84-4d92-37e2-bd1e-b687f554e950 | -2.6776 | -54.02705 | 2024-11-02 05:04:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 65206b7f-63db-32ed-93b5-594b2a15a8a9 | -2.67428 | -54.02652 | 2024-11-02 05:04:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| cc66f50a-d113-3271-8c4e-9f11d54463b9 | -2.62599 | -54.00875 | 2024-11-02 05:04:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 17c78c63-712c-30f6-ad21-a16f45808f8e | -2.6249 | -54.01575 | 2024-11-02 05:04:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| de2f2b67-2688-30e1-b7b8-5ae4255a5391 | -2.61771 | -54.01823 | 2024-11-02 05:04:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 999838e0-5e47-3f6c-b4d6-05be61f9531a | -2.58779 | -54.01363 | 2024-11-02 05:04:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 9ff9fc7d-15bd-3c8d-beba-a456c6eadf7d | -2.58222 | -54.00563 | 2024-11-02 05:04:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| aa681d7c-9331-3929-baef-a2446faeb4f9 | -2.58168 | -54.00912 | 2024-11-02 05:04:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 7510412c-75c5-34fb-a478-3930d36b011f | -2.5789 | -54.00512 | 2024-11-02 05:04:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f7d6f325-6aa4-34af-86eb-d589906b91fe | -2.5788 | -53.98368 | 2024-11-02 05:04:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 91221e09-cc8b-3739-acd2-17067d549fb8 | -2.57836 | -54.00861 | 2024-11-02 05:04:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 57a5d2de-5198-3bbe-bb8d-564ae6f0b64c | -2.57674 | -54.01907 | 2024-11-02 05:04:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| cb156197-c8a3-3e69-a708-1a2726f04993 | -2.57503 | -54.0081 | 2024-11-02 05:04:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| d8debb38-1480-3486-a97c-6746138a3c8c | -2.57342 | -54.01855 | 2024-11-02 05:04:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| d657e543-a32c-3789-beca-4918939d57a0 | -2.57215 | -53.98265 | 2024-11-02 05:04:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 20ba7cfe-fa4f-3387-b918-3176e0372f27 | -2.56452 | -54.01005 | 2024-11-02 05:04:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| a9b85321-0717-3771-b222-e5e14750c607 | -2.56344 | -54.01702 | 2024-11-02 05:04:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 766460d2-b351-30a0-8eb3-f9edd32f93fb | -2.5612 | -54.00954 | 2024-11-02 05:04:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |


[Clique aqui para ver as próximas entradas](README81.md)
