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
| cdabf961-7577-3c0a-807a-ccde4454ed7f | -6.66544 | -45.91587 | 2025-09-03 03:53:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 9b4d60e4-a03d-376c-a8ef-d10424aafea5 | -8.06879 | -45.38346 | 2025-09-03 03:53:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 3.1 |
| a1fe462b-3065-3864-8c32-fbc7a065b533 | -7.71409 | -48.74818 | 2025-09-03 03:53:00 | NOAA-20 | BANDEIRANTES DO TOCANTINS | TOCANTINS | Brasil | 1703057 | 17 | 33 | nan | nan | nan | Amazônia | 2.8 |
| e0e628ae-33ba-3e0e-ab0c-99b52bbdd411 | -7.70439 | -48.73761 | 2025-09-03 03:53:00 | NOAA-20 | BANDEIRANTES DO TOCANTINS | TOCANTINS | Brasil | 1703057 | 17 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 3dd1f658-0bac-33a1-89e9-8e8897acb58a | -6.97194 | -44.35446 | 2025-09-03 03:53:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| c9aac502-1db6-385d-97d1-e8012c41f584 | -6.86319 | -45.54145 | 2025-09-03 03:53:00 | NOAA-20 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| fb7f8b1d-68e6-3440-95d1-21b8854e9582 | -8.44106 | -47.34711 | 2025-09-03 03:53:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 225e9b84-fff0-3959-a747-6167ca527ec6 | -9.17837 | -45.21881 | 2025-09-03 03:53:00 | NOAA-20 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 2.9 |
| f072469f-4623-32f2-8464-ce7fbd480835 | -6.41302 | -43.76006 | 2025-09-03 03:53:00 | NOAA-20 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 22dc5a7c-5f49-32f2-9c94-3bef6fd0067b | -6.3214 | -42.54778 | 2025-09-03 03:53:00 | NOAA-20 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 2c77acda-8a9e-32a8-ad2d-e9a74d38127b | -5.88801 | -43.00648 | 2025-09-03 03:53:00 | NOAA-20 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 3.8 |
| af9a6e65-56b0-3c1f-8e9e-002d66deb26c | -8.37263 | -48.30785 | 2025-09-03 03:53:00 | NOAA-20 | PRESIDENTE KENNEDY | TOCANTINS | Brasil | 1718402 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 1d43c820-56ea-34d0-9fa6-d99e03396fbe | -7.50197 | -45.35554 | 2025-09-03 03:53:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 8b34cbd9-4563-3283-98a8-cc075cd3ce9f | -7.47884 | -45.6568 | 2025-09-03 03:53:00 | NOAA-20 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| a172aad0-bbf6-3a20-8d71-b4f5ecc1f833 | -6.69718 | -44.18447 | 2025-09-03 03:53:00 | NOAA-20 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 1b02b5d2-66e6-3128-a487-034306a05e34 | -6.87659 | -43.8354 | 2025-09-03 03:53:00 | NOAA-20 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 6102219d-cc69-3930-85b6-817e22b00a5d | -7.79444 | -45.43753 | 2025-09-03 03:53:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 4999799d-e425-3ed4-abca-00e685ea0511 | -8.36117 | -48.30943 | 2025-09-03 03:53:00 | NOAA-20 | PRESIDENTE KENNEDY | TOCANTINS | Brasil | 1718402 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 73e75c81-6711-30bc-b6f3-2c2601ba46f9 | -7.13357 | -44.57535 | 2025-09-03 03:53:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 690c34da-d2e3-3f0a-a53e-d75b9d5db3e0 | -7.55802 | -45.72007 | 2025-09-03 03:53:00 | NOAA-20 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 0b7216fb-b337-3954-b9bc-e8ad0d397732 | -6.25765 | -42.60041 | 2025-09-03 03:53:00 | NOAA-20 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 4b71e176-23df-36d0-9f68-1fb49236fa51 | -7.00494 | -43.22713 | 2025-09-03 03:53:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| f4a27ae2-7e85-3846-bed0-25e217ec25f8 | -5.94018 | -43.02837 | 2025-09-03 03:53:00 | NOAA-20 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 3bd4f6c2-7806-3020-9ba1-d85d8ccb3c6a | -6.19639 | -43.3582 | 2025-09-03 03:53:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 47c79ffc-76a3-3a27-a175-e333579c7a77 | -5.89518 | -46.16249 | 2025-09-03 03:53:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 14c6fd34-bba9-3f11-9e67-2c21f83d0736 | -6.89227 | -44.23651 | 2025-09-03 03:53:00 | NOAA-20 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 0dbc27fb-7fd1-3fe9-96fa-2504d7a25e23 | -6.9319 | -45.55584 | 2025-09-03 03:53:00 | NOAA-20 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| bb355d46-f7c2-31c1-b47c-d3c988c40e62 | -6.97795 | -43.10162 | 2025-09-03 03:53:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 9195d8c1-2ed6-3fd5-a0d5-1400d133fb42 | -8.08256 | -47.60391 | 2025-09-03 03:53:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 09961f1f-ce03-38ac-96a9-c2ee8a3ae87c | -6.54342 | -44.56079 | 2025-09-03 03:53:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 893f0a90-79ab-398e-b4cd-dafbe7f8f0cb | -7.93119 | -46.54621 | 2025-09-03 03:53:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 7.7 |
| 652b5fca-4353-364d-bb11-614c8b1a4c63 | -7.48248 | -44.80927 | 2025-09-03 03:53:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 8.1 |
| 379429ba-f777-31a4-97b9-aa6aa9127aab | -7.49747 | -45.339 | 2025-09-03 03:53:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 2dcdc104-e520-3516-add3-d386d66f8717 | -6.26518 | -42.62614 | 2025-09-03 03:53:00 | NOAA-20 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| e666a9af-9f62-3ecd-8f8b-b710a4c892b8 | -7.69948 | -48.73267 | 2025-09-03 03:53:00 | NOAA-20 | BANDEIRANTES DO TOCANTINS | TOCANTINS | Brasil | 1703057 | 17 | 33 | nan | nan | nan | Amazônia | 12.8 |
| bfc6dc8e-89a5-3964-b1eb-908ac66439ce | -6.91335 | -44.36482 | 2025-09-03 03:53:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| dd258602-6aca-39c1-a3cd-16fb5b8eebe2 | -6.62283 | -43.9546 | 2025-09-03 03:53:00 | NOAA-20 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 9f73a2ba-1944-3489-b6c1-ffab5aa83c4f | -6.79567 | -44.08922 | 2025-09-03 03:53:00 | NOAA-20 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 40f7d049-bb4a-33e2-9988-2905cb5ac971 | -8.88947 | -45.80758 | 2025-09-03 03:53:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 8a563579-90c0-31bf-bb17-9e6d6b10411d | -7.49901 | -45.34567 | 2025-09-03 03:53:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 2c5f5c09-b4e0-3497-8349-9158ca4bc8fb | -7.63093 | -46.54797 | 2025-09-03 03:53:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| e0fd1f4c-acd4-345d-a6a5-ecf11056a0b4 | -8.02051 | -44.08009 | 2025-09-03 03:53:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 3343a688-ca70-31f7-9797-1b262277560c | -7.28958 | -45.28787 | 2025-09-03 03:53:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 3a888d58-b958-3376-840c-435eb99d35cb | -5.99464 | -43.82035 | 2025-09-03 03:53:00 | NOAA-20 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 5.5 |
| a25113dc-ad9b-3a36-b818-37f38579cc08 | -7.90464 | -46.45095 | 2025-09-03 03:53:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 0983888c-38b4-3b96-9242-af28063c8ece | -8.43149 | -47.34205 | 2025-09-03 03:53:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 7dc2ca6d-5142-36cf-9763-db3c48d97a7a | -8.18968 | -42.29986 | 2025-09-03 03:53:00 | NOAA-20 | SÃO JOÃO DO PIAUÍ | PIAUÍ | Brasil | 2210003 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 089a057f-6079-3e29-b0bc-c08e476857f2 | -6.92688 | -44.26184 | 2025-09-03 03:53:00 | NOAA-20 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 98e1ff85-29bf-358d-b354-f974f7e18ee0 | -6.07833 | -46.82302 | 2025-09-03 03:53:00 | NOAA-20 | LAJEADO NOVO | MARANHÃO | Brasil | 2105989 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 3a2269a8-cbda-39ad-b11e-5375fd054f71 | -6.59784 | -44.10394 | 2025-09-03 03:53:00 | NOAA-20 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 69a5c9fd-be16-3c67-b33f-eb436665d069 | -5.8964 | -43.35857 | 2025-09-03 03:53:00 | NOAA-20 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 5.6 |
| d7d42a63-873f-38c9-b857-8ddf6cc76064 | -7.6154 | -42.65003 | 2025-09-03 03:53:00 | NOAA-20 | RIBEIRA DO PIAUÍ | PIAUÍ | Brasil | 2208874 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 13634f7d-c388-362a-b0b6-76eba623e88c | -9.19657 | -45.19156 | 2025-09-03 03:53:00 | NOAA-20 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| b89b54fd-06dd-33cf-a996-0bd916afd357 | -9.16252 | -45.20741 | 2025-09-03 03:53:00 | NOAA-20 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 37a6fe9b-b5ad-3e81-8376-57c6dd5f9196 | -7.47949 | -44.82624 | 2025-09-03 03:53:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| b8284ee3-3c19-3d87-8ea3-3a27d16f1d3c | -5.89417 | -43.34726 | 2025-09-03 03:53:00 | NOAA-20 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 5d4e59b2-e819-3b89-8692-e700a7691507 | -5.60595 | -45.01898 | 2025-09-03 03:53:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 2d966197-0ef4-3ede-8e8e-5183c9b76a90 | -7.80132 | -45.45989 | 2025-09-03 03:53:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 2.7 |
| e08e7ead-1c28-3374-a292-24319a320720 | -7.71834 | -48.72481 | 2025-09-03 03:53:00 | NOAA-20 | BANDEIRANTES DO TOCANTINS | TOCANTINS | Brasil | 1703057 | 17 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 930601cb-5863-3055-999f-677377095bc1 | -7.11149 | -44.75592 | 2025-09-03 03:53:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 6.8 |
| d0a11d07-83c5-319e-b980-cea784a9c2f1 | -8.05065 | -45.36744 | 2025-09-03 03:53:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 7.8 |
| 85af6a4a-0e41-3530-a742-9afafe336529 | -8.05349 | -45.36585 | 2025-09-03 03:53:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 789d3d51-060b-3b60-a2d3-113a30eb2aa4 | -7.38034 | -43.00677 | 2025-09-03 03:53:00 | NOAA-20 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| baaaea42-415c-3cb4-8822-fccd95572140 | -6.45179 | -44.67871 | 2025-09-03 03:53:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 016e7cd4-5a5a-3691-8e71-aa32eb74eaa0 | -6.12249 | -44.11913 | 2025-09-03 03:53:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 3ab750e6-c361-3d82-b7d8-8830ab857e77 | -8.02273 | -44.09195 | 2025-09-03 03:53:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 0bddc3e0-63e9-30d3-bafe-adc10236422a | -6.45112 | -42.39446 | 2025-09-03 03:53:00 | NOAA-20 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 0bb730d5-252e-3a0f-9439-40c5ff5439be | -5.88214 | -43.2398 | 2025-09-03 03:53:00 | NOAA-20 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 3caaa20b-fad5-3d6f-bf2e-f3d199b54875 | -7.71516 | -50.25097 | 2025-09-03 03:53:00 | NOAA-20 | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 8.5 |
| e1d8c2b9-dfd2-31e1-991c-ea829e70f314 | -8.55003 | -47.47617 | 2025-09-03 03:53:00 | NOAA-20 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 7b69bdc8-c6cf-39cb-a9b3-54d216ba71dd | -8.87097 | -45.83289 | 2025-09-03 03:53:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 0b69f841-1d08-3552-b781-4599f10d01ca | -6.87366 | -45.56333 | 2025-09-03 03:53:00 | NOAA-20 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| c25fac59-c4e8-3b55-b4be-99e0cada5af6 | -6.50291 | -43.57368 | 2025-09-03 03:53:00 | NOAA-20 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 8e0bad1a-d506-33b0-912c-5468c4b42045 | -5.61202 | -45.01049 | 2025-09-03 03:53:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 05696195-d7d6-3f45-8561-6dacca9e2eab | -8.06958 | -45.37893 | 2025-09-03 03:53:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 3.1 |
| e1494a91-1ca3-39e9-9d6c-d472adbade44 | -6.46608 | -45.41535 | 2025-09-03 03:53:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 8c94879b-fdb7-3f13-8276-3e1d962732a1 | -6.69904 | -44.17339 | 2025-09-03 03:53:00 | NOAA-20 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 45e1ac57-8351-3ea6-87e1-ca480b523c8e | -7.49978 | -45.34111 | 2025-09-03 03:53:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 89f344db-fb10-3226-b45f-f3b8f68d885e | -5.6117 | -45.01811 | 2025-09-03 03:53:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 4.3 |
| e46bc4e4-0040-3986-aec4-f5cafc451563 | -9.17913 | -45.21453 | 2025-09-03 03:53:00 | NOAA-20 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 2050e204-d8ee-3c82-86e9-6af79edf2306 | -7.00763 | -43.42771 | 2025-09-03 03:53:00 | NOAA-20 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| f00472ee-253c-35cf-981a-22005b43818f | -6.30769 | -43.29047 | 2025-09-03 03:53:00 | NOAA-20 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 641eb4c8-05c5-3f3b-943e-c6666031af5e | -6.09543 | -43.28708 | 2025-09-03 03:53:00 | NOAA-20 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 107163ec-9a61-3fe7-baee-cde86d971827 | -6.2818 | -43.59927 | 2025-09-03 03:53:00 | NOAA-20 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 04f0a8f2-26f9-3dea-a49c-45e8d84cfa46 | -6.34793 | -42.56885 | 2025-09-03 03:53:00 | NOAA-20 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| f11b5def-637b-38fe-a379-0d10e677f894 | -7.98859 | -44.04482 | 2025-09-03 03:53:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 0c241717-660d-3236-a0bc-4fd2b993a37f | -5.43483 | -45.97653 | 2025-09-03 03:53:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 59b1d426-f51d-3e1c-9852-477f19a14400 | -6.22652 | -43.38104 | 2025-09-03 03:53:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 73fbaa09-a5bc-326e-a10a-903cb4e66cd6 | -6.77993 | -44.48319 | 2025-09-03 03:53:00 | NOAA-20 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| f3b9e2b3-175f-31ee-acd2-f609965a7d53 | -5.9408 | -43.03135 | 2025-09-03 03:53:00 | NOAA-20 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 1b5d779b-a806-35c9-8acb-3472a779d300 | -7.8005 | -45.46447 | 2025-09-03 03:53:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 3.8 |
| bba734f1-866a-3d96-af32-2da3da252e14 | -6.30502 | -43.55867 | 2025-09-03 03:53:00 | NOAA-20 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 78f3accf-873a-3148-85cc-560f048b32b5 | -7.69233 | -48.73998 | 2025-09-03 03:53:00 | NOAA-20 | BANDEIRANTES DO TOCANTINS | TOCANTINS | Brasil | 1703057 | 17 | 33 | nan | nan | nan | Amazônia | 11.0 |
| 5cdd3428-f3cc-35a3-9f01-5522b5424178 | -6.1 | -43.28431 | 2025-09-03 03:53:00 | NOAA-20 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Caatinga | 1.1 |
| dff28e6a-a994-3bcc-8991-0a43240c9ff6 | -6.27215 | -43.30628 | 2025-09-03 03:53:00 | NOAA-20 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 0af08aca-9774-3f44-a8bd-6cb391274e5a | -8.83544 | -45.76999 | 2025-09-03 03:53:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| a4fead18-8805-3ec4-aa70-70686b6fc411 | -5.80072 | -43.23334 | 2025-09-03 03:53:00 | NOAA-20 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 033e5da0-de11-3c68-b1c0-970e3f533663 | -6.24676 | -42.6183 | 2025-09-03 03:53:00 | NOAA-20 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 4.0 |
| 31ae0d06-1e54-3987-9034-011fcef3ce9e | -6.4992 | -44.07181 | 2025-09-03 03:53:00 | NOAA-20 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 4191635b-2d01-37ea-9723-db3d30c60bde | -6.09829 | -43.29475 | 2025-09-03 03:53:00 | NOAA-20 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Caatinga | 2.5 |


[Clique aqui para ver as próximas entradas](README32.md)
