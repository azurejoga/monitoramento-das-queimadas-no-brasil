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

## Dados Diários - Página 167

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 8ff757b6-1bdd-354d-b54c-8437cc2e1d19 | -13.1924 | -51.2097 | 2024-10-01 13:16:20 | GOES-16 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 139.2 |
| 113d47d0-9387-3fe7-83ad-1a4430bdc43a | -13.218 | -48.5797 | 2024-10-01 13:16:20 | GOES-16 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 132.2 |
| bbb69504-d288-30f9-aaec-f749e2dee918 | -12.9169 | -62.6829 | 2024-10-01 13:16:20 | GOES-16 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 334.2 |
| 19c690be-3f13-3480-8ab5-47a760a9f8c2 | -13.2112 | -51.2287 | 2024-10-01 13:16:21 | GOES-16 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 86.6 |
| 61c9d1a9-9099-3fb4-b714-e73a5bcc42b9 | -13.6164 | -51.0913 | 2024-10-01 13:16:23 | GOES-16 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 77.4 |
| 797cb165-d31e-321f-85b5-fa9f938726be | -14.7735 | -48.0757 | 2024-10-01 13:16:29 | GOES-16 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 120.3 |
| 86d68775-18c6-38a2-aa5e-997dfdc44a55 | -14.754 | -48.0788 | 2024-10-01 13:16:29 | GOES-16 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 97.5 |
| 10fc4b6a-b707-3424-aaaf-5f1773943064 | -16.474 | -57.3553 | 2024-10-01 13:16:39 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 130.8 |
| b1bae66a-f9c9-35b8-9bc6-0d4f93ea3468 | -16.4536 | -57.4188 | 2024-10-01 13:16:39 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 327.8 |
| eab043b3-9a23-340d-9522-4e5db9f6e43a | -16.4743 | -57.3349 | 2024-10-01 13:16:39 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 101.4 |
| 98cf53ee-5cee-30f3-852e-39a3aa55d68b | -16.7728 | -55.7773 | 2024-10-01 13:16:40 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 137.4 |
| 61a8354f-adbb-338d-b29a-d828e69f975b | -16.613 | -55.9836 | 2024-10-01 13:16:40 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 58.7 |
| 2c1be450-0255-32fb-86df-4dd20aca49e2 | -16.6528 | -55.9373 | 2024-10-01 13:16:40 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 116.6 |
| 2345dfa2-b968-3fdd-9db7-9ab489327166 | -16.7528 | -55.8005 | 2024-10-01 13:16:40 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 93.0 |
| fedca08f-965c-3396-911c-7534f30e19b2 | -16.6263 | -55.1934 | 2024-10-01 13:16:40 | GOES-16 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 82.5 |
| 3b7786c2-f4a7-314b-9549-2f46e3190cb0 | -16.7724 | -55.798 | 2024-10-01 13:16:40 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 97.8 |
| 10519bba-c5a1-34ec-ad37-0631e1c14ecd | -16.6521 | -55.9787 | 2024-10-01 13:16:40 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 52.6 |
| f0dbcb92-7995-39ed-b306-814d25e93f93 | -16.6455 | -55.2117 | 2024-10-01 13:16:40 | GOES-16 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 69.9 |
| 82753aeb-3248-396e-b89e-0df064cc1ace | -16.6525 | -55.958 | 2024-10-01 13:16:40 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 183.2 |
| eacedd53-eaf8-3ae6-b7ac-5a5c60319ff4 | -16.6332 | -55.9397 | 2024-10-01 13:16:40 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 53.3 |
| 380f0d48-163c-34de-ad94-f3a9dfea39fa | -16.6329 | -55.9604 | 2024-10-01 13:16:40 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 68.0 |
| 508c6770-c2f6-3562-ab8a-6b59ffceea41 | -16.7532 | -55.7797 | 2024-10-01 13:16:40 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 134.8 |
| 5980c270-3de9-3868-9d3d-69681731ebc9 | -16.6259 | -55.2142 | 2024-10-01 13:16:40 | GOES-16 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 78.4 |
| 7b9fdafb-2887-393d-b441-81fd0e304c7a | -16.898 | -57.7153 | 2024-10-01 13:16:41 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 75.3 |
| af846907-573f-3a80-8b80-37f41a613a7c | -16.8591 | -57.6993 | 2024-10-01 13:16:41 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 64.9 |
| 3a8e6795-d846-345a-8561-147ecb6fb0bf | -16.8787 | -57.6971 | 2024-10-01 13:16:41 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 214.2 |
| 65bd3ab9-3771-3cc9-a131-572039bdb8e5 | -16.76 | -57.792 | 2024-10-01 13:16:41 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 104.1 |
| 5f276ade-a91e-3362-89dc-7d011dbc7233 | -16.942 | -56.1908 | 2024-10-01 13:16:41 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 67.7 |
| 12665b7d-e3e1-3d45-9e09-2ff1d4b963c0 | -16.8784 | -57.7175 | 2024-10-01 13:16:41 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 69.4 |
| 5abef897-d361-3f35-979f-b1fc1b4c9d53 | -16.8983 | -57.6949 | 2024-10-01 13:16:41 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 91.5 |
| 851e4d8d-01b2-3c56-96a6-8d020281a2a9 | -16.7796 | -57.7898 | 2024-10-01 13:16:41 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 63.9 |
| c4585cbc-77dd-3ac2-84e6-13afeefaab04 | -16.9689 | -49.7326 | 2024-10-01 13:16:41 | GOES-16 | VARJÃO | GOIÁS | Brasil | 5221908 | 52 | 33 | nan | nan | nan | Cerrado | 84.9 |
| cbeb8d05-5cb2-3494-84e7-5150db667f09 | -17.0442 | -58.3907 | 2024-10-01 13:16:42 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 125.0 |
| c941ec04-c512-3b07-ab4b-fe82794ee0ef | -17.1381 | -56.1869 | 2024-10-01 13:16:42 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 91.9 |
| 3a9ff178-38f2-310c-867e-db11ca69a21f | -17.0439 | -58.4111 | 2024-10-01 13:16:42 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 72.0 |
| 3d8be1e0-470d-33c3-a1a8-a94b1d73bbb4 | -17.0805 | -56.1114 | 2024-10-01 13:16:42 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 96.2 |
| 23f05e10-80f0-352a-ac89-f83806ee8ebc | -17.0802 | -56.1321 | 2024-10-01 13:16:42 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 64.2 |
| f610f77a-fbea-3f31-8985-fc8ab945e189 | -17.1377 | -56.2076 | 2024-10-01 13:16:42 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 101.5 |
| 58a4a218-b371-3370-a423-665baf8eb0e9 | -17.157 | -56.2259 | 2024-10-01 13:16:43 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 99.6 |
| 799d2468-e308-353c-a4c9-44291c665078 | -17.1767 | -56.2234 | 2024-10-01 13:16:43 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 163.9 |
| 84d4b1cf-536f-31b8-88eb-a4cd6902334c | -17.1584 | -56.1429 | 2024-10-01 13:16:43 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 65.9 |
| 862cd943-bf4e-3475-ad0f-8769c023032d | -17.197 | -57.3741 | 2024-10-01 13:16:43 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 78.1 |
| 87e37d33-de34-37ac-a352-11f2811221fa | -17.1964 | -56.2209 | 2024-10-01 13:16:43 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 108.4 |
| f83f68fe-e934-3a5e-a17d-b3dd6d445f56 | -17.2167 | -57.3718 | 2024-10-01 13:16:43 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 59.6 |
| 98039189-c97b-3b53-ad3f-6fffe292c047 | -17.1781 | -56.1404 | 2024-10-01 13:16:43 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 65.4 |
| 6f73f352-63fa-3d5c-9707-9ad9bf579c77 | -17.1967 | -57.3946 | 2024-10-01 13:16:43 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 58.8 |
| 56efce42-725e-344b-96fe-2cf39084b6b4 | -17.705 | -53.2046 | 2024-10-01 13:16:45 | GOES-16 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 82.6 |
| 5129274d-3ef7-33d8-8f39-82d8543e5ea3 | -18.6973 | -57.333 | 2024-10-01 13:16:51 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 120.8 |
| 77ad84a0-f086-3fda-941a-db6cbbcd39ef | -18.7176 | -57.3097 | 2024-10-01 13:16:51 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 91.9 |
| 706fcd17-4d3b-35e1-9464-962938b85d95 | -18.7172 | -57.3305 | 2024-10-01 13:16:51 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 63.1 |
| b3bdb123-1ee0-3835-a79f-72730571e8da | -18.9091 | -49.2129 | 2024-10-01 13:16:51 | GOES-16 | MONTE ALEGRE DE MINAS | MINAS GERAIS | Brasil | 3142809 | 31 | 33 | nan | nan | nan | Mata Atlântica | 92.9 |
| 35df264a-f8bf-33c7-8d89-77cfd10cd3f3 | -18.6977 | -57.3123 | 2024-10-01 13:16:51 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 151.4 |
| b9e2c312-f00a-35dc-8998-b2a1ca60bb10 | -19.7638 | -46.6286 | 2024-10-01 13:16:55 | GOES-16 | IBIÁ | MINAS GERAIS | Brasil | 3129509 | 31 | 33 | nan | nan | nan | Cerrado | 98.2 |
| 99f7189d-5a82-34dd-9be0-32cb5a96c835 | -19.9921 | -55.4728 | 2024-10-01 13:16:58 | GOES-16 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Cerrado | 66.5 |
| 462a75b1-4ad5-3ac5-87e4-b2f25594c806 | -20.629 | -51.4722 | 2024-10-01 13:17:00 | GOES-16 | ITAPURA | SÃO PAULO | Brasil | 3523008 | 35 | 33 | nan | nan | nan | Mata Atlântica | 114.0 |
| cfcb8116-3a28-3472-9e4a-ba9d0d759590 | -20.6494 | -51.4681 | 2024-10-01 13:17:00 | GOES-16 | ITAPURA | SÃO PAULO | Brasil | 3523008 | 35 | 33 | nan | nan | nan | Mata Atlântica | 130.9 |
| a6dc1fa3-1465-31fc-b3de-2f8525faa61e | -20.6284 | -51.4945 | 2024-10-01 13:17:00 | GOES-16 | ITAPURA | SÃO PAULO | Brasil | 3523008 | 35 | 33 | nan | nan | nan | Mata Atlântica | 62.9 |
| 58de50ae-b48d-3e92-a005-56a06a46f713 | -20.9359 | -49.1023 | 2024-10-01 13:17:02 | GOES-16 | TABAPUÃ | SÃO PAULO | Brasil | 3552601 | 35 | 33 | nan | nan | nan | Mata Atlântica | 241.6 |
| a93a7418-64b5-3008-8043-bd767433522d | -20.9153 | -49.1069 | 2024-10-01 13:17:02 | GOES-16 | TABAPUÃ | SÃO PAULO | Brasil | 3552601 | 35 | 33 | nan | nan | nan | Mata Atlântica | 128.9 |
| c1adecae-57e2-32cf-95c8-b059f83c9cdc | -22.3707 | -49.3244 | 2024-10-01 13:17:09 | GOES-16 | DUARTINA | SÃO PAULO | Brasil | 3514502 | 35 | 33 | nan | nan | nan | Mata Atlântica | 296.6 |
| 5f417d69-85bb-3c81-a96b-e52bb8a6e1c6 | -22.37 | -49.3477 | 2024-10-01 13:17:09 | GOES-16 | DUARTINA | SÃO PAULO | Brasil | 3514502 | 35 | 33 | nan | nan | nan | Mata Atlântica | 127.8 |
| 1c599083-ac9d-399e-bca1-88d07fd72cb0 | -22.3916 | -49.3194 | 2024-10-01 13:17:09 | GOES-16 | CABRÁLIA PAULISTA | SÃO PAULO | Brasil | 3508306 | 35 | 33 | nan | nan | nan | Mata Atlântica | 165.5 |
| de280b48-d277-366b-a3a4-f9d534810f34 | -22.3713 | -49.3011 | 2024-10-01 13:17:09 | GOES-16 | PIRATININGA | SÃO PAULO | Brasil | 3539400 | 35 | 33 | nan | nan | nan | Mata Atlântica | 281.5 |
| 4f286685-78e2-3aad-8402-b202971942a6 | -22.41 | -49.36 | 2024-10-01 14:03:15 | MSG-03 | DUARTINA | SÃO PAULO | Brasil | 3514502 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 82829704-05a4-3ee0-b9f8-667424a2f1e0 | -22.4 | -49.3 | 2024-10-01 14:03:15 | MSG-03 | CABRÁLIA PAULISTA | SÃO PAULO | Brasil | 3508306 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 92b821ad-acb6-35a1-a658-eb67905e71d0 | -22.37 | -49.34 | 2024-10-01 14:03:15 | MSG-03 | DUARTINA | SÃO PAULO | Brasil | 3514502 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 1ba1e350-3145-366a-98ca-705ce0048aa2 | -21.59 | -47.84 | 2024-10-01 14:03:21 | MSG-03 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| 77c81a5b-fc92-3ef0-ba2d-cac7d5a7dede | -21.59 | -47.79 | 2024-10-01 14:03:21 | MSG-03 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| a5cefab0-cb01-3e9a-900f-0765990c8c5c | -21.62 | -47.86 | 2024-10-01 14:03:21 | MSG-03 | SÃO CARLOS | SÃO PAULO | Brasil | 3548906 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| 0df8bbc8-5201-3769-9a8d-99ec59b3df07 | -21.62 | -47.81 | 2024-10-01 14:03:21 | MSG-03 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| 3a3c5ead-fbcf-3497-bf7e-5164ea85b206 | -21.37 | -51.02 | 2024-10-01 14:03:23 | MSG-03 | VALPARAÍSO | SÃO PAULO | Brasil | 3556305 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 28a024c3-ecaa-30c7-a4db-259220f16847 | -20.66 | -51.47 | 2024-10-01 14:03:26 | MSG-03 | ITAPURA | SÃO PAULO | Brasil | 3523008 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 2736c616-b48c-3988-9ec9-cb5e0b7131ef | -20.83 | -51.1 | 2024-10-01 14:03:26 | MSG-03 | PEREIRA BARRETO | SÃO PAULO | Brasil | 3537404 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 0f005860-6cfd-3f2b-8dde-66a7f945e5e7 | -15.31 | -46.74 | 2024-10-01 14:03:55 | MSG-03 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| e42982d2-43ac-3b27-adb9-c148573d5ef9 | -12.13 | -50.07 | 2024-10-01 14:04:16 | MSG-03 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 38128de0-a2e6-391d-955c-027445a9fab8 | -8.79 | -45.16 | 2024-10-01 14:04:35 | MSG-03 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 8b690bef-aedd-3fba-aa65-96e45965a34b | -8.49 | -40.43 | 2024-10-01 14:04:37 | MSG-03 | DORMENTES | PERNAMBUCO | Brasil | 2605152 | 26 | 33 | nan | nan | nan | Caatinga | nan |
| e0daa28b-29b7-35ee-9954-f5a97ea5eded | 2.1265 | -50.9204 | 2024-10-01 14:44:54 | GOES-16 | AMAPÁ | AMAPÁ | Brasil | 1600105 | 16 | 33 | nan | nan | nan | Amazônia | 64.1 |
| 709cfa07-0470-3987-9ede-46760ebf00d4 | -18.6977 | -57.3123 | 2024-10-01 14:46:51 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 150.9 |
| 0deeefbe-30f4-382a-bc2d-74f8dc692c10 | -19.6509 | -56.4738 | 2024-10-01 14:46:56 | GOES-16 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 75.5 |
| 25d064dd-d2c2-3c54-9e63-1cafb03735fa | -19.6706 | -56.492 | 2024-10-01 14:46:56 | GOES-16 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 50.6 |
| 39e495c2-ba14-3185-b937-dc4abec508c8 | -19.7109 | -56.4862 | 2024-10-01 14:46:56 | GOES-16 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 34.3 |
| b6260ad3-43ff-3338-9431-0b08d6934e75 | -19.6505 | -56.4948 | 2024-10-01 14:46:56 | GOES-16 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 47.9 |
| d8a898d2-098a-3bc1-a7d0-53566fdfa971 | -19.671 | -56.4709 | 2024-10-01 14:46:56 | GOES-16 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 57.7 |
| 8cae7d91-f6fb-349e-8ed8-86f7d32b63a9 | -19.9917 | -55.4941 | 2024-10-01 14:46:58 | GOES-16 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Cerrado | 64.6 |
| 2ed92521-f437-3314-99b2-f8b81e610c3b | -21.5461 | -50.7682 | 2024-10-01 14:47:05 | GOES-16 | PIACATU | SÃO PAULO | Brasil | 3537701 | 35 | 33 | nan | nan | nan | Mata Atlântica | 113.4 |
| c2f1b6e0-f566-3441-8e28-7ae8f24785e8 | -21.5878 | -47.8355 | 2024-10-01 14:47:05 | GOES-16 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 283.9 |
| 812358f9-fb4f-385b-a8f2-5477d6b8f6c5 | -21.5691 | -47.7696 | 2024-10-01 14:47:05 | GOES-16 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 198.7 |
| c8809445-d61e-3c72-9c36-883d7be18055 | -21.5668 | -50.7638 | 2024-10-01 14:47:05 | GOES-16 | RINÓPOLIS | SÃO PAULO | Brasil | 3543808 | 35 | 33 | nan | nan | nan | Mata Atlântica | 191.3 |
| 317663a6-4b5a-3525-99c0-f3b2e3d8eb44 | -21.5684 | -47.7933 | 2024-10-01 14:47:05 | GOES-16 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 603.7 |
| 9b0528d4-357d-3439-88cd-f4e2aec7b136 | -21.5892 | -47.7882 | 2024-10-01 14:47:05 | GOES-16 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 811.2 |
| 0bed6e77-1985-378c-81f1-e96b5f560bd0 | -21.5871 | -47.8591 | 2024-10-01 14:47:05 | GOES-16 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 293.2 |
| d9666046-0b9f-3293-b384-0d4713538e12 | -21.5677 | -47.8169 | 2024-10-01 14:47:05 | GOES-16 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 206.7 |
| 040b96bb-25e1-3159-bb68-4fcb3ea304d2 | -21.5885 | -47.8118 | 2024-10-01 14:47:05 | GOES-16 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 479.4 |
| 0ac49d63-9f52-326f-86bf-11dccf479337 | -21.5864 | -47.8827 | 2024-10-01 14:47:05 | GOES-16 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 176.0 |
| b642c946-6dbf-3402-a034-bd601f6691e1 | -22.372 | -49.2777 | 2024-10-01 14:47:09 | GOES-16 | PIRATININGA | SÃO PAULO | Brasil | 3539400 | 35 | 33 | nan | nan | nan | Mata Atlântica | 311.6 |
| 8ab9b31c-b2be-32e4-a206-59f55e3b00b1 | -22.7964 | -53.4848 | 2024-10-01 14:47:12 | GOES-16 | TAQUARUSSU | MATO GROSSO DO SUL | Brasil | 5007976 | 50 | 33 | nan | nan | nan | Mata Atlântica | 84.9 |


