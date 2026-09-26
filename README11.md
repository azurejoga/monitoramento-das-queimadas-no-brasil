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

## Dados Diários - Página 11

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 165e7de8-2b57-355a-abab-64e25846b03b | -15.16758 | -48.8143 | 2026-09-26 04:10:00 | NPP-375D | VILA PROPÍCIO | GOIÁS | Brasil | 5222302 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 2bd7e1e0-180d-3799-b497-d98613fe0884 | -19.89539 | -48.2671 | 2026-09-26 04:10:00 | NPP-375D | CONCEIÇÃO DAS ALAGOAS | MINAS GERAIS | Brasil | 3117306 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 3fdf9562-f7ab-34fe-ab06-e434c2b2793d | -16.75859 | -47.25564 | 2026-09-26 04:10:00 | NPP-375D | CRISTALINA | GOIÁS | Brasil | 5206206 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 4d4e02e8-e4a2-3453-8741-b44aebc66b6a | -16.57052 | -43.98949 | 2026-09-26 04:10:00 | NPP-375D | MONTES CLAROS | MINAS GERAIS | Brasil | 3143302 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| e8e1ae9a-8373-3b57-9917-8845a5e4dd6d | -16.35967 | -42.56541 | 2026-09-26 04:10:00 | NPP-375D | PADRE CARVALHO | MINAS GERAIS | Brasil | 3146255 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 240fec91-411e-3bd1-9dfd-439d9a986912 | -12.9466 | -51.06546 | 2026-09-26 04:10:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 7.8 |
| 0e85b13d-4726-3d14-8cbe-2483805d77aa | -15.43045 | -47.90359 | 2026-09-26 04:10:00 | NPP-375D | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 4a46512b-a46c-36af-aa90-e54d90b0267a | -12.94746 | -51.06668 | 2026-09-26 04:10:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 15.9 |
| 70e48379-fcad-3445-b145-b533498a3471 | -15.89597 | -43.47674 | 2026-09-26 04:10:00 | NPP-375D | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| ed15b6fd-333b-3dd3-9149-0dafe9b0070d | -15.24725 | -43.27156 | 2026-09-26 04:10:00 | NPP-375D | PAI PEDRO | MINAS GERAIS | Brasil | 3146552 | 31 | 33 | nan | nan | nan | Caatinga | 35.9 |
| 768425ed-b0b9-39d1-aadf-6289fe42ac76 | -15.89526 | -43.48095 | 2026-09-26 04:10:00 | NPP-375D | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 0b0ce36d-cb4b-33f1-9ec0-7ae6ad2445c9 | -16.49076 | -45.98281 | 2026-09-26 04:10:00 | NPP-375D | BONFINÓPOLIS DE MINAS | MINAS GERAIS | Brasil | 3108206 | 31 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 2f91f9cc-7caf-387b-aa19-cedb8d156dd7 | -17.38176 | -41.77833 | 2026-09-26 04:10:00 | NPP-375D | NOVO CRUZEIRO | MINAS GERAIS | Brasil | 3145307 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.4 |
| 03f04d7a-f9ba-3591-890f-3a6505376df7 | -21.10604 | -45.65726 | 2026-09-26 04:10:00 | NPP-375D | BOA ESPERANÇA | MINAS GERAIS | Brasil | 3107109 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 4309183e-13eb-3d95-bf83-be62f5f34e71 | -15.25081 | -43.27222 | 2026-09-26 04:10:00 | NPP-375D | PAI PEDRO | MINAS GERAIS | Brasil | 3146552 | 31 | 33 | nan | nan | nan | Caatinga | 4.0 |
| 7bcd353e-5d81-3b77-a3f6-abd066d953b7 | -18.22998 | -45.59465 | 2026-09-26 04:10:00 | NPP-375D | SÃO GONÇALO DO ABAETÉ | MINAS GERAIS | Brasil | 3161700 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 5f8033cf-6545-3023-ac74-7a3cd4b81b5f | -14.87639 | -47.13468 | 2026-09-26 04:10:00 | NPP-375D | VILA BOA | GOIÁS | Brasil | 5222203 | 52 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 3ea6ba20-8f78-300f-b9a2-2aaee367f207 | -13.19828 | -48.32486 | 2026-09-26 04:10:00 | NPP-375D | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| b9faed24-b3f3-37bb-bd40-cca846a74e10 | -15.42201 | -47.89708 | 2026-09-26 04:10:00 | NPP-375D | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 446dd7cd-3c76-31e7-8823-90a47abe4787 | -15.2451 | -43.26265 | 2026-09-26 04:10:00 | NPP-375D | PAI PEDRO | MINAS GERAIS | Brasil | 3146552 | 31 | 33 | nan | nan | nan | Caatinga | 27.0 |
| a79ba93b-0c6d-3d80-9445-4262bc08094f | -13.20447 | -48.31981 | 2026-09-26 04:10:00 | NPP-375D | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 6846e223-56df-396a-8d03-1f1fe4eb30e5 | -15.9785 | -43.00946 | 2026-09-26 04:10:00 | NPP-375D | RIACHO DOS MACHADOS | MINAS GERAIS | Brasil | 3154507 | 31 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 6d21b423-56b2-36ee-a31b-26dccc33437e | -14.22183 | -43.73843 | 2026-09-26 04:10:00 | NPP-375D | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| de9097ec-a863-3cf3-8cff-1f4b396a8b7a | -14.86654 | -47.13751 | 2026-09-26 04:10:00 | NPP-375D | VILA BOA | GOIÁS | Brasil | 5222203 | 52 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 74d92460-8e5a-3934-aa5f-623426e02ffd | -14.22319 | -43.7413 | 2026-09-26 04:10:00 | NPP-375D | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| f45cd0b1-f098-33d7-873b-81dd07fa2da4 | -16.56365 | -43.98561 | 2026-09-26 04:10:00 | NPP-375D | MONTES CLAROS | MINAS GERAIS | Brasil | 3143302 | 31 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 800b4b4c-23ab-34c6-a170-41a2e8541f2d | -17.12872 | -50.29867 | 2026-09-26 04:10:00 | NPP-375D | PARAÚNA | GOIÁS | Brasil | 5216403 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 71391f4b-acb0-3b74-ba66-8e15b25fcee7 | -18.24099 | -45.5951 | 2026-09-26 04:10:00 | NPP-375D | SÃO GONÇALO DO ABAETÉ | MINAS GERAIS | Brasil | 3161700 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| aa5ef7dc-8414-3264-a138-d05f074d44b1 | -16.56652 | -43.99068 | 2026-09-26 04:10:00 | NPP-375D | MONTES CLAROS | MINAS GERAIS | Brasil | 3143302 | 31 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 98e53f35-de1c-31d7-bc64-4944f92cade9 | -20.42583 | -47.45795 | 2026-09-26 04:10:00 | NPP-375D | CRISTAIS PAULISTA | SÃO PAULO | Brasil | 3513207 | 35 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 593bda5d-365b-31fd-a433-9fecd7539aab | -16.56766 | -43.98445 | 2026-09-26 04:10:00 | NPP-375D | MONTES CLAROS | MINAS GERAIS | Brasil | 3143302 | 31 | 33 | nan | nan | nan | Cerrado | 2.7 |
| dfbf12d9-5cc5-3e43-bbe7-37117c3c29a9 | -16.49007 | -45.98653 | 2026-09-26 04:10:00 | NPP-375D | BONFINÓPOLIS DE MINAS | MINAS GERAIS | Brasil | 3108206 | 31 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 5af7d02d-cf29-3a92-84d0-dc5f470e56a2 | -19.05552 | -46.82531 | 2026-09-26 04:10:00 | NPP-375D | PATROCÍNIO | MINAS GERAIS | Brasil | 3148103 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 6c91090e-5d3b-3fdc-97a9-2f530f64e51f | -16.90192 | -42.12257 | 2026-09-26 04:10:00 | NPP-375D | ARAÇUAÍ | MINAS GERAIS | Brasil | 3103405 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 63a534dd-2bde-3799-a0ef-83644fac31fe | -20.42506 | -47.46193 | 2026-09-26 04:10:00 | NPP-375D | CRISTAIS PAULISTA | SÃO PAULO | Brasil | 3513207 | 35 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 0027c325-f9d9-3c49-9b47-cfbf5003196d | -15.24866 | -43.26328 | 2026-09-26 04:10:00 | NPP-375D | PAI PEDRO | MINAS GERAIS | Brasil | 3146552 | 31 | 33 | nan | nan | nan | Caatinga | 27.0 |
| a895fd1b-709a-30eb-ba8a-07e077cb8d8a | -12.9484 | -51.06218 | 2026-09-26 04:10:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 10.9 |
| 9fe87e51-32ca-393d-847c-610dfe8f7fcd | -19.89278 | -48.26405 | 2026-09-26 04:10:00 | NPP-375D | CONCEIÇÃO DAS ALAGOAS | MINAS GERAIS | Brasil | 3117306 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 709ce9d9-cc27-32d1-b8e6-92fead32a0c3 | -19.90157 | -48.25924 | 2026-09-26 04:10:00 | NPP-375D | CONCEIÇÃO DAS ALAGOAS | MINAS GERAIS | Brasil | 3117306 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| e21f68a1-ca55-37c9-9d2d-22c4f23450af | -16.76294 | -47.25664 | 2026-09-26 04:10:00 | NPP-375D | CRISTALINA | GOIÁS | Brasil | 5206206 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| b9466a3b-27e2-358f-bbd7-d48e93630ee5 | -16.56728 | -43.98626 | 2026-09-26 04:10:00 | NPP-375D | MONTES CLAROS | MINAS GERAIS | Brasil | 3143302 | 31 | 33 | nan | nan | nan | Cerrado | 2.5 |
| b47d9d65-6ba4-3d0c-86a5-de0db75cf656 | -14.87554 | -47.13921 | 2026-09-26 04:10:00 | NPP-375D | VILA BOA | GOIÁS | Brasil | 5222203 | 52 | 33 | nan | nan | nan | Cerrado | 9.6 |
| c03aebc2-24e0-3230-9079-4fb9d788e6f9 | -15.1973 | -49.28936 | 2026-09-26 04:10:00 | NPP-375D | GOIANÉSIA | GOIÁS | Brasil | 5208608 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 5a7dc797-cc5c-3523-bfc4-76d91a9fa49c | -19.90853 | -48.25383 | 2026-09-26 04:10:00 | NPP-375D | CONCEIÇÃO DAS ALAGOAS | MINAS GERAIS | Brasil | 3117306 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 344a5083-4f0f-3c25-811d-e3ea05e538a9 | -16.67645 | -41.85463 | 2026-09-26 04:10:00 | NPP-375D | ITINGA | MINAS GERAIS | Brasil | 3134004 | 31 | 33 | nan | nan | nan | Mata Atlântica | 16.8 |
| 847edc08-92f7-3a70-8d7e-4f0f13cfa27e | -15.42104 | -47.90199 | 2026-09-26 04:10:00 | NPP-375D | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| e1583e11-12f6-347e-ba50-06cbe7dc511d | -13.20331 | -48.32578 | 2026-09-26 04:10:00 | NPP-375D | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | 11.7 |
| b1dd39d3-a095-3ac1-980e-be5556016cc4 | -18.24924 | -45.59858 | 2026-09-26 04:10:00 | NPP-375D | SÃO GONÇALO DO ABAETÉ | MINAS GERAIS | Brasil | 3161700 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| ae763de0-1e31-3817-a96e-57e7e2002fcf | -12.95258 | -51.0668 | 2026-09-26 04:10:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 7.8 |
| b5cca8d6-f698-3f9e-a7d7-1767b8aeb2d9 | -19.91123 | -48.2569 | 2026-09-26 04:10:00 | NPP-375D | CONCEIÇÃO DAS ALAGOAS | MINAS GERAIS | Brasil | 3117306 | 31 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 3fdd02f2-656b-368d-9475-668d86071865 | -15.21654 | -41.5081 | 2026-09-26 04:10:00 | NPP-375D | TREMEDAL | BAHIA | Brasil | 2931806 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.4 |
| d3720d98-130e-3b4a-9424-f7700d1f8071 | -15.43138 | -47.89887 | 2026-09-26 04:10:00 | NPP-375D | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 10fd055b-c3db-31fc-90c9-1d0b4597fed0 | -15.42459 | -47.90065 | 2026-09-26 04:10:00 | NPP-375D | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 5a63d05c-f8d2-30b9-8154-0f4a64c34372 | -12.94149 | -51.06538 | 2026-09-26 04:10:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 15.9 |
| df47efac-bde5-3ef1-9140-b4d558a50c3b | -15.23298 | -43.26897 | 2026-09-26 04:10:00 | NPP-375D | PAI PEDRO | MINAS GERAIS | Brasil | 3146552 | 31 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 4383bc79-6156-30b3-8f00-1cb077638b51 | -18.23328 | -45.59352 | 2026-09-26 04:10:00 | NPP-375D | SÃO GONÇALO DO ABAETÉ | MINAS GERAIS | Brasil | 3161700 | 31 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 3ed6a42d-e46d-396c-9720-037f9c291b39 | -16.76994 | -47.2676 | 2026-09-26 04:10:00 | NPP-375D | CRISTALINA | GOIÁS | Brasil | 5206206 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| edb50114-f847-363f-831d-d7c057265c33 | -12.95348 | -51.06228 | 2026-09-26 04:10:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 7.8 |
| e9ce2523-fdfe-3042-9a6a-0d18419cad19 | -15.23655 | -43.26962 | 2026-09-26 04:10:00 | NPP-375D | PAI PEDRO | MINAS GERAIS | Brasil | 3146552 | 31 | 33 | nan | nan | nan | Caatinga | 33.5 |
| 988710e1-6661-3c0b-8d89-c19b4c10fa48 | -15.16141 | -48.81923 | 2026-09-26 04:10:00 | NPP-375D | VILA PROPÍCIO | GOIÁS | Brasil | 5222302 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 3cddb472-c702-3fde-954c-bb5afecb8bbe | -19.90766 | -48.25835 | 2026-09-26 04:10:00 | NPP-375D | CONCEIÇÃO DAS ALAGOAS | MINAS GERAIS | Brasil | 3117306 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 7888eec8-27cf-340c-b1d6-a547c2c1a272 | -19.90328 | -48.25727 | 2026-09-26 04:10:00 | NPP-375D | CONCEIÇÃO DAS ALAGOAS | MINAS GERAIS | Brasil | 3117306 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| b91e345c-35ee-36a2-8612-ecd0498b992d | -15.89384 | -43.47537 | 2026-09-26 04:10:00 | NPP-375D | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 6.8 |
| f9c070d4-c9b4-3cae-b168-2f6a6adc16a3 | -15.19662 | -49.29281 | 2026-09-26 04:10:00 | NPP-375D | GOIANÉSIA | GOIÁS | Brasil | 5208608 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 2a0ce995-c272-3fa5-935a-111f3c07c510 | -16.56403 | -43.9838 | 2026-09-26 04:10:00 | NPP-375D | MONTES CLAROS | MINAS GERAIS | Brasil | 3143302 | 31 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 4e9112a1-7f72-37cc-857f-9d9abe53ed09 | -14.82015 | -43.32023 | 2026-09-26 04:10:00 | NPP-375D | GAMELEIRAS | MINAS GERAIS | Brasil | 3127339 | 31 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 46ab0ebd-c118-3c87-ad16-100f46efe703 | -15.20187 | -49.29332 | 2026-09-26 04:10:00 | NPP-375D | GOIANÉSIA | GOIÁS | Brasil | 5208608 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| f1955ded-7fc6-38c2-b338-8da89232c419 | -15.16876 | -48.80834 | 2026-09-26 04:10:00 | NPP-375D | VILA PROPÍCIO | GOIÁS | Brasil | 5222302 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 68c39e04-2086-3beb-b9d7-c5b70b0b4b5f | -12.94751 | -51.06094 | 2026-09-26 04:10:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 7.8 |
| ad71cb17-11f5-3e97-aec3-90db5c0c3331 | -21.1069 | -45.6525 | 2026-09-26 04:10:00 | NPP-375D | BOA ESPERANÇA | MINAS GERAIS | Brasil | 3107109 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 30e938fa-8874-3ec2-9d11-6b96c5f04043 | -18.23384 | -45.59542 | 2026-09-26 04:10:00 | NPP-375D | SÃO GONÇALO DO ABAETÉ | MINAS GERAIS | Brasil | 3161700 | 31 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 2643acc0-e4c6-3abb-97bf-0b9bce080eaf | -15.17373 | -48.80946 | 2026-09-26 04:10:00 | NPP-375D | VILA PROPÍCIO | GOIÁS | Brasil | 5222302 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| bd99c3aa-cbf0-3f6a-995d-f438608f4013 | -15.73105 | -50.79951 | 2026-09-26 04:10:00 | NPP-375D | ITAPIRAPUÃ | GOIÁS | Brasil | 5211008 | 52 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 207a30ab-bd65-3eaf-9dd4-1d8947d88300 | -17.12943 | -50.29526 | 2026-09-26 04:10:00 | NPP-375D | PARAÚNA | GOIÁS | Brasil | 5216403 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 72492713-61a3-30c9-a8ca-055457c49422 | -16.35561 | -42.5686 | 2026-09-26 04:10:00 | NPP-375D | PADRE CARVALHO | MINAS GERAIS | Brasil | 3146255 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 8d235cfe-6bb0-3c6c-a9ca-e72ce01dcd8c | -19.8919 | -48.26856 | 2026-09-26 04:10:00 | NPP-375D | CONCEIÇÃO DAS ALAGOAS | MINAS GERAIS | Brasil | 3117306 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 6066030b-ab7d-3841-9b6d-8e81508f4547 | -16.35624 | -42.56482 | 2026-09-26 04:10:00 | NPP-375D | PADRE CARVALHO | MINAS GERAIS | Brasil | 3146255 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| f0001f27-2f85-3bde-bf62-4b4a49d46ad4 | -16.75813 | -45.0625 | 2026-09-26 04:10:00 | NPP-375D | BURITIZEIRO | MINAS GERAIS | Brasil | 3109402 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 599195e2-8e3e-3a11-9950-97812b2aac3d | -15.24654 | -43.27573 | 2026-09-26 04:10:00 | NPP-375D | PAI PEDRO | MINAS GERAIS | Brasil | 3146552 | 31 | 33 | nan | nan | nan | Caatinga | 35.9 |
| 1f4342d1-3620-366d-884f-de314a58a506 | -15.8924 | -43.47609 | 2026-09-26 04:10:00 | NPP-375D | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 7.8 |
| 290200b0-193f-3d14-8fab-1a19c1a5b74f | -15.42082 | -47.89489 | 2026-09-26 04:10:00 | NPP-375D | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 202ca903-36dd-3652-be60-accb53508831 | -16.56325 | -43.98819 | 2026-09-26 04:10:00 | NPP-375D | MONTES CLAROS | MINAS GERAIS | Brasil | 3143302 | 31 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 52b26a09-8393-3076-a953-ae435d86596f | -16.67369 | -41.85031 | 2026-09-26 04:10:00 | NPP-375D | ITINGA | MINAS GERAIS | Brasil | 3134004 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.0 |
| ca8e1597-8c92-3dfe-be8f-75efd24b2a63 | -16.26022 | -47.80881 | 2026-09-26 04:10:00 | NPP-375D | LUZIÂNIA | GOIÁS | Brasil | 5212501 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 6fa6ed9f-692d-3ee7-ac18-be2b27ebeed6 | -15.25152 | -43.26806 | 2026-09-26 04:10:00 | NPP-375D | PAI PEDRO | MINAS GERAIS | Brasil | 3146552 | 31 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 3396cc40-a084-3d8f-8b49-0736c316c437 | -15.89311 | -43.47956 | 2026-09-26 04:10:00 | NPP-375D | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 1db8e1a7-dba1-3179-b323-11efad0ca797 | -15.89169 | -43.48029 | 2026-09-26 04:10:00 | NPP-375D | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 7.8 |
| 7cce2a53-4c70-331b-9fc7-86a98c277e36 | -17.37473 | -42.51393 | 2026-09-26 04:10:00 | NPP-375D | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 6080103d-3e23-3044-be5e-ce554a277147 | -14.60982 | -41.03171 | 2026-09-26 04:10:00 | NPP-375D | ANAGÉ | BAHIA | Brasil | 2901205 | 29 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 481cc6f0-090f-3c18-911c-2b06255c0b39 | -18.24187 | -45.59013 | 2026-09-26 04:10:00 | NPP-375D | SÃO GONÇALO DO ABAETÉ | MINAS GERAIS | Brasil | 3161700 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 47a954d8-da9b-3a22-b316-4f6dcdcc9688 | -15.16265 | -48.81301 | 2026-09-26 04:10:00 | NPP-375D | VILA PROPÍCIO | GOIÁS | Brasil | 5222302 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 80ae5791-372a-384f-b845-ab3b1e4259ab | -21.10268 | -46.26685 | 2026-09-26 04:10:00 | NPP-375D | CONCEIÇÃO DA APARECIDA | MINAS GERAIS | Brasil | 3117108 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| c167ec69-56c6-354f-a938-2ef97131f55d | -14.88004 | -47.14009 | 2026-09-26 04:10:00 | NPP-375D | VILA BOA | GOIÁS | Brasil | 5222203 | 52 | 33 | nan | nan | nan | Cerrado | 9.6 |
| 723804a7-28f5-3471-9d8a-864518e68bbf | -14.83307 | -43.30951 | 2026-09-26 04:10:00 | NPP-375D | GAMELEIRAS | MINAS GERAIS | Brasil | 3127339 | 31 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 8010410d-7cde-3421-bf0d-e4e76a49eab8 | -16.67706 | -41.8509 | 2026-09-26 04:10:00 | NPP-375D | ITINGA | MINAS GERAIS | Brasil | 3134004 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.0 |
| 79ddda14-bc3b-3fc2-a7c4-6f9a67b7bc55 | -15.24368 | -43.27091 | 2026-09-26 04:10:00 | NPP-375D | PAI PEDRO | MINAS GERAIS | Brasil | 3146552 | 31 | 33 | nan | nan | nan | Caatinga | 35.9 |
| ec886378-4015-3327-a111-f6917a8f38a0 | -18.54272 | -50.66786 | 2026-09-26 04:10:00 | NPP-375D | QUIRINÓPOLIS | GOIÁS | Brasil | 5218508 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 95d97ede-66cb-3736-8d16-e25916373b52 | -17.59294 | -46.56631 | 2026-09-26 04:10:00 | NPP-375D | LAGOA GRANDE | MINAS GERAIS | Brasil | 3137536 | 31 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 5d74fc77-9d44-3770-899a-7d6cfe6e2103 | -14.86739 | -47.13297 | 2026-09-26 04:10:00 | NPP-375D | VILA BOA | GOIÁS | Brasil | 5222203 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 74607816-44ea-3102-8ce0-da351866a9bb | -18.26184 | -45.61702 | 2026-09-26 04:10:00 | NPP-375D | SÃO GONÇALO DO ABAETÉ | MINAS GERAIS | Brasil | 3161700 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |


[Clique aqui para ver as próximas entradas](README12.md)
