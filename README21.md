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

## Dados Diários - Página 21

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 5ba4b87a-65a7-36da-85b8-f5cc8cf27a96 | -11.20206 | -53.82459 | 2024-12-13 04:23:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 11.7 |
| 752167f1-6098-3bfd-ae80-ebf9a1c3caab | -14.9145 | -52.88042 | 2024-12-13 04:23:00 | NPP-375D | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 8d6f38a7-d1e9-3497-9465-b0dbc5bbb2ed | -12.054 | -46.8875 | 2024-12-13 04:23:00 | NPP-375D | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 74242b19-fbae-32ac-85cf-a8900ad825a8 | -13.05232 | -52.03948 | 2024-12-13 04:23:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| d439ce4c-7286-3a64-aef7-29eb9369f29a | -14.76379 | -52.64005 | 2024-12-13 04:23:00 | NPP-375D | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 0b0f9b4e-1fe2-3652-9cea-053567dd9f15 | -12.07548 | -48.40045 | 2024-12-13 04:23:00 | NPP-375D | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| ec610ffa-594b-3540-ab49-1ffb0d64f22a | -11.49855 | -52.93018 | 2024-12-13 04:23:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 7.0 |
| deaa45b5-a4a7-3b9e-a70a-dff232725079 | -14.77432 | -52.64492 | 2024-12-13 04:23:00 | NPP-375D | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 1305ffee-d685-322e-b2de-98786e3d4f7b | -12.7494 | -48.34354 | 2024-12-13 04:23:00 | NPP-375D | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 1e8a7dce-0532-38f3-951f-9eb541b431c1 | -12.92255 | -47.88951 | 2024-12-13 04:23:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| acb9eb1b-8c1e-30cc-9069-bdd7e83de134 | -13.54396 | -55.38514 | 2024-12-13 04:23:00 | NPP-375D | SANTA RITA DO TRIVELATO | MATO GROSSO | Brasil | 5107768 | 51 | 33 | nan | nan | nan | Cerrado | 0.6 |
| d6c0bbd5-bb6d-3e8e-859d-1d20b6645c24 | -12.33965 | -43.6717 | 2024-12-13 04:23:00 | NPP-375D | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 3.3 |
| dcd74a81-9bc4-3575-a147-34ff5ca2d9ee | -13.0664 | -52.03382 | 2024-12-13 04:23:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 00650798-1f0d-3755-b155-a0977ae188c7 | -11.8635 | -46.94815 | 2024-12-13 04:23:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 0886a191-4d72-39dc-b74b-becb9c0049fb | -11.43678 | -55.91817 | 2024-12-13 04:23:00 | NPP-375D | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 1265eb2a-5117-31d1-9cdf-d4438dc1a63b | -11.81715 | -46.60723 | 2024-12-13 04:23:00 | NPP-375D | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 66eec17a-ea56-38bb-9333-1ea4525aea07 | -14.76729 | -52.64499 | 2024-12-13 04:23:00 | NPP-375D | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 436db631-e00c-3336-8b22-e3eef49e3cd7 | -13.68382 | -54.74533 | 2024-12-13 04:23:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| b5559bc6-21b5-3be0-95fd-0bc387bd6dd7 | -14.78497 | -52.64447 | 2024-12-13 04:23:00 | NPP-375D | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 02f9fd09-656c-3527-9655-92d71841c388 | -14.77151 | -52.64594 | 2024-12-13 04:23:00 | NPP-375D | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 96ec81e3-ae25-3b87-9b3d-1450daf19cbf | -13.06567 | -52.0378 | 2024-12-13 04:23:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Amazônia | 6.2 |
| c92a535d-df03-3575-b3a7-4b02bb1aa08e | -14.78423 | -52.64861 | 2024-12-13 04:23:00 | NPP-375D | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 80ffd1b9-a559-3596-9acc-ff691968da10 | -14.77855 | -52.64581 | 2024-12-13 04:23:00 | NPP-375D | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 4.4 |
| cb2b8e4b-913e-3a22-955e-962554839555 | -11.19616 | -53.82921 | 2024-12-13 04:23:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 11.7 |
| 9638f20c-3f52-34f4-8641-299c4e860684 | -11.51722 | -45.00378 | 2024-12-13 04:23:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| cc387ab3-4842-3ca7-91fb-d164d4bd1839 | -12.35611 | -44.71571 | 2024-12-13 04:23:00 | NPP-375D | CATOLÂNDIA | BAHIA | Brasil | 2907400 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 6da4bcc1-727f-30a2-b1b3-baa0974169e2 | -14.74384 | -52.65294 | 2024-12-13 04:23:00 | NPP-375D | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| e3342cb1-467d-3cc1-b0b0-7e6437aa1160 | -12.36431 | -45.67347 | 2024-12-13 04:23:00 | NPP-375D | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| df87efdb-6f9b-3c74-8a9a-85dd8e2da37f | -14.91528 | -52.87615 | 2024-12-13 04:23:00 | NPP-375D | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 6d619cc8-c3b8-3681-9809-72090d9bfab9 | -11.19664 | -53.83646 | 2024-12-13 04:23:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 15590ebb-e49a-3c01-9e96-04d8bf53133f | -11.44184 | -55.89169 | 2024-12-13 04:23:00 | NPP-375D | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d94d4019-8ace-3767-8044-288fc00190f0 | -13.69158 | -54.75875 | 2024-12-13 04:23:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 64c41b3e-1ea5-313f-a0a1-7d4949f60f31 | -11.19767 | -53.83102 | 2024-12-13 04:23:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 998f0d7d-64ca-301e-820f-205c93c58434 | -14.77508 | -52.64083 | 2024-12-13 04:23:00 | NPP-375D | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 636e0c93-5dcc-320d-b4a8-a2b93d932e43 | -14.78702 | -52.64755 | 2024-12-13 04:23:00 | NPP-375D | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 469414fa-d0dc-3b13-a503-16cd3d829bfc | -15.23668 | -43.36228 | 2024-12-13 04:23:00 | NPP-375D | JAÍBA | MINAS GERAIS | Brasil | 3135050 | 31 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 6db74a81-dac2-3ec0-b98b-44a5bbe39e65 | -11.68977 | -48.07038 | 2024-12-13 04:23:00 | NPP-375D | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 3866a272-dd63-3e89-84e1-a43db818fd36 | -11.48196 | -48.2318 | 2024-12-13 04:23:00 | NPP-375D | SANTA ROSA DO TOCANTINS | TOCANTINS | Brasil | 1718907 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 2e9b7844-d01d-3816-82f2-6de020e0fa7e | -14.75661 | -52.65534 | 2024-12-13 04:23:00 | NPP-375D | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| aca90cc3-bed3-32a8-9e4e-1258cc9ddcb1 | -11.81061 | -49.32713 | 2024-12-13 04:23:00 | NPP-375D | CARIRI DO TOCANTINS | TOCANTINS | Brasil | 1703867 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 8180b080-ef33-38e8-b240-69f64df4187f | -11.20464 | -53.82095 | 2024-12-13 04:23:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 9.6 |
| ce9ff702-ecbd-35b2-b0dc-80d3f32424f8 | -13.05798 | -52.03229 | 2024-12-13 04:23:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 8c6eb05b-5910-38f9-95bd-056a713f1f0c | -23.4641 | -46.46917 | 2024-12-13 04:23:00 | NPP-375D | GUARULHOS | SÃO PAULO | Brasil | 3518800 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 5240fca2-c7c8-30f4-9c85-a6b7efd688d6 | -13.37652 | -54.24633 | 2024-12-13 04:23:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d2234587-2e58-3a1a-863c-5025702152e7 | -12.76637 | -49.3077 | 2024-12-13 04:23:00 | NPP-375D | TALISMÃ | TOCANTINS | Brasil | 1720978 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 97c05236-7030-376f-a9bc-72ae6208453f | -11.1987 | -53.82558 | 2024-12-13 04:23:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 8.8 |
| 3ba515b5-b0f4-34a1-ad40-c0caafdca795 | -11.20795 | -53.81998 | 2024-12-13 04:23:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 4.0 |
| cac057d4-593e-3da9-9bbe-eb481a300e10 | -12.35273 | -44.71518 | 2024-12-13 04:23:00 | NPP-375D | CATOLÂNDIA | BAHIA | Brasil | 2907400 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 307225a0-eb27-3d53-a8ef-1651840b0552 | -13.23551 | -48.2392 | 2024-12-13 04:23:00 | NPP-375D | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 4dead396-deef-3f89-bbde-6fd1196cba54 | -13.69546 | -54.76546 | 2024-12-13 04:23:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 5516d55c-c1f5-3a49-b7fe-418618661b2a | -14.74459 | -52.64885 | 2024-12-13 04:23:00 | NPP-375D | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 18f48196-c643-3f16-ab3c-c053d6ea187f | -14.77079 | -52.64996 | 2024-12-13 04:23:00 | NPP-375D | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 9d0d7105-8b26-3ddc-ac0c-67c937a59a5b | -10.64683 | -51.66227 | 2024-12-13 04:23:00 | NPP-375D | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e48aa4ec-cc1a-3bc9-9426-461630a00cb3 | -13.5394 | -55.38086 | 2024-12-13 04:23:00 | NPP-375D | SANTA RITA DO TRIVELATO | MATO GROSSO | Brasil | 5107768 | 51 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 84a57365-dc7b-3b62-96d0-e1f6c18ca2a5 | -11.36782 | -49.24772 | 2024-12-13 04:23:00 | NPP-375D | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 236b1c84-be67-354a-bc0a-17c1a43c9f6b | -13.70043 | -54.76649 | 2024-12-13 04:23:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 4fd4a449-9dc2-3399-ac70-60ac82446467 | -11.4249 | -55.91967 | 2024-12-13 04:23:00 | NPP-375D | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d9a7ca06-5bad-30c5-bc72-c9b87397438b | -14.77429 | -52.65496 | 2024-12-13 04:23:00 | NPP-375D | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 5.7 |
| e9f9da48-81d3-3240-a0a0-1760668694e9 | -11.8774 | -47.05395 | 2024-12-13 04:23:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 4b84fdf0-d6f7-3459-8c14-cca9242b0fde | -11.88075 | -47.05451 | 2024-12-13 04:23:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 924a307e-6926-3908-8990-5d6d9f1b32fd | -12.85717 | -45.67657 | 2024-12-13 04:23:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 5c4559e3-7f84-352b-9aeb-250a91ac2dc9 | -11.43605 | -55.92202 | 2024-12-13 04:23:00 | NPP-375D | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 0819c61d-610e-3105-9994-a88d2e056739 | -12.10611 | -44.75604 | 2024-12-13 04:23:00 | NPP-375D | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 51d8906c-a3f5-3c8f-9fec-16c05d24bf8a | -14.77203 | -52.65708 | 2024-12-13 04:23:00 | NPP-375D | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 4.7 |
| b0c3cf26-d63c-36dd-a2ac-02dddbe18056 | -14.76932 | -52.65809 | 2024-12-13 04:23:00 | NPP-375D | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 5.7 |
| d084432a-1935-3ddd-8255-355e3ff357bf | -11.44234 | -55.9194 | 2024-12-13 04:23:00 | NPP-375D | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 7ce1b257-7f9e-3909-adb7-be01c5b1fc51 | -13.06988 | -52.03855 | 2024-12-13 04:23:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 80524d90-c76a-3897-a236-0dd277951f2b | -12.28383 | -45.49729 | 2024-12-13 04:23:00 | NPP-375D | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| e18a9dc9-998b-340a-855f-1a91a528f032 | -14.77723 | -52.63861 | 2024-12-13 04:23:00 | NPP-375D | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 6.4 |
| d824bfbe-308a-3ce5-b02b-f314ae68f1af | -13.05304 | -52.03551 | 2024-12-13 04:23:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 8f1920fe-a977-3c16-a061-e3b767e24058 | -12.02044 | -49.5443 | 2024-12-13 04:23:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 8f7052d3-189a-3297-b728-19e446f7cd5b | -12.76567 | -49.31192 | 2024-12-13 04:23:00 | NPP-375D | TALISMÃ | TOCANTINS | Brasil | 1720978 | 17 | 33 | nan | nan | nan | Cerrado | 4.4 |
| f87bafb6-02ce-3bf7-ae84-d96e579bf3f9 | -12.45716 | -46.94648 | 2024-12-13 04:23:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 23e3113a-95e3-3744-9dc1-d35fea507d4f | -11.43556 | -55.89425 | 2024-12-13 04:23:00 | NPP-375D | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 45b42ad4-7a8a-3980-9772-7bb44bd82978 | -11.43047 | -55.92084 | 2024-12-13 04:23:00 | NPP-375D | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d3303d99-033e-3d08-b32b-c058b0c18b11 | -11.20107 | -53.83006 | 2024-12-13 04:23:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 11.7 |
| 0c2ba957-e1f4-384f-bb16-3b7e714d3d3c | -11.20567 | -53.81554 | 2024-12-13 04:23:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 8ddc03fe-53d0-345c-98aa-6f6798a575c5 | -12.65835 | -46.57726 | 2024-12-13 04:23:00 | NPP-375D | AURORA DO TOCANTINS | TOCANTINS | Brasil | 1702703 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| a7d19da6-d6aa-3334-9587-9036418ba4e4 | -14.78279 | -52.64669 | 2024-12-13 04:23:00 | NPP-375D | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 1dca8ee8-7af1-31da-944b-7e1b90b3e54b | -12.38086 | -51.45338 | 2024-12-13 04:23:00 | NPP-375D | BOM JESUS DO ARAGUAIA | MATO GROSSO | Brasil | 5101852 | 51 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 65aa1b9b-b83a-3daf-b22c-254332f79f3c | -14.77356 | -52.64897 | 2024-12-13 04:23:00 | NPP-375D | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 9a223e15-d410-3f5e-a205-99953b9f09d4 | -14.76802 | -52.64095 | 2024-12-13 04:23:00 | NPP-375D | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 6.4 |
| b0259493-6533-3da7-b8ea-ab7c4af67fea | -13.07551 | -52.03153 | 2024-12-13 04:23:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 5b57849b-93b4-343c-861d-c7a7845233e0 | -11.68913 | -48.07421 | 2024-12-13 04:23:00 | NPP-375D | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 29d10c12-6595-39d9-b477-222643981d54 | -14.76511 | -52.65702 | 2024-12-13 04:23:00 | NPP-375D | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| af00da28-5792-3c17-a63f-afef114b6a9f | -13.05304 | -52.03645 | 2024-12-13 04:23:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 29452f7d-83b9-3f11-9e28-d33edb4bea43 | -12.74876 | -48.3474 | 2024-12-13 04:23:00 | NPP-375D | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 2f9af2ae-ee70-38b7-956a-bcee50eb04ab | -13.37167 | -54.24544 | 2024-12-13 04:23:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 5d9bb093-b4f2-3f65-854d-670ea04fc259 | -11.4906 | -48.20126 | 2024-12-13 04:23:00 | NPP-375D | SANTA ROSA DO TOCANTINS | TOCANTINS | Brasil | 1718907 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 16b776c7-ce6f-3282-8179-941e1363d9bb | -12.41359 | -43.80223 | 2024-12-13 04:23:00 | NPP-375D | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| e90f055c-1adf-35bc-ba40-55580594b2d5 | -14.77575 | -52.64683 | 2024-12-13 04:23:00 | NPP-375D | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 5.3 |
| f16ca7ab-1886-3914-b622-7262f508b31b | -11.21087 | -53.83183 | 2024-12-13 04:23:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 5.9 |
| cd942e9f-296a-35f8-ab1f-d560aa975501 | -11.68567 | -48.07362 | 2024-12-13 04:23:00 | NPP-375D | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| a2f77c8d-9a5e-3c9f-b3e2-990c933ee815 | -11.15977 | -49.44035 | 2024-12-13 04:23:00 | NPP-375D | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 4b8f90d5-58c3-3fda-bb22-2a2844dd0ba0 | -11.19974 | -53.82011 | 2024-12-13 04:23:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 8.8 |
| 9d1ddadd-f968-3790-8992-39eccde2d341 | -12.42488 | -46.6411 | 2024-12-13 04:23:00 | NPP-375D | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 351c5923-a90c-3238-af83-1cd30787d0f3 | -10.29505 | -53.7022 | 2024-12-13 04:23:00 | NPP-375D | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| d3197e17-b9f8-3462-acfe-a7f627151bc6 | -13.05726 | -52.03626 | 2024-12-13 04:23:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Amazônia | 4.2 |
| ca573cce-3ff1-3fe6-ab14-66a4da8afde9 | -14.76451 | -52.63603 | 2024-12-13 04:23:00 | NPP-375D | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 9617d94e-6a2f-3720-9bd8-825a23a422e2 | -13.69654 | -54.75981 | 2024-12-13 04:23:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | 3.5 |


[Clique aqui para ver as próximas entradas](README22.md)
