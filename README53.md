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
| 944b1b04-d601-3b1d-94e8-ce4d079280d4 | -10.35965 | -44.97855 | 2025-10-07 04:36:00 | NPP-375D | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| b5c7d1f5-fd6d-30b9-acf2-af956855297c | -8.52793 | -54.85967 | 2025-10-07 04:36:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 347244c8-2366-3fd4-9334-00b1633afc38 | -8.8001 | -47.8611 | 2025-10-07 04:36:00 | NPP-375D | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 2bd3ed37-bcc7-38d7-8de0-99135ec9e72d | -6.1597 | -44.0922 | 2025-10-07 04:36:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| dd1bfd2f-b1b3-359f-993a-707d9b66cea5 | -6.50111 | -41.55307 | 2025-10-07 04:36:00 | NPP-375D | LAGOA DO SÍTIO | PIAUÍ | Brasil | 2205599 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 0c7e0e19-f729-3f81-978d-e66f1d92edaf | -7.69128 | -42.40649 | 2025-10-07 04:36:00 | NPP-375D | SÃO MIGUEL DO FIDALGO | PIAUÍ | Brasil | 2210391 | 22 | 33 | nan | nan | nan | Caatinga | 4.0 |
| 7a450529-1cf5-3392-a9e5-f42720fa576b | -9.59263 | -51.62218 | 2025-10-07 04:36:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 2408a735-17cd-322f-86be-8b550c256688 | -8.65122 | -46.29903 | 2025-10-07 04:36:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| cb4dd712-6fad-3b58-b301-9c88336e6b45 | -8.19503 | -44.20168 | 2025-10-07 04:36:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 94645290-a574-341a-ad28-a12c896d7076 | -9.03663 | -50.59507 | 2025-10-07 04:36:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| b7acb14b-639f-3156-b7e6-4850c51dcc39 | -7.46187 | -43.03273 | 2025-10-07 04:36:00 | NPP-375D | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 5d13f27e-72a1-3cdf-9acd-cc7366d4bcfe | -8.61694 | -44.92878 | 2025-10-07 04:36:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 13a78dd5-ad53-31da-9473-9edc8a581f21 | -7.69438 | -42.41499 | 2025-10-07 04:36:00 | NPP-375D | SÃO MIGUEL DO FIDALGO | PIAUÍ | Brasil | 2210391 | 22 | 33 | nan | nan | nan | Caatinga | 4.6 |
| fe336eae-b8c8-3bf1-87bb-77dfa35c70ea | -9.20388 | -47.84893 | 2025-10-07 04:36:00 | NPP-375D | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| f4e5ef3a-2c3f-3df1-9229-ebb51bbd5cc0 | -8.57705 | -46.23786 | 2025-10-07 04:36:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| d6128282-4823-3fbf-aa59-831e290537b7 | -8.30266 | -50.75074 | 2025-10-07 04:36:00 | NPP-375D | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 5d04fce0-d34b-3ed3-acd2-b2839029ba70 | -7.70118 | -42.39044 | 2025-10-07 04:36:00 | NPP-375D | SÃO MIGUEL DO FIDALGO | PIAUÍ | Brasil | 2210391 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 36b6fabf-d041-398c-a9da-5c7a039991de | -5.70662 | -44.83064 | 2025-10-07 04:36:00 | NPP-375D | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 61484535-3848-3513-9e38-33f4afbda2ef | -6.69998 | -42.86305 | 2025-10-07 04:36:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 3.0 |
| 38f407f2-7d04-30b6-b9d7-c3cdaeaa1b21 | -5.22705 | -43.79424 | 2025-10-07 04:36:00 | NPP-375D | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 8f0c3a72-d1cc-3a04-8909-10b041218d5c | -5.14116 | -43.82733 | 2025-10-07 04:36:00 | NPP-375D | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 35fc9d7b-07c3-3356-b4dc-1ba8c5b6cfaf | -8.91551 | -49.70921 | 2025-10-07 04:36:00 | NPP-375D | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 73c4452d-e61d-3796-a1a1-a1d95f0ecad2 | -6.90881 | -47.34894 | 2025-10-07 04:36:00 | NPP-375D | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 82978b11-83fc-3494-a224-af4f2a8379a3 | -8.20788 | -44.19393 | 2025-10-07 04:36:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 33cbb955-fd35-3319-b78d-3b13f52f681b | -5.15146 | -49.84768 | 2025-10-07 04:36:00 | NPP-375D | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| b949905e-f564-3052-b84e-04cf80f86e62 | -7.68163 | -42.41291 | 2025-10-07 04:36:00 | NPP-375D | SÃO MIGUEL DO FIDALGO | PIAUÍ | Brasil | 2210391 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 917f7034-0dbd-358a-afb8-df66484a57db | -8.54872 | -46.23731 | 2025-10-07 04:36:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 5ef09d4b-5181-36f7-ba59-416ba8cf778f | -6.16452 | -42.58938 | 2025-10-07 04:36:00 | NPP-375D | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 2.9 |
| f949e94c-2abf-3dc4-bfa7-806f5afef7b6 | -8.19749 | -44.21169 | 2025-10-07 04:36:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 4a5eede3-a080-3674-8441-c7c8a9f3c7bb | -5.099 | -46.15672 | 2025-10-07 04:36:00 | NPP-375D | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 291a6d3d-5547-3bb4-bcb6-8eea5955c94b | -8.61926 | -54.99503 | 2025-10-07 04:36:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ee435a73-9fca-3e29-a965-e0b7633919e8 | -4.59091 | -47.0362 | 2025-10-07 04:36:00 | NPP-375D | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 35b9f540-3fe0-3245-99b5-303a63da4455 | -4.11551 | -50.05217 | 2025-10-07 04:36:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 45570cde-3835-3c31-aaf7-0ccb9d658012 | -4.64534 | -50.56219 | 2025-10-07 04:36:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 1fcc2ea9-5e61-3e42-b8ef-ca8d47e86856 | -8.56702 | -44.63395 | 2025-10-07 04:36:00 | NPP-375D | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 3896f3c1-0e27-3f3e-8f61-16ab8419fbeb | -8.498 | -46.32771 | 2025-10-07 04:36:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| a48f54ca-33ea-33ac-9bb5-b304ec70c63a | -4.8704 | -50.90193 | 2025-10-07 04:36:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 8d97c10b-d4e5-3932-8d0c-fb8b316bfb97 | -10.41125 | -45.39101 | 2025-10-07 04:36:00 | NPP-375D | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 7.8 |
| a34b76a5-95a9-36a6-a0f0-b02ed8d41b06 | -5.22023 | -47.37306 | 2025-10-07 04:36:00 | NPP-375D | SÃO FRANCISCO DO BREJÃO | MARANHÃO | Brasil | 2110856 | 21 | 33 | nan | nan | nan | Amazônia | 2.5 |
| cb30bf32-5d14-35b4-850f-2fc64bc07d47 | -4.55322 | -46.67675 | 2025-10-07 04:36:00 | NPP-375D | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 554c38c1-559d-3bae-9eb3-9c15fe39616b | -9.02651 | -50.6992 | 2025-10-07 04:36:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 7a4e5871-5ebb-3084-848b-836bd42b09dc | -6.27751 | -42.92096 | 2025-10-07 04:36:00 | NPP-375D | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| b1046061-ab59-3f85-9a3e-dcdd57c35d92 | -6.32217 | -41.61249 | 2025-10-07 04:36:00 | NPP-375D | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 0ac6ac3b-408e-3bb3-b671-cbd6c8140d3d | -10.25615 | -44.3648 | 2025-10-07 04:36:00 | NPP-375D | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| e6b7aa36-e0e7-3952-8854-55ebd4bea345 | -8.46827 | -43.72489 | 2025-10-07 04:36:00 | NPP-375D | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 3.2 |
| ddd96000-cf51-3d7c-9cd5-476b59bdee5c | -8.68382 | -49.95451 | 2025-10-07 04:36:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 80f14150-329f-3c06-8c7e-52b71c6e0fd0 | -8.61851 | -44.92652 | 2025-10-07 04:36:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 4201fd7a-a155-3c54-b1e6-e55b0f4d8c5c | -8.55397 | -46.24958 | 2025-10-07 04:36:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 57849ef1-3256-3a06-8024-82f39b224cb7 | -5.80175 | -45.21568 | 2025-10-07 04:36:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 259c2ede-a79c-322b-ae6a-a6a9d853e2d8 | -7.70062 | -42.39441 | 2025-10-07 04:36:00 | NPP-375D | SÃO MIGUEL DO FIDALGO | PIAUÍ | Brasil | 2210391 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 59ce9573-495e-3aff-93d9-0e51c2767c7f | -9.92281 | -49.96435 | 2025-10-07 04:36:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 3c3f92b9-63d1-30ac-993b-52da79f8a809 | -3.66687 | -51.95058 | 2025-10-07 04:36:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 49f3b4c6-41d0-3072-b536-a7a68b681e66 | -4.91762 | -48.02524 | 2025-10-07 04:36:00 | NPP-375D | VILA NOVA DOS MARTÍRIOS | MARANHÃO | Brasil | 2112852 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 01ab3894-435a-3374-a78b-9b1ed5445e84 | -9.68364 | -48.3931 | 2025-10-07 04:36:00 | NPP-375D | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 6ed62063-d64d-324d-b803-ef7074b211ad | -5.68018 | -45.32607 | 2025-10-07 04:36:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| a97033c9-4987-3a6b-b22d-391c5d1b00b4 | -6.28153 | -42.92168 | 2025-10-07 04:36:00 | NPP-375D | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| f47d9c9f-2cf6-38e7-9666-a42b9cdbd54e | -7.77617 | -44.20085 | 2025-10-07 04:36:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| d42c1ea1-cfd7-3503-a75f-10fd5c9e7cd7 | -6.17151 | -51.15944 | 2025-10-07 04:36:00 | NPP-375D | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 4a0a499e-9e33-3b0f-9f64-867ff03a3ab7 | -7.7262 | -42.39824 | 2025-10-07 04:36:00 | NPP-375D | SÃO MIGUEL DO FIDALGO | PIAUÍ | Brasil | 2210391 | 22 | 33 | nan | nan | nan | Caatinga | 3.8 |
| 6ab0fa46-61e2-3eea-a2ca-28bd556565ce | -4.14714 | -47.66159 | 2025-10-07 04:36:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 067b5a78-3f86-39fd-a294-ca36acff177e | -6.64742 | -41.98865 | 2025-10-07 04:36:00 | NPP-375D | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 9dafdd4c-0b42-3d97-afca-558732be8f88 | -4.87449 | -50.89658 | 2025-10-07 04:36:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 58c2f3d4-4af6-3dc1-8b05-0422143433d1 | -8.10951 | -55.08773 | 2025-10-07 04:36:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 9f5b8fa9-8a62-30ba-8082-096d2e45fa4d | -8.52798 | -46.25719 | 2025-10-07 04:36:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 3662e004-d370-3561-bace-da6f17355a04 | -6.16584 | -42.59021 | 2025-10-07 04:36:00 | NPP-375D | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 4513a10a-95ef-38a2-b7a3-d6f0098c5766 | -8.95331 | -44.59995 | 2025-10-07 04:36:00 | NPP-375D | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 2c440db3-fe11-34db-853a-4ef3635e58c8 | -8.62 | -44.93371 | 2025-10-07 04:36:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 7.7 |
| 26ca9d84-292c-3049-b0b3-bf8b3bb7414c | -6.16145 | -44.08575 | 2025-10-07 04:36:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 97c2aa19-4006-3711-b28f-68c242b4bb3e | -5.39474 | -40.99051 | 2025-10-07 04:36:00 | NPP-375D | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 7.7 |
| b16c9819-d27a-375c-a1b6-fccbdb391027 | -4.91484 | -48.02126 | 2025-10-07 04:36:00 | NPP-375D | VILA NOVA DOS MARTÍRIOS | MARANHÃO | Brasil | 2112852 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 1b64b1b4-8bd5-3099-b3af-8debf775900e | -9.18269 | -47.8311 | 2025-10-07 04:36:00 | NPP-375D | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | 7.6 |
| 50f1c810-b358-3f23-85e1-4aef7344a1f2 | -8.62453 | -54.99137 | 2025-10-07 04:36:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b5e5f153-5b1c-3b36-86dd-206e256647fe | -8.60574 | -44.91116 | 2025-10-07 04:36:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 270e5fb2-dfd7-353f-a382-c3a349874b50 | -6.23758 | -43.27063 | 2025-10-07 04:36:00 | NPP-375D | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 2e5dc923-1039-398f-beb8-36584c6ee9cb | -9.03161 | -50.66835 | 2025-10-07 04:36:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 82c05375-d599-34a2-8ff0-7a43de8d932c | -5.50015 | -43.08065 | 2025-10-07 04:36:00 | NPP-375D | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 13.5 |
| 78d422b8-d6cd-33b2-bea1-9e06a07d9287 | -8.19925 | -44.22638 | 2025-10-07 04:36:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 100e4dab-f3fb-3995-bd0f-d208d04bcc3f | -7.14753 | -39.72122 | 2025-10-07 04:36:00 | NPP-375D | SANTANA DO CARIRI | CEARÁ | Brasil | 2312106 | 23 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 419d4daa-60ad-369d-885f-f879616bf8f9 | -7.15261 | -39.722 | 2025-10-07 04:36:00 | NPP-375D | SANTANA DO CARIRI | CEARÁ | Brasil | 2312106 | 23 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 1990f041-8092-3c4e-9509-b3bcc52a285e | -9.02019 | -50.69425 | 2025-10-07 04:36:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d52d75c4-27e9-3ccc-8b88-b1858371eb59 | -6.7184 | -42.85103 | 2025-10-07 04:36:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| f13f92a9-93be-3126-b38a-41f377653921 | -5.73569 | -42.53181 | 2025-10-07 04:36:00 | NPP-375D | BARRO DURO | PIAUÍ | Brasil | 2201408 | 22 | 33 | nan | nan | nan | Caatinga | 5.4 |
| a6793042-eb33-3f6f-ad2b-42f31eaa85c2 | -5.50239 | -43.06571 | 2025-10-07 04:36:00 | NPP-375D | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 31.8 |
| 4e84721b-f7d6-3fe0-8538-ee69f9cb1fa6 | -5.25422 | -46.5721 | 2025-10-07 04:36:00 | NPP-375D | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 2cf08583-fe54-3e2f-be2b-4345195413ed | -8.53562 | -54.85925 | 2025-10-07 04:36:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 37360008-9890-36b2-8ff4-dc1b7a3f2753 | -7.01792 | -42.78296 | 2025-10-07 04:36:00 | NPP-375D | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 632b10fe-a7f2-3d73-a8d3-11a95855433d | -5.60432 | -51.2245 | 2025-10-07 04:36:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 2046698d-9d08-3035-8ee5-565dd4c6a3e6 | -6.74033 | -50.83342 | 2025-10-07 04:36:00 | NPP-375D | ÁGUA AZUL DO NORTE | PARÁ | Brasil | 1500347 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| c70ec291-6f67-3094-a173-43da417153c6 | -5.74681 | -44.985 | 2025-10-07 04:36:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 79e57945-1220-38e1-a3f8-ceab664ca9eb | -9.96677 | -43.78332 | 2025-10-07 04:36:00 | NPP-375D | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 3.6 |
| f851ae6c-b44b-3cc2-9561-35805c2bb26f | -5.49694 | -43.07512 | 2025-10-07 04:36:00 | NPP-375D | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 21.8 |
| 69845567-6632-395a-8c32-1f7585ecedd6 | -6.65044 | -41.96814 | 2025-10-07 04:36:00 | NPP-375D | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 392963f5-e249-3b16-9af4-92b8f5ef351b | -5.65491 | -43.18957 | 2025-10-07 04:36:00 | NPP-375D | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 1680b6dd-65dc-322b-b4d8-00891b686156 | -9.16965 | -50.83355 | 2025-10-07 04:36:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 023a4cc7-c2b1-3e5f-b445-f93793db34bb | -4.87536 | -45.95922 | 2025-10-07 04:36:00 | NPP-375D | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 962f3208-b9e6-31c5-a08f-5db72fb721dd | -5.23004 | -43.79693 | 2025-10-07 04:36:00 | NPP-375D | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 5fa36fb9-0e2f-3008-999f-ab0ad7ce58a6 | -5.14983 | -46.12024 | 2025-10-07 04:36:00 | NPP-375D | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 7c797004-7287-3210-9c95-5bdc09a32801 | -5.23852 | -46.56236 | 2025-10-07 04:36:00 | NPP-375D | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 645d5501-42bd-359d-be08-2c6bf991a435 | -9.97997 | -48.01423 | 2025-10-07 04:36:00 | NPP-375D | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 7b85fe9f-eeaf-3ac9-b232-4d298bdc0332 | -9.0892 | -47.95747 | 2025-10-07 04:36:00 | NPP-375D | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |


[Clique aqui para ver as próximas entradas](README54.md)
