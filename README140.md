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

## Dados Diários - Página 140

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 2aeb3744-86be-3fdd-9351-12a50a767b4f | -16.41815 | -55.94601 | 2024-10-09 04:40:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.6 |
| 57bdf1ea-c5b2-33bd-9791-1a6953260c11 | -16.41697 | -55.93061 | 2024-10-09 04:40:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 5.0 |
| 8d48caa5-30e1-32e9-8107-ee5d6c4c7ada | -16.41609 | -55.9355 | 2024-10-09 04:40:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 5.0 |
| ca802845-24c7-3fdc-9dbc-a499a10040e5 | -16.41573 | -57.32665 | 2024-10-09 04:40:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.0 |
| 68a87718-30d9-3133-843c-f3dc9d7e4df9 | -16.4152 | -55.94039 | 2024-10-09 04:40:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 5.9 |
| 8b1f7fde-9a21-3645-8236-1e020b1024aa | -16.41432 | -55.94528 | 2024-10-09 04:40:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 5.9 |
| c2b4236c-fdfd-31d4-a875-0606ad7f79de | -16.41226 | -55.93476 | 2024-10-09 04:40:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 5.0 |
| 356e6519-23db-31dc-a55c-22afa09b5bb8 | -16.41138 | -55.93965 | 2024-10-09 04:40:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 5.9 |
| 2a2890a7-a727-3b8d-aba9-e07e6458c772 | -16.41084 | -57.32975 | 2024-10-09 04:40:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.5 |
| e832fe6f-7641-3dce-be5d-c71afe7338d8 | -16.41049 | -55.94456 | 2024-10-09 04:40:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 5.9 |
| 65c1eb65-bd45-3632-9c1e-8fb1f240cf45 | -16.41034 | -55.9376 | 2024-10-09 04:40:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 7.5 |
| b4936430-4551-3d27-9642-c42c87a62971 | -16.4096 | -55.94946 | 2024-10-09 04:40:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.6 |
| fa00edf6-8dcb-3e50-ad86-757bc97a9f34 | -16.40949 | -55.94251 | 2024-10-09 04:40:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 4.9 |
| 35a7a0fe-e260-3db0-9a03-c4f9501927eb | -16.39524 | -57.69764 | 2024-10-09 04:40:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.2 |
| b3d9acde-1f54-38f7-acb7-184227ea3c33 | -16.39447 | -57.70187 | 2024-10-09 04:40:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.2 |
| 01c68eba-a270-3972-bb75-4824174453b1 | -16.39178 | -57.69248 | 2024-10-09 04:40:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.3 |
| 86ff47c5-cc79-348d-89b5-d3ec0ab23253 | -16.39099 | -57.69674 | 2024-10-09 04:40:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.2 |
| a737d413-d564-3e56-adbd-fbab38c25959 | -16.39021 | -57.70099 | 2024-10-09 04:40:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.2 |
| 475fe456-db7f-3bd1-b5c1-2c79e426918b | -16.38944 | -57.7052 | 2024-10-09 04:40:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.8 |
| 3aef71a7-60c6-3aea-90aa-47031f090f37 | -16.38596 | -57.70009 | 2024-10-09 04:40:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.6 |
| 0736bd2c-ce18-31dd-8146-94151b003767 | -16.38518 | -57.70433 | 2024-10-09 04:40:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.1 |
| 327eb967-805c-3d1b-b910-d8e3b8bee49f | -16.38441 | -57.70846 | 2024-10-09 04:40:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.1 |
| 69fe6b39-058f-32c9-96f7-52627e1333e1 | -16.38015 | -57.70759 | 2024-10-09 04:40:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.1 |
| 1912b6b4-bf45-32e2-98f0-670e08d6d0cb | -16.37938 | -57.71175 | 2024-10-09 04:40:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.4 |
| a847ecbb-4f4d-3b87-9adb-3daacd804beb | -16.35571 | -55.97779 | 2024-10-09 04:40:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 3.2 |
| 4a8dadee-49e0-3e15-af30-adf5220b7545 | -16.21711 | -54.99605 | 2024-10-09 04:40:00 | NPP-375D | JUSCIMEIRA | MATO GROSSO | Brasil | 5105200 | 51 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 65993205-ec56-3d92-b51c-e33821decf65 | -16.21634 | -55.00049 | 2024-10-09 04:40:00 | NPP-375D | JUSCIMEIRA | MATO GROSSO | Brasil | 5105200 | 51 | 33 | nan | nan | nan | Cerrado | 4.7 |
| aa1b1fbf-4223-355e-bffd-4ed37ffe8000 | -16.21345 | -54.99539 | 2024-10-09 04:40:00 | NPP-375D | JUSCIMEIRA | MATO GROSSO | Brasil | 5105200 | 51 | 33 | nan | nan | nan | Cerrado | 6.6 |
| a37893f3-3a21-3974-918a-044409ed0c47 | -16.16579 | -55.93716 | 2024-10-09 04:40:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 3.1 |
| ac977da6-b6dd-3ba4-bc28-89eea4ae0b60 | -16.16403 | -57.41936 | 2024-10-09 04:40:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 61259413-1d15-3464-a0ac-5ce70d41a08b | -16.16195 | -55.93641 | 2024-10-09 04:40:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.9 |
| 72d1058c-66b5-35a7-8f14-db73213d8be8 | -16.15984 | -57.41843 | 2024-10-09 04:40:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | 7.4 |
| 4305bbc6-9fb8-3bfa-917f-e4fad6b78408 | -16.1581 | -55.93574 | 2024-10-09 04:40:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.9 |
| 9ec19060-171b-307d-984a-91b019d8e93c | -16.15163 | -57.60323 | 2024-10-09 04:40:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.3 |
| 500b242e-00c1-3ff3-b5cc-3282ea0a835b | -16.14061 | -57.40825 | 2024-10-09 04:40:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 0115e5b7-366a-3048-8911-a4a1899d23f5 | -16.14022 | -57.40692 | 2024-10-09 04:40:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 6d91eb8b-0d1c-3a28-b1b1-6bd678d8d73f | -16.13997 | -57.41172 | 2024-10-09 04:40:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 323830bb-0e5e-33f5-a102-093c2e1f5e2a | -16.13958 | -57.41034 | 2024-10-09 04:40:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | 6.5 |
| ece5e5b8-f507-3004-aebe-1def05a2a665 | -16.13579 | -57.41077 | 2024-10-09 04:40:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 9dffb692-ea07-359c-9276-dc7c2f1af7f2 | -16.13539 | -57.40945 | 2024-10-09 04:40:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 40750c01-7313-3626-a569-7ae9bc1e51bd | -16.12983 | -57.55496 | 2024-10-09 04:40:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.9 |
| 4d8c1767-665f-3c19-b079-8275ffa18b44 | -16.12913 | -57.55869 | 2024-10-09 04:40:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.7 |
| dbe84e1e-1afd-315d-9634-f1634d01760c | -16.12811 | -55.85906 | 2024-10-09 04:40:00 | NPP-375D | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 2.3 |
| 3d992c53-7c75-31c1-b668-9b522edb47c8 | -16.12724 | -55.86396 | 2024-10-09 04:40:00 | NPP-375D | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 1.7 |
| 9087f29c-49d1-3665-a605-edc77468ffe4 | -16.12517 | -55.85342 | 2024-10-09 04:40:00 | NPP-375D | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 2.3 |
| 0ee45ce7-b891-3acf-9e50-b6b6cebe6ff8 | -16.12429 | -55.85831 | 2024-10-09 04:40:00 | NPP-375D | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 2.3 |
| 3b78363a-1c3f-3dbc-825e-ca89d7c6ce74 | -15.97324 | -55.62016 | 2024-10-09 04:40:00 | NPP-375D | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| ffbd17e1-54cf-3948-b572-e8838d470ede | -15.96865 | -59.08752 | 2024-10-09 04:40:00 | NPP-375D | PORTO ESPERIDIÃO | MATO GROSSO | Brasil | 5106828 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| c1e48b2f-1c14-3156-ae1f-ca2c63b2c827 | -15.96765 | -59.09262 | 2024-10-09 04:40:00 | NPP-375D | PORTO ESPERIDIÃO | MATO GROSSO | Brasil | 5106828 | 51 | 33 | nan | nan | nan | Amazônia | 5.2 |
| b3e821f9-d12b-3719-9f34-c52587787366 | -15.9547 | -57.2137 | 2024-10-09 04:40:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 7123a3ef-21e9-375f-9fd5-22236d6c6292 | -15.95466 | -57.21621 | 2024-10-09 04:40:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 78697681-741a-3762-ba94-cb9152ecca28 | -15.95402 | -57.21748 | 2024-10-09 04:40:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 112f5beb-f4a6-36e5-97bb-bfd453761444 | -15.95394 | -57.22002 | 2024-10-09 04:40:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| c4f96bbd-43a2-34b2-aae5-254717b3e5e6 | -15.95331 | -57.22137 | 2024-10-09 04:40:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| ba5db9b3-f868-3549-9faf-f48bd7058bfb | -15.95124 | -57.21144 | 2024-10-09 04:40:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| a2cdeafd-0319-3168-b165-df6aaa46d1f9 | -15.95057 | -57.21266 | 2024-10-09 04:40:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | 2.9 |
| b3b12805-e864-357e-872f-9cff94d2d4d1 | -15.95053 | -57.2152 | 2024-10-09 04:40:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 38db19c4-110c-35e5-89c3-188f37092aac | -15.94987 | -57.21652 | 2024-10-09 04:40:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | 2.9 |
| e9674275-5da7-30d7-8856-014d52e5c407 | -15.94979 | -57.21912 | 2024-10-09 04:40:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| cc062ac4-c69a-3024-aee4-6036e65107e0 | -15.94916 | -57.22047 | 2024-10-09 04:40:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 5255bb40-19b1-3121-a246-047fd60faaf5 | -15.94904 | -57.2231 | 2024-10-09 04:40:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 268df17d-7bc5-3aca-8905-313a03ed62b3 | -15.94573 | -57.21556 | 2024-10-09 04:40:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 8fc6ad58-7bcd-3e54-90c3-c492f1195d19 | -15.945 | -57.21959 | 2024-10-09 04:40:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 5eae9b0d-32f7-3357-8f17-4f23eac0d598 | -15.94226 | -57.21092 | 2024-10-09 04:40:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 31dcf951-c1df-395d-9362-4879535b0827 | -15.94156 | -57.21483 | 2024-10-09 04:40:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 21140787-50f6-3b2c-b6dd-1306a605f904 | -15.94083 | -57.21885 | 2024-10-09 04:40:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 0f8b51e5-286b-3de6-bc49-fd86c73d804f | -15.93808 | -57.21019 | 2024-10-09 04:40:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 8def882f-2a22-3de6-9b3d-df601af8cda5 | -15.93737 | -57.21412 | 2024-10-09 04:40:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 79a42994-a572-3e85-a96d-5e14cec44ff5 | -15.92962 | -55.01085 | 2024-10-09 04:40:00 | NPP-375D | JACIARA | MATO GROSSO | Brasil | 5104807 | 51 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 1a2a10ec-dda3-3d07-8571-ec99825ab5d0 | -15.92519 | -55.01447 | 2024-10-09 04:40:00 | NPP-375D | JACIARA | MATO GROSSO | Brasil | 5104807 | 51 | 33 | nan | nan | nan | Cerrado | 0.3 |
| 96e00f63-38d1-3ca5-8c64-874b68579f85 | -15.92153 | -55.01378 | 2024-10-09 04:40:00 | NPP-375D | JACIARA | MATO GROSSO | Brasil | 5104807 | 51 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 14d46fe0-2199-3ee8-8d8e-d125ccf0062d | -15.92077 | -55.01807 | 2024-10-09 04:40:00 | NPP-375D | JACIARA | MATO GROSSO | Brasil | 5104807 | 51 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 8c205a73-7a97-3bfc-9f08-5040bd28212a | -15.91899 | -55.01553 | 2024-10-09 04:40:00 | NPP-375D | JACIARA | MATO GROSSO | Brasil | 5104807 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 24a8bbbb-e372-3bd0-a660-3fa448a1aad5 | -15.91785 | -55.01316 | 2024-10-09 04:40:00 | NPP-375D | JACIARA | MATO GROSSO | Brasil | 5104807 | 51 | 33 | nan | nan | nan | Cerrado | 0.4 |
| b30bc490-3cbc-3296-816e-4d8c65ca5583 | -15.81734 | -55.31684 | 2024-10-09 04:40:00 | NPP-375D | CAMPO VERDE | MATO GROSSO | Brasil | 5102678 | 51 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 91706a32-c4c8-38c8-89a4-4475e92971eb | -15.81361 | -55.31614 | 2024-10-09 04:40:00 | NPP-375D | CAMPO VERDE | MATO GROSSO | Brasil | 5102678 | 51 | 33 | nan | nan | nan | Cerrado | 8.6 |
| 590c4e19-48a1-3111-9fa1-4212d7b7b54d | -15.80184 | -59.21127 | 2024-10-09 04:40:00 | NPP-375D | PORTO ESPERIDIÃO | MATO GROSSO | Brasil | 5106828 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 4f7d7b62-8606-33d8-a21f-6178c85f4340 | -15.71693 | -59.44658 | 2024-10-09 04:40:00 | NPP-375D | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d06098ea-20b7-3426-ba11-7d6d1e9fc8c5 | -15.71102 | -59.45119 | 2024-10-09 04:40:00 | NPP-375D | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 71b3b37b-9ee0-3e00-bb10-69b819b09de6 | -15.7101 | -59.37843 | 2024-10-09 04:40:00 | NPP-375D | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 3.6 |
| e5bb3ed8-7d70-3320-a294-aa248f6bc0f5 | -15.70911 | -59.38354 | 2024-10-09 04:40:00 | NPP-375D | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| c7b81408-bdd1-36ce-bc4b-16dedc9b0a44 | -15.70636 | -59.37197 | 2024-10-09 04:40:00 | NPP-375D | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| fa0787b4-fa19-31c2-860b-3a7a72af774e | -15.70534 | -59.37718 | 2024-10-09 04:40:00 | NPP-375D | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| daf372c4-db4b-382c-a646-e7dbcf1d27d0 | -15.70435 | -59.38228 | 2024-10-09 04:40:00 | NPP-375D | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| a87162a0-994c-3e4b-beee-7d641e7a4f1b | -15.70052 | -59.37626 | 2024-10-09 04:40:00 | NPP-375D | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 7314432b-6c7e-3648-8887-3419e9b824e3 | -15.69949 | -59.38154 | 2024-10-09 04:40:00 | NPP-375D | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| a142e492-88de-3812-be05-e4b5419ebd3d | -15.6992 | -59.40868 | 2024-10-09 04:40:00 | NPP-375D | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| adbcc6de-cd0d-3545-9d32-f6c5c32908fd | -15.69811 | -59.41426 | 2024-10-09 04:40:00 | NPP-375D | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 04f256ca-c96d-351a-ae49-f1f391e1f1e6 | -15.69461 | -59.38089 | 2024-10-09 04:40:00 | NPP-375D | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 0ecbe694-cc23-3be7-8926-141f4bbf4fc0 | -15.69432 | -59.40799 | 2024-10-09 04:40:00 | NPP-375D | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| f638f5de-a3cd-3f40-bb8f-1f094c5a52d9 | -15.69361 | -59.38603 | 2024-10-09 04:40:00 | NPP-375D | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| d865312d-7bfe-3a22-bc60-6699da3897bc | -15.69215 | -59.41909 | 2024-10-09 04:40:00 | NPP-375D | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 25b51e28-c770-3a37-ad47-b8d3e5123803 | -15.68942 | -59.40744 | 2024-10-09 04:40:00 | NPP-375D | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| debfa66e-b0a7-319b-90c1-9d459c09472b | -15.68872 | -59.38543 | 2024-10-09 04:40:00 | NPP-375D | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| a4733030-f766-3357-851b-eff15d92326e | -15.68772 | -59.39053 | 2024-10-09 04:40:00 | NPP-375D | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 0ad96542-e193-310b-9b5d-0243a5582877 | -15.68181 | -59.39509 | 2024-10-09 04:40:00 | NPP-375D | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 79be1181-1f5b-3c21-b926-2552a063307b | -15.67693 | -59.39442 | 2024-10-09 04:40:00 | NPP-375D | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 04bf3b53-71a4-361b-bdfa-1820578b08b9 | -15.67593 | -59.39953 | 2024-10-09 04:40:00 | NPP-375D | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 16476798-9fb0-3ac6-9ec1-9ad9e4920803 | -15.67581 | -52.52118 | 2024-10-09 04:40:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 4.6 |
| b14885eb-8152-3bc4-a86e-eb890d02a8f5 | -15.67492 | -59.40465 | 2024-10-09 04:40:00 | NPP-375D | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |


[Clique aqui para ver as próximas entradas](README141.md)
