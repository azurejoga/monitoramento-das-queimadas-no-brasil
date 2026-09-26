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
| 5ed859f9-682e-33bc-aa8e-4ad4d56bdd1b | -12.20871 | -50.34495 | 2026-09-26 04:27:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 7.9 |
| 1ba6e980-e4ce-321b-868d-4b5375555fcd | -9.26297 | -40.59621 | 2026-09-26 04:27:00 | NOAA-20 | PETROLINA | PERNAMBUCO | Brasil | 2611101 | 26 | 33 | nan | nan | nan | Caatinga | 1.2 |
| eeb4b9ed-54bc-3161-896e-18ef07aac95a | -9.46731 | -40.32924 | 2026-09-26 04:27:00 | NOAA-20 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 8.0 |
| 2b4a4bb2-7d54-3c0e-a257-a9855d08d645 | -8.4956 | -54.78014 | 2026-09-26 04:27:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 4daad424-538e-3e28-8a36-b08d712a2387 | -15.20512 | -49.29329 | 2026-09-26 04:27:00 | NOAA-20 | GOIANÉSIA | GOIÁS | Brasil | 5208608 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 9eb26c95-c2b0-3282-a6f2-5de5d97c49c6 | -9.63605 | -55.13808 | 2026-09-26 04:27:00 | NOAA-20 | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| b8fe2f21-0d59-3037-bddc-a6aa2c743d16 | -9.50938 | -54.66378 | 2026-09-26 04:27:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 1424c8c9-9a46-3c68-96f7-c6464c93f8ea | -12.25307 | -50.31211 | 2026-09-26 04:27:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 2ecb3af5-dddb-3e83-a3bf-f2af1759dfb3 | -12.07357 | -42.21955 | 2026-09-26 04:27:00 | NOAA-20 | BROTAS DE MACAÚBAS | BAHIA | Brasil | 2904506 | 29 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 01b45eac-2f5b-32d0-ad44-1849e29eff1e | -15.24751 | -43.27099 | 2026-09-26 04:27:00 | NOAA-20 | PAI PEDRO | MINAS GERAIS | Brasil | 3146552 | 31 | 33 | nan | nan | nan | Caatinga | 10.6 |
| 154c8789-44ee-351a-8ddc-a90c8691b344 | -11.85781 | -50.54449 | 2026-09-26 04:27:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 4.3 |
| b8c45c24-fa4a-3cff-b360-3941f8aca0e9 | -13.70905 | -48.81007 | 2026-09-26 04:27:00 | NOAA-20 | FORMOSO | GOIÁS | Brasil | 5208103 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 6b47bf9a-aced-3be2-b2ce-a537714482d4 | -8.52398 | -44.96742 | 2026-09-26 04:27:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 7b224c13-3704-3587-a455-6dbdc9404440 | -12.26407 | -50.7261 | 2026-09-26 04:27:00 | NOAA-20 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 16.1 |
| 7edd06a4-b3b8-3d7a-a9b2-e590f65556a1 | -14.47503 | -53.63984 | 2026-09-26 04:27:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 327fbb10-7277-3883-9c3f-e7a616f13018 | -9.54195 | -56.16068 | 2026-09-26 04:27:00 | NOAA-20 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 5fa3945b-d382-3c11-b0dc-92e842c67956 | -8.49764 | -54.78038 | 2026-09-26 04:27:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 2ed814d3-f85a-36c4-b263-5d388319da61 | -13.7056 | -48.80944 | 2026-09-26 04:27:00 | NOAA-20 | FORMOSO | GOIÁS | Brasil | 5208103 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 544624a2-a14d-3e05-bfc0-3e84ca324748 | -10.76178 | -50.84047 | 2026-09-26 04:27:00 | NOAA-20 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 5.3 |
| dd9b7c69-8775-3579-9a33-19f0baa102c5 | -12.26705 | -50.3437 | 2026-09-26 04:27:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 10.8 |
| e7ffecd6-6db2-3d08-a4ce-3e39fb04c24e | -13.71662 | -48.80735 | 2026-09-26 04:27:00 | NOAA-20 | FORMOSO | GOIÁS | Brasil | 5208103 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 171b4824-226c-3576-83c3-8cf2e8e48fc2 | -11.78909 | -50.65695 | 2026-09-26 04:27:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 4578ec2d-4dc7-384e-80be-4b446b9618ed | -14.86389 | -47.14175 | 2026-09-26 04:27:00 | NOAA-20 | VILA BOA | GOIÁS | Brasil | 5222203 | 52 | 33 | nan | nan | nan | Cerrado | 3.4 |
| cbdcc8b0-7516-3228-9fc2-0c9c17705758 | -12.68165 | -47.29388 | 2026-09-26 04:27:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 2aee7210-ef9a-3b4c-803f-0fa9ade03fbf | -12.27652 | -50.72328 | 2026-09-26 04:27:00 | NOAA-20 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 6046f970-484f-3f59-bde9-4748e1523f36 | -11.12606 | -42.8245 | 2026-09-26 04:27:00 | NOAA-20 | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Caatinga | 1.2 |
| faac91ca-f1b9-33cd-bc11-6171755c1c43 | -12.60502 | -51.9496 | 2026-09-26 04:27:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 8f97502b-ca6f-37f8-b662-4ddc1c857626 | -12.60157 | -51.94502 | 2026-09-26 04:27:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| ae921aae-ad1c-30de-aa13-7d1bac7bc3e7 | -10.40965 | -53.81304 | 2026-09-26 04:27:00 | NOAA-20 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 9d86fd41-7513-3769-99c1-83d68ed71834 | -15.1621 | -48.81565 | 2026-09-26 04:27:00 | NOAA-20 | VILA PROPÍCIO | GOIÁS | Brasil | 5222302 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 9b79c8ab-bfdc-3334-b009-e19c7e010377 | -11.96005 | -50.67209 | 2026-09-26 04:27:00 | NOAA-20 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| a58e9e9d-5ec7-37a2-a633-8c7aa43e0684 | -11.78995 | -51.01568 | 2026-09-26 04:27:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 2.7 |
| b4f63ef1-5496-301b-bb3f-778da6f49c58 | -9.47191 | -40.32618 | 2026-09-26 04:27:00 | NOAA-20 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 6.0 |
| 8d4fafe6-b6c7-33dc-bb9c-20b6a31ad8a1 | -12.00222 | -50.30347 | 2026-09-26 04:27:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| b04c2dca-c3f7-37a1-89ae-8f498353f18a | -11.89502 | -50.5815 | 2026-09-26 04:27:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| a32ee311-f952-3a4f-a33b-2deff83cb272 | -11.02181 | -54.04856 | 2026-09-26 04:27:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 9cbde4d9-9035-33ad-adcf-566b179afe35 | -15.25184 | -43.26704 | 2026-09-26 04:27:00 | NOAA-20 | PAI PEDRO | MINAS GERAIS | Brasil | 3146552 | 31 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 0f9d4dd0-bbfe-3c54-aaeb-56e80f829684 | -14.86891 | -47.13161 | 2026-09-26 04:27:00 | NOAA-20 | VILA BOA | GOIÁS | Brasil | 5222203 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| addfa12b-483b-3bbb-8bf6-a710c265034a | -11.7387 | -50.61972 | 2026-09-26 04:27:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 6cac6df1-9972-3ae6-b7a3-303edd11a076 | -12.94214 | -51.06668 | 2026-09-26 04:27:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 23.2 |
| 569e794d-82a5-304c-adc8-1e8ced92d6d7 | -9.4668 | -40.33288 | 2026-09-26 04:27:00 | NOAA-20 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 8.0 |
| a1f8663b-5d53-33bb-8cfe-7893aecf5925 | -12.67889 | -47.28975 | 2026-09-26 04:27:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 9166b9e4-3de6-39bf-ba0c-3336fe41c7f0 | -12.13106 | -50.30041 | 2026-09-26 04:27:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| a4229c5a-25e5-34b6-9c53-c52dbff148de | -15.42152 | -47.89951 | 2026-09-26 04:27:00 | NOAA-20 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 258f0cf1-d06b-35f2-ad34-e68833088314 | -12.59999 | -51.94499 | 2026-09-26 04:27:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 0521f7af-18df-3c12-9a74-bf77d34df1f7 | -11.95918 | -50.67705 | 2026-09-26 04:27:00 | NOAA-20 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| ca5423ec-15fa-3b63-8991-e4b7593f3178 | -11.73917 | -50.62234 | 2026-09-26 04:27:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 500aa45f-cc84-3a62-8ada-647161db1224 | -11.27974 | -54.43974 | 2026-09-26 04:27:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 6.9 |
| ccb77662-ad97-3303-bf4b-2d961d1565c7 | -13.078 | -47.42677 | 2026-09-26 04:27:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 09933393-3b6a-3778-9e28-3c819f79ae6c | -14.96383 | -47.5369 | 2026-09-26 04:27:00 | NOAA-20 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 87d002cb-d06e-30b6-8437-22429c953f63 | -12.59672 | -51.94805 | 2026-09-26 04:27:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 906d8628-17b8-3b6e-b143-b6e3758881f7 | -12.59187 | -51.9511 | 2026-09-26 04:27:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 58371e50-0681-345f-91d0-b7d25a5c0bc0 | -12.25463 | -50.73458 | 2026-09-26 04:27:00 | NOAA-20 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| e4c71c04-2f3a-3ed2-a9b1-5ccc36decbae | -12.25143 | -50.32149 | 2026-09-26 04:27:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 2d9f4a5c-29ae-359c-94f1-3509fb33674b | -12.15815 | -50.32124 | 2026-09-26 04:27:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 8.6 |
| 565f6cf5-9b17-3138-b792-1d09a1cd0de0 | -7.77412 | -54.68679 | 2026-09-26 04:27:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| d1606854-090e-3941-a6c7-0583c83b8895 | -11.93889 | -38.28661 | 2026-09-26 04:27:00 | NOAA-20 | INHAMBUPE | BAHIA | Brasil | 2913705 | 29 | 33 | nan | nan | nan | Mata Atlântica | 2.4 |
| 0e0a7fe2-0166-3b21-80e6-7d201c71dbf3 | -11.76455 | -50.63715 | 2026-09-26 04:27:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 13229f0d-a6d2-347c-89da-624fbb7f36b1 | -12.26838 | -50.3585 | 2026-09-26 04:27:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 78b472c0-ec07-373c-86e2-ceb430c8105a | -12.26031 | -50.33762 | 2026-09-26 04:27:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 4fc5248b-d1b0-3113-a83b-149bc316d590 | -12.24105 | -50.35842 | 2026-09-26 04:27:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 5.3 |
| f81cf507-fddc-366a-b563-17df3c4f8ebb | -14.33466 | -52.72252 | 2026-09-26 04:27:00 | NOAA-20 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| c472d371-1dbb-30ed-9dab-4b24a4d1055c | -11.78897 | -51.00842 | 2026-09-26 04:27:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 59b424f1-83bc-3061-b248-1920150e1e5e | -14.86778 | -47.13874 | 2026-09-26 04:27:00 | NOAA-20 | VILA BOA | GOIÁS | Brasil | 5222203 | 52 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 3bb78376-4073-302f-9aa5-1e70a4fef2c6 | -11.27615 | -54.43428 | 2026-09-26 04:27:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 7e54a6a6-b4b7-3170-8c80-93436cef82b6 | -12.1243 | -50.29434 | 2026-09-26 04:27:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| fa22c9dc-fae6-308d-84a6-d9a65f48a780 | -13.08195 | -47.4236 | 2026-09-26 04:27:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 0981f426-595f-3f82-9596-1705d57c488b | -11.94454 | -50.68719 | 2026-09-26 04:27:00 | NOAA-20 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 8afee769-42c0-3c7e-8024-77f0757e50da | -11.28085 | -54.43392 | 2026-09-26 04:27:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 7.5 |
| 1e0e22df-15c2-3d8e-a170-c226f317b76d | -11.2706 | -54.43624 | 2026-09-26 04:27:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 51828b99-ba4f-37e8-8ca3-ad4ecca07b31 | -12.26638 | -50.71832 | 2026-09-26 04:27:00 | NOAA-20 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 10.8 |
| 80e7491b-e67d-3a11-b3ab-a84925126358 | -12.16275 | -50.31722 | 2026-09-26 04:27:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 24.3 |
| d19ca511-7744-3238-a24a-60009a069b8c | -11.80073 | -50.65907 | 2026-09-26 04:27:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| b013e886-02bf-3ad6-ad46-0a2a7ebfadee | -14.96051 | -47.53631 | 2026-09-26 04:27:00 | NOAA-20 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 1fd8cf4f-cf6f-3d2e-baea-eb9f0e54813d | -12.04771 | -50.62703 | 2026-09-26 04:27:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 72043d9d-3418-3240-9f6d-71b7303c8ea9 | -11.76067 | -50.63644 | 2026-09-26 04:27:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 6baad7e0-b47b-3bda-93b6-71121e64a029 | -11.17569 | -50.04898 | 2026-09-26 04:27:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 86d7cd5d-fcb4-3480-8e25-cb275671aa12 | -11.90273 | -50.5829 | 2026-09-26 04:27:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 8d9e21f6-51a7-36a4-a80b-d26881632e40 | -12.2493 | -50.31143 | 2026-09-26 04:27:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| f573fa75-49f8-3be4-8167-8ad3fd316166 | -12.16193 | -50.32192 | 2026-09-26 04:27:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 24.3 |
| 82a904c8-4059-366c-a907-9fb22c751227 | -11.27669 | -54.43135 | 2026-09-26 04:27:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| dba96438-7ab3-3a62-96ae-927ebc9ca7f5 | -10.79295 | -49.06951 | 2026-09-26 04:27:00 | NOAA-20 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| fb0f222d-5e1b-3d2f-ab3b-047b4290af30 | -11.27027 | -54.43494 | 2026-09-26 04:27:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 9a95e972-71a1-343d-869c-9ab8bc488fd9 | -12.26409 | -50.33831 | 2026-09-26 04:27:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| f643b381-28aa-3685-84e7-58c8ba076f1b | -10.99372 | -58.66268 | 2026-09-26 04:27:00 | NOAA-20 | CASTANHEIRA | MATO GROSSO | Brasil | 5102850 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 79bb2d51-1a65-3c04-b89b-15850b5fa6e0 | -14.86564 | -48.20616 | 2026-09-26 04:27:00 | NOAA-20 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| f2b90a78-0b80-313b-bc3a-f8aa7ee38612 | -12.26081 | -50.35713 | 2026-09-26 04:27:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 7610bd96-796b-320d-b0d5-b86cd1bd786e | -11.90574 | -50.5885 | 2026-09-26 04:27:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 83bab1ab-251d-3ffe-ac25-d0e42115123c | -11.96393 | -50.6728 | 2026-09-26 04:27:00 | NOAA-20 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 2d82907e-e4fb-362e-9e03-115999c1dccf | -13.20067 | -48.32396 | 2026-09-26 04:27:00 | NOAA-20 | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 41bd466f-8370-3c48-8b08-25c47e5146a1 | -11.77531 | -50.64421 | 2026-09-26 04:27:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| e24ef7f1-3377-351f-bbdd-fc58c807884e | -13.91731 | -46.16915 | 2026-09-26 04:27:00 | NOAA-20 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 976b4467-3dc8-3ee6-91eb-314e612d50e0 | -12.26277 | -50.32354 | 2026-09-26 04:27:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 08839895-bf06-3d18-bc4f-f9ed1886bea6 | -8.50097 | -54.78125 | 2026-09-26 04:27:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 1c8a7ef8-c87f-3fac-93cd-3e6eab987b4f | -12.01943 | -50.65232 | 2026-09-26 04:27:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 597642a1-f736-3bf6-81f9-32432b587c1f | -8.23377 | -54.66625 | 2026-09-26 04:27:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 9b5b5d6f-ba45-335e-98c4-f63e98f7766d | -12.60848 | -51.95417 | 2026-09-26 04:27:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 7ab0b56a-e2f2-3509-8fe5-7183a9b70150 | -13.70974 | -48.80602 | 2026-09-26 04:27:00 | NOAA-20 | FORMOSO | GOIÁS | Brasil | 5208103 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 96f28788-12ec-3522-8ac6-5b5c79316bfa | -9.54253 | -56.15822 | 2026-09-26 04:27:00 | NOAA-20 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 62f59c78-58e0-38dc-a750-6285ffe54b12 | -14.87383 | -47.14342 | 2026-09-26 04:27:00 | NOAA-20 | VILA BOA | GOIÁS | Brasil | 5222203 | 52 | 33 | nan | nan | nan | Cerrado | 21.9 |


[Clique aqui para ver as próximas entradas](README18.md)
