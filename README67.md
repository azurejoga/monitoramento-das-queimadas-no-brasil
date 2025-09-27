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

## Dados Diários - Página 67

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| d681bc67-f6ed-33bc-975b-5bba04e4ef58 | -14.8304 | -45.3947 | 2025-09-27 14:00:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 124.8 |
| d8091f02-233e-38dc-b9f7-d4468afb464a | -11.4417 | -44.9767 | 2025-09-27 14:00:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 162.2 |
| 6919393c-03c5-3e21-9abf-a2b2e44abcb6 | -8.1363 | -42.3801 | 2025-09-27 14:00:00 | GOES-19 | PEDRO LAURENTINO | PIAUÍ | Brasil | 2207934 | 22 | 33 | nan | nan | nan | Caatinga | 101.9 |
| 4e29f027-5175-31a3-9acc-1a2538d4dd0a | -7.7609 | -46.9166 | 2025-09-27 14:00:00 | GOES-19 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 147.3 |
| a0137806-c1ef-32e0-9854-abc07aae4b36 | -5.407 | -42.2812 | 2025-09-27 14:00:00 | GOES-19 | ALTO LONGÁ | PIAUÍ | Brasil | 2200301 | 22 | 33 | nan | nan | nan | Caatinga | 77.1 |
| 89356d3c-cca2-342a-91fb-d972aaac9a05 | -5.7588 | -42.7976 | 2025-09-27 14:00:00 | GOES-19 | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 101.4 |
| 9bf77274-360f-322a-b37e-f5d87e90bd4d | -8.1805 | -46.3657 | 2025-09-27 14:00:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 60.2 |
| 088dc3ee-57c8-33aa-9507-98b876544996 | -8.1619 | -46.3451 | 2025-09-27 14:00:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 57.4 |
| b6c2abcb-b7b9-38af-baec-569bea1a5557 | -4.6946 | -37.661 | 2025-09-27 14:00:00 | GOES-19 | ARACATI | CEARÁ | Brasil | 2301109 | 23 | 33 | nan | nan | nan | Caatinga | 145.5 |
| 11bdfa91-4773-3547-a8b4-995913298d6b | -5.4937 | -43.0761 | 2025-09-27 14:00:00 | GOES-19 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 84.3 |
| 591f6538-f2db-3883-85bf-a9de953810e7 | -5.7585 | -42.8211 | 2025-09-27 14:00:00 | GOES-19 | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 162.9 |
| 82750224-340f-3045-8096-db0df391120c | -7.3659 | -47.0394 | 2025-09-27 14:00:00 | GOES-19 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 130.1 |
| 8bc51b74-fff9-3e18-a146-ff552cae1a6d | -7.3661 | -47.0173 | 2025-09-27 14:00:00 | GOES-19 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 83.3 |
| 7ec55b13-5e91-38c5-bd9a-38135c3d143b | -8.6442 | -43.9931 | 2025-09-27 14:00:00 | GOES-19 | CRISTINO CASTRO | PIAUÍ | Brasil | 2203107 | 22 | 33 | nan | nan | nan | Cerrado | 101.8 |
| 06119506-9520-3997-aefb-e397b804a619 | -5.7227 | -42.6354 | 2025-09-27 14:00:00 | GOES-19 | MIGUEL LEÃO | PIAUÍ | Brasil | 2206308 | 22 | 33 | nan | nan | nan | Caatinga | 102.3 |
| 8d279f39-c8b0-3e40-a314-e3ec2551e440 | -11.3646 | -45.0108 | 2025-09-27 14:00:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 108.3 |
| efafad8b-6bf9-3602-9221-bb32e7cefb87 | -10.4025 | -48.1256 | 2025-09-27 14:00:00 | GOES-19 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 58.0 |
| 92674817-f765-3b99-8699-0a0f6edd257b | -5.6223 | -43.3701 | 2025-09-27 14:00:00 | GOES-19 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 75.5 |
| 6322d77e-c4a1-31dc-8b6b-02d1894e9d5f | -9.3343 | -48.9364 | 2025-09-27 14:00:00 | GOES-19 | DOIS IRMÃOS DO TOCANTINS | TOCANTINS | Brasil | 1707207 | 17 | 33 | nan | nan | nan | Cerrado | 74.2 |
| a57bb449-b101-3e25-a796-9b3581af39f9 | -7.8175 | -46.8894 | 2025-09-27 14:00:00 | GOES-19 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 82.1 |
| 73fbc8e5-fb13-38fe-9b1e-98343d0bc2be | -7.7794 | -46.9371 | 2025-09-27 14:00:00 | GOES-19 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 400.9 |
| 228e0217-0066-3041-9ade-0b3bb8d4255e | -8.6517 | -44.846 | 2025-09-27 14:00:00 | GOES-19 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 81.8 |
| 37daf5e7-9af8-3d61-bbd1-141e68fc76e2 | -7.8637 | -44.5382 | 2025-09-27 14:00:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 77.2 |
| 10231eaa-7de1-3294-bb37-8dda902288a6 | -14.85 | -45.3911 | 2025-09-27 14:00:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 92.2 |
| a3dbe169-0477-3171-9d59-00b301f81afe | -20.564 | -57.1616 | 2025-09-27 14:00:00 | GOES-19 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 180.6 |
| 4ba83299-fdfa-377f-bb08-4813c32af189 | -6.5801 | -45.1117 | 2025-09-27 14:00:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 84.9 |
| fe94b57e-d7ff-3921-a5df-75fc758b4009 | -18.3049 | -57.0938 | 2025-09-27 14:00:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 119.3 |
| 86453d98-93b9-3f78-b388-150c41937302 | -7.798 | -46.9576 | 2025-09-27 14:00:00 | GOES-19 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 97.9 |
| d4ef4293-0566-36ec-bbb9-45bf6654f629 | -12.6495 | -51.6797 | 2025-09-27 14:00:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 539.8 |
| bc4fc6dd-084a-3c91-a55a-6573b3260868 | -7.3849 | -47.0157 | 2025-09-27 14:00:00 | GOES-19 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 142.4 |
| 79a84e1c-6a6a-32d5-b59a-468221025221 | -12.2632 | -44.0834 | 2025-09-27 14:00:00 | GOES-19 | TABOCAS DO BREJO VELHO | BAHIA | Brasil | 2930907 | 29 | 33 | nan | nan | nan | Cerrado | 204.2 |
| 8006fba7-064e-3782-8bc9-f6304e75aad2 | -8.8415 | -46.2095 | 2025-09-27 14:00:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 88.1 |
| cac8e2b0-8eba-31de-9d84-29dd7c91d74e | -11.4225 | -44.9794 | 2025-09-27 14:00:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 92.4 |
| f12079dc-bb0f-3471-b9fe-50f9e75f4ac6 | -8.6631 | -43.991 | 2025-09-27 14:00:00 | GOES-19 | CRISTINO CASTRO | PIAUÍ | Brasil | 2203107 | 22 | 33 | nan | nan | nan | Cerrado | 112.3 |
| 2f9774c6-aabf-3012-ba8b-e9ac8de3542a | -5.7225 | -42.659 | 2025-09-27 14:00:00 | GOES-19 | MIGUEL LEÃO | PIAUÍ | Brasil | 2206308 | 22 | 33 | nan | nan | nan | Caatinga | 205.3 |
| abc9154d-3e82-3b31-a611-9d92423806c1 | -11.3642 | -45.0339 | 2025-09-27 14:00:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 160.5 |
| 8d2333fe-a04f-300d-b4a3-37ee400dc8c4 | -8.8996 | -46.0909 | 2025-09-27 14:00:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 110.0 |
| dce70f06-6340-3fa7-bb8a-c4f5dabca34a | -5.6813 | -43.0619 | 2025-09-27 14:00:00 | GOES-19 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 249.0 |
| e0902e2b-942a-3281-a1fb-ca09a7eb5fa9 | -5.7413 | -42.6576 | 2025-09-27 14:00:00 | GOES-19 | AGRICOLÂNDIA | PIAUÍ | Brasil | 2200103 | 22 | 33 | nan | nan | nan | Caatinga | 86.2 |
| 6a52aff7-f2d0-3849-bc0a-75594d0ee459 | -7.1383 | -45.5174 | 2025-09-27 14:00:00 | GOES-19 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 72.8 |
| 46aad4a9-9515-3df4-b204-dfc44bd3df01 | -6.6986 | -42.741 | 2025-09-27 14:00:00 | GOES-19 | FRANCISCO AYRES | PIAUÍ | Brasil | 2204105 | 22 | 33 | nan | nan | nan | Caatinga | 107.2 |
| 4e406b4a-b722-3e86-980c-f1cbfc0e338a | -8.822 | -46.2564 | 2025-09-27 14:00:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 110.6 |
| 0c4d083a-a2eb-38eb-9c21-15160e693278 | -20.5842 | -57.1587 | 2025-09-27 14:00:00 | GOES-19 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 91.2 |
| 313784be-a081-3af3-b978-5ea0f76cb5a0 | -9.3702 | -47.6002 | 2025-09-27 14:00:00 | GOES-19 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 100.6 |
| 77691afe-8a50-307f-a531-90e6684f6ee0 | -11.7006 | -44.4049 | 2025-09-27 14:00:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 109.5 |
| 0dd33df2-952f-35a4-af9e-453ae6e0e89c | -14.8454 | -45.6013 | 2025-09-27 14:00:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 79.5 |
| ce495b5a-7828-32f5-a5f6-dc43adc8f9f9 | -11.6805 | -44.4545 | 2025-09-27 14:00:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 96.9 |
| 4bff543e-c528-3875-b7f3-1499a58044ca | -4.1761 | -44.2716 | 2025-09-27 14:00:00 | GOES-19 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 95.4 |
| 29cd1d8d-6224-33d4-8b29-0cfea5f10665 | -17.1739 | -56.3892 | 2025-09-27 14:00:00 | GOES-19 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 63.2 |
| 623c76d3-669f-30af-a6a0-81265be1bd26 | -8.4825 | -47.8421 | 2025-09-27 14:00:00 | GOES-19 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 212.5 |
| 89a5c6bc-1564-38d8-9623-5cc295db36e3 | -6.819 | -43.7831 | 2025-09-27 14:00:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 84.1 |
| bc7bc8b9-9047-3039-88b7-b2e23ed83925 | -4.1759 | -44.2945 | 2025-09-27 14:00:00 | GOES-19 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 167.1 |
| 122fffa3-30d8-35b9-b4a6-862f91adc7b6 | -5.7961 | -42.8182 | 2025-09-27 14:00:00 | GOES-19 | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 91.5 |
| 560e3f36-41b0-3004-82bd-0346ebdd5982 | -9.3511 | -47.6243 | 2025-09-27 14:00:00 | GOES-19 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 108.0 |
| ad98d150-fa5e-35b5-9e7d-3b4f4766b413 | -4.1947 | -44.2706 | 2025-09-27 14:00:00 | GOES-19 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 83.0 |
| 2bcfb158-c98f-348b-a417-4d7506a45fb4 | -6.7172 | -42.7629 | 2025-09-27 14:00:00 | GOES-19 | FRANCISCO AYRES | PIAUÍ | Brasil | 2204105 | 22 | 33 | nan | nan | nan | Caatinga | 82.0 |
| 68c1c7b0-bee7-3f74-98c5-45a934f5fdff | -4.1946 | -44.2935 | 2025-09-27 14:00:00 | GOES-19 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 186.4 |
| 0158ca8d-2b19-3db7-86ca-bb8210c54008 | -10.8242 | -45.3841 | 2025-09-27 14:00:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 117.1 |
| 461e6a26-204b-3af6-b7bb-cbec8c35fa13 | -7.6399 | -45.9907 | 2025-09-27 14:00:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 66.1 |
| 8d7e2ee5-d215-30df-ad1b-4e1085b8a1a1 | -9.4269 | -47.5943 | 2025-09-27 14:00:00 | GOES-19 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 71.9 |
| db10648b-2d20-3313-8476-f5ea5cb7c3a3 | -11.3654 | -44.9645 | 2025-09-27 14:00:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 144.9 |
| ed3e2b05-f84f-325b-b5cf-7e7e3362048b | -9.3517 | -47.5801 | 2025-09-27 14:00:00 | GOES-19 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 88.7 |
| 7bd85bdd-5bd5-3699-85dc-62ecc24d0e11 | -9.9772 | -43.5962 | 2025-09-27 14:00:00 | GOES-19 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 147.7 |
| 7a70430c-9b1c-3cf3-87d2-23c14b50aa49 | -8.9185 | -46.0889 | 2025-09-27 14:00:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 125.0 |
| 411d69db-0534-3a38-8739-6b12179bd7e8 | -11.681 | -44.4312 | 2025-09-27 14:00:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 98.8 |
| d7dde6ec-a062-360e-a2f0-a0825b6ed2c2 | -8.6328 | -44.848 | 2025-09-27 14:00:00 | GOES-19 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 142.7 |
| 3c6b7d4c-02fa-3adf-a70f-282800244a72 | -9.8971 | -47.7421 | 2025-09-27 14:00:00 | GOES-19 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 73.2 |
| 6fb0d436-65d9-3901-934e-581e1858939c | -6.2501 | -42.4736 | 2025-09-27 14:00:00 | GOES-19 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 82.3 |
| a4524834-8481-3b3d-b853-3bb76e8cc716 | -7.1571 | -45.5158 | 2025-09-27 14:00:00 | GOES-19 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 163.0 |
| 0de86a25-fd33-3296-954f-e94722b5ad4e | -7.7797 | -46.9149 | 2025-09-27 14:00:00 | GOES-19 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 130.4 |
| ae87076c-2fa8-3979-b812-86227ab537be | -5.3693 | -42.3077 | 2025-09-27 14:00:00 | GOES-19 | ALTO LONGÁ | PIAUÍ | Brasil | 2200301 | 22 | 33 | nan | nan | nan | Caatinga | 98.1 |
| f19fc11b-625e-317b-a452-9e8685ab72d6 | -12.6498 | -48.1509 | 2025-09-27 14:00:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 72.1 |
| 9d427bf8-88fc-3dd4-a298-65396ab2f1d3 | -8.8226 | -46.2115 | 2025-09-27 14:00:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 99.8 |
| af917cda-22c7-361e-b14f-1512ea0117cc | -3.8277 | -40.3373 | 2025-09-27 14:00:00 | GOES-19 | FORQUILHA | CEARÁ | Brasil | 2304350 | 23 | 33 | nan | nan | nan | Caatinga | 107.7 |
| c9f42004-6808-3fdc-904c-e7d045df3f04 | -11.4425 | -44.9303 | 2025-09-27 14:00:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 192.1 |
| 7ab1cbdb-eca1-3aa7-beeb-2bffba318591 | -9.6159 | -47.5741 | 2025-09-27 14:00:00 | GOES-19 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 146.8 |
| 90802c3e-2d41-30a5-863c-31ef5bd170fc | -10.4215 | -48.1234 | 2025-09-27 14:00:00 | GOES-19 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 76.4 |
| e46d0b78-492e-35e9-9052-681eecb94d13 | -6.6983 | -42.7646 | 2025-09-27 14:00:00 | GOES-19 | FRANCISCO AYRES | PIAUÍ | Brasil | 2204105 | 22 | 33 | nan | nan | nan | Caatinga | 113.0 |
| e1142060-0978-3918-bced-08b8ee5b22cb | -10.0187 | -48.5183 | 2025-09-27 14:00:00 | GOES-19 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 68.4 |
| 8a744b2e-20f8-3223-a1e6-e0715cb21d49 | -7.2607 | -42.9703 | 2025-09-27 14:10:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 93.6 |
| 93d69762-9e1e-3213-9657-b0f5c10d04d5 | -5.8149 | -42.8167 | 2025-09-27 14:10:00 | GOES-19 | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 96.8 |
| d8a49b1a-31e3-3a9e-ba3a-ff7ab3bd61ae | -10.8242 | -45.3841 | 2025-09-27 14:10:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 79.0 |
| 6cb25ac7-20cc-386f-8418-a82cf033be6a | -5.7585 | -42.8211 | 2025-09-27 14:10:00 | GOES-19 | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 120.0 |
| 837fedc4-5fd9-30f5-87e4-bf6599805b27 | -4.6946 | -37.661 | 2025-09-27 14:10:00 | GOES-19 | ARACATI | CEARÁ | Brasil | 2301109 | 23 | 33 | nan | nan | nan | Caatinga | 142.9 |
| 17e06480-5c7e-3809-a806-f0bf3c2de343 | -20.5842 | -57.1587 | 2025-09-27 14:10:00 | GOES-19 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 85.6 |
| 7b48c0c9-6998-3fa9-90f2-557dfe36a61e | -5.475 | -43.0774 | 2025-09-27 14:10:00 | GOES-19 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 97.2 |
| c9711c41-f688-3c19-be37-f858d7b56b4e | -8.4827 | -47.8202 | 2025-09-27 14:10:00 | GOES-19 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 163.6 |
| b7b9603d-847a-3928-b39e-b5168ed2af75 | -9.0391 | -45.5334 | 2025-09-27 14:10:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 82.5 |
| efaa6fa1-b224-3b66-a9c4-a90e7afb5f3f | -6.5614 | -45.1132 | 2025-09-27 14:10:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 60.5 |
| c751af80-5743-3ad6-81bd-973a6595dde6 | -7.5571 | -46.6906 | 2025-09-27 14:10:00 | GOES-19 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 80.7 |
| 55a2ae40-ab83-3ae5-b355-9cf3d3c50dde | -14.4921 | -48.5668 | 2025-09-27 14:10:00 | GOES-19 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 80.2 |
| 46543d1d-1444-34a4-98c7-753673104fd4 | -12.6495 | -51.6797 | 2025-09-27 14:10:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 387.0 |
| 210b8420-a4bf-3089-b519-62770776d47b | -20.7545 | -57.7845 | 2025-09-27 14:10:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 108.7 |
| c1c30e9a-9f39-3a12-ac6a-76b4f43433c7 | -7.7794 | -46.9371 | 2025-09-27 14:10:00 | GOES-19 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 429.5 |
| aa1bb2be-80e1-3f48-854d-c2624944093b | -11.681 | -44.4312 | 2025-09-27 14:10:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 98.0 |
| 2164f2f5-1c4d-306d-afd5-a3095b190cde | -6.5801 | -45.1117 | 2025-09-27 14:10:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 82.8 |
| 17ee4429-6850-3031-b7cc-ccb1294d54cc | -20.564 | -57.1616 | 2025-09-27 14:10:00 | GOES-19 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 141.2 |
| 9b09d340-8821-3ab9-a9f6-bf28b0dd0c01 | -7.5568 | -46.7128 | 2025-09-27 14:10:00 | GOES-19 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 77.1 |
| 7e9ca34f-171e-3ef9-bcc4-f55337fd37f0 | -9.9776 | -43.5727 | 2025-09-27 14:10:00 | GOES-19 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 78.0 |
| ffdfacbc-433c-3c37-b46c-caacb07fd150 | -7.1571 | -45.5158 | 2025-09-27 14:10:00 | GOES-19 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 109.7 |


[Clique aqui para ver as próximas entradas](README68.md)
