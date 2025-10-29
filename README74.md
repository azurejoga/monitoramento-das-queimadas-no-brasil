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

## Dados Diários - Página 74

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 29dd8988-980f-35b2-ac0b-164f3b61ee3d | -11.33543 | -46.07064 | 2025-10-29 04:46:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 095f2f65-535a-38e4-a4df-e663058c6719 | -13.64322 | -46.50324 | 2025-10-29 04:46:00 | NOAA-20 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| e72757ac-0576-3b96-8979-4c77a546bcef | -13.98955 | -44.54537 | 2025-10-29 04:46:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| b76ce1e5-11eb-3db3-83a1-25648b4839fb | -14.32522 | -46.52221 | 2025-10-29 04:46:00 | NOAA-20 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| fdbdafbd-8061-32bd-82dc-3b39dd986809 | -10.65702 | -47.90712 | 2025-10-29 04:46:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 9d5b0c0c-8661-39db-a92d-fde6cb3b84ad | -10.98759 | -47.72541 | 2025-10-29 04:46:00 | NOAA-20 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 7d408965-217f-399c-ba9d-902bab15e1b6 | -13.56715 | -47.33477 | 2025-10-29 04:46:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 1cb84aab-515e-31be-8699-971f28b61ab8 | -13.34257 | -46.35341 | 2025-10-29 04:46:00 | NOAA-20 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 65f3e144-f1fa-33ad-aa0f-c0bdcdb2658c | -11.27931 | -45.50969 | 2025-10-29 04:46:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 5.3 |
| fec5e191-4e28-3d61-935b-1aa45067ca7d | -11.9343 | -51.33517 | 2025-10-29 04:46:00 | NOAA-20 | SERRA NOVA DOURADA | MATO GROSSO | Brasil | 5107883 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 6e6fd7bc-b0c6-3063-9c5c-ddfac3325966 | -13.21131 | -47.0581 | 2025-10-29 04:46:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 352e477c-1017-31ec-a572-6dc85583cab8 | -9.49801 | -46.93764 | 2025-10-29 04:46:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| f3c158b6-79c8-304f-a5fc-8f67b6e65f78 | -10.98397 | -44.68558 | 2025-10-29 04:46:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 40c2cf37-a24c-3508-83d5-615e8d1de0da | -11.14694 | -47.77606 | 2025-10-29 04:46:00 | NOAA-20 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 0fa01ad7-3f28-33a5-910d-478a95a67b9b | -12.69845 | -46.30718 | 2025-10-29 04:46:00 | NOAA-20 | AURORA DO TOCANTINS | TOCANTINS | Brasil | 1702703 | 17 | 33 | nan | nan | nan | Cerrado | 10.6 |
| 504e9c60-fda8-3653-9389-9949d34dc9f6 | -12.15182 | -47.68869 | 2025-10-29 04:46:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 4.5 |
| b853d9e8-f4fe-322c-ba6c-1771ff647066 | -13.42103 | -47.37517 | 2025-10-29 04:46:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 1ed90d2b-b489-38f7-9dc1-384b318790a6 | -10.84352 | -47.73984 | 2025-10-29 04:46:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 022396c8-c561-3363-9817-32e9e556e829 | -11.02522 | -47.84458 | 2025-10-29 04:46:00 | NOAA-20 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| d75f1011-f56c-3001-9748-21c77fa367d8 | -14.27896 | -47.31507 | 2025-10-29 04:46:00 | NOAA-20 | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 589c519e-660e-3dcf-a7d5-a465116eaef8 | -10.52687 | -47.73878 | 2025-10-29 04:46:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| aa639eb8-6255-3309-9a3a-155fbe28ee82 | -14.48487 | -43.94727 | 2025-10-29 04:46:00 | NOAA-20 | JUVENÍLIA | MINAS GERAIS | Brasil | 3136959 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 8ae14b3b-49f5-36b9-9d56-d7001f1fd835 | -15.09486 | -43.84444 | 2025-10-29 04:46:00 | NOAA-20 | MATIAS CARDOSO | MINAS GERAIS | Brasil | 3140852 | 31 | 33 | nan | nan | nan | Cerrado | 2.9 |
| f6c4404c-c785-35d2-883e-8ae03a596912 | -13.79794 | -52.79319 | 2025-10-29 04:46:00 | NOAA-20 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 44e277b5-22a0-3047-8b2a-7371d1146731 | -12.72512 | -46.70714 | 2025-10-29 04:46:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 5265c0a5-23d0-3490-8e62-e2a707805ab1 | -13.33558 | -47.48223 | 2025-10-29 04:46:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 4ddd1d22-75f6-332e-8d65-ba1f61f3818c | -10.84491 | -47.88988 | 2025-10-29 04:46:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 79cac6cc-4b4e-37dd-b6a6-3ae1475e876d | -13.55295 | -47.13939 | 2025-10-29 04:46:00 | NOAA-20 | TERESINA DE GOIÁS | GOIÁS | Brasil | 5221080 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| c3f98798-6215-3b9e-99b4-1bcfcead5597 | -10.85988 | -50.14689 | 2025-10-29 04:46:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| b735a483-de5e-3556-aab1-3a5008eb3df3 | -10.65002 | -48.00975 | 2025-10-29 04:46:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 7.8 |
| a0c71e55-c376-319d-940d-4ecb92247205 | -14.48161 | -49.33216 | 2025-10-29 04:46:00 | NOAA-20 | URUAÇU | GOIÁS | Brasil | 5221601 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 958ee8aa-cd13-3a9b-80be-632f92c69b3c | -12.01132 | -49.83889 | 2025-10-29 04:46:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| b83cb7ae-5606-3907-a570-b192296a6beb | -12.01003 | -46.77525 | 2025-10-29 04:46:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 8.9 |
| 99510782-e929-3813-b7cf-1ad4ea4fad14 | -13.91966 | -48.44716 | 2025-10-29 04:46:00 | NOAA-20 | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 27d82b6b-9f3c-3d44-b7b1-231e812c7d9d | -13.58056 | -49.60354 | 2025-10-29 04:46:00 | NOAA-20 | BONÓPOLIS | GOIÁS | Brasil | 5203575 | 52 | 33 | nan | nan | nan | Cerrado | 13.7 |
| b298e7c0-52da-3ea0-b34a-ac86e50298cd | -9.87825 | -44.88502 | 2025-10-29 04:46:00 | NOAA-20 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 93804cee-497f-3a00-8473-b2aee64ef13a | -15.16689 | -47.22792 | 2025-10-29 04:46:00 | NOAA-20 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 1848a47c-982e-315b-9539-0ed06d7c559d | -13.34529 | -46.34867 | 2025-10-29 04:46:00 | NOAA-20 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 3a560e94-31ff-3e80-8726-61e9c289cbef | -10.76289 | -47.89645 | 2025-10-29 04:46:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| d85f1db3-5991-354c-a351-8164a0adfb2d | -10.43025 | -44.99025 | 2025-10-29 04:46:00 | NOAA-20 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 1eccd300-385e-3d2a-af43-fb63795f6815 | -13.04371 | -47.57642 | 2025-10-29 04:46:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 397fbaf7-2c59-3365-87d1-f7a45b27a771 | -9.50701 | -46.51863 | 2025-10-29 04:46:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 2836e8b9-3b49-3693-8624-36114921b19f | -9.88421 | -44.88399 | 2025-10-29 04:46:00 | NOAA-20 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 8e7c1d62-bcb5-305a-b794-72f12e1f7dc3 | -11.17917 | -45.22218 | 2025-10-29 04:46:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 205db4a7-2ee5-325a-8f90-4de704d376b6 | -12.18887 | -46.71762 | 2025-10-29 04:46:00 | NOAA-20 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 9.1 |
| 6ceb2d4d-aa62-3c22-b8a7-95b3f6caa5fc | -10.85586 | -50.1272 | 2025-10-29 04:46:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 86a121c0-ab7f-3faf-8b7d-04e58a620a4c | -13.68177 | -47.19171 | 2025-10-29 04:46:00 | NOAA-20 | TERESINA DE GOIÁS | GOIÁS | Brasil | 5221080 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 20285a92-3b82-3452-a650-2b753b5640e0 | -10.54414 | -45.04661 | 2025-10-29 04:46:00 | NOAA-20 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| b1452389-8789-3096-8d02-07a82ebb2027 | -14.55162 | -49.26122 | 2025-10-29 04:46:00 | NOAA-20 | URUAÇU | GOIÁS | Brasil | 5221601 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 5c899a42-7ac7-383f-b065-d14fa0d6aee5 | -9.22394 | -46.34946 | 2025-10-29 04:46:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| a092c8a4-3bf1-38e1-9bf5-6bc3c9335f50 | -10.6428 | -45.24588 | 2025-10-29 04:46:00 | NOAA-20 | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 2a0b46c8-db5a-3789-9894-970662a268bf | -13.3287 | -43.1889 | 2025-10-29 04:46:00 | NOAA-20 | BOM JESUS DA LAPA | BAHIA | Brasil | 2903904 | 29 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 60b1103b-1580-31fc-b98c-6950ee7969c5 | -10.50855 | -47.73126 | 2025-10-29 04:46:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 4.5 |
| b6b9259f-d363-37e9-9b83-909932f2bfe8 | -10.86924 | -46.04175 | 2025-10-29 04:46:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 9b7e1079-d3b5-3943-be04-95cc09dce67a | -15.63531 | -42.99004 | 2025-10-29 04:46:00 | NOAA-20 | PORTEIRINHA | MINAS GERAIS | Brasil | 3152204 | 31 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 609a9096-eb71-3c35-8812-b4e56bce93ce | -10.61609 | -47.86931 | 2025-10-29 04:46:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 77c5baf8-9988-399a-b99d-8c3ee82b8d3e | -13.54756 | -47.32647 | 2025-10-29 04:46:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| e12c3dc5-ccb0-3d67-b381-84f39910d233 | -13.41195 | -47.38154 | 2025-10-29 04:46:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 7a9d19e4-494a-37a1-b748-1366da46a256 | -13.37349 | -47.41525 | 2025-10-29 04:46:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 60a586af-9534-3ed7-9d89-7614f8a01e68 | -9.30833 | -47.06029 | 2025-10-29 04:46:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 2d146735-f720-3fa9-8652-bdbc35e7afa5 | -12.35939 | -50.15881 | 2025-10-29 04:46:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 3f2412e1-9595-361b-9d86-545996941e32 | -10.92301 | -47.61081 | 2025-10-29 04:46:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 75b42736-db70-39ea-8542-8d6fb8819712 | -13.70128 | -47.67889 | 2025-10-29 04:46:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| a51cccd1-a0a7-361c-97a4-124011e956f3 | -10.76468 | -47.8292 | 2025-10-29 04:46:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| d93ffc72-4917-3dda-aee0-151aa47364fe | -9.94404 | -47.09327 | 2025-10-29 04:46:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 13.9 |
| e61ee514-0e5e-3206-9c95-08fad8fe5aaa | -12.70523 | -46.3098 | 2025-10-29 04:46:00 | NOAA-20 | AURORA DO TOCANTINS | TOCANTINS | Brasil | 1702703 | 17 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 251155f1-33e8-3ef4-b55d-8be967b7d5e2 | -13.63338 | -46.52525 | 2025-10-29 04:46:00 | NOAA-20 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 9c10b822-0d31-3a02-9927-49cdf36fe4c0 | -10.52618 | -47.7435 | 2025-10-29 04:46:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| cc1e32a8-ad92-38fe-a67e-b24e69f62430 | -13.22987 | -47.73043 | 2025-10-29 04:46:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 1a11da0e-25d1-3b8b-b163-6c7c6295eec0 | -14.68055 | -46.33773 | 2025-10-29 04:46:00 | NOAA-20 | SÍTIO D'ABADIA | GOIÁS | Brasil | 5220702 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 66b1f70c-d78a-3470-8c50-7ee208d26b17 | -12.32189 | -46.91996 | 2025-10-29 04:46:00 | NOAA-20 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 0.3 |
| 0a69cfe4-d247-3b15-bc2c-e3b2dc72fa70 | -12.24877 | -47.93058 | 2025-10-29 04:46:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| d6010035-1eee-30ce-b268-b4db27211247 | -14.88848 | -46.76181 | 2025-10-29 04:46:00 | NOAA-20 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| ddd514e9-0444-36c8-9b5e-cae5a54d8d6a | -10.56364 | -49.83834 | 2025-10-29 04:46:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 08deda53-0124-3f98-bd7b-ead38f1a9319 | -11.93375 | -51.33873 | 2025-10-29 04:46:00 | NOAA-20 | SERRA NOVA DOURADA | MATO GROSSO | Brasil | 5107883 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 76d6ac11-24a8-3bd0-89f4-250ee118437e | -13.91804 | -48.45367 | 2025-10-29 04:46:00 | NOAA-20 | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| f6a0837f-1dbe-349f-a26a-dfc72e21ef45 | -12.43744 | -43.75682 | 2025-10-29 04:46:00 | NOAA-20 | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 4.6 |
| f425ad6a-1535-33f6-8e32-ddb445e7d849 | -10.76848 | -47.82975 | 2025-10-29 04:46:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 43e8a04e-f1d8-30ea-a4b8-210c7e40c8a2 | -12.00951 | -46.77904 | 2025-10-29 04:46:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 8.9 |
| 4cb01e6d-493d-3656-b74f-7ea53145a329 | -13.20775 | -47.05349 | 2025-10-29 04:46:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| c60e9f1c-db2a-3617-aa98-586d928ff631 | -12.16162 | -47.90873 | 2025-10-29 04:46:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 1d517c5a-a0c0-3d54-baf2-15ff81b4014b | -9.80205 | -47.75308 | 2025-10-29 04:46:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 4bc6fc68-d4f0-30d2-962a-95df283d85b6 | -10.86375 | -50.09787 | 2025-10-29 04:46:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 14.8 |
| 64ea6660-b6f9-3439-bc3c-2c5074808be9 | -9.80136 | -47.75768 | 2025-10-29 04:46:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 22da582b-5de6-33e5-b384-6124051f2fd4 | -13.63467 | -46.4837 | 2025-10-29 04:46:00 | NOAA-20 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 1510fb42-ce6c-3894-bb12-9ee1bbdbb332 | -13.63305 | -46.51431 | 2025-10-29 04:46:00 | NOAA-20 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 6991e1e8-779e-3635-9c1c-b4e9c177da20 | -11.97844 | -49.94115 | 2025-10-29 04:46:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 89a4846a-5922-3370-b147-0c947e708a24 | -12.00332 | -46.76273 | 2025-10-29 04:46:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| c26db692-2e28-32f6-ac81-78c80e051b8e | -13.63569 | -46.49384 | 2025-10-29 04:46:00 | NOAA-20 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 7875a8f1-61f8-3517-8152-5b3ca0629b3f | -13.31776 | -42.42119 | 2025-10-29 04:46:00 | NOAA-20 | CATURAMA | BAHIA | Brasil | 2907558 | 29 | 33 | nan | nan | nan | Caatinga | 5.8 |
| 341ed4d8-ad0f-302e-9970-24144bda47df | -13.63984 | -47.04603 | 2025-10-29 04:46:00 | NOAA-20 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 72ef8138-3930-31e4-9d7c-7bd9252a681b | -10.76976 | -44.62675 | 2025-10-29 04:46:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 20e0e2aa-2336-3119-a1ab-d3e97500c925 | -13.93532 | -48.4411 | 2025-10-29 04:46:00 | NOAA-20 | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 5d6dbfea-a44b-3e9e-9016-605bac175391 | -12.83049 | -47.26438 | 2025-10-29 04:46:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 66997196-e2c2-36bc-b073-a4d4e6eb7e1c | -13.66683 | -47.17821 | 2025-10-29 04:46:00 | NOAA-20 | TERESINA DE GOIÁS | GOIÁS | Brasil | 5221080 | 52 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 14d909d9-dc63-3d9b-84b7-dc77bdf6aac6 | -12.91139 | -45.04045 | 2025-10-29 04:46:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| b18cd234-3444-388c-b344-755d6debc179 | -15.1005 | -43.8418 | 2025-10-29 04:46:00 | NOAA-20 | MATIAS CARDOSO | MINAS GERAIS | Brasil | 3140852 | 31 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 39e54a39-f94a-3d7a-952e-20264ce59b7e | -13.24322 | -44.11012 | 2025-10-29 04:46:00 | NOAA-20 | SANTA MARIA DA VITÓRIA | BAHIA | Brasil | 2928109 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 946cf1a4-cf3f-3f59-80c6-ae9856aff962 | -10.56993 | -49.84318 | 2025-10-29 04:46:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 7.0 |
| 97b2a855-7489-3d81-9244-002e3ab21061 | -12.07983 | -48.00122 | 2025-10-29 04:46:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |


[Clique aqui para ver as próximas entradas](README75.md)
