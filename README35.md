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

## Dados Diários - Página 35

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| d53cc654-042e-3c38-a8dd-fbe112e887e9 | -16.8532 | -55.96433 | 2024-10-02 01:26:00 | TERRA_M-M | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 9.3 |
| 6080e3ab-c74d-3345-88e3-2526c6a7cfc3 | -16.85296 | -55.90708 | 2024-10-02 01:26:00 | TERRA_M-M | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 13.0 |
| 372d3093-020b-3de8-bfbf-a3acb9596c0d | -16.85167 | -55.89707 | 2024-10-02 01:26:00 | TERRA_M-M | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 16.5 |
| fd5dd887-deb6-3dbe-917c-c45ea50cda5e | -16.85038 | -55.88707 | 2024-10-02 01:26:00 | TERRA_M-M | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 17.4 |
| 6b4d188d-3e30-3940-a34d-6eb6804de9bd | -16.84522 | -55.90414 | 2024-10-02 01:26:00 | TERRA_M-M | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 10.0 |
| 2cb8b73a-2e10-3e13-b37e-fdec6de9ecf6 | -16.84389 | -55.89415 | 2024-10-02 01:26:00 | TERRA_M-M | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 26.2 |
| 5ae748bb-7b62-3517-b4b8-215134c59fa0 | -16.84256 | -55.88416 | 2024-10-02 01:26:00 | TERRA_M-M | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 17.5 |
| f11b687f-ab4d-3363-bc23-7de9ea39081b | -16.836 | -55.90547 | 2024-10-02 01:26:00 | TERRA_M-M | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 42.7 |
| 4aa812b1-2b27-3b59-aec8-c91db7b2f576 | -16.83467 | -55.89547 | 2024-10-02 01:26:00 | TERRA_M-M | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 70.6 |
| 3694ec58-c8bd-3f1e-967c-8a16b9858702 | -16.83335 | -55.88548 | 2024-10-02 01:26:00 | TERRA_M-M | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 37.6 |
| b48d8d73-4d21-3dc9-9d10-6c36a70ec3d0 | -16.83203 | -55.87551 | 2024-10-02 01:26:00 | TERRA_M-M | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 8.5 |
| 19c99387-146e-33e5-8083-6e27a4de0a15 | -16.82809 | -55.91679 | 2024-10-02 01:26:00 | TERRA_M-M | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 29.7 |
| 31131448-565c-3471-a490-9be7d3ab7aac | -16.82677 | -55.90678 | 2024-10-02 01:26:00 | TERRA_M-M | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 53.4 |
| 45694de7-0cde-30b8-96eb-7d60be8fb1e4 | -16.82547 | -55.96832 | 2024-10-02 01:26:00 | TERRA_M-M | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 5.5 |
| d4960f76-489a-3bf5-a21b-9dd3e674c0f5 | -16.82545 | -55.89678 | 2024-10-02 01:26:00 | TERRA_M-M | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 13.7 |
| 2e2c1981-bffa-30d2-820c-835c9d7876b6 | -16.82413 | -55.8868 | 2024-10-02 01:26:00 | TERRA_M-M | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 36.5 |
| 5e0be8f7-110a-3b67-8dd0-4eef67bb0647 | -16.82282 | -55.87682 | 2024-10-02 01:26:00 | TERRA_M-M | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 13.9 |
| 6732bf2c-0989-359d-ad83-6bb7469a7219 | -16.81887 | -55.91813 | 2024-10-02 01:26:00 | TERRA_M-M | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 67.6 |
| ade4036d-20e5-3f6d-ab13-bd93422a409a | -16.81624 | -55.89811 | 2024-10-02 01:26:00 | TERRA_M-M | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 7.1 |
| 282e2a48-5676-3a02-a162-ed69d934a79d | -16.81492 | -55.88813 | 2024-10-02 01:26:00 | TERRA_M-M | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 16.6 |
| 68c65669-e6f8-30d9-8caf-dddc3a824105 | -16.81361 | -55.87814 | 2024-10-02 01:26:00 | TERRA_M-M | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 14.3 |
| 2e5213aa-e022-3111-af69-41b9048a2b64 | -16.81227 | -55.93949 | 2024-10-02 01:26:00 | TERRA_M-M | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 5.3 |
| 1c2b3aeb-cc57-3cea-ad4f-3f87caa7710e | -16.81096 | -55.92947 | 2024-10-02 01:26:00 | TERRA_M-M | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 7.0 |
| 75255db2-053b-3318-b0f6-a155174bc25d | -16.68206 | -55.9335 | 2024-10-02 01:26:00 | TERRA_M-M | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 15.5 |
| 34d2d969-8580-3365-9584-eee0965958db | -16.64532 | -55.92474 | 2024-10-02 01:26:00 | TERRA_M-M | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 26.6 |
| 02971980-4e48-3f8e-9b55-79960db3914b | -13.28168 | -56.14789 | 2024-10-02 01:26:00 | TERRA_M-M | LUCAS DO RIO VERDE | MATO GROSSO | Brasil | 5105259 | 51 | 33 | nan | nan | nan | Cerrado | 7.6 |
| 9386a9c8-5a51-3371-bb5c-7908fe4d0ee0 | -16.63742 | -55.93605 | 2024-10-02 01:26:00 | TERRA_M-M | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 11.7 |
| f16208c0-fab0-3448-bbee-0407b4a21762 | -16.63611 | -55.92607 | 2024-10-02 01:26:00 | TERRA_M-M | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 13.7 |
| e780407d-391b-3a47-aa47-b1810d701ff2 | -16.62821 | -55.93737 | 2024-10-02 01:26:00 | TERRA_M-M | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 12.1 |
| b8c54232-ee9f-395a-a144-095060e927c0 | -16.6269 | -55.92739 | 2024-10-02 01:26:00 | TERRA_M-M | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 11.6 |
| 62253fa0-17d0-3882-a149-454ff2987d72 | -16.61899 | -55.9387 | 2024-10-02 01:26:00 | TERRA_M-M | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 9.9 |
| 2652c037-59ff-3564-a122-54649e3185b0 | -16.61768 | -55.92872 | 2024-10-02 01:26:00 | TERRA_M-M | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 10.9 |
| 7992a31f-b208-34c6-b07b-d5d4d3d4868d | -16.61359 | -56.04166 | 2024-10-02 01:26:00 | TERRA_M-M | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 11.3 |
| dfc59567-5401-3b16-bd36-53725817e714 | -16.60978 | -55.94003 | 2024-10-02 01:26:00 | TERRA_M-M | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 6.8 |
| 1a295c1d-af6c-36cc-8b98-21fbdbcb8844 | -16.60847 | -55.93005 | 2024-10-02 01:26:00 | TERRA_M-M | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 6.6 |
| 878303c3-e882-37ae-b429-05fba4dda15b | -16.60706 | -55.99139 | 2024-10-02 01:26:00 | TERRA_M-M | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 16.6 |
| fd543bf5-d957-3a63-827d-7af5aafaf421 | -16.60433 | -56.04298 | 2024-10-02 01:26:00 | TERRA_M-M | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 12.2 |
| 19c14f2b-f054-3245-9b1e-baf7f93c8e45 | -16.59783 | -55.99271 | 2024-10-02 01:26:00 | TERRA_M-M | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 6.4 |
| 370e22cf-b08b-3d66-bee9-77c39d2992f4 | -16.59637 | -56.05439 | 2024-10-02 01:26:00 | TERRA_M-M | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 10.5 |
| 29d2aa6c-d68b-3c3b-91ae-cb6e8053eea7 | -16.59507 | -56.04431 | 2024-10-02 01:26:00 | TERRA_M-M | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 10.8 |
| 8f765a28-b195-3088-be4c-4dfb05ce9101 | -16.58903 | -56.05107 | 2024-10-02 01:26:00 | TERRA_M-M | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 5.7 |
| b3d276af-5d1b-31dd-a1b9-3e2656406802 | -11.82993 | -56.8504 | 2024-10-02 01:26:00 | TERRA_M-M | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 5.8 |
| fc699913-7229-3537-8bde-f9d42f5c3bdd | -11.82865 | -56.84072 | 2024-10-02 01:26:00 | TERRA_M-M | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 9.2 |
| 80a9ad3c-ab4e-3c71-9d37-da6dffa80fee | -11.77721 | -56.31738 | 2024-10-02 01:26:00 | TERRA_M-M | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 4e8ebb5c-5157-3161-8ec8-ca2946d9b7e2 | -11.82156 | -56.84797 | 2024-10-02 01:26:00 | TERRA_M-M | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 5.6 |
| dcdd4a20-3f1d-37c0-84b0-880a26090938 | -11.49192 | -56.79496 | 2024-10-02 01:26:00 | TERRA_M-M | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 20.4 |
| 7b1db2a2-3ea9-3e2b-814d-f6ae26026a7e | -11.49064 | -56.78541 | 2024-10-02 01:26:00 | TERRA_M-M | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 9.7 |
| 3b8dadbc-9eb3-30da-829b-856673842f3a | -11.48281 | -56.79626 | 2024-10-02 01:26:00 | TERRA_M-M | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 19.2 |
| fb83539f-d071-36a5-89de-62884f7408a8 | -11.48153 | -56.78671 | 2024-10-02 01:26:00 | TERRA_M-M | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 28.8 |
| e9ceee24-209b-398b-9778-1cf08a8c0ef6 | -11.32521 | -56.24313 | 2024-10-02 01:26:00 | TERRA_M-M | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 20.8 |
| 94ab041f-2222-3eca-9e82-dbff4a1d4e31 | -11.32395 | -56.23393 | 2024-10-02 01:26:00 | TERRA_M-M | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 7.7 |
| 7d51ea69-742d-329f-8a66-96734d0eb5f0 | -13.28296 | -56.15734 | 2024-10-02 01:26:00 | TERRA_M-M | LUCAS DO RIO VERDE | MATO GROSSO | Brasil | 5105259 | 51 | 33 | nan | nan | nan | Cerrado | 10.4 |
| 6da9914e-659d-33d5-b8f3-a1d5b7fdd4ed | -12.32351 | -63.7161 | 2024-10-02 01:26:00 | TERRA_M-M | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 22.1 |
| 13d13ab4-7ce2-3308-8ba0-12c805b291bd | -12.63495 | -63.1125 | 2024-10-02 01:26:00 | TERRA_M-M | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 21.3 |
| 84b7b5f7-3a89-36a9-acd8-d717843ffcb2 | -12.64955 | -63.11082 | 2024-10-02 01:26:00 | TERRA_M-M | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 127.4 |
| 1f962781-6d43-3bab-9922-00ffb95a1a41 | -12.74637 | -62.90678 | 2024-10-02 01:26:00 | TERRA_M-M | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 18.0 |
| b152a292-cbbd-3f31-9fbc-700840fc3886 | -12.84387 | -62.80492 | 2024-10-02 01:26:00 | TERRA_M-M | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 26.3 |
| c0311f0a-4761-386a-9260-92d1f80990c2 | -12.8696 | -62.77592 | 2024-10-02 01:26:00 | TERRA_M-M | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 49.7 |
| b8700b3f-d955-3067-96b7-be1c7afcc554 | -12.81139 | -62.55973 | 2024-10-02 01:26:00 | TERRA_M-M | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 19.2 |
| d8692df6-9ec2-3e9e-885c-3763aacf2463 | -12.8163 | -62.55388 | 2024-10-02 01:26:00 | TERRA_M-M | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 40.9 |
| 6c23074f-5c68-3d7f-b9be-81d0886b7d7e | -12.82541 | -62.55814 | 2024-10-02 01:26:00 | TERRA_M-M | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 23.4 |
| 91dbc215-52a0-39c2-a864-67198bc468ec | -12.84157 | -62.52615 | 2024-10-02 01:26:00 | TERRA_M-M | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 162.9 |
| 7c90c0b2-7333-37d5-988c-b94c288ed51e | -12.84432 | -62.55062 | 2024-10-02 01:26:00 | TERRA_M-M | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 264.8 |
| a99dc1de-a664-3702-9b57-1240c74d2095 | -12.85555 | -62.52451 | 2024-10-02 01:26:00 | TERRA_M-M | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 144.7 |
| 3718ca70-c837-3c29-bb3f-721b15a5883d | -12.85833 | -62.54898 | 2024-10-02 01:26:00 | TERRA_M-M | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 56.4 |
| abcf5153-ceac-3305-b949-451697029c53 | -12.9178 | -62.69321 | 2024-10-02 01:26:00 | TERRA_M-M | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 43.5 |
| ba4c9c90-6061-31c2-8126-d7c8b83de470 | -12.92073 | -62.71839 | 2024-10-02 01:26:00 | TERRA_M-M | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 17.9 |
| 0a8d6e2b-fcb6-3746-98f1-024275ad63d2 | -12.93608 | -62.68448 | 2024-10-02 01:26:00 | TERRA_M-M | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 137.5 |
| b689f716-fad5-38fa-8715-3973bf691002 | -12.93886 | -62.70963 | 2024-10-02 01:26:00 | TERRA_M-M | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 124.3 |
| 9101f0ee-08e1-3677-a6fd-eb7226028749 | -12.95025 | -62.6828 | 2024-10-02 01:26:00 | TERRA_M-M | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 218.1 |
| 43066d41-7d58-3a25-a887-10e7e0b5ffb2 | -12.95307 | -62.70798 | 2024-10-02 01:26:00 | TERRA_M-M | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 135.5 |
| 72d7627e-8c08-3eeb-907c-daf791138fb7 | -12.96158 | -62.65594 | 2024-10-02 01:26:00 | TERRA_M-M | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 25.3 |
| 0470ce37-ee27-3e7a-aff4-aedba2c9fb49 | -12.96442 | -62.68104 | 2024-10-02 01:26:00 | TERRA_M-M | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 38.6 |
| 8394c59b-184c-3304-b903-8acb19dc3777 | -12.7048 | -63.0773 | 2024-10-02 01:26:00 | TERRA_M-M | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 42.8 |
| d7697609-d4be-3467-8916-64f43c7b5602 | -12.74908 | -62.89987 | 2024-10-02 01:26:00 | TERRA_M-M | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 17.7 |
| 3a5070ad-233f-34f1-a66c-1f3a3c549258 | -12.82759 | -62.52779 | 2024-10-02 01:26:00 | TERRA_M-M | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 21.0 |
| 07efc6ab-92c2-3e57-b77f-75ad38d1bfa4 | -12.88386 | -62.77423 | 2024-10-02 01:26:00 | TERRA_M-M | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 25.7 |
| 5c7db57d-a4f4-3c4c-a5b9-012845388bda | -12.9219 | -62.68616 | 2024-10-02 01:26:00 | TERRA_M-M | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 46.9 |
| 66a15fbb-9c02-39dc-aab9-3f4ffa897c78 | -12.92466 | -62.71137 | 2024-10-02 01:26:00 | TERRA_M-M | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 66.9 |
| ff85c703-9da7-3d4c-bab6-dd827f73ccf0 | -12.93197 | -62.69153 | 2024-10-02 01:26:00 | TERRA_M-M | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 141.9 |
| 02315ff0-fe6f-32ff-9ac8-18dedcadcb83 | -12.93493 | -62.71665 | 2024-10-02 01:26:00 | TERRA_M-M | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 64.6 |
| d0abbc6a-ce85-3c76-8161-4c621dba8820 | -12.95876 | -62.631 | 2024-10-02 01:26:00 | TERRA_M-M | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 27.4 |
| 4e604741-962a-33dd-aa6b-63804077d4cd | -12.27213 | -62.31673 | 2024-10-02 01:26:00 | TERRA_M-M | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 13.2 |
| a459d7c5-06ca-3b0f-9ebd-abf5b45534aa | -12.34616 | -59.21735 | 2024-10-02 01:26:00 | TERRA_M-M | COMODORO | MATO GROSSO | Brasil | 5103304 | 51 | 33 | nan | nan | nan | Cerrado | 12.7 |
| fe30a8f6-efe9-3934-bbf4-2023a01ac87f | -12.14293 | -59.88985 | 2024-10-02 01:26:00 | TERRA_M-M | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 23.4 |
| 72fa62e5-034a-34c9-a926-d190c65acbc4 | -16.56376 | -58.24675 | 2024-10-02 01:26:00 | TERRA_M-M | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 7.6 |
| d424ba54-62e1-321f-be58-c5f5c9ff9424 | -16.57269 | -58.23201 | 2024-10-02 01:26:00 | TERRA_M-M | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 21.6 |
| 333bf753-2525-3d59-8a74-acb8cd55ae90 | -16.57432 | -58.24534 | 2024-10-02 01:26:00 | TERRA_M-M | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 28.8 |
| cbb01b7f-d37d-300d-98a1-de5956c0b04d | -16.58159 | -58.21728 | 2024-10-02 01:26:00 | TERRA_M-M | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 32.7 |
| 2a3df404-ee46-3e16-986a-a3d9ea78d5da | -16.58323 | -58.23055 | 2024-10-02 01:26:00 | TERRA_M-M | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 330.5 |
| 0ca2e136-5045-3d8c-b59c-c0094b694419 | -16.58489 | -58.24393 | 2024-10-02 01:26:00 | TERRA_M-M | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 163.7 |
| 5f6c8a00-de07-3ac7-9038-20e23b24e065 | -16.58822 | -58.22351 | 2024-10-02 01:26:00 | TERRA_M-M | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 561.9 |
| d0fd8d97-2493-3836-bb6f-0d82251f6702 | -16.58979 | -58.23691 | 2024-10-02 01:26:00 | TERRA_M-M | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 595.2 |
| 45a8857b-4177-3f03-89e3-5bf322b753fe | -16.59136 | -58.25034 | 2024-10-02 01:26:00 | TERRA_M-M | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 17.5 |
| f7f0f3d6-3fa2-3187-9d54-2f281fce0d3d | -16.59213 | -58.2158 | 2024-10-02 01:26:00 | TERRA_M-M | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 354.8 |
| 91e07ceb-4e2b-364a-bb8a-ca0e7ec67d29 | -16.59378 | -58.22906 | 2024-10-02 01:26:00 | TERRA_M-M | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 928.3 |
| 92368a31-c4de-33d4-8369-78c76ca282af | -16.59546 | -58.24249 | 2024-10-02 01:26:00 | TERRA_M-M | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 59.2 |
| 484ae1c0-475f-3dd8-8136-85b1b3077226 | -16.59721 | -58.20889 | 2024-10-02 01:26:00 | TERRA_M-M | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 23.4 |
| 58758775-1a3b-32d3-b35b-989a9eaeafe8 | -16.59877 | -58.22209 | 2024-10-02 01:26:00 | TERRA_M-M | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1228.4 |
| 21c098f8-2ae9-32d4-8025-a37e6b2d387c | -16.60035 | -58.23544 | 2024-10-02 01:26:00 | TERRA_M-M | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 198.6 |


[Clique aqui para ver as próximas entradas](README36.md)
