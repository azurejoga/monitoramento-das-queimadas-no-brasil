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

## Dados Diários - Página 23

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 26b0ce14-83f2-3ff6-ab56-49c66635ff73 | -12.65005 | -54.11914 | 2025-06-20 04:53:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| ae7fbb57-b081-364e-b7ff-5893015dce2f | -11.98485 | -51.60903 | 2025-06-20 04:53:00 | NOAA-21 | BOM JESUS DO ARAGUAIA | MATO GROSSO | Brasil | 5101852 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| d1a6d342-9c42-3e82-a3cd-d218ebe65b69 | -13.14382 | -56.80625 | 2025-06-20 04:53:00 | NOAA-21 | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 1bfb3c14-4a24-36c2-ab5f-7720b5601fb4 | -11.92062 | -54.81595 | 2025-06-20 04:53:00 | NOAA-21 | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| bba4d281-cf26-36ff-8816-65687852dc65 | -11.93874 | -48.42428 | 2025-06-20 04:53:00 | NOAA-21 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| ba5ffa1e-af7c-39d0-88b8-52a90040d5cf | -15.40393 | -47.8125 | 2025-06-20 04:53:00 | NOAA-21 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| fb30528e-94d7-3bab-95c7-7644e78af64c | -13.77641 | -54.20192 | 2025-06-20 04:53:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 6170a565-4ffb-368a-a72a-53d0757bd5dd | -11.87455 | -54.6776 | 2025-06-20 04:53:00 | NOAA-21 | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 7be34226-f4bc-3751-8b1e-9a28d8075d61 | -13.7808 | -54.1954 | 2025-06-20 04:53:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 11.2 |
| f543476c-5b4e-3d1b-80ba-36e0532aacd2 | -12.6539 | -54.11616 | 2025-06-20 04:53:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| aa541ed0-c098-3198-a75b-4608b1bdb0df | -12.14409 | -54.30671 | 2025-06-20 04:53:00 | NOAA-21 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a8a1fde4-d6c8-38ae-9bf8-1413ff163273 | -14.03435 | -53.36601 | 2025-06-20 04:53:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| d55f9ce1-6d60-355f-97e0-f95300890d1e | -14.02817 | -55.13266 | 2025-06-20 04:53:00 | NOAA-21 | SANTA RITA DO TRIVELATO | MATO GROSSO | Brasil | 5107768 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 2dc9cb0c-7019-357a-ba4c-19d3ed0d788f | -22.3165 | -53.58921 | 2025-06-20 04:55:00 | NOAA-21 | IVINHEMA | MATO GROSSO DO SUL | Brasil | 5004700 | 50 | 33 | nan | nan | nan | Mata Atlântica | 14.4 |
| 1e54b16a-0a7f-3343-86d9-5108b68b3363 | -18.41623 | -51.98825 | 2025-06-20 04:55:00 | NOAA-21 | SERRANÓPOLIS | GOIÁS | Brasil | 5220504 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 9d4cb872-3f90-34cc-b290-c3c66bd67230 | -21.21211 | -48.6358 | 2025-06-20 04:55:00 | NOAA-21 | MONTE ALTO | SÃO PAULO | Brasil | 3531308 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| b8d43525-3b1e-3615-b3c1-324e8892d4ae | -18.65711 | -55.7504 | 2025-06-20 04:55:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.0 |
| a620ab89-ef1e-3f5e-8580-879da9f8f81e | -20.38148 | -55.03946 | 2025-06-20 04:55:00 | NOAA-21 | TERENOS | MATO GROSSO DO SUL | Brasil | 5008008 | 50 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 648dbaba-419f-3893-9258-1ae15986a50d | -20.31192 | -45.58312 | 2025-06-20 04:55:00 | NOAA-21 | ARCOS | MINAS GERAIS | Brasil | 3104205 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| b54a9349-bb90-3041-9d56-5928a4ff7bfb | -24.2418 | -50.74047 | 2025-06-20 04:55:00 | NOAA-21 | ORTIGUEIRA | PARANÁ | Brasil | 4117305 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 1dc975ec-e737-379a-beed-a8b1191a5c22 | -22.19797 | -41.64299 | 2025-06-20 04:55:00 | NOAA-21 | CARAPEBUS | RIO DE JANEIRO | Brasil | 3300936 | 33 | 33 | nan | nan | nan | Mata Atlântica | 3.0 |
| f8b698ad-c26e-3969-a244-f7102a736f52 | -18.99219 | -52.08755 | 2025-06-20 04:55:00 | NOAA-21 | CASSILÂNDIA | MATO GROSSO DO SUL | Brasil | 5002902 | 50 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 20e280d1-1d2b-33bb-9bb6-50a67e296ff7 | -18.65985 | -55.7546 | 2025-06-20 04:55:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.1 |
| d64547f6-61e4-3766-ab00-ec41abcf9061 | -18.99584 | -52.08812 | 2025-06-20 04:55:00 | NOAA-21 | CASSILÂNDIA | MATO GROSSO DO SUL | Brasil | 5002902 | 50 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 24e56823-6c10-31d8-9add-936646e76cae | -21.20688 | -48.64048 | 2025-06-20 04:55:00 | NOAA-21 | VISTA ALEGRE DO ALTO | SÃO PAULO | Brasil | 3556909 | 35 | 33 | nan | nan | nan | Mata Atlântica | 4.1 |
| fb73237d-f47b-34ec-9260-826a7e314334 | -21.20745 | -48.63526 | 2025-06-20 04:55:00 | NOAA-21 | MONTE ALTO | SÃO PAULO | Brasil | 3531308 | 35 | 33 | nan | nan | nan | Mata Atlântica | 7.1 |
| 2b9de22a-74ad-3a3e-9c10-4b6b8522c0e4 | -18.65438 | -55.74621 | 2025-06-20 04:55:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.1 |
| 5a4b1d80-1683-3e47-a256-81a32d745c30 | -22.54033 | -48.81403 | 2025-06-20 04:55:00 | NOAA-21 | MACATUBA | SÃO PAULO | Brasil | 3528007 | 35 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 1ebe324a-1eae-3ce6-be34-1cfb099c4cae | -18.95537 | -54.33605 | 2025-06-20 04:55:00 | NOAA-21 | SÃO GABRIEL DO OESTE | MATO GROSSO DO SUL | Brasil | 5007695 | 50 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 3063b5e3-08ac-3032-b735-ba41721ca20e | -18.99645 | -52.08368 | 2025-06-20 04:55:00 | NOAA-21 | CASSILÂNDIA | MATO GROSSO DO SUL | Brasil | 5002902 | 50 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 97deaee4-dfc2-386f-bbf4-773609abbdb8 | -20.37815 | -55.03889 | 2025-06-20 04:55:00 | NOAA-21 | TERENOS | MATO GROSSO DO SUL | Brasil | 5008008 | 50 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 4ab1eaba-c632-3211-aa36-b7b23ff8e66a | -19.6396 | -45.1946 | 2025-06-20 04:55:00 | NOAA-21 | BOM DESPACHO | MINAS GERAIS | Brasil | 3107406 | 31 | 33 | nan | nan | nan | Cerrado | 3.8 |
| d1d81dc9-ff86-30f0-b8f4-e1be7540624d | -19.5435 | -49.66485 | 2025-06-20 04:55:00 | NOAA-21 | CAMPINA VERDE | MINAS GERAIS | Brasil | 3111101 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 9d67cc7e-d4b8-3055-a4f3-249d134feee8 | -19.33606 | -54.17663 | 2025-06-20 04:55:00 | NOAA-21 | CAMAPUÃ | MATO GROSSO DO SUL | Brasil | 5002605 | 50 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 4dcb4312-6d36-33db-8f95-c6b6074b707b | -19.86182 | -54.38563 | 2025-06-20 04:55:00 | NOAA-21 | BANDEIRANTES | MATO GROSSO DO SUL | Brasil | 5001508 | 50 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 74e5455b-4466-3c2c-b6ac-887307e770e4 | -11.952 | -58.7376 | 2025-06-20 05:00:00 | GOES-19 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 52.2 |
| dc05700a-26c8-3e7e-861b-a569e36667ad | -10.475 | -47.0548 | 2025-06-20 05:00:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 99.0 |
| 848857ff-38b2-3d4d-9aff-dec8bc42f4e9 | -10.456 | -47.0571 | 2025-06-20 05:00:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 149.9 |
| 895e612f-e97d-3f2a-b2b8-ba09dcac8d11 | -10.4754 | -47.0325 | 2025-06-20 05:00:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 147.4 |
| de3bef76-b9c4-3fe7-ba9e-7122268f33fe | -10.4564 | -47.0347 | 2025-06-20 05:00:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 65.0 |
| cec8d05e-b5d0-398a-bb8c-281acfa54b66 | -16.3047 | -58.2676 | 2025-06-20 05:00:00 | GOES-19 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 56.5 |
| 105f8616-0256-3789-b1c3-25db071d7d62 | -10.4564 | -47.0347 | 2025-06-20 05:10:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 57.3 |
| b5dcece7-4b3d-3997-8a07-e4593b61cedb | -10.475 | -47.0548 | 2025-06-20 05:10:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 68.4 |
| 529315b2-bd85-33fe-9399-c29dd0b5095d | -10.4754 | -47.0325 | 2025-06-20 05:10:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 119.8 |
| 7f50ce98-2322-3dfa-87b4-2cfdb9007360 | -16.3047 | -58.2676 | 2025-06-20 05:10:00 | GOES-19 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 62.8 |
| 14cb516c-706b-36f1-b5ca-81653d058d29 | -3.04227 | -49.42777 | 2025-06-20 05:18:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 1b5a572f-c5f0-38a3-8e26-ae841bfdcc6a | -3.03151 | -49.42643 | 2025-06-20 05:18:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 289b9b8f-497f-3e2e-8220-7ecfaea3984e | -2.91389 | -48.23359 | 2025-06-20 05:18:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 106fd958-cf74-311c-9da1-59559ed0876d | -2.91332 | -48.2375 | 2025-06-20 05:18:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| bebe5f07-4ceb-31a9-acf3-fc5acf6eee19 | -7.26961 | -45.35527 | 2025-06-20 05:18:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 48d0bbf2-bf23-31fb-a5e8-4fb76031bfad | -3.03676 | -49.42723 | 2025-06-20 05:18:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| defad448-d227-3eac-88a6-3ac3271fbf6f | -3.41629 | -47.60815 | 2025-06-20 05:18:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c012338d-4a1c-3bef-a991-2fab9c1a1c41 | -3.03603 | -49.43335 | 2025-06-20 05:18:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| f1f8a4f6-84c4-3415-b95c-a1689a36955c | -3.03078 | -49.43257 | 2025-06-20 05:18:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d1b0978e-6b1c-33a2-9129-49e9a1d0edad | -7.96818 | -46.2212 | 2025-06-20 05:18:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| b3e29523-6f0a-3da9-a5f6-0993074875fc | -3.04154 | -49.43124 | 2025-06-20 05:18:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 8a6f63bc-d677-3213-9de9-1bd92756f3b9 | -3.03702 | -49.42697 | 2025-06-20 05:18:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 9760c39e-bbfe-3c03-b3e2-b6611ced2cec | -3.04178 | -49.43096 | 2025-06-20 05:18:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| f8475054-6258-3efd-a63f-dacd27f60d81 | -3.03177 | -49.42618 | 2025-06-20 05:18:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 37a399ec-bb03-3d33-94bf-76f599bd00ce | -3.03127 | -49.42939 | 2025-06-20 05:18:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 045ef7af-3720-3805-bbc2-b399b5881332 | -7.2687 | -45.3623 | 2025-06-20 05:18:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| ce317fc4-77e8-3673-bafb-a0f50d085107 | -7.38946 | -45.40442 | 2025-06-20 05:18:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 03e9acce-c3ff-3093-b512-22f5021bef33 | -4.37885 | -48.08102 | 2025-06-20 05:18:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| e553c2ec-c6e9-39d8-9db6-63f095c61f13 | -3.72713 | -53.77216 | 2025-06-20 05:18:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 1d4faa70-56a4-374a-8221-1d9b4fc50648 | -4.77941 | -47.25051 | 2025-06-20 05:18:00 | NPP-375D | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 3f80057b-ece9-34a9-9e92-1f425d2270f2 | -3.03629 | -49.43043 | 2025-06-20 05:18:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 4751bd7a-8763-36de-89a8-7a63834ecdb1 | -4.37945 | -48.07697 | 2025-06-20 05:18:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 5b73bfbc-19b1-39d3-a538-bb49483b25e5 | -3.03653 | -49.43016 | 2025-06-20 05:18:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 1cdc3cf0-a290-3a64-ba1f-0e91d5272c0f | -2.919 | -48.23836 | 2025-06-20 05:18:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| d06f14f4-5ba7-31e5-85e1-9ed5d233f0e9 | -4.77871 | -47.25548 | 2025-06-20 05:18:00 | NPP-375D | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f41826b4-8fe1-30ee-90c3-c2a365b00d43 | -3.73185 | -53.76768 | 2025-06-20 05:18:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 61970814-3047-392b-87a4-63c3ce044df8 | -3.03583 | -49.43362 | 2025-06-20 05:18:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| c31a4d80-5d6e-3422-a09f-dcb6da261b27 | -5.30424 | -55.97315 | 2025-06-20 05:18:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 5ba8c7ee-0d87-3714-bdf3-62dfc33fa2e5 | -7.26778 | -45.36941 | 2025-06-20 05:18:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| b48c1ccb-2236-3a60-a01d-15c1c9ac09be | -7.72189 | -55.13502 | 2025-06-20 05:18:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 5e540d6b-7279-3ad6-b41d-999d54d24db9 | -3.03104 | -49.42964 | 2025-06-20 05:18:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 6f170a54-5ecd-3105-821a-ea0947a268e5 | -2.91957 | -48.23451 | 2025-06-20 05:18:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 23af4f94-6cdd-35c4-b48e-4fa544a41b03 | -3.03057 | -49.43283 | 2025-06-20 05:18:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 0d8d8bdb-f11e-3a29-b157-d425b73567a6 | -7.38858 | -45.41117 | 2025-06-20 05:18:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| cadf1c18-02c8-322e-868a-7f7a568b9846 | -7.15819 | -55.45667 | 2025-06-20 05:18:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| c635e2f9-ef4d-3e96-8d08-f50e6d6507ee | -6.60358 | -55.30154 | 2025-06-20 05:18:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| d4c334a9-b31e-3c7a-88b5-23abdb021fe0 | -7.96891 | -46.21545 | 2025-06-20 05:18:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| bd326b26-7aaf-351c-99d8-83e5f691854f | -3.04201 | -49.42805 | 2025-06-20 05:18:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 4bded33f-fcc5-364e-a9ad-5ff69718b0f4 | -3.42227 | -47.60887 | 2025-06-20 05:18:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 3acaf003-a9b9-3dea-b8b6-c6b037ca1582 | -11.952 | -58.7376 | 2025-06-20 05:20:00 | GOES-19 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 47.7 |
| b5c6123c-522b-34ea-a3b9-c36538b7e0ce | -10.4564 | -47.0347 | 2025-06-20 05:20:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 63.9 |
| ceb4b768-b4e8-31bb-99dd-b612a3972657 | -10.4754 | -47.0325 | 2025-06-20 05:20:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 114.9 |
| 4b0a5c19-0243-37d3-8431-73ddffd5bce3 | -10.456 | -47.0571 | 2025-06-20 05:20:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 53.3 |
| 6709b3af-0bdd-37c6-a1b5-d131b0c43028 | -16.3047 | -58.2676 | 2025-06-20 05:20:00 | GOES-19 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 52.1 |
| 07f5e93a-97e0-335b-a554-31790cabeee5 | -10.475 | -47.0548 | 2025-06-20 05:20:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 70.7 |
| 3eb042dc-33fa-32c3-a41a-8a90b5ae105f | -10.49168 | -47.02648 | 2025-06-20 05:21:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 24352ce1-de8e-388e-ae8b-aea608d6f0d1 | -12.50606 | -58.35027 | 2025-06-20 05:21:00 | NPP-375D | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 0.5 |
| b7de3c20-1c37-3f04-b97d-6f630183803e | -10.83192 | -54.00986 | 2025-06-20 05:21:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 7d14f3a6-94c5-384f-8ec5-dae7fc74f169 | -11.13694 | -46.63218 | 2025-06-20 05:21:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 3b9e81fe-c59a-3edf-b868-d048dea7d3d7 | -11.62283 | -58.29211 | 2025-06-20 05:21:00 | NPP-375D | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| c9420bc3-c962-3ab2-a049-8e44695ddf2c | -11.14581 | -46.63525 | 2025-06-20 05:21:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 67da94d9-4e4d-3f25-9691-39acbb0bdbee | -12.89428 | -56.98811 | 2025-06-20 05:21:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 70306be9-2d59-331a-846c-d4dcb19a7c47 | -14.62903 | -48.11658 | 2025-06-20 05:21:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 7a744681-6f6b-38c8-b649-7ef9292ea3ea | -12.89582 | -56.9851 | 2025-06-20 05:21:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 0918bd7c-6008-3e55-8e4a-5e5044431aef | -9.45465 | -57.83394 | 2025-06-20 05:21:00 | NPP-375D | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |


[Clique aqui para ver as próximas entradas](README24.md)
