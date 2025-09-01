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

## Dados Diários - Página 8

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 01f1d2f0-d17b-3e0a-8e28-5c9e6a44af6f | -6.4417 | -43.9548 | 2025-09-01 01:50:00 | GOES-19 | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 92.2 |
| 98130e67-61b3-30c9-8187-250596404e4a | -11.0568 | -45.146 | 2025-09-01 01:50:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 72.5 |
| 4821edc1-7033-39f9-9644-458a992c4935 | -6.7438 | -43.7898 | 2025-09-01 01:50:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 122.0 |
| 8682355c-9ff9-368f-b451-7a2df931aba6 | -6.4793 | -43.9516 | 2025-09-01 01:50:00 | GOES-19 | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 120.1 |
| 7d2d2dc2-7838-32f5-b423-876a4ec9f5ed | -9.1337 | -65.844 | 2025-09-01 01:50:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 45.0 |
| c982cb0c-d52d-38b8-b9f0-989fc703e9e5 | -7.2929 | -60.667 | 2025-09-01 01:50:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 44.4 |
| 2f016ff5-edc2-3d6d-b930-a4a1aec1ec7c | -13.1842 | -45.2633 | 2025-09-01 01:50:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 65.0 |
| 9ef93c06-e721-327e-9796-ac0e105499d8 | -12.9385 | -56.9655 | 2025-09-01 01:50:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 68.4 |
| 12220849-6388-3a2c-b712-4c82293d73c6 | -8.7684 | -61.4261 | 2025-09-01 01:50:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 66.4 |
| 50650d35-7d6f-3fd0-b697-7bed44f9b5bc | -6.4602 | -43.9764 | 2025-09-01 01:50:00 | GOES-19 | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 210.6 |
| b868f524-9b60-38f9-8e66-f336add68591 | -12.9387 | -56.9454 | 2025-09-01 01:50:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 102.5 |
| 99dd6c54-25f4-3934-aea4-cd70e90ed3a2 | -7.9335 | -73.0052 | 2025-09-01 01:50:00 | GOES-19 | RODRIGUES ALVES | ACRE | Brasil | 1200427 | 12 | 33 | nan | nan | nan | Amazônia | 46.7 |
| 38de09cc-efb5-3b9a-ad97-13e2f114bda4 | -13.1837 | -45.2865 | 2025-09-01 01:50:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 79.2 |
| f6a8abc6-6783-3353-87e2-4599cc31439b | -6.7626 | -43.7881 | 2025-09-01 01:50:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 71.1 |
| 023ef43e-5050-305d-bde2-a1b01a15298c | -9.135 | -65.5453 | 2025-09-01 01:50:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 74.2 |
| bf665a09-8cee-352c-9be9-186b208ad6c1 | -11.0377 | -45.1487 | 2025-09-01 01:50:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 102.3 |
| 19082490-191e-3545-9b62-5a38691d3f15 | -12.9194 | -56.9672 | 2025-09-01 01:50:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 159.5 |
| ced14e97-2e52-33de-a337-818bd529a559 | -7.6783 | -61.0908 | 2025-09-01 01:50:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 50.5 |
| a4000cde-8ecb-3abc-b1b6-422f8a550809 | -8.7683 | -61.4452 | 2025-09-01 01:50:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 39.4 |
| c3fa1162-1df3-38f5-b93b-01f433ae0421 | -15.5867 | -48.321 | 2025-09-01 01:50:00 | GOES-19 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 79.1 |
| 31958458-d887-3d6e-b6c7-eac871015720 | -15.7112 | -48.9032 | 2025-09-01 01:50:00 | GOES-19 | PIRENÓPOLIS | GOIÁS | Brasil | 5217302 | 52 | 33 | nan | nan | nan | Cerrado | 79.4 |
| df1ff8c9-1e25-39c3-a573-4f75a6496030 | -15.5862 | -48.3435 | 2025-09-01 01:50:00 | GOES-19 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 205.5 |
| 6feae096-157a-370e-8b56-ddbe7d04231a | -7.9335 | -72.987 | 2025-09-01 01:50:00 | GOES-19 | RODRIGUES ALVES | ACRE | Brasil | 1200427 | 12 | 33 | nan | nan | nan | Amazônia | 46.0 |
| 7547f429-a60f-3c17-887a-c32d313aa0c3 | -13.1644 | -45.2897 | 2025-09-01 01:50:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 78.1 |
| d01dcdf9-d59f-387c-bdea-ec7eeb879f8f | -10.6128 | -44.3284 | 2025-09-01 01:50:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 94.1 |
| fc8b0ea8-5fbd-3303-97c6-b864a03dad87 | -7.0757 | -44.3606 | 2025-09-01 01:50:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 118.6 |
| 68a5492e-0979-3e4e-bba6-66802be9213c | -15.6053 | -48.3627 | 2025-09-01 01:50:00 | GOES-19 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 67.9 |
| a6c06c7e-3b1f-362b-921d-bd7dc51a85f1 | -15.6058 | -48.3402 | 2025-09-01 01:50:00 | GOES-19 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 169.9 |
| 84cde19c-a137-3573-8c99-d0fa9d2f2bd1 | -7.0948 | -44.3358 | 2025-09-01 01:50:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 170.8 |
| 479f53d8-c5a9-3ce6-9782-45a87db0f661 | -9.1165 | -65.5459 | 2025-09-01 01:50:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 32.4 |
| f6cc3ddb-1aea-397f-a7da-6426f68ad86d | -6.8466 | -52.8132 | 2025-09-01 01:50:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 50.5 |
| 43c38bea-3902-34f9-820f-43793b436b63 | -6.4605 | -43.9532 | 2025-09-01 01:50:00 | GOES-19 | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 603.9 |
| e41c5a97-4a2b-34fe-a1eb-f8cc3ed4040e | -9.4432 | -60.5692 | 2025-09-01 01:50:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 53.6 |
| cc49a9bd-1445-3e10-a8de-3bb7788adf5a | -7.0946 | -44.3589 | 2025-09-01 01:50:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 129.8 |
| 90112ddf-c45f-3157-8507-21fe95494b31 | -12.9197 | -56.9471 | 2025-09-01 01:50:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 271.3 |
| b4c61c3e-0804-387f-bf33-bf7599ca9514 | -13.1648 | -45.2665 | 2025-09-01 01:50:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 60.2 |
| ff663063-2a02-34b6-b81b-d98700a4781c | -8.6468 | -67.2515 | 2025-09-01 01:50:00 | GOES-19 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 28.1 |
| 56f71c84-bc96-38f5-9a5b-ef03c2861adf | -15.5857 | -48.366 | 2025-09-01 01:50:00 | GOES-19 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 81.4 |
| 07fabe00-87a7-319c-beb7-61225a9619e1 | -9.6316 | -47.8149 | 2025-09-01 01:50:00 | GOES-19 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 56.2 |
| 11321f2e-309f-32c5-ba2d-9fc7d3cec7e4 | -11.0381 | -45.1256 | 2025-09-01 01:50:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 70.3 |
| 77cc748a-5b4f-3c47-82cb-4bdfba28be7d | -11.0377 | -45.1487 | 2025-09-01 02:00:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 121.4 |
| a5c9f4d2-5308-3f89-b30a-3a8f1156c15a | -6.8466 | -52.8132 | 2025-09-01 02:00:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 59.7 |
| 59e95774-a333-3720-ad24-43995a4b0ac4 | -12.9006 | -56.9488 | 2025-09-01 02:00:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 57.9 |
| f15ff785-1d7b-37d7-91da-4661823ef6fd | -15.6053 | -48.3627 | 2025-09-01 02:00:00 | GOES-19 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 72.2 |
| 33d10086-5728-333e-8223-0ce9a9aaf79d | -13.1837 | -45.2865 | 2025-09-01 02:00:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 59.5 |
| b97bbde5-70b8-38e0-814a-f81794e80ab3 | -6.4607 | -43.9301 | 2025-09-01 02:00:00 | GOES-19 | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 74.1 |
| 316548dd-f089-3d3c-ad6d-17d59d007493 | -6.4605 | -43.9532 | 2025-09-01 02:00:00 | GOES-19 | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 434.3 |
| 6608b4b3-a478-3669-831c-99c6b60c0ab1 | -12.9194 | -56.9672 | 2025-09-01 02:00:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 248.5 |
| 544775f8-e03b-3af1-8279-a8750814caec | -8.7684 | -61.4261 | 2025-09-01 02:00:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 69.3 |
| 4b6b8877-7120-3545-9789-3e86e3d352d9 | -6.4415 | -43.9779 | 2025-09-01 02:00:00 | GOES-19 | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 56.4 |
| 08263899-e9ff-3888-ac24-e429f1f3629d | -7.0946 | -44.3589 | 2025-09-01 02:00:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 104.6 |
| 87b34108-08e2-37ee-b4d3-8662eec7ef04 | -12.9199 | -56.927 | 2025-09-01 02:00:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 58.6 |
| 6c8b5663-e7d5-372f-be3b-d756e3fd884d | -15.5862 | -48.3435 | 2025-09-01 02:00:00 | GOES-19 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 115.4 |
| d756d943-5eb1-31d2-a024-4f38fa905ca9 | -10.5937 | -44.331 | 2025-09-01 02:00:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 61.7 |
| f7335880-56e7-38c8-88dd-cd02fa1b7bc8 | -6.4793 | -43.9516 | 2025-09-01 02:00:00 | GOES-19 | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 97.8 |
| 74581673-bff8-3f9d-8fb1-9d40983ead4c | -9.1522 | -65.8434 | 2025-09-01 02:00:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 34.8 |
| 8016ae57-5734-3bdd-b8ed-11477a06e0be | -7.0948 | -44.3358 | 2025-09-01 02:00:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 148.8 |
| e8a66470-242e-31d0-abbf-7ac1d80712ba | -9.1165 | -65.5459 | 2025-09-01 02:00:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 34.4 |
| b6ba93b5-0c2f-3f64-803f-21eb69453597 | -9.135 | -65.5453 | 2025-09-01 02:00:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 79.7 |
| 59feac0a-b8c1-33ae-9d4a-e641e0c7da94 | -10.0434 | -48.0998 | 2025-09-01 02:00:00 | GOES-19 | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 57.8 |
| aad0ad8a-9c07-3ca5-82e6-259b2dafd0dc | -15.6058 | -48.3402 | 2025-09-01 02:00:00 | GOES-19 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 154.9 |
| d8301995-579b-3fb6-bac5-5eec8ed1d275 | -7.076 | -44.3376 | 2025-09-01 02:00:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 129.6 |
| 66acd969-9d37-38cf-be80-83e5d9513582 | -15.7112 | -48.9032 | 2025-09-01 02:00:00 | GOES-19 | PIRENÓPOLIS | GOIÁS | Brasil | 5217302 | 52 | 33 | nan | nan | nan | Cerrado | 98.9 |
| 45b59675-a159-3643-8234-161c72017cda | -13.1842 | -45.2633 | 2025-09-01 02:00:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 66.4 |
| 125dbf31-5438-396a-a42b-a6ca40ca0c02 | -13.1644 | -45.2897 | 2025-09-01 02:00:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 65.2 |
| da807757-196f-34af-bf47-9d522590af13 | -12.9385 | -56.9655 | 2025-09-01 02:00:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 81.4 |
| 456c4c83-c346-3b28-9a2b-0a98a9f2d74a | -9.1337 | -65.844 | 2025-09-01 02:00:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 70.1 |
| e308cfc3-43ee-341b-9c58-9046273b6217 | -12.9387 | -56.9454 | 2025-09-01 02:00:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 101.8 |
| 0ce45679-f8ff-39f4-b197-62fabc99ed01 | -15.6063 | -48.3177 | 2025-09-01 02:00:00 | GOES-19 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 69.2 |
| a51ed503-1985-3210-8d73-3e6a64ab7c54 | -6.4417 | -43.9548 | 2025-09-01 02:00:00 | GOES-19 | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 100.0 |
| 477bd429-325f-30a0-85bb-4e9e502d6849 | -7.6783 | -61.0908 | 2025-09-01 02:00:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 57.6 |
| 79f3aeda-fc58-32e2-aa48-ba769c8ae139 | -6.4602 | -43.9764 | 2025-09-01 02:00:00 | GOES-19 | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 216.7 |
| afa14c0e-fdba-3f0d-928f-f8ee051011c7 | -4.9124 | -43.187 | 2025-09-01 02:00:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 49.8 |
| 2d4a9938-a7c0-3c92-8c9f-9681f4bfc30a | -7.0757 | -44.3606 | 2025-09-01 02:00:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 98.7 |
| a5690bce-3880-3aef-9557-83bda6ffce0e | -13.1648 | -45.2665 | 2025-09-01 02:00:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 68.1 |
| 49bd43aa-cee7-39dd-a248-fdf31a395e4b | -12.9197 | -56.9471 | 2025-09-01 02:00:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 318.9 |
| 39d81bb4-5862-3727-b3e7-219d6810c16a | -11.0568 | -45.146 | 2025-09-01 02:00:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 73.9 |
| 99d3871d-12e9-3053-8219-c66c6a0a68ec | -9.1336 | -65.8627 | 2025-09-01 02:00:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 47.6 |
| 2b44df97-eea6-3487-92a7-95a21febc595 | -15.5867 | -48.321 | 2025-09-01 02:00:00 | GOES-19 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 69.8 |
| 53debe3f-082c-35bc-96fa-d154c1b578a9 | -10.6128 | -44.3284 | 2025-09-01 02:00:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 97.5 |
| a5f9172c-afa5-3e29-8467-dff152cf5c1d | -11.0381 | -45.1256 | 2025-09-01 02:00:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 65.5 |
| 23c59aae-b48f-3163-8bc6-d064b0b1ede5 | -12.9385 | -56.9655 | 2025-09-01 02:10:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 152.4 |
| b1469000-fe9d-3959-ada9-23a63b58d06f | -13.1837 | -45.2865 | 2025-09-01 02:10:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 63.7 |
| 0d761474-022a-3686-ac3f-611b46726ce3 | -12.9387 | -56.9454 | 2025-09-01 02:10:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 227.9 |
| 29b1dc90-f232-3ec5-94b4-dcb34f889333 | -11.0568 | -45.146 | 2025-09-01 02:10:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 52.1 |
| 96b45371-8050-3360-8de5-a0dbaccd8a28 | -9.135 | -65.5453 | 2025-09-01 02:10:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 51.6 |
| 9d3e2860-fa5c-318d-9e60-df1c8fab68f3 | -11.0377 | -45.1487 | 2025-09-01 02:10:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 118.3 |
| c00ff810-0cb7-3567-af38-df8be1fcb1be | -8.7684 | -61.4261 | 2025-09-01 02:10:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 45.7 |
| 58cf2d0b-0793-39bb-a606-cbd2e6685a4b | -6.7626 | -43.7881 | 2025-09-01 02:10:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 92.1 |
| c1237087-3e90-3a28-8070-ea34026be7d3 | -9.0799 | -65.4349 | 2025-09-01 02:10:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 34.7 |
| f71f9748-337b-329a-8a4b-0fe7afabef2a | -10.6131 | -44.3051 | 2025-09-01 02:10:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 59.7 |
| e7de0263-cefa-3419-a99b-bd124a47b438 | -9.1165 | -65.5459 | 2025-09-01 02:10:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 39.3 |
| fc3398d1-f5bd-3d65-85be-9c40267852f2 | -8.7499 | -61.4269 | 2025-09-01 02:10:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 42.9 |
| bf89a1e9-e2ff-32d6-9a4b-d9a6f4d16fbb | -6.4605 | -43.9532 | 2025-09-01 02:10:00 | GOES-19 | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 323.3 |
| adf49fa0-757c-3a0e-9ed4-037375f96643 | -7.0946 | -44.3589 | 2025-09-01 02:10:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 90.3 |
| b4677c5e-4d20-3c9f-9ae6-8a9570f0f643 | -6.7438 | -43.7898 | 2025-09-01 02:10:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 80.2 |
| f5986ecf-d9c0-34c0-b419-5515af2d6588 | -10.2488 | -51.1128 | 2025-09-01 02:10:00 | GOES-19 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Cerrado | 94.2 |
| be971a9e-f551-3500-bf56-39c516c41989 | -6.4602 | -43.9764 | 2025-09-01 02:10:00 | GOES-19 | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 123.5 |
| 3817f67f-9ab9-315d-9baa-462c5e2c52f2 | -15.5862 | -48.3435 | 2025-09-01 02:10:00 | GOES-19 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 139.6 |
| 55cd771d-53aa-3d2c-a549-89d60097ca4d | -12.9006 | -56.9488 | 2025-09-01 02:10:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 84.4 |


[Clique aqui para ver as próximas entradas](README9.md)
