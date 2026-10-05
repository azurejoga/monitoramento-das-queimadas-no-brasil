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

## Dados Diários - Página 107

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 1a41e0de-691f-36bf-9578-625e599d29c8 | -9.85373 | -44.7922 | 2026-10-05 17:13:00 | NPP-375 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 16.1 |
| 13284c5e-7102-34f5-9edd-4c0461a44187 | -9.87543 | -44.84996 | 2026-10-05 17:13:00 | NPP-375 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 04ac691e-de17-3ecb-8d8f-2bab3ba9b8dd | -12.1426 | -50.99195 | 2026-10-05 17:13:00 | NPP-375 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 85df2950-7d13-35e1-ab30-1a1809b1e8b3 | -12.08975 | -43.41319 | 2026-10-05 17:13:00 | NPP-375 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 15.3 |
| e5c77c2d-5a68-3fa2-979d-696bdd1687fe | -12.58488 | -47.22134 | 2026-10-05 17:13:00 | NPP-375 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 9.0 |
| 3d5c9c79-2a42-3e38-8927-ae9dbe75241d | -9.84355 | -38.92078 | 2026-10-05 17:13:00 | NPP-375 | JEREMOABO | BAHIA | Brasil | 2918100 | 29 | 33 | nan | nan | nan | Caatinga | 8.1 |
| 8a5127cf-c7f8-396e-b941-42e244f467a5 | -11.20021 | -46.27309 | 2026-10-05 17:13:00 | NPP-375 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 7.0 |
| 32b35a1c-0f9a-37b9-98b1-a66ca3b05aca | -11.37015 | -47.51888 | 2026-10-05 17:13:00 | NPP-375 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 13.4 |
| 4c6a05de-b33a-3eb9-bbf7-a4365e301bd7 | -10.95857 | -45.43002 | 2026-10-05 17:13:00 | NPP-375 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 16.4 |
| 3a92f5d0-7a04-3b8c-843a-3c27647eb536 | -11.63317 | -43.62714 | 2026-10-05 17:13:00 | NPP-375 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 301c04bb-26a3-3ac4-91f1-ce50451ae5f3 | -11.16027 | -43.49161 | 2026-10-05 17:13:00 | NPP-375 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 11.3 |
| 7cfe9c72-8026-3ae4-b7d8-3f64a5578fe7 | -14.70314 | -58.67316 | 2026-10-05 17:13:00 | NPP-375 | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | 10.5 |
| 14970141-fa74-3f5d-93dd-83144c3c41ff | -12.56198 | -46.67744 | 2026-10-05 17:13:00 | NPP-375 | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 6.7 |
| d3098eb0-ca09-3b71-ab1a-6b622012dde5 | -9.85752 | -44.80745 | 2026-10-05 17:13:00 | NPP-375 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 11.1 |
| 88a51285-1a90-3ba4-93f2-585d0392b883 | -11.24678 | -43.52097 | 2026-10-05 17:13:00 | NPP-375 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 3.1 |
| b85b13f7-73f0-376c-b30e-e4b2197f5fbe | -11.37414 | -47.51813 | 2026-10-05 17:13:00 | NPP-375 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 13.4 |
| 90bacce4-05c6-3332-ac01-c3ee2a2fa9fe | -11.80902 | -47.3607 | 2026-10-05 17:13:00 | NPP-375 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 64154347-3ae2-3566-a3e4-ad413d887344 | -11.80561 | -47.36497 | 2026-10-05 17:13:00 | NPP-375 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| d25032c0-e655-36db-9db5-1a187d617551 | -14.85695 | -41.67828 | 2026-10-05 17:13:00 | NPP-375 | PRESIDENTE JÂNIO QUADROS | BAHIA | Brasil | 2925709 | 29 | 33 | nan | nan | nan | Caatinga | 8.8 |
| 0cceaeb9-f135-3898-bbb5-af3654058a64 | -9.96707 | -45.60631 | 2026-10-05 17:13:00 | NPP-375 | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 8b279688-56e0-3bcb-baa5-56287f6475a6 | -14.5748 | -41.39284 | 2026-10-05 17:13:00 | NPP-375 | CARAÍBAS | BAHIA | Brasil | 2906899 | 29 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 187e9e9a-423f-36cb-8770-4ab06a291587 | -10.48897 | -47.24386 | 2026-10-05 17:13:00 | NPP-375 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 40.8 |
| 1489974a-307e-3bb0-a70b-dcdbfee3dfc5 | -11.34094 | -46.67045 | 2026-10-05 17:13:00 | NPP-375 | RIO DA CONCEIÇÃO | TOCANTINS | Brasil | 1718659 | 17 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 3e832324-fd01-302a-a24a-c31c7ef90543 | -12.01936 | -62.52746 | 2026-10-05 17:13:00 | NPP-375 | SÃO MIGUEL DO GUAPORÉ | RONDÔNIA | Brasil | 1100320 | 11 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 51b5a6bf-bbe7-3988-a114-9f170de486dd | -12.88134 | -62.15038 | 2026-10-05 17:13:00 | NPP-375 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 77906e49-5a4b-3a61-8450-584c248a3143 | -9.85173 | -44.78077 | 2026-10-05 17:13:00 | NPP-375 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 7.5 |
| 164afb67-306b-3741-89d2-5179fd83492d | -11.77901 | -43.53956 | 2026-10-05 17:13:00 | NPP-375 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 10.0 |
| c6bd18e7-31f4-3059-a312-652e723c834e | -11.39994 | -50.84771 | 2026-10-05 17:13:00 | NPP-375 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 13.3 |
| b3713b7a-f682-3349-a215-1191a21789f6 | -10.96966 | -47.27329 | 2026-10-05 17:13:00 | NPP-375 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 5.3 |
| bc0edc7b-0b10-3746-8f34-1dafa83cf3b5 | -11.68594 | -43.65342 | 2026-10-05 17:13:00 | NPP-375 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 7.9 |
| 44593f49-4347-3b85-abab-7e32f1d2d23b | -12.28926 | -64.15919 | 2026-10-05 17:13:00 | NPP-375 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 9.4 |
| 21026ad5-970c-3177-8301-7de0bf086fa1 | -10.23573 | -46.66031 | 2026-10-05 17:13:00 | NPP-375 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 278547b7-bf04-3cb1-bda0-98392d7a4f58 | -12.80673 | -43.32002 | 2026-10-05 17:13:00 | NPP-375 | BOM JESUS DA LAPA | BAHIA | Brasil | 2903904 | 29 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 730e920d-5dd0-3422-9287-063263933b34 | -13.50131 | -40.84134 | 2026-10-05 17:13:00 | NPP-375 | IRAMAIA | BAHIA | Brasil | 2914307 | 29 | 33 | nan | nan | nan | Caatinga | 34.0 |
| 98c4f97a-8d16-387f-a30f-8b071f531794 | -12.92464 | -40.01721 | 2026-10-05 17:13:00 | NPP-375 | IAÇU | BAHIA | Brasil | 2911907 | 29 | 33 | nan | nan | nan | Caatinga | 4.9 |
| 8aa21519-73c0-3d75-9712-722fa1122587 | -11.37916 | -42.54812 | 2026-10-05 17:13:00 | NPP-375 | GENTIO DO OURO | BAHIA | Brasil | 2911303 | 29 | 33 | nan | nan | nan | Caatinga | 20.3 |
| 8cdfc917-8432-30ec-99db-7ea3ed20493f | -12.58124 | -40.80664 | 2026-10-05 17:13:00 | NPP-375 | IBIQUERA | BAHIA | Brasil | 2912608 | 29 | 33 | nan | nan | nan | Caatinga | 6.8 |
| e6377790-b297-3be1-8c67-39e1ee3a90fb | -10.53279 | -46.45126 | 2026-10-05 17:13:00 | NPP-375 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 5feb08c3-ab7c-316c-b415-0d64ef88c1a3 | -14.63349 | -40.56698 | 2026-10-05 17:13:00 | NPP-375 | PLANALTO | BAHIA | Brasil | 2925006 | 29 | 33 | nan | nan | nan | Mata Atlântica | 10.1 |
| 1b454c7a-eb8f-3e3c-bde2-b618132602c7 | -11.27883 | -44.2919 | 2026-10-05 17:13:00 | NPP-375 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 93.2 |
| 44f313da-6a61-30bc-914a-a6e87027598c | -10.33722 | -43.73018 | 2026-10-05 17:13:00 | NPP-375 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 11.3 |
| fe593e82-899b-3903-9279-bbe5089df6e0 | -9.78408 | -45.90254 | 2026-10-05 17:13:00 | NPP-375 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 11.6 |
| e503c183-3349-3e4a-8dde-6c167955fb44 | -10.33575 | -39.49172 | 2026-10-05 17:13:00 | NPP-375 | MONTE SANTO | BAHIA | Brasil | 2921500 | 29 | 33 | nan | nan | nan | Caatinga | 18.0 |
| b5f9ceb0-d3ab-318f-9311-59c9fbeaf860 | -11.24179 | -45.25804 | 2026-10-05 17:13:00 | NPP-375 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 14.4 |
| f88a5da9-37a9-33d9-aa6d-b1b5179d1b23 | -10.23142 | -46.66104 | 2026-10-05 17:13:00 | NPP-375 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 4.8 |
| bdb76cd9-d823-3c5b-b8cb-c308de176114 | -16.23452 | -41.79718 | 2026-10-05 17:13:00 | NPP-375 | COMERCINHO | MINAS GERAIS | Brasil | 3117009 | 31 | 33 | nan | nan | nan | Mata Atlântica | 5.9 |
| b1af950d-77b6-3dbf-af84-41d01daa5e06 | -16.33104 | -41.94851 | 2026-10-05 17:13:00 | NPP-375 | RUBELITA | MINAS GERAIS | Brasil | 3156502 | 31 | 33 | nan | nan | nan | Mata Atlântica | 7.0 |
| 6b6d8412-859a-3170-b1cc-54b7f82a6d79 | -11.11101 | -45.94389 | 2026-10-05 17:13:00 | NPP-375 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 7.5 |
| c1f7087d-ca85-32d0-af18-c4c0cf031781 | -14.692 | -41.90606 | 2026-10-05 17:13:00 | NPP-375 | GUAJERU | BAHIA | Brasil | 2911659 | 29 | 33 | nan | nan | nan | Caatinga | 4.3 |
| 910513ab-5b79-3f17-9fb6-4e066cf9d368 | -14.85616 | -41.67431 | 2026-10-05 17:13:00 | NPP-375 | PRESIDENTE JÂNIO QUADROS | BAHIA | Brasil | 2925709 | 29 | 33 | nan | nan | nan | Caatinga | 16.9 |
| 6832a7fa-e9db-36f2-8e7f-52bcfb495105 | -10.97226 | -45.42657 | 2026-10-05 17:13:00 | NPP-375 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 7.6 |
| fa3a78e7-aad4-3f80-93f2-975358341ced | -13.50229 | -61.13411 | 2026-10-05 17:13:00 | NPP-375 | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 7.9 |
| ad6dbecc-cd14-309c-99ac-6ed9769b92b7 | -13.54395 | -60.00769 | 2026-10-05 17:13:00 | NPP-375 | COMODORO | MATO GROSSO | Brasil | 5103304 | 51 | 33 | nan | nan | nan | Amazônia | 44.1 |
| b01a8178-8a5d-30b4-bff5-2faff6d8567b | -10.11537 | -45.89182 | 2026-10-05 17:13:00 | NPP-375 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 13c9b911-0cc3-3e79-a5f9-ef3653081053 | -14.85552 | -41.67671 | 2026-10-05 17:13:00 | NPP-375 | PRESIDENTE JÂNIO QUADROS | BAHIA | Brasil | 2925709 | 29 | 33 | nan | nan | nan | Caatinga | 11.3 |
| cbc8f3b2-a15d-3cd0-994e-4dccb649fa06 | -16.02433 | -45.13288 | 2026-10-05 17:13:00 | NPP-375 | PINTÓPOLIS | MINAS GERAIS | Brasil | 3150570 | 31 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 66a4160d-9ac1-3367-979e-ef224898ffa9 | -11.377 | -42.54667 | 2026-10-05 17:13:00 | NPP-375 | GENTIO DO OURO | BAHIA | Brasil | 2911303 | 29 | 33 | nan | nan | nan | Caatinga | 18.4 |
| d3efa53c-a02c-3419-837f-95e65d15d8f9 | -10.24431 | -49.65691 | 2026-10-05 17:13:00 | NPP-375 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 22fa7d2d-d3ce-38ff-a629-741b1612259a | -8.52607 | -39.54665 | 2026-10-05 17:13:00 | NPP-375 | OROCÓ | PERNAMBUCO | Brasil | 2609808 | 26 | 33 | nan | nan | nan | Caatinga | 7.7 |
| e70922f4-df10-30c8-8e0c-c6055f3dc218 | -11.21232 | -47.13104 | 2026-10-05 17:13:00 | NPP-375 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 8.8 |
| d02c2e34-0a52-38db-a979-ededc529c354 | -13.50084 | -61.13334 | 2026-10-05 17:13:00 | NPP-375 | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 10.1 |
| f99bece7-50ce-33fb-a31d-4019987a1881 | -6.69 | -45.27 | 2026-10-05 17:15:00 | MSG-03 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| b8d36b08-159d-3276-b481-4ba2f22e7772 | -3.11 | -53.69 | 2026-10-05 17:15:00 | MSG-03 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 16bcab93-14f3-37a9-9785-02e6dd217869 | -3.11 | -53.75 | 2026-10-05 17:15:00 | MSG-03 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 8016ff32-5868-34ed-a56b-49bf21bed12f | -6.72 | -45.27 | 2026-10-05 17:15:00 | MSG-03 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| c8c1c69e-9c29-366c-8d34-2e4ba8a797ba | -6.72 | -45.23 | 2026-10-05 17:15:00 | MSG-03 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| ef6874b9-ebdb-3721-889e-6c4cb3c1711b | -6.69 | -45.22 | 2026-10-05 17:15:00 | MSG-03 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 74825820-74df-3969-a249-4ab69594b6da | -5.85 | -45.01 | 2026-10-05 17:15:00 | MSG-03 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| f76bc9e2-b0ae-3be3-9bf3-7a13ed6c2d97 | -3.28176 | -42.25447 | 2026-10-05 17:15:00 | NPP-375 | MAGALHÃES DE ALMEIDA | MARANHÃO | Brasil | 2106300 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| e6042aff-e28f-3f90-8011-9cb6db19262e | -9.88792 | -64.17668 | 2026-10-05 17:15:00 | NPP-375 | BURITIS | RONDÔNIA | Brasil | 1100452 | 11 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 5fa894d7-6ce6-3117-a1f9-d8cf0555e944 | -8.77044 | -66.5722 | 2026-10-05 17:15:00 | NPP-375 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 17.6 |
| c7a03531-5ba9-36bc-b525-c8608eb3a838 | -3.42039 | -42.5636 | 2026-10-05 17:15:00 | NPP-375 | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 892dd26d-3b9b-332f-bf07-4d9434d038f5 | -9.03307 | -45.16005 | 2026-10-05 17:15:00 | NPP-375 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 844995a8-c0bd-3f75-a3ca-9079441ac674 | -6.79216 | -66.67441 | 2026-10-05 17:15:00 | NPP-375 | TAPAUÁ | AMAZONAS | Brasil | 1304104 | 13 | 33 | nan | nan | nan | Amazônia | 8.8 |
| a6f95112-3c9e-3d02-8814-f58e7d27c026 | -3.96912 | -59.3349 | 2026-10-05 17:15:00 | NPP-375 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 99ba4b33-566e-3e72-96d8-28e194e40ed2 | -8.59755 | -48.07449 | 2026-10-05 17:15:00 | NPP-375 | ITAPIRATINS | TOCANTINS | Brasil | 1710904 | 17 | 33 | nan | nan | nan | Cerrado | 7.7 |
| 36dcf192-8ee3-355a-8bea-28cfca9c8054 | -4.06004 | -54.04624 | 2026-10-05 17:15:00 | NPP-375 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 29.4 |
| fed41aea-b755-37ac-a925-b08d392b87f6 | -3.67253 | -55.94949 | 2026-10-05 17:15:00 | NPP-375 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 49.0 |
| 8f098182-5b21-319b-986a-4458495a840c | -4.90843 | -41.74143 | 2026-10-05 17:15:00 | NPP-375 | SIGEFREDO PACHECO | PIAUÍ | Brasil | 2210656 | 22 | 33 | nan | nan | nan | Caatinga | 12.3 |
| 33fe9fe0-0096-31ae-a89e-2b7deed006d3 | -3.22407 | -42.7767 | 2026-10-05 17:15:00 | NPP-375 | SANTANA DO MARANHÃO | MARANHÃO | Brasil | 2110237 | 21 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 1dc5bb42-e2c4-3115-911f-6514a3b9418b | -3.12555 | -53.70881 | 2026-10-05 17:15:00 | NPP-375 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 14.5 |
| dd85d5f8-2010-33d7-b81f-4f9e8e17601d | -7.22484 | -55.18241 | 2026-10-05 17:15:00 | NPP-375 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 32.5 |
| 9c467170-ec5b-35ed-be03-7f8a969b55e5 | -10.30154 | -63.39446 | 2026-10-05 17:15:00 | NPP-375 | MONTE NEGRO | RONDÔNIA | Brasil | 1101401 | 11 | 33 | nan | nan | nan | Amazônia | 9.7 |
| b01795d0-3787-34e4-87f1-db79ba78a86f | -7.22757 | -55.2008 | 2026-10-05 17:15:00 | NPP-375 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 12.2 |
| ce10096b-ee60-329e-9dff-627fe292bfbb | -3.68972 | -42.19364 | 2026-10-05 17:15:00 | NPP-375 | ESPERANTINA | PIAUÍ | Brasil | 2203701 | 22 | 33 | nan | nan | nan | Caatinga | 6.4 |
| b616c5f9-7e2e-3da5-8444-75fc340f3b0b | -6.40256 | -44.00912 | 2026-10-05 17:15:00 | NPP-375 | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 8.4 |
| 88e9b8ef-dcf2-34dc-8f5a-0a1af2d9800e | -3.01254 | -53.23088 | 2026-10-05 17:15:00 | NPP-375 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 7c0c680a-ee8b-3b69-86f5-112c91b24798 | -3.47963 | -55.43067 | 2026-10-05 17:15:00 | NPP-375 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| bcd97f2d-0888-3763-bd91-354af501b92a | -7.89916 | -44.20788 | 2026-10-05 17:15:00 | NPP-375 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 7.8 |
| b7de666d-d8eb-3ca1-91b8-85af03c3ad1f | -8.52494 | -54.59888 | 2026-10-05 17:15:00 | NPP-375 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 12.6 |
| 736e1d84-8639-3dc0-9d8b-2c8c01f6eadc | -6.89646 | -43.67422 | 2026-10-05 17:15:00 | NPP-375 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 555b7d75-7c90-3e30-bbc6-1f574537a19b | -6.03436 | -45.22786 | 2026-10-05 17:15:00 | NPP-375 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 30a095da-ce04-3523-999f-84be6673c55d | -2.44718 | -50.2534 | 2026-10-05 17:15:00 | NPP-375 | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 33b0cc42-4303-35fb-b873-a69b9a5ab407 | -5.2602 | -47.92247 | 2026-10-05 17:15:00 | NPP-375 | SAMPAIO | TOCANTINS | Brasil | 1718808 | 17 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 49cb7583-f844-3efa-a665-1f379adb68e4 | -7.2144 | -55.20264 | 2026-10-05 17:15:00 | NPP-375 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| d772e5b1-92da-31e1-96a9-1414f9485e0b | -4.86569 | -43.47096 | 2026-10-05 17:15:00 | NPP-375 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 4.9 |
| f96b0cc1-869a-354e-b28a-9573a9315c01 | -9.38165 | -47.06888 | 2026-10-05 17:15:00 | NPP-375 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| b4dbf940-7fe8-37f0-84c5-ca27a016f918 | -8.43896 | -54.97672 | 2026-10-05 17:15:00 | NPP-375 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 12ec9446-0328-3e84-90ad-fff5c5e58270 | -3.28537 | -54.17599 | 2026-10-05 17:15:00 | NPP-375 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 15.6 |
| 40772b80-5dcf-32c4-a6b3-df00d6cf2b7e | -3.64098 | -54.5088 | 2026-10-05 17:15:00 | NPP-375 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |


[Clique aqui para ver as próximas entradas](README108.md)
