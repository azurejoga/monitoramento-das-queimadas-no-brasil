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

## Dados Diários - Página 59

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 7bc66ff7-6654-3cc5-acb1-cec2ee694422 | -8.93102 | -46.21045 | 2025-09-17 12:36:00 | TERRA_M-T | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 31.2 |
| 066a5a59-a62e-391b-8f89-7992962767c9 | -8.9586 | -46.32631 | 2025-09-17 12:36:00 | TERRA_M-T | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 64.9 |
| 92215ead-c18f-33f0-bdb1-24a0190935f0 | -9.0461 | -44.88888 | 2025-09-17 12:36:00 | TERRA_M-T | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 54.2 |
| 1d692c92-f460-324d-9ae5-096fc62f6a2b | -13.03287 | -47.95304 | 2025-09-17 12:36:00 | TERRA_M-T | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 14.1 |
| 12c43d0d-b0db-3f13-b167-4689ad3f08ef | -8.68016 | -46.35818 | 2025-09-17 12:36:00 | TERRA_M-T | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 32.4 |
| 4b7356cd-44ee-3820-a2fc-947d68dcf0db | -7.57498 | -44.58069 | 2025-09-17 12:36:00 | TERRA_M-T | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 39.6 |
| 47dd20a9-3b3a-30ec-abd2-003b56d6fd0d | -6.6069 | -45.59467 | 2025-09-17 12:36:00 | TERRA_M-T | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 170.8 |
| 9f9921a3-350f-3807-bcea-dbf224d7f513 | -8.8936 | -47.87658 | 2025-09-17 12:36:00 | TERRA_M-T | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 48.6 |
| 26f53a4f-2342-37be-bc3b-6c5f82734282 | -8.63932 | -46.43185 | 2025-09-17 12:36:00 | TERRA_M-T | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 25.5 |
| 285de1ba-915e-3c60-bc34-782a96c15810 | -8.79889 | -46.0446 | 2025-09-17 12:36:00 | TERRA_M-T | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 32.0 |
| 6c03f32c-98d2-3d66-921c-e516cb9a1066 | -12.12163 | -47.55631 | 2025-09-17 12:36:00 | TERRA_M-T | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 27.0 |
| d34fd96d-dc70-32b6-9a32-829f6c4b27b9 | -9.06751 | -44.93705 | 2025-09-17 12:36:00 | TERRA_M-T | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 39.9 |
| 3ea5ed63-13f6-353a-beb9-21d64eb1b35f | -13.3236 | -48.74674 | 2025-09-17 12:36:00 | TERRA_M-T | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | 49.8 |
| 7b3d7ee7-5b44-3174-a86f-7826d0dc719e | -8.96079 | -46.30896 | 2025-09-17 12:36:00 | TERRA_M-T | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 252.8 |
| 9a8d5ffd-0337-318f-9099-e952f68ae6ce | -8.98912 | -46.27836 | 2025-09-17 12:36:00 | TERRA_M-T | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 543.0 |
| b726d504-c121-3e68-9fd1-f51ad489ee6b | -12.0063 | -46.67555 | 2025-09-17 12:36:00 | TERRA_M-T | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 29.0 |
| 5436b008-087e-3e4e-93bb-27efaf15241b | -12.7054 | -47.73445 | 2025-09-17 12:36:00 | TERRA_M-T | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 13.4 |
| 5c7b88f4-3ca7-30e7-9316-d94cb1129cbc | -12.69695 | -45.29083 | 2025-09-17 12:36:00 | TERRA_M-T | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 84.8 |
| 54afb27a-4cb7-311b-8615-1de402b5c867 | -11.60459 | -46.95602 | 2025-09-17 12:36:00 | TERRA_M-T | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 15.2 |
| 9c2f79b7-214c-33b5-8003-8062be85e026 | -9.12543 | -48.1216 | 2025-09-17 12:36:00 | TERRA_M-T | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | 47.9 |
| bc0b3a4e-29a9-317c-acb6-f00d2b1413d8 | -7.89233 | -48.17881 | 2025-09-17 12:36:00 | TERRA_M-T | PALMEIRANTE | TOCANTINS | Brasil | 1715705 | 17 | 33 | nan | nan | nan | Cerrado | 42.3 |
| 0427a5a8-4c97-3bef-9461-ecb5bc8ec266 | -12.45171 | -49.74051 | 2025-09-17 12:36:00 | TERRA_M-T | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 9.2 |
| 8b3a8ca1-56b1-3886-b4de-ae993775757d | -10.95828 | -47.34486 | 2025-09-17 12:36:00 | TERRA_M-T | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 20.0 |
| b7bff481-362d-3f0a-8557-d1dd76a705e2 | -11.21675 | -47.3816 | 2025-09-17 12:36:00 | TERRA_M-T | PINDORAMA DO TOCANTINS | TOCANTINS | Brasil | 1717008 | 17 | 33 | nan | nan | nan | Cerrado | 45.1 |
| 49e55468-24e9-3257-9f02-a3501a7bdb7b | -8.27098 | -47.31364 | 2025-09-17 12:36:00 | TERRA_M-T | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 14.3 |
| c87b9344-c98a-30f6-8741-d162f43909ff | -10.31337 | -46.65716 | 2025-09-17 12:36:00 | TERRA_M-T | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 24.0 |
| 8021d895-ec74-30d7-b7f6-be498f2b50b8 | -11.18197 | -50.64661 | 2025-09-17 12:36:00 | TERRA_M-T | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 8.3 |
| d1948875-fc7d-3aa4-8d8a-b03cc4dd176e | -8.41516 | -45.7616 | 2025-09-17 12:36:00 | TERRA_M-T | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 30.2 |
| e5072c6b-b180-3f4e-9724-ec72630fea7b | -12.72045 | -47.98128 | 2025-09-17 12:36:00 | TERRA_M-T | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 23.6 |
| 85382540-aab1-383d-9a87-2bad27a8acb2 | -8.43931 | -47.67965 | 2025-09-17 12:36:00 | TERRA_M-T | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 27.4 |
| b5217688-8cd0-3458-9031-96653db6a8d0 | -12.00982 | -46.68248 | 2025-09-17 12:36:00 | TERRA_M-T | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 60.9 |
| 544730a6-3bed-3ab2-bfb2-b6a25a31472c | -12.68897 | -45.29654 | 2025-09-17 12:36:00 | TERRA_M-T | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 145.1 |
| e13bb475-9938-323b-add2-9c757f3278dc | -8.94044 | -45.53577 | 2025-09-17 12:36:00 | TERRA_M-T | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 152.9 |
| be814e1d-09ba-38de-8248-6aaa2a521bdf | -9.07359 | -50.31182 | 2025-09-17 12:36:00 | TERRA_M-T | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 8.0 |
| 44472d4d-b5ec-321d-9029-e980e219608d | -12.73899 | -48.01335 | 2025-09-17 12:36:00 | TERRA_M-T | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 186.5 |
| 48b79669-49c3-3e82-96da-54834858e632 | -11.81374 | -47.90807 | 2025-09-17 12:36:00 | TERRA_M-T | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 12.6 |
| 903ab72c-dc62-3a9a-8cce-eb2f305e1f00 | -7.06542 | -44.34737 | 2025-09-17 12:36:00 | TERRA_M-T | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 46.8 |
| 9cca2e5e-7ec6-3621-95f5-ebb0ab8a8895 | -12.06423 | -46.54216 | 2025-09-17 12:36:00 | TERRA_M-T | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 15.1 |
| 75e2c967-249b-3036-9e1c-71ca2fc12f04 | -8.65566 | -46.45637 | 2025-09-17 12:36:00 | TERRA_M-T | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 104.6 |
| 9f5029cb-96f3-3841-af7d-64b2840e78e9 | -12.74111 | -48.00524 | 2025-09-17 12:36:00 | TERRA_M-T | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 50.5 |
| 57c46f96-87ad-3d6c-adfe-919c5dd62f76 | -9.03512 | -44.90381 | 2025-09-17 12:36:00 | TERRA_M-T | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 28.4 |
| 04617872-5b4c-380a-9914-9b7f8a6fe85e | -13.22773 | -47.29241 | 2025-09-17 12:36:00 | TERRA_M-T | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 25.3 |
| c4aa74dc-8e82-3891-83df-6e53cb0849b2 | -12.70931 | -47.97982 | 2025-09-17 12:36:00 | TERRA_M-T | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 18.6 |
| 4aa2635b-471d-3d6d-9cb2-c526263a5b51 | -8.54654 | -47.56337 | 2025-09-17 12:36:00 | TERRA_M-T | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 21.9 |
| 6e25b1e6-a376-3653-904f-4b7b97b20a94 | -8.90141 | -46.15351 | 2025-09-17 12:36:00 | TERRA_M-T | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 29.7 |
| a5e819f9-fa45-3049-b087-a0cab475125e | -8.41757 | -45.74281 | 2025-09-17 12:36:00 | TERRA_M-T | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 51.3 |
| 8f221883-ad8e-3edd-ab51-90ae97c5be3d | -13.96694 | -44.93275 | 2025-09-17 12:36:00 | TERRA_M-T | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 183.6 |
| a2241c62-c379-358a-9e71-ed62b8264fea | -7.59929 | -44.56675 | 2025-09-17 12:36:00 | TERRA_M-T | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 31.6 |
| c38d55fe-5ef9-3554-9490-6bfdf908a635 | -7.58848 | -44.58249 | 2025-09-17 12:36:00 | TERRA_M-T | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 81.3 |
| e9849d08-37b9-3c0d-a17f-16e745e65c8e | -10.16386 | -52.62393 | 2025-09-17 12:36:00 | TERRA_M-T | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 6.5 |
| e6a55b24-257c-334f-a703-659f4b7cab04 | -11.5811 | -48.28953 | 2025-09-17 12:36:00 | TERRA_M-T | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 18.6 |
| 37692bd9-6632-35ec-abe6-77ecde7353ac | -12.09419 | -48.73838 | 2025-09-17 12:36:00 | TERRA_M-T | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 45.6 |
| 5b6a2faa-f118-3f8a-b4d2-af1e8869e81c | -11.58285 | -48.27607 | 2025-09-17 12:36:00 | TERRA_M-T | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 24.8 |
| edb65e07-5043-3516-abd1-0689852b687d | -12.00172 | -46.71163 | 2025-09-17 12:36:00 | TERRA_M-T | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 22.1 |
| 9661741f-1722-3091-9106-c75d50883308 | -8.9488 | -46.30733 | 2025-09-17 12:36:00 | TERRA_M-T | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 92.6 |
| 4111e755-1411-323a-8a44-09f9703e8658 | -8.90367 | -46.13571 | 2025-09-17 12:36:00 | TERRA_M-T | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 19.2 |
| b9aa3068-95df-3ea5-8654-361b825f5274 | -11.20533 | -47.38023 | 2025-09-17 12:36:00 | TERRA_M-T | PINDORAMA DO TOCANTINS | TOCANTINS | Brasil | 1717008 | 17 | 33 | nan | nan | nan | Cerrado | 169.9 |
| 09ef48c0-bdfc-3616-a2f7-96aa22b77bf0 | -12.28876 | -50.1315 | 2025-09-17 12:36:00 | TERRA_M-T | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 18.1 |
| 967eeb4b-019f-3d85-bbfa-530c1c240e9d | -10.07331 | -48.18527 | 2025-09-17 12:36:00 | TERRA_M-T | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 25.3 |
| 6758443f-6f99-3412-8601-a5ef052e147c | -8.68562 | -46.4099 | 2025-09-17 12:36:00 | TERRA_M-T | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 50.1 |
| 80206437-38a1-36e2-84cc-daad7eb30473 | -13.03251 | -47.95887 | 2025-09-17 12:36:00 | TERRA_M-T | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 14.4 |
| 82cf344e-2e5b-3d14-b7c2-85b5fe7eb560 | -11.22855 | -51.43399 | 2025-09-17 12:36:00 | TERRA_M-T | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 16.8 |
| 7108ddfa-8000-31be-ba42-581d024f2861 | -12.82317 | -44.98901 | 2025-09-17 12:36:00 | TERRA_M-T | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 27.7 |
| 64d0075b-79c1-3eb4-8aad-9a8540445ef3 | -8.56993 | -47.55264 | 2025-09-17 12:36:00 | TERRA_M-T | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 12.6 |
| 50d606dd-7f61-3842-985b-abf07ad60596 | -9.47311 | -48.26844 | 2025-09-17 12:36:00 | TERRA_M-T | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 18.8 |
| 54829dee-86f7-3071-9856-bfb1d2cf7982 | -9.13002 | -44.87619 | 2025-09-17 12:36:00 | TERRA_M-T | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 122.4 |
| 9e7c533e-72df-3200-a187-21c19a8abede | -11.01888 | -48.91834 | 2025-09-17 12:36:00 | TERRA_M-T | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 22.2 |
| 291699bf-0558-3f15-a2a5-3420d0076ae2 | -8.43142 | -47.38261 | 2025-09-17 12:36:00 | TERRA_M-T | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 9.7 |
| d9a45dbf-ea29-3436-8012-0cef6ee8962b | -9.13773 | -44.88388 | 2025-09-17 12:36:00 | TERRA_M-T | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 111.4 |
| bdba93d3-24d5-3a2e-ba8e-18df2f42d766 | -11.65128 | -46.59102 | 2025-09-17 12:36:00 | TERRA_M-T | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 32.7 |
| 988a713d-aa21-3f25-8a07-5ae5f913bf1b | -8.43754 | -47.69296 | 2025-09-17 12:36:00 | TERRA_M-T | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 23.3 |
| 7fe9dee5-5347-34e4-af66-f064ff827533 | -7.88534 | -48.15327 | 2025-09-17 12:36:00 | TERRA_M-T | PALMEIRANTE | TOCANTINS | Brasil | 1715705 | 17 | 33 | nan | nan | nan | Cerrado | 35.9 |
| 818e6ede-1f1a-3d5f-bdea-86ce82be976f | -8.91888 | -46.20927 | 2025-09-17 12:36:00 | TERRA_M-T | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 18.2 |
| 4a021dfc-1871-3967-97b5-429a15f36e6e | -8.15104 | -46.74352 | 2025-09-17 12:36:00 | TERRA_M-T | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 45.0 |
| a4024ab6-d379-34db-af7d-5eb39dbd876e | -12.73935 | -48.01975 | 2025-09-17 12:36:00 | TERRA_M-T | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 111.0 |
| dc2767e6-5506-393f-9e28-a38045659fd1 | -12.70043 | -44.89114 | 2025-09-17 12:36:00 | TERRA_M-T | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 203.5 |
| 8bb2de8c-9a1b-3921-bfff-a795054c91cd | -12.70167 | -47.76503 | 2025-09-17 12:36:00 | TERRA_M-T | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 22.5 |
| 9664319d-b0ed-3c6a-a8c5-45791560b305 | -12.39192 | -51.41324 | 2025-09-17 12:36:00 | TERRA_M-T | BOM JESUS DO ARAGUAIA | MATO GROSSO | Brasil | 5101852 | 51 | 33 | nan | nan | nan | Cerrado | 19.7 |
| db3c6622-090f-3d37-a3d2-9685701b3e0d | -13.96991 | -44.90561 | 2025-09-17 12:36:00 | TERRA_M-T | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 71.4 |
| f76a933a-e082-33db-897b-3c8b7cdf0f78 | -8.43345 | -47.3893 | 2025-09-17 12:36:00 | TERRA_M-T | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 10.6 |
| a71adf95-060a-36f9-8c76-fde3617f0656 | -8.94366 | -46.30051 | 2025-09-17 12:36:00 | TERRA_M-T | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 97.7 |
| 08b2048a-f0eb-3511-8902-b121eafe7e45 | -7.40399 | -50.00362 | 2025-09-17 12:36:00 | TERRA_M-T | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 61.7 |
| 066bf8a8-bd58-370e-932f-01cf0f8ad9fd | -8.89534 | -47.86371 | 2025-09-17 12:36:00 | TERRA_M-T | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 16.8 |
| f18a05bf-b20f-3092-8e4d-0d96bbb3de3c | -8.55552 | -47.5783 | 2025-09-17 12:36:00 | TERRA_M-T | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 10.8 |
| b6edcef3-010b-3e15-a216-b91cfcff89e0 | -9.1404 | -44.86197 | 2025-09-17 12:36:00 | TERRA_M-T | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 37.7 |
| 1e34b223-e971-3b5a-aa4e-31743b6116ce | -12.004 | -46.69366 | 2025-09-17 12:36:00 | TERRA_M-T | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 182.2 |
| 4a3646e7-ff0f-3375-aec2-41d198c06acc | -12.09251 | -48.75111 | 2025-09-17 12:36:00 | TERRA_M-T | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 19.5 |
| ab02477d-84dc-3a5c-bb65-0387b1a8fe35 | -8.94324 | -45.51016 | 2025-09-17 12:36:00 | TERRA_M-T | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 93.9 |
| 5e999d95-2554-3d2f-af84-df3d597496c0 | -7.57785 | -44.55843 | 2025-09-17 12:36:00 | TERRA_M-T | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 27.1 |
| 89438c60-bdc6-3566-944a-55dea4125b0c | -7.4572 | -46.18278 | 2025-09-17 12:36:00 | TERRA_M-T | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 14.8 |
| 7392332b-cf85-3f72-b40a-1801c55be073 | -8.18727 | -44.78877 | 2025-09-17 12:36:00 | TERRA_M-T | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 29.1 |
| 90b09b0c-470d-344a-a0e6-a1a48dd67f44 | -11.40713 | -52.51615 | 2025-09-17 12:36:00 | TERRA_M-T | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 6.8 |
| 3b1c9302-c708-39a9-a5d7-1749afb33668 | -8.69202 | -46.35999 | 2025-09-17 12:36:00 | TERRA_M-T | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 24.5 |
| e770c4d9-0dff-3c77-90a2-0a7fdbb8435d | -9.00634 | -45.32009 | 2025-09-17 12:36:00 | TERRA_M-T | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 40.8 |
| 19069e1b-8fa3-3a07-8953-958b68a89089 | -8.57891 | -47.56751 | 2025-09-17 12:36:00 | TERRA_M-T | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 210.0 |
| c1a919b9-9984-3a80-ad2a-ecd93df05d3e | -9.12714 | -48.10886 | 2025-09-17 12:36:00 | TERRA_M-T | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | 66.4 |
| 6486f207-dbd4-3e29-acfe-cc05af4266c8 | -7.68362 | -46.63593 | 2025-09-17 12:36:00 | TERRA_M-T | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 23.4 |
| 98918b79-1773-3df7-b327-82bee500644a | -11.20338 | -47.39582 | 2025-09-17 12:36:00 | TERRA_M-T | PINDORAMA DO TOCANTINS | TOCANTINS | Brasil | 1717008 | 17 | 33 | nan | nan | nan | Cerrado | 152.0 |
| c20b9280-b330-38e4-b500-f0ec66b748fc | -10.32958 | -46.62505 | 2025-09-17 12:36:00 | TERRA_M-T | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 29.0 |
| d85af549-4cf8-3d17-9b51-88917eedd4b7 | -13.32193 | -48.75998 | 2025-09-17 12:36:00 | TERRA_M-T | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | 11.1 |


[Clique aqui para ver as próximas entradas](README60.md)
