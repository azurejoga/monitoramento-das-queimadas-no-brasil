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

## Dados Diários - Página 85

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 26d486ab-7b6e-3adf-bda9-c51293818782 | -13.82632 | -44.59508 | 2024-10-09 04:17:00 | NOAA-21 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 6a250644-4901-3f71-a273-bcb5713648d3 | -13.82577 | -44.59861 | 2024-10-09 04:17:00 | NOAA-21 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| fe6d46cd-95f5-3ead-9641-06a32933a327 | -13.81146 | -44.60352 | 2024-10-09 04:17:00 | NOAA-21 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| e41b199e-6320-305d-a3ee-9b8203b7f637 | -13.8792 | -44.52012 | 2024-10-09 04:17:00 | NOAA-21 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| fe48a696-0a94-3080-a2cc-826d0d67526e | -13.87865 | -44.52366 | 2024-10-09 04:17:00 | NOAA-21 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| d09b20c8-6949-3e02-a92d-5167e6dbd3e9 | -13.87315 | -44.53725 | 2024-10-09 04:17:00 | NOAA-21 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 6fadf217-b80f-3b0c-a1e6-b711890598f1 | -13.8704 | -44.53318 | 2024-10-09 04:17:00 | NOAA-21 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| f14472ed-51de-3763-bf49-6c2991c59903 | -13.8671 | -44.55437 | 2024-10-09 04:17:00 | NOAA-21 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 5dc3941c-9bd1-387f-ad23-4e61349bc799 | -13.86599 | -44.5397 | 2024-10-09 04:17:00 | NOAA-21 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 2478be38-ad7d-36e0-a147-b8fdca8eb389 | -13.86434 | -44.5503 | 2024-10-09 04:17:00 | NOAA-21 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| a8cd4bf8-6b7a-36d0-88b8-a8b6fb40fab5 | -13.86159 | -44.54623 | 2024-10-09 04:17:00 | NOAA-21 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| ed66de1e-086c-3d35-8441-077053019c06 | -13.85774 | -44.54922 | 2024-10-09 04:17:00 | NOAA-21 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 7a9a33aa-5a3e-347d-b5f9-ea2c5820daa9 | -13.91112 | -44.51083 | 2024-10-09 04:17:00 | NOAA-21 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 20.7 |
| edb23918-80f2-37d3-a356-d092565f0055 | -13.83679 | -44.57144 | 2024-10-09 04:17:00 | NOAA-21 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 5.2 |
| e5986c71-626f-3bef-90f7-7055e3376144 | -13.83403 | -44.58909 | 2024-10-09 04:17:00 | NOAA-21 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 3.8 |
| e0844a28-3311-3ce5-bcab-710b96cbca87 | -13.83073 | -44.58855 | 2024-10-09 04:17:00 | NOAA-21 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 37.4 |
| 5f426d3b-5488-34ae-9aaa-4b53948588ff | -13.82743 | -44.58801 | 2024-10-09 04:17:00 | NOAA-21 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 37.4 |
| bc381408-dff5-3c8d-a47e-1f9e041e32f9 | -13.82413 | -44.58747 | 2024-10-09 04:17:00 | NOAA-21 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 958e213b-65fc-3143-ab56-52b848d5a07f | -13.82302 | -44.59454 | 2024-10-09 04:17:00 | NOAA-21 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 4f5a5a6d-94b7-39f3-a1eb-71f7bc380bb0 | -13.81751 | -44.60812 | 2024-10-09 04:17:00 | NOAA-21 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 8.0 |
| 32f4096f-7621-3c63-8b98-8626a7a11ba4 | -13.81642 | -44.59346 | 2024-10-09 04:17:00 | NOAA-21 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 796c43b4-33c0-3d37-a39d-f9c45e8d4972 | -13.81587 | -44.59699 | 2024-10-09 04:17:00 | NOAA-21 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 14.7 |
| e48c77d7-3f4e-3fea-bafe-e62e6e7c202f | -13.81532 | -44.60052 | 2024-10-09 04:17:00 | NOAA-21 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 14.7 |
| d5db27e1-3fa3-3c23-a86d-dc46acf714eb | -13.81257 | -44.59645 | 2024-10-09 04:17:00 | NOAA-21 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 14.7 |
| 1c430fb8-8fc5-3e22-a599-351230d17d6c | -13.92157 | -44.57413 | 2024-10-09 04:17:00 | NOAA-21 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 10.3 |
| 623e08eb-892c-3eff-9fbc-1d89837fa3e1 | -13.92103 | -44.51244 | 2024-10-09 04:17:00 | NOAA-21 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 2.9 |
| f05b7b95-ed3e-3522-8379-ae465e9ee8c7 | -13.92048 | -44.51597 | 2024-10-09 04:17:00 | NOAA-21 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 3d7e00da-7a94-33b8-9e7e-d28d19e2aca4 | -13.91993 | -44.51951 | 2024-10-09 04:17:00 | NOAA-21 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 4193310e-d362-3d7d-88fe-e4bb5351f38e | -13.91938 | -44.52304 | 2024-10-09 04:17:00 | NOAA-21 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 814fe5d1-beae-32be-8d0f-abdcb62b669f | -13.91828 | -44.50837 | 2024-10-09 04:17:00 | NOAA-21 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| fb96942e-6ec1-3ac4-ac59-80c6186ba6c1 | -13.91773 | -44.5119 | 2024-10-09 04:17:00 | NOAA-21 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 8ce5b04b-462b-36f2-88d8-c6604aa5d11a | -13.91718 | -44.51544 | 2024-10-09 04:17:00 | NOAA-21 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 41598878-2b4d-389a-a176-5096f1ac2cb6 | -13.91663 | -44.51897 | 2024-10-09 04:17:00 | NOAA-21 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 1ca048cd-ec30-34de-a1f7-7d022aae7f29 | -13.91608 | -44.52251 | 2024-10-09 04:17:00 | NOAA-21 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| b54b068c-2b18-3f26-9649-2905b457e936 | -13.91553 | -44.52604 | 2024-10-09 04:17:00 | NOAA-21 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 9.0 |
| 44736408-a39c-3f21-a68a-8c1143c01ad0 | -13.91498 | -44.52958 | 2024-10-09 04:17:00 | NOAA-21 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 9.0 |
| fc235749-5f43-3864-bfe5-25a20a612c0a | -13.91498 | -44.50783 | 2024-10-09 04:17:00 | NOAA-21 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 3ae45a06-7dcf-3bab-8c7a-3ead8d4dbb50 | -13.91443 | -44.51136 | 2024-10-09 04:17:00 | NOAA-21 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 9c46d393-8676-37b1-9cd0-ff5a8c37d4f8 | -13.91387 | -44.5149 | 2024-10-09 04:17:00 | NOAA-21 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| fb1e451e-45f5-337d-9098-207cd86c094f | -13.91333 | -44.51844 | 2024-10-09 04:17:00 | NOAA-21 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| fa14f7b2-287d-3d39-88dc-c39c4d9ac52d | -13.91277 | -44.52197 | 2024-10-09 04:17:00 | NOAA-21 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| c5853840-667c-3cab-ace1-0f9cccf40476 | -13.91222 | -44.52551 | 2024-10-09 04:17:00 | NOAA-21 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 9.0 |
| 1c963b86-96e5-3269-bcbd-5171c5e5625c | -13.91222 | -44.50375 | 2024-10-09 04:17:00 | NOAA-21 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 944b66ea-6b74-3bc3-90ea-f76da7899f04 | -13.91167 | -44.52904 | 2024-10-09 04:17:00 | NOAA-21 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 9.0 |
| 52e515fc-a447-3dda-84ce-69c0894d4796 | -13.91167 | -44.50729 | 2024-10-09 04:17:00 | NOAA-21 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 3a0d4599-3b19-3f4d-b92e-57b2fc37fb54 | -13.91112 | -44.53258 | 2024-10-09 04:17:00 | NOAA-21 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| c602571d-e65d-32db-9a2c-053c3e350d23 | -14.14991 | -44.94165 | 2024-10-09 04:17:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 69466201-46cc-3258-a66a-24173e0d18f0 | -14.08426 | -44.53579 | 2024-10-09 04:17:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 5b26de7a-4441-3c76-bf33-6ec75aaca1f1 | -13.91057 | -44.51437 | 2024-10-09 04:17:00 | NOAA-21 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 20.7 |
| 921dca85-bb15-3898-948f-c91498c34570 | -13.91002 | -44.5179 | 2024-10-09 04:17:00 | NOAA-21 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 8d2ab510-7375-3fc8-8b52-9bd097518eea | -13.91 | -44.6266 | 2024-10-09 04:17:00 | NOAA-21 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 4c78a16c-03a9-381b-83e5-2e9050661011 | -13.90947 | -44.52143 | 2024-10-09 04:17:00 | NOAA-21 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 26107420-06c4-33cf-a3d6-2b0353c88c56 | -13.90892 | -44.52497 | 2024-10-09 04:17:00 | NOAA-21 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 5da1b360-80cd-3af4-8a7b-5296f5885183 | -13.90892 | -44.50322 | 2024-10-09 04:17:00 | NOAA-21 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 1b96888c-8971-3b83-98f7-051614471611 | -13.90837 | -44.57198 | 2024-10-09 04:17:00 | NOAA-21 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 0901f2dc-b7cb-3609-bde0-7f6909fdebc8 | -13.90837 | -44.52851 | 2024-10-09 04:17:00 | NOAA-21 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 73e69e12-3c94-3d9e-8301-9cfb4b144caa | -13.90837 | -44.50675 | 2024-10-09 04:17:00 | NOAA-21 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 7575bc5d-2aab-3b86-9ebb-7d148bf92338 | -13.90782 | -44.53204 | 2024-10-09 04:17:00 | NOAA-21 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| f20df30f-d602-35a6-84c8-3eec6efef422 | -13.90782 | -44.51029 | 2024-10-09 04:17:00 | NOAA-21 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 20.7 |
| a4a5e944-6bd2-30af-868d-53e7059d1c37 | -13.90781 | -44.57552 | 2024-10-09 04:17:00 | NOAA-21 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 9b7989f8-7129-36d6-aa33-442974b2951d | -13.90727 | -44.53558 | 2024-10-09 04:17:00 | NOAA-21 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 1557b70b-174b-31f2-9bf1-251b1edaa79e | -13.90727 | -44.51383 | 2024-10-09 04:17:00 | NOAA-21 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 20.7 |
| 8102a829-44ce-3624-9570-d0abd1052a9d | -13.90672 | -44.51736 | 2024-10-09 04:17:00 | NOAA-21 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 96be63f6-e304-30e8-97f0-41722a5ed99c | -13.90617 | -44.52089 | 2024-10-09 04:17:00 | NOAA-21 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 6caf012c-8741-3347-9551-38827137674f | -13.90562 | -44.52443 | 2024-10-09 04:17:00 | NOAA-21 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 5910fb67-7a8c-3312-9c38-2e4fb0af3457 | -13.90507 | -44.52797 | 2024-10-09 04:17:00 | NOAA-21 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| a0b7ce31-e896-353e-b1c9-43ac9fb26054 | -13.90506 | -44.57145 | 2024-10-09 04:17:00 | NOAA-21 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 3.3 |
| aa6bbe4e-dc09-391a-9073-786f181e313d | -13.90452 | -44.50975 | 2024-10-09 04:17:00 | NOAA-21 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 2f7c09ac-23f1-3e92-be05-e9e99582999e | -13.90397 | -44.51329 | 2024-10-09 04:17:00 | NOAA-21 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| e36a3dcf-f65f-3699-b468-dd2a84f03304 | -13.90342 | -44.51682 | 2024-10-09 04:17:00 | NOAA-21 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 13.4 |
| f23f1ba6-ff11-3db6-929c-47f2fcc26ef5 | -13.90287 | -44.52036 | 2024-10-09 04:17:00 | NOAA-21 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 13.4 |
| 5539efe7-5362-3b8f-b404-73a17807b168 | -13.90232 | -44.5239 | 2024-10-09 04:17:00 | NOAA-21 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 815e9845-0003-3267-8032-03560971a400 | -13.90122 | -44.53097 | 2024-10-09 04:17:00 | NOAA-21 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 2dd12354-8be7-3d55-b92d-c7d8371ea5c2 | -13.90121 | -44.50922 | 2024-10-09 04:17:00 | NOAA-21 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 027d5fca-3535-3267-8f14-58e9eaf4a962 | -13.90067 | -44.51275 | 2024-10-09 04:17:00 | NOAA-21 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| d00b59bf-4e9b-30d5-be0c-dbc6bf6601a9 | -13.90066 | -44.57798 | 2024-10-09 04:17:00 | NOAA-21 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 1eb52b4a-f81b-3d99-b958-996ff97374fc | -14.87122 | -45.13722 | 2024-10-09 04:17:00 | NOAA-21 | BONITO DE MINAS | MINAS GERAIS | Brasil | 3108255 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| a6614d1f-0c2b-31d1-b9ce-a63848c236ba | -14.86792 | -45.13667 | 2024-10-09 04:17:00 | NOAA-21 | BONITO DE MINAS | MINAS GERAIS | Brasil | 3108255 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| cb5163c1-fe90-3660-b0f8-f116e2de8b4e | -14.86736 | -45.14022 | 2024-10-09 04:17:00 | NOAA-21 | BONITO DE MINAS | MINAS GERAIS | Brasil | 3108255 | 31 | 33 | nan | nan | nan | Cerrado | 0.4 |
| a2f786d6-67aa-321d-958e-4bd551328bcb | -14.48708 | -44.96106 | 2024-10-09 04:17:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| f15e357d-cf95-301a-9c69-f5465b4a5ba6 | -14.15316 | -44.94226 | 2024-10-09 04:17:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 4.4 |
| d28e7dde-4163-35b2-be28-6c12f170968e | -14.06677 | -44.47079 | 2024-10-09 04:17:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 568b6ad4-ac70-3eb3-bb75-891ad50ece1a | -13.92763 | -44.53526 | 2024-10-09 04:17:00 | NOAA-21 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 4.9 |
| e7792d94-7f6b-393f-8758-2c81ada75f9c | -14.06622 | -44.47433 | 2024-10-09 04:17:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 5.9 |
| f5c2adff-56c6-3d45-8f35-93f38aabe11b | -14.06347 | -44.47025 | 2024-10-09 04:17:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 4b8b7c4a-1cc6-3080-a7e9-cdbcfb803b05 | -14.06292 | -44.47379 | 2024-10-09 04:17:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 48d2ba17-1748-3b94-8220-9bdab02e982c | -14.06017 | -44.4697 | 2024-10-09 04:17:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 95587c4e-878a-3b7f-8bbb-6f6ee5a8a578 | -13.9447 | -44.53442 | 2024-10-09 04:17:00 | NOAA-21 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 31b13f4c-5f42-3787-badd-de95c2a733b0 | -13.94415 | -44.53795 | 2024-10-09 04:17:00 | NOAA-21 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| fbacca09-681f-3dca-833a-d4737f6f6291 | -13.94359 | -44.54149 | 2024-10-09 04:17:00 | NOAA-21 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| ef38cfe8-e4fe-31a4-b1cb-28e81ed65e9d | -13.9425 | -44.52681 | 2024-10-09 04:17:00 | NOAA-21 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 3b17ec66-2197-3b61-9d75-1c5b5e75070d | -13.94195 | -44.53035 | 2024-10-09 04:17:00 | NOAA-21 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 1f0d0c2d-4384-3bcf-a9ac-13a8ba4d112d | -13.94139 | -44.53388 | 2024-10-09 04:17:00 | NOAA-21 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| f1624fdf-6b27-3038-a41d-ba9be2afcf66 | -13.94084 | -44.53741 | 2024-10-09 04:17:00 | NOAA-21 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 2c816b00-d7de-3294-afbb-a19e1f1ba697 | -13.93974 | -44.54449 | 2024-10-09 04:17:00 | NOAA-21 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 31.8 |
| 225710b5-3dda-331c-b43f-3f9372539b5f | -13.93919 | -44.54802 | 2024-10-09 04:17:00 | NOAA-21 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 31.8 |
| 3c40fdbf-44ac-3cd0-930f-a885d8f8648f | -13.93919 | -44.52627 | 2024-10-09 04:17:00 | NOAA-21 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| ccc6d44b-bb0e-3c2e-adf1-661aaf28df8f | -13.93754 | -44.53688 | 2024-10-09 04:17:00 | NOAA-21 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 6fa0f9bc-2ccb-31ab-ac85-40df5c22e8b6 | -13.93644 | -44.54395 | 2024-10-09 04:17:00 | NOAA-21 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 31.8 |
| c8ffa06a-8a27-3e25-b6ff-b51343a81f15 | -13.93589 | -44.54749 | 2024-10-09 04:17:00 | NOAA-21 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 31.8 |


[Clique aqui para ver as próximas entradas](README86.md)
