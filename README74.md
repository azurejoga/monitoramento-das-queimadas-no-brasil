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

## Dados Diários - Página 74

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 3b5a47e1-21ee-3bb7-8bf3-305ede82629e | -14.57929 | -54.57201 | 2025-09-04 04:55:00 | NPP-375D | PLANALTO DA SERRA | MATO GROSSO | Brasil | 5106455 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| f842703a-1517-3962-bd0a-12ab2bb6254a | -15.30008 | -52.74905 | 2025-09-04 04:55:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 96d2b691-d1d8-380a-ae85-b2a14164b8ea | -14.81643 | -48.22239 | 2025-09-04 04:55:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 8ae48e94-c891-3f15-8014-4c3f40a2fcab | -14.56913 | -48.03811 | 2025-09-04 04:55:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 95bbc513-73fb-3e9e-8b51-07e3aa8523c4 | -10.94933 | -50.99703 | 2025-09-04 04:55:00 | NPP-375D | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 11bf2358-4ec6-37a0-9886-e93de41f685f | -11.8772 | -51.53494 | 2025-09-04 04:55:00 | NPP-375D | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| b1d0eeee-45d8-315c-8752-26b80fdfbf95 | -14.28291 | -45.22507 | 2025-09-04 04:55:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 06dcbb4a-d0e5-3846-8c3a-503f4a997e36 | -11.61776 | -47.77203 | 2025-09-04 04:55:00 | NPP-375D | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| ade6c65a-11f5-3b67-9a2e-9de67bdcf74a | -12.18423 | -53.89238 | 2025-09-04 04:55:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| a8bec0b1-1c47-358a-b3ad-3661863aa364 | -9.80773 | -54.883 | 2025-09-04 04:55:00 | NPP-375D | GUARANTÃ DO NORTE | MATO GROSSO | Brasil | 5104104 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 44fecb3e-f96f-3411-a597-d9b17c0db781 | -10.47665 | -53.63028 | 2025-09-04 04:55:00 | NPP-375D | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 75bd9628-b0d8-34a4-b918-fe9e1e80e26f | -15.02361 | -48.10053 | 2025-09-04 04:55:00 | NPP-375D | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 4d06d646-dcad-3970-a27f-a359498106b5 | -12.18202 | -53.88477 | 2025-09-04 04:55:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 6ffeb768-72a8-3771-97d0-8b32dffd8e2c | -13.5664 | -48.12766 | 2025-09-04 04:55:00 | NPP-375D | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| e06de150-6444-34d4-ad57-454c929796e2 | -11.09897 | -52.02609 | 2025-09-04 04:55:00 | NPP-375D | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 70e8c856-53c1-3f71-9320-46a0f01d2f0e | -14.77888 | -48.16833 | 2025-09-04 04:55:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 2a0e4903-096d-3778-9d22-f0fe963ccd7b | -14.2878 | -45.22908 | 2025-09-04 04:55:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 860156de-195e-34b7-9ae0-83f5048f9011 | -14.39275 | -51.6695 | 2025-09-04 04:55:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| cc94586d-f605-3c93-8aa2-b3c8326d12ce | -11.68127 | -52.1861 | 2025-09-04 04:55:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| d5cb647b-4188-3a7e-bcd3-2093d7d1b3fa | -10.11112 | -54.798 | 2025-09-04 04:55:00 | NPP-375D | MATUPÁ | MATO GROSSO | Brasil | 5105606 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 394a0354-0acd-35ff-ad4e-fd7c40bcfbd4 | -15.30293 | -52.75344 | 2025-09-04 04:55:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 81b2250b-6835-36c4-9b54-b850e83b5b25 | -15.41 | -55.94536 | 2025-09-04 04:55:00 | NPP-375D | CUIABÁ | MATO GROSSO | Brasil | 5103403 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 1532b31c-a555-3730-b7d8-0a934d4ff645 | -15.01201 | -50.03282 | 2025-09-04 04:55:00 | NPP-375D | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 8eda5b4b-4f9e-38f5-ba0e-5709e54f71e4 | -14.59975 | -54.59376 | 2025-09-04 04:55:00 | NPP-375D | PLANALTO DA SERRA | MATO GROSSO | Brasil | 5106455 | 51 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 63980f5a-e8be-3b9a-9c77-5c592f1b33b6 | -11.63592 | -52.18657 | 2025-09-04 04:55:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 312e68ed-4006-3f0c-8a8f-5053a3a8206f | -11.628 | -46.65004 | 2025-09-04 04:55:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| e3fb816a-8e74-3111-8996-c5cbfd340409 | -10.61327 | -55.40329 | 2025-09-04 04:55:00 | NPP-375D | COLÍDER | MATO GROSSO | Brasil | 5103205 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| ae20b63e-b4e3-36f4-9357-2f7517890e4b | -12.97031 | -54.77121 | 2025-09-04 04:55:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| cc895006-aa21-3917-8f33-080a789b59ef | -10.48384 | -53.64944 | 2025-09-04 04:55:00 | NPP-375D | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| fcf138d4-5456-3ec4-bf5b-7c68f7b7b85b | -12.92091 | -57.00279 | 2025-09-04 04:55:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 7f4c62a2-9beb-379a-a7ce-6027efd0f050 | -11.58943 | -47.75526 | 2025-09-04 04:55:00 | NPP-375D | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| f9ac3b5f-f563-36a4-9f06-0d55bab525e0 | -10.06373 | -54.79013 | 2025-09-04 04:55:00 | NPP-375D | MATUPÁ | MATO GROSSO | Brasil | 5105606 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| e10c4f04-066f-3f41-85fe-c6bacfca8bb1 | -17.04149 | -47.14631 | 2025-09-04 04:55:00 | NPP-375D | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 5.6 |
| ad9c9f45-3ef9-32ae-a46a-b93bb8b10ee3 | -15.55345 | -48.41882 | 2025-09-04 04:55:00 | NPP-375D | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 31643f57-f845-3a23-87f8-a29f06252535 | -8.70327 | -62.39508 | 2025-09-04 04:55:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 1e3a5325-55a4-3028-9ebe-c8659a098b18 | -11.73853 | -47.7518 | 2025-09-04 04:55:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 2d478b7b-1322-3c5d-bdd6-80d5b3d9c1d9 | -11.65676 | -54.52927 | 2025-09-04 04:55:00 | NPP-375D | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 7b6bd911-cae7-3f60-9e02-c2a312f181f1 | -15.00422 | -50.03165 | 2025-09-04 04:55:00 | NPP-375D | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 5e31553e-b20f-3671-8669-6063a1a3de20 | -14.56737 | -48.05138 | 2025-09-04 04:55:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| da52c01c-ad9c-3daf-93bb-6684250a8e08 | -15.04939 | -50.07806 | 2025-09-04 04:55:00 | NPP-375D | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 0929bcf8-4a64-30e6-bee8-85a70c7f60c8 | -11.68129 | -52.20881 | 2025-09-04 04:55:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 55847a89-6994-32ae-ab25-65fe98005d70 | -14.55595 | -48.07002 | 2025-09-04 04:55:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.7 |
| a4f2d3d5-753f-32bd-88e9-2b588e94122b | -13.57498 | -48.12924 | 2025-09-04 04:55:00 | NPP-375D | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| bfa92ab9-471e-3239-934b-987d3f8b1f48 | -12.87263 | -48.01768 | 2025-09-04 04:55:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| b34c8d60-b6b2-3fa9-a488-2b0bace8cc1f | -11.09216 | -52.04773 | 2025-09-04 04:55:00 | NPP-375D | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| d4d81ae9-d527-3323-8582-9e5241aaac03 | -16.31671 | -52.96122 | 2025-09-04 04:55:00 | NPP-375D | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 50468504-a4ad-3fd6-bd08-cc1de2bc5206 | -16.31614 | -52.965 | 2025-09-04 04:55:00 | NPP-375D | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 0496a857-26e3-374a-9fd8-4a06c957004d | -10.45996 | -54.7758 | 2025-09-04 04:55:00 | NPP-375D | TERRA NOVA DO NORTE | MATO GROSSO | Brasil | 5108055 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| a7e6d9c9-2f0c-33f0-b901-fa032a9ad1bd | -12.18034 | -53.89537 | 2025-09-04 04:55:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 493c5f52-66d2-3891-be7f-3205559d161f | -11.67253 | -57.34697 | 2025-09-04 04:55:00 | NPP-375D | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 20.7 |
| 43016a72-4b0b-3824-8a59-ea96592592d5 | -13.45498 | -46.82943 | 2025-09-04 04:55:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 06a1a772-033a-3756-821e-0780b6d3e8d9 | -13.75066 | -46.94292 | 2025-09-04 04:55:00 | NPP-375D | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| af29c7ec-3501-3125-bad1-129afadbe965 | -14.53351 | -48.07074 | 2025-09-04 04:55:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 784ac350-0796-377b-83f1-7a9baa13fee8 | -11.19964 | -55.02349 | 2025-09-04 04:55:00 | NPP-375D | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| fe652417-35d1-3689-8a1b-153886092687 | -16.31384 | -52.95687 | 2025-09-04 04:55:00 | NPP-375D | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| b718cde1-fd50-3d11-a9e8-fd10c2187a89 | -15.54636 | -48.40508 | 2025-09-04 04:55:00 | NPP-375D | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| b44ed143-c65a-3aa0-a3da-3d2ea6fd5abf | -14.57822 | -54.55718 | 2025-09-04 04:55:00 | NPP-375D | PLANALTO DA SERRA | MATO GROSSO | Brasil | 5106455 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 1b6ce2d1-c2e5-30e0-b036-0dfefb685e37 | -15.59881 | -52.89547 | 2025-09-04 04:55:00 | NPP-375D | GENERAL CARNEIRO | MATO GROSSO | Brasil | 5103908 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| e0bf6357-6ed5-304e-a13d-183f0b481879 | -9.50054 | -57.81663 | 2025-09-04 04:55:00 | NPP-375D | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 84d5070c-fb84-371f-9ffe-488d2e3cdae4 | -11.10408 | -52.03824 | 2025-09-04 04:55:00 | NPP-375D | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 9adfa180-4b4f-3f85-9307-8347183326e2 | -10.09774 | -54.7733 | 2025-09-04 04:55:00 | NPP-375D | MATUPÁ | MATO GROSSO | Brasil | 5105606 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 4b88d5b6-72a4-352b-8b13-77123da33346 | -11.86443 | -51.50097 | 2025-09-04 04:55:00 | NPP-375D | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 4bb93989-bde9-3f59-ad6f-1952b5c4499b | -11.65399 | -54.52515 | 2025-09-04 04:55:00 | NPP-375D | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 4e289efd-bdd8-39c8-a18c-34ba42317059 | -11.65122 | -54.52103 | 2025-09-04 04:55:00 | NPP-375D | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 6.6 |
| 857c37ad-2e93-349e-9cfb-e92397e9017d | -11.79519 | -51.52607 | 2025-09-04 04:55:00 | NPP-375D | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 4cfd4c43-6c49-3e7b-a8af-88b9172a8568 | -15.46641 | -53.01018 | 2025-09-04 04:55:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| afbf9a5c-8f08-3008-b467-63710fe5c509 | -11.63933 | -52.1871 | 2025-09-04 04:55:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 9f88b7e9-6503-34fe-8f82-d491c3a46507 | -11.73187 | -47.75274 | 2025-09-04 04:55:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 8be7b018-a5a4-334e-a8be-87b08fdc36c3 | -11.59337 | -52.1465 | 2025-09-04 04:55:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f46bdea2-330b-3971-adf8-98952bac51fc | -11.68071 | -52.1898 | 2025-09-04 04:55:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| b5855534-41bd-3334-bdc3-4dd75f6d9b0f | -11.61948 | -52.18082 | 2025-09-04 04:55:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 866a2a86-4f97-30c1-89e7-b330c861bf93 | -10.46999 | -53.6292 | 2025-09-04 04:55:00 | NPP-375D | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 14b9a279-01ad-3eda-8852-b62d721694cf | -11.53246 | -54.41384 | 2025-09-04 04:55:00 | NPP-375D | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b15ebf1f-11d9-3452-9fae-aa5742077f1c | -11.58426 | -52.11477 | 2025-09-04 04:55:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 76689eca-ba47-36d8-8e50-1ed8c260113d | -11.20641 | -55.02462 | 2025-09-04 04:55:00 | NPP-375D | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| d9a0abf3-91da-3a30-aa41-dd09bd6f8acf | -12.90334 | -48.05036 | 2025-09-04 04:55:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| b0fff247-e0fa-39c5-93cb-41c39614895c | -14.57596 | -54.57146 | 2025-09-04 04:55:00 | NPP-375D | PLANALTO DA SERRA | MATO GROSSO | Brasil | 5106455 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 764b6abe-c784-3c0a-a821-f524c5e4c2df | -16.46033 | -49.5153 | 2025-09-04 04:55:00 | NPP-375D | CATURAÍ | GOIÁS | Brasil | 5205208 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| b71179f0-63f3-3be0-a17e-a8d72106d21f | -12.63883 | -57.00842 | 2025-09-04 04:55:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 8366fcc4-140f-3fbe-844b-03f94197f04a | -12.89253 | -48.03289 | 2025-09-04 04:55:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| fc6631b8-a57a-3342-b5f7-d2c658ed7cd5 | -15.04162 | -50.07692 | 2025-09-04 04:55:00 | NPP-375D | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| de1eb78d-26af-33b4-820e-c6b29facd359 | -10.85226 | -55.75079 | 2025-09-04 04:55:00 | NPP-375D | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| b8679dac-a0cb-3f53-9211-be7ac093a936 | -11.6206 | -52.19614 | 2025-09-04 04:55:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 91aed159-4011-3294-96d7-0969468a83c8 | -12.60722 | -56.99853 | 2025-09-04 04:55:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 10.5 |
| 89fdb181-6368-32b6-b976-b222d12d345c | -11.86028 | -51.43243 | 2025-09-04 04:55:00 | NPP-375D | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| ed92735d-c976-3494-bdfb-6955495d08d6 | -12.50248 | -48.07103 | 2025-09-04 04:55:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 4a7f6c3e-ef9c-3240-9c68-26323d633332 | -15.49256 | -56.04018 | 2025-09-04 04:55:00 | NPP-375D | CUIABÁ | MATO GROSSO | Brasil | 5103403 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 5c7c4776-fa3a-3036-9e09-8886ac0dfdad | -15.04762 | -50.03395 | 2025-09-04 04:55:00 | NPP-375D | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 25817496-f565-39b2-84ef-0a862895572d | -13.10615 | -57.11517 | 2025-09-04 04:55:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 0f034345-0296-337b-8350-43705ef68911 | -14.5705 | -54.54124 | 2025-09-04 04:55:00 | NPP-375D | PLANALTO DA SERRA | MATO GROSSO | Brasil | 5106455 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 4d49fd38-366e-38d1-a259-f2cd34c1e372 | -12.45819 | -48.07736 | 2025-09-04 04:55:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| c37737d8-70a0-3f0a-be59-1505b1c6d6c3 | -12.94164 | -56.9893 | 2025-09-04 04:55:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| b8303188-18cc-3dc3-a431-1ecd3e953f6d | -11.86555 | -51.46929 | 2025-09-04 04:55:00 | NPP-375D | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| a189d578-5e50-39af-b5d0-d73a1691104d | -15.20167 | -52.35435 | 2025-09-04 04:55:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 212f850c-0ebd-37a4-bedb-39304f066de0 | -16.31163 | -45.69483 | 2025-09-04 04:55:00 | NPP-375D | SÃO ROMÃO | MINAS GERAIS | Brasil | 3164209 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 19738e1f-9fbd-323d-a082-527542e57d3d | -11.03775 | -52.0391 | 2025-09-04 04:55:00 | NPP-375D | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 6be517c5-0dde-3eb4-b01e-48e5fe276d84 | -16.55177 | -55.10333 | 2025-09-04 04:55:00 | NPP-375D | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 1.9 |
| 9b480970-3e1f-3b56-9abd-a8570f36b548 | -11.8714 | -51.54995 | 2025-09-04 04:55:00 | NPP-375D | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 6f98b90b-fa7e-318a-b22c-3568e3a302e3 | -11.85565 | -51.43956 | 2025-09-04 04:55:00 | NPP-375D | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Cerrado | 2.8 |
| bab03f5d-f807-3273-a1bf-a095fd267df9 | -11.86377 | -51.433 | 2025-09-04 04:55:00 | NPP-375D | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |


[Clique aqui para ver as próximas entradas](README75.md)
