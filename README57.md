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

## Dados Diários - Página 57

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| fcd9b721-f74d-38b6-bf32-6a3a91748b1a | -7.2853 | -43.68849 | 2025-09-01 04:32:00 | NOAA-20 | CANAVIEIRA | PIAUÍ | Brasil | 2202251 | 22 | 33 | nan | nan | nan | Cerrado | 2.8 |
| b6f51c2a-b814-3d72-a258-e4f7fb67a531 | -6.82709 | -52.80986 | 2025-09-01 04:32:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| d8e00b2d-10d5-3fb2-9ae7-c6cb70accc47 | -7.11305 | -44.76904 | 2025-09-01 04:32:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 19f30035-a563-3206-944c-96cb849dc28e | -6.52149 | -43.54708 | 2025-09-01 04:32:00 | NOAA-20 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 60f8fc29-ff80-35ba-b5b3-a87a06da0a1f | -6.30122 | -43.30099 | 2025-09-01 04:32:00 | NOAA-20 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| a80ae0aa-1664-3e64-9a99-62cc94c7a04f | -6.51233 | -43.55567 | 2025-09-01 04:32:00 | NOAA-20 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| c66a4df0-984c-3c07-912c-21853f5bfab1 | -7.89698 | -48.27601 | 2025-09-01 04:32:00 | NOAA-20 | PALMEIRANTE | TOCANTINS | Brasil | 1715705 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| aba97bfb-fa10-3abf-9936-5959fbc83560 | -7.5838 | -61.63238 | 2025-09-01 04:32:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 22261546-021b-3b0a-8ba5-3a13f06bd006 | -6.30028 | -43.55364 | 2025-09-01 04:32:00 | NOAA-20 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 4a73dd21-0b9f-3795-995d-488dd93e7c48 | -6.16162 | -43.32442 | 2025-09-01 04:32:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| a3c7b9f3-d0dc-3491-a6c3-11cbc44ada75 | -6.87014 | -44.32269 | 2025-09-01 04:32:00 | NOAA-20 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 9dc8def4-2fcd-3a47-bd39-1bf1b940ad61 | -6.31264 | -43.62952 | 2025-09-01 04:32:00 | NOAA-20 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| a959fa62-2a2d-3d01-98f2-b56752e40bdb | -9.63766 | -46.60561 | 2025-09-01 04:32:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| dd718f05-ecbf-30da-a273-cb5b1fa65a1e | -5.04698 | -50.79284 | 2025-09-01 04:32:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 047d6b3e-917a-3e93-b3ef-f0c3a6b2688e | -7.87864 | -46.98093 | 2025-09-01 04:32:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 9e9629cd-1fe3-3b45-8db7-a7a598afa372 | -7.71248 | -50.26553 | 2025-09-01 04:32:00 | NOAA-20 | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| b99073bc-fe01-32b8-a1ae-6977546f2772 | -6.82241 | -43.32628 | 2025-09-01 04:32:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 9.7 |
| ab483f6c-a658-317e-a532-eeb6eeb67995 | -7.45763 | -44.81306 | 2025-09-01 04:32:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 08eb03f7-b22f-3611-a14e-55b153c9093c | -8.87196 | -47.94956 | 2025-09-01 04:32:00 | NOAA-20 | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| fca61a8e-a2f1-3a7e-a5d7-fed300c00746 | -7.76905 | -50.32535 | 2025-09-01 04:32:00 | NOAA-20 | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 0.2 |
| 931034ad-2375-32ae-bd48-75b31abf59ed | -6.54589 | -43.51592 | 2025-09-01 04:32:00 | NOAA-20 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 9eb49e22-f07e-357c-a42c-c6de56f1b0c4 | -6.27676 | -43.52567 | 2025-09-01 04:32:00 | NOAA-20 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| f458440d-6bd1-32ae-a0e9-0021e265c842 | -6.33376 | -53.42848 | 2025-09-01 04:32:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 4aba3048-10b5-34c4-846c-6c700036d4af | -9.23984 | -47.06068 | 2025-09-01 04:32:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 71d3f1e9-1ed5-377e-b431-9712d09f441c | -10.04016 | -48.09834 | 2025-09-01 04:32:00 | NOAA-20 | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| dce79bd3-05af-31b9-963e-003feb4065d5 | -9.50501 | -48.84718 | 2025-09-01 04:32:00 | NOAA-20 | DOIS IRMÃOS DO TOCANTINS | TOCANTINS | Brasil | 1707207 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 231274fc-a25a-3c98-81f0-f0688a95b43a | -7.8792 | -46.97736 | 2025-09-01 04:32:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| ff111e6b-9c13-3c30-b836-c1fd48fcbae1 | -7.24938 | -44.24026 | 2025-09-01 04:32:00 | NOAA-20 | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| ed06a044-a7a0-3e1c-aa7c-f508ee0b721c | -7.42377 | -44.08371 | 2025-09-01 04:32:00 | NOAA-20 | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| a02a94aa-dcea-3cd4-852d-0a2c7fbf112e | -6.33179 | -53.43991 | 2025-09-01 04:32:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e825363a-b508-317a-8902-0883c646dd80 | -6.24348 | -43.39315 | 2025-09-01 04:32:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 5ccef6d5-cf2b-37ff-97f8-fb189d62e9ff | -7.87813 | -45.17802 | 2025-09-01 04:32:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 83b201f1-1c71-3e6d-a934-f3a72e80d376 | -6.93766 | -42.01313 | 2025-09-01 04:32:00 | NOAA-20 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 7de4a3fb-e671-35e8-af5c-3d3881f549b2 | -7.98028 | -46.43475 | 2025-09-01 04:32:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 9e608263-2c6d-341e-b638-b4fb8f38df8e | -10.04571 | -48.10642 | 2025-09-01 04:32:00 | NOAA-20 | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 7.9 |
| 41abd783-88a4-3b7e-addb-9fa909cdf482 | -7.76217 | -50.3242 | 2025-09-01 04:32:00 | NOAA-20 | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| d8d8dc25-8d84-31c3-b855-5d687f303d80 | -7.08017 | -44.3411 | 2025-09-01 04:32:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 373ffc29-c5bd-3071-9377-1e32fc100a11 | -9.23651 | -47.08249 | 2025-09-01 04:32:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 0d90329b-1972-3d6c-9745-258875b9d71d | -3.93607 | -48.44706 | 2025-09-01 04:32:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 6a3c1883-0da1-3c35-96b3-e9234db2366a | -6.9685 | -44.31219 | 2025-09-01 04:32:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 660d6b65-d216-3d63-9b7b-1666990bb25f | -6.85883 | -52.81517 | 2025-09-01 04:32:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 9359afb5-579f-371b-a811-bf481b10a897 | -5.3294 | -42.85966 | 2025-09-01 04:32:00 | NOAA-20 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Caatinga | 5.7 |
| bfd779cf-8247-30ec-a5dc-ae9239627e79 | -7.74454 | -50.25916 | 2025-09-01 04:32:00 | NOAA-20 | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 433977c3-c104-3406-ba1d-9b18c5432777 | -7.46126 | -44.81364 | 2025-09-01 04:32:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 2980e230-b1f3-31e0-b562-a54be2647151 | -4.91607 | -43.18194 | 2025-09-01 04:32:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| f0a1e2cb-a429-321f-87dd-994fe7a651c9 | -10.04348 | -48.09888 | 2025-09-01 04:32:00 | NOAA-20 | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 61c5dbfc-7360-30e1-a186-40d544388c69 | -5.72125 | -43.93835 | 2025-09-01 04:32:00 | NOAA-20 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 2bbb93ba-612a-3d0b-88bc-62200f08230f | -8.84042 | -49.54053 | 2025-09-01 04:32:00 | NOAA-20 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 943c7595-b5c0-3a06-bf68-c36b1bc306d1 | -6.28784 | -43.82188 | 2025-09-01 04:32:00 | NOAA-20 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 09d8399f-453f-32f6-98ed-35b0cb4136e4 | -5.73544 | -45.53015 | 2025-09-01 04:32:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 587c647f-cdd0-3d90-899f-d5457fc09fd1 | -9.64799 | -46.63033 | 2025-09-01 04:32:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 5cf16bd5-3eba-338a-a379-7ec4b4379b03 | -11.04015 | -45.14236 | 2025-09-01 04:32:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 87.2 |
| 8913b9ff-9ec0-39d0-a588-fdb50fd8e09c | -6.85967 | -52.81002 | 2025-09-01 04:32:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| eaef3031-2724-3bb4-9d5f-4c5c3dded1e4 | -9.38118 | -48.01558 | 2025-09-01 04:32:00 | NOAA-20 | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 75a33494-4c2a-36e5-adb5-5cbe5292f799 | -6.55164 | -44.07504 | 2025-09-01 04:32:00 | NOAA-20 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| d80321c9-89a5-3f46-bee0-026cc87a258e | -4.55181 | -46.43614 | 2025-09-01 04:32:00 | NOAA-20 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 782ba9c5-2503-3248-8348-d8c566299d29 | -4.73114 | -44.44976 | 2025-09-01 04:32:00 | NOAA-20 | SANTO ANTÔNIO DOS LOPES | MARANHÃO | Brasil | 2110302 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 4a9a7cb0-5bec-3571-9a69-0282d81fc451 | -4.27251 | -48.64197 | 2025-09-01 04:32:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 7a6d2217-c9ea-332a-a539-cec36dd5ba80 | -6.29473 | -43.82767 | 2025-09-01 04:32:00 | NOAA-20 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 87f5d6f8-7c37-3cde-bda4-77b42cd15df5 | -3.93663 | -48.44352 | 2025-09-01 04:32:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 1b7ff30b-c254-319b-8626-113ca0eb41f5 | -7.7377 | -50.25786 | 2025-09-01 04:32:00 | NOAA-20 | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 9905ed8d-6544-32d6-a9af-b6442ca0dee9 | -6.16236 | -43.31945 | 2025-09-01 04:32:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 618f49a3-a3ee-374a-adbb-ea75bc2d9481 | -8.90908 | -47.99479 | 2025-09-01 04:32:00 | NOAA-20 | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 250d00ea-a33c-3219-b4fa-6bc27d428f54 | -7.3997 | -47.44209 | 2025-09-01 04:32:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| b9680774-578a-3a42-963c-4ad115f7ae0d | -8.83309 | -47.80688 | 2025-09-01 04:32:00 | NOAA-20 | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| d5b42a2a-0e49-3159-8772-1f8cb0834b43 | -7.623 | -42.65308 | 2025-09-01 04:32:00 | NOAA-20 | RIBEIRA DO PIAUÍ | PIAUÍ | Brasil | 2208874 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 1b819618-8868-3f13-9e5d-5036e87f7ab0 | -11.04079 | -45.13789 | 2025-09-01 04:32:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 2f0bd88b-cb20-3d1c-b86c-c08edeb8754b | -7.42102 | -47.43498 | 2025-09-01 04:32:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 5fa069a1-2dfb-329e-98fd-567bf5bfd01a | -6.46729 | -42.43715 | 2025-09-01 04:32:00 | NOAA-20 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| af754545-2626-3888-bdc5-bdcf02cf722b | -6.82622 | -52.81504 | 2025-09-01 04:32:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| e8e5f7c5-f915-3c7d-b0e1-9e1a2f57b3e0 | -6.78418 | -44.6212 | 2025-09-01 04:32:00 | NOAA-20 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 38725339-7abf-31a3-b5f2-331e2e51fb3d | -6.53616 | -42.98768 | 2025-09-01 04:32:00 | NOAA-20 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| af17bdf7-9149-3187-bae9-5c724a61deaf | -9.66629 | -48.34055 | 2025-09-01 04:32:00 | NOAA-20 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 94a95713-20c1-3bd8-b711-52ff212ddc3f | -6.57874 | -43.71681 | 2025-09-01 04:32:00 | NOAA-20 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 4.0 |
| ea82a758-8e38-3c1d-becd-b43b8e469134 | -6.30084 | -43.6032 | 2025-09-01 04:32:00 | NOAA-20 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 1f66a367-52cf-3ca4-8a6a-db48fa631af3 | -6.35426 | -43.56182 | 2025-09-01 04:32:00 | NOAA-20 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| b6dceaea-e52d-3099-bc1f-894bbafbbdbb | -7.27616 | -60.65993 | 2025-09-01 04:32:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 3.6 |
| e5c60a69-2930-3701-82f2-304249775d50 | -8.77284 | -46.10422 | 2025-09-01 04:32:00 | NOAA-20 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| cba51979-50da-3aec-bb0e-663604764477 | -6.30598 | -43.64795 | 2025-09-01 04:32:00 | NOAA-20 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 587409e8-c135-37c5-9e33-cb5e64cea5f1 | -7.08389 | -44.34165 | 2025-09-01 04:32:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 7d617e4b-d5ca-32a4-978a-fa18eea3d440 | -6.80244 | -52.81086 | 2025-09-01 04:32:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 6f649ee8-cdbf-39d8-92f1-15d04e4cf0ec | -10.11077 | -49.28963 | 2025-09-01 04:32:00 | NOAA-20 | CHAPADA DE AREIA | TOCANTINS | Brasil | 1704600 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 174fa500-3dac-3ecc-aaa7-e4a9c904b687 | -9.70549 | -48.30777 | 2025-09-01 04:32:00 | NOAA-20 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 4df85023-24a6-3dc7-9ec1-4a9b301bc217 | -9.3845 | -48.0161 | 2025-09-01 04:32:00 | NOAA-20 | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 40d1bc8c-33e1-39e9-b006-30d95deb78c2 | -6.3088 | -43.62896 | 2025-09-01 04:32:00 | NOAA-20 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 743223b7-2d6d-35a2-a1d5-b7809e70bad9 | -7.67608 | -61.08259 | 2025-09-01 04:32:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 7.2 |
| 5597e414-dd79-3692-ad99-ae13a202e566 | -5.56412 | -47.41076 | 2025-09-01 04:32:00 | NOAA-20 | DAVINÓPOLIS | MARANHÃO | Brasil | 2103752 | 21 | 33 | nan | nan | nan | Cerrado | 5.7 |
| c47f2a6a-98da-313e-99bd-d02af76c520e | -11.04697 | -45.14797 | 2025-09-01 04:32:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 124.4 |
| 9dfcb7a1-4343-3263-b734-ff3de3da715a | -7.63032 | -46.54779 | 2025-09-01 04:32:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 3894659b-7107-3ce0-86c3-d178fde5b5d7 | -9.23258 | -47.08561 | 2025-09-01 04:32:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 04354f6c-93e5-31a1-8cf3-50c613c85ffd | -7.72055 | -50.25925 | 2025-09-01 04:32:00 | NOAA-20 | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 06b799e9-524d-3586-b649-2c32f6ab0062 | -7.39638 | -47.44157 | 2025-09-01 04:32:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 713abd61-62a7-3258-9aef-b740d575004b | -7.09637 | -44.55911 | 2025-09-01 04:32:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 640a66cf-8778-311d-a001-8dcab3ed0409 | -8.77575 | -46.10851 | 2025-09-01 04:32:00 | NOAA-20 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 7d8437d5-69ba-3579-a1ab-e048d5e6c9af | -6.53355 | -44.59692 | 2025-09-01 04:32:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| cef3eeb3-6031-3bb2-815b-14211edddbcf | -6.09241 | -43.33397 | 2025-09-01 04:32:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| a3fb89de-ef7f-378a-8fe8-d5731c42cfed | -7.69273 | -61.10415 | 2025-09-01 04:32:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| fc5a1d48-5269-33ad-9d9b-dc4a13420cd4 | -7.24542 | -44.06201 | 2025-09-01 04:32:00 | NOAA-20 | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| c1261018-b984-3bc7-a4aa-0fb2e4aaa43b | -6.57179 | -43.71101 | 2025-09-01 04:32:00 | NOAA-20 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 132d5bd7-2ccb-30f3-b3dc-eb7fa54c8ab4 | -6.81109 | -45.68491 | 2025-09-01 04:32:00 | NOAA-20 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |


[Clique aqui para ver as próximas entradas](README58.md)
