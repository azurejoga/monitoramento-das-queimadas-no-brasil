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

## Dados Diários - Página 106

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 28968bd2-bcf7-330b-b0c5-3731d7512fd2 | -16.85372 | -56.71116 | 2024-10-08 04:59:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.8 |
| 10385ba6-9866-35c0-a0ab-57b82546118f | -16.85314 | -56.71478 | 2024-10-08 04:59:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 4.0 |
| c7ab0c86-25b8-372d-97c8-fe6d2cc51452 | -16.85131 | -56.74786 | 2024-10-08 04:59:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.0 |
| c662f4d3-652f-36f3-8a3b-203d2f055220 | -16.85039 | -56.71059 | 2024-10-08 04:59:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.8 |
| 4579c3b3-2a69-3d69-93a0-acacc918c4a7 | -16.84982 | -56.71421 | 2024-10-08 04:59:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 4.0 |
| df6bf6bc-64ec-3565-8e38-5fda497684d4 | -16.84798 | -56.7473 | 2024-10-08 04:59:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.3 |
| d7493e1b-25d2-3290-af8a-65b440e30538 | -16.84763 | -56.70641 | 2024-10-08 04:59:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 6.3 |
| 612a3995-6a2b-3163-a570-f9ea5d26894d | -16.84741 | -56.75091 | 2024-10-08 04:59:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.1 |
| 6728e299-64a0-35db-ba54-4b08412380b6 | -16.84706 | -56.71002 | 2024-10-08 04:59:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 6.3 |
| 1e4a78a8-fe15-3e42-bc6a-b0a3f9210142 | -16.84695 | -56.73227 | 2024-10-08 04:59:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.6 |
| ce012149-31b9-3033-86bf-a2519736592f | -16.84649 | -56.71363 | 2024-10-08 04:59:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.4 |
| 992a3221-98b1-34ce-9a99-50c2d7940696 | -16.84637 | -56.73589 | 2024-10-08 04:59:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.7 |
| e2e9c87b-de86-3f87-b8cf-2b4b262e43d2 | -16.84419 | -56.72809 | 2024-10-08 04:59:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 4.9 |
| 338fbc2b-686b-3c32-b269-dcddf723ba8b | -16.84362 | -56.7317 | 2024-10-08 04:59:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 4.9 |
| 6237bf49-69b7-360e-b444-4392d79b72e3 | -16.84247 | -56.73893 | 2024-10-08 04:59:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.4 |
| eede5f9d-4d90-3fa1-87a0-1196daadc120 | -16.74903 | -56.71166 | 2024-10-08 04:59:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.2 |
| 30a219f0-5539-377c-9dc2-ba957f3d2f70 | -16.74627 | -56.70749 | 2024-10-08 04:59:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.2 |
| b59a7ac5-c308-340c-9185-6742f6a18f7c | -16.7457 | -56.71109 | 2024-10-08 04:59:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.5 |
| 7e387e33-af19-33e8-936a-6c11d6487e4c | -16.74512 | -56.71471 | 2024-10-08 04:59:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.5 |
| 90dbeb58-a879-3a04-85ad-222015aaf8f2 | -16.74237 | -56.71053 | 2024-10-08 04:59:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.5 |
| 1b2b536e-f781-3a41-a712-17deb15142fd | -16.73961 | -56.70634 | 2024-10-08 04:59:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.6 |
| a0c3000d-a020-3b9c-afd9-9b207107657b | -17.16541 | -56.75204 | 2024-10-08 04:59:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 26.5 |
| 582a5ac3-0496-38c4-8e1a-c2f643b63901 | -17.16323 | -56.74424 | 2024-10-08 04:59:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 4.0 |
| e6229624-8f44-3bb5-aaba-206ea2769cd5 | -17.16265 | -56.74786 | 2024-10-08 04:59:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 4.0 |
| 8a1d7ee5-e3c2-3acd-aa24-3e4acb09be7d | -17.16208 | -56.75147 | 2024-10-08 04:59:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 26.5 |
| 440662d9-3fb0-3cf7-b22c-7f1213254175 | -17.15875 | -56.7509 | 2024-10-08 04:59:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.6 |
| a067d65e-db95-392b-b5c1-82630efcfc40 | -17.15818 | -56.75452 | 2024-10-08 04:59:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.6 |
| d01eec5b-bcaa-30d8-8db5-5fbb03f6b798 | -17.1576 | -56.75813 | 2024-10-08 04:59:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 4.0 |
| f1322eab-3740-3b98-9267-96b2867cdc37 | -17.14673 | -56.76782 | 2024-10-08 04:59:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.7 |
| c51ba82d-c369-3e0f-afcd-34115c4317c9 | -17.14615 | -56.77143 | 2024-10-08 04:59:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.4 |
| 1917a86a-5c8b-351e-945a-b09d318317be | -17.14225 | -56.77448 | 2024-10-08 04:59:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.9 |
| f4af9fc3-18bd-3ade-9bff-98bf6fe25b6c | -17.14075 | -56.74079 | 2024-10-08 04:59:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.3 |
| 8ec922ea-0a90-3dbb-b746-f79b09efe748 | -17.13892 | -56.77391 | 2024-10-08 04:59:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.9 |
| d498be31-9423-3f4c-bd91-c3c282959e55 | -17.13835 | -56.77753 | 2024-10-08 04:59:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.2 |
| 01511666-c920-32c9-a3cd-1bdef862bcbc | -17.13778 | -56.78115 | 2024-10-08 04:59:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.2 |
| 8501669f-4bc8-3613-88ef-4b65367a316c | -17.1356 | -56.77334 | 2024-10-08 04:59:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.6 |
| 91183928-562d-3071-8ef0-10b2bd9f547c | -17.00171 | -56.69902 | 2024-10-08 04:59:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.2 |
| 0fc9e2ac-0cda-3753-97ff-dc8a582939ad | -16.99229 | -56.6937 | 2024-10-08 04:59:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.0 |
| 003b0fbc-e11c-3067-a768-99820be54f3e | -16.99162 | -56.71956 | 2024-10-08 04:59:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.7 |
| fd65b4eb-d17c-3a89-a5fe-7f7319970339 | -16.99104 | -56.72317 | 2024-10-08 04:59:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.4 |
| adec7618-331e-30dd-9393-922116db776e | -16.99047 | -56.72679 | 2024-10-08 04:59:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.4 |
| 0eebd11a-092a-3cc8-9c02-800fc743045b | -16.9899 | -56.7304 | 2024-10-08 04:59:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.7 |
| 9a84b43b-cb12-32af-a373-265212b0a72b | -16.98896 | -56.69313 | 2024-10-08 04:59:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.0 |
| 5555e1be-a992-33cb-af8c-4bae73219376 | -16.98829 | -56.71899 | 2024-10-08 04:59:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.9 |
| a0760c33-da65-3db5-b6fd-0fe9f741e08e | -16.98782 | -56.70036 | 2024-10-08 04:59:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.2 |
| 7c1d9167-3ade-376e-a3cb-ad112348db9b | -16.98771 | -56.7226 | 2024-10-08 04:59:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.7 |
| 14c4e8ac-d9a2-35e0-9224-04f421c0420a | -16.98714 | -56.72622 | 2024-10-08 04:59:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.7 |
| 3ed88d90-7d86-3e3c-bb6c-933480902308 | -16.98657 | -56.72983 | 2024-10-08 04:59:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.5 |
| eaa3500d-9450-30c3-938e-65c68e6f292f | -16.986 | -56.73344 | 2024-10-08 04:59:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.5 |
| 50a87121-721a-3daa-9a7b-e03dc51000bd | -16.98439 | -56.72203 | 2024-10-08 04:59:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.7 |
| bb602332-7c0b-3b86-baa1-6dad7fee16c6 | -16.98381 | -56.72565 | 2024-10-08 04:59:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.7 |
| 63ee2bc1-e70c-32d0-a912-c7bb16e9d8b2 | -16.98324 | -56.72926 | 2024-10-08 04:59:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.5 |
| e62a639a-637d-373c-8ca2-b0186be96991 | -16.98267 | -56.73287 | 2024-10-08 04:59:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.5 |
| f8b58d1a-9df8-33a3-aaab-9d647d41e4a4 | -16.98209 | -56.73649 | 2024-10-08 04:59:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.7 |
| 39775c27-392a-3a1e-b4b2-3741503512cf | -16.98106 | -56.72146 | 2024-10-08 04:59:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 0.8 |
| 69f916f8-ef3c-343d-b132-df7c0c8de8a8 | -16.96649 | -56.74866 | 2024-10-08 04:59:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.9 |
| ef07eb75-f29b-39fd-960b-930c2d913110 | -16.96591 | -56.75228 | 2024-10-08 04:59:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.9 |
| af92d11f-9a46-3d03-af8b-756beea4ab59 | -16.96465 | -56.78176 | 2024-10-08 04:59:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.5 |
| 56ed07c9-3d65-343d-95eb-190c61ff0657 | -16.96144 | -56.75894 | 2024-10-08 04:59:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.8 |
| b05e53b8-3dd3-304e-8ffd-a16b03e9c391 | -16.96132 | -56.7812 | 2024-10-08 04:59:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.5 |
| 8cb73427-b88a-30d0-b704-042ed45eadac | -16.96075 | -56.78481 | 2024-10-08 04:59:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.6 |
| 5f807979-730d-3e7c-af5e-54b9b3a515a5 | -16.95811 | -56.75837 | 2024-10-08 04:59:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.8 |
| 7f5344ab-c688-386c-9b90-3c9bd07553cf | -16.95753 | -56.76198 | 2024-10-08 04:59:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.9 |
| 1d02bdfa-ed78-3a73-a0ff-5f87bec12137 | -16.95696 | -56.76559 | 2024-10-08 04:59:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.9 |
| 097710ac-c48e-340f-8b0e-ce694594e1d6 | -16.95524 | -56.77644 | 2024-10-08 04:59:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.2 |
| cc1edd93-497c-3fc3-ab93-d701a150e43c | -16.95466 | -56.78006 | 2024-10-08 04:59:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.2 |
| 4385d500-a108-3ebb-afdb-e284ffdbf57e | -16.95409 | -56.78367 | 2024-10-08 04:59:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.5 |
| 7baecb73-ad34-3505-98e6-73b0f1d2c226 | -18.89749 | -57.75027 | 2024-10-08 04:59:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.2 |
| 72abdf93-fcdf-30bd-8664-6af43c8aa2a2 | -18.88687 | -57.75217 | 2024-10-08 04:59:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.5 |
| 1bc84c11-86b2-3ab5-8b08-dac9054f1430 | -18.88412 | -57.74789 | 2024-10-08 04:59:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.3 |
| 00c058af-6b02-396e-adad-d1a69941071f | -18.88352 | -57.75157 | 2024-10-08 04:59:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.5 |
| b620db67-b225-324d-9b5e-a81bbf693837 | -18.87528 | -57.73872 | 2024-10-08 04:59:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.7 |
| 26a5d77c-fc40-3dd7-85e7-58b32549b87b | -18.87468 | -57.7424 | 2024-10-08 04:59:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.3 |
| 8ea6ff98-b95d-3da2-9a8e-12cf258d6e54 | -18.87409 | -57.7461 | 2024-10-08 04:59:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.3 |
| 6011e953-aa44-3fd8-9673-d1fc62b27fe4 | -18.7307 | -57.29155 | 2024-10-08 04:59:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.2 |
| b1d767f4-c6dc-3860-9629-745883429380 | -18.72737 | -57.29096 | 2024-10-08 04:59:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.2 |
| c74b96df-60b5-381a-a696-e7bbbc12ee3c | -18.72579 | -57.2794 | 2024-10-08 04:59:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.1 |
| 6a2dbd4d-632d-3565-a4bd-b7704376abd5 | -18.7252 | -57.28306 | 2024-10-08 04:59:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.1 |
| 81301f58-d921-3656-ac1d-5ead99d7f265 | -18.72304 | -57.27516 | 2024-10-08 04:59:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.8 |
| a4f1ec28-3e7a-3086-9508-e090a4721f2f | -18.72246 | -57.27882 | 2024-10-08 04:59:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.1 |
| 03f9154e-58ff-37ec-9d40-af3c525ff793 | -18.72187 | -57.28248 | 2024-10-08 04:59:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.1 |
| 902b0ee6-93f1-309a-aae3-b69cbc6a4d15 | -18.72129 | -57.28613 | 2024-10-08 04:59:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.6 |
| 8d58c196-256b-35e2-bcc0-6e4126919a3b | -18.71971 | -57.27458 | 2024-10-08 04:59:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.3 |
| ffe70f76-3c17-350f-8956-0157eb4eab41 | -18.71854 | -57.28189 | 2024-10-08 04:59:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.3 |
| d0fd312c-6b20-39cf-aae3-1e64f9b9216a | -18.71696 | -57.27034 | 2024-10-08 04:59:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.3 |
| dcba6e9c-f22a-3f90-9b73-0c2b5c41acb3 | -18.71638 | -57.27399 | 2024-10-08 04:59:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.3 |
| 25c8c1d9-a1db-32c3-8265-49e57b89115a | -18.71463 | -57.28497 | 2024-10-08 04:59:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.5 |
| cc584721-0a21-3dbf-8329-e8190aabda1e | -18.71363 | -57.26975 | 2024-10-08 04:59:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 0.8 |
| 7490ea5d-bec1-3f25-809e-0b3e1bfa6b88 | -18.70034 | -57.23361 | 2024-10-08 04:59:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 0.7 |
| 62a8506b-7947-3426-9697-df32eb04cacb | -18.69701 | -57.23302 | 2024-10-08 04:59:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 0.7 |
| cf2d97d4-9632-37ab-8b46-2df73d4025ca | -18.65704 | -57.22602 | 2024-10-08 04:59:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.0 |
| 01e904fc-220e-35ab-80b6-b59a04d33255 | -18.65371 | -57.22544 | 2024-10-08 04:59:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 0.6 |
| c7271660-a6fd-3c3d-b373-0775c5725024 | -18.6498 | -57.22851 | 2024-10-08 04:59:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.0 |
| 3a63358b-3563-3a31-978d-757544ee01a0 | -18.6398 | -57.22676 | 2024-10-08 04:59:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.0 |
| 770934b0-f9de-3733-a92c-edf6a6130d93 | -18.63922 | -57.23042 | 2024-10-08 04:59:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.0 |
| 6b67fb4d-731f-3a51-bc73-af3071c63a61 | -18.63875 | -57.29788 | 2024-10-08 04:59:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.8 |
| f3ea3c0c-ae34-3861-8e7d-781fabc61ba2 | -18.63657 | -57.29004 | 2024-10-08 04:59:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.0 |
| 882c87f6-5c21-31a9-9bb4-5ef4775df504 | -18.63647 | -57.22618 | 2024-10-08 04:59:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.0 |
| f497d553-e869-3123-b6c2-977c9ffab5d3 | -18.636 | -57.29364 | 2024-10-08 04:59:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 4.5 |
| 5495191f-1fea-306d-b792-6ae0b898630b | -18.63589 | -57.22983 | 2024-10-08 04:59:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.0 |


[Clique aqui para ver as próximas entradas](README107.md)
