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

## Dados Diários - Página 30

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 01f1c64d-6e4a-3aed-b107-6841680a7606 | -14.36709 | -52.11336 | 2026-09-25 04:49:00 | NOAA-20 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 62a11e92-f6ae-3a76-a952-f4998d01f380 | -13.22261 | -51.56074 | 2026-09-25 04:49:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 046dc78d-29ba-3ea1-a8fd-965621b6f533 | -14.51915 | -49.57645 | 2026-09-25 04:49:00 | NOAA-20 | SANTA TEREZINHA DE GOIÁS | GOIÁS | Brasil | 5219704 | 52 | 33 | nan | nan | nan | Cerrado | 0.2 |
| 93d119c9-dc60-3de8-859e-7eb0d700574d | -14.74708 | -45.58963 | 2026-09-25 04:49:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 67864e8e-6228-3111-87a4-126e5a87cd41 | -13.69796 | -48.79511 | 2026-09-25 04:49:00 | NOAA-20 | FORMOSO | GOIÁS | Brasil | 5208103 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| d7f07307-3bbd-387e-8d6b-c6cabdf7d2cb | -31.3411 | -54.06531 | 2026-09-25 04:51:00 | NOAA-20 | BAGÉ | RIO GRANDE DO SUL | Brasil | 4301602 | 43 | 33 | nan | nan | nan | Pampa | 0.8 |
| 7ff11ed4-31c0-348b-961c-1b639f5e7dd0 | -27.34258 | -50.7339 | 2026-09-25 04:51:00 | NOAA-20 | CURITIBANOS | SANTA CATARINA | Brasil | 4204806 | 42 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 28d02192-f583-3952-a10d-589b26026bd0 | -1.21867 | -54.55706 | 2026-09-25 05:27:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 84bd863b-9bb4-30aa-8eef-bd9299afdb28 | -3.20561 | -53.41395 | 2026-09-25 05:27:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 177c61a8-b327-3f59-b912-971996d62294 | -1.22171 | -54.56728 | 2026-09-25 05:27:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 98b395bb-93d4-3f1a-880f-81b1fe2099e6 | -3.44839 | -50.07892 | 2026-09-25 05:27:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| c57af0a3-1e34-3fc1-9211-7c7c340473c7 | -3.98305 | -48.43494 | 2026-09-25 05:27:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| aa8d2eb1-da60-3e1e-aab5-13df95f86085 | -1.31548 | -54.57052 | 2026-09-25 05:27:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| fd0d8a5c-f66b-3812-9c5b-30cd1f914e3e | -2.56268 | -49.08795 | 2026-09-25 05:27:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 85ffd0c3-5de4-3aea-9fac-27007e7649dd | 1.62442 | -56.00654 | 2026-09-25 05:27:00 | NOAA-21 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 341e7d32-132c-35ad-be11-e09dbeac078a | 1.61541 | -55.89651 | 2026-09-25 05:27:00 | NOAA-21 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 5b1d0aae-db54-31fe-a438-16ac8163177e | -3.49716 | -50.74293 | 2026-09-25 05:27:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| cbee174a-c1b2-3a8b-a625-5e22fd4a113d | -1.13747 | -54.10181 | 2026-09-25 05:27:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 05d5f369-21d8-3263-8a92-43d348d693c9 | -1.14285 | -54.09768 | 2026-09-25 05:27:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 9.0 |
| 8fb3c4bb-ea6a-3499-b93b-74e8942ce441 | -3.20016 | -53.41613 | 2026-09-25 05:27:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 0ab7e09c-ef51-3932-a5a4-eb7eb197b335 | 1.6249 | -55.95369 | 2026-09-25 05:27:00 | NOAA-21 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| d4719bbf-6dde-3683-939d-6b3ca348c2a1 | -2.57461 | -54.74587 | 2026-09-25 05:27:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| b345e3c6-58c1-3512-bb26-71ce6786451f | 0.49365 | -60.59439 | 2026-09-25 05:27:00 | NOAA-21 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 0.7 |
| cdd33c14-6408-37f5-a7ed-4fc36d781bb9 | 2.25172 | -50.90462 | 2026-09-25 05:27:00 | NOAA-21 | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 4f402c3a-5c31-300f-897c-736acdf65f90 | -1.21725 | -54.56651 | 2026-09-25 05:27:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 7.5 |
| 8bb052c3-3000-34cf-8a1b-d68ed1e850ba | 1.59484 | -56.02131 | 2026-09-25 05:27:00 | NOAA-21 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 3ab2f435-e998-3834-ac27-d10dd8e6c268 | -3.98397 | -48.42846 | 2026-09-25 05:27:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 833f8a6a-9548-3dcc-b68e-be517268cfde | 1.55504 | -55.81918 | 2026-09-25 05:27:00 | NOAA-21 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| a573810d-6b06-37e9-ba72-d730b668fee2 | -3.50377 | -50.73954 | 2026-09-25 05:27:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 451c3319-9e2b-3b26-b920-b6fc484766de | 2.07338 | -55.91496 | 2026-09-25 05:27:00 | NOAA-21 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 2a7757c1-6457-3065-8ca9-eae8f4e0c665 | 1.48402 | -55.8523 | 2026-09-25 05:27:00 | NOAA-21 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 88074189-7f44-3247-ad7f-89e1e6da85fa | -3.44691 | -50.08902 | 2026-09-25 05:27:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| f189a5c7-7cab-3e93-9553-04f78e8c91f2 | 1.61688 | -55.9041 | 2026-09-25 05:27:00 | NOAA-21 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| ae26ebbe-5ffd-344f-a132-65d774e47688 | 0.49695 | -60.59389 | 2026-09-25 05:27:00 | NOAA-21 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 64fe3133-a5a9-3415-bd11-c1adac9b9fca | -1.29786 | -54.21874 | 2026-09-25 05:27:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 13f3129e-3c55-3d69-9aae-54681418be57 | -1.2971 | -54.22368 | 2026-09-25 05:27:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| fdca2999-333a-3316-92c4-134696b74b02 | 3.5605 | -61.16812 | 2026-09-25 05:27:00 | NOAA-21 | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 8a102b6b-fffe-33b9-b5c0-e7cf45165ea0 | -1.21797 | -54.56168 | 2026-09-25 05:27:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 05ba55a8-23da-359c-aca9-59d8a26e6835 | -1.13823 | -54.09698 | 2026-09-25 05:27:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 323bef1b-b4d0-378f-94b0-431f86fcd0f6 | -3.26402 | -49.19333 | 2026-09-25 05:27:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 35653cd6-f58e-3b14-b53f-9dbd31c5b2b5 | -1.53589 | -54.29048 | 2026-09-25 05:27:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| a7d4cc53-c64c-3784-b820-09bd42d98b39 | 1.57553 | -55.82112 | 2026-09-25 05:27:00 | NOAA-21 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| f6519899-95ca-3a01-a54f-ea942862cc41 | -1.14359 | -54.0929 | 2026-09-25 05:27:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |
| d817126c-3897-36f4-8efc-1f7f1aa82fc2 | -1.15107 | -54.10051 | 2026-09-25 05:27:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| b7fb9bbd-af4c-36d3-ac8e-6ddce6c08b36 | 2.24629 | -50.90556 | 2026-09-25 05:27:00 | NOAA-21 | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 1.8 |
| e44bf5fd-65f3-33a7-b7e9-630111fdd861 | 1.5716 | -55.82184 | 2026-09-25 05:27:00 | NOAA-21 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| a5df944c-8f5c-3f3e-9118-a9cbafb5eb57 | 1.59796 | -56.01581 | 2026-09-25 05:27:00 | NOAA-21 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 78aa7061-3095-3e25-ac55-9581240bfd3b | 2.0979 | -50.97342 | 2026-09-25 05:27:00 | NOAA-21 | AMAPÁ | AMAPÁ | Brasil | 1600105 | 16 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 8cffbf2c-2fd0-3d05-8579-b191cc30da38 | 3.55996 | -61.16462 | 2026-09-25 05:27:00 | NOAA-21 | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 0.4 |
| c4f61176-fd3c-32a5-a6dc-07255c7ae7cd | 1.62462 | -55.95617 | 2026-09-25 05:27:00 | NOAA-21 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 73a1d204-5b03-3e85-b30f-0aaef185e000 | 2.00725 | -61.08874 | 2026-09-25 05:27:00 | NOAA-21 | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 49758f71-4a03-3e4e-bc7d-f5b611e38d43 | 0.49749 | -60.59731 | 2026-09-25 05:27:00 | NOAA-21 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 4.8 |
| b6a4f782-e8cc-3b27-83a9-c71ccdb35285 | 1.87374 | -50.66716 | 2026-09-25 05:27:00 | NOAA-21 | AMAPÁ | AMAPÁ | Brasil | 1600105 | 16 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 036a72d1-c28d-33f7-9261-bbff1157cdba | 1.6247 | -55.93075 | 2026-09-25 05:27:00 | NOAA-21 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| bb48ea33-d19e-31c5-9e08-41f2378b6e42 | -3.50023 | -50.74553 | 2026-09-25 05:27:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| e571217d-fe43-3043-8048-81b38c357f19 | -1.1262 | -54.14397 | 2026-09-25 05:27:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 6a033840-a50a-3d96-8f35-5680386da7da | 1.59516 | -50.90804 | 2026-09-25 05:27:00 | NOAA-21 | PRACUÚBA | AMAPÁ | Brasil | 1600550 | 16 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 905be627-10bd-328c-a6b3-e4953ee43777 | -1.15035 | -54.10538 | 2026-09-25 05:27:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 28c25589-8f43-3755-9fc3-5535fb5fd534 | -1.22243 | -54.56252 | 2026-09-25 05:27:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 6042a218-cf75-31dc-a4dd-e0f87099a7e8 | -1.53518 | -54.29509 | 2026-09-25 05:27:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 58a0b68f-6d37-3936-929f-7b0bec6a8f04 | 1.58163 | -56.0134 | 2026-09-25 05:27:00 | NOAA-21 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 9f0aef85-1a66-3d33-b743-48af7a47657c | 1.57084 | -55.81694 | 2026-09-25 05:27:00 | NOAA-21 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 997a815f-89c2-3a9e-a161-688d0f9d09bb | 1.61527 | -55.89413 | 2026-09-25 05:27:00 | NOAA-21 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 4bc5aaa3-576b-3d93-97cc-8330967615ec | 1.62776 | -55.95059 | 2026-09-25 05:27:00 | NOAA-21 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 39133353-7782-38c2-b6ae-aad4ff17f8ce | -1.15283 | -54.09429 | 2026-09-25 05:27:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| f9e277e5-4a3a-3248-8840-5d032e3b92bc | 1.55823 | -55.8138 | 2026-09-25 05:27:00 | NOAA-21 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| b86e4e23-3c8e-3c75-9376-88a642b1bc5a | -1.14746 | -54.09838 | 2026-09-25 05:27:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 9.0 |
| fee42ef6-d80f-30bd-97e1-f66132a8772e | -1.1525 | -54.09088 | 2026-09-25 05:27:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| ca9104df-fd65-3d44-94d8-64d466a8acc1 | 1.62699 | -55.94563 | 2026-09-25 05:27:00 | NOAA-21 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 587506a1-ea2c-3b0d-9985-ad34dee21a86 | 1.628 | -55.94813 | 2026-09-25 05:27:00 | NOAA-21 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| c359cb5f-a139-385c-a704-06ee3caf71f1 | -1.15179 | -54.09568 | 2026-09-25 05:27:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 00261c5e-355f-3ba1-a942-7b46240287e5 | -3.45463 | -50.07994 | 2026-09-25 05:27:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 9933589a-4189-38b3-8e74-a4e4376f5e0f | 1.62546 | -55.93572 | 2026-09-25 05:27:00 | NOAA-21 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 6aed1471-9e2c-3a5b-adae-0b133234e569 | -1.14788 | -54.09018 | 2026-09-25 05:27:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| b34bffb9-54e2-31ce-b670-e130cd6480ca | 1.6288 | -55.95308 | 2026-09-25 05:27:00 | NOAA-21 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 421ce6f4-9720-3f73-960c-b4da75afd1b8 | 1.61695 | -55.90649 | 2026-09-25 05:27:00 | NOAA-21 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 548b389b-ccf4-3029-a920-acdc58261835 | 1.57476 | -55.81618 | 2026-09-25 05:27:00 | NOAA-21 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 55c306fb-c7ca-3235-b8b5-4cda7f010834 | -1.14717 | -54.09496 | 2026-09-25 05:27:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| f2b97886-a362-3081-baf9-c70d286c7980 | -1.14645 | -54.09977 | 2026-09-25 05:27:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| e72eb9f3-921e-3547-b72b-0c1867146fea | 1.62401 | -55.92339 | 2026-09-25 05:27:00 | NOAA-21 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 99cfd32b-d9cb-3fd3-a53a-50f8ae3202e2 | 1.60763 | -55.87214 | 2026-09-25 05:27:00 | NOAA-21 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 538962ff-cfd9-3094-969c-748de7f5f2d0 | -1.62677 | -54.92754 | 2026-09-25 05:27:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 025ddb4f-12dd-3c26-b7c8-94fbbf059ab4 | -1.14671 | -54.10318 | 2026-09-25 05:27:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 9.0 |
| eea2b6da-36d7-34e6-943e-b8c8e585463e | 1.29606 | -50.843 | 2026-09-25 05:27:00 | NOAA-21 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 364542c0-7a41-33ae-b429-109b09837620 | 1.59719 | -56.01092 | 2026-09-25 05:27:00 | NOAA-21 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| ab36978a-db13-3e9d-a472-476e70a49e69 | 1.59407 | -56.01643 | 2026-09-25 05:27:00 | NOAA-21 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 7fa407af-adfa-3614-a74d-7ce12cb4647c | -3.20517 | -53.41687 | 2026-09-25 05:27:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| e3708205-c3aa-32b8-91e5-d8c36e2b7cf2 | 1.62504 | -56.00399 | 2026-09-25 05:27:00 | NOAA-21 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 3dc96e2b-ff79-328f-973e-a21ecc922e89 | -2.56467 | -49.08286 | 2026-09-25 05:27:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 35f21c16-a1dd-3b91-b3c2-f0f8b37f8751 | 1.61839 | -55.88853 | 2026-09-25 05:27:00 | NOAA-21 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 505cacb9-8ed3-34da-adc7-806f01d168b6 | 1.6272 | -55.94318 | 2026-09-25 05:27:00 | NOAA-21 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 560fcfbe-00ef-3679-9c18-f46d56ce503f | 1.62561 | -55.93329 | 2026-09-25 05:27:00 | NOAA-21 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 63613907-9c3a-3fcc-a6d6-db0cfb7bc804 | -1.14433 | -54.08813 | 2026-09-25 05:27:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 29415928-09fa-3e4f-9f01-71f10c94da79 | 3.07817 | -59.9714 | 2026-09-25 05:27:00 | NOAA-21 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 0.8 |
| d3a9d8d4-b564-336d-8e97-d81899d15359 | -3.4978 | -50.73843 | 2026-09-25 05:27:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 4fb29497-3c76-3d8f-bda8-c3db3a5ffd4a | 1.58552 | -56.01277 | 2026-09-25 05:27:00 | NOAA-21 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 4a4e956e-aa8d-385c-b21a-0350dc4514de | -1.14896 | -54.08881 | 2026-09-25 05:27:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 48339f41-8aa6-38de-84f5-470422fd2856 | 1.59668 | -55.85337 | 2026-09-25 05:27:00 | NOAA-21 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| ce1849b9-6c3a-3f38-8e53-926539a92964 | -1.14821 | -54.09359 | 2026-09-25 05:27:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |
| fbd70e3c-6dd3-3276-a9a2-588ce426d35f | -3.45229 | -50.08017 | 2026-09-25 05:27:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |


[Clique aqui para ver as próximas entradas](README31.md)
