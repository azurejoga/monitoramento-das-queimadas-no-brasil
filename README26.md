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

## Dados Diários - Página 26

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 891db8be-8243-3ca0-b3e2-3752bce6b9a3 | -15.23286 | -46.14188 | 2026-10-01 03:40:00 | NOAA-21 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 22e34f42-b2aa-3595-82c8-425c19daa82b | -19.2304 | -42.94547 | 2026-10-01 03:40:00 | NOAA-21 | FERROS | MINAS GERAIS | Brasil | 3125903 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.7 |
| 1cb1a205-811f-3392-8a35-0e1d21a812a7 | -17.08914 | -46.82031 | 2026-10-01 03:40:00 | NOAA-21 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 8309d549-3d33-3e48-a960-b2e8ed3c3d96 | -20.18641 | -47.40732 | 2026-10-01 03:40:00 | NOAA-21 | PEDREGULHO | SÃO PAULO | Brasil | 3537008 | 35 | 33 | nan | nan | nan | Cerrado | 21.7 |
| 5c645ee9-1abc-3763-8287-d2f4586d5d56 | -19.11119 | -41.50168 | 2026-10-01 03:40:00 | NOAA-21 | CONSELHEIRO PENA | MINAS GERAIS | Brasil | 3118403 | 31 | 33 | nan | nan | nan | Mata Atlântica | 7.8 |
| 37061591-74a0-3ebd-81ac-30cc15cf0493 | -19.23386 | -42.95039 | 2026-10-01 03:40:00 | NOAA-21 | FERROS | MINAS GERAIS | Brasil | 3125903 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.9 |
| 076cc93c-a81a-3c57-b127-49913f73b7f7 | -22.14582 | -46.67411 | 2026-10-01 03:40:00 | NOAA-21 | SANTO ANTÔNIO DO JARDIM | SÃO PAULO | Brasil | 3548104 | 35 | 33 | nan | nan | nan | Mata Atlântica | 4.2 |
| d04efc8f-e0d1-3ef2-8a26-225d7f51b14e | -14.49372 | -48.31118 | 2026-10-01 03:40:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 6.2 |
| a4f04c08-ab3c-39f7-a8b6-16557fa6db69 | -18.47727 | -41.42867 | 2026-10-01 03:40:00 | NOAA-21 | SÃO JOSÉ DO DIVINO | MINAS GERAIS | Brasil | 3163300 | 31 | 33 | nan | nan | nan | Mata Atlântica | 7.8 |
| 8601f124-a650-3072-a277-27e1ca840a48 | -18.07157 | -44.36853 | 2026-10-01 03:40:00 | NOAA-21 | AUGUSTO DE LIMA | MINAS GERAIS | Brasil | 3104809 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 451a0171-3afc-3595-8571-fd69411dad7b | -20.19182 | -50.90038 | 2026-10-01 03:40:00 | NOAA-21 | SANTA FÉ DO SUL | SÃO PAULO | Brasil | 3546603 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| e9a9e364-b86b-34dc-a278-8b1e523cd110 | -22.1401 | -46.6761 | 2026-10-01 03:40:00 | NOAA-21 | SANTO ANTÔNIO DO JARDIM | SÃO PAULO | Brasil | 3548104 | 35 | 33 | nan | nan | nan | Mata Atlântica | 4.2 |
| fae3afc6-9785-3032-a69c-3a8cb0c8c974 | -19.23418 | -42.94609 | 2026-10-01 03:40:00 | NOAA-21 | FERROS | MINAS GERAIS | Brasil | 3125903 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.0 |
| 302dbab5-2aa8-3b77-82c0-b12fc9436973 | -21.17518 | -47.01531 | 2026-10-01 03:40:00 | NOAA-21 | MONTE SANTO DE MINAS | MINAS GERAIS | Brasil | 3143203 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 2918c467-f2ad-3ab6-b256-74ab8e82d8a3 | -15.95505 | -41.89929 | 2026-10-01 03:40:00 | NOAA-21 | SANTA CRUZ DE SALINAS | MINAS GERAIS | Brasil | 3157377 | 31 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 2627d7c1-e5c8-30c8-8843-16f22419ff64 | -20.89632 | -47.41956 | 2026-10-01 03:40:00 | NOAA-21 | ALTINÓPOLIS | SÃO PAULO | Brasil | 3501004 | 35 | 33 | nan | nan | nan | Cerrado | 7.2 |
| 90f608fb-17b4-327e-b6bb-6682aba33793 | -19.04259 | -45.66638 | 2026-10-01 03:40:00 | NOAA-21 | CEDRO DO ABAETÉ | MINAS GERAIS | Brasil | 3115607 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| c4abbf62-ac85-31ab-b9f1-d239798abe2f | -20.89804 | -47.41169 | 2026-10-01 03:40:00 | NOAA-21 | ALTINÓPOLIS | SÃO PAULO | Brasil | 3501004 | 35 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 1f991e92-e9d1-3696-9e2e-bb05fa3d5b67 | -17.47346 | -43.56479 | 2026-10-01 03:40:00 | NOAA-21 | OLHOS-D'ÁGUA | MINAS GERAIS | Brasil | 3145455 | 31 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 7805b93b-cd40-318d-822e-b03bfec9ed7f | -16.67875 | -41.8515 | 2026-10-01 03:40:00 | NOAA-21 | ITINGA | MINAS GERAIS | Brasil | 3134004 | 31 | 33 | nan | nan | nan | Mata Atlântica | 13.3 |
| 396bc23e-97f2-3fd4-9eda-cf5c4829a8c5 | -16.14088 | -43.74518 | 2026-10-01 03:40:00 | NOAA-21 | CAPITÃO ENÉAS | MINAS GERAIS | Brasil | 3112703 | 31 | 33 | nan | nan | nan | Cerrado | 4.9 |
| b2bbc27a-e41d-3e42-b9c0-dcf61b977dc1 | -17.91259 | -45.04456 | 2026-10-01 03:40:00 | NOAA-21 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 8238011f-885e-3d50-8134-4cbed97bdf63 | -17.78382 | -42.57697 | 2026-10-01 03:40:00 | NOAA-21 | CAPELINHA | MINAS GERAIS | Brasil | 3112307 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.5 |
| d4820fd9-8165-3aa9-83cc-564203aeaa48 | -14.48723 | -48.31005 | 2026-10-01 03:40:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 8.0 |
| f2aa4dd9-30c8-362a-a096-492a60a34f8c | -17.4732 | -43.5622 | 2026-10-01 03:40:00 | NOAA-21 | OLHOS-D'ÁGUA | MINAS GERAIS | Brasil | 3145455 | 31 | 33 | nan | nan | nan | Cerrado | 9.0 |
| d50c23b2-d227-3b17-83b3-50955f7e389f | -16.22483 | -43.6214 | 2026-10-01 03:40:00 | NOAA-21 | CAPITÃO ENÉAS | MINAS GERAIS | Brasil | 3112703 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 5f7bb986-618b-36cb-9fc6-3d1aba903f83 | -16.17827 | -42.88051 | 2026-10-01 03:40:00 | NOAA-21 | GRÃO MOGOL | MINAS GERAIS | Brasil | 3127800 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 856f4b9d-5ddd-33c2-8a2f-b48a18e68321 | -18.51057 | -45.14568 | 2026-10-01 03:40:00 | NOAA-21 | TRÊS MARIAS | MINAS GERAIS | Brasil | 3169356 | 31 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 1b3f3cf8-a5c5-3c70-9793-08d216413280 | 3.2742 | -60.6105 | 2026-10-01 03:50:00 | GOES-19 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 59.1 |
| ca29b280-c501-3359-8485-79390bb7c0df | -11.4495 | -43.4566 | 2026-10-01 03:50:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 74.2 |
| 3eaf1b32-8c65-397e-b05d-3ffe2a82320e | -14.8762 | -51.8427 | 2026-10-01 03:50:00 | GOES-19 | ARAGUAIANA | MATO GROSSO | Brasil | 5101001 | 51 | 33 | nan | nan | nan | Cerrado | 100.5 |
| ea7a9990-bf2c-3385-a594-cba3b3274315 | -3.1655 | -54.1045 | 2026-10-01 03:50:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 139.4 |
| 5ce6c4d6-b4ae-3f54-a9c1-65650c5dcabc | 1.7853 | -55.6449 | 2026-10-01 03:50:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 36.4 |
| 9ebd633e-942e-39e0-b777-d4460e618fad | 1.8036 | -55.6447 | 2026-10-01 03:50:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 24.2 |
| 5d66cfb7-7a7d-3b36-8a31-6b51dcea0619 | -3.106 | -50.2896 | 2026-10-01 03:50:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 84.9 |
| ea6355b5-9730-3d34-ac2a-78cecfb07f4c | -5.7561 | -45.1747 | 2026-10-01 03:50:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 62.6 |
| 0108d02f-2d76-3154-9ceb-5f67af28ed4c | -11.4311 | -43.4121 | 2026-10-01 03:50:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 78.2 |
| 04e6aa38-fe44-3c2c-b5bf-9b6b74d8c5f7 | -14.4027 | -51.2865 | 2026-10-01 03:50:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 69.9 |
| 337a8508-bf67-3efc-9084-0c1a392d5614 | -12.1857 | -48.4345 | 2026-10-01 03:50:00 | GOES-19 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 83.7 |
| 996d071e-b21e-3c60-8700-312011ade29e | -3.1838 | -54.1241 | 2026-10-01 03:50:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 54.1 |
| dcaa2b03-ee8e-3624-ae42-d0d980e1090e | -13.6479 | -53.9336 | 2026-10-01 03:50:00 | GOES-19 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Cerrado | 67.0 |
| 4c2c0cfa-1875-3b7b-803e-450115970724 | -14.4035 | -51.2435 | 2026-10-01 03:50:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 76.7 |
| 9867a430-4d84-3e68-a659-db800d9dda32 | -11.4687 | -43.4537 | 2026-10-01 03:50:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 72.4 |
| fdf38ce2-aeb2-30e6-ac75-57fa54bb320e | -3.1838 | -54.104 | 2026-10-01 03:50:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 176.8 |
| cbf3071e-ba0a-3c8b-a6e4-dbf527051a86 | -3.1655 | -54.0844 | 2026-10-01 03:50:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 119.5 |
| 90db3cf8-d731-3a62-bf1b-3d7a7b6649e9 | -14.8758 | -51.8641 | 2026-10-01 03:50:00 | GOES-19 | ARAGUAIANA | MATO GROSSO | Brasil | 5101001 | 51 | 33 | nan | nan | nan | Cerrado | 84.3 |
| fc337c70-d1f7-3ac5-a7c8-f5806e724877 | -13.6671 | -53.9314 | 2026-10-01 03:50:00 | GOES-19 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Cerrado | 71.2 |
| 64354fe8-5a14-382d-8e08-3b264d98ce41 | -10.7853 | -50.5279 | 2026-10-01 03:50:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 53.0 |
| 5e21b30c-1771-3dd6-800b-8e016554ff68 | -3.295 | -53.8597 | 2026-10-01 03:50:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 100.6 |
| f97700c1-c45f-3c38-b474-e03f7fc29353 | -5.7563 | -45.152 | 2026-10-01 03:50:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 82.5 |
| bda09377-1092-3821-8c2e-549e5a01f3c4 | -3.2766 | -53.8602 | 2026-10-01 03:50:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 47.2 |
| 0597c111-8269-3ad5-baa2-ab68cacc0363 | -3.1245 | -50.289 | 2026-10-01 03:50:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 66.4 |
| de5fc608-3992-3ea1-b700-5611007577a8 | -14.4031 | -51.265 | 2026-10-01 03:50:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 154.0 |
| 8f03b5c0-35a3-3ded-b8fe-456a5e824b69 | -3.1839 | -54.0839 | 2026-10-01 03:50:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 47.6 |
| 4389a27b-ed18-396f-a0da-14b5a2770f97 | -14.8568 | -51.8454 | 2026-10-01 03:50:00 | GOES-19 | ARAGUAIANA | MATO GROSSO | Brasil | 5101001 | 51 | 33 | nan | nan | nan | Cerrado | 89.9 |
| 592e6376-2678-311d-ae47-61969154239d | -14.3834 | -51.2892 | 2026-10-01 03:50:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 77.6 |
| 1bc55ad4-b7c7-3c06-9e12-16252f1da793 | -11.4499 | -43.4329 | 2026-10-01 03:50:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 117.6 |
| 76c0815b-40bb-3119-b7f5-e391a3a90b43 | -14.8564 | -51.8668 | 2026-10-01 04:00:00 | GOES-19 | ARAGUAIANA | MATO GROSSO | Brasil | 5101001 | 51 | 33 | nan | nan | nan | Cerrado | 93.7 |
| 63c17b38-0fbd-3774-879f-99d25bc2a327 | -12.1857 | -48.4345 | 2026-10-01 04:00:00 | GOES-19 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 103.7 |
| 155c26f2-2799-3f57-bef1-d423b4eaf271 | -14.8568 | -51.8454 | 2026-10-01 04:00:00 | GOES-19 | ARAGUAIANA | MATO GROSSO | Brasil | 5101001 | 51 | 33 | nan | nan | nan | Cerrado | 155.2 |
| cad59c1a-e928-32eb-8962-5581e702e40f | 1.7853 | -55.6449 | 2026-10-01 04:00:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 38.8 |
| 189f190b-60cb-36ef-9ad6-6042969095b5 | -3.106 | -50.2896 | 2026-10-01 04:00:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 89.5 |
| 23b812d5-ef97-35ca-8fc6-8eaa3abad931 | -14.8758 | -51.8641 | 2026-10-01 04:00:00 | GOES-19 | ARAGUAIANA | MATO GROSSO | Brasil | 5101001 | 51 | 33 | nan | nan | nan | Cerrado | 94.1 |
| b93c6b93-8b6c-30d7-a157-38f26222b2af | -14.3834 | -51.2892 | 2026-10-01 04:00:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 74.7 |
| c9439167-8d8c-3170-bce4-cddb6341f359 | -3.1061 | -50.2686 | 2026-10-01 04:00:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 53.0 |
| 6ed2dd4b-d9a0-34fe-8414-e52246e588bb | -3.1839 | -54.0839 | 2026-10-01 04:00:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 49.1 |
| 58f7b74a-d78f-386d-8436-bd125a8c7518 | -14.4035 | -51.2435 | 2026-10-01 04:00:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 97.3 |
| dd35fac5-611a-3d30-96ee-71a07cf6ed69 | -14.4225 | -51.2624 | 2026-10-01 04:00:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 79.3 |
| f0ad9e84-63b6-377c-b028-20a025eb8ee8 | -14.4031 | -51.265 | 2026-10-01 04:00:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 173.0 |
| 194699b2-4e1b-3af8-b908-36b582baec9b | -13.6479 | -53.9336 | 2026-10-01 04:00:00 | GOES-19 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Cerrado | 69.1 |
| 7f90346c-a1ad-3787-93a1-6741864db1f2 | -5.7563 | -45.152 | 2026-10-01 04:00:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 75.6 |
| cc47734e-dfa1-3d69-8d95-acc9dff5968d | -3.2766 | -53.8602 | 2026-10-01 04:00:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 56.2 |
| 7120a126-36f5-3946-9a22-c0489f16d6ed | -11.4495 | -43.4566 | 2026-10-01 04:00:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 62.1 |
| f3d98ad8-e932-38b6-993d-42ae27817af4 | -11.4503 | -43.4091 | 2026-10-01 04:00:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 68.1 |
| c227d8e2-2795-3d08-9cca-e1bf20df2d1e | -14.8762 | -51.8427 | 2026-10-01 04:00:00 | GOES-19 | ARAGUAIANA | MATO GROSSO | Brasil | 5101001 | 51 | 33 | nan | nan | nan | Cerrado | 137.5 |
| baf5083e-91f3-33c6-bc70-5bf91c784258 | -14.4027 | -51.2865 | 2026-10-01 04:00:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 69.0 |
| c74e87a4-e67c-3ecf-bc19-068c6bad58a8 | -11.4687 | -43.4537 | 2026-10-01 04:00:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 74.6 |
| a15f9377-77a6-3894-ba93-2356889e8c12 | -3.1655 | -54.0844 | 2026-10-01 04:00:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 110.5 |
| c416914b-dd26-3b3e-81d8-f2532bc71222 | -3.1245 | -50.289 | 2026-10-01 04:00:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 53.7 |
| bf9e0c6a-c436-3dba-ab0d-70202c2923ee | -3.1655 | -54.1045 | 2026-10-01 04:00:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 148.3 |
| 9642d1a7-215a-3a56-bb58-572319f23dcd | -3.1838 | -54.104 | 2026-10-01 04:00:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 139.7 |
| 7a14969a-2752-3b90-bb04-7bc667a26ae0 | -11.4499 | -43.4329 | 2026-10-01 04:00:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 103.9 |
| 678eb5d0-74d7-3b7a-a94b-9438b5a1e7ea | -3.295 | -53.8597 | 2026-10-01 04:00:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 80.8 |
| 9ad22e75-0573-31c2-9425-f65c315b1537 | -10.7853 | -50.5279 | 2026-10-01 04:00:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 65.0 |
| bfe62233-a2f9-36ed-98ca-acc88203dbe2 | -14.3838 | -51.2677 | 2026-10-01 04:00:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 90.3 |
| 5492cf27-eed1-3099-9395-a3c94a575bb2 | -3.1655 | -54.1045 | 2026-10-01 04:10:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 131.6 |
| 6b6ca0d5-30fd-3a38-99cd-07853bac95ff | -3.1839 | -54.0839 | 2026-10-01 04:10:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 64.5 |
| 599ca576-07d1-3989-a678-51e513a4094d | -11.4691 | -43.4299 | 2026-10-01 04:10:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 61.2 |
| 612ea9b5-024b-347f-bed8-97aeee27a102 | -14.4027 | -51.2865 | 2026-10-01 04:10:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 63.4 |
| c55175c3-dea1-3bfb-82c3-3b68e6658f40 | -11.4499 | -43.4329 | 2026-10-01 04:10:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 96.4 |
| 6770e90b-9d00-3942-81ba-d49f72246aa5 | -3.295 | -53.8597 | 2026-10-01 04:10:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 81.1 |
| 9c2bbc78-0da2-3e2b-9ec5-83fde96b9371 | -12.1857 | -48.4345 | 2026-10-01 04:10:00 | GOES-19 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 82.4 |
| 323f8cb3-ae35-38a1-8d59-cbc6948a4a63 | -3.106 | -50.2896 | 2026-10-01 04:10:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 82.5 |
| fb16a71f-479b-3044-95c2-1e8028002fd6 | -14.4031 | -51.265 | 2026-10-01 04:10:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 136.9 |
| 3151e01f-2127-313a-8a31-62108b7fe6ec | -14.4035 | -51.2435 | 2026-10-01 04:10:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 83.1 |
| 66d06f40-25f1-39cc-953c-80883a2d6248 | -13.6479 | -53.9336 | 2026-10-01 04:10:00 | GOES-19 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Cerrado | 76.3 |
| 615f0f7d-379e-3187-b242-dd280b249bb3 | -3.1838 | -54.104 | 2026-10-01 04:10:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 114.8 |
| 6160abf2-1600-3e9b-a2d5-12f36dfe341c | -13.6671 | -53.9314 | 2026-10-01 04:10:00 | GOES-19 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Cerrado | 72.1 |
| 881d1528-3480-3398-91cc-7b36cafaa22f | -14.4225 | -51.2624 | 2026-10-01 04:10:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 59.9 |
| 259b2ba8-97c8-3aac-932f-6b7b35684c9c | -3.1655 | -54.0844 | 2026-10-01 04:10:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 117.2 |


[Clique aqui para ver as próximas entradas](README27.md)
