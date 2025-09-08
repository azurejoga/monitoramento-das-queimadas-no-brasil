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

## Dados Diários - Página 44

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 22ca92d6-8077-36c5-a50c-1ed40331a677 | -14.78205 | -48.14242 | 2025-09-08 04:02:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.6 |
| b384e8c9-6a7b-3b8e-835a-c775649af656 | -11.42357 | -43.65595 | 2025-09-08 04:02:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 3.4 |
| e1865396-2b53-348d-a740-c014907c3be8 | -11.39343 | -43.54993 | 2025-09-08 04:02:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 3280bfc2-1d17-3692-9e97-2fac6a346aaf | -14.51855 | -48.78955 | 2025-09-08 04:02:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| ceefb3e4-0404-3b19-947d-61e4344f0cfb | -12.94121 | -54.77247 | 2025-09-08 04:02:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 05b927ea-e0f5-3bcb-90c6-41c7595f66d5 | -9.71833 | -43.97925 | 2025-09-08 04:02:00 | NOAA-20 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 07846c3f-5b9e-32fb-9686-44463a6a2cc2 | -14.50898 | -48.81043 | 2025-09-08 04:02:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| fe692019-7d09-3de2-8a85-60213c4b84fb | -14.99629 | -48.00196 | 2025-09-08 04:02:00 | NOAA-20 | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 0e311718-b4ea-3ad5-b579-0e9b6a24df4e | -11.66631 | -46.88278 | 2025-09-08 04:02:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 5367139f-9c85-3229-b43b-7ef9121d538f | -14.50941 | -48.81276 | 2025-09-08 04:02:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 5.4 |
| b6783136-6831-33c9-bfc9-f56df4c5b0ae | -8.70109 | -45.30759 | 2025-09-08 04:02:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 5.0 |
| fbf748c5-a546-34b9-902d-51afbc913bc5 | -11.30691 | -46.52877 | 2025-09-08 04:02:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 7d902ceb-831f-3474-b062-53d5be1696de | -11.40667 | -50.3961 | 2025-09-08 04:02:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 5.2 |
| f0193b3e-294e-36b5-a849-0517de8f8dde | -14.601 | -48.08949 | 2025-09-08 04:02:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 2653c4d6-08a7-35e6-93dc-5f37c7d1a8e8 | -14.21644 | -53.35852 | 2025-09-08 04:02:00 | NOAA-20 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 51cc83ff-9b17-34d5-aea2-7aaa603a9957 | -12.03765 | -45.77903 | 2025-09-08 04:02:00 | NOAA-20 | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 26cdf471-70f3-3d83-a7cd-6d92d91b1107 | -11.32833 | -46.55201 | 2025-09-08 04:02:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| c935ab11-b376-3371-9da6-92406072c34f | -14.58908 | -48.08168 | 2025-09-08 04:02:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 40cc0260-2df4-34e1-ab8c-e71d512abd5f | -11.40935 | -50.37218 | 2025-09-08 04:02:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| ecbc3c20-e2d2-32d2-b3b7-38f588c7090d | -13.91667 | -48.01822 | 2025-09-08 04:02:00 | NOAA-20 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 15d369eb-8741-3824-9892-72e8c6902f20 | -8.19358 | -50.13594 | 2025-09-08 04:02:00 | NOAA-20 | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 411d3e5b-b0d7-37f8-b5cc-fb9932006d20 | -14.52679 | -48.76448 | 2025-09-08 04:02:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 00ee5159-192f-3841-a1a1-ed76f077d6f9 | -14.68526 | -48.19747 | 2025-09-08 04:02:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 5c490cd0-c654-3821-804a-89bc28bbe3b0 | -9.99293 | -51.66627 | 2025-09-08 04:02:00 | NOAA-20 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 4764ca79-0bec-3e5b-bf09-e30f9ea914e7 | -11.28252 | -46.4748 | 2025-09-08 04:02:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 49a00667-d7f7-3867-9ed0-cb0d7e4baae7 | -11.65729 | -46.8849 | 2025-09-08 04:02:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| cfa0ff54-4ed9-373b-b4f2-62f62a26acb4 | -8.50703 | -45.71411 | 2025-09-08 04:02:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 8f0d3f88-c778-39ea-8f21-eabffb6b4de1 | -9.7218 | -43.97719 | 2025-09-08 04:02:00 | NOAA-20 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 9d89160a-7486-3baf-9b3f-347c0d3c8447 | -11.40451 | -50.37817 | 2025-09-08 04:02:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| f342f834-53c7-3667-900e-896a981ae942 | -16.33839 | -45.05579 | 2025-09-08 04:02:00 | NOAA-20 | ICARAÍ DE MINAS | MINAS GERAIS | Brasil | 3130051 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| f7306c5f-0694-32b3-9283-f2717b888f69 | -9.96109 | -51.21065 | 2025-09-08 04:02:00 | NOAA-20 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 5.7 |
| b3e677fe-ff48-3f58-8907-52405537216b | -8.19677 | -47.56359 | 2025-09-08 04:02:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| fd3e528f-2c39-3261-a4d3-95c98df8e6ce | -14.50535 | -48.80472 | 2025-09-08 04:02:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| e5420a0c-48ac-3faa-9c6c-abab195f6d34 | -10.2872 | -48.8089 | 2025-09-08 04:02:00 | NOAA-20 | PARAÍSO DO TOCANTINS | TOCANTINS | Brasil | 1716109 | 17 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 45e55224-7b1e-35fd-b0c6-4edf7d43440c | -11.0306 | -45.93738 | 2025-09-08 04:02:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| fd70b42a-0911-3fcd-bb0f-0b3e69e6d2c1 | -12.93853 | -54.78507 | 2025-09-08 04:02:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 6a351d00-1dab-3aaf-96b1-42df0924aaf8 | -14.99233 | -48.01703 | 2025-09-08 04:02:00 | NOAA-20 | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| f2b70dd2-29e5-3f1a-9cad-be5667823a13 | -12.00016 | -47.77147 | 2025-09-08 04:02:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 10.9 |
| 7c77b5b7-8fb9-39a4-8302-ce17617e525b | -10.81408 | -47.74571 | 2025-09-08 04:02:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 3618de7a-d414-3106-a13c-2fb09d2ccc70 | -11.56861 | -44.65706 | 2025-09-08 04:02:00 | NOAA-20 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| caebeca1-062c-39c5-833a-f166e2041eba | -11.42623 | -43.64009 | 2025-09-08 04:02:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 057467cf-83cc-33be-bf8d-24bdcff16588 | -10.13756 | -46.18815 | 2025-09-08 04:02:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 3009f498-b79a-3e2d-8e50-e38e49c50e73 | -13.73715 | -46.90261 | 2025-09-08 04:02:00 | NOAA-20 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| cb225a69-527d-3a71-af1c-8d8c966c96a7 | -9.71689 | -43.98771 | 2025-09-08 04:02:00 | NOAA-20 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 94cd346d-5e5c-3c82-abc4-926901e8717a | -11.42273 | -43.6395 | 2025-09-08 04:02:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 4.4 |
| d04fb84f-1037-377f-a9cf-6f21a3694692 | -14.28114 | -44.99091 | 2025-09-08 04:02:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| e6d6e4f9-4286-3fe6-87ac-0156278a7ba9 | -8.19411 | -50.1364 | 2025-09-08 04:02:00 | NOAA-20 | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 3e693145-5c2b-331f-a882-e57db66df35b | -11.61943 | -47.14623 | 2025-09-08 04:02:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 7a6a78d5-56c3-3c16-bd07-26720efaf5d4 | -9.33366 | -46.53551 | 2025-09-08 04:02:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 315e8528-31f4-331c-8124-dc248630dce4 | -13.70851 | -46.87588 | 2025-09-08 04:02:00 | NOAA-20 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| c1b25d55-4876-30a7-bd39-db2bd1267d9e | -11.83355 | -46.77025 | 2025-09-08 04:02:00 | NOAA-20 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 90d86165-2e01-396f-99cd-c735ebbddd95 | -13.67119 | -44.22264 | 2025-09-08 04:02:00 | NOAA-20 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 68644a91-0eb4-32a2-9544-c325158bc2e1 | -9.4414 | -49.44699 | 2025-09-08 04:02:00 | NOAA-20 | ABREULÂNDIA | TOCANTINS | Brasil | 1700251 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 1ed12ea2-ad4b-3e8d-a998-d724e147f70c | -13.74381 | -46.91227 | 2025-09-08 04:02:00 | NOAA-20 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| bd04c712-19e5-3f80-abcb-b4816165a1bd | -14.51795 | -48.78713 | 2025-09-08 04:02:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 6da3aac5-f466-3c01-9be1-7c61118430cc | -10.79626 | -47.74157 | 2025-09-08 04:02:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| d7229639-93f9-3fde-a02b-694080b3bc5d | -11.90804 | -50.99855 | 2025-09-08 04:02:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 6a1d5c3f-f272-39f3-925f-504e8bda575e | -9.79635 | -46.22601 | 2025-09-08 04:02:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 0475504b-b123-3e29-90fd-a3d0256373da | -14.99835 | -48.01492 | 2025-09-08 04:02:00 | NOAA-20 | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| ff904b12-76bd-3657-8223-10d7754e6922 | -16.08424 | -43.63672 | 2025-09-08 04:02:00 | NOAA-20 | CAPITÃO ENÉAS | MINAS GERAIS | Brasil | 3112703 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| a91db84a-b71c-3716-95ff-ae9c9e37ac18 | -7.74056 | -50.31205 | 2025-09-08 04:02:00 | NOAA-20 | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 4e6465c3-9fd6-3f5f-9c89-cfcd8d6484de | -11.28134 | -46.50539 | 2025-09-08 04:02:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 377f4818-ca5b-361e-a289-7efc2150da02 | -15.0878 | -48.13479 | 2025-09-08 04:02:00 | NOAA-20 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 768133d3-fbc9-3563-8ba6-e78848af3bcc | -14.42809 | -48.45971 | 2025-09-08 04:02:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 50d33339-5aa5-3fec-9943-b951c3ce2623 | -15.29182 | -44.76608 | 2025-09-08 04:02:00 | NOAA-20 | BONITO DE MINAS | MINAS GERAIS | Brasil | 3108255 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 37c6ec5e-d456-38f0-957d-fe2a49fbf192 | -15.54489 | -48.37603 | 2025-09-08 04:02:00 | NOAA-20 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 87a29191-012e-356f-8ad3-0bedb3f67b35 | -15.38266 | -46.4278 | 2025-09-08 04:02:00 | NOAA-20 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 1c93c933-7d88-3424-92fa-3298edaefe29 | -14.51256 | -48.79102 | 2025-09-08 04:02:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 2213caa1-12e3-3797-8f09-28c8a4441fe8 | -11.31979 | -47.33179 | 2025-09-08 04:02:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 7588928d-7691-3857-99ce-09cb2a6820ed | -14.51165 | -48.79591 | 2025-09-08 04:02:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 25d14bbe-9d2d-3e4f-9f71-5370cbb52b9c | -12.19532 | -53.90348 | 2025-09-08 04:02:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| a43602bf-791b-3c0b-bc12-e566edc45297 | -14.50357 | -48.81435 | 2025-09-08 04:02:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| e4d2a9c7-8333-3b87-94d6-d0e0ca93c8b0 | -13.12918 | -42.30263 | 2025-09-08 04:02:00 | NOAA-20 | RIO DO PIRES | BAHIA | Brasil | 2926905 | 29 | 33 | nan | nan | nan | Caatinga | 0.4 |
| 2bfffc9c-fb13-35da-8c37-717578170857 | -8.19464 | -50.13346 | 2025-09-08 04:02:00 | NOAA-20 | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| efa82b9c-908b-3253-8596-b64bee192e7b | -11.22507 | -55.01126 | 2025-09-08 04:02:00 | NOAA-20 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 2d882577-0ee1-338d-9282-46b6d377f878 | -9.44198 | -49.44387 | 2025-09-08 04:02:00 | NOAA-20 | ABREULÂNDIA | TOCANTINS | Brasil | 1700251 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| c9f0c74b-0540-3ecb-a186-9b31b8f6f72e | -11.61516 | -47.14548 | 2025-09-08 04:02:00 | NOAA-20 | PORTO ALEGRE DO TOCANTINS | TOCANTINS | Brasil | 1718006 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| cf7a0c7e-56ff-3f26-a5e2-bff35d5a79b4 | -14.51406 | -48.78858 | 2025-09-08 04:02:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 4ecaf9b9-a757-3012-b92c-16236ff9d15d | -10.22375 | -45.3671 | 2025-09-08 04:02:00 | NOAA-20 | SÃO GONÇALO DO GURGUÉIA | PIAUÍ | Brasil | 2209757 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| f7df950b-9302-33b6-99c7-d8028a8f5b62 | -11.21813 | -55.00941 | 2025-09-08 04:02:00 | NOAA-20 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 2b5dbfdb-4445-3d38-83fe-5bd9ac6a9e6f | -9.803 | -46.0249 | 2025-09-08 04:02:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 39c44db3-49d0-3574-ae30-53822e89bba0 | -10.08339 | -48.09976 | 2025-09-08 04:02:00 | NOAA-20 | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 8772e1b5-fb65-33fa-b9e9-e2c057bbac38 | -10.47225 | -47.73175 | 2025-09-08 04:02:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 9b6e9c3a-8821-3976-981f-0069533fec0c | -11.39627 | -43.55445 | 2025-09-08 04:02:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| a552e076-4837-37dc-ace4-24d32972cfde | -15.52801 | -48.18092 | 2025-09-08 04:02:00 | NOAA-20 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 6cf0b625-4897-31a0-8662-7b61af1b260d | -11.42423 | -43.65199 | 2025-09-08 04:02:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 87a11509-b362-3697-949a-26e1a9a10498 | -9.19932 | -46.03421 | 2025-09-08 04:02:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 478d652d-ae5f-339d-a97f-df6a6e04de48 | -9.81599 | -53.3187 | 2025-09-08 04:02:00 | NOAA-20 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 4.3 |
| b59665be-9a4e-374b-a9db-c317484c4589 | -12.19294 | -53.91925 | 2025-09-08 04:02:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| cbcd6560-b0ac-3f3d-a940-9f05b18cb3d4 | -13.74116 | -46.90363 | 2025-09-08 04:02:00 | NOAA-20 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| d0ce0dc6-8997-3c79-9eea-bef2816a52e9 | -11.89534 | -46.64963 | 2025-09-08 04:02:00 | NOAA-20 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 379cfd9c-9879-314f-9eb3-73f34b72be77 | -10.28898 | -48.81246 | 2025-09-08 04:02:00 | NOAA-20 | PARAÍSO DO TOCANTINS | TOCANTINS | Brasil | 1716109 | 17 | 33 | nan | nan | nan | Cerrado | 5.6 |
| d715f620-2705-39ba-91ac-63e80b71a4a9 | -14.47372 | -48.79853 | 2025-09-08 04:02:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 9592a1ff-8ece-378f-bd9c-71e6e55a9507 | -11.93368 | -44.87497 | 2025-09-08 04:02:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 3e323784-45c1-3824-b8f3-c246ce9f64e1 | -9.71124 | -43.50772 | 2025-09-08 04:02:00 | NOAA-20 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 40276060-8498-323b-8b07-df000c213c36 | -12.86775 | -47.9804 | 2025-09-08 04:02:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 3c6b4c64-4891-3b80-8dde-570e34daf716 | -10.28407 | -48.81175 | 2025-09-08 04:02:00 | NOAA-20 | PARAÍSO DO TOCANTINS | TOCANTINS | Brasil | 1716109 | 17 | 33 | nan | nan | nan | Cerrado | 5.6 |
| cbfe022f-d787-3886-b450-2918d0dd39ed | -15.01658 | -48.00517 | 2025-09-08 04:02:00 | NOAA-20 | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| f110f9a8-1151-3fe3-87cf-8fdec56c236b | -11.27911 | -46.47018 | 2025-09-08 04:02:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 4.6 |
| bff81053-fd74-316a-be69-05b31fa308a0 | -12.94119 | -54.80569 | 2025-09-08 04:02:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | 5.3 |


[Clique aqui para ver as próximas entradas](README45.md)
