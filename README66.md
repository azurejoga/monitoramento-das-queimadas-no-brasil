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

## Dados Diários - Página 66

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 0aa44c14-8832-3cae-b0f2-a170c1c9e99d | -8.8415 | -46.2095 | 2025-09-27 13:50:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 100.7 |
| 2198421e-edd6-3452-91a7-8e68a978720e | -7.1571 | -45.5158 | 2025-09-27 13:50:00 | GOES-19 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 91.4 |
| 0ea38047-4081-3ce9-ab23-fb392efa42ca | -8.6442 | -43.9931 | 2025-09-27 13:50:00 | GOES-19 | CRISTINO CASTRO | PIAUÍ | Brasil | 2203107 | 22 | 33 | nan | nan | nan | Cerrado | 87.4 |
| 3addd621-5d7a-3818-bbd9-7728d0088cca | -3.8277 | -40.3373 | 2025-09-27 13:50:00 | GOES-19 | FORQUILHA | CEARÁ | Brasil | 2304350 | 23 | 33 | nan | nan | nan | Caatinga | 107.5 |
| fe3e9b58-7e92-360a-9881-d553ef646bab | -9.0422 | -46.7255 | 2025-09-27 13:50:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 210.8 |
| 6130e97f-ad24-38b7-80e8-67244c60e36f | -5.7225 | -42.659 | 2025-09-27 13:50:00 | GOES-19 | MIGUEL LEÃO | PIAUÍ | Brasil | 2206308 | 22 | 33 | nan | nan | nan | Caatinga | 82.2 |
| db4a1169-c9f3-3bf9-a79e-8206f028e800 | -5.7588 | -42.7976 | 2025-09-27 13:50:00 | GOES-19 | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 85.4 |
| 95dc36d1-3210-370b-bc98-83ee914ee8f9 | -7.7797 | -46.9149 | 2025-09-27 13:50:00 | GOES-19 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 119.3 |
| 795b65a4-fc31-3eb4-8425-fef42ca3e5a7 | -9.8781 | -47.7441 | 2025-09-27 13:50:00 | GOES-19 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 72.8 |
| 8cabe963-a835-302d-aeec-91bd91d3b0b8 | -11.3654 | -44.9645 | 2025-09-27 13:50:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 84.9 |
| 7024abb7-4146-32f7-be9a-627f2e93a316 | -9.9776 | -43.5727 | 2025-09-27 13:50:00 | GOES-19 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 74.1 |
| e223c5f0-e2b0-3ec6-a12f-0cb9309774bd | -11.3642 | -45.0339 | 2025-09-27 13:50:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 151.0 |
| df10c2e2-d7ac-3721-8306-a5960458d6e8 | -7.7609 | -46.9166 | 2025-09-27 13:50:00 | GOES-19 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 107.2 |
| 554330a1-8a7a-3091-aedc-8e2f345c0265 | -14.0191 | -56.0927 | 2025-09-27 13:50:00 | GOES-19 | NOVA MUTUM | MATO GROSSO | Brasil | 5106224 | 51 | 33 | nan | nan | nan | Cerrado | 73.5 |
| 5f6b27b2-5f66-3aa9-a500-1e195861e351 | -5.7585 | -42.8211 | 2025-09-27 13:50:00 | GOES-19 | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 91.2 |
| 9eb7db28-2950-3418-b2ce-0901597a3d41 | -7.6064 | -47.3278 | 2025-09-27 13:50:00 | GOES-19 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 71.1 |
| 1f296c56-43f3-3760-b81f-8a2fab248375 | -18.3049 | -57.0938 | 2025-09-27 13:50:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 75.7 |
| 810d210c-9e84-3ae9-8aa0-0a70c0b558e3 | -7.7558 | -47.3809 | 2025-09-27 13:50:00 | GOES-19 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 66.9 |
| 65c48640-6792-3b7b-9a2c-465377497808 | -11.385 | -44.9386 | 2025-09-27 13:50:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 115.8 |
| 79f33fa9-9d7e-3a59-bbb5-9ca0ba2ba7eb | -9.6159 | -47.5741 | 2025-09-27 13:50:00 | GOES-19 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 112.0 |
| b3e23d8c-214a-38fd-b56d-0d2499580ffd | -9.1753 | -46.6444 | 2025-09-27 13:50:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 71.5 |
| 0ce3247e-dabf-32e8-9a88-c0362cf24235 | -9.3514 | -47.6022 | 2025-09-27 13:50:00 | GOES-19 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 167.8 |
| c524d162-2d14-3aa6-afe6-0f57b4eaaa1a | -9.3511 | -47.6243 | 2025-09-27 13:50:00 | GOES-19 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 79.4 |
| 17092e87-eb84-37c9-814d-3e25fa00d2a9 | -5.475 | -43.0774 | 2025-09-27 13:50:00 | GOES-19 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 89.9 |
| e7042f58-5882-38a1-a688-9d32e1266fae | -8.6328 | -44.848 | 2025-09-27 13:50:00 | GOES-19 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 162.9 |
| 76efcc37-b3a3-35e6-ba97-f2eee3bacc1f | -9.8662 | -45.9145 | 2025-09-27 13:50:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 88.6 |
| 8b95657c-30a7-38a9-9787-e0f6c4b8be9b | -7.3849 | -47.0157 | 2025-09-27 13:50:00 | GOES-19 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 163.5 |
| 1145bc96-ec68-3e4b-adfe-795b89dea1d0 | -9.9772 | -43.5962 | 2025-09-27 13:50:00 | GOES-19 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 139.7 |
| 9d3769bb-554f-3ecf-9393-fdcc54552eb7 | -10.8242 | -45.3841 | 2025-09-27 13:50:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 158.2 |
| a6fbbf5f-7f2d-366d-961e-870fc445e1c9 | -10.8051 | -45.3866 | 2025-09-27 13:50:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 112.8 |
| 935e94f5-7b28-39ce-bfcc-62e7cb30cc51 | -11.4417 | -44.9767 | 2025-09-27 13:50:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 151.9 |
| 71785a0d-8583-382f-b618-4ec42fe03700 | -11.0125 | -45.5189 | 2025-09-27 13:50:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 303.4 |
| 4fcedd0f-da37-3783-b9e6-b9a512973d3d | -12.6495 | -51.6797 | 2025-09-27 13:50:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 564.0 |
| cd8f6745-0b20-39d2-8d5e-e0f4484a0225 | -14.4921 | -48.5668 | 2025-09-27 13:50:00 | GOES-19 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 72.1 |
| 8b2551b1-128b-317f-8bac-2232049d1db9 | -11.7194 | -44.4254 | 2025-09-27 13:50:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 84.5 |
| 4a6bc312-e586-3f24-a1b3-94c1698edb16 | -8.6517 | -44.846 | 2025-09-27 13:50:00 | GOES-19 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 109.9 |
| 2083d2b7-9807-3637-856d-36bf03362bd9 | -6.2689 | -42.472 | 2025-09-27 13:50:00 | GOES-19 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 81.7 |
| a7c54e1b-7f0c-3c38-9dff-864ee5d9fcaa | -14.0807 | -48.8292 | 2025-09-27 13:50:00 | GOES-19 | URUAÇU | GOIÁS | Brasil | 5221601 | 52 | 33 | nan | nan | nan | Cerrado | 57.7 |
| 1c3985d8-ec65-3977-96be-d78c9a4f4c85 | -14.8304 | -45.3947 | 2025-09-27 13:50:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 237.1 |
| f2791c82-d0f1-37c9-a4a4-a9054a55daca | -9.3517 | -47.5801 | 2025-09-27 13:50:00 | GOES-19 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 81.6 |
| f28bba55-8fe3-3acf-8d60-f6acf5dffdf8 | -7.798 | -46.9576 | 2025-09-27 13:50:00 | GOES-19 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 145.8 |
| 027d415f-e304-3aa7-b03c-b32330e54b47 | -11.7002 | -44.4283 | 2025-09-27 13:50:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 92.2 |
| 5237f0e5-99cd-314e-9975-a639d6d9d83b | -7.7794 | -46.9371 | 2025-09-27 13:50:00 | GOES-19 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 567.9 |
| da362106-9c2d-3aa3-b458-a44868401b59 | -9.3702 | -47.6002 | 2025-09-27 13:50:00 | GOES-19 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 105.6 |
| 48375fb6-669e-3279-978b-1f77b5dd9cdc | -17.1739 | -56.3892 | 2025-09-27 13:50:00 | GOES-19 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 63.9 |
| f527b0fb-fdb1-398a-95a7-cbfb7d364834 | -7.1192 | -42.1786 | 2025-09-27 13:50:00 | GOES-19 | COLÔNIA DO PIAUÍ | PIAUÍ | Brasil | 2202778 | 22 | 33 | nan | nan | nan | Caatinga | 83.2 |
| 621c14f4-46f8-3876-803c-fd71c871a69b | -9.0391 | -45.5334 | 2025-09-27 13:50:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 70.4 |
| 3ba29c05-4a18-373a-b666-a00465da9640 | -14.85 | -45.3911 | 2025-09-27 13:50:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 255.2 |
| 10cd2078-b36b-3423-a315-db59d334fbc3 | -11.3646 | -45.0108 | 2025-09-27 13:50:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 108.6 |
| 66582b78-91c2-3b0c-a86d-9b1ffdb065f2 | -5.7961 | -42.8182 | 2025-09-27 13:50:00 | GOES-19 | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 89.0 |
| 8704568b-73bf-3a88-bf8e-bee87090fafa | -7.3659 | -47.0394 | 2025-09-27 13:50:00 | GOES-19 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 105.9 |
| 446a7fd6-79ab-31b8-a564-0dc615b4300f | -14.8299 | -45.4181 | 2025-09-27 13:50:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 71.4 |
| d215fe98-132f-3ef0-961c-705c521d6963 | -20.564 | -57.1616 | 2025-09-27 13:50:00 | GOES-19 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 56.2 |
| 5f292c67-c60b-31e7-a5f2-611dc394f291 | -6.6986 | -42.741 | 2025-09-27 13:50:00 | GOES-19 | FRANCISCO AYRES | PIAUÍ | Brasil | 2204105 | 22 | 33 | nan | nan | nan | Caatinga | 103.1 |
| 6bd19ef1-a657-3f6f-8455-dcb1f0344322 | -14.0188 | -56.1131 | 2025-09-27 13:50:00 | GOES-19 | NOVA MUTUM | MATO GROSSO | Brasil | 5106224 | 51 | 33 | nan | nan | nan | Cerrado | 64.2 |
| bc8e385a-9a1b-3118-8e25-60d590fe616c | -12.0369 | -47.0543 | 2025-09-27 13:50:00 | GOES-19 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 66.5 |
| a8ed5c7e-90e4-3b61-87a8-f22db69fd871 | -7.2216 | -44.7601 | 2025-09-27 13:50:00 | GOES-19 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 106.3 |
| 1b19cfad-d998-3a37-8ccc-88a34b0ebff9 | -11.7006 | -44.4049 | 2025-09-27 13:50:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 107.6 |
| 7f007120-cb36-3ec6-ac3e-208c60b8d2b7 | -7.3661 | -47.0173 | 2025-09-27 13:50:00 | GOES-19 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 91.3 |
| 533afa75-8026-38e4-9623-898f96b9bbc1 | -9.4269 | -47.5943 | 2025-09-27 13:50:00 | GOES-19 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 95.6 |
| 8173f52d-ccee-38ed-a3c3-165b3971611a | -8.4827 | -47.8202 | 2025-09-27 13:50:00 | GOES-19 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 171.9 |
| a4e32821-b8f1-3000-be35-1655489fedd7 | -5.6223 | -43.3701 | 2025-09-27 13:50:00 | GOES-19 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 101.0 |
| 4dca148d-4b56-3a41-b115-81a1b47db0c9 | -8.8226 | -46.2115 | 2025-09-27 13:50:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 99.7 |
| 5b303a5d-32e2-3132-8d68-faf2509215ce | -6.2501 | -42.4736 | 2025-09-27 13:50:00 | GOES-19 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 84.5 |
| b06e942b-5593-349d-8e60-3e7154f7b7dd | -9.0419 | -46.7478 | 2025-09-27 13:50:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 71.1 |
| dedee405-210b-3f95-bbc9-561964ca9191 | -6.8444 | -43.1745 | 2025-09-27 13:50:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 81.5 |
| 195954be-132c-3a0a-b8a8-46cdac689265 | -4.6946 | -37.661 | 2025-09-27 13:50:00 | GOES-19 | ARACATI | CEARÁ | Brasil | 2301109 | 23 | 33 | nan | nan | nan | Caatinga | 112.7 |
| 91fbe20c-c41b-3247-a2cc-2cff20964642 | -5.8149 | -42.8167 | 2025-09-27 13:50:00 | GOES-19 | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 73.4 |
| e219d656-3f4a-35a1-b01b-d76b056f1419 | -9.8784 | -47.7221 | 2025-09-27 13:50:00 | GOES-19 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 69.7 |
| 97ae67d1-2635-3ccf-9c20-42e40322a653 | -5.3693 | -42.3077 | 2025-09-27 13:50:00 | GOES-19 | ALTO LONGÁ | PIAUÍ | Brasil | 2200301 | 22 | 33 | nan | nan | nan | Caatinga | 85.2 |
| 4ca347ba-7248-32aa-ae79-2614e21ad240 | -11.3846 | -44.9618 | 2025-09-27 13:50:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 102.2 |
| 159df3a6-7ccb-3b28-a951-f02d44a1716a | -8.822 | -46.2564 | 2025-09-27 13:50:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 148.3 |
| bda0dad9-104d-3757-a37b-3e76005660d7 | -6.7172 | -42.7629 | 2025-09-27 13:50:00 | GOES-19 | FRANCISCO AYRES | PIAUÍ | Brasil | 2204105 | 22 | 33 | nan | nan | nan | Caatinga | 116.6 |
| b5088c27-0535-3ccd-80dc-ca958d730403 | -6.7174 | -42.7393 | 2025-09-27 13:50:00 | GOES-19 | FRANCISCO AYRES | PIAUÍ | Brasil | 2204105 | 22 | 33 | nan | nan | nan | Caatinga | 83.6 |
| d7cc03b9-4293-3b23-bea7-440a75be6406 | -5.6813 | -43.0619 | 2025-09-27 13:50:00 | GOES-19 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 98.1 |
| a838c0a5-ce09-354b-af04-c53e2e2e5bc0 | -5.9472 | -42.7118 | 2025-09-27 13:50:00 | GOES-19 | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 80.6 |
| 33433794-a6ee-3899-9eee-4da7e66ce3be | -5.3091 | -42.761 | 2025-09-27 13:50:00 | GOES-19 | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Caatinga | 87.9 |
| 3c42e2f0-7cb4-32b2-b750-e5018786ca9a | -5.4937 | -43.0761 | 2025-09-27 13:50:00 | GOES-19 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 80.4 |
| 4ee886f3-8be6-3f26-919b-c7d687006a2e | -9.3343 | -48.9364 | 2025-09-27 13:50:00 | GOES-19 | DOIS IRMÃOS DO TOCANTINS | TOCANTINS | Brasil | 1707207 | 17 | 33 | nan | nan | nan | Cerrado | 64.3 |
| 21dc129d-3421-32e0-baa7-f49e1403a455 | -11.4413 | -44.9998 | 2025-09-27 13:50:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 286.8 |
| 20b32e36-84d5-3757-b2a2-f45db2d65420 | -12.6498 | -48.1509 | 2025-09-27 13:50:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 86.3 |
| 891a440a-0ba4-3e81-bfed-0399179d1d70 | -8.4825 | -47.8421 | 2025-09-27 13:50:00 | GOES-19 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 129.1 |
| 0529cd5a-1577-3388-b52b-220777a8bece | -11.4221 | -45.0025 | 2025-09-27 13:50:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 103.2 |
| fc46729a-c063-3e08-9e10-8b7edc1b991c | -8.6631 | -43.991 | 2025-09-27 13:50:00 | GOES-19 | CRISTINO CASTRO | PIAUÍ | Brasil | 2203107 | 22 | 33 | nan | nan | nan | Cerrado | 113.7 |
| d2293b07-3985-3613-b962-b0f77bea9b32 | -11.4425 | -44.9303 | 2025-09-27 13:50:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 107.7 |
| b418cbbc-8d2f-3e2f-9bc9-d82533a0497a | -8.9182 | -46.1115 | 2025-09-27 14:00:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 70.0 |
| 76be388f-7803-3425-90a6-6af82ed191cc | -9.8662 | -45.9145 | 2025-09-27 14:00:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 102.2 |
| d6de579c-872b-32ad-b875-a2ffeb055b28 | -5.475 | -43.0774 | 2025-09-27 14:00:00 | GOES-19 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 92.4 |
| ef1f4c20-b313-3d6a-a05d-17806d62a09b | -11.4413 | -44.9998 | 2025-09-27 14:00:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 147.0 |
| 6a318e42-9278-3024-9734-660d68c71a25 | -11.3846 | -44.9618 | 2025-09-27 14:00:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 102.7 |
| 90066f85-d471-36fa-9c6f-3e991f058d42 | -13.7109 | -51.1861 | 2025-09-27 14:00:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 72.4 |
| c691e7c6-605f-39ab-98ff-17b1a9a01949 | -15.2136 | -56.0047 | 2025-09-27 14:00:00 | GOES-19 | CUIABÁ | MATO GROSSO | Brasil | 5103403 | 51 | 33 | nan | nan | nan | Cerrado | 89.3 |
| f4a44811-a5b2-3a1f-9f2a-a9a0c19ad4c3 | -9.3514 | -47.6022 | 2025-09-27 14:00:00 | GOES-19 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 176.8 |
| e22cd7c8-b0ba-3b96-a46e-6a35847fcb58 | -14.4921 | -48.5668 | 2025-09-27 14:00:00 | GOES-19 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 65.3 |
| 7b97c047-b36c-32ff-8dcf-fe2f73f0512c | -11.385 | -44.9386 | 2025-09-27 14:00:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 134.6 |
| 82b95256-e676-3054-8fc7-4fd393c44d55 | -11.0125 | -45.5189 | 2025-09-27 14:00:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 86.6 |
| 4e73cd4d-2b6f-3fcf-b70c-feb4f82a14ab | -15.8884 | -46.1944 | 2025-09-27 14:00:00 | GOES-19 | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 75.3 |
| 34a66cf3-9861-3997-8d98-aca215f8eca2 | -6.8444 | -43.1745 | 2025-09-27 14:00:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 88.1 |
| 91933452-9a63-3cb1-aa76-78ac3708f9b0 | -11.4221 | -45.0025 | 2025-09-27 14:00:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 111.5 |
| 3ea8b5fa-73d6-3ffd-be84-ad19a7bf5c80 | -6.7174 | -42.7393 | 2025-09-27 14:00:00 | GOES-19 | FRANCISCO AYRES | PIAUÍ | Brasil | 2204105 | 22 | 33 | nan | nan | nan | Caatinga | 78.2 |


[Clique aqui para ver as próximas entradas](README67.md)
