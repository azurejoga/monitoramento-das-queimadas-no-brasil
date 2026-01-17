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

## Dados Diários - Página 9

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| cf80de02-682b-3f50-b190-cd39fb20e99c | -14.78087 | -45.94146 | 2026-01-17 04:48:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 1d0b8199-680a-3e79-bb46-210c37a9933f | -10.98307 | -54.2504 | 2026-01-17 04:48:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 1ef054f2-6f84-3ba6-9f1e-9ac71c3be990 | -13.28035 | -53.96215 | 2026-01-17 04:48:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 932bdefe-b5e6-38bf-9f19-030ce59d5d55 | -13.6989 | -45.47649 | 2026-01-17 04:48:00 | NOAA-20 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 29628277-618c-3664-be5e-5b82f6646c1a | -13.69515 | -55.68789 | 2026-01-17 04:48:00 | NOAA-20 | NOVA MUTUM | MATO GROSSO | Brasil | 5106224 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 00836bb0-b1d7-3936-b8aa-169afa7b4f57 | -14.7123 | -53.95696 | 2026-01-17 04:48:00 | NOAA-20 | PRIMAVERA DO LESTE | MATO GROSSO | Brasil | 5107040 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| bf4b2ab0-7c7b-3f34-b3e0-d44e9e952d1c | -10.56269 | -44.31548 | 2026-01-17 04:48:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 27a4d050-4adc-380b-9696-616d41371877 | -12.2265 | -49.62824 | 2026-01-17 04:48:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| d2ca419c-5918-3361-be21-7233ef40e5dc | -14.75156 | -45.91253 | 2026-01-17 04:48:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 2c2e4e7c-8e0e-3179-b8a7-ba5e6275f4dd | -11.28891 | -48.73508 | 2026-01-17 04:48:00 | NOAA-20 | ALIANÇA DO TOCANTINS | TOCANTINS | Brasil | 1700350 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 4a068344-32a5-39d9-a9eb-731f4fc19a17 | -10.71227 | -44.15207 | 2026-01-17 04:48:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 9a586bdb-b305-33a3-bb30-ee9594c3cdea | -10.56096 | -44.31736 | 2026-01-17 04:48:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 8.4 |
| a6d2f24f-789f-3b2e-b2ec-af9af8cc51f9 | -10.93506 | -49.42596 | 2026-01-17 04:48:00 | NOAA-20 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 4d461ea5-e19f-3bdf-904a-5b1082169546 | -13.55153 | -53.25293 | 2026-01-17 04:48:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 33b29a44-bf55-362d-a562-d74495011c27 | -14.77564 | -45.94576 | 2026-01-17 04:48:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 0392fa47-c939-38c9-bf3b-0fab7f3fd36c | -13.69792 | -55.67152 | 2026-01-17 04:48:00 | NOAA-20 | NOVA MUTUM | MATO GROSSO | Brasil | 5106224 | 51 | 33 | nan | nan | nan | Cerrado | 3.3 |
| fd2df815-bd0d-3d32-8b01-0ebc88a9432f | -13.68946 | -55.67844 | 2026-01-17 04:48:00 | NOAA-20 | NOVA MUTUM | MATO GROSSO | Brasil | 5106224 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| a9892ab6-7871-3881-91af-d64751349078 | -14.78487 | -45.94695 | 2026-01-17 04:48:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| d24e21ad-096e-3fdc-9198-13b27c442db7 | -12.91488 | -49.486 | 2026-01-17 04:48:00 | NOAA-20 | ARAGUAÇU | TOCANTINS | Brasil | 1702000 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| c89f9ef5-ce65-3a25-a6b9-680e35f3d0f3 | -14.7178 | -53.9653 | 2026-01-17 04:48:00 | NOAA-20 | PRIMAVERA DO LESTE | MATO GROSSO | Brasil | 5107040 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 3955a431-d51a-3153-9878-450af1fa76de | -11.32239 | -44.49306 | 2026-01-17 04:48:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| de0c2e84-2bdc-3959-835b-5009224035c2 | -13.69653 | -55.67969 | 2026-01-17 04:48:00 | NOAA-20 | NOVA MUTUM | MATO GROSSO | Brasil | 5106224 | 51 | 33 | nan | nan | nan | Cerrado | 14.1 |
| 1f2aef7e-98fb-399a-861d-540c5714c35a | -15.0144 | -48.66977 | 2026-01-17 04:48:00 | NOAA-20 | VILA PROPÍCIO | GOIÁS | Brasil | 5222302 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 07779dd5-37a6-3183-af16-cc52dad10016 | -14.70792 | -48.89969 | 2026-01-17 04:48:00 | NOAA-20 | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 8aa15d86-3b78-3ddb-b403-9372c0668171 | -12.41829 | -55.45153 | 2026-01-17 04:48:00 | NOAA-20 | VERA | MATO GROSSO | Brasil | 5108501 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 4d80e350-ac72-3fcd-aac8-d3243d8385ea | -9.76328 | -48.27498 | 2026-01-17 04:48:00 | NOAA-20 | LAJEADO | TOCANTINS | Brasil | 1712009 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 96fef1dd-c762-36de-b391-a32873164ab6 | -10.9317 | -49.42626 | 2026-01-17 04:48:00 | NOAA-20 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 846ce680-c16a-33e4-bbd0-c06d364e4a44 | -11.80225 | -45.35859 | 2026-01-17 04:48:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 9f218287-86d7-3118-af47-9c68e86c4816 | -12.49751 | -46.34479 | 2026-01-17 04:48:00 | NOAA-20 | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 76f95372-3a52-3c5e-beeb-7dab754d2db1 | -11.28523 | -48.73452 | 2026-01-17 04:48:00 | NOAA-20 | ALIANÇA DO TOCANTINS | TOCANTINS | Brasil | 1700350 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| ebb20dbd-8311-3c26-a269-5af052fd5251 | -13.35818 | -50.51679 | 2026-01-17 04:48:00 | NOAA-20 | SÃO MIGUEL DO ARAGUAIA | GOIÁS | Brasil | 5220207 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| d556fcbb-4126-3341-8d5d-d1c94f8d34fa | -14.71447 | -53.96474 | 2026-01-17 04:48:00 | NOAA-20 | PRIMAVERA DO LESTE | MATO GROSSO | Brasil | 5107040 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 440ef15a-9308-38f5-9283-13bc3883fb2e | -13.6993 | -55.6773 | 2026-01-17 04:50:00 | GOES-19 | NOVA MUTUM | MATO GROSSO | Brasil | 5106224 | 51 | 33 | nan | nan | nan | Cerrado | 101.2 |
| dc03184a-808e-3449-a387-9a7b352eb03e | -20.4493 | -57.8895 | 2026-01-17 04:50:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 62.2 |
| c1aacc51-542b-3b63-9e4a-2d1055ac6227 | -20.73012 | -55.1585 | 2026-01-17 04:50:00 | NOAA-20 | SIDROLÂNDIA | MATO GROSSO DO SUL | Brasil | 5007901 | 50 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 50cd3226-cab3-3546-869e-bc33f675773f | -15.6095 | -57.32383 | 2026-01-17 04:50:00 | NOAA-20 | PORTO ESTRELA | MATO GROSSO | Brasil | 5106851 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 70e04a98-3604-392e-885b-b399a2cf19bb | -16.31438 | -57.56048 | 2026-01-17 04:50:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.4 |
| 21e92728-9913-3305-a68a-67242fe2b74b | -18.3066 | -54.57252 | 2026-01-17 04:50:00 | NOAA-20 | COXIM | MATO GROSSO DO SUL | Brasil | 5003306 | 50 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 24901b4b-1955-34dc-a276-7905bac76942 | -20.43875 | -57.88794 | 2026-01-17 04:50:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 0.8 |
| 9d8f7191-d10c-3359-b35e-4429c4d23f3f | -16.3219 | -57.56194 | 2026-01-17 04:50:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.3 |
| 9c1749cc-3bb1-381d-8899-2f6157cff50a | -16.32105 | -57.56675 | 2026-01-17 04:50:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.3 |
| ed55e4d6-f428-3b17-b54b-4861438214a8 | -20.42866 | -57.87838 | 2026-01-17 04:50:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.0 |
| 71413844-3506-3b11-993f-d3192ac939ca | -15.44303 | -56.3327 | 2026-01-17 04:50:00 | NOAA-20 | VÁRZEA GRANDE | MATO GROSSO | Brasil | 5108402 | 51 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 463c9d15-dacd-38f0-b477-092e63ba1647 | -15.43091 | -56.31744 | 2026-01-17 04:50:00 | NOAA-20 | VÁRZEA GRANDE | MATO GROSSO | Brasil | 5108402 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 6642e8ae-0997-3e1b-894a-a161802f0bac | -16.58524 | -57.80949 | 2026-01-17 04:50:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.0 |
| 1af65d6c-d534-357a-8cea-30dd1aac377c | -20.43511 | -57.88428 | 2026-01-17 04:50:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 10.8 |
| d9f76d44-ba7b-3369-b475-e7fdc5dc3b31 | -15.43661 | -56.32716 | 2026-01-17 04:50:00 | NOAA-20 | VÁRZEA GRANDE | MATO GROSSO | Brasil | 5108402 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| ede9d8d0-d420-34ce-ba43-4cd1cc6e1c17 | -20.44234 | -57.88574 | 2026-01-17 04:50:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.1 |
| 0a555ffb-e83e-3cec-a210-5021245228c2 | -20.72619 | -55.16161 | 2026-01-17 04:50:00 | NOAA-20 | SIDROLÂNDIA | MATO GROSSO DO SUL | Brasil | 5007901 | 50 | 33 | nan | nan | nan | Cerrado | 2.0 |
| cbe9c3e4-98e3-32c9-9044-fee3a8074ca5 | -20.44028 | -57.87612 | 2026-01-17 04:50:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.3 |
| 858f4618-e794-310e-bacb-784dd518cd02 | -20.44673 | -57.88202 | 2026-01-17 04:50:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.1 |
| 5c65cae4-fdff-3936-a007-83e5db6f0e95 | -20.43589 | -57.87983 | 2026-01-17 04:50:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 10.8 |
| 7ed701ad-2a4d-3777-aab6-0e6a37b164a1 | -16.11382 | -56.75509 | 2026-01-17 04:50:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 1ce122f5-0412-3ca2-9b06-c78ede67deb1 | -17.60777 | -46.66191 | 2026-01-17 04:50:00 | NOAA-20 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| f0377975-1263-3ee1-b7d4-eab0db9c3613 | -18.30269 | -54.57558 | 2026-01-17 04:50:00 | NOAA-20 | COXIM | MATO GROSSO DO SUL | Brasil | 5003306 | 50 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 513d2293-b574-3c18-a9b1-455615b440c1 | -19.17196 | -57.54607 | 2026-01-17 04:50:00 | NOAA-20 | LADÁRIO | MATO GROSSO DO SUL | Brasil | 5005202 | 50 | 33 | nan | nan | nan | Pantanal | 1.1 |
| c50af221-4543-38a4-a68d-91847fa1a2d0 | -20.44036 | -57.87906 | 2026-01-17 04:50:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 10.8 |
| a01533fd-5c4b-3619-becf-0c437ba40605 | -20.42485 | -57.83629 | 2026-01-17 04:50:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.8 |
| 88b4af59-8157-39df-9ae9-3a9258868948 | -20.44317 | -57.88423 | 2026-01-17 04:50:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 10.8 |
| b417f38c-ba0a-3b5a-928d-2d7e21ce201f | -15.61031 | -57.31916 | 2026-01-17 04:50:00 | NOAA-20 | PORTO ESTRELA | MATO GROSSO | Brasil | 5106851 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 971bbcf3-2755-38d3-a5fc-594f9786a47f | -15.43376 | -56.32231 | 2026-01-17 04:50:00 | NOAA-20 | VÁRZEA GRANDE | MATO GROSSO | Brasil | 5108402 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 3d6603d3-2aea-3e82-b76c-ccac93cadff2 | -15.97609 | -56.48486 | 2026-01-17 04:50:00 | NOAA-20 | NOSSA SENHORA DO LIVRAMENTO | MATO GROSSO | Brasil | 5106109 | 51 | 33 | nan | nan | nan | Cerrado | 0.5 |
| bba1d9a5-3e0c-3874-ad27-b3a3fb507744 | -20.44389 | -57.87685 | 2026-01-17 04:50:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.2 |
| 83200975-53ed-3336-abf0-e056710e2290 | -15.43946 | -56.33203 | 2026-01-17 04:50:00 | NOAA-20 | VÁRZEA GRANDE | MATO GROSSO | Brasil | 5108402 | 51 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 2409bb13-7a4e-3355-8626-69bd94407fa4 | -18.81968 | -51.60656 | 2026-01-17 04:50:00 | NOAA-20 | ITAJÁ | GOIÁS | Brasil | 5210802 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 273098f4-c987-3e3f-acf3-15e760fd0570 | -17.76918 | -54.13298 | 2026-01-17 04:50:00 | NOAA-20 | PEDRO GOMES | MATO GROSSO DO SUL | Brasil | 5006408 | 50 | 33 | nan | nan | nan | Cerrado | 0.7 |
| bc42a054-7533-3937-b1e6-985c55760039 | -20.84244 | -51.73771 | 2026-01-17 04:50:00 | NOAA-20 | TRÊS LAGOAS | MATO GROSSO DO SUL | Brasil | 5008305 | 50 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| feda2dc5-e849-37d1-b498-79f323788006 | -15.43019 | -56.32164 | 2026-01-17 04:50:00 | NOAA-20 | VÁRZEA GRANDE | MATO GROSSO | Brasil | 5108402 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| d4e0056f-6b9e-35c6-94a7-564a7f231e3d | -20.44116 | -57.87463 | 2026-01-17 04:50:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.0 |
| 83c14713-5a87-35a8-8f91-592f315bfff9 | -16.1102 | -56.75439 | 2026-01-17 04:50:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Cerrado | 3.9 |
| b9070eb3-d1d9-3d10-abc7-def6347da802 | -20.45481 | -57.88198 | 2026-01-17 04:50:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.3 |
| 205f4411-85de-3acf-84f8-515f167e1da9 | -20.41977 | -57.78048 | 2026-01-17 04:50:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 0.7 |
| 7e94c58b-057a-3daa-9c68-90fbf4574179 | -18.32688 | -42.98849 | 2026-01-17 04:50:00 | NOAA-20 | RIO VERMELHO | MINAS GERAIS | Brasil | 3156007 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| 85814139-1035-3165-895f-2af27651eef6 | -19.17272 | -57.54169 | 2026-01-17 04:50:00 | NOAA-20 | LADÁRIO | MATO GROSSO DO SUL | Brasil | 5005202 | 50 | 33 | nan | nan | nan | Pantanal | 1.1 |
| f9d78922-7345-3fe5-ad2f-9c8b1bc0355a | -20.72952 | -55.16221 | 2026-01-17 04:50:00 | NOAA-20 | SIDROLÂNDIA | MATO GROSSO DO SUL | Brasil | 5007901 | 50 | 33 | nan | nan | nan | Cerrado | 1.6 |
| fe8eb04e-70fa-3c66-8d4f-255bdf588ca9 | -15.96788 | -56.27594 | 2026-01-17 04:50:00 | NOAA-20 | NOSSA SENHORA DO LIVRAMENTO | MATO GROSSO | Brasil | 5106109 | 51 | 33 | nan | nan | nan | Pantanal | 1.2 |
| 216f3845-e06c-39f1-bd19-fc0d07b3b685 | -15.97143 | -56.27658 | 2026-01-17 04:50:00 | NOAA-20 | NOSSA SENHORA DO LIVRAMENTO | MATO GROSSO | Brasil | 5106109 | 51 | 33 | nan | nan | nan | Pantanal | 2.0 |
| 556b450c-7fa2-3365-886a-f12cf56802da | -16.58612 | -57.80457 | 2026-01-17 04:50:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.0 |
| 57c4d451-9337-3030-b0c5-b6e9fadd93f3 | -20.45762 | -57.88715 | 2026-01-17 04:50:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.3 |
| 55623c98-d6fb-34c9-a9b8-fe8093c5b1f3 | -20.44397 | -57.87979 | 2026-01-17 04:50:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 10.8 |
| c23cf1d5-71af-3c68-9751-f2c1586a84b7 | -18.19693 | -54.49414 | 2026-01-17 04:50:00 | NOAA-20 | COXIM | MATO GROSSO DO SUL | Brasil | 5003306 | 50 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 622487c3-a5be-325e-ae41-134eafecbe4c | -16.58991 | -57.80535 | 2026-01-17 04:50:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.2 |
| 645b6dd8-52dd-3156-8acb-807b1d2c2058 | -15.43232 | -56.3307 | 2026-01-17 04:50:00 | NOAA-20 | VÁRZEA GRANDE | MATO GROSSO | Brasil | 5108402 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 76225441-931b-3020-812a-4473ca7c2356 | -20.44312 | -57.88129 | 2026-01-17 04:50:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.1 |
| 4b688863-865d-37aa-85e3-82ea6c1b3e25 | -15.43589 | -56.33136 | 2026-01-17 04:50:00 | NOAA-20 | VÁRZEA GRANDE | MATO GROSSO | Brasil | 5108402 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| b084d8a5-d5b3-3659-9cf2-4b3bc1f90c53 | -17.60836 | -46.65708 | 2026-01-17 04:50:00 | NOAA-20 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 535ec606-4eb0-3d43-a782-94d1ba822ba0 | -20.40525 | -57.84151 | 2026-01-17 04:50:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.6 |
| 76fb9094-a476-303c-b7ad-4d7e33385c7b | -18.19361 | -54.49357 | 2026-01-17 04:50:00 | NOAA-20 | COXIM | MATO GROSSO DO SUL | Brasil | 5003306 | 50 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 54751c0b-f30a-36f6-9399-1aa12f1caac6 | -20.43872 | -57.88501 | 2026-01-17 04:50:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 10.8 |
| 19706b35-86c5-31ce-a45e-982e8f22eb4d | -20.43955 | -57.8835 | 2026-01-17 04:50:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 10.8 |
| 1849838a-0217-3012-8800-71323a9853b2 | -20.43228 | -57.8791 | 2026-01-17 04:50:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.0 |
| c9ee53d4-2329-3521-b96a-1e28d67cbf02 | -20.4395 | -57.88056 | 2026-01-17 04:50:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 10.8 |
| b4bddf7a-f139-3a60-ac42-33f148cfea2d | -24.95798 | -49.28893 | 2026-01-17 04:53:00 | NOAA-20 | CERRO AZUL | PARANÁ | Brasil | 4105201 | 41 | 33 | nan | nan | nan | Mata Atlântica | 3.0 |
| 300f3c12-fae1-399e-8d4c-2be9bb4d5c61 | -25.719 | -51.59379 | 2026-01-17 04:53:00 | NOAA-20 | PINHÃO | PARANÁ | Brasil | 4119301 | 41 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| eecc25fe-009f-39d0-b4c2-e470c6e24991 | -24.96099 | -49.29251 | 2026-01-17 04:53:00 | NOAA-20 | CERRO AZUL | PARANÁ | Brasil | 4105201 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| e7690d28-6c7f-3bf4-be5d-8cfe93353693 | -24.95676 | -49.29168 | 2026-01-17 04:53:00 | NOAA-20 | CERRO AZUL | PARANÁ | Brasil | 4105201 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| 52be9c30-e1f7-30b3-98a9-ff865b0c148d | -13.6993 | -55.6773 | 2026-01-17 05:00:00 | GOES-19 | NOVA MUTUM | MATO GROSSO | Brasil | 5106224 | 51 | 33 | nan | nan | nan | Cerrado | 57.9 |
| 83d78cdd-3401-3472-8ee0-4794d62ac21c | -13.6993 | -55.6773 | 2026-01-17 05:10:00 | GOES-19 | NOVA MUTUM | MATO GROSSO | Brasil | 5106224 | 51 | 33 | nan | nan | nan | Cerrado | 55.4 |
| 0e30187c-c1dc-3088-9ac5-57ba8bc92776 | -13.6993 | -55.6773 | 2026-01-17 05:30:00 | GOES-19 | NOVA MUTUM | MATO GROSSO | Brasil | 5106224 | 51 | 33 | nan | nan | nan | Cerrado | 63.4 |
| 0f0a0fcb-7bba-31d7-ac19-12c9429e2b1b | 2.75402 | -60.3177 | 2026-01-17 05:33:00 | NOAA-21 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 1.8 |


[Clique aqui para ver as próximas entradas](README10.md)
