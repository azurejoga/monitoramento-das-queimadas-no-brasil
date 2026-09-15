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

## Dados Diários - Página 53

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 76f36b87-98b1-33f2-b504-691f224b8b6c | -3.91955 | -54.51803 | 2026-09-15 05:16:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 777b5640-5961-3a5e-bd57-a629c19f1452 | -3.80993 | -58.90026 | 2026-09-15 05:16:00 | NOAA-21 | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| aa7ead45-4026-39bc-8e0a-017406a2a6fd | -3.40188 | -50.75277 | 2026-09-15 05:16:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 27f530aa-38c3-3343-b257-b6f5e4cabf3e | -3.10745 | -61.09914 | 2026-09-15 05:16:00 | NOAA-21 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 78c6156b-d2f8-379f-9445-2d105568e7be | -2.89289 | -50.41395 | 2026-09-15 05:16:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| b663ccbd-11be-3b2c-a529-7ec27ab0f817 | -3.54468 | -53.98406 | 2026-09-15 05:16:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| da1c718c-9c59-3647-b248-9fba8dcdd5a8 | -2.91578 | -50.39495 | 2026-09-15 05:16:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| e1d8b0cb-c71c-3e44-abb4-92323dec1f0d | 3.23861 | -61.23292 | 2026-09-15 05:16:00 | NOAA-21 | ALTO ALEGRE | RORAIMA | Brasil | 1400050 | 14 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 3b6ad646-916e-3f39-9cdf-faf781a5d7e2 | -3.07997 | -50.57372 | 2026-09-15 05:16:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| c8294d8b-ab03-38af-a9a9-09ca04909e0c | -2.58224 | -49.44267 | 2026-09-15 05:16:00 | NOAA-21 | MOCAJUBA | PARÁ | Brasil | 1504604 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 9532b354-5019-3c78-9527-18932e813a36 | -2.90888 | -54.15614 | 2026-09-15 05:16:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 408c5796-85e3-38ac-b1f6-6549255b960a | -3.35819 | -58.17786 | 2026-09-15 05:16:00 | NOAA-21 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| d06d4c7e-bbb6-3d99-907e-721e3c1e1708 | -3.81377 | -58.89733 | 2026-09-15 05:16:00 | NOAA-21 | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 427eaf8d-9681-31db-88b9-172fedddf4ea | -3.72994 | -61.74934 | 2026-09-15 05:16:00 | NOAA-21 | ANORI | AMAZONAS | Brasil | 1300102 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 24b0cb39-c7eb-3995-9ea9-b05eba663dee | -3.70366 | -58.86248 | 2026-09-15 05:16:00 | NOAA-21 | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | 3.3 |
| abea2f20-3272-38b0-9556-e81d258bbad0 | -1.3228 | -54.6622 | 2026-09-15 05:16:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 5c546f99-87f2-30e5-b4aa-1a35c3576bb0 | -2.69737 | -57.52695 | 2026-09-15 05:16:00 | NOAA-21 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 7.6 |
| 2bc85e13-f626-3c2b-ae34-109433900e65 | -1.00996 | -53.04085 | 2026-09-15 05:16:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| b3aee9e9-34b3-3833-874b-9a5116e2be89 | -3.3858 | -61.3079 | 2026-09-15 05:16:00 | NOAA-21 | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 837ee3ed-9648-3a96-8cff-cdd0c5f6efef | -2.90763 | -50.41625 | 2026-09-15 05:16:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| cb52bf9c-44cc-3861-9911-e157c9c6a9b2 | -3.26385 | -54.52579 | 2026-09-15 05:16:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| dada3684-e49c-3962-b583-30c39fb0c5e9 | -3.16305 | -58.64359 | 2026-09-15 05:16:00 | NOAA-21 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d70f1c7d-f9ce-3354-b134-db7c96a5caab | -3.64389 | -58.61319 | 2026-09-15 05:16:00 | NOAA-21 | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 0f86e90c-92b7-3340-b730-b3fc47c3497f | -3.08073 | -50.56845 | 2026-09-15 05:16:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 783982e5-3a67-3ace-aed7-7aef31d789e6 | -3.99464 | -59.73862 | 2026-09-15 05:16:00 | NOAA-21 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| d6dced59-ad28-38e5-a20b-0bfc296f6e74 | -3.37805 | -61.31081 | 2026-09-15 05:16:00 | NOAA-21 | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 8ad72c42-9614-31e1-9124-6efd42fed66a | 0.62101 | -60.15876 | 2026-09-15 05:16:00 | NOAA-21 | SÃO LUIZ | RORAIMA | Brasil | 1400605 | 14 | 33 | nan | nan | nan | Amazônia | 1.4 |
| fca8a025-8bff-3cc4-a02a-05ab75632f8c | -2.96581 | -50.3971 | 2026-09-15 05:16:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 942e8c17-427a-3876-9a86-e64101d462f3 | -3.44775 | -59.2579 | 2026-09-15 05:16:00 | NOAA-21 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| bb9ef6e0-8aa9-398b-b228-b6a26b1ec5ad | -3.32983 | -54.18974 | 2026-09-15 05:16:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| cc96fc64-6a54-3b5c-b77b-9bf655c1d269 | 2.76329 | -60.21597 | 2026-09-15 05:16:00 | NOAA-21 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 86c51e1b-e400-3766-97c4-f0fb2e39e81a | -3.84884 | -51.76422 | 2026-09-15 05:16:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 15.9 |
| d0923c91-f1e2-3da1-a2d4-1b5b970932ce | -3.73422 | -61.74573 | 2026-09-15 05:16:00 | NOAA-21 | ANORI | AMAZONAS | Brasil | 1300102 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 0d8cd63e-173a-36c9-9a70-82ae2f90776d | -2.68051 | -57.59185 | 2026-09-15 05:16:00 | NOAA-21 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 813a6035-14ef-37ba-97ba-c77838015400 | -3.39627 | -50.75733 | 2026-09-15 05:16:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| b5624e92-799c-3ffe-93b5-40d62736f2b5 | -4.53619 | -55.61992 | 2026-09-15 05:16:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 1a29ee35-ad66-3955-98b1-cdd6f1090611 | -4.53557 | -55.62405 | 2026-09-15 05:16:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 959827f9-5042-35c0-9c32-4946344b46ca | -3.38225 | -61.30734 | 2026-09-15 05:16:00 | NOAA-21 | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 1ba91d61-dd16-3611-8a9c-d5ac10e0fa3a | -4.54041 | -55.61633 | 2026-09-15 05:16:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| bb7db148-41a3-303a-a4b0-a7fd1b38b5eb | -3.08566 | -60.7102 | 2026-09-15 05:16:00 | NOAA-21 | IRANDUBA | AMAZONAS | Brasil | 1301852 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 6703b6fd-a8f9-3e6b-a7e3-4700e8effd6c | -3.17388 | -61.11342 | 2026-09-15 05:16:00 | NOAA-21 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 6b5d8350-bda1-35c7-9c52-e9630b02094e | -3.23158 | -50.58097 | 2026-09-15 05:16:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 10.7 |
| 6495f348-6387-3c74-8aee-1c8cbe42ab63 | -3.37948 | -50.77089 | 2026-09-15 05:16:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 5edad77e-7d1e-34d7-ad40-b5a9396607e3 | 1.32254 | -60.71749 | 2026-09-15 05:16:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 18863a42-0fdf-3047-9f32-ebf2d2f8732b | -3.07937 | -57.25656 | 2026-09-15 05:16:00 | NOAA-21 | BARREIRINHA | AMAZONAS | Brasil | 1300508 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 61c58844-05a9-3ac9-ab17-6fceaa72000b | -3.25771 | -54.51549 | 2026-09-15 05:16:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 6.5 |
| 769cf4ca-a8cc-3b4d-8915-bcefbc42a733 | -3.18155 | -61.11058 | 2026-09-15 05:16:00 | NOAA-21 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 4.8 |
| ea8539a3-e12a-3039-95c7-dcd692035568 | -3.91575 | -54.5175 | 2026-09-15 05:16:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 06773d5e-bef6-30c9-80cd-8319f70093d8 | -4.1858 | -48.68699 | 2026-09-15 05:16:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 6.5 |
| 7e7962ee-d1aa-3198-aa2d-e999afa5f366 | -3.06312 | -59.27975 | 2026-09-15 05:16:00 | NOAA-21 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 58e6507b-b07f-3126-b478-8309527816b3 | -3.43043 | -58.21363 | 2026-09-15 05:16:00 | NOAA-21 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| c196b9ac-0d2c-3ffa-9084-d9e233885e33 | -2.95515 | -50.40105 | 2026-09-15 05:16:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 29713602-3694-3048-8b98-6ab8d2fb2978 | -2.90111 | -50.42649 | 2026-09-15 05:16:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 9e0f71a9-91ab-3a41-bc26-af2d871dc2db | -3.078 | -50.56725 | 2026-09-15 05:16:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a142e56f-4603-34dd-80ec-01bb5c5a7730 | -3.45157 | -57.9913 | 2026-09-15 05:16:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 46eaa81e-0c5c-3002-8840-0115e21c8b1d | -3.48681 | -50.37885 | 2026-09-15 05:16:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 6.9 |
| e5c96072-fa73-3d12-a3b4-8d68bafa2826 | -3.54076 | -53.98999 | 2026-09-15 05:16:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 546d8a02-f9de-3bf1-9514-e16c0767ab17 | -2.90682 | -50.42176 | 2026-09-15 05:16:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 0d8a3682-48b9-3582-85ad-533207b048f0 | -2.98156 | -54.1594 | 2026-09-15 05:16:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 55ca2e63-f1ce-3bb8-9a9a-f89fe662585d | -3.18446 | -61.11509 | 2026-09-15 05:16:00 | NOAA-21 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 9a70834b-e807-3667-808d-60931e0b0d52 | -2.58176 | -49.44584 | 2026-09-15 05:16:00 | NOAA-21 | MOCAJUBA | PARÁ | Brasil | 1504604 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 8e43bba4-5a42-350e-939d-29adef104f56 | -3.54538 | -53.98571 | 2026-09-15 05:16:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 2b94df43-60bc-348e-ae8b-177797098cc3 | -3.64442 | -58.60976 | 2026-09-15 05:16:00 | NOAA-21 | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 29cdb7b5-952a-38e1-bbd4-6519f32d8b9d | -3.49674 | -50.38039 | 2026-09-15 05:16:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 626b9aea-146a-3fce-b69d-d05365a94272 | -4.36991 | -55.03258 | 2026-09-15 05:16:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 29305715-3b48-3205-8ef9-31c2181ce09b | -2.68561 | -57.49312 | 2026-09-15 05:16:00 | NOAA-21 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 3.3 |
| e220b3d1-d8f7-3a42-bea3-f540c7a714b7 | -5.41384 | -48.53558 | 2026-09-15 05:16:00 | NOAA-21 | ESPERANTINA | TOCANTINS | Brasil | 1707405 | 17 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 0e4f5b9a-5844-38a0-8156-7d7827d70059 | -4.52222 | -54.96829 | 2026-09-15 05:16:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| b5a1fdda-a7ac-3137-abdb-2d083648d7c9 | -3.17678 | -61.11793 | 2026-09-15 05:16:00 | NOAA-21 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| dc0bb0ec-791e-30d0-934c-11ff3105391c | -3.1669 | -58.64066 | 2026-09-15 05:16:00 | NOAA-21 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 97e97f27-7240-39d9-9031-5f9178e611f6 | -4.52593 | -54.9689 | 2026-09-15 05:16:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| cc6fe13c-da18-3c34-8a4e-b17783cb038f | -2.95023 | -50.40026 | 2026-09-15 05:16:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 34d7ca49-fc9f-3ea2-861f-ad46e17a04fb | -3.40111 | -50.75806 | 2026-09-15 05:16:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| c20ea05b-63ff-3b2c-a0e5-7b0cd6a137e3 | -2.91254 | -50.41702 | 2026-09-15 05:16:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| ed7ab5a7-8484-3d25-8867-1184351e0993 | -3.70914 | -52.09615 | 2026-09-15 05:16:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 96977306-8a93-39cf-89c3-c7b0e41184a6 | -3.86561 | -51.97651 | 2026-09-15 05:16:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a8560bd2-7d0c-3f2d-a04d-bd5298530ebb | -3.37951 | -50.7758 | 2026-09-15 05:16:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 87512716-7453-37dc-9622-b9d4d3efb0b7 | 2.70085 | -60.30082 | 2026-09-15 05:16:00 | NOAA-21 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 729399f2-4a7f-3dc3-8382-6fd1ec1f0fbb | -3.88304 | -51.91996 | 2026-09-15 05:16:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 0837df73-3c9e-3994-b1d2-c9a6078572bc | -3.86496 | -51.98094 | 2026-09-15 05:16:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 63871e63-2510-31e5-9bd9-5e1077282c72 | -3.16966 | -58.64461 | 2026-09-15 05:16:00 | NOAA-21 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 03b65213-c69a-3d4d-8e27-90802286f355 | -2.662 | -57.53575 | 2026-09-15 05:16:00 | NOAA-21 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 6d0d2dd9-fca7-3787-ab0e-53b3389300fd | -3.19028 | -61.12409 | 2026-09-15 05:16:00 | NOAA-21 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 3.6 |
| f88bf4c3-11e4-32d2-82b0-691fe8fd6818 | -3.11123 | -53.9544 | 2026-09-15 05:16:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| d0de1f01-38d0-33ff-aea0-98af377664b9 | -4.57268 | -54.91189 | 2026-09-15 05:16:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| bcb81076-9de8-38e4-840f-62c4877ff93d | -2.89094 | -50.41301 | 2026-09-15 05:16:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 99018648-69fb-303e-9bf0-d7b45f718f4b | -2.68507 | -57.49659 | 2026-09-15 05:16:00 | NOAA-21 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 246cf2ee-0280-3c67-b164-7f094998f8e3 | -2.90103 | -50.39261 | 2026-09-15 05:16:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| f20fc2c6-cd6f-31c0-b03c-d4c8dbba3765 | -3.35605 | -59.62411 | 2026-09-15 05:16:00 | NOAA-21 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 8c24bc54-fe6e-386c-8cb9-8acd316eded4 | -3.39143 | -50.7566 | 2026-09-15 05:16:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| b47580a7-9015-3302-8cb8-6452c94ef5ea | -3.61287 | -60.57375 | 2026-09-15 05:16:00 | NOAA-21 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| dbb0e6be-150d-3821-a9b9-6fa180450dec | -3.18966 | -61.12806 | 2026-09-15 05:16:00 | NOAA-21 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b28a4751-f7e8-3f1d-885b-b4d0621d4270 | -3.72266 | -57.20674 | 2026-09-15 05:16:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 4c9a28d4-fc71-339f-a175-b986d8a58e8e | -2.89009 | -50.41853 | 2026-09-15 05:16:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 6c382d94-c0fb-3532-8b9c-435d4bc5c2af | -2.91584 | -50.42873 | 2026-09-15 05:16:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 3f7dba0c-9907-3173-9683-574967f13de8 | -3.07766 | -61.07904 | 2026-09-15 05:16:00 | NOAA-21 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 1d72f2c3-0711-30a1-ab7d-8c33862f0182 | -3.48113 | -59.47767 | 2026-09-15 05:16:00 | NOAA-21 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| d4164fb1-f458-3ba5-82df-875d9314e807 | -2.69459 | -57.52296 | 2026-09-15 05:16:00 | NOAA-21 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 4.3 |
| b0dca318-8558-3b3c-9947-c1dbf98bb3b4 | -3.17573 | -58.64907 | 2026-09-15 05:16:00 | NOAA-21 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| a2456046-9f8a-3527-b4d7-f90b18b62140 | -5.19678 | -49.33512 | 2026-09-15 05:16:00 | NOAA-21 | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |


[Clique aqui para ver as próximas entradas](README54.md)
