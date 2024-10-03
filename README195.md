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

## Dados Diários - Página 195

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 3db808ad-eb0d-3431-8643-a09600f764f6 | -12.4104 | -62.98634 | 2024-10-03 06:10:00 | NOAA-21 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 2708a6a4-6fc4-3dc7-ae96-a6f7a588a216 | -12.41233 | -63.00378 | 2024-10-03 06:10:00 | NOAA-21 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 20.7 |
| 7fe78ff6-375f-3e23-b785-b677cf1e58ed | -12.41278 | -62.99996 | 2024-10-03 06:10:00 | NOAA-21 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 80.7 |
| 4bd0ad46-0568-37a9-a283-e0e338fe7ed9 | -12.41322 | -62.99613 | 2024-10-03 06:10:00 | NOAA-21 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 80.7 |
| 488c2d07-88e3-3a99-bceb-1e4235925c09 | -12.4141 | -62.98861 | 2024-10-03 06:10:00 | NOAA-21 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 43.8 |
| c05cdca9-1972-351e-9f66-914455978841 | -12.41454 | -62.98484 | 2024-10-03 06:10:00 | NOAA-21 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 6bd0fc5a-2651-38b0-a8a0-b31d8242efcd | -12.41882 | -62.9969 | 2024-10-03 06:10:00 | NOAA-21 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 2.4 |
| a8b33fd3-6dc9-35f2-b7a4-e9e446216a25 | -12.41926 | -62.99312 | 2024-10-03 06:10:00 | NOAA-21 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 2.6 |
| c3e5c3b7-4710-3120-91e2-976c03256f8c | -12.63317 | -63.13072 | 2024-10-03 06:10:00 | NOAA-21 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 290a3a2a-e58a-3507-a49f-779184cd70e8 | -12.63362 | -63.12695 | 2024-10-03 06:10:00 | NOAA-21 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 5ea804e0-03ac-3add-9a53-48e9d77004d0 | -12.63406 | -63.12318 | 2024-10-03 06:10:00 | NOAA-21 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 3f0f3ff4-b082-3c52-a48b-98167ff8e9a2 | -12.63451 | -63.11942 | 2024-10-03 06:10:00 | NOAA-21 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 3.5 |
| be949d91-5ac6-324a-bb73-4356c4156860 | -12.63495 | -63.11565 | 2024-10-03 06:10:00 | NOAA-21 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 75664cc8-5139-311f-b6db-2380a559e7da | -12.63829 | -63.13521 | 2024-10-03 06:10:00 | NOAA-21 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 8b178125-5f10-3eb2-9408-9f4ffdf95f4e | -12.63963 | -63.12392 | 2024-10-03 06:10:00 | NOAA-21 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 5.5 |
| fc050703-53de-338e-b00f-f2e33b02465b | -12.64008 | -63.12016 | 2024-10-03 06:10:00 | NOAA-21 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 7.3 |
| 13b67329-48fe-3607-bc0e-e8df003c39cf | -12.64052 | -63.11641 | 2024-10-03 06:10:00 | NOAA-21 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 7.3 |
| 950265a0-8835-3c68-950a-36efb2610dfb | -12.64097 | -63.11264 | 2024-10-03 06:10:00 | NOAA-21 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 0d3b5545-82da-3311-97e9-c9f7b4886c91 | -12.64142 | -63.10886 | 2024-10-03 06:10:00 | NOAA-21 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 4.3 |
| cbfa91dc-8817-37a7-84c2-dbcd62f9f358 | -12.64186 | -63.10507 | 2024-10-03 06:10:00 | NOAA-21 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 6ed69316-938f-351e-a99e-422c69a16279 | -12.64386 | -63.13595 | 2024-10-03 06:10:00 | NOAA-21 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 991a790e-12e0-3d95-bb73-f389867beb04 | -12.64609 | -63.11714 | 2024-10-03 06:10:00 | NOAA-21 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 7.3 |
| a839bf99-6623-3ece-bccc-a23e438cc539 | -12.64654 | -63.11336 | 2024-10-03 06:10:00 | NOAA-21 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 3c004e2a-d0cc-3b2f-b886-0f0cfa7cc7ec | -12.64699 | -63.10958 | 2024-10-03 06:10:00 | NOAA-21 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 75c3b0a1-c2fd-3d3e-b62d-f91b84e8a693 | -12.64744 | -63.1058 | 2024-10-03 06:10:00 | NOAA-21 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 2.9 |
| ee7a3de7-ac2f-3b4f-aae6-77378f658b17 | -12.65212 | -63.1141 | 2024-10-03 06:10:00 | NOAA-21 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 2.2 |
| bffe035b-80a4-3441-9471-d25e35c269ec | -12.65257 | -63.11032 | 2024-10-03 06:10:00 | NOAA-21 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 705e9cdb-1c1f-3dc0-bd13-a86f7491e63d | -12.65302 | -63.10653 | 2024-10-03 06:10:00 | NOAA-21 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 8b6cd0d2-580f-3c34-b6ca-ba2d6000ebd0 | -12.76544 | -62.76242 | 2024-10-03 06:10:00 | NOAA-21 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 1.9 |
| b5b5af8d-0831-3b71-b786-26b13fccbd23 | -12.7659 | -62.75843 | 2024-10-03 06:10:00 | NOAA-21 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 30a58082-dfb0-3490-8320-4d4ead5dc732 | -12.83635 | -62.80017 | 2024-10-03 06:10:00 | NOAA-21 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 28626c9b-075b-3c7d-93ea-4c362dd9661c | -12.8381 | -62.80217 | 2024-10-03 06:10:00 | NOAA-21 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 6f3d6c05-d978-3bd2-a18d-aa2e0c92e142 | -12.84157 | -62.80492 | 2024-10-03 06:10:00 | NOAA-21 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 2cd881bb-e58e-3a18-972a-e402229e2a59 | -12.84205 | -62.80093 | 2024-10-03 06:10:00 | NOAA-21 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 0904bbe2-f46b-3f53-be56-e3bbf373d2d9 | -12.84253 | -62.79693 | 2024-10-03 06:10:00 | NOAA-21 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 60d8f429-37b9-3778-8b1e-4b36de94f61d | -12.84381 | -62.80295 | 2024-10-03 06:10:00 | NOAA-21 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 2.4 |
| bdf40b51-6fb4-3941-8ba1-a845473a2a5a | -12.84426 | -62.79895 | 2024-10-03 06:10:00 | NOAA-21 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 82ddaf39-6ce8-3f6c-b3cd-cfd5c91e1b37 | -12.84679 | -62.80966 | 2024-10-03 06:10:00 | NOAA-21 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 6c46cf5e-cb9a-3c01-8257-9aac863aa510 | -12.84823 | -62.7977 | 2024-10-03 06:10:00 | NOAA-21 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 5ec762d0-8921-38cd-8b18-0fdbcaa82498 | -12.85042 | -62.79573 | 2024-10-03 06:10:00 | NOAA-21 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 4.4 |
| d052d3b9-6edd-39b4-81aa-d3ceb322e2bd | -12.86892 | -62.78595 | 2024-10-03 06:10:00 | NOAA-21 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 329fa4d3-c92c-3c6b-8cd9-7cdc78560b98 | -12.86938 | -62.78193 | 2024-10-03 06:10:00 | NOAA-21 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 8451e821-719b-3155-9312-36f6cc1b8920 | -12.87216 | -62.75774 | 2024-10-03 06:10:00 | NOAA-21 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 28b7e5e1-f79d-311e-80fa-9a992adc4b26 | -12.89237 | -62.63216 | 2024-10-03 06:10:00 | NOAA-21 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 2.3 |
| ce7b6cf8-b940-35e2-b5b0-e76758966f2e | -12.9021 | -62.69996 | 2024-10-03 06:10:00 | NOAA-21 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 2.8 |
| c62db914-d206-3043-a1f0-a496295ad9c2 | -12.90737 | -62.70478 | 2024-10-03 06:10:00 | NOAA-21 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 3334b9c1-a472-30e3-ac31-3ee924092eb5 | -12.90784 | -62.70071 | 2024-10-03 06:10:00 | NOAA-21 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 1cafe971-4eac-3045-9b34-f0a680a71887 | -12.91216 | -62.7137 | 2024-10-03 06:10:00 | NOAA-21 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 2.9 |
| b4b526d2-8b69-391a-8987-3a59bd8e5c37 | -12.91264 | -62.70961 | 2024-10-03 06:10:00 | NOAA-21 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 2.9 |
| dd849de4-1753-31dd-8919-ac656f91b86f | -12.9179 | -62.71448 | 2024-10-03 06:10:00 | NOAA-21 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 2.9 |
| ac47b5c6-ded2-36d9-81fe-3e7951004d1b | -12.91838 | -62.71038 | 2024-10-03 06:10:00 | NOAA-21 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 2.9 |
| d62cceaa-f578-3ff6-a460-19fb191dfe89 | -12.97842 | -62.64765 | 2024-10-03 06:10:00 | NOAA-21 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 7.7 |
| 4747c068-a9bf-3ccd-851a-0ebf75ac5e71 | -12.97892 | -62.64352 | 2024-10-03 06:10:00 | NOAA-21 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 7.7 |
| 84059af1-a6be-325b-b87a-998b7f1bb909 | -12.97955 | -62.64659 | 2024-10-03 06:10:00 | NOAA-21 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 9.3 |
| 9158b74e-d2da-33cd-a728-8a3b08b0456b | -12.98361 | -62.71376 | 2024-10-03 06:10:00 | NOAA-21 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 2.2 |
| c82b561b-aed7-32c7-a4cf-ca79384bfaa3 | -12.98419 | -62.64841 | 2024-10-03 06:10:00 | NOAA-21 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 7.7 |
| f0d646b5-261a-320d-8d31-c2d5adacb865 | -12.98469 | -62.64428 | 2024-10-03 06:10:00 | NOAA-21 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 7.7 |
| 1d281512-a7d9-3840-9d11-55922b0d4e38 | -12.98485 | -62.65149 | 2024-10-03 06:10:00 | NOAA-21 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 11.1 |
| d891ce39-7331-343d-8dc4-8d91d1cbd8ed | -12.98519 | -62.64016 | 2024-10-03 06:10:00 | NOAA-21 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 0b219ccd-e604-3e65-bbbb-c2bd7109bd6c | -12.98532 | -62.64737 | 2024-10-03 06:10:00 | NOAA-21 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 9.3 |
| fbec6d67-0375-34a9-87d4-e7136a10b4af | -12.98579 | -62.64323 | 2024-10-03 06:10:00 | NOAA-21 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 9.3 |
| fcc98ac0-4fad-3dfc-9694-a50d502a1d7c | -12.98626 | -62.63909 | 2024-10-03 06:10:00 | NOAA-21 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 704de160-57fa-32a6-83e8-c2db044c784a | -12.99109 | -62.64814 | 2024-10-03 06:10:00 | NOAA-21 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 5.7 |
| a39367a3-379b-30b4-b041-66995a33ba71 | -12.7886 | -62.50656 | 2024-10-03 06:10:00 | NOAA-21 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 7.1 |
| ed45fd76-4286-36b3-bc7e-425c627a215a | -12.78873 | -62.50758 | 2024-10-03 06:10:00 | NOAA-21 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 4704490a-28ac-3b93-a351-46f0eb635ba4 | -12.7891 | -62.50243 | 2024-10-03 06:10:00 | NOAA-21 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 5.6 |
| df91eff1-f27e-3799-80ab-9eb0b98504ca | -12.7892 | -62.50345 | 2024-10-03 06:10:00 | NOAA-21 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 6be3175b-47f9-3ee3-b981-0539c3bac559 | -12.79502 | -62.50413 | 2024-10-03 06:10:00 | NOAA-21 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 13.5 |
| 0829ba76-ab9f-3fc0-9b65-5ec7e79ac857 | -12.80036 | -62.50903 | 2024-10-03 06:10:00 | NOAA-21 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 13.5 |
| 759c1571-8b0c-3d4a-a9c6-3ec43035eb6e | -12.80083 | -62.50484 | 2024-10-03 06:10:00 | NOAA-21 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 13.5 |
| 70d30492-ea7f-352e-8587-3aec841fabdf | -12.80665 | -62.5056 | 2024-10-03 06:10:00 | NOAA-21 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 65602c5a-d3e1-35d8-9bdb-c708a0f0f026 | -12.81487 | -62.48538 | 2024-10-03 06:10:00 | NOAA-21 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 3d573151-9a7a-3acd-b47d-28851a86f097 | -12.81536 | -62.48118 | 2024-10-03 06:10:00 | NOAA-21 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 4.2 |
| a18c3386-e9fa-34b3-abe7-e170db051e07 | -12.82118 | -62.48193 | 2024-10-03 06:10:00 | NOAA-21 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 6.8 |
| b5c055fe-c62f-3372-a845-691a8dce628f | -12.82598 | -62.59262 | 2024-10-03 06:10:00 | NOAA-21 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 1c1cf81b-27ab-371d-b495-ce53189a0c3d | -12.827 | -62.48271 | 2024-10-03 06:10:00 | NOAA-21 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 6.8 |
| d86d5171-9398-39e1-9197-589c09649bcf | -12.82748 | -62.47851 | 2024-10-03 06:10:00 | NOAA-21 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 4a9faaf5-de1e-3e35-a1f0-fdaa6fa110bc | -12.83281 | -62.48351 | 2024-10-03 06:10:00 | NOAA-21 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 83ee2733-4e7b-38e3-9372-df4b5f25a2e4 | -12.8333 | -62.47934 | 2024-10-03 06:10:00 | NOAA-21 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 5.2 |
| d0297912-0c3a-306e-9a96-9b3eb259cc45 | -12.85856 | -62.46557 | 2024-10-03 06:10:00 | NOAA-21 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 9a039005-884f-306f-be0d-61d3ce283fd8 | -12.85906 | -62.46138 | 2024-10-03 06:10:00 | NOAA-21 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 391dbf91-68b8-3dc3-981e-bac653033d42 | -12.86489 | -62.4621 | 2024-10-03 06:10:00 | NOAA-21 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 3c4f3ab6-c0b1-3b43-b34b-7b7c4cc99a4e | -12.86538 | -62.45791 | 2024-10-03 06:10:00 | NOAA-21 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 02fdc2d0-c1cb-3486-a2b7-ac9d6aac22a8 | -12.87011 | -62.46418 | 2024-10-03 06:10:00 | NOAA-21 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 6.9 |
| 1ba21f85-0993-3d18-87af-4c4ccce7cacb | -12.87057 | -62.45998 | 2024-10-03 06:10:00 | NOAA-21 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 6.9 |
| 5f81c7e2-24be-34f3-9c45-e805a9c53a89 | -12.87073 | -62.46281 | 2024-10-03 06:10:00 | NOAA-21 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 7.4 |
| 0b1742b5-3863-31a9-a2db-6960ea4b0cfd | -12.87122 | -62.45863 | 2024-10-03 06:10:00 | NOAA-21 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 5.2 |
| aa42440a-07e2-35e2-92fc-85dae338d49f | -12.87312 | -62.49019 | 2024-10-03 06:10:00 | NOAA-21 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 608c282d-9e25-3817-bf0a-26d54d5f0b19 | -12.87594 | -62.46496 | 2024-10-03 06:10:00 | NOAA-21 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 6.9 |
| fc26415d-5be8-377f-8b61-e401f11289d9 | -12.87606 | -62.46778 | 2024-10-03 06:10:00 | NOAA-21 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 7.4 |
| dafc21da-2060-323d-a005-696caa6cfb9e | -12.87641 | -62.46076 | 2024-10-03 06:10:00 | NOAA-21 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 6.9 |
| bef641bb-ff5e-386c-9c53-fa092e173493 | -12.87655 | -62.46359 | 2024-10-03 06:10:00 | NOAA-21 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 7.4 |
| 7b5dd0ce-7aca-3861-934f-3e564a614196 | -12.87687 | -62.45656 | 2024-10-03 06:10:00 | NOAA-21 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 8.0 |
| e4da8b1b-61d1-3407-a9f5-2ab89bb826bf | -12.87705 | -62.4594 | 2024-10-03 06:10:00 | NOAA-21 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 5c580eb3-25b9-3c2f-8d4d-4a8e4738a8fc | -12.87755 | -62.45521 | 2024-10-03 06:10:00 | NOAA-21 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 36e6fd49-60cf-3c53-a3bf-118b4a45d61e | -12.88271 | -62.45732 | 2024-10-03 06:10:00 | NOAA-21 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 3.7 |
| bfdeaa0c-96bc-3d95-9485-22b6b96e6e34 | -12.88349 | -62.5537 | 2024-10-03 06:10:00 | NOAA-21 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 264082c9-9f32-3930-8928-ee7f98b5e3be | -12.88397 | -62.5511 | 2024-10-03 06:10:00 | NOAA-21 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 81b39b79-245a-356b-a6ba-9dfa0d5c8cb6 | -12.88399 | -62.54953 | 2024-10-03 06:10:00 | NOAA-21 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 3.0 |
| c0fea6ff-41ac-3cbf-aeb7-6311554d8c0d | -12.88855 | -62.45806 | 2024-10-03 06:10:00 | NOAA-21 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 3.7 |


[Clique aqui para ver as próximas entradas](README196.md)
