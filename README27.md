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

## Dados Diários - Página 27

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| a93ed1ab-bac7-33d2-8d56-3840eaff187a | -11.44489 | -45.63142 | 2025-09-13 03:47:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 5ef05a3f-f20a-34d7-a643-416f75bf389a | -10.73432 | -50.50197 | 2025-09-13 03:47:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| d06dc0af-44b0-3719-b02c-1dd077d1e9ae | -13.92412 | -48.22648 | 2025-09-13 03:47:00 | NPP-375D | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 9f44e333-86d8-3d7c-9547-81822483566b | -11.86071 | -50.56794 | 2025-09-13 03:47:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 21.8 |
| b850e289-fee3-3ec6-94c7-e76f21847b35 | -10.37899 | -50.49466 | 2025-09-13 03:47:00 | NPP-375D | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 7d85461f-7a86-35ea-bbeb-1aa7d7d390a7 | -20.4219 | -46.45781 | 2025-09-13 03:47:00 | NPP-375D | SÃO JOÃO BATISTA DO GLÓRIA | MINAS GERAIS | Brasil | 3162203 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 6fc450ea-35bf-3bec-a29f-fd747c446d72 | -13.47956 | -48.45328 | 2025-09-13 03:47:00 | NPP-375D | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 6256cd50-703a-31e9-8cc4-7bfeaecfa905 | -12.10774 | -44.89024 | 2025-09-13 03:47:00 | NPP-375D | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 7b875c33-b252-3aec-97b1-f77df4d16479 | -11.44082 | -43.56249 | 2025-09-13 03:47:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 17237319-ce74-349d-9c89-85b9e2096894 | -11.82375 | -50.56691 | 2025-09-13 03:47:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 12.2 |
| 66b6dd7a-0767-3336-89e3-e8dc856c5e77 | -12.1108 | -44.85221 | 2025-09-13 03:47:00 | NPP-375D | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 1fcde0b1-785f-3381-955f-300a76a5340e | -11.7347 | -46.61739 | 2025-09-13 03:47:00 | NPP-375D | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 8.1 |
| 5d92cb71-0cc1-357d-9b1f-7d2ef63f29cb | -8.50588 | -47.32405 | 2025-09-13 03:47:00 | NPP-375D | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 232d81f6-a8de-3c1f-9d7b-1a2e87191dba | -16.60979 | -49.47347 | 2025-09-13 03:47:00 | NPP-375D | TRINDADE | GOIÁS | Brasil | 5221403 | 52 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 20ba6b3b-9175-39d8-abf3-3e2c476f5be6 | -20.39049 | -45.54013 | 2025-09-13 03:47:00 | NPP-375D | CÓRREGO FUNDO | MINAS GERAIS | Brasil | 3119955 | 31 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 3f27a946-5f2a-36a2-961c-09d303a566e9 | -12.13331 | -44.83882 | 2025-09-13 03:47:00 | NPP-375D | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 5.0 |
| b9bc9482-e49a-30e8-a849-b2645d83518d | -13.92107 | -48.27213 | 2025-09-13 03:47:00 | NPP-375D | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 75c53649-1624-3ff1-b73b-754bb7fadbc6 | -12.56546 | -45.67121 | 2025-09-13 03:47:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 3ba7bd5f-d271-3597-a6e4-09cdb41d3db7 | -11.85923 | -50.57507 | 2025-09-13 03:47:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 71.0 |
| 9b8e525c-946f-344a-a712-4df21037fea8 | -14.33939 | -46.61477 | 2025-09-13 03:47:00 | NPP-375D | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 0a01c38f-c3a3-3cbf-b384-76687dcdbb65 | -13.47328 | -48.4527 | 2025-09-13 03:47:00 | NPP-375D | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 46adb61b-e3c7-3d60-95b9-fae288f8f696 | -11.15445 | -50.7105 | 2025-09-13 03:47:00 | NPP-375D | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 1ef3746a-cb9f-389d-9afd-f63f3afb3d26 | -14.20712 | -46.27622 | 2025-09-13 03:47:00 | NPP-375D | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 1ae9e189-5b2d-31ed-a2ac-6ff1981afcd3 | -16.78801 | -51.35875 | 2025-09-13 03:47:00 | NPP-375D | PALESTINA DE GOIÁS | GOIÁS | Brasil | 5215652 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| bac3c1ea-5fbd-30a0-bdf4-c62545ef288e | -11.58804 | -50.61332 | 2025-09-13 03:47:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| c75b4a60-78c9-356b-b8b8-71b4a67fe796 | -11.1167 | -50.70984 | 2025-09-13 03:47:00 | NPP-375D | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| d9965442-7fe2-3cc3-a756-31c0e2c151e5 | -8.18717 | -42.43462 | 2025-09-13 03:47:00 | NPP-375D | SÃO JOÃO DO PIAUÍ | PIAUÍ | Brasil | 2210003 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| f427b66f-baf6-3ccd-af1e-5bc8782c74d3 | -8.94115 | -44.45017 | 2025-09-13 03:47:00 | NPP-375D | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 679af532-f70a-3487-b54f-836b6e87e0ae | -18.43231 | -43.65413 | 2025-09-13 03:47:00 | NPP-375D | DATAS | MINAS GERAIS | Brasil | 3121001 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 98789ad1-2b16-3c10-bd0a-b754aabbbb25 | -13.92307 | -48.26483 | 2025-09-13 03:47:00 | NPP-375D | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 7.2 |
| 0d391d03-198c-381c-8e10-80cb7836cd0a | -13.88587 | -48.25989 | 2025-09-13 03:47:00 | NPP-375D | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 1f07bd6a-e09f-3b01-afff-5ef5cd938426 | -14.21 | -46.2336 | 2025-09-13 03:47:00 | NPP-375D | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| cdb4cc09-60dc-3c87-beca-46d2e5ebd5cb | -16.34132 | -51.53416 | 2025-09-13 03:47:00 | NPP-375D | ARENÓPOLIS | GOIÁS | Brasil | 5202353 | 52 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 780dc5a8-49fe-3f19-84f8-5a5402d8a826 | -20.46915 | -42.39703 | 2025-09-13 03:47:00 | NPP-375D | PEDRA BONITA | MINAS GERAIS | Brasil | 3148756 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| ea28060f-efa1-37d2-8171-785182c46323 | -10.75409 | -50.52172 | 2025-09-13 03:47:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 369f9f4a-ca6c-3a7a-bf42-b4a4be0d93f2 | -11.41359 | -50.74206 | 2025-09-13 03:47:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 3.6 |
| ca1520e6-ef26-3e26-bdb0-95a48ce65866 | -12.12919 | -44.83702 | 2025-09-13 03:47:00 | NPP-375D | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 255282c9-e938-33fd-8dd6-07c500c95c77 | -13.77901 | -46.28587 | 2025-09-13 03:47:00 | NPP-375D | GUARANI DE GOIÁS | GOIÁS | Brasil | 5209408 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| fa176908-f0ce-3cb2-8e26-404c4a2dee14 | -14.19932 | -46.25988 | 2025-09-13 03:47:00 | NPP-375D | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 4.3 |
| abe39245-2fac-3968-9cdf-5db787a8034e | -14.2081 | -46.24326 | 2025-09-13 03:47:00 | NPP-375D | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| ba7291f7-6ef6-3979-a887-7052c0cdd96b | -12.00109 | -47.76084 | 2025-09-13 03:47:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 1b707504-4ab5-3cc9-8af1-69ab72daab11 | -14.41704 | -46.40666 | 2025-09-13 03:47:00 | NPP-375D | BURITINÓPOLIS | GOIÁS | Brasil | 5203962 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 4958916d-b2f3-3798-8aad-de0e165dd0e7 | -9.06449 | -47.03195 | 2025-09-13 03:47:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| d51c49a9-f289-3c8f-a38c-7cd62bce3e61 | -14.20839 | -46.2698 | 2025-09-13 03:47:00 | NPP-375D | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| c7b1e7af-fd4f-3074-810e-f258de95dbc8 | -7.329 | -44.6025 | 2025-09-13 03:47:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 9e73ea7f-faa6-3c24-a170-1b4bb337f4fc | -14.20512 | -46.25841 | 2025-09-13 03:47:00 | NPP-375D | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 3d5f805b-9336-3911-8360-f6d55473189c | -11.46803 | -43.59823 | 2025-09-13 03:47:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 22d4af5b-84b0-317d-8a41-6c88907e9155 | -20.42654 | -46.45942 | 2025-09-13 03:47:00 | NPP-375D | SÃO JOÃO BATISTA DO GLÓRIA | MINAS GERAIS | Brasil | 3162203 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 11953afc-7ae0-3b46-9b61-c136947e1a20 | -18.15801 | -49.18677 | 2025-09-13 03:47:00 | NPP-375D | BURITI ALEGRE | GOIÁS | Brasil | 5203906 | 52 | 33 | nan | nan | nan | Mata Atlântica | 7.5 |
| 9962b792-3903-39b5-a57a-07d145112aa5 | -17.31146 | -48.74343 | 2025-09-13 03:47:00 | NPP-375D | SANTA CRUZ DE GOIÁS | GOIÁS | Brasil | 5219209 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 166da5ea-6f31-3fd6-937d-d92945b12b8e | -11.81815 | -50.55816 | 2025-09-13 03:47:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 12.7 |
| 15fc9501-cd96-3523-9fd8-cb7408e5bee8 | -11.4193 | -45.60798 | 2025-09-13 03:47:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 8.6 |
| f2d45198-e29d-3bb4-a909-1314d2a47a3b | -13.95178 | -48.18828 | 2025-09-13 03:47:00 | NPP-375D | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 02ef16fe-5cd9-3efa-b8d5-ac1309c56ca0 | -6.8353 | -47.86325 | 2025-09-13 03:47:00 | NPP-375D | DARCINÓPOLIS | TOCANTINS | Brasil | 1706506 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 18589e6b-186b-3598-8f09-eb30849fe8d5 | -17.83862 | -44.22145 | 2025-09-13 03:47:00 | NPP-375D | BUENÓPOLIS | MINAS GERAIS | Brasil | 3109204 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| c588e006-96c8-3c3d-838a-ce69517d8f78 | -11.47178 | -43.60415 | 2025-09-13 03:47:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 9b319713-0ae0-3721-bc61-cd6ad99577a8 | -14.28145 | -46.06285 | 2025-09-13 03:47:00 | NPP-375D | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 34a6066b-be01-3147-a41a-2745c3f2ea33 | -9.8532 | -43.14451 | 2025-09-13 03:47:00 | NPP-375D | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Caatinga | 2.7 |
| 001cbacd-a8c4-3856-8b3a-cf5f17f34415 | -20.54961 | -45.83063 | 2025-09-13 03:47:00 | NPP-375D | PIMENTA | MINAS GERAIS | Brasil | 3150505 | 31 | 33 | nan | nan | nan | Cerrado | 3.4 |
| cd6027f1-5c18-35fc-b7b2-ee88a96ae570 | -12.13148 | -44.8247 | 2025-09-13 03:47:00 | NPP-375D | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 08d1ac01-df50-3cd0-983b-d68950b0b3d6 | -20.59382 | -44.90486 | 2025-09-13 03:47:00 | NPP-375D | CARMO DA MATA | MINAS GERAIS | Brasil | 3114006 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.3 |
| 8bf62984-8f57-3036-bef5-a1e90bf84e26 | -10.78543 | -50.55179 | 2025-09-13 03:47:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 10.6 |
| 15c344d6-773e-3f0b-95d0-3a4c477e5693 | -10.76007 | -50.52316 | 2025-09-13 03:47:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 0c0e97d0-7e3a-3aa5-993f-927e086d4820 | -11.82675 | -50.55268 | 2025-09-13 03:47:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 23.2 |
| 3b669c1a-7887-3562-a867-20c993a78c61 | -11.86485 | -50.58382 | 2025-09-13 03:47:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 16.5 |
| 21a89c64-6d76-3651-86e4-6e3f8d49a96c | -7.56083 | -42.64437 | 2025-09-13 03:47:00 | NPP-375D | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 3.8 |
| a6d0680a-40b9-3454-a335-af952b0eae5d | -11.84355 | -50.57893 | 2025-09-13 03:47:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 58.3 |
| 95028dc3-5ecb-35f2-8f70-ef8665aca9a9 | -17.12757 | -48.48389 | 2025-09-13 03:47:00 | NPP-375D | PIRES DO RIO | GOIÁS | Brasil | 5217401 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 40b49a43-f920-322e-a5ea-521ee95c3e95 | -10.78821 | -44.77808 | 2025-09-13 03:47:00 | NPP-375D | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 4f2a6f5c-f365-3d8c-876d-8704730e7af2 | -14.41405 | -46.40624 | 2025-09-13 03:47:00 | NPP-375D | BURITINÓPOLIS | GOIÁS | Brasil | 5203962 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| b2e781ec-a549-35c6-9677-20474f5d146e | -14.41785 | -46.40267 | 2025-09-13 03:47:00 | NPP-375D | BURITINÓPOLIS | GOIÁS | Brasil | 5203962 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| e8dd9305-6e3b-3643-bf27-10637630494d | -16.32784 | -51.54965 | 2025-09-13 03:47:00 | NPP-375D | ARENÓPOLIS | GOIÁS | Brasil | 5202353 | 52 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 3bd96daf-dead-3021-b4ce-3459dbc4db68 | -17.90586 | -47.02425 | 2025-09-13 03:47:00 | NPP-375D | GUARDA-MOR | MINAS GERAIS | Brasil | 3128600 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| b815c02d-d272-32a9-9413-8aba77a9cd37 | -10.23701 | -48.63799 | 2025-09-13 03:47:00 | NPP-375D | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 8caedd07-7b23-38ca-a457-01e793d3b211 | -11.78977 | -50.55169 | 2025-09-13 03:47:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 8c4faa8a-72dc-3a78-a62d-20f55247a4d1 | -14.2282 | -41.97691 | 2025-09-13 03:47:00 | NPP-375D | RIO DO ANTÔNIO | BAHIA | Brasil | 2926806 | 29 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 9b897fd1-510e-3875-a673-fe9302113188 | -20.25915 | -44.18969 | 2025-09-13 03:47:00 | NPP-375D | BONFIM | MINAS GERAIS | Brasil | 3108107 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.3 |
| f2ed8184-5170-3589-a45a-9a08bfbe2528 | -14.21538 | -46.26222 | 2025-09-13 03:47:00 | NPP-375D | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 3392282c-bb39-3eb3-b8d8-ae2dd96448cb | -10.71564 | -48.60935 | 2025-09-13 03:47:00 | NPP-375D | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 25f59c30-41ed-34a5-bf1b-5790378efe1a | -12.84905 | -47.94713 | 2025-09-13 03:47:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 8.3 |
| d3e4b872-bdfd-36a4-83ca-a02ab36f9c96 | -17.27838 | -47.25187 | 2025-09-13 03:47:00 | NPP-375D | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 1843aff1-4cf3-3e3b-bb4e-b224abccad0a | -10.90198 | -45.58323 | 2025-09-13 03:47:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 15ab54ee-d671-37bc-bccb-66f5afd573eb | -14.20899 | -46.26674 | 2025-09-13 03:47:00 | NPP-375D | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 1186afcf-34b2-3ffb-8fb3-e7a5b711e5aa | -20.2857 | -46.59256 | 2025-09-13 03:47:00 | NPP-375D | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 2.8 |
| b368bb74-b88e-3c33-bcce-73c97c1ce212 | -12.12321 | -44.83736 | 2025-09-13 03:47:00 | NPP-375D | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 20281ba8-acf4-3045-8f12-2b438c9d6af1 | -16.64691 | -49.79838 | 2025-09-13 03:47:00 | NPP-375D | PALMEIRAS DE GOIÁS | GOIÁS | Brasil | 5215702 | 52 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 4235f2fa-b83d-3973-9a49-a422b558a682 | -8.08062 | -42.56308 | 2025-09-13 03:47:00 | NPP-375D | RIBEIRA DO PIAUÍ | PIAUÍ | Brasil | 2208874 | 22 | 33 | nan | nan | nan | Caatinga | 3.6 |
| c48049b3-af36-36e6-8258-22e4eee5573c | -17.41946 | -49.23807 | 2025-09-13 03:47:00 | NPP-375D | PROFESSOR JAMIL | GOIÁS | Brasil | 5218391 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 2fcf0ae4-47fd-3df5-82c8-d823b6aacbf3 | -16.35509 | -51.53788 | 2025-09-13 03:47:00 | NPP-375D | ARENÓPOLIS | GOIÁS | Brasil | 5202353 | 52 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 9419baa4-58bf-36e6-a227-5d4db6beda57 | -14.22272 | -46.28098 | 2025-09-13 03:47:00 | NPP-375D | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 37.5 |
| 2ea6001a-ac2f-38ad-9018-880dced3bb6a | -18.14935 | -48.46217 | 2025-09-13 03:47:00 | NPP-375D | CORUMBAÍBA | GOIÁS | Brasil | 5205901 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 87dce672-c357-3fc5-84a3-f35949f97b41 | -14.43213 | -46.39857 | 2025-09-13 03:47:00 | NPP-375D | BURITINÓPOLIS | GOIÁS | Brasil | 5203962 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 3d3f74cc-bba0-3b1c-8f15-983d1b06f019 | -11.47553 | -43.61008 | 2025-09-13 03:47:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 0dd15516-d5a6-3c4d-80be-0b11ed122d1c | -11.86829 | -46.75826 | 2025-09-13 03:47:00 | NPP-375D | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| eec2da75-2a09-307d-8d01-1a7ea1350d64 | -16.79443 | -51.36093 | 2025-09-13 03:47:00 | NPP-375D | PALESTINA DE GOIÁS | GOIÁS | Brasil | 5215652 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| c4d5ff75-8e27-3844-a4c9-d93196b0c079 | -12.12945 | -44.83192 | 2025-09-13 03:47:00 | NPP-375D | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| f23b5404-c626-3160-a71f-833ab4f4e68d | -13.92195 | -48.26781 | 2025-09-13 03:47:00 | NPP-375D | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 5443bf3d-b468-30e8-874d-1d77662f6db9 | -20.07602 | -43.6955 | 2025-09-13 03:47:00 | NPP-375D | RIO ACIMA | MINAS GERAIS | Brasil | 3154804 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 313d5387-b5cc-325d-9360-9c54361dfea1 | -14.43443 | -46.40283 | 2025-09-13 03:47:00 | NPP-375D | BURITINÓPOLIS | GOIÁS | Brasil | 5203962 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 9d16d052-77a5-327f-b51e-c73a6c3dec90 | -11.13989 | -45.31626 | 2025-09-13 03:47:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 4.2 |


[Clique aqui para ver as próximas entradas](README28.md)
