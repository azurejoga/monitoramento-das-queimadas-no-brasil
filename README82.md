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

## Dados Diários - Página 82

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| ba4e846b-7e5d-3a8c-bfda-9a452cd00126 | -2.86596 | -52.90683 | 2024-10-07 04:51:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 40c3afdb-7b18-3cfd-a4fb-7d5165196fa5 | -2.8654 | -52.91034 | 2024-10-07 04:51:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 713f1f66-aafa-3ec1-8990-e38fa7670885 | -2.86485 | -52.91385 | 2024-10-07 04:51:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| f122ef1e-ec5f-39c1-a587-b35b6ec5abd3 | -2.86373 | -52.89931 | 2024-10-07 04:51:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 0789a440-678e-3761-ab69-daa7167e5842 | -2.86317 | -52.90282 | 2024-10-07 04:51:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 0cd6e903-e5b7-3ba3-86ca-589e1537b66b | -2.86262 | -52.90633 | 2024-10-07 04:51:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 6.0 |
| e66bbb22-dfcb-359d-b16d-d4cfedc3a92e | -2.86207 | -52.90984 | 2024-10-07 04:51:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 6.0 |
| dfc8b978-0619-3266-8b35-c3a9efe2d876 | -2.8604 | -52.8988 | 2024-10-07 04:51:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 031cb34d-a73f-389a-8607-3ef5422f09a9 | -2.85984 | -52.90231 | 2024-10-07 04:51:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 9b3717bc-f07f-306f-9f3b-dfd5f317af02 | -2.85928 | -52.90582 | 2024-10-07 04:51:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| de47ac5b-bc1a-3f5e-adc6-8346bfb6aea5 | -2.77692 | -53.20837 | 2024-10-07 04:51:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 5fe893ce-6d15-38ba-bc45-cedc744696ab | -2.77635 | -53.21194 | 2024-10-07 04:51:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| bd55d9f7-3f1a-3207-9837-f0b16997d9c2 | -2.77299 | -53.21142 | 2024-10-07 04:51:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 8a2fbc67-e76f-3854-8147-d46203178d00 | -2.77241 | -53.21502 | 2024-10-07 04:51:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 83ec24e8-a3d6-327b-8cd1-e925155b5a65 | -2.7709 | -53.21109 | 2024-10-07 04:51:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b6e5c358-0547-3335-bae1-bee2b58584b6 | -2.77034 | -53.21469 | 2024-10-07 04:51:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 69147af1-6e7e-333d-a4d2-efc763922f54 | -3.65516 | -53.59991 | 2024-10-07 04:51:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| be2dcd23-5bbd-3de9-8732-25bd21ebaf5d | -5.92661 | -53.41998 | 2024-10-07 04:51:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| d8b62a9a-5db6-3280-9c3c-b74c18ea1911 | -5.92329 | -53.41946 | 2024-10-07 04:51:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| db9cd15e-caf7-33b9-9868-9bd2a46cccc1 | -2.22788 | -53.697 | 2024-10-07 04:51:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| f314224a-283e-32d9-8fec-0fd541abbc46 | -2.22386 | -53.7002 | 2024-10-07 04:51:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 6d84781e-8bf6-3004-a633-18f7fda6f006 | -2.22161 | -53.69224 | 2024-10-07 04:51:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| f9ef7f33-80b6-33ba-9640-c05b01286e04 | -2.22102 | -53.69596 | 2024-10-07 04:51:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 62ffd362-7a37-370e-a81b-86b6dc97793e | -2.22044 | -53.69968 | 2024-10-07 04:51:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| a430d317-11d0-364a-aca1-9145f401e620 | -2.21985 | -53.70339 | 2024-10-07 04:51:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 4cc66fa2-def2-3a7f-bf03-afa235a316de | -2.21936 | -53.68427 | 2024-10-07 04:51:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| cb02a2be-3664-35df-a655-4101bae1b7e4 | -2.21926 | -53.70711 | 2024-10-07 04:51:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 951c11f8-1618-3fe3-9b3a-b937153ff64c | -2.21877 | -53.688 | 2024-10-07 04:51:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| d7e9a828-6e53-3701-b59c-8d2abe9b7787 | -2.21818 | -53.69172 | 2024-10-07 04:51:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| c7e2bbc7-699b-39ed-8a84-c8b06b1a58a4 | -2.21759 | -53.69545 | 2024-10-07 04:51:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 1bfe6437-445f-3140-805c-0a14f676125a | -2.21701 | -53.69917 | 2024-10-07 04:51:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 0f491a65-5dfb-36bb-be59-1d7f74439abd | -2.21642 | -53.70288 | 2024-10-07 04:51:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 698ae0b1-108d-3a48-81f6-f956ac5ec3b6 | -2.21593 | -53.68374 | 2024-10-07 04:51:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| d5ae9c08-2773-3208-94f2-9f6d4e51e1ab | -2.21583 | -53.70659 | 2024-10-07 04:51:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 8f41c358-1228-3db9-9277-42e4e18e1544 | -2.21534 | -53.68747 | 2024-10-07 04:51:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| e84c5f97-32b0-34e1-a3b3-62646068ffa4 | -2.21525 | -53.7103 | 2024-10-07 04:51:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| a7d3cbb3-f850-3e13-9b38-65535c6f5a7f | -2.81356 | -54.35928 | 2024-10-07 04:51:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 1bfc750e-b591-37b0-a979-57a5d99f7b55 | -2.30127 | -53.52353 | 2024-10-07 04:51:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| d07f9dac-fd5f-3be0-82ca-c36b50ba3478 | -2.30069 | -53.52718 | 2024-10-07 04:51:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 41611e54-29b6-37a2-bd98-dea61ca051b9 | -7.98428 | -54.76699 | 2024-10-07 04:51:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| f88111fe-9dc8-3d87-a3e3-ae1f05314ec3 | -7.98208 | -54.75908 | 2024-10-07 04:51:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e7d3719e-42cf-3d40-9b51-ff83caff23d7 | -7.98148 | -54.76276 | 2024-10-07 04:51:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 14613a4c-400d-3eb4-b265-5d55ffde4c8f | -7.98088 | -54.76645 | 2024-10-07 04:51:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| c2b09993-9452-3910-9818-3150757251a1 | -7.97809 | -54.76221 | 2024-10-07 04:51:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| bb5bff61-0e33-3a7d-a638-11a1d9b774b0 | -7.87063 | -54.88202 | 2024-10-07 04:51:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 48e335b9-edf6-3aea-a538-fe287462f1e2 | -7.86881 | -54.8932 | 2024-10-07 04:51:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d4abd092-dae3-32fe-9617-cb7560fcc38e | -7.866 | -54.8889 | 2024-10-07 04:51:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 324aac26-c23c-3c3e-a4af-88e8c02ac3b3 | -7.8654 | -54.89263 | 2024-10-07 04:51:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| f69e24ba-2214-3828-ad78-825d4826ecd6 | -7.86479 | -54.89637 | 2024-10-07 04:51:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| b0f837f5-7200-3097-b293-c10a94db6931 | -7.86198 | -54.89208 | 2024-10-07 04:51:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| f9541558-902a-3321-99e6-3bbf5077bf07 | -7.86137 | -54.89582 | 2024-10-07 04:51:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 90ea5262-052a-3bae-beb8-95ab36566ea0 | -7.86076 | -54.89956 | 2024-10-07 04:51:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| d2b0bc5a-017a-312d-b8d8-eb0637bfeeda | -17.84258 | -42.22318 | 2024-10-07 04:53:00 | AQUA_M-M | MALACACHETA | MINAS GERAIS | Brasil | 3139201 | 31 | 33 | nan | nan | nan | Mata Atlântica | 9.8 |
| 6db11582-e9bc-3fcd-85ff-9faed0601545 | -19.29368 | -42.57335 | 2024-10-07 04:53:00 | AQUA_M-M | MESQUITA | MINAS GERAIS | Brasil | 3141702 | 31 | 33 | nan | nan | nan | Mata Atlântica | 8.8 |
| c60cbd28-3216-376b-a879-524d8064c38e | -19.14198 | -42.72571 | 2024-10-07 04:53:00 | AQUA_M-M | BRAÚNAS | MINAS GERAIS | Brasil | 3108800 | 31 | 33 | nan | nan | nan | Mata Atlântica | 34.5 |
| 642909a3-5cc3-338f-a7f6-ab42c1f113bb | -19.14052 | -42.73521 | 2024-10-07 04:53:00 | AQUA_M-M | BRAÚNAS | MINAS GERAIS | Brasil | 3108800 | 31 | 33 | nan | nan | nan | Mata Atlântica | 28.4 |
| 12caa18b-95db-34fe-a8e2-d294216826e1 | -18.53783 | -42.08415 | 2024-10-07 04:53:00 | AQUA_M-M | MARILAC | MINAS GERAIS | Brasil | 3140100 | 31 | 33 | nan | nan | nan | Mata Atlântica | 7.7 |
| 49dee26c-4f02-3403-ac61-0f3a47e72873 | -14.11962 | -45.52841 | 2024-10-07 04:53:00 | AQUA_M-M | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 54.9 |
| b85574e2-1cfd-3ab3-8191-5324dd80f092 | -19.57304 | -42.74248 | 2024-10-07 04:53:00 | AQUA_M-M | ANTÔNIO DIAS | MINAS GERAIS | Brasil | 3103009 | 31 | 33 | nan | nan | nan | Mata Atlântica | 53.1 |
| 4c6375b8-3d71-3bc8-b413-8e2aed5a6142 | -19.57156 | -42.75203 | 2024-10-07 04:53:00 | AQUA_M-M | ANTÔNIO DIAS | MINAS GERAIS | Brasil | 3103009 | 31 | 33 | nan | nan | nan | Mata Atlântica | 12.4 |
| 2895f4ba-84dd-3326-9bcc-628f72d55884 | -19.56414 | -42.74086 | 2024-10-07 04:53:00 | AQUA_M-M | ANTÔNIO DIAS | MINAS GERAIS | Brasil | 3103009 | 31 | 33 | nan | nan | nan | Mata Atlântica | 8.6 |
| 3cd26f69-5f61-30ec-a63f-b5e9cdb71052 | -19.56269 | -42.75026 | 2024-10-07 04:53:00 | AQUA_M-M | ANTÔNIO DIAS | MINAS GERAIS | Brasil | 3103009 | 31 | 33 | nan | nan | nan | Mata Atlântica | 5.6 |
| aa4c1a65-7525-3a08-94ef-2a50372afe62 | -17.54924 | -43.75251 | 2024-10-07 04:53:00 | AQUA_M-M | OLHOS-D'ÁGUA | MINAS GERAIS | Brasil | 3145455 | 31 | 33 | nan | nan | nan | Cerrado | 7.9 |
| a31c27d8-1a24-302c-8132-ff74053d4d8d | -17.53986 | -43.75093 | 2024-10-07 04:53:00 | AQUA_M-M | OLHOS-D'ÁGUA | MINAS GERAIS | Brasil | 3145455 | 31 | 33 | nan | nan | nan | Cerrado | 9.5 |
| 24f6b27a-91c8-3b20-a768-6eebc6194c71 | -13.85461 | -44.63032 | 2024-10-07 04:53:00 | AQUA_M-M | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 14.8 |
| 21137315-5548-3bc7-91e1-fb2cddb49ace | -13.84415 | -44.62853 | 2024-10-07 04:53:00 | AQUA_M-M | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 12.9 |
| f5b43a98-8b73-30f4-a7be-cbf78c9a292e | -14.13199 | -45.52248 | 2024-10-07 04:53:00 | AQUA_M-M | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 20.1 |
| 69ad3d15-df19-3d56-a30f-4ed8beefd21f | -14.21552 | -46.45715 | 2024-10-07 04:53:00 | AQUA_M-M | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 10.7 |
| 09146eea-fb81-34de-acb3-854fb403a6a8 | -14.12947 | -45.53715 | 2024-10-07 04:53:00 | AQUA_M-M | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 41.9 |
| ff25eae6-8f8a-3071-a96d-3f980a5c08f2 | -14.12204 | -45.51379 | 2024-10-07 04:53:00 | AQUA_M-M | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 62.1 |
| 8e4b1db1-5334-36bb-9ed9-b982a0ac8800 | -14.12182 | -45.58149 | 2024-10-07 04:53:00 | AQUA_M-M | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 14.6 |
| d10548e4-f39d-33d7-a3a5-c7b9988c8d5f | -14.12089 | -45.52047 | 2024-10-07 04:53:00 | AQUA_M-M | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 93.3 |
| 4c90bd4f-6486-3b49-994d-f0db62405e15 | -14.11838 | -45.53499 | 2024-10-07 04:53:00 | AQUA_M-M | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 14.2 |
| 8133954c-2b8a-3dcd-b792-fc9dbedc28cd | -14.08509 | -45.46164 | 2024-10-07 04:53:00 | AQUA_M-M | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 14.1 |
| 9d65f5eb-42e4-3201-af48-d806f9f95754 | -17.61959 | -46.93557 | 2024-10-07 04:53:00 | AQUA_M-M | GUARDA-MOR | MINAS GERAIS | Brasil | 3128600 | 31 | 33 | nan | nan | nan | Cerrado | 17.6 |
| 151d8fa3-d80b-3fc6-84ba-0efe76744105 | -17.61676 | -46.95158 | 2024-10-07 04:53:00 | AQUA_M-M | GUARDA-MOR | MINAS GERAIS | Brasil | 3128600 | 31 | 33 | nan | nan | nan | Cerrado | 26.6 |
| 061496da-8c3a-32d9-a3de-f06cca8809e5 | -16.89752 | -47.15317 | 2024-10-07 04:53:00 | AQUA_M-M | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 11.8 |
| 3d723a81-a23e-3665-9d00-65ea9054899c | -18.31229 | -47.1356 | 2024-10-07 04:53:00 | AQUA_M-M | COROMANDEL | MINAS GERAIS | Brasil | 3119302 | 31 | 33 | nan | nan | nan | Cerrado | 19.9 |
| 7a8cc409-187c-3c43-9b38-1fd2b59a8d2c | -18.30945 | -47.15143 | 2024-10-07 04:53:00 | AQUA_M-M | COROMANDEL | MINAS GERAIS | Brasil | 3119302 | 31 | 33 | nan | nan | nan | Cerrado | 16.9 |
| d4517e98-8863-310f-ba75-8c7de736444d | -16.14021 | -48.89322 | 2024-10-07 04:53:00 | AQUA_M-M | ABADIÂNIA | GOIÁS | Brasil | 5200100 | 52 | 33 | nan | nan | nan | Cerrado | 44.3 |
| e395eab9-f3e4-326e-9aa9-b68d69b0fa92 | -17.15461 | -51.70475 | 2024-10-07 04:53:00 | AQUA_M-M | CAIAPÔNIA | GOIÁS | Brasil | 5204409 | 52 | 33 | nan | nan | nan | Cerrado | 42.4 |
| 51de8056-397b-352b-92d8-07ff26852222 | -17.14364 | -51.7074 | 2024-10-07 04:53:00 | AQUA_M-M | CAIAPÔNIA | GOIÁS | Brasil | 5204409 | 52 | 33 | nan | nan | nan | Cerrado | 87.9 |
| d98e7d02-87b4-3559-8e96-8d84dfe26a92 | -17.13803 | -51.70104 | 2024-10-07 04:53:00 | AQUA_M-M | CAIAPÔNIA | GOIÁS | Brasil | 5204409 | 52 | 33 | nan | nan | nan | Cerrado | 55.0 |
| 256c9e27-dbbd-38e0-9e95-6976bfa21f8e | -13.8417 | -44.63156 | 2024-10-07 04:53:00 | NOAA-21 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 7.4 |
| 2f399db1-0fd9-318d-bf7e-0ad0f2d5d143 | -9.58884 | -66.7532 | 2024-10-07 04:53:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 1ac66664-3b6f-3ef0-8088-c0a89ac4b7ad | -9.58878 | -66.75713 | 2024-10-07 04:53:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 14891153-6e76-3b26-a57a-1d6c19fa7d1f | -9.58755 | -66.75973 | 2024-10-07 04:53:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 3.0 |
| ebf8880d-00ce-35df-9367-189ed7f1916b | -9.49585 | -67.11079 | 2024-10-07 04:53:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 08f51c38-465d-3329-9b54-116f3d49323e | -12.72064 | -40.21746 | 2024-10-07 04:53:00 | NOAA-21 | ITABERABA | BAHIA | Brasil | 2914703 | 29 | 33 | nan | nan | nan | Caatinga | 2.9 |
| 3baa6431-1729-37d8-82aa-3dd787101f36 | -12.71993 | -40.22456 | 2024-10-07 04:53:00 | NOAA-21 | ITABERABA | BAHIA | Brasil | 2914703 | 29 | 33 | nan | nan | nan | Caatinga | 3.6 |
| 74b25e08-f92e-3093-9e11-a2d477a8aa4e | -12.71638 | -40.21585 | 2024-10-07 04:53:00 | NOAA-21 | ITABERABA | BAHIA | Brasil | 2914703 | 29 | 33 | nan | nan | nan | Caatinga | 4.3 |
| 13b8e72a-532d-3f50-8262-508bcd2d64f1 | -12.71562 | -40.22293 | 2024-10-07 04:53:00 | NOAA-21 | ITABERABA | BAHIA | Brasil | 2914703 | 29 | 33 | nan | nan | nan | Caatinga | 4.3 |
| f4002f69-e3f5-3e11-ad81-90af97c43c04 | -12.71359 | -40.2164 | 2024-10-07 04:53:00 | NOAA-21 | ITABERABA | BAHIA | Brasil | 2914703 | 29 | 33 | nan | nan | nan | Caatinga | 2.9 |
| d5d27178-8689-3522-bb32-275976a7db74 | -12.71288 | -40.2235 | 2024-10-07 04:53:00 | NOAA-21 | ITABERABA | BAHIA | Brasil | 2914703 | 29 | 33 | nan | nan | nan | Caatinga | 3.6 |
| aa73975e-e549-3411-a895-3dcbd16b1ffa | -16.35048 | -43.69581 | 2024-10-07 04:53:00 | NOAA-21 | CAPITÃO ENÉAS | MINAS GERAIS | Brasil | 3112703 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 12895890-432c-3063-874e-90c6cf0ec6d2 | -11.75316 | -44.49962 | 2024-10-07 04:53:00 | NOAA-21 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 25.3 |
| 0309238a-63b0-3bdf-8c08-a9b6e4df9b05 | -11.75274 | -44.50306 | 2024-10-07 04:53:00 | NOAA-21 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 31.0 |
| cfa8c001-0866-33ee-b2d8-1a0fcae748fa | -11.74655 | -44.50919 | 2024-10-07 04:53:00 | NOAA-21 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 82e2b5d0-b247-3c45-9b72-b41dd614e868 | -14.69177 | -45.14361 | 2024-10-07 04:53:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 551ba6a6-df82-3c68-87aa-e9df535c528b | -14.68722 | -45.13612 | 2024-10-07 04:53:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |


[Clique aqui para ver as próximas entradas](README83.md)
