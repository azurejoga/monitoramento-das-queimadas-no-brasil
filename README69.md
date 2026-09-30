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
| 7ab13cfb-9b16-370d-98a6-5901b6d7ec07 | -7.2567 | -43.3228 | 2026-09-30 14:00:00 | GOES-19 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 87.4 |
| 6935e188-0055-33db-a7d1-95ecd7eb8f20 | -11.1958 | -44.8269 | 2026-09-30 14:00:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 109.3 |
| ac2e774b-a128-370b-9f03-f1b10b4b8d4e | -10.2839 | -44.6505 | 2026-09-30 14:00:00 | GOES-19 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 72.8 |
| 0a353509-b3b3-3914-a080-dccdf8427c5f | -11.3918 | -43.4654 | 2026-09-30 14:00:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 261.9 |
| 262d885b-cade-36c0-b917-811638076eb6 | -6.7062 | -45.6216 | 2026-09-30 14:00:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 113.0 |
| 77948778-5ca4-311f-b650-a9a716730850 | -8.2102 | -45.4621 | 2026-09-30 14:00:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 84.1 |
| 6f0e73c5-70b1-325d-839e-7d7a04b4bf53 | -12.6082 | -47.2429 | 2026-09-30 14:00:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 80.8 |
| dbd2be7c-8dbf-398e-bbc9-682cafe852e4 | -11.1954 | -44.85 | 2026-09-30 14:00:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 92.1 |
| 845668c3-45de-367b-97d3-43701c156710 | -10.2847 | -44.6042 | 2026-09-30 14:00:00 | GOES-19 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 93.8 |
| d08d232b-a911-30c4-b4aa-f1c862ec0fb0 | -10.907 | -43.8433 | 2026-09-30 14:00:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 119.6 |
| 5cfdb681-f160-30b7-8a4d-6fdbaa1897d6 | -8.3617 | -45.4013 | 2026-09-30 14:00:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 81.2 |
| b30bd85a-2af9-37df-a448-09e1f1f187db | -11.411 | -43.4625 | 2026-09-30 14:00:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 166.3 |
| cedd1653-eab8-3a9d-8a8f-076374e2b7ac | -11.1767 | -44.8296 | 2026-09-30 14:00:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 92.7 |
| f29416f1-29e8-3251-a65a-e323f9827d71 | -7.4156 | -42.6241 | 2026-09-30 14:00:00 | GOES-19 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 94.6 |
| bfd9f51d-ad97-3cef-9cfa-842f94f0286f | -12.4355 | -44.1262 | 2026-09-30 14:00:00 | GOES-19 | TABOCAS DO BREJO VELHO | BAHIA | Brasil | 2930907 | 29 | 33 | nan | nan | nan | Cerrado | 141.9 |
| 58fb3954-bd47-3d16-b30c-e68b390fff26 | -12.4539 | -44.1702 | 2026-09-30 14:00:00 | GOES-19 | TABOCAS DO BREJO VELHO | BAHIA | Brasil | 2930907 | 29 | 33 | nan | nan | nan | Cerrado | 304.2 |
| e5a32c17-1ccf-341d-b682-34220223de74 | -7.3656 | -42.0819 | 2026-09-30 14:00:00 | GOES-19 | COLÔNIA DO PIAUÍ | PIAUÍ | Brasil | 2202778 | 22 | 33 | nan | nan | nan | Caatinga | 78.9 |
| f72758b9-9878-32d0-b22d-797a9d4bb1d8 | -12.1078 | -47.3803 | 2026-09-30 14:00:00 | GOES-19 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 61.9 |
| 2b766f81-44cb-3f05-8967-8e1e5cf520f5 | -9.5087 | -45.7525 | 2026-09-30 14:00:00 | GOES-19 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 55.5 |
| fcf21c14-2b2b-3c5f-8efe-af0269ae142d | -11.6797 | -44.5012 | 2026-09-30 14:00:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 159.6 |
| 7a0ac5b7-0361-3e2c-94af-4119bf7b62f3 | -10.1881 | -49.9703 | 2026-09-30 14:00:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 64.2 |
| 171b5d2a-4204-3122-be76-3e9ce3dc9dca | -12.0694 | -48.5377 | 2026-09-30 14:00:00 | GOES-19 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 69.5 |
| f1ff6944-da37-3570-9a4b-6a683137fb7f | -7.0736 | -42.8708 | 2026-09-30 14:00:00 | GOES-19 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 67.9 |
| 76528423-55dd-30fc-a927-f4482648347f | -8.6451 | -45.3489 | 2026-09-30 14:00:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 90.8 |
| d2b486e3-cbe6-3d7c-ae1e-a549e384c75a | -7.0359 | -42.8744 | 2026-09-30 14:00:00 | GOES-19 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 78.4 |
| 8b7d8664-57e9-39d2-8ddb-d7e04707817e | -8.0169 | -42.8444 | 2026-09-30 14:00:00 | GOES-19 | PAJEÚ DO PIAUÍ | PIAUÍ | Brasil | 2207355 | 22 | 33 | nan | nan | nan | Caatinga | 144.6 |
| 53718717-8db6-3560-8a68-c23a24c5c93c | -7.2755 | -43.321 | 2026-09-30 14:00:00 | GOES-19 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 101.4 |
| fb08bb5f-1b43-3cf0-aac1-9933052c023a | -7.4733 | -45.7809 | 2026-09-30 14:00:00 | GOES-19 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 64.5 |
| 760647e3-d550-35ed-835b-52b2e5e2259a | 4.1882 | -60.687 | 2026-09-30 14:00:00 | GOES-19 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 62.6 |
| acd6a623-3d4e-3428-8f14-78d11392d0e5 | -7.3467 | -42.0839 | 2026-09-30 14:00:00 | GOES-19 | COLÔNIA DO PIAUÍ | PIAUÍ | Brasil | 2202778 | 22 | 33 | nan | nan | nan | Caatinga | 53.8 |
| a0f81c6a-afee-334c-9828-aa15df7db576 | -7.0547 | -42.8726 | 2026-09-30 14:00:00 | GOES-19 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 80.6 |
| f513e447-083f-33b3-a969-616889706b5e | -12.7618 | -47.2431 | 2026-09-30 14:00:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 91.0 |
| 60aa201c-b370-30b6-9700-93de135aaea5 | -12.6086 | -47.2204 | 2026-09-30 14:00:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 62.0 |
| 31df16ba-c011-3307-89a3-319e465aeed7 | -11.6605 | -44.5041 | 2026-09-30 14:00:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 162.0 |
| 96ca24ac-45a1-32d1-a4ec-f6a0059202b9 | 1.7115 | -55.9221 | 2026-09-30 14:00:00 | GOES-19 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 110.7 |
| e4da6a6b-8e6b-3d0f-8b1e-648438196ec8 | -11.6395 | -43.5455 | 2026-09-30 14:00:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 119.5 |
| a84882a0-e52e-3050-a9cc-3c92b6c2c177 | -7.4153 | -42.6479 | 2026-09-30 14:00:00 | GOES-19 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 97.6 |
| 51629861-552e-373e-a81f-40a10160fcf5 | -9.8613 | -44.9577 | 2026-09-30 14:00:00 | GOES-19 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 314.8 |
| 1e609c3b-b6bb-3225-b101-802310ca0a5e | -13.3469 | -46.8169 | 2026-09-30 14:00:00 | GOES-19 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 115.3 |
| b2405939-1e63-3b4f-9a91-6dfbd78f2867 | 3.64 | -60.5086 | 2026-09-30 14:00:00 | GOES-19 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 64.1 |
| d178ccc1-e36b-384a-bc2f-2072d5bf584e | -10.2067 | -49.9898 | 2026-09-30 14:00:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 61.3 |
| e513d976-fd54-32bf-b07f-7622e2b58544 | -12.4351 | -44.1497 | 2026-09-30 14:00:00 | GOES-19 | TABOCAS DO BREJO VELHO | BAHIA | Brasil | 2930907 | 29 | 33 | nan | nan | nan | Cerrado | 269.5 |
| bdbe7868-60a0-37f5-a244-fa61b3e9c5ad | -7.0074 | -43.7428 | 2026-09-30 14:00:00 | GOES-19 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 68.7 |
| c66e98ed-b368-3ba1-88da-d1f6bb7c9a3c | -10.5496 | -49.7823 | 2026-09-30 14:00:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 68.6 |
| 95f0b9d3-d833-348c-a603-e6d7f1139e96 | -11.215 | -44.8242 | 2026-09-30 14:00:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 84.4 |
| 0c77cf16-aab0-3200-aad2-4d84dfefcf91 | -9.4328 | -50.1086 | 2026-09-30 14:00:00 | GOES-19 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 63.5 |
| 8348cbbd-a3de-372f-9e3d-5653cdde2a6b | -11.2566 | -43.5331 | 2026-09-30 14:00:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 111.9 |
| 1ff0a202-31ba-33b1-bf48-ecc28c64356e | 1.8586 | -55.6241 | 2026-09-30 14:00:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 65.5 |
| 1c4d12d4-d734-383c-8063-328878a28637 | -8.2668 | -45.4564 | 2026-09-30 14:00:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 70.0 |
| 4873c427-5e22-3feb-a5bc-05482818fc8f | 1.6933 | -55.9026 | 2026-09-30 14:00:00 | GOES-19 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 66.9 |
| ffa018e9-f743-38da-9ca3-bc7a35cc8d89 | 1.675 | -55.9028 | 2026-09-30 14:00:00 | GOES-19 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 65.2 |
| c5862ecd-b19e-39ed-90a3-ce91ba067289 | 1.6566 | -55.9227 | 2026-09-30 14:00:00 | GOES-19 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 58.8 |
| e957a92e-c0ea-370c-a37c-7954743ecb8b | -11.3927 | -43.418 | 2026-09-30 14:00:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 172.4 |
| 0f27f83e-39e8-3545-8503-0baa96c99bfb | -11.64 | -43.5218 | 2026-09-30 14:00:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 185.7 |
| 87ff6b5b-9e12-39c9-8714-1f6bbf9447e2 | 1.8586 | -55.6439 | 2026-09-30 14:00:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 63.9 |
| 36fe4f9a-af91-3cc8-9e45-f38a8cabe743 | -10.7686 | -47.7302 | 2026-09-30 14:00:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 55.5 |
| 7b4e0e24-8184-3ea0-8ef4-2d0d4e5f601d | -10.2843 | -44.6274 | 2026-09-30 14:00:00 | GOES-19 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 174.5 |
| b36fb874-c056-3cd5-a940-5c9ead42c89c | -14.3959 | -41.3729 | 2026-09-30 14:00:00 | GOES-19 | ARACATU | BAHIA | Brasil | 2902005 | 29 | 33 | nan | nan | nan | Caatinga | 108.1 |
| 20c4cd73-877e-351f-878c-cb18dbb04162 | -10.7255 | -44.4291 | 2026-09-30 14:00:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 99.2 |
| aa123317-15cb-3c6b-b0cf-d416b03c5412 | -6.7059 | -45.6441 | 2026-09-30 14:00:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 81.9 |
| df0a27c6-2544-30ba-b9b5-b136ef5d0dc9 | -9.8617 | -44.9347 | 2026-09-30 14:00:00 | GOES-19 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 148.4 |
| ce26d39a-1bea-3c68-b33a-2ca76b7773e1 | -7.0612 | -42.3035 | 2026-09-30 14:00:00 | GOES-19 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 98.8 |
| af8625a3-c852-31b3-be26-469874270c95 | -11.1903 | -45.1505 | 2026-09-30 14:10:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 83.4 |
| 8fb25f8f-a3f1-33d9-88e8-e432d4d12314 | -11.3927 | -43.418 | 2026-09-30 14:10:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 155.5 |
| d3a5541f-3f03-3a5a-856b-78e8b954ac8c | -7.4153 | -42.6479 | 2026-09-30 14:10:00 | GOES-19 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 103.6 |
| d55ac260-3b2b-3df3-a6bb-778641d90d67 | -9.8617 | -44.9347 | 2026-09-30 14:10:00 | GOES-19 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 112.9 |
| 2a5d6f66-2c30-3c16-a4f3-65ae81a37d28 | -9.7965 | -48.1923 | 2026-09-30 14:10:00 | GOES-19 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 133.2 |
| 4d15aed0-c24d-33bf-8d48-06f927a9fa04 | -7.0612 | -42.3035 | 2026-09-30 14:10:00 | GOES-19 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 100.2 |
| da4d7aad-2ce5-33f3-a98b-e43f1278c688 | -8.0166 | -42.8681 | 2026-09-30 14:10:00 | GOES-19 | PAJEÚ DO PIAUÍ | PIAUÍ | Brasil | 2207355 | 22 | 33 | nan | nan | nan | Caatinga | 119.2 |
| 8d4ff524-6683-304a-a111-976b789e180b | 1.8586 | -55.6241 | 2026-09-30 14:10:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 86.9 |
| eab353fb-61a2-3568-914e-c468faf81552 | -5.6036 | -43.3715 | 2026-09-30 14:10:00 | GOES-19 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 63.7 |
| f6417e06-4256-3327-8032-bfd00e2d070a | -10.7689 | -47.708 | 2026-09-30 14:10:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 51.9 |
| 0881ae9d-24a4-3347-bf81-79fdaac2adf4 | -14.6474 | -40.6939 | 2026-09-30 14:10:00 | GOES-19 | VITÓRIA DA CONQUISTA | BAHIA | Brasil | 2933307 | 29 | 33 | nan | nan | nan | Mata Atlântica | 161.2 |
| 3504471f-9cd7-3033-b0f8-244f6de142fc | -8.0169 | -42.8444 | 2026-09-30 14:10:00 | GOES-19 | PAJEÚ DO PIAUÍ | PIAUÍ | Brasil | 2207355 | 22 | 33 | nan | nan | nan | Caatinga | 146.8 |
| 4e7c80ab-fc56-305d-80f4-fe81e1e3b2e4 | -11.7182 | -43.4386 | 2026-09-30 14:10:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 183.1 |
| 41b8f77a-0d7b-398a-917b-2982a2bd4773 | -10.1881 | -49.9703 | 2026-09-30 14:10:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 76.5 |
| 768641b1-b822-3774-b074-b3a96e501ef8 | -10.2843 | -44.6274 | 2026-09-30 14:10:00 | GOES-19 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 121.9 |
| 3bcb4417-0caf-3891-bb68-d0cbd57d7107 | -8.3805 | -45.3994 | 2026-09-30 14:10:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 81.0 |
| 0dfef105-b6eb-39d6-91b4-ed178c49d5c6 | -17.5345 | -43.6891 | 2026-09-30 14:10:00 | GOES-19 | OLHOS-D'ÁGUA | MINAS GERAIS | Brasil | 3145455 | 31 | 33 | nan | nan | nan | Cerrado | 141.8 |
| e8801405-8b7f-3861-a72a-538e3db393da | -14.6277 | -40.6982 | 2026-09-30 14:10:00 | GOES-19 | VITÓRIA DA CONQUISTA | BAHIA | Brasil | 2933307 | 29 | 33 | nan | nan | nan | Mata Atlântica | 220.3 |
| 745e72bd-c8d7-39f9-afb4-955884e7824f | -13.3658 | -46.8366 | 2026-09-30 14:10:00 | GOES-19 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 66.1 |
| e848b671-f3fe-3bc8-a6be-03815d42c34b | 1.6566 | -55.9227 | 2026-09-30 14:10:00 | GOES-19 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 61.0 |
| 10f66ea2-1f44-3e40-9509-848de562bff4 | -11.4106 | -43.4862 | 2026-09-30 14:10:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 107.5 |
| cfbe4e27-0ca1-3395-8c0c-22b7e94b4556 | -13.3469 | -46.8169 | 2026-09-30 14:10:00 | GOES-19 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 116.5 |
| 593b6b60-3c91-37bb-b004-4cad4ed5cf04 | -6.7251 | -45.5975 | 2026-09-30 14:10:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 88.5 |
| 2537ecd0-58ab-30c7-96e7-4f3738783728 | -11.64 | -43.5218 | 2026-09-30 14:10:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 164.0 |
| d99f9955-2955-33c9-82e9-8545347a7b2d | -9.7877 | -44.8058 | 2026-09-30 14:10:00 | GOES-19 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 82.6 |
| 36bdf720-6b3d-330e-b466-b177ce672a3f | -11.1767 | -44.8296 | 2026-09-30 14:10:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 99.2 |
| e4d5abfa-2476-3386-bc57-5330a12345f9 | -6.8762 | -43.7083 | 2026-09-30 14:10:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 71.4 |
| 2f48601a-33d1-3211-b944-c7b7f943870d | 1.6933 | -55.9026 | 2026-09-30 14:10:00 | GOES-19 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 80.4 |
| f0e3a911-19a0-3e34-af37-6795d95765d8 | -6.8957 | -43.6368 | 2026-09-30 14:10:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 69.2 |
| 6267ac54-c8ba-3036-8725-697449d4638e | -14.3959 | -41.3729 | 2026-09-30 14:10:00 | GOES-19 | ARACATU | BAHIA | Brasil | 2902005 | 29 | 33 | nan | nan | nan | Caatinga | 94.7 |
| ce6cbe91-4c78-30ec-82b7-34364c0789f8 | -6.7254 | -45.5749 | 2026-09-30 14:10:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 122.6 |
| 395f64bf-ee1c-3f32-9107-2bbdb8e590b7 | -5.8712 | -51.7974 | 2026-09-30 14:10:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 81.2 |
| 0d778fd4-d209-3666-b7b3-064119e140b9 | -7.2755 | -43.321 | 2026-09-30 14:10:00 | GOES-19 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 97.7 |
| 2f59eab2-7ab0-3d83-bb30-9912bfc0c4f6 | -11.2095 | -45.1478 | 2026-09-30 14:10:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 177.9 |
| 6162823a-7962-385f-9140-dff35c389a41 | -11.6395 | -43.5455 | 2026-09-30 14:10:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 126.6 |
| 00309b71-8d2b-3980-ab21-9cce8d27f0f1 | -12.4355 | -44.1262 | 2026-09-30 14:10:00 | GOES-19 | TABOCAS DO BREJO VELHO | BAHIA | Brasil | 2930907 | 29 | 33 | nan | nan | nan | Cerrado | 123.0 |
| 3c7da9dd-9d86-342a-9be0-501959545f66 | 1.6932 | -55.9223 | 2026-09-30 14:10:00 | GOES-19 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 82.7 |
| db3f81d4-bceb-3ebf-83c5-13b141191a7a | -9.7962 | -48.2143 | 2026-09-30 14:10:00 | GOES-19 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 59.6 |


[Clique aqui para ver as próximas entradas](README70.md)
