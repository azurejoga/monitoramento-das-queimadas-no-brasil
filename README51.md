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

## Dados Diários - Página 51

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 7e282254-06b1-355d-87ad-c617c0cac38b | -2.25726 | -50.44618 | 2024-11-03 04:46:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 0b2ac66c-8e7d-30ab-a339-674f544fa7d1 | -2.25672 | -50.44962 | 2024-11-03 04:46:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| e2bf2a2a-fa30-3433-910e-5a37b9769123 | -2.2561 | -50.43193 | 2024-11-03 04:46:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ce04056c-6305-359a-b372-28c6b041f429 | -2.25395 | -50.44567 | 2024-11-03 04:46:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 766f4374-f478-3093-bd92-34b90b016cf6 | -2.2528 | -50.43142 | 2024-11-03 04:46:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 5a47535d-6a68-3ef6-86ae-6ee1eb9ba3b8 | -2.25181 | -50.45941 | 2024-11-03 04:46:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| cf8bd33b-c00f-3bac-ba6c-8cb29b0000f9 | -2.25057 | -50.42404 | 2024-11-03 04:46:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| f3bd071a-e29b-332d-a664-470339ddb131 | -2.25003 | -50.42748 | 2024-11-03 04:46:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| b8a988c2-6e1b-3e11-b245-01a21f37d20e | -2.24992 | -50.53657 | 2024-11-03 04:46:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 9d4973cd-7a34-3bd8-a315-47eda3ce2c4a | -2.24949 | -50.43091 | 2024-11-03 04:46:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| c4eae4ad-3262-3ce9-90ab-f21203417836 | -2.24896 | -50.43435 | 2024-11-03 04:46:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 691e3c82-98b5-3445-b4fe-96e26fb3d280 | -2.2485 | -50.45891 | 2024-11-03 04:46:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 8d82dbf3-dc19-37ae-934a-0dac788af10a | -2.24842 | -50.43779 | 2024-11-03 04:46:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| e3d5f18b-cda8-33c2-8a52-ff99d89da2c6 | -2.24661 | -50.53606 | 2024-11-03 04:46:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| d3a07b9b-ea0b-32d8-bfd0-04fe3b6cb1a5 | -2.24565 | -50.43384 | 2024-11-03 04:46:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 20c403f0-6fe3-39ce-8dc6-596976a72b9c | -2.24438 | -50.52867 | 2024-11-03 04:46:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 994b1257-6414-394e-98e6-fa6333052ad7 | -2.24384 | -50.53211 | 2024-11-03 04:46:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| f3897f65-fec2-3f94-84d6-2f6d1daeb00b | -2.23244 | -50.43181 | 2024-11-03 04:46:00 | NOAA-21 | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 9a4fb188-ac40-30f4-9637-77fcc6b82748 | -2.23191 | -50.43525 | 2024-11-03 04:46:00 | NOAA-21 | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 118d8091-46f3-3d02-b598-58954364e2a3 | -2.23137 | -50.43868 | 2024-11-03 04:46:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 692da8a2-d48e-30e6-9122-1cf6cf82fb60 | -2.22807 | -50.43817 | 2024-11-03 04:46:00 | NOAA-21 | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| b34fe846-850c-32bc-a77d-e560d9675673 | -2.21641 | -50.55607 | 2024-11-03 04:46:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| e5717a22-2fcd-3c3b-9fdb-8bb0663266ae | -2.20088 | -50.5255 | 2024-11-03 04:46:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| c49de3a2-a16c-30f6-a0d5-b8ce9ad1c9ff | -2.20034 | -50.52894 | 2024-11-03 04:46:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 9497cd17-7c28-345f-a836-a70d8e777764 | -2.19589 | -50.51416 | 2024-11-03 04:46:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 1000a5db-b14c-3fb0-b212-2b74cf3facc5 | -2.19581 | -50.49303 | 2024-11-03 04:46:00 | NOAA-21 | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| c5a51216-b2bf-3542-9e24-a2c28c24fcf7 | -2.19535 | -50.5176 | 2024-11-03 04:46:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| cb63d443-f4ff-357d-ae1f-36e3c7a35d48 | -2.19251 | -50.49252 | 2024-11-03 04:46:00 | NOAA-21 | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 0bde7453-61cf-340f-b42b-648e2f1e9e90 | -2.17829 | -50.5185 | 2024-11-03 04:46:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 48a74fd6-4724-3197-bf3f-20b96df3714e | -2.1776 | -50.47967 | 2024-11-03 04:46:00 | NOAA-21 | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| c9c56b3c-268c-370d-96a4-089ef7924272 | -2.16948 | -50.50638 | 2024-11-03 04:46:00 | NOAA-21 | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| ebf9e974-6edf-335b-bff0-2e5c156eb9d9 | -2.16894 | -50.50982 | 2024-11-03 04:46:00 | NOAA-21 | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 53f2dbe2-28e2-3af1-8ab4-6a2ffd3eec89 | -2.16876 | -50.46753 | 2024-11-03 04:46:00 | NOAA-21 | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| c7bd1df1-d75a-35fa-b66e-3342252bc1ff | -2.16617 | -50.50587 | 2024-11-03 04:46:00 | NOAA-21 | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| c5a69c0e-f7ae-3012-b781-9abf0de97adc | -2.16564 | -50.50931 | 2024-11-03 04:46:00 | NOAA-21 | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| b67879df-3149-38d8-a26b-fe307e198c2c | -2.20399 | -50.78738 | 2024-11-03 04:46:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 932b6927-c4ee-3aa6-93e6-e3ab05c8ac03 | -2.20345 | -50.79084 | 2024-11-03 04:46:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| f26230e9-746b-34f8-b2f1-28488d82647e | -2.20067 | -50.78688 | 2024-11-03 04:46:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 174842d5-c908-34ed-be9f-5d20d82dcf4a | -2.19912 | -50.81854 | 2024-11-03 04:46:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d40bfa47-ea41-37bf-8637-85273cd717c8 | -2.19527 | -50.8215 | 2024-11-03 04:46:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 495aba08-5c9a-335c-94c5-3867d64e792a | -2.1935 | -50.78931 | 2024-11-03 04:46:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 9700140a-711c-3d7f-82cf-1c2d24e87607 | -2.1908 | -50.80662 | 2024-11-03 04:46:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| cb9cd2fa-2b55-3525-83d7-e30f269ab2bc | -2.18855 | -50.97341 | 2024-11-03 04:46:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 5f9e86ed-d10b-39c1-b012-9f568aa81c2f | -2.18801 | -50.97689 | 2024-11-03 04:46:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ddc650c0-9fdf-3d06-932e-9f361ca3e60f | -2.18468 | -50.97638 | 2024-11-03 04:46:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 7d56f19a-08a4-3be9-9718-627e9612ab46 | -2.15793 | -50.90813 | 2024-11-03 04:46:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 1817ce2f-85cf-37f5-9774-b7549e838dcf | -2.15401 | -50.88974 | 2024-11-03 04:46:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 87958f5c-63ae-3a03-8c82-edffb2651aa1 | -2.15053 | -50.82526 | 2024-11-03 04:46:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 5b8dedb8-f038-3f00-be88-94f7cc7d487b | -2.14716 | -50.80345 | 2024-11-03 04:46:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 8cdcdef2-19d0-3c81-805d-a0f1d5e1f05f | -2.14708 | -50.99913 | 2024-11-03 04:46:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e1b9115a-3b50-3ede-a4be-c0cb13ca07d0 | -2.14439 | -50.79948 | 2024-11-03 04:46:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b87b2490-5de7-3153-b3b9-b32d7d39b7f7 | -2.14321 | -51.00211 | 2024-11-03 04:46:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| e5cd8087-33dc-310b-a7f4-8b992a7f3c7b | -2.14266 | -51.00559 | 2024-11-03 04:46:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 4f0c7e65-2d73-3599-a1e9-99b689a995c3 | -2.14211 | -51.00908 | 2024-11-03 04:46:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 6c2b49c9-2899-388c-9434-3f71ed359aa8 | -2.13127 | -50.86136 | 2024-11-03 04:46:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 0c2720b5-ac7b-3df7-a224-44cbc9deddb0 | -2.12568 | -50.83208 | 2024-11-03 04:46:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 3e9c9bb7-0f66-391b-8d9e-f9cdd6423995 | -2.12291 | -50.82811 | 2024-11-03 04:46:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 747b1343-d80b-3097-9bbd-ea1dfc44ecb6 | -2.12236 | -50.83158 | 2024-11-03 04:46:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |
| cb0af33a-5e6e-3c6c-8e11-e5e7be682e75 | -2.11893 | -50.83088 | 2024-11-03 04:46:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 661005c6-e4b6-3fba-a8eb-6b1a5bb214f2 | -2.11562 | -50.83037 | 2024-11-03 04:46:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c2f13e8b-3e48-3fcb-8300-0658a33df9e5 | -2.1123 | -50.82986 | 2024-11-03 04:46:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| d261cf32-5e08-385a-b8d2-2594109f88af | -2.10898 | -50.82935 | 2024-11-03 04:46:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| a698150b-4bc1-354d-8644-adda3c9c2ef5 | -2.09843 | -51.09181 | 2024-11-03 04:46:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 3a74ad72-80fc-3c01-82e6-21c0d0fafa7e | -2.09708 | -50.90574 | 2024-11-03 04:46:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| ea7aa9da-a976-33c9-b279-62fdb0241f08 | -2.09327 | -50.75599 | 2024-11-03 04:46:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| cf67f6e5-b2c8-38c6-bad6-1b79654e6926 | -2.09098 | -50.90124 | 2024-11-03 04:46:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| fab06830-6777-3109-83b2-d99787947ba3 | -2.08591 | -51.43316 | 2024-11-03 04:46:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| cfab250c-fa6c-31f7-a781-4733639c2fa2 | -2.03704 | -50.78988 | 2024-11-03 04:46:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| b995e759-e539-3ad8-9089-fc0be09d34a5 | -2.0367 | -50.87865 | 2024-11-03 04:46:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 2b7c056b-e470-3bb5-9ec6-c0e74bac3dae | -2.0241 | -50.93724 | 2024-11-03 04:46:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 697117d1-1abf-3ea3-9d3d-3197f3782974 | -2.02078 | -50.93673 | 2024-11-03 04:46:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 621143b3-96d9-362a-b10d-40cf6908d14e | -1.96571 | -50.63663 | 2024-11-03 04:46:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 6790f6e5-19c2-37a1-971a-ccb3d2ff5b35 | -1.9624 | -50.63612 | 2024-11-03 04:46:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 10074ac4-b625-3bed-b58a-d9246baab116 | -1.96186 | -50.63957 | 2024-11-03 04:46:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 99936832-d913-3aac-98ed-2368e2276e7f | -1.93711 | -51.40294 | 2024-11-03 04:46:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 7fbf9376-acb6-3ca1-86a2-f8c5c49d23eb | -1.8644 | -51.32573 | 2024-11-03 04:46:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| a93cc6a6-a870-3f1f-b9b1-10c415007ebb | -2.23126 | -50.69955 | 2024-11-03 04:46:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 35d54567-9c3b-3506-abe9-96acf0e24991 | -2.22734 | -50.68127 | 2024-11-03 04:46:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 7daf9ab5-002d-3208-ab6b-30c02502612e | -2.22364 | -50.72666 | 2024-11-03 04:46:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 534c2a81-f322-36eb-a84e-f18dd3c04524 | -2.22087 | -50.7227 | 2024-11-03 04:46:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 50ff4c0c-b022-3d99-83c2-a5ded2789037 | -2.16343 | -50.69971 | 2024-11-03 04:46:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| cb80e742-3ec0-382a-b627-5c9b432636ad | -2.16295 | -50.7244 | 2024-11-03 04:46:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 7fed0832-8e17-3ea2-b6f0-18a1aca12082 | -2.16241 | -50.72785 | 2024-11-03 04:46:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 6e2b4545-4d7c-33db-a00a-d73875b1792f | -2.16156 | -50.62522 | 2024-11-03 04:46:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| fb87dd6b-d673-3815-9d57-683ac8ccbcb8 | -2.16101 | -50.62867 | 2024-11-03 04:46:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 806b6cf1-ad66-3995-bc37-8fb46b244a39 | -2.15885 | -50.64246 | 2024-11-03 04:46:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| d1c4caaf-5840-3344-ba66-7c1a0972fcc2 | -2.15862 | -50.75205 | 2024-11-03 04:46:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 3256f3e9-4c8c-3c53-98d3-50ad106da8af | -2.15825 | -50.62471 | 2024-11-03 04:46:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 1fad6da5-1103-315f-a5b6-2d6fab72f513 | -2.15771 | -50.62816 | 2024-11-03 04:46:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 7b7d548f-8485-3469-b697-aa5868055328 | -2.155 | -50.6454 | 2024-11-03 04:46:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 2833c432-0342-3c7f-9d70-b234d0ca80b3 | -2.15422 | -50.75846 | 2024-11-03 04:46:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| af6e7f1f-b7d1-3e85-aeab-e3073cf6424e | -2.14964 | -50.70113 | 2024-11-03 04:46:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| a90688ea-b8ac-3b50-a0d2-eccb95b346d2 | -2.14356 | -50.69666 | 2024-11-03 04:46:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| c4ed5f70-715c-3ae2-b504-6a56e721e3a1 | -2.14302 | -50.70011 | 2024-11-03 04:46:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 35945be4-e4b9-3152-86e2-54d8628ea68c | -2.13941 | -50.69937 | 2024-11-03 04:46:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 73b62d6c-a2c9-33e7-95af-0f211724aec2 | -3.51839 | -51.66748 | 2024-11-03 04:46:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 6640fd46-f6be-3927-b00d-3b8d14849232 | -3.51783 | -51.67102 | 2024-11-03 04:46:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 73c9a624-8cfb-3139-89e8-93ac9babd17b | -3.51448 | -51.67051 | 2024-11-03 04:46:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 59b30f78-3daa-3227-b2ab-417a1d647214 | -3.45749 | -51.77765 | 2024-11-03 04:46:00 | NOAA-21 | VITÓRIA DO XINGU | PARÁ | Brasil | 1508357 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 8ada4363-d136-3c66-8bbd-d75ca884007e | -3.39959 | -52.14599 | 2024-11-03 04:46:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |


[Clique aqui para ver as próximas entradas](README52.md)
