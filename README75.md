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

## Dados Diários - Página 75

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 5d22bb49-45e5-35f5-9f91-82376e0717c0 | -7.47616 | -42.14348 | 2025-10-16 05:08:00 | NPP-375D | SANTO INÁCIO DO PIAUÍ | PIAUÍ | Brasil | 2209500 | 22 | 33 | nan | nan | nan | Caatinga | 2.7 |
| e021667c-f7e0-3fd9-8b62-21f1cfc52c5c | -4.65133 | -47.95393 | 2025-10-16 05:08:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| d16eb3ff-c811-3eca-b6a3-69461c54ce83 | -11.21437 | -43.99884 | 2025-10-16 05:08:00 | NPP-375D | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 1532e4ea-869a-30ac-af1c-3cbd54431779 | -7.66266 | -42.3802 | 2025-10-16 05:08:00 | NPP-375D | SÃO MIGUEL DO FIDALGO | PIAUÍ | Brasil | 2210391 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 886ef156-a725-3244-a551-66c1315135f0 | -10.81738 | -43.94283 | 2025-10-16 05:08:00 | NPP-375D | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 62b0e524-a4a6-39f8-991b-e087876dfc1f | -7.8544 | -45.40843 | 2025-10-16 05:08:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 2b3465b4-417a-31e7-91cb-77003be72909 | -11.44716 | -44.05391 | 2025-10-16 05:08:00 | NPP-375D | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 123ef88b-dfe1-3b3f-a25d-3fcd4b36a1a4 | -10.12684 | -52.34664 | 2025-10-16 05:08:00 | NPP-375D | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c3ee5d8d-114e-3d3b-a222-186ac07e76be | -10.05393 | -43.82988 | 2025-10-16 05:08:00 | NPP-375D | AVELINO LOPES | PIAUÍ | Brasil | 2201101 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 4f931978-3b5d-3366-9865-c8f9dbb40598 | -7.48097 | -42.14579 | 2025-10-16 05:08:00 | NPP-375D | SANTO INÁCIO DO PIAUÍ | PIAUÍ | Brasil | 2209500 | 22 | 33 | nan | nan | nan | Caatinga | 2.7 |
| a494f832-2a53-3cab-b4af-814d266aafb0 | -7.48194 | -42.13858 | 2025-10-16 05:08:00 | NPP-375D | SANTO INÁCIO DO PIAUÍ | PIAUÍ | Brasil | 2209500 | 22 | 33 | nan | nan | nan | Caatinga | 2.9 |
| 275a8943-1bcf-38d8-9a8a-1adc7abe8f78 | -9.22468 | -48.59769 | 2025-10-16 05:08:00 | NPP-375D | MIRANORTE | TOCANTINS | Brasil | 1713304 | 17 | 33 | nan | nan | nan | Cerrado | 5.3 |
| a90e4980-f0d0-3b12-a7bb-e369a0d9aa1c | -10.65011 | -45.2523 | 2025-10-16 05:08:00 | NPP-375D | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 295dfa76-c5d6-39ec-bf3f-d8c625649a8b | -7.47278 | -42.1521 | 2025-10-16 05:08:00 | NPP-375D | SANTO INÁCIO DO PIAUÍ | PIAUÍ | Brasil | 2209500 | 22 | 33 | nan | nan | nan | Caatinga | 2.7 |
| 1229ae89-1281-3c71-adce-38f919022bff | -5.87367 | -43.8759 | 2025-10-16 05:08:00 | NPP-375D | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| e85ad775-336f-3581-ba1e-ac14d4b45ac7 | -10.82415 | -43.94375 | 2025-10-16 05:08:00 | NPP-375D | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 69bdf489-c080-310e-98f2-44b4dc764023 | -4.77736 | -49.23728 | 2025-10-16 05:08:00 | NPP-375D | JACUNDÁ | PARÁ | Brasil | 1503804 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 5862e8e8-e07b-3dd3-9553-023006b788e8 | -5.46602 | -42.93742 | 2025-10-16 05:08:00 | NPP-375D | NAZÁRIA | PIAUÍ | Brasil | 2206720 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 8c56244b-6855-3baf-a5de-b96d46a39651 | -5.74653 | -44.98664 | 2025-10-16 05:08:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 27c8272e-0cf3-32df-8310-3280af26f322 | -10.1404 | -44.5645 | 2025-10-16 05:08:00 | NPP-375D | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 5117833c-570d-35b7-b8d6-1f287df4c661 | -7.05921 | -45.0608 | 2025-10-16 05:08:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 978ebdec-52f3-371c-b36d-3a97124924f9 | -8.46972 | -44.19025 | 2025-10-16 05:08:00 | NPP-375D | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 17.3 |
| 39c2b0f7-348b-3f92-bf5a-f3e260d360d0 | -8.27327 | -48.00357 | 2025-10-16 05:08:00 | NPP-375D | ITAPIRATINS | TOCANTINS | Brasil | 1710904 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| ce9dba73-ea02-3ab4-ba75-c3b1e02b3e66 | -9.69014 | -44.5377 | 2025-10-16 05:08:00 | NPP-375D | REDENÇÃO DO GURGUÉIA | PIAUÍ | Brasil | 2208700 | 22 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 97a6b8bd-3179-353c-bb2e-00a5c71700f2 | -7.63891 | -44.09231 | 2025-10-16 05:08:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 3.1 |
| cdbccf9e-a8c4-3ef7-a10b-dae06c4e5d8a | -9.15678 | -46.87072 | 2025-10-16 05:08:00 | NPP-375D | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 25519ede-8ce7-3ac8-b829-9e2f5ab4c971 | -9.68432 | -44.5249 | 2025-10-16 05:08:00 | NPP-375D | REDENÇÃO DO GURGUÉIA | PIAUÍ | Brasil | 2208700 | 22 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 37d9f650-87fb-35dd-81f9-09679929d039 | -7.64015 | -44.08772 | 2025-10-16 05:08:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 5.7 |
| cac600e4-eb99-3e2f-958e-b778e2b207fc | -7.48398 | -47.02791 | 2025-10-16 05:08:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 578ba20e-f69d-3b89-bf08-7748546a67cb | -7.08089 | -44.94281 | 2025-10-16 05:08:00 | NPP-375D | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| b301861c-5a30-35ac-b4e9-0526f41dd553 | -11.44143 | -44.16375 | 2025-10-16 05:08:00 | NPP-375D | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 5cfc538a-847a-303e-8db2-2491e0b65422 | -8.07502 | -45.43295 | 2025-10-16 05:08:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 33bdbca9-1558-3411-87b3-f4a7dca1bf3e | -8.06865 | -45.43523 | 2025-10-16 05:08:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 88ba48dc-2650-3f58-853e-9a6535589fdc | -7.60906 | -46.47493 | 2025-10-16 05:08:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| f99295a4-5164-39a3-9bbf-c522ba99a8b8 | -12.33276 | -47.82777 | 2025-10-16 05:08:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| a3b7cc44-eaff-3f38-9be0-b029979186a9 | -8.38949 | -46.26146 | 2025-10-16 05:08:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 08671c9d-f8dd-3998-9a0e-62e86a0bcacd | -7.93826 | -44.12532 | 2025-10-16 05:08:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 5.3 |
| faeb51bf-e595-3e1c-bac7-9e42c0d490fa | -8.2919 | -43.42113 | 2025-10-16 05:08:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 0b49c46e-071b-3b7f-9970-816e19e01d05 | -8.24665 | -44.13334 | 2025-10-16 05:08:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 240d66c3-4a79-36e7-aff4-8dcc934a12b9 | -8.3018 | -44.97423 | 2025-10-16 05:08:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| b1846e37-0068-33d9-a9e3-2975a6f4d2e8 | -8.24007 | -44.02685 | 2025-10-16 05:08:00 | NPP-375D | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 3.1 |
| a5c05b8b-7e56-3c93-94b3-6b1b40db232d | -5.878 | -43.85064 | 2025-10-16 05:08:00 | NPP-375D | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 89910d39-a600-35ae-a8a6-019e93eebf51 | -7.05821 | -45.05454 | 2025-10-16 05:08:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 3d73be00-dbdb-38e4-913e-171334af3de2 | -11.57658 | -48.56195 | 2025-10-16 05:08:00 | NPP-375D | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 02fcdd9b-b291-363c-ac14-86711c14c181 | -9.6921 | -44.51541 | 2025-10-16 05:08:00 | NPP-375D | REDENÇÃO DO GURGUÉIA | PIAUÍ | Brasil | 2208700 | 22 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 8ffd2bb6-f9e5-3a38-8731-926eff656590 | -4.8171 | -46.83962 | 2025-10-16 05:08:00 | NPP-375D | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 42a183b8-7c6f-3447-bf47-6c38541c74fe | -6.44342 | -43.38578 | 2025-10-16 05:08:00 | NPP-375D | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 60f0fbd0-0aed-37c7-a7e8-6b948d9113c0 | -7.17763 | -42.19151 | 2025-10-16 05:08:00 | NPP-375D | COLÔNIA DO PIAUÍ | PIAUÍ | Brasil | 2202778 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| b3b3dcd6-e154-3bfa-a7db-608559d897c0 | -4.91749 | -45.97781 | 2025-10-16 05:08:00 | NPP-375D | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 1750f6ec-1397-327e-8105-c59a84c8acf2 | -10.72401 | -47.58744 | 2025-10-16 05:08:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 629a3139-21a4-37ed-bdc9-db7bcdc5e6a1 | -9.68371 | -44.53669 | 2025-10-16 05:08:00 | NPP-375D | REDENÇÃO DO GURGUÉIA | PIAUÍ | Brasil | 2208700 | 22 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 9ccf5bb3-be28-3504-8faa-c5c9e20b1db2 | -8.56282 | -44.59085 | 2025-10-16 05:08:00 | NPP-375D | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 05a201a9-383d-379f-bde4-ea52141b605f | -9.68564 | -44.52079 | 2025-10-16 05:08:00 | NPP-375D | REDENÇÃO DO GURGUÉIA | PIAUÍ | Brasil | 2208700 | 22 | 33 | nan | nan | nan | Cerrado | 7.0 |
| 0c3fce3c-acd0-32af-9428-380401f71c1d | -6.56444 | -42.973 | 2025-10-16 05:08:00 | NPP-375D | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 0027daf8-b7ef-38ef-9b8c-d5d3747fe76b | -8.19336 | -43.32059 | 2025-10-16 05:08:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 8.0 |
| 6ad88776-0d0a-3554-b606-4cdd17f58c82 | -7.96242 | -44.13939 | 2025-10-16 05:08:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 3.3 |
| cca031b5-5414-3d0f-81ee-cfcced317241 | -11.46025 | -44.17825 | 2025-10-16 05:08:00 | NPP-375D | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 078e5aeb-0daa-3f38-98f0-05443ac7be2a | -7.40545 | -44.75124 | 2025-10-16 05:08:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 0328c573-6884-3651-a05f-a72a2ee74129 | -10.83756 | -44.00519 | 2025-10-16 05:08:00 | NPP-375D | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 06b4546c-f659-366c-9a15-927c0e0d08c0 | -6.47718 | -48.76429 | 2025-10-16 05:08:00 | NPP-375D | PIÇARRA | PARÁ | Brasil | 1505635 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| f3650693-6755-3420-9aa6-f570b8567bc0 | -10.13135 | -44.58469 | 2025-10-16 05:08:00 | NPP-375D | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 8.0 |
| 1b274c86-8e3f-3a8d-84d7-00c3b5c70eef | -7.05405 | -46.68301 | 2025-10-16 05:08:00 | NPP-375D | FEIRA NOVA DO MARANHÃO | MARANHÃO | Brasil | 2104073 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| e9786065-2860-3c40-85ec-0fe486c6bdbc | -6.57292 | -42.96156 | 2025-10-16 05:08:00 | NPP-375D | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| d2073cb2-84b9-36b5-92b8-b4901f104126 | -5.47639 | -42.93276 | 2025-10-16 05:08:00 | NPP-375D | NAZÁRIA | PIAUÍ | Brasil | 2206720 | 22 | 33 | nan | nan | nan | Caatinga | 5.8 |
| 8f2c5f67-be8b-3d13-98bc-f1a21d5e7f49 | -10.13327 | -44.56899 | 2025-10-16 05:08:00 | NPP-375D | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| e475300b-b21b-35f4-9e25-20d77ae46da9 | -8.07229 | -45.43088 | 2025-10-16 05:08:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 96faed5c-4b92-3e3f-ab86-a08aef739c6c | -6.32383 | -44.32042 | 2025-10-16 05:08:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 2aad8572-09e3-3278-92ed-9b77c08bdb4d | -7.94401 | -44.13157 | 2025-10-16 05:08:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 9aedcedc-9299-3a1d-9e0f-cafa71240766 | -6.54727 | -43.92349 | 2025-10-16 05:08:00 | NPP-375D | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 2d66af91-6b30-325a-83ca-a6193a2df6ab | -8.46363 | -44.18813 | 2025-10-16 05:08:00 | NPP-375D | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 19.6 |
| cd2e53d0-651d-3df5-99d4-8cf7eb8fb898 | -5.83762 | -42.34521 | 2025-10-16 05:08:00 | NPP-375D | PASSAGEM FRANCA DO PIAUÍ | PIAUÍ | Brasil | 2207751 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| e495befb-14ef-3b64-b1ae-afc09473f2a6 | -10.72357 | -47.59079 | 2025-10-16 05:08:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| ae25da18-ba94-3877-8094-fb213b3dd3d4 | -9.16276 | -46.86897 | 2025-10-16 05:08:00 | NPP-375D | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| c3cafad0-3789-3f28-a50c-631312cc1374 | -7.11608 | -44.72239 | 2025-10-16 05:08:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 22bcc164-4475-3f26-8578-003411d9f564 | -9.7114 | -44.52477 | 2025-10-16 05:08:00 | NPP-375D | REDENÇÃO DO GURGUÉIA | PIAUÍ | Brasil | 2208700 | 22 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 6697f14c-9c6f-3f0a-b88d-a034a3f0e527 | -6.03989 | -41.92034 | 2025-10-16 05:08:00 | NPP-375D | SANTA CRUZ DOS MILAGRES | PIAUÍ | Brasil | 2209153 | 22 | 33 | nan | nan | nan | Caatinga | 4.7 |
| 8a6f3c1f-dd75-3a0b-94fe-0b08ee5a5c96 | -10.6507 | -45.24737 | 2025-10-16 05:08:00 | NPP-375D | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 016c520a-9885-3b3c-950f-7dcf07aa104e | -7.20832 | -45.49165 | 2025-10-16 05:08:00 | NPP-375D | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 340b2f64-ab60-382f-8c91-b060602135f3 | -8.41963 | -44.73774 | 2025-10-16 05:08:00 | NPP-375D | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 2d10202c-abb8-3eb9-b803-4128bfdc0f3a | -8.24597 | -44.13873 | 2025-10-16 05:08:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 8e8746b2-6e41-3828-99b6-d9caf0678f46 | -5.12516 | -50.42209 | 2025-10-16 05:08:00 | NPP-375D | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c7e5bf00-d340-3294-9bb6-0a257d5e3266 | -5.87153 | -43.85025 | 2025-10-16 05:08:00 | NPP-375D | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 616bdb9f-1164-355a-9c5f-e91a116cd551 | -5.30425 | -49.57685 | 2025-10-16 05:08:00 | NPP-375D | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 0ebeb944-1b13-3b80-9892-5fdc8ff3acff | -5.60814 | -49.03498 | 2025-10-16 05:08:00 | NPP-375D | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| eb675024-05d0-3440-a820-720aa764dc00 | -7.54164 | -44.28149 | 2025-10-16 05:08:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 7e2d603b-e0ee-3686-b035-9fe117c7000e | -6.05333 | -41.92946 | 2025-10-16 05:08:00 | NPP-375D | SANTA CRUZ DOS MILAGRES | PIAUÍ | Brasil | 2209153 | 22 | 33 | nan | nan | nan | Caatinga | 3.5 |
| fbe0a096-1865-352d-94e4-45a86099d991 | -9.08455 | -47.95098 | 2025-10-16 05:08:00 | NPP-375D | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 7.8 |
| e3a09da6-d4c3-3425-90a6-a85060d2d2ee | -6.22688 | -44.1554 | 2025-10-16 05:08:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| a311691b-e96b-39ef-9b27-d803f39d03d7 | -5.47192 | -42.94418 | 2025-10-16 05:08:00 | NPP-375D | NAZÁRIA | PIAUÍ | Brasil | 2206720 | 22 | 33 | nan | nan | nan | Caatinga | 10.8 |
| 791fa8dd-70bd-3502-b8f9-9d91b702910f | -11.44074 | -44.16975 | 2025-10-16 05:08:00 | NPP-375D | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 1e971609-3e50-3852-b848-bb83f782d1d9 | -8.40373 | -46.24218 | 2025-10-16 05:08:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 56a39bd8-7a70-3fc2-b64d-7e8920802c35 | -6.71297 | -44.38039 | 2025-10-16 05:08:00 | NPP-375D | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 761d8e72-2134-30f2-9aa6-527f5e8cd50e | -10.6646 | -45.28991 | 2025-10-16 05:08:00 | NPP-375D | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 138246c3-42f2-34f6-8d2f-e8e495820e8e | -10.42193 | -48.8848 | 2025-10-16 05:08:00 | NPP-375D | PUGMIL | TOCANTINS | Brasil | 1718451 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 80555315-2cca-3efd-a622-1afa06cf6bf0 | -7.95455 | -44.14946 | 2025-10-16 05:08:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 3fbd5330-39a0-3994-b086-8dbaf0264c7e | -8.40337 | -46.26197 | 2025-10-16 05:08:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 416b0121-214f-3fd2-b802-8ce64828d30d | -6.04424 | -41.94263 | 2025-10-16 05:08:00 | NPP-375D | SANTA CRUZ DOS MILAGRES | PIAUÍ | Brasil | 2209153 | 22 | 33 | nan | nan | nan | Caatinga | 2.8 |
| 371ba4f6-6578-32fb-8710-34a959cbfdac | -8.45777 | -44.18224 | 2025-10-16 05:08:00 | NPP-375D | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 11.3 |
| b28e64a4-7068-3589-aaaa-592640982936 | -6.45697 | -44.58182 | 2025-10-16 05:08:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 24252c52-d636-38d3-b12b-1c888e59b01e | -5.46963 | -42.93198 | 2025-10-16 05:08:00 | NPP-375D | NAZÁRIA | PIAUÍ | Brasil | 2206720 | 22 | 33 | nan | nan | nan | Caatinga | 5.8 |


[Clique aqui para ver as próximas entradas](README76.md)
