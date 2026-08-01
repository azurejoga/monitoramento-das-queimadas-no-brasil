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

## Dados Diários - Página 3

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 9c61ede4-daa6-302d-8b5e-04578a3e55d5 | -1.6591 | -54.4543 | 2026-08-01 00:50:00 | GOES-19 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 59.5 |
| 2c807789-07cd-31f8-8e6c-4282776fe278 | -11.2404 | -54.833 | 2026-08-01 00:50:00 | GOES-19 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 48.7 |
| dfb7ef82-b2c5-3459-be83-397e4fd234b8 | -11.2402 | -54.8534 | 2026-08-01 00:50:00 | GOES-19 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 374.4 |
| ac023c5a-e757-300f-a530-120479c1be3b | -5.5608 | -43.9775 | 2026-08-01 00:50:00 | GOES-19 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 56.8 |
| efa083fb-5107-3ac3-b504-b586e395d129 | -8.6191 | -50.0256 | 2026-08-01 00:56:00 | METOP-C | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 65f3164b-6ffe-3a6e-99e2-0c0ab1f7f701 | -8.2823 | -49.381599 | 2026-08-01 00:56:00 | METOP-C | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 6a075c69-2864-32dc-89a1-d546533eaa04 | -11.2495 | -54.851002 | 2026-08-01 00:56:00 | METOP-C | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 9a39a8ae-cbe1-3647-a653-33dbd7f9aa2a | -14.0716 | -46.244301 | 2026-08-01 00:56:00 | METOP-C | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| f1be1f65-2be9-31b6-9090-bfd40764dc99 | -4.2788 | -48.198002 | 2026-08-01 00:56:00 | METOP-C | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 6bcf26d0-84a4-3565-b00f-10c454ac9c28 | -11.2415 | -54.861401 | 2026-08-01 00:56:00 | METOP-C | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 04986936-08ff-3e84-8889-809a80360566 | -4.2763 | -48.187401 | 2026-08-01 00:56:00 | METOP-C | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 47a5b435-b739-3ac3-9f42-2426245f1e8d | -11.2281 | -54.846901 | 2026-08-01 00:56:00 | METOP-C | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| a82db117-8ffa-3195-a29c-5f862dcf28c0 | -2.8858 | -48.0093 | 2026-08-01 00:56:00 | METOP-C | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 591a595f-cbf4-3a8d-b1fa-79fecf3147c9 | -7.2965 | -55.320202 | 2026-08-01 00:56:00 | METOP-C | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b66ce009-a5be-36df-a6f6-efa2673d4122 | -11.4401 | -50.618198 | 2026-08-01 00:56:00 | METOP-C | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 86cdf1be-805c-345e-b283-9658fef2e2e2 | -17.059401 | -45.884399 | 2026-08-01 00:56:00 | METOP-C | BRASILÂNDIA DE MINAS | MINAS GERAIS | Brasil | 3108552 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| cf69b1a5-9117-3fe1-8c13-9aef6819389f | -8.1855 | -55.438 | 2026-08-01 00:56:00 | METOP-C | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 40c73865-bbc7-3cb3-9452-d12e305a2a1b | -2.8982 | -48.018398 | 2026-08-01 00:56:00 | METOP-C | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 86bc11a5-59cb-3ea1-a426-f05fe4118e23 | -13.0663 | -52.719898 | 2026-08-01 00:56:00 | METOP-C | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| e333e871-1807-361f-946a-9e602c26b758 | -3.119 | -47.9072 | 2026-08-01 00:56:00 | METOP-C | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 3f6a1f15-67f1-315c-8f7e-206da0477dfd | -11.2397 | -54.8531 | 2026-08-01 00:56:00 | METOP-C | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| af1b61e3-0e06-3e4f-8e53-dafc8a82bcb7 | -20.3706 | -57.9981 | 2026-08-01 00:56:00 | METOP-C | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 97b404a2-4270-3809-86cf-d3d5e34af411 | -11.2513 | -54.859299 | 2026-08-01 00:56:00 | METOP-C | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 45e04826-4db5-3e15-bd4a-9ea7e4d1d11c | -7.647 | -45.041401 | 2026-08-01 00:56:00 | METOP-C | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 6312a117-445f-3c65-8a56-a0fcec21c822 | -14.349 | -48.0341 | 2026-08-01 00:56:00 | METOP-C | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| f95f3de1-757c-3d7d-977f-9f8821faac9d | -14.3471 | -48.025902 | 2026-08-01 00:56:00 | METOP-C | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| a74e537f-15db-3aab-956f-a7e3dd43d680 | -9.8862 | -48.739399 | 2026-08-01 00:56:00 | METOP-C | BARROLÂNDIA | TOCANTINS | Brasil | 1703107 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 3d62d561-fa5f-3f2c-b8d1-ae1cb3490ed5 | -4.6143 | -49.052799 | 2026-08-01 00:56:00 | METOP-C | JACUNDÁ | PARÁ | Brasil | 1503804 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 9fc40aa8-3e73-3f24-bec4-baced07d4b7c | -6.5607 | -55.1553 | 2026-08-01 00:56:00 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0131cef2-d157-366e-b305-ab69fea7b99e | -2.604 | -47.335602 | 2026-08-01 00:56:00 | METOP-C | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 8507e8be-69e2-3be3-bfae-c6857c79f1f4 | -6.7692 | -41.002102 | 2026-08-01 00:56:00 | METOP-C | MONSENHOR HIPÓLITO | PIAUÍ | Brasil | 2206506 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 56bfca23-2778-3265-a0ad-07b133a3d0ef | -7.6507 | -45.056702 | 2026-08-01 00:56:00 | METOP-C | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 945c5894-ba3f-30c6-880a-ee2a39dc7be4 | -7.5035 | -45.839401 | 2026-08-01 00:56:00 | METOP-C | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| d0e8b990-20cf-3d5a-97c4-398c2c370cae | -5.5603 | -43.963299 | 2026-08-01 00:56:00 | METOP-C | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| a07fc68b-91ca-30b8-b5af-ba1317dfc203 | -14.0788 | -46.231602 | 2026-08-01 00:56:00 | METOP-C | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| db624f06-9b0d-3536-8a0a-8237329f9687 | -5.5652 | -43.9828 | 2026-08-01 00:56:00 | METOP-C | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 93cc311b-987f-38e9-8f99-6c782c69be8b | -11.4385 | -50.611099 | 2026-08-01 00:56:00 | METOP-C | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 0f626eb9-7c66-3770-a1bb-151fb5f57683 | -6.5624 | -55.162899 | 2026-08-01 00:56:00 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 5f048d9c-0c1a-3e85-a099-1806ce7e00e9 | -13.9589 | -49.1437 | 2026-08-01 00:56:00 | METOP-C | MARA ROSA | GOIÁS | Brasil | 5212808 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| a6f50358-c868-3ed4-8505-f515ce96ef95 | -17.0569 | -45.874599 | 2026-08-01 00:56:00 | METOP-C | BRASILÂNDIA DE MINAS | MINAS GERAIS | Brasil | 3108552 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 4c05db4b-d5b7-36fd-ac66-1465d2a3938d | -2.8885 | -48.020699 | 2026-08-01 00:56:00 | METOP-C | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 9876b9e9-abe7-352e-8b6c-f2f4395dceb1 | -2.8956 | -48.007 | 2026-08-01 00:56:00 | METOP-C | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 7034c837-12db-384b-b5bb-a209d8626c9b | -1.6513 | -54.444401 | 2026-08-01 00:56:00 | METOP-C | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 6910fbf5-2b61-3b75-8677-527d7e4647cb | -14.351 | -48.0424 | 2026-08-01 00:56:00 | METOP-C | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 436b0cd8-f078-37bd-ad35-5bcfa1eb5e26 | -18.526199 | -47.371101 | 2026-08-01 00:56:00 | METOP-C | ABADIA DOS DOURADOS | MINAS GERAIS | Brasil | 3100104 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 95fab1e3-faa7-3dae-a67d-8640e02d00ac | -14.0885 | -46.229099 | 2026-08-01 00:56:00 | METOP-C | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 6a93b423-6fca-3693-ad53-5376feef5148 | 1.0977 | -60.511501 | 2026-08-01 00:56:00 | METOP-C | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| 1c09b541-d302-300e-b114-c9fee7b546a6 | -8.1971 | -55.444099 | 2026-08-01 00:56:00 | METOP-C | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 48970de9-4355-3e04-8ff3-db059a0dc3d2 | -18.488199 | -51.7089 | 2026-08-01 00:56:00 | METOP-C | ITARUMÃ | GOIÁS | Brasil | 5211305 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| e150270e-f461-3488-99e9-ef8e4e5378ec | -9.8822 | -48.7225 | 2026-08-01 00:56:00 | METOP-C | BARROLÂNDIA | TOCANTINS | Brasil | 1703107 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 2920db88-364c-345a-93aa-23eb7d7818e2 | -6.0991 | -55.807098 | 2026-08-01 00:56:00 | METOP-C | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| da70571b-a521-33b0-b7b4-4c152b2d8397 | -8.1953 | -55.435902 | 2026-08-01 00:56:00 | METOP-C | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 5d7930df-7da0-343b-b268-95cbcf312fcf | -21.670401 | -56.3321 | 2026-08-01 00:56:00 | METOP-C | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| e4107a6f-84d4-3087-9f77-b44d214aec3b | -4.3738 | -47.772301 | 2026-08-01 00:56:00 | METOP-C | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ed2d7cd2-c70d-34bb-ac9a-8429d55521bf | 1.1046 | -60.525902 | 2026-08-01 00:56:00 | METOP-C | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| e5b8d14e-3283-3ca1-bbc3-ef519a4afc9b | -3.0405 | -48.4053 | 2026-08-01 00:56:00 | METOP-C | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 933653b2-d0fd-32e7-8b0c-3a8576c610f3 | -14.4135 | -48.044399 | 2026-08-01 00:56:00 | METOP-C | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 552e67f3-6a04-3317-a281-4b37e71ecbe2 | -1.6529 | -54.451199 | 2026-08-01 00:56:00 | METOP-C | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 79b02de4-8104-3ed3-948c-331c21c490a1 | -6.7673 | -41.034401 | 2026-08-01 00:56:00 | METOP-C | MONSENHOR HIPÓLITO | PIAUÍ | Brasil | 2206506 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| b8f44e2c-c030-3581-aa34-86b89385b389 | -1.6544 | -54.458099 | 2026-08-01 00:56:00 | METOP-C | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c82b38b1-9e73-39a8-adb7-65e6bf4a1673 | -11.4271 | -50.6063 | 2026-08-01 00:56:00 | METOP-C | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 53331d39-f7cc-3d33-ade1-d05896b70b73 | -21.6607 | -56.334 | 2026-08-01 00:56:00 | METOP-C | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| 6c67af1c-5b66-31e4-9a6c-f3a27d911006 | -14.4115 | -48.036201 | 2026-08-01 00:56:00 | METOP-C | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 0dcbe63d-1231-3940-a146-76db74136677 | -11.2433 | -54.869801 | 2026-08-01 00:56:00 | METOP-C | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 1a7af53a-7eca-3af0-bdf6-eecc50ff5588 | -6.5589 | -55.147598 | 2026-08-01 00:56:00 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b18e7d24-d369-3289-9490-9b8a6dc3893b | -18.4849 | -51.693802 | 2026-08-01 00:56:00 | METOP-C | SERRANÓPOLIS | GOIÁS | Brasil | 5220504 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| a357f60b-6496-3007-977d-c3e3d01e7ca2 | -11.2451 | -54.878101 | 2026-08-01 00:56:00 | METOP-C | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| f2c0a201-1fd0-307e-b72a-008a9a11254a | -8.1677 | -55.4505 | 2026-08-01 00:56:00 | METOP-C | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 2e2fe2c6-9d72-34a2-a96e-8b4f11097c57 | -11.2379 | -54.844799 | 2026-08-01 00:56:00 | METOP-C | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 74de12d6-bdd7-3b86-bed3-02cddfb5cfab | -14.0838 | -46.252102 | 2026-08-01 00:56:00 | METOP-C | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| fdf28857-b6b8-3bc7-96fe-527786d3075c | -18.528099 | -47.3792 | 2026-08-01 00:56:00 | METOP-C | ABADIA DOS DOURADOS | MINAS GERAIS | Brasil | 3100104 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| ed6f60f3-a994-3adc-8335-1099c49437fa | -11.2245 | -54.8302 | 2026-08-01 00:56:00 | METOP-C | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 1bf3fb89-2eda-3dc3-b670-bb4a6fb3fd63 | -3.8617 | -44.099602 | 2026-08-01 00:56:00 | METOP-C | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| fa28aaaa-f4de-3679-a616-095f19e51113 | -2.607 | -47.348301 | 2026-08-01 00:56:00 | METOP-C | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 90c11ac6-e339-361a-b24a-4669e51e64fc | -4.6164 | -49.062099 | 2026-08-01 00:56:00 | METOP-C | JACUNDÁ | PARÁ | Brasil | 1503804 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 710c2f32-ec5c-30a1-8188-ebbbfb6cf325 | -11.4287 | -50.6134 | 2026-08-01 00:56:00 | METOP-C | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 6ea3dbf7-03a0-3715-9d2a-b7b19dc43a35 | -7.296 | -50.5937 | 2026-08-01 00:56:00 | METOP-C | BANNACH | PARÁ | Brasil | 1501253 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| faadd92d-f5c1-3f6a-933f-21a87a8974e2 | -11.4369 | -50.604 | 2026-08-01 00:56:00 | METOP-C | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 04dedd11-89a5-3fba-b72c-77c89a77f9fa | -14.3373 | -48.0284 | 2026-08-01 00:56:00 | METOP-C | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| ae2be9e1-395f-3a52-8cae-986aa2aef889 | -6.5641 | -55.170502 | 2026-08-01 00:56:00 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| cd07b368-78bd-33e3-8a5b-e15e2814b166 | -3.1092 | -47.909401 | 2026-08-01 00:56:00 | METOP-C | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| cbbae10e-189f-33d9-90f8-fa4e49a63a58 | -9.8842 | -48.730999 | 2026-08-01 00:56:00 | METOP-C | BARROLÂNDIA | TOCANTINS | Brasil | 1703107 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 5104cf77-962f-3cdb-9fb5-849b2973a75f | -14.3393 | -48.036598 | 2026-08-01 00:56:00 | METOP-C | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| ff04e88c-5472-3c2a-b5b5-a7ca6833f90f | -14.0741 | -46.254601 | 2026-08-01 00:56:00 | METOP-C | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| e75d642b-cef7-3fe9-9690-e561e154477d | -20.5224 | -48.861698 | 2026-08-01 00:56:00 | METOP-C | BARRETOS | SÃO PAULO | Brasil | 3505500 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 05f181db-11dc-302a-aa61-63f9017d4db9 | -11.2531 | -54.867699 | 2026-08-01 00:56:00 | METOP-C | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 0947941f-ada1-3d59-bd58-f9346dda5c11 | -14.0813 | -46.241798 | 2026-08-01 00:56:00 | METOP-C | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| be023111-9c1b-3f6d-957f-9a7974026ead | -8.1695 | -55.458698 | 2026-08-01 00:56:00 | METOP-C | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 67cae041-552a-344c-a1ff-5cfbd684a46c | -16.4886 | -49.0961 | 2026-08-01 00:56:00 | METOP-C | TEREZÓPOLIS DE GOIÁS | GOIÁS | Brasil | 5221197 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 96be40ba-e1a2-32ce-a0ac-aeb1790b89ec | -11.2477 | -54.842701 | 2026-08-01 00:56:00 | METOP-C | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 13afc74b-3f7b-3e70-951a-87bd86128a1e | -18.043301 | -51.310101 | 2026-08-01 00:56:00 | METOP-C | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 9d0520f4-0c1b-35f0-b0d0-46118bc7c50f | -18.530001 | -47.387299 | 2026-08-01 00:56:00 | METOP-C | ABADIA DOS DOURADOS | MINAS GERAIS | Brasil | 3100104 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 337c998a-8727-3017-9e26-ff5e640c404e | -4.6121 | -49.0434 | 2026-08-01 00:56:00 | METOP-C | JACUNDÁ | PARÁ | Brasil | 1503804 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 84395858-6ae6-339f-a056-fe59f469461a | -21.6679 | -56.317699 | 2026-08-01 00:56:00 | METOP-C | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| 9df7b608-dc97-38de-8c00-9b892b8449a6 | -3.1217 | -47.918701 | 2026-08-01 00:56:00 | METOP-C | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e324479f-b6c9-3772-a9c7-d0dc92d44c66 | -18.4865 | -51.701302 | 2026-08-01 00:56:00 | METOP-C | ITARUMÃ | GOIÁS | Brasil | 5211305 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| b3c5f214-92e5-383e-bbdd-f4a05999c114 | -6.7769 | -41.031898 | 2026-08-01 00:56:00 | METOP-C | MONSENHOR HIPÓLITO | PIAUÍ | Brasil | 2206506 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 5fd9a2e9-0fe7-33a9-ad2a-5ef422a2287b | -21.658199 | -56.319599 | 2026-08-01 00:56:00 | METOP-C | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| 9ff9873f-0970-3466-91a4-3c1541b3a495 | -7.5132 | -45.837002 | 2026-08-01 00:56:00 | METOP-C | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| b7825fb5-fa29-35f5-890c-020266e7d1aa | -11.2263 | -54.838501 | 2026-08-01 00:56:00 | METOP-C | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | nan |


[Clique aqui para ver as próximas entradas](README4.md)
