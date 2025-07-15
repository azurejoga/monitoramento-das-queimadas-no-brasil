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

## Dados Diários - Página 14

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 2a110285-af5f-3583-b514-c1c911814909 | -10.28515 | -47.61433 | 2025-07-15 04:10:00 | NPP-375D | LAGOA DO TOCANTINS | TOCANTINS | Brasil | 1711951 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| dd05d400-ede8-3799-b86e-93b1100cabc4 | -16.90055 | -52.67471 | 2025-07-15 04:12:00 | NPP-375D | DOVERLÂNDIA | GOIÁS | Brasil | 5207253 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 1f5fe757-86aa-3377-8176-d1d3690a5196 | -19.52285 | -44.26027 | 2025-07-15 04:12:00 | NPP-375D | SETE LAGOAS | MINAS GERAIS | Brasil | 3167202 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 28460274-3cf0-3fdb-bf17-a31db9bd7b17 | -15.74931 | -49.64405 | 2025-07-15 04:12:00 | NPP-375D | ITAGUARU | GOIÁS | Brasil | 5210604 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 8ff5476d-da0a-37bf-bddc-773c0f40d2d2 | -19.163 | -49.13864 | 2025-07-15 04:12:00 | NPP-375D | PRATA | MINAS GERAIS | Brasil | 3152808 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 896fa650-94b8-372b-a21e-b3f553b3014b | -18.40449 | -44.1907 | 2025-07-15 04:12:00 | NPP-375D | SANTO HIPÓLITO | MINAS GERAIS | Brasil | 3160603 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 53d9791d-5f04-3e8f-b1cc-ddafda916d52 | -15.23176 | -46.98746 | 2025-07-15 04:12:00 | NPP-375D | VILA BOA | GOIÁS | Brasil | 5222203 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 8a055348-cd33-3ea0-a636-10beebf858d3 | -18.40116 | -44.19013 | 2025-07-15 04:12:00 | NPP-375D | SANTO HIPÓLITO | MINAS GERAIS | Brasil | 3160603 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| a086c4cf-b3d9-341e-a60b-0109f5125415 | -15.23843 | -46.97625 | 2025-07-15 04:12:00 | NPP-375D | VILA BOA | GOIÁS | Brasil | 5222203 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| a3a3eff7-89de-358a-bfd9-fb20e1807ab1 | -15.6172 | -46.46343 | 2025-07-15 04:12:00 | NPP-375D | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| a31aa1f2-cd36-38e4-80c1-75c317560469 | -15.62004 | -46.46822 | 2025-07-15 04:12:00 | NPP-375D | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 9a744114-0be9-3136-bc8a-46035cf5c532 | -15.23711 | -46.97852 | 2025-07-15 04:12:00 | NPP-375D | VILA BOA | GOIÁS | Brasil | 5222203 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 6c836da4-c1c1-3f78-a079-57edb144647b | -14.58387 | -48.11947 | 2025-07-15 04:12:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| a556f117-1cb1-316c-a573-f6a0629b8e97 | -19.5375 | -44.0781 | 2025-07-15 04:12:00 | NPP-375D | MATOZINHOS | MINAS GERAIS | Brasil | 3141108 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 8d51ddec-b19a-37f9-ad58-0e078b98780c | -18.00914 | -45.75932 | 2025-07-15 04:12:00 | NPP-375D | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 6e88b9f0-47b4-3cfe-9d82-b691ff59f6fa | -20.14746 | -41.67091 | 2025-07-15 04:12:00 | NPP-375D | LAJINHA | MINAS GERAIS | Brasil | 3137700 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| ba673f14-021a-3158-b5ec-d3e22348602e | -14.57691 | -48.11297 | 2025-07-15 04:12:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 66459f71-6d74-3a32-bd9b-faca661979c2 | -15.24072 | -46.97941 | 2025-07-15 04:12:00 | NPP-375D | VILA BOA | GOIÁS | Brasil | 5222203 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 34955225-acdf-3057-825d-6fb28ca0f20d | -15.62359 | -46.46887 | 2025-07-15 04:12:00 | NPP-375D | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| f1b52b1c-f39c-387c-9719-690ad1eb8c45 | -15.07881 | -48.94668 | 2025-07-15 04:12:00 | NPP-375D | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 89a44b24-0d01-35d9-807f-786cc2d3a71a | -14.58088 | -48.11341 | 2025-07-15 04:12:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 51e776e2-ddaf-36a7-b2d7-51e68d482304 | -18.81674 | -45.74207 | 2025-07-15 04:12:00 | NPP-375D | TIROS | MINAS GERAIS | Brasil | 3168903 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| bfa4c1eb-d36e-3da5-a895-0a6cc84687ea | -19.15913 | -49.13781 | 2025-07-15 04:12:00 | NPP-375D | PRATA | MINAS GERAIS | Brasil | 3152808 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| f7e00efe-79f8-38f0-835a-3c398e489214 | -18.81737 | -45.73828 | 2025-07-15 04:12:00 | NPP-375D | TIROS | MINAS GERAIS | Brasil | 3168903 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| a1987aea-5599-3431-8ceb-eab47d9ab915 | -14.5888 | -48.11447 | 2025-07-15 04:12:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| b9c029a3-987b-3ceb-bc5b-cc98d2da0968 | -15.57002 | -47.85636 | 2025-07-15 04:12:00 | NPP-375D | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 47971c4f-39e7-3fff-b871-3322281fe851 | -19.43943 | -44.34018 | 2025-07-15 04:12:00 | NPP-375D | SETE LAGOAS | MINAS GERAIS | Brasil | 3167202 | 31 | 33 | nan | nan | nan | Cerrado | 0.3 |
| c2035740-6795-3b29-a1a0-21e101e6b31a | -15.22607 | -46.96052 | 2025-07-15 04:12:00 | NPP-375D | VILA BOA | GOIÁS | Brasil | 5222203 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 6eaaca3c-a955-3fa6-b87d-35309d81fbaf | -15.22671 | -46.97879 | 2025-07-15 04:12:00 | NPP-375D | VILA BOA | GOIÁS | Brasil | 5222203 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 6fd14d5f-d728-381f-94f9-c52285039470 | -15.23764 | -46.98095 | 2025-07-15 04:12:00 | NPP-375D | VILA BOA | GOIÁS | Brasil | 5222203 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 092538e5-61b9-308a-ac0e-161eb2928c71 | -15.22826 | -46.96971 | 2025-07-15 04:12:00 | NPP-375D | VILA BOA | GOIÁS | Brasil | 5222203 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 848140f6-3c37-30db-b46d-11ace40570aa | -15.23263 | -46.98256 | 2025-07-15 04:12:00 | NPP-375D | VILA BOA | GOIÁS | Brasil | 5222203 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 354a4383-4d81-3546-bfa5-2a37a5009ef0 | -15.22531 | -46.96497 | 2025-07-15 04:12:00 | NPP-375D | VILA BOA | GOIÁS | Brasil | 5222203 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 94fadb99-43b1-3ced-98da-4ef216d99435 | -15.22303 | -46.97834 | 2025-07-15 04:12:00 | NPP-375D | VILA BOA | GOIÁS | Brasil | 5222203 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 2e2c5f66-5216-3f78-8ee4-65e1b72552d5 | -18.00575 | -45.75869 | 2025-07-15 04:12:00 | NPP-375D | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 447742a1-e0aa-3366-b8a9-87dd67820572 | -19.58623 | -44.22613 | 2025-07-15 04:12:00 | NPP-375D | SETE LAGOAS | MINAS GERAIS | Brasil | 3167202 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 78545d60-8271-319e-aee7-426065a16f48 | -20.41557 | -43.55305 | 2025-07-15 04:12:00 | NPP-375D | OURO PRETO | MINAS GERAIS | Brasil | 3146107 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| f2ad7b27-37df-3155-90a1-6e57a438f223 | -15.7501 | -49.63983 | 2025-07-15 04:12:00 | NPP-375D | ITAGUARU | GOIÁS | Brasil | 5210604 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 84364e0b-a9cf-3a97-8195-b6fedb96c14e | -19.47014 | -44.29667 | 2025-07-15 04:12:00 | NPP-375D | SETE LAGOAS | MINAS GERAIS | Brasil | 3167202 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 6fc7613a-bf11-30c5-9296-e752cbb6fada | -18.73847 | -39.92591 | 2025-07-15 04:12:00 | NPP-375D | SÃO MATEUS | ESPÍRITO SANTO | Brasil | 3204906 | 32 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| d3189b48-83e0-31d9-ab05-7ef81352e115 | -15.44829 | -47.62422 | 2025-07-15 04:12:00 | NPP-375D | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| c91bde83-f3d6-30ee-8279-7e24e0f68eb1 | -15.23318 | -46.98506 | 2025-07-15 04:12:00 | NPP-375D | VILA BOA | GOIÁS | Brasil | 5222203 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 43cd5e5e-ef0e-3d4d-af0c-bb8b1e76c584 | -16.07112 | -43.64701 | 2025-07-15 04:12:00 | NPP-375D | CAPITÃO ENÉAS | MINAS GERAIS | Brasil | 3112703 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 2409ef4b-2367-3192-82c7-dc15004b5eaf | -15.44804 | -47.62669 | 2025-07-15 04:12:00 | NPP-375D | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| bfc0cc73-f1fd-330d-ace4-b2cfbabd320a | -20.14682 | -41.6754 | 2025-07-15 04:12:00 | NPP-375D | LAJINHA | MINAS GERAIS | Brasil | 3137700 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.7 |
| e8ce4958-5e2b-3e1c-9815-19a423080a09 | -16.90623 | -52.67267 | 2025-07-15 04:12:00 | NPP-375D | DOVERLÂNDIA | GOIÁS | Brasil | 5207253 | 52 | 33 | nan | nan | nan | Cerrado | 0.1 |
| 4cf0d950-9c10-3a97-8388-71ef0939859a | -15.22899 | -46.96542 | 2025-07-15 04:12:00 | NPP-375D | VILA BOA | GOIÁS | Brasil | 5222203 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 65b3358f-dcc0-38a1-8a84-68ea41df56fe | -19.51335 | -44.27745 | 2025-07-15 04:12:00 | NPP-375D | SETE LAGOAS | MINAS GERAIS | Brasil | 3167202 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 3a3e1882-7925-33d5-99b2-3a03d665879f | -14.58487 | -48.11376 | 2025-07-15 04:12:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 44ce3bea-ae77-3341-901d-89602cb2ddab | -23.36403 | -47.27696 | 2025-07-15 04:14:00 | NPP-375D | ITU | SÃO PAULO | Brasil | 3523909 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| c4b235b2-2ef2-3b7c-8187-b753aaa7a921 | -21.8621 | -56.75068 | 2025-07-15 04:14:00 | NPP-375D | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 53f93554-5586-3588-9b18-8c32b4dc6daf | -23.2083 | -49.41055 | 2025-07-15 04:14:00 | NPP-375D | PIRAJU | SÃO PAULO | Brasil | 3538808 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 03d30406-d563-39d8-ba62-a6a199036767 | -22.57804 | -44.07894 | 2025-07-15 04:14:00 | NPP-375D | VOLTA REDONDA | RIO DE JANEIRO | Brasil | 3306305 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| cca718a4-fadb-3562-9915-b2801b41d708 | -24.54416 | -51.85192 | 2025-07-15 04:14:00 | NPP-375D | PITANGA | PARANÁ | Brasil | 4119608 | 41 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 0feb13ac-b61c-312f-b8c6-555a2aa3d803 | -19.29252 | -55.16141 | 2025-07-15 04:14:00 | NPP-375D | RIO VERDE DE MATO GROSSO | MATO GROSSO DO SUL | Brasil | 5007406 | 50 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 7ca19589-9cdf-3315-998d-299f14aabcd5 | -21.62473 | -43.64775 | 2025-07-15 04:14:00 | NPP-375D | JUIZ DE FORA | MINAS GERAIS | Brasil | 3136702 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| f072fb2d-19ba-386a-aba3-32e84516a214 | -23.33635 | -46.13561 | 2025-07-15 04:14:00 | NPP-375D | GUARAREMA | SÃO PAULO | Brasil | 3518305 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| bbc6944d-6e8d-31d4-90c4-8c980316ec72 | -23.59223 | -47.43998 | 2025-07-15 04:14:00 | NPP-375D | VOTORANTIM | SÃO PAULO | Brasil | 3557006 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 7024978a-befe-3bff-bb39-3039d8bf71b7 | -20.37801 | -45.6038 | 2025-07-15 04:14:00 | NPP-375D | PAINS | MINAS GERAIS | Brasil | 3146503 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| b8efbe3c-ffef-3ccc-bfe7-29069b80ac0e | -20.37261 | -46.56372 | 2025-07-15 04:14:00 | NPP-375D | DELFINÓPOLIS | MINAS GERAIS | Brasil | 3121209 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 223bc0ab-db13-35ec-87b3-7514e3af7c99 | -20.96098 | -44.46721 | 2025-07-15 04:14:00 | NPP-375D | RITÁPOLIS | MINAS GERAIS | Brasil | 3156106 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 1280d931-4572-3017-98b8-b255e47a88b4 | -25.25072 | -49.92863 | 2025-07-15 04:14:00 | NPP-375D | PONTA GROSSA | PARANÁ | Brasil | 4119905 | 41 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 21551568-398f-38d4-974f-919d63e786dd | -22.92014 | -45.4144 | 2025-07-15 04:14:00 | NPP-375D | PINDAMONHANGABA | SÃO PAULO | Brasil | 3538006 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 124cf1cb-3371-392a-b3ed-961b04cb3753 | -20.76068 | -46.01983 | 2025-07-15 04:14:00 | NPP-375D | GUAPÉ | MINAS GERAIS | Brasil | 3128105 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 91bebe57-ee9d-396c-87a3-56d796e86505 | -21.2429 | -49.19831 | 2025-07-15 04:14:00 | NPP-375D | URUPÊS | SÃO PAULO | Brasil | 3556008 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.5 |
| 621aa5fb-8403-3d01-8580-28e306e7d11a | -20.7613 | -46.01605 | 2025-07-15 04:14:00 | NPP-375D | GUAPÉ | MINAS GERAIS | Brasil | 3128105 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 8085bf66-3320-3ad4-bfd6-12e912a15d0d | -23.5045 | -47.33633 | 2025-07-15 04:14:00 | NPP-375D | SOROCABA | SÃO PAULO | Brasil | 3552205 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 50cf8600-6beb-3760-ac5e-25657df97b62 | -21.13106 | -47.80198 | 2025-07-15 04:14:00 | NPP-375D | RIBEIRÃO PRETO | SÃO PAULO | Brasil | 3543402 | 35 | 33 | nan | nan | nan | Cerrado | 0.3 |
| 1394637e-482d-3c3e-bd99-e829e3600dd3 | -22.05545 | -50.60089 | 2025-07-15 04:14:00 | NPP-375D | TUPÃ | SÃO PAULO | Brasil | 3555000 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 740fc92f-d6d4-3e79-8696-6e04f344fa4f | -21.86014 | -56.74796 | 2025-07-15 04:14:00 | NPP-375D | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 19db184e-b097-30ac-bb96-5320eda6b42a | -20.37197 | -46.56755 | 2025-07-15 04:14:00 | NPP-375D | DELFINÓPOLIS | MINAS GERAIS | Brasil | 3121209 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 5aaaac64-4654-3f76-b25d-4a68c5394a43 | -20.39416 | -46.53976 | 2025-07-15 04:14:00 | NPP-375D | DELFINÓPOLIS | MINAS GERAIS | Brasil | 3121209 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 7e417055-493e-313c-b39f-09d7e0ae7c2a | -23.33998 | -46.77282 | 2025-07-15 04:14:00 | NPP-375D | CAIEIRAS | SÃO PAULO | Brasil | 3509007 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| e8a08e19-1aca-34cd-a065-d8850ff349aa | -19.7545 | -54.00227 | 2025-07-15 04:14:00 | NPP-375D | BANDEIRANTES | MATO GROSSO DO SUL | Brasil | 5001508 | 50 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 0e3b5d1c-b467-3c60-b057-c158a4ca790c | -19.7548 | -53.99847 | 2025-07-15 04:14:00 | NPP-375D | BANDEIRANTES | MATO GROSSO DO SUL | Brasil | 5001508 | 50 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 7ef8aad0-05dc-3ad2-b527-2e1a9f78aca8 | -21.62766 | -43.46552 | 2025-07-15 04:14:00 | NPP-375D | JUIZ DE FORA | MINAS GERAIS | Brasil | 3136702 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 27c80e43-20fe-3c8b-9584-cee35e897936 | -23.47693 | -47.18784 | 2025-07-15 04:14:00 | NPP-375D | MAIRINQUE | SÃO PAULO | Brasil | 3528403 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.4 |
| 18e71dfa-01b8-3fd7-acf3-00ac7867f52a | -22.90093 | -43.75787 | 2025-07-15 04:14:00 | NPP-375D | RIO DE JANEIRO | RIO DE JANEIRO | Brasil | 3304557 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| cfb68042-0821-367b-9ecc-4e3043707437 | -24.54496 | -51.85038 | 2025-07-15 04:14:00 | NPP-375D | PITANGA | PARANÁ | Brasil | 4119608 | 41 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| ac19230c-7d4b-3dd5-8cf8-c15c47a11208 | -22.67326 | -42.85514 | 2025-07-15 04:14:00 | NPP-375D | ITABORAÍ | RIO DE JANEIRO | Brasil | 3301900 | 33 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| 9eba41ee-46ac-3d34-8f56-1a899ffb1bfd | -22.90151 | -43.75394 | 2025-07-15 04:14:00 | NPP-375D | RIO DE JANEIRO | RIO DE JANEIRO | Brasil | 3304557 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 67083d99-4dcf-3626-a9b9-b88e371bd5a3 | -22.39809 | -49.80141 | 2025-07-15 04:14:00 | NPP-375D | LUPÉRCIO | SÃO PAULO | Brasil | 3527801 | 35 | 33 | nan | nan | nan | Mata Atlântica | 4.3 |
| 49f410f8-2234-306f-9a93-04cf31e3de36 | -20.23777 | -47.50648 | 2025-07-15 04:14:00 | NPP-375D | PEDREGULHO | SÃO PAULO | Brasil | 3537008 | 35 | 33 | nan | nan | nan | Cerrado | 1.4 |
| a7cddb53-f417-318b-b9fa-cce1fe961dab | -23.51365 | -47.21931 | 2025-07-15 04:14:00 | NPP-375D | MAIRINQUE | SÃO PAULO | Brasil | 3528403 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 3c1b4262-684b-352f-8a1a-f498fc537e52 | -19.28814 | -55.16284 | 2025-07-15 04:14:00 | NPP-375D | RIO VERDE DE MATO GROSSO | MATO GROSSO DO SUL | Brasil | 5007406 | 50 | 33 | nan | nan | nan | Cerrado | 1.1 |
| bf9f2248-6131-3b6a-a87a-7d18ec1e7673 | -22.08412 | -43.178 | 2025-07-15 04:14:00 | NPP-375D | TRÊS RIOS | RIO DE JANEIRO | Brasil | 3306008 | 33 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| f3eaeff5-7a84-3a0c-9ced-abc3f4326772 | -19.75518 | -53.99898 | 2025-07-15 04:14:00 | NPP-375D | BANDEIRANTES | MATO GROSSO DO SUL | Brasil | 5001508 | 50 | 33 | nan | nan | nan | Cerrado | 0.7 |
| c24f0ee9-eb3e-316a-a24b-494dcede0521 | -19.7541 | -54.00175 | 2025-07-15 04:14:00 | NPP-375D | BANDEIRANTES | MATO GROSSO DO SUL | Brasil | 5001508 | 50 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 77fe4f7a-e5ce-3a9f-bb59-e02b979092db | -22.78555 | -43.75917 | 2025-07-15 04:14:00 | NPP-375D | SEROPÉDICA | RIO DE JANEIRO | Brasil | 3305554 | 33 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| d22dfe80-6d92-327b-ac35-541deb904b8c | -21.89259 | -41.4214 | 2025-07-15 04:14:00 | NPP-375D | CAMPOS DOS GOYTACAZES | RIO DE JANEIRO | Brasil | 3301009 | 33 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| c5ec1339-0549-33fc-9aeb-fee7c2e725f6 | -21.11567 | -48.3995 | 2025-07-15 04:14:00 | NPP-375D | TAIÚVA | SÃO PAULO | Brasil | 3553203 | 35 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 99b22318-a78c-3019-b14d-fa2fcb8ceb02 | -21.24012 | -49.19472 | 2025-07-15 04:14:00 | NPP-375D | URUPÊS | SÃO PAULO | Brasil | 3556008 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| 54ded81d-c188-3106-8615-4dd715d36e91 | -18.65135 | -55.72423 | 2025-07-15 04:14:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.6 |
| b89cc89f-6730-3c22-9c2d-bc3eb1f972d8 | -20.99588 | -51.79416 | 2025-07-15 04:14:00 | NPP-375D | TRÊS LAGOAS | MATO GROSSO DO SUL | Brasil | 5008305 | 50 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| bf9b1b2c-aa39-374a-94db-e60e53b7ea85 | -20.3914 | -46.5353 | 2025-07-15 04:14:00 | NPP-375D | DELFINÓPOLIS | MINAS GERAIS | Brasil | 3121209 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 64bfe4c6-4205-3705-9d9a-3d5cc63ec43e | -22.79987 | -47.05352 | 2025-07-15 04:14:00 | NPP-375D | CAMPINAS | SÃO PAULO | Brasil | 3509502 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 8bae1b8c-e7ff-32ca-91e7-35251291e5b1 | -23.33968 | -46.13624 | 2025-07-15 04:14:00 | NPP-375D | GUARAREMA | SÃO PAULO | Brasil | 3518305 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 2f43043d-f0ab-31a3-b8d5-9e632fe96f87 | -23.40695 | -46.5559 | 2025-07-15 04:14:00 | NPP-375D | GUARULHOS | SÃO PAULO | Brasil | 3518800 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 055576df-7f66-32d5-aca5-dae5e6e708ba | -22.99433 | -48.62601 | 2025-07-15 04:14:00 | NPP-375D | BOTUCATU | SÃO PAULO | Brasil | 3507506 | 35 | 33 | nan | nan | nan | Cerrado | 0.3 |
| 8aa74249-2730-3468-8f35-1588d3dab67e | -20.59651 | -45.10976 | 2025-07-15 04:14:00 | NPP-375D | CAMACHO | MINAS GERAIS | Brasil | 3110400 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |


[Clique aqui para ver as próximas entradas](README15.md)
