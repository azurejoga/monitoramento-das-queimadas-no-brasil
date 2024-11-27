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

## Dados Diários - Página 39

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| b0a97e38-d00c-399f-a3f7-8a1a363c0e56 | -3.81571 | -47.47389 | 2024-11-27 04:18:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c6c71e8e-58df-3c1d-a4eb-672e402ff87f | -4.38976 | -47.77432 | 2024-11-27 04:18:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| bf8cc964-c5ac-3a25-a323-7a547d453c50 | -4.2474 | -48.6777 | 2024-11-27 04:18:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| cbba7e61-1483-37d2-8fe5-d2770b212ed5 | -2.71114 | -46.29927 | 2024-11-27 04:18:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c743f586-7f95-31d2-a06a-abd7991d8e90 | -3.90462 | -42.24612 | 2024-11-27 04:18:00 | NPP-375D | ESPERANTINA | PIAUÍ | Brasil | 2203701 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 43cc4789-8278-3e3b-b934-53e40d7011ae | -4.01465 | -47.6538 | 2024-11-27 04:18:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| e4d36621-de67-33d0-9d84-a2b23e802b80 | -2.82189 | -48.60791 | 2024-11-27 04:18:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 15ee8619-6ca6-3447-ac33-8f66322e8d27 | -3.4101 | -50.20438 | 2024-11-27 04:18:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| c53f9fdf-f228-3238-9756-f58b2d213889 | -3.78951 | -50.1373 | 2024-11-27 04:18:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| f3b94c85-c3cc-3c6c-9e12-d97bdd5f9681 | -2.82561 | -45.9231 | 2024-11-27 04:18:00 | NPP-375D | NOVA OLINDA DO MARANHÃO | MARANHÃO | Brasil | 2107357 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 374ca554-bada-3076-a3f3-367b2d1b5d33 | -1.18594 | -51.976 | 2024-11-27 04:18:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 16366bdd-b6c9-3d78-9953-e73b9a4aaf5b | -4.09166 | -44.85861 | 2024-11-27 04:18:00 | NPP-375D | LAGO VERDE | MARANHÃO | Brasil | 2105906 | 21 | 33 | nan | nan | nan | Amazônia | 3.0 |
| e60a3580-1ea4-3996-977d-926edad19efa | -4.18245 | -48.63161 | 2024-11-27 04:18:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 18f9ae95-2b7b-3d0b-be78-c796460e31c8 | -3.96867 | -48.08438 | 2024-11-27 04:18:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 6.8 |
| ed981fb5-3ff0-32b8-91ca-97e9a9338c32 | -3.11318 | -45.95539 | 2024-11-27 04:18:00 | NPP-375D | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 306dc846-0dc5-32d0-97f1-310e18c26177 | -3.91216 | -42.41966 | 2024-11-27 04:18:00 | NPP-375D | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 860d4e13-77aa-3750-a7db-92ffcec070d7 | -2.79693 | -52.90849 | 2024-11-27 04:18:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| fafcf3c3-4960-3b1c-9c15-c7280f35a2e6 | -3.97626 | -48.06192 | 2024-11-27 04:18:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 8b45a7b7-c867-34e4-aa1a-409f321f2858 | -1.36396 | -52.12888 | 2024-11-27 04:18:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 6a00f9e7-b0ba-3439-9079-6301bda5a2cb | -2.86694 | -46.80947 | 2024-11-27 04:18:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| fd762aca-713b-32fd-94e6-956831915748 | -1.95806 | -52.16854 | 2024-11-27 04:18:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 3d32060e-a0e0-35b2-8df8-9140d0bc50de | -1.76581 | -53.62053 | 2024-11-27 04:18:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 64a672da-a88e-3364-a987-ca1ae3357b97 | -2.18401 | -53.78305 | 2024-11-27 04:18:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 19.0 |
| b9310af3-ce62-38a0-b5cb-c6c3669184bb | -3.97324 | -48.08029 | 2024-11-27 04:18:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 441edbf6-a087-3a31-94f6-b3b2499323e0 | -4.06575 | -41.44595 | 2024-11-27 04:18:00 | NPP-375D | BRASILEIRA | PIAUÍ | Brasil | 2201960 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| e87e0a10-952a-325e-8d99-993ae73571cd | -4.14692 | -43.7991 | 2024-11-27 04:18:00 | NPP-375D | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 0acf82b1-caaf-3f9c-9015-9bcd46897acf | -2.4977 | -52.14979 | 2024-11-27 04:18:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 93dc697b-0ebc-30c1-9115-24be8587df30 | -2.94315 | -54.79045 | 2024-11-27 04:18:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 26650df0-cadf-34f3-867b-cc1a23c52c88 | -4.23167 | -48.67522 | 2024-11-27 04:18:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| d04874f7-7fb5-36a3-81fc-30b112a1caab | -3.9434 | -46.69393 | 2024-11-27 04:18:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 130c7d58-a655-3902-a700-1b7e99a60521 | -1.65486 | -52.4169 | 2024-11-27 04:18:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 1b4caf0b-d168-38db-8428-c39303c5309a | -3.10305 | -53.27046 | 2024-11-27 04:18:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| bf179095-c166-3a3d-8eec-705deb85b0b3 | -4.22703 | -46.88401 | 2024-11-27 04:18:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 0034697f-6e2a-309b-86bb-2ef99486e2be | -3.90188 | -47.73288 | 2024-11-27 04:18:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 7cd8ed4a-428f-3d7a-944e-42c7d1df19e2 | -3.58834 | -50.35513 | 2024-11-27 04:18:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c7a6fec1-ff9e-361c-b5d9-e59351ed9717 | -2.62139 | -46.20622 | 2024-11-27 04:18:00 | NPP-375D | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 8622865d-f937-34e4-b471-4af5ff3039d7 | -3.44896 | -50.29898 | 2024-11-27 04:18:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 98dafec9-f457-34b3-82dd-08332c3cd1ba | -4.40908 | -44.1124 | 2024-11-27 04:18:00 | NPP-375D | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 4e032693-aee4-355d-8a7c-3ab2600ead1b | -4.21676 | -48.66778 | 2024-11-27 04:18:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 7.6 |
| dea484c9-716e-32ff-8262-dc40d10652ad | -3.91273 | -42.41601 | 2024-11-27 04:18:00 | NPP-375D | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 7.3 |
| ad8ca0ad-2ed7-3ff5-8970-c216a4ec24fc | -3.10247 | -53.27402 | 2024-11-27 04:18:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 096a997e-0df1-398a-9fac-b63f1fc84a03 | -3.80805 | -46.59286 | 2024-11-27 04:18:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 1663a7ab-826b-315a-af63-ce054759c41c | -3.22928 | -50.78308 | 2024-11-27 04:18:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 877a896f-c57e-362c-bfef-14aba1d22f15 | -5.8831 | -41.32883 | 2024-11-27 04:18:00 | NPP-375D | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 10cdcc2b-0775-3579-bceb-c1c0465f65bf | -1.19041 | -51.76896 | 2024-11-27 04:18:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ff691d47-2ce7-34e2-8d3f-f5362ee56a41 | -5.58809 | -43.15361 | 2024-11-27 04:18:00 | NPP-375D | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Caatinga | 3.7 |
| 951e9740-c3f9-3434-b6aa-53873a444dd8 | -3.609 | -49.89455 | 2024-11-27 04:18:00 | NPP-375D | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 7e66de71-9237-3e78-9031-62bcdb7f7ad8 | -3.59531 | -50.36026 | 2024-11-27 04:18:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 6.5 |
| 0cee92cc-1022-3307-992c-116b10174b8c | -2.60043 | -51.83046 | 2024-11-27 04:18:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 7c55b9d3-3828-31f6-8234-c01163976a5d | -2.83296 | -54.12372 | 2024-11-27 04:18:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 18.0 |
| abfe56e2-3cc2-3700-aa30-32526ef1b5a9 | -3.2848 | -50.61618 | 2024-11-27 04:18:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 0f0465e7-6958-315c-8071-d534e70c4a59 | -2.11281 | -46.45729 | 2024-11-27 04:18:00 | NPP-375D | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 20.1 |
| 83769b9a-b31f-3571-b8b3-4dfdc786a7f8 | -5.6986 | -43.25848 | 2024-11-27 04:18:00 | NPP-375D | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 8869b70c-b766-3217-9be6-739cb7dd4555 | -2.60388 | -53.97018 | 2024-11-27 04:18:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| dc182cd6-597a-3d5d-8d33-90c2a3d0bbe7 | -2.81039 | -46.83131 | 2024-11-27 04:18:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 23b20f99-a550-37fb-866c-151816c9115e | -3.17907 | -50.2207 | 2024-11-27 04:18:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 15e58986-6453-3add-8cb3-9a893a4f0427 | -2.93617 | -54.79962 | 2024-11-27 04:18:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| aa5b4c6d-2aa1-38f5-9fee-9b3d2213148a | -4.66856 | -46.38415 | 2024-11-27 04:18:00 | NPP-375D | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 0370bc33-b27e-3a54-b05d-b9ea18004405 | -2.69775 | -51.98542 | 2024-11-27 04:18:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 712a1399-b721-362a-8306-bccea700a6ef | -3.85059 | -46.50735 | 2024-11-27 04:18:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| e70e3e99-cdbd-305e-ba0d-765494109fd6 | -3.29027 | -50.27509 | 2024-11-27 04:18:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| cbdde4f0-520c-327b-bf87-4fe8b82aea8d | -3.84449 | -47.73265 | 2024-11-27 04:18:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 265b4f1e-0b10-327d-8e69-ad6a0244fa7c | -3.2822 | -51.11556 | 2024-11-27 04:18:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 19fddf68-8a06-3293-8a7e-6c4f83719d5e | -4.65424 | -43.82175 | 2024-11-27 04:18:00 | NPP-375D | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| c5e1ad5c-b8e0-3fee-bacb-2da26c743f96 | -4.02475 | -45.5425 | 2024-11-27 04:18:00 | NPP-375D | ALTAMIRA DO MARANHÃO | MARANHÃO | Brasil | 2100402 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 841f57bf-38ab-3287-84ae-72cb6e04d397 | -2.59746 | -53.97317 | 2024-11-27 04:18:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 21515c7c-367a-30d8-9f09-8dd1fa09e61f | -3.95064 | -46.91564 | 2024-11-27 04:18:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 5ac9e79f-41ec-3cb0-ac2e-77f3aa35bcb6 | -3.97053 | -46.72564 | 2024-11-27 04:18:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| cacc285c-99af-318f-afc3-d85f37faabfe | -2.46668 | -48.79808 | 2024-11-27 04:18:00 | NPP-375D | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| e0030b7f-0c96-362f-bbb2-3d1655281cb9 | -3.18706 | -48.42898 | 2024-11-27 04:18:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 3a58f37e-815a-3bf5-86d5-275d6f62b77e | -3.08175 | -47.81543 | 2024-11-27 04:18:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 87ef378f-533c-3aa9-bc40-f31e82ba6a0a | -3.08533 | -53.28037 | 2024-11-27 04:18:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 08ca7293-bcb7-3a28-b7dd-a3caa4464d17 | -3.65639 | -50.23802 | 2024-11-27 04:18:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 30093ef8-d924-331b-8d10-239292d356bc | -1.79343 | -52.74308 | 2024-11-27 04:18:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 5e466b84-eb30-32bf-b30f-ba4f2d948cf3 | -4.17219 | -48.45221 | 2024-11-27 04:18:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| e1c7fb58-7615-3c0b-896e-4c0ce301af61 | -3.10189 | -53.27757 | 2024-11-27 04:18:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 388383d2-529b-372c-9af6-29716b396d4d | -3.45409 | -50.29538 | 2024-11-27 04:18:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 1f180e11-4481-3e66-8387-c82c6563f086 | -3.28588 | -50.75392 | 2024-11-27 04:18:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f7c55f32-2f81-3cc8-a483-a77759a8851b | -1.81146 | -45.92505 | 2024-11-27 04:18:00 | NPP-375D | MARACAÇUMÉ | MARANHÃO | Brasil | 2106326 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 80fc8cba-21a2-39ca-bb26-59120794fbcf | -3.75538 | -52.17902 | 2024-11-27 04:18:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d677d56e-cd9a-389d-a911-51ac0517082c | -3.06628 | -49.19884 | 2024-11-27 04:18:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 83c091e8-079f-3ee5-a1d6-8774a392f3a3 | -2.49723 | -52.15271 | 2024-11-27 04:18:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 0ccda5f3-d717-3947-a316-611249256a27 | -2.88699 | -51.38178 | 2024-11-27 04:18:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 40d5f17f-6cec-3e21-acee-349d50b4093b | -4.81378 | -46.84542 | 2024-11-27 04:18:00 | NPP-375D | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b6a92397-235e-3612-bf04-16a1d3fd5fb0 | -4.00303 | -44.04863 | 2024-11-27 04:18:00 | NPP-375D | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| e5098ff8-1fa7-39db-ba1d-0c3271ce5547 | -1.94511 | -46.59865 | 2024-11-27 04:18:00 | NPP-375D | VISEU | PARÁ | Brasil | 1508308 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e239dd11-abb1-3400-9208-6876c9df727c | -3.27872 | -48.75918 | 2024-11-27 04:18:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 52e97966-0670-38b6-b1e1-47d04a85ca96 | -4.23666 | -41.9253 | 2024-11-27 04:18:00 | NPP-375D | PIRIPIRI | PIAUÍ | Brasil | 2208403 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 047587e1-0c8f-346a-a5e8-f470489e6f08 | -4.05338 | -46.83578 | 2024-11-27 04:18:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 9fe129e2-2226-3a6a-8e54-ecf5342d78bc | -4.04853 | -46.84319 | 2024-11-27 04:18:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 012b0b53-6ae5-3d28-a292-d14a5abd6da5 | -4.59871 | -43.96136 | 2024-11-27 04:18:00 | NPP-375D | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 8b0ceade-3dbf-3c2e-ae5d-ba353ea3ba2f | -3.38772 | -50.09404 | 2024-11-27 04:18:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 5cc3e3e6-e066-3f15-ac49-bc7dcf8ba4dc | -3.0936 | -50.35426 | 2024-11-27 04:18:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 8b7548bd-0faa-3bf8-a5ef-d2fcbdb16695 | -5.3254 | -43.07364 | 2024-11-27 04:18:00 | NPP-375D | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| b8216279-26f8-39f1-8d12-80bb213f74ac | -3.21401 | -49.45856 | 2024-11-27 04:18:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 3934a679-eba7-3cee-b8f3-d720c3f49c80 | -2.83923 | -46.83585 | 2024-11-27 04:18:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 12.7 |
| 4b089cb3-ebb0-3841-a30c-82ae9f92debf | -4.16852 | -46.08281 | 2024-11-27 04:18:00 | NPP-375D | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 57d216a1-7027-36ce-b611-f8a7f79aed9b | -3.43347 | -54.53639 | 2024-11-27 04:18:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 279afad8-a70d-3ecb-9085-53b485dc35b0 | -5.21984 | -44.91069 | 2024-11-27 04:18:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| d70298b3-aad5-3a44-8d24-ca299ed72361 | -2.61656 | -52.53809 | 2024-11-27 04:18:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |


[Clique aqui para ver as próximas entradas](README40.md)
