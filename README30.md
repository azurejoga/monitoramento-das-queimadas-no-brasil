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

## Dados Diários - Página 30

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| ff7cd867-8980-3c2e-93fd-43a1225d4dc0 | -6.09055 | -59.92662 | 2025-08-13 05:27:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 8ecae2fd-3d7b-35b2-bda7-72ccba3418d0 | -7.06834 | -59.20204 | 2025-08-13 05:27:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 5f73f07e-d3d1-392e-b697-a15bd4fdcb1d | -6.89444 | -59.14696 | 2025-08-13 05:27:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 41.3 |
| efd83f47-6d0a-3d1f-8696-a9671ccf1e03 | -2.90994 | -48.25383 | 2025-08-13 05:27:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 15.5 |
| 258de9ac-29b6-36c4-a909-45ede38b7240 | -6.90906 | -59.1235 | 2025-08-13 05:27:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 04cf9583-ed2e-33fa-8dab-4bd1862abd32 | -7.07778 | -59.19736 | 2025-08-13 05:27:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 925b8512-04bd-34f7-b150-326de6ad101d | -6.96805 | -59.28031 | 2025-08-13 05:27:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 97d4cbd8-77e6-345b-92f1-2b5aa11d2342 | -7.14324 | -60.12439 | 2025-08-13 05:27:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 4.8 |
| cc524dc1-58ca-3157-9067-42873edd3190 | -7.06508 | -59.2083 | 2025-08-13 05:27:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| facc4654-1106-30f2-b80e-2627e8bf7315 | -6.90781 | -59.13184 | 2025-08-13 05:27:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 8.4 |
| b7bd60e5-fc80-3e69-a5d4-3ba48b2c08f5 | -6.88909 | -59.13329 | 2025-08-13 05:27:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 19.4 |
| 024482d0-f9df-3135-87b5-31df6b81af60 | -7.13977 | -60.12387 | 2025-08-13 05:27:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 0e2b8daa-8875-38e2-af35-840bd3b4c7db | -7.25767 | -57.63741 | 2025-08-13 05:27:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 75849a42-4f51-3cf5-98f0-a7fbb24f07c1 | -6.10554 | -59.92119 | 2025-08-13 05:27:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 5f17b921-4d52-33c4-987f-bba771063738 | -6.89083 | -59.14641 | 2025-08-13 05:27:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 39.8 |
| 34406e6d-75ea-3c51-ac3d-8e1f537b0c10 | -2.91029 | -48.25262 | 2025-08-13 05:27:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| eabd21da-ec66-32a3-98af-f8bf42bc272c | -6.07257 | -59.93595 | 2025-08-13 05:27:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 76c66949-88af-31af-9acd-ff40033f355b | -6.87761 | -59.13585 | 2025-08-13 05:27:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 10.3 |
| 292be5b1-0fa5-30cd-89d0-7b5f4286bd7c | -7.06345 | -59.20982 | 2025-08-13 05:27:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 20df520f-0046-37e7-acbc-bbe6d65715f1 | -6.88485 | -59.13693 | 2025-08-13 05:27:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 10.3 |
| d2aa884f-6b33-3e75-9992-d000360ec484 | -6.974 | -59.28969 | 2025-08-13 05:27:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| b976a96f-9710-3aab-9784-faaa66c9aacc | -6.89507 | -59.14275 | 2025-08-13 05:27:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 41.3 |
| 0e12fcb8-f61c-3506-9574-13e48bede68e | -6.08997 | -59.93042 | 2025-08-13 05:27:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 4cbd6b6f-51aa-3553-8102-425710aebbdf | -6.89757 | -59.12605 | 2025-08-13 05:27:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 7.9 |
| a03777e5-b65c-3070-98ab-330a87f50338 | -6.89271 | -59.13383 | 2025-08-13 05:27:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 19.4 |
| 8974876b-485e-32c8-bf61-dbd98b47ccef | -6.89633 | -59.13437 | 2025-08-13 05:27:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 18.8 |
| 9d6b2a80-3301-3bb1-a2ed-488a992b5dba | -7.09485 | -60.02279 | 2025-08-13 05:27:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 49161c09-bdfa-3314-b22a-636593c8ade7 | -6.91177 | -59.63239 | 2025-08-13 05:27:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 922c385b-2137-3818-b47f-846db5746c3d | -7.09715 | -60.03105 | 2025-08-13 05:27:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.9 |
| f2499680-c593-3c74-86d3-839d14b8a4cc | -6.09106 | -59.93091 | 2025-08-13 05:27:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| f8f816db-6737-34da-9049-04af8f25041d | -6.88609 | -59.12855 | 2025-08-13 05:27:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.1 |
| f54a4818-095c-30f6-a1c9-10229815be41 | -6.88359 | -59.14533 | 2025-08-13 05:27:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 22.5 |
| 06281f37-7304-3f1f-b8e2-cb494cfc7ccb | -7.09079 | -60.02608 | 2025-08-13 05:27:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.9 |
| b6b39223-2b55-3572-b7f9-030867c65c1a | -6.90231 | -59.14384 | 2025-08-13 05:27:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 10.0 |
| 1a333b75-f54b-365f-8790-c621a2b514f4 | -6.69403 | -59.13651 | 2025-08-13 05:27:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 23a4cafd-a803-377b-abd1-a8b62a600f4c | -6.91142 | -59.1324 | 2025-08-13 05:27:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 11.8 |
| 60c27198-762c-36f7-abc0-c8ef0ae4985e | -7.09833 | -60.02331 | 2025-08-13 05:27:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 5.3 |
| d1cfdb6c-b5f3-3d20-972b-4e05eda1f65a | -6.07198 | -59.93975 | 2025-08-13 05:27:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| eb718f72-5355-3995-87ae-e824fe454dc7 | -6.88422 | -59.14112 | 2025-08-13 05:27:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 22.5 |
| d4ddd00d-5fe2-3ecb-bb58-dd1b50da3a52 | -6.09047 | -59.9347 | 2025-08-13 05:27:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c70fbabe-3ae4-325a-a952-0b093649c91b | -6.89333 | -59.12966 | 2025-08-13 05:27:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 11.0 |
| 0604f7c4-0633-3b34-9037-1187ea954985 | -6.6934 | -59.14066 | 2025-08-13 05:27:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 91a8084f-04c9-348c-92ee-ec9cfe8679f9 | -6.97462 | -59.28555 | 2025-08-13 05:27:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 1577d6aa-6700-3a15-8864-7f4c576713ed | -7.06472 | -59.20151 | 2025-08-13 05:27:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| fb02b67e-e62d-340f-a6ce-04708f18d3b0 | -6.87823 | -59.13165 | 2025-08-13 05:27:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 10.3 |
| 0ac5bb22-cd43-344c-8b84-9143d09ab5bc | -6.88721 | -59.14586 | 2025-08-13 05:27:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 39.8 |
| 314b965e-eb2f-3929-9718-a71bec1f4f79 | -6.06852 | -59.93922 | 2025-08-13 05:27:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 610ac9f9-40c5-380b-9ad1-c387c14502b7 | -3.21853 | -60.60087 | 2025-08-13 05:27:00 | NOAA-20 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 4d2d5705-22a7-3ac9-b5bf-9bccfa2cc508 | -6.90119 | -59.12659 | 2025-08-13 05:27:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 7.9 |
| ea4c405e-16a8-374f-a549-49dba9f294bd | -6.86675 | -59.13426 | 2025-08-13 05:27:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 4.0 |
| ede22aba-be0c-379b-853b-1a6ff26d3061 | -6.91471 | -59.63688 | 2025-08-13 05:27:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 33253bec-49fb-377b-9689-6a5e913d6225 | -7.07132 | -59.2067 | 2025-08-13 05:27:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 994a3d54-c430-3340-96b7-cdc5e7a9c385 | -5.88646 | -57.74704 | 2025-08-13 05:27:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 99a5c506-ad76-3596-ab91-260f0df40718 | -7.09138 | -60.02224 | 2025-08-13 05:27:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.9 |
| e8a953cc-219d-3138-89b8-b0e83d16bcef | -6.87511 | -59.15266 | 2025-08-13 05:27:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 16.7 |
| b6c1e8bc-9990-3fae-8bdf-5cbdf00229cf | -7.13572 | -60.12715 | 2025-08-13 05:27:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 96d76391-5de1-342c-8432-bfe2bdb3223a | -7.07354 | -59.20103 | 2025-08-13 05:27:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 0e0f6e98-5aa5-3792-9580-dc010ae39ae9 | -6.88297 | -59.14954 | 2025-08-13 05:27:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 26.8 |
| 0daa0696-3172-38fc-a77b-dd3076e4ad10 | -6.1113 | -59.92988 | 2025-08-13 05:27:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 6f0bc868-1331-3ba2-a393-84cb9b1db6a8 | -7.06992 | -59.20052 | 2025-08-13 05:27:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a02cbaf3-dbf6-3d04-99f7-1febd9127135 | -6.87399 | -59.13533 | 2025-08-13 05:27:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 10.3 |
| 89d15b7c-04a1-3e9d-b765-777cf3579229 | -5.89213 | -57.74497 | 2025-08-13 05:27:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 9.0 |
| 466c38aa-440e-31ee-800f-ac1ef318c7b4 | -7.09196 | -60.01836 | 2025-08-13 05:27:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 8aff39da-7880-3a83-af2c-baaea5129f54 | -6.09804 | -59.92389 | 2025-08-13 05:27:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 51919330-bdc2-387b-a0c5-cc14eacd6a1e | -5.88336 | -57.74144 | 2025-08-13 05:27:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 98221f3a-4a4d-339c-b8b5-8802ef08baf9 | -5.84633 | -59.9262 | 2025-08-13 05:27:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 1b54323f-22e5-3da5-be3f-668941a056e1 | -6.97103 | -59.28501 | 2025-08-13 05:27:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 315eaf8a-fe83-3101-8bc4-18322fcc781c | -7.12474 | -60.12935 | 2025-08-13 05:27:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 87bbe861-1a49-351c-84d9-2cdffb4e6915 | -6.87997 | -59.1448 | 2025-08-13 05:27:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 22.5 |
| 457fae5e-9c52-3a9c-a16d-932f4a46ff48 | -2.9034 | -48.25151 | 2025-08-13 05:27:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 16.7 |
| ff4ae465-34fb-3e60-acca-e7e33b4483df | -7.14384 | -60.12055 | 2025-08-13 05:27:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 62f036f1-5876-3a0e-8920-b44dc840e3c1 | -7.13166 | -60.13045 | 2025-08-13 05:27:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 007baeb9-2cfc-3115-a1d5-67829d736c8b | -6.90843 | -59.12767 | 2025-08-13 05:27:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 8.4 |
| 6866f567-90b8-3d9e-8e0c-4c695ade79d1 | -5.85389 | -59.90023 | 2025-08-13 05:27:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 39de126d-6cc3-376d-ba63-dfd050d89712 | -6.89146 | -59.1422 | 2025-08-13 05:27:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 39.8 |
| c94bc040-85cb-313d-a862-12d10110c557 | -6.88971 | -59.1291 | 2025-08-13 05:27:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 11.0 |
| 3592cc59-7afd-309b-9708-f5e4dfc0054d | -5.88722 | -57.74208 | 2025-08-13 05:27:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 9bc360a9-9927-3055-9361-100495bb3a33 | -7.12997 | -60.11843 | 2025-08-13 05:27:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| f6d000cb-cb78-3726-849f-a50cafd5de80 | -6.90057 | -59.13075 | 2025-08-13 05:27:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 7.9 |
| f372a5b6-7d93-38f8-b7ac-1dd578a64cc5 | -6.87935 | -59.14901 | 2025-08-13 05:27:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 26.8 |
| 537552ac-966d-34d4-8be5-3cc08fdf43db | -6.86974 | -59.139 | 2025-08-13 05:27:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 5.9 |
| f92a3f3f-c0fb-32aa-8ad4-51cf3b1e5ac3 | -6.88547 | -59.13274 | 2025-08-13 05:27:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 10.3 |
| 5606795a-044b-3227-864e-5cf1353d8eae | -6.97165 | -59.28086 | 2025-08-13 05:27:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 1c660fb8-055c-3737-94b1-2f2b5191668e | -6.10842 | -59.92554 | 2025-08-13 05:27:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 5db13ff3-253a-3cca-bdf3-7ef14228e7f1 | -7.07716 | -59.20155 | 2025-08-13 05:27:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| d2eb6b48-5885-35ae-a624-dd0f04b89d6e | -6.88123 | -59.13639 | 2025-08-13 05:27:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 10.3 |
| 9c1eb6d8-1147-3914-9630-18eb7c4a4afa | -7.06409 | -59.20567 | 2025-08-13 05:27:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 307a9b0f-7ed0-3aa2-b407-7ef6e322e759 | -6.89208 | -59.13801 | 2025-08-13 05:27:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 19.4 |
| a25829cf-4fd4-3281-85c5-b63b9460f590 | -7.11496 | -59.84285 | 2025-08-13 05:27:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 8d777c96-2043-3162-ad60-78d1d0cb890b | -2.9021 | -48.25894 | 2025-08-13 05:27:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 16.7 |
| e871dbcc-cf87-3ec6-bb19-5f1d2ffa95f0 | -7.1282 | -60.12991 | 2025-08-13 05:27:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 0220694d-1183-3d38-afa0-1d7bc6c10a0c | -7.09427 | -60.02665 | 2025-08-13 05:27:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 3a211415-fda1-3794-b0fa-1b40cc0c1106 | -6.09977 | -59.93585 | 2025-08-13 05:27:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 3.1 |
| ec988a45-52c5-3728-8e4a-995850d71d49 | -6.1015 | -59.92444 | 2025-08-13 05:27:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 49029a17-b23f-3e1f-8387-d6eaadd03367 | -6.10035 | -59.93205 | 2025-08-13 05:27:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 3.1 |
| ca2d2176-1d94-3f8c-aee2-84bf0c0d9019 | -6.87636 | -59.14427 | 2025-08-13 05:27:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 9.0 |
| b676826e-30ad-3d05-9654-9a998e732e2a | -3.42992 | -49.04622 | 2025-08-13 05:27:00 | NOAA-20 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 39f36da1-dcb1-30e0-8964-08ad1c81737c | -6.87573 | -59.14847 | 2025-08-13 05:27:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 16.7 |
| edb906d8-a921-3473-97db-bdf2225fe5b8 | -7.06569 | -59.20415 | 2025-08-13 05:27:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c614395a-ed30-3656-9d91-dda6118f3008 | -5.84346 | -59.92189 | 2025-08-13 05:27:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |


[Clique aqui para ver as próximas entradas](README31.md)
