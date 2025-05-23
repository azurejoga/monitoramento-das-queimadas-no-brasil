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

## Dados Diários - Página 9

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 23c8f58a-f71e-3c43-848b-8e5927927da6 | -11.78717 | -44.28374 | 2025-05-23 04:04:00 | NPP-375D | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 8.3 |
| 889d8117-75c4-312a-b3c4-74cd80e042e0 | -8.75185 | -48.03962 | 2025-05-23 04:04:00 | NPP-375D | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| e312d41d-9464-30f2-ba80-ba8d7ffd94c6 | -14.05549 | -53.37374 | 2025-05-23 04:04:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| c7c793a8-f4ba-3886-9c6e-55b131432757 | -10.65224 | -49.48127 | 2025-05-23 04:04:00 | NPP-375D | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 3f371b77-399d-3a32-827c-95a846689d34 | -12.29691 | -52.49986 | 2025-05-23 04:04:00 | NPP-375D | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 7b82bb2e-6485-33ca-9256-94af7703b949 | -12.82266 | -47.38755 | 2025-05-23 04:04:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 8d817c7f-d74a-3602-a069-858cd7112f7b | -16.71231 | -43.22788 | 2025-05-23 04:04:00 | NPP-375D | ITACAMBIRA | MINAS GERAIS | Brasil | 3132008 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 56c44055-f747-3dd0-96f6-5b1f9429e7a5 | -14.03269 | -55.13703 | 2025-05-23 04:04:00 | NPP-375D | SANTA RITA DO TRIVELATO | MATO GROSSO | Brasil | 5107768 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| bc718c5b-8454-33e2-88af-f74b790f689e | -12.39229 | -49.97831 | 2025-05-23 04:04:00 | NPP-375D | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| b806c36d-54e3-3ea2-b153-861a98fc7681 | -12.33278 | -49.9857 | 2025-05-23 04:04:00 | NPP-375D | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| f911a024-8c31-3972-b2e3-2455061324e5 | -14.0494 | -53.37236 | 2025-05-23 04:04:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 522ff056-9e8c-3774-913e-371d6dcb9d8e | -12.07345 | -47.34362 | 2025-05-23 04:04:00 | NPP-375D | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 92575c0d-92e4-398f-ac46-4358e38e7eab | -12.3413 | -49.98552 | 2025-05-23 04:04:00 | NPP-375D | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 8ffd0206-6bb3-399f-b107-7c75b7243ea3 | -11.97328 | -44.15995 | 2025-05-23 04:04:00 | NPP-375D | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 358fea88-8442-3d73-b45a-58bc5916c430 | -12.29751 | -52.50418 | 2025-05-23 04:04:00 | NPP-375D | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| fc8899fc-3845-36fa-a229-53b30bc950dd | -15.74694 | -43.48706 | 2025-05-23 04:04:00 | NPP-375D | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 10fd95ae-1335-3450-b714-76ac6e7687c5 | -14.04842 | -53.37714 | 2025-05-23 04:04:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 6541b618-abe7-3751-b6da-dc00d36750d7 | -12.83724 | -47.39401 | 2025-05-23 04:04:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 13f5ab10-0e12-3475-bbb9-e4d09b130202 | -12.33675 | -49.98158 | 2025-05-23 04:04:00 | NPP-375D | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 78e7e638-d883-3893-8438-c9c038cdd534 | -14.13323 | -41.69112 | 2025-05-23 04:04:00 | NPP-375D | BRUMADO | BAHIA | Brasil | 2904605 | 29 | 33 | nan | nan | nan | Caatinga | 1.0 |
| a68e6b6e-8dd0-3697-9ec5-b49f2a24a78f | -13.98735 | -56.01199 | 2025-05-23 04:04:00 | NPP-375D | NOVA MUTUM | MATO GROSSO | Brasil | 5106224 | 51 | 33 | nan | nan | nan | Cerrado | 18.5 |
| 8d24f1f8-e0f5-3839-bad8-b7bd26bf45ad | -12.06558 | -47.33795 | 2025-05-23 04:04:00 | NPP-375D | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 80c73a21-ee3d-3340-bf3c-60847e4867f1 | -12.32427 | -49.99186 | 2025-05-23 04:04:00 | NPP-375D | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 7414bfab-0c46-3d75-b0ba-048526af1975 | -14.04134 | -53.38059 | 2025-05-23 04:04:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 1638aaef-1de9-38f8-bd73-fd8ce5b1a7ee | -11.55542 | -47.44658 | 2025-05-23 04:04:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| ba0e090d-ea5e-3b1c-b93e-1847921a62a5 | -14.04035 | -53.38542 | 2025-05-23 04:04:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| c64c63bb-2d0f-3bb5-9860-deea05a285c5 | -9.04099 | -47.74118 | 2025-05-23 04:04:00 | NPP-375D | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 5d89b571-105a-31d1-8eb0-151f9b64f3c8 | -14.87328 | -51.98442 | 2025-05-23 04:04:00 | NPP-375D | ARAGUAIANA | MATO GROSSO | Brasil | 5101001 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 5b722b07-2c8e-36e8-992c-b4d9e01dd2be | -13.99156 | -56.01319 | 2025-05-23 04:04:00 | NPP-375D | NOVA MUTUM | MATO GROSSO | Brasil | 5106224 | 51 | 33 | nan | nan | nan | Cerrado | 13.0 |
| 88fe3d75-3abf-3d48-9a1e-c7f33c35c6ba | -12.33562 | -49.98763 | 2025-05-23 04:04:00 | NPP-375D | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| db9b2842-0d87-359d-a6d3-e8144a94729d | -11.51531 | -48.55812 | 2025-05-23 04:04:00 | NPP-375D | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 8996fa1d-fb8b-3f91-848d-2bca4e9ee6fc | -12.82525 | -47.38748 | 2025-05-23 04:04:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| f5bd0e53-348d-3515-a166-09312c79de94 | -15.42491 | -41.40981 | 2025-05-23 04:04:00 | NPP-375D | CÂNDIDO SALES | BAHIA | Brasil | 2906709 | 29 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| ab4fdd0e-3aef-3b1d-b5b6-84830d1dac2a | -12.13487 | -54.66513 | 2025-05-23 04:04:00 | NPP-375D | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 11355381-1712-3414-b5ee-36cdd166876e | -13.18466 | -53.57275 | 2025-05-23 04:04:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| e187d0e9-5a71-3d99-a0b1-20914b4253c1 | -12.08339 | -47.34855 | 2025-05-23 04:04:00 | NPP-375D | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 6a6a8033-dabe-374f-af94-da1861760fd6 | -12.28586 | -52.49283 | 2025-05-23 04:04:00 | NPP-375D | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 7350e659-e3e1-3e5a-a245-00b12eb7b9c1 | -12.42329 | -49.98166 | 2025-05-23 04:04:00 | NPP-375D | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| d62c6a0b-83f5-3634-859f-54236e8911e1 | -12.34186 | -49.98251 | 2025-05-23 04:04:00 | NPP-375D | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| bb266dc6-c717-3cf9-b070-a9590bb4ba8a | -11.29773 | -53.98534 | 2025-05-23 04:04:00 | NPP-375D | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 7718d388-7a41-3eac-8c2e-496cf1386037 | -14.87206 | -51.98361 | 2025-05-23 04:04:00 | NPP-375D | ARAGUAIANA | MATO GROSSO | Brasil | 5101001 | 51 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 95804b6b-4bae-3474-a8c8-088a1af83a20 | -12.17556 | -40.34921 | 2025-05-23 04:04:00 | NPP-375D | MACAJUBA | BAHIA | Brasil | 2919603 | 29 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 84e8aa03-fae3-3e86-a853-f35e77227c9b | -11.78357 | -44.28312 | 2025-05-23 04:04:00 | NPP-375D | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 12.3 |
| d86bea06-a81f-3491-b3f1-d6d68c9772c7 | -12.82599 | -47.38346 | 2025-05-23 04:04:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| d8c35c22-08dc-3da0-95e0-81f8a5e7588c | -7.9705 | -49.69577 | 2025-05-23 04:04:00 | NPP-375D | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 5842367b-aff4-3971-9353-bce47dd60bf4 | -9.02154 | -47.74267 | 2025-05-23 04:04:00 | NPP-375D | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| e27f3ab0-6942-3da3-927b-b513be30c754 | -14.70491 | -48.66795 | 2025-05-23 04:04:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| c74047d4-a2eb-36a0-b9ca-d28654f49b7a | -12.33099 | -49.99489 | 2025-05-23 04:04:00 | NPP-375D | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 07a95479-9e0f-35f1-9c49-e1a770ac910b | -10.79104 | -48.83934 | 2025-05-23 04:04:00 | NPP-375D | FÁTIMA | TOCANTINS | Brasil | 1707553 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 30d8f70f-0100-30b7-ac42-e88a63f91d4c | -13.98035 | -56.01 | 2025-05-23 04:04:00 | NPP-375D | NOVA MUTUM | MATO GROSSO | Brasil | 5106224 | 51 | 33 | nan | nan | nan | Cerrado | 9.9 |
| 220fdd8d-752f-326d-a052-90c3d634b00f | -11.30389 | -54.02321 | 2025-05-23 04:04:00 | NPP-375D | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 0e8c658c-283a-3be2-8a3d-f3e359b4cbc0 | -9.56343 | -48.22602 | 2025-05-23 04:04:00 | NPP-375D | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 5bcdb9b7-0cbd-3041-a954-7b0efc84b2a4 | -12.29183 | -52.49408 | 2025-05-23 04:04:00 | NPP-375D | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 4.0 |
| ba290ac1-a3ff-3a4c-b796-b960150baf99 | -11.78788 | -44.27956 | 2025-05-23 04:04:00 | NPP-375D | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 8.3 |
| d3c07691-5f7b-3e68-b504-b09b2140bf7f | -12.71739 | -54.97767 | 2025-05-23 04:04:00 | NPP-375D | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| c317b62d-eefb-3432-be7e-257862cca63d | -11.28493 | -41.86229 | 2025-05-23 04:04:00 | NPP-375D | IRECÊ | BAHIA | Brasil | 2914604 | 29 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 0fa5bb27-0bad-3db3-bbb9-65329ed2e37a | -12.07126 | -47.34209 | 2025-05-23 04:04:00 | NPP-375D | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 4.5 |
| e62c8d1e-1362-3c47-b892-5c70dbf0cc9e | -12.34358 | -49.9845 | 2025-05-23 04:04:00 | NPP-375D | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 27c76893-0c75-3ec4-952c-6988df782c8a | -11.57123 | -54.5631 | 2025-05-23 04:04:00 | NPP-375D | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| b7abb8ee-6342-3f7a-9667-ef2aad813810 | -8.72314 | -50.2549 | 2025-05-23 04:04:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 254c27a4-eeb0-3ec8-b4f2-6ee5d85fd4c3 | -12.29602 | -52.50438 | 2025-05-23 04:04:00 | NPP-375D | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 5ffcb547-6bdd-33d6-bf02-3f84d9ce96c1 | -12.13561 | -54.65818 | 2025-05-23 04:04:00 | NPP-375D | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| b593fd88-4623-3950-a4c0-b80f1228d109 | -11.97398 | -44.15582 | 2025-05-23 04:04:00 | NPP-375D | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 70a8fbe5-2f36-35c7-a58b-741b99232c8e | -13.98457 | -56.01111 | 2025-05-23 04:04:00 | NPP-375D | NOVA MUTUM | MATO GROSSO | Brasil | 5106224 | 51 | 33 | nan | nan | nan | Cerrado | 13.0 |
| 3e685665-40a7-3146-a597-664413aca8ed | -15.42547 | -41.40619 | 2025-05-23 04:04:00 | NPP-375D | CÂNDIDO SALES | BAHIA | Brasil | 2906709 | 29 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| cb7f81ff-8d59-3b7e-bc05-b9d386d0915c | -12.41764 | -49.9837 | 2025-05-23 04:04:00 | NPP-375D | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| cae0378a-ffb9-3787-bb78-7fce3be011c7 | -12.2874 | -52.49268 | 2025-05-23 04:04:00 | NPP-375D | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 3f106188-6bcc-36ff-a05c-b3e50042e66c | -12.84149 | -47.39483 | 2025-05-23 04:04:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 9d3a2afb-0906-39a8-adf3-f3ebb27a308f | -12.31802 | -49.997 | 2025-05-23 04:04:00 | NPP-375D | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| e14faeab-9985-3a53-82dd-f340a6c9a69f | -14.05354 | -53.38331 | 2025-05-23 04:04:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 90e0d0c9-117c-3704-bbad-69ecf2591ff2 | -15.42157 | -41.40926 | 2025-05-23 04:04:00 | NPP-375D | CÂNDIDO SALES | BAHIA | Brasil | 2906709 | 29 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| fd616cbe-4958-3ff2-a3c8-2e05fb9e8f7d | -12.4098 | -42.52713 | 2025-05-23 04:04:00 | NPP-375D | OLIVEIRA DOS BREJINHOS | BAHIA | Brasil | 2923209 | 29 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 5e10fbcb-fddf-3882-adb7-fc5586c55f10 | -11.79148 | -44.28017 | 2025-05-23 04:04:00 | NPP-375D | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 8.3 |
| 81c4f16e-3b8c-36e2-bdbb-72c0cfc1faa6 | -12.32369 | -49.99493 | 2025-05-23 04:04:00 | NPP-375D | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 89680ab6-c9c8-3a07-b97d-d920e3022cd9 | -12.29246 | -52.49841 | 2025-05-23 04:04:00 | NPP-375D | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 8cc58a23-ffd0-3d05-8a0d-652281702d3b | -9.04014 | -47.74598 | 2025-05-23 04:04:00 | NPP-375D | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| c0cafa3e-ffc1-3597-8acd-0cab47a585a1 | -9.02913 | -47.75397 | 2025-05-23 04:04:00 | NPP-375D | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| d7e4be9b-58d7-30da-b643-71bef45e752b | -15.42213 | -41.40564 | 2025-05-23 04:04:00 | NPP-375D | CÂNDIDO SALES | BAHIA | Brasil | 2906709 | 29 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| 5aa96767-a0f6-301e-9ee8-5fdcdc8e5069 | -11.5575 | -47.46009 | 2025-05-23 04:04:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 1b012095-d323-3897-be6e-85488b539020 | -11.56415 | -47.44818 | 2025-05-23 04:04:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 06acb3e7-b248-3946-9694-eacfbb584c0f | -13.78108 | -54.31199 | 2025-05-23 04:04:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 80c3e6ac-f3f8-39c8-87c3-e5e32824e48c | -11.30149 | -39.17674 | 2025-05-23 04:04:00 | NPP-375D | CONCEIÇÃO DO COITÉ | BAHIA | Brasil | 2908408 | 29 | 33 | nan | nan | nan | Caatinga | 1.0 |
| eecd42fa-146b-3991-97e2-979bc7b81880 | -12.34073 | -49.98856 | 2025-05-23 04:04:00 | NPP-375D | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| fbc227c1-8146-3b35-9ef7-1ddfeb21caf7 | -14.0466 | -53.38046 | 2025-05-23 04:04:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 43bbb45f-ff7b-3419-8e4d-5b842ff27a6a | -9.47243 | -40.49401 | 2025-05-23 04:04:00 | NPP-375D | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 0.3 |
| 21422584-e640-3913-b6f7-7e95a1db41d7 | -13.98297 | -56.01839 | 2025-05-23 04:04:00 | NPP-375D | NOVA MUTUM | MATO GROSSO | Brasil | 5106224 | 51 | 33 | nan | nan | nan | Cerrado | 13.0 |
| 7ca72e71-4913-305a-85b8-e0f75c9e0a6a | -12.4188 | -49.97756 | 2025-05-23 04:04:00 | NPP-375D | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 32d2f996-058a-37e7-830f-e93f097b0be0 | -15.0285 | -43.84048 | 2025-05-23 04:04:00 | NPP-375D | MATIAS CARDOSO | MINAS GERAIS | Brasil | 3140852 | 31 | 33 | nan | nan | nan | Caatinga | 0.7 |
| e95fadcf-719e-31b4-a950-3458ef4cdf8e | -12.72466 | -54.9763 | 2025-05-23 04:04:00 | NPP-375D | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a44118c8-8f6c-3db9-9811-417a303e2772 | -12.06915 | -47.34285 | 2025-05-23 04:04:00 | NPP-375D | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 9863c54c-1be7-3706-a454-0a1cde88459c | -12.33109 | -49.98367 | 2025-05-23 04:04:00 | NPP-375D | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 7e2b6aea-ac6b-38a0-8b91-34055060de92 | -14.05471 | -53.37227 | 2025-05-23 04:04:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| a5b0e609-30fa-3124-9b2c-70fadd388559 | -10.66404 | -49.4743 | 2025-05-23 04:04:00 | NPP-375D | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 23d94496-c227-3270-87ed-dacb1e4c522f | -12.06842 | -47.34698 | 2025-05-23 04:04:00 | NPP-375D | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 1206db19-6f07-35b0-87be-5361f4589487 | -15.42435 | -41.41343 | 2025-05-23 04:04:00 | NPP-375D | CÂNDIDO SALES | BAHIA | Brasil | 2906709 | 29 | 33 | nan | nan | nan | Mata Atlântica | 2.7 |
| 1f77aeb5-3387-37b6-9dd7-0f4e59f352b2 | -9.02448 | -47.75313 | 2025-05-23 04:04:00 | NPP-375D | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 15bd5595-da45-33dc-bc7c-a4aef1c4a50d | -14.071 | -53.38582 | 2025-05-23 04:04:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 653bb09e-4e86-3067-ae38-8ccf3c87c7c4 | -12.82337 | -47.38352 | 2025-05-23 04:04:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 0db0f1c2-f3ae-35d6-9305-7e03f2dbe723 | -14.86776 | -51.9832 | 2025-05-23 04:04:00 | NPP-375D | ARAGUAIANA | MATO GROSSO | Brasil | 5101001 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 0422949d-df65-3750-a0ff-ba32138c0d2a | -12.29934 | -52.49519 | 2025-05-23 04:04:00 | NPP-375D | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 4.1 |


[Clique aqui para ver as próximas entradas](README10.md)
