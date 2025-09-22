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

## Dados Diários - Página 48

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 2e60c040-e6fc-365e-946d-af431301f60b | -9.9814 | -45.8101 | 2025-09-22 14:10:00 | GOES-19 | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 59.5 |
| 4c02c237-4127-3bb1-9746-fe2cfeb70395 | -12.6663 | -45.1385 | 2025-09-22 14:10:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 130.2 |
| f44dab24-75da-3bb4-ba5b-92609839d2cd | -16.4711 | -55.1301 | 2025-09-22 14:10:00 | GOES-19 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 87.6 |
| 47b1c124-7cab-3031-8e70-75e62bfd033c | -11.5237 | -43.587 | 2025-09-22 14:10:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 92.0 |
| 24a526c7-dc5e-3efc-b9ad-905d19e60a82 | -14.8361 | -45.137 | 2025-09-22 14:10:00 | GOES-19 | BONITO DE MINAS | MINAS GERAIS | Brasil | 3108255 | 31 | 33 | nan | nan | nan | Cerrado | 83.1 |
| f86d57b5-056a-392e-9a25-9273995e8855 | -11.9108 | -43.4081 | 2025-09-22 14:10:00 | GOES-19 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 106.2 |
| 37ffa3f7-85ba-3cc6-86b4-180729d4883a | -11.4674 | -43.5248 | 2025-09-22 14:10:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 93.4 |
| 43e9e21d-2e2f-3488-a2f0-703e3e4f2252 | -10.3572 | -46.0585 | 2025-09-22 14:10:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 228.4 |
| 5108a440-4d36-3987-97b3-15011d969095 | -11.5233 | -43.6107 | 2025-09-22 14:10:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 89.7 |
| 7931637e-4447-3f8b-b54d-f1c58105b587 | -12.1348 | -44.7809 | 2025-09-22 14:10:00 | GOES-19 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 125.9 |
| afcd32da-c4f3-32b5-98c6-f646305f91d0 | -12.1353 | -44.7576 | 2025-09-22 14:10:00 | GOES-19 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 96.6 |
| faeb6040-6d0b-3aad-9741-bda978b8792b | -5.5585 | -42.1269 | 2025-09-22 14:10:00 | GOES-19 | ALTO LONGÁ | PIAUÍ | Brasil | 2200301 | 22 | 33 | nan | nan | nan | Caatinga | 107.0 |
| 389d844e-a6bf-3bf4-bb3e-ee690ea93e27 | -14.4917 | -44.8496 | 2025-09-22 14:10:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 114.1 |
| 864d660e-5145-30f5-8f2d-5c55d55f314a | -12.1156 | -44.7839 | 2025-09-22 14:10:00 | GOES-19 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 125.8 |
| 3bbd567e-2407-3fd5-89a1-88682d267229 | -8.9592 | -44.4667 | 2025-09-22 14:10:00 | GOES-19 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 92.9 |
| 50f73fc5-5f0c-3a9c-80a2-b4718eafda8a | -14.9693 | -44.4297 | 2025-09-22 14:10:00 | GOES-19 | ITACARAMBI | MINAS GERAIS | Brasil | 3132107 | 31 | 33 | nan | nan | nan | Cerrado | 75.8 |
| 67955454-8cf6-31aa-8357-affd7a827285 | -14.4259 | -60.2984 | 2025-09-22 14:10:00 | GOES-19 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 130.1 |
| ff20d201-d6bd-3827-bd5c-31873ab6e82c | -11.9493 | -43.4019 | 2025-09-22 14:20:00 | GOES-19 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 115.8 |
| 428a6ae3-bcdc-31b9-90ac-e30eb6fcbe72 | -12.753 | -47.7364 | 2025-09-22 14:20:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 91.6 |
| 92271c18-4b43-3590-bbda-05f699da3208 | -14.8479 | -45.4846 | 2025-09-22 14:20:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 120.1 |
| 434c9c3a-71d1-3a18-a2d9-3b26d4359fd2 | -14.9699 | -44.406 | 2025-09-22 14:20:00 | GOES-19 | ITACARAMBI | MINAS GERAIS | Brasil | 3132107 | 31 | 33 | nan | nan | nan | Cerrado | 141.6 |
| ae09c19a-ebae-3860-a7ca-7e270651a832 | -11.5233 | -43.6107 | 2025-09-22 14:20:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 166.0 |
| 360abed6-253a-3360-b39d-63fac1df0113 | -5.5585 | -42.1269 | 2025-09-22 14:20:00 | GOES-19 | ALTO LONGÁ | PIAUÍ | Brasil | 2200301 | 22 | 33 | nan | nan | nan | Caatinga | 107.2 |
| 5db49a1c-1d67-379e-aec0-ab60a3f0e5dd | -12.7341 | -47.7168 | 2025-09-22 14:20:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 93.8 |
| 78d9241c-ac3e-33b7-8ec7-a98984ddcf63 | -6.1878 | -41.2097 | 2025-09-22 14:20:00 | GOES-19 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 99.1 |
| 17416c32-9287-3727-8ceb-3d950bb02272 | -12.0767 | -44.8131 | 2025-09-22 14:20:00 | GOES-19 | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 95.7 |
| bcd76825-5fd4-381d-8fbd-e1eaef5300bc | -14.9693 | -44.4297 | 2025-09-22 14:20:00 | GOES-19 | ITACARAMBI | MINAS GERAIS | Brasil | 3132107 | 31 | 33 | nan | nan | nan | Cerrado | 69.0 |
| 3b1dfbf8-268e-367d-92b2-da3b5fd0d62d | -10.3572 | -46.0585 | 2025-09-22 14:20:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 123.3 |
| e1f9060c-b947-37f5-841d-de0d3aa16565 | -5.3711 | -42.0937 | 2025-09-22 14:20:00 | GOES-19 | ALTO LONGÁ | PIAUÍ | Brasil | 2200301 | 22 | 33 | nan | nan | nan | Caatinga | 104.0 |
| 90162a91-1285-3387-8809-b396e056567f | -11.5045 | -43.59 | 2025-09-22 14:20:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 102.6 |
| 4d81b8c1-3849-3d33-b437-6fa6860016e1 | -12.7333 | -47.7615 | 2025-09-22 14:20:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 84.1 |
| 6fdebc2c-00a7-3239-96d7-edea6e7c2f93 | -8.2803 | -44.3801 | 2025-09-22 14:20:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 400.4 |
| 2d217dc6-9028-331b-a2ef-a5fbf07f9a8d | -12.4361 | -45.1052 | 2025-09-22 14:20:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 64.9 |
| 28b9c6cd-fbd9-3b07-bf0b-0cc4e5f3dd53 | -14.8484 | -45.4613 | 2025-09-22 14:20:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 125.4 |
| 1b2d4225-2892-3cac-9cda-d10220a2d7b2 | -4.1382 | -41.5557 | 2025-09-22 14:20:00 | GOES-19 | BRASILEIRA | PIAUÍ | Brasil | 2201960 | 22 | 33 | nan | nan | nan | Caatinga | 88.2 |
| 2afb2da9-1930-303d-ae9a-d53125b02d11 | -12.6474 | -45.1183 | 2025-09-22 14:20:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 129.5 |
| a195ee13-fe03-305e-b6e3-e257d2688f4c | -4.8638 | -42.2252 | 2025-09-22 14:20:00 | GOES-19 | CAMPO MAIOR | PIAUÍ | Brasil | 2202208 | 22 | 33 | nan | nan | nan | Caatinga | 91.5 |
| b0e60197-7991-3c96-a969-2f54c22e33f8 | -15.4459 | -55.9989 | 2025-09-22 14:20:00 | GOES-19 | CUIABÁ | MATO GROSSO | Brasil | 5103403 | 51 | 33 | nan | nan | nan | Cerrado | 81.5 |
| b3371d56-1ae3-3cef-883d-27fec8149644 | -11.9301 | -43.405 | 2025-09-22 14:20:00 | GOES-19 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 126.7 |
| 26f3cd53-c5a7-3419-b2ae-f0231611c545 | -8.2614 | -44.3821 | 2025-09-22 14:20:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 95.9 |
| d4041da0-a239-38ae-a85c-97bf9dad10fe | -11.5237 | -43.587 | 2025-09-22 14:20:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 199.1 |
| 7f14fcb1-4f70-3822-a22e-fe005491228d | -9.086 | -44.8663 | 2025-09-22 14:20:00 | GOES-19 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 61.5 |
| 0359d50b-1d10-38c7-be91-27dcb9b053cf | -5.5773 | -42.1255 | 2025-09-22 14:20:00 | GOES-19 | ALTO LONGÁ | PIAUÍ | Brasil | 2200301 | 22 | 33 | nan | nan | nan | Caatinga | 106.4 |
| 734687a0-6a6a-3049-b611-f6b690393771 | -11.9296 | -43.4288 | 2025-09-22 14:20:00 | GOES-19 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 158.8 |
| 1b735d77-aa84-3b2b-8f90-961bcbb316eb | -11.6249 | -52.8416 | 2025-09-22 14:20:00 | GOES-19 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 142.8 |
| 89cbfc51-2939-33c2-86d9-09c6e5ca503e | -5.7795 | -42.5837 | 2025-09-22 14:20:00 | GOES-19 | OLHO D'ÁGUA DO PIAUÍ | PIAUÍ | Brasil | 2207108 | 22 | 33 | nan | nan | nan | Caatinga | 71.3 |
| eb0971c2-eee0-3faf-91cc-0c6bcad16fe5 | -12.6281 | -45.1213 | 2025-09-22 14:20:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 70.1 |
| 1a070629-905d-3768-ac00-df09c2cbc847 | -12.7149 | -47.7195 | 2025-09-22 14:20:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 98.1 |
| 22363d91-b7e1-3c5d-99c2-b6406ef4c58c | -5.5771 | -42.1493 | 2025-09-22 14:20:00 | GOES-19 | ALTO LONGÁ | PIAUÍ | Brasil | 2200301 | 22 | 33 | nan | nan | nan | Caatinga | 100.7 |
| 102859cc-d880-38d3-8efb-39fc8a2f45b9 | -14.8675 | -45.481 | 2025-09-22 14:20:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 171.3 |
| 582ce6e3-ebd9-3d9a-b636-da89ee81deca | -11.6247 | -52.8624 | 2025-09-22 14:20:00 | GOES-19 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 119.2 |
| 8c300f34-11a9-32b0-997e-68eea1c94d82 | -14.4259 | -60.2984 | 2025-09-22 14:20:00 | GOES-19 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 127.7 |
| d7925c15-e810-3411-a34a-202777cd7d01 | -10.3568 | -46.0812 | 2025-09-22 14:20:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 102.7 |
| 8897c03c-d618-3636-a803-bf498e28a0eb | -10.5802 | -50.3148 | 2025-09-22 14:20:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 69.4 |
| dffd9acb-8dd9-3fe4-bc73-0ccfe14857f0 | -11.5041 | -43.6136 | 2025-09-22 14:20:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 99.1 |
| 3b478612-4027-3475-865b-4e30158f1d9c | -17.6831 | -44.0901 | 2025-09-22 14:20:00 | GOES-19 | JOAQUIM FELÍCIO | MINAS GERAIS | Brasil | 3136405 | 31 | 33 | nan | nan | nan | Cerrado | 100.8 |
| 8ceb09bf-8fd5-35cc-a7bc-adfd0fb721bd | -7.4503 | -46.1647 | 2025-09-22 14:20:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 57.8 |
| a9382533-012c-3c39-9ec5-d3b57c850412 | -5.5583 | -42.1507 | 2025-09-22 14:20:00 | GOES-19 | ALTO LONGÁ | PIAUÍ | Brasil | 2200301 | 22 | 33 | nan | nan | nan | Caatinga | 102.5 |
| 7742a17f-106f-3dc2-91b5-634bc315352c | -14.4721 | -44.8532 | 2025-09-22 14:20:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 144.1 |
| 2558821a-72cc-3270-b1da-deaa8195ea85 | -11.6436 | -52.8605 | 2025-09-22 14:20:00 | GOES-19 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 203.6 |
| 5ca838a2-7968-30b1-9324-5b3584d91720 | -7.5818 | -44.4971 | 2025-09-22 14:20:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 65.1 |
| a96ec108-04c1-3a8a-939d-26be562d4b5a | -5.5959 | -42.1478 | 2025-09-22 14:20:00 | GOES-19 | ALTO LONGÁ | PIAUÍ | Brasil | 2200301 | 22 | 33 | nan | nan | nan | Caatinga | 96.5 |
| b2b0ed2a-836c-345a-908e-6857bc68a1a9 | -10.2621 | -46.0703 | 2025-09-22 14:20:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 63.2 |
| f2974b96-7991-3fea-b1a4-2a805460f1f2 | -18.5983 | -45.0287 | 2025-09-22 14:20:00 | GOES-19 | FELIXLÂNDIA | MINAS GERAIS | Brasil | 3125705 | 31 | 33 | nan | nan | nan | Cerrado | 394.2 |
| 3406ceb4-cf5b-3426-ae1f-4380e8f2c15f | -11.7687 | -44.8826 | 2025-09-22 14:20:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 84.6 |
| b019f5d8-7bbb-3ba8-a8f9-36a2dea8643e | -11.6249 | -52.8416 | 2025-09-22 14:30:00 | GOES-19 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 137.8 |
| f5f57dc1-3fdf-30b1-8711-c6ce9bec292e | -8.2803 | -44.3801 | 2025-09-22 14:30:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 110.0 |
| fa834994-eeb4-3dd9-9ffa-78c0d38f5180 | -12.753 | -47.7364 | 2025-09-22 14:30:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 86.8 |
| 22e23e30-3b62-3b12-9230-feabead4e304 | -5.5771 | -42.1493 | 2025-09-22 14:30:00 | GOES-19 | ALTO LONGÁ | PIAUÍ | Brasil | 2200301 | 22 | 33 | nan | nan | nan | Caatinga | 104.9 |
| 6243c7a2-dde3-3def-8a0d-8fdc5206da0a | -14.4721 | -44.8532 | 2025-09-22 14:30:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 192.2 |
| 7c3b8c4d-4656-3777-a52b-686d3227a3ce | -12.3399 | -44.0946 | 2025-09-22 14:30:00 | GOES-19 | TABOCAS DO BREJO VELHO | BAHIA | Brasil | 2930907 | 29 | 33 | nan | nan | nan | Cerrado | 73.1 |
| c61c3ad7-1b02-32f2-8c3d-00feda630ddc | -10.4132 | -46.1194 | 2025-09-22 14:30:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 95.8 |
| 3712d496-14fc-320b-86b4-20d81f44c9bc | -12.647 | -45.1415 | 2025-09-22 14:30:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 71.0 |
| 9c0b2b2b-4996-38a6-b65c-2e6e73414be2 | -7.4503 | -46.1647 | 2025-09-22 14:30:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 60.5 |
| 103e3359-a25e-3159-865e-f629b239a058 | -4.5695 | -41.5047 | 2025-09-22 14:30:00 | GOES-19 | PEDRO II | PIAUÍ | Brasil | 2207900 | 22 | 33 | nan | nan | nan | Caatinga | 76.6 |
| 4b258969-b76c-341d-a956-b6c68dcbabc1 | -12.6663 | -45.1385 | 2025-09-22 14:30:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 178.2 |
| e1d20b08-f332-338b-81af-a2daae0e375c | -12.6474 | -45.1183 | 2025-09-22 14:30:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 115.4 |
| 66f0e92b-25ec-3a9e-8dc3-9a5132228d44 | -14.8484 | -45.4613 | 2025-09-22 14:30:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 520.7 |
| 4207daff-bb05-3dc4-abbd-1bf2e0082af7 | -11.7687 | -44.8826 | 2025-09-22 14:30:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 84.8 |
| 5fabf7d0-a0bb-3089-994e-a898660a4bd6 | -10.561 | -50.3381 | 2025-09-22 14:30:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 65.6 |
| fc592465-73af-3b43-8402-88c01bf1fa9e | -16.3198 | -43.0684 | 2025-09-22 14:30:00 | GOES-19 | GRÃO MOGOL | MINAS GERAIS | Brasil | 3127800 | 31 | 33 | nan | nan | nan | Cerrado | 81.4 |
| 349d0f73-8c9a-3eb6-8033-7913f7e39ea9 | -14.8479 | -45.4846 | 2025-09-22 14:30:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 360.1 |
| d2e895b4-3bde-37a7-8272-275521732fe2 | -10.5802 | -50.3148 | 2025-09-22 14:30:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 74.0 |
| 0e35dcae-0f7e-3097-ac2d-f30d57592b71 | -4.8638 | -42.2252 | 2025-09-22 14:30:00 | GOES-19 | CAMPO MAIOR | PIAUÍ | Brasil | 2202208 | 22 | 33 | nan | nan | nan | Caatinga | 94.4 |
| cc7e2f1a-9368-30c2-9ce4-e8e8aaefc8f7 | -17.5614 | -44.9092 | 2025-09-22 14:30:00 | GOES-19 | VÁRZEA DA PALMA | MINAS GERAIS | Brasil | 3170800 | 31 | 33 | nan | nan | nan | Cerrado | 145.8 |
| be58001b-bec9-3b11-9770-bd040cf835f6 | -6.1878 | -41.2097 | 2025-09-22 14:30:00 | GOES-19 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 100.3 |
| 09c43b1d-58f9-361a-b989-6d6ef26f9d2c | -14.8283 | -45.4882 | 2025-09-22 14:30:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 92.1 |
| 6b6971bc-d5f1-3fb5-a7c2-db77a354c8c9 | -10.3568 | -46.0812 | 2025-09-22 14:30:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 100.6 |
| 4df20a2f-eb05-32e5-8137-92dc61a74f29 | -5.5959 | -42.1478 | 2025-09-22 14:30:00 | GOES-19 | ALTO LONGÁ | PIAUÍ | Brasil | 2200301 | 22 | 33 | nan | nan | nan | Caatinga | 97.2 |
| 7ded4ef9-e6d1-3b00-b0e8-895278b3552a | -11.6436 | -52.8605 | 2025-09-22 14:30:00 | GOES-19 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 236.4 |
| 4df97466-2d10-3a6d-9631-cffe3477b5c9 | -12.2983 | -45.2881 | 2025-09-22 14:30:00 | GOES-19 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 77.3 |
| 8f95a53e-aa0e-3908-8436-c5f5450bc5eb | -8.2614 | -44.3821 | 2025-09-22 14:30:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 68.0 |
| 25cfd5fd-eb7e-3bff-b993-cd066394a9b0 | -10.3755 | -46.1015 | 2025-09-22 14:30:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 99.0 |
| 0a9c0cef-cee3-3b04-8084-9b9e4981b5ea | -12.4361 | -45.1052 | 2025-09-22 14:30:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 93.6 |
| 9b1d7c26-ab1f-37da-a43b-5d6e006875d1 | -5.5583 | -42.1507 | 2025-09-22 14:30:00 | GOES-19 | ALTO LONGÁ | PIAUÍ | Brasil | 2200301 | 22 | 33 | nan | nan | nan | Caatinga | 96.3 |
| a343ffd1-7729-3f79-aa81-47624938b517 | -14.8675 | -45.481 | 2025-09-22 14:30:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 377.9 |
| 0f314741-a040-3d15-9781-721463c2ad49 | -11.6247 | -52.8624 | 2025-09-22 14:30:00 | GOES-19 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 145.0 |
| 2ddd8df6-9d47-392c-852c-b39a4dc1d674 | -10.3572 | -46.0585 | 2025-09-22 14:30:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 117.3 |
| de510c62-4c4d-3736-87ba-c4b63c2be903 | -4.1382 | -41.5557 | 2025-09-22 14:30:00 | GOES-19 | BRASILEIRA | PIAUÍ | Brasil | 2201960 | 22 | 33 | nan | nan | nan | Caatinga | 98.2 |
| 8c9cb587-5607-319e-881a-993a7d0005d5 | -5.5773 | -42.1255 | 2025-09-22 14:30:00 | GOES-19 | ALTO LONGÁ | PIAUÍ | Brasil | 2200301 | 22 | 33 | nan | nan | nan | Caatinga | 104.7 |


[Clique aqui para ver as próximas entradas](README49.md)
