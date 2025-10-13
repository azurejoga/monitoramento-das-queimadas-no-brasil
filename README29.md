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

## Dados Diários - Página 29

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 68bdb19a-086e-397d-943a-53933bffb9a1 | -4.66929 | -46.2877 | 2025-10-13 04:44:00 | NOAA-20 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 8c0f76a3-0970-3686-bef4-08b150ebfd89 | -2.95645 | -49.20543 | 2025-10-13 04:44:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 2b531726-06ac-3e70-aa0b-2b3ce3e47d0d | -8.5369 | -44.58847 | 2025-10-13 04:44:00 | NOAA-20 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 7.3 |
| f1a65b75-87a8-3c10-81fb-84dc116ee5c9 | -3.4055 | -46.89943 | 2025-10-13 04:44:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 896279db-6ed7-3f25-938c-9f2bb20c2618 | -3.85017 | -50.96909 | 2025-10-13 04:44:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| a18be630-5ed7-32a3-8625-aa61a07df096 | -6.72937 | -42.07428 | 2025-10-13 04:44:00 | NOAA-20 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| c8074a9c-28d2-361c-bc2f-10ff53fa1c8e | -7.54297 | -46.0995 | 2025-10-13 04:44:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 1e69f984-6444-3e2e-99d5-bc8d5aca3621 | -4.18301 | -46.23056 | 2025-10-13 04:44:00 | NOAA-20 | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 8055af0a-cfea-3850-97e0-c20a0fd8e664 | -4.47799 | -44.94168 | 2025-10-13 04:44:00 | NOAA-20 | LAGO DO JUNCO | MARANHÃO | Brasil | 2105807 | 21 | 33 | nan | nan | nan | Amazônia | 5.1 |
| a9c0c8a0-fa44-38c6-98a6-0ba0fb1e49d3 | -7.69422 | -42.37753 | 2025-10-13 04:44:00 | NOAA-20 | SÃO MIGUEL DO FIDALGO | PIAUÍ | Brasil | 2210391 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 0b26e06c-237a-3368-a762-d35bd1d18360 | -3.91926 | -50.01545 | 2025-10-13 04:44:00 | NOAA-20 | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 1e9ecf2c-0291-3b51-acab-aec558493aea | -7.65228 | -42.5701 | 2025-10-13 04:44:00 | NOAA-20 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 5ee22dfd-b138-3a5b-9550-3efc2cd4f5b6 | -3.13804 | -50.21018 | 2025-10-13 04:44:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 6.6 |
| 336d1c80-3b62-31ea-ab58-f8245bc7d08f | -3.38533 | -50.17126 | 2025-10-13 04:44:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c76a4e86-4548-3d32-9e25-f6ea45c22f0d | -6.94205 | -42.04814 | 2025-10-13 04:44:00 | NOAA-20 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 1dff121e-7b01-3456-8a7c-ca681b90f343 | -7.50653 | -44.63245 | 2025-10-13 04:44:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 5aefd5ce-de19-33db-9cce-2b381f89c8a0 | -8.44974 | -46.12263 | 2025-10-13 04:44:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 7.5 |
| 21c2fe99-38ca-3910-8478-36c6c7044377 | -5.53567 | -46.49364 | 2025-10-13 04:44:00 | NOAA-20 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 19cd69f7-9cd5-317f-a598-72026d217073 | -3.06765 | -49.40466 | 2025-10-13 04:44:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 11.1 |
| 7a359b9a-e452-3cbc-82e5-dbaf9ad764ce | -7.64124 | -42.57447 | 2025-10-13 04:44:00 | NOAA-20 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 61ce8148-27e3-3423-99b7-08d8c9e013ea | -7.70074 | -42.36855 | 2025-10-13 04:44:00 | NOAA-20 | SÃO MIGUEL DO FIDALGO | PIAUÍ | Brasil | 2210391 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| c8509530-ccef-3210-adda-778025ae68b2 | -5.93135 | -40.88429 | 2025-10-13 04:44:00 | NOAA-20 | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 1023415b-8928-374d-adc3-064a99f9ea25 | -4.28386 | -48.56988 | 2025-10-13 04:44:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 26ae2d6e-81e5-363a-bbc7-789a317dd08b | -5.21888 | -50.95186 | 2025-10-13 04:44:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| ea0bed57-e398-31ad-b66d-98b688c26d19 | -8.04805 | -47.09203 | 2025-10-13 04:44:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 2880e6f0-f701-3838-9de4-794312bbf658 | -7.50778 | -44.59197 | 2025-10-13 04:44:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 3.5 |
| c58061d3-7c5c-3443-ab1b-d89c32cf26f7 | -2.88601 | -50.72854 | 2025-10-13 04:44:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 8e4298e5-3ff6-325a-b30e-cfa11631ab88 | -5.93662 | -44.21632 | 2025-10-13 04:44:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 9.9 |
| 4ca642a7-3779-3c09-9679-994220f6c53b | -7.33579 | -43.86401 | 2025-10-13 04:44:00 | NOAA-20 | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 85de3c91-13b6-3175-ae5b-d176bae70f25 | -7.50335 | -44.59127 | 2025-10-13 04:44:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 456be760-aaff-3327-845c-293f1de59252 | -3.37105 | -52.17481 | 2025-10-13 04:44:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 3f53a4d7-2958-3226-8418-95d858499d78 | -5.5784 | -41.10605 | 2025-10-13 04:44:00 | NOAA-20 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 0.7 |
| dc5810ae-3091-3dd5-91e9-bb1deb818369 | -7.6877 | -42.57845 | 2025-10-13 04:44:00 | NOAA-20 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| b29a42f3-273a-3e80-976c-6c478ab9c284 | -3.58475 | -47.28307 | 2025-10-13 04:44:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 8.8 |
| 2c71dda9-f26e-3ac3-823b-cbae56f8240d | -6.67625 | -46.02878 | 2025-10-13 04:44:00 | NOAA-20 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 9a4edf22-9543-3a8d-85a8-9f6b93510a3a | -8.23013 | -43.3445 | 2025-10-13 04:44:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 3.7 |
| dafcb0f1-8b58-3da2-ad54-e4291998f4d0 | -10.03485 | -43.81022 | 2025-10-13 04:44:00 | NOAA-20 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 3.1 |
| 103e8de0-49ee-38b7-9e5a-7f0e00a8e780 | -7.31907 | -47.81649 | 2025-10-13 04:44:00 | NOAA-20 | BABAÇULÂNDIA | TOCANTINS | Brasil | 1703008 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| e8687dc8-f37d-34e2-a820-d8619b4aef46 | -4.86502 | -45.73511 | 2025-10-13 04:44:00 | NOAA-20 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| fb5779c6-38f5-31fc-b83c-500ce4f227df | -8.46497 | -46.13224 | 2025-10-13 04:44:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 11fd1682-3425-3c45-8ca9-caa4f8e59347 | -3.61701 | -51.06834 | 2025-10-13 04:44:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 97c4c76c-19a8-367c-8e6e-148d25d11776 | -4.51228 | -50.39114 | 2025-10-13 04:44:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| c9987c4b-ba25-3589-a1cd-e7a611088622 | -10.03273 | -45.6902 | 2025-10-13 04:44:00 | NOAA-20 | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 8e9a9bb5-de28-3ba0-a179-f393b4ad2aa5 | -6.48001 | -42.05856 | 2025-10-13 04:44:00 | NOAA-20 | BARRA D'ALCÂNTARA | PIAUÍ | Brasil | 2201176 | 22 | 33 | nan | nan | nan | Caatinga | 2.8 |
| 93512e5a-4e8b-317b-b057-4d181a649ba0 | -7.28507 | -41.96156 | 2025-10-13 04:44:00 | NOAA-20 | WALL FERRAZ | PIAUÍ | Brasil | 2211704 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 31389f8b-cba7-3860-a0b4-ed8fe8b13529 | -10.80085 | -43.97621 | 2025-10-13 04:44:00 | NOAA-20 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 84726b53-23f1-378c-96cd-e190c7c2b123 | -10.80779 | -43.96111 | 2025-10-13 04:44:00 | NOAA-20 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 5.3 |
| e02769bb-de64-3d0b-a4e8-2519439e7dc8 | -8.53889 | -44.58708 | 2025-10-13 04:44:00 | NOAA-20 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 11.6 |
| b42b5983-55a5-30cb-8090-a2a532769edb | -8.22523 | -43.34381 | 2025-10-13 04:44:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 3.7 |
| 09f84a60-ba44-3fc7-8e4b-fb75c2489254 | -7.48393 | -42.76177 | 2025-10-13 04:44:00 | NOAA-20 | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 97be7f76-9c63-36cd-a016-96d085c1912e | -4.86664 | -45.91 | 2025-10-13 04:44:00 | NOAA-20 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| c3573201-3fef-35c3-a7e1-a564522393b8 | -10.80921 | -43.98805 | 2025-10-13 04:44:00 | NOAA-20 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 32.8 |
| 881985ea-663d-309e-8aca-2e6d22e3735e | -4.88538 | -37.50438 | 2025-10-13 04:44:00 | NOAA-20 | ARACATI | CEARÁ | Brasil | 2301109 | 23 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 2b6bf4a5-5687-3861-b363-45cb93bd6054 | -3.13478 | -49.51798 | 2025-10-13 04:44:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| f94b3c13-b62c-35b9-94f9-829d6b953a85 | -3.09732 | -50.37956 | 2025-10-13 04:44:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 8.8 |
| 74ba8c00-88f9-37c2-aa42-714bedb6982c | -7.48474 | -42.75602 | 2025-10-13 04:44:00 | NOAA-20 | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| dabd51f0-7a22-31e1-bc50-5228226614ba | -2.88381 | -50.74242 | 2025-10-13 04:44:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| c4663b5c-16cd-3934-89ae-cdcfc452e195 | -3.06379 | -49.40762 | 2025-10-13 04:44:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| e7b14f09-bb54-36c8-aa66-e0617dec3940 | -6.48042 | -42.05565 | 2025-10-13 04:44:00 | NOAA-20 | BARRA D'ALCÂNTARA | PIAUÍ | Brasil | 2201176 | 22 | 33 | nan | nan | nan | Caatinga | 4.5 |
| 8035e4d6-5f8d-3b7f-9b6b-cd2c8183365b | -7.49385 | -44.62619 | 2025-10-13 04:44:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 18.3 |
| 0cd524f9-69a0-3ff7-a5d6-f85745d0e5e9 | -7.49003 | -44.6212 | 2025-10-13 04:44:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 25.9 |
| 0b878fe5-081e-350b-a0dc-45281592e469 | -3.06433 | -49.40414 | 2025-10-13 04:44:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| f27a7f55-eddb-3942-a819-c04a5291bd05 | -6.42596 | -42.5487 | 2025-10-13 04:44:00 | NOAA-20 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| b1627983-f3ad-31b4-acab-a15bb306b2fd | -6.73339 | -42.08347 | 2025-10-13 04:44:00 | NOAA-20 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 05e6f08b-b722-3829-9b18-abac2c219aed | -2.87882 | -50.73097 | 2025-10-13 04:44:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 0a39c808-c1f5-3447-b2ee-5f4ba0d97c5a | -8.54074 | -44.59374 | 2025-10-13 04:44:00 | NOAA-20 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 7666fb3b-f3b4-3e2f-a11a-7b6d0d37ffde | -3.14404 | -50.45078 | 2025-10-13 04:44:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| deee5534-871d-3c8f-899d-ba4873401165 | -7.35045 | -44.08543 | 2025-10-13 04:44:00 | NOAA-20 | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 6dc719a1-328c-3928-9a5a-05ca9b3c4875 | -5.0472 | -49.88425 | 2025-10-13 04:44:00 | NOAA-20 | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| f20c74d2-416e-39e7-8914-682b49307311 | -4.87055 | -45.91066 | 2025-10-13 04:44:00 | NOAA-20 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 6d1e4215-0bb8-37b2-8b6d-01da5cd98c2c | -3.92311 | -50.01252 | 2025-10-13 04:44:00 | NOAA-20 | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 5ab3cef0-c94c-3331-904d-1ecaf8af0faf | -3.84962 | -50.97256 | 2025-10-13 04:44:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 6b35f94c-8604-3df7-86eb-d749859eee92 | -7.67269 | -43.986 | 2025-10-13 04:44:00 | NOAA-20 | BERTOLÍNIA | PIAUÍ | Brasil | 2201705 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 17fb3565-b206-3405-8bc7-7608b4cdfdda | -7.54 | -46.09187 | 2025-10-13 04:44:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 24267e5f-6451-3d03-b7bf-01eb8d21be8a | -7.54751 | -46.09662 | 2025-10-13 04:44:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 7.0 |
| aa30e0a1-3c4a-3030-a306-438362756753 | -10.81061 | -43.97742 | 2025-10-13 04:44:00 | NOAA-20 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 16.2 |
| b3aa35f5-6a7a-30e7-8cb3-217a66704320 | -8.23607 | -43.37358 | 2025-10-13 04:44:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 2.7 |
| cc067179-3f6e-34fa-b20c-05856c0b1289 | -8.32487 | -46.24197 | 2025-10-13 04:44:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| ff297d2d-4f48-3f59-b682-54a40d9a19cb | -8.21767 | -43.32615 | 2025-10-13 04:44:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| d2219f8a-ba6a-3ca6-bed5-7abb40330540 | -3.58314 | -51.23893 | 2025-10-13 04:44:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| daebbfc0-b357-335e-9143-0decd3f41d72 | -6.63596 | -44.66004 | 2025-10-13 04:44:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 2ad059c5-c5d8-38af-bb40-ab0196ce7644 | -4.50923 | -47.52607 | 2025-10-13 04:44:00 | NOAA-20 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 71453e2d-ba44-3449-baec-195433407f3c | -7.917 | -47.21738 | 2025-10-13 04:44:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 3693d39d-be91-3a9f-b3f6-e8fa7e4b660e | -3.14128 | -50.44682 | 2025-10-13 04:44:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| a039ab33-c502-3846-8a00-7613b98c0fb7 | -7.64084 | -42.57749 | 2025-10-13 04:44:00 | NOAA-20 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| ad12d4ba-7c41-3e39-9862-bcd0f0e41d8b | -3.814 | -45.76451 | 2025-10-13 04:44:00 | NOAA-20 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 6704f0ec-2dff-3e97-90e4-a64539ab2e9f | -3.23069 | -50.05217 | 2025-10-13 04:44:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 092c213d-127e-35e8-9c4a-5135c1071fc3 | -10.81478 | -43.98336 | 2025-10-13 04:44:00 | NOAA-20 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 32.8 |
| 016db0ff-84d8-33c4-b0bc-5dde6610c367 | -3.14459 | -50.44733 | 2025-10-13 04:44:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 3d7b32e0-263c-303b-8b80-f91179160051 | -4.83777 | -41.48041 | 2025-10-13 04:44:00 | NOAA-20 | JUAZEIRO DO PIAUÍ | PIAUÍ | Brasil | 2205516 | 22 | 33 | nan | nan | nan | Caatinga | 0.7 |
| a9b09f06-46c9-3f4c-8351-dc42d686458e | -7.49912 | -44.65269 | 2025-10-13 04:44:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 08dc266f-831e-3c5e-86a1-91dcdf3ecf22 | -6.57991 | -45.97634 | 2025-10-13 04:44:00 | NOAA-20 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| d57325c2-1522-3ce3-885d-30f8224d512a | -2.88159 | -50.73496 | 2025-10-13 04:44:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 53320669-0886-3be4-b66d-211473f7bc2e | -5.73779 | -40.76707 | 2025-10-13 04:44:00 | NOAA-20 | QUITERIANÓPOLIS | CEARÁ | Brasil | 2311264 | 23 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 249c760b-9a06-36a1-b03e-1f279a1c3d49 | -5.9411 | -44.21681 | 2025-10-13 04:44:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 8b51b280-e354-3ad0-b088-c0e65880fbd9 | -10.79874 | -43.95443 | 2025-10-13 04:44:00 | NOAA-20 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 7.9 |
| 34f2f2fd-a8b9-3954-a41f-a5b3f5744f22 | -4.30017 | -48.1031 | 2025-10-13 04:44:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 858f0e06-053b-3817-876b-a870dc8f4a08 | -5.22273 | -50.94893 | 2025-10-13 04:44:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 1eb55d19-5a02-3a33-b3c1-f9d19de6dc14 | -7.84038 | -44.52389 | 2025-10-13 04:44:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| d91eeac4-f447-326e-ad1f-de5d8cfb29b8 | -4.47914 | -44.93417 | 2025-10-13 04:44:00 | NOAA-20 | LAGO DO JUNCO | MARANHÃO | Brasil | 2105807 | 21 | 33 | nan | nan | nan | Amazônia | 7.4 |


[Clique aqui para ver as próximas entradas](README30.md)
