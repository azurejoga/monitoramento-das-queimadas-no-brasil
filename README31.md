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

## Dados Diários - Página 31

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 81195afc-ee7e-3201-8240-f7967cb6a651 | -6.3438 | -43.78923 | 2025-09-07 03:57:00 | NPP-375D | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 1d51e5d3-d2be-3ea2-bebe-d4fc9b26c67c | -10.78259 | -48.27462 | 2025-09-07 03:57:00 | NPP-375D | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| e52361f0-7f14-342e-a69e-d0a0b4818358 | -8.02128 | -45.44845 | 2025-09-07 03:57:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 39b0c757-8b30-38f9-8481-da81eccb4989 | -6.87923 | -45.54551 | 2025-09-07 03:57:00 | NPP-375D | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| b1a72330-c10c-3d43-99a5-dd1bd60e92d0 | -7.35284 | -43.95399 | 2025-09-07 03:57:00 | NPP-375D | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| f3696efd-7730-3fe2-9d2f-9eda6addafd0 | -11.4102 | -43.61373 | 2025-09-07 03:57:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 14623b50-dddd-3310-9f7c-c99ea88570cf | -13.79235 | -43.16562 | 2025-09-07 03:57:00 | NPP-375D | RIACHO DE SANTANA | BAHIA | Brasil | 2926400 | 29 | 33 | nan | nan | nan | Caatinga | 0.9 |
| bfea6729-b27a-3c47-ab50-772f0bd441af | -6.83569 | -46.39194 | 2025-09-07 03:57:00 | NPP-375D | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| eb810ef4-c2a8-35e1-be81-6928fa13140a | -5.97703 | -44.73675 | 2025-09-07 03:57:00 | NPP-375D | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| ea435b16-a9ff-3d1c-8b5a-ffd31308367a | -11.77497 | -47.55962 | 2025-09-07 03:57:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 2541a997-78f4-3ffa-9d3b-a01e97ba7312 | -6.20368 | -43.37595 | 2025-09-07 03:57:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| fecc945f-a898-3d27-ac92-14c100f5a34e | -13.02987 | -48.07794 | 2025-09-07 03:57:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 6ede4152-08ea-31cd-935f-328c7ede3fbd | -11.26201 | -46.44908 | 2025-09-07 03:57:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| ecee2813-573b-3f4b-8044-72536f2956f3 | -11.13942 | -48.38707 | 2025-09-07 03:57:00 | NPP-375D | IPUEIRAS | TOCANTINS | Brasil | 1709807 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 042adfb5-e25c-3b5f-bf1d-907487fd9fe0 | -6.24458 | -43.27659 | 2025-09-07 03:57:00 | NPP-375D | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| b0050f4c-c6f8-3ee6-93cb-f85800acac20 | -10.06176 | -48.06827 | 2025-09-07 03:57:00 | NPP-375D | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 1f2ac365-35e0-3b22-9132-d739df02c79c | -7.01763 | -44.95065 | 2025-09-07 03:57:00 | NPP-375D | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| d665abdd-591e-3bbe-bda8-2fbae7cfac77 | -13.05366 | -48.05893 | 2025-09-07 03:57:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 8f4d281a-52f0-3836-9f09-1f78f64fb08c | -13.33373 | -43.24953 | 2025-09-07 03:57:00 | NPP-375D | BOM JESUS DA LAPA | BAHIA | Brasil | 2903904 | 29 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 58df662c-5578-3304-8276-edbe2107be31 | -13.82426 | -43.86442 | 2025-09-07 03:57:00 | NPP-375D | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 7cc85f45-386c-308f-b8f0-3b9d6358674d | -11.90729 | -46.6422 | 2025-09-07 03:57:00 | NPP-375D | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| de5860a1-3b99-3597-abf9-8d1046fe879e | -11.81393 | -48.23628 | 2025-09-07 03:57:00 | NPP-375D | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| c6ab4196-a6e6-3ad9-8c14-00fba137ec21 | -11.26116 | -46.45383 | 2025-09-07 03:57:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| ce381eb5-e02e-35ec-85c6-2d19acd998ea | -11.57778 | -47.76117 | 2025-09-07 03:57:00 | NPP-375D | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| a7ad8816-b0a2-3217-b1e4-4124a095ac43 | -5.94249 | -46.16735 | 2025-09-07 03:57:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 4652ab4e-3571-3681-82c3-fc104e033b6b | -7.81904 | -45.12488 | 2025-09-07 03:57:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| de43138d-eae5-3d14-a0b8-293f0ab8cbd4 | -6.47184 | -43.97643 | 2025-09-07 03:57:00 | NPP-375D | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 28652f4f-2652-37f6-bb96-12b800f694f0 | -7.86046 | -47.86809 | 2025-09-07 03:57:00 | NPP-375D | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 2e674427-c51d-34a0-9cba-80cd566ae1ba | -11.5892 | -47.75648 | 2025-09-07 03:57:00 | NPP-375D | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 08a15bd6-3eb5-341f-8191-46cd2287a096 | -7.74642 | -44.00756 | 2025-09-07 03:57:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 10.0 |
| a6288c02-c89b-367b-a4f0-711dfcf0519c | -11.89903 | -46.64366 | 2025-09-07 03:57:00 | NPP-375D | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| b0e0dbc4-f642-337d-a073-b3e473d346df | -6.20426 | -43.37241 | 2025-09-07 03:57:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 14371c06-6e14-34f5-a535-d55a05c2365c | -10.61034 | -44.33669 | 2025-09-07 03:57:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 8.5 |
| 190b678b-5d4d-3eb2-8944-7f46063808f9 | -7.60606 | -44.6641 | 2025-09-07 03:57:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 39f66388-19df-3eab-a46d-01c2266dfee4 | -6.73394 | -50.45678 | 2025-09-07 03:57:00 | NPP-375D | ÁGUA AZUL DO NORTE | PARÁ | Brasil | 1500347 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 9c86cc93-dea5-333d-9db2-331d9518702e | -10.08875 | -48.09779 | 2025-09-07 03:57:00 | NPP-375D | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| c6b9ac13-e9e7-3640-b043-07a447fa02cd | -8.0221 | -45.44382 | 2025-09-07 03:57:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 6c4fe4b0-e005-349b-9705-afdb2bb103a4 | -13.18458 | -44.48418 | 2025-09-07 03:57:00 | NPP-375D | SANTA MARIA DA VITÓRIA | BAHIA | Brasil | 2928109 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| f6e4c5f0-b2af-3d48-8235-447b39ae81ac | -7.76389 | -50.76169 | 2025-09-07 03:57:00 | NPP-375D | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 462670c5-83ca-3417-83d0-c895a5bb2cd1 | -11.34761 | -43.50854 | 2025-09-07 03:57:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| bc9e2d92-cb3e-3e83-8f06-931b07fc77c0 | -10.34671 | -46.46651 | 2025-09-07 03:57:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 70.9 |
| 006b870f-1dbd-37dc-adb5-6203ed76a6ff | -6.2312 | -43.28196 | 2025-09-07 03:57:00 | NPP-375D | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 4d6a9621-797a-3c88-babe-750b4d4adbb9 | -8.49227 | -45.10783 | 2025-09-07 03:57:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 77fa6416-c505-3958-bd88-c95ed19f09bf | -11.58219 | -47.1761 | 2025-09-07 03:57:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 29c42ab7-1bce-3dd2-b493-c2ab37e8af8d | -9.83957 | -46.55404 | 2025-09-07 03:57:00 | NPP-375D | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 22747dbd-b7f7-3db6-94e1-49cfeb1cc05f | -10.34515 | -44.9087 | 2025-09-07 03:57:00 | NPP-375D | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 5251cb86-9aae-3928-a7a9-19ad78480589 | -5.86884 | -51.95989 | 2025-09-07 03:57:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 3c9a3bb8-5765-369d-892f-e5ca2afea2ec | -6.43644 | -43.62081 | 2025-09-07 03:57:00 | NPP-375D | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| e2db2149-0ac6-3223-8768-18beff4853dd | -12.0066 | -47.77959 | 2025-09-07 03:57:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 1760e4ad-9850-3f65-aba3-14659f05de62 | -6.21082 | -44.18953 | 2025-09-07 03:57:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 5bd9f2d7-92eb-35a8-9b02-8ae7981db8e8 | -8.44264 | -45.02865 | 2025-09-07 03:57:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 3.1 |
| e6dd0692-0e85-35ef-a759-75aa4a35d284 | -6.59958 | -43.96082 | 2025-09-07 03:57:00 | NPP-375D | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| ce7c2ea6-3d30-3011-86c4-c9dc97db3bca | -12.0152 | -47.7859 | 2025-09-07 03:57:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 0512505a-7d77-3519-9403-4bb675d2625e | -11.58357 | -47.73094 | 2025-09-07 03:57:00 | NPP-375D | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 74e0d274-3600-399b-8d63-5c7202968be7 | -6.26676 | -43.49407 | 2025-09-07 03:57:00 | NPP-375D | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| b86770e4-1202-310d-af1c-d487bed45504 | -6.23181 | -43.27837 | 2025-09-07 03:57:00 | NPP-375D | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| a71efb07-0186-3141-9fdc-d789d4aa9404 | -10.74566 | -48.186 | 2025-09-07 03:57:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 250d6d6a-b30f-3eec-83ad-fa458165167d | -7.81437 | -45.42378 | 2025-09-07 03:57:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 4.2 |
| be3fcbfc-0144-3324-be4a-a54dc7726194 | -11.14462 | -48.38826 | 2025-09-07 03:57:00 | NPP-375D | IPUEIRAS | TOCANTINS | Brasil | 1709807 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 5197f6c6-06d3-3a46-aa2b-42841ae75fd8 | -7.33913 | -48.50782 | 2025-09-07 03:57:00 | NPP-375D | ARAGUAÍNA | TOCANTINS | Brasil | 1702109 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 59c605a1-cb98-3f86-ac2d-bd86e41e2f4b | -7.80978 | -45.42319 | 2025-09-07 03:57:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 537bd75d-7bc4-3f32-a5a9-c89844a76ca2 | -13.05767 | -48.06716 | 2025-09-07 03:57:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 7.2 |
| d47a4634-3f2b-38a3-b212-fd978fc42613 | -7.75499 | -48.81737 | 2025-09-07 03:57:00 | NPP-375D | ARAPOEMA | TOCANTINS | Brasil | 1702307 | 17 | 33 | nan | nan | nan | Amazônia | 3.7 |
| c55a9a30-e1da-338d-ab8e-e9b024c6a238 | -7.71321 | -44.71955 | 2025-09-07 03:57:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| f779872f-b58a-3e91-81da-10152056d95b | -6.30153 | -51.41201 | 2025-09-07 03:57:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 10.0 |
| d44e2d99-3017-334f-8715-cb752b35a072 | -8.45585 | -45.03054 | 2025-09-07 03:57:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 13.7 |
| 2880a3b3-15f9-3a48-aed9-a5aedc2c230c | -10.60907 | -44.34391 | 2025-09-07 03:57:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| e66207a5-1a91-3c74-98e6-74c1d3be48ee | -8.14766 | -44.86005 | 2025-09-07 03:57:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 381d4498-b295-340b-a7ff-f2035fed5e6b | -8.70845 | -47.87397 | 2025-09-07 03:57:00 | NPP-375D | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 88c8faa6-a6bb-3ac5-8dfd-5db4e1fa4157 | -8.47984 | -45.18057 | 2025-09-07 03:57:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 4b231aab-a622-37f1-9ff1-2587bdd177d7 | -10.80455 | -47.72195 | 2025-09-07 03:57:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 821554f9-dc5b-3a3c-b3d6-c21daf83adef | -9.17753 | -45.59501 | 2025-09-07 03:57:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 47bd7134-dee3-3229-9ee8-2f2f546a10c3 | -6.59208 | -43.97967 | 2025-09-07 03:57:00 | NPP-375D | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 10b26525-51d5-368f-9c0c-049aaf010ca7 | -8.15637 | -44.86156 | 2025-09-07 03:57:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.7 |
| c0c3a21e-01cf-3bcd-81bb-d18b798255f9 | -6.79554 | -50.84775 | 2025-09-07 03:57:00 | NPP-375D | OURILÂNDIA DO NORTE | PARÁ | Brasil | 1505437 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a2f1086e-cbd6-36a6-b7fc-0066d29c6277 | -11.57645 | -47.74163 | 2025-09-07 03:57:00 | NPP-375D | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| b6e8f08f-a64d-322c-b04c-eeb6d23fd8a1 | -6.59625 | -43.98064 | 2025-09-07 03:57:00 | NPP-375D | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| fd6c687f-a188-3d3b-b680-2f1ee1d08edf | -10.74026 | -44.35715 | 2025-09-07 03:57:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| cc50e20b-3dc6-301f-8a0a-543559540963 | -5.94914 | -46.1843 | 2025-09-07 03:57:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| e86a502b-b7d8-305d-9f4a-a3121e227e46 | -12.84566 | -47.99187 | 2025-09-07 03:57:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| d255441b-f3f5-3c3f-8230-b787c4d0f9cd | -10.05771 | -48.06096 | 2025-09-07 03:57:00 | NPP-375D | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 5bce1ae9-74ca-332f-ae28-2e662e9fea49 | -8.18899 | -50.13496 | 2025-09-07 03:57:00 | NPP-375D | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 287cb9da-d718-38ce-94fe-6ec2c782636d | -12.84026 | -48.01985 | 2025-09-07 03:57:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| d22f214a-f14c-3966-a450-5364247ac62f | -9.98105 | -51.66079 | 2025-09-07 03:57:00 | NPP-375D | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| e21e8be8-dcb1-33e6-9787-baae0191ed96 | -6.13166 | -44.25381 | 2025-09-07 03:57:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 4.0 |
| ca175624-3bb2-3425-8f59-8a14e36b0ca8 | -10.7386 | -48.59589 | 2025-09-07 03:57:00 | NPP-375D | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 25bc644a-347b-303c-802f-c2914524f3d8 | -9.97915 | -51.6619 | 2025-09-07 03:57:00 | NPP-375D | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 0186cf7e-5112-3571-a707-23bb9dab4e24 | -9.97247 | -51.66129 | 2025-09-07 03:57:00 | NPP-375D | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| c9a79bb8-a88f-3d06-9bad-e10feaeed33f | -7.34714 | -44.31327 | 2025-09-07 03:57:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| d11f27f9-72aa-3a64-8bc3-4a1e92ad1668 | -8.30839 | -44.97271 | 2025-09-07 03:57:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| fd2c7672-32b1-330a-8997-7443ae1adb79 | -6.2282 | -43.2996 | 2025-09-07 03:57:00 | NPP-375D | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 4c9ed067-e582-370d-adf7-ca5c3f406c10 | -6.3777 | -42.98551 | 2025-09-07 03:57:00 | NPP-375D | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| ce979dce-b6c6-302b-b823-66fd367d5a2c | -12.85042 | -47.99241 | 2025-09-07 03:57:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 3f88d940-d28a-3a7f-9f25-3bb2be8a38cc | -6.92482 | -44.3317 | 2025-09-07 03:57:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 1a484f02-8eee-3f29-a391-44a75eb8ddb5 | -7.76485 | -50.75657 | 2025-09-07 03:57:00 | NPP-375D | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 87a3f371-2ed6-3c01-8022-b1d7cf0748da | -7.60424 | -44.6682 | 2025-09-07 03:57:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 05d34b48-5387-3c1b-aa24-25e551e451f3 | -11.62317 | -47.16206 | 2025-09-07 03:57:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 056c85c6-63f1-3433-949e-46bab418f839 | -12.01645 | -47.78171 | 2025-09-07 03:57:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| eb343fd0-9c1f-3873-ad00-b19061b31d30 | -6.93882 | -43.22735 | 2025-09-07 03:57:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 4.0 |
| b37d7704-e6d4-3462-8358-cd5cf465be37 | -13.01924 | -48.05083 | 2025-09-07 03:57:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |


[Clique aqui para ver as próximas entradas](README32.md)
