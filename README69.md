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

## Dados Diários - Página 69

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 97cd14a4-fd02-33e0-95af-3ebe43d9566d | -9.355 | -45.9284 | 2025-10-09 14:00:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 123.0 |
| 26a7cf21-07e4-349d-a8f5-7484bf71ddfc | -15.8288 | -43.7555 | 2025-10-09 14:00:00 | GOES-19 | SÃO JOÃO DA PONTE | MINAS GERAIS | Brasil | 3162401 | 31 | 33 | nan | nan | nan | Cerrado | 256.9 |
| 2ab3d918-c965-3c34-9d1d-3fa258b40919 | -13.2971 | -48.4579 | 2025-10-09 14:00:00 | GOES-19 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 175.7 |
| 1bfd86b0-11ca-3da9-832c-acf1db618a64 | -8.8335 | -45.3741 | 2025-10-09 14:00:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 127.6 |
| 572dd2c4-c2be-38ab-b37f-637016d2580d | -15.4772 | -47.9578 | 2025-10-09 14:00:00 | GOES-19 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 97.7 |
| d18c983d-811f-3d3a-916d-f475496d5f62 | -8.1049 | -44.8349 | 2025-10-09 14:00:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 81.1 |
| f1177469-e78b-37fa-acc5-6c7b673a04b1 | -14.2754 | -45.8647 | 2025-10-09 14:00:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 150.6 |
| 6ad9bfd3-8b85-3932-9e1b-ebf26e467a9a | -9.3922 | -45.9694 | 2025-10-09 14:00:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 127.0 |
| 744ae784-e22e-31d9-b7a3-9f4e9862b9d3 | -7.7924 | -44.1998 | 2025-10-09 14:00:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 127.1 |
| 5d7143f8-d8d4-3479-b4ae-0e949e0bfcb2 | -10.2095 | -44.5446 | 2025-10-09 14:00:00 | GOES-19 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 130.0 |
| 55f7937e-c610-3464-ace7-6d3ac264b1bf | -17.6538 | -44.4339 | 2025-10-09 14:00:00 | GOES-19 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 110.2 |
| aba08014-29f7-3d1f-994f-982825116d56 | -12.425 | -45.7056 | 2025-10-09 14:00:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 267.4 |
| 98e9afb6-7073-39d3-b674-8f4ace3c7e25 | -7.7746 | -42.5865 | 2025-10-09 14:00:00 | GOES-19 | SOCORRO DO PIAUÍ | PIAUÍ | Brasil | 2210904 | 22 | 33 | nan | nan | nan | Caatinga | 87.6 |
| 06dcab46-bd45-3061-be75-3ff1161f9ef5 | -16.2788 | -47.1556 | 2025-10-09 14:00:00 | GOES-19 | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 111.3 |
| 68d3e7bd-9874-324f-8b0d-232d9605ce6c | -15.8091 | -43.7597 | 2025-10-09 14:00:00 | GOES-19 | SÃO JOÃO DA PONTE | MINAS GERAIS | Brasil | 3162401 | 31 | 33 | nan | nan | nan | Cerrado | 187.0 |
| 9bcdbfcd-5227-3c4c-a883-a899d4e8867a | -13.0976 | -47.7982 | 2025-10-09 14:00:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 121.8 |
| 45973e2b-71f1-305e-9653-43cd65cb4cf6 | -13.7548 | -45.723 | 2025-10-09 14:00:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 154.5 |
| 5d9e9d14-d6a8-333a-b407-8dec07315e48 | -13.2967 | -48.4801 | 2025-10-09 14:00:00 | GOES-19 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 155.0 |
| 4af00f61-b489-3152-8fc8-e8e77afaac5a | -10.1199 | -45.4292 | 2025-10-09 14:00:00 | GOES-19 | SÃO GONÇALO DO GURGUÉIA | PIAUÍ | Brasil | 2209757 | 22 | 33 | nan | nan | nan | Cerrado | 124.3 |
| abe3a18e-61e7-3c45-8599-eb45371209b3 | -7.6296 | -45.2464 | 2025-10-09 14:00:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 89.2 |
| 434a0198-d096-3db5-82c6-88a2cf63ab66 | -7.5466 | -44.2933 | 2025-10-09 14:00:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 100.7 |
| b994ca01-315f-3e19-8c97-e6cd4f79c035 | -13.8311 | -45.7793 | 2025-10-09 14:00:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 147.8 |
| 810da61d-57e2-32b2-8552-85a9cf2b0c48 | -10.1905 | -44.5471 | 2025-10-09 14:00:00 | GOES-19 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 180.6 |
| 0ce39962-c8fb-39b8-b10d-f6345c3dd807 | -10.158 | -45.4244 | 2025-10-09 14:00:00 | GOES-19 | SÃO GONÇALO DO GURGUÉIA | PIAUÍ | Brasil | 2209757 | 22 | 33 | nan | nan | nan | Cerrado | 124.7 |
| 72fd97f4-b985-3348-a1b4-592f54ff21c5 | -14.9699 | -49.9263 | 2025-10-09 14:00:00 | GOES-19 | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 106.3 |
| 6922bf5a-36ec-3953-aee9-d894f2afbd49 | -7.6635 | -43.9582 | 2025-10-09 14:00:00 | GOES-19 | BERTOLÍNIA | PIAUÍ | Brasil | 2201705 | 22 | 33 | nan | nan | nan | Cerrado | 80.2 |
| 6d2847d3-4906-3090-a7d8-9a4c4f057607 | -7.8121 | -44.1285 | 2025-10-09 14:00:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 87.4 |
| 6f677b0b-5494-3cee-afd2-15486c1c2053 | -11.4682 | -43.4774 | 2025-10-09 14:00:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 126.5 |
| 4484f78e-ceda-31b9-86d4-2f0112dda963 | -10.0798 | -45.5709 | 2025-10-09 14:00:00 | GOES-19 | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 128.6 |
| 87f963cc-e6ae-34d9-8c71-442e91db4924 | -14.2559 | -45.8681 | 2025-10-09 14:00:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 144.0 |
| 3f5b75b3-1a53-3cad-87d5-9e9f2bbe42f9 | -10.1393 | -45.4039 | 2025-10-09 14:00:00 | GOES-19 | SÃO GONÇALO DO GURGUÉIA | PIAUÍ | Brasil | 2209757 | 22 | 33 | nan | nan | nan | Cerrado | 110.5 |
| f9e03d8c-e413-3853-8e74-b1a204c57427 | -12.2754 | -47.6473 | 2025-10-09 14:00:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 141.7 |
| 18584a59-1e1b-3b13-8bd3-5d5f3fe93c0c | -8.1891 | -44.1357 | 2025-10-09 14:10:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 83.0 |
| a4a4fea3-9242-30bd-850f-f14e6828f061 | -7.5466 | -44.2933 | 2025-10-09 14:10:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 113.3 |
| b0db7e91-871c-3233-8b70-fa171dd7f29f | -17.9002 | -57.6594 | 2025-10-09 14:10:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 71.9 |
| 4d1e6f49-da1b-3d36-8500-bed655766099 | -8.0861 | -44.8368 | 2025-10-09 14:10:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 85.0 |
| 559c0a1c-4020-33a5-940d-bd8b5685c3ed | -8.8335 | -45.3741 | 2025-10-09 14:10:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 111.1 |
| 81869740-e297-3be0-8578-bbfefaae5ea4 | -11.993 | -45.1958 | 2025-10-09 14:10:00 | GOES-19 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 191.8 |
| c61c9ba7-6bef-38ec-adc1-8cc8329db4be | -7.7932 | -42.6082 | 2025-10-09 14:10:00 | GOES-19 | RIBEIRA DO PIAUÍ | PIAUÍ | Brasil | 2208874 | 22 | 33 | nan | nan | nan | Caatinga | 72.7 |
| 5cfe65ec-2424-3993-9888-ac229823ee32 | -3.8948 | -41.5458 | 2025-10-09 14:10:00 | GOES-19 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 93.6 |
| 07f7f9c4-1401-3c37-b823-b4da223a8371 | -15.8288 | -43.7555 | 2025-10-09 14:10:00 | GOES-19 | SÃO JOÃO DA PONTE | MINAS GERAIS | Brasil | 3162401 | 31 | 33 | nan | nan | nan | Cerrado | 181.1 |
| d5129b8e-b265-3798-9230-f7599b5812f5 | -7.7924 | -44.1998 | 2025-10-09 14:10:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 113.8 |
| d25782a9-d346-3276-9400-1007b36a172a | -13.1361 | -47.7926 | 2025-10-09 14:10:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 116.0 |
| b4b9df9f-4ebd-3b44-8aaa-66a594376898 | -10.2092 | -44.5678 | 2025-10-09 14:10:00 | GOES-19 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 471.7 |
| 462d0533-97f4-359c-ab6b-d4708c25e1a0 | -8.6292 | -45.1228 | 2025-10-09 14:10:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 168.2 |
| 86f2b952-f3a1-34dd-ba8f-d3663c31cb26 | -3.8946 | -41.5698 | 2025-10-09 14:10:00 | GOES-19 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 87.0 |
| cae244e1-1987-3c43-870e-d9326478eae7 | -13.0775 | -47.8457 | 2025-10-09 14:10:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 116.2 |
| de0552ad-6b02-3e19-b69b-e626e5123a01 | -7.5463 | -44.3164 | 2025-10-09 14:10:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 143.1 |
| e9bd699d-8fd6-300e-a913-81cd642bd89b | -14.8633 | -48.441 | 2025-10-09 14:10:00 | GOES-19 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 82.5 |
| 7cf21342-ff63-3b9f-b40d-3d0f6f4db366 | -15.8091 | -43.7597 | 2025-10-09 14:10:00 | GOES-19 | SÃO JOÃO DA PONTE | MINAS GERAIS | Brasil | 3162401 | 31 | 33 | nan | nan | nan | Cerrado | 138.1 |
| 78087b26-1ce7-3c07-a6eb-ff94cd262651 | -11.7219 | -44.285 | 2025-10-09 14:10:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 129.4 |
| 777a76f8-e48a-34eb-b4cf-09c0216dbbf8 | -14.4452 | -47.9943 | 2025-10-09 14:10:00 | GOES-19 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 103.5 |
| e72ca6b7-912b-30a2-b395-9e8b302ae01e | -8.1618 | -43.323 | 2025-10-09 14:10:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 153.0 |
| e39428bc-86a1-390c-a872-0458b6aac939 | -11.6742 | -47.0365 | 2025-10-09 14:10:00 | GOES-19 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 138.0 |
| aaff3f84-e7ac-3faa-887e-aa9edcb66756 | -15.1543 | -45.7533 | 2025-10-09 14:10:00 | GOES-19 | CHAPADA GAÚCHA | MINAS GERAIS | Brasil | 3116159 | 31 | 33 | nan | nan | nan | Cerrado | 99.4 |
| 99a4b587-968e-39b0-8477-b3e5d7956c90 | -10.1901 | -44.5703 | 2025-10-09 14:10:00 | GOES-19 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 490.5 |
| 379ed6aa-0f59-3b94-b4d8-0b997819737a | -13.8302 | -45.8255 | 2025-10-09 14:10:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 343.7 |
| 99bb31e5-99d2-3de8-b422-b2d6fb81aae8 | -13.0976 | -47.7982 | 2025-10-09 14:10:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 118.2 |
| 239b33ed-591b-31df-87e9-5d267d66cf30 | -7.7933 | -44.1304 | 2025-10-09 14:10:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 97.7 |
| a5d84a35-bce6-3ea7-a996-48f168b9fd41 | -12.2525 | -47.8728 | 2025-10-09 14:10:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 129.3 |
| 0dd734bf-17ee-3655-a351-bb44d8d74541 | -12.2688 | -49.1907 | 2025-10-09 14:10:00 | GOES-19 | ALVORADA | TOCANTINS | Brasil | 1700707 | 17 | 33 | nan | nan | nan | Cerrado | 117.6 |
| d6b51bde-2c64-35fd-bae6-f67f8db9564f | -8.1055 | -44.7891 | 2025-10-09 14:10:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 93.3 |
| 17589785-a7e5-3aea-b1bb-245f3df576f4 | -8.6295 | -45.1 | 2025-10-09 14:10:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 154.7 |
| 8260a38c-83b7-3376-ac81-aaac53eccee0 | -7.5654 | -44.2915 | 2025-10-09 14:10:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 83.1 |
| c57166ae-1d23-312f-a681-26d2593ec7ba | -13.8108 | -45.8288 | 2025-10-09 14:10:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 426.8 |
| f26328b6-4ee1-380f-8ded-309b02d18fa8 | -12.2754 | -47.6473 | 2025-10-09 14:10:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 149.1 |
| fb33831d-0d25-3d0f-b3ee-6966c9acd4d6 | -8.1049 | -44.8349 | 2025-10-09 14:10:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 89.1 |
| a437af84-ffef-3d20-ae04-51639e95995e | -12.5733 | -48.1393 | 2025-10-09 14:10:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 124.2 |
| dfc9a8c8-b8c5-3dd2-8feb-2d9cf5666892 | -8.1052 | -44.812 | 2025-10-09 14:10:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 81.6 |
| e984482b-30fd-3c4b-ae15-6f814cb3a224 | -14.8438 | -48.4442 | 2025-10-09 14:10:00 | GOES-19 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 80.1 |
| 555a8be8-b5b0-3f6b-a0a2-4cb59f1481cc | -8.6106 | -45.102 | 2025-10-09 14:10:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 164.5 |
| 3e9757df-921b-3102-884a-d6197ccac621 | -11.655 | -47.039 | 2025-10-09 14:10:00 | GOES-19 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 132.7 |
| 7742b7b1-60b2-3f70-95b4-6ba08938fe3e | -13.2971 | -48.4579 | 2025-10-09 14:10:00 | GOES-19 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 169.7 |
| 97de9d0a-f6d6-3929-a414-32aaf625cb39 | -14.2559 | -45.8681 | 2025-10-09 14:10:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 138.7 |
| a6aaaa6b-6e23-393e-9799-ee8e689070e0 | -14.2754 | -45.8647 | 2025-10-09 14:10:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 145.0 |
| 62fc5a19-e4d1-3ea2-80ce-1f5dcdfa0935 | -15.8085 | -43.7838 | 2025-10-09 14:10:00 | GOES-19 | SÃO JOÃO DA PONTE | MINAS GERAIS | Brasil | 3162401 | 31 | 33 | nan | nan | nan | Caatinga | 420.0 |
| f52ed698-9cd3-3f5f-b991-ed47bdfea0bb | -11.4682 | -43.4774 | 2025-10-09 14:10:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 134.0 |
| fb99bbb0-e3e3-353b-8405-cfdbd0f1c065 | -13.429 | -47.5701 | 2025-10-09 14:10:00 | GOES-19 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 173.8 |
| c70832ee-8541-3b98-ab4e-164d990be75d | -7.8372 | -45.181 | 2025-10-09 14:10:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 82.3 |
| 8ce2cda9-00b5-3fde-bad7-5ae987244dcf | -8.1894 | -44.1125 | 2025-10-09 14:10:00 | GOES-19 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 71.8 |
| d6d6320f-9e7c-3c51-bd1b-c2b8700f1a9d | -13.7553 | -45.6999 | 2025-10-09 14:10:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 158.1 |
| e985d23d-33fc-3637-9763-1909822ec9d5 | -7.6635 | -43.9582 | 2025-10-09 14:10:00 | GOES-19 | BERTOLÍNIA | PIAUÍ | Brasil | 2201705 | 22 | 33 | nan | nan | nan | Cerrado | 78.5 |
| 765aceaf-d79f-3728-a8ca-fbe88994859a | -8.0866 | -44.791 | 2025-10-09 14:10:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 85.2 |
| 1e5934d8-6231-3ee5-8cc8-cf64ba508493 | -3.8761 | -41.5468 | 2025-10-09 14:10:00 | GOES-19 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 84.5 |
| 2f40ccbe-a587-375a-8881-52eb14a6902a | -12.6496 | -45.0021 | 2025-10-09 14:10:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 138.0 |
| d9ecba0a-f720-33aa-8565-b8d84c0dc50f | -13.7913 | -45.8321 | 2025-10-09 14:10:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 326.9 |
| c5dbd6c1-fdf2-3b6a-af44-1a9d7b71fa41 | -13.4101 | -47.5506 | 2025-10-09 14:10:00 | GOES-19 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 122.5 |
| dda6591c-da71-3a03-b9ad-a1b8d1691ea9 | -8.1804 | -43.3445 | 2025-10-09 14:10:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 193.4 |
| cae41175-b03d-3692-acef-b07b8d9ed951 | -13.8307 | -45.8024 | 2025-10-09 14:10:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 161.1 |
| 9f0deb48-c459-3602-8e6c-fe71b47e168d | -15.556 | -45.3043 | 2025-10-09 14:10:00 | GOES-19 | CHAPADA GAÚCHA | MINAS GERAIS | Brasil | 3116159 | 31 | 33 | nan | nan | nan | Cerrado | 93.9 |
| efb4035f-bdbc-3bf0-83eb-18a34a0d3371 | -11.7833 | -45.1347 | 2025-10-09 14:10:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 146.4 |
| fb6e9a7b-c603-3f0b-b33b-15fe424940e9 | -13.7548 | -45.723 | 2025-10-09 14:10:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 165.5 |
| 185c3671-3f0a-3b83-bb4c-133fc33267df | -7.7746 | -42.5865 | 2025-10-09 14:10:00 | GOES-19 | SOCORRO DO PIAUÍ | PIAUÍ | Brasil | 2210904 | 22 | 33 | nan | nan | nan | Caatinga | 92.0 |
| 6477d949-e7b7-38b8-90f9-20db755d5e99 | -13.3677 | -47.7584 | 2025-10-09 14:10:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 108.5 |
| 360348b9-75b5-3133-a8c2-511575f44f1f | -13.0387 | -46.819 | 2025-10-09 14:10:00 | GOES-19 | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 133.5 |
| 2e5b3f52-88f1-3dc7-9f65-5034b849d2d1 | -12.5926 | -48.1366 | 2025-10-09 14:10:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 120.0 |
| 4a201385-556e-3967-a0ba-11a508f59573 | -12.425 | -45.7056 | 2025-10-09 14:10:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 262.0 |
| ee788647-0558-354b-8173-5b995add0aee | -14.3349 | -50.7578 | 2025-10-09 14:10:00 | GOES-19 | NOVA CRIXÁS | GOIÁS | Brasil | 5214838 | 52 | 33 | nan | nan | nan | Cerrado | 94.9 |
| 9a2e01ab-4e9d-3ad9-a375-f70f48977ae0 | -13.0783 | -47.801 | 2025-10-09 14:10:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 128.7 |
| 9e99177b-b1ea-3f44-9977-92a50162fa8a | -10.1711 | -44.5727 | 2025-10-09 14:10:00 | GOES-19 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 117.2 |


[Clique aqui para ver as próximas entradas](README70.md)
