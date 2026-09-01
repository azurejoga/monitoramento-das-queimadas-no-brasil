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

## Dados Diários - Página 91

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| d66e3cca-f047-324a-a1bf-81e99db6fedf | -10.0353 | -44.7019 | 2026-09-01 11:13:00 | TERRA_M-M | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 31.3 |
| 2c39c687-8a7d-3ca5-866d-ce880b738a1c | -10.45006 | -46.75031 | 2026-09-01 11:13:00 | TERRA_M-M | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 20.9 |
| aa0b651e-cfc1-3ec3-8c90-c2d536151626 | -11.26582 | -45.10471 | 2026-09-01 11:13:00 | TERRA_M-M | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 12.5 |
| ec69d860-4e98-3647-9d71-0d08498b0719 | -11.9114 | -45.0719 | 2026-09-01 11:13:00 | TERRA_M-M | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 13.0 |
| fba612ba-a399-3d32-af6f-f7abefaebe82 | -10.02885 | -44.69498 | 2026-09-01 11:13:00 | TERRA_M-M | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 16.0 |
| f32f1421-3e1d-35a6-8e57-34966349308d | -11.5334 | -45.50029 | 2026-09-01 11:13:00 | TERRA_M-M | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 29.5 |
| 7861e3af-2d5e-3dac-af9d-17b8c155b461 | -7.39732 | -37.35995 | 2026-09-01 11:13:00 | TERRA_M-M | SÃO JOSÉ DO EGITO | PERNAMBUCO | Brasil | 2613602 | 26 | 33 | nan | nan | nan | Caatinga | 4.2 |
| 7211feb4-b61c-33e1-894d-b135bbd3763f | -7.41781 | -38.77165 | 2026-09-01 11:13:00 | TERRA_M-M | MAURITI | CEARÁ | Brasil | 2308104 | 23 | 33 | nan | nan | nan | Caatinga | 8.0 |
| d43f4b81-24fa-35cd-90fb-30942efbe1cb | -11.2153 | -46.08033 | 2026-09-01 11:13:00 | TERRA_M-M | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 51.6 |
| 836e0427-05b3-3a4e-8699-819beae33616 | -11.52428 | -45.47917 | 2026-09-01 11:13:00 | TERRA_M-M | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 650.1 |
| c0a9a4b6-0534-3c09-8724-70b42ccfa884 | -11.32542 | -45.15504 | 2026-09-01 11:13:00 | TERRA_M-M | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 11.6 |
| fbff061a-90a0-397e-b92a-d122c9c17bac | -11.32258 | -45.17276 | 2026-09-01 11:13:00 | TERRA_M-M | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 16.6 |
| 21f98d75-332b-3a5b-8505-0c35420195a6 | -7.41655 | -38.78049 | 2026-09-01 11:13:00 | TERRA_M-M | MAURITI | CEARÁ | Brasil | 2308104 | 23 | 33 | nan | nan | nan | Caatinga | 12.8 |
| 8fdfa514-cde0-3a9b-a5f0-252290f3abb3 | -11.53637 | -45.48209 | 2026-09-01 11:13:00 | TERRA_M-M | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 45.6 |
| 8ef8f07b-154c-3724-97ea-9d36ff16605e | -10.04068 | -44.69675 | 2026-09-01 11:13:00 | TERRA_M-M | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 14.3 |
| d5669d75-e4a0-36e9-9e91-0c3bebef0396 | -4.7673 | -41.79798 | 2026-09-01 11:13:00 | TERRA_M-M | JATOBÁ DO PIAUÍ | PIAUÍ | Brasil | 2205276 | 22 | 33 | nan | nan | nan | Caatinga | 6.9 |
| bcf6e502-9132-3fdf-9410-2f1abfe05fbf | -7.25204 | -39.22157 | 2026-09-01 11:13:00 | TERRA_M-M | MISSÃO VELHA | CEARÁ | Brasil | 2308401 | 23 | 33 | nan | nan | nan | Caatinga | 68.6 |
| 35ab96a1-2c57-31e6-a1cf-42d3a43fdfa8 | -6.68089 | -43.41433 | 2026-09-01 11:13:00 | TERRA_M-M | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 31.9 |
| c4671cfb-053d-39e5-b445-d43aacacd1cb | -11.25643 | -45.12654 | 2026-09-01 11:13:00 | TERRA_M-M | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 16.6 |
| 4f4e7dc3-45d8-3c51-a3d8-ecb17c6343d7 | -7.39861 | -37.35072 | 2026-09-01 11:13:00 | TERRA_M-M | SÃO JOSÉ DO EGITO | PERNAMBUCO | Brasil | 2613602 | 26 | 33 | nan | nan | nan | Caatinga | 4.1 |
| 3a673a70-750b-323a-b9e7-7283e52a1954 | -8.70033 | -41.30836 | 2026-09-01 11:13:00 | TERRA_M-M | AFRÂNIO | PERNAMBUCO | Brasil | 2600203 | 26 | 33 | nan | nan | nan | Caatinga | 5.1 |
| e5e08bc4-c312-38d2-ba4b-0a4c96fe22ef | -11.52129 | -45.49739 | 2026-09-01 11:13:00 | TERRA_M-M | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 807.7 |
| c537c0bc-570a-3242-a8e2-9ff29beeb191 | -11.53 | -45.51 | 2026-09-01 11:15:00 | MSG-03 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 3f19338a-38b0-3761-84c2-1acc7284fd61 | -19.07867 | -40.11802 | 2026-09-01 11:15:00 | TERRA_M-M | SOORETAMA | ESPÍRITO SANTO | Brasil | 3205010 | 32 | 33 | nan | nan | nan | Mata Atlântica | 5.6 |
| 4ecc3195-02e1-345d-9612-9582e72e543c | -17.06318 | -45.40192 | 2026-09-01 11:15:00 | TERRA_M-M | BURITIZEIRO | MINAS GERAIS | Brasil | 3109402 | 31 | 33 | nan | nan | nan | Cerrado | 13.8 |
| 5c9d97e6-0621-320c-bcbf-65b2fc222331 | -17.27838 | -39.55513 | 2026-09-01 11:15:00 | TERRA_M-M | ALCOBAÇA | BAHIA | Brasil | 2900801 | 29 | 33 | nan | nan | nan | Mata Atlântica | 10.7 |
| 37fed7ff-8e0f-39df-a34d-b319a950183a | -12.09969 | -45.07482 | 2026-09-01 11:15:00 | TERRA_M-M | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 11.3 |
| 22c135a7-1e02-312e-8ed8-ae41805478d2 | -17.13052 | -46.85008 | 2026-09-01 11:15:00 | TERRA_M-M | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 17.6 |
| 6786ac33-dbd0-37c7-b5eb-2856058e7a90 | -15.58835 | -43.81096 | 2026-09-01 11:15:00 | TERRA_M-M | VARZELÂNDIA | MINAS GERAIS | Brasil | 3170909 | 31 | 33 | nan | nan | nan | Caatinga | 7.0 |
| 2905bf62-a414-300f-8cf6-b277d0331f1c | -15.21826 | -46.22824 | 2026-09-01 11:15:00 | TERRA_M-M | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 16.4 |
| 1a5e48f8-c981-34d8-8c89-c7c3168f9f6e | -17.27968 | -39.54557 | 2026-09-01 11:15:00 | TERRA_M-M | ALCOBAÇA | BAHIA | Brasil | 2900801 | 29 | 33 | nan | nan | nan | Mata Atlântica | 7.1 |
| 3f85a665-8837-3689-ad50-6269b08351fe | -17.79218 | -39.69975 | 2026-09-01 11:15:00 | TERRA_M-M | NOVA VIÇOSA | BAHIA | Brasil | 2923001 | 29 | 33 | nan | nan | nan | Mata Atlântica | 5.0 |
| 6b342e45-3259-3040-b00a-27deb0983019 | -20.1709 | -41.77512 | 2026-09-01 11:15:00 | TERRA_M-M | DURANDÉ | MINAS GERAIS | Brasil | 3123528 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.7 |
| 090e2b9b-df98-381b-8674-2387ed400953 | -18.28591 | -42.78534 | 2026-09-01 11:15:00 | TERRA_M-M | COLUNA | MINAS GERAIS | Brasil | 3116803 | 31 | 33 | nan | nan | nan | Mata Atlântica | 13.2 |
| a687e26f-c2dd-36c7-a111-09092f218342 | -12.91277 | -45.82686 | 2026-09-01 11:15:00 | TERRA_M-M | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 13.0 |
| 3bedbfe4-d10b-3c56-95d3-3def5547b275 | -19.07737 | -40.12757 | 2026-09-01 11:15:00 | TERRA_M-M | SOORETAMA | ESPÍRITO SANTO | Brasil | 3205010 | 32 | 33 | nan | nan | nan | Mata Atlântica | 4.7 |
| 738f5993-e05f-3751-8a2d-2b9c82da0386 | -14.95777 | -41.35159 | 2026-09-01 11:15:00 | TERRA_M-M | TREMEDAL | BAHIA | Brasil | 2931806 | 29 | 33 | nan | nan | nan | Caatinga | 6.9 |
| 14300870-e235-3851-8235-53ebc35fb7e0 | -19.90837 | -41.5522 | 2026-09-01 11:15:00 | TERRA_M-M | MUTUM | MINAS GERAIS | Brasil | 3144003 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.3 |
| 9dbc0b8f-c5b6-35f8-93c6-b2cb3b450b9d | -12.7679 | -42.76063 | 2026-09-01 11:15:00 | TERRA_M-M | BOQUIRA | BAHIA | Brasil | 2904100 | 29 | 33 | nan | nan | nan | Caatinga | 7.8 |
| 16734cb6-6150-300b-906a-ad679209c290 | -15.22121 | -46.21057 | 2026-09-01 11:15:00 | TERRA_M-M | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 10.8 |
| 9691cc03-04b2-3d97-b376-a6a90f13739b | -17.06073 | -45.41653 | 2026-09-01 11:15:00 | TERRA_M-M | BURITIZEIRO | MINAS GERAIS | Brasil | 3109402 | 31 | 33 | nan | nan | nan | Cerrado | 11.3 |
| 3685b284-aa22-314b-a2c0-58d8cd9c8f3e | -12.44262 | -43.40254 | 2026-09-01 11:15:00 | TERRA_M-M | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 40.3 |
| de848353-d746-39ed-a9a3-b9a3ab00eed0 | -18.5667 | -41.26773 | 2026-09-01 11:15:00 | TERRA_M-M | ITABIRINHA | MINAS GERAIS | Brasil | 3131802 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.4 |
| 6c65d438-50bd-3ffa-beba-e7dd349c0f88 | -12.95855 | -45.9558 | 2026-09-01 11:15:00 | TERRA_M-M | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 25.1 |
| 48426f78-c936-3475-8bd0-ec7ae68cea89 | -12.44453 | -43.39014 | 2026-09-01 11:15:00 | TERRA_M-M | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 10.5 |
| 940d556f-eae8-36dd-8e23-e05b6e9d711f | -15.85013 | -47.69 | 2026-09-01 11:15:00 | TERRA_M-M | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 21.3 |
| d4bbc0cf-c145-3710-8ad7-02770648b931 | -13.38033 | -41.35051 | 2026-09-01 11:15:00 | TERRA_M-M | IBICOARA | BAHIA | Brasil | 2912202 | 29 | 33 | nan | nan | nan | Caatinga | 6.3 |
| b444ff4f-53cb-37b9-95ce-324cbe8fe14b | -15.59025 | -43.79893 | 2026-09-01 11:15:00 | TERRA_M-M | VERDELÂNDIA | MINAS GERAIS | Brasil | 3171030 | 31 | 33 | nan | nan | nan | Caatinga | 30.2 |
| 4e1ce9a5-096f-39ed-a184-5a7295e2e56a | -15.9797 | -43.67128 | 2026-09-01 11:15:00 | TERRA_M-M | SÃO JOÃO DA PONTE | MINAS GERAIS | Brasil | 3162401 | 31 | 33 | nan | nan | nan | Cerrado | 14.4 |
| 7819815c-d599-36e5-b31f-e915eba32621 | -14.65087 | -41.55575 | 2026-09-01 11:15:00 | TERRA_M-M | MAETINGA | BAHIA | Brasil | 2919959 | 29 | 33 | nan | nan | nan | Caatinga | 4.5 |
| c4224d1e-4485-3f60-84e9-87e32ea0c3b5 | -19.39799 | -40.87251 | 2026-09-01 11:15:00 | TERRA_M-M | BAIXO GUANDU | ESPÍRITO SANTO | Brasil | 3200805 | 32 | 33 | nan | nan | nan | Mata Atlântica | 5.4 |
| 73236a21-6e91-3566-8b60-adc53d54bc18 | -13.5277 | -40.66674 | 2026-09-01 11:15:00 | TERRA_M-M | MARACÁS | BAHIA | Brasil | 2920502 | 29 | 33 | nan | nan | nan | Caatinga | 15.7 |
| 5b14a87d-3eed-3300-a88b-89d8db4b818d | -17.07413 | -45.40383 | 2026-09-01 11:15:00 | TERRA_M-M | BURITIZEIRO | MINAS GERAIS | Brasil | 3109402 | 31 | 33 | nan | nan | nan | Cerrado | 10.1 |
| 04512714-0b6b-3231-8802-0f2ba334a07e | -15.22508 | -46.21797 | 2026-09-01 11:15:00 | TERRA_M-M | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 19.1 |
| 4e2d8996-23c2-3db6-bfa3-367901f2d071 | -17.89615 | -45.87468 | 2026-09-01 11:15:00 | TERRA_M-M | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 8.0 |
| 1dab4da4-757d-32fd-9d0e-a4a33ba9e0dc | -15.17915 | -46.23873 | 2026-09-01 11:15:00 | TERRA_M-M | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 14.0 |
| 6300188c-51b5-3c26-b36b-4571ba1ff4b9 | -16.14531 | -46.67366 | 2026-09-01 11:15:00 | TERRA_M-M | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 12.2 |
| cf7cb69f-6b5b-3f41-a397-128e74b98db8 | -17.11833 | -46.84771 | 2026-09-01 11:15:00 | TERRA_M-M | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 30.1 |
| 3b2aae1f-170e-33f5-a706-2b4771d09d34 | -15.98959 | -43.67291 | 2026-09-01 11:15:00 | TERRA_M-M | CAPITÃO ENÉAS | MINAS GERAIS | Brasil | 3112703 | 31 | 33 | nan | nan | nan | Cerrado | 11.1 |
| 3f240528-1573-3fc9-bd42-65787569bf4a | -16.15752 | -46.67632 | 2026-09-01 11:15:00 | TERRA_M-M | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 12.4 |
| 1281b207-914f-3664-9ba1-e71cd5d97e2c | -17.11513 | -46.86625 | 2026-09-01 11:15:00 | TERRA_M-M | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 16.5 |
| 2b873b77-88d7-32fb-b56e-5b1dcc96862e | -11.5283 | -45.4933 | 2026-09-01 11:20:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 148.8 |
| 358e9b57-34f7-3b05-8768-ba83a6c81036 | -11.213 | -46.0839 | 2026-09-01 11:20:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 85.9 |
| b147daca-67a7-3e6b-87b2-5bf445ee247b | -6.9552 | -55.635 | 2026-09-01 11:20:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 238.0 |
| c2d24027-7a67-3967-aa55-fc7fc45958a6 | -6.1659 | -57.7403 | 2026-09-01 11:30:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 64.8 |
| 66b1d0c4-9c05-3f92-95b9-8b23de66c2b5 | -10.8209 | -50.6945 | 2026-09-01 11:30:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 74.2 |
| 2f80b789-babf-385b-9603-52924730043e | -11.5283 | -45.4933 | 2026-09-01 11:30:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 96.4 |
| f45e6807-67c5-3735-8500-3352a5a28fbd | -11.213 | -46.0839 | 2026-09-01 11:30:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 103.9 |
| 65a03fb3-ad52-3dd2-a814-26fc4f3cd928 | -15.4429 | -52.681 | 2026-09-01 11:30:00 | GOES-19 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 107.7 |
| 11cc75b8-0354-3057-aa57-1e31944a000f | -6.9552 | -55.635 | 2026-09-01 11:40:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 119.8 |
| 6ad9405f-4ed8-35f0-ad36-f8508257e3cf | -11.213 | -46.0839 | 2026-09-01 11:40:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 75.9 |
| 40a9099c-cc4b-3e9a-a8fe-8c7b6f7b254d | -6.9552 | -55.635 | 2026-09-01 11:50:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 224.8 |
| f8da3c84-664e-3a24-874c-fdc6afc12f4d | -15.4429 | -52.681 | 2026-09-01 11:50:00 | GOES-19 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 126.0 |
| 361b3c57-80d5-3512-aad1-046f3b434041 | -6.9553 | -55.6151 | 2026-09-01 11:50:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 105.4 |
| ea218aa0-8f88-3d0c-818b-5233aa1540b5 | -11.2482 | -45.1194 | 2026-09-01 11:50:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 75.9 |
| c34f7ce1-5e85-353f-8142-c22a4aa5f46f | -8.7628 | -46.4642 | 2026-09-01 11:50:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 84.7 |
| ced975ed-dbbc-3f7a-8818-bdce88c83fd0 | -8.7817 | -46.4623 | 2026-09-01 11:50:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 90.8 |
| 1372c393-8615-3239-a9d7-0deeb9eb222e | -6.1659 | -57.7403 | 2026-09-01 11:50:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 64.7 |
| 474a531c-1502-3703-a0a3-657e2553dbc8 | -11.2673 | -45.1167 | 2026-09-01 11:50:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 109.3 |
| 93c1ccf4-6062-319a-8d55-219f7cab360c | -6.9553 | -55.6151 | 2026-09-01 12:00:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 103.9 |
| ea0b2700-547e-3961-ba30-c2d847618931 | -17.4644 | -52.4045 | 2026-09-01 12:00:00 | GOES-19 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 129.6 |
| af07d965-6578-3759-8a83-de247fd3ea03 | -8.7628 | -46.4642 | 2026-09-01 12:00:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 77.1 |
| d2585271-d223-388a-a233-e5020a9a99c5 | -6.9552 | -55.635 | 2026-09-01 12:00:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 222.4 |
| f6a101a0-ecfe-3ed5-bbf8-fc0ac2f200e0 | -8.7817 | -46.4623 | 2026-09-01 12:00:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 76.1 |
| 8c2ffccd-82ba-3025-a508-c66db5f84bc7 | -11.213 | -46.0839 | 2026-09-01 12:00:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 82.2 |
| 60739029-d6d6-3eea-ab6a-5b2b001f237e | -11.2482 | -45.1194 | 2026-09-01 12:00:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 68.9 |
| 5ab2efff-336a-3791-90db-be972f472781 | -14.4397 | -52.4964 | 2026-09-01 12:00:00 | GOES-19 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 93.2 |
| 5cfc720c-376a-3c6a-8cbc-0b6e298dd74f | -15.4429 | -52.681 | 2026-09-01 12:00:00 | GOES-19 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 89.6 |
| f2aed227-c43a-3d94-822f-f1b3c47d42af | -6.1659 | -57.7403 | 2026-09-01 12:00:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 89.1 |
| d17f1e06-e337-396e-88d6-aefd33c18b73 | -10.8627 | -45.356 | 2026-09-01 12:00:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 63.5 |
| bd0891e8-c6b0-3c4e-8689-c11c47a6c2e7 | -11.2673 | -45.1167 | 2026-09-01 12:00:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 82.0 |
| bc3f26eb-97b5-3a0f-a448-b3457cdb9461 | -17.4644 | -52.4045 | 2026-09-01 12:10:00 | GOES-19 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 118.6 |
| bcfc2615-10fa-35ee-b18e-65f40cc915ce | -6.9552 | -55.635 | 2026-09-01 12:10:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 137.6 |
| 5462742d-e9e7-356c-9ba0-573310b328be | -11.2673 | -45.1167 | 2026-09-01 12:10:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 115.1 |
| f290b491-912a-37e6-add0-6a1e3f5f1121 | -10.1324 | -45.8598 | 2026-09-01 12:10:00 | GOES-19 | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 105.7 |
| f57ed9dc-26e5-305a-9b89-4b883532624e | -10.8627 | -45.356 | 2026-09-01 12:10:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 210.0 |
| 7fee5c3e-a353-39a0-9360-4e992f4f9cef | -14.4397 | -52.4964 | 2026-09-01 12:10:00 | GOES-19 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 75.0 |
| 0038991c-0fab-389c-93d0-ba5e25c515cd | -6.1659 | -57.7403 | 2026-09-01 12:10:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 197.2 |
| 964366b8-d773-301e-8b15-1df2aa8ec405 | -14.4204 | -52.4989 | 2026-09-01 12:10:00 | GOES-19 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 73.2 |
| 8b8b1ec4-e22c-3814-b42f-aa3031e0e77f | -10.8818 | -45.3534 | 2026-09-01 12:10:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 117.8 |


[Clique aqui para ver as próximas entradas](README92.md)
