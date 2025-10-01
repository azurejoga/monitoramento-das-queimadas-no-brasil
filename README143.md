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

## Dados Diários - Página 143

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 35fa8ed0-58d4-36f5-9ced-8482fa54e1a4 | -13.66574 | -48.04135 | 2025-10-01 12:00:00 | TERRA_M-T | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 35.9 |
| 93c63969-cb4e-390e-8f98-91636f0f8e6f | -8.6499 | -43.98431 | 2025-10-01 12:00:00 | TERRA_M-T | CRISTINO CASTRO | PIAUÍ | Brasil | 2203107 | 22 | 33 | nan | nan | nan | Cerrado | 26.1 |
| 414635c5-1594-3085-a5c5-883daccb8a3d | -10.89983 | -46.55647 | 2025-10-01 12:00:00 | TERRA_M-T | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 14.8 |
| 89c850f2-8532-3640-ab0b-085a36d020b4 | -15.00986 | -39.73559 | 2025-10-01 12:00:00 | TERRA_M-T | ITAJU DO COLÔNIA | BAHIA | Brasil | 2915403 | 29 | 33 | nan | nan | nan | Mata Atlântica | 9.9 |
| d3d1278e-2812-399c-bad9-a31d7e48ed2e | -9.94523 | -43.5819 | 2025-10-01 12:00:00 | TERRA_M-T | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 9.3 |
| 204883c5-9733-3c93-8b1a-49a4dd2362f7 | -13.77935 | -47.97921 | 2025-10-01 12:00:00 | TERRA_M-T | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 15.4 |
| a6dae4a7-0071-3c9d-9dc6-010e875b358c | -10.21447 | -48.21182 | 2025-10-01 12:00:00 | TERRA_M-T | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 27.6 |
| 520e9585-b80c-38c1-8712-0ebfd82cf646 | -11.19628 | -47.75179 | 2025-10-01 12:00:00 | TERRA_M-T | PINDORAMA DO TOCANTINS | TOCANTINS | Brasil | 1717008 | 17 | 33 | nan | nan | nan | Cerrado | 12.0 |
| 6f58ced6-2c84-3ece-9597-49a15cd3f32f | -9.80704 | -45.93075 | 2025-10-01 12:00:00 | TERRA_M-T | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 19.7 |
| 5550abdb-ff5b-3467-beda-d377476fea3c | -8.75149 | -45.92802 | 2025-10-01 12:00:00 | TERRA_M-T | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 22.0 |
| 971904df-f306-39e6-92ae-5804552b9ba4 | -13.66352 | -48.03491 | 2025-10-01 12:00:00 | TERRA_M-T | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 13.5 |
| 48957f10-be7e-3f02-bad0-953bac1e568e | -10.91469 | -44.32688 | 2025-10-01 12:00:00 | TERRA_M-T | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 1584968c-58d8-3e2c-a948-1a348a1961b1 | -12.8505 | -46.86685 | 2025-10-01 12:00:00 | TERRA_M-T | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 8.5 |
| 3895b1a1-e02a-3f30-a602-a2da7009b615 | -10.9036 | -46.53209 | 2025-10-01 12:00:00 | TERRA_M-T | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 19.4 |
| 4e3acfff-cf67-3487-8966-fb29230c5b86 | -11.78541 | -47.59367 | 2025-10-01 12:00:00 | TERRA_M-T | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 11.7 |
| 7affccfe-6818-36bc-8c0e-4969b0e0df9e | -8.5219 | -44.6613 | 2025-10-01 12:00:00 | TERRA_M-T | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 14.0 |
| ce53afc8-d501-3793-82fa-d19fa287cc9b | -8.93022 | -47.57848 | 2025-10-01 12:00:00 | TERRA_M-T | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 30.7 |
| 8be48fea-9023-3da4-8340-f45e9008b599 | -11.86856 | -48.01952 | 2025-10-01 12:00:00 | TERRA_M-T | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 23.2 |
| abbe0740-1321-34f6-ae5e-3d2acabfc5df | -9.92788 | -43.70011 | 2025-10-01 12:00:00 | TERRA_M-T | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Cerrado | 168.9 |
| 5d4caa89-66ed-3a09-9b52-081751e8791b | -12.78989 | -46.86363 | 2025-10-01 12:00:00 | TERRA_M-T | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 21.5 |
| 8059f308-2f00-3687-8707-42baa5a3ab63 | -9.20426 | -41.02035 | 2025-10-01 12:00:00 | TERRA_M-T | CASA NOVA | BAHIA | Brasil | 2907202 | 29 | 33 | nan | nan | nan | Caatinga | 7.4 |
| c3102c2c-5fc4-35a8-81a0-2158470daba9 | -12.36506 | -50.20851 | 2025-10-01 12:00:00 | TERRA_M-T | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 127.2 |
| 3445f7f9-1724-3d0c-b4f5-9b71a9eab753 | -10.98076 | -46.56257 | 2025-10-01 12:00:00 | TERRA_M-T | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 114.3 |
| 40d3d113-0e18-3263-9a83-6b3dbc3dd9b0 | -14.23256 | -43.51941 | 2025-10-01 12:00:00 | TERRA_M-T | IUIU | BAHIA | Brasil | 2917334 | 29 | 33 | nan | nan | nan | Cerrado | 11.8 |
| b6cfffab-3a41-30be-9912-71e1d96a407e | -8.55305 | -44.64502 | 2025-10-01 12:00:00 | TERRA_M-T | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 15.0 |
| 53e2c139-3e76-3376-aeaf-a15a9e6b4abd | -10.70576 | -46.75503 | 2025-10-01 12:00:00 | TERRA_M-T | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 11.9 |
| 07c58f59-83f0-323a-9476-87fa7bbb5769 | -12.46687 | -50.23235 | 2025-10-01 12:00:00 | TERRA_M-T | SÃO MIGUEL DO ARAGUAIA | GOIÁS | Brasil | 5220207 | 52 | 33 | nan | nan | nan | Cerrado | 134.2 |
| 99e01d30-94a1-31ce-9b02-0df2c1ae9027 | -11.38547 | -45.06489 | 2025-10-01 12:00:00 | TERRA_M-T | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 42.4 |
| b786f340-56ab-3676-a836-8b377efb926d | -14.18511 | -41.35207 | 2025-10-01 12:00:00 | TERRA_M-T | TANHAÇU | BAHIA | Brasil | 2931004 | 29 | 33 | nan | nan | nan | Caatinga | 17.5 |
| 7aa9e2cd-ad01-34de-bde4-90645ca8f519 | -12.82708 | -47.01396 | 2025-10-01 12:00:00 | TERRA_M-T | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 13.5 |
| 8edade3c-8460-3d05-a4c3-43f581c82860 | -12.06607 | -43.07273 | 2025-10-01 12:00:00 | TERRA_M-T | OLIVEIRA DOS BREJINHOS | BAHIA | Brasil | 2923209 | 29 | 33 | nan | nan | nan | Caatinga | 9.8 |
| db9bd71d-870e-3651-82fe-1513ac811667 | -12.22562 | -43.75755 | 2025-10-01 12:00:00 | TERRA_M-T | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 17.9 |
| 1cd88432-d1cc-3b94-a753-8830f068ded4 | -14.34932 | -45.91653 | 2025-10-01 12:00:00 | TERRA_M-T | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 64.4 |
| 058dc0c9-62b4-3a0c-ba35-57cdef2f1dcf | -9.64853 | -45.562 | 2025-10-01 12:00:00 | TERRA_M-T | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 38.8 |
| 1a12eb2c-b232-3e90-9260-8fc42b9913d1 | -7.83659 | -48.1975 | 2025-10-01 12:00:00 | TERRA_M-T | PALMEIRANTE | TOCANTINS | Brasil | 1715705 | 17 | 33 | nan | nan | nan | Cerrado | 84.1 |
| e8e1cdf5-fa4b-39ad-a087-7f84193ebfa2 | -10.63848 | -48.51992 | 2025-10-01 12:00:00 | TERRA_M-T | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 17.6 |
| d95e63c4-5910-340e-9b2a-191dd40f7c2e | -11.86342 | -45.01785 | 2025-10-01 12:00:00 | TERRA_M-T | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 25.9 |
| e0bc75fd-fc5f-30ef-80a3-ee9509195e56 | -9.63879 | -45.56054 | 2025-10-01 12:00:00 | TERRA_M-T | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 14.8 |
| 8a8a4876-90c0-31f8-9cf7-6602813de487 | -11.84133 | -48.04573 | 2025-10-01 12:00:00 | TERRA_M-T | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 23.2 |
| c0831cc3-c46a-3dee-8c91-a5166c256f03 | -8.15882 | -44.12451 | 2025-10-01 12:00:00 | TERRA_M-T | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 7.6 |
| 99cb4616-128c-3d9e-9e75-7e6573dacaee | -7.81908 | -45.11098 | 2025-10-01 12:00:00 | TERRA_M-T | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 4a13f6ba-8605-3fc3-bfd5-d13f3b562cfd | -10.8415 | -46.66071 | 2025-10-01 12:00:00 | TERRA_M-T | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 29.3 |
| 69ba3282-42b2-3e57-8496-a5e0f8c73428 | -8.49519 | -47.78653 | 2025-10-01 12:00:00 | TERRA_M-T | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 57.8 |
| 9f0ccd5d-d46d-3a9d-8498-d9faa1f44b18 | -11.50569 | -43.5102 | 2025-10-01 12:00:00 | TERRA_M-T | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 9.3 |
| f1eac7d4-810a-30ea-ad88-760444b47b1a | -9.80939 | -47.8447 | 2025-10-01 12:00:00 | TERRA_M-T | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 25.8 |
| b6ecfa02-e02d-3761-97f9-4517d8128814 | -13.40864 | -47.55275 | 2025-10-01 12:00:00 | TERRA_M-T | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 16.1 |
| f3421b8c-869e-3b0b-bdea-de263d091efd | -9.93457 | -43.65457 | 2025-10-01 12:00:00 | TERRA_M-T | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 12.9 |
| 89d73978-2da7-3356-8ab1-0f64f916158b | -12.39993 | -45.00777 | 2025-10-01 12:00:00 | TERRA_M-T | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 34.4 |
| 0d593012-8aac-3bd3-bd7d-6d2df45a80c0 | -13.34152 | -47.32811 | 2025-10-01 12:00:00 | TERRA_M-T | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 9.6 |
| d9729b84-7383-3a20-9057-6ce908ca8d38 | -7.56644 | -46.79295 | 2025-10-01 12:00:00 | TERRA_M-T | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 42.7 |
| 70f7efe9-02c2-3495-bb4a-ce881e7cf065 | -8.88438 | -46.60857 | 2025-10-01 12:00:00 | TERRA_M-T | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 33.0 |
| 74c9e439-fb31-3435-90f1-f4a2b49f5e2b | -11.84321 | -44.96478 | 2025-10-01 12:00:00 | TERRA_M-T | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 26.0 |
| 0ab815fb-5484-39c6-9f92-15eafed39afa | -13.33456 | -48.15222 | 2025-10-01 12:00:00 | TERRA_M-T | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 11.1 |
| 4633bb53-542d-31c7-ac0f-b908e796f44c | -10.54265 | -47.87917 | 2025-10-01 12:00:00 | TERRA_M-T | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 46.0 |
| 4203c5da-b32a-3b21-9c2e-91575b0f2aba | -14.21038 | -46.10006 | 2025-10-01 12:00:00 | TERRA_M-T | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 7.7 |
| f0dfc86a-78c5-306e-ac8e-ef0cc6f94988 | -9.79711 | -45.92911 | 2025-10-01 12:00:00 | TERRA_M-T | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 11.6 |
| 9cc0dedb-dacc-3370-968d-1254c2b67dda | -11.45716 | -44.96524 | 2025-10-01 12:00:00 | TERRA_M-T | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 11.0 |
| 63bbf474-a125-3d7e-bb6a-e34bdda94943 | -14.31628 | -45.21581 | 2025-10-01 12:00:00 | TERRA_M-T | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 6.1 |
| d773fe65-2e9d-361e-b14e-6085a58cbac8 | -13.13041 | -47.42576 | 2025-10-01 12:00:00 | TERRA_M-T | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 17.9 |
| 0b009e4d-9929-3a5d-8ccd-a055a1501c66 | -10.82457 | -46.65145 | 2025-10-01 12:00:00 | TERRA_M-T | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 19.1 |
| aa959d69-7c91-34fb-ba8d-d60fada5fece | -12.42595 | -44.09336 | 2025-10-01 12:00:00 | TERRA_M-T | TABOCAS DO BREJO VELHO | BAHIA | Brasil | 2930907 | 29 | 33 | nan | nan | nan | Cerrado | 8.5 |
| bf7fedb6-e226-3f96-91f8-51cd86811897 | -11.45441 | -45.03135 | 2025-10-01 12:00:00 | TERRA_M-T | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 32.8 |
| 92bafe45-5b74-3248-846c-fa56f083e8b0 | -9.821 | -47.85658 | 2025-10-01 12:00:00 | TERRA_M-T | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 27.0 |
| 8e29b782-535c-3ea6-8a82-cfaf00b9bc96 | -14.35327 | -43.83673 | 2025-10-01 12:00:00 | TERRA_M-T | JUVENÍLIA | MINAS GERAIS | Brasil | 3136959 | 31 | 33 | nan | nan | nan | Cerrado | 7.8 |
| 8556f4c7-4125-3cc8-b104-cb3cf56136b5 | -13.30027 | -47.58509 | 2025-10-01 12:00:00 | TERRA_M-T | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 15.7 |
| 0c217219-51de-3ad2-b9f2-7e215fde0564 | -13.75505 | -40.22091 | 2025-10-01 12:00:00 | TERRA_M-T | JEQUIÉ | BAHIA | Brasil | 2918001 | 29 | 33 | nan | nan | nan | Caatinga | 9.0 |
| 5137dc48-d969-367b-b1d5-16d6d7c2ccbc | -12.24681 | -47.82125 | 2025-10-01 12:00:00 | TERRA_M-T | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 41.4 |
| e122e3d2-8a1b-32a1-92d5-952c5986b817 | -13.70717 | -48.62806 | 2025-10-01 12:00:00 | TERRA_M-T | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 21.2 |
| 7982d355-d47b-358e-ba51-396f3cc5ea0d | -13.82698 | -43.06784 | 2025-10-01 12:00:00 | TERRA_M-T | MATINA | BAHIA | Brasil | 2921054 | 29 | 33 | nan | nan | nan | Caatinga | 11.2 |
| 5e089ea0-a952-333c-bf47-6221d200110d | -9.80953 | -47.85474 | 2025-10-01 12:00:00 | TERRA_M-T | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 44.0 |
| 4cee4b84-b1f4-374d-bd2b-c2774f2278f8 | -8.65734 | -44.86088 | 2025-10-01 12:00:00 | TERRA_M-T | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 17.0 |
| 049fd5da-9913-32ae-b4d1-ba03de76c177 | -7.80515 | -46.74737 | 2025-10-01 12:00:00 | TERRA_M-T | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 167.4 |
| 5ac44edc-1883-3e49-a21d-062783e05526 | -11.35421 | -44.97336 | 2025-10-01 12:00:00 | TERRA_M-T | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 11.2 |
| f51a5cdd-3a2b-3ee5-989c-5299441e2eb8 | -10.98641 | -46.52632 | 2025-10-01 12:00:00 | TERRA_M-T | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 28.1 |
| d2221b8b-61a1-3671-bdaf-21e176fdd492 | -10.9781 | -46.5128 | 2025-10-01 12:00:00 | TERRA_M-T | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 158.5 |
| 320cefdc-4f9c-3c6e-a88f-064ce091676a | -14.35243 | -45.89599 | 2025-10-01 12:00:00 | TERRA_M-T | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 17.0 |
| c8e2c5b5-a146-350e-9436-05c42465b8ed | -11.9487 | -47.06725 | 2025-10-01 12:00:00 | TERRA_M-T | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 23.9 |
| aafca00c-8a6b-35e3-9c3c-a69ca500f9b3 | -14.28112 | -41.17862 | 2025-10-01 12:00:00 | TERRA_M-T | TANHAÇU | BAHIA | Brasil | 2931004 | 29 | 33 | nan | nan | nan | Caatinga | 21.2 |
| 53f977fc-f685-3651-b1c2-bad0ba0a87da | -8.55203 | -44.75489 | 2025-10-01 12:00:00 | TERRA_M-T | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 33.0 |
| 61818b15-5b61-3591-b2c8-3d0a8177c4e9 | -8.85669 | -46.57741 | 2025-10-01 12:00:00 | TERRA_M-T | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 13.8 |
| 0bf3bf03-e440-39d4-a216-5a06bb12b247 | -7.56859 | -46.77882 | 2025-10-01 12:00:00 | TERRA_M-T | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 51.9 |
| 59e1ae31-3b99-3158-ad43-36289c7ad00d | -8.93225 | -47.5729 | 2025-10-01 12:00:00 | TERRA_M-T | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 29.1 |
| ef3c04ab-b0e6-392f-9730-a4b3761d6caf | -10.64405 | -48.52666 | 2025-10-01 12:00:00 | TERRA_M-T | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 29.1 |
| f8efc1f4-a802-3b20-80cf-d007241113a6 | -12.80454 | -46.90282 | 2025-10-01 12:00:00 | TERRA_M-T | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 16.6 |
| 9ae182c3-3449-31fb-9a9e-874c2a27bfd7 | -14.02583 | -46.31581 | 2025-10-01 12:00:00 | TERRA_M-T | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 7.7 |
| 29df4284-3592-3d84-ba7e-8241b1ec5ffe | -8.52654 | -47.29152 | 2025-10-01 12:00:00 | TERRA_M-T | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 26.8 |
| 715f7562-8d0c-3d00-b183-a9412b487cf3 | -12.13272 | -42.66866 | 2025-10-01 12:00:00 | TERRA_M-T | OLIVEIRA DOS BREJINHOS | BAHIA | Brasil | 2923209 | 29 | 33 | nan | nan | nan | Caatinga | 14.8 |
| 0bb692d6-61a0-3f88-98f2-ae2736254ee8 | -9.79882 | -45.91791 | 2025-10-01 12:00:00 | TERRA_M-T | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 9.9 |
| 5e439006-c30a-3aee-86a3-09cfb7407f7d | -8.51758 | -47.27489 | 2025-10-01 12:00:00 | TERRA_M-T | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 21.0 |
| 3bae5636-2012-334f-920b-9a5835da78f3 | -7.55762 | -46.77711 | 2025-10-01 12:00:00 | TERRA_M-T | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 21.7 |
| 88345986-87f8-3c78-acb2-c371403f1814 | -15.01158 | -39.722 | 2025-10-01 12:00:00 | TERRA_M-T | ITAJU DO COLÔNIA | BAHIA | Brasil | 2915403 | 29 | 33 | nan | nan | nan | Mata Atlântica | 12.6 |
| b5a4bc3a-bcc7-3758-82ee-c9865edf9f3e | -12.75376 | -46.89514 | 2025-10-01 12:00:00 | TERRA_M-T | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 51.7 |
| 5642dd6f-33df-31a1-9f73-d39015ffc16e | -8.71344 | -44.84389 | 2025-10-01 12:00:00 | TERRA_M-T | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 10.5 |
| 0c858d70-4fef-38a4-8c3b-c88169f36881 | -10.83486 | -46.65303 | 2025-10-01 12:00:00 | TERRA_M-T | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 16.1 |
| 763d73c3-a4ba-39c4-835a-3f664b74d297 | -8.22995 | -45.78731 | 2025-10-01 12:00:00 | TERRA_M-T | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 11.5 |
| 285ed80c-0d8c-3e2a-8a6b-dc0c2f00dfcc | -7.81746 | -45.1219 | 2025-10-01 12:00:00 | TERRA_M-T | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 8.7 |
| f95346bd-d395-33eb-bfc6-5dfdd4275b01 | -11.91799 | -47.99702 | 2025-10-01 12:00:00 | TERRA_M-T | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 17.8 |
| d14934d4-29c4-3e5d-8560-2d24156e40c2 | -10.97887 | -46.57468 | 2025-10-01 12:00:00 | TERRA_M-T | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 106.1 |
| 9b017827-5cb3-3e78-a41f-4c42e5e46d85 | -12.62998 | -44.45651 | 2025-10-01 12:00:00 | TERRA_M-T | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 9.2 |
| 3889cae8-dd63-3ad7-bdfc-155443786dfb | -9.9439 | -43.59096 | 2025-10-01 12:00:00 | TERRA_M-T | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 35.4 |


[Clique aqui para ver as próximas entradas](README144.md)
