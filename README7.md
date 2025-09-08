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

## Dados Diários - Página 7

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 0cce1590-3649-3eb9-bf23-cdb82c63488d | -20.4613 | -43.9799 | 2025-09-08 00:25:00 | METOP-C | BELO VALE | MINAS GERAIS | Brasil | 3106408 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| ec82203f-5933-3218-89bc-17dc56002494 | -9.8049 | -47.7728 | 2025-09-08 00:25:00 | METOP-C | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| cedaf6a2-f01b-3576-9da0-5b0c3a991740 | -9.1831 | -46.0466 | 2025-09-08 00:25:00 | METOP-C | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| dba5ce3b-fcef-3593-a820-6641893622dd | -5.2051 | -43.712601 | 2025-09-08 00:25:00 | METOP-C | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 4ca5b0c7-6533-34f9-93f2-fc332041779e | -5.6565 | -45.4631 | 2025-09-08 00:25:00 | METOP-C | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 521f2829-b6e8-3b2a-b2f6-77d415d4854b | -5.6244 | -43.921501 | 2025-09-08 00:25:00 | METOP-C | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 31c1d372-9e69-342c-9cf1-659d5e6d76aa | -14.452 | -48.795399 | 2025-09-08 00:25:00 | METOP-C | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| b5fd0dc3-b380-30cd-b1ac-d6ce028a12a7 | -6.7589 | -43.426498 | 2025-09-08 00:25:00 | METOP-C | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Caatinga | nan |
| 6b513733-01d8-3125-9d2d-50b05798d776 | -11.3814 | -50.393101 | 2025-09-08 00:25:00 | METOP-C | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 80cbee4b-1d52-3e1f-a1d1-150448540833 | -16.905899 | -45.844398 | 2025-09-08 00:25:00 | METOP-C | BRASILÂNDIA DE MINAS | MINAS GERAIS | Brasil | 3108552 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 3d46fe71-7a03-3268-b661-5db6c33cb1da | -9.7025 | -43.9925 | 2025-09-08 00:25:00 | METOP-C | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 6b33d272-337f-320b-8404-069129436bc5 | -10.2707 | -48.810398 | 2025-09-08 00:25:00 | METOP-C | PARAÍSO DO TOCANTINS | TOCANTINS | Brasil | 1716109 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 95e86111-cdf2-32b9-9685-110601f84d85 | -5.9445 | -45.7799 | 2025-09-08 00:25:00 | METOP-C | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| b451f24e-a241-35f3-b85c-514d99f6e1b8 | -16.312201 | -43.0723 | 2025-09-08 00:25:00 | METOP-C | GRÃO MOGOL | MINAS GERAIS | Brasil | 3127800 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 8d1375f4-34e8-3a22-92f2-2d8afde41012 | -9.8447 | -46.582298 | 2025-09-08 00:25:00 | METOP-C | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| cf2f508b-15c9-3d77-8512-4aa4528faf31 | -6.6089 | -53.349602 | 2025-09-08 00:25:00 | METOP-C | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 6f193a18-fb5f-3231-a56a-79e14368ad4d | -7.7653 | -50.754799 | 2025-09-08 00:25:00 | METOP-C | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 2b8dd5db-7057-370e-9bfe-edde9d53ec12 | -18.937 | -46.795601 | 2025-09-08 00:25:00 | METOP-C | PATROCÍNIO | MINAS GERAIS | Brasil | 3148103 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 65d1c895-cfe7-36ef-8cee-8eee2eba4428 | -5.8694 | -46.040001 | 2025-09-08 00:25:00 | METOP-C | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 919cdedc-c597-378e-af9f-57e1127686b5 | -6.1832 | -43.614799 | 2025-09-08 00:25:00 | METOP-C | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 99a5b308-ed35-313d-8214-8bdca515c15e | -5.4538 | -42.823898 | 2025-09-08 00:25:00 | METOP-C | NAZÁRIA | PIAUÍ | Brasil | 2206720 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| e8415ffe-2aba-3789-aa29-6b9ff7cf8859 | -3.2944 | -48.720402 | 2025-09-08 00:25:00 | METOP-C | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a7e51db2-927f-3d3a-a36a-881c1beb2210 | -3.2964 | -48.7295 | 2025-09-08 00:25:00 | METOP-C | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 294cc931-25c8-320a-8326-47cf82f52417 | -6.1625 | -44.787399 | 2025-09-08 00:25:00 | METOP-C | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| bc19175b-ad29-3d12-8bc3-f0dcb836905b | -14.2761 | -44.868 | 2025-09-08 00:25:00 | METOP-C | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 924d48fb-5c9b-32eb-a84f-053e9a30da2b | -6.3902 | -42.9907 | 2025-09-08 00:25:00 | METOP-C | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 8e49be0f-c877-3193-91aa-6fbf8efeb173 | -11.3716 | -50.395 | 2025-09-08 00:25:00 | METOP-C | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 4c3f62d5-0bc8-3802-84e3-cbb46eeb5fbf | -8.6101 | -40.212399 | 2025-09-08 00:25:00 | METOP-C | LAGOA GRANDE | PERNAMBUCO | Brasil | 2608750 | 26 | 33 | nan | nan | nan | Caatinga | nan |
| bfe1589a-1c3f-3822-92f3-955598c3950e | -5.4303 | -43.436298 | 2025-09-08 00:25:00 | METOP-C | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| e7c372e4-5cb8-32e6-ad29-d352dfba6922 | -18.939301 | -46.807301 | 2025-09-08 00:25:00 | METOP-C | PATROCÍNIO | MINAS GERAIS | Brasil | 3148103 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 58e7071d-e1ab-3b06-8ac0-9a19b326725a | -13.8197 | -46.292 | 2025-09-08 00:25:00 | METOP-C | GUARANI DE GOIÁS | GOIÁS | Brasil | 5209408 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 70476266-a7eb-3cf8-8539-a3d430a0d75a | -8.0241 | -44.0438 | 2025-09-08 00:25:00 | METOP-C | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| bf7fee0c-17f2-3be9-839d-18cee9cebe66 | -5.6533 | -45.4491 | 2025-09-08 00:25:00 | METOP-C | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 4d0c1cb7-bcd9-36be-85f7-6225061fe0a1 | -11.388 | -50.3759 | 2025-09-08 00:25:00 | METOP-C | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 15ee326a-34ce-3aa7-99c8-271504253c2d | -6.3409 | -42.598999 | 2025-09-08 00:25:00 | METOP-C | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| c8c07789-f4dd-393c-b6d3-6c7cd3354808 | -6.5812 | -44.001099 | 2025-09-08 00:25:00 | METOP-C | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 25a8e18e-86ea-31be-99f7-6cfbcde1b733 | -6.9072 | -44.3456 | 2025-09-08 00:25:00 | METOP-C | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| dd3e2a62-e8a0-3d5e-ae5c-c89477af288b | -6.0639 | -43.365799 | 2025-09-08 00:25:00 | METOP-C | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Caatinga | nan |
| f48c8ea9-773c-37bd-bcd4-8c2e2dda7d90 | -6.2051 | -42.5923 | 2025-09-08 00:25:00 | METOP-C | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 2fd1e105-e133-31d0-9f5f-ddec0518aa90 | -6.5471 | -42.955002 | 2025-09-08 00:25:00 | METOP-C | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| eb86431f-dad0-32d4-ad9e-19373f85dac2 | -16.9 | -45.8158 | 2025-09-08 00:25:00 | METOP-C | BRASILÂNDIA DE MINAS | MINAS GERAIS | Brasil | 3108552 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 1b8fed63-75d1-3399-aa3f-f37b551d173c | -11.3728 | -43.541 | 2025-09-08 00:25:00 | METOP-C | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| e24228e0-c0da-307e-8e70-995288384615 | -11.392 | -43.5807 | 2025-09-08 00:25:00 | METOP-C | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| a2c67312-a273-35f4-953e-808f2d4924f1 | -6.3882 | -43.878899 | 2025-09-08 00:25:00 | METOP-C | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| eec5c972-c029-3bff-9b65-acc98b185555 | -13.6344 | -43.805 | 2025-09-08 00:25:00 | METOP-C | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 9cab0d11-70f5-399d-a434-115b76a07399 | -13.6246 | -43.807301 | 2025-09-08 00:25:00 | METOP-C | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 17dfc989-84e1-32de-90d8-0f6b72c95992 | -13.6262 | -43.814499 | 2025-09-08 00:25:00 | METOP-C | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 1c0596d5-ef5c-372d-9312-0220739206ff | -6.2031 | -43.297699 | 2025-09-08 00:25:00 | METOP-C | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| df972858-420f-3aa4-b8ca-6fdc9b6d499a | -6.8409 | -44.824799 | 2025-09-08 00:25:00 | METOP-C | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| dcbeeeeb-3f01-390f-92f9-ed107b59cb99 | -11.365 | -50.4123 | 2025-09-08 00:25:00 | METOP-C | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 7eea12a8-712b-337e-8a7e-1a732b2b4b63 | -11.2666 | -46.470501 | 2025-09-08 00:25:00 | METOP-C | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| fcbf5858-296e-3c37-9ded-c658f827127e | -6.1776 | -42.651402 | 2025-09-08 00:25:00 | METOP-C | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 1fe4d10e-1db3-366a-b6fc-8b3035c17e36 | -6.4447 | -43.9454 | 2025-09-08 00:25:00 | METOP-C | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 3c099342-5192-3b0c-9cbe-c70031243145 | -12.1558 | -43.9575 | 2025-09-08 00:25:00 | METOP-C | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 3396f637-7fcc-3ad0-a293-6f16342d5d61 | -9.6888 | -43.522099 | 2025-09-08 00:25:00 | METOP-C | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 85ecbb91-b369-3599-a0fc-d7648c29c77b | -6.2429 | -43.695301 | 2025-09-08 00:25:00 | METOP-C | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 1c11ca50-e736-31a1-87fa-f27a5b9bc6e9 | -19.1719 | -42.083599 | 2025-09-08 00:25:00 | METOP-C | FERNANDES TOURINHO | MINAS GERAIS | Brasil | 3125804 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| b7c2e316-8817-3fcf-9cb3-3fbc6308d1db | -6.4697 | -41.778 | 2025-09-08 00:25:00 | METOP-C | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 25e0c20d-dc2e-3fea-aa1e-fe5133bfcd99 | -5.8661 | -46.025398 | 2025-09-08 00:25:00 | METOP-C | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 23927e65-f3af-3d5f-99b4-20bcf353c2b4 | -11.3759 | -43.554901 | 2025-09-08 00:25:00 | METOP-C | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 3fc3afd3-213f-35e2-9cef-464b0ac7ecbb | -4.9738 | -43.157001 | 2025-09-08 00:25:00 | METOP-C | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| e3ee1d7b-42d6-394f-94ae-fcd590d4e713 | -4.2532 | -48.185101 | 2025-09-08 00:25:00 | METOP-C | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b00f3cc0-8c2f-30b3-8e71-cb7d6cd71a9a | -19.180099 | -42.073898 | 2025-09-08 00:25:00 | METOP-C | ENGENHEIRO CALDAS | MINAS GERAIS | Brasil | 3123700 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 022f7d73-9333-3f7b-8f48-b8891cddb67b | -3.3223 | -44.092999 | 2025-09-08 00:25:00 | METOP-C | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| b91c558a-a222-3c86-9368-54f7cbf24a12 | -11.3295 | -50.387699 | 2025-09-08 00:25:00 | METOP-C | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 8e837126-7fcf-351d-ab49-acae75b396da | -6.2015 | -43.290699 | 2025-09-08 00:25:00 | METOP-C | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| d0919ea6-fe35-3f40-bba1-f39582dc9975 | -11.2831 | -46.4591 | 2025-09-08 00:30:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 72.9 |
| 71b156e5-6be3-32b1-9391-fedebda6d959 | -11.3748 | -50.3783 | 2025-09-08 00:30:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 64.0 |
| 6f74f37f-1008-389a-9946-97d81735e7ec | -12.948 | -54.7724 | 2025-09-08 00:30:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 67.9 |
| 38d3baf2-f8e4-3c40-80a9-334124c6a29c | -6.6198 | -53.3576 | 2025-09-08 00:30:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 64.9 |
| b7ce169e-b4cd-3554-906f-78d546ce1033 | -9.453 | -61.8338 | 2025-09-08 00:30:00 | GOES-19 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 69.4 |
| 19a01f3c-a3d1-33aa-99bb-f4f4e6c1ff78 | -10.0495 | -59.3547 | 2025-09-08 00:30:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 92.6 |
| e17b1db3-ad5b-312f-ad92-82ded520b02c | -17.482 | -39.9449 | 2025-09-08 00:30:00 | GOES-19 | CARAVELAS | BAHIA | Brasil | 2906907 | 29 | 33 | nan | nan | nan | Mata Atlântica | 169.0 |
| 9a755983-384e-34b7-aaf9-2de0c7a91fec | -7.4168 | -61.6339 | 2025-09-08 00:30:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 117.9 |
| 899cee51-5b6a-347e-9be1-9e479d23c4bf | -14.527 | -48.7611 | 2025-09-08 00:30:00 | GOES-19 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 58.5 |
| 99288ed0-8910-3137-9948-6bf7cac4898b | -11.2007 | -54.9992 | 2025-09-08 00:30:00 | GOES-19 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 132.2 |
| 11cf4eb0-ff14-3940-bbeb-c2ae567c2cdf | -7.3799 | -61.6353 | 2025-09-08 00:30:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 84.6 |
| e9238533-4a44-3cce-b33b-97a5d324da80 | -6.8282 | -52.7938 | 2025-09-08 00:30:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 56.4 |
| 9b1a230b-b0ed-3d64-a4e0-23f11e4d0f4d | -22.3306 | -52.2665 | 2025-09-08 00:30:00 | GOES-19 | TEODORO SAMPAIO | SÃO PAULO | Brasil | 3554300 | 35 | 33 | nan | nan | nan | Mata Atlântica | 83.8 |
| a4aa7550-be38-3b33-84c4-1fb2d53bc335 | -10.0682 | -59.3536 | 2025-09-08 00:30:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 66.1 |
| 4e6085a5-f368-3437-b7ac-90d75b10b74c | -12.9477 | -54.793 | 2025-09-08 00:30:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 127.0 |
| e79e8fc4-cba4-34b8-a637-318cfadda259 | -11.2005 | -55.0195 | 2025-09-08 00:30:00 | GOES-19 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 93.8 |
| b93b257c-6fa9-3af8-bd5a-4ec95f517b45 | -22.3395 | -51.9287 | 2025-09-08 00:30:00 | GOES-19 | MIRANTE DO PARANAPANEMA | SÃO PAULO | Brasil | 3530201 | 35 | 33 | nan | nan | nan | Mata Atlântica | 82.0 |
| 8faabb33-30fc-33c0-b62f-c60acfc548ff | -3.316 | -48.7134 | 2025-09-08 00:30:00 | GOES-19 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 73.7 |
| f137e383-105b-3dab-98a6-361534c57007 | -8.8821 | -64.2238 | 2025-09-08 00:30:00 | GOES-19 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 67.1 |
| c1e336c7-7ac8-30a3-98a3-1552b7739d2d | -9.173 | -59.3659 | 2025-09-08 00:30:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 68.8 |
| 84c17c04-90ca-3b1e-bc9d-033bb361b0ba | -9.4624 | -60.4912 | 2025-09-08 00:30:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 69.1 |
| 22c092f7-dc37-31c2-bf8a-616cb0226cfe | -12.1699 | -43.9338 | 2025-09-08 00:30:00 | GOES-19 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 84.9 |
| 21df0ee8-e723-3841-b8ec-79d9fd71b4e0 | -11.3745 | -50.3997 | 2025-09-08 00:30:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 90.8 |
| a3a4c932-0a91-3b82-b581-ef78e5a110d8 | -6.6382 | -53.377 | 2025-09-08 00:30:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 76.1 |
| 4a3554e2-5083-3ef9-98b7-aef0dad4f83b | -7.3984 | -61.6156 | 2025-09-08 00:30:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 84.0 |
| c6e65398-fbad-3d93-b283-64132297d2b8 | -10.0493 | -59.3742 | 2025-09-08 00:30:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 91.3 |
| 0a2992d1-6cf6-39f5-ac74-77e7de11f792 | -12.9474 | -54.8135 | 2025-09-08 00:30:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | 73.6 |
| eaa9c06a-789a-396a-89dd-2dafb77fd250 | -9.4531 | -61.8147 | 2025-09-08 00:30:00 | GOES-19 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 77.9 |
| a17a2469-68c3-3def-a95e-13eb6a87293f | -9.4345 | -61.8156 | 2025-09-08 00:30:00 | GOES-19 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 89.9 |
| e1e834b9-9ca9-3579-936c-27d59d5d8f2b | -14.5266 | -48.7833 | 2025-09-08 00:30:00 | GOES-19 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 36.7 |
| 8cac5c83-0dfa-3b78-b375-47c7148b539a | -11.3742 | -50.4212 | 2025-09-08 00:30:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 87.0 |
| 8d2cc895-f947-3706-87bb-c37cac6fb28f | -6.4605 | -43.9532 | 2025-09-08 00:30:00 | GOES-19 | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 119.0 |
| 027e80d8-67d1-3cce-8f44-99a44f9f6422 | -8.6219 | -40.2058 | 2025-09-08 00:30:00 | GOES-19 | LAGOA GRANDE | PERNAMBUCO | Brasil | 2608750 | 26 | 33 | nan | nan | nan | Caatinga | 119.5 |
| e74ed4af-6d50-33c7-aba0-82792e3e42be | -17.4828 | -39.9188 | 2025-09-08 00:30:00 | GOES-19 | TEIXEIRA DE FREITAS | BAHIA | Brasil | 2931350 | 29 | 33 | nan | nan | nan | Mata Atlântica | 69.3 |


[Clique aqui para ver as próximas entradas](README8.md)
