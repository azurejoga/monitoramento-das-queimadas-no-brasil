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

## Dados Diários - Página 10

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| db1e6ab9-7e1b-3503-9536-33808b2815f0 | -11.0568 | -45.146 | 2025-09-01 02:30:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 99.4 |
| c1c9a0ae-791d-3729-8850-15b3046f5d22 | -7.0757 | -44.3606 | 2025-09-01 02:30:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 116.7 |
| baf906aa-f234-3f8e-8343-d94d6451c398 | -9.1337 | -65.844 | 2025-09-01 02:30:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 29.3 |
| 697fddd2-7cab-3d7c-b53b-39c0011dccfc | -12.9194 | -56.9672 | 2025-09-01 02:30:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 76.0 |
| c2abb55b-78a7-30a5-9fb5-341fdb930c78 | -15.6058 | -48.3402 | 2025-09-01 02:40:00 | GOES-19 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 74.8 |
| 64dc03e8-3bdb-3902-b1dd-815d15e42ed3 | -9.1337 | -65.844 | 2025-09-01 02:40:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 33.2 |
| 2b59d512-6a57-3bf1-807b-85950630d595 | -11.0381 | -45.1256 | 2025-09-01 02:40:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 118.1 |
| 8226889d-67be-379e-a2d4-6767416b192f | -10.0434 | -48.0998 | 2025-09-01 02:40:00 | GOES-19 | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 59.9 |
| e64f4f46-8b8f-3f3b-8314-bbcbb6fc85b7 | -7.0757 | -44.3606 | 2025-09-01 02:40:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 119.9 |
| 9b569d91-b91c-3df9-a6ef-71b6fa1ab3a0 | -15.7116 | -48.8809 | 2025-09-01 02:40:00 | GOES-19 | PIRENÓPOLIS | GOIÁS | Brasil | 5217302 | 52 | 33 | nan | nan | nan | Cerrado | 60.7 |
| e3365753-cb95-3809-92e0-59b9c4d89e60 | -13.1644 | -45.2897 | 2025-09-01 02:40:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 71.7 |
| 6eb93a3e-b586-3aed-bb35-9b7bf501b9f4 | -7.0948 | -44.3358 | 2025-09-01 02:40:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 160.8 |
| f3465095-4486-3f33-9245-152bc05d4b6e | -13.1837 | -45.2865 | 2025-09-01 02:40:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 63.8 |
| 9cd7d216-1ff8-3533-bbaa-e903ac05ca8d | -9.135 | -65.5453 | 2025-09-01 02:40:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 76.4 |
| 858ec7e9-5d56-38a9-bebe-20c35cab2870 | -7.076 | -44.3376 | 2025-09-01 02:40:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 135.6 |
| 1f50eba7-77dd-38cd-944f-d14662bcccef | -12.5722 | -48.2059 | 2025-09-01 02:40:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 51.0 |
| 4844e1d6-d61f-355d-878c-1ec4ab43f0e4 | -11.0568 | -45.146 | 2025-09-01 02:40:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 147.7 |
| e72b43f5-db4b-3e95-a342-c34fc67b91cf | -11.0572 | -45.123 | 2025-09-01 02:40:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 78.3 |
| 70faddb4-ccea-3f83-812c-879cc65ff469 | -6.4605 | -43.9532 | 2025-09-01 02:40:00 | GOES-19 | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 88.3 |
| ac123254-1c37-392a-b237-68f3682f11ff | -11.0377 | -45.1487 | 2025-09-01 02:40:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 228.8 |
| 0e941fd9-4419-310f-9d9f-b8d4f6ff6bf7 | -8.7684 | -61.4261 | 2025-09-01 02:40:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 61.0 |
| bbf67183-a82d-3648-978f-f3a66e9bc8d2 | -10.2488 | -51.1128 | 2025-09-01 02:40:00 | GOES-19 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Cerrado | 45.9 |
| c26d4c4d-01bc-3615-a0ce-3a62f00ba337 | -10.5937 | -44.331 | 2025-09-01 02:40:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 71.1 |
| 717061ed-9485-3478-8615-662cd26cca7f | -6.8095 | -52.8154 | 2025-09-01 02:40:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 54.6 |
| 493bfd1b-5aa9-3173-af81-0e18c230d736 | -10.23 | -51.1147 | 2025-09-01 02:40:00 | GOES-19 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Cerrado | 55.5 |
| da5ea14b-da02-3474-91ac-ff502d082722 | -7.0946 | -44.3589 | 2025-09-01 02:40:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 141.6 |
| 339ba241-9bc9-3cf2-9167-9b1a4fd43225 | -15.7112 | -48.9032 | 2025-09-01 02:40:00 | GOES-19 | PIRENÓPOLIS | GOIÁS | Brasil | 5217302 | 52 | 33 | nan | nan | nan | Cerrado | 91.0 |
| 566389d5-0824-32d9-9f0d-d0d0463711d7 | -9.1165 | -65.5459 | 2025-09-01 02:40:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 37.8 |
| 8117bccc-1d1a-392e-9ce1-53ffef51f6f0 | -10.6128 | -44.3284 | 2025-09-01 02:40:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 121.2 |
| 59270f6d-ab07-3794-a843-9b82d7b7d118 | -6.8466 | -52.8132 | 2025-09-01 02:40:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 74.4 |
| e5a99bf9-073d-3184-b11d-492534eadd63 | -18.6704 | -52.5973 | 2025-09-01 02:40:00 | GOES-19 | CHAPADÃO DO CÉU | GOIÁS | Brasil | 5205471 | 52 | 33 | nan | nan | nan | Cerrado | 49.9 |
| 6973ca75-ed4d-3817-a875-0ad973af91e5 | -6.8281 | -52.8143 | 2025-09-01 02:40:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 84.5 |
| 3316cc07-5263-3daa-a83b-a4665323c273 | -9.68 | -47.0353 | 2025-09-01 02:40:00 | GOES-19 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 52.1 |
| 3389fb4b-dc3d-347a-ac08-7e8cff4c94fd | -15.5862 | -48.3435 | 2025-09-01 02:40:00 | GOES-19 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 76.8 |
| a62b77c5-3211-3e89-98f4-8e2f6596fa05 | -10.6131 | -44.3051 | 2025-09-01 02:40:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 61.9 |
| 5527cafc-a107-3c43-b318-cb9122b56e09 | -15.5862 | -48.3435 | 2025-09-01 02:50:00 | GOES-19 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 75.0 |
| 9eb6a5a0-ac0c-3a9a-b8d3-7b6eee06e732 | -13.1644 | -45.2897 | 2025-09-01 02:50:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 92.5 |
| b3f0df3f-5a40-3e43-b0fb-4ac9453575a3 | -10.2488 | -51.1128 | 2025-09-01 02:50:00 | GOES-19 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Cerrado | 64.7 |
| fb56031a-67a9-3f7b-b0fc-4208c8e81506 | -13.1648 | -45.2665 | 2025-09-01 02:50:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 65.8 |
| 54f1591c-0c90-365d-811d-8ae43be59d77 | -7.0946 | -44.3589 | 2025-09-01 02:50:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 109.4 |
| 164c24f5-5438-3c39-8d88-dc007542d870 | -11.0377 | -45.1487 | 2025-09-01 02:50:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 279.5 |
| 2db6dd2f-f713-3d31-baf1-5504674fa864 | -12.9197 | -56.9471 | 2025-09-01 02:50:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 123.2 |
| 9a2e237d-deae-362c-b434-2891b463cd32 | -9.6607 | -47.0597 | 2025-09-01 02:50:00 | GOES-19 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 73.1 |
| 00905178-2976-36ba-8e9f-b123dc919c88 | -11.0381 | -45.1256 | 2025-09-01 02:50:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 185.0 |
| cbd8c566-d42f-373d-9b6a-7120ce3164bd | -12.9006 | -56.9488 | 2025-09-01 02:50:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 43.6 |
| 70e71eaf-64a7-34ad-9d0b-c18435aaf578 | -10.6128 | -44.3284 | 2025-09-01 02:50:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 91.6 |
| 2eab6484-dcfb-32d9-a955-816c605ee661 | -7.0948 | -44.3358 | 2025-09-01 02:50:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 140.8 |
| 74d44a01-61d0-3cb6-86a8-bc71588df9ea | -12.9387 | -56.9454 | 2025-09-01 02:50:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 86.3 |
| d711e447-cfe6-3512-8528-d2c902065118 | -6.8281 | -52.8143 | 2025-09-01 02:50:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 79.0 |
| 2e9de8f4-5082-3793-be0f-e389750d8df4 | -9.135 | -65.5453 | 2025-09-01 02:50:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 58.4 |
| 18225197-9e14-35f9-a7ea-5c1ff4c3776e | -9.68 | -47.0353 | 2025-09-01 02:50:00 | GOES-19 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 102.1 |
| 2c79d4d5-401b-38a0-9e91-efca61863f52 | -9.1337 | -65.844 | 2025-09-01 02:50:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 30.2 |
| d4c7c675-bfbc-3601-a738-eafa78ed2729 | -7.076 | -44.3376 | 2025-09-01 02:50:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 171.4 |
| 36124a77-5650-310b-8089-452a008360d6 | -10.5937 | -44.331 | 2025-09-01 02:50:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 96.0 |
| 7b6b2955-104c-30b9-af6e-b6b174a8e288 | -8.6468 | -67.2515 | 2025-09-01 02:50:00 | GOES-19 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 37.2 |
| 42afa7db-1fed-3e83-b2ef-9f0f4ec123e2 | -6.8466 | -52.8132 | 2025-09-01 02:50:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 63.0 |
| 7aec3e87-ae0e-3743-a612-f6d26d892661 | -15.7289 | -48.9892 | 2025-09-01 02:50:00 | GOES-19 | PIRENÓPOLIS | GOIÁS | Brasil | 5217302 | 52 | 33 | nan | nan | nan | Cerrado | 69.7 |
| 78879d8c-bc62-37f5-a4c8-b24eaa594f08 | -11.0568 | -45.146 | 2025-09-01 02:50:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 72.2 |
| 457a1be7-6438-3b99-a4fc-7f3946acb33b | -12.9194 | -56.9672 | 2025-09-01 02:50:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 93.9 |
| 82715121-a9d5-30d4-bbc0-44920d0286e4 | -15.6058 | -48.3402 | 2025-09-01 02:50:00 | GOES-19 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 78.3 |
| 77b36050-3bec-3572-87df-925e7c4ac6ef | -15.7112 | -48.9032 | 2025-09-01 02:50:00 | GOES-19 | PIRENÓPOLIS | GOIÁS | Brasil | 5217302 | 52 | 33 | nan | nan | nan | Cerrado | 65.4 |
| 109634ac-2a58-3a72-b684-42b2b0ccb159 | -9.1165 | -65.5459 | 2025-09-01 02:50:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 39.5 |
| a2cd4fb5-9386-3b29-9b8d-24ea7ac97310 | -7.0757 | -44.3606 | 2025-09-01 02:50:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 133.2 |
| 2a9e2644-6a3e-3333-8aa4-25a339cd84d8 | -9.6797 | -47.0576 | 2025-09-01 02:50:00 | GOES-19 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 99.8 |
| 3e49a9d8-19be-3725-8690-dc4c6cab7bf3 | -6.4605 | -43.9532 | 2025-09-01 02:50:00 | GOES-19 | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 65.9 |
| d7a583e5-bafd-3a30-8b32-05d25dd7b21a | -9.661 | -47.0374 | 2025-09-01 02:50:00 | GOES-19 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 68.0 |
| eeb32ea0-500c-3348-806c-2bced3cae68f | -15.6916 | -48.9065 | 2025-09-01 02:50:00 | GOES-19 | PIRENÓPOLIS | GOIÁS | Brasil | 5217302 | 52 | 33 | nan | nan | nan | Cerrado | 56.8 |
| 13b45c8e-c2bd-3108-9033-c86044e74262 | -12.9385 | -56.9655 | 2025-09-01 02:50:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 67.3 |
| 127b2069-b2d8-3718-bf47-570f34600c82 | -10.0434 | -48.0998 | 2025-09-01 03:00:00 | GOES-19 | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 57.6 |
| 84170a9c-e89e-353c-bcd9-c4f2291e160c | -9.694 | -65.0958 | 2025-09-01 03:00:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 56.0 |
| 7fd71c11-e439-3212-80fe-ffdb96370f1e | -7.0948 | -44.3358 | 2025-09-01 03:00:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 155.5 |
| cddc61df-a084-32e8-a56f-591bd7ccb69c | -12.9385 | -56.9655 | 2025-09-01 03:00:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 64.4 |
| 9e11a29e-3909-331d-aa86-4f582ff7874b | -9.1165 | -65.5459 | 2025-09-01 03:00:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 33.6 |
| 30a29648-6554-306d-84e0-48c5100adc90 | -7.0946 | -44.3589 | 2025-09-01 03:00:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 109.0 |
| 0ca2da13-a003-34cf-b7d1-9fb190d5a8b4 | -7.076 | -44.3376 | 2025-09-01 03:00:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 156.3 |
| 1cb2b45d-6d19-31be-8e53-0e12a0f11cad | -11.0568 | -45.146 | 2025-09-01 03:00:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 112.9 |
| 3a7de09f-cc32-332d-b508-3db48ced967d | -12.9194 | -56.9672 | 2025-09-01 03:00:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 135.9 |
| b4ee1601-19ce-3e17-99af-d5431a965d1b | -10.23 | -51.1147 | 2025-09-01 03:00:00 | GOES-19 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Cerrado | 45.9 |
| 14a9bc8b-d039-3407-b402-5f22190a8664 | -10.6128 | -44.3284 | 2025-09-01 03:00:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 110.5 |
| 12d50463-5f36-3420-a1fa-b555cfb3157a | -15.7289 | -48.9892 | 2025-09-01 03:00:00 | GOES-19 | PIRENÓPOLIS | GOIÁS | Brasil | 5217302 | 52 | 33 | nan | nan | nan | Cerrado | 67.5 |
| 65fc3b15-e193-3d93-a9f3-ea1a6112c419 | -11.0572 | -45.123 | 2025-09-01 03:00:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 82.4 |
| 64e86ec0-e2b5-39e8-b5b6-c7b74e96242a | -13.1644 | -45.2897 | 2025-09-01 03:00:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 72.6 |
| 675f720f-c9d1-36ba-99fb-bee0f0c775fc | -7.0757 | -44.3606 | 2025-09-01 03:00:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 107.3 |
| 16b0055b-fdbc-3869-a20c-0aedd000750b | -10.5937 | -44.331 | 2025-09-01 03:00:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 101.4 |
| 167a4438-53f6-3ef6-b237-76c4cd8b0df2 | -12.9006 | -56.9488 | 2025-09-01 03:00:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 56.1 |
| 39bc9205-6659-3ebb-9698-8174e9069dea | -8.7684 | -61.4261 | 2025-09-01 03:00:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 47.7 |
| 9182e44c-6867-3da9-84a0-3e5c2bb13613 | -6.8466 | -52.8132 | 2025-09-01 03:00:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 63.0 |
| f5a39a6c-9bec-3c84-8b00-13a4b7a46852 | -15.7112 | -48.9032 | 2025-09-01 03:00:00 | GOES-19 | PIRENÓPOLIS | GOIÁS | Brasil | 5217302 | 52 | 33 | nan | nan | nan | Cerrado | 74.7 |
| f026b1fc-fae4-34a5-b825-9b99b634637a | -11.0377 | -45.1487 | 2025-09-01 03:00:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 270.6 |
| b0962fae-9527-3388-8835-a827755bd340 | -12.9387 | -56.9454 | 2025-09-01 03:00:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 97.4 |
| d475ae3f-21fc-39c0-a4f8-0b5630c2f94a | -6.8281 | -52.8143 | 2025-09-01 03:00:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 72.8 |
| 60111659-bc3b-3b10-8dd0-5b1a7dfe8530 | -10.6131 | -44.3051 | 2025-09-01 03:00:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 59.2 |
| 7d574632-9562-3154-8f00-330379ad5d63 | -15.7116 | -48.8809 | 2025-09-01 03:00:00 | GOES-19 | PIRENÓPOLIS | GOIÁS | Brasil | 5217302 | 52 | 33 | nan | nan | nan | Cerrado | 56.8 |
| b0e9c93e-955d-3ae2-b489-38b1702dba97 | -9.6939 | -65.1145 | 2025-09-01 03:00:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 46.3 |
| d664d5a4-1e21-350b-9925-adea9898c010 | -11.0381 | -45.1256 | 2025-09-01 03:00:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 190.6 |
| ef837409-1fa1-345a-9ecf-2e825ce34e7a | -10.2488 | -51.1128 | 2025-09-01 03:00:00 | GOES-19 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Cerrado | 61.7 |
| 620c3c21-ab76-3916-a378-45cf58195b5e | -9.135 | -65.5453 | 2025-09-01 03:00:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 70.2 |
| 86cba672-d140-35d7-8458-54f95369f9df | -13.1837 | -45.2865 | 2025-09-01 03:00:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 56.3 |
| 2c89c4ce-fc5b-3009-ba4e-0e89ae36f993 | -15.6058 | -48.3402 | 2025-09-01 03:00:00 | GOES-19 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 78.5 |
| 51237baa-21dd-3909-a1cd-26abd1787bc9 | -12.9197 | -56.9471 | 2025-09-01 03:00:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 201.2 |


[Clique aqui para ver as próximas entradas](README11.md)
