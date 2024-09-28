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

## Dados Diários - Página 33

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| d5493982-4b90-398e-b37b-c2fe05bcfec7 | -18.48586 | -42.21899 | 2024-09-28 03:32:00 | NOAA-20 | NACIP RAYDAN | MINAS GERAIS | Brasil | 3144201 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| 9666d038-c80f-3dd4-98c6-a3ac9d4153df | -18.48477 | -42.22444 | 2024-09-28 03:32:00 | NOAA-20 | NACIP RAYDAN | MINAS GERAIS | Brasil | 3144201 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| b4ee1e58-ede7-3830-9cb2-094210a4a7bc | -18.48167 | -42.19176 | 2024-09-28 03:32:00 | NOAA-20 | NACIP RAYDAN | MINAS GERAIS | Brasil | 3144201 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.4 |
| 188b7eb6-7181-329f-9883-a3c2d287b4e1 | -18.47717 | -42.19019 | 2024-09-28 03:32:00 | NOAA-20 | NACIP RAYDAN | MINAS GERAIS | Brasil | 3144201 | 31 | 33 | nan | nan | nan | Mata Atlântica | 8.2 |
| e1ca3aac-5ab5-3313-ba93-39194698c90f | -18.47463 | -42.18788 | 2024-09-28 03:32:00 | NOAA-20 | NACIP RAYDAN | MINAS GERAIS | Brasil | 3144201 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| e200a12e-1635-3f6b-b0a5-567a4bd3d1c4 | -20.88927 | -42.41583 | 2024-09-28 03:32:00 | NOAA-20 | MIRADOURO | MINAS GERAIS | Brasil | 3142106 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.2 |
| fdaa7d52-b052-3d68-b1e5-1b3fe5905167 | -20.88835 | -42.42044 | 2024-09-28 03:32:00 | NOAA-20 | MIRADOURO | MINAS GERAIS | Brasil | 3142106 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.2 |
| f34aaa1f-9163-3e58-ac3e-70a403ee9367 | -20.88486 | -42.41452 | 2024-09-28 03:32:00 | NOAA-20 | MIRADOURO | MINAS GERAIS | Brasil | 3142106 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.2 |
| ce1a38d1-3f41-3c59-858b-ee0125a96241 | -20.88393 | -42.41917 | 2024-09-28 03:32:00 | NOAA-20 | MIRADOURO | MINAS GERAIS | Brasil | 3142106 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.2 |
| ec5189c9-f8bf-366d-a014-a929bd9d3cd8 | -20.63649 | -42.26182 | 2024-09-28 03:32:00 | NOAA-20 | FERVEDOURO | MINAS GERAIS | Brasil | 3125952 | 31 | 33 | nan | nan | nan | Mata Atlântica | 5.2 |
| de1f70b3-e961-3e46-ae5d-3d7acce85911 | -20.63482 | -42.2593 | 2024-09-28 03:32:00 | NOAA-20 | FERVEDOURO | MINAS GERAIS | Brasil | 3125952 | 31 | 33 | nan | nan | nan | Mata Atlântica | 5.9 |
| 4d6d62e7-c865-3b09-949c-5c091854899b | -20.63388 | -42.26411 | 2024-09-28 03:32:00 | NOAA-20 | FERVEDOURO | MINAS GERAIS | Brasil | 3125952 | 31 | 33 | nan | nan | nan | Mata Atlântica | 6.4 |
| 7768c5e6-0097-3170-89f8-2268fdc7b3cb | -20.63203 | -42.26085 | 2024-09-28 03:32:00 | NOAA-20 | FERVEDOURO | MINAS GERAIS | Brasil | 3125952 | 31 | 33 | nan | nan | nan | Mata Atlântica | 5.2 |
| a3fd9f34-2398-391d-8785-214f7d02070c | -19.99939 | -42.40624 | 2024-09-28 03:32:00 | NOAA-20 | RAUL SOARES | MINAS GERAIS | Brasil | 3154002 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.3 |
| 5edd3c94-16a4-3b54-b756-940d892b01c7 | -19.99835 | -42.41145 | 2024-09-28 03:32:00 | NOAA-20 | RAUL SOARES | MINAS GERAIS | Brasil | 3154002 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.9 |
| 38e5a7db-22e8-3a62-8d1a-870ccbfdadf0 | -19.99384 | -42.41026 | 2024-09-28 03:32:00 | NOAA-20 | RAUL SOARES | MINAS GERAIS | Brasil | 3154002 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.9 |
| 9ac6ba1c-18fc-32c1-945f-6837b314f3fc | -19.99283 | -42.41528 | 2024-09-28 03:32:00 | NOAA-20 | RAUL SOARES | MINAS GERAIS | Brasil | 3154002 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.9 |
| 87ea7a20-142a-33f8-8a17-bda99bdca13c | -19.98934 | -42.409 | 2024-09-28 03:32:00 | NOAA-20 | RAUL SOARES | MINAS GERAIS | Brasil | 3154002 | 31 | 33 | nan | nan | nan | Mata Atlântica | 5.3 |
| 6e47c2f9-6a78-30e4-9890-675c200294aa | -19.87732 | -42.16592 | 2024-09-28 03:32:00 | NOAA-20 | CARATINGA | MINAS GERAIS | Brasil | 3113404 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 02463c74-45ce-3ae5-9bb3-c8fe5ee17fd5 | -19.87657 | -42.16219 | 2024-09-28 03:32:00 | NOAA-20 | CARATINGA | MINAS GERAIS | Brasil | 3113404 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.9 |
| b59ad54c-6f9e-36d2-9d0c-2a7715b3459a | -19.86662 | -42.16519 | 2024-09-28 03:32:00 | NOAA-20 | CARATINGA | MINAS GERAIS | Brasil | 3113404 | 31 | 33 | nan | nan | nan | Mata Atlântica | 6.9 |
| 713dcd86-d72d-30a3-9cc1-447e1e8134b0 | -19.866 | -42.36194 | 2024-09-28 03:32:00 | NOAA-20 | BOM JESUS DO GALHO | MINAS GERAIS | Brasil | 3107802 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 002b42d3-b01d-3269-a44d-0413940d3a04 | -19.86252 | -42.35564 | 2024-09-28 03:32:00 | NOAA-20 | BOM JESUS DO GALHO | MINAS GERAIS | Brasil | 3107802 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.9 |
| b9229849-db69-3f06-a242-10eb686be714 | -19.82886 | -41.94228 | 2024-09-28 03:32:00 | NOAA-20 | CARATINGA | MINAS GERAIS | Brasil | 3113404 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.0 |
| ad1d6bd2-29c3-3458-8b38-a43d01ab6db1 | -19.82754 | -41.93959 | 2024-09-28 03:32:00 | NOAA-20 | CARATINGA | MINAS GERAIS | Brasil | 3113404 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.4 |
| 7e16daa7-f63c-3a11-8758-f1069f0d445f | -19.82336 | -42.40988 | 2024-09-28 03:32:00 | NOAA-20 | CÓRREGO NOVO | MINAS GERAIS | Brasil | 3120003 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| 77d746db-1a69-3082-8f7e-b62fde19f8bd | -19.81881 | -42.40884 | 2024-09-28 03:32:00 | NOAA-20 | CÓRREGO NOVO | MINAS GERAIS | Brasil | 3120003 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| bcc299d8-7d60-3e25-af84-6dbb85e9d736 | -19.8178 | -42.41392 | 2024-09-28 03:32:00 | NOAA-20 | CÓRREGO NOVO | MINAS GERAIS | Brasil | 3120003 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| de56e547-a2ab-3dd5-8a04-b05b6ce6c96b | -19.7841 | -41.95868 | 2024-09-28 03:32:00 | NOAA-20 | CARATINGA | MINAS GERAIS | Brasil | 3113404 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 8bf9231e-6848-3afc-a059-26d65446fe8d | -20.87638 | -43.22189 | 2024-09-28 03:32:00 | NOAA-20 | BRÁS PIRES | MINAS GERAIS | Brasil | 3108701 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 9177e344-3257-3f7f-af75-427569e056d1 | -20.81987 | -43.32668 | 2024-09-28 03:32:00 | NOAA-20 | SENHORA DE OLIVEIRA | MINAS GERAIS | Brasil | 3166006 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.9 |
| a3986e86-3184-3a28-988c-0afa8308d09e | -20.7155 | -43.0149 | 2024-09-28 03:32:00 | NOAA-20 | PORTO FIRME | MINAS GERAIS | Brasil | 3152303 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| e856be8c-4875-3b71-ab95-0e1a0bfa588c | -20.71085 | -43.01383 | 2024-09-28 03:32:00 | NOAA-20 | PORTO FIRME | MINAS GERAIS | Brasil | 3152303 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 66538043-7078-3cab-ab29-1770b27d208f | -20.64299 | -43.58295 | 2024-09-28 03:32:00 | NOAA-20 | ITAVERAVA | MINAS GERAIS | Brasil | 3133907 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 94e6b951-51a2-38b2-be08-01771594e45b | -20.61594 | -42.89766 | 2024-09-28 03:32:00 | NOAA-20 | TEIXEIRAS | MINAS GERAIS | Brasil | 3168507 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| 41c41948-e986-3dd5-9c17-452e85f17a9a | -20.61394 | -42.89463 | 2024-09-28 03:32:00 | NOAA-20 | TEIXEIRAS | MINAS GERAIS | Brasil | 3168507 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| fa1e910c-bd80-37f3-9bbd-8335803fbbcc | -20.61288 | -42.89992 | 2024-09-28 03:32:00 | NOAA-20 | TEIXEIRAS | MINAS GERAIS | Brasil | 3168507 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.4 |
| d40bfdc0-9428-3640-a0f9-7aa4099cb40e | -20.61131 | -42.89659 | 2024-09-28 03:32:00 | NOAA-20 | TEIXEIRAS | MINAS GERAIS | Brasil | 3168507 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| 08625202-bf5b-31aa-9177-e09130156a4d | -20.45558 | -42.92298 | 2024-09-28 03:32:00 | NOAA-20 | PONTE NOVA | MINAS GERAIS | Brasil | 3152105 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| d4e27608-1876-357b-abfb-3de07568ea76 | -20.45448 | -42.92842 | 2024-09-28 03:32:00 | NOAA-20 | PONTE NOVA | MINAS GERAIS | Brasil | 3152105 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| dc075a22-701e-3123-a752-c21261694c6d | -20.45091 | -42.92199 | 2024-09-28 03:32:00 | NOAA-20 | PONTE NOVA | MINAS GERAIS | Brasil | 3152105 | 31 | 33 | nan | nan | nan | Mata Atlântica | 5.9 |
| 11ab8e11-fc59-3f87-938d-3c474866d59d | -20.44982 | -42.9274 | 2024-09-28 03:32:00 | NOAA-20 | PONTE NOVA | MINAS GERAIS | Brasil | 3152105 | 31 | 33 | nan | nan | nan | Mata Atlântica | 5.9 |
| 807476b8-04d9-3a34-802e-826efcc4f9b1 | -20.14369 | -43.48274 | 2024-09-28 03:32:00 | NOAA-20 | MARIANA | MINAS GERAIS | Brasil | 3140001 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.5 |
| 22f5ec0c-fe87-3477-9c46-03e9ba5d482a | -20.12094 | -43.44507 | 2024-09-28 03:32:00 | NOAA-20 | CATAS ALTAS | MINAS GERAIS | Brasil | 3115359 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| 2ad1c235-7f8e-3253-8be9-64d614d19896 | -20.1197 | -43.45113 | 2024-09-28 03:32:00 | NOAA-20 | CATAS ALTAS | MINAS GERAIS | Brasil | 3115359 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| eed6ed95-9d84-36f3-9288-9e4f6afeb932 | -20.11626 | -43.44321 | 2024-09-28 03:32:00 | NOAA-20 | CATAS ALTAS | MINAS GERAIS | Brasil | 3115359 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.0 |
| edd3f7d3-4538-3506-937e-af081ea3043a | -20.11509 | -43.44891 | 2024-09-28 03:32:00 | NOAA-20 | CATAS ALTAS | MINAS GERAIS | Brasil | 3115359 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.0 |
| c7203a48-f726-3740-98e8-c1ad248f59a0 | -20.11359 | -43.45619 | 2024-09-28 03:32:00 | NOAA-20 | CATAS ALTAS | MINAS GERAIS | Brasil | 3115359 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.5 |
| 62cb87f4-5676-36ce-a33f-b31886b135f9 | -19.87319 | -43.17926 | 2024-09-28 03:32:00 | NOAA-20 | RIO PIRACICABA | MINAS GERAIS | Brasil | 3155702 | 31 | 33 | nan | nan | nan | Mata Atlântica | 9.4 |
| 09e652bb-0f55-30d7-be24-138fbdb4372b | -19.87224 | -43.18394 | 2024-09-28 03:32:00 | NOAA-20 | RIO PIRACICABA | MINAS GERAIS | Brasil | 3155702 | 31 | 33 | nan | nan | nan | Mata Atlântica | 10.2 |
| 2ab2932b-436f-3109-88e0-672414c17543 | -19.87127 | -43.1887 | 2024-09-28 03:32:00 | NOAA-20 | RIO PIRACICABA | MINAS GERAIS | Brasil | 3155702 | 31 | 33 | nan | nan | nan | Mata Atlântica | 10.2 |
| 0a5c5af8-1680-3eb7-87e2-3ff05d899ec3 | -19.86852 | -43.17762 | 2024-09-28 03:32:00 | NOAA-20 | JOÃO MONLEVADE | MINAS GERAIS | Brasil | 3136207 | 31 | 33 | nan | nan | nan | Mata Atlântica | 9.4 |
| 5626a9ad-ff26-386c-9a50-4a71ae5131f7 | -19.86753 | -43.18248 | 2024-09-28 03:32:00 | NOAA-20 | JOÃO MONLEVADE | MINAS GERAIS | Brasil | 3136207 | 31 | 33 | nan | nan | nan | Mata Atlântica | 10.2 |
| 1c8b2770-a7db-394c-8c0c-98b8c309b814 | -19.8665 | -43.18756 | 2024-09-28 03:32:00 | NOAA-20 | JOÃO MONLEVADE | MINAS GERAIS | Brasil | 3136207 | 31 | 33 | nan | nan | nan | Mata Atlântica | 10.2 |
| 65185458-3883-3b9a-8953-f0ee21562f96 | -19.86382 | -43.17612 | 2024-09-28 03:32:00 | NOAA-20 | JOÃO MONLEVADE | MINAS GERAIS | Brasil | 3136207 | 31 | 33 | nan | nan | nan | Mata Atlântica | 6.2 |
| c67e4f20-23bd-3005-8d8f-59c334192420 | -19.62854 | -42.84746 | 2024-09-28 03:32:00 | NOAA-20 | ANTÔNIO DIAS | MINAS GERAIS | Brasil | 3103009 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.6 |
| 417d584f-73f9-3401-9134-cc76da26e461 | -19.62815 | -42.84584 | 2024-09-28 03:32:00 | NOAA-20 | ANTÔNIO DIAS | MINAS GERAIS | Brasil | 3103009 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.3 |
| 00f5f615-dc0f-3fca-bcbf-6e425c68bbfd | -19.62704 | -42.8514 | 2024-09-28 03:32:00 | NOAA-20 | ANTÔNIO DIAS | MINAS GERAIS | Brasil | 3103009 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| e0c5f8de-3239-3b65-9ed9-064defe2bea8 | -19.6268 | -42.92759 | 2024-09-28 03:32:00 | NOAA-20 | ANTÔNIO DIAS | MINAS GERAIS | Brasil | 3103009 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 6240e54d-5083-397f-bd16-48a2a8c50cac | -19.6034 | -42.79773 | 2024-09-28 03:32:00 | NOAA-20 | ANTÔNIO DIAS | MINAS GERAIS | Brasil | 3103009 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 6190b9da-e4e7-3564-b608-5c3b2ff961aa | -19.60242 | -42.80259 | 2024-09-28 03:32:00 | NOAA-20 | ANTÔNIO DIAS | MINAS GERAIS | Brasil | 3103009 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.4 |
| 4af9a6ed-62cb-3327-8111-63fefab1b9c8 | -19.51575 | -42.88918 | 2024-09-28 03:32:00 | NOAA-20 | ANTÔNIO DIAS | MINAS GERAIS | Brasil | 3103009 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.8 |
| 0f785af0-091d-372c-8369-48516705b38d | -19.51467 | -42.89265 | 2024-09-28 03:32:00 | NOAA-20 | ANTÔNIO DIAS | MINAS GERAIS | Brasil | 3103009 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.0 |
| b1a7bc71-6e39-31ce-abcb-5817ed576bbe | -19.51454 | -42.89507 | 2024-09-28 03:32:00 | NOAA-20 | ANTÔNIO DIAS | MINAS GERAIS | Brasil | 3103009 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.8 |
| 2362ce1e-89f9-323b-b48f-1083d25daf83 | -21.03816 | -42.66865 | 2024-09-28 03:32:00 | NOAA-20 | GUIRICEMA | MINAS GERAIS | Brasil | 3129004 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.4 |
| f20100fb-ed9b-31a4-931f-dbfbc2937c1f | -21.03701 | -42.6744 | 2024-09-28 03:32:00 | NOAA-20 | GUIRICEMA | MINAS GERAIS | Brasil | 3129004 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.4 |
| 6e971310-9d82-37bc-a9ef-f2aee5e1dc4d | -21.03472 | -42.66222 | 2024-09-28 03:32:00 | NOAA-20 | GUIRICEMA | MINAS GERAIS | Brasil | 3129004 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.0 |
| 6317ce87-1b08-35c5-a34f-5c6ab3cd0b09 | -21.03359 | -42.66785 | 2024-09-28 03:32:00 | NOAA-20 | GUIRICEMA | MINAS GERAIS | Brasil | 3129004 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.4 |
| 397ad15b-11ba-3976-8a5a-7b5ca14bbd29 | -21.03248 | -42.67333 | 2024-09-28 03:32:00 | NOAA-20 | GUIRICEMA | MINAS GERAIS | Brasil | 3129004 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.4 |
| d9c6623a-f075-3c7e-bbe9-ee89b428f3c5 | -21.03004 | -42.66195 | 2024-09-28 03:32:00 | NOAA-20 | GUIRICEMA | MINAS GERAIS | Brasil | 3129004 | 31 | 33 | nan | nan | nan | Mata Atlântica | 5.4 |
| 4020ee09-565a-3270-86c2-289dc983ceaa | -21.029 | -42.66711 | 2024-09-28 03:32:00 | NOAA-20 | GUIRICEMA | MINAS GERAIS | Brasil | 3129004 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.4 |
| e0bd3e0f-6a79-3248-8191-f225f376f00f | -21.02795 | -42.67229 | 2024-09-28 03:32:00 | NOAA-20 | GUIRICEMA | MINAS GERAIS | Brasil | 3129004 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.4 |
| c7c979a0-8819-3957-b32c-62b8316e6b1d | -21.02686 | -42.67769 | 2024-09-28 03:32:00 | NOAA-20 | GUIRICEMA | MINAS GERAIS | Brasil | 3129004 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| ce503e50-db0f-3c07-994d-25360ee4c287 | -21.01328 | -42.67451 | 2024-09-28 03:32:00 | NOAA-20 | GUIRICEMA | MINAS GERAIS | Brasil | 3129004 | 31 | 33 | nan | nan | nan | Mata Atlântica | 14.8 |
| 0d216d37-992c-3b84-b545-02245a962fa4 | -21.00871 | -42.67366 | 2024-09-28 03:32:00 | NOAA-20 | GUIRICEMA | MINAS GERAIS | Brasil | 3129004 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 73980e61-ad05-319a-a48d-01bdefe11625 | -18.51445 | -43.88828 | 2024-09-28 03:32:00 | NOAA-20 | GOUVEIA | MINAS GERAIS | Brasil | 3127602 | 31 | 33 | nan | nan | nan | Cerrado | 3.8 |
| f0692aac-7d3b-3ede-b4c7-f8e0db697e80 | -18.51376 | -43.89165 | 2024-09-28 03:32:00 | NOAA-20 | GOUVEIA | MINAS GERAIS | Brasil | 3127602 | 31 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 5b790c2d-2e1e-36ba-9555-d6a2cb0f5e6b | -18.49917 | -43.88422 | 2024-09-28 03:32:00 | NOAA-20 | MONJOLOS | MINAS GERAIS | Brasil | 3142502 | 31 | 33 | nan | nan | nan | Cerrado | 12.0 |
| ebc37974-2554-3c05-8e57-828f6f8dc0c4 | -18.4748 | -43.84655 | 2024-09-28 03:32:00 | NOAA-20 | GOUVEIA | MINAS GERAIS | Brasil | 3127602 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| fa589baa-1872-33af-8fe4-bf2ae1422565 | -18.3688 | -44.01335 | 2024-09-28 03:32:00 | NOAA-20 | MONJOLOS | MINAS GERAIS | Brasil | 3142502 | 31 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 4a40308c-8dc9-3abc-a19b-a71129948a88 | -18.3638 | -44.01126 | 2024-09-28 03:32:00 | NOAA-20 | MONJOLOS | MINAS GERAIS | Brasil | 3142502 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| e5456a3a-6aca-3c69-bdd9-a18a3dce6a8a | -18.3628 | -44.01606 | 2024-09-28 03:32:00 | NOAA-20 | MONJOLOS | MINAS GERAIS | Brasil | 3142502 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 06014f23-8af7-329c-89d6-f59b80b33c1f | -18.35844 | -44.01088 | 2024-09-28 03:32:00 | NOAA-20 | MONJOLOS | MINAS GERAIS | Brasil | 3142502 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 3a8e6e1f-ffbe-3543-9bce-0ae36d1c0a64 | -18.35753 | -44.01524 | 2024-09-28 03:32:00 | NOAA-20 | MONJOLOS | MINAS GERAIS | Brasil | 3142502 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 3f5bc2a1-9549-376a-90c1-9e7462e882bd | -18.3552 | -44.00037 | 2024-09-28 03:32:00 | NOAA-20 | MONJOLOS | MINAS GERAIS | Brasil | 3142502 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 38c96388-9b1e-31e2-9362-1b7e85366d72 | -18.35446 | -44.00395 | 2024-09-28 03:32:00 | NOAA-20 | MONJOLOS | MINAS GERAIS | Brasil | 3142502 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 2c496832-2cd6-338d-9350-25c271231728 | -18.05218 | -44.38033 | 2024-09-28 03:32:00 | NOAA-20 | AUGUSTO DE LIMA | MINAS GERAIS | Brasil | 3104809 | 31 | 33 | nan | nan | nan | Cerrado | 25.4 |
| f3e7e688-1f98-3e76-82b6-f52c5dd3e2d5 | -18.05149 | -44.3836 | 2024-09-28 03:32:00 | NOAA-20 | AUGUSTO DE LIMA | MINAS GERAIS | Brasil | 3104809 | 31 | 33 | nan | nan | nan | Cerrado | 12.0 |
| 07064a8a-2ebb-31b3-b4fe-23c85732fdd8 | -18.05081 | -44.38683 | 2024-09-28 03:32:00 | NOAA-20 | AUGUSTO DE LIMA | MINAS GERAIS | Brasil | 3104809 | 31 | 33 | nan | nan | nan | Cerrado | 12.0 |
| 41a9f249-f7c9-335a-99b7-6a04ca51d59f | -18.05012 | -44.39009 | 2024-09-28 03:32:00 | NOAA-20 | AUGUSTO DE LIMA | MINAS GERAIS | Brasil | 3104809 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 74ce5402-5d4f-36f9-b337-5495cb7d4509 | -18.04683 | -44.37912 | 2024-09-28 03:32:00 | NOAA-20 | AUGUSTO DE LIMA | MINAS GERAIS | Brasil | 3104809 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| bea9288e-65e4-3d0b-953f-c2a89da75c97 | -18.04545 | -44.38565 | 2024-09-28 03:32:00 | NOAA-20 | AUGUSTO DE LIMA | MINAS GERAIS | Brasil | 3104809 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| f62380a5-4514-3f4c-8ebc-1f8d9834f0fd | -19.09678 | -43.45238 | 2024-09-28 03:32:00 | NOAA-20 | CONCEIÇÃO DO MATO DENTRO | MINAS GERAIS | Brasil | 3117504 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.0 |
| 1cb8d56f-4874-3a0b-a1b4-46327c2c7c93 | -19.09556 | -43.45826 | 2024-09-28 03:32:00 | NOAA-20 | CONCEIÇÃO DO MATO DENTRO | MINAS GERAIS | Brasil | 3117504 | 31 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 4e096c1a-b5a8-3df8-b3c8-42211c38f618 | -19.0955 | -43.45747 | 2024-09-28 03:32:00 | NOAA-20 | CONCEIÇÃO DO MATO DENTRO | MINAS GERAIS | Brasil | 3117504 | 31 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 796dcbbf-34cc-39bb-b91b-3229825629b3 | -18.60335 | -43.4044 | 2024-09-28 03:32:00 | NOAA-20 | SERRO | MINAS GERAIS | Brasil | 3167103 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 6edcb7ca-8ccd-3a93-9a92-35f02a9bc2ed | -18.60272 | -43.40745 | 2024-09-28 03:32:00 | NOAA-20 | SERRO | MINAS GERAIS | Brasil | 3167103 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 599bdffd-4915-3931-97e7-753a97722ce7 | -18.60209 | -43.41055 | 2024-09-28 03:32:00 | NOAA-20 | SERRO | MINAS GERAIS | Brasil | 3167103 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| e4b74399-215c-3ad6-9d1c-2a63a249f325 | -18.59776 | -43.40628 | 2024-09-28 03:32:00 | NOAA-20 | SERRO | MINAS GERAIS | Brasil | 3167103 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| c77fb502-dde5-3ada-9380-162f020c1220 | -18.59709 | -43.40953 | 2024-09-28 03:32:00 | NOAA-20 | SERRO | MINAS GERAIS | Brasil | 3167103 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |


[Clique aqui para ver as próximas entradas](README34.md)
