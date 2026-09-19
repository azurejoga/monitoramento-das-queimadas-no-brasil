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

## Dados Diários - Página 49

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 980325b2-8865-3269-84cf-bf72ec95e203 | -4.82124 | -42.88015 | 2026-09-19 04:38:00 | NPP-375D | UNIÃO | PIAUÍ | Brasil | 2211100 | 22 | 33 | nan | nan | nan | Cerrado | 9.1 |
| ec75cf93-d41c-3cf1-9677-aacda1cccb92 | -7.58376 | -43.44732 | 2026-09-19 04:38:00 | NPP-375D | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 5b2084e5-9664-3dc6-9b01-6c7b4d0f6eac | -3.5014 | -49.5144 | 2026-09-19 04:38:00 | NPP-375D | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| ee642b47-2bca-3ac3-8e51-be2ce6142286 | -3.35721 | -50.46209 | 2026-09-19 04:38:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| c3cd7793-f12e-36f0-9330-0a746f1cdc0e | -3.35836 | -50.45514 | 2026-09-19 04:38:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 48f8ddf1-247d-302a-966d-0d59c964ce9d | -4.28256 | -48.5876 | 2026-09-19 04:38:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 2ee5575a-918c-3ef5-89e8-fda32f6616b8 | -8.23199 | -50.65146 | 2026-09-19 04:38:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 6fcc6981-2917-31bf-8987-863f5c7b6afe | -3.3666 | -50.73531 | 2026-09-19 04:38:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ce77bb19-7e01-307b-9d24-a24ffe90853f | -9.01036 | -44.91586 | 2026-09-19 04:38:00 | NPP-375D | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 6e256b7b-51b1-3080-a1ed-21c4b8686a22 | -3.37839 | -50.45847 | 2026-09-19 04:38:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| b0599b03-ef9b-3a84-af00-b20049a61611 | -7.20122 | -44.09879 | 2026-09-19 04:38:00 | NPP-375D | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| bf950363-0eb4-32d2-a978-a832b795fbd4 | -5.85469 | -51.93656 | 2026-09-19 04:38:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 5f2ff9e4-aa0f-3ecd-8ab2-b655491d0ebf | -7.49702 | -55.01628 | 2026-09-19 04:38:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| dcac7fb5-a243-3b88-b636-5ff28df47da9 | -8.49852 | -44.89349 | 2026-09-19 04:38:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 20194016-c1f9-32ac-a7bb-5cf5b773fdb7 | -5.86024 | -52.0347 | 2026-09-19 04:38:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| cac5522c-dcc8-36b8-8aac-0d961ce56282 | -6.37354 | -58.31311 | 2026-09-19 04:38:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 4dee3d69-427b-38b5-8103-23645120183e | -7.82203 | -44.96144 | 2026-09-19 04:38:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 321d87a5-a09f-3183-b9f7-e89ebb0c916e | -4.50949 | -54.9677 | 2026-09-19 04:38:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e353c72a-3891-3bbe-b34b-0d4df30b8af0 | -6.57545 | -44.15994 | 2026-09-19 04:38:00 | NPP-375D | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 97844986-0591-388f-9daf-2387ce725e08 | -6.94255 | -43.10622 | 2026-09-19 04:38:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| fcf71123-20c6-3bae-9d7b-dc197029ad89 | -8.54897 | -44.56474 | 2026-09-19 04:38:00 | NPP-375D | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 53e645c1-badb-372b-9012-ec5a63335aeb | -5.07144 | -44.85384 | 2026-09-19 04:38:00 | NPP-375D | JOSELÂNDIA | MARANHÃO | Brasil | 2105609 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| e5b77925-3a4e-3751-ac91-e7f0c0a6f09b | -6.44929 | -59.98195 | 2026-09-19 04:38:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 47ffe43c-e81d-3651-905b-adfd26542b83 | -4.83836 | -48.20176 | 2026-09-19 04:38:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| b68be3c7-69ab-3b8d-99f8-de51c3f8eaa5 | -6.6752 | -43.63239 | 2026-09-19 04:38:00 | NPP-375D | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 4.1 |
| f5ae26f4-4d13-3610-9311-841413324216 | -6.95115 | -46.97098 | 2026-09-19 04:38:00 | NPP-375D | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| bfbe80be-5254-3741-8038-6c2627dd876c | -7.77711 | -44.8907 | 2026-09-19 04:38:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| b2671cb6-b7e4-34fc-897b-43ced175f169 | -5.84283 | -44.89625 | 2026-09-19 04:38:00 | NPP-375D | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 810b4d91-3c53-3e6d-b30b-672562918445 | -2.90283 | -54.18458 | 2026-09-19 04:38:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d1299948-2243-32ad-8868-7540aca8adc7 | -8.36989 | -45.65688 | 2026-09-19 04:38:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 9fd0f16a-9eb1-3ea9-a070-3b8491fad00f | -8.75919 | -44.2244 | 2026-09-19 04:38:00 | NPP-375D | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 4.5 |
| b7f4c0b0-dc95-3fa2-b71d-9800533d99a3 | -8.44396 | -45.69733 | 2026-09-19 04:38:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 69a16d22-af1c-3d5f-82fe-7a2af77f6d52 | -7.86016 | -44.87306 | 2026-09-19 04:38:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 4.3 |
| d8aa7ee9-337f-3c3d-a74e-611628d9e29f | -2.89231 | -57.80428 | 2026-09-19 04:38:00 | NPP-375D | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 8fcdecd4-8571-30d7-b4a9-c44e478c95c6 | -7.79082 | -44.84765 | 2026-09-19 04:38:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 762b2377-b10d-3cd1-9ada-5e70124cb5e0 | -4.53504 | -54.93048 | 2026-09-19 04:38:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f9e9e0e7-37fb-3f50-91d1-1e1f508fe959 | -8.77594 | -46.92005 | 2026-09-19 04:38:00 | NPP-375D | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| ce7d376f-6b3f-3223-99fe-fea104dcc6ff | -8.77927 | -46.92059 | 2026-09-19 04:38:00 | NPP-375D | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 1a8770d1-9fd3-3159-8965-f0e504180173 | -5.93899 | -43.33904 | 2026-09-19 04:38:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Caatinga | 1.7 |
| b59d638e-8ba8-322b-a61b-512781981d1a | -8.71788 | -44.87249 | 2026-09-19 04:38:00 | NPP-375D | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| ec8a0f8a-6108-3346-b8d6-53aaa1dd4d87 | -7.58016 | -43.44667 | 2026-09-19 04:38:00 | NPP-375D | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 20fb23ce-dc0a-3f81-9c03-00aef70e4b65 | -2.8337 | -50.46312 | 2026-09-19 04:38:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 70019af7-14bc-3815-86d1-b08ac70b1d1e | -4.4075 | -55.49702 | 2026-09-19 04:38:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a3ccd0dd-9ed9-30b3-901f-5d5314f2220e | -6.97954 | -42.17624 | 2026-09-19 04:38:00 | NPP-375D | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| ac3cd46e-c355-37a1-8412-4348e00e8581 | -5.64815 | -51.70015 | 2026-09-19 04:38:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| bef066ef-2921-369d-b982-8524e5c592a7 | -2.81983 | -50.47176 | 2026-09-19 04:38:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| f2d5fcd5-bbee-3fd9-9461-cecdc8bd1aa6 | -5.86614 | -52.03929 | 2026-09-19 04:38:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| ce959670-de96-3cf8-a209-74757a6ffe29 | -2.963 | -50.3312 | 2026-09-19 04:38:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 6e5b7bd7-ffa0-3b0d-a6f3-ce79a3ab4a9d | -8.66416 | -45.44479 | 2026-09-19 04:38:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 208c0146-8018-3d3a-a7a0-d9f26723ffaa | -7.0886 | -42.08663 | 2026-09-19 04:38:00 | NPP-375D | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 84aa2ee2-373f-3663-9ae3-25d56e678c60 | -6.67582 | -43.62838 | 2026-09-19 04:38:00 | NPP-375D | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 3607bd06-682d-3e6e-a16a-b89e1ce2ba55 | -6.94685 | -43.10254 | 2026-09-19 04:38:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| ae95bcac-3635-35a9-9233-ca2e54d03cb2 | -7.36061 | -44.46946 | 2026-09-19 04:38:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| fa4383de-5910-3f3a-83e2-6f234e9952b9 | -8.46817 | -44.5015 | 2026-09-19 04:38:00 | NPP-375D | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 7dd9ca61-6b53-3082-b127-bcf64325d4a7 | -5.89302 | -53.56667 | 2026-09-19 04:38:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 83192cf2-b0a6-3f0b-a178-f08f39f7c709 | -8.3608 | -47.23695 | 2026-09-19 04:38:00 | NPP-375D | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| b6333a8f-cbaf-3260-838c-c63e54592356 | -5.83459 | -52.03027 | 2026-09-19 04:38:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| c6e83028-d9b1-3ea5-8cc5-26cde8579fbd | -8.78059 | -45.86326 | 2026-09-19 04:38:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 550f9acc-4daa-334a-a760-b92eb7e2c3d0 | -1.58851 | -54.42899 | 2026-09-19 04:38:00 | NPP-375D | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 43218de6-fc0f-3ab1-a0e4-d1e4fa7211ad | -6.7853 | -46.46589 | 2026-09-19 04:38:00 | NPP-375D | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 5501d323-6dd8-32f2-96f2-a1b59fd58fed | -5.23064 | -49.30475 | 2026-09-19 04:38:00 | NPP-375D | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| bba0793c-81b5-3b25-8234-9b39a4a5d5b8 | -8.43921 | -46.87315 | 2026-09-19 04:38:00 | NPP-375D | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 5fccacd7-1012-327e-a015-adcb4cec5d45 | -8.12317 | -44.83619 | 2026-09-19 04:38:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 5026f2cb-3564-3435-b1cf-5f95df2e9200 | -6.36999 | -58.2962 | 2026-09-19 04:38:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 8e07e1b2-5b4d-38ab-8cff-314c9b2b67cc | -6.29898 | -45.68669 | 2026-09-19 04:38:00 | NPP-375D | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 5bedeeca-7ca2-34b7-89df-478f63858f04 | -4.49459 | -55.488 | 2026-09-19 04:38:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| f2bed6c8-957a-31a2-9b31-aa49a86e0f7d | -8.43588 | -46.87262 | 2026-09-19 04:38:00 | NPP-375D | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| ea3b3da8-9594-3f6c-8a80-cec6e4c4d36e | -2.8152 | -50.47467 | 2026-09-19 04:38:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 9135d5b9-5c36-35e0-831a-d4175777c292 | -6.46591 | -48.00726 | 2026-09-19 04:38:00 | NPP-375D | RIACHINHO | TOCANTINS | Brasil | 1718550 | 17 | 33 | nan | nan | nan | Amazônia | 1.6 |
| d0b3b681-327c-351f-9203-77ece720e097 | -3.24049 | -46.95166 | 2026-09-19 04:38:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| ce6be2c3-41d8-3568-af4f-10de93b79b06 | -6.65397 | -50.91289 | 2026-09-19 04:38:00 | NPP-375D | ÁGUA AZUL DO NORTE | PARÁ | Brasil | 1500347 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 6a8a2a30-3254-3aeb-a16f-3eb7563345ef | -3.23992 | -46.95524 | 2026-09-19 04:38:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 8900328d-4c8b-310c-8952-5f1468650d15 | -5.18856 | -49.33277 | 2026-09-19 04:38:00 | NPP-375D | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| acee1426-c5bc-38d1-861f-0dd06c0446ec | -3.72868 | -49.04286 | 2026-09-19 04:38:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 440c87b4-94c3-3e92-b58a-28282e2b8d93 | -8.37639 | -47.20351 | 2026-09-19 04:38:00 | NPP-375D | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 85147710-24f9-30fc-91d0-66a5a3cd34c9 | -7.64191 | -46.11673 | 2026-09-19 04:38:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 124b3eab-7951-357b-b56b-3f8e37f5d14d | -7.60684 | -45.42853 | 2026-09-19 04:38:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| be711748-5dc8-34fb-9711-5f7368f9474b | -7.78171 | -44.83862 | 2026-09-19 04:38:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 3bfe0b24-0b22-3771-a84b-a1bcf52fc574 | -7.00695 | -49.75975 | 2026-09-19 04:38:00 | NPP-375D | XINGUARA | PARÁ | Brasil | 1508407 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 55749ef7-efe6-3a90-95e5-95a0ee87ea78 | -8.87741 | -44.91935 | 2026-09-19 04:38:00 | NPP-375D | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 641bebfe-a57f-331f-a2bd-1274f6b5f2b3 | -8.47359 | -47.01447 | 2026-09-19 04:38:00 | NPP-375D | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| f2b9562d-20c7-3e8c-97de-40190948557b | -4.25696 | -48.54226 | 2026-09-19 04:38:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 2c8e8dc6-e48f-3a8e-aa2f-edf4a410631a | -4.2128 | -56.33229 | 2026-09-19 04:38:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f73ce053-8919-312e-94af-2a06e071d02a | -6.57892 | -44.16047 | 2026-09-19 04:38:00 | NPP-375D | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 7cfc5d41-7caf-37cf-a083-0fc4888f726b | -7.08215 | -44.71396 | 2026-09-19 04:38:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 5191dc49-8141-34c4-a074-5a0a3dda64b5 | -8.24452 | -45.61107 | 2026-09-19 04:38:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 36109b76-3a2e-33a4-8d53-5ac97768b8d6 | -6.99458 | -49.76645 | 2026-09-19 04:38:00 | NPP-375D | XINGUARA | PARÁ | Brasil | 1508407 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 866ba374-9841-3a37-9d73-1baabcddd970 | -7.0217 | -44.65573 | 2026-09-19 04:38:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| d7c55145-c3ea-3e89-ac68-689ed4e0704b | -8.77052 | -46.91553 | 2026-09-19 04:38:00 | NPP-375D | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 7.2 |
| 5ae2e43f-f440-3dc0-a7fb-95762b340805 | -6.65237 | -51.48834 | 2026-09-19 04:38:00 | NPP-375D | TUCUMÃ | PARÁ | Brasil | 1508084 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 16812e67-7d56-37af-a4bd-5c4e809c6d7a | -7.0019 | -49.76764 | 2026-09-19 04:38:00 | NPP-375D | XINGUARA | PARÁ | Brasil | 1508407 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 3143a671-537d-325d-8a06-1377a8838ff8 | -5.76728 | -57.45935 | 2026-09-19 04:38:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 10.5 |
| 42adcc9c-9c06-340f-b8b6-2f090dea1543 | -3.3343 | -50.11792 | 2026-09-19 04:38:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 9b1e34dc-f39f-36d2-890f-19327d393fc6 | -5.84086 | -52.0982 | 2026-09-19 04:38:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e9631cd6-7851-3ddb-8781-05708cdf803f | -4.43574 | -55.07685 | 2026-09-19 04:38:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 144dfab7-ea3b-3ff5-98ee-e2ffe6899b3c | -3.55859 | -50.29146 | 2026-09-19 04:38:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 20893769-9a86-3a0c-9904-c1b6ab0b0557 | -2.90732 | -57.79552 | 2026-09-19 04:38:00 | NPP-375D | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 3.0 |
| ea9cba3f-957f-3b3e-879d-2b377e3b38ae | -7.1956 | -47.88079 | 2026-09-19 04:38:00 | NPP-375D | BABAÇULÂNDIA | TOCANTINS | Brasil | 1703008 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 1dc5319b-c368-35b2-a4e3-843e5a9d783c | -7.76538 | -46.70469 | 2026-09-19 04:38:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 9ed64334-eb8c-3071-b78c-6ba03b97f22a | -3.36792 | -50.44703 | 2026-09-19 04:38:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |


[Clique aqui para ver as próximas entradas](README50.md)
