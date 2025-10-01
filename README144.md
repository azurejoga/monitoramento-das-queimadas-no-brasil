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

## Dados Diários - Página 144

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 792be65a-db91-3ff6-a2b8-ec820bb09056 | -12.49499 | -50.28844 | 2025-10-01 12:00:00 | TERRA_M-T | SÃO MIGUEL DO ARAGUAIA | GOIÁS | Brasil | 5220207 | 52 | 33 | nan | nan | nan | Cerrado | 57.9 |
| ccf6a676-7d05-3ae8-96d7-c4d0925bb55e | -10.78655 | -45.36197 | 2025-10-01 12:00:00 | TERRA_M-T | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 24.9 |
| 76c0499b-2dcb-3e92-a6ae-8ed5965fcf4a | -13.46943 | -47.23763 | 2025-10-01 12:00:00 | TERRA_M-T | TERESINA DE GOIÁS | GOIÁS | Brasil | 5221080 | 52 | 33 | nan | nan | nan | Cerrado | 11.8 |
| 4ddc6fe9-c192-3cd1-bb47-a061aab1249a | -14.34618 | -45.93723 | 2025-10-01 12:00:00 | TERRA_M-T | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 33.5 |
| ee8a27c2-ab6c-32d3-9445-4844fd5086de | -8.21304 | -47.01476 | 2025-10-01 12:00:00 | TERRA_M-T | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 46.4 |
| 9713957b-fed3-373e-a89f-954768cecd31 | -13.62896 | -47.63588 | 2025-10-01 12:00:00 | TERRA_M-T | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 30.8 |
| 7cb61eb2-db1f-3886-84fc-abe46bd18319 | -13.88191 | -40.72783 | 2025-10-01 12:00:00 | TERRA_M-T | MANOEL VITORINO | BAHIA | Brasil | 2920403 | 29 | 33 | nan | nan | nan | Caatinga | 10.8 |
| cebfff5e-a9a5-3c78-937b-7926f6514a3f | -9.03535 | -46.68469 | 2025-10-01 12:00:00 | TERRA_M-T | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 25.4 |
| 6c87c303-153b-37be-8ff7-5e9ea4288e87 | -10.89413 | -46.59322 | 2025-10-01 12:00:00 | TERRA_M-T | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 15.7 |
| 4ecc211b-93f1-3501-899e-a6e8c71b5f82 | -12.88457 | -40.16955 | 2025-10-01 12:00:00 | TERRA_M-T | IAÇU | BAHIA | Brasil | 2911907 | 29 | 33 | nan | nan | nan | Caatinga | 11.9 |
| 6fd54a1c-aaba-3dc6-bf9e-43ac3fb86e24 | -12.39848 | -45.0174 | 2025-10-01 12:00:00 | TERRA_M-T | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 11.5 |
| 00ece1c4-b19d-3592-b1f6-5667328a8177 | -14.51622 | -39.76165 | 2025-10-01 12:00:00 | TERRA_M-T | IBICUÍ | BAHIA | Brasil | 2912301 | 29 | 33 | nan | nan | nan | Mata Atlântica | 11.2 |
| f954ff50-81af-3a3a-88e6-2259abaea760 | -12.70145 | -45.28281 | 2025-10-01 12:00:00 | TERRA_M-T | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 10.2 |
| 01b7fbf3-b35c-382f-a616-5fb7d3b37035 | -13.46755 | -47.24952 | 2025-10-01 12:00:00 | TERRA_M-T | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 12.3 |
| 6b124c15-75eb-308b-9c01-9413a9a8ec16 | -11.85716 | -44.99694 | 2025-10-01 12:00:00 | TERRA_M-T | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 48.4 |
| cb791033-81ab-33fd-92fa-96a102628a49 | -13.42958 | -45.89926 | 2025-10-01 12:00:00 | TERRA_M-T | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 15.9 |
| 0926c01e-277f-3c1b-972b-cc24ca652530 | -8.16022 | -44.11491 | 2025-10-01 12:00:00 | TERRA_M-T | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 17.2 |
| b98bb2ab-f8fd-38ba-874a-cc37e8924bad | -11.84173 | -44.97453 | 2025-10-01 12:00:00 | TERRA_M-T | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 19.6 |
| 9c7e1aff-5c8b-3f24-9892-ae2664a7c3b6 | -11.94672 | -47.08 | 2025-10-01 12:00:00 | TERRA_M-T | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 18.2 |
| 963852fe-1d70-3c72-bc38-9290d8c681ec | -12.6922 | -45.28139 | 2025-10-01 12:00:00 | TERRA_M-T | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 69.6 |
| 56bff40b-a723-3d28-937e-e7f140e0e890 | -12.21256 | -47.80901 | 2025-10-01 12:00:00 | TERRA_M-T | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 21.3 |
| f1ea73b8-3049-3b68-bc8a-5fb0d2bbe206 | -9.92922 | -43.69099 | 2025-10-01 12:00:00 | TERRA_M-T | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Cerrado | 44.2 |
| e579b33e-017c-386b-96f2-36d1ddeb8742 | -11.8557 | -45.00663 | 2025-10-01 12:00:00 | TERRA_M-T | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 14.3 |
| 398bb3fc-5ae5-3f96-a0db-70f6ce4b3d85 | -13.0133 | -39.7344 | 2025-10-01 12:00:00 | TERRA_M-T | AMARGOSA | BAHIA | Brasil | 2901007 | 29 | 33 | nan | nan | nan | Mata Atlântica | 13.0 |
| 44a4f415-58c4-3d84-9e8c-feb9e0cb0e46 | -12.85925 | -46.94283 | 2025-10-01 12:00:00 | TERRA_M-T | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 18.0 |
| 96d03dcf-5975-38e9-a836-4a3074d88763 | -12.76587 | -46.88433 | 2025-10-01 12:00:00 | TERRA_M-T | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 13.3 |
| f4405de8-759d-36bd-b217-bc7292cadc80 | -13.37673 | -48.09979 | 2025-10-01 12:00:00 | TERRA_M-T | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 24.0 |
| f6176d8d-3449-36cc-9625-3530f337954d | -13.82862 | -47.50269 | 2025-10-01 12:00:00 | TERRA_M-T | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 8.0 |
| fef687d8-6e73-30ff-9f65-7542c1db4958 | -8.91363 | -47.61777 | 2025-10-01 12:00:00 | TERRA_M-T | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 17.7 |
| 9f539681-71f9-3f94-8423-e691a05bc3d6 | -14.35087 | -45.90625 | 2025-10-01 12:00:00 | TERRA_M-T | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 38.3 |
| 2b2dd776-fc18-39c5-bc73-96d8bef7c551 | -10.35617 | -43.73816 | 2025-10-01 12:00:00 | TERRA_M-T | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 6.8 |
| d0fe2528-4cd6-3634-9a0f-a3bfefc87c00 | -7.83019 | -48.18535 | 2025-10-01 12:00:00 | TERRA_M-T | PALMEIRANTE | TOCANTINS | Brasil | 1715705 | 17 | 33 | nan | nan | nan | Cerrado | 37.3 |
| ca29ae30-c353-3fea-95d2-aebc083f2e58 | -7.73848 | -46.19425 | 2025-10-01 12:00:00 | TERRA_M-T | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 30.9 |
| 99e3ced6-fcb5-3d68-8882-682bf77b9b98 | -14.22367 | -41.24604 | 2025-10-01 12:00:00 | TERRA_M-T | TANHAÇU | BAHIA | Brasil | 2931004 | 29 | 33 | nan | nan | nan | Caatinga | 8.1 |
| c8c07525-7ae1-378b-9158-cf328e8742d0 | -9.81195 | -47.83912 | 2025-10-01 12:00:00 | TERRA_M-T | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 26.5 |
| 0d6ac8ac-6b6b-3ee4-8955-c4b2c5afcbb5 | -11.8542 | -45.01656 | 2025-10-01 12:00:00 | TERRA_M-T | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 46.5 |
| e5fdb8ca-c3fa-34ff-ac4b-7f2f3d6f68e6 | -10.97623 | -46.52478 | 2025-10-01 12:00:00 | TERRA_M-T | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 113.4 |
| 7d87bbd6-4d77-3ae7-97cf-ca97d0af8693 | -8.89555 | -46.67825 | 2025-10-01 12:00:00 | TERRA_M-T | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 17.6 |
| 6b051f0f-4110-33a0-bc0a-9b0190c387e6 | -11.92319 | -47.89901 | 2025-10-01 12:00:00 | TERRA_M-T | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 22.0 |
| a105cced-15a6-3fdf-acd4-018c3079c3f1 | -11.43275 | -43.50233 | 2025-10-01 12:00:00 | TERRA_M-T | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 13.7 |
| 1839a3d3-74f0-32da-bece-4e3d2d345435 | -14.17703 | -46.12758 | 2025-10-01 12:00:00 | TERRA_M-T | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 691ba2d8-159a-3c11-8400-78b5ae2c4180 | -8.90654 | -45.0436 | 2025-10-01 12:00:00 | TERRA_M-T | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 9.5 |
| efc3e1e9-253b-3a66-8cb7-3402d98c9082 | -10.63279 | -48.5952 | 2025-10-01 12:00:00 | TERRA_M-T | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 17.1 |
| e73385a3-bd45-3497-baef-cd9bf529122c | -8.50637 | -47.27313 | 2025-10-01 12:00:00 | TERRA_M-T | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 75.1 |
| 5cdd31a5-fd7c-31d7-ad96-94d9f3e7d7d3 | -13.00603 | -42.62337 | 2025-10-01 12:00:00 | TERRA_M-T | MACAÚBAS | BAHIA | Brasil | 2919801 | 29 | 33 | nan | nan | nan | Caatinga | 7.9 |
| 458462e2-f176-3b38-a224-aaceda195f0b | -13.32588 | -47.83632 | 2025-10-01 12:00:00 | TERRA_M-T | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 58.9 |
| cd0fab4c-5ec2-37d9-a2de-38c93a4d2d63 | -13.67426 | -48.05735 | 2025-10-01 12:00:00 | TERRA_M-T | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 32.5 |
| 47cdaae9-8e3e-338e-9194-6288853ee02f | -13.79973 | -47.48302 | 2025-10-01 12:00:00 | TERRA_M-T | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 9.8 |
| 5b7acc19-16ea-3155-9b97-26563def1fbe | -8.90173 | -46.6715 | 2025-10-01 12:00:00 | TERRA_M-T | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 22.5 |
| 4f184d2c-5c1b-3f7a-9f9c-b9e04c25fef1 | -12.69368 | -45.27148 | 2025-10-01 12:00:00 | TERRA_M-T | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 100.9 |
| be6bc68f-3cf8-3586-9c50-c0d0fec5e80b | -13.63293 | -47.6429 | 2025-10-01 12:00:00 | TERRA_M-T | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 48.6 |
| 0cbb85a0-1a49-3d3e-80bf-ef41da2f78d6 | -11.71514 | -44.46759 | 2025-10-01 12:00:00 | TERRA_M-T | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 7.2 |
| 6ba84d08-11f6-3bd1-9cd6-caf1456c5539 | -11.61152 | -45.04104 | 2025-10-01 12:00:00 | TERRA_M-T | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 17.5 |
| b2946ef0-90a4-3555-9ed7-a93e14f69c2a | -8.83375 | -46.65516 | 2025-10-01 12:00:00 | TERRA_M-T | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 16.6 |
| 035fea0b-049e-3413-ae79-0a1c19cdb875 | -12.49867 | -50.26683 | 2025-10-01 12:00:00 | TERRA_M-T | SÃO MIGUEL DO ARAGUAIA | GOIÁS | Brasil | 5220207 | 52 | 33 | nan | nan | nan | Cerrado | 84.8 |
| 45249e73-4dbf-3173-b8f2-06732960a7de | -13.75341 | -40.23338 | 2025-10-01 12:00:00 | TERRA_M-T | JEQUIÉ | BAHIA | Brasil | 2918001 | 29 | 33 | nan | nan | nan | Caatinga | 8.8 |
| 271edabb-e03f-3f66-9e19-dea055ca459e | -11.08215 | -47.81814 | 2025-10-01 12:00:00 | TERRA_M-T | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 24.2 |
| d1119d8f-bc82-38a9-8e01-6f8eb5a139f2 | -8.57999 | -45.50637 | 2025-10-01 12:00:00 | TERRA_M-T | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 7d678f98-0b9a-347e-bd80-c4054273bd57 | -11.19601 | -42.12429 | 2025-10-01 12:00:00 | TERRA_M-T | CENTRAL | BAHIA | Brasil | 2907608 | 29 | 33 | nan | nan | nan | Caatinga | 7.3 |
| 7cf2082b-f69c-3958-ba45-6200e6b5e9c3 | -12.01729 | -46.62395 | 2025-10-01 12:00:00 | TERRA_M-T | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 8.3 |
| 3b99ede9-65d8-3d8f-b57b-644f1cc4bd35 | -8.8974 | -46.63009 | 2025-10-01 12:00:00 | TERRA_M-T | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 32.2 |
| c5c6d63d-8470-356a-b0c1-badb43f30c6b | -14.19089 | -41.34855 | 2025-10-01 12:00:00 | TERRA_M-T | TANHAÇU | BAHIA | Brasil | 2931004 | 29 | 33 | nan | nan | nan | Caatinga | 13.2 |
| b6ee03c5-6d54-3a69-bbe6-06d9ba014a8e | -14.354 | -45.94899 | 2025-10-01 12:00:00 | TERRA_M-T | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 34.2 |
| 7d414250-d18f-363d-a5e2-a827e23e779c | -8.56145 | -44.75632 | 2025-10-01 12:00:00 | TERRA_M-T | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 33.0 |
| c83c762b-b6f5-3039-af2e-539e533262bf | -13.53784 | -47.25513 | 2025-10-01 12:00:00 | TERRA_M-T | TERESINA DE GOIÁS | GOIÁS | Brasil | 5221080 | 52 | 33 | nan | nan | nan | Cerrado | 17.1 |
| 7d178abf-a921-3241-9786-cf7955449b2d | -12.87655 | -44.59859 | 2025-10-01 12:00:00 | TERRA_M-T | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 10.6 |
| b0f66f55-5e73-3d3f-b0b3-7cdf20a2638d | -7.55546 | -46.79124 | 2025-10-01 12:00:00 | TERRA_M-T | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 45.2 |
| 44fea5c0-d331-32c2-8b5d-f7851bdab758 | -8.69069 | -47.71498 | 2025-10-01 12:00:00 | TERRA_M-T | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 127.7 |
| cd0796f7-fa56-348a-8bf1-415b06b81009 | -8.70774 | -44.84703 | 2025-10-01 12:00:00 | TERRA_M-T | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 22.6 |
| 739fbbcc-8ca7-31ca-947d-30a70e64b9fd | -12.84032 | -46.86563 | 2025-10-01 12:00:00 | TERRA_M-T | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 8.9 |
| cae647c4-b728-3dd7-82dc-4b7c98790c77 | -10.98451 | -46.53849 | 2025-10-01 12:00:00 | TERRA_M-T | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 20.4 |
| e7b9cfd1-61de-3449-98a2-e26c8c75b6fb | -11.46812 | -45.00336 | 2025-10-01 12:00:00 | TERRA_M-T | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 9.3 |
| 92794576-5262-3418-86eb-a1705ec980f2 | -12.7747 | -42.43124 | 2025-10-01 12:00:00 | TERRA_M-T | IBIPITANGA | BAHIA | Brasil | 2912509 | 29 | 33 | nan | nan | nan | Caatinga | 8.3 |
| b659ee14-e17b-30a0-b5c0-7c4fd25dd662 | -14.91401 | -41.32999 | 2025-10-01 12:00:00 | TERRA_M-T | TREMEDAL | BAHIA | Brasil | 2931806 | 29 | 33 | nan | nan | nan | Caatinga | 5.1 |
| 92efb90e-4d64-35e8-a0e8-b1cc783ef615 | -12.58249 | -41.28673 | 2025-10-01 12:00:00 | TERRA_M-T | ANDARAÍ | BAHIA | Brasil | 2901304 | 29 | 33 | nan | nan | nan | Caatinga | 29.6 |
| c07ed9ac-1079-369d-8a6b-452f2492e6ad | -14.34462 | -45.94756 | 2025-10-01 12:00:00 | TERRA_M-T | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 70.8 |
| 145e1933-b871-39b5-a577-86d8582d3365 | -8.83581 | -46.64199 | 2025-10-01 12:00:00 | TERRA_M-T | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 12.1 |
| 1bb2c64d-903c-3932-a218-f1151dcc9c00 | -13.32815 | -47.82183 | 2025-10-01 12:00:00 | TERRA_M-T | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 33.8 |
| e5993725-8aab-36cc-8b13-a25fc02a442a | -10.54351 | -47.86969 | 2025-10-01 12:00:00 | TERRA_M-T | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 13.9 |
| 5ee123a7-1a23-32e9-b66b-29427c6037d8 | -12.62438 | -44.86694 | 2025-10-01 12:00:00 | TERRA_M-T | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 34.1 |
| 7d66e49d-2e10-3351-90d2-c071f9164402 | -12.62581 | -44.85738 | 2025-10-01 12:00:00 | TERRA_M-T | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 28.9 |
| 0187d639-f282-3ba5-9132-6492591e0b99 | -7.73655 | -46.207 | 2025-10-01 12:00:00 | TERRA_M-T | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 83.4 |
| 9870430f-025b-3885-8c38-85d9e3dd129d | -11.69179 | -45.35298 | 2025-10-01 12:00:00 | TERRA_M-T | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 7.4 |
| 934eb9f5-935e-37e0-81db-9dd8060946e1 | -12.75574 | -46.88268 | 2025-10-01 12:00:00 | TERRA_M-T | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 19.4 |
| 42a09714-401c-3533-b8f7-ee129d7cc58a | -11.1973 | -42.11515 | 2025-10-01 12:00:00 | TERRA_M-T | CENTRAL | BAHIA | Brasil | 2907608 | 29 | 33 | nan | nan | nan | Caatinga | 9.4 |
| fa424728-fca8-31bb-a951-2c7ec55c3484 | -9.0206 | -46.70964 | 2025-10-01 12:00:00 | TERRA_M-T | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 20.6 |
| e4041a50-7bda-3b68-8a71-8d3fa48358d3 | -12.66451 | -46.87519 | 2025-10-01 12:00:00 | TERRA_M-T | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 14.7 |
| aae80f07-9f49-31bb-9b94-15f88e7736cb | -7.88347 | -47.27776 | 2025-10-01 12:00:00 | TERRA_M-T | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 24.7 |
| 34924dcd-c0a2-378b-b20f-5f11fff6315d | -7.83958 | -48.20494 | 2025-10-01 12:00:00 | TERRA_M-T | PALMEIRANTE | TOCANTINS | Brasil | 1715705 | 17 | 33 | nan | nan | nan | Cerrado | 35.3 |
| 2d5e6be2-422d-3148-b7be-c9fab5d838d1 | -8.88638 | -46.59543 | 2025-10-01 12:00:00 | TERRA_M-T | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 21.7 |
| 383e2e64-d9d4-3422-b268-082466eefb6f | -11.8364 | -48.07611 | 2025-10-01 12:00:00 | TERRA_M-T | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 50.4 |
| f8020b6f-9791-360e-bbdc-25e329311a48 | -14.55674 | -40.5633 | 2025-10-01 12:00:00 | TERRA_M-T | PLANALTO | BAHIA | Brasil | 2925006 | 29 | 33 | nan | nan | nan | Caatinga | 11.6 |
| 86405ece-bada-395d-b3a2-e8cbd3588723 | -11.81546 | -44.97394 | 2025-10-01 12:00:00 | TERRA_M-T | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 21.2 |
| 508ac464-576e-36bc-bed5-1bb051a068bb | -8.52786 | -47.28325 | 2025-10-01 12:00:00 | TERRA_M-T | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 40.0 |
| a40c87f2-f71f-3090-85ad-0bb584c72906 | -13.67652 | -48.04353 | 2025-10-01 12:00:00 | TERRA_M-T | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 59.7 |
| 39139dde-0596-3e3c-84f1-5acb0f2980bd | -9.45744 | -47.60007 | 2025-10-01 12:00:00 | TERRA_M-T | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 36.7 |
| 0b41717d-4d2d-3156-8f63-f7dc723874bd | -8.69316 | -47.69925 | 2025-10-01 12:00:00 | TERRA_M-T | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 28.2 |
| 5fa1ddc6-8e91-362e-922f-ad1b144dc83f | -7.99263 | -47.31669 | 2025-10-01 12:00:00 | TERRA_M-T | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 17.1 |
| 25b06bea-6505-3998-a934-4f6cb8a1987f | -13.335 | -47.87326 | 2025-10-01 12:00:00 | TERRA_M-T | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 49.2 |
| 7bcc4ea2-6c2d-33bc-948e-88a07a3e3cd1 | -11.94478 | -43.91041 | 2025-10-01 12:00:00 | TERRA_M-T | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 9.1 |


[Clique aqui para ver as próximas entradas](README145.md)
