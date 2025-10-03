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

## Dados Diários - Página 23

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 313a708d-b50b-33df-8da0-a54c89f4aeb1 | -15.51286 | -45.90448 | 2025-10-03 03:45:00 | NOAA-21 | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 49a0f65c-1260-3332-87a9-8a8924e37ed3 | -11.4529 | -44.96489 | 2025-10-03 03:45:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| d140b6c3-6b4c-3832-949f-197a9ede4c35 | -14.89631 | -46.97335 | 2025-10-03 03:45:00 | NOAA-21 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 268e0825-397e-313c-b4f9-6fec464da38b | -11.84209 | -45.04482 | 2025-10-03 03:45:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| d2dacfca-c1ff-3b02-857f-c97faf1d5d72 | -11.29521 | -47.83599 | 2025-10-03 03:45:00 | NOAA-21 | SANTA ROSA DO TOCANTINS | TOCANTINS | Brasil | 1718907 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 23f8ca31-8c05-3a33-a50d-3e953a653bd7 | -11.43775 | -43.49784 | 2025-10-03 03:45:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 846c3ab8-2e9f-32b0-9ffb-2061def81452 | -14.30414 | -45.88055 | 2025-10-03 03:45:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| e8833f5a-0fc7-39fa-9eda-14b87202cdcd | -15.71 | -46.27313 | 2025-10-03 03:45:00 | NOAA-21 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 8259fd98-bb68-326e-84ab-bdabd600832b | -13.74531 | -47.98644 | 2025-10-03 03:45:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.3 |
| a06502f2-f591-38b0-9da0-d6b76f734afb | -10.28473 | -44.32446 | 2025-10-03 03:45:00 | NOAA-21 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 62ee4dfe-22b7-3a34-97fd-4a71d3ae87a1 | -13.75413 | -48.08303 | 2025-10-03 03:45:00 | NOAA-21 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 14.6 |
| ffa85136-5941-321a-ae5f-27f6b5116eff | -15.5898 | -46.90608 | 2025-10-03 03:45:00 | NOAA-21 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| b912542a-3706-3ea9-acd7-837ae80d7e03 | -14.36176 | -43.84573 | 2025-10-03 03:45:00 | NOAA-21 | JUVENÍLIA | MINAS GERAIS | Brasil | 3136959 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| fa6503b9-c292-31d0-81bc-f0f5e63c7664 | -13.12125 | -47.85038 | 2025-10-03 03:45:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 3f347670-73e8-37f1-a9c4-32b875f445e5 | -10.86818 | -46.66611 | 2025-10-03 03:45:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 12.2 |
| 54d080ba-028c-36aa-b71e-164bf83e5a12 | -10.85889 | -45.40904 | 2025-10-03 03:45:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| f8f9e1f3-9598-326d-83bb-56a11a3cf09a | -15.08616 | -42.1181 | 2025-10-03 03:45:00 | NOAA-21 | CONDEÚBA | BAHIA | Brasil | 2908705 | 29 | 33 | nan | nan | nan | Mata Atlântica | 2.3 |
| f952f24f-d761-3f72-b38f-3d0dc9a3663b | -15.31844 | -46.89848 | 2025-10-03 03:45:00 | NOAA-21 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| dd16f691-5ef3-3939-91bc-08094056a6de | -14.62 | -48.23795 | 2025-10-03 03:45:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 010b5f0e-d9a0-3310-90f7-212676e2c604 | -11.09917 | -47.83241 | 2025-10-03 03:45:00 | NOAA-21 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 4.6 |
| c57f1ee6-fea4-3f9d-b295-38030b52338d | -9.92932 | -43.72958 | 2025-10-03 03:45:00 | NOAA-21 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| efceea5a-f0f0-3d17-a8a5-19f2fec54fac | -13.19881 | -47.83052 | 2025-10-03 03:45:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 2250362a-e17b-3a0e-87e6-687e436b2152 | -13.47454 | -47.23148 | 2025-10-03 03:45:00 | NOAA-21 | TERESINA DE GOIÁS | GOIÁS | Brasil | 5221080 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| d866ade6-f52b-3ae5-a7ed-8202a45e61c6 | -14.64747 | -48.25316 | 2025-10-03 03:45:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 5dbd2c06-18fc-364d-9fce-709e2f397bd9 | -14.28863 | -45.8913 | 2025-10-03 03:45:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 214acd80-d7ae-33db-84f2-51499ea4e14b | -13.77355 | -47.5791 | 2025-10-03 03:45:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 14.8 |
| e6abe2b1-8284-3b61-bc7b-8608d24574df | -11.85732 | -44.95959 | 2025-10-03 03:45:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 94916864-aa10-32f3-b6b4-82cf174a48b1 | -12.62541 | -46.99281 | 2025-10-03 03:45:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 9.3 |
| 991ee75f-08f1-3134-9869-18c04ae74e50 | -14.18694 | -46.68954 | 2025-10-03 03:45:00 | NOAA-21 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 1290e888-e627-3861-8910-133de2aa4a75 | -14.19304 | -46.687 | 2025-10-03 03:45:00 | NOAA-21 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| dd26e46e-6569-317f-b58f-5a96ccb6e250 | -10.34355 | -43.73446 | 2025-10-03 03:45:00 | NOAA-21 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 3fb888b4-cd20-3cb6-8d0d-7afdd544ebcc | -12.30495 | -46.88071 | 2025-10-03 03:45:00 | NOAA-21 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| d5b49644-9a05-3c49-8f55-f62e6dcbbf1d | -14.94803 | -46.89511 | 2025-10-03 03:45:00 | NOAA-21 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| cf5defb1-75e0-3c1b-ab8e-d9423f3c9f03 | -13.78017 | -47.57586 | 2025-10-03 03:45:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 9.3 |
| 4155faac-a040-3549-824b-342a47ec9ee9 | -13.26761 | -47.25465 | 2025-10-03 03:45:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 5b56f055-784c-31ed-b661-98e1bde6e750 | -13.14229 | -47.89717 | 2025-10-03 03:45:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| dd3b5df2-9397-3b6a-887a-48f5031a7754 | -9.90478 | -43.72869 | 2025-10-03 03:45:00 | NOAA-21 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 5.6 |
| b89841bf-44fb-3142-997f-d1104156faa4 | -15.30007 | -46.29068 | 2025-10-03 03:45:00 | NOAA-21 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| f65abdf9-e8c7-3da2-bda7-e229f86649b3 | -13.74311 | -47.98866 | 2025-10-03 03:45:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 8d600e3c-b703-36a9-abfb-7d2db8f33423 | -10.82247 | -46.58823 | 2025-10-03 03:45:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 3613b100-8bb5-305c-b699-b6be0d218422 | -14.1983 | -46.10992 | 2025-10-03 03:45:00 | NOAA-21 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 761cb8e8-48db-363e-8254-3fa67a4da8af | -15.20804 | -47.18416 | 2025-10-03 03:45:00 | NOAA-21 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| ec7f7ea8-e180-3ab2-b6a6-e219466a7eb4 | -13.33561 | -47.59976 | 2025-10-03 03:45:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| c1866052-bdce-3d25-86ce-6b829384ded4 | -15.22043 | -47.1846 | 2025-10-03 03:45:00 | NOAA-21 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 5.7 |
| d910fb5a-b3c6-371b-b91a-d48bd1d146cd | -13.3216 | -47.19087 | 2025-10-03 03:45:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 78144518-8a90-3fcb-9242-8f65976354d2 | -11.85746 | -44.96132 | 2025-10-03 03:45:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 4.2 |
| b14b5183-7f17-39fc-bd98-2760367fd9bd | -11.2138 | -41.59469 | 2025-10-03 03:45:00 | NOAA-21 | JOÃO DOURADO | BAHIA | Brasil | 2918357 | 29 | 33 | nan | nan | nan | Caatinga | 3.1 |
| 76089c0c-1285-3eab-82d9-42b1ca1b8e43 | -9.90958 | -43.72942 | 2025-10-03 03:45:00 | NOAA-21 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 22.7 |
| 6135bd97-24f3-397c-9e96-ea8ffb25d4bf | -14.59875 | -46.71973 | 2025-10-03 03:45:00 | NOAA-21 | ALVORADA DO NORTE | GOIÁS | Brasil | 5200803 | 52 | 33 | nan | nan | nan | Cerrado | 4.0 |
| f793fc33-cb2c-389e-8dc6-1340040bdd96 | -14.32765 | -45.86856 | 2025-10-03 03:45:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 1c48f980-8f74-3c49-ad26-48549c7e3108 | -13.75607 | -48.07373 | 2025-10-03 03:45:00 | NOAA-21 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 17.3 |
| 3cc50378-34bc-379a-86bf-e2e8b9978a6c | -15.30229 | -46.38577 | 2025-10-03 03:45:00 | NOAA-21 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 2db8b4e1-e78f-3247-8168-5111f23cde00 | -14.66009 | -48.25133 | 2025-10-03 03:45:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 2c24319c-5d88-311a-a518-6d6d7e148f17 | -11.11337 | -47.85757 | 2025-10-03 03:45:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 3972f90f-e128-39a5-962b-55dea06cfe0e | -13.13818 | -47.89841 | 2025-10-03 03:45:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| b3a202f0-cec1-3072-8658-31dba6f9925b | -9.95483 | -48.77464 | 2025-10-03 03:45:00 | NOAA-21 | BARROLÂNDIA | TOCANTINS | Brasil | 1703107 | 17 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 5a922216-7d21-3951-9ac4-f426194ad70f | -13.74079 | -48.00881 | 2025-10-03 03:45:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 6a00fa90-6fdb-3228-8953-add3811efe92 | -14.38284 | -45.95265 | 2025-10-03 03:45:00 | NOAA-21 | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 08a55a24-4841-301c-9a79-014e06c88b40 | -14.29265 | -45.88515 | 2025-10-03 03:45:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 5dbe0c49-b687-3465-a045-661178e2d12e | -11.63552 | -45.06513 | 2025-10-03 03:45:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 0b83a72d-280b-343f-bb96-03a9f3bd73e2 | -11.59164 | -47.62706 | 2025-10-03 03:45:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 7257941a-0a42-37d4-9c4b-5810714038d6 | -11.13778 | -43.40466 | 2025-10-03 03:45:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Caatinga | 6.6 |
| 0b797ff8-4d5a-308f-b8ec-c20d8b32f5b5 | -14.97538 | -49.97121 | 2025-10-03 03:45:00 | NOAA-21 | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 4.5 |
| ce57d6ae-309f-3b43-8a5b-f1161d208b08 | -9.06355 | -46.64589 | 2025-10-03 03:45:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| e7ad74c7-1372-3f57-a03f-a02857a6db6d | -15.27676 | -47.91735 | 2025-10-03 03:45:00 | NOAA-21 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 79c92998-83e2-3350-9265-dd2e7e274ec1 | -15.95478 | -43.30863 | 2025-10-03 03:45:00 | NOAA-21 | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 07afa344-9048-33e8-ac60-6893f2fe0a37 | -11.48845 | -45.11162 | 2025-10-03 03:45:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| bcb0d80d-e372-391f-9241-0dd0c6d874c8 | -14.89757 | -48.34934 | 2025-10-03 03:45:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 4.6 |
| d084624a-6eb7-37f4-824a-8004861afb94 | -11.85232 | -44.95862 | 2025-10-03 03:45:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 9d1899b5-b2f4-3b34-9200-697c8c8c6438 | -13.8526 | -47.93126 | 2025-10-03 03:45:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 10b069be-671e-3367-9f09-d0d8d5badfd2 | -14.67724 | -48.07905 | 2025-10-03 03:45:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.9 |
| b629d79c-6840-3cf6-b15a-5fe30baa386a | -11.50294 | -43.50273 | 2025-10-03 03:45:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 5e4964d1-ff7b-3897-ab95-fed2a332932e | -13.30158 | -47.26141 | 2025-10-03 03:45:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 9ad61e3b-58a2-354e-8d11-5daf46aec711 | -14.67322 | -48.06918 | 2025-10-03 03:45:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 05536cb3-02db-3ce4-96dc-01305e8da637 | -11.817 | -45.03948 | 2025-10-03 03:45:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 63df59f3-0205-3929-96b5-cec83d425917 | -13.96424 | -48.17454 | 2025-10-03 03:45:00 | NOAA-21 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 3.3 |
| f9ad70f0-28cb-38ee-9b83-7367131d6ea4 | -14.37837 | -45.93401 | 2025-10-03 03:45:00 | NOAA-21 | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| f80d7673-1f63-320c-a01b-f5463bebc362 | -12.90004 | -46.9348 | 2025-10-03 03:45:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| c57eab6a-3044-321d-9f3c-4eedf7ab2b06 | -11.14604 | -43.4113 | 2025-10-03 03:45:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Caatinga | 4.6 |
| 7758dd7e-543f-346a-b91c-7b6a079c9ada | -15.94883 | -46.21918 | 2025-10-03 03:45:00 | NOAA-21 | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 51577aeb-366d-30e8-90bd-f84373137206 | -11.46597 | -45.03459 | 2025-10-03 03:45:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 6bcc156c-c7a8-30b3-abd8-c4356d040249 | -14.72899 | -48.1185 | 2025-10-03 03:45:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 872c0c58-0f12-3ee8-94e9-6bcd7bfb7431 | -9.58761 | -43.32515 | 2025-10-03 03:45:00 | NOAA-21 | CAMPO ALEGRE DE LOURDES | BAHIA | Brasil | 2905909 | 29 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 6b1f5a9a-bcd1-3f90-b3f1-18dd57954484 | -12.90318 | -46.93881 | 2025-10-03 03:45:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| be123820-caaa-308e-b71f-b7ae9b55d01e | -11.11005 | -47.84243 | 2025-10-03 03:45:00 | NOAA-21 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 4.4 |
| bbb35b82-474d-373f-b531-d95eb4dc5eab | -13.40242 | -42.64679 | 2025-10-03 03:45:00 | NOAA-21 | MACAÚBAS | BAHIA | Brasil | 2919801 | 29 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 20d623fc-a28d-3230-a23f-41145e5bba6c | -13.13081 | -47.843 | 2025-10-03 03:45:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 5.7 |
| fac500ae-86a1-3930-810f-479697a14111 | -12.83937 | -46.86006 | 2025-10-03 03:45:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| d9b5062b-a11a-3605-95a9-5d450ceabaf3 | -13.97905 | -48.16259 | 2025-10-03 03:45:00 | NOAA-21 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 5.9 |
| a577cc62-52bf-3aba-8552-88c1eceec15e | -11.62591 | -45.03315 | 2025-10-03 03:45:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 0fdcfa4e-fcd0-3b5f-9d20-8cd7a9f5e505 | -15.27768 | -47.91287 | 2025-10-03 03:45:00 | NOAA-21 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 10.0 |
| dcc97529-d35c-395e-aea6-8fbfb1effc20 | -12.92607 | -45.08499 | 2025-10-03 03:45:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 668a20c1-3cb6-3d08-afb8-25001df15c07 | -13.33895 | -48.11459 | 2025-10-03 03:45:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| d6318890-1f4c-3f91-963f-e37fabad8c11 | -11.92041 | -46.28061 | 2025-10-03 03:45:00 | NOAA-21 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 33.5 |
| eb26f59f-56fe-3596-97e6-d06afe900b21 | -11.10487 | -47.83668 | 2025-10-03 03:45:00 | NOAA-21 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 9.2 |
| b29c187f-0f13-328d-a079-01435ce6f274 | -11.49366 | -44.99855 | 2025-10-03 03:45:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 95d24d24-2ec9-3457-8e74-26468792b31f | -16.3355 | -42.38406 | 2025-10-03 03:45:00 | NOAA-21 | RUBELITA | MINAS GERAIS | Brasil | 3156502 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| ef12ef32-92e4-38a2-914c-a29e273d88f3 | -14.90843 | -48.29782 | 2025-10-03 03:45:00 | NOAA-21 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 5de5a298-3c49-38da-bf9c-acb4f836f025 | -14.90174 | -46.9743 | 2025-10-03 03:45:00 | NOAA-21 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 3.8 |
| fe1e95d3-5ea8-3d52-a24f-9cc04e52aadf | -13.69392 | -48.61518 | 2025-10-03 03:45:00 | NOAA-21 | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |


[Clique aqui para ver as próximas entradas](README24.md)
