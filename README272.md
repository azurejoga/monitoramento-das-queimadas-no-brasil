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

## Dados Diários - Página 272

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 5c4a97a3-d3a5-3778-a889-d08764bfd160 | -8.18644 | -44.41628 | 2026-10-09 16:01:00 | NPP-375 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 6.3 |
| ba49f704-16f7-30a2-a7d7-32ed9c4f7d2f | -10.48698 | -47.22464 | 2026-10-09 16:01:00 | NPP-375 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 9.7 |
| c0cf3a26-359e-3837-b553-f5214fc772e6 | -11.08786 | -43.99808 | 2026-10-09 16:01:00 | NPP-375 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 11.5 |
| b6c79846-d750-3bff-96b7-16d2006ef472 | -7.48692 | -42.84132 | 2026-10-09 16:01:00 | NPP-375 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 7.6 |
| 21f08e50-125a-3583-a85f-3bfacc473373 | -10.33387 | -39.48728 | 2026-10-09 16:01:00 | NPP-375 | MONTE SANTO | BAHIA | Brasil | 2921500 | 29 | 33 | nan | nan | nan | Caatinga | 6.8 |
| 665c88e0-8f72-3ac5-ae8c-6030d3f7f0df | -7.24813 | -39.25288 | 2026-10-09 16:01:00 | NPP-375 | BARBALHA | CEARÁ | Brasil | 2301901 | 23 | 33 | nan | nan | nan | Caatinga | 53.3 |
| 8951ce31-44e0-3fcc-90cf-43fd061c3003 | -5.81614 | -42.48655 | 2026-10-09 16:01:00 | NPP-375 | BARRO DURO | PIAUÍ | Brasil | 2201408 | 22 | 33 | nan | nan | nan | Caatinga | 4.3 |
| 354c7d32-21ea-3e80-9fbb-ed21099038d5 | -10.39755 | -39.86417 | 2026-10-09 16:01:00 | NPP-375 | ANDORINHA | BAHIA | Brasil | 2901353 | 29 | 33 | nan | nan | nan | Caatinga | 21.8 |
| 88598a0c-16a5-3c74-9e77-f1dd9d5dec6b | -11.04999 | -44.02802 | 2026-10-09 16:01:00 | NPP-375 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 89.2 |
| 677232eb-997f-3dc3-bc77-3b48aced1107 | -11.0612 | -44.12081 | 2026-10-09 16:01:00 | NPP-375 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 237.2 |
| 163943a6-98aa-3aa6-b7d9-c714f30f9236 | -8.93076 | -45.14631 | 2026-10-09 16:01:00 | NPP-375 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 14.5 |
| 0c737687-b99d-3738-8a3a-9890f8737e60 | -7.24658 | -37.97792 | 2026-10-09 16:01:00 | NPP-375 | PIANCÓ | PARAÍBA | Brasil | 2511301 | 25 | 33 | nan | nan | nan | Caatinga | 5.9 |
| 27c4c6a1-72df-3ae9-98af-290ecdc2aee7 | -10.44806 | -47.29951 | 2026-10-09 16:01:00 | NPP-375 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 18.7 |
| 45d59ea0-eba6-3a18-ae18-4abcd77e5d1d | -10.83618 | -47.35153 | 2026-10-09 16:01:00 | NPP-375 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 13.2 |
| cde148eb-6b96-3200-9749-fcb83c2c92cf | -9.7964 | -45.61278 | 2026-10-09 16:01:00 | NPP-375 | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 8.4 |
| e4106900-8d5b-3875-852d-19287b8b9a3a | -7.51305 | -45.29757 | 2026-10-09 16:01:00 | NPP-375 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 20.2 |
| 5317fcaa-ac9d-378a-9a06-e8cfaef0818c | -5.51071 | -43.06729 | 2026-10-09 16:01:00 | NPP-375 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 93f3bffc-8057-3383-ac5f-03eb381d8018 | -11.04232 | -44.06303 | 2026-10-09 16:01:00 | NPP-375 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 34.7 |
| d5399f54-433f-3545-8270-0157be48bb8b | -7.22217 | -44.16962 | 2026-10-09 16:01:00 | NPP-375 | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 7.2 |
| b5391d3b-a4da-3ec8-b40e-cb999e0118ff | -11.2895 | -45.20597 | 2026-10-09 16:01:00 | NPP-375 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 7.8 |
| 0bca9b8d-f0ac-3f80-ae66-3a699974f1c1 | -6.55087 | -42.35333 | 2026-10-09 16:01:00 | NPP-375 | TANQUE DO PIAUÍ | PIAUÍ | Brasil | 2210979 | 22 | 33 | nan | nan | nan | Caatinga | 5.7 |
| 88db5a30-f934-394c-b42a-12372606f93d | -10.31309 | -46.28827 | 2026-10-09 16:01:00 | NPP-375 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 297b90fe-0642-36c2-b34e-6c01768f5315 | -6.29814 | -37.69698 | 2026-10-09 16:01:00 | NPP-375 | CATOLÉ DO ROCHA | PARAÍBA | Brasil | 2504306 | 25 | 33 | nan | nan | nan | Caatinga | 5.7 |
| dd1cba62-afd8-3e7a-b72e-6326caf93ea1 | -11.24781 | -45.17744 | 2026-10-09 16:01:00 | NPP-375 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 33909915-8afd-3f06-b67b-bf7e967b15bb | -6.40752 | -35.28658 | 2026-10-09 16:01:00 | NPP-375 | PEDRO VELHO | RIO GRANDE DO NORTE | Brasil | 2409803 | 24 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| e9e22010-27dd-382d-b30d-e207ba05cd85 | -7.327 | -43.98517 | 2026-10-09 16:01:00 | NPP-375 | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 8.8 |
| 751074d3-062a-31f5-914b-49fa17e6849a | -5.98956 | -41.36298 | 2026-10-09 16:01:00 | NPP-375 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 5.2 |
| 3e1ccef6-3e77-3c3a-af2a-0e6cc9bff21e | -8.99621 | -45.95694 | 2026-10-09 16:01:00 | NPP-375 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 13.4 |
| ab3ff4db-1cf2-3651-8a13-6b74af164ab3 | -8.99044 | -45.96304 | 2026-10-09 16:01:00 | NPP-375 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 13.4 |
| ac487cf6-437c-3d89-b86e-ab139c7fdab0 | -8.97499 | -45.15232 | 2026-10-09 16:01:00 | NPP-375 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 64.8 |
| c7aecc3a-6925-36fb-840a-522c78b1a44a | -7.37946 | -44.03846 | 2026-10-09 16:01:00 | NPP-375 | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 8.7 |
| 8988baba-7bcd-3c2d-9c6a-9dde445477cd | -10.88117 | -44.79037 | 2026-10-09 16:01:00 | NPP-375 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 10.8 |
| a58d211a-2897-33d0-90d5-4f8ad2c3d940 | -9.39396 | -45.81942 | 2026-10-09 16:01:00 | NPP-375 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 7.3 |
| 3bebef85-5271-30be-a765-2f8d88baab2c | -5.52512 | -43.05951 | 2026-10-09 16:01:00 | NPP-375 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 9.1 |
| 9647060f-1d26-35bb-b5c9-95027f6e4edb | -5.9922 | -41.38174 | 2026-10-09 16:01:00 | NPP-375 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 17.1 |
| 67c05d08-cd3a-3efa-8ded-2e3e350ceeb6 | -7.50703 | -45.2986 | 2026-10-09 16:01:00 | NPP-375 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 20.2 |
| 8db6220e-9fae-3de4-803c-45cb6616012c | -6.97269 | -43.44802 | 2026-10-09 16:01:00 | NPP-375 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 75ac3476-3b27-32f4-b69a-fb3ada8a4787 | -7.29804 | -44.02237 | 2026-10-09 16:01:00 | NPP-375 | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 57.0 |
| 320fbd5f-88f9-3ae9-8c28-5ad71827a097 | -6.00583 | -40.96801 | 2026-10-09 16:01:00 | NPP-375 | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 39.4 |
| b6f5dd69-e428-3758-b67e-21807c7acb87 | -10.49406 | -47.22396 | 2026-10-09 16:01:00 | NPP-375 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 158.5 |
| 8c75edd8-1db9-39f6-ba4a-f92aa7809783 | -6.88885 | -43.68856 | 2026-10-09 16:01:00 | NPP-375 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 10.5 |
| 4cb66397-0de8-3803-9315-1b7a00bb6bd4 | -9.74482 | -44.807 | 2026-10-09 16:01:00 | NPP-375 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 72fef9e1-ce57-385e-ae10-8acf1d501ef1 | -11.41553 | -46.6838 | 2026-10-09 16:01:00 | NPP-375 | RIO DA CONCEIÇÃO | TOCANTINS | Brasil | 1718659 | 17 | 33 | nan | nan | nan | Cerrado | 21.8 |
| c676527e-a1c8-3c01-a7d7-dda51fa37266 | -7.70953 | -44.72947 | 2026-10-09 16:01:00 | NPP-375 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 66c19e1e-9c5f-3aa6-bf08-88c89ea98563 | -8.90724 | -45.40543 | 2026-10-09 16:01:00 | NPP-375 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 417726ba-8da4-39f1-bca3-d8ee18e7a00c | -11.09082 | -44.07008 | 2026-10-09 16:01:00 | NPP-375 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 25.6 |
| 68762071-dce9-3ffb-8d42-7ddf7b5930b0 | -5.99774 | -43.60784 | 2026-10-09 16:01:00 | NPP-375 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 247c7722-fc06-3483-9ea8-3a15e5a43699 | -9.92572 | -44.80847 | 2026-10-09 16:01:00 | NPP-375 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 71.6 |
| bb8615d9-9b69-3646-986b-cafd19cbad7a | -8.6768 | -41.18992 | 2026-10-09 16:01:00 | NPP-375 | AFRÂNIO | PERNAMBUCO | Brasil | 2600203 | 26 | 33 | nan | nan | nan | Caatinga | 4.9 |
| 1d917813-aa7d-3c9f-8645-885bcba31c69 | -7.49107 | -42.79472 | 2026-10-09 16:01:00 | NPP-375 | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | 5.4 |
| 1419351c-62b7-33a1-8b3e-b906f057bc31 | -6.58821 | -47.3634 | 2026-10-09 16:01:00 | NPP-375 | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 6.4 |
| e2a445ba-a015-3060-b2b9-b7906bc256e9 | -11.23969 | -46.30385 | 2026-10-09 16:01:00 | NPP-375 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 11.8 |
| c37daa75-f4a1-3bf4-b44b-6fa89fa13aba | -6.70716 | -44.12023 | 2026-10-09 16:01:00 | NPP-375 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 8.0 |
| d2447674-932f-3872-9005-0060b82cc371 | -10.98881 | -45.51173 | 2026-10-09 16:01:00 | NPP-375 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 7f1c144a-4052-3d7e-a15c-9c20b2eb8b29 | -9.02196 | -44.36795 | 2026-10-09 16:01:00 | NPP-375 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 13.0 |
| 3e162e9c-6b64-31bd-8653-ae1b6ba5f5b3 | -6.9026 | -38.55033 | 2026-10-09 16:01:00 | NPP-375 | CAJAZEIRAS | PARAÍBA | Brasil | 2503704 | 25 | 33 | nan | nan | nan | Caatinga | 14.3 |
| 2458b5c6-4ee6-3d7c-a91e-2d92ca1655fb | -9.84159 | -44.78162 | 2026-10-09 16:01:00 | NPP-375 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 15.3 |
| d0334a0a-b871-3073-ae44-1a16349b9776 | -7.37844 | -44.03099 | 2026-10-09 16:01:00 | NPP-375 | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 20.2 |
| 5a700d28-7369-3467-9525-6af557e4d328 | -6.84201 | -41.75071 | 2026-10-09 16:01:00 | NPP-375 | IPIRANGA DO PIAUÍ | PIAUÍ | Brasil | 2204808 | 22 | 33 | nan | nan | nan | Caatinga | 7.9 |
| 44c2040d-12a3-3795-90b4-0cd79ae61c5f | -9.91016 | -44.78255 | 2026-10-09 16:01:00 | NPP-375 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 25.8 |
| 67340e7f-1b09-3571-a9e9-126e6d0888be | -8.92026 | -45.16191 | 2026-10-09 16:01:00 | NPP-375 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 7.2 |
| ca7c7f0b-6568-3a41-986c-a8627e623ca7 | -7.04279 | -42.29765 | 2026-10-09 16:01:00 | NPP-375 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 6.6 |
| 927c22b1-4563-38fd-9e52-0f9e66d52dd2 | -9.17817 | -43.3846 | 2026-10-09 16:01:00 | NPP-375 | CARACOL | PIAUÍ | Brasil | 2202505 | 22 | 33 | nan | nan | nan | Caatinga | 19.9 |
| 7e63e577-9668-3872-a557-40a165951b99 | -8.99552 | -45.95152 | 2026-10-09 16:01:00 | NPP-375 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 27.2 |
| c69efe1f-3550-395b-840a-7f261cd170cb | -10.46192 | -47.19301 | 2026-10-09 16:01:00 | NPP-375 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 95.5 |
| d4453f90-cdfb-34cd-a078-2c24aea13402 | -7.47661 | -42.84253 | 2026-10-09 16:01:00 | NPP-375 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 5.4 |
| 91a4ae07-2d41-3121-95be-7b1a67cc1182 | -6.48717 | -42.70238 | 2026-10-09 16:01:00 | NPP-375 | AMARANTE | PIAUÍ | Brasil | 2200509 | 22 | 33 | nan | nan | nan | Caatinga | 10.7 |
| 17fa240b-f354-3893-9a30-ee8f3c08d1b9 | -6.96907 | -45.28334 | 2026-10-09 16:01:00 | NPP-375 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 5.0 |
| a070f76f-8d9a-3979-bc56-fb69e80ce345 | -8.94185 | -45.1356 | 2026-10-09 16:01:00 | NPP-375 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 11.4 |
| 3cba018c-3591-362a-880e-c27dc33c563e | -9.93843 | -43.56223 | 2026-10-09 16:01:00 | NPP-375 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 43.4 |
| ed8fdffa-65d5-31d0-8c04-08fa99467a96 | -7.26862 | -43.51012 | 2026-10-09 16:01:00 | NPP-375 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Caatinga | 4.5 |
| 0b13c531-465e-35f9-9efe-0d0619e41cdc | -5.35572 | -43.40599 | 2026-10-09 16:01:00 | NPP-375 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 34bd6a8b-6313-3c6c-8917-1f48c719f480 | -7.4762 | -42.83949 | 2026-10-09 16:01:00 | NPP-375 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 5.4 |
| 8faab0a8-0d75-309a-9181-8ddf3edf54a2 | -7.59393 | -43.07907 | 2026-10-09 16:01:00 | NPP-375 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 2d1cac7a-56f1-3376-8a15-ea22e9a7b0cb | -9.75412 | -45.69056 | 2026-10-09 16:01:00 | NPP-375 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 34.6 |
| b2c8f995-2ba0-3f33-bece-d6e011039c25 | -6.15302 | -47.92544 | 2026-10-09 16:01:00 | NPP-375 | CACHOEIRINHA | TOCANTINS | Brasil | 1703826 | 17 | 33 | nan | nan | nan | Cerrado | 11.2 |
| 878cbd04-4dd6-3ad4-95bc-147e9d75482e | -8.39371 | -39.56126 | 2026-10-09 16:01:00 | NPP-375 | OROCÓ | PERNAMBUCO | Brasil | 2609808 | 26 | 33 | nan | nan | nan | Caatinga | 11.4 |
| 6a30e70f-f7fd-303f-a590-f68f4eb7fbd5 | -10.28623 | -43.93539 | 2026-10-09 16:01:00 | NPP-375 | AVELINO LOPES | PIAUÍ | Brasil | 2201101 | 22 | 33 | nan | nan | nan | Cerrado | 10.1 |
| 6a42ad65-a102-3a4a-acea-24987b5ce0dc | -10.28046 | -43.93602 | 2026-10-09 16:01:00 | NPP-375 | AVELINO LOPES | PIAUÍ | Brasil | 2201101 | 22 | 33 | nan | nan | nan | Cerrado | 7.8 |
| ed2b7e7f-46a3-3bef-9941-c21f9ed1d351 | -8.91473 | -45.16742 | 2026-10-09 16:01:00 | NPP-375 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 7.9 |
| e12a5c12-f177-36cb-8a3c-68fdd814133c | -7.00314 | -47.68676 | 2026-10-09 16:01:00 | NPP-375 | BABAÇULÂNDIA | TOCANTINS | Brasil | 1703008 | 17 | 33 | nan | nan | nan | Cerrado | 28.5 |
| fb981088-530e-33db-b66e-24dc8fa4ca77 | -8.17299 | -40.00422 | 2026-10-09 16:01:00 | NPP-375 | PARNAMIRIM | PERNAMBUCO | Brasil | 2610400 | 26 | 33 | nan | nan | nan | Caatinga | 7.2 |
| 6859b502-51b4-3707-a890-1231e5f97492 | -6.0601 | -42.59429 | 2026-10-09 16:01:00 | NPP-375 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 10.2 |
| a7557f28-855a-3e76-9475-0041de6559ba | -11.22121 | -45.30576 | 2026-10-09 16:01:00 | NPP-375 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 156.0 |
| d3a9ae5c-5039-324e-aab8-d5be77afc2ef | -5.17777 | -42.68954 | 2026-10-09 16:01:00 | NPP-375 | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Cerrado | 4.1 |
| a809288c-335f-3d18-bf8b-70285ca78238 | -7.19328 | -44.27411 | 2026-10-09 16:01:00 | NPP-375 | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 8.3 |
| f7afa83d-31c1-33e1-ad0d-f748efdb38f9 | -10.88515 | -45.51529 | 2026-10-09 16:01:00 | NPP-375 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 9.9 |
| 5416ad3b-fc5a-375c-aa0e-67593921fc4d | -11.0112 | -45.41973 | 2026-10-09 16:01:00 | NPP-375 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 9.8 |
| 6cbadd81-fba7-3d24-92fc-52f68e725e81 | -7.50817 | -45.3073 | 2026-10-09 16:01:00 | NPP-375 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 26.8 |
| 039d0b3a-b4d8-383b-b2cc-96763cdd1d80 | -7.72092 | -43.9628 | 2026-10-09 16:01:00 | NPP-375 | BERTOLÍNIA | PIAUÍ | Brasil | 2201705 | 22 | 33 | nan | nan | nan | Cerrado | 3.5 |
| cb0cb69f-0d06-39f9-9ccb-4de9388cdf75 | -7.46779 | -42.81577 | 2026-10-09 16:01:00 | NPP-375 | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | 8.3 |
| 4bdddff4-07dd-3c8c-9987-488ebf1c4346 | -8.23388 | -40.57429 | 2026-10-09 16:01:00 | NPP-375 | SANTA FILOMENA | PERNAMBUCO | Brasil | 2612554 | 26 | 33 | nan | nan | nan | Caatinga | 11.3 |
| 4a908e94-0151-3741-b0c6-fceff0049510 | -5.60902 | -44.11871 | 2026-10-09 16:01:00 | NPP-375 | GOVERNADOR LUIZ ROCHA | MARANHÃO | Brasil | 2104628 | 21 | 33 | nan | nan | nan | Cerrado | 7.4 |
| 45099711-79b9-3a41-b5f7-7eefa5600719 | -8.84263 | -45.4266 | 2026-10-09 16:01:00 | NPP-375 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 6.9 |
| a1eabf99-b255-3474-ad3d-43c632cfebe5 | -6.00489 | -40.96466 | 2026-10-09 16:01:00 | NPP-375 | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 47.8 |
| 241f78cc-8c2d-318d-9034-57b41e38a466 | -7.30284 | -44.01107 | 2026-10-09 16:01:00 | NPP-375 | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 10.3 |
| 424870b2-3a5e-34b9-89df-e521a7657b20 | -6.97042 | -45.24756 | 2026-10-09 16:01:00 | NPP-375 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 816591eb-04bb-368f-80d0-6d1a2352a58d | -5.12633 | -37.09018 | 2026-10-09 16:01:00 | NPP-375 | SERRA DO MEL | RIO GRANDE DO NORTE | Brasil | 2413359 | 24 | 33 | nan | nan | nan | Caatinga | 4.4 |
| f8c2fa31-d497-3858-9a5b-0ec6ba5f06ac | -11.06401 | -44.09468 | 2026-10-09 16:01:00 | NPP-375 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 58.0 |
| 7018cc8e-1bf0-3767-8757-346e68f1ddcb | -6.02355 | -38.48805 | 2026-10-09 16:01:00 | NPP-375 | PEREIRO | CEARÁ | Brasil | 2310803 | 23 | 33 | nan | nan | nan | Caatinga | 33.6 |


[Clique aqui para ver as próximas entradas](README273.md)
