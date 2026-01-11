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

## Dados Diários - Página 7

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 92b00aeb-d86c-3098-b65e-bc25aa5b36d5 | -13.34309 | -41.33449 | 2026-01-11 04:40:00 | NPP-375D | IBICOARA | BAHIA | Brasil | 2912202 | 29 | 33 | nan | nan | nan | Caatinga | 3.4 |
| 3bb31e67-3a5a-3614-8b9a-c2883acc8673 | -13.43036 | -43.85958 | 2026-01-11 04:40:00 | NPP-375D | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| c7ac3632-e0f1-3cc0-911e-384608fa92be | -12.91184 | -52.52418 | 2026-01-11 04:40:00 | NPP-375D | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 272c1a44-8552-340e-8c3e-3e28e8be56b6 | -10.84607 | -44.03513 | 2026-01-11 04:40:00 | NPP-375D | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| b5a18be0-a0ca-33f8-ba9f-782fef1e6ed3 | -13.66567 | -53.94859 | 2026-01-11 04:40:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 5733b563-3e88-3cd8-afe5-65de8ad2a819 | -11.83619 | -49.19857 | 2026-01-11 04:40:00 | NPP-375D | CARIRI DO TOCANTINS | TOCANTINS | Brasil | 1703867 | 17 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 55d28f18-4acc-3106-a0fb-b25802a202b0 | -13.7675 | -46.63431 | 2026-01-11 04:40:00 | NPP-375D | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 99b14649-f503-39e8-a8c5-575b54654875 | -12.91112 | -52.52837 | 2026-01-11 04:40:00 | NPP-375D | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 15cb17b9-bf50-37a6-99bb-1a76363452f6 | -16.05437 | -47.21466 | 2026-01-11 04:40:00 | NPP-375D | CABECEIRA GRANDE | MINAS GERAIS | Brasil | 3109451 | 31 | 33 | nan | nan | nan | Cerrado | 0.3 |
| da24f3e2-25b9-3fee-a155-25da0741ec2d | -12.89928 | -52.52789 | 2026-01-11 04:40:00 | NPP-375D | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 3e1a5911-5559-3307-a10f-b520a640bc2a | -11.83675 | -49.19505 | 2026-01-11 04:40:00 | NPP-375D | CARIRI DO TOCANTINS | TOCANTINS | Brasil | 1703867 | 17 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 287aae30-c82e-3625-b339-9232f914cc6b | -12.50766 | -46.67733 | 2026-01-11 04:40:00 | NPP-375D | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 0dadc3ff-e694-3216-9418-7103109e389b | -13.67333 | -53.95003 | 2026-01-11 04:40:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| d18de6ae-7372-3a6d-ad2f-701b81ce6b42 | -12.89998 | -52.5237 | 2026-01-11 04:40:00 | NPP-375D | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| c9298bed-301f-3b0a-94d5-7667f1310938 | -12.90646 | -52.52917 | 2026-01-11 04:40:00 | NPP-375D | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 9f2493f7-8235-37bd-8840-5f3d8a8d4d49 | -12.91075 | -52.52563 | 2026-01-11 04:40:00 | NPP-375D | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 795100fe-5a3f-3dc6-96ee-7bfe7826186c | -16.05078 | -47.21407 | 2026-01-11 04:40:00 | NPP-375D | CABECEIRA GRANDE | MINAS GERAIS | Brasil | 3109451 | 31 | 33 | nan | nan | nan | Cerrado | 0.3 |
| 21f0c67d-ad1d-3a7c-8029-1b66e43d8dda | -16.10024 | -56.75236 | 2026-01-11 04:40:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 9aaa3dea-cf78-3b7f-b4d5-cfbd951cd054 | -12.90357 | -52.52433 | 2026-01-11 04:40:00 | NPP-375D | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Amazônia | 3.7 |
| a0ff554c-715f-3803-aa3c-652781eb6bcd | -11.16844 | -43.30766 | 2026-01-11 04:40:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 1718ed64-b28e-309f-8867-ae504b124072 | -15.26055 | -42.88143 | 2026-01-11 04:40:00 | NPP-375D | MONTE AZUL | MINAS GERAIS | Brasil | 3142908 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 708bf539-c36c-38f0-9518-691f8bc4c931 | -10.98527 | -47.73497 | 2026-01-11 04:40:00 | NPP-375D | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 68826574-4253-3b94-985b-2d192b907ae4 | -11.84007 | -49.19559 | 2026-01-11 04:40:00 | NPP-375D | CARIRI DO TOCANTINS | TOCANTINS | Brasil | 1703867 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 61629470-69e1-3f52-b8a1-8f1ab5d33437 | -11.8373 | -49.19152 | 2026-01-11 04:40:00 | NPP-375D | CARIRI DO TOCANTINS | TOCANTINS | Brasil | 1703867 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 9cb8e0e1-8134-3f43-997b-4f5b790d853f | -18.81917 | -51.60697 | 2026-01-11 04:42:00 | NPP-375D | ITAJÁ | GOIÁS | Brasil | 5210802 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| efca710a-f35e-3c68-bb05-6120037a1416 | -20.14563 | -46.84499 | 2026-01-11 04:42:00 | NPP-375D | SACRAMENTO | MINAS GERAIS | Brasil | 3156908 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 7b59557d-9cb2-301f-be86-c01b153a9b1d | -18.59552 | -46.55339 | 2026-01-11 04:42:00 | NPP-375D | PATOS DE MINAS | MINAS GERAIS | Brasil | 3148004 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 1a382b59-4543-3917-a8a0-ca7f2eec5d0c | -20.24468 | -46.39747 | 2026-01-11 04:42:00 | NPP-375D | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| c2deae19-0c0a-3e5b-ac98-8d1f356dbeb4 | -20.25764 | -46.51415 | 2026-01-11 04:42:00 | NPP-375D | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| c218f992-5d9b-372b-a42c-bd36a1e37012 | -20.24069 | -46.39723 | 2026-01-11 04:42:00 | NPP-375D | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| bc5b00ba-219f-3c16-9179-0a323526891a | -18.81857 | -51.61066 | 2026-01-11 04:42:00 | NPP-375D | ITAJÁ | GOIÁS | Brasil | 5210802 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 9546e5ff-42d1-3dc0-9f2e-79366e9a5d3f | -20.24208 | -46.48001 | 2026-01-11 04:42:00 | NPP-375D | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 5.2 |
| bbfb4bb1-801a-3c4e-8cbf-ddd4d3f60e42 | -18.59412 | -46.55169 | 2026-01-11 04:42:00 | NPP-375D | PATOS DE MINAS | MINAS GERAIS | Brasil | 3148004 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| d65047fd-ef15-3dae-b0fe-54d50f8ce19f | -19.40933 | -43.50305 | 2026-01-11 04:42:00 | NPP-375D | JABOTICATUBAS | MINAS GERAIS | Brasil | 3134608 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 93745b2d-5618-34cc-9f21-71c00563a27b | -20.2414 | -46.48531 | 2026-01-11 04:42:00 | NPP-375D | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 11.2 |
| d946c680-600f-33e2-8276-37b0dad3cb0b | -20.24145 | -46.39127 | 2026-01-11 04:42:00 | NPP-375D | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| cecb14a8-8444-39f1-8453-607e4a002dba | -20.24791 | -46.4968 | 2026-01-11 04:42:00 | NPP-375D | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 1cd5d604-86ea-3892-b80c-15c8c44e7929 | -17.62209 | -50.35297 | 2026-01-11 04:42:00 | NPP-375D | TURVELÂNDIA | GOIÁS | Brasil | 5221551 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 32fb6ea5-eb60-3dad-b84b-608505f29123 | -20.25372 | -46.51361 | 2026-01-11 04:42:00 | NPP-375D | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 20689903-f5be-37d9-bdde-4e33ecf9d441 | -19.0672 | -44.32874 | 2026-01-11 04:42:00 | NPP-375D | CORDISBURGO | MINAS GERAIS | Brasil | 3118908 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 8d5d7c35-4ca7-3bef-a2bc-c21dbd2d60f2 | -20.12899 | -46.85221 | 2026-01-11 04:42:00 | NPP-375D | SACRAMENTO | MINAS GERAIS | Brasil | 3156908 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 8f941720-0de6-3198-8d9b-113ea76255c2 | -20.24466 | -46.49104 | 2026-01-11 04:42:00 | NPP-375D | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 7a0a3925-65df-3328-9274-391d621b0eee | -20.2342 | -46.47905 | 2026-01-11 04:42:00 | NPP-375D | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 5.1 |
| ab164a6e-df12-3a86-8c20-d58b3141bde0 | -20.23882 | -46.4743 | 2026-01-11 04:42:00 | NPP-375D | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 3fa8ef52-9e12-36d1-b812-56d6925bff23 | -20.2544 | -46.50838 | 2026-01-11 04:42:00 | NPP-375D | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 4aa42dd2-a6b1-37cc-9558-42f6266b3561 | -18.81583 | -51.60638 | 2026-01-11 04:42:00 | NPP-375D | ITAJÁ | GOIÁS | Brasil | 5210802 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 905359ed-c5d6-387b-b050-7a86b680ab82 | -18.81523 | -51.61007 | 2026-01-11 04:42:00 | NPP-375D | ITAJÁ | GOIÁS | Brasil | 5210802 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| c3751607-78ef-35de-9031-a3bac92cc607 | -20.23814 | -46.47957 | 2026-01-11 04:42:00 | NPP-375D | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 8fd10c02-42b8-3b4b-9545-3a86502897d0 | -20.24859 | -46.4916 | 2026-01-11 04:42:00 | NPP-375D | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 6.3 |
| c280dcf3-fdf7-3d0e-89ff-336aa8b091bc | -23.39638 | -45.37507 | 2026-01-11 04:42:00 | NPP-375D | NATIVIDADE DA SERRA | SÃO PAULO | Brasil | 3532306 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.4 |
| ab9c2d93-cc0a-3020-8e62-117bdabb6924 | -20.13798 | -46.84362 | 2026-01-11 04:42:00 | NPP-375D | SACRAMENTO | MINAS GERAIS | Brasil | 3156908 | 31 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 2b19611b-214f-3c9c-82d2-25df00db41f4 | -20.14181 | -46.84432 | 2026-01-11 04:42:00 | NPP-375D | SACRAMENTO | MINAS GERAIS | Brasil | 3156908 | 31 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 2f09b9ed-fa28-3e41-9b5c-1cabe6e0aef4 | -18.82406 | -51.61921 | 2026-01-11 04:42:00 | NPP-375D | ITAJÁ | GOIÁS | Brasil | 5210802 | 52 | 33 | nan | nan | nan | Cerrado | 7.9 |
| 5b550f49-90c9-3565-bfc7-26aeca43fe1b | -20.24398 | -46.49626 | 2026-01-11 04:42:00 | NPP-375D | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 4fd8280f-6afb-33da-ae27-4e05d6d5f6a4 | -20.13416 | -46.84291 | 2026-01-11 04:42:00 | NPP-375D | SACRAMENTO | MINAS GERAIS | Brasil | 3156908 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 4b88fcd8-140b-307a-9fd1-ea151fce1f52 | -20.24534 | -46.48578 | 2026-01-11 04:42:00 | NPP-375D | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 84280bc6-0222-3587-a902-53803a713fbd | -20.13349 | -46.8479 | 2026-01-11 04:42:00 | NPP-375D | SACRAMENTO | MINAS GERAIS | Brasil | 3156908 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 221dc69e-1803-3e93-b11f-df228c786bb1 | 0.73041 | -51.41431 | 2026-01-11 04:55:00 | NOAA-20 | PORTO GRANDE | AMAPÁ | Brasil | 1600535 | 16 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 6e61a9e1-0c2f-39ab-a723-4f6c2692cc60 | 0.73097 | -51.41787 | 2026-01-11 04:55:00 | NOAA-20 | PORTO GRANDE | AMAPÁ | Brasil | 1600535 | 16 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 9876f183-a471-3c94-8e5f-a8caf882da4a | -5.4985 | -42.16455 | 2026-01-11 04:57:00 | NOAA-20 | ALTO LONGÁ | PIAUÍ | Brasil | 2200301 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 1e21c971-89d1-3a28-a48b-16dd29d518c7 | 0.68859 | -59.27997 | 2026-01-11 04:57:00 | NOAA-20 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 1.2 |
| afe073b5-3a2e-301b-b8e9-3bf5235537cc | -3.93861 | -40.70115 | 2026-01-11 04:57:00 | NOAA-20 | MUCAMBO | CEARÁ | Brasil | 2309003 | 23 | 33 | nan | nan | nan | Caatinga | 5.3 |
| 24b8d9d3-cd9f-3e5d-b68c-a30c18042f65 | -7.59022 | -45.89053 | 2026-01-11 04:57:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| a9aee710-6439-3bf1-bf9f-381327033d91 | -1.80771 | -53.60532 | 2026-01-11 04:57:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| a93e007a-7e93-3c32-b7cb-a67e20b37324 | -3.88728 | -50.01166 | 2026-01-11 04:57:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c858f512-be00-399a-837e-c3b244b0ea25 | -5.49762 | -42.16287 | 2026-01-11 04:57:00 | NOAA-20 | ALTO LONGÁ | PIAUÍ | Brasil | 2200301 | 22 | 33 | nan | nan | nan | Caatinga | 6.4 |
| 3f20c780-dd42-3999-89dd-0425c008d986 | -5.49923 | -42.15918 | 2026-01-11 04:57:00 | NOAA-20 | ALTO LONGÁ | PIAUÍ | Brasil | 2200301 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 5a5e218b-38c4-33e2-a35d-be817f8323b2 | -2.91956 | -51.40561 | 2026-01-11 04:57:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 83906bb6-5765-39ba-9797-7bb1a9506e71 | -4.7088 | -44.48261 | 2026-01-11 04:57:00 | NOAA-20 | SANTO ANTÔNIO DOS LOPES | MARANHÃO | Brasil | 2110302 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| e55e50d0-00ef-3761-91ed-b507216c496d | 0.35304 | -60.40913 | 2026-01-11 04:57:00 | NOAA-20 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 483af5e5-7f5e-3043-9741-89337dd54ec8 | -1.08417 | -46.77526 | 2026-01-11 04:57:00 | NOAA-20 | BRAGANÇA | PARÁ | Brasil | 1501709 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 32731a20-cd82-3584-ac9c-7b580f9176b9 | -7.48844 | -45.58178 | 2026-01-11 04:57:00 | NOAA-20 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 83d4ad41-0487-322e-858b-729591bd5dd5 | -7.41307 | -48.95029 | 2026-01-11 04:57:00 | NOAA-20 | ARAGUAÍNA | TOCANTINS | Brasil | 1702109 | 17 | 33 | nan | nan | nan | Amazônia | 0.8 |
| d6098f88-478f-3224-ba42-7fd7c4c28059 | -2.62191 | -43.10207 | 2026-01-11 04:57:00 | NOAA-20 | SANTO AMARO DO MARANHÃO | MARANHÃO | Brasil | 2110278 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 4e79c76a-9ca4-38ff-a6ac-79d4d22e5a49 | -5.13002 | -46.12399 | 2026-01-11 04:57:00 | NOAA-20 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| c9801da0-93b1-3aa2-bef7-5276328d76cd | -5.45886 | -45.28428 | 2026-01-11 04:57:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| d3e5bd99-3e5e-308f-a8a4-767591022911 | 0.86123 | -59.68584 | 2026-01-11 04:57:00 | NOAA-20 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 1b3b37a9-53e2-3ba6-8b33-c25dae9a6ccb | -2.93535 | -52.31136 | 2026-01-11 04:57:00 | NOAA-20 | VITÓRIA DO XINGU | PARÁ | Brasil | 1508357 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 5a7ab359-8faa-3607-b2c1-757ca3971354 | -5.96038 | -46.15113 | 2026-01-11 04:57:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 478b6747-2d03-3325-b176-44c58a313416 | -0.0897 | -51.27972 | 2026-01-11 04:57:00 | NOAA-20 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 27.3 |
| 91923da0-4485-3d70-ba3b-f3ce32c21067 | 0.64284 | -59.52451 | 2026-01-11 04:57:00 | NOAA-20 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 646fcf45-8297-3fc3-ad6e-6166ab7cac07 | -2.98904 | -52.36331 | 2026-01-11 04:57:00 | NOAA-20 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 98fc19a7-dc82-3898-8255-ff911feb6e97 | -2.98848 | -52.36684 | 2026-01-11 04:57:00 | NOAA-20 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| fe0dae4c-88d2-3d53-bfef-587be57723c9 | -4.64726 | -45.79392 | 2026-01-11 04:57:00 | NOAA-20 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 0c2f518d-ae3e-343a-97e5-0dace3643ad6 | -1.05552 | -47.13136 | 2026-01-11 04:57:00 | NOAA-20 | CAPANEMA | PARÁ | Brasil | 1502202 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| fb93ac9b-4d87-3c79-b6ce-7a01f8907cb8 | -3.5594 | -43.6568 | 2026-01-11 04:57:00 | NOAA-20 | NINA RODRIGUES | MARANHÃO | Brasil | 2107209 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| f171dc79-73fa-3018-a9b3-b2e1aeb31a10 | -5.28638 | -45.8261 | 2026-01-11 04:57:00 | NOAA-20 | ITAIPAVA DO GRAJAÚ | MARANHÃO | Brasil | 2105351 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 6a3ee88c-5b80-3241-9051-0c901756b409 | -0.02048 | -51.09757 | 2026-01-11 04:57:00 | NOAA-20 | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 0.8 |
| e5a34160-e155-3b17-aa56-d5ace70df4ab | -1.26777 | -45.74393 | 2026-01-11 04:57:00 | NOAA-20 | GODOFREDO VIANA | MARANHÃO | Brasil | 2104305 | 21 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 631756e8-2764-3af3-86b2-9fc6b881a854 | -1.16034 | -46.74537 | 2026-01-11 04:57:00 | NOAA-20 | BRAGANÇA | PARÁ | Brasil | 1501709 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| a1f100a3-6d04-3565-ad1a-b9e2c2167cb0 | -3.71206 | -47.20495 | 2026-01-11 04:57:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 2652dd3d-180c-3dd1-9d78-dd625c79459b | -1.26857 | -45.7388 | 2026-01-11 04:57:00 | NOAA-20 | GODOFREDO VIANA | MARANHÃO | Brasil | 2104305 | 21 | 33 | nan | nan | nan | Amazônia | 2.7 |
| b50253a8-f3af-3077-ae73-280d2416dcd5 | 1.1202 | -60.51272 | 2026-01-11 04:57:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 2a856a34-d6b3-3f18-a6c1-e5632cd69c7e | -5.13149 | -46.12552 | 2026-01-11 04:57:00 | NOAA-20 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| ecf0d6d4-cc25-3071-93ea-1b2062dbd62a | -2.91435 | -54.14732 | 2026-01-11 04:57:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 1edb4a17-903d-359e-a5ec-aa6d57d276b0 | -2.15367 | -53.65272 | 2026-01-11 04:57:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 4a7875c1-cb81-30cf-9324-3bde5da6dd7a | -1.84139 | -54.31441 | 2026-01-11 04:57:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 7633ea38-45af-33b1-b95c-4426ce23ff63 | -2.18752 | -52.01059 | 2026-01-11 04:57:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| c5abf17d-490c-3627-a559-d788bb7cf9ca | -5.4928 | -42.15835 | 2026-01-11 04:57:00 | NOAA-20 | ALTO LONGÁ | PIAUÍ | Brasil | 2200301 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 37f988df-fda5-3396-8535-32db5e3b78bd | -1.53482 | -54.53688 | 2026-01-11 04:57:00 | NOAA-20 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |


[Clique aqui para ver as próximas entradas](README8.md)
