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

## Dados Diários - Página 120

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 7a3add63-9f1a-31f3-bee2-cba92d131d6a | -3.65492 | -54.72261 | 2024-11-30 05:27:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 5c5971d0-f35a-3618-a1d9-38551c74d599 | -3.15037 | -53.83963 | 2024-11-30 05:27:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 6.9 |
| a5328883-5ad3-342f-99cf-b119bfa87e6c | -3.92576 | -53.85728 | 2024-11-30 05:27:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| a5ba44a6-8ae8-399b-8d96-5828e290166a | -3.96754 | -48.10025 | 2024-11-30 05:27:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| a6fa0fad-c895-3272-b1ba-167f58b12c90 | -2.30246 | -51.98863 | 2024-11-30 05:27:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 8fa4eec9-c6e5-3408-8faf-6ae5c3e9c2e6 | -4.18331 | -54.76195 | 2024-11-30 05:27:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 8c6203a0-baff-3124-b47d-bb1cf5892874 | -3.59697 | -49.98611 | 2024-11-30 05:27:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 14.3 |
| ca217a61-9b80-3c17-bf21-b642aa0ada52 | -1.28924 | -51.72733 | 2024-11-30 05:27:00 | NOAA-20 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 8b187916-9c43-3d78-b663-ee8c1877fbf7 | -3.82567 | -50.13716 | 2024-11-30 05:27:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 0c3f6a6e-e348-3e51-b0a2-022616d5e74e | -1.20061 | -51.7472 | 2024-11-30 05:27:00 | NOAA-20 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 553f4d96-a2c5-3b2e-a2fd-f87d17873a15 | -1.4767 | -55.38142 | 2024-11-30 05:27:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| c5ea64c0-4df0-39f9-aa15-32f9e287a872 | -4.16657 | -48.6264 | 2024-11-30 05:27:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| c55d200e-5e8c-3f09-be43-9e864e679f3a | -1.32389 | -55.83618 | 2024-11-30 05:27:00 | NOAA-20 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| cdade6a1-641d-38e4-949c-87f54cf31164 | -1.37084 | -55.87955 | 2024-11-30 05:27:00 | NOAA-20 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 170c9d85-9e9a-34cd-a7b4-d1cc6771195d | -1.44999 | -52.61689 | 2024-11-30 05:27:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 81cda1de-892f-31d1-aece-6aff3d16d27c | -3.30243 | -50.37601 | 2024-11-30 05:27:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| b0d3e82d-4a2b-39d6-95f1-bfa8fed6960f | -2.98208 | -53.29336 | 2024-11-30 05:27:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 19664266-c1e9-3758-81dc-d6870a5d5534 | -1.6181 | -52.45807 | 2024-11-30 05:27:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| b0254709-eff4-38d9-935f-21f775d83a0a | -1.99542 | -53.29599 | 2024-11-30 05:27:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| f8edaeab-40e3-3d56-9adf-89a22aa073e7 | -3.98647 | -48.94662 | 2024-11-30 05:27:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| c0f13c12-9e5f-36d6-a3ba-48310b98675e | -3.06949 | -50.331 | 2024-11-30 05:27:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 8.2 |
| 44cb788a-dabf-3f1c-9169-1b2b7e18d8e5 | -2.77102 | -55.34072 | 2024-11-30 05:27:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 277896b6-91a3-33e7-94d2-e5948e02bd77 | -3.30318 | -51.06593 | 2024-11-30 05:27:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 5792457d-74f5-3cac-86eb-34acb627a553 | -1.46261 | -54.50296 | 2024-11-30 05:27:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| ecab4b88-56a2-35ff-b7f0-bb186f90b6a6 | 1.99069 | -60.56476 | 2024-11-30 05:27:00 | NOAA-20 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 2.7 |
| bbb4d31a-9ed7-3911-9505-45bf3b56a003 | 0.88938 | -51.98166 | 2024-11-30 05:27:00 | NOAA-20 | SERRA DO NAVIO | AMAPÁ | Brasil | 1600055 | 16 | 33 | nan | nan | nan | Amazônia | 2.6 |
| c20c81da-7afb-3f87-a043-3ed4f40aa5d1 | -2.88029 | -53.9462 | 2024-11-30 05:27:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 83e8ab2f-20bb-304d-b962-84e1f9f5052e | -2.02932 | -52.08467 | 2024-11-30 05:27:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| a85dacc8-4bb8-3fa7-b9cc-fcf4a79accee | -1.08008 | -53.64122 | 2024-11-30 05:27:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| d278c628-eaa7-3be4-a173-eb033df673dd | 1.20815 | -55.93596 | 2024-11-30 05:27:00 | NOAA-20 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| bf2aadb2-a44f-38b6-9995-2d815712de69 | -2.98774 | -53.35692 | 2024-11-30 05:27:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 77bae90d-7aa6-35d5-9098-d5617c1ec4ec | -3.10563 | -53.81255 | 2024-11-30 05:27:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| d828444f-d92e-3301-b1d4-d967f9017d27 | -2.72162 | -52.9785 | 2024-11-30 05:27:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| e8d60b46-e91d-372c-ba3c-5962a4080e53 | -3.28504 | -50.62114 | 2024-11-30 05:27:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ab0dd3b9-1b54-3d34-a910-c151e848b05d | -3.01855 | -51.3706 | 2024-11-30 05:27:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 20cb8c24-d3b0-319a-b3c4-3ca109d8142b | -1.35803 | -55.64289 | 2024-11-30 05:27:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| e70b6696-dff9-3da3-a8d3-2f62adf390a8 | -2.8902 | -53.32265 | 2024-11-30 05:27:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f4d66882-2966-361c-94ed-45206bb6dce9 | -2.8501 | -54.03539 | 2024-11-30 05:27:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 19add8f8-d385-3b93-a93f-0fe37eec313e | -3.29802 | -53.83492 | 2024-11-30 05:27:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| d5cb734f-5986-3bb4-a4eb-e204dc6edd02 | -2.65801 | -48.78938 | 2024-11-30 05:27:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 937320b5-f870-3c5f-b6b9-961753dc6420 | -1.70932 | -52.63189 | 2024-11-30 05:27:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 7d818997-206d-3f26-b8a4-6bb99af26ae2 | -2.89647 | -51.57676 | 2024-11-30 05:27:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| f2f68612-ca43-3bd5-8bb9-28f3b321b584 | -3.08528 | -49.21348 | 2024-11-30 05:27:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 3fd81786-779a-3761-9a15-0310b32124fd | -3.5176 | -62.8469 | 2024-11-30 05:27:00 | NOAA-20 | CODAJÁS | AMAZONAS | Brasil | 1301308 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| efc54acd-f15a-312f-bcbd-5fd27241fbe7 | -1.30109 | -55.74147 | 2024-11-30 05:27:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 9dd5e0ba-b9ab-3321-9fcd-019cd1e91545 | -1.35292 | -54.62902 | 2024-11-30 05:27:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 3d7bde32-3036-31b5-b898-d6f81e65da24 | -2.95914 | -50.57963 | 2024-11-30 05:27:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 6af1e490-5ff4-38ac-95fe-906aec4c4025 | 1.21202 | -55.93535 | 2024-11-30 05:27:00 | NOAA-20 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 18517555-6664-3250-98af-8de0c676fa02 | -2.86014 | -54.00163 | 2024-11-30 05:27:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 69e1ade2-6e1b-3992-b7a8-a70b9f895c40 | -3.49052 | -53.82276 | 2024-11-30 05:27:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| a637da4b-6c25-3da8-a3ac-9f06f9ecb28b | -3.03534 | -51.78174 | 2024-11-30 05:27:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 1f74eb66-0fcd-30d8-a45c-dbdcf50bbe11 | -2.29565 | -51.98497 | 2024-11-30 05:27:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| cb9ae196-c7c3-363e-b095-92fbe337bc15 | 0.09395 | -51.17245 | 2024-11-30 05:27:00 | NOAA-20 | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 8450f0ce-fd4a-370b-9924-887f40e7adf7 | -3.10555 | -53.81017 | 2024-11-30 05:27:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 6d0ea3e9-370e-37a8-9531-f0ca02e1defb | -3.38032 | -50.70013 | 2024-11-30 05:27:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| c904ef5c-b78f-365d-9c44-f0049c7ca4be | -3.98728 | -48.94103 | 2024-11-30 05:27:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b7287fa7-91fe-37d0-a838-c731c6be65b9 | -3.75896 | -49.94064 | 2024-11-30 05:27:00 | NOAA-20 | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 328d15a0-7c6c-3619-81e4-89de444216c1 | -2.15691 | -56.02348 | 2024-11-30 05:27:00 | NOAA-20 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| a0a63f2d-dc15-32e0-8a27-9fad85bedb23 | -0.87767 | -51.71839 | 2024-11-30 05:27:00 | NOAA-20 | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e0bc5358-baba-345f-ad55-73056e5f7f4a | -2.23323 | -53.62264 | 2024-11-30 05:27:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 3c466c35-1c8d-37ef-8d41-7993411bed6c | -1.65251 | -52.73405 | 2024-11-30 05:27:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| c45a52e0-7946-35d3-897b-06c601b0f98b | -1.2573 | -54.54811 | 2024-11-30 05:27:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 57e0b4a3-8cbc-355e-894f-72f7f72091d3 | -3.24904 | -54.21426 | 2024-11-30 05:27:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 2a75bff3-837b-3490-b8e1-c818bc1308f9 | -2.01017 | -53.04105 | 2024-11-30 05:27:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| f80a8698-221b-328c-ba6f-65e8e412a671 | -3.09776 | -54.02901 | 2024-11-30 05:27:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 02e55591-e9e2-385d-8f36-5304de337cd2 | -1.14892 | -51.69114 | 2024-11-30 05:27:00 | NOAA-20 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 8e961833-1531-37c2-82a2-acc3b183558f | -3.49626 | -53.84959 | 2024-11-30 05:27:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e3569cb7-ee87-352f-9aa4-8bca9abbfbfc | -3.15263 | -53.82459 | 2024-11-30 05:27:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 3b2dc2f9-d445-33ac-8136-5202958de6d5 | -1.09283 | -53.39352 | 2024-11-30 05:27:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 1d4c0a48-74b2-3b59-9cd3-8852d67bf8de | -2.4133 | -56.44241 | 2024-11-30 05:27:00 | NOAA-20 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| b1c85330-0a5c-302f-9791-fc5895b52bc8 | -3.23972 | -53.92832 | 2024-11-30 05:27:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 6.4 |
| 1dab46e3-de4c-3854-b5a0-4761ab510984 | -3.9552 | -50.19558 | 2024-11-30 05:27:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| d656f2c1-11a9-3986-be68-28ddebc2490e | -1.32629 | -55.84738 | 2024-11-30 05:27:00 | NOAA-20 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 73f343ff-9ef4-3d81-83f9-3e60a3c4a280 | -2.83279 | -54.10548 | 2024-11-30 05:27:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| a8c6ccf4-a6e4-30a2-926f-5e131e9552dc | -2.61317 | -51.81203 | 2024-11-30 05:27:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 3adc2fd5-065a-3e52-8eac-db40170c60e9 | -1.71946 | -52.63342 | 2024-11-30 05:27:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| ad1f7333-1f24-3e55-bbc1-0c73306c308e | -2.60827 | -51.80771 | 2024-11-30 05:27:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| fda64e81-7cb3-332c-b7b3-56a34396c033 | 0.99309 | -50.2701 | 2024-11-30 05:27:00 | NOAA-20 | CUTIAS | AMAPÁ | Brasil | 1600212 | 16 | 33 | nan | nan | nan | Amazônia | 1.5 |
| ec47ca54-d05c-3e31-b15f-8ed03f850367 | -2.30099 | -51.98581 | 2024-11-30 05:27:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 27d8b7de-985e-313c-be94-73cd0126e7ec | -2.29229 | -51.98365 | 2024-11-30 05:27:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 45be0c83-8418-3679-9780-3c7655466411 | -3.46616 | -50.53103 | 2024-11-30 05:27:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 6c131eab-316f-3d0a-97bb-aba553faf4dd | -3.54338 | -50.18243 | 2024-11-30 05:27:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 3a622632-13c7-360e-ab65-4e17728acc98 | -3.26955 | -50.21259 | 2024-11-30 05:27:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 405ee86e-2d72-38bb-aff3-45b1b776d58c | -1.21165 | -54.196 | 2024-11-30 05:27:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 0bf4c8fd-83e9-3538-846e-0a44ae2cbee5 | -1.59445 | -52.28982 | 2024-11-30 05:27:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| d7f6d62a-66b7-30fe-b6bf-4efbcc28ea20 | -1.2572 | -54.54921 | 2024-11-30 05:27:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| d55a44a7-d57d-3349-9a4b-a4095f0e6c64 | 0.62801 | -59.57145 | 2024-11-30 05:27:00 | NOAA-20 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 922c0401-502d-3c44-a343-7162b8e555b9 | -1.14781 | -53.66766 | 2024-11-30 05:27:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 1f79eb30-0d03-3d49-a096-58b0c42c0b6b | -3.76059 | -49.94397 | 2024-11-30 05:27:00 | NOAA-20 | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 9941f363-f6f7-356c-bec7-e54004d10342 | -1.65526 | -54.23841 | 2024-11-30 05:27:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 7bec5e3b-37d2-3e8c-9f57-6dbdfdcca458 | -1.89615 | -53.01576 | 2024-11-30 05:27:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| cf48ee47-5856-3042-a305-fa322f527b10 | -1.78397 | -52.74683 | 2024-11-30 05:27:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| f342df0e-816e-37c5-9c6d-b8d3d3b0f038 | -3.7924 | -58.97202 | 2024-11-30 05:27:00 | NOAA-20 | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 807eeeb5-5714-3496-a137-c2c07ea6e52f | -1.60027 | -55.5583 | 2024-11-30 05:27:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 8c3e77e5-a0f5-3469-9f22-814302b4bdda | -1.89213 | -54.54941 | 2024-11-30 05:27:00 | NOAA-20 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| feaac638-4f21-32b5-908c-fabdb507a2c9 | -2.80868 | -53.04756 | 2024-11-30 05:27:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| c74ae512-f57e-34cb-89b3-71f0bed64be5 | 0.94033 | -50.73975 | 2024-11-30 05:27:00 | NOAA-20 | CUTIAS | AMAPÁ | Brasil | 1600212 | 16 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 7f5dcb96-f72a-31f8-922a-6b5c01309aa8 | -4.07699 | -54.56253 | 2024-11-30 05:27:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 36c18071-935d-3986-ac62-7fb47366737f | 0.88988 | -51.98477 | 2024-11-30 05:27:00 | NOAA-20 | SERRA DO NAVIO | AMAPÁ | Brasil | 1600055 | 16 | 33 | nan | nan | nan | Amazônia | 2.6 |
| a42a795a-a240-3c93-9516-11993e5ad448 | -2.79909 | -53.04314 | 2024-11-30 05:27:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |


[Clique aqui para ver as próximas entradas](README121.md)
