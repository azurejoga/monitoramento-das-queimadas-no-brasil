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

## Dados Diários - Página 110

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| c8b2eb2f-fcea-3a9d-ba1a-cd657eb85047 | -13.22733 | -48.44278 | 2025-10-01 04:51:00 | NPP-375D | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 157bd9be-423b-3e84-aa56-8c84fd80effa | -15.47443 | -45.87582 | 2025-10-01 04:51:00 | NPP-375D | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 9458faaa-1a91-39e9-8390-dfef6fff5697 | -13.7739 | -47.97015 | 2025-10-01 04:51:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 27.6 |
| 6bc166fb-ab36-3515-8b8a-79e21d203eae | -13.31456 | -47.2238 | 2025-10-01 04:51:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 5ce04a03-cb89-3c52-9a34-f9385d80c90d | -13.70853 | -48.63433 | 2025-10-01 04:51:00 | NPP-375D | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 95ad3ce6-b07b-36ea-b92e-3ae3eaea1401 | -13.36867 | -48.11109 | 2025-10-01 04:51:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| d56caca7-7fe1-3625-a70d-6f054b43c37e | -12.87264 | -46.90284 | 2025-10-01 04:51:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| f49ac4d8-693c-3362-a93a-56b7b7aff486 | -14.89894 | -47.20599 | 2025-10-01 04:51:00 | NPP-375D | VILA BOA | GOIÁS | Brasil | 5222203 | 52 | 33 | nan | nan | nan | Cerrado | 0.3 |
| 45e41346-f8a5-37b3-a84e-d07904977b5d | -14.03184 | -47.99554 | 2025-10-01 04:51:00 | NPP-375D | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 3bd902bb-c08c-3467-96ed-d60d5bd7000c | -11.80029 | -47.60063 | 2025-10-01 04:51:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 0280773f-7597-34cd-b6d9-a241ee6accf1 | -12.89277 | -45.26941 | 2025-10-01 04:51:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 18129a55-dc0b-31cf-a368-5ac1c0d4107d | -9.40909 | -63.69313 | 2025-10-01 04:51:00 | NPP-375D | ALTO PARAÍSO | RONDÔNIA | Brasil | 1100403 | 11 | 33 | nan | nan | nan | Amazônia | 2.0 |
| cabe1b36-bde4-318b-8e90-f89ad89810e3 | -12.21278 | -47.81001 | 2025-10-01 04:51:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 15430f88-7895-353c-915e-768acd9061af | -10.6486 | -48.52532 | 2025-10-01 04:51:00 | NPP-375D | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 9fcee28a-604c-305e-a697-346e452dab0a | -14.18525 | -46.10822 | 2025-10-01 04:51:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 131ba7e7-dc25-301d-aec6-e4b880442b9c | -14.3931 | -46.22255 | 2025-10-01 04:51:00 | NPP-375D | BURITINÓPOLIS | GOIÁS | Brasil | 5203962 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| d050e1a3-08a9-3a83-a3c8-6d93bbcde6e6 | -15.24485 | -50.08586 | 2025-10-01 04:51:00 | NPP-375D | ARAGUAPAZ | GOIÁS | Brasil | 5202155 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| b019801e-3acb-3f1f-bf7c-c68a6572502f | -15.26832 | -49.2895 | 2025-10-01 04:51:00 | NPP-375D | GOIANÉSIA | GOIÁS | Brasil | 5208608 | 52 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 36edcfcc-1ea8-367c-abbd-8a5e29513a5a | -14.14677 | -49.2011 | 2025-10-01 04:51:00 | NPP-375D | NOVA IGUAÇU DE GOIÁS | GOIÁS | Brasil | 5214879 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 3b1ca650-0142-322c-b312-34c46d7528b3 | -13.79962 | -51.2275 | 2025-10-01 04:51:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 93fba251-db19-35d8-9508-0f3aeece0c7f | -13.91841 | -48.09957 | 2025-10-01 04:51:00 | NPP-375D | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 60dc68e1-c2c7-3b02-ac51-30442bfa2149 | -11.09671 | -40.9573 | 2025-10-01 04:51:00 | NPP-375D | VÁRZEA NOVA | BAHIA | Brasil | 2933158 | 29 | 33 | nan | nan | nan | Caatinga | 1.1 |
| eee5cd6c-bcb0-3103-a9fa-ad7203d50086 | -10.21356 | -43.0409 | 2025-10-01 04:51:00 | NPP-375D | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 1623e208-7a6d-3cb2-b4af-008467cb7a81 | -15.47507 | -45.87074 | 2025-10-01 04:51:00 | NPP-375D | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 5f05d92b-b3b2-3245-87dc-8dbc23d6900b | -15.26014 | -49.26562 | 2025-10-01 04:51:00 | NPP-375D | GOIANÉSIA | GOIÁS | Brasil | 5208608 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 603a8758-ad27-3649-a57c-9c383e6bceb6 | -12.90445 | -54.75282 | 2025-10-01 04:51:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| ff7770d5-f6f6-3b27-ad77-da397d521785 | -12.7939 | -46.91502 | 2025-10-01 04:51:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| f6196815-14a4-39c0-8940-d57c49eb15ee | -11.18746 | -47.20169 | 2025-10-01 04:51:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 337ddb5d-00f9-3e52-b356-1c7f7dc97645 | -15.27858 | -47.83189 | 2025-10-01 04:51:00 | NPP-375D | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 1a0824d1-e5b7-3393-975e-3f08419d0b72 | -8.80406 | -48.78187 | 2025-10-01 04:51:00 | NPP-375D | COLMÉIA | TOCANTINS | Brasil | 1716703 | 17 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 82eef6fb-f092-33e4-a5e7-0699efb769bb | -11.83397 | -44.97959 | 2025-10-01 04:51:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 20649c02-f57f-3981-a6d6-8e457d871081 | -14.49679 | -48.44159 | 2025-10-01 04:51:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 44a99350-c793-326d-b689-fe4ac55323f2 | -11.46995 | -45.09538 | 2025-10-01 04:51:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 17973e4e-e6ff-379e-96f8-9167d75e8791 | -13.38079 | -48.08215 | 2025-10-01 04:51:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| b5becb45-0d77-3d63-9167-3fb2feb3c7e8 | -16.01269 | -50.87923 | 2025-10-01 04:51:00 | NPP-375D | JUSSARA | GOIÁS | Brasil | 5212204 | 52 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 59877f13-a6d2-32bf-9e82-5f4d1ec2ff01 | -14.70691 | -48.12757 | 2025-10-01 04:51:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 251b2bea-7b02-3e37-9caf-e82f5953327a | -14.54809 | -48.24777 | 2025-10-01 04:51:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| bb7c6fbc-8304-36e7-a232-7be9b2868906 | -14.02201 | -46.32431 | 2025-10-01 04:51:00 | NPP-375D | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| ec8186d7-526b-3aad-8cea-9177e607b619 | -8.22009 | -55.19969 | 2025-10-01 04:51:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 81e96f8d-dc11-3c78-a048-3d1a49fd2d52 | -12.22233 | -43.75349 | 2025-10-01 04:51:00 | NPP-375D | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 3f1b94e8-cef5-3ddb-b4db-ee12ab60eed9 | -8.21635 | -55.19906 | 2025-10-01 04:51:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| ce1f7165-b1ee-377c-adc5-5b401c705753 | -8.85122 | -48.41607 | 2025-10-01 04:51:00 | NPP-375D | GUARAÍ | TOCANTINS | Brasil | 1709302 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| ab832ffc-0bff-3db6-8606-77d87edf4027 | -16.49894 | -43.73201 | 2025-10-01 04:51:00 | NPP-375D | FRANCISCO SÁ | MINAS GERAIS | Brasil | 3126703 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| b5fe7e74-e3a1-30d7-943a-ee3d3f7ce7d3 | -11.46036 | -45.02372 | 2025-10-01 04:51:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 1ddff2b3-3a81-3599-8d2f-e48faffa2463 | -11.47265 | -45.11077 | 2025-10-01 04:51:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| ff386c12-60c1-34b1-b438-75ac229ec4de | -12.24658 | -47.79811 | 2025-10-01 04:51:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 5.8 |
| ad0ce2f6-af3c-3988-ae2d-8163bba76c11 | -13.76321 | -47.92981 | 2025-10-01 04:51:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 3e85b955-08cd-3c3a-b464-8c6c8593fb1c | -13.7836 | -47.98779 | 2025-10-01 04:51:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 1d11c655-b28e-392c-8be7-40a72b654a73 | -15.17113 | -52.81223 | 2025-10-01 04:51:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| ad09414c-86cf-3862-8921-f023f48f6262 | -9.93035 | -43.66816 | 2025-10-01 04:51:00 | NPP-375D | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 802baa78-bfd9-3b5d-ba73-1dc17dd5ece9 | -11.68144 | -44.28846 | 2025-10-01 04:51:00 | NPP-375D | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 0fb51db7-e9d9-3a61-af58-ac165809070b | -11.46954 | -44.98992 | 2025-10-01 04:51:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| ed32f3ec-216a-3c17-83c7-aa4fde1217ae | -9.43191 | -54.71372 | 2025-10-01 04:51:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| d3668aae-ee82-3780-b380-cb6f9cbd6bd2 | -14.90398 | -48.37587 | 2025-10-01 04:51:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| f750fcbf-7f32-30b2-8dd8-082aca9b683f | -12.42097 | -44.09624 | 2025-10-01 04:51:00 | NPP-375D | TABOCAS DO BREJO VELHO | BAHIA | Brasil | 2930907 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 62d69420-4b75-306e-a4b1-1f170a411c03 | -14.50527 | -48.43784 | 2025-10-01 04:51:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 5a4a793a-3493-33c8-9a27-514c4d06f062 | -13.0804 | -47.07459 | 2025-10-01 04:51:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 7bef98cf-9e15-32fc-b2ce-edf1a18321f5 | -10.10845 | -50.31551 | 2025-10-01 04:51:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| cd12646a-99d5-355c-9c4b-f4ac589d7fdd | -12.23098 | -47.82279 | 2025-10-01 04:51:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 50ba5b90-7534-3012-aac5-a6c5fbfdc308 | -10.83837 | -46.65719 | 2025-10-01 04:51:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 14200c05-0cfc-3379-a12c-ab5e118a5d9d | -10.66338 | -48.52751 | 2025-10-01 04:51:00 | NPP-375D | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 5b35891a-ec2d-376c-97e9-337af1e210d7 | -10.62255 | -48.60149 | 2025-10-01 04:51:00 | NPP-375D | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 7ab8b9b2-b05d-3d5e-8264-a799647f9f5c | -14.18482 | -46.11906 | 2025-10-01 04:51:00 | NPP-375D | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 3.3 |
| e3847979-8e78-3620-8abc-0075af754279 | -13.66502 | -48.04137 | 2025-10-01 04:51:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| cea33e56-12c3-36cf-a539-dcdd0c97cd2e | -14.79889 | -48.3272 | 2025-10-01 04:51:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 6.8 |
| e11e18bf-7e53-3bb2-8136-d032ec5b3a47 | -10.82778 | -45.37662 | 2025-10-01 04:51:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 13.6 |
| 193d9eb3-107a-3c4f-a498-2ae2bd879328 | -11.14516 | -54.30811 | 2025-10-01 04:51:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| da2a591d-9219-3a90-99e6-67357464afaa | -11.79646 | -46.61502 | 2025-10-01 04:51:00 | NPP-375D | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 7f073b4d-9734-3d20-894d-7afc7b20fdd9 | -15.61464 | -47.85168 | 2025-10-01 04:51:00 | NPP-375D | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 0.9 |
| d88366f3-7ce0-331b-9fad-3867a399ef5a | -15.38494 | -49.19701 | 2025-10-01 04:51:00 | NPP-375D | GOIANÉSIA | GOIÁS | Brasil | 5208608 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 80a162ff-e823-3e45-b7b7-413a9dd19439 | -12.04296 | -47.90958 | 2025-10-01 04:51:00 | NPP-375D | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| e3c26f77-d713-3bb7-b154-0d58c2c9e3c4 | -12.87318 | -46.77317 | 2025-10-01 04:51:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| f453d3cc-6656-3d5a-979e-b2dbe6c365ac | -13.13985 | -47.42073 | 2025-10-01 04:51:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 2315cdf0-8036-38b9-98c5-88e7d87ba030 | -12.15823 | -47.76996 | 2025-10-01 04:51:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| a3e80685-2546-3de7-866c-5435355bb968 | -11.45571 | -44.96974 | 2025-10-01 04:51:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| aec6cb5d-1592-32ba-a633-82fa77f19659 | -14.57663 | -46.36485 | 2025-10-01 04:51:00 | NPP-375D | SÍTIO D'ABADIA | GOIÁS | Brasil | 5220702 | 52 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 5a82d060-267c-35c4-8614-316be9196da7 | -15.26204 | -49.27791 | 2025-10-01 04:51:00 | NPP-375D | GOIANÉSIA | GOIÁS | Brasil | 5208608 | 52 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 29edd8a8-daa3-380e-a7a7-2e35127ef1d9 | -15.39037 | -49.18585 | 2025-10-01 04:51:00 | NPP-375D | GOIANÉSIA | GOIÁS | Brasil | 5208608 | 52 | 33 | nan | nan | nan | Cerrado | 5.0 |
| d55861f4-e4f9-34a5-8f21-4ef3780c7f67 | -11.05063 | -47.82423 | 2025-10-01 04:51:00 | NPP-375D | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 459766bb-918b-376f-9ccc-d9073b3c705d | -14.68225 | -48.24959 | 2025-10-01 04:51:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| e9e5e4e7-b52a-3a80-b360-39abcb070790 | -13.7786 | -47.96544 | 2025-10-01 04:51:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 7.7 |
| 555ee447-669d-3dd8-b8a8-bccd06a7117a | -13.46082 | -44.37694 | 2025-10-01 04:51:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| ed1fbd96-30ad-3de0-b38c-5fb903cb8ca2 | -10.97984 | -46.53279 | 2025-10-01 04:51:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 4cb422d7-23e7-3066-b34f-9365cfe57110 | -10.9118 | -46.56204 | 2025-10-01 04:51:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| c906bce6-36f2-3fb5-98a4-448d59a6cb44 | -13.70922 | -48.62949 | 2025-10-01 04:51:00 | NPP-375D | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 5e46bf99-2d66-332f-ae20-302be9fd45a5 | -10.9243 | -46.50143 | 2025-10-01 04:51:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 4.7 |
| cb71547c-3009-3f5f-9c99-ff1f8dea0762 | -8.97542 | -50.27029 | 2025-10-01 04:51:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 29691a79-9254-3f60-a267-e216cf25963d | -10.90494 | -46.54672 | 2025-10-01 04:51:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 62d956fe-b3cc-3951-9b23-28f0b1195693 | -11.12109 | -49.78777 | 2025-10-01 04:51:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 0a029d41-6d6a-35b7-a08b-5e2f3f1e648a | -11.15194 | -54.12551 | 2025-10-01 04:51:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 7cff8c28-1d36-33b6-bb4f-ce4301f0da70 | -11.94664 | -47.88805 | 2025-10-01 04:51:00 | NPP-375D | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 47ed1bfc-0baa-37df-9b82-cddc00a50209 | -14.99191 | -46.95092 | 2025-10-01 04:51:00 | NPP-375D | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| fd9696bf-20e8-3043-a1b0-79a8ea0c834e | -14.68182 | -48.13293 | 2025-10-01 04:51:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 425d0db8-b91e-3d96-8aa9-b2060569c966 | -10.06978 | -50.27169 | 2025-10-01 04:51:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 3a8ade91-db02-325d-b2f3-48697717b8f0 | -9.39452 | -54.69472 | 2025-10-01 04:51:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 8c26c68f-dc8b-3904-a02b-ece729de4191 | -14.06523 | -44.36884 | 2025-10-01 04:51:00 | NPP-375D | FEIRA DA MATA | BAHIA | Brasil | 2910776 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 244f2725-3401-35ab-baa0-b742247f930b | -14.35068 | -45.90962 | 2025-10-01 04:51:00 | NPP-375D | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| c978c152-bb1f-3b8b-a7d5-3ba0f52efb32 | -14.67766 | -46.966 | 2025-10-01 04:51:00 | NPP-375D | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 43d18d93-ac0a-3036-b5d5-9a22aaceaf34 | -13.63628 | -47.64957 | 2025-10-01 04:51:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| cf18938a-6599-39ff-a7ea-0528446a22c0 | -13.37212 | -47.29557 | 2025-10-01 04:51:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |


[Clique aqui para ver as próximas entradas](README111.md)
