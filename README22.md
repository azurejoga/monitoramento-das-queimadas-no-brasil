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

## Dados Diários - Página 22

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 46a794fe-f21f-3883-b68a-8eb86c3c29c7 | -9.80918 | -44.8187 | 2026-10-01 03:38:00 | NOAA-21 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| cc7cefd6-58d6-3cd0-a00e-d39d64782f79 | -11.45847 | -43.44016 | 2026-10-01 03:38:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 17.4 |
| a835c560-7b9f-3b09-ab1c-cc832ad3c863 | -11.4529 | -43.44214 | 2026-10-01 03:38:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 90dcc1e7-3373-3d3f-890e-eb7108203fbd | -15.63688 | -40.99976 | 2026-10-01 03:38:00 | NOAA-21 | ENCRUZILHADA | BAHIA | Brasil | 2910404 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| c990a153-ffa1-35a9-a1e9-fc9e6e353424 | -7.85284 | -45.82088 | 2026-10-01 03:38:00 | NOAA-21 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 8.6 |
| 27d03fd6-0d1d-34b3-9d9f-cd94c6d524a6 | -10.25706 | -44.58374 | 2026-10-01 03:38:00 | NOAA-21 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 5d56c437-1138-395d-972a-a12f79156c0b | -11.38337 | -43.37157 | 2026-10-01 03:38:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 08f2b9e7-1607-39c7-877f-2465b2672e6c | -12.56542 | -43.0666 | 2026-10-01 03:38:00 | NOAA-21 | PARATINGA | BAHIA | Brasil | 2923704 | 29 | 33 | nan | nan | nan | Caatinga | 3.7 |
| 0ead9821-af91-3748-be3f-5cc010565750 | -12.1888 | -48.43256 | 2026-10-01 03:38:00 | NOAA-21 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 29.4 |
| 22d38641-1871-374a-a56a-7448fef48c18 | -9.19602 | -45.81762 | 2026-10-01 03:38:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 38613609-f5a7-3a2c-bdb5-b72cadd7e30a | -11.18618 | -45.10967 | 2026-10-01 03:38:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 81928bce-83c4-3ce4-ae22-0c6ecbaf9bcb | -9.20332 | -45.81229 | 2026-10-01 03:38:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 4.8 |
| c202ff28-41ff-30b5-aea7-5a479a8b190e | -11.45066 | -43.42633 | 2026-10-01 03:38:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 7.7 |
| 1c0c6911-b6a4-3cf2-a7cd-477c83d614ae | -7.56636 | -47.20799 | 2026-10-01 03:38:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 55e16d27-6041-3253-8c34-b20773e655ab | -11.19287 | -45.19482 | 2026-10-01 03:38:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 5.1 |
| e4a875fa-4c3d-334e-9fc7-0d62148163a6 | -8.20424 | -45.4977 | 2026-10-01 03:38:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 9d20f449-a788-3d1c-a06c-c12bc8435f7c | -13.32041 | -43.82472 | 2026-10-01 03:38:00 | NOAA-21 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 0a891979-941b-3d60-9971-6b749418795a | -13.52751 | -46.88683 | 2026-10-01 03:38:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 1d0b7716-0674-3675-af50-df4e14541582 | -11.63067 | -41.8334 | 2026-10-01 03:38:00 | NOAA-21 | IBITITÁ | BAHIA | Brasil | 2913101 | 29 | 33 | nan | nan | nan | Caatinga | 1.0 |
| e720cff6-4312-3fdd-8465-6a75b4fd97d0 | -7.56769 | -47.20924 | 2026-10-01 03:38:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 1944d423-4deb-3a64-b122-33be314dff69 | -11.43169 | -43.41668 | 2026-10-01 03:38:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 8e900e32-7315-30c4-9521-94a87991242b | -15.4078 | -39.05066 | 2026-10-01 03:38:00 | NOAA-21 | UNA | BAHIA | Brasil | 2932507 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 0d57cea7-a35f-39d1-8de3-c752978ed182 | -13.87317 | -43.99244 | 2026-10-01 03:38:00 | NOAA-21 | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 52440f5d-cd10-3248-94bf-24c92b3488c7 | -11.41359 | -43.40466 | 2026-10-01 03:38:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 614b3ae3-4b62-3d73-b0b7-c19ff89de736 | -15.6428 | -40.98958 | 2026-10-01 03:38:00 | NOAA-21 | ENCRUZILHADA | BAHIA | Brasil | 2910404 | 29 | 33 | nan | nan | nan | Mata Atlântica | 2.9 |
| c57947cd-c330-31cb-bc9a-07898404b8b2 | -11.47079 | -43.4578 | 2026-10-01 03:38:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| e72f814d-6cea-34f5-8d34-4981d8428d83 | -12.45045 | -44.19175 | 2026-10-01 03:38:00 | NOAA-21 | TABOCAS DO BREJO VELHO | BAHIA | Brasil | 2930907 | 29 | 33 | nan | nan | nan | Cerrado | 3.3 |
| fb31f8db-929b-3ad0-bfd5-cb9e4da04f65 | -11.41829 | -43.48771 | 2026-10-01 03:38:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 53523a6b-504e-3f03-863a-0c18326f2c7e | -11.46294 | -43.44408 | 2026-10-01 03:38:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 17.4 |
| 9023da75-e68e-3c45-8de2-fa638226eba0 | -11.44509 | -43.42831 | 2026-10-01 03:38:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 8.1 |
| d609513e-f433-32e1-9f58-ef2fa91daf5a | -10.45829 | -46.77403 | 2026-10-01 03:38:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 29.0 |
| 75c59d7a-3045-36c7-9670-31dc42c71690 | -11.45567 | -43.42733 | 2026-10-01 03:38:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 7.7 |
| be640129-c25e-3874-a7ad-5ab1cd5711d4 | -11.17907 | -45.1161 | 2026-10-01 03:38:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 16244a5c-e68b-31de-88af-6cf3cc7ec4fa | -12.64406 | -47.6408 | 2026-10-01 03:38:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 4.7 |
| d30a7a12-2628-3793-a4e8-55bbe8182d20 | -11.44619 | -43.42244 | 2026-10-01 03:38:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 11.3 |
| 7633fd42-8d2f-3cbb-96bd-e53d6def304c | -11.44789 | -43.44114 | 2026-10-01 03:38:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 86ee8ab4-0bf3-38ff-a1a8-70ee2b7d0eef | -8.01895 | -42.89052 | 2026-10-01 03:38:00 | NOAA-21 | PAJEÚ DO PIAUÍ | PIAUÍ | Brasil | 2207355 | 22 | 33 | nan | nan | nan | Caatinga | 6.4 |
| f23f70b7-03b6-32f3-a650-310dbdeeb96d | -13.32377 | -43.47599 | 2026-10-01 03:38:00 | NOAA-21 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 4.6 |
| f8cf101a-9ac4-31b0-b228-84d0092b2f83 | -7.50105 | -45.83843 | 2026-10-01 03:38:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| f0fe0e2b-3057-3786-8748-c817ac9db569 | -10.4573 | -46.7792 | 2026-10-01 03:38:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 19.1 |
| 0bb4f2db-5261-32b1-ae46-dce88cdd37d1 | -11.38891 | -43.36961 | 2026-10-01 03:38:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 410d8dfd-1379-35de-8972-845a28f3a87c | -8.01816 | -47.46076 | 2026-10-01 03:38:00 | NOAA-21 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 13.7 |
| f60ece5c-ee9d-39a0-a4aa-28c386a16c34 | -12.18966 | -47.38966 | 2026-10-01 03:38:00 | NOAA-21 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 6.9 |
| a9eca1d4-9984-3f02-b401-6d82da665fe2 | -8.21375 | -45.4865 | 2026-10-01 03:38:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 2564f848-3da7-358a-b429-499b657312d0 | -9.21507 | -45.82093 | 2026-10-01 03:38:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 4.6 |
| dbc3482d-547f-3f9d-83d1-48700af71a62 | -9.87053 | -44.94217 | 2026-10-01 03:38:00 | NOAA-21 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| bf47d2ac-21b0-30d7-828e-38a2b02564b5 | -12.51431 | -43.10081 | 2026-10-01 03:38:00 | NOAA-21 | PARATINGA | BAHIA | Brasil | 2923704 | 29 | 33 | nan | nan | nan | Caatinga | 3.2 |
| 2d0c93d5-726a-3172-b0ba-4befa503d297 | -11.46239 | -43.44704 | 2026-10-01 03:38:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 20.3 |
| 56c7232e-9714-3975-a685-c6639d509d10 | -7.61606 | -44.55185 | 2026-10-01 03:38:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| d0169dfb-8254-3d18-bcbb-715a26dfd9c4 | -8.3255 | -46.75919 | 2026-10-01 03:38:00 | NOAA-21 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 53f9c03c-8668-34f2-be74-51f3da388a4c | -10.45927 | -46.76897 | 2026-10-01 03:38:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 29.0 |
| b07cac77-d1d3-388e-9b00-5974e01343fb | -13.52626 | -46.88461 | 2026-10-01 03:38:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 4.1 |
| e7a2a596-99a7-3e27-a3bb-8f41af555d02 | -12.45112 | -44.19286 | 2026-10-01 03:38:00 | NOAA-21 | TABOCAS DO BREJO VELHO | BAHIA | Brasil | 2930907 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 08b1475a-5da9-33c6-9148-66aa2e43b9ee | -8.38792 | -46.29658 | 2026-10-01 03:38:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| cc077ef8-975d-3e3c-b725-ecb47e49e04b | -11.38391 | -43.36864 | 2026-10-01 03:38:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 31864dcd-170a-377b-bee3-79629a9259ab | -11.42723 | -43.41279 | 2026-10-01 03:38:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 3.6 |
| c9d9f2cc-efa2-31d6-b252-fbfec84e7c3d | -13.38581 | -44.02198 | 2026-10-01 03:38:00 | NOAA-21 | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| aba2ada4-8ac7-376e-a433-f76c50658248 | -10.2968 | -44.64703 | 2026-10-01 03:38:00 | NOAA-21 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 2.7 |
| ff826619-bfc6-344b-af3b-a0adeabfe19a | -12.18333 | -47.38829 | 2026-10-01 03:38:00 | NOAA-21 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 6.7 |
| f351f2cc-87b9-3ba8-86aa-014a48ce8cf4 | -12.17698 | -47.38696 | 2026-10-01 03:38:00 | NOAA-21 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 1c5fa141-2f35-3a8f-b4d6-fd365713a7cc | -11.88267 | -40.96592 | 2026-10-01 03:38:00 | NOAA-21 | TAPIRAMUTÁ | BAHIA | Brasil | 2931301 | 29 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 895fbaeb-f050-3266-914b-cbef18a1254e | -10.46105 | -46.77412 | 2026-10-01 03:38:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 20.2 |
| eedf35c5-9ad6-3279-9886-f4c9df5d5656 | -11.22354 | -45.18787 | 2026-10-01 03:38:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 1fea1c1f-cbde-3938-93bb-0e61eb7b2597 | -11.4312 | -43.50235 | 2026-10-01 03:38:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 82af994f-0486-3d40-8bc9-3ef5086bcea2 | -11.12085 | -44.59629 | 2026-10-01 03:38:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| b6ec8332-35f8-3291-9018-38de8dc216ee | -8.21469 | -45.47482 | 2026-10-01 03:38:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| d3a87e3e-1c2e-3b8b-8457-a6ed90ee4e77 | -7.5083 | -45.83435 | 2026-10-01 03:38:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| f33c33a1-b40e-34aa-af52-d60619204f5d | -11.41885 | -43.48472 | 2026-10-01 03:38:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 2439474d-d6ac-3d48-8623-00262ba053c4 | -11.45512 | -43.43029 | 2026-10-01 03:38:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 7.7 |
| 10495061-e339-3714-b921-1ea448484ad9 | -12.2051 | -43.83595 | 2026-10-01 03:38:00 | NOAA-21 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 0e110d57-e803-3c31-8e05-399e042ee58e | -11.4082 | -43.48585 | 2026-10-01 03:38:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 83d010ad-5837-3c08-8475-7a087cd5d0cc | -12.20212 | -43.83463 | 2026-10-01 03:38:00 | NOAA-21 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 212d95a9-d69e-3386-b726-b228acb61348 | -12.35764 | -46.38005 | 2026-10-01 03:38:00 | NOAA-21 | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| b228a34d-2386-3a2a-9c34-633bbbcba755 | -11.21383 | -45.14743 | 2026-10-01 03:38:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 139ca193-5e25-3cdf-99dc-35d63e30c1df | -10.45475 | -46.77288 | 2026-10-01 03:38:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 20.2 |
| d4cb1633-3f64-35af-885c-a6ca7a9663ab | -11.42165 | -43.41481 | 2026-10-01 03:38:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 3.1 |
| a0028631-1fd1-3ea3-b34f-eec394b5f4fb | -11.44228 | -43.41561 | 2026-10-01 03:38:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 12.3 |
| 61801ec6-3d23-31ca-8a5a-52104c66d9bb | -11.454 | -43.43623 | 2026-10-01 03:38:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 11.1 |
| d3883c11-950c-3110-bf53-f5c178be827a | -8.62949 | -45.32485 | 2026-10-01 03:38:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 7.4 |
| bb1ba5c7-e47f-3194-a36d-894b8858deed | -13.39148 | -46.83099 | 2026-10-01 03:38:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 009530ec-3772-3132-af6f-1bdf6158c82d | -8.20568 | -45.49592 | 2026-10-01 03:38:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 4852ccad-6474-3a35-a0b9-ed7d34356dd5 | -10.91111 | -43.84558 | 2026-10-01 03:38:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 71bb5093-6623-3ce0-a9bd-2241baff6689 | -11.41197 | -43.41356 | 2026-10-01 03:38:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 0e4d7d0e-8284-3209-90ba-9e2c12542630 | -13.43143 | -43.81249 | 2026-10-01 03:38:00 | NOAA-21 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| f39860a7-e157-3198-aebc-5626fe40d6b7 | -11.19177 | -45.1109 | 2026-10-01 03:38:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| f8b9d2cf-dfd6-35c3-a91f-e875633704ca | -10.29607 | -44.65096 | 2026-10-01 03:38:00 | NOAA-21 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 3.8 |
| f18e38e1-1735-30c7-b591-d69efca96825 | -11.19034 | -45.19494 | 2026-10-01 03:38:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 9463fb7e-6794-3c1b-800f-0d981ff5a936 | -12.86339 | -44.33516 | 2026-10-01 03:38:00 | NOAA-21 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 4.5 |
| f67914e2-bef1-39aa-95db-f111d5e15898 | -11.40804 | -43.40665 | 2026-10-01 03:38:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 4359eebc-35d5-35f3-af71-fafa2feec523 | -12.8616 | -44.34065 | 2026-10-01 03:38:00 | NOAA-21 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 8.0 |
| c030f5e7-c6e8-31e8-b200-8bad8cf00f35 | -11.18051 | -45.10879 | 2026-10-01 03:38:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| f9e07738-538b-35bd-ad70-b66e28473e26 | -11.42611 | -43.4187 | 2026-10-01 03:38:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 4e3c63c1-dd34-397d-ad44-f1df59cc5f86 | -11.47134 | -43.45483 | 2026-10-01 03:38:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| aff172d1-540c-3a39-bc7e-6f1e8b2728c0 | -11.39337 | -43.3735 | 2026-10-01 03:38:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| c45a14cc-c27d-3380-8f36-f072151befa4 | -12.35848 | -46.3759 | 2026-10-01 03:38:00 | NOAA-21 | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 528640cf-d980-355c-bc5d-4bfdf8769478 | -8.21391 | -45.4791 | 2026-10-01 03:38:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| d105bc77-ae57-3370-a701-028cd2a47df0 | -11.40717 | -43.40899 | 2026-10-01 03:38:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 4364f341-d2d1-3ff0-942d-f7965b81d658 | -11.26316 | -43.52034 | 2026-10-01 03:38:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 152a9295-ab77-381f-8b8d-41145f736e9b | -13.38819 | -46.81648 | 2026-10-01 03:38:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 370fbe1f-cef7-3ace-9ab3-8185c48a1197 | -7.50264 | -45.79587 | 2026-10-01 03:38:00 | NOAA-21 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |


[Clique aqui para ver as próximas entradas](README23.md)
