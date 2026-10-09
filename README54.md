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

## Dados Diários - Página 54

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| d43c04f2-16db-3104-b94f-253b616605c5 | -8.5367 | -67.032 | 2026-10-09 02:50:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 64.3 |
| c0b7035c-4085-354c-9171-29db724eccd3 | -6.0024 | -40.935 | 2026-10-09 02:50:00 | GOES-19 | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 93.5 |
| a73f4d05-527e-3a80-ad98-4fe015bee68e | -7.2187 | -55.0815 | 2026-10-09 02:50:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 57.9 |
| 80c6483d-9e3c-324b-a01e-d75f5558b46e | -9.4578 | -40.3392 | 2026-10-09 02:50:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 72.0 |
| a09b7630-df52-3f2c-9803-c956c792a7c6 | -3.5493 | -54.6951 | 2026-10-09 02:50:00 | GOES-19 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 106.2 |
| 489af89b-b17d-3f09-a125-f3a3c0e4768b | -3.1285 | -54.1657 | 2026-10-09 02:50:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 152.2 |
| 511f6c7a-a9e2-327c-88c4-56f6ee28ada8 | -3.5677 | -54.6746 | 2026-10-09 02:50:00 | GOES-19 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 63.6 |
| e4629b16-b444-35b2-93d2-c284b75a7a98 | -6.7363 | -55.1675 | 2026-10-09 02:50:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 96.8 |
| 8369bc50-59a6-3202-aadb-5d93a2e3fc4c | -12.2346 | -57.1071 | 2026-10-09 02:50:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 223.6 |
| 342bd002-a77b-3a36-9f3e-7fa277a9dd24 | -3.5493 | -54.6752 | 2026-10-09 02:50:00 | GOES-19 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 59.9 |
| 1328715c-4449-3090-a8b1-1d9a56aa8914 | -13.1827 | -54.3571 | 2026-10-09 02:50:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 74.8 |
| 794aa943-0c89-3bb8-bbd9-97cb41b49448 | -8.742 | -45.1563 | 2026-10-09 02:50:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 176.5 |
| 463f1bbc-4c5c-37de-bebb-e458e12cdbd8 | -8.5051 | -54.6202 | 2026-10-09 02:50:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 48.1 |
| dbee7b6b-ca89-36ab-91cc-59612b735597 | -8.5183 | -67.0139 | 2026-10-09 03:00:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 48.8 |
| 91ce0f80-3780-3056-9fe5-b1cbb5477fa5 | -2.7428 | -54.1146 | 2026-10-09 03:00:00 | GOES-19 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 58.6 |
| 1ad7058c-3c47-35f5-b80c-af2823a68fdc | -7.1995 | -55.1627 | 2026-10-09 03:00:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 64.0 |
| 7bd0b667-156e-3643-8600-a83db08ff1ea | -13.2662 | -42.2365 | 2026-10-09 03:00:00 | GOES-19 | CATURAMA | BAHIA | Brasil | 2907558 | 29 | 33 | nan | nan | nan | Caatinga | 221.5 |
| 6bb1a63d-ce4c-389c-93d3-d56a437439ec | -12.2158 | -57.0887 | 2026-10-09 03:00:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 68.6 |
| a8fac145-d67b-3c75-8344-23ce2500e79a | -3.5676 | -54.6946 | 2026-10-09 03:00:00 | GOES-19 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 85.5 |
| 31fdf5b8-2780-3b5b-90c6-b3a3f538d414 | -6.0021 | -40.9594 | 2026-10-09 03:00:00 | GOES-19 | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 264.4 |
| ce9aea35-edcd-3a62-8034-a99f98f97fa3 | -13.1827 | -54.3571 | 2026-10-09 03:00:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 64.8 |
| ba39e1e0-0271-33c7-a416-95b1b2479479 | -3.5493 | -54.6752 | 2026-10-09 03:00:00 | GOES-19 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 67.4 |
| 90bd42d7-a10c-367e-95b4-6e2ec7ffdf2d | -6.021 | -40.9577 | 2026-10-09 03:00:00 | GOES-19 | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 75.7 |
| 8ae681ee-c40e-370a-8e57-8abf15fe7e88 | -9.4578 | -40.3392 | 2026-10-09 03:00:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 190.7 |
| a29a843f-c580-3f3e-947a-92a8154d462b | -5.7117 | -53.4862 | 2026-10-09 03:00:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 61.3 |
| 0fe6eac6-2bc1-3204-a341-f3b08cd92f24 | -8.742 | -45.1563 | 2026-10-09 03:00:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 127.4 |
| b9c6285d-760c-3778-8113-c44bbf16597b | -3.11 | -54.1862 | 2026-10-09 03:00:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 64.6 |
| 1a06d39a-9d55-33ae-9d7b-31c1cbdab790 | -8.5367 | -67.032 | 2026-10-09 03:00:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 47.9 |
| 4ee3bd4e-2691-3c52-ad50-5ae252f68ac6 | -3.0007 | -53.9075 | 2026-10-09 03:00:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 81.8 |
| 60d0bb71-3a42-346c-89be-e3a91fd86f55 | -8.5183 | -67.0325 | 2026-10-09 03:00:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 92.4 |
| 01ffd6af-4a47-317d-b837-bde2a943f77c | -7.9086 | -54.7194 | 2026-10-09 03:00:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 45.0 |
| b9156124-90c7-3d96-8028-d40a1ed2e816 | -9.4773 | -40.3116 | 2026-10-09 03:00:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 87.4 |
| 14b77aa2-66fd-34c0-ad68-09199fd2f965 | -8.7426 | -45.1106 | 2026-10-09 03:00:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 48.0 |
| 8784fb88-a2c5-3cfe-b710-954b8c7ef26b | -3.1109 | -53.945 | 2026-10-09 03:00:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 73.6 |
| e7937284-7c36-3225-b701-0519729f0de5 | -13.2657 | -42.2609 | 2026-10-09 03:00:00 | GOES-19 | CATURAMA | BAHIA | Brasil | 2907558 | 29 | 33 | nan | nan | nan | Caatinga | 132.2 |
| 3b5b19f2-cf03-323f-b969-9bf5c5a3e134 | -3.1284 | -54.1857 | 2026-10-09 03:00:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 82.3 |
| 04001a9c-2e61-3edf-a22b-8bc8007dcf66 | -9.4769 | -40.3365 | 2026-10-09 03:00:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 526.8 |
| 3adae069-22e5-3d71-a71a-95a0011c3268 | -2.499 | -56.0675 | 2026-10-09 03:00:00 | GOES-19 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 87.5 |
| a79ef9bb-fe99-3924-b54b-db399b3b3a44 | -8.7231 | -45.1583 | 2026-10-09 03:00:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 87.5 |
| 744a3b00-3361-37f2-bdd6-2cfbaa9bef9b | -7.2182 | -55.1416 | 2026-10-09 03:00:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 64.2 |
| 6e7d53d5-d919-366e-800e-d7f457cb1bcc | -13.2462 | -42.2645 | 2026-10-09 03:00:00 | GOES-19 | CATURAMA | BAHIA | Brasil | 2907558 | 29 | 33 | nan | nan | nan | Caatinga | 174.3 |
| 4f92434b-33dc-38f3-ab82-183361f454dc | -7.218 | -55.1617 | 2026-10-09 03:00:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 77.5 |
| ae619cec-8376-30b8-8896-7dbb4fe23d37 | -12.2348 | -57.0871 | 2026-10-09 03:00:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 83.7 |
| 48ed631e-68bf-37af-9b93-49edfbdb6475 | -12.2154 | -57.1287 | 2026-10-09 03:00:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 44.6 |
| 8617e746-a61a-30bc-8de3-7a3a7810d377 | -9.4765 | -40.3613 | 2026-10-09 03:00:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 115.3 |
| 4347393a-dd3d-32a2-b381-cf1796bededd | -12.2156 | -57.1087 | 2026-10-09 03:00:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 93.5 |
| 72c484a7-e2cc-3a5d-928d-15c3ca420a20 | -3.1787 | -50.5807 | 2026-10-09 03:00:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 56.8 |
| b0472011-5a0b-37d7-b1b7-cba953c3f8d1 | -3.1101 | -54.1661 | 2026-10-09 03:00:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 79.5 |
| a753f2e3-f23d-3aea-a7ed-9566f33488c7 | -10.6199 | -60.4852 | 2026-10-09 03:00:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 76.6 |
| c92f77ca-7f2e-3885-974b-4e4724e05846 | -8.537 | -66.9764 | 2026-10-09 03:00:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 46.5 |
| 6d826eb2-f09c-3e6b-85b2-cb97f497cfc0 | -3.5493 | -54.6951 | 2026-10-09 03:00:00 | GOES-19 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 86.5 |
| 9615efbb-8f3b-3160-9a4a-6c3e63864318 | -10.6012 | -60.4863 | 2026-10-09 03:00:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 43.1 |
| 14f8fb7a-2400-35ad-9122-04019e00fedc | -8.7234 | -45.1355 | 2026-10-09 03:00:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 90.6 |
| c0637fbe-f0de-36e9-b4d1-bc8ba298a323 | -13.1639 | -54.3385 | 2026-10-09 03:00:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 58.8 |
| d563b3bd-2cd4-3b98-a392-6af1b1219670 | -12.2346 | -57.1071 | 2026-10-09 03:00:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 111.9 |
| 8ad977a7-b629-3626-a514-273329df7bbb | -3.1285 | -54.1657 | 2026-10-09 03:00:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 124.9 |
| c1cebdd7-e0a4-30e2-be06-7f7241ef8f98 | -3.5677 | -54.6746 | 2026-10-09 03:00:00 | GOES-19 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 69.2 |
| f90878b4-2281-3563-aa75-e3e190359c9f | -3.1114 | -53.7839 | 2026-10-09 03:00:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 66.3 |
| 99173418-2741-3359-88f2-ad0fe2579bcb | -6.0019 | -40.9837 | 2026-10-09 03:00:00 | GOES-19 | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 111.9 |
| be35272d-de4a-38d2-839b-47155f9acd7b | -2.823 | -58.2838 | 2026-10-09 03:00:00 | GOES-19 | SILVES | AMAZONAS | Brasil | 1304005 | 13 | 33 | nan | nan | nan | Amazônia | 47.5 |
| ab5e26bb-5cd0-36d5-aa83-e872f44ef012 | -5.6934 | -53.4667 | 2026-10-09 03:00:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 48.8 |
| 018d7fad-1f3a-317e-8803-2aec8358c5a6 | -13.2467 | -42.2401 | 2026-10-09 03:00:00 | GOES-19 | CATURAMA | BAHIA | Brasil | 2907558 | 29 | 33 | nan | nan | nan | Caatinga | 296.4 |
| 7550ef28-8d30-3084-9f95-2e980b44f51e | -6.0024 | -40.935 | 2026-10-09 03:00:00 | GOES-19 | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 81.9 |
| 10447e8f-95fc-3e2b-a1ee-f73225f4a50a | -7.2187 | -55.0815 | 2026-10-09 03:00:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 49.7 |
| 820bfbdd-2090-3d9f-93f1-7e6881ca016d | -13.1636 | -54.3591 | 2026-10-09 03:00:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 61.3 |
| 17da47a0-4255-327a-ac37-bb09f4fd4a2e | -8.7423 | -45.1334 | 2026-10-09 03:00:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 232.0 |
| 0eb4b5e8-e9ce-3737-8a89-c633308dd69c | -3.0925 | -53.9455 | 2026-10-09 03:00:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 74.3 |
| 9408a98e-0172-357f-a71c-4171c479854e | -10.6201 | -60.4658 | 2026-10-09 03:00:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 36.8 |
| 5a28680f-736e-3fe1-9bcc-1e653a69fa4b | -8.7067 | -62.4184 | 2026-10-09 03:10:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 48.2 |
| c56d4de5-cc48-3baf-91a9-5ac02d8c0d39 | -3.5677 | -54.6746 | 2026-10-09 03:10:00 | GOES-19 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 61.9 |
| 7af65750-c9e4-396f-b456-744b41073dd2 | -3.1787 | -50.5807 | 2026-10-09 03:10:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 52.7 |
| ec733acd-9f05-3f88-a22c-260486a5a19c | -6.0207 | -40.982 | 2026-10-09 03:10:00 | GOES-19 | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 101.8 |
| 0cdf1ffe-f9e4-3087-b594-9640b5ba722d | -3.1285 | -54.1657 | 2026-10-09 03:10:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 111.1 |
| 56e231f5-7d63-35f6-9ccb-e323a8c35ac8 | -13.1827 | -54.3571 | 2026-10-09 03:10:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 63.4 |
| d450c37b-8749-36a3-9c1a-623bfeabf284 | -6.0021 | -40.9594 | 2026-10-09 03:10:00 | GOES-19 | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 578.9 |
| 357c71a8-c51d-3801-bbab-76c0deae5656 | -7.5649 | -61.5523 | 2026-10-09 03:10:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 31.1 |
| 52f021da-e6ca-3dba-b2b3-11a89526f707 | -3.1114 | -53.7839 | 2026-10-09 03:10:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 66.0 |
| f96bdf9f-ba0b-3905-9e73-f5f8b4279a98 | -6.8907 | -45.8988 | 2026-10-09 03:10:00 | GOES-19 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 50.9 |
| 2c3f7e34-2e1f-3886-bafb-f8078080d83f | -8.6882 | -62.4192 | 2026-10-09 03:10:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 39.8 |
| f4ef73d1-f6ad-3188-8c8d-165af2267bf3 | -5.6934 | -53.4667 | 2026-10-09 03:10:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 47.6 |
| 2a1e6e55-92c8-351d-bb30-c9612db034b7 | -8.7234 | -45.1355 | 2026-10-09 03:10:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 62.6 |
| b64ba90c-d237-36a7-be3f-7fda436f4f2a | -10.6199 | -60.4852 | 2026-10-09 03:10:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 58.5 |
| 5e74a0b4-596a-35f5-8079-8d64b35e21e1 | -8.7068 | -62.3995 | 2026-10-09 03:10:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 47.4 |
| cfee4600-e99d-33ea-9b38-711ffe1ea254 | -7.1995 | -55.1627 | 2026-10-09 03:10:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 65.1 |
| eeff5461-b555-36cc-973e-3f22c273abcb | -3.1109 | -53.945 | 2026-10-09 03:10:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 69.4 |
| 951a7e7b-a974-367e-98cd-276e38f5332c | -3.1284 | -54.1857 | 2026-10-09 03:10:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 78.8 |
| 2f98459e-6f31-35cb-8a57-5ba514372907 | -8.6883 | -62.4002 | 2026-10-09 03:10:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 38.5 |
| a85c3b1c-6974-3765-a62a-e68c08155aff | -3.3455 | -50.4078 | 2026-10-09 03:10:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 51.0 |
| 3057a850-9376-3455-a413-3d379a1ed13a | -10.8598 | -45.5394 | 2026-10-09 03:10:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 74.4 |
| 9ba891e2-c9c8-3830-9995-c21d168798cb | -7.2182 | -55.1416 | 2026-10-09 03:10:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 55.8 |
| d0501bc9-eb4d-3078-8430-fa7db2c12db6 | -6.8719 | -45.9003 | 2026-10-09 03:10:00 | GOES-19 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 59.5 |
| c859ee98-135e-3af1-8642-958fca255fc9 | -7.218 | -55.1617 | 2026-10-09 03:10:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 74.4 |
| 37d109e8-ac42-34f6-82db-fa48b19b0c90 | -3.1101 | -54.1661 | 2026-10-09 03:10:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 80.9 |
| 2a25b91c-688a-3797-af82-fbc72009f287 | -2.499 | -56.0675 | 2026-10-09 03:10:00 | GOES-19 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 88.2 |
| f1fc59f7-abd2-3dc4-85d3-2ae148d57262 | -6.0019 | -40.9837 | 2026-10-09 03:10:00 | GOES-19 | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 250.9 |
| 7102f372-b57e-3230-9591-5fd8851dea72 | -13.1639 | -54.3385 | 2026-10-09 03:10:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 54.1 |
| 126dd314-0368-39e9-a5f8-0ada6ce306e9 | -7.9086 | -54.7194 | 2026-10-09 03:10:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 46.5 |
| d73ec00d-36a1-3332-8818-a673c5c2e078 | -13.1636 | -54.3591 | 2026-10-09 03:10:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 59.3 |
| 0b5702fc-deda-37f2-a305-2f4b0f026815 | -5.7117 | -53.4862 | 2026-10-09 03:10:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 58.5 |
| c9bbc9a0-9913-34dc-b0d4-ab63ecf9d7d6 | -6.0024 | -40.935 | 2026-10-09 03:10:00 | GOES-19 | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 123.6 |


[Clique aqui para ver as próximas entradas](README55.md)
