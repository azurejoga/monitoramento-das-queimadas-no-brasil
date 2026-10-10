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

## Dados Diários - Página 75

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 3a58f5c9-6ffb-300e-9ae5-9f2cb653a018 | -12.02751 | -43.4698 | 2026-10-10 04:46:00 | NPP-375D | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 59fd8a2f-dba3-351a-9ee5-273274e66c60 | -5.95833 | -55.33643 | 2026-10-10 04:46:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 4d53d266-0a10-36c9-8937-57ca47da3d5c | -11.36516 | -54.0323 | 2026-10-10 04:46:00 | NPP-375D | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 5f41068a-6972-37bf-adf6-8b298361f7b8 | -14.46021 | -43.96431 | 2026-10-10 04:46:00 | NPP-375D | JUVENÍLIA | MINAS GERAIS | Brasil | 3136959 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| f921691c-2623-3a85-814b-23e524808d2b | -13.38354 | -43.71464 | 2026-10-10 04:46:00 | NPP-375D | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 161fef4b-f916-31b2-b501-b30df8f877a1 | -13.4832 | -48.58921 | 2026-10-10 04:46:00 | NPP-375D | TROMBAS | GOIÁS | Brasil | 5221452 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| bcf8f2bf-b81b-356b-bed5-92c182b61d41 | -5.88899 | -57.72521 | 2026-10-10 04:46:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 24bec779-d8a1-39c7-9ef2-f8f11cb12f4c | -8.86846 | -50.19091 | 2026-10-10 04:46:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| a7f185f4-fab3-31de-a888-d1ed73b8f6fe | -14.45495 | -43.93956 | 2026-10-10 04:46:00 | NPP-375D | JUVENÍLIA | MINAS GERAIS | Brasil | 3136959 | 31 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 0f0c1416-6e88-3934-8457-3888786d4528 | -11.69291 | -43.65517 | 2026-10-10 04:46:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 3.0 |
| f07482ee-7f96-3637-ad93-08e64dbc2205 | -10.25112 | -49.66221 | 2026-10-10 04:46:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| f45da67a-c683-3c2e-bd19-80b58d8c2a6b | -11.09898 | -47.63688 | 2026-10-10 04:46:00 | NPP-375D | PINDORAMA DO TOCANTINS | TOCANTINS | Brasil | 1717008 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 99a1c8af-d471-3a4e-bd7b-3fcea83e4ebe | -11.84034 | -43.61047 | 2026-10-10 04:46:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| e0e3b08f-cf2a-34a4-aee6-39c98480ee12 | -7.08999 | -52.68606 | 2026-10-10 04:46:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| ac64349b-f640-3c13-89aa-7235e02193d2 | -6.70709 | -49.13034 | 2026-10-10 04:46:00 | NPP-375D | PIÇARRA | PARÁ | Brasil | 1505635 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| ecbdbb8f-4d14-3573-aeb1-6833583748f0 | -7.23134 | -55.14123 | 2026-10-10 04:46:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 28419b7e-68f5-341c-8d54-56de9894ac15 | -11.19913 | -44.87797 | 2026-10-10 04:46:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 2.9 |
| a5a07a38-139d-349b-ba1c-10895f634af8 | -10.89749 | -44.83556 | 2026-10-10 04:46:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 10.2 |
| be79b070-a2d2-3b61-a473-973b29884001 | -6.36604 | -55.16043 | 2026-10-10 04:46:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| bba7c04b-fc62-3da7-917f-63220f34d1f3 | -9.28631 | -47.39831 | 2026-10-10 04:46:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| d7b3aead-eafe-3898-988f-db264e319075 | -12.01048 | -43.43293 | 2026-10-10 04:46:00 | NPP-375D | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| a6aeb14d-402b-3253-99b7-01b9652fa2f4 | -11.99053 | -43.45326 | 2026-10-10 04:46:00 | NPP-375D | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 8b8d24c8-278c-363b-a35b-e63fa75b4a91 | -6.48448 | -55.96169 | 2026-10-10 04:46:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 8101643b-3977-39b0-9fc0-ec9c9f670371 | -14.02784 | -48.76127 | 2026-10-10 04:46:00 | NPP-375D | URUAÇU | GOIÁS | Brasil | 5221601 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 344bf98a-87a7-3132-b850-beffac820645 | -6.12072 | -55.69849 | 2026-10-10 04:46:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| e04b510a-e0b4-3c06-98f5-7e345a27d742 | -10.49574 | -51.93982 | 2026-10-10 04:46:00 | NPP-375D | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 24b5dee1-1695-38a1-bad5-a3267b596753 | -14.57685 | -43.83036 | 2026-10-10 04:46:00 | NPP-375D | MALHADA | BAHIA | Brasil | 2920205 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 3d6074c0-b40b-36cd-863e-116a086b6294 | -11.68128 | -43.48508 | 2026-10-10 04:46:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| d769eca0-5450-3531-925e-562c92b29495 | -13.35809 | -43.92648 | 2026-10-10 04:46:00 | NPP-375D | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | 4.5 |
| ca26bf7f-eb1d-36b1-94c8-55dd7166350f | -8.25442 | -46.42941 | 2026-10-10 04:46:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 77007ee1-bdeb-3e86-9ced-abf6aa14582b | -11.83055 | -43.58981 | 2026-10-10 04:46:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| f287e3dd-a4ce-36c7-8a3f-2fbab0f459d1 | -12.02701 | -43.47354 | 2026-10-10 04:46:00 | NPP-375D | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| b88de9d2-191f-3c63-a69e-6f1b102f5d8f | -7.02668 | -47.65508 | 2026-10-10 04:46:00 | NPP-375D | BABAÇULÂNDIA | TOCANTINS | Brasil | 1703008 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 048e2609-0ce3-390e-9aeb-edad6ac8d732 | -7.93838 | -49.74475 | 2026-10-10 04:46:00 | NPP-375D | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 174f835d-c9f1-3662-b21d-1e8e11b5bc14 | -7.23611 | -56.41845 | 2026-10-10 04:46:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 9722a27d-5d67-344d-b5cd-52b4b8108b25 | -12.41006 | -54.365 | 2026-10-10 04:46:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b951327d-7761-3d1d-9e3e-f8448ac6091b | -11.69599 | -47.28915 | 2026-10-10 04:46:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| f965011d-7822-361c-b807-372f630f3e4c | -6.70506 | -58.72021 | 2026-10-10 04:46:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 59fcc036-dbda-3a6e-90d2-7b00b589ad61 | -14.24366 | -47.30627 | 2026-10-10 04:46:00 | NPP-375D | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 75182bff-ecd8-329e-978a-5936a3aa4bce | -6.9957 | -47.72152 | 2026-10-10 04:46:00 | NPP-375D | BABAÇULÂNDIA | TOCANTINS | Brasil | 1703008 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 122c99af-10b6-3297-a7f9-5e87e998427f | -9.62924 | -48.88084 | 2026-10-10 04:46:00 | NPP-375D | DOIS IRMÃOS DO TOCANTINS | TOCANTINS | Brasil | 1707207 | 17 | 33 | nan | nan | nan | Cerrado | 9.6 |
| f5cb48b9-e047-3a68-8616-7d35cc7d5732 | -6.49073 | -55.31641 | 2026-10-10 04:46:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 85573ef0-ab76-3816-a0bc-7f80059b0587 | -11.88049 | -47.35928 | 2026-10-10 04:46:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 7923d27c-cc3c-3a6a-ae36-3766bee3888f | -5.19308 | -60.30825 | 2026-10-10 04:46:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 468d7397-aa59-3702-a38f-fab1cd406239 | -8.89985 | -51.70597 | 2026-10-10 04:46:00 | NPP-375D | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 91d82036-fe63-3a42-b2d5-f949dc81c6d0 | -5.99348 | -55.36391 | 2026-10-10 04:46:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 0d105a4e-fe2c-3c15-a6ed-619f9a2b89d6 | -6.36487 | -55.1681 | 2026-10-10 04:46:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e52c7b2f-8d84-3d14-a657-74f57bee4816 | -7.24294 | -55.21451 | 2026-10-10 04:46:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 6ee5a038-d5df-394c-b3c2-e7f18f3a8f3a | -6.52539 | -55.25885 | 2026-10-10 04:46:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| d7d37c00-62f2-3d1a-97ba-e2407f0a56d1 | -10.56824 | -47.81877 | 2026-10-10 04:46:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 9791e6bb-e273-3efb-83ac-1ef58e876b0b | -11.87992 | -47.36299 | 2026-10-10 04:46:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 3c6485a8-862c-3ce8-bcf8-b6350d08783d | -10.45645 | -47.84075 | 2026-10-10 04:46:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 22702e82-efe8-3d50-8715-5797b799321c | -6.3761 | -55.15959 | 2026-10-10 04:46:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 3093fdd9-f392-3dca-9bb8-f5661dff70a9 | -10.73834 | -52.0297 | 2026-10-10 04:46:00 | NPP-375D | PORTO ALEGRE DO NORTE | MATO GROSSO | Brasil | 5106778 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 0862fa33-695c-36c2-af7a-59b0e3dfdf09 | -8.63196 | -50.22569 | 2026-10-10 04:46:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 76390229-4569-3fdf-aa13-179dbe995422 | -13.38549 | -43.89029 | 2026-10-10 04:46:00 | NPP-375D | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| e7e0143d-c2e0-3ceb-b286-584e00642426 | -6.4376 | -55.19897 | 2026-10-10 04:46:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 1936e2bf-2d67-3c91-b467-884b6adfcbb6 | -12.2401 | -54.3868 | 2026-10-10 04:46:00 | NPP-375D | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| f93708e6-6555-301e-a61e-e4040997ab40 | -6.43178 | -55.2612 | 2026-10-10 04:46:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 83051edc-9929-312e-b442-96c2088c4380 | -8.18704 | -54.71866 | 2026-10-10 04:46:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 7b2d0fd7-6574-31df-8cd2-e18cc468f4ad | -7.00679 | -47.71614 | 2026-10-10 04:46:00 | NPP-375D | BABAÇULÂNDIA | TOCANTINS | Brasil | 1703008 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 83f8d73f-7ce7-3960-92c4-43280ff80f95 | -6.13394 | -53.10571 | 2026-10-10 04:46:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d78f0f5d-56cc-34ab-b7d4-4cbc21d14e30 | -7.91128 | -54.73514 | 2026-10-10 04:46:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| ddcab7d1-4775-3f55-b57b-dbc5936a39ac | -9.83599 | -44.78259 | 2026-10-10 04:46:00 | NPP-375D | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| bf443089-1e91-365e-bc50-f11546cfcb93 | -8.65218 | -54.53782 | 2026-10-10 04:46:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| c8584033-5752-3e70-9a1c-9bddf19893de | -7.31957 | -46.72303 | 2026-10-10 04:46:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 10b2ed7d-1040-38a8-9228-0c6b37914784 | -11.87708 | -47.35874 | 2026-10-10 04:46:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 1f5b45e8-8a1e-3dab-9c17-12ea6ea10284 | -6.44733 | -55.28525 | 2026-10-10 04:46:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| c725c3f5-6cef-3e61-97aa-16837ca3e976 | -11.96272 | -43.46917 | 2026-10-10 04:46:00 | NPP-375D | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 6cc292fa-cfa6-3fb4-a2be-ba34e5c46240 | -11.46473 | -43.37703 | 2026-10-10 04:46:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| caaa8d8c-f148-3823-8f33-d413e4da2169 | -12.24417 | -54.3876 | 2026-10-10 04:46:00 | NPP-375D | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 5e6a578b-3ef9-3710-a366-826b8245ca08 | -14.01723 | -48.76326 | 2026-10-10 04:46:00 | NPP-375D | URUAÇU | GOIÁS | Brasil | 5221601 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 893dcb1c-ab3a-3826-b89a-e68919408286 | -14.02952 | -48.77253 | 2026-10-10 04:46:00 | NPP-375D | URUAÇU | GOIÁS | Brasil | 5221601 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| a28e20d8-e688-3520-bc34-b78784246a6e | -12.91077 | -45.11194 | 2026-10-10 04:46:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 177c3d47-5843-3acc-b3b3-2dcea62869e0 | -14.45863 | -43.94407 | 2026-10-10 04:46:00 | NPP-375D | JUVENÍLIA | MINAS GERAIS | Brasil | 3136959 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| f025bb6a-63a8-3bc5-b61f-c0a44a8ba708 | -8.79757 | -47.5798 | 2026-10-10 04:46:00 | NPP-375D | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| fd03e9b0-6dde-38e8-9ce4-bbb2499fa796 | -11.09346 | -43.98964 | 2026-10-10 04:46:00 | NPP-375D | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| e22c323b-773c-37f5-929b-060f3c8c96e0 | -7.10096 | -46.71525 | 2026-10-10 04:46:00 | NPP-375D | FEIRA NOVA DO MARANHÃO | MARANHÃO | Brasil | 2104073 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 2c944309-13a5-341c-bf2b-7fc1f86aa603 | -6.21997 | -52.64412 | 2026-10-10 04:46:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 60378310-f36f-34a9-93c1-b76841774c00 | -13.36944 | -43.91532 | 2026-10-10 04:46:00 | NPP-375D | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | 3.1 |
| e2ed9363-5f2a-3522-b34d-5edaf3fa0002 | -7.91208 | -54.73057 | 2026-10-10 04:46:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 79616adc-555b-3b96-8cff-1c4106d63841 | -12.37745 | -46.60453 | 2026-10-10 04:46:00 | NPP-375D | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 1fda78e3-753e-3f3c-9e8f-582d32c2697f | -11.91149 | -46.56966 | 2026-10-10 04:46:00 | NPP-375D | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| ef4ccd79-1fa2-3ac1-82e3-d49e13afe00e | -6.93129 | -59.24641 | 2026-10-10 04:46:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| ae0e225d-8d09-3dbb-9305-b6cec3b9a74a | -6.64922 | -55.33509 | 2026-10-10 04:46:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 8f4b2e5a-311a-3a95-8224-35daec524c31 | -11.87252 | -47.36564 | 2026-10-10 04:46:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 0f531ea8-94ea-3f27-8276-ca34465d8c32 | -8.59006 | -44.00041 | 2026-10-10 04:46:00 | NPP-375D | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 38f76b0e-19f3-3a51-933a-0b802a5f1884 | -10.6616 | -49.25819 | 2026-10-10 04:46:00 | NPP-375D | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| ebb6a878-39a5-3e7b-9f16-cd924510cf4f | -8.65281 | -54.5315 | 2026-10-10 04:46:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| e7b6ec53-0f56-370a-b78e-033cac93f5b1 | -11.60161 | -43.75214 | 2026-10-10 04:46:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 660dc5f7-e29c-3a34-b7f9-02ffa6520757 | -7.20781 | -55.08273 | 2026-10-10 04:46:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| f0de35a4-eb3b-31ba-b61e-fb00829c8fbd | -11.0834 | -44.10177 | 2026-10-10 04:46:00 | NPP-375D | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 9e9fcacb-f3dd-3d93-afdf-2f14912bfb9a | -11.66011 | -43.69289 | 2026-10-10 04:46:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 3f33d7f4-b9ba-330d-a470-dc0dee406af1 | -6.48981 | -55.32162 | 2026-10-10 04:46:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 364e8d5b-b461-38cf-add4-06874ff35247 | -9.83667 | -44.778 | 2026-10-10 04:46:00 | NPP-375D | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 02b15e6b-fc1c-3e94-9408-154ecfb9cec1 | -8.27723 | -46.41773 | 2026-10-10 04:46:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 60f45607-508b-3e41-9253-5b7fd85719bc | -12.3839 | -46.6096 | 2026-10-10 04:46:00 | NPP-375D | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 1aab5a1d-6123-390d-925b-0112645c21cf | -6.44173 | -53.65665 | 2026-10-10 04:46:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 245a393b-e6cf-3cc1-98eb-b6634ebed432 | -13.25952 | -44.00039 | 2026-10-10 04:46:00 | NPP-375D | SANTA MARIA DA VITÓRIA | BAHIA | Brasil | 2928109 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 26c9297f-0c8b-3bab-850f-2a6a182b9f0f | -8.98535 | -47.54373 | 2026-10-10 04:46:00 | NPP-375D | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |


[Clique aqui para ver as próximas entradas](README76.md)
