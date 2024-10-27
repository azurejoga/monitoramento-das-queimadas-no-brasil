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
| 03e5590b-4667-383c-a0b6-38a8c7ce2e69 | -3.29455 | -50.08531 | 2024-10-27 05:16:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 4988855c-ae1b-39cb-ada9-3dd128f923cc | -3.29413 | -50.0847 | 2024-10-27 05:16:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 95e3e449-4214-3568-86ea-155b854f5bf2 | -3.23275 | -50.18896 | 2024-10-27 05:16:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 2aa2c5f0-2623-34b0-9096-53967d6bb438 | -3.21545 | -50.16925 | 2024-10-27 05:16:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| d7354dcd-49c4-3604-9c03-85306600dbb2 | -3.20806 | -50.21929 | 2024-10-27 05:16:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 9e8a133e-4677-31f0-b873-50cae4920a82 | -4.99034 | -49.90329 | 2024-10-27 05:16:00 | NOAA-21 | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 81bac5ee-870e-3423-802a-363184644671 | -4.98516 | -49.90256 | 2024-10-27 05:16:00 | NOAA-21 | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 23d6537f-c677-388d-9747-a104cce43a00 | -4.98471 | -49.90567 | 2024-10-27 05:16:00 | NOAA-21 | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| c85b3d0d-1bd5-34f5-9eb1-c1485839a476 | -3.77905 | -50.16921 | 2024-10-27 05:16:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 0f00df52-b09b-37ae-8cfd-c273e087b034 | -5.1473 | -50.75854 | 2024-10-27 05:16:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| dcf223c4-be9c-36b9-8817-4e679ca12690 | 1.93122 | -50.8435 | 2024-10-27 05:16:00 | NOAA-21 | AMAPÁ | AMAPÁ | Brasil | 1600105 | 16 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 234472bb-ce38-3de0-9b1a-4511a19e7471 | 1.92253 | -50.84492 | 2024-10-27 05:16:00 | NOAA-21 | AMAPÁ | AMAPÁ | Brasil | 1600105 | 16 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 188c8853-3422-3b89-862d-8bd796942449 | 1.78307 | -50.45693 | 2024-10-27 05:16:00 | NOAA-21 | AMAPÁ | AMAPÁ | Brasil | 1600105 | 16 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 4e1f3f27-b7cc-38f7-8407-374a3517747e | 1.77931 | -50.46214 | 2024-10-27 05:16:00 | NOAA-21 | AMAPÁ | AMAPÁ | Brasil | 1600105 | 16 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 0a78aee6-f8b4-3611-8b22-25b5aa9a8709 | 1.7786 | -50.45766 | 2024-10-27 05:16:00 | NOAA-21 | AMAPÁ | AMAPÁ | Brasil | 1600105 | 16 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 8730c127-06a5-3b73-9330-cb0e802daf13 | 1.77627 | -50.47177 | 2024-10-27 05:16:00 | NOAA-21 | AMAPÁ | AMAPÁ | Brasil | 1600105 | 16 | 33 | nan | nan | nan | Amazônia | 7.8 |
| 20388414-819f-3101-a37a-f8b7288a5c4f | 1.77484 | -50.46286 | 2024-10-27 05:16:00 | NOAA-21 | AMAPÁ | AMAPÁ | Brasil | 1600105 | 16 | 33 | nan | nan | nan | Amazônia | 22.0 |
| 3b45e289-52d6-31a6-af76-ae836b48c808 | 1.39611 | -50.71865 | 2024-10-27 05:16:00 | NOAA-21 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 151daccc-3e39-3590-aa33-3c54b031d0de | 1.39169 | -50.71939 | 2024-10-27 05:16:00 | NOAA-21 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 4ccc5e70-733b-3b6a-8f1f-04c50ab3db50 | 1.25245 | -50.86627 | 2024-10-27 05:16:00 | NOAA-21 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 20ff9dec-975a-36c0-afe5-74d579cfcfd6 | 1.24129 | -50.88125 | 2024-10-27 05:16:00 | NOAA-21 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 40a90093-494f-39e5-9288-e6f2c90747c1 | 1.23757 | -50.88622 | 2024-10-27 05:16:00 | NOAA-21 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a53ca223-e56f-34b9-9306-c113c3cdb5ac | 0.42638 | -50.27264 | 2024-10-27 05:16:00 | NOAA-21 | CHAVES | PARÁ | Brasil | 1502509 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 174a7586-cde5-31e4-a23f-9b2d9a58b723 | 0.33464 | -50.94085 | 2024-10-27 05:16:00 | NOAA-21 | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 1.6 |
| daf69ca9-4d46-3022-bd80-3e697821ce50 | 0.33089 | -50.94588 | 2024-10-27 05:16:00 | NOAA-21 | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 1.6 |
| ba770f06-63fd-38fe-95a5-fdf682c91d24 | 0.33021 | -50.94154 | 2024-10-27 05:16:00 | NOAA-21 | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 1.6 |
| daf6ec3c-2d6f-35cd-b0a0-85ae277f8090 | 0.31996 | -50.93422 | 2024-10-27 05:16:00 | NOAA-21 | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 479150f6-0cc4-3819-80f7-8f087d6aa4a5 | 0.11327 | -51.0821 | 2024-10-27 05:16:00 | NOAA-21 | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 19a31970-a09d-3eae-a7f2-08d2d6a79e23 | -0.09758 | -51.32306 | 2024-10-27 05:16:00 | NOAA-21 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 1.7 |
| a29c2b7b-b5fa-3ad4-9316-3cbcc26ae5c9 | -2.93114 | -51.74817 | 2024-10-27 05:16:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a4de4255-4c99-37f3-ba17-3d47b4a53cae | -2.93071 | -51.74998 | 2024-10-27 05:16:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 5066abc3-8bbe-35b7-a657-dc1dd2c43ded | -2.93048 | -51.75247 | 2024-10-27 05:16:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 41f31c94-6984-3bf1-89fd-9cb45a6bf0de | -2.93008 | -51.75429 | 2024-10-27 05:16:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 2d4e4c0c-09b3-354a-b2cb-2037dfeb6f6a | -2.92982 | -51.75677 | 2024-10-27 05:16:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| aa8e694f-6018-3e89-943e-1c50c4a4c457 | -2.92945 | -51.75861 | 2024-10-27 05:16:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 61146948-7c5a-3a18-9e20-7ccbebec5681 | -2.92915 | -51.76107 | 2024-10-27 05:16:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 1055fcdf-46d6-3dee-b7ee-cab275f8ffd7 | -2.92881 | -51.76294 | 2024-10-27 05:16:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| c61e62de-565e-3e80-8e16-69bb6d7080c8 | -2.92849 | -51.76537 | 2024-10-27 05:16:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| e61898f2-a581-3f84-98bb-a4d12e494384 | -2.92819 | -51.7672 | 2024-10-27 05:16:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| c6ef19e1-f263-389b-a072-383d614673a0 | -2.92783 | -51.76964 | 2024-10-27 05:16:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 8af16431-06f7-3bad-928f-4d969ff0e9e0 | -2.92672 | -51.74755 | 2024-10-27 05:16:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 9828320d-08e7-387a-8cfe-762c54e77e93 | -2.92606 | -51.75186 | 2024-10-27 05:16:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 8.4 |
| 0fc06e2a-fd04-3c35-8bfa-4a0f00047258 | -2.92539 | -51.75618 | 2024-10-27 05:16:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 8.4 |
| fd5d36b4-5d95-3957-95cd-880ab53836e5 | -2.92473 | -51.76052 | 2024-10-27 05:16:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| dc35bee3-45ad-3b70-8c38-08cdaf46d043 | -2.92407 | -51.76479 | 2024-10-27 05:16:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| f3e0474b-7a19-3e7a-b13a-f163653ca017 | -2.92341 | -51.76905 | 2024-10-27 05:16:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 61e83d17-8996-35d1-a3d7-2ff11bfccae7 | -2.92229 | -51.74699 | 2024-10-27 05:16:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 6114acc8-b9e5-368a-a8e1-c06bea06dd62 | -2.92163 | -51.75128 | 2024-10-27 05:16:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 8.4 |
| e002bf56-f196-3f5d-8b84-737dda410727 | -2.92097 | -51.75557 | 2024-10-27 05:16:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 8.4 |
| b967c898-7151-30d9-ac14-0c51ac2d7f3d | -2.92031 | -51.75993 | 2024-10-27 05:16:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| fe208895-91a3-3464-b6e6-89a400f0e427 | -2.91657 | -51.75489 | 2024-10-27 05:16:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 1da94b2a-5d23-3f17-b2ad-fdf4a8dafbd4 | -2.84461 | -51.81415 | 2024-10-27 05:16:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 5586698f-94cd-36eb-a59c-1e1f104e767b | -2.84212 | -51.80072 | 2024-10-27 05:16:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| ef99a330-f6f5-3145-a327-3d8ed33d4449 | -2.84149 | -51.805 | 2024-10-27 05:16:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| d5326494-7ed7-3bff-a3f9-fda08f595a44 | -2.84085 | -51.80927 | 2024-10-27 05:16:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 9819a698-101b-3e37-b4a9-f9c0155bdf68 | -2.84022 | -51.81353 | 2024-10-27 05:16:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 2a8a3ddb-7219-3f8c-848f-f0e77c89f60b | -2.8371 | -51.80431 | 2024-10-27 05:16:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 17cbe589-8fad-39c0-9af4-bbe67233bd4b | -2.83646 | -51.80859 | 2024-10-27 05:16:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 7ae2e846-adac-33d7-8be5-20de144ff2d6 | -2.83583 | -51.81287 | 2024-10-27 05:16:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 9bbb2631-1e69-3f14-bbee-b02ecb55a792 | -2.83208 | -51.80788 | 2024-10-27 05:16:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 2fb1bc67-7cb7-3834-9d6a-f42f0db4021f | -2.83145 | -51.81216 | 2024-10-27 05:16:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| e96cbb4c-2627-3636-9437-3434916ef405 | -2.81413 | -51.5988 | 2024-10-27 05:16:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 20ab2171-76a5-338b-9782-3f53ed356c96 | -2.40757 | -51.18467 | 2024-10-27 05:16:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 37d45955-5044-3eae-a75b-ed4c8b5d27a1 | -2.27789 | -51.2666 | 2024-10-27 05:16:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 76bc2f67-0c53-3bc6-85c3-aa82f2f21a95 | -2.26435 | -51.25336 | 2024-10-27 05:16:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f05d87ff-03b3-3a77-8d26-b94e1da7a807 | -2.54933 | -51.17655 | 2024-10-27 05:16:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| fa7afc8b-086b-3324-888f-865f6d5cff61 | -2.54862 | -51.18121 | 2024-10-27 05:16:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f5320c97-7ae0-358c-9e93-db1178983048 | -2.54792 | -51.18585 | 2024-10-27 05:16:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 8e98ed8b-b7c5-3966-b516-620edac46f68 | -2.54618 | -51.1665 | 2024-10-27 05:16:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 903535a3-c3f6-3996-ae6d-1d2a226800ef | -2.54548 | -51.17117 | 2024-10-27 05:16:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 6.6 |
| 9adb48d7-4668-3d35-ad07-d5936fbd1897 | -2.54477 | -51.17582 | 2024-10-27 05:16:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 6.6 |
| aec9bf9c-3287-3214-99db-255c6abae5fa | -2.54406 | -51.18048 | 2024-10-27 05:16:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 11.6 |
| e12e5f16-a100-3c10-824f-7c912513922b | -2.54336 | -51.18514 | 2024-10-27 05:16:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 11.6 |
| 53363ed1-227b-305e-9a91-67f780b65b9a | -2.54265 | -51.18981 | 2024-10-27 05:16:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 624bf6fd-82b3-3d0e-8784-b2c2fdd68aff | -2.54194 | -51.19446 | 2024-10-27 05:16:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| fed8d399-08ee-36a6-88ad-8b1e9c9d13c0 | -2.54162 | -51.16578 | 2024-10-27 05:16:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| b028f705-2da6-327c-ba31-c826bd5d792c | -2.54091 | -51.17043 | 2024-10-27 05:16:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 6.6 |
| e65b4dd4-d1e3-3ebb-9199-d82dcea70db7 | -2.54021 | -51.1751 | 2024-10-27 05:16:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 6.6 |
| 6ea49950-aa09-3898-bc5c-3bf067f53fb1 | -2.5395 | -51.17976 | 2024-10-27 05:16:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 11.6 |
| dff13aa8-7e77-34dd-9420-a9add98fc251 | -2.5388 | -51.18444 | 2024-10-27 05:16:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 11.6 |
| ef31937c-efc1-391b-8bcc-2fc4ae8bd84c | -2.53809 | -51.18911 | 2024-10-27 05:16:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 9e2938b2-34f0-3e3e-86c3-8ce3e52816b7 | -2.53739 | -51.19374 | 2024-10-27 05:16:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| af88053d-7800-3783-ba68-ea7f21a1fabb | -2.53705 | -51.16505 | 2024-10-27 05:16:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f24bce10-690b-3cff-9fbd-52ce0a207f1f | -2.53635 | -51.1697 | 2024-10-27 05:16:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 03f65204-9d75-371e-9d62-389afad21c0e | -2.53565 | -51.17437 | 2024-10-27 05:16:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 5ab9c2c3-288a-3136-8641-cd2dc99e75d6 | -2.53494 | -51.17904 | 2024-10-27 05:16:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 15.8 |
| 0b8327b4-02b9-37ec-beb5-9b6b11082315 | -2.53424 | -51.18372 | 2024-10-27 05:16:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 15.8 |
| 2e02d00a-7a02-33f9-bfe1-9d597e40e1c4 | -2.53353 | -51.1884 | 2024-10-27 05:16:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 5ed21ea8-4c04-3389-9280-f00fc932100a | -2.53283 | -51.19303 | 2024-10-27 05:16:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| a95f4bb2-4717-3afb-9d79-cbd0cc7adafb | -2.53249 | -51.16431 | 2024-10-27 05:16:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e2732086-8a15-3961-944b-2d95fa53719a | -2.53213 | -51.19766 | 2024-10-27 05:16:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| ce285d12-4ba6-3e57-8ced-679df5411d49 | -2.53179 | -51.16897 | 2024-10-27 05:16:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 5ac82339-7fd1-396c-96cf-a01c0b33908f | -2.53109 | -51.17365 | 2024-10-27 05:16:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 82c438db-1cb3-3077-82a1-637a6894e145 | -2.53038 | -51.17833 | 2024-10-27 05:16:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 15.8 |
| 2d0584df-6fc1-3813-ac49-92787291a665 | -2.52968 | -51.183 | 2024-10-27 05:16:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 15.8 |
| 7f0ee432-4fc4-3dec-8c4b-f7ff2299d159 | -2.52898 | -51.18767 | 2024-10-27 05:16:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 7d318032-0261-3c43-9768-e981a34bbfc4 | -2.52828 | -51.19231 | 2024-10-27 05:16:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 8d5073e9-4dab-3d5e-97fb-478ef74c788b | -2.52794 | -51.16351 | 2024-10-27 05:16:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 46024d0c-a544-31ea-be8c-d910815c441d | -2.52758 | -51.19694 | 2024-10-27 05:16:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| f09c59c5-be6d-3243-87a8-643c694e9e7c | -2.52723 | -51.16822 | 2024-10-27 05:16:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |


[Clique aqui para ver as próximas entradas](README59.md)
