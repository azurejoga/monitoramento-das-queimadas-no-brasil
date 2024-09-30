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

## Dados Diários - Página 58

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 7122e34c-baed-3fc6-a934-811d09e0a892 | -14.75715 | -48.75 | 2024-09-30 05:06:00 | AQUA_M-M | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 22.6 |
| 2c311398-be9e-33b7-b881-44944dad08f4 | -14.74864 | -48.73521 | 2024-09-30 05:06:00 | AQUA_M-M | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 10.4 |
| bf93c01b-ffec-31bb-a5ab-36039fd806f8 | -14.17926 | -46.4492 | 2024-09-30 05:06:00 | AQUA_M-M | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 12.2 |
| 0be3dc56-9c59-37b3-82f5-de2572f71ca3 | -14.16828 | -46.45785 | 2024-09-30 05:06:00 | AQUA_M-M | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 12.6 |
| c2d7ac7c-3b8a-3ccf-8a88-dc6564619386 | -13.49164 | -48.58118 | 2024-09-30 05:06:00 | AQUA_M-M | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 9.6 |
| ade887d5-a1d6-31d5-b4a6-aa4d34294117 | -13.48917 | -48.59598 | 2024-09-30 05:06:00 | AQUA_M-M | TROMBAS | GOIÁS | Brasil | 5221452 | 52 | 33 | nan | nan | nan | Cerrado | 11.5 |
| ba071f2b-8e0f-31bb-baf6-29acbf80e69e | -13.47595 | -48.60842 | 2024-09-30 05:06:00 | AQUA_M-M | TROMBAS | GOIÁS | Brasil | 5221452 | 52 | 33 | nan | nan | nan | Cerrado | 14.2 |
| ceea8b29-b8f6-3b26-969b-cf611e989537 | -13.25167 | -46.34997 | 2024-09-30 05:06:00 | AQUA_M-M | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 9.7 |
| 9d5bcb92-013a-3b61-99aa-71e5eae6ad04 | -13.24475 | -46.35352 | 2024-09-30 05:06:00 | AQUA_M-M | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 9.5 |
| e5d1e510-24fd-3f52-941b-228346218e3d | -13.20271 | -46.31473 | 2024-09-30 05:06:00 | AQUA_M-M | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 9.6 |
| 32e9dbb4-a345-309e-a7de-a17cf0575bda | -13.19166 | -46.32371 | 2024-09-30 05:06:00 | AQUA_M-M | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 45.3 |
| 2845405c-b820-39b3-86a4-3a739cc0978e | -13.19002 | -46.33399 | 2024-09-30 05:06:00 | AQUA_M-M | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 26.3 |
| 729bfebd-2694-3173-b73a-f2199eea962e | -13.18839 | -46.34426 | 2024-09-30 05:06:00 | AQUA_M-M | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 17.2 |
| beb0833a-aa56-3e10-af34-a50094a39d80 | -13.18674 | -46.35458 | 2024-09-30 05:06:00 | AQUA_M-M | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 54.2 |
| dd485a05-0306-3536-9aa2-9a9098838651 | -13.18403 | -46.31117 | 2024-09-30 05:06:00 | AQUA_M-M | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 12.8 |
| 2be7f253-17b9-3987-b21f-f493a5fe340b | -13.179 | -46.34269 | 2024-09-30 05:06:00 | AQUA_M-M | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 39.1 |
| 87c0d867-727f-3ba8-8893-445c28e31cf6 | -13.17734 | -46.35303 | 2024-09-30 05:06:00 | AQUA_M-M | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 120.7 |
| 838d263e-d9ba-3047-9886-bf2e8acfe5bd | -13.1757 | -46.36331 | 2024-09-30 05:06:00 | AQUA_M-M | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 8.5 |
| 3b3f6056-00e1-3ef9-b0d7-a32652885bc1 | -11.24525 | -45.65692 | 2024-09-30 05:06:00 | AQUA_M-M | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 11.5 |
| 32626182-e4b9-34ff-8f5c-5fd317a9b93c | -11.24367 | -45.66692 | 2024-09-30 05:06:00 | AQUA_M-M | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 5.3 |
| f7d64408-e07c-3310-912b-9b8179d4575c | -11.21095 | -45.6549 | 2024-09-30 05:06:00 | AQUA_M-M | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 5.9 |
| acef18db-30f4-31f7-909a-e617167ada01 | -11.20477 | -45.6947 | 2024-09-30 05:06:00 | AQUA_M-M | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 11.1 |
| 16472269-daca-38c6-bffc-3662042099e5 | -11.19084 | -45.7229 | 2024-09-30 05:06:00 | AQUA_M-M | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 10.0 |
| e49e8bbf-858a-3ba1-bc2c-edb8bcc6ec6e | -11.18928 | -45.73292 | 2024-09-30 05:06:00 | AQUA_M-M | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 19.6 |
| c4501ff4-810b-3d12-8988-524152f8808e | -11.18771 | -45.74294 | 2024-09-30 05:06:00 | AQUA_M-M | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 11.5 |
| 59486a4c-201c-3120-905e-dfeae93bf3db | -11.1862 | -45.69147 | 2024-09-30 05:06:00 | AQUA_M-M | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 4.4 |
| eec2ffcf-5d73-3209-8b5a-9ce943d95505 | -11.18309 | -45.7114 | 2024-09-30 05:06:00 | AQUA_M-M | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 11.3 |
| 71e682fc-96be-309f-ad12-bf8aecdf9941 | -11.17839 | -45.74145 | 2024-09-30 05:06:00 | AQUA_M-M | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 16.0 |
| 801f22d4-ec9f-34a9-b4ef-ac6d4b6bbe9f | -11.16906 | -45.73996 | 2024-09-30 05:06:00 | AQUA_M-M | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 46.8 |
| 45717652-1c2c-3faf-8049-3aec386ad322 | -11.16748 | -45.75 | 2024-09-30 05:06:00 | AQUA_M-M | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 22.3 |
| 87b56a65-9d22-3bad-9471-043c46248693 | -11.15998 | -45.61597 | 2024-09-30 05:06:00 | AQUA_M-M | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 13.9 |
| 76a31d68-c63e-32cd-953f-49730ec09ab8 | -11.15973 | -45.73848 | 2024-09-30 05:06:00 | AQUA_M-M | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 45.7 |
| 033c4cc4-d40d-3080-955d-b9d22ca3bdea | -11.15841 | -45.62587 | 2024-09-30 05:06:00 | AQUA_M-M | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 11.5 |
| 2ee2bd33-f69c-3b9b-8913-aff668358e10 | -11.15815 | -45.74852 | 2024-09-30 05:06:00 | AQUA_M-M | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 37.1 |
| d0f589b4-e334-300d-bb8f-442d2f661e86 | -11.15275 | -45.96668 | 2024-09-30 05:06:00 | AQUA_M-M | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 7.4 |
| 87d92f22-f54a-39d8-bb32-4ceda50e0099 | -11.15056 | -45.67557 | 2024-09-30 05:06:00 | AQUA_M-M | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 23.1 |
| 39db5849-6199-3456-9e15-28cf32b6071f | -11.1504 | -45.73701 | 2024-09-30 05:06:00 | AQUA_M-M | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 44.4 |
| 2b63054b-4994-3165-bd4e-e5ec75b3ec1e | -11.14913 | -45.62441 | 2024-09-30 05:06:00 | AQUA_M-M | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 5.7 |
| e39031d8-d8e9-3bc3-8564-22477671fd05 | -11.14898 | -45.68554 | 2024-09-30 05:06:00 | AQUA_M-M | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 17.1 |
| 8d374b61-7e71-3036-9d15-d56351743711 | -11.14882 | -45.74704 | 2024-09-30 05:06:00 | AQUA_M-M | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 13.3 |
| 29cebb24-afaf-3ebf-872c-d8da6aa15481 | -11.14272 | -45.61766 | 2024-09-30 05:06:00 | AQUA_M-M | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 7.5 |
| 1de9c291-37f8-3979-9a6f-4c2cadf706fa | -11.14266 | -45.72552 | 2024-09-30 05:06:00 | AQUA_M-M | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 22.4 |
| 0963f2c6-57aa-3f8d-9001-7feaeb53b10c | -11.14119 | -45.6276 | 2024-09-30 05:06:00 | AQUA_M-M | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 13.8 |
| fb2b9b96-b672-324b-9b31-bb60fc271581 | -11.14107 | -45.73555 | 2024-09-30 05:06:00 | AQUA_M-M | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 31.4 |
| f0a6e016-0cdc-3c92-b7af-4cbf6879e47d | -11.13968 | -45.68407 | 2024-09-30 05:06:00 | AQUA_M-M | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 24.4 |
| 3cf9555c-6621-35d7-bc1e-2d30406e8253 | -11.13948 | -45.74558 | 2024-09-30 05:06:00 | AQUA_M-M | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 8.6 |
| 40bd09e9-fa7a-324e-9e87-e5b7e98373a0 | -11.1319 | -45.62616 | 2024-09-30 05:06:00 | AQUA_M-M | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 47.7 |
| 2947e138-a25a-3c52-9d77-d68c7ed316a4 | -11.13174 | -45.73409 | 2024-09-30 05:06:00 | AQUA_M-M | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 39.1 |
| f5a9d642-b5a5-3850-a73e-33ad3b4d54a8 | -11.13014 | -45.74413 | 2024-09-30 05:06:00 | AQUA_M-M | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 38.9 |
| cfb7e1b8-d31b-3a10-be06-6522250721e3 | -11.0381 | -45.85852 | 2024-09-30 05:06:00 | AQUA_M-M | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 11.7 |
| 11f4b383-d71d-3fc0-a7e6-09f8611f7322 | -10.88406 | -46.03312 | 2024-09-30 05:06:00 | AQUA_M-M | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 727e6eed-de5e-3b4e-b3fc-058530032338 | -10.88243 | -46.04364 | 2024-09-30 05:06:00 | AQUA_M-M | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 9.0 |
| 69e45f43-b7e3-3f8f-b46e-f5ae1f467987 | -10.67157 | -46.14838 | 2024-09-30 05:06:00 | AQUA_M-M | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 7.0 |
| af8fc325-b4c6-390b-88b9-be04efc38bd0 | -10.66991 | -46.15893 | 2024-09-30 05:06:00 | AQUA_M-M | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 16.3 |
| 4e1c2c79-d0fb-33b4-8346-22c2b2200f31 | -13.20648 | -48.55716 | 2024-09-30 05:06:00 | AQUA_M-M | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 10.3 |
| 21a4ac64-637e-3a13-a9ff-37ae9e465cf0 | -13.03656 | -48.60257 | 2024-09-30 05:06:00 | AQUA_M-M | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 15.6 |
| ec5638d5-4ef2-3c87-8474-30a968331425 | -12.72489 | -46.41846 | 2024-09-30 05:06:00 | AQUA_M-M | AURORA DO TOCANTINS | TOCANTINS | Brasil | 1702703 | 17 | 33 | nan | nan | nan | Cerrado | 21.2 |
| 17ddae79-b9d1-3c82-a3ea-f341ef9152cc | -11.97799 | -47.29488 | 2024-09-30 05:06:00 | AQUA_M-M | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 78725e5b-5a86-399b-b0f4-531e420c8fc3 | -11.97607 | -47.30689 | 2024-09-30 05:06:00 | AQUA_M-M | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 7.6 |
| 4a5b4a84-73bc-37b6-9ffb-6cfdf5cd9f36 | -11.57619 | -48.43111 | 2024-09-30 05:06:00 | AQUA_M-M | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 25.9 |
| 0a49e80d-a23b-3ed6-b432-e3230e9a0ba9 | -11.44785 | -46.95179 | 2024-09-30 05:06:00 | AQUA_M-M | PORTO ALEGRE DO TOCANTINS | TOCANTINS | Brasil | 1718006 | 17 | 33 | nan | nan | nan | Cerrado | 9.3 |
| 64582300-6a5f-319d-b4ea-2e80ebda18cf | -11.39387 | -47.22244 | 2024-09-30 05:06:00 | AQUA_M-M | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 7.9 |
| 8212db93-68a6-3c8d-b5c7-23d2a6a0f14a | -11.39193 | -47.23443 | 2024-09-30 05:06:00 | AQUA_M-M | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 12.2 |
| 07c92478-931f-31a8-9fa8-3e5617180b70 | -11.38998 | -47.24643 | 2024-09-30 05:06:00 | AQUA_M-M | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 12.1 |
| fa367789-989e-3bcf-8e34-421a47f2d626 | -11.07166 | -52.42812 | 2024-09-30 05:06:00 | AQUA_M-M | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 58.5 |
| 490cf061-b3f2-3ab7-b47c-1cd53f4ce5be | -10.97467 | -46.44365 | 2024-09-30 05:06:00 | AQUA_M-M | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 7.2 |
| 284a1c60-3828-33e8-8a49-d173046446fc | -10.97285 | -46.45509 | 2024-09-30 05:06:00 | AQUA_M-M | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 12.2 |
| 1d90d1fd-53eb-3d15-9fe8-d16da9261468 | -10.96054 | -46.40729 | 2024-09-30 05:06:00 | AQUA_M-M | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 4155b6a1-0b80-34e9-bc13-4459ca564e29 | -10.9526 | -46.39479 | 2024-09-30 05:06:00 | AQUA_M-M | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 6.5 |
| a6df1f69-1806-3b6a-b759-4c9cfa386c0f | -10.93035 | -47.30235 | 2024-09-30 05:06:00 | AQUA_M-M | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 10.0 |
| 98ce6311-6f27-3553-8141-8cf430ffcaf9 | -10.84092 | -48.13728 | 2024-09-30 05:06:00 | AQUA_M-M | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 11.1 |
| 16d2188e-ff19-36ff-8b30-4abf38996309 | -10.83838 | -48.14489 | 2024-09-30 05:06:00 | AQUA_M-M | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 14.6 |
| aa4dc4fd-701d-3417-a055-79120620b9a8 | -10.81867 | -48.12739 | 2024-09-30 05:06:00 | AQUA_M-M | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 7.9 |
| 2d10589e-fa84-39e9-93ea-f6b13dd2a236 | -10.76302 | -48.73888 | 2024-09-30 05:06:00 | AQUA_M-M | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 10.1 |
| 9d6c8039-3c46-3509-aa8d-5e54408a92e4 | -10.71718 | -47.9725 | 2024-09-30 05:06:00 | AQUA_M-M | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 11.7 |
| 07b61bfa-fcfa-3fb9-92e8-bb3501ea0f77 | -10.71484 | -47.98674 | 2024-09-30 05:06:00 | AQUA_M-M | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 23.1 |
| 6a053298-7344-39ac-bbc6-c7d57974e550 | -10.70627 | -47.9711 | 2024-09-30 05:06:00 | AQUA_M-M | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 25.0 |
| 368d0a2a-7d07-3739-a165-64ed08b24a83 | -10.70393 | -47.98526 | 2024-09-30 05:06:00 | AQUA_M-M | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 6.9 |
| a7ae00aa-46fe-31dc-85fc-806c6d22a0c5 | -10.56454 | -48.05148 | 2024-09-30 05:06:00 | AQUA_M-M | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 54577d8d-ba61-3d5f-98c3-c76f20f15901 | -10.44899 | -48.20142 | 2024-09-30 05:06:00 | AQUA_M-M | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 12.7 |
| d3e8715c-32dd-33ff-b971-a4475ffce316 | -10.44796 | -48.20884 | 2024-09-30 05:06:00 | AQUA_M-M | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 16.6 |
| 4d90c417-493f-3d40-965b-27220a1ee2c9 | -10.44772 | -50.74273 | 2024-09-30 05:06:00 | AQUA_M-M | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 25.2 |
| 94cea435-19fc-3557-a729-9cba286cf0a2 | -10.40423 | -48.19619 | 2024-09-30 05:06:00 | AQUA_M-M | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 23.6 |
| d3f5291a-4343-3b41-9eaa-c4b61148ee8a | -22.73816 | -43.75923 | 2024-09-30 05:08:00 | AQUA_M-M | SEROPÉDICA | RIO DE JANEIRO | Brasil | 3305554 | 33 | 33 | nan | nan | nan | Mata Atlântica | 14.1 |
| aef95e79-6aa1-3197-b532-4a0566bc1a2f | -22.69909 | -42.14862 | 2024-09-30 05:08:00 | AQUA_M-M | SÃO PEDRO DA ALDEIA | RIO DE JANEIRO | Brasil | 3305208 | 33 | 33 | nan | nan | nan | Mata Atlântica | 11.2 |
| fb86e581-8bda-3a0a-8fb8-e4449e190fd9 | -22.69166 | -42.15593 | 2024-09-30 05:08:00 | AQUA_M-M | SÃO PEDRO DA ALDEIA | RIO DE JANEIRO | Brasil | 3305208 | 33 | 33 | nan | nan | nan | Mata Atlântica | 7.6 |
| 87e5a363-502b-3441-943d-104f6125d69c | -21.97676 | -46.80495 | 2024-09-30 05:08:00 | AQUA_M-M | SÃO JOÃO DA BOA VISTA | SÃO PAULO | Brasil | 3549102 | 35 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 894a61b5-4662-3e1e-9371-e79a2122d5f5 | -21.97528 | -46.81454 | 2024-09-30 05:08:00 | AQUA_M-M | SÃO JOÃO DA BOA VISTA | SÃO PAULO | Brasil | 3549102 | 35 | 33 | nan | nan | nan | Cerrado | 16.7 |
| 8e0b5b06-cea0-3321-9f4b-5e103d51a55a | -21.85876 | -48.37014 | 2024-09-30 05:08:00 | AQUA_M-M | BOA ESPERANÇA DO SUL | SÃO PAULO | Brasil | 3506706 | 35 | 33 | nan | nan | nan | Cerrado | 12.1 |
| 87af058d-1aba-3959-b01b-90854ff4e7da | -21.62818 | -47.78353 | 2024-09-30 05:08:00 | AQUA_M-M | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 6.8 |
| f7ebf364-b864-3304-8f8c-e37e41e56645 | -21.61903 | -47.78181 | 2024-09-30 05:08:00 | AQUA_M-M | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 14.9 |
| c8ace8d2-ccf3-36e4-a478-10870560535f | -21.61738 | -47.792 | 2024-09-30 05:08:00 | AQUA_M-M | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 14.2 |
| 2a1c6d22-4d84-3708-9ac6-434f222ef4c7 | -21.61572 | -47.80223 | 2024-09-30 05:08:00 | AQUA_M-M | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 20.6 |
| 9655ea09-6982-3a7a-9da7-6b6c60f7fd3b | -21.61406 | -47.81247 | 2024-09-30 05:08:00 | AQUA_M-M | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 25.0 |
| 2ae573e2-baa2-39ae-af9b-a38b045cceae | -21.61009 | -47.79454 | 2024-09-30 05:08:00 | AQUA_M-M | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 7.5 |
| 9e3da126-454c-358e-a61f-e6d679170af3 | -21.60847 | -47.80478 | 2024-09-30 05:08:00 | AQUA_M-M | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 41.5 |
| 10477e03-a8a0-3eb4-9d67-e484bf5005a1 | -21.60685 | -47.81496 | 2024-09-30 05:08:00 | AQUA_M-M | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 10.4 |
| d575f9f1-b47c-3466-a7f7-bd50bcccc528 | -21.5891 | -47.7487 | 2024-09-30 05:08:00 | AQUA_M-M | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 5.2 |
| ee1e99b6-9dfb-3d70-9fa7-f3666bc5d1b8 | -21.49111 | -49.82133 | 2024-09-30 05:08:00 | AQUA_M-M | PROMISSÃO | SÃO PAULO | Brasil | 3541604 | 35 | 33 | nan | nan | nan | Mata Atlântica | 48.6 |
| 4b05df19-47c1-3dc5-9075-950d848c06f2 | -21.48888 | -49.8342 | 2024-09-30 05:08:00 | AQUA_M-M | PROMISSÃO | SÃO PAULO | Brasil | 3541604 | 35 | 33 | nan | nan | nan | Mata Atlântica | 17.3 |


[Clique aqui para ver as próximas entradas](README59.md)
