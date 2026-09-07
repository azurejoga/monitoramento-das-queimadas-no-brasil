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

## Dados Diários - Página 19

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 094721af-8eb9-36e8-95e0-46f6394c8e88 | -4.03587 | -52.07346 | 2026-09-07 05:01:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 96585c1e-dcd3-33d3-8aa0-c5b7e4995344 | -3.55243 | -48.17939 | 2026-09-07 05:01:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 699a5b6d-4e64-308a-af77-cf9376b6e7e8 | -2.76938 | -54.17872 | 2026-09-07 05:01:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 9b6d9d7b-5c10-3258-b448-88e3ea5fa398 | -3.02096 | -51.34735 | 2026-09-07 05:01:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| a5b7e421-bfa1-3923-bfd2-a93b1329175c | -3.49685 | -50.6092 | 2026-09-07 05:01:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| f9181d86-644d-3745-83b2-efd3e6b13891 | -4.07603 | -48.95288 | 2026-09-07 05:01:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 6.6 |
| 76a0b76e-64a3-39c8-b7a0-358af9a50ea1 | -3.49066 | -50.60454 | 2026-09-07 05:01:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| e410d362-ef64-3a3e-ab39-2058ff1c4ebb | -3.26386 | -57.87459 | 2026-09-07 05:01:00 | NPP-375D | BOA VISTA DO RAMOS | AMAZONAS | Brasil | 1300680 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 6585916e-1da3-3471-890d-24e5c1537edb | -3.47481 | -54.48385 | 2026-09-07 05:01:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 6e53cabc-0838-30a7-89d8-8897cf368c4a | -2.87108 | -50.461 | 2026-09-07 05:01:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 09b43d88-e2f9-3087-822e-d0d8979c75c8 | -3.11964 | -57.69511 | 2026-09-07 05:01:00 | NPP-375D | BOA VISTA DO RAMOS | AMAZONAS | Brasil | 1300680 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 91149042-751b-303a-81ba-12e4ea250f87 | -3.14305 | -60.66 | 2026-09-07 05:01:00 | NPP-375D | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 12.8 |
| 77d2fb7c-bdbd-38f0-8e4b-74ba7737606b | -4.06537 | -50.64 | 2026-09-07 05:01:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 8e30474a-818c-3ac0-8644-e792a2aa828f | -2.87617 | -50.45075 | 2026-09-07 05:01:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 4ea5f966-3648-3cae-a536-856415190408 | -2.88006 | -50.45462 | 2026-09-07 05:01:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 01335a03-5d7b-3bd3-89d5-8a2cbeafdfc1 | -3.62433 | -54.60591 | 2026-09-07 05:01:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b51ff248-9025-3e51-952d-94e1760c6ea0 | -1.77478 | -54.96236 | 2026-09-07 05:01:00 | NPP-375D | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| c5b0ae8f-88ce-3f98-8ee8-8afdaf5f22e7 | -2.63284 | -46.77235 | 2026-09-07 05:01:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 18.8 |
| ec583319-d474-349c-8484-15c212bcd956 | 2.43907 | -50.77493 | 2026-09-07 05:01:00 | NPP-375D | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 23dbf5c3-e57d-3dc7-9fd3-58b79bb67cd1 | -2.63339 | -46.76883 | 2026-09-07 05:01:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 18.8 |
| 693bf862-5368-3ad0-ad1b-15f71654c782 | -3.08281 | -61.53385 | 2026-09-07 05:01:00 | NPP-375D | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| ad7d1398-7a2e-3f01-99e2-655fefe09676 | 2.49249 | -50.81601 | 2026-09-07 05:01:00 | NPP-375D | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 5.5 |
| fbd10857-fdca-36b3-9d9c-f344d8bd3305 | -3.37689 | -59.41866 | 2026-09-07 05:01:00 | NPP-375D | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 61a45f27-a18f-3e94-b227-430c568961ea | 0.21714 | -51.28009 | 2026-09-07 05:01:00 | NPP-375D | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 702aef8a-626b-384b-b6cb-b3d767c4ac82 | -2.86321 | -50.44505 | 2026-09-07 05:01:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 7a955e73-1529-3da1-af2e-d24556235c69 | -2.88286 | -50.43664 | 2026-09-07 05:01:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| e6a1fcec-c615-338f-a476-d1e8a8351661 | -4.03974 | -52.07053 | 2026-09-07 05:01:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 3fd31dd5-777e-392b-92d1-489e3b28f620 | -3.37806 | -59.41154 | 2026-09-07 05:01:00 | NPP-375D | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 31f995c2-0ab4-3a61-a90d-e2f555149acc | -3.14145 | -60.63734 | 2026-09-07 05:01:00 | NPP-375D | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| a4260e8a-75c8-33f2-8924-58cc538fd67c | -1.49146 | -54.81775 | 2026-09-07 05:01:00 | NPP-375D | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 21b54ce8-576e-39c7-a039-ea404fb87c95 | -3.78955 | -55.87761 | 2026-09-07 05:01:00 | NPP-375D | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| da2c97f2-0314-3dda-8bb5-6dacd1b6e42f | -2.87732 | -50.44356 | 2026-09-07 05:01:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 7.6 |
| 89a6a20f-f22e-314f-a990-ce817f208af2 | -2.87674 | -50.44715 | 2026-09-07 05:01:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| fcb2b05a-88f6-3b7b-aadc-18519cee8b48 | -4.59406 | -50.9831 | 2026-09-07 05:01:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| e6fd58cf-8a02-3baa-b179-09b092cebb6e | -2.8745 | -50.43945 | 2026-09-07 05:01:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 7.6 |
| cec78f9b-74c0-3c32-9776-6848bea3f9c5 | -3.11741 | -57.69194 | 2026-09-07 05:01:00 | NPP-375D | BOA VISTA DO RAMOS | AMAZONAS | Brasil | 1300680 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 7709ff59-920c-3f17-b404-ab21bfdc3ee3 | -1.20227 | -55.73474 | 2026-09-07 05:01:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 1d2c1010-302b-3420-b018-f7f49eefbd38 | -4.06876 | -50.64052 | 2026-09-07 05:01:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 961e3a7d-8acf-3730-b0e7-f9e0a5db96d6 | -1.20381 | -55.72521 | 2026-09-07 05:01:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 0530d4b8-cd56-3789-a287-80522b7dbbbd | 2.02825 | -50.9173 | 2026-09-07 05:01:00 | NPP-375D | AMAPÁ | AMAPÁ | Brasil | 1600105 | 16 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 7f9ca543-b05b-3c13-a93b-20975247dd0e | -2.86827 | -50.45687 | 2026-09-07 05:01:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f309eb5a-87fb-3ef9-b433-03fc608156b5 | -3.49009 | -50.60813 | 2026-09-07 05:01:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| d52a5ed1-aea3-344f-8916-4630cef5600c | -3.12229 | -57.6887 | 2026-09-07 05:01:00 | NPP-375D | BOA VISTA DO RAMOS | AMAZONAS | Brasil | 1300680 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 1032ec16-1535-3dc2-a8d0-48a74a9040ba | -2.3002 | -48.58007 | 2026-09-07 05:01:00 | NPP-375D | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b8fea788-113c-3c80-ba56-a50c69cc848d | -1.86021 | -47.97907 | 2026-09-07 05:01:00 | NPP-375D | CONCÓRDIA DO PARÁ | PARÁ | Brasil | 1502756 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| ee43fa56-2dcc-3890-8060-0e2a08fff500 | -1.86348 | -47.97661 | 2026-09-07 05:01:00 | NPP-375D | CONCÓRDIA DO PARÁ | PARÁ | Brasil | 1502756 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 62bec42b-cb21-3b1a-ab72-59da6c572c72 | 2.44184 | -50.77097 | 2026-09-07 05:01:00 | NPP-375D | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 3.3 |
| f0c05f24-daa9-3455-a06a-babc80a16c2e | -4.59687 | -50.98718 | 2026-09-07 05:01:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 35144cca-9f9f-3ebb-aefa-40145708b46b | -3.14877 | -60.65774 | 2026-09-07 05:01:00 | NPP-375D | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 0de6ddcd-66c8-38dc-9a59-fb50c7516058 | -3.80984 | -52.34924 | 2026-09-07 05:01:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 11024f2a-db15-3acf-8900-4fcec95f94bd | -3.11678 | -57.6959 | 2026-09-07 05:01:00 | NPP-375D | BOA VISTA DO RAMOS | AMAZONAS | Brasil | 1300680 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| c12239b6-9738-36d2-ab58-d4a33a6431cd | -4.64978 | -46.31178 | 2026-09-07 05:01:00 | NPP-375D | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 32fd5824-aeb4-362e-a3b9-6654cad1070a | -2.88062 | -50.45103 | 2026-09-07 05:01:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| f97de00f-abb5-3f9c-b64c-1ce87dd8d1c1 | 2.43961 | -50.77837 | 2026-09-07 05:01:00 | NPP-375D | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 2.4 |
| abeff547-94b1-3500-8fec-272be410e5cf | -1.2015 | -55.7395 | 2026-09-07 05:01:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| e318fbd4-ddce-338e-b39f-16f706dc0691 | -2.87789 | -50.43996 | 2026-09-07 05:01:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 7.6 |
| a9e0db56-9794-338c-a255-6c132a4d00cb | -3.14826 | -60.66084 | 2026-09-07 05:01:00 | NPP-375D | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 3.3 |
| afe07441-151c-3fe6-9be5-a2c494108674 | -2.87667 | -50.4541 | 2026-09-07 05:01:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 48897fe0-e71e-3f51-b1b5-438f2dd79aa5 | -3.9832 | -56.08716 | 2026-09-07 05:01:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| c710414f-116b-32c3-a908-598029e35b9e | -3.24327 | -52.27092 | 2026-09-07 05:01:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| c4cbf307-35e4-34a6-856c-686cc91d1776 | -2.86431 | -50.45994 | 2026-09-07 05:01:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 5d9f8822-ff4d-32ff-894e-c6e99b05ba1b | 2.49194 | -50.81256 | 2026-09-07 05:01:00 | NPP-375D | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 96786921-b66c-394e-a61b-fb1c375d6351 | -3.85252 | -54.22087 | 2026-09-07 05:01:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 2c28deaa-516d-3ac4-89b5-7b509419267b | -2.87503 | -50.45793 | 2026-09-07 05:01:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 7edb7ec1-ea37-3358-9233-896b06f67328 | -2.915 | -54.12296 | 2026-09-07 05:01:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 71749491-28e2-3868-8fec-3e31eb0ac249 | -2.97968 | -54.01981 | 2026-09-07 05:01:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 2345b7e9-5d06-388d-9b5b-893f905c3c02 | -2.96256 | -48.71075 | 2026-09-07 05:01:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 6.3 |
| ac262bb6-b522-3feb-830c-72a7696b7842 | -4.03642 | -52.07001 | 2026-09-07 05:01:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a29a567d-5369-3f1f-8618-a15bcd98c325 | -2.87393 | -50.44304 | 2026-09-07 05:01:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 7.6 |
| 650c4242-e0b1-39b2-8078-22130e4a3ef1 | -1.19997 | -55.72453 | 2026-09-07 05:01:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| ee291dea-9f5a-36a4-a996-f3c095cd5216 | -2.88513 | -50.44435 | 2026-09-07 05:01:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| af3faa1b-97a6-3f19-bd6a-182078a2be3b | -3.16014 | -50.82356 | 2026-09-07 05:01:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 74328013-781a-3859-a543-5b137c30390c | -3.81363 | -55.89537 | 2026-09-07 05:01:00 | NPP-375D | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 7f150167-cef0-338d-bf1e-24c7e16d309c | -2.6369 | -46.77295 | 2026-09-07 05:01:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 18.8 |
| 6be6470a-efe2-35b1-8f46-a85d3fa328ab | -3.37771 | -59.41356 | 2026-09-07 05:01:00 | NPP-375D | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 4.1 |
| d907343a-17b8-3348-b953-770066dde3bd | -2.87111 | -50.43892 | 2026-09-07 05:01:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 2a2077e9-cde0-389f-a42e-383e1c632e8f | -4.03532 | -52.07692 | 2026-09-07 05:01:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 6ee1e7f4-5b50-310b-baa0-36ebc3d3b551 | -2.8756 | -50.45434 | 2026-09-07 05:01:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 1ea84c93-b52e-3d12-9678-4faf863bb0da | -2.9156 | -54.11915 | 2026-09-07 05:01:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| a4a8a089-dd0a-3232-8a66-33230a3da522 | -3.83174 | -55.47995 | 2026-09-07 05:01:00 | NPP-375D | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| d9771b70-6f6a-3179-bef4-f459253f18e5 | -2.82055 | -46.70861 | 2026-09-07 05:01:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 21a8265b-b2ee-36fd-aa49-a12ce646b634 | -4.07967 | -48.95342 | 2026-09-07 05:01:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 6.6 |
| b88dee42-3156-3b40-a2a3-afeda8c6ee9a | -4.11122 | -49.06361 | 2026-09-07 05:01:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 9.8 |
| 0106afdd-43ca-3f4c-82f4-02f104254f1d | -1.86698 | -47.98466 | 2026-09-07 05:01:00 | NPP-375D | CONCÓRDIA DO PARÁ | PARÁ | Brasil | 1502756 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 070707f4-7138-393d-aa90-c83769137e4a | -3.81436 | -55.89086 | 2026-09-07 05:01:00 | NPP-375D | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 14db6862-37b3-3d61-b0d5-930a84e447c1 | -4.10761 | -49.06306 | 2026-09-07 05:01:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 9.8 |
| e028ff2d-f7b5-32d7-8d83-8540edc6d099 | -2.88456 | -50.44796 | 2026-09-07 05:01:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c61b0dbc-3708-3d54-9390-e3932203449c | -1.18615 | -55.71235 | 2026-09-07 05:01:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 0b5f8ae2-e9ba-3c5d-b5d6-f0a5825cd72c | 2.44238 | -50.77441 | 2026-09-07 05:01:00 | NPP-375D | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 8.1 |
| bc2c123b-ec1c-3674-938e-b6b7468a955f | -2.86883 | -50.45329 | 2026-09-07 05:01:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b41003c7-4fea-3c6e-ae0b-26a40a73f419 | -2.96321 | -48.70657 | 2026-09-07 05:01:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 6.3 |
| bf25d040-e334-39d4-a65c-1e52f987fd43 | -3.11605 | -57.69049 | 2026-09-07 05:01:00 | NPP-375D | BOA VISTA DO RAMOS | AMAZONAS | Brasil | 1300680 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| f3a49d3a-1342-3dbe-bf3c-fee4fdfaa583 | -2.62878 | -46.77174 | 2026-09-07 05:01:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| fce17eb7-f567-37f1-bb8c-241bf2818ae5 | -3.38759 | -59.41307 | 2026-09-07 05:01:00 | NPP-375D | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 4badab59-928e-3194-bd9b-39cd61038706 | -3.90457 | -55.83429 | 2026-09-07 05:01:00 | NPP-375D | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 34ce2521-83d4-386a-ac1b-6bcb4a785ff7 | -2.86716 | -50.44198 | 2026-09-07 05:01:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 797a641f-92bd-3ac6-a983-ce7b51ce3336 | -2.82511 | -49.22688 | 2026-09-07 05:01:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| b92b1171-815b-367b-b08f-31e4c84573ad | -3.57231 | -54.5507 | 2026-09-07 05:01:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 691b68aa-ce95-32b9-9845-42bec635ee01 | -3.79257 | -55.88272 | 2026-09-07 05:01:00 | NPP-375D | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| ca67d98e-9fd8-33e8-bff1-8b1da6b048c7 | -2.87611 | -50.45769 | 2026-09-07 05:01:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |


[Clique aqui para ver as próximas entradas](README20.md)
