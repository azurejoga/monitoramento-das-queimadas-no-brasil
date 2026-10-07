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

## Dados Diários - Página 239

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| f81a8011-e1ae-38d6-a0c8-25f0525237ee | -3.10115 | -57.63443 | 2026-10-07 16:39:00 | NPP-375 | BOA VISTA DO RAMOS | AMAZONAS | Brasil | 1300680 | 13 | 33 | nan | nan | nan | Amazônia | 6.5 |
| 57debc16-2d3a-391f-8f65-156198cebe8b | -3.62435 | -55.50911 | 2026-10-07 16:39:00 | NPP-375 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 19.7 |
| 2d0ccadf-b791-354d-893b-64e31a1c63da | -1.28031 | -55.41114 | 2026-10-07 16:39:00 | NPP-375 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 8.7 |
| 86947940-c5c7-3556-b981-d15f51f7b7a0 | 3.22705 | -51.30847 | 2026-10-07 16:39:00 | NPP-375 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 5.5 |
| cadd432d-91ad-35c7-8c60-d266c41389cd | 1.94831 | -55.13458 | 2026-10-07 16:39:00 | NPP-375 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 20.5 |
| f4a93f5c-e8da-3c53-8594-08a3ec3d4f4a | -3.65273 | -55.4528 | 2026-10-07 16:39:00 | NPP-375 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 19.7 |
| 7edea3ff-f91f-32f5-bc0f-35be5f59920b | -3.21642 | -53.8806 | 2026-10-07 16:39:00 | NPP-375 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 0775cc09-9156-39ac-ab7b-5083320e4bc4 | -3.27275 | -54.06266 | 2026-10-07 16:39:00 | NPP-375 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 31.7 |
| 34542cf6-4454-3980-9bd4-9e844bfdc40f | -3.43979 | -49.2533 | 2026-10-07 16:39:00 | NPP-375 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 10.4 |
| 77863ebc-7dec-3e60-ac47-0e4812b53af0 | -2.49575 | -56.24145 | 2026-10-07 16:39:00 | NPP-375 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 15.7 |
| ec63aa7c-99e5-393f-89f8-c672f89b20a8 | -2.83745 | -54.12785 | 2026-10-07 16:39:00 | NPP-375 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 16.7 |
| 923e469c-2114-3bcf-80c8-64670886964b | -4.09756 | -52.06622 | 2026-10-07 16:39:00 | NPP-375 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 31.3 |
| e0e17993-7e75-3acd-8db9-60df2408efd5 | -2.0545 | -45.97545 | 2026-10-07 16:39:00 | NPP-375 | MARACAÇUMÉ | MARANHÃO | Brasil | 2106326 | 21 | 33 | nan | nan | nan | Amazônia | 7.5 |
| 18c6f4bc-f115-3814-b5ec-45f1d3e77813 | -2.18813 | -56.10749 | 2026-10-07 16:39:00 | NPP-375 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 10.2 |
| 508f9723-662f-3346-9c9d-742fd06605e9 | -4.91542 | -55.86135 | 2026-10-07 16:39:00 | NPP-375 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 8cb84f00-fd41-3d41-8c28-7481421bff20 | -1.84917 | -44.8036 | 2026-10-07 16:39:00 | NPP-375 | CURURUPU | MARANHÃO | Brasil | 2103703 | 21 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 4331d8f6-5879-31dc-ae09-d5bf5a713218 | -1.28605 | -54.56648 | 2026-10-07 16:39:00 | NPP-375 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| d890787c-1bbc-3931-90dc-4be6ab034b20 | -3.16335 | -50.43803 | 2026-10-07 16:39:00 | NPP-375 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 9.1 |
| 6a2d7dcd-5e98-399a-980a-0c56615cadb6 | -3.00051 | -54.04817 | 2026-10-07 16:39:00 | NPP-375 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 49ea37a2-1a2d-3ecd-a0c6-f8c054df986e | -1.05483 | -53.59186 | 2026-10-07 16:39:00 | NPP-375 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 48f427aa-b081-36d1-bfda-01b0bc467928 | 0.72327 | -51.36552 | 2026-10-07 16:39:00 | NPP-375 | PORTO GRANDE | AMAPÁ | Brasil | 1600535 | 16 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 122101c3-04b5-38c1-8fdb-f7e07b3eed1a | -2.42764 | -56.53699 | 2026-10-07 16:39:00 | NPP-375 | PARINTINS | AMAZONAS | Brasil | 1303403 | 13 | 33 | nan | nan | nan | Amazônia | 24.3 |
| 58f37da4-ce25-33fb-8c76-8debbf3085e0 | -1.43835 | -49.03458 | 2026-10-07 16:39:00 | NPP-375 | PONTA DE PEDRAS | PARÁ | Brasil | 1505700 | 15 | 33 | nan | nan | nan | Amazônia | 14.3 |
| 383807fd-95e7-35a7-84f9-ae1d4420a83e | -3.28992 | -54.02879 | 2026-10-07 16:39:00 | NPP-375 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 11.4 |
| 58ca3937-a5ce-3649-a5be-67f6cc59cc89 | 1.52828 | -56.02398 | 2026-10-07 16:39:00 | NPP-375 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 760b1753-77cc-376e-a169-f1895acc5a7f | -2.51488 | -56.25347 | 2026-10-07 16:39:00 | NPP-375 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 63.5 |
| d92db0f4-b5cf-34f7-b2aa-358854cf4f63 | -1.2779 | -55.85395 | 2026-10-07 16:39:00 | NPP-375 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 29.3 |
| 78e68074-dc14-3eff-9d8a-83ec49f5e8e2 | -3.2786 | -54.02686 | 2026-10-07 16:39:00 | NPP-375 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 6.5 |
| 9ac3d35c-af0d-31ca-84f5-1c158a160455 | -3.26778 | -54.25909 | 2026-10-07 16:39:00 | NPP-375 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 217eb5e0-beda-38e7-ab7f-951cc3176bbd | -2.90931 | -57.39743 | 2026-10-07 16:39:00 | NPP-375 | BARREIRINHA | AMAZONAS | Brasil | 1300508 | 13 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 62080fd4-bc28-3aa8-82c0-7f5ca0d6ed72 | -2.4563 | -46.03164 | 2026-10-07 16:39:00 | NPP-375 | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 9.6 |
| 12aeb280-70bc-36de-a5a4-7574676f424e | -2.94277 | -54.12015 | 2026-10-07 16:39:00 | NPP-375 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 10.4 |
| 4aa77ab6-3eb1-348f-a9d0-5162c7a9f9ff | -3.08049 | -54.28406 | 2026-10-07 16:39:00 | NPP-375 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 84.9 |
| 5e4307f9-4faf-3072-a7cc-9b2391c05247 | -2.92963 | -54.14297 | 2026-10-07 16:39:00 | NPP-375 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| ba6633a8-8cf6-3a31-85eb-76ca262a6e08 | -3.05093 | -53.92937 | 2026-10-07 16:39:00 | NPP-375 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 11.5 |
| 795b2f63-269d-3184-b4a6-2aa00fae870e | -1.17236 | -53.02781 | 2026-10-07 16:39:00 | NPP-375 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 10737b07-a021-3a0f-8fac-40ccd65168a2 | -3.05551 | -54.26697 | 2026-10-07 16:39:00 | NPP-375 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 18.3 |
| 9794df0e-6f9a-3068-b20c-971e45cb6d09 | -2.42689 | -56.53204 | 2026-10-07 16:39:00 | NPP-375 | PARINTINS | AMAZONAS | Brasil | 1303403 | 13 | 33 | nan | nan | nan | Amazônia | 31.7 |
| b1f0ea88-1447-3c02-aa7b-21dc7ed3b9c8 | -3.64228 | -54.51141 | 2026-10-07 16:39:00 | NPP-375 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 7.0 |
| 1fce6629-bffd-3c0e-b6b0-7c050930040a | -3.08774 | -54.29631 | 2026-10-07 16:39:00 | NPP-375 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 22.1 |
| 6e1a4621-b293-3ef2-862d-d686b8e62e8e | -3.21009 | -53.87482 | 2026-10-07 16:39:00 | NPP-375 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 19.0 |
| d10c139c-c541-334f-8581-a8a9d030737f | -1.27328 | -55.86318 | 2026-10-07 16:39:00 | NPP-375 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 16.1 |
| d94d8ff5-6777-3756-a09e-cd7ff0aecca9 | -0.95848 | -47.90134 | 2026-10-07 16:39:00 | NPP-375 | SÃO JOÃO DA PONTA | PARÁ | Brasil | 1507466 | 15 | 33 | nan | nan | nan | Amazônia | 7.8 |
| 5148ab9d-2e5e-34f4-beba-ec32a0806d36 | -3.04599 | -53.16399 | 2026-10-07 16:39:00 | NPP-375 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 7.0 |
| b45aae3c-fbbf-3829-b3f8-54bec7b86805 | -3.13056 | -43.83841 | 2026-10-07 16:39:00 | NPP-375 | CACHOEIRA GRANDE | MARANHÃO | Brasil | 2102374 | 21 | 33 | nan | nan | nan | Cerrado | 46.9 |
| abd0dfe9-83cb-3476-ba50-8363e151ea44 | 1.34467 | -56.13007 | 2026-10-07 16:39:00 | NPP-375 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| b9ef7359-f1c8-3583-8e5a-5d3943ec3862 | -3.04462 | -53.92358 | 2026-10-07 16:39:00 | NPP-375 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 9.9 |
| 985169f1-9503-3aef-bc56-c0d9783ceee3 | -2.9387 | -54.1663 | 2026-10-07 16:39:00 | NPP-375 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 8.5 |
| ee0f8b53-c899-3151-b3e7-d8a1eb577b6d | -3.03927 | -53.92435 | 2026-10-07 16:39:00 | NPP-375 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 9.9 |
| 0849cbd3-7961-382a-b586-3108fa820c29 | -3.50428 | -58.54805 | 2026-10-07 16:39:00 | NPP-375 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 8.2 |
| e26a0aee-d47b-3e74-8c7e-a6eb6f17e8ce | -3.65596 | -50.9547 | 2026-10-07 16:39:00 | NPP-375 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 37.3 |
| f2c48602-8b70-35a8-9c19-2944cb0d5a24 | -3.29232 | -54.0075 | 2026-10-07 16:39:00 | NPP-375 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 20.2 |
| 3b3b7373-aea1-38af-89f2-14abecfa80b5 | -4.09356 | -52.07218 | 2026-10-07 16:39:00 | NPP-375 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 13.1 |
| ee0679f1-3915-375b-9306-a229fba4fbfd | -2.9901 | -54.77407 | 2026-10-07 16:39:00 | NPP-375 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| fd7a2eab-f25e-3f07-b1c2-908f42675005 | -3.29684 | -54.03829 | 2026-10-07 16:39:00 | NPP-375 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 67.3 |
| ebe454f7-7db6-3593-85dd-9b02316a5cfa | -3.29434 | -54.02129 | 2026-10-07 16:39:00 | NPP-375 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 6c325396-66ae-339a-bfb1-3338a01dea8e | -3.30121 | -57.84734 | 2026-10-07 16:39:00 | NPP-375 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 9.3 |
| c1e91234-53a6-35e5-899c-d627ad9e6146 | -3.51225 | -54.6609 | 2026-10-07 16:39:00 | NPP-375 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 7.4 |
| 153bfa1f-7077-323b-86ba-538aa3f62038 | -3.99328 | -56.2664 | 2026-10-07 16:39:00 | NPP-375 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 7.2 |
| cd831dd3-4b8c-3cd3-a841-63d3c0a3ea13 | -3.17235 | -50.44069 | 2026-10-07 16:39:00 | NPP-375 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 7.2 |
| df8e9643-fd33-368e-90e8-644429f88268 | -3.11206 | -54.15749 | 2026-10-07 16:39:00 | NPP-375 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 697f71b0-0806-3812-bd29-a916c7090726 | -3.96417 | -55.83417 | 2026-10-07 16:39:00 | NPP-375 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 8.8 |
| 07b23a65-57a0-3feb-860a-c03b7be1bf50 | 3.22591 | -51.31553 | 2026-10-07 16:39:00 | NPP-375 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 15.8 |
| 76bfcd31-f663-3406-a393-aa2e6b31aadb | -1.02742 | -53.73663 | 2026-10-07 16:39:00 | NPP-375 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 7c393314-150c-32b8-9905-1f25fdbee236 | -2.48937 | -56.11685 | 2026-10-07 16:39:00 | NPP-375 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 7.7 |
| 3c521603-acfc-3b9a-87aa-c410324e6f87 | -2.51701 | -56.25667 | 2026-10-07 16:39:00 | NPP-375 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 27.3 |
| 217c7ea1-45ac-3cf7-b8bc-cfe1a96a1598 | -3.3627 | -53.53849 | 2026-10-07 16:39:00 | NPP-375 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 8cdc84c1-605c-3c7d-aa73-ca6fe13fbef3 | -4.1099 | -54.41619 | 2026-10-07 16:39:00 | NPP-375 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 6.9 |
| 2f490ebd-b43c-35c9-9252-59591b73e486 | -1.24792 | -55.70714 | 2026-10-07 16:39:00 | NPP-375 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 4555a1b2-4f10-36e0-95c8-f208baa0644d | -2.03591 | -55.63651 | 2026-10-07 16:39:00 | NPP-375 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| bc21222e-bfb3-3427-8a32-79a7514c3e7b | -3.65604 | -55.46103 | 2026-10-07 16:39:00 | NPP-375 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 30.7 |
| a18d1b2f-4abd-3ac3-aca6-e0a5a42ff9e6 | -3.0 | -54.04478 | 2026-10-07 16:39:00 | NPP-375 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 338469f7-6c11-32ee-a4b6-c9817dd5bca2 | -1.41869 | -55.42831 | 2026-10-07 16:39:00 | NPP-375 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 10.6 |
| 9fb6539d-3a6a-38a8-bb7d-9369270df229 | -2.76891 | -54.07516 | 2026-10-07 16:39:00 | NPP-375 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 30.4 |
| cb50a65c-539e-31b1-9ed7-c70aabcdeeac | -1.80664 | -57.11311 | 2026-10-07 16:39:00 | NPP-375 | NHAMUNDÁ | AMAZONAS | Brasil | 1303007 | 13 | 33 | nan | nan | nan | Amazônia | 79.4 |
| aca9d22c-3635-38e2-9867-2fd910f388bd | -2.88812 | -54.12429 | 2026-10-07 16:39:00 | NPP-375 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 8.2 |
| 53559c67-b3ed-341d-b311-0965964a9d56 | -3.5436 | -54.66381 | 2026-10-07 16:39:00 | NPP-375 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 19.3 |
| 3e252d37-0191-3984-8ffe-15c9ca76c80f | -3.84326 | -50.32061 | 2026-10-07 16:39:00 | NPP-375 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 1e218d98-9c6d-33ec-a1ce-038b64ccf663 | -0.95789 | -47.89743 | 2026-10-07 16:39:00 | NPP-375 | SÃO JOÃO DA PONTA | PARÁ | Brasil | 1507466 | 15 | 33 | nan | nan | nan | Amazônia | 7.8 |
| c0fb9bf8-2a88-3ab3-8b26-7a40ab57e1d3 | 3.21896 | -51.3072 | 2026-10-07 16:39:00 | NPP-375 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 42fa4cb6-5197-328d-886e-bc7d8db055e7 | 1.69695 | -55.63831 | 2026-10-07 16:39:00 | NPP-375 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 22.3 |
| cfadaf0f-d1e7-368b-808d-317b5658cd8a | -2.94859 | -54.06957 | 2026-10-07 16:39:00 | NPP-375 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 10.7 |
| f8093475-e870-3a2e-9557-23c1f0049966 | -1.88819 | -53.9754 | 2026-10-07 16:39:00 | NPP-375 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 8.2 |
| d9d076d8-20b9-34b0-8e14-c8db57e9859d | -3.28692 | -54.00825 | 2026-10-07 16:39:00 | NPP-375 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 20.2 |
| 12c88814-9b53-3977-922f-66783c991456 | -4.06698 | -55.32131 | 2026-10-07 16:39:00 | NPP-375 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 27.6 |
| 11bbec84-204b-34b8-b3a7-e08a3c55ae4b | -2.64723 | -56.54377 | 2026-10-07 16:39:00 | NPP-375 | PARINTINS | AMAZONAS | Brasil | 1303403 | 13 | 33 | nan | nan | nan | Amazônia | 8.5 |
| c00e8115-6daf-3605-a593-80d0f5213a0a | -3.00704 | -43.84047 | 2026-10-07 16:39:00 | NPP-375 | MORROS | MARANHÃO | Brasil | 2107100 | 21 | 33 | nan | nan | nan | Cerrado | 5.6 |
| d9c43bd7-39f4-35e2-be05-136d246ad76f | -3.02487 | -54.17419 | 2026-10-07 16:39:00 | NPP-375 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 9c533faa-cc7a-36ed-bf5d-e3218b11f6d8 | -3.41249 | -58.02819 | 2026-10-07 16:39:00 | NPP-375 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 16.0 |
| f6a33e99-3894-3dce-a3df-e62053ccf937 | -2.94083 | -54.1688 | 2026-10-07 16:39:00 | NPP-375 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 10.3 |
| f0abdc43-6f08-3a53-9655-800faff4d00c | -1.4852 | -55.87279 | 2026-10-07 16:39:00 | NPP-375 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 6.2 |
| ccc45987-b7af-3377-ab69-db5a2880f537 | -2.96602 | -56.63166 | 2026-10-07 16:39:00 | NPP-375 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 14.0 |
| dc59b817-0d9a-3ac1-99a4-a08234e04cf7 | -3.2797 | -54.07242 | 2026-10-07 16:39:00 | NPP-375 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 10.6 |
| d61275eb-9b96-3649-8cd1-49d5230c73fc | -3.35749 | -53.53944 | 2026-10-07 16:39:00 | NPP-375 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 2e5a4f2a-3fb5-3a74-aa8e-f577a01d2a19 | 3.22648 | -51.31201 | 2026-10-07 16:39:00 | NPP-375 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 15.8 |
| 90168f66-3f81-37c7-99b0-71b5de662fb0 | -3.24948 | -56.80387 | 2026-10-07 16:39:00 | NPP-375 | PARINTINS | AMAZONAS | Brasil | 1303403 | 13 | 33 | nan | nan | nan | Amazônia | 54.0 |
| 7bbeb9cb-110d-3583-a3c9-7202c6240e29 | -3.27021 | -54.0071 | 2026-10-07 16:39:00 | NPP-375 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 7.2 |
| 110a6ee8-454e-369b-a106-5332d44bf250 | -3.10318 | -54.28685 | 2026-10-07 16:39:00 | NPP-375 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 20.5 |
| b3423703-c05f-3fd9-9ca3-e3ffa2e68f63 | -3.07621 | -54.25595 | 2026-10-07 16:39:00 | NPP-375 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 7.6 |
| 4421e72d-9c1b-34fe-b11b-0555b0e4fd31 | 1.08919 | -50.72882 | 2026-10-07 16:39:00 | NPP-375 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 9.6 |


[Clique aqui para ver as próximas entradas](README240.md)
