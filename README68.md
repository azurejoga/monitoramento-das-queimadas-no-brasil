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

## Dados Diários - Página 68

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 9eef1551-9402-366f-9057-07c28a0f346d | -8.1687 | -44.2534 | 2025-10-09 13:50:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 89.8 |
| 8624d1a8-b1d7-3f4b-bd90-2beb7c39272c | -7.7927 | -44.1767 | 2025-10-09 13:50:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 102.1 |
| 6563fde2-1f51-3c22-b1dd-9b016be312b5 | -13.0586 | -47.8262 | 2025-10-09 13:50:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 162.5 |
| 9df126e0-6cc1-3513-902f-791c1c09a367 | -11.7215 | -44.3084 | 2025-10-09 13:50:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 200.6 |
| bba2178f-2cdb-3ec2-8d58-d1352789225f | -11.4682 | -43.4774 | 2025-10-09 13:50:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 120.5 |
| 5dcae229-1af4-322c-a7b4-359259109eb0 | -17.6538 | -44.4339 | 2025-10-09 13:50:00 | GOES-19 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 124.6 |
| 7d663735-b5e1-36e7-8448-782fa8dd1d89 | -12.4705 | -47.4416 | 2025-10-09 13:50:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 130.9 |
| 26778307-1019-3f31-8d64-798fdca43826 | -13.0783 | -47.801 | 2025-10-09 13:50:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 121.4 |
| 52eb2e54-fad0-340e-8aaf-778b7e08e240 | -15.8085 | -43.7838 | 2025-10-09 13:50:00 | GOES-19 | SÃO JOÃO DA PONTE | MINAS GERAIS | Brasil | 3162401 | 31 | 33 | nan | nan | nan | Caatinga | 243.6 |
| 03ec6fd8-74c1-3a83-becf-ea167e7ccd08 | -8.1052 | -44.812 | 2025-10-09 13:50:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 87.5 |
| a31b50ff-6903-3627-8857-a3f9bae4e119 | -7.6635 | -43.9582 | 2025-10-09 13:50:00 | GOES-19 | BERTOLÍNIA | PIAUÍ | Brasil | 2201705 | 22 | 33 | nan | nan | nan | Cerrado | 80.1 |
| 6f3f8c86-5088-3895-ba62-a6ac0736367f | -9.355 | -45.9284 | 2025-10-09 13:50:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 126.1 |
| edb8ee33-0bfd-304e-acfd-0c8d06b80805 | -11.6742 | -47.0365 | 2025-10-09 13:50:00 | GOES-19 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 130.5 |
| 88c3f24c-9c98-3b85-8954-191dd1bd29b2 | -7.9963 | -44.4788 | 2025-10-09 13:50:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 116.4 |
| 8577d913-61ba-3a4d-ba34-fcb0537a4530 | -10.1905 | -44.5471 | 2025-10-09 13:50:00 | GOES-19 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 205.2 |
| 02cbe3df-d6e1-3150-98d4-9fad7baaa9d3 | -8.5602 | -44.6264 | 2025-10-09 13:50:00 | GOES-19 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 103.2 |
| 5f94c74a-3b42-371e-b32d-4852f6a3566a | -8.1049 | -44.8349 | 2025-10-09 13:50:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 90.4 |
| 20897518-c3d1-3217-b834-013dadf9613b | -10.1576 | -45.4473 | 2025-10-09 13:50:00 | GOES-19 | SÃO GONÇALO DO GURGUÉIA | PIAUÍ | Brasil | 2209757 | 22 | 33 | nan | nan | nan | Cerrado | 122.1 |
| a9bf5482-454b-36df-87a5-fdaa9e2c3337 | -14.2559 | -45.8681 | 2025-10-09 13:50:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 131.8 |
| bb707aa6-02f6-3f48-8c58-7c2d33f61217 | -15.3984 | -47.9938 | 2025-10-09 13:50:00 | GOES-19 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 104.0 |
| 3cfc3d82-782e-3440-af38-9a22de05fb9b | -13.7548 | -45.723 | 2025-10-09 13:50:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 182.2 |
| 7da17d23-61b6-3dba-bfb5-7ff81f55f85b | -8.5599 | -44.6494 | 2025-10-09 13:50:00 | GOES-19 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 116.6 |
| 44813198-04cb-3fc3-babd-7ce38499e1fb | -8.1807 | -43.321 | 2025-10-09 13:50:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 242.8 |
| 08e4f21d-d6b2-34be-b14d-921d8f094728 | -13.0582 | -47.8485 | 2025-10-09 13:50:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 124.4 |
| 5c28bf78-31ee-361e-ba53-48a1ab1a6670 | -9.3209 | -45.6607 | 2025-10-09 13:50:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 123.1 |
| 36af929d-608c-3404-bd2e-c899d5e8156a | -11.785 | -45.0421 | 2025-10-09 13:50:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 118.8 |
| 5c9dbf0b-aab3-3a16-9de4-971ec52243ef | -10.9109 | -47.1129 | 2025-10-09 13:50:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 132.5 |
| e92422db-68bc-39d0-ad7c-24ffe98697cd | -10.1901 | -44.5703 | 2025-10-09 13:50:00 | GOES-19 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 248.2 |
| 649dec40-2acb-392c-a561-c1778874efc1 | -13.2971 | -48.4579 | 2025-10-09 13:50:00 | GOES-19 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 172.5 |
| 49f405f7-508b-3f29-abd5-d06f4f2a63b7 | -12.2754 | -47.6473 | 2025-10-09 13:50:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 127.8 |
| 966bb17c-f40d-3307-8d82-cba828b7c264 | -13.3022 | -47.14 | 2025-10-09 13:50:00 | GOES-19 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 123.5 |
| cc0860d7-ce47-3646-aba5-533dfd637238 | -13.0779 | -47.8234 | 2025-10-09 13:50:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 117.7 |
| 9854ec2a-1fc1-32b9-9736-aec361799ae2 | -11.655 | -47.039 | 2025-10-09 13:50:00 | GOES-19 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 128.8 |
| 201e07a1-8479-30c0-b413-7249a1bde7b1 | -10.1389 | -45.4268 | 2025-10-09 13:50:00 | GOES-19 | SÃO GONÇALO DO GURGUÉIA | PIAUÍ | Brasil | 2209757 | 22 | 33 | nan | nan | nan | Cerrado | 140.1 |
| 725fb793-c5d3-3fe4-86fb-ec51fbf2b7ad | -15.2384 | -46.3616 | 2025-10-09 13:50:00 | GOES-19 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 81.7 |
| 24e85b53-7535-3306-ab0c-58a7b4979a2e | -10.2095 | -44.5446 | 2025-10-09 13:50:00 | GOES-19 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 152.2 |
| 2116d3c3-6a82-319d-97ff-2557e1150a30 | -13.8436 | -51.2971 | 2025-10-09 13:50:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 94.1 |
| 027cca20-f596-322b-a37e-db7702ad733a | -15.8288 | -43.7555 | 2025-10-09 13:50:00 | GOES-19 | SÃO JOÃO DA PONTE | MINAS GERAIS | Brasil | 3162401 | 31 | 33 | nan | nan | nan | Cerrado | 147.2 |
| f8510ecf-f708-35c4-be1f-225ea8ab6bfd | -17.3781 | -45.0687 | 2025-10-09 13:50:00 | GOES-19 | BURITIZEIRO | MINAS GERAIS | Brasil | 3109402 | 31 | 33 | nan | nan | nan | Cerrado | 92.7 |
| 401439c0-cb99-327b-8f65-e74f0f8302c8 | -13.7553 | -45.6999 | 2025-10-09 13:50:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 163.7 |
| fdffe3c0-a415-3de1-9cba-9acd817a816a | -9.2979 | -45.9574 | 2025-10-09 13:50:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 124.8 |
| 27be579c-f06f-3094-a66a-bdbaeb80e945 | -15.8091 | -43.7597 | 2025-10-09 13:50:00 | GOES-19 | SÃO JOÃO DA PONTE | MINAS GERAIS | Brasil | 3162401 | 31 | 33 | nan | nan | nan | Cerrado | 133.1 |
| 23cbc2a9-3237-33cb-a4e8-ebb1cec8d2ea | -12.6964 | -47.6776 | 2025-10-09 13:50:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 152.3 |
| 5eceda07-1f20-36cf-8536-5d1b8ffb202d | -10.0798 | -45.5709 | 2025-10-09 13:50:00 | GOES-19 | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 112.8 |
| 7fb673a3-d6f6-380e-9807-e7a4cfeb0d0b | -13.2967 | -48.4801 | 2025-10-09 13:50:00 | GOES-19 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 151.4 |
| 0f1d0788-3e61-3792-bf0e-fcc0e7704cc6 | -7.7924 | -44.1998 | 2025-10-09 13:50:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 113.9 |
| 1c03ecdc-882e-306b-9f0f-2195e6def00c | -12.5733 | -48.1393 | 2025-10-09 13:50:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 117.3 |
| 283f7e20-bbf3-3a05-9a6d-36d9344f033f | -16.0946 | -45.7829 | 2025-10-09 13:50:00 | GOES-19 | URUCUIA | MINAS GERAIS | Brasil | 3170529 | 31 | 33 | nan | nan | nan | Cerrado | 123.1 |
| 941fc88e-2442-3283-ad94-969030b1b344 | -8.1618 | -43.323 | 2025-10-09 13:50:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 110.0 |
| 6ea7103b-4864-3413-b6f0-e050fc8b978c | -11.7238 | -46.354 | 2025-10-09 13:50:00 | GOES-19 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 143.7 |
| aa580acb-7bf3-3fa4-9845-3eda32cdaae3 | -14.4452 | -47.9943 | 2025-10-09 13:50:00 | GOES-19 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 91.4 |
| dce0e1e7-79a1-3762-a4eb-241b7ab2a288 | -7.7932 | -42.6082 | 2025-10-09 13:50:00 | GOES-19 | RIBEIRA DO PIAUÍ | PIAUÍ | Brasil | 2208874 | 22 | 33 | nan | nan | nan | Caatinga | 72.9 |
| a5ece00a-22f0-367d-a9ba-c4faed2b4155 | -14.7284 | -47.4307 | 2025-10-09 13:50:00 | GOES-19 | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 82.4 |
| 2813275e-3b50-301e-9059-df13f7dd4181 | -8.2074 | -44.18 | 2025-10-09 13:50:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 124.3 |
| e8a26b1e-2e46-3be1-95cf-92ec404c25cd | -17.2846 | -58.0384 | 2025-10-09 13:50:00 | GOES-19 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 81.1 |
| 9519c6b6-b23a-3573-a5ae-1017585afbc4 | -13.0976 | -47.7982 | 2025-10-09 13:50:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 115.4 |
| ca70b004-8a0d-30c2-8b28-d6bab663a95b | -16.2788 | -47.1556 | 2025-10-09 13:50:00 | GOES-19 | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 94.5 |
| 26078457-381a-33f7-a925-85a986f47dd5 | -10.2092 | -44.5678 | 2025-10-09 13:50:00 | GOES-19 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 240.7 |
| b9cf68b7-9962-3377-ade9-1ffac180e8f6 | -14.2754 | -45.8647 | 2025-10-09 13:50:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 145.4 |
| 86a5e656-c519-36d6-8f51-098d71f0d02e | -15.4772 | -47.9578 | 2025-10-09 13:50:00 | GOES-19 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 98.2 |
| 1c6733ee-845e-3e65-8598-a6375e770dc9 | -11.993 | -45.1958 | 2025-10-09 13:50:00 | GOES-19 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 234.6 |
| 20fdd071-47c7-3d09-b7e8-05182a99d618 | -11.7833 | -45.1347 | 2025-10-09 13:50:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 144.8 |
| 5bee314f-65ab-34de-92b6-8777fde48349 | -10.1199 | -45.4292 | 2025-10-09 13:50:00 | GOES-19 | SÃO GONÇALO DO GURGUÉIA | PIAUÍ | Brasil | 2209757 | 22 | 33 | nan | nan | nan | Cerrado | 124.5 |
| 81cfb2cb-ea2c-3207-b4e3-1ea62c66501c | -12.425 | -45.7056 | 2025-10-09 13:50:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 293.5 |
| 5fa3f3ae-2499-332a-aa2f-473f88511e77 | -12.4897 | -47.4389 | 2025-10-09 13:50:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 133.0 |
| bc0c8466-40e0-3e6e-bdd6-adec3c0c9177 | -13.1361 | -47.7926 | 2025-10-09 13:50:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 122.9 |
| 9c02e37e-4168-30a9-96dc-60eb9e311034 | -12.2525 | -47.8728 | 2025-10-09 13:50:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 126.8 |
| 0d012cf1-1a14-3461-83d9-17bbd171a930 | -7.5041 | -44.7109 | 2025-10-09 13:50:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 73.1 |
| 927e0930-7f3e-3111-9098-ea60cb543ebe | -8.8335 | -45.3741 | 2025-10-09 13:50:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 119.5 |
| df60dd01-c2bd-378f-a294-ea5dbc5e63e8 | -8.1618 | -43.323 | 2025-10-09 14:00:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 147.4 |
| ad556f04-b3ed-3764-8f8b-92026e2b6aaa | -12.6964 | -47.6776 | 2025-10-09 14:00:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 150.2 |
| d0cc2462-7d26-36c9-ae8a-2b769919d20a | -9.2979 | -45.9574 | 2025-10-09 14:00:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 128.6 |
| 54e737ce-c354-39d8-954c-1aff71e9195c | -7.9963 | -44.4788 | 2025-10-09 14:00:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 110.0 |
| 3f95102d-bc34-38ec-bbf2-b6192140868f | -7.7927 | -44.1767 | 2025-10-09 14:00:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 103.1 |
| 039a7ca5-bdd4-38b2-aa56-8462988fa1ac | -17.3781 | -45.0687 | 2025-10-09 14:00:00 | GOES-19 | BURITIZEIRO | MINAS GERAIS | Brasil | 3109402 | 31 | 33 | nan | nan | nan | Cerrado | 97.0 |
| 24acc6e5-a912-3ec8-a12a-ce3f45df0e5c | -7.5086 | -44.3201 | 2025-10-09 14:00:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 89.6 |
| c1f6c0ca-da5a-372b-9b57-a58b33b923d2 | -10.1389 | -45.4268 | 2025-10-09 14:00:00 | GOES-19 | SÃO GONÇALO DO GURGUÉIA | PIAUÍ | Brasil | 2209757 | 22 | 33 | nan | nan | nan | Cerrado | 137.2 |
| 28fcf173-c58a-35c4-8fe3-dbcf4ff0665e | -17.9002 | -57.6594 | 2025-10-09 14:00:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 71.5 |
| fa3ceb02-d9e8-330d-afd6-91302e8273b4 | -11.6742 | -47.0365 | 2025-10-09 14:00:00 | GOES-19 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 131.7 |
| 33ea884e-5f8f-34fc-955a-286a6810755b | -14.3543 | -50.7551 | 2025-10-09 14:00:00 | GOES-19 | NOVA CRIXÁS | GOIÁS | Brasil | 5214838 | 52 | 33 | nan | nan | nan | Cerrado | 102.0 |
| e2a7644b-f7e1-3913-b129-3ff38f50f514 | -12.5733 | -48.1393 | 2025-10-09 14:00:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 119.6 |
| f20c0447-e0a0-3fb6-92b7-6102d58fa6fd | -8.1804 | -43.3445 | 2025-10-09 14:00:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 186.9 |
| bbdf6678-144f-3ff7-880c-fec1551b2c24 | -8.1052 | -44.812 | 2025-10-09 14:00:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 86.0 |
| afb99b76-fce8-3886-a63f-992e45e4b18e | -14.3349 | -50.7578 | 2025-10-09 14:00:00 | GOES-19 | NOVA CRIXÁS | GOIÁS | Brasil | 5214838 | 52 | 33 | nan | nan | nan | Cerrado | 107.1 |
| 5cbc897a-47e0-36b4-89a2-fdad43b2a14d | -17.285 | -58.018 | 2025-10-09 14:00:00 | GOES-19 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 81.9 |
| 6469db36-2002-3537-a737-924e64654069 | -7.5463 | -44.3164 | 2025-10-09 14:00:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 102.5 |
| 50569e59-65ec-3d4b-bc6b-a67ffc5fd42f | -11.7833 | -45.1347 | 2025-10-09 14:00:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 144.3 |
| d9dbdce5-52a5-3eca-8f2f-746bff177fdf | -11.655 | -47.039 | 2025-10-09 14:00:00 | GOES-19 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 129.5 |
| 6839e1f9-8506-3602-a797-bd137e78fa63 | -13.0783 | -47.801 | 2025-10-09 14:00:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 131.4 |
| 7b0b3a41-1991-3f08-9da9-165a0923d8f9 | -15.556 | -45.3043 | 2025-10-09 14:00:00 | GOES-19 | CHAPADA GAÚCHA | MINAS GERAIS | Brasil | 3116159 | 31 | 33 | nan | nan | nan | Cerrado | 104.0 |
| eb103453-94a6-3336-9bd2-c3016fd741bc | -13.0586 | -47.8262 | 2025-10-09 14:00:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 139.6 |
| e859b240-901c-3eaf-a7b2-660168db231d | -8.5602 | -44.6264 | 2025-10-09 14:00:00 | GOES-19 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 126.7 |
| fbf682dc-7e4d-38b4-b696-b4d47e924db0 | -8.2083 | -44.1105 | 2025-10-09 14:00:00 | GOES-19 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 90.1 |
| 72c11ea8-fc82-3b7d-beab-4cbdb2be1d1f | -10.2092 | -44.5678 | 2025-10-09 14:00:00 | GOES-19 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 180.8 |
| 1e19b575-4139-33f9-972b-1ac0aa22e1b1 | -15.8085 | -43.7838 | 2025-10-09 14:00:00 | GOES-19 | SÃO JOÃO DA PONTE | MINAS GERAIS | Brasil | 3162401 | 31 | 33 | nan | nan | nan | Caatinga | 439.2 |
| d1d698f6-1b11-343e-ab6d-c092cad9c941 | -7.546 | -44.3395 | 2025-10-09 14:00:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 72.3 |
| 0669efb6-8272-3f59-847d-c46f02a1a864 | -11.993 | -45.1958 | 2025-10-09 14:00:00 | GOES-19 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 183.6 |
| 6d8939e6-4a0f-3abf-aea0-6d78fa94dbb8 | -10.1901 | -44.5703 | 2025-10-09 14:00:00 | GOES-19 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 221.2 |
| 3bcd8505-a838-384b-9839-da147171a441 | -9.3925 | -45.9468 | 2025-10-09 14:00:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 120.8 |
| d8d27c18-fbb6-3e97-9ec7-d11889b5bb56 | -8.1615 | -43.3465 | 2025-10-09 14:00:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 79.1 |


[Clique aqui para ver as próximas entradas](README69.md)
