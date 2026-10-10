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

## Dados Diários - Página 163

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| bd1563c7-04ba-33bb-bcf1-230d25c716c1 | -1.3447 | -56.3979 | 2026-10-10 14:50:00 | GOES-19 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 102.5 |
| 815b2e7c-b1c5-3c7d-996f-89a629db5567 | -2.8529 | -54.1723 | 2026-10-10 14:50:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 54.2 |
| 8cc79a35-96b1-3a30-ae31-1f07890e491c | -1.254 | -55.7496 | 2026-10-10 14:50:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 63.0 |
| e5b5d90c-2abb-3567-813b-cd7249908cdc | -12.0646 | -43.4071 | 2026-10-10 14:50:00 | GOES-19 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 131.8 |
| bfe5b8fa-e8e3-32c9-bb63-8536c1b9b1d1 | -9.0829 | -45.0957 | 2026-10-10 14:50:00 | GOES-19 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 135.6 |
| decf6684-5474-3a97-a6db-b71d2ef7fdf4 | -11.0374 | -44.0355 | 2026-10-10 14:50:00 | GOES-19 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 199.0 |
| 5b59ecc1-e5e4-3ded-a97d-8a09d265e3df | -1.6578 | -55.211 | 2026-10-10 14:50:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 65.4 |
| 6e0d9f68-d138-34a1-98b7-daaedc0c3fd9 | -1.2455 | -49.0194 | 2026-10-10 14:50:00 | GOES-19 | PONTA DE PEDRAS | PARÁ | Brasil | 1505700 | 15 | 33 | nan | nan | nan | Amazônia | 65.7 |
| e489e3f7-66a5-3543-8de1-8e91e962104d | -11.3636 | -54.0246 | 2026-10-10 14:50:00 | GOES-19 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 66.5 |
| 292e4b84-d0b6-3164-b024-d1ea5e78ca00 | -12.1857 | -48.4345 | 2026-10-10 14:50:00 | GOES-19 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 73.2 |
| a4d13488-f4c8-3b31-86b4-328b3cef5d3a | -8.9311 | -45.1355 | 2026-10-10 14:50:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 122.4 |
| a6199f06-1506-3aa5-9434-d8b4b2d40271 | -4.4025 | -49.7774 | 2026-10-10 14:50:00 | GOES-19 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 91.7 |
| 304a0518-05a2-32ae-91b2-ff132ec3e132 | -2.8491 | -49.8763 | 2026-10-10 14:50:00 | GOES-19 | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 60.2 |
| a6a27b6e-d117-339f-af0a-48b4b7ef1b97 | -11.0379 | -44.012 | 2026-10-10 14:50:00 | GOES-19 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 229.1 |
| 4bbaa6db-4528-341b-b08a-a8d2e7e8225b | -10.9533 | -50.7018 | 2026-10-10 14:50:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 71.2 |
| f2fd278b-249b-37bf-9dab-43c112462a0a | -1.3933 | -48.9534 | 2026-10-10 14:50:00 | GOES-19 | PONTA DE PEDRAS | PARÁ | Brasil | 1505700 | 15 | 33 | nan | nan | nan | Amazônia | 62.2 |
| 355be69e-cb16-35e9-8576-d210e5a392fd | -13.1641 | -54.3178 | 2026-10-10 14:50:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 116.5 |
| b8a6bb50-4e8f-3a4d-822a-e6bfe9187fdd | -11.1873 | -45.3347 | 2026-10-10 14:50:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 113.4 |
| dfcb1112-7d46-3740-9ffe-124b2db9e666 | -9.0944 | -44.266 | 2026-10-10 14:50:00 | GOES-19 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 133.4 |
| ee06365f-bd14-3a4d-b066-cf82447b154a | -11.6002 | -43.5989 | 2026-10-10 14:50:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 111.5 |
| 4564a87c-219b-3e47-8c5c-684336e5af55 | -3.2717 | -50.4102 | 2026-10-10 14:50:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 192.2 |
| 8cf4d7e5-5e5d-3a90-a9a3-d706b6dffd26 | -3.1114 | -53.7839 | 2026-10-10 14:50:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 54.4 |
| 756bc4a5-3a5c-3770-a683-f5e89374711b | -11.0328 | -45.4475 | 2026-10-10 14:50:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 130.5 |
| 1626daae-7dfb-3e25-af65-896a55e515c8 | -11.7768 | -45.5035 | 2026-10-10 14:50:00 | GOES-19 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 227.0 |
| 1f486ada-134b-3a79-be83-360be7ef4cb4 | -2.0403 | -56.3895 | 2026-10-10 14:50:00 | GOES-19 | TERRA SANTA | PARÁ | Brasil | 1507979 | 15 | 33 | nan | nan | nan | Amazônia | 64.7 |
| 9cb2425e-1aed-38c3-81c7-cadddd7d2b16 | -1.6579 | -55.1912 | 2026-10-10 14:50:00 | GOES-19 | CURUÁ | PARÁ | Brasil | 1502855 | 15 | 33 | nan | nan | nan | Amazônia | 120.8 |
| 51a66df1-13f4-33a5-8d11-888e6c427055 | -11.2064 | -45.3321 | 2026-10-10 14:50:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 126.5 |
| a91eaa47-4328-3dc0-b0e5-3c268a657327 | -10.2491 | -49.642 | 2026-10-10 14:50:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 50.7 |
| 68758256-e5b1-3727-bb04-8084f5e2f006 | -10.2486 | -49.6851 | 2026-10-10 14:50:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 60.1 |
| 75a2bc13-94f1-3125-be6b-314d1d6109d5 | -1.3447 | -56.4175 | 2026-10-10 14:50:00 | GOES-19 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 65.5 |
| 62a4705f-4b74-3eb6-b1a8-6d4fe3468607 | -0.9829 | -52.4415 | 2026-10-10 14:50:00 | GOES-19 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 67.3 |
| e9eb576a-ef08-3a84-8061-11d353b83bae | -0.8768 | -48.7033 | 2026-10-10 14:50:00 | GOES-19 | CACHOEIRA DO ARARI | PARÁ | Brasil | 1502004 | 15 | 33 | nan | nan | nan | Amazônia | 74.8 |
| 287a659b-845b-354a-8376-b1b2dc442d91 | -3.0192 | -53.887 | 2026-10-10 14:50:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 63.9 |
| 564b2308-7c52-3eee-be0a-96a39966c4f3 | -11.0332 | -45.4246 | 2026-10-10 14:50:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 108.0 |
| e269fdab-bd6d-367e-982d-8b7b048a2cae | -12.2145 | -44.6291 | 2026-10-10 14:50:00 | GOES-19 | CATOLÂNDIA | BAHIA | Brasil | 2907400 | 29 | 33 | nan | nan | nan | Cerrado | 133.2 |
| b605cb6e-9c7a-3290-8eef-db6ce42047bd | -1.8986 | -53.9899 | 2026-10-10 14:50:00 | GOES-19 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 72.5 |
| 479c0c09-2d2e-3028-a3eb-e7d625f94821 | -15.3832 | -41.9029 | 2026-10-10 14:50:00 | GOES-19 | SÃO JOÃO DO PARAÍSO | MINAS GERAIS | Brasil | 3162708 | 31 | 33 | nan | nan | nan | Mata Atlântica | 124.8 |
| 349c6d1b-548b-3fae-a638-4225ddff2e74 | -3.2766 | -53.8602 | 2026-10-10 14:50:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 92.0 |
| c1d34220-51e7-3a59-b75c-7251821e6e8a | -9.9384 | -44.8791 | 2026-10-10 14:50:00 | GOES-19 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 107.6 |
| b7740cfc-f701-3692-afc7-a9b3f73f617a | -12.0265 | -43.3895 | 2026-10-10 14:50:00 | GOES-19 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 132.9 |
| 37fb8475-edc6-31e3-afef-62854450d388 | -3.106 | -50.2896 | 2026-10-10 14:50:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 63.1 |
| 40b65e87-a9c1-3a83-a64c-5e3f27cbaf02 | -0.8768 | -48.7246 | 2026-10-10 14:50:00 | GOES-19 | CACHOEIRA DO ARARI | PARÁ | Brasil | 1502004 | 15 | 33 | nan | nan | nan | Amazônia | 72.5 |
| 9b113d34-9edc-3845-996e-daf157312ebc | -12.1729 | -44.7983 | 2026-10-10 14:50:00 | GOES-19 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 187.9 |
| 34ea2049-03c2-3839-9e00-c9e316f4bd06 | -1.3264 | -56.4176 | 2026-10-10 14:50:00 | GOES-19 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 54.4 |
| 25e69920-5469-3c74-996f-feadd64c83d2 | -11.0183 | -44.0382 | 2026-10-10 14:50:00 | GOES-19 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 168.7 |
| 0a7d3ad7-6969-3706-9b5f-a6da76e97202 | -2.798 | -54.0933 | 2026-10-10 14:50:00 | GOES-19 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 70.0 |
| 8d9c00c2-2eab-3362-965b-d9f117429672 | -3.11 | -54.1862 | 2026-10-10 14:50:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 62.0 |
| 3a11b382-c0bd-39ef-ad4a-004a5e01a4e0 | -9.9208 | -44.7893 | 2026-10-10 14:50:00 | GOES-19 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 119.1 |
| e5ea2f1d-a2bd-31a8-a1ac-7a47c815bfce | -11.1876 | -45.3117 | 2026-10-10 14:50:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 98.8 |
| 70f3599c-5edf-3dd9-94b4-41af0b5056b8 | -12.7072 | -43.0611 | 2026-10-10 14:50:00 | GOES-19 | PARATINGA | BAHIA | Brasil | 2923704 | 29 | 33 | nan | nan | nan | Caatinga | 153.0 |
| 0d0d0ee1-48ed-342c-a320-7d0406fd88bc | -3.053 | -54.7679 | 2026-10-10 14:50:00 | GOES-19 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 82.5 |
| 6edea032-59ae-325a-aa8f-6ddc19a6d903 | -12.1819 | -45.3518 | 2026-10-10 14:50:00 | GOES-19 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 130.8 |
| 8a34ee1e-b805-3f33-a1aa-d075c6019748 | -10.9343 | -50.7039 | 2026-10-10 14:50:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 67.3 |
| f75b4475-95fa-3f1b-aa6e-b84a7219f1fd | -3.2765 | -53.8803 | 2026-10-10 14:50:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 94.1 |
| 0b67171e-c3cc-32ce-a656-e2eebe48c55e | -9.5541 | -45.2239 | 2026-10-10 14:50:00 | GOES-19 | MONTE ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2206605 | 22 | 33 | nan | nan | nan | Cerrado | 90.0 |
| 45ae751b-1571-38f7-9d1c-c9b3357f92eb | -18.3125 | -42.3901 | 2026-10-10 14:50:00 | GOES-19 | SANTA MARIA DO SUAÇUÍ | MINAS GERAIS | Brasil | 3158201 | 31 | 33 | nan | nan | nan | Mata Atlântica | 102.4 |
| a54b2599-5419-319c-a2f8-bef368e50f67 | -2.4623 | -56.0879 | 2026-10-10 14:50:00 | GOES-19 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 54.2 |
| 930abd93-9884-3992-b6b2-eee8d29983a6 | -12.0453 | -43.4102 | 2026-10-10 14:50:00 | GOES-19 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 144.0 |
| f6e5feab-7312-3152-8c39-84d3c787c802 | -10.2488 | -49.6636 | 2026-10-10 14:50:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 58.3 |
| bb9749cc-e378-3de0-b98c-b38acd518d9f | -3.0531 | -54.7479 | 2026-10-10 14:50:00 | GOES-19 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 61.8 |
| d118a4d5-ae8e-3261-a17d-d56cb18d3f83 | -11.6194 | -43.5959 | 2026-10-10 14:50:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 148.8 |
| 4d2bcaa5-6f07-344e-9876-1fb0a8e69563 | -9.8442 | -47.4608 | 2026-10-10 14:50:00 | GOES-19 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 47.5 |
| 6c3bea28-e24d-30c5-b9d7-2a5250e8d30f | -12.8321 | -50.9981 | 2026-10-10 15:00:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 62.9 |
| 9e63ef1a-14e9-31aa-b9bd-c998f67dca26 | -11.7764 | -45.5265 | 2026-10-10 15:00:00 | GOES-19 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 123.1 |
| e13ff68e-480c-3e22-9b10-549cd360a2a9 | -8.9504 | -45.1105 | 2026-10-10 15:00:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 171.8 |
| d31ec232-58be-3281-8156-db746c4ea68d | 4.2606 | -60.932 | 2026-10-10 15:00:00 | GOES-19 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 71.8 |
| c3fff12f-c73a-36a4-8304-4eebff302f06 | -11.3636 | -54.0246 | 2026-10-10 15:00:00 | GOES-19 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 66.0 |
| f5dc2445-a37b-3bce-9216-7aa1d5d328c3 | -3.053 | -54.7679 | 2026-10-10 15:00:00 | GOES-19 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 130.7 |
| 9f09cc32-1791-3e0a-bda5-0959a810a10a | -2.8529 | -54.1723 | 2026-10-10 15:00:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 59.0 |
| a99d6b54-9fbe-3047-817f-9b71379a4181 | -11.0379 | -44.012 | 2026-10-10 15:00:00 | GOES-19 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 198.7 |
| f4dc289c-47a6-3ac2-be83-74607a9fad21 | -1.6409 | -54.3946 | 2026-10-10 15:00:00 | GOES-19 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 96.0 |
| 810fa953-af40-3937-bc0a-c9d1cfad7f44 | 2.4028 | -50.9561 | 2026-10-10 15:00:00 | GOES-19 | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 65.7 |
| 7654bc40-0cab-3ec0-8f6f-b089c1d18018 | -1.8986 | -53.9899 | 2026-10-10 15:00:00 | GOES-19 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 86.1 |
| 173d4340-277b-339c-912f-e745f80f4673 | -11.0393 | -51.329 | 2026-10-10 15:00:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 56.6 |
| f7f866fa-53a2-31b1-9041-80495e37c078 | -1.3447 | -56.3979 | 2026-10-10 15:00:00 | GOES-19 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 107.7 |
| d750a49d-db5a-3361-8711-07a711e075fc | -10.2486 | -49.6851 | 2026-10-10 15:00:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 76.0 |
| 2d300fcb-e6fb-362e-8b89-d130fe667824 | -17.4581 | -45.0511 | 2026-10-10 15:00:00 | GOES-19 | BURITIZEIRO | MINAS GERAIS | Brasil | 3109402 | 31 | 33 | nan | nan | nan | Cerrado | 101.9 |
| 98f3dc31-91dd-37f3-a514-b423a5be8a64 | -12.1857 | -48.4345 | 2026-10-10 15:00:00 | GOES-19 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 75.0 |
| 1219e4c3-303d-3816-9ce0-2585f7c891b8 | -10.9197 | -45.3712 | 2026-10-10 15:00:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 229.2 |
| 43a94c2b-68e1-3d35-9d6e-8a97a0b920e2 | -3.5144 | -54.1955 | 2026-10-10 15:00:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 60.7 |
| b0deb5be-f28e-38d5-b0fe-c9f799516c12 | -10.2675 | -49.6831 | 2026-10-10 15:00:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 44.2 |
| 899a155e-148a-30e5-a9f5-ab1fdb7e2150 | -11.7742 | -43.5245 | 2026-10-10 15:00:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 381.2 |
| f15220a4-a8e9-3150-9f6d-8243cebeca98 | -3.2031 | -53.842 | 2026-10-10 15:00:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 95.6 |
| 24e2718a-e157-38ae-800d-721911aa6015 | -17.4775 | -45.0705 | 2026-10-10 15:00:00 | GOES-19 | BURITIZEIRO | MINAS GERAIS | Brasil | 3109402 | 31 | 33 | nan | nan | nan | Cerrado | 124.5 |
| 2d4c76be-594e-3d48-925b-f758cc0d9897 | -10.9533 | -50.7018 | 2026-10-10 15:00:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 75.7 |
| 026c16ce-164e-39bc-a512-c5fa31e38f2c | -10.9579 | -45.3661 | 2026-10-10 15:00:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 287.8 |
| 11e1a1ea-1fc6-3f53-8525-aabf43f687dc | -2.4238 | -56.8534 | 2026-10-10 15:00:00 | GOES-19 | PARINTINS | AMAZONAS | Brasil | 1303403 | 13 | 33 | nan | nan | nan | Amazônia | 62.4 |
| aca12140-760d-3dd3-a3e3-db88c6e86a2c | -3.2766 | -53.8602 | 2026-10-10 15:00:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 130.2 |
| ff55207c-6e6a-3039-97e9-057c72629018 | -2.8247 | -57.606 | 2026-10-10 15:00:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 94.3 |
| 76ce0e19-b93e-3a0e-b24f-6983a9f6e216 | -3.0192 | -53.887 | 2026-10-10 15:00:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 64.6 |
| fa7c54c1-ac0c-3186-99f3-634d46609de2 | -15.0893 | -46.9378 | 2026-10-10 15:00:00 | GOES-19 | VILA BOA | GOIÁS | Brasil | 5222203 | 52 | 33 | nan | nan | nan | Cerrado | 91.0 |
| 3d392825-a5bd-3bcc-91b9-e3df4a248b2f | 4.279 | -60.9126 | 2026-10-10 15:00:00 | GOES-19 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 62.0 |
| 9f0aa2fa-ca4a-35bc-bfa8-29a27f27bcfd | -3.2533 | -50.3899 | 2026-10-10 15:00:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 59.8 |
| c5805e3a-f265-395d-b851-e14e510f1e71 | -11.7545 | -43.5512 | 2026-10-10 15:00:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 155.9 |
| f31fa268-256e-3a43-ba6f-22eb3697e0be | -2.8247 | -57.6254 | 2026-10-10 15:00:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 88.9 |
| 76f6f7f8-f0f3-3b8c-9d69-d5b4d3cb7504 | -10.9388 | -45.3687 | 2026-10-10 15:00:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 223.0 |
| adff3f5c-4fe1-326f-9ad6-1aaa4a461088 | -12.4759 | -54.4919 | 2026-10-10 15:00:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 69.9 |
| 3eda657b-7862-3357-abab-48fa17a84d2f | -11.6789 | -43.4921 | 2026-10-10 15:00:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 159.3 |
| 235f8800-7218-3ef1-82dd-0cd26287a9c4 | -2.5689 | -57.4163 | 2026-10-10 15:00:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 80.8 |
| 44b5f955-2aae-3905-a0af-1852417cb787 | -4.4977 | -43.6315 | 2026-10-10 15:00:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 73.4 |


[Clique aqui para ver as próximas entradas](README164.md)
