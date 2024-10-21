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

## Dados Diários - Página 60

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| d8b77ce1-c488-3e3c-b782-69fe16a7f832 | -3.08894 | -54.18409 | 2024-10-21 05:53:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 15.1 |
| f2bcc695-f524-3f7b-8777-1983582f602e | -3.08864 | -54.17179 | 2024-10-21 05:53:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 57.0 |
| d81c69fb-ab35-3de8-86fb-4ff007d397b4 | -3.08795 | -54.19075 | 2024-10-21 05:53:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 05c25cf1-a2ac-3feb-8b2a-9ef240728eb5 | -3.08766 | -54.17876 | 2024-10-21 05:53:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 57.0 |
| 262d7ed7-6084-3587-b27f-d4ec2ec2517a | -3.08703 | -54.1484 | 2024-10-21 05:53:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 9f883834-da47-3cef-ac7f-e742e5bb592b | -3.08696 | -54.1974 | 2024-10-21 05:53:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 6562536d-ef7b-32b2-8e5a-50a43486e176 | -3.0867 | -54.1855 | 2024-10-21 05:53:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 11.3 |
| cc1f30e3-ba0a-3865-a2bc-9ec850fdac80 | -3.08604 | -54.15505 | 2024-10-21 05:53:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| a855dcc9-b1d3-3fc1-9b61-82f71a505c24 | -3.08576 | -54.19215 | 2024-10-21 05:53:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 11.3 |
| 7a2ed994-aba1-30b1-9d32-6d693dd7dda2 | -3.08502 | -54.16198 | 2024-10-21 05:53:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 19.2 |
| ea857794-01ab-3be8-8c6a-c65d412cd4b9 | -3.08396 | -54.16914 | 2024-10-21 05:53:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 19.2 |
| 6eb21fad-8851-3a7c-b0ff-2ecbfda0bb3d | -3.08292 | -54.17618 | 2024-10-21 05:53:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 15.1 |
| 3f48d558-1fbe-3358-a5c1-dda7926cba49 | -3.0819 | -54.18304 | 2024-10-21 05:53:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 15.1 |
| db542039-4843-3a29-b51f-566387a3d4e3 | -3.07693 | -54.16802 | 2024-10-21 05:53:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 88119d47-209f-315a-a843-7a7ebcfd9a54 | -3.02205 | -54.3468 | 2024-10-21 05:53:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| d786970a-9179-3487-9180-2ac8372905f0 | -3.02115 | -54.35293 | 2024-10-21 05:53:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 7ac4d650-0f7d-3eae-b738-b573ec89e991 | -2.27443 | -53.75745 | 2024-10-21 05:53:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| cde31cbf-621d-346a-81a4-f3b696f5441a | -2.26729 | -53.75641 | 2024-10-21 05:53:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| db8b0413-c359-35a9-9584-7933022f3451 | -9.96089 | -64.87988 | 2024-10-21 05:55:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 366dd34e-f6ae-3022-82fe-02cd541e1d9b | -9.87586 | -65.1506 | 2024-10-21 05:55:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| b7da9362-1c36-38bd-abdd-9287efc50939 | -9.87567 | -65.14799 | 2024-10-21 05:55:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 692d3517-243e-3b4a-beae-6d85d09e09d3 | -9.43265 | -67.75053 | 2024-10-21 05:55:00 | NPP-375D | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 7c5647c5-4127-300e-9208-c9c2061f2beb | -17.79968 | -57.48511 | 2024-10-21 05:55:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.7 |
| c877e756-9704-3327-9493-204638a2de21 | -17.71819 | -57.46369 | 2024-10-21 05:55:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.9 |
| 2dab5243-36f1-31e1-bbd5-7e0948d950dc | -17.71762 | -57.47021 | 2024-10-21 05:55:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.9 |
| 2a952271-5dde-36af-9364-71de10ae34c9 | -17.71236 | -57.45811 | 2024-10-21 05:55:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.2 |
| ab308d00-0996-31ca-947b-47e4b7b97f60 | -17.71186 | -57.45645 | 2024-10-21 05:55:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.2 |
| f0066c6b-80a7-329c-afdf-cd23906a030b | -17.71176 | -57.46463 | 2024-10-21 05:55:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.2 |
| b1905459-e723-3509-95f8-ed0e7aef527c | -17.71129 | -57.46297 | 2024-10-21 05:55:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.9 |
| dae3fc71-294f-3eda-abb0-5a7a9ddbfe90 | -17.70547 | -57.45745 | 2024-10-21 05:55:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.2 |
| 0a486e87-d16f-3c12-af2d-448f12561193 | -17.70497 | -57.45575 | 2024-10-21 05:55:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.0 |
| 43200f3b-a1dd-3a27-9b6d-81bc8278889a | -17.70487 | -57.46396 | 2024-10-21 05:55:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.2 |
| 43265be7-0dfd-3202-b96a-de510ef915dd | -17.7044 | -57.46228 | 2024-10-21 05:55:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 10.2 |
| f9308282-8f07-3e64-81f9-f01b366f8348 | -17.69349 | -57.4365 | 2024-10-21 05:55:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.2 |
| 59fca554-c8f3-325f-b784-f94c287fd55b | -17.69286 | -57.43469 | 2024-10-21 05:55:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.0 |
| af89612a-7bc3-3357-9ed8-0e05bd504a78 | -17.68719 | -57.42928 | 2024-10-21 05:55:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.5 |
| 46ebb24e-598b-3294-96f7-8d483e013741 | -17.68659 | -57.43581 | 2024-10-21 05:55:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.5 |
| 6c830b29-5020-34ab-8ef6-50b3e076279f | -17.68652 | -57.42742 | 2024-10-21 05:55:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.9 |
| 0315c169-bd1a-3bca-a80d-9b27ab5152a3 | -17.68596 | -57.43397 | 2024-10-21 05:55:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.0 |
| feebc414-bec4-38ae-92ad-560dcf9a8ba8 | -17.25372 | -57.30629 | 2024-10-21 05:55:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.0 |
| faeefb6f-af69-3925-957c-b6e746774a74 | -17.25312 | -57.31285 | 2024-10-21 05:55:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.0 |
| 3125c499-0ee8-3520-9fd9-057b7de38a8b | -12.84097 | -63.00188 | 2024-10-21 05:55:00 | NPP-375D | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 8594bc63-1232-3e26-a7c6-f398ca05e10d | -12.83642 | -63.00127 | 2024-10-21 05:55:00 | NPP-375D | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c7deb3ec-d1e1-303e-b89d-e6a5abfc90ee | -12.8358 | -63.00594 | 2024-10-21 05:55:00 | NPP-375D | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 6ef67233-efa2-372a-afaf-ecf4bdb5afe3 | -12.54807 | -63.28444 | 2024-10-21 05:55:00 | NPP-375D | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 3.7 |
| bccb9b59-6ea2-335c-93e8-341f1f3dcb6c | -12.54749 | -63.28886 | 2024-10-21 05:55:00 | NPP-375D | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 4.2 |
| c90f1637-f118-3fb9-80ec-258cb92a8130 | -12.5448 | -63.27498 | 2024-10-21 05:55:00 | NPP-375D | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 3.9 |
| e05e6462-c533-3ac7-bb06-be371b9f31e7 | -12.54422 | -63.27942 | 2024-10-21 05:55:00 | NPP-375D | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 1c0cad71-ba78-345f-81ba-73b0d2f7b059 | -12.54363 | -63.28383 | 2024-10-21 05:55:00 | NPP-375D | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 3.7 |
| e12e6514-07c7-3b58-bd11-9b1e389da71f | -12.54305 | -63.28824 | 2024-10-21 05:55:00 | NPP-375D | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 7fb82769-1823-3b84-a256-8031d383c085 | -12.54036 | -63.27436 | 2024-10-21 05:55:00 | NPP-375D | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 4.0 |
| f5acbaac-29dd-31dd-8418-787cd66d4f66 | -12.53977 | -63.27879 | 2024-10-21 05:55:00 | NPP-375D | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 3.0 |
| e5484d3d-abcc-3ddc-93fe-3004599cc74d | -12.53693 | -63.19685 | 2024-10-21 05:55:00 | NPP-375D | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 55153812-ee61-3977-8aa7-e01ff0b1a8f9 | -12.53446 | -63.03952 | 2024-10-21 05:55:00 | NPP-375D | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| f8cbd2b8-7325-363a-8c6a-7d0cc31e0881 | -12.53387 | -63.04409 | 2024-10-21 05:55:00 | NPP-375D | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 90a5d00e-d6fa-35cd-9fd4-e960d7387a3f | -12.53363 | -63.18725 | 2024-10-21 05:55:00 | NPP-375D | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 5b325396-b3bc-3199-a591-5b4eb59c83c4 | -12.5332 | -63.03741 | 2024-10-21 05:55:00 | NPP-375D | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 0.6 |
| b954fb04-d0ce-3c1d-a713-a12f908f50af | -12.53304 | -63.19173 | 2024-10-21 05:55:00 | NPP-375D | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 1d1b5085-4568-38f5-ba36-6facc72cfd4d | -12.53257 | -63.04198 | 2024-10-21 05:55:00 | NPP-375D | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| d49efb6b-c865-3f75-ab5a-09adc96d6c83 | -12.53246 | -63.1962 | 2024-10-21 05:55:00 | NPP-375D | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 09517980-7049-32c9-bc60-5df1dca4691f | -12.5317 | -63.0251 | 2024-10-21 05:55:00 | NPP-375D | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 64a359ce-a8e0-3f37-b0d5-bb551037a93d | -12.53112 | -63.0297 | 2024-10-21 05:55:00 | NPP-375D | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 2.1 |
| abbf28f5-b718-3d64-a5bd-0c58d2b5a25f | -12.52993 | -63.02762 | 2024-10-21 05:55:00 | NPP-375D | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 62f04357-667b-34ff-938e-a93faeeba639 | -12.52916 | -63.18662 | 2024-10-21 05:55:00 | NPP-375D | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| eb0a5aee-7733-3f6f-8a49-93cf9219f533 | -12.52857 | -63.19111 | 2024-10-21 05:55:00 | NPP-375D | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 83374b63-64a9-34ca-932f-cc9bc9c92622 | -12.52744 | -63.04593 | 2024-10-21 05:55:00 | NPP-375D | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 921268da-908d-3466-abba-08dbf79d6e62 | -12.5266 | -63.02905 | 2024-10-21 05:55:00 | NPP-375D | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 2.6 |
| d2111558-9f6a-3865-bb65-ae0664b72f81 | -12.52542 | -63.03825 | 2024-10-21 05:55:00 | NPP-375D | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 55413bd6-722d-3f07-9b23-76a1cedf21f1 | -12.52541 | -63.027 | 2024-10-21 05:55:00 | NPP-375D | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 6a11cd48-b0dd-37d8-86e4-f640e8bd577a | -12.52484 | -63.04283 | 2024-10-21 05:55:00 | NPP-375D | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 303fbdff-8345-375d-a650-65e30f210108 | -12.52425 | -63.04742 | 2024-10-21 05:55:00 | NPP-375D | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 92a4c74b-0f82-31ed-9765-2051708bfe6a | -12.52417 | -63.03616 | 2024-10-21 05:55:00 | NPP-375D | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 8422e9ac-3d7c-3741-bbe0-5ea557328fe5 | -12.52411 | -63.19046 | 2024-10-21 05:55:00 | NPP-375D | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 3.2 |
| ffafa205-e536-3b3a-b9eb-a90ec9b62307 | -12.52353 | -63.19495 | 2024-10-21 05:55:00 | NPP-375D | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a056736d-9efb-3e08-a559-07350bcc2ee2 | -12.52324 | -63.01929 | 2024-10-21 05:55:00 | NPP-375D | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 2.7 |
| d9363fb7-ac3e-398a-b60b-206116dc0ec9 | -12.52297 | -63.3034 | 2024-10-21 05:55:00 | NPP-375D | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 7.0 |
| dda7b306-774e-361a-a5df-3ebee4749f97 | -12.52293 | -63.04531 | 2024-10-21 05:55:00 | NPP-375D | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 2.6 |
| afcf0fe2-5acf-34e6-9d50-a500b42cff77 | -12.52239 | -63.30781 | 2024-10-21 05:55:00 | NPP-375D | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 7.0 |
| f9931a94-b53b-36e2-ac28-dafcabef0a42 | -12.5215 | -63.02181 | 2024-10-21 05:55:00 | NPP-375D | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 2c5ef7ad-1753-3adf-9bf6-ea04ca01854e | -12.52032 | -63.0422 | 2024-10-21 05:55:00 | NPP-375D | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 667963e1-ac36-345b-8da8-46095b9f2d6d | -12.51974 | -63.04679 | 2024-10-21 05:55:00 | NPP-375D | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 3.8 |
| db56b8a0-a3f2-3df2-9924-f6495de2c8d7 | -12.51906 | -63.19432 | 2024-10-21 05:55:00 | NPP-375D | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 224f8349-5c62-39c3-a973-ff96cf893b74 | -12.51853 | -63.30279 | 2024-10-21 05:55:00 | NPP-375D | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 7.6 |
| 3eb6af3a-c288-3c8d-8a82-44b66899ce31 | -12.51841 | -63.04469 | 2024-10-21 05:55:00 | NPP-375D | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 35dbfe36-3c2d-3c3f-bcc4-25d13d4657d6 | -12.51796 | -63.30719 | 2024-10-21 05:55:00 | NPP-375D | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 7.6 |
| 8131f5fa-18cc-3159-b03b-50e5e49d4480 | -12.51779 | -63.04926 | 2024-10-21 05:55:00 | NPP-375D | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 2e756311-1378-3ed8-93a6-952c7f9f6e13 | -12.51467 | -63.29776 | 2024-10-21 05:55:00 | NPP-375D | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 3.2 |
| d12a8f7b-340d-3157-ac34-dc025c480283 | -12.5141 | -63.30217 | 2024-10-21 05:55:00 | NPP-375D | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 7.6 |
| ec6ef9ad-b233-340d-9690-0dfdd71a6aeb | -12.5139 | -63.04407 | 2024-10-21 05:55:00 | NPP-375D | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 0209899d-4ef5-3563-b845-185b200c2ef5 | -12.51352 | -63.30657 | 2024-10-21 05:55:00 | NPP-375D | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 7.6 |
| 38304e4c-2113-3d17-90c4-659393474dae | -12.51012 | -63.19307 | 2024-10-21 05:55:00 | NPP-375D | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e2801353-d106-3429-add6-9702c16cb6c0 | -12.50909 | -63.30595 | 2024-10-21 05:55:00 | NPP-375D | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 2.9 |
| ef505ee4-0e52-3f36-80d8-e1208ff903fd | -12.50637 | -63.29212 | 2024-10-21 05:55:00 | NPP-375D | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 3.9 |
| db4b103b-4c7f-36c5-9cb5-947a04c7de45 | -12.50523 | -63.30093 | 2024-10-21 05:55:00 | NPP-375D | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 2.9 |
| fd989035-62c0-3ff9-a68b-b8ee791c158b | -12.50465 | -63.30533 | 2024-10-21 05:55:00 | NPP-375D | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 2.9 |
| a20febfc-c74d-3790-a8a8-76c6613ff934 | -12.50388 | -63.1856 | 2024-10-21 05:55:00 | NPP-375D | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 37155edb-4a3a-35e8-9dad-249109a75bc1 | -12.50328 | -63.28957 | 2024-10-21 05:55:00 | NPP-375D | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 0693303e-006c-366e-b985-a2ecb21fc3f3 | -12.50327 | -63.19007 | 2024-10-21 05:55:00 | NPP-375D | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 2.5 |
| ca7bb8c8-ca1f-38ea-bf7c-2943ce60aa46 | -12.50251 | -63.28708 | 2024-10-21 05:55:00 | NPP-375D | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 2.1 |
| bd5fab3d-96c6-34c4-92bf-bb7462b56f5f | -12.50208 | -63.29837 | 2024-10-21 05:55:00 | NPP-375D | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 2.2 |


[Clique aqui para ver as próximas entradas](README61.md)
