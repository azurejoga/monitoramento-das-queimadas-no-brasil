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

## Dados Diários - Página 107

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| d59d938b-1e2f-38b5-8f35-44cdb8771fa2 | -11.1183 | -54.0062 | 2026-09-20 07:20:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 86.7 |
| ec946bf1-82fc-3f87-84b2-56c3e9513dec | -11.0991 | -54.0285 | 2026-09-20 07:20:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 334.2 |
| beaba9ed-e9ac-30f5-8f9f-0d5083312f1d | -10.3168 | -50.2352 | 2026-09-20 07:30:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 37.9 |
| 039a48a9-4dab-34c4-978d-6b6aa6b6db3c | -11.118 | -54.0268 | 2026-09-20 07:30:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 213.4 |
| d8c9a455-fd11-3e2c-968c-1aecd3cfe66e | -11.0802 | -54.0302 | 2026-09-20 07:30:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 69.6 |
| 60efecd3-b70b-3d1f-b999-8930aaa3d26a | -11.0991 | -54.0285 | 2026-09-20 07:30:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 211.4 |
| af286440-c582-31f1-a0f6-8809de77a147 | -11.1369 | -54.0251 | 2026-09-20 07:30:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 56.4 |
| b3640264-bad3-336c-a76a-36ffab8d7343 | -11.0994 | -54.008 | 2026-09-20 07:30:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 64.4 |
| 0e61432c-384a-375c-bbca-78330d134bcc | -11.1183 | -54.0062 | 2026-09-20 07:30:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 80.5 |
| e060f662-1d0b-323c-9b9c-a7f21441d9e9 | -11.1183 | -54.0062 | 2026-09-20 07:40:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 83.0 |
| fd6638c2-399a-346f-9900-9e9b3d0238e2 | -11.118 | -54.0268 | 2026-09-20 07:40:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 258.1 |
| ddc59f60-b27e-3233-a1c8-2afb9e20fe03 | -11.0994 | -54.008 | 2026-09-20 07:40:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 74.0 |
| e08fb8e7-ede9-369e-829d-6fd62aa16eab | -11.0802 | -54.0302 | 2026-09-20 07:40:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 55.2 |
| 0aa1d31e-f3b3-3e58-ba07-d6b7a85d8229 | -11.0991 | -54.0285 | 2026-09-20 07:40:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 261.8 |
| 511f067c-7d0d-3ded-864b-92b3a29e2062 | -11.1369 | -54.0251 | 2026-09-20 07:40:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 58.2 |
| bf038e16-b818-3afd-b81f-5f0b246db5e4 | -11.0994 | -54.008 | 2026-09-20 07:50:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 98.2 |
| 8d9fcbeb-36be-3a9a-8e40-5ed59b74b7cd | -14.0421 | -52.0812 | 2026-09-20 07:50:00 | GOES-19 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 77.9 |
| c6f9a4aa-ba3b-3904-af9e-aa33063a34d2 | -11.1183 | -54.0062 | 2026-09-20 07:50:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 82.7 |
| d96f4f6f-972e-3a40-8436-9d8a23753414 | -11.0991 | -54.0285 | 2026-09-20 07:50:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 233.5 |
| 6ff00407-7114-3e8d-a7a6-f3419919f019 | -11.118 | -54.0268 | 2026-09-20 07:50:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 179.9 |
| 7b2314a5-127c-3d25-8e79-c5b2ba2b2a40 | -10.41 | -48.933 | 2026-09-20 07:50:00 | GOES-19 | PUGMIL | TOCANTINS | Brasil | 1718451 | 17 | 33 | nan | nan | nan | Cerrado | 54.8 |
| 2a703a8e-d19e-3498-9119-a77cae821021 | 4.53302 | -60.87329 | 2026-09-20 07:58:00 | AQUA_M-M | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 7fdc0b03-a38e-30b7-94e6-106e3213d40c | -10.3168 | -50.2352 | 2026-09-20 08:00:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 132.9 |
| 4b4a7948-5b00-30c8-9692-3060bd1dd31b | -10.3171 | -50.2138 | 2026-09-20 08:00:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 42.2 |
| ba25d09a-0f9c-3c12-a2ff-ae94ef64cf85 | -10.3165 | -50.2566 | 2026-09-20 08:00:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 187.4 |
| 4941778c-c257-37a9-aacb-883505efc817 | -10.336 | -50.2119 | 2026-09-20 08:00:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 49.1 |
| 16ca303a-c29a-3dc9-8aa5-b46eeb1cb857 | -11.118 | -54.0268 | 2026-09-20 08:00:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 140.4 |
| fe49fa0b-0ce9-3506-a89d-4eee53cdc550 | -10.41 | -48.933 | 2026-09-20 08:00:00 | GOES-19 | PUGMIL | TOCANTINS | Brasil | 1718451 | 17 | 33 | nan | nan | nan | Cerrado | 74.6 |
| 1c9ef580-d1fd-31ff-be9e-7fe17189cf8d | -10.3354 | -50.2547 | 2026-09-20 08:00:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 36.7 |
| 418b1e84-b205-35f3-af08-094f1c591876 | -11.0994 | -54.008 | 2026-09-20 08:00:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 60.0 |
| 3be963cc-c949-3754-b329-5382f9cde398 | -11.0991 | -54.0285 | 2026-09-20 08:00:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 138.3 |
| 5c1fdc0a-6d2a-3f87-ae79-6b4e5b9111c0 | -10.2976 | -50.2585 | 2026-09-20 08:00:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 38.7 |
| 287033c4-9db3-38dc-86dd-269c1a55a3a0 | -11.1183 | -54.0062 | 2026-09-20 08:00:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 67.8 |
| 39c8ffe1-16bf-32a4-9d7f-0baf00c63f9b | -3.68898 | -60.58692 | 2026-09-20 08:03:00 | AQUA_M-M | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 10.2 |
| 9a317d49-b25e-3462-b0cc-faec2a88d39a | -9.03404 | -61.64317 | 2026-09-20 08:03:00 | AQUA_M-M | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 11.4 |
| ee46a363-aea3-32bd-9dc4-7bbc9b0ef3ef | -2.87322 | -57.81231 | 2026-09-20 08:03:00 | AQUA_M-M | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 27.0 |
| f66986eb-955f-31ad-8ab8-050b364fb659 | -3.68459 | -60.61778 | 2026-09-20 08:03:00 | AQUA_M-M | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 9.7 |
| 7f1eb4cb-67aa-33c4-89a4-393bfeef49b8 | -3.68678 | -60.60238 | 2026-09-20 08:03:00 | AQUA_M-M | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 12.6 |
| cda62900-274b-33e4-b796-dd50c71be7ac | -9.03182 | -61.65903 | 2026-09-20 08:03:00 | AQUA_M-M | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 14.8 |
| 1e06c135-3544-37fc-92aa-52744aa71a14 | -6.44949 | -59.97195 | 2026-09-20 08:03:00 | AQUA_M-M | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 18.0 |
| 62e0c6b4-7b14-36cb-b391-96d1a5e6403c | -2.88436 | -57.80648 | 2026-09-20 08:03:00 | AQUA_M-M | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 32.8 |
| 8013bfe9-b338-3b06-890e-ad8e0c784e92 | -9.03189 | -61.64812 | 2026-09-20 08:03:00 | AQUA_M-M | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 18.0 |
| f36e861b-3651-3a52-bc2f-97618427b268 | -6.43686 | -59.97015 | 2026-09-20 08:03:00 | AQUA_M-M | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 10.6 |
| a09b7ebb-7bf8-3cc8-a880-cdb2cbe99971 | -2.87672 | -57.78722 | 2026-09-20 08:03:00 | AQUA_M-M | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 30.8 |
| 4b0ed076-e000-31ec-adfb-095f3f8e3e17 | -11.0991 | -54.0285 | 2026-09-20 08:10:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 132.5 |
| 4b016057-f1fe-310f-a116-f7a8d5982147 | -11.118 | -54.0268 | 2026-09-20 08:10:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 143.4 |
| 0017dcc4-0fde-3a1e-b1fe-de879362ab30 | -12.152 | -47.0383 | 2026-09-20 08:10:00 | GOES-19 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 41.3 |
| 75e7429a-08aa-355d-bd37-a80bf6af7ccb | -10.32 | -50.22 | 2026-09-20 08:15:00 | MSG-03 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| f2abc474-c557-3094-8751-34eb93611113 | -10.3354 | -50.2547 | 2026-09-20 08:20:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 49.8 |
| 3b60fbb9-e327-3e9e-abc9-25c9adb1619d | -10.3165 | -50.2566 | 2026-09-20 08:20:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 83.2 |
| 67d81f13-5b27-34b2-9136-36c6400c993e | -10.3168 | -50.2352 | 2026-09-20 08:20:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 85.6 |
| fd0cff1a-36ab-3571-9ea2-0eed2206ecba | -11.0991 | -54.0285 | 2026-09-20 08:20:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 118.5 |
| 96a6dfb9-6c74-3f7c-9573-1fd277b8769d | -10.3357 | -50.2333 | 2026-09-20 08:20:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 63.2 |
| 7c266f5d-6a97-3804-93ed-caf0bfc35359 | -10.336 | -50.2119 | 2026-09-20 08:20:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 127.5 |
| 950cb2d9-64dc-3729-81c0-7bc8a7c3dacc | -11.118 | -54.0268 | 2026-09-20 08:20:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 117.8 |
| c9c2c098-718e-3228-bd22-2dbb7f4442da | -10.3171 | -50.2138 | 2026-09-20 08:20:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 98.2 |
| b62067b4-8109-3ce5-87ec-00490afdde83 | -11.0991 | -54.0285 | 2026-09-20 08:30:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 95.1 |
| e03100ad-f759-338b-ac74-9c712f7cbc3c | -11.118 | -54.0268 | 2026-09-20 08:30:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 93.3 |
| 9c4feacb-f008-3b6a-8dc4-fca0569da98a | -11.0991 | -54.0285 | 2026-09-20 08:40:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 79.0 |
| b2df77ea-2f70-31a4-8ffa-abd7e03c9b32 | -11.118 | -54.0268 | 2026-09-20 08:40:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 86.3 |
| c2c653cf-1b31-36d4-9070-93c1c8751963 | -11.118 | -54.0268 | 2026-09-20 08:50:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 59.5 |
| fb2abe01-33d9-34c2-8645-d4cd9459ffdf | -11.0991 | -54.0285 | 2026-09-20 08:50:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 73.4 |
| 531e4ab6-d047-39ad-80ba-b0fef7aa8fcb | -10.3357 | -50.2333 | 2026-09-20 09:20:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 141.0 |
| 18066db6-9fed-33e8-b6d2-099b72c1b10c | -10.3354 | -50.2547 | 2026-09-20 09:20:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 115.4 |
| a73ead3b-be0d-3940-8dab-d07c1ddead2b | -10.3168 | -50.2352 | 2026-09-20 09:30:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 109.1 |
| 4565015b-8e62-36db-9d10-47be8bfb3d45 | -10.3357 | -50.2333 | 2026-09-20 09:30:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 94.4 |
| cef3f8bb-c156-3f1c-9c40-fefd9acc9baf | -10.3354 | -50.2547 | 2026-09-20 09:40:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 308.7 |
| f2a91265-8adf-36d4-83ca-f359b3a76499 | -10.3357 | -50.2333 | 2026-09-20 09:40:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 262.5 |
| 2bba14a6-ced4-3a23-946e-5a87f6b89f0e | -10.3165 | -50.2566 | 2026-09-20 09:40:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 101.0 |
| e658ae9a-3522-3f87-b6f9-e1404bab7aa0 | -10.336 | -50.2119 | 2026-09-20 09:40:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 89.4 |
| fce84162-f87f-3eb2-ab2e-37e24d5753f5 | -10.3168 | -50.2352 | 2026-09-20 09:40:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 116.5 |
| 1871f6a3-79a9-35b6-87e8-6615dfe44422 | -10.3168 | -50.2352 | 2026-09-20 09:50:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 216.5 |
| fdee191b-a92b-3eae-8952-4f9687689120 | -10.3357 | -50.2333 | 2026-09-20 09:50:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 287.1 |
| be61fe78-c8f1-3742-b4c1-053af3405abd | -10.3171 | -50.2138 | 2026-09-20 09:50:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 101.5 |
| c8337471-9575-3128-8d5b-b075d5f7dc84 | -10.3354 | -50.2547 | 2026-09-20 09:50:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 379.8 |
| dbb2b4cb-4091-3822-9fec-2b31166b8be7 | -10.336 | -50.2119 | 2026-09-20 09:50:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 114.8 |
| d64b9243-7d53-36b0-b507-54d3852e1d73 | -10.3165 | -50.2566 | 2026-09-20 09:50:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 226.7 |
| 02a10ff0-fb6a-3f72-a731-7b05773ceac3 | -12.152 | -47.0383 | 2026-09-20 10:00:00 | GOES-19 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 89.5 |
| 76823c09-2678-3f9a-8056-de82d8b9802e | -10.3354 | -50.2547 | 2026-09-20 10:00:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 196.1 |
| e405093c-27af-3361-b45e-3730b8fafbc5 | -10.336 | -50.2119 | 2026-09-20 10:00:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 172.5 |
| 4cac258c-9f02-3cfc-b10c-8073c8e0365c | -10.336 | -50.2119 | 2026-09-20 10:10:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 128.7 |
| eaaec01b-c04a-3ef7-a413-1bc4957428f7 | -10.3357 | -50.2333 | 2026-09-20 10:10:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 186.6 |
| 3a7c5e5f-bc2a-3b60-954e-46026756415f | -12.1328 | -47.041 | 2026-09-20 10:10:00 | GOES-19 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 89.0 |
| 78bd522b-8fbf-3f9b-9e43-427c0a69a22a | -10.3354 | -50.2547 | 2026-09-20 10:20:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 91.4 |
| 4df57d84-b3d0-3979-a84f-24ca6473680e | -7.5337 | -45.4141 | 2026-09-20 10:20:00 | GOES-19 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 113.8 |
| 07ccf584-f011-37a1-b43f-592dcf8bc35c | -10.3357 | -50.2333 | 2026-09-20 10:20:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 126.6 |
| 4146d16e-95fb-3e21-a9bf-18d788506fd3 | -7.5334 | -45.4367 | 2026-09-20 10:20:00 | GOES-19 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 92.6 |
| efea65b7-7137-3edd-ad09-0bd9482be1c2 | -10.3168 | -50.2352 | 2026-09-20 10:30:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 81.9 |
| 23aafc4b-72b9-3553-9d7a-5d1375b15946 | -10.336 | -50.2119 | 2026-09-20 10:30:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 84.2 |
| a21f15bd-ae3e-3d51-b453-dd364d65d716 | -7.5334 | -45.4367 | 2026-09-20 10:30:00 | GOES-19 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 87.3 |
| 0d6c513f-f276-38f3-89bb-f8d618d4b339 | -10.3354 | -50.2547 | 2026-09-20 10:30:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 118.2 |
| 4ac24a9a-c1fe-302e-aeac-fbeb803427a8 | -10.3357 | -50.2333 | 2026-09-20 10:30:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 179.3 |
| cfab57df-6496-3ea0-a264-25a564a82f4c | -10.3357 | -50.2333 | 2026-09-20 10:40:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 105.4 |
| 18315e94-70ab-3c70-a112-0ea4666d5c33 | -7.5337 | -45.4141 | 2026-09-20 10:40:00 | GOES-19 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 100.9 |
| 148db916-6c0b-3ff4-bc5b-f9128507d0df | -14.6661 | -46.6919 | 2026-09-20 10:40:00 | GOES-19 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 112.3 |
| dd970596-91a7-3c61-94e0-764adfe2bc4e | -10.3168 | -50.2352 | 2026-09-20 10:40:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 94.7 |
| ea20c3f2-4806-3a8f-9c8c-1f97690be2e7 | -7.5334 | -45.4367 | 2026-09-20 10:40:00 | GOES-19 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 112.9 |
| d8365578-f74f-3f43-81bd-3b4606a5c09c | -10.3168 | -50.2352 | 2026-09-20 10:50:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 136.2 |
| 4b2aea9e-4e49-3e58-9203-c9e795b1c7e4 | -7.5334 | -45.4367 | 2026-09-20 10:50:00 | GOES-19 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 92.0 |
| bd9e921e-f9b2-3ec6-a7f8-eb140760d519 | -10.8659 | -50.1775 | 2026-09-20 10:50:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 94.7 |


[Clique aqui para ver as próximas entradas](README108.md)
