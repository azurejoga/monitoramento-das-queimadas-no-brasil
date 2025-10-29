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

## Dados Diários - Página 84

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| d51ca44e-42a9-32fa-a41b-affad0bae479 | -15.96789 | -47.9725 | 2025-10-29 12:19:00 | TERRA_M-T | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 11.0 |
| a28c0625-d504-394a-aac4-a4767360e2bc | -12.65721 | -47.33773 | 2025-10-29 12:19:00 | TERRA_M-T | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 13.4 |
| 82331520-c5f9-36fa-9974-3deb261c7f01 | -7.50798 | -46.26858 | 2025-10-29 12:19:00 | TERRA_M-T | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 10.2 |
| 03d14852-4747-3f9e-a06b-b4c80dcb6bd5 | -12.10308 | -47.14483 | 2025-10-29 12:19:00 | TERRA_M-T | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 13.8 |
| 2169ffff-f33c-30e6-9584-b2444e7f394f | -9.6699 | -45.53905 | 2025-10-29 12:19:00 | TERRA_M-T | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 7.3 |
| b3df3525-bc25-3379-9b92-ec8ae5b4da6e | -10.10523 | -46.60849 | 2025-10-29 12:19:00 | TERRA_M-T | SÃO FÉLIX DO TOCANTINS | TOCANTINS | Brasil | 1720150 | 17 | 33 | nan | nan | nan | Cerrado | 9.2 |
| 55377b76-c858-3050-83d9-cfe6852f1adc | -12.87227 | -48.63211 | 2025-10-29 12:19:00 | TERRA_M-T | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 9.7 |
| 0e6a2ead-6690-39f0-8c3b-bd6fd4a78290 | -10.34906 | -47.5666 | 2025-10-29 12:19:00 | TERRA_M-T | LAGOA DO TOCANTINS | TOCANTINS | Brasil | 1711951 | 17 | 33 | nan | nan | nan | Cerrado | 13.3 |
| cb861078-e162-3e76-96ef-6622d15c5024 | -12.10828 | -47.17517 | 2025-10-29 12:19:00 | TERRA_M-T | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 16.6 |
| cb541b98-b423-3ec5-bb11-11c7f43466f6 | -12.10959 | -47.16551 | 2025-10-29 12:19:00 | TERRA_M-T | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 26.6 |
| 73aa0828-5ddc-3832-bb44-99efd1215700 | -7.7055 | -46.89774 | 2025-10-29 12:19:00 | TERRA_M-T | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 39.7 |
| 3f847845-ca71-3e77-867c-d4a2e5e82507 | -12.98311 | -47.91126 | 2025-10-29 12:19:00 | TERRA_M-T | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 7.7 |
| 8a17f78d-a5b6-3452-ab14-61de03654d86 | -9.49885 | -46.99189 | 2025-10-29 12:19:00 | TERRA_M-T | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 20.9 |
| 244a2fed-b0ff-36d9-a2ff-b585627c319b | -13.12796 | -46.93354 | 2025-10-29 12:19:00 | TERRA_M-T | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 11.8 |
| 2ff4aba7-10db-338c-894c-c9d2ddabee5e | -8.69737 | -47.12217 | 2025-10-29 12:19:00 | TERRA_M-T | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 11.0 |
| e1411df7-891e-3faa-a22a-7f8e9b8f97a8 | -14.47003 | -45.60295 | 2025-10-29 12:19:00 | TERRA_M-T | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 103.9 |
| 713683c2-15f1-3d39-8733-a25e87ae39bc | -7.63641 | -46.92817 | 2025-10-29 12:19:00 | TERRA_M-T | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 7.0 |
| 095ce403-f077-305e-951e-c758eb9dc2dd | -9.67137 | -45.5281 | 2025-10-29 12:19:00 | TERRA_M-T | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 14.8 |
| 541f2788-1329-38fa-ac99-b7b848290a1f | -9.48854 | -46.99993 | 2025-10-29 12:19:00 | TERRA_M-T | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 16.8 |
| c670076d-1d97-3b43-a247-5fad60eddf7c | -12.69528 | -46.30097 | 2025-10-29 12:19:00 | TERRA_M-T | AURORA DO TOCANTINS | TOCANTINS | Brasil | 1702703 | 17 | 33 | nan | nan | nan | Cerrado | 19.1 |
| 3f0bb9fc-b009-34ad-b66d-73de0afb0590 | -8.06207 | -45.03336 | 2025-10-29 12:19:00 | TERRA_M-T | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 12.4 |
| f8c57fe8-b19b-32b8-804b-94ad66ba3c53 | -12.94929 | -46.5386 | 2025-10-29 12:19:00 | TERRA_M-T | NOVO ALEGRE | TOCANTINS | Brasil | 1715150 | 17 | 33 | nan | nan | nan | Cerrado | 11.6 |
| 47420e7b-4b10-34b6-8971-9d1a471d09c8 | -12.35773 | -44.64713 | 2025-10-29 12:19:00 | TERRA_M-T | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 20.7 |
| 71104406-baf2-3e8b-a6e8-0eb2fb550081 | -9.80245 | -46.99556 | 2025-10-29 12:19:00 | TERRA_M-T | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 12.0 |
| da1846cf-27e6-3df7-aa6f-8cb0af7eaf59 | -10.91465 | -47.81071 | 2025-10-29 12:19:00 | TERRA_M-T | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 16.6 |
| eece52f0-6242-3e9e-83d8-d54ce0915183 | -8.24689 | -46.91079 | 2025-10-29 12:19:00 | TERRA_M-T | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 36.9 |
| bbe8e539-0da6-31e9-bd25-2f1a62e64dcf | -8.55659 | -47.0064 | 2025-10-29 12:19:00 | TERRA_M-T | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 7.0 |
| 89042adb-ebd9-3c4c-8fac-7799c3b5c7d6 | -10.35798 | -47.56784 | 2025-10-29 12:19:00 | TERRA_M-T | LAGOA DO TOCANTINS | TOCANTINS | Brasil | 1711951 | 17 | 33 | nan | nan | nan | Cerrado | 165.3 |
| 539b19ef-3001-3b63-aa07-16819ec71c60 | -12.18999 | -46.71198 | 2025-10-29 12:19:00 | TERRA_M-T | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 42.0 |
| 3ae824c5-3383-3b38-a754-5688623b80cb | -11.58602 | -47.94846 | 2025-10-29 12:19:00 | TERRA_M-T | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 36.9 |
| fe0ca24c-8c0b-3261-965e-d9b9c541cd38 | -10.65469 | -48.01281 | 2025-10-29 12:19:00 | TERRA_M-T | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 23.9 |
| 4b507bb9-1109-305b-9034-421601d517f0 | -9.89831 | -44.9012 | 2025-10-29 12:19:00 | TERRA_M-T | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 214.4 |
| 730bed32-ed30-3001-9a8c-09a26549bc85 | -11.99584 | -46.78617 | 2025-10-29 12:19:00 | TERRA_M-T | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 58.8 |
| b36656f1-e3f6-3b7f-865f-55fe397fa0f8 | -7.99426 | -45.53749 | 2025-10-29 12:19:00 | TERRA_M-T | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 9.5 |
| dc4901e8-8efd-3590-af3e-a67c5251919e | -7.50092 | -47.0416 | 2025-10-29 12:19:00 | TERRA_M-T | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 46597ce6-a0f0-35bc-af2f-3d8317a661e8 | -8.75565 | -46.50743 | 2025-10-29 12:19:00 | TERRA_M-T | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 10.8 |
| 552bfaff-1872-3fe9-b402-191be0a83df3 | -10.51016 | -47.73151 | 2025-10-29 12:19:00 | TERRA_M-T | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 13.9 |
| c02bfe49-962a-3f1c-bcf5-01ba2e94ef63 | -13.27634 | -47.85717 | 2025-10-29 12:19:00 | TERRA_M-T | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 11.3 |
| 1aeb3eea-506b-327a-9dce-201021abc1ee | -9.89993 | -44.88924 | 2025-10-29 12:19:00 | TERRA_M-T | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 101.7 |
| 9bb890dc-776e-3341-9e7d-0922c07bf7bd | -13.01434 | -47.21331 | 2025-10-29 12:19:00 | TERRA_M-T | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 7.7 |
| c8cfa868-1da3-3386-ae2e-f0799d8427c7 | -10.29564 | -47.29109 | 2025-10-29 12:19:00 | TERRA_M-T | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 12.7 |
| 24fb6864-8e26-3c8b-8d95-35b96bc0d42c | -12.15699 | -47.69115 | 2025-10-29 12:19:00 | TERRA_M-T | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 7.3 |
| 0fcf7876-d5de-37bf-b296-71441f35d8fb | -11.02964 | -47.8423 | 2025-10-29 12:19:00 | TERRA_M-T | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 7f6fab60-4d3a-379a-a2de-5bb0a6ff0a3a | -8.05558 | -45.15595 | 2025-10-29 12:19:00 | TERRA_M-T | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 15.1 |
| 1fe2e111-141a-360a-96f7-995c259553e9 | -10.60101 | -49.60051 | 2025-10-29 12:19:00 | TERRA_M-T | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 8.4 |
| 35b9437d-330a-3414-a2bf-a9b3237d4c2e | -14.28885 | -47.31587 | 2025-10-29 12:19:00 | TERRA_M-T | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 14.9 |
| f601e07e-cd27-38c1-a3f6-2f31b3768469 | -9.51107 | -45.57165 | 2025-10-29 12:19:00 | TERRA_M-T | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 11.8 |
| a9da9b1b-31d8-38f1-8b66-5cb2053c613b | -9.08791 | -47.81339 | 2025-10-29 12:19:00 | TERRA_M-T | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 8.2 |
| 0c3f74de-c469-366a-8ec0-027391707f3a | -10.36818 | -47.55995 | 2025-10-29 12:19:00 | TERRA_M-T | LAGOA DO TOCANTINS | TOCANTINS | Brasil | 1711951 | 17 | 33 | nan | nan | nan | Cerrado | 13.7 |
| 6b45a6f4-0d52-3699-a37d-ec315bb976d0 | -9.5054 | -46.94516 | 2025-10-29 12:19:00 | TERRA_M-T | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 12.8 |
| b91326ad-3acd-3378-9bda-c0a105d383e3 | -7.79442 | -46.45813 | 2025-10-29 12:19:00 | TERRA_M-T | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 28.6 |
| a75a020b-416a-38ac-bb3a-07ca98c7aac1 | -11.29841 | -47.57209 | 2025-10-29 12:19:00 | TERRA_M-T | PINDORAMA DO TOCANTINS | TOCANTINS | Brasil | 1717008 | 17 | 33 | nan | nan | nan | Cerrado | 8.4 |
| 939b6db7-bcde-384b-995b-0fb214cd6041 | -8.05739 | -46.94638 | 2025-10-29 12:19:00 | TERRA_M-T | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 11.2 |
| 91b2ae50-e3ea-34ec-b417-0dff5445d639 | -7.78666 | -46.44748 | 2025-10-29 12:19:00 | TERRA_M-T | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 18.0 |
| 49b91789-6451-334a-a887-862a93d325b5 | -9.9555 | -47.1527 | 2025-10-29 12:19:00 | TERRA_M-T | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 22.8 |
| bf7170d8-a930-3812-b2e1-cb2e545443fd | -13.66142 | -50.63064 | 2025-10-29 12:19:00 | TERRA_M-T | NOVA CRIXÁS | GOIÁS | Brasil | 5214838 | 52 | 33 | nan | nan | nan | Cerrado | 10.8 |
| 7ae356cd-aee3-326d-84c0-245bf67b410e | -12.10044 | -47.16424 | 2025-10-29 12:19:00 | TERRA_M-T | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 39.6 |
| 2bd4cca4-996a-377b-9bf7-a2441b6f2e17 | -7.77883 | -46.50371 | 2025-10-29 12:19:00 | TERRA_M-T | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 13.5 |
| 83599e3e-766e-31cf-b72d-ce323ba5b3a8 | -7.69644 | -46.89011 | 2025-10-29 12:19:00 | TERRA_M-T | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 22.6 |
| 70b4c511-2be4-3854-bb75-8c9437888010 | -13.21741 | -47.07153 | 2025-10-29 12:19:00 | TERRA_M-T | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 24.6 |
| 68b7f866-3940-358a-a2aa-5edec8e259c9 | -12.27766 | -42.74559 | 2025-10-29 12:19:00 | TERRA_M-T | OLIVEIRA DOS BREJINHOS | BAHIA | Brasil | 2923209 | 29 | 33 | nan | nan | nan | Caatinga | 31.8 |
| f7aacd01-866a-3e71-a445-6cddb2b62ef3 | -8.03968 | -47.40075 | 2025-10-29 12:19:00 | TERRA_M-T | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 8.8 |
| 71486c6e-c785-30d5-99c4-77f5b45ae069 | -13.06341 | -43.02419 | 2025-10-29 12:19:00 | TERRA_M-T | PARATINGA | BAHIA | Brasil | 2923704 | 29 | 33 | nan | nan | nan | Caatinga | 156.6 |
| ad5beece-6824-3f6d-905e-94b588e65b63 | -8.21126 | -47.30026 | 2025-10-29 12:19:00 | TERRA_M-T | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 11.1 |
| 2ae8017c-6bdc-34c0-a9ad-567847922332 | -12.17161 | -46.56342 | 2025-10-29 12:19:00 | TERRA_M-T | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 22.0 |
| 10b55483-8792-3847-b661-b70948c4c4a5 | -14.76282 | -49.6633 | 2025-10-29 12:19:00 | TERRA_M-T | GUARINOS | GOIÁS | Brasil | 5209457 | 52 | 33 | nan | nan | nan | Cerrado | 9.3 |
| c8bd1ed3-9759-348c-a3d7-87ee1aec8403 | -12.11092 | -47.15581 | 2025-10-29 12:19:00 | TERRA_M-T | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 39.8 |
| 8baf4fc4-af85-3c28-94cf-215d9d5f10b6 | -11.01947 | -47.85017 | 2025-10-29 12:19:00 | TERRA_M-T | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 15.4 |
| d3de5b71-f9a0-3683-98d1-be7a58f87e32 | -14.96173 | -48.19424 | 2025-10-29 12:19:00 | TERRA_M-T | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 18bc67c7-0ee5-3c24-86e5-d23c5bd4904b | -9.16671 | -46.27205 | 2025-10-29 12:19:00 | TERRA_M-T | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 1576bc53-016f-35e0-905f-b87f6a8a2533 | -9.9052 | -44.92658 | 2025-10-29 12:19:00 | TERRA_M-T | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 38.9 |
| 52300fcb-b4dc-34f3-ab7e-d18a2e6bf7f9 | -13.04411 | -48.46623 | 2025-10-29 12:19:00 | TERRA_M-T | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | 7.6 |
| 821b0e80-bb76-36df-b217-d5eaf7a7c9f3 | -11.06444 | -47.52964 | 2025-10-29 12:19:00 | TERRA_M-T | PINDORAMA DO TOCANTINS | TOCANTINS | Brasil | 1717008 | 17 | 33 | nan | nan | nan | Cerrado | 26.7 |
| 27faf081-e262-3572-83d5-84a074b7862b | -7.36964 | -47.63413 | 2025-10-29 12:19:00 | TERRA_M-T | FILADÉLFIA | TOCANTINS | Brasil | 1707702 | 17 | 33 | nan | nan | nan | Cerrado | 13.9 |
| a5a89fa0-b077-3ef0-af35-d28355544037 | -13.57402 | -49.58998 | 2025-10-29 12:19:00 | TERRA_M-T | PORANGATU | GOIÁS | Brasil | 5218003 | 52 | 33 | nan | nan | nan | Cerrado | 10.1 |
| 84de559c-76bb-31f2-97ac-7bbf0474cf73 | -10.29433 | -47.30035 | 2025-10-29 12:19:00 | TERRA_M-T | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 12.5 |
| 4194c140-6aa3-34f0-afbb-c0147ea40882 | -10.65595 | -48.00389 | 2025-10-29 12:19:00 | TERRA_M-T | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 39.2 |
| 4befc88e-c131-3a9e-914a-a5b0e1858630 | -10.89034 | -47.58663 | 2025-10-29 12:19:00 | TERRA_M-T | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 07316498-149e-3c27-9188-10c781625eb7 | -14.4277 | -47.85818 | 2025-10-29 12:19:00 | TERRA_M-T | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 38.0 |
| 8d7c317e-857c-368e-8d87-62adaf59f40e | -7.3621 | -47.62403 | 2025-10-29 12:19:00 | TERRA_M-T | FILADÉLFIA | TOCANTINS | Brasil | 1707702 | 17 | 33 | nan | nan | nan | Cerrado | 29.6 |
| 66ef9735-51f2-379f-8163-24a3dd75e304 | -10.76462 | -47.88779 | 2025-10-29 12:19:00 | TERRA_M-T | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 12.5 |
| 9a0b4fa2-70df-3b79-bfd6-389577899a21 | -11.41281 | -51.38885 | 2025-10-29 12:19:00 | TERRA_M-T | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 9.5 |
| fdbad5fa-d897-3501-a6dd-2222e1b674fd | -9.90807 | -44.89628 | 2025-10-29 12:19:00 | TERRA_M-T | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 16.7 |
| d111d42b-c97b-30a6-ae35-8e127f45a8d3 | -10.65723 | -47.99493 | 2025-10-29 12:19:00 | TERRA_M-T | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 10.8 |
| cd29fde6-b028-373f-a5d2-390a360d1bae | -11.57841 | -47.9381 | 2025-10-29 12:19:00 | TERRA_M-T | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 42.0 |
| 8f7f2a16-f1db-36b4-95ec-7fcb5fca1761 | -8.36312 | -47.26329 | 2025-10-29 12:19:00 | TERRA_M-T | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 16.3 |
| ae44a7c8-67bc-3d13-a5c7-1db9396bd86e | -9.2296 | -46.347 | 2025-10-29 12:19:00 | TERRA_M-T | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 61.0 |
| 645423c1-17d4-33d2-b395-05e260d01715 | -12.17926 | -46.72088 | 2025-10-29 12:19:00 | TERRA_M-T | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 31.7 |
| 4d196d48-6124-3cc1-b051-b1b5678e92ef | -7.49887 | -46.26728 | 2025-10-29 12:19:00 | TERRA_M-T | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 43.0 |
| 4258d707-7f52-3efe-bbec-3d81dbb45caf | -10.42684 | -44.99553 | 2025-10-29 12:19:00 | TERRA_M-T | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 109.1 |
| 804ead51-1897-3722-833e-ec2df248bafa | -16.10546 | -49.44624 | 2025-10-29 12:19:00 | TERRA_M-T | SANTA ROSA DE GOIÁS | GOIÁS | Brasil | 5219506 | 52 | 33 | nan | nan | nan | Cerrado | 53.2 |
| 100a9579-9366-315e-958a-9b7eca749313 | -11.5873 | -47.93937 | 2025-10-29 12:19:00 | TERRA_M-T | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 79.8 |
| 9484ee12-b441-38af-ae4f-87f6481bfc01 | -13.58884 | -48.526 | 2025-10-29 12:19:00 | TERRA_M-T | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 10.1 |
| a248a1e5-1dcc-3cac-86c9-577f9b300736 | -14.23394 | -48.12748 | 2025-10-29 12:19:00 | TERRA_M-T | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 10.2 |
| ae62e22f-35c9-35f6-a1cb-2a9f0e37c155 | -11.02076 | -47.84103 | 2025-10-29 12:19:00 | TERRA_M-T | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 19.4 |
| d53909b5-cd2f-3d7d-b20a-34dd1827f48c | -9.50672 | -46.93579 | 2025-10-29 12:19:00 | TERRA_M-T | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 24.2 |
| 8f715d2e-6fcd-3e9e-8cb9-4bd498b586fa | -8.19024 | -44.45939 | 2025-10-29 12:19:00 | TERRA_M-T | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 22.5 |
| be984d11-b980-36d0-896d-f610d76a2721 | -10.5387 | -47.73278 | 2025-10-29 12:19:00 | TERRA_M-T | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 7e2dd89a-3db4-3543-96ee-610305ab1ccb | -11.58473 | -47.95755 | 2025-10-29 12:19:00 | TERRA_M-T | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 13.1 |
| 080fc1f3-1df7-3ab2-822f-f161d652ee08 | -14.98846 | -47.86548 | 2025-10-29 12:19:00 | TERRA_M-T | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 18.8 |


[Clique aqui para ver as próximas entradas](README85.md)
