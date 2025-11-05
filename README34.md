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

## Dados Diários - Página 34

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 1e31ac09-1dbf-3c5f-91cd-ca1e9eec3b4a | -3.81134 | -52.26461 | 2025-11-05 05:01:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 42c1428f-51c7-39fc-8332-2b1953ae6c82 | -3.77111 | -51.71223 | 2025-11-05 05:01:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 1a068b62-6f3f-3eb1-a527-d1cf38fd7947 | -2.37229 | -53.97654 | 2025-11-05 05:01:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| cfd64109-0554-36e4-bc6e-f96149366b34 | -4.30078 | -43.79853 | 2025-11-05 05:01:00 | NOAA-21 | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| ffc8745e-7391-326c-80ed-fbfbac8217a3 | -1.24397 | -49.1414 | 2025-11-05 05:01:00 | NOAA-21 | MUANÁ | PARÁ | Brasil | 1504901 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 1ea75822-9b40-314c-ba28-560b9ce5909f | 0.63572 | -51.51076 | 2025-11-05 05:01:00 | NOAA-21 | PORTO GRANDE | AMAPÁ | Brasil | 1600535 | 16 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 4f5bc636-db6e-36be-9ba6-e1f7669810b0 | -3.24522 | -52.91819 | 2025-11-05 05:01:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 85d00798-540c-3e9d-8c2b-ad1ff84b67d0 | -6.42935 | -43.06971 | 2025-11-05 05:01:00 | NOAA-21 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 8fc9b281-344d-3ced-98af-abe4f4f55da9 | -5.92535 | -43.37121 | 2025-11-05 05:01:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Caatinga | 4.2 |
| 4141e05a-4214-3375-94e4-74e1c1f1a492 | 1.20356 | -52.97127 | 2025-11-05 05:01:00 | NOAA-21 | PEDRA BRANCA DO AMAPARI | AMAPÁ | Brasil | 1600154 | 16 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 24facfd1-d2ce-3cc4-8793-adcb236efa77 | -3.82482 | -48.66558 | 2025-11-05 05:01:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 9887dfa7-07bd-31fe-accc-5ab87b37e289 | -4.92084 | -47.32836 | 2025-11-05 05:01:00 | NOAA-21 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 6.4 |
| b69fa29e-f044-312d-92d2-a5c98a339031 | -3.41936 | -52.67511 | 2025-11-05 05:01:00 | NOAA-21 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b743330e-9d1c-3085-b8cc-737d143f8c44 | -3.33705 | -52.09567 | 2025-11-05 05:01:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f642d654-34e3-3699-b96e-eb233b872c86 | -3.79464 | -51.38437 | 2025-11-05 05:01:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 7c5dea0d-b6b0-3a5d-9071-328c05c3d79e | -3.48971 | -50.46345 | 2025-11-05 05:01:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 9.1 |
| 3a5b4f97-da66-3572-a97a-aa892f2b8a46 | -4.3588 | -50.88565 | 2025-11-05 05:01:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 001d3826-f0b3-30d3-8850-53459b3381d2 | -3.76996 | -51.71369 | 2025-11-05 05:01:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 790da30f-27f4-3596-9d3d-ab56c307053e | -3.44705 | -50.21662 | 2025-11-05 05:01:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| dd0d8cb0-fe89-375a-a171-82db6d24eeb1 | -3.68896 | -51.16547 | 2025-11-05 05:01:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| cdc54155-454a-343f-bd4c-8bd858798777 | -4.6713 | -46.30372 | 2025-11-05 05:01:00 | NOAA-21 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 1ce1ad49-2002-38f6-ac2d-6d6c2e78926b | -3.23017 | -43.43922 | 2025-11-05 05:01:00 | NOAA-21 | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 9b839ab6-35a8-3f7f-9de5-7df32f8ab9e8 | -2.72715 | -47.38972 | 2025-11-05 05:01:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 8f9c04f4-2ccb-3014-bcb7-919330404219 | -3.77048 | -51.71641 | 2025-11-05 05:01:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| f4699f8c-f15c-3865-89be-513f6d26a067 | -2.70418 | -49.87185 | 2025-11-05 05:01:00 | NOAA-21 | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| a3c4e0a0-ed6a-3263-bea4-16cd92d87cab | -5.29883 | -50.27561 | 2025-11-05 05:01:00 | NOAA-21 | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 94fd64cf-ecad-34c1-b38b-73bfac1b449f | -2.82684 | -49.41843 | 2025-11-05 05:01:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 9b408bd4-8a18-3457-ba56-dd56de0651e3 | -4.5565 | -46.76641 | 2025-11-05 05:01:00 | NOAA-21 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 2.4 |
| b03bf2bf-da20-338b-821d-26c5ef424bbe | -3.84601 | -49.90391 | 2025-11-05 05:01:00 | NOAA-21 | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| eceaab93-1c67-32f2-845f-40132c2e0c98 | -1.22028 | -49.13511 | 2025-11-05 05:01:00 | NOAA-21 | MUANÁ | PARÁ | Brasil | 1504901 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 506780f6-01da-301a-89d5-fb59ce7648db | -3.91414 | -54.25563 | 2025-11-05 05:01:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| e6378047-035d-38f9-ac73-833531ca0554 | -2.62582 | -49.22795 | 2025-11-05 05:01:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| bd498ae4-6df7-3e1e-834d-b966af1e40c0 | -3.47714 | -43.63713 | 2025-11-05 05:01:00 | NOAA-21 | SÃO BENEDITO DO RIO PRETO | MARANHÃO | Brasil | 2110401 | 21 | 33 | nan | nan | nan | Cerrado | 4.7 |
| e8d778a3-7985-32ae-ac2c-c5144c4d6ecd | -3.23712 | -43.43501 | 2025-11-05 05:01:00 | NOAA-21 | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 0a4be8e7-2f86-3243-ba8f-49a5779ad4a1 | -2.50732 | -56.198 | 2025-11-05 05:01:00 | NOAA-21 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| da274c9c-2396-3309-aadf-c88960ac2dd6 | -4.22825 | -56.20259 | 2025-11-05 05:01:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| d33f8a68-7874-3fa8-94f8-fc085eea7c83 | -4.11162 | -48.01773 | 2025-11-05 05:01:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| b38de6f0-d7c2-32d2-98e4-51050cce492e | -3.81867 | -51.07737 | 2025-11-05 05:01:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 74be618c-9b4c-34bc-ac08-9e6596074bb2 | -3.88023 | -49.11347 | 2025-11-05 05:01:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 438e06f4-2e7f-37fd-96b4-143d40600da5 | -6.71641 | -47.79227 | 2025-11-05 05:03:00 | NOAA-21 | DARCINÓPOLIS | TOCANTINS | Brasil | 1706506 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| dc2ee6f2-b266-38fa-9eea-c0401ee28c7d | -6.22337 | -55.6372 | 2025-11-05 05:03:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 91eb8840-57f8-309e-a8f2-034e2c4b5b87 | -6.06631 | -47.3065 | 2025-11-05 05:03:00 | NOAA-21 | RIBAMAR FIQUENE | MARANHÃO | Brasil | 2109551 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| af9d059d-baeb-34b4-a731-d79bb53898ea | -9.21201 | -48.59472 | 2025-11-05 05:03:00 | NOAA-21 | MIRANORTE | TOCANTINS | Brasil | 1713304 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 238b112e-196e-303e-b1be-e66d42da474b | -8.04935 | -49.63187 | 2025-11-05 05:03:00 | NOAA-21 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 7.7 |
| dcfd0fc8-5760-3aa8-931e-2678e0c9a725 | -8.85514 | -49.88058 | 2025-11-05 05:03:00 | NOAA-21 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| ec1b4f5b-c9de-301e-8be5-ae4afea306f0 | -7.97038 | -50.00257 | 2025-11-05 05:03:00 | NOAA-21 | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 6f69d27e-609e-3048-a19e-ffe657e0006b | -11.84335 | -43.72812 | 2025-11-05 05:03:00 | NOAA-21 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 6978ecb2-019e-3c2b-938b-6b37a5b89bd5 | -8.06131 | -49.64222 | 2025-11-05 05:03:00 | NOAA-21 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| b7f5cee6-15bd-31e8-8be3-ac20cf89fce8 | -12.23815 | -50.29034 | 2025-11-05 05:03:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 4bff3dfb-4f80-373d-8fb5-2b14b47bd759 | -8.86387 | -49.88188 | 2025-11-05 05:03:00 | NOAA-21 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 7.3 |
| bd84a5c0-20c0-3a3f-b3cc-3d801e31344a | -7.6713 | -47.42005 | 2025-11-05 05:03:00 | NOAA-21 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| d28b4db5-0569-363f-be54-45787355aae2 | -9.79565 | -49.30613 | 2025-11-05 05:03:00 | NOAA-21 | DIVINÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1707108 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| d01c1fc7-35e5-3239-952a-f1900197935a | -8.63132 | -54.55908 | 2025-11-05 05:03:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 686da3d2-464c-311c-bbe1-1aeee5eaf495 | -10.38549 | -47.75355 | 2025-11-05 05:03:00 | NOAA-21 | SANTA TEREZA DO TOCANTINS | TOCANTINS | Brasil | 1719004 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 0bd7e81c-f8e4-31bb-9168-ac9953d97926 | -8.05313 | -49.63677 | 2025-11-05 05:03:00 | NOAA-21 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 14.9 |
| 4c3a36f9-25e9-3f18-af6b-832172a64da0 | -6.33824 | -49.20571 | 2025-11-05 05:03:00 | NOAA-21 | PIÇARRA | PARÁ | Brasil | 1505635 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e914dbb4-82db-35c6-9317-599a0eafeba1 | -6.21628 | -46.13528 | 2025-11-05 05:03:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 7.4 |
| 534ad965-ef45-38c0-868a-2d09acd38034 | -7.94467 | -49.73437 | 2025-11-05 05:03:00 | NOAA-21 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f38236d7-75b0-390e-8125-d7daac06a964 | -10.37519 | -47.75189 | 2025-11-05 05:03:00 | NOAA-21 | SANTA TEREZA DO TOCANTINS | TOCANTINS | Brasil | 1719004 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 0a5b5516-2729-3a7c-a304-4b97d6ba0140 | -7.23613 | -45.69976 | 2025-11-05 05:03:00 | NOAA-21 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| dc8ec0f1-19c5-3c50-a205-8e6cfaef292c | -10.37696 | -47.75176 | 2025-11-05 05:03:00 | NOAA-21 | SANTA TEREZA DO TOCANTINS | TOCANTINS | Brasil | 1719004 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 08eca973-beb9-3e56-bdd3-c6499d23cb27 | -11.35137 | -55.05469 | 2025-11-05 05:03:00 | NOAA-21 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 130a439a-fa1e-3a3a-8199-b6d0666fff0b | -7.33057 | -47.25236 | 2025-11-05 05:03:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 3aba4e6e-f776-3d47-aefb-dc78761bdf5f | -7.33017 | -47.25537 | 2025-11-05 05:03:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 98ee02fc-1a3a-3f3e-a86b-7c1798b8ec7a | -7.28577 | -45.45494 | 2025-11-05 05:03:00 | NOAA-21 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 4.8 |
| c22ef731-2fa4-3a6a-bb8f-e3a706d00728 | -6.6437 | -42.28397 | 2025-11-05 05:03:00 | NOAA-21 | TANQUE DO PIAUÍ | PIAUÍ | Brasil | 2210979 | 22 | 33 | nan | nan | nan | Caatinga | 16.1 |
| 49a73893-9a75-3a92-af41-521a14186b04 | -10.38507 | -47.75672 | 2025-11-05 05:03:00 | NOAA-21 | SANTA TEREZA DO TOCANTINS | TOCANTINS | Brasil | 1719004 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| f9ed7f12-9e53-3f51-8d26-4486db948bf0 | -6.12117 | -57.70747 | 2025-11-05 05:03:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 7a920399-7151-324c-89ea-d1b51b6a0976 | -9.06324 | -48.83467 | 2025-11-05 05:03:00 | NOAA-21 | GOIANORTE | TOCANTINS | Brasil | 1708304 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 4b2cc05e-2ffe-3548-9ed7-be3341738462 | -7.4252 | -47.13412 | 2025-11-05 05:03:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| d46e858c-962f-380c-b268-07e2acddee1f | -11.84495 | -43.73219 | 2025-11-05 05:03:00 | NOAA-21 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 8.2 |
| 12aa0d3c-d44b-3a6d-8d73-5c062e91e8f6 | -8.06071 | -49.64647 | 2025-11-05 05:03:00 | NOAA-21 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 9aa22c2c-80b6-355c-8f6f-af3e9b7cb8c8 | -6.73752 | -44.14975 | 2025-11-05 05:03:00 | NOAA-21 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 48.5 |
| aaca4481-e6bb-30fa-a504-c3ae403a1bed | -10.37141 | -47.75415 | 2025-11-05 05:03:00 | NOAA-21 | SANTA TEREZA DO TOCANTINS | TOCANTINS | Brasil | 1719004 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 5e8ca8c1-3bee-3e86-b4a5-41080ceb8b01 | -9.06391 | -48.82963 | 2025-11-05 05:03:00 | NOAA-21 | GOIANORTE | TOCANTINS | Brasil | 1708304 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 6a0927cd-0c40-39b8-b29a-71034460c729 | -8.22849 | -49.98301 | 2025-11-05 05:03:00 | NOAA-21 | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| d394be37-1a08-39ea-883b-252cc9947aeb | -9.87847 | -47.46272 | 2025-11-05 05:03:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 69d23221-cd6e-3993-b3e9-d9d03323099f | -8.27623 | -48.00796 | 2025-11-05 05:03:00 | NOAA-21 | ITAPIRATINS | TOCANTINS | Brasil | 1710904 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 1e7931e4-c2b2-3afc-aa22-c1c4f4383abe | -10.93181 | -59.02449 | 2025-11-05 05:03:00 | NOAA-21 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 66e14d72-6626-358e-9392-ea0fcc21a711 | -8.85951 | -49.88123 | 2025-11-05 05:03:00 | NOAA-21 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 7.3 |
| 64de6d83-0994-3d44-a6ab-a246a89e57e0 | -7.4423 | -46.61142 | 2025-11-05 05:03:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 08f7dc63-752a-31a4-9cd8-593eae0efc3e | -7.54836 | -45.85001 | 2025-11-05 05:03:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| aefa169d-30f9-39e6-bd85-e4bbf447792e | -7.28631 | -45.45089 | 2025-11-05 05:03:00 | NOAA-21 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 4aebbd25-8efb-345d-9bf3-6139864ae19f | -10.37181 | -47.75091 | 2025-11-05 05:03:00 | NOAA-21 | SANTA TEREZA DO TOCANTINS | TOCANTINS | Brasil | 1719004 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 844cef34-d7c4-31f6-a1c8-030cfa86047c | -11.13076 | -55.19043 | 2025-11-05 05:03:00 | NOAA-21 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| c2a8a84b-7832-3367-b4fd-f52d7a3873db | -8.05374 | -49.63253 | 2025-11-05 05:03:00 | NOAA-21 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 7.7 |
| 019da2ca-3a89-3606-bb01-896af55c10fe | -7.44275 | -46.608 | 2025-11-05 05:03:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 9a900129-25f3-3686-b0b6-f7d68ad54cb8 | -11.01188 | -42.73319 | 2025-11-05 05:03:00 | NOAA-21 | GENTIO DO OURO | BAHIA | Brasil | 2911303 | 29 | 33 | nan | nan | nan | Caatinga | 3.5 |
| 39b25455-0cd6-327f-b002-eeb660b4061b | -7.94033 | -49.73368 | 2025-11-05 05:03:00 | NOAA-21 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 9658892b-6950-3ab3-8374-90badf04ee6c | -7.30952 | -46.29273 | 2025-11-05 05:03:00 | NOAA-21 | NOVA COLINAS | MARANHÃO | Brasil | 2107258 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 1edda0f8-2bb2-367f-9d59-f0194e553610 | -6.22171 | -46.13607 | 2025-11-05 05:03:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 7.4 |
| 5d19be36-a52b-3921-8fe5-e73a2aa5468a | -12.24262 | -50.29098 | 2025-11-05 05:03:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| b03f07a4-c097-3e83-806d-a667cd02da5c | -6.55138 | -44.46804 | 2025-11-05 05:03:00 | NOAA-21 | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| d98ba7c7-7497-310e-a4a6-d05ca6c1dcf5 | -9.88451 | -47.45699 | 2025-11-05 05:03:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 0ab5d2d9-5968-397b-a94b-85e583b47aa8 | -11.35081 | -55.05839 | 2025-11-05 05:03:00 | NOAA-21 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| b0303ee6-531b-3cd1-8060-5d2749278e48 | -6.55598 | -44.47264 | 2025-11-05 05:03:00 | NOAA-21 | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 7a33d0ea-64b0-3efa-952e-32c5da740767 | -6.54429 | -47.03068 | 2025-11-05 05:03:00 | NOAA-21 | SÃO JOÃO DO PARAÍSO | MARANHÃO | Brasil | 2111052 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 450fc0c6-1332-3ae5-ac91-43bf6a4d9b48 | -7.87372 | -46.79087 | 2025-11-05 05:03:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 39d9f206-163c-39fb-87b4-c3a05a60a3ff | -7.67171 | -47.417 | 2025-11-05 05:03:00 | NOAA-21 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| dec87358-b24c-3f01-a503-85bec0f43006 | -12.23369 | -50.28971 | 2025-11-05 05:03:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |


[Clique aqui para ver as próximas entradas](README35.md)
