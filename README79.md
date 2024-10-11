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

## Dados Diários - Página 79

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| b43bc186-153f-302a-8bac-490e69b288c0 | -5.61427 | -51.17033 | 2024-10-11 05:16:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 9705fe90-901e-3b69-8f0b-d6d78f1797ec | -5.55647 | -51.61704 | 2024-10-11 05:16:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 71f13aa8-f4fd-3588-88fd-f37613b8679a | 0.58136 | -51.70099 | 2024-10-11 05:16:00 | NOAA-21 | PORTO GRANDE | AMAPÁ | Brasil | 1600535 | 16 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 345286af-83bc-38aa-ba7b-c088eb645da7 | -1.66129 | -52.13823 | 2024-10-11 05:16:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 9d8a74cf-5d44-34d7-84c5-59282ed12a5f | -1.66069 | -52.1421 | 2024-10-11 05:16:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 35d5ada1-b06b-3c98-bc48-a69f35a97886 | -1.36682 | -53.01855 | 2024-10-11 05:16:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 6e9d1ce0-6f78-32eb-b22f-e8b7a457b3b8 | -3.55323 | -53.27885 | 2024-10-11 05:16:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 9e7f3207-25bf-359e-9ebf-cac32f4db24d | -3.3563 | -53.37727 | 2024-10-11 05:16:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| d7ef5865-512e-34ec-91ff-b350161d1e18 | -3.33622 | -53.22576 | 2024-10-11 05:16:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 2fe7f12c-e2a0-365d-b340-e768d55bf11c | -3.33274 | -53.2216 | 2024-10-11 05:16:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 204e66eb-1fe9-397a-9b0b-2e160477a197 | -3.3322 | -53.22513 | 2024-10-11 05:16:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 7bac9530-a2a0-34e7-9fdb-4a20add39897 | -3.32872 | -53.22094 | 2024-10-11 05:16:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 3662f978-d36c-39a1-8445-9fde4e2130b5 | -3.32818 | -53.22448 | 2024-10-11 05:16:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d22ca3a0-9294-313e-8ce0-ea9edeb36ffb | -2.84375 | -53.31672 | 2024-10-11 05:16:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 51cc2b1f-e80b-3132-b148-c5df81ed1a3c | -2.84324 | -53.32014 | 2024-10-11 05:16:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 161acb92-5ca5-3926-bdbb-62655077ef8f | -2.83927 | -53.31953 | 2024-10-11 05:16:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 654b5d5d-a170-3bc6-9980-b5e90c1a43c2 | -2.83875 | -53.32295 | 2024-10-11 05:16:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 4ec584a9-43b3-3857-a81d-709e10901506 | -3.48443 | -52.82716 | 2024-10-11 05:16:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 64965cae-f5b0-316a-abb8-ac79f5088002 | -3.47784 | -52.81467 | 2024-10-11 05:16:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 4d29cb17-1bb4-3634-af12-f591b5c2ff35 | -3.47657 | -52.87921 | 2024-10-11 05:16:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| b5da06ae-1b61-3981-8bdd-6ff86a8b3df5 | -3.44925 | -52.72097 | 2024-10-11 05:16:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| ec7ce248-e122-3f7d-8580-99fedd15a7f1 | -3.32836 | -53.0038 | 2024-10-11 05:16:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 87f46ec3-16c3-3fc3-93e3-01286a4ee4f8 | -3.32781 | -53.00746 | 2024-10-11 05:16:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 03cb1ce9-3279-3c86-87aa-c093e98a7e87 | -3.32427 | -53.00326 | 2024-10-11 05:16:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 33f34506-113b-3ac4-a5d1-77052a758da8 | -3.06742 | -52.91304 | 2024-10-11 05:16:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 288885eb-2299-39d2-bcf4-3fe173d04d65 | -3.03918 | -53.04257 | 2024-10-11 05:16:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 8ed59eba-dba2-3c99-b59e-0bf29ba8982e | -2.98857 | -52.90845 | 2024-10-11 05:16:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 25.4 |
| 884e1e88-9c43-3c30-961f-e01230bf1151 | -2.98803 | -52.91209 | 2024-10-11 05:16:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| a1b922aa-0062-38dc-95eb-e126b4b72ef7 | -2.98503 | -52.90415 | 2024-10-11 05:16:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 25.4 |
| 5432c01b-a069-331e-ae44-d388faf7ed78 | -2.98448 | -52.90782 | 2024-10-11 05:16:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 25.4 |
| 7cc4c844-cdeb-3889-8df2-2365bea1ef9f | -2.98394 | -52.9115 | 2024-10-11 05:16:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 53e6ace2-4902-387c-825c-8b00625ed169 | -2.98127 | -52.90369 | 2024-10-11 05:16:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 11.4 |
| c2e45721-3f07-3211-975c-37af04f631fd | -2.98094 | -52.90345 | 2024-10-11 05:16:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 11.8 |
| cbe592e9-4790-3338-b805-68184f96f96b | -2.9807 | -52.90739 | 2024-10-11 05:16:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 11.4 |
| 7e02a994-6160-3f32-bb43-69fd9d753f46 | -2.9804 | -52.90717 | 2024-10-11 05:16:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 11.8 |
| 890bf351-7748-3a98-9e04-d0255523330a | -2.98012 | -52.9111 | 2024-10-11 05:16:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 681e6cdb-062b-310a-9593-252d409d6a33 | -2.97985 | -52.91088 | 2024-10-11 05:16:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 6.4 |
| 8113f5c9-d296-3188-bda1-aec15a268800 | -2.97776 | -52.89933 | 2024-10-11 05:16:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| d0d820a7-d45c-3767-a05a-194d071e731a | -2.9774 | -52.89909 | 2024-10-11 05:16:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| fcb72c8e-2af0-3998-95d7-7b69d298773f | -2.97719 | -52.90305 | 2024-10-11 05:16:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 11.4 |
| 36bd1c49-c851-3fbd-af38-57704c68cbd9 | -2.97685 | -52.90281 | 2024-10-11 05:16:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 11.8 |
| 6d1afc56-fb2b-3a2a-a15f-38f9f31bf391 | -2.97661 | -52.90676 | 2024-10-11 05:16:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 11.4 |
| 9963081b-8778-36c2-9101-2763e81bbbea | -2.97631 | -52.90654 | 2024-10-11 05:16:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 11.8 |
| 790ba43e-1b71-3a22-9748-4837f3d2b5ca | -2.97603 | -52.91048 | 2024-10-11 05:16:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 4d7dad5e-06c7-3334-975e-5dc43fb71c11 | -2.97576 | -52.91025 | 2024-10-11 05:16:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 6.4 |
| 9b70299b-750c-3e70-8eac-82a4a302a8d8 | -2.97367 | -52.89873 | 2024-10-11 05:16:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 628731d1-902f-34c8-b3a5-1f0644126a24 | -2.97309 | -52.90244 | 2024-10-11 05:16:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 7.1 |
| c49ce939-e2c2-36c7-a370-b76221ee3969 | -2.97252 | -52.90616 | 2024-10-11 05:16:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 7.1 |
| ab71f8e7-dd58-3d20-9242-a958f9e29c00 | -2.97195 | -52.90985 | 2024-10-11 05:16:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 9.0 |
| dd28e5b5-0595-30cc-86ea-8c9f897169d2 | -2.969 | -52.90186 | 2024-10-11 05:16:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 7.1 |
| e74bddb8-2a44-32a2-b74e-5efc2eaeeeee | -2.96842 | -52.90558 | 2024-10-11 05:16:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 7.1 |
| ae15c546-12af-38ad-a2c7-08166fa9e061 | -2.96785 | -52.90929 | 2024-10-11 05:16:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 9.0 |
| 317aa17b-3a7b-3e8e-8210-5bda8bf4b0cd | -2.9649 | -52.90129 | 2024-10-11 05:16:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 7.2 |
| 78fde42a-28a8-3376-8acb-c0b833d40e58 | -2.96433 | -52.90502 | 2024-10-11 05:16:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 7.2 |
| ade8bcd9-f5e0-3808-b663-e20ede823d2d | -2.96375 | -52.90875 | 2024-10-11 05:16:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 7.8 |
| 6bf8230e-bd18-3e96-9f8b-58f4614027fa | -2.96081 | -52.90068 | 2024-10-11 05:16:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 7.2 |
| 08f99deb-3c6d-30bf-8367-b7a3e94e98c6 | -2.96024 | -52.9044 | 2024-10-11 05:16:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 7.2 |
| a489b7eb-348a-3956-b9c4-ec641d2fa861 | -2.95966 | -52.90812 | 2024-10-11 05:16:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 7.8 |
| 23488dda-e45b-3da9-a968-dae9e5c3353c | -2.95043 | -52.55039 | 2024-10-11 05:16:00 | NOAA-21 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 92ec3cda-a0e7-3d05-853e-d3f12b342107 | -2.85152 | -52.90682 | 2024-10-11 05:16:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 57a847d1-5a3d-3592-a3ee-d7e9fe0e5d29 | -2.85095 | -52.91052 | 2024-10-11 05:16:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 42570655-5ea8-33da-bb6e-882bf1db4707 | -2.85053 | -52.94028 | 2024-10-11 05:16:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| a5e47d44-d3f3-3a36-942e-5752a40da14b | -2.84745 | -52.90616 | 2024-10-11 05:16:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 7299c086-e1c4-3e3d-9c51-45504d080181 | -2.84701 | -52.93609 | 2024-10-11 05:16:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 18e9aa57-8c94-3e42-839d-9b906467fa14 | -2.84688 | -52.90985 | 2024-10-11 05:16:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 57d93c3c-88f2-398a-b5c9-31a1b932d935 | -2.84646 | -52.93965 | 2024-10-11 05:16:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 1d8898cd-4af7-36cf-8936-9d88fa5c1bde | -2.84294 | -52.93542 | 2024-10-11 05:16:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| dcdf0322-c3f2-3227-9dd1-d7a4abe73b4e | -2.84238 | -52.93902 | 2024-10-11 05:16:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 11544fc0-3495-3cbf-ad07-8bcce35ab478 | -2.7947 | -52.92365 | 2024-10-11 05:16:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 2f72864c-8ddd-3602-8abe-67395820a7f0 | -2.79416 | -52.92727 | 2024-10-11 05:16:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b4a151f7-dcb0-3f77-b3db-18e277e4dfd1 | -2.78663 | -52.48479 | 2024-10-11 05:16:00 | NOAA-21 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 6.3 |
| a33b56de-1ef9-3d53-91c3-ca235ebe30d1 | -2.78604 | -52.48864 | 2024-10-11 05:16:00 | NOAA-21 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 6.3 |
| ff85f475-7dd0-313a-8692-731ae61b2332 | -2.78244 | -52.48416 | 2024-10-11 05:16:00 | NOAA-21 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 41feb771-e521-3bbd-bd55-1d0d4b1be740 | -2.78185 | -52.48801 | 2024-10-11 05:16:00 | NOAA-21 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 9a521560-1695-3c10-b8c9-b1381764f6b5 | -2.77883 | -52.47965 | 2024-10-11 05:16:00 | NOAA-21 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 55fbbd87-b643-3132-9a42-23793121968c | -2.77824 | -52.48352 | 2024-10-11 05:16:00 | NOAA-21 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 8.4 |
| 401a28a3-4f7d-32d0-a645-0c4146925f8a | -2.77765 | -52.48738 | 2024-10-11 05:16:00 | NOAA-21 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 8.4 |
| e572a3ae-bf35-3261-a83b-c837c0f5417f | -2.77463 | -52.47899 | 2024-10-11 05:16:00 | NOAA-21 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| f3bcdd1a-fa42-3edf-9e54-3e13caf9f13b | -2.77405 | -52.48286 | 2024-10-11 05:16:00 | NOAA-21 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 8.4 |
| cfbbdb6c-5175-36cf-9de4-b0eaa4dbd4db | -2.68323 | -53.34567 | 2024-10-11 05:16:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| edfa94d3-9fa0-30cd-a4a2-da3fe98bb379 | -2.68244 | -53.35075 | 2024-10-11 05:16:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 03e13a21-bf83-3803-9de7-3555780d930e | -2.68006 | -53.33996 | 2024-10-11 05:16:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| a2e3bc8a-3219-3deb-8e5a-9e6a006616ca | -2.67927 | -53.34506 | 2024-10-11 05:16:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| e48a4bd6-95b6-3ee9-8842-7988833f6ec5 | -2.67849 | -53.35014 | 2024-10-11 05:16:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| be81f116-8b72-36b2-9902-8acb6dc6f192 | -2.67611 | -53.33934 | 2024-10-11 05:16:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 1d125ca6-8d79-3c3e-adf8-17c803c9af1f | -2.67532 | -53.34444 | 2024-10-11 05:16:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 6d7015b8-7986-3417-b84f-0b830a0e60ab | -2.67453 | -53.34953 | 2024-10-11 05:16:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 83a326b9-19e0-39b4-af9f-d5d817df5c92 | -2.67375 | -53.3546 | 2024-10-11 05:16:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 2556e6cc-ef12-32aa-9b9f-d7496a65ca33 | -2.67136 | -53.34382 | 2024-10-11 05:16:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 655807a0-83b2-3482-ad3d-50ea5d24c085 | -2.67058 | -53.34891 | 2024-10-11 05:16:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 5066931b-c5bc-32ce-b0ab-a836c6ccbf40 | -2.66979 | -53.35399 | 2024-10-11 05:16:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 4c092b7b-2be8-3d32-8d80-2e65dce61361 | -2.66741 | -53.34321 | 2024-10-11 05:16:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| f4e950f3-ddbc-3487-9100-11594f58213f | -2.66662 | -53.3483 | 2024-10-11 05:16:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 280e5185-417b-3bbf-99c0-749ee2e2e04a | -2.66584 | -53.35339 | 2024-10-11 05:16:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 67af2362-9d98-35d6-b496-12740e0cb975 | -2.66345 | -53.3426 | 2024-10-11 05:16:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 20.1 |
| 05eb62c3-4b57-3ae4-b2ad-419ebbc423e4 | -2.66267 | -53.34769 | 2024-10-11 05:16:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 20.1 |
| 10513afa-f915-3a4d-9df6-0377fffde8ce | -2.66189 | -53.35278 | 2024-10-11 05:16:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 21.0 |
| 00126428-59dd-33f4-ae82-c90934a9f7a2 | -2.65872 | -53.34708 | 2024-10-11 05:16:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 20.1 |
| f6548e78-b54d-3311-ab21-1b4809737ab2 | -2.65793 | -53.35217 | 2024-10-11 05:16:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 21.0 |
| 7b56a545-05ba-3b1d-a1ff-78276560313b | -2.65476 | -53.34646 | 2024-10-11 05:16:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 7.9 |


[Clique aqui para ver as próximas entradas](README80.md)
