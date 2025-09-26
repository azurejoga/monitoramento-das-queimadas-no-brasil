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

## Dados Diários - Página 19

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| efb3ec75-27e2-3948-a63a-238a89604fdc | -13.86792 | -42.37621 | 2025-09-26 04:17:00 | NOAA-21 | CAETITÉ | BAHIA | Brasil | 2905206 | 29 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 664ebcf5-2f91-31d7-a258-7e4c0c5b39ea | -21.00349 | -50.01028 | 2025-09-26 04:17:00 | NOAA-21 | PLANALTO | SÃO PAULO | Brasil | 3539608 | 35 | 33 | nan | nan | nan | Mata Atlântica | 4.3 |
| 45973d27-885f-3e32-b3e4-d39693e3ba0a | -11.02231 | -44.64767 | 2025-09-26 04:17:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| c3fc7cad-f7ff-39ab-b12a-b878c8a1d351 | -13.53874 | -47.70821 | 2025-09-26 04:17:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 8b3f4b6e-484e-31b6-b665-47deb121d1e4 | -11.41107 | -44.92317 | 2025-09-26 04:17:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| b08dbd69-4f6f-3e72-ada8-8bdf1286659f | -15.14219 | -46.43386 | 2025-09-26 04:17:00 | NOAA-21 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| b76167c0-be43-3dde-9579-1585882ab986 | -13.94809 | -44.09976 | 2025-09-26 04:17:00 | NOAA-21 | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 78a1dca8-c29b-364e-8ee0-f964d629caf1 | -11.41874 | -44.96051 | 2025-09-26 04:17:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 6374997a-559f-3e9c-949b-a3df37549cb6 | -14.98616 | -50.05973 | 2025-09-26 04:17:00 | NOAA-21 | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 3.8 |
| ef87c5ac-3923-3287-bad0-61a5c137bdc5 | -15.6394 | -48.84421 | 2025-09-26 04:17:00 | NOAA-21 | PIRENÓPOLIS | GOIÁS | Brasil | 5217302 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 1899e48e-dc4e-3dcc-bd93-0063f2290f8e | -12.35871 | -51.21199 | 2025-09-26 04:17:00 | NOAA-21 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 8167b3eb-904d-3130-b8c1-1a04c4e03a1f | -15.73108 | -43.15709 | 2025-09-26 04:17:00 | NOAA-21 | PORTEIRINHA | MINAS GERAIS | Brasil | 3152204 | 31 | 33 | nan | nan | nan | Caatinga | 0.5 |
| a99461f1-e3f6-3806-9e72-f3362728e89d | -12.02403 | -43.63325 | 2025-09-26 04:17:00 | NOAA-21 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| e5c80515-2201-350d-8199-c158223ba9e0 | -11.2408 | -45.5624 | 2025-09-26 04:17:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 86.3 |
| 81d61243-c693-3c6e-b931-5dacf7225afd | -15.33714 | -47.99406 | 2025-09-26 04:17:00 | NOAA-21 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 0dfcf10b-56b1-32bc-a75a-9fbbf7a702cd | -11.42613 | -44.97968 | 2025-09-26 04:17:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 94284120-f7a0-3db9-8351-ca3c9d985937 | -13.15769 | -44.93915 | 2025-09-26 04:17:00 | NOAA-21 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| e073f6f4-e34c-3d28-90a9-f61a2d130318 | -10.62357 | -53.88741 | 2025-09-26 04:17:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| c5ec272f-1b30-3775-b769-8776818b2fca | -21.23076 | -49.04159 | 2025-09-26 04:17:00 | NOAA-21 | CATANDUVA | SÃO PAULO | Brasil | 3511102 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.3 |
| 8d97ad53-846e-3046-be08-ced9664e9847 | -14.57816 | -51.40516 | 2025-09-26 04:17:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 88303930-29b8-3044-9a0d-5b2592dc1169 | -12.05477 | -44.83412 | 2025-09-26 04:17:00 | NOAA-21 | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| b764be48-5262-3f70-9857-01bac9e6cf30 | -15.91927 | -57.49937 | 2025-09-26 04:17:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | 3.4 |
| d6a4949a-edaa-3040-aeb1-a16d433415fa | -11.61529 | -44.42882 | 2025-09-26 04:17:00 | NOAA-21 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 65287ff4-4bcb-3ea2-bfef-5288efd50152 | -18.58298 | -45.21832 | 2025-09-26 04:17:00 | NOAA-21 | TRÊS MARIAS | MINAS GERAIS | Brasil | 3169356 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 51e468bc-971e-3d01-aaa7-871a72490357 | -13.89129 | -43.91421 | 2025-09-26 04:17:00 | NOAA-21 | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| ffa20a32-77b3-3cbd-b3a2-cc2f81ef5734 | -13.27243 | -51.90371 | 2025-09-26 04:17:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 998b3500-da05-357a-8c77-67c0e00c271b | -15.90906 | -59.33885 | 2025-09-26 04:17:00 | NOAA-21 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 067f9d4c-81d5-3e79-a16c-0fc131a542c3 | -11.0727 | -48.36315 | 2025-09-26 04:17:00 | NOAA-21 | IPUEIRAS | TOCANTINS | Brasil | 1709807 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| cf252e48-6244-3318-b651-3d466252bafc | -11.68018 | -44.42491 | 2025-09-26 04:17:00 | NOAA-21 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 5.2 |
| a0adc271-e37c-34cf-a608-7275a3587edc | -15.38453 | -46.11406 | 2025-09-26 04:17:00 | NOAA-21 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| cca43bcc-6c36-3cd4-ba3e-e7bc4aa956f3 | -13.33122 | -47.30239 | 2025-09-26 04:17:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 9014ee53-f921-3d38-9dc2-de0cdbccdb65 | -11.41825 | -44.92068 | 2025-09-26 04:17:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 6128367d-c7b4-37f3-8496-96f5427893f5 | -11.78787 | -44.90913 | 2025-09-26 04:17:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| c93a2a99-405a-3e8b-b139-76b8f9ec68b4 | -11.40329 | -44.97232 | 2025-09-26 04:17:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 8a20b33a-7b39-318f-a3db-4b61a58203d9 | -22.13496 | -50.01812 | 2025-09-26 04:17:00 | NOAA-21 | MARÍLIA | SÃO PAULO | Brasil | 3529005 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 693ecda9-d2f5-3249-9ae7-decbee7a72a4 | -11.66865 | -44.45533 | 2025-09-26 04:17:00 | NOAA-21 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 0e8585bf-bd4f-378d-9fda-aaa4c762430d | -11.14079 | -46.34811 | 2025-09-26 04:17:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 4e8d82b2-4591-3318-88a5-0bb162245e8b | -11.70274 | -44.45365 | 2025-09-26 04:17:00 | NOAA-21 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 4.4 |
| b05fb571-d651-3756-854a-179e818a051b | -17.02796 | -52.23715 | 2025-09-26 04:17:00 | NOAA-21 | CAIAPÔNIA | GOIÁS | Brasil | 5204409 | 52 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 77b82ef3-8bb0-3369-a908-744c53827cf9 | -12.35181 | -44.35022 | 2025-09-26 04:17:00 | NOAA-21 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| bcf9c45f-dd38-3bfe-9c1e-b8f8639023e8 | -11.02286 | -44.64418 | 2025-09-26 04:17:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| f8857927-2fe6-3d27-a3df-0d591b765549 | -13.85106 | -45.61336 | 2025-09-26 04:17:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 3.3 |
| c6a03784-a290-3d51-8ab4-8186711770a3 | -20.56426 | -57.08147 | 2025-09-26 04:17:00 | NOAA-21 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 7dee6bd6-357f-3d30-9eb8-343c7a458a13 | -11.42943 | -44.98024 | 2025-09-26 04:17:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 00f45dff-e17d-3a7d-91d5-09749fb2a207 | -12.73649 | -47.07474 | 2025-09-26 04:17:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 47e62427-cf1c-3801-b023-8c34776e41cb | -11.97404 | -46.62658 | 2025-09-26 04:17:00 | NOAA-21 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 7.5 |
| 9a323564-0608-3947-b0ac-33ec6ed7cf88 | -15.02477 | -46.93835 | 2025-09-26 04:17:00 | NOAA-21 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 647b25f7-0a01-371d-902c-6d9d3d773876 | -12.87556 | -44.69836 | 2025-09-26 04:17:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 6694624d-d445-3b53-b9f1-97f809e35ea9 | -11.04732 | -45.88134 | 2025-09-26 04:17:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 474f49ad-00b8-3e49-90fc-df03015736c6 | -13.84993 | -45.62048 | 2025-09-26 04:17:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 6559c726-bd2f-3ff9-8cf9-91e56ece7961 | -11.6824 | -44.45396 | 2025-09-26 04:17:00 | NOAA-21 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 49125596-53b5-3613-8b27-b93ca478efec | -20.55491 | -57.14989 | 2025-09-26 04:17:00 | NOAA-21 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 48970f1f-4631-3ec2-811c-a3300355671e | -11.43111 | -44.96972 | 2025-09-26 04:17:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 503646bb-108d-334e-8423-795eefa71ea4 | -9.51236 | -54.66108 | 2025-09-26 04:17:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 38259e0b-a0b9-3852-9feb-b393b375e518 | -20.99331 | -50.46741 | 2025-09-26 04:17:00 | NOAA-21 | SANTO ANTÔNIO DO ARACANGUÁ | SÃO PAULO | Brasil | 3548054 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| e50bac4e-5f1e-35ca-8441-1037de63c521 | -11.24705 | -45.54496 | 2025-09-26 04:17:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 19.9 |
| 188cb6da-426e-3134-88d1-fa401205effc | -11.61087 | -44.4312 | 2025-09-26 04:17:00 | NOAA-21 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 889c7884-5bd0-3da2-9c74-c58db5f72f3e | -13.28442 | -50.69958 | 2025-09-26 04:17:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| de2abfaf-4566-3ab1-a1ea-5d3217d3b645 | -13.84661 | -45.61992 | 2025-09-26 04:17:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 9aa88a90-a9fc-3aec-8aad-e0e7cb8cf04e | -20.99631 | -50.0088 | 2025-09-26 04:17:00 | NOAA-21 | PLANALTO | SÃO PAULO | Brasil | 3539608 | 35 | 33 | nan | nan | nan | Mata Atlântica | 4.8 |
| 1ecc7bcc-22ff-3084-8352-b42ef55a6784 | -20.75273 | -57.89169 | 2025-09-26 04:17:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 12.5 |
| a5b2b323-1b2a-35f6-b7c4-e304175b0745 | -15.26623 | -51.47408 | 2025-09-26 04:17:00 | NOAA-21 | JUSSARA | GOIÁS | Brasil | 5212204 | 52 | 33 | nan | nan | nan | Cerrado | 8.5 |
| 0964f92d-e187-30da-bb1a-7f9a99ebebcf | -11.22232 | -45.57047 | 2025-09-26 04:17:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 6a8020d1-02db-3503-b532-8a32fdf4bb20 | -12.62173 | -48.12941 | 2025-09-26 04:17:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 98266ae1-4258-318b-961b-0bff959de135 | -12.55747 | -45.84671 | 2025-09-26 04:17:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 0356bd53-5b4f-386b-a59a-e10eff4e253c | -13.84605 | -45.62348 | 2025-09-26 04:17:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 82752639-bcf5-3b2d-a906-a85f963b24a0 | -12.74062 | -47.0714 | 2025-09-26 04:17:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 71f311df-410e-3c2a-8503-7c31632952b0 | -14.94877 | -47.49763 | 2025-09-26 04:17:00 | NOAA-21 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 5d329287-0afb-3e4d-8863-c6743083d692 | -11.62024 | -44.44037 | 2025-09-26 04:17:00 | NOAA-21 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 71c50dfe-448f-3f9c-8d69-458d7c74be45 | -13.89074 | -43.91781 | 2025-09-26 04:17:00 | NOAA-21 | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 4dbb7926-91b0-3bfc-bfd5-f2ba000dcf4a | -21.00754 | -50.02961 | 2025-09-26 04:17:00 | NOAA-21 | PLANALTO | SÃO PAULO | Brasil | 3539608 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| bbe8b86f-7e80-33de-9a4b-f7e4054b2089 | -20.9999 | -50.00954 | 2025-09-26 04:17:00 | NOAA-21 | PLANALTO | SÃO PAULO | Brasil | 3539608 | 35 | 33 | nan | nan | nan | Mata Atlântica | 4.8 |
| e6eb49a2-23e1-39fc-9919-04469f4106f1 | -11.00521 | -44.3477 | 2025-09-26 04:17:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| dba95b42-d89a-3e90-bd63-c305c1cd0f5d | -12.75792 | -42.98413 | 2025-09-26 04:17:00 | NOAA-21 | PARATINGA | BAHIA | Brasil | 2923704 | 29 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 85c57bfa-21eb-38ce-b8f9-3e1aa73f0950 | -17.03057 | -52.2441 | 2025-09-26 04:17:00 | NOAA-21 | CAIAPÔNIA | GOIÁS | Brasil | 5204409 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| a5e3155b-4769-3a22-b709-2c247d622bba | -10.62287 | -53.891 | 2025-09-26 04:17:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 5afff002-9884-3c6a-8ba9-26ad51d1d885 | -21.14653 | -46.82669 | 2025-09-26 04:17:00 | NOAA-21 | MONTE SANTO DE MINAS | MINAS GERAIS | Brasil | 3143203 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| aa14e28e-f6bd-3e76-8cd3-65c6c3ab7c74 | -15.27364 | -46.42245 | 2025-09-26 04:17:00 | NOAA-21 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 10f933f9-09ad-3490-b14a-7d5bea45bf16 | -20.61144 | -56.7388 | 2025-09-26 04:17:00 | NOAA-21 | BODOQUENA | MATO GROSSO DO SUL | Brasil | 5002159 | 50 | 33 | nan | nan | nan | Cerrado | 7.2 |
| 550b9b4e-1fa1-37ef-be43-098cc955e349 | -11.6857 | -44.45449 | 2025-09-26 04:17:00 | NOAA-21 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 766e43c5-0d64-3a73-8aa4-a5cf8c79d4a5 | -11.19722 | -46.30362 | 2025-09-26 04:17:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| b2392557-ae3d-374e-9281-ec68c04c135e | -15.40476 | -47.06166 | 2025-09-26 04:17:00 | NOAA-21 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| b346869a-8629-35f3-8e62-7a9867f8fb4d | -12.98311 | -43.20743 | 2025-09-26 04:17:00 | NOAA-21 | BOM JESUS DA LAPA | BAHIA | Brasil | 2903904 | 29 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 3ae14fa5-f872-3489-94e2-21056b90f4ef | -12.05147 | -44.83358 | 2025-09-26 04:17:00 | NOAA-21 | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 88815b58-31ff-3976-a777-fc50b76c3da4 | -13.31265 | -43.6753 | 2025-09-26 04:17:00 | NOAA-21 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 73a0a25f-a0bd-372a-91f1-fea8cfb8ff03 | -10.62253 | -53.88736 | 2025-09-26 04:17:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| ac8b1b7d-a2b2-31ec-9d21-34758cd45ab6 | -11.04395 | -45.88076 | 2025-09-26 04:17:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 669fade0-25bf-3137-b681-faf49e9d4417 | -11.65885 | -45.3558 | 2025-09-26 04:17:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 037e71d9-6542-38f5-bcc8-ae527ca79955 | -18.25117 | -45.01046 | 2025-09-26 04:17:00 | NOAA-21 | TRÊS MARIAS | MINAS GERAIS | Brasil | 3169356 | 31 | 33 | nan | nan | nan | Cerrado | 2.5 |
| d142d36e-3847-3b7c-8e46-95f4fc819b3a | -11.24923 | -45.5527 | 2025-09-26 04:17:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 33.4 |
| 5c61340b-d5ef-3d00-9c66-f1e001972c60 | -20.75371 | -57.88732 | 2025-09-26 04:17:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 12.5 |
| 1a4c7a73-828f-307c-a96f-353b7897fa7b | -21.03961 | -51.11348 | 2025-09-26 04:17:00 | NOAA-21 | MIRANDÓPOLIS | SÃO PAULO | Brasil | 3530102 | 35 | 33 | nan | nan | nan | Mata Atlântica | 10.3 |
| 598d7570-ad5b-3b91-9bd6-83255c5e67f3 | -11.0151 | -44.34929 | 2025-09-26 04:17:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 1148eaf2-06a7-3e4f-a22d-6e5fa6c7b741 | -15.90843 | -57.48958 | 2025-09-26 04:17:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 9939210a-2850-3427-8daa-5d382edfb2a2 | -13.84501 | -45.6087 | 2025-09-26 04:17:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 41749f01-0859-3d87-8034-cac0ca89e553 | -15.1966 | -50.21776 | 2025-09-26 04:17:00 | NOAA-21 | ARAGUAPAZ | GOIÁS | Brasil | 5202155 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 43e8fb49-04d8-35c3-9c32-43177378616f | -21.0425 | -51.1193 | 2025-09-26 04:17:00 | NOAA-21 | MIRANDÓPOLIS | SÃO PAULO | Brasil | 3530102 | 35 | 33 | nan | nan | nan | Mata Atlântica | 10.3 |
| 14feb0d5-9762-3c21-86c4-57757860998f | -15.11068 | -46.45855 | 2025-09-26 04:17:00 | NOAA-21 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 2.5 |
| e99fd1d8-84b5-315f-b2b2-cafc611a9c1f | -13.63507 | -48.09031 | 2025-09-26 04:17:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 64b6e9c4-a954-3a71-b998-fe69be08efaa | -20.55579 | -57.14595 | 2025-09-26 04:17:00 | NOAA-21 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 2.0 |


[Clique aqui para ver as próximas entradas](README20.md)
