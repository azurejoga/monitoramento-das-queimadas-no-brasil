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

## Dados Diários - Página 29

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| ceef3703-1f84-3d8e-b6b7-2a468e788f84 | -2.59484 | -50.02922 | 2024-10-20 04:29:00 | NPP-375D | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 045ad435-528a-3817-8883-100b3574e9c8 | -2.56811 | -49.21642 | 2024-10-20 04:29:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| c4eda9b7-aeba-34e9-b8de-edd33452b791 | -2.56462 | -49.21587 | 2024-10-20 04:29:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 3f4637c7-3c92-3340-b7bf-d7e213a3162f | -2.55678 | -49.17539 | 2024-10-20 04:29:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| d3d488d3-bc7e-3f29-ad3d-03b1f468f6fd | -2.55617 | -49.17921 | 2024-10-20 04:29:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 8fd09fc5-abb9-333a-a7ff-aabbb862ac4d | -2.53142 | -50.10052 | 2024-10-20 04:29:00 | NPP-375D | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 635344df-c69b-3d71-9033-efbd9bd82804 | -2.51839 | -49.13868 | 2024-10-20 04:29:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| ce5f2e71-97e8-305d-8088-fdb496efd157 | -2.49832 | -49.28923 | 2024-10-20 04:29:00 | NPP-375D | MOCAJUBA | PARÁ | Brasil | 1504604 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 4a6fb1f1-af96-31ec-b796-e312e7e9bdc8 | -2.47799 | -49.10104 | 2024-10-20 04:29:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 18.5 |
| 8d5f5879-0960-338e-9200-55e18893fcc5 | -2.47451 | -49.10049 | 2024-10-20 04:29:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 18.5 |
| 3339098b-2929-3dba-908c-444e10af93dc | -2.46668 | -49.06029 | 2024-10-20 04:29:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 6e777a22-a8b4-36cd-8cf3-e6ededc309d5 | -2.39469 | -49.14759 | 2024-10-20 04:29:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 67785368-4b33-3937-adc8-9c89adbf055b | -2.3945 | -49.08102 | 2024-10-20 04:29:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e12db666-b290-3212-b237-aaa998c5486d | -2.3906 | -49.15088 | 2024-10-20 04:29:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b720b575-21f2-384a-931e-7b68fc50fe30 | -2.38363 | -49.14977 | 2024-10-20 04:29:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 6abba999-d50d-30fd-8b9d-bed351521d8e | -2.36149 | -49.80923 | 2024-10-20 04:29:00 | NPP-375D | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 12b1742c-4dfb-3ee6-83ce-58e49c2ce40f | -2.34033 | -49.10765 | 2024-10-20 04:29:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 1a222fb9-06cb-3566-b8f4-2eccc9d688ff | -2.33562 | -49.11474 | 2024-10-20 04:29:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| a0e984ce-5f20-3e3a-991a-c2ed7fe30ba5 | -2.22048 | -49.87689 | 2024-10-20 04:29:00 | NPP-375D | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| fea7467d-e7e8-334a-8da6-7acddf9b8731 | -2.20481 | -50.30359 | 2024-10-20 04:29:00 | NPP-375D | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 9f36efc2-60a0-3dd2-a3c5-c10ad648f289 | 1.13512 | -51.0308 | 2024-10-20 04:29:00 | NPP-375D | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 1.4 |
| e36deba2-8bb5-3def-ada9-24beae00799f | 1.1246 | -51.04323 | 2024-10-20 04:29:00 | NPP-375D | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b065fdc9-60e5-315e-a0b5-88aebac7fa12 | 1.12456 | -51.04288 | 2024-10-20 04:29:00 | NPP-375D | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 1.2 |
| be8af417-0aec-3211-95d1-a5c4e03680cc | -2.23246 | -50.44925 | 2024-10-20 04:29:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 70f7e9a2-f057-3fb3-9747-4113b92f0e21 | -2.22803 | -50.45303 | 2024-10-20 04:29:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| ead1d603-b00a-3ff8-b9c3-0aed9f8b71be | -2.22431 | -50.45245 | 2024-10-20 04:29:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| b6fbd096-bb09-3284-a023-2b53916e9c88 | -2.22288 | -50.46126 | 2024-10-20 04:29:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 3436c773-5472-352a-bcce-f3b3454f1651 | -2.22216 | -50.46567 | 2024-10-20 04:29:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| f9e8a8f5-1c33-3d1a-bb8a-b9e4090de66c | -2.21242 | -50.4551 | 2024-10-20 04:29:00 | NPP-375D | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| b7169c4e-c55b-30da-826a-da601cafd5ed | -2.21176 | -50.45272 | 2024-10-20 04:29:00 | NPP-375D | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 44bb3d59-2ef4-357c-980d-a3907d87d6bc | -2.2117 | -50.45953 | 2024-10-20 04:29:00 | NPP-375D | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 28ead9b1-1840-3927-b5a0-56e200e5bea6 | -2.21107 | -50.45714 | 2024-10-20 04:29:00 | NPP-375D | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| a5b14d4c-d818-3c38-bf1d-acb12e69028e | -2.21098 | -50.46394 | 2024-10-20 04:29:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| c95d4b09-d2c6-32ad-986b-e39b01734c3c | -2.21038 | -50.46157 | 2024-10-20 04:29:00 | NPP-375D | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 9a761f05-6cc2-398b-bef3-85d23abb0fd2 | -2.20969 | -50.46598 | 2024-10-20 04:29:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| aea458ba-5f76-3416-bd27-c4bbe3bad416 | -2.2087 | -50.4545 | 2024-10-20 04:29:00 | NPP-375D | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 7.3 |
| 5b8c43c9-8b19-3264-a5c9-f0d6b411aa8b | -2.20804 | -50.45211 | 2024-10-20 04:29:00 | NPP-375D | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 428551b0-216b-30e7-958e-226f98ecb573 | -2.20798 | -50.45892 | 2024-10-20 04:29:00 | NPP-375D | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 26b16a88-9d7c-3874-8b1a-da50f1bb17ac | -2.20735 | -50.45654 | 2024-10-20 04:29:00 | NPP-375D | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 5a030401-31d4-34d5-9ab6-5738f1188231 | -2.20726 | -50.46333 | 2024-10-20 04:29:00 | NPP-375D | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| fbf84633-f8ca-3fcb-bc19-6c9be1c01e8d | -2.20666 | -50.46095 | 2024-10-20 04:29:00 | NPP-375D | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 5502046c-c7e3-3c19-9ea7-e8b1f9f43a6a | -2.20654 | -50.46774 | 2024-10-20 04:29:00 | NPP-375D | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| e5ff49a9-f1fa-3721-a2a9-fa593c713a67 | -2.20597 | -50.46537 | 2024-10-20 04:29:00 | NPP-375D | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 4f18c145-f562-309f-a418-bc22620c310e | -2.20426 | -50.45831 | 2024-10-20 04:29:00 | NPP-375D | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 6afdb587-ae27-3252-b524-6a88dacc008c | -2.20354 | -50.46273 | 2024-10-20 04:29:00 | NPP-375D | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 2a3671ed-c6df-367b-be11-e00ddd78e3b9 | -2.20293 | -50.46035 | 2024-10-20 04:29:00 | NPP-375D | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 8ae1f739-9af4-339c-a27b-35fd88ab4f5f | -2.19693 | -50.52311 | 2024-10-20 04:29:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 3d463f69-8b46-3bef-99ba-f05f4e7acf1a | -2.17004 | -50.52341 | 2024-10-20 04:29:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e6eee2da-8836-3430-a79b-a00229554f3d | -2.1663 | -50.52283 | 2024-10-20 04:29:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 7700ef3f-8c2d-3663-b82e-e23e9fca69b4 | -2.14223 | -50.69925 | 2024-10-20 04:29:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 52f8946c-23b2-3773-b2ea-5fe87fd0c812 | -2.12962 | -50.85315 | 2024-10-20 04:29:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| ad157cff-e4fe-32fe-be28-07ca3f7d8ac6 | -2.12171 | -50.8043 | 2024-10-20 04:29:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| bcc98f4b-669c-3612-9420-3b63f172c7cf | -1.74492 | -51.16167 | 2024-10-20 04:29:00 | NPP-375D | MELGAÇO | PARÁ | Brasil | 1504505 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 4e4f436a-e366-3f50-baf5-98991dcf2463 | -2.90128 | -50.70744 | 2024-10-20 04:29:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 00a40f76-4e3d-30d0-a8ea-654800bd20a8 | -2.87347 | -51.6143 | 2024-10-20 04:29:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 03220843-f9bc-3936-821f-39c20cc15eaf | -2.85377 | -51.28749 | 2024-10-20 04:29:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 04ac2935-dff3-396c-ab51-e6dd518ffe97 | -2.84989 | -51.28688 | 2024-10-20 04:29:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| be1fdae8-eda7-3949-8600-15a1099e97a4 | -2.83897 | -51.30493 | 2024-10-20 04:29:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| a4740fb5-c2bd-3d4a-9905-7c9c831f22f1 | -2.83855 | -51.30269 | 2024-10-20 04:29:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 18c93402-4f00-326a-81f2-d1e392d8ea41 | -2.83779 | -51.30754 | 2024-10-20 04:29:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| aea86b59-3535-396b-b16d-03bdcd59a427 | -2.83589 | -51.29948 | 2024-10-20 04:29:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| e871f279-2c5f-3d0f-8177-46a5650bd3ae | -2.83509 | -51.30432 | 2024-10-20 04:29:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| ffed8e4c-6058-3ec9-bca8-1258374a6f2e | -2.83467 | -51.30208 | 2024-10-20 04:29:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| cfcb2106-fe5b-3b51-a3b1-9773538b06be | -2.83391 | -51.30692 | 2024-10-20 04:29:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 220ee11d-ec76-37fb-83fd-950025bab48f | -2.82742 | -51.27839 | 2024-10-20 04:29:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| ea823535-f3ba-34c3-9d55-524f208bb4d6 | -2.82683 | -51.2761 | 2024-10-20 04:29:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| e5db6844-7b58-3323-a546-dedea2e5f126 | -2.82015 | -51.34667 | 2024-10-20 04:29:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 49649c59-d5dc-3abb-8c50-29dd129c06ab | -2.82002 | -51.3445 | 2024-10-20 04:29:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 5e8d99df-e61b-356c-90a4-bd27fb413672 | -2.81925 | -51.34939 | 2024-10-20 04:29:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 8a956595-7180-3e11-8902-839f19882211 | -2.81706 | -51.34119 | 2024-10-20 04:29:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| ad971d9c-7e2b-3bc8-92b5-dfb8b3b152a1 | -2.81689 | -51.33902 | 2024-10-20 04:29:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 9855af75-8908-33b6-955c-aec80d678573 | -2.81625 | -51.34605 | 2024-10-20 04:29:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| b197a025-6ec6-389a-8439-ceb6fc2908b0 | -2.81613 | -51.34388 | 2024-10-20 04:29:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| ecf861b2-b604-3b10-a514-bc1989ffeff0 | -2.81536 | -51.34876 | 2024-10-20 04:29:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 9e0e09f3-9d42-3ae9-8543-f46aa0cca82b | -2.813 | -51.33839 | 2024-10-20 04:29:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| f3930cdd-9de8-31fa-a455-4f2bf232c6ae | -2.81223 | -51.34326 | 2024-10-20 04:29:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 49e38e44-291e-32da-8b7b-38d6f7dd95aa | -2.81146 | -51.34813 | 2024-10-20 04:29:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| a0ecfa85-c885-3520-8f99-ddb3af7d4aaa | -2.80468 | -51.01987 | 2024-10-20 04:29:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 5a563f56-2f08-388a-92c3-4891dcb779f8 | -2.80225 | -51.60291 | 2024-10-20 04:29:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 92d77025-4374-3a2f-ba20-eb32ba61ab58 | -2.80212 | -51.35663 | 2024-10-20 04:29:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 689af5b9-0bb6-3b7b-a024-35c30e4fb885 | -2.80135 | -51.36152 | 2024-10-20 04:29:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| b1acdee6-0880-3ac8-8497-f475575fe8c7 | -2.79823 | -51.35601 | 2024-10-20 04:29:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| c9d7fefc-60e8-3f0a-b5cf-ea0f1732c55c | -2.79745 | -51.3609 | 2024-10-20 04:29:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 4c09662b-c1bd-3a50-80f0-23dc8cdb936e | -2.79355 | -51.36028 | 2024-10-20 04:29:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| b591682f-ec71-343a-9ff6-c2bf2658d94b | -2.79277 | -51.36516 | 2024-10-20 04:29:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 4b7ece56-f5f3-3d78-94e6-5b8e53cfb22f | -2.78965 | -51.35965 | 2024-10-20 04:29:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 512fcf6b-e528-37f4-90c6-9c9cebc8a936 | -2.78887 | -51.36453 | 2024-10-20 04:29:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 11.1 |
| 1ef09901-be90-3e96-966d-c8fdd7e18682 | -2.77112 | -51.97107 | 2024-10-20 04:29:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 6.3 |
| a0a390f3-c037-3b2d-abf2-0488eac94ec9 | -2.76707 | -51.97041 | 2024-10-20 04:29:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| fe7e8867-8c1e-387c-a62d-b6d189e39fe0 | -2.70427 | -51.34426 | 2024-10-20 04:29:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d2e89c2c-dda8-359d-85fb-dea5f00e9e00 | -2.62151 | -51.7637 | 2024-10-20 04:29:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| d7f67c77-53f2-3120-8e89-79e93c9fe0b6 | -2.59553 | -51.84897 | 2024-10-20 04:29:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e3e4afd9-d5aa-312f-b817-d3db18685293 | -2.5524 | -51.24295 | 2024-10-20 04:29:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| afd6b5cf-e3dd-350f-ba5a-4ea65b83db78 | -2.45705 | -50.99524 | 2024-10-20 04:29:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 803e4d47-2370-30ef-b8a5-520a9c944581 | -2.45221 | -51.36957 | 2024-10-20 04:29:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| a0307234-aacb-3376-ac23-76fb3752da27 | -2.40725 | -50.43903 | 2024-10-20 04:29:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 6f052358-ac72-32e1-90d9-062d6de58db1 | -2.40354 | -50.43843 | 2024-10-20 04:29:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c389fefb-936f-3787-8159-6ef2257c2076 | -2.39436 | -51.80878 | 2024-10-20 04:29:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 4d0ab25b-c521-3ce8-9398-902eabb28ca8 | -2.2717 | -51.24638 | 2024-10-20 04:29:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 91f74a85-f98b-3fa8-bd0d-20e7a9d3cc15 | -2.2678 | -51.24577 | 2024-10-20 04:29:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |


[Clique aqui para ver as próximas entradas](README30.md)
