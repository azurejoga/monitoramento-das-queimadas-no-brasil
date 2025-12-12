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

## Dados Diários - Página 25

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 311d87d0-693f-3a40-90db-ffed7979abd5 | -1.29313 | -53.16262 | 2025-12-12 05:37:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 033c6808-b1f7-389d-9f60-7c2acb6017bb | -1.3416 | -54.60776 | 2025-12-12 05:37:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 1b146377-c82c-37c3-8db4-e997266ccd5a | -1.1115 | -53.68604 | 2025-12-12 05:37:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 89aab869-206d-33cd-b9e8-d26b14a55e16 | -1.03366 | -53.73895 | 2025-12-12 05:37:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 376dc0ce-0a95-313a-b3f8-2cb461309c70 | 4.08136 | -60.81148 | 2025-12-12 05:37:00 | NPP-375D | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 5f17b094-9fd3-3de0-ba91-1e1e3b6b2a76 | 1.12749 | -60.5242 | 2025-12-12 05:37:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 4940ef82-2943-3963-99c2-82066ab3060e | -1.76292 | -54.04069 | 2025-12-12 05:37:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 7c6b28dd-b1a3-3a8a-afc8-92f82ae71e2e | -1.03416 | -53.73574 | 2025-12-12 05:37:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| b6251288-3e23-3bbd-838e-bfa88adbbf1d | 4.00636 | -60.82713 | 2025-12-12 05:37:00 | NPP-375D | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 55bc388c-29be-3108-aac3-84b6beef539a | 0.46305 | -60.43182 | 2025-12-12 05:37:00 | NPP-375D | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 6d98a8c8-c673-336e-9f9e-acf6ae6aa679 | 0.55478 | -60.3954 | 2025-12-12 05:37:00 | NPP-375D | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 966a986b-e284-315f-a873-7027fbee1c78 | -1.1158 | -53.69325 | 2025-12-12 05:37:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 0fb9b9fa-561f-3147-abc6-984e6a9328c8 | 0.45847 | -60.42501 | 2025-12-12 05:37:00 | NPP-375D | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 4f5bbe18-9428-3c56-9c2a-d834b6e0c4d3 | 3.2219 | -61.19561 | 2025-12-12 05:37:00 | NPP-375D | ALTO ALEGRE | RORAIMA | Brasil | 1400050 | 14 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 07683307-78a1-3824-8a2d-51dffcc26423 | -1.3466 | -54.60844 | 2025-12-12 05:37:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 40348e97-666f-3b8e-9903-6916dbb51492 | -1.76327 | -54.03902 | 2025-12-12 05:37:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 949a370b-c397-3a4a-ae3a-2e3645f32ff5 | -12.3946 | -58.0307 | 2025-12-12 05:40:00 | GOES-19 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 83.1 |
| 52fde219-7bde-338a-b4e1-8aee90002299 | -2.4183 | -51.9278 | 2025-12-12 05:40:00 | GOES-19 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 66.7 |
| 5b74f848-e8e3-3a6f-a49c-9da202d7f16e | -12.4323 | -58.0475 | 2025-12-12 05:40:00 | GOES-19 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 43.1 |
| 67e201ad-5889-3b41-b995-12020ddfafc5 | -14.9134 | -58.1263 | 2025-12-12 05:40:00 | GOES-19 | SALTO DO CÉU | MATO GROSSO | Brasil | 5107750 | 51 | 33 | nan | nan | nan | Amazônia | 49.1 |
| 608c4bb7-e0c6-3138-ab56-32bad0dd3e9e | -12.4135 | -58.0292 | 2025-12-12 05:40:00 | GOES-19 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 91.8 |
| ab670ae6-a1f0-3b44-b845-6296530aa375 | -2.4367 | -51.9274 | 2025-12-12 05:40:00 | GOES-19 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 86.0 |
| d8ae1db6-e25e-3faa-b85c-55b9c2a84aee | -2.4923 | -51.8027 | 2025-12-12 05:40:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 36.8 |
| 29ad386e-c6d1-3419-951a-2883fe59f8cb | -14.8941 | -58.1282 | 2025-12-12 05:40:00 | GOES-19 | SALTO DO CÉU | MATO GROSSO | Brasil | 5107750 | 51 | 33 | nan | nan | nan | Amazônia | 43.3 |
| ec41cd9b-98a1-3ae8-bbbc-78e0ad346837 | -12.3943 | -58.0506 | 2025-12-12 05:40:00 | GOES-19 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 49.5 |
| d15f8eea-0f69-3a6c-9681-f7d70a4d7eea | -12.4325 | -58.0276 | 2025-12-12 05:40:00 | GOES-19 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 60.2 |
| b83418f8-dafd-312c-8e22-e6f2d2332adb | -12.4133 | -58.049 | 2025-12-12 05:40:00 | GOES-19 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 61.0 |
| 5cf7c8f8-bc3f-356d-8aa2-b764a3d1bf66 | -2.4367 | -51.948 | 2025-12-12 05:40:00 | GOES-19 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 34.5 |
| 8c563d6d-3d2c-3dce-be37-65dc3fe5d774 | -2.6099 | -58.16119 | 2025-12-12 05:40:00 | NPP-375D | ITAPIRANGA | AMAZONAS | Brasil | 1302009 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e95a2c12-11c5-399f-9a77-5834a4244e50 | -2.69054 | -59.42682 | 2025-12-12 05:40:00 | NPP-375D | RIO PRETO DA EVA | AMAZONAS | Brasil | 1303569 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 497e40d4-cf62-3314-bdb6-52c14f487d9a | -2.65644 | -51.64169 | 2025-12-12 05:40:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 0429f05d-7133-3f8b-b488-58dbb08cc7b6 | -2.74939 | -52.97541 | 2025-12-12 05:40:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 426d731f-182d-39ad-806e-3952de443a8a | -1.38608 | -60.28705 | 2025-12-12 05:40:00 | NPP-375D | PRESIDENTE FIGUEIREDO | AMAZONAS | Brasil | 1303536 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d78b6570-07f9-369a-92d4-39b324fd19f5 | -7.56561 | -55.35278 | 2025-12-12 05:40:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d4273876-ce03-3626-a324-63551e9850b3 | -2.42694 | -51.92945 | 2025-12-12 05:40:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 8.6 |
| 65bbd4d3-0936-3ecd-9972-3fe3213bfcbe | -3.81237 | -58.99499 | 2025-12-12 05:40:00 | NPP-375D | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| c0a7c641-cb44-3b06-bd89-78ec8f9c4bdc | -2.65575 | -51.64647 | 2025-12-12 05:40:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 9092a9de-cfee-3aa8-8c6f-b9bbece6c80a | -2.433 | -51.93032 | 2025-12-12 05:40:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 8.6 |
| 1e84242a-86d1-3f97-8625-b6f4d7530e04 | -6.56156 | -56.13765 | 2025-12-12 05:40:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 5b018a29-bcb1-363c-8ff9-1feddb768a1f | -2.4337 | -51.92561 | 2025-12-12 05:40:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 8.1 |
| 40f19dc0-01bb-3105-8f2b-675ae9b22ec5 | -2.14754 | -53.76068 | 2025-12-12 05:40:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| ed18ef51-9e5e-3be7-b8fe-fbbeb8e9cb0f | -2.43232 | -51.93488 | 2025-12-12 05:40:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 8.6 |
| 0308d20d-2a37-3947-aa89-62d9070c440d | -2.50162 | -51.80537 | 2025-12-12 05:40:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| ae5b367e-1c10-3b1a-ac69-a3fe95cc82ec | -2.74373 | -52.97441 | 2025-12-12 05:40:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 24ca34ce-b236-3e3f-b35b-76f608e22249 | -2.50304 | -51.79608 | 2025-12-12 05:40:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 4f283561-af40-38c3-b84b-cc23532aeb6c | -7.56145 | -55.34543 | 2025-12-12 05:40:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| af647a97-5a9c-324a-95ac-cfe9b2dcac4f | -2.15288 | -53.76157 | 2025-12-12 05:40:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| cb8c5b99-70fc-3ec1-bcb3-476ef4c7307a | -2.42447 | -51.9363 | 2025-12-12 05:40:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 9.2 |
| 287f8044-c0cc-3e74-b307-5fe51a0e8426 | -2.42765 | -51.92461 | 2025-12-12 05:40:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 8.1 |
| 4672a7bb-b6fe-3905-b2c2-f7bb3484b6fb | -3.15384 | -54.60411 | 2025-12-12 05:40:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| a67b3d54-e169-3a0e-ad72-4f3718ed7507 | -3.15896 | -54.60487 | 2025-12-12 05:40:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 0.3 |
| 71200aa6-8504-3d70-a125-92ca6353ec11 | -2.15238 | -53.76491 | 2025-12-12 05:40:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 249a44b7-9f9e-3c9a-b463-9e0e5e9241bf | -7.56581 | -55.35247 | 2025-12-12 05:40:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f518eea9-fee6-3624-a860-babe7b2f977a | -6.52119 | -55.04048 | 2025-12-12 05:40:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| e2f9f4e0-e740-3ac3-b4e6-514460556093 | -7.5613 | -55.34576 | 2025-12-12 05:40:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 4408568c-7f60-3062-bb21-7258b3465086 | -2.49551 | -51.80447 | 2025-12-12 05:40:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 87997fa1-fee0-3abc-872b-377720e0b124 | -2.9714 | -52.7208 | 2025-12-12 05:40:00 | NPP-375D | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| f2717f21-30f8-3cb2-bff7-46894120fef5 | -3.0202 | -52.828 | 2025-12-12 05:40:00 | NPP-375D | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| ffa5cb26-bf51-364a-ae39-ecbe2955ac8d | -3.34041 | -53.33623 | 2025-12-12 05:40:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b853e388-81c9-3935-93c4-62087fc564fc | -7.5665 | -55.34654 | 2025-12-12 05:40:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 983fd5c4-4427-3725-8d63-53c1c56b7159 | -2.41984 | -51.92621 | 2025-12-12 05:40:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 8651b829-6a11-3f58-9c94-6c8b20c0d89b | -6.51596 | -55.03969 | 2025-12-12 05:40:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 97595e1c-a66c-3be8-8cbc-8b803cf8e833 | -2.49621 | -51.79982 | 2025-12-12 05:40:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 4fb6935f-7780-3a58-bd0f-d083327865cd | -2.42626 | -51.93397 | 2025-12-12 05:40:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 8.6 |
| 13e0f1b2-784a-3208-9c68-363f639d710f | -2.42021 | -51.93301 | 2025-12-12 05:40:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 646c40ab-a03d-3818-8d3a-73e554d908f2 | -2.42089 | -51.92845 | 2025-12-12 05:40:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 2f4b0e51-fe62-34eb-ad23-d246d8d754bd | -2.50233 | -51.80071 | 2025-12-12 05:40:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 7b2ca830-555c-3d47-b96a-4a4d7d24f44b | -3.0138 | -52.83151 | 2025-12-12 05:40:00 | NPP-375D | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| e6d01eb2-a01b-3af0-b594-dc978dfd9d9b | -2.42665 | -51.92234 | 2025-12-12 05:40:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| aee3edd1-380c-3306-ae13-baa44d377f00 | -6.51642 | -55.0365 | 2025-12-12 05:40:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 3b9fc29d-bb91-385c-b40f-4758f66a7f6e | -2.42589 | -51.9272 | 2025-12-12 05:40:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 3f368e99-9a81-3ef0-98d7-9f121818d6b3 | -2.42559 | -51.93849 | 2025-12-12 05:40:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 7.4 |
| 3712f1ab-1557-3e4f-b513-b5c11528dd01 | -2.42158 | -51.92381 | 2025-12-12 05:40:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| bb0e1db7-12ab-3f40-b240-cebd9fb02f73 | -2.42517 | -51.93177 | 2025-12-12 05:40:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 9.2 |
| d6de8a63-93cd-344a-a1b9-647c6fa368f2 | -3.0208 | -52.82388 | 2025-12-12 05:40:00 | NPP-375D | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 5a41bf13-d18e-33d9-aef0-0501d4f955c4 | -3.0174 | -65.4639 | 2025-12-12 05:40:00 | NPP-375D | UARINI | AMAZONAS | Brasil | 1304260 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 0d23cd1d-6574-3ea7-98df-36289c885947 | -2.49692 | -51.79519 | 2025-12-12 05:40:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 845b3f0a-7985-3e6c-976b-f0b699352fa9 | -2.43907 | -51.93118 | 2025-12-12 05:40:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 70ecece7-299f-342c-819e-7d6d4ed97f46 | -12.38692 | -58.03975 | 2025-12-12 05:42:00 | NPP-375D | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 11.6 |
| 3cc3d6ef-f650-3959-a53d-674cc5f4fb1f | -14.89466 | -58.12908 | 2025-12-12 05:42:00 | NPP-375D | SALTO DO CÉU | MATO GROSSO | Brasil | 5107750 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ae110721-f39b-35ae-8f03-b4e9fd1bc822 | -12.39684 | -58.03627 | 2025-12-12 05:42:00 | NPP-375D | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 0050230f-905d-356d-b9bb-4bff348b0489 | -14.90486 | -58.12516 | 2025-12-12 05:42:00 | NPP-375D | SALTO DO CÉU | MATO GROSSO | Brasil | 5107750 | 51 | 33 | nan | nan | nan | Amazônia | 10.7 |
| 55890fc8-52c7-3d38-9efb-214eb3e2ff4b | -12.41541 | -58.03886 | 2025-12-12 05:42:00 | NPP-375D | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 067872c4-932b-3683-a2f8-b7503e03b443 | -12.51348 | -58.34928 | 2025-12-12 05:42:00 | NPP-375D | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| b8798182-f5eb-378e-a878-63e4c03f8294 | -12.38292 | -58.03423 | 2025-12-12 05:42:00 | NPP-375D | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 07082f09-57d3-35f9-8ded-f049379bd85b | -11.88045 | -57.01903 | 2025-12-12 05:42:00 | NPP-375D | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| e86ec3e3-802e-375e-8c61-73bd163709f1 | -12.62346 | -58.08335 | 2025-12-12 05:42:00 | NPP-375D | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 489f5add-bcda-3acb-b17b-483dba8a4f88 | -12.62703 | -58.08043 | 2025-12-12 05:42:00 | NPP-375D | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 4ba74895-6ed1-347f-9b95-8ee893e34465 | -14.89944 | -58.12975 | 2025-12-12 05:42:00 | NPP-375D | SALTO DO CÉU | MATO GROSSO | Brasil | 5107750 | 51 | 33 | nan | nan | nan | Amazônia | 10.7 |
| 63035d93-19c2-3002-9fa5-f51299fc33c4 | -13.42965 | -56.83349 | 2025-12-12 05:42:00 | NPP-375D | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Cerrado | 0.4 |
| c86771b4-5de2-3afa-8812-7a16850f0a36 | -14.90422 | -58.1304 | 2025-12-12 05:42:00 | NPP-375D | SALTO DO CÉU | MATO GROSSO | Brasil | 5107750 | 51 | 33 | nan | nan | nan | Amazônia | 10.7 |
| 24f3e719-c48f-37ce-a37b-3ad2012bc045 | -12.42998 | -58.03606 | 2025-12-12 05:42:00 | NPP-375D | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 0.6 |
| dcb02229-1236-3dfd-81a3-13258ae97d3e | -12.38756 | -58.03493 | 2025-12-12 05:42:00 | NPP-375D | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 8.2 |
| aa479150-02f7-39a7-b949-68689636c359 | -12.41077 | -58.03822 | 2025-12-12 05:42:00 | NPP-375D | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| ee13309d-7925-3368-a686-ba11dbbc4eb8 | -12.41476 | -58.0437 | 2025-12-12 05:42:00 | NPP-375D | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 9c091de2-8d81-31a9-8cbe-3f2c4b6f93c0 | -11.8755 | -57.01841 | 2025-12-12 05:42:00 | NPP-375D | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 40393c32-13ea-3c2c-8090-19b5b7930a80 | -12.62812 | -58.08386 | 2025-12-12 05:42:00 | NPP-375D | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 3.3 |
| afc6b8a6-a2ce-3379-9fce-260a10d7ee35 | -11.87624 | -57.01272 | 2025-12-12 05:42:00 | NPP-375D | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f52496da-66ac-397c-99a2-c84779e37b00 | -12.448 | -63.63321 | 2025-12-12 05:42:00 | NPP-375D | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 774cab3f-e1ed-37d1-9e07-d340468f16a5 | -12.62642 | -58.08524 | 2025-12-12 05:42:00 | NPP-375D | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 6.8 |


[Clique aqui para ver as próximas entradas](README26.md)
