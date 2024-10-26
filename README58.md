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

## Dados Diários - Página 58

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 469af73f-f973-371b-9126-dfbd1f04e863 | -17.87419 | -57.52168 | 2024-10-26 04:21:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 22.2 |
| e4635c64-c36a-30c2-a208-7dc9b416e50f | -17.87399 | -57.51295 | 2024-10-26 04:21:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 13.6 |
| a6d728b9-d608-3fa0-a435-acc16ccb5b09 | -17.87386 | -57.56733 | 2024-10-26 04:21:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.2 |
| 17ada6f9-9a4a-3f38-98c9-ab7afd9ad90e | -17.87323 | -57.5165 | 2024-10-26 04:21:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 28.9 |
| 8b513050-b74a-3871-9fcb-58c8e03e15f2 | -17.87243 | -57.52017 | 2024-10-26 04:21:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 28.9 |
| 1adb704e-9e26-308a-afbe-e57451acc09e | -17.87005 | -57.51376 | 2024-10-26 04:21:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 13.1 |
| 9c184052-4a7f-3e57-a7ad-350de4e2594a | -17.86928 | -57.51744 | 2024-10-26 04:21:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 22.2 |
| f6c67c17-483c-3046-89a1-8fed8a5af944 | -17.86852 | -57.52109 | 2024-10-26 04:21:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 22.2 |
| 1d2998e0-a655-35f6-b2c8-c5bbde477732 | -17.86824 | -57.57795 | 2024-10-26 04:21:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.1 |
| bb02ca24-4a56-3f07-80d2-cdceef533161 | -17.86779 | -57.5246 | 2024-10-26 04:21:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 8.8 |
| 7312f4b2-4d21-322a-9019-b196d825e020 | -17.86762 | -57.51561 | 2024-10-26 04:21:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 11.9 |
| 80c399d9-0f07-3de9-b58d-8621b47521cd | -17.86751 | -57.58142 | 2024-10-26 04:21:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.1 |
| 381ca670-7a5d-3f18-aeda-8176554906f9 | -17.86682 | -57.51932 | 2024-10-26 04:21:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 11.9 |
| cbd1769e-ac1b-37f3-b394-e58c000689af | -17.86604 | -57.57662 | 2024-10-26 04:21:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.3 |
| 1ba72ad0-6ef5-310c-b938-4a5ce29b5bc9 | -17.86604 | -57.52293 | 2024-10-26 04:21:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 10.2 |
| 8d442bf6-390d-3e58-abaf-3306e0ad0c22 | -17.86535 | -57.57983 | 2024-10-26 04:21:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.3 |
| bd506bc4-ef0f-3358-afba-1dd4954680ae | -17.86527 | -57.52648 | 2024-10-26 04:21:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 10.2 |
| a11e33a7-c6f9-3e48-898b-248568e1b44c | -17.86374 | -57.51628 | 2024-10-26 04:21:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 10.4 |
| e0242774-e68e-3c19-9747-bbc9eed5d57c | -17.86294 | -57.52009 | 2024-10-26 04:21:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 10.4 |
| cfdf44a4-ff4c-3e16-a25f-06c4bb5ac534 | -17.86218 | -57.5237 | 2024-10-26 04:21:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 9.7 |
| a6a18853-56aa-3bdd-be9c-8cfc4ed1846b | -17.86143 | -57.52732 | 2024-10-26 04:21:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 9.7 |
| 701d07cd-e608-3a5a-a76a-10eae7643573 | -17.86069 | -57.53082 | 2024-10-26 04:21:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 5.9 |
| a965ab96-3e63-3fb0-9258-36239b0d879d | -17.86045 | -57.52193 | 2024-10-26 04:21:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 10.2 |
| 9a48bb1e-92dd-3c88-8667-d21b0eabb34e | -17.85966 | -57.5256 | 2024-10-26 04:21:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 10.2 |
| 12f5c91f-26ae-3622-a628-f097668463e6 | -17.85887 | -57.52924 | 2024-10-26 04:21:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 8.2 |
| 9b869752-44db-3ba0-bbe2-9e1324b4ac8c | -17.85812 | -57.53272 | 2024-10-26 04:21:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 8.2 |
| ace9b16c-f1eb-3bd9-b75d-38d5900a65dc | -17.85668 | -57.60549 | 2024-10-26 04:21:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.7 |
| 65298ff1-9375-3e66-a80c-b87626e8e3c9 | -17.85463 | -57.60244 | 2024-10-26 04:21:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 5.1 |
| 4a8dcf7f-7b85-3229-af6f-e3fd94758bcd | -17.85116 | -57.60406 | 2024-10-26 04:21:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.7 |
| af03137d-e31f-32fa-aa7d-671abbb3f640 | -17.86127 | -57.51819 | 2024-10-26 04:21:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 11.9 |
| 9dcd12d1-14a7-3225-92c6-a702e252cf02 | -17.85582 | -57.5264 | 2024-10-26 04:21:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 9.7 |
| 0df7ce5b-693f-3c5e-8ce3-49420267c313 | -17.85504 | -57.53013 | 2024-10-26 04:21:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 5.9 |
| 6761b02d-6756-3cb2-aff6-5a6d18f4abb1 | -17.85039 | -57.49714 | 2024-10-26 04:21:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.9 |
| 71cc30f6-26fa-3fb2-98e9-5682df13108a | -17.84959 | -57.50094 | 2024-10-26 04:21:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.9 |
| 5aeaeb4d-e272-3245-ac0f-65629ee79ef6 | -17.84408 | -57.49963 | 2024-10-26 04:21:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 4.4 |
| e0e18db8-a705-3485-b625-6558023659e7 | -17.84328 | -57.50345 | 2024-10-26 04:21:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.1 |
| d5ab493f-2385-365b-8512-8015ddde1bc7 | -17.83144 | -57.50465 | 2024-10-26 04:21:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 4.1 |
| 31a7fe35-c001-322a-93ce-d3194ab2c1a5 | -17.83063 | -57.50846 | 2024-10-26 04:21:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.8 |
| 03f25e5a-ef1a-3753-a34a-492a3a2cb23c | -17.82754 | -57.49574 | 2024-10-26 04:21:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 4.0 |
| 6f511ad1-a2b8-3cb7-bd76-a7e975c6604c | -17.82673 | -57.49955 | 2024-10-26 04:21:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 4.1 |
| c6054398-4434-3c68-aea0-ab3e592b55b4 | -17.82592 | -57.50335 | 2024-10-26 04:21:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 4.1 |
| e00bc99e-e594-3846-8ac6-e49b39735ff3 | -17.82512 | -57.50717 | 2024-10-26 04:21:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.8 |
| 788203ff-741c-3679-98c3-9b40c4ffbfcf | -17.82121 | -57.49825 | 2024-10-26 04:21:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 4.4 |
| 9db52db6-f2f3-3ed5-b5f0-7e1fa0bed970 | -17.81878 | -57.50968 | 2024-10-26 04:21:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.1 |
| 7a43c104-b570-3812-8762-b28f13a12b8f | -17.81472 | -57.52881 | 2024-10-26 04:21:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.2 |
| 3c03d4f8-12ed-3e70-8e74-33c12c50597d | -17.81164 | -57.51603 | 2024-10-26 04:21:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.1 |
| 97efed2e-0f75-3342-acd9-75e99bcd7b0e | -17.8092 | -57.5275 | 2024-10-26 04:21:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.2 |
| 0f4d8372-ca5f-33b8-a74c-9819cdf9a772 | -17.80612 | -57.51473 | 2024-10-26 04:21:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.6 |
| f7606873-02a5-3255-9644-c12555b78869 | -17.80078 | -57.59435 | 2024-10-26 04:21:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.4 |
| b54ebaf1-a6c2-3163-a350-4fd286ac2f82 | -17.7944 | -57.59692 | 2024-10-26 04:21:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.9 |
| 52607749-daa6-3de3-8816-0dd6a637e0b6 | -17.78885 | -57.5956 | 2024-10-26 04:21:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.7 |
| 5f873fa4-ba1c-37ad-b97a-041aa58c2c9f | -17.78802 | -57.59948 | 2024-10-26 04:21:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.7 |
| 1edc1070-ce52-3a12-9b1b-c290717bd361 | -17.7833 | -57.59428 | 2024-10-26 04:21:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.7 |
| b53cc4d8-e359-36d6-b294-d87ec1fba2ed | -17.78247 | -57.59815 | 2024-10-26 04:21:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.7 |
| bd438bb2-f92b-3d48-af4c-2692b8ec4a2f | -17.77941 | -57.5114 | 2024-10-26 04:21:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.8 |
| db6a3393-75ea-3bbd-a2a7-b55470ea52d9 | -17.77769 | -57.51203 | 2024-10-26 04:21:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.4 |
| 43adcb56-8a7b-39fa-a150-cc1d452c0673 | -17.7722 | -57.59168 | 2024-10-26 04:21:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.3 |
| 5a03a6c9-4962-3800-b826-bc5759f5bfa6 | -17.77136 | -57.59554 | 2024-10-26 04:21:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.3 |
| 70470e47-73e8-33ba-a90b-b27e31faf9d0 | -17.93571 | -57.54949 | 2024-10-26 04:21:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.1 |
| d9d0d9a1-a7e3-3131-adee-43101350a4d4 | -17.9351 | -57.55237 | 2024-10-26 04:21:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.1 |
| f604b032-2777-36be-8d38-53e33abd78ed | -17.93444 | -57.55545 | 2024-10-26 04:21:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 4.7 |
| c28ac31e-f836-3fb6-961c-d41fa0094619 | -17.93376 | -57.53137 | 2024-10-26 04:21:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 6.1 |
| 545413de-2564-31fc-a75a-16e39d4ff34c | -17.93308 | -57.53457 | 2024-10-26 04:21:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 6.2 |
| 899a9b36-b607-3362-9007-0691a6894f06 | -17.9324 | -57.53779 | 2024-10-26 04:21:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 6.2 |
| 96b43470-83e8-3c6b-b5f4-56cc946d6129 | -17.93165 | -57.5413 | 2024-10-26 04:21:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 7.3 |
| 9513c4d3-fa14-3444-ae08-7a182046dea3 | -17.93108 | -57.57134 | 2024-10-26 04:21:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 5.3 |
| e1ad8ee5-46a7-3796-99de-fccc78b78d0e | -17.93087 | -57.54499 | 2024-10-26 04:21:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 7.3 |
| d32e4a93-7e91-3f38-a48f-831ef95ca4c0 | -17.92946 | -57.55159 | 2024-10-26 04:21:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 6.3 |
| 0582d5a7-325a-3dc7-9971-c7587f4c2c14 | -17.92842 | -57.52924 | 2024-10-26 04:21:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 6.1 |
| d2420e9b-4a82-3ccd-be8d-7e3c20572d66 | -17.92775 | -57.53238 | 2024-10-26 04:21:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 6.2 |
| de9a3521-5ee0-3139-9276-44f594640d77 | -17.92488 | -57.57317 | 2024-10-26 04:21:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.2 |
| de0940dd-86b0-3ab3-8232-522c79c9af32 | -17.92307 | -57.52718 | 2024-10-26 04:21:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 9.8 |
| 66c22d4e-6771-32c2-baf0-2dd70ee712e1 | -17.92236 | -57.53049 | 2024-10-26 04:21:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 9.0 |
| c68c60f0-82a4-33b3-a79e-2b67ee148fd0 | -17.9205 | -57.56648 | 2024-10-26 04:21:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.2 |
| 3335a2f0-6209-39da-99b2-3849036bbf49 | -17.9177 | -57.52518 | 2024-10-26 04:21:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 9.8 |
| 25976caa-b787-3089-adbd-cf06e898a624 | -17.91701 | -57.52844 | 2024-10-26 04:21:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 9.0 |
| bb88c606-bfb8-3550-8495-24dd53c17c5c | -17.91566 | -57.56192 | 2024-10-26 04:21:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.2 |
| c654fcc1-7c2d-36bb-846e-f472543e1dff | -17.91553 | -57.53533 | 2024-10-26 04:21:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 4.9 |
| 4f26ab53-68b8-3740-b6f5-e9f09d23dd5c | -17.91485 | -57.56573 | 2024-10-26 04:21:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 6.0 |
| 5b48b576-6682-33c7-9edc-bf4673d28a08 | -17.91089 | -57.52995 | 2024-10-26 04:21:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 6.7 |
| 3a77e377-69d3-3d55-90c5-ace1847b7fec | -17.90983 | -57.5621 | 2024-10-26 04:21:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.2 |
| 5c4d8ac3-ad2e-300c-b0cc-121ecdfcaafc | -17.90726 | -57.51986 | 2024-10-26 04:21:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.4 |
| aeaeed68-fdbc-36df-8377-1a09e5bae8c2 | -17.90664 | -57.52275 | 2024-10-26 04:21:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.4 |
| 3c0f49ba-9913-383c-9fa5-7896ffeea39f | -17.90226 | -57.51615 | 2024-10-26 04:21:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 8.2 |
| bea8f83b-496b-3b5b-89ae-674ec8833427 | -17.90167 | -57.51893 | 2024-10-26 04:21:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 6.9 |
| f2d82a59-4a8d-36e5-bf5b-b16c3563330c | -17.89866 | -57.53297 | 2024-10-26 04:21:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.9 |
| c7dc3d57-f079-3895-b12a-8873b3d7fed8 | -17.89616 | -57.51759 | 2024-10-26 04:21:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 6.9 |
| ee117a8f-b569-3f9d-877f-8819a45f57aa | -17.89378 | -57.52868 | 2024-10-26 04:21:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 7.7 |
| 26e31fd4-ca1b-3f46-835a-a6f92be4758b | -17.89297 | -57.53244 | 2024-10-26 04:21:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.9 |
| fea383a9-14b3-3cf9-8139-3de3e139c958 | -17.89111 | -57.51415 | 2024-10-26 04:21:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.4 |
| e50bcac6-6311-30e7-a937-05ed196d17c9 | -17.89041 | -57.51742 | 2024-10-26 04:21:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 6.3 |
| 86ab98e2-33c1-3fa6-b37b-f0d2f784adeb | -18.11353 | -57.30254 | 2024-10-26 04:21:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.3 |
| 0fc7aca5-49a6-39f9-ac6c-1b38de15226c | -18.11276 | -57.30621 | 2024-10-26 04:21:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.7 |
| d372d7fa-8273-3fb2-9620-ae9e304c591b | -18.11118 | -57.2866 | 2024-10-26 04:21:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.6 |
| 4214358c-e8fa-3c6a-ac8d-502f192f0eeb | -18.10653 | -57.28166 | 2024-10-26 04:21:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.2 |
| e0567794-5721-3cfc-9d43-bccfd0b49257 | -18.10577 | -57.28531 | 2024-10-26 04:21:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.2 |
| a0edd21d-0388-3e3b-ac07-eedb2ec831ed | -18.105 | -57.28897 | 2024-10-26 04:21:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 7.0 |
| 471fbaae-4251-3b4d-9f47-a25cc624a000 | -18.10118 | -57.36149 | 2024-10-26 04:21:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 5.3 |
| abe3ffb2-ab5e-3de7-8356-cf8b352077b4 | -18.10041 | -57.36517 | 2024-10-26 04:21:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 6.7 |
| 2a847ca9-4cea-378a-b362-dfabf06b30d5 | -18.10035 | -57.28403 | 2024-10-26 04:21:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.2 |


[Clique aqui para ver as próximas entradas](README59.md)
