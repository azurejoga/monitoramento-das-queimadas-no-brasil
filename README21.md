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

## Dados Diários - Página 21

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 4d3efbd4-28ef-38a9-86e7-3e593717618e | -5.38169 | -42.88554 | 2024-12-04 03:49:00 | NPP-375D | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 2e179c2f-e102-3cb6-a116-bc5d766916de | -4.05755 | -46.602 | 2024-12-04 03:49:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 63a87959-3b7e-3b99-adef-6294356cf99f | -13.24191 | -39.98025 | 2024-12-04 03:49:00 | NPP-375D | IRAJUBA | BAHIA | Brasil | 2914208 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 09a2dd16-3596-312c-8881-b1db66d71428 | -13.80923 | -41.5752 | 2024-12-04 03:49:00 | NPP-375D | RIO DE CONTAS | BAHIA | Brasil | 2926707 | 29 | 33 | nan | nan | nan | Caatinga | 2.7 |
| 57c6e8e2-3733-31ac-9a0b-75115e161f4a | -3.68742 | -42.04323 | 2024-12-04 03:49:00 | NPP-375D | BATALHA | PIAUÍ | Brasil | 2201507 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| b7ddecca-6c43-340a-a85f-dd3d3480ba19 | -15.6419 | -39.18911 | 2024-12-04 03:49:00 | NPP-375D | CANAVIEIRAS | BAHIA | Brasil | 2906303 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| de328a70-19c5-3aed-b4ec-1a88393dd5da | -3.17895 | -44.43441 | 2024-12-04 03:49:00 | NPP-375D | ANAJATUBA | MARANHÃO | Brasil | 2100709 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 85bc4c28-9b8b-362b-82a8-43e7b326412f | -5.22857 | -35.63462 | 2024-12-04 03:49:00 | NPP-375D | TOUROS | RIO GRANDE DO NORTE | Brasil | 2414407 | 24 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 9ad65099-7de5-328a-a00e-0c50d6f21b62 | -5.37883 | -42.88238 | 2024-12-04 03:49:00 | NPP-375D | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 830f1053-fbf7-3bb0-90d6-f80e9f5b4fca | -3.67991 | -50.26353 | 2024-12-04 03:49:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| c0635e0d-a52c-359e-9f20-e59b222b2133 | -2.83222 | -46.75751 | 2024-12-04 03:49:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 8.0 |
| 4e13be48-8581-3c1a-ad6f-e7b47ca706e0 | -2.8012 | -53.0633 | 2024-12-04 03:50:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 61.3 |
| 16a7aab5-d169-3f6d-ba2a-f9c4027f6276 | -3.1454 | -54.6059 | 2024-12-04 03:50:00 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 56.5 |
| 35d70172-3a56-3844-935c-3b30119dcb8b | -6.0672 | -48.0786 | 2024-12-04 03:50:00 | GOES-16 | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | 61.4 |
| f41f1e44-92ce-39c8-b12a-61b04e929bc2 | -3.1086 | -54.6068 | 2024-12-04 03:50:00 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 70.1 |
| 723ee0ba-4ce9-37a4-b0ff-f9193f7d48f3 | -1.7545 | -52.6159 | 2024-12-04 03:50:00 | GOES-16 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 189.1 |
| 0eaf4785-d34d-318f-b521-d44399e9bf50 | -3.1453 | -54.6259 | 2024-12-04 03:50:00 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 55.3 |
| 54801019-8204-387e-8e7c-01649bdfd70d | -1.6446 | -52.393 | 2024-12-04 03:50:00 | GOES-16 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 63.7 |
| 00e9ce13-c187-3f42-8ed7-7c00bb52311c | -3.259 | -53.659 | 2024-12-04 03:50:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 67.1 |
| 80e28af3-34d1-3193-99de-703e2a170723 | -1.7361 | -52.6366 | 2024-12-04 03:50:00 | GOES-16 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 50.2 |
| 3e4c9b75-5f08-39de-b35c-ee186dbf6f4a | -2.6428 | -45.7394 | 2024-12-04 03:50:00 | GOES-16 | NOVA OLINDA DO MARANHÃO | MARANHÃO | Brasil | 2107357 | 21 | 33 | nan | nan | nan | Amazônia | 46.1 |
| 66980868-546a-304e-9c80-4e12c1a12438 | -3.127 | -54.6063 | 2024-12-04 03:50:00 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 126.8 |
| 604fe254-5d17-3dd3-88d5-bb76eae43e29 | -3.2591 | -53.6186 | 2024-12-04 03:50:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 57.9 |
| 6d4e2f76-3fe6-3942-90d3-220e3495d912 | -3.259 | -53.6388 | 2024-12-04 03:50:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 60.1 |
| 3c491435-a7b6-3cec-806c-0464f142b02e | -3.1086 | -54.6268 | 2024-12-04 03:50:00 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 72.8 |
| 10b1d515-821c-316f-a4ec-0dacd16dc81e | -6.0858 | -48.0774 | 2024-12-04 03:50:00 | GOES-16 | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | 107.9 |
| c3651951-a319-3e64-9548-52cad9260556 | -3.1269 | -54.6263 | 2024-12-04 03:50:00 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 138.2 |
| 0f97b6af-55b9-3136-8264-169f4a16536a | -1.6631 | -52.3723 | 2024-12-04 03:50:00 | GOES-16 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 46.3 |
| 2c60edf6-bad3-3e6e-bc85-bc9ea4d21175 | -1.7544 | -52.6363 | 2024-12-04 03:50:00 | GOES-16 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 137.5 |
| e482d660-b631-3703-a597-ef58a003476b | -1.663 | -52.3927 | 2024-12-04 03:50:00 | GOES-16 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 57.2 |
| 217b978b-91c0-3389-8aba-100dde9f0dda | -1.6447 | -52.3725 | 2024-12-04 03:50:00 | GOES-16 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 61.0 |
| f68c00fc-d73f-332f-b5f4-3fb701594f14 | -1.7729 | -52.6156 | 2024-12-04 03:50:00 | GOES-16 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 74.1 |
| a13ed1a4-8fa3-38fb-b7fe-8a78eecaf66f | -1.7361 | -52.6162 | 2024-12-04 03:50:00 | GOES-16 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 92.7 |
| 5fbf81c1-a541-3c3b-9324-ecd928fcf6d9 | -2.8197 | -53.0425 | 2024-12-04 03:50:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 65.2 |
| 84bbc1dc-7f2e-33c7-82d5-4a310f545fa6 | -1.7728 | -52.636 | 2024-12-04 03:50:00 | GOES-16 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 66.9 |
| 584cd658-5d7f-301f-bf03-ffbaf35a25bf | -2.8196 | -53.0629 | 2024-12-04 03:50:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 85.2 |
| 3930b693-1136-33f1-8ca8-5a50cf5b7698 | -6.086 | -48.0557 | 2024-12-04 03:50:00 | GOES-16 | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | 106.5 |
| 0de004ef-96e7-38db-ac8e-6c2c6493d4ab | -18.73098 | -39.89558 | 2024-12-04 03:51:00 | NPP-375D | SÃO MATEUS | ESPÍRITO SANTO | Brasil | 3204906 | 32 | 33 | nan | nan | nan | Mata Atlântica | 0.4 |
| 7080f202-2f17-3264-a27f-3f245c3196fc | -1.7545 | -52.6159 | 2024-12-04 04:00:00 | GOES-16 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 152.4 |
| 65e1dee5-54d9-3552-9554-51dfcd828980 | -6.086 | -48.0557 | 2024-12-04 04:00:00 | GOES-16 | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | 71.5 |
| 0563d4da-4c61-34a5-9928-772474fc6bf3 | -3.2591 | -53.6186 | 2024-12-04 04:00:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 57.4 |
| b1e11395-e7da-3f36-bc25-b6713f305d5a | -3.259 | -53.6388 | 2024-12-04 04:00:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 67.1 |
| 312af453-78cd-3665-9673-2ecca4b20a5e | -2.6428 | -45.7394 | 2024-12-04 04:00:00 | GOES-16 | NOVA OLINDA DO MARANHÃO | MARANHÃO | Brasil | 2107357 | 21 | 33 | nan | nan | nan | Amazônia | 44.2 |
| 9e8e5f8e-e6aa-3ca3-b54b-6cde39b4df45 | -2.6242 | -45.7399 | 2024-12-04 04:00:00 | GOES-16 | SANTA LUZIA DO PARUÁ | MARANHÃO | Brasil | 2110039 | 21 | 33 | nan | nan | nan | Amazônia | 51.8 |
| 612d890c-b4ab-3964-a3cd-7f2ce0fd07ad | -1.6446 | -52.393 | 2024-12-04 04:00:00 | GOES-16 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 50.1 |
| f1a7f3ce-9efe-3b26-9d21-887763534856 | -3.259 | -53.659 | 2024-12-04 04:00:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 71.7 |
| 635905df-f5ac-3370-b724-3db1e43d23b1 | -1.7729 | -52.6156 | 2024-12-04 04:00:00 | GOES-16 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 58.9 |
| d40ef14e-c0e4-3e56-948a-da976a925368 | -1.7544 | -52.6363 | 2024-12-04 04:00:00 | GOES-16 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 124.3 |
| 741624c1-8b46-3688-94a3-728e0615e3fd | -6.0858 | -48.0774 | 2024-12-04 04:00:00 | GOES-16 | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | 79.0 |
| af5c9d26-9506-3470-aa22-e4be3e5ffa72 | -2.8012 | -53.0633 | 2024-12-04 04:00:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 61.1 |
| 05ce60e8-573f-3962-9a45-46124d309d9f | -1.7361 | -52.6162 | 2024-12-04 04:00:00 | GOES-16 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 94.3 |
| 8c06912a-56d6-3ba7-8d95-fc4a210d9686 | -1.663 | -52.3927 | 2024-12-04 04:00:00 | GOES-16 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 64.8 |
| 547573a1-8184-397d-88a8-b43dabcf67ce | -1.6631 | -52.3723 | 2024-12-04 04:00:00 | GOES-16 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 62.8 |
| 55add853-4ee2-3542-ac95-2bd93143c099 | -6.0674 | -48.0569 | 2024-12-04 04:00:00 | GOES-16 | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | 55.0 |
| cc5d1525-b9c5-398d-bf89-76830d56380b | -1.6447 | -52.3725 | 2024-12-04 04:00:00 | GOES-16 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 49.0 |
| b03856a2-3399-301f-8bb4-43d8babd8e0e | -1.7728 | -52.636 | 2024-12-04 04:00:00 | GOES-16 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 64.0 |
| 0cb2e456-fd80-30f8-b132-6ebaefa5e617 | -2.8197 | -53.0425 | 2024-12-04 04:00:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 70.8 |
| 1a8c1119-cf44-38db-a14e-a2dffc6b098c | -2.8196 | -53.0629 | 2024-12-04 04:00:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 88.6 |
| 7f892a45-6e8d-322a-97ae-e45e93392b1d | -1.7361 | -52.6366 | 2024-12-04 04:00:00 | GOES-16 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 53.9 |
| 37f527c8-2d1a-3661-8975-b3fa8842e312 | -1.663 | -52.3927 | 2024-12-04 04:10:00 | GOES-16 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 49.7 |
| 714d940b-9036-3dae-a677-5bc9bada00c2 | -1.7545 | -52.6159 | 2024-12-04 04:10:00 | GOES-16 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 159.1 |
| abbc59a5-d86e-3f7f-9b20-93ed5f550b1c | -3.1086 | -54.6068 | 2024-12-04 04:10:00 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 41.4 |
| 3814ec32-c736-3880-98f8-bf27ea727969 | -3.259 | -53.659 | 2024-12-04 04:10:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 61.6 |
| 6f829715-78cc-3ccb-9794-253d7e5ca309 | -2.6428 | -45.7394 | 2024-12-04 04:10:00 | GOES-16 | NOVA OLINDA DO MARANHÃO | MARANHÃO | Brasil | 2107357 | 21 | 33 | nan | nan | nan | Amazônia | 55.8 |
| 72d6ed33-8fa6-3a92-b8f3-0ab0815939c8 | -6.086 | -48.0557 | 2024-12-04 04:10:00 | GOES-16 | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | 122.8 |
| 3aac2792-7d7b-3ce2-83f4-5dcc4f9d6a11 | -2.8197 | -53.0425 | 2024-12-04 04:10:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 65.9 |
| 0514aaec-e535-39ed-ac6a-f7aa7287231f | -6.0672 | -48.0786 | 2024-12-04 04:10:00 | GOES-16 | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | 56.9 |
| 480ce3df-8ad5-36f2-ad27-78f4cf20dacc | -1.7728 | -52.636 | 2024-12-04 04:10:00 | GOES-16 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 79.2 |
| ac14ff25-73f4-34b3-9623-4ab5c418234c | -3.127 | -54.6063 | 2024-12-04 04:10:00 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 54.9 |
| ea83311f-a552-320c-8bfc-463d2d0a90ad | -3.259 | -53.6388 | 2024-12-04 04:10:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 60.9 |
| ca39a3a3-bbb6-3414-85d4-cf6873f779c7 | -2.8196 | -53.0629 | 2024-12-04 04:10:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 85.9 |
| 26dd43ea-bb02-398d-a59d-a937cee79e18 | -2.8012 | -53.0633 | 2024-12-04 04:10:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 58.4 |
| 7e52e18a-094e-3a05-8afa-5462ccf3141b | -1.7729 | -52.6156 | 2024-12-04 04:10:00 | GOES-16 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 74.9 |
| 95d4f265-6a01-39a4-ada5-78a4c29885ea | -1.7361 | -52.6162 | 2024-12-04 04:10:00 | GOES-16 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 76.9 |
| 267db777-7eda-373c-a139-e677785259b4 | -3.1269 | -54.6263 | 2024-12-04 04:10:00 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 45.7 |
| aee95d6e-db9f-364c-b4d3-c540db2ccf38 | -6.0858 | -48.0774 | 2024-12-04 04:10:00 | GOES-16 | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | 104.2 |
| 992b2b8a-2075-35a7-962f-644bfd991a5f | -1.6446 | -52.393 | 2024-12-04 04:10:00 | GOES-16 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 51.8 |
| 9ee183f2-a070-329b-8c5f-66a17ef0f3a0 | -1.7544 | -52.6363 | 2024-12-04 04:10:00 | GOES-16 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 134.1 |
| d5f06ed1-bc56-3591-8819-b1f206634196 | -3.2591 | -53.6186 | 2024-12-04 04:10:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 55.9 |
| d93a2783-09c7-35f9-aab5-a8a1c5dcc91a | -6.0674 | -48.0569 | 2024-12-04 04:10:00 | GOES-16 | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | 61.1 |
| efcf4302-bbae-35bd-993c-769fe5cd5b2c | -3.25338 | -50.61198 | 2024-12-04 04:10:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 97b4305d-f717-3cbb-a551-18c2cb8db502 | -2.9038 | -51.82299 | 2024-12-04 04:10:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 7.5 |
| 927ef837-644b-3efe-8af1-0d777644bda0 | -3.25823 | -53.65345 | 2024-12-04 04:10:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 701ac9ee-6464-33fb-b791-e0b932bd5b7c | -2.1991 | -47.24813 | 2024-12-04 04:10:00 | NOAA-20 | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 6.5 |
| ad759961-9896-3b85-aeca-d5e20fadd29e | -3.85393 | -52.1607 | 2024-12-04 04:10:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 291f757c-602b-3d2d-aad9-66feb1fa34f2 | -1.74799 | -52.63235 | 2024-12-04 04:10:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 6708993f-2de3-3259-b16d-3c5eb6ae9644 | -3.70537 | -51.06905 | 2024-12-04 04:10:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 8350ea5e-6abc-372d-9441-0f0057798067 | -2.81469 | -53.06508 | 2024-12-04 04:10:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 54842704-14d9-35aa-96ae-0356fddf7997 | -3.57687 | -43.30864 | 2024-12-04 04:10:00 | NOAA-20 | MATA ROMA | MARANHÃO | Brasil | 2106409 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| c69f4531-4d25-3f02-833d-615ebf52e8ff | -4.19774 | -50.67952 | 2024-12-04 04:10:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 821e4df8-62f7-3826-9d5f-48cbda461a7d | -4.05017 | -47.00034 | 2024-12-04 04:10:00 | NOAA-20 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 939b58ec-9ef4-35cb-8638-7a4ff99fa0b9 | -3.33195 | -51.20528 | 2024-12-04 04:10:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 4257018e-8cc6-30bd-8c6b-9ba41a8f0ffc | -2.02596 | -46.8476 | 2024-12-04 04:10:00 | NOAA-20 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 3c72cf66-0bf8-3d5d-925e-b754ae343daf | -3.93401 | -46.92125 | 2024-12-04 04:10:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 2.2 |
| dc4b5250-3704-384b-8e9d-475abee87025 | -0.25614 | -51.5041 | 2024-12-04 04:10:00 | NOAA-20 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 57315257-ab6d-3c11-8bb0-27724221e278 | -3.89863 | -46.67255 | 2024-12-04 04:10:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 8a0338ce-242b-3233-9938-ef86eac7d27d | -5.122 | -43.206 | 2024-12-04 04:10:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 018fd496-cf51-3048-b190-66ef7103bf4d | -3.09942 | -54.68999 | 2024-12-04 04:10:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 71ab6e32-580d-3575-bdae-1e2f894fa1e5 | -4.07299 | -46.6794 | 2024-12-04 04:10:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| d12f5bdf-53d4-36e5-8eef-b01bdc8d296b | -3.10037 | -54.68446 | 2024-12-04 04:10:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |


[Clique aqui para ver as próximas entradas](README22.md)
