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
| 75fbcb08-613a-365c-8b0f-05b4e65f0ecd | -7.63205 | -50.22236 | 2026-06-26 04:29:00 | NPP-375D | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 486b9f12-f94a-30ce-b009-62569809da75 | -8.57664 | -46.89309 | 2026-06-26 04:29:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 7b4815a6-9284-3ba5-ac7a-3249920e0967 | -4.98374 | -37.23372 | 2026-06-26 04:29:00 | NPP-375D | MOSSORÓ | RIO GRANDE DO NORTE | Brasil | 2408003 | 24 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 81771523-187c-32ce-9346-108119ec2496 | -7.74786 | -44.62238 | 2026-06-26 04:29:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 5.4 |
| ef51aded-b0f0-3d82-b3b9-670cf65f0744 | -5.78034 | -45.05893 | 2026-06-26 04:29:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 13.1 |
| 90ce0e3c-5764-3d7f-b125-3220c0dc075c | -6.3053 | -44.65182 | 2026-06-26 04:29:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 1e953a25-2f1e-3fa8-88ba-25ea16fe4802 | -5.78477 | -45.05252 | 2026-06-26 04:29:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 22.9 |
| c1e1b759-b031-330a-98f4-f2d16f9a16d9 | -4.14196 | -43.6592 | 2026-06-26 04:29:00 | NPP-375D | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 1f62d861-4d7b-3b19-ba56-e55570e4519c | -4.94382 | -48.2476 | 2026-06-26 04:29:00 | NPP-375D | ABEL FIGUEIREDO | PARÁ | Brasil | 1500131 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| ccca3ac8-3a6d-3a49-98a8-71c201447292 | -6.30639 | -44.64487 | 2026-06-26 04:29:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 49092e7d-5dbc-3bef-8c1a-62a7abc5225e | -7.2599 | -46.91275 | 2026-06-26 04:29:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 86e2cc64-dc99-3daf-909f-1cf141f6fe44 | -4.14252 | -43.65571 | 2026-06-26 04:29:00 | NPP-375D | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 0a9e255e-1315-3b06-b9e6-e5baa464fab3 | -6.50552 | -42.22676 | 2026-06-26 04:29:00 | NPP-375D | VÁRZEA GRANDE | PIAUÍ | Brasil | 2211407 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| c54e2fa2-175c-3697-ac83-4ce9dfbc1e75 | -5.87499 | -47.19638 | 2026-06-26 04:29:00 | NPP-375D | RIBAMAR FIQUENE | MARANHÃO | Brasil | 2109551 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| bc2d9dfc-d79e-32b4-833e-0fe60429d2ae | -4.35231 | -47.76269 | 2026-06-26 04:29:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 9c07431d-ce32-3308-bdba-de4d7b6ca976 | -7.74206 | -44.17699 | 2026-06-26 04:29:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 5ae7e93d-10c0-3837-9b52-6c68018c7dca | -8.13667 | -47.88762 | 2026-06-26 04:29:00 | NPP-375D | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 8caf87fd-457c-39d5-985b-70f41b1ce5b9 | -6.87208 | -43.66476 | 2026-06-26 04:29:00 | NPP-375D | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 0.5 |
| fed26d76-c6eb-33c2-bab4-786fc188de95 | -4.66249 | -43.22252 | 2026-06-26 04:29:00 | NPP-375D | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| bdcc736c-9ae9-3f0a-be34-25b3185ac570 | -6.50196 | -42.22625 | 2026-06-26 04:29:00 | NPP-375D | VÁRZEA GRANDE | PIAUÍ | Brasil | 2211407 | 22 | 33 | nan | nan | nan | Caatinga | 3.2 |
| 400f2530-4cc7-3776-bd04-8d2b6212a3a1 | -6.50613 | -42.2228 | 2026-06-26 04:29:00 | NPP-375D | VÁRZEA GRANDE | PIAUÍ | Brasil | 2211407 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| dea74b17-d875-383e-a41a-57eb70ebf3d4 | -8.13314 | -47.88704 | 2026-06-26 04:29:00 | NPP-375D | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| bcb9e012-aab4-3085-80fc-abf013a664d1 | -7.63266 | -50.21883 | 2026-06-26 04:29:00 | NPP-375D | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 67bfd83c-288d-316e-814f-8203dae50921 | -5.79263 | -43.89165 | 2026-06-26 04:29:00 | NPP-375D | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 98128151-c6bb-3de0-bd77-8cea9bbe0ae2 | -5.77701 | -45.0584 | 2026-06-26 04:29:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 13.1 |
| eceb179b-8145-30a1-b628-112767fe7579 | -8.6326 | -47.17456 | 2026-06-26 04:29:00 | NPP-375D | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| ea4b0926-fd7f-347d-9acc-fa9ec5c5c040 | -6.50257 | -42.2223 | 2026-06-26 04:29:00 | NPP-375D | VÁRZEA GRANDE | PIAUÍ | Brasil | 2211407 | 22 | 33 | nan | nan | nan | Caatinga | 3.2 |
| e326eb7c-8578-386f-b7c0-320554af28e2 | -5.94271 | -43.47079 | 2026-06-26 04:29:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 2a182b9c-24aa-3358-887d-551aceb050da | -5.4334 | -49.30033 | 2026-06-26 04:29:00 | NPP-375D | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 621cbeae-2a39-3309-8d01-52c556697267 | -5.78928 | -43.89112 | 2026-06-26 04:29:00 | NPP-375D | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| a41e0357-bb0a-3e50-830a-997aa67d2e85 | -7.56928 | -45.87804 | 2026-06-26 04:29:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| aeda036d-6e6e-33bc-bcb6-7dd9465aa642 | -6.93689 | -43.67122 | 2026-06-26 04:29:00 | NPP-375D | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 9ebcf403-e07b-3896-a91d-2c05c56a435c | -8.01571 | -49.64526 | 2026-06-26 04:29:00 | NPP-375D | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| e877d84a-9954-3583-993e-765881bc08f6 | -4.34865 | -47.76212 | 2026-06-26 04:29:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| b7b743f9-bfe4-3b9b-8d25-3f358fded49a | -8.22567 | -47.12072 | 2026-06-26 04:29:00 | NPP-375D | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 70ab606f-4396-39f1-ac08-d638ebcbbbd0 | -5.78089 | -45.05546 | 2026-06-26 04:29:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 1dcaad6d-47b0-3a69-8448-57e6da421e48 | -6.30475 | -44.65528 | 2026-06-26 04:29:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| b102ee7c-ffef-3b7e-8469-b161a46e51e4 | -7.63025 | -47.29942 | 2026-06-26 04:29:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 94e3fb5f-ac68-3a7c-abdb-373167586417 | -5.32536 | -44.68851 | 2026-06-26 04:29:00 | NPP-375D | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| c1d611d6-9c4d-3499-8f9d-893f58c32860 | -7.56871 | -45.88156 | 2026-06-26 04:29:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| c7654f5c-881e-3c30-b574-0247256a735c | -7.63087 | -47.29562 | 2026-06-26 04:29:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 24c6c36c-2033-38a5-ba5e-d25fb4a3ca1d | -5.782 | -45.04852 | 2026-06-26 04:29:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| e267bb42-244c-390a-ad3b-c7cac1451932 | -6.98729 | -42.89222 | 2026-06-26 04:29:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 2.7 |
| eab3c531-0189-35ac-9c46-09fe0c4f060e | -6.99076 | -42.89275 | 2026-06-26 04:29:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 2.7 |
| 3890f632-cbd6-3760-8ef8-05d966089607 | -3.31 | -42.49758 | 2026-06-26 04:29:00 | NPP-375D | SÃO BERNARDO | MARANHÃO | Brasil | 2110609 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| da5b954c-e767-307e-8f68-2e8974cd15e9 | -5.78809 | -45.05304 | 2026-06-26 04:29:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 22.9 |
| 5d6e3658-b63b-3bba-8c03-8df492a32305 | -7.74563 | -44.61484 | 2026-06-26 04:29:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 9b468958-1762-311b-a2b9-554b00c70c67 | -5.79699 | -45.12567 | 2026-06-26 04:29:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 268edb84-5bca-36ea-bfa5-ae823d526fa4 | -8.13248 | -47.89104 | 2026-06-26 04:29:00 | NPP-375D | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 35b23a86-92e7-38a1-a811-a87abcc05bf9 | -8.4958 | -44.74771 | 2026-06-26 04:29:00 | NPP-375D | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| cecc0fdc-f402-35f4-b331-021eec9d7cbc | -4.40528 | -40.69534 | 2026-06-26 04:29:00 | NPP-375D | IPU | CEARÁ | Brasil | 2305803 | 23 | 33 | nan | nan | nan | Caatinga | 1.1 |
| ea759249-d70d-3296-bac0-09dc45ff0f9e | -7.62678 | -47.29887 | 2026-06-26 04:29:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 8016247b-273f-35ca-b74f-469e361368b4 | -8.136 | -47.89162 | 2026-06-26 04:29:00 | NPP-375D | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 03c4c336-ff1a-3f88-b248-e8146185a0c5 | -6.97515 | -42.90204 | 2026-06-26 04:29:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 3.0 |
| 7dcc8e61-2a26-306a-8456-55d787da12f5 | -6.94027 | -43.67173 | 2026-06-26 04:29:00 | NPP-375D | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| aadbcedd-f32d-363a-9209-6e1476f81d05 | -8.01651 | -49.64044 | 2026-06-26 04:29:00 | NPP-375D | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b8701199-c228-34ba-b076-6a80533af4a3 | -4.85474 | -42.94876 | 2026-06-26 04:29:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 8f9f2f9f-ec1b-3910-977a-2acf120ddb3e | -6.50969 | -42.22326 | 2026-06-26 04:29:00 | NPP-375D | VÁRZEA GRANDE | PIAUÍ | Brasil | 2211407 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 0e3c18bf-072f-3474-a2a1-e50abffdd495 | -8.26196 | -46.22113 | 2026-06-26 04:29:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| bf5008f9-6272-34e6-8f98-03b8c2a94f3a | -7.75508 | -44.61993 | 2026-06-26 04:29:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 89a76364-3874-3204-9ff5-7e3740512fdc | -8.32999 | -47.12215 | 2026-06-26 04:29:00 | NPP-375D | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 7cad3461-1cfc-32c6-9844-37ce8217513b | -8.25861 | -46.2206 | 2026-06-26 04:29:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 01b7bd0e-761e-3a33-aa8b-151230865c7a | -6.98324 | -42.8955 | 2026-06-26 04:29:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 9.3 |
| 0e8ace7a-74fe-3ee5-b8d0-dbbe1435595f | -6.97977 | -42.89498 | 2026-06-26 04:29:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 9.3 |
| bf1dbd05-a70d-39ce-9842-020bc8ef00a7 | -7.2605 | -46.90904 | 2026-06-26 04:29:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| eb79e9ab-84b0-34ac-9406-8ec86e07f560 | -8.22909 | -47.12129 | 2026-06-26 04:29:00 | NPP-375D | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 008babaf-b4d1-36e0-9b4a-8f75e6dfaf34 | -7.75563 | -44.61641 | 2026-06-26 04:29:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| ef208c0f-d22f-3620-a6ca-144a84ad63be | -8.23311 | -47.11815 | 2026-06-26 04:29:00 | NPP-375D | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 1afd2aaa-2ed9-360e-b76c-88186a271743 | -6.50318 | -42.21833 | 2026-06-26 04:29:00 | NPP-375D | VÁRZEA GRANDE | PIAUÍ | Brasil | 2211407 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 10f58dd8-097c-3b41-8332-bac1484fc8e5 | -8.45446 | -47.0016 | 2026-06-26 04:29:00 | NPP-375D | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 36619dc4-e569-32db-a5e0-678a4cce8a48 | -8.01101 | -49.64948 | 2026-06-26 04:29:00 | NPP-375D | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 6422650d-ed52-3342-86ce-b8bed979dd82 | -6.30197 | -44.65129 | 2026-06-26 04:29:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 9558a82c-bfd7-3976-8785-bbf1b9d258e4 | -5.32868 | -44.68904 | 2026-06-26 04:29:00 | NPP-375D | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 7.9 |
| bed991bd-2f3e-371c-b668-112983212bcf | -8.1338 | -47.88309 | 2026-06-26 04:29:00 | NPP-375D | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 5.1 |
| e6153336-bbba-3f4a-a866-c97bd0034af8 | -5.93933 | -43.47026 | 2026-06-26 04:29:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 84d167f3-5d97-3a77-9b57-51d8ae97c44b | -7.652 | -50.02575 | 2026-06-26 04:29:00 | NPP-375D | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 9e0eccf8-3683-3db9-b5c1-ce93a83d6ab9 | -5.94327 | -43.46719 | 2026-06-26 04:29:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 84bee3d7-19c6-3ffc-a6b8-6fdf1ad77c41 | -6.49842 | -42.22569 | 2026-06-26 04:29:00 | NPP-375D | VÁRZEA GRANDE | PIAUÍ | Brasil | 2211407 | 22 | 33 | nan | nan | nan | Caatinga | 3.2 |
| 76e63b2b-5bb3-395b-bd77-54cdf8d16ab5 | -6.98266 | -42.8993 | 2026-06-26 04:29:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 9.3 |
| 85d653f3-4836-32c7-8eb8-76ae62dadd19 | -5.727 | -49.10055 | 2026-06-26 04:29:00 | NPP-375D | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 350d264d-d0a9-3752-95be-511070cd06cd | -4.14424 | -43.6596 | 2026-06-26 04:29:00 | NPP-375D | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| dc7460ee-1d81-336a-98cb-25399c42eb89 | -5.78699 | -45.05998 | 2026-06-26 04:29:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 15.8 |
| 680a30c3-c92f-315f-855a-83a15e1d525b | -7.74032 | -44.17693 | 2026-06-26 04:29:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 21042c45-ea7e-303a-bf69-2a24b314eb44 | -7.93624 | -47.81173 | 2026-06-26 04:29:00 | NPP-375D | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 99ea151a-1d79-3d59-b861-b222d837953f | -6.94422 | -43.66864 | 2026-06-26 04:29:00 | NPP-375D | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 7059602e-5b26-3085-b47c-2d810b25adf7 | -8.22848 | -47.12511 | 2026-06-26 04:29:00 | NPP-375D | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| d1c40ff5-52bd-3e81-a282-2a6fe1c34c13 | -7.75174 | -44.6194 | 2026-06-26 04:29:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 6.5 |
| de4c835c-d7a2-3695-8ce7-185ac575b20f | -7.73696 | -44.17642 | 2026-06-26 04:29:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| b3da121c-53fd-3f5b-b217-d4e35b2fd79a | -5.7758 | -45.0599 | 2026-06-26 04:30:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 75.3 |
| f65b8ad9-f16b-381d-8e71-aa2f93e0685c | -5.7945 | -45.0586 | 2026-06-26 04:30:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 58.6 |
| 05db1ef2-5916-3c14-ae2d-449b3f3fd49a | -11.77593 | -46.44384 | 2026-06-26 04:32:00 | NPP-375D | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 127eb512-b43e-3461-bafe-05eb7dbf4253 | -15.59634 | -48.35513 | 2026-06-26 04:32:00 | NPP-375D | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 3b4afff4-dec0-358e-a3c4-1fa7ae994379 | -8.68313 | -47.86094 | 2026-06-26 04:32:00 | NPP-375D | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| ab6be4e4-a47d-3729-a314-c88779582ccd | -10.3595 | -47.34052 | 2026-06-26 04:32:00 | NPP-375D | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 7da446a2-1764-3ebf-bdc9-98b143988662 | -14.63509 | -54.4612 | 2026-06-26 04:32:00 | NPP-375D | PLANALTO DA SERRA | MATO GROSSO | Brasil | 5106455 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| e5a88481-6b36-39f1-ad96-7399710f529b | -10.38369 | -56.71534 | 2026-06-26 04:32:00 | NPP-375D | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 6880fabd-4d37-3a74-8567-a67f69ee83d6 | -14.84068 | -48.12681 | 2026-06-26 04:32:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 485662f2-e988-3a31-9f77-1c32fb41c6e0 | -12.4435 | -49.58027 | 2026-06-26 04:32:00 | NPP-375D | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 4.2 |
| cce9901a-04bb-3da4-a404-fec3495a7de4 | -10.38865 | -56.72142 | 2026-06-26 04:32:00 | NPP-375D | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ede75879-ef05-31bb-bce9-f03117906c53 | -10.10966 | -47.56636 | 2026-06-26 04:32:00 | NPP-375D | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |


[Clique aqui para ver as próximas entradas](README8.md)
