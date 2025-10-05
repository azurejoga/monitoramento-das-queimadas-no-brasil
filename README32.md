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

## Dados Diários - Página 32

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 512a7df5-73dd-3cfa-a976-2d90ed50a841 | -11.00327 | -46.52908 | 2025-10-05 03:34:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 10.7 |
| f9a3e946-24a7-3fcc-9824-77cb5b41a756 | -7.71932 | -42.39361 | 2025-10-05 03:34:00 | NPP-375D | SÃO MIGUEL DO FIDALGO | PIAUÍ | Brasil | 2210391 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| f27409f3-218c-3a63-8353-93d7670de309 | -13.52343 | -47.28589 | 2025-10-05 03:34:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| bf314677-1401-3c1c-9055-e7faa85de3f0 | -13.34964 | -47.19902 | 2025-10-05 03:34:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| a9d767f9-e59b-3624-b703-82ee4d36e6a6 | -10.39261 | -45.39684 | 2025-10-05 03:34:00 | NPP-375D | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| f2016d9a-8b5b-325e-a5bf-c9417d5ec58f | -11.88465 | -44.97366 | 2025-10-05 03:34:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 14429591-f93d-3a46-bbec-954741a269ba | -13.48028 | -47.28625 | 2025-10-05 03:34:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 4.2 |
| eaa36cc9-80b9-3007-9ee0-9653d1d68758 | -13.11657 | -44.07908 | 2025-10-05 03:34:00 | NPP-375D | SANTANA | BAHIA | Brasil | 2928208 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| a5ea75c7-8414-31d8-94f4-0ce48c4e8a64 | -13.45602 | -47.2669 | 2025-10-05 03:34:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| ac262896-0f71-3cd5-884d-3e6b20ef8106 | -13.09463 | -47.87914 | 2025-10-05 03:34:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 51e61c5a-3be3-3ce0-b6ae-1cb56866cec8 | -9.4712 | -45.5414 | 2025-10-05 03:34:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 2ae1b538-e897-30c0-be42-dd53d1513e37 | -11.82579 | -45.08518 | 2025-10-05 03:34:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 10.8 |
| c4dfaf24-bbd3-3e7a-a7b5-d783dcbc4730 | -8.60074 | -46.28147 | 2025-10-05 03:34:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 0b0f7bc8-5662-3fe9-8042-00ac1c457cf6 | -9.06808 | -47.01772 | 2025-10-05 03:34:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 5d17a58a-4654-3271-9812-ae6014958c60 | -8.53566 | -46.33028 | 2025-10-05 03:34:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 4.8 |
| a8898875-b34b-3d2e-9ab2-83662d77f507 | -11.48855 | -45.03452 | 2025-10-05 03:34:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 9d3aeb82-e5ea-3e8f-b85d-c3ae6cad889f | -11.44345 | -43.49434 | 2025-10-05 03:34:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| f4c1d935-1316-3ca7-b3ab-8a38989b39a4 | -8.53835 | -46.31655 | 2025-10-05 03:34:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 8.5 |
| becfd4cf-059e-327b-b53a-79f2e2a95c25 | -7.79094 | -44.13169 | 2025-10-05 03:34:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| fa318167-1f52-340f-90a1-a164cd97d0e3 | -10.94818 | -47.05434 | 2025-10-05 03:34:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 4.7 |
| e147482c-13f5-345c-95be-3c6a42cda257 | -10.63575 | -46.33974 | 2025-10-05 03:34:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 5b5ba415-52eb-311c-b71f-35698af5bfc8 | -7.24342 | -44.89085 | 2025-10-05 03:34:00 | NPP-375D | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 67dbc6a9-d74f-3f66-8d7b-027b64d75403 | -13.09389 | -47.91668 | 2025-10-05 03:34:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| abc0e83d-8b59-3344-882b-e719c61d4b2f | -12.89559 | -47.31915 | 2025-10-05 03:34:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 3217fd55-4511-334a-8246-bcd4d5f5da1f | -7.78721 | -42.60038 | 2025-10-05 03:34:00 | NPP-375D | RIBEIRA DO PIAUÍ | PIAUÍ | Brasil | 2208874 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| e2e3002f-fced-3b4b-9de2-cb6968949982 | -7.31708 | -45.55891 | 2025-10-05 03:34:00 | NPP-375D | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| c0c09d77-4a82-3eb8-b436-41d76f7873a5 | -7.77277 | -42.61995 | 2025-10-05 03:34:00 | NPP-375D | RIBEIRA DO PIAUÍ | PIAUÍ | Brasil | 2208874 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| c035219b-f5c3-3ab2-ac0b-f77771491c4a | -13.32479 | -47.18163 | 2025-10-05 03:34:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 303c33e1-e92d-38a3-9098-be7f41304759 | -7.47216 | -42.63052 | 2025-10-05 03:34:00 | NPP-375D | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 04e081a7-f26a-3e55-a64a-d24d86c3a819 | -13.29933 | -48.09887 | 2025-10-05 03:34:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 7.0 |
| 0be9f735-64f4-3881-a8fa-a24011dcc86e | -13.81381 | -43.17173 | 2025-10-05 03:34:00 | NPP-375D | RIACHO DE SANTANA | BAHIA | Brasil | 2926400 | 29 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 87945006-657f-3102-9b00-bf7f1c5c1749 | -9.63745 | -40.58392 | 2025-10-05 03:34:00 | NPP-375D | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 89f2218b-2544-3ae5-ba02-d1626ec36fb7 | -13.33644 | -48.06758 | 2025-10-05 03:34:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 6.9 |
| ac7d3843-4597-3e52-b5dc-4f1d7a3b705a | -10.64391 | -46.33458 | 2025-10-05 03:34:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| ab759c28-0e88-3f63-902e-bc3313097177 | -13.28221 | -47.6114 | 2025-10-05 03:34:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 0311b456-e09d-3e5e-ab5f-1f20b26fb0da | -14.87699 | -40.83325 | 2025-10-05 03:34:00 | NPP-375D | VITÓRIA DA CONQUISTA | BAHIA | Brasil | 2933307 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| a6e9e85b-478d-3ac1-9b15-9d444f7ad93b | -8.5547 | -46.2704 | 2025-10-05 03:34:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 946d5265-4cac-3af5-aa7f-13aaab2daca1 | -12.46506 | -45.51995 | 2025-10-05 03:34:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 31518667-fc74-3ab2-891b-bf4cb82b4bf0 | -11.85918 | -44.94856 | 2025-10-05 03:34:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| b818b3be-4b4a-30a9-be8c-b45e1857c2e6 | -8.90084 | -46.68572 | 2025-10-05 03:34:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 5ea4accc-abb8-3992-8591-ba2f12ee4f44 | -8.58899 | -46.31958 | 2025-10-05 03:34:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 32.4 |
| fe880b8b-fd12-3dd3-8763-ec054710e2c4 | -13.73303 | -47.95857 | 2025-10-05 03:34:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.3 |
| c4e70ae2-cfe3-3895-b3be-a786ad603e41 | -11.83779 | -45.07736 | 2025-10-05 03:34:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 647923a6-2a09-3cf9-b653-6e011db97487 | -11.86336 | -44.95196 | 2025-10-05 03:34:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 031ace3a-7b98-32b7-88a8-5d1789004d29 | -11.01626 | -46.70572 | 2025-10-05 03:34:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 15.2 |
| 285dcc1b-f196-3d0c-94a5-f51df5f9f266 | -9.2583 | -46.7795 | 2025-10-05 03:34:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 738138ae-8dcc-36ae-aeb6-c375ada8e796 | -10.93731 | -47.08839 | 2025-10-05 03:34:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 95.1 |
| 5548bf23-ffc1-3785-850d-d0cad3e69f59 | -10.39614 | -45.41289 | 2025-10-05 03:34:00 | NPP-375D | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 6.6 |
| a71e9918-37b0-3253-a0e9-77a372c1418a | -7.74805 | -42.52372 | 2025-10-05 03:34:00 | NPP-375D | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 5.6 |
| 8e9fe1ee-a72c-38ad-83a2-d9c9da241736 | -11.11717 | -47.21346 | 2025-10-05 03:34:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| a9f34b47-b13f-3969-973b-ae1c36b9f1a0 | -8.54303 | -46.3138 | 2025-10-05 03:34:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 0bdc15a0-0d4f-3171-bf26-9d2aa63092f6 | -13.31857 | -47.17733 | 2025-10-05 03:34:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 99a4358d-eff6-3ea0-aceb-eb23f2d74427 | -11.48332 | -45.02817 | 2025-10-05 03:34:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| acbbcee7-31eb-3046-b159-1f9465b20a7e | -13.30007 | -48.12922 | 2025-10-05 03:34:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 71d3fbc1-f32b-305e-bcde-c177c4dd95b6 | -13.32527 | -47.56709 | 2025-10-05 03:34:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 11104d9a-14df-3b9a-af65-1a2b3410be36 | -11.62659 | -45.02834 | 2025-10-05 03:34:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 4.7 |
| aaed0c52-48f8-3b86-9c26-a903e93349ed | -12.45672 | -45.52026 | 2025-10-05 03:34:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 7338b56a-f5dd-337e-bb8c-a599d604e4fb | -13.26093 | -47.60807 | 2025-10-05 03:34:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.3 |
| c95847ae-aa70-3e8f-90df-a8513ba7c503 | -9.12399 | -44.39569 | 2025-10-05 03:34:00 | NPP-375D | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 47ed1c64-f2ed-3f29-80c4-9d6dcf684068 | -11.53188 | -47.2349 | 2025-10-05 03:34:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| f63773fc-bcea-3c62-a974-649ca22eb82a | -9.29768 | -45.99332 | 2025-10-05 03:34:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 53961d37-0056-3882-a85c-cdd802401e9a | -7.25205 | -44.89833 | 2025-10-05 03:34:00 | NPP-375D | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 1f1f94c0-976b-3399-9d60-989ea73b5548 | -7.16194 | -46.08997 | 2025-10-05 03:34:00 | NPP-375D | NOVA COLINAS | MARANHÃO | Brasil | 2107258 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 11f72383-57d9-33a9-b133-75aca10965c7 | -13.735 | -48.08541 | 2025-10-05 03:34:00 | NPP-375D | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 1a92b79a-fb32-3fd6-922d-ac9799ec6623 | -13.59094 | -48.15962 | 2025-10-05 03:34:00 | NPP-375D | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 5ea8ff15-2b24-3d8b-a1a4-c3c7e6d95ba6 | -10.15073 | -45.43474 | 2025-10-05 03:34:00 | NPP-375D | SÃO GONÇALO DO GURGUÉIA | PIAUÍ | Brasil | 2209757 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| b3ecbfa3-0d67-37c8-b5e9-6c01c48c03e2 | -9.56941 | -46.12502 | 2025-10-05 03:34:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 6.1 |
| d2ebd707-c817-3973-88ba-40867c8dc78e | -13.35958 | -48.06492 | 2025-10-05 03:34:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 5.6 |
| e33e7ff6-bc81-35af-9772-afbe71828120 | -13.35229 | -47.57719 | 2025-10-05 03:34:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 43a9def1-0968-3bfb-a133-81cdcd26197d | -13.29279 | -47.58149 | 2025-10-05 03:34:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 225b16e6-82db-3f56-b348-4daf165b7ad8 | -7.69584 | -42.58298 | 2025-10-05 03:34:00 | NPP-375D | SOCORRO DO PIAUÍ | PIAUÍ | Brasil | 2210904 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 7aedf125-8b8b-3b4b-9ace-c4125d8fbf7d | -8.55022 | -46.36834 | 2025-10-05 03:34:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 32b0049e-32b1-370e-83b7-bc7e990a6d0b | -8.58094 | -46.36128 | 2025-10-05 03:34:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 985177f0-f2d6-366d-8f07-5373e64d37b8 | -7.58631 | -43.10449 | 2025-10-05 03:34:00 | NPP-375D | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 6e9a84dd-5c46-3b9a-9fd4-0bf5fdbb6bdc | -8.5714 | -46.35495 | 2025-10-05 03:34:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| e3a44725-158c-3e09-9df3-096e56851d1e | -13.44889 | -47.26673 | 2025-10-05 03:34:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 74b4987f-4790-3176-b667-ffdb2b1235eb | -7.4373 | -46.52419 | 2025-10-05 03:34:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 57930c43-9f81-38e4-a2fe-74d3dc6918c1 | -13.29002 | -47.82673 | 2025-10-05 03:34:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| c77e45b3-04ba-34b3-b565-22c33dc67eeb | -7.77358 | -42.61564 | 2025-10-05 03:34:00 | NPP-375D | RIBEIRA DO PIAUÍ | PIAUÍ | Brasil | 2208874 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 9b8ec695-5696-319a-a961-439d8e2faf8c | -13.74059 | -48.07301 | 2025-10-05 03:34:00 | NPP-375D | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 322dd244-d3a9-3c82-8d6f-59d14c5aa1a9 | -12.91084 | -47.31576 | 2025-10-05 03:34:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 44a7d295-8463-3407-b65e-f86ca3085ae5 | -8.56287 | -46.37883 | 2025-10-05 03:34:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| d522967f-7bdd-3978-b3f7-566d43e27037 | -11.48423 | -45.03949 | 2025-10-05 03:34:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 753f6fc2-67b4-3c68-b556-72cffb3a2703 | -13.26479 | -47.62403 | 2025-10-05 03:34:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.6 |
| e813dcc5-3995-38db-96c8-b1e752673821 | -12.82259 | -46.85872 | 2025-10-05 03:34:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 4.4 |
| c8812080-31f6-3c2a-b319-7aca4f21e9c0 | -11.83544 | -45.05721 | 2025-10-05 03:34:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 78c71197-5628-3a22-8f52-632064890cae | -10.63443 | -46.34619 | 2025-10-05 03:34:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 00d5da0f-ebfc-3ea4-9b03-a548e4a2bf98 | -8.56713 | -46.26691 | 2025-10-05 03:34:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 3d1aab3c-0604-37af-aa4a-a019f3d46893 | -13.5871 | -48.17001 | 2025-10-05 03:34:00 | NPP-375D | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 382cdd9e-5b1c-3a6d-ac56-fb8fedfbec56 | -12.45879 | -45.51004 | 2025-10-05 03:34:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| f7df4b8c-5c6d-3238-a364-e0f42b64bbb1 | -11.81456 | -45.0644 | 2025-10-05 03:34:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 382ea200-0cfa-3baa-96b0-397b3106d516 | -11.5014 | -44.98753 | 2025-10-05 03:34:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 6727c921-2cd5-3ccf-9372-9aad5d635529 | -7.24654 | -44.89124 | 2025-10-05 03:34:00 | NPP-375D | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 4d685575-1952-39ce-ae83-1a52f839ed3e | -11.83182 | -45.07491 | 2025-10-05 03:34:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 0614b7a7-c729-3647-a3a5-dd31a14bccd7 | -13.31802 | -47.5668 | 2025-10-05 03:34:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 2922898e-9c61-3629-84e4-d49a4c9eb41a | -11.80405 | -46.82478 | 2025-10-05 03:34:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 94ad2f57-3ee8-3612-8507-a5cabc02bbb5 | -9.29326 | -46.01608 | 2025-10-05 03:34:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 24.0 |
| d68d4b72-1826-385f-a3d5-cbafc86d15f1 | -7.58715 | -43.10001 | 2025-10-05 03:34:00 | NPP-375D | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 84518c88-b292-3741-b02a-e3f84e383d0f | -13.0921 | -47.9249 | 2025-10-05 03:34:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 5.2 |
| acce90a8-f434-3bd8-86d5-49838f42a247 | -10.39508 | -45.41815 | 2025-10-05 03:34:00 | NPP-375D | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 6.6 |


[Clique aqui para ver as próximas entradas](README33.md)
