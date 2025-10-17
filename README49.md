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
| 272302e1-189e-30bd-b362-bfd29f691591 | -6.84883 | -44.38934 | 2025-10-17 04:19:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 856ccdd8-d51b-378e-948a-d92199acb493 | -5.48609 | -42.92631 | 2025-10-17 04:19:00 | NOAA-21 | NAZÁRIA | PIAUÍ | Brasil | 2206720 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 153c7277-bc6a-3426-94c2-512190ca9fb6 | -3.65893 | -50.27002 | 2025-10-17 04:19:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 8aaa4bd8-a772-37fd-9439-138b78193c63 | -10.15298 | -44.53337 | 2025-10-17 04:19:00 | NOAA-21 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 10.0 |
| 414d7883-4c21-3371-abba-a72c0c7eb50d | -4.95468 | -49.57452 | 2025-10-17 04:19:00 | NOAA-21 | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| a7a5d5ff-13a6-3615-b9cf-d1b635f8c514 | -6.59022 | -43.92968 | 2025-10-17 04:19:00 | NOAA-21 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 6e28e6bf-0d9b-397b-9017-8a10c6c61923 | -8.6327 | -45.68765 | 2025-10-17 04:19:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| bc42c57f-56c7-3cf3-a6f3-0aaf851a48a4 | -5.16495 | -42.91429 | 2025-10-17 04:19:00 | NOAA-21 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| e620dec2-fc50-370b-ac15-68eec0098336 | -7.47063 | -42.65276 | 2025-10-17 04:19:00 | NOAA-21 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 5f428e65-63e4-3580-be0a-786f7adc7b68 | -6.68982 | -40.87719 | 2025-10-17 04:19:00 | NOAA-21 | PIO IX | PIAUÍ | Brasil | 2208205 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| b0f20d89-78b1-3d97-92b7-d21d13c3b19a | -6.93811 | -43.68176 | 2025-10-17 04:19:00 | NOAA-21 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 261f49b9-f855-31e0-9bca-03caecfd6d81 | -3.81743 | -52.34624 | 2025-10-17 04:19:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 8038de52-3bea-3fca-95ae-e9cf5b51b37d | -10.64838 | -45.24547 | 2025-10-17 04:19:00 | NOAA-21 | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 33698af3-a792-3486-8413-027e6f3ca0b0 | -8.33262 | -46.22971 | 2025-10-17 04:19:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 2983bd30-071f-3354-a817-21f7bc3c0a09 | -5.72944 | -44.51949 | 2025-10-17 04:19:00 | NOAA-21 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 0602b615-c8a9-3465-8ec4-a19303012f12 | -9.04638 | -47.91585 | 2025-10-17 04:19:00 | NOAA-21 | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 7464482b-8542-3ad1-9d06-041f08e3c308 | -3.4746 | -49.92241 | 2025-10-17 04:19:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 5951dda5-62ec-336d-9f52-69c9af7c4f96 | -10.50727 | -43.41603 | 2025-10-17 04:19:00 | NOAA-21 | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 49d0fbb3-6743-37e2-acc5-ea64e8c16367 | -3.51491 | -52.48975 | 2025-10-17 04:19:00 | NOAA-21 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 7a57b6f8-eddf-3cea-8f3a-41d1ba2a5c2a | -5.83751 | -45.54139 | 2025-10-17 04:19:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 5b59336a-621f-3d87-88f7-be1740d5114c | -5.91779 | -44.75056 | 2025-10-17 04:19:00 | NOAA-21 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 70e6c454-01c2-3f51-8dc5-551acbda49ff | -5.87897 | -44.82565 | 2025-10-17 04:19:00 | NOAA-21 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 4bb0772e-bda0-30f2-9169-85be8c91a730 | -9.65575 | -48.71903 | 2025-10-17 04:19:00 | NOAA-21 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| cc854e60-08ea-39e6-98b0-d1bdf990fb89 | -11.48155 | -44.28574 | 2025-10-17 04:19:00 | NOAA-21 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| bae39221-baba-33ea-8bba-fceb9dd03bb0 | -4.01774 | -44.19288 | 2025-10-17 04:19:00 | NOAA-21 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| f6a59c2b-601f-3e56-acb6-db5137643370 | -5.24419 | -50.95763 | 2025-10-17 04:19:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 932f1a8d-db5a-3397-baa5-6d6d9cbda774 | -5.33517 | -44.84163 | 2025-10-17 04:19:00 | NOAA-21 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 2eebd8b4-9725-3681-bc2a-bf1537a44289 | -11.39759 | -44.2132 | 2025-10-17 04:19:00 | NOAA-21 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 5fb1846f-c384-3022-a6cb-f40049a800f5 | -5.99164 | -44.14855 | 2025-10-17 04:19:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 89706220-3d8d-34c8-8698-e564a60f41d3 | -6.15924 | -40.90037 | 2025-10-17 04:19:00 | NOAA-21 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| b9ac0711-d5cf-3c45-bc84-b00c075a3b7e | -7.29479 | -41.95005 | 2025-10-17 04:19:00 | NOAA-21 | WALL FERRAZ | PIAUÍ | Brasil | 2211704 | 22 | 33 | nan | nan | nan | Caatinga | 2.9 |
| 4c9b8beb-54f9-33ed-92ae-575d950e105b | -9.09403 | -46.6828 | 2025-10-17 04:19:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 45e2780d-5c9e-31a4-9606-96be017ec13f | -10.29816 | -44.03093 | 2025-10-17 04:19:00 | NOAA-21 | AVELINO LOPES | PIAUÍ | Brasil | 2201101 | 22 | 33 | nan | nan | nan | Cerrado | 7.3 |
| 3a7755a7-87b5-3618-b7e9-79e577e06c75 | -10.81315 | -44.01559 | 2025-10-17 04:19:00 | NOAA-21 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| bd23e358-fd01-316d-82fd-a91aed5cdca2 | -10.4692 | -44.0644 | 2025-10-17 04:19:00 | NOAA-21 | JÚLIO BORGES | PIAUÍ | Brasil | 2205524 | 22 | 33 | nan | nan | nan | Cerrado | 0.6 |
| c420dc8f-e634-3c20-b216-d24ea43bb7f8 | -10.5354 | -44.50188 | 2025-10-17 04:19:00 | NOAA-21 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 21e7b4d8-df01-3271-92cd-f198bc384417 | -10.12333 | -44.55065 | 2025-10-17 04:19:00 | NOAA-21 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 3ca6faa7-bea3-3655-b12d-386660ae9ec3 | -6.83026 | -41.69437 | 2025-10-17 04:19:00 | NOAA-21 | IPIRANGA DO PIAUÍ | PIAUÍ | Brasil | 2204808 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 22888800-75ac-3289-a54f-2ea966734579 | -9.92136 | -45.35041 | 2025-10-17 04:19:00 | NOAA-21 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 0112d511-c3d8-3a59-a8c7-98b89bd69ebd | -5.46574 | -44.63973 | 2025-10-17 04:19:00 | NOAA-21 | SANTA FILOMENA DO MARANHÃO | MARANHÃO | Brasil | 2109759 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| c8b2e3ca-cae8-3965-bb37-dae044e4c406 | -4.88519 | -49.95031 | 2025-10-17 04:19:00 | NOAA-21 | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| afec58f5-1c47-3230-a2de-69985d4d6ab7 | -11.44743 | -43.47849 | 2025-10-17 04:19:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| d4620bc4-3df4-3200-b74a-229932591d06 | -11.40034 | -44.19484 | 2025-10-17 04:19:00 | NOAA-21 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 420cea62-8925-3103-9492-1347b04207e9 | -10.30981 | -43.90915 | 2025-10-17 04:19:00 | NOAA-21 | AVELINO LOPES | PIAUÍ | Brasil | 2201101 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 20cca48b-8d86-3238-9e7f-9638e6e99fc7 | -6.36816 | -43.58344 | 2025-10-17 04:19:00 | NOAA-21 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 9a0f0e66-1049-3eaa-817c-8846cd6e2f1d | -11.46231 | -44.24205 | 2025-10-17 04:19:00 | NOAA-21 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| c91b71d8-49f7-3f7b-96bb-c3f886c70d40 | -7.53931 | -42.0588 | 2025-10-17 04:19:00 | NOAA-21 | SANTO INÁCIO DO PIAUÍ | PIAUÍ | Brasil | 2209500 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 0d167ccf-4c80-38dc-bc68-c91f4ef417b6 | -8.91038 | -47.97201 | 2025-10-17 04:19:00 | NOAA-21 | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 1cb6a378-3b8e-3687-91cd-f99164d9918e | -8.22326 | -43.99359 | 2025-10-17 04:19:00 | NOAA-21 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 8efd5b69-a5b4-3573-aa80-a418a610b1d0 | -7.33403 | -44.15692 | 2025-10-17 04:19:00 | NOAA-21 | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 30b2ba62-4248-3ab5-9621-a50b2a21436b | -4.51021 | -46.01017 | 2025-10-17 04:19:00 | NOAA-21 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 12.0 |
| 96dcad29-46bf-3e3c-8451-5752393667ba | -7.1992 | -45.49716 | 2025-10-17 04:19:00 | NOAA-21 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 61fae489-ba8c-3c71-9fb4-d8b9270c16df | -6.2199 | -44.42765 | 2025-10-17 04:19:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| f319da02-27e9-3b28-a8c2-3140b9a8a025 | -8.4507 | -44.74218 | 2025-10-17 04:19:00 | NOAA-21 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| b9e9e8f8-1218-31ec-b81f-0a4a6d3c4ce3 | -6.20479 | -41.75829 | 2025-10-17 04:19:00 | NOAA-21 | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 8.8 |
| c7926421-050d-3e28-918a-073ff331bfac | -8.39633 | -46.27684 | 2025-10-17 04:19:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| e02bbb0a-039d-38aa-94c5-1cecbcfb2d04 | -6.93416 | -44.89097 | 2025-10-17 04:19:00 | NOAA-21 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| e4904ffb-b8a6-3d47-871b-d0a5a01f83b3 | -9.01985 | -46.6157 | 2025-10-17 04:19:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| ad08da8c-5bc8-38eb-9e32-5851c4cf1acf | -11.41109 | -44.21531 | 2025-10-17 04:19:00 | NOAA-21 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 512fd922-ca28-3be3-86cf-93b80a76f694 | -7.83359 | -44.13816 | 2025-10-17 04:19:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 4a3050d6-3247-316b-91b4-4a469a9448c1 | -9.09461 | -46.67921 | 2025-10-17 04:19:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 05c69d81-11ff-3bc7-a33d-44546bf281b0 | -7.75349 | -42.49288 | 2025-10-17 04:19:00 | NOAA-21 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 3aa3761d-033f-37ca-920f-37e80a573671 | -11.41274 | -44.2043 | 2025-10-17 04:19:00 | NOAA-21 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 3.0 |
| c9152056-84b2-334f-b38b-37d14a2eb3c0 | -9.14062 | -46.64968 | 2025-10-17 04:19:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 6.1 |
| e9bb8557-340d-374c-b1f1-483b0cb105b1 | -6.49737 | -44.46127 | 2025-10-17 04:19:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 35b2734b-63e2-3009-9f06-ec09bba6ffa8 | -6.21084 | -47.87774 | 2025-10-17 04:19:00 | NOAA-21 | LUZINÓPOLIS | TOCANTINS | Brasil | 1712454 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 1f41fc64-7dff-3a01-a609-d8310abd2069 | -6.42372 | -43.09482 | 2025-10-17 04:19:00 | NOAA-21 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| fd2b070b-ff36-3835-b54d-77a258b24ef4 | -10.72315 | -47.58526 | 2025-10-17 04:19:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| f4690176-a247-361a-b4db-2026c3206f29 | -5.87991 | -44.75523 | 2025-10-17 04:19:00 | NOAA-21 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| d1afde53-33d4-3348-ac28-3cf9ab105fdf | -5.18608 | -46.17591 | 2025-10-17 04:19:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c027735a-cbc4-32eb-b104-ee3d44ad643d | -5.87145 | -43.91321 | 2025-10-17 04:19:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 5bcc0e36-d6ed-373e-a660-25ac5de32344 | -10.8378 | -43.94418 | 2025-10-17 04:19:00 | NOAA-21 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| b5bcd997-ffb7-384e-b9b9-73586935b7da | -7.85925 | -43.88232 | 2025-10-17 04:19:00 | NOAA-21 | BERTOLÍNIA | PIAUÍ | Brasil | 2201705 | 22 | 33 | nan | nan | nan | Cerrado | 0.5 |
| ebc5e4c2-eb1e-3445-854e-dcf49b749ef7 | -11.41502 | -44.21216 | 2025-10-17 04:19:00 | NOAA-21 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| ad8933c8-3168-35f6-81f0-16b281db62fe | -6.34742 | -41.51358 | 2025-10-17 04:19:00 | NOAA-21 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| cd19f29e-3de8-3f94-9601-7d45f638dbe7 | -4.15398 | -42.79224 | 2025-10-17 04:19:00 | NOAA-21 | MIGUEL ALVES | PIAUÍ | Brasil | 2206209 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| d02e38c0-87f4-3717-b611-08ca9258f986 | -4.91991 | -41.5603 | 2025-10-17 04:19:00 | NOAA-21 | JUAZEIRO DO PIAUÍ | PIAUÍ | Brasil | 2205516 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| b8d0dae5-b1ad-3100-99d2-e735334d87fc | -5.61015 | -42.68158 | 2025-10-17 04:19:00 | NOAA-21 | MONSENHOR GIL | PIAUÍ | Brasil | 2206407 | 22 | 33 | nan | nan | nan | Caatinga | 4.1 |
| 32ee052d-0704-3bec-b74e-52faa0cb0267 | -8.73115 | -43.87144 | 2025-10-17 04:19:00 | NOAA-21 | CRISTINO CASTRO | PIAUÍ | Brasil | 2203107 | 22 | 33 | nan | nan | nan | Cerrado | 7.2 |
| a1833d69-14d0-32c5-9212-ebadcfc02627 | -9.34223 | -46.91328 | 2025-10-17 04:19:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 51c597bb-1391-342e-b185-c92c3289b0f7 | -11.40544 | -44.20692 | 2025-10-17 04:19:00 | NOAA-21 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 262e5032-a33c-35ba-a7d4-2e7971e5804b | -8.20041 | -43.96464 | 2025-10-17 04:19:00 | NOAA-21 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 08fe4bbc-8e29-3f3a-ad51-64c432baa6c3 | -11.41729 | -44.22003 | 2025-10-17 04:19:00 | NOAA-21 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 3d409246-b6f0-3ddc-b997-9b42ba903433 | -7.20956 | -43.8395 | 2025-10-17 04:19:00 | NOAA-21 | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 4a05a9c8-4e6d-374c-95f7-49c9bfb92444 | -4.93592 | -48.5549 | 2025-10-17 04:19:00 | NOAA-21 | BOM JESUS DO TOCANTINS | PARÁ | Brasil | 1501576 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 7ebb1c02-3881-3eac-9be6-242a75d7c3f3 | -7.0288 | -41.81846 | 2025-10-17 04:19:00 | NOAA-21 | SÃO JOÃO DA VARJOTA | PIAUÍ | Brasil | 2209955 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 048a819e-02c6-3d6d-8851-15fd744376db | -5.74416 | -39.90438 | 2025-10-17 04:19:00 | NOAA-21 | MOMBAÇA | CEARÁ | Brasil | 2308500 | 23 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 29c128ec-f81e-3e5a-b656-f6b3725125e0 | -5.91218 | -46.51707 | 2025-10-17 04:19:00 | NOAA-21 | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| e0685ea8-4171-3406-9ac4-26720de2dab3 | -4.22614 | -48.35878 | 2025-10-17 04:19:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f95dfb6c-9339-3aa8-bbb2-8413bac14d9e | -5.65692 | -46.81284 | 2025-10-17 04:19:00 | NOAA-21 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 7d2cfd5e-a5f2-3f7e-a891-dce9bbc65436 | -8.40799 | -46.28963 | 2025-10-17 04:19:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 10.8 |
| 7d84091f-51d2-3095-90e4-6920eda51fd6 | -10.13107 | -44.54463 | 2025-10-17 04:19:00 | NOAA-21 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 6.3 |
| dde74363-96dd-3301-8fa0-1550fb34ddc1 | -7.75176 | -42.50447 | 2025-10-17 04:19:00 | NOAA-21 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 583dc4ca-6d0e-3ebd-be56-5794d1c95797 | -7.95576 | -44.1182 | 2025-10-17 04:19:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 72e34149-a469-3952-95bc-b21278697eff | -5.46058 | -41.01838 | 2025-10-17 04:19:00 | NOAA-21 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| f218e628-ea3d-3932-820c-b8c37d501a54 | -10.11117 | -44.56323 | 2025-10-17 04:19:00 | NOAA-21 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 23c333a1-6922-3528-8dc7-6b0de71ea4de | -10.12268 | -52.34587 | 2025-10-17 04:19:00 | NOAA-21 | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 01751542-e7a6-3512-8a62-a3c9e3aaa651 | -11.45802 | -44.04128 | 2025-10-17 04:19:00 | NOAA-21 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 080ca57c-6eda-333d-9bf6-6fd1eec68a83 | -10.26619 | -44.0372 | 2025-10-17 04:19:00 | NOAA-21 | AVELINO LOPES | PIAUÍ | Brasil | 2201101 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 27777722-95ec-3373-a2ae-05738399dbe4 | -8.38757 | -46.24602 | 2025-10-17 04:19:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 5.3 |


[Clique aqui para ver as próximas entradas](README50.md)
