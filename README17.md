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

## Dados Diários - Página 17

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| a933a2e7-d9bc-304d-ba6e-fd09c3bd7fdb | -6.94243 | -45.20874 | 2024-10-23 03:36:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 8649d023-bcf3-3ad0-8dd6-406dea33a3d5 | -6.94157 | -45.2135 | 2024-10-23 03:36:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 2b084149-3bc4-3ab3-98aa-4bb1cbe79c3b | -7.42616 | -46.61747 | 2024-10-23 03:36:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 079c1b97-8cfa-3dc8-9a4e-e6f9913af30e | -7.42395 | -46.61638 | 2024-10-23 03:36:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 16d3c43e-5dc7-372f-a66e-94aa32ac54c7 | -7.42285 | -46.62228 | 2024-10-23 03:36:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 66d2c042-ebe0-3ee7-9d59-4b47c7cab44a | -7.41946 | -46.61606 | 2024-10-23 03:36:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 003fadd9-94c4-385a-be14-f7e569021d6c | -7.41834 | -46.62188 | 2024-10-23 03:36:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 4cfc7577-abb7-3722-90bf-0dc6e8f932bd | -7.41725 | -46.61496 | 2024-10-23 03:36:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 4fbd25a8-e4a5-3508-a23d-f98bc15b5e4c | -7.41617 | -46.62075 | 2024-10-23 03:36:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 75c7d645-fd72-346a-b958-af928cd55e82 | -11.63016 | -47.57812 | 2024-10-23 03:36:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 2ec97e25-edce-3efc-a9c0-6adc01f331b2 | -11.62896 | -47.58389 | 2024-10-23 03:36:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 4.8 |
| ef36745b-1858-3937-b8b7-45f200daee41 | -11.62609 | -47.58182 | 2024-10-23 03:36:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 4.7 |
| c6852f5c-76d7-3e4e-9ecc-08ec4d455085 | -11.62354 | -47.57664 | 2024-10-23 03:36:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| fda8dd4c-f9b4-3414-8e53-31847049feb6 | -11.62235 | -47.58237 | 2024-10-23 03:36:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 6.0 |
| cc6c604c-143f-3639-8811-a14f202a7487 | -11.61946 | -47.58036 | 2024-10-23 03:36:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 61a2d857-2880-3c77-a615-771b81fec25e | -9.07976 | -47.98995 | 2024-10-23 03:36:00 | NPP-375D | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| d82f65f0-3581-3f06-9d8e-a176c39e88f7 | -9.07834 | -47.99696 | 2024-10-23 03:36:00 | NPP-375D | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| c0e3e7f5-348a-38a2-8cf0-1fee124b53c4 | -9.07623 | -47.98959 | 2024-10-23 03:36:00 | NPP-375D | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 132c44b2-a756-3616-86de-ece310666bdc | -9.07485 | -47.99665 | 2024-10-23 03:36:00 | NPP-375D | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| db602905-afc8-3bb8-8e11-bdc56c03b557 | -9.54127 | -47.82421 | 2024-10-23 03:36:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 0bdc1459-3565-3732-969d-30af072eea1f | -9.53996 | -47.83091 | 2024-10-23 03:36:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 81957d31-41b8-32e9-ac3f-cb69c77da787 | -9.53963 | -47.82363 | 2024-10-23 03:36:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 2a15304c-05cf-3e0d-b18b-f3ba0716df65 | -9.53827 | -47.83034 | 2024-10-23 03:36:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 83d3fc0e-1df8-3e11-beda-5247cffa27fd | -11.57048 | -48.72323 | 2024-10-23 03:36:00 | NPP-375D | GURUPI | TOCANTINS | Brasil | 1709500 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| a25050a5-831e-3bff-8735-d34fb4d39d5f | -11.56348 | -48.72139 | 2024-10-23 03:36:00 | NPP-375D | GURUPI | TOCANTINS | Brasil | 1709500 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 2d526f6b-67a4-3008-a0ba-87e824c55e7e | -11.11664 | -48.11179 | 2024-10-23 03:36:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| b547b286-9a18-3442-be6f-dc9a55815393 | -11.11525 | -48.11851 | 2024-10-23 03:36:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| df7b1ed6-8859-3000-a2df-e2c1287c2cbf | -11.0249 | -48.28575 | 2024-10-23 03:36:00 | NPP-375D | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 5.0 |
| c8f07998-4817-3063-8377-059daddc6bb8 | -11.02362 | -48.29203 | 2024-10-23 03:36:00 | NPP-375D | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 5.0 |
| d7c9e01d-b79e-35b9-8936-064e32f55409 | -11.02277 | -48.28391 | 2024-10-23 03:36:00 | NPP-375D | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 7.9 |
| 8f5285b3-5c90-3aef-a183-41781358799f | -11.02141 | -48.2903 | 2024-10-23 03:36:00 | NPP-375D | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 14.8 |
| d5ea28e1-4672-335a-8f8e-be26d953a8c9 | -11.0179 | -48.28445 | 2024-10-23 03:36:00 | NPP-375D | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 66b57af1-2382-33a3-a421-849df65b5c24 | -11.01656 | -48.29097 | 2024-10-23 03:36:00 | NPP-375D | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 5.0 |
| ec1323dc-e007-3673-81a8-15517c2bfc40 | -11.0144 | -48.28903 | 2024-10-23 03:36:00 | NPP-375D | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| fc52cfe3-1f37-3c2a-9dcf-0c9058772ecb | -17.6868 | -57.4593 | 2024-10-23 03:36:46 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 85.6 |
| d8e155d5-e170-3e8c-83da-d1cf21965c6f | -17.6865 | -57.4798 | 2024-10-23 03:36:46 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 65.4 |
| 17136120-7111-3bc3-b72b-62513ea7f7b2 | -17.764 | -57.5526 | 2024-10-23 03:36:46 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 71.5 |
| bae8faf1-fa3d-338e-a14a-6d5b2e0d0b8d | -17.7637 | -57.5732 | 2024-10-23 03:36:46 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 69.8 |
| 40ba5e72-0b8e-3f5f-b124-28da162e9603 | -18.3207 | -56.1986 | 2024-10-23 03:36:49 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 80.2 |
| af16a266-5380-312c-a2a5-bd63d8e47905 | -18.3203 | -56.2195 | 2024-10-23 03:36:49 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 137.0 |
| 35c67c0e-bb55-329a-a810-33a845b1da92 | -18.3004 | -56.2222 | 2024-10-23 03:36:49 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 89.5 |
| 5ad4e216-f118-3b0b-944a-c37faf2d16be | -16.515 | -43.59491 | 2024-10-23 03:38:00 | NPP-375D | FRANCISCO SÁ | MINAS GERAIS | Brasil | 3126703 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 9a7f71ee-259d-3bf1-bc88-a57fa311681f | -16.34732 | -43.69727 | 2024-10-23 03:38:00 | NPP-375D | CAPITÃO ENÉAS | MINAS GERAIS | Brasil | 3112703 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| db9aee8b-fe7f-342b-a9f7-44db145f7a00 | -15.61542 | -42.89933 | 2024-10-23 03:38:00 | NPP-375D | PORTEIRINHA | MINAS GERAIS | Brasil | 3152204 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| ae314ff8-48fb-3756-8a6a-1680ac34821e | -16.68142 | -43.88467 | 2024-10-23 03:38:00 | NPP-375D | MONTES CLAROS | MINAS GERAIS | Brasil | 3143302 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| c66187ba-f505-35f0-9db8-9fc53cfd8cd7 | -13.60194 | -43.99579 | 2024-10-23 03:38:00 | NPP-375D | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 4c2b78cd-ba4b-3bc5-88ed-ebfa47a89c63 | -13.60134 | -43.99892 | 2024-10-23 03:38:00 | NPP-375D | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| b939a759-54e2-3dc7-88fa-a3bc1ba91c45 | -18.03934 | -39.92706 | 2024-10-23 03:38:00 | NPP-375D | MUCURI | BAHIA | Brasil | 2922003 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| a7ca52bd-d9ad-33b2-b853-c22dcefcb214 | -19.83842 | -40.08105 | 2024-10-23 03:38:00 | NPP-375D | ARACRUZ | ESPÍRITO SANTO | Brasil | 3200607 | 32 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 4e43d494-dd19-3ae3-bbb7-e9ebee863c83 | -14.62118 | -40.60084 | 2024-10-23 03:38:00 | NPP-375D | PLANALTO | BAHIA | Brasil | 2925006 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| da7fdb81-b841-3b7b-8fed-ebc94d78fd2d | -14.61712 | -40.60018 | 2024-10-23 03:38:00 | NPP-375D | PLANALTO | BAHIA | Brasil | 2925006 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.4 |
| 8cb90f3c-1681-3c71-8064-c7ef4f0cf124 | -14.12116 | -41.67665 | 2024-10-23 03:38:00 | NPP-375D | BRUMADO | BAHIA | Brasil | 2904605 | 29 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 7dd9a1ee-899b-3185-90c8-c3b5248f9627 | -14.10262 | -41.18654 | 2024-10-23 03:38:00 | NPP-375D | TANHAÇU | BAHIA | Brasil | 2931004 | 29 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 812530a1-8db5-365f-ae95-fc22e43768f5 | -14.71338 | -40.73536 | 2024-10-23 03:38:00 | NPP-375D | VITÓRIA DA CONQUISTA | BAHIA | Brasil | 2933307 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 81102abb-63ed-3cd9-b88b-1c543b8ef8f2 | -20.51444 | -42.55882 | 2024-10-23 03:38:00 | NPP-375D | JEQUERI | MINAS GERAIS | Brasil | 3135506 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 36ab8122-af77-3ca1-929b-eb50d6ff3232 | -15.84515 | -43.81839 | 2024-10-23 03:38:00 | NPP-375D | SÃO JOÃO DA PONTE | MINAS GERAIS | Brasil | 3162401 | 31 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 5dce5f1c-e21b-3995-9075-7b664fec80d5 | -15.5212 | -43.13607 | 2024-10-23 03:38:00 | NPP-375D | PAI PEDRO | MINAS GERAIS | Brasil | 3146552 | 31 | 33 | nan | nan | nan | Caatinga | 4.8 |
| 691f20aa-0c5e-3c8f-af3e-210cab8bb282 | -15.52054 | -43.13478 | 2024-10-23 03:38:00 | NPP-375D | PAI PEDRO | MINAS GERAIS | Brasil | 3146552 | 31 | 33 | nan | nan | nan | Caatinga | 4.8 |
| 3529e5a7-754f-34f3-8a79-a2a91cb99d66 | -22.30475 | -41.88338 | 2024-10-23 03:40:00 | NPP-375D | MACAÉ | RIO DE JANEIRO | Brasil | 3302403 | 33 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| 69092a05-b9d2-318a-ac70-46efbc8c7fe7 | -22.90008 | -43.75165 | 2024-10-23 03:40:00 | NPP-375D | RIO DE JANEIRO | RIO DE JANEIRO | Brasil | 3304557 | 33 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| c442cd86-3002-32da-98e3-93af4c61d174 | -22.78542 | -43.75682 | 2024-10-23 03:40:00 | NPP-375D | SEROPÉDICA | RIO DE JANEIRO | Brasil | 3305554 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 1c1a6a8e-df32-3fa8-908a-e0eb74bdc266 | -1.388 | -51.9867 | 2024-10-23 03:45:14 | GOES-16 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 63.2 |
| fce4800f-adcb-316f-9170-36957d9d927f | -1.3879 | -52.0072 | 2024-10-23 03:45:14 | GOES-16 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 56.1 |
| 52cf978d-80df-343b-bde5-091c1fc318f6 | -3.1102 | -54.146 | 2024-10-23 03:45:24 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 62.4 |
| 17ed9d14-873e-3133-8786-f76f4b2274ea | -3.1101 | -54.1661 | 2024-10-23 03:45:24 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 112.5 |
| 8c02e675-b229-3192-827b-b3869ac74b56 | -3.0917 | -54.1666 | 2024-10-23 03:45:24 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 61.4 |
| 24569b22-b0b8-3ef2-95b2-0ba032925072 | -3.5491 | -54.7351 | 2024-10-23 03:45:26 | GOES-16 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 51.0 |
| 3021bf56-4217-3026-94f2-50aa61b86098 | -4.7565 | -46.6249 | 2024-10-23 03:45:33 | GOES-16 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 165.2 |
| 90316bde-ce67-35d5-869a-6e2b24d1f4a3 | -4.7751 | -46.6238 | 2024-10-23 03:45:33 | GOES-16 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 169.3 |
| 3f73f022-c94d-383b-afc8-8e31bc7aa47a | -5.5671 | -43.2576 | 2024-10-23 03:45:37 | GOES-16 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 53.9 |
| 3ed43acc-5a7d-389e-9e70-623ef746808e | -5.5858 | -43.2562 | 2024-10-23 03:45:38 | GOES-16 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 77.2 |
| 8e6931ba-0d8b-362c-a71f-ee6a13572963 | -17.764 | -57.5526 | 2024-10-23 03:46:46 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 69.5 |
| 81238202-ce80-39a4-ad85-e2de2ed8c690 | -18.3203 | -56.2195 | 2024-10-23 03:46:49 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 128.0 |
| 95091f3a-5f9a-3ac1-8574-bd1d53ae2d96 | -18.3004 | -56.2222 | 2024-10-23 03:46:49 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 78.5 |
| b752ac9f-56ad-302c-a29b-c3419ce9618b | -19.6453 | -56.7681 | 2024-10-23 03:46:56 | GOES-16 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 64.7 |
| 66776a2f-2ebf-3436-ade7-6342882ed58f | -19.645 | -56.7891 | 2024-10-23 03:46:56 | GOES-16 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 96.7 |
| cebfc8a2-52fc-3bb1-8bfe-b93b86af1589 | -19.6446 | -56.8101 | 2024-10-23 03:46:56 | GOES-16 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 74.9 |
| 12440ab5-3304-38d6-a64c-fb874ce86942 | -19.6253 | -56.7709 | 2024-10-23 03:46:56 | GOES-16 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 60.9 |
| fc9204cd-5f0b-3f20-b113-a04b26b7b9e2 | -19.6249 | -56.7919 | 2024-10-23 03:46:56 | GOES-16 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 96.9 |
| 818197b6-8b6d-3bb0-a914-4a6fc405118e | -19.6245 | -56.8129 | 2024-10-23 03:46:56 | GOES-16 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 72.7 |
| b3f337d9-12f9-342f-b1d2-6cf6d827d1e6 | -1.3879 | -52.0072 | 2024-10-23 03:55:14 | GOES-16 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 58.2 |
| 8bf1d1af-dea8-30c9-aa27-d0f87e5f373e | -3.0917 | -54.1666 | 2024-10-23 03:55:24 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 85.9 |
| 71cf61c2-19b3-3963-950d-b3923e3e1c93 | -3.1101 | -54.1661 | 2024-10-23 03:55:24 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 93.4 |
| ec781cd2-9bd0-3c0d-9c92-403cb6f602ac | -4.7254 | -45.7363 | 2024-10-23 03:55:33 | GOES-16 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 51.6 |
| 02cb73de-b941-3ae3-9b01-df2d1279fa1e | -4.7565 | -46.6249 | 2024-10-23 03:55:33 | GOES-16 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 90.1 |
| 761ea495-b4ea-3bce-950c-35ffa5d27559 | -4.7751 | -46.6238 | 2024-10-23 03:55:33 | GOES-16 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 84.7 |
| ef68e80b-b797-3e32-a536-347a0511473f | -5.5671 | -43.2576 | 2024-10-23 03:55:37 | GOES-16 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 64.5 |
| 8806a747-5bc9-3910-8595-d0e257f3275f | -5.5858 | -43.2562 | 2024-10-23 03:55:38 | GOES-16 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 58.1 |
| bc8f7102-e87e-3d40-b52a-166c30a8d996 | -17.7637 | -57.5732 | 2024-10-23 03:56:46 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 71.0 |
| 561a9eb9-cced-34c3-a465-8276e1bf633a | -18.3004 | -56.2222 | 2024-10-23 03:56:49 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 89.3 |
| 83515ba6-b157-3525-b89b-40946fb2c80e | -18.3203 | -56.2195 | 2024-10-23 03:56:49 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 117.7 |
| fb4e1506-e961-3f79-9ba8-1e5341fbccb7 | -18.3207 | -56.1986 | 2024-10-23 03:56:49 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 77.4 |
| b930b995-1619-37b7-8ca2-c88131f1b31f | -19.5469 | -56.6773 | 2024-10-23 03:56:55 | GOES-16 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 63.0 |
| 518a4f51-93c5-30a3-b770-bbc7da4d65d8 | -19.6446 | -56.8101 | 2024-10-23 03:56:56 | GOES-16 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 51.4 |
| 01a5b6fd-2c0c-3d29-9973-380aaa0ffb01 | -19.5669 | -56.6744 | 2024-10-23 03:56:56 | GOES-16 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 53.4 |
| 83a57a66-76ec-3e09-bea6-de2f375c25dd | -19.645 | -56.7891 | 2024-10-23 03:56:56 | GOES-16 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 71.2 |
| fb16b742-e27a-3cae-b775-b9bd1c525ca6 | -19.6453 | -56.7681 | 2024-10-23 03:56:56 | GOES-16 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 61.1 |
| f0b92a33-5ad2-32fb-865c-4c40128065a1 | -19.6253 | -56.7709 | 2024-10-23 03:56:56 | GOES-16 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 91.7 |
| 37fcbc1e-d2f1-3be9-b08b-960e2dc026a9 | -19.6249 | -56.7919 | 2024-10-23 03:56:56 | GOES-16 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 136.5 |
| b5cfe686-a3ac-385c-91fe-a0dedecbeaa3 | -19.6245 | -56.8129 | 2024-10-23 03:56:56 | GOES-16 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 99.4 |


[Clique aqui para ver as próximas entradas](README18.md)
