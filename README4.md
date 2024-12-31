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

## Dados Diários - Página 4

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 18ae6aa7-fd06-35ef-b190-a0ab9e0cb7ed | -22.11972 | -51.46707 | 2024-12-31 03:49:00 | NPP-375D | PRESIDENTE PRUDENTE | SÃO PAULO | Brasil | 3541406 | 35 | 33 | nan | nan | nan | Mata Atlântica | 20.7 |
| 8c98a64f-3084-3c35-bacf-21aaa3c3c721 | -3.55228 | -43.56416 | 2024-12-31 04:04:00 | NOAA-20 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 2b86f537-7ac8-3f09-9a09-04a3d687caea | -2.03179 | -45.67376 | 2024-12-31 04:04:00 | NOAA-20 | GOVERNADOR NUNES FREIRE | MARANHÃO | Brasil | 2104677 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| d660088c-3e68-3b70-84cb-adee7be1591b | -3.76026 | -43.95873 | 2024-12-31 04:04:00 | NOAA-20 | VARGEM GRANDE | MARANHÃO | Brasil | 2112704 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| c94d2ee1-0e2e-3ca5-a79e-84bdb00692f4 | -2.80104 | -41.7772 | 2024-12-31 04:04:00 | NOAA-20 | ILHA GRANDE | PIAUÍ | Brasil | 2204659 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 4db18573-6303-3804-86e4-264124d87cdd | -1.65192 | -45.86649 | 2024-12-31 04:04:00 | NOAA-20 | AMAPÁ DO MARANHÃO | MARANHÃO | Brasil | 2100550 | 21 | 33 | nan | nan | nan | Amazônia | 7.4 |
| b204e2fb-c47c-37db-afdc-609b80d888a1 | -4.91319 | -41.11384 | 2024-12-31 04:04:00 | NOAA-20 | PORANGA | CEARÁ | Brasil | 2311009 | 23 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 7057afa3-a935-3c9d-b85d-f493ed401443 | -5.48264 | -43.34132 | 2024-12-31 04:04:00 | NOAA-20 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 40349be7-313b-344c-af2f-7807cb690065 | -6.38683 | -39.39373 | 2024-12-31 04:04:00 | NOAA-20 | IGUATU | CEARÁ | Brasil | 2305506 | 23 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 294420aa-d54f-3a6f-bdf4-2f134d88cd28 | -4.52373 | -44.23862 | 2024-12-31 04:04:00 | NOAA-20 | PERITORÓ | MARANHÃO | Brasil | 2108454 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| a71df86e-2b2f-3b4a-aeed-24c8a10ca5d7 | -1.64836 | -45.8621 | 2024-12-31 04:04:00 | NOAA-20 | AMAPÁ DO MARANHÃO | MARANHÃO | Brasil | 2100550 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 997285cd-af79-3ca6-a2e4-0055d0a69687 | -3.7581 | -41.03084 | 2024-12-31 04:04:00 | NOAA-20 | TIANGUÁ | CEARÁ | Brasil | 2313401 | 23 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 43a5910d-5a48-390c-84de-575507188df0 | -1.65666 | -45.8634 | 2024-12-31 04:04:00 | NOAA-20 | AMAPÁ DO MARANHÃO | MARANHÃO | Brasil | 2100550 | 21 | 33 | nan | nan | nan | Amazônia | 7.4 |
| b2feb44e-e712-302c-8598-d92dafa79101 | -1.85888 | -45.58337 | 2024-12-31 04:04:00 | NOAA-20 | TURIAÇU | MARANHÃO | Brasil | 2112407 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| b91de069-2de5-3fb3-92ad-89ce6a313980 | -5.93594 | -40.02446 | 2024-12-31 04:04:00 | NOAA-20 | TAUÁ | CEARÁ | Brasil | 2313302 | 23 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 58eeca28-44c6-3a65-9bbd-2fa6112c91e5 | -4.52669 | -44.24335 | 2024-12-31 04:04:00 | NOAA-20 | PERITORÓ | MARANHÃO | Brasil | 2108454 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 1f8652a8-9d08-3ece-aec9-196cdb42e1fe | -6.70559 | -34.96418 | 2024-12-31 04:04:00 | NOAA-20 | BAÍA DA TRAIÇÃO | PARAÍBA | Brasil | 2501401 | 25 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| 53ff57be-5454-309b-8273-78127c0784ce | -5.52906 | -37.76284 | 2024-12-31 04:04:00 | NOAA-20 | APODI | RIO GRANDE DO NORTE | Brasil | 2401008 | 24 | 33 | nan | nan | nan | Caatinga | 1.2 |
| bc04567a-ec8b-3bbb-858b-7c33c9d25934 | -5.19467 | -40.64077 | 2024-12-31 04:04:00 | NOAA-20 | CRATEÚS | CEARÁ | Brasil | 2304103 | 23 | 33 | nan | nan | nan | Caatinga | 0.7 |
| cee7185c-6c88-30c8-a906-db43c76f5d8d | -2.14579 | -45.17395 | 2024-12-31 04:04:00 | NOAA-20 | SANTA HELENA | MARANHÃO | Brasil | 2109809 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| da130563-9bf5-3a71-a558-d3dbd71b6a9c | -4.29963 | -38.69984 | 2024-12-31 04:04:00 | NOAA-20 | REDENÇÃO | CEARÁ | Brasil | 2311603 | 23 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 702dbefc-9229-32ef-8418-b4fde2e883cb | -2.03468 | -45.68164 | 2024-12-31 04:04:00 | NOAA-20 | GOVERNADOR NUNES FREIRE | MARANHÃO | Brasil | 2104677 | 21 | 33 | nan | nan | nan | Amazônia | 0.4 |
| bfc45c9a-38b2-3dae-9e9e-75dff6fb9f3d | -1.6448 | -45.85765 | 2024-12-31 04:04:00 | NOAA-20 | AMAPÁ DO MARANHÃO | MARANHÃO | Brasil | 2100550 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 802aea0f-3c4f-3259-a758-d96fbcb6cf3d | -5.58827 | -39.53386 | 2024-12-31 04:04:00 | NOAA-20 | SENADOR POMPEU | CEARÁ | Brasil | 2312700 | 23 | 33 | nan | nan | nan | Caatinga | 0.9 |
| f703c761-c39c-3b83-aa73-532d86c7af48 | -3.37534 | -41.26046 | 2024-12-31 04:04:00 | NOAA-20 | GRANJA | CEARÁ | Brasil | 2304707 | 23 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 4f92ab65-782c-3455-8071-9f3338a45287 | -2.84072 | -40.29799 | 2024-12-31 04:04:00 | NOAA-20 | ACARAÚ | CEARÁ | Brasil | 2300200 | 23 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 2b9cc8c7-6577-3347-a73d-404852796ef8 | -4.52603 | -44.24751 | 2024-12-31 04:04:00 | NOAA-20 | PERITORÓ | MARANHÃO | Brasil | 2108454 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| b9de6bfa-7dfe-382e-ab6a-000facbf30a9 | -1.57212 | -46.04493 | 2024-12-31 04:04:00 | NOAA-20 | CARUTAPERA | MARANHÃO | Brasil | 2102903 | 21 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 6ade1730-0281-3d43-b3c8-5b18eac05c36 | -3.76385 | -43.95931 | 2024-12-31 04:04:00 | NOAA-20 | VARGEM GRANDE | MARANHÃO | Brasil | 2112704 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| e2107fda-94ef-334c-b461-bcd9b9c5aa70 | -2.49232 | -45.44777 | 2024-12-31 04:04:00 | NOAA-20 | PRESIDENTE SARNEY | MARANHÃO | Brasil | 2109270 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 57a894ca-c626-3374-a7b4-3d6fd3131eae | -5.52538 | -37.76229 | 2024-12-31 04:04:00 | NOAA-20 | APODI | RIO GRANDE DO NORTE | Brasil | 2401008 | 24 | 33 | nan | nan | nan | Caatinga | 0.5 |
| 7048adfa-da20-332c-ad29-95fa09346b9b | -6.38749 | -39.39505 | 2024-12-31 04:04:00 | NOAA-20 | IGUATU | CEARÁ | Brasil | 2305506 | 23 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 306b3067-de73-3e0a-aef0-073b4b22b0e2 | -4.57379 | -41.30742 | 2024-12-31 04:04:00 | NOAA-20 | MILTON BRANDÃO | PIAUÍ | Brasil | 2206357 | 22 | 33 | nan | nan | nan | Caatinga | 0.6 |
| f9d257b2-4fec-31ac-8f7a-a1efbd3ebe48 | -4.91497 | -40.75711 | 2024-12-31 04:04:00 | NOAA-20 | IPAPORANGA | CEARÁ | Brasil | 2305654 | 23 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 5b55f4eb-4aa1-3396-a771-022de98460b8 | -2.81108 | -41.77877 | 2024-12-31 04:04:00 | NOAA-20 | ILHA GRANDE | PIAUÍ | Brasil | 2204659 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| bab47bba-4f64-3ea1-a6bb-b5438217e1f8 | -4.93829 | -41.85825 | 2024-12-31 04:04:00 | NOAA-20 | SIGEFREDO PACHECO | PIAUÍ | Brasil | 2210656 | 22 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 8ca2ac1a-9833-3637-b3fa-95714e563dc2 | -1.67618 | -45.84736 | 2024-12-31 04:04:00 | NOAA-20 | CÂNDIDO MENDES | MARANHÃO | Brasil | 2102606 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 24458770-0216-3abd-8332-d789c1b7bca5 | -4.54539 | -44.68773 | 2024-12-31 04:04:00 | NOAA-20 | TRIZIDELA DO VALE | MARANHÃO | Brasil | 2112233 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 80589318-9198-3ed5-9992-a0eb80c3a0b8 | -5.02102 | -39.71224 | 2024-12-31 04:04:00 | NOAA-20 | BOA VIAGEM | CEARÁ | Brasil | 2302404 | 23 | 33 | nan | nan | nan | Caatinga | 1.1 |
| fa2eee79-6b0b-3ac4-b2c1-c777d73794eb | -4.90766 | -41.10591 | 2024-12-31 04:04:00 | NOAA-20 | PORANGA | CEARÁ | Brasil | 2311009 | 23 | 33 | nan | nan | nan | Caatinga | 1.7 |
| b8fbcd1c-3c78-3a6a-9fa3-baaeea7a3ea4 | -2.86269 | -40.56987 | 2024-12-31 04:04:00 | NOAA-20 | JIJOCA DE JERICOACOARA | CEARÁ | Brasil | 2307254 | 23 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 9d9c6559-4e6a-3da2-8de8-42c217c1e21d | -3.76451 | -43.95518 | 2024-12-31 04:04:00 | NOAA-20 | VARGEM GRANDE | MARANHÃO | Brasil | 2112704 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 749e0355-7f2d-3a0f-8665-2f3b9bfb7a32 | -4.91374 | -41.11039 | 2024-12-31 04:04:00 | NOAA-20 | PORANGA | CEARÁ | Brasil | 2311009 | 23 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 2b803e69-d3b7-356d-8976-e06eded0611b | -4.91596 | -41.11781 | 2024-12-31 04:04:00 | NOAA-20 | PORANGA | CEARÁ | Brasil | 2311009 | 23 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 1053214b-0935-3db9-90a9-5cfcaad78f26 | -3.96237 | -40.87633 | 2024-12-31 04:04:00 | NOAA-20 | IBIAPINA | CEARÁ | Brasil | 2305308 | 23 | 33 | nan | nan | nan | Caatinga | 4.5 |
| 121a7dcd-a0e6-3347-942e-1a854f2fbff1 | -2.71497 | -45.57598 | 2024-12-31 04:04:00 | NOAA-20 | SANTA HELENA | MARANHÃO | Brasil | 2109809 | 21 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 71a93e82-b83d-3e51-8557-7f4f6b6805cf | -2.86323 | -40.56643 | 2024-12-31 04:04:00 | NOAA-20 | JIJOCA DE JERICOACOARA | CEARÁ | Brasil | 2307254 | 23 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 77bd1bb2-0f4c-3f99-9223-183ed42ece07 | -2.42101 | -45.58604 | 2024-12-31 04:04:00 | NOAA-20 | SANTA HELENA | MARANHÃO | Brasil | 2109809 | 21 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 2f38ea38-6a06-35be-80ea-27787945aff5 | -5.4432 | -43.49772 | 2024-12-31 04:04:00 | NOAA-20 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| ed582191-998d-3302-8313-eb003a4428f2 | -1.64777 | -45.86584 | 2024-12-31 04:04:00 | NOAA-20 | AMAPÁ DO MARANHÃO | MARANHÃO | Brasil | 2100550 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c5827e75-67b0-3392-afc6-7478dd5bbdac | -3.52692 | -40.92376 | 2024-12-31 04:04:00 | NOAA-20 | VIÇOSA DO CEARÁ | CEARÁ | Brasil | 2314102 | 23 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 3498c0a5-7e7f-3424-9772-f29458acd34f | -4.52735 | -44.23921 | 2024-12-31 04:04:00 | NOAA-20 | PERITORÓ | MARANHÃO | Brasil | 2108454 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| c161b6b2-8a9c-3505-bda8-58dab0578df9 | -2.71554 | -45.5725 | 2024-12-31 04:04:00 | NOAA-20 | SANTA HELENA | MARANHÃO | Brasil | 2109809 | 21 | 33 | nan | nan | nan | Amazônia | 2.7 |
| badae300-1a78-3ad6-bd79-2297538d791d | -4.53523 | -44.23629 | 2024-12-31 04:04:00 | NOAA-20 | PERITORÓ | MARANHÃO | Brasil | 2108454 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 28cb268b-b545-3da6-8372-b9a803a8bdd0 | -5.85396 | -39.08358 | 2024-12-31 04:04:00 | NOAA-20 | SOLONÓPOLE | CEARÁ | Brasil | 2313005 | 23 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 868d1b84-e38f-391d-8578-56266de27aa8 | -1.25179 | -46.60717 | 2024-12-31 04:04:00 | NOAA-20 | AUGUSTO CORRÊA | PARÁ | Brasil | 1500909 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| cf38c8c2-5167-30b6-b9d4-c3c05f357b41 | -4.12954 | -46.85684 | 2024-12-31 04:04:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| f9a44b42-9f2e-3c8a-9f3a-1c771a33a915 | -1.67819 | -45.84697 | 2024-12-31 04:04:00 | NOAA-20 | CÂNDIDO MENDES | MARANHÃO | Brasil | 2102606 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 06233885-7483-3c4b-b2b4-b716100354e5 | -4.53225 | -44.23788 | 2024-12-31 04:04:00 | NOAA-20 | PERITORÓ | MARANHÃO | Brasil | 2108454 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 814c2644-8509-31a3-bead-303546da6053 | -5.48325 | -43.33757 | 2024-12-31 04:04:00 | NOAA-20 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| e2816947-842a-32c8-a643-a0932b3416db | -2.8016 | -41.77368 | 2024-12-31 04:04:00 | NOAA-20 | ILHA GRANDE | PIAUÍ | Brasil | 2204659 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 442631c1-fa4c-3b95-a141-c58d94b64a57 | -1.65251 | -45.86274 | 2024-12-31 04:04:00 | NOAA-20 | AMAPÁ DO MARANHÃO | MARANHÃO | Brasil | 2100550 | 21 | 33 | nan | nan | nan | Amazônia | 7.4 |
| f1b95a1a-4d04-3788-b352-98c4bbfbd1d9 | -5.72721 | -43.23806 | 2024-12-31 04:04:00 | NOAA-20 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 7.9 |
| c35d50dc-d426-33ff-a720-f0888fc885d0 | -6.12912 | -39.79906 | 2024-12-31 04:04:00 | NOAA-20 | ACOPIARA | CEARÁ | Brasil | 2300309 | 23 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 58c19118-d461-3a17-a667-6f00c48ff519 | -3.42516 | -40.53444 | 2024-12-31 04:04:00 | NOAA-20 | SENADOR SÁ | CEARÁ | Brasil | 2312809 | 23 | 33 | nan | nan | nan | Caatinga | 0.9 |
| c3704eb5-a13c-3d77-b301-108d6ccc32ca | -2.83741 | -40.29748 | 2024-12-31 04:04:00 | NOAA-20 | ACARAÚ | CEARÁ | Brasil | 2300200 | 23 | 33 | nan | nan | nan | Caatinga | 1.3 |
| dbbb2b48-e542-3e41-9540-6509e01ccb29 | -3.78502 | -41.61282 | 2024-12-31 04:04:00 | NOAA-20 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 0c1b2eaf-949e-3315-b6af-581473d02403 | -6.13251 | -39.79959 | 2024-12-31 04:04:00 | NOAA-20 | ACOPIARA | CEARÁ | Brasil | 2300309 | 23 | 33 | nan | nan | nan | Caatinga | 1.7 |
| a837d021-045d-318b-9e52-741eed5bad38 | -5.50442 | -39.12505 | 2024-12-31 04:04:00 | NOAA-20 | QUIXERAMOBIM | CEARÁ | Brasil | 2311405 | 23 | 33 | nan | nan | nan | Caatinga | 1.0 |
| e14cce80-ac80-39d7-871a-644cf31f985e | -1.64421 | -45.86142 | 2024-12-31 04:04:00 | NOAA-20 | AMAPÁ DO MARANHÃO | MARANHÃO | Brasil | 2100550 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| f57f3246-bc66-3599-894a-d707d583aa63 | -5.31583 | -44.55362 | 2024-12-31 04:04:00 | NOAA-20 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 228e9be5-4526-346e-9fd5-9bc4808d8832 | -4.8752 | -39.05134 | 2024-12-31 04:04:00 | NOAA-20 | QUIXADÁ | CEARÁ | Brasil | 2311306 | 23 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 206be385-166f-33a4-9b7e-373a5da65be7 | -3.78169 | -41.6123 | 2024-12-31 04:04:00 | NOAA-20 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 6e418a34-052a-3258-a885-0aa9bd65cc9d | -5.17608 | -45.08347 | 2024-12-31 04:04:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| a165232d-d7c2-3c66-8a6a-6ae5940388e6 | -2.0612 | -45.38181 | 2024-12-31 04:04:00 | NOAA-20 | TURILÂNDIA | MARANHÃO | Brasil | 2112456 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 63cbdaeb-abe7-31eb-8dc1-07d905693696 | -4.62257 | -38.48457 | 2024-12-31 04:04:00 | NOAA-20 | OCARA | CEARÁ | Brasil | 2309458 | 23 | 33 | nan | nan | nan | Caatinga | 1.4 |
| a171e002-f220-35ba-9d56-88fc6fba07bf | -2.49178 | -45.45122 | 2024-12-31 04:04:00 | NOAA-20 | PRESIDENTE SARNEY | MARANHÃO | Brasil | 2109270 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| ff41e884-2f88-3fe1-b556-6e76764f90ef | -6.28196 | -43.81992 | 2024-12-31 04:06:00 | NOAA-20 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| c0be58aa-66db-3764-adc6-9671c8f32dc7 | -7.90771 | -35.2089 | 2024-12-31 04:06:00 | NOAA-20 | PAUDALHO | PERNAMBUCO | Brasil | 2610608 | 26 | 33 | nan | nan | nan | Mata Atlântica | 3.8 |
| 1a983284-4b5a-33b0-a973-674519772ccd | -7.06082 | -40.56184 | 2024-12-31 04:06:00 | NOAA-20 | FRONTEIRAS | PIAUÍ | Brasil | 2204303 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 0bae4888-02bd-3477-b0f8-83d0e3ba19a4 | -9.88124 | -37.23944 | 2024-12-31 04:06:00 | NOAA-20 | BELO MONTE | ALAGOAS | Brasil | 2700904 | 27 | 33 | nan | nan | nan | Caatinga | 1.4 |
| cc7cc900-83f7-34b6-9867-b14e2304f9b5 | -6.94959 | -43.00728 | 2024-12-31 04:06:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 4.2 |
| 36afd27a-4498-3504-9b18-e5f295dcf8c3 | -6.5963 | -39.42574 | 2024-12-31 04:06:00 | NOAA-20 | CARIÚS | CEARÁ | Brasil | 2303303 | 23 | 33 | nan | nan | nan | Caatinga | 3.0 |
| 0f03fd87-7c7c-360b-9282-301cbff38fc7 | -10.63599 | -40.21349 | 2024-12-31 04:06:00 | NOAA-20 | FILADÉLFIA | BAHIA | Brasil | 2910859 | 29 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 10f8cc6c-fd8a-353b-9200-67ed539fdd70 | -12.05931 | -40.01506 | 2024-12-31 04:06:00 | NOAA-20 | IPIRÁ | BAHIA | Brasil | 2914000 | 29 | 33 | nan | nan | nan | Caatinga | 0.6 |
| a73fbaf8-4d1f-3b71-89da-6faab295bd42 | -6.95354 | -43.00422 | 2024-12-31 04:06:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 4.2 |
| ed2bd021-b0c2-32a0-8598-0a6417f8bd44 | -12.8407 | -38.33727 | 2024-12-31 04:06:00 | NOAA-20 | LAURO DE FREITAS | BAHIA | Brasil | 2919207 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 37f949e3-926f-32e1-b3d2-3ce0b1a5067a | -6.27849 | -43.81934 | 2024-12-31 04:06:00 | NOAA-20 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 971f1ff9-eeb8-3b43-914d-e890b96606ad | -7.90843 | -35.2363 | 2024-12-31 04:06:00 | NOAA-20 | PAUDALHO | PERNAMBUCO | Brasil | 2610608 | 26 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| fccdb4ff-1ff5-387e-a74c-c21a8acc32b5 | -7.91665 | -35.21038 | 2024-12-31 04:06:00 | NOAA-20 | PAUDALHO | PERNAMBUCO | Brasil | 2610608 | 26 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| 8e6e4deb-4f84-3764-9e8b-b78751158fc3 | -10.69614 | -37.0494 | 2024-12-31 04:06:00 | NOAA-20 | ROSÁRIO DO CATETE | SERGIPE | Brasil | 2806107 | 28 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 59eba57c-f4f4-3317-bce4-7dee7e65a799 | -6.95691 | -43.00475 | 2024-12-31 04:06:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 5dfaef60-42cd-306d-84a6-d302c1c37a9c | -7.88991 | -45.95952 | 2024-12-31 04:06:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 664d2b3c-f2e3-3b91-93fc-4ff8447eb96d | -6.95633 | -43.00835 | 2024-12-31 04:06:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 4f0e8cf6-94ee-38e9-a248-17adc4c878fe | -6.96981 | -43.0105 | 2024-12-31 04:06:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 933b2030-65f5-3958-949a-275a9bf1c94f | -6.27501 | -43.81878 | 2024-12-31 04:06:00 | NOAA-20 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| d8458494-abcd-3a62-b2ab-1743a7635e5c | -11.47907 | -41.69604 | 2024-12-31 04:06:00 | NOAA-20 | LAPÃO | BAHIA | Brasil | 2919157 | 29 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 076015fe-d236-3ddc-9b4a-b2ef9bfe9d2d | -7.72734 | -40.17525 | 2024-12-31 04:06:00 | NOAA-20 | OURICURI | PERNAMBUCO | Brasil | 2609907 | 26 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 8a3a918f-afd3-33b4-8784-b90f06000d0d | -6.88139 | -40.62064 | 2024-12-31 04:06:00 | NOAA-20 | PIO IX | PIAUÍ | Brasil | 2208205 | 22 | 33 | nan | nan | nan | Caatinga | 4.0 |
| 7d68f828-06bb-38b7-8b3c-52da33c81314 | -6.75749 | -39.14037 | 2024-12-31 04:06:00 | NOAA-20 | LAVRAS DA MANGABEIRA | CEARÁ | Brasil | 2307502 | 23 | 33 | nan | nan | nan | Caatinga | 1.7 |


[Clique aqui para ver as próximas entradas](README5.md)
