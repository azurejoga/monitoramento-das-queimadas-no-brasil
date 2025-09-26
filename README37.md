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

## Dados Diários - Página 37

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| e037334d-9d0b-3145-b290-e82ef11db86f | -15.52015 | -50.4288 | 2025-09-26 04:44:00 | NPP-375D | FAINA | GOIÁS | Brasil | 5207535 | 52 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 5ec2d173-09f6-324e-95c0-aafad398e167 | -10.93464 | -44.296 | 2025-09-26 04:44:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 0d508b65-d7e5-3e7b-8bd6-d3cdbd055adb | -14.77001 | -60.19077 | 2025-09-26 04:44:00 | NPP-375D | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a4995da9-097f-3955-b244-13eebd68c750 | -14.82709 | -52.92356 | 2025-09-26 04:44:00 | NPP-375D | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 28bf7ade-695a-332f-8244-dc389d71ece0 | -15.38283 | -46.10975 | 2025-09-26 04:44:00 | NPP-375D | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| f9a1c44a-5a22-357f-843c-289afa97e6b3 | -15.91261 | -57.49741 | 2025-09-26 04:44:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| f210e365-8cd9-3b73-816b-77176771ae47 | -16.40348 | -54.82973 | 2025-09-26 04:44:00 | NPP-375D | RONDONÓPOLIS | MATO GROSSO | Brasil | 5107602 | 51 | 33 | nan | nan | nan | Cerrado | 3.4 |
| c39898fc-3c8e-3680-ada3-05e1f52072ea | -13.53853 | -47.71033 | 2025-09-26 04:44:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 7b810e51-b88d-3dcf-b2c3-b75eb4679af3 | -11.25064 | -45.54457 | 2025-09-26 04:44:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 12.4 |
| 268dccc7-022d-3fce-ad12-4fa9042a1b6d | -10.54072 | -47.52383 | 2025-09-26 04:44:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 8e9cb0b2-9b97-3652-a1a0-ef09fb0a07eb | -15.72488 | -59.49625 | 2025-09-26 04:44:00 | NPP-375D | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 86b64fbb-3642-3d8b-aef6-17e36730449f | -11.65023 | -45.34643 | 2025-09-26 04:44:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| a4784c12-dc4a-3f68-bebc-61e8c29cbfd1 | -15.93928 | -59.50133 | 2025-09-26 04:44:00 | NPP-375D | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 144418a2-8083-360a-bc82-85dfbcb96bd5 | -11.38924 | -44.94348 | 2025-09-26 04:44:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| a9b112e9-51f2-3feb-8394-05e6a9be3ebf | -12.13491 | -47.95169 | 2025-09-26 04:44:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| f7a32ac4-bd08-377c-8116-ab584f4727f3 | -18.25065 | -45.01446 | 2025-09-26 04:44:00 | NPP-375D | TRÊS MARIAS | MINAS GERAIS | Brasil | 3169356 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| c2932c1d-6c5c-3f90-a4d6-e50746e024d2 | -14.76049 | -48.35561 | 2025-09-26 04:44:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 47747774-5aaf-3d71-9508-ec9e4b8f1eb0 | -14.87875 | -45.5449 | 2025-09-26 04:44:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| b2ab0229-1712-32b9-b6d6-a6b855caa23b | -14.77982 | -60.19487 | 2025-09-26 04:44:00 | NPP-375D | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 507e3e25-9ab5-3100-a0b7-e233350628fd | -11.97823 | -46.62898 | 2025-09-26 04:44:00 | NPP-375D | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 2ef91812-6eb4-3ed8-97a2-5daada1e17e8 | -15.24181 | -48.07975 | 2025-09-26 04:44:00 | NPP-375D | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| fef69553-2be4-349a-bf06-bc2e7077d2f5 | -15.87878 | -59.33582 | 2025-09-26 04:44:00 | NPP-375D | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 26c562ec-afad-3a8c-9053-ea8cd5373995 | -11.24108 | -45.55408 | 2025-09-26 04:44:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 23.3 |
| 7198ab7f-ffd4-35f9-90e0-5f390982d577 | -11.0469 | -49.47229 | 2025-09-26 04:44:00 | NPP-375D | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| a7cae14c-6c51-3036-bd3f-4ca24fcc868f | -14.88353 | -45.5414 | 2025-09-26 04:44:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| c6de2187-1766-31e4-a6b5-2b7a3e1bbf26 | -16.20708 | -53.86081 | 2025-09-26 04:44:00 | NPP-375D | GUIRATINGA | MATO GROSSO | Brasil | 5104203 | 51 | 33 | nan | nan | nan | Cerrado | 0.6 |
| a97b6319-27c0-3b4a-a07f-d15257f9d380 | -15.93815 | -59.50698 | 2025-09-26 04:44:00 | NPP-375D | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 7042dc8c-c549-3400-9c8c-fc55e6d2f1c8 | -11.68038 | -44.45715 | 2025-09-26 04:44:00 | NPP-375D | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 2cc85957-6ef0-3418-a797-6e8e87a1c939 | -15.57907 | -51.68306 | 2025-09-26 04:44:00 | NPP-375D | MONTES CLAROS DE GOIÁS | GOIÁS | Brasil | 5213707 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| e4348c35-f37b-3bcd-9f3d-2887be1e876c | -11.22137 | -45.57257 | 2025-09-26 04:44:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 10.7 |
| 1678b7c3-9b09-3122-85fa-841411d2fc1e | -15.27473 | -46.42678 | 2025-09-26 04:44:00 | NPP-375D | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| dd9acc8e-69c7-387b-b1b5-7275ee71f391 | -11.7043 | -44.41038 | 2025-09-26 04:44:00 | NPP-375D | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 13019df4-bba2-3691-9b21-555bd16eb704 | -14.15249 | -46.9786 | 2025-09-26 04:44:00 | NPP-375D | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 99efa015-5cae-39b5-9123-dfde9a83fe5a | -16.30746 | -48.72961 | 2025-09-26 04:44:00 | NPP-375D | GAMELEIRA DE GOIÁS | GOIÁS | Brasil | 5208152 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| bdd8b144-be15-3668-b238-8090dd0807ab | -11.22151 | -45.57657 | 2025-09-26 04:44:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 7dca0e2f-bf56-3cae-af11-631eee3d5302 | -12.14144 | -47.95683 | 2025-09-26 04:44:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| a1742ca1-81b0-32b4-af8e-6a47aacd1483 | -15.59178 | -46.45878 | 2025-09-26 04:44:00 | NPP-375D | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| c24003ef-d129-35eb-8985-52f6e78a5cd6 | -11.65731 | -45.35577 | 2025-09-26 04:44:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 7a38348c-e03e-3ef6-824f-3fcd309099ed | -11.61103 | -44.44302 | 2025-09-26 04:44:00 | NPP-375D | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| cdfd8491-524d-35db-8316-83e5ffded051 | -14.77415 | -60.19669 | 2025-09-26 04:44:00 | NPP-375D | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| b8768540-1fba-38f6-8b94-ec203796b9c1 | -11.02164 | -44.64602 | 2025-09-26 04:44:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 19acb675-65c0-3dc1-8e08-024b3d542834 | -10.43158 | -48.20913 | 2025-09-26 04:44:00 | NPP-375D | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| f0e88b22-dbb7-328c-953f-8b7d3a3462b9 | -15.93945 | -59.50616 | 2025-09-26 04:44:00 | NPP-375D | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 3.7 |
| e580f052-1d10-3034-91a6-52d0eff5b82b | -11.69624 | -44.40729 | 2025-09-26 04:44:00 | NPP-375D | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| d8a6ff57-d3aa-312d-b753-11cfefe92316 | -11.23704 | -45.5535 | 2025-09-26 04:44:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 23.3 |
| 50418a2d-cfdf-3a60-9454-1d21318dae7e | -15.8834 | -59.33486 | 2025-09-26 04:44:00 | NPP-375D | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c33b25ac-ca20-31a1-9e2e-242ac31ee974 | -12.02276 | -46.50936 | 2025-09-26 04:44:00 | NPP-375D | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 9cd37ae7-240e-3b05-8c2b-e9f5cc396619 | -12.0266 | -46.50998 | 2025-09-26 04:44:00 | NPP-375D | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 9c6fb345-9f2b-3175-bdfe-d7075821121f | -15.92941 | -57.5006 | 2025-09-26 04:44:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 11062f5f-559d-3316-916a-5f1a87594db7 | -11.24059 | -45.55764 | 2025-09-26 04:44:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 11.2 |
| f0d3a887-e3ec-3cda-a781-b30d0b9c1926 | -11.97059 | -46.62782 | 2025-09-26 04:44:00 | NPP-375D | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 44dc7068-73bd-3c2c-923d-d6c3607451c6 | -11.19528 | -46.30293 | 2025-09-26 04:44:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| a585408a-bece-3fc3-a7c9-b62f1b307810 | -12.84729 | -44.70783 | 2025-09-26 04:44:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 456e3871-0c54-3847-b328-adab61685acc | -11.38332 | -44.95507 | 2025-09-26 04:44:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 8c8b7b6f-0542-3015-9060-73944e2b8407 | -11.68013 | -44.4268 | 2025-09-26 04:44:00 | NPP-375D | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 617b6afc-1e18-379a-b22e-7a397344cf63 | -12.55898 | -45.84724 | 2025-09-26 04:44:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| e157c231-221f-37fb-ae93-59ebc5794d3b | -15.02439 | -46.93991 | 2025-09-26 04:44:00 | NPP-375D | VILA BOA | GOIÁS | Brasil | 5222203 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 256f84b9-f845-3bad-8ea7-9873848995a0 | -11.21736 | -45.57182 | 2025-09-26 04:44:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 10.7 |
| fa773296-bf0f-3569-a897-272ac7ef98a2 | -11.67719 | -44.44806 | 2025-09-26 04:44:00 | NPP-375D | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 76c2884f-b706-3148-b8af-727ba6b3d822 | -10.93902 | -44.29661 | 2025-09-26 04:44:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| b7855db0-e1db-3624-84e4-eb5eae34d360 | -16.51375 | -50.10158 | 2025-09-26 04:44:00 | NPP-375D | TURVÂNIA | GOIÁS | Brasil | 5221502 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 144a584d-4b57-3ad1-998d-40ee66794cca | -13.84955 | -45.62039 | 2025-09-26 04:44:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| be49ed38-ec5a-3c96-9287-84fcda3174c6 | -12.73831 | -46.8251 | 2025-09-26 04:44:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| e9b18650-33a7-3948-898f-f3369fe2807a | -19.07997 | -48.15482 | 2025-09-26 04:46:00 | NPP-375D | UBERLÂNDIA | MINAS GERAIS | Brasil | 3170206 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 5860c8ef-521c-3d8a-9d7a-ad4c9e227136 | -23.11873 | -54.44898 | 2025-09-26 04:46:00 | NPP-375D | IGUATEMI | MATO GROSSO DO SUL | Brasil | 5004304 | 50 | 33 | nan | nan | nan | Mata Atlântica | 3.4 |
| 575e7371-69fb-3522-bc81-f28266c98153 | -17.94573 | -55.86523 | 2025-09-26 04:46:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.1 |
| ad876a04-9e6b-302d-8c69-989371efef26 | -18.30005 | -57.09921 | 2025-09-26 04:46:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 5.2 |
| cc0a9665-f7ce-3016-8f81-d3af2ba5ba7a | -17.19409 | -56.36946 | 2025-09-26 04:46:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.2 |
| 2d149518-0a5c-3b94-aa59-b870f82edbfb | -21.00724 | -50.0177 | 2025-09-26 04:46:00 | NPP-375D | PLANALTO | SÃO PAULO | Brasil | 3539608 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 97f133b0-609d-3bde-9de8-fa6113987758 | -20.99478 | -50.00279 | 2025-09-26 04:46:00 | NPP-375D | PLANALTO | SÃO PAULO | Brasil | 3539608 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 931a63ea-3195-3038-8bf1-9223ae757633 | -17.92804 | -55.85016 | 2025-09-26 04:46:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.1 |
| 5533e974-50ca-3a10-b678-9cf1bcb47474 | -17.1988 | -56.36526 | 2025-09-26 04:46:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.5 |
| e8447540-0b7b-359c-b3b0-5ed75c7f9783 | -17.17961 | -56.36148 | 2025-09-26 04:46:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.6 |
| f61d3099-a7e9-3c36-aeb9-35cb569ae1be | -20.99239 | -50.01968 | 2025-09-26 04:46:00 | NPP-375D | PLANALTO | SÃO PAULO | Brasil | 3539608 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 1d56cd9c-3d2d-337a-992e-cb69d9a61028 | -22.61042 | -49.02128 | 2025-09-26 04:46:00 | NPP-375D | AGUDOS | SÃO PAULO | Brasil | 3500709 | 35 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 4a517a9e-cf98-3b4f-8d84-841c8c58805a | -17.17489 | -56.36567 | 2025-09-26 04:46:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.3 |
| 600bebbe-3ffb-3812-ba35-3edadb6446e3 | -20.55968 | -57.08363 | 2025-09-26 04:46:00 | NPP-375D | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 10dd935b-f54c-309f-9be0-8124e6fc7da5 | -18.55149 | -46.96425 | 2025-09-26 04:46:00 | NPP-375D | COROMANDEL | MINAS GERAIS | Brasil | 3119302 | 31 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 669590af-c532-3c85-9ef0-614498eb168c | -22.13202 | -50.01824 | 2025-09-26 04:46:00 | NPP-375D | MARÍLIA | SÃO PAULO | Brasil | 3529005 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| d3c66e36-9473-3fde-8246-384104bbcd92 | -20.53908 | -57.07748 | 2025-09-26 04:46:00 | NPP-375D | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 2.1 |
| e94079a8-0f6c-372e-96ac-e0ff597fe403 | -21.00131 | -50.00815 | 2025-09-26 04:46:00 | NPP-375D | PLANALTO | SÃO PAULO | Brasil | 3539608 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.9 |
| e8ee12b0-bff7-39cb-ae5b-a2ef505bf127 | -20.98901 | -50.47049 | 2025-09-26 04:46:00 | NPP-375D | SANTO ANTÔNIO DO ARACANGUÁ | SÃO PAULO | Brasil | 3548054 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| a61e30aa-859b-337f-a40e-422ee35412f9 | -21.00428 | -50.01293 | 2025-09-26 04:46:00 | NPP-375D | PLANALTO | SÃO PAULO | Brasil | 3539608 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.9 |
| 0d017d56-9f6f-32d4-a3d1-10858008b351 | -20.55635 | -57.14442 | 2025-09-26 04:46:00 | NPP-375D | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 2.2 |
| a3a4f653-c0a7-380f-ab6d-f5ea47f099bd | -23.12209 | -54.44962 | 2025-09-26 04:46:00 | NPP-375D | IGUATEMI | MATO GROSSO DO SUL | Brasil | 5004304 | 50 | 33 | nan | nan | nan | Mata Atlântica | 3.4 |
| 32ab8712-0c02-379b-afee-ce9b4fca8f7f | -20.55726 | -57.13948 | 2025-09-26 04:46:00 | NPP-375D | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 2.8 |
| f1eb2386-8ed9-3e25-8a33-6a1ed94eba9d | -20.99774 | -50.00761 | 2025-09-26 04:46:00 | NPP-375D | PLANALTO | SÃO PAULO | Brasil | 3539608 | 35 | 33 | nan | nan | nan | Mata Atlântica | 4.3 |
| c5a467fd-99b0-3e8b-8c29-5c3ba90de6d4 | -17.17577 | -56.36073 | 2025-09-26 04:46:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 0.7 |
| 296432b0-2c48-35ef-b512-c22630f0ad41 | -20.55543 | -57.14938 | 2025-09-26 04:46:00 | NPP-375D | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 2.2 |
| fdf9644c-b535-39a0-902b-c5134418d616 | -17.18867 | -56.36081 | 2025-09-26 04:46:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.4 |
| 0aa91e28-7e5f-3e0c-a5ec-e2a37e02225b | -21.22746 | -49.04099 | 2025-09-26 04:46:00 | NPP-375D | CATANDUVA | SÃO PAULO | Brasil | 3511102 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.9 |
| 3568e609-8338-3753-948a-73b12dd9a127 | -20.99122 | -50.00219 | 2025-09-26 04:46:00 | NPP-375D | PLANALTO | SÃO PAULO | Brasil | 3539608 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.4 |
| 1a2c6643-cc3a-32fc-841e-66c17ffd28bd | -18.30791 | -57.1008 | 2025-09-26 04:46:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.3 |
| 95f9803d-a84e-307c-988d-92d431079d19 | -17.19793 | -56.37021 | 2025-09-26 04:46:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.2 |
| bfd609c5-0fff-31e1-9bda-f45931405dd0 | -21.01315 | -50.02738 | 2025-09-26 04:46:00 | NPP-375D | PLANALTO | SÃO PAULO | Brasil | 3539608 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 99bed5e9-d460-31ff-b08f-1ad824048e4f | -20.553 | -57.07713 | 2025-09-26 04:46:00 | NPP-375D | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 1.8 |
| ac40321d-cabf-335b-910c-101b0330e94c | -22.13561 | -50.01887 | 2025-09-26 04:46:00 | NPP-375D | MARÍLIA | SÃO PAULO | Brasil | 3529005 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 4642221c-8664-35fb-81ec-0522513c3997 | -17.18345 | -56.36224 | 2025-09-26 04:46:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.6 |
| 7e5d09cd-9b20-3989-b167-f1b70689c9c1 | -20.97756 | -50.02154 | 2025-09-26 04:46:00 | NPP-375D | PLANALTO | SÃO PAULO | Brasil | 3539608 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| f474d4a2-c906-3da2-9d17-9bf654f8b6d8 | -21.03587 | -51.11389 | 2025-09-26 04:46:00 | NPP-375D | MIRANDÓPOLIS | SÃO PAULO | Brasil | 3530102 | 35 | 33 | nan | nan | nan | Mata Atlântica | 10.5 |


[Clique aqui para ver as próximas entradas](README38.md)
