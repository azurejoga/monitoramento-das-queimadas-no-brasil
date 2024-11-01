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

## Dados Diários - Página 47

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| c33b078b-75bf-340d-8f8e-bede4ea56c78 | -3.27325 | -53.3335 | 2024-11-01 05:23:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 1f6f255c-b783-3510-b4bd-09542bf6b986 | -3.27262 | -53.33784 | 2024-11-01 05:23:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 6e203b39-eb60-3a84-a460-9bceb5dd15a9 | -3.2544 | -53.0713 | 2024-11-01 05:23:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 9.0 |
| 73b22769-f529-33ac-99d4-975d5910edf6 | -3.25372 | -53.07583 | 2024-11-01 05:23:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 6499788d-4e41-37fe-8707-e53df11701e8 | -3.25098 | -53.33627 | 2024-11-01 05:23:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ca9bd580-6780-3eb6-adc7-617844c915e0 | -3.25032 | -53.34058 | 2024-11-01 05:23:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| ca81a0ca-8c0a-3a27-b40e-8dcc9222ebbb | -3.24976 | -53.33895 | 2024-11-01 05:23:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 4da7bb34-8d68-399c-9469-336aa4dcf9be | -3.24653 | -53.33562 | 2024-11-01 05:23:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 8f7eb4d2-1b5d-39de-a040-a2a58dd11be7 | -3.2375 | -53.36518 | 2024-11-01 05:23:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 20.5 |
| db20269a-3d0f-38b8-b322-64198e3e819d | -3.23735 | -53.27622 | 2024-11-01 05:23:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 0ab9a49e-f66a-3ee9-81dd-5ecf7bcb5a28 | -3.23684 | -53.36951 | 2024-11-01 05:23:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 20.5 |
| 2a326cd8-99fe-3677-bc8f-33f6d1a39899 | -3.21392 | -53.40138 | 2024-11-01 05:23:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| afd48f3e-b86e-37e3-aecb-415ecb5ec8de | -3.21325 | -53.4058 | 2024-11-01 05:23:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a7470866-b97c-3102-93e5-0250720639fa | -3.20949 | -53.40078 | 2024-11-01 05:23:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 25368353-f355-3987-89d4-a0f75bf35947 | -3.20883 | -53.40516 | 2024-11-01 05:23:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 9afab5ec-2836-3b95-9c5d-a7695888e825 | -3.06024 | -53.25103 | 2024-11-01 05:23:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ec72ed22-f63d-3aed-8e4a-3931dcb5b174 | -3.00963 | -53.44081 | 2024-11-01 05:23:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 6f87e530-0f3b-340d-b089-c6535552c114 | -2.877 | -52.89322 | 2024-11-01 05:23:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 5ff62c41-04f2-3572-b691-68f8d69f01ab | -2.87628 | -52.89791 | 2024-11-01 05:23:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 85ea9320-5ae2-311e-b278-a6f23a939ea2 | -2.87316 | -52.88783 | 2024-11-01 05:23:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 29df4a78-93ef-3cd5-9140-37869be11a48 | -2.87245 | -52.89249 | 2024-11-01 05:23:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 4a4998ae-388e-352e-94ed-47b6426f7928 | -2.85321 | -53.34382 | 2024-11-01 05:23:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 0c943369-6d32-34c8-8892-7ccbfaac864e | -2.67617 | -53.01851 | 2024-11-01 05:23:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 3b3d6f56-5671-3064-8071-1b569d4057ac | -2.18738 | -53.7202 | 2024-11-01 05:23:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| b24d1def-040b-309b-839e-ee99df9b1000 | -2.18677 | -53.72419 | 2024-11-01 05:23:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 85d75e40-7e03-36cf-ad17-4cfed2714207 | -2.16301 | -53.67974 | 2024-11-01 05:23:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 632162aa-0237-31e1-a5bb-1345610d6c1c | -2.15995 | -53.6711 | 2024-11-01 05:23:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 19d7a1bc-dcb7-3f2a-85f4-f9fcfdd885be | -1.5127 | -54.45055 | 2024-11-01 05:23:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 0948768f-4a44-3052-8a89-46a3c6ee1024 | -1.51216 | -54.4541 | 2024-11-01 05:23:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 9be76f96-26f2-39c7-bbbd-554535306fbb | -1.47076 | -54.23402 | 2024-11-01 05:23:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| c3439c16-ad62-3584-a408-583ae783c211 | -1.40835 | -54.20669 | 2024-11-01 05:23:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 978ebd80-1887-3612-8b4c-3cd1ede78be9 | -1.3412 | -54.6518 | 2024-11-01 05:23:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 023c188c-6956-388d-a8b9-4c22cd156bac | -1.17063 | -53.68459 | 2024-11-01 05:23:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| dba2e775-7a26-3914-a1a5-010e30dee1af | -1.14785 | -53.38129 | 2024-11-01 05:23:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| ef455905-2708-35c6-af38-c1ba13f43fbf | -1.08816 | -53.65693 | 2024-11-01 05:23:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| ee9cd228-5a8d-3fdb-b842-a3942766b641 | -1.08034 | -53.65189 | 2024-11-01 05:23:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 09509acc-b050-3316-b572-74b0f22afd39 | -2.16907 | -53.66854 | 2024-11-01 05:23:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 71e477ef-6203-344c-9ce1-33b7ee85e8cc | -2.16361 | -53.67578 | 2024-11-01 05:23:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 9bb849f0-5965-3eb3-8115-5e77d3136f43 | -2.15935 | -53.67506 | 2024-11-01 05:23:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 0d09a0b7-d45b-300c-8a88-d665ca60f2f9 | -1.46668 | -54.23348 | 2024-11-01 05:23:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| eaa4a5d6-7bed-31bc-bc17-4fd15faada50 | -1.38663 | -53.60184 | 2024-11-01 05:23:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 4684c3e1-50e9-384f-ae87-86a2419448d6 | -1.20663 | -53.646 | 2024-11-01 05:23:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| e9e06617-4e03-3089-9e7a-f38ce7f8c184 | -1.19405 | -53.6437 | 2024-11-01 05:23:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 31709c82-c235-36f1-ad03-9845bc2513b9 | -1.18987 | -53.6428 | 2024-11-01 05:23:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 19b1be2c-fc20-362c-af02-e24ec02ec328 | -1.17125 | -53.68048 | 2024-11-01 05:23:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 88ae0c0b-89d3-3d77-bcc6-1033cab2d467 | -1.08876 | -53.65302 | 2024-11-01 05:23:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 7e029aab-c8ee-384e-a41a-9737279ce89c | -1.06658 | -53.65756 | 2024-11-01 05:23:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 4d29ea4e-45db-3d2b-a8c1-3165f29b8723 | -0.97967 | -53.71337 | 2024-11-01 05:23:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 00d72f37-6c90-3b23-a103-bdee20ee24a8 | -2.96777 | -53.91165 | 2024-11-01 05:23:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| fe040f40-5afd-3431-85d5-c0af726e5660 | -2.96351 | -53.91102 | 2024-11-01 05:23:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| ae237413-5f5f-33de-8cd6-4dbde840d239 | -2.96232 | -53.86446 | 2024-11-01 05:23:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 7c41dad9-1708-3c41-b291-9af4b4b341d1 | -2.96136 | -53.86643 | 2024-11-01 05:23:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 5957eab6-69d9-3397-97e7-fc5eb1f7502f | -2.95926 | -53.9104 | 2024-11-01 05:23:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| f12f0b1b-9f50-3b5e-b02c-8593a66280ac | -2.94228 | -53.70859 | 2024-11-01 05:23:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| f7b911c2-0e7f-3abe-932f-863ac6596611 | -2.92116 | -54.19864 | 2024-11-01 05:23:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ae31de5b-b8ea-3596-83b5-e9cb778e5fc5 | -2.91699 | -54.19801 | 2024-11-01 05:23:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 73b10720-a128-325c-a597-d23e15aa9e76 | -2.61574 | -54.934 | 2024-11-01 05:23:00 | NOAA-21 | BELTERRA | PARÁ | Brasil | 1501451 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| a04df7ca-df24-30c2-b79a-f7618de73448 | -2.55906 | -54.01049 | 2024-11-01 05:23:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 8d27dd4b-66bf-35ce-b9b1-30d3691702e9 | -2.55486 | -54.00984 | 2024-11-01 05:23:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 34c791a2-5ac9-34cd-a4d6-d3ffcf42d061 | -2.47648 | -53.98186 | 2024-11-01 05:23:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 7ed15090-1f14-3afd-be51-174f1aafb14b | -2.47591 | -53.98563 | 2024-11-01 05:23:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 26897b3f-0deb-32e6-aedd-3312d5fd4790 | -2.47228 | -53.98126 | 2024-11-01 05:23:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 045a0087-3971-34a7-b6f5-c60f45f4218f | -2.47113 | -53.98882 | 2024-11-01 05:23:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| ab3d9447-dc24-3423-b216-0b3f967a3c52 | -2.37011 | -53.79914 | 2024-11-01 05:23:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 184dc5d1-8ece-3bc5-8f38-a4ceccaaca13 | -2.36586 | -53.79852 | 2024-11-01 05:23:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 8cda0fc6-8abc-3a73-b5d6-f00b6f13ef77 | -2.31682 | -53.98164 | 2024-11-01 05:23:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 92c7d9e9-9b90-3224-b796-1ccd27e07f30 | -3.49144 | -54.02668 | 2024-11-01 05:23:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| edf4a9a5-29a0-3213-87c7-dc592a24b637 | -3.49085 | -54.0307 | 2024-11-01 05:23:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 713a970f-f46f-3d55-b220-f0c2785d89d6 | -3.4872 | -54.02596 | 2024-11-01 05:23:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 165513fb-71bd-3339-9fa8-318474e5d1f4 | -3.48661 | -54.02997 | 2024-11-01 05:23:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| dd3bb2c8-14dc-3386-914c-6b88c989753d | -3.48294 | -54.02533 | 2024-11-01 05:23:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 90eb340b-768a-3218-af72-eb07f5db9c3e | -3.45422 | -54.0745 | 2024-11-01 05:23:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 5ca8f223-959a-3050-aed3-9232b625d79a | -3.45362 | -54.07843 | 2024-11-01 05:23:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 63eb0e46-b61a-302c-a489-4ca8d009aafb | -3.4071 | -53.80446 | 2024-11-01 05:23:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b61ae463-95df-3a61-a5fd-bf826eba723b | -3.4065 | -53.80857 | 2024-11-01 05:23:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e7fb7684-15aa-3362-a9b9-2389eace2a3c | -3.40434 | -53.80612 | 2024-11-01 05:23:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 39d517a3-f0ca-3062-8e02-a901e5386838 | -3.40279 | -53.80378 | 2024-11-01 05:23:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d7c0227d-ad4f-325b-b1cf-69ec09bc296b | -3.4022 | -53.80786 | 2024-11-01 05:23:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 174628f9-1561-3527-a056-8a52269e4d90 | -3.37454 | -54.70914 | 2024-11-01 05:23:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 84be2acd-72ea-312e-bced-c774bd81fe53 | -3.37406 | -54.70888 | 2024-11-01 05:23:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e37e4468-dfe1-395b-a2ff-395ae042df6f | -3.33845 | -54.61508 | 2024-11-01 05:23:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| a5945143-6569-37cc-8fc2-3f44d6b7881a | -3.23959 | -54.63441 | 2024-11-01 05:23:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 36c1a5e4-5dd9-3635-a373-d307c6874b48 | -3.20653 | -53.84789 | 2024-11-01 05:23:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| c30068ee-d6b3-3655-87db-a57826b3e410 | -3.20593 | -53.85195 | 2024-11-01 05:23:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| dfe7432f-24a1-3a69-8e15-2b7a8d8825ba | -3.12794 | -54.26379 | 2024-11-01 05:23:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 8f2e9d4b-c16f-3485-80d5-6863c452e709 | -3.12433 | -54.2594 | 2024-11-01 05:23:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 1ed49649-de32-32de-9a1a-ef6bf40615a9 | -3.12377 | -54.26324 | 2024-11-01 05:23:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| cc5cd0f3-aab4-37e3-a6fe-d2b2050eb708 | -3.12321 | -54.26708 | 2024-11-01 05:23:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| f1163fdf-c992-3457-af43-ae9c4ba4ea90 | -3.12291 | -54.29799 | 2024-11-01 05:23:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 1ae7bc66-fa98-3200-8183-844884cff6e9 | -3.12264 | -54.27092 | 2024-11-01 05:23:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| f3d49610-7e3f-313e-932a-7fac21809103 | -3.12209 | -54.27472 | 2024-11-01 05:23:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 77f516b3-8faa-3b3e-bd15-e44df1c15314 | -3.12016 | -54.25883 | 2024-11-01 05:23:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 56ff7228-1ac5-3ad1-9483-9aa7d4ebc0f9 | -3.1196 | -54.26266 | 2024-11-01 05:23:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 1a8245fc-56dc-30de-9141-499ffeb9e609 | -3.11904 | -54.26648 | 2024-11-01 05:23:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 83c750db-ab25-3ab9-ada9-8ed69634ba66 | -3.11876 | -54.29736 | 2024-11-01 05:23:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| ede2097d-d9a0-3197-b49d-883ebdb7ae76 | -3.11848 | -54.2703 | 2024-11-01 05:23:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 0330cd56-c2b3-3f09-ad3c-a2c206f63c2f | -3.11821 | -54.30111 | 2024-11-01 05:23:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 46429aaf-e67b-3849-86bf-97eb9162bc33 | -3.11759 | -54.26269 | 2024-11-01 05:23:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 6d289c3d-6561-3e4a-bea8-def36fbf7451 | -3.11701 | -54.26649 | 2024-11-01 05:23:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 6577a95c-b1d7-3dd6-9a35-85a4d073f58d | -3.11642 | -54.2703 | 2024-11-01 05:23:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |


[Clique aqui para ver as próximas entradas](README48.md)
